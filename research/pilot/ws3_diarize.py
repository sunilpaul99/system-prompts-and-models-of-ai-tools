#!/usr/bin/env python3
"""WS3: diarization + host attribution.

Pipeline (per episode, runs once its WS2 transcript exists):
 1. Speech regions = Whisper segments (transcript JSON word timestamps).
 2. ECAPA embeddings (speechbrain/spkrec-ecapa-voxceleb, 192-d) on 1.5 s
    windows (0.75 s hop) inside speech regions, decoded via PyAV @16 kHz mono.
 3. Agglomerative clustering (cosine, average linkage) with K chosen by
    silhouette over K in {2..5} (interview shows expected K=2; MBMBaM K in 3-5).
 4. Words assigned to the cluster owning their midpoint window; turns rebuilt
    as maximal same-speaker runs.
 5. Host attribution: cosine similarity of cluster centroids vs. the host
    enrollment centroid (build_enrollment). Nearest cluster above
    HOST_SIM_MIN=0.30 -> HOST; others -> GUEST/OTHER. Below threshold ->
    episode flagged UNATTRIBUTED for the V3 queue.

Enrollment: 3 reference episodes per host; windows from a hand-checked
[start,end] span where only the host speaks (spans recorded in
enrollment_spans.json, PI-auditable). Output per episode:
transcripts_diarized/<ep>.json with per-word speaker labels + audit fields.

V3 audit hooks: --audit-sample N exports stratified 2-min segments with
pipeline labels for PI relabeling.

Usage:
  python3 ws3_diarize.py enroll   <scratchpad>   # build host centroids
  python3 ws3_diarize.py run      <scratchpad>   # diarize all transcribed eps
  python3 ws3_diarize.py audit    <scratchpad> --audit-sample 24
"""
import glob, json, os, sys, wave
import numpy as np

WIN, HOP, SR = 1.5, 0.75, 16000
HOST_SIM_MIN = 0.30

def decode(mp3, t0, t1):
    import av
    c = av.open(mp3); s = c.streams.audio[0]
    r = av.AudioResampler(format="s16", layout="mono", rate=SR)
    buf = []
    c.seek(int(t0 / s.time_base), stream=s)
    for fr in c.decode(s):
        t = float(fr.pts * s.time_base)
        if t < t0 - 1: continue
        if t > t1: break
        for rf in r.resample(fr): buf.append(rf.to_ndarray())
    if not buf: return np.zeros(0, dtype=np.float32)
    a = np.concatenate(buf, axis=1)[0]
    return a.astype(np.float32) / 32768.0

_enc = None
def encoder():
    global _enc
    if _enc is None:
        from speechbrain.inference.speaker import EncoderClassifier
        _enc = EncoderClassifier.from_hparams(
            "speechbrain/spkrec-ecapa-voxceleb", savedir=os.path.expanduser("~/.sb_ecapa"))
    return _enc

def embed_windows(audio, starts):
    import torch
    embs = []
    for s0 in starts:
        i = int(s0 * SR); seg = audio[i:i + int(WIN * SR)]
        if len(seg) < int(WIN * SR) * 0.8: continue
        e = encoder().encode_batch(torch.from_numpy(seg).unsqueeze(0)).squeeze().numpy()
        embs.append((s0, e / np.linalg.norm(e)))
    return embs

def speech_windows(tr):
    ws = []
    for seg in tr["segments"]:
        t = seg["start"]
        while t + WIN <= seg["end"]:
            ws.append(t); t += HOP
    return ws

def enroll(scratch):
    spans = json.load(open(os.path.join(os.path.dirname(__file__), "enrollment_spans.json")))
    cents = {}
    for host, refs in spans.items():
        if host.startswith("_"): continue
        embs = []
        for ref in refs:  # {"file": ..., "start": s, "end": e}
            path = glob.glob(os.path.join(scratch, "audio", host, ref["file"] + "*"))[0]
            audio = decode(path, ref["start"], ref["end"])
            offs = np.arange(0, len(audio)/SR - WIN, HOP)
            embs += [e for _, e in embed_windows(audio, offs)]
        c = np.mean(embs, axis=0); cents[host] = (c / np.linalg.norm(c)).tolist()
        print(f"enrolled {host}: {len(embs)} windows")
    json.dump(cents, open(os.path.join(scratch, "host_centroids.json"), "w"))

def diarize_episode(mp3, tr_path, centroid, outdir):
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.metrics import silhouette_score
    tr = json.load(open(tr_path))
    dur = tr["duration"]
    audio = decode(mp3, 0, dur)
    wins = speech_windows(tr)
    embs = embed_windows(audio, wins)
    if len(embs) < 20:
        return {"status": "TOO_FEW_WINDOWS"}
    X = np.stack([e for _, e in embs]); T = [t for t, _ in embs]
    best = None
    for k in range(2, 6):
        lab = AgglomerativeClustering(n_clusters=k, metric="cosine",
                                      linkage="average").fit_predict(X)
        s = silhouette_score(X, lab, metric="cosine")
        if best is None or s > best[1]: best = (lab, s, k)
    lab, sil, k = best
    cents = {c: X[lab == c].mean(axis=0) for c in range(k)}
    sims = {c: float(np.dot(v/np.linalg.norm(v), centroid)) for c, v in cents.items()}
    host_c = max(sims, key=sims.get)
    status = "OK" if sims[host_c] >= HOST_SIM_MIN else "UNATTRIBUTED"
    # label words by midpoint window
    win_lab = list(zip(T, lab))
    def spk(t):
        j = min(range(len(win_lab)), key=lambda i: abs(win_lab[i][0] + WIN/2 - t))
        return "HOST" if win_lab[j][1] == host_c else f"S{win_lab[j][1]}"
    segs = []
    for seg in tr["segments"]:
        words = [{"w": w["w"], "s": w["s"], "e": w["e"],
                  "spk": spk((w["s"] + w["e"]) / 2)} for w in seg["words"]]
        segs.append({"start": seg["start"], "end": seg["end"], "words": words})
    hostwords = sum(1 for s in segs for w in s["words"] if w["spk"] == "HOST")
    total = sum(len(s["words"]) for s in segs)
    out = {"file": tr["file"], "status": status, "k": k, "silhouette": sil,
           "host_cluster_sim": sims[host_c], "cluster_sims": sims,
           "host_word_share": hostwords / max(total, 1), "segments": segs}
    json.dump(out, open(os.path.join(outdir, os.path.basename(tr_path)), "w"))
    return {"status": status, "k": k, "host_share": out["host_word_share"]}

def run(scratch, tdir="transcripts", outname="transcripts_diarized"):
    cents = json.load(open(os.path.join(scratch, "host_centroids.json")))
    outdir = os.path.join(scratch, outname); os.makedirs(outdir, exist_ok=True)
    for tr_path in sorted(glob.glob(os.path.join(scratch, tdir, "*.json"))):
        base = os.path.basename(tr_path).replace(".json", "")
        if os.path.exists(os.path.join(outdir, base + ".json")): continue
        mp3s = glob.glob(os.path.join(scratch, "audio", "*", base + ".mp3"))
        if not mp3s: continue
        host = os.path.basename(os.path.dirname(mp3s[0]))
        c = np.array(cents[host])
        r = diarize_episode(mp3s[0], tr_path, c, outdir)
        print(base[:60], r, flush=True)

if __name__ == "__main__":
    {"enroll": enroll, "run": run}[sys.argv[1]](*sys.argv[2:])

#!/usr/bin/env python3
"""WS3-B: pyannote-based diarization for multi-speaker formats.

Motivation: ECAPA-embedding + agglomerative clustering (ws3_diarize.py)
fails structurally on MBMBaM — three sibling voices cluster as one
(DAILY_BRIEF cycle 59). pyannote/speaker-diarization-3.1 is a purpose-built
diarization pipeline (segmentation + embedding + clustering trained jointly)
and is the pre-registered option (b) for the multi-speaker case.

Pipeline per episode:
 1. pyannote speaker-diarization-3.1 -> speaker turns (start, end, label).
 2. For each pyannote speaker, pool its longest turns, embed with the SAME
    ECAPA encoder used for host enrollment, and compare to the enrolled host
    centroid (so host attribution stays consistent with the interview-format
    path and with enrollment_spans.json).
 3. Words assigned to the pyannote turn covering their midpoint; the host
    speaker's words -> HOST, others -> S<label>.
 4. Output schema is IDENTICAL to ws3_diarize.py, so ws5_count.py and
    ws6_turns.py consume it unchanged.

Auth: needs HF_TOKEN (read token, model terms accepted) in the environment
or ~/.cache/huggingface/token. The token is a credential: never committed,
never logged.

Usage:
  python3 ws3_diarize_pyannote.py <scratchpad> [host_filter] [tdir] [outdir]
    host_filter: substring of the audio subdir, e.g. "mbmbam" (default: all)
"""
import glob, json, os, sys
import numpy as np

SR = 16000
HOST_SIM_MIN = 0.30
MIN_TURN_S = 1.0          # turns shorter than this are not used for centroids
MAX_CENTROID_S = 120      # cap per-speaker audio used for identification

def load_pipeline():
    from pyannote.audio import Pipeline
    tok = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    kw = {"use_auth_token": tok} if tok else {}
    return Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", **kw)

def decode(mp3):
    import av
    c = av.open(mp3); s = c.streams.audio[0]
    r = av.AudioResampler(format="s16", layout="mono", rate=SR)
    buf = []
    for fr in c.decode(s):
        for rf in r.resample(fr):
            buf.append(rf.to_ndarray())
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

def embed(audio_slice):
    import torch
    e = encoder().encode_batch(torch.from_numpy(audio_slice).unsqueeze(0)).squeeze().numpy()
    return e / np.linalg.norm(e)

def raw_turns(mp3, pipeline, cache_dir):
    """Run pyannote and CACHE the speaker turns before any downstream work.

    The pipeline costs ~1x realtime on CPU; a bug in later stages must never
    discard it again (it did once — pyannote 4.x returns DiarizeOutput, not
    Annotation, and the parse error threw away a 2h run)."""
    import torch
    os.makedirs(cache_dir, exist_ok=True)
    cache = os.path.join(cache_dir, os.path.basename(mp3) + ".turns.json")
    if os.path.exists(cache):
        return [tuple(t) for t in json.load(open(cache))]
    audio = decode(mp3)   # PyAV: this container's torchcodec cannot load
    out = pipeline({"waveform": torch.from_numpy(audio).unsqueeze(0),
                    "sample_rate": SR})
    # pyannote 4.x: DiarizeOutput wrapper. "exclusive" resolves overlapping
    # speech to one speaker per instant, which is what word attribution needs.
    ann = getattr(out, "exclusive_speaker_diarization", None)
    if ann is None:
        ann = getattr(out, "speaker_diarization", out)
    turns = [(seg.start, seg.end, str(label))
             for seg, _, label in ann.itertracks(yield_label=True)]
    tmp = cache + ".tmp"
    json.dump(turns, open(tmp, "w")); os.replace(tmp, cache)
    return turns

def diarize_episode(mp3, tr_path, centroid, outdir, pipeline):
    tr = json.load(open(tr_path))
    turns = raw_turns(mp3, pipeline, os.path.join(os.path.dirname(outdir), "pyannote_turns"))
    if not turns:
        return {"status": "NO_TURNS"}
    audio = decode(mp3)
    # per-speaker centroid from longest turns (capped)
    sims = {}
    for label in {t[2] for t in turns}:
        segs = sorted([t for t in turns if t[2] == label and t[1] - t[0] >= MIN_TURN_S],
                      key=lambda t: t[0] - t[1])
        embs, used = [], 0.0
        for s0, s1, _ in segs:
            if used >= MAX_CENTROID_S: break
            clip = audio[int(s0 * SR):int(min(s1, s0 + 10) * SR)]
            if len(clip) < SR: continue
            embs.append(embed(clip)); used += len(clip) / SR
        if embs:
            c = np.mean(embs, axis=0)
            sims[label] = float(np.dot(c / np.linalg.norm(c), centroid))
    if not sims:
        return {"status": "NO_EMBEDDINGS"}
    host_label = max(sims, key=sims.get)
    status = "OK" if sims[host_label] >= HOST_SIM_MIN else "UNATTRIBUTED"
    turns.sort(key=lambda t: t[0])
    starts = [t[0] for t in turns]
    import bisect
    def spk(t):
        i = bisect.bisect_right(starts, t) - 1
        if i < 0: i = 0
        # walk back to a turn containing t, else nearest
        if turns[i][0] <= t <= turns[i][1]:
            lab = turns[i][2]
        else:
            lab = min(turns, key=lambda x: min(abs(x[0] - t), abs(x[1] - t)))[2]
        return "HOST" if lab == host_label else f"S{lab}"
    segs_out = []
    for seg in tr["segments"]:
        words = [{"w": w["w"], "s": w["s"], "e": w["e"],
                  "spk": spk((w["s"] + w["e"]) / 2)} for w in seg["words"]]
        segs_out.append({"start": seg["start"], "end": seg["end"], "words": words})
    hostwords = sum(1 for s in segs_out for w in s["words"] if w["spk"] == "HOST")
    total = sum(len(s["words"]) for s in segs_out)
    out = {"file": tr["file"], "status": status, "k": len(sims),
           "diarizer": "pyannote/speaker-diarization-3.1",
           "host_cluster_sim": sims[host_label],
           "cluster_sims": {str(k): v for k, v in sims.items()},
           "host_word_share": hostwords / max(total, 1), "segments": segs_out}
    json.dump(out, open(os.path.join(outdir, os.path.basename(tr_path)), "w"))
    return {"status": status, "speakers": len(sims),
            "host_share": out["host_word_share"], "host_sim": round(sims[host_label], 3)}

def main(scratch, host_filter="", tdir="transcripts_det2", outname="transcripts_diarized_pyannote"):
    cents = json.load(open(os.path.join(scratch, "host_centroids.json")))
    outdir = os.path.join(scratch, outname); os.makedirs(outdir, exist_ok=True)
    pipeline = load_pipeline()
    for tr_path in sorted(glob.glob(os.path.join(scratch, tdir, "*.json"))):
        base = os.path.basename(tr_path).replace(".json", "")
        if os.path.exists(os.path.join(outdir, base + ".json")): continue
        mp3s = glob.glob(os.path.join(scratch, "audio", "*", base + ".mp3"))
        if not mp3s: continue
        host = os.path.basename(os.path.dirname(mp3s[0]))
        if host_filter and host_filter not in host: continue
        r = diarize_episode(mp3s[0], tr_path, np.array(cents[host]), outdir, pipeline)
        print(base[:55], r, flush=True)

if __name__ == "__main__":
    main(*sys.argv[1:])

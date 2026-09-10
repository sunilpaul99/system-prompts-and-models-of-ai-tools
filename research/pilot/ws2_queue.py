#!/usr/bin/env python3
"""WS2 queue: restart-resilient chunked transcription of the analytic corpus.

Rebuilt 2026-09-11 (original was scratchpad-only and lost). The design is
the one that survived ~25 container restarts in the pilot (WS8 §3):

  * work unit = one 25-min chunk (« restart interval)
  * atomic claims via mkdir(claims/<base>__<idx>) — a mkdir either succeeds
    or raises; two workers cannot both win
  * per-chunk checkpoint files written by atomic rename
  * launch-time reconciliation: claims without an output file are stale
    (their worker died) and are cleared
  * completion = COUNT OUTPUT FILES against the expected chunk count, never
    trust process exit codes
  * per-chunk hard timeout at 3x realtime; on timeout re-run with
    --no-context (loop guard [B2]) and flag it
  * one full audio decode per episode (int16 @16 kHz, PyAV), cached on
    disk as a memmap, deleted once the episode is assembled

Assembly: when every chunk of an episode exists, merge into
transcripts/<base>.json in the exact schema ws3_diarize / ws5_count /
ws6_turns consume: {file, duration, config, segments:[{start,end,words}],
loopguard_chunks:[...]}.

Usage:
  ws2_queue.py decode   <scratch>              # decode all audio (one-off)
  ws2_queue.py worker   <scratch> <worker_id>  # run forever until queue empty
  ws2_queue.py assemble <scratch>              # merge complete episodes
  ws2_queue.py status   <scratch>
"""
import glob, json, os, subprocess, sys, time

import numpy as np

SR = 16000
CHUNK_S = 1500
TIMEOUT_FACTOR = 3.0
HERE = os.path.dirname(os.path.abspath(__file__))
WORKER = os.path.join(HERE, "ws2_chunk_worker.py")


def episodes(scratch):
    """(base, host, mp3_path) for every episode in the rebuild list."""
    lst = json.load(open(os.path.join(scratch, "rebuild_30.json")))
    out = []
    for e in lst:
        mp3 = os.path.join(scratch, "audio", e["host"], e["base"] + ".mp3")
        if os.path.exists(mp3):
            out.append((e["base"], e["host"], mp3))
    return out


def decode_full(mp3):
    """Whole file -> int16 mono 16 kHz. PyAV; verified bit-identical in WS2."""
    import av
    c = av.open(mp3); s = c.streams.audio[0]
    r = av.AudioResampler(format="s16", layout="mono", rate=SR)
    buf = []
    for fr in c.decode(s):
        for rf in r.resample(fr):
            buf.append(rf.to_ndarray()[0])
    for rf in r.resample(None):          # flush resampler
        buf.append(rf.to_ndarray()[0])
    return np.concatenate(buf).astype(np.int16)


def decode(scratch):
    d = os.path.join(scratch, "decoded"); os.makedirs(d, exist_ok=True)
    for base, host, mp3 in episodes(scratch):
        dest = os.path.join(d, base + ".npy")
        if os.path.exists(dest) or os.path.exists(os.path.join(scratch, "transcripts", base + ".json")):
            continue
        a = decode_full(mp3)
        np.save(dest + ".tmp.npy", a); os.replace(dest + ".tmp.npy", dest)
        json.dump({"samples": int(len(a)), "duration": len(a) / SR,
                   "n_chunks": int(np.ceil(len(a) / SR / CHUNK_S))},
                  open(os.path.join(d, base + ".meta.json"), "w"))
        print(f"decoded {base[:50]} {len(a)/SR/3600:.2f} h -> "
              f"{int(np.ceil(len(a)/SR/CHUNK_S))} chunks", flush=True)


def meta(scratch, base):
    p = os.path.join(scratch, "decoded", base + ".meta.json")
    return json.load(open(p)) if os.path.exists(p) else None


def pending_chunks(scratch):
    """All (base, idx) with no output file, shortest episodes first so
    complete episodes flow to diarization early."""
    items = []
    for base, host, mp3 in episodes(scratch):
        if os.path.exists(os.path.join(scratch, "transcripts", base + ".json")):
            continue
        m = meta(scratch, base)
        if not m:
            continue
        for i in range(m["n_chunks"]):
            if not os.path.exists(os.path.join(scratch, "chunks", base, f"{i:03}.json")):
                items.append((m["n_chunks"], base, i))
    items.sort()
    return [(b, i) for _, b, i in items]


def _alive(pid):
    try:
        os.kill(pid, 0); return True
    except (ProcessLookupError, PermissionError, ValueError):
        return False


def reconcile(scratch):
    """Clear claims whose owner is dead and whose output never appeared.

    A claim records its owner's PID. A live owner with no output yet is
    simply in flight — the first rebuild treated those as stale and three
    workers converged on one chunk. After a container restart every old
    PID is dead, so those claims clear as intended."""
    n = 0
    for c in glob.glob(os.path.join(scratch, "claims", "*")):
        base, idx = os.path.basename(c).rsplit("__", 1)
        if os.path.exists(os.path.join(scratch, "chunks", base, f"{int(idx):03}.json")):
            continue
        try:
            pid = int(open(os.path.join(c, "pid")).read())
        except (FileNotFoundError, ValueError):
            pid = -1
        if not _alive(pid):
            for f in glob.glob(os.path.join(c, "*")):
                os.remove(f)
            os.rmdir(c); n += 1
    return n


def claim(scratch, base, idx):
    os.makedirs(os.path.join(scratch, "claims"), exist_ok=True)
    d = os.path.join(scratch, "claims", f"{base}__{idx}")
    try:
        os.mkdir(d)
    except FileExistsError:
        return False
    with open(os.path.join(d, "pid"), "w") as f:
        f.write(str(os.getpid()))
    return True


def run_chunk(scratch, base, idx, log):
    m = meta(scratch, base)
    audio_s = min(CHUNK_S, m["duration"] - idx * CHUNK_S)
    timeout = max(600, TIMEOUT_FACTOR * audio_s)
    env = dict(os.environ, OMP_NUM_THREADS="1")
    for flags in ([], ["--no-context"]):
        t = time.time()
        try:
            subprocess.run([sys.executable, WORKER, scratch, base, str(idx)] + flags,
                           timeout=timeout, env=env, stdout=log, stderr=log, check=True)
            return True
        except subprocess.TimeoutExpired:
            print(f"  TIMEOUT {base[:40]} #{idx} after {time.time()-t:.0f}s"
                  f"{' -> retry no-context' if not flags else ' even without context'}",
                  flush=True)
        except subprocess.CalledProcessError as e:
            print(f"  FAILED {base[:40]} #{idx} rc={e.returncode}", flush=True)
            return False
    return False


def worker(scratch, wid):
    log = open(os.path.join(scratch, f"worker{wid}.log"), "a")
    print(f"[w{wid}] reconciled {reconcile(scratch)} stale claims", flush=True)
    idle = 0
    while True:
        todo = [(b, i) for b, i in pending_chunks(scratch)
                if not os.path.exists(os.path.join(scratch, "claims", f"{b}__{i}"))]
        if not todo:
            assemble(scratch)
            if not pending_chunks(scratch):
                print(f"[w{wid}] queue empty, exiting", flush=True); return
            idle += 1; time.sleep(30); continue
        for base, idx in todo:
            if claim(scratch, base, idx):
                print(f"[w{wid}] {base[:40]} #{idx}", flush=True)
                run_chunk(scratch, base, idx, log)
                assemble(scratch, only=base)
                break


def assemble(scratch, only=None):
    tdir = os.path.join(scratch, "transcripts"); os.makedirs(tdir, exist_ok=True)
    for base, host, mp3 in episodes(scratch):
        if only and base != only:
            continue
        dest = os.path.join(tdir, base + ".json")
        if os.path.exists(dest):
            continue
        m = meta(scratch, base)
        if not m:
            continue
        paths = [os.path.join(scratch, "chunks", base, f"{i:03}.json") for i in range(m["n_chunks"])]
        if not all(os.path.exists(p) for p in paths):
            continue
        segs, flagged, cfg = [], [], None
        for p in paths:
            c = json.load(open(p))
            segs += c["segments"]
            cfg = cfg or c.get("config")
            if c.get("loopguard_no_context"):
                flagged.append(c["idx"])
        out = {"file": base + ".mp3", "duration": m["duration"], "config": cfg,
               "n_chunks": m["n_chunks"], "loopguard_chunks": flagged, "segments": segs}
        tmp = dest + ".tmp"; json.dump(out, open(tmp, "w")); os.replace(tmp, dest)
        words = sum(len(s["words"]) for s in segs)
        print(f"ASSEMBLED {base[:50]} {words:,} words"
              f"{' loopguard:'+str(flagged) if flagged else ''}", flush=True)
        npy = os.path.join(scratch, "decoded", base + ".npy")
        if os.path.exists(npy):
            os.remove(npy)


def status(scratch):
    done = len(glob.glob(os.path.join(scratch, "transcripts", "*.json")))
    pend = pending_chunks(scratch)
    chunks_done = len(glob.glob(os.path.join(scratch, "chunks", "*", "*.json")))
    print(f"episodes assembled: {done}/30 | chunks done: {chunks_done} | chunks pending: {len(pend)}")


if __name__ == "__main__":
    {"decode": decode, "worker": worker, "assemble": assemble,
     "status": status}[sys.argv[1]](*sys.argv[2:])

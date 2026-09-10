#!/usr/bin/env python3
"""WS2 chunk worker: transcribe ONE 25-minute chunk under the pinned config.

Rebuilt 2026-09-11 after the container reclaim destroyed the original
(scratchpad-only) worker. Lives in the repo now.

PINNED CONFIG (PROTOCOL §6 [B1]):
    faster-whisper-1.2.1/medium/int8/threads1/temp0/beam5/chunk1500
    OMP_NUM_THREADS=1, cpu_threads=1, num_workers=1, Silero VAD on.

Why one chunk per PROCESS: (1) memory isolation — each worker holds the
model plus one chunk, never a 4-hour episode; (2) the loop guard [B2]. A
deterministic decode has no repetition-escape ladder, so a chunk can stall
inside a single decode call where no in-process guard can fire. The queue
runs this script under a hard wall-clock timeout (~3x realtime) and, on
timeout, re-runs it with --no-context, which sets
condition_on_previous_text=False and marks the chunk `loopguard_no_context`.

Audio: the queue pre-decodes each episode ONCE to int16 @16 kHz mono
(PyAV, bit-identical across runs) as decoded/<base>.npy; this script slices
its [t0, t1) window from that memmap. Slicing a full decode — rather than
seeking the mp3 per chunk — is what makes chunk boundaries reproducible.

Usage: ws2_chunk_worker.py <scratch> <base> <chunk_idx> [--no-context]
Writes: <scratch>/chunks/<base>/<idx:03>.json  (atomic via .tmp rename)
"""
import json, os, sys, time

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

SR = 16000
CHUNK_S = 1500
MODEL, COMPUTE = "medium", "int8"
CONFIG = f"faster-whisper-1.2.1/{MODEL}/{COMPUTE}/threads1/temp0/beam5/chunk{CHUNK_S}"


def main(scratch, base, idx, *flags):
    idx = int(idx)
    no_context = "--no-context" in flags
    out_dir = os.path.join(scratch, "chunks", base)
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, f"{idx:03}.json")
    if os.path.exists(dest):
        print(f"exists {base[:40]} #{idx}"); return

    audio = np.load(os.path.join(scratch, "decoded", base + ".npy"), mmap_mode="r")
    t0 = idx * CHUNK_S
    seg = np.asarray(audio[t0 * SR:(t0 + CHUNK_S) * SR], dtype=np.float32) / 32768.0
    if len(seg) == 0:
        json.dump({"idx": idx, "t0": t0, "segments": [], "empty": True},
                  open(dest, "w")); return

    from faster_whisper import WhisperModel
    t_start = time.time()
    model = WhisperModel(MODEL, device="cpu", compute_type=COMPUTE,
                         cpu_threads=1, num_workers=1)
    segments, info = model.transcribe(
        seg, language="en", beam_size=5, temperature=[0.0],
        condition_on_previous_text=not no_context,
        word_timestamps=True, vad_filter=True)
    out = []
    for s in segments:
        out.append({"start": round(s.start + t0, 3), "end": round(s.end + t0, 3),
                    "words": [{"w": w.word, "s": round(w.start + t0, 3),
                               "e": round(w.end + t0, 3)} for w in (s.words or [])]})
    rec = {"idx": idx, "t0": t0, "config": CONFIG, "segments": out,
           "loopguard_no_context": no_context,
           "wall_s": round(time.time() - t_start, 1),
           "audio_s": round(len(seg) / SR, 1)}
    tmp = dest + ".tmp"
    json.dump(rec, open(tmp, "w")); os.replace(tmp, dest)
    print(f"done {base[:40]} #{idx} {len(out)} segs "
          f"{rec['wall_s']:.0f}s wall / {rec['audio_s']:.0f}s audio"
          f"{' [no-context]' if no_context else ''}")


if __name__ == "__main__":
    main(*sys.argv[1:])

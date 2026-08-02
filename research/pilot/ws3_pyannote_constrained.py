"""WS3-B experiment: does constraining the speaker count fix MBMBaM segmentation?

Design: PAIRED comparison. Re-run the SAME episodes that failed unconstrained
(62/31 and 65/32 two-way splits) with num_speakers fixed, and compare word
shares against their unconstrained results. Episode 455 (which already split
correctly at 39/33/23) is the control — the constraint must not break it.

Why constraining is principled here and not fitting-to-result: MBMBaM studio
episodes have a KNOWN cast (three brothers), and the unconstrained runs detect
9-14 speakers, i.e. the failure mode is over-segmentation, not under. The
constraint encodes prior knowledge about the show, not a preference about the
answer. Declared in Appendix A if adopted; applies ONLY to formats whose cast
is known and fixed.

Writes to pyannote_turns_k<N>/ and transcripts_diarized_pyannote_k<N>/ so the
unconstrained results stay intact for comparison.
"""
import json, os, sys, glob
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ws3_diarize_pyannote as base

def turns_constrained(mp3, pipeline, cache_dir, n_speakers):
    import torch
    os.makedirs(cache_dir, exist_ok=True)
    cache = os.path.join(cache_dir, os.path.basename(mp3) + f".turns.json")
    if os.path.exists(cache):
        return [tuple(t) for t in json.load(open(cache))]
    audio = base.decode(mp3)
    out = pipeline({"waveform": torch.from_numpy(audio).unsqueeze(0),
                    "sample_rate": base.SR}, num_speakers=n_speakers)
    ann = getattr(out, "exclusive_speaker_diarization", None) or \
          getattr(out, "speaker_diarization", out)
    turns = [(seg.start, seg.end, str(label))
             for seg, _, label in ann.itertracks(yield_label=True)]
    tmp = cache + ".tmp"; json.dump(turns, open(tmp, "w")); os.replace(tmp, cache)
    return turns

def main(scratch, n_speakers="3", *episodes):
    n = int(n_speakers)
    cents = json.load(open(os.path.join(scratch, "host_centroids.json")))
    outdir = os.path.join(scratch, f"transcripts_diarized_pyannote_k{n}")
    os.makedirs(outdir, exist_ok=True)
    cache_dir = os.path.join(scratch, f"pyannote_turns_k{n}")
    pipeline = base.load_pipeline()
    # monkey-patch the turn source so the rest of the attribution logic is
    # byte-identical to the unconstrained path (only segmentation differs)
    base.raw_turns = lambda mp3, pl, cd: turns_constrained(mp3, pl, cache_dir, n)
    for pat in episodes:
        for tr_path in sorted(glob.glob(os.path.join(scratch, "transcripts_det2", f"*{pat}*.json"))):
            b = os.path.basename(tr_path).replace(".json", "")
            if os.path.exists(os.path.join(outdir, b + ".json")): continue
            mp3s = glob.glob(os.path.join(scratch, "audio", "*", b + ".mp3"))
            if not mp3s: continue
            host = os.path.basename(os.path.dirname(mp3s[0]))
            r = base.diarize_episode(mp3s[0], tr_path, np.array(cents[host]), outdir, pipeline)
            print(f"k={n} {b[:45]} {r}", flush=True)

if __name__ == "__main__":
    main(*sys.argv[1:])

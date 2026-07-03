"""VL-B study-parity check (axis-2 foundation build, CC 2026-07-03).

The axis-2 analogue of the music21<->L1/L2 neutral-extractor cross-check (spec
cowork_voiceleading_axis_design.md §5.2 parity duty, §10). It runs
`batch_analyze --dump-vl` on a pinned RESEARCH-TIER sample, then feeds the DUMPED
per-line (onset, top-pitch) tuples (`reducedLines`) through the STUDY's OWN feature
functions — voiceleading.py `vl_profile` (View A / interval) and voiceleading2.py
`vl_profile_B` (View B / motion) — and diffs the result against the C++ profiles the
dump reports.

This tests the feature ARITHMETIC on IDENTICAL input (the dumped tuples). Ingestion
differences (how each side reads the score into voices) are OUT OF SCOPE by design —
both sides operate on the same reducedLines, so any mismatch is a real arithmetic
divergence. Rates are integer count/total ratios, so float-EXACT parity is expected;
the declared tolerance is 1e-9 (a guard against representation noise, never observed).

Usage:  .venv/Scripts/python.exe tools/compare_vl_parity.py
            [--batch-analyze ninja_build_rel/batch_analyze.exe] [SCORE ...]
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "idiom_discovery"))
import numpy as np
from parsers.voiceleading import vl_profile           # View A (unchanged pilot feature)
from parsers.voiceleading2 import vl_profile_B        # View B (motion feature)

TOL = 1e-9

# The pinned research-tier sample (docs/score_inventory.md — DCML corpus scores; the
# do-not-touch gate corpus is not here). ~10 Bach chorales (4-voice contrapuntal) + 5
# keyboard/chamber. Pinned so the parity run is reproducible and reportable.
PINNED = [
    "tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx",
    "tools/dcml/bach_chorales/MS3/002 Ich danke dir, lieber Herre.mscx",
    "tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx",
    "tools/dcml/bach_chorales/MS3/004 Es ist das Heil uns kommen her.mscx",
    "tools/dcml/bach_chorales/MS3/006 Nun lob, mein Seel, den Herren.mscx",
    "tools/dcml/bach_chorales/MS3/007 Christus, der ist mein Leben.mscx",
    "tools/dcml/bach_chorales/MS3/008 Freuet euch, ihr Christen alle.mscx",
    "tools/dcml/bach_chorales/MS3/009 Ermuntre dich, mein schwacher Geist.mscx",
    "tools/dcml/bach_chorales/MS3/010 Aus tiefer Not schrei ich zu dir.mscx",
    "tools/dcml/bach_chorales/MS3/011 Jesu, nun sei gepreiset.mscx",
    "tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx",
    "tools/dcml/mozart_piano_sonatas/MS3/K279-2.mscx",
    "tools/dcml/beethoven_piano_sonatas/MS3/01-1.mscx",
    "tools/dcml/corelli/MS3/op01n01a.mscx",
    "tools/dcml/corelli/MS3/op01n01b.mscx",
]


def dump_vl(batch_analyze, score, out_path):
    completed = subprocess.run(
        [str(batch_analyze), score, str(out_path), "--dump-vl"],
        check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError("batch_analyze --dump-vl failed for %s\n%s" % (score, completed.stderr))
    with open(out_path, encoding="utf-8") as fh:
        return json.load(fh)


def check_one(data):
    """Return (ok, maxDiffA, maxDiffB, note). Feeds reducedLines through the study
    feature functions and diffs vs the dumped C++ profiles."""
    voices_A = [[p for _o, p in ln["onsets"]] for ln in data["reducedLines"]]
    voices_on = [[(o, p) for o, p in ln["onsets"]] for ln in data["reducedLines"]]

    # ── View A (interval) ──
    pyA = vl_profile(voices_A)
    ip = data["intervalProfile"]
    diffA = 0.0
    if ip["defined"]:
        assert pyA is not None, "C++ interval defined but study vl_profile returned None"
        cxxA = np.array(list(ip["hist"]) + [ip["repeat"], ip["step"], ip["leap"]])
        diffA = float(np.max(np.abs(np.array(pyA) - cxxA)))
    else:
        assert pyA is None, "C++ interval undefined but study vl_profile returned a value"

    # ── View B (motion) ──
    pyB = vl_profile_B(voices_on)
    mp = data["motionProfile"]
    diffB = 0.0
    if mp["defined"]:
        assert pyB is not None, "C++ motion defined but study vl_profile_B returned None"
        cxxB = np.array([mp["parallel"], mp["similar"], mp["contrary"], mp["oblique"]])
        diffB = float(np.max(np.abs(np.array(pyB) - cxxB)))
    else:
        assert pyB is None, "C++ motion defined mismatch (study returned a value)"

    ok = diffA <= TOL and diffB <= TOL
    return ok, diffA, diffB


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-analyze",
                    default=os.path.join(REPO, "ninja_build_rel", "batch_analyze.exe"))
    ap.add_argument("scores", nargs="*", help="override the pinned sample")
    args = ap.parse_args()
    scores = args.scores or [os.path.join(REPO, p) for p in PINNED]

    print("VL study-parity check (tol=%g) — %d scores" % (TOL, len(scores)))
    n_ok = n_fail = 0
    worstA = worstB = 0.0
    with tempfile.TemporaryDirectory() as td:
        for i, sc in enumerate(scores):
            out = os.path.join(td, "vl_%d.json" % i)
            try:
                data = dump_vl(args.batch_analyze, sc, out)
                ok, dA, dB = check_one(data)
            except Exception as e:                                    # noqa: BLE001
                print("  FAIL  %-60s %s" % (os.path.basename(sc), e))
                n_fail += 1
                continue
            worstA = max(worstA, dA); worstB = max(worstB, dB)
            tex = data["textureClass"]
            status = "ok  " if ok else "FAIL"
            print("  %s %-52s A=%.2e B=%.2e  texture=%s%s"
                  % (status, os.path.basename(sc)[:52], dA, dB, tex["committed"],
                     "" if not tex["abstained"] else "(abstained:%s)" % tex["reason"]))
            n_ok += 1 if ok else 0
            n_fail += 0 if ok else 1

    print("\n%d ok / %d fail   worst |diff| A=%.2e B=%.2e" % (n_ok, n_fail, worstA, worstB))
    if n_fail:
        sys.exit(1)
    print("PARITY OK — feature arithmetic reproduces the study within tolerance.")


if __name__ == "__main__":
    main()

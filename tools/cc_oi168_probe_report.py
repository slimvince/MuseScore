#!/usr/bin/env python3
"""OI-168 — the reporting side of the default-OFF key-collection probe.

The probe itself lives in src/composing/analysis/chord/keycollectionprobe.{h,cpp} and is driven by
one environment flag, unset in production:

    MU_KEY_COLLECTION_PROBE=1   count the branches; batch_analyze writes <out>.probe.json

The flag is value-less, so a corpus run is just the ordinary tools/run_bach_preset.py with it
exported into the environment — no separate driver, no path rewriting.

HISTORY — the A/B switch this tool was built to drive (MU_KEY_COLLECTION_SIGMASK_VARIANT) is GONE.
It compared the two key-consuming scoring terms' mode-tonic-anchored membership set against the key
signature's own collection. The signature-mask form won and was adopted (cc_oi168_fix_report.md), so
the committed branch it was switching against no longer exists. The subcommands below still work:
`flips` diffs any two corpora and needs no build flag.

Three subcommands:

  byteid  <dir_a> <dir_b>      Every <stem>.ours.json byte-compared (sha256). The inertness proof
                               for a change that must not move the corpus.

  counters <dir> [--label L]   Sum the per-score <stem>.ours.json.probe.json blocks written by the
                               probe, and report the per-score detail for every score whose Altered
                               / AlteredDomBB7 population is non-zero.

  flips   <base_dir> <var_dir> The committed-chord diff between two corpora. Reports every region
                               whose committed chord moved, split by whether the region's local key
                               is an Altered-family mode (the population the OI-168 defect could
                               reach) or not (where the two membership tests are provably the same
                               set, so a flip there would REFUTE the OI-168 derivation).

Usage:
    python tools/cc_oi168_probe_report.py byteid   <dir_a> <dir_b>
    python tools/cc_oi168_probe_report.py counters <dir> [--label L]
    python tools/cc_oi168_probe_report.py flips    <base_dir> <var_dir>
"""
import glob
import hashlib
import json
import os
import sys

# The two modes whose tonic offset differs from their diatonic parent's (OI-168). The region key
# string in .ours.json ends with keyModeSuffix(mode) — "alt" / "altDom" for these two.
DELTA_NONZERO_SUFFIXES = ("alt", "altDom")

COUNTER_FIELDS = [
    "sparseRefineEntries", "sparseGuardShapeMatched", "sparseAeolianGuardFires",
    "analyzeChordCalls", "analyzeChordCallsAltered", "analyzeChordCallsAlteredDomBB7",
    "regionCommitCalls", "regionCommitCallsAltered", "regionCommitCallsAlteredDomBB7",
    "decoderWindowCalls", "decoderWindowCallsAltered", "decoderWindowCallsAlteredDomBB7",
    "dim7MembershipTests", "dim7MembershipDiffers",
    "diatonicRootMembershipTests", "diatonicRootMembershipDiffers",
]


def _stem(path):
    return os.path.basename(path).replace(".ours.json.probe.json", "").replace(".ours.json", "")


def _sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def _delta_nonzero(region):
    return region.get("key", "").endswith(DELTA_NONZERO_SUFFIXES)


def _chord_of(region):
    """The committed chord, as the fields a consumer of .ours.json would read."""
    return (region.get("rootPitchClass"), region.get("quality"), region.get("chordSymbol"),
            region.get("bassPitchClass"), region.get("romanNumeral"))


def cmd_byteid(dir_a, dir_b):
    files_a = sorted(glob.glob(os.path.join(dir_a, "*.ours.json")))
    files_b = {_stem(p) for p in glob.glob(os.path.join(dir_b, "*.ours.json"))}
    identical, differing, missing = 0, [], []
    for pa in files_a:
        stem = _stem(pa)
        pb = os.path.join(dir_b, stem + ".ours.json")
        if stem not in files_b:
            missing.append(stem)
            continue
        if _sha256(pa) == _sha256(pb):
            identical += 1
        else:
            differing.append(stem)
    print("=== byte-identity: %s vs %s" % (dir_a, dir_b))
    print("  compared        : %d" % len(files_a))
    print("  byte-identical  : %d" % identical)
    print("  DIFFERING       : %d   <- must be 0" % len(differing))
    print("  missing in b    : %d" % len(missing))
    for s in differing[:40]:
        print("    differs: %s" % s)
    return 2 if (differing or missing) else 0


def cmd_counters(directory, label):
    files = sorted(glob.glob(os.path.join(directory, "*.probe.json")))
    if not files:
        print("no .probe.json files under %s — was MU_KEY_COLLECTION_PROBE set?" % directory)
        return 2
    total = dict.fromkeys(COUNTER_FIELDS, 0)
    per_score = []
    variant_flags = set()
    for p in files:
        with open(p) as fh:
            block = json.load(fh)
        variant_flags.add(bool(block.get("signatureMaskVariant")))
        for f in COUNTER_FIELDS:
            total[f] += int(block.get(f, 0))
        if block.get("regionCommitCallsAltered", 0) or block.get("regionCommitCallsAlteredDomBB7", 0):
            per_score.append((_stem(p), block))

    print("=== counters: %s  (%d scores, signatureMaskVariant=%s)"
          % (label or directory, len(files),
             "/".join(sorted(str(v) for v in variant_flags))))
    for f in COUNTER_FIELDS:
        print("  %-32s %d" % (f, total[f]))
    print("  scores with an Altered-family region: %d" % len(per_score))
    for stem, block in per_score:
        print("    %-12s regionCommit alt=%d altDom=%d | analyzeChord alt=%d altDom=%d"
              % (stem, block["regionCommitCallsAltered"], block["regionCommitCallsAlteredDomBB7"],
                 block["analyzeChordCallsAltered"], block["analyzeChordCallsAlteredDomBB7"]))
    return 0


def cmd_flips(base_dir, var_dir):
    base_files = sorted(glob.glob(os.path.join(base_dir, "*.ours.json")))
    flips_in, flips_out, seg_diffs = [], [], []
    delta_regions = 0
    for pb in base_files:
        stem = _stem(pb)
        pv = os.path.join(var_dir, stem + ".ours.json")
        if not os.path.exists(pv):
            seg_diffs.append((stem, "missing in variant"))
            continue
        with open(pb) as fh:
            base = json.load(fh)
        with open(pv) as fh:
            var = json.load(fh)
        b_by_tick = {r["startTick"]: r for r in base["regions"]}
        v_by_tick = {r["startTick"]: r for r in var["regions"]}
        if set(b_by_tick) != set(v_by_tick):
            seg_diffs.append((stem, "region boundaries differ: base=%d var=%d"
                              % (len(b_by_tick), len(v_by_tick))))
        for tick, rb in sorted(b_by_tick.items()):
            if _delta_nonzero(rb):
                delta_regions += 1
            rv = v_by_tick.get(tick)
            if rv is None:
                continue
            if _chord_of(rb) == _chord_of(rv):
                continue
            row = (stem, tick, rb.get("key"), rv.get("key"),
                   rb.get("chordSymbol"), rv.get("chordSymbol"),
                   rb.get("romanNumeral"), rv.get("romanNumeral"))
            (flips_in if _delta_nonzero(rb) else flips_out).append(row)

    print("=== committed-chord flips: base=%s  variant=%s" % (base_dir, var_dir))
    print("  scores compared                                   : %d" % len(base_files))
    print("  regions under an Altered-family local key (base)   : %d" % delta_regions)
    print("  FLIPS inside those regions                        : %d" % len(flips_in))
    print("  FLIPS anywhere else (must be 0 — structural)      : %d" % len(flips_out))
    print("  segmentation differences                          : %d" % len(seg_diffs))
    if flips_in:
        print("  --- flips inside the Altered-family regions ---")
        print("  %-10s %-7s %-7s %-10s -> %-10s  %-9s -> %-9s"
              % ("stem", "tick", "key", "chord(base)", "chord(var)", "rn(base)", "rn(var)"))
        for stem, tick, kb, kv, cb, cv, rb, rv in flips_in:
            print("  %-10s %-7d %-7s %-10s -> %-10s  %-9s -> %-9s"
                  % (stem, tick, kb, cb, cv, rb, rv))
    if flips_out:
        print("  --- FLIPS OUTSIDE (a STOP: refutes the OI-168 derivation) ---")
        for row in flips_out[:60]:
            print("    %s" % (row,))
    for stem, why in seg_diffs[:20]:
        print("    segmentation: %s — %s" % (stem, why))
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == "byteid" and len(sys.argv) >= 4:
        return cmd_byteid(sys.argv[2], sys.argv[3])
    if cmd == "counters" and len(sys.argv) >= 3:
        label = sys.argv[sys.argv.index("--label") + 1] if "--label" in sys.argv else ""
        return cmd_counters(sys.argv[2], label)
    if cmd == "flips" and len(sys.argv) >= 4:
        return cmd_flips(sys.argv[2], sys.argv[3])
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Aggregate the oracle fire-count JSONL emitted by the default-OFF instrumentation in
chordanalyzer.cpp (Layer-4 audit pass-1, oracle session). Each batch_analyze process
appends one JSON line (keyed by pid) when MU_ORACLE_FIRECOUNT names this file; a parallel
run_bach_preset corpus pass therefore yields one line per process. This sums them and
prints the per-mechanism fire table with denominators, so protocol P4 ("what does it DO?")
is answered from measured behavior over the pinned Baroque corpus (git_hash c50002fee1),
not from reading. Read-only; validates the line count and reports any unparseable line.
"""
import json, sys

path = sys.argv[1] if len(sys.argv) > 1 else "fire_counts.jsonl"
lines = open(path, encoding="utf-8").read().splitlines()
agg = {}
n_ok = 0
n_bad = 0
pids = set()
for ln in lines:
    ln = ln.strip()
    if not ln:
        continue
    try:
        d = json.loads(ln)
    except Exception:
        n_bad += 1
        continue
    n_ok += 1
    pids.add(d.get("pid"))
    for k, v in d.items():
        if k == "pid":
            continue
        agg[k] = agg.get(k, 0) + int(v)

print(f"processes(lines): {n_ok} ok, {n_bad} unparseable; distinct pids: {len(pids)}")
calls = agg.get("analyzeCalls", 0)
print(f"analyzeChord invocations (non-empty input): {calls}")
print()
order = ["insufficientData", "jointEnabled", "bassEnumerated", "sparseUpperAmbiguous",
         "legacySingleBass", "structuralBassFalse", "wCompleteFired", "dim7BonusFired",
         "nonBassPenaltyApplied", "nonBassPenaltyWaived", "sus4MissingFourth",
         "sus4VariantMissing7th", "sus4Maj7MissingP5", "dom7b5TpcPenalty", "dom7b5Missing7th",
         "power3pcPenalty", "aug7GuardSkip", "augFactorHalved", "augRootCorrection",
         "sus2ToSus4", "susToMajorOmitsThird"]
print(f"{'mechanism':26s} {'count':>12s}  {'per analyzeChord call':>22s}")
for k in order:
    v = agg.get(k, 0)
    per = (v / calls) if calls else 0
    print(f"{k:26s} {v:12d}  {per:22.3f}")
# any counter not in the known order (defensive)
for k, v in agg.items():
    if k not in order and k != "analyzeCalls":
        print(f"{k:26s} {v:12d}  (unlisted)")

# machine-readable dump beside the human table
out = {"processes_ok": n_ok, "processes_bad": n_bad, "aggregate": agg}
json.dump(out, open(path.rsplit(".", 1)[0] + "_agg.json", "w", encoding="utf-8"), indent=1)

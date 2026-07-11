#!/usr/bin/env python3
"""Read-only aggregation of oracle OUTPUT-observable behavior over the committed
Baroque corpus (tools/corpus/baroque, pinned git_hash c50002fee1). No rebuild, no
re-run: parses the committed .ours.json winner+alternatives per region. Measures the
oracle mechanisms whose firing is visible in the output surface (quality win
distribution => dead-template check; slash rate; sparse-region populations; diatonic
rate; fan-out size). Internal branches (aug7 guard, w_complete, dim7 bonus,
structuralPenalties) are NOT visible here and are measured separately / flagged."""
import json, glob, collections, os

CORPUS = "tools/corpus/baroque"
files = sorted(glob.glob(os.path.join(CORPUS, "*.ours.json")))
qual = collections.Counter()
qual_dur = collections.Counter()
notecount = collections.Counter()
slash = 0
total = 0
total_dur = 0.0
slash_dur = 0.0
diatonic = 0
pedal = 0
alt_counts = collections.Counter()
sym_ext = collections.Counter()
regions_with_alts = 0
noteCount_le2 = 0
key_conf_regions = 0
for fp in files:
    d = json.load(open(fp))
    for r in d.get("regions", []):
        if not r.get("hasAnalyzedChord", True):
            continue
        total += 1
        dur = r.get("duration", 0) or 0
        total_dur += dur
        q = r.get("quality", "?")
        qual[q] += 1
        qual_dur[q] += dur
        nc = r.get("noteCount", 0)
        notecount[nc] += 1
        if nc <= 2:
            noteCount_le2 += 1
        if not r.get("bassIsRoot", True):
            slash += 1
            slash_dur += dur
        if r.get("diatonicToKey"):
            diatonic += 1
        sym = r.get("chordSymbol", "") or ""
        if "pedal" in sym.lower() or r.get("isPedalPoint"):
            pedal += 1
        alts = r.get("alternatives", []) or []
        alt_counts[len(alts)] += 1
        if alts:
            regions_with_alts += 1
        # crude extension presence from chord symbol tail
        for tag in ["maj7","m7","7","6","sus","dim","aug","ø","+","b5","#5","9","11","13"]:
            if tag in sym:
                sym_ext[tag] += 1

print(f"files={len(files)} regions(analyzed)={total} total_duration={total_dur:.0f}")
print()
print("== Quality win distribution (region count | duration) ==")
for q,c in qual.most_common():
    print(f"  {q:16s} {c:6d} ({100*c/total:5.1f}%) | dur {qual_dur[q]:8.0f} ({100*qual_dur[q]/total_dur:5.1f}%)")
print()
print("== noteCount (distinct sounding note population) ==")
for nc in sorted(notecount):
    print(f"  noteCount={nc}: {notecount[nc]} ({100*notecount[nc]/total:.1f}%)")
print(f"  noteCount<=2 (sparse edge population): {noteCount_le2} ({100*noteCount_le2/total:.1f}%)")
print()
print(f"== Slash / inversion (bassIsRoot=false) ==")
print(f"  slash regions: {slash} ({100*slash/total:.1f}%) | slash duration {slash_dur:.0f} ({100*slash_dur/total_dur:.1f}%)")
print(f"== diatonicToKey ==")
print(f"  diatonic regions: {diatonic} ({100*diatonic/total:.1f}%)")
print(f"== pedal-point-symbol regions ==")
print(f"  {pedal} ({100*pedal/total:.2f}%)")
print()
print("== alternatives[] count per region (fan-out the oracle handed up) ==")
for n in sorted(alt_counts):
    print(f"  {n} alts: {alt_counts[n]} ({100*alt_counts[n]/total:.1f}%)")
print(f"  regions with >=1 alt: {regions_with_alts} ({100*regions_with_alts/total:.1f}%)")
print()
print("== chord-symbol extension/quality tag frequency (crude) ==")
for tag,c in sym_ext.most_common():
    print(f"  '{tag}': {c}")

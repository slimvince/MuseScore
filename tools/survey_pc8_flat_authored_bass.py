"""
Iter 89 survey — pc=8 (Ab/G#) bass with flat-authored TPC.

Scans tools/corpus/*.ours.json (the active preset; rerun for both presets
manually) and classifies every region whose bass is pc=8 by:

  1) Is the bass tone TPC flat-authored?  (tpc <= 14 in MuseScore's "[7,14]
     flat range", honoring the dual MuseScore [7,13] / +1 [8,14] encoding
     described in chordanalyzer.cpp around the pitchClassNameFromTpc block.)
  2) Given root_pc + quality, is pc=8 a sharp-spelled chord tone (G#) or a
     flat-spelled chord tone (Ab)?

Buckets:
  SHARP_CORRECT — flat-authored Ab in a context where G# is the right name
                  (these are the cases the proposed fix WOULD flip).
  FLAT_CORRECT  — flat-authored Ab in a context where Ab is the right name
                  (these MUST remain Ab — false-positive risk if a fix
                  incorrectly catches them).
  AMBIGUOUS     — pc=8 is not a standard chord tone, or quality is Power/
                  Suspended where the rule is unclear.

We classify using only the analyzer-emitted root_pc + quality, plus the
bass interval (bass_pc - root_pc mod 12).  Spelling decisions:

  root_pc -> "sharp root"  letters: roots whose conventional spelling on the
  fifths circle is sharp-side or natural-going-sharp: pc in {1,4,6,9,11}
  with their interval to pc=8 below.
  root_pc -> "flat root"   pc in {3,5,8,10}.
  Otherwise (root_pc = 0/2/7) we look at chord quality + key.

Bass-as-chord-tone classification (interval = (8 - root_pc) mod 12):
  interval 0  : bass is root
  interval 3  : bass is m3
  interval 4  : bass is M3
  interval 6  : bass is dim5/aug4
  interval 7  : bass is P5
  interval 8  : bass is m6 (added)
  interval 9  : bass is M6
  interval 10 : bass is m7
  interval 11 : bass is M7
  other       : non-chord tone

Spelling rules (per common Baroque/jazz practice):

  G# (sharp) is correct when:
    - root spelled as E (pc=4) and bass is the M3 of E major
    - root spelled as C# (pc=1) and bass is the P5 of C# / C#m
    - root spelled as A (pc=9), Augmented or Major, and bass is the M7
      (G# is the leading tone in A major)
    - root spelled as B (pc=11) and bass is the M6 of B (rarer)
    - root spelled as G# (pc=8) — but only if the chord is naturally
      spelled with sharps (Jazz: G#m7b5 over G# bass).  At pc=8 root the
      chord MIGHT also be Ab — depends on context.

  Ab (flat) is correct when:
    - root spelled as Ab (pc=8) and the chord is naturally Ab/Abm/Ab7
    - root spelled as Db (pc=1) and bass is the P5 of Db — but pc=1 is
      ambiguous: C# vs Db.  Decided by the chord quality + key.
    - root spelled as F (pc=5) and bass is the m3 of Fm
    - root spelled as Eb (pc=3) and bass is the b6/aug5 of Eb+ (rare)
    - root spelled as Bb (pc=10) and bass is the m7 of Bb/Bbm
    - root spelled as C (pc=0) and bass is the b6 of C minor

For root_pc=1 (C#/Db) and root_pc=8 (G#/Ab), we DON'T flip — these are
genuinely ambiguous root spellings and the bass should be consistent with
the root spelling, which we don't have without checking root TPC.

Rule we'll evaluate (chord-tone guard, proposed fix):
  Flip bass pc=8 spelling to G# when:
    - bass tpc is flat-authored (tpc <= 14)
    - root_pc is in SHARP_ROOT_ROOTS = {4, 11, 9}  (E, B, A — common
      Baroque sharp-side roots that ground a chord with G# in it)
    - the interval (8 - root_pc) mod 12 places pc=8 as a chord tone of
      the identified quality (so we are sure pc=8 is part of the chord)

This intentionally excludes root_pc=1 and root_pc=8 (ambiguous) and any
case where pc=8 is a non-chord tone (passing/auxiliary).
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
CORPUS_DIR = os.path.join(ROOT, "corpus")

# MuseScore TPC numbering: F=13, C=14 (flats run [7,13] in MS, [8,14] in
# +1 encoding).  The "flat-authored for pc=8" condition is tpc<=14 (Ab=10
# in MS, =11 in +1; natural F/C also fall in the range but pc=8 won't hit
# those TPCs).
def is_flat_authored_tpc(tpc):
    return tpc is not None and tpc <= 14


def quality_chord_intervals(quality):
    """Return the set of intervals (mod 12) that are chord tones for a
    given primary triad/seventh quality.  This is intentionally coarse —
    extensions and inversions don't matter for spelling membership."""
    base = {0, 7}  # root, P5
    q = quality
    if q == "Major":
        return base | {4}            # +M3
    if q == "Minor":
        return base | {3}            # +m3
    if q == "Diminished":
        return {0, 3, 6}             # m3, dim5
    if q == "HalfDiminished":
        return {0, 3, 6, 10}         # m3, dim5, m7
    if q == "Augmented":
        return {0, 4, 8}             # M3, aug5
    if q in ("Suspended2", "Suspended4"):
        return {0, 7}                # P5 only (3rd absent)
    if q == "Power":
        return {0, 7}
    return set()


def classify_region(region):
    """Return one of: ('SHARP_CORRECT', root_pc, quality, chord_symbol),
    ('FLAT_CORRECT', ...), ('AMBIGUOUS', ...), or None if region does not
    qualify (bass pc != 8 or bass tpc not flat-authored)."""

    bass_pc = region.get("bassPitchClass")
    if bass_pc != 8:
        return None

    tones = region.get("tones", [])
    bass_tones = [t for t in tones if t.get("isBass")]
    if not bass_tones:
        return None
    bass_tpc = bass_tones[0].get("tpc")
    if not is_flat_authored_tpc(bass_tpc):
        return None

    root_pc = region.get("rootPitchClass")
    quality = region.get("quality")
    chord_symbol = region.get("chordSymbol", "")
    interval = (8 - root_pc) % 12 if root_pc is not None else None

    chord_tones = quality_chord_intervals(quality)
    is_chord_tone = interval in chord_tones

    # SHARP-CORRECT cases (proposed flip targets) ---------------------
    # E major (root=4) with G# as M3
    if root_pc == 4 and quality in ("Major", "Augmented") and interval == 4:
        return ("SHARP_CORRECT_E_M3", root_pc, quality, chord_symbol, bass_tpc)
    # A major (root=9) — pc=8 is M7 (leading tone)
    if root_pc == 9 and quality in ("Major", "Augmented") and interval == 11:
        return ("SHARP_CORRECT_A_M7", root_pc, quality, chord_symbol, bass_tpc)
    # B (root=11) — pc=8 is M6 (rare)
    if root_pc == 11 and quality == "Major" and interval == 9:
        return ("SHARP_CORRECT_B_M6", root_pc, quality, chord_symbol, bass_tpc)
    # C# (root=1) — pc=8 is P5 of C# triad (rare, root itself ambiguous)
    if root_pc == 1 and quality in ("Major", "Minor") and interval == 7:
        return ("AMBIGUOUS_CSharp_P5", root_pc, quality, chord_symbol, bass_tpc)
    # G# (root=8) — bass is root; root ambiguous
    if root_pc == 8 and interval == 0:
        return ("AMBIGUOUS_root_pc_8", root_pc, quality, chord_symbol, bass_tpc)

    # FLAT-CORRECT cases (must NOT flip) -----------------------------
    # Ab root chord (root=8) — already caught by ambiguous above
    # F minor (root=5) with Ab as m3
    if root_pc == 5 and quality == "Minor" and interval == 3:
        return ("FLAT_CORRECT_F_m3", root_pc, quality, chord_symbol, bass_tpc)
    # Db (root=1) with Ab as P5 — same chord as C#, classified ambiguous above
    # Bb (root=10) with Ab as m7
    if root_pc == 10 and quality in ("Major", "Minor") and interval == 10:
        return ("FLAT_CORRECT_Bb_m7", root_pc, quality, chord_symbol, bass_tpc)
    # Eb augmented (root=3) with Ab as aug5/m6 - rare
    if root_pc == 3 and quality == "Augmented" and interval == 8:
        return ("FLAT_CORRECT_Eb_aug5", root_pc, quality, chord_symbol, bass_tpc)
    # D (root=2) with Ab as dim5 (D7b5 / Ddim) — actually this is
    # the dim5 of D, but D7b5 in jazz is spelled with Ab.  In Baroque
    # context this would be unusual — flagged FLAT_CORRECT to be safe.
    if root_pc == 2 and quality in ("Diminished", "HalfDiminished") and interval == 6:
        return ("FLAT_CORRECT_D_dim5", root_pc, quality, chord_symbol, bass_tpc)
    # Db/C# diminished (root=1) with Ab as dim5? interval=7, not 6, so
    # doesn't apply.
    # Other Ab-as-chord-tone with flat-natural root:
    if root_pc in (0, 3, 5, 7, 8, 10) and is_chord_tone:
        return ("FLAT_CORRECT_OTHER", root_pc, quality, chord_symbol, bass_tpc)

    # Non-chord tone or unhandled
    return ("AMBIGUOUS_OTHER", root_pc, quality, chord_symbol, bass_tpc)


KEY_FIFTHS = {
    # Major keys
    "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7,
    "F": -1, "Bb": -2, "Eb": -3, "Ab": -4, "Db": -5, "Gb": -6, "Cb": -7,
    # Minor keys (same fifths as relative major)
    "Amin": 0, "Emin": 1, "Bmin": 2, "F#min": 3, "C#min": 4,
    "G#min": 5, "D#min": 6, "A#min": 7,
    "Dmin": -1, "Gmin": -2, "Cmin": -3, "Fmin": -4, "Bbmin": -5,
    "Ebmin": -6, "Abmin": -7,
    # Dorian (parent at +1 of the natural-minor)
    "DDor": 0, "ADor": 1, "EDor": 2, "BDor": 3, "F#Dor": 4,
    "GDor": -1, "CDor": -2, "FDor": -3, "BbDor": -4, "EbDor": -5,
    # Melodic minor variants map to Dorian parent (analyzer convention)
    "Amel": 1, "Dmel": 0, "Gmel": -1, "Cmel": -2,
}


def key_to_fifths(key_str):
    if key_str in KEY_FIFTHS:
        return KEY_FIFTHS[key_str]
    return None


def classify_sharp_authored(region):
    """Mirror classify_region but for SHARP-authored pc=8 bass (tpc>=20)."""
    bass_pc = region.get("bassPitchClass")
    if bass_pc != 8:
        return None
    tones = region.get("tones", [])
    bass_tones = [t for t in tones if t.get("isBass")]
    if not bass_tones:
        return None
    bass_tpc = bass_tones[0].get("tpc")
    if bass_tpc is None or bass_tpc < 20:
        return None

    root_pc = region.get("rootPitchClass")
    quality = region.get("quality")
    chord_symbol = region.get("chordSymbol", "")
    interval = (8 - root_pc) % 12 if root_pc is not None else None

    # Same buckets as before — the sharp-authored cases are the ones where
    # the current code FLATTENS to "Ab" but composer wrote "G#".
    if root_pc == 4 and quality in ("Major", "Augmented") and interval == 4:
        return ("SHARP_AUTHORED_E_M3", root_pc, quality, chord_symbol, bass_tpc)
    if root_pc == 9 and quality in ("Major", "Augmented") and interval == 11:
        return ("SHARP_AUTHORED_A_M7", root_pc, quality, chord_symbol, bass_tpc)
    if root_pc == 11 and quality == "Major" and interval == 9:
        return ("SHARP_AUTHORED_B_M6", root_pc, quality, chord_symbol, bass_tpc)
    if root_pc == 1 and quality in ("Major", "Minor") and interval == 7:
        return ("SHARP_AUTHORED_CSharp_P5", root_pc, quality, chord_symbol, bass_tpc)
    if root_pc == 8 and interval == 0:
        return ("SHARP_AUTHORED_root_pc_8", root_pc, quality, chord_symbol, bass_tpc)
    if root_pc == 5 and quality == "Minor" and interval == 3:
        return ("SHARP_AUTHORED_F_m3", root_pc, quality, chord_symbol, bass_tpc)
    if root_pc == 10 and quality in ("Major", "Minor") and interval == 10:
        return ("SHARP_AUTHORED_Bb_m7", root_pc, quality, chord_symbol, bass_tpc)
    return ("SHARP_AUTHORED_OTHER", root_pc, quality, chord_symbol, bass_tpc)


def main():
    if not os.path.isdir(CORPUS_DIR):
        print("corpus directory not found:", CORPUS_DIR)
        sys.exit(1)

    files = sorted(f for f in os.listdir(CORPUS_DIR) if f.endswith(".ours.json"))

    preset_counter = Counter()
    bucket_counter = Counter()
    detail_counter = Counter()
    examples_by_bucket = defaultdict(list)
    sharp_bucket_counter = Counter()
    sharp_detail_counter = Counter()
    sharp_examples_by_bucket = defaultdict(list)
    sharp_by_fifths = defaultdict(Counter)
    flat_by_fifths = defaultdict(Counter)

    total_regions = 0
    total_pc8_bass = 0
    total_pc8_flat_authored = 0
    total_pc8_sharp_authored = 0

    for fname in files:
        path = os.path.join(CORPUS_DIR, fname)
        try:
            with open(path, "r") as f:
                data = json.load(f)
        except Exception as e:
            print(f"skip {fname}: {e}")
            continue
        preset = data.get("preset", "?")
        preset_counter[preset] += 1

        for region in data.get("regions", []):
            total_regions += 1
            if region.get("bassPitchClass") == 8:
                total_pc8_bass += 1
                tones = region.get("tones", [])
                bass_tones = [t for t in tones if t.get("isBass")]
                bass_tpc = bass_tones[0].get("tpc") if bass_tones else None
                if is_flat_authored_tpc(bass_tpc):
                    total_pc8_flat_authored += 1
                elif bass_tpc is not None and bass_tpc >= 20:
                    total_pc8_sharp_authored += 1

                fifths = key_to_fifths(region.get("key", ""))
                if is_flat_authored_tpc(bass_tpc):
                    flat_by_fifths[fifths][region.get("chordSymbol", "")] += 1
                elif bass_tpc is not None and bass_tpc >= 20:
                    sharp_by_fifths[fifths][region.get("chordSymbol", "")] += 1

            classification = classify_region(region)
            if classification is not None:
                bucket = classification[0]
                bucket_counter[bucket] += 1
                detail_counter[(bucket, classification[3])] += 1
                if len(examples_by_bucket[bucket]) < 5:
                    examples_by_bucket[bucket].append(
                        f"{fname} m{region.get('measureNumber')} b{region.get('beat')} "
                        f"{classification[3]} (root_pc={classification[1]} "
                        f"quality={classification[2]} bass_tpc={classification[4]} "
                        f"key={region.get('key')})"
                    )

            sharp_classification = classify_sharp_authored(region)
            if sharp_classification is not None:
                bucket = sharp_classification[0]
                sharp_bucket_counter[bucket] += 1
                sharp_detail_counter[(bucket, sharp_classification[3])] += 1
                if len(sharp_examples_by_bucket[bucket]) < 5:
                    sharp_examples_by_bucket[bucket].append(
                        f"{fname} m{region.get('measureNumber')} b{region.get('beat')} "
                        f"{sharp_classification[3]} (root_pc={sharp_classification[1]} "
                        f"quality={sharp_classification[2]} bass_tpc={sharp_classification[4]} "
                        f"key={region.get('key')})"
                    )

    print("=" * 76)
    print(f"Corpus: {CORPUS_DIR}")
    print(f"Files scanned: {len(files)}")
    print(f"Preset distribution: {dict(preset_counter)}")
    print(f"Total regions: {total_regions}")
    print(f"Regions with bass pc=8: {total_pc8_bass}")
    print(f"  ... flat-authored TPC (tpc<=14): {total_pc8_flat_authored}")
    print(f"  ... sharp-authored TPC (tpc>=20): {total_pc8_sharp_authored}")
    print("=" * 76)
    print("FLAT-AUTHORED bucket counts:")
    for bucket, n in sorted(bucket_counter.items(), key=lambda x: -x[1]):
        print(f"  {bucket:30s}  {n}")
    print("=" * 76)
    print("SHARP-AUTHORED bucket counts (these are cases where current code flattens):")
    for bucket, n in sorted(sharp_bucket_counter.items(), key=lambda x: -x[1]):
        print(f"  {bucket:30s}  {n}")
    print("=" * 76)
    print("FLAT-AUTHORED bass: distribution by detected key fifths (current chord symbol):")
    for fifths in sorted(flat_by_fifths, key=lambda x: (x is None, x)):
        rows = flat_by_fifths[fifths].most_common(8)
        total = sum(flat_by_fifths[fifths].values())
        print(f"  fifths={fifths!s:>5}  total={total}")
        for sym, n in rows:
            print(f"     {sym:30s} {n}")
    print("=" * 76)
    print("SHARP-AUTHORED bass: distribution by detected key fifths (current chord symbol):")
    for fifths in sorted(sharp_by_fifths, key=lambda x: (x is None, x)):
        rows = sharp_by_fifths[fifths].most_common(8)
        total = sum(sharp_by_fifths[fifths].values())
        print(f"  fifths={fifths!s:>5}  total={total}")
        for sym, n in rows:
            print(f"     {sym:30s} {n}")
    print("=" * 76)
    print("Top chord-symbol details (FLAT-AUTHORED):")
    by_bucket = defaultdict(list)
    for (bucket, sym), n in detail_counter.items():
        by_bucket[bucket].append((sym, n))
    for bucket in sorted(by_bucket):
        rows = sorted(by_bucket[bucket], key=lambda x: -x[1])
        print(f"\n  [{bucket}]  (total {sum(n for _, n in rows)})")
        for sym, n in rows[:10]:
            print(f"    {sym:40s}  {n}")
    print("=" * 76)
    print("Top chord-symbol details (SHARP-AUTHORED):")
    by_bucket = defaultdict(list)
    for (bucket, sym), n in sharp_detail_counter.items():
        by_bucket[bucket].append((sym, n))
    for bucket in sorted(by_bucket):
        rows = sorted(by_bucket[bucket], key=lambda x: -x[1])
        print(f"\n  [{bucket}]  (total {sum(n for _, n in rows)})")
        for sym, n in rows[:10]:
            print(f"    {sym:40s}  {n}")
    print("=" * 76)
    print("Examples per FLAT-AUTHORED bucket:")
    for bucket in sorted(examples_by_bucket):
        print(f"\n  [{bucket}]")
        for line in examples_by_bucket[bucket]:
            print(f"    {line}")
    print("=" * 76)
    print("Examples per SHARP-AUTHORED bucket:")
    for bucket in sorted(sharp_examples_by_bucket):
        print(f"\n  [{bucket}]")
        for line in sharp_examples_by_bucket[bucket]:
            print(f"    {line}")


if __name__ == "__main__":
    main()

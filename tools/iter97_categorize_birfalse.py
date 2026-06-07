"""One-shot characterization: pull per-case details for the 26 Baroque BIR=false cases.

Read-only. Outputs structured data for docs/iter97_bir_false_categorization.md.
"""
import json
import sys
from pathlib import Path

CASES = [
    ("bwv114.7", 6000, 7, "Minor", 2, 9, "Diminished", 9),
    ("bwv14.5",  8160, 7, "Minor", 10, 10, "Major", 10),
    ("bwv17.7",  46080, 9, "Major", 3, 3, "Unknown", 3),
    ("bwv174.5", 6240, 4, "Major", 8, 8, "Minor", 8),
    ("bwv245.17", 4800, 5, "Major", 2, 2, "Unknown", 2),
    ("bwv245.28", 4320, 11, "Major", 8, 4, "Major", 4),
    ("bwv245.40", 51360, 5, "Suspended4", 10, 3, "Unknown", 3),
    ("bwv25.6",  20640, 4, "Diminished", 0, 0, "Major", 0),
    ("bwv258",   6000, 11, "Minor", 6, 1, "Diminished", 1),
    ("bwv269",   20640, 2, "Major", 6, 6, "Diminished", 6),
    ("bwv301",   960, 7, "Major", 9, 11, "Minor", 11),
    ("bwv309",   2160, 7, "Minor", 2, 9, "Diminished", 9),
    ("bwv309",   8160, 6, "HalfDiminished", 0, 9, "Diminished", 9),
    ("bwv354",   14400, 8, "Major", 6, 1, "Major", 1),
    ("bwv354",   20880, 10, "Minor", 5, 0, "Diminished", 0),
    ("bwv356",   25920, 6, "HalfDiminished", 0, 9, "Diminished", 9),
    ("bwv381",   4800, 7, "Major", 6, 4, "Minor", 4),
    ("bwv40.8",  30720, 10, "Minor", 1, 1, "Major", 1),
    ("bwv422",   23040, 9, "Suspended4", 2, 7, "Unknown", 7),
    ("bwv426",   960, 9, "Minor", 5, 5, "Major", 5),
    ("bwv432",   5520, 9, "Minor", 4, 4, "Minor", 4),
    ("bwv45.7",  20160, 6, "Major", 4, 10, "Diminished", 10),
    ("bwv48.7",  18480, 7, "Minor", 2, 9, "Diminished", 9),
    ("bwv60.5",  1920, 6, "Diminished", 0, 8, "Major", 8),
    ("bwv65.2",  11040, 9, "Diminished", 6, 2, "Major", 2),
    ("bwv74.8",  13440, 4, "Minor", 2, 0, "Major", 0),
]

PC_NAME = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

def pc_to_name(pc):
    return PC_NAME[pc % 12] if pc is not None and pc >= 0 else "?"

def find_region(regions, start_tick):
    for r in regions:
        if r.get("startTick") == start_tick:
            return r
    return None

def get_key_signature_fifths(region):
    # Not always emitted; derive from key string if absent.
    return region.get("keySignatureFifths")

def main():
    out_path = Path("C:/s/MS/tools") / "iter97_birfalse_cases_data.txt"
    lines = []
    for (stem, st, our_root, our_q, our_bass, their_root, their_q, wir_root) in CASES:
        json_path = Path("C:/s/MS/tools/corpus") / f"{stem}.ours.json"
        if not json_path.exists():
            lines.append(f"## {stem} tick={st}\n  MISSING JSON\n")
            continue
        with open(json_path) as f:
            data = json.load(f)
        regions = data.get("regions", [])
        r = find_region(regions, st)
        if r is None:
            lines.append(f"## {stem} tick={st}\n  REGION NOT FOUND in ours.json\n")
            continue
        # PCs present
        tones = r.get("tones", [])
        pcs = sorted({t["pitch"] % 12 for t in tones})
        pc_str = ",".join(pc_to_name(p) for p in pcs)
        distinct_pcs = len(pcs)
        # Bass tone
        bass_pcs = sorted({t["pitch"] % 12 for t in tones if t.get("isBass")})
        # Alternatives
        alts = r.get("alternatives", [])
        alts_str = " | ".join(
            f"{a.get('chordSymbol','?')}[{a.get('quality','?')}] s={a.get('score',0):.2f}"
            for a in alts[:4]
        )
        lines.append(
            f"## {stem} tick={st} m{r.get('measureNumber','?')}b{r.get('beat','?')}\n"
            f"  Key: {data.get('detectedKey','?')} (region key={r.get('key','?')}, kConf={r.get('keyConfidence',0):.2f})\n"
            f"  Tones (pcs, n={distinct_pcs}): {{{pc_str}}}  bassPCs={[pc_to_name(p) for p in bass_pcs]}\n"
            f"  Analyzer: root={pc_to_name(our_root)} q={our_q} bass={pc_to_name(our_bass)}  "
            f"score={r.get('chordScore',0):.2f} margin={r.get('chordScoreMargin',0):.2f}  noteCount={r.get('noteCount',0)}\n"
            f"  Ground truth: root={pc_to_name(their_root)} q={their_q} (WiR root={pc_to_name(wir_root)})\n"
            f"  Symbol: {r.get('chordSymbol','?')} / RN={r.get('romanNumeral','?')}\n"
            f"  Alts: {alts_str}\n"
        )
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(CASES)} cases to {out_path}")

if __name__ == "__main__":
    main()

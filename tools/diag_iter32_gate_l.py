"""Diagnostic for Gate L: Augmented root-position -> same-root Major."""
import json, glob, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml

CORPUS_DIR = ROOT / "tools" / "corpus"
WIR_DIR    = ROOT / "tools" / "dcml" / "when_in_rome"

NOTE_TO_PC = {'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,
              'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}

def parse_root(sym):
    m = re.match(r'^([A-G][b#]?)', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else -1

def parse_bass(sym):
    m = re.search(r'/([A-G][b#]?)$', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else parse_root(sym)

def infer_quality(sym):
    s = sym.split('/')[0]
    m = re.match(r'^[A-G][#b]?', s)
    if not m:
        return ""
    body = s[m.end():]
    if 'dim7' in body or 'o7' in body:
        return "Diminished7"
    if body.startswith('o') or 'm7b5' in body.lower():
        return "HalfDiminished"
    if 'maj7' in body.lower() or body.startswith('M7'):
        return "Major7"
    if body.startswith('m7') or body.startswith('min7'):
        return "Minor7"
    if body.startswith('7'):
        return "Dominant7"
    if '+' in body or 'aug' in body.lower():
        return "Augmented"
    if 'dim' in body.lower():
        return "Diminished"
    if body.startswith('m') or body.startswith('min'):
        return "Minor"
    return "Major"

# Build BIR=true error set using three-way method (same as analyze_inversion_errors.py)
bir_true_set = set()  # (stem, measureNumber, beat_rounded)

ours_files = sorted(CORPUS_DIR.glob("*.ours.json"))
for ours_path in ours_files:
    stem = ours_path.stem.replace(".ours", "")
    m21_path = CORPUS_DIR / f"{stem}.music21.json"
    if not m21_path.exists():
        continue
    _, ours_regions = cmp.load_analysis(ours_path)
    _, m21_regions  = cmp.load_analysis(m21_path)
    aligned = cmp.align_regions(ours_regions, m21_regions)

    wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
    wir_regions = []
    if wir_path:
        try:
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            pass

    wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions) if wir_regions else [None]*len(ours_regions)

    for i, (our_r, their_r) in enumerate(aligned):
        result = cmp.classify(our_r, their_r)
        if result.category != "chord_disagree":
            continue
        if not our_r.bass_is_root:
            continue
        # Three-way check
        if wir_regions and i < len(wir_aligned):
            wir_r = wir_aligned[i]
            wir_pc = wir_r.root_pc if wir_r is not None else None
            their_pc = their_r.root_pc if their_r is not None else None
            cat = cmp.three_way_classify(our_r.root_pc, their_pc, wir_pc)
            if cat == "music21_dcml_agree":
                bir_true_set.add((stem, our_r.measure_number, round(our_r.beat, 2)))

print(f"BIR=true error set size (three-way genuine): {len(bir_true_set)}\n")

# Now scan for Gate L candidate fires
hits_error   = []  # BIR=true errors Gate L would fix
hits_correct = []  # BIR=false correct regions Gate L would break (false positives)

THRESHOLD = 0.40

for ours_path in ours_files:
    stem = ours_path.stem.replace(".ours", "")
    data = json.load(open(ours_path))
    for r in data.get('regions', []):
        if not r.get('bassIsRoot', False):
            continue
        if r.get('quality', '') != 'Augmented':
            continue
        wb = r.get('bassPitchClass', -1)
        wr = r.get('rootPitchClass', parse_root(r.get('chordSymbol', '')))
        ws = r.get('chordScore', 0)
        key = r.get('key', '?')

        for i, alt in enumerate(r.get('alternatives', [])):
            asym = alt.get('chordSymbol', '')
            # Use rootPitchClass from alt if present, else parse from symbol
            ar = alt.get('rootPitchClass', parse_root(asym))
            ab = parse_bass(asym)   # alt has no bassPitchClass; infer from symbol
            aq = infer_quality(asym)
            if aq != 'Major':
                continue
            if ar != wr:
                continue
            if ab != wb:
                continue
            margin = ws - alt.get('score', 0)
            if margin > THRESHOLD:
                continue

            beat_r = round(r['beat'], 2)
            key3 = (stem, r['measureNumber'], beat_r)
            is_error = key3 in bir_true_set
            entry = (f"  {'ERROR ' if is_error else 'CORRECT'} "
                     f"bwv={stem:12s} m={r['measureNumber']:3} b={r['beat']:.1f}  "
                     f"winner={r['chordSymbol']:8s} alt[{i}]={asym:8s}  "
                     f"margin={margin:+.3f}  key={key}")
            if is_error:
                hits_error.append(entry)
            else:
                hits_correct.append(entry)
            break

print(f"Gate L would FIX {len(hits_error)} BIR=true error(s):")
for e in hits_error:
    print(e)

print(f"\nGate L would BREAK {len(hits_correct)} BIR=false correct case(s) [FALSE POSITIVES]:")
for e in hits_correct:
    print(e)

print(f"\nSummary: fixes={len(hits_error)}, false_positives={len(hits_correct)}")

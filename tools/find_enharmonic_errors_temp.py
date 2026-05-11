#!/usr/bin/env python3
"""Find genuine BIR=true errors where refRootPc == (winnerRootPc + 9) % 12."""

import sys, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / 'tools' / 'corpus'
WIR_DIR = ROOT / 'tools' / 'dcml' / 'when_in_rome'

sys.path.insert(0, str(ROOT / 'tools'))

import compare_analyses as cmp
import dcml_parser as dcml

NOTE_NAMES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

def parse_root_pc(sym):
    m = re.match(r'^([A-G][#b]?)', sym)
    if not m:
        return None
    note = m.group(1)
    mapping = {
        'C': 0, 'C#': 1, 'Db': 1,
        'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'Fb': 4, 'E#': 5,
        'F': 5, 'F#': 6, 'Gb': 6,
        'G': 7, 'G#': 8, 'Ab': 8,
        'A': 9, 'A#': 10, 'Bb': 10,
        'B': 11, 'Cb': 11, 'B#': 0,
    }
    return mapping.get(note)

ours_files = sorted(CORPUS_DIR.glob('*.ours.json'))
print(f"ROOT: {ROOT}")
print(f"CORPUS_DIR: {CORPUS_DIR}")
print(f"Found {len(ours_files)} ours.json files")

enharmonic_errors = []
processed = 0

for ours_path in ours_files:
    stem = ours_path.stem.replace('.ours', '')
    music21_path = CORPUS_DIR / f'{stem}.music21.json'
    if not music21_path.exists():
        continue

    try:
        _, ours_regions = cmp.load_analysis(ours_path)
        _, m21_regions  = cmp.load_analysis(music21_path)
    except Exception:
        continue

    if not ours_regions:
        continue

    aligned = cmp.align_regions(ours_regions, m21_regions)

    wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
    wir_regions = []
    if wir_path:
        try:
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            pass

    wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions) if wir_regions else [None] * len(ours_regions)
    processed += 1

    for i, (our_r, their_r) in enumerate(aligned):
        result = cmp.classify(our_r, their_r)
        if result.category != 'chord_disagree':
            continue
        if not our_r.bass_is_root:
            continue

        ref_pc_m21 = their_r.root_pc if their_r else None
        wir_r = wir_aligned[i] if wir_regions and i < len(wir_aligned) else None
        wir_pc = wir_r.root_pc if wir_r is not None else None

        category = cmp.three_way_classify(our_r.root_pc, ref_pc_m21, wir_pc)
        if category != 'music21_dcml_agree':
            continue

        ref_pc = ref_pc_m21
        if ref_pc is None:
            continue

        winner_pc = our_r.root_pc
        if ref_pc != (winner_pc + 9) % 12:
            continue

        alts_with_pc = []
        for alt in (our_r.alternatives or []):
            sym = alt.get('chordSymbol', '')
            rpc = parse_root_pc(sym)
            alts_with_pc.append({
                'symbol': sym,
                'root_pc': rpc,
                'score': alt.get('score', 0),
            })

        enh_alt_in_alts = any(a['root_pc'] == ref_pc for a in alts_with_pc)

        enharmonic_errors.append({
            'stem': stem,
            'measure': our_r.measure_number,
            'beat': our_r.beat,
            'winner_pc': winner_pc,
            'winner_quality': our_r.quality,
            'winner_symbol': our_r.chord_symbol,
            'ref_pc': ref_pc,
            'ref_pc_m21': ref_pc_m21,
            'wir_pc': wir_pc,
            'margin': our_r.chord_score_margin or 0.0,
            'chord_score': our_r.chord_score or 0.0,
            'note_count': our_r.note_count or 0,
            'bass_pc': our_r.bass_pc,
            'alts': alts_with_pc,
            'enh_alt_in_alts': enh_alt_in_alts,
            'ref_symbol_m21': their_r.chord_symbol if their_r else '?',
        })

print(f"\nProcessed {processed} chorales")
print(f"Genuine BIR=true enharmonic-pair errors (refPc = (winnerPc+9)%12): {len(enharmonic_errors)}")

enharmonic_errors.sort(key=lambda x: x['margin'])

print("\n--- All enharmonic-pair errors (sorted by margin) ---")
for e in enharmonic_errors:
    enh_note = NOTE_NAMES[e['ref_pc']]
    winner_note = NOTE_NAMES[e['winner_pc']]
    wir_str = f"wir={NOTE_NAMES[e['wir_pc']] if e['wir_pc'] is not None else '?'}"
    alts_str = ', '.join(f"{a['symbol']}(s={a['score']:.2f})" for a in e['alts'][:4])
    print(f"  {e['stem']} m{e['measure']} b{e['beat']:.0f} | winner={winner_note}{e['winner_quality'][:3]}({e['winner_pc']}) should={enh_note}({e['ref_pc']}) {wir_str} | margin={e['margin']:.3f} nc={e['note_count']} | enh_in_alts={e['enh_alt_in_alts']} | alts=[{alts_str}]")

in_alts = sum(1 for e in enharmonic_errors if e['enh_alt_in_alts'])
not_in_alts = len(enharmonic_errors) - in_alts
print(f"\nEnharmonic alt IN alternatives: {in_alts}/{len(enharmonic_errors)}")
print(f"Enharmonic alt NOT in alternatives: {not_in_alts}/{len(enharmonic_errors)}")

# Group by what's actually in the alternatives
print("\n--- Categorization of enharmonic alt in alts ---")
for e in enharmonic_errors:
    if e['enh_alt_in_alts']:
        matching = [a for a in e['alts'] if a['root_pc'] == e['ref_pc']]
        for a in matching:
            print(f"  ALT_PRESENT: {e['stem']} m{e['measure']} b{e['beat']:.0f} | alt_sym={a['symbol']} margin={e['margin']:.3f}")

low_m = sum(1 for e in enharmonic_errors if e['margin'] < 0.10)
med_m = sum(1 for e in enharmonic_errors if 0.10 <= e['margin'] < 0.20)
hi_m  = sum(1 for e in enharmonic_errors if e['margin'] >= 0.20)
print(f"\nMargin < 0.10: {low_m}")
print(f"Margin 0.10-0.20: {med_m}")
print(f"Margin >= 0.20: {hi_m}")

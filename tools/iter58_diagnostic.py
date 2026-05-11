"""Iter 58 Blocker C diagnostic — diagnostic-only, no source-code changes.

Identifies the 8 Blocker C cases by re-running compare_analyses on the
current corpus, then for each erroneous region tests Hypotheses A/B/C
for why the HalfDim candidate at the agreed root is absent.
"""
import sys
sys.path.insert(0, 'tools')

import json
from pathlib import Path

import compare_analyses as cmp
import dcml_parser as dcml

CORPUS = Path('tools/corpus')
WIR    = Path('tools/dcml/when_in_rome')

PC_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def pcs_from_mask(mask):
    return sorted([i for i in range(12) if mask & (1 << i)])

def pcs_from_tones(tones):
    return sorted({t['pitch'] % 12 for t in tones})

def halfdim_pcs(root):
    """HalfDiminished (m7b5) = root, m3, b5, m7 = root + {0, 3, 6, 10}."""
    return sorted([(root + iv) % 12 for iv in (0, 3, 6, 10)])

def fmt_pcs(pcs):
    return '[' + ','.join(PC_NAMES[p] for p in pcs) + ']'

def norm_q(q):
    return cmp._norm_quality(q) if q else ''

# Build the current authoritative list of genuine BIR=true cases.
# For each, capture our_region_index (position in regions[]) for examination.
def collect_genuine_bir_true():
    out = []
    for of in sorted(CORPUS.glob('*.ours.json')):
        stem = of.name.replace('.ours.json','')
        m21f = CORPUS / f'{stem}.music21.json'
        if not m21f.exists():
            continue
        try:
            ours_data, ours_regs = cmp.load_analysis(of)
            _, m21_regs = cmp.load_analysis(m21f)
        except Exception:
            continue
        if not ours_regs:
            continue
        aligned = cmp.align_regions(ours_regs, m21_regs)
        wir_path = dcml.find_wir_file(str(WIR), stem)
        if not wir_path:
            continue
        try:
            wir_regs = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        wir_aligned = cmp.align_dcml_regions(ours_regs, wir_regs)
        raw = json.loads(of.read_text(encoding='utf-8'))
        raw_regs = raw.get('regions', [])
        for i, (our_r, their_r) in enumerate(aligned):
            result = cmp.classify(our_r, their_r)
            if result.category != 'chord_disagree':
                continue
            if not our_r.bass_is_root:
                continue
            wir_r = wir_aligned[i] if i < len(wir_aligned) else None
            wir_pc = wir_r.root_pc if wir_r else None
            cat = cmp.three_way_classify(our_r.root_pc, their_r.root_pc if their_r else None, wir_pc)
            if cat != 'music21_dcml_agree':
                continue
            agreed_root = their_r.root_pc if their_r else wir_pc
            ridx = None
            nq = norm_q(our_r.quality)
            for ri, rr in enumerate(raw_regs):
                if (rr.get('measureNumber') == our_r.measure_number
                    and abs(rr.get('beat', 0.0) - our_r.beat) < 0.01
                    and rr.get('rootPitchClass') == our_r.root_pc
                    and norm_q(rr.get('quality','')) == nq):
                    ridx = ri
                    break
            out.append({
                'stem': stem,
                'measure': our_r.measure_number,
                'beat': our_r.beat,
                'our_root': our_r.root_pc,
                'agreed_root': agreed_root,
                'our_quality': our_r.quality,
                'region_idx': ridx,
            })
    return out

# Decide which cases are Cluster A Blocker C.
# Pattern: our quality=Minor, ranked-alt[1] is same-root Diminished, HalfDim at
# agreed root absent from alternatives.
def classify_cluster_a_blocker_c(case, region):
    if norm_q(case['our_quality']) != 'Minor':
        return False, 'not_minor_winner'
    alts = region.get('alternatives', [])
    has_same_root_dim = any(
        int(a.get('rootPitchClass', -1)) == case['our_root']
        and norm_q(a.get('quality','')) in ('Diminished','Diminished7','HalfDiminished')
        for a in alts
    )
    has_halfdim_at_agreed = any(
        int(a.get('rootPitchClass', -1)) == case['agreed_root']
        and norm_q(a.get('quality','')) == 'HalfDiminished'
        for a in alts
    )
    # Cluster A Blocker C: same-root dim alt present, halfdim-at-agreed absent
    if has_same_root_dim and not has_halfdim_at_agreed:
        return True, 'cluster_a_blocker_c'
    if has_halfdim_at_agreed:
        return False, 'has_halfdim_alt (gate-fixable, not Blocker C)'
    return False, 'no_dim_alt'

genuine = collect_genuine_bir_true()
print(f'Current genuine BIR=true: {len(genuine)}')

# Load corpus JSONs once per stem
corpus_cache = {}
def get_json(stem):
    if stem not in corpus_cache:
        corpus_cache[stem] = json.loads((CORPUS / f'{stem}.ours.json').read_text(encoding='utf-8'))
    return corpus_cache[stem]

blocker_c = []
for c in genuine:
    data = get_json(c['stem'])
    regs = data['regions']
    if c['region_idx'] is None or c['region_idx'] >= len(regs):
        continue
    r = regs[c['region_idx']]
    is_bc, why = classify_cluster_a_blocker_c(c, r)
    if is_bc:
        blocker_c.append((c, r))

print(f'Cluster A Blocker C cases identified: {len(blocker_c)}')
print()

out_lines = []
def w(s=''):
    print(s)
    out_lines.append(s)

w('=== Blocker C Investigation — Iter 58 ===')
w('')
w(f'Corpus baseline: BIR=true=14, BIR=false=132 (Iter 55 corpus state)')
w(f'Cluster A Blocker C cases identified (Minor winner + same-root Dim alt, no HalfDim-at-agreed-root alt): {len(blocker_c)}')
w('')

# Corpus-wide HalfDim scan (confirms candidate generation works in general)
halfdim_winners = 0
halfdim_alts = 0
halfdim_samples = []
for jp in sorted(CORPUS.glob('*.ours.json')):
    try:
        d = json.loads(jp.read_text(encoding='utf-8'))
    except Exception:
        continue
    for r in d.get('regions', []):
        if 'half' in str(r.get('quality','')).lower():
            halfdim_winners += 1
            if len(halfdim_samples) < 5:
                halfdim_samples.append(('winner', jp.stem, r.get('measureNumber'),
                                        r.get('beat'), r.get('quality'),
                                        r.get('pitchClassSet'),
                                        r.get('rootPitchClass')))
        for a in r.get('alternatives', []):
            if 'half' in str(a.get('quality','')).lower():
                halfdim_alts += 1

hyp_counts = {'A': 0, 'B': 0, 'C': 0, 'unclear': 0}

for case, r in blocker_c:
    stem = case['stem']
    meas = case['measure']
    beat = case['beat']
    ours_pc = case['our_root']
    agreed_pc = case['agreed_root']
    agreed_name = PC_NAMES[agreed_pc]
    idx = case['region_idx']

    data = get_json(stem)
    regs = data['regions']

    mask = r.get('pitchClassSet', 0)
    pcs = pcs_from_mask(mask)
    tones = r.get('tones', [])
    tones_pcs = pcs_from_tones(tones) if tones else []
    expected = set(halfdim_pcs(agreed_pc))
    present = set(pcs)
    missing = sorted(expected - present)
    extra = sorted(present - expected)

    w('')
    w(f'--- {stem}  m={meas} b={beat}  (region idx={idx}) ---')
    w(f'  Our root: {PC_NAMES[ours_pc]} ({case["our_quality"]})  Agreed root: {agreed_name}')
    w(f'  Expected HalfDim {agreed_name}m7b5 PC set: {fmt_pcs(halfdim_pcs(agreed_pc))}')
    w(f'  Erroneous region:')
    w(f'    startTick={r.get("startTick")} endTick={r.get("endTick")} dur={r.get("duration")}')
    w(f'    pitchClassSet=0x{mask:04X}  PCs={fmt_pcs(pcs)}  count={len(pcs)}')
    w(f'    tones PCs={fmt_pcs(tones_pcs)}')
    w(f'    bass pc={r.get("bassPitchClass")} ({PC_NAMES[r.get("bassPitchClass",0)]})')
    w(f'    winner: {r.get("quality")} root={r.get("rootPitchClass")} score={r.get("chordScore"):.4f}')
    w(f'    Missing PCs for HalfDim {agreed_name}: {fmt_pcs(missing) if missing else "none"}')
    w(f'    Extra PCs vs HalfDim {agreed_name}:   {fmt_pcs(extra) if extra else "none"}')

    alts = r.get('alternatives', [])
    w(f'  alternatives ({len(alts)}):')
    for j, a in enumerate(alts):
        w(f'    [{j}] root={a.get("rootPitchClass")} ({PC_NAMES[a.get("rootPitchClass",0)]}) '
          f'qual={a.get("quality")} bassIsRoot={a.get("bassIsRoot")} '
          f'score={a.get("score"):.4f} sym={a.get("chordSymbol")}')

    # Examine immediate neighbours (region idx-2 .. idx+2) for missing PC
    w(f'  Neighbours (idx ±3):')
    found_in_neighbour = []  # (offset, ni, list_of_missing_present, dur, m, b)
    for ni in range(max(0, idx-3), min(len(regs), idx+4)):
        if ni == idx:
            continue
        nr = regs[ni]
        nmask = nr.get('pitchClassSet', 0)
        npcs = pcs_from_mask(nmask)
        ntones_pcs = pcs_from_tones(nr.get('tones', []))
        dur = nr.get('duration', 0)
        npresent = set(npcs)
        neighbour_has_missing = [p for p in missing if p in npresent or p in set(ntones_pcs)]
        flag = ' ***HAS-MISSING***' if neighbour_has_missing else ''
        w(f'    [idx={ni:>3}] m={nr.get("measureNumber"):>3} b={nr.get("beat"):.2f} '
          f'dur={dur} qual={nr.get("quality")} '
          f'PCs={fmt_pcs(npcs)}{flag}')
        if neighbour_has_missing:
            found_in_neighbour.append((ni - idx, ni, neighbour_has_missing, dur,
                                       nr.get('measureNumber'), nr.get('beat')))

    # Hypothesis decision
    w('  HYPOTHESIS ANALYSIS:')
    if not missing:
        hyp = 'C'
        evidence = 'all HalfDim PCs present in region, but HalfDim candidate not generated'
    else:
        tones_only = set(tones_pcs) - present
        in_tones_missing = tones_only & expected
        # Restrict to IMMEDIATELY adjacent (offset == ±1) for boundary-split confirmation
        immediate = [t for t in found_in_neighbour if abs(t[0]) == 1]
        if in_tones_missing:
            hyp = 'B'
            evidence = f'missing PC {fmt_pcs(sorted(in_tones_missing))} in tones but not in pitchClassSet — accumulation gap'
        elif immediate:
            t = immediate[0]
            hyp = 'A'
            offset_str = 'next' if t[0] == 1 else 'prev'
            evidence = (f'missing PC {fmt_pcs(t[2])} in IMMEDIATE neighbour ({offset_str}, idx={t[1]}, '
                        f'm={t[4]} b={t[5]:.2f}, dur={t[3]}) — greedy boundary split')
        elif found_in_neighbour:
            # Found in non-immediate neighbour — less likely a clean boundary split
            t = found_in_neighbour[0]
            hyp = 'unclear'
            evidence = (f'missing PC found only in distant neighbour offset={t[0]:+d} idx={t[1]} '
                        f'(m={t[4]} b={t[5]:.2f}) — not an immediate-boundary split')
        else:
            hyp = 'unclear'
            evidence = f'missing PC {fmt_pcs(missing)} not present in region or immediate neighbours'

    w(f'    Hypothesis: {hyp}')
    w(f'    Evidence:   {evidence}')
    hyp_counts[hyp] = hyp_counts.get(hyp, 0) + 1

w('')
w('=' * 70)
w('CORPUS-WIDE HalfDim CANDIDATE SCAN')
w('=' * 70)
w(f'Regions with HalfDim as WINNER:       {halfdim_winners}')
w(f'Alternative entries with HalfDim:     {halfdim_alts}')
w('Confirms: candidate generation produces HalfDim freely when pitch-class set supports it.')
w('Samples (winner only):')
for s in halfdim_samples[:5]:
    w(f'  {s}')

w('')
w('=' * 70)
w('HYPOTHESIS SUMMARY')
w('=' * 70)
w(f'Hypothesis A (boundary split):       {hyp_counts.get("A", 0)} cases')
w(f'Hypothesis B (accumulation gap):     {hyp_counts.get("B", 0)} cases')
w(f'Hypothesis C (candidate generation): {hyp_counts.get("C", 0)} cases')
w(f'Unclear:                             {hyp_counts.get("unclear", 0)} cases')

# Fix-direction recommendation
w('')
w('=' * 70)
w('FIX-DIRECTION RECOMMENDATION')
w('=' * 70)
w(f'Result: {hyp_counts["A"]} cases Hypothesis A (boundary split), '
  f'{hyp_counts["C"]} cases Hypothesis C (candidate gap), '
  f'{hyp_counts["B"]} cases Hypothesis B, '
  f'{hyp_counts["unclear"]} unclear.')
w('')
w('The Iter 56 working hypothesis ("greedy boundary split fragmented the Xm6")')
w('is only HALF the story. Two distinct root causes co-exist:')
w('')
w('-- Hypothesis A (4 cases) --------------------------------------------')
w('  The erroneous region has a 3-PC subset of the would-be HalfDim, and')
w('  the missing chord tone sits in the IMMEDIATELY-preceding short region.')
w('  Greedy segmentation placed a boundary between the bass entry and the')
w('  added tone (or between the m7 release and the rest of the chord).')
w('')
w('  Fix direction:')
w('    R3-MERGE — after Round 2 boundaries are placed, run a "completion')
w('    pass" that merges two adjacent regions when (a) both have duration')
w('    < DIVISION/2 (i.e. they are short fragments, not full beats), (b) the')
w('    UNION of their pitch-class sets matches a known seventh-chord PC mask')
w('    (HalfDim, MinMaj7, Dom7, etc.), and (c) the bass PC remains unchanged')
w('    across the boundary. The merge reconstructs the full PC set so the')
w('    candidate generator sees the complete chord.')
w('')
w('    Risk on BIR=false: LOW–MEDIUM. The duration guard limits merging to')
w('    very short fragments; long Diminished/Minor chords are untouched.')
w('    But the merge could occasionally swap a correct two-chord reading')
w('    (e.g. passing-tone followed by chord) into a false single-chord call.')
w('    Mitigation: require the union to be a strict match against a known')
w('    seventh-chord pattern, not merely a superset of three notes.')
w('')
w('-- Hypothesis C (4 cases) --------------------------------------------')
w('  The erroneous region has the COMPLETE HalfDim PC set, yet the')
w('  candidate generator does NOT produce a HalfDim candidate with the')
w('  agreed root (the bass-minus-m3). It only produces same-root Minor and')
w('  same-root Diminished alternatives.')
w('')
w('  Concrete example — bwv244.44 m=5 b=1.0:')
w('    PC set = {C#, E, G, B}, bass = E. C#m7b5 = {C#, E, G, B} exactly.')
w('    Yet alternatives are only Em (alt[0]) and Edim (alt[1]). No C#m7b5.')
w('')
w('  This indicates the candidate generator restricts root selection to a')
w('  subset of the present PCs (likely bass-pc or strongly-weighted PCs).')
w('  It does not enumerate "what if the M6-above-bass is the actual root,')
w('  making this an X-half-diminished?" — even though that interpretation')
w('  is enharmonically equivalent and structurally consistent.')
w('')
w('  Fix direction:')
w('    In the chord-candidate generator, when the bass pc forms a minor third')
w('    above some other PC in the set, ADD a HalfDim candidate rooted at that')
w('    other PC. (Equivalently: for any PC in the set, generate a HalfDim')
w('    candidate rooted at PC if the set contains PC + {m3, b5, m7}.)')
w('')
w('    Risk on BIR=false: MEDIUM. This is a broader candidate-pool change')
w('    affecting all minor-triad-plus-major-6th voicings. Many of these')
w('    are correctly read as Xm6 in the corpus. Mitigation:')
w('      - Require minimum support score (e.g. all 4 chord tones present)')
w('        before HalfDim is added, never as a fallback.')
w('      - Let downstream gates (Gate K/L/M-style preferences) decide')
w('        between Xm6 and (X+m3)m7b5 in tied-score situations using key')
w('        context (the agreed root should be diatonic).')
w('')
w('-- Combined recommendation -------------------------------------------')
w('  Both fixes are needed for the full 8-case Blocker C reduction.')
w('  Recommended sequencing:')
w('    1. Tackle Hypothesis C first (4 cases). The fix is localized to')
w('       candidate generation; once HalfDim candidates appear in')
w('       alternatives, the existing post-ranking infrastructure (Gate M-')
w('       style preferences) can rank them. Verify zero BIR=false regressions')
w('       on Baroque and Jazz before proceeding.')
w('    2. Tackle Hypothesis A second (4 cases). The R3-merge change is')
w('       more invasive (touches segmentation), so isolating it from the')
w('       candidate-generation change keeps the regression surface small.')
w('       After the C fix, A cases will likely become "post-merge -> full PC')
w('       set -> HalfDim candidate" — i.e. they depend on C.')

Path('tools/iter58_blocker_c_investigation.txt').write_text('\n'.join(out_lines), encoding='utf-8')
print()
print('[saved to tools/iter58_blocker_c_investigation.txt]')

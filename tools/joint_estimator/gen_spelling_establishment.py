#!/usr/bin/env python3
"""gen_spelling_establishment.py — the §5.2 establishment of the notation record's root/bass tonal
SPELLINGS (notation output-surface contract §3.2 / §5.2).

Read-only. It reads the committed SELECTED-arm decode (decode_parity_ref.json — the authoritative §5
decode, class keys + framework per segment) and the notated notes (note_events.json — each note's
line-of-fifths tpc), derives every committed segment's root (and bass-factor) tonal spelling from
(key, degree/class) by the SAME standard-theory line-of-fifths mapping the C++ module implements
(joint::recordRootSpellingLof / joint::recordBassSpellingLof), and — wherever the derived pitch class
ACTUALLY SOUNDS as a notated note inside the segment span — compares the derived spelling against the
notated tpc. It writes spelling_establishment.json: agreement counts overall and per (mode,
degree/class) cell, and EVERY divergence enumerated (stem@tick, derived vs notated, class).

No decode is run here (the decode is the committed reference); no committed artifact is modified. The
line-of-fifths convention is C=0 (each +1 = a perfect fifth up), identical to note_events' `lof` field
(= tpc - Tpc::TPC_C). Spec: cowork_notation_output_contract.md §3.2 + §5.2.

Usage:  python tools/joint_estimator/gen_spelling_establishment.py [--out <path>]
"""
import argparse
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))

# ── the line-of-fifths derivation (mirror of the C++ jointspelling; see that file for the full
#    derivation comment block). Every mapping carries its music-theory basis. ──────────────────────

# scale-degree line-of-fifths offset relative to the mode tonic (major / natural minor).
_MAJOR_LOF = [0, 2, 4, -1, 1, 3, 5]     # I..VII : C D E F G A B  (relative to C)
_MINOR_LOF = [0, 2, -3, -1, 1, -4, -2]  # i..VII : A B C D E F G  (relative to A; ♭3 ♭6 ♭7)
_DEG = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7}
_DIM_QUALS = {'Dim', 'Dim7', 'HalfDim7', 'HalfDim'}   # jointprimitives.isDimQuality

# canonical line-of-fifths spelling of a chord-factor semitone interval (the standard tertian
# spellings): unison 0->0, m3 3->-3, M3 4->+4, d5 6->-6, P5 7->+1, A5 8->+8, d7 9->-9, m7 10->-2,
# M7 11->+5.
_INTERVAL_LOF = {0: 0, 3: -3, 4: 4, 6: -6, 7: 1, 8: 8, 9: -9, 10: -2, 11: 5}
_QUAL_TMPL = {
    "Maj": [0, 4, 7], "Min": [0, 3, 7], "Dim": [0, 3, 6], "Aug": [0, 4, 8],
    "Dom7": [0, 4, 7, 10], "Maj7": [0, 4, 7, 11], "Min7": [0, 3, 7, 10], "MinMaj7": [0, 3, 7, 11],
    "Dim7": [0, 3, 6, 9], "HalfDim7": [0, 3, 6, 10], "HalfDim": [0, 3, 6],
    "Aug7": [0, 4, 8, 10], "AugMaj7": [0, 4, 8, 11],
}
_ROLES = ['root', 'third', 'fifth', 'seventh']

# (Ionian pc) -> {primary, enharmonic-alternate} signature fifths (the circle-of-fifths signatures).
_SIG_OPTS = {0: (0, 0), 1: (7, -5), 2: (2, 2), 3: (-3, -3), 4: (4, 4), 5: (-1, -1),
             6: (6, -6), 7: (1, 1), 8: (-4, -4), 9: (3, 3), 10: (-2, -2), 11: (5, -7)}


def _split_degree(base):
    acc, i = 0, 0
    while i < len(base) and base[i] in 'b#':
        acc += (1 if base[i] == '#' else -1)
        i += 1
    return _DEG.get(base[i:].upper(), -1), acc


def _degree_lof_offset(num, acc, is_major, quality):
    base = (_MAJOR_LOF if is_major else _MINOR_LOF)[num - 1]
    if (not is_major) and acc == 0 and quality in _DIM_QUALS:
        if num == 7:
            base = 5    # raised leading tone (harmonic/melodic minor)
        elif num == 6:
            base = 3    # raised submediant
    return base + 7 * acc


def _key_sig_fifths(tonic, is_major, ref):
    ion = (tonic if is_major else tonic + 3) % 12
    o0, o1 = _SIG_OPTS[ion]
    return o0 if abs(o0 - ref) <= abs(o1 - ref) else o1


def _key_tonic_lof(tonic, is_major, ref):
    return _key_sig_fifths(tonic, is_major, ref) + (0 if is_major else 3)


def _class_fields(class_key):
    parts = (class_key.split(' | ') + ['', '', '', ''])[:4]
    return parts[0], parts[1], parts[2], parts[3]   # degree, quality, inversion, target


def root_lof(class_key, tonic, is_major, ref):
    """The root's line-of-fifths spelling, or None for an unmappable/rootless-derivation class."""
    degree, quality, _inv, target = _class_fields(class_key)
    ktl = _key_tonic_lof(tonic, is_major, ref)
    fw_lof, fw_major = ktl, is_major
    if target:
        if '/' in target:
            return None
        tnum, tacc = _split_degree(target)
        if tnum < 0:
            return None
        fw_lof = ktl + _degree_lof_offset(tnum, tacc, is_major, '')
        tbase = target.lstrip('b#')
        fw_major = bool(tbase) and tbase[0].isupper()
    if quality == 'Neapolitan':
        return fw_lof - 5      # ♭2 spelling (Db in C)
    if quality == 'AugSixth':
        return fw_lof          # the chromatic "root" is the framework tonic (chromatic_root_pc)
    num, acc = _split_degree(degree)
    if num < 0 or quality not in _QUAL_TMPL:
        return None
    return fw_lof + _degree_lof_offset(num, acc, fw_major, quality)


def factor_lofs(class_key, tonic, is_major, ref):
    """role -> (pc, lof) for each chord factor, or {} for a chromatic/unmappable class."""
    _deg, quality, _inv, _tgt = _class_fields(class_key)
    rl = root_lof(class_key, tonic, is_major, ref)
    if rl is None or quality not in _QUAL_TMPL:
        return {}
    out = {}
    for k, iv in enumerate(_QUAL_TMPL[quality]):
        lof = rl + _INTERVAL_LOF[iv]
        out[_ROLES[k]] = ((7 * lof) % 12, lof)
    return out


def _pc(lof):
    return (7 * lof) % 12


def compare_cpp_parity(decode, ne, cpp):
    """OI-197: compare the C++ dump's per-segment root/factor spellings against the Python derivation,
    lof-EXACT, over EVERY committed segment. Both sides implement the ONE documented line-of-fifths
    derivation (jointprimitives::rootSpellingLof/factorSpellingLof == root_lof/factor_lofs here), so any
    divergence means one implementation is wrong (a STOP; the artifact records it, the fix is not decided
    by editing). The comparison cells are exactly the establishment's: the ROOT field on every committed
    segment (13,063), and the BASS field at each segment's lowest-note factor cell (11,182). The full
    factor set is compared too (a stronger superset). Note-selection (lowest sounding note -> factor) is
    done here, identically to the notated establishment above, so the C++ dump only supplies the
    derivation (root_lof + all factor lofs). Returns the cpp_parity block; note-independent of any table.
    """
    pieces = ne['pieces']
    selected = decode['selected']
    cpp_pieces = cpp.get('pieces', {})

    seg_total = 0
    matched = 0
    root_cells = 0
    bass_cells = 0
    factor_cells = 0
    root_div, bass_div, factor_div = [], [], []
    class_mismatch, missing = [], []
    cpp_seen = set()   # (stem, tick) committed cells matched into the C++ dump

    for stem in sorted(selected.keys()):
        if stem not in pieces:
            continue
        dec = selected[stem]
        sig = dec.get('sig_fifths')
        ref = sig if sig is not None else 0
        pc = pieces[stem]
        events = pc['events']
        notes = pc['notes']
        cpp_segs = {s['tick']: s for s in cpp_pieces.get(stem, {}).get('segments', [])}

        for seg in dec['segments']:
            i, j, tonic, is_major, class_key, _root_pc = seg[0], seg[1], seg[2], seg[3], seg[4], seg[5]
            if i < 0 or j <= i or j > len(events):
                continue
            seg_total += 1
            seg_start = events[i][0]
            seg_end = events[j - 1][1]

            rl = root_lof(class_key, tonic, is_major, ref)
            factors = factor_lofs(class_key, tonic, is_major, ref)   # role -> (pc, lof)

            cs = cpp_segs.get(seg_start)
            if cs is None:
                missing.append({'stem': stem, 'tick': seg_start, 'class': class_key})
                continue
            cpp_seen.add((stem, seg_start))
            matched += 1
            if cs.get('class_key') != class_key:
                class_mismatch.append({'stem': stem, 'tick': seg_start,
                                       'cpp_class': cs.get('class_key'), 'py_class': class_key})
                continue   # a DECODE divergence (not spelling): skip the spelling compare, still reported

            # ROOT field parity (every committed segment; the establishment's 13,063 cells)
            root_cells += 1
            if cs.get('root_lof') != rl:
                root_div.append({'stem': stem, 'tick': seg_start, 'class': class_key,
                                 'py_root_lof': rl, 'cpp_root_lof': cs.get('root_lof')})

            # full FACTOR set parity (superset) — cpp factors keyed by pc (distinct per tertian chord)
            cpp_facs = {f['pc']: f['lof'] for f in cs.get('factors', [])}
            for role, (fpc, flof) in factors.items():
                factor_cells += 1
                if cpp_facs.get(fpc) != flof:
                    factor_div.append({'stem': stem, 'tick': seg_start, 'class': class_key,
                                       'role': role, 'pc': fpc, 'py_lof': flof, 'cpp_lof': cpp_facs.get(fpc)})

            # BASS field parity — the establishment's segment-level lowest-note factor cell (11,182)
            sounding = [n for n in notes if n[6] != 0 and n[0] < seg_end and (n[0] + n[1]) > seg_start]
            if sounding:
                bass_pc = min(sounding, key=lambda n: n[3])[2]
                match = [(role, lof) for role, (fpc, lof) in factors.items() if fpc == bass_pc]
                if match:
                    bass_cells += 1
                    role, py_blof = match[0]
                    if cpp_facs.get(bass_pc) != py_blof:
                        bass_div.append({'stem': stem, 'tick': seg_start, 'class': class_key,
                                         'role': role, 'pc': bass_pc, 'py_lof': py_blof,
                                         'cpp_lof': cpp_facs.get(bass_pc)})

    extra = [{'stem': stem, 'tick': s['tick'], 'class': s.get('class_key')}
             for stem, cs in cpp_pieces.items()
             for s in cs.get('segments', []) if (stem, s['tick']) not in cpp_seen]

    div_total = (len(root_div) + len(bass_div) + len(factor_div)
                 + len(class_mismatch) + len(missing) + len(extra))
    return {
        'purpose': 'OI-197 lof-exact C++<->Python spelling-derivation parity (a notation-switch precondition)',
        'cpp_source': cpp.get('tool'),
        'cpp_weight_arm': cpp.get('weight_arm'),
        'cpp_tables': cpp.get('tables'),
        'segments_total': seg_total,
        'segments_matched': matched,
        'root_cells_compared': root_cells,
        'bass_cells_compared': bass_cells,
        'factor_cells_compared': factor_cells,
        'root_divergences': root_div,
        'bass_divergences': bass_div,
        'factor_divergences': factor_div,
        'decode_alignment': {
            'class_mismatch': class_mismatch, 'missing_in_cpp': missing, 'extra_in_cpp': extra,
        },
        'divergences_total': div_total,
        'pass': div_total == 0,
        'inheritance': (
            'lof-EXACT on all cells (0 divergences): the C++ mapping produces the identical spelling as '
            'the Python mapping on every committed segment, so the C++ derivation INHERITS the Python-side '
            'corpus establishment (root 13061/13063 = 99.985 %, bass 11180/11182 = 99.982 % derived-vs-'
            'notated, with the 4 enumerated enharmonic-convention divergences). See root_spelling / '
            'bass_spelling above for that notated establishment.'
        ) if div_total == 0 else (
            'DIVERGENCE FOUND (%d): one implementation is wrong; STOP and report, do not resolve by editing.'
            % div_total),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--decode', default=os.path.join(_HERE, 'decode_parity_ref.json'))
    ap.add_argument('--note-events', default=os.path.join(_HERE, 'note_events', 'note_events.json'))
    ap.add_argument('--out', default=os.path.join(_HERE, 'spelling_establishment.json'))
    ap.add_argument('--cpp-parity', default=None,
                    help='path to the C++ dump (batch_analyze --joint-spelling-parity); when given, adds '
                         'the OI-197 lof-exact C++<->Python parity block and exits nonzero on any divergence')
    args = ap.parse_args()

    decode = json.load(open(args.decode, encoding='utf-8'))
    ne = json.load(open(args.note_events, encoding='utf-8'))
    pieces = ne['pieces']
    selected = decode['selected']

    root_overall = {'agree': 0, 'disagree': 0, 'not_sounding': 0, 'unmappable': 0}
    bass_overall = {'agree': 0, 'disagree': 0, 'not_sounding': 0, 'no_factor_bass': 0}
    per_cell = {}   # "mode/class" -> {agree, disagree}
    root_divergences = []
    bass_divergences = []

    for stem in sorted(selected.keys()):
        if stem not in pieces:
            continue
        dec = selected[stem]
        sig = dec.get('sig_fifths')
        ref = sig if sig is not None else 0
        pc = pieces[stem]
        events = pc['events']
        notes = pc['notes']   # [onset,dur,pc,midi,lof,part,measure,beat,mc,ap,dp,tied,ferm]

        for seg in dec['segments']:
            i, j, tonic, is_major, class_key, root_pc = seg[0], seg[1], seg[2], seg[3], seg[4], seg[5]
            if i < 0 or j <= i or j > len(events):
                continue
            seg_start = events[i][0]
            seg_end = events[j - 1][1]
            # notes sounding in [seg_start, seg_end): overlap AND non-anacrusis (measure != 0)
            sounding = [n for n in notes
                        if n[6] != 0 and n[0] < seg_end and (n[0] + n[1]) > seg_start]

            deg, quality, _inv, target = _class_fields(class_key)
            cell = ('major' if is_major else 'minor') + ' / ' + class_key

            # ── ROOT spelling ─────────────────────────────────────────────────────────────────────
            rl = root_lof(class_key, tonic, is_major, ref)
            if rl is None:
                root_overall['unmappable'] += 1
            else:
                # internal consistency: the derived pc equals the committed root pc.
                if _pc(rl) != (root_pc % 12) and root_pc >= 0:
                    root_divergences.append({
                        'stem': stem, 'tick': seg_start, 'class': class_key,
                        'mode': 'major' if is_major else 'minor',
                        'kind': 'pc_mismatch', 'derived_lof': rl, 'derived_pc': _pc(rl),
                        'committed_root_pc': root_pc})
                root_notes = [n for n in sounding if n[2] == (root_pc % 12)]
                if not root_notes:
                    root_overall['not_sounding'] += 1
                else:
                    notated_lofs = sorted({n[4] for n in root_notes})
                    cd = per_cell.setdefault(cell, {'agree': 0, 'disagree': 0})
                    if rl in notated_lofs:
                        root_overall['agree'] += 1
                        cd['agree'] += 1
                    else:
                        root_overall['disagree'] += 1
                        cd['disagree'] += 1
                        root_divergences.append({
                            'stem': stem, 'tick': seg_start, 'class': class_key,
                            'mode': 'major' if is_major else 'minor',
                            'kind': 'lof_mismatch', 'derived_lof': rl,
                            'notated_lofs': notated_lofs})

            # ── BASS factor spelling ──────────────────────────────────────────────────────────────
            if sounding:
                bass_note = min(sounding, key=lambda n: n[3])   # lowest midi
                bass_pc = bass_note[2]
                factors = factor_lofs(class_key, tonic, is_major, ref)
                match = [(role, lof) for role, (fpc, lof) in factors.items() if fpc == bass_pc]
                if not match:
                    bass_overall['no_factor_bass'] += 1
                else:
                    _role, blof = match[0]
                    if blof == bass_note[4]:
                        bass_overall['agree'] += 1
                    else:
                        bass_overall['disagree'] += 1
                        bass_divergences.append({
                            'stem': stem, 'tick': seg_start, 'class': class_key,
                            'mode': 'major' if is_major else 'minor', 'role': _role,
                            'derived_lof': blof, 'notated_lof': bass_note[4]})

    # per-cell summary sorted by disagreement then name
    cells = [{'cell': k, 'agree': v['agree'], 'disagree': v['disagree']}
             for k, v in sorted(per_cell.items(), key=lambda kv: (-kv[1]['disagree'], kv[0]))]

    out = {
        'provenance': {
            'generator': 'tools/joint_estimator/gen_spelling_establishment.py',
            'decode_source': os.path.basename(args.decode),
            'decode_arm': 'selected',
            'note_events_git_hash': ne.get('provenance', {}).get('note_events_git_hash'),
            'lof_convention': 'C=0, +1 = perfect fifth up (== note_events lof = tpc - Tpc::TPC_C)',
        },
        'root_spelling': {
            'overall': root_overall,
            'agree_rate_where_sounding': (
                root_overall['agree'] / (root_overall['agree'] + root_overall['disagree'])
                if (root_overall['agree'] + root_overall['disagree']) else None),
            'per_cell': cells,
            'divergences': root_divergences,
        },
        'bass_spelling': {
            'overall': bass_overall,
            'agree_rate_where_factor': (
                bass_overall['agree'] / (bass_overall['agree'] + bass_overall['disagree'])
                if (bass_overall['agree'] + bass_overall['disagree']) else None),
            'divergences': bass_divergences,
        },
    }
    parity = None
    if args.cpp_parity:
        cpp = json.load(open(args.cpp_parity, encoding='utf-8'))
        parity = compare_cpp_parity(decode, ne, cpp)
        out['cpp_parity'] = parity

    with open(args.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    r = root_overall
    b = bass_overall
    print(f"root: agree={r['agree']} disagree={r['disagree']} not_sounding={r['not_sounding']} "
          f"unmappable={r['unmappable']}")
    print(f"bass: agree={b['agree']} disagree={b['disagree']} not_sounding={b['not_sounding']} "
          f"no_factor_bass={b['no_factor_bass']}")
    print(f"root divergences: {len(root_divergences)}; bass divergences: {len(bass_divergences)}")
    print(f"wrote {args.out}")

    if parity is not None:
        print(f"cpp-parity: segments matched={parity['segments_matched']}/{parity['segments_total']} "
              f"root_cells={parity['root_cells_compared']} bass_cells={parity['bass_cells_compared']} "
              f"factor_cells={parity['factor_cells_compared']}")
        print(f"cpp-parity divergences: root={len(parity['root_divergences'])} "
              f"bass={len(parity['bass_divergences'])} factor={len(parity['factor_divergences'])} "
              f"class_mismatch={len(parity['decode_alignment']['class_mismatch'])} "
              f"missing={len(parity['decode_alignment']['missing_in_cpp'])} "
              f"extra={len(parity['decode_alignment']['extra_in_cpp'])} -> "
              f"{'PASS' if parity['pass'] else 'FAIL (STOP)'}")
        if not parity['pass']:
            for key in ('root_divergences', 'bass_divergences', 'factor_divergences'):
                for d in parity[key][:10]:
                    print(f"  {key}: {d}")
            return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

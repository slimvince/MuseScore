#!/usr/bin/env python3
"""Transposition-equivariance probe for the production joint-estimator decode.

READ-ONLY exploratory measurement (the #17 funnel's read-only-probe stage; surprises are the
desired product here). Nothing under the repository is written: sys.dont_write_bytecode is set
BEFORE any repo import, and all artifacts go to this script's own directory.

THE QUESTION: if a piece's note events are transposed by k semitones (with a consistent
line-of-fifths respelling and the signature-fifths input shifted to match), does the decode
transpose with it — every committed key tonic and chord root shifted by k (mod 12), the
class labels and segment boundaries identical?

INPUT TRANSPOSITION (declared):
  k semitones maps to a line-of-fifths shift f_raw with 7*f_raw == k (mod 12), folded into
  (-6, 6] :  +2 st -> +2 fifths;  -3 st -> +3 fifths;  +6 st -> +6 fifths (the SHARPWARD
  tritone spelling is chosen for the ambiguous +6 case, and stated).
  Per piece the ACTUAL uniform respell delta is chosen the way an engraver would: the
  transposed signature is sig_t = _fold_fifths_diff(sig + f_raw) (the repo's ONE fifths-folding
  helper, gen_label_tables._fold_fifths_diff, folding into (-6,6]), and delta_lof = sig_t - sig
  (== f_raw mod 12). Every note: pc -> (pc+k)%12, midi -> midi+k, lof -> lof+delta_lof.
  Events carry no pitch and are unchanged; approach/departure (melodic contour), tied, fermata,
  measure, beat are transposition-invariant and unchanged. declared_mode is unchanged.
  If sig is None (no header), sig_t = None and delta_lof = f_raw.

Phases (resumable — each invocation does work until the time budget, then exits; state on disk):
  establish  : decode the 12 sample pieces untransposed; must reproduce decode_parity_ref.json
               ('selected' arm) segments + total_score exactly. Mismatch => STOP.
  transpose  : decode each sample piece at k in {+2, -3, +6}; the untransposed reference is the
               ESTABLISHED parity ref itself (phase 1 proved this decode reproduces it exactly);
               compare per segment; diagnose every violation.
"""
from __future__ import annotations

import bisect
import json
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True          # NEVER write .pyc into the read-only repository

REPO = Path("/sessions/adoring-admiring-fermi/mnt/MS")
OUT = Path("/sessions/adoring-admiring-fermi/mnt/outputs/transposition_probe")
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(REPO / "tools" / "joint_estimator"))

import probe_decoder as pd              # noqa: E402  the pinned production reference decoder
import gen_label_tables as glt          # noqa: E402  _fold_fifths_diff / _collection_fifths / _PC_TO_FIFTHS

# the report-only per-segment posterior is skipped (it runs AFTER the backtrack and moves neither
# the committed segments nor total_score — the same skip gen_window_study.py uses and established).
pd._segment_posterior = lambda *a, **k: []

SEG_CAP = 4                              # the production config (OI-178 adoption; parity ref arm)
SHIFTS = [2, -3, 6]
K_TO_F = {2: 2, -3: 3, 6: 6}             # semitones -> raw fifths shift in (-6,6]; 7*f == k (mod 12)
PCF = glt._PC_TO_FIFTHS
BUDGET = 33.0                            # seconds of work per invocation (sandbox call cap 45 s)

_T0 = time.perf_counter()


def load_apparatus(sample_only=True):
    parity = json.loads((REPO / "tools/joint_estimator/decode_parity_ref.json")
                        .read_text(encoding="utf-8"))
    stems = sorted(parity["selected"])
    sample = stems[::27][:12]            # every 27th of the name-sorted covered list, first 12
    d = json.loads((REPO / "tools/joint_estimator/note_events/note_events.json")
                   .read_text(encoding="utf-8"))
    prov = d["provenance"]
    if prov.get("ticks_per_quarter") != pd.TICKS_PER_QUARTER:
        raise SystemExit("STOP: ticks_per_quarter mismatch")
    pieces = {}
    for stem in (sample if sample_only else stems):
        p = d["pieces"][stem]
        pc = pd.Piece(stem=stem, events=p["events"], notes=p["notes"],
                      n_quarter=p["n_quarter"], meter=tuple(p["meter"]) if p["meter"] else None)
        pc.prepare()
        pieces[stem] = pc
    adapter = pd.FittedAdapter(leftover_mode="freq", table_set="all",
                               weights=parity["selected_weights"])
    adapter.mode_marginal("major")
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()
    return parity, pieces, prov, adapter, vocab, cache, sample


def decode(piece, adapter, vocab, cache, sig, dm):
    return pd.decode_piece(piece, adapter, vocab, cache, seg_cap=SEG_CAP,
                           sig_fifths=sig, declared_mode=dm)


def seg_tuple(s):
    return (s["i"], s["j"], s["tonic_pc"], s["is_major"], s["class_key"])


def transpose_piece(piece, k, sig):
    f_raw = K_TO_F[k]
    if sig is None:
        sig_t, dlof = None, f_raw
    else:
        sig_t = glt._fold_fifths_diff(sig + f_raw)
        dlof = sig_t - sig               # == f_raw (mod 12); the uniform engraver respell
    notes = []
    for n in piece.notes:
        m = list(n)
        m[pd.N_PC] = (m[pd.N_PC] + k) % 12
        m[pd.N_MIDI] = m[pd.N_MIDI] + k
        m[pd.N_LOF] = m[pd.N_LOF] + dlof
        notes.append(m)
    tp = pd.Piece(stem=piece.stem, events=[list(e) for e in piece.events],
                  notes=notes, n_quarter=piece.n_quarter, meter=piece.meter)
    tp.prepare()
    return tp, sig_t, dlof


def sig_key_of(sig):
    if sig is None:
        return None
    for (t, m) in pd.KEYS_24:
        if m and glt._collection_fifths(t, m) == sig:
            return (t, m)
    return None


def ref_segments_from_parity(ps, piece):
    """The established untransposed reference reading, reconstructed from the parity ref
    (phase 1 proved the decode reproduces it exactly, segments AND total_score)."""
    out = []
    for (i, j, t, m, ck, root) in ps["segments"]:
        out.append({"i": i, "j": j,
                    "start_tick": piece.events[i][pd.EV_START],
                    "end_tick": piece.events[j - 1][pd.EV_END],
                    "tonic_pc": t, "is_major": m, "class_key": ck, "root_pc": root})
    return out


def _load_state(name):
    p = OUT / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def _save_state(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=1), encoding="utf-8")


def phase_establish():
    state = _load_state("establish_state.json")
    parity, pieces, prov, adapter, vocab, cache, sample = load_apparatus()
    state.setdefault("sample", sample)
    state.setdefault("note_events_git_hash", prov.get("corpus_git_hash"))
    state.setdefault("seg_cap", SEG_CAP)
    results = state.setdefault("results", {})
    for stem in sample:
        if stem in results:
            continue
        if time.perf_counter() - _T0 > BUDGET:
            _save_state("establish_state.json", state)
            print(f"BUDGET: {len(results)}/{len(sample)} done — rerun to continue", flush=True)
            return 2
        ps = parity["selected"][stem]
        sig, dm = ps["sig_fifths"], ps["declared_mode"]
        hdr_sig, hdr_dm = pd.piece_header(stem)     # cross-check the header source (read-only)
        t0 = time.perf_counter()
        res = decode(pieces[stem], adapter, vocab, cache, sig, dm)
        got = [seg_tuple(s) for s in res.segments]
        exp = [(i, j, t, m, ck) for (i, j, t, m, ck, _r) in ps["segments"]]
        seg_match = got == exp
        score_match = abs(res.total_score - ps["total_score"]) < 1e-6
        results[stem] = {
            "ok": bool(seg_match and score_match), "seg_match": seg_match,
            "score_match": score_match, "n_seg": len(got), "n_seg_exp": len(exp),
            "score_got": res.total_score, "score_exp": ps["total_score"],
            "sig_fifths": sig, "declared_mode": dm,
            "header_crosscheck_ok": (hdr_sig == sig and (hdr_dm or "") == (dm or "")),
            "decode_seconds": round(time.perf_counter() - t0, 2),
        }
        print(f"  {stem}: ok={results[stem]['ok']} ({len(got)} segs)", flush=True)
        _save_state("establish_state.json", state)
    ok_all = all(r["ok"] for r in results.values()) and len(results) == len(sample)
    state["ok_all"] = ok_all
    state["complete"] = True
    _save_state("establish_state.json", state)
    print(f"ESTABLISH {'PASS 12/12' if ok_all else 'FAIL — STOP'}", flush=True)
    return 0 if ok_all else 1


def factor_delta(piece_a, state_a, piece_b, state_b, i, j, adapter, cache, vocab):
    """Per-factor raw feature values for (piece_a,state_a) vs (piece_b,state_b) on span [i,j)."""
    fa = pd.segment_features(piece_a, i, j, state_a[0], state_a[1],
                             vocab.classes[state_a[2]], adapter, cache)
    fb = pd.segment_features(piece_b, i, j, state_b[0], state_b[1],
                             vocab.classes[state_b[2]], adapter, cache)
    if fa is None or fb is None:
        return {"a": fa, "b": fb, "delta": None}
    return {"a": {k: round(v, 6) for k, v in fa.items()},
            "b": {k: round(v, 6) for k, v in fb.items()},
            "delta": {k: round(fb[k] - fa[k], 6) for k in fa}}


def run_condition(stem, k, parity, piece, adapter, vocab, cache):
    ps = parity["selected"][stem]
    sig, dm = ps["sig_fifths"], ps["declared_mode"]
    ref_segs = ref_segments_from_parity(ps, piece)
    tp, sig_t, dlof = transpose_piece(piece, k, sig)
    res = decode(tp, adapter, vocab, cache, sig_t, dm)
    t_segs = res.segments
    cond = {"sig_fifths": sig, "sig_t": sig_t, "delta_lof": dlof, "declared_mode": dm,
            "total_score_ref": round(ps["total_score"], 6),
            "total_score_trans": round(res.total_score, 6),
            "total_score_delta": round(res.total_score - ps["total_score"], 6),
            "n_segments_ref": len(ref_segs), "n_segments_trans": len(t_segs)}
    # committed-tonic canonical-spelling wrap flags (the predicted spelling mechanism)
    cond["tonic_lof_wrap_pcs"] = sorted({t0 for t0 in {s["tonic_pc"] for s in ref_segs}
                                         if PCF[(t0 + k) % 12] != PCF[t0] + dlof})
    ref_b = [(s["start_tick"], s["end_tick"]) for s in ref_segs]
    t_b = [(s["start_tick"], s["end_tick"]) for s in t_segs]
    cond["boundaries_identical"] = (ref_b == t_b)
    viols = []
    n_cmp = n_match = 0
    if ref_b == t_b:
        for idx, (r, t) in enumerate(zip(ref_segs, t_segs)):
            n_cmp += 1
            exp_tonic = (r["tonic_pc"] + k) % 12
            exp_root = None if r["root_pc"] is None else (r["root_pc"] + k) % 12
            ok = (t["tonic_pc"] == exp_tonic and t["is_major"] == r["is_major"]
                  and t["class_key"] == r["class_key"] and t["root_pc"] == exp_root)
            if ok:
                n_match += 1
                continue
            i, j = r["i"], r["j"]
            exp_state = (exp_tonic, r["is_major"], r["class_key"])
            obs_state = (t["tonic_pc"], t["is_major"], t["class_key"])
            cands = pd._candidate_states_for_segment(
                tp, i, j, vocab, cache, pd.KEYS_24, sig_key_of(sig_t))
            exp_content = pd.score_segment_content(
                tp, i, j, exp_state[0], exp_state[1], vocab.classes[exp_state[2]],
                adapter, cache)
            obs_content = pd.score_segment_content(
                tp, i, j, obs_state[0], obs_state[1], vocab.classes[obs_state[2]],
                adapter, cache)
            viols.append({
                "seg_index": idx, "tick": r["start_tick"],
                "span": [r["start_tick"], r["end_tick"]],
                "expected": {"tonic_pc": exp_tonic, "is_major": r["is_major"],
                             "class_key": r["class_key"], "root_pc": exp_root,
                             "key": pd._key_string(exp_tonic, r["is_major"])},
                "observed": {"tonic_pc": t["tonic_pc"], "is_major": t["is_major"],
                             "class_key": t["class_key"], "root_pc": t["root_pc"],
                             "key": t["key"]},
                "expected_state_in_candidates": exp_state in cands,
                "content_score_expected": (None if exp_content == pd.NEG_INF
                                           else round(exp_content, 6)),
                "content_score_observed": (None if obs_content == pd.NEG_INF
                                           else round(obs_content, 6)),
                # which factor moved: original committed state on the ORIGINAL piece vs the
                # shifted expected state on the TRANSPOSED piece (equivariance predicts all-0)
                "factor_delta_orig_vs_expected": factor_delta(
                    piece, (r["tonic_pc"], r["is_major"], r["class_key"]),
                    tp, exp_state, i, j, adapter, cache, vocab),
            })
    else:
        cond["boundary_diff"] = {"ref_only": [b for b in ref_b if b not in t_b][:40],
                                 "trans_only": [b for b in t_b if b not in ref_b][:40]}
        starts = [s["start_tick"] for s in t_segs]
        for idx, r in enumerate(ref_segs):
            n_cmp += 1
            tk = r["start_tick"]
            si = bisect.bisect_right(starts, tk) - 1
            t = t_segs[si] if 0 <= si < len(t_segs) else None
            exp_tonic = (r["tonic_pc"] + k) % 12
            exp_root = None if r["root_pc"] is None else (r["root_pc"] + k) % 12
            ok = (t is not None and t["start_tick"] == r["start_tick"]
                  and t["end_tick"] == r["end_tick"]
                  and t["tonic_pc"] == exp_tonic and t["is_major"] == r["is_major"]
                  and t["class_key"] == r["class_key"] and t["root_pc"] == exp_root)
            if ok:
                n_match += 1
            else:
                viols.append({
                    "seg_index": idx, "tick": tk, "type": "boundary_or_label_at_tick",
                    "expected": {"span": [r["start_tick"], r["end_tick"]],
                                 "tonic_pc": exp_tonic, "is_major": r["is_major"],
                                 "class_key": r["class_key"], "root_pc": exp_root},
                    "observed": (None if t is None else
                                 {"span": [t["start_tick"], t["end_tick"]],
                                  "tonic_pc": t["tonic_pc"], "is_major": t["is_major"],
                                  "class_key": t["class_key"], "root_pc": t["root_pc"]}),
                })
    cond["n_segments_compared"] = n_cmp
    cond["n_segments_matched"] = n_match
    cond["violations"] = viols
    return cond


def phase_transpose():
    est = _load_state("establish_state.json")
    if not est.get("ok_all"):
        print("STOP: establishment has not passed — refusing to transpose", flush=True)
        return 1
    state = _load_state("transpose_state.json")
    parity, pieces, prov, adapter, vocab, cache, sample = load_apparatus()
    state.setdefault("sample", sample)
    state.setdefault("shifts", SHIFTS)
    state.setdefault("seg_cap", SEG_CAP)
    state.setdefault("note_events_git_hash", prov.get("corpus_git_hash"))
    conds = state.setdefault("conditions", {})
    for stem in sample:
        for k in SHIFTS:
            ck = f"{stem}|{k:+d}"
            if ck in conds:
                continue
            if time.perf_counter() - _T0 > BUDGET:
                _save_state("transpose_state.json", state)
                print(f"BUDGET: {len(conds)}/{len(sample) * len(SHIFTS)} conditions done — "
                      f"rerun to continue", flush=True)
                return 2
            cond = run_condition(stem, k, parity, pieces[stem], adapter, vocab, cache)
            conds[ck] = cond
            print(f"  {ck}: {cond['n_segments_matched']}/{cond['n_segments_compared']} matched, "
                  f"boundaries_identical={cond['boundaries_identical']}", flush=True)
            _save_state("transpose_state.json", state)
    tot_cmp = sum(c["n_segments_compared"] for c in conds.values())
    tot_match = sum(c["n_segments_matched"] for c in conds.values())
    state["totals"] = {"segments_compared": tot_cmp, "segments_matched": tot_match,
                       "match_fraction": (tot_match / tot_cmp if tot_cmp else None)}
    state["complete"] = True
    _save_state("transpose_state.json", state)
    print(f"TOTAL: {tot_match}/{tot_cmp} segments matched "
          f"({100.0 * tot_match / tot_cmp:.2f}%)", flush=True)
    return 0


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "establish"
    rc = phase_establish() if phase == "establish" else phase_transpose()
    sys.exit(rc)

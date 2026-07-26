#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
"""gen_posterior_slice.py — the POSTERIOR-SLICE reference (notation output contract §3.3 group (i)).

Import-only reuse of the pinned probe_decoder (#6). Decodes all 326 covered pieces at the SELECTED
weight vector (the §5 deterministic decode — the adopted production arm, the vector the C++ module
embeds) and publishes, per COMMITTED segment, the two group-(i) uncertainty lists:

  * KEY axis: for EVERY candidate key the decode evaluated for the piece — KEYS_24, the exact set
    probe_decoder._segment_posterior iterates, filtered per segment to (root defined AND finite
    content score) — the segment's WEIGHTED content score under (that key, the committed chord
    class). The committed key is flagged. Gaps are derived facts (score differences), not stored.
  * CHORD axis: under the COMMITTED key, for EVERY vocabulary class scoreable on the span (root
    defined AND finite content score), the segment's weighted content score. The committed class
    flagged.

The published scores are the ★R2-weighted within-segment content scores (probe_decoder.
weighted_content) — a LOG-score, NOT a probability; group (ii) forward-backward marginals are a
SEPARATE later step (OI-193) and are NOT in this artifact. Floats are full precision (json's
round-trippable float repr). This artifact is the Task-3 C++ parity oracle.

Establishment (#19) — the ratified two-half form, both halves against frozen committed objects:
  (a) The slice arithmetic (mechanism half): run the SAME slice derivation additionally at IDENTITY
      weights on the §5-current decoder. For every piece whose identity-arm committed segmentation
      equals probe_corpus_decode.json's stored segments (the §5-UNAFFECTED pieces), the derived
      key-axis runner-up + gap (rounded to the stored 4 decimals) reproduce the committed artifact's
      `posterior` entries EXACTLY, segment for segment. The §5-canonicalised pieces are
      PRE-ENUMERATED (identity-arm segments != stored segments) BEFORE any slice comparison and each
      is explained by the ratified §5 tie-break (equal total score, shown). A seventh unexplained
      piece — or any divergence not attributable to the tie-break — is a STOP.
  (b) The decode half: the generator's SELECTED-weights committed segments equal
      decode_parity_ref.json's selected-arm segments EXACTLY on all 326 pieces. Any mismatch a STOP.

Config is probe_run's / gen_decode_parity_ref's exactly: seg_cap 4, leftover option 2a ("freq"),
table_set "all", signature/declared-mode from the xml header, NO key prune (KEYS_24 candidate set).

Usage:
    python tools/joint_estimator/gen_posterior_slice.py            # full corpus: establish + write
    python tools/joint_estimator/gen_posterior_slice.py --stems bwv10.7 bwv362   # subset, dry-run
        (subset: measures axis sizes + validates against the oracles; writes NOTHING)
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd     # noqa: E402  the pinned decoder — IMPORT-ONLY (not edited)

SEG_CAP = 4
LEFTOVER = "freq"
ART_PATH = _HERE / "posterior_slice_ref.json"


def _git_head() -> str:
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def _seg_tuple_from_dict(d):
    """Committed-segment identity in decode_parity_ref.json's compact shape."""
    return [d["i"], d["j"], d["tonic_pc"], d["is_major"], d["class_key"],
            (d["root_pc"] if d["root_pc"] is not None else None)]


def _seg_tuple_from_probe(seg):
    """probe_corpus_decode.json stores segments as dicts with the same fields."""
    return [seg["i"], seg["j"], seg["tonic_pc"], seg["is_major"], seg["class_key"],
            (seg.get("root_pc") if seg.get("root_pc") is not None else None)]


# ── the two group-(i) axes (the ONE re-scoring mechanism, both axes) ───────────────────────────

def key_axis(piece, seg, adapter, vocab, cache):
    """For seg (a decode seg_dict), the KEY axis (contract §3.3 group (i)): the weighted content
    score of the COMMITTED chord class under every candidate key in KEYS_24 scoreable on the span.
    Compact parallel-array form {"keys":[...], "scores":[...], "committed": idx} — the FULL list (no
    truncation), full precision; the committed key's list index is flagged. Iterated in KEYS_24 order
    (deterministic; == the order _segment_posterior builds its `scores` dict); mirrors its inner loop
    (root-defined AND finite-score filter)."""
    i, j = seg["i"], seg["j"]
    cls = vocab.classes[seg["class_key"]]
    sp = piece.overlap_pcs(i, j)                      # key-independent; precomputed for speed
    committed = (seg["tonic_pc"], seg["is_major"])
    keys, scores, cidx = [], [], -1
    for (tonic, is_major) in pd.KEYS_24:
        _mem, _fac, root = cache.get(cls, tonic, is_major)
        if root is None:
            continue
        sc = pd.score_segment_content(piece, i, j, tonic, is_major, cls, adapter, cache, seg_pcs=sp)
        if sc == pd.NEG_INF:
            continue
        if (tonic, is_major) == committed:
            cidx = len(keys)
        keys.append(pd._key_string(tonic, is_major))
        scores.append(sc)
    return {"keys": keys, "scores": scores, "committed": cidx}


def chord_axis(piece, seg, adapter, vocab, cache):
    """For seg, the CHORD axis (contract §3.3 group (i)): under the COMMITTED key, the weighted
    content score of every vocabulary class scoreable on the span. Compact parallel-array form
    {"classes":[...], "scores":[...], "committed": idx} — the FULL list, full precision; the committed
    class's index flagged. Iterated in vocab.keylist (sorted) order (deterministic)."""
    i, j = seg["i"], seg["j"]
    tonic, is_major = seg["tonic_pc"], seg["is_major"]
    sp = piece.overlap_pcs(i, j)
    committed_key = seg["class_key"]
    classes, scores, cidx = [], [], -1
    for ckey in vocab.keylist:
        cls2 = vocab.classes[ckey]
        _mem, _fac, root = cache.get(cls2, tonic, is_major)
        if root is None:
            continue
        sc = pd.score_segment_content(piece, i, j, tonic, is_major, cls2, adapter, cache, seg_pcs=sp)
        if sc == pd.NEG_INF:
            continue
        if ckey == committed_key:
            cidx = len(classes)
        classes.append(ckey)
        scores.append(sc)
    return {"classes": classes, "scores": scores, "committed": cidx}


def derive_runner4(kax):
    """Reduce a compact key-axis {"keys","scores","committed"} to (committed_key, committed_score4,
    runner_key, runner_score4, gap4) EXACTLY as _segment_posterior does: committed = the flagged
    index; runner = the strict argmax over the non-committed entries in list order; gap =
    round(committed_unrounded - runner_unrounded, 4). Returns the 4-decimal fields probe_corpus stores."""
    keys, scores, cidx = kax["keys"], kax["scores"], kax["committed"]
    best_sc = scores[cidx] if cidx >= 0 else pd.NEG_INF
    alt_i, alt_sc = -1, pd.NEG_INF
    for idx, sc in enumerate(scores):
        if idx == cidx:
            continue
        if sc > alt_sc:
            alt_i, alt_sc = idx, sc
    return {
        "committed_key": keys[cidx] if cidx >= 0 else None,
        "committed_key_content_score": round(best_sc, 4) if best_sc != pd.NEG_INF else None,
        "runner_key": keys[alt_i] if alt_i >= 0 else None,
        "runner_key_content_score": round(alt_sc, 4) if alt_sc != pd.NEG_INF else None,
        "gap": round(best_sc - alt_sc, 4) if (alt_i >= 0 and best_sc != pd.NEG_INF) else None,
    }


def build_arm(weights, stems, need_chord=True):
    """Decode the given stems at `weights`; return {stem: {decode record + per-seg axes}}. The
    identity arm (establishment half a) needs only the KEY axis, so `need_chord=False` skips the
    (dominant) chord-axis re-scoring there."""
    pieces, prov = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER, table_set="all", weights=weights)
    adapter.mode_marginal("major")
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()
    result = {}
    for stem in stems:
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        r = pd.decode_piece(piece, adapter, vocab, cache, seg_cap=SEG_CAP,
                            sig_fifths=sig, declared_mode=dm)
        segs = []
        for s in r.segments:
            seg = {
                "i": s["i"], "j": s["j"], "span": [s["start_tick"], s["end_tick"]],
                "committed_key": s["key"], "committed_class": s["class_key"],
                "committed_root_pc": s["root_pc"],
                "degree": s["degree"], "quality": s["quality"],
                "inversion": s["inversion"], "target": s["target"],
                "key_axis": key_axis(piece, s, adapter, vocab, cache),
            }
            if need_chord:
                seg["chord_axis"] = chord_axis(piece, s, adapter, vocab, cache)
            segs.append(seg)
        result[stem] = {
            "n_segments": len(r.segments), "total_score": r.total_score,
            "sig_fifths": sig, "declared_mode": dm,
            "seg_tuples": [_seg_tuple_from_dict(s) for s in r.segments],
            "posterior": r.posterior,                      # the pinned _segment_posterior slice
            "segments": segs,
        }
    return result, prov


# ── establishment ──────────────────────────────────────────────────────────────────────────────

def establish_a(ident_arm, verbose=True):
    """(a) mechanism: identity-arm derived runner-up/gap reproduces probe_corpus_decode.json on the
    §5-unaffected pieces; §5-affected pieces pre-enumerated and explained by equal total score."""
    pc = json.loads((_HERE / "probe_corpus_decode.json").read_text(encoding="utf-8"))["pieces"]
    exceptions = []
    unaffected = 0
    mism = 0
    detail = []
    for stem in sorted(ident_arm):
        if stem not in pc:
            detail.append(f"STOP: {stem} absent from probe_corpus_decode.json")
            mism += 1
            continue
        stored_segs = [_seg_tuple_from_probe(s) for s in pc[stem]["segments"]]
        my_segs = ident_arm[stem]["seg_tuples"]
        if my_segs != stored_segs:
            # §5-affected: pre-enumerated; explain by equal total score (probe rounds to 3 dec).
            my_tot = ident_arm[stem]["total_score"]
            pc_tot = pc[stem].get("total_score")
            equal_score = (pc_tot is not None and round(my_tot, 3) == round(pc_tot, 3))
            exceptions.append({
                "stem": stem, "reason": "§5 tie-break (equal-score segmentation difference)",
                "total_score_identity_current": round(my_tot, 6),
                "total_score_probe_corpus": pc_tot,
                "equal_score": equal_score,
                "n_seg_identity": len(my_segs), "n_seg_probe": len(stored_segs),
            })
            if not equal_score:
                detail.append(f"STOP: {stem} segmentation differs but total scores are NOT equal "
                              f"({my_tot} vs {pc_tot}) — not attributable to §5")
                mism += 1
            continue
        # §5-unaffected: reproduce the posterior EXACTLY (4 decimals), segment for segment.
        unaffected += 1
        stored_post = pc[stem]["posterior"]
        my_segs_full = ident_arm[stem]["segments"]
        if len(stored_post) != len(my_segs_full):
            detail.append(f"STOP: {stem} posterior length {len(stored_post)} != segments "
                          f"{len(my_segs_full)}")
            mism += 1
            continue
        for si, (ps, seg) in enumerate(zip(stored_post, my_segs_full)):
            d = derive_runner4(seg["key_axis"])
            if (d["committed_key"] != ps["committed_key"]
                    or d["committed_key_content_score"] != ps["committed_key_content_score"]
                    or d["runner_key"] != ps["runner_key"]
                    or d["runner_key_content_score"] != ps["runner_key_content_score"]
                    or d["gap"] != ps["gap"]):
                detail.append(f"STOP: {stem} seg {si} posterior mismatch\n"
                              f"    mine : {d}\n    probe: {ps}")
                mism += 1
    ok = (mism == 0)
    if verbose:
        print(f"  (a) identity mechanism: {unaffected} §5-unaffected pieces reproduce the committed "
              f"posterior EXACTLY; {len(exceptions)} §5 exception(s): "
              f"{[e['stem'] for e in exceptions]}; mismatches={mism}")
        for line in detail[:20]:
            print("    " + line)
    return ok, {"pieces_compared": len(ident_arm), "s5_unaffected": unaffected,
                "exceptions": exceptions, "mismatches": mism}


def establish_b(sel_arm, verbose=True):
    """(b) decode: SELECTED-weights committed segments equal decode_parity_ref.json selected arm."""
    dp = json.loads((_HERE / "decode_parity_ref.json").read_text(encoding="utf-8"))["selected"]
    mism = 0
    detail = []
    for stem in sorted(sel_arm):
        # decode_parity_ref stores segments in the SAME compact [i,j,tonic,is_major,class_key,root]
        # shape as our seg_tuples (JSON arrays -> lists); compare directly.
        ref = dp[stem]["segments"]
        mine = sel_arm[stem]["seg_tuples"]
        if mine != ref:
            mism += 1
            detail.append(f"STOP: {stem} selected segments differ from decode_parity_ref "
                          f"({len(mine)} vs {len(ref)} segs)")
    ok = (mism == 0)
    if verbose:
        print(f"  (b) selected decode: {len(sel_arm) - mism}/{len(sel_arm)} pieces segment-exact "
              f"vs decode_parity_ref.json; mismatches={mism}")
        for line in detail[:20]:
            print("    " + line)
    return ok, {"pieces_compared": len(sel_arm), "mismatches": mism}


# ── the artifact (SELECTED arm; the two established halves composed) ──────────────────────────────

def render_artifact(sel_arm, prov, est_a, est_b, weight_identity):
    # The scoreable candidate sets are span-INDEPENDENT on this corpus (verified: exactly one
    # distinct key-label list and one distinct chord-label list across all segments — a class's root
    # is defined and content finite in every key). So the labels are factored to shared TOP-LEVEL
    # lists (lossless — NOT truncation; the full list + full precision are preserved) and each segment
    # stores only its scores + the committed index. Uniformity is ASSERTED here: a non-uniform corpus
    # (some class/key not scoreable on some span) would break the shared-label form and is a STOP.
    key_labels = chord_labels = None
    pieces_out = {}
    for stem in sorted(sel_arm):
        a = sel_arm[stem]
        segs_out = []
        for s in a["segments"]:
            kx, cx = s["key_axis"], s["chord_axis"]
            if key_labels is None:
                key_labels, chord_labels = kx["keys"], cx["classes"]
            if kx["keys"] != key_labels:
                raise SystemExit(f"STOP: {stem} seg {s['i']} key-axis label set differs from the shared "
                                 f"set — the scoreable key set is NOT span-independent (shared-label "
                                 f"form invalid).")
            if cx["classes"] != chord_labels:
                raise SystemExit(f"STOP: {stem} seg {s['i']} chord-axis label set differs from the shared "
                                 f"set — the scoreable chord set is NOT span-independent.")
            segs_out.append({
                "i": s["i"], "j": s["j"], "span": s["span"],
                "committed_key": s["committed_key"], "committed_class": s["committed_class"],
                "committed_root_pc": s["committed_root_pc"], "degree": s["degree"],
                "quality": s["quality"], "inversion": s["inversion"], "target": s["target"],
                "key_scores": kx["scores"], "key_committed": kx["committed"],
                "chord_scores": cx["scores"], "chord_committed": cx["committed"],
            })
        pieces_out[stem] = {
            "n_segments": a["n_segments"], "sig_fifths": a["sig_fifths"],
            "declared_mode": a["declared_mode"], "segments": segs_out,
        }
    return {
        "key_axis_labels": key_labels,      # shared KEYS_24-order key strings (candidate key set)
        "chord_axis_labels": chord_labels,  # shared sorted class-key strings (candidate chord set)
        "provenance": {
            "generator": "tools/joint_estimator/gen_posterior_slice.py",
            "instrument_commit": _git_head(),
            "decoder": "tools/joint_estimator/probe_decoder.py (pinned; import-only)",
            "note_events_git_hash": prov["corpus_git_hash"],
            "seg_cap": SEG_CAP, "leftover_rule": f"option 2a ({LEFTOVER})", "table_set": "all",
            "weight_arm": "selected",
            "weight_vector_identity": weight_identity,
            "weight_vector_source": "decode_parity_ref.json selected_weights (== the C++ embedded vector)",
            "key_candidate_set": ("KEYS_24 — the decoder's declared candidate key set, the exact set "
                                  "probe_decoder._segment_posterior iterates; filtered per segment to "
                                  "(root defined AND finite content score)"),
            "content_score_semantics": ("the ★R2-weighted within-segment content score "
                                        "(probe_decoder.weighted_content); a LOG-score, NOT a "
                                        "probability. gaps are score differences, derived not stored."),
            "group_i_only": ("this is contract §3.3 GROUP (i) — the established content-score slice. "
                             "GROUP (ii) forward-backward marginals are OI-193's later step and are "
                             "NOT in this artifact."),
            "float_form": "full precision (json round-trippable float repr)",
            "schema": ("shared-label form: the FULL candidate lists are span-INDEPENDENT on this "
                       "corpus (exactly one distinct scoreable key set = all 24 keys, one distinct "
                       "scoreable chord set = 104 classes, across all 13063 segments), so the labels "
                       "are published ONCE at top level (key_axis_labels / chord_axis_labels) and each "
                       "segment stores key_scores[24] + key_committed (index into key_axis_labels) and "
                       "chord_scores[104] + chord_committed (index into chord_axis_labels). LOSSLESS — "
                       "the full list + full precision are preserved; NOT a truncation. Uniformity is "
                       "asserted at generation (a non-span-independent set is a STOP)."),
            "establishment": {
                "form": ("ratified two-half (dispatch cc_instruction_posterior_slice.md amendment "
                         "2026-07-26): (a) identity-arm mechanism vs probe_corpus_decode.json, "
                         "(b) selected-arm decode vs decode_parity_ref.json"),
                "a_identity_mechanism": est_a,
                "b_selected_decode": est_b,
            },
        },
        "pieces": pieces_out,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stems", nargs="*", default=None,
                    help="subset (dry-run: measure + validate, write nothing)")
    args = ap.parse_args()

    parity = json.loads((_HERE / "decode_parity_ref.json").read_text(encoding="utf-8"))
    sel_weights = parity["selected_weights"]
    weight_identity = parity.get("provenance", {}).get("selected_start", "")
    ident_weights = pd.identity_weights()

    all_pieces = sorted(pd.load_pieces()[0])
    stems = args.stems if args.stems else all_pieces
    dry = args.stems is not None

    print(f"decoding {len(stems)} piece(s) at SELECTED weights ('{weight_identity}')"
          + (" [dry-run subset]" if dry else "") + " ...", flush=True)
    t0 = time.perf_counter()
    sel_arm, prov = build_arm(sel_weights, stems)
    t_sel = time.perf_counter() - t0
    print(f"  selected arm decoded in {t_sel:.1f}s", flush=True)

    # axis-size measurement (candidate counts; both arms share span geometry — measured on selected)
    kl = [len(s["key_axis"]["keys"]) for a in sel_arm.values() for s in a["segments"]]
    cl = [len(s["chord_axis"]["classes"]) for a in sel_arm.values() for s in a["segments"]]
    nseg = sum(a["n_segments"] for a in sel_arm.values())
    if kl:
        print(f"  segments={nseg}  key_axis len min/mean/max={min(kl)}/{sum(kl)/len(kl):.1f}/{max(kl)}"
              f"  chord_axis len min/mean/max={min(cl)}/{sum(cl)/len(cl):.1f}/{max(cl)}", flush=True)

    print("decoding at IDENTITY weights (establishment half a; key axis only) ...", flush=True)
    t1 = time.perf_counter()
    ident_arm, _prov = build_arm(ident_weights, stems, need_chord=False)
    print(f"  identity arm decoded in {time.perf_counter()-t1:.1f}s", flush=True)

    print("establishment:", flush=True)
    ok_a, est_a = establish_a(ident_arm)
    ok_b, est_b = establish_b(sel_arm)

    if not (ok_a and ok_b):
        print("STOP: establishment failed — artifact NOT written.", file=sys.stderr)
        sys.exit(1)

    if dry:
        art = render_artifact(sel_arm, prov, est_a, est_b, weight_identity)
        blob = json.dumps(art)
        print(f"[dry-run] establishment PASSED; artifact would be {len(blob.encode('utf-8')):,} bytes "
              f"for {len(stems)} piece(s). Nothing written.", flush=True)
        return

    art = render_artifact(sel_arm, prov, est_a, est_b, weight_identity)
    ART_PATH.write_text(json.dumps(art) + "\n", encoding="utf-8", newline="\n")
    size = ART_PATH.stat().st_size
    print(f"wrote {ART_PATH}  ({size:,} bytes, {len(sel_arm)} pieces, {nseg} segments)")
    print(f"  establishment PASS: (a) {est_a['s5_unaffected']} unaffected + "
          f"{len(est_a['exceptions'])} §5 exception(s); (b) {est_b['pieces_compared']} segment-exact")


if __name__ == "__main__":
    main()

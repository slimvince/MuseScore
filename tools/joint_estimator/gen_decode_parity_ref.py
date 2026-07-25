#!/usr/bin/env python3
"""gen_decode_parity_ref.py — full-precision decode-parity REFERENCE for the C++ joint module.

READ-ONLY MEASUREMENT. No src/ change, no build, no gate. Reuses the pinned probe_decoder verbatim
(#6) to decode ALL covered pieces at BOTH committed weight arms — the identity (generative-baseline)
vector and the direct-metric SELECTED all-326 vector (weight_search.json, the best-training-R start
of the 'all' fit) — recording, per piece, the FULL-PRECISION total score + the segment state sequence
(i, j, tonic_pc, is_major, class_key, root_pc). The committed probe_corpus_decode.json rounds the score
to 3 decimals and is identity-only; this reference carries unrounded scores for both arms so the C++
decode parity can be checked to 1e-6 relative (the build dispatch's Task-2 bar) on both arms.

Config is probe_run's exactly: seg_cap 4, leftover option 2a ("freq"), table_set "all",
signature/declared-mode from the xml header. Output: decode_parity_ref.json.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd     # noqa: E402  the pinned decoder (reused verbatim)

SEG_CAP = 4
LEFTOVER = "freq"


def _git_head() -> str:
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def _selected_weights():
    """The direct-metric SELECTED all-326 vector: the best-training-R start of the 'all' fit
    (search_run.select_optimum == min R_train; ties by lower start index)."""
    ws = json.loads((_HERE / "weight_search.json").read_text(encoding="utf-8"))
    starts = ws["fits"]["all"]["starts"]
    best = min(starts, key=lambda s: (s["R_train"], s["start_index"]))
    return dict(best["weights"]), best["start_name"], best["R_train"]


def _decode_all(weights, label):
    pieces, prov = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER, table_set="all", weights=weights)
    adapter.mode_marginal("major")
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()
    out = {}
    t0 = time.perf_counter()
    for idx, stem in enumerate(sorted(pieces)):
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        r = pd.decode_piece(piece, adapter, vocab, cache, seg_cap=SEG_CAP, sig_fifths=sig, declared_mode=dm)
        out[stem] = {
            "total_score": r.total_score,           # FULL precision
            "n_segments": len(r.segments),
            "sig_fifths": sig, "declared_mode": dm,
            "segments": [[s["i"], s["j"], s["tonic_pc"], s["is_major"], s["class_key"],
                          (s["root_pc"] if s["root_pc"] is not None else None)] for s in r.segments],
        }
        if idx % 40 == 0:
            print(f"  [{label}] {idx+1}/{len(pieces)} {stem} {r.decode_seconds:.1f}s", flush=True)
    return out, prov, round(time.perf_counter() - t0, 1)


def main():
    ident = pd.identity_weights()
    sel, sel_name, sel_R = _selected_weights()
    print(f"selected all-326 start: {sel_name} R_train={sel_R}")
    id_decode, prov, id_secs = _decode_all(ident, "identity")
    sel_decode, _prov2, sel_secs = _decode_all(sel, "selected")
    art = {
        "provenance": {
            "generator": "tools/joint_estimator/gen_decode_parity_ref.py",
            "instrument_commit": _git_head(),
            "decoder": "tools/joint_estimator/probe_decoder.py (pinned; reused verbatim)",
            "note_events_git_hash": prov["corpus_git_hash"],
            "seg_cap": SEG_CAP, "leftover_rule": f"option 2a ({LEFTOVER})", "table_set": "all",
            "selected_start": sel_name, "selected_R_train": sel_R,
            "wall_seconds": {"identity": id_secs, "selected": sel_secs},
            "note": ("full-precision total scores + segment state sequences for BOTH weight arms; the "
                     "C++ joint decoder must reproduce these EXACTLY (segments) and to 1e-6 relative "
                     "(scores). Identity segments equal probe_corpus_decode.json; scores here are "
                     "unrounded."),
            "reproducibility_coupling": ("this reference's scores are Python builtin sum() sums (CPython "
                                         "3.12+ Neumaier-compensated). The C++ decoder mirrors that with "
                                         "jointprimitives.neumaierSum; the bit-identity RESTS on CPython "
                                         "keeping sum() compensated. A future Python changing sum() would "
                                         "surface as a decode-parity break — the correct loud signal; "
                                         "re-mirror neumaierSum and re-stamp this reference then."),
        },
        "selected_weights": sel,
        "identity": id_decode,
        "selected": sel_decode,
    }
    (_HERE / "decode_parity_ref.json").write_text(json.dumps(art), encoding="utf-8")
    print(f"wrote decode_parity_ref.json  ({len(id_decode)} pieces, identity {id_secs}s / selected {sel_secs}s)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""adoption_measure.py — the OI-178 robust-stop ADOPTION MEASUREMENT (measurement + record; NO adoption).

Dispatch: cc_instruction_adoption_measurement.md (Cowork 2026-07-20, at the user's ★R=A1 ruling).

★ MEASUREMENT ONLY. No src/ change, no build, no golden refresh, no tools/robust_stop/ re-baseline,
NO adoption commit. This produces the ADOPTION RECORD for the user's ratification. The pinned
instruments are IMPORT-ONLY; nothing here fits, tunes, or feeds any value back into the decoder or a
table (the firewall — the only decoder input is the FROZEN selected weight vector read from
weight_search.json; the only grading is the pinned a8/compare_rn chain).

WHAT IT DOES (Task 2 of the dispatch):
  A decodes the full covered corpus FROM ITS OWN FACT ADAPTER (the production path: adapter_facts.json,
  the direct-metric SELECTED all-326 weight vector, the ratified §5 tie-break, seg_cap 4, leftover 2a),
  is rendered to the a8-comparable region stream through the RETAINED measurement chain
  (probe_run.decode_to_regions / grade_regions -> a8.build_piece_grid vs dcml_parser.load_wir_regions),
  and is compared to the committed tools/robust_stop/ reference per preset. Every PASS condition of
  OI-178 (as amended ★R=A1) is evaluated and the whole record assembled.

REUSE (#6): decode = probe_decoder.decode_piece (pinned; the §5 rule is inside it); regions =
probe_run.decode_to_regions; grading = probe_run.grade_regions -> a8_rebaseline_measure.build_piece_grid;
per-preset run enumeration + class-(a)/(b) split + set-diff = the pinned a8_rebaseline_measure.py +
robust_stop_diff.py run over A's decode rendered as a candidate corpus (the ratified R10 sandwich);
pooled columns + piece-bootstrap = fit_run.pooled / _NUM / AXES; modulation = search_run
.decode_modulation_rate / gt_modulation_rate; the selected weights = the exact vector the C++
production path decodes with (decode_parity_ref.selected_weights).

ESTABLISHMENT (#19): the Python-from-adapter decode reproduces the C++ production decode-from-adapter
EXACTLY — proven by reproducing joint_endtoend_parity.json's divergent-vs-oracle stem set (cross-language
decoder parity is 326/326 on identical input, Task A; the adapter Piece is that identical input, so the
Python decode == the C++ decode, and the observable is the identical divergent set vs the note_events
oracle). The current-system per-piece grading reproduces the committed manifest ROOT column exactly.

Usage:
  python tools/joint_estimator/adoption_measure.py decode [--limit N]   # phase A: decode + candidate corpus
  python tools/joint_estimator/adoption_measure.py measure              # phase B: grade + diff + record
  python tools/joint_estimator/adoption_measure.py all                  # both
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

# The DECODE phase touches ONLY the pinned decoder and the region renderer — no grading module (the
# firewall: grading is confined to adoption_measure_b.py and feeds nothing back into the decode).
import probe_decoder as pd            # noqa: E402  the pinned decoder (the §5 rule lives inside)
import probe_run as pr                # noqa: E402  decode_to_regions (render only; grade_regions unused here)

ADAPTER_FACTS = _HERE / "adapter_facts.json"
DECODE_REF = _HERE / "decode_parity_ref.json"           # the note_events §5 oracle (both arms)
ENDTOEND = _HERE / "joint_endtoend_parity.json"         # the C++ from-adapter divergent set
WEIGHT_SEARCH = _HERE / "weight_search.json"

# scratch (session temp; never in the repo)
SCRATCH = Path(r"C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\eb2a4d53-5569-4c8f-88d0-457816f1e002\scratchpad")
CAND_CORPUS = SCRATCH / "adoption_cand_corpus"          # <preset>/<stem>.ours.json + corpus_manifest.json
CAND_A8 = SCRATCH / "adoption_cand_a8out"               # a8 --out-dir for A
DECODE_CACHE = _HERE / "adoption_decode.json"           # cached A decode (segments + regions + timing)

SEG_CAP = 4
LEFTOVER = "freq"
PRESETS = ["baroque", "jazz", "default"]
MANIFEST_NAME = "corpus_manifest.json"


def _git_head() -> str:
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def selected_weights():
    """The direct-metric SELECTED all-326 vector — the exact vector the C++ production path decodes
    with (best-training-R start of the 'all' fit; ties by lower start index). Cross-checked below
    against decode_parity_ref.selected_weights (the committed §5 oracle's arm)."""
    ws = json.loads(WEIGHT_SEARCH.read_text(encoding="utf-8"))
    starts = ws["fits"]["all"]["starts"]
    best = min(starts, key=lambda s: (s["R_train"], s["start_index"]))
    return dict(best["weights"]), best["start_name"], best["R_train"]


def load_adapter_pieces():
    """Build pd.Piece objects from the C++ FACT ADAPTER's own extraction (adapter_facts.json) — the
    production input. sig_fifths/declared_mode are the adapter's OWN header (the production path reads
    them from the engraving model, not from music21)."""
    adp = json.loads(ADAPTER_FACTS.read_text(encoding="utf-8"))
    prov = adp["provenance"]
    pieces, header = {}, {}
    for stem, p in adp["pieces"].items():
        pc = pd.Piece(stem=stem, events=p["events"], notes=p["notes"],
                      n_quarter=p["n_quarter"], meter=tuple(p["meter"]) if p["meter"] else None)
        pc.prepare()
        pieces[stem] = pc
        header[stem] = (p.get("sig_fifths"), p.get("declared_mode") or "")
    return pieces, header, prov


def region_to_dict(r):
    """cmp.Region -> the .ours.json region schema compare_analyses._load_region reads (camelCase)."""
    return {
        "measureNumber": r.measure_number, "beat": r.beat,
        "startTick": r.start_tick, "endTick": r.end_tick, "duration": r.duration,
        "rootPitchClass": r.root_pc, "quality": r.quality, "chordSymbol": r.chord_symbol,
        "romanNumeral": r.roman_numeral, "key": r.key, "keyConfidence": r.key_confidence,
        "diatonicToKey": r.diatonic_to_key, "alternatives": r.alternatives,
        "bassPitchClass": r.bass_pc, "bassIsRoot": r.bass_is_root,
        "noteCount": r.note_count, "pitchClassSet": r.pitch_class_set,
    }


def phase_decode(limit=None, verbose=True):
    """Decode A from the adapter at the selected weights, establish vs the C++ production decode, write
    the candidate corpus (3 preset dirs, identical — A is preset-independent) + the decode cache."""
    t0 = time.perf_counter()
    pieces, header, prov = load_adapter_pieces()
    sel, sel_name, sel_R = selected_weights()
    dref = json.loads(DECODE_REF.read_text(encoding="utf-8"))
    assert dict(dref["selected_weights"]) == sel, "selected weights != decode_parity_ref oracle arm"
    e2e = json.loads(ENDTOEND.read_text(encoding="utf-8"))
    expected_divergent = set(e2e["arms"]["selected"]["divergent"])

    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER, table_set="all", weights=sel)
    adapter.mode_marginal("major")
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()

    stems = sorted(pieces)
    if limit:
        stems = stems[:limit]
    decode = {}
    regions_json = {}
    timings = []
    divergent = []                      # my Python-from-adapter decode vs the note_events oracle
    oracle_sel = dref["selected"]
    for idx, stem in enumerate(stems):
        piece = pieces[stem]
        sig, dm = header[stem]
        r = pd.decode_piece(piece, adapter, vocab, cache, seg_cap=SEG_CAP,
                            sig_fifths=sig, declared_mode=dm)
        timings.append((stem, r.decode_seconds, r.n_events))
        regs = pr.decode_to_regions(piece, r, vocab, cache)
        regions_json[stem] = [region_to_dict(x) for x in regs]
        decode[stem] = {"n_events": r.n_events, "n_segments": len(r.segments),
                        "total_score": r.total_score, "decode_seconds": r.decode_seconds,
                        "sig_fifths": sig, "declared_mode": dm, "segments": r.segments}
        # establishment observable: divergence of THIS (adapter) decode vs the note_events oracle
        if stem in oracle_sel:
            mine = [(s["i"], s["j"], s["tonic_pc"], s["is_major"], s["class_key"]) for s in r.segments]
            theirs = [(x[0], x[1], x[2], x[3], x[4]) for x in oracle_sel[stem]["segments"]]
            if mine != theirs:
                divergent.append(stem)
        if verbose and idx % 25 == 0:
            print(f"  [decode {idx+1}/{len(stems)}] {stem} {r.n_events}ev {r.decode_seconds:.1f}s",
                  flush=True)

    divergent = sorted(divergent)
    established = (not limit) and (set(divergent) == expected_divergent)
    est = {"reproduces_cpp_from_adapter": bool(established),
           "my_divergent_vs_note_events_oracle": divergent,
           "cpp_from_adapter_divergent_vs_oracle": sorted(expected_divergent),
           "note": ("cross-language decoder parity is 326/326 on identical input (Task A); the adapter "
                    "Piece is that identical input, so the Python-from-adapter decode == the C++ "
                    "production decode-from-adapter. The observable is the IDENTICAL divergent set vs "
                    "the note_events oracle (decode_parity_ref selected arm).")}
    if not limit and not established:
        print(f"  !! ESTABLISHMENT MISMATCH: mine={divergent} vs cpp={sorted(expected_divergent)}",
              flush=True)

    # ── write the candidate corpus (3 preset dirs, identical; A is preset-independent) ──
    for preset in PRESETS:
        d = CAND_CORPUS / preset
        d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.ours.json"):
            f.unlink()
        scores = {}
        for stem in stems:
            body = {"source": "joint_estimator_A_from_adapter", "preset": preset,
                    "regions": regions_json[stem]}
            b = json.dumps(body, indent=1).encode("utf-8")
            (d / f"{stem}.ours.json").write_bytes(b)
            scores[stem] = {"status": "OK", "sha256": hashlib.sha256(b).hexdigest()}
        manifest = {"preset": preset, "expected_count": len(stems), "ours_count": len(stems),
                    "complete": True, "scores": scores,
                    "note": ("A's decode-from-adapter rendered as .ours.json for the pinned a8/robust_"
                             "stop_diff sandwich; identical across presets (A is preset-independent at "
                             "the inference layer). ADOPTION-MEASUREMENT scratch, not a batch_analyze run.")}
        (d / MANIFEST_NAME).write_text(json.dumps(manifest, indent=1), encoding="utf-8")

    out = {
        "provenance": {
            "generator": "tools/joint_estimator/adoption_measure.py",
            "instrument_commit": _git_head(),
            "corpus_git_hash": prov.get("corpus_git_hash"),
            "reader": "adapter_facts.json (composing/analysis/joint/jointfactadapter — the production path)",
            "selected_start": sel_name, "selected_R_train": sel_R,
            "seg_cap": SEG_CAP, "leftover_rule": f"option 2a ({LEFTOVER})", "table_set": "all",
            "tie_break": "the ratified §5 total order (inside probe_decoder.decode_piece)",
            "n_pieces": len(stems),
        },
        "selected_weights": sel,
        "establishment_vs_cpp_production": est,
        "timing": {"decode_mean_s": round(sum(t for _s, t, _e in timings) / len(timings), 3),
                   "decode_max_s": round(max(t for _s, t, _e in timings), 3),
                   "decode_total_s": round(sum(t for _s, t, _e in timings), 1),
                   "slowest": sorted([(s, round(t, 2), e) for s, t, e in timings],
                                     key=lambda x: -x[1])[:8]},
        "decode": decode,
    }
    DECODE_CACHE.write_text(json.dumps(out), encoding="utf-8")
    print(f"\n[decode] {len(stems)} pieces in {time.perf_counter()-t0:.0f}s wall; "
          f"establishment reproduces C++ production decode: {established} "
          f"(divergent {divergent})", flush=True)
    print(f"[decode] wrote {DECODE_CACHE.name} + candidate corpus {CAND_CORPUS}", flush=True)
    return out


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    if mode in ("decode", "all"):
        phase_decode(limit=limit)
    if mode in ("measure", "all"):
        import adoption_measure_b  # noqa: E402  the measure/record phase (kept in its own module)
        adoption_measure_b.main()

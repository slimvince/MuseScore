#!/usr/bin/env python3
"""probe_run.py — the probe decoder's orchestrator (Task 1 decode + Task 3 corpus decode & grading;
Task 2 establishment via probe_desksim). READ-ONLY MEASUREMENT. No src/, no build, no golden, no
re-baseline. The GRADING import (compare_rn / compare_analyses / a8_rebaseline_measure) is confined
to the Task-3 measurement step and feeds NO value back into the decoder (the firewall).

Usage:
  python tools/joint_estimator/probe_decoder.py parity          # Task 2 establishment only
  python tools/joint_estimator/probe_decoder.py corpus          # Task 3 decode + grade
  python tools/joint_estimator/probe_decoder.py all              # everything (default), writes artifacts
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd            # noqa: E402
import normalize as norm             # noqa: E402
import gen_note_tables as gnt        # noqa: E402
# grading chain (READ-ONLY; Task 3 only)
import compare_analyses as cmp       # noqa: E402
import compare_rn as crn             # noqa: E402
import dcml_parser as dcml           # noqa: E402
import a8_rebaseline_measure as a8   # noqa: E402

SEG_CAP = 4
LEFTOVER = "freq"                    # the ratified §5 rule (option 2a)
WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")

_MAJOR_COLOR = {"Maj", "Dom7", "Maj7", "Aug", "Aug7", "AugMaj7", "AugSixth", "Neapolitan"}
_QUAL_STR = {"Maj": "Major", "Dom7": "Major", "Maj7": "Major", "Min": "Minor", "Min7": "Minor",
             "MinMaj7": "Minor", "Dim": "Diminished", "Dim7": "Diminished",
             "HalfDim": "HalfDiminished", "HalfDim7": "HalfDiminished",
             "Aug": "Augmented", "Aug7": "Augmented", "AugMaj7": "Augmented",
             "AugSixth": "Major", "Neapolitan": "Major"}
_FIG_TRIAD = {"root": "", "third": "6", "fifth": "6/4"}
_FIG_SEVENTH = {"root": "7", "third": "6/5", "fifth": "4/3", "seventh": "4/2"}


def _git_head():
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def render_rn(cls: norm.LabelClass, bass_role, family):
    """A When-in-Rome-style Roman numeral from the (inversion-free) class + the derived bass role."""
    d = cls.degree_base if cls.quality in _MAJOR_COLOR else cls.degree_base.lower()
    sig = ""
    if cls.quality in ("Dim", "Dim7"):
        sig = "o"
    elif cls.quality in ("HalfDim", "HalfDim7"):
        sig = "ø"
    elif cls.quality in ("Aug", "Aug7", "AugMaj7"):
        sig = "+"
    fig = (_FIG_SEVENTH if family == "seventh" else _FIG_TRIAD).get(bass_role, "")
    tgt = ("/" + cls.target) if cls.target else ""
    return f"{d}{sig}{fig}{tgt}"


def _pcs_bitmask(pcs):
    b = 0
    for pc in pcs:
        b |= (1 << pc)
    return b


def decode_to_regions(piece: pd.Piece, result: pd.DecodeResult, vocab, cache):
    """Convert a DecodeResult into compare_analyses.Region objects (the .ours.json region model) so
    the pinned a8/compare_rn grading chain scores it exactly like a committed corpus."""
    regions = []
    for s in result.segments:
        cls = vocab.classes[s["class_key"]]
        i, j = s["i"], s["j"]
        tonic, is_major = s["tonic_pc"], s["is_major"]
        mem, fac, root = cache.get(cls, tonic, is_major)
        family = "seventh" if (fac and len(fac) == 4) else "triad"
        fac_pc = {pc: role for role, pc in (fac or [])}
        bass = piece.ev_bass[i]
        bass_role = fac_pc.get(bass) if bass is not None else None
        onset_pcs = set()
        for e in range(i, j):
            onset_pcs |= piece.ev_onset_pcs[e]
        rn = render_rn(cls, bass_role, family)
        ev0 = piece.events[i]
        regions.append(cmp.Region(
            measure_number=ev0[pd.EV_MEAS], beat=float(ev0[pd.EV_BEAT]),
            start_tick=s["start_tick"], end_tick=s["end_tick"],
            duration=float(s["end_tick"] - s["start_tick"]) / 480.0,   # QUARTERS (ticks/quarter=480)
            # ^ compare_analyses._infer_ticks_per_beat divides (end-start ticks)/duration to recover
            #   ticks-per-beat; duration MUST be in quarter-beats or the GT tick anchoring collapses.
            root_pc=(root if root is not None else -1),
            quality=_QUAL_STR.get(cls.quality, "Unknown"),
            chord_symbol=f"{pd._PC_KEYNAME[root % 12]}{cls.quality}" if root is not None else "",
            roman_numeral=rn, key=pd._key_string(tonic, is_major),
            key_confidence=1.0, diatonic_to_key=None,
            bass_pc=(bass if bass is not None else None),
            bass_is_root=(bass_role == "root"),
            note_count=len(onset_pcs), pitch_class_set=_pcs_bitmask(onset_pcs)))
    return regions


def grade_regions(stem, ours_regions):
    """Grade one decoded piece on the robust unit via the pinned a8 build_piece_grid (root / RN / key
    home+local, duration-weighted). Returns per-respect (agree, disagree) durations + the RN buckets."""
    wir_regions = dcml.load_wir_regions(WIR_DIR, stem)     # the OI-142-corrected substrate (shared)
    if not wir_regions or not ours_regions:
        return None
    pg = a8.build_piece_grid(stem, ours_regions, wir_regions, [])   # m21 leg unused for the columns
    agg = Counter()
    for c in pg.cells:
        w = c["w"]
        agg["root_agree" if c["root_agree"] else "root_dis"] += w
        agg["rn_agree" if c["rn_agree"] else "rn_dis"] += w
        agg["key_" + c["key_verdict"]] += w
        agg["keyl_" + c["key_verdict_local"]] += w
        agg["bucket_" + c["bucket"]] += w
    agg["scored"] = pg.scored_dur
    agg["unscored"] = pg.unscored_dur
    return agg


def _pct(a, b):
    return round(100.0 * a / b, 2) if b else None


# The committed probe baseline (e3d17c325d; cadence-free, pre-chromatic-vocabulary decode) — the
# side-by-side reference the dispatch asks for. Task 3 reports the axes BESIDE these.
PROBE_BASELINE = {"root_agree_pct": 72.97, "rn_agree_pct": 59.50,
                  "key_home_agree_pct": 53.67, "key_local_agree_pct": 74.43}


def _delta(new, base):
    if new is None or base is None:
        return None
    return round(new - base, 2)


def _prediction_verdict(cols, base):
    """The dispatch's ±1-point prediction: every axis moves < ±1pp. Returns the per-axis |delta| and a
    boolean; a larger movement on any axis is a prominently-reported surprise (the dispatch's wording)."""
    axes = ("root_agree_pct", "rn_agree_pct", "key_home_agree_pct", "key_local_agree_pct")
    deltas = {a: _delta(cols.get(a), base.get(a)) for a in axes}
    over = {a: d for a, d in deltas.items() if d is not None and abs(d) >= 1.0}
    return {"deltas_pp": deltas, "prediction": "every axis moves < +/-1.0pp",
            "holds": len(over) == 0, "axes_over_1pp": over}


def run_corpus(write=True, verbose=True, stems=None):
    t_all = time.perf_counter()
    pieces, prov = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER)
    adapter.mode_marginal("major")       # warm the class marginal (one-time)
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()

    stem_list = stems or sorted(pieces)
    decode_records = {}
    timings = []
    grand = Counter()
    per_piece_grade = {}
    n_no_wir = 0
    cad_totals = Counter()                          # WEIGHTLESS cadence-feature fires, corpus-wide
    chromatic_decodes = {}                          # stem -> [ (start_tick, class_key, root_pc) ] (Task 3)
    for idx, stem in enumerate(stem_list):
        piece = pieces[stem]
        sig, dm = pd.piece_header(stem)
        r = pd.decode_piece(piece, adapter, vocab, cache, seg_cap=SEG_CAP,
                            sig_fifths=sig, declared_mode=dm)
        timings.append((stem, r.decode_seconds, len(piece.events)))
        ours_regions = decode_to_regions(piece, r, vocab, cache)
        if r.cadence_fires:
            cad_totals.update(r.cadence_fires)
        chrom = [(s["start_tick"], s["class_key"], s["root_pc"]) for s in r.segments
                 if s["quality"] in ("AugSixth", "Neapolitan")]
        if chrom:
            chromatic_decodes[stem] = chrom
        decode_records[stem] = {
            "n_events": r.n_events, "n_segments": len(r.segments),
            "total_score": round(r.total_score, 3), "decode_seconds": round(r.decode_seconds, 4),
            "sig_fifths": sig, "declared_mode": dm,
            "cadence_fires": r.cadence_fires,
            "segments": r.segments, "posterior": r.posterior,
        }
        g = grade_regions(stem, ours_regions)
        if g is None:
            n_no_wir += 1
        else:
            per_piece_grade[stem] = g
            grand.update(g)
        if verbose and (idx % 40 == 0):
            print(f"  [{idx+1}/{len(stem_list)}] {stem} {len(piece.events)}ev "
                  f"{r.decode_seconds:.1f}s", flush=True)

    # aggregate columns
    cols = {
        "root_agree_pct": _pct(grand["root_agree"], grand["root_agree"] + grand["root_dis"]),
        "rn_agree_pct": _pct(grand["rn_agree"], grand["rn_agree"] + grand["rn_dis"]),
        "key_home_agree_pct": _pct(grand["key_agree"], grand["key_agree"] + grand["key_disagree"]),
        "key_local_agree_pct": _pct(grand["keyl_agree"], grand["keyl_agree"] + grand["keyl_disagree"]),
        "key_home_abstain_pct": _pct(grand["key_keyfail"],
                                     grand["key_agree"] + grand["key_disagree"] + grand["key_keyfail"]),
        "key_local_abstain_pct": _pct(grand["keyl_keyfail"],
                                      grand["keyl_agree"] + grand["keyl_disagree"] + grand["keyl_keyfail"]),
    }
    tsec = [t for _s, t, _e in timings]
    timing_summary = {"mean_s": round(sum(tsec) / len(tsec), 3), "max_s": round(max(tsec), 3),
                      "total_s": round(sum(tsec), 1),
                      "slowest": sorted([(s, round(t, 2), e) for s, t, e in timings],
                                        key=lambda x: -x[1])[:8]}

    # win/loss vs the Default baseline on the key-LOCAL axis (per piece)
    wl = _win_loss(per_piece_grade)

    result = {
        "provenance": {
            "generator": "tools/joint_estimator/probe_run.py",
            "decoder": "tools/joint_estimator/probe_decoder.py (identity weights; ratified factorization)",
            "instrument_commit": _git_head(),
            "note_events_git_hash": prov["corpus_git_hash"],
            "tables_git_hash": adapter.corpus_git_hash,
            "leftover_rule": f"option 2{'a' if LEFTOVER=='freq' else 'b'} ({LEFTOVER})",
            "seg_cap_events": SEG_CAP, "key_prune_topk": pd.KEY_PRUNE_TOPK,
            "cadence": ("WIRED, WEIGHTLESS (algorithm-completion step 1): the ratified cadence-evidence "
                        "features compute at every committed boundary and are LOGGED (cadence_feature_fires), "
                        "but every weight is 0 so they move no score — the vocabulary change is isolated."),
            "fermata": ("EXTRACTED (note_events fermata field, step 1); the cadence-location feature is "
                        "wired weightless; the counted fermata-boundary cells are in fermata_boundary_addendum.json."),
            "chromatic_vocab": ("Task 3: AugSixth (Italian; the 2 corpus tokens) + Neapolitan added to the "
                                "decode vocabulary via chromatic_root_pc; see chromatic_decodes."),
            "grading": "a8_rebaseline_measure.build_piece_grid (pinned, read-only) vs "
                       "dcml_parser.load_wir_regions (OI-142-corrected)",
            "coverage": len(per_piece_grade), "no_wir": n_no_wir,
        },
        "columns": cols,
        "probe_baseline_columns": PROBE_BASELINE,
        "axis_delta_vs_probe_baseline": {
            "root_agree_pct": _delta(cols["root_agree_pct"], PROBE_BASELINE["root_agree_pct"]),
            "rn_agree_pct": _delta(cols["rn_agree_pct"], PROBE_BASELINE["rn_agree_pct"]),
            "key_home_agree_pct": _delta(cols["key_home_agree_pct"], PROBE_BASELINE["key_home_agree_pct"]),
            "key_local_agree_pct": _delta(cols["key_local_agree_pct"], PROBE_BASELINE["key_local_agree_pct"]),
        },
        "prediction_verdict": _prediction_verdict(cols, PROBE_BASELINE),
        "cadence_feature_fires": dict(cad_totals),
        "chromatic_decodes": {
            "n_segments": sum(len(v) for v in chromatic_decodes.values()),
            "n_pieces": len(chromatic_decodes),
            "by_piece": chromatic_decodes,
        },
        "duration_totals": {k: grand[k] for k in sorted(grand)},
        "timing": timing_summary,
        "win_loss_key_local": wl,
    }
    if write:
        (_HERE / "probe_grading.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
        (_HERE / "probe_corpus_decode.json").write_text(
            json.dumps({"provenance": result["provenance"], "pieces": decode_records}, indent=1),
            encoding="utf-8")
    if verbose:
        _print_corpus_report(cols, timing_summary, wl, len(per_piece_grade), n_no_wir,
                             time.perf_counter() - t_all, result)
    return result


# the current committed Default baselines (CLAUDE.md block (A), OI-168 re-baseline) — comparison only
BASELINES = {
    "key_local": {"Baroque": 65.99, "Jazz": 62.98, "Default": 65.71},
    "key_home": {"Baroque": 71.42, "Jazz": 67.83, "Default": 70.65},
    "root": {"Baroque": 66.04, "Jazz": 64.98, "Default": 65.93},
    "rn": {"Baroque": 46.33, "Jazz": 44.10, "Default": 46.23},
}
PREDICTIONS = {
    "key_local": "70-80% (UP; the load-bearing prediction)",
    "key_home": "72-82% (UP)",
    "root": "55-70% (may sit BELOW current)",
    "rn": "40-55%",
}


class _StubResult:
    def __init__(self, segments):
        self.segments = segments


# a fixed, size-and-difficulty-mixed sample for the §5 reserve prune-loss measurement (declared).
PRUNE_LOSS_SAMPLE = ["bwv269", "bwv352", "bwv10.7", "bwv110.7", "bwv254", "bwv101.7",
                     "bwv266", "bwv40.3", "bwv277", "bwv88.7", "bwv293", "bwv320"]


def measure_prune_loss(write=True, verbose=True):
    """The DECLARED pruning's established loss (§5): decode the fixed sample at the TIGHT prune
    (the headline: seg_cap 4, key-top-K 6) and a LOOSER one (seg_cap 6, key-top-K 12), grade both
    on the robust unit, report the agreement gain from loosening. A small gain ⟹ the tight-prune
    headline is a conservative lower bound; the exact decode would score at most that much higher."""
    pieces, _ = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER)
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()

    def grade_at(seg_cap, topk):
        old = pd.KEY_PRUNE_TOPK
        pd.KEY_PRUNE_TOPK = topk
        g = Counter()
        t0 = time.perf_counter()
        for stem in PRUNE_LOSS_SAMPLE:
            p = pieces[stem]
            sig, dm = pd.piece_header(stem)
            r = pd.decode_piece(p, adapter, vocab, cache, seg_cap=seg_cap, sig_fifths=sig, declared_mode=dm)
            reg = decode_to_regions(p, r, vocab, cache)
            wir = dcml.load_wir_regions(WIR_DIR, stem)
            pg = a8.build_piece_grid(stem, reg, wir, [])
            for c in pg.cells:
                w = c["w"]
                g["ra" if c["root_agree"] else "rd"] += w
                if c["key_verdict_local"] == "agree":
                    g["la"] += w
                elif c["key_verdict_local"] == "disagree":
                    g["ld"] += w
        pd.KEY_PRUNE_TOPK = old
        return g, time.perf_counter() - t0

    tight, tt = grade_at(4, 6)
    loose, lt = grade_at(6, 12)

    def cols(g):
        return {"root_pct": round(100 * g["ra"] / (g["ra"] + g["rd"]), 2),
                "key_local_pct": round(100 * g["la"] / (g["la"] + g["ld"]), 2)}
    tc, lc = cols(tight), cols(loose)
    out = {
        "provenance": {"generator": "tools/joint_estimator/probe_run.py:measure_prune_loss",
                       "instrument_commit": _git_head(), "sample": PRUNE_LOSS_SAMPLE,
                       "note": "the DECLARED candidate prune's established loss (ratified §5 reserve): "
                       "root-present + member-overlap + few-NCT + key-top-K + seg-cap + inversion-free "
                       "state collapse. The headline uses TIGHT; LOOSE widens seg_cap and key-top-K."},
        "tight": {"seg_cap": 4, "key_top_k": 6, **tc, "seconds": round(tt, 1)},
        "loose": {"seg_cap": 6, "key_top_k": 12, **lc, "seconds": round(lt, 1)},
        "loss_pp": {"root": round(lc["root_pct"] - tc["root_pct"], 2),
                    "key_local": round(lc["key_local_pct"] - tc["key_local_pct"], 2)},
        "compute_ratio": round(lt / tt, 1) if tt else None,
    }
    if write:
        (_HERE / "probe_prune_loss.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    if verbose:
        print(f"prune loss (12-piece sample): root {out['loss_pp']['root']:+.2f}pp  "
              f"key_local {out['loss_pp']['key_local']:+.2f}pp  at {out['compute_ratio']}x compute")
    return out


def re_grade_from_artifact(write=True, verbose=True):
    """Re-grade from the committed decode artifact WITHOUT re-decoding (reuses the valid segments;
    used after a region-emission fix so the expensive Viterbi is not repeated). Recomputes every
    grading column + the win/loss surface and rewrites probe_grading.json."""
    pieces, prov = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER)
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()
    dec = json.loads((_HERE / "probe_corpus_decode.json").read_text(encoding="utf-8"))
    grand = Counter()
    per_piece_grade = {}
    n_no_wir = 0
    tsec = []
    events_of = {}
    for stem, rec in dec["pieces"].items():
        piece = pieces[stem]
        tsec.append(rec.get("decode_seconds", 0.0))
        events_of[stem] = rec.get("n_events", len(piece.events))
        ours_regions = decode_to_regions(piece, _StubResult(rec["segments"]), vocab, cache)
        g = grade_regions(stem, ours_regions)
        if g is None:
            n_no_wir += 1
        else:
            per_piece_grade[stem] = g
            grand.update(g)
    cols = {
        "root_agree_pct": _pct(grand["root_agree"], grand["root_agree"] + grand["root_dis"]),
        "rn_agree_pct": _pct(grand["rn_agree"], grand["rn_agree"] + grand["rn_dis"]),
        "key_home_agree_pct": _pct(grand["key_agree"], grand["key_agree"] + grand["key_disagree"]),
        "key_local_agree_pct": _pct(grand["keyl_agree"], grand["keyl_agree"] + grand["keyl_disagree"]),
        "key_home_abstain_pct": _pct(grand["key_keyfail"],
                                     grand["key_agree"] + grand["key_disagree"] + grand["key_keyfail"]),
        "key_local_abstain_pct": _pct(grand["keyl_keyfail"],
                                      grand["keyl_agree"] + grand["keyl_disagree"] + grand["keyl_keyfail"]),
    }
    timing_summary = {"mean_s": round(sum(tsec) / len(tsec), 3), "max_s": round(max(tsec), 3),
                      "total_s": round(sum(tsec), 1),
                      "slowest": sorted([(s, round(dec["pieces"][s]["decode_seconds"], 2),
                                          events_of[s]) for s in dec["pieces"]],
                                        key=lambda x: -x[1])[:8]}
    wl = _win_loss(per_piece_grade)
    prov_old = dec.get("provenance", {})
    result = {
        "provenance": {**prov_old, "regraded": "from probe_corpus_decode.json (region-emission fix)",
                       "instrument_commit": _git_head(), "coverage": len(per_piece_grade),
                       "no_wir": n_no_wir},
        "columns": cols, "duration_totals": {k: grand[k] for k in sorted(grand)},
        "timing": timing_summary, "win_loss_key_local": wl,
    }
    if write:
        (_HERE / "probe_grading.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
    if verbose:
        _print_corpus_report(cols, timing_summary, wl, len(per_piece_grade), n_no_wir, 0.0)
    return result


def add_vs_default(write=True, verbose=True):
    """Per-piece key-LOCAL and root agreement of the probe decode vs the committed Default corpus
    (`tools/corpus/default/*.ours.json`), graded through the same pinned chain — the dispatch's
    'ten largest key-axis wins and losses versus the Default baseline'. Adds `win_loss_vs_default`
    to probe_grading.json. Read-only (grades the committed Default corpus; changes no value)."""
    pieces, _ = pd.load_pieces()
    adapter = pd.FittedAdapter(leftover_mode=LEFTOVER)
    vocab = pd.Vocabulary(adapter.tables)
    cache = pd.ChordCache()
    dec = json.loads((_HERE / "probe_corpus_decode.json").read_text(encoding="utf-8"))
    def_dir = _ROOT / "tools" / "corpus" / "default"

    def _kl(pg):
        a = sum(c["w"] for c in pg.cells if c["key_verdict_local"] == "agree")
        d = sum(c["w"] for c in pg.cells if c["key_verdict_local"] == "disagree")
        return (100.0 * a / (a + d)) if (a + d) else None

    def _rt(pg):
        a = sum(c["w"] for c in pg.cells if c["root_agree"])
        t = sum(c["w"] for c in pg.cells)
        return (100.0 * a / t) if t else None

    rows = []
    for stem, rec in dec["pieces"].items():
        dp = def_dir / f"{stem}.ours.json"
        if not dp.exists():
            continue
        wir = dcml.load_wir_regions(WIR_DIR, stem)
        myreg = decode_to_regions(pieces[stem], _StubResult(rec["segments"]), vocab, cache)
        _, defreg = cmp.load_analysis(dp)
        mypg = a8.build_piece_grid(stem, myreg, wir, [])
        defpg = a8.build_piece_grid(stem, defreg, wir, [])
        mkl, dkl = _kl(mypg), _kl(defpg)
        mrt, drt = _rt(mypg), _rt(defpg)
        if None in (mkl, dkl, mrt, drt):
            continue
        rows.append({"stem": stem, "kl_delta": round(mkl - dkl, 1), "my_kl": round(mkl, 1),
                     "def_kl": round(dkl, 1), "root_delta": round(mrt - drt, 1),
                     "my_root": round(mrt, 1), "def_root": round(drt, 1)})
    rows.sort(key=lambda r: r["kl_delta"])
    n = len(rows)
    summary = {
        "n_pieces": n,
        "mean_key_local_delta_pp": round(sum(r["kl_delta"] for r in rows) / n, 2),
        "mean_root_delta_pp": round(sum(r["root_delta"] for r in rows) / n, 2),
        "pieces_key_local_better": sum(1 for r in rows if r["kl_delta"] > 0),
        "pieces_key_local_worse": sum(1 for r in rows if r["kl_delta"] < 0),
        "largest_key_local_losses": rows[:10],
        "largest_key_local_wins": rows[-10:][::-1],
    }
    if write:
        g = json.loads((_HERE / "probe_grading.json").read_text(encoding="utf-8"))
        g["win_loss_vs_default"] = summary
        (_HERE / "probe_grading.json").write_text(json.dumps(g, indent=1), encoding="utf-8")
    if verbose:
        print(f"vs Default: mean key_local {summary['mean_key_local_delta_pp']:+.2f}pp  "
              f"root {summary['mean_root_delta_pp']:+.2f}pp  "
              f"(better/worse {summary['pieces_key_local_better']}/{summary['pieces_key_local_worse']})")
    return summary


def _win_loss(per_piece_grade):
    """Per-piece key-LOCAL agreement fraction (this probe's own; there is no per-piece Default column
    on disk — the ten largest agreement pieces and the ten weakest are reported as the win/loss
    surface for the named-piece diagnosis)."""
    rows = []
    for stem, g in per_piece_grade.items():
        den = g["keyl_agree"] + g["keyl_disagree"]
        if den == 0:
            continue
        rows.append({"stem": stem, "key_local_agree_pct": round(100.0 * g["keyl_agree"] / den, 1),
                     "root_agree_pct": round(100.0 * g["root_agree"] /
                                             max(1, g["root_agree"] + g["root_dis"]), 1),
                     "dur": den})
    rows.sort(key=lambda r: r["key_local_agree_pct"])
    return {"weakest_key_local": rows[:10], "strongest_key_local": rows[-10:][::-1]}


def _print_corpus_report(cols, timing, wl, cov, no_wir, wall, result=None):
    print("\n" + "=" * 78)
    print("TASK 3 — probe decode + grading (326 covered; identity weights; leftover 2a)")
    print("      (cadence WIRED-WEIGHTLESS; chromatic vocab completed)")
    print("=" * 78)
    print(f"coverage: {cov} graded pieces ({no_wir} without WiR); wall {wall:.0f}s "
          f"(decode mean {timing['mean_s']}s / max {timing['max_s']}s)")
    print(f"\n{'axis':16s} {'PROBE base':11s} {'MEASURED':11s} {'delta':8s} {'Default(B/J/D)'}")
    print("-" * 78)
    for axis, colkey, bkey in (("key vs LOCAL", "key_local_agree_pct", "key_local"),
                               ("key vs HOME", "key_home_agree_pct", "key_home"),
                               ("chord root", "root_agree_pct", "root"),
                               ("Roman numeral", "rn_agree_pct", "rn")):
        b = BASELINES[bkey]
        pb = PROBE_BASELINE[colkey]
        d = _delta(cols[colkey], pb)
        bl = f"{b['Baroque']}/{b['Jazz']}/{b['Default']}"
        print(f"{axis:16s} {pb!s:11s} {cols[colkey]!s:11s} {d:+8.2f} {bl}")
    if result:
        pv = result["prediction_verdict"]
        print(f"\nprediction (<+/-1.0pp on every axis): {'HOLDS' if pv['holds'] else 'SURPRISE — '+str(pv['axes_over_1pp'])}")
        cf = result["cadence_feature_fires"]
        print(f"cadence fires (WEIGHTLESS, over {cf.get('boundaries',0)} committed boundaries): "
              f"LT={cf.get('leading_tone',0)} tritone={cf.get('tritone_pair',0)} "
              f"domBass={cf.get('dominant_tonic_bass',0)} fermata={cf.get('fermata_location',0)} "
              f"any={cf.get('any_fire',0)}")
        ch = result["chromatic_decodes"]
        print(f"chromatic classes decoded: {ch['n_segments']} segments on {ch['n_pieces']} pieces "
              f"{list(ch['by_piece'].keys())[:8]}")
    print(f"\nkey abstain: home {cols['key_home_abstain_pct']}%  local {cols['key_local_abstain_pct']}% "
          f"(the probe commits its best path everywhere — should be ~0)")
    print("\nslowest pieces:", timing["slowest"][:5])


def run_parity_artifact(write=True):
    import probe_desksim as ds
    rows, nfail = ds.run_parity(verbose=True)
    fire_rows, fire_stop = ds.run_cadence_fire_establishment(verbose=True)
    if fire_stop:
        raise SystemExit("STOP (Task 2): a cadence feature does not fire where the desk-sim applied its "
                         "credit, and the mismatch is NOT the documented approach-window under-spec — "
                         "the feature implementation is wrong. " + json.dumps(fire_rows))
    fitted = ds.run_fitted_probe(verbose=True)
    art = {"provenance": {"generator": "tools/joint_estimator/probe_desksim.py",
                          "instrument_commit": _git_head(),
                          "establishment": "structural parity (all non-cadence factors) vs the "
                          "desk-simulation hand arithmetic; the cadence MECHANISM-FIRES table (Task 2) "
                          "checks the WEIGHTLESS features fire where the desk-sim applied its credits; "
                          "fitted-table recomputation under both leftover variants",
                          "cadence_window_note": ("the tritone feature uses a SINGLE-event approach "
                          "(committed probe convention); the desk-sim S2 credit assumed a multi-beat "
                          "window (Bigo 'last four beats', theory §F4). The divergence is confined to "
                          "S2's tritone, is verdict-irrelevant, and is DECLARED to Cowork as the "
                          "fit-time window design question — NOT built around here.")},
           "structural_parity": rows, "structural_fail": nfail,
           "cadence_fire_establishment": fire_rows, "cadence_fire_stop": fire_stop,
           "fitted_recomputation": fitted}
    if write:
        (_HERE / "probe_parity_report.json").write_text(json.dumps(art, indent=1), encoding="utf-8")
    return art


def write_summaries():
    """Emit the two human-readable committed summary artifacts from the JSON (all figures generated,
    #17f — nothing hand-transcribed)."""
    g = json.loads((_HERE / "probe_grading.json").read_text(encoding="utf-8"))
    p = json.loads((_HERE / "probe_parity_report.json").read_text(encoding="utf-8"))
    c, tm, wl = g["columns"], g["timing"], g["win_loss_key_local"]
    L = ["=== probe decoder — Task-3 corpus decode + grading (summary) ===",
         f"instrument_commit {g['provenance']['instrument_commit']}",
         f"note_events_git_hash {g['provenance']['note_events_git_hash']}  "
         f"tables_git_hash {g['provenance']['tables_git_hash']}",
         f"leftover_rule {g['provenance']['leftover_rule']}  seg_cap {g['provenance']['seg_cap_events']}"
         f"  key_prune_topk {g['provenance']['key_prune_topk']}",
         f"cadence: {g['provenance']['cadence']}",
         f"fermata: {g['provenance']['fermata']}",
         f"coverage {g['provenance']['coverage']} graded / {g['provenance']['no_wir']} no-WiR;"
         f" decode mean {tm['mean_s']}s max {tm['max_s']}s total {tm['total_s']}s",
         "",
         "axis                PROBE-base   MEASURED     delta      Default(B/J/D)",
         "-" * 78]
    for axis, ck, bk in (("key vs LOCAL", "key_local_agree_pct", "key_local"),
                         ("key vs HOME", "key_home_agree_pct", "key_home"),
                         ("chord root", "root_agree_pct", "root"),
                         ("Roman numeral", "rn_agree_pct", "rn")):
        b = BASELINES[bk]
        pb = PROBE_BASELINE[ck]
        d = _delta(c[ck], pb)
        L.append(f"{axis:18s} {pb!s:12s} {c[ck]!s:12s} {d:+7.2f}    {b['Baroque']}/{b['Jazz']}/{b['Default']}")
    pv = g.get("prediction_verdict", {})
    L.append("")
    L.append(f"PREDICTION (<+/-1.0pp on every axis vs probe baseline): "
             f"{'HOLDS' if pv.get('holds') else 'SURPRISE — ' + str(pv.get('axes_over_1pp'))}")
    cf = g.get("cadence_feature_fires", {})
    if cf:
        L.append(f"cadence fires (WEIGHTLESS; {cf.get('boundaries',0)} committed boundaries; move NO score): "
                 f"leading_tone={cf.get('leading_tone',0)} tritone_pair={cf.get('tritone_pair',0)} "
                 f"dominant_tonic_bass={cf.get('dominant_tonic_bass',0)} "
                 f"fermata_location={cf.get('fermata_location',0)} any_fire={cf.get('any_fire',0)}")
    ch = g.get("chromatic_decodes", {})
    if ch:
        L.append(f"chromatic classes decoded (Task 3): {ch.get('n_segments',0)} segments on "
                 f"{ch.get('n_pieces',0)} pieces  {list(ch.get('by_piece',{}).keys())}")
    L += ["", f"key abstain: home {c['key_home_abstain_pct']}%  local {c['key_local_abstain_pct']}% "
              "(commits best path everywhere)",
          f"slowest pieces: {tm['slowest'][:6]}",
          "", "10 weakest key-local pieces:"]
    for r in wl["weakest_key_local"]:
        L.append(f"  {r['stem']:10s} key_local {r['key_local_agree_pct']:5.1f}%  root {r['root_agree_pct']:5.1f}%")
    L.append("10 strongest key-local pieces:")
    for r in wl["strongest_key_local"]:
        L.append(f"  {r['stem']:10s} key_local {r['key_local_agree_pct']:5.1f}%  root {r['root_agree_pct']:5.1f}%")
    vd = g.get("win_loss_vs_default")
    if vd:
        L += ["", f"-- per-piece vs Default baseline ({vd['n_pieces']} pieces) --",
              f"mean key_local delta {vd['mean_key_local_delta_pp']:+.2f}pp  root delta "
              f"{vd['mean_root_delta_pp']:+.2f}pp  (key_local better/worse "
              f"{vd['pieces_key_local_better']}/{vd['pieces_key_local_worse']})",
              "10 largest key-local WINS vs Default (stem: mine vs default):"]
        for r in vd["largest_key_local_wins"]:
            L.append(f"  {r['stem']:10s} {r['kl_delta']:+6.1f}pp  ({r['my_kl']} vs {r['def_kl']})  root {r['root_delta']:+.1f}pp")
        L.append("10 largest key-local LOSSES vs Default:")
        for r in vd["largest_key_local_losses"]:
            L.append(f"  {r['stem']:10s} {r['kl_delta']:+6.1f}pp  ({r['my_kl']} vs {r['def_kl']})  root {r['root_delta']:+.1f}pp")
    try:
        pl = json.loads((_HERE / "probe_prune_loss.json").read_text(encoding="utf-8"))
        L += ["", f"-- prune-loss (§5 reserve, {len(pl['provenance']['sample'])}-piece sample) --",
              f"tight(seg_cap{pl['tight']['seg_cap']},topK{pl['tight']['key_top_k']}): "
              f"root {pl['tight']['root_pct']} key_local {pl['tight']['key_local_pct']}",
              f"loose(seg_cap{pl['loose']['seg_cap']},topK{pl['loose']['key_top_k']}): "
              f"root {pl['loose']['root_pct']} key_local {pl['loose']['key_local_pct']}",
              f"LOSS: root {pl['loss_pp']['root']:+.2f}pp key_local {pl['loss_pp']['key_local']:+.2f}pp "
              f"at {pl['compute_ratio']}x compute -> the headline is a conservative LOWER BOUND"]
    except FileNotFoundError:
        pass
    (_HERE / "probe_grading_summary.txt").write_text("\n".join(L) + "\n", encoding="utf-8")

    # parity summary
    Lp = ["=== probe decoder — Task-2 establishment (parity + fitted recomputation) ===",
          f"instrument_commit {p['provenance']['instrument_commit']}",
          f"STRUCTURAL PARITY (synthetic, all non-cadence factors): "
          f"{sum(1 for r in p['structural_parity'] if r['kind']=='synthetic' and r['struct_pass'])}"
          f"/{sum(1 for r in p['structural_parity'] if r['kind']=='synthetic')} within +/-0.05; "
          f"structural_fail={p['structural_fail']}",
          "", "case        hyp        struct_delta   full_delta   cadence(me/desk)"]
    for r in p["structural_parity"]:
        Lp.append(f"{r['case']:11s} {r['hyp']:9s} {r['delta_struct']:+8.3f}    {r['delta_full']:+7.2f}"
                  f"     {r['my_cadence']:+.1f}/{r['desk_cadence']:+.1f}  [{r['kind']}]")
    fe = p.get("cadence_fire_establishment")
    if fe is not None:
        Lp += ["", f"-- cadence MECHANISM-FIRES establishment (Task 2): "
                   f"{'STOP' if p.get('cadence_fire_stop') else 'PASS'} --",
               "  (weightless features must FIRE where the desk-sim applied its credits)"]
        for r in fe:
            marks = []
            for f, d in r["per_feature"].items():
                tag = "OK" if d["match"] else ("slip" if d["classify"] == "documented_window_underspec" else "STOP")
                marks.append(f"{f.split('_')[0]}:desk{int(d['desk'])}/act{int(d['actual'])}[{tag}]")
            res = ("" if r["resolution_fires_only_at_arrival"] is None
                   else f"  resolution-only-at-arrival={r['resolution_fires_only_at_arrival']}")
            Lp.append(f"  {r['check'][:34]:34s} {r['case']}/{r['hyp']}@e{r['arrival_event']}: "
                      + " ".join(marks) + res)
    Lp += ["", "-- fitted-table recomputation (probe sensitive cells) --"]
    for lo in ("freq", "even"):
        f = p["fitted_recomputation"][lo]
        Lp.append(f"leftover={lo}:")
        for bn, rr in f["bwv352"].items():
            Lp.append(f"  bwv352 bass {bn:2s}: margin(viø7-i) {rr['margin_viø7_minus_i']:+.2f} winner {rr['winner']}")
        Lp.append(f"  bwv10.7: margin(split-merge) {f['bwv10.7']['margin_split_minus_merge']:+.2f} "
                  f"winner {f['bwv10.7']['winner']}")
    (_HERE / "probe_parity_summary.txt").write_text("\n".join(Lp) + "\n", encoding="utf-8")
    print("summaries written")


def main(argv):
    mode = argv[0] if argv else "all"
    if mode in ("parity", "all"):
        run_parity_artifact(write=True)
    if mode in ("corpus", "all"):
        run_corpus(write=True, verbose=True)
    if mode == "regrade":
        re_grade_from_artifact(write=True, verbose=True)
    if mode in ("regrade", "vsdefault"):
        add_vs_default(write=True, verbose=True)
    if mode == "pruneloss":
        measure_prune_loss(write=True, verbose=True)
    if mode == "summaries":
        write_summaries()


if __name__ == "__main__":
    main(sys.argv[1:])

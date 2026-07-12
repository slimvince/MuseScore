#!/usr/bin/env python3
"""gen_grading_fitting_dispositions.py — EG-7 Layer-5 audit PASS-1, grading+fitting
instruments subsplit (OI-116). Emits a closed-set disposition for EVERY deep inventory
row of the 6 grading/fitting instruments, at full vocabulary resolution.

READ-ONLY over the committed inventory tables. Writes ONLY the disposition artifacts
(pass1_dispositions_grading_fitting.csv/.json) under tools/audit/l5/. It touches no
production, no corpus, no robust_stop reference.

Scope (partition artifact pass1_partition.json -> INSTRUMENT.possible_subsplit."grading + fitting"):
  tools/analyze_inversion_errors.py  tools/music21_batch.py  tools/oracle_root_metric.py
  tools/calibration_fit.py           tools/c1_reliability.py tools/stage5_fit_driver.py

Verdict vocabulary (cowork_audit_protocol.md P2 + the L4/L5 instructions):
  code (functions / branches / io / crosslayer) : SURVIVES | RETIRES
  constants (numeric literals)                  : ESTABLISHED | UNFIT | DEAD
  (premises would be FACT/THEORY/ASSUMPTION and derived facts PUBLISHED/SILOED/TRAPPED/
   DUPLICATED; the grading/fitting instruments carry no standalone premise rows — the
   establishment answers live in the per-row notes and the report's establishment table.)

"no issue" is a RECORDED claim with a stated reason (P2): every row carries verdict +
category + note; `flag=1` marks a row surfaced in the report.
"""
from __future__ import annotations
import csv, json, os
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
SCOPE = {
    "tools/analyze_inversion_errors.py", "tools/music21_batch.py",
    "tools/oracle_root_metric.py", "tools/calibration_fit.py",
    "tools/c1_reliability.py", "tools/stage5_fit_driver.py",
}

# ── literal overrides keyed (file, line) or (file, line, value) ─────────────────────────
# value strings match the inventory column exactly (e.g. "0.7", "480", "1e-09").
AIE = "tools/analyze_inversion_errors.py"
MB  = "tools/music21_batch.py"
ORM = "tools/oracle_root_metric.py"
CF  = "tools/calibration_fit.py"
C1  = "tools/c1_reliability.py"
S5  = "tools/stage5_fit_driver.py"

# (verdict, category, flag, note)
LIT_OVERRIDE = {
    # analyze_inversion_errors --------------------------------------------------------
    (AIE, "322", "0.7"): ("ESTABLISHED", "value-copied-constant", 1,
        "INVERSION_SUSPICION_MARGIN=0.70 hardcodes a copy of the production pref "
        "inversionSuspicionMargin (also carried in stage5 PARAMS + param_manifest.json); "
        "the blocker analysis silently assumes production margin=0.70 and drifts if the "
        "pref moves (value-copied constant)."),
    (AIE, "273", "0.26"): ("UNFIT", "grading-tolerance", 1,
        "beat-classification window +/-0.26 around integer beats -- hand-set, no cited "
        "provenance (why 0.26 rather than 0.25/0.5?)."),
    (AIE, "274", "0.26"): ("UNFIT", "grading-tolerance", 1, "beat-classification window +/-0.26 (hand-set)."),
    (AIE, "275", "0.26"): ("UNFIT", "grading-tolerance", 1, "beat-classification window +/-0.26 (hand-set)."),
    (AIE, "276", "0.26"): ("UNFIT", "grading-tolerance", 1, "beat-classification window +/-0.26 (hand-set)."),
    (AIE, "260", "3"): ("UNFIT", "grading-bucket", 1,
        "noteCount>=3 'genuine chord' bucket boundary -- interpretive threshold, no cited provenance."),
    (AIE, "289", "3"): ("UNFIT", "grading-bucket", 1, "noteCount>=3 targetable-error bucket (interpretive)."),
    (AIE, "292", "3"): ("UNFIT", "grading-bucket", 1, "noteCount>=3 targetable-error bucket (interpretive)."),
    (AIE, "214", "2.0"): ("DEAD", "dead-computation", 1,
        "lt_2 = count(margins<2.0) is computed but never printed or used downstream -- dead variable."),
    (AIE, "215", "2.0"): ("UNFIT", "grading-bucket", 1,
        "margin>=2.0 bucket carries the interpretive claim (line 301) 'fix won't help, likely correct' "
        "-- an unvalidated interpretation attached to a hand-set boundary."),
    (AIE, "210", "0.25"): ("ESTABLISHED", "grading-bucket", 0, "margin<0.25 'barely wins' bucket (presentation of the margin distribution)."),
    (AIE, "211", "0.5"): ("ESTABLISHED", "grading-bucket", 0, "margin<0.5 low-confidence bucket."),
    (AIE, "213", "1.5"): ("ESTABLISHED", "grading-bucket", 0, "margin<1.5 bucket."),
    (AIE, "216", "0.5"): ("ESTABLISHED", "grading-bucket", 0, "0.5<=margin<2.0 moderate band."),
    (AIE, "216", "2.0"): ("ESTABLISHED", "grading-bucket", 0, "0.5<=margin<2.0 moderate band."),
    (AIE, "288", "0.5"): ("ESTABLISHED", "grading-bucket", 0, "targetable margin<0.5 summary."),
    (AIE, "305", "0.25"): ("ESTABLISHED", "presentation", 0, "margin histogram bin width 0.25."),
    (AIE, "305", "12"): ("ESTABLISHED", "presentation", 0, "12 histogram bins of 0.25 = [0,3)."),
    (AIE, "310", "3.0"): ("ESTABLISHED", "presentation", 0, "histogram tail margin>=3.0."),
    (AIE, "259", "2"): ("ESTABLISHED", "grading-bucket", 0, "noteCount==2 'ambiguous' bucket label."),
    # c1_reliability ------------------------------------------------------------------
    (C1, "63", "3.5"): ("ESTABLISHED", "squash-constant", 1,
        "SQUASH_K_CADENCE=3.5 declared; the c1 run observes median tonicVote=3.5 (reproduce-check "
        "corroborates). Ranking is squash-invariant so the monotonicity finding is k-independent "
        "(docstring); only [0,1] bin placement/ECE depends on k."),
    (C1, "73", "10"): ("ESTABLISHED", "binning-convention", 0, "10 equal-width reliability bins on [0,1]."),
    (C1, "110", "1e-09"): ("ESTABLISHED", "epsilon", 0, "monotonicity-violation numeric epsilon."),
    # calibration_fit -----------------------------------------------------------------
    (CF, "219", "0.05"): ("UNFIT", "shape-selection-tolerance", 1,
        "near_logistic threshold 0.05 (isotonic-vs-Platt selection): the RULE is design 4.5.1-cited "
        "but the 0.05 magnitude is hand-set with no stated provenance."),
    (CF, "199", "50"): ("UNFIT", "min-sample-bucket", 1,
        "INSUFFICIENT-cells boundary (fit<50) -- hand-set minimum sample size, no cited provenance."),
    (CF, "199", "20"): ("UNFIT", "min-sample-bucket", 1,
        "INSUFFICIENT-cells boundary (held<20) -- hand-set minimum sample size, no cited provenance."),
    (CF, "174", "1000000.0"): ("ESTABLISHED", "solver-param", 0,
        "C=1e6 near-unregularized logistic == Platt scaling (documented in code)."),
    (CF, "174", "10000"): ("ESTABLISHED", "solver-param", 0, "LogisticRegression max_iter."),
    (CF, "221", "1e-06"): ("ESTABLISHED", "epsilon", 0, "platt_not_worse tie tolerance."),
    (CF, "226", "50"): ("ESTABLISHED", "grading-boundary", 0, "flat-band low-band [0,0.5) assertion boundary (design 4.5)."),
    (CF, "226", "100.0"): ("ESTABLISHED", "presentation", 0, "low-band grid resolution."),
    (CF, "215", "100.0"): ("ESTABLISHED", "presentation", 0, "near-logistic test grid resolution."),
    (CF, "215", "101"): ("ESTABLISHED", "presentation", 0, "near-logistic test grid point count."),
    # music21_batch -------------------------------------------------------------------
    (MB, "71", "480"): ("ESTABLISHED", "value-copied-constant", 1,
        "TICKS_PER_QUARTER=480 duplicates MuseScore Constants::DIVISION (documented). Value-copied; "
        "silently drifts if DIVISION ever changes (DIVISION is fixed, so low risk)."),
    (MB, "193", "4"): ("UNFIT", "oracle-param", 1,
        "FloatingKey.numFlats=4 -- local-key search bounded to +/-4 flats, hand-set with no cited "
        "provenance; shapes keyLocal, which feeds oracle_root_metric's KEY tiers."),
    (MB, "194", "4"): ("UNFIT", "oracle-param", 1,
        "FloatingKey.numSharps=4 -- local-key search bounded to +/-4 sharps, hand-set (no provenance)."),
    (MB, "108", "4"): ("ESTABLISHED", "corpus-membership", 1,
        "len(score.parts)!=4 SATB filter (definitional 4-voice chorale); defines corpus membership "
        "(the 352-count denominator)."),
    # oracle_root_metric --------------------------------------------------------------
    (ORM, "229", "2"): ("ESTABLISHED", "structural-threshold", 0,
        ">=2 distinct oracle roots inside one covering region ==> OVER-GRAB (definitional segmentation test)."),
    (ORM, "93", "12"): ("ESTABLISHED", "music-theory-constant", 0, "pitch-class modulo 12."),
    (ORM, "109", "12"): ("ESTABLISHED", "music-theory-constant", 0, "pitch-class modulo 12."),
    (ORM, "141", "12"): ("ESTABLISHED", "music-theory-constant", 0, "pitch-class modulo 12."),
    (ORM, "317", "6"): ("ESTABLISHED", "presentation", 0, "keep <=6 worked examples per tier."),
    # stage5_fit_driver ---------------------------------------------------------------
    (S5, "206", "0.2"): ("ESTABLISHED", "split-convention", 0, "held_frac 0.2 = ~80/20 stratified split (design 4.3 1a)."),
    (S5, "367", "0.05"): ("ESTABLISHED", "step-policy", 0, "perturbation +/-0.05 for values in [0,1] (design 4.3 1b)."),
    (S5, "367", "0.1"): ("ESTABLISHED", "step-policy", 0, "perturbation +/-10% for values >1 (design 4.3 1b)."),
    (S5, "405", "1.2"): ("ESTABLISHED", "optimizer-default", 0, "fit upper bound default (design 5)."),
    (S5, "406", "9"): ("ESTABLISHED", "optimizer-default", 0, "coarse-ladder step count."),
    (S5, "407", "2"): ("ESTABLISHED", "optimizer-default", 0, "refine rounds."),
    (S5, "608", "63.36"): ("ESTABLISHED", "reproduce-target", 1,
        "RATIFIED Baroque baseline hand-transcribed; reproduced EXACTLY by the fixture this run (MATCH) "
        "and matches CLAUDE.md. Hand-maintained (comment shows a prior 63.32->63.36 hand-update at 2.2e) "
        "-- must be re-synced at each corpus re-baseline. Self-checking: the fixture FAILS loudly if it drifts."),
    (S5, "608", "62.37"): ("ESTABLISHED", "reproduce-target", 1, "RATIFIED Jazz baseline; fixture MATCH; hand-maintained."),
    (S5, "608", "63.25"): ("ESTABLISHED", "reproduce-target", 1, "RATIFIED Default baseline; fixture MATCH; hand-maintained."),
    (S5, "620", "0.005"): ("ESTABLISHED", "reproduce-tolerance", 0, "fixture match tolerance = half the last printed digit."),
    (S5, "533", "1e-09"): ("ESTABLISHED", "epsilon", 0, "already-optimal delta epsilon."),
    (S5, "633", "0.9"): ("ESTABLISHED", "test-input", 0, "determinism-check perturbation value (arbitrary)."),
    (S5, "634", "0.9"): ("ESTABLISHED", "test-input", 0, "determinism-check perturbation value (arbitrary)."),
    (S5, "214", "2"): ("ESTABLISHED", "structural", 0, "min split step floor = 2."),
}

# stage5 PARAMS fit-surface mirror: module-scope literals on the PARAMS dict (lines 67-146,
# per_preset lines contribute multiple values). The dict opens at 65 and closes at 147.
S5_PARAMS_LINES = set(range(67, 147))

# branches to flag as silent-failure swallows (broad except that drops data with no signal)
SILENT_SWALLOW = {
    (AIE, "149"),                                   # WiR parse except: pass (silent loss of 3-way coverage)
    (ORM, "159"), (ORM, "169"),                     # load/wir except: continue / []
    (C1, "169"), (C1, "187"), (C1, "196"), (C1, "237"), (C1, "246"), (C1, "292"),
    (CF, "57"), (CF, "77"), (CF, "86"), (CF, "122"), (CF, "131"),
    (MB, "199"),                                    # chordify fail -> 0-region .music21.json silently written to corpus
}
# branch that prints a WRONG path in its error message
WRONG_PATH_MSG = {(AIE, "102")}  # "No .ours.json files in tools/reports/corpus/" -- actually reads corpus_dir

# functions carrying grading/establishment decisions (specific establishment note)
FUNC_NOTE = {
    (AIE, "_infer_quality"): "tool-local chord-SYMBOL->quality heuristic; unmatched body defaults to 'Major' (line 56) -- a silent misclassification path.",
    (ORM, "parse_our_key"): "tool-local key parser; a mode suffix absent from _OUR_MINOR/_MAJOR_MODES returns mode=None -> mode-agnostic key match (silently masks a mode error).",
    (ORM, "parse_m21_key"): "music21 key parser; a key string not matching ' major'/' minor' returns None -> AMBIGUOUS/dispute grain.",
    (ORM, "classify_charged_event"): "the 5-tier grading classifier; conventions: unparseable key->AMBIGUOUS, >=2 oracle roots->OVER-GRAB, mode compared only when both sides resolve to maj/min.",
    (CF, "fit_row"): "the fitting decision: isotonic-default / Platt-if-near-logistic-and-not-worse; carries the 50/20 sufficiency + 0.05 near-logistic tolerances.",
    (C1, "curve_diagnostics"): "the ECE/monotonicity/signed-gap grading; monotonicity is squash-invariant, ECE is not.",
    (MB, "analyze_chorale"): "the music21 GT producer; chordify failure yields 0 regions + an 'error' field (silently written).",
    (MB, "_normalize_quality"): "music21 quality->bucket map; dominant/major-seventh collapse to 'Major', minor-seventh to 'Minor' (seventh->triad grading convention); unmapped->'Unknown'.",
    (S5, "evaluate"): "the objective+constraint evaluator; constraint = a8 robust-unit class-(b) non-increase + no new class-(b) case (NOT the batch stop the docstring names).",
    (S5, "measure"): "reads the a8 summary/mapping; root/rn/key% + per-run class map = the reproduce surface.",
}

def load(table):
    rows = []
    with open(os.path.join(BASE, table + ".csv"), newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["file"] in SCOPE:
                rows.append(r)
    return rows

PRESENT_HINT = ("='*", "'*", ":.1f", ":>", ":<", "sys.exit", "[-400", "most_common",
                "indent=", "round(", "% 12", "m.group", "len(parts)")

def lit_default(r):
    ctx = r["context"]
    v = r["value"]
    # PARAMS fit-surface mirror
    if r["file"] == S5 and r["func"] == "<module-scope>" and int(r["line"]) in S5_PARAMS_LINES:
        return ("ESTABLISHED", "fit-surface-mirror", 0,
                "fit-surface parameter value mirrored from the C++ source + param_manifest.json; "
                "established by the fixture reproduce-check for sensitive params (see report's "
                "PARAMS triple-representation finding for the zero-sensitivity gap). In param_manifest: yes.")
    # presentation / structural defaults
    if any(h in ctx for h in ("=\"=\"", "'='", "'-'", "*70", "*78", "*86", "*60", "*52",
                              "100*", "100 *", ":.1f", ":>", ":<", "sys.exit", "[-400",
                              "most_common", "indent=", "round(", "% 12", "m.group",
                              "len(parts)", "numFlats", "numSharps")):
        return ("ESTABLISHED", "presentation", 0, "display/format/structural constant; no inference effect.")
    return ("ESTABLISHED", "structural", 0, "structural constant reviewed at source; not inference-affecting.")

def main():
    out_rows = []

    # functions -> SURVIVES
    for r in load("l5_functions"):
        note = FUNC_NOTE.get((r["file"], r["name"]), "live instrument function.")
        flag = 1 if (r["file"], r["name"]) in FUNC_NOTE else 0
        out_rows.append(dict(file=r["file"], line=r["start_line"], row_type="function",
                             item=r["name"], func=r["name"], verdict="SURVIVES",
                             category="instrument-function", flag=flag, note=note))

    # branches -> SURVIVES (flag silent swallows + wrong-path msg)
    for r in load("l5_branches"):
        key = (r["file"], r["line"])
        if key in SILENT_SWALLOW:
            cat, flag = "silent-failure-swallow", 1
            note = ("broad except/guard drops a score/region/value from the measurement denominator "
                    "with no stderr signal (silent partial-coverage path).")
        elif key in WRONG_PATH_MSG:
            cat, flag = "misleading-error-message", 1
            note = ("empty-input error prints 'No .ours.json files in tools/reports/corpus/' but the "
                    "code actually reads corpus_dir (default tools/corpus/baroque) -- stale message path.")
        else:
            cat, flag = "control-flow", 0
            note = f"{r['kind']} branch in {r['func']}."
        out_rows.append(dict(file=r["file"], line=r["line"], row_type="branch",
                             item=r["kind"], func=r["func"], verdict="SURVIVES",
                             category=cat, flag=flag, note=note))

    # literals -> ESTABLISHED / UNFIT / DEAD
    for r in load("l5_literals"):
        ov = LIT_OVERRIDE.get((r["file"], r["line"], r["value"])) or LIT_OVERRIDE.get((r["file"], r["line"]))
        if ov:
            verdict, cat, flag, note = ov
        else:
            verdict, cat, flag, note = lit_default(r)
        out_rows.append(dict(file=r["file"], line=r["line"], row_type="literal",
                             item=r["value"], func=r["func"], verdict=verdict,
                             category=cat, flag=flag, note=note))

    # io -> SURVIVES. flag=1 for a DANGEROUS DEFAULT that overwrites a committed reference;
    # flag=0 for a by-design committed-artifact write (recorded, not a defect).
    COMMITTED_WRITE = {
        (MB, "439"): (1, "default --output tools/corpus writes .music21.json into the COMMITTED canonical corpus (dangerous default)."),
        (CF, "323"): (1, "default --out-dir tools/calibration_maps writes into a COMMITTED location (dangerous default)."),
        (CF, "333"): (1, "default --out-dir tools/calibration_maps writes into a COMMITTED location (dangerous default)."),
        (S5, "242"): (1, "split-mode writes the COMMITTED tools/stage5_split_registry.json (dangerous default)."),
        (S5, "432"): (1, "split-mode writes the COMMITTED tools/stage5_split_registry.json (dangerous default)."),
        (S5, "491"): (0, "fit-mode appends to the COMMITTED tools/fit_ledgers -- by design (O-8), not a defect."),
        (S5, "594"): (0, "audit-mode appends to the COMMITTED tools/fit_ledgers -- by design (O-8), not a defect."),
    }
    for r in load("l5_io"):
        key = (r["file"], r["line"])
        call = r["call"]
        is_write = call in ("write_text", "dump", "open", "mkdir")
        if key in COMMITTED_WRITE:
            cwflag, cwnote = COMMITTED_WRITE[key]
            cat, flag, note = "io-write-committed", cwflag, cwnote
        elif is_write:
            cat, flag, note = "io-write", 0, "writes a scratch/artifact output."
        else:
            cat, flag, note = "io-read", 0, "consumes a reference/substrate artifact."
        out_rows.append(dict(file=r["file"], line=r["line"], row_type="io",
                             item=call, func=r["func"], verdict="SURVIVES",
                             category=cat, flag=flag, note=note))

    # crosslayer (internal imports) -> SURVIVES / reuse-verbatim
    for r in load("l5_crosslayer"):
        out_rows.append(dict(file=r["file"], line=r["line"], row_type="crosslayer",
                             item=r["include"], func="<import>", verdict="SURVIVES",
                             category="reuse-verbatim-import", flag=0,
                             note=f"imports {r['include']} (shared regression-stop-core primitive); "
                                  f"one-path reuse (#6), not a fork."))

    # ── write CSV ──
    cols = ["file", "line", "row_type", "item", "func", "verdict", "category", "flag", "note"]
    csv_path = os.path.join(BASE, "pass1_dispositions_grading_fitting.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for row in out_rows:
            w.writerow(row)

    # ── write JSON summary ──
    by_verdict = Counter(r["verdict"] for r in out_rows)
    by_type = Counter(r["row_type"] for r in out_rows)
    by_cat = Counter(r["category"] for r in out_rows)
    by_file = Counter(r["file"] for r in out_rows)
    flagged = [r for r in out_rows if r["flag"]]
    summary = {
        "audit": "EG-7 Layer-5 PASS-1 grading+fitting instruments subsplit (OI-116)",
        "scope_files": sorted(SCOPE),
        "total_rows": len(out_rows),
        "by_verdict": dict(by_verdict),
        "by_row_type": dict(by_type),
        "by_category": dict(by_cat),
        "by_file": dict(by_file),
        "flagged_count": len(flagged),
        "flagged": [{"file": r["file"], "line": r["line"], "row_type": r["row_type"],
                     "item": r["item"], "verdict": r["verdict"], "category": r["category"],
                     "note": r["note"]} for r in flagged],
    }
    json_path = os.path.join(BASE, "pass1_dispositions_grading_fitting.json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1)

    print(f"rows={len(out_rows)}  verdicts={dict(by_verdict)}  flagged={len(flagged)}")
    print(f"by_type={dict(by_type)}")
    print(f"wrote {csv_path}")
    print(f"wrote {json_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""gen_fold_assignment.py — the OI-176 held-out-split artifact generator.

READ-ONLY / MEASUREMENT-LAYER. No src/ change, no corpus mutation, no gate change,
no value fitted. This generates the committed, seeded, grouped 5-fold assignment the
ratified held-out evaluation protocol (`cowork_prefit_gates.md`, OI-176, user-ratified
2026-07-19) requires. It is generated ONCE and never regenerated outside a protocol
amendment (a re-split is a protocol amendment, #22).

WHAT IT DOES (the ratified protocol, executed):
  1. Enumerate the WiR-covered stems through the EXISTING coverage resolution — the same
     find_wir_file / load_wir_regions / load_analysis chain a8_rebaseline_measure.measure_preset
     uses (imported, not re-derived). Establishment check: the covered-stem count MUST equal
     326 (CLAUDE.md gate block (A) coverage); otherwise STOP (exit nonzero).
  2. Group by WiR analysis file — stems resolving to the same analysis.txt share a group
     (the ratified leakage guard). 326 stems -> 324 files (a small number of multi-stem groups).
  3. Balance weight = per-stem graded duration (PieceGrid.scored_dur), computed by IMPORTING
     a8_rebaseline_measure.build_piece_grid against the committed Default corpus dir. Fold
     membership is preset-independent; the Default corpus is the DECLARED preset-independent
     balance-weight source. No a8 file is edited.
  4. Assignment: seeded shuffle of the group list (seed 20260719), then deterministic greedy —
     each group in shuffled order goes to the currently lightest-total-duration fold. 5 folds.
  5. Output tools/joint_estimator/fold_assignment.json — per fold: stem/group lists, piece
     count, total scored duration; plus provenance (corpus git_hash, seed, generator path,
     coverage count, the analysis-file multimap). Every figure generated, nothing hand-typed
     (#17f).

REUSE (TOTAL UNIFICATION, #6): imports and reuses verbatim —
  - compare_analyses.load_analysis            (our-region loader)
  - dcml_parser.find_wir_file                 (stem -> analysis.txt resolution / grouping key)
  - dcml_parser.load_wir_regions              (the OI-142-corrected WiR loading substrate)
  - a8_rebaseline_measure.build_piece_grid    (the graded-duration primitive; self-validates
                                               its variant-(b) buckets == grid_score_regions)
Nothing new is defined that any of these already provides.

Usage:
    python tools/joint_estimator/gen_fold_assignment.py                # writes the committed artifact
    python tools/joint_estimator/gen_fold_assignment.py --out <path>   # writes elsewhere (reproducibility check)
"""
from __future__ import annotations

import argparse
import json
import random
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent.parent   # tools/joint_estimator/ -> repo root
sys.path.insert(0, str(_ROOT / "tools"))

import compare_analyses as cmp          # noqa: E402
import dcml_parser as dcml              # noqa: E402
import a8_rebaseline_measure as a8      # noqa: E402

WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")
DEFAULT_CORPUS_DIR = _ROOT / "tools" / "corpus" / "default"

# ── Ratified protocol constants (`cowork_prefit_gates.md`, [prov-ratify]) ──
# Changing either is a protocol amendment (#22), not a tuning act.
SEED = 20260719          # committed shuffle seed (this dispatch's date)
N_FOLDS = 5              # 5-fold cross-validation
EXPECTED_COVERAGE = 326  # CLAUDE.md gate block (A) WiR coverage at 326/352


def _rel(p) -> str:
    """Repo-relative path with forward slashes (stable across machines)."""
    return Path(p).resolve().relative_to(_ROOT).as_posix()


def _git_head() -> str:
    """The corpus git_hash = repo HEAD at generation time (manifest pattern, #16)."""
    out = subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                         capture_output=True, text=True, check=True)
    return out.stdout.strip()


def enumerate_coverage():
    """Enumerate WiR-covered stems through the EXISTING coverage resolution (the same
    chain a8_rebaseline_measure.measure_preset walks). Returns:
      covered   : sorted list of covered stems
      stem_wir  : {stem -> analysis.txt path}
      stem_dur  : {stem -> PieceGrid.scored_dur (Default corpus)}
      diag      : dict of coverage diagnostics
    STOPs (SystemExit) if the covered count != EXPECTED_COVERAGE.
    """
    if not DEFAULT_CORPUS_DIR.is_dir():
        sys.exit(f"STOP: Default corpus dir not found: {DEFAULT_CORPUS_DIR}")

    ours_files = sorted(DEFAULT_CORPUS_DIR.glob("*.ours.json"))
    covered, stem_wir, stem_dur = [], {}, {}
    empty_ours = no_wir = wir_parse_fail = 0
    for p in ours_files:
        stem = p.name.replace(".ours.json", "")
        try:
            _, ours_regions = cmp.load_analysis(p)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            sys.exit(f"STOP: .ours.json load failed for {stem}: {type(exc).__name__}: {exc}")
        if not ours_regions:
            empty_ours += 1
            continue
        wir_path = dcml.find_wir_file(WIR_DIR, stem)
        if wir_path is None:
            no_wir += 1                      # legitimate exclusion (no human GT)
            continue
        wir_regions = dcml.load_wir_regions(WIR_DIR, stem)
        if not wir_regions:
            wir_parse_fail += 1              # present WiR file but no scoreable region
            continue
        # graded-duration balance weight (Default corpus), via the pinned a8 primitive.
        m21_regions = []
        m21_path = DEFAULT_CORPUS_DIR / f"{stem}.music21.json"
        if m21_path.exists():
            try:
                _, m21_regions = cmp.load_analysis(m21_path)
            except (OSError, ValueError, KeyError, TypeError):
                m21_regions = []             # m21 leg does not affect scored_dur
        pg = a8.build_piece_grid(stem, ours_regions, wir_regions, m21_regions)
        covered.append(stem)
        stem_wir[stem] = wir_path
        stem_dur[stem] = pg.scored_dur

    diag = {
        "total_ours_files": len(ours_files),
        "empty_ours": empty_ours,
        "no_wir": no_wir,
        "wir_parse_fail": wir_parse_fail,
        "covered": len(covered),
    }
    if len(covered) != EXPECTED_COVERAGE:
        sys.exit(f"STOP: covered-stem count {len(covered)} != expected {EXPECTED_COVERAGE} "
                 f"(coverage diagnostics: {diag}). Not proceeding on a different population.")
    return sorted(covered), stem_wir, stem_dur, diag


def build_groups(covered, stem_wir, stem_dur):
    """Group stems by their WiR analysis file. Returns a list of group dicts sorted by
    group_label (the analysis folder name — unique per chorale folder), each with member
    stems (sorted), the repo-relative analysis path, and the summed scored duration."""
    by_file = {}
    for stem in covered:
        by_file.setdefault(stem_wir[stem], []).append(stem)
    groups = []
    for wir_path, stems in by_file.items():
        stems = sorted(stems)
        groups.append({
            "group_label": Path(wir_path).parent.name,      # e.g. "026" (unique folder)
            "analysis_file": _rel(wir_path),
            "stems": stems,
            "scored_dur": sum(stem_dur[s] for s in stems),
        })
    groups.sort(key=lambda g: g["group_label"])             # deterministic base order
    return groups


def assign_folds(groups):
    """Seeded shuffle of the group list, then deterministic greedy least-duration-first
    assignment into N_FOLDS folds. Returns the fold list (each a dict)."""
    shuffled = list(groups)
    random.Random(SEED).shuffle(shuffled)                   # seed committed in the artifact

    folds = [{"fold": i, "stems": [], "groups": [], "total_scored_dur": 0}
             for i in range(N_FOLDS)]
    for g in shuffled:
        # lightest fold; tie-break on lowest fold index (deterministic)
        target = min(folds, key=lambda f: (f["total_scored_dur"], f["fold"]))
        target["groups"].append(g["group_label"])
        target["stems"].extend(g["stems"])
        target["total_scored_dur"] += g["scored_dur"]
    for f in folds:
        f["stems"].sort()
        f["groups"].sort()
        f["piece_count"] = len(f["stems"])
        f["group_count"] = len(f["groups"])
    return folds


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "fold_assignment.json"),
                    help="Output path (default: the committed artifact). Use a scratch path "
                         "for the run-twice reproducibility check.")
    args = ap.parse_args()

    covered, stem_wir, stem_dur, diag = enumerate_coverage()
    groups = build_groups(covered, stem_wir, stem_dur)
    folds = assign_folds(groups)

    # stem index (group + fold + weight per stem) — no information loss (#12), and the
    # lookup Task B (the count inventory) reads for its per-fold keying.
    stem_to_fold = {}
    for f in folds:
        for s in f["stems"]:
            stem_to_fold[s] = f["fold"]
    stem_index = {
        s: {"group": Path(stem_wir[s]).parent.name,
            "fold": stem_to_fold[s],
            "scored_dur": stem_dur[s]}
        for s in covered
    }

    multi = {g["group_label"]: g["stems"] for g in groups if len(g["stems"]) > 1}

    artifact = {
        "provenance": {
            "generator": _rel(__file__),
            "corpus_git_hash": _git_head(),
            "seed": SEED,
            "n_folds": N_FOLDS,
            "balance_weight": (
                "PieceGrid.scored_dur (a8_rebaseline_measure.build_piece_grid) against the "
                "committed Default corpus (tools/corpus/default); the declared preset-independent "
                "balance-weight source. Fold membership is preset-independent."),
            "coverage_resolution": (
                "compare_analyses.load_analysis + dcml_parser.find_wir_file + "
                "dcml_parser.load_wir_regions (the OI-142-corrected substrate); identical to "
                "a8_rebaseline_measure.measure_preset."),
            "expected_coverage": EXPECTED_COVERAGE,
            "coverage_diagnostics": diag,
            "wir_dir": _rel(WIR_DIR),
            "default_corpus_dir": _rel(DEFAULT_CORPUS_DIR),
            "protocol": "cowork_prefit_gates.md (OI-176), user-ratified 2026-07-19",
        },
        "coverage_count": len(covered),
        "distinct_analysis_files": len(groups),
        "multi_stem_groups": multi,
        "folds": folds,
        "groups": groups,
        "stem_index": stem_index,
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(artifact, indent=1, ensure_ascii=False) + "\n",
                        encoding="utf-8")

    print(f"Wrote {out_path}")
    print(f"  coverage: {len(covered)} stems -> {len(groups)} analysis files; "
          f"multi-stem groups: {multi}")
    for f in folds:
        print(f"  fold {f['fold']}: {f['piece_count']} pieces, {f['group_count']} groups, "
              f"scored_dur={f['total_scored_dur']}")


if __name__ == "__main__":
    main()

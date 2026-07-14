#!/usr/bin/env python3
"""Re-stamp the committed robust-stop reference from a candidate a8 measurement.

Guiding principle #17(f): no hand-transcribed measurement numbers. Every figure in
`tools/robust_stop/manifest.json` is DERIVED here from the candidate `summary.json` that
`tools/a8_rebaseline_measure.py` produced — the same derivation the consuming instrument
`tools/robust_stop_diff.py` uses (all four agreement columns are duration fractions of
`scored_dur`; the key columns therefore carry their abstain duration in the denominator,
the OI-33 convention).

This script does NOT decide whether a re-baseline is allowed. Run `robust_stop_diff.py`
first and read its verdict: the hard stop is the class-(b) root-disagree duration
non-increase on every preset, plus an explained run-level set-diff (CLAUDE.md gate block (A)).
Snapshot the outgoing reference (O-12) before invoking this.

Usage:
    python tools/robust_stop_restamp.py --candidate <a8-out-dir> \
        --artifact "<what this reference is>" --dispatch "<the instruction>" \
        --date 2026-07-14 --head <short-sha> --corpus-hash <short-sha> \
        --snapshot tools/robust_stop/snapshot_.../ --ratified 2026-07-14 \
        [--reproduce-note "..."] [--dry-run]
"""
import argparse
import json
import shutil
from pathlib import Path

REF_DIR = Path("tools/robust_stop")
PRESETS = ("baroque", "jazz", "default")

# The enumeration/mapping artifacts the reference carries, per preset. The `_cells` files the
# instrument also emits are diagnostics and are deliberately NOT part of the committed reference
# (only the run-level enumerations are — the run is the stop's identity unit).
PER_PRESET_FILES = (
    "{p}_variant_a_root_fail_runs.txt",
    "{p}_variant_b_root_fail_runs.txt",
    "{p}_mapping.json",
)


def preset_block(summary: dict, preset: str) -> dict:
    """Derive one manifest preset block from the candidate summary. Denominator = scored_dur
    for every agreement column — verified to reproduce the committed reference exactly."""
    s = summary[preset]
    a = s["agg"]
    sd = a["scored_dur"]

    def pct(num: int) -> float:
        return round(100.0 * num / sd, 4) if sd else 0.0

    return {
        "scored_dur": sd,
        "unscored_dur": a["unscored_dur"],
        "root_agree_pct": pct(a["b_root_agree"]),
        "rn_agree_pct": pct(a["b_rn_agree"]),
        "key_agree_pct": pct(a["b_key_agree"]),
        "key_agree_pct_local": pct(a["b_key_agree_local"]),
        "key_parse_fail_pct": pct(a["b_key_fail"]),
        "root_disagree_dur": a["b_root_dis"],
        "root_disagree_cells": a["b_root_dis_cells"],
        "class_b_root_disagree_dur": a["b_cls_b_dur"],
        "class_b_root_disagree_cells": a["b_cls_b_cells"],
        "class_a_root_disagree_dur": a["b_cls_a_dur"],
        "class_a_root_disagree_cells": a["b_cls_a_cells"],
        "variant_b_root_fail_runs": s["grid_b_root_fail_runs"],
        "variant_b_root_fail_cells": s["grid_b_root_fail_cells"],
        "variant_a_root_fail_runs": s["grid_a_root_fail_runs"],
        "variant_a_root_fail_cells": s["grid_a_root_fail_cells"],
        "variant_a_root_disagree_dur": a["a_root_dis_dur"],
        "variant_a_class_b_dur": a["a_cls_b_dur"],
        "variant_a_class_a_dur": a["a_cls_a_dur"],
        "batch_stop_count": s["batch_gate_count"],
        "mapping_summary": s["mapping_summary"],
        "coverage": {
            k: s["coverage"][k]
            for k in ("total_ours_files", "wir_covered", "m21_and_wir", "no_wir",
                      "wir_no_annotation", "wir_parse_fail", "wir_source_sha256")
        },
        "run_enumeration_file": f"{preset}_variant_b_root_fail_runs.txt",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True, type=Path,
                    help="a8_rebaseline_measure.py --out-dir of the ADOPTED candidate")
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--dispatch", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--head", required=True, help="short sha of HEAD at generation")
    ap.add_argument("--corpus-hash", required=True)
    ap.add_argument("--snapshot", required=True, help="the O-12 outgoing-reference snapshot dir")
    ap.add_argument("--ratified", required=True)
    ap.add_argument("--adoption-commit", default="")
    ap.add_argument("--instrument-note", default="")
    ap.add_argument("--reproduce-note", default="")
    ap.add_argument("--supersedes-key", default="",
                    help="reproduce_status key under which to preserve the OUTGOING columns, "
                         "e.g. superseded_oi132_oi144 (#12 — never drop a replaced column)")
    ap.add_argument("--supersedes-note", default="")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    summary = json.load(open(args.candidate / "summary.json", encoding="utf-8"))
    old = json.load(open(REF_DIR / "manifest.json", encoding="utf-8"))

    # DT-24 guard (destructive write to a COMMITTED reference). This tool overwrites
    # tools/robust_stop/ by design — that is what a re-baseline is — so the O-12 discipline is
    # enforced mechanically here rather than left to convention: refuse to write unless the
    # named outgoing-reference snapshot actually exists on disk. `--snapshot` is a required
    # argument, so a no-arg invocation cannot reach this point at all.
    if not args.dry_run:
        snap = Path(args.snapshot.split(" (")[0].rstrip("/"))
        if not (snap.is_dir() and (snap / "manifest.json").is_file()):
            print(f"REFUSING to re-stamp {REF_DIR}/: the O-12 outgoing-reference snapshot "
                  f"'{snap}' does not exist (expected a directory containing manifest.json).\n"
                  f"Snapshot the outgoing reference FIRST (guiding principle #16 / O-12), or "
                  f"pass --dry-run to preview.")
            return 2

    manifest = {
        "schema": old["schema"],
        "artifact": args.artifact,
        "date": args.date,
        "dispatch": args.dispatch,
        # Convention notes are the reference's standing contract, not per-event figures: carried
        # forward verbatim (they describe how the columns are defined, and that has not changed).
        "coverage_hardening_note": old["coverage_hardening_note"],
        "abstain_convention_note": old["abstain_convention_note"],
        "unit": old["unit"],
        "identity": old["identity"],
        "generated_by": dict(old["generated_by"],
                             instrument_note=args.instrument_note
                             or old["generated_by"]["instrument_note"]),
        "provenance": {
            "head_at_generation_short": args.head,
            "adoption_commit": args.adoption_commit
            or "see the adoption report (the revertible commit that lands this reference)",
            "corpus_git_hash": args.corpus_hash,
            "corpus_complete": True,
            "corpus_scores": summary["baroque"]["coverage"]["total_ours_files"],
            "wir_coverage": summary["baroque"]["coverage"]["wir_covered"],
            "wir_excluded_no_annotation": summary["baroque"]["coverage"]["no_wir"],
            "outgoing_reference_snapshot": args.snapshot,
            "user_ratified": args.ratified,
        },
        "reproduce_status": {
            "note": args.reproduce_note or old["reproduce_status"]["note"],
            "root": {p: preset_block(summary, p)["root_agree_pct"] for p in PRESETS},
            "rn": {p: preset_block(summary, p)["rn_agree_pct"] for p in PRESETS},
            "key_home": {p: preset_block(summary, p)["key_agree_pct"] for p in PRESETS},
            "key_local": {p: preset_block(summary, p)["key_agree_pct_local"] for p in PRESETS},
        },
        "presets": {p: preset_block(summary, p) for p in PRESETS},
    }

    # #12 (no information loss): every superseded-column record the outgoing manifest carried is
    # carried forward verbatim, and THIS event's outgoing columns are appended as one more. A
    # re-baseline must never silently drop the history of the columns it replaces.
    for k, v in old["reproduce_status"].items():
        if k.startswith("superseded_"):
            manifest["reproduce_status"][k] = v
    if args.supersedes_key:
        manifest["reproduce_status"][args.supersedes_key] = {
            "note": args.supersedes_note,
            "root": {p: old["presets"][p]["root_agree_pct"] for p in PRESETS},
            "rn": {p: old["presets"][p]["rn_agree_pct"] for p in PRESETS},
            "key_home": {p: old["presets"][p]["key_agree_pct"] for p in PRESETS},
            "key_local": {p: old["presets"][p]["key_agree_pct_local"] for p in PRESETS},
            "class_b_root_disagree_dur": {p: old["presets"][p]["class_b_root_disagree_dur"]
                                          for p in PRESETS},
            "variant_b_root_fail_runs": {p: old["presets"][p]["variant_b_root_fail_runs"]
                                         for p in PRESETS},
        }

    if args.dry_run:
        print(json.dumps(manifest["presets"], indent=1))
        return 0

    for p in PRESETS:
        for tpl in PER_PRESET_FILES:
            name = tpl.format(p=p)
            shutil.copyfile(args.candidate / name, REF_DIR / name)
    shutil.copyfile(args.candidate / "summary.json", REF_DIR / "summary.json")
    with open(REF_DIR / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
        f.write("\n")

    for p in PRESETS:
        b = manifest["presets"][p]
        print(f"  {p:<8} root {b['root_agree_pct']:.4f}  rn {b['rn_agree_pct']:.4f}  "
              f"key(home) {b['key_agree_pct']:.4f}  key(local) {b['key_agree_pct_local']:.4f}  "
              f"class-(b) dur {b['class_b_root_disagree_dur']}  runs {b['variant_b_root_fail_runs']}")
    print(f"re-stamped {REF_DIR}/ from {args.candidate}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

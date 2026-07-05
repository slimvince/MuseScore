#!/usr/bin/env python3
"""
stage5_fit_driver.py — the Stage-5 fitter harness (design §4.3 1a / §7).

Evaluate a candidate scoring-parameter VECTOR against the ratified objective, under the
ratified constraints, reusing the pinned instruments (run_bach_preset.py regen +
a8_rebaseline_measure.py objective + the batch-stop cases a8 already reproduces). NO FIT
is performed here: this dispatch builds + validates the harness (determinism, known-vector
fixture) and runs the Phase-1b sensitivity SCREEN through it. Nothing is adopted.

Objective (design §4.2): duration-weighted variant-(b) root agreement (root governs;
RN + key tracked beside). Per-evaluation constraints: no NEW class-(b) batch-stop case
(vs the CLAUDE.md 53/24/53 identity sets) + class-(b) root-disagree DURATION non-increase.

The driver REFUSES to propose/accept a vector touching a FROZEN row (P0 enforcement),
except under --perturb-frozen (the Phase-1b read-only frozen-row rider), which is labeled
as such in the ledger.

Determinism: two identical evaluations produce byte-identical ledger rows (the run_id +
timestamp live in separate columns and are excluded from the comparison).

Modes:
  split        Compute + write the proposed fitting/held-out split (stratified by mode).
  fixture      Known-vector fixture: current constants -> reproduce the ratified baselines.
  determinism  Run one evaluation twice; assert byte-identical ledger rows.
  screen       The Phase-1b one-at-a-time sensitivity screen.
  evaluate     A single ad-hoc evaluation of a name=value override (+ optional --disable-rule).
  fit          The Checkpoint-P1 1-D coordinate/pattern-search optimizer (one row, one carrier).
  audit        The §6-block per-rule dissolution audit: one eval per rule with that rule
               ALONE disabled, at current weights, on the fitting split (design D-7 / Phase 2.2a).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
import dcml_parser as dcml  # noqa: E402

WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"
BATCH_ANALYZE = _ROOT / "ninja_build_rel" / "batch_analyze.exe"

# ── Ledger location (design §7 as amended by O-8, 2026-07-05) ──────────────────────────
# The COMPACT PER-RUN ledgers (the fit ladder, the §6 dissolution audit) are committed
# artifacts under a NON-gitignored path. The shared full-row append-log + a8 per-cell
# enumerations stay regenerable scratch under the gitignored tools/reports/ (the A-8
# precedent for large enumerations).
FIT_LEDGER_DIR = _ROOT / "tools" / "fit_ledgers"      # committed compact per-run ledgers
SCRATCH_LEDGER_DIR = _ROOT / "tools" / "reports"      # gitignored append-log scratch

# ── The parameter registry: the REACHABLE override names (production fit surface) ──────
# Each row: family, frozen?, kind, and the baseline value (shared) OR per-preset values.
# 38 registered globals (G1/G6/G7/G10) + 21 ChordAnalyzerPreferences fields (G2-G5).
# The 19 DORMANT / null rows (G8/G9/G11/G12/G13) are NOT reachable by the mechanism and
# are recorded (dormant-only => Delta=0 by construction on the production carrier) in the
# Phase-1 report, not here. Canonical keys for the embedded-literal rows: complexityFactor
# floor -> kComplexityEvidenceFloor; augFactor halving -> kAugThinEvidenceFactor;
# wComplete lambda-local presence bar -> kWCompletePresenceThreshold.
SHARED = "shared"
PARAMS = {
    # G1 — chordanalyzer.cpp file constants + relocated locals/literals (all shared)
    "kContradictionPenalty":          dict(g="G1", fam="continuous", frozen=False, val=0.75),
    "kRootToneFactor":                dict(g="G1", fam="continuous", frozen=False, val=1.8),
    "kSecondToneFactor":              dict(g="G1", fam="continuous", frozen=False, val=1.2),
    "kOtherToneFactor":               dict(g="G1", fam="continuous", frozen=True,  val=1.0),
    "kTemplateToneWeightCap":         dict(g="G1", fam="continuous", frozen=False, val=3.0),
    "kExtraNoteWeightCap":            dict(g="G1", fam="continuous", frozen=False, val=2.0),
    "kExtensionFactor7th":            dict(g="G1", fam="continuous", frozen=False, val=0.45),
    "kExtensionFactorFlat13":         dict(g="G1", fam="continuous", frozen=False, val=0.20),
    "kExtensionFactorDefault":        dict(g="G1", fam="continuous", frozen=False, val=0.35),
    "kForeignPenalty":                dict(g="G1", fam="continuous", frozen=False, val=0.45),
    "kSus4FlatThirdFactor":           dict(g="G1", fam="continuous", frozen=False, val=0.10),
    "kSus4SharpThirdFactor":          dict(g="G1", fam="continuous", frozen=False, val=0.45),
    "kDim7CharacteristicBonus":       dict(g="G1", fam="continuous", frozen=True,  val=0.75),
    "kNonBassPenalty":                dict(g="G1", fam="continuous", frozen=False, val=0.35),
    "kSus4VariantMissing7th":         dict(g="G1", fam="continuous", frozen=False, val=0.70),
    "kSus4Maj7MissingP5":             dict(g="G1", fam="continuous", frozen=False, val=0.50),
    "kSus4MissingFourth":             dict(g="G1", fam="continuous", frozen=False, val=0.70),
    "kSus4StructuralFourthThreshold": dict(g="G1", fam="abstention",  frozen=True,  val=0.50),
    "kDom7FlatFiveTpcPenalty":        dict(g="G1", fam="continuous", frozen=False, val=0.55),
    "kDom7FlatFiveMissing7th":        dict(g="G1", fam="continuous", frozen=False, val=0.50),
    "kPowerChord3PcPenalty":          dict(g="G1", fam="continuous", frozen=False, val=0.30),
    "kBassSupportPresenceThreshold":  dict(g="G1", fam="abstention",  frozen=True,  val=0.05),
    "kSeventhThreshold":              dict(g="G1", fam="abstention",  frozen=True,  val=0.12),
    "kExtensionThreshold":            dict(g="G1", fam="abstention",  frozen=True,  val=0.20),
    "kWComplete":                     dict(g="G1", fam="continuous", frozen=False, val=0.50),
    "kWCompletePresenceThreshold":    dict(g="G1", fam="abstention",  frozen=True,  val=0.05),
    "kComplexityEvidenceFloor":       dict(g="G1", fam="continuous", frozen=False, val=0.5),
    "kAugThinEvidenceFactor":         dict(g="G1", fam="continuous", frozen=False, val=0.5),
    # G6 — harmonicfunctionlayer.h progression constants (shared)
    "kWSeq":                          dict(g="G6", fam="continuous", frozen=False, val=0.20),
    "kWDim":                          dict(g="G6", fam="continuous", frozen=False, val=0.15),
    "kWStepIn":                       dict(g="G6", fam="continuous", frozen=False, val=0.10),
    "kWStepOut":                      dict(g="G6", fam="continuous", frozen=False, val=0.10),
    "kStepBudget":                    dict(g="G6", fam="threshold",   frozen=True,  val=0.21),
    # G7 — postscoringgates.cpp gate margins (shared; §6-block dissolution targets)
    "kGateIMargin":                   dict(g="G7", fam="threshold",   frozen=False, val=0.45),
    "kGateKMargin":                   dict(g="G7", fam="threshold",   frozen=False, val=0.20),
    "kGateLMargin":                   dict(g="G7", fam="threshold",   frozen=False, val=0.35),
    "kHalfDimFirstInversionBonus":    dict(g="G7", fam="threshold",   frozen=False, val=0.55),
    # G10 — sectionanalyzer.h section-layer abstention bar (production)
    "kAnnotateKeyConfidenceThreshold": dict(g="G10", fam="abstention", frozen=False, val=0.8),
    # G2 — ChordAnalyzerPreferences root/bass/diatonic (shared)
    "bassNoteRootBonus":              dict(g="G2", fam="continuous", frozen=False, val=0.70),
    "bassRootThirdOnlyMultiplier":    dict(g="G2", fam="continuous", frozen=False, val=0.3),
    "bassRootAloneMultiplier":        dict(g="G2", fam="continuous", frozen=False, val=0.1),
    "diatonicRootBonus":              dict(g="G2", fam="continuous", frozen=False, val=0.30),
    "tpcConsistencyBonusPerTone":     dict(g="G2", fam="continuous", frozen=False, val=0.20),
    "rootContinuityBonus":            dict(g="G2", fam="continuous", frozen=False, val=0.40),
    "resolutionBonus":                dict(g="G2", fam="continuous", frozen=False, val=0.35),
    # G3 — inversion context bonuses (PRESET-VARYING; textural)
    "stepwiseBassInversionBonus":     dict(g="G3", fam="continuous", frozen=False,
                                           per_preset={"Baroque": 0.5, "Jazz": 0.20, "Default": 0.5}),
    "stepwiseBassLookaheadBonus":     dict(g="G3", fam="continuous", frozen=False,
                                           per_preset={"Baroque": 0.5, "Jazz": 0.20, "Default": 0.5}),
    "completeTriadInversionBonus":    dict(g="G3", fam="continuous", frozen=False,
                                           per_preset={"Baroque": 0.45, "Jazz": 0.20, "Default": 0.45}),
    "sameRootInversionBonus":         dict(g="G3", fam="continuous", frozen=False,
                                           per_preset={"Baroque": 0.4, "Jazz": 0.15, "Default": 0.4}),
    "maxTotalInversionContextBonus":  dict(g="G3", fam="continuous", frozen=True,  val=2.0),
    # G4 — gate/correction prefs
    "inversionSuspicionMargin":       dict(g="G4", fam="threshold",   frozen=False, val=0.70),
    "inversionBonusReduction":        dict(g="G4", fam="threshold",   frozen=False, val=0.0),
    "preferMinorOverMajorAdd6":       dict(g="G4", fam="threshold",   frozen=True,  kind="bool",
                                           per_preset={"Baroque": 1, "Jazz": 0, "Default": 0}),
    "minDistinctPcsForCandidate":     dict(g="G4", fam="abstention",  frozen=True,  kind="int", val=3),
    # G5 — segmentation / pedal / misc prefs
    "harmonicBoundaryJaccardThreshold": dict(g="G5", fam="continuous", frozen=False, val=0.6),
    "pedalTailWeightMultiplier":      dict(g="G5", fam="continuous", frozen=False, val=0.3),
    "bassPassingToneMinWeightFraction": dict(g="G5", fam="abstention", frozen=False, val=0.05),
    "extensionThreshold":             dict(g="G5", fam="abstention",  frozen=False,
                                           per_preset={"Baroque": 0.20, "Jazz": 0.12, "Default": 0.20}),
    "pedalConfidenceThreshold":       dict(g="G5", fam="abstention",  frozen=False, val=0.65),
}


# ── The §6-block post-scoring rules (design D-7; the dissolution-audit subject) ────────
# Canonical names must match paramoverride.h PostScoringRule / postScoringRuleNames().
# Execution order (docs/scoring_model.md §6): bias correction, FM2, then the lettered
# gates. Each disables via a `disable_rule <Name>` override line (measurement-only).
POST_SCORING_RULES = [
    "BiasCorrection", "FM2", "GateA", "GateE", "GateF",
    "GateGE", "GateGB", "GateGC", "GateGD",
    "GateH", "GateI", "GateK", "GateL", "GateJ",
]


def baseline_value(name, preset):
    p = PARAMS[name]
    if "per_preset" in p:
        return p["per_preset"][preset]
    return p["val"]


def fmt_val(name, v):
    if PARAMS[name].get("kind") == "bool":
        return "true" if v else "false"
    return repr(v)


def git_head():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True,
                       text=True, cwd=str(_ROOT))
    return r.stdout.strip() if r.returncode == 0 else "unknown"


def wir_covered_stems():
    """The WiR-annotated corpus stems (variant-(b) coverage) — deterministic, sorted."""
    stems = []
    for xml in sorted((_ROOT / "tools" / "corpus").glob("*.xml")):
        if dcml.find_wir_file(str(WIR_DIR), xml.stem):
            stems.append(xml.stem)
    return stems


def score_mode(stem):
    """major/minor from the music21 detectedKey (the split stratifier)."""
    m21 = _ROOT / "tools" / "corpus" / f"{stem}.music21.json"
    try:
        dk = (json.loads(m21.read_text()).get("detectedKey") or "").lower()
    except Exception:
        return "unknown"
    if "minor" in dk:
        return "minor"
    if "major" in dk:
        return "major"
    return "unknown"


# ── The split (design §4.3 1a) ────────────────────────────────────────────────────────
def compute_split(held_frac=0.2):
    """Deterministic, mode-stratified ~80/20 fitting/held-out split over the WiR-covered
    scores. Every 1/held_frac-th score (sorted, within each mode stratum) -> held-out, so
    both strata carry members in BOTH splits (§4.4a mode strata exist inside fitting)."""
    stems = wir_covered_stems()
    by_mode = {"major": [], "minor": [], "unknown": []}
    for s in stems:
        by_mode[score_mode(s)].append(s)
    step = max(2, round(1 / held_frac))
    registry = {}
    strata = {}
    for mode, members in by_mode.items():
        members = sorted(members)
        fit = held = 0
        for i, s in enumerate(members):
            split = "held_out" if (i % step == step - 1) else "fitting"
            registry[s] = {"mode": mode, "split": split}
            if split == "fitting":
                fit += 1
            else:
                held += 1
        if members:
            strata[mode] = {"fitting": fit, "held_out": held, "total": len(members)}
    return registry, strata


def split_scores_file(which, scratch):
    """Write the stem list for a named split to `scratch` and return its path.
    which='full' -> None (no restriction). 'fitting'/'held_out' read the ratified
    tools/stage5_split_registry.json. Used by fit (objective on the fitting split) and by
    evaluate --split (the decision-surface held-out/full scoring)."""
    if which == "full":
        return None
    split = json.loads((_ROOT / "tools" / "stage5_split_registry.json").read_text())
    stems = sorted(s for s, r in split["scores"].items() if r["split"] == which)
    p = Path(scratch) / f"{which}_split.txt"
    p.write_text("\n".join(stems) + "\n")
    return p


# ── Evaluation ────────────────────────────────────────────────────────────────────────
def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def write_override(perturb, preset, path, disable_rules=None):
    """Write a MINIMAL override file: only the perturbed params + any §6 rule-disables
    (all others stay at their byte-identical defaults/preset values, all rules enabled)."""
    lines = ["# stage5 fit driver override"]
    for name, v in perturb.items():
        lines.append(f"{name} {fmt_val(name, v)}")
    for rule in (disable_rules or []):
        lines.append(f"disable_rule {rule}")
    Path(path).write_text("\n".join(lines) + "\n")


def regen(preset, override_win_path, scratch_root):
    out = scratch_root / preset.lower()
    cmd = [sys.executable, str(_ROOT / "tools" / "run_bach_preset.py"),
           "--preset", preset,
           "--corpus-dir", str(_ROOT / "tools" / "corpus"),
           "--output-dir", str(out)]
    if override_win_path:
        cmd += ["--param-override", override_win_path]
    r = run(cmd)
    if r.returncode != 0:
        raise RuntimeError(f"regen failed ({preset}): {r.stderr[-400:]}")
    return out


def measure(preset, scratch_root, a8_out, scores_file=None):
    cmd = [sys.executable, str(_ROOT / "tools" / "a8_rebaseline_measure.py"),
           "--out-dir", str(a8_out), "--corpus-root", str(scratch_root),
           "--preset", preset.lower()]
    if scores_file:
        cmd += ["--scores", str(scores_file)]
    r = run(cmd)
    if r.returncode != 0:
        raise RuntimeError(f"a8 measure failed ({preset}): {r.stderr[-400:]}")
    summ = json.loads((Path(a8_out) / "summary.json").read_text())[preset.lower()]
    mapping = json.loads((Path(a8_out) / f"{preset.lower()}_mapping.json").read_text())
    agg = summ["agg"]
    root = 100 * agg["b_root_agree"] / (agg["b_root_agree"] + agg["b_root_dis"])
    rn = 100 * agg["b_rn_agree"] / (agg["b_rn_agree"] + agg["b_rn_dis"])
    kd = agg["b_key_agree"] + agg["b_key_dis"]
    key = 100 * agg["b_key_agree"] / kd if kd else 0.0
    cases = {f"{row['stem']}@{row['tick']}": row["cls"] for row in mapping["rows"]}
    return {
        "root_pct": root, "rn_pct": rn, "key_pct": key,
        "batch_gate": summ["batch_gate_count"],
        "cls_b_dur": agg["b_cls_b_dur"], "cls_a_dur": agg["b_cls_a_dur"],
        "cases": cases,
    }


def evaluate(perturb, preset, scratch_root, a8_out, baseline=None,
             perturb_frozen=False, scores_file=None, disable_rules=None):
    disable_rules = disable_rules or []
    # P0 enforcement: refuse a vector touching a frozen row unless the frozen rider is on.
    frozen_hit = [n for n in perturb if PARAMS[n]["frozen"]]
    if frozen_hit and not perturb_frozen:
        raise ValueError(f"refusing frozen row(s) {frozen_hit} (use --perturb-frozen for the "
                         f"Phase-1b read-only rider)")
    ov = scratch_root / f"override_{preset.lower()}.txt"
    write_override(perturb, preset, ov, disable_rules)
    ov_win = str(ov).replace("\\", "/")
    has_override = bool(perturb) or bool(disable_rules)
    regen(preset, ov_win if has_override else None, scratch_root)
    m = measure(preset, scratch_root, a8_out, scores_file)

    row = {
        "preset": preset,
        "vector": {n: v for n, v in perturb.items()},
        "disabled_rules": sorted(disable_rules),
        "families": sorted({PARAMS[n]["fam"] for n in perturb}) if perturb else [],
        "objective_root_pct": round(m["root_pct"], 4),
        "tracked": {"rn_pct": round(m["rn_pct"], 4), "key_pct": round(m["key_pct"], 4)},
        "batch_gate": m["batch_gate"],
        "cls_b_dur": m["cls_b_dur"], "cls_a_dur": m["cls_a_dur"],
        "perturb_frozen": bool(frozen_hit),
    }
    if baseline is not None:
        new_b = [c for c, cl in m["cases"].items()
                 if cl == "b" and c not in baseline["cases"]]
        row["constraints"] = {
            "new_class_b_batch_cases": sorted(new_b),
            "class_b_dur_delta": m["cls_b_dur"] - baseline["cls_b_dur"],
            "class_b_nonincrease_ok": m["cls_b_dur"] <= baseline["cls_b_dur"],
            "no_new_class_b_ok": len(new_b) == 0,
        }
        row["objective_delta"] = round(m["root_pct"] - baseline["root_pct"], 4)
    return row, m


def ledger_append(path, row, run_id, timestamp, instruments):
    # run_id + timestamp are SEPARATE columns, excluded from the determinism comparison.
    full = dict(row)
    full["_run_id"] = run_id
    full["_timestamp"] = timestamp
    full["_instruments"] = instruments
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(full, sort_keys=True) + "\n")


def stable_row(row):
    """The determinism-comparable projection (drops nothing — row has no time/id)."""
    return json.dumps(row, sort_keys=True)


# ── Perturbation steps (Phase-1b screen resolution; NOT a fit) ─────────────────────────
def perturbations_for(name, preset):
    """Return [(dir, value, step_label)] for the one-at-a-time screen. Step policy
    (design 4.3 1b): values in [0,1] -> +/-0.05 absolute; values >1 -> +/-10%; ints -> +/-1;
    bool -> flip. Non-negative doubles are floored at 0 (a clamped direction is recorded)."""
    p = PARAMS[name]
    base = baseline_value(name, preset)
    kind = p.get("kind")
    if kind == "bool":
        return [("flip", 1 - int(base), f"flip->{1-int(base)}")]
    if kind == "int":
        return [("down", int(base) - 1, "-1"), ("up", int(base) + 1, "+1")]
    step = round(0.10 * base, 6) if base > 1.0 else 0.05
    out = []
    lo = max(0.0, round(base - step, 6))
    if lo != base:
        out.append(("down", lo, f"-{step}"))
    else:
        out.append(("down", base, f"-{step}(clamped0)"))
    out.append(("up", round(base + step, 6), f"+{step}"))
    return out


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    sub.add_parser("split")
    fx = sub.add_parser("fixture"); fx.add_argument("--scratch", default="C:/tmp/s5_scratch/driver")
    dt = sub.add_parser("determinism"); dt.add_argument("--scratch", default="C:/tmp/s5_scratch/driver")
    sc = sub.add_parser("screen")
    sc.add_argument("--scratch", default="C:/tmp/s5_scratch/driver")
    sc.add_argument("--carrier", default="Baroque")
    sc.add_argument("--out", default=str(_ROOT / "tools" / "reports" / "stage5_screen.jsonl"))
    sc.add_argument("--resume", action="store_true")
    sc.add_argument("--only", default=None, help="comma-separated subset of param names")
    ev = sub.add_parser("evaluate")
    ev.add_argument("--preset", default="Baroque")
    ev.add_argument("--set", action="append", default=[], help="name=value (repeatable)")
    ev.add_argument("--scratch", default="C:/tmp/s5_scratch/driver")
    ev.add_argument("--perturb-frozen", action="store_true")
    ev.add_argument("--disable-rule", action="append", default=[],
                    help="§6 rule to disable for this eval (repeatable; measurement-only)")
    ev.add_argument("--split", default="full", choices=["full", "fitting", "held_out"],
                    help="objective/constraint denominator (default full = byte-compat)")
    # fit — the ratified coordinate/pattern-search optimizer (design §5 Optimizer block,
    # Checkpoint P1). 1-D over one row on one carrier; objective on the fitting split.
    ft = sub.add_parser("fit")
    ft.add_argument("--param", required=True)
    ft.add_argument("--carrier", default="Baroque")
    ft.add_argument("--lo", type=float, default=0.0)
    ft.add_argument("--hi", type=float, default=1.2)
    ft.add_argument("--coarse-steps", type=int, default=9)
    ft.add_argument("--refine-rounds", type=int, default=2)
    ft.add_argument("--split", default="fitting", choices=["fitting", "held_out", "full"])
    ft.add_argument("--scratch", default="C:/tmp/s5_scratch/fit")
    ft.add_argument("--out", default=str(FIT_LEDGER_DIR / "stage5_fit_<param>.jsonl"))
    # audit — the §6-block per-rule dissolution audit (design D-7 / Phase 2.2a Task 3).
    # One evaluation per rule with that rule ALONE disabled, at current weights, on the
    # fitting split; objective delta + batch subset-diff + class split, ledgered.
    au = sub.add_parser("audit")
    au.add_argument("--carrier", default="Baroque")
    au.add_argument("--split", default="fitting", choices=["fitting", "held_out", "full"])
    au.add_argument("--scratch", default="C:/tmp/s5_scratch/audit")
    au.add_argument("--only", default=None, help="comma-separated subset of rule names")
    au.add_argument("--resume", action="store_true")
    au.add_argument("--out", default=str(FIT_LEDGER_DIR / "stage5_rule_dissolution_audit.jsonl"))
    args = ap.parse_args()

    ledger = SCRATCH_LEDGER_DIR / "stage5_fit_ledger.jsonl"   # shared full-row append-log (scratch)
    ledger.parent.mkdir(parents=True, exist_ok=True)
    instruments = {"head": git_head(),
                   "objective": "a8_rebaseline_measure.py variant-(b) root-agree"}
    STAMP = "unstamped"   # constant so the double-run ledger check is byte-identical

    if args.mode == "split":
        registry, strata = compute_split()
        outp = _ROOT / "tools" / "stage5_split_registry.json"
        outp.write_text(json.dumps({"strata": strata, "scores": registry},
                                   indent=1, sort_keys=True), encoding="utf-8")
        print(f"split -> {outp}")
        for mode, s in strata.items():
            print(f"  {mode}: fitting={s['fitting']} held_out={s['held_out']} total={s['total']}")
        tf = sum(s["fitting"] for s in strata.values())
        th = sum(s["held_out"] for s in strata.values())
        print(f"  TOTAL: fitting={tf} held_out={th} "
              f"({100*tf/(tf+th):.1f}% / {100*th/(tf+th):.1f}%)")
        return

    if args.mode == "evaluate":
        scratch = Path(args.scratch); scratch.mkdir(parents=True, exist_ok=True)
        a8_out = scratch / "a8"
        scores_file = split_scores_file(args.split, scratch)
        perturb = {}
        for kv in args.set:
            k, v = kv.split("=", 1)
            perturb[k] = (v == "true") if PARAMS[k].get("kind") == "bool" else float(v)
        _, base_m = evaluate({}, args.preset, scratch, a8_out, scores_file=scores_file)
        row, _ = evaluate(perturb, args.preset, scratch, a8_out, baseline=base_m,
                          perturb_frozen=args.perturb_frozen, scores_file=scores_file,
                          disable_rules=args.disable_rule)
        row["split"] = args.split
        row["baseline_root_pct"] = round(base_m["root_pct"], 4)
        ledger_append(ledger, row, f"adhoc_{args.split}", STAMP, instruments)
        print(json.dumps(row, indent=1))
        return

    if args.mode == "fit":
        scratch = Path(args.scratch); scratch.mkdir(parents=True, exist_ok=True)
        a8_out = scratch / "a8"
        carrier, name = args.carrier, args.param
        p = PARAMS[name]
        scores_file = split_scores_file(args.split, scratch)
        outp = Path(args.out.replace("<param>", name)); outp.parent.mkdir(parents=True, exist_ok=True)
        cur = baseline_value(name, carrier)
        _, base_m = evaluate({}, carrier, scratch, a8_out, scores_file=scores_file)
        base_root = round(base_m["root_pct"], 4)
        results = {}

        def eval_at(raw):
            v = round(raw, 6)
            if v in results:
                return results[v]
            row, _m = evaluate({name: v}, carrier, scratch, a8_out, baseline=base_m,
                               perturb_frozen=p["frozen"], scores_file=scores_file)
            c = row["constraints"]
            feasible = c["no_new_class_b_ok"] and c["class_b_nonincrease_ok"]
            rec = {"param": name, "carrier": carrier, "split": args.split, "value": v,
                   "root_pct": row["objective_root_pct"], "objective_delta": row["objective_delta"],
                   "rn_pct": row["tracked"]["rn_pct"], "key_pct": row["tracked"]["key_pct"],
                   "batch_gate": row["batch_gate"],
                   "no_new_class_b_ok": c["no_new_class_b_ok"],
                   "class_b_nonincrease_ok": c["class_b_nonincrease_ok"],
                   "new_class_b_batch_cases": c["new_class_b_batch_cases"],
                   "class_b_dur_delta": c["class_b_dur_delta"], "feasible": feasible}
            results[v] = rec
            ledger_append(ledger, row, f"fit_{name}_{v}", STAMP, instruments)
            with open(outp, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, sort_keys=True) + "\n")
            print(f"  {name}={v:<9g} root={rec['root_pct']:.4f} d={rec['objective_delta']:+.4f} "
                  f"batch={rec['batch_gate']} newB={len(rec['new_class_b_batch_cases'])} "
                  f"clsBdur_d={rec['class_b_dur_delta']:+g} feas={feasible}")
            return rec

        lo, hi, n = args.lo, args.hi, args.coarse_steps
        coarse = [round(lo + i * (hi - lo) / (n - 1), 6) for i in range(n)]
        print(f"FIT {name} carrier={carrier} split={args.split} "
              f"baseline_root={base_root:.4f} (current value {cur})")
        print(f"  ladder(coarse) lo={lo} hi={hi} steps={n} -> {coarse}")
        for v in coarse:
            eval_at(v)

        def best_feasible():
            feas = [r for r in results.values() if r["feasible"]]
            if not feas:
                return None
            # maximize root; tie-break toward the current value (minimal conservative change)
            return max(feas, key=lambda r: (r["root_pct"], -abs(r["value"] - cur)))

        step = (hi - lo) / (n - 1)
        best = best_feasible()
        for _rnd in range(args.refine_rounds):
            step /= 2
            if best is None:
                break
            for cand in (round(best["value"] - step, 6), round(best["value"] + step, 6)):
                if lo <= cand <= hi:
                    eval_at(cand)
            best = best_feasible()

        best_obj = max(results.values(), key=lambda r: (r["root_pct"], -abs(r["value"] - cur)))
        print(f"\nFIT SUMMARY {name}  baseline_root={base_root:.4f} @ value={cur}")
        if best:
            print(f"  CANDIDATE (best feasible): value={best['value']} root={best['root_pct']:.4f} "
                  f"delta={best['objective_delta']:+.4f} batch={best['batch_gate']}")
        print(f"  unconstrained-max: value={best_obj['value']} root={best_obj['root_pct']:.4f} "
              f"feasible={best_obj['feasible']}")
        if best is None:
            result = "UNFITTABLE-UNDER-CONSTRAINT (no feasible point; objective-max infeasible)"
        elif best["objective_delta"] <= 1e-9:
            result = ("ALREADY-OPTIMAL-AT-THIS-RESOLUTION (best feasible = baseline; "
                      f"candidate value {best['value']})")
        elif not best_obj["feasible"]:
            result = ("FEASIBLE-IMPROVEMENT (constraint-bounded: the unconstrained-max value "
                      f"{best_obj['value']} is INFEASIBLE; candidate is the best feasible)")
        else:
            result = "FEASIBLE-IMPROVEMENT (unconstrained-max is itself feasible)"
        print(f"  RESULT: {result}")
        return

    if args.mode == "audit":
        scratch = Path(args.scratch); scratch.mkdir(parents=True, exist_ok=True)
        a8_out = scratch / "a8"
        carrier = args.carrier
        scores_file = split_scores_file(args.split, scratch)
        outp = Path(args.out); outp.parent.mkdir(parents=True, exist_ok=True)
        rules = POST_SCORING_RULES if not args.only else args.only.split(",")
        done = set()
        if args.resume and outp.exists():
            for ln in outp.read_text().splitlines():
                try:
                    d = json.loads(ln)
                    if d.get("record") == "rule":
                        done.add(d["rule"])
                except Exception:
                    pass
        elif outp.exists():
            outp.unlink()   # fresh compact per-run ledger (truncate) unless resuming

        _, base_m = evaluate({}, carrier, scratch, a8_out, scores_file=scores_file)
        base_root = round(base_m["root_pct"], 4)
        print(f"AUDIT carrier={carrier} split={args.split} baseline_root={base_root:.4f} "
              f"batch={base_m['batch_gate']} rules={len(rules)} (resume: {len(done)} done)")
        if ("__baseline__" not in done) and not (args.resume and outp.exists()):
            with open(outp, "a", encoding="utf-8") as f:
                f.write(json.dumps({"record": "baseline", "carrier": carrier,
                                    "split": args.split, "root_pct": base_root,
                                    "batch_gate": base_m["batch_gate"],
                                    "cls_b_dur": base_m["cls_b_dur"],
                                    "cls_a_dur": base_m["cls_a_dur"]}, sort_keys=True) + "\n")
        for rule in rules:
            if rule in done:
                continue
            row, m = evaluate({}, carrier, scratch, a8_out, baseline=base_m,
                              scores_file=scores_file, disable_rules=[rule])
            added = sorted(c for c in m["cases"] if c not in base_m["cases"])
            removed = sorted(c for c in base_m["cases"] if c not in m["cases"])
            changed = sorted(c for c in m["cases"]
                             if c in base_m["cases"] and m["cases"][c] != base_m["cases"][c])
            rec = {"record": "rule", "rule": rule, "carrier": carrier, "split": args.split,
                   "root_pct": row["objective_root_pct"],
                   "objective_delta": row["objective_delta"],
                   "rn_pct": row["tracked"]["rn_pct"], "key_pct": row["tracked"]["key_pct"],
                   "batch_gate": row["batch_gate"],
                   "batch_added": added, "batch_removed": removed,
                   "batch_class_changed": changed,
                   "class_b_dur_delta": m["cls_b_dur"] - base_m["cls_b_dur"],
                   "class_a_dur_delta": m["cls_a_dur"] - base_m["cls_a_dur"],
                   "new_class_b_batch_cases": row["constraints"]["new_class_b_batch_cases"]}
            ledger_append(ledger, row, f"audit_{rule}", STAMP, instruments)
            with open(outp, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, sort_keys=True) + "\n")
            print(f"  {rule:<16} root={rec['root_pct']:.4f} d={rec['objective_delta']:+.4f} "
                  f"batch={rec['batch_gate']} +{len(added)}/-{len(removed)}/~{len(changed)} "
                  f"newB={len(rec['new_class_b_batch_cases'])} "
                  f"clsBdur_d={rec['class_b_dur_delta']:+g} clsAdur_d={rec['class_a_dur_delta']:+g}")
        print(f"AUDIT done -> {outp}")
        return

    if args.mode == "fixture":
        scratch = Path(args.scratch); scratch.mkdir(parents=True, exist_ok=True)
        a8_out = scratch / "a8"
        RATIFIED = {"Baroque": 63.32, "Jazz": 62.37, "Default": 63.22}
        split = json.loads((_ROOT / "tools" / "stage5_split_registry.json").read_text())
        fit_stems = sorted(s for s, r in split["scores"].items() if r["split"] == "fitting")
        scores_file = scratch / "fitting_split.txt"
        scores_file.write_text("\n".join(fit_stems) + "\n")
        print("KNOWN-VECTOR FIXTURE (identity override; full coverage) — reproduce baselines:")
        ok = True
        for preset in ("Baroque", "Jazz", "Default"):
            ident = {n: baseline_value(n, preset) for n in PARAMS}
            row, m = evaluate(ident, preset, scratch, a8_out, perturb_frozen=True)
            _, msplit = evaluate(ident, preset, scratch, a8_out, perturb_frozen=True,
                                 scores_file=scores_file)
            match = abs(m["root_pct"] - RATIFIED[preset]) < 0.005
            ok = ok and match
            print(f"  {preset}: full-root={m['root_pct']:.2f}% (ratified {RATIFIED[preset]}) "
                  f"{'MATCH' if match else 'MISMATCH'}  batch={m['batch_gate']}  "
                  f"fitting-split-root={msplit['root_pct']:.2f}%")
            ledger_append(ledger, row, f"fixture_{preset}", STAMP, instruments)
        print("FIXTURE:", "PASS" if ok else "FAIL")
        return

    if args.mode == "determinism":
        scratch = Path(args.scratch); scratch.mkdir(parents=True, exist_ok=True)
        a8_out = scratch / "a8"
        _, base_m = evaluate({}, "Baroque", scratch, a8_out)
        r1, _ = evaluate({"kContradictionPenalty": 0.9}, "Baroque", scratch, a8_out, baseline=base_m)
        r2, _ = evaluate({"kContradictionPenalty": 0.9}, "Baroque", scratch, a8_out, baseline=base_m)
        same = stable_row(r1) == stable_row(r2)
        print("DETERMINISM (identical eval x2, ledger row ex-timestamp/run_id):",
              "BYTE-IDENTICAL" if same else "DIVERGED")
        if not same:
            print("r1:", stable_row(r1)); print("r2:", stable_row(r2))
        return

    if args.mode == "screen":
        scratch = Path(args.scratch); scratch.mkdir(parents=True, exist_ok=True)
        a8_out = scratch / "a8"
        carrier = args.carrier
        outp = Path(args.out); outp.parent.mkdir(parents=True, exist_ok=True)
        done = set()
        if args.resume and outp.exists():
            for ln in outp.read_text().splitlines():
                try:
                    d = json.loads(ln); done.add((d["param"], d["dir"], d["preset"]))
                except Exception:
                    pass
        names = list(PARAMS) if not args.only else args.only.split(",")
        print(f"SCREEN carrier={carrier} rows={len(names)} (resume: {len(done)} done)")
        _, base_m = evaluate({}, carrier, scratch, a8_out)
        base_root = round(base_m["root_pct"], 4)
        if ("__baseline__", "-", carrier) not in done:
            with open(outp, "a", encoding="utf-8") as f:
                f.write(json.dumps({"param": "__baseline__", "dir": "-", "preset": carrier,
                                    "root_pct": base_root, "batch_gate": base_m["batch_gate"],
                                    "cls_b_dur": base_m["cls_b_dur"]}, sort_keys=True) + "\n")
        for name in names:
            p = PARAMS[name]
            for dirn, value, steplab in perturbations_for(name, carrier):
                if (name, dirn, carrier) in done:
                    continue
                if "clamped0" in steplab:
                    rec = {"param": name, "dir": dirn, "preset": carrier, "group": p["g"],
                           "family": p["fam"], "frozen": p["frozen"], "step": steplab,
                           "value": value, "objective_delta": 0.0, "clamped": True,
                           "root_pct": base_root, "batch_gate": base_m["batch_gate"],
                           "no_new_class_b_ok": True, "class_b_nonincrease_ok": True,
                           "new_class_b_batch_cases": [], "class_b_dur_delta": 0}
                else:
                    row, _ = evaluate({name: value}, carrier, scratch, a8_out, baseline=base_m,
                                      perturb_frozen=p["frozen"])
                    c = row["constraints"]
                    rec = {"param": name, "dir": dirn, "preset": carrier, "group": p["g"],
                           "family": p["fam"], "frozen": p["frozen"], "step": steplab, "value": value,
                           "objective_delta": row["objective_delta"], "clamped": False,
                           "root_pct": row["objective_root_pct"], "batch_gate": row["batch_gate"],
                           "rn_pct": row["tracked"]["rn_pct"], "key_pct": row["tracked"]["key_pct"],
                           "no_new_class_b_ok": c["no_new_class_b_ok"],
                           "class_b_nonincrease_ok": c["class_b_nonincrease_ok"],
                           "new_class_b_batch_cases": c["new_class_b_batch_cases"],
                           "class_b_dur_delta": c["class_b_dur_delta"]}
                    ledger_append(ledger, row, f"screen_{name}_{dirn}", STAMP, instruments)
                with open(outp, "a", encoding="utf-8") as f:
                    f.write(json.dumps(rec, sort_keys=True) + "\n")
                print(f"  {name:<34} {dirn:<4} {steplab:<16} d_root={rec['objective_delta']:+.4f} "
                      f"batch={rec['batch_gate']} newB={len(rec['new_class_b_batch_cases'])}")
        print(f"SCREEN done -> {outp}")
        return


if __name__ == "__main__":
    main()

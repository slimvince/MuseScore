#!/usr/bin/env python3
"""hardening_battery.py — the OI-145 wave-1 measurement-chain establishment battery.

READ-ONLY / VERIFICATION-ONLY. The single instrument that proves a measurement-chain
hardening fix (OI-140/OI-124/OI-129/OI-132/OI-33 + the wave-1 remainder) moved NO grading
digit. It orchestrates the committed instruments exactly as they are used in production —
it defines no metric of its own — and reports each gate PASS/FAIL against the committed
reference artifacts. Run it FIRST to record the clean starting state, then after EVERY fix;
any deviation is the discovery protocol (its own register row + STOP-and-report).

Gates (all scratch; no committed file is written):
  0. register  [HARD, <1s]  register_lint: no OPEN_ITEMS.md row ID collides (OI-153). Cheap,
                            so it runs at every fold — which is the whole point of it.
  1. a8_diff   [HARD, ~6s]  a8_rebaseline_measure -> scratch, then robust_stop_diff vs the
                            committed tools/robust_stop reference. PASS iff diff exits 0
                            (class-(b) duration non-increase, all presets) AND every preset's
                            run-level set-diff is (+0 / -0) AND WiR coverage is unchanged.
  2. calib     [HARD, ~30s] calibration_fit -> scratch; PASS iff all four committed
                            tools/calibration_maps/*.json reproduce byte-identical.
  3. validate  [HARD, <1s]  characterise_bir_false.validate_corpus_dir on all three presets.
  4. fixture   [--fixture]  stage5_fit_driver fixture (full corpus regen x3 + a8); reports the
                            per-preset variant-(b) root-% and whether it MATCHES the value
                            recorded at baseline time (--fixture-expect). EXPENSIVE (~minutes).
  5. regen     [--corpus-regen] run_bach_preset -> scratch for all three presets; PASS iff
                            every {stem}.ours.json sha256 equals the committed tools/corpus
                            copy. The batch_analyze.cpp byte-identity proof. EXPENSIVE.

Exit code 0 iff every RUN hard gate passes. Gates 4/5 run only when their flag is given.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent.parent          # repo root
_TOOLS = _ROOT / "tools"
sys.path.insert(0, str(_TOOLS))

import characterise_bir_false as cbf   # noqa: E402  (validate_corpus_dir)

sys.path.insert(0, str(Path(__file__).resolve().parent))
import register_lint                   # noqa: E402  (the OI-153 ID-collision check)

PRESETS = ["baroque", "jazz", "default"]
PY = sys.executable
REF_DIR = _TOOLS / "robust_stop"
CORPUS_ROOT = _TOOLS / "corpus"
CALIB_DIR = _TOOLS / "calibration_maps"
CALIB_MAPS = [
    "stage5_classP_l3_key_margin_baroque.json",
    "stage5_classP_l3_key_margin_default.json",
    "stage5_classP_l4_chord_composite_baroque.json",
    "stage5_classP_l4_chord_composite_default.json",
]


def _run(cmd, log_path):
    """Run a subprocess, tee stdout+stderr to log_path, return (returncode, text)."""
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", cwd=str(_ROOT))
    text = (r.stdout or "") + (r.stderr or "")
    Path(log_path).write_text(text, encoding="utf-8")
    return r.returncode, text


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ── Gate 0: register ID-collision lint (OI-153) ───────────────────────────────────────
def gate_register() -> dict:
    ids = register_lint.collect_row_ids(_ROOT / "OPEN_ITEMS.md")
    collisions = register_lint.find_collisions(ids)
    detail = f"{len(ids)} row IDs, no collision"
    if collisions:
        detail = "; ".join(f"{oi} heads {len(lines)} rows (lines {lines})"
                           for oi, lines in sorted(collisions.items()))
    return {"gate": "register", "pass": not collisions, "detail": detail}


# ── Gate 1: a8 measure + robust_stop_diff vs the committed reference ──────────────────
def gate_a8_diff(scratch: Path) -> dict:
    a8_out = scratch / "a8"
    a8_out.mkdir(parents=True, exist_ok=True)
    rc_a8, _ = _run([PY, _TOOLS / "a8_rebaseline_measure.py", "--out-dir", a8_out],
                    scratch / "a8.log")
    if rc_a8 != 0:
        return {"gate": "a8_diff", "pass": False, "detail": "a8_rebaseline_measure FAILED"}
    rc_diff, text = _run([PY, _TOOLS / "robust_stop_diff.py",
                          "--candidate", a8_out, "--reference", REF_DIR],
                         scratch / "diff.log")
    # every preset must show (+0 / -0); parse the run lines
    run_lines = re.findall(r"runs: reference=(\d+) candidate=(\d+)\s+\(\+(\d+) / -(\d+)\)", text)
    all_zero = bool(run_lines) and all(a == "0" and b == "0" for (_, _, a, b) in run_lines)
    overall_pass = ("OVERALL: PASS" in text) and rc_diff == 0
    # coverage reconcile line (added by OI-140): "COVERAGE ... OK/SHRUNK"
    cov_ok = "COVERAGE SHRUNK" not in text
    ok = overall_pass and all_zero and cov_ok and len(run_lines) == 3
    return {"gate": "a8_diff", "pass": ok,
            "detail": f"diff_exit={rc_diff} overall_pass={overall_pass} "
                      f"run_diffs={[(a, b) for (_, _, a, b) in run_lines]} coverage_ok={cov_ok}"}


# ── Gate 2: calibration_fit byte-identity vs the committed maps ───────────────────────
def gate_calib(scratch: Path) -> dict:
    out = scratch / "calib"
    out.mkdir(parents=True, exist_ok=True)
    rc, _ = _run([PY, _TOOLS / "calibration_fit.py", "--out-dir", out], scratch / "calib.log")
    if rc != 0:
        return {"gate": "calib", "pass": False, "detail": "calibration_fit FAILED"}
    diffs = []
    for name in CALIB_MAPS:
        committed = CALIB_DIR / name
        produced = out / name
        if not produced.exists() or _sha256(committed) != _sha256(produced):
            diffs.append(name)
    return {"gate": "calib", "pass": not diffs,
            "detail": f"{len(CALIB_MAPS) - len(diffs)}/{len(CALIB_MAPS)} byte-identical"
                      + (f"; DIFFER: {diffs}" if diffs else "")}


# ── Gate 3: validate_corpus_dir on all three presets ─────────────────────────────────
def gate_validate() -> dict:
    bad = []
    for p in PRESETS:
        try:
            cbf.validate_corpus_dir(CORPUS_ROOT / p)
        except Exception as exc:
            bad.append(f"{p}: {exc}")
    return {"gate": "validate", "pass": not bad,
            "detail": "3/3 OK" if not bad else "; ".join(bad)}


# ── Gate 4 (opt): stage5 fixture reproduce ───────────────────────────────────────────
def gate_fixture(scratch: Path, expect: dict | None) -> dict:
    rc, text = _run([PY, _TOOLS / "stage5_fit_driver.py", "fixture",
                     "--scratch", scratch / "fixture"], scratch / "fixture.log")
    # lines: "  Baroque: full-root=NN.NN% (ratified R) MATCH  batch=B  fitting-split-root=..."
    got = {}
    for preset, root, ratified, verdict, batch in re.findall(
            r"(\w+): full-root=([\d.]+)% \(ratified ([\d.]+)\) (MATCH|MISMATCH)\s+batch=(\d+)", text):
        got[preset] = {"root": float(root), "ratified": float(ratified),
                       "self_verdict": verdict, "batch": int(batch)}
    stable = True
    detail_bits = []
    for preset, v in sorted(got.items()):
        note = v["self_verdict"]
        if expect is not None and preset in expect:
            moved = abs(v["root"] - expect[preset]) >= 0.005
            if moved:
                stable = False
            note += f" baseline={expect[preset]:.2f}{' MOVED' if moved else ' stable'}"
        detail_bits.append(f"{preset}: root={v['root']:.2f} batch={v['batch']} [{note}]")
    ok = (rc == 0) and bool(got) and stable
    return {"gate": "fixture", "pass": ok, "detail": " | ".join(detail_bits),
            "roots": {p: v["root"] for p, v in got.items()}}


# ── Gate 5 (opt): scratch corpus regen sha256 vs committed corpus ─────────────────────
def gate_corpus_regen(scratch: Path) -> dict:
    regen_root = scratch / "regen"
    mismatched = {}
    for p in PRESETS:
        preset_name = {"baroque": "Baroque", "jazz": "Jazz", "default": "Default"}[p]
        out = regen_root / p
        rc, _ = _run([PY, _TOOLS / "run_bach_preset.py", "--preset", preset_name,
                      "--corpus-dir", CORPUS_ROOT, "--output-dir", out], scratch / f"regen_{p}.log")
        diffs = []
        for committed in sorted((CORPUS_ROOT / p).glob("*.ours.json")):
            produced = out / committed.name
            if not produced.exists() or _sha256(committed) != _sha256(produced):
                diffs.append(committed.name)
        mismatched[p] = diffs
    total_bad = sum(len(v) for v in mismatched.values())
    return {"gate": "corpus_regen", "pass": total_bad == 0,
            "detail": "; ".join(f"{p}: {len(v)} differ" for p, v in mismatched.items())}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scratch", default="C:/tmp/hardening_battery/run",
                    help="scratch dir for all intermediate outputs")
    ap.add_argument("--fixture", action="store_true",
                    help="also run the expensive stage5 fixture reproduce (~minutes)")
    ap.add_argument("--fixture-expect", default=None,
                    help="JSON {preset: root_pct} baseline the fixture must reproduce")
    ap.add_argument("--corpus-regen", action="store_true",
                    help="also run the expensive full corpus regen sha256 check (batch_analyze.cpp touch)")
    ap.add_argument("--json-out", default=None, help="write the gate results JSON here")
    args = ap.parse_args()

    scratch = Path(args.scratch)
    scratch.mkdir(parents=True, exist_ok=True)

    results = [gate_register(), gate_a8_diff(scratch), gate_calib(scratch), gate_validate()]
    if args.fixture:
        expect = json.loads(Path(args.fixture_expect).read_text()) if args.fixture_expect else None
        results.append(gate_fixture(scratch, expect))
    if args.corpus_regen:
        results.append(gate_corpus_regen(scratch))

    print("=" * 78)
    print("OI-145 WAVE-1 ESTABLISHMENT BATTERY")
    print("=" * 78)
    all_pass = True
    for r in results:
        status = "PASS" if r["pass"] else "FAIL"
        all_pass = all_pass and r["pass"]
        print(f"  [{status}] {r['gate']:<14} {r['detail']}")
    print("-" * 78)
    print(f"BATTERY: {'PASS' if all_pass else 'FAIL'}")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(results, indent=1), encoding="utf-8")

    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Repository-side re-run of the 2026-08-02 transposition-equivariance probe (OI-243 / OI-244).

WHY THIS EXISTS. `OPEN_ITEMS.md` OI-243 records the original probe as agent-run with an
agent-written script, established only by its own self-check and its six bit-exact conditions, and
states that the row's FIRST action is a repository-side re-run before the finding carries any load
(#19). Two family rows (OI-243, OI-244) cannot bear weight until this runs.

WHY IT IS A DRIVER AND NOT A SECOND PROBE (#6, one path per concern). The committed apparatus
`tools/joint_estimator/transposition_probe_2026_08_02/run_probe.py` holds the whole measurement:
the transposition convention, the establishment phase, the per-condition comparison and the
per-violation diagnosis. Re-implementing any of it would produce a second answer to one question
and would measure this script rather than that one. What the committed script cannot do is run
here: its REPO and OUT constants are absolute sandbox paths that exist on no machine in this
repository. So this driver imports it AS IS, re-points exactly those two constants, and drives the
two phases. Nothing else about the apparatus is touched, and the driver asserts as much before it
runs (see `_assert_apparatus_untouched`).

READ-ONLY on the repository. Everything written goes into this script's own directory.

Usage:
  python tools/joint_estimator/transposition_probe_rerun_2026_08_03/rerun_repo_side.py
"""
from __future__ import annotations

import importlib.util
import json
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True                       # never write .pyc into the repository

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent                     # tools/joint_estimator/<dir>/  ->  repo root
APPARATUS = REPO / "tools" / "joint_estimator" / "transposition_probe_2026_08_02" / "run_probe.py"

# The committed apparatus imports `probe_decoder` and `gen_label_tables` at module import time via
# a sandbox path that does not exist here; putting the real directories on sys.path FIRST makes
# those imports resolve without editing the committed file.
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(REPO / "tools" / "joint_estimator"))


def _load_apparatus():
    spec = importlib.util.spec_from_file_location("committed_run_probe", APPARATUS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _assert_apparatus_untouched(rp):
    """Everything this driver changes, named. Anything else differing is a STOP: it would mean the
    re-run measured a different apparatus from the committed one."""
    changed = {"REPO": (str(rp.REPO), str(REPO)), "OUT": (str(rp.OUT), str(HERE))}
    # The measurement constants must be the committed ones, byte for byte.
    expected = {"SEG_CAP": 4, "SHIFTS": [2, -3, 6], "K_TO_F": {2: 2, -3: 3, 6: 6}}
    for name, want in expected.items():
        got = getattr(rp, name)
        if got != want:
            raise SystemExit(f"STOP: apparatus constant {name} is {got!r}, expected {want!r}")
    return changed


def main():
    if not APPARATUS.exists():
        raise SystemExit(f"STOP: the committed apparatus is not at {APPARATUS}")
    rp = _load_apparatus()
    changed = _assert_apparatus_untouched(rp)

    # Re-point the two path constants. They are read at CALL time inside load_apparatus() and
    # _load_state()/_save_state(), so rebinding them here is sufficient and touches nothing else.
    rp.REPO = REPO
    rp.OUT = HERE
    # The committed script exits after BUDGET seconds so a sandbox call cap could not kill it
    # mid-piece; the state is resumable, so raising the budget is equivalent to invoking it
    # repeatedly and changes no measured value. Recorded rather than done silently.
    committed_budget = rp.BUDGET
    rp.BUDGET = 10 ** 9

    run = {
        "purpose": (
            "Repository-side re-run of the transposition-equivariance probe, the first action "
            "OI-243 owes before its finding carries load (#19)."
        ),
        "apparatus": str(APPARATUS.relative_to(REPO)).replace("\\", "/"),
        "driver": str(Path(__file__).resolve().relative_to(REPO)).replace("\\", "/"),
        "what_the_driver_changed": {
            "REPO": {"committed": changed["REPO"][0], "here": changed["REPO"][1],
                     "why": "an absolute sandbox path that exists on no machine in this repository"},
            "OUT": {"committed": changed["OUT"][0], "here": changed["OUT"][1],
                    "why": "artifacts go to this run's own directory; the repository is read-only"},
            "BUDGET": {"committed": committed_budget, "here": "effectively unlimited",
                       "why": ("the committed value is a sandbox call cap with resumable state on "
                               "disk; raising it is equivalent to invoking the script repeatedly "
                               "and changes no measured value")},
            "nothing_else": ("SEG_CAP, SHIFTS and K_TO_F are asserted equal to the committed "
                             "values before the run; every function is the committed one"),
        },
    }

    t0 = time.perf_counter()
    print("PHASE 1 - establish (the committed decode parity reference must reproduce EXACTLY)")
    rc_est = rp.phase_establish()
    run["establish_rc"] = rc_est
    run["establish_seconds"] = round(time.perf_counter() - t0, 1)
    if rc_est != 0:
        run["stop"] = ("ESTABLISHMENT FAILED - the apparatus is NOT established here and the "
                       "finding cannot be re-measured with it (#19). Nothing further was run.")
        (HERE / "rerun_record.json").write_text(json.dumps(run, indent=1, ensure_ascii=False),
                                               encoding="utf-8")
        print(run["stop"])
        return 1

    t1 = time.perf_counter()
    print("PHASE 2 - transpose (36 conditions: 12 pieces x {+2, -3, +6})")
    rc_tr = rp.phase_transpose()
    run["transpose_rc"] = rc_tr
    run["transpose_seconds"] = round(time.perf_counter() - t1, 1)
    (HERE / "rerun_record.json").write_text(json.dumps(run, indent=1, ensure_ascii=False),
                                            encoding="utf-8")
    return 0 if rc_tr == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

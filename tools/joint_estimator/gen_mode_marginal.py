#!/usr/bin/env python3
"""gen_mode_marginal.py — dump the per-mode chord-class MARGINAL as a committed runtime artifact.

READ-ONLY / instrument-layer. No src/ change, no build, no gate, no metric consulted. This exists so
the C++ joint-estimator module (the OI-180 dual path) can LOAD the marginal from a committed artifact
on its sanctioned input surface, rather than re-deriving it — which would require porting the fit-time
When-in-Rome label pipeline (dcml.load_wir_regions + crn._dcml_key_tonic + normalize.normalize_label),
the very pipeline the build dispatch keeps in Python.

The marginal is exactly what the ratified below-threshold apportionment rule (option 2a, §5 of
cowork_joint_estimator_factorization.md) needs: for each mode, the count of every normalized chord
CLASS KEY over the ground-truth-labeled segments of all covered stems. It REUSES the pinned decoder's
own producer (probe_decoder.FittedAdapter._count_mode_marginal), so the dumped values are
byte-identical to what the Python decode computes at runtime — no second derivation (#6). The C++ side
computes the apportionment denominator itself from this marginal + the ported back-off parent
functions, exactly as _apportion does.

Output: tools/joint_estimator/mode_marginal.json  {major: {class_key: count}, minor: {...}} + provenance.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_decoder as pd     # noqa: E402  the pinned decoder (its _count_mode_marginal is reused)


def _git_head() -> str:
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def main():
    adapter = pd.FittedAdapter(leftover_mode="freq", table_set="all")
    marg = adapter._count_mode_marginal()      # {"major": {key: count}, "minor": {key: count}}
    out = {
        "provenance": {
            "generator": "tools/joint_estimator/gen_mode_marginal.py",
            "instrument_commit": _git_head(),
            "source": "probe_decoder.FittedAdapter._count_mode_marginal (pinned; reused verbatim)",
            "note": ("per-mode count of every normalized chord CLASS KEY over the GT-labeled segments "
                     "of all covered stems (fold_assignment.stem_index), excluding is_major=None and "
                     "raw_unnormalized classes. Consumed by the C++ joint module's leftover-rule "
                     "apportionment (option 2a); the denominator is recomputed C++-side from this "
                     "marginal + the ported back-off parents, matching _apportion."),
            "n_major_classes": len(marg["major"]),
            "n_minor_classes": len(marg["minor"]),
            "total_major_tokens": sum(marg["major"].values()),
            "total_minor_tokens": sum(marg["minor"].values()),
        },
        "major": marg["major"],
        "minor": marg["minor"],
    }
    path = _HERE / "mode_marginal.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {path}  major={len(marg['major'])} classes / {sum(marg['major'].values())} tokens; "
          f"minor={len(marg['minor'])} classes / {sum(marg['minor'].values())} tokens")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
test_snapshot_sources.py — cheap drift check for the external corpora the gates
depend on (corpus audit C1).

The pipeline_snapshot goldens (src/notation/tests/pipeline_snapshot_tests/) and
the BIR baselines are only meaningful against the *exact bytes* of the DCML/WiR
source files. Those files live in `tools/dcml/*`, which is gitignored and cloned
at floating upstream HEAD — so nothing in the tree, until now, recorded their
identity. `tools/snapshot_sources_manifest.json` pins them (per-file sha256 +
the upstream clone commit). This test verifies the on-disk bytes still match the
manifest and fails loudly if upstream drifted.

It does NOT clone anything and does NOT touch the C++ suite. On a fresh checkout
(no `tools/dcml/`), every check skips with a clear message.

Run (no pytest in the venv — use unittest):
    cd C:\\s\\MS && python -m unittest discover -s tools/tests -p "test_*.py" -v
or:
    cd C:\\s\\MS && python tools/tests/test_snapshot_sources.py
"""
from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent
_MANIFEST = _ROOT / "tools" / "snapshot_sources_manifest.json"
_DCML = _ROOT / "tools" / "dcml"

_DRIFT_MSG = ("source corpus drifted — see tools/snapshot_sources_manifest.json "
              "(the pinned DCML/WiR bytes no longer match disk; the snapshot/BIR "
              "gates rest on these exact files)")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_manifest() -> dict:
    return json.loads(_MANIFEST.read_text(encoding="utf-8"))


class SnapshotSourcesManifest(unittest.TestCase):
    def test_manifest_present_and_wellformed(self):
        self.assertTrue(_MANIFEST.exists(), f"missing {_MANIFEST}")
        m = _load_manifest()
        self.assertEqual(len(m.get("snapshot_sources", [])), 11,
                         "manifest must pin exactly the 11 kCorpus snapshot sources")

    def test_eleven_snapshot_sources_match_manifest(self):
        if not _DCML.exists():
            self.skipTest("tools/dcml absent (fresh checkout) — nothing to verify")
        m = _load_manifest()
        mismatches = []
        for src in m["snapshot_sources"]:
            p = _ROOT / src["path"]
            if not p.exists():
                mismatches.append(f"MISSING {src['path']}")
                continue
            digest = _sha256(p)
            if digest != src["sha256"]:
                mismatches.append(
                    f"{src['path']}\n      manifest={src['sha256']}\n      ondisk  ={digest}")
        self.assertEqual(mismatches, [],
                         _DRIFT_MSG + "\n  " + "\n  ".join(mismatches))

    def test_bir_gate_wir_aggregate_matches_manifest(self):
        """The BIR gate consumes the When-in-Rome analysis.txt set; pin its
        aggregate hash too. Skips if when_in_rome is absent."""
        if not (_DCML / "when_in_rome").exists():
            self.skipTest("tools/dcml/when_in_rome absent — nothing to verify")
        m = _load_manifest()
        wir = m["bir_gate_wir_annotations"]
        perfile = []
        missing = []
        for rel in wir["paths"]:
            p = _ROOT / rel
            if not p.exists():
                missing.append(rel)
                continue
            perfile.append(_sha256(p))
        self.assertEqual(missing, [],
                         _DRIFT_MSG + "\n  missing WiR annotation files:\n  "
                         + "\n  ".join(missing))
        agg = hashlib.sha256("\n".join(sorted(perfile)).encode()).hexdigest()
        self.assertEqual(agg, wir["aggregate_sha256"], _DRIFT_MSG
                         + "\n  When-in-Rome BIR annotation set aggregate hash changed")


if __name__ == "__main__":
    unittest.main(verbosity=2)

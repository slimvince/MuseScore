#!/usr/bin/env python3
"""
test_dcml_parser_figbass_pedal.py — pins the two additive DcmlRegion fields
`figbass` (N10 inversion figured-bass) and `pedal` (N20 pedal-point) exposed at
the Wave-3 addendum (cc_wave3_addendum_report.md).

The two columns exist on every held DLC `.harmonies.tsv`; before the addendum the
parser dropped them.  The exposure is ADDITIVE: new fields with a `None` default,
no existing field's parsing changed, and — crucially — no consumer reads them yet,
so the BIR gate stays byte-identical (proven separately in the report).

These tests are self-contained (a temp TSV fixture, no dependency on the gitignored
`tools/dcml/` clones) and assert:
  1. figbass/pedal are carried verbatim when present, None when empty;
  2. a TSV that LACKS the columns still parses (safe default);
  3. the change is additive — the existing RN / root / key read surface is unchanged;
  4. the rntxt path (When in Rome has neither column) leaves both fields None.

Run:
    cd C:\\s\\MS && python -m unittest tools.tests.test_dcml_parser_figbass_pedal -v
or:
    cd C:\\s\\MS && python tools/tests/test_dcml_parser_figbass_pedal.py
"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path

_THIS_DIR  = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent
sys.path.insert(0, str(_TOOLS_DIR))

import dcml_parser as dcml            # noqa: E402


# A DLC-shaped harmonies TSV carrying the columns parse_abc_harmonies_file reads,
# incl. figbass + pedal.  Rows: a V6 with figbass but no pedal; a I with a pedal
# but no figbass; a V65 with both; and a deliberate rest (numeral '.') that the
# region stream skips.
_TSV_WITH_COLS = (
    "mn\tmn_onset\tquarterbeats\tquarterbeats_all_endings\tglobalkey\tlocalkey\t"
    "relativeroot\tchord\tnumeral\tfigbass\tpedal\tcadence\tphraseend\n"
    "1\t0\t0\t0\tC\tC\t\tV6\tV\t6\t\t\t\n"
    "1\t1\t1\t1\tC\tC\t\tI\tI\t\t1\t\t\n"
    "2\t0\t4\t4\tC\tC\t\tV65\tV\t65\t5\tPAC\t}\n"
    "2\t2\t6\t6\tC\tC\t\t.\t.\t\t\t\t\n"
)

# The same rows WITHOUT the figbass/pedal columns (an older/other TSV shape) —
# the fields must default to None, not raise.
_TSV_NO_COLS = (
    "mn\tmn_onset\tquarterbeats\tquarterbeats_all_endings\tglobalkey\tlocalkey\t"
    "relativeroot\tchord\tnumeral\n"
    "1\t0\t0\t0\tC\tC\t\tV6\tV\n"
    "1\t1\t1\t1\tC\tC\t\tI\tI\n"
)


def _write_tmp(text: str) -> str:
    fd, path = tempfile.mkstemp(suffix=".harmonies.tsv")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    return path


class TestFigbassPedalExposure(unittest.TestCase):
    def setUp(self):
        self._paths = []

    def tearDown(self):
        for p in self._paths:
            try:
                os.remove(p)
            except OSError:
                pass

    def _parse(self, text):
        p = _write_tmp(text)
        self._paths.append(p)
        return dcml.parse_abc_harmonies_file(p)

    def test_figbass_and_pedal_carried_verbatim(self):
        regs = self._parse(_TSV_WITH_COLS)
        # three scoreable rows (the numeral '.' rest is skipped)
        self.assertEqual(len(regs), 3)
        by_key = {(r.roman_numeral, r.figbass, r.pedal) for r in regs}
        self.assertIn(("V", "6", None), by_key)   # V6: figbass only
        self.assertIn(("I", None, "1"), by_key)   # I: pedal only (scale-degree 1)
        self.assertIn(("V", "65", "5"), by_key)   # V65: both

    def test_empty_cells_are_none(self):
        regs = self._parse(_TSV_WITH_COLS)
        v6 = next(r for r in regs if r.chord_symbol == "V6")
        self.assertEqual(v6.figbass, "6")
        self.assertIsNone(v6.pedal)          # empty pedal cell -> None (not "")

    def test_missing_columns_default_none(self):
        # A TSV lacking figbass/pedal columns must still parse; fields default None.
        regs = self._parse(_TSV_NO_COLS)
        self.assertEqual(len(regs), 2)
        for r in regs:
            self.assertIsNone(r.figbass)
            self.assertIsNone(r.pedal)

    def test_additive_read_surface_unchanged(self):
        # The existing RN / root / key parse is unchanged by the new fields.
        regs = self._parse(_TSV_WITH_COLS)
        v6 = next(r for r in regs if r.chord_symbol == "V6")
        self.assertEqual(v6.roman_numeral, "V")
        self.assertEqual(v6.root_pc, 7)      # G in C major
        self.assertEqual(v6.global_key, "C")
        # the cadence/phraseend oracle columns still work beside the new ones
        v65 = next(r for r in regs if r.chord_symbol == "V65")
        self.assertEqual(v65.cadence, "PAC")
        self.assertEqual(v65.phraseend, "}")
        self.assertEqual(v65.figbass, "65")
        self.assertEqual(v65.pedal, "5")

    def test_rntxt_path_leaves_fields_none(self):
        # When-in-Rome rntxt has neither column; DcmlRegions from it default None.
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                         encoding="utf-8") as f:
            f.write("Composer: Test\nWork: Test\nAnalyst: Test\n\n"
                    "Time Signature: 4/4\nm1 C: I b3 V\nm2 I\n")
            path = f.name
        self._paths.append(path)
        regs = dcml.parse_rntxt_file(path)
        self.assertTrue(regs)
        for r in regs:
            self.assertIsNone(r.figbass)
            self.assertIsNone(r.pedal)


if __name__ == "__main__":
    unittest.main()

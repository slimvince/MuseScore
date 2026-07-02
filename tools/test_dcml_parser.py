#!/usr/bin/env python3

import unittest
from pathlib import Path

from dcml_parser import parse_abc_harmonies_file, parse_cadence_phrase_markers


_FIXTURES = Path(__file__).resolve().parent / "tests" / "fixtures"


class DcmlParserTests(unittest.TestCase):
    def test_parse_abc_harmonies_resolves_relativeroot_applied_chords(self) -> None:
        repo_root = Path(__file__).resolve().parent.parent
        fixture = repo_root / "tools" / "dcml" / "corelli" / "harmonies" / "op01n08d.harmonies.tsv"

        regions = parse_abc_harmonies_file(str(fixture))
        by_measure = {(region.measure_number, region.beat): region for region in regions}

        self.assertEqual(by_measure[(10, 1.0)].chord_symbol, "V/v")
        self.assertEqual(by_measure[(10, 1.0)].root_pc, 2)

        self.assertEqual(by_measure[(15, 1.0)].chord_symbol, "IV/III")
        self.assertEqual(by_measure[(15, 1.0)].root_pc, 8)

        self.assertEqual(by_measure[(16, 1.0)].chord_symbol, "ii/III")
        self.assertEqual(by_measure[(16, 1.0)].root_pc, 5)

        self.assertEqual(by_measure[(17, 1.0)].chord_symbol, "iii/III")
        self.assertEqual(by_measure[(17, 1.0)].root_pc, 7)

        self.assertEqual(by_measure[(18, 1.0)].chord_symbol, "vi/III")
        self.assertEqual(by_measure[(18, 1.0)].root_pc, 0)

        self.assertEqual(by_measure[(19, 1.0)].chord_symbol, "I/III")
        self.assertEqual(by_measure[(19, 1.0)].root_pc, 3)

        self.assertEqual(by_measure[(23, 1.0)].chord_symbol, "V6/III")
        self.assertEqual(by_measure[(23, 1.0)].root_pc, 10)


class L6OracleColumnTests(unittest.TestCase):
    """Task 1 — the additive `cadence`/`phraseend` L6-oracle columns."""

    def test_region_fields_populated_from_columns(self) -> None:
        fixture = _FIXTURES / "l6_markers_with_columns.harmonies.tsv"
        regions = parse_abc_harmonies_file(str(fixture))

        # Rest row (numeral '.') is still skipped — 6 scoreable regions, not 7.
        self.assertEqual(len(regions), 6)
        by_tick = {r.abs_tick: r for r in regions}

        # cadence + phraseend carried verbatim on the bearing region; None when empty.
        self.assertEqual(by_tick[0].phraseend, "{")
        self.assertIsNone(by_tick[0].cadence)
        self.assertIsNone(by_tick[960].cadence)
        self.assertIsNone(by_tick[960].phraseend)
        self.assertEqual(by_tick[1920].cadence, "PAC")
        self.assertEqual(by_tick[1920].phraseend, "}{")
        self.assertEqual(by_tick[3840].cadence, "HC")
        self.assertEqual(by_tick[3840].phraseend, "}")
        # HC sub-type carried verbatim, not normalized.
        self.assertEqual(by_tick[7680].cadence, "HC.SIM")
        self.assertIsNone(by_tick[7680].phraseend)

        # The RN read surface is untouched by the added columns.
        self.assertEqual(by_tick[9600].roman_numeral, "I")
        self.assertEqual(by_tick[9600].local_key, "G")

    def test_marker_extractor_captures_rest_row_markers(self) -> None:
        fixture = _FIXTURES / "l6_markers_with_columns.harmonies.tsv"
        cadence_markers, phrase_markers = parse_cadence_phrase_markers(str(fixture))

        # Cadence labels sit only on numeral-bearing rows here: PAC, HC, HC.SIM, PAC.
        self.assertEqual([(m.abs_tick, m.label) for m in cadence_markers],
                         [(1920, "PAC"), (3840, "HC"), (7680, "HC.SIM"), (9600, "PAC")])

        # phraseend markers include the REST-row bracket ('\\' @5760) that the
        # region stream drops — 5 markers, one more than the region-fields carry.
        # NB: the DCML phrase-end backslash bracket is literally two backslash
        # characters ("\\\\" in source) — carried verbatim, not unescaped.
        self.assertEqual([(m.abs_tick, m.label) for m in phrase_markers],
                         [(0, "{"), (1920, "}{"), (3840, "}"), (5760, "\\\\"), (9600, "}")])
        rest_row = [m for m in phrase_markers if m.abs_tick == 5760]
        self.assertEqual(len(rest_row), 1)
        self.assertEqual(rest_row[0].kind, "phraseend")

    def test_missing_columns_parse_identically(self) -> None:
        with_cols = _FIXTURES / "l6_markers_with_columns.harmonies.tsv"
        no_cols = _FIXTURES / "l6_markers_no_columns.harmonies.tsv"

        # A TSV without the columns parses exactly as before: fields default None,
        # and the RN/root read surface is unchanged.
        regions = parse_abc_harmonies_file(str(no_cols))
        self.assertEqual(len(regions), 4)
        for r in regions:
            self.assertIsNone(r.cadence)
            self.assertIsNone(r.phraseend)
        self.assertEqual({r.abs_tick for r in regions}, {0, 960, 1920, 3840})

        # The marker extractor returns empty lists when the columns are absent.
        cad, phr = parse_cadence_phrase_markers(str(no_cols))
        self.assertEqual(cad, [])
        self.assertEqual(phr, [])

        # Root/RN read surface identical to the with-columns fixture on the shared
        # first four scoreable rows (additive columns change nothing).
        base = parse_abc_harmonies_file(str(with_cols))
        base_by_tick = {r.abs_tick: r for r in base}
        for r in regions:
            self.assertEqual(r.roman_numeral, base_by_tick[r.abs_tick].roman_numeral)
            self.assertEqual(r.root_pc, base_by_tick[r.abs_tick].root_pc)


if __name__ == '__main__':
    unittest.main()
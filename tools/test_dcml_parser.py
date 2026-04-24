#!/usr/bin/env python3

import unittest
from pathlib import Path

from dcml_parser import parse_abc_harmonies_file


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


if __name__ == '__main__':
    unittest.main()
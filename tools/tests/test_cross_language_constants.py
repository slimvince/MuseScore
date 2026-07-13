#!/usr/bin/env python3
"""
test_cross_language_constants.py — the guard on every Python constant that VALUE-COPIES a C++ one.

OI-132(b) / DT-3. Two measurement instruments hold a number that is really the production C++
value, restated in Python because a C++ constant cannot be imported:

  tools/analyze_inversion_errors.INVERSION_SUSPICION_MARGIN  copies the production default of
      the preference `inversionSuspicionMargin`  (src/composing/analysis/types/analysistypes.h)
  tools/music21_batch.TICKS_PER_QUARTER                      copies MuseScore's
      `Constants::DIVISION`                     (src/engraving/types/constants.h)

Neither can be single-sourced, so the only thing that can keep them honest is a test that reads
the producer. These tests PARSE the C++ declaration and assert the Python copy equals it — the
same producer-parsing pattern the OI-155 mode-vocabulary test and the OI-135 sync test use. A
change to either C++ value now turns this red instead of silently mis-attributing every inversion
blocker (the margin) or mis-scaling every music21 alignment (the tick grid).

The tests assert AGREEMENT, not a particular number: if the production value legitimately moves,
the fix is to move the Python copy with it in the same commit — which is exactly the sync this
guard exists to force.

Run:
    cd C:\\s\\MS && python -m unittest discover -s tools/tests -p "test_*.py" -v
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

_THIS_DIR  = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent
_REPO_ROOT = _TOOLS_DIR.parent
sys.path.insert(0, str(_TOOLS_DIR))

import analyze_inversion_errors as aie   # noqa: E402
import compare_analyses as cmp           # noqa: E402
import music21_batch as m21b             # noqa: E402

_ANALYSIS_TYPES_H = _REPO_ROOT / "src" / "composing" / "analysis" / "types" / "analysistypes.h"
_ENGRAVING_CONSTANTS_H = _REPO_ROOT / "src" / "engraving" / "types" / "constants.h"
_BATCH_ANALYZE_CPP = _TOOLS_DIR / "batch_analyze.cpp"


def _cpp_pref_default(header: Path, field: str) -> float:
    """The in-class default initializer of a C++ preference field, e.g.
    `double inversionSuspicionMargin = 0.70;` -> 0.70."""
    text = header.read_text(encoding="utf-8")
    m = re.search(rf"\b(?:double|float)\s+{re.escape(field)}\s*=\s*([0-9.]+)\s*;", text)
    if not m:
        raise AssertionError(f"could not find the default of `{field}` in {header}")
    return float(m.group(1))


def _cpp_int_constant(header: Path, name: str) -> int:
    """A C++ integer constant, e.g. `constexpr static int DIVISION = 480;` -> 480."""
    text = header.read_text(encoding="utf-8")
    m = re.search(rf"\b{re.escape(name)}\s*=\s*(\d+)\s*;", text)
    if not m:
        raise AssertionError(f"could not find the constant `{name}` in {header}")
    return int(m.group(1))


def _emitted_quality_strings() -> set:
    """Every string batch_analyze's qualityToString(ChordQuality) can write into a .ours.json —
    the OURS-side quality vocabulary the comparator must be able to normalise."""
    text = _BATCH_ANALYZE_CPP.read_text(encoding="utf-8")
    body = text.split("static const char* qualityToString(ChordQuality q)\n{", 1)[1].split("}", 1)[0]
    out = set(re.findall(r'return "([^"]+)";', body))
    if not out:
        raise AssertionError(f"could not parse qualityToString() in {_BATCH_ANALYZE_CPP}")
    return out


class TestCrossLanguageConstantCopies(unittest.TestCase):

    def test_inversion_suspicion_margin_matches_the_production_default(self):
        """analyze_inversion_errors attributes each residual inversion error to a blocker by
        comparing the recorded score margin against the margin the analyzer ACTUALLY ran with.
        If the production default moves and this copy does not, every blocker-B/C count is
        silently attributed to the wrong cause."""
        produced = _cpp_pref_default(_ANALYSIS_TYPES_H, "inversionSuspicionMargin")
        self.assertEqual(
            aie.INVERSION_SUSPICION_MARGIN, produced,
            f"analyze_inversion_errors.INVERSION_SUSPICION_MARGIN = "
            f"{aie.INVERSION_SUSPICION_MARGIN} but the production default of "
            f"inversionSuspicionMargin is {produced}. Sync the copy in the same commit.")

    def test_ticks_per_quarter_matches_the_engraving_division(self):
        """music21 reports offsets in quarter notes; this factor puts them on the SAME tick grid
        our regions use. A disagreement with Constants::DIVISION mis-scales every music21-vs-ours
        tick alignment — and would do so silently, since both sides would still be self-consistent."""
        produced = _cpp_int_constant(_ENGRAVING_CONSTANTS_H, "DIVISION")
        self.assertEqual(
            m21b.TICKS_PER_QUARTER, produced,
            f"music21_batch.TICKS_PER_QUARTER = {m21b.TICKS_PER_QUARTER} but MuseScore's "
            f"Constants::DIVISION is {produced}. Sync the copy in the same commit.")


class TestQualityVocabularyIsComplete(unittest.TestCase):
    """OI-127(a): the comparator's quality map passes an unmapped string through unnormalised.
    That is safe only while it can normalise everything the producer emits — so the producer's
    own vocabulary is read here and required to be covered."""

    def test_every_emitted_quality_is_normalisable(self):
        emitted = _emitted_quality_strings()
        # "Unknown" is the default arm — the no-quality marker, settled by _quality_matches
        # before normalisation, deliberately NOT a key in the map.
        self.assertIn("Unknown", emitted)
        for q in sorted(emitted - {"Unknown"}):
            with self.subTest(quality=q):
                self.assertIn(
                    q, cmp._QUALITY_NORMALISE,
                    f"batch_analyze can emit quality '{q}' but compare_analyses._QUALITY_NORMALISE "
                    f"has no entry for it — it would pass through unnormalised and could score a "
                    f"false quality (dis)agreement. Add it to the map.")

    def test_two_unknown_qualities_are_not_an_agreement(self):
        """Both sides saying 'I cannot name this' is two abstains, not a match (OI-127(a))."""
        r = lambda q: cmp.Region(  # noqa: E731
            measure_number=1, beat=1.0, start_tick=0, end_tick=480, duration=1.0,
            root_pc=0, quality=q, chord_symbol="x", roman_numeral="I", key="Cmaj",
            key_confidence=0.9, diatonic_to_key=True, alternatives=[],
            bass_pc=None, bass_is_root=None)
        self.assertFalse(cmp._quality_matches(r("Unknown"), r("Unknown")))
        self.assertTrue(cmp._quality_matches(r("Major"), r("Major")))


class TestUnresolvedRootIsNotAnAgreement(unittest.TestCase):
    """OI-127(b): the JSON schema spells 'no root' as -1, so two rootless regions would compare
    EQUAL and score a chord agreement — a false agreement that flatters the metric."""

    def _region(self, root_pc):
        return cmp.Region(
            measure_number=1, beat=1.0, start_tick=0, end_tick=480, duration=1.0,
            root_pc=root_pc, quality="Major", chord_symbol="x", roman_numeral="I",
            key="Cmaj", key_confidence=0.9, diatonic_to_key=True, alternatives=[],
            bass_pc=None, bass_is_root=None)

    def test_two_rootless_regions_do_not_match(self):
        self.assertFalse(cmp._roots_match(self._region(-1), self._region(-1)))
        self.assertFalse(cmp._chord_matches(self._region(-1), self._region(-1)))

    def test_a_rootless_region_never_matches_a_resolved_one(self):
        self.assertFalse(cmp._roots_match(self._region(-1), self._region(0)))
        self.assertFalse(cmp._roots_match(self._region(0), self._region(-1)))

    def test_resolved_roots_still_compare_normally(self):
        self.assertTrue(cmp._roots_match(self._region(7), self._region(7)))
        self.assertFalse(cmp._roots_match(self._region(7), self._region(9)))


if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
"""
test_oracle_root_metric.py — pins the standing per-event tiered oracle-root metric
(tools/oracle_root_metric.py).

The round-3 charged/floor separation and the decomposition machinery are REUSED
verbatim from compare_analyses / dcml_parser / characterise_bir_false (already covered
by their own tests and validated by reproduction against the on-disk corpora). What is
NEW in this tool, and what these tests pin, is:

  1. classify_charged_event — the 5-tier decision tree, in particular the mandated
     KEY-HARD vs KEY-TONICIZATION split (the separation that is "the whole point"):
       KEY-HARD          our key != DCML AND music21 corroborates DCML (m21 == DCML)
       KEY-TONICIZATION  our key != DCML but music21 disputes DCML (m21 != DCML)
       OVER-GRAB         keys agree, region spans >= 2 oracle roots
       CHORD-ID          keys agree, region spans exactly 1 oracle root
       AMBIGUOUS         our key == DCML but m21 disputes it, or a key is unparseable
  2. the three key parsers (parse_our_key / parse_dcml_key / parse_m21_key).
  3. the structural charged/floor separation invariant (no event is ever both).

Every expected value is hand-derived (derivations inline).

Run:
    cd C:\\s\\MS && python -m unittest discover -s tools/tests -p "test_*.py" -v
or:
    cd C:\\s\\MS && python tools/tests/test_oracle_root_metric.py
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent
sys.path.insert(0, str(_TOOLS_DIR))

import compare_analyses as cmp            # noqa: E402
import dcml_parser as dcml                # noqa: E402
import oracle_root_metric as orm          # noqa: E402


# ── builders (carry only the fields the tool reads) ───────────────────────────
def OURS(key="Cmaj", root_pc=0, *, start=0, end=480):
    """An analyzer Region; the tier classifier reads only .key (and .start/.end_tick
    for the over-grab span, supplied separately as a count here)."""
    return cmp.Region(
        measure_number=1, beat=1.0, start_tick=start, end_tick=end,
        duration=1.0, root_pc=root_pc, quality="Major", chord_symbol="x",
        roman_numeral="I", key=key, key_confidence=0.9, diatonic_to_key=True,
        alternatives=[], bass_pc=None, bass_is_root=None,
    )


def M21(key="C major", root_pc=0):
    return cmp.Region(
        measure_number=1, beat=1.0, start_tick=0, end_tick=480,
        duration=1.0, root_pc=root_pc, quality="Major", chord_symbol="x",
        roman_numeral="I", key=key, key_confidence=0.9, diatonic_to_key=True,
        alternatives=[], bass_pc=None, bass_is_root=None,
    )


def DR(local_key="C", root_pc=0, rn="I"):
    return dcml.DcmlRegion(
        measure_number=1, beat=1.0, global_key="C", local_key=local_key,
        chord_symbol=rn, roman_numeral=rn, root_pc=root_pc,
    )


# ════════════════════════════════════════════════════════════════════════════
# 1 — the 5-tier decision tree (classify_charged_event)
# ════════════════════════════════════════════════════════════════════════════
class TestTierClassifier(unittest.TestCase):
    def test_key_hard_tonic(self):
        # our Cmaj(0) vs DCML g(7,minor); m21 'g minor'(7) CORROBORATES DCML.
        # our != both oracles -> genuine key-detection error.
        tier, why = orm.classify_charged_event(
            OURS("Cmaj"), M21("g minor"), 1, DR("g", rn="V"))
        self.assertEqual(tier, "KEY-HARD")
        self.assertEqual(why, "tonic")

    def test_key_hard_mode_only(self):
        # our Cmaj(0,major) vs DCML c(0,minor); m21 'c minor'(0) corroborates DCML.
        # tonic matches, mode differs -> KEY band, hard (m21 == DCML).
        tier, why = orm.classify_charged_event(
            OURS("Cmaj"), M21("c minor"), 1, DR("c", rn="i"))
        self.assertEqual(tier, "KEY-HARD")
        self.assertEqual(why, "mode-only")

    def test_key_tonicization(self):
        # our Cmaj(0) vs DCML a(9,minor); m21 'C major'(0) DISPUTES DCML's local key.
        # the local-vs-global grain -> reported separately, NEVER folded into KEY-HARD.
        tier, why = orm.classify_charged_event(
            OURS("Cmaj"), M21("C major"), 1, DR("a", rn="IV"))
        self.assertEqual(tier, "KEY-TONICIZATION")

    def test_key_tonicization_third_key(self):
        # our key, DCML key, and m21 key are three DIFFERENT keys: our != DCML, and
        # m21 disputes DCML (m21 != DCML). Operationally this is the disputed-local-key
        # grain -> KEY-TONICIZATION (not KEY-HARD: m21 does NOT corroborate DCML).
        tier, why = orm.classify_charged_event(
            OURS("Cmaj"), M21("d minor"), 1, DR("a", rn="IV"))
        self.assertEqual(tier, "KEY-TONICIZATION")

    def test_over_grab(self):
        # all three keys agree (C); our region covers >= 2 oracle roots.
        tier, why = orm.classify_charged_event(
            OURS("Cmaj"), M21("C major"), 3, DR("C", rn="ii"))
        self.assertEqual(tier, "OVER-GRAB")
        self.assertIn("3", why)

    def test_chord_id(self):
        # all three keys agree (C); our region aligns 1:1 (exactly 1 oracle root).
        tier, why = orm.classify_charged_event(
            OURS("Cmaj"), M21("C major"), 1, DR("C", rn="ii"))
        self.assertEqual(tier, "CHORD-ID")

    def test_ambiguous_oracle_key_disputed_keymatch(self):
        # our key MATCHES DCML (C), but m21 disputes the oracle key ('a minor'(9)).
        # the oracle key is not cleanly established -> AMBIGUOUS, not OVER-GRAB/CHORD-ID.
        tier, why = orm.classify_charged_event(
            OURS("Cmaj"), M21("a minor"), 3, DR("C", rn="ii"))
        self.assertEqual(tier, "AMBIGUOUS")
        self.assertEqual(why, "oracle_key_disputed_keymatch")

    def test_ambiguous_unparseable_our_key(self):
        tier, why = orm.classify_charged_event(
            OURS("???"), M21("C major"), 1, DR("C", rn="I"))
        self.assertEqual(tier, "AMBIGUOUS")
        self.assertEqual(why, "unparseable_key")

    def test_key_band_partitions_into_hard_and_tonic(self):
        # The aggregate KEY band (our != DCML) must split exhaustively into exactly
        # KEY-HARD (m21 corroborates) xor KEY-TONICIZATION (m21 disputes) — never both,
        # never neither. Sweep all m21 keys for a fixed our!=DCML pair.
        ours, dr = OURS("Cmaj"), DR("g", rn="V")  # our 0 != DCML 7
        for m21key, expect in [
            ("g minor", "KEY-HARD"),        # m21 == DCML
            ("C major", "KEY-TONICIZATION"),  # m21 == ours, disputes DCML
            ("d minor", "KEY-TONICIZATION"),  # m21 third key, disputes DCML
        ]:
            tier, _ = orm.classify_charged_event(ours, M21(m21key), 1, dr)
            self.assertIn(tier, ("KEY-HARD", "KEY-TONICIZATION"))
            self.assertEqual(tier, expect, m21key)


# ════════════════════════════════════════════════════════════════════════════
# 2 — the key parsers
# ════════════════════════════════════════════════════════════════════════════
class TestKeyParsers(unittest.TestCase):
    def test_parse_our_key(self):
        self.assertEqual(orm.parse_our_key("Cmaj"), (0, "major"))
        self.assertEqual(orm.parse_our_key("Gmin"), (7, "minor"))
        self.assertEqual(orm.parse_our_key("Bbmaj"), (10, "major"))
        # exotic modes map to their third's maj/minor class
        self.assertEqual(orm.parse_our_key("ADor"), (9, "minor"))
        self.assertEqual(orm.parse_our_key("FMixolyd"), (5, "major"))
        # unknown mode -> tonic only
        self.assertEqual(orm.parse_our_key("Cweird"), (0, None))
        # unicode accidentals normalized
        self.assertEqual(orm.parse_our_key("F♯maj"), (6, "major"))
        self.assertEqual(orm.parse_our_key(""), (None, None))

    def test_parse_dcml_key(self):
        self.assertEqual(orm.parse_dcml_key("C"), (0, "major"))
        self.assertEqual(orm.parse_dcml_key("g"), (7, "minor"))
        self.assertEqual(orm.parse_dcml_key("Bb"), (10, "major"))
        self.assertEqual(orm.parse_dcml_key("f#"), (6, "minor"))
        self.assertEqual(orm.parse_dcml_key(""), (None, None))

    def test_parse_m21_key(self):
        self.assertEqual(orm.parse_m21_key("g minor"), (7, "minor"))
        self.assertEqual(orm.parse_m21_key("B- major"), (10, "major"))   # '-' = flat
        self.assertEqual(orm.parse_m21_key("f# minor"), (6, "minor"))
        self.assertEqual(orm.parse_m21_key("C major"), (0, "major"))
        self.assertEqual(orm.parse_m21_key("garbage"), (None, None))
        self.assertEqual(orm.parse_m21_key(""), (None, None))


# ════════════════════════════════════════════════════════════════════════════
# 3 — the structural charged/floor separation invariant
# ════════════════════════════════════════════════════════════════════════════
class TestChargedFloorSeparation(unittest.TestCase):
    """A charge requires m21 == dcml; a floor requires m21 != dcml. So over every
    (our, m21, dcml) root combination no event can be BOTH charged and floor — the
    separation that lets the tool report them as never-summed standing sets."""

    def test_no_event_is_both_charged_and_floor(self):
        vals = [None, 0, 4, 7]
        for o in vals:
            for m in vals:
                for d in vals:
                    cat = cmp.three_way_classify(o, m, d)
                    charged = (cat == "music21_dcml_agree")
                    scoreable = (m is not None and d is not None)
                    floor = scoreable and (m != d)
                    self.assertFalse(charged and floor, (o, m, d, cat))
                    if charged:
                        # charged => m21 == dcml (and ours present, differing)
                        self.assertEqual(m, d)
                        self.assertIsNotNone(o)
                        self.assertNotEqual(o, d)

    def test_absent_our_root_is_not_charged(self):
        # oracle pair concurs but our root absent -> NOT charged (the flagged residual)
        self.assertEqual(cmp.three_way_classify(None, 7, 7), "no_dcml")
        self.assertNotEqual(cmp.three_way_classify(None, 7, 7), "music21_dcml_agree")


# ════════════════════════════════════════════════════════════════════════════
# 4 — region_at (tick-containment with boundary fallback)
# ════════════════════════════════════════════════════════════════════════════
class TestRegionAt(unittest.TestCase):
    def test_containment_and_boundary(self):
        regs = [OURS("Cmaj", 0, start=0, end=480),
                OURS("Gmaj", 7, start=480, end=960)]
        self.assertEqual(orm.region_at(regs, 0).key, "Cmaj")
        self.assertEqual(orm.region_at(regs, 479).key, "Cmaj")
        self.assertEqual(orm.region_at(regs, 480).key, "Gmaj")   # end-exclusive edge
        # tick at/after the final end -> boundary fallback to a region starting there,
        # else None
        self.assertIsNone(orm.region_at(regs, 960))


if __name__ == "__main__":
    unittest.main(verbosity=2)

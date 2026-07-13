#!/usr/bin/env python3
"""
test_metric_primitives_l0l1.py — pins the three DCML-only metric primitives added
for the ratified precision-metric design (L0–L1), built in compare_rn.py:

  BUILD 1  --wir-bach DIR          — score *.ours.json vs When-in-Rome Bach rntxt;
                                     report the covered/total coverage denominator.
  BUILD 2  --granularity-robust    — the duration-weighted union-of-boundaries unit
                                     (segmentation-invariant; design §2).
  BUILD 3  --key-breakdown         — split key_disagree into S1 (=global ≠local) and
                                     S2 (≠global), with the our-key parse-fail caveat.

These primitives are ORCHESTRATION + ONE NEW UNIT over already-pinned functions;
they do NOT redefine any existing bucket.  The 70 tests in test_metric_scripts.py
stay green unchanged (the existing region-count buckets are untouched).

The load-bearing property is segmentation-invariance (BUILD 2): the SAME underlying
analysis scored at two different segmentations must yield the SAME duration-weighted
fractions.  Every expected value here is derived BY HAND (derivations inline).

Run:
    cd C:\\s\\MS && python -m unittest discover -s tools/tests -p "test_*.py" -v
or:
    cd C:\\s\\MS && python tools/tests/test_metric_primitives_l0l1.py
"""

from __future__ import annotations

import io
import re
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

import sys

_THIS_DIR  = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent
sys.path.insert(0, str(_TOOLS_DIR))

import compare_analyses as cmp        # noqa: E402
import compare_rn as crn              # noqa: E402
import dcml_parser as dcml            # noqa: E402
import producer_key_modes as pkm      # noqa: E402  (the ONE reader of the producer's vocabulary)


# ── builders (carry only the fields the metric reads) ────────────────────────

def R(root_pc, rn="I", quality="Major", *, start=0, end=480, dur=1.0,
      measure=1, beat=1.0, key="Cmaj"):
    """An analyzer Region.  `key` defaults to the corpus form 'Cmaj' (no space)
    so the key-breakdown parser sees a parseable key by default."""
    return cmp.Region(
        measure_number=measure, beat=beat, start_tick=start, end_tick=end,
        duration=dur, root_pc=root_pc, quality=quality, chord_symbol="x",
        roman_numeral=rn, key=key, key_confidence=0.9, diatonic_to_key=True,
        alternatives=[], bass_pc=None, bass_is_root=None,
    )


def D(root_pc, chord, numeral=None, *, measure=1, beat=1.0,
      global_key="C", local_key="C"):
    """A DcmlRegion with root_pc supplied directly (not recomputed)."""
    return dcml.DcmlRegion(
        measure_number=measure, beat=beat, global_key=global_key,
        local_key=local_key, chord_symbol=chord,
        roman_numeral=numeral if numeral is not None else chord,
        root_pc=root_pc,
    )


def _fractions(gs):
    """Duration-weighted bucket fractions of a GridStats, as a dict over the
    five RN categories (over scored_dur)."""
    tot = gs.scored_dur
    return {k: (gs.bucket_dur[k] / tot if tot else 0.0) for k in crn.RN_CATEGORIES}


# ════════════════════════════════════════════════════════════════════════════
# BUILD 2 — the granularity-robust duration-weighted unit
#
# Shared fixture: one underlying analysis (I over the first half, V over the
# second), DCML reading I / vi / V across three quarter-spans.  tpb inferred 480,
# measure-1 anchor at tick 0 in BOTH segmentations, so the DCML tick spans are
# identical:  I=[0,480)  vi=[480,960)  V=[960,1920).
#
# COARSE segmentation (2 regions):  I[0,960)  V[960,1920)
# FINE   segmentation (4 regions):  I[0,480) I[480,960) V[960,1440) V[1440,1920)
#
# Hand-derived COARSE grid  (union bounds {0,480,960,1920}):
#   [0,480)   ours I(0) vs dcml I(0)  -> exact     w=480
#   [480,960) ours I(0) vs dcml vi(9) -> root_err  w=480   (root 0 != 9)
#   [960,1920)ours V(7) vs dcml V(7)  -> exact     w=960
#   => exact 1440, root_err 480, scored 1920  -> exact 0.75, root_err 0.25
#
# Hand-derived FINE grid  (union bounds {0,480,960,1440,1920}):
#   [0,480)    I(0)/I(0)  exact     480
#   [480,960)  I(0)/vi(9) root_err  480
#   [960,1440) V(7)/V(7)  exact     480
#   [1440,1920)V(7)/V(7)  exact     480
#   => exact 1440, root_err 480, scored 1920  -> exact 0.75, root_err 0.25  (SAME)
# ════════════════════════════════════════════════════════════════════════════

def _dcml_three():
    return [
        D(0, "I",  measure=1, beat=1.0),
        D(9, "vi", measure=1, beat=2.0),
        D(7, "V",  measure=1, beat=3.0),
    ]

def _ours_coarse():
    return [
        R(0, "I", start=0,   end=960,  dur=2.0, measure=1, beat=1.0),
        R(7, "V", start=960, end=1920, dur=2.0, measure=1, beat=3.0),
    ]

def _ours_fine():
    return [
        R(0, "I", start=0,    end=480,  dur=1.0, measure=1, beat=1.0),
        R(0, "I", start=480,  end=960,  dur=1.0, measure=1, beat=2.0),
        R(7, "V", start=960,  end=1440, dur=1.0, measure=1, beat=3.0),
        R(7, "V", start=1440, end=1920, dur=1.0, measure=1, beat=4.0),
    ]


class TestGridHandDerived(unittest.TestCase):
    """Known-input / known-output on the tiny COARSE fixture (cells + durations
    + expected weighted fractions derived by hand above)."""

    def setUp(self):
        self.gs = crn.grid_score_regions(_ours_coarse(), _dcml_three())

    def test_scored_and_unscored_duration(self):
        self.assertEqual(self.gs.scored_dur, 1920)
        self.assertEqual(self.gs.unscored_dur, 0)
        self.assertEqual(self.gs.pieces, 1)

    def test_bucket_durations(self):
        self.assertEqual(self.gs.bucket_dur["exact"], 1440)
        self.assertEqual(self.gs.bucket_dur["root_err"], 480)
        self.assertEqual(self.gs.bucket_dur["partial"], 0)
        self.assertEqual(self.gs.bucket_dur["key_disagree"], 0)
        self.assertEqual(self.gs.bucket_dur["quality_disagree"], 0)

    def test_weighted_fractions(self):
        fr = _fractions(self.gs)
        self.assertAlmostEqual(fr["exact"], 0.75)
        self.assertAlmostEqual(fr["root_err"], 0.25)


class TestGridSegmentationInvariance(unittest.TestCase):
    """THE load-bearing property (design §2): the same underlying analysis scored
    at two different segmentations yields the SAME duration-weighted fractions.

    Contrast the region-count metric, which would report different bucket
    *fractions* for the coarse (2 regions) vs fine (4 regions) segmentation — the
    2.2-i ~7× artifact.  The duration-weighted unit removes it by construction."""

    def test_coarse_equals_fine_fractions(self):
        coarse = crn.grid_score_regions(_ours_coarse(), _dcml_three())
        fine   = crn.grid_score_regions(_ours_fine(),   _dcml_three())
        self.assertEqual(_fractions(coarse), _fractions(fine))

    def test_invariance_is_nontrivial(self):
        # The fixture must exercise more than one bucket, else "invariance" is
        # vacuous.  Both segmentations carry exact AND root_err.
        coarse = crn.grid_score_regions(_ours_coarse(), _dcml_three())
        self.assertGreater(coarse.bucket_dur["exact"], 0)
        self.assertGreater(coarse.bucket_dur["root_err"], 0)

    def test_total_scored_duration_is_segmentation_independent(self):
        # Σ dur is fixed by the piece, not by either side's segmentation —
        # splitting a region cannot change it (the denominator-shift fix).
        coarse = crn.grid_score_regions(_ours_coarse(), _dcml_three())
        fine   = crn.grid_score_regions(_ours_fine(),   _dcml_three())
        self.assertEqual(coarse.scored_dur, fine.scored_dur)


class TestGridEdgeCases(unittest.TestCase):

    def test_zero_length_region_contributes_no_boundary(self):
        # A zero-length ours region (start==end) adds no boundary and does not
        # crash or double-count.  Result must match the clean coarse fixture.
        ours = _ours_coarse() + [R(0, "I", start=480, end=480, dur=0.0,
                                   measure=1, beat=1.5)]
        gs = crn.grid_score_regions(ours, _dcml_three())
        self.assertEqual(gs.scored_dur, 1920)
        self.assertEqual(gs.bucket_dur["exact"], 1440)
        self.assertEqual(gs.bucket_dur["root_err"], 480)

    def test_coincident_boundary_not_double_counted(self):
        # ours boundary at 960 coincides with the dcml V-span start at 960; the
        # union de-dups it, so total scored duration is unchanged (no overlap).
        gs = crn.grid_score_regions(_ours_coarse(), _dcml_three())
        self.assertEqual(
            gs.scored_dur,
            sum(gs.bucket_dur[k] for k in crn.RN_CATEGORIES))

    def test_gap_in_ours_coverage_charged_unscored(self):
        # ours covers only [0,480).  The DCML tick spans are clamped to the ours
        # tick extent (piece_end = max ours end_tick = 480), so only the I-span
        # [0,480) and vi-span [480,960) survive; the V-span collapses.  Cell
        # [0,480) scores exact; cell [480,960) has no active ours region -> it is
        # charged unscored, NOT mis-bucketed as an error.
        ours = [R(0, "I", start=0, end=480, dur=1.0, measure=1, beat=1.0)]
        gs = crn.grid_score_regions(ours, _dcml_three())
        self.assertEqual(gs.bucket_dur["exact"], 480)     # only [0,480) scored
        self.assertEqual(gs.scored_dur, 480)
        self.assertEqual(gs.unscored_dur, 480)            # [480,960) is a gap
        # Crucially: the gap did not inflate root_err / any error bucket.
        self.assertEqual(gs.bucket_dur["root_err"], 0)

    def test_empty_inputs_return_empty(self):
        self.assertEqual(crn.grid_score_regions([], _dcml_three()).pieces, 0)
        self.assertEqual(crn.grid_score_regions(_ours_coarse(), []).pieces, 0)

    def test_determinism(self):
        a = crn.grid_score_regions(_ours_coarse(), _dcml_three())
        b = crn.grid_score_regions(_ours_coarse(), _dcml_three())
        self.assertEqual(dict(a.bucket_dur), dict(b.bucket_dur))
        self.assertEqual((a.scored_dur, a.unscored_dur),
                         (b.scored_dur, b.unscored_dur))


# ════════════════════════════════════════════════════════════════════════════
# BUILD 1 — --wir-bach coverage denominator
#   A fixture dir with two *.ours.json; only one stem has a WiR analysis.txt
#   (find_wir_file stubbed).  Coverage must be covered=1 / total=2, never /2-by
#   -silently-dividing-by-the-corpus-size.
# ════════════════════════════════════════════════════════════════════════════

_OURS_JSON = (
    '{"regions":[{"measureNumber":1,"beat":1.0,"startTick":0,"endTick":480,'
    '"duration":1.0,"rootPitchClass":0,"quality":"Major","romanNumeral":"I",'
    '"key":"Cmaj"},'
    '{"measureNumber":1,"beat":3.0,"startTick":960,"endTick":1440,'
    '"duration":1.0,"rootPitchClass":7,"quality":"Major","romanNumeral":"V",'
    '"key":"Cmaj"}]}'
)

# Minimal When-in-Rome rntxt: m1 has I at b1 and V at b3 in C major.
_WIR_TXT = (
    "Composer: Test\n"
    "Title: Fixture\n"
    "Analyst: hand-derived\n"
    "Time Signature: 4/4\n"
    "\n"
    "m1 C: I b3 V\n"
)


class TestWirBachCoverage(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = Path(self._tmp.name)
        (self.dir / "probeA.ours.json").write_text(_OURS_JSON, encoding="utf-8")
        (self.dir / "probeB.ours.json").write_text(_OURS_JSON, encoding="utf-8")
        self.wir = self.dir / "probeA.analysis.txt"
        self.wir.write_text(_WIR_TXT, encoding="utf-8")

    def _stub(self, base, stem):
        # Only probeA has a WiR annotation; probeB has none.
        return str(self.wir) if stem == "probeA" else None

    def test_coverage_denominator_is_covered_over_total(self):
        with mock.patch("dcml_parser.find_wir_file", side_effect=self._stub):
            result = crn.score_corpus_wir(self.dir, self.dir)
        self.assertIsNotNone(result)
        stats, grid, cov = result
        self.assertEqual(cov.total, 2)      # both *.ours.json count toward total
        self.assertEqual(cov.covered, 1)    # only probeA has WiR -> never /2 silently
        self.assertEqual(stats.movements, 1)

    def test_scored_only_covered_movement(self):
        with mock.patch("dcml_parser.find_wir_file", side_effect=self._stub):
            result = crn.score_corpus_wir(self.dir, self.dir)
        stats, grid, cov = result
        # probeA: regions I(0)@b1, V(7)@b3 vs WiR I(0)@b1, V(7)@b3 -> 2 exact.
        self.assertEqual(stats.matched, 2)
        self.assertEqual(stats.exact, 2)
        self.assertGreater(grid.scored_dur, 0)   # grid computed for the covered piece

    def test_cli_reports_coverage_line(self):
        argv = ["compare_rn.py", "--wir-bach", str(self.dir),
                "--wir-base", str(self.dir)]
        buf = io.StringIO()
        with mock.patch("dcml_parser.find_wir_file", side_effect=self._stub), \
             mock.patch.object(sys, "argv", argv), redirect_stdout(buf):
            rc = crn.main()
        out = buf.getvalue()
        self.assertEqual(rc, 0)
        self.assertIn("WiR coverage: 1/2", out)


# ════════════════════════════════════════════════════════════════════════════
# BUILD 3 — --key-breakdown split of key_disagree
#   Three key_disagree pairs (root✓ 7, coarse-quality✓ Maj, degree V vs I), with
#   our key = {global, non-global, unparseable} respectively.
#     region1 key Cmaj  -> our (0,maj) == global C (0,maj)  -> S1 eq_global
#     region2 key Amin  -> our (9,min) != global C          -> S2 ne_global
#     region3 key ""    -> unparseable                       -> keyfail (in S2)
#   => key_disagree 3, S1 1, S2 2, keyfail 1, corpus-wide keyparse_fail 1.
# ════════════════════════════════════════════════════════════════════════════

class TestKeyBreakdownSplit(unittest.TestCase):

    def setUp(self):
        ours = [
            R(7, "V", start=0,   end=480,  measure=1, beat=1.0, key="Cmaj"),
            R(7, "V", start=480, end=960,  measure=1, beat=2.0, key="Amin"),
            R(7, "V", start=960, end=1440, measure=1, beat=3.0, key=""),
        ]
        dcmls = [
            D(7, "I", measure=1, beat=1.0, global_key="C", local_key="G"),
            D(7, "I", measure=1, beat=2.0, global_key="C", local_key="G"),
            D(7, "I", measure=1, beat=3.0, global_key="C", local_key="G"),
        ]
        self.stats = crn.score_regions(ours, dcmls)

    def test_all_three_are_key_disagree(self):
        # root 7==7, coarse quality Maj==Maj, degree V!=I -> key_disagree (not
        # root_err, not quality_disagree).
        self.assertEqual(self.stats.key_disagree, 3)
        self.assertEqual(self.stats.root_err, 0)
        self.assertEqual(self.stats.quality_disagree, 0)

    def test_s1_s2_split(self):
        self.assertEqual(self.stats.kd_eq_global, 1)   # S1
        self.assertEqual(self.stats.kd_ne_global, 2)   # S2 (incl. the keyfail)
        # invariant: S1 + S2 == key_disagree
        self.assertEqual(self.stats.kd_eq_global + self.stats.kd_ne_global,
                         self.stats.key_disagree)

    def test_keyfail_is_subset_of_s2(self):
        self.assertEqual(self.stats.kd_keyfail, 1)
        self.assertLessEqual(self.stats.kd_keyfail, self.stats.kd_ne_global)

    def test_corpus_wide_keyparse_fail(self):
        # The empty-key region is the only matched pair whose key fails to parse.
        self.assertEqual(self.stats.keyparse_fail, 1)
        self.assertEqual(self.stats.matched, 3)


class TestKeyTonicHelpers(unittest.TestCase):
    """The ported key parsers (must match the key_confound driver they reproduce)."""

    def test_our_key_tonic(self):
        self.assertEqual(crn._our_key_tonic("Cmaj"), (0, True))
        self.assertEqual(crn._our_key_tonic("Cmin"), (0, False))
        # The suffix is the PRODUCER's spelling ("Mixolyd", keyModeSuffix()), not an
        # abbreviation: the classification is set-membership in the emitted vocabulary,
        # not a prefix match (OI-155). "Gmix" is not a string the chain can emit.
        self.assertEqual(crn._our_key_tonic("GMixolyd"), (7, True))   # mixolydian = major-ish
        self.assertEqual(crn._our_key_tonic("Gdor"), (7, False))      # dorian = minor-ish
        self.assertEqual(crn._our_key_tonic("Bbmaj"), (10, True))
        self.assertEqual(crn._our_key_tonic("C#min"), (1, False))

    def test_our_key_tonic_mode_qualified_normalization(self):
        # carry-fix 2 Task 2: mode-qualified local-key names (correct tonic, uppercase
        # in the mode) normalize to (tonic, minor) instead of counting as a parse failure.
        self.assertEqual(crn._our_key_tonic("DDor"), (2, False))       # Dorian -> minor tonic
        # OI-132 (user-ruled 2026-07-13): the five dominant-family exotics reduce to the
        # MINOR key of their PARENT COLLECTION. E Phrygian-dominant is the dominant of A
        # minor (offset -7), so it grades A minor (9), not E minor (4).
        self.assertEqual(crn._our_key_tonic("EPhrygDom"), (9, False))
        self.assertEqual(crn._our_key_tonic("Gharm"), (7, False))      # harmonic minor
        self.assertEqual(crn._our_key_tonic("Dmel"), (2, False))       # melodic minor
        self.assertEqual(crn._our_key_tonic("F#harm"), (6, False))     # with accidental
        self.assertEqual(crn._our_key_tonic("Clyd"), (0, True))        # lydian = major-ish

    def test_our_key_tonic_unknown_mode_abstains(self):
        # ★ THE ABSTAIN RULE (OI-33, user-ruled at OI-155). A mode suffix OUTSIDE the
        # producer's vocabulary abstains on the MODE axis — (tonic, None) — and is NOT
        # silently graded minor. The tonic is still known, so this is not a full parse
        # failure; _our_key_ident (the one abstain decision) turns it into a keyfail.
        self.assertEqual(crn._our_key_tonic("Cweird"), (0, None))
        self.assertIsNone(crn._mode_class("weird"))
        self.assertIsNone(crn._our_key_ident("Cweird"))
        # ... while a mode IN the vocabulary yields a full identity.
        self.assertEqual(crn._our_key_ident("Cmaj"), (0, True))
        self.assertEqual(crn._our_key_ident("EPhrygDom"), (9, False))
        # An unparseable string abstains on BOTH axes.
        self.assertIsNone(crn._our_key_ident(""))

    def test_our_key_tonic_parse_failures(self):
        self.assertEqual(crn._our_key_tonic(""), (None, None))
        self.assertEqual(crn._our_key_tonic(None), (None, None))
        self.assertEqual(crn._our_key_tonic("C major"), (None, None))  # space -> no parse
        # OI-152 (the remaining key-parse abstain): the six emitted suffixes carrying an
        # accidental or a digit are rejected by _KB_OURS_KEY_RE's [A-Za-z]+ mode group, so
        # they abstain on BOTH axes (tonic included). Unchanged here — OI-152 owns it.
        self.assertEqual(crn._our_key_tonic("CDor♭2"), (None, None))
        self.assertEqual(crn._our_key_tonic("CLoc#2"), (None, None))

    def test_our_key_tonic_unicode_accidental_tonic(self):
        # The reduction ASCII-normalizes ♯/♭ before parsing, so a unicode-accidental TONIC
        # grades identically to its ASCII spelling. (The OI-132 fold dropped this
        # normalization from the graded path; restored with the OI-155 abstain fix.)
        self.assertEqual(crn._our_key_tonic("F♯maj"), crn._our_key_tonic("F#maj"))
        self.assertEqual(crn._our_key_tonic("F♯maj"), (6, True))
        self.assertEqual(crn._our_key_tonic("B♭min"), (10, False))

    def test_dcml_key_tonic(self):
        self.assertEqual(crn._dcml_key_tonic("C"), (0, True))    # uppercase = major
        self.assertEqual(crn._dcml_key_tonic("c"), (0, False))   # lowercase = minor
        self.assertEqual(crn._dcml_key_tonic("f#"), (6, False))
        self.assertEqual(crn._dcml_key_tonic("Bb"), (10, True))
        self.assertEqual(crn._dcml_key_tonic(""), (None, None))


# ════════════════════════════════════════════════════════════════════════════
# The grader's mode table vs the PRODUCER's emitted vocabulary (OI-155).
#
# The grader must READ the producer's vocabulary, not re-decide it (#6, the fact-publication
# corollary), and an emitted mode it cannot place must ABSTAIN, not default to minor (OI-33).
# Prose cannot enforce either property, so this test PARSES the two producing sources —
#   src/composing/analysis/key/keymodeformatting.cpp   keyModeSuffix()   (the 21 spellings)
#   src/composing/analysis/key/keymodeanalyzer.h       keyModeIsMajor()  (their maj/min partition)
# — and asserts compare_rn's table is COMPLETE and FAITHFUL to them. If a 22nd mode is added to
# the producer, or an existing one is respelled or re-classified, this test goes red instead of
# the new mode silently abstaining (or, before OI-155, silently grading as minor).
# ════════════════════════════════════════════════════════════════════════════

_SRC_KEY_DIR = _TOOLS_DIR.parent / "src" / "composing" / "analysis" / "key"

# The five dominant-family exotics: graded by the OI-132 parent-collection reduction (user-ruled
# 2026-07-13) INSTEAD of by the producer's major/minor partition — that is the whole point of the
# ruling, so they are excluded from the faithfulness comparison and checked separately.
_EXOTIC_PRODUCER_MODES = {"PhrygianDominant", "MixolydianB6", "LydianDominant",
                          "LydianAugmented", "Altered"}


# The producer sources are parsed by ONE reader — tools/producer_key_modes.py (OI-157). The two
# parsers this test used to hold are folded onto it; the shared reader is also what
# measure_joint_probe uses to resolve a KeySigMode integer to the suffix it prints. The test stays
# an INDEPENDENT check of compare_rn's table: the reader reports what the producer emits,
# compare_rn holds the hand-checked mirror, and the two are compared here.


class TestModeVocabularyMatchesProducer(unittest.TestCase):

    def setUp(self):
        self.suffixes = pkm.mode_suffixes()
        self.major_modes = pkm.major_mode_names()

    def test_producer_emits_the_expected_number_of_modes(self):
        # KEY_MODE_COUNT in keymodeanalyzer.h is the producer's own declared total.
        header = (_SRC_KEY_DIR / "keymodeanalyzer.h").read_text(encoding="utf-8")
        declared = int(re.search(r"KEY_MODE_COUNT\s*=\s*(\d+)", header).group(1))
        self.assertEqual(len(self.suffixes), declared)
        self.assertEqual(len(self.major_modes), 9)   # the major-third modes

    def test_the_enum_order_join_covers_every_emitted_mode(self):
        """OI-157: the (mode integer -> suffix) join through which measure_joint_probe grades a
        carried key. Every KeySigMode enumerator must have a keyModeSuffix() case, and the join
        must be exactly as long as the producer's declared count — otherwise a mode integer coming
        out of batch_analyze would index past the table, or onto the wrong mode."""
        self.assertEqual(len(pkm.suffix_by_enum_index()), len(self.suffixes))
        self.assertEqual(len(pkm.mode_names_in_enum_order()), len(self.suffixes))
        # The DECLARATION order is what the C++ casts to int — pin both ends of it.
        self.assertEqual(pkm.mode_names_in_enum_order()[0], "Ionian")
        self.assertEqual(pkm.suffix_by_enum_index()[0], "maj")
        self.assertEqual(pkm.mode_names_in_enum_order()[-1], "AlteredDomBB7")
        self.assertEqual(pkm.suffix_by_enum_index()[-1], "altDom")

    def test_every_emitted_mode_is_classified(self):
        """COMPLETENESS: no mode the producer can emit falls through to the abstain path."""
        for name, suffix in sorted(self.suffixes.items()):
            with self.subTest(mode=name, suffix=suffix):
                if name in _EXOTIC_PRODUCER_MODES:
                    ascii_suffix = crn._ascii_accidentals(suffix)
                    self.assertIn(ascii_suffix, crn._KB_PARENT_COLLECTION_MODES)
                else:
                    self.assertIsNotNone(
                        crn._mode_class(suffix),
                        f"producer mode {name} ('{suffix}') is in NEITHER grader set — it would "
                        f"ABSTAIN on the mode axis. Add it to _KB_MAJOR_MODES/_KB_MINOR_MODES.")

    def test_classification_is_faithful_to_the_producer(self):
        """FAITHFULNESS: for every non-exotic mode, the grader's class == keyModeIsMajor()."""
        for name, suffix in sorted(self.suffixes.items()):
            if name in _EXOTIC_PRODUCER_MODES:
                continue
            with self.subTest(mode=name, suffix=suffix):
                self.assertEqual(crn._mode_class(suffix), name in self.major_modes)

    def test_the_exotic_five_are_exactly_the_parent_collection_set(self):
        """The OI-132 ruling covers exactly these five producer modes — no more, no fewer."""
        ascii_exotics = {crn._ascii_accidentals(self.suffixes[n]) for n in _EXOTIC_PRODUCER_MODES}
        self.assertEqual(ascii_exotics, set(crn._KB_PARENT_COLLECTION_MODES))

    def test_the_grader_sets_contain_no_mode_the_producer_cannot_emit(self):
        """No invented entries: every grader-set suffix is one the producer actually emits."""
        emitted = {crn._ascii_accidentals(s).lower() for s in self.suffixes.values()}
        self.assertTrue(crn._KB_MAJOR_MODES <= emitted, crn._KB_MAJOR_MODES - emitted)
        self.assertTrue(crn._KB_MINOR_MODES <= emitted, crn._KB_MINOR_MODES - emitted)


if __name__ == "__main__":
    unittest.main(verbosity=2)

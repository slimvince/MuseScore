#!/usr/bin/env python3
"""
test_metric_scripts.py — pins the de-facto metric definitions implemented by the
three Python comparison scripts the whole project is judged by:

  * tools/compare_analyses.py   — align_regions / align_dcml_regions (the
                                  lenient-OR time-overlap comparator everything
                                  reuses), classify(), three_way_classify().
  * tools/characterise_bir_false.py — the BIR=false residual classifier
                                  (chord_disagree ∧ ¬bassIsRoot ∧
                                  music21_dcml_agree) and the delta convention.
  * tools/compare_rn.py         — the Roman-numeral classifier, including the
                                  2026-06-04 key_disagree / quality_disagree
                                  split fix, the normalization rules, and the
                                  coarse extract_quality() token.

Every expected value here is derived BY HAND; the derivations live in
tools/tests/fixtures/README.md and in inline comments.  A metric-definition
change must now fail one of these tests rather than silently re-baselining.

NOTE (Stage 1d hard constraint): the scripts under test are NOT modified by this
file.  Where a test pins behavior that looks suspect, it is marked
``pins current (suspect) behavior`` and called out in cc_stage1d_report.md §4.
Metric definitions only change by explicit decision.

Run (no pytest in the venv — use unittest):
    cd C:\\s\\MS && python -m unittest discover -s tools/tests -p "test_*.py" -v
or:
    cd C:\\s\\MS && python tools/tests/test_metric_scripts.py
"""

from __future__ import annotations

import io
import json
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

import sys

_THIS_DIR  = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent
_FIX       = _THIS_DIR / "fixtures"
sys.path.insert(0, str(_TOOLS_DIR))

import compare_analyses as cmp        # noqa: E402
import compare_rn as crn              # noqa: E402
import dcml_parser as dcml            # noqa: E402
import characterise_bir_false as cbf  # noqa: E402
import run_bach_preset as rbp         # noqa: E402


# ── small builders ──────────────────────────────────────────────────────────

def R(root_pc, rn="I", quality="Major", *, start=0, end=480, dur=1.0,
      measure=1, beat=1.0, bass_pc=None, bass_is_root=None, alternatives=None,
      key="C major"):
    """Construct an analyzer Region with only the fields the comparators read."""
    return cmp.Region(
        measure_number=measure, beat=beat, start_tick=start, end_tick=end,
        duration=dur, root_pc=root_pc, quality=quality, chord_symbol="x",
        roman_numeral=rn, key=key, key_confidence=0.9, diatonic_to_key=True,
        alternatives=alternatives or [],
        bass_pc=bass_pc, bass_is_root=bass_is_root,
    )


def D(root_pc, chord, numeral=None, *, measure=1, beat=1.0):
    """Construct a DcmlRegion directly (root_pc supplied, not recomputed)."""
    return dcml.DcmlRegion(
        measure_number=measure, beat=beat, global_key="C", local_key="C",
        chord_symbol=chord, roman_numeral=numeral if numeral is not None else chord,
        root_pc=root_pc,
    )


# ════════════════════════════════════════════════════════════════════════════
# 1.  align_regions — the lenient-OR ≥50% time-overlap rule (music21 side)
# ════════════════════════════════════════════════════════════════════════════

class TestAlignRegions(unittest.TestCase):
    """The comparator rule: for each of OUR regions pick the THEIRS region with
    the largest tick overlap; aligned iff overlap ≥50% of *either* side's
    duration (lenient OR).  Verified by probe run, not docstring."""

    def _aligned(self, ours, theirs):
        return cmp.align_regions(ours, theirs)[0][1] is not None

    def test_overlap_exactly_50pct_of_our_aligns(self):
        # our [0,100) dur 100; their [50,200) overlap 50 -> 50% of our (>=) -> aligned
        self.assertTrue(self._aligned([R(0, start=0, end=100)],
                                      [R(0, start=50, end=200)]))

    def test_overlap_below_50pct_both_sides_does_not_align(self):
        # our [0,100) their [51,200): overlap 49 -> our 49%, their 49/149≈33% -> no
        self.assertFalse(self._aligned([R(0, start=0, end=100)],
                                       [R(0, start=51, end=200)]))

    def test_lenient_or_fully_contained_their_region_aligns(self):
        # our [0,100) their [0,49): our-side 49% (<50) BUT their-side 49/49=100%
        # -> OR clause keeps it aligned.
        self.assertTrue(self._aligned([R(0, start=0, end=100)],
                                      [R(0, start=0, end=49)]))

    def test_lenient_or_subbeat_contained_in_their_region_aligns(self):
        # our [60,100) dur 40 fully inside their [0,200): our-side 100% -> aligned
        self.assertTrue(self._aligned([R(0, start=60, end=100)],
                                      [R(0, start=0, end=200)]))

    def test_multi_candidate_picks_max_overlap(self):
        # our [0,100); A [0,30) ov30, B [30,100) ov70 -> B wins
        winner = cmp.align_regions([R(0, start=0, end=100)],
                                   [R(0, start=0, end=30),
                                    R(1, start=30, end=100)])[0][1]
        self.assertIsNotNone(winner)
        self.assertEqual(winner.end_tick, 100)
        self.assertEqual(winner.root_pc, 1)

    def test_zero_length_our_region_never_aligns(self):
        # our_dur == 0 fails the `our_dur > 0` guard
        self.assertFalse(self._aligned([R(0, start=50, end=50)],
                                       [R(0, start=0, end=100)]))

    def test_no_overlap_unaligned(self):
        self.assertFalse(self._aligned([R(0, start=0, end=100)],
                                       [R(0, start=200, end=300)]))

    def test_empty_theirs_unaligned(self):
        self.assertFalse(self._aligned([R(0, start=0, end=100)], []))


# ════════════════════════════════════════════════════════════════════════════
# 2.  classify — the music21 agreement buckets
# ════════════════════════════════════════════════════════════════════════════

class TestClassify(unittest.TestCase):

    def test_full_agree(self):
        c = cmp.classify(R(0, "I"), R(0, "I"))
        self.assertEqual(c.category, "full_agree")

    def test_chord_agree_rn_differs_same_key(self):
        # same root+quality, different RN base, same key tonic -> rn_differs
        c = cmp.classify(R(0, "I"), R(0, "VI"))
        self.assertEqual(c.category, "chord_agree_rn_differs")

    def test_chord_disagree_root_differs(self):
        c = cmp.classify(R(0, "I"), R(7, "V"))
        self.assertEqual(c.category, "chord_disagree")

    def test_near_agree_matches_alternative(self):
        ours = R(0, "I", alternatives=[{"rootPitchClass": 7, "quality": "Major"}])
        c = cmp.classify(ours, R(7, "V"))
        self.assertEqual(c.category, "near_agree")

    def test_unaligned_when_theirs_none(self):
        self.assertEqual(cmp.classify(R(0, "I"), None).category, "unaligned")


# ════════════════════════════════════════════════════════════════════════════
# 3.  three_way_classify — ours / music21 / DCML root-pc agreement
#     (the pitch-class–based core; enharmonic spellings collapse by pc).
# ════════════════════════════════════════════════════════════════════════════

class TestThreeWayClassify(unittest.TestCase):

    def test_all_agree(self):
        self.assertEqual(cmp.three_way_classify(0, 0, 0), "all_agree")

    def test_dcml_ours_agree_m21_wrong(self):
        self.assertEqual(cmp.three_way_classify(5, 9, 5), "dcml_ours_agree")

    def test_music21_dcml_agree_we_wrong(self):
        self.assertEqual(cmp.three_way_classify(7, 0, 0), "music21_dcml_agree")

    def test_all_differ(self):
        self.assertEqual(cmp.three_way_classify(7, 5, 0), "all_differ")

    def test_no_dcml_when_dcml_none(self):
        self.assertEqual(cmp.three_way_classify(0, 0, None), "no_dcml")

    def test_no_dcml_when_ours_or_theirs_none(self):
        self.assertEqual(cmp.three_way_classify(None, 0, 0), "no_dcml")
        self.assertEqual(cmp.three_way_classify(0, None, 0), "no_dcml")

    def test_enharmonic_root_collapses_to_pc(self):
        # The metric is purely pitch-class based: a DCML "bII" in C resolves to
        # pc 1 (Db == C#), so an analyzer root_pc of 1 agrees regardless of how
        # either side would *spell* the note.  This is the pc-vs-spelling point.
        self.assertEqual(dcml._compute_root_pc("bII", "C"), 1)
        self.assertEqual(cmp.three_way_classify(1, 1, 1), "all_agree")


# ════════════════════════════════════════════════════════════════════════════
# 4.  align_dcml_regions — DCML (measure,beat) → tick conversion + lenient-OR
# ════════════════════════════════════════════════════════════════════════════

class TestAlignDcmlRegions(unittest.TestCase):
    """ours regions all dur=1.0 over 480 ticks => inferred tpb = 480; measure 1
    anchored at tick 0.  DCML beats 1..4 -> ticks 0/480/960/1440, spans
    [0,480) [480,960) [960,1440) [1440,1920).  Each of our 4 regions overlaps
    exactly one span -> 1:1 mapping.  Derivation in fixtures/README.md."""

    def setUp(self):
        self.ours = [
            R(0, start=0,    end=480,  measure=1, beat=1.0),
            R(0, start=480,  end=960,  measure=1, beat=2.0),
            R(0, start=960,  end=1440, measure=1, beat=3.0),
            R(0, start=1440, end=1920, measure=1, beat=4.0),
        ]
        # DcmlRegions carry only (measure,beat,root_pc); root_pc set explicitly.
        self.dcml = [
            D(0, "I",  measure=1, beat=1.0),
            D(7, "V",  measure=1, beat=2.0),
            D(5, "IV", measure=1, beat=3.0),
            D(11, "vii", measure=1, beat=4.0),
        ]

    def test_one_to_one_overlap_mapping(self):
        matches = cmp.align_dcml_regions(self.ours, self.dcml)
        self.assertEqual([m.root_pc if m else None for m in matches],
                         [0, 7, 5, 11])

    def test_subbeat_region_contained_aligns_lenient_or(self):
        # add a half-beat region [240,480) inside DCML span [0,480): our-side
        # overlap 240/240 = 100% -> aligned to the "I" span.
        ours = self.ours + [R(0, start=240, end=480, measure=1, beat=1.5, dur=0.5)]
        matches = cmp.align_dcml_regions(ours, self.dcml)
        self.assertIsNotNone(matches[-1])
        self.assertEqual(matches[-1].root_pc, 0)

    def test_beat_snap_legacy_mode(self):
        # Legacy beat-snap: smallest |Δbeat| within same measure, tol 0.5.
        matches = cmp.align_dcml_regions(self.ours, self.dcml, mode="beat-snap")
        self.assertEqual([m.root_pc if m else None for m in matches],
                         [0, 7, 5, 11])


# ════════════════════════════════════════════════════════════════════════════
# 5.  compare_rn — normalization + the coarse extract_quality token
# ════════════════════════════════════════════════════════════════════════════

class TestCompareRnNormalisation(unittest.TestCase):

    def test_key_prefix_stripped(self):
        self.assertEqual(crn.normalise_rn("[C:]I"), "I")

    def test_modulation_marker_stripped(self):
        self.assertEqual(crn.normalise_rn("→V"), "V")
        self.assertEqual(crn.normalise_rn(">V"), "V")

    def test_halfdim_sigil_percent_to_oslash(self):
        self.assertEqual(crn.normalise_rn("ii%65"), "iiø65")

    def test_paren_figured_bass_stripped(self):
        self.assertEqual(crn.normalise_rn("V(4)"), "V")
        self.assertEqual(crn.normalise_rn("V(#11)"), "V")

    def test_split_rn_keeps_case(self):
        self.assertEqual(crn.split_rn("V7"), ("", "V", "7"))
        self.assertEqual(crn.split_rn("vi65"), ("", "vi", "65"))
        self.assertEqual(crn.split_rn("bII6"), ("b", "II", "6"))


class TestExtractQuality(unittest.TestCase):
    """Coarse chord-quality token.  Several entries pin SUSPECT behavior — see
    cc_stage1d_report.md §4.  Verified by probe run on the real corpus
    convention (DCML and ours both use the letter 'o' for diminished)."""

    def test_basic_triads(self):
        self.assertEqual(crn.extract_quality("I"), "Maj")
        self.assertEqual(crn.extract_quality("i"), "Min")

    def test_seventh_figures(self):
        self.assertEqual(crn.extract_quality("V7"), "Dom7")
        self.assertEqual(crn.extract_quality("IVM7"), "Maj7")
        self.assertEqual(crn.extract_quality("vi65"), "Min7")

    def test_halfdim_via_normalised_sigil(self):
        self.assertEqual(crn.extract_quality(crn.normalise_rn("ii%65")), "HalfDim7")
        self.assertEqual(crn.extract_quality("viø7"), "HalfDim7")

    def test_augmented_plus_recognised(self):
        self.assertEqual(crn.extract_quality("IV+6"), "Aug")

    def test_letter_o_diminished_is_recognised(self):
        # re-pinned 2026-06-10: intentional metric correction (Stage 2.2-ii;
        # dossier §4).  F-1: extract_quality now keys diminished off BOTH the
        # degree-sign '°' (U+00B0) AND the letter 'o' that DCML and our analyzer
        # actually emit (viio6 / iio65).  Previously 'o'-diminished chords were
        # mis-coarse-classified Min / Min7, collapsing the dim-vs-min distinction
        # in the disagreement bucket.  Both the viio6 (triad) and iio65 (seventh)
        # shapes are now correct.
        self.assertEqual(crn.extract_quality("viio6"), "Dim")     # was "Min"
        self.assertEqual(crn.extract_quality("viio7"), "Dim7")    # was "Min7"
        self.assertEqual(crn.extract_quality("iio65"), "Dim7")    # was "Min7"

    def test_degree_sign_diminished_still_recognised(self):
        # The '°' branch is unchanged by the F-1 fix (kept alongside the new 'o'
        # branch).  Pinned so the letter-'o' addition does not regress it.
        self.assertEqual(crn.extract_quality("vii°7"), "Dim7")
        self.assertEqual(crn.extract_quality("vii°"), "Dim")

    def test_augmented_sixth_and_neapolitan_unparseable(self):
        # re-pinned 2026-06-10: intentional metric correction (Stage 2.2-ii;
        # dossier §4).  F-2: 'Ger65'/'N6' still have no Roman-degree token the
        # regex accepts -> '?'.  'It6' (Italian augmented sixth) used to match
        # degree 'I' and mis-read as a major tonic; it is now routed to the same
        # unparseable -> root-only fallback (split_rn returns None), so its coarse
        # quality is '?'.
        self.assertEqual(crn.extract_quality("Ger65"), "?")
        self.assertEqual(crn.extract_quality("N6"), "?")
        self.assertEqual(crn.extract_quality("It6"), "?")    # was "Maj" (mis-parsed as 'I')
        self.assertEqual(crn.extract_quality("It"), "?")     # bare Italian-sixth token
        self.assertEqual(crn.extract_quality("It6/ii"), "?") # tonicised variant

    def test_split_rn_routes_it6_to_unparseable(self):
        # re-pinned 2026-06-10: intentional metric correction (Stage 2.2-ii;
        # dossier §4).  split_rn now returns None for the Italian augmented-sixth
        # token so It6 takes the unparseable branch in classify_pair, exactly
        # like Ger/Fr/N.  Genuine tonic degrees ('I', 'I6', 'i') are unaffected.
        self.assertIsNone(crn.split_rn("It6"))
        self.assertIsNone(crn.split_rn("It"))
        self.assertIsNone(crn.split_rn("It6/ii"))
        self.assertEqual(crn.split_rn("I"),  ("", "I", ""))
        self.assertEqual(crn.split_rn("I6"), ("", "I", "6"))
        self.assertEqual(crn.split_rn("i"),  ("", "i", ""))


# ════════════════════════════════════════════════════════════════════════════
# 6.  compare_rn.classify_pair — the five buckets + the 2026-06-04 split
# ════════════════════════════════════════════════════════════════════════════

class TestClassifyPair(unittest.TestCase):

    def test_exact(self):
        self.assertEqual(crn.classify_pair(R(0, "I"), D(0, "I")).category, "exact")

    def test_partial_inversion_differs(self):
        # root + degree-case match, inversion/extension differs -> partial
        self.assertEqual(crn.classify_pair(R(0, "I"), D(0, "I6")).category, "partial")
        self.assertEqual(crn.classify_pair(R(7, "V7"), D(7, "V")).category, "partial")

    def test_root_err(self):
        self.assertEqual(crn.classify_pair(R(2, "ii"), D(7, "V")).category, "root_err")

    def test_key_disagree_is_the_V_to_I_shape(self):
        # REGRESSION PIN for the 2026-06-04 fix: root matches (both pc 7),
        # degree token differs (V vs I) but the COARSE quality matches (both
        # uppercase triads -> 'Maj'), so this is a key/mode-context difference,
        # NOT a chord-quality error.  The OLD single-bucket classifier counted
        # this as a quality error; it must now be key_disagree.
        self.assertEqual(crn.classify_pair(R(7, "V"), D(7, "I")).category,
                         "key_disagree")

    def test_quality_disagree_true_quality_error(self):
        # root matches, degree case differs AND coarse quality differs
        # (Maj vs Min) -> a genuine chord-quality error.
        self.assertEqual(crn.classify_pair(R(7, "V"), D(7, "v")).category,
                         "quality_disagree")
        self.assertEqual(crn.classify_pair(R(7, "V"), D(7, "i")).category,
                         "quality_disagree")

    def test_unparseable_falls_back_to_root_only(self):
        # 'Ger65' is unparseable -> root-only: same root -> partial; diff -> root_err
        self.assertEqual(crn.classify_pair(R(7, "V"), D(7, "Ger65")).category,
                         "partial")
        self.assertEqual(crn.classify_pair(R(2, "V"), D(7, "Ger65")).category,
                         "root_err")

    def test_it6_routes_to_root_only_fallback(self):
        # re-pinned 2026-06-10: intentional metric correction (Stage 2.2-ii;
        # dossier §4).  It6 now follows the SAME unparseable -> root-only path as
        # Ger/Fr/N rather than being scored as a fabricated 'Maj' tonic.  The
        # DCML-side root_pc is whatever dcml_parser resolves (supplied here);
        # same root -> partial, different root -> root_err.
        self.assertEqual(crn.classify_pair(R(7, "V"), D(7, "It6")).category,
                         "partial")
        self.assertEqual(crn.classify_pair(R(2, "V"), D(7, "It6")).category,
                         "root_err")

    def test_none_dcml_returns_none(self):
        self.assertIsNone(crn.classify_pair(R(0, "I"), None))

    def test_none_dcml_rootpc_returns_none(self):
        self.assertIsNone(crn.classify_pair(R(0, "I"), D(None, "I")))


# ════════════════════════════════════════════════════════════════════════════
# 7.  compare_rn.score_piece — end-to-end on the 9-row fixture
#     Hand-derived totals (see fixtures/README.md):
#       matched=9  exact=5  partial=1  key_disagree=1  quality_disagree=1
#       root_err=1   root_aligned=9  root_agree=8
#     Sum invariant: key_disagree + quality_disagree == old quality_err == 2.
# ════════════════════════════════════════════════════════════════════════════

class TestScorePiece(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stats = crn.score_piece(_FIX / "rn" / "probe_rn.ours.json",
                                    _FIX / "rn" / "probe_rn.harmonies.tsv")

    def test_loaded(self):
        self.assertIsNotNone(self.stats)

    def test_bucket_counts(self):
        s = self.stats
        self.assertEqual(
            (s.matched, s.exact, s.partial, s.key_disagree,
             s.quality_disagree, s.root_err),
            (9, 5, 1, 1, 1, 1))

    def test_buckets_partition_matched(self):
        s = self.stats
        self.assertEqual(
            s.exact + s.partial + s.key_disagree + s.quality_disagree + s.root_err,
            s.matched)

    def test_split_sum_invariant_equals_old_quality_err(self):
        # The 2026-06-04 fix split a single bucket; the sum is conserved.
        # old "quality_err" = #(root matches AND degree token differs) = 2.
        s = self.stats
        self.assertEqual(s.key_disagree + s.quality_disagree, 2)

    def test_root_agree_parity(self):
        # root_agree (8/9) is computed independently of rn_agree (6/9):
        # the V→I key_disagree pair has root_agree=True but is not rn-exact.
        s = self.stats
        self.assertEqual((s.root_aligned, s.root_agree), (9, 8))
        self.assertEqual(s.exact + s.partial, 6)  # rn_agree

    def test_determinism(self):
        again = crn.score_piece(_FIX / "rn" / "probe_rn.ours.json",
                                _FIX / "rn" / "probe_rn.harmonies.tsv")
        s = self.stats
        self.assertEqual(
            (again.matched, again.exact, again.partial, again.key_disagree,
             again.quality_disagree, again.root_err,
             again.root_aligned, again.root_agree),
            (s.matched, s.exact, s.partial, s.key_disagree,
             s.quality_disagree, s.root_err, s.root_aligned, s.root_agree))


# ════════════════════════════════════════════════════════════════════════════
# 8.  compare_analyses.load_analysis — JSON field-mapping contract
# ════════════════════════════════════════════════════════════════════════════

class TestLoadAnalysisContract(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.meta, cls.regions = cmp.load_analysis(
            _FIX / "align" / "contract.ours.json")

    def test_single_region(self):
        self.assertEqual(len(self.regions), 1)

    def test_field_mapping(self):
        r = self.regions[0]
        # JSON camelCase -> dataclass snake_case mapping is the contract.
        self.assertEqual(r.root_pc, 9)              # rootPitchClass
        self.assertEqual(r.bass_pc, 0)              # bassPitchClass
        self.assertEqual(r.bass_is_root, False)     # bassIsRoot
        self.assertEqual(r.note_count, 3)           # noteCount
        self.assertEqual(r.pitch_class_set, 529)    # pitchClassSet
        self.assertAlmostEqual(r.chord_score, 3.17)
        self.assertAlmostEqual(r.chord_score_margin, 0.42)
        self.assertEqual(r.roman_numeral, "vi6")
        self.assertEqual(r.start_tick, 1200)
        self.assertEqual(r.end_tick, 1680)
        self.assertEqual(r.key_runner_up, {"key": "A minor", "confidence": 0.40})
        self.assertEqual(len(r.alternatives), 1)


# ════════════════════════════════════════════════════════════════════════════
# 9.  characterise_bir_false — the BIR=false residual classifier + delta
#     Run main() against the fixture corpus by pointing its module globals at
#     fixtures/bir_corpus and stubbing find_wir_file.  Hand-derived:
#       R0 (beat1): chord_disagree, bassIsRoot=False, music21+DCML agree (pc0)
#                   -> COUNTED, delta = (7-0)%12 = 7
#       R1 (beat2): music21_dcml_agree BUT bassIsRoot=True -> EXCLUDED
#       R2 (beat3): chord_disagree but dcml_ours_agree (we're right) -> EXCLUDED
#       R3 (beat4): full_agree (pc1=Db, all three agree) -> EXCLUDED
#     => TOTAL genuine BIR=false = 1, delta histogram {7: 1}.
# ════════════════════════════════════════════════════════════════════════════

class TestCharacteriseBirFalse(unittest.TestCase):

    def _run_main(self):
        corpus = _FIX / "bir_corpus"
        wir_txt = str(corpus / "probe01.wir.txt")

        def fake_find_wir(base, stem):
            return wir_txt if stem == "probe01" else None

        # Exercise run() directly (the classification logic); manifest validation
        # is covered separately in TestCorpusManifestValidation.
        buf = io.StringIO()
        with mock.patch("dcml_parser.find_wir_file", side_effect=fake_find_wir), \
             redirect_stdout(buf):
            cbf.run(corpus, corpus)
        return buf.getvalue()

    def test_total_bir_false_is_one(self):
        out = self._run_main()
        self.assertIn("TOTAL genuine BIR=false: 1", out)

    def test_delta_histogram_has_only_delta_7(self):
        out = self._run_main()
        # The only counted residual is delta=+7 with count 1.
        self.assertRegex(out, r"\+\s*7\s+1\s+")
        # No delta=+5 / +2 / +8 lines should appear (those were the real corpus).
        self.assertNotRegex(out, r"\+\s*8\s+\d")

    def test_processed_one_score_with_wir(self):
        out = self._run_main()
        self.assertIn("Processed 1 scores (1 with WiR coverage) -> 1", out)

    def test_main_validates_manifest_then_runs(self):
        # End-to-end via main(): the fixture dir carries a valid corpus_manifest.json,
        # so validation passes and the same BIR=false=1 result is produced.
        corpus = _FIX / "bir_corpus"
        wir_txt = str(corpus / "probe01.wir.txt")
        buf = io.StringIO()
        with mock.patch("dcml_parser.find_wir_file",
                        side_effect=lambda b, s: wir_txt if s == "probe01" else None), \
             redirect_stdout(buf):
            cbf.main(["--corpus-dir", str(corpus), "--wir-dir", str(corpus)])
        out = buf.getvalue()
        self.assertIn("Corpus OK: preset=Baroque", out)
        self.assertIn("TOTAL genuine BIR=false: 1", out)


# ════════════════════════════════════════════════════════════════════════════
# 10.  Stage 2.2a — corpus manifest write (run_bach_preset) + validate
#      (characterise_bir_false). The M3 contamination scenario must now ERROR
#      rather than silently mis-count.
# ════════════════════════════════════════════════════════════════════════════

class TestCorpusManifestValidation(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def _write_ours(self, stem, body='{"meta":{},"regions":[]}'):
        p = self.dir / f"{stem}.ours.json"
        p.write_text(body, encoding="utf-8")
        return p

    def _build_manifest(self, preset, stems, expected_count=None):
        for s in stems:
            self._write_ours(s)
        status = {s: "OK" for s in stems}
        return rbp._write_manifest(
            self.dir, preset, status,
            expected_count=expected_count if expected_count is not None else len(stems),
            git_hash="t", timestamp="t", exe=None)

    # ── manifest writer ──────────────────────────────────────────────────────

    def test_write_manifest_records_fingerprints_and_complete(self):
        m = self._build_manifest("Baroque", ["bwv1", "bwv2"])
        self.assertTrue(m["complete"])
        self.assertEqual(m["ours_count"], 2)
        self.assertIn("sha256", m["scores"]["bwv1"])
        self.assertEqual(m["preset"], "Baroque")

    def test_write_manifest_incomplete_when_status_failed(self):
        # one OK file present, one FAILED -> not complete (the fail-loud trigger)
        self._write_ours("bwv1")
        m = rbp._write_manifest(self.dir, "Jazz",
                                {"bwv1": "OK", "bwv2": "FAILED"},
                                expected_count=2, git_hash="t", timestamp="t", exe=None)
        self.assertFalse(m["complete"])
        self.assertEqual(m["ours_count"], 1)

    # ── validator: happy path ────────────────────────────────────────────────

    def test_validate_accepts_complete_clean_corpus(self):
        self._build_manifest("Baroque", ["bwv1", "bwv2"])
        m = cbf.validate_corpus_dir(self.dir)
        self.assertEqual(m["preset"], "Baroque")

    # ── validator: failure modes ─────────────────────────────────────────────

    def test_validate_rejects_missing_manifest(self):
        self._write_ours("bwv1")
        with self.assertRaises(cbf.CorpusValidationError):
            cbf.validate_corpus_dir(self.dir)

    def test_validate_rejects_incomplete_corpus(self):
        # manifest declares 3 expected but only 2 OK -> incomplete
        self._build_manifest("Baroque", ["bwv1", "bwv2"], expected_count=3)
        with self.assertRaises(cbf.CorpusValidationError) as ctx:
            cbf.validate_corpus_dir(self.dir)
        self.assertIn("INCOMPLETE", str(ctx.exception))

    def test_validate_rejects_contamination_by_overwrite(self):
        # The exact M3 scenario: a foreign-preset file overwrites a listed score,
        # so its fingerprint no longer matches the manifest.
        self._build_manifest("Jazz", ["bwv1", "bwv2"])
        (self.dir / "bwv1.ours.json").write_text(
            '{"meta":{},"regions":[{"x":1}]}', encoding="utf-8")  # different bytes
        with self.assertRaises(cbf.CorpusValidationError) as ctx:
            cbf.validate_corpus_dir(self.dir)
        self.assertIn("CONTAMINATION", str(ctx.exception))

    def test_validate_rejects_extra_unlisted_file(self):
        # A foreign .ours.json with a stem absent from the manifest.
        self._build_manifest("Jazz", ["bwv1", "bwv2"])
        self._write_ours("bwv_intruder")
        with self.assertRaises(cbf.CorpusValidationError) as ctx:
            cbf.validate_corpus_dir(self.dir)
        self.assertIn("CONTAMINATION", str(ctx.exception))

    def test_validate_rejects_missing_ours_file(self):
        # manifest lists a score whose .ours.json was deleted post-write
        self._build_manifest("Baroque", ["bwv1", "bwv2"])
        (self.dir / "bwv2.ours.json").unlink()
        with self.assertRaises(cbf.CorpusValidationError):
            cbf.validate_corpus_dir(self.dir)


if __name__ == "__main__":
    unittest.main(verbosity=2)

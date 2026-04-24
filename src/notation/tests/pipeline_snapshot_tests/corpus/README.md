# pipeline_snapshot_tests corpus

Phase 1b of the unified-pipeline refactor
(`docs/unified_analysis_pipeline.md`). This harness pins the current
user-facing output of paths P1 (Implode), P2 (Annotation), P3 (Tick-regional),
and P4 (Tick-local) before Phase 2+ starts moving analysis code around.

All scores are linked by path into the DCML corpora that already live in
`tools/dcml/`. Nothing is copied; if the DCML directories are ever moved, the
paths in `pipeline_snapshot_tests.cpp::kCorpus[]` need updating.

## Runtime cap

To keep CI time bounded, each score is analysed only up to
`kMaxAnalysisMeasures = 16` opening measures. That window is enough to exercise
each analysis path on every corpus entry (chorales are typically ~12 measures
and exposition heads of the sonatas comfortably fit) while keeping full-corpus
runtime under a minute. Phase 2+ can widen the cap once it has a reason to.

## The 10 scores

| # | ID                          | Source                                                                     | Why this slot                                                                                                                                                  |
|---|-----------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | `bach_chorale_001`          | `bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx`                     | SATB baseline — dense 4-voice functional-tonal writing, the densest shared fixture the analyzer is tuned against.                                               |
| 2 | `bach_chorale_003`          | `bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx`              | Second Bach chorale — modal colouring and a different cadence profile give an independent chorale observation.                                                  |
| 3 | `bach_bwv806_prelude`       | `bach_en_fr_suites/MS3/BWV806_01_Prelude.mscx`                             | Substitute for the two-voice invention slot (DCML has no WTC inventions). Keyboard prelude covers contrapuntal keyboard texture.                                |
| 4 | `bach_bwv806_gigue`         | `bach_en_fr_suites/MS3/BWV806_10_Gigue.mscx`                               | Substitute for the fugue slot (DCML has no WTC fugues). Gigue gives dance-form imitative entries.                                                               |
| 5 | `mozart_k279_1`             | `mozart_piano_sonatas/MS3/K279-1.mscx`                                     | Classical piano sonata exposition — already a chord-analyzer fixture (§4.1c).                                                                                   |
| 6 | `mozart_k280_1`             | `mozart_piano_sonatas/MS3/K280-1.mscx`                                     | Substitute for the Haydn string quartet slow-movement slot (DCML has no Haydn). Second Mozart exposition widens the Classical sample.                          |
| 7 | `chopin_bi105_op30_1`       | `chopin_mazurkas/MS3/BI105-1op30-1.mscx`                                   | Substitute for the Chopin prelude slot (DCML has mazurkas but no preludes). Romantic harmonic language with dance-rhythm phrase structure.                      |
| 8 | `chopin_bi105_op30_2`       | `chopin_mazurkas/MS3/BI105-2op30-2.mscx`                                   | Substitute for the Brahms intermezzo slot (DCML has no Brahms). Adds modulation and chromatic colour on top of a second Romantic sample.                        |
| 9 | `corelli_op01n08a`          | `corelli/MS3/op01n08a.mscx`                                                | Cadence-heavy Baroque ground already used in `notationimplode_tests` as a known-good fixture for classical-path regression work.                                |
| 10 | `schumann_kinderszenen_n01` | `schumann_kinderszenen/MS3/n01.mscx`                                       | Fills the sub-beat-passing-harmony slot. See below — this category is under-represented in Phase 1.                                                              |

## Known under-representation

The prompt's "sub-beat passing harmony" and "ambiguous cadence" categories are
deliberately under-represented in the Phase 1 corpus. Synthetic fixtures in
those categories fail to clear the analyzer's 0.8 assertive-confidence gate, so
a handcrafted score would report no cadences or no stable key and produce a
less useful snapshot than natural-corpus material. Schumann's Kinderszenen
No. 1 covers *some* of this ground (the opening has ornaments and passing
figures that exercise Pass 0 onset sub-boundaries), but Phase 2+ should add
targeted synthetic fixtures once the analyzer's assertive-confidence thresholds
are refactored or when a real-corpus sub-beat example becomes available.

Brahms, Haydn, and the WTC fugues/inventions are absent from the DCML corpus
as shipped; they would need separate fixture copies. That work is deferred —
the substitutions above cover the same stylistic neighborhoods.

## Why the `implode` snapshot captures regions, not chord-track pitches

The `implode` array in each snapshot records the output of
`prepareUserFacingHarmonicRegions` — the sequence of harmonic regions
`populateChordTrack` consumes as input. Reading the chord-track staves back
after emission would couple the snapshot to voicing logic, notation font
rendering, and the chord-track staff-pair setup; for a Phase 1b safety net the
region list is the cleaner observable. Phase 2+ (`emitImplodedChordTrack`)
continues to consume this same region list, so drift on either side of the
pipeline still shows up in the snapshot.

## The `tickLocal` slot

Phase 2 exposes `analyzeHarmonicContextLocallyAtTick` via
`notationcomposingbridge.h`, and the harness now populates `tickLocal` at the
same sample tick set as `tickRegional`. Divergence A (Policy #2) can be
read two ways in the same snapshot:

- `tickRegional[].wasRegional == false` at a tick marks a P3→P4 fallback
  (the regional path returned no result and the bridge fell through).
- For ticks where both `tickRegional` and `tickLocal` entries exist, the
  two arrays encode what each path independently reports — any difference
  between them is divergence A showing up at a tick both paths covered.

Sample ticks for `tickLocal` are the same as for `tickRegional` (one per
measure downbeat plus one mid-measure tick), so the two arrays align
index-for-index.

## Updating the baselines

```
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe --update-goldens   # regenerate *.json under snapshots/
./pipeline_snapshot_tests.exe                    # confirm the re-read matches
```

The flag is also accepted via `PIPELINE_SNAPSHOT_UPDATE=1` in the environment.
CI must not set this flag — in CI the harness runs as a comparator only.

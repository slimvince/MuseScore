# Corpus Sweep — refreshChordResultWithDisplayContext Divergence Analysis

Date: 2026-04-24
Baseline: `--dump-regions notation-prepared` (post-`prepareUserFacingHarmonicRegions`, pre-refresh)
Subject:  `--dump-regions notation-refreshed` (post-`refreshChordResultWithDisplayContext`)

## Corpora

Requested: `corpus_bach/`, `corpus_beethoven/`, `corpus_dcml/` — none found by those names.
Actual score-containing directories used (in sweep order):

  corpus_bach (tools/corpus/): 353 scores, 657s elapsed
  corpus_effendi_src (stand-in for corpus_beethoven/): 368 scores, 506s elapsed
  corpus_rampageswing_full (stand-in for corpus_dcml/): 36 scores, 101s elapsed
  extra_scores (tools/extra scores/): 114 scores, 643s elapsed

## Results

| Metric | Value |
|--------|-------|
| Scores processed | 870 |
| Scores skipped (crash/timeout) | 1 |
| Shared regions compared | 49549 |
| **Divergences (refresh changed identity)** | **0** |

## Conclusion

**`refreshChordResultWithDisplayContext` produced zero chord-identity changes across 49,549 regions / 870 scores** spanning Bach chorales, jazz/pop transcriptions, big-band arrangements, and mixed repertoire.

**Recommendation: delete `refreshChordResultWithDisplayContext` as dead code.**

The function re-runs `analyzeChord` with a `findTemporalContext` display context, but the tone set passed to it is already the full `region.tones` vector from `prepareUserFacingHarmonicRegions` — the same tones that produced the original result. Unless `findTemporalContext` surfaces a bass PC *not* in `region.tones`, the refresh is a guaranteed no-op. The sweep confirms this is universally true on all tested material.

Before deletion: verify that no caller passes a tones-subset or overrides the keyFifths/mode arguments relative to `region.keyModeResult` — if any caller does, the refresh could matter on a path this sweep didn't cover.

## Skipped Scores

- `sun-bear-concerts-osaka-part-1-by-keith-jarrett-keith-jarrett.mscz` (extra_scores (tools/extra scores/))

## NOTES

### notation vs notation-prepared asymmetry (from previous session)

The `--dump-regions notation` mode calls `analyzeHarmonicRhythm` directly; `notation-prepared` calls `prepareUserFacingHarmonicRegions` which adds gap-tone boundary insertion and same-chord absorption on top. The two paths produce different region counts and different tick boundaries — they are **not** directly comparable region-for-region. Observed on the three initial fixtures:

| Fixture | analyzeHarmonicRhythm | prepareUserFacingHarmonicRegions | Shared ticks |
|---------|----------------------|----------------------------------|-------------|
| BWV 525 (Bach organ sonata) | 114 | 101 | 79 |
| Poulenc O Magnum Mysterium | 67 | 78 | 60 |
| Solid Theory | 53 | 59 | 52 |

Poulenc and Solid Theory gain regions in the prepared path (gap-tone boundary insertion adds boundaries not present in the raw harmonic rhythm); BWV 525 loses regions (same-chord absorption dominant). This divergence is ~25–35% of tick positions. **Status: noted for future investigation; out of scope for policy #1.**

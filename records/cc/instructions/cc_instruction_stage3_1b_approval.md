# CC Instruction: 3.1b approval — B1′ + B2 with ONE pre-commit condition

## Ratification

The bounded-window revision is **approved** (report §R read in full; §R1–R4 verified
against the working tree earlier this session). MRU=16 justification accepted; the A/B
realization (always-on unit + DISABLED sweep at 0 diffs) accepted; P4 stays cold and
the D-P4/D-BRIDGE rollback stands as amended.

## The one pre-commit condition — close the pointer-reuse hazard (§R4/§6.3)

A cache that can false-hit on a freed-then-reallocated `Score*` with a coincidentally
equal undo token can silently show stale labels — that is not a "flagged note" class
of risk for a correctness-first cache; it rides IN B1′, not behind it.

Implement the cheapest RELIABLE guard, your pick with justification:
- a score-identity salt in the guard tuple (a per-Score creation serial / `cmdState`
  generation — whatever the notation layer offers that is unique per object LIFETIME,
  not per address), or
- a flush hook on score close/destruction, or
- both if each is one line.

Add one unit test for the guard's semantics (whatever is constructible — e.g. the
DistinctScoresDoNotShareCache pattern extended to a destroy-then-create sequence if
the test env allows; if genuinely untestable, say so and document the guard's
reasoning in the code comment). **If NO reliable per-lifetime identity or close hook
exists: stop and report** — we will not ship the cache with a known silent-staleness
hole.

## Then commit (both held items)

- **B1′** as staged + the hazard guard + its test:
  `feat: bounded-window decode cache for the P3 query path (Stage 3.1b, byte-identical)`
  — message body must carry: byte-identity evidence (snapshots 11/11 no-refresh,
  CachedEqualsUncachedAcrossWarmSweep, AnswerDelta 0 diffs), cold≈baseline /
  warm ~0.003 ms, Q1 re-decision pointer (design §8 amendment), whole-score evidence
  artifact reference.
- **B2** (rule-5 doc riders) as staged.

Re-run before committing (the guard touches the cache): notation suite + the always-on
A/B + snapshots. Report both hashes + the guard chosen. STATUS/COWORK_HANDOFF stay
mine — I fold the 3.1b saga in after your hashes.

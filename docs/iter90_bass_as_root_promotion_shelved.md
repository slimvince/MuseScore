# Iter 90 — Bass-as-root promotion (shelved)

*Written 2026-05-15. Records the investigation, why a local fix could not be
made safe, and where a future attempt should look instead.*

## Problem

Per `tools/iter90_wrong_root_characterization.txt`, 122 of 122 genuine
wrong-root errors in the Baroque BIR=false=118 baseline cluster sharply by
`(true_root - our_root) mod 12`:

| offset | n | our quality | meaning |
|---|---|---|---|
| +8 | 56 | Minor | iii of true root (e.g. `Em/C` instead of `C` / `Cmaj7`) |
| +9 | 47 | Major (42) / Minor (5) | III of true root (e.g. `C/A` instead of `Am` / `Am7`) |
| +5 | 8 | Major / Power / Dim | mixed |
| +4 | 8 | Major | bass=3rd patterns |
| other | 3 | mixed | |

103 of 122 (84%) follow Patterns A (Em/C → Cmaj-rooted) and B (C/A →
Am-rooted). 55 of those 103 have `bass == true_root` exactly.

The analyzer correctly captures the pitch classes — `true_root` is in
`pcWeight` 100% of the time — but ranks the iii/III triad above the
bass-rooted reading. The bass-rooted candidate often does not enter
`results[]` at all (the top-3 cap is exhausted by same-root variants of
the iii/III reading), so any post-ranking gate must scan
`rawCandidates`.

## What was tried

A post-ranking gate symmetric to **Iter 86** (bass-b7 promotion) at
[chordanalyzer.cpp:2571](../src/composing/analysis/chord/chordanalyzer.cpp#L2571):
when the winner is a Major/Minor slash chord whose root sits a third (m3
or M3) above the bass, look in `rawCandidates` for the bass-rooted target
and promote it.

Two discriminator stacks were tested.

**Variant A (simple)** — slashChord + delta∈{3,4} + `pcWeight[bass] >
extensionThreshold` + `score-gap ≤ inversionSuspicionMargin (0.7)` +
`no result has rootPc == bassPc`:

- Baroque: BIR=true 4 → **23**, BIR=false 118 → 111
- Net: **+12 wrong-root errors**
- Jazz: BIR=false 7 → 4 (no hard-stop)

**Variant B (sophisticated)** — Variant A plus `winner is plain triad (no
7th)` + `existingMargin = winner.score − results[1].score < 0.05` +
score-gap widened to `≤ 1.0`:

- Baroque: BIR=true 4 → **28**, BIR=false 118 → 116
- Net: **+22 wrong-root errors**
- Wider score-gap (1.0) overpowered the new tightenings.

Both variants regress.

## Why no local discriminator worked

The pitch-class set `{C, E, G}` is genuinely ambiguous: it can be C
major, or it can be Em (rootless or otherwise) embedded in an E-rooted
context. The same is true of `{A, C, E}` (Am vs. C major rootless
voicing).

The discriminator the analyzer can see locally — pcSet, pcWeights,
templates, key — does not contain the information that disambiguates
these. The information that does is **non-local**:

- The next chord's root (does the bass progress as if it is the chord
  root, or as if it is a passing/non-chord tone?)
- The previous chord's identity (is the iii/III a passing chord between
  V and I, or is the bass-rooted reading the structural arrival?)
- The metric position (is the bass on a strong beat suggesting it is
  structural, or on a weak beat suggesting it is passing?)

Cases where the analyzer is *correct* with the iii/III reading
(e.g. genuine `Em/C` first-inversion sevenths and pedal points) are
indistinguishable from cases where it is *wrong* (e.g. bwv279 m=10 b=1
where the chord is plainly G major) using only the local sonority. A
sample of the regressions includes `Em/C → C6` flips where the truth is
neither — it is `Am7` — so the gate is just rebucketing one wrong
answer into another.

## Cascade-from-segmentation effect

A subtler issue: when a chord identity changes (e.g. the gate flips
`Dm/Bb → Bb6` correctly at one region), the bridge's greedy-expand
re-merges adjacent regions differently because chord identity drives
boundary placement. Some of the +22 regressions are not direct gate
fires but **downstream re-segmentation artifacts** in regions the gate
never touched. This is structural, not a tunable local condition.

## Recommendation for a future attempt

Do not pursue this as a chord-analyzer-local gate. Two more promising
angles:

1. **Bridge-level pass** that, after `analyzeChord` per region, looks at
   the surrounding regions' inferred roots and bass progressions, and
   chooses between `iii/I` and `Imaj7` (or `III/i` and `i7`) using
   adjacent context. This is essentially what tonal harmony analysis
   tools do. Lives in `notationharmonicrhythmbridge.cpp` after the main
   analysis loop, before key-context resolution.

2. **Temporal-context gate** in `chordanalyzer.cpp` that fires only when
   `context->nextRootPc` or `context->previousRootPc` equals the
   bass-rooted reading's root (analogous to existing Gates B/C/D in the
   inversion-correction block). This requires the bridge and batch path
   to both populate temporal context for these regions (already done as
   of Iter 8 / Iter 86).

Approach 2 is incremental and could be tried as Iter 91 with the same
structural triggers (Pattern A/B, slashChord, plain triad) plus the
temporal guard.

## Tooling left in the tree (untracked)

These remain for the next attempt and are not part of Iter 89:

- `tools/analyze_wrong_root_iter90.py` — main characterization script
  (122 cases, offset/quality/bass-relation breakdown).
- `tools/iter90_wrong_root_characterization.txt` — full enumeration with
  per-case detail.
- `tools/analyze_iter90_regressions.py` — dumps current BIR=true cases
  with pcWeights, alts, key info; useful for diagnosing post-gate
  regressions.
- `tools/survey_iii_slash_correct_iter90.py` — counts CORRECT iii-slash
  patterns (Em/C, C/A) where the analyzer's reading agrees with ground
  truth; what would be regressed by an unconditional flip.
- `tools/diff_iter90_classification.py`, `tools/diff_iter90_flips.py` —
  per-case bucket diffs from earlier iteration attempts.

## Outcome

No code change committed for Iter 90. Working tree (after revert)
matches HEAD = `2085f11322` (Iter 89). Baroque baseline restored:
BIR=true=4, BIR=false=118. Jazz baseline restored: BIR=false=7.

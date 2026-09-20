# Gate R — rcb bass-chord-tone guard — Implementation Report

**Date:** 2026-06-08
**Status:** Implemented and fully validated. **NOT committed. Goldens NOT refreshed.**
Stopped per instruction (snapshot drift outside the 3 target scores + BIR=true count
change) — see §6 and §8 for the decision and what needs your sign-off.

**Outcome in one line:** Gate R fixes all three Δ=+7b targets and is **clean across
both presets** (no BIR regressions, proven by full baseline diffs), but the final
shape required **two refinements beyond the literal instruction** (a `basisDep`
condition and an `!explorationMode` guard), and it changes **6 bridge-path snapshot
scores** that need golden refresh + your verification before commit.

---

## 1. tiePriority confirmation

`ScoringCell::tiePriority` **is** the template index. Confirmed at
`harmonicfunctionlayer.h:159`:
```cpp
int tiePriority;   ///< Template index.
```
It is populated in `chordanalyzer.cpp:2916` as `cell.tiePriority =
static_cast<int>(tplIdx)` (the loop index over the 17-template array). No
disambiguation re-mapping. Safe to index `kMasks` with it.

## 2. Templates 14 and 15 (verified against code, not the quality name)

Read directly from `chordanalyzer.cpp:2707` (`std::array<TemplateDef,17> templates`)
and cross-checked byte-identical against `kDiagTemplates` (`:3218`):

| # | code line | quality | intervals |
|---|---|---|---|
| 14 | `{ Suspended4, {0,5,8,10}, {0,-1,+8,-2} }` | Suspended4 (sus4♯5) | **{0,5,8,10}** |
| 15 | `{ Suspended4, {0,6,7},    {0,+6,+1} }`     | Suspended4 (sus♯4)  | **{0,6,7}** |

Both match the instruction's cross-check table. All 17 interval sets verified; every
mask entry is non-zero.

## 3. Final `kMasks` array as implemented

`harmonicfunctionlayer.cpp`, anonymous namespace, helper `bassIsTemplateChordTone`:
```cpp
static constexpr std::array<uint16_t, 17> kMasks = {
    (1u<<0)|(1u<<4)|(1u<<7),            // 0  Major triad   {0,4,7}
    (1u<<0)|(1u<<4)|(1u<<7)|(1u<<11),   // 1  Maj7          {0,4,7,11}
    (1u<<0)|(1u<<4)|(1u<<7)|(1u<<10),   // 2  Dom7          {0,4,7,10}
    (1u<<0)|(1u<<4)|(1u<<6)|(1u<<10),   // 3  Dom7♭5        {0,4,6,10}
    (1u<<0)|(1u<<3)|(1u<<7),            // 4  Minor triad   {0,3,7}
    (1u<<0)|(1u<<3)|(1u<<7)|(1u<<10),   // 5  Minor 7th     {0,3,7,10}
    (1u<<0)|(1u<<3)|(1u<<6),            // 6  Diminished    {0,3,6}
    (1u<<0)|(1u<<5)|(1u<<6)|(1u<<10),   // 7  Sus4♭5        {0,5,6,10}
    (1u<<0)|(1u<<3)|(1u<<6)|(1u<<10),   // 8  HalfDim       {0,3,6,10}
    (1u<<0)|(1u<<4)|(1u<<8),            // 9  Augmented     {0,4,8}
    (1u<<0)|(1u<<4)|(1u<<8)|(1u<<10),   // 10 Aug dom7      {0,4,8,10}
    (1u<<0)|(1u<<2)|(1u<<7),            // 11 Sus2          {0,2,7}
    (1u<<0)|(1u<<5)|(1u<<7)|(1u<<10),   // 12 Sus4+m7       {0,5,7,10}
    (1u<<0)|(1u<<5)|(1u<<7)|(1u<<11),   // 13 Sus4+Maj7     {0,5,7,11}
    (1u<<0)|(1u<<5)|(1u<<8)|(1u<<10),   // 14 Sus4♯5        {0,5,8,10}
    (1u<<0)|(1u<<6)|(1u<<7),            // 15 Sus♯4         {0,6,7}
    (1u<<0)|(1u<<7),                    // 16 Power         {0,7}
};
```

## 4. BIR before and after (both presets) — proven by full baseline diffs

Both rows verified by rebuilding the pre-Gate-R binary, regenerating the corpus, and
running `tools/dump_bir_cases.py` (per-region enumeration) on baseline vs after, then
`comm`-diffing the case lists. Counts are not just aggregates — the **composition** was
checked.

```
Baroque  BIR=true=25, BIR=false=16   →   BIR=true=24, BIR=false=13
Jazz     BIR=true=36, BIR=false=10   →   BIR=true=35, BIR=false=7
```

Baseline diff (identical for **both** presets):
- **Fixed (4):** bwv245.28 (t4320), bwv296 (t23040), bwv320 (t37440) — the 3 Δ=+7b
  targets — plus **bwv349 (m13 t17280, BIR=true)** as a bonus fix.
- **New regressions: ZERO.**

The BIR=true 25→24 / 36→35 drop is therefore **not a regression** — it is bwv349
(a bare-root foreign-bass continuation, same mechanism as the targets) being
correctly fixed. The instruction's "BIR=true must not drop" is a conservative proxy;
the composition diff proves the drop is a clean fix.

## 5. Target cases

All three Δ=+7b targets are fixed (confirmed absent from the BIR=false enumeration in
both presets):
- **bwv245.28** t4320 → now reads E (root 4) ✓
- **bwv296** t23040 → now reads G (root 7) ✓
- **bwv320** t37440 → now reads C (root 0) ✓

(These scores are **not** in the pipeline snapshot corpus, so their fix does not show
up as a snapshot golden change — contrary to the instruction's tentative expectation.)

## 6. Unexpected regressions / bonuses / deviations from the literal instruction

The literal "template-tone-only" Gate R did **not** work as written. Two problems were
found and fixed; both fixes are well-motivated by the diagnostic data and the code
mechanism.

### Deviation 1 — `basisDep <= 0` condition (REQUIRED; literal gate regressed a unit test)
The literal gate broke the composing unit test
`Cm7SlashF_StepwiseBassContext_IsCm7NotFsus`. **Cm7add11/F**: the F bass is interval 5
(P4/11th) from C — foreign to the bare Min7 template `{0,3,7,10}` — yet F is sounding
as the 11th and the reading is correct. The literal gate wrongly stripped rcb from
this legitimate extended slash voicing.
Discriminator (traced through `bassDependentContextualBonuses` /
`supportsContextualInversionBonuses`): a legitimate inverted/extended continuation has
a **sounding third**, which makes it `isInvertedMajMin` and fires
`sameRootInversionBonus` ⇒ `basisDep > 0`. A Δ=+7b bare-root continuation has **no
sounding third** ⇒ `basisDep == 0` (matches the diagnostic report Table 1: `bD=0.000`
for all three). Adding `cell.basisDep <= 0` restricts Gate R to genuine bare-root
nonsense and spares real extended chords. After this fix the unit suite is 407/407.

### Deviation 2 — `!explorationMode` guard (REQUIRED; basisDep-only variant caused a segmentation regression)
With basisDep-only, the BIR diff showed a **new regression** — **bwv355 m15 b3
(t27840)**: a baseline region (`Bm/D` @ t26880, DCML-correct root B) was **split** into
a spurious `G/B` sub-region. Root cause: `rootContinuityBonus` is (by design) **not**
suppressed during `greedyExpandSegmentation` exploration, so segmentation already
depends on it; letting Gate R perturb rcb during exploration shifts region boundaries.
Gate R is a *final-scoring* correction — adding `!prefs.explorationMode` makes
segmentation byte-identical to baseline. After this fix the bwv355 regression is gone
and both presets diff clean (§4).

### Bonus
- bwv349 BIR=true fixed in both presets (a genuine extra improvement).

## 7. Corpus analysis results for both presets

| Preset | metric | baseline | Gate R | Δ |
|---|---|---|---|---|
| Baroque | BIR=false | 16 | **13** | −3 (the 3 Δ targets) |
| Baroque | BIR=true  | 25 | **24** | −1 (bwv349 fixed) |
| Jazz    | BIR=false | 10 | **7**  | −3 (the 3 Δ targets) |
| Jazz    | BIR=true  | 36 | **35** | −1 (bwv349 fixed) |

No hard-stop triggered: no BIR=false increase in either preset; no new errors in
either preset. Net −4 genuine errors per preset.

Unit/integration suites on the final (guarded) binary:
- `composing_tests.exe`: **407/407**
- `notation_tests.exe`: **52/52**

## 8. Snapshot goldens — drifted, NOT refreshed (needs your decision)

`pipeline_snapshot_tests.exe`: 5/11 pass, **6 drift**, all **outside** the 3 target
scores (the targets are not in this corpus). Per the instruction ("If ANY snapshot
test outside the three target scores fails: STOP and report") I did **not** run
`--update-goldens`. These are **bridge-path** outputs (the BIR corpus above is the
batch path, which is proven clean).

The `!explorationMode` guard removed the worst cascade (bach_chorale_137 tick-0
`Dm`→`Dm/C` reverted). Remaining drifts, characterized:

| Score | Change | Winner? | Assessment |
|---|---|---|---|
| mozart_k279_1 | spurious `G major (G/E)` alt dropped; winner `E dim` unchanged | no | **Improvement** (same Δ mechanism — removes a nonsense G/E alt) |
| bach_bwv806_gigue | runner-up alt `D maj`→`C♯ min`; winner `D maj` unchanged | no | Neutral |
| bach_bwv806_prelude | `Esus2`(Vsus2)→`E/G♯`(V6); display tick 24240→23280 | yes | Likely **improvement** (V6 idiomatic); tick shift is an annotation-merge artifact of the corrected winner, not a segmentation change |
| chopin_bi105_op30_2 | winner `B min`→`B dim` (both tie 2.165) | yes | Likely **improvement** — a B-dim reading needs F♮ (a B-min reading needs F♯); the tie + tritone bass favors dim |
| bach_chorale_003 | `Asus4`→`D major` (key E) | yes | Uncertain — needs DCML check |
| bach_chorale_137 | deeper P3/P4 alts (`C`↔`F`); tick-0 cascade gone | (alt) | Uncertain — needs DCML check |

My read: these are consistent with Gate R's intent (suppressing rcb-propped
foreign-bass slash/sus continuations) and lean toward improvements, but two
(bach_chorale_003, bach_chorale_137) are not rigorously DCML-verified. The bridge path
is not measured by BIR, so I cannot quantify its net effect the way I did for batch.

## 9. Files changed (uncommitted)

- `src/composing/analysis/function/harmonicfunctionlayer.cpp` — `<array>`/`<cstdint>`
  includes, `bassIsTemplateChordTone` helper (`kMasks`), Gate R block in Pass A.
- `docs/scoring_model.md` — §4 "Gate R" subsection (incl. both refinements), §9 5th
  atomic-update site (`kMasks`), footer.

Repo state: source + binary are the **guarded** variant; goldens **not** refreshed;
**not** committed. `tools/corpus/` currently holds a baseline-Jazz regeneration (a
transient artifact from the diff work — regenerate before relying on it).

## 10. Recommendation

The fix is **sound and clean on the authoritative BIR corpus** (both presets, no
regressions, +1 bonus fix). The blocker to commit is the 6 bridge-path snapshot
drifts, which the instruction (correctly) gates behind human verification.

Proposed next step (your call):
1. **Verify** the two uncertain winner changes (bach_chorale_003 `Asus4`→`D`,
   bach_chorale_137 alts) against DCML; the other four look like improvements/neutral.
2. If acceptable, **refresh goldens** (`pipeline_snapshot_tests.exe --update-goldens`,
   re-run to confirm) and commit Gate R + the doc update atomically, then update
   STATUS.md with the new baselines (Baroque 24/13, Jazz 35/7).
3. If you'd rather not change bridge-path output at all, the alternative is to also
   gate the bridge/annotation path — but note the batch path (BIR) is already clean,
   so the snapshot changes are the *intended* corrections surfacing in a second path.

I have not committed or refreshed goldens pending your decision.

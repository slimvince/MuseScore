# Duplication Audit — Analysis Pipeline (2026-05-18)

> **★ HISTORICAL RECORD — a read-only audit of the tree as it stood on 2026-05-18, parts of whose
> subject the record has since left behind. Banner added 2026-08-13 under the FILING CONVENTION
> (`cowork_design_doc_template.md`, the user's Ruling 62 of
> `cowork_rulings_2026_08_11_fourteenth_stop.md`); tracking row `OPEN_ITEMS.md` OI-315. THE BODY
> BELOW IS UNTOUCHED (#12).**
>
> **What this document is a record OF:** a read-only duplication audit, dated 2026-05-18, taken at
> baseline `7060f2c5db`, of the batch and bridge analysis paths as they stood on that date.
>
> **The fate of the part of its subject that was established at this reading, and of nothing else.**
> §2.11 says of the two key-resolution entry points that *"both have the same piece-start
> shortcut"*, and lists a *"strong declared-mode prior"* block as a bridge-side divergence. **Both of
> those code paths are gone.** They were removed in **Stage 4b-i, 2026-06-14** — the increment that
> made the opening note-based and demoted the declared mode to a small hint — which
> `ARCHITECTURE.md` §5.2 records and which `keyresolver::resolveKeyAndModeRanked` states in its own
> two comments. **Established at the code 2026-08-13**, reading the whole of each enclosing function:
> that resolver carries no piece-start branch, its only early return being the
> insufficient-pitch-classes fallback; and the bridge entry point `resolveKeyAndMode`
> (`notationcomposingbridgehelpers.cpp`) is a preference load followed by a delegation to it, with
> neither block. §2.11's line citations into that file resolve to neither function at HEAD.
>
> **THE BOUND ON THIS BANNER, STATED SO IT IS NOT READ AS MORE THAN IT IS.** No sweep was run over
> this audit's remaining findings, and none is claimed to hold or not to hold. The banner names the
> fates established at this reading; every other statement in the body is a 2026-05-18 statement
> about a 2026-05-18 tree and is neither endorsed nor withdrawn here. Two facts a reader should carry
> into the body anyway, both from the record rather than from a sweep: the helper duplication §§2.1–2.13
> describes has since been unified onto shared `engravingbridge` implementations, which the code's own
> comment at the surviving pass-throughs points back at this document for; and the joint estimator has
> since become the production inference layer on **both** the batch/corpus surface and the in-app
> notation surface (`CLAUDE.md` gate block (A)), so the two-path framing this audit is built on no
> longer describes what runs.

**Scope.** Read-only audit across `tools/batch_analyze.cpp`,
`src/notation/internal/notationharmonicrhythmbridge.cpp`,
`src/notation/internal/notationcomposingbridgehelpers.{cpp,h}`,
`src/composing/analysis/chord/chordanalyzer.{cpp,h}`,
`src/composing/analysis/harmony/harmonicsegmenter.{cpp,h}`, and
their callers.

**Baseline.** HEAD `7060f2c5db` (Iter 96). Working tree has uncommitted v3
changes; none affect this audit.

---

## 1. Executive summary

The duplication is severe and load-bearing. **`batch_analyze.cpp` re-implements
the entire bridge-side analysis pipeline as a parallel translation unit** that
links against the composing module but deliberately does *not* call any of the
shared bridge helpers in `notationcomposingbridgehelpers.cpp`. Every primitive
of the per-region pipeline — `collectRegionTones`, `collectSoundingAt`,
`buildTones`, `beatTypeToWeight`, `safeBeatType`, `regionMetricWeightForBeatType`,
`detectBassMovementSubBoundaries`, `findTemporalContext` — exists in BOTH files,
and the larger orchestrators (`analyzeScore` in batch vs `analyzeHarmonicRhythm`
in the bridge) duplicate the same Pass 1 / Pass 2 / Pass 2b structure with
hand-synchronized fixes.

The "unification" of Iters 92–95 plumbed identical scoring inputs by **patching
both sides in lockstep**, not by adding a single shared call. The result is
two analysis paths that are *intended* to be equivalent but routinely diverge
in practice — confirmed at bwv356 m19 b1 (§4), where the same input tones at
the same tick produce `Gbm7b5b9/C` on the batch path and `Cm6` on the bridge
path. The full bwv356 score produces **31 batch regions vs 61 bridge regions**.

The shared infrastructure that *does* exist — `harmonicsegmenter.cpp`
(greedy-expand, fillGap, head-/tail-gap synthesis), the `IChordAnalyzer`
interface, and the inline helpers in `chordanalyzer.h` (`inferNextRootPc`,
`advanceTemporalContext`) — works correctly and is a model for what the
duplicated helpers should look like.

---

## 2. Complete duplication inventory

For each entry: which files hold copies, what the divergence status is, and
where the canonical home should be (§5).

### 2.1 `collectRegionTones` — **CRITICAL DIVERGENCE**

| File | Lines | Signature |
|---|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L769) | 769–1178 | `static std::vector<ChordAnalysisTone> collectRegionTones(const Score*, int startTickInt, int endTickInt, const std::set<size_t>& excludeStaves, int parentStartTickInt = -1)` |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L836) | 836–1197 | `std::vector<ChordAnalysisTone> collectRegionTones(const Score*, int startTickInt, int endTickInt, const std::set<size_t>&, int parentStartTickInt)` |

The header [notationcomposingbridgehelpers.h:82-83](../src/notation/internal/notationcomposingbridgehelpers.h#L82-L83)
already carries an explicit `TODO (ARCHITECTURE.md §2.10)` note acknowledging the
duplication. Both copies share the same Pass 2 (repetition boost), Pass 3
(cross-voice boost) and Pass 4 (pedal-tail multiplier) structure. Three
hard divergences exist:

**Divergence A — bass selection (semantic, observable).**
- Batch ([batch_analyze.cpp:1145-1151](../tools/batch_analyze.cpp#L1145-L1151)):
  bass = absolute lowest pitch over PCs with `totalWeight > 0.0`. No
  passing-tone filter.
- Bridge helpers ([notationcomposingbridgehelpers.cpp:1148-1167](../src/notation/internal/notationcomposingbridgehelpers.cpp#L1148-L1167)):
  bass = lowest pitch whose PC weight ≥ `totalWeight * prefs.bassPassingToneMinWeightFraction`,
  with a fallback to the absolute lowest pitch if the filter excludes everything.

  ```cpp
  // helpers
  const double bassMinWeight = totalWeight * prefs.bassPassingToneMinWeightFraction;
  // batch:  NO equivalent — bass passing-tone filter does not exist on the batch path.
  ```

  This means the analyzer's bass PC choice can differ between paths whenever a
  brief, low-weight bass passing tone is the lowest sounding pitch. The bridge
  filters it out and selects a more durable bass; batch keeps it.

**Divergence B — look-ahead exclusion (structural, observable).**
- Batch ([batch_analyze.cpp:984-1021](../tools/batch_analyze.cpp#L984-L1021)):
  computes `pcsSoundingAtStart` from the backward-pass + the forward seg-0 tick,
  then sets `excludeLookAhead = (pcsSoundingAtStart >= 3)`. When true, the
  forward walk skips any note whose onset is `> startTickInt` ([batch_analyze.cpp:1051-1053](../tools/batch_analyze.cpp#L1051-L1053)):
  ```cpp
  if (excludeLookAhead && segTickInt > startTickInt) {
      continue;
  }
  ```
- Bridge helpers: **no equivalent**. The bridge always accumulates the full
  region from `startTick` to `endTick`. This is a fundamental shape difference:
  the bridge sees more tones than batch whenever the region opens with ≥3 PCs
  sounding.

**Divergence C — `staffIsEligible` tick awareness.**
- Batch passes `staffIsEligible(score, si)` (the non-tick overload, defined at
  [batch_analyze.cpp:360-371](../tools/batch_analyze.cpp#L360-L371) and ignored
  by [batch_analyze.cpp:373-376](../tools/batch_analyze.cpp#L373-L376) — the
  tick overload is a no-op).
- Bridge helpers pass `staffIsEligible(sc, si, startTick)` (backward walk) or
  `staffIsEligible(sc, si, s->tick())` (forward walk), using the tick-aware
  overload defined in `notationanalysisinternal.h`.

  In the current codebase this difference is mostly cosmetic (no eligibility
  check varies with tick), but the bridge form is correct under any future
  tick-dependent eligibility rule (e.g. mid-piece instrument changes).

**Minor structural differences:** the bridge factors pedal-window collection
into `buildPedalWindowIndex()` ([notationcomposingbridgehelpers.cpp:780-831](../src/notation/internal/notationcomposingbridgehelpers.cpp#L780-L831));
batch inlines it ([batch_analyze.cpp:832-873](../tools/batch_analyze.cpp#L832-L873)).
Same logic, different shape.

---

### 2.2 `detectBassMovementSubBoundaries` — duplicated, near-identical

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L1409) | 1409–1493 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L1315) | 1315–1397 |

The batch copy at [batch_analyze.cpp:1405-1406](../tools/batch_analyze.cpp#L1405-L1406)
literally states: `// Pass 2b: bass-movement sub-boundary detection (local copy; canonical in notationcomposingbridgehelpers.cpp).`
Bodies are byte-equivalent apart from the same `staffIsEligible` tick-awareness
difference (Divergence C above) and a parameter-default difference: bridge declares
`int minGapTicks = 2 * Constants::DIVISION` in the header; batch uses an explicit
default in the local declaration.

---

### 2.3 `collectSoundingAt` — duplicated

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L1500) | 1500–1553 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L353) | 353–403 |

Same algorithm (collect at anchor + walk back ≤ 4 quarter notes for sustained
notes). Same `staffIsEligible` tick-awareness difference. Both gate on
`n->play() && n->visible()`.

---

### 2.4 `buildTones` — duplicated, byte-identical

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L1555) | 1555–1572 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L405) | 405–426 |

Pure mechanical conversion (`SoundingNote → ChordAnalysisTone`); marks the
lowest ppitch as bass. Identical logic.

---

### 2.5 `beatTypeToWeight` — duplicated, identical

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L465) | 465–478 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L428) | 428–442 |

Identical switch on `BeatType` returning `prefs.beatWeight*`. Trivial.

---

### 2.6 `safeBeatType` — duplicated, identical

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L480) | 480–493 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L444) | 444–460 |

Identical — null-guards, falls back to `BeatType::SUBBEAT`, computes
`rtick2beatType` from the measure's `timesig()`.

---

### 2.7 `regionMetricWeightForBeatType` — duplicated, identical

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L497) | 497–507 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L462) | 462–473 |

Identical hard-coded `{1.0, 0.85, 0.75, 0.5}` table. The header already carries
a `TODO (ARCHITECTURE.md §2.10)` note at [notationcomposingbridgehelpers.h:82-83](../src/notation/internal/notationcomposingbridgehelpers.h#L82-L83).

---

### 2.8 `timeDecay` — duplicated, identical

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L509) | 509–512 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L475) | 475–478 |

Identical `pow(decayRate, beatsAgo/4.0)`. Trivial helper; still duplicated.

---

### 2.9 `distinctPitchClasses(PitchContext)` — duplicated

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L514) | 514–521 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L480) | 480–493 |

Trivial duplicate (batch uses `std::set`; helpers uses a 12-element bool array).
Semantically equivalent.

---

### 2.10 `collectPitchContext` — duplicated

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L523) | 523–582 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L495) | 495–574 |

Same windowed lookback/lookahead loop. Batch uses fixed
`LOOKAHEAD_WEIGHT = 0.5` constant; bridge inlines the same constant. Same
`staffIsEligible` tick-awareness difference (Divergence C). Both feed
`KeyModeAnalyzer::PitchContext` records into `analyzeKeyMode`.

---

### 2.11 Key resolution — **API ASYMMETRY** (not a direct duplicate, but parallel)

| Path | Function | Where | Returns |
|---|---|---|---|
| batch | `inferLocalKey` | [batch_analyze.cpp:593](../tools/batch_analyze.cpp#L593)–721 | `std::vector<KeyModeAnalysisResult>` (top 3 candidates, post-hysteresis) |
| bridge | `resolveKeyAndMode` | [notationcomposingbridgehelpers.cpp:576](../src/notation/internal/notationcomposingbridgehelpers.cpp#L576)–773 | Out-params (`outKeyFifths`, `outMode`, `outConfidence`, optional `outScore`) — single winner only |

Both invoke `KeyModeAnalyzer::analyzeKeyMode` with the same input shape
(`PitchContext` vector + key fifths + declared mode + prefs), both implement
the same windowed lookback + dynamic-lookahead loop, both implement hysteresis
the same way, and both have the same piece-start shortcut.

Divergences:
- **Return shape.** Batch returns ranked top-3 (for JSON `keyModeRunnerUp`
  emission); bridge returns the single chosen result via out-params. The bridge
  builds the `keyModeRunnerUp` field via a separate call site (none does so in
  the current bridge; that field is only populated in the batch JSON output).
- **Declared-mode strong prior.** Bridge `resolveKeyAndMode`
  ([notationcomposingbridgehelpers.cpp:744-767](../src/notation/internal/notationcomposingbridgehelpers.cpp#L744-L767))
  contains a "strong declared-mode prior" block that finds the best result
  compatible with the score's declared key/mode and returns it instead of an
  incompatible top scorer. **Batch `inferLocalKey` has no equivalent block.**

This is an asymmetry that can produce different chosen keys on the same input.

---

### 2.12 `findTemporalContext` — duplicated, near-identical

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L1574) | 1574–1630 |
| [src/notation/internal/notationcomposingbridgehelpers.cpp](../src/notation/internal/notationcomposingbridgehelpers.cpp#L1399) | 1399–1459 |

Both walk backward from `seg` to find the previous chord, run `analyzeChord` on
its sounding notes, populate `previousRootPc / previousQuality / previousBassPc`.
Same `staffIsEligible` tick-awareness difference.

---

### 2.13 `detectHarmonicBoundariesJaccard` — dead code (batch only)

| File | Lines |
|---|---|
| [tools/batch_analyze.cpp](../tools/batch_analyze.cpp#L1180) | 1180–1403 |

Dead since Iter 54 (batch switched to greedy-expand). Removed from the bridge
in Iter 81 ([STATUS.md history](../STATUS.md)). Carried in batch only as
"retained for reference" per the comment at
[batch_analyze.cpp:1660](../tools/batch_analyze.cpp#L1660). **224 dead lines.**

---

### 2.14 Region orchestrator — **STRUCTURAL DUPLICATION**

| Path | Function | Where |
|---|---|---|
| batch | `analyzeScore` | [batch_analyze.cpp:1640](../tools/batch_analyze.cpp#L1640)–1983 |
| bridge | `analyzeHarmonicRhythm` (regional path) | [notationharmonicrhythmbridge.cpp:103](../src/notation/internal/notationharmonicrhythmbridge.cpp#L103)–819 |

Both orchestrators perform the same five-stage pipeline:

1. Initial key resolution (`inferLocalKey` vs `resolveKeyAndMode`).
2. Pass 1 boundary detection via `greedyExpandSegmentation` (shared composing
   helper — good!), then expand boundaries from `placedRegionsToTicks`.
3. **Iter 77 Fix B** (placedRegionsToTicks + END ticks of placed regions) —
   the same fix is patched into both:
   - bridge: [notationharmonicrhythmbridge.cpp:266-287](../src/notation/internal/notationharmonicrhythmbridge.cpp#L266-L287)
   - batch: [batch_analyze.cpp:1672-1695](../tools/batch_analyze.cpp#L1672-L1695)
4. Pass 2 / Pass 2b sub-boundary expansion + per-sub-region `analyzeChord`.
5. Same-chord region merge (`mergeChordAnalysisTones` + bass tone re-derivation).

Structural divergences:
- **Pass 2 (onset Jaccard sub-boundaries).** Bridge has it
  ([notationharmonicrhythmbridge.cpp:454-630](../src/notation/internal/notationharmonicrhythmbridge.cpp#L454-L630),
  calling `detectOnsetSubBoundaries` which lives ONLY in the helpers). **Batch
  does not.** Batch skips straight from Pass 1 to Pass 2b.
- **Pass 2b iteration.** Bridge runs Pass 2b in a `while (anyNewSplit)` loop up
  to `kMaxBassMovementPasses = 8`
  ([notationharmonicrhythmbridge.cpp:643-795](../src/notation/internal/notationharmonicrhythmbridge.cpp#L643-L795)).
  **Batch runs Pass 2b exactly once**
  ([batch_analyze.cpp:1735-1753](../tools/batch_analyze.cpp#L1735-L1753)) — no
  iteration. If a Pass 2b split exposes a further bass change inside one of the
  new sub-regions, batch misses it.
- **`absorbShortRegions` (Pass 3).** Bridge defines it as a local lambda
  ([notationharmonicrhythmbridge.cpp:165-199](../src/notation/internal/notationharmonicrhythmbridge.cpp#L165-L199))
  with the Iter 78 Fix A `sharesPrevRoot` predicate. Batch does it inline in
  `analyzeScore` ([batch_analyze.cpp:1934-1945](../tools/batch_analyze.cpp#L1934-L1945))
  but **WITHOUT the `sharesPrevRoot` guard** — batch unconditionally absorbs
  any region shorter than `Constants::DIVISION`. This is a clear divergence:
  Iter 78 Fix A landed on the bridge but never ported to batch.
- **Iter 87 post-merge MinorSeventh re-stamp.** Lives ONLY in batch
  ([batch_analyze.cpp:1947-1980](../tools/batch_analyze.cpp#L1947-L1980)) —
  the bridge has no equivalent. Bridge relies on the analyzer's intra-call
  Iter 86 stamp surviving the merge; batch additionally re-stamps after the
  merge. This is a known asymmetry documented in STATUS.md Iter 87.
- **`backfillNextRootPc`.** Lives ONLY in the bridge
  ([notationharmonicrhythmbridge.cpp:78-85](../src/notation/internal/notationharmonicrhythmbridge.cpp#L78-L85)) —
  for emitting `V/x` and `viio/x` Roman-numeral labels via
  `ChordSymbolFormatter::formatRomanNumeral`. Batch does not run this pass; its
  JSON output omits the tonicization slash. This is silent: batch's
  `chordSymbol`/`romanNumeral` JSON fields differ from the bridge's whenever
  the analyzer would have emitted a `V/x` label.

---

### 2.15 Parent-scope plumbing — **lockstep duplicated**

The Iter 92–95 plumbing for joint scoring lives in BOTH orchestrators with
identical intent but parallel code:

- **`parentStartTick` (Iter 93)** — passed to `collectRegionTones` to anchor
  `onsetAtRegionStart` at the parent boundary:
  - bridge Pass 2: [notationharmonicrhythmbridge.cpp:527-533](../src/notation/internal/notationharmonicrhythmbridge.cpp#L527-L533)
  - bridge Pass 2b: [notationharmonicrhythmbridge.cpp:714-718](../src/notation/internal/notationharmonicrhythmbridge.cpp#L714-L718)
  - batch: [batch_analyze.cpp:1772-1784](../tools/batch_analyze.cpp#L1772-L1784) (via `parentBoundaryTicks` set lookup)

- **`parentPredBassPc` / `parentSuccBassPc` (Iter 94)** — parent-scope
  neighbours for `w_stepIn` / `w_stepOut` bonuses:
  - bridge Pass 2: [notationharmonicrhythmbridge.cpp:499-502](../src/notation/internal/notationharmonicrhythmbridge.cpp#L499-L502)
  - bridge Pass 2b: [notationharmonicrhythmbridge.cpp:686-689](../src/notation/internal/notationharmonicrhythmbridge.cpp#L686-L689)
  - batch: [batch_analyze.cpp:1856-1874](../tools/batch_analyze.cpp#L1856-L1874) (via `parentBassPcMap` precomputed earlier)

- **`parentSuccRootPc` (Iter 95 Step 2)** — parent successor root PC for
  `w_seq`:
  - bridge Pass 2: [notationharmonicrhythmbridge.cpp:503-505](../src/notation/internal/notationharmonicrhythmbridge.cpp#L503-L505)
  - bridge Pass 2b: [notationharmonicrhythmbridge.cpp:690-692](../src/notation/internal/notationharmonicrhythmbridge.cpp#L690-L692)
  - batch: [batch_analyze.cpp:1819-1846](../tools/batch_analyze.cpp#L1819-L1846)
    (computed differently — batch does a full sub-region `collectRegionTones`
    + `inferNextRootPc` call per region, while the bridge uses
    `regions[parentIdx + 1].chordResult.identity.rootPc` from the already-analyzed
    parent. **These are not equivalent values**: batch's `nextRootPc` is the root
    of the *next sub-region's* tone union analyzed context-free, while bridge's
    is the root of the *next parent region's* already-finalized identity.)

- **Sub-region temporal-context plumbing** is independently re-implemented in
  each Pass 2 / Pass 2b block of the bridge and inline in batch.

The intent is identical; the implementations were typed twice. Iter 95 STATUS
explicitly admits this: *"Step 2 ... bridge Pass 2/2b nextRootPc plumbing
(activates w_seq on live chord track)"* — the change was a pure mirror of
batch-side plumbing.

---

### 2.16 Inline Pedal-window collection — duplicated

Both files re-implement a `pedalWindowsByStaff` map walking the score's spanner
list and skipping sostenuto/soft pedals:
- batch (inside `collectRegionTones`): [batch_analyze.cpp:832-873](../tools/batch_analyze.cpp#L832-L873)
- batch (inside `detectHarmonicBoundariesJaccard`, dead): [batch_analyze.cpp:1216-1260](../tools/batch_analyze.cpp#L1216-L1260)
- helpers (`buildPedalWindowIndex`): [notationcomposingbridgehelpers.cpp:780-831](../src/notation/internal/notationcomposingbridgehelpers.cpp#L780-L831)

The helpers extracted this into a named function; batch keeps two parallel
inline copies (one dead).

---

### 2.17 Constants and magic numbers duplicated across files

| Constant | Batch | Bridge / Helpers |
|---|---|---|
| `LOOKBACK_BEATS = 16` | [batch_analyze.cpp:460](../tools/batch_analyze.cpp#L460) | [helpers.cpp:646](../src/notation/internal/notationcomposingbridgehelpers.cpp#L646) |
| `LOOKAHEAD_BEATS = 8` | [batch_analyze.cpp:461](../tools/batch_analyze.cpp#L461) | [helpers.cpp:647](../src/notation/internal/notationcomposingbridgehelpers.cpp#L647) (`INITIAL_LOOKAHEAD_BEATS`) |
| `LOOKAHEAD_WEIGHT = 0.5` | [batch_analyze.cpp:462](../tools/batch_analyze.cpp#L462) | [helpers.cpp:506](../src/notation/internal/notationcomposingbridgehelpers.cpp#L506) |
| `DECAY_RATE = 0.7` | [batch_analyze.cpp:463](../tools/batch_analyze.cpp#L463) | parameter default in [helpers.h:87](../src/notation/internal/notationcomposingbridgehelpers.h#L87) |
| `kPass2bMinRegionTicks = 4 * DIVISION` | [batch_analyze.cpp:1736](../tools/batch_analyze.cpp#L1736) | [bridge.cpp:640](../src/notation/internal/notationharmonicrhythmbridge.cpp#L640) |
| `kMinRegionTicks = DIVISION` | [batch_analyze.cpp:1934](../tools/batch_analyze.cpp#L1934) | [bridge.cpp:148](../src/notation/internal/notationharmonicrhythmbridge.cpp#L148) |
| `kPass2MinRegionTicks = 4 * DIVISION` | (no equivalent — batch has no Pass 2) | [bridge.cpp:458](../src/notation/internal/notationharmonicrhythmbridge.cpp#L458) |
| `kMaxBassMovementPasses = 8` | (no equivalent — batch iterates once) | [bridge.cpp:641](../src/notation/internal/notationharmonicrhythmbridge.cpp#L641) |
| `backLimit = 4 quarter notes` | [batch_analyze.cpp:914](../tools/batch_analyze.cpp#L914) etc. | [helpers.cpp:949](../src/notation/internal/notationcomposingbridgehelpers.cpp#L949) etc. |

Drift risk: any constant can be changed on one side without the other noticing.

---

### 2.18 Mode prior preset values — duplicated

`applyPreset` in [batch_analyze.cpp:158-222](../tools/batch_analyze.cpp#L158-L222)
hard-codes the same Standard / Jazz / Modal / Baroque / Contemporary preset
values as `modePriorPresets()` in `src/composing/internal/composingconfiguration.cpp`.
The comment at [batch_analyze.cpp:152](../tools/batch_analyze.cpp#L152) admits
this: *"Keep in sync with composingconfiguration.cpp."* Five presets × 21
mode-prior fields = 105 hand-synchronized constants.

---

## 3. Asymmetry inventory (logic in one path only)

| Asymmetry | Lives in | Missing from | Impact |
|---|---|---|---|
| **Bass passing-tone filter** (`bassPassingToneMinWeightFraction`) in `collectRegionTones` | bridge | batch | Different bass PC chosen on sparse regions with brief low passing tones |
| **Look-ahead exclusion** when ≥3 PCs at start (`excludeLookAhead`) | batch | bridge | Different tone set on dense onset regions → different `analyzeChord` input |
| **Pass 2 onset Jaccard sub-boundary detection** (`detectOnsetSubBoundaries`) | bridge | batch | Bridge can split parent regions where attack patterns shift mid-region; batch cannot |
| **Pass 2b iteration loop** (`while anyNewSplit`, 8 passes) | bridge | batch | Bridge finds nested bass changes; batch sees only first-level splits |
| **`absorbShortRegions` `sharesPrevRoot` guard** (Iter 78 Fix A) | bridge | batch | Batch silently absorbs short genuinely-distinct intervening chords into preceding region |
| **Iter 87 post-merge MinorSeventh re-stamp** | batch | bridge | Already documented; bridge depends on intra-`analyzeChord` Iter 86 stamp surviving the merge |
| **`backfillNextRootPc`** (V/x, vii°/x tonicization labels) | bridge | batch | Batch's emitted `romanNumeral` JSON field omits the `/x` slash whenever applicable |
| **Strong declared-mode prior** in key resolution | bridge (`resolveKeyAndMode`) | batch (`inferLocalKey`) | Key choices can diverge when top score is incompatible with the score's declared mode |
| **Key/mode `keyRanked` top-3 emission** | batch | bridge | JSON output detail only — bridge doesn't need it for chord-track display |
| **Per-region key resolution** | both call independently | n/a | The bridge calls `resolveKeyAndMode` per region; batch calls `inferLocalKey` per region. Equivalent intent; both do redundant per-region work because there is no shared per-section key-area pass on either side. |
| **`detectHarmonicBoundariesJaccard`** | batch (dead) | bridge (removed Iter 81) | Pure dead weight — 224 lines |
| **`Pass 1 PreserveAllChanges` granularity** (`denseBoundaryTicks`) | bridge | batch | Bridge supports a granularity mode that emits a boundary at every PC-set change; batch always uses smoothed greedy-expand |
| **`HarmonicRegionGranularity::Smoothed` Pass 3 absorption gate** | bridge (only in Smoothed) | batch (unconditional) | Bridge skips Pass 3 in PreserveAllChanges mode; batch does it unconditionally |
| **Debug capture (`HarmonicRegionDebugCapture`) of pre-/post-merge regions** | bridge | batch (separate `analyzeScoreNotation` path uses bridge's capture) | Asymmetric debug surface |

---

## 4. The bwv356 bar 19 finding — CONFIRMED divergent

Ran:
```
batch_analyze.exe --preset Baroque tools/corpus/bwv356.xml --dump-regions batch
batch_analyze.exe --preset Baroque tools/corpus/bwv356.xml --dump-regions notation
```

At **bar 19, beat 1, tick 25920, duration 1 quarter note**, the two paths
produce different winners despite identical-looking input tones at the same
tick.

**Input tones (identical on both paths):**
| pitch | tpc | pc | weight | isBass |
|---|---|---|---|---|
| 48 | 14 | 0 (C) | 0.25 | true |
| 63 | 11 | 3 (Eb) | 0.25 | false |
| 55 | 15 | 7 (G) | 0.25 | false |
| 69 | 17 | 9 (A) | 0.25 | false |

PCs `{0, 3, 7, 9}` = C minor 7 with added 6 above C bass.

**Batch path winner:**
```json
{
  "rootPitchClass": 6,
  "quality": "HalfDiminished",
  "chordSymbol": "Gbm7b5b9/C",
  "romanNumeral": "biø7b943",
  "chordScore": 0.1,
  "chordScoreMargin": -2.3875,
  "bassPitchClass": 0,
  ...
  "alternatives": [
    {"chordSymbol": "Cm6", "romanNumeral": "iv(add6)", "score": 2.4875},
    {"chordSymbol": "Cm6", "score": 1.7875},
    {"chordSymbol": "Am7b5/C", "romanNumeral": "iiø65", "score": 2.7}
  ]
}
```

**Bridge path winner:**
```json
{
  "rootPitchClass": 0,
  "quality": "Minor",
  "chordSymbol": "Cm6",
  "romanNumeral": "iv(add6)",
  "chordScore": 2.4875,
  "chordScoreMargin": 0,
  "bassPitchClass": 0
}
```

**Diagnosis.** The bridge's winner `Cm6 (score 2.4875)` is the batch's listed
**first alternative** with the *same score*. The batch's winner `Gbm7b5b9/C`
has chord root `Gb (pc 6)` which is **not in the tone set** at all, and its
chord score (0.1) is FAR below the runner-up score (2.4875) — a negative
`chordScoreMargin` of −2.3875, which is structurally impossible inside
`analyzeChord` (winners are always the highest scorer). The most plausible
explanation: the batch winner is being inherited from a *previous* region
through the `analyzeScore` same-bass merge or an Iter 87-style post-process
mutation. The bridge does not apply the same post-merge mutation.

**Whole-score scale of divergence.** The same score produces:
- batch path: 31 regions
- bridge path: 61 regions

The 2× region count is itself a divergence indicator: the bridge's Pass 2 +
iterative Pass 2b splits parent regions that batch leaves whole.

The bwv356 bar 19 case is therefore not an edge case — it is one
specific symptom of pervasive structural divergence between the two
orchestrators. Other ticks in the same score will diverge in similar ways.

---

## 5. Structural recommendation

For each major duplication, the canonical home for the shared implementation:

### 5.1 `collectRegionTones`, `collectSoundingAt`, `buildTones`, `findTemporalContext`, `detectOnsetSubBoundaries`, `detectBassMovementSubBoundaries`, `collectPitchContext`

**Move to a new shared module: `src/composing/analysis/engraving_bridge/`** (or
similar) that depends only on `engraving::Score` (not on the notation module).

The pattern is already established by `src/composing/analysis/harmony/harmonicsegmenter.cpp`,
which is shared via `HarmonicSegmenterCallbacks`. The right shape is the same:
take the score (or callbacks) as input, return tone vectors and boundary ticks.

Both batch and bridge then call the single shared function. The bass passing-tone
filter (Divergence A) becomes a `ChordAnalyzerPreferences` field that batch can
opt into; the look-ahead exclusion (Divergence B) becomes a parameter explicitly
named (e.g. `excludeLookAheadOnDenseStart`) so both paths can opt in. Goal: a
single named call site for any future change.

### 5.2 `beatTypeToWeight`, `safeBeatType`, `regionMetricWeightForBeatType`, `timeDecay`, `distinctPitchClasses`

**Move to `src/composing/analysis/engraving_bridge/metric_weights.{cpp,h}`** (or
roll into the same module above). Trivially shareable. The header already has a
TODO note pointing at ARCHITECTURE.md §2.10.

### 5.3 `inferLocalKey` / `resolveKeyAndMode`

**Unify under a single API in the new shared module** (signature: return ranked
top-N candidates as a vector; both callers extract `[0]` if they only want the
winner, batch additionally extracts `[1]` for the runner-up JSON). Migrate the
**bridge's strong-declared-mode prior** into the shared body so both paths apply
it.

### 5.4 `analyzeScore` (batch) and `analyzeHarmonicRhythm` (bridge)

**The orchestrator itself should be shared.** Move the regional analysis pipeline
to `src/composing/analysis/region/` as a single `analyzeRegions(...)` function
that returns a vector of `HarmonicRegion`. Bridge would call it directly with
`HarmonicRegionGranularity` as an enum parameter; batch would call it and then
do the JSON-shape post-processing (alternatives extraction, measure-number
annotation, pcMask computation).

The Iter 87 post-merge MinorSeventh re-stamp belongs *inside* this shared
function (so it fires consistently on both paths). The `backfillNextRootPc`
pass belongs there too. `absorbShortRegions` with the Iter 78 Fix A
`sharesPrevRoot` guard belongs there too.

### 5.5 Pedal-window collection

Lift the bridge's `buildPedalWindowIndex` out of the `notation::internal`
namespace into the new shared module. Delete the inline batch copies.

### 5.6 Mode-prior presets (`applyPreset` in batch vs `modePriorPresets()` in composingconfiguration)

Either (a) batch links the composing module's preset table directly (preferred —
single source of truth), or (b) the preset table moves to a header that both
TUs include. The current "keep in sync" comment is fragile.

### 5.7 Dead code cleanup

- Remove `detectHarmonicBoundariesJaccard` from `batch_analyze.cpp` (224 dead
  lines).
- Audit any remaining "retained for reference" comments and delete if Iter 54+
  greedy-expand is the only used path.

### 5.8 Order of operations (least-risk to most-risk)

1. **Constants and trivial helpers first** (§5.2). Zero behavior change; both
   paths call the same compile-time constants. Tests should be green
   unchanged.
2. **Pedal-window collection** (§5.5). Pure refactor.
3. **`collectRegionTones` shared implementation** (§5.1). This *will* change
   behavior on one path or the other; flag-gate the bass-passing-tone filter
   and look-ahead exclusion so both paths can be brought to parity in a
   controlled BIR comparison.
4. **Key resolution unification** (§5.3). Bring the strong-declared-mode prior
   to both paths; expect chord-output diffs.
5. **Orchestrator unification** (§5.4). The big one. Requires both BIR baselines
   and pipeline snapshot goldens to be re-anchored.
6. **Mode-prior preset table** (§5.6). Easy if (a); medium if (b).
7. **Dead code removal** (§5.7). Last, after confidence the bridge-side paths
   are exercised by the shared code.

---

## 6. Pointers to the existing TODO notes

The codebase already acknowledges the duplication in three places. Anything
addressed below should also remove the TODO it references:

- [`notationcomposingbridgehelpers.h:82-83`](../src/notation/internal/notationcomposingbridgehelpers.h#L82-L83):
  `TODO (ARCHITECTURE.md §2.10): duplicate of batch_analyze.cpp's regionMetricWeightForBeatType.`
- [`notationcomposingbridgehelpers.cpp:833-835`](../src/notation/internal/notationcomposingbridgehelpers.cpp#L833-L835):
  `TODO (ARCHITECTURE.md §2.10 / §4.1c): duplicate of batch_analyze.cpp's collectRegionTones.`
- [`batch_analyze.cpp:404-450`](../tools/batch_analyze.cpp#L404-L450):
  `TODO(Rule 10): The batch-side helpers below mirror live bridge logic ... Move shared note collection, boundary detection, key resolution, and temporal-context code into src/composing/ so the bridge and batch_analyze call one implementation.`

ARCHITECTURE.md §2.10 (the "Bridge and batch use the same segmentation" item
that Iter 77 marked "resolved") covers only the *segmentation* layer — not the
tone collection, region orchestration, key resolution, or temporal-context
plumbing that this audit found.

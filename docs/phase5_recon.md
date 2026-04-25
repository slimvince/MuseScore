# Phase 5 — Modulation-Aware Annotation Recon

Date: 2026-04-25  
Scope: read-only, no source edits.  
Base commit: `36368d67cc` (Phase 4b — `analyzeSection` canonical)

---

## Recommended implementation shape

**2-session split (5a → 5b).**  Evidence: engraving support requires no new
capability (Q1 — text-only is sufficient); DCML key labels exist and are ban-free
(Q2); `NoteHarmonicContext` needs only a small additive field (Q3); but the current
`analyzeSection` KeyArea derivation is missing the confidence gate described in
`unified_analysis_pipeline.md`, and empirical observation of actual KeyArea spans
is needed before writing the modulation annotation emitter (Q4 — risk: medium).

---

## Q1 — MuseScore engraving capability for pivot notation

### Parser path

`HarmonyType::ROMAN` parsing is a no-op
(`src/engraving/dom/harmony.cpp:522–527`):

```cpp
if (m_harmonyType == HarmonyType::ROMAN) {
    info->setTextName(s);
    info->setRootTpc(Tpc::TPC_INVALID);
    info->setBassTpc(Tpc::TPC_INVALID);
    return nullptr;
}
```

Any string — including `I=IV`, `vi→ii`, `♭VII`, or random text — is accepted
verbatim, stored in `HarmonyInfo::m_textName`, and marked non-realizable via
`TPC_INVALID`. No rejection, no crash, no parsing. This is by design: Roman
numerals are key-relative and MuseScore makes no attempt to understand their
structure.

For `HarmonyType::STANDARD` (chord symbols), equals signs are stripped during
display (`harmony.cpp:226–228`). For `ROMAN`, no such stripping applies — the
string is rendered exactly as stored.

### Formatter path

`harmonyName()` (`harmony.cpp:198–269`) returns `info->textName()` for Roman
numerals. **There is no special typography** for conventions like `I=IV` or
`vi→ii`. The formatted output is the raw stored string. Consequence: any label
our emitter writes is rendered exactly as written — a useful property that
requires no engraving workarounds.

### Metadata: no pivot fields

The `Harmony` class (`harmony.h:211–356`) and `HarmonyInfo` struct
(`harmony.h:155–203`) have no fields or methods exposing pivot status, modulation
identity, or dual-key membership. The element is purely a text+format container.

### Transposition

`transposeHarmony()` (`transpose.cpp:548–575`) operates on `rootTpc` and
`bassTpc`. Both are `TPC_INVALID` for Roman numerals, so **Roman numerals are
silently not transposed**. When a score is transposed, Romans remain unchanged
and reinterpret relative to the new key signature — the correct semantic.

### Existing pivot detection

`detectPivotChords` (`notationcomposingbridgehelpers.cpp:1697–1808`) already
produces pivot labels in format `"vi → ii"` (U+2192 RIGHT ARROW, e.g.
`"vi → ii"` when moving from the outgoing to the incoming key). These are
written to `HarmonyType::ROMAN` Harmony elements by the annotation emitter
(`notationcomposingbridge.cpp`). The `→` format is established in the codebase
and renders correctly.

### Verdict

**Text-only support.** MuseScore accepts any Roman numeral string verbatim and
renders it literally. `I=IV` would display as plain text, not as
specially-typeset notation. However, this is entirely adequate for Phase 5:
modulation transitions are communicated via text labels our emitter writes to
ROMAN elements. The `→` format (`"vi → ii"`) is already used by `detectPivotChords`
and is the obvious convention to extend for key-area annotations. No new
engraving capability is needed, and no convention investigation is required —
the answer is already in the codebase.

No quirks to work around. No sub-recon needed.

---

## Q2 — Authoritative corpora for modulation tuning

### Chord-symbol-ban applicability

`docs/symbol_input_audit.md` states the operating principle:

> Symbols are instructions written by the user, not analysis results. Production
> paths must not read them as input to analysis. Tools may read them only as
> comparison/ground-truth labels — never as input that influences what the analyzer
> computes.

This ban applies to **Harmony elements** (DOM objects) as analysis input. It does
not apply to external TSV/CSV files (DCML key labels are flat data files, not
Harmony elements). The audit's §A confirms: "Production retirement complete: YES.
No production path … reads a `Harmony` element … to influence analysis output."
Key label files from DCML are a completely different data source and are not
subject to this ban.

### DCML corpus key labels

`tools/dcml/` contains 12 collections with 1,538 MSCX scores. Ten of twelve
collections have harmonic TSV sidecar files:

| Collection | TSV files | Notes |
|---|---:|---|
| `corelli/` | 149 | Full globalkey/localkey per annotation |
| `mozart_piano_sonatas/` | 54 | Modulation-bearing; flagged in `unified_analysis_pipeline.md:267` |
| `chopin_mazurkas/` | 55 | Modulation-bearing; mentioned in `docs/divergence_c_observation.md:74` |
| `bach_en_fr_suites/` | 89 | — |
| `cpe_bach_keyboard/` | 66 | — |
| `grieg_lyric_pieces/` | 66 | — |
| `schumann_kinderszenen/` | 13 | — |
| `dvorak_silhouettes/` | 12 | — |
| `ABC/` | 71 | — |
| `tchaikovsky_seasons/` | 12 | — |
| `bach_chorales/` | **0** | README: "labels: 0" — structural metadata only (measures/, notes/) |
| `when_in_rome/` | uncertain | Anthology/Code/Corpus structure; no harmonies/ subdirectory confirmed |

**TSV format**: two columns of primary interest — `globalkey` (tonal center of the
piece or section, e.g. `F` for F major, `b` for B minor) and `localkey` (local
Roman numeral context, e.g. `I`, `V`, `iv`). Modulations are tracked by
`localkey` transitions. There is no dedicated "modulation" column; key areas are
inferred from spans where `localkey` or `globalkey` changes.

### Snapshot corpus overlap

Two corpus scores that modulate are in the 10-score pipeline snapshot harness:
`chopin_bi105_op30_2` (Mazurka Op. 30 No. 2 — "adds modulation and chromatic
colour", per `divergence_c_observation.md:74`) and the Mozart sonatas. Chopin
has corresponding TSV files in `tools/dcml/chopin_mazurkas/harmonies/`.

### Tooling requirement

No current infrastructure compares `AnalyzedSection.keyAreas` output against DCML
TSV key labels. Extracting globalkey/localkey transitions from DCML TSVs and
aligning them with `KeyArea` spans would require new tooling. The effort is modest
(Python script, ~100 LOC) but is not yet done.

### Verdict

DCML key labels are usable for modulation-detection tuning (**yes-with-tooling**).
The ban on chord-symbol input does not apply. The primary modulation-rich
collections (Corelli 149, Mozart 54, Chopin 55) overlap with the pipeline snapshot
corpus and are immediately available for comparison. New tooling is needed to
automate the comparison; it can be developed as part of Phase 5a or 5b.

---

## Q3 — `NoteHarmonicContext` and status-bar surface today

### Current fields

`NoteHarmonicContext` (`notationcomposingbridge.h:56–75`):

```cpp
struct NoteHarmonicContext {
    std::vector<ChordAnalysisResult> chordResults;  // candidates, rank-ordered
    int keyFifths = 0;
    KeySigMode keyMode = KeySigMode::Ionian;
    double keyConfidence = 0.0;
    ChordTemporalExtensions temporalExtensions;     // Phase 3c
    bool wasRegional = true;                        // Phase 3c
};
```

**Key-related data present**: `keyFifths`, `keyMode`, `keyConfidence`. No
`KeyArea` field. No modulation label.

### Status-bar path

1. `harmonicAnnotation(Note*)` (`notationcomposingbridge.cpp:474–584`): entry
   point. Calls `analyzeNoteHarmonicContextDetails(note)` (line 482), extracts
   `keyFifths`, `keyMode`, `keyConfidence` (lines 483–485). Builds a string in
   the form `"Chord: Dm (0.88) | D (0.76) in key: F Major"` using
   `ChordSymbolFormatter::formatSymbol/RomanNumeral/NashvilleNumber`.
2. Consumer: `notationaccessibility.cpp:204` appends the returned string to the
   status bar.

### Right-click menu path

`appendAnalysisItemsForContext` (`notationcontextmenumodel.cpp:55–164`) receives a
pre-populated `NoteHarmonicContext`, reads `context.keyFifths` for the formatter
(line 58), iterates `chordResults` (line 92), and builds symbol/Roman/Nashville
submenus. `KeyArea` is not referenced.

### `KeyArea` current status

`AnalyzedSection.keyAreas` is produced by `analyzeSection` and consumed in the
P3 path (`analyzeNoteHarmonicContextRegionallyInWindow`,
`notationcomposingbridge.cpp:244`) — but the matched `AnalyzedRegion.keyAreaId`
is **not propagated to `NoteHarmonicContext`**. The section is constructed inside
`analyzeNoteHarmonicContextRegionallyInWindow` and discarded after the matched
region is extracted.

### Cleanest KeyArea slot-in

Add a `KeyArea` value copy to `NoteHarmonicContext`:

```cpp
std::optional<mu::composing::analysis::KeyArea> enclosingKeyArea;
```

Populated from `section.keyAreas[matchedRegion.keyAreaId]` inside
`analyzeNoteHarmonicContextRegionallyInWindow`; left as `std::nullopt` on the P4
fallback path (which has no region concept). The `harmonicAnnotation` formatter
then has the `startTick`, `endTick`, `keyFifths`, `mode`, and `confidence` of the
enclosing key area and can append modulation context.

**Ripple cost**: small. `NoteHarmonicContext` is a value type; adding a field adds
one optional (`~24 bytes`). The only construction sites are
`analyzeNoteHarmonicContextRegionallyInWindow` and the P4 path; both have
contained scopes.

The `harmonicAnnotation` formatter signature (`std::string harmonicAnnotation(const Note*)`)
does not need to change — the additional context travels through the populated
struct.

### Verdict

The bridge surface is well-understood. The slot-in is low-cost, low-ripple, and
follows the Phase 3c precedent (`wasRegional` and `temporalExtensions` were added
by the same mechanism). No sub-recon needed.

---

## Q4 — `KeyArea` production logic post-4b

### KeyArea derivation in `analyzeSection`

The collapsing loop is near the end of `analyzeSection`
(`notationcomposingbridgehelpers.cpp`, post-4b):

```cpp
if (out.keyAreas.empty()
    || out.keyAreas.back().keyFifths != regionFifths
    || out.keyAreas.back().mode != regionMode) {
    // open new KeyArea
} else {
    // extend existing KeyArea; confidence = max of merged regions
}
```

**Fields compared**: `keySignatureFifths` and `mode`. **No confidence gate.**
A new `KeyArea` opens whenever the key or mode changes, regardless of how
confident the per-region key analysis is. `KeyArea.confidence` is the maximum
`normalizedConfidence` across all merged regions.

**Deviation from design**: `unified_analysis_pipeline.md:149–163` specifies a
confidence-gated algorithm: a new key area should open only when the diverging
region clears the assertive-confidence threshold (0.8). Regions that disagree
with the enclosing area but don't clear the threshold should be assigned to the
enclosing area via `keyAreaId` while retaining their own `keyModeResult`. The
current Phase 4b implementation is simpler — it opens a new key area on any key
change — and is explicitly flagged in the doc as "initial sketches; Phase 5
tunes empirically."

### `stabilizeHarmonicRegionsForDisplay` smoothing

`stabilizeHarmonicRegionsForDisplay` (`notationcomposingbridgehelpers.cpp:246–311`)
applies one round of hysteresis:

```
for each region i:
    if key[i] differs from stableKey:
        persistent = (i is last) OR (key[i+1] == key[i])
        if persistent: update stableKey
    region[i].keyModeResult = stableKey  // always overwrite with stable
```

**Effect**: a single-region key deviation is suppressed — the region inherits the
prior stable key. A two-consecutive-region deviation is accepted and propagates
forward. This runs **before** KeyArea derivation, so single-region transients
never reach KeyArea collapsing. Only two-or-more consecutive key changes become
a new `KeyArea`.

### `resolveKeyAndMode` hysteresis

`resolveKeyAndMode` (`notationcomposingbridgehelpers.cpp:525–722`) accepts a
`prevResult` parameter. When non-null, it applies a margin test: if the top-scoring
mode differs from `prevResult->mode`, the switch is accepted only when the new
mode's score exceeds `prevResult`'s score by `hysteresisMargin` (or
`relativeKeyHysteresisMargin` when only the mode changes). This is called in
`analyzeHarmonicRhythm` (`notationharmonicrhythmbridge.cpp`) with the prior
region's result, so smoothing occurs at the per-region key-analysis level before
`stabilizeHarmonicRegionsForDisplay` runs.

Two smoothing layers therefore exist before KeyArea derivation:
1. **Per-region hysteresis** in `resolveKeyAndMode` (prevents single-region blips).
2. **Stabilization pass** in `stabilizeHarmonicRegionsForDisplay` (suppresses
   isolated single-region survivors).

### Predicted behavior on V/V tonicization

Scenario: 4 beats (one region) of D-major harmony in a C-major piece.

1. `resolveKeyAndMode` with `prevResult = C major` context:
   D-major pitch evidence (D, F#, A) is strong; the hysteresis margin is overcome
   → region labeled D Ionian.
2. `stabilizeHarmonicRegionsForDisplay`: only one D-region exists; the next region
   returns to C → **NOT persistent** → D-region is clamped to C major.
3. `KeyArea` derivation: no new `KeyArea` opens. The V/V tonicization stays inside
   the enclosing C-major area. ✓

Scenario: 8 beats (two consecutive regions) of D-major harmony:

1. Both regions labeled D Ionian.
2. `stabilizeHarmonicRegionsForDisplay`: two consecutive D-regions → **persistent**
   → both stay D Ionian.
3. Current (no-gate) KeyArea derivation: new D-major `KeyArea` opens.
4. With the planned confidence gate (0.8): if the per-region `normalizedConfidence`
   of the D-regions meets threshold, the gate passes; if it's a brief tonicization
   with weak evidence, the gate suppresses it and the regions are grouped into the
   enclosing C-major area.

The confidence gate is Phase 5b's primary algorithmic addition to `analyzeSection`.

### `keyAreas` length

No guarantee. Empirically: ≥ 1 when `regions` is non-empty (the first region
always opens an area), 0 only when `regions` is empty and `analyzeSection` returns
early.

### Verdict

Production logic is **reasonable but incomplete**. Two smoothing layers
(per-region hysteresis + stabilization) already suppress most single-region noise.
The missing confidence gate is a clean, well-specified addition (0.8 threshold,
following `unified_analysis_pipeline.md:151`). The Q4 analysis can be done from
code; empirical observation (Phase 5a) is needed to determine whether the
two-consecutive-region threshold is set correctly and whether `stabilizeHarmonicRegionsForDisplay`'s
two-region criterion is too liberal for real-world music.

---

## Q5 — Synthesis and Phase 5 implementation shape

### Dependency order

```
docs state         code state           risk
─────────────────────────────────────────────────
5a: add KeyArea    add KeyArea to       low
   snapshot        snapshot + fix
   observation     confidence gate

5b: modulation     add KeyArea to       medium
   annotation      NoteHarmonicContext;
   emitter         implement annotation
                   emitter
```

No sub-recons required before 5a. The Q4 finding (missing confidence gate) is
actionable from code inspection. The Q1 finding (text-only support sufficient)
eliminates an engraving investigation. The Q2 finding (DCML labels available,
ban does not apply) is settled.

### Phase 5a — Empirical observation + confidence gate

**Scope:**

- Add `keyAreas` JSON array to the pipeline snapshot harness
  (`pipeline_snapshot_tests.cpp`). Shape: `[{"startTick": …, "endTick": …,
  "keyFifths": …, "mode": …, "confidence": …}]` per score. Additive field; existing
  snapshot entries unchanged.
- Implement the confidence-gated `KeyArea` derivation in `analyzeSection` per
  `unified_analysis_pipeline.md:149–163`. Open a new `KeyArea` only when the
  diverging region's `normalizedConfidence ≥ 0.8`. Regions that disagree but fall
  below threshold retain their own `keyModeResult` (status-bar remains accurate)
  but receive the enclosing area's `keyAreaId`.
- Regenerate golden snapshots. The snapshot diff for the `keyAreas` field is the
  first empirical view of key-area spans across the 10-score corpus.

**Snapshot impact**: new `keyAreas` field in all 10 snapshots; `implode`,
`annotation`, and `tickRegional` arrays unchanged (confidence gate affects only
`keyAreaId` assignment and `keyAreas` vector, not per-region chord results).

**Behavior-preservation risk**: **low**. The confidence gate changes `keyAreaId`
assignments silently; no user-visible behavior changes until the annotation emitter
consumes `KeyArea` (Phase 5b). All existing tests pass unchanged.

**Deliverable**: The 5a snapshot diff provides the empirical data needed to assess
whether the 0.8 threshold is well-calibrated on real music. If the Chopin and
Mozart scores show sensible modulation boundaries (matching domain knowledge of
where those pieces modulate), 5b can proceed. If the thresholding reveals
unexpected behavior, a scope adjustment for 5b is possible without regressions.

### Phase 5b — Modulation-aware annotation emitter

**Scope:**

- Add `std::optional<KeyArea> enclosingKeyArea` field to `NoteHarmonicContext`
  (`notationcomposingbridge.h:56`). Populate from the matched region's
  `keyAreaId` inside `analyzeNoteHarmonicContextRegionallyInWindow`
  (`notationcomposingbridge.cpp:226–306`).
- Extend `harmonicAnnotation` formatter to surface the enclosing key area when
  present and when it differs from the per-region key (i.e., when the region is
  assigned to an enclosing area that smoothed a local key deviation).
- Extend the annotation emitter (`notationcomposingbridge.cpp:756` /
  `emitHarmonicAnnotations` path) to:
  - Write Romans relative to the **enclosing `KeyArea`** key/mode, not the
    per-region key, when `useKeyAreaRelativeRomanNumerals = true`
    (per `unified_analysis_pipeline.md:195`).
  - Write key-change annotations at `KeyArea` boundary ticks using the
    existing `detectPivotChords` `→`-format convention.
- Design decision: notation format for modulation labels. Two options consistent
  with existing code:
  1. **Key-area boundary labels**: write a `ROMAN` Harmony element at the first
     tick of each new `KeyArea` reading e.g. `"[in D:]"` or simply use the
     existing pivot format `"vi → ii"` already implemented in `detectPivotChords`.
  2. **Roman numeral key-prefix form**: write `"D: I"` at modulation targets
     (prefix style common in theory pedagogy).
  The decision is deferred to the Phase 5b implementation prompt; the options
  are noted here. Both are viable given text-only engraving support (Q1).
- Update snapshot goldens; expect annotation diffs on the modulating scores
  (Chopin `bi105_op30_2`, Mozart K.279/K.280, Corelli Op. 1 No. 8).

**Snapshot impact**: expected on modulating scores' `annotation` arrays.
`implode`, `tickRegional`, `tickLocal` arrays are unaffected (they don't emit
Harmony elements). The diff shape is: modulating scores gain additional
`HarmonyType::ROMAN` entries at `KeyArea` boundary ticks, and Roman numerals
in the new key after a modulation shift their degree numbers. This is the Phase 5
"expected behavior change" diff profile; any other diff is a regression.

**Behavior-preservation risk**: **medium**. The annotation output changes on
modulating scores, which is the intended effect. Non-modulating scores
(all-Bach corpus: `bach_chorale_001`, `bach_chorale_003`, `bach_bwv806_prelude`,
`bach_bwv806_gigue`, `schumann_kinderszenen_n01`) should be byte-identical because
they have a single `KeyArea` and no key transitions.

### Is Phase 5c needed?

Deferred until after 5a. If 5a's snapshot reveals systematic noise (e.g., the
Baroque dance forms show spurious inter-measure key-area boundaries), a Phase 5c
threshold-tuning session would be warranted. Based on Q4's code analysis
(double smoothing already in place, `stabilizeHarmonicRegionsForDisplay` already
suppresses 1-region transients), the baseline noise is expected to be low. The
confidence gate at 0.8 is the assertive-confidence constant already used by
`hasAssertiveKeyConfidence`, `kAnnotateKeyConfidenceThreshold`, and cadence/pivot
detection — it has empirical standing in the existing code.

### Boundary conditions / open design questions

1. **`minimumDisplayDurationBeats` interaction** (`unified_analysis_pipeline.md:191`,
   divergence C): `divergence_c_observation.md` found 1 sub-beat region across
   10 corpus scores. The gate's effect on modulation annotation is negligible. No
   action in Phase 5.

2. **P4 fallback**: the tick-local path (`analyzeHarmonicContextLocallyAtTick`)
   produces no `AnalyzedSection` and therefore no `KeyArea`. The `enclosingKeyArea`
   field on `NoteHarmonicContext` stays `std::nullopt` on the fallback path, and
   the formatter degrades gracefully to the current behavior.

3. **`batch_analyze.cpp` impact**: `prepareUserFacingHarmonicRegions` shim
   (introduced in Phase 4b) insulates the tool from `analyzeSection` changes.
   The confidence gate modifies `keyAreaId` assignment on `AnalyzedRegion` but
   `HarmonicRegion` (which the shim returns) has no `keyAreaId` field. No
   tool-side impact.

4. **`detectPivotChords` relationship**: `detectPivotChords` operates at region
   granularity and identifies the specific *chord* that is reinterpreted.
   Phase 5b's modulation-aware annotation operates at `KeyArea` granularity and
   controls which *key* the Roman numerals are written in. The two mechanisms are
   complementary and should coexist: pivot-chord labels at the transition region,
   key-area-relative Romans from that point forward.

---

## Summary table

| Question | Finding | Action in Phase 5 |
|---|---|---|
| Q1 — Engraving | Text-only; any string renders as typed; `→` format already in codebase | No new engraving work; use existing `detectPivotChords` convention |
| Q2 — Corpora | DCML key labels in 10/12 collections; ban does not apply to TSV files | New comparison tooling optional; use Chopin/Mozart/Corelli as ground truth |
| Q3 — Bridge surface | `NoteHarmonicContext` needs one `optional<KeyArea>` field; formatter is in `harmonicAnnotation` | Low-cost additive change in Phase 5b |
| Q4 — KeyArea logic | Confidence gate missing; two smoothing layers otherwise sound | Add confidence gate in Phase 5a; annotation emitter in Phase 5b |
| Q5 — Split | 2 sessions (5a observation+gate, 5b emitter) | Promote to 3 only if 5a reveals threshold noise |

**Most surprising finding**: the current `analyzeSection` KeyArea derivation
(introduced in Phase 2, unchanged through Phase 4b) implements a simpler
algorithm than the one documented in `unified_analysis_pipeline.md:149–163`. The
doc specifies a confidence gate (regions below 0.8 stay in the enclosing area
via `keyAreaId`); the code opens a new `KeyArea` on any key change regardless of
confidence. This is not a regression — the doc explicitly flags it as an "initial
sketch" to be tuned in Phase 5 — but it means Phase 5a carries both the empirical
observation goal AND a real code fix, not just additive plumbing.

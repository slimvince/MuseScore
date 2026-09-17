# Refactor #1 — `chordanalyzer.cpp` layer-split: READ-ONLY design dossier

> **Status:** READ-ONLY design. No code moved, HEAD unchanged (`5fee657578`). This is the
> **spec for the byte-identical split build** (the follow-on instruction). Frame: a pure
> code-movement refactor that decomposes the 3,679-line `chordanalyzer.cpp` into
> single-responsibility translation units, each move independently verifiable byte-identical
> (BIR 57/23/57, both suites green, snapshots unchanged, `.ours.json` 0-diff on all 3 presets).
>
> **Gitignored / HELD** (`cc_*.md`, `.gitignore:118`). Do not commit without an approval file.
>
> All line numbers are against `src/composing/analysis/chord/chordanalyzer.cpp` @ `5fee657578`
> unless another file is named.

---

## §0 — Executive summary

- `chordanalyzer.cpp` (3,679 lines) conflates **six** distinct responsibilities in one TU:
  the vertical scoring **oracle** + result construction, the **post-scoring gate layer A–L**,
  the **Iter-86/91/pedal tail**, the **diagnose replay**, the **chord-symbol/RN/Nashville
  formatter**, and the **keyboard-reduction voicing**.
- The **competition / function scoring pipeline is ALREADY a separate TU**
  (`function/harmonicfunctionlayer.cpp`): `analyzeChord` builds the vertical-only
  `ScoringSnapshot` and hands it to `fn::applyHarmonicFunction` ([chordanalyzer.cpp:2766](src/composing/analysis/chord/chordanalyzer.cpp#L2766)).
  So there is **no competition layer to extract here** — the residual of this file *is* the oracle.
- Proposed decomposition: **residual `chordanalyzer.cpp` (the oracle) + 5 new sibling TUs.**
  The **gate layer is isolated into its own TU last** — that TU is the refactor-#2 dissolution target.
- The `kTemplateCount` size model is **invariant under this split**: all three derived arrays
  (the `templates` array + the three score matrices in `analyzeChord`; `kMasks` in
  `harmonicfunctionlayer.cpp`) stay in their current TUs. No size-model obstruction.
- Unity/jumbo ODR is the one real mechanical hazard — handled by the established `jkd*`/`lmd*`
  anon-namespace **prefix precedent** (internal-linkage rename ⇒ byte-identical).
- **Tangles found** (§7): `buildChordResult` is shared infrastructure (kept with the oracle,
  reached cross-TU via the header), `isBassChordTone` is mis-grouped, and diatonic-scale tables
  are triplicated. None blocks the byte-identical split; all are noted for the layer audit / refactor #2.

---

## §1 — Current-file map (line-ranged, with single responsibility)

### Structural skeleton

| Lines | Element |
|---|---|
| 1–21 | License header |
| 23–31 | Includes: `chordanalyzer.h`, `analysisutils.h`, `function/harmonicfunctionlayer.h`; `<algorithm> <array> <cmath> <limits> <utility>` |
| 33 | `namespace fn = mu::composing::function;` |
| 35 | `namespace mu::composing::analysis {` |
| 36 | anonymous namespace opens |
| **1557** | `} // namespace` (anon ns closes) |
| 1559–3380 | named-namespace function definitions |
| 3382–3466 | `namespace ChordSymbolFormatter { … }` (Nashville sub-block) |
| 3468–3678 | voicing + factory |
| 3679 | `} // namespace mu::composing::analysis` |

### Anonymous namespace (36–1556) — TWO disjoint groups, clean boundary at line 619/621

**Group A — FORMATTING helpers (44–619)** — consumed *only* by the formatter functions:

| Lines | Symbol | Used by |
|---|---|---|
| 44–67 | `pitchClassName` | `pitchClassNameFromTpc` (193) |
| 86–194 | `pitchClassNameFromTpc` | `formatSymbol` (3149/3153/3162/3189) |
| 196–447 | `qualitySuffix` | `formatSymbol` (3163) |
| 456–485 | `chromaticRoman` | `formatRomanNumeral` (3260) |
| 487–619 | `diatonicRoman` | `formatRomanNumeral` (3269/3273) |

**Group B — SCORING constants + helpers (621–1556)** — consumed by `analyzeChord` and
`buildChordResult` (all internal to one prospective TU, except `isBassChordTone`):

| Lines | Symbol | Used by |
|---|---|---|
| 621–665 | `coreIntervals` | `categorizeExtraNote` (831) |
| 679 | `enum ExtraNoteCategory` | scoring |
| 685–756 | scoring constants (`kContradictionPenalty`…`kExtensionThreshold` 756, `kSeventhThreshold` 751, factors, sus/dim/dom7 penalties) | scoring helpers + `detectExtensions` |
| 774–866 | `categorizeExtraNote` | `scoreExtraNotes` (1073) |
| 868–885 | `struct ExtensionFlags` | `detectExtensions`, `buildChordResult` |
| 887–1000 | `detectExtensions` | **`buildChordResult`** (1614/1619/1635) |
| 1010–1021 | `struct TemplateDef` | `analyzeChord` + all scoring helpers |
| 1023–1044 | `scoreTemplateTones` | `analyzeChord` (2590) |
| 1046–1120 | `scoreExtraNotes` | `analyzeChord` (2591) |
| 1122–1158 | `dim7CharacteristicBonus` | `analyzeChord` (2592) |
| 1160–1165 | `struct TpcMatchCounts` | `countTpcMatches` |
| 1167–1200 | `countTpcMatches` | `structuralPenalties` (1219), `tpcConsistencyBonus` (1322) |
| 1202–1228 | `nonBassAdjustment` | `analyzeChord` (2700) |
| 1230–1316 | `structuralPenalties` | `analyzeChord` (2593) |
| 1318–1324 | `tpcConsistencyBonus` | `analyzeChord` (2594) |
| 1326–1375 | `bassRootBonusMultiplier` | `appliedBassRootBonus` (1452) |
| 1377–1386 | `templateHasMatchingThird` | `qualifies…`/`supports…` (1421/1439) |
| 1388–1397 | `templateHasMatchingFifth` | `qualifies…` (1422) |
| 1399–1423 | `qualifiesForCompleteTriadInversionBonus` | `analyzeChord` (2724) |
| 1425–1440 | `supportsContextualInversionBonuses` | `analyzeChord` (2721) |
| 1442–1461 | `appliedBassRootBonus` | `analyzeChord` (2694) |
| **1463–1527** | **`isBassChordTone`** (`static`) | **`applyIter8691Pedal` ONLY** (2897) |
| 1544–1555 | `diatonicRootContribution` | `analyzeChord` (2595) |

> Verified self-containment: `detectExtensions` ([887](src/composing/analysis/chord/chordanalyzer.cpp#L887)) calls **no** other anon-ns helper
> (only the threshold constants + `ChordQuality`/`Extension`); `isBassChordTone`
> ([1463](src/composing/analysis/chord/chordanalyzer.cpp#L1463)) calls **only** `hasExtension` (header inline) + enums.

### Named-namespace functions (1559–3380)

| Lines | Symbol | Responsibility | Internal deps |
|---|---|---|---|
| 1559–1701 | `buildChordResult` *(header-decl)* | Construct/normalize a `ChordAnalysisResult` from a `RawCandidate` (Aug-root correction, Sus→Maj, extension detect, degree/diatonic check) | `detectExtensions` |
| **1703–2255** | **`applyPostScoringGates`** *(header-decl)* | **The post-scoring identity gate layer A–L** | `buildChordResult` (header) only |
| 2257–2782 | `RuleBasedChordAnalyzer::analyzeChord` | **The vertical oracle:** pcWeight histogram, bass enumeration, template array, the three score matrices, `ScoringSnapshot` build, `fn::applyHarmonicFunction` call | scoring helpers; `fn::applyHarmonicFunction` (header) |
| 2792–2968 | `applyIter8691Pedal` *(header-decl)* | Iter-86 (bass-b7), Iter-91 (bass-as-root), two-pass pedal detection | `buildChordResult` (header), **`isBassChordTone`** |
| 2970–3123 | `RuleBasedChordAnalyzer::diagnoseChord` | Replay production pipeline + decorate ORACLE/COMPETITION/POST-GATES view | `analyzeChord`/`applyIter8691Pedal`/`applyPostScoringGates` (header) + `fn::` public fns — **no anon-ns helper** |
| 3129–3139 | `isValidBassNoteName` (`static`) | formatter helper (`std::isupper`) | — |
| 3141–3197 | `ChordSymbolFormatter::formatSymbol` | chord-symbol string | `pitchClassNameFromTpc`, `qualitySuffix`, `isValidBassNoteName` |
| 3199–3239 | tonicization tables + `diatonicDegreeForPc` (3221) + `isDegreeMajorThird` (3234) | formatter helpers (V/x, viio/x labels) | — |
| 3241–3379 | `ChordSymbolFormatter::formatRomanNumeral` | Roman-numeral string | `chromaticRoman`, `diatonicRoman`, tonicization helpers |

### `namespace ChordSymbolFormatter { }` (3382–3466) + voicing/factory (3468–3678)

| Lines | Symbol | Responsibility |
|---|---|---|
| 3384–3435 | anon ns: `nashvilleDegree`/`nashvilleQualitySuffix`/`nashvilleExtensionSuffix`/`nashvilleBassSuffix` | Nashville formatter helpers |
| 3437–3464 | `formatNashvilleNumber` | Nashville string |
| 3470–3613 | `chordTonePitchClasses` *(header-decl)* | idealized chord-tone pc set (header-only deps) |
| 3617–3668 | `closePositionVoicing` *(header-decl)* | keyboard reduction voicing (calls `chordTonePitchClasses`) |
| 3670–3677 | `ChordAnalyzerFactory::create` | factory → `RuleBasedChordAnalyzer` |

---

## §2 — Mapping onto the architecture's layers

| Architecture layer | Where it lives now | Action in refactor #1 |
|---|---|---|
| **Vertical oracle** | `analyzeChord` (2257–2782) + scoring helpers (Group B 621–1556 minus `isBassChordTone`) + `TemplateDef`/template array + `buildChordResult` (1559–1701) | **Residual** of `chordanalyzer.cpp` (does not move) |
| **Competition + function scoring** | **Already extracted** → `function/harmonicfunctionlayer.cpp` (reached via `fn::applyHarmonicFunction`, 2766) | Untouched |
| **Post-scoring gates A–L** | `applyPostScoringGates` (1703–2255) | → **`postscoringgates.cpp`** (own TU; refactor-#2 target) |
| **Post-competition tail** (Iter 86/91/pedal) | `applyIter8691Pedal` (2792–2968) + `isBassChordTone` | → **`chordpostpasses.cpp`** |
| **Diagnose / replay** | `diagnoseChord` (2970–3123) | → **`chorddiagnose.cpp`** |
| **Formatting** (symbol/RN/Nashville) | `formatSymbol`/`formatRomanNumeral`/`formatNashvilleNumber` + formatting helpers (Group A 44–619, 3129–3239, 3384–3435) | → **`chordsymbolformatter.cpp`** |
| **Voicing** (keyboard reduction) | `chordTonePitchClasses`, `closePositionVoicing` | → **`chordvoicing.cpp`** |
| Shared helper | `buildChordResult` (called by oracle, gates, tail) | Stays with oracle; exposed via header (§7-T1) |

Sections whose responsibility is **split / tangled** → §7.

---

## §3 — Target file decomposition (TUs + interfaces)

All new TUs are added to [analysis/CMakeLists.txt](src/composing/analysis/CMakeLists.txt) `target_sources(composing_analysis …)` under the
existing `chord/` group. **`chordanalyzer.h` is unchanged** — it is the stable integration
boundary for ~40 consumers (the notation bridge, `tools/batch_analyze.cpp`, every
`region/`/`section/`/`function/` TU, and all tests). Every new TU `#include`s it.

### Residual — `chord/chordanalyzer.cpp` (the vertical oracle)
- **Boundary:** pcWeight/bass enumeration, the template vocabulary, the three score matrices,
  `ScoringSnapshot` construction, the `fn::applyHarmonicFunction` call, and result construction.
- **Holds:** scoring constants (685–756), scoring helpers (Group B minus `isBassChordTone`),
  `TemplateDef`, `detectExtensions`, `buildChordResult`, `RuleBasedChordAnalyzer::analyzeChord`,
  `ChordAnalyzerFactory::create`.
- **Public interface (in `chordanalyzer.h`, unchanged):** `IChordAnalyzer::analyzeChord`,
  `RuleBasedChordAnalyzer::analyzeChord`, `buildChordResult`, `ChordAnalyzerFactory::create`.
- **Owns the size model:** the `templates` array (2494–2512), `static_assert` (2513), and the
  three `std::array<std::array<double, kTemplateCount>,12>` matrices (2553–2555).

### New TU 1 — `chord/chordsymbolformatter.cpp` (chord labeling)
- **Holds:** `formatSymbol`, `formatRomanNumeral`, `formatNashvilleNumber` + ALL their helpers:
  Group A (44–619), `isValidBassNoteName`, tonicization tables, `diatonicDegreeForPc`,
  `isDegreeMajorThird`, the Nashville anon-ns helpers (3384–3435).
- **Interface:** the three `ChordSymbolFormatter::` functions (header-decl unchanged).
- **Includes:** `chordanalyzer.h`; `<string> <array> <cstdint> <cstddef> <cctype>` (the
  `isupper` in `isValidBassNoteName`). `endsWith`/`normalizePc` arrive transitively via
  `analysisutils.h` (included by `chordanalyzer.h`).

### New TU 2 — `chord/chordvoicing.cpp` (keyboard reduction)
- **Holds:** `chordTonePitchClasses`, `closePositionVoicing`. **No anon-ns helper** (local lambdas only).
- **Interface:** those two functions (header-decl unchanged).
- **Includes:** `chordanalyzer.h`; `<vector> <algorithm> <cmath>` (`std::abs`).

### New TU 3 — `chord/chorddiagnose.cpp` (diagnostic replay)
- **Holds:** `RuleBasedChordAnalyzer::diagnoseChord`. **No anon-ns helper** (local `sameIdentity` lambda).
- **Interface:** the method (header-decl unchanged).
- **Includes:** `chordanalyzer.h`; **`function/harmonicfunctionlayer.h`** (it reads
  `fn::ScoringSnapshot`/`fn::ScoringCell` and calls `fn::resolutionEdgeBonus`,
  `fn::inversionContextBonus`, `fn::rootContinuityBonus`, `fn::gateRZeroesRootContinuity`,
  `fn::wSeqBonus`, `fn::wStepInBonus`, `fn::wStepOutBonus`); `<algorithm> <vector>`.

### New TU 4 — `chord/chordpostpasses.cpp` (Iter-86/91/pedal tail)
- **Holds:** `applyIter8691Pedal` + `isBassChordTone` (relocated from the oracle anon ns).
- **Interface:** `applyIter8691Pedal` (header-decl unchanged).
- **Includes:** `chordanalyzer.h`; `<set>` (`std::set` pedal pass), `<cmath>` (`std::exp`),
  `<vector> <algorithm>`. Re-invokes `RuleBasedChordAnalyzer{}.analyzeChord` (header) for Pass 2.

### New TU 5 — `chord/postscoringgates.cpp` (gate layer A–L) — *refactor-#2 target*
- **Holds:** `applyPostScoringGates` (1703–2255). **No file-scope anon-ns helper** (local
  `buildResult` lambda → `buildChordResult`).
- **Interface:** `applyPostScoringGates` (header-decl unchanged).
- **Includes:** `chordanalyzer.h`; `<algorithm>` (`std::stable_sort`), `<vector>`.

> **Why `buildChordResult` stays with the oracle and is NOT its own TU:** it shares the
> threshold constants (`kSeventhThreshold`/`kExtensionThreshold`, 751/756) and `ExtensionFlags`
> with `detectExtensions` and the scoring helpers. Splitting it out would force those constants
> into a new shared header for zero behavioral gain. It is already header-declared, so the gate
> TU and the post-passes TU call it across the TU boundary with no new plumbing. (See §7-T1.)

---

## §4 — The byte-identical split SEQUENCE

Five extraction steps; **leaf/independent units first, the gate layer isolated last**. After
each step the residual `chordanalyzer.cpp` shrinks; nothing inside it depends on the moved-out
functions' *internals* (consumers reach them through the header), so each step is independently
verifiable. **Acceptance gate per step (all must hold):**

1. Build green (`setup_and_build.bat`).
2. `composing_tests.exe` + `notation_tests.exe` pass.
3. `pipeline_snapshot_tests.exe` 11/11 (no golden refresh — output unchanged).
4. 3-preset corpus regen `.ours.json` **0-diff** (Baroque / Jazz / Default), BIR **57/23/57**
   via `characterise_bir_false.py`.

Mechanics common to every step: create the new `.cpp` (license header + includes per §3),
**cut** the listed bodies/helpers out of `chordanalyzer.cpp` and **paste** them unchanged into
the new TU's anonymous/named scopes, prefix the moved anon-ns helpers (§5), add the file to
[analysis/CMakeLists.txt](src/composing/analysis/CMakeLists.txt). A missing `#include` is a **compile error** (surfaced before any
behavior test), so it cannot silently break byte-identity.

| Step | Moves | New TU | Risk | Why this order |
|---|---|---|---|---|
| **1** | formatter fns + Group A helpers (44–619) + `isValidBassNoteName` + tonicization helpers (3199–3239) + Nashville block (3384–3464) | `chordsymbolformatter.cpp` | Low | Pure leaf — biggest clean lift; helpers used *only* by the formatter; nothing in the file depends on the formatter |
| **2** | `chordTonePitchClasses`, `closePositionVoicing` | `chordvoicing.cpp` | Trivial | Header-only deps, no helpers |
| **3** | `diagnoseChord` | `chorddiagnose.cpp` | Low | Depends only on the public interface + `fn::` public fns |
| **4** | `applyIter8691Pedal` + `isBassChordTone` | `chordpostpasses.cpp` | Low | `isBassChordTone` follows its sole consumer out of the oracle anon ns |
| **5** | `applyPostScoringGates` (+ its margin constants 1723–1725) | `postscoringgates.cpp` | Low | **LAST — isolates the gate layer as the refactor-#2 target;** depends only on `buildChordResult` (header) |

**Residual after Step 5:** `chordanalyzer.cpp` = the vertical oracle (scoring constants +
helpers + `TemplateDef` + `detectExtensions` + `buildChordResult` + `analyzeChord` + factory).

> The instruction's "template/oracle first" is honored by the oracle being the **anchored
> residual**: the template vocabulary + size model never move, so the oracle's identity (and the
> `kTemplateCount` arrays) is stable from step 1 onward; everything else is lifted away from it.

Optional finer step (defer): split `buildChordResult` into its own `chordresult.cpp` — only if a
shared-constants header is introduced first (not byte-identical-free; out of scope for #1).

---

## §5 — Constraint-handling plan

### 5.1 `kTemplateCount` size model — **invariant under this split**
The three compiler-enforced arrays derived from `analysis::kTemplateCount`
([chordanalyzer.h:74](src/composing/analysis/chord/chordanalyzer.h#L74)) are:
- the `templates` `std::array<TemplateDef, kTemplateCount>` + its `static_assert`
  ([chordanalyzer.cpp:2494–2514](src/composing/analysis/chord/chordanalyzer.cpp#L2494)) — **stays in the residual oracle TU**;
- the three `std::array<std::array<double, kTemplateCount>,12>` matrices
  ([2553–2555](src/composing/analysis/chord/chordanalyzer.cpp#L2553)) — **stays in the residual oracle TU**;
- `kMasks` `std::array<uint16_t, analysis::kTemplateCount>` + its `static_assert`
  ([harmonicfunctionlayer.cpp:191–211](src/composing/analysis/function/harmonicfunctionlayer.cpp#L191)) — **untouched** (different module file).

No `kTemplateCount`-derived array moves to a new TU. `kTemplateCount` itself stays in the header.
**No silent stack-buffer regression is possible** — the split touches none of the three arrays.

### 5.2 Unity/jumbo ODR — anon-namespace prefixing (the `jkd*`/`lmd*` precedent)
`composing_analysis` is built `muse_create_module(composing_analysis NO_QT)` — **not** `NO_UNITY`
— so with `MUSE_COMPILE_USE_UNITY` ON it is a unity build
([MuseCreateModule.cmake:111–116](muse/framework/cmake/MuseCreateModule.cmake#L111), batch size 12 via `SetupBuildEnvironment.cmake:26`).
In a unity TU all `mu::composing::analysis::<anonymous>` blocks from co-batched files **merge**;
identically-named anon-ns symbols collide. This is exactly why `jointkeydecision.cpp` uses
`jkdPcMod12`/`jkdCollectionMask`/… and `localmodulationdetector.cpp` uses
`lmdCollectionMask`/`lmdRootIsDiatonic`/… (verified at source).

**Plan — prefix the MOVED anon-ns helpers per-TU (internal-linkage rename ⇒ byte-identical):**
- `chordsymbolformatter.cpp` → **`csf`** prefix: `csfPitchClassName`, `csfPitchClassNameFromTpc`,
  `csfQualitySuffix`, `csfChromaticRoman`, `csfDiatonicRoman`, `csfIsValidBassNoteName`,
  `csfTonicizationScales`, `csfTonicizationParent`, `csfDiatonicDegreeForPc`, `csfIsDegreeMajorThird`
  (+ optionally the `ChordSymbolFormatter::<anon>` Nashville helpers, though that nested anon ns
  has no other contributor and is collision-safe as-is).
- `chordpostpasses.cpp` → **`cpt`** prefix: `cptIsBassChordTone`.
- `chordvoicing.cpp`, `chorddiagnose.cpp`, `postscoringgates.cpp` → **no file-scope anon-ns
  symbols** to prefix (local lambdas only).
- **Residual `chordanalyzer.cpp`:** its helpers do not move, but the file shrinks → unity
  batching may regroup it. The names are specific (`scoreTemplateTones`, `detectExtensions`, …)
  and currently coexist in the batch without collision; keep them, and if the build surfaces a
  redefinition (compile error — never a silent behavior change), prefix reactively (`cso`).
  Proactive prefixing of the residual is optional and equally byte-identical.

### 5.3 `docs/scoring_model.md` sync — reference-only
The split changes **no scoring logic**, so the doc's *content* (template list §2, bonus/gate
descriptions §4/§6, the §9 template-addition checklist) is unchanged and the §2 template count
stays 17. Only **file/location references** update: the post-scoring gates A–L now live in
`postscoringgates.cpp` (not `chordanalyzer.cpp`), the formatter in `chordsymbolformatter.cpp`,
the tail in `chordpostpasses.cpp`. Per the CLAUDE.md sync rule, the split build's final commit
updates those pointers in the same commit. (No template/bonus/gate term is added or modified ⇒
no §2/§4/§6/§8 content edit.)

### 5.4 Byte-identity is the acceptance gate
Pure code movement within one static library preserves runtime output provided (a) no ODR
collision (§5.2), (b) the linker resolves every header-declared symbol (each lands in exactly one
new TU), (c) no order-dependent static init is introduced — none is: the only file-scope statics
are `constexpr`/`static const` (incl. the function-local `templates` array), which carry no
cross-TU init-order dependency. The §4 per-step gate (suites + snapshots + 3-preset 0-diff +
57/23/57) is the proof obligation.

---

## §6 — The post-scoring gate layer, precisely located (for refactor #2)

`applyPostScoringGates` — [chordanalyzer.cpp:1703–2255](src/composing/analysis/chord/chordanalyzer.cpp#L1703) (→ `postscoringgates.cpp` after Step 5).
Header declaration: [chordanalyzer.h:976–980](src/composing/analysis/chord/chordanalyzer.h#L976). Margin constants:
`kGateIMargin=0.45` (1723), `kGateKMargin=0.20` (1724), `kGateLMargin=0.35` (1725).
Sole internal dependency: `buildChordResult` (via the `buildResult` lambda, 1712–1718).
Gate-by-gate anchors within the body:

| Gate | Line | Purpose |
|---|---|---|
| Inversion/bass-root correction block | opens 1727 (comment) / 1736 (`if`); captures `originalWinner*` 1755–1760 | the FM2 fallback + Gates A/E/F run inside this block |
| E | 1884 | first-inversion detection |
| F | 1906 | second-inversion detection |
| G-E | 1975 / 2010 | HalfDim leading-tone key-context gate |
| G-B | 2024 | next-region root matches HalfDim root |
| G-C | 2034 | HalfDim root in 3-region window + stepwise bass |
| G-D | 2047 | ≥2 consecutive stepwise bass moves |
| H / H-B / H-C / H-D | 2063 / 2091 / 2099 / 2107 | Augmented root-symmetry resolution |
| I | 2116 | diatonic first-inversion Major over root-position Minor |
| K | 2151 | first-inversion Augmented over root-position Augmented |
| L | 2187 | same-root Major over root-position Augmented |
| J | 2221 | inverted dom7 over root-position diminished triad |

**Refactor #2 readiness:** after Step 5 the gate layer is a single 553-line TU with exactly one
inbound edge (`buildChordResult`, header) and three callers (`regionanalyzer.cpp` production
sequence, `diagnoseChord`, `inferNextRootPc` in the header) — so each gate's proof-obligation /
dissolution can be staged against `postscoringgates_tests.cpp` in isolation. Refactor #2 does
**not** happen here.

---

## §7 — Tangles / findings (surfaced, not forced)

- **T1 — `buildChordResult` is shared post-scoring infrastructure, not a clean single-layer
  member.** It is the oracle's output-construction stage (uses `detectExtensions` + the scoring
  constants) **and** is called by the gate layer (1712) and the tail (2802) cross-TU. *Resolution:*
  keep it in the oracle TU, reached via the header (already declared). Its quality-normalization
  (Aug-root correction 1589, Sus→Major 1631) is conceptually a post-scoring identity refinement,
  adjacent to the gates — a candidate to consider during refactor #2, **not** moved in #1.

- **T2 — the oracle/competition seam is ALREADY split.** `analyzeChord` builds the vertical-only
  snapshot and delegates ranking/winner-selection to `fn::applyHarmonicFunction`
  (harmonicfunctionlayer.cpp). So #1 does **not** extract a competition layer — it isolates the
  oracle + the still-in-`chordanalyzer.cpp` post-scoring stages. The CMake comment
  ([analysis/CMakeLists.txt:29–34](src/composing/analysis/CMakeLists.txt#L29)) describes a plan to migrate the gates *into*
  `harmonicfunctionlayer`; #1's gate TU (`postscoringgates.cpp`) is reconcilable with that — #1
  **isolates**, #2 **dissolves** (subsumed by the constrained-joint decision).

- **T3 — `isBassChordTone` is mis-grouped** in the oracle anon ns (1463) though its only consumer
  is the tail. Cleanly resolved by moving it with `applyIter8691Pedal` (Step 4).

- **T4 — diatonic-scale tables are triplicated:** `chromaticRoman` SCALES (458–466, formatter),
  `analyzeChord` DIATONIC_PARENT_INDEX (2525–2531, oracle — note `analyzeChord` also uses the
  shared `keyModeScaleIntervals`), and the tonicization tables (3202–3217, formatter). The split
  *separates* these into different TUs (byte-identical) but **perpetuates** the duplication. A
  shared diatonic-scale-table helper is a layer-audit cleanup candidate — **not** a byte-identical
  step, out of scope for #1.

None of T1–T4 blocks the byte-identical split; all are recorded for the layer audit / refactor #2.

---

## §8 — Stop-condition disposition (per the instruction §5)

- No code moved / no file touched in this step — **honored** (read-only; HEAD `5fee657578`).
- A responsibility that can't be assigned to one layer → surfaced as **T1** (`buildChordResult`,
  shared infra, kept with the oracle) and **T2** (competition already external).
- A section that can't be made byte-identical → **none found.** The size model is invariant
  (§5.1); the one real hazard (unity ODR) has a byte-identical fix (§5.2).
- Uncertainty → resolved at source with citations throughout; nothing guessed.

**Hand-off:** this dossier is the spec for the byte-identical split build instruction — the five
steps in §4 with the includes/prefixes in §3/§5 are concrete enough to execute and verify directly.

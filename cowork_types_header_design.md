# Types-only header extraction — design (Phase 5 refactor 2 of 2)

> **Status: BUILT / AS-BUILT (2026-06-26).** Realised as `analysis/types/analysistypes.h` (commit `11f26864f9`): the
> value-type closure lives in the leaf, both header back-edges are killed (`regiontonecollector.h` + `keymodeanalyzer.h`
> include only the leaf), and `PitchContext` is un-nested with the compatibility alias — all D1/D2/leaf-location
> decisions below match the built artifact. (Outstanding follow-up D1: the `analysisutils.h` relocation, tracked in the
> completion ledger A4.) Grounded in `cc_types_header_investigation_report.md` (CC read-only, no source
> touched). The last Phase-5 structural refactor (audit Q2): relocate the cross-layer value types to a **leaf** header so
> the L1.5/L3 headers compile **without** the L4 headers — killing the two type-only header back-edges and making the
> include graph forward-only. **Byte-identical: a pure relocation** (every type keeps its name, namespace, and
> definition; only the *defining file* changes), so sites are untouched via transitive includes + one alias.

## The leaf header
- **New:** `src/composing/analysis/types/analysistypes.h` — a **leaf**: depends on nothing from `chord/` or `key/`
  (STL + engraving *primitives* only). CC verified every member is a dependency-free POD / enum / `inline constexpr`.
- **Holds the closure, EACH IN ITS EXISTING NAMESPACE** (so every qualified name — `analysis::KeySigMode`,
  `function::ScoringPhase`, … — is *unchanged* → zero call-site churn):
  - `namespace mu::composing::analysis`: `ChordQuality`, `ChordAnalysisTone`, `ChordTemporalContext`,
    `ChordAnalyzerPreferences` (+ `kDefaultChordAnalyzerPreferences`), `ParameterBound`, `ParameterBoundsMap`,
    `KeySigMode`, `KeyModeAnalyzerPreferences` (+ `kDefault…`), and **`PitchContext`** (un-nested — see below).
  - `namespace …::function`: `ScoringPhase`, `DecodeQualityLevel` (members of `ChordAnalyzerPreferences`; the leaf spans
    both namespaces — acceptable for a value-types leaf, and required to keep names unchanged).

## D2 (ratify) — `PitchContext` un-nesting = **member alias** (zero-churn)
Move `PitchContext` from `class KeyModeAnalyzer` scope to `namespace analysis` in the leaf; add **`using PitchContext =
analysis::PitchContext;` inside `KeyModeAnalyzer`**. The ~42 `KeyModeAnalyzer::PitchContext` sites then resolve to the
same type — **byte-identical, 1 edit.** (The full rename of all 42 sites to `analysis::PitchContext` is an *optional
later* cosmetic cleanup, not now.) Namespace-qualified, so no clash with the unrelated `muse::mpe::PitchContext`.
**My call: alias.**

## D1 (ratify) — `ParameterBoundsMap` home = **host in the leaf** (minimal); `analysisutils.h` relocation DEFERRED
Move **only** `ParameterBound` / `ParameterBoundsMap` to the leaf (this alone kills header back-edge B). **Leave the rest
of `chord/analysisutils.h`** (the free functions `ionianTonicPcFromFifths`, `normalizePc`, `diatonicMaskFromFifths`,
`isDiatonicStep`) where it is for now. **My call: minimal.**
- **Recorded separate follow-up (NOT this refactor):** those free functions are cross-cutting **pitch/key** utilities
  *mis-located* in `chord/` (e.g. `ionianTonicPcFromFifths` is a key function, not chord-specific). After this refactor
  `keymodeanalyzer.cpp:24` still `#include`s `chord/analysisutils.h` for them — a **.cpp-level** cross-layer include, not
  a header back-edge, so it does not block the forward-only *header* graph. Relocating the whole header out of `chord/`
  (~20 include-path edits) is a distinct cleanup — schedule it on its own (Phase 6 or a standalone step), not folded in.

## Back-edge rewiring
- `chord/chordanalyzer.h` + `key/keymodeanalyzer.h`: **`#include` the leaf** and **remove the relocated definitions**
  (now in the leaf). Their existing includers + the tests get the types **transitively** → unchanged.
- `engravingbridge/regiontonecollector.h`: replace `#include chordanalyzer.h` + `#include keymodeanalyzer.h` with the
  **single leaf include**. → **back-edge A killed.**
- `key/keymodeanalyzer.h`: drop `#include chord/analysisutils.h` (`ParameterBoundsMap` now in the leaf). → **back-edge B
  killed.**
- **Mechanical follow-on (CC-flagged, required):** `engravingbridge/regiontoneprimitives.cpp` calls the analyzer API
  (`ChordAnalyzerFactory`, `analyzeChord`, `applyPostScoringGates`, `applyIter8691Pedal`) + `isDiatonicStep`, which it
  gets **transitively** today via `regiontonecollector.h`'s dropped includes. It must gain a **direct** `#include
  chord/chordanalyzer.h` (and `chord/analysisutils.h` for `isDiatonicStep`). *(A `.cpp` directly including what it
  actually uses is correct hygiene — not a new back-edge.)*

## Byte-identity (the hard gate)
- **Pure relocation:** no type's name, namespace, layout, or definition changes — only which file defines it. All sites
  resolve identically via transitive includes + the one `PitchContext` alias.
- **Gate:** corpus BIR 53/24/53 + `composing_tests` + `notation_tests` + `pipeline_snapshot_tests` **UNCHANGED**; build
  green. Any movement → STOP (a relocation altered something). *(Corpus by-construction acceptable per the Phase-5
  gate while `batch_analyze` is down; the suites + snapshots are the live gate.)*
- **No behaviour, logic, signature, or namespace change.**

## Build outline (the instruction follows on ratification)
Create the leaf; move the closure (definitions only, namespaces preserved); un-nest `PitchContext` + add the member
alias; rewire the 3 headers + the 1 `.cpp` follow-on; prove byte-identical. CC verifies by sha that only those files +
the new leaf changed, with no scoring/signature edits.

## Decisions to ratify
1. **D1 = minimal** (ParameterBound/Map → leaf; `analysisutils.h` relocation deferred as a recorded follow-up).
2. **D2 = member alias** for `PitchContext` (zero-churn; full rename optional-later).
3. **Leaf location/name** = `analysis/types/analysistypes.h`.

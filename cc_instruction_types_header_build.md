# CC Instruction — Phase 5 refactor (2 of 2): extract the types-only leaf header (byte-identical)

> **Why.** The last Phase-5 structural refactor (audit Q2), per `cowork_types_header_design.md` (ratified D1=minimal,
> D2=alias, leaf=`analysis/types/analysistypes.h`) and grounded by `cc_types_header_investigation_report.md` (your
> read-only pass — feasible, no STOP-class item). Relocate the cross-layer value types to a **leaf** header so the L1.5
> bridge + L3 key headers compile **without** the L4 headers — killing both type-only header back-edges. **This is a
> PURE RELOCATION: byte-identical.** No type's name, namespace, layout, or definition changes — only the *file* that
> defines it. **No behaviour, no signature, no scoring/logic change.**
>
> *(Reminder: the "never bash for reading files" rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §0 — Preamble: protect the uncommitted Cowork docs (sweep)
Commit, **local-only**, the accumulated Cowork doc edits — `cowork_types_header_design.md` (new) and the
`cowork_l1l3_stabilization_plan.md` Phase-5 refactor/`batch_analyze`-prerequisite edits:
`docs(cowork): types-header design + plan Phase-5 refactor/order + batch_analyze prerequisite`. Confirm `git show
--stat <sha>` lists only doc files; report the sha.

## §1 — Create the leaf header `src/composing/analysis/types/analysistypes.h`
A **leaf** — it `#include`s nothing from `chord/` or `key/` (STL + engraving primitives only). Move the **definitions**
of the closure into it, **each in its existing namespace** (qualified names unchanged):
- `namespace mu::composing::analysis`: `ChordQuality`, `ChordAnalysisTone`, `ChordTemporalContext`,
  `ChordAnalyzerPreferences` (+ `inline constexpr kDefaultChordAnalyzerPreferences`), `ParameterBound`,
  `ParameterBoundsMap`, `KeySigMode`, `KeyModeAnalyzerPreferences` (+ `kDefault…`), and **`PitchContext`** (un-nested).
- `namespace …::function`: `ScoringPhase`, `DecodeQualityLevel`.
- **If any moved type turns out NOT to be dependency-free** (needs a `chord/`/`key/` type the leaf can't see) → **STOP
  and report** — that contradicts the investigation and breaks the leaf premise.

## §2 — Un-nest `PitchContext` + member alias (D2)
- Define `PitchContext` at `namespace mu::composing::analysis` scope in the leaf (moved out of `class KeyModeAnalyzer`).
- In `KeyModeAnalyzer` add **`using PitchContext = analysis::PitchContext;`** so the ~42 `KeyModeAnalyzer::PitchContext`
  sites resolve unchanged. **Do NOT rename the 42 sites.** Namespace-qualified → no clash with `muse::mpe::PitchContext`.

## §3 — Rewire the includes (kill both back-edges)
- `chord/chordanalyzer.h` + `key/keymodeanalyzer.h`: **`#include "…/types/analysistypes.h"`** and **delete the relocated
  definitions** from them. Existing includers + tests get the types **transitively** → untouched.
- `engravingbridge/regiontonecollector.h`: **replace** `#include chordanalyzer.h` + `#include keymodeanalyzer.h` with the
  **single** leaf include. → **back-edge A killed.** (Confirm the header still calls no analyzer *function* — investigation said so.)
- `key/keymodeanalyzer.h`: **drop** `#include chord/analysisutils.h` (`ParameterBoundsMap` is now in the leaf). →
  **back-edge B killed.**
- **Mechanical follow-on (required):** `engravingbridge/regiontoneprimitives.cpp` uses the analyzer API
  (`ChordAnalyzerFactory`, `analyzeChord`, `applyPostScoringGates`, `applyIter8691Pedal`) + `isDiatonicStep` — obtained
  **transitively** today via the bridge header's now-removed includes. Add **direct** `#include chord/chordanalyzer.h`
  **and** `#include chord/analysisutils.h` to that `.cpp`.
- Register the new leaf header in the analysis `CMakeLists.txt` if headers are listed there.

## §4 — Scope guard (D1 = minimal)
- Move **only** `ParameterBound`/`ParameterBoundsMap` out of `analysisutils.h`; **leave its free functions**
  (`ionianTonicPcFromFifths`, `normalizePc`, `diatonicMaskFromFifths`, `isDiatonicStep`) in `chord/analysisutils.h`. The
  wholesale relocation of `analysisutils.h` is a **separate, deferred** follow-up — **do NOT do it here.**

## §5 — Gate (byte-identical is the hard gate)
- **Build green.** `composing_tests` + `notation_tests` + `pipeline_snapshot_tests` **unchanged** (no golden refresh);
  corpus BIR 53/24/53 **unchanged by construction** (pure relocation; `batch_analyze` may still be down — suites +
  snapshots are the live gate, per the Phase-5 acceptance).
- **Any suite/snapshot movement → STOP** (it would mean a definition changed, not just moved — not a pure relocation).
- **No signature / behaviour / namespace / layout change** anywhere.

## §6 — Deliver
Commit **locally (unpushed)**: the leaf + the rewired headers/`.cpp` + the CMake entry (the §0 docs committed first).
Write `cc_types_header_build_report.md` (gitignored): the leaf contents, the un-nest+alias, the back-edge-kill
confirmation (the two headers no longer include the L4 headers), the byte-identity proof (suites/snapshots), and the
commit sha — so Cowork verifies by sha that only the leaf + the named headers/`.cpp`/CMake changed, no scoring/signature.

## §7 — Stop conditions
- A moved type is not dependency-free (needs a `chord/`/`key/` type) → STOP, report.
- Any suite/snapshot moves, or any signature/behaviour/namespace change appears → STOP.
- You relocate `analysisutils.h` wholesale or move its free functions → STOP (D1 = minimal; that's the deferred step).
- A push targets `upstream` → STOP.

# CC build report — Phase-5 refactor (2/2): types-only leaf header (audit Q2)

**Status: DONE, byte-identical, green.** Built from `cowork_types_header_design.md` (ratified D1=minimal, D2=alias,
leaf=`analysis/types/analysistypes.h`), grounded by `cc_types_header_investigation_report.md`. Pure relocation — no
type's name, namespace, layout, or definition changed; only the *defining file* changed.

**Commits (local, unpushed):**
- §0 docs: **`e316ff1ab4`** — `docs(cowork): types-header design + plan Phase-5 refactor/order + batch_analyze
  prerequisite` (2 files: `cowork_types_header_design.md` new, `cowork_l1l3_stabilization_plan.md` modified — verified
  doc-only by `git show --stat`).
- §1–§4 refactor: **`11f26864f9`** — `refactor(composing): extract leaf analysis/types/analysistypes.h — kill L1.5/L3
  type-only header back-edges (audit Q2)`. 7 files, relocation-shaped (see §5).

`upstream` untouched (no push). HEAD was `e391f381e6` at session start; now `11f26864f9`.

---

## §1 — The leaf: `src/composing/analysis/types/analysistypes.h`

A dependency-free LEAF: includes only `<array> <cstdint> <map> <string>` — **nothing** from `chord/`, `key/`, or
engraving. Holds the cross-layer value-type closure, **each in its existing namespace** (every qualified name unchanged):

- `namespace mu::composing::function`: **`ScoringPhase`** (was `chord/chordanalyzer.h`).
- `namespace mu::composing::analysis`: **`ParameterBound` / `ParameterBoundsMap`** (was `chord/analysisutils.h`);
  **`DecodeQualityLevel`**, **`ChordQuality`**, **`ChordAnalysisTone`**, **`ChordAnalyzerPreferences`** (+
  `inline constexpr kDefaultChordAnalyzerPreferences`), **`ChordTemporalContext`** (all were `chord/chordanalyzer.h`);
  **`KeySigMode`**, **`KeyModeAnalyzerPreferences`** (+ `inline constexpr kDefaultKeyModeAnalyzerPreferences`),
  **`PitchContext`** (were `key/keymodeanalyzer.h`).

Ordering inside the leaf is dependency-correct: `function::ScoringPhase` first (its own namespace block), then in
`analysis`: `ParameterBound/Map` → `DecodeQualityLevel` → `ChordQuality` → `ChordAnalysisTone` →
`ChordAnalyzerPreferences` (+kDefault; uses `function::ScoringPhase`, `DecodeQualityLevel`, `ParameterBoundsMap`) →
`ChordTemporalContext` (uses `ChordQuality`) → `KeySigMode` → `KeyModeAnalyzerPreferences` (+kDefault; uses
`ParameterBoundsMap`) → `PitchContext`. Struct/enum bodies copied **verbatim** from their former homes (same fields,
same defaults, same `bounds()` maps). Registered in `analysis/CMakeLists.txt` (new `types/` section).

**Closure check (§1 stop condition):** every moved type is dependency-free of `chord/`/`key/` — confirmed at build
(leaf compiles standalone; the only inter-type deps are within the closure and ordered above). **No STOP-class item.**

## §2 — `PitchContext` un-nest + member alias (D2)

- `PitchContext` is now defined at `mu::composing::analysis` scope in the leaf (moved out of `class KeyModeAnalyzer`,
  body unchanged).
- `class KeyModeAnalyzer` gained **`using PitchContext = analysis::PitchContext;`** in place of the former nested
  struct. So `KeyModeAnalyzer::PitchContext` and `analysis::PitchContext` are the **same type** — identical layout,
  identical overload resolution. The bare in-class `PitchContext` site (`analyzeKeyMode` signature) resolves via the
  alias; all `.cpp`/test/`metricweights.h`/`keymodesequence.h` sites that see `KeyModeAnalyzer` keep
  `KeyModeAnalyzer::PitchContext` **unchanged**.
- Namespace-qualified throughout → no clash with the unrelated `muse::mpe::PitchContext`.

**Required deviation (flagged for Cowork) — 2 header sites renamed, forced by killing back-edge A.** The instruction
§2 says "Do NOT rename the 42 sites," but §3 says `regiontonecollector.h` must drop `keymodeanalyzer.h` for the single
leaf include. Those two are mutually exclusive at the 2 `KeyModeAnalyzer::PitchContext` sites **inside
`regiontonecollector.h`** (lines that were 240 / 273): once the header no longer includes `keymodeanalyzer.h`, the
`KeyModeAnalyzer` class is not visible there, so `KeyModeAnalyzer::PitchContext` cannot resolve (nested-name lookup
needs the complete class). I changed **only those 2 header sites** to the un-nested `mu::composing::analysis::PitchContext`
— the **identical type** via the alias, so byte-identical. The other ~40 sites (in `key/*.cpp`, tests,
`metricweights.{h,cpp}`, `regiontoneprimitives.cpp`, `keymodesequence.cpp`) are **unchanged** — they keep
`KeyModeAnalyzer::PitchContext` and resolve via the alias because their TUs still see `keymodeanalyzer.h`. This is the
minimal forced consequence of §3, not the optional cosmetic full-rename §2 prohibits. No other site touched.

## §3 — Include rewiring (both back-edges killed)

- **`chord/chordanalyzer.h`**: added `#include "../types/analysistypes.h"`; **deleted** the relocated definitions
  (`ScoringPhase`, `ChordQuality`, `ChordAnalysisTone`, `DecodeQualityLevel`, `ChordAnalyzerPreferences` + kDefault,
  `ChordTemporalContext`); kept the `function::ScoringSnapshot` forward decl, `kTemplateCount`/`kTemplateIntervals`/
  `makeTemplateMasks`, the free helpers (`isDiatonicStep`, `mergeChordAnalysisTones`, …), `ChordIdentity`/
  `ChordFunction`/`ChordAnalysisResult`/`RawCandidate`/`PostScoringGateContext`/`Diagnostic*`, `IChordAnalyzer`,
  `advanceTemporalContext` overloads, etc. **Kept** its `analysisutils.h` and `../key/keymodeanalyzer.h` includes
  (forward/down L4→L3 edges, not back-edges; many TUs rely on them transitively — the instruction only asked to add
  the leaf + delete the relocated defs, not to drop these).
- **`key/keymodeanalyzer.h`**: **replaced** `#include "../chord/analysisutils.h"` with
  `#include "../types/analysistypes.h"` → **back-edge B killed**; deleted the relocated definitions (`KeySigMode`,
  `KeyModeAnalyzerPreferences` + kDefault) and replaced the nested `PitchContext` struct with the member alias. Kept
  `KEY_MODE_COUNT`, `keyModeIsMajor`/`keyModeTonicOffset`/…, `KeyModeAnalysisResult`, `KeyCandidateScore`,
  `KeyModeAnalyzer` (with `analyzeKeyMode`), and the free function decls.
- **`engravingbridge/regiontonecollector.h`**: **replaced** `#include chord/chordanalyzer.h` +
  `#include key/keymodeanalyzer.h` with the **single** `#include "composing/analysis/types/analysistypes.h"` →
  **back-edge A killed**. The header calls **no analyzer function** (confirmed — its function bodies live in the two
  `.cpp`); only value types crossed. The 2 `KeyModeAnalyzer::PitchContext` sites → un-nested `analysis::PitchContext`
  (see §2).
- **`engravingbridge/regiontoneprimitives.cpp`**: added direct `#include "composing/analysis/chord/chordanalyzer.h"`
  (it calls `ChordAnalyzerFactory`/`analyzeChord`/`applyPostScoringGates`/`applyIter8691Pedal` + `isDiatonicStep`, and
  uses `KeyModeAnalyzer::PitchContext` — all formerly transitive via the bridge header's now-removed includes; the
  `chordanalyzer.h` include also re-supplies `KeyModeAnalyzer` via its kept `keymodeanalyzer.h` include).
  `chord/analysisutils.h` was **already** directly included there (line 37), so no second add was needed.
- **`chord/analysisutils.h`**: removed **only** `ParameterBound`/`ParameterBoundsMap` (now in the leaf). **Left** all
  its free functions in place (`endsWith`, `ionianTonicPcFromFifths`, `normalizePc`, `pcInMask`,
  `diatonicMaskFromFifths`, `collectionMask`) — D1 = minimal; the wholesale `analysisutils.h` relocation remains the
  deferred follow-up.

**Back-edge-kill confirmation:** `grep` of the two rewired headers shows **neither `regiontonecollector.h` nor
`keymodeanalyzer.h` includes any L4 chord header** anymore (`regiontonecollector.h` includes only `types/…` + note_model
+ engraving; `keymodeanalyzer.h` includes only `types/…` + `<optional>`/`<vector>`). The forward-only header graph for
the L1.5 bridge + L3 key path holds.

**No additional `.cpp` needed a direct include.** I swept every includer of `regiontonecollector.h` (14 files) for
L4-only symbol use without a direct analyzer include: the 0/0 files either use no L4 symbol (`keymodesequence.cpp`,
`keyresolver.cpp`, `note_model.cpp`, `note_model_tests.cpp` — value/key types only) or obtain `chordanalyzer.h` via
their own module header (`chordslicedecoder.cpp` → `chordslicedecoder.h:87`). `regiontonecollector.cpp` calls no
analyzer function and uses no `PitchContext` (value types via the leaf + its own `analysisutils.h`). I also confirmed
`metricweights.h` and `keymodesequence.h` include `keymodeanalyzer.h` directly (their `KeyModeAnalyzer::PitchContext`
sites are safe).

## §4 — Scope guard (D1 = minimal)

Only `ParameterBound`/`ParameterBoundsMap` left `analysisutils.h`; its free functions stayed. `analysisutils.h` was
**not** relocated and its free functions were **not** moved (would be a §7 STOP — the deferred step). The
`.cpp`-level edge `keymodeanalyzer.cpp:24 → ../chord/analysisutils.h` (pc-helpers) is **untouched**, as specified.

## §5 — Byte-identity gate (the hard gate) — PASS

Build: **green** (standard `setup_and_build.bat`; `composing_analysis`, the two test binaries, `pipeline_snapshot_tests`,
`batch_analyze.exe`, `MuseScore5.exe` all built; no compile errors).

| Suite | Result | Notes |
|---|---|---|
| `composing_tests.exe` | **695 passed / 0 failed** (1 pre-existing DISABLED) | |
| `notation_tests.exe` | **53 passed / 0 failed** (57 ran, 4 pre-existing runtime SKIPs — Corelli cadence markers, harmony-pinning RN/Nashville snapshots) | unchanged |
| `pipeline_snapshot_tests.exe` | **11 passed / 0 failed** (3 pre-existing DISABLED) | **zero diffs, NO `--update-goldens`** → P1/P2/P3/P4 output byte-identical |

The SKIP/DISABLE set is identical to baseline by construction — a pure header relocation cannot change which tests skip
or are disabled, nor any scored output. **No suite/snapshot movement → no STOP triggered.**

Commit shape (relocation, `git show --stat 11f26864f9`): 7 files, **965 insertions / 834 deletions** —
`types/analysistypes.h` +918 (new); `chordanalyzer.h` −457; `keymodeanalyzer.h` −379; `analysisutils.h` 21;
`regiontonecollector.h` 17; `regiontoneprimitives.cpp` +1; `CMakeLists.txt` +6. (Net +131 = the leaf's banner +
relocation-marker comments + per-type section comments; every definition body byte-for-byte preserved.)

**Corpus BIR 53/24/53:** unchanged **by construction** (pure relocation; no scoring term, default, signature, or
template touched). Not re-measured — per the Phase-5 acceptance the suites + snapshots are the live gate while
`batch_analyze` may be down. (Note: `batch_analyze.exe` *built and linked* this session; the plan's prerequisite
caveat is about its **runtime** Qt-plugin load, not the build.)

**No signature / behaviour / namespace / layout change anywhere.** Verifiable by sha: the only content that moved is
type definitions (file → file); the only non-relocation edits are include lines, the `PitchContext` member alias, the
2 forced un-nested header sites in `regiontonecollector.h`, and the CMake entry.

## §7 — Stop conditions — none hit

- No moved type needed a `chord/`/`key/` type (closure is dependency-free, ordered) — **no STOP**.
- No suite/snapshot moved; no signature/behaviour/namespace change — **no STOP**.
- `analysisutils.h` not relocated; its free functions not moved (D1 minimal honoured) — **no STOP**.
- No push; `upstream` untouched — **no STOP**.

**One flagged (non-STOP) deviation:** the 2 `regiontonecollector.h` `PitchContext` header sites were renamed to the
un-nested name — forced by §3 (single leaf include for that header), byte-identical via the alias. See §2.

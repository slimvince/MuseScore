# CC investigation — Phase-5 refactor (2/2): types-only leaf header (audit Q2)

**Scope:** READ-ONLY investigation. No source was edited. This grounds Cowork's design of the
`analysis/types/` leaf-header extraction; CC builds it afterward from Cowork's spec.

**Method:** read the four headers in full (`chord/chordanalyzer.h`, `chord/analysisutils.h`,
`key/keymodeanalyzer.h`, `engravingbridge/regiontonecollector.h`), swept every `#include` of the
chord/key headers tree-wide, and counted/located every reference site for each crossing type. Counts
below are from `Grep --count`; I separate **real source** (`src/`, `tools/`) from documentation noise
(`docs/`, `*.md`, `STATUS.md`, `ARCHITECTURE.md`) and from `scratch_artifacts/` coverage HTML (ignored).

---

## §0 — Verdict up front (feasibility)

**Feasible, pure relocation, byte-identical — but the closure is larger than the four audit-named types.**

- A leaf `analysis/types/` header depending on **nothing** from `chord/`/`key/` **can** carry the
  crossing types, with `chordanalyzer.h` / `keymodeanalyzer.h` then `#include`-ing it. Both named
  back-edges are then removable. Every type move is a **pure relocation** (no behaviour touch) → corpus
  byte-identical, both suites + snapshots unaffected.
- **None of the moves is STOP-class.** No type's extraction requires a behaviour change.
- **The closure is bigger than the audit's 4 names.** To make `ChordAnalysisTone`,
  `ChordTemporalContext`, `ChordAnalyzerPreferences`, `PitchContext` self-contained in a dependency-free
  leaf — AND to let `regiontonecollector.h` include *only* the leaf — the header must **also** carry the
  transitive members `ChordQuality`, `function::ScoringPhase`, `DecodeQualityLevel`, `ParameterBound` /
  `ParameterBoundsMap`, and the two types `regiontonecollector.h` uses directly beyond the named four:
  `KeySigMode` and `KeyModeAnalyzerPreferences` (+ both `kDefault…` objects). All are dependency-free or
  reduce to the same leaf — see §4.
- **`PitchContext` un-nest is byte-identical** via a member-type alias (`using PitchContext =
  types::PitchContext;` inside `KeyModeAnalyzer`); it depends on **no** `KeyModeAnalyzer` internals.
- **Two flags for the design (neither a STOP):**
  1. **Name collision (benign):** an unrelated `muse::mpe::PitchContext` exists
     (`muse/framework/mpe/events.h`) used by the audio/playback layer. It is in a **different
     namespace**, so the un-nested `mu::composing::analysis::…::PitchContext` does not clash — *provided*
     the extraction keeps it namespace-qualified (do **not** introduce an unqualified `using` that could
     surface it ADL-adjacent to mpe code). Today the `KeyModeAnalyzer::` nesting disambiguates; the
     `types::`/member-alias form keeps it disambiguated.
  2. **Required follow-on include (mechanical):** `regiontonecollector.h` is included by
     `regiontoneprimitives.cpp`, which actually **calls the analyzer API** (`ChordAnalyzerFactory::create`,
     `analyzeChord`, `applyIter8691Pedal`, `applyPostScoringGates`) and uses the free function
     `isDiatonicStep` — all from `chordanalyzer.h`, obtained **only transitively** today. When the header
     drops its `chordanalyzer.h`/`keymodeanalyzer.h` includes, that TU must gain a **direct**
     `#include "composing/analysis/chord/chordanalyzer.h"`. This is the "header used only for value types,
     .cpp uses the real API" split — exactly the audit's premise — and is byte-identical.

---

## §1 — Cross-layer value-type inventory

### Layer orientation (for "back-edge" sense)
Per the audit / `cowork_l1l3_stabilization_plan.md`: engravingbridge = **L1.5**, key = **L3**, chord =
**Architectural Layer 4**. So:
- chord (L4) `#include`-ing key (L3) — `chordanalyzer.h:35 → ../key/keymodeanalyzer.h` — is a **forward/down**
  edge (allowed; that's how `chordanalyzer.h` gets `KeySigMode`).
- L1.5 or L3 `#include`-ing chord (L4) is a **back-edge** (the thing to kill).
- `analysisutils.h` sits physically under `chord/` but is a pure leaf (only `<cstdint>/<map>/<string>`); the
  key layer reaching into `chord/` for it is a **directory-level back-edge**.

### The four audit-named types

| Type | Defined | Nested? | Own dependencies | Real-source ref sites |
|---|---|---|---|---|
| `ChordAnalysisTone` | `chord/chordanalyzer.h:148–177` | No (namespace `mu::composing::analysis`) | **Primitives/STL only** (`int`,`double`,`bool`; used in `std::vector`). The free helpers `normalizeMergedBassTone`/`mergeChordAnalysisTones`/`bassToneFromTones` sit beside it but are not members. | **156 total / 44 files**; real source ≈ **125 / 29 files** (rest are docs). Heaviest: `chordanalyzer.h` (14, incl. def), `chordanalyzer_tests.cpp` (17), `chordanalyzer.cpp` (7), `sectionanalyzer.cpp` (6), `postscoringgates_tests.cpp` (6), `regiontone{collector.h,collector.cpp,primitives.cpp}` (4 each), `notationcomposingbridgehelpers.{h,cpp}`, `tools/batch_analyze.cpp` (5). |
| `ChordTemporalContext` | `chord/chordanalyzer.h:699–766` | No | **`ChordQuality`** (member `previousQuality`, line 704) + `std::array`/primitives. → carrying it requires carrying `ChordQuality`. | **248 total / 57 files**; real source ≈ **90 / ~20 files**. Heaviest: `chordanalyzer.h` (10, incl. def), `postscoringgates_tests.cpp` (16), `decode_tests.cpp` (11), `chordanalyzer_tests.cpp` (11), `chordpathdecoder.h` (6), `regionanalyzer.cpp` (6), `harmonicrhythm.h` (3), `regiontone{primitives.cpp,collector.h}` (2 each). |
| `ChordAnalyzerPreferences` (+ `kDefaultChordAnalyzerPreferences`, `chordanalyzer.h:684`) | `chord/chordanalyzer.h:403–680` (object 684) | No | **`function::ScoringPhase`** (member `scoringPhase`, line 598, default-init `= ScoringPhase::Final`), **`DecodeQualityLevel`** (member `decodeQualityLevel`, line 606, default-init), **`ParameterBoundsMap`** (return of `bounds()`, line 656 — from `analysisutils.h`). | **241 total / 66 files**; real source ≈ **170 / ~35 files**. Heaviest: `chordanalyzer.h` (13, incl. def+object), `postscoringgates_tests.cpp` (22), `chordanalyzer_tests.cpp` (20), `chordanalyzer.cpp` (6), `chordslicedecoder.cpp` (6), `regiontoneprimitives.cpp` (6), `regionanalyzer.cpp` (5), `notationcomposingbridge.cpp` (3), `tools/batch_analyze.cpp` (6). |
| `PitchContext` | `key/keymodeanalyzer.h:498–503` | **YES — nested in `class KeyModeAnalyzer`** | **Primitives only** (`int pitch`, `double durationWeight`, `double beatWeight`, `bool isBass`). **No** `KeyModeAnalyzer` internals (no nested enum/const/typedef). | See §3 — **~42 real reference sites** across 10 files (all as `KeyModeAnalyzer::PitchContext`, plus 2 in-class bare `PitchContext`). |

### Other types that cross the boundary (audit did NOT name — found by sweeping the includes)

These are pulled across the **same** two back-edges (or are transitive members of the named four), so the
leaf header must carry them too for the back-edges to actually disappear:

| Type | Defined | Why it crosses | Dependencies | Ref-site scale |
|---|---|---|---|---|
| `KeySigMode` (enum, 21 modes) | `key/keymodeanalyzer.h:36–63` | Used **by value** in `regiontonecollector.h:220` (`findTemporalContext(... KeySigMode keyMode ...)`); also a member of `ChordFunction`. By-value enum ⇒ needs the complete definition at the leaf. | **None** (plain `enum class`). | **1721 total / 171 files** (foundational). Real source vast: `keymodeanalyzer_tests.cpp` (49), `chordanalyzer_tests.cpp` (110), `keymodeanalyzer.{h,cpp}`, `keymodeformatting.cpp` (44), `batch_analyze.cpp` (11), notation bridges. **Only the *definition* relocates; reference sites are untouched (transitive include).** |
| `KeyModeAnalyzerPreferences` (+ `kDefaultKeyModeAnalyzerPreferences`, `keymodeanalyzer.h:491`) | `key/keymodeanalyzer.h:172–488` | Used by **const-ref** in `regiontonecollector.h:239,271`. (By-ref ⇒ could *technically* be forward-declared, but it is itself in the key layer, so cleanest to host in the leaf.) | **`ParameterBoundsMap`** only (return of `bounds()`, line 406). | **84 total / 29 files**; real source ≈ **70 / ~22 files**: `keyresolver.{h,cpp}`, `keymodesequence.{h,cpp}`, `keymodeanalyzer.{h,cpp}`, `regionanalyzer.{h,cpp}`, `sparsechordrefinement.h`, `metricweights.{h,cpp}`, `batch_analyze.cpp` (8), notation bridges. |
| `ChordQuality` (enum) | `chord/chordanalyzer.h:136–146` | **Member of `ChordTemporalContext`** (must travel with it). Also independently pulled "for ChordQuality" by several *later-layer* headers (`section/jointkeydecision.h`, `section/cadencekeyanchor.h`, `function/tonicizationlabeler.h`, `intonation/tuning_system.h`) — those are **forward/down** edges (allowed), not the targeted back-edge. | **None** (plain `enum class`). | **3485 total / 200 files** (foundational); definition relocation only — reference sites untouched. |
| `function::ScoringPhase` (enum) | `chord/chordanalyzer.h:51–55` (namespace `mu::composing::function`) | **Member of `ChordAnalyzerPreferences`** (default-initialized). | **None**. Note it is defined *inside `chordanalyzer.h`* specifically because the include direction is `harmonicfunctionlayer.h → chordanalyzer.h`, and a forward-declared enum can't satisfy the `= ScoringPhase::Final` default-init (header comment, lines 43–55). | Many, mostly chord/function/region; relocation only. |
| `DecodeQualityLevel` (enum) | `chord/chordanalyzer.h:392–396` | **Member of `ChordAnalyzerPreferences`** (default-initialized). Defined in `chordanalyzer.h` for the same include-direction reason (`chordpathdecoder.h → chordanalyzer.h`). | **None**. | Few; relocation only. |
| `ParameterBound` / `ParameterBoundsMap` | `chord/analysisutils.h:41–48` | Return type of **both** `ChordAnalyzerPreferences::bounds()` and `KeyModeAnalyzerPreferences::bounds()`. The reason `keymodeanalyzer.h` back-edges into `chord/analysisutils.h` (see §2). | `<map>`, `<string>` (STL only). | Used by the two `bounds()` definitions + optimizer tooling. |

**Not in scope** (cross only on forward/down edges or via other headers, not the two named back-edges):
`ChordIdentity`/`ChordFunction`/`ChordAnalysisResult`/`RawCandidate`/the `Diagnostic*` structs (chord
result types), `KeyModeAnalysisResult`/`KeyCandidateScore` (key result types, e.g. `tuning_system.h`
pulls `KeyModeAnalysisResult`). These are consumed by **later** layers including the chord/key headers
forward — they don't create the L1.5/L3 back-edges and need not move. (Flagging them only so the design
knows the leaf does **not** need to swallow the whole header.)

---

## §2 — The exact header back-edges to kill (confirmed at source)

### Back-edge A — `engravingbridge/regiontonecollector.h` (L1.5) → chord (L4) + key (L3)
Two includes, both present **only for value types** (the header references no analyzer *function* — those
calls live in `regiontoneprimitives.cpp`):

- `regiontonecollector.h:48 #include "composing/analysis/chord/chordanalyzer.h"`
- `regiontonecollector.h:49 #include "composing/analysis/key/keymodeanalyzer.h"`

**Exact type set the header needs** (with the use-site that forces a *complete* type):

| Type | Use in `regiontonecollector.h` | Needs complete type? |
|---|---|---|
| `ChordAnalysisTone` | return `std::vector<…>` (lines 129,159,171) | Yes (vector element) |
| `ChordAnalyzerPreferences` + `kDefaultChordAnalyzerPreferences` | `weightedPcView(... const ChordAnalyzerPreferences& prefs = kDefault…)` (166–167) | Yes (default-arg object) |
| `ChordTemporalContext` | return by value (215) | Yes |
| `KeySigMode` | `findTemporalContext(... KeySigMode keyMode ...)` by value (220) | Yes (by-value enum) |
| `PitchContext` | `std::vector<…KeyModeAnalyzer::PitchContext>&` (240,273) | Yes (vector element) |
| `KeyModeAnalyzerPreferences` | `const …& prefs` (239,271) | by-const-ref (forward-declarable, but host in leaf) |

⇒ The leaf must carry **{ChordAnalysisTone, ChordTemporalContext(+ChordQuality), ChordAnalyzerPreferences
(+kDefault,+ScoringPhase,+DecodeQualityLevel,+ParameterBoundsMap), KeySigMode, PitchContext,
KeyModeAnalyzerPreferences(+kDefault,+ParameterBoundsMap)}** for `regiontonecollector.h` to include the
leaf **only**.

**Consequence (mechanical, byte-identical):** `regiontoneprimitives.cpp` (defines the analyzer-calling
helpers — `findTemporalContext` cold-analyzes neighbours at lines 464–573; also uses `isDiatonicStep` at
line 44) currently gets `chordanalyzer.h` **transitively** through this header. It must gain a **direct**
`#include "composing/analysis/chord/chordanalyzer.h"`. (`regiontonecollector.cpp` appears to use only the
value types + `analysisutils.h` helpers it already includes directly — to be confirmed at build, but it
calls no analyzer function per the sweep.)

### Back-edge B — `key/keymodeanalyzer.h` (L3) → `chord/analysisutils.h` (chord dir)
- `keymodeanalyzer.h:27 #include "../chord/analysisutils.h"`

**Exact type set the header needs:** **`ParameterBoundsMap`** only (used by
`KeyModeAnalyzerPreferences::bounds()`'s return type, line 406). Nothing else from `analysisutils.h` is
referenced *in the header* (the pc-helpers `normalizePc`/`diatonicMaskFromFifths`/`collectionMask`/… are
used in `keymodeanalyzer.cpp`, line 24 — a separate **.cpp-level** back-edge).

⇒ Killing back-edge B needs `ParameterBound`/`ParameterBoundsMap` reachable from a **layer-neutral** spot.
Two clean shapes for the design (Cowork's call):
- host `ParameterBound`/`ParameterBoundsMap` **in the new leaf** `types/` header (the `bounds()` returns
  it; the leaf depends only on `<map>/<string>`), **or**
- **relocate `analysisutils.h` itself** out of `chord/` to a neutral `analysis/util/` (it is already a
  pure leaf with zero layer deps). This also resolves the `keymodeanalyzer.cpp` line-24 .cpp back-edge in
  one move, but touches ~20 includer paths (mechanical).

### Other includers (not the two named back-edges — context only)
Headers that include **both** chord+key headers but live in region/section/top-level (not the audited
L1.5/L3 back-edge): `analyzed_section.h`, `region/harmonicrhythm.h`, `region/regionanalyzer.h`,
`region/sparsechordrefinement.h`, `harmony/harmonicsegmenter.h`, `section/sectionanalyzer.h`,
`intonation/tuning_system.h`/`tuning_utils.h`, `decode/chordpathdecoder.h`,
`function/harmonicfunctionlayer.h`. They would **also** transitively benefit from a leaf types header
(value types without the full analyzer API), but they are out of this step's named scope; noted so the
design can decide whether to point them at the leaf in the same pass or leave them.

---

## §3 — `PitchContext` un-nesting (the crux)

**Definition (`key/keymodeanalyzer.h:498–503`):**
```cpp
class KeyModeAnalyzer {
public:
    struct PitchContext {
        int pitch = 0;
        double durationWeight = 1.0;
        double beatWeight = 1.0;
        bool isBass = false;
    };
    ...
};
```

**(a) Depends on `KeyModeAnalyzer` internals?** **No.** Four primitive members, default-initialized; it
references no nested enum, constant, or typedef of `KeyModeAnalyzer`. It is a pure POD and can stand alone
in a `types` namespace unchanged.

**(b) Reference-site count & locations** — every site is `KeyModeAnalyzer::PitchContext` *except* two
in-class bare `PitchContext` (which resolve via class scope):

| File | Sites | Form |
|---|---|---|
| `key/keymodeanalyzer.h` | 1 def (498) + 1 bare in `analyzeKeyMode` sig (519) | def + in-class bare |
| `key/keymodeanalyzer.cpp` | 228,240,249,266,281,322,332,364,369 (qualified) + 543 (bare, in member def) | 9 qualified + 1 bare |
| `key/keymodesequence.cpp` | 78, 88, 143 | qualified |
| `key/keyresolver.cpp` | 304 | qualified |
| `scoreharvest/metricweights.h` | 107 | qualified (declaration) |
| `scoreharvest/metricweights.cpp` | 115 | qualified (definition) |
| `engravingbridge/regiontoneprimitives.cpp` | 129, 192, 223, 269 | qualified |
| `engravingbridge/regiontonecollector.h` | 240, 273 (+ comment at 41) | qualified |
| `tests/test_helpers.h` | 59, 62, 70, 72 | qualified |
| `tests/synthetic_tests.cpp` | 359, 362 | qualified |
| `tests/keymodeanalyzer_tests.cpp` | 308,336,343,441,464,539,570,609,627,645,663,681,699,719,742 (×15) | qualified |

**≈ 42 real reference sites across 10 files** (plus the def). **Zero** sites in `tools/batch_analyze.cpp`
or the notation layer (the bridge funnels through `regiontone…`). The unrelated `muse::mpe::PitchContext`
hits in the sweep are a **different type in a different namespace** (audio layer) — not reference sites.

**(c) Can the un-nest be byte-identical?** **Yes — pure relocation + member alias.**
- Move the struct to the leaf as `mu::composing::analysis::types::PitchContext` (identical body).
- Inside `class KeyModeAnalyzer`, add `using PitchContext = types::PitchContext;` (member type alias).
  Then **every existing site keeps compiling unchanged**: qualified `KeyModeAnalyzer::PitchContext` still
  names it, and the two in-class bare `PitchContext` still resolve through the alias.
- `KeyModeAnalyzer::PitchContext` and `types::PitchContext` become the **same type** — identical layout,
  identical overload resolution, identical analyzer behaviour. The corpus is byte-identical. (Mangled
  names of functions taking the type change from the nested to the `types::` spelling, but all TUs
  recompile together — a link-consistency non-issue, not a behaviour change.)
- **Nothing here is not-a-pure-relocation.** No `KeyModeAnalyzer` static/const is dragged along; the
  alias keeps the ~42 sites zero-churn. (If the design instead prefers to *rename* all 42 sites to
  `types::PitchContext` and drop the alias, that is also byte-identical but is 42 edits vs. 1 alias.)

---

## §4 — Feasibility verdict + proposed leaf-header shape

**Verdict: feasible, byte-identical, no STOP-class item.** A dependency-free leaf header can carry the
crossing types; `chordanalyzer.h`/`keymodeanalyzer.h` then `#include` it (so all existing includers + the
gtest suites keep compiling transitively, with the member alias for `PitchContext`); and the two named
back-edges (`regiontonecollector.h`'s two includes; `keymodeanalyzer.h → analysisutils.h`) collapse to a
single leaf include each.

### Proposed leaf contents (the transitive closure — for Cowork to ratify/trim)
A leaf `analysis/types/…h` (depending on **only** `<array>`,`<cstdint>`,`<map>`,`<string>`,`<vector>`):

1. **`ParameterBound` / `ParameterBoundsMap`** — *or* keep these in `analysisutils.h` and relocate that
   file to a neutral dir (decision point, see §2-B). Needed first (both `bounds()` return it).
2. **`KeySigMode`** (enum) — dependency-free; needed by `ChordFunction`, `findTemporalContext`, everything.
3. **`ChordQuality`** (enum) — dependency-free; member of `ChordTemporalContext`.
4. **`function::ScoringPhase`** (enum, in `mu::composing::function`) — member of `ChordAnalyzerPreferences`.
5. **`DecodeQualityLevel`** (enum) — member of `ChordAnalyzerPreferences`.
6. **`ChordAnalysisTone`** (struct) — primitives only.
7. **`ChordTemporalContext`** (struct) — uses `ChordQuality`.
8. **`ChordAnalyzerPreferences`** + `inline constexpr kDefaultChordAnalyzerPreferences` — uses
   `ScoringPhase`, `DecodeQualityLevel`, `ParameterBoundsMap`.
9. **`PitchContext`** (un-nested, in a `types` namespace) — primitives only.
10. **`KeyModeAnalyzerPreferences`** + `inline constexpr kDefaultKeyModeAnalyzerPreferences` — uses
    `ParameterBoundsMap`.

### Headers that change their includes
- `chord/chordanalyzer.h` — moves items 3–8 out; `#include`s the leaf (keeps its `../key/keymodeanalyzer.h`
  for `KeySigMode` *or* gets it from the leaf too — design choice). Keeps the analyzer interface, the free
  helpers (`isDiatonicStep`, `mergeChordAnalysisTones`, …), template tables, result/diagnostic structs.
- `key/keymodeanalyzer.h` — moves items 2, 9, 10 out; `#include`s the leaf; **drops** `../chord/analysisutils.h`
  (back-edge B gone) since its only header-level need (`ParameterBoundsMap`) now comes from the leaf; adds
  `using PitchContext = types::PitchContext;` inside `KeyModeAnalyzer`.
- `engravingbridge/regiontonecollector.h` — **drops** both `chordanalyzer.h` and `keymodeanalyzer.h`;
  `#include`s the leaf **only** (back-edge A gone).
- `engravingbridge/regiontoneprimitives.cpp` — **adds** a direct `#include
  "composing/analysis/chord/chordanalyzer.h"` (it uses the analyzer API + `isDiatonicStep` transitively
  today). Possibly `keymodeanalyzer.h` too if it touches anything beyond the leaf there (it does not call
  `analyzeKeyMode` per the sweep).
- (If `analysisutils.h` is relocated rather than copying `ParameterBoundsMap`: ~20 includer paths update —
  mechanical; enumerated on request.)

### Types whose extraction is NOT byte-identical / needs a behaviour touch
**None.** Every listed move is a pure type relocation (enums and PODs), an `inline constexpr` object
relocation (ODR-safe), or a member-alias addition. No scoring term, default value, or signature semantics
changes. The only **non-type** consequences are include-line edits (the `regiontoneprimitives.cpp` direct
include; optional `analysisutils.h` path churn) — also byte-identical.

**Two design decision points to settle before building (not blockers):**
- **D1 — `ParameterBoundsMap` home:** copy into the leaf, or relocate `analysisutils.h` to a neutral dir
  (the latter also fixes the `.cpp`-level back-edge `keymodeanalyzer.cpp:24`).
- **D2 — `PitchContext` sites:** keep the member alias (1 edit, zero site churn) vs. rename all ~42 sites
  to `types::PitchContext` (explicit, no alias). Both byte-identical.

---

## §5 — Stops check
- No source was edited (read-only honoured).
- No push performed; `upstream` untouched.
- No STOP-class extraction found; both decision points (D1/D2) are scoping choices, not stops.

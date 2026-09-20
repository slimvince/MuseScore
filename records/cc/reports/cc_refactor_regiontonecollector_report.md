# Refactor #2-candidate — `regiontonecollector.cpp` split: BUILD REPORT (HELD)

> **Status: HELD — local, UNCOMMITTED, UNPUSHED.** Awaiting Cowork verification that the
> diff is move-only (committed-object path) before the single commit. Executes
> `cc_instruction_refactor_regiontonecollector_split.md` (the top pure-split candidate,
> `cc_module_layering_assessment_dossier.md` §5 #1). Baseline / HEAD: `41f7c65f63`
> (Refactor #1). Gitignored (`cc_*.md`).

---

## §0 — Result

The split completed **strictly byte-identical** (pure code movement; NO logic / scoring /
inference / constant / behavior change). Every acceptance-gate item passed:

| Gate | Requirement | Result |
|---|---|---|
| Build | green (`setup_and_build.bat`) | ✅ exit 0 (composing_analysis unity lib linked clean) |
| `composing_tests` | pass | ✅ 545/545 |
| `notation_tests` | pass | ✅ 57/57 |
| `pipeline_snapshot_tests` | 11/11, **no `--update-goldens`** | ✅ 11/11 (golden tree git-clean) |
| 3-preset `.ours.json` 0-diff | Baroque / Jazz / Default | ✅ **TOTAL_DIFF=0** (SHA-256, 353×3) |
| BIR=false | 57 / 23 / 57 | ✅ 57 / 23 / 57 |

`regiontonecollector.h` is **unchanged** (the stable integration boundary). The single
dropped line beyond the 6 moved functions is one redundant separator blank (orig L576).

The `.ours.json` 0-diff is **SHA-256 bit-identity** of all 353×3 analysis outputs vs the
HEAD-`41f7c65f63`-equivalent baseline — this subsumes the BIR **case-identity** gate
(identical `.ours.json` ⟹ identical BIR `stem@tick` sets, not merely the integer 57/23/57).

---

## §1 — What moved (final TU map)

`regiontonecollector.cpp` (891 lines) conflated the tone/context **primitives** with the
`collectRegionTones` accumulator. The 6 independent free functions named by the assessment
(§5 #1) lifted into a new sibling TU; `collectRegionTones` is the lone residual.

| File | Lines | Holds |
|---|---|---|
| **`engravingbridge/regiontoneprimitives.cpp`** (NEW) | 514 | `collectSoundingAt`, `buildTones`, `collectPitchContext`, `detectOnsetSubBoundaries`, `detectBassMovementSubBoundaries`, `findTemporalContext` |
| `engravingbridge/regiontonecollector.cpp` (residual) | 891 → **421** | `collectRegionTones` (the 376-line region-tone accumulator) alone |
| `engravingbridge/regiontonecollector.h` | unchanged | declares all 7 functions (the stable boundary) |

All 6 moved functions are **external-linkage API** declared in the unchanged header, so the
40+ external call sites (notation bridge, `tools/batch_analyze`, the test suites) are
unaffected — the linker resolves the moved definitions from the new TU in the same
`composing_analysis` lib.

---

## §2 — Move list + call-site re-confirmation (per instruction §2)

| Moved fn | orig lines | callers (source-verified) |
|---|---|---|
| `collectSoundingAt` | 46–96 | external + `findTemporalContext` (moved with it) |
| `buildTones` | 98–119 | external + `findTemporalContext` (moved with it) |
| `collectPitchContext` | 121–198 | external (key/mode resolution) |
| `detectOnsetSubBoundaries` | 577–666 | external (Pass-2 segmentation) |
| `detectBassMovementSubBoundaries` | 668–747 | external (Pass-2b segmentation) |
| `findTemporalContext` | 749–889 | external (bridge temporal context) |

**Residual independence confirmed at source (the call-site check the instruction mandates):**
`collectRegionTones` (orig 200–575) calls **none** of the 6 moved functions — `grep` over the
residual for all six names returns 0 hits. The only intra-file calls were
`findTemporalContext` → `collectSoundingAt`/`buildTones` (orig L799/801/857/859); all three
move together, so those calls stay intra-TU. Mutual independence ⟹ clean seam, no residual
dependency dragged out.

**`using mu::composing::analysis::isDiatonicStep;` (orig L44)** is consumed **only** by
`findTemporalContext` (the unqualified `isDiatonicStep(...)` at orig L828/885); it moved to
the new TU with its sole consumer (the refactor-#1 `coreIntervals`/`romanWithInversion`
precedent — a helper travels with the function that needs it). `collectRegionTones` does not
use it (it has its own function-local `using namespace mu::composing::analysis;`), so the
residual compiles without it.

---

## §3 — No deviation, no caveat

The assessment flagged this candidate as **"highest yield, no caveat"** and that held:

- **No anonymous-namespace / `static` file-scope helpers** exist in the TU (`grep` for
  `namespace {` and `static ` → 0) — so **no ODR prefixing** was needed (unlike refactor #1's
  `csf*`/`cpt*` renames). The move is literal verbatim cut/paste of whole external-linkage
  functions.
- **No shared mutable state / shared anon-ns helper** split across the seam.
- **No `scoring_model.md` sync** — `regiontonecollector.cpp` contains no template / bonus /
  guard / gate / scoring term (it is engraving-bridge tone collection); the CLAUDE.md sync
  rule does not apply.

The only divergence from a literal "delete just the 6 function ranges" is the single dropped
redundant separator blank (orig L576) and relocating the `using isDiatonicStep` declaration
(§2) — both byte-identical-in-behavior, neither a logic change.

---

## §4 — Pure-movement verification (how Cowork can confirm)

**Committed-object path** (authoritative, per the handoff note — working-tree numstat can be
stale): after a trial commit, `git show <hash> --numstat` should show exactly:

| File | ins | del | meaning |
|---|---|---|---|
| `engravingbridge/regiontonecollector.cpp` | **0** | **470** | PURE deletion (no residual line edited) |
| `engravingbridge/regiontoneprimitives.cpp` | 514 | 0 | new file (the moved functions) |
| `analysis/CMakeLists.txt` | 7 | 0 | new-TU registration + comment |

`regiontonecollector.h` absent from the diff (unchanged). Working-tree numstat already shows
`0 470` / `7 0` and the header clean (pre-commit).

**Source-level move-only proof** (reproducible, `C:/tmp/cc_refac_rtc_verify.py`, run against
the pristine HEAD backup `C:/tmp/regiontonecollector.cpp.orig`) — all assertions PASS:
1. **Residual is a pure ordered subsequence** of the original (every residual line equals an
   original line, in order, none edited) ⟹ `residual == original − lines[44–199] − lines[576–889]`.
2. **New TU is the verbatim concatenation** `original[1–199] ++ [577–891]` (every byte a copied
   original byte).
3. **Reconstruction:** every original line is covered by residual ∪ newTU **except** the single
   dropped separator blank (orig L576); the uncovered-set is exactly `{576}`.
4. Each of the **6 moved function bodies is byte-identical** pre/post and present **only** in the
   new TU; `collectRegionTones` present **only** in the residual.

**End-to-end behavior corroboration:**
- 3-preset corpus regen → `cc_refac1_corpusdiff.py diff` → **TOTAL_DIFF=0** (SHA-256 over
  353×3 `.ours.json` vs `C:/tmp/refac1_base`, the HEAD-`41f7c65f63`-equivalent baseline that
  refactor #1 itself proved 0-diff).
- `characterise_bir_false.py --corpus-dir` (manifest-validated, 353/353 complete each) →
  **57 / 23 / 57**.
- `composing_tests` 545 / `notation_tests` 57 / `pipeline_snapshot_tests` 11/11 (goldens
  untouched, golden tree git-clean — no `--update-goldens`).

**Baseline note:** `C:/tmp/refac1_base` is the HEAD-equivalent reference (refactor #1 snapshot,
proven 0-diff vs `41f7c65f63`). The working tree also carries the **uncommitted B2 guard**
(`localmodulationdetector`, correctly excluded from this refactor's scope); it is
flag-OFF-byte-identical with default flags (STATUS.md, Cowork-verified) so it does not confound
the 0-diff — confirmed by the actual TOTAL_DIFF=0.

Artifacts (gitignored scratch): `C:/tmp/regiontonecollector.cpp.orig` (pristine HEAD),
`C:/tmp/cc_refac_rtc_verify.py` (move-only proof), `C:/tmp/cc_refac1_corpusdiff.py` (0-diff
harness) + `C:/tmp/refac1_base/{baroque,jazz,default}` (baseline `.ours.json`).

---

## §5 — Unity / ODR handling

`composing_analysis` is a unity build; the new TU compiled into `unity_1_cxx.cxx.obj` and the
lib **linked with no redefinition error**. Two file-scope constructs are duplicated across the
residual and the new TU — both proven-safe:
- `namespace shv = mu::composing::analysis::scoreharvest;` — a namespace-alias redefinition to
  the **same** target is legal C++ and already appears in 3 sibling TUs of this same unity lib
  (`regionanalyzer.cpp`, `keyresolver.cpp`, `regiontonecollector.cpp`).
- `using mu::composing::analysis::isDiatonicStep;` — relocated to the new TU **only** (decision
  B), so there is exactly **one** occurrence in the `engravingbridge` namespace across the lib —
  zero duplicate-using surface.

No internal-linkage symbols moved, so **no `jkd*`/`csf*`-style prefixing** was required.

---

## §6 — Scope / stop-condition disposition

- Edits confined to instruction scope: the new TU `regiontoneprimitives.cpp`, the residual
  `regiontonecollector.cpp`, and `analysis/CMakeLists.txt`. `regiontonecollector.h` untouched;
  **nothing outside `src/composing/analysis/`** touched by this refactor. ✅
- No logic / constant / behavior / inference change; `collectRegionTones`' interior (the
  behavior-entangled pedal-tail / boost-normalize / traversal-idiom core flagged in the
  assessment §2.1) was **not** touched — it is the residual, audited later, not "fixed." ✅
- No named function turned out non-liftable; the seam was clean (no shared anon-ns helper, no
  residual dependency). No STOP condition hit. ✅
- HELD: **not committed, not pushed.** ✅

---

## §7 — On Cowork confirmation (the single commit)

One commit, local, **UNPUSHED** (user pushes), once Cowork verifies the move-only diff via the
committed-object path:

> `refactor: split regiontonecollector.cpp — lift tone/context primitives into their own TU`
> `(byte-identical).`

Staged together: the new `engravingbridge/regiontoneprimitives.cpp`, the modified
`engravingbridge/regiontonecollector.cpp` (pure deletion), and `analysis/CMakeLists.txt`. The
residual `collectRegionTones` accumulator is now isolated as an independently-auditable unit;
next pure-split candidates in assessment §5 order: `sectionanalyzer.cpp` → `harmonicsegmenter.cpp`
→ `keymodeanalyzer.cpp` → `keyresolver.cpp`.

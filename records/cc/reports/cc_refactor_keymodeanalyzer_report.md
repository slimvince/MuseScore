# CC Refactor Report — split `keymodeanalyzer.cpp` (byte-identical)

**Commit (local, UNPUSHED):** `a03c2493bba3690e5c9e661abe011b6c92cabe81`
*refactor: split keymodeanalyzer.cpp — lift display formatters
(keyModeTonicName/keyModeSuffix) into own TU (byte-identical).*

Branch `master`, 4 commits ahead of `origin/master` (this commit + the 3 prior
byte-identical split commits, all unpushed). **No push performed.**

---

## §0 Feasibility gate — results

Two candidate blocks were assessed at source (`git grep` for cross-TU reuse +
header read for external declarations).

### PASS — Display formatting → lifted
`keyModeTonicName(int, KeySigMode)` and `keyModeSuffix(KeySigMode)`:
- **Header-declared (external linkage)** — `keymodeanalyzer.h:551` / `:555`.
- Used across many TUs (notation bridges, `tools/batch_analyze.cpp`,
  `pipeline_snapshot_tests.cpp`) — confirmed by `git grep`.
- Depend on **nothing** in the anonymous namespace: only the `KeySigMode` enum
  (header) + `std::clamp` (`<algorithm>`). No coupling to `MODES`,
  `CHARACTERISTIC`, or any scorer helper.
- → Verbatim-liftable into `key/keymodeformatting.cpp`.

### SKIP — Mode-data / scorer library (the "shared-header caveat" block)
`MODES`, `ACTIVE_MODE_INDICES`, `CHARACTERISTIC`, `noteWeight`,
`scoreScaleMembership`, `scoreTriadEvidence`, `scoreCharacteristicPitch`,
`scoreTrueLeadingTone`, `scoreModePrior`, `scoreKeySignatureProximity`,
`tonalCenterScore`, `applyPairwiseDisambiguation`, `modeIsCompatibleWithDeclared`,
`possibleIonianFifthsForPc`, `resolveToFifths`, `TriadEvidence`,
`CandidateEvaluation`:
- An **anonymous-namespace internal-linkage cluster** whose **sole caller is the
  residual** `analyzeKeyMode`. This is exactly the harmonicsegmenter case.
- Separating it would require a **new shared header** or a **linkage promotion**
  (exposing internals) — **non-verbatim**.
- → **SKIPPED + surfaced** per §0 / §5. Not forced. Cohesive → stays in
  `keymodeanalyzer.cpp` as the orchestrator + its private scorer.

### SKIP — `keyModeScaleIntervals`
Header-declared, but its body reads the anon-ns `MODES` table — it cannot move
without the table (which stays with the scorer). → Left in the residual
(`keymodeanalyzer.cpp`, "Scale interval accessor" section, unchanged).

The externally-declared scorer-library helpers `ionianTonicPcForMode` and
`keySignatureFifthsForKey` are tightly coupled to the anon-ns scorer
(`resolveToFifths` / `scoreKeySignatureProximity`) and are not display
formatting; left in the residual.

---

## Move list

| File | Change |
|---|---|
| `src/composing/analysis/key/keymodeformatting.cpp` | **NEW** — license + `#include "keymodeanalyzer.h"` + `<algorithm>` + namespace; `keyModeTonicName` and `keyModeSuffix` moved **verbatim** (incl. the `// ── Display helpers ──` section comment). |
| `src/composing/analysis/key/keymodeanalyzer.cpp` | Removed the Display-helpers block (110 lines deleted, **0 added**). Header `keymodeanalyzer.h` **unchanged**. |
| `src/composing/analysis/CMakeLists.txt` | Registered the new TU under `key/` (+7 lines, comment + source entry). |

`git show a03c2493bb --numstat`:
```
7    0    src/composing/analysis/CMakeLists.txt
0  110    src/composing/analysis/key/keymodeanalyzer.cpp
139  0    src/composing/analysis/key/keymodeformatting.cpp
```

**Verbatim proof:** the moved 109-line block (committed new file) vs the
pre-commit original `keymodeanalyzer.cpp:832-940` → `diff` empty (0). Line
endings CRLF throughout, consistent with the repo.

---

## §3 Acceptance gate — byte-identical (all PASS)

1. **Build green** — full `setup_and_build.bat`, exit 0 (composing_analysis,
   composing_tests, notation_tests, batch_analyze, pipeline_snapshot_tests,
   MuseScore5 all linked).
2. **composing_tests** — 545/545 passed.
   **notation_tests** — 57/57 passed.
3. **pipeline_snapshot_tests** — 11/11 passed, **no `--update-goldens`**
   (1 pre-existing SKIP, 3 pre-existing DISABLED — unchanged).
4. **3-preset `.ours.json` 0-diff** — regenerated Baroque / Jazz / Default
   (353/353 each) into verification dirs; per-file `diff` vs the canonical
   HEAD-state dirs = **0 differing** for all three presets.
   **BIR** — Baroque **57** / Jazz **23** / Default **57** (exact match).

---

## Files outside the allowed set: none
Only the new TU + `keymodeanalyzer.cpp` + `CMakeLists.txt` changed. No header
change. No doc update needed (the moved functions are display formatters, not a
scoring term tracked by `docs/scoring_model.md`; the lone descriptive mention in
the working-tree-dirty `ARCHITECTURE.md` was not bundled, per §1). No push.

**Cowork:** verify the committed object `a03c2493bb` (`git show --numstat` +
verbatim `comm`/`diff` of the moved block + `:path`). Revert if any issue.

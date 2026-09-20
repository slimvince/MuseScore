# CC Refactor Report — split `sectionanalyzer.cpp` (byte-identical)

**Commit (local, UNPUSHED):** `2024f2951e`
**Parent:** `ed4b462021` (linear; HEAD before this work)
**Scope:** byte-identical pure code movement — cadence/pivot detection lifted into its own TU.
**Pass-4 stabilization extraction:** NOT done — surfaced as not cleanly liftable (see §4).

---

## §1 — What moved

Extracted **one** clean, self-contained block: the section-level **cadence + pivot
detection** (assessment §5 candidate #1, "~200 lines, fully independent").

| Symbol | Linkage | Declared in | Called by |
|---|---|---|---|
| `hasAssertiveKeyConfidence` | external (header-declared) | `sectionanalyzer.h` (unchanged) | `detectCadences`/`detectPivotChords`, residual `analyzeSection` (cross-TU via header), notation bridge |
| `detectCadences` | external (header-declared) | `sectionanalyzer.h` (unchanged) | `notationimplodebridge.cpp`, `notationcomposingbridge.cpp`, tests |
| `detectPivotChords` | external (header-declared) | `sectionanalyzer.h` (unchanged) | `notationcomposingbridge.cpp`, tests |

These three are independent of `analyzeSection` (the residual only *calls*
`hasAssertiveKeyConfidence`, which resolves across the TU boundary via the unchanged
header — exactly the regiontoneprimitives precedent). The original block was
`sectionanalyzer.cpp` lines **157–364** (section comment + the three functions +
trailing blank).

**New TU:** `src/composing/analysis/section/sectioncadencedetection.cpp`
- License header + descriptive comment + minimal includes
  (`sectionanalyzer.h`, `<algorithm>/<limits>/<string>/<vector>`, `analysisutils.h`,
  `chordanalyzer.h`, `keymodeanalyzer.h`, `sparsechordrefinement.h`) +
  `namespace cra = mu::composing::analysis::region;` + the verbatim block, wrapped in
  `namespace mu::composing::analysis { … }`.
- The moved 208 lines are **character-for-character identical** to the deleted lines.

**Declaring header:** `sectionanalyzer.h` is **unchanged** (the three functions were
already declared there).

**CMakeLists:** registered the new `.cpp` with a comment.

---

## §2 — Numstat (the byte-identity signature)

`git show 2024f2951e --numstat`:
```
5    0    src/composing/analysis/CMakeLists.txt
0    208  src/composing/analysis/section/sectionanalyzer.cpp
255  0    src/composing/analysis/section/sectioncadencedetection.cpp
```
`sectionanalyzer.cpp` = **0 insertions / 208 deletions = PURE DELETION** ⇒ byte-identical
movement (mirrors `ed4b462021`'s 0/470 on regiontonecollector.cpp). The new TU's 255
lines = 47-line header/includes/namespace prelude + 208 moved lines (verbatim) + closing
namespace.

---

## §3 — Acceptance gate (all PASS)

| Gate | Result |
|---|---|
| 1. Build green | ✓ (Unity build; all 5 executables linked; no errors) |
| 2. `composing_tests` | ✓ **545/545** |
| 2. `notation_tests` | ✓ **57/57** |
| 3. `pipeline_snapshot_tests` | ✓ **11/11**, NO `--update-goldens` (12th = baseline `PipelineDivergenceCObservation` SKIP, unchanged) |
| 4. 3-preset `.ours.json` 0-diff | ✓ Baroque **0/353**, Jazz **0/353**, Default **0/353** |
| 4. BIR | ✓ **57 / 23 / 57** (Baroque / Jazz / Default) |

Method for gate 4: regenerated each preset into a fresh `*_verify` dir (source corpus
`tools/corpus`, music21 GT copied not regenerated), diffed every `.ours.json` against the
baseline `tools/corpus/{baroque,jazz,default}` (manifest `git_hash=41f7c65f63`, a valid
reference since `ed4b462021` was itself verified byte-identical to it), then ran
`characterise_bir_false.py` on each verify dir. Verify dirs removed after measurement
(gitignored anyway).

---

## §4 — Pass-4 stabilization: NOT extracted (surfaced, not forced)

The assessment listed `stabilizeHarmonicRegionsForDisplay` ("Pass-4 stabilization") as a
*conditional* second extraction ("IF it extracts clean"). It does **not** extract cleanly
under the byte-identical / pure-movement rule:

- `stabilizeHarmonicRegionsForDisplay` is an **anonymous-namespace** helper (internal
  linkage) whose **sole caller is the residual `analyzeSection`** (`sectionanalyzer.cpp:920`).
- Moving it to a sibling TU would require promoting it **internal → external linkage** plus
  adding a new declaration (a new header or a `sectionanalyzer.h` change). That is *not*
  verbatim code movement and *not* the §1(b) "internal-linkage rename" — the
  regiontoneprimitives / regiontonecollector precedent only moved functions that were
  **already external + header-declared**.
- Its companion `distinctPitchClassCount` is likewise anon-namespace and is used by the
  orchestration residual (`sectionanalyzer.cpp:901-902`), not by stabilization — so they
  don't even form a self-contained unit.

Per §2 ("move only what is genuinely self-contained; if a piece is entangled with the
residual … STOP and surface it rather than forcing the split") and §5, this is surfaced
as entangled-with-residual and left in place. If a future (ratified) step wants it
extracted, it needs an explicit decision on the linkage promotion + declaration site (a
new internal `sectionstabilization.h`), which is beyond the byte-identical purity rule.

---

## §5 — Cowork verification (committed-object path)

```
git show 2024f2951e --numstat                 # exactly 3 files; sectionanalyzer.cpp 0/208 (pure deletion)
git log --format='%h parent=%p' -1 2024f2951e # parent=ed4b462021 (linear)

# verbatim move at the committed objects:
diff <(git show ed4b462021:src/composing/analysis/section/sectionanalyzer.cpp | sed -n '157,364p') \
     <(git show 2024f2951e:src/composing/analysis/section/sectioncadencedetection.cpp | sed -n '47,254p')
# → identical (CC ran this: COMMITTED-OBJECT VERBATIM MATCH; comm -23 empty)
```
- `.h` absent from the commit (boundary held — `sectionanalyzer.h` unchanged).
- Only in-scope files touched (new TU + `sectionanalyzer.cpp` + `CMakeLists.txt`); no
  docs/scoring_model.md change (the moved functions are not scoring terms — confirmed not
  referenced there).
- NOT pushed. If Cowork finds a problem: `git reset --soft HEAD~1`.

---

## §6 — Residual `sectionanalyzer.cpp` (now 763 lines)

Holds the section **orchestration**: `analyzeSection` (Passes 1–4 inline + key-area
grouping), the Pass-4 `stabilizeHarmonicRegionsForDisplay` + `distinctPitchClassCount`
anon-namespace helpers. Includes left untouched (a few may now be unused by the residual;
removing them would be a non-movement change, so left as-is per purity).

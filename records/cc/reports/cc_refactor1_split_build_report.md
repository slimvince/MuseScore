# Refactor #1 — `chordanalyzer.cpp` layer-split: BUILD REPORT (HELD)

> **Status: HELD — local, UNCOMMITTED, UNPUSHED.** Awaiting Cowork verification that the
> `git diff` is move-only before the single commit. Executes
> `cc_refactor1_split_design_dossier.md` §4 (the 5-step byte-identical split).
> Baseline / HEAD: `5fee657578`. Gitignored (`cc_*.md`).

---

## §0 — Result

All 5 extraction steps completed **strictly byte-identical** (pure code movement; NO
logic / scoring / inference / constant / template / gate change). Every per-step
acceptance gate passed:

| Gate | Requirement | Every step |
|---|---|---|
| Build | green (`setup_and_build.bat`) | ✅ |
| `composing_tests` | pass | ✅ 545/545 |
| `notation_tests` | pass | ✅ 57/57 |
| `pipeline_snapshot_tests` | 11/11, **no `--update-goldens`** | ✅ 11/11 (goldens untouched) |
| 3-preset `.ours.json` 0-diff | Baroque/Jazz/Default | ✅ TOTAL_DIFF=0 |
| BIR=false | 57 / 23 / 57 | ✅ 57 / 23 / 57 |

`chordanalyzer.h` is **unchanged** (the stable integration boundary). The
`kTemplateCount` size model never moved (templates array + 3 score matrices stay in the
oracle residual). No new compiler warnings — the only two C4100 warnings
(`chordanalyzer.cpp` `extThreshold`, `chordsymbolformatter.cpp` `keySignatureFifths`) are
pre-existing, relocated verbatim.

---

## §1 — What moved (final TU map)

Residual `chordanalyzer.cpp`: **3679 → 1501 lines** (the vertical **oracle**: scoring
constants/helpers, `TemplateDef`, the `kTemplateCount`-derived `templates` array + the 3
score matrices, `detectExtensions`, `buildChordResult`, `analyzeChord`, the factory).

| New TU | Lines | Holds | anon-ns renames |
|---|---|---|---|
| `chordsymbolformatter.cpp` | 1054 | `formatSymbol`, `formatRomanNumeral`, `formatNashvilleNumber` + Group-A helpers + `coreIntervals` + `romanWithInversion` + `isValidBassNoteName` + tonicization tables/helpers + Nashville block | `csf*` (12 ids) |
| `chordvoicing.cpp` | 233 | `chordTonePitchClasses`, `closePositionVoicing` | none |
| `chorddiagnose.cpp` | 188 | `RuleBasedChordAnalyzer::diagnoseChord` | none |
| `chordpostpasses.cpp` | 297 | `applyIter8691Pedal` + `isBassChordTone` | `cptIsBassChordTone` (1 id) |
| `postscoringgates.cpp` | 586 | `applyPostScoringGates` (+ margin constants `kGateIMargin/K/L`) | none |

`function/harmonicfunctionlayer.cpp` (the competition / function layer) was already a
separate TU — untouched.

---

## §2 — Per-step detail + gate results

Each step: programmatic extraction (exact source lines copied; word-boundary `\b` rename
of moved internal-linkage helpers only) → CMake add → build → 3 suites → snapshot 11/11 →
3-preset regen + 0-diff vs frozen baseline + BIR. Line ranges are against the file state
**at that step** (the file shrinks each step).

| Step | TU | Source ranges moved (at step) | Drops | Renames | Gate |
|---|---|---|---|---|---|
| 1 | `chordsymbolformatter.cpp` | 38–665, 823–864, 3125–3466 | 1012 | `pitchClassName→csfPitchClassName`, `pitchClassNameFromTpc→csf…`, `qualitySuffix`, `chromaticRoman`, `diatonicRoman`, `coreIntervals`, `romanWithInversion`, `isValidBassNoteName`, `kTonicizationScales/Parent`, `diatonicDegreeForPc`, `isDegreeMajorThird` → `csf*` | ✅ 0-diff / 57·23·57 / 545·57·11 |
| 2 | `chordvoicing.cpp` | 2456–2656 | 201 | none | ✅ 0-diff / 57·23·57 / 545·57·11 |
| 3 | `chorddiagnose.cpp` | 2300–2453 | 154 | none | ✅ 0-diff / 57·23·57 / 545·57·11 |
| 4 | `chordpostpasses.cpp` | 785–857 (isBassChordTone), 2114–2298 (applyIter8691Pedal) | 258 | `isBassChordTone→cptIsBassChordTone` | ✅ 0-diff / 57·23·57 / 545·57·11 |
| 5 | `postscoringgates.cpp` | 960–1512 | 553 | none | ✅ 0-diff / 57·23·57 / 545·57·11 |

**Σ drops = 1012+201+154+258+553 = 2178 = 3679 − 1501** (exact reconciliation — no gaps,
no double-counting).

---

## §3 — Dossier deviation surfaced (necessary, still pure movement)

**`coreIntervals` (orig 621–665) and `romanWithInversion` (orig 823–864) were added to
Step 1**, beyond the dossier §3 step-1 list ("Group A helpers 44–619 + …"). Reason,
verified at source by grep:

- `romanWithInversion` is called **only** by `formatRomanNumeral` (orig L3276).
- `coreIntervals` is called **only** by `romanWithInversion` (orig L831).

Both are formatter-exclusive, internal-linkage anon-ns helpers. `formatRomanNumeral`
moves to `chordsymbolformatter.cpp`, so leaving these two behind in the oracle's anon
namespace would make the formatter TU **fail to link** (internal-linkage symbols are not
visible across TUs), and exposing them would require touching `chordanalyzer.h`
(forbidden). Moving them with their sole consumer is the only byte-identical option and is
pure code movement (prefixed `csfCoreIntervals` / `csfRomanWithInversion`). The dossier's
move-list under-specified them; no logic changed. (This is the only divergence from the
dossier's literal step lists.)

---

## §4 — Pure-movement verification (how Cowork can confirm)

For every step the extraction script asserted, with CRLF preserved byte-for-byte:

1. **Reverted-block verbatim:** reverting the `csf*`/`cpt*` renames in the new TU
   reproduces the moved source block **exactly** (`block in reverted-new == True`).
2. **Residual is a pure subsequence:** `residual == original-minus-dropped-line-ranges`
   (`== True`) — no residual line modified.
3. **No old identifier survives:** 0 occurrences of any renamed id in the new TU or the
   residual; all `csf*`/`cpt*` ids present in the new TU.

End-to-end corroboration:
- `git diff --stat src/composing/analysis/chord/chordanalyzer.cpp` → **2178 deletions,
  0 insertions** (the residual is the original with lines removed — no line changed/added).
- `git status` on `chordanalyzer.h` → **no change**.
- Σ per-step drops = 2178 = 3679 − 1501 (§2).
- 5× full 3-preset corpus 0-diff + BIR 57/23/57 + snapshots untouched (no `--update-goldens`).

Reproduction artifacts (in `c:/tmp/`, gitignored scratch):
- `chordanalyzer.cpp.step1.bak` = pristine HEAD `5fee657578` original (for diffing).
- `cc_refac1_step{1..5}.py` = the extraction scripts (each prints its self-verification).
- `cc_refac1_corpusdiff.py` = baseline-snapshot / 0-diff harness; baseline `.ours.json`
  in `c:/tmp/refac1_base/{baroque,jazz,default}`.

---

## §5 — Unity / ODR handling

`composing_analysis` is a unity build (`unity_0/1_cxx.cxx.obj` observed). Moved file-scope
anon-ns / `static` helpers were prefixed (`csf*` in the formatter TU; `cptIsBassChordTone`
in the post-passes TU) per the established `jkd*`/`lmd*` precedent — internal-linkage
rename ⇒ byte-identical. The lib linked with **no redefinition error** at every step. The
Nashville nested-anon-ns helpers (`namespace ChordSymbolFormatter { namespace { … } }`)
were left unprefixed (sole contributor; collision-safe) and linked clean.

---

## §6 — `docs/scoring_model.md` sync (location pointers only — done)

No scoring term added/changed ⇒ §2 template count (17) and all bonus/gate/§9 content
unchanged. Edits are **file-location pointers only**:
- New intro "File layout after refactor #1" note (the 5 TUs + what each holds; oracle
  stays in `chordanalyzer.cpp`).
- §6 E3 "execution location": `applyPostScoringGates` defined in **`postscoringgates.cpp`**
  (was `chordanalyzer.cpp`).
- §10 E3 changelog: gates A–L now in **`postscoringgates.cpp`**.

**Not touched (out of scope):** the §5 "Lambda at `chordanalyzer.cpp:~L20xx`" refs for
`w_complete`/`w_stepIn`/`w_stepOut`/`w_seq`/`w_dim`/B2-aug7-guard. Verified those signals
live in `function/harmonicfunctionlayer.cpp` (Stage-3.3 migration) — i.e. those refs are
**pre-existing staleness this refactor did not cause and did not move**; per the purity
rule ("do not fix the surfaced tangles") they are left for a separate doc cleanup.

---

## §7 — Scope / stop-condition disposition

- Edits confined to §2-scope: `chord/` (5 new TUs + residual), `analysis/CMakeLists.txt`,
  `docs/scoring_model.md`. `chordanalyzer.h` untouched. ✅
- No logic / constant / template / gate / inference change; no tangle "fix" (T1–T4 left
  as-is — `buildChordResult` stays with the oracle, diatonic tables still triplicated). ✅
- One surfaced necessity (§3, `coreIntervals`/`romanWithInversion`) — byte-identical, not a
  logic change; documented rather than silently absorbed. ✅
- HELD: **not committed, not pushed.** ✅

---

## §8 — On Cowork confirmation (the single commit)

One commit, local, **UNPUSHED** (do not push):

> `refactor: split chordanalyzer.cpp into single-responsibility layer TUs (byte-identical;`
> `oracle residual + formatter/voicing/diagnose/post-passes/gates); isolates the gate layer`
> `for refactor #2.`

Staged together: the 5 new `chord/*.cpp`, modified `chordanalyzer.cpp`,
`analysis/CMakeLists.txt`, and `docs/scoring_model.md` (CLAUDE.md sync rule). The gate
layer is now isolated in `postscoringgates.cpp` — the refactor-#2 dissolution target.

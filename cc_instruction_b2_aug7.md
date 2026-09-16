# CC Instruction — Commit tooling + B2 Augmented dominant 7th template

**Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`

**Current state:** Branch `master`, HEAD `f3e0f5f72c`. Working tree has uncommitted
tooling changes from the classifier-fix session (no src/ edits, no rebuild needed).
BIR baselines (lenient-OR): Baroque BIR=true=28, BIR=false=16; Jazz BIR=true=35,
BIR=false=10. Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
Tests: 407/407 composing, 52/52 notation (fully green), pipeline_snapshot 11/11 (1
skipped). rn_agree hard stop: must not drop below 27.6%.

---

## Step 1 — Commit the dirty tooling changes (no src/ changes)

These files are already edited and correct; just commit them:

```
cd C:\s\MS && git add tools/compare_rn.py tools/find_maj_to_dom7.py tools/reports/rn_corrected_classifier_f3e0f5f72c.txt tools/reports/rn_corrected_breakdown_f3e0f5f72c.txt tools/reports/maj_to_dom7_samples.txt; echo "exit:$?"
cd C:\s\MS && git commit -m "tools: fix compare_rn.py classifier (split quality_err into key_disagree/quality_disagree), add find_maj_to_dom7.py, save corrected RN reports"; echo "exit:$?"
```

Report the new HEAD commit hash.

---

## Step 2 — B2: Add Augmented dominant 7th template {0,4,8,10} (C7♯5)

**Goal:** Give the analyzer a dedicated template for the augmented dominant seventh
chord (C7♯5 = C, E, G#, Bb). Currently these chords score against the plain Augmented
triad template {0,4,8} (missing the 7th) or the dominant-7th template {0,4,7,10}
(missing the augmented fifth), whichever happens to win. A dedicated template improves
scoring precision.

**Risk assessment** (do this before any edit):

Read `src/composing/analysis/chord/chordanalyzer.cpp` lines 1955–1972 to confirm
the current 16-entry template array. Then verify that {0,4,8,10} (C, E, G#, Bb) does
NOT appear as a subset of any common Baroque diatonic chord. Key check: G# (pc=8) is
the augmented fifth and is non-diatonic in both C major and C minor — it requires a
chromatic alteration. This means the {0,4,8,10} PC set cannot arise from a diatonic
Baroque progression, so the B1 leading-tone-ambiguity concern does NOT apply here.
Confirm this reasoning and proceed.

**Pre-edit checks:**

a) Search for how `ChordQuality::Augmented` is handled in `detectExtensions()` — verify
   that MinorSeventh can already be detected on an Augmented-quality result:
   ```
   grep -n "Augmented\|augmented\|Aug" src/composing/analysis/chord/chordanalyzer.cpp | head -40; echo "exit:$?"
   ```
   The template sets `quality = Augmented`; `detectExtensions()` should apply the
   standard MinorSeventh gate (`pcWeight[rootPc+10] > extensionThreshold`) regardless
   of quality. Confirm it is not Augmented-quality-gated out.

b) Verify that `qualitySuffix()` / `formatSymbol()` can produce the correct symbol for
   `Augmented` + `MinorSeventh` extension. The expected output is something like `C+7`
   or `Caug7` or `C7#5`. If the formatter doesn't handle this combination, note what it
   does produce (so we can gauge whether a display fix is also needed — but don't block
   the template addition on display).

**Edit sites — four total (same pattern as B1):**

**Site 1 — `analyzeChord` templates array (L1955)**

Change `std::array<TemplateDef, 16>` → `std::array<TemplateDef, 17>`.

Insert the new template **immediately after** the existing Augmented triad entry
`{ ChordQuality::Augmented, {0,4,8}, {0,+4,+8} }`:

```cpp
{ ChordQuality::Augmented,      { 0, 4, 8 },        { 0, +4, +8 }       },
{ ChordQuality::Augmented,      { 0, 4, 8, 10 },    { 0, +4, +8, -2 }   },  // aug7 (C7♯5)
```

The score offset for the minor-seventh tone (10) is `-2`, consistent with all other
seventh templates in the array (dom7, min7, HalfDim).

**Site 2 — Three score matrices (L2013–2015)**

Change each of the three `std::array<std::array<double, 16>, 12>` declarations to
`std::array<std::array<double, 17>, 12>`:

```cpp
std::array<std::array<double, 17>, 12> basisIndepMatrix{};
std::array<std::array<double, 17>, 12> complexityFactorMatrix{};
std::array<std::array<double, 17>, 12> augFactorMatrix{};
```

**Site 3 — `diagnoseChord` templates array (L3368)**

Change `std::array<TemplateDef, 16>` → `std::array<TemplateDef, 17>`.

Insert the same new entry in the same position (immediately after the Augmented
triad entry in `kDiagTemplates`).

That is all four edit sites. **Do not edit any other file at this stage.**

---

## Step 3 — Build and run both test suites

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_b2.txt 2>&1; echo "exit:$?"
head -5 /tmp/comp_b2.txt; tail -5 /tmp/comp_b2.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_b2.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|tests?" /tmp/note_b2.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_b2.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|tests?" /tmp/snap_b2.txt | tail -5; echo "exit:$?"
```

**Expected:** 407/407 composing, 52/52 notation, 11/11 pipeline_snapshot (1 skipped).
If pipeline_snapshot tests fail, read the first failing test's diff:
```
grep -A 30 "FAILED\|Expected" /tmp/snap_b2.txt | head -60; echo "exit:$?"
```

If any snapshots fail due to the new template firing on an existing snapshot score
(winner changed), the change is likely correct — run `--update-goldens` **only after**
verifying the new winner is musically correct:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens > /tmp/snap_b2_upd.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|updated" /tmp/snap_b2_upd.txt | tail -10; echo "exit:$?"
```
Then re-run to confirm all pass. Do **not** update goldens if the snapshot regression
is in a Baroque score and the new winner looks wrong (e.g., an E major triad becoming
E7♯5 on a thin 2-PC region).

---

## Step 4 — BIR check for both presets

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_baroque_b2.txt 2>&1; echo "exit:$?"
cat /tmp/bir_baroque_b2.txt; echo "exit:$?"
```

Then Jazz:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_jazz_b2.txt 2>&1; echo "exit:$?"
cat /tmp/bir_jazz_b2.txt; echo "exit:$?"
```

**Hard stops:** Baroque BIR=false > 25, Jazz BIR=false > 13.

If either hard stop is hit, **revert the template addition** (git checkout
src/composing/analysis/chord/chordanalyzer.cpp), report the regression details, and
stop. Do not attempt fixes without further instruction.

---

## Step 5 — Read chord mismatch report

```
cat C:\s\MS\src\composing\tests\chord_mismatch_report.txt; echo "exit:$?"
```

Expected: 4 RealDiff / 127 ConventionDiff (unchanged from baseline). Any new RealDiff
entry is a regression — report it.

---

## Step 6 — Report and commit (if clean)

If all tests pass and BIR is within hard stops, commit:

```
cd C:\s\MS && git add src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"
cd C:\s\MS && git commit -m "B2: add Augmented dominant 7th template {0,4,8,10} (C7#5)

Adds a dedicated template for the augmented dominant seventh chord alongside
the existing Augmented triad. The minor seventh offset (-2) is consistent with
all other seventh templates. {0,4,8,10} is non-diatonic in both major and
minor keys (augmented fifth requires chromatic alteration), so no Baroque
leading-tone ambiguity.

BIR: Baroque BIR=true=XX BIR=false=XX; Jazz BIR=true=XX BIR=false=XX.
Tests: 407/407 composing, 52/52 notation, 11/11 pipeline_snapshot (1 skipped).
[N goldens refreshed / no goldens changed]"; echo "exit:$?"
```

(Fill in the actual BIR numbers from Step 4.)

Report back:
1. Commit hash for the tooling commit (Step 1)
2. Pre-edit risk-assessment result (was {0,4,8,10} safe from B1-style ambiguity?)
3. detectExtensions + formatSymbol behaviour for Augmented+MinorSeventh
4. BIR delta: Baroque (before → after) + Jazz (before → after)
5. Any snapshot goldens refreshed (and whether the new winner is musically correct)
6. Commit hash for B2 (or revert notice if hard stop was hit)

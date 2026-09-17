# CC Instruction: Stage 2.1 — Phase 4c move: analyzeSection into the composing module

## Context

Master plan: `docs/implementation_roadmap.md` Stage 2, item **2.1** — the first
production-code instruction since the reviews. The unified section-level analysis entry
`analyzeSection()` and its analysis helpers live in
`src/notation/internal/notationcomposingbridgehelpers.cpp` — analysis logic in the wrong
module (Dependency Rule §3.3; `composing/CMakeLists.txt:41` records the deferred move).
This blocks Stage 2.2 (batch parity needs to CALL the section-level pass from
`batch_analyze`, which must not link the notation module) and Phase E/E4 (the only
cadence implementation must live where the function layer will consume it).

**Goal: relocation, byte-identical. Zero logic changes.** Same code, new home.

**Epistemic rule (standing, from Stage 1d): NEVER GUESS** — investigate or state the
unknown explicitly. For a move this size, that especially means: do not "tidy" code in
flight, do not resolve TODOs you pass, do not reorder logic. Mechanical relocation only.

**File authorization for this run** (explicitly approved, relayed by the user):
- `src/composing/**` (pre-authorized as always)
- `src/notation/internal/notationcomposingbridgehelpers.{cpp,h}`,
  `notationcomposingbridge.{cpp,h}`, `notationimplodebridge.{cpp,h}`,
  `notationharmonicrhythmbridge.cpp` — caller/include updates and code REMOVAL only
- `src/notation/tests/**` (test relocation/include updates),
  `src/composing/tests/**`, both CMakeLists
- NOTHING else. If the move seems to require touching engraving or other modules,
  stop and ask.

Mandatory reads: STATUS.md header; `docs/implementation_roadmap.md` Stage 2;
`docs/unified_analysis_pipeline.md` (Phase 4c deferral context); `analyzed_section.h`
(the types already in composing); `composing/CMakeLists.txt` ~L41 comment;
`notationcomposingbridgehelpers.cpp` end-to-end (the code being moved).

---

## Task 1 — Survey + move plan (report §1 BEFORE implementing; no stop needed unless a
blocker appears — proceed when the plan is internally consistent)

1. Inventory `notationcomposingbridgehelpers.cpp`: for every function, classify:
   - **MOVE** — analysis logic: `analyzeSection`, `stabilizeHarmonicRegionsForDisplay`,
     `detectCadences`, `detectPivotChords`, `diatonicDegreeForRootPc`,
     `resolveKeyAndMode`, `collectPitchContext`, weighting helpers
     (`beatTypeToWeight`, `timeDecay`, `regionMetricWeightForBeatType`, …), the thin
     sparse-refinement wrappers, and whatever else is score-analysis (verify each —
     this list is from the part-2 review, re-derive it, don't trust it).
   - **STAY** — genuinely notation/UI-side: annotation writing, selection handling,
     display-string assembly, anything touching notation interaction types.
   - **UNCLEAR** — list with the specific question.
2. Decide the target home and justify: suggested
   `src/composing/analysis/section/sectionanalyzer.{h,cpp}` (new), or extend
   `engravingbridge/` — the code consumes `mu::engraving::Score`, which
   `composing/analysis/engravingbridge/regiontonecollector` already does, so the
   dependency is precedented. Namespace: `mu::composing::analysis` (or a `section`
   sub-namespace). Composing must NOT include anything from `src/notation`.
3. Configuration access: the helpers read `IComposingAnalysisConfiguration` (already a
   composing-owned interface — verify) — confirm the move keeps the same access path or
   document the injection change (mechanical only).
4. Caller strategy: `notationcomposingbridge.cpp` (:244, :1117),
   `notationimplodebridge.cpp` (:1373), `pipeline_snapshot_tests.cpp` (:320, :716,
   :1059) call `mu::notation::internal::analyzeSection`. Plan: callers switch to the
   composing symbol directly (preferred — no shim), OR a temporary inline delegate in
   the notation header if churn demands it (justify if so; it must be marked for
   removal in 2.2).
5. Tests: `notationannotate_tests.cpp` pins detectCadences/detectPivotChords. Decide:
   move those tests to `src/composing/tests/` (now possible — the 1c environment loads
   Scores… verify they even need Scores; the 1b-style direct-construction may apply) or
   leave them in notation tests calling the composing symbol. Either is fine;
   byte-identical test count (52 notation may shrink if tests move — document the
   ledger so total coverage provably doesn't drop).

## Task 2 — The move

Mechanical relocation per the Task-1 plan. Rules:
- Function bodies byte-identical (whitespace/include-order changes only as forced by
  the new home). No renames beyond namespace. No logic edits.
- `notationcomposingbridgehelpers.cpp` shrinks accordingly; what remains must be only
  the STAY list. Update the file-top comment to say the analysis layer moved
  (reference composing target + this instruction).
- CMakeLists: composing gains the new sources; check link direction (notation already
  links composing — verify nothing now needs the reverse, which would be a stop
  condition).
- Update the `composing/CMakeLists.txt:41` comment (the deferral is resolved).

## Task 3 — Riders (small, explicitly in scope)

1. `chordanalyzer.h:402–409` doc-comment fix (the residual): delete the
   "Baroque: 2.5 / Jazz: 0.6" lines and correct the stale signal list (the four LIVE
   signals are stepwise, lookahead, sameRoot, completeTriad — verify against
   `bassDependentContextualBonuses` before writing; nextRoot/consecutive/recentRoot/
   weakBeat are not part of this sum — verify what happened to them and reflect
   reality). Reference scoring_model §4's "currently inert" paragraph.
2. NOTHING else rides. (No B/C/D removal, no diagnoseChord work — later items.)

## Task 4 — Verify (full gate)

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/s21_compose.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s21_compose.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/s21_notation.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s21_notation.txt
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/s21_snap.txt 2>&1; echo "exit:$?"
tail -10 /tmp/s21_snap.txt
cd C:\s\MS && python -m unittest discover -s tools/tests -p "test_*.py" > /tmp/s21_py.txt 2>&1; echo "exit:$?"
tail -3 /tmp/s21_py.txt
```
Required: composing 498 (± the documented test-ledger moves) all green; notation
all green (± ledger); **pipeline snapshots 11/11 ZERO diffs — this is the decisive
byte-identity proof, since the snapshot tests call analyzeSection itself**; 54 Python OK.

BIR both presets (code touched — policy):
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus > /tmp/s21_b.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py > /tmp/s21_bir_b.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s21_bir_b.txt
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus > /tmp/s21_j.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py > /tmp/s21_bir_j.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s21_bir_j.txt
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus > /tmp/s21_rest.txt 2>&1; echo "exit:$?"
```
Required: 13 / 7, unchanged (batch path doesn't touch the moved code — confirm that
expectation held).

## Report — `cc_stage2_1_report.md`

1. §1 the MOVE/STAY/UNCLEAR inventory + target-home decision + caller strategy +
   test ledger (counts before/after per suite, proving no coverage drop).
2. §2 file map: what now lives where (this updates ARCHITECTURE.md in a follow-up doc
   pass — propose the text, don't apply).
3. §3 the Task-3 rider diff (quote the new chordanalyzer.h comment).
4. §4 verification table incl. BIR.
5. §5 deviations/unknowns (never-guess rule).
6. §6 commit proposal — TWO commits, both awaiting Cowork confirmation:
   - Commit A (rider): `docs(code): correct stale maxTotalInversionContextBonus
     doc-comment (chordanalyzer.h)` — tiny, separable.
   - Commit B (move): `refactor: move analyzeSection + section-level analysis into
     composing module (Phase 4c / Stage 2.1)` — full message proposing the file map,
     byte-identity evidence (zero snapshot diffs, BIR unchanged), and the test ledger.

Stop conditions: any snapshot diff or BIR movement (byte-identity broken — stop, do not
refresh goldens); a circular module dependency; an UNCLEAR item that blocks the STAY/MOVE
split; anything outside the authorized file list; any temptation to change logic.

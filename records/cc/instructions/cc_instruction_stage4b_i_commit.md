# CC Instruction: commit Stage 4b-i (RATIFIED)

Stage 4b-i was Cowork-verified at source (four demotions correct; hysteresis `:323-345` untouched;
toggle inert default-off; mode-present gate byte-identical 57/23/57 all three presets; no off-limits
production edit; the mode-absent floor is pre-existing crutchless behavior, not a regression). **This
instruction releases the HELD hold and ratifies the commit.**

## Commit exactly the 13 already-staged files — nothing else

```
docs/back_half_design.md
docs/key_path_design.md
docs/stage4b_design.md
src/composing/analysis/key/keymodeanalyzer.cpp
src/composing/analysis/key/keymodeanalyzer.h
src/composing/analysis/key/keyresolver.cpp
src/composing/analysis/key/keyresolver.h
src/composing/tests/regionanalysis_tests.cpp
src/notation/tests/notationimplode_tests.cpp
src/notation/tests/pipeline_snapshot_tests/snapshots/chopin_bi105_op30_2.json
src/notation/tests/pipeline_snapshot_tests/snapshots/corelli_op01n08a.json
tools/batch_analyze.cpp
tools/run_bach_preset.py
```

Before committing, confirm `git diff --cached --name-only` lists **exactly** those 13. The report
`cc_stage4b_i_report.md` is gitignored — confirm it is **NOT** in the staged set (do not add it). The
regenerated `tools/corpus/*_4bi*/` corpora are gitignored — do not add them. If anything else is
staged, STOP and report.

## Commit message

```
feat(key): demote declared-mode wall to a droppable hint; note-based mode inference primary (Stage 4b-i)

Demotes the four declared-mode mechanisms so note-based major/minor inference is primary
and the declared mode is a low-weight droppable tiebreaker (Stage-4 redirect, back_half_design §4):
- declaredModePenalty 7.0 -> 1.0 (a tiebreaker, not a wall); bounds {3.0,15.0} -> {0.0,15.0}
- removed the hard "Strong declared-mode prior" promotion (keyresolver) -- a score-gap-ignoring
  veto incompatible with note-based-primary inference
- piece-start declared anchor -> note-based opening (normal lookahead runs from piece start)
- partialSignatureCorrection unchanged (declared-gated; a note-triggered detector is deferred)
- adds --ignore-declared-mode measurement toggle (default off, inert by construction)

2nd intentional behavior change. Mode-present: nearly free (Default S2 +2, Baroque 0); BIR gate
byte-identical 57/23/57 on all three presets; corelli_op01n08a snapshot improves G/iv -> C/i
(DCML-correct). The mode-absent floor (measurement only) quantifies that note-based relative-pair
inference is currently weak -- the 4b-ii target; it is pre-existing crutchless behavior, not a
regression (the four mechanisms are all gated on declaredMode.has_value()). Test re-pins + 2
snapshot goldens DCML-verified. Report: cc_stage4b_i_report.md.
```

## Do NOT push

The user pushes (timing is theirs). **Note the chain:** 4b-i commits on top of the Stage-4a commit
`faa1ee5388`. Local history is `a96f179f40` (on origin/master) → `faa1ee5388` (4a) → 4b-i. Both 4a and
4b-i can go to the user's FORK (`origin` = slimvince/MuseScore) freely — `origin` is not MuseScore core,
and `upstream` push is disabled. The guardrail against MuseScore core is the disabled upstream push +
upstreaming-by-deliberate-cherry-pick, NOT keeping commits off the fork. CC simply does not push here;
the user pushes when ready.

Report the new commit hash and `git log --oneline -3`.

**Stop conditions:** anything other than the 13 files staged; the report or corpora appearing in the
staged set; unexpected tracked `src/` modifications (report before committing).

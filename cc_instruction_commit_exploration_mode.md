# CC Instruction: Commit Phase E explorationMode resolution

## Context

The explorationMode work is verified and approved (Cowork re-verified code-level
equivalence independently, 2026-06-10). Commit it now.

**⚠ The working tree contains UNRELATED dirty files that must NOT be committed:**
`CLAUDE.md`, `ARCHITECTURE.md`, `docs/redesign_plan.md`, `COWORK_HANDOFF.md`,
`STATUS.md`, and the perpetually-dirty `muse` submodule (intentional Snap fix +
CRLF noise — never stage it). Use explicit per-file `git add` only. No `git add -A`,
no `git add .`, no `git commit -a`.

## Task 1 — Stage exactly these 7 files

```
cd C:\s\MS && git add \
  src/composing/analysis/chord/chordanalyzer.h \
  src/composing/analysis/chord/chordanalyzer.cpp \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/harmony/harmonicsegmenter.cpp \
  src/composing/tests/gater_tests.cpp \
  docs/scoring_model.md ; echo "exit:$?"
```

Verify the staged set is exactly those 7 paths and nothing else:

```
cd C:\s\MS && git diff --cached --name-only ; echo "exit:$?"
```

If anything else appears staged (especially `muse`), `git reset` and start over.

## Task 2 — Commit

Use the report §6 message verbatim. Write it to a temp file and commit with `-F`:

```
cd C:\s\MS && git commit -F /tmp/expl_commit_msg.txt ; echo "exit:$?"
```

Message (write to `/tmp/expl_commit_msg.txt` first, exact content):

```
refactor: replace explorationMode flag with ScoringPhase enum (Phase E Step 5)

Remove the explorationMode bool from ChordAnalyzerPreferences and from the five
bonus/gate signatures (wSeqBonus, wDimBonus, wStepInBonus, wStepOutBonus,
gateRZeroesRootContinuity). Those functions are now stateless and pure. The
segmentation-vs-final control point lives in one place: applyHarmonicFunction()
checks `phase == ScoringPhase::Final` once (applyProgressionSignals) and gates the
four progression bonuses, Gate R, and the Pass B step-bonus guard on it.
rootContinuityBonus stays active in both phases (segmentation depends on it).

ScoringPhase is defined in chordanalyzer.h (function namespace, alongside the
ScoringSnapshot forward declaration) — not harmonicfunctionlayer.h — because the
include chain runs harmonicfunctionlayer.h -> chordanalyzer.h and the
ChordAnalyzerPreferences `= ScoringPhase::Final` default member initializer needs the
complete enum (a forward declaration is insufficient).

harmonicsegmenter.cpp's two boundary-exploration sites now set
scoringPhase = ScoringPhase::Segmentation. gater_tests.cpp Branch 4 ("no fire in
exploration mode") is replaced by an end-to-end phase-gating test via
applyHarmonicFunction. docs/scoring_model.md updated in the same commit (sync rule).

Behaviour-preserving: composing 416/416, notation 52/52, pipeline snapshots 11/11
(zero diffs, no goldens refreshed). BIR unchanged on both corpora: Baroque 24/13,
Jazz 35/7.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

## Task 3 — Post-commit verification

```
cd C:\s\MS && git show --stat HEAD > /tmp/expl_commit_stat.txt 2>&1 ; echo "exit:$?"
head -30 /tmp/expl_commit_stat.txt
cd C:\s\MS && git status --porcelain | head -20 ; echo "exit:$?"
```

Confirm:
1. HEAD commit contains exactly the 7 files.
2. The unrelated dirty files (CLAUDE.md, ARCHITECTURE.md, redesign_plan.md,
   COWORK_HANDOFF.md, STATUS.md, muse) are still modified-but-uncommitted.
3. Do NOT push.

## Report

Reply with: the new HEAD hash, the `git show --stat` file list, and confirmation
that the unrelated dirty files were untouched. No separate report file needed.

## Out of scope

- The ARCHITECTURE.md / layer_architecture_audit.md / COWORK_HANDOFF.md doc pass
  (explorationMode references) — separate task, Cowork will instruct later.
- No code changes, no builds, no test runs — this is a commit-only task.

# CC — Stage-0 stash doc-recovery report

**Date:** 2026-06-25 · **Operator:** Claude Code · **Outcome:** SUCCESS — Cowork doc work recovered & committed; stash retained.

## 1. Safety preconditions (§0)
- Stash present: `stash@{0}` = `bc4fa79c4a9ef4401794b321dfec81fa54bae78e` ✓ (matches instruction).
- HEAD == `b57dbfa7a805…` (the `--seq-tpc-weight` backout) ✓; tree clean at start ✓.
- **Stash never popped/dropped/applied.** Restores done via `git checkout <treeish> -- <path>` (path-scoped), retaining the stash.

## 2. Stash-contents enumeration + cross-check (§0)
Stash holds **23 tracked-modified** (`stash@{0}` tree) + **33 untracked** (`stash@{0}^3` tree) = 56 paths.

### 2a. Tracked-modified (23) — all classified, none surprising
- **§1 (restore):** `CLAUDE.md`, `COWORK_HANDOFF.md`, `cowork_design_doc_template.md`, `cowork_layer1_note_model_design.md`, `cowork_layer2_slicing_design.md`, `cowork_layer3_keymode_design.md`, `cowork_target_architecture.md` (7)
- **§2 (leave in stash):** `BUILD_AND_TEST.md`, `STATUS.md`, `cowork_github_9444_comment_draft.md`, `docs/back_half_design.md`, `docs/decoder_design.md`, `src/composing/analysis/chord/chordslicedecoder.{cpp,h}`, `src/composing/analysis/engravingbridge/regiontoneprimitives.cpp`, `src/composing/analysis/key/keymodeanalyzer.h`, `src/composing/analysis/key/keymodesequence.{cpp,h}`, `src/composing/analysis/section/localmodulationdetector.{cpp,h}`, `tools/batch_analyze.cpp`, `tools/cc_layer3_keymode_baseline.py`, `tools/compare_rn.py` (16)

### 2b. Untracked (33) — 9 §1 + 24 NOT-IN-EITHER-LIST (surprise; flagged & classified before acting)
- **§1 (restore), 9:** `cowork_bounded_context_design.md`, `cowork_delta_check_dispositions.md`, `cowork_l1l3_stabilization_plan.md`, `cowork_layer1_extend_design.md`, `cowork_layer3_spec_language_sweep.md`, `cowork_layer4_chordsymbol_design.md`, `cowork_layer4_spec_review.md`, `cowork_spec_language_sweep.md`, `cowork_uncertain_resolver_investigation.md`
- **SURPRISE — in neither §1 nor §2 (24):** STOPPED per §0/§6 and asked the user (classify first):
  - `cowork_prune_pass_checklist.md` (1) — genuine Cowork process doc ("PRUNE/TIDY PASS checklist"). **User ruled (AskUserQuestion 2026-06-25): "Add to the §1 commit"** → restored & committed.
  - `err.txt` (1) — empty (0 lines) — scratch.
  - `src/composing/tests/data/{META-INF/container.xml, Thumbnails/thumbnail.png, audiosettings.json, automation.json, score_style.mss, viewsettings.json}` (6) — unzipped-`.mscz` innards / test-data scratch.
  - `tools/{b2_measure.sh, dump_bir_cases.py, iter90_wrong_root_characterization.txt, iter97_birfalse_cases_data.txt}` (4) — non-`cc_`-prefixed iteration scratch.
  - `ai-assistant/` (13) — read-only ms-core-api share (`CLAUDE.md`, `ROADMAP.md`, `TODO.md`, `handover.md`, `SESSION_START.md`, `HANDOVER_TESTING.md`, `CC_LOG_FIX_REQUIRED.md`, `GITHUB_COMMENT_24673.md`, `SMOKETEST_batch3_8.md`, `SMOKETEST_v051.md`, `SMOKETEST_v051_RESULTS.md`, `SMOKETEST_v052_RESULTS.md`, `SMOKETEST_v054_RESULTS.md`).
  - **Note:** `cowork_prune_pass_checklist.md` *itself* catalogs these 23 (its §2/§3/§4) as do-not-commit scratch / belongs-elsewhere — consistent with leaving them in the stash. Only the checklist doc was committed (per user ruling); the other 23 remain in the stash, uncommitted.

## 3. Restored file list + §3 content spot-checks
17 files restored & staged = §1 (16) + `cowork_prune_pass_checklist.md` (1). Spot-checks:
- `cowork_bounded_context_design.md` — "increment size" present (line 64); requester-owned-increment concept present ("chosen by the requesting" L64, "the requester owns the extend → re-infer → re-check loop" L70). ✓
- `cowork_layer4_chordsymbol_design.md` — "stepwise structure decides" ×1 ✓; header "SIGNED (user, 2026-06-24)" ×1 ✓.
- `CLAUDE.md` — "Cross-layer-budget caveat" ×1 ✓.
- `cowork_layer3_keymode_design.md` — "Architectural Layer 5" ×14 ✓; circle-of-fifths change-cost qualification ×2 ✓.
- No file failed to restore cleanly; no conflicts.

## 4. Commit (§4) — local only, unpushed
- **Hash:** `ccc5e78096672434ec0b40d67537422a03452253`
- **Parent:** `b57dbfa7a8` (the backout) — clean linear add.
- **Subject:** `docs(cowork): restore design + architecture work swept by the Stage-0 stash — L4 rewrite, bounded-context model, L1–L3 stabilization plan, L1 extend design, spec amendments + reviews (version-controlled to prevent WIP loss)`
- **`git show --stat`:** 17 files changed, 2628 insertions(+), 39 deletions(-) — exactly the §1 set + prune checklist; **zero §2 files**. (10 `create mode` = the 10 restored untracked docs; 7 modified = the tracked docs.)
- Not pushed. `origin` held; `upstream` never.

## 5. Post-conditions
- **Stash retained:** `git stash list` still shows `stash@{0}` (`bc4fa79c4a…`, "foundation WIP — preserved for Stage-2 hunk-by-hunk triage"). ✓
- **§2 set untouched:** no §2 path in the commit or working tree; all remain in the stash for Stage-2 triage. ✓
- **Working tree clean** after commit (no §2 leak). ✓
- No stop condition tripped during the restore (the only §6 surprise — the 24 unlisted untracked paths — was surfaced to the user and resolved before any action).

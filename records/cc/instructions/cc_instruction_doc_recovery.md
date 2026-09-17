# CC Instruction — recover Cowork's swept documentation work from the Stage-0 stash (then commit it)

> **What happened.** Stage 0's `git stash push -u` (stash `bc4fa79c4a9ef4401794b321dfec81fa54bae78e`) swept up not only
> the code WIP but **all of Cowork's uncommitted documentation work this session** — the new `cowork_*.md` design
> docs (untracked → removed from the tree) and Cowork's edits to several tracked docs (reverted to HEAD). User has
> approved **restoring and committing** that doc work. This recovers it and version-controls it so it can never be
> swept again.
>
> **Critical safety:** the stash is currently the **only** copy of the new untracked docs **and** of the code WIP that
> Stage 2 will triage. **Do NOT `git stash pop` or `git stash drop` — never drop the stash.** Use `apply`/`checkout`/
> `restore` that *retains* it. Restore **only the doc files below**; leave everything else in the stash.

## §0 — Inventory and safety
- Confirm the stash exists: `git stash list` shows `stash@{0}` = `bc4fa79c4a…`. Confirm HEAD == `b57dbfa7a8`
  (the backout). Tree should be clean.
- Enumerate the stash's full contents — tracked-modified **and** untracked (`-u`) — e.g.
  `git stash show -p stash@{0}` for tracked, and list the untracked portion (the `-u` third parent). Cross-check every
  stashed path against the two lists below. **If any stashed file is in neither list, STOP and report it** (a surprise
  we must classify before acting).

## §1 — RESTORE-AND-COMMIT set (Cowork's doc work — restore these to the tree)
**New design docs** (untracked in the stash — extract them from the stash's untracked portion to the working tree):
```
cowork_bounded_context_design.md
cowork_l1l3_stabilization_plan.md
cowork_layer1_extend_design.md
cowork_layer4_chordsymbol_design.md
cowork_uncertain_resolver_investigation.md
cowork_delta_check_dispositions.md
cowork_layer4_spec_review.md
cowork_spec_language_sweep.md
cowork_layer3_spec_language_sweep.md
```
**Edited tracked docs** (restore Cowork's stashed version — `git checkout stash@{0} -- <file>`; this re-applies the
edits onto the HEAD-version file; none of these conflict with the backout):
```
CLAUDE.md
cowork_layer1_note_model_design.md
cowork_layer2_slicing_design.md
cowork_layer3_keymode_design.md
cowork_target_architecture.md
cowork_design_doc_template.md
COWORK_HANDOFF.md
```

## §2 — LEAVE-IN-STASH set (do NOT restore — Stage-2 triage / not Cowork's)
Leave every one of these in the stash, untouched:
- **Code WIP:** `src/composing/analysis/chord/chordslicedecoder.{cpp,h}`,
  `src/composing/analysis/engravingbridge/regiontoneprimitives.cpp`,
  `src/composing/analysis/key/keymodeanalyzer.h`, `src/composing/analysis/key/keymodesequence.{cpp,h}`,
  `src/composing/analysis/section/localmodulationdetector.{cpp,h}`.
- **Tooling WIP:** `tools/batch_analyze.cpp` (its B2 hunks; **do not restore it** — the committed backout `b57dbfa7a8`
  already handled the tpc consumer, and the stash's copy still has the old consumer + B2 hunks; Stage 2 triages it),
  `tools/cc_layer3_keymode_baseline.py`, `tools/compare_rn.py`.
- **Pre-existing non-Cowork doc WIP (unknown provenance — triage later, do NOT commit blindly):** `STATUS.md`,
  `BUILD_AND_TEST.md`, `cowork_github_9444_comment_draft.md`, `docs/back_half_design.md`, `docs/decoder_design.md`.
- `cc_*` files are gitignored scratch — ignore them (not in the stash; already on disk).

## §3 — Verify the restore before committing (spot-check content)
Confirm the restored files are present and carry this session's content, e.g.:
- `grep -c "increment size" cowork_bounded_context_design.md` > 0 and it mentions the requester-owned increment;
- `grep -c "stepwise structure decides" cowork_layer4_chordsymbol_design.md` > 0 (the sharpened membership rule) and
  the header reads `SIGNED (user, 2026-06-24)`;
- `grep -c "Cross-layer-budget caveat" CLAUDE.md` > 0 (Cowork's edit restored);
- `cowork_layer3_keymode_design.md` mentions `Architectural Layer 5` for the resolver (the O1 name-collapse) and the
  circle-of-fifths change-cost qualification.
Report any file that does **not** restore cleanly.

## §4 — Commit (Cowork doc work, local-only)
- `git add` **exactly** the §1 list (the new docs + the restored tracked docs). Confirm `git status` shows **only**
  those staged and the §2 set still absent/untracked-in-stash.
- Commit: `docs(cowork): restore design + architecture work swept by the Stage-0 stash — L4 rewrite, bounded-context model, L1–L3 stabilization plan, L1 extend design, spec amendments + reviews (version-controlled to prevent WIP loss)`.
- **Local only, unpushed.** `origin` held; `upstream` never.

## §5 — Deliverable
`cc_doc_recovery_report.md` (gitignored): the stash-contents enumeration + the cross-check (any unlisted file
flagged); the restored file list with the §3 spot-checks; the commit hash + `git show --stat` of it (so Cowork can
verify it contains **only** the §1 docs); confirmation the **stash is retained** (`git stash list` still shows
`bc4fa79c4a…`) and the §2 set is untouched.

## §6 — Stop conditions
- The stash would be dropped/popped, or any §2 (code/tooling/pre-existing-doc) file gets restored or committed → STOP.
- A stashed path is in neither §1 nor §2 → STOP and report (classify first).
- Any restore conflicts → STOP and report (do not force).
- A push would target `origin`/`upstream` → STOP (local commit only here).

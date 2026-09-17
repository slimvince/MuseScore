# CC INSTRUCTION — docs(cowork) fold commit after the VL foundation landing + SHA statement (2026-07-03)

**Status: ACTIVE DISPATCH (the only open instruction). Small, docs-only. No build, no tests, no corpus regen —
nothing here touches code, so byte-identity holds by construction.**

## Context

The VL-A/B/C foundation build is landed, Cowork-verified, and ratified (STATUS session 22g). Your report
correctly left three Cowork narrative files uncommitted for the post-verification fold — that fold is this
dispatch. Your report also omitted the four build-commit SHAs, which blocks Cowork's object-level verification —
this dispatch closes that too.

## Task 1 — the fold commit

ONE commit, message prefix `docs(cowork):`, containing EXACTLY these three files and nothing else:

1. `STATUS.md` — carries the Cowork-written session-22f and 22g entries (already in the working tree; do not
   edit their content).
2. `COWORK_HANDOFF.md` — the updated header (already in the working tree; do not edit).
3. `cowork_polyphony_phrase_harmony_research.md` — the §6b targeted-sweep section (already in the working tree;
   do not edit).

Also fold INTO this same commit, force-added per the `/cc_*.md` convention (they are dispatch/verification
records referenced by the STATUS entries): `cc_instruction_vl_foundation_build.md`,
`cc_instruction_vl_docs_fold.md` (this file), and — if your build's `docs(cowork):` commit did not already carry
it — `cc_vl_foundation_build_report.md`. Do NOT add: the untracked measurement dumps
(`vl_discovery_out.txt`, `vl_orthogonality_out.txt`), `scratch_artifacts/`, or any `tools/corpus/` churn
(gitignored, stays untracked). If `git status` shows any OTHER modified/untracked file not named here, do not
bundle it — list it in your confirmation and leave it in place.

## Task 2 — the SHA statement (report defect close-out)

In your confirmation (a short reply or a ≤20-line addendum appended to `cc_vl_foundation_build_report.md`
BEFORE committing it, your choice), state:

- The **four build-commit SHAs** from the foundation build (module / tests / diagnostic+parity / docs), each
  with its one-line subject.
- The **fold-commit SHA** from Task 1.
- The output of `git status --porcelain` AFTER the fold commit (expect: only the deliberately-untracked files).

Remember the CLAUDE.md bash rules even for git commands (`; echo "exit:$?"`, no large output).

## Hard limits / STOP

Local only, no push, fork-only. Nothing under `src/`, `docs/`, `tools/` is touched. No file content edits —
this is a pure staging/commit act plus the SHA statement. STOP and report if: any of the three named files is
missing or unexpectedly conflicted; the spec `cowork_voiceleading_axis_design.md` shows as modified (it should
already be committed AS-BUILT by your build session); or anything else looks different from the tree state your
report described.

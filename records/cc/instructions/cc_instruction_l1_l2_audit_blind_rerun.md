# CC INSTRUCTION — L1/L2 audit: fully-blind re-run of the second reading and the error-rate measurement, plus two authorized documentation fixes — EG-7 / OI-84 / OI-89

> **Issued by Cowork, 2026-07-11.** Why this session exists: the previous pass-2 session
> declared honestly that its independent second reading was only PARTIALLY blind — the
> instruction it followed required reading `STATUS.md` at the start, and `STATUS.md`
> carried the first pass's headline verdict. The user therefore WITHHELD certification of
> layers 1 and 2 (register row OI-89; catalog row DT-20). This session repeats ONLY the
> two blinding-dependent measurements, fully blind this time, and applies two authorized
> one-line documentation fixes. Nothing else from pass 2 is repeated — the catalog sweep
> stands.
>
> **REMINDERS — the standing rules you work under (read `CLAUDE.md` in full; these are
> pointers, not replacements):**
> - Guiding principle 8: no inference-problem fixing until ALL refactoring, architectural
>   design, and algorithmic completion are done. In this session you fix NOTHING except
>   the two documentation comments explicitly authorized in Task 4. Any other problem you
>   find — even an obvious bug — is recorded as a register row, never patched.
> - Guiding principle 7: any amendment belongs to the layer that owns the concern. (The
>   two authorized fixes are comment text only; they move no code between layers.)
> - Guiding principles 15 and 19: verify at the actual code and data, never at someone's
>   assertion — including your own earlier sessions' assertions.
> - The conventions: no self-invented labels, abbreviations, numbering schemes, or jargon
>   — in your report, register rows, commit messages, everywhere. Use existing repository
>   names or plain words.
> - The self-check rule (new in `CLAUDE.md`, 2026-07-11): after EVERY coding exercise —
>   scripts and document edits included — and before reporting done, re-read the actual
>   diff of every file you touched and check it against the principles, the conventions,
>   and `DEFECT_TYPES.md`. Note: for you, this check against `DEFECT_TYPES.md` can only
>   happen AFTER the unblinding point in Task 2, since that file is withheld until then.
> - Shell rules: append `; echo "exit:$?"` to any command that may return non-zero;
>   redirect large output to a file.
> - Git rules: stage only your own files, named one by one; never `git add -A`. After any
>   commit, confirm with `git status` that disk matches the commit. The working tree may
>   carry the user's or Cowork's uncommitted edits — leave them untouched.
> - Push rules: `origin` (the user's fork) only. Never `upstream` — the standing hard
>   stop. Verify with `git remote -v` before any push.
>
> **⚠ WITHHELD READS — the whole point of this session.** Do NOT open ANY of the
> following until Task 1 is finished and committed: `STATUS.md`, `OPEN_ITEMS.md`,
> `DEFECT_TYPES.md`, `cowork_handoff.md`, `cc_l1l2_audit_pass1_report.md`,
> `cc_l1l2_audit_pass2_report.md`, `tools/audit/l1l2/pass1_dispositions.csv/.json`,
> `tools/audit/l1l2/pass2_blind_sample.csv/.json`,
> `tools/audit/l1l2/pass2_errorrate_sample.csv/.json`, `tools/audit/l1l2/pass2_compare.txt`,
> `cowork_siloed_facts_audit.md`, `cowork_adjudication_dossier.md`. The deferral of the
> mandatory session-start `OPEN_ITEMS.md` read is deliberate, declared, and limited to
> Task 1 — it happens in Task 2 instead. In your report, state at which point you first
> opened each withheld file. Safe to read from the start: `CLAUDE.md`,
> `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, this instruction, the inventory tables
> named in Task 1, and the source code itself.

## Task 0 — Preconditions

0. **First action of the session — commit Cowork's waiting edits.** Cowork left finished
   edits in the working tree that must land as their own commit before your work starts
   (clean provenance). Stage EXACTLY these five files, named one by one, and commit —
   WITHOUT opening the two withheld ones among them (staging needs no reading; their
   content is Cowork's, already verified, and summarized for you in this instruction's
   preamble):
   ```
   git add CLAUDE.md OPEN_ITEMS.md DEFECT_TYPES.md cc_instruction_l1_l2_audit_blind_rerun.md cc_instruction_l1_l2_audit_pass2.md
   git commit -m "docs(cowork): L1/L2 certification withheld on partial blinding - OI-89 + DT-20 + the blind re-run instruction; CLAUDE.md conventions: no self-invented labels; the self-check after every coding exercise"
   ```
   Then `git status --short; echo "exit:$?"` — the only remaining working-tree entries
   should be the known OI-51 carry (`cowork_joint_key_chord_design.md`) and untracked
   scratch. Anything else: stop and report. If any of the five files has nothing to
   stage (already committed), say so in the report and continue.
1. Check the git state WITHOUT displaying commit messages — recent messages summarize the
   earlier passes' conclusions and would break your blinding. Use exactly:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor b5a9be9ac1 HEAD; echo "exit:$?"` (the second must print
   `exit:0`, meaning HEAD is at or after `b5a9be9ac1`). Do not run `git log` in any form
   until after the Task-1 commit.
2. Do not read the withheld files.

## Task 1 — The blind work (all judging happens here, before anything is unblinded)

Read only: the row inventory tables under `tools/audit/l1l2/` (`file_table.csv`,
`l1l2_functions.csv`, `l1l2_literals.csv`, `l1l2_branches.csv`, `l1l2_fields.csv`,
`l1l2_decls.csv`, `l1l2_crosslayer.csv`, `inventory.json`, `manifest.json`) and the source
code. NOT any verdict file.

1. Write a sampling script (commit it; no hand-picked rows; you may reuse
   `tools/audit/gen_pass2_sample.py` ONLY by reading its code, not its outputs). Draw TWO
   samples with NEW fixed seeds, both seeds recorded in the artifacts and different from
   `20260711`:
   - at least 110 rows, spread across the five row kinds in proportion to their counts,
     every layer-1/layer-2 file represented — the independent second reading;
   - 40 rows, uniformly random — the error-rate sample.
2. Judge EVERY sampled row from the code itself, from scratch, using the fixed verdict
   vocabulary of `cowork_audit_protocol.md` (step P2) and its four standing questions
   (what does the row assume? what does it publish? who consumes it? what happens at its
   edge cases?). Work in the random order the script produced. Record your own verdict
   per row for BOTH samples — for the 40-row sample too, you judge first and compare
   later; you do not yet know what the first pass said.
3. Write `tools/audit/l1l2/blind_rerun_reading.csv/.json` (the 110+) and
   `tools/audit/l1l2/blind_rerun_errorrate.csv/.json` (the 40), and commit script +
   artifacts as ONE commit with a `feat(tools):` message. Record the hash. THIS commit is
   the unblinding point — after it, the withheld list is lifted.

## Task 2 — Unblind, compare, diagnose

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read — pay
   attention to OI-88 and OI-89), `DEFECT_TYPES.md`, `STATUS.md`, both pass reports, and
   the first pass's verdict files.
2. Compare your 110+ verdicts against the first pass's on the same rows; classify every
   disagreement (substantive miss / wording difference / judgment tie) and diagnose which
   protocol step let each substantive one through. Treat every substantive disagreement
   as a stop-and-diagnose case before proceeding.
3. Compare your 40 blind verdicts against the first pass's on the same rows. The
   disagreement fraction IS the audit's measured error rate — this time produced by a
   reader who did not know the first pass's conclusions when judging. Report the number
   and list any failing rows. If a failure implies a whole class of rows was judged
   wrongly, say so plainly — that class must be re-examined, not averaged away.

## Task 3 — Compare with the superseded partially-blind results

Diff your two artifacts against the earlier `pass2_blind_sample.*` and
`pass2_errorrate_sample.*` conclusions at the aggregate level: did full blinding change
the picture (flag rates, error rate, the kinds of things flagged)? One honest paragraph
in the report — this answers the user's question "did the leak matter?" with measurement
instead of opinion.

## Task 4 — The two authorized documentation fixes (the ONLY fixes permitted)

Authorized by the user 2026-07-11, from register row OI-88; both are comment text only,
no code change, no behavior change:

1. `src/composing/analysis/slicing/slicer.h` line 68: the anchor
   `regionanalyzer.cpp:579` is stale — the decoder calls are at
   `regionanalyzer.cpp:634` and `:705`. Correct the anchor (cite both call sites, or
   reword so the anchor cannot silently drift again).
2. `src/composing/analysis/notemodel/note_model.h` lines 161–163: the docstring claims
   "no layer calls it yet". Wrong as worded — gated production call sites exist at
   `regionanalyzer.cpp:702`, `chordslicedecoder.cpp:1387/1393`,
   `textureclassifier.cpp:183/187`, all off by default. Reword to say exactly that (the
   capability is dormant in substance, its callers gated off), keeping the Phase 1a/1b
   explanation intact.

Verify both fixed comments against the code (the line numbers above are Cowork-verified
2026-07-11, but verify again yourself — they may have moved). Commit the two files as one
commit. These are comment-only edits; state in the report that no compiled behavior can
change, and apply the self-check rule to the diff.

## Task 5 — Report, register, push

1. Write `cc_l1l2_audit_blind_rerun_report.md`: seeds and sample designs; when each
   withheld file was first opened; the comparison tables with per-disagreement diagnoses;
   the error rate; the did-the-leak-matter paragraph; the state of the two doc fixes; and
   your certification proposal — propose certifying layers 1 and 2 only if this fully
   blind re-run supports it; otherwise propose withholding, with the concrete reason. You
   only propose; Cowork verifies at the code; the user decides. Write the status as
   "proposed, awaiting the user's decision".
2. Register updates in the SAME commit as the report: flip OI-88 (the doc fixes) to
   resolved with provenance; update OI-89's status to reflect the re-run's outcome (leave
   the certification decision itself to the user); add rows for anything new you found.
   Update `STATUS.md` (prepend) and the entry block of `cowork_handoff.md`. Plain
   language everywhere.
3. Commits: the Task-1 `feat(tools):` freeze; the Task-4 doc-fix commit; one `docs(cc):`
   fold. Each revertible on its own; stage only your own files.
4. Run the self-check (the new `CLAUDE.md` section) over every diff before reporting.
5. **Push — authorized by the user 2026-07-11:** push all local commits to `origin`
   only. Verify `upstream` push is still disabled first; anything that would touch
   `upstream` is the standing hard stop — stop and report instead. Confirm in the
   report: the pushed hash, `upstream` untouched.

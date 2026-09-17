# CC INSTRUCTION — The key-grading re-baseline: arithmetic correction of the 12 transposed scores + the dual local/home key columns — OI-142 / OI-143

> **Issued by Cowork, 2026-07-12.** The user decided both measurement corrections
> (register rows OI-142 and OI-143); this session executes them as ONE re-baseline
> event under the standing ritual, and PAUSES for the user's ratification of the new
> baseline figures before the reference commit lands. This is measurement-layer work
> ONLY: no `src/` change of any kind, no constant tuned, no corpus file and no
> ground-truth file edited, no golden refresh. The two changes:
> 1. **OI-142, arithmetic correction:** the grading applies each transposed piece's
>    constant offset to the ground truth for the 12 documented stems, so those pieces
>    grade against what their edition actually contains. No file edited — the offsets
>    live in ONE committed data file and are applied at the shared ground-truth
>    loading substrate, so EVERY consumer (the regression-stop instrument, the batch
>    diagnostic, the probe harness, the diagnosis classifier) sees the same corrected
>    view through the one path.
> 2. **OI-143, the dual key columns:** everywhere the key-agreement column appears,
>    it becomes TWO columns — against the DCML global (home) key as today, and
>    against the DCML LOCAL key — both computed, both reported, nothing dropped.
>
> **Read first:** `OPEN_ITEMS.md` (rows OI-141/OI-142/OI-143 carry the decisions and
> the 12 stems with offsets), `CLAUDE.md` in full (the gate-policy blocks you will be
> re-stamping — read them as the contract), `cc_key_mode_inference_diagnosis_report.md`
> §5 (the transposition evidence), `tools/REPRODUCIBILITY.md`, `BUILD_AND_TEST.md`.
> Open-book session; surprises are findings except in your own tooling.
>
> **REMINDERS:** the ritual is the law here — outgoing reference snapshotted FIRST
> (the O-12 discipline), every run-level diff explained, the manifest re-stamped, and
> the new figures RATIFIED BY THE USER before the reference commit (guiding
> principles 14 and 16); no self-invented labels or jargon; the self-check over every
> diff before reporting done; shell rules (`; echo "exit:$?"`, redirect large
> output); git rules (stage only your own files by name, never `git add -A`,
> `git status` after every commit; the known carry `cowork_joint_key_chord_design.md`
> stays unstaged; `cc_*.md` force-added); push to `origin` only, never `upstream` —
> the standing hard stop, `git remote -v` first.

## Task 0 — Preconditions and the register commit

0. **Commit Cowork's waiting register edits** (the user's OI-142/OI-143 decisions,
   the OI-141 research direction, and this instruction):
   ```
   git add OPEN_ITEMS.md
   git add -f cc_instruction_key_grading_rebaseline.md
   git commit -m "docs(cowork): OI-142 arithmetic correction + OI-143 dual local/home key grading DECIDED (user 2026-07-12) + OI-141 research direction (drift first; leading-tone/cadence second) + the re-baseline instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining: the known carry plus
   untracked scratch only; anything else, stop and report.
1. `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor a7312b8591 HEAD; echo "exit:$?"` — the second must
   print `exit:0`.

## Task 1 — Snapshot the outgoing reference (before anything else changes)

Snapshot the current `tools/robust_stop/` reference in the committed form the O-12
discipline expects (the pattern used at the earlier re-baseline: the outgoing
enumerations and summary preserved under a dated snapshot path or the established
frozen-history mechanism — follow the existing precedent in that directory, do not
invent a new shape). Commit the snapshot as its own commit BEFORE any instrument
change.

## Task 2 — The offsets file and the substrate change

1. Create ONE committed data file (beside the reference, e.g. under
   `tools/robust_stop/`) holding the 12 stems and their offsets exactly as recorded
   in register row OI-142, each entry carrying provenance (the diagnosis report) and
   the detection rule reference. Before trusting them: RE-VERIFY each offset
   independently at the artifacts (the modal-offset signature over the committed
   corpus versus the ground truth — the stated reproducible rule), and record the
   verification per stem. A stem whose offset does not re-verify is a STOP.
2. Apply the offsets at the SHARED ground-truth loading substrate (the one loading
   path all instruments import), so a corrected piece grades identically everywhere.
   No consumer-side special-casing anywhere.
3. Add the LOCAL-key grading beside the global everywhere the key column exists:
   the regression-stop instrument's summary, its diff tool's report, the batch
   diagnostic where applicable, and the probe/classifier outputs. Both columns
   named plainly (key-agree against the home key; key-agree against the local key).

## Task 3 — Re-run, and explain everything that moved

1. Run the regression-stop instrument to a candidate output and the diff against
   the snapshotted reference. EXPECTATIONS to check, not assume: the run-level
   set-diff should be REMOVALS concentrated on the 12 corrected stems (their
   false root-fails dissolving); the other 314 stems must be BYTE-IDENTICAL in
   their grids (the offsets file must not touch them — prove it, don't assert it).
   ANY added run, and any change on a non-corrected stem, is a STOP-and-explain
   before proceeding.
2. Produce the proposed NEW baselines, all columns, all three presets: root-agree,
   RN-agree, key-agree-home, key-agree-local — with the per-stem before/after for
   the 12 corrected pieces, and the explained per-run diff.
3. Re-run the batch diagnostic (`characterise_bir_false.py`) and record its new
   case counts as the updated diagnostic numbers (it is not the gate; its shift is
   expected and reported, with the affected cases listed).
4. No `src/` was touched, so the test suites are unaffected; state that in the
   report rather than assuming silently — run the composing suite once as the
   cheap sanity check.

## Task 4 — PAUSE: the user ratifies before the reference lands

Present to the user (via your question tool), with full context in the question
itself: the old and proposed-new figures side by side (all columns, all presets),
the size and shape of the run-diff (removals on the 12, nothing else), and the
per-stem verification summary. DO NOT commit the new reference, the manifest
re-stamp, or the `CLAUDE.md` baseline text until the user approves. If the user
declines or redirects, stop and report.

## Task 5 — On ratification: land it as one revertible adoption commit + fold

1. The adoption commit: the new `tools/robust_stop/` reference artifacts +
   re-stamped `manifest.json` (corpus hash, instrument provenance, the offsets file
   hash) + the updated `CLAUDE.md` gate-block text (the ratified-baselines
   paragraphs updated with the new figures, both key columns, and a provenance line
   naming this event, the report, and the user's ratification date; the two-tier
   class policy text unchanged).
2. The `docs(cc):` fold: `cc_key_grading_rebaseline_report.md` (the snapshot hash;
   the per-stem verifications; the diff explained; the old/new figure table; the
   ratification record; when anything surprising appeared, what it was); register
   updates in the SAME commit — close OI-142 and OI-143 with the landing hashes;
   note at OI-141 that the drift research now grades against honest columns; any
   new discovery gets its own row. Update `STATUS.md` (prepend) and the entry block
   of `cowork_handoff.md`. Plain language everywhere.
3. Run the self-check over every diff. **Push — user-authorized 2026-07-12:** all
   local commits to `origin` only, after `git remote -v` confirms `upstream` push
   is still disabled; anything that would touch `upstream` is the standing hard
   stop. Confirm in the report: the pushed hash, `upstream` untouched.

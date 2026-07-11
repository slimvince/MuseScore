# CC INSTRUCTION — Layer-3 audit: re-derive the fine verdict labels from the FROZEN blind prose — EG-7 / OI-84 / OI-100

> **Issued by Cowork, 2026-07-11.** Why this session exists: the layer-3 second reading
> (pass 2) judged its 156 blind rows with a deliberately coarse four-label vocabulary
> instead of the audit protocol's full verdict set, and defended the deviation with the
> claim that "the per-row prose carries the finer distinctions." That claim is checkable
> but unchecked, and the user directed that it be CHECKED before the layer-3
> certification is decided (register row OI-100). The blinding of that reading HELD and
> its verdicts were frozen and committed before unblinding, so the evidence exists in
> untainted form. Your job: derive the fine labels from that frozen prose ALONE, and
> measure how far the prose actually carries.
>
> **The one rule that makes this session meaningful: the frozen prose is your ONLY
> evidence.** You are establishing what the frozen reading contains — not performing a
> new reading. Do NOT open any source code file, do NOT consult
> `tools/param_manifest.json`, do NOT re-measure anything. If a row's prose (plus its
> coarse label and row identity) does not decide the fine label, the answer for that row
> is UNRESOLVABLE-FROM-PROSE with one sentence why — that outcome is not a failure, it
> is exactly the measurement the user asked for.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix nothing (guiding
> principle 8) and amend nothing — this is a measurement session; verify at the actual
> artifacts, never at assertion (principles 15 and 19); no self-invented labels,
> abbreviations, numbering schemes, or jargon anywhere (the conventions — the verdict
> vocabulary you emit is the protocol's, plus the single plain phrase
> "unresolvable from prose"); run the self-check over every diff before reporting done;
> shell rules (`; echo "exit:$?"`, redirect large output); git rules (stage only your own
> files by name, never `git add -A`, `git status` after every commit; the known working-tree
> carry `cowork_joint_key_chord_design.md` stays untouched; `cc_*.md` files are gitignored
> — force-add this instruction file in your final commit); push to `origin` (the fork)
> ONLY, never `upstream` — the standing hard stop, verify with `git remote -v` first.
>
> **⚠ WITHHELD READS — do NOT open until your Task-2 freeze commit exists:**
> `tools/audit/l3/pass1_dispositions.csv/.json`, `cc_l3_audit_pass2_report.md` (it
> contains the crosstab and diagnoses that would anchor you), every other
> `cc_*_report.md`, `OPEN_ITEMS.md`, `DEFECT_TYPES.md`, `STATUS.md`,
> `cowork_handoff.md`, `tools/audit/l3/sweep_results.json/.txt`, and
> `tools/audit/l3/firerate.json`. The mandatory session-start `OPEN_ITEMS.md` read is
> deferred to Task 3 — declared here for the user; Cowork performed the register check
> for this dispatch. Declare in your report when each withheld file was first opened.
> Safe reads from the start: `CLAUDE.md`, `cowork_audit_protocol.md` (its step P2
> defines the fine vocabulary you emit), this instruction, and the two frozen artifacts:
> `tools/audit/l3/pass2_blind_reading.csv/.json` and
> `tools/audit/l3/pass2_blind_errorrate.csv/.json`.
>
> **Scope declaration:** READ-ONLY measurement. No `src/` read, no production change, no
> constant tuned, no golden refreshed, `tools/robust_stop/` and `tools/corpus/`
> untouched.

## Task 0 — Preconditions

0. **First action — commit Cowork's waiting edits** (content is Cowork's, summarized in
   this preamble: the register row OI-100 recording the deviation and this remedy, plus
   this instruction file). Stage WITHOUT opening the register:
   ```
   git add OPEN_ITEMS.md
   git add -f cc_instruction_l3_audit_pass2_relabel.md
   git commit -m "docs(cowork): OI-100 - the L3 pass-2 vocabulary deviation and its user-directed remedy (fine-label re-derivation from the frozen blind prose)"
   ```
   Then `git status --short; echo "exit:$?"` — remaining entries: the known carry plus
   untracked scratch only; anything else, stop and report.
1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor aa43ef4a21 HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-2 freeze.
2. Do not read the withheld files. Do not open any file under `src/`.

## Task 1 — Re-derive the fine labels, blind to pass 1

For EVERY row of both frozen artifacts (the 116-row reading and the 40-row error
sample): from the row's identity (kind, file, line, identifier), its coarse label, and
its prose reasoning — and NOTHING else — derive the protocol's fine verdict:

- rows that are causal premises: FACT / THEORY / ASSUMPTION;
- rows that are derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED (with declared
  dormancy noted where the prose names a future consumer);
- rows that are numeric literals or constants: ESTABLISHED / UNFIT / DEAD;
- rows that are code: RETIRES / SURVIVES;
- any row whose prose does not decide the fine label: UNRESOLVABLE-FROM-PROSE, one
  sentence why (for example: "prose argues theory-correctness but never engages fit
  provenance, which is what separates ESTABLISHED from UNFIT").

Record per row: the derived fine label, one sentence of justification quoting or
paraphrasing the prose, and a yes/no field "prose decided it". Work in the artifact's
stored order. Write `tools/audit/l3/pass2_fine_relabel_reading.csv/.json` and
`tools/audit/l3/pass2_fine_relabel_errorrate.csv/.json`, generated by a committed
script where mechanical (parsing, joining, counting) and by recorded judgment where not
— never hand-edit a generated artifact.

## Task 2 — Freeze

Commit the relabel artifacts + any script as ONE `feat(tools):` commit; record the hash
in the report. THIS commit lifts the withheld list.

## Task 3 — Unblind, crosstab, conclude

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read — the
   relevant rows are OI-90 through OI-100), `cc_l3_audit_pass2_report.md`, and
   `tools/audit/l3/pass1_dispositions.csv/.json`.
2. Crosstab your fine labels against pass 1's on the same rows. Every row lands in
   exactly one bucket:
   - CONCORDANT — the fine label matches pass 1;
   - GENUINE DISAGREEMENT — the prose decided a fine label and it contradicts pass 1;
     each one is a stop-and-diagnose case (which protocol step let it through, in
     whichever pass was wrong);
   - UNRESOLVABLE-FROM-PROSE — the frozen reading does not reach this row's fine axis.
3. Report the three counts per sample, and per fine axis (the constants axis
   ESTABLISHED-versus-UNFIT separately — it is the axis the coarse vocabulary most
   plausibly collapsed, and the axis on which the mechanical manifest sweep provides
   independent coverage; say explicitly whether every unresolvable constant row is
   covered by that sweep).
4. **Updated certification statement — propose, never grant:** taking pass 1, the
   pass-2 sweep, the blind reading, and this re-derivation together, state whether the
   layer-3 certification proposal still stands, weakened only by named, bounded gaps —
   or does not. Write "proposed, awaiting the user's decision"; leave OI-84 and the
   entry-gate condition open.

## Task 4 — Report, register, push

1. `cc_l3_audit_pass2_relabel_report.md`: when each withheld file was first opened; the
   per-row artifact locations; the crosstab with the three buckets per sample; every
   genuine disagreement with its diagnosis; the constants-axis statement; the updated
   certification statement.
2. Register discipline in the SAME commit: update OI-100 with the measured outcome
   (leave the certification decision to the user); new rows for any genuine
   disagreement that survives diagnosis as a real defect; reference existing rows
   rather than duplicating. Update `STATUS.md` (prepend) and the entry block of
   `cowork_handoff.md`. Plain language everywhere.
3. Commits: the Task-0 commit, the Task-2 `feat(tools):` freeze, one `docs(cc):` fold
   (force-add this instruction). Run the self-check over every diff before reporting
   done.
4. **Push — authorized by the user, 2026-07-11:** all local commits to `origin` only,
   after `git remote -v` confirms `upstream` push is still disabled; anything that
   would touch `upstream` is the standing hard stop. Confirm in the report: the pushed
   hash, `upstream` untouched.

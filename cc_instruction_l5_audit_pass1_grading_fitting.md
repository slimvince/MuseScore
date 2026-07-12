# CC INSTRUCTION — Layer-5 audit, first pass, session 2b: the grading and fitting instruments — EG-7 / OI-84 / OI-116

> **Issued by Cowork, 2026-07-12.** The instruments population split (user-ratified at
> the session-2a feasibility stop) put the regression-stop core first — done, 954 rows,
> the stop reproducing clean at head. THIS session completes the instruments: the
> GRADING + FITTING population (6 files / 733 rows per the committed subsplit in the
> layer-5 partition artifact). One session remains after it (the shared harness), then
> the whole-scope second pass. Certification is NOT decided here.
>
> **Scope definition — from the committed artifacts, not memory:** every deep
> inventory row whose file is in the grading+fitting half of the instruments subsplit
> recorded in the partition artifact under `tools/audit/l5/`. A tag that looks wrong at
> the code is a finding; record it and proceed with the corrected scope, stating both.
>
> **The establishment question governs, same as session 2a:** per instrument — what
> does it CLAIM to measure or grade; what positively establishes that (oracle
> cross-check, derivation of the unit, reproduce-check) and where is that RECORDED;
> what is stamped and what is not; which failures pass SILENTLY. Grading instruments
> deserve one extra edge: their tolerances, bucket boundaries, and tie-breaking
> conventions ARE measurement decisions — per such value, where does it come from, and
> what would change if it moved? A grading convention nobody ratified is an assumption
> carrying load.
>
> **⚠ Read-only running rule (same sharp edge as 2a):** running instruments is wanted;
> reading the committed references (`tools/corpus/`, `tools/robust_stop/`, committed
> report artifacts) is fine; WRITING goes only to scratch output directories. Never
> regenerate into the committed reference locations. An instrument that cannot run
> without touching them is a finding, not a run. Long runs: let them finish; never
> kill one; no subset substitutes.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING —
> findings become register rows, never patches (guiding principle 8); you are an
> auditor, not an amender (principle 7); verify at the actual code and data, never at
> assertion (principles 15 and 19); no self-invented labels, abbreviations, numbering
> schemes, or jargon anywhere — plain-language finding slugs, the convention the 2a
> self-check settled; run the self-check over every diff before reporting done (the
> catalog part only after the freeze); shell rules (`; echo "exit:$?"`, redirect large
> output to a file); git rules (stage only your own files by name, never
> `git add -A`, `git status` after every commit — the register row OI-85 convention;
> the known working-tree carry `cowork_joint_key_chord_design.md` stays untouched;
> `cc_*.md` is gitignored — force-add this instruction in your final commit); push to
> `origin` (the user's fork) ONLY, never `upstream` — the standing hard stop,
> `git remote -v` first.
>
> **⚠ WITHHELD READS (blind first pass, the DT-20 discipline):** do NOT open until
> your Task-3 freeze commit exists: `DEFECT_TYPES.md`, `OPEN_ITEMS.md`, `STATUS.md`,
> `cowork_handoff.md`, every `cc_*_report.md`, `cowork_siloed_facts_audit.md`,
> `cowork_adjudication_dossier.md`, `cowork_structural_integrity_audit.md`,
> `cowork_l1_l5_premise_debt_audit.md`, `cowork_layer5_engagement_design.md`,
> `cowork_layer5_function_design.md`, `cowork_joint_key_chord_design.md` (also the
> working-tree carry — do not read or touch it), `cowork_fb_redesign_design.md`,
> `cowork_gate_policy_amendment.md`, `cowork_premise_gate_reflection.md`,
> `cowork_engage_arc_plan.md`, `cowork_stage5_fitter_design.md`,
> `cowork_uncertain_resolver_investigation.md`,
> `cowork_functional_analysis_research_grounding.md`; and under `tools/audit/` every
> `*dispositions*`, `*blind*`, `*errorrate*`, `*relabel*`, `*compare*`,
> `sweep_results*`, `firecount*`, and `firerate*` file, plus the verdict-embodying
> `gen_*_dispositions*` scripts and `gen_signature_sweep.py` (if any of their own rows
> fall in this scope, judge them in a marked post-freeze section, same as 2a). The
> mandatory session-start `OPEN_ITEMS.md` read is deferred to Task 4 — declared here
> for the user; Cowork performed the register check for this dispatch. Declare in the
> report when each withheld file was first opened. Safe reads from the start:
> `CLAUDE.md` (its gate-policy and secondary-metric blocks are these instruments'
> contract where they are named there), `cowork_audit_protocol.md`,
> `BUILD_AND_TEST.md` (it documents the grading tools' commands), `ARCHITECTURE.md`,
> the roadmap, `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md`, the corpus
> registries, `tools/param_manifest.json` (in scope — data, not verdicts), the
> committed references under `tools/corpus/` and `tools/robust_stop/` (read freely,
> write never), the raw inventory tables and `manifest.json` under `tools/audit/l5/`
> (scope, not verdicts), `cc_instruction_l5_audit_pass1.md` and
> `cc_instruction_l5_audit_pass1_instruments.md` (the parent instructions, for
> definitions), and the instrument source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/` written
> to by NOTHING this session. A surprise in the audited instruments is a finding; a
> surprise in your own tooling is a stop — fix the tool, restamp, rerun, never
> hand-edit a generated artifact.

## Task 0 — Preconditions

1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor a64c5622fb HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-3 freeze.
2. Do not read the withheld files.
3. Cross-check the row count for this scope against the inventory (~733). If
   every-row rigor cannot honestly fit, STOP at the counts and propose a further
   split — never silently sample, never thin the verdicts.

## Task 1 — Dispositions for every row in scope (protocol P2 + P3)

EVERY row a closed-set verdict at full vocabulary resolution, with the establishment
answers in the row notes (claim / establishment record / stamping / silent-failure
modes). Attend particularly to:

- grading tolerances, bucket boundaries, alignment windows, and tie-breaks — each is
  a measurement decision: provenance or ASSUMPTION, stated per value;
- any place a grading convention differs between instruments that grade the same
  thing (one concern, one path — a divergence is a finding);
- the fit manifest's own integrity as data: does anything validate its sites,
  values, and consuming-path notes against the code, or can it drift silently?
- figures that travel from these instruments into documents: generated artifact or
  hand-transcription (the hand-transcription rule)?
- silent-failure paths: empty inputs, missing files, unmatched stems, partial
  coverage folded into the wrong bucket, exceptions swallowed broadly.

**The contract direction is mandatory (protocol P3):** from `CLAUDE.md`'s blocks that
name these instruments, `BUILD_AND_TEST.md`, `tools/REPRODUCIBILITY.md`, and
`docs/score_inventory.md`: enumerate every documented guarantee and command contract
and locate the code that delivers it — or flag it as prose enforced by nothing (the
2a first-rank shape).

## Task 2 — Behavioral characterization (protocol P4): run them

Each runnable instrument: run it READ-ONLY (scratch output) against the committed
references and record whether it reproduces its documented or committed results, and
which branches the run exercised. An instrument with no committed reference to
reproduce against is flagged as unestablished-by-construction — that is a finding,
not a shrug. Long runs: let them finish.

## Task 3 — Freeze (the blinding boundary)

Write `tools/audit/l5/pass1_dispositions_grading_fitting.csv/.json` plus the report
draft; commit as one `feat(tools):`; record the hash. THIS commit lifts the withheld
list. Any in-scope audit-tooling rows: marked post-freeze section, second commit,
split declared in the report.

## Task 4 — Unblind, reconcile, report, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read —
   the instrument-layer rows and the 2a findings are the near neighbors; converge or
   diverge explicitly), `DEFECT_TYPES.md`, `STATUS.md`,
   `cc_l5_audit_pass1_report.md`, and `cc_l5_audit_pass1_instruments_report.md`.
2. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. The whole-scope signature sweep is NOT run here — second pass.
3. `cc_l5_audit_pass1_grading_fitting_report.md`: disposition summary per verdict
   class; EVERY flagged row with file, line, one plain-language sentence; the
   per-instrument establishment table; the contract-check results with every
   unenforced guarantee named; reproduce-check results; the blind/post-freeze split
   if any; when each withheld file was first opened. Register discipline: every
   discovered issue gets its `OPEN_ITEMS.md` row in the SAME commit as the report;
   update OI-116 (instruments population complete). Update `STATUS.md` (prepend) and
   the entry block of `cowork_handoff.md`. Plain language everywhere.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-12):** the freeze commit, any
   post-freeze commit, one `docs(cc):` fold (force-add this instruction). Push all
   local commits to `origin` only, after `git remote -v` confirms `upstream` push is
   still disabled; anything that would send content toward `upstream` is the standing
   hard stop. Confirm in the report: the pushed hash, `upstream` untouched.

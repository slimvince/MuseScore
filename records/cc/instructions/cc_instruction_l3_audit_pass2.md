# CC INSTRUCTION — Layer-3 (key/mode) Certification Audit, PASS 2 (blind second reading + catalog sweep + measured error rate) — EG-7 / OI-84

> **Issued by Cowork, 2026-07-11.** The second and final pass of the layer-3 audit.
> Certification of layer 3 is decided after this pass — by the user, never here. The audit
> protocol is `cowork_audit_protocol.md`; this instruction carries out the independent
> second reading (step P5), the measured error rate (step P6), and the known-problem-type
> sweep (step P8, second run). It incorporates the two lessons already paid for: the
> second reading is FULLY blind (the L1/L2 second pass leaked through a required read —
> catalog row DT-20 — and had to be re-run), and the error-rate rows are judged blind
> FIRST, then compared.
>
> **REMINDERS — the standing rules you work under (read `CLAUDE.md` in full; these are
> pointers, not replacements):**
> - Guiding principle 8: no inference-problem fixing until ALL refactoring, architectural
>   design, and algorithmic completion are done. You fix NOTHING in this session. A
>   discovered violation — even an obvious bug — becomes a register row, never a patch.
> - Guiding principle 7: any amendment belongs to the layer that owns the concern; you
>   are an auditor here, not an amender.
> - Guiding principles 15 and 19: verify at the actual code and data, never at assertion
>   — including assertions in comments, docs, and earlier passes' artifacts.
> - The conventions: no self-invented labels, abbreviations, numbering schemes, or jargon
>   — anywhere. Use existing repository names or plain words. (The first pass caught
>   itself inventing a finding-numbering scheme in its self-check; do not repeat it.)
> - The self-check rule (`CLAUDE.md`, 2026-07-11): after every coding exercise — scripts
>   and document edits included — and before reporting done, re-read the actual diff of
>   every touched file and check it against the principles, the conventions, and the
>   catalog. The catalog part of the check happens only after your Task-1 freeze, since
>   `DEFECT_TYPES.md` is withheld until then.
> - Long-running measurements: never stop a running process without asking the user; no
>   subset substitutes for a full-corpus run (the first pass's recorded lesson).
> - Shell rules: append `; echo "exit:$?"` to any command that may return non-zero;
>   redirect large output to a file and read the file.
> - Git rules: stage only your own files, named one by one; never `git add -A`. After any
>   commit, confirm with `git status` that disk matches the commit (the register row
>   OI-85 convention). The working tree may carry the user's or Cowork's uncommitted
>   edits — known carry: `cowork_joint_key_chord_design.md` (register row OI-51); leave
>   them untouched. `cc_*.md` files are gitignored; tracked ones use the established
>   force-add (`git add -f`) convention — force-add THIS instruction file in your final
>   documentation commit.
> - Push rules: `origin` (the user's fork, `slimvince/MuseScore`) only. NEVER `upstream`
>   (`musescore/MuseScore`) — the standing hard stop. Verify with `git remote -v` first.
>
> **⚠ WITHHELD READS — do NOT open ANY of the following until your Task-1 freeze commit
> exists:** `STATUS.md`, `OPEN_ITEMS.md`, `DEFECT_TYPES.md`, `cowork_handoff.md`, every
> `cc_*_report.md`, `cowork_siloed_facts_audit.md`, `cowork_adjudication_dossier.md`,
> `tools/audit/l3/pass1_dispositions.csv/.json`, `tools/audit/l3/firerate.json` (pass-1
> measurement output — it flags mechanisms and would anchor you), everything under
> `tools/audit/l1l2/` except the raw inventory tables, and
> `tools/audit/gen_signature_sweep.py` together with `tools/audit/gen_dispositions.py`
> and `tools/audit/l3/gen_l3_dispositions.py` (their code embodies catalog signatures and
> verdict vocabulary applications). The mandatory session-start read of `OPEN_ITEMS.md`
> is deferred to Task 2 — deliberate, declared here for the user; Cowork performed the
> session-start register check for this dispatch (no open register row gates this pass).
> Declare in your report when each withheld file was first opened. Safe reads from the
> start: `CLAUDE.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`,
> the roadmap, the layer-3 inventory tables (`tools/audit/l3/file_table.csv`,
> `l3_functions.csv`, `l3_literals.csv`, `l3_branches.csv`, `l3_decls.csv`,
> `l3_fields.csv`, `l3_crosslayer.csv`, `inventory.json`, `manifest.json`), the sampling
> script `tools/audit/gen_pass2_sample.py` or `gen_blind_rerun_sample.py` (code only, to
> adapt), and the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/` reference
> artifacts untouched. A surprise in the audited code is a finding to record; a surprise
> in your own tooling is a stop — fix the tool, restamp, rerun, never hand-edit a
> generated artifact.

## Task 0 — Preconditions

1. Check the git state WITHOUT displaying commit messages (recent messages summarize
   pass-1 findings): `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 310750b2f8 HEAD; echo "exit:$?"` — the second must
   print `exit:0`. Do not run `git log` in any form until after the Task-1 commit.
2. Do not read the withheld files.

## Task 1 — The blind work (all judging happens before anything is unblinded)

You are the independent second reader for layer 3. Your job is to find what the first
pass got wrong or missed; you succeed by disagreeing, not by confirming.

1. Adapt the existing sampling approach into a committed script (no hand-picked rows).
   Draw TWO samples from the layer-3 inventory (1943 rows), with NEW fixed seeds — both
   recorded in the artifacts, different from `20260712`/`20260713`:
   - at least 110 rows, spread across the five row kinds in proportion to their counts,
     every layer-3 file represented — the independent second reading;
   - 40 rows, uniformly random — the error-rate sample.
2. Judge EVERY sampled row from the code itself, from scratch, using the fixed verdict
   vocabulary of `cowork_audit_protocol.md` (step P2) and its four standing questions:
   what does the row assume, what does it publish, who consumes it, what happens at its
   edge cases. Verify at the code and data, in the random order the script produced.
   Record your own verdict per row for BOTH samples — the 40 error-rate rows too are
   judged now, before you know what the first pass said.
3. Write `tools/audit/l3/pass2_blind_reading.csv/.json` (the 110+) and
   `tools/audit/l3/pass2_blind_errorrate.csv/.json` (the 40); commit script + artifacts
   as ONE `feat(tools):` commit and record the hash. THIS commit lifts the withheld list.

## Task 2 — Unblind, compare, diagnose

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read — the
   layer-3 pass-1 rows are OI-90 through OI-95), `DEFECT_TYPES.md`, `STATUS.md`,
   `cc_l3_audit_pass1_report.md`, and `tools/audit/l3/pass1_dispositions.csv/.json`.
2. Compare your verdicts with the first pass's on the same rows, both samples. Classify
   every disagreement — substantive miss / wording or verdict-axis difference / judgment
   tie — and for every substantive one, diagnose which protocol step let it through
   before proceeding.
3. The disagreement fraction on the 40 blind-judged error-rate rows IS the audit's
   measured error rate. Report the number and list the failing rows. If a failure
   implies a whole class of rows was judged wrongly, say so plainly — that class must be
   re-examined, not averaged away.

## Task 3 — Sweep the whole layer with the full catalog

Apply every entry of `DEFECT_TYPES.md` — all twenty-one, including DT-20 and DT-21 —
across the ENTIRE layer-3 inventory. All 1943 rows, not a sample. This is the main
instance-finding work of the pass.

1. For the mechanical entries: extend `tools/audit/gen_signature_sweep.py` to take the
   layer as an argument (one instrument, the way `gen_inventory.py --layer` went — this
   also discharges the spirit of the register row OI-95 point (a) for the sweep tool; do
   NOT create a parallel sweep script). It writes a hit table per catalog entry under
   `tools/audit/l3/` and fails loudly if any mechanical rule could not run.
2. For the review entries: row-by-row against the inventory; per entry record rows
   checked and every hit.
3. Every hit: file and line, one plain-language sentence a reader who does not know the
   code can understand, and whether an existing register row already covers it (name the
   row) or it is new.
4. A NEW problem TYPE (a pattern, not an instance) gets its `DEFECT_TYPES.md` entry in
   the same commit as the report.

## Task 4 — Certification proposal

Propose certifying layer 3 only if: both passes are complete, the error rate is measured
on blind-first verdicts, every disagreement is diagnosed, and the sweep found no
untracked correctness defect. Otherwise propose withholding, naming concretely what
remains. You only PROPOSE — Cowork verifies your report against the code, and the user
decides. Write the status everywhere as "proposed, awaiting the user's decision"; do not
mark the audit plan (register row OI-84) or the entry-gate condition (EG-7) satisfied
yourself.

## Task 5 — Report, register, push

1. Write `cc_l3_audit_pass2_report.md`: sample designs and seeds; when each withheld
   file was first opened; the comparison tables with per-disagreement diagnoses; the
   error rate with its failing rows; the per-catalog-entry sweep results; the
   certification proposal and exactly what it rests on.
2. Register discipline in the SAME commit as the report: every new issue gets its own
   `OPEN_ITEMS.md` row (next free number); issues pass 1 already registered are
   referenced, not duplicated; new types get catalog rows. Update `STATUS.md` (prepend)
   and the entry block of `cowork_handoff.md`. Plain language everywhere.
3. Commits: the Task-1 `feat(tools):` freeze; a `feat(tools):` for the sweep extension
   if it is not sensibly part of the fold; then ONE `docs(cc):` fold (force-add this
   instruction file into it). Each revertible on its own; stage only your own files.
4. Run the self-check over every diff before reporting done.
5. **Push — authorized by the user, 2026-07-11:** push all local commits to `origin`
   only, after `git remote -v` confirms `upstream` push is still disabled. Anything that
   would send content toward `upstream` is the standing hard stop — stop and report
   instead. Confirm in the report: the pushed hash, `upstream` untouched.

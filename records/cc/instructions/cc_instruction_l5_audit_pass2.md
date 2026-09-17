# CC INSTRUCTION — Layer-5 + instruments Certification Audit, PASS 2 (blind second reading + catalog sweep + measured error rate) — EG-7 / OI-84 / OI-116 — the FINAL session of the certification plan

> **Issued by Cowork, 2026-07-12.** The layer-5 + instruments first pass is complete
> across all four populations: the dormant resolver (815 rows), the regression-stop
> core instruments (954), the grading + fitting instruments (733), and the shared
> harness (870) — 3,372 deep rows, all verdicted, in the four `pass1_dispositions_*`
> artifacts under `tools/audit/l5/`. This is the second and final pass, and the final
> session of the whole dependency-ordered certification plan. The certification
> decision follows it — made by the user, never here.
>
> **The three paid-for lessons, baked in:** FULL blinding until your verdicts are
> frozen and committed; the error-rate rows judged blind FIRST, then compared; the
> FULL protocol P2 verdict vocabulary at full resolution from the start — a coarser
> vocabulary is a deviation that triggers a re-derivation remedy.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING beyond
> the one authorized deletion in Task 0 — findings become register rows, never patches
> (guiding principle 8); you are an auditor, not an amender (principle 7); verify at
> the actual code and data, never at assertion (principles 15 and 19); no self-invented
> labels, abbreviations, numbering schemes, or jargon anywhere — plain-language finding
> slugs; run the self-check over every diff before reporting done (the catalog part
> only after the freeze); never stop a running process without asking the user — no
> subset substitutes for a full-corpus run; shell rules (`; echo "exit:$?"`, redirect
> large output to a file); git rules (stage only your own files by name, never
> `git add -A`, `git status` after every commit — the register row OI-85 convention;
> the known working-tree carry `cowork_joint_key_chord_design.md` stays untouched;
> `cc_*.md` is gitignored — force-add this instruction in your final commit); push to
> `origin` (the user's fork) ONLY, never `upstream` — the standing hard stop,
> `git remote -v` first.
>
> **⚠ WITHHELD READS — do NOT open until your Task-2 freeze commit exists:**
> `STATUS.md`, `OPEN_ITEMS.md`, `DEFECT_TYPES.md`, `cowork_handoff.md`, every
> `cc_*_report.md`, `cowork_siloed_facts_audit.md`, `cowork_adjudication_dossier.md`,
> `cowork_structural_integrity_audit.md`, `cowork_l1_l5_premise_debt_audit.md`,
> `cowork_layer5_engagement_design.md`, `cowork_layer5_function_design.md`,
> `cowork_joint_key_chord_design.md` (also the working-tree carry — do not read or
> touch it), `cowork_fb_redesign_design.md`, `cowork_gate_policy_amendment.md`,
> `cowork_premise_gate_reflection.md`, `cowork_engage_arc_plan.md`,
> `cowork_stage5_fitter_design.md`, `cowork_uncertain_resolver_investigation.md`,
> `cowork_functional_analysis_research_grounding.md`; and under `tools/audit/` every
> `*dispositions*`, `*blind*`, `*errorrate*`, `*relabel*`, `*compare*`,
> `sweep_results*`, `firecount*`, and `firerate*` file, plus the verdict-embodying
> `gen_*_dispositions*` scripts and `gen_signature_sweep.py`. NOTE: the signed
> function-design exception of the first-pass sessions does NOT apply here — the
> second reader judges rows from the code alone, exactly like every other second
> pass. The mandatory session-start `OPEN_ITEMS.md` read is deferred to Task 3 —
> declared here for the user; Cowork performed the register check for this dispatch.
> Declare in the report when each withheld file was first opened. Safe reads from the
> start: `CLAUDE.md`, `cowork_audit_protocol.md` (step P2 defines the vocabulary),
> `BUILD_AND_TEST.md`, `ARCHITECTURE.md`, the roadmap, `docs/scoring_model.md`,
> `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md`, the corpus registries,
> `tools/param_manifest.json`, the committed references under `tools/corpus/` and
> `tools/robust_stop/` (read freely, write never), the RAW inventory tables and
> `manifest.json`s under `tools/audit/l5/` (row lists — scope, not verdicts), the
> sampling scripts' CODE (to adapt), the first-pass instructions (definitions), and
> the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding, plus exactly ONE authorized deletion
> (Task 0). No production change; no constant tuned; no golden refresh;
> `tools/robust_stop/` and `tools/corpus/` written to by NOTHING this session.

## Task 0 — Preconditions, the register commit, and the authorized deletion

0. **Commit Cowork's waiting register edits** (content is Cowork's, summarized here:
   the user's decisions on the debris row OI-134 — delete — and the corpus-expansion
   directive added to OI-38). Stage WITHOUT opening the register:
   ```
   git add OPEN_ITEMS.md
   git add -f cc_instruction_l5_audit_pass2.md
   git commit -m "docs(cowork): OI-134 deletion authorized + OI-38 corpus-expansion directive (user, 2026-07-12) + the layer-5 pass-2 instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining entries: the known carry plus
   untracked scratch only; anything else, stop and report.
1. **Execute the authorized deletion (user-decided, register row OI-134):** delete
   the untracked debris directory `tools/tools/` entirely. It is untracked (verified:
   zero git-tracked files), so this is a filesystem deletion with no git commit of
   its own. Confirm afterward that `tools/tools/` no longer exists and that
   `git status --short` is unchanged by the deletion. The comparison that justified
   it is committed in the harness session's fold; OI-134 gets its closing note in
   your Task-4 fold.
2. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 38a1adeaeb HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-2 freeze.
3. Do not read the withheld files.

## Task 1 — The blind work (all judging happens before anything is unblinded)

You are the independent second reader for layer 5 and the instruments. You succeed by
disagreeing, not by confirming.

1. Adapt the sampling approach into a committed script (no hand-picked rows). Draw
   TWO samples from the full 3,372-row inventory, with NEW fixed seeds — both
   recorded, different from every seed recorded in the audit artifacts so far:
   - at least 140 rows, spread across the four populations in proportion to their row
     counts and across the row kinds within each — the independent second reading;
   - 40 rows, uniformly random over the whole 3,372 — the error-rate sample.
2. Judge EVERY sampled row from the code itself, from scratch, at the FULL protocol
   P2 vocabulary (premises FACT / THEORY / ASSUMPTION; derived facts PUBLISHED /
   SILOED / TRAPPED / DUPLICATED; constants ESTABLISHED / UNFIT / DEAD with the
   manifest-presence check; code RETIRES / SURVIVES; instrument rows additionally get
   the establishment answers: claim / establishment record / stamping /
   silent-failure modes), plus the four standing questions per row, in the random
   order the script produced. Both samples are judged now, blind.
3. Write `tools/audit/l5/pass2_blind_reading.csv/.json` and
   `tools/audit/l5/pass2_blind_errorrate.csv/.json`; commit script + artifacts as ONE
   `feat(tools):` commit and record the hash. THIS commit lifts the withheld list.

## Task 2 — (this freeze commit is the boundary referenced above)

The Task-1 commit IS the freeze. After it, proceed.

## Task 3 — Unblind, compare, diagnose

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read —
   the layer-5 and instrument rows are OI-116 through OI-138 plus the older rows they
   reference), `DEFECT_TYPES.md`, `STATUS.md`, the four first-pass session reports,
   and the four `pass1_dispositions_*` artifacts.
2. Compare your verdicts with the first pass's on the same rows, both samples.
   Classify every disagreement — substantive miss / wording or verdict-axis
   difference / judgment tie — and for every substantive one, diagnose which protocol
   step let it through before proceeding.
3. The disagreement fraction on the 40 blind-judged error-rate rows IS the audit's
   measured error rate. Report the number and list the failing rows. A failure
   implying a whole class was judged wrongly re-opens that class — say so plainly,
   never average it away.

## Task 4 — Sweep the whole scope with the full catalog

Apply every entry of `DEFECT_TYPES.md` — all twenty-five, including DT-22 through
DT-25 founded during this audit — across the ENTIRE 3,372-row inventory, all four
populations.

1. Mechanical entries: `tools/audit/gen_signature_sweep.py --layer l5` (extend the
   one instrument if needed — no parallel script; note the Python-file rows need the
   Python-aware signatures). Hit tables per catalog entry under `tools/audit/l5/`;
   the script fails loudly if any mechanical rule could not run.
2. Review entries: row-by-row against the inventory; per entry record rows checked
   and every hit.
3. Every hit: file and line, one plain-language sentence, and whether an existing
   register row covers it (name it) or it is new.
4. A NEW problem TYPE gets its `DEFECT_TYPES.md` entry in the same commit as the
   report.

## Task 5 — Certification proposal, and the plan's completion statement

1. Propose certifying layer 5 + the instruments only if: the first pass is complete
   (it is), your blind reading and error rate are measured at full vocabulary
   resolution, every disagreement is diagnosed, and the sweep found no untracked
   correctness defect. Otherwise propose withholding, naming concretely what
   remains. You only PROPOSE — write "proposed, awaiting the user's decision"
   everywhere; do not mark OI-84, OI-116, or the entry-gate condition satisfied
   yourself.
2. State plainly in the report: IF the user grants this certification, the OI-84
   dependency-ordered certification plan is COMPLETE — every surviving layer and the
   measurement chain audited on two passes each — and per the register, the held
   OI-43 discussion (mode/key + chord inference — where and how) opens, along with
   the remaining Stage-3 entry-gate items. That statement is orientation for the
   user, not a status you set.

## Task 6 — Report, register, push

1. `cc_l5_audit_pass2_report.md`: sample designs and seeds; when each withheld file
   was first opened; the comparison tables with per-disagreement diagnoses; the error
   rate with its failing rows; the per-catalog-entry sweep results; the Task-0
   deletion confirmation; the certification proposal and exactly what it rests on;
   the completion statement.
2. Register discipline in the SAME commit: every new issue gets its own
   `OPEN_ITEMS.md` row; existing rows referenced, not duplicated; new types get
   catalog rows; update OI-116 (second pass done, proposal stated); close OI-134
   (deletion confirmed). Update `STATUS.md` (prepend) and the entry block of
   `cowork_handoff.md`. Plain language everywhere.
3. Commits: the Task-0 register commit; the Task-1 `feat(tools):` freeze; a
   `feat(tools):` for the sweep if not sensibly part of the fold; ONE `docs(cc):`
   fold (force-add this instruction). Run the self-check over every diff before
   reporting done.
4. **Push — authorized by the user, 2026-07-12:** all local commits to `origin`
   only, after `git remote -v` confirms `upstream` push is still disabled; anything
   that would send content toward `upstream` is the standing hard stop. Confirm in
   the report: the pushed hash, `upstream` untouched.

# CC INSTRUCTION — Layer-5 audit, first pass, session 3 of 3: the shared harness — EG-7 / OI-84 / OI-116

> **Issued by Cowork, 2026-07-12.** Last first-pass session of the whole certification
> plan. Scope: the HARNESS population (~870 deep rows per the committed partition) —
> `tools/batch_analyze.cpp`, the shared executable that generates every corpus, applies
> the presets, hosts the diagnostic flags, and feeds every instrument audited in the
> two sessions before this one. After this session: the whole-scope second pass, then
> the final certification decision, and the plan closes. Certification is NOT decided
> here.
>
> **Scope definition — from the committed artifacts, not memory:** every deep inventory
> row whose file is tagged to the harness population in the layer-5 partition artifact
> under `tools/audit/l5/`. A tag that looks wrong at the code is a finding; record it
> and proceed with the corrected scope, stating both.
>
> **What the harness is, and the questions it gets.** It is BOTH an instrument and a
> program with production-shaped behavior: it drives the real analysis pipeline over
> corpora, defines the preset parameter sets, and emits the serialized results
> everything downstream grades. So it gets both question forms: the correctness
> questions (its preset definitions are inference-affecting constants — provenance and
> manifest-presence per value; its serialization decides what downstream instruments
> can see — the fact-publication questions apply), and the establishment questions
> (what does each output surface claim to represent; what is stamped; which failures
> pass silently — a partial run, a missing score, a flag interaction). Attend
> particularly to: the preset builders (every hand-set value: provenance /
> manifest-presence); flag interactions (which diagnostic flags alter the produced
> artifacts and which are inert — a flag that silently changes serialized output is a
> finding); the exit path (it is known to terminate abruptly rather than through
> normal shutdown — what relies on that, and what could lose buffered output); and
> everything written to disk (which paths, defaulting where — the destructive-default
> family DT-24 was founded one session ago).
>
> **⚠ Read-only running rule (same sharp edge):** run the harness freely for
> characterization, but ONLY writing to scratch output directories. Never regenerate
> into `tools/corpus/` or anything committed. Long runs: let them finish; never kill
> one; no subset substitutes.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING —
> findings become register rows, never patches (guiding principle 8); you are an
> auditor, not an amender (principle 7); verify at the actual code and data, never at
> assertion (principles 15 and 19); no self-invented labels, abbreviations, numbering
> schemes, or jargon anywhere — plain-language finding slugs; run the self-check over
> every diff before reporting done (the catalog part only after the freeze); shell
> rules (`; echo "exit:$?"`, redirect large output to a file); git rules (stage only
> your own files by name, never `git add -A`, `git status` after every commit — the
> register row OI-85 convention; the known working-tree carry
> `cowork_joint_key_chord_design.md` stays untouched; `cc_*.md` is gitignored —
> force-add this instruction in your final commit); push to `origin` (the user's
> fork) ONLY, never `upstream` — the standing hard stop, `git remote -v` first.
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
> `gen_*_dispositions*` scripts and `gen_signature_sweep.py` (in-scope rows of their
> own, if any: marked post-freeze section, same as before). The mandatory
> session-start `OPEN_ITEMS.md` read is deferred to Task 4 — declared here for the
> user; Cowork performed the register check for this dispatch. Declare in the report
> when each withheld file was first opened. Safe reads from the start: `CLAUDE.md`,
> `cowork_audit_protocol.md`, `BUILD_AND_TEST.md` (the harness's documented command
> contract), `ARCHITECTURE.md`, the roadmap, `docs/scoring_model.md` (the preset
> discussion there is contract), `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md`,
> the corpus registries, `tools/param_manifest.json` (data, not verdicts), the
> committed references under `tools/corpus/` and `tools/robust_stop/` (read freely,
> write never), the raw inventory tables and `manifest.json` under `tools/audit/l5/`
> (scope, not verdicts), the parent instructions
> (`cc_instruction_l5_audit_pass1.md`, `cc_instruction_l5_audit_pass1_instruments.md`),
> and the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/` written
> to by NOTHING this session. A surprise in the audited code is a finding; a surprise
> in your own tooling is a stop — fix the tool, restamp, rerun, never hand-edit a
> generated artifact.

## Task 0 — Preconditions

0. **First action — commit Cowork's waiting register edit** (content is Cowork's,
   summarized here: the new row OI-134 recording the discovered untracked debris
   directory `tools/tools/corpus/` and the user's held deletion pending the Task-4.2
   comparison). Stage WITHOUT opening the register:
   ```
   git add OPEN_ITEMS.md
   git add -f cc_instruction_l5_audit_pass1_harness.md
   git commit -m "docs(cowork): OI-134 - untracked debris directory tools/tools/corpus discovered (DT-24 fired historically); deletion held pending the stem-set comparison + the layer-5 harness session instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining entries: the known carry plus
   untracked scratch (including `tools/tools/` itself) only; anything else, stop and
   report.
1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 36c850b0d3 HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-3 freeze.
2. Do not read the withheld files. Do not touch `tools/tools/` (see Task 4.2).
3. Cross-check the row count for the harness population against the inventory (~870).
   If every-row rigor cannot honestly fit, STOP at the counts and propose a further
   split — never silently sample, never thin the verdicts.

## Task 1 — Dispositions for every harness row (protocol P2 + P3)

EVERY row a closed-set verdict at full vocabulary resolution, with the establishment
answers in the row notes where the row is an instrument surface. The priority
attentions from the preamble apply: preset-builder constants (provenance +
manifest-presence per value, no batching); flag inventory (per diagnostic flag: does
it alter serialized output, and is that documented?); the abrupt-exit path and what
depends on it; every disk write with its default path (the DT-24 family).

**The contract direction is mandatory (protocol P3):** from `BUILD_AND_TEST.md`,
`tools/REPRODUCIBILITY.md`, `CLAUDE.md`'s command blocks, and `docs/scoring_model.md`
where it speaks of presets: enumerate every documented command, flag, and guarantee
and locate the code that delivers it — or flag it as prose enforced by nothing.
Equally the other direction: every flag or behavior the code has that no document
mentions is a finding (an undocumented mode on the shared harness is an unratified
measurement path).

## Task 2 — Behavioral characterization (protocol P4): run it

Full-corpus runs to scratch on the pinned corpus (`c50002fee1`, all three presets
where preset-dependent): does the scratch regeneration reproduce the committed
corpus byte-identically (the reproduce-check that establishes the harness end to
end)? Which flags did the runs exercise; which flags did no run exercise (say so per
flag — an unexercised mode is unestablished). Long runs: let them finish.

## Task 3 — Freeze (the blinding boundary)

Write `tools/audit/l5/pass1_dispositions_harness.csv/.json` plus the report draft;
commit as one `feat(tools):`; record the hash. THIS commit lifts the withheld list.

## Task 4 — Unblind, reconcile, the held comparison, report, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read),
   `DEFECT_TYPES.md`, `STATUS.md`, and the three earlier layer-5 session reports.
   Converge or diverge with existing rows explicitly.
2. **The OI-134 comparison (user-directed, post-freeze — READ-ONLY, delete nothing):**
   the untracked debris directory `tools/tools/corpus/` holds converted copies of the
   music21 package's Bach corpus. Mechanically diff its stem set against the project
   corpus registry and `docs/score_inventory.md`'s documented exclusions. Report:
   which stems appear in the debris but not in the project's 352; for each, whether
   its exclusion is documented (where) or undocumented. Update OI-134 with the
   comparison result — the deletion and any corpus-onboarding implication are the
   user's decision on these facts. Do NOT delete anything.
3. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. The whole-scope signature sweep is NOT run here — it is the second pass.
4. `cc_l5_audit_pass1_harness_report.md`: disposition summary per verdict class;
   EVERY flagged row with file, line, one plain-language sentence; the flag inventory
   with exercised/unexercised status; the reproduce-check result; the contract check
   in both directions; the OI-134 comparison table; when each withheld file was first
   opened. Register discipline: every discovered issue gets its `OPEN_ITEMS.md` row
   in the SAME commit as the report; update OI-116 (first pass COMPLETE across all
   populations). Update `STATUS.md` (prepend) and the entry block of
   `cowork_handoff.md`. Plain language everywhere. Say plainly: the first pass of the
   final audit is complete; the second pass decides the certification proposal.
5. Run the self-check over every diff before reporting done.
6. **Commit and PUSH (user-authorized 2026-07-12):** the freeze commit, any
   post-freeze commit, one `docs(cc):` fold (force-add this instruction). Push all
   local commits to `origin` only, after `git remote -v` confirms `upstream` push is
   still disabled; anything that would send content toward `upstream` is the standing
   hard stop. Confirm in the report: the pushed hash, `upstream` untouched.

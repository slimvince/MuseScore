# CC INSTRUCTION — Layer-4 (chord) Certification Audit, PASS 2 (blind second reading + catalog sweep + measured error rate) — EG-7 / OI-84 / OI-102

> **Issued by Cowork, 2026-07-11.** The layer-4 first pass is complete: three sessions
> dispositioned all ~1,869 deep rows (the decoder, the oracle, the satellites — their
> verdicts live in the three `pass1_dispositions_*` artifacts under `tools/audit/l4/`).
> This is the second and final pass; the layer-4 certification decision follows it — made
> by the user, never here. The audit protocol is `cowork_audit_protocol.md`; this
> instruction carries out the independent second reading (step P5), the measured error
> rate (step P6), and the known-problem-type sweep (step P8, second run).
>
> **Three paid-for lessons are baked in — do not relearn them:**
> 1. FULL blinding (the DT-20 lesson): every file that could tell you what the first
>    pass concluded is withheld until your verdicts are frozen and committed.
> 2. Blind-first error rate: the error-rate rows are judged BEFORE you see any pass-1
>    verdict, then compared.
> 3. The FULL fine verdict vocabulary (the OI-100 lesson): the layer-3 second reading
>    used a coarse four-label vocabulary and its "the prose carries the rest" defense
>    cost a whole extra re-derivation session to check. Use the complete protocol P2
>    verdict set per row, at full resolution, from the start. A coarser vocabulary is a
>    deviation that will trigger the same remedy — don't.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING —
> findings become register rows, never patches (guiding principle 8); you are an
> auditor, not an amender (principle 7); verify at the actual code and data, never at
> assertion (principles 15 and 19); no self-invented labels, abbreviations, numbering
> schemes, or jargon anywhere; run the self-check over every diff before reporting done
> (the catalog part only after the freeze); never stop a running process without asking
> the user — no subset substitutes for a full-corpus run; shell rules
> (`; echo "exit:$?"`, redirect large output to a file); git rules (stage only your own
> files by name, never `git add -A`, `git status` after every commit — the register row
> OI-85 convention; the known working-tree carry `cowork_joint_key_chord_design.md`
> stays untouched; `cc_*.md` is gitignored — force-add this instruction in your final
> commit); push to `origin` (the user's fork) ONLY, never `upstream` — the standing
> hard stop, `git remote -v` first.
>
> **⚠ WITHHELD READS — do NOT open until your Task-1 freeze commit exists:**
> `STATUS.md`, `OPEN_ITEMS.md`, `DEFECT_TYPES.md`, `cowork_handoff.md`, every
> `cc_*_report.md`, `cowork_siloed_facts_audit.md`, `cowork_adjudication_dossier.md`,
> `cowork_structural_integrity_audit.md`, `cowork_l1_l5_premise_debt_audit.md`,
> `cowork_layer5_engagement_design.md`, `cowork_layer5_function_design.md`,
> `cowork_joint_key_chord_design.md` (also the working-tree carry — do not read or
> touch it), `cowork_gate_policy_amendment.md`; under `tools/audit/` every
> `*dispositions*`, `*blind*`, `*errorrate*`, `*relabel*`, `*compare*`,
> `sweep_results*`, `firecount*`, and `firerate*` file; and the verdict-embodying
> scripts `tools/audit/gen_signature_sweep.py`, `tools/audit/gen_dispositions.py`,
> `tools/audit/l3/gen_l3_dispositions.py`, and any `gen_*_dispositions*` sibling. The
> mandatory session-start `OPEN_ITEMS.md` read is deferred to Task 2 — declared here
> for the user; Cowork performed the register check for this dispatch. Declare in the
> report when each withheld file was first opened. Safe reads from the start:
> `CLAUDE.md`, `cowork_audit_protocol.md` (its step P2 defines the verdict vocabulary),
> `BUILD_AND_TEST.md`, `ARCHITECTURE.md`, the roadmap, `docs/scoring_model.md`, the
> layer-4 RAW inventory tables and `manifest.json` under `tools/audit/l4/` (the row
> lists — scope, not verdicts), the sampling scripts' CODE
> (`tools/audit/gen_pass2_sample.py` / `gen_blind_rerun_sample.py`, to adapt),
> `cc_instruction_l4_audit_pass1.md` (definitions), and the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/`
> untouched. A surprise in the audited code is a finding; a surprise in your own
> tooling is a stop — fix the tool, restamp, rerun, never hand-edit a generated
> artifact.

## Task 0 — Preconditions

1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor f1b69cc78d HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-1 freeze.
2. Do not read the withheld files.

## Task 1 — The blind work (all judging happens before anything is unblinded)

You are the independent second reader for layer 4. Your job is to find what the first
pass got wrong or missed; you succeed by disagreeing, not by confirming.

1. Adapt the sampling approach into a committed script (no hand-picked rows). Draw TWO
   samples from the layer-4 deep inventory (~1,869 rows across the decoder, oracle, and
   satellite files), with NEW fixed seeds — both recorded, different from every seed
   used so far (`20260712`–`20260715`):
   - at least 120 rows, spread across the five row kinds in proportion to their counts
     and across all in-scope files — the independent second reading;
   - 40 rows, uniformly random — the error-rate sample.
2. Judge EVERY sampled row from the code itself, from scratch, using the FULL protocol
   P2 verdict vocabulary at full resolution — premises FACT / THEORY / ASSUMPTION;
   derived facts PUBLISHED / SILOED / TRAPPED / DUPLICATED; constants ESTABLISHED /
   UNFIT / DEAD with the manifest-presence check; code RETIRES / SURVIVES — plus the
   four standing questions per row, in the random order the script produced. Both
   samples are judged now, blind.
3. Write `tools/audit/l4/pass2_blind_reading.csv/.json` and
   `tools/audit/l4/pass2_blind_errorrate.csv/.json`; commit script + artifacts as ONE
   `feat(tools):` commit and record the hash. THIS commit lifts the withheld list.

## Task 2 — Unblind, compare, diagnose

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read — the
   layer-4 rows are OI-101 through OI-114, plus the older rows the first pass
   referenced), `DEFECT_TYPES.md`, `STATUS.md`, the parent report
   `cc_l4_audit_pass1_report.md`, the three session reports, and the three
   `pass1_dispositions_*` artifacts.
2. Compare your verdicts with the first pass's on the same rows, both samples.
   Classify every disagreement — substantive miss / wording or verdict-axis
   difference / judgment tie — and for every substantive one, diagnose which protocol
   step let it through before proceeding.
3. The disagreement fraction on the 40 blind-judged error-rate rows IS the audit's
   measured error rate. Report the number and list the failing rows. A failure that
   implies a whole class was judged wrongly re-opens that class — say so plainly,
   never average it away.

## Task 3 — Sweep the whole layer with the full catalog

Apply every entry of `DEFECT_TYPES.md` — all twenty-one — across the ENTIRE layer-4
deep inventory. All rows, all three scopes, not a sample.

1. Mechanical entries: run `tools/audit/gen_signature_sweep.py --layer l4` (extend the
   one instrument if the layer argument needs it — no parallel script). Hit tables per
   catalog entry under `tools/audit/l4/`; the script fails loudly if any mechanical
   rule could not run.
2. Review entries: row-by-row against the inventory; per entry record rows checked and
   every hit.
3. Every hit: file and line, one plain-language sentence, and whether an existing
   register row covers it (name it) or it is new.
4. A NEW problem TYPE gets its `DEFECT_TYPES.md` entry in the same commit as the
   report.

## Task 4 — The instrumentation lifecycle facts (register row OI-110)

The oracle fire-count instrumentation (127 default-OFF lines in
`chord/chordanalyzer.cpp` + the gated flush in `tools/batch_analyze.cpp`) has an open
keep-or-revert decision scheduled for now. Gather the facts and state a
recommendation — the decision is the user's: what the instrument measures that nothing
else can; what re-running it costs; what keeping it costs (code weight in the oracle,
maintenance at the planned file split); whether the layer-5 audit or the Stage-5
fitter's liveness checks (register row OI-36) would plausibly reuse it. Facts and one
recommendation, no action.

## Task 5 — Certification proposal

Propose certifying layer 4 only if: the first pass is complete (it is — all three
sessions), your blind reading and error rate are measured at full vocabulary
resolution, every disagreement is diagnosed, and the sweep found no untracked
correctness defect. Otherwise propose withholding, naming concretely what remains. You
only PROPOSE — write "proposed, awaiting the user's decision" everywhere; do not mark
OI-84, OI-102, or the entry-gate condition satisfied yourself.

## Task 6 — Report, register, push

1. `cc_l4_audit_pass2_report.md`: sample designs and seeds; when each withheld file
   was first opened; the comparison tables with per-disagreement diagnoses; the error
   rate with its failing rows; the per-catalog-entry sweep results; the OI-110 facts
   and recommendation; the certification proposal and exactly what it rests on.
2. Register discipline in the SAME commit: every new issue gets its own
   `OPEN_ITEMS.md` row; existing rows referenced, not duplicated; new types get
   catalog rows; update OI-102 (the three-session plan is complete) and add the
   OI-110 facts to its row (decision left open for the user). Update `STATUS.md`
   (prepend) and the entry block of `cowork_handoff.md`. Plain language everywhere.
3. Commits: the Task-1 `feat(tools):` freeze; a `feat(tools):` for the sweep run if
   not sensibly part of the fold; ONE `docs(cc):` fold (force-add this instruction).
   Run the self-check over every diff before reporting done.
4. **Push — authorized by the user, 2026-07-11:** all local commits to `origin` only,
   after `git remote -v` confirms `upstream` push is still disabled; anything that
   would send content toward `upstream` is the standing hard stop. Confirm in the
   report: the pushed hash, `upstream` untouched.

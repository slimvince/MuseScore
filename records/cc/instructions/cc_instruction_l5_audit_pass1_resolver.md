# CC INSTRUCTION — Layer-5 audit, first pass, session 1 of 3: the dormant resolver pipeline — EG-7 / OI-84 / OI-116

> **Issued by Cowork, 2026-07-12.** The layer-5 + instruments inventory is committed
> (`c081f79f63`, feasibility stop at `0382c3275e`, register row OI-116): 3,372 deep rows
> split into three sessions. THIS session is the first: the DORMANT RESOLVER population
> (~815 rows) — the built-but-unwired function pipeline that the engagement stage will
> make production. Two sessions follow (the Python instruments; the shared harness),
> then the whole-scope second pass. Certification is NOT decided here.
>
> **Scope definition — take it from the committed artifacts, not from memory:** every
> deep inventory row whose file is tagged to the dormant-resolver population in the
> layer-5 file table / partition artifact under `tools/audit/l5/` (committed at the
> freeze `0382c3275e`). Those tables are scope, not verdicts — safe to read. If a file's
> tag looks wrong at the code, that is a finding (the catalog's mis-tag type has now
> been founded twice); record it and proceed with the corrected scope, stating both.
>
> **What this code is:** the dormant layer-5 machinery — carried-reading resolution,
> function-output assembly, and whatever progression/vocabulary machinery the tags
> place in this population. It is not on any production path; it runs only in the test
> suites. It is audited in full as surviving code, because the engagement will stand on
> it. Attend especially to its INPUT contract (what it expects the carry to contain)
> and its OUTPUT surface (what it emits forward, at what confidence, on what scale) —
> and, per the fact-publication rule, to what it computes that dies inside.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING —
> findings become register rows, never patches (guiding principle 8); you are an
> auditor, not an amender (principle 7); verify at the actual code and data, never at
> assertion (principles 15 and 19) — including design-document assertions: where the
> signed design and the code disagree, that is a finding, not a reading error; no
> self-invented labels, abbreviations, numbering schemes, or jargon anywhere; run the
> self-check over every diff before reporting done (the catalog part only after the
> freeze); never stop a running process without asking the user; shell rules
> (`; echo "exit:$?"`, redirect large output to a file); git rules (stage only your own
> files by name, never `git add -A`, `git status` after every commit — the register row
> OI-85 convention; the known working-tree carry `cowork_joint_key_chord_design.md`
> stays untouched; `cc_*.md` is gitignored — force-add this instruction in your final
> commit); push to `origin` (the user's fork) ONLY, never `upstream` — the standing
> hard stop, `git remote -v` first.
>
> **⚠ WITHHELD READS (blind first pass, the DT-20 discipline):** do NOT open until your
> Task-3 freeze commit exists: `DEFECT_TYPES.md`, `OPEN_ITEMS.md`, `STATUS.md`,
> `cowork_handoff.md`, every `cc_*_report.md`, `cowork_siloed_facts_audit.md`,
> `cowork_adjudication_dossier.md`, `cowork_structural_integrity_audit.md`,
> `cowork_l1_l5_premise_debt_audit.md`, `cowork_layer5_engagement_design.md`,
> `cowork_joint_key_chord_design.md` (also the working-tree carry — do not read or
> touch it), `cowork_fb_redesign_design.md`, `cowork_gate_policy_amendment.md`,
> `cowork_premise_gate_reflection.md`, `cowork_engage_arc_plan.md`,
> `cowork_stage5_fitter_design.md`, `cowork_uncertain_resolver_investigation.md`,
> `cowork_functional_analysis_research_grounding.md`; and under `tools/audit/` every
> `*dispositions*`, `*blind*`, `*errorrate*`, `*relabel*`, `*compare*`,
> `sweep_results*`, `firecount*`, and `firerate*` file, plus the verdict-embodying
> `gen_*_dispositions*` scripts and `gen_signature_sweep.py`. **The ONE declared
> exception (same as the parent session): `cowork_layer5_function_design.md` is a SAFE
> read** — the signed design specification of exactly this dormant pipeline, its
> contract for the specification-to-code direction; contract, not findings. The
> audit-era documents ABOUT it stay withheld — they contain the findings your blind
> reading exists to independently confirm or contradict. The mandatory session-start
> `OPEN_ITEMS.md` read is deferred to Task 4 — declared here for the user; Cowork
> performed the register check for this dispatch. Declare in the report when each
> withheld file was first opened. Safe reads from the start: `CLAUDE.md`,
> `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`, the roadmap,
> `docs/scoring_model.md`, `cowork_layer5_function_design.md` (the declared
> exception), the raw inventory tables and `manifest.json` under `tools/audit/l5/`
> (scope, not verdicts), `cc_instruction_l5_audit_pass1.md` (the parent instruction,
> for definitions), and the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/`
> untouched. A surprise in the audited code is a finding; a surprise in your own
> tooling is a stop — fix the tool, restamp, rerun, never hand-edit a generated
> artifact.

## Task 0 — Preconditions

1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor d9c7ec6d2d HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-3 freeze.
2. Do not read the withheld files.
3. Cross-check the row count for the dormant-resolver population against the
   inventory; if every-row rigor cannot fit this session, STOP and report with a
   proposed further split — never silently sample.

## Task 1 — Dispositions for every resolver row (protocol P2 + P3)

EVERY row in scope gets a verdict from the closed set, at FULL vocabulary resolution
(the layer-3 lesson — a coarser vocabulary triggers a re-derivation remedy; don't):

- causal premises: FACT (citation) / THEORY (citation answering the specific
  question) / ASSUMPTION (flag). This population encodes decisions about how carried
  readings are selected, ranked, overridden, and marked open — label the load-bearing
  claim UNDER each such decision, and be exact about which are established and which
  are assumed;
- derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED, under the fact-publication
  corollary;
- numeric literals and constants: ESTABLISHED (provenance) / UNFIT (hand-set) / DEAD —
  and whether each appears in `tools/param_manifest.json`. Attend to placeholder
  values that carry load (a constant that is "1.0 for now" is a premise, not a
  neutral default), and to any place where confidence-like quantities from different
  sources meet: state per site whether they are on the same scale, and what
  establishes that;
- code rows: population re-affirmed per row;
- per row, the four standing questions: what does it assume, what does it publish,
  who consumes it, what happens at its edge cases (an empty carry, a single carried
  reading, ties, an abstaining input, conflicting evidence channels, region
  boundaries).

**The contract direction is mandatory (protocol P3):** from the signed
`cowork_layer5_function_design.md`, section by section, plus `ARCHITECTURE.md` and the
roadmap: enumerate every specified behavior, ordering, invariant, and output field,
and locate each in the code — or flag the absence. Equally: every code behavior NOT in
the specification is flagged the other way (an unspecified behavior in a dormant
pipeline is a premise nobody ratified). Where the design and the code disagree, record
the disagreement precisely — which section, which lines, what differs.

## Task 2 — Behavioral characterization (protocol P4)

The resolver is dormant: production fire rates are zero by construction. Characterize
via the test suites: run them, and record per mechanism/branch which tests reach it
and which branches no test reaches (an untested branch in the engagement's target is a
finding of its own rank). Where a branch's designed population can be stated from the
design document, say whether any test exercises that population. No production
instrumentation is needed for a dormant path; if you believe otherwise, STOP and
report instead.

## Task 3 — Freeze (the blinding boundary)

Write `tools/audit/l5/pass1_dispositions_resolver.csv/.json` plus the report draft;
commit as one `feat(tools):`; record the hash. THIS commit lifts the withheld list.

## Task 4 — Unblind, reconcile, report, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read —
   several existing rows concern this pipeline directly; where your blind findings
   coincide with them, say so explicitly and reference the row — that convergence is
   evidence the register is right, and divergence is bigger news), `DEFECT_TYPES.md`,
   `STATUS.md`, and `cc_l5_audit_pass1_report.md` (the parent session's report).
2. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. The whole-scope signature sweep is NOT run here — it belongs to the second
   pass.
3. `cc_l5_audit_pass1_resolver_report.md`: disposition summary per verdict class;
   EVERY flagged row with file, line, and one plain-language sentence for a reader who
   does not know the code; the test-coverage table (which branches no test reaches);
   the full specification-to-code results in BOTH directions (absences and
   unspecified behaviors); when each withheld file was first opened. Register
   discipline: every discovered issue gets its `OPEN_ITEMS.md` row in the SAME commit
   as the report. Update `STATUS.md` (prepend) and the entry block of
   `cowork_handoff.md`. Plain language everywhere.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-12):** the Task-3 `feat(tools):`
   freeze, one `docs(cc):` fold (force-add this instruction). Push all local commits
   to `origin` only, after `git remote -v` confirms `upstream` push is still
   disabled; anything that would send content toward `upstream` is the standing hard
   stop. Confirm in the report: the pushed hash, `upstream` untouched.

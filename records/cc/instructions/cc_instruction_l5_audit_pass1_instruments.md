# CC INSTRUCTION — Layer-5 audit, first pass, session 2 of 3: the Python measurement instruments — EG-7 / OI-84 / OI-116

> **Issued by Cowork, 2026-07-12.** Second of the three sessions completing the
> layer-5 + instruments first pass (register row OI-116; the dormant-resolver session
> is done). THIS session covers the PYTHON INSTRUMENTS population (~1,687 deep rows per
> the committed partition) — the measurement chain the project's regression stops,
> corpus generation, ground-truth parsing, grading, and fitting all stand on. One
> session follows (the shared harness), then the whole-scope second pass.
> Certification is NOT decided here.
>
> **Scope definition — from the committed artifacts, not memory:** every deep
> inventory row whose file is tagged to the Python-instruments population in the
> layer-5 partition artifact under `tools/audit/l5/` (committed at `0382c3275e`).
> A tag that looks wrong at the code is a finding; record it and proceed with the
> corrected scope, stating both.
>
> **The question these rows get is the ESTABLISHMENT question (guiding principle 19).**
> For code layers the audit asks "is this correct?"; for an instrument it asks: what
> does this instrument CLAIM to measure; what positively establishes that it measures
> it (an oracle cross-check, a derivation of the measurement unit, a reproduce-check) —
> and where is that establishment RECORDED; what is stamped (corpus hash, commit,
> row counts) and what is not; which failure modes pass SILENTLY (an empty input, a
> missing file, a partial corpus, a stale manifest, a format drift in what it parses).
> An instrument trusted only because it has never visibly failed is exactly what
> principle 19 forbids — say so per instrument, honestly.
>
> **⚠ Special rule for this session — the audit's own tooling may be IN scope.** If
> the partition includes the audit's own verdict-embodying scripts (the disposition
> generators, the signature sweep), those specific rows CANNOT be judged blind — the
> scripts are on the withheld list precisely because reading them reveals catalog
> signatures and verdict vocabulary. Resolution, declared here for the user: judge
> every OTHER instrument row blind first, freeze (Task 3), and only THEN disposition
> the audit-tooling rows as a clearly-marked post-freeze section of the same artifact.
> State in the report which rows were judged on which side of the freeze.
>
> **⚠ Read-only discipline has a sharp edge here: running instruments is allowed and
> wanted, but ONLY in modes that write nowhere near the committed references.** Never
> regenerate into `tools/corpus/`, never write into `tools/robust_stop/`; every run
> output goes to a scratch directory (the instruments' own output-directory arguments
> exist for this). If an instrument CANNOT be run without touching committed
> artifacts, that fact is itself a finding — record it, do not run it. Long runs: let
> them finish; never kill one; no subset substitutes.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING —
> findings become register rows, never patches (guiding principle 8); you are an
> auditor, not an amender (principle 7); verify at the actual code and data, never at
> assertion (principles 15 and 19); no self-invented labels, abbreviations, numbering
> schemes, or jargon anywhere; run the self-check over every diff before reporting
> done (the catalog part only after the freeze); shell rules (`; echo "exit:$?"`,
> redirect large output to a file); git rules (stage only your own files by name,
> never `git add -A`, `git status` after every commit — the register row OI-85
> convention; the known working-tree carry `cowork_joint_key_chord_design.md` stays
> untouched; `cc_*.md` is gitignored — force-add this instruction in your final
> commit); push to `origin` (the user's fork) ONLY, never `upstream` — the standing
> hard stop, `git remote -v` first.
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
> `gen_*_dispositions*` scripts and `gen_signature_sweep.py` (see the special rule
> above for their own in-scope rows). The mandatory session-start `OPEN_ITEMS.md`
> read is deferred to Task 4 — declared here for the user; Cowork performed the
> register check for this dispatch. Declare in the report when each withheld file was
> first opened. Safe reads from the start: `CLAUDE.md` (its gate-policy blocks are the
> regression-stop instruments' own CONTRACT — what they promise to measure; contract,
> not findings), `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`,
> the roadmap, `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md`, the corpus
> registries (`tools/corpus_registry.json`, `tools/extra_scores_registry.json`),
> `tools/param_manifest.json` (itself in scope — data, not verdicts), the committed
> reference artifacts under `tools/robust_stop/` and the corpus manifests (READ them
> freely — they are what the instruments are checked AGAINST; never write), the raw
> inventory tables and `manifest.json` under `tools/audit/l5/` (scope, not verdicts),
> `cc_instruction_l5_audit_pass1.md` (the parent instruction, for definitions), and
> the instrument source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/` written
> to by NOTHING this session. A surprise in the audited instruments is a finding; a
> surprise in your own tooling is a stop — fix the tool, restamp, rerun, never
> hand-edit a generated artifact.

## Task 0 — Preconditions

1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor dc2d564f9e HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-3 freeze.
2. Do not read the withheld files.
3. Cross-check the row count for the instruments population against the inventory.
   ~1,687 rows is the largest single session of the plan: if every-row rigor cannot
   honestly fit, STOP after stating the counts and propose a further split — never
   silently sample, never thin the verdicts to make it fit.

## Task 1 — Dispositions for every instrument row (protocol P2 + P3)

EVERY row in scope gets a verdict from the closed set at full vocabulary resolution.
The standard verdicts apply (premises FACT / THEORY / ASSUMPTION; derived facts
PUBLISHED / SILOED / TRAPPED / DUPLICATED; constants ESTABLISHED / UNFIT / DEAD with
the manifest-presence check where a constant is inference-affecting; code SURVIVES /
RETIRES), and per instrument the establishment questions above are answered as part
of the row notes: claim, establishment record, stamping, silent-failure modes.
Attend particularly to:

- thresholds and tolerances inside instruments (a grading tolerance is a measurement
  decision — where does its value come from?);
- duplicated logic between instruments (two parsers, two tick-matchers, two grading
  conventions — one concern, one path);
- what each instrument writes that downstream instruments or documents consume, and
  whether any figure can travel from measurement to document by hand (the
  hand-transcription rule);
- silent-failure paths: empty inputs, missing manifests, partial corpora, unmatched
  stems, format drift in parsed ground truth.

**The contract direction is mandatory (protocol P3):** from `CLAUDE.md`'s gate-policy
blocks (what the regression stop PROMISES: the per-preset non-increase check, the
explained per-run diff, the manifest re-stamping, the corpus validation refusing
contaminated directories), `tools/REPRODUCIBILITY.md`, and `docs/score_inventory.md`:
enumerate every documented guarantee and locate the code that delivers it — or flag
the absence. Every guarantee that exists in prose but is enforced by nothing is a
finding of the first rank for this scope.

## Task 2 — Behavioral characterization (protocol P4): run them

For each runnable instrument: run it READ-ONLY against its committed reference
artifacts (scratch output only) and record: does it reproduce its committed results
(the reproduce-check half of establishment)? Which of its branches did the run
exercise? For the regression-stop pair specifically: a full run against the committed
reference must PASS clean on the current head — if it does not, that is a
stop-and-report finding of the highest rank this audit can produce. Instruments that
cannot run read-only, or whose reference artifacts do not exist, are flagged as
unestablished-by-construction. Long runs: let them finish.

## Task 3 — Freeze (the blinding boundary)

Write `tools/audit/l5/pass1_dispositions_instruments.csv/.json` (blind rows) plus the
report draft; commit as one `feat(tools):`; record the hash. THIS commit lifts the
withheld list. Then, per the special rule: disposition the audit's own
verdict-embodying tooling rows as a clearly-marked post-freeze section appended to
the same artifact (a second commit), stating in the report which rows were judged on
which side.

## Task 4 — Unblind, reconcile, report, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read —
   the instrument-layer section has standing rows; where your blind findings
   coincide, say so and reference; divergence is bigger news), `DEFECT_TYPES.md`,
   `STATUS.md`, and `cc_l5_audit_pass1_report.md`.
2. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. The whole-scope signature sweep is NOT run here — it belongs to the second
   pass.
3. `cc_l5_audit_pass1_instruments_report.md`: disposition summary per verdict class;
   EVERY flagged row with file, line, and one plain-language sentence; the
   per-instrument establishment table (claim / establishment record / stamped /
   silent-failure modes / reproduce-check result); the contract-check results with
   every unenforced guarantee named; the blind/post-freeze row split; when each
   withheld file was first opened. Register discipline: every discovered issue gets
   its `OPEN_ITEMS.md` row in the SAME commit as the report. Update `STATUS.md`
   (prepend) and the entry block of `cowork_handoff.md`. Plain language everywhere.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-12):** the Task-3 freeze commit, the
   post-freeze tooling-rows commit, one `docs(cc):` fold (force-add this
   instruction). Push all local commits to `origin` only, after `git remote -v`
   confirms `upstream` push is still disabled; anything that would send content
   toward `upstream` is the standing hard stop. Confirm in the report: the pushed
   hash, `upstream` untouched.

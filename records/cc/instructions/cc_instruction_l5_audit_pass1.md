# CC INSTRUCTION — Layer-5 (function) + instruments Certification Audit, PASS 1 (blind enumerative) — EG-7 / OI-84

> **Issued by Cowork, 2026-07-11.** Layers 1 through 4 are certified. This opens the
> LAST audit of the dependency-ordered plan: layer 5 — the harmonic-function machinery —
> plus the measurement instruments. When this audit completes (both passes), the
> certification plan is done. This is the FIRST pass; certification is NOT granted
> here. The audit protocol is `cowork_audit_protocol.md`; this instruction carries out
> steps P1–P4, blind (step P8, first run). As with layer 4, the inventory may prove too
> large for one session — the feasibility stop below is expected, not exceptional.
>
> **The layer-5 wrinkle — most of this layer is DORMANT, and that is the point.** Layer
> 5 contains, side by side: (a) code that RETIRES per the roadmap's retirement map;
> (b) the DORMANT-BUT-SURVIVING resolver pipeline — built, tested, not yet wired to
> production — which is the engagement's target and is audited in full as surviving
> code; (c) LIVE code on today's production path. Tag every file (and every row where a
> file mixes populations) to one of these three, each tag verified at the code and call
> sites; inherited file-table tags are starting points to re-verify, never facts (the
> catalog's mis-tag type was founded on exactly this mistake). THE INSTRUMENTS are a
> fourth scope: the measurement chain under `tools/` that the project's regression
> stops, corpus generation, ground-truth parsing, and fitting depend on — for these the
> audit question is establishment (guiding principle 19): what does each instrument
> actually measure, what validates it, and what would silently break it.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING beyond
> the one explicitly authorized revert in Task 0 — findings become register rows, never
> patches (guiding principle 8); you are an auditor, not an amender (principle 7);
> verify at the actual code and data, never at assertion (principles 15 and 19); no
> self-invented labels, abbreviations, numbering schemes, or jargon anywhere; run the
> self-check over every diff before reporting done (the catalog part only after the
> freeze); never stop a running process without asking the user — no subset substitutes
> for a full-corpus run; shell rules (`; echo "exit:$?"`, redirect large output to a
> file); git rules (stage only your own files by name, never `git add -A`, `git status`
> after every commit — the register row OI-85 convention; the known working-tree carry
> `cowork_joint_key_chord_design.md` stays untouched; `cc_*.md` is gitignored —
> force-add this instruction in your final commit); push to `origin` (the user's fork)
> ONLY, never `upstream` — the standing hard stop, `git remote -v` first.
>
> **⚠ WITHHELD READS (blind first pass, the DT-20 discipline):** do NOT open until your
> Task-4 freeze commit exists: `DEFECT_TYPES.md`, `OPEN_ITEMS.md`, `STATUS.md`,
> `cowork_handoff.md`, every `cc_*_report.md`, `cowork_siloed_facts_audit.md`,
> `cowork_adjudication_dossier.md`, `cowork_structural_integrity_audit.md`,
> `cowork_l1_l5_premise_debt_audit.md`, `cowork_layer5_engagement_design.md`,
> `cowork_joint_key_chord_design.md` (also the working-tree carry — do not read or
> touch it), `cowork_fb_redesign_design.md`, `cowork_gate_policy_amendment.md`,
> `cowork_premise_gate_reflection.md`, `cowork_engage_arc_plan.md`,
> `cowork_stage5_fitter_design.md`, `cowork_uncertain_resolver_investigation.md`; and
> under `tools/audit/` every `*dispositions*`, `*blind*`, `*errorrate*`, `*relabel*`,
> `*compare*`, `sweep_results*`, `firecount*`, and `firerate*` file, plus the
> verdict-embodying `gen_*_dispositions*` scripts and `gen_signature_sweep.py`.
> **ONE deliberate exception, declared for the user:** `cowork_layer5_function_design.md`
> is a SAFE read — it is the signed design specification of the dormant resolver (the
> layer's contract, needed for the specification-to-code direction), accepted and
> declared as contract, not findings. The audit-era documents ABOUT that design (the
> engagement design, the premise-debt audit, the investigation reports) remain
> withheld — they contain the very findings your blind reading exists to independently
> confirm or contradict. The mandatory session-start `OPEN_ITEMS.md` read is deferred
> to Task 5 — declared here for the user; Cowork performed the register check for this
> dispatch. Declare in the report when each withheld file was first opened. Safe reads
> from the start: `CLAUDE.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`,
> `ARCHITECTURE.md`, the roadmap, `docs/scoring_model.md`,
> `cowork_layer5_function_design.md` (the declared exception above),
> `tools/REPRODUCIBILITY.md` and the corpus registries (instrument-scope context), the
> raw inventory tables and `manifest.json`s under `tools/audit/` (scope, not
> verdicts), `cc_instruction_l4_audit_pass1.md` (definitions), and the source code
> itself.
>
> **Scope declaration:** READ-ONLY fact-finding, plus exactly ONE authorized code
> change (the Task-0 revert, decided by the user at register row OI-110). No other
> production change; no constant tuned; no golden refresh; `tools/robust_stop/` and
> `tools/corpus/` reference artifacts untouched. A surprise in the audited code is a
> finding; a surprise in your own tooling is a stop — fix the tool, restamp, rerun,
> never hand-edit a generated artifact.

## Task 0 — Preconditions, the register commit, and the authorized revert

0. **Commit Cowork's waiting register edits** (content is Cowork's, summarized here:
   the layer-4 certification grant and the OI-110 revert decision). Stage WITHOUT
   opening the register:
   ```
   git add OPEN_ITEMS.md
   git add -f cc_instruction_l5_audit_pass1.md
   git commit -m "docs(cowork): L4 certification GRANTED + OI-110 decided (revert the oracle fire-count instrumentation) + the layer-5 audit pass-1 instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining entries: the known carry plus
   untracked scratch only; anything else, stop and report.
1. **Execute the authorized revert (user-decided, register row OI-110):**
   `git revert --no-edit 55829ebe15` — removes the oracle fire-count instrumentation
   (127 default-OFF lines in `chord/chordanalyzer.cpp` + the gated flush in
   `tools/batch_analyze.cpp`). Then prove it: build, run BOTH test suites (green
   required), and confirm the revert touched exactly those two files. The reverted
   instrument remains in history at `55829ebe15` for any future re-add. If the revert
   does not apply cleanly or a suite fails, STOP and report — do not improvise.
2. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 824c419cb9 HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-4 freeze (the revert
   above needs no log — the hash is given).
3. Do not read the withheld files.

## Task 1 — The machine-generated inventory (protocol P1)

1. Extend `tools/audit/gen_inventory.py` with the layer-5 and instruments extraction —
   ONE instrument, no parallel script. The layer-5 definition comes from
   `ARCHITECTURE.md`, the roadmap, and the signed function design (the declared
   contract read); the instruments scope is the measurement chain under `tools/`: the
   regression-stop instruments, the corpus generators and validators, the ground-truth
   parser, the comparison and grading tools, the fit manifest, and `batch_analyze`
   itself as the shared harness. Re-verify every inherited file tag at the code; tag
   each file to retiring / dormant-but-surviving / live / instrument, one-line reason
   each; a mis-tag is a finding.
2. For surviving and live layer-5 files and for the instruments: the complete row
   lists (functions; numeric literals with the trivial-0/1 exclusion in the script;
   externally visible fields; branches in non-trivial functions; cross-layer calls
   both directions — for instruments also: what production or corpus surface each
   reads, and what artifact each writes). For retiring files: file-level rows with the
   information-loss interpretation-check note only.
3. Artifacts under `tools/audit/l5/` as CSV/JSON; stamp `tools/audit/l5/manifest.json`
   with HEAD commit, corpus hash `c50002fee1`, row counts. The script fails if any
   file lacks a tag. Commit as one `feat(tools):`.
4. **Feasibility stop (expected):** if the deep-row count makes every-row disposition
   infeasible in one session — likely, given the instruments' breadth — STOP after
   this task, freeze what exists, and report the counts with a proposed partition into
   sequential sessions (for example: the dormant resolver pipeline; the live function
   path; the instruments). Do NOT silently sample.

## Task 2 — Dispositions (protocol P2 + P3), if feasible this session

Same discipline as every layer: EVERY deep row a closed-set verdict with the four
standing questions; premises FACT / THEORY / ASSUMPTION; derived facts PUBLISHED /
SILOED / TRAPPED / DUPLICATED under the fact-publication corollary; constants
ESTABLISHED / UNFIT / DEAD with the manifest-presence check; code population
re-affirmed per row. For the dormant resolver, attend to what it reads from the carry
and what it emits — the engagement will stand on exactly those surfaces. For the
instruments, the P2 questions take their establishment form: what does this instrument
claim to measure; what derivation or oracle cross-check establishes that it measures
it; what is stamped (corpus hash, commit) and what is not; what failure would pass
silently. **The contract direction (P3) is mandatory:** from the signed function
design, `ARCHITECTURE.md`, and the roadmap — every specified behavior located in code
or flagged absent; for instruments, from `CLAUDE.md`'s own gate-policy section and
`tools/REPRODUCIBILITY.md` — every documented guarantee located or flagged.

## Task 3 — Behavioral characterization (protocol P4), if feasible this session

Live code: fire rates on the pinned corpus (`c50002fee1`, Baroque unless
preset-gated), least-invasive routes first; a default-OFF counter only where nothing
else can count, own revertible commit, byte-identity re-proven. Dormant resolver:
production fire rates are zero by construction — characterize via the test suites and
say so per row. Instruments: characterize by RUNNING them against their own committed
reference artifacts where that is read-only (the regression-stop pair, the corpus
validators) and recording agreement; an instrument that cannot be re-run read-only is
flagged as such. Full-corpus runs are long: let them finish.

## Task 4 — Freeze (the blinding boundary)

Write `tools/audit/l5/pass1_dispositions.csv/.json` (or the partition-appropriate
artifact if the feasibility stop fired) plus the report draft; commit as one
`feat(tools):`; record the hash. THIS commit lifts the withheld list.

## Task 5 — Unblind, promote, report, fold, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read —
   many rows concern layer 5 and the instruments directly; where your findings
   coincide, reference and enrich, don't duplicate), `DEFECT_TYPES.md`, `STATUS.md`.
2. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. The whole-scope signature sweep is NOT run here — it belongs to the second
   pass.
3. `cc_l5_audit_pass1_report.md`: inventory sizes and manifest; the population
   partition with counts; disposition summary per verdict class (or the partition
   proposal if the stop fired); EVERY flagged row with file, line, and one
   plain-language sentence; the fire-rate/establishment table; the retiring-code
   interpretation-check notes; the Task-0 revert confirmation (hash, files, suites);
   when each withheld file was first opened. Register discipline: every discovered
   issue gets its `OPEN_ITEMS.md` row in the SAME commit as the report; flip OI-110 to
   closed with the revert commit hash. Update `STATUS.md` (prepend) and the entry
   block of `cowork_handoff.md`. Plain language everywhere.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-11):** the Task-0 commits (register +
   revert), the Task-1 `feat(tools):`, any Task-3 counter `feat(tools):`, the Task-4
   freeze, one `docs(cc):` fold (force-add this instruction). Push all local commits
   to `origin` only, after `git remote -v` confirms `upstream` push is still disabled;
   anything that would send content toward `upstream` is the standing hard stop.
   Confirm in the report: the pushed hash, `upstream` untouched.

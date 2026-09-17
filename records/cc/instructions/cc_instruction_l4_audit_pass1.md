# CC INSTRUCTION — Layer-4 (chord) Certification Audit, PASS 1 (blind enumerative) — EG-7 / OI-84

> **Issued by Cowork, 2026-07-11.** Layers 1, 2, and 3 are certified. The audit plan's
> dependency order names layer 4 next: the chord layer — the dormant slice decoder and
> the surviving scorer core. This is the FIRST of two passes; certification is NOT
> granted here. The audit protocol is `cowork_audit_protocol.md`; this instruction
> carries out its inventory, dispositions, contract-direction check, and behavioral
> characterization (steps P1–P4), blind (step P8, first run).
>
> **The layer-4 wrinkle — three populations, and mixing them up is itself a defect.**
> Layer 4 contains, side by side: (a) code that RETIRES at the decoder engagement per
> the roadmap's retirement map — it gets NO deep audit, only the information-loss
> interpretation-check note recorded for its deletion; (b) the DORMANT-BUT-SURVIVING
> decoder — not yet on the production path, but it is the engagement's clean target and
> is audited as surviving code in full; (c) the LIVE surviving scorer core. Tag every
> file (and, where a file mixes populations, every row) to one of these three, each tag
> with a one-line reason verified at the code — the file-table tags inherited from the
> earlier audits contain at least one known mis-tag (the catalog's file-table mis-tag
> type), so inherited tags are starting points to re-verify, never facts.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):**
> - Guiding principle 8: you fix NOTHING. A discovered violation — even an obvious bug —
>   becomes a register row, never a patch. Guiding principle 7: you are an auditor, not
>   an amender; any eventual fix belongs to the layer that owns the concern.
> - Guiding principles 15 and 19: verify at the actual code and data, never at assertion
>   — comments, docs, and earlier sessions' reports included.
> - The conventions: no self-invented labels, abbreviations, numbering schemes, or
>   jargon, anywhere. Existing repository names or plain words.
> - The self-check rule: after every coding exercise, re-read the actual diff of every
>   touched file against the principles, the conventions, and the gate policies before
>   reporting done. The catalog part of the check runs only after your Task-4 freeze.
> - Long-running measurements: never stop a running process without asking the user; no
>   subset substitutes for a full-corpus run.
> - Shell rules: append `; echo "exit:$?"` to any command that may return non-zero;
>   redirect large output to a file and read the file.
> - Git rules: stage only your own files, named one by one; never `git add -A`;
>   `git status` after every commit to confirm disk matches (the register row OI-85
>   convention). Known working-tree carry: `cowork_joint_key_chord_design.md` (register
>   row OI-51) — leave untouched. `cc_*.md` files are gitignored; force-add this
>   instruction file in your final documentation commit.
> - Push rules: `origin` (the user's fork, `slimvince/MuseScore`) only. NEVER `upstream`
>   (`musescore/MuseScore`) — the standing hard stop. Verify with `git remote -v` first.
>
> **⚠ WITHHELD READS (blind first pass, the DT-20 discipline):** do NOT open until your
> Task-4 freeze commit exists: `DEFECT_TYPES.md`, `OPEN_ITEMS.md`, `STATUS.md`,
> `cowork_handoff.md`, every `cc_*_report.md`, `cowork_siloed_facts_audit.md`,
> `cowork_adjudication_dossier.md`, `cowork_structural_integrity_audit.md`,
> `cowork_l1_l5_premise_debt_audit.md`, and under `tools/audit/` every `*dispositions*`,
> `*blind*`, `*errorrate*`, `*relabel*`, `*compare*`, `sweep_results*`, and
> `firerate*` file. The mandatory session-start `OPEN_ITEMS.md` read is deferred to
> Task 5 — deliberate, declared here for the user; Cowork performed the register check
> for this dispatch (no open register row gates the layer-4 first pass). Declare in the
> report when each withheld file was first opened. Safe reads from the start:
> `CLAUDE.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`, the
> roadmap (the retirement map lives there — scope information, accepted and declared),
> `docs/scoring_model.md` (the layer's authoritative contract document, REQUIRED for the
> contract-direction check; it records historical constraints and dead ends — accepted
> and declared as contract, not findings), the raw inventory tables and instruments
> under `tools/audit/` (`gen_inventory.py`, `file_table.csv`, `l3_*.csv` and
> `l1l2_*.csv` raw tables, `manifest.json`s), and the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/` reference
> artifacts untouched. A surprise in the audited code is a finding to record; a surprise
> in your own tooling is a stop — fix the tool, restamp, rerun, never hand-edit a
> generated artifact.

## Task 0 — Preconditions

0. **First action — commit Cowork's waiting register edits** (content is Cowork's,
   user-ratified: the rows recording the layer-3 certification grant, plus this
   instruction file). Stage WITHOUT opening the register:
   ```
   git add OPEN_ITEMS.md
   git add -f cc_instruction_l4_audit_pass1.md
   git commit -m "docs(cowork): L3 certification GRANTED (OI-84/OI-100 updated) + the layer-4 audit pass-1 instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining entries: the known carry plus
   untracked scratch only; anything else, stop and report. A file with nothing to stage
   is noted and skipped.
1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 4a3952d594 HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-4 freeze.
2. Do not read the withheld files.

## Task 1 — The machine-generated inventory (protocol P1)

1. Extend `tools/audit/gen_inventory.py` with the layer-4 extraction — ONE instrument,
   no parallel script. The layer-4 definition comes from `ARCHITECTURE.md`, the roadmap,
   and `docs/scoring_model.md` (read them; do not guess). Re-verify every inherited
   file tag at the code; tag each layer-4 file to one of the three populations above,
   with the one-line reason. A mis-tag you find is a finding.
2. For every layer-4 file in populations (b) and (c) — the surviving code: the complete
   row lists, same shape as the earlier layers (functions and methods; numeric literals
   with the trivial-0/1 exclusion IN the script; externally visible fields; branches in
   non-trivial functions; cross-layer calls in both directions). For population (a) —
   retiring code: file-level rows only, each carrying the information-loss
   interpretation-check note (what embedded interpretation must be consciously kept or
   rejected when it is deleted); no deep rows.
3. Artifacts under `tools/audit/l4/` as CSV/JSON; stamp `tools/audit/l4/manifest.json`
   with HEAD commit, corpus hash `c50002fee1`, and row counts. The script fails if any
   file lacks a tag. Commit script + artifacts as one `feat(tools):` commit.
4. **Feasibility stop:** layer 4 is the largest layer (the chord analyzer file alone
   awaits its planned split). If the deep-row count makes every-row disposition
   infeasible in one session, STOP after this task and report the counts with a
   proposed partition into sequential sessions — do NOT silently sample or skip; the
   protocol's totality is the point.

## Task 2 — Dispositions (protocol P2 + P3)

For EVERY deep inventory row, a verdict from the closed set — "no issue" is a recorded
claim with a stated reason:

- causal premises: FACT (citation) / THEORY (citation answering the specific question) /
  ASSUMPTION (flag);
- derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED, under the fact-publication
  corollary (pay particular attention to what the decoder computes that the layers
  above will need at the engagement: alternatives, margins, membership verdicts,
  per-note evidence);
- numeric literals and constants: ESTABLISHED (provenance) / UNFIT (hand-set) / DEAD —
  and whether each appears in `tools/param_manifest.json`;
- code: population tag re-affirmed per row (retiring rows are not deep-judged);
- per row, the four standing questions: what does it assume, what does it publish, who
  consumes it, what happens at its edge cases (empty slices, single-note sonorities,
  symmetric chords, enharmonic spellings, voice crossings, grace notes, ties).

**The contract direction is mandatory (protocol P3):** from `docs/scoring_model.md`,
`ARCHITECTURE.md`, and the roadmap's statements of what layer 4 must deliver upward,
enumerate every expected output and behavior and locate each in the code — or flag the
absence. Check the scoring document's own sync invariants against the code (its
template count must match the declared constant); a drift is a finding.

## Task 3 — Behavioral characterization (protocol P4)

For every live layer-4 mechanism and branch: fire rate on the pinned corpus
(`c50002fee1`; Baroque unless preset-gated). For the DORMANT decoder population, fire
rates on the production path are zero by construction — characterize instead via the
existing test suites and any existing default-OFF diagnostic paths; say per row which
route you used. Least-invasive route first: existing dumps and standalone scripts;
where only instrumentation can count, a minimal default-OFF counter as its own
revertible `feat(tools):` commit with production byte-identity re-proven (standard
corpus regeneration, zero diff, both suites green, NO golden refresh); where even that
is disproportionate, "fire rate not measured" with the reason. A mechanism that never
fires, always fires, or wildly misses its documented population is a finding.

## Task 4 — Freeze (the blinding boundary)

Write `tools/audit/l4/pass1_dispositions.csv/.json` plus the report draft; commit;
record the hash. THIS commit lifts the withheld list.

## Task 5 — Unblind, promote, report, fold, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read — many
   existing rows concern layer 4: the anchor and carry rows, the siloed-facts rows, the
   temporal-extension row among them), `DEFECT_TYPES.md`, `STATUS.md`. Where a finding
   coincides with an existing row, reference it instead of duplicating.
2. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. Do NOT run the second-pass signature sweep — separate instruction, fresh
   session.
3. `cc_l4_audit_pass1_report.md`: inventory sizes and manifest; the three-population
   partition with counts; disposition summary per verdict class; EVERY flagged row with
   file, line, and one plain-language sentence; the fire-rate table; the retiring-code
   list with its interpretation-check notes; when each withheld file was first opened.
   Register discipline: every discovered issue gets its `OPEN_ITEMS.md` row in the SAME
   commit as the report; new types get catalog rows. Update `STATUS.md` (prepend) and
   the entry block of `cowork_handoff.md`. Plain language everywhere.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-11):** the Task-0 commit, the Task-1
   `feat(tools):`, any Task-3 counter `feat(tools):`, one `docs(cc):` fold (force-add
   this instruction). Push all local commits to `origin` only, after `git remote -v`
   confirms `upstream` push is still disabled; anything that would send content toward
   `upstream` is the standing hard stop. Confirm in the report: the pushed hash,
   `upstream` untouched.

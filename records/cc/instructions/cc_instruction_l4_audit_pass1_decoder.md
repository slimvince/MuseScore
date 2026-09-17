# CC INSTRUCTION — Layer-4 audit, first pass, session 1 of 3: the dormant slice decoder — EG-7 / OI-84 / OI-102

> **Issued by Cowork, 2026-07-11.** The layer-4 first pass hit its planned feasibility
> stop: the inventory (committed at `88befa3055`, artifacts under `tools/audit/l4/`)
> came out to ~2,100 deep rows, too many for one rigorous session, so the row-by-row
> work was split into three sessions (register row OI-102). THIS session is the first:
> the dormant slice decoder, `chord/chordslicedecoder.h` and
> `chord/chordslicedecoder.cpp` (~311 inventory rows). Two more sessions follow (the
> scoring oracle; then the formatter and satellites), then the whole-layer second pass.
> Certification is NOT decided here.
>
> **What this code is:** `ChordSliceDecoder` is dormant-but-surviving — not on the
> production path, reachable only through the `batch_analyze --decode-chords`
> diagnostic and the test suites, but it is the decoder the engagement stage will make
> production. Audit it as surviving code in full. It reuses the live scoring oracle
> (`analyzeChord`) rather than re-deriving scores; where its rows touch oracle
> internals, the verdict belongs to the oracle session — record the boundary, don't
> audit across it.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING —
> findings become register rows, never patches (guiding principle 8); you are an
> auditor, not an amender (principle 7); verify at the actual code and data, never at
> assertion (principles 15 and 19); no self-invented labels, abbreviations, numbering
> schemes, or jargon anywhere — existing repository names or plain words; run the
> self-check over every diff before reporting done (the catalog part only after the
> freeze); never stop a running process without asking the user, and no subset
> substitutes for a full-corpus run; shell rules (`; echo "exit:$?"`, redirect large
> output to a file); git rules (stage only your own files by name, never `git add -A`,
> `git status` after every commit — the register row OI-85 convention; the known
> working-tree carry `cowork_joint_key_chord_design.md` stays untouched; `cc_*.md` is
> gitignored — force-add this instruction in your final commit); push to `origin` (the
> user's fork) ONLY, never `upstream` — the standing hard stop, `git remote -v` first.
>
> **⚠ WITHHELD READS (blind first pass, the DT-20 discipline):** do NOT open until your
> Task-3 freeze commit exists: `DEFECT_TYPES.md`, `OPEN_ITEMS.md`, `STATUS.md`,
> `cowork_handoff.md`, every `cc_*_report.md`, `cowork_siloed_facts_audit.md`,
> `cowork_adjudication_dossier.md`, `cowork_structural_integrity_audit.md`,
> `cowork_l1_l5_premise_debt_audit.md`, `cowork_layer5_engagement_design.md`,
> `cowork_layer5_function_design.md`, `cowork_joint_key_chord_design.md` (also the
> working-tree carry — do not read or touch it), and under `tools/audit/` every
> `*dispositions*`, `*blind*`, `*errorrate*`, `*relabel*`, `*compare*`,
> `sweep_results*`, and `firerate*` file. The mandatory session-start `OPEN_ITEMS.md`
> read is deferred to Task 4 — declared here for the user; Cowork performed the
> register check for this dispatch (the layer-4 first pass is open work, nothing gates
> it). Declare in the report when each withheld file was first opened. Safe reads from
> the start: `CLAUDE.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`,
> `ARCHITECTURE.md`, the roadmap, `docs/scoring_model.md`, the layer-4 inventory
> tables under `tools/audit/l4/` (the raw row tables and `manifest.json` — scope, not
> verdicts), `cc_instruction_l4_audit_pass1.md` (the parent instruction, for
> definitions), and the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/`
> untouched. A surprise in the audited code is a finding to record; a surprise in your
> own tooling is a stop — fix the tool, restamp, rerun, never hand-edit a generated
> artifact.

## Task 0 — Preconditions

1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor d9e1912aaa HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-3 freeze.
2. Do not read the withheld files.

## Task 1 — Dispositions for every decoder row (protocol P2 + P3)

Work from the committed layer-4 inventory: every row whose file is
`chord/chordslicedecoder.h` or `chord/chordslicedecoder.cpp`. EVERY row gets a verdict
from the closed set — "no issue" is a recorded claim with a stated reason:

- causal premises: FACT (citation) / THEORY (citation answering the specific question)
  / ASSUMPTION (flag);
- derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED, under the fact-publication
  corollary — pay particular attention to everything the decoder computes per slice
  and per region that a layer above could want (candidates, alternatives, margins,
  membership, abstention reasons, per-note evidence), and record for each whether it
  survives to the decoder's output surface or dies inside;
- numeric literals and constants: ESTABLISHED (provenance) / UNFIT (hand-set) / DEAD —
  and whether each appears in `tools/param_manifest.json`;
- code rows: SURVIVES is expected throughout (this population is the engagement's
  clean target); anything that looks like it should retire instead is a finding;
- per row, the four standing questions: what does it assume, what does it publish, who
  consumes it, what happens at its edge cases (empty slices, single-note sonorities,
  symmetric chords, enharmonic spellings, abstention boundaries, region starts and
  ends, preset differences).

**The contract direction is mandatory (protocol P3):** from what `ARCHITECTURE.md`,
the roadmap's engagement stage, and `docs/scoring_model.md` say the decoder must
deliver — decode each slice against the one scorer's candidates, carry alternatives,
commit or abstain with a stated margin, and hand a governed result forward — enumerate
every expected behavior and locate it in the code, or flag the absence. An absence is
a finding of the same rank as a positive.

## Task 2 — Behavioral characterization (protocol P4)

The decoder is dormant: production fire rates are zero by construction. Characterize
it on its two reachable routes and say per row which route you used:

1. The test suites that exercise it (run them; count which branches the tests reach).
2. A full-corpus `batch_analyze --decode-chords` run over the pinned corpus
   (`c50002fee1`, Baroque preset unless a mechanism is preset-gated), writing dumps to
   scratch — NOT to `tools/corpus/`. This is a long run: let it finish; never kill it;
   no subset substitutes.

Report per mechanism/branch: fire count, population, and whether the rate matches the
documented intent — never-fires, always-fires, or a wild miss of the documented
population is a finding. Where neither route can count a branch, the row says "fire
rate not measured" with the reason.

## Task 3 — Freeze (the blinding boundary)

Write `tools/audit/l4/pass1_dispositions_decoder.csv/.json` plus the report draft;
commit as one `feat(tools):`; record the hash. THIS commit lifts the withheld list.

## Task 4 — Unblind, reconcile, report, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read —
   several existing rows concern this decoder directly; where your findings coincide,
   reference the row instead of duplicating it), `DEFECT_TYPES.md`, `STATUS.md`, and
   `cc_l4_audit_pass1_report.md` (the parent session's report).
2. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. The whole-layer signature sweep is NOT run here — it belongs to the
   layer-4 second pass after all three sessions.
3. `cc_l4_audit_pass1_decoder_report.md`: disposition summary per verdict class; EVERY
   flagged row with file, line, and one plain-language sentence for a reader who does
   not know the code; the fire-rate table with the route per row; the contract-check
   results including absences; when each withheld file was first opened. Register
   discipline: every discovered issue gets its `OPEN_ITEMS.md` row in the SAME commit
   as the report. Update `STATUS.md` (prepend) and the entry block of
   `cowork_handoff.md`. Plain language everywhere.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-11):** the Task-3 `feat(tools):` freeze,
   any behavioral-characterization `feat(tools):` if instrumentation was needed (with
   production byte-identity re-proven: standard corpus regeneration zero-diff, both
   suites green, NO golden refresh), one `docs(cc):` fold (force-add this
   instruction). Push all local commits to `origin` only, after `git remote -v`
   confirms `upstream` push is still disabled; anything that would send content toward
   `upstream` is the standing hard stop. Confirm in the report: the pushed hash,
   `upstream` untouched.

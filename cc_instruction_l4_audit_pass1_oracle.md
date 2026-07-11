# CC INSTRUCTION — Layer-4 audit, first pass, session 2 of 3: the live scoring oracle — EG-7 / OI-84 / OI-102

> **Issued by Cowork, 2026-07-11.** Second of the three sessions completing the layer-4
> first pass (register row OI-102; the decoder session is done). THIS session covers the
> live scoring oracle: `chord/chordanalyzer.cpp`, `chord/chordanalyzer.h`, and
> `chord/analysisutils.h` (~855 inventory rows, committed at `88befa3055` under
> `tools/audit/l4/`). One session follows (the formatter and satellites), then the
> whole-layer second pass. Certification is NOT decided here.
>
> **What this code is:** `analyzeChord` and its templates, score matrices, bonuses, and
> guards — the vertical scoring oracle. It is LIVE on the production path (every region
> analysis runs it) AND it is what the dormant decoder reuses, so it survives the
> engagement; the roadmap's planned split of this file rearranges it, it does not delete
> it. Two boundaries to record, not cross: rows that exist solely to serve the RETIRING
> post-scoring gates (for example the gate-context declarations in the header) get their
> verdict PLUS a note of that retirement coupling; rows about how the DECODER consumes
> the oracle were already judged in the decoder session — reference, don't re-judge.
>
> **REMINDERS (read `CLAUDE.md` in full — note it MANDATES `docs/scoring_model.md` for
> any session touching scoring logic, which this is; these are pointers):** you fix
> NOTHING — findings become register rows, never patches (guiding principle 8); you are
> an auditor, not an amender (principle 7); verify at the actual code and data, never at
> assertion (principles 15 and 19); no self-invented labels, abbreviations, numbering
> schemes, or jargon anywhere — existing repository names or plain words; run the
> self-check over every diff before reporting done (the catalog part only after the
> freeze); never stop a running process without asking the user — full-corpus runs are
> long, let them finish, no subset substitutes; shell rules (`; echo "exit:$?"`,
> redirect large output to a file); git rules (stage only your own files by name, never
> `git add -A`, `git status` after every commit — the register row OI-85 convention; the
> known working-tree carry `cowork_joint_key_chord_design.md` stays untouched;
> `cc_*.md` is gitignored — force-add this instruction in your final commit); push to
> `origin` (the user's fork) ONLY, never `upstream` — the standing hard stop,
> `git remote -v` first.
>
> **⚠ WITHHELD READS (blind first pass, the DT-20 discipline):** do NOT open until your
> Task-3 freeze commit exists: `DEFECT_TYPES.md`, `OPEN_ITEMS.md`, `STATUS.md`,
> `cowork_handoff.md`, every `cc_*_report.md`, `cowork_siloed_facts_audit.md`,
> `cowork_adjudication_dossier.md`, `cowork_structural_integrity_audit.md`,
> `cowork_l1_l5_premise_debt_audit.md`, `cowork_layer5_engagement_design.md`,
> `cowork_layer5_function_design.md`, `cowork_joint_key_chord_design.md` (also the
> working-tree carry — do not read or touch it), `cowork_gate_policy_amendment.md`, and
> under `tools/audit/` every `*dispositions*`, `*blind*`, `*errorrate*`, `*relabel*`,
> `*compare*`, `sweep_results*`, and `firerate*` file. The mandatory session-start
> `OPEN_ITEMS.md` read is deferred to Task 4 — declared here for the user; Cowork
> performed the register check for this dispatch. Declare in the report when each
> withheld file was first opened. Safe reads from the start: `CLAUDE.md`,
> `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`, the roadmap,
> `docs/scoring_model.md` (the oracle's authoritative contract — REQUIRED; it records
> historical constraints and dead ends, accepted and declared as contract, not
> findings), the layer-4 raw inventory tables and `manifest.json` under
> `tools/audit/l4/` (scope, not verdicts), `cc_instruction_l4_audit_pass1.md` (the
> parent instruction, for definitions), and the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/` reference
> artifacts untouched. A surprise in the audited code is a finding to record; a
> surprise in your own tooling is a stop — fix the tool, restamp, rerun, never
> hand-edit a generated artifact.

## Task 0 — Preconditions

1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 52064298c8 HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-3 freeze.
2. Do not read the withheld files.
3. Cross-check the row count for the three files against the inventory. If it is
   substantially larger than planned (~855) such that every-row rigor cannot fit this
   session, STOP and report with a proposed further split — never silently sample.

## Task 1 — Dispositions for every oracle row (protocol P2 + P3)

Work from the committed layer-4 inventory: every row whose file is
`chord/chordanalyzer.cpp`, `chord/chordanalyzer.h`, or `chord/analysisutils.h`. EVERY
row gets a verdict from the closed set — "no issue" is a recorded claim with a stated
reason:

- causal premises: FACT (citation) / THEORY (citation answering the specific question —
  for scoring terms, `docs/scoring_model.md` §-references count as the contract but the
  underlying musical claim still needs its FACT/THEORY/ASSUMPTION label) / ASSUMPTION
  (flag);
- derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED, under the fact-publication
  corollary — attend to what the oracle computes per candidate that consumers (the
  region path today, the decoder at engagement) can and cannot see;
- numeric literals and constants: ESTABLISHED (provenance) / UNFIT (hand-set) / DEAD —
  and whether each appears in `tools/param_manifest.json`. This file is expected to be
  dense with scoring magnitudes; classify every one, no batching by "looks similar";
- code rows: SURVIVES expected; rows serving only the retiring gates get the
  retirement-coupling note; anything that looks like it should retire outright is a
  finding;
- per row, the four standing questions: what does it assume, what does it publish, who
  consumes it, what happens at its edge cases (single-note and two-note sonorities,
  symmetric chords, enharmonic spellings, absent roots, added-tone versus extension
  readings, template ties, preset differences).

**The contract direction is mandatory (protocol P3):** from `docs/scoring_model.md`
(section by section), `ARCHITECTURE.md`, and the roadmap: enumerate every documented
template, bonus, guard, gate-input, invariant, and constraint, and locate each in the
code — or flag the absence or drift. Check the document's own sync invariants
mechanically (the template count against the declared constant; every documented term
present; every code term documented). Doc-code drift is a finding of the same rank as
a code defect.

## Task 2 — Behavioral characterization (protocol P4)

The oracle is LIVE: fire rates on the pinned corpus (`c50002fee1`, Baroque preset
unless a mechanism is preset-gated) are the real thing here, and this is the layer's
production hot path — do it properly:

1. Least-invasive first: existing dumps and diagnostics that already expose per-term
   behavior, and standalone replays through the public interface.
2. Where only instrumentation can count a branch or term: a minimal default-OFF
   counter as its own revertible `feat(tools):` commit, with production byte-identity
   re-proven — standard corpus regeneration zero-diff against the frozen corpus, both
   test suites green, NO golden refresh.
3. Where even that is disproportionate for a row: "fire rate not measured" with the
   reason — flagged, never silently skipped.

Report per mechanism/branch/term: fire count, population, and whether the rate matches
the documented intent (`docs/scoring_model.md` states intents for most terms — a term
that never fires, always fires, or wildly misses its documented population is a
finding). Full-corpus runs are long: let them finish.

## Task 3 — Freeze (the blinding boundary)

Write `tools/audit/l4/pass1_dispositions_oracle.csv/.json` plus the report draft;
commit as one `feat(tools):`; record the hash. THIS commit lifts the withheld list.

## Task 4 — Unblind, reconcile, report, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read),
   `DEFECT_TYPES.md`, `STATUS.md`, `cc_l4_audit_pass1_report.md`, and
   `cc_l4_audit_pass1_decoder_report.md`. Where a finding coincides with an existing
   register row, reference it instead of duplicating.
2. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. The whole-layer signature sweep is NOT run here — it belongs to the
   layer-4 second pass after all three sessions.
3. `cc_l4_audit_pass1_oracle_report.md`: disposition summary per verdict class; EVERY
   flagged row with file, line, and one plain-language sentence for a reader who does
   not know the code; the fire-rate table with the route per row; the full
   contract-check results including absences and drifts; when each withheld file was
   first opened. Register discipline: every discovered issue gets its `OPEN_ITEMS.md`
   row in the SAME commit as the report. Update `STATUS.md` (prepend) and the entry
   block of `cowork_handoff.md`. Plain language everywhere.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-11):** the Task-3 `feat(tools):` freeze,
   any Task-2 counter `feat(tools):` (byte-identity proven as above), one `docs(cc):`
   fold (force-add this instruction). Push all local commits to `origin` only, after
   `git remote -v` confirms `upstream` push is still disabled; anything that would
   send content toward `upstream` is the standing hard stop. Confirm in the report:
   the pushed hash, `upstream` untouched.

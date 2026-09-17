# CC INSTRUCTION — Layer-4 audit, first pass, session 3 of 3: the formatter, the path decoder, the sparse refinement, and the layer-4 types — EG-7 / OI-84 / OI-102

> **Issued by Cowork, 2026-07-11.** Last of the three sessions completing the layer-4
> first pass (register row OI-102; the decoder and oracle sessions are done). THIS
> session covers the remaining surviving in-scope files (~717 inventory rows, committed
> at `88befa3055` under `tools/audit/l4/`):
> - `chord/chordsymbolformatter.cpp` — the live shared chord-symbol formatter
>   (committed identity → display strings; chord symbols, Roman numerals, Nashville);
> - `decode/chordpathdecoder.h` — the live beam-1 commit-chain re-expression;
> - `region/sparsechordrefinement.{h,cpp}` — the live sparse-slice quality refinement;
> - the layer-4 portion of `types/analysistypes.h` (the chord types; the layer-3 types
>   were covered by the layer-3 audit — reference, don't re-judge).
> After this session the whole-layer second pass runs (catalog sweep + blind second
> reading + error rate), then the layer-4 certification decision goes to the user.
> Certification is NOT decided here.
>
> **Two boundary questions live in this scope — gather facts, do NOT decide them:**
> 1. `sparsechordrefinement` overwrites a committed layer-4 field from a resolved-key
>    concern after commit — whether that concern is owned by layer 4 or layer 5 is an
>    open register question. Audit the code as the live code it is; record what it
>    assumes, publishes, and overwrites; the ownership decision belongs elsewhere.
> 2. `chordpathdecoder.h` — whether it retires with the legacy path at the engagement
>    or survives as wider-beam scaffolding is open. Record its callers, its coupling to
>    the retiring competition versus the surviving oracle, and every fact bearing on
>    that decision; do not make it.
>
> **REMINDERS (read `CLAUDE.md` in full; these are pointers):** you fix NOTHING —
> findings become register rows, never patches (guiding principle 8); you are an
> auditor, not an amender (principle 7); verify at the actual code and data, never at
> assertion (principles 15 and 19); no self-invented labels, abbreviations, numbering
> schemes, or jargon anywhere — existing repository names or plain words; run the
> self-check over every diff before reporting done (the catalog part only after the
> freeze); never stop a running process without asking the user — full-corpus runs are
> long, let them finish, no subset substitutes; shell rules (`; echo "exit:$?"`,
> redirect large output to a file); git rules (stage only your own files by name, never
> `git add -A`, `git status` after every commit — the register row OI-85 convention;
> the known working-tree carry `cowork_joint_key_chord_design.md` stays untouched;
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
> `*compare*`, `sweep_results*`, and `firecount*`/`firerate*` file. The mandatory
> session-start `OPEN_ITEMS.md` read is deferred to Task 4 — declared here for the
> user; Cowork performed the register check for this dispatch. Declare in the report
> when each withheld file was first opened. Safe reads from the start: `CLAUDE.md`,
> `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`, the roadmap,
> `docs/scoring_model.md`, the layer-4 raw inventory tables and `manifest.json` under
> `tools/audit/l4/` (scope, not verdicts), `cc_instruction_l4_audit_pass1.md` (the
> parent instruction, for definitions), and the source code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/`
> untouched. A surprise in the audited code is a finding to record; a surprise in your
> own tooling is a stop — fix the tool, restamp, rerun, never hand-edit a generated
> artifact.

## Task 0 — Preconditions

0. **First action — commit Cowork's waiting register edits** (content is Cowork's,
   summarized here: the OI-109 adjudication — the register row is the marker
   question's one home, the scoring question parked to the precision phase — and the
   new OI-110 row tracking the oracle instrumentation's keep-or-revert lifecycle).
   Stage WITHOUT opening the register:
   ```
   git add OPEN_ITEMS.md
   git add -f cc_instruction_l4_audit_pass1_satellites.md
   git commit -m "docs(cowork): OI-109 adjudicated (marker re-point + scoring question parked) + OI-110 instrumentation lifecycle + the layer-4 session-3 instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining entries: the known carry plus
   untracked scratch only; anything else, stop and report.
1. Check the git state WITHOUT displaying commit messages:
   `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor ac945e23c6 HEAD; echo "exit:$?"` — the second must
   print `exit:0`. No `git log` in any form until after the Task-3 freeze.
2. Do not read the withheld files.
3. Cross-check the row count for the scope against the inventory; if every-row rigor
   cannot fit this session, STOP and report with a proposed split — never silently
   sample.

## Task 1 — Dispositions for every row in scope (protocol P2 + P3)

EVERY inventory row for the files above gets a verdict from the closed set — "no
issue" is a recorded claim with a stated reason:

- causal premises: FACT (citation) / THEORY (citation answering the specific question)
  / ASSUMPTION (flag) — the formatter encodes notation conventions (symbol spelling,
  Roman-numeral figures, Nashville numbering): label the load-bearing ones;
- derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED, under the fact-publication
  corollary;
- numeric literals and constants: ESTABLISHED (provenance) / UNFIT (hand-set) / DEAD —
  and whether each appears in `tools/param_manifest.json`;
- code rows: SURVIVES expected; for the two boundary files, add the boundary facts
  (callers, coupling direction, what is overwritten or re-expressed) to the row notes;
- per row, the four standing questions: what does it assume, what does it publish, who
  consumes it, what happens at its edge cases (for the formatter: enharmonic
  spellings, slash chords, altered and added tones, minor-key Roman numerals,
  half-diminished symbols, empty or sparse identities; for the types: default values,
  invariants, which fields cross layer boundaries).

**The contract direction is mandatory (protocol P3):** from `ARCHITECTURE.md`, the
roadmap, and `docs/scoring_model.md` where they speak about these files: enumerate
every expected output and behavior and locate each — or flag the absence. For the
formatter specifically: every committed-identity shape the oracle can produce must
have a defined rendering — enumerate the identity space at the contract level and
check the formatter covers it; an unrenderable or silently-mangled identity class is a
finding.

## Task 2 — Behavioral characterization (protocol P4)

All four scopes are LIVE (the formatter on the notation render and batch output
paths; the path decoder and the sparse refinement on the region path). Fire rates on
the pinned corpus (`c50002fee1`, Baroque unless preset-gated): least-invasive routes
first — existing dumps, the batch output itself (the formatter's outputs are directly
observable in the corpus artifacts), standalone replays; a minimal default-OFF counter
only where nothing else can count, as its own revertible `feat(tools):` commit with
production byte-identity re-proven (standard corpus regeneration zero-diff, both
suites green, NO golden refresh); "fire rate not measured" with the reason where even
that is disproportionate. A mechanism that never fires, always fires, or wildly
misses its documented population is a finding. For the sparse refinement, report
separately how often each of its two entry points fires and how often it actually
changes a committed quality.

## Task 3 — Freeze (the blinding boundary)

Write `tools/audit/l4/pass1_dispositions_satellites.csv/.json` plus the report draft;
commit as one `feat(tools):`; record the hash. THIS commit lifts the withheld list.

## Task 4 — Unblind, reconcile, report, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read —
   the boundary questions above have existing rows; where your findings bear on them,
   reference and enrich, don't duplicate), `DEFECT_TYPES.md`, `STATUS.md`,
   `cc_l4_audit_pass1_report.md`, and the two earlier session reports.
2. Any NEW problem TYPE is promoted into `DEFECT_TYPES.md` in the same commit as the
   report. The whole-layer signature sweep is NOT run here — it is the next
   instruction.
3. `cc_l4_audit_pass1_satellites_report.md`: disposition summary per verdict class;
   EVERY flagged row with file, line, and one plain-language sentence; the fire-rate
   table with the route per row; the contract-check results including the formatter
   coverage statement; the gathered boundary facts for the two open questions (facts,
   not decisions); when each withheld file was first opened. Register discipline:
   every discovered issue gets its `OPEN_ITEMS.md` row in the SAME commit as the
   report. Update `STATUS.md` (prepend) and the entry block of `cowork_handoff.md`.
   Plain language everywhere. This completes the layer-4 first pass: say so plainly,
   and say equally plainly that certification awaits the second pass.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-11):** the Task-0 commit, the Task-3
   `feat(tools):` freeze, any Task-2 counter `feat(tools):` (byte-identity proven),
   one `docs(cc):` fold (force-add this instruction). Push all local commits to
   `origin` only, after `git remote -v` confirms `upstream` push is still disabled;
   anything that would send content toward `upstream` is the standing hard stop.
   Confirm in the report: the pushed hash, `upstream` untouched.

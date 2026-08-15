# CC dispatch — the period-split tool with its check, then the July screen over the pre-S4 specification-bearing candidates

> **Status: ACTIVE DISPATCH, written 2026-08-15 (Cowork), at a verified STOP** — the candidate
> pass (`cc_instruction_evidence_candidate_pass.md`) completed 2026-08-14, its close appended to
> `cowork_away_returns.md` and read by the writing side in full (Ruling 15 of the eighteenth
> stop). Nothing is running.
>
> **★ THE RULINGS THIS DISPATCH APPLIES, QUOTED IN FULL (D-643).** From
> `cowork_rulings_2026_08_15_period_start.md`: *"The restructuring period opens EXCLUSIVE at
> commit `b006dc15b5f696f2fc86ad72b97fae58d2119cd7`"*, and the second ruling adopting the
> surface's recommendation verbatim: *"(1) A1's split re-derived by a checked tool; (2) the July
> screen — the pre-S4 specification-bearing flagged hunks read individually, with the
> falsification rule stated now: if any shows a code-influenced correction, the period question
> RE-OPENS."* And from `cowork_rulings_2026_08_13_eighteenth_stop.md`, Ruling 5, because the
> screen judges influence: *"ALL EVIDENCE MUST BE RESTORED. The restoration test is **not
> *copied from the implementation*** — that is useless, since nobody pasted code into a
> specification. It is **whether any fact in the code influenced the change**. Influence is
> **invisible in the text**: a narrowed rule reads exactly like a rule that was always narrow."*
> Its §3 also binds: *"**No repair is authorized.**"* — this dispatch screens and reports; it
> repairs nothing.
>
> **Read IN FULL, and read FIRST:** `cowork_rulings_2026_08_15_period_start.md`;
> `ratification_surfaces/cowork_restructuring_period_start_decision_surface.md`;
> `cowork_rulings_2026_08_13_eighteenth_stop.md`; `tools/audit/doc_change_candidates.json`'s
> summary surface (the hunk file `tools/audit/doc_change_candidates_hunks.jsonl` is data, read by
> the tool).
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_period_checks.md`. Acts dated from the
> clock; no positional count anywhere; cite rulings by number or by their record's file name.
>
> **★ All standing rules as adopted.** D-253 in every dialect — working-tree reads through the
> file tools; historical content through git object queries by explicit hash only. NO TRANSCRIBED
> VALUES (D-431) — every count enters reports by citation to a generated artifact; the
> predictions in §0a are registered expectations, not values, and carry no authority.
> Hold-don't-guess. **NO `src/` EDIT — no ruling permitting a named act is granted by this
> dispatch, and none is implied.** No golden, no test changed, no corpus of scores, nothing under
> `tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis, no design. **No edit
> to any screened document.** D-231 and #8 stand. **Phase 1's completion statement is not
> written, not drafted and not partially written.** Commit and push per task boundary; `origin`
> only.

## 0a. THE PREDICTIONS, REGISTERED BEFORE ANYTHING RUNS (#17b)

**P1 — the split.** Cowork derived, by an ad-hoc script over staged snapshots (a declared
departure, recorded on the decision surface as assumption A1), flagged hunks by stratum:
S1 705, S2 378, S3 1,279, S4 19,836; and the specification-bearing slice (roles `governing` +
`specification-or-docs`) by stratum: S1 22, S2 17, S3 28, S4 247. **Moderate confidence the
checked tool reproduces these exactly**, since both derive from the same artifacts. **A
difference is a FINDING, reported with the per-cell diff — never reconciled silently, and never
resolved in favour of Cowork's numbers, which carry no authority.**

**P2 — the screen.** The screen population is the pre-S4 specification-bearing flagged hunks
(67 if P1 holds; the tool's own count governs). **Prediction — moderate confidence: the large
majority classify as RATIFIED-ACT EDIT or RESTRUCTURING-SHAPED, and ZERO classify POSITIVELY
CODE-INFLUENCED.** Ground: the July weeks were dominated by user-ratified, measured acts (the
mode-grading consolidation 07-13, the signature-mask fix 07-14, the joint-estimator adoption
07-26, the notation switch 07-27), and the instruction directing correction against the code
(D-231's truth half) did not exist before `b006dc15b5`. **What would refute it:** one hunk whose
change, or whose commit's own account, states or shows correction against the implementation.
**Refutation fires the ruled falsification rule — the period question re-opens — and the screen
COMPLETES either way**; the re-opening is the user's act on the report, never this dispatch's.

**What the screen cannot settle, stated in advance so the result is not over-read:** a clean
screen does not establish the July strata pollution-free — Ruling 5 says influence is invisible
in the text, so the screen finds only POSITIVE evidence of influence, and its clear verdicts are
bounded by that. The UNDETERMINED class exists for exactly this reason and is reported, never
argued down.

## 0b. THE PREMISE LEDGER (#17a)

**FACT — read at the artifact:** `tools/audit/doc_change_candidates.json` and
`tools/audit/doc_change_candidates_hunks.jsonl` exist, self-reproduce via
`python tools/audit/gen_doc_change_candidates.py --check`, and carry stratum per commit (the
`commits` table) and role + verdict per hunk. **FACT — read at the ruling record:** the period
opens exclusive at `b006dc15b5f696f2fc86ad72b97fae58d2119cd7`. **FACT — carried caveat:** the
generator that produced both input artifacts is itself unestablished (#19, the fourteenth
handoff block); the new tool INHERITS that caveat and must state it in its own artifact.

**ASSUMPTION — each checked BEFORE the act resting on it; a refutation is a STOP.**

- **A1.** The hunk file's `role`, `v` and per-commit stratum fields suffice to derive the split
  and the screen population mechanically. *Check: the tool derives the population and publishes
  it whole; a hunk missing any needed field is a STOP, never skipped.*
- **A2.** Every screened hunk's old and new text is retrievable at its recorded coordinates —
  `git show <parent-sha> -- <path>` and `git show <child-sha> -- <path>` at the `-U0` header's
  ranges, the artifact's own retrieval note. *Check: per hunk; one that does not resolve is
  reported per hunk with its coordinates, and the screen continues over the rest.*
- **A3.** The screen's four classes are decidable from the hunk text, the commit's subject and
  the record's account of the commit's act — never from memory of what July's work was. *Check:
  every RATIFIED-ACT verdict cites the ratified act AND where its ratification is recorded;
  every verdict names its ground; a hunk supporting no ground goes to UNDETERMINED.*

## 0c. THE TASKS, IN ORDER

**Task 1 — the checked tool (A1).** Write `tools/audit/gen_period_stratum_split.py`, writing
`tools/audit/period_stratum_split.json`. Inputs: the two candidate artifacts, whose file hashes
are recorded in the output. It publishes: flagged hunks by stratum × role; the
specification-bearing slice per stratum; the in-period / pre-period split under the ruled start
commit, which it names by full hash; and **the screen population for Task 2, enumerated whole by
hunk identity** (commit sha, file path, hunk header). It carries a `--check` mode that
re-derives the output from the inputs and exits non-zero on any drift, and its artifact states
the inherited #19 caveat in its own words. Grade P1, with the per-cell diff if refuted. Commit
and push.

**Task 2 — the July screen (A2, A3). Read-only on history; it edits nothing it screens.** For
every hunk in Task 1's published screen population, retrieve the old and new text at the parent
and child commits by explicit hash and classify into EXACTLY ONE: **RATIFIED-ACT EDIT** (
positively tied to a named user-ratified act, the act and its ratification's recorded place both
cited); **RESTRUCTURING-SHAPED** (relocation, split or growth with no reference to the code in
the change or in its commit's account); **POSITIVELY CODE-INFLUENCED** (the change or its
commit's own account states or shows correction against the implementation); **UNDETERMINED**
(no ground establishable — NOT cleared, per Ruling 5's invisibility clause). Deliverables:
`tools/audit/july_screen.json` (a verdict per hunk with its ground and citations) and the
readable `tools/audit/july_screen_report.md` — **a verdict per hunk, never an edit to any
screened document**. If any hunk is POSITIVELY CODE-INFLUENCED: complete the screen, then mark
the falsification at the TOP of the report and in the close — the period question re-opens and
that is the user's act. Grade P2. Commit and push.

**Task 3 — the close.** One `STATUS.md` pointer entry per task, nothing else in that file.
Append the close to `cowork_away_returns.md`. Report at the objects, with commit hashes.

## 0d. WHAT IS DELIBERATELY NOT DONE

**No repair** — nothing is restored, reverted, reconciled or corrected in any screened document,
in any specification, or anywhere else; the eighteenth stop's §3 stands whole. **No open-items
row is marked, flipped or discarded** — Ruling 13's marking runs after these checks and is not
this dispatch's. **No register entry is written** — the decisions register is under the
filtering ruling. **The phases are not defined and D-231 is not rephrased** — this dispatch
neither needs nor touches them, and the bar on correcting any document on the ground that the
code says otherwise is untouched by everything here. OI-179 stays OPEN and GATES.

## 0e. STOP RULES

Halt with a STOP in `cowork_away_returns.md` if: the screen POPULATION itself cannot be derived
(A1 refuted — a per-hunk retrieval failure is reported per hunk and is NOT a halt); the new
tool's `--check` cannot reproduce its own output; Task 1's split disagrees with the input
artifact's own published totals (its `flags_by_document_role` and `flags_by_stratum`) in a way
that publishing the diff cannot express; any act would require editing a screened document,
`src/`, or a scoring value; or a guard goes red for a cause that is neither this dispatch's own
edits nor already recorded — the recorded standing reds are not that.

---

*Provenance: Cowork, 2026-08-15. Executes the second ruling of
`cowork_rulings_2026_08_15_period_start.md`, taken on
`ratification_surfaces/cowork_restructuring_period_start_decision_surface.md` ("B", then "as per
your recommendation"). Form taken from `cc_instruction_scoring_model_pass.md`, read in full
before writing. Self-check run before release (D-434).*

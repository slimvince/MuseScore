# CC dispatch — principle #10 gains its purpose, and the worth test is applied to the three rows that prompted it

> **Status: ACTIVE DISPATCH, written 2026-08-11 (Cowork), at a verified STOP** — the previous
> batch completed, five commits, verified by Cowork at the objects: the union of changed paths
> across all five carries no `src/`, no `tools/corpus/`, no `tools/robust_stop/` and no golden;
> OI-372, OI-373 and OI-374 landed with their detail files in the same commits; the twenty-five
> lapse records written. Nothing is running.
>
> **Read IN FULL, and read FIRST:** `cowork_rulings_2026_08_11_sixteenth_stop.md` (Ruling 68,
> WHOLE, D-643); `CLAUDE.md`'s principle #10 as it now stands and R3 at
> `cowork_audit_protocol.md`; `OPEN_ITEMS.md` (INDEX); `DECISIONS.md` (INDEX).
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_worth_test.md`. Acts dated from the
> clock; commit messages via `-F`; identifiers and ruling numbers verified at their own indexes
> immediately before being written.
>
> **★ All standing rules as adopted.** D-253 in every dialect and mechanism. NO TRANSCRIBED
> VALUES (D-431). Hold-don't-guess. **Read-only on the analysis: no behaviour change, no `src/`
> edit, no golden, no corpus of scores, nothing under `tools/corpus/` or `tools/robust_stop/`,
> no fix to inference, no design.** D-231 and #8 stand. **Phase 1's completion statement is not
> written, not drafted and not partially written.** Commit and push per task boundary; `origin`
> only, NEVER `upstream`.

## 0a. WHAT THIS DISPATCH IS FOR, AND WHAT IT DELIBERATELY IS NOT

It writes Ruling 68 into principle #10, enters it in the decisions register, and applies the
worth test to **exactly three rows** — the ones the batch that prompted the ruling created.
**It does NOT run the test over the open population.** A sweep would be documentation spending
of precisely the kind the ruling exists to stop, and the ruling says in terms that what the test
does to rows already on the books is a separate act.

## 0b. THE RULING LEDGER

**Ruling 68 is carried in full at `cowork_rulings_2026_08_11_sixteenth_stop.md` and is not
restated here (#6).** Read it whole before acting (D-643). **The ruled amendment text is the
user's and is written VERBATIM, never paraphrased or improved**, with #10's former wording
preserved in place (#12).

## 0c. THE PREMISE LEDGER (#17a)

**FACT — verified by Cowork at the objects.** The previous batch's five commits, their union of
changed paths, and their push state, read as git objects by explicit hash. The substring first
cut at `tools/audit/gen_nongating_apparatus_rows.py:1175`, read at the code. Principle #10's
current five-word text, read at `CLAUDE.md`. R3's mandatory-row clause, read at
`cowork_audit_protocol.md`.

**ASSUMPTION — each checked BEFORE the act resting on it; a refutation is a STOP.**

- **A1.** Ruling numbers: the fifteenth stop carried 65 and 66, Ruling 67 is carried at
  `cc_instruction_resume_lapse_records.md` §0a, so this is 68. *Check at the records; correct
  rather than propagate.*
- **A2.** **DISCARDED's representation is settled by the record, not invented.** It is a terminal
  state WITH provenance — the finding, its date and the reason — and is therefore not the same as
  RESOLVED, which claims something was done. *Check, before writing any row: establish at rule
  (f)'s home (`tools/audit/index_status_lint.py`) and at the one index parser whether DISCARDED
  must be a canonical opening token, or whether it is representable within the existing
  vocabulary plus a derived field, as `owed` proved to be. **If the record does not settle it,
  STOP.** Do not invent a token and do not assume one is unnecessary.*
- **A3.** The three rows are tested individually and the test's answer is written per row, with
  the consumer named or its absence stated. *Check: no row is discarded by class or by batch.*
- **A4.** **#19's carve-out is applied first, per row.** A row carrying an establishment
  obligation is never discarded whatever its subject. *Check: stated per row, before its worth
  verdict.*
- **A5.** The cheap-look branch is honoured. *Check: for any of the three whose consumer can
  neither be named nor cheaply established, it is looked at ONCE, cheaply, and the result
  recorded — it is neither discarded nor left as an obligation without that look.*

## 0d. THE TASKS, IN ORDER

**Task 1 — the amendment and its entry. FIRST, atomic under the decisions register's rule (c).**
Write the ruled text into principle #10 verbatim, former wording preserved in place. Enter Ruling
68 in the register through the backbone data and the generator, never by hand-editing a rendered
file. Record at R3 that its mandatory-row clause is superseded for the discarded class and
otherwise untouched — a pointer, not a copy (#6). Commit the ruling record with it. Then
`gen_decisions_register.py --check` and `gen_cluster_dispositions.py --verify`, re-aiming any
drifted citation per citation. Commit and push.

**Task 2 — the worth test applied to three rows (A2, A3, A4, A5).** The three are **OI-372**
(the guard tool's tail window), **OI-373** (the guard-set runner's exit) and **OI-374** (the guard
artifact's captured text following the environment). For each, in this order: the #19 check; then
name the analysis decision that consumes it, or state that none does and why; then the verdict.
**A verdict of WORTH FIXING for any of them is a correct outcome, not a failure of this dispatch**
— the test is being applied, not confirmed. Whatever the representation question in A2 returns,
apply it. Commit and push.

**Task 3 — the close.** One `STATUS.md` pointer entry per completed task and nothing else in that
file, which remains unreadable and whose row OI-370 stays open and gates. Append the close to
`cowork_away_returns.md`. Report at the objects: commits and push state, A2's finding, and the
three per-row verdicts with their reasons.

## 0e. STOP RULES

Write a STOP into `cowork_away_returns.md` and halt if: the ruling numbers are wrong; A2's
representation question is not settled by the record; a row carries an establishment obligation
and the worth test would otherwise discard it; a row's consumer can neither be named nor cheaply
established and the cheap look does not settle it; or a guard goes red for a cause that is
neither this dispatch's own edits nor already recorded in the register or the returns file.

---

*Provenance: Cowork, 2026-08-11, at the verified STOP following the previous batch, written from
all present knowledge with nothing running. The standing writing-side self-check was run against
this file's own text before release (D-434).*

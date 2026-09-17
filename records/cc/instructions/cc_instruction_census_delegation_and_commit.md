# CC dispatch — the census delegation, two declines, and the outstanding commits

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_census_delegation_and_commit.md`.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231. The freeze holds.
>
> **★ PHASE 1's COMPLETION STATEMENT IS NOT WRITTEN HERE.** OI-336 is unruled and untouched.

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04.** **Widen the existing `ARCHITECTURE.md` §8c pointer to
  `cowork_score_census.md` so it names the sections the six entries sit in.** Not a document-level
  pointer: the census is a findings document with a few rule-stating blocks, and naming the sections
  says exactly that, while a document-level delegation would assert the whole census is the
  authoritative detail for its scope — a stronger claim than the record makes.
- **R2 — RULED, same act.** **Do NOT widen the `cowork_voiceleading_axis_design.md` delegation** to
  reach §15 and §16. The three entries **stay `gap`**, and the reason is recorded: D-397 and D-400
  **are** ratification asks A7 and A5 put to the user, and D-398 sits in a tracking list — an ask is
  not a rule, and forcing it a contract home would misdescribe it. The kind half would exclude both
  sections at the next run in any case, so a widening would be a wording change that closes nothing.
- **R3 — RULED, same act.** **No delegation is drafted or written for
  `cowork_structural_integrity_audit.md`.** The register's own `not_write_list_cases` already rules
  it — a delegation cannot repair that class, and the remedy is at the document. Recorded for
  completeness of the class, not as a proposal.
- **R4 — RULED, same act.** **Commit the outstanding waves** — the phase-1 completion inventory and
  the delegations-and-corrections wave — together with this one, as provenance-stamped commits, with
  the guards re-run at the committed tree. Two waves uncommitted is the OI-285 class, and this
  dispatch authorizes the commit explicitly rather than presupposing one.

**None of R1–R4 authorizes a fix to the analysis, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session:**

- **F1.** The six entries are D-359…D-364 and the artifact enumerates the sections they sit in,
  beginning §1 (*"Why corpora kept being 'discovered' — and the method that closes it"*) and §3
  (*"Inclusion criteria"*) — `tools/audit/decisions/outstanding_delegations.json:514-535`.
- **F2.** `ARCHITECTURE.md:317-319` already delegates the licence-pool constraint to
  `cowork_score_census.md` **§8c** — so the home is one the record means to keep, and what is missing
  is reach.
- **F3.** D-397 and D-400 are §16's ratification asks **A7 and A5**; D-398 sits in §15, *"Open items &
  deferred refinements"* — same artifact, `:596-625`.
- **F4.** The audit case carries **no draft by design**, on the register's own `not_write_list_cases`
  ruling — same artifact, `:592`.

**ASSUMPTION — checked before the act it licenses:**

- **A1.** That the six entries sit **only** in the sections Cowork read. **Cowork read a truncated
  block** — §1 and §3 were visible and the enumeration continued past what was read. → **Task 1.1**:
  enumerate every section holding one of the six **before** the widening names any.

## 1. Task 1 — Write the census delegation (R1)

**1.1 Discharge A1.** Enumerate, from the artifact, **every** section holding one of D-359…D-364.
Report the full set. **Do not widen to a set Cowork named** — widen to the set the data gives.

**1.2** Widen the existing §8c pointer at `ARCHITECTURE.md` to name that full set, in the form the
document already uses. **Report the wording verbatim** so the user can correct it; it is one line and
revertible.

**1.3** Record in the clause that the delegation half is what this closes, and that **D-430's kind
half is then judged per section and is not pre-judged by the widening** — a named section that records
findings still admits nothing.

**1.4** Re-run the classification and report what actually moves. **If nothing moves, say so** — it
would mean every named section fails the kind half, which is a finding about the census rather than
about the delegation.

## 2. Task 2 — Record the two declines (R2, R3)

**2.1** Record R2 at the voice-leading document's write-list row and on the affected entries: the
delegation is **not** widened, the three entries stay `gap`, and the reason is that §16 holds
ratification asks put to the user and §15 is a tracking list. **This is a ruling, not a deferral** —
say so, so a later wave does not read it as owed work.

**2.2** Record R3 likewise: no delegation for the structural-integrity audit, on the register's
existing ruling, with the remedy named as being at the document.

**2.3** Update `outstanding_delegations.json`'s classes to reflect both rulings — **derived, not
hand-marked** (D-640: the list is kept and its state is derived).

## 3. Task 3 — Commit (R4)

Verify what is uncommitted through `tools/audit/changed_paths.py`. **If anything is modified outside
the three waves named in R4, STOP and report.** Commit by git plumbing, and **re-run every guard at the
committed tree** with the list `gen_guard_state.py` derives.

`STATUS.md` gains one POINTER entry covering all three waves.

## 4. Task 4 — Close

Run `tools/audit/process_check.py` over this dispatch. Re-aim any anchor this wave's edits drift, per
citation. Report the guard state at the committed tree and **fix nothing**.

**Still owed and NOT in this dispatch:** OI-336 (unruled), the COMPLETE half's remaining homing and
defense gaps, the TRUE half's gating rows, and phase 1's completion statement.

## 5. Accepted outcomes

**Task 1.1 finding more sections than Cowork read is expected** — that is why A1 is an assumption.
**Task 1.4 moving nothing is a result**, and a finding about the census rather than a failure of the
widening.

## 6. Self-check (D-434) — run by Cowork before release

- **Ruling ledger.** Four rulings, with R2 and R3 stated as **rulings rather than deferrals** so
  neither reads as owed work later.
- **#17(a).** Four facts read at the artifact and the canonical document. One assumption, and it
  exists because Cowork read a truncated block and would otherwise have named a section set from a
  partial read — the exact failure this arc keeps producing.
- **Principles.** #12 — nothing deleted; the declines are recorded with their reasons. D-640 — the
  write-list state is derived, never hand-marked. Rule (g) — the delegation is written on the user's
  ruling and reported verbatim for correction. D-599 — no alternatives offered where the principles
  decide.
- **R4 is explicit.** The previous dispatch presupposed a commit it never authorized; this one
  authorizes it in the ledger.

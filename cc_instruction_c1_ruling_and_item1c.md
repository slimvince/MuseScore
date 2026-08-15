# CC dispatch — the C1 ruling on its real basis, the full-quote rule, and item 1 continued

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_c1_ruling_and_item1c.md`.
>
> **★ D-641 GOVERNS.** Findings bearing on the analysis, its inputs, or a measurement instrument are
> **surfaced**; anything else is **rowed and left — no wave, no fix.**
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231.
>
> **★ THE FINISH LINE IS THE SCOPE.** Item 1 only. Item 2 is not started. Phase 1's completion
> statement is not written, drafted, or partially written.

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04. C1 reaches every decision whose content is LIVE.** A
  superseded decision's live content lives in its **successor**; C1 is satisfied for that content
  **when the successor is homed**, and the superseded entry itself is recorded in the register, which
  D-231 makes the status ledger for supersession. **Where the successor is NOT homed, C1 is defeated
  and the owed act is homing the SUCCESSOR — not the superseded entry.**

  **★ ITS BASIS, AND THE WITHDRAWAL.** R1 rests on **D-231's own clause, quoted in full below**. The
  previous dispatch called it an application of **OI-272's per-kind scheme; that reading is
  WITHDRAWN.** CC's refutation stands: the scheme partitions by what a decision **is**, not by its
  status, so class 1 claims these entries and routes them the opposite way; its prescribed home
  differs; its tried-and-closed pointer would state something false; and it carries no
  homed-successor condition. Record the withdrawal — a wrong basis retracted is #12 evidence.

- **R2 — RULED, same act. THE FULL-QUOTE RULE.** A claim that invokes a ruling **as an application**
  must **quote that ruling in full**, not the branch that supports the claim. **Its measured
  instance:** the OI-272 reading cited the class about shelvings and dead ends and never put class 1
  on the page — and class 1 is the branch that decided the case the other way.

- **R3 — RULED, same act.** Apply R1 to item 1's no-home class, then continue the re-home class as
  capacity allows.

**None of R1–R3 authorizes a fix to the analysis, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session. Quoted in full per R2:**

- **F1.** `CLAUDE.md:1115-1121`, D-231's phase-1 clause, entire:

  > **Phase 1 — the specifications are made COMPLETE and TRUE:** every recorded decision is written
  > into its owning specification (the homing acts), with its defense, so that conformance is
  > thereafter measured against the specifications themselves — the decisions register remains the
  > status ledger (supersession, shelving, the same-commit rule), never the conformance reference;
  > and the specification text is corrected wherever it states something false at HEAD (the doc-sync
  > debt), because a specification cannot be the compliance standard while it misdescribes the code.

  **What R1 takes from it:** the clause assigns **supersession to the register** and **conformance to
  the specifications**, naming supersession and shelving as two distinct things the register is ledger
  of. A superseded decision is not something conformance is measured against.

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That OI-340 records the refutation as the session report describes. **Cowork has not read
  OI-340.** → **Task 1.1**.
- **A2.** That every member of item 1's no-home superseded class **has a homed successor**. **This is
  not established** — the routes artifact gives a reason per entry, and Cowork has read four of them.
  **R1's application turns on it per entry.** → **Task 2.1**, and an entry whose successor is unhomed
  does **not** leave the item; it changes route.

## 1. Task 1 — Record R1 and R2

**1.1** Discharge A1: read OI-340 and confirm it records the refutation. Report any divergence.

**1.2** Record R1 where the C1 criteria live, quoting F1's clause rather than paraphrasing it. Record
the **withdrawal** of the OI-272 basis in the same place, with CC's four grounds preserved (#12).
**Flip OI-340.**

**1.3** Home **R2** in `cowork_audit_protocol.md`'s dispatch-protocol section beside D-431, D-434,
D-436, D-640 and D-641, with a register entry in the same commit. State its measured instance.

## 2. Task 2 — Apply R1 to the no-home class

**2.1 Discharge A2 per entry.** For each superseded member: name its successor, and establish
**whether that successor is homed**, from the register data.

**2.2** An entry whose successor **is homed** is **correctly homed already** — register plus the
successor's home — and leaves item 1. Record the successor and its home, derived.

**2.3** An entry whose successor is **NOT homed** stays in item 1, **with its route changed to
"home the successor"**. Report these separately; they are real work, not bookkeeping.

**2.4** Report how many entries leave, how many change route, and how many neither.

## 3. Task 3 — Continue the re-home class

Home entries whose owning specification is unambiguous, each written into the specification **in its
own voice, with its defense**, verbatim and home re-taken, former preserved (#12).

**Do not name a former-home document by filename in `ARCHITECTURE.md`** — a filename there reads as a
new naming and moves a measured population by the act of recording provenance. Provenance goes in the
register field.

**OI-342 is relevant and not to be worked around:** the `owner_is_unambiguous` column is carrying
"outside this dispatch's edit surface" for some rows, which the artifact has a separate field for.
**Read the owner judgment itself, not the column**, and report if the two disagree.

Where the owning specification is not unambiguous, **do not guess** — report it in the residue.

## 4. Task 4 — Close

Guards at the committed tree with the list `gen_guard_state.py` derives; report and **fix none**.
Re-aim any anchor this wave's edits drift, per citation. Verify what is committed through
`tools/audit/changed_paths.py`. Run `tools/audit/process_check.py` over this dispatch. `STATUS.md`
gains one POINTER entry. Report item 1's remaining population by route.

## 5. Accepted outcomes

**A2 finding unhomed successors is expected and is the useful part** — it converts a bookkeeping flip
into named work. **A short Task 3 is acceptable.** **OI-342's column disagreeing with the underlying
judgment is a result**, and reporting it beats correcting a count.

## 6. Self-check (D-434) — run by Cowork before release

- **R2 applied to this dispatch.** F1 quotes D-231's phase-1 clause **entire**, including the half
  that does not help R1, and states what R1 takes from it separately from the quote.
- **Ruling ledger.** R1 carries its own withdrawal — the basis previously claimed is retracted in the
  ruling that replaces it, rather than quietly dropped.
- **#17(a).** One fact, quoted in full. Two assumptions — A1 because Cowork has not read the row it
  cites, A2 because Cowork read four entries of a class and R1's application turns on all of them.
- **Principles.** #6 — R1 refuses a second copy of a homed rule. #12 — the withdrawn basis and its
  grounds are preserved. C4 — re-homing preferred because the specifications must suffice without the
  register.

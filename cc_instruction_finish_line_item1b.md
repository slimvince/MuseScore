# CC dispatch — the C1 ruling for superseded entries, the yield-artifact classification, and item 1 continued

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_finish_line_item1b.md`.
>
> **★ D-641 GOVERNS.** A finding bearing on the analysis, its inputs, or an instrument a measurement
> depends on is **surfaced**; anything else is **rowed and left — no wave, no fix.**
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231.
>
> **★ THE FINISH LINE IS THE SCOPE.** Item 1 only. Do not start item 2. Phase 1's completion
> statement is not written, drafted, or partially written.

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04.** **C1 reaches LIVE decisions.** For a **superseded** entry
  whose live content is carried by a homed successor, the home is **the register plus the successor's
  home** — writing it into a specification would be a second copy of a rule the successor already
  states (#6). This applies **OI-272's per-kind scheme** to the superseded kind; it is an application,
  not a new rule.
- **R2 — RULED, same act.** The read-wave **yield artifacts are checked against R4's classification**
  before the re-homing continues. R4's ruled form: *a tool that re-derives a live invariant belongs in
  the guard list; a tool that records a measurement taken at a point in time does not.* **A
  point-in-time measurement leaves the live list**, artifact preserved and marked historical.
- **R3 — RULED, same act.** **Continue item 1's re-home class**, as capacity allows after R1 and R2.
  Report the remainder.

**None of R1–R3 authorizes a fix to the analysis, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session:**

- **F1.** `tools/audit/decisions/finish_line_item1_routes.json:168-201` records the superseded class
  and its reason per entry: D-282's live content carried by D-115/D-191, D-283's by D-001/D-096,
  D-284's by D-036 with D-001/D-010, D-285's by the ratified factorization emission design — each
  homed, so re-homing would duplicate (#6).
- **F2.** `OPEN_ITEMS.md`'s OI-272 row states the per-kind scheme: live constraints and policies homed
  into the owning specification; **shelvings, falsifications and dead ends NEVER become live
  specification statements — home is the register plus the evidence document, with a one-line
  tried-and-closed pointer in the owning spec**; process rules to `CLAUDE.md` or the audit protocol;
  measurement conventions to the gate block.
- **F3.** `robust_stop_diff.py` returns **OVERALL PASS** against the committed reference after the
  dumps were moved — run by Cowork this session.

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That the three failing read-wave yield artifacts are **point-in-time measurements** sitting
  on R4's live side. Cowork has this from a session report plus its own inference. → **Task 2.1**.
- **A2.** That OI-272's per-kind scheme **reaches the superseded kind**, which F2's text does not name
  literally — it names shelvings, falsifications and dead ends. **This is Cowork's reading, put to the
  user and agreed.** → **Task 1.1**: verify the ruling's own text and, **if it will not carry the
  superseded kind, STOP and report** rather than stretching it.

## 1. Task 1 — Apply R1 (and check A2 first)

**1.1** Read OI-272's ruling at its own text. Report whether it carries the superseded kind. **If it
does not, STOP** — R1 would then be a new ruling rather than an application, and that is the user's.

**1.2** Apply R1 to item 1's **no-home** class: an entry whose live content is carried by a **homed**
successor is **correctly homed already** — register plus successor — and leaves the outstanding
population. Record per entry the successor and its home, derived, not asserted.

**1.3** Where the owning specification would benefit, note the **one-line tried-and-closed pointer**
F2 prescribes as owed — **do not write it here**; that is specification text and belongs with the
homing acts, not with a re-classification.

**1.4** Report how many entries move out of item 1 under R1, and how many remain.

## 2. Task 2 — Apply R2 (and check A1 first)

**2.1** For each guard failing on this wave's or the previous wave's homings, determine from the tool
itself: does it **re-derive a live invariant**, or **record a measurement taken at a point in time**?
Cite the evidence per tool. **Report if the earlier R4 classification put any of them on the wrong
side, and why** — that is a finding about the classification, not about the tool.

**2.2** Move the point-in-time ones out of the live guard list, artifact preserved and marked
historical. **Repair none.** A tool that stays and fails, stays failing.

**2.3** State the scaling fact plainly for the record: item 1's remaining re-homings will move more
entries and therefore break more artifacts that name them, so this classification is what makes the
rest of the item affordable without accumulating failures.

## 3. Task 3 — Continue item 1's re-home class (R3)

Home entries whose owning specification is **unambiguous**, each written into the specification **in
its own voice, with its defense**, verbatim and home re-taken, former preserved (#12).

**Do not name a former-home document by filename in `ARCHITECTURE.md`** — the previous wave
established that a filename there reads as a new naming and moves a measured population by the act of
recording provenance. Provenance goes in the register field.

**Where the owning specification is not unambiguous, do not guess** — report it in the residue.

**Report the delegation-route residue** for the user, without drafting wordings unless the document is
already a home for a related concern.

## 4. Task 4 — Close

Guards at the committed tree with the list `gen_guard_state.py` derives, **reflecting Task 2's
classification**; report and **fix none**. Re-aim any anchor this wave's edits drift, per citation.
Verify what is committed through `tools/audit/changed_paths.py`. Run `tools/audit/process_check.py`
over this dispatch. `STATUS.md` gains one POINTER entry.

Report item 1's remaining population by route.

## 5. Accepted outcomes

**A2 failing is a STOP** and R1 becomes a user ruling rather than an application. **A1 coming back
different is a result** — if the artifacts genuinely re-derive a live invariant, they stay and fail.
**A short Task 3 is acceptable**; R1 and R2 are the wave's first duties because they change what the
rest of the item costs.

## 6. Self-check (D-434) — run by Cowork before release

- **Ruling ledger.** Three rulings; R1 stated as an **application** of OI-272 with A2 as its check and
  a STOP if the text will not carry it.
- **#17(a).** Three facts read at the objects, including the robust-stop diff run by Cowork rather
  than taken from a report. Two assumptions, both checked before the acts resting on them.
- **D-641.** Task 2 classifies apparatus rather than repairing it; Task 4 states the filter for
  anything else met.
- **Principles.** #6 — R1 refuses a second copy of a homed rule. C4 — re-homing preferred because the
  specifications must suffice without the register. #12 — nothing deleted; artifacts preserved and
  marked. #19 — the yield artifacts are classified on their own text, not on a filename.

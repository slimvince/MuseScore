# CC dispatch — derive what phase 1's completion statement still requires

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1_completion_inventory.md`.
>
> **★ THIS WAVE DERIVES. IT DOES NOT COMPLETE.** Phase 1's completion statement is **not written
> here** and this dispatch does not authorize it. The deliverable is a measured list of what the
> statement would still require.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231, gate at `CLAUDE.md` #8.
> **The freeze holds**, with one conditional exception at Task 1.

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04.** Derive, as a **measured list**, exactly what phase 1's
  completion statement still requires. **Not from anyone's recollection** — from D-231's own text and
  from the register and open-items data.

## 0b. THE PREMISE LEDGER (#17a)

**FACT — established at the object by Cowork this session:**

- **F1.** The owed reading set is **empty** — `tools/audit/decisions/reads6_yield.json` →
  `the_running_read_count.the_owed_set_is_empty`, with the surface, exclusions and read counts in the
  same block. Run by Cowork.
- **F2.** `gen_cluster_dispositions.py`'s **write** mode terminates with `re.PatternError` before
  writing anything, because six register entries carry an unescaped markdown `**` inside a `patterns`
  string; all six were authored by read wave 5 — `open_items/OI-333.md:10-32`.
- **F3.** That tool's **check** mode passes regardless, because it **re-reads rather than
  re-derives** — same row. So its passing figures bound quote and anchor integrity and say nothing
  about regenerability.
- **F4.** `regionanalyzer.cpp:653-659` records the D-261 proxy as measured to *"stop PREMATURELY"*,
  with the headline criterion implemented directly instead — the OI-331 conformance finding, read at
  the code.

**ASSUMPTION — checked before the act it licenses:**

- **A1.** That phase 1's completion statement **needs the disposition layer to be regenerable**. If it
  does, F2 blocks this derivation and the fix falls under the freeze's blocks-the-work exception; if
  it does not, F2 stays rowed and untouched. → **Task 1**.
- **A2. Cowork's recollection of the outstanding rows** — OI-274's body-tense half, OI-282, OI-283's
  remedy, OI-290, OI-296, OI-299, OI-320, OI-300, OI-325, OI-331, OI-333. **This list is NOT an input
  to the derivation.** It is a **cross-check applied afterwards**, and any divergence is a finding
  about the recollection, not about the derivation. → **Task 4.3**.

## 1. Task 1 — Settle A1, and fix only if it blocks

**1.1** Establish whether the completion statement's claims would rest on the disposition layer — for
instance any claim that the harvested statements are all dispositioned, or any coverage figure drawn
from it.

**1.2 If it blocks:** the fix is licensed as the freeze's blocks-the-work exception, and it is small —
escape the six `**` occurrences in the affected `patterns` strings so they compile as literals.
**Verify the write mode then completes and the artifacts re-derive.** Report the fix as an exception
exercised, not as the freeze relaxing.

**1.3 If it does not block:** change nothing; OI-333 stays rowed exactly as it is.

**1.4 Either way**, record on OI-333 that F3 is the sharper half — a guard whose check mode re-reads
cannot see that its write mode is dead, and every wave that cited it as verification was citing a
narrower check than it appeared to be.

## 2. Task 2 — State the requirement from D-231's own text

Read D-231 at `CLAUDE.md` and quote its phase-1 clause verbatim. Phase 1 has **two halves** —
specifications made **COMPLETE** (every recorded decision written into its owning specification, with
its defense) and **TRUE** (the specification text corrected wherever it states something false at
HEAD).

**Derive the completion criteria from that sentence**, not from any summary of it. If the clause
contains obligations Cowork has not named — and it may — those are part of the answer.

## 3. Task 3 — Derive the outstanding set

Generate an artifact enumerating, **per half**, what remains:

- **The COMPLETE half.** Which registered decisions are not written into an owning specification.
  Derive from the register's own home and gap data, and state the classes: documentation gaps,
  entries whose home is a tracking surface, entries whose home fails the section criterion. Report the
  population, not a judgment about it.
- **The TRUE half.** Which open rows assert that a specification states something false at HEAD.
  Derive from the open-items data by class rather than by remembering row numbers.
- **The gating set.** Which of the above **gate** under D-438's test — does the row's subject bear on
  the analysis, its inputs, or an instrument a measurement depends on — and which are apparatus and
  therefore do not. **An establishment obligation (#19) always gates.**

For each item: its identifier, which half it belongs to, whether it gates, and the evidence.

**Report the reads as done** (F1), with the derivation showing it rather than asserting it.

## 4. Task 4 — Report, and grade Cowork's list

**4.1** State plainly what the completion statement would still require, and what it could already say.

**4.2 Do not write it.** Not a draft, not a partial. It rests on the derivation this wave produces and
on the user's ruling, and neither exists yet.

**4.3 Then compare A2's recollected list against the derived one**, and report the divergence in both
directions: what Cowork listed that the derivation does not carry, and what the derivation carries
that Cowork missed. **The derivation is the answer; the comparison measures the recollection.**

## 5. Task 5 — Close

Guards at the committed tree with the list derived by `gen_guard_state.py`, reflecting read wave 6's
classification; report what fails and **fix none** beyond Task 1.2 if it fired. Re-aim any anchor this
wave's edits drift, per citation. Verify what is committed through `tools/audit/changed_paths.py`. Run
`tools/audit/process_check.py` over this dispatch. `STATUS.md` gains one POINTER entry.

## 6. Accepted outcomes

**A1 coming back "does not block" is a result** and OI-333 stays rowed. **The derived list being
longer than Cowork's is expected** — that is why it is derived. **A completion statement that turns
out to be far off is the honest outcome**; the reads being finished was never the whole of phase 1.

## 7. Self-check (D-434) — run by Cowork before release

- **Ruling ledger.** One ruling: derive, do not complete.
- **#17(a).** Four facts established at the objects, including the two gating findings read at their
  own sources. Two assumptions — A1 gates the one licensed fix, and **A2 is explicitly demoted from an
  input to a graded output**, because a recollected list is the thing this wave exists not to rely on.
- **Principles.** #19 — the derivation replaces recollection. #12 — nothing corrected away; findings
  rowed. D-438 — the gating test is applied per row rather than assumed. #6 — the freeze exception is
  narrow, conditional and reported as exercised rather than relaxed.
- **D-599.** No alternatives are offered: the principles decide that a completion claim must be
  derived, and this dispatch states it rather than presenting it as a choice.

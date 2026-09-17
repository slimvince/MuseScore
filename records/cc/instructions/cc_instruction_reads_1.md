# CC dispatch — READ WAVE 1: the owed OI-207 documents, and nothing else

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork).** Queued behind
> `cc_instruction_phase1z_commit_and_instrument_record.md`.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_reads_1.md`.
>
> **★★ THIS WAVE READS. IT DOES NOTHING ELSE.** No tool is built, no tool is fixed, no guard is
> repaired, no doc-sync correction is applied, no criterion is revisited. **The mechanism set is
> FROZEN.** A defect found in a tool is **rowed and left**, unless it blocks a read — and "blocks"
> means the read cannot proceed, not that the tool is annoying.
>
> **★ WHY.** Fourteen waves have passed since the read count last moved. Every one was consumed by
> something the previous wave discovered, and a growing share of those discoveries are faults in
> apparatus this arc built. The reads are the only bounded item on the board and they are the gate on
> phase 2, which gates phase 3. This wave exists to move that number.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> `tools/robust_stop/`, no behaviour change, no fix, no design. Phase 1 under D-231.

## 0. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session:**

- **F1.** The reading regime — the ordering, the per-document predicted yield bands registered before
  any of them was read, and the size fields — is at
  `tools/audit/decisions/phase1n_reading_regime.json`. **It is the authority for what to read and in
  what order; this dispatch names no document itself.**
- **F2.** The regime records that **no tail is bounded**: the best proxy is fitted-and-self-measured
  on the read set with counter-examples inside it, so every owed document is read.

**ASSUMPTION — checked before the reading rests on it:**

- **A1.** That the regime's ordering and bands are still current after the waves since phase 1n, and
  that no owed document has been read in the interim. → **Task 1**.
- **A2.** That the phase-1t recording rule (D-431 widened to every surface) is **not** yet in force,
  since phase 1t has still not run. → **Task 1**; if it has run, apply it; if it has not, apply the
  stricter standard voluntarily as phase 1w did, and say which.

## 1. Task 1 — Check the regime, then read

Confirm A1 and A2 and report both. Then read documents **in the regime's order**, in full, for as
many as this wave's capacity allows.

**Per document:**

- Enter every decision-bearing statement as a register entry with **the record's own status only**.
  Inference of a status is forbidden; *"not stated"* is expected and is the correct value where the
  record is silent.
- Record the document's **actual yield against its registered band** (F1). A refuted band is a
  result — the proxy was declared unvalidated when it was registered, and this is how it gets
  established or falsified.
- Row any finding of the OI-232 / OI-274 / OI-276 / OI-279 class — a document stating as current
  something false at HEAD. **Row it; do not correct it.** Corrections are action and they wait.
- Where a decision's home is a section that records findings rather than states rules, note it for
  OI-296's sweep rather than resolving it.

## 2. Task 2 — What to do with what you find

**Row, do not fix.** This applies to everything: doc-sync findings, tool defects, guard failures,
register gaps, stale figures. The freeze is the point of the wave, and a wave that reads five
documents and fixes three things is the pattern that produced the last fourteen.

**Two exceptions, both narrow.** A finding that **blocks the reading itself** may be fixed, and the
fix reported. A finding that is a **#19 establishment obligation** gates under D-438 and must be
rowed prominently — but still not fixed here.

**If a read turns up a member of the struck-versus-sounding family**, that is a **#13 STOP for the
gate partition**, not for this wave: report it against
`tools/audit/phase3_gate_partition.json`'s registered check, keep reading, and let the partition's
own stop condition do its work.

## 3. Task 3 — Update the count, honestly

Update the OI-207 note with the new read count, the remaining list, and the yield measured against
the bands.

**Do not revise the remaining-session estimate without a measured basis**, and do not revise it
downward because a wave went well. The wave-schedule artifact already records that per-document
overhead is unmodelled and that its implied wave count is a **lower bound**.

## 4. Task 4 — Close

Run the guards at the committed tree with the list derived by `gen_guard_state.py`; **report the six
pre-existing failures as unchanged or changed, and fix none.** Verify what is being committed through
`tools/audit/changed_paths.py`. Run `tools/audit/process_check.py` over this dispatch.

`STATUS.md` gains one POINTER entry giving the new read count and nothing else of substance.

## 5. Accepted outcomes

**A short wave is acceptable; a wave that read three documents and repaired four tools is not.**
Reading fewer documents than hoped is a capacity fact. Fixing things instead of reading is a failure
of this dispatch's one instruction.

**Refuted yield bands are the expected result** on at least some documents — the proxy was registered
as unvalidated, and this is the out-of-sample test it was registered for.

**Zero-yield documents are a result**, not wasted effort: the regime's own measurement found that a
substantial share of already-read documents yielded nothing, and confirming that on the owed set is
part of what bounds the residual.

## 6. Self-check (D-434) — run by Cowork before release

- **#17(a).** Two facts, both cited to the regime artifact rather than restated. Two assumptions,
  both checked before the reading rests on them — A2 exists because phase 1t has still not run and
  this dispatch must not assume its rule is in force.
- **The dispatch names no document and no count.** Both live in the regime artifact (D-431), which
  also removes the failure mode where a dispatch's list and the artifact's list diverge.
- **Principles.** #12 — findings rowed, nothing corrected away. #13 — a family member found is a stop
  for the partition, with its own registered check. #19 — establishment obligations rowed
  prominently. D-438 — apparatus findings gate nothing and are left.
- **Scope.** This is the freeze, stated three times, because the last fourteen waves each began as a
  bounded act.

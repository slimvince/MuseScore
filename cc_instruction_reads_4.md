# CC dispatch — READ WAVE 4: apply the OI-326 ruling (measured first), close the status gap, then read

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_reads_4.md`.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231. **The freeze holds: no tool
> built, no tool fixed, no guard repaired.** A tool defect found is rowed and left.

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04, OI-326.** `ARCHITECTURE.md`'s doc-governance hierarchy clause
  **delegates, but only to the members it names EXPLICITLY.** The glob `cowork_layer*_design.md` and
  the trailing ellipsis **confer nothing** — a delegation with indeterminate membership could be
  extended by a session, which is the authority rule (g) reserves to the user. **D-432 is unchanged**;
  this applies its logic rather than amending it.
- **R2 — RULED, same act.** Anything R1 leaves out is decided through the **OI-293 write list**: a
  delegation the user writes settles that document without touching the bar.
- **R3 — CONFIRMED, same act.** Where a document is named in **both** an admitting and an excluded
  form, **the strongest naming governs**. Being cited elsewhere in a weaker form does not undo a
  delegation. This confirms D-432 rather than extending it.
- **R4 — CONFIRMED, same act.** **D-430 requires BOTH halves and the kind half is decisive.** A
  well-formed delegation to a section that records findings rather than states rules **admits
  nothing**. The halves are applied in that order.
- **R5 — THE CONDITION ON R1, ruled with it.** Before R1 is applied, **measure how many
  glob-matched documents are already `contract-home` on their own separate anchors.** If the split
  moves a **large** population, **report and STOP** — it is measured before it lands, not after.
- **R6 — RULED, same act.** Write the status-surface entry recording that read wave 3 is committed
  (`0787ebf0ff`) with its committed-tree guard result, **and commit it with this wave** — one entry,
  one commit. The gap arose because a commit-only dispatch cannot record its own commit; folding it
  forward closes it without a regress.

**None of R1–R6 authorizes a fix, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — established at the object by Cowork this session:**

- **F1.** `ARCHITECTURE.md:346-351` names the per-layer / per-component design documents by a **glob**,
  three explicit filenames, a prose reference (*"the phrase-boundary design"*) and a **trailing
  ellipsis**, with the predicate *"are the **authoritative detail** for their own scope — the rules,
  the mechanisms, the per-layer decisions-with-alternatives."* The indeterminate membership is what
  R1 turns on.
- **F2.** Commit `0787ebf0ff` exists on master with 39 files changed — read at the object by hash.
- **F3.** At HEAD the register verifier and the open-items split check both pass — run by Cowork.

**ASSUMPTION — checked before the act it licenses:**

- **A1.** That "several" glob-matched documents are already `contract-home` on their own anchors, so
  R1's split is less consequential than it reads. Cowork has this from OI-326's row, not from the
  data. **This is exactly what R5 makes a measurement.** → **Task 1**.

## 1. Task 1 — Measure R5 BEFORE applying R1

Enumerate, from the register data:

1. every document the clause reaches under **reading A** (explicit names, glob matches, the prose
   reference, and anything the ellipsis has been taken to cover in existing grades);
2. of those, which are **already** `contract-home` on a **separate** anchor of their own;
3. therefore, which entries actually **move** under R1, and in which direction.

**Publish it as a generated artifact.** If the moving population is large, **STOP and report** — R5
is a stop condition, not a caution, and "large" is reported with the number rather than judged
silently.

## 2. Task 2 — Apply R1, if Task 1 clears

Apply the ruling to the delegation grading: explicitly-named members admit on this clause;
glob-matched and ellipsis members do not admit **on this clause** — they keep whatever class their own
separate anchors give them.

Record **R3 and R4 as confirmations** where the criterion lives, so neither is re-asked: strongest
naming governs; both halves required with the kind half decisive.

**Do not promote any wave-3 entry beyond what R1 licenses.** They were entered as documentation gaps
so nothing moved on a session's reading; R1 moves only what R1 names.

**Anything R1 leaves out goes to the OI-293 write list (R2)** — enumerate the affected documents there
with a draft delegation each, for the user to write or reject. **Do not write a delegation into
`ARCHITECTURE.md`.**

**Flip OI-326** with the ruling, the measurement, and the write-list residue.

## 3. Task 3 — Close the status gap (R6)

Write one `STATUS.md` entry covering **both** read wave 3's commit — naming `0787ebf0ff` and the
committed-tree guard result — **and this wave**, and commit it with this wave's work. It is a pointer,
per the standard.

**Record the general lesson beside it, briefly:** a commit-only dispatch cannot record its own commit,
so the record goes in the next wave's entry. That is a protocol note, not a defect to fix.

## 4. Task 4 — Read

Read documents **in the regime's order**, in full, for as much capacity as Tasks 1–3 leave. Per
document, exactly as waves 1–3: entries at the record's own status, *"not stated"* expected; actual
yield against the registered band in **this wave's own artifact**; OI-232 / OI-274 / OI-276 / OI-279 /
OI-315 class findings **rowed, not corrected**; decisions homed in findings-recording sections noted
for OI-296.

**Do not write yields into the regime artifact** — OI-316, now four waves deep.

**On the bands:** two consecutive waves have fallen in one length tercile, so the proxy has twice made
a single prediction for a packing whose yields differ several-fold. **Report band and point both ways,
and do not describe a band pass as validating the proxy.**

## 5. Task 5 — Close

Guards at the **committed** tree with the list derived by `gen_guard_state.py`; report the six
pre-existing failures as moved or unmoved and **fix none**. Where this wave's own edits drift an
anchor, re-aim per citation — completing the edit, not fixing a rowed defect. Verify what is committed
through `tools/audit/changed_paths.py`. Run `tools/audit/process_check.py` over this dispatch.

Update the OI-207 note with the new read count and the measured yield. **Do not revise the remaining
estimate without a measured basis.**

## 6. Accepted outcomes

**Task 1 stopping the wave is a success** — R5 exists so the split is measured before it lands.
**A short read half is acceptable**; the ruling and the status gap are this wave's first duties.
**Refuted bands are expected.**

## 7. Self-check (D-434) — run by Cowork before release

- **Ruling ledger.** Six rulings stated verbatim from the user's act, including the condition R5 and
  the confirmations R3/R4 — written out because dropping a ruling in a re-issue is a defect this side
  has already committed once, and D-468 carries the scar.
- **#17(a).** Three facts established at the objects — the clause's own text, the commit by hash, the
  guards by running them. One assumption, and it is the very thing R5 turns into a measurement.
- **Principles.** Rule (g) — R1 refuses membership a session could extend. #6 — D-432 is applied, not
  duplicated or amended. #19 — R5 measures before applying. #12 — nothing promoted, nothing deleted.
  D-231/freeze — no tool built or repaired; findings rowed.

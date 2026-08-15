# CC dispatch — READ WAVE 2: the owed documents, one bounded check, one ruling I failed to transmit

> **Status: ACTIVE DISPATCH. RE-ISSUED 2026-08-04 (Cowork)** after phase 1z returned. Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_reads_2.md`.
>
> **★★ THIS WAVE READS.** The mechanism set is FROZEN. No tool built, no tool fixed, no guard
> repaired, no doc-sync correction applied. A defect found is **rowed and left** unless it blocks a
> read — and "blocks" means the read cannot proceed, not that the tool is annoying. Task 3 is the one
> exception and it is not a fix; it completes a ruling that this side failed to transmit.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231.

## 0a. THE RULING LEDGER — new, and here because its absence caused a defect

**A dispatch that applies a ruling states the ruling.** Phase 1z's re-issue dropped the sentence
recording that the user had ratified the instrument default; CC correctly refused to infer a ratifier
from a dispatch that did not name one, and **D-468 now reads "ratifier not stated" about a decision
the user made.** The premise ledger checks facts this side asserts. It had no slot for the authority
this side acts on. This section is that slot, and it stands in every dispatch from here.

- **R1 — RULED by the user, 2026-08-03, in session.** `tools/a8_rebaseline_measure.py` defaulting
  `--expect-arm joint` is **ratified**, and the change is to be **recorded in `CLAUDE.md` block (A)'s
  provenance with its measured evidence**. Presented as three options with the third recommended —
  ratify *and* record — and agreed. **Phase 1z executed the recording half and, through Cowork's
  omission, not the ratification half.** Task 3 completes it.

## 0b. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session:**

- **F1.** D-468 reads **"LIVE · decided 2026-08-03 · ratifier not stated"**, homed at
  `CLAUDE.md:376-377` — `decisions/group_C.md:894`, `:896`.
- **F2.** `ARCHITECTURE.md:3510-3518` now carries §5.2's own scoping sentence, naming the legacy key
  path, its dormancy behind the notation flag, and that it *"is still what plain `batch_analyze` runs
  when `--joint-inference` is not passed."*
- **F3.** D-058 was one of **three** decisions the 2026-08-01 adjudication named as invisible to the
  harvest's signature net; it was found by full reading and never checked against the code afterwards.

**ASSUMPTION — each checked before the work rests on it:**

- **A1.** That the other two are the **priority-of-evidence ranking** and the **slicer boundary rule**.
  Cowork has this from the OI-207 note, whose cited line numbers have drifted since. → **Task 2.1**:
  identify all three from the adjudication's own record, not from Cowork's memory of it.
- **A2.** That read wave 1's yield record lives in its **own re-deriving artifact** rather than in the
  regime's owed rows (OI-316). → **Task 1.1**; follow whatever is actually in place, and do **not**
  write yields into the regime.

## 1. Task 1 — Read

**1.1** Confirm A2 and report the arrangement. **Do not update the regime artifact's bands or owed
rows** — OI-316 records why: writing a yield back recomputes the bands from a read set that now
contains the document being graded (#20). The regime showing a stale owed figure is the declared
defect, not a thing to tidy.

**1.2** Read documents **in the regime's order**, in full, for as many as capacity allows. Per
document:

- Enter every decision-bearing statement with **the record's own status only**; *"not stated"* is
  expected and correct where the record is silent.
- Record the actual yield against the registered band, in this wave's own artifact.
- Row any OI-232 / OI-274 / OI-276 / OI-279 / OI-315 class finding — a document stating as current
  something false at HEAD. **Row it; do not correct it.**
- Note, for OI-296's sweep, any decision homed in a section that records findings rather than states
  rules.

## 2. Task 2 — The two-sibling check (gathering, bounded to two)

Read wave 1 established that a decision entered with unusual care was never checked against the code
afterwards (F3). **Finding is not verifying.**

**2.1** Identify, from the adjudication's own record, the **three** decisions it names as invisible to
the harvest. Discharge A1 — do not take Cowork's two names on trust, and expect the cited line
numbers to have drifted.

**2.2** For the two that are not D-058, **check each against the code or the record it describes**: is
the statement still true at HEAD?

**2.3 Row what you find. Correct nothing.** If either is false it is the OI-315 class, and the
correction is a later act.

**Bounded to those two.** This is not a licence to re-check the register.

## 3. Task 3 — Complete R1

Per the ruling ledger: set **D-468's ratifier from the record of the user's ruling** — ratified by the
user, 2026-08-03 — and correct its provenance, which currently states that the ruling is still owed.
It is not; the omission was Cowork's dispatch, not the user's silence.

**This is the only non-read edit in the wave**, and it is not a fix: it completes a transmission that
broke. Do not extend it to any other entry, and if the register's ratification convention requires a
form Cowork has not anticipated, **follow the convention and report the difference**.

## 4. Task 4 — What to do with what you find

**Row, do not fix.** Doc-sync findings, tool defects, guard failures, register gaps, stale figures —
all rowed. A wave that reads five documents and fixes three things is the pattern that consumed the
fifteen waves before read wave 1.

**Two narrow exceptions.** Something that genuinely **blocks the reading** may be fixed and reported.
A **#19 establishment obligation** gates under D-438 and is rowed prominently — still not fixed here.

**If a read turns up a member of the struck-versus-sounding family**, report it against the registered
check in `tools/audit/phase3_gate_partition.json` and **keep reading**; the partition's own stop
condition does the work and this wave does not stop for it.

## 5. Task 5 — Update the count, honestly

Update the OI-207 note with the new read count, the remaining list, and the measured yield.

**Do not revise the remaining-session estimate without a measured basis**, and not downward because a
wave went well.

**On the bands:** read wave 1 measured that every registered band has a floor of zero, so a pass is
close to unfalsifiable, and against the point prediction that wave split two above and four below.
**Report both ways** — band and point — and do not describe a band pass as validating the proxy.

## 6. Task 6 — Close

Guards at the committed tree with the list derived by `gen_guard_state.py`; report the pre-existing
failures as moved or unmoved and **fix none**. Where this wave's own edits drift an anchor, re-aim it
per citation — that is completing the edit, not fixing a rowed defect, and phase 1z's report drew the
distinction correctly. Verify the commit through `tools/audit/changed_paths.py`. Run
`tools/audit/process_check.py` over this dispatch.

`STATUS.md` gains one POINTER entry giving the new read count and nothing else of substance.

## 7. Accepted outcomes

**A short wave is acceptable; a wave that read three documents and repaired four tools is not.**
**Task 2 finding both siblings still true is a result** — it bounds the class at one instance.
**Task 2 finding either false is the OI-315 class again**, and rowing it is the deliverable.
**Refuted bands are expected** and are the out-of-sample test the proxy was registered for.

## 8. Self-check (D-434) — run by Cowork before release

- **★ The ruling ledger (§0a) is new**, and it exists because its absence produced F1. Every dispatch
  from here states the rulings it applies, alongside the facts it asserts.
- **#17(a).** Three facts read at the objects. Two assumptions, both checked first — A1 because
  Cowork's names come from a note whose line numbers drifted, A2 because the arrangement changed
  under OI-316 after the regime was written.
- **The dispatch names no document and no count**; both live in the regime and the wave artifacts
  (D-431).
- **Principles.** #12 findings rowed, nothing corrected away. #20 — Task 1.1 refuses the yield
  write-back. #13 — a family member is reported against the registered check. D-438 — apparatus
  findings gate nothing.
- **Scope.** Task 3 is one field on one entry, and it is named as a transmission repair rather than
  smuggled in as maintenance.

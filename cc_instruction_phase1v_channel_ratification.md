# CC dispatch — phase 1v: commit phase 1u, and ratify the discovery-channel enumeration

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's ruling of the same
> date (twelfth set).** Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1v_channel_ratification.md`.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** Every load-bearing claim is FACT with a
> citation to the object it is about, or ASSUMPTION with an ordered check before the act it licenses.
>
> **★ PHASE 1u's WORK IS UNCOMMITTED IN THE WORKING TREE.** Task 1 commits it. **Do not rewrite any
> of it** — Cowork has reviewed it and confirmed the one call it was held for.
>
> **★ `cc_instruction_phase1t_restatement_and_pruning.md` is queued BEHIND this wave.**
>
> **★ THIS WAVE READS NO OI-207 DOCUMENTS.** No `src/`, no goldens, no `tools/corpus/`, no
> `tools/robust_stop/`, no behaviour change, no fix, no design. Phase 1 under D-231.

## 0. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork in the session that wrote this dispatch:**

- **F1.** `CLAUDE.md:1028` names the discovery channels as six subjects in a parenthesis.
- **F2.** `cowork_oi200_perspective_inventory.md` §4 enumerates **ten** channels — headings read at
  `:113`, `:129`, `:142`, `:161`, `:170`, `:183`, `:199`, `:212`, `:225`, `:234`.
- **F3.** Channel 4's own text: *"none new — the channel is already mandated"* (`:167`).
- **F4.** Channel 8's own text: *"already scheduled — OI-199 pass 2 and partitions 2–3 run exactly
  this"* (`:221`).
- **F5.** Channel 9's own text: *"none new — the adjudication is this channel run to completion"*
  (`:230-232`).
- **F6.** Channel 10's own text: *"by construction they cannot find a class nobody has named … their
  role in this program is inventory completeness and regression, not discovery"* (`:236-238`).
- **F7.** §9 records the document's one requested decision as *"adopt, amend or reject the §6
  program"*, and it is untaken (`:335-336`).
- **F8.** `tools/open_items_split_check.py` reads the index for **IDs only** (`:104-112`); its
  byte-verbatim comparison is against the **detail** row (`:184-186`). *(Recorded here because
  Cowork's earlier claim that this guard blocks an index-row reshape was wrong; OI-299 carries the
  corrected reason.)*
- **F9.** `ratification_surfaces/` holds the moved class and the reading surface.

**ASSUMPTION — each has an ordered check before the act it licenses:**

- **A1.** That the inventory's banner reads *"STATUS: DRAFT for discussion (Cowork, 2026-08-01)"*.
  Cowork has this from the reading surface, which is a secondary source. → **Task 3.1**.
- **A2.** That the OI-207 adjudication's residual second pass ran on 2026-08-02 and that both of its
  faces — the unresolved cluster residual and the owed full reads — are live at HEAD. Cowork has this
  from the reading surface. **This is the substance of the channel-9 correction and must be
  established before that correction is written.** → **Task 3.2**.

## 1. The ruling this dispatch carries

The user has ruled **option (C) with (B)'s correction folded in**: amend the scope, correct channel 9,
then ratify — because channel 9 is both the scope gap and the stale sentence, and ruling its scope
while its text says the work is complete would ratify a contradiction.

## 2. Task 1 — Commit phase 1u

Phase 1u's six tasks are complete and staged. Cowork has reviewed them and **confirms the call the
wave was held for: the directory's CLASS reading was the intended one.** The dispatch's wording
("derive that set from what register entries actually cite") read literally returns one file; the
ruling and OI-287 both say *the ratification surfaces*, plural, and a one-file directory does not do
what was asked. The member left in place — untracked, where moving it would commit it — was also
correct: that is the OI-285 question, and it was not asked for that file.

Commit the wave. Verify what is being committed through `tools/audit/changed_paths.py`. **Change
nothing in it.**

## 3. Task 2 — Check A1 and A2

**3.1** Read the inventory's banner at the document and report it verbatim.

**3.2** Establish, at the objects, whether the OI-207 adjudication is complete: the unresolved
cluster residual (its current value lives in the disposition manifest — cite the artifact and field,
do not transcribe) and the owed full document reads on the OI-207 row. **If the adjudication turns
out complete after all, STOP** — the channel-9 correction would then be wrong, and the ruling rests
on it.

## 4. Task 3 — Correct channel 9, then ratify

### 4.1 The correction (ratified content — write this, do not paraphrase)

Channel 9's *"Proposed probe: none new — the adjudication is this channel run to completion"* becomes
a statement that **the OI-207 adjudication is this channel IN FLIGHT, not run to completion** — its
residual second pass ran 2026-08-02 and both faces remain live, the unresolved cluster residual and
the owed full document reads. The rest of channel 9's text, including the decisions register as the
mechanism that keeps the class empty afterwards, is unchanged.

Preserve the former sentence in the document's own dated note or in the register's provenance (#12).

### 4.2 The scope ruling (ratified content)

Record which channels `CLAUDE.md`'s phase-2 clause reaches, each with the ground from the channel's
own text:

- **Channel 9 — IN.** A distinct search the clause names nowhere, and it gates.
- **Channels 4 and 8 — ALREADY REACHED.** Channel 4 is an obligation carried by the other probes and
  not a search of its own (F3). Channel 8 is the audit passes the clause names separately, in the
  words immediately preceding its parenthesis (F4).
- **Channel 10 — NOT a discovery channel**, on its own account (F6); its catalog-feeding role is
  noted rather than dropped.

### 4.3 The ratification

Flip the inventory's banner from its drafted state to ratified, with the date and this ruling. **§4
becomes the ONE home for the enumerated discovery channels.**

### 4.4 Then, and only then, the clause

Change `CLAUDE.md`'s phase-2 clause from listing six subjects to **pointing at the inventory's §4**.
This is a change to a user-directed rule and is made **only** on this ratification — it is licensed by
it and by nothing else.

### 4.5 The register, the partition, and the row

Register entry in the same commit (D-230), covering the ratification and the scope ruling.
`tools/audit/gen_phase3_gate_partition.py`'s `status_of_this_source` block updated to record that the
enumeration is now ratified, and the artifact regenerated — the partition currently carries a stated
workaround that this retires. Flip **OI-298**.

## 5. Task 4 — What this does NOT do, and must say so

State it in the register entry and in the inventory's new banner, because a later reader will
otherwise assume more was decided than was:

- the **§6 program is NOT adopted**, in whole or in part;
- **OI-200 is not pulled forward**, and the document's own §9 request (adopt, amend or reject the §6
  program) **stays open and untaken** (F7);
- no probe, fix, design or inference change is authorized;
- **phase 1 is not completed.**

## 6. Task 5 — Guards, notes, close

Run every guard at the committed tree; **derive the list from what exists** and report rather than
substitute if one this dispatch names is absent. Read each output separately. Run
`tools/audit/process_check.py` over **this dispatch** and report what it finds against Cowork.

Anchor drift from the `CLAUDE.md` clause change is re-aimed **per citation from the drift report's own
numbers**.

`STATUS.md` gains one POINTER entry.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's own remedy, OI-274's body-tense
half, OI-288 half (a), OI-289, OI-290's document-side remedy, OI-296's sweep, OI-299's index-row
reshape (**now known NOT to be blocked by the split guard, F8** — it wants scheduling on its own),
OI-301, the owed reads, and the queued phase-1t dispatch.

## 7. Accepted outcomes

Tasks 1, 3, 4 and 5 are bounded and expected complete. **Task 2.2 finding the adjudication complete is
a STOP** — the ruling rests on it being in flight, and building the correction anyway would be
building around a refuted premise. **A1 coming back different is reportable, not fatal** — the banner's
exact words do not change what is ratified, only what the flip replaces.

## 8. Self-check (D-434) — run by Cowork on this dispatch before release

- **#17(a).** Nine facts, each cited to the object the claim is about — the channel texts read at
  their own lines rather than through the reading surface, which is how Cowork's reading came to
  differ from it on channels 8 and 10. Two assumptions, both from the reading surface, both checked
  before the act that rests on them, and A2 carries a STOP.
- **Principles.** #12 — the former sentence preserved, nothing deleted. #13 — A2's refutation is a
  STOP, not a workaround. #6 — the inventory becomes one home and the clause stops being a second,
  shorter enumeration. #7 — the clause changes at `CLAUDE.md`, the enumeration at the inventory, the
  status at the register. #19 — the ratification retires a stated workaround in the partition rather
  than leaving it carried.
- **D-431.** No bare quantity; the residual is named as an artifact field for CC to read.
- **Consistency.** Checked: Task 3.2's scope ruling and Task 3.1's correction are the same channel,
  which is why the ruling folds them; Task 4's disclaimers bound what Task 3.3 flips; nothing here
  contradicts anything else here.

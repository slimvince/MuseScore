# CC dispatch — phase 1u: record what the partition measured, prepare the channel ratification, and file the surfaces

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's rulings of the same
> date (eleventh set).** Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1u_partition_record_and_directory.md`.
>
> **★ THIS DISPATCH ASSERTS NO FIGURES (D-431) AND NO STATE IT HAS NOT READ (#17a).** Every
> load-bearing claim is FACT with a citation to the object it is about, or ASSUMPTION with an ordered
> check that runs before the act it licenses. An unlabelled claim is a defect — report it.
>
> **★ `cc_instruction_phase1t_restatement_and_pruning.md` is queued BEHIND this wave.**
>
> **★ THIS WAVE READS NO OI-207 DOCUMENTS.** No `src/`, no goldens, no `tools/corpus/`, no
> `tools/robust_stop/`, no behaviour change, no fix, no design. Phase 1 under D-231.

## 0. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork in the session that wrote this dispatch:**

- **F1.** D-437 and D-438 both read *"LIVE · decided 2026-08-03 · ratified by user"* —
  `decisions/group_T.md:551`, `:566`. **The rulings are ratified; the per-item APPLICATIONS are what
  this wave records.**
- **F2.** The partition exists with per-item verdicts and per-item reasons, nearly all GATING —
  `tools/audit/phase3_gate_partition.json`.
- **F3.** `CLAUDE.md:1028` names the discovery channels as *"(populations, oracles, invariants,
  residual decomposition, concept gaps, requirement side)"* — six subjects.
- **F4.** The inventory's channels are numbered and include **Channel 4 — Prediction-first operation
  (vary the EXPECTATION)** at `cowork_oi200_perspective_inventory.md:161`, which F3's list does not
  name. So the clause under-names the inventory **by at least one channel**, established.
- **F5.** OI-287 states the constraint any move must satisfy: every citation re-aimed **PER CITATION**
  from `gen_cluster_dispositions.py --verify`'s own output, never by an assumed path rewrite —
  `OPEN_ITEMS.md`, the OI-287 row.
- **F6.** `.gitignore:116` excludes `/cc_instruction_*.md` as a class, so a dispatch is in the record
  only if force-added.
- **F7.** D-436's text: a mechanism is kept when it *"has a measured false-positive rate at or near
  zero on legitimate work"*, its stated reason being that *"one that fires on legitimate work gets
  switched off, which is worse than having none"* — `decisions/group_T.md:526-530`.
- **F8.** OI-297's artifact is written **before** the print and is complete, so no recorded figure is
  affected — `open_items/OI-297.md:27-28`.

**ASSUMPTION — NOT read at the object; each has an ordered check, and no act depends on it first:**

- **A1.** That the inventory holds **ten** channels, and that of the four F3 omits, the fresh-reader
  channel and history mining are the two that matter — the latter being the OI-207 residual second
  pass, which gates. **Cowork verified channels 1–7 and F4's omission only; the total and the
  omitted set are from a session report.** → checked at **Task 2.1**.
- **A2.** That the ratification surfaces are a complete and correctly bounded set to move. → derived
  at **Task 4.1**, not assumed.

## 1. The rulings this dispatch carries

| # | Subject | Ruling |
|---|---|---|
| AA1 | The gate partition's verdicts | **Accept, and record that the ruling's measured effect was small** (option 1C) |
| AA2 | The phase-2 channel clause | **The inventory becomes the one home and is ratified; the clause points at it** (option 2B) — **preparation only here** |
| AA3 | The register's index-row shape | **Rowed with the deferred resolved-row split as ONE redesign** (option 3D) — not done |
| AA4 | OI-287 | **A directory for the ratification surfaces only** (option 4A) |
| AA5 | D-436 | **The criterion INFORMS; removal or retention is the user's ruling** (option 5C) |

## 2. Task 1 — Record what the partition measured (AA1)

Accept the per-item verdicts as generated (F2). **Then record, in the artifact and at D-437's entry,
what the partition's measured effect actually was:** most items gate, several on demonstrated grounds
rather than the doubt default, and the narrowing bites in one place — the family design need not wait
for phase 2's bounded trust statement to be *written*, only for the gating searches to have *run*.

**And record the refuted prediction beside the ruling it justified.** Cowork's decision surface said
this option *"removes the largest share of the blocking for the smallest loss of rigor."* It did not.
The ruling stands; the prediction that sold it was wrong, and a later session must meet the result
rather than inherit the expectation. State it plainly — this is #17(b) applied to a planning claim.

## 3. Task 2 — Prepare the channel ratification (AA2)

### 3.1 Check A1 first

Read `cowork_oi200_perspective_inventory.md` **in full**. Report: how many channels it enumerates;
which of them `CLAUDE.md:1028` names and which it omits; and for each omission, whether it is a
distinct search or an obligation carried by other channels. **Report the answer whatever it is** — if
the inventory holds fewer or more than A1 claims, that is the finding, and A1 came from a session
report rather than the document.

### 3.2 Prepare, do not apply

The ruling makes the inventory the one home for the channel list, with the clause pointing rather than
listing (#6). **Two halves, and only the first runs here:**

- **Build the ratification reading surface** for the inventory — the document put to the user in the
  form the register's ratification queues use, so it can be read and ruled on. It is currently an
  unratified draft that a binding rule points at, and that is what the ratification fixes.
- **Do NOT change the clause.** Pointing a governing rule at content the user has not ratified is the
  defect this ruling exists to close; changing the clause before the ratification would re-commit it
  in a new form.

**One thing may be written now**, because it is true and undisputed: a dated note at the phase-2 clause
recording that the enumeration it relies on is **unratified**, and that its ratification is owed.
That states the gap rather than filling it.

## 4. Task 3 — Row the index-row redesign (AA3)

The phase-1n correction to OI-288 reached the detail file; the INDEX row carried the false claim
through five further waves. The cause is that index rows are paragraph-length narratives duplicating
their detail files — the restatement problem inside the register itself.

**Row the redesign: an index row carries status, subject and a pointer; the narrative lives once, in
the detail file.** Record that it is **one act with the deferred resolved-row split** — both disturb
`tools/open_items_split_check.py`, which holds the original rows byte-verbatim and enforces a
bijection, so both need that guard's redesign and its own establishment step (#19).

**Do not do it here, and do not do half of it.** If phase 1t has already rowed the split, amend that
row rather than opening a second (#6).

## 5. Task 4 — The ratification-surface directory (AA4)

### 5.1 Derive the membership — this discharges A2

The ruling is: **the ratification surfaces only.** Derive that set from what register entries actually
cite as ratification provenance, not from a list. **Dispatches are excluded**, and F6 is why the
question is different for them — they are gitignored as a class, so a directory for them would either
force-add every one or stand half empty. Report the set you derive.

### 5.2 Move, and re-aim per citation

Name the directory in plain words (no invented label), move the derived set, and re-aim **every**
citation individually from the verify report's own output (F5). **A path rewrite is forbidden**: it
produces a tree where every reference resolves and some resolve to the wrong thing, which is the
failure shape with none of the visibility.

After the move, **re-read the register's provenance fields** and confirm each resolves to the file it
means. Flip OI-287.

## 6. Task 5 — D-436 becomes a reporting duty (AA5)

Amend D-436 at its home: the three conditions stay, and **a mechanism failing one is REPORTED with its
reason, not automatically removed — keeping or removing it is the user's ruling.**

**Preserve F7's stated reason in the amended text** — a check that fires on legitimate work gets
switched off, which is worse than having none. That reason is why the false-positive condition exists
and it survives the change; what changes is who decides the consequence.

Re-take D-436's verbatim; preserve the former (#12).

**Row the establishment run the guard needs.** The shell guard has two shapes its corpora do not cover
— a common existence-listing command, and a path outside the repository. Neither may be added to its
denied set without the false-deny establishment run D-436 requires. CC was right to refuse; the row
schedules it rather than leaving it to the next person who trips over it.

**OI-297** is recorded as a known limit with F8 stated — the artifact is complete and written first,
so no recorded figure is affected, and the fix is a print-encoding matter rather than a check defect.

## 7. Task 6 — Guards, notes, close

Run every guard at the committed tree; **derive the list from what exists** and report rather than
substitute if one this dispatch names is absent. Read each output separately. Verify what is being
committed through `tools/audit/changed_paths.py`. Run `tools/audit/process_check.py` over **this
dispatch** and report what it finds against Cowork.

Anchor drift from the Task 2 note and the Task 6 amendment is re-aimed **per citation from the drift
report's own numbers**. The Task 4 move drifts **paths**, not lines — treat it as its own re-aim with
its own verification pass, and do not assume the line-drift procedure covers it.

`STATUS.md` gains one POINTER entry.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's own remedy, OI-274's body-tense
half, OI-288 half (a), OI-289, OI-290's document-side remedy, OI-296's sweep, the inventory's
ratification, the index-row redesign, the owed reads, and the queued phase-1t dispatch.

## 8. Accepted outcomes

Tasks 1, 3, 5 and 6 are bounded and expected complete. **A1 coming back different is a success** — it
is why it is labelled. **Task 4 stopping because the derived membership is ambiguous is acceptable**;
report the ambiguity rather than choosing. **Task 2 delivering only the reading surface is the
intended outcome** — the clause does not move until the user has ratified what it would point at.

## 9. Self-check (D-434) — run by Cowork on this dispatch before release

- **#17(a).** Eight facts, each cited to the object the claim is about; two assumptions, each with an
  ordered check preceding any act that rests on it. A1 is an assumption specifically because its
  source was a session report, and Cowork verified only part of it directly.
- **Principles.** #12 — nothing deleted; former verbatims preserved. #13 — no surprise built around.
  #19 — the guard's uncovered shapes are rowed for establishment rather than closed by assertion.
  #6 — the inventory becomes one home rather than a second list; Task 3 amends an existing row rather
  than opening a rival. #7 — each amendment at the surface that owns it. #17(b) — Cowork's refuted
  planning prediction is recorded beside the ruling it justified.
- **D-431.** No bare quantity; F4 states an established lower bound rather than repeating a count
  Cowork did not verify.
- **Consistency between rulings.** Checked: AA2 and AA3 both remove restatement and both defer their
  applying half to a ratification or a guard redesign; AA5 changes who decides, not the conditions;
  AA1 and AA4 are independent. Nothing here contradicts anything else here.

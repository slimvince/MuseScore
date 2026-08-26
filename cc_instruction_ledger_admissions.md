# CC DISPATCH — LAND THE SEVEN DISPOSITIONS INTO THE LEDGER

*Written by the Cowork writing side, 2026-08-26, against tip
`052b183006ec89243d8f7863c59622b7d62d435c`. Executes Rulings 1–3 of
`cowork_rulings_2026_08_26_ledger_dispositions_sitting.md`. This batch performs NO ratification of its
own and orders NO register entry.*

---

## 0. What this batch is

The user disposed seven outstanding items: the one admission the gate re-check refused, and the six
candidates of the third harvest. **Five entries enter the ledger, three do not, and one statement is
routed.** This batch writes those into `EMPIRICAL_FINDINGS_LEDGER.md`, re-checks the new admissions at
the gate as Ruling 8 requires, and does nothing else.

**The prohibition that shapes everything: you dispose nothing.** The dispositions are the user's, taken
in the ruling record. Your job is to write them in, re-check them, and report.

---

## Task 0 — start state and landings

**(a)** Read `.git/refs/heads/master` with the file tool. **It must read
`052b183006ec89243d8f7863c59622b7d62d435c`. If it does not, STOP and report.** Name the side measured
wherever you state a hash.

**★ (b) ONE THING THE WRITING SIDE COULD NOT SETTLE, AND YOU CAN.** `cc_report_ledger_build.md` names
`902d903a62443fe2f0f503deafdca3264e59f7fb` as *"the batch's second and final commit"*, which is not the
tip. **Report whether a commit exists after it, or whether an amend replaced it** — `git log` by
explicit hash is the read D-253 permits. **Do not edit that report**; it is dated, and it disclaims its
own end state in terms. Report the fact only.

**(c) Do NOT run `git status`** (D-253). Run `python tools/audit/changed_paths.py`; record the
population; commit none of the standing untracked population **except** the file named at (d).

**(d) Land, in one commit:** `cowork_rulings_2026_08_26_ledger_dispositions_sitting.md` (untracked, the
record this dispatch executes); this dispatch; **and `cowork_fact_gate_admissions_2026_08_26.md`** —
untracked, and **the ledger already cites into it**, so the committed tree currently carries citations
whose target is not tracked. That omission is the writing side's, from the previous dispatch, and this
is its correction. Also land any other file left tracked-modified by the previous batch, naming each.

Then `python tools/audit/gen_evidence_pin_membership.py`.

---

## Task 1 — the five entries that enter the ledger

Each is written in the ruled form: **the fact in one sentence, its identifier, its gate verdict, and
the citation to where its five ruled fields already stand.** It restates no five-field entry. That is
Ruling 1 of `cowork_rulings_2026_08_26_ledger_form_sitting.md`.

**1. C9 — the ruled restatement.** The admitted sentence is authored in the ruling record and is
**quoted from there**, not re-derived:

> *In this repertoire, the presence of a leading tone does not distinguish passages where a diminished
> reading is the correct one from passages where it is not.*

Its five fields stand at `cowork_empirical_findings_candidates.md`'s C9 entry; **cite both** — the
candidates file for the fields, the ruling record for the restatement.

**★ The scope goes in the UNCERTAINTY field and NOT in the sentence, and this is a hard requirement.**
What was measured is the cases our gate fired on; the restatement speaks of passages generally. The
uncertainty field carries that difference explicitly, in the source's own terms. **If you find the
uncertainty field as it stands does not carry it, say so and STOP rather than widening the sentence or
narrowing it yourself.**

**★ And the refusal is kept, beside and never over (#12).** The REFUSED AT RE-CHECK record of the
original wording *"The presence of a leading tone does not distinguish the genuine cases"* stays in the
banner, with its ground, **pointing at the entry that replaces it.** A reader must be able to see that
the first wording was refused and why.

**2. C42** — admitted on the leading-tone half. **Not admitted:** the ceiling figures and the clause
about falling below the bar one wiring step required. The scope travels in the uncertainty field: Bach
ground-truth corpus, other repertoires unmeasured. **Cross-reference C39**, which measures the same
question from the other side.

**3. C43** — admitted on its **fact half only**. The rule half is **not** re-published (#6).

**4. C44** — admitted **at the width the user's 2026-08-02 scoping ruling gives it**, and the width is
part of the entry, not a note beside it. Its failure-diagnosis field keeps the record's own words:
**cause undiagnosed**.

**5. C45 reading one** — *an incorrect reading can be the optimum of a locally-informed objective on
this repertoire.* Its establishment travels with it: **derived and cross-checked against independent
earlier measurements, not measured over a corpus**, not upgraded.

---

## Task 2 — re-check the five at the gate, per Ruling 8

Ruling 8 requires **every** hand admission re-checked at the gate when it enters. These five are hand
admissions and this is that re-check. **The gate:** *does the fact survive the implementation being
thrown away?* — plus **approach-level**.

Report a verdict and a one-sentence ground for each of the five.

**If the re-check refuses any of them — including C9's restatement — do not enter it in the body, do
not drop it, list it in the banner under REFUSED AT RE-CHECK with your ground, and propose nothing.**
The disposition is the user's; the re-check is Ruling 8's; reconciling the two is the user's act.

**C9's restatement is the one to check hardest**, because it exists precisely to survive a refusal. If
it does not, that is the single most important thing this batch can report.

---

## Task 3 — the three that do not enter, and the one that is routed

Written into the ledger's §8, *what stands outside the ledger*, so silence claims nothing:

- **C45 reading two** — NOT ADMITTED. *Our failure class was of that kind*; the population is ours.
- **C46** — PROPOSED FOR NOTHING. Its durable half is already ruled and homed as the decision-neutrality
  corollary (**D-190**); admitting it would publish that rule twice. Record it as the clearest measured
  instance of why that corollary was needed.
- **C47** — FAILS. Every quantity is a property of our resolver's ranking and our carried menu.
- **C45 reading three** — **ROUTED** to the phase definitions' constraints and stop rules. *Diagnose
  whether an error is a search failure or a model failure before widening the search.*

**★ Record the routing WITH its bound, which the ruling states in terms: the destination cannot
presently receive it.** It joins the twenty-one defect-catalogue rows and the two earlier candidates
already routed there. **Write nothing to the phase definitions** — the routing is a disposition, not a
transfer, and no artifact can take it yet.

---

## Task 4 — the ledger's banner

Update it to state: the count of entries; that the **third ruled seed is now represented**, with its
coverage bound restated (the population was reached by pattern over the register's entry headings and
477 entries were not all read); the REFUSED AT RE-CHECK list, now carrying the original C9 wording with
its pointer to the replacement, plus anything Task 2 refuses; and the disposition arithmetic for these
seven, so it closes on the face of the record.

**Do NOT edit `cowork_empirical_findings_candidates.md`.** Its Part Three carries *proposed* verdicts,
which the ruling record has now ruled. Leaving them as proposed is correct: the candidates file is a
working list, the ruling record is where dispositions live, and editing the working list to match would
create the second copy the ledger's whole form exists to prevent. **Its banner sentence calling itself
superseded stays untouched**, as before.

---

## Task 5 — `STATUS.md`, the forward bound, the sweep, the report, the commit

**(a)** One **POINTER** entry in `STATUS.md` (OI-222 remedy; **D-431**: no count, no identity, no
rendered value), **written BEFORE the forward-bound tool runs**.

**(b)** Re-aim `tools/audit/gen_status_batch_bound.py` — the **five** aiming constants, and **append**
the outgoing aiming to `PREVIOUS_AIMINGS` rather than overwriting it (#12). Read the tool's parser for
the flag; report the exact command line, the values set, and **which task number you used for `TASK`
and why**.

**(c) The sweep**, in the ruled order: `gen_guard_state.py`, then `gen_guard_classification.py`. Three
reds are standing and **not yours to cure**: `[[OI-372]]`'s guard, `apply_soft_discard.py --check`,
`apply_residue_discard.py --check`. A staleness red caused by this batch's own writes is cured under
the standing sweep rule. **For any other red: if you cannot tell whether it is a decision red or a
regeneration red, treat it as a DECISION red and STOP.**

**Re-run the sweep with this batch's new root-level file(s) on disk** and report the filing-convention
guard's candidate list — the previous batch established that an unclassified candidate raises
`SystemExit`, so an entry there turns a failing guard into a crashing one. **Report it; do not classify
it, cure it or regenerate the guard.**

**(d)** Write `cc_report_ledger_admissions.md` at the root, then commit. State separately: the Task
0(b) commit finding; the Task 0(d) landings; **all five gate verdicts**; where the C9 scope was carried
and whether the uncertainty field held it; the sweep; every path written; and **every departure and
every instruction you could not obey.**

---

## §6 THE FENCE

Writes permitted at **exactly** these paths:

- `EMPIRICAL_FINDINGS_LEDGER.md`
- `cc_report_ledger_admissions.md` — new
- `STATUS.md` — one pointer entry
- `tools/audit/gen_status_batch_bound.py` — five aiming constants and the appended row, carve-out
- the Task 0(d) landings and `tools/audit/evidence_pin_membership.json`
- **any file a tool this dispatch orders you to run writes as its own output.** Name each in the report.

**Explicitly forbidden.** No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md` edit. **No register
entry** — these are the user's ratifications and their entries are OWED, named in the ruling record's
§5, and deliberately not ordered here because the register cannot presently accept one; **this is the
fourth consecutive batch shaped that way and the report should say so.** **No `cowork_empirical_findings_candidates.md`
edit of any kind.** No `cowork_fact_gate_admissions_2026_08_26.md` edit — it is landed, not modified.
Nothing written to the phase definitions. No `src/` change, no test changed, moved or run, no golden.
Nothing under `tools/corpus/` or `tools/robust_stop/`. No open-items row created, flipped or discarded.
No finding number allocated. Neither blind output opened. Neither pack, the generator, the manifest or
any withheld family touched. No other `.py` source edited. Do not cure the two discard-act checks; do
not regenerate `[[OI-372]]`.

**★ THE STANDING CLAUSE.** **If obeying any instruction here would require a write outside this fence,
STOP and report the conflict. Do not choose a route, do not widen the fence, and do not substitute a
weaker form of the instruction to stay inside it.** Stopping and reporting is the correct outcome.

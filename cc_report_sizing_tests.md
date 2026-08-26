# CC REPORT — the sizing unit's tests (a) and (b), and the sizing record

*Claude Code, 2026-08-26, under `cc_instruction_sizing_tests.md`, which executes Rulings 1 and 2 of
`cowork_rulings_2026_08_26_sizing_tests_sitting.md`. One reading file was delivered:
`ratification_surfaces/cowork_sizing_tests_reading.md`. This report states what was done, what was
established and how, and every departure.*

**The batch performed NO ratification, ordered and wrote NO register entry, built no ledger, admitted
nothing to one, and made no recommendation anywhere in its output.**

---

## 1. Task 0 — the start state and the landings

### 1(a) The tip

`.git/refs/heads/master` read with the file tool: **`c4a2563515fa6e6a46c06f036b06677b713a9852`**.
**Side measured: the REF side.** It is the hash the dispatch requires. **No STOP.**

### 1(b) The changed-path population — `git status` NOT run (D-253)

`python tools/audit/changed_paths.py`:

→ **836 changed path record(s) [worktree]**

| | count | note |
|---|---|---|
| untracked (`??`) | **835** | the standing untracked population — **not committed by this batch** |
| tracked, modified (` M`) | **1** | `cowork_handoff.md`, which the dispatch names as this batch's to land |

Both `cowork_rulings_2026_08_26_sizing_tests_sitting.md` and `cc_instruction_sizing_tests.md` were
present in the untracked population, as the dispatch states.

### 1(c) The landing commit

**One commit, `9683a9c1fe351cde4450bfe63c86d2331a83946b`** (read back at `.git/refs/heads/master`
with the file tool — **the REF side** — and independently at the shell as the commit just written;
the two agree). Three paths: the ruling record, this batch's dispatch, and `cowork_handoff.md`.

**★ The handoff modification was ESTABLISHED before it was committed rather than assumed.** The
dispatch says only that the file *"stands tracked-modified against the tip"*. What was measured:

| | at the tip (blob side, `c4a2563515…`, blob `6ba98a06da2419dc06b33e35d88dde657e0e21a1`) | in the working tree (file tools) |
|---|---|---|
| second-level headings | **92** | **93** |
| lines | **9,146** | — |
| the heading at line 4 | the **sixty-fifth** entry | the **sixty-sixth** entry |

**Exactly one entry heading is added, at the head, and the sixty-fifth entry's heading text is
identical on both sides.** The sixty-sixth entry (working-tree lines 4–302) was **read whole** before
the file was staged. Nothing else about the file moved.

### 1(d) The evidence-pin regeneration

`python tools/audit/gen_evidence_pin_membership.py` run after the commit, as ordered. It wrote
`tools/audit/evidence_pin_membership.json` and reported `members 7 — pinned 5, UNRESOLVED 0`.

---

## 2. Task 1 — the reading order and the verification

### 2(a) The ordered departure was performed as written

`cowork_blind_derivation_scoring_model_2026_08_24.md` was read **WHOLE, FIRST**, before `STATUS.md`,
`DECISIONS.md`, `BUILD_AND_TEST.md` and the gating identities were opened. **The read SET is
unchanged; only its order was.**

**★ AND IT COULD NOT ACHIEVE ITS PURPOSE — SEE §8.1. THIS IS THE DT-20 SHAPE, ON THIS SESSION.**

### 2(b) The verification, with the side measured — ★ PASSES

| Demand | Found | Side measured |
|---|---|---|
| banner *DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED* | present, verbatim, at line 3 | **worktree**, file tool |
| size **125,529 bytes** | **125,529** | **BLOB**, `git ls-tree -l` at tip `c4a2563515…` |
| sha256 `4887a9ab4dd16494cd7799b18babbfede83e51a40e11205920f1137a84a9861b` | **identical** | **BLOB**, `git cat-file -p d2942786fd83b9714ac833cb53ea9a224734427b \| sha256sum` |

**Why the blob side.** The size and hash receipt was taken at the working-tree file on 2026-08-24 and
committed byte-identical under Ruling 2 of the blinding-failure sitting, so the blob is a legitimate
side to measure and it is the **self-verifying, content-addressed** route D-253 prefers. **The
worktree copy is unmodified against that blob**, established separately: the file does not appear in
`changed_paths.py`'s population at all, so it is tracked and unmodified at the tip.

**No STOP. Banner, size and hash all agree.**

### 2(c) The session-start read

Taken after 2(a): `CLAUDE.md`, `STATUS.md`, `DECISIONS.md` in full; `BUILD_AND_TEST.md` **read** (the
conditional fired — this batch runs measurement tools whose commands and standing rules live there);
and rule (a)'s **`gating_ids`** at `tools/audit/nongating_apparatus_rows.json` →
`★_the_live_gating_answer` → `gating_ids`.

---

## 3. Task 2 — where the sizing record was found, and how

**It is §3 of the output, *"The sizing record"*, lines 1377–1510, with subsections §3.1–§3.4.** It is
**not** at a section numbered §5 — §5 of the output is *"The independence record"*.

**How it was found:** by content, not by number. The output was read whole; the section that reports
timings, counts, shares and the noise measurement was located and then confirmed by its own heading.

**It is reported at the reading file §1**, field by field against the ruled list, every share with its
denominator, **labelled NOT A BUDGET with its three defects beside it every time it is presented**.

**Nothing was reconstructed by the deriving session.** The one measurement not taken at the ruled
granularity — time per statement — is reported as a shortfall in the output's own words, with a batch
mean explicitly not presented as what was asked for. **The record's internal arithmetic was checked
here and closes** (the four writing batches sum to the stated total; the statement counts sum to 36;
every printed share recomputes; every per-statement source list equals its own count).

---

## 4. Task 3(a) — the dead-end corpus, identified and proved

**IDENTIFIED: `docs/scoring_model.md` §8, *"Known constraints and dead ends"*, lines 1129–1456.**

**Four texts establish it as the authoritative source; all four are quoted in full at the reading file
§2.1.** In brief:

1. **`CLAUDE.md`'s mandatory sync rule for this very document** — *"Adding a new constraint or dead
   end: add it to §8"*. That is the ONE place a dead end is recorded.
2. **The governing plan's own referent cites INTO this section by line.**
   `cowork_specification_reconstruction_plan_successor_2026_08_21.md` §6.4's single worked PASS case is
   *"an absent root does not mean a wrong reading, corpus-wide"*, cited to **`docs/scoring_model.md:1396`**
   — which is inside §8 and carries that sentence verbatim. §6.1 describes the corpus as *"LEGACY-scoped"*
   with *"a different subject from a blind derivation"*, which is what §8 says of itself throughout.
3. **The ruled seed list names it by name** — `cowork_rulings_2026_08_15_method_directions.md`,
   direction 4: *"Existing seeds: `DEFECT_TYPES.md`, `docs/scoring_model.md` §8, the refuted-repair
   register entries."*
4. **§8 claims the home for itself under #6** — *"This is the dead end the two *tried and closed — do
   not retry* lists in `ARCHITECTURE.md` name; they point here and the rule is published once (#6)."*

**No source was assembled.** `ARCHITECTURE.md` carries four further *"Tried and closed"* pointer lines
naming register identifiers whose homes are elsewhere (D-278, D-287, D-288, D-290, D-572 among them).
**They were NOT folded in**, they are named at the reading file §2.1, and the coverage of test (a) is
reported at its true width.

---

## 5. Task 3(b)–(c) — the test applied, and the two products

**The admission test was applied by hand to every §8 item that bears on a statement — 28 items,
tabled one by one at the reading file §2.2**, each with its own text, the statement it bears on, its
gate verdict and whether it withdraws. The calibration used is the plan's own two worked cases.

### 5.1 Product one — the withdrawal rate

**ZERO of 36 statements are withdrawn by a passing dead end. 0 / 36 = 0.0 %.**

**It is labelled `UNCITABLE` at the point it appears in the reading file, in the same sentence that
states it, with the reason named:** it is a measurement over statements produced by a session whose
blinding failed. The label is repeated in the paragraph beneath it so the number and its bound cannot
travel apart.

**Eight dead ends passed the test and none of them withdrew a statement.** Six of the eight
**corroborate** a statement; a corroboration is not a withdrawal and is not counted as one.

### 5.2 Where the ledger's entry shape was found, quoted

**It is FIVE fields, and it is ruled** — `cowork_rulings_2026_08_15_method_directions.md:46–54`,
quoted whole at the reading file §2.4:

> 4. **OUR OWN EXPERIMENTAL FINDINGS ENTER VIA AN EMPIRICAL FINDINGS LEDGER, THROUGH AN AIRLOCK.**
>    Admission test: *does the fact survive the implementation being thrown away?* Entries are
>    approach-level, implementation-stripped, each with provenance, uncertainty (#24) and
>    establishment status (#19), and its failure diagnosis or "cause undiagnosed". […] Existing
>    seeds: `DEFECT_TYPES.md`, `docs/scoring_model.md` §8, the refuted-repair register entries.

Restated whole at `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:95–99`. **The
five fields: the fact (approach-level, implementation-stripped); provenance; uncertainty (#24);
establishment status (#19); failure diagnosis or "cause undiagnosed".** No shape was invented; no
STOP was reached.

### 5.3 Product two — and the finding that governs it

**Eight facts pass. ★ EVERY ONE OF THEM ALREADY STANDS IN THE FIVE-FIELD SHAPE, AND EVERY ONE IS
ALREADY IN THE 31-ADMISSION SEED** (C1, C2, C4, C5, C6, C7 admitted in round one; C8 and C9 in round
three as restated music halves). They are tabled at the reading file §2.4 by identifier, with the
place their five fields stand and their standing in the seed. **They seed the ledger and are not
admissions to it**, and they carry the ruled **COVERAGE** bound, stated where they appear.

> ### ★ 5.4 A FINDING FOR THE WRITING SIDE — THE RULING RECORD'S §3 IS FALSE AT THE OBJECT ON THIS POINT
>
> `cowork_rulings_2026_08_26_sizing_tests_sitting.md` §3 states that test (a)'s *"harvest is additive
> to the 31-admission seed of `cowork_fact_gate_admissions_2026_08_26.md`, **which came from a
> different source entirely**."*
>
> **It did not.** `cowork_empirical_findings_candidates.md` §5 records, of the dead-end corpus:
> *"§8 read whole, `:1129–1457`, at the object"*, yielding *"**10 candidates — C1–C10.** The richest
> source by a wide margin, exactly as plan §6.1 and the ruled seed list predict."* **The largest single
> contributor to the 31-admission seed IS the dead-end corpus**, mined whole on 2026-08-25 and
> dispositioned by the user across three rounds on 2026-08-26.
>
> **The consequence, stated without a recommendation.** Test (a)'s second product is **additive by
> nothing**: every fact it returns was already in the seed. The only §8 item bearing on a statement
> that the seed does not carry is the *"no spelling-bonus window exists"* clause, which fails the gate
> as stated (reading file §2.2 row 9) and whose possible restatement is **named and NOT proposed**,
> because on this record a restatement is the user's to accept.
>
> **This also re-scopes the COVERAGE bound the ruling attaches.** The ruling grounds that bound in the
> contamination — *which* dead ends came up being driven by *which* statements they collided with. That
> is true and is carried. But it is **dominated** by a larger fact measured here: the source had already
> been read whole, independently of any statement, so the statement-driven scope did not narrow the
> harvest below what an unscoped mining had already reached. **Both bounds are stated at the reading
> file §2.4.**

---

## 6. Task 4 — the format test

### 6.1 The five sample statements, and how the two required kinds were located

**Located at the text, by reading the statements — not taken from the output's own §3.3, which was
found to agree afterwards.**

- **The probabilistic factor form is S13**, located by reading the output's §1.3, *"The form of a
  term"*. Its statement field is *"Every term is a conditional probability of an observation given the
  candidate reading — a factor of a likelihood…"*.
- **The conditional-independence premise is S18**, located by reading §1.4, *"How the terms
  combine"*. Its statement field asserts the product form's conditional independence and requires the
  model to declare it per factor group.

**Both kinds are present. No STOP was reached on Task 4(a), no third tractable kind was substituted,
and the test did not proceed on four.**

**The other three were chosen by a stated rule — span the three shapes field six takes across this
output, so the test is not run only on the tractable shape:** **S31** (falsifier = a differential
experiment over a score input), **S8** (falsifier = the model's own internal arithmetic), **S35**
(status *open*).

### 6.2 The judgement, and ★ the finding that governs every row

**Each of the five sub-fields was judged separately per statement; the grid is at the reading file
§3.2.**

> **★ THE ARM AND THE SITE ARE ABSENT FROM ALL THIRTY-SIX STATEMENTS, BY INSTRUCTION — SO THIS OUTPUT
> CANNOT TEST TWO OF THE FIVE SUB-FIELDS AT ALL.** The output's own §1 preamble: *"Field 6 is written
> in terms of an **observable** and a **decision rule over it**; naming code sites is left to a later
> session, **as the brief directs**."* The deriving session opened no code (§5.1).
>
> **Why this matters to the writing side.** The ruling record's §3 grounds running (b) on its being
> *"the only test of fields the plan itself marks UNESTABLISHED"*, and names all five. **Three of the
> five are what this test can reach.** The ARM and the SITE remain untested, and no output produced
> under a brief carrying that instruction can test them.

**The results.** S13, S31 and S35 return field six **returnable** on the reachable sub-fields (S13's
decision rule and S35's observable each with a stated qualification). **S8 returns NOT returnable
without interpretation** on its decision rule and its near-miss: the observable names run-time
candidate scores while the decision rule names *"equal by construction"*, which is a property of the
arithmetic and not of the observation, and the near-miss (*"where the bass is genuinely ambiguous"*)
asks the checker for a musical judgment. **That is a defect IN field six, not an absence of it**, so it
does not put S8 in the UNVERIFIABLE class.

**UNVERIFIABLE.** The output marks **0 of 36**; **none of the five sampled was marked**, and none of
the five is a statement that cannot carry field six. The output's zero is not contradicted by this
sample, and this sample settles nothing about the other thirty-one.

> **★ TWO FURTHER FINDINGS ABOUT THE FORM ITSELF, both at the reading file §3.2 and §3.3.**
>
> **(i) There is a THIRD footing for field six that §7 does not provide for.** The plan gives two —
> behavioural-in-code, and premise-in-the-residual. S18's field six falsifies in **the model's own
> written specification**; S14, S20, S22, S23, S24, S25 and S33 name a document, a fit record or a
> written defense. Neither code nor residual.
>
> **(ii) NO statement of the thirty-six falsifies in the residual.** All thirty-six field-six entries
> were read. Their observables are: a model behaviour or output; the model's parameter set or its
> arithmetic; a fit record; a written record, defense or document; and the order of operations. **The
> output put its premises in field FIVE of every statement and wrote none as a statement of its own**,
> so the residual footing the dispatch directs be used had nothing to attach to. Reported as a property
> of the output, with no verdict on whether it should have been otherwise.

### 6.3 The five separability determinations — Ruling 2

**The test used was stated before it was applied, at the reading file §4:** *a form verdict rests on
the statement's CONTENT if reversing the claim — or substituting a different claim of the same shape,
with field six written in the same words about it — would change the verdict.* A second question is
recorded beside each row: could the verdict have rested on anything **the contamination** could have
supplied (thresholds, constants, code identifiers, baselines, grading conventions)?

| Statement | Determination | Rested on anything the contamination carries? |
|---|---|---|
| **S13** | **SEPARABLE** | No |
| **S18** | **SEPARABLE** | No |
| **S31** | **SEPARABLE** | No |
| **S8** | **SEPARABLE** — recorded explicitly because it is the one row with a failing sub-field; the failure was found in a mismatch between two of field six's own clauses | No |
| **S35** | **SEPARABLE** | No |

**No row returns *cannot separate*. The stop rule of Ruling 2 was live throughout and was not
triggered.** The question *does (b) survive the contamination on its own ground* returns **YES ON THIS
SAMPLE** — five statements of thirty-six, a verdict about **separability only**, and an argued answer
rather than an established one.

---

## 7. Tasks 5–7 — the outputs, the forward bound and the sweep

### 7.1 Every path this batch wrote, and its licence

| path | what | licence |
|---|---|---|
| `ratification_surfaces/cowork_sizing_tests_reading.md` | the reading file, new | §8 fence, named |
| `cc_report_sizing_tests.md` | this file, new | §8 fence, named |
| `STATUS.md` | ONE pointer entry (OI-222 remedy; no count, no identity, no rendered value — D-431), **written BEFORE `--apply`**; the previous batch's entry then moved out by the tool | §8 fence, named |
| `STATUS_ARCHIVE.md` | written by `gen_status_batch_bound.py --apply` | tool output |
| `tools/audit/gen_status_batch_bound.py` | the **five** aiming constants and the appended `PREVIOUS_AIMINGS` row | §8 fence, the named carve-out |
| `tools/audit/status_batch_bound.json` | written by the same run | tool output |
| `tools/audit/evidence_pin_membership.json` | written by `gen_evidence_pin_membership.py` | §8 fence, named |
| `tools/audit/guard_state.json` | written by `gen_guard_state.py` | tool output |
| `tools/audit/guard_classification.json` | written by `gen_guard_classification.py` | tool output |
| `tools/audit/session_start_read_size.json` | written by `gen_session_start_read_size.py` (the one staleness cure) | tool output |
| the three Task 0(c) landings | committed | §8 fence, named |

**Exactly one path under `tools/` ending `.py` is modified**, under the carve-out ruled for it by
name. No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md` edit. No `src/` change, no test changed,
moved or run, no golden, nothing under `tools/corpus/` or `tools/robust_stop/`, no open-items row
created, flipped or discarded, no finding number allocated, no ledger built, created or admitted to.

### 7.2 The forward bound

**The five aiming constants** were re-aimed after reading the tool's own source: `BASE_COMMIT` →
`9683a9c1fe351cde4450bfe63c86d2331a83946b`; `PREVIOUS_BATCH_DISPATCH` →
`cc_instruction_boot_pack_regeneration.md`; `ACT_DATE` unchanged at `2026-08-26`; `DISPATCH` →
`cc_instruction_sizing_tests.md`; `TASK` → `Task 7`. **The outgoing aiming was APPENDED to
`PREVIOUS_AIMINGS` rather than overwritten** (#12), as part of the act the carve-out names.

**★ `TASK` is a choice and it is declared.** This dispatch numbers no task for the forward bound —
§8's fence names the tool without a task number — so `Task 7` (*report and commit*, the batch's close)
was used, because Ruling 4's bound is performed *in the same act that writes this batch's own
entries*. The archive header now reads *"moved verbatim out of `STATUS.md` by
`cc_instruction_sizing_tests.md` Task 7"*, which is true of the close.

`--apply` reported: **entries moved 1, 2,192 characters; byte-present in the archive exactly once
True; absent from the must-read True.** `--check` passes at the final sweep round.

### 7.3 The sweep, with every red named and classified

**Run as ruled: `python tools/audit/gen_guard_state.py`, then
`python tools/audit/gen_guard_classification.py`, in that order** (the classification reads the
artifact the state tool writes and its own STOP requires the order).

**Round 1 — 75 run, 4 failing, 4 not run, 16 historical records.** Every red classified **at its own
captured text**, before anything was touched:

| # | guard | captured text | class | acted |
|---|---|---|---|---|
| 1 | `gen_filing_convention_application.py --check` | `STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md, OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md. An unclassified candidate is a STOP, never a silent pass (D-661).` | **DECISION — the standing `[[OI-372]]` red the dispatch names and forbids curing** | **untouched** |
| 2 | `decisions/apply_soft_discard.py --check` | `STOP: the committed plan's recorded arithmetic disagrees with the data file's: the plan records {'the_live_record_before': 677, 'retired_by_this_act': 165, 'the_live_record_after': 512}, while the block's former population is 680 and 165 record(s) carry this act's own `retired_by`` | **DECISION — standing, named by the dispatch and forbidden to cure** | **untouched** |
| 3 | `decisions/apply_residue_discard.py --check` | `STOP: the sitting's arithmetic does not reconcile at ['the_whole_population', 'the_live_record']: {"the_whole_population": {"keep_plus_retired": 677, "the_sum_the_sitting_states": 677, "the_population_the_data_file_records_before_any_retirement": 680, "it_reconciles": false}, "the_live_record": {"before_this_act": 515, "after_this_act": 477, "the_movement_the_sitting_states": "512 → 474", "it_reconciles": false}} — the ruling makes this a STOP-and-report, not an adjustment` | **DECISION — standing, named by the dispatch and forbidden to cure** | **untouched** |
| 4 | `gen_session_start_read_size.py --check` | `STALE vs the measurement: session_start_read_size.json does not re-derive` | **REGENERATION (staleness), BY CONSTRUCTION — this batch writes to a member of the session-start read** | **regenerated**, under the dispatch's own clause that a staleness red caused by this batch's own writes is cured |

**★ RED 1's CANDIDATE LIST IS UNCHANGED — the same three, no fourth.** Neither this batch's files nor
this report widened it. It was **not** regenerated, **not** run in write mode and **not** investigated.

**Round 2 — the fixpoint: 75 run, 72 passing, 3 failing, 4 not run, 16 historical records.** The
residue is exactly the three standing decision reds above. **Classification: live 69 · point-in-time
16 · neither 2 · live-and-failing 3.**

**No red was ambiguous.** Every one was classifiable at its own captured text, so the dispatch's
*"treat it as a DECISION red and STOP"* clause was never reached.

---

## 8. Departures, declarations, and the one thing that could not be obeyed

### 8.1 ★ THE ORDERED READING-ORDER DEPARTURE COULD NOT ACHIEVE ITS PURPOSE — THE DT-20 SHAPE, ON THIS SESSION

Task 1(a) ordered the blind output read whole **before** the session-start read, on the stated ground
that `CLAUDE.md` *"carries an entire section on this unit's own subject … and reading it first would
frame your view of statements before you have seen them."*

**This session's boot carried `CLAUDE.md` in full, as project instructions, before its first token.**
That is the identical mechanism the graded output records at its own §5.3 and names **DT-20** — *an
instruction whose mandatory or unavoidable preconditions defeat one of its own requirements.*

**What was done.** The order was obeyed to the letter: the output was read whole before `STATUS.md`,
`DECISIONS.md`, `BUILD_AND_TEST.md` and the gating identities were opened. **The instruction was not
substituted, softened or skipped — it was performed and it could not have the effect it was ordered
for.** Whether the grading is affected is not something this session can establish about itself, which
is the position §5.3 takes about its own independence. It is why the separability test at the reading
file §4 asks, per row, whether the verdict could have rested on anything the contamination carries;
**on all five rows the recorded answer is no, and that is an argued answer, not an established one.**

**Named as a condition of this session's own run, not as a proposal.** No verdict, no row, no finding
number.

### 8.2 Neither brief was opened — the reading of Task 6, declared

Task 6 reads *"Do not open the harmony-boundary blind output. Do not touch either pack, the
generator, the manifest, any withheld family, or either brief."* **Read at least as strongly as
*open*, so neither brief was opened.**

The dispatch supplies §5's six bullets in its own words, so nothing was lost. **But the consequence is
declared:** the ruled list at the reading file §1.3 is the **dispatch's relay**, not the brief's own
text, and **the relay and the successor plan's own sizing list at §6.1 are not the same list** — §6.1
reads *"time per statement, statements per unit, share withdrawn, share needing a user ruling, share
whose falsification field could not be written, and a noise measurement"*, while the relay drops
*share withdrawn* and adds three fields §6.1 does not name. **Which of the two the brief's §5 carries
cannot be established from inside this batch.**

### 8.3 The `44 of 241` value is relayed, not re-measured

The output states **241** entry headings and reports its stop point by identifier and by position; **it
does not state the number 44.** That number is the ruling record's and the dispatch's. Verifying it
would require opening the boot pack, which Task 6 forbids. **Relayed with that bound, at the reading
file §1.1.**

### 8.4 The entries were CITED rather than transcribed, and the ground is declared

Task 3(c) orders product two *"written in the ledger's ruled entry shape"*. **The five-field shape is
quoted whole before any entry appears, and the entries are then presented by identifier with the place
their five fields stand — not retyped.** The ground: every passing fact already stands in the shape at
`cowork_empirical_findings_candidates.md`, and `cowork_fact_gate_admissions_2026_08_26.md` refused
exactly that retyping one act ago, under the same Ruling 8, in these words — *"No fact is transcribed
here… Retyping one would be the transcription the record forbids (D-431), and it would let the two
copies drift."* **Following that precedent rather than inventing a second discipline (#6).** Declared
here because it is a departure from the instruction's letter, taken for a stated reason and not to
avoid work.

### 8.5 The register entry this batch's ruling implies is OWED and is NOT written

The dispatch names it and orders no entry: Ruling 1 changes a hold status, which is register business
of the same kind as the phase-status change entered as **D-680**. **It is not written here.** No
identifier was consumed and no class was chosen. It joins the five already owed from the sixty-sixth
handoff entry. **Curing what blocks it — the two mutually unsatisfiable discard-act checks above — is a
decision act and is not this batch's.**

### 8.6 Oracle awareness for the OTHER unit, declared

Reading `cowork_handoff.md`'s sixty-sixth entry (required, because this batch commits that file) and
the ruling record's own §6 both put in front of this session the writing side's declaration about the
**harmony-boundary** unit's evidence ranking. **That unit is not graded here, its blind output was not
opened, and nothing about it appears in this batch's output.** Declared so the exposure is on the
record rather than discovered later. For the **scoring-model** unit the question does not arise: its
withheld family is ruled EMPTY.

### 8.7 Shell use, stated exactly

**No `git status`, no `git diff`, and no shell text utility on a repository working-tree file.**
Repository content was read with the file tools throughout; the armed guard denied one attempt to name
repository paths inside interpreter code and the read was re-taken with the file tools.

**What the shell was used for, in full:** read-only git OBJECT queries by explicit hash
(`git ls-tree -l`, `git cat-file -p`, piped to `sha256sum`); `git add` and `git commit` for the ordered
landing; `git log -1 --format=%H` to name the commit just written — **cross-checked at
`.git/refs/heads/master` with the file tool, and the two agree**; and the ordered `python tools/...`
runs.

**One boundary declared for the writing side to rule on if it wishes:** shell utilities (`grep`, `wc`,
`tail`, `awk`) were used on **tool stdout captured to files in the session scratchpad outside the
repository**, never on a repository path. D-253's subject is working-tree files and the guard did not
fire; the practice is named so it is a declared reading rather than an unnoticed one.

### 8.8 What was NOT done, in terms

No comparison against the code or against any specification. No measurement of the analysis built,
designed, scoped or run — **these tests are TEXTUAL**. No derivation. The harmony-boundary blind output
not opened. Neither pack, the generator, the manifest and every withheld family untouched. **The three
ruled annotated pairs and the BWV 301 score were not opened either** — none of the five sampled
statements names one in its own text, so the permission was never needed, and nothing was run over
them. No recommendation appears anywhere in the reading file or in this report.

### 8.9 Nothing else could not be obeyed, and the §8 fence was not reached

**No instruction required a write outside the fence.** No route was chosen in place of one, no fence
was widened, and no weaker form of an instruction was substituted — except the one declared at §8.4,
which is a departure from an instruction's letter taken openly and for a stated reason, and which the
writing side may disallow.

---

## 9. The tree at this report's writing

`python tools/audit/changed_paths.py` at the time this report was written, with it on disk:

- **start state:** 836 records — 835 untracked, 1 tracked-modified (`cowork_handoff.md`).
- **the landing commit** took the three named paths, leaving 833 untracked and **0** tracked
  modifications.
- **this batch then wrote** the reading file and this report (2 new untracked paths) and modified
  `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py` and six generated
  artifacts, of which those already tracked appear as tracked modifications.

## 10. The closing measurement, taken with this report on disk

`python tools/audit/changed_paths.py` → **842 changed path record(s) [worktree]**:

| | count | which |
|---|---|---|
| untracked (`??`) | **835** | the standing population (833 after the landing commit) **plus this batch's two new files** — the reading file and this report |
| tracked, modified (` M`) | **7** | `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`, `tools/audit/evidence_pin_membership.json`, `tools/audit/guard_state.json`, `tools/audit/session_start_read_size.json` |

**Every one of the seven is inside the §8 fence** — three named in it, four written by a tool this
dispatch ordered run. **The arithmetic closes against the start state:** 836 records at the start
(835 untracked + 1 tracked-modified); the landing commit took three paths out (two untracked, one
tracked-modified), leaving 833 untracked and zero tracked modifications; this batch then added two
untracked files and seven tracked modifications — 835 + 7 = **842**.

**Nothing of the standing untracked population is committed by this batch.**

**The sweep was run a THIRD time with this report on disk** and returns the same fixpoint — 75 run,
72 passing, 3 failing, 4 not run, 16 historical records — with the standing red's candidate list
re-checked and **unchanged: the same three, no fourth.**

**The end state is NOT asserted by the commit that carries this file**, because a commit cannot assert
its own end state; the measurement above is the state at the moment the report was written, which is
the state that commit takes.

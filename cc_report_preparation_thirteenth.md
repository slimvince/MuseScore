# CC report — the preparation phase's THIRTEENTH batch: **COMPLETE**

> **Dispatch `cc_instruction_preparation_thirteenth.md` (Cowork, 2026-08-19), read in full by CC on
> 2026-08-19.** Four task commits, Tasks 0 through 3, the close being a task commit with its own
> entry — plus ONE FURTHER commit carrying the end-state guard run, whose values this report does
> not state until **§12**, appended after that run and that commit exist.
>
> **Nothing in this report is a claim about the analysis.** No `src/` change, no golden, no test
> changed, moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the
> analysis built, designed, scoped or run. **No open-items row was created, flipped or discarded.**
> Every figure below is cited to a generated artifact or to a content-addressed git object, and none
> is transcribed from memory (**D-431**).
>
> **★ THE THREE THINGS TO READ FIRST, because they are what the writing side is owed.**
> **(1)** Task 2's derivation returned the first expectation as **ESTABLISHED**, derived at the tool
> and at its artifact — so the derived gating answer a session reads at boot is on the established
> side and F84 does not reach it — §4.c. **(2)** The sort's member test needed **TWO corrections**,
> both recorded at the tool as corrections with one ground between them, and one of them was forced
> by the derivation **failing to see itself** — §4.e, and it is the one thing here that most
> deserves a second opinion. **(3)** This batch allocated **no new finding number**; what it carries
> is at §9.

---

## 1. The reading

`CLAUDE.md` and `STATUS.md` **as they stood, in full**. `DECISIONS.md` in full — unconditional and
explicitly not demoted. `BUILD_AND_TEST.md` in full, because this batch MEETS its condition: it runs
the guard set, whose commands live there.

**The whole open-items INDEX was NOT read.** Rule (a)'s derived gating answer was read at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`, narrowed to
its identity list. **No verdict was challenged, so the grounds at `the_gating_rows` were not opened.**

**The standing clause was obeyed:** `cowork_handoff.md`, its **THIRTY-SECOND** block, was read. That
is what told this session the findings series stands at **F87** and that numbering begins at **F88**.

Then, as the dispatch orders, in full: `cowork_rulings_2026_08_19_twelfth_return.md`;
`cc_report_preparation_twelfth.md`, its §5 and §10 above all — §5 because Task 2 generalizes what it
built, §10 because F84 is the ground of the clause Task 1 lands;
`cowork_rulings_2026_08_19_eleventh_return.md`; and **`cowork_audit_protocol.md`'s dispatch-protocol
section in full**, so that all SEVEN standing clauses were met before an eighth was written.

The artifacts the dispatch orders binding at were read at their own text:
`tools/audit/epoch_write_path.json` and its generator, `tools/audit/nongating_apparatus_rows.json`
(**read and never written**), `tools/audit/evidence_pin_membership.json` and its generator,
`tools/audit/guard_classification.json` and `tools/audit/guard_state.json`.

---

## 2. Task 0 — the four paths, and the membership check cleared in the same act

**`ae55748557`, parent `16a172715a`, pushed, 4 paths** (2 modifications, 2 additions; no staging
override).

### 2.a The declared start state matched at the tree

Taken **before any edit, at a quiet tree**, by `python tools/audit/gen_guard_state.py --check`
followed by `python tools/audit/gen_guard_classification.py --check`:

| | run | passing | failing | not run | historical | STOPs |
|---|---:|---:|---:|---:|---:|---:|
| declared by the dispatch | 72 | 70 | 2 | 4 | 16 | 0 |
| **measured, before any edit** | 72 | **70** | **2** | 4 | 16 | 0 |

Both reds are the ones the dispatch names with their causes —
`gen_filing_convention_application.py --check` ([[OI-372]]) and
`gen_evidence_pin_membership.py --check`, whose artifact is STALE because this dispatch's own
untracked ruling record already sits inside a derivation whose population is the file system. The
guard classification re-derives, exactly as declared.

**The guard registry's own drift was NAMED BY THE DISPATCH this time rather than left** — F83 applied
rather than repeated. `gen_guard_state.py --check` opens with *"STALE vs the run"* because the
committed registry records the twelfth batch's end state, one failing, while the tree has two. It is
not a third failing check: the runner is not a subject of its own run.

### 2.b Assumption A1 — HELD, checked first and entirely at content-addressed objects

`tools/audit/changed_paths.py` reports **exactly ONE tracked modification in the whole working
tree** — `cowork_handoff.md`. `tools/audit/evidence_pin_membership.json` is **not among the
modifications**, which is A1's expected-unmodified path holding, proven at the object.

| | blob |
|---|---|
| `cowork_handoff.md` committed at `16a172715a` | `bf31a8007ef93625792bc9bb23885e0035fbe845` |
| working copy, content-addressed | `ada40e360210c68fea1825bfcbbb5006d44fe065` |

The difference, measured blob against blob, is **ONE contiguous changed passage — 181 insertions and
1 deletion** — carrying both parts A1's own sentence names: the THIRTY-SECOND block inserted, and the
THIRTY-FIRST heading's entry-point demotion marker, the single deletion being that heading in its
undemoted form. **No changed-passage count was asserted in advance** (the F25 lesson). **The F57
caveat was applied rather than assumed:** git's own check-in normalisation warning establishes the
working copy is stored LF, so the two blob hashes are directly comparable.

The two invariant paths were content-addressed in the same act and match the terminus:
`OPEN_ITEMS.md` at `6ae67d8603` and `tools/audit/nongating_apparatus_rows.json` at `5bb43d0b3a`.

A1's untracked half held as the tree carries it — the two files to land are untracked, and the wider
untracked population (`cc_instruction_*.md`, `cc_*_report.md`, `cc_*_dossier.md`, a scratch
directory) was touched by nothing this batch did. **A1's STOP condition is scoped to TRACKED paths**,
and the tracked half held exactly.

### 2.c The regeneration's difference, measured before it was accepted

| | blob |
|---|---|
| committed at `16a172715a` | `bb3a43237d5563a0e25969d0c3eb83216e4ce387` |
| regenerated at this tree | `28d6b7f048120b6bc495726a1c206332307ddd78` |

**NO VERDICT MOVED.** Members stay at **7**, pinned at **5**, UNRESOLVED at **0**; every member's
route, document, pin constant and state is byte-identical.

The difference is **TWO hunks, and the dispatch's prediction names both**:

1. `"ruling_records_read": 39` → `40` — route A, predicted.
2. One name added to `ruling_records_read` — route A, predicted.

**★ ROUTE B'S HALF WAS ESTABLISHED AT THE RECORD'S OWN TEXT BEFORE THE RUN, not merely observed
afterwards.** The new ruling record carries three lines containing *pinned*; the only one that also
carries a backtick-quoted name names `tools/audit/epoch_write_path.json`, a `.json` artifact, and the
tool's route-B resolver matches a backtick-quoted `*.py` only. **So route B was predicted to add
nothing, and adds nothing — no third hunk.**

At the tree this commit carries, `gen_evidence_pin_membership.py --check` prints *"the evidence pin's
class membership re-derives"*, so the guard set stands at **72 run, 71 passing, ONE failing** from
Task 0 onward.

---

## 3. Task 1 — the EIGHTH standing clause, at the home the record already makes one

**`2a909b47c2`, parent `ae55748557`, pushed, 4 paths.**

### 3.a The clause, its placement, its grounds and its bound

The clause stands at `cowork_audit_protocol.md`'s dispatch-protocol section: **a recognizer over a
population states, at its own artifact, whether an independently-known population exists to reconcile
against — and where none does, it publishes its output as a LOWER BOUND with its reach declared
UNMEASURED, never as a census.**

**The placement is stated at the site**, on the siting logic its own neighbours use of themselves: it
stands beside the three sections saying what a MECHANISM, a COMPLETENESS CLAIM and an ENUMERATING
PATTERN are each worth unmeasured — and it supplies the test the completeness rule leaves open, that
rule demanding a measured miss rate against a seed without saying what is owed where the record holds
no second enumeration to measure against.

**F84 is recorded as its ground** with its measured instance, and **F87 as the test it rests on**,
measured on three. Both general forms are stated at the site: *a recognizer's reach is measured by the
instances it FAILS to find, never by the ones it does*, and *establishment needs a SECOND, INDEPENDENT
enumeration of the same population.*

**The bound is stated at the site** — it binds a recognizer written or touched from here, and existing
recognizers' own artifacts are NOT retro-fitted, because the sort carries the per-recognizer verdict
so the information has ONE home (#6) and retro-fitting a population under the standing mechanism
freeze would be tool work that blocks nothing. **The cost the user accepted rides with it:** the
clause CLASSIFIES exposure and does not MEASURE it.

### 3.b The anchored-quote class fired and was cleared by its ruled treatment

20 register home anchors drifted, all into this file. Every one was re-aimed **per citation** from the
drift report's own reported start line, through the applier that reads the verifier's own machinery —
**never by an assumed uniform shift**, and the fact that all twenty happen to sit at the same offset
is a property of the single insertion point rather than a shift applied.

The drift authority reports **474/474** verbatim quotes at their cited home and **468/468** cited line
numbers correct, against **448/468** measured after the edit and before the re-aim.

### 3.c Every regenerated artifact's difference, measured before it was accepted

| artifact | before → after | difference | every changed line carries a `cowork_audit_protocol.md` coordinate |
|---|---|---|---|
| `tools/audit/decisions/backbone_decisions.json` | `ec760474d6` → `f4b452fa93` | 20 insertions, 20 deletions | 40 / 40 |
| `decisions/group_T.md` | `ca85557b1f` → `97a721c1ac` | 20 insertions, 20 deletions | 40 / 40 |
| `tools/audit/rulings_sort_classification.json` | `2ab15465ce` → `de49e85312` | 40 insertions, 40 deletions | 80 / 80 |

**Counted rather than sampled.** The sort artifact's count is twice the others because each entry
carries the coordinate in two fields. `DECISIONS.md` is **byte-unchanged**, the INDEX naming homes
without a line, and **no other group file moved**.

**★ One departure declared rather than absorbed (F85 recurring).** The sort generator has ONE write
path for TWO outputs, so regenerating the classification also rewrote the ruling surface it renders.
**The surface came out BYTE-IDENTICAL to its committed object `5c62e70a38`, proven rather than
assumed**, and all **27** documents under `ratification_surfaces/` were content-addressed and match
their committed objects exactly.

---

## 4. Task 2 — the recognizer sort, derived, published as data, authorizing nothing

**`a33a933404`, parent `2a909b47c2`, pushed, 5 paths.**

### 4.a A3 checked first

The walk enumerates. A walk that enumerated nothing would raise and publish nothing, which is A3's own
stated condition.

### 4.b The derivation, and what it is bounded by

The population is **DERIVED from the tools' own syntax trees, never hand-listed**. The walk and the
own-output recognizer are **IMPORTED from `gen_epoch_write_path.py`**, which already owns them and
whose own artifact establishes them, rather than written a second time (**#6**) — which is what
"generalizes §5" means here.

A tool is a member when all three hold: it **writes an artifact of its own**; it draws candidates from
an **enumeration source it does not itself write**; and it decides membership or class with a
**recognizer**. Per member the artifact publishes what population it claims to describe — quoted from
the tool's own docstring, never authored by this session — what enumerates its candidates
independently, every set operation guarded by a raise, whether two of them form a reversed pair,
whether a side of that pair is authored inside the tool, whether it halts, and the verdict.

**Every count is at `tools/audit/recognizer_establishment_sort.json` and none is restated here
(D-431).** The artifact states its own bound: it reads SOURCE and never a run; the authored-side test
expands ONE level of local assignment, and a collection reached through two or more intermediate names
would read as non-authored — **the DANGEROUS direction, named as such**; a reconciliation is
recognised only where the set operation is guarded by a raise; a computed path or key carries no
literal to find; and **the membership recognizer's own reach beyond the three seeds is UNMEASURED.**

### 4.c ★ The first expectation, DERIVED and not inherited

`gen_nongating_apparatus_rows.py` derives **ESTABLISHED**. That was established **at the tool and at
its artifact**, not taken from the dispatch or from the ruling record: its candidate population is the
PARSED INDEX (`INDEX = ROOT / "OPEN_ITEMS.md"`, read with `read_text` at its own parser), and it
reconciles against that parse **in both directions with a halt** — none in both, none in neither,
every gating identity an open row of it, every gating row carrying a ground, and a row it cannot place
raising rather than being defaulted silently.

**So the derived gating answer a session reads at boot is on the ESTABLISHED side, and F84 does not
reach it.** That is the load-bearing consequence, because that answer replaced the whole-index read
for every session on both sides.

### 4.d MIXED is expressible and is used; and the two non-seed ESTABLISHED members were checked

`gen_evidence_pin_membership.py` — the known instance — derives **MIXED**: established on its
population, an external file-system enumeration published whole as `ruling_records_read`, and
unestablished on its classification, which is its own regular expressions over record text. Its one
set-difference is single-directional and is published rather than raised on.

**The two ESTABLISHED members that are not the seed were checked against the record's own description
of them rather than taken from the derivation**, because ESTABLISHED is the direction where a false
verdict does damage: `gen_decisions_filter.py` reconciles its population against the rendered INDEX in
both directions with a raise, and `gen_rulings_sort.py` reconciles the imported filter population
against the register's data file in both directions with a raise. Both readings agree with what the
guard registry's own authored entries say those tools do.

### 4.e ★ Two corrections to the member test — recorded as corrections, with ONE ground between them

**This is the part of the batch that most deserves a second opinion, and it is reported first rather
than buried.** Parts (ii) and (iii) of the member test were first written to read a tool's own source
alone. Each was refuted by a case the record itself produces:

- **(iii)** — the first establishment seed derived as **NOT A MEMBER**.
  `gen_nongating_apparatus_rows.py` imports the row split and the leading-token test from
  `index_status_lint.py`, under an explicit **#6** comment saying those live in ONE place.
- **(ii)** — **the derivation could not see ITSELF.** Its own walk is imported from
  `gen_epoch_write_path.py`, which owns it (#6), so no walk appears in its own source and it failed
  its own member test — while the ruled clause requires it to declare its own status under the very
  test it applies.

**The ground is the same in both places and it is this project's own #6:** a walk or a recognizer with
several users is given ONE home and imported, so a test reading a tool's own source alone reports
every tool that FOLLOWS that rule as drawing on nothing and recognizing nothing. **Neither widening
was made to make a seed pass** — that would be the defect the catalog names DT-2 — and in both places
the two cases are published **separately** per member, at `found_in` and at
`where_its_placement_recognizer_lives`, so a reader sees which it is rather than taking the
derivation's word for it. Both corrections are recorded **at the tool**, in its docstring, as
corrections and not as the first writing.

A third instance of the same blind spot followed and was fixed on the same ground: the
candidate-collection detector did not follow an imported walking helper, which made the sort derive
the wrong verdict **about itself** — see §4.f.

### 4.f ★ The sort declares its own status under its own test, and that is DERIVED rather than asserted

The sort is a member of its own population and places **itself**. Its population — every `*.py` under
`tools/` — is externally enumerable and is **published whole**; which of those tools it classes as a
recognizer over a population is **its own** classification, and nothing outside it enumerates that.
So it derives **MIXED**, and **its member list is published as a LOWER BOUND with its reach declared
UNMEASURED, never as a census.**

**The declaration and the derivation must AGREE, and a disagreement HALTS the run.** That guard is
what caught the third blind spot: before the candidate-detector was corrected, the tool declared
itself MIXED while its own test derived NO INDEPENDENTLY-KNOWN POPULATION for it. **The declaration
was not edited to match the derivation, and the derivation was not bent to match the declaration** —
the substantive question was settled first (its candidate enumeration *is* published whole, at
`the_candidate_population_walked`), and the detector was corrected because it was wrong on that fact.

### 4.g All three STOPs were shown both to FIRE and to stay QUIET (#19)

By probes run **outside the repository**, in check mode so nothing was written:

| STOP | fired |
|---|---|
| an establishment seed that stops deriving to its established side | **yes** |
| an authored unplaced reason naming a member the derivation now places | **yes** |
| a self-declaration the tool's own test does not support | **yes** |

and the derivation stays **quiet on the tree as it stands**. The third probe was **confounded on its
first attempt** — mutating the verdict constant disturbed the seeds, so the seed STOP fired first and
the wrong thing was tested — and it was re-run in isolation rather than accepted.

### 4.h This task corrected nothing, and the new-tool rule is discharged in the same commit

**No recognizer is edited, widened or acted on, no enumerated member's artifact is written, and no
member is owed by appearing.** The published sort is the standing input to a later ruled act.

The new-tool rule was discharged in the same commit: the authored run-instruction in
`gen_guard_state.py` and the authored classification verdict in `gen_guard_classification.py`. **The
guard count rises by exactly that one invocation, 72 to 73.**

### 4.i One consequence, measured and declared

`tools/audit/epoch_write_path.json` was regenerated because its population is the **file system** and
this task's own new tool entered it. Its whole difference, measured blob against blob
`253ad79963` → `4debec9910`, is **ONE hunk** — `tools_walked` rising by one — with **no member,
verdict, seed or unplaced entry moving**, and the new tool correctly not an epoch member. **That is
an ADDITION caused by the ordered act**, which is the sharpened bar's own case rather than an
exception to it.

---

## 5. Task 3 — the close

**Four `STATUS.md` pointer entries, one per task**, and **in the same act Ruling 4's forward bound
moves the TWELFTH batch's entries verbatim to `STATUS_ARCHIVE.md`**. `gen_status_batch_bound.py` was
re-aimed at this batch's own base commit `a33a933404`, its every previous aiming kept rather than
replaced (#12). The tool reports **6 entries moved, 7,017 characters**, and **both directions
proven**: every moved entry byte-present in the archive exactly once, and every moved entry absent
from the must-read. **The declared `Last updated: ` prefix adjustment is IMPORTED and not re-decided
(#6)**, and no entry needed a second adjustment — the tool's own occurrence test would have STOPPED
on one.

The FULL close is appended to `cowork_away_returns.md` as **THE PREPARATION THIRTEENTH BATCH**, and
**it does not assert the end state**: a block at its head states that the end-state run is taken after
the commit carrying it exists and that its values land in ONE FURTHER commit.

**The two do-nothings are recorded as ruled decisions**, in the close at §4 and here at §6.

---

## 6. ★ The two do-nothings, recorded as decisions

**(a) Ruling 2 — the three UNPLACED members of `tools/audit/epoch_write_path.json` STAY UNPLACED.**
No verdict was added, no recognizer was widened, no member was acted on. **The ground recorded:** the
unplaced set is self-maintaining through its both-ways halt — an unplaced member with no authored
reason halts the run, and an authored reason naming a member the derivation now places halts it too —
so a new unrecognised shape cannot enter silently and an authored reason cannot outlive its subject.
**#19** is already served, the members having been returned rather than guessed. Widening the
recognizer to place the two builder-default members was declined because **it is F84's own hazard
repeated**: a widened recognizer still has no independently-known population, so widening buys
coverage nobody can measure while making the artifact read as more complete than it is.

**(b) Ruling 3 — no blob resolution form was added to `gen_evidence_pin_membership.py`.** The ruling
record is the authority and the artifact points at it. **The ground recorded:** the
index-plus-detail shape this record already uses twice — the open-items register's INDEX with its
detail files, and the decisions register's INDEX with its group files. Adding a resolution form would
spend tool work that blocks nothing and would widen a recognizer's resolution forms in the very
sitting that ruled recognizer-widening the thing to be careful about. **The cost accepted:** a reader
of the membership artifact alone must open the ruling record. **Nothing is foreclosed.**

---

## 7. The registered expectations

| | verdict |
|---|---|
| **E0** | **MET.** Exactly 4 paths — two modifications matching A1's shape and the bounded regeneration, two additions, no staging override — and the membership check passing at the resulting tree, so the guard set stands at 72 run, 71 passing, ONE failing from Task 0 onward. **The prediction held on BOTH routes**, with no third hunk, and route B's half was established at the record's own text BEFORE the run rather than observed after it. |
| **E1** | **MET.** The clause stands at the dispatch-protocol section with its two named grounds, its two general forms and its bound; no other authoring rule moved; the drift authority reports every re-aimed anchor correct at its new coordinate. |
| **E2** | **MET.** The population is derived and every member placed with its evidence; MIXED expressible and used where it applies; `gen_nongating_apparatus_rows.py` derived as ESTABLISHED at the tool and at its artifact rather than inherited; **the sort's own status declared under its own test, as a lower bound with UNMEASURED reach, and DERIVED rather than asserted with a halt behind it**; no recognizer edited or acted on; the new measurement tool registered in the act that created it, with the guard count's movement caused and named. |
| **E3** | **NOT GRADED IN THIS COMMIT, BY DESIGN.** The end-state run is taken after the commit carrying this report exists, and its values and E3's grade land in ONE FURTHER commit as §12. Grading it here would be the very defect **F79** records. |

---

## 8. The declared departures

1. **A new measurement tool was built under the standing mechanism freeze** (Task 2), declared as a
   judgment at the site, in the commit message, in the close and here. A DERIVED enumeration
   published as data is not performable without one; the dispatch's own step 6 anticipates it.
2. **`tools/audit/epoch_write_path.json` was regenerated inside Task 2**, its difference measured
   before acceptance and its cause named (§4.i).
3. **A generator with one write path for two outputs also rewrote a ruling surface** (Task 1); the
   surface came out byte-identical, proven rather than assumed (F85).
4. **The guard registry and its classification are regenerated in the FURTHER commit**, at the quiet
   tree, together with the end-state run that produces their values — never before it. They were
   deliberately **restored to their committed state** before Task 2 was committed, so that only the
   intended paths moved.
5. **Working-tree files were content-addressed into the object database** (`git hash-object -w`) so
   that both sides of every blob comparison are content-addressed — the route the three preceding
   batches used, imported rather than re-invented.
6. **Three shell invocations were refused by the armed guard** — a variable-carrying path and two
   interpreter bodies naming repository paths. Each was re-taken through the sanctioned route and
   **none was worked around**; the deny-on-indeterminate policy behaved exactly as **D-647** states.
7. **One write was attempted through shell redirection and ABANDONED rather than retried:** the close
   was written with the file tools, the recorded 2026-08-02 slip not repeated and the twelfth batch's
   own remedy imported.

---

## 9. Findings — **no new number was allocated this batch**

The dispatch bars creating an open-items row and this session created none. **The row bar stands
whole: no row was created, flipped or discarded, and no finding is rowed.**

**This batch allocated no new finding number.** Numbering was to begin at F88; nothing this session
met was a new general form rather than an instance of one already on the record. What it met:

- **F84** — the ground of the clause Task 1 landed, and the thing Task 2's own two corrections are
  further instances of: a recognizer written from what its author can see recognises what its author
  can see. It bit **three times inside this batch**, each time in the same shape — an imported helper
  the recognizer did not follow — and each time it was found by seeking a case the recognizer did
  NOT return rather than by checking the ones it did.
- **F87** — the test that clause rests on, applied per member by Task 2's derivation.
- **F83** — applied rather than repeated: the dispatch's declared start state named the guard
  registry's own drift with its cause.
- **F82** — applied rather than repeated: A1 named the untracked population as the tree carries it.
- **F85** — recurring, declared at §3.c.
- **F3 FIRED AGAIN, in Task 1** — `reaim_home_anchors.py --check` exited 0 while printing 20 drifted
  anchors. **Sixteenth surfacing; still unfixed and unrowed**, with
  `gen_cluster_dispositions.py --verify` the drift authority throughout.
- **F25 did not repeat. F57 was applied rather than assumed** at §2.b. **F79 did not repeat** — the
  end state is not asserted in the close.

**F1–F87 ride to the preparation phase's retrospective unchanged**, with the E3 ordering defect and
the A1 premise error.

---

## 10. What the writing side is owed, stated as questions rather than as recommendations

The record does not settle these, so no recommendation is made (**D-658**).

1. **The sort's member test was corrected three times during the task** (§4.e, §4.f), each time on
   the same #6 ground and each time because an imported helper was not followed. All three
   corrections are recorded at the tool. **The question is whether the writing side wants the
   corrections reviewed as a class** — they widen what counts as a recognizer over a population, and
   a wider member test produces a larger published population, which is a change to what the sort
   claims rather than to how it claims it.
2. **The sort's reach is UNMEASURED and says so**, which is the ruled clause working. Whether
   anything is wanted about the 37-plus members it places on the no-external-population side is not
   settled by anything here: the ruling says the result authorizes NOTHING, and nothing was done with
   them.
3. **The one-level authored-side expansion is the sort's own most dangerous bound** (§4.b), because
   its error direction is toward a false ESTABLISHED. Two of the three ESTABLISHED members were
   checked by hand against the record's own descriptions (§4.d); **whether that check should be
   mechanical is a question, not a defect I can close.**

---

## 11. The self-check over this session's whole diff (`CLAUDE.md`, the standing self-check)

The diff of every touched file was re-read before this report was written, not the memory of writing
it. Checked against the principles, the conventions and the gate and threshold policies:

**#19** governs the new derivation: three seeds re-checked on every run, its reach beyond them
declared UNMEASURED, all three STOPs shown both to fire and to stay quiet, and its own status about
itself derived rather than asserted with a halt behind it. **#6** is why the walk and the own-output
recognizer are imported rather than re-written, why the clause landed at ONE home, and — twice over —
why the member test had to follow an imported helper at all. **#12** governs every correction: the
tool's own docstring records both member-test widenings **as corrections**, with what was first
written and why it was wrong, rather than presenting the corrected form as the first one; and every
previous aiming of the batch-bound tool is kept. **#13** is what §4.e and §4.f are — a surprise
surfaced rather than built around. **#15** is why every commit was verified at the object and every
difference taken between two content-addressed objects. **DT-2** is named explicitly at the tool,
because widening a test after a seed fails is exactly the shape DT-2 forbids and the ground had to be
independent of the seed. **D-431** is why every figure enters by citation.

**D-253 was obeyed** — every working-tree read went through the file tools, and every shell
invocation was a content-addressed git object query, a per-path git query, a git write, or a
committed measurement tool. **Three shell invocations were refused by the armed guard**; each was
re-taken through the sanctioned route and none was worked around. **One write was attempted through
shell redirection and abandoned rather than retried.**

**The reserved-word conventions bind this document**: *measurement tool* never *instrument*, *the
open-items register* in full, *value* rather than the numerical sense of the collided word, and
*TOWARDS* rather than *against* wherever a rating is stated. **The vocabulary rule of 2026-08-17
binds every line written this batch.**

**Nothing this batch did touches the analysis, its inputs, or any measurement tool the analysis
depends on.**

---

## 12. The chain, and where the end state is NOT

| | commit | parent | paths |
|---|---|---|---|
| Task 0 | `ae55748557` | `16a172715a` | 4 |
| Task 1 | `2a909b47c2` | `ae55748557` | 4 |
| Task 2 | `a33a933404` | `2a909b47c2` | 5 |
| Task 3 — the close and this report | the commit that carries this section, whose own identity it cannot contain | `a33a933404` | — |

Every commit named above was verified at the object by explicit hash — its parent confirmed and its
path count read from the object, never from the memory of making it (**#15**).

**★ THE END STATE IS NOT IN THIS SECTION, AND THAT IS DELIBERATE.** The end-state guard run is taken
AFTER the commit carrying this report exists, at the quiet tree it leaves; **its values, the sequence
that produced them, and E3's grade land in ONE FURTHER commit as §13 below.** No row, no cell and no
sentence here states what that run returned. **This is the E-ordering rule at both grains** — the
rule is not satisfied by taking the run late if the sentence about the run was written early, and the
cheapest test of whether it has been obeyed is whether the sentence could have been wrong.

**Read the chain at the branch tip, never at this table** — a commit cannot contain its own identity,
so this table is one commit short of the tip by construction, and the further commit is not written
yet.

---

*Provenance: CC, 2026-08-19, executing `cc_instruction_preparation_thirteenth.md`. Every commit hash
above was read at the object by explicit hash; every blob comparison was taken between two
content-addressed objects; every guard figure in §2.a comes from the run recorded there. **No
end-state value is stated in the commit that carries §1–§12.***

---

## 13. The end state — appended AFTER the run that produced it, in the ONE FURTHER commit

**The close commit is `1fdce14fdd`, parent `a33a933404`, pushed, 6 paths** — verified at the object,
its parent confirmed and its path count read from the object. Its own identity could not be written
into it, which is why it is stated here.

**THE SEQUENCE IS RECORDED RATHER THAN THE SUMMARY, because the sequence is the evidence.** Every run
below was taken at the quiet tree the close commit left, and every value was read off the run, never
inferred:

1. **`gen_session_start_read_size.py --check` went RED on the first end-state run** — *"STALE vs the
   measurement"* — **expected, and F79's own instance**: Task 3's close moves `STATUS.md`, a member of
   the read that tool measures. **Cleared by regenerating the measurement and by nothing else**; the
   re-check then prints *"the session-start read measurement re-derives"*, with rule (a)'s
   artifact-and-key pointer still resolving.
2. **The full guard set then returned: `73 guard(s) run, 1 failing, 4 not run, 16 historical
   record(s)`** — the ONE failing being `[FAIL] tools/audit/gen_filing_convention_application.py
   --check`, [[OI-372]]'s tool and no other — with **ZERO STOPs**.
3. **The guard registry was then regenerated in write mode at that same tree, and the classification
   AFTER it** — the order the classification's own STOP requires. `gen_guard_state.py --check` now
   prints *"the guard state re-derives"*, which it did **NOT** at this batch's start state (§2.a,
   F83), and `gen_guard_classification.py --check` prints *"the guard classification re-derives"*.

| | run | passing | failing | not run | historical | STOPs |
|---|---:|---:|---:|---:|---:|---:|
| start state, before any edit | 72 | 70 | 2 | 4 | 16 | 0 |
| **end state, at the quiet tree the close left** | **73** | **72** | **1** | 4 | 16 | **0** |

**The guard population rose by exactly one invocation**, which is Task 2's new measurement tool
registered in the act that created it, and the two start-state reds are down to the one standing red
the record already carries.

**★ F86 DID NOT RECUR, and that is a consequence of the order rather than luck.** The new tool's
`state_at_the_committed_tree` cell in `guard_classification.json` reads **`PASS`**, not `unknown`,
because the registry was regenerated **before** the classification read it. The twelfth batch had to
declare that cell as `unknown` and resolve it in its own further commit; here the ordering resolved
it in one pass.

**E3 — MET**, on that run and on nothing else.

**★ THIS SECTION WAS WRITTEN AFTER THE RUNS AND AFTER THE CLOSE COMMIT EXISTED**, and the commit
carrying it cannot contain its own identity — the regress ends where the record's own precedent ends
it, with git carrying what a sentence cannot. **No sentence asserting the end state was written
before the run that produced it existed**, which is the E-ordering rule at both grains and the remedy
F79 names.

*Provenance: CC, 2026-08-19, appended in the ONE FURTHER commit after `1fdce14fdd`. Every value in
this section was read from the runs recorded above at the quiet tree that commit left; the close
commit's hash, parent and path count were read at the object by explicit hash.*

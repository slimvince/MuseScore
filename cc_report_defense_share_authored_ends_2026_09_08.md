# CC REPORT — the defense-share measurement's clause ENDS become AUTHORED

**Dispatch:** `cc_instruction_defense_share_authored_ends_2026_09_08.md`.
**Base:** `cdd7ff4aca948156291725c76535bedfd84d9be5`, read at `.git/refs/heads/master` with the file
tools and unmoved when this batch started — the tip the dispatch names.
**Ran:** 2026-09-09. **The dispatch is dated 2026-09-08 and this batch ran the day after**, which is
recorded because one authored field of the forward bound turns on exactly that difference.

---

## 0. The commits

| # | Commit | What it carries |
|---|---|---|
| A | `fc88d1c41ab03f13558a7a3e7de0bf211059d52b` | Task 0(c) — the ordered paths, verbatim |
| B | `e6fa18961a097ab2b2c7afa2affe57aeeed630bf` | Tasks 1 and 2 — the authored ends at the generator, the regenerated measurement, the re-bannered dispatch |
| C | *(the close)* | Task 3 — the `STATUS.md` entries, the forward bound, the regenerated read-size and defense-share artifacts, this report, and the two banner corrections §6 records |

**Why the re-bannered dispatch appears in C as well as in B.** The standing self-check found two
defects in the banner I had written — a false date and a false claim about which sections carry no
blank line — **after** B had landed. They are corrected at the object in C rather than folded back
into B, so the record shows what was written and when it was corrected. The banner's
additions-only property against the body it re-banners is unaffected: both corrections are inside
the banner.

**B is the batch's LAST TASK COMMIT** and is therefore what the forward bound is aimed at, per that
tool's own docstring.

**One observation, declared rather than absorbed.** `git add` emitted this repository's standing
line-ending normalization warning for the text paths. That is the repository's own configuration, it
applies to every commit made in it, and it is not an act of this batch. **Nothing was edited,
reformatted, re-wrapped or normalised by me** in any of the Task 0(c) paths.

---

## 1. The two declared-unestablished premises, answered

**Premise 7 — whether any tracked modification exists at the tree. ANSWERED: NONE, and the
dispatch's expectation held exactly.** The sanctioned enumeration was run over the whole tracked
population and its artifact is `tools/audit/changed_paths_defense_authored_ends_task0.json`. Every
record it carries is untracked; **no tracked modification, no deletion and no rename**. This is the
shape the hundred-and-fiftieth handoff entry predicted for a base whose newest entry was written
once and never amended, and it is the first start state of this arc that needed no qualification.
No earlier result was carried: the enumeration was re-run at the tree.

**Premise 8 — whether the guard set still stands where the record says. ANSWERED: IT DOES, and the
failing set matches member for member.** The set was run with `--check` and **not** bare, for the
standing reason the dispatch gives: a bare run rewrites the committed `tools/audit/guard_state.json`
and would fold this tree's state into a committed record before this batch's own commit. The run's
population, its passing, failing, not-run and historical counts, and its failing set all match what
the committed artifact records — the failing members compared one by one against that artifact's own
`failing_tools` list rather than against a memory of it, and they agree in membership and in order.

**★ AND ONE THING THAT RUN REPORTS IS REPORTED HERE AND NOT CORRECTED, BECAUSE IT IS PRESENT AT BOTH
TREES ALIKE.** `gen_guard_state.py --check` prints `STALE vs the run: guard_state.json does not
re-derive` and exits non-zero on that account — **at the start state exactly as at the close**. Its
counts and verdicts are unaffected, which is why premise 8 still holds. **No cause was hunted**, the
dispatch barring one, and **nothing was regenerated to make it green**: regenerating is the bare
invocation the dispatch forbids for this batch. It is recorded as a start-state condition this batch
neither created nor changed. What this batch did **not** establish, and does not claim: whether the
condition predates the batch entirely. Task 0(a) writes its artifact before Task 0(b) runs, in the
order the dispatch fixes, so the guard set was never run at a tree without that file.

**★ AND PREMISE 5 WAS VERIFIED AT THE OBJECT RATHER THAN RELAYED.** The dispatch declares it
ESTABLISHED and orders it reported. `tools/audit/gen_guard_classification.py --check` was run: it
STOPs, naming `tools/audit/gen_l0_l1_outgoing_population.py` and
`tools/audit/gen_withheld_family_reading.py` as guard-state members with no authored verdict, and it
writes nothing before stopping. **Neither is this batch's, no verdict was authored for either, and
the STOP already stood with the user before this batch began.** Reported, not corrected.

---

## 2. Task 0 — the start state and the tracking commit

The enumeration ran first and is the artifact named above. The guard set then ran with `--check`.
The ordered commit then took the paths the dispatch names, verbatim, all present at the tree — named
rather than counted: this dispatch; the enumeration artifact; `cowork_handoff_entry_one_hundred_and_
fifty.md`; `cowork_rulings_2026_09_08_extent_rule_sitting.md`; and
`cowork_defense_clause_ends_2026_09_08.md`. What the commit touched was read back from its own git
object by explicit hash and is exactly that set.

---

## 3. Task 1 — the authored ends

### 3.1 What changed in the definition

`clauses_in()` is untouched: the same imported emphasis patterns, the same marker table, the same
found clauses. **What changed is only where each found clause ENDS.**

- **The paragraph end stops being the measurement.** It is still computed and still published, as a
  comparison column.
- **`close_at_the_next_clause()` is KEPT**, keeps its ONE implementation of the rule the 2026-09-08
  ruling settled (#6), and now runs over a COPY of the extents so that its result is the second
  comparison column rather than the measurement.
- **The measurement is now: from the first character of the marker through the end of that clause's
  AUTHORED END ANCHOR**, the anchors being the pass published in
  `cowork_defense_clause_ends_2026_09_08.md`.

### 3.2 How an anchor is compiled, and that it mattered

Each anchor is split on whitespace, each word escaped, the words joined with a whitespace pattern.
**Both reasons the dispatch gives were live at this tree**: anchors wrap across a line break, so a
plain single-line search for them finds nothing, and anchors carry characters a regular expression
treats as special. The technique is the one `KNOWN_MISS` already uses, reused rather than reinvented.

**`KNOWN_MISS` itself was deliberately left alone.** It could have been expressed through the new
compiler, and that was considered and declined: it is a fixed literal locator with its own recorded
reason, the dispatch frames the new helper as a reuse of the technique rather than a unification of
the two patterns, and rewriting an established locator buys no measurement and risks its STOP.

### 3.3 Every anchor STOP is in force, and every one passed

The anchor count against the marked-clause count; each anchor locatable exactly once inside its own
clause's span; located in the span the authored table names; beginning at or after its own marker;
ending at or before its own paragraph end; ending strictly before the next marker; and standing in
strictly increasing file order. **Every STOP the tool already carried stays in force** — the
six-span check, the dead-row check, the clause-inside-its-span check, the no-overlap check, the
per-span-not-exceeded check, the total-equals-the-reader's check, the known-miss check and
`--check`. All are published as taken positively on the artifact.

### 3.4 ★ The authored pass was cross-checked rather than trusted

The pass names, for each marker, the line its defense ends on. The tool located each anchor at the
file independently, by pattern, knowing nothing of those lines. **The line the tool resolved to
equals the line the pass names, for every marked clause without exception.** Two derivations made by
different means agree completely, which is evidence about the anchors that neither could give alone.
It establishes that the anchors are located where the pass says; **it does not establish that any
anchor is the RIGHT place for a defense to stop** — that judgment is the pass's, is declared AUTHORED
on the artifact, and is challengeable at its own marker.

### 3.5 What is published per clause, and what the movement is

Every clause carries three lengths — the authored measurement, the length it would have had under
the ruled closing reading, and the length it would have had running to its paragraph end — plus the
anchor as written and the line that anchor ends on. The per-span and total columns carry the same
three. **Every value is at `tools/audit/defense_share.json` and none is transcribed here (D-431).**

**★ THE MOVEMENT, STATED AS A MOVEMENT.** The measured quantity moved **DOWNWARD**, and it moved
downward in every span that carries a clause at all. **This is not a correction of a number.** The
previous value was the size of something else — extents that ran from a marker to the next marker
through text that is live rule — so there is no arithmetic relation between the two to correct.
What changed is what is being measured. The direction was predicted by the dispatch and by the pass
before either ran, and the run's own comparison columns are where the size of the movement is read.

**Nothing published was lost (#12), and that is provable rather than asserted:** both comparison
columns re-derive the values published before this act, per clause, per span and in total. A reader
comparing the outgoing artifact with this one finds the old totals present, under names saying which
reading produced them.

### 3.6 The bound wording, and the stale departure block

The artifact declared its value a LOWER BOUND on defense material. **That was false of the value it
then published**, which counted text that is not defense while still missing every unmarked defense
— wrong in both directions at once, so not a bound in either. The block now states: that the value
**is** a lower bound on MARKED defense, the marker set's reach being unmeasured; that it was **not**
a bound in either direction before this act, with **the former wording preserved verbatim** rather
than quietly replaced (#12); that the ends are AUTHORED, published in the pass, and challengeable at
their anchor; and that `cowork_claude_md_live_rule_classification_2026_09_08.md` is **STILL not
consumed** — it is read nowhere in this tool.

The docstring's declared-departure block about the closing rule is **replaced by a pointer to
`cowork_rulings_2026_09_08_extent_rule_sitting.md`**, which ruled it, so the tool no longer says an
outstanding departure is owed when it is not. This also discharges §3(b) of that ruling record — the
stale *owed to the writing side* wording, corrected AT THE GENERATOR and regenerated, never by hand.
**No line number was carried into the docstring** (D-307).

---

## 4. Task 2 — the spent dispatch re-bannered

`cc_instruction_defense_share_sizing_third_2026_09_08.md` has run and is committed, so under D-674
it is **re-bannered and never rewritten**. A banner was added at its head recording that its extent
sentence was defective as written; that the executing batch declared and resolved the conflict; that
the resolution was ruled on 2026-09-08; and that the paragraph unit both readings were built on has
since been replaced. **Not one other character of that file changed** — the edit inserted the banner
between the heading and the body it left intact, which is why additions-only is a property of the
act rather than a claim about it.

---

## 5. Task 3 — the close

**(a)** `STATUS.md` gained this batch's entries, per the OI-222 pointer convention, restating no
value (D-431).

**(b)** The forward bound was performed ONCE, as an ORDINARY move: `tools/audit/gen_status_batch_
bound.py` re-aimed at every one of its authored inputs, the then-previous batch being the
defense-share sizing batch, with **this batch's own entries written FIRST and `--apply` run second**
— the order the declared prefix adjustment makes mechanical rather than preferred. Every previous
aiming is appended to rather than replaced (#12). **No count of entries was written into the
re-aiming comment**, which is the dispatch's own instruction and its reason: the previous re-aiming
asserted a count its own run then contradicted, and a comment stating a count the tool contradicts
is the defect #10 forbids. The move's own artifact is `tools/audit/status_batch_bound.json`, and its
reconciliation came back green in both limbs — every moved entry byte-present in the archive exactly
once and absent from the must-read.

**★ ONE AUTHORED FIELD TURNS ON THE DATE, AND IT WAS SET TO THE DAY THE ACT HAPPENED.** `ACT_DATE`
is 2026-09-09, not the dispatch's 2026-09-08, because the archive header states when the ACT
happened and a header carrying a dispatch's date would say something false about the record (#10) —
the case that field's own comment provides for. **No claim is made that this is the first such
batch**: the older rows record no date of their own, so the question cannot be settled at the tool,
and the report says so rather than reaching for a superlative.

**(c) THE REGENERATION RAN IN THE ORDERED SEQUENCE, AND I STATE THAT IT DID.** First
`tools/audit/session_start_read_size.json`, because (a) and (b) move `STATUS.md`, a member of the
read it measures. **Then `tools/audit/defense_share.json`**, because it re-derives the whole-read
denominator through that same reader and would otherwise go stale the moment `STATUS.md` moved.
**That the order matters was observed and not assumed**: the whole-read denominator on the defense
artifact moved with each `STATUS.md` edit, so a defense-share artifact generated before the read-size
one would have published a denominator the tree no longer had. **No measured value was adjusted to
reach a number**, and the sequence was re-run in full after every later `STATUS.md` correction rather
than patched.

**(d)** The full guard set was re-run with `--check` at the closing tree. **Its whole captured output
is byte-identical to the Task 0(b) run's** — same population, same verdicts, same failing set member
for member and in the same order, and the same start-state staleness line §1 records. **No departure
at all is traced to this batch's ordered acts**, and none had to be explained away.

---

## 6. The standing self-check, and what it found in my own new text

The diff of every touched file was re-read against the guiding principles, the conventions and
`DEFECT_TYPES.md`. **It found defects of mine, and they are named rather than summarised** — every
one corrected before this report was written, and every one found by the check rather than by a run.

- **Three reserved-word breaches in the new tool text.** Bare *register* in the phrase *the two
  register sections*, twice; bare *part* in *is part of what the correction is*, twice; and *rest*
  as a verb in *the unit both of them rest on*. All replaced with the qualified or plain forms the
  disambiguation convention names. **The regenerated artifact was diffed against the pre-correction
  run and every measured value was unchanged**, so the corrections were to wording alone.
- **A register status word used loosely.** The artifact said the ruled closing reading was
  *superseded* as the measurement. *Superseded* is decisions-register vocabulary and this batch
  writes no register entry; it now reads *replaced*.
- **A false date in my own banner.** It read RE-BANNERED 2026-09-08. The act happened on 2026-09-09
  — the very error `ACT_DATE` exists to prevent, written into a banner in the same batch that
  reasoned about it. Corrected to the day the act happened.
- **A false claim in my own banner, and an unqualified predicate beside it.** The banner said
  `CLAUDE.md` carries no blank lines *inside its two longest sections*. That is not true — the two
  unbroken sections at issue are the ones for the open-items register and for the decisions
  register, and neither is the longest session-start span. The same sentence had said *this file*
  where it meant `CLAUDE.md`, in a file that is not `CLAUDE.md`. Both corrected at the object.
- **Two numbers in `STATUS.md` entries that contradicted those entries' own restatement bar.** An
  entry saying *no value is restated here (D-431)* also said *four where five moved* and *the two
  unclassified guard-set members*. Both replaced by the members and the reason.
- **An unestablished superlative, in three places at once.** *For the first time in this arc*, of
  the act date differing from the dispatch date. The older aimings record no date, so the claim
  cannot be settled at the tool. Struck from `STATUS.md`, from the tool comment and from the
  aiming row, and replaced by the statement that no such claim is made.

**Against the defect catalog**, the acts of this batch were checked at the types that could reach
them: DT-11 (no hand-transcribed measurement value — every value is at the artifact and the two
`STATUS.md` numbers above were the near miss); DT-12 (no line number carried into any docstring or
banner; every citation is to a file or a named section); DT-23 (every anchor failure is a STOP, none
is swallowed — no broad exception was added); DT-24 (the tool writes only its own artifact); DT-7 (no
dead row and no never-firing check — every marker row matched and every anchor located, both under
STOPs); and DT-26 (the anchor search is bounded to each clause's own span, and the count check plus
the span-name check plus the file-order check are what stop a clause being silently unanchored).

---

## 7. Readings taken that this dispatch did not order

- **The ordinary session-start read, in full**, on the standing rule that a single-file opening
  instruction is not an exemption from it: `STATUS.md`; `DECISIONS.md` whole; the derived gating
  answer at `tools/audit/nongating_apparatus_rows.json`; `CLAUDE.md` at its ruled membership; and
  `BUILD_AND_TEST.md` under its conditional, this session running measurement tools. **The
  build-and-test read yielded nothing bearing on this batch** — none of the tools run here has a
  command recorded there — and it is named because it was performed, not because it paid.
- **`cowork_defense_clause_ends_2026_09_08.md` whole.** The dispatch supplies the anchors in its own
  table and does not order the pass to be read. It was read whole, and that is what made §3.4's
  cross-check possible and what supplied the two bounds the pass declares on itself, now published
  on the artifact.
- **`cowork_rulings_2026_09_08_extent_rule_sitting.md` whole.** Committed by Task 0(c), not ordered
  to be read. **It carried something this batch needed**: its §3(b) names the stale *owed to the
  writing side* wording as a correction owed at the generator, which Task 1.7 discharges.
- **`cowork_handoff_entry_one_hundred_and_fifty.md` whole.** Committed by Task 0(c), not ordered to
  be read; it is the boot authority for the sitting and it named the start-state shape premise 7
  asks about.
- **`tools/audit/changed_paths.py` whole**, to know what the sanctioned enumeration covers and what
  it does not, rather than treating its output as self-explaining.
- **`tools/audit/gen_status_batch_bound.py` whole**, and with it `ENTRY` in
  `gen_status_archive_pass.py` and `PREFIX_ADJUSTMENT` in `gen_governing_surface_split.py` — which
  is how the write-entries-then-apply order was established at the objects rather than followed on
  the dispatch's word.
- **`tools/audit/gen_guard_state.py` at its `main()`**, to establish what its exit code and its
  drift line actually mean before reporting either.
- **`tools/audit/gen_guard_classification.py` at its `--check` handling, and RUN with `--check`** —
  the verification of premise 5 described in §1. It writes nothing.
- **`DEFECT_TYPES.md` at its type table**, for the standing self-check.
- **`tools/audit/gen_session_start_read_size.py` beyond the symbols the dispatch names**, at
  `rule_a_pointer`, `key_span_characters`, `_resolve_span` and `_bullet_list`.
- **`cc_report_defense_share_sizing_third_2026_09_08.md` at its commit table**, to follow the
  close-row convention the previous batch set rather than invent one.

**Acts taken that the dispatch did not name, declared here rather than absorbed.** The artifact's
`generated_for` field named only the dispatch that created the tool; it now names this dispatch's
repair as well and keeps the creating one, because a field claiming the measurement was generated
for a task that no longer defines it is a statement the file makes falsely about itself (#10). And
the line-holding index computation that `close_at_the_next_clause` carried inline was extracted into
a named helper so the authored path and the comparison path share one implementation (#6); the
comparison column re-deriving its previously published values per clause, per span and in total is
what shows the extraction changed nothing.

---

## 8. What this batch did NOT do

No edit to `CLAUDE.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md`, any ruling record, or
`cowork_defense_clause_ends_2026_09_08.md`. No change to the marker table, to the span source, to
the denominators, or to which clauses are found. No satellite file, and **no text moved out of any
governing document** — the ordered act was a measurement-definition repair and nothing else. No
open-items row created, flipped or discarded. No decisions-register entry, no `D-NNN`, no finding
number. No `src/` change, no build, no test, no golden, no corpus, nothing under
`tools/robust_stop/` or `tools/corpus/`. No paper opened, no extract, no sweep, no verdict moved, no
gate lifted. No new guard enrolment — the tool was already enrolled, at both the invocation and the
LIVE verdict, and neither was touched. No verdict authored for the two unclassified guard-set
members. And no hunt for anything the guard set reports.

**★ THAT THE EXISTING VERDICT STILL RESOLVES WAS CHECKED, NOT ASSUMED.** The LIVE verdict for this
tool cites its evidence by name — two named sections of the module docstring and two named functions
— and an amendment that renamed any of the four would have left the classification pointing at
nothing while still reading LIVE. **All four survive the amendment unchanged**, which is why the
enrolment needed no touch rather than merely appearing to need none.

**It also settles nothing about MOVABILITY.** Whether any measured character may live in a satellite
is Ruling 1's question, and neither the repaired measurement nor this report answers any portion of
it.

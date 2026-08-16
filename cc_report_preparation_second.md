# CC report — the preparation phase's second batch

> **What this is.** The coding side's report on `cc_instruction_preparation_second.md`, performed
> 2026-08-16. The batch record beside it is THE PREPARATION SECOND BATCH section of
> `cowork_away_returns.md`; this file is the whole of what the coding side says back.
>
> **THE HEADLINE, BEFORE ANY DETAIL.** All four tasks are performed. The sitting's ruling record and
> the dispatch are landed; the caller-check is RE-RUN under the ruled reading and **now
> discriminates**; the deciding-act recovery pass covers the whole non-keep population and
> **recovers a user act for a substantial minority of it**; and the rulings sort is PROPOSED over
> the ratified confirmed side with its seed list visible in full. **Nothing was archived, moved,
> deleted or discarded, and no decisions-register file was touched.**
>
> **THREE THINGS THE USER SHOULD READ BEFORE ANYTHING ELSE.** *(1)* **Eight callers come back
> KIND-UNDERIVABLE and return to the user** — that is the ruling's own STOP firing, at the one place
> where this derivation could have been dishonest and was not (§3.c). *(2)* **The soft-discard
> ruling can now be put over evidence rather than over a provenance field** — the recovery pass
> found, for a substantial minority of the non-keep entries, a user act in a document the entry
> itself cites (§4). *(3)* **Three false-positive shapes were measured in this batch's own first
> runs and corrected at the tool** — a derivation over the record's own machinery is more fragile
> than it looks, and the three shapes are named so the next one meets them knowingly (§3.b).
>
> *(Every guard count lives at `tools/audit/guard_state.json`; every caller-check value at
> `tools/audit/retirement_caller_check.json`; every recovery result at
> `tools/audit/deciding_act_recovery.json`; every sort proposal at
> `tools/audit/rulings_sort_classification.json`. None is restated here beyond the few this report
> is reporting ABOUT, each naming where it was read — **D-431**.)*

---

## 1. Both guard-set states

- **START, before the first act:** `gen_guard_state.py --check` printed **"the guard state
  re-derives"** — **50 guards run, 49 passing, ONE failing**
  (`gen_filing_convention_application.py --check`, which is [[OI-372]]), 4 not run, 10 historical
  records, **no STOP**. `gen_guard_classification.py --check` printed **"the guard classification
  re-derives"**. **This is exactly the start state the dispatch declares as expected**, so no
  STOP-and-report was owed on it. The sanctioned enumeration reported **no tracked modification
  anywhere in the working tree**, with both of the dispatch's own two files untracked — assumption
  **A1** exactly as stated.
- **END, after both new tools were added and registered:** **52 run, 51 passing, ONE failing**
  ([[OI-372]]'s tool), 4 not run, 10 historical, **no STOP**;
  `gen_guard_classification.py --check` — **"the guard classification re-derives"**. The two checks
  this batch adds are inside the classified population under authored verdicts, and both PASS.
- **E5's run, taken at the tree carrying the close and after the commit that carries it**, is
  recorded at §7 — **run and read, never inferred, and its values committed only after the run.**

---

## 2. Task 0 — the sitting's ruling record and this dispatch enter git

**Commit `6529d10ae4`, parent `c2213b52fb`, pushed.**

**A1's check came first**, through the sanctioned enumeration `tools/audit/changed_paths.py`. It
reported **no tracked modification anywhere** — every record it returned was untracked — and
`cowork_rulings_2026_08_16_preparation_return.md` and `cc_instruction_preparation_second.md` were
among the untracked. **The premise held exactly as stated and the ordered STOP was not reached.**

Exactly the two paths the dispatch names and no third, verified at the index through the same tool
before the commit (2 records, both `A`) and at the object after it. **Both were staged PLAINLY** —
both ignore rules over this family are gone, so no override was used and none was needed.

**Registered expectation E0 — MET on all three limbs:** exactly 2 paths at `git diff-tree`; both
additions; no staging override of any kind.

*One detail about the premise rather than about the act, declared rather than glossed:* the
dispatch's FACT names `5c384d8966` as the commit the previous batch is complete and pushed through,
and the current commit was one further on — `c2213b52fb`, whose subject is a correction to that same
batch's report. Nothing turned on it, because A1's check is about the working tree and the working
tree was clean. It is recorded as **F12** because a premise about where the record ends was slightly
behind the record.

---

## 3. Task 1 — the caller-check re-run under the ruled reading. Commit `7e400491f9`, pushed, four paths

### 3.a What the ruled reading changed, and what is derived in it

The user's ruling (`cowork_rulings_2026_08_16_preparation_return.md`, the caller-check ruling) is
that **a naming from a tree-enumerating record does not hold a candidate**, under a **derived**
caller-kind classification — *"never a naming-breadth threshold … and never a hand-typed exemption
list"*. Every sentence of that ruling is LOCATED in its record on every run, exactly as the ruled
candidacy conditions already were: a reading may not outlive the words that imposed it.

**The kind is derived in two links, each published per caller with its evidence.**

- **Link 1 — caller to generator**, by two routes, and which one fired is recorded per caller.
  *Route A:* the caller's own text DECLARES its generator. *Route B:* a tracked Python source's
  **write site** resolves to the caller's repository-relative path — found in the syntax tree and
  resolved through the name chain (`OUT`, `HERE`, `ROOT`, `os.path.join`, `Path(...) / "…"`),
  **never matched by base name**, because a base-name match confuses a reader of a file with its
  writer.
- **Link 2 — generator to enumerating.** A tracked-tree enumeration among the generator's own
  **string constants**, or the caller's own declaration that it is **rendered from** an artifact
  that is one — the ruling's *or a surface rendered from one* limb, taken from the surface's own
  words rather than inferred.

**DERIVED:** the caller population; both links and every piece of evidence for them; every kind,
tally and holder kind. **AUTHORED and published in full:** which git subcommands count as
enumerating the tracked tree, which spellings declare a generator, and which extensions make a
holder a tool.

**It is neither shape the ruling forbids.** No count of how many files a caller names enters the
rule anywhere, and **no caller is named in the tool** — a record becomes an enumerator only by
carrying a resolvable producer whose source enumerates.

### 3.b ★ THREE FALSE-POSITIVE SHAPES, MEASURED IN THIS TOOL'S OWN FIRST RUNS AND CORRECTED AT THE TOOL

None of these was reasoned about in advance. Each appeared in a run, was read at the artifact, and
was fixed at the tool rather than worked around. They are recorded because the next derivation over
this machinery will meet the same three.

1. **A generator declaring ITSELF.** A generator's source carries the very field literal it writes
   into its artifact — `"generated_by": "tools/audit/gen_x.py"` sits inside `gen_x.py` — so three
   measurement tools were read as generated artifacts and classified as tree enumerations. **A
   self-reference is not a declaration**, and is now excluded.
2. **A sentence about somebody else.** A coding-side report says, in prose, that a DIFFERENT file is
   generated by a tool; that sentence was read as a declaration about itself. **A declaration now
   has to open its line**; a mention does not.
3. **A signal sought in text rather than in code.** The enumeration test matched the source's TEXT,
   so a corpus-registry builder whose notes field says an inventory was *"taken from git objects
   (ls-tree)"* and the shell-read guard, whose forbidden-utility list contains the word `grep`, both
   came back enumerating. Neither calls git to enumerate anything. **The signal is now sought among
   the source's string CONSTANTS**, with `grep` counting only where the source hands it to git.

### 3.c ★ THE RULED STOP IS WHERE THIS PASS IS HONEST, AND EIGHT CALLERS RETURN TO THE USER

A generator that merely **imports** an enumerating module, or **reads** an artifact one produced,
may be passing the enumeration through into its own output or may be consuming it for something
else — and **nothing in the source separates those two**. The first version of this derivation
treated the weaker relation as the stronger one, and the visible consequence was that the decisions
register's own AUTHORED data file was classified as a tree enumeration, because three tools that
edit fields inside it read an enumeration somewhere.

So the weaker relation **establishes nothing**: the caller becomes **KIND-UNDERIVABLE**, its naming
**HOLDS**, and it **returns to the user** — which is exactly what the ruling requires of a kind that
cannot be derived. **Eight callers are in that list**, each with the precise relation that could not
be resolved, and ruling on them is what would let the check discriminate further.

### 3.d The measured result: the check now discriminates

**One candidacy comes back PASSES-THE-CHECK.** The rest are still held, and every surviving holder
is published **BY KIND** — a tool reading the file by name, a mandatory-read or boot listing, a
prose citation — **with the line its naming was found on**, centred on the naming rather than cut
from the start of the line. A **fourth bucket** is published rather than forced into the three: a
DATA record that is none of them. Forcing it into *a tool reading the file by name* would inflate
exactly the kind a reader is most likely to take for a real dependency.

**The deferred question — whether a prose citation holds — is NOT decided here.** The ruling defers
it to this evidence, and this artifact supplies the evidence and takes no position.

**Namings from fellow flagged files are set aside into their own field**, like same-class namings,
and every one stays published (#12).

### 3.e Two evidence-quality facts now measured rather than left as caveats

- **Whether each flagged member's base name is unique in the tracked tree.** The reference test is a
  base-name match by design, so a member whose base name several tracked paths share is named by
  every mention of any of them — a `README.md` inside a flagged directory is held by every sentence
  in the record that says README.md. Each member now carries the answer, and the members held on a
  shared base name are listed.
- **Which tracked Python sources would not parse.** A caller one of them writes keeps holding, so
  the list is published rather than the cost being assumed to be zero.

**Registered expectation E1 — MET on every limb.** Every candidacy re-verdicted under the ruled
reading over the same derived population; every set-aside naming still present in its own field;
every surviving holder carrying a kind with quoted evidence, or sitting on the KIND-UNDERIVABLE
list; `--check` re-derives; and no path outside the tool, its artifact and the guard-mechanism
records in the commit.

### 3.f ★ ONE PLACE WHERE THE DISPATCH CANNOT BE OBEYED LITERALLY, DECLARED RATHER THAN RESOLVED

Task 1 step 3 says the KIND-UNDERIVABLE list is published *"on the artifact and the surface"*.
**There is no caller-check surface in the record**, and E1 bounds this task's commit to the tool, its
artifact and the guard-mechanism records — so creating one would have broken the expectation the
same dispatch registers. The list is published **on the artifact**, and returns to the user through
this report and the close. Stated as **F11**; a session does not resolve a conflict between two
clauses of its own dispatch.

---

## 4. Task 2 — the deciding-act recovery pass. Commit `ddbf89d002`, pushed, seven paths

### 4.a What it is, and what it is not

**The filter read the decisions register. This reads the record that register points at.** A
decision whose entry records no ratifier may still have been ruled in a document the entry cites,
and until somebody follows the citation nobody knows which.

The population is **IMPORTED** from the committed filter artifact and never restated (#6), and
reconciled against the decisions register's data file **in both directions as a STOP**. For every
member the pass follows the entry's own cited sources — the documents its `home`, `status_source`,
`rationale` and `verbatim` name, plus the dated ruling records where it records a date — and
searches them for a passage carrying a **user-act marker** AND matching that entry's **own subject
recognizers**.

**★ THE SUBJECT TEST IS THE RECORD'S OWN.** The decisions register carries a `patterns` list per
entry — its own recognizers for that entry's subject, authored when the entry was written. Those,
with the entry's identity, are what a passage must match. Nothing here is this side's reading of
what an entry is about.

**An ACT-FOUND is evidence, not a verdict.** A passage can carry both and still be about something
else; the tool quotes it, names where it is, and stops. **No entry is re-classified** — the filter's
proposed class rides beside every result.

### 4.b The result, and the split that makes it readable

**Of the whole non-keep population, a substantial minority carry a recoverable user act**, and the
split **by the filter's own class** is published on the surface, so the two readings can be compared
directly. **The CITATIONS-UNRESOLVED class is empty**: every entry resolved at least one citation, so
assumption **A3** held in the direction it predicted, and no malformed entry was met.

**The soft-discard ruling is therefore now put over evidence rather than over a provenance field**,
which is what the ruling ordered this pass for. The user's own clause is quoted **verbatim in the
surface's banner**, so whoever rules meets it before the members: a soft-discard record is a
PROVENANCE verdict and not a judgment on soundness or usefulness.

### 4.c Two limits stated before the first result, and one of them is a real weakness

- **The citation walk is ONE LEVEL** — the documents the entry names, plus the dated ruling records
  where it records a date. An act recorded somewhere the entry does not cite is outside this pass by
  construction, and that is where the limit sits.
- **★ THE BLOCK RULE IS VACUOUS ON A DOCUMENT WITH NO BLANK LINES.** An act and a subject must be in
  the same blank-line-separated passage, so that a ruling on the first page is not read as evidence
  about a subject on the fortieth — but a JSON artifact or a CSV table is ONE block, and there the
  locality buys nothing. **No size threshold was imposed to patch it**: a hand-picked number over
  varying data is the shape this record has twice declined. Instead **every recovered passage
  publishes how many lines it spans**, and the concentration table publishes the same span beside
  the count of entries each passage carries — so a reader sees at once whether an act is a paragraph
  or a whole file. Recorded as **F9**.
- **The concentration is measured rather than left to be noticed.** One large user-ratified passage
  can match many entries' recognizers at once, and an ACT-FOUND resting only on such a passage is
  weaker evidence than one resting on a passage written about that entry. The passages are ranked by
  how many entries' evidence they carry, and the entries whose whole evidence is one passage are
  counted.

### 4.d The decisions register is byte-unchanged, proven by hashing

`DECISIONS.md`, `tools/audit/decisions/backbone_decisions.json` and **every** rendered
`decisions/group_*.md` file were each hashed against their committed blobs after the run. **Every
one is byte-identical.** No entry was retired, edited, moved or marked, and no soft-discard was
executed.

**Registered expectation E2 — MET on every limb.** The artifact covers the whole non-keep
population, each entry in exactly one of the three result classes with its evidence; the register's
rendered and data files are byte-identical to their committed blobs; `--check` re-derives.

---

## 5. Task 3 — the rulings sort, proposed. Commit `2fa6ffcbf9`, pushed, seven paths

### 5.a The rule leans first on the record's own judgment, and only then on words

Two fields the decisions register already carries decide most of the population without this tool
reading anything into an entry:

- **`home_is_layer_spec`** — the entry is recorded in a layer's own specification, which is where a
  decision about what the analysis is or does lives. That is design intent.
- **`nonspec_kind`** — read by the definitions the data file's **own header** gives those values,
  quoted rather than interpreted: `process` is *"a decision about how the work is done, not about
  the system"*, which IS the management class; `gap` is *"a decision that governs a layer and is not
  findable from that layer's section"*, which is design intent recorded in the wrong place.

Only what those leave undecided reaches the authored word recognizers, and what THOSE leave
undecided is proposed **NEEDS-THE-USER** — never guessed. **The distribution by the route that
decided it is published**, so a reader can see how much of the sort is the record's own recorded
judgment and how much is this side's authored words. It is the majority on the record's side.

### 5.b Why the design-intent side is listed in full

It becomes the framework phase's **seed list** — the decisions a derivation would be allowed to
start from. A decision wrongly placed there seeds the architecture with something nobody meant to
seed it with; one wrongly placed on the other side is simply not consulted. **That asymmetry is why
every design-intent member, and every NEEDS-THE-USER member, is listed with what the decisions
register itself says the decision is.** The management side is listed by identity, with the surface
saying in terms that this is not a judgment on their worth.

### 5.c ★ A SECOND RECORD-LEVEL DISAGREEMENT, RECORDED AND NOT REPAIRED

The data file's header says `nonspec_kind` says which of **three** cases an entry is, and names
three. **The entries use more than three.** The values the header does not define are **not mapped
by their name** — they fall through to the recognizers, which is the only honest treatment of a
value the record does not define. Nothing was repaired: this batch edits no decisions-register file,
and a disagreement between a record and what it describes is evidence. It is the sibling of **F7**,
the status-spelling disagreement the filter pass recorded, and it is **F10**.

**The decisions register is byte-unchanged, proven by hashing a second time** — the INDEX, the data
file and every rendered group file against their committed blobs.

**Registered expectation E3 — MET.** The artifact classifies exactly the confirmed side, each entry
in one proposed class with its evidence; the scope block names its population as the ratified keep
side of the filter artifact by citation; `--check` re-derives.

---

## 6. The new-tool rule, discharged twice

Each check this batch adds joined the derived guard-candidate population the moment it existed, and
**each landed WITH its authored run-instruction and its authored classification verdict in the SAME
commit that adds it**. Both take `--check` and not the bare invocation, for a reason about the
tools: run with no flag each REWRITES its committed outputs, which is the OI-301 hazard.

*One ordering consequence is declared rather than glossed.* Task 3's tool existed on disk while Task
2's guard state was being taken. It was **moved out of the repository** for the duration and restored
for its own task, so the state committed with Task 2 is the state of Task 2's own tree — the same
practice the previous batch recorded, for the same reason.

*And one wasted run is declared too, because it is the honest account of the work.* Task 2's first
guard regeneration was discarded: the tool's prose was corrected after the artifact had been
written, so its own `--check` went red in that run. The correction was a reserved-word one — bare
*register* where the convention requires *the decisions register* in full — found by the standing
self-check on this batch's own new prose.

---

## 7. Every registered expectation, graded

- **E0 — MET.** Exactly 2 paths at `git diff-tree` on `6529d10ae4`, both additions; no staging
  override of any kind.
- **E1 — MET.** Every candidacy re-verdicted under the ruled reading; every set-aside naming in its
  own field; every surviving holder with a kind and quoted evidence, or on the KIND-UNDERIVABLE
  list; `--check` re-derives; no path outside the tool, its artifact and the guard-mechanism
  records.
- **E2 — MET.** The whole non-keep population covered, each entry in exactly one of the three result
  classes with its evidence; the decisions register's rendered and data files byte-identical to
  their committed blobs, proven by hashing; `--check` re-derives.
- **E3 — MET.** Exactly the confirmed side classified, each entry in one proposed class with
  evidence; the scope block naming its population by citation to the filter artifact; `--check`
  re-derives.
- **E4 — MET.** The end guard state shows every check passing except
  `gen_filing_convention_application.py --check` ([[OI-372]]), zero STOPs, with both of this batch's
  new checks inside the classified population under authored verdicts, and the runner and
  `gen_guard_classification.py` both printing their re-derives lines. **No other failing check
  appeared at the end of any task**, so no STOP-and-report was owed.
- **E5 — see below, and the ordering rule the dispatch imposes was obeyed.**

**★ E5 — MET, RUN AT THE TREE CARRYING THE CLOSE AND AFTER THE COMMIT THAT CARRIES IT.** Task 4's
close is commit **`4926284de7`**, pushed, parent `2fa6ffcbf9`, three paths. At that tree, after that
commit existed, `gen_guard_state.py --check` printed **"the guard state re-derives"** — **52 guards
run, 51 passing, ONE failing** (`gen_filing_convention_application.py --check`, [[OI-372]]), 4 not
run, 10 historical, **no STOP** — and `gen_guard_classification.py --check` printed **"the guard
classification re-derives"**. The sanctioned enumeration at the same tree reported **no tracked
modification anywhere**: every record it returned was untracked. **Run and read, never inferred.**

Per the dispatch's ordering rule — *no graded value is committed before the run that produced it* —
this paragraph and the SHA in it land in **one further commit** after the close, so nothing here was
on disk before the run that produced it. **The E3-ordering defect that rule exists against is not
repeated in this batch: no expectation anywhere in this report was written before its
measurement.**

---

## 8. Surfaced findings (D-641, #13, #19) — surfaced, not rowed

The dispatch bars creating an open-items row, so each is stated here and in the close.

- **F8 (new) — a derivation over the record's own machinery is fragile in three separate ways**, and
  all three were measured in this batch's own first runs rather than reasoned about: a generator
  declaring itself, a report's prose about a different file, and a signal sought in text rather than
  among a source's string constants. §3.b.
- **F9 (new) — the recovery pass's locality rule is vacuous on a document with no blank lines.** No
  threshold was imposed; every passage publishes its span instead. §4.c.
- **F10 (new) — the decisions register's data file uses `nonspec_kind` values its own header does not
  define.** Not repaired; the undefined values are not mapped by name. §5.c.
- **F11 (new) — Task 1 step 3 and expectation E1 cannot both be satisfied literally.** The
  KIND-UNDERIVABLE list is published on the artifact and returned through this report. §3.f.
- **F12 (new, small) — the dispatch's FACT names a commit one behind the record's actual head.**
  Nothing turned on it. §2.
- **F5 (carried) — the caller-check's signal swamped by tree-enumerating artifacts.** This is the
  finding the user's ruling ANSWERS, and this batch is that answer applied. Carried to the
  retrospective as a closed loop rather than an open defect.
- **F6, F7 (carried, unchanged).**
- **F4 (carried)** — the anchor-remap practice reaches artifacts that turn red only in a SECOND guard
  run.
- **F3 (carried, unchanged, now four times surfaced)** — `reaim_home_anchors.py --check` exits 0
  while printing drifted anchors; the drift authority is `gen_cluster_dispositions.py --verify`.
  **Still unfixed and unrowed — the dispatch bars both.**
- **F1 and F2 (carried).**
- **The E3 ordering defect and the A1 premise error of the earlier batches** are carried to the
  phase's retrospective as the dispatch orders.
- **No finding bearing on the analysis, its inputs, or a measurement tool the analysis depends on.**
  Every subject of this batch is the project's own record and the apparatus that reads it.

---

## 9. What this batch did NOT do

**Nothing was discarded and nothing was archived.** No soft-discard executed, no decisions-register
entry written, edited or retired, **no register file touched — proven by hashing on two separate
occasions**. No file moved, renamed, retired, archived or deleted; every retirement flag stays a
candidacy, the re-derived PASSES verdict confers nothing, and the ruled conditions (mined-first;
members-seen-by-the-user-first) stand untouched. The newly visible instruction files and the
remaining ignored files stay unlanded. No mining, no empirical findings ledger, no fact-gate
admission, no curated boot list. No derivation of any specification, no design, no repair, no pilot
act. **No `src/` change, no golden, no test changed, moved or run, nothing under `tools/corpus/` or
`tools/robust_stop/`, no measurement of the analysis.** **No open-items row created, flipped or
discarded** — [[OI-372]] and [[OI-374]] stay exactly as found, [[OI-179]] stays OPEN and GATES, and
`reaim_home_anchors.py`'s F3 defect stays surfaced, unfixed and unrowed.

*Provenance: CC, 2026-08-16, dispatch `cc_instruction_preparation_second.md`. Task 0 is commit
`6529d10ae4` (parent `c2213b52fb`), pushed. Task 1 is `7e400491f9` (parent `6529d10ae4`), pushed.
Task 2 is `ddbf89d002` (parent `7e400491f9`), pushed. Task 3 is `2fa6ffcbf9` (parent `ddbf89d002`),
pushed. Task 4's close is **`4926284de7`** (parent `2fa6ffcbf9`), pushed, three paths; **E5's run
and that SHA are recorded in the one further commit after it** — the ordering the dispatch imposes, so that no graded
value is committed before the run that produced it. As the previous batch's report recorded of
itself, the recursion stops at the commit carrying that sentence: a commit cannot contain its own
identity, and that terminus is named rather than left as a gap.*

# CC REPORT — the register-reconciliation and harvest-completion batch

> **STATUS: BATCH RUN TO ITS END. TWO COMMITS LANDED. TASKS 2 AND 3 STOPPED ON THEIR OWN RULED STOP
> CONDITIONS AND ARE REPORTED, NOT RESOLVED.**
>
> CC, 2026-08-26, executing `cc_instruction_register_reconciliation.md`.
>
> **NOTHING WAS WRITTEN TO THE DECISIONS REGISTER.** No entry of `decisions/group_S.md` was amended,
> no identifier was allocated, no rendered register file was hand-edited, and no row was renumbered.
> The two ordered register acts each hit a STOP condition the dispatch itself states, and this report
> is the account of why, measured at the generator, at the establishment check and at the guard set
> rather than argued.
>
> **The harvest's two unreached sources are BOTH mined** and the candidate surface is extended,
> uncompared and unadmitted. **The guard set closes at the standing decision red alone.**

---

## 0. THE HEADLINE, IN SIX SENTENCES

1. **Task 2 STOPPED.** The ruled amendment texts cannot be applied to `decisions/group_S.md`:
   that file is GENERATED, its `verbatim` field is establishment-checked against `CLAUDE.md`, the
   entry shape has **no field that carries an added clause**, and `CLAUDE.md` is the file the
   dispatch forbids editing — while the ruling record itself says the landing act is an edit to
   *"their home file"*, and that home is `CLAUDE.md`.
2. **Task 3 STOPPED.** The sharpened decision-surface rule's restatements **differ from one
   another** — three distinct wordings are on the record — and the dispatch says in terms that which
   one is authoritative is the user's.
3. **Assumption A2 HOLDS and is reported anyway**, because it is useful: the register's identifiers
   are dense from D-001 to D-677, so the allocation convention determines **D-678** uniquely.
4. **Task 4 landed, with one declared departure**: Ruling 4's forward bound was performed WITHOUT its
   ruled measurement tool, because that tool's per-batch re-aiming is a tool-source edit E5 and the
   dispatch's own header bar forbid. **This is a conflict between the dispatch's bars and a standing
   user ruling, and it is reported as one.**
5. **Tasks 5–7 delivered**: `DEFECT_TYPES.md` mined WHOLE, the coding side's measurement reports
   enumerated at **265 files** with the coverage boundary named, **21 new candidates** proposed and
   **none admitted** — and the dispatch's own predicted "high pass rate" for `DEFECT_TYPES.md` is
   **FALSIFIED**, for a reason that is itself the finding.
6. **The guard set closes at [[OI-372]] alone** — 75 run, 74 passing, 1 failing — reached in two
   rounds, with everything that moved reported.

---

## 1. DECLARED START STATE (§2), MEASURED — nothing asserted

### 1.1 The refs

| Item | Measured value | Command / route |
|---|---|---|
| `.git/HEAD` | `ref: refs/heads/master` | Read tool |
| Tip (`.git/refs/heads/master`) | `0f18b358bc6a8da5ec6064760d675129e64d8f3b` — **equals §2**; proceeded | Read tool |
| `.git/refs/remotes/origin/master` | `f225b61343ff3de022d32d6b7514d835b87093cf` — **equals §2**; not the tip; **not a STOP** | Read tool |

**No ancestry claim is made or repeated here.** The previous batch established that
`origin/master` is an ancestor of the tip; this batch did not re-establish it and does not restate
it as its own measurement.

### 1.2 The tracked and untracked populations

`python tools/audit/changed_paths.py` → **844 changed path record(s) [worktree]**.

**Tracked, modified — FOUR, exactly the four §2 names:**

```
 M  cowork_handoff.md
 M  open_items/OI-374.md
 M  open_items/OI-376.md
 M  tools/audit/guard_state.json
```

**Untracked root-level, the nine §2 names — ALL NINE PRESENT.** Located in the same enumeration at
its lines 206, 271, 408, 452, 453, 454, 455, 456, 457. **840 untracked records in total**, so the
standing untracked population stands as §2 describes it. **Nothing differs from §2.**

### 1.3 Sizes and hashes — THE SIDE, STATED FIRST

**Side declared: the GIT BLOB — the object git would store for the path, after the `.gitattributes`
`text: auto` conversion.** This is **not** the same digest the previous batch published: that report
gave a **sha256 of the worktree bytes**, and this one gives the **SHA-1 blob identity** git itself
uses. The two are different functions of (possibly) the same bytes and **must not be compared**.
Route: `git hash-object -w -- <path>` followed by `git cat-file -s <hash>` — a content-addressed
computation that returns a hash and a length and no file content, which is why it was used in
preference to a shell read.

**The two sides agree on LENGTH here, and that is measured rather than assumed:** the previous
batch's worktree byte counts for the four paths it published — 722512 / 10785 / 8119 / 22535 — match
this batch's blob lengths on the three that did not change (10785, 8119, 22535). `cowork_handoff.md`
is the fourth and has since grown, which is the writing side's newest entry.

| Path | Blob length | Blob (SHA-1) |
|---|---:|---|
| `cowork_handoff.md` | 761322 | `6ba98a06da2419dc06b33e35d88dde657e0e21a1` |
| `cowork_rulings_2026_08_25_next_act_sitting.md` | 10785 | `9605da504806c3b6f48af4ce93f487cc6c8e1937` |
| `cowork_rulings_2026_08_25_second_vector_sitting.md` | 11105 | `06e3f619df0a3ed47a5880998350adeccbfe97ae` |
| `cowork_rulings_2026_08_25_regress_termination_sitting.md` | 21304 | `3474d415a23476f1c2762df6bc7e376f4ffaf816` |
| `cowork_rulings_2026_08_25_v1_sufficiency_sitting.md` | 7082 | `38fe75b50c8c169c69cda0b36c198b335aefacc0` |
| `cowork_blind_session_opening_instruction_harmony_boundary.md` | 8119 | `717c7a2eaf8507f64d847abca5848bd633bcb427` |
| `cc_instruction_ledger_harvest.md` | 22535 | `31ac8f6ba1a26e184eb72a890580ce6f8e2789cf` |
| `cc_report_ledger_harvest.md` | 48672 | `e12927223defba0c299ccbde1333edb88c99a80d` |
| `cowork_empirical_findings_candidates.md` | 46592 | `ddbcc5305e8cefacfd8f69ed7ed108e8319a4f68` |
| `cc_instruction_register_reconciliation.md` | 20894 | `0a29ab41a21769c5ea3e2af68e17df1d6c8421bf` |

### 1.4 The guard set at the previous batch's close

`tools/audit/guard_state.json` **as found in the tree** (the stopped batch's uncommitted run):
`{run 75, passing 73, failing 2, not_run 4, historical_records 16}` — matching §2 exactly, with
[[OI-372]] and `gen_evidence_pin_membership.py --check` failing. **This batch did not re-derive that
figure at the tip; it read the artifact the stopped batch left, which is what §2 describes.**

---

## 2. TASK 0 — the writing-side landing

**Commit `0a2675855c5a92fc2e32cd55c05281ba4d2c24e6`.** `changed_paths.py --commit` reports **exactly
six records** and no others:

```
A   cc_instruction_register_reconciliation.md
M   cowork_handoff.md
A   cowork_rulings_2026_08_25_next_act_sitting.md
A   cowork_rulings_2026_08_25_regress_termination_sitting.md
A   cowork_rulings_2026_08_25_second_vector_sitting.md
A   cowork_rulings_2026_08_25_v1_sufficiency_sitting.md
```

**Every landed blob is byte-identical to the §1.3 measurement**, verified at the objects by
`git rev-parse <commit>:<path>` against the pre-commit `git hash-object` values. **E0 is MET** and
the measurement is at §7.

---

## 3. ★ TASK 2 — STOPPED. The ruled amendments cannot be sited in the register, and the record says where they belong

**The ordered act:** apply the three clauses of `cowork_rulings_2026_08_25_regress_termination_sitting.md`
Limbs A and B to **D-182 (#19)**, **D-181 (#18)** and **D-187 (#24)** in `decisions/group_S.md`.

**The dispatch's own STOP conditions, quoted:** *"the record's text does not determine where in an
entry the clause belongs; or applying it would require rewording an existing sentence; or an entry's
text on disk differs from the text the record quotes for it."*

### 3.1 What was checked FIRST, and what came back clean

**The third condition does NOT fire.** The three entries' texts on disk match the ruling record's
quotations. Read at `decisions/group_S.md:272–273` (D-181), `:287–290` (D-182) and `:374–377`
(D-187), and at the ruling record `:46–54`. The only differences are typographic — the register
renders `*positively established*` with emphasis markers the ruling record dropped, and renders one
em dash inside D-181's *Why* field as a hyphen. **No word differs.** So the record and the register
are quoting the same texts, and the STOP is not about a mismatch.

**The word the dispatch validates on was measured before and after:**
`grep -n "inspectable" decisions/group_S.md` returns **zero** matches before this batch and
**zero** after it, because nothing was written.

### 3.2 ★ WHY THE FIRST CONDITION FIRES — four measurements, none of them an opinion

**(1) `decisions/group_S.md` IS A GENERATED FILE AND MAY NOT BE HAND-EDITED.** Its own banner, at
`:3–7`: *"**GENERATED FILE — do not hand-edit.** … the source of record is
`tools/audit/decisions/backbone_decisions.json`; the generator is
`tools/audit/decisions/gen_decisions_register.py`. To change an entry, edit the data and
regenerate."* The governing document says the same as register rule (d).

**(2) A HAND EDIT WOULD TURN A GUARD RED ON THE SPOT.**
`tools/audit/decisions/gen_decisions_register.py --check` is a guard-set member —
`tools/audit/gen_guard_state.py:810–811`, *"the rendered register matches its source data across
every emitted file"* — and it re-renders every file from the source data and reports **STALE** on
any difference (`gen_decisions_register.py:652–658`). A clause typed into the rendered file is a
staleness red whose only lawful repair is regeneration, which would erase it.

**(3) THE ENTRY SHAPE HAS NO FIELD THAT CARRIES AN ADDED CLAUSE.** `render_entry`
(`gen_decisions_register.py:510–566`) emits exactly: the heading, an optional legacy mark, the
**verbatim** quote, **In plain words**, **Why**, **Status**, an optional **Entry ratified**,
**Home**, an optional **Home section**, and **Provenance**. **There is no amendment field, and
adding one is an edit to a tool source that E5 and the dispatch's header bar forbid.**

**(4) THE ONLY FIELD THAT COULD CARRY THE DECISION TEXT IS ESTABLISHMENT-CHECKED AGAINST
`CLAUDE.md`.** `gen_cluster_dispositions.py --verify` — also a guard-set member
(`gen_guard_state.py:812–813`, *"every register entry's verbatim quote and cited line is found at its
home"*) — requires each entry's `verbatim` to be **found in its cited home file** and to **start at
the cited line** (`gen_cluster_dispositions.py:326–366`). D-181, D-182 and D-187 are homed at
`CLAUDE.md:116`, `:118` and `:223`. **So writing the ruled clause into the verbatim requires editing
`CLAUDE.md`, which §6 of the dispatch forbids by name.**

### 3.3 ★ AND THE RULING RECORD ITSELF NAMES THE TARGET — IT IS NOT THE REGISTER

`cowork_rulings_2026_08_25_regress_termination_sitting.md:238–239`, in the section headed *"What
these rulings do NOT do"*:

> No amendment is landed. The three amendment texts above are the ruled wording; **the edits to
> their home file** are a landing act for a dispatch that does not yet exist.

**"Their home file."** The register's own Home field for all three entries reads `CLAUDE.md`. The
dispatch orders the clauses applied to `decisions/group_S.md` and, in the same document, forbids
editing `CLAUDE.md`. **Those two instructions cannot both be obeyed**, and the dispatch's own bar —
*"You may write only the amendments those rulings order"* — decides which way a session must fail:
it must not invent a siting the ruling did not order.

### 3.4 What was NOT done, stated so silence claims nothing

No field of any entry was edited. `backbone_decisions.json` was **read only**. No generator was
edited, no regeneration was run, and no clause was written anywhere — not into a provenance field,
not into a plain restatement, not into `CLAUDE.md`. **The amendment texts remain exactly where the
ruling record put them, and nothing about their standing is changed by this batch.**

### 3.5 The question this leaves for the user, stated as a question and not as a recommendation

Three routes exist and **the dispatch authorises none of them**: amend `CLAUDE.md` at the three
principles and re-anchor the three register entries (the route the ruling record's own words point
at, and the one this dispatch forbids); add an amendment field to the register's entry shape (a tool
source edit); or carry the clauses as new register entries that supersede-in-part the three
(a shape the register already has, but a different act from the one ruled). **Which is right is not
a session's to pick.**

---

## 4. ★ TASK 3 — STOPPED. The restatements differ from one another

**The ordered act:** enter the sharpened decision-surface rule in the register under its own
identifier, after reconciling the restatements. **The dispatch:** *"if they differ from one another,
report the difference and **STOP** — which restatement is authoritative is the user's, not yours."*

### 4.1 THEY DIFFER. Three distinct wordings, quoted whole

**(A) THE ORIGIN — the fifty-first handoff entry, `cowork_handoff.md:1882–1886`:**

> **★ A STANDING SHARPENING, GIVEN BY THE USER THIS CYCLE AND BINDING EVERY FUTURE DECISION
> SURFACE:** every alternative is weighed against the ULTIMATE OBJECTIVE **and** the GUIDING
> PRINCIPLES, explicitly; alternatives must NOT be reactions to the latest news taken apart from
> the larger context and plan; and alternatives must NOT self-generate work. A surface that fails
> this is re-put in the corrected form (this cycle's first method surface was, and was).

**(B) THE COMPRESSED CARRY — identical at three sites, `cowork_handoff.md:1463–1465`, `:1563–1565`
and `:1676–1678`:**

> the fifty-first entry's SHARPENED DECISION-SURFACE RULE (every alternative weighed against the
> ultimate objective AND the guiding principles; never a reaction to the latest news apart from the
> plan; never self-generated work)

**(C) THE SIXTY-THIRD ENTRY'S §6, `cowork_handoff.md:595–600` — the one the dispatch names, and the
one that calls itself verbatim:**

> **★ THE DECISION-SURFACE RULE, RESTATED VERBATIM BECAUSE IT WAS THE THING THAT FAILED.** *All
> useful alternatives, with pros and cons, weighed against the ULTIMATE OBJECTIVE **and** the
> GUIDING PRINCIPLES; and the alternatives must not be (a) acting on the latest "news" regardless
> of the larger context and the larger plan, (b) self-generating work for ourselves.* **Write the
> rating as "toward the objective" and "counting against the objective", never as "against", which
> is ambiguous.** **One decision per turn; the surface first, the question in a later turn; the user
> rules by letter.**

### 4.2 The differences, itemised — they are not typographic

| Clause | (A) the origin | (B) the carry | (C) the sixty-third entry's §6 |
|---|---|---|---|
| the alternatives are weighed on two axes | present | present | present |
| **"All USEFUL alternatives, with pros and cons"** | absent | absent | **present** |
| not a reaction to the latest news | present | present | present |
| not self-generating work | present | present | present |
| **"A surface that fails this is re-put in the corrected form"** | **present** | absent | absent |
| **the rating vocabulary — "toward the objective" / "counting against the objective", never "against"** | absent | absent | **present** |
| **"One decision per turn; the surface first, the question in a later turn; the user rules by letter"** | absent | absent | **present** |

**(C) adds three clauses (A) does not have; (A) has one clause (C) does not; (B) has neither.**
Any of the three is a defensible reading of "the rule", and they bind differently — (C) alone
imposes a vocabulary and a turn structure, and (A) alone imposes the re-put obligation.

**A fourth wording exists and is recorded because it bears on the choice:** this dispatch's own §0
mandates *"towards the objective" / "towards the principles", never against* — which is a **third**
rating vocabulary, differing from (C)'s *"toward the objective" / "counting against the objective"*
in both the preposition and the second axis. **No act is taken on that, and it is not proposed as
the answer.**

### 4.3 ★ A2 HOLDS, AND THE IDENTIFIER IS REPORTED ANYWAY

The dispatch asks for the candidates if the convention fails to determine one. **It does not fail.**
Measured:

- `tools/audit/decisions/backbone_decisions.json` carries **677** entries matching `"id": "D-NNN"`
  (live plus retired).
- Its own retired-entries block records `"the_population_before_this_retirement": 677` at `:14651`,
  and the generator STOPS unless live + retired equals that number exactly
  (`gen_decisions_register.py:626–629`) — so the identifiers are **dense from D-001 to D-677 with no
  gap**, and the arithmetic is enforced on every render rather than assumed.
- The highest identifier the rendered index carries is **D-677** (`DECISIONS.md:834`).
- `grep D-678` over `DECISIONS.md`: **zero**.

**The next free identifier is therefore `D-678`, uniquely.** The repository's stated convention for
the neighbouring register — *the next free identity, MEASURED across both surfaces* — gives the same
answer when applied to both the source data and the rendered index. **Nothing was allocated.**

### 4.4 The group is also undetermined, and that is reported rather than decided

The rule's two registered siblings sit in **different groups**: `D-424` (a surface names the
principle behind every pro and con and rates every option on two axes) is in **group K, documentation
governance** (`DECISIONS.md:625`); `D-249` (the whole surface is delivered as user-visible text
before any choice question) is in **group T, standing process rules** (`DECISIONS.md:768`). **A
third rule of the same family therefore has no determined group**, and picking one would be a
register convention decision this batch may not take.

---

## 5. TASK 4 — the status record, LANDED, with the changed passages in full and one declared departure

### 5.1 What was done

`STATUS.md` at the Task-0 commit was **14 lines, 6240 bytes**, its line 8 being the previous batch's
entry (3634 bytes). The new file is **5441 bytes** and is composed as: lines 1–7 unchanged (405
bytes) + the new entry (2836 bytes) + lines 9–14 unchanged (2200 bytes). **405 + 2836 + 2200 = 5441**,
and **405 + 3634 + 1 + 2200 = 6240** accounts for the source object to the byte, so nothing was lost
or gained in transit.

The superseded entry was **moved verbatim** to `STATUS_ARCHIVE.md`, which grew from **1680607** to
**1685322** bytes — the moved entry (3635 bytes with its newline) plus a 1080-byte declaring header.
**The move reconciles in both directions, measured at the two new blobs:** the entry's opening text
occurs **exactly once** in the archive blob and **zero times** in the status blob.

**Route, declared:** the moved text was taken from `git show <Task-0 commit>:STATUS.md`, a
content-addressed object read, and never retyped. **No character of the moved entry was authored.**

### 5.2 The changed passage of `STATUS.md`, in full

**REMOVED (line 8, moved to the archive):** the previous batch's entry, opening
*"\*Last updated: 2026-08-25 (CC — \*\*★ THE SIZING DERIVATION'S OUTPUT IS LANDED …"* and running to
3634 bytes. It is not reproduced here because it is reproduced, whole and byte-identical, in
`STATUS_ARCHIVE.md`, and reproducing it twice is what the move exists to avoid.

**ADDED (the new line 8), in full:**

> \*Last updated: 2026-08-26 (CC — **★ THE FOUR 2026-08-25 RULING RECORDS AND THE HANDOFF'S NEWEST
> ENTRY ARE LANDED, AND THE METHOD RULING IS NO LONGER SUSPENDED — the v1-sufficiency sitting rules
> the derivation method USABLE FOR V1 on the user's own ground, superseding its VOIDED status; the
> framework and the detail-specification phases are NO LONGER HELD; and E and C are neither the next
> act nor owed, while the EMPIRICAL FINDINGS LEDGER STAYS OWED as a framework-phase input.** ★
> **BOTH ORDERED REGISTER ACTS WERE STOPPED ON THE DISPATCH'S OWN RULED STOP CONDITIONS AND ARE
> REPORTED, NOT RESOLVED — nothing was written to the decisions register, no entry was amended, no
> identifier was allocated and no rendered register file was hand-edited.** ★ **THE LEDGER HARVEST'S
> TWO PREVIOUSLY UNREACHED SOURCES ARE MINED AND THE CANDIDATE SURFACE IS EXTENDED — UNCOMPARED,
> UNADMITTED, AND EXPLICITLY NOT THE LEDGER.** No `src/` change, no golden, **no test changed, moved
> or run**, nothing under `tools/corpus/` or `tools/robust_stop/`, no behaviour change to the
> analysis, no fix to inference, no design; **no measurement of the analysis built, designed, scoped
> or run; NO SESSION BOOTED; no derivation and NO COMPARISON; NO TOOL SOURCE EDITED; the blind
> derivation outputs NOT opened at all and no oracle document opened; no edit to any governing
> document — `CLAUDE.md` above all — to `ARCHITECTURE.md`, to the boot-pack generator, to either
> pack directory or to the manifest; NO open-items row created, flipped or discarded; no register
> row opened, amended or renumbered; NO finding number allocated; and NO ADMISSION TO THE EMPIRICAL
> FINDINGS LEDGER, WHICH THIS BATCH DID NOT BUILD.** Dispatch
> **`cc_instruction_register_reconciliation.md`**, executing the two amendment rulings of
> `cowork_rulings_2026_08_25_regress_termination_sitting.md` and the status half of
> `cowork_rulings_2026_08_25_v1_sufficiency_sitting.md`. Per the OI-222 remedy this entry is a
> **POINTER** — the report is `cc_report_register_reconciliation.md`, the candidate surface is
> `cowork_empirical_findings_candidates.md` under its own DRAFT banner, and no count, no identity and
> no rendered value is restated here (**D-431**). **Carried by the report and deliberately not by
> this entry:** why each register act stopped, established at the generator, at the establishment
> check and at the guard set rather than argued; the enumerated coding-side measurement-report
> population with its coverage boundary named; and the DECLARED DEPARTURE that Ruling 4's forward
> bound below was performed WITHOUT its ruled tool, because that tool's per-batch re-aiming is a
> tool-source edit this dispatch forbids — the move itself was taken from the committed object and is
> byte-faithful, and the tool's own record of aimings therefore carries no entry for it.)\*

### 5.3 The changed passage of `STATUS_ARCHIVE.md`, in full

Appended after the file's existing content, in the shape the forward-bound tool itself uses
(`gen_status_batch_bound.py:141–148, 248`): a header line, a blank line, the moved entry:

> \> **★ RULING 4's FORWARD BOUND, 2026-08-26.** The entry below is the PREVIOUS batch's
> (`cc_instruction_sizing_output_landing.md`), moved verbatim out of `STATUS.md` by
> `cc_instruction_register_reconciliation.md` Task 4 in the same act that wrote this batch's own
> entry — Ruling 4 of `cowork_rulings_2026_08_17_governing_surface_split.md`: *an entry is SUPERSEDED
> the moment a later batch's close exists, and the site keeps only the latest batch's entries.*
> Nothing was edited in transit: the text was taken from the committed object at
> `0a2675855c5a92fc2e32cd55c05281ba4d2c24e6` and is byte-faithful. **DECLARED, because this block
> departs from every block above it:** the move was NOT performed by
> `tools/audit/gen_status_batch_bound.py`. That tool's per-batch re-aiming is an edit to a tool
> source, which the executing dispatch forbids by name, so the tool's own record of aimings carries
> no entry for this move and its `--check` continues to reconcile the batch before this one. The
> conflict is reported at `cc_report_register_reconciliation.md` and is not resolved here.

*(followed by the moved entry, byte-identical.)*

### 5.4 ★ THE CONFLICT, REPORTED AS A FINDING — E5 BLOCKS THE RULED FORWARD BOUND

**The forward bound is a user ruling with a built mechanism.** Ruling 4 of 2026-08-17 says *"every
future batch close, in the same act that writes its own entries, moves the then-previous batch's
entries to the archive"*, and `tools/audit/gen_status_batch_bound.py` is the tool the same ruling
installed to do it. Its own docstring explains why it is a tool: *"The entries are single lines of
several thousand characters each. Retyping one to move it is the transcription the record forbids."*

**That tool is RE-AIMED EVERY BATCH, and the re-aiming is a source edit.** Its own words, at
`:59–62`: *"★ THE FORWARD BOUND IS APPLIED ONCE PER BATCH, AND EXACTLY THREE INPUTS MOVE WITH IT —
the base commit, the then-previous batch and the executing act."* Those three are authored constants
in the `.py` file (`BASE_COMMIT`, `PREVIOUS_BATCH_DISPATCH`, `DISPATCH`), together with an appended
row in its `PREVIOUS_AIMINGS` list, which the file keeps *"rather than replaced (#12)"*.

**E5 forbids modifying any path under `tools/` ending `.py`, and the dispatch's header bar says the
batch "edits no tool source".** So the ruled mechanism was unavailable.

**What was done instead, and its cost, stated plainly:** the move was performed from the committed
object, byte-faithfully, and declared at the archive block itself. **The cost is that
`PREVIOUS_AIMINGS` carries no row for this move** — an information gap in a record the tool keeps
deliberately (#12) — and that the tool's `--check` now reconciles the batch *before* the one just
moved. **The check still PASSES** (§8), because it grades only the batch it is aimed at; it does not
know a later move happened.

**Not proposed, not fixed, no row opened.** The remedy is a three-constant re-aiming of a tool
source, and this batch may not make it.

---

## 6. TASKS 5–7 — the harvest completed, and the population's boundary named

The candidates themselves, with the ruled five fields each, are in
**`cowork_empirical_findings_candidates.md`, PART TWO (§§7–12)**, which lands in the same commit.
**The first harvest's twenty candidates are untouched** — no candidate C1–C20 was edited, renumbered
or re-verdicted, and §3's summary table there still counts the first harvest alone.

### 6.1 `DEFECT_TYPES.md` — MINED WHOLE, and the dispatch's expectation for it is FALSIFIED

**Read whole at the object: the banner, all 26 rows DT-1…DT-26, and the usage note.** Nothing
sampled.

**The dispatch predicts a HIGH pass rate**, on the ground that *"a defect type is by construction the
generalization of an instance, so it is already approach-level."* **The measured result is FIVE
candidates from twenty-six rows, of which TWO propose PASSES.**

**The reasoning's first half holds and its conclusion does not, and the gap is the finding.** The
rows are approach-level — that column passes almost everywhere, exactly as predicted. What fails is
the fact-gate's OWN half: *does the fact survive the implementation being thrown away?* **The
catalog's subject is overwhelmingly this project's own apparatus and working method — auditing,
dispatching, documenting, instrument hygiene, enumeration discipline — and not the music, the corpus
or the analysis's design.** Under the ruled polarity split those rows are **process antipatterns**
and go to the phase definitions' constraints and stop rules.

**So being approach-level is necessary and not sufficient**, and the dispatch's own accompanying
warning — *"a catalog of problem types is exactly where design and process antipatterns are most
likely to be mixed"* — is the half that turned out to be load-bearing.

**Twenty-one of the twenty-six rows route AWAY. Two are flagged**, because they bear on phases this
record has not yet run, and **neither is written anywhere by this batch**:

- **From DT-20 — an instruction whose mandatory preconditions defeat one of its own requirements.**
  Founding instance: a required session-start read leaking exactly what a blinding requirement
  withheld. **This is LIVE in the present arrangement**, not historical — the handover record's own
  standing bar says the governing document carries both withheld passages, so any session taking the
  ordinary session-start read is oracle-aware for both pilot units.
- **From DT-26 — scope-assumed enumeration**, a completeness claim proven only within a scope that
  was never itself checked, whose founding record is **four consecutive audits of one defect family
  each missing sites**. It bears on the audit phase directly, and it is the discipline §6.2 below is
  written under.

### 6.2 The coding side's measurement reports — the population MEASURED BEFORE MINING (E7)

Enumerated with the file tools at the repository root:

| Pattern | Files |
|---|---:|
| `cc_*_report.md` | **241** |
| — of which `cc_instruction_*_report.md` (excluded) | **0** |
| — of which `cc_report_*_report.md` (excluded) | **0** |
| `cc_*_dossier.md` | **25** |
| — of which `cc_instruction_*_dossier.md` (excluded — an instruction) | **1** |
| **THE TASK-6 POPULATION** | **265** |

**Reconciled arithmetically, per DT-26's own discipline:** the 241 were enumerated a second time in
seven disjoint first-letter partitions — `[a-c]` 30, `[d-h]` 40, `[i-l]` 57, `[m-p]` 45, `[q-s]` 52,
`[t-z0-9]` 16, `[A-Z]` 1 — and **30+40+57+45+52+16+1 = 241**, which matches the unpartitioned count
exactly. The `[A-Z]` partition is not decorative: it holds `cc_L6_corpus_oracle_report.md`, which a
lower-case-only enumeration would have dropped silently.

**For contrast, and because it is the measurement that created this task:** the first dispatch's glob
`cc_report_*.md` matches **38** files today (**37** when the previous report measured it — the
difference is that report itself), and **it intersects the 265 not at all.**

### 6.3 THE COVERAGE BOUNDARY — declared, in two shapes, because conflating them is the DT-26 defect

**(a) The signature search reached ALL 265 files.** Every file was searched by pattern for the shape
the artifact inventory's ruled verdict names for this class. **The patterns, listed so the bound is
inspectable and re-runnable:** `measured worse`, `dead end`, `cause undiagnosed`, `not diagnosed`,
`null result`, `negative result`, `no measurable`, `measurably worse`, `made it worse`, `REJECTED`,
`NOT ADOPTED`, `reverted`, `shelved`, `refuted`, `abandoned`, `regress`, `no improvement`, `did not
help`, `inert`, `is inert`, `proved inert`, `no measurable effect`, `zero effect`, `did not move`,
`moves nothing`, `no effect on`. **A finding recorded in words none of these anticipates would have
been missed. That is this search's stated ceiling, and it is not a claim of completeness.**

**(b) TWELVE files were OPENED. TWO HUNDRED AND FIFTY-THREE WERE NOT.** The twelve are listed in
`cowork_empirical_findings_candidates.md` §8.2 with how far each was opened and what each yielded,
**including the three that yielded nothing**. The reading order was the signature search's own
ranking, and **that ordering is declared rather than presented as a neutral sweep**.

**The 253 not opened are named exactly**, as the population minus those twelve — re-derivable by
re-running the two globs — **and the thirty highest-value members are named individually** at §8.2,
being the files the signature search flagged and that were not opened. **A continuation resumes
there. Nothing in this batch claims the harvest of this source is complete.**

### 6.4 ★ THE RULED VERDICT FOR THIS CLASS IS CONFIRMED AT THE OBJECTS

Twelve files yielded **sixteen** candidates, **fourteen** proposing PASSES — against twenty
candidates from four sources in the whole of the first harvest. **And the fifth field is present at
the source**, which is what the first harvest could not obtain: these reports state not only that an
approach was measured worse but WHY, and several state why a neighbouring approach cannot be
substituted. `docs/scoring_model.md` §8, the first harvest's richest source, is a *summary* of
exactly these reports; the diagnosis is what the summary compresses away.

### 6.5 THE CANDIDATE TABLE (Task 7) — 21 NEW, NONE ADMITTED

| # | Candidate | Source | Survives? | Approach-level? | Verdict |
|---|---|---|---|---|---|
| C21 | A mechanism's firing population on the repertoire is measured, not designed | `DEFECT_TYPES.md` DT-7 | YES | YES | **PASSES** |
| C22 | A guard's precondition can exclude the population it was written for | `DEFECT_TYPES.md` DT-14 | YES | YES | **PASSES** |
| C23 | A structural proxy can diverge from its target by close to an order of magnitude | `DEFECT_TYPES.md` DT-9 | PARTLY | YES | **UNDECIDABLE** · #6 |
| C24 | Confidence-like quantities from different stages share no scale | `DEFECT_TYPES.md` DT-8 | PARTLY | YES | **UNDECIDABLE** · strong #6 |
| C25 | A quality measurement an abstention can move is not one | `DEFECT_TYPES.md` DT-15 | YES | YES | **NOT PROPOSED — already homed (#6)** |
| C26 | Duration weight cannot separate a long non-chord tone from an added tone | anchor redesign dossier | YES | YES | **PASSES** |
| C27 | Embellishment discrimination lives in the boundary, not in the sonority | anchor redesign dossier | YES | YES | **PASSES only as restated** |
| C28 | A bass-is-root gate is not a proxy for root correctness | anchor redesign dossier | YES | YES | **PASSES** |
| C29 | Root continuity cannot tell a correct root change from a wrong one | anchor redesign dossier + deltaseven 7a | YES | YES | **PASSES** |
| C30 | The shape of a change is orthogonal to whether it is correct | anchor redesign dossier | YES | YES | **PASSES** |
| C31 | A residual bucket named for an assumed cause can hide the opposite mechanism | stepback report | PARTLY | YES | **UNDECIDABLE** · leans PROCESS |
| C32 | One continuity term is asked to serve two opposite repertoire behaviours | deltaseven 7a + phase E | YES | YES | **PASSES on the conflict; remedy NOT proposed** |
| C33 | A four-pitch-class entry condition cannot fire where the failures live | deltaseven phase E + stepback | YES | YES | **PASSES** |
| C34 | An absent defining third leaves two readings inseparable at that moment | stepback report | YES | YES | **PASSES** |
| C35 | A tritone in a three-pitch-class slice is ambiguous by construction | stepback report | YES | YES | **PASSES** · #6 |
| C36 | A tonic prolongation is evidence-poor for its own tonic | key regression diagnosis | YES | YES | **PASSES** |
| C37 | A fixed beat window imports the next bar's harmony as evidence | key regression diagnosis | YES | YES | **PASSES** (source ranks it secondary) |
| C38 | Aggregating an arpeggiated harmony's pitches does not recover its root | phase D merger report | YES | YES | **PASSES** — tried, measured, reverted, diagnosed |
| C39 | Tonicization-against-modulation separates on the subdominant, not the dominant | b-guard scoping dossier | YES | YES | **PASSES** — widest population here |
| C40 | A structurally-predicted benefit missed on both size and failure mode | eg2 probe report | PARTLY | PARTLY | **UNDECIDABLE** · leans PROCESS |
| C41 | A wrong continued root has no musical future | deltaseven phase E | YES | YES | **PASSES** |

**16 PASSES · 4 UNDECIDABLE · 1 NOT PROPOSED = 21. NOTHING IS ADMITTED.** Every verdict is a
proposal with its reasoning stated in the candidates file so the user can overturn it. **The two
harvests are NOT merged and no combined verdict count is offered**: Part One's verdicts were taken
under their own dispatch and are not reopened.

**Three of the twenty-one are the strongest in either harvest and are named for that reason:**
**C38** is the ruled shape exactly — an approach built, measured, reverted, and diagnosed, with the
source itself naming why the neighbouring approach cannot substitute; **C39** is measured over the
widest population of any candidate in the file; and **C28** is the one place where a proxy and its
target were both computed on the same cases and compared, which is why it passes where the same
claim in the abstract (C23) does not.

---

## 7. TASK 8 — THE GUARD SET, THE ROUNDS, AND EVERYTHING THAT MOVED

### 7.1 Round 1 — three failing

```
python tools/audit/gen_guard_state.py     →  75 guard(s) run, 3 failing, 4 not run, 16 historical record(s)
```

**Each red classified FIRST, at its captured text, before anything was regenerated:**

| Tool | Captured output | KIND | Why that kind |
|---|---|---|---|
| `gen_filing_convention_application.py --check` | *"STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md, OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md. An unclassified candidate is a STOP, never a silent pass (D-661)."* | **DECISION** | It demands an **authored verdict** and halts for the want of one. This is the standing red [[OI-372]]. **NEVER regenerated, never run in write mode, not investigated, no verdict authored for it.** |
| `gen_evidence_pin_membership.py --check` | *"STALE vs the derivation: evidence_pin_membership.json does not re-derive"* | **STALENESS** | It reports an artifact that no longer re-derives and demands no verdict. Regenerated. |
| `gen_session_start_read_size.py --check` | *"STALE vs the measurement: session_start_read_size.json does not re-derive"* | **STALENESS** | Same shape. Regenerated. |

**Neither staleness red needed §0's fallback**: the kind is unambiguous at the captured text in both
cases. **No decision red beyond the standing one appeared, so A5 is not falsified.**

**The evidence-pin staleness is the expected class and is noted in one line, as ordered:** landing
four root-level ruling records at Task 0 turned it stale, the derivation reading every root-level
`cowork_rulings_*.md`; regenerated under the sweep rule, and not reported as a notable consequence.

**The session-start-read staleness is this batch's own, by construction and not by surprise:** Task 4
changed `STATUS.md`, and that measurement is over the session-start read of which `STATUS.md` is a
member.

### 7.2 The regeneration

```
python tools/audit/gen_evidence_pin_membership.py   → wrote tools/audit/evidence_pin_membership.json
                                                      ruling records read 68; members 7 — pinned 5, UNRESOLVED 0
python tools/audit/gen_session_start_read_size.py   → wrote tools/audit/session_start_read_size.json
```

Both re-derived and both cleared. **No tool source was touched by either run.**

### 7.3 Round 2 — the fixpoint, in TWO rounds

```
python tools/audit/gen_guard_state.py     →  75 guard(s) run, 1 failing, 4 not run, 16 historical record(s)
```

**The guard summary in its ruled shape, read at `tools/audit/guard_state.json:1407–1420`:**

| | |
|---|---|
| run | **75** |
| passing | **74** |
| failing | **1** |
| not run | **4** |
| historical records | **16** |

**failing_tools:** `tools/audit/gen_filing_convention_application.py --check` — **[[OI-372]], the
standing DECISION red, alone.** **E6 is MET.** No third round was needed and none was run: nothing
was regenerated after round 2, so there was nothing for a third round to re-measure.

### 7.4 ★ EVERYTHING THAT MOVED — not only what appeared in a failing set

The dispatch warns that two guard-set members run in living mode and write on every run, and that
more may move than the failing set names. **Measured, by enumerating changed paths after each round
and hashing the artifacts:**

| Path | Before | After | Cause |
|---|---|---|---|
| `tools/audit/guard_state.json` | `efd08d21…` after round 1 | `3f3c7924…` after round 2 | The living-mode writer, by construction — it records each run. |
| `tools/audit/evidence_pin_membership.json` | `14bb366c…` | `7730eed4…` | Regenerated under the sweep rule. |
| `tools/audit/session_start_read_size.json` | `ad2072bb…` | `21c3d4df…` | Regenerated under the sweep rule. |

**AND NOTHING ELSE MOVED.** The tracked-modified set after round 1 was exactly
{`STATUS.md`, `STATUS_ARCHIVE.md`, `open_items/OI-374.md`, `open_items/OI-376.md`,
`tools/audit/guard_state.json`} — the first four being this batch's own Task-4 edits and the stopped
batch's two riders — and after round 2 it was that set plus the two regenerated artifacts. **No third
artifact appeared in either enumeration**, and `open_items/register_check.json`, which one guard's
own output names as a file it writes, re-derived identically and does not appear.

### 7.5 ★ THE [[OI-374]] ENCODING CLASS DID **NOT** REPRODUCE, AND THAT IS ITSELF A MEASUREMENT

The previous batch reported that its guard run flipped a captured PASS message to a replacement
character because it was launched from a different shell. **This batch's guard artifact reads
`"OVERALL PASS — bijection holds…"` with the em dash intact** (`tools/audit/guard_state.json:1388`),
byte-identical in that respect to the tip's copy.

**The variable was controlled deliberately:** both guard runs were launched from PowerShell with
`PYTHONIOENCODING=utf-8` set. **This corroborates [[OI-374]]'s recorded diagnosis from the positive
direction** — the launching shell is the variable, and setting the interpreter's output encoding
holds the captured text steady. **Reported. Nothing is fixed, the row is not flipped, no remedy is
proposed, and no row is opened.**

### 7.6 A consequence for the NEXT batch, reported because a batch cannot see its own successor

`gen_filing_convention_application.py`'s STOP names three derived candidates with no authored
verdict, one of which is a `cc_report_*.md` file. **This report is a new root-level document of the
same family**, and it lands after the guard run, so **it may present as a fourth unclassified
candidate to that same DECISION red on the next run.** That is a prediction, not a measurement — the
guard was not re-run after this file was written, because doing so would have been a run whose only
purpose was to inspect the standing red. **Stated so it is not met as a surprise (#13).**

---

## 8. REGISTERED EXPECTATIONS E0–E8, with the measurement beside each

| | Expectation | Verdict | The measurement |
|---|---|---|---|
| **E0** | The six paths of Task 0 land byte-identical to the Task-1 measurement, with the side stated | **MET** | **Side: the GIT BLOB** (§1.3). All six blob identities at `0a2675855c…` equal the pre-commit `git hash-object` values: `6ba98a06…` handoff, `9605da50…` next-act, `06e3f619…` second-vector, `3474d415…` regress-termination, `38fe75b5…` v1-sufficiency, `0a29ab41…` the instruction file. |
| **E1** | `grep -n "inspectable" decisions/group_S.md`: zero before Task 2, at least one after | **NOT MET — because Task 2 STOPPED** | **Zero before, zero after.** Nothing was written. The STOP and its four measurements are §3. |
| **E2** | Exactly three entries of `decisions/group_S.md` changed, and they are D-182, D-181, D-187 | **NOT MET — because Task 2 STOPPED** | **ZERO entries changed.** `decisions/group_S.md` is not in either commit and is byte-unchanged. |
| **E3** | The Task-3 identifier appears in `DECISIONS.md` exactly once, no row renumbered | **NOT REACHED — because Task 3 STOPPED** | **No identifier was allocated.** `grep D-678 DECISIONS.md` → zero, before and after. No row moved; `DECISIONS.md` is in neither commit. **A2 nonetheless HOLDS and D-678 is reported at §4.3.** |
| **E4** | `OPEN_ITEMS.md` is in neither commit | **MET** | `changed_paths.py --commit` on both commits: 6 records and 11 records, and `OPEN_ITEMS.md` is in neither. It was never opened for writing. |
| **E5** | No path under `tools/` ending `.py` is modified | **MET** | Of the 17 records across both commits, three are under `tools/` and all three are generated `.json` artifacts: `guard_state.json`, `evidence_pin_membership.json`, `session_start_read_size.json`. **No `.py` path in either commit.** ★ **But see §5.4: E5 is what blocked the ruled forward-bound tool, and that conflict is reported rather than resolved.** |
| **E6** | The failing set at Task 8's last round is [[OI-372]] alone | **MET** | Round 2: 75 run, 74 passing, **1 failing**, and `failing_tools` names `gen_filing_convention_application.py --check` and nothing else. Reached in two rounds, well inside the three-round cap. |
| **E7** | The population count is measured and stated before Task 6 mines it, and the files not reached are named | **MET** | **265** (§6.2), measured before any file of that population was opened, and reconciled arithmetically across seven disjoint partitions. **253 not reached**, named exactly as the complement and with thirty flagged members named individually (§6.3, and the candidates file §8.2). |
| **E8** | No path of the ~834 standing untracked population is in either commit | **MET** | The Task-0 commit adds five untracked paths, all five named in §2's list of nine. The Task-9 commit adds four, all four named in Task 9's own path list. **The nine §2 paths and the standing population are disjoint by §2's own construction**, and no other untracked path was staged at any point. |

---

## 9. THE ASSUMPTIONS OF §3 — which were falsified, and how

| | Assumption | Outcome |
|---|---|---|
| **A1** | The record's Limbs A and B carry amendment text complete enough to apply verbatim, with **no interpretation needed to site it** in `decisions/group_S.md` | **★ FALSIFIED.** The TEXT is complete; the SITING is not determinable. Four independent measurements at §3.2 show the register cannot carry it, and the record itself names a different target — *"their home file"* — which is the one file the dispatch forbids editing. |
| **A2** | The register's allocation convention determines a **unique** identifier | **HOLDS.** Measured at §4.3: identifiers dense D-001…D-677, arithmetic enforced by the generator on every render, next free = **D-678**. **Reported rather than used**, since Task 3 stopped for a different reason. |
| **A3** | `DEFECT_TYPES.md` and the `cc_<topic>_report.md` / `cc_<topic>_dossier.md` population are the **only** two harvest sources the previous batch did not reach | **NOT TESTED, and stated as such.** This batch mined both and did not attempt to establish that no third unreached source exists. **A3 is neither confirmed nor falsified here**, and no claim of harvest completeness rests on it. |
| **A4** | Regenerating `evidence_pin_membership.json` clears the staleness red | **HOLDS, and is now measured rather than assumed** — the dispatch notes no side had claimed it. Regenerated; the check passed at round 2. |
| **A5** | No amendment at Tasks 2 and 3 turns a **decision** red on | **HOLDS VACUOUSLY, and the vacuity is stated.** No amendment was made, so the assumption was never exercised. The only decision red at any round is the standing one. |

**A sixth thing was falsified that no assumption covered**, and it is the batch's most useful
finding after A1: **the dispatch's predicted "high pass rate" for `DEFECT_TYPES.md`** (§6.1). It is
not an assumption of §3, so it is recorded here rather than in the table.

---

## 10. FINDINGS ROUTED UNDER RULING 9 OF 2026-08-21

**No register row was opened. No open-items row was created, flipped or discarded. No finding number
was allocated — Ruling 9 opens no findings series. Nothing was fixed. No remedy is proposed for
anything below.**

### 10.1 APPARATUS findings — REPORTED, not rowed

1. **The ruled amendments have no site in the register, and the register cannot be made to carry
   them without an act the dispatch forbids** (§3). Four measurements; the record's own words name
   `CLAUDE.md`.
2. **The sharpened decision-surface rule exists in three materially different wordings** (§4.1–4.2),
   and this dispatch's own §0 introduces a fourth rating vocabulary.
3. **The rule's two registered siblings sit in different register groups**, so a third has no
   determined group (§4.4).
4. **E5 and the no-tool-source bar block the ruled `STATUS.md` forward bound** (§5.4). The mechanism
   the ruling installed is re-aimed every batch by editing three constants in a tool source.
5. **The dispatch's predicted high pass rate for `DEFECT_TYPES.md` is falsified**, and the reason —
   the catalog's subject is the apparatus, not the analysis — is the finding (§6.1).
6. **DT-20's shape is LIVE in the present arrangement**: a mandatory session-start read carries what
   a blinding requirement withholds (§6.1). Routed to the phase definitions on paper; **written
   nowhere**.
7. **This report may present as a fourth unclassified candidate to the standing decision red on the
   next run** (§7.6).
8. **The `PREVIOUS_AIMINGS` record of the forward-bound tool now has a gap** — the move this batch
   performed is not in it (§5.4).

### 10.2 ANALYSIS findings — NONE OF THIS BATCH'S OWN MAKING

**This batch measured nothing about the analysis, built and ran no measurement tool over it, and made
no analysis finding of its own.** Every one of the twenty-one candidates is a **RELAY** of a finding
already in the record, judged against the admission test and proposed for the user. **Nothing is
routed to the quarantined audit questions, and the five quarantined questions stand exactly as
found.**

### 10.3 DISCARDED — with finding, date and reason

**One.**

- **Finding:** the first attempt to summarise the changed-path enumeration used shell text utilities
  (`wc`, `grep`, `awk`) aimed at a scratchpad path written as an unexpanded shell variable. **The
  shell-read guard DENIED it**, correctly by its own rule and incorrectly by its own published
  false-deny shape — the unexpanded variable is `OPEN_ITEMS.md` OI-300's shape (2), a path outside
  the working tree that the guard cannot resolve and therefore treats as inside.
- **Date:** 2026-08-26.
- **Reason it is DISCARDED rather than rowed:** the guard's refusal cost one call and nothing else;
  the readings were re-taken through the file tools, and **no claim in this report or in the
  candidates file rests on any shell read of a repository path**. Under amended #10's worth test it
  risks neither something being built that does not serve maximum-precision inference nor code
  ceasing to be comparable against its specification. The #19 carve-out does not apply — it is not an
  establishment obligation. **It is recorded rather than dropped because the shape is a known,
  published false-deny that has now fired again in ordinary work (#12).**

---

## 11. ★ A PROPOSAL, NOT AN ACT — register entries for the rulings that have none

**Written in this report only. NOTHING BELOW IS WRITTEN ANYWHERE. No identifier is allocated, no
entry is created, no group is assigned, and no home is claimed.** Whether these are entered, under
what identifiers, in which groups and at which homes is the user's to rule.

**The identifiers proposed run from D-678**, the next free identity measured at §4.3, in the order
the rulings were given. **The order is itself a proposal**: nothing in the record fixes it.

**The group is proposed as T (standing process rules)** for every one of them, on the ground that
`D-231` — the phase-sequencing rule these all operate inside — sits in T with its home in
`CLAUDE.md`. **The alternative is K (documentation governance)**, where `D-424` sits, and it is a
live alternative rather than a courtesy: the subject of these rulings is the production of
specifications, which is what K names. **§4.4's finding applies here too** — the family is split
across groups today, and this proposal does not resolve that.

### 11.1 The three rulings of `cowork_rulings_2026_08_25_v1_sufficiency_sitting.md`

| Proposed ID | Proposed title | Status | Proposed home, with the reasoning |
|---|---|---|---|
| **D-678** | The derivation method is ruled USABLE for v1 on the user's ground — a first specification cannot be the ultimate one because the sources are not exhausted until the audit has run, so the best derivable from everything held except the code is good enough by construction | **LIVE** · 2026-08-25 · user | The **register itself**, under rule (n): this is an establishment verdict about a measurement route, and rule (n) makes such a verdict register business with its evidence pointed at the record that took it. **Alternative:** `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3.2, whose pilot postcondition this ruling discharges by its first limb, and which `CLAUDE.md` names as the ruled definitions' ONE home. |
| **D-679** | Independence of a deriving session from the shipped code is evidenced by the ten DIFFERS rows of the comparison reading — a session covertly reading the implementation does not produce ten disagreements with it | **LIVE** · 2026-08-25 · user | **Unresolved, and stated as such.** The natural home, the comparison reading's §6, **RECORDS FINDINGS rather than STATING RULES**, which rule (h)'s kind half excludes. The register under rule (n) is the fallback. **This one needs a ruling, not a default.** |
| **D-680** | The framework and detail-specification phases are NO LONGER HELD; E (the user's judgement of the existing derivation) and C (the re-run of the held-out test) are neither the next act nor owed; the empirical findings ledger is UNTOUCHED and still owed as a framework-phase input | **LIVE** · 2026-08-25 · user | `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3 — the ruled definitions' ONE home, which `CLAUDE.md` points at and does not restate. This ruling changes a phase's STATUS, which is what that section carries. |

**Recorded with D-680, because it changes an existing entry's standing:** this ruling **supersedes
as the ordering** Ruling 3 of `cowork_rulings_2026_08_25_regress_termination_sitting.md` (*E first,
then C with B running alongside*). **If that earlier ruling is entered at all, the two entries are a
supersession pair** and neither should be entered without the other, on the register's own
supersession convention.

### 11.2 ★ AND THE TWO RULINGS TASKS 2 AND 3 WERE TO EXECUTE HAVE NO ENTRIES EITHER

The dispatch's §7 asks for proposals for *today's three rulings*. **The two rulings of the
regress-termination sitting are in the same position** — recorded in a file and in no register — and
they are the two this batch was sent to execute and could not. **They are proposed here so the
picture is whole, and they are equally unwritten.**

| Proposed ID | Proposed title | Status | Note |
|---|---|---|---|
| **D-681** | An establishment demand with no inspectable object is terminated by SCOPE and by DECLARATION — #19's objects are the four it names and each is an inspectable, re-runnable artifact; #18 reaches a causal claim only where it is checkable; and #24 extends from figures to results, a declared bound discharging an establishment demand that has no inspectable object and never one that has | **LIVE** · 2026-08-25 · user | Home: `CLAUDE.md`, at principles #18, #19 and #24 — **which is exactly the act §3 could not perform.** An entry recording this ruling while its clauses are not at their home would put the register ahead of the specification, which is the drift the batch exists to close, in the other direction. **Entering it and applying it are the same question and should be ruled together.** |
| **D-682** | The sharpened decision-surface rule is registered under its own identifier; and every decision surface states in one line which ratified phase the act it proposes serves, saying "none" where it serves none, with no running tally kept | **LIVE** · 2026-08-25 · user | **This is the entry Task 3 was to write.** It cannot be written until §4's question is answered, because the rule's text is exactly what differs between the three restatements. **The second limb — the phase field — has no such problem and could be entered on its own**, which is recorded as an option and not as a recommendation. |

**No identifier above is reserved by this report.** If any other act allocates before the user rules,
the numbers shift and the proposal shifts with them.

---

## 12. THE STANDING SELF-CHECK OVER THIS BATCH'S OWN DIFF

Performed against the diff on disk, not against the memory of writing it.

- **`STATUS.md`** — one line replaced. The arithmetic accounts for the source object to the byte
  (§5.1). The new entry restates **no count, no identity and no rendered value** (D-431), names its
  dispatch and its report as a pointer, and **does not assert the end state**, which the E-ordering
  rule forbids in a commit's own content.
- **`STATUS_ARCHIVE.md`** — appended only; nothing that stood in it moved. The moved entry came from
  a content-addressed object read and was never retyped. The departure from the ruled tool is
  declared **in the archive block itself**, so a later reader meets it at the site rather than only
  in this report.
- **`cowork_empirical_findings_candidates.md`** — Part One is byte-unchanged; every added candidate
  carries its provenance at file and line, its uncertainty **in the source's own words**, and its
  establishment status **as the source declares it**. Re-read for the failure the first dispatch
  warns of — *do not paraphrase a source into a stronger claim than it makes*: **C27 is the one place
  a restatement would strengthen its source, and it is marked "PASSES only as restated" with the
  implementation-bound half explicitly not proposed**; **C32 carries its source's own unmet condition
  (*"must still be corpus-validated on both presets before any commit"*) unaltered**; **C37 carries
  its source's own ranking of itself as secondary**; and **C38 carries the limitation that its
  source's corpus-wide regression claim rests on the test suites rather than on the corpus gate,
  because the change was reverted before a corpus run.**
- **★ TWO MISCOUNTS WERE FOUND BY THIS CHECK AND CORRECTED.** The candidates file's §10 read *"15
  propose PASSES"* and its §8.3 read *"thirteen of them"*; both were one short of the table they
  summarise (16 PASSES + 4 UNDECIDABLE + 1 NOT PROPOSED = 21). **Corrected, with the correction
  declared in the file itself and in the commit that carries it**, rather than made silently. The
  correction lands in this report's commit and not in the commit that wrote the table, which is
  stated rather than left to be discovered.
- **The three guard artifacts** — not authored; written by the runs. Every one is accounted for at
  §7.4, including the living-mode writer that moved without appearing in a failing set.
- **No tool source, no `src/`, no test, no golden, no corpus of scores, nothing under
  `tools/robust_stop/`, no governing document.** Verified at both commits' own path lists.
- **The E-ordering rule is not breached:** neither commit message asserts its own end state, and the
  guard summary appears only here, in the second commit.
- **Vocabulary:** *measurement tool* throughout, never *instrument* except inside a quotation, where
  it is the source's own word; *a changed passage*, never *hunk*; *the current commit* or an explicit
  hash, never a bare abbreviation; *towards the objective* / *towards the principles* where an option
  is rated.

---

## 13. DECLARED DEPARTURES — what was not read, and what was relayed rather than measured

**Read, and it matters for what this session may judge.** The governing document `CLAUDE.md` reached
this session in full as part of its own start-up context, together with `STATUS.md` and
`DECISIONS.md`. **Under the fifty-sixth handoff entry's standing bar that makes this session
ORACLE-AWARE FOR BOTH PILOT UNITS.** Accordingly: **neither blind derivation output was opened at
all, no oracle document was opened, no comparison was made, and no verdict of any kind was taken on
either output, on the derivation method or on the blinding failure.** `ARCHITECTURE.md` was not
opened. `BUILD_AND_TEST.md` was not opened — this batch ran no build, no test and no measurement of
the analysis, which is the condition its read is now gated on.

**Not read.** `cowork_rulings_2026_08_25_next_act_sitting.md` and
`cowork_rulings_2026_08_25_second_vector_sitting.md` were **landed at Task 0 and never opened** — the
dispatch names them for landing and not for absorption. `cowork_blind_session_opening_instruction_harmony_boundary.md`
was **landed and never opened**. `cowork_handoff.md` was read at its sixty-fifth entry's §§ on this
sitting's rulings, at the sixty-fourth and sixty-third entries' opening blocks, at the sixty-third
entry's §6, at the fifty-first entry whole, and at targeted searches — **NOT whole**.
`DECISIONS.md` was read at its preamble, its how-to-read guide, its group S and group T tables and
its provenance block — **NOT whole**. `decisions/group_S.md` was read at its banner and at entries
D-165…D-188 — **NOT whole**. `tools/audit/decisions/backbone_decisions.json` was read at D-182,
D-183 and its retired-entries block only.

**Relayed, not re-measured.** The previous batch's account of the guard set at the tip, of the two
riders' content, and of its own reading of `docs/scoring_model.md` §8 — taken as that report states
them and **not** verified at the objects. [[OI-374]]'s diagnosis that the launching shell is the
variable — relayed from the cascade-sweep batch; what this batch measured is only that the em dash
survived under a controlled encoding (§7.5), which corroborates but does not establish it. The
previous batch's worktree sha256 figures — quoted at §1.3 for the length comparison only, **never
compared as digests**, the two sides using different hash functions.

**Measured by this session, at the objects.** Both refs, from the three ref files with the file
tools. The tracked and untracked populations, by the sanctioned enumeration tool, at four points in
the batch. Every blob identity and length in §1.3 and §5.1, by `git hash-object` and
`git cat-file -s`. The `decisions/group_S.md` entry texts, against the ruling record's quotations.
The register's identifier density, at the source data and the rendered index. The three restatements
of the decision-surface rule, at their own lines. The 265-file population, twice, by disjoint
partitions reconciled arithmetically. Every guard verdict and every captured red, at
`tools/audit/guard_state.json`. Both commits' path lists, by explicit hash.

**Not attempted.** No third unreached harvest source was searched for (A3). No claim is made that the
coding side's measurement reports are exhausted — 253 of 265 were not opened, and §6.3 names them.
No re-run of the guard set was taken after this report was written, so §7.6's prediction is a
prediction.

---

## 14. WHERE THIS LEAVES THINGS

**Landed, in order:** `0a2675855c5a92fc2e32cd55c05281ba4d2c24e6` (the writing-side files) and
`bae32fec8f4845868b22361ed3faea965aa87216` (the batch's work). This report landed as the third
commit, `da06b82079e56e6c107ffb2a6cd07925a5434c19`, **together with — and not alone — the two-figure
correction §12 records**, because a correction the self-check found in a file the previous commit had
already written cannot land in that previous commit. **A fourth commit carries this paragraph and
nothing else**, correcting a sentence of this report that said *"alone"*: the statement was false of
the commit it described, and #10 does not let a document state something false about itself. **No
other word of this report changed, and no measurement in it moved.**

**The closing tree, measured after the report's own commit** and recorded here because no earlier
commit could carry it: `python tools/audit/changed_paths.py` → **831 changed path record(s)
[worktree]**, **every one of them untracked**. **ZERO tracked modifications remain.** The arithmetic
closes against §1.2's start state: 840 untracked at Task 1, less the nine §2 paths this batch landed,
is 831; and the four tracked modifications §1.2 found are all committed. **Nothing of the standing
untracked population was committed, touched or re-litigated.**

**Owed and NOT discharged, stated as facts and not as asks:**

1. **The three ruled clause amendments are not written anywhere.** §3 states why and names the three
   available routes without choosing.
2. **The sharpened decision-surface rule is not registered.** §4 states which restatement question
   must be answered first, and reports **D-678** as the identifier the convention determines.
3. **The forward bound's tool is not re-aimed**, and its record of aimings has a gap (§5.4).
4. **The harvest of the coding side's measurement reports is 12 of 265 files deep**, with the
   complement named exactly and its thirty most promising members named individually (§6.3).
5. **[[OI-372]] stays the one standing red**, untouched and never run in write mode. **[[OI-179]]
   stays OPEN and GATES** — not re-confirmed by this batch. **[[OI-374]], [[OI-376]] and [[OI-377]]
   stand as found**, apart from the two riders the stopped batch had already applied and this batch
   landed. **The five quarantined questions and the three deferred apparatus items stand.**
6. **The empirical findings ledger is still owed and was not built.** Forty-one candidates now stand
   proposed across two harvests; **none of them is admitted**, and admission is not a session's act.

# CC REPORT — ENUMERATE, DRAW, SEAL AND COMMIT THE PLACEMENT SAMPLE

*Claude Code, 2026-08-27. Dispatch: `cc_instruction_placement_sample.md`, which executes Rulings 1,
2 and 3 of `cowork_rulings_2026_08_27_placement_sample_sitting.md`. Start tip
`0e7186a961f50b32e0552483b289b11069f1319a`, read at `.git/refs/heads/master` with the file tool —
the ref side — and it matched, so Task 0(a)'s STOP did not fire.*

> **★ THIS REPORT DELIBERATELY DOES NOT CARRY THE DRAWN ITEMS, AND THAT IS A CHOICE WITH A GROUND.**
> The sealed sample is withheld from the frame's author (Ruling 3 of 2026-08-27). A report that
> restated the drawn items, or the full enumerations they were drawn from, would be a second copy of
> the withheld material standing outside the withheld file — and the frame's author is a **fresh**
> Cowork session that may reasonably open a coding-side report. Task 5(d) asks this report for each
> stratum's **defining object, its quotation, its `N`, census-or-take and `k`**, and it asks for no
> item; that is exactly what is below. **The drawn items live only in
> `cowork_placement_sample_sealed_2026_08_27.md`.** If the writing side wants them restated here,
> that is a ruling, not an omission to be corrected quietly.

---

## 1. THE HEADLINE — FOUR STRATA ARE STOPPED, AND THE FRAME IS GATED ON EVERY ONE OF THEM

Eight strata were enumerated at their objects. **Four are drawn and sealed. Four are STOPPED.**

| # | Stratum | Outcome | `N` | census / take | `k` |
|---|---|---|---|---|---|
| 1 | ruling records | **STOPPED** — two named objects disagree | — | — | — |
| 2 | decision surfaces | **STOPPED** — no object enumerates the class | — | — | — |
| 3 | dossiers | **STOPPED** — no defining artifact; the unit is also undeterminable | — | — | — |
| 4 | DEFERRED entries of the decisions register | drawn | 21 | **census** | n/a |
| 5 | the evidence inventory | drawn | 33 | take | 1 |
| 6 | declared dormancies | **STOPPED** — no defining artifact; three readings disagree | — | — | — |
| 7 | every current document heading | drawn | 730 | take | 29 |
| 8 | every heading ever deleted from the document set | drawn | 59 | take | 2 |

Drawn items: 21 + 25 + 25 + 25 = **96**.

**The gate.** The sealed file's banner states, first and where it cannot be missed, that **the frame
is not authored until the user has ruled on every stopped stratum**. That is Ruling 3 of 2026-08-26
read plainly, as the dispatch's Task 3 requires: a sample missing a stratum nobody ruled on is not
sealed, it is incomplete.

**No stratum enumerated to zero.** The dispatch's provision for `N = 0` is unused.

**In no drawn stratum are two items identical on all three ordering keys**, so the Task 2.1 STOP did
not fire. *(The dispatch words that condition with the verb "tie"; this record avoids the word in its
own prose under the reserved-word convention, and changes nothing about the condition.)* The third
ordering key was **load-bearing in stratum 8**: three items share `ARCHITECTURE.md` line 635 and are
separated only by their deleting commit hashes.

---

## 2. TASK 0 — THE START STATE AND THE LANDING

### 2.1 The start state, measured by the tool and not by `git status` (D-253)

`python tools/audit/changed_paths.py`: **839 changed-path records — 838 untracked and exactly ONE
tracked modification, `cowork_handoff.md`.** Nothing of the standing untracked population was
committed beyond the seven paths Task 0(c) names.

### 2.2 The establishment of the tracked-modified handoff — done BEFORE it was committed

Task 0(c) required the modification to be established rather than taken from the dispatch's account
of it. It was established on both sides, and the two sides agree.

**The BLOB side**, by content-addressed read at explicit hash. `git rev-parse
0e7186a961f50b32e0552483b289b11069f1319a:cowork_handoff.md` resolves to blob
`18388cc93943a63bf7d6ea514fc307d316afdc14`, measuring **783,112 bytes, 9,445 lines, LF endings, a
terminating newline, no CR anywhere**, and carrying **122** markdown headings.

**The WORKTREE side**, by the file tools. `cowork_handoff.md` measures **9,879 lines** and carries
**149** markdown headings.

**The reconciliation.** 9,879 − 9,445 = **434**. Every one of the blob's 122 headings is re-found in
the worktree at a uniform offset of **+434** from blob line 4 onward, with the file's own title line
unmoved at line 1; the **27** headings with no blob counterpart all stand between worktree lines 4
and 437. So the change is **ADDITIONS ONLY, PREPENDED, in one contiguous block, with no earlier
entry reworded and no heading lost.**

**The object-to-object confirmation.** After staging, the working copy's blob is
`a984d5a87d2d7ff8d9e5ebb3828ad5b936fd7598` (812,048 bytes). `git diff
18388cc93943a63bf7d6ea514fc307d316afdc14 a984d5a87d2d7ff8d9e5ebb3828ad5b936fd7598` — two explicit
hashes, the permitted object-to-object form — reports **one hunk, `@@ -1,5 +1,439 @@`, 434
insertions and ZERO deletions**. It closes exactly against the line arithmetic.

### 2.3 ★ ONE CORRECTION OF RECORD TO THE DISPATCH, REPORTED RATHER THAN SMOOTHED

The dispatch's Task 0(c) says of `cowork_handoff.md`:

> It carries the sixty-eighth entry from 2026-08-26 and a sixty-ninth entry added 2026-08-27,
> **additions only, prepended, no earlier entry reworded**.

**The characterisation is confirmed at the object. The count is not.** The tip blob's topmost entry
is the **SIXTY-SIXTH**, so **three** entries are new against the tip, not two:

| Entry | Worktree line |
|---|---|
| sixty-ninth (2026-08-27) | 4 |
| sixty-eighth (2026-08-26) | 118 |
| **sixty-seventh (2026-08-26)** | **265** |
| sixty-sixth (2026-08-26) — the tip blob's topmost | 438 |

Nothing turns on it for this batch — the whole file was landed either way — but the writing side's
account of what stood untracked was short by one entry, and a later reader reconciling the handoff's
history against the commits would find the difference.

### 2.4 The landing

**Commit `9053861b9cc71d8de8dc9c12105abd553620b55a`**, 7 files changed, 2,273 insertions:
`cowork_handoff.md` (modified, +434/−0) and six created —
`cowork_framework_phase_opening_surface_2026_08_26.md`,
`cowork_rulings_2026_08_26_framework_opening_sitting.md`,
`cowork_literature_reachability_2026_08_26.md`,
`cowork_placement_sample_surface_2026_08_27.md`,
`cowork_rulings_2026_08_27_placement_sample_sitting.md`, `cc_instruction_placement_sample.md`.

Then `python tools/audit/gen_evidence_pin_membership.py` ran, as ordered: *"wrote
tools/audit/evidence_pin_membership.json — generated ratification documents 7; ruling records read
74; members 7 — pinned 5, UNRESOLVED 0; tools carrying a pin constant 8; outside this class 3."*
**That run is also one half of stratum 1's STOP** — see §3.1.

---

## 3. TASK 1 — THE EIGHT STRATA AT THEIR OBJECTS

For each: the defining object, the text relied on, and the outcome. The full quotations stand in the
sealed file; the load-bearing ones are repeated here because Task 5(d) asks for them.

### 3.1 Stratum 1 — ruling records — **STOPPED: two named objects disagree**

**Object A — `tools/audit/gen_evidence_pin_membership.py`**, the tool this dispatch itself ordered
run at Task 0(c). It publishes the definition among the things it DERIVES, at line 29:

> `RULING RECORDS       Every root-level `cowork_rulings_*.md`.`

implemented at line 112 as `RULING_RECORD = re.compile(r'^cowork_rulings_.*\.md$')`, and its output
`tools/audit/evidence_pin_membership.json` carries the same words in its own
`the_derivation.ruling_records` field. Its run reported **`ruling records read 74`**.

**Object B — `tools/audit/gen_artifact_inventory.py`**, the derived walk of the whole tree, class
`writing-side-ruling-records`, lines 245–249:

> `"repository-root files whose name begins `cowork_rulings_`, `cowork_ruling_`,`
> `` `cowork_owner_rulings_`, `cowork_pending_rulings_` or `cowork_document_route_rulings_`" ``

That class and its signature were **put to the user and ruled** — the reading surface is
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` §16, which carries the signature
verbatim.

**The disagreement, measured.** Object B admits four root-level files Object A excludes, all four on
disk at the seal: `cowork_ruling_guard_family_2026_08_08.md`, `cowork_owner_rulings_2026_08_07.md`,
`cowork_pending_rulings_2026_08_02.md`, `cowork_document_route_rulings_2026_08_08.md`. **74 files
against 78.** Because the declared unit is a numbered ruling *inside* a record, the item count
differs by more than four and `k = floor(N/25)` differs, so the two readings give **entirely
different draws** — not one draw four items longer.

**What is missing:** a ruling naming which object defines the stratum. Nothing else: both objects
exist, both are generated, both are current, and each is unambiguous on its own terms.

**One axis checked and found inert**, so the writing side does not have to: at the start state
exactly **two** root-level ruling records stood untracked, and both were landed by Task 0(c), so
working-tree and tracked membership coincide at the seal.

### 3.2 Stratum 2 — decision surfaces — **STOPPED: no object enumerates the class**

**Candidate A — the directory `ratification_surfaces/`**, named as a class at
`tools/audit/gen_artifact_inventory.py:240-242` (*"anywhere below `ratification_surfaces/` — the
reading surfaces a ruling was taken on"*). Its authored reason on the ruling surface (§15) is the
only place in the record that says what a decision surface **is**: *"a decision surface argues from
principles toward a choice, which is design intent by construction."* **31 files** at the seal.

**Candidate A is refuted as complete, at the objects.** Decision surfaces stand at the repository
root, outside that directory: `cowork_extent_decision_surface.md`,
`cowork_phase1_commissioning_surface_2026_08_11.md`,
`cowork_framework_phase_opening_surface_2026_08_26.md`,
`cowork_placement_sample_surface_2026_08_27.md`. The writing side's own text says so —
`cowork_placement_sample_surface_2026_08_27.md:239-241` lists what the frame's author must read
(*"this handoff, yesterday's ruling record, the opening surface, the plan, the phase-definition
surface"*) and then: *"Those are ruling records and decision surfaces: two of the eight strata the
sample is drawn from."* The *opening surface* in that list is a root-level file.

**Candidate B — `tools/audit/gen_ratification_surface_set.py`** and its output. Its CLASS reading
(lines 15–18) is *"every root-level document whose own opening declares it a ratification queue or a
ratification review aid"* — a **different subject** (queues and review aids, not surfaces that argue
alternatives) and root-scoped, so it excludes the directory Candidate A is. The two do not disagree
at the edges; they enumerate different kinds.

**What is missing:** an object, or a ruling, saying which documents are the decision surfaces.

### 3.3 Stratum 3 — dossiers — **STOPPED: no defining artifact, and the unit is undeterminable**

**The one object that could have supplied the membership declines to, deliberately.**
`tools/audit/gen_artifact_inventory.py` is this project's only derived, whole-tree, user-ruled
classification of every file — all 44 classes were put to the user and ruled. **It has no dossier
class.** It lumps dossiers in by path prefix, naming them in the class descriptions:
`writing-side-design-documents` (line 257) is *"every other repository-root file beginning `cowork_`
— designs, audits, **dossiers**, plans, inventories and findings"*, and `reports-from-the-coding-side`
(line 270) is *"every other repository-root file beginning `cc_` — the reports, **dossiers** and
measurement outputs CC returned"*. Lines 25–29 state why it will never separate them: *"THE SIGNATURE
IS PATH AND EXTENSION ONLY … a signature that opens a file is one that can be argued about, and this
table cannot."*

**The only remaining candidate is the filename convention `*_dossier.md`**, which the record nowhere
establishes. It matches **26** root-level files, and it collides with the ruled classification for at
least one: `cc_instruction_stage3_4i_gate_retirement_dossier.md` is a **dispatch** under
`dispatches-to-the-coding-side` (line 266: *"repository-root files beginning `cc_instruction_` — one
dispatch per CC session"*) and a **dossier** under the convention.

**A second, independent reason: the declared unit — "one claim or finding entry in a dossier" — has
no determinable form.** No dossier declares a claim or finding entry as its unit of record, and the
two opened to check use unrelated structures: `cowork_adjudication_dossier.md` is two Parts (`## Part
A — the seven audit adjudications, in plain language`, line 14; `## Part B — the 17 siloed facts:
complete disposition …`, line 90); `cc_functional_residual_dossier.md` is numbered task sections with
sub-sections (`## §0 — Task 0: the headroom decomposition …`, line 22; `### §0.1 — The three headline
counts (NEW vs OLD)`, line 33). **Even with the membership ruled, the items could not be enumerated
until the writing side fixes the unit.**

### 3.4 Stratum 4 — the DEFERRED entries of the decisions register — **CENSUS, `N = 21`**

**Defining object: a register field** — the STATUS cell of the INDEX `DECISIONS.md`, whose own
vocabulary table states at line 175: `| **DEFERRED** | Decided to be built later. The decision itself
stands. |`, and whose banner (lines 90–93) declares it **GENERATED** from
`tools/audit/decisions/backbone_decisions.json`. Membership is the rows whose status cell **opens**
`DEFERRED`, which under the register's rule (f) is what carries a row's state; `⚠LEGACY` is a
separate flag and does not change the status. **`N = 21`.** `N ≤ T`, so census; `k` does not apply
and no uncertainty range is needed.

**★ One thing established rather than assumed, because it would otherwise silently change `N`.** The
source `backbone_decisions.json` carries **51** records with `"status": "deferred"`. Thirty of them
sit in the file's **retired / soft-discarded** array rather than its `decisions` array and the
register does not render them — they were retired from it on 2026-08-17 under Rulings 1 and 3 of
`cowork_rulings_2026_08_17_residue_sitting.md`. **The register's DEFERRED entries are the 21 the
register carries.** Both numbers are in the sealed file so that a successor meeting 51 elsewhere does
not read the census as short.

### 3.5 Stratum 5 — the evidence inventory — **TAKE, `N = 33`, `k = 1`**

**Defining object: `cowork_evidence_inventory.md`**, one file, a member of the specification document
set by an ADMITTED delegation `ARCHITECTURE.md` writes to it — the grade's ground is at
`tools/audit/gen_specification_document_set.py:280-287`: *"A subject-is-X naming with a delegating
predicate — 'The catalog of what each layer discovers is X' … and it binds an obligation to the
document."*

**★ THE UNIT IS A DECLARED READING AND IT CHANGES BOTH `N` AND THE DRAW.** The dispatch's unit is
*"one inventory row"*. **The document contains no table and therefore no rows** — a search for
`^\s*\|` returns **zero** matches. Its records are markdown list items. The reading taken is **every
markdown list item at any nesting depth, `N = 33`**, because it is the only reading that adds no
judgement of mine: 24 items sit at the top level, 9 are nested one level, and excluding the nested
ones — or excluding the two top-level items that are bare labels introducing nested ones
(`cowork_evidence_inventory.md:100` and `:123`) — would each be a decision about which items count.
**Under the alternative reading `N = 24 ≤ T`, the stratum would be a CENSUS of 24, and the drawn set
would be different.** Declared, not concealed; it is the writing side's to fix.

### 3.6 Stratum 6 — the declared dormancies — **STOPPED: no defining artifact; three readings disagree**

**The concept is defined and the population is not.** `CLAUDE.md:251-255`, the fact-publication
corollary ratified 2026-07-10: *"A fact consumed by no one is either **declared dormancy** (its
future consumer named) or **waste** (removed)."*

**No generated artifact enumerates them.** A search of the whole `.json` population for the stem
`dormanc` returns 36 files; every one is register data, a per-layer audit disposition set, a guard
classification or a screen. **None is an enumeration of the declared dormancies, and no generator
writes one.**

**Three candidate readings, disagreeing about the subject as well as the extent.** (i) The evidence
inventory's own status vocabulary (*"DORMANT (built, gated off)"*, banner lines 10–13) together with
its §8b `Declared future consumers, named by the user (2026-07-13)` — the corollary's *future
consumer named* half; a set of rows in one document. (ii) The free-text declarations scattered across
the record — `ARCHITECTURE.md:31` (*"…as declared dormancy — consumer: the notation record build…"*)
and `:87`, and recurrences across dispatches, CC reports and per-layer audit dispositions, with **no
marker convention to find them by**. (iii) The specification document set's per-member
`live_or_dormant` property — a **different subject**, a document's dormancy rather than a published
fact's, named so it can be ruled out explicitly rather than found and used by a successor.

**What is missing:** an object, or a ruling, saying what the declared dormancies are. Note the shape
of reading (ii): if it governs, the stratum cannot be enumerated at all until a marker convention is
built, which is work rather than a ruling.

### 3.7 Stratum 7 — every current document heading — **TAKE, `N = 730`, `k = 29`**

**Defining object: `tools/audit/specification_document_set.json`**, the derived membership of THE
DOCUMENT SET, written by `tools/audit/gen_specification_document_set.py`. The stratum's wording is the
successor plan §6.2 (`cowork_specification_reconstruction_plan_successor_2026_08_21.md:323-327`):
*"They are demoted to a TEST POPULATION for the placement test below — every current heading and every
heading ever deleted from the document set is a statement to be placed."* The document set is the
plan's §5, and the tool states at lines 7–12 that it exists to derive exactly that: *"The ruling fixes
the answer in three limbs: `ARCHITECTURE.md` itself …; every document `ARCHITECTURE.md` delegates to
in a form the delegation-form rule admits; and `docs/scoring_model.md`."*

**The artifact is current at the seal:** `--check` re-derives — *"targets named 68; namings 199;
admitted 25; members 26; with no file 0; seed misses 5 of 25."* **26 members.** `STATUS.md` is graded
ADMITTED and then excluded from the member list by the authored exclusion the user ruled 2026-08-22
(Ruling 1(a) of `cowork_rulings_2026_08_22_step_zero_return_sitting.md`), so it is not in the
stratum.

**Two readings declared, each moving `N`.**

- **Whole file, not the delegated sections.** Several members carry `delegation_scope: sections`;
  `ARCHITECTURE.md` itself is scoped to three named regions. The reading taken is **every heading in
  the member FILE**, because the dispatch's unit is *"one markdown heading in a current member of the
  document set"* and the artifact's member field is the file path, while the scope field governs how
  far a delegation REACHES. Under the narrow reading `ARCHITECTURE.md` contributes only three
  regions' headings and `N` falls sharply.
- **Fenced code blocks are excluded.** A bare `^#{1,6} ` match also catches `#` comments inside
  fenced code blocks. **Fence-aware `N = 730`; naive `N = 737`.** The seven excluded lines are all
  shell comments in `ARCHITECTURE.md` (lines 896–907 and 7794–7797). **The naive reading would have
  put two of those shell comments into the drawn sample**, at ordered positions 30 and 262 — which is
  why the exclusion is taken, and why it is declared rather than left silent.

**Established on both sides.** The heading population was extracted from the content-addressed git
objects at the tip and independently counted in the WORKING TREE with the file tools; the two agree
**per file and in total at 737 naive**, so the working tree and the tip carry the same headings for
all 26 members. Every one of the 25 drawn items was then re-read from the working tree with the file
tool at its own line and matched verbatim.

### 3.8 Stratum 8 — every heading ever deleted from the document set — **TAKE, `N = 59`, `k = 2`**

**Defining object: the same 26-member document set, plus the repository's history walked from the
explicit tip hash.** Ruling 1 of `cowork_rulings_2026_08_26_framework_opening_sitting.md` is why this
side enumerates it: *"the deleted half requires the repository's history."*

**How.** For each member, every commit that changed it was listed from the explicit tip —
**279 commits across the 26 members** — and every one of those versions was read from its
content-addressed git object. Walking newest to oldest, a heading present in a version, absent from
its successor and absent at the tip is a deleted heading; its recorded line is its line in the last
version that carried it, and its deleting commit is the version in which it first does not appear.
**`N = 59`**, fence-aware on the same rule as §3.7 (naive 60; the extra is `# Full corpus` at
`ARCHITECTURE.md:2523` in a historical version, a shell comment inside a fence).

**Two readings declared.** *"Absent at the tip"* is read **per member** — the unit's own wording is
*"present in an earlier commit of a document-set member"* — so a heading that moved between members
counts as deleted from the first. And a heading deleted, reintroduced and deleted again is carried
**once**, at its latest presence.

---

## 4. ★ A PROPERTY OF THE DECLARED SELECTION RULE THAT ITS WORDING DOES NOT SHOW

Reported because it decides what two of the four drawn strata contain, and the writing side authored
the rule without the counts.

For any stratum with `T < N < 2T` — that is `26 ≤ N ≤ 49` — `k = floor(N/T) = 1`, and the take
`1, 1+k, …, 1+24k` **degenerates to positions 1 … 25: the first twenty-five items of the ordering,
contiguously, and nothing after them.** It is not a spread.

- **Stratum 5** (`N = 33`, `k = 1`): items 26–33 cannot be drawn. The evidence inventory's Layer-5
  section contributes nothing, and most of its Layer-4 section contributes nothing.
- **Stratum 8** (`N = 59`, `k = 2`): positions 51–59 of the ordering cannot be drawn.

The rule was applied exactly as written and **nothing was adjusted to soften it.**

---

## 5. TASK 4 — THE ROOT-POPULATION HAZARD

### 5.1 The prediction, made from the guard's own derivation BEFORE either file was written

`tools/audit/gen_filing_convention_application.py` derives its candidate population over
`SURFACE_GLOBS` — which begins `"*.md"`, the repository root's own documents — by two signatures
(lines 81–97 and 275–302):

- **S1**, the closing-line fate signature: within the document's **last 25 non-blank lines**, a line
  matching **both** `S1_FATE` — `resolved in|deleted|removed|retired|superseded|falsified|no longer
  exists|no longer present` — **and** `S1_MARKER`, which is a line opening `status` **or containing a
  7-to-40-character hex run**, i.e. a commit hash.
- **S2**, the banner-over-a-falsified-subject signature: a status word in the first 20 non-blank
  lines **AND** a decisions-register entry with a falsified / shelved / superseded status whose own
  record names the document.

**Predicted before writing:** **S2 cannot fire on either new file** — no register entry can name a
file that did not exist when the register was written. **S1 will fire on
`cowork_placement_sample_sealed_2026_08_27.md`**, near-certainly and by construction: its tail is the
stratum-8 list, every row of which carries the word **deleted** beside a **40-character commit
hash**. S1 was judged **likely** to fire on this report for the same reason. **Both would therefore
enter the candidate population, and because no verdict is authored for them, each would become a new
member of the STOP list behind the standing DECISION red `[[OI-372]]`.**

**Before writing, the derived population was 17 candidates and the STOP list was exactly three** —
`BUILD_AND_TEST_ARCHIVE.md`, `OPEN_ITEMS_ARCHIVE.md`, `cc_report_preparation_fourteenth.md`.

### 5.2 The measurement, with both files on disk

**THE LIST WIDENED. It is reported and NOT cured.**

`tools/audit/gen_filing_convention_application.py --check`, run inside the sweep, now stops with:

> `STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md,
> OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md,
> cowork_placement_sample_sealed_2026_08_27.md. An unclassified candidate is a STOP, never a silent
> pass (D-661).`

The measured final candidate list and STOP list are at §5.4 below, taken after this report reached
its final text.

**Nothing was classified, nothing was cured, and the guard was NOT regenerated.**
`tools/audit/filing_convention_application.json` is untouched.

### 5.3 ★ NEITHER FILE WAS SHAPED TO STAY OUT OF THE POPULATION, AND THAT IS THE POINT

The dispatch's Task 4 says so in terms, and names the reason: a previous report's absence from the
candidate list **was engineered** by keeping commit hashes out of its tail, which silently voided
every *"the list did not widen"* result taken from it. **Both files here were written as their
content required.** The sealed sample's tail is its stratum-8 list because that is what the ordering
puts last; this report names commit hashes wherever it establishes something at an object. **The
guard was allowed to say what it says.**

### 5.4 A finding about the guard's reach, reported and acted on by nothing

S1 is a **fate** signature: it exists to catch a document whose closing line declares that *its own
subject* was deleted, retired or superseded. It cannot distinguish that from a document that
**enumerates deletions in another document** — which is exactly what stratum 8 is. The sealed sample
is not a document whose subject has been overtaken; it is a list of headings that were removed from
`ARCHITECTURE.md` and others, each cited to the commit that removed it, and the signature reads the
two the same way. **The signature is NOT re-tuned here** — the tool's own record already carries the
same shape of finding about itself (lines 235–236: *"the signature encodes a wrong premise … It is
REPORTED and the signature is NOT re-tuned here"*), and re-tuning a guard to exclude the batch that
tripped it is what DT-2 forbids.

---

## 6. TASK 5 — THE STATUS ENTRY, THE FORWARD BOUND, THE SWEEP

### 6.1 `STATUS.md`

**Exactly ONE POINTER entry** (OI-222 remedy; **D-431** — no count, no identity, no rendered value),
**written BEFORE the forward-bound tool ran**, as ordered — the reverse order makes the tool's
occurrence test find zero and STOP, because the then-previous entry only loses its `Last updated: `
prefix when a newer entry takes it.

**★ ONE THING THE SELF-CHECK CAUGHT AND CORRECTED, DECLARED RATHER THAN LEFT.** A second dated entry
had been written beside it, for Task 0(c)'s landing, in the record's own `Same dispatch` form — a
common shape in this file's history, and one the forward-bound tool's own derivation expects to
find. **§6's fence permits `STATUS.md` "one pointer entry", and nothing in the dispatch required the
second.** It was removed on the self-check rather than declared as an extension, because unlike a
declared extension it was not forced by anything: the single entry already points at this report,
which is where the landing's establishment is written. The removal changed `STATUS.md`'s size, so the
staleness cure of §6.3 and the sweep were re-run after it.

### 6.2 The forward bound

`tools/audit/gen_status_batch_bound.py` re-aimed at its **five** aiming constants, and the outgoing
aiming **APPENDED** to `PREVIOUS_AIMINGS` rather than overwriting it (#12). Both edits are inside the
carve-out ruled for this tool by name (Ruling 5 of
`cowork_rulings_2026_08_26_amendment_landing_sitting.md`).

| Constant | Outgoing | Incoming |
|---|---|---|
| `BASE_COMMIT` | `550ffc28cd80b52aa8d0e6f8a88925b8b3cf2de0` | `9053861b9cc71d8de8dc9c12105abd553620b55a` |
| `PREVIOUS_BATCH_DISPATCH` | `cc_instruction_ledger_build.md` | `cc_instruction_ledger_admissions.md` |
| `ACT_DATE` | `2026-08-26` | `2026-08-27` |
| `DISPATCH` | `cc_instruction_ledger_admissions.md` | `cc_instruction_placement_sample.md` |
| `TASK` | `Task 5` | `Task 5` |

Appended row: `{"executing_act": "cc_instruction_ledger_admissions.md, Task 5", "base_commit":
"550ffc28cd80b52aa8d0e6f8a88925b8b3cf2de0", "the_then_previous_batch":
"cc_instruction_ledger_build.md"}`.

**`TASK` is a CHOICE and is declared as one.** The value is `"Task 5"` because the dispatch's own
Task 5 is what orders the `STATUS.md` entry and this tool's re-aiming, in that order and in one act —
which is what the constant is for: it is rendered into the archive header so a later reader can find
the instruction that performed the move. `BASE_COMMIT` is likewise the dispatch's own Task 0(c)
commit, which is the last task commit pushed before this close began, exactly as the constant's own
comment specifies.

**Exact command line:** `python tools/audit/gen_status_batch_bound.py --apply` — read from the tool's
own `argparse` group, which accepts `--apply` and `--check` and nothing else.

**Result:** *"entries moved: 1, 3,741 characters; byte-present in the archive exactly once: True;
absent from the must-read: True."* It wrote `STATUS.md`, `STATUS_ARCHIVE.md` and
`tools/audit/status_batch_bound.json` as its own outputs.

### 6.3 The sweep

`gen_guard_state.py`, then `gen_guard_classification.py`, in that order, iterated to a fixpoint. The
measured final state is at §8.

**Three reds are the standing DECISION reds the dispatch names and forbids curing**, and none was
touched: `gen_filing_convention_application.py --check` (the `[[OI-372]]` guard),
`decisions/apply_soft_discard.py --check`, `decisions/apply_residue_discard.py --check`.

**One staleness red was cured and is declared:** `gen_session_start_read_size.py --check`, stale by
construction because this batch writes to `STATUS.md`, a member of the session-start read. That is
the standing sweep rule's own case.

**No red required the "if you cannot tell, treat it as a DECISION red and STOP" fallback.** Every
failing guard was identifiable from its own captured output.

---

## 7. DEPARTURES, DECLARED READINGS, AND ONE PROCEDURAL SLIP

### 7.1 Instructions I could not obey — none, and the four STOPs are obedience rather than failure

**There is no instruction in this dispatch I could not obey.** The four stopped strata are the
dispatch's Task 1 STOP condition doing what it was written to do: *"do not invent a definition and do
not pick between them."* Each was carried on the merits and none was reached by shortage of effort —
in each case the candidate objects were read at their own source and quoted.

**I did not widen the fence and I did not substitute a weaker form of any instruction.** No write
occurred outside §6's list.

### 7.2 Declared readings — where the rule did not decide and I did not STOP

Three places where the declared **unit** admitted more than one mechanical reading. In each, the
reading that adds **no judgement of mine** was taken and the alternative is named with what it
changes. These are reported as questions for the writing side, not as stops, because in each case the
stratum's **membership** — which is what the Task 1 STOP condition names — is determinable from a
named object; it is the unit's rendering that is open.

1. **Stratum 5's "row"** — every markdown list item (33) versus top-level items only (24), which
   would flip the stratum from a take to a census. §3.5.
2. **Strata 7 and 8's "member"** — the whole member file versus only its delegated sections. §3.7.
3. **Strata 7 and 8's "markdown heading"** — fence-aware (730 / 59) versus naive (737 / 60). §3.7.

**If the writing side disagrees with any of the three, the affected stratum must be redrawn**, and
the sealed file names each reading at the stratum it governs so that a redraw is one instruction
rather than a re-derivation.

### 7.3 One step taken that the dispatch did not order, declared

`python tools/audit/gen_specification_document_set.py --check` was run — read-only, **writes
nothing** — to establish that the artifact stratum 7 and 8 rest on is current at HEAD rather than a
stale committed snapshot. Task 1 requires each stratum's object to be established at the objects, and
a membership artifact that has drifted is not established (#19). It re-derives.

### 7.4 One wording substitution against the dispatch's own text, declared

The dispatch states the Task 2.1 STOP condition as *"If two items tie on all three keys"*. **Both
files written here express that condition without the word "tie"**, because `CLAUDE.md`'s
reserved-word convention reserves the bare word for the notated tie and requires that no NEW
collision be introduced in anything written for the user. The condition itself is untouched and each
file says at the point of use that the substitution is a wording choice. The dispatch's own text is
not edited.

### 7.5 One procedural slip, declared

`python tools/audit/gen_guard_state.py --help` was issued to read the tool's usage. **Its `main`
takes `sys.argv[1:]` and tests only for `--check`, so the flag is inert and the tool ran the whole
sweep in write mode instead of printing usage.** It was harmless — the sweep is this batch's own
ordered act at Task 5(c), and it ran again afterwards to a fixpoint — but it is **the same slip the
previous batch declared for the same class of tool**, and repeating it after it was recorded is worth
saying rather than passing over.

### 7.6 Method — what was read how, since the file-tools rule (D-253) binds every read here

- **The branch tip** was read at `.git/refs/heads/master` **with the file tool**, per Task 0(a).
- **Every working-tree read** — every count, every quotation, every line — went through the file
  tools (Read / Grep / Glob). No shell text utility was aimed at a repository path; the guard denied
  the two attempts that were, and both were re-done with the file tools.
- **The repository's history** was reached only through **content-addressed git object queries**:
  `git rev-list <explicit tip hash> -- <path>` to enumerate the commits that changed each member, and
  `git cat-file -p <commit>:<path>` to read each historical version. **No branch-tip or index read is
  trusted for what is current** — every walk starts from the tip hash the dispatch names, which was
  read at the ref with the file tool.
- **Historical blob content** was written to the session scratchpad and processed there, outside the
  repository. That content came from content-addressed objects, which are self-verifying; **no
  working-tree file was read by a shell utility or by interpreter code.**
- **The cross-check that makes the git-object route trustworthy for stratum 7** is in §3.7: the
  working-tree heading count taken with the file tools agrees with the git-object extraction **per
  file and in total**, and all 25 drawn items were re-read individually from the working tree.

---

## 8. THE CLOSE — EVERY PATH WRITTEN, AND THE MEASURED END STATE

### 8.1 Paths written by this batch

**Authored (inside the fence):**

| Path | What |
|---|---|
| `cowork_placement_sample_sealed_2026_08_27.md` | new — the sealed sample |
| `cc_report_placement_sample.md` | new — this report |
| `STATUS.md` | the POINTER entry plus the Task 0(c) `Same dispatch` entry |
| `tools/audit/gen_status_batch_bound.py` | the five aiming constants and the appended row — the named carve-out |

**Written by a tool this dispatch ordered run, named as §6's fence requires:**

| Path | Written by |
|---|---|
| `tools/audit/evidence_pin_membership.json` | `gen_evidence_pin_membership.py` (Task 0(c)) |
| `tools/audit/status_batch_bound.json` | `gen_status_batch_bound.py --apply` (Task 5(b)) |
| `STATUS_ARCHIVE.md` | `gen_status_batch_bound.py --apply` — the move's destination |
| `tools/audit/guard_state.json` | `gen_guard_state.py` (Task 5(c)) |
| `tools/audit/guard_classification.json` | `gen_guard_classification.py` (Task 5(c)) |
| `tools/audit/session_start_read_size.json` | `gen_session_start_read_size.py` — the declared staleness cure |

**Committed at Task 0(c), before any of the above:** the seven landings of §2.4.

### 8.2 What did NOT happen

**NO ratification. NO register entry** — this batch performs none, so the decisions register's rule
(c) is not engaged and the two mutually unsatisfiable discard-act checks stay out of its path. **This
is the fifth consecutive batch shaped that way**; the dispatch records it in its own fence, and it is
recorded here rather than hidden. Curing the blocker is a decision act that has never been put to the
user, and nothing here proposes it.

**No frame text authored. No part of the frame written. No statement placed. No judgement about
placeability recorded.** The placement test is a later dispatch and this one had no frame to run it
against.

No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md` edit. No `src/` change. No test changed, moved or
run. No golden. Nothing under `tools/corpus/` or `tools/robust_stop/`. No open-items row created,
flipped or discarded. No finding number allocated. **No existing ruling record, surface, dossier,
register entry or inventory row edited** — they were read, not maintained. Neither blind output
opened; neither brief, neither pack, the generator, the manifest and every withheld family untouched.
No score opened. **Exactly one path under `tools/` ending `.py` is modified**, under the carve-out
ruled for it by name. No item was added to, removed from or reordered in the sample except by the
rule at Task 2.

### 8.3 The measured end state

**The sweep, at its fixpoint** (`gen_guard_state.py`, then `gen_guard_classification.py`, in that
order): **75 guards run, 72 passing, THREE failing, 4 not run, 16 historical records**;
classification **live 69 · point-in-time 16 · neither 2 · live-and-failing 3**. It reached the
fixpoint in **two rounds**; it was then run twice more in `--check` form — once after this report's
figures were written in and once after the self-check's wording corrections — both returning *"the
guard state re-derives"* with *"the guard classification re-derives"* beside it; and it was run a
final time in write form after the self-check removed the second `STATUS.md` entry (§6.1), returning
the same 75 / 72 / 3 / 4 / 16 and the same classification. **Five rounds in all, the last three
confirming.**

The three reds are exactly the standing DECISION reds the dispatch names and forbids curing —
`gen_filing_convention_application.py --check`, `decisions/apply_soft_discard.py --check`,
`decisions/apply_residue_discard.py --check`. The first round of the sweep had **four**, the fourth
being the declared staleness red `gen_session_start_read_size.py --check`; it was classified at its
own captured text **before** anything was touched, then cured by regenerating it (its own re-run
reports the session-start read at the tree, `STATUS.md` having changed under it), and the second
round returned to three. **`tools/audit/guard_classification.json` re-derived byte-identically and is
therefore not among this batch's modified paths.**

**The filing-convention population, measured with both new files on disk:** **18 derived candidates,
up from 17**, and the STOP list is **four**, up from three — `BUILD_AND_TEST_ARCHIVE.md`,
`OPEN_ITEMS_ARCHIVE.md`, `cc_report_preparation_fourteenth.md`, and
**`cowork_placement_sample_sealed_2026_08_27.md`**, which entered on S1 with six matching tail lines.
**This report did NOT enter**: its own last twenty-five non-blank lines carry no line matching both
signature halves. The prediction of §5.1 is therefore confirmed for the sealed sample and was
over-cautious for the report. **Nothing was classified, nothing cured, and
`tools/audit/filing_convention_application.json` was NOT regenerated.**

**The tree arithmetic, measured by `tools/audit/changed_paths.py` and not by `git status`, and it
closes.**

| | Start | Close |
|---|---|---|
| changed-path records | 839 | 841 |
| untracked | 838 | 834 |
| tracked modifications | 1 | 7 |

The close arithmetic: the Task 0(c) commit took six previously-untracked files and the one
tracked-modified file into the tree (838 − 6 = 832 untracked, 0 tracked modifications); this batch
then authored two new root-level files (832 + 2 = 834) and left seven tracked modifications.
834 + 7 = 841. **Every one of the seven is inside §6's fence**, and each is named at §8.1:
`STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/evidence_pin_membership.json`,
`tools/audit/gen_status_batch_bound.py`, `tools/audit/guard_state.json`,
`tools/audit/session_start_read_size.json`, `tools/audit/status_batch_bound.json`. **Nothing of the
standing untracked population is committed** beyond the seven the dispatch names at Task 0(c).

**The end state is NOT asserted by this report.** These are the values measured immediately before
the closing commit; the commit itself moves the tracked half.

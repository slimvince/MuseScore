# CC REPORT — the ledger-build batch

> **STATUS: COMPLETE. Tasks 0–5 all performed. Two commits.**
>
> CC, 2026-08-26, executing `cc_instruction_ledger_build.md`. Start-state tip
> `673d0eec4e66fc62ceb9eb7d33faf7aef98d4c7f`, read at `.git/refs/heads/master` with the file tool —
> **the ref side**. Task 0(c)'s landing commit is `4bc362c57e300688a28617a764f97f98e9df836e`.
>
> **NOTHING WAS ADMITTED, CHANGED OR REFUSED AS AN ACT.** The thirty-one admissions are the user's.
> What this batch performed is the **re-check at the gate** Ruling 8 requires when the ledger is
> built, and it **REPORTS**. **One admission is refused at that re-check** — it is not in the
> ledger's body, it is not dropped, it is listed in the ledger's banner with its ground, and
> **nothing is proposed about it.**
>
> **FOUR FINDINGS ARE DECLARED TO THE WRITING SIDE** at §7. One of them is a correction of record to
> a dated report, which is not edited.

---

## 0. THE HEADLINE, IN SIX SENTENCES

1. **The empirical findings ledger EXISTS**, at `EMPIRICAL_FINDINGS_LEDGER.md`, in the form Ruling 1
   ruled: one hand-written record whose entries **CITE** the five ruled fields where they already
   stand and restate none of them.
2. **The re-check ran on all thirty-one and REFUSED ONE.** Thirty entries stand in the body; the
   refusal is in the banner under *REFUSED AT RE-CHECK* with its ground.
3. **The third ruled seed was established at the objects and had NOT been mined**, by either harvest;
   it is mined here as a third harvest, and its six candidates are **undispositioned and not in the
   ledger**.
4. **A correction of record is declared**: `cc_report_ledger_harvest.md` §9.1's account of which
   ruled seeds its own dispatch reached is false at the object.
5. **The root population did NOT widen.** Predicted from the guard's own derivation before the
   ledger was written, and measured after: the standing red's candidate list is the same three, no
   fourth.
6. **The sweep reached its fixpoint in two rounds** — 75 run, 72 passing, **THREE** failing, 4 not
   run, 16 historical records — all three the standing decision reds the dispatch names and forbids
   curing.

---

## 1. TASK 0 — START STATE, AND THE ESTABLISHMENT OF THE MODIFIED RULING RECORD

### 1.1 (a) The tip

`.git/refs/heads/master` read with the file tool: **`673d0eec4e66fc62ceb9eb7d33faf7aef98d4c7f`** —
equals the dispatch's stated tip. Proceeded. **The side is the REF side**, not a worktree or blob
measurement.

### 1.2 (b) The changed-path population

`python tools/audit/changed_paths.py` at Task 0(b): **836 changed path record(s) [worktree]** — **one
tracked modification** (`cowork_rulings_2026_08_26_sizing_tests_sitting.md`) and 835 untracked.
`git status` was **not** run (**D-253**).

**Nothing of the standing untracked population is committed.** In particular
`cowork_fact_gate_admissions_2026_08_26.md` — the source of the thirty-one, untracked, and **not**
named as a Task 0(c) landing — **is left uncommitted**, which is reported rather than left to be
noticed: the ledger cites into it for three admitted restatements, so a reader of the committed tree
will find a citation whose target is not yet tracked. **No act is taken on that; it is the writing
side's.**

### 1.3 ★ (c) THE MODIFIED RULING RECORD — ESTABLISHED BEFORE IT WAS COMMITTED, NOT ASSUMED

The dispatch says a §8 *Corrections of record* was added to
`cowork_rulings_2026_08_26_sizing_tests_sitting.md`, **additions only, no sentence above it reworded
and no ruling amended**, and orders that established before committing. **It was, by the two-sided
read the record's own rule prescribes, and the two sides agree exactly.**

| Side | How measured | Result |
|---|---|---|
| **BLOB (at the tip)** | content-addressed read by explicit hash — `git rev-parse` resolved the path to blob `0098082e74230ecb0d6f8b9f5ce09165d5df1b8d`; `git cat-file -s`; `git cat-file blob … \| wc -l`; tail bytes inspected | **11,141 bytes; 168 lines; LF endings; terminating newline present** |
| **WORKTREE** | the file tool, read whole | **275 lines** |

**What differs — ADDITIONS ONLY, and it closes exactly.** Staged, the change is **+107 / −0**, and
107 is exactly the two insertions:

1. **Worktree lines 65–68** — a four-line blockquote at the opening of §3, a forward pointer to the
   new section: *"★ TWO STATEMENTS OF THIS SECTION ARE CORRECTED OF RECORD AT §8 … The text below
   stands unamended — the correction is recorded beside it and never over it (#12)."*
2. **Worktree lines 173–275** — 103 lines: a horizontal rule, `## 8. CORRECTIONS OF RECORD`, its five
   subsections §8.1–§8.5, and a §8 provenance paragraph.

**Every line of the blob stands verbatim in the worktree**, at a four-line offset from blob line 65
onward; blob line 168 is worktree line 172. **No sentence above §8 is reworded, no ruling is amended
and none is voided** — which is what the dispatch's account says and what the read confirms at the
object. Second-level headings move seven → eight; five third-level headings appear where the blob has
none.

**★ ONE CORRECTION OF MY OWN, MADE BEFORE IT MATTERED:** the worktree file is **275** lines, not 276;
the miscount surfaced against the staged `+107` and was resolved at the object (the blob's own
newline count and tail bytes), not by adjusting the arithmetic.

### 1.4 The landing commit, and the evidence-pin regeneration

**Commit `4bc362c57e300688a28617a764f97f98e9df836e`** — three paths, `3 files changed, 384
insertions(+)`: the ruling record `cowork_rulings_2026_08_26_ledger_form_sitting.md` (new), this
dispatch `cc_instruction_ledger_build.md` (new), and the modified
`cowork_rulings_2026_08_26_sizing_tests_sitting.md` (+107/−0).

Then, as ordered: `python tools/audit/gen_evidence_pin_membership.py` — exit 0, wrote
`tools/audit/evidence_pin_membership.json`; 7 generated ratification documents, 71 ruling records
read, 7 members, 5 pinned, **0 UNRESOLVED**.

---

## 2. TASK 1 — THE THIRD RULED SEED

### 2.1 (a) WHAT THE PHRASE DENOTES, ESTABLISHED AT THE OBJECT

**The ruled phrase, quoted from `cowork_rulings_2026_08_15_method_directions.md:53–54`:**

> Existing seeds: `DEFECT_TYPES.md`, `docs/scoring_model.md` §8, the
> refuted-repair register entries.

The restatement at `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md:218` drops
the word *register* — *"the refuted-repair entries"* — so the restatement cannot settle it.

**★ THE REGISTER IS THE DECISIONS REGISTER, AND THE ESTABLISHING TEXT IS `OPEN_ITEMS.md:42`** — row
OI-2, which uses the phrase in this project's own sense:

> **D-490** and **D-491** are the falsification and the refuted repair behind that recommendation,
> **D-493** the un-computable long-run successor.

`D-491` is a **decisions-register** entry whose own title reads *"REFUTED: making the override's
comparison vertically fair does not repair it"* (`decisions/group_H.md:1121`). **The usage pre-dates
the ruling by eleven days**, so it was available to whoever wrote the seed list.

**Two supports beside the quotation, because one quotation is not an establishment:**

- **The unit word.** The decisions register's own rules call its unit an **entry** — `CLAUDE.md`, the
  decisions-register section, rule (c): *"gets its register entry"*. The open-items register's rules
  call its unit a **row** and an **item** — rules (c) and (d): *"an index row"*, *"flips the INDEX
  row"*. The ruled phrase says **entries**.
- **The subject.** The open-items register holds **open issues**. A *refuted-repair row* would have no
  referent there; a refuted-repair **entry** has many in the decisions register.

**The criterion applied, stated once so every verdict is mechanical.** A register entry is a
**refuted-repair entry** when its recorded content is that a **repair** — a proposed or built remedy
for a known defect of the analysis: a guard, a gate, a threshold, a re-ordering, a widening, an
alternative mechanism or an alternative approach — was **tried or analysed and then REFUTED,
FALSIFIED, SHELVED WITH EVIDENCE, REVERTED, measured inert, or recorded as a dead end.** A positive
design choice, a convention, a scope decision or a process rule is not one, however worded.

### 2.2 (b) IT WAS **NOT** MINED — established at the objects, in both harvests

- **`cc_instruction_ledger_harvest.md:223–230`, Task 3, read at the object.** It names **four**
  sources and the decisions register is **not among them**. Its source 2 is *"`OPEN_ITEMS.md` and
  `open_items/` — the register's own recorded empirical findings"*, which is **a different
  register**.
- **`cc_report_ledger_harvest.md:454–459`, §8's source table.** The same four.
- **`cowork_empirical_findings_candidates.md` §11**, the second harvest's sources: `DEFECT_TYPES.md`
  and the coding side's measurement reports. Neither is the decisions register.
- **No candidate C1–C41 carries a `D-…` provenance.** C10 names D-490 and D-491 in its
  *establishment status* field, but its **provenance** is `docs/scoring_model.md:1276–1292` — reached
  through the scoring model, not the register.

**★ FINDING F1 — A CORRECTION OF RECORD IS DECLARED TO THE WRITING SIDE.**
`cc_report_ledger_harvest.md` §9.1 states, of the three ruled seeds: *"Task 3 names the second and the
third and not the first."* **That is FALSE at the object.** Task 3 names the **second only**; that
report read its source 2 — the open-items register — as though it were the ruled third seed. **The
consequence is exactly what this task existed to catch: a ruled seed stood recorded as accounted for
while nothing had ever been mined from it.** **No edit is made to that report** — it is a dated
report, and the correction is declared here and at the candidates file's §13.2.

### 2.3 ★ FINDING F2 — THE THIRD SEED AND THE SECOND OVERLAP HEAVILY, BY CONSTRUCTION

Enumerating the population and splitting it **by HOME** produced a finding nobody had recorded:
**fourteen of the refuted-repair entries are homed INSIDE `docs/scoring_model.md` §8** — the second
ruled seed, which the first harvest read **whole** at `:1129–1457`.

| Entry | Home | Already reached as |
|---|---|---|
| D-215 | `:1137` | — |
| D-299 | `:1413–1417` | — |
| D-300 | `:1418–1424` | **C9** |
| D-301 | `:1425–1430` | **C8** |
| D-302 | `:1431–1439` | **C5**, **C7** |
| D-317 | `:1375–1381` | — |
| D-318 | `:1382–1385` | — |
| D-319 | `:1386–1392` | **C4** |
| D-320 | `:1393–1399` | **C1** |
| D-328 | `:1207–1216` | — |
| D-490 | `:1276–1284` | **C10** |
| D-491 | `:1285–1292` | **C10** |
| D-492 | `:1302–1312` | **C10** |
| D-493 | `:1293–1301` | **C10** |

**The overlap is not an accident.** The user's homing ruling of 2026-08-07 routed the chord- and
function-layer refuted-repair family into `docs/scoring_model.md` §8 under the scoring-surface rule —
each entry's provenance records it. **So the ruled three-seed list double-counts a large part of its
own third member through its second**, and the seed's genuinely unreached membership is the part
homed elsewhere.

### 2.4 (c) THE THIRD HARVEST — SIX CANDIDATES, C42–C47, APPENDED AND UNDISPOSITIONED

Written as **Part Three (§§13–17)** of `cowork_empirical_findings_candidates.md`, **append only**,
numbered from the highest existing identifier + 1. **No existing candidate was edited, renumbered or
re-verdicted; neither existing summary table was touched; the file was not retired, pruned,
superseded or re-bannered.**

| # | Candidate | Source entry | Verdict proposed |
|---|---|---|---|
| C42 | A diatonic leading tone does not discriminate a real modulation from a passing one | **D-290** | **PASSES on the leading-tone half** |
| C43 | One settled indication does not fix the key at a selection edge; a confident earlier key over a RUN does | **D-622** | **PASSES** · #6 reservation on the rule half |
| C44 | Re-ranking already-committed carried lists adds nothing | **D-026** | **PASSES as a design-class antipattern**, at the user's own scoping width |
| C45 | Widening a search cannot reach a modelling error | **D-288** | **UNDECIDABLE** · leans PROCESS |
| C46 | The rejected joint factoring is the production shape | **D-376** | **UNDECIDABLE** · leans PROCESS · #6 reservation |
| C47 | The correct key never sits below the top carried rank | **D-287** | **FAILS** |

**Eight further entries were considered and NOT proposed**, each with its reason at §15 of that file:
D-608 (corroborates C22 at a named instance), D-278 (its content is C11's), D-609, D-403, the four
superseded meta-findings D-282/283/284/285, D-286, D-531, D-098.

**★ THE DECLARED DEPARTURE — THE §8-HOMED MEMBERS WERE NOT RE-HARVESTED.** The dispatch says *"mine
it now"*. **The fourteen entries of §2.3 were deliberately left unmined**, and the ground is Ruling 1
itself: the first harvest read `docs/scoring_model.md` §8 **whole** at the object, so re-harvesting
them would produce a second set of candidates for facts already carried — **the second copy the whole
ledger form exists to prevent.** The seed was mined; what was mined is its part that no source had
reached. **Declared here rather than made silently**, and the precedent is the preceding batch's
declared departure under the same ruling.

**The coverage bound, stated rather than left to be found (#19).** The population was reached by
**pattern over the `### D-…` headings** of the twenty group files, with the signature set listed at
§13.4 of the candidates file. **The 477 entries were NOT all read.** An entry whose heading carries
none of those words would have been missed. **The harvest is not claimed complete over the third
seed.**

---

## 3. TASK 2 — THE RE-CHECK AT THE GATE, ALL THIRTY-ONE, ONE BY ONE

**The gate, in its ruled words:** *does the fact survive the implementation being thrown away?* —
plus the separately judged requirement that the entry be **approach-level**. **The gate is not a
correctness test**: correctness travels in two of the five fields.

**Source of the admissions:** `cowork_fact_gate_admissions_2026_08_26.md`. Where an admission was made
on a **restated** text or a **named half**, the re-check was applied to **that** text, not to the
source's own sentence.

### 3.1 THE THIRTY THAT PASS

| # | Gate verdict | Ground, in one sentence |
|---|---|---|
| **C1** | PASSES | A claim about what the published human annotation of this repertoire does; nothing in it depends on any reader of the music. |
| **C2** | PASSES | It states what information is and is not present at a moment of the music; the two failed discriminators are its establishment, not its subject. |
| **C4** | PASSES (music half) | The duration profile of an arpeggio is a property of the music, and *a duration-weighted aggregate* names a method class, not our code. |
| **C5** | PASSES | The load-bearing half is a corpus statistic about the annotated music; the population half is defined by a method class (*a vertical reading*) and not by our code. |
| **C6** | PASSES | A statement about pitch-class content, true of the material being read whatever reads it — and the restriction *of that content* is load-bearing. |
| **C7** | PASSES | A claim about what two ways of reading a sonority are; the #6 question against its homed sibling **D-604** is carried beside it, never converted into a refusal. |
| **C8** | PASSES | The admitted restatement is checkable at the notes alone; what was stripped is the source's word *scores*, which is our scorer's. |
| **C11** | PASSES | The admitted restatement is music theory and needs no implementation to be true. |
| **C12** | PASSES | The source itself labels it a musical fact, and it is one. |
| **C13** | PASSES | A fact about held corpora and about repertoire; it bounds what any figure fitted here can claim (#24). |
| **C14** | PASSES | A notation-practice fact about how the repertoire is written down, with its detecting signal itself musical. |
| **C15** | PASSES | A fact about two published corpora, true of whatever reads them. |
| **C16** | PASSES | A fact about how the ground truth is held; the *analyst variants* clause bears directly on #21. |
| **C21** | PASSES | The load-bearing half is a fact about the repertoire — this music does not present some configurations mechanisms are written for — visible only by counting on the actual music. |
| **C22** | PASSES | A property of a designed mechanism meeting a real repertoire; a guard's pass rate is a separate measured quantity from its body's correctness. |
| **C26** | PASSES | It says non-chord tones in this repertoire are not systematically shorter than chord tones, which is about the music. |
| **C27** | PASSES (fact half) | Where the discriminating information lives — in the boundary placement — is a claim about the evidence, not about our pipeline. |
| **C28** | PASSES | Bass-equals-root and root-correctness are properties of any chord reading against any annotation, and the entry computed both on the same cases. |
| **C29** | PASSES | Correct harmonic readings routinely change root from stretch to stretch, so root persistence is not evidence of correctness — a musical claim. |
| **C30** | PASSES | The classification is a property of the edit and correctness a property of the music; nothing links them, and the population bound sits in the uncertainty field. |
| **C31** | PASSES (half b), wording flagged | The fact is a property of the pairing between an analysis and an annotation on this repertoire and is checkable at the sounding weights; **the admitted transcription writes the second mechanism as *"our root"*, and that pronoun is carried rather than altered** — altering an admitted text is not this batch's act. |
| **C32** | PASSES (conflict) | Each repertoire's correct behaviour is the other's error: a fact about two repertoires. |
| **C33** | PASSES | The musical half is that the hard cases here are sparse sonorities. |
| **C34** | PASSES | The annotation is functional and the evidence at that instant is acoustic; the two need not coincide — about the ground truth (#21) and the music. |
| **C35** | PASSES | A property of the interval content, not a shortcoming of any reader. |
| **C36** | PASSES | A tonic prolongation is evidence-poor for its own tonic on characteristic and leading tones — about the music, constraining any model of that family. |
| **C37** | PASSES | A fixed metric window crosses harmonic boundaries because the music's organization does not use that unit. |
| **C38** | PASSES | The ruled shape exactly — tried, measured worse, diagnosed — and the identifying information is not vertical information at all. |
| **C39** | PASSES | The difficulty is asymmetric between the two scale relations, which is about the repertoire's own behaviour. |
| **C41** | PASSES | Harmonic syntax: a root that belongs continues or resolves, so the separating evidence arrives after the moment of the error. |

**Every bound and every not-admitted half travels into the ledger with its entry** — C4's, C11's,
C14's, C27's, C31's, C32's, C37's, C38's two, C39's two, C41's — and none is netted away.

### 3.2 ★ THE ONE REFUSAL — C9

**The admitted text, verbatim** (`cowork_fact_gate_admissions_2026_08_26.md:120`):

> *The presence of a leading tone does not distinguish the genuine cases.*

**REFUSED.** **The admitted sentence's SUBJECT is a population defined by a mechanism of the
implementation.** *"The genuine cases"* denotes the correct fires of the minor-read-as-diminished
gate — register entry **D-300**, homed `docs/scoring_model.md:1418–1424`, whose own source phrase is
*"a genuine minor-read-as-diminished case … a wrong firing"*. **Throw the implementation away and the
sentence has no population**, so the fact does not survive **in the form admitted**.

**Why this is a real gate failure and not pedantry.** Round three's own stated line is sound —
*"stripping is a translation"* — and on C8 and C11 the translation produced full, self-standing music
sentences. **On C9 the translation was incomplete**: our vocabulary was removed from the predicate
(*"available at analysis time"*) and left in the subject, where it is **invisible**, which is worse
than an explicit implementation word because nothing in the sentence flags it.

**What this refusal is NOT.** It is not a judgment on whatever music claim may sit under the sentence.
It is not a proposal, not a correction and not a resolution. **No restatement is offered**, and none
should be read into the ground above. **The admission is the user's; the re-check is Ruling 8's;
reconciling the two is the user's act and not this batch's.**

### 3.3 THE RE-CHECK DID REFUSE SOMETHING, AND THAT IS SAID IN TERMS

The dispatch asks that a re-check refusing nothing be visible as such. **It refused one of
thirty-one.** Thirty pass.

---

## 4. TASK 3 — THE LEDGER

**Path: `EMPIRICAL_FINDINGS_LEDGER.md` at the repository root.** New file.

**Its banner carries, as ordered:** that this IS the ledger; the gate in its ruled words (quoted from
the phase-definition surface `:92–94`); the five-field shape and its two attached rules, quoted whole
from `cowork_rulings_2026_08_15_method_directions.md:46–54`; **which of the three ruled seeds are
represented and which is not**; the **REFUSED AT RE-CHECK** list; and that the third harvest's
candidates are **undispositioned and not in the ledger**.

**Its body carries thirty entries**, each with the fact in one sentence, its identifier, its gate
verdict from Task 2 with a one-sentence ground, and **the citation to where its five ruled fields
already stand** — file, section and line span. **It restates no five-field entry.** That is Ruling 1.

**★ THREE ADDITIONS TO THE ORDERED CONTENT, DECLARED SO THEY ARE NOT TAKEN FOR SILENT SCOPE
WIDENING.**

1. **§7 — the ONE POINTER, C17.** The admissions record states in terms *"The ledger carries a
   pointer to its existing home instead"* (the user's word: *"17=pointer"*). That is a **user
   disposition about this ledger's own content**, so omitting it would have dropped a user-ruled
   element. It is marked as the user's routing, **not** an admission, and the re-check took no
   verdict on it — the re-check's subject is the thirty-one.
2. **§8 — what stands outside the ledger, named so silence claims nothing:** the three HELD, the two
   that FAILED, the three proposed for nothing on #6, and the routed-away material. **The
   routed-away material still has nowhere to go**, which is carried into the ledger because a
   reader of the ledger must meet it (see F4 below).
3. **§9 — the three standing coverage bounds**, plus the sizing-tests ruling's coverage bound and
   the larger measured one that dominates it. Without them the ledger's silence would read as
   completeness, which is **DT-26**'s own shape.

**★ THE CONSEQUENCE THE DISPATCH TOLD ME TO REPORT AND NOT ACT ON — F5, below. The candidates file
was NOT retired, pruned, superseded or re-bannered**, and its own banner sentence calling itself *"a
working list superseded by the ledger itself"* stands untouched.

---

## 5. TASK 4 — THE ROOT-POPULATION HAZARD

### 5.1 THE PREDICTION, MADE FROM THE TOOL'S OWN DERIVATION **BEFORE** THE LEDGER WAS WRITTEN

`gen_filing_convention_application.py` derives its population from `SURFACE_GLOBS` — which includes
`*.md` at the repository root — minus `EXCLUDED_NAMES` and `EXCLUDED_DIRS`, and then keeps only files
carrying one of two signatures:

- **S1 — the closing-line fate signature.** Within the last **25 non-blank** lines, a line matching
  **BOTH** `S1_FATE` = `\b(resolved in|deleted|removed|retired|superseded|falsified|no longer
  (exists|present))\b` **and** `S1_MARKER` = `(^\s*>?\s*\*{0,2}status\b|[0-9a-f]{7,40})` — a leading
  status marker, or a 7-to-40-character hexadecimal run.
- **S2 — a banner over a falsified subject.** A status word in the first **20 non-blank** lines
  **AND** the document named in a register entry whose status is falsified, shelved or superseded.

**The prediction, stated before the file existed:**

- **S2 CANNOT fire for a new file.** Its second half requires the register to name the document in a
  superseded-status entry's own record, and **this batch writes no register entry**, so no entry can
  name it.
- **S1 fires only on the ledger's own last 25 non-blank lines**, and on nothing else. It was
  therefore predicted **NOT** to enter, provided the file's own tail carried no line pairing a fate
  word with a hex run — which the project's ordinary convention already secures, because a report's
  or record's provenance hashes go in its **banner**.
- **★ AND IF IT HAD ENTERED, THE EFFECT WOULD HAVE BEEN STRONGER THAN A FOURTH CANDIDATE:** an
  unclassified candidate raises `SystemExit` at **STOP 2** (*"An unclassified candidate is a STOP,
  never a silent pass (D-661)"*), so the guard would have gone from a failing comparison to a crash.

**Declared, because it bears on how the prediction should be read:** the ledger was written in this
project's ordinary form, with its provenance in the banner. **No sentence was contrived to dodge the
signature, and no content was distorted for it.**

### 5.2 THE MEASUREMENT, WITH THE LEDGER ON DISK — **THE LIST DID NOT WIDEN**

The guard's own captured failure text at `tools/audit/guard_state.json`, after the ledger was written:

> `STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md,`
> `OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md. An unclassified candidate is a STOP,`
> `never a silent pass (D-661).`

**The same three, no fourth. `EMPIRICAL_FINDINGS_LEDGER.md` is not among them.**

The **whole** derived candidate population was read read-only through the tool's own `--derive-only`
mode, which writes nothing: **17 candidates**, and the ledger is not one of them. The seventeen are
`BUILD_AND_TEST_ARCHIVE.md`, `OPEN_ITEMS_ARCHIVE.md`, `STATUS_ARCHIVE.md`,
`cc_instruction_phase1s_stale_rules_and_enumeration.md`,
`cc_instruction_phase1z_commit_and_instrument_record.md`,
`cc_key_grading_and_calibration_rebaseline_report.md`, `cc_oi207_residual_pass_report.md`,
`cc_report_preparation_fourteenth.md`, `cc_stage2a_wip_triage_report.md`, `cc_stage3_4i_dossier.md`,
`cc_stage5_phase2_2d_report.md`, `docs/iter92_joint_bass_chord_scoring.md`,
`docs/key_path_design.md`, `docs/policy2_coalescing_map.md`, `docs/stage4b_design.md`,
`docs/symbol_input_audit.md`, and
`ratification_surfaces/cowork_pending_ratifications_next_session.md`.

**`STATUS_ARCHIVE.md` is in that population and was already**, and it carries an authored verdict, so
the forward-bound move's new archive header did not widen the STOP list either. **Nothing was
classified, nothing was cured and the guard was not regenerated.**

---

## 6. TASK 5 — `STATUS.md`, THE FORWARD BOUND, THE SWEEP

### 6.1 (a) The `STATUS.md` entry — a POINTER, written BEFORE the tool

One entry, written **first**, exactly as ordered — the reverse order would have made the forward-bound
tool's occurrence test find zero and STOP, because the tool searches the live file for the previous
entry **without** its `Last updated: ` prefix (the tool's own `PREFIX_ADJUSTMENT`, imported from
`gen_governing_surface_split.py` rather than re-decided).

**It is a POINTER per the OI-222 remedy and carries no count, no identity and no rendered value
(D-431).** The refusal is named as *an admission*, never by identifier; the harvest is named without
a count.

**One further `STATUS.md` change, declared:** the `Last updated: ` prefix moved off the previous
batch's entry onto this one. That is not an edit to the previous entry's content — it is the shift
the tool documents and adjusts for, and without it the move is not byte-faithful.

### 6.2 (b) The forward-bound tool, re-aimed — the exact command line and the values

**Command line, taken from the tool's own argument parser rather than assumed** (`--apply` /
`--check`, mutually exclusive):

```
python tools/audit/gen_status_batch_bound.py --apply
```

**The five aiming constants, before → after:**

| Constant | Outgoing | Set to |
|---|---|---|
| `BASE_COMMIT` | `9683a9c1fe351cde4450bfe63c86d2331a83946b` | **`4bc362c57e300688a28617a764f97f98e9df836e`** |
| `PREVIOUS_BATCH_DISPATCH` | `cc_instruction_boot_pack_regeneration.md` | **`cc_instruction_sizing_tests.md`** |
| `ACT_DATE` | `2026-08-26` | **`2026-08-26`** (unchanged in value; re-stated as one of the five) |
| `DISPATCH` | `cc_instruction_sizing_tests.md` | **`cc_instruction_ledger_build.md`** |
| `TASK` | `Task 7` | **`Task 5`** |

**`TASK` is a choice, and the choice is declared with its ground.** I used **`Task 5`** because that
is the task of this dispatch under which the re-aiming and the move are ordered — §5(b). The field's
only consumer is the archive header's prose, where it tells a later reader which task of which
dispatch performed the move; naming the task that ordered it is what makes that sentence true.

**The outgoing aiming was APPENDED to `PREVIOUS_AIMINGS`, not overwritten (#12)** — one new row:
`{"executing_act": "cc_instruction_sizing_tests.md, Task 7", "base_commit":
"9683a9c1fe351cde4450bfe63c86d2331a83946b", "the_then_previous_batch":
"cc_instruction_boot_pack_regeneration.md"}`. **Both edits are inside the carve-out ruled for this
tool by name**, and `RULINGS` — which names the ruling the tool exists for, not the aiming — was not
touched.

**Result:** exit 0. **1 entry moved, 2,812 characters**; byte-present in the archive exactly once
**True**; absent from the must-read **True**.

### 6.3 (c) The sweep — fixpoint in TWO rounds

Run in the ruled order: `gen_guard_state.py`, then `gen_guard_classification.py`.

| Round | run | passing | failing | not run | historical |
|---|---:|---:|---:|---:|---:|
| 1 | 75 | 71 | **4** | 4 | 16 |
| 2 (fixpoint) | 75 | 72 | **3** | 4 | 16 |
| 3 — re-run with the ledger **and this report** on disk | 75 | 72 | **3** | 4 | 16 |
| 4 — re-run after the self-check's corrections, so the committed state describes the committed tree | 75 | 72 | **3** | 4 | 16 |

**Round 3 is the one that matters for §5.2's claim**: with both new root-level documents on disk the
failing set is the same three, and the filing-convention guard's STOP list is still
`BUILD_AND_TEST_ARCHIVE.md, OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md` — **no
fourth, and neither new document is in it.** The classification was re-run after it, unchanged.

**Every red was classified at its own captured text before anything was touched.**

- **`gen_filing_convention_application.py --check`** — captured text is the STOP quoted at §5.2, the
  standing red behind `[[OI-372]]`. **DECISION red. Not regenerated, not investigated, not cured**;
  its candidate list is unchanged (§5.2).
- **`decisions/apply_soft_discard.py --check`** — the standing decision red the dispatch names and
  forbids curing. **Untouched.**
- **`decisions/apply_residue_discard.py --check`** — the standing decision red the dispatch names and
  forbids curing. **Untouched.**
- **`gen_session_start_read_size.py --check`** — captured text: *"STALE vs the measurement:
  session_start_read_size.json does not re-derive"*. **A STALENESS red, and it is caused by this
  batch's own writes**: `STATUS.md` is a member of the session-start read and this batch writes to
  it. **Cured under the standing sweep rule**, by re-running the tool. It is the only red cured, and
  it is declared rather than absorbed.

**No red of an unknown kind appeared, so the treat-it-as-a-DECISION-red STOP was not reached.**

**`gen_guard_classification.py`:** exit 0 — **live 69 · point-in-time 16 · neither 2 ·
live-and-failing 3**. The three live-and-failing are exactly the three standing decision reds.

---

## 7. THE FINDINGS DECLARED TO THE WRITING SIDE

**F1 — `cc_report_ledger_harvest.md` §9.1 IS FALSE AT THE OBJECT.** Detail at §2.2. Its dispatch's
Task 3 names the **second** ruled seed only; that report read its source 2, the **open-items**
register, as though it were the ruled **third** seed. The dated report is **not** edited.

**F2 — THE RE-CHECK REFUSES C9.** Detail at §3.2. Not a proposal, not a correction, nothing proposed
about it.

**F3 — THE THREE-SEED LIST DOUBLE-COUNTS ITS OWN THIRD MEMBER THROUGH ITS SECOND.** Detail at §2.3.
Fourteen refuted-repair entries are homed inside `docs/scoring_model.md` §8 because the user's homing
ruling of 2026-08-07 put them there; a reader of the ruled seed list has no way to see that from the
list. **No act is proposed.**

**F4 — THE ROUTED-AWAY MATERIAL STILL HAS NOWHERE TO GO, AND THE LEDGER NOW SAYS SO.** Twenty-one
`DEFECT_TYPES.md` rows, C31's half (a) and C40 stand routed to *"the phase definitions' constraints
and stop rules"*, and there is **no artifact that could receive them** — the phase definitions live in
a frozen ratification surface whose §3 is proposal text with no place for a constraint added later.
**DT-20 is live in the present arrangement.** Carried into the ledger's §8 because a reader of the
ledger must meet it; **nothing written anywhere.**

**F5 — THE CANDIDATES FILE'S OWN BANNER CONTRADICTS RULING 1, AND IS UNTOUCHED.**
`cowork_empirical_findings_candidates.md` says of itself that it is *"a working list superseded by the
ledger itself"*. Under the ruled form the ledger **cites into it**, so it is load-bearing. **Reported
and acted on by nothing**, exactly as the dispatch orders. It is recorded at the ledger's §10 and at
the candidates file's §17.

**F6 — A STANDING OBSERVATION, NOT AN ACT.** The preceding batch declared a register entry OWED under
the decisions register's rule (c) and named the blocker. **This batch writes no register entry and
performs no ratification**, so rule (c) is not engaged here and the two mutually unsatisfiable
discard-act checks stayed out of its path — as the dispatch was shaped to ensure. **The owed entry is
neither written nor discharged here, and no identifier was consumed.**

---

## 8. EVERY PATH WRITTEN

**Committed in the Task 0(c) landing commit `4bc362c57e`:**

1. `cowork_rulings_2026_08_26_ledger_form_sitting.md` — new (the record this dispatch executes)
2. `cc_instruction_ledger_build.md` — new (this dispatch)
3. `cowork_rulings_2026_08_26_sizing_tests_sitting.md` — modified, +107/−0, established at §1.3

**Written after it, and in the final commit:**

4. `tools/audit/evidence_pin_membership.json` — output of a tool the dispatch orders (Task 0)
5. `cowork_empirical_findings_candidates.md` — **APPEND ONLY**, Part Three (§§13–17), Task 1(c)
6. `EMPIRICAL_FINDINGS_LEDGER.md` — **new**, the deliverable, Task 3
7. `STATUS.md` — one POINTER entry, plus the `Last updated: ` prefix shift the tool requires
8. `STATUS_ARCHIVE.md` — **written by** `gen_status_batch_bound.py --apply`, its own output
9. `tools/audit/gen_status_batch_bound.py` — the five aiming constants and the appended row, carve-out
10. `tools/audit/status_batch_bound.json` — that tool's own output
11. `tools/audit/session_start_read_size.json` — output of the staleness cure
12. `tools/audit/guard_state.json` — the sweep's own output
13. `tools/audit/guard_classification.json` — the classification's own output
14. `cc_report_ledger_build.md` — **new**, this report

**Exactly one path under `tools/` ending `.py` is modified**, under the carve-out ruled for it by
name. **No other `.py` source was edited.**

---

## 9. DEPARTURES, AND EVERY INSTRUCTION I COULD NOT OBEY

**★ NO INSTRUCTION OF THIS DISPATCH WENT UNOBEYED, and the standing clause's STOP was never
reached** — no instruction required a write outside the fence.

**ONE DECLARED DEPARTURE FROM THE LETTER, with its ground:**

- **The third harvest did not re-harvest the fourteen refuted-repair entries homed inside
  `docs/scoring_model.md` §8** (§2.4). The dispatch says *"mine it now"*; those fourteen were
  deliberately left, because the first harvest read that section **whole** at the object and
  re-harvesting them would produce a second set of candidates for facts already carried — the second
  copy the ledger's ruled form exists to prevent. The seed **was** mined; what was mined is the part
  no source had reached. The population, the split and the reason are all written into the candidates
  file so the departure is inspectable rather than asserted.

**THREE ADDITIONS TO THE ORDERED CONTENT**, declared at §4 rather than made silently: the ledger's
§7 pointer (a user disposition about the ledger's content), §8 (what stands outside), and §9 (the
coverage bounds).

**THREE CORRECTIONS OF MY OWN, declared rather than made silently:**

- **At §1.3** — a line count of the modified ruling record was one too high in my own working notes,
  and was resolved at the object (the blob's own newline count and tail bytes) rather than by
  adjusting the arithmetic to fit.
- **At the ledger's §3, found by the standing self-check re-reading the file against itself** — the
  seed table said *"Eight entries below … come from it"* and then listed C9 among them, which is the
  one entry that is **not** below. Corrected to seven in the body plus the one refused.
- **At the ledger's C36, found by the same self-check against the reserved-word convention** — the
  fact sentence used the verb *to score* bare in its numerical sense. Reworded to *rating* / *rates*,
  which is the same claim without the collision. Inherited idioms already standing in the candidates
  file and in `CLAUDE.md` itself — *no figure is restated*, *no interval given* — were **kept**, on
  the convention's own rule that an existing collision is not renamed unilaterally (`OPEN_ITEMS.md`
  OI-229).

---

## 10. WHAT THIS BATCH DID **NOT** DO

**No admission made, changed or refused as an act** — the Task 2 re-check REPORTS; the refusal is a
verdict recorded in the ledger's banner, not an act on the admissions record, which is untouched.
**No ratification. No register entry**, so the decisions register's same-commit rule is not engaged.
**No open-items row created, flipped or discarded. No finding number allocated.**

**No `CLAUDE.md` edit. No `ARCHITECTURE.md` edit. No `DECISIONS.md` edit.** No `src/` change. **No
test changed, moved or run.** No golden. Nothing under `tools/corpus/` or `tools/robust_stop/`. No
behaviour change to the analysis, and **no measurement of the analysis built, designed, scoped or
run** — every measurement in this batch is textual or over the guard set.

**No derivation and no comparison.** Neither blind derivation output opened. Neither brief, neither
pack, the generator, the manifest and every withheld family untouched.

**No existing candidate edited, renumbered or re-verdicted**, and neither existing summary table
touched. **`cowork_empirical_findings_candidates.md` was not retired, pruned, superseded or
re-bannered.**

**The two discard-act checks were not cured and `[[OI-372]]`'s guard was not regenerated.** Nothing of
the standing untracked population is committed.

**The end state is NOT asserted by this report** — the final sweep and the tree arithmetic at the
close are stated in the commit that carries this file.

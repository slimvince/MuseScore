# BRIEF for the INFORMED deriving session — the FRAMEWORK document

> **STATUS: DRAFT — NOT RULED, NOT DISPATCHED. §7 lists the points the user rules before this brief
> is handed to anyone, and none of them is ruled.** Written by the writing side (Cowork, 2026-08-28)
> at branch tip `bf3249e73d9eb91d0f2513bc2c16aa626b53e464`, read as a file at
> `.git/refs/heads/master`. It dispatches nothing and boots no session.
>
> **★ IT SUPERSEDES `cowork_blind_session_brief_framework.md`, WHICH IS KEPT AND NOT EDITED (#12).**
> That brief was written for an implementation-blind session under the arrangement in force until
> 2026-08-28. **The user ruled that arrangement away** —
> `cowork_rulings_2026_08_28_informed_framework_sitting.md`, his words *"In my opinion 3 still stands,
> yours too it seems."* The blind brief stays on disk as the record of what was designed under the
> previous ruling and as the starting point for any later blind run over this subject. **It is
> tracked; putting a superseded banner on its face is owed to a dispatch and is not done here.**
>
> **★ WHAT CHANGED, IN ONE SENTENCE.** The session may now read this project's own material —
> `ARCHITECTURE.md`, the specifications, the registers, the code — as design input; **there is no boot
> pack, no withheld family and no leak check**; and what replaces blindness as the guard against
> simply restating what exists is **§3's incumbency rule**, which is where the weight of this brief now
> sits.
>
> **★ THREE BARS SURVIVE THE RULING AND A READER MUST NOT ASSUME OTHERWISE.** The three sealed
> placement-sample files stay sealed (§3). The second limb of the phase constraint — *evidence treated
> as the decision* — still binds (§4). And **no session that has read
> `cowork_rulings_2026_08_28_informed_framework_sitting.md` or the seventy-sixth entry of
> `cowork_handoff.md` may author this document**, the bar being that the authoring side is not the
> side that argued the case for the arrangement it works under.
>
> **On the section set.** It follows the ruled form of the two pilot briefs
> (`cowork_rulings_2026_08_23_brief_validation_sitting.md`), with §5 changed in kind — an independence
> record is meaningless for an informed session, and what replaces it is stated there.

---

## 0. Terms, explained before anything rests on them

A reader of this brief knows music theory and may know nothing about this project. Every project term
is explained here, once, before it is used; standard music theory is used in its standard sense.

- **The analysis** — the harmonic-analysis software this project builds: given a notated score, it
  decides the tonality, the chords, and the moments at which one chord gives way to the next, and
  writes the result into the score as Roman numerals and chord symbols.
- **An informed deriving session** — one that writes what the analysis SHOULD do, and **may read what
  this project's code and specifications say it DOES.** It is not blind. What it may not do is treat
  what exists as a reason — see §3.
- **A layer** — one stage of the analysis, responsible for one question. *(The word is the ruled
  vocabulary of this phase, not this brief's choice: the phase's purpose is written as deciding "the
  layer decomposition". A session that concludes the layered shape is the wrong shape says so, with
  its reasons, as a finding.)*
- **A charter** — for one layer: the question it answers, the evidence it consumes, and the facts it
  publishes.
- **A boundary contract** — what one layer may assume about what reaches it from another, and what it
  owes in return.
- **The decomposition** — the set of layers together with what each is responsible for. It is the
  thing this session is chiefly for.
- **A unit** — one item of the list the sources of §3 yield: the things the framework is a framework
  OF. **What a unit IS, is itself an open question and is treated at §4.**
- **A design point** — one place where the architecture could go more than one way, and a choice is
  therefore made rather than followed.
- **Incumbency** — the fact that some design is the one this project already built or already
  specified. §3 states what incumbency is worth here.
- **Tonality** — used throughout for what is commonly called "the key". In this project the bare word
  *key* is reserved for tonality and is never used for a lookup key or a map key; *bar* is used for
  the metric unit, never *measure*; *score* means the musical score and never a number; *note* means a
  pitch event and never a remark; *instrument* means a violin and never a measurement tool.

## 1. What this session is for, in one paragraph

Decide **the all-encompassing architecture of the analysis** — the layer decomposition, each layer's
charter, and the boundary contracts between layers — and write it as the **framework document**, so
that detail specifications can later be derived inside ruled charters. The session produces the
framework document, its open questions and its sources-and-incumbency record. It produces no code, no
detail specification, no measurement design and no fix plan.

## 2. The subject, in plain words

**Into what layers should a harmonic analysis of a notated score be divided; what question does each
layer answer, on what evidence, and what does it publish; and what may each layer assume about what
reaches it from the others?**

The purpose of dividing it at all, stated so the session can judge a division against something: so
that each question is answered where the evidence for it lives, once, and so that a later
specification of any one layer is written inside a charter that already says what that layer is for.

The question has at least these faces, listed so that none is silently dropped. **The session is free
to find this list incomplete, or wrongly cut, and to say so — the list is the writing side's reading
of the ruled purpose and is not itself ruled:**

- **What the layers are.** What is the set of questions a harmonic analysis must answer, and which of
  them belong together in one layer because they cannot be answered apart?
- **The grain.** How large is one layer — and how large is one unit inside it? **See §4; this is not
  the session's to settle alone.**
- **What each layer consumes.** What evidence does each question actually need, and what does needing
  it imply about the order the layers run in, or about whether they can run in an order at all?
- **What each layer publishes.** What facts does it owe outward, and to whom — including facts nothing
  currently asks for.
- **Where uncertainty lives.** Which layers may decline to answer, what they publish when they do, and
  what a later layer may assume about an answer that was committed under doubt.
- **The boundaries.** What may cross between two layers, in which direction, and what may not.
- **What is NOT a layer.** Responsibilities that look like one and are not — a view over what other
  layers decided, a presentation concern, a measurement concern.

## 3. What the session reads — and the one rule that now carries the weight

**The session may read this repository.** `ARCHITECTURE.md` and the per-layer design documents,
`docs/scoring_model.md` and the other design documents, the decisions register, the open-items
register, `EMPIRICAL_FINDINGS_LEDGER.md`, the ratified design intent, the source code. **Whether that
read is unbounded or is an enumerated list is §7 (P1) and is not ruled.**

**It should also fetch and read published research** — peer-reviewed papers, published algorithms,
public datasets' documentation. `docs/research_papers/` holds **fifty-eight PDFs and a
`BIBLIOGRAPHY.md`**, counted at the folder, and they are read from disk rather than re-fetched.
`cowork_literature_reachability_2026_08_26.md` §5 carries a candidate list of published models this
project does not reference, each with a remark on what it decomposes differently; **its own §6 declares
the sweep non-exhaustive** — one item was actually read and the rest are titles and abstracts — **so a
session that treats that list as coverage has misread it.**

**One gap is named rather than hidden.** The same report's §4 item 3 records that the primary source
for key profiles is **not held on disk**. A conclusion resting on key profiles is defending a factor
form from secondary descriptions, and says so in its own defense.

### ★ THE INCUMBENCY RULE — the whole of what replaces blindness

**Reading what exists is permitted. Citing it as a reason is not.**

Every design point is chosen on music theory, on published research, or on the ultimate objective and
the guiding principles. **"This is what the analysis currently does", "this is what the specification
says", and "changing it would be expensive" are NOT defenses and may not appear as one.** This is not
this brief's invention: it is the ratified decision-neutrality corollary, register entry **D-190**,
whose clause (a) states that reuse counts only as **carried-forward establishment** and never as sunk
cost.

**What incumbency IS worth, stated so the rule is not read as a ban on using what we know.** Where the
existing arrangement rests on a measurement, that measurement is evidence and travels with its own
establishment status. Where it rests on a fact in `EMPIRICAL_FINDINGS_LEDGER.md`, that fact has already
passed the test of surviving the implementation being thrown away and is evidence of the strongest kind
available here. Where it rests on nothing recorded, **it is worth nothing at this desk**, however long
it has been in place.

**Every point at which the derived answer agrees with the existing arrangement is flagged**, with a
one-line statement of whether the agreement was reached on the evidence or carried forward. That is
§5, and it is the one instrument this phase now has in place of independence.

### ★ THE THREE SEALED FILES STAY SEALED

`cowork_placement_sample_sealed_2026_08_27.md`,
`cowork_placement_sample_sealed_redraw_2026_08_27.md` and
`cowork_placement_sample_sealed_third_2026_08_27.md` are **NOT OPENED, in any portion.** They hold the
sample of statements a different side will later try to place into this document. **A session that read
them could write a framework document shaped around the statements it will be tested on**, which would
make the placement test measure nothing. The ruling of 2026-08-28 changed what this session may read
about the project; **it did not touch these**, and their disposition is an open question of the user's.

## 4. The form of the output's content, and the one question the session must NOT settle

**Per design point** (`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3.3,
outputs):

- **the candidates enumerated**, from every source kind, each with its **establishment status**;
- **at most ONE chosen per concern**, because one concern has one home — **or NONE**, written as
  *"underived: open, needs a ruling or new research"*;
- **the rivals recorded in the defense**, with why each is excluded, so that a later reader can
  re-test whether the ground for excluding it still holds.

**Every choice carries its defense in the same breath as the choice**, each load-bearing claim
labelled **FACT** where a source actually read states or measures it, **THEORY** where it is
established published theory, **CONJECTURE** otherwise.

**The phase constraint, quoted rather than paraphrased, with its two limbs at different strengths.**
The surface reads:

> **NOT ALLOWED:** implementation-derived material as design input; evidence treated as the decision.

- **The FIRST limb is SET ASIDE for this phase** by the ruling of 2026-08-28. *(That set-aside has
  been ruled and has not yet reached the phase-definition surface itself, there being no artifact
  that can receive an amendment to it. A reader who checks the surface will find the limb still
  standing there. The ruling record governs.)*
- **The SECOND limb BINDS, untouched, and is the easier one to breach without noticing:** evidence is
  an input and the choice is made against the objective and the principles — a measurement, or an
  annotation practice, does not decide a design point by itself.

**NOT DONE by this session** (same section): no detail specification is derived; no measurement-layer
design; no fix plan.

**★ THE GRAIN OF A UNIT IS NOT THIS SESSION'S TO SETTLE, AND THE RULING NAMES THE THREE CANDIDATE
READINGS.** Ruling 2 of `cowork_rulings_2026_08_21_successor_plan_sitting.md` places the grain with
this phase and states the question in these terms: *whether the resulting units are **factors of the
model**, **decisions the analysis makes about the music**, or **a reconciliation of the two**, is the
framework phase's first ratified finding, put to the user then with the evidence.* **So the session
states which reading it is working at, with its evidence and with what the other two would have
changed, as an explicit finding for the user to rule** — and does not present it as settled.

**Where a statement is behavioural**, it names what would falsify it in plain terms: the
**OBSERVABLE**, the **DECISION RULE** over it, and the **near-miss it is NOT falsified by**.
*(Under the previous arrangement this session could not name code sites and that fill-in was ruled to
a side permitted to read code —`cowork_rulings_2026_08_26_framework_opening_sitting.md`, Ruling 4.
**This session may read code, so whether it performs that fill-in itself or leaves it to the ruled
side is §7 (P7) and is not ruled.** Until it is, the session leaves the fill-in undone and declares
the gap, which is the previous arrangement's behaviour and the safe one.)*

**What cannot be settled is written as an open question, never filled with the most plausible
reading.**

## 5. The sources-and-incumbency record — what replaces the independence record

An independence record is meaningless for a session that may read everything. What this session
records instead, and **an output without it is incomplete**:

1. **Every source it opened** — repository files by path, fetched or on-disk research by citation.
2. **Every design point at which its answer AGREES with the arrangement this project already has**,
   each with one line: **reached on the evidence**, or **carried forward** — and, where carried
   forward, what evidence would be needed to reach it independently.
3. **Every design point at which its answer DIFFERS**, with the difference stated plainly. These are
   the phase's most valuable output and must not be buried in the defense prose.
4. **A positive statement that none of the three sealed files was opened.**

**Why (2) exists, stated so it is not treated as bookkeeping.** The framework document produced under
this ruling rests on the current division being right wherever it agrees with it, and that is a claim
which is checkable and which this arrangement does not check — the **#18** exposure the ruling record
names as undischarged. Item (2) does not discharge it. It makes the exposure **enumerable**, so that a
later independent run, if the user commissions one, has a list to attack rather than a whole document.

## 6. The output, and what the session does NOT do

**One file, at the repository root**, whose name is §7 (P4), carrying the status banner **DRAFT —
INFORMED DERIVATION, NOT COMPARED, NOT RATIFIED**, and bound by the fourteen-section design-document
standard the writing-standards document states. It is written for a reader who knows music theory and
not this project: terms explained at first use, predicates qualified, no invented labels, music-theory
words in their musical sense only.

**What happens to it afterwards.** A different side runs the **placement test**: it takes the sealed
sample and tries to place each statement into this document. There is no bright line — every
unplaceable statement is reported to the user as a finding, with the sample's size, the observed
proportion and its uncertainty range, and the user rules per finding
(`cowork_framework_phase_opening_surface_2026_08_26.md` §1(f)). **What that test now measures is
narrower than it was**: with an informed author it can no longer speak to independence, only to
coverage — whether the framework has a home for each statement. **Ratification of the decomposition is
separately HELD** until the external list of published research the user is assembling has arrived and
been dispositioned against it (2026-08-27,
`cowork_rulings_2026_08_27_framework_authoring_sitting.md`).

**What the session does NOT do:** it edits no specification and no code; it runs no build, no test, no
measurement tool, no generator and no guard; it creates, flips or discards no open-items row; it
allocates no finding number; it writes no `STATUS.md` entry, no handover block, no report and no
close; it commits nothing; it writes no dispatch; and **it decides nothing about the derivation
method**, which was ruled usable for a first version on 2026-08-25 and is not this session's business.

## 7. The points the user rules before this brief is dispatched — NONE IS RULED

- **(P1) What the informed session reads — unbounded, or an enumerated list.** The ruling permits
  this project's material as design input; it does not say whether the session is pointed at named
  documents or turned loose on the repository. **An enumerated list is a smaller read and risks
  omitting what matters; an unbounded read risks the session spending its span on the code.** The
  writing side names this as the largest of the remaining points.

- **(P4) The output file's name.** Fixed by the user for each pilot unit by ruling; not fixed here.

- **(P5) Whether this session keeps a sizing record.** The pilot's sizing was the pilot's business and
  no ruling extends it. **Must be settled before the session runs — a cost measurement cannot be
  reconstructed afterwards.**

- **(P6) Whether annotated scores are staged, and which.** The pilot units were given three
  score-and-analysis pairs BY NAME, as exemplars and never as a corpus, with the bar that no
  measurement is built, designed, scoped or run over them. **The annotation schema is a source**, and
  it is a question about what annotators record, so some exemplar may be needed. Which, and how many,
  is not ruled. **Must be settled before the session runs.**

- **(P7) Whether this session performs the code-site fill-in itself.** Ruling 4 of the framework-opening
  sitting routes that fill-in to a side permitted to read code, on the ground that the deriving session
  was not one. **That ground is gone.** Whether the routing goes with it, or stands for a separate
  reason, is the user's.

**Two points of the superseded brief are recorded as DISSOLVED rather than dropped (#12).** **(P2)**,
the withheld set for this subject — which that brief called the hardest of its points — and **(P3)**,
whether the staged candidate list is cut. Both existed only because a pack was to be rendered with a
withheld family. **No pack is rendered; neither question arises.** The enumeration performed for P2
is kept at `ratification_surfaces/cowork_withheld_family_framework_reading.md`.

## 8. Provenance — for the user and the record; NOT opened by the deriving session

Written by the writing side (Cowork) on 2026-08-28, in the session that took the informed-framework
ruling, at tip `bf3249e73d9eb91d0f2513bc2c16aa626b53e464` read as a file at the ref. **No shell
command was run against the repository by this side and every git-object value it could state is
RELAYED**, the tip included. It supersedes `cowork_blind_session_brief_framework.md` and carries that
brief's §0, §1, §2, §4 and §6 substantially unchanged, its §3 and §5 replaced in kind, and its §7
reduced and extended as §7 states.

**The bar on who may author from this brief is in the banner and is not a formality:** the session
that wrote this brief argued the case for the arrangement the brief describes, and a side that has
argued a case is not the side to test it.

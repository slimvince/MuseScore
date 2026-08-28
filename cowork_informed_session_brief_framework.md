# BRIEF for the INFORMED deriving session — the FRAMEWORK document

> **STATUS: READY, NOT DISPATCHED. ★ ALL SEVEN OF §7's POINTS ARE NOW RULED** —
> `cowork_rulings_2026_08_28_informed_brief_points_sitting.md`, the user's words *"I agree with all
> recommendations."* **One item is left undecided by name and is marked at §5.** Written by the
> writing side (Cowork, 2026-08-28) and revised the same day against those rulings; the tip at the
> revision was `8798d6049e2e237efd4d8bffd5b7f7f904815493`, read as a file at
> `.git/refs/heads/master`. It dispatches nothing and boots no session.
>
> **★ IT SUPERSEDES `cowork_blind_session_brief_framework.md`, WHICH IS KEPT AND NOT EDITED (#12).**
> That brief was written for an implementation-blind session under the arrangement in force until
> 2026-08-28. **The user ruled that arrangement away** —
> `cowork_rulings_2026_08_28_informed_framework_sitting.md`, his words *"In my opinion 3 still stands,
> yours too it seems."* The blind brief stays on disk as the record of what was designed under the
> previous ruling and as the starting point for any later blind run over this subject. **It now
> carries a superseded banner on its face**, placed by
> `cc_instruction_framework_arrangement_landing.md` Task 2.
>
> **★ WHAT CHANGED, IN ONE SENTENCE.** The session may now read this project's own material —
> `ARCHITECTURE.md`, the specifications, the registers, the code — as design input; **there is no boot
> pack, no withheld family and no leak check**; and what replaces blindness as the guard against
> simply restating what exists is **the two-stage order of §3 together with the incumbency rule**,
> which is where the whole weight of this brief now sits.
>
> **★ THE SHAPE OF THE WORK, BEFORE ANY DETAIL: IT IS TWO STAGES AND THE ORDER IS NOT A SUGGESTION.**
> **Stage one derives from OUTSIDE this project and is written down before anything of ours is
> opened. Stage two reads ours and revises, recording every change and why.** A session that reads our
> material first has destroyed the only instrument this phase has, and cannot restore it by trying
> harder afterwards. §3 states it; §5 is the record it produces.
>
> **★ THREE BARS SURVIVE THE RULING AND A READER MUST NOT ASSUME OTHERWISE.** The three sealed
> placement-sample files stay sealed (§3). The second limb of the phase constraint — *evidence treated
> as the decision* — still binds (§4). And **no session that has read
> `cowork_rulings_2026_08_28_informed_framework_sitting.md`,
> `cowork_rulings_2026_08_28_informed_brief_points_sitting.md`, or the seventy-sixth or
> seventy-seventh entry of `cowork_handoff.md` may author this document**, the bar being that the
> authoring side is not the side that argued the case for the arrangement it works under.
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
- **The first-stage draft** — what this session writes from the outside sources alone, before it opens
  any of this project's own material. It is a deliverable in its own right and is never overwritten.
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

## 3. What the session reads, and IN WHAT ORDER — the rule that carries the whole weight

**Ruled** (`cowork_rulings_2026_08_28_informed_brief_points_sitting.md`, Ruling 1). The read is
**neither unbounded nor an enumerated list. It is two stages, and the order is the instrument.**

### Stage one — derive from outside this project, and WRITE IT DOWN

**★ WHAT THE STAGE-ONE BAR ACTUALLY IS, because the obvious reading of it is wrong.** It is **not**
*open no file of this project* — four of the six sources below are files in this repository. **It is:
open nothing that says what this project's analysis DOES or is SPECIFIED to do.** That means
`ARCHITECTURE.md`, the per-layer design documents, `docs/scoring_model.md`, the registers and the
source code — and nothing else is closed to stage one. **The sources below are admissible precisely
because none of them describes the built thing:** published research and music theory are not ours;
the annotation exemplars are other people's readings of music; the ledger's entries have each passed
the test of surviving our implementation being thrown away; and the ten-factor model is ratified
design intent, admitted to a deriving session by name.

Derive the decomposition from these and nothing else:

- **music theory** — what a harmonic analysis of this repertoire consists of, *including what
  annotators do not write down*;
- **published research**, fetched or read from disk. `docs/research_papers/` holds **fifty-eight PDFs
  and a `BIBLIOGRAPHY.md`**, counted at the folder; read them there rather than re-fetching. The
  candidate list at `cowork_literature_reachability_2026_08_26.md` §5 names published models this
  project does not reference, each with a remark on what it decomposes differently;
- **the ground-truth annotation schema**, read at the three exemplars of §7 (P6). **They are inside
  this repository and nothing needs staging** — the paths are named there. **★ TWO OF THE THREE CARRY
  TWO INDEPENDENT HUMAN ANALYSES OF THE SAME PIECE**, which is a fact about the ground truth and not a
  duplicate: what two analysts of one chorale agree and disagree about bears directly on what any one
  layer can be expected to decide;
- **`EMPIRICAL_FINDINGS_LEDGER.md`** — thirty-five facts that have already passed the test of
  surviving the implementation being thrown away, which is what makes them admissible here;
- **`cowork_joint_estimator_factorization.md`**, the user-ratified ten-factor model, admissible as
  design intent by Ruling 2 of the successor-plan sitting.

**The first-stage draft is then WRITTEN — a complete answer to §2's question, in §4's form, with its
defenses.** It is not notes and it is not an outline. **It is never overwritten and never edited after
stage two opens** (#12): stage two revises the document, and the first-stage draft stands beside it as
what this session would have said. *Where the first-stage draft lives — a section of the framework
document, an appendix, or a sibling file — is the one thing the rulings leave open; see §5.*

### Stage two — read this project's material, and revise on the record

**Only now** open `ARCHITECTURE.md`, the per-layer design documents, `docs/scoring_model.md`, the
decisions register, the open-items register, the ratified design intent and the source code. Read what
you judge relevant; nothing here is enumerated, because the guard is the order and not the list.

**Every change stage two makes to the stage-one answer is recorded with its reason**, and every point
at which stage one already agreed is recorded as agreement. That record is §5, and producing it is not
a chore attached to the work — **it is the phase's second deliverable.**

**Why the order and not a wall.** A session that reads our answer first cannot afterwards say what it
would have derived; a session that writes its own answer first can say exactly what our material
changed and why. The difference is observed rather than remembered, which is the only reason this
arrangement can claim anything at all about independence.

### ★ WHAT THIS SESSION DOES NOT OPEN IN EITHER STAGE — AND THE ORDINARY SESSION-START READ IS REPLACED

**The ordinary session-start read of this repository does NOT apply to this session.** Do not perform
it. **Read this brief first, and open nothing else until stage one is written.**

**These are closed to this session in BOTH stages, and opening any of them disqualifies it from
authoring** — the bar is that the authoring side must not be the side that argued the case for the
arrangement it is working under:

- **`cowork_handoff.md`** — any entry, in any portion. It carries the argument that produced this
  brief.
- **`cowork_rulings_2026_08_28_informed_framework_sitting.md`** and
  **`cowork_rulings_2026_08_28_informed_brief_points_sitting.md`** — the two records that decided how
  this session works. **What they ruled is already in this brief; their reasoning is not for you.**
- **Any `cc_report_*.md` and any `cc_instruction_*.md`** — the coding side's reports and dispatches.
- **§8 of this brief**, its provenance section.
- **The three sealed placement-sample files**, as below.

**This is not a blindness bar and it is not about the analysis.** Everything closed here is a record
of *how this phase was decided*, not of what the analysis does — and stage two opens the whole of the
latter. **If you have already read any of them, say so and stop; the session is not void, but it may
not author this document.**

*(`EMPIRICAL_FINDINGS_LEDGER.md`, `PHASE_CONSTRAINTS_AND_STOP_RULES.md` and the phase-definition
surface are NOT on this list. The first is a stage-one source; the other two state the rules you work
under and are meant to be read.)*

### The two bounds that travel with stage one's sources

**The literature sweep is not coverage.** `cowork_literature_reachability_2026_08_26.md` **§6 declares
its own sweep non-exhaustive** — one item was actually read and every other is a title and an abstract,
and four classes of work were unreachable by construction. **A session that treats its §5 list as
coverage has misread it**, and a decomposition the list does not contain is not thereby excluded.

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
**★ IT DOES NOT NAME CODE SITES AND DOES NOT NAME WHICH ARM A STATEMENT BINDS — RULED, AND NOT
BECAUSE IT CANNOT.** That fill-in stays with a side other than the author
(`cowork_rulings_2026_08_28_informed_brief_points_sitting.md`, Ruling 5). This session may read code,
so the original ground — that it could not — is gone; **the routing is kept because a verifier who is
not the author is the stronger form of #15, and an author checking its own statements against the code
it just read as design input is the weakest.** **The gap is declared on the face of the framework
document:** its statements are checkable in principle and not yet checkable in fact until that fill-in
runs.

**What cannot be settled is written as an open question, never filled with the most plausible
reading.**

## 5. The two-stage record — the phase's second deliverable

An independence record is meaningless for a session that may read everything. **What replaces it is
not a claim the session makes about itself but a comparison of two texts it wrote**, and an output
without it is incomplete.

1. **The first-stage draft, whole and unedited.** It is the artifact the rest of this section is read
   against. **★ WHERE IT LIVES IS THE ONE THING THE RULINGS LEAVE OPEN** — a section of the framework
   document, an appendix, or a sibling file. Until the user settles it, **the session keeps it as a
   clearly-marked appendix of the one output file** and says on its face that the placement is not
   ruled. It is never edited after stage two opens (#12).
2. **Every source opened, in each stage separately** — repository files by path, research by citation
   — so that the two stages' inputs can be told apart by a reader.
3. **Every design point at which stage two's answer AGREES with the arrangement this project already
   has**, each with one line: **reached at stage one on the evidence**, or **carried forward at stage
   two** — and, where carried forward, what evidence would be needed to reach it independently.
4. **Every design point at which the answer DIFFERS from this project's arrangement**, stated plainly.
   **These are the phase's most valuable output and must not be buried in the defense prose.**
5. **Every change stage two made to the stage-one draft, with its reason** — including changes that
   have nothing to do with our arrangement, so that the list is a complete account of the revision and
   not a curated one.
6. **A positive statement that none of the three sealed files was opened.**

**Why this exists, stated so it is not treated as bookkeeping.** The framework document produced under
the informed arrangement rests on the current division being right wherever it agrees with it, and
that is a claim which is checkable and which this arrangement does not check — the **#18** exposure the
ruling record names as **undischarged**. **This record does not discharge it.** It makes the exposure
**enumerable**: a later independent run, should the user commission one, attacks a list rather than a
whole document, and item (1) lets a reader see what this session had before it read ours.

## 6. The output, and what the session does NOT do

**One file, at the repository root**, named
**`cowork_framework_document_draft_<YYYY_MM_DD>.md`** — the date being the day the session writes it,
**established at the user's machine and never asserted from the session's own environment**, a
misdating having been a counted error of 2026-08-28. **The draft name is ruled and so is its
retirement: the file is RENAMED as an explicit step at ratification** and not before
(`cowork_rulings_2026_08_28_informed_brief_points_sitting.md`, Ruling 2). It carries the status banner
**DRAFT — INFORMED DERIVATION, NOT COMPARED, NOT RATIFIED**, and is bound by the fourteen-section
design-document standard the writing-standards document states. It is written for a reader who knows music theory and
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

## 7. The points the user ruled — ALL FIVE RULED 2026-08-28, and ONE ITEM LEFT OPEN

Ruled at `cowork_rulings_2026_08_28_informed_brief_points_sitting.md`; the user's words, *"I agree
with all recommendations."* **The points are recorded here rather than removed (#12), because a
successor reading the brief alone must be able to see what was decided and what the alternative was.**

- **(P1) What the informed session reads. RULED: two stages, §3.** Declined: an unbounded read, on
  the ground that the shortest path to a finished document runs through `ARCHITECTURE.md`; an
  enumerated list, because authoring that list is the same judgment the retired 208 verdicts were.
- **(P4) The output file's name. RULED: a dated draft name, renamed at ratification, §6.** Declined:
  a permanent root name, on **#6**, while the document it may supersede still stands.
- **(P5) A sizing record. RULED: a minimal one, declared NOT A BUDGET.** The session records when it
  started and ended, what it read in each stage, and what it produced. Declined: none, because it
  cannot be reconstructed afterwards; and a full record in the pilot's shape, on **#19** — the pilot's
  carries three named defects and a second copy of them is not established by being second.
- **(P6) Annotated scores. RULED: the same three score-and-analysis pairs the pilot units were given,
  BY NAME, as exemplars and never as a corpus**, with the bar that **no measurement is built,
  designed, scoped or run over them.** They serve stage one's annotation-schema source. Declined:
  none, which would leave that source with no artifact behind it; and a larger set, which at some size
  stops being exemplars and engages **#9** and **#20**.

  **★ THE PATHS, ENUMERATED AT THE FOLDERS BY THE WRITING SIDE ON 2026-08-28. ALL SIX FILES ARE
  INSIDE THIS REPOSITORY; NOTHING IS STAGED, CONNECTED OR COPIED.**

  | | The score | The human analysis |
  |---|---|---|
  | **001** | `tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx` | `tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/001/analysis.txt` **and `analysis_BCMH.txt`** |
  | **003** | `tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx` | `…/Chorales/003/analysis.txt` **and `analysis_BCMH.txt`** |
  | **137** | `tools/dcml/bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx` | `…/Chorales/137/analysis.txt` **only — no `analysis_BCMH.txt`**, established at the folder |

  **The analyses are RomanText: plain text, Roman numerals with the beat positions they sit at.** The
  scores carry **no harmony annotation of their own** — the human reading is these separate files, which
  is itself a fact about how this ground truth is shaped.

  **★ 001 AND 003 EACH CARRY TWO INDEPENDENT ANALYSES OF THE SAME PIECE, AND THAT IS THE POINT OF
  READING THEM.** Where the two disagree is evidence about what a human analysis actually settles and
  what it leaves open — which bears directly on what any one layer can be asked to decide, and on
  where uncertainty has to live. **Reading the disagreement is not measuring it:** no rate, no count
  and no proportion is taken from three pieces, and a statement resting on one would be exactly the
  unestablished instrument **#19** forbids.
- **(P7) The code-site fill-in. RULED: it stays with a side other than the author**, §4. **Declared:
  the original ground is gone and this ruling rests on a preference the writing side marked as one.**

**★ THE ONE ITEM STILL OPEN: where the first-stage draft lives** — a section of the framework
document, an appendix, or a sibling file. **Until it is settled the session keeps it as a
clearly-marked appendix and says the placement is not ruled** (§5, item 1).

**Two points of the superseded brief are recorded as DISSOLVED rather than dropped (#12).** **(P2)**,
the withheld set for this subject — which that brief called the hardest of its points — and **(P3)**,
whether the staged candidate list is cut. Both existed only because a pack was to be rendered with a
withheld family. **No pack is rendered; neither question arises.** The enumeration performed for P2
is kept, and now bannered, at `ratification_surfaces/cowork_withheld_family_framework_reading.md`.

## 8. Provenance — for the user and the record; NOT opened by the deriving session

Written by the writing side (Cowork) on 2026-08-28, in the session that took the informed-framework
ruling, at tip `bf3249e73d9eb91d0f2513bc2c16aa626b53e464`, **landed by
`cc_instruction_framework_arrangement_landing.md` Task 0, and REVISED the same day against the seven
rulings of the informed-brief-points sitting at tip
`8798d6049e2e237efd4d8bffd5b7f7f904815493`** — every tip read as a file at the ref. **No shell command
was run against the repository by this side and every git-object value it could state is RELAYED**,
the tips included.

It supersedes `cowork_blind_session_brief_framework.md` and carries that brief's §0, §1, §2 and §4
substantially unchanged. **Changed in kind at the revision:** §3 became the two-stage order, §5 became
the two-stage record, §6 took the ruled draft name, and §7 became a record of what was ruled rather
than a list of what was open. **The revision added no bar and removed none.**

**The bar on who may author from this brief is in the banner and is not a formality:** the session
that wrote this brief argued the case for the arrangement the brief describes, and a side that has
argued a case is not the side to test it.

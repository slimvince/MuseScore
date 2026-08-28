# BRIEF for the blind deriving session — the FRAMEWORK document

> **★ SUPERSEDED, 2026-08-28, BY `cowork_informed_session_brief_framework.md`.** The user ruled at
> `cowork_rulings_2026_08_28_informed_framework_sitting.md` that the framework phase's deriving
> session is **not implementation-blind**, so the arrangement this brief is written for — a rendered
> boot pack, a withheld family, a leak check — is not the arrangement that phase now runs under.
> **This file is KEPT and not deleted (#12):** it is the record of what was designed under the
> previous arrangement, and it is the starting point for any later blind run over this subject.
> **Nothing else in it is edited**, and every statement below it stands as it was written — read it
> as a record, never as an instruction.
>
> **STATUS: DRAFT — NOT RULED, NOT DISPATCHED, AND NOT YET USABLE.** Written by the writing side
> (Cowork, 2026-08-27, the fifty-fourth session) at branch tip
> `acedffc66d8c40f17d5fe6dbb73ca1ac90129997`, read as a file at `.git/refs/heads/master`.
> **It dispatches nothing and boots no session.**
>
> **★ TWO THINGS MUST HAPPEN BEFORE THIS BRIEF IS HANDED TO ANYONE.** First, **the boot pack this
> brief's §3 names does not exist**: `tools/audit/derivation_boot_pack/` holds `scoring-model/` and
> `harmony-boundary/` and no third subject. It is rendered by `gen_derivation_boot_pack.py`, which is
> a Claude Code act by dispatch, and **its withheld set must be derived for THIS subject** — see §7
> (P2), which is the hardest of the open points and not a formality. Second, **§7 lists the points
> the user rules before this brief is dispatched, and none of them is ruled.**
>
> **Who reads this file, and when.** The deriving session reads it FIRST, before it opens the boot
> pack. Everything the session may read is named in §3; **this brief and that directory are the
> session's whole read inside this repository.** The provenance at the foot (§8) is for the user and
> for a later reader of the record; **the deriving session does not open any file §8 names.**
>
> **On the section set.** It follows the two pilot briefs, which are the ruled form
> (`cowork_rulings_2026_08_23_brief_validation_sitting.md`), with one change declared rather than
> made silently: **the pilot's sizing record is not carried**, because sizing was the pilot's own
> business and no ruling extends it to this phase. Whether this session keeps one is §7 (P5).

---

## 0. Terms, explained before anything rests on them

A reader of this brief knows music theory and knows nothing about this project. Every project term is
explained here, once, before it is used; standard music theory is used in its standard sense.

- **The analysis** — the harmonic-analysis software this project builds: given a notated score, it
  decides the tonality, the chords, and the moments at which one chord gives way to the next, and
  writes the result into the score as Roman numerals and chord symbols. **How it CURRENTLY does any
  of this is exactly what this session must not know.**
- **A deriving session** — one that writes what the analysis SHOULD do, from music theory, from
  published research it fetches and reads, and from the ruled design intent it is given — WITHOUT
  reading what this project's code or this project's specifications say it DOES. Such a session is
  called *implementation-blind*, or *blind* for short.
- **The boot pack** — the one directory a deriving session reads at boot, generated from a ruled
  reading list: six rendered files plus a read-me. §3 names the directory.
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
- **A unit** — one item of the list the four sources of §3 yield: the things the framework is a
  framework OF. **What a unit IS, is itself an open question and is treated at §4.**
- **A design point** — one place where the architecture could go more than one way, and a choice is
  therefore made rather than followed.
- **Tonality** — used throughout for what is commonly called "the key". In this project the bare word
  *key* is reserved for tonality and is never used for a lookup key or a map key; *bar* is used for
  the metric unit, never *measure*; *score* means the musical score and never a number; *note* means a
  pitch event and never a remark; *instrument* means a violin and never a measurement tool.

## 1. What this session is for, in one paragraph

Decide, blind, **the all-encompassing architecture of the analysis**: the layer decomposition, each
layer's charter, and the boundary contracts between layers — and write it as the **framework
document**, so that detail specifications can later be derived inside ruled charters. The session
produces the framework document, its open questions and its independence record. It produces no code,
no detail specification, no measurement design, no fix plan, no comparison against anything this
project currently has, and no verdict on anything this project currently does.

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

## 3. What the session reads — and the one rule that matters most

**The session's whole read inside this repository is this brief and the directory
`tools/audit/derivation_boot_pack/framework/`.** Open its `00_READ_THIS_FIRST.md` first; it names the
files and the order in which to read them. Nothing else inside this repository is opened: **not
`ARCHITECTURE.md`, which is the current statement of this very subject and is exactly what this
session must not read**; not any other specification; not the code; not the open-items register or the
decisions register; not any session handoff, dispatch or report; not `STATUS.md`. **The ordinary
session-start read of this repository is REPLACED, for this session, by the pack.** The session does
not take the branch rule, does not read the commit log, and runs nothing.

**Three sealed files are withheld by name, and the session is told so rather than left to wonder:**
`cowork_placement_sample_sealed_2026_08_27.md`,
`cowork_placement_sample_sealed_redraw_2026_08_27.md` and
`cowork_placement_sample_sealed_third_2026_08_27.md`. They hold the sample of statements that a
different side will later try to place into this session's framework document. **A session that read
them could write a framework document shaped around the statements it will be tested on**, which would
make the test measure nothing. This is not a suspicion about the session; it is the reason the sample
was sealed before the framework document was authored.

**Beyond the repository, the session MAY and SHOULD fetch and read published research** —
peer-reviewed papers, published algorithms, public datasets' documentation. This is not a permission
at the edge of the method; it is **source (ii) below**, and reaching the open web is the stated reason
this side of the work is a Cowork session at all
(`cowork_rulings_2026_08_26_framework_opening_sitting.md`, Ruling 1). Every load-bearing claim taken
from a source is labelled as the pack's principles prescribe: **FACT** where a paper actually fetched
and read states or measures it, **THEORY** where it is established published theory, **CONJECTURE**
otherwise. **A source that could not be fetched yields no statement**; the gap is recorded.

**The four sources the unit list is derived from, none weighted above the others**
(`cowork_rulings_2026_08_21_successor_plan_sitting.md`, Ruling 2, read at the object by the writing
side):

1. **the ground-truth annotation schema** — what published human analyses actually record, which is
   what the analysis is graded against;
2. **the state and factor spaces of the published models this project rests on**, fetched and read;
3. **music theory** — what a harmonic analysis of this repertoire consists of, *including what
   annotators do not write down*;
4. **the user-ratified ten-factor model of 2026-07-19** (`cowork_joint_estimator_factorization.md`),
   which that ruling holds **admissible to a blind session because it is a user-ratified ruling** —
   design intent, not a description of built software.

**A candidate list is staged with this brief, and its bound travels with it.** Ruling 6 of
`cowork_rulings_2026_08_26_framework_opening_sitting.md` §6A ordered an outward sweep for published
models this project does not reference, each carrying a remark on **what it decomposes differently**,
and ruled that its returns "become candidate inputs to source (ii) … and nothing more" — **no
admission, no ranking, no establishment status.** The list is
`cowork_literature_reachability_2026_08_26.md` §5. **Its own §6 declares the sweep non-exhaustive and
does not discharge that bound:** one item was actually read, every other is a title and an abstract,
and four classes of work were unreachable by construction. **A session that treats the list as
coverage has misread it**, and a decomposition it does not contain is not thereby excluded.

**One gap is named rather than hidden.** The same report's §4 item 3 records that **the primary source
for key profiles is not held on disk.** If this session's answer comes to rest on key profiles, it is
defending a factor form from secondary descriptions, and it says so in the defense rather than letting
the citation stand as if the primary source had been read.

**★ THE STOP-ON-MEETING CLAUSE.** If, anywhere in the pack, in this brief, or in the staged candidate
list, the session meets a statement about **how THIS project's analysis is currently built or how it
currently behaves**, it **STOPS READING THAT FILE AT THAT POINT** and records, in its independence
record (§5), which file, where in it, and how much it saw before stopping. It then continues with the
remaining files. It does not delete, paraphrase or reason about what it saw. **Ratified design intent
is NOT such a statement** — the pack's design-intent member is a ruled input and is meant to be read;
what triggers the clause is a description of the built thing. **A session whose output carries no such
record, and no positive statement that nothing was met, is incomplete.**

## 4. The form of the output's content, and the one question the session must NOT settle

**Per design point** (`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3.3,
outputs):

- **the candidates enumerated**, from both source kinds, each with its **establishment status**;
- **at most ONE chosen per concern**, because one concern has one home — **or NONE**, written as
  *"underived: open, needs a ruling or new research"*;
- **the rivals recorded in the defense**, with why each is excluded, so that a later reader can
  re-test whether the ground for excluding it still holds.

**Every choice carries its defense in the same breath as the choice** — the music theory, the research
fetched and read, or the constraint that forces it, each load-bearing claim labelled FACT / THEORY /
CONJECTURE. **"Because the current implementation does this" is not available to this session and is
not a defense.**

**Two clauses bind and are quoted rather than paraphrased** (same section, constraints):

> **NOT ALLOWED:** implementation-derived material as design input; evidence treated as the decision.

The second is the easier one to breach without noticing: **evidence is an input, and the choice is made
against the objective and the principles** — a measurement, or an annotation practice, does not decide
a design point by itself.

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
**OBSERVABLE**, the **DECISION RULE** over it, and the **near-miss it is NOT falsified by**. **It does
not name code sites and does not name which code arm a statement binds** — that fill-in is ruled to a
side permitted to read code (`cowork_rulings_2026_08_26_framework_opening_sitting.md`, Ruling 4), and
**the gap is declared on the face of the framework document**: its statements are checkable in
principle and not yet checkable in fact until that fill-in runs.

**Current and previously deleted headings of this project's documents are NOT a source of the
framework** (`cowork_framework_phase_opening_surface_2026_08_26.md` §1(e)). The session will not meet
them; it is told so that it does not go looking for what an existing document says.

**What cannot be settled is written as an open question, never filled with the most plausible
reading.**

## 5. The independence record

The output states: every file the session opened, pack files and fetched sources alike, the latter by
citation; every pack file it did not open, if any; and the stop-on-meeting record of §3 — or the
positive statement that it met no such passage. **An output with no independence record is
incomplete.**

## 6. The output, and what the session does NOT do

**One file, at the repository root**, whose name is §7 (P4), carrying the status banner **DRAFT —
BLIND DERIVATION, NOT COMPARED, NOT RATIFIED**, and bound by the fourteen-section design-document
standard the pack's writing-standards member states. It is written for a reader who knows music theory
and not this project: terms explained at first use, predicates qualified, no invented labels,
music-theory words in their musical sense only.

**What happens to it afterwards, so the session knows what its output is and is not.** A different
side then runs the **placement test**: it takes the sealed sample of statements and tries to place
each one into this framework document. There is no bright line — every unplaceable statement is
reported to the user as a finding, with the sample's size, the observed proportion and its uncertainty
range, and the user rules per finding (`cowork_framework_phase_opening_surface_2026_08_26.md` §1(f)).
**Ratification of the decomposition is separately HELD** until an external list of published research
the user is assembling has arrived and been dispositioned against it (ruled 2026-08-27,
`cowork_rulings_2026_08_27_framework_authoring_sitting.md`). **This changes nothing about how the
session works** and is stated only so that the session does not treat its draft as final, and does not
hedge in anticipation of a list it will never see.

**What the session does NOT do:** it compares nothing against anything; it edits no specification and
no code; it runs no build, no test, no measurement tool, no generator and no guard; it creates, flips
or discards no open-items row; it allocates no finding number; it writes no `STATUS.md` entry, no
handover block, no report and no close; it commits nothing; it writes no dispatch; it opens no
untrusted source; and **it decides nothing about the derivation method**, which was ruled usable for a
first version on 2026-08-25 and is not this session's business.

## 7. The points the user rules before this brief is dispatched — NONE IS RULED

- **(P1) Who renders the boot pack, and from which reading list.** The pack does not exist. Rendering
  it is a Claude Code act by dispatch; the reading list is ruled
  (`cowork_rulings_2026_08_22_boot_list_sitting.md`) but has been applied only to the pilot's two
  subjects. **Whether this subject takes that list unchanged is not ruled.**

- **(P2) ★ THE WITHHELD SET FOR THIS SUBJECT — the hardest point, and it is not a formality.** The
  pack's member (2) is `CLAUDE.md` **rendered whole**, and the record already carries **two separate
  occasions on which that member leaked the held-out answer** for the harmony-boundary subject: the
  founding-instance passage of the never-work-from-memory rule
  (`cowork_rulings_2026_08_22_member_two_leak_sitting.md`, Ruling 1) and the founding-instances
  sentence of the defense-at-its-home rule
  (`cowork_rulings_2026_08_23_member_two_second_leak_sitting.md`, Ruling 1). **Both lay outside the
  generator's leak-check scope, which is members (5) and (6)**, and both were withheld by an authored
  per-passage list **scoped to that subject.**

  **The consequence for this subject is stated rather than left to be met at the render.** The
  withheld answer here is **the decomposition itself**, so any passage of `CLAUDE.md` that states what
  the layers are, what each is responsible for, what evidence ranks where, or where a boundary falls
  is a leak — and `CLAUDE.md` is a document about exactly those things. **The harmony-boundary
  withheld list does not carry across**, and a render that reuses it would be a render with no
  withheld set worth the name. **Deriving this subject's withheld set is a first-class act with its
  own dispatch, and this brief is not final until it has run and been verified at the objects.**
  Member (5), the ratified design intent, has its own standing check and is the second surface, not
  the first.

- **(P3) Whether the candidate list of §3 is staged whole or in part.** Its §5 preamble states, in one
  clause, the shape this project's ratified design intent already commits to. That is design intent
  and therefore admissible — **but it pre-frames the decomposition this session exists to derive**,
  and the writing side does not treat "admissible" as settling "wise". Staging §4 item 3 and §5 alone,
  without that clause, is the alternative.

- **(P4) The output file's name.** Fixed by the user for each pilot unit by ruling; not fixed here.

- **(P5) Whether this session keeps a sizing record.** The pilot's sizing was the pilot's business and
  no ruling extends it; this brief therefore carries none. If a cost measurement for this phase is
  wanted, it must be asked for before the session runs, because it cannot be reconstructed afterwards.

- **(P6) Whether annotated scores are staged, and which.** The pilot units were given three
  score-and-analysis pairs BY NAME, as exemplars and never as a corpus, with the bar that no
  measurement is built, designed, scoped or run over them. **Source (i) of the four is the annotation
  schema**, which is a question about what annotators record — so some exemplar may be needed. Which,
  and how many, is not ruled.

## 8. Provenance — for the user and the record; NOT opened by the deriving session

Written by Cowork, 2026-08-27, the fifty-fourth session, at tip
`acedffc66d8c40f17d5fe6dbb73ca1ac90129997`, read as a file at `.git/refs/heads/master` with the file
tool. **No shell command was run against the repository by this side.** This session is barred from
authoring the framework document by Ruling 1 of
`cowork_rulings_2026_08_26_framework_opening_sitting.md` and by the seventy-third handoff entry, which
is what makes it eligible to write this brief: writing a brief is not a deriving act.

**Where §2's subject statement and its faces came from, so a reader can check that no implementation
content entered them.** From `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`
§3.3, read whole, and from `cowork_framework_phase_opening_surface_2026_08_26.md` §1, read whole —
both governance documents about what the phase IS. **`ARCHITECTURE.md` was NOT opened by the writing
side, not in any portion.** The faces in §2 are the writing side's own decomposition of the ruled
purpose, written to be answerable from the domain; a session that finds the decomposition wrong says
so.

**★ ONE CONTAMINATION HAZARD OF THE WRITING SIDE, DECLARED BECAUSE IT IS INVISIBLE FROM INSIDE THE
DERIVING SESSION.** This session performed the mandatory session-start read of `DECISIONS.md`, the
decisions register's INDEX, **in full**. That index carries one-line restatements of every recorded
decision, and a number of them describe the analysis as it is currently built. **Nothing from it was
used in writing this brief**, and §2 was written from the two sources named above and from nothing
else — but the claim is the writing side's own and cannot be checked from inside the deriving session,
so it is stated here rather than assumed. **A reviewer of this brief should read §0 and §2 against
that hazard specifically.**

**Other reads by the writing side, named so the brief's own independence can be judged:** the
seventy-first to seventy-third entries of `cowork_handoff.md`;
`cowork_literature_reachability_2026_08_26.md` whole; `cowork_rulings_2026_08_26_framework_opening_sitting.md`
§0–§6A; `cowork_rulings_2026_08_21_successor_plan_sitting.md` at Ruling 2, read at the object rather
than relayed through the opening surface's restatement of it; both member-(2) leak records at their
Ruling 1; `cc_report_unit_correction_redraw.md` §9 and §12.3;
`cowork_blind_session_brief_scoring_model.md`, whose form this brief follows; `STATUS.md`;
`tools/audit/nongating_apparatus_rows.json` at its live gating answer; and the directory listing of
`tools/audit/derivation_boot_pack/`. **NOT opened:** any of the three sealed files, not in any portion;
`ARCHITECTURE.md`; `cowork_evidence_inventory.md`; `cowork_joint_estimator_factorization.md`; any
source file, measurement output, dossier, boot-pack member, or PDF.

**The verification limit, unchanged for a tenth session:** this side cannot resolve a commit or a blob
without a shell, so **every git-object value it might have relayed is unverified here**, and none is
relayed into this brief.

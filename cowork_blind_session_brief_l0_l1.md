# BRIEF for the blind deriving session — the L0+L1 subject (the detail-specification phase's first derivation)

> **STATUS: ALL FIVE POINTS OF §8 ARE RULED, THE BOOT PACK §3 NAMES EXISTS, AND FOUR SCORES ARE STAGED.
> This brief is complete. It dispatches nothing and boots no session.** **P1, P2 and P4 were ruled
> 2026-08-31** (Ruling 13, `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3m); **(P5) the pack
> was rendered 2026-08-31**; **(P3) the notation question was ruled across 2026-08-31 and 2026-09-01**
> (Rulings 15, 19, 22, 23 and 24 of the same record). All five are applied below. Written by the Cowork
> writing side on 2026-08-31, under **Ruling 10** (L0+L1 is the phase's first deriving subject),
> **Ruling 11** (what the pack carries) and **Ruling 12** (annotated material) of
> `cowork_rulings_2026_08_31_decision_surface_sitting.md`. **The user opens the deriving session when
> the user chooses** (the 2026-08-26 role ruling: the writing side writes instructions to disk and
> never starts the sessions that run them).
>
> **Who reads this file, and when.** The deriving session reads it FIRST, before it opens the boot
> pack. Everything the session may read is named in §3; **this brief and that directory are the
> session's whole read inside this repository.** The provenance at §9 is for the user and for a later
> reader; **the deriving session does not open any file §9 names.**
>
> **★ THIS SESSION DERIVES INSIDE A RATIFIED CHARTER, AND THAT IS THE DIFFERENCE FROM THE PILOT.**
> The pilot derived against nothing ruled above it. Here the layer's charter is **ratified and given**:
> it is not re-decided, not argued with, and not improved upon. **The session derives HOW the layer
> does what the charter says it does — never WHAT it does.** Where the charter is silent, the session
> derives; where the charter speaks, the session obeys and says so.

---

## 0. Terms, explained before anything rests on them

A reader of this brief knows music theory and knows nothing about this project. Every project term is
explained here, once, before it is used; standard music theory is used in its standard sense.

- **The analysis** — the harmonic-analysis software this project builds: given a notated score, it
  decides the tonality, the chords, and the moments at which one chord gives way to the next. **How it
  CURRENTLY does any of this is exactly what this session must not know.**
- **A deriving session** — one that writes what the analysis SHOULD do for one subject, from music
  theory, from published research it fetches and reads, and from the ruled material it is given —
  WITHOUT reading what this project's code or this project's specifications say it DOES. Such a
  session is **implementation-blind**, or **blind**.
- **The boot pack** — the one directory a deriving session reads at boot. §3 names it.
- **A charter** — the ratified statement of one layer's job: the question it answers, what it may
  consume, and what it publishes. Charters were derived and ratified in an earlier phase and are
  **given** to this session.
- **A layer** — one stage of the analysis, responsible for one question, consuming only what earlier
  layers published.
- **A statement** — one atomic sentence of the derived answer, in the six-field form of §4. The
  derived answer is a set of statements, not a paragraph.
- **A slice** — the charter's own term, defined in the charter the session is given. It is not
  redefined here.
- **Tonality** — used throughout for what is commonly called "the key". In this project the bare word
  *key* is reserved for tonality and never used for a lookup key; *bar* is used for the metric unit,
  never *measure*; *score* means the musical score and never a number; *note* is a pitch event and
  never a remark; *stem* is a note stem and never a file name.

## 1. What this session is for, in one paragraph

Derive, blind, **how the analysis should read a notated record and turn it into the change points,
the metric strength, the notated evidence and the cadence cues its charter says it publishes** (§2) —
and write that answer as statements in the six-field form of §4, each carrying its defense in the same
breath. The session produces statements, open questions, a measured-cost record and an independence
record. **It produces no code, no comparison against anything this project already has, and no verdict
on anything this project currently does.**

## 2. The subject, in plain words

**Two charters, derived together because the first is the second's whole input.**

**L0 is the input contract, and it is NOT a layer.** It states what the analysis is given: the notated
record and nothing derived from it. The subject question:

> **What exactly must a notated record supply for this analysis to run, what may be assumed about it,
> and what happens when a real score does not supply it?**

**★ AND THE ANSWER IS A CRITERION, NOT ONLY A LIST.** Beside whatever facts the session concludes a
notated record must supply, it states **the TEST by which a fact is admitted to that list at all** — what
makes something the kind of thing this layer may be given, and what makes something the kind of thing the
analysis must instead decide for itself. **A list without its test cannot be extended or argued with; a
test can.** Where the session finds the test does not settle a case it has met, that case is an open
question and is written as one.

**L1 is the first layer, and it decides nothing about the music.** Its charter question, in the
charter's own words, is: *at which moments MAY a harmony begin, and what does the notation say at each?*
The subject question:

> **How are those moments found, how is what the notation says at each of them established, and in what
> form are both published — given that this layer may decide nothing about the music?**

The faces below are the writing side's decomposition of those two questions, listed so none is silently
dropped. **The session is free to find the decomposition wrong and to say so.**

**(a) What counts as a note event at all.** The charter's change point is defined over *eligible*
notes and does not say what makes a note eligible. Grace notes, ornaments written as small notes,
trills and tremolo, cue-sized notes, notes in a voice that is not sounding, unpitched percussion, a
note of no duration: which of these open a change point, which sound, and which do neither? **This is
the largest hole the charter deliberately leaves, and it is this session's to fill.**

**(b) What a tie does.** Ties are given by L0. A tied group is one sounding event with one onset and
one release, and the notation writes it as several notes. Where does the release fall, what happens
when a tie crosses a bar line or a repeat, and what happens to a tie whose second note is missing or
whose pitch disagrees?

**(c) The change-point set and the slices over it.** The charter fixes that change points are every
onset **and every release**, and that the slices are ordered, covering, gapless and non-overlapping.
What remains: how simultaneity is decided when two events are notated at the same moment but not
identically; what happens where nothing sounds at all; whether a slice may have zero length and what
is done if the notation implies one; and what the boundary convention is — which slice a change point
belongs to.

**(d) Metric strength.** The charter says a metric strength class is published per change point.
What are the classes, how many, and how is each derived from the time signature, the bar line and the
position within the bar? What happens at a time-signature change, at an anacrusis, and where the
notated meter and the sounding accent disagree? **The charter fixes that this is a CLASS and not a
judgment; the session decides what the classes are.**

**(e) The notated boundary evidence.** The charter names bar line, fermata, rest, repeat sign and
double bar. What is published at a change point for each, what is published when several coincide, and
what is done with a mark that is not at a change point at all — a fermata over a rest, a double bar
mid-bar, a repeat whose ending differs on the second pass?

**(f) The local cadence cues.** The charter names three: a falling-fifth or rising-fourth bass motion,
a leading-tone resolution, and the sounding together of the fourth and seventh degrees of a candidate
tonality in the approach. **Each must be computable without knowing the tonality** — that is the
charter's own reason for placing them here. How is each defined precisely, over what window, from
which voice, and what does "a candidate tonality" mean when no tonality has been decided?

**(g) The form of what is published, and the bar on deciding.** The charter forbids L1 to publish any
decided boundary or any tonality claim. What does that forbid in practice — is a cue a claim? is a
metric strength class a claim? — and how must the published facts be shaped so that the next layer
receives **candidates and evidence, never decisions**?

**Scope.** Common-practice tonal music as notated in a score. **Deciding where one harmony actually
gives way to the next is OUT of scope** — that belongs to the next layer, and the charter says so. Where
a statement here depends on that, the dependency is written as a statement in its own right.

## 3. What the session reads — and the one rule that matters most

**The session's whole read inside this repository is this brief, the directory
`tools/audit/derivation_boot_pack/l0-l1/`, and the four score files named later in this section.** Open
the directory's `00_READ_THIS_FIRST.md` first; it names the
members and the order to read them. **Nothing else inside this repository is opened:** not this
project's specifications, not `ARCHITECTURE.md`, not the open-items or decisions registers, not any
session handoff, dispatch or report, and **above all not any document that states how this project's
analysis currently reads a score, finds change points, or computes metric strength.** The ordinary
session-start read of this repository is **REPLACED, for this session, by the pack.** The session takes
no branch rule, reads no commit log, and runs nothing.

**Beyond the repository, the session MAY fetch and read published research** — peer-reviewed papers,
published algorithms, public documentation — and MUST label every load-bearing claim it takes from them
FACT (stated or measured in a paper actually fetched and read), THEORY (established published theory),
or CONJECTURE. **A source that could not be fetched yields no statement**; the gap is recorded.

**★ THE STOP-ON-MEETING CLAUSE.** If anywhere in the pack or in this brief the session meets a statement
about how THIS project's analysis currently does any of §2's subject, it **STOPS READING THAT FILE AT
THAT POINT** and records, in its independence record (§6), which file, where in it, and how much it saw
before stopping. It then continues with the remaining files. It does not delete, paraphrase or reason
about what it saw. **A session whose output carries no such record, and no positive statement that
nothing was met, is incomplete.**

**★ FOUR SCORES ARE STAGED, BY NAME. The session may open these four files, and no other score:**

- `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`
- `tools/dcml/bach_chorales/MS3/011 Jesu, nun sei gepreiset.mscx`
- `tools/dcml/cpe_bach_keyboard/MS3/wq55n02a.mscx`
- `tools/dcml/couperin_clavecin/MS3/02_second_prelude.mscx`

**Nothing is said here about what any of them contains, or why each was chosen.** They are notated
scores. Read them as notation, and find in them whatever is there.

**Two elements in them are not notation and are not this session's subject.** `<Harmony>` and
`<StaffText>` carry text a transcriber added on top of the notation — in one of these files an
analytical reading of the music. **In every staged file the session does not read the contents of
`<Harmony>` or `<StaffText>` and derives nothing from them.** It records in its independence record
(§6) that it observed this, and how many of each it passed over in each file. **This is the same rule as
the stop-on-meeting clause above, applied to an element name instead of a passage.**

**★ THE SESSION NEED NOT READ ANY STAGED FILE WHOLE.** These are **exemplars, not a corpus**: no
measurement is built, designed, scoped or run over them; **no count taken from them is evidence for a
statement**; and **no statement may rest on how often something occurs in them.** A score is here so
that a case can be met, not so that a case can be counted. **The session records in §6, for each staged
file, how much of it it read** — whole, or which parts, or none — **and a file it did not open is
recorded as unopened rather than left unmentioned.**

**Two notational cases the staged set does not contain, declared rather than left to be discovered: no
staged file carries a tremolo, and no staged file carries a pedal mark.** Where the session wants a case
the staged set does not supply — either of those or any other — it **writes the want as an open
question, names the face of §2 it belongs to, and does not fill it** — the pilot's own precedent for a
declared hole.

## 4. The form of every statement — six fields, one rule per statement

Atomic, because a paragraph cannot be compared against anything. Every statement carries all six
fields; a statement that cannot carry the sixth is marked UNVERIFIABLE rather than left to look
checkable.

1. **The statement** — what the analysis must do, or must be ABLE to do.
2. **The defense** — the music theory, the published research fetched and read, or the kind of
   measurement that would decide it, each load-bearing claim labelled FACT / THEORY / CONJECTURE.
   *"Because the current implementation does this"* is not available to this session and is not a
   defense; a statement supportable only by appeal to what software usually does is marked UNSUPPORTED.
3. **The source class** — *derived* (from theory or research), *given* (fixed by the charter, cited to
   the charter's own words), or *measured* (resting on a measurement this session cannot make — written
   with the measurement it would need, its establishment status UNESTABLISHED, and no value).
4. **The status** — *settled* or *open*.
5. **The premise it rests on, and that premise's false-negative path.**
6. **What would falsify it** — in CODE where the statement is behavioural (name the OBSERVABLE, the
   DECISION RULE over it, and the near-miss it is NOT falsified by); in the RESIDUAL where it is a
   modelling premise with no code site. Name observables in plain terms; leave code sites to a later
   session.

**★ THE *given* SOURCE CLASS IS NEW TO THIS SUBJECT AND IS THE ONE TO USE CAREFULLY.** It is for a
statement the charter already settles, restated here only because the specification would be incomplete
without it. **A *given* statement carries no defense of its own beyond the charter's words** — and a
session that finds itself marking many statements *given* should say so, because that is evidence the
charter has already answered the subject and the derivation is thinner than the phase expects.

**What cannot be settled is written as an open question, never filled with the most plausible reading.**

## 5. The measured-cost record

**Declared as this side's addition, not as a phase requirement** — the pilot's sizing already decided
this phase's ratification granularity, and nothing here re-opens it. It is kept because it is cheap and
because a later subject's budget is better set from two measurements than from one. Recorded as plain
counts and durations measured as the work goes, never reconstructed at the end: **time before the first
statement was written, separately from time spent writing statements**; **the number of statements and
the time per statement**; **the share marked *open***, and the share the session would put to the user
for a ruling, with the question each would ask; **the share marked *given***; **the share whose sixth
field could not be written**; **the share resting on a *measured* source class**; and **which pack
members and which fetched sources were actually consulted for each statement, with any pack member
consulted by no statement listed as such.** **No share is reported without its denominator, and no value
is estimated.**

## 6. The independence record

The output states: every file the session opened, pack members and fetched sources alike, the latter by
citation; every pack member it did not open, if any; the stop-on-meeting record of §3, or the positive
statement that it met no such passage; and **every place where it wanted notation and wrote an open
question instead** (§3).

**★ AND ONE REPORTING BOUND THAT COMES WITH P2's RULING.** Five papers bearing on this subject are
already read at the object and their extracts are pack members. **The session may fetch and read any of
those primaries — nothing bars it — but it records which of them it re-read and why**, so a later reader
can tell a check of a relayed extract from a duplication of work already done. *An extract is a relayed
reading, and a session that may not reach its primary must trust it, which #19 declines.*

**An output with no independence record is incomplete.**

## 7. The output, and what the session does NOT do

**One file for both charters**, written to the repository root, **named
`cowork_blind_derivation_l0_l1_2026_08_31.md`** (RULED, §8 (P4)), with the status banner
*DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED*. It is written for a reader who knows music
theory and not this project: terms explained at first use, predicates qualified, no invented labels,
music-theory words in their musical sense only.

**★ THE COMPARISON IS NOT THIS SESSION'S ACT.** The phase's method is derive-before-compare: the outgoing
texts are read as witnesses **only after each derived statement is written**, and every statement of
those texts is then given one of five recorded dispositions. **That is a later act with its own
instruction.** This session compares nothing, dispositions nothing, and must not go looking for the
documents it would compare against.

**What the session does NOT do:** it opens no untrusted source; it edits no specification and no code;
it runs no build, no test, no measurement tool; it creates, flips or discards no open-items row; it
allocates no register identity; it takes no branch rule and reads no commit log; it derives nothing on
any subject but §2's; and **it decides nothing about the derivation method itself**, which was ruled
established on a different unit.

**The deriving side is a fresh Cowork session.** The file is delivered to the repository root through
the device bridge, hash-verified after re-staging, and committed by a later dispatch. **The session
itself commits nothing, writes no `STATUS.md` entry, no handover block, no report and no close beyond
its own output file.**

## 8. The points the user rules before this brief is dispatched — ALL FIVE RULED

- **(P1) The deriving side's identity — RULED 2026-08-31:** **a fresh Cowork session** (Ruling 13, §3m).
  Applied in §7. **A session that has performed the ordinary session-start read is disqualified from
  deriving this subject**, on the ground recorded with the ruling: `CLAUDE.md`, which that read includes
  whole, describes how a key signature and a declared mode are read out of a MusicXML file, and that is
  implementation knowledge about L0's and L1's own subject.
- **(P2) Fetched research — RULED 2026-08-31: ALLOWED, UNBOUNDED** (Ruling 13, §3m). Applied in §3. The
  ground: the phase definition names published research fetched and read among this phase's inputs, so
  forbidding it would put the session outside the phase's own definition; and barring the session from
  the five primaries whose extracts are pack members would make those relayed extracts unfalsifiable
  inside the session that most depends on them (#19). **The reporting bound that came with it is at §6.**
- **(P3) Notation — RULED, across five rulings.** **The session MEETS NOTATION** (Ruling 15, §3o): the
  staged set spans notational phenomena named in advance from the charter's own open faces, each score's
  claim checked at the file before it is staged, and the set stays small — **exemplars, not a corpus**.
  Ruling 12's criterion over the chorale corpus had degenerated and its own overturn condition fired, so
  the set was built by checking named files instead. **The contrapuntal file was recovered from a
  container by extraction, unaltered** (Ruling 19, §3w), after a check over whole staves established that
  no two of its staves are copies. **The set is four files** (Rulings 22 and 23, §3ac and §3ad), each
  checked for annotation content, for duplicated staves, and for which build wrote it. **No file was
  dropped or shortened to reduce how much the session must read** (Ruling 24, §3ae). §3 carries the
  staged list, the two elements not read, and the permission to read a file in part.
- **(P4) The output — RULED 2026-08-31: ONE FILE for both charters, named
  `cowork_blind_derivation_l0_l1_2026_08_31.md`** (Ruling 13, §3m). Applied in §7. **The condition that
  came with it:** L0 and L1 are two charters, and if the deriving session finds they separate cleanly it
  **says so in its output**, leaving the split to the later act rather than to a decision taken now on
  no evidence.
- **(P5) The pack — RULED and RENDERED.** `tools/audit/derivation_boot_pack/l0-l1/` **exists and holds
  ten members**, rendered after Ruling 14's overturn condition fired and the generator was extended to
  carry a per-subject dimension (Ruling 16, §3p). Ruling 11's two mechanisms are in it: the charter
  member is leak-filtered, and the research extracts are section-cut. **The charter member was corrected
  after rendering** and re-rendered, so that §9.0 of the charter reads as settled rather than open
  (Ruling 8 as scoped by Ruling 18, §3g and §3r). **This blocker is cleared.**

## 9. Provenance — for the user and the record; NOT opened by the deriving session

Written by the Cowork writing side, 2026-08-31, in the session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. Its form follows
`cowork_blind_session_brief_scoring_model.md`, read whole at the file, whose §§0–7 structure, six-field
statement form, stop-on-meeting clause and independence record are reused deliberately so that two
subjects of the same phase are derived under the same instrument. **The additions declared as this
side's own:** the *given* source class of §4, which the pilot's subject did not need because nothing was
ratified above it; the §7 paragraph placing the comparison outside this session; and §5's framing as an
addition rather than a phase requirement.

**The subject statement and the faces of §2 were derived from `FRAMEWORK.md` §5's L0 and L1 charters and
its boundary-contract table, read whole at the file, together with §9's design points.** They are the
writing side's own decomposition of the charter's plain meaning, written to be answerable from the
domain; a session that finds the decomposition wrong says so. **No specification of this project's own
L0 or L1, and no code, was opened by the writing side in composing them** — `ARCHITECTURE.md`'s layer
sections were not read in this session.

The writing standards applied are `cowork_design_doc_template.md`'s two — predicates qualified, defined
terms and plain vocabulary. The fourteen-section structure does not bind this kind, and the kind is
stated so the exemption is not claimed by silence. The reserved-word conventions bind every line above.

**Amended 2026-08-31, second time (§3s of the same record, NOT a ruling — the user's deferral with a
caution).** §2's L0 subject question gained the requirement that the answer state **the criterion by which
a fact is admitted to L0's given list**, beside the list itself. **The amendment names no candidate fact
and discloses nothing of this project's record**: a list written closed would foreclose a later addition
by construction, while a stated test lets a later addition be judged against it. Nothing else moved.

**Amended 2026-09-01, third time — the staging amendment, after Rulings 15, 16, 19, 22, 23 and 24.**
The banner records that all five points of §8 are ruled and the pack exists. **§3's *no annotated scores
are staged* paragraph is REPLACED** by the staged list of four files, the two element names not read, the
permission to read a file in part with its recording requirement, and the two declared gaps. **§8's (P3)
and (P5) are brought to the rulings' state.** ***The former §3 wording, preserved:*** *"**No annotated
scores are staged** (Ruling 12, and §8 (P3) below). Where the session would have wanted notation in front
of it, it **writes the want as an open question, names the face of §2 it belongs to, and does not fill
it** — the pilot's own precedent for a declared hole."* **That last sentence survives inside the new
paragraph and is not withdrawn; only the first is.** **§§0–2, §§4–7 and everything of §9 above this note
are byte-unchanged.**

**What the staging paragraph deliberately does NOT say, declared because the omission is a choice.** It
does not say what any staged file contains, which face any of them serves, or why any was chosen.
**Naming the phenomenon a file was staged for would point at the conclusion this session is chartered to
derive** — the objection Ruling 12 upheld against its own declined option. **A bound on method is not a
pointer at content**, and the permission to read in part is a bound on method. The two declared gaps name
only vocabulary the session already holds from the charter and from §2.

**Amended 2026-08-31, after Ruling 13** (`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3m):
the banner records which points are ruled and which are not; **§6 gained the P2 reporting bound**; §7's
one name sentence was fixed by (P4) and its "one file" made explicit; and **§8 was brought to the
rulings' state**, with (P3) carrying what drafting this brief established about where notation would
have a job. **§§0–5, the whole of §7 but its one name sentence, and everything of §9 above this note are
byte-unchanged.** No point of §8 that was open before this amendment was closed by it except P1, P2 and
P4, which the user ruled.

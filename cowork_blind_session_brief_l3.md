# BRIEF for the blind deriving session — the L3 subject (the detail-specification phase's third derivation)

> **STATUS: DRAFT — WRITTEN 2026-10-17, NOT YET RELEASED.** It is released by the Cowork writing side once
> (i) its check at its sources has been run in a turn of its own and its corrections made, and (ii) it has
> been landed in git at the next Claude Code dispatch's Task 0. The L3 counterparts of the two conditions
> the L2 brief waited on are met on disk: the two cut input-contract files exist at their paths (§9), and
> the user ruled their cut list (Ruling 1 of the 2026-10-15 cut-lists record). **Whether those two files
> are committed in git was not checked by the writing side.** **The user opens the deriving session when the user chooses**; the writing side writes
> instructions to disk and never starts the sessions that run them.
>
> **Who reads this file, and when.** The deriving session reads it FIRST and ALONE, in the first message
> it is sent (§3a). Everything else the session may read arrives later and is named in §3. **The
> provenance at §9 is for the user and for a later reader; the deriving session does not open any file
> §9 names.**
>
> **★ THIS SESSION DERIVES INSIDE A RATIFIED CHARTER AND AGAINST A RATIFIED INPUT.** The layer's charter
> is **given**: not re-decided, not argued with, not improved upon. **So are the specifications of the
> layers beneath it**, which state what this layer receives (§3). **The session derives HOW the
> layer does what the charter says it does — never WHAT it does, and never what the layers beneath it
> publish.** Where the charter or the input contract is silent, the session derives; where either
> speaks, the session obeys and says so.

---

## ★★ BEFORE §0, BEFORE ANYTHING — DECLARE WHAT YOU WERE GIVEN AT BOOT

**Stop here and do this first. It is not a formality. Earlier sessions on this kind of work ended at
exactly this point, each through something that reached it before it could act.**

**★ YOU HAVE NO PROJECT FOLDER AND YOU MUST NOT ACQUIRE ONE.** This session is opened with **nothing
mounted**. **Everything you may read is ATTACHED to this conversation**, and **there is no other source you
may draw on inside this project.** You do not mount, connect, request or accept a project folder; you do
not list a directory; you do not run a shell over project material; you do not search for a project file.
**If a project folder becomes available to you at any point, that is not an opportunity — STOP and say
so.** The ground is at §3; it is named here because §3 is read too late for the acts it forbids, which
happen while a session is still orienting itself.

*Why. Earlier attempts at this kind of derivation were disqualified. One met roughly 250 document titles
while hunting for its brief — **file names are content**, and this project's titles announce its own
decomposition of the analysis. Another received this project's standing instructions file in full, because
the harness injects it for any session with the project folder connected. **Neither failed through its own
conduct**; each was booted into a room that contained more than it was allowed to see.*

**In your first message, before you read §0 and before you open anything at all, state everything that
was present in your context before your first act and that you did not fetch yourself** — an injected
memory index, a project note, a summary of prior decisions, a file the harness opened for you, anything
at all. **Quote it or describe it, and say how much of it you saw. Report ALL of it, the expected
material below included** — the report is part of your independence record (§6).

**★ HOW TO DO THIS, MECHANICALLY.** **Enumerate the blocks in your context ONE BY ONE and quote each
one's opening line.** Do not summarise a region as "the generic system prompt", "the usual scaffolding"
or "harness boilerplate" and move on: a repository file once sat nested inside a block that looked
generic, and a careful reader classified the block instead of reading it. **A block you have not quoted
the opening line of is a block you have not inventoried.**

**Then apply this test. It is a MATCHING test, not a judgment. Do not reason about whether what you
received matters.**

**EXPECTED MATERIAL — this and nothing else. It is NOT a stop:**

- **this brief, and — in message one — nothing else of this project.** It may already have been read
  into your context before your turn began; **that is expected** (§3a). Report it; do not stop on it.
- ordinary harness scaffolding with no project content: today's date, the timezone, tool and skill
  inventories, subagent listings, git-attribution boilerplate, generic product and behaviour guidance
- a note saying a computer is reachable, **provided no project folder is connected to you**

**The pack members, the two input-contract files, the scores and the analysis are NOT expected in message
one.** They arrive later (§3a). **If any of them is already present when you make this declaration, say
so** — it means the staging did not hold. That is a fact the user needs, though not by itself a stop,
those files being material you are entitled to.

**If everything you received matches that list: say so positively** — *"everything I received at boot is
on the expected list; no project folder is connected, no repository file reached me, and nothing else was
present"* — **and continue to §0.**

**If ANYTHING falls outside it: STOP.** Named because each has actually happened: **a `# claudeMd` block
or any other block carrying the contents of a repository file**; `CLAUDE.md` under any path, including a
staged or uploaded copy; **an injected memory index, a memory snapshot, or any summary of this project's
prior decisions**; a project-instruction note carrying any content at all; **a folder-context reminder
naming a connected project folder**; a file the harness opened for you. Do not read the rest of this
brief. Do not open anything. **Report what you received and its extent, and end there.** Whether it
disqualifies you is not yours to judge — **say what you got and stop.**

**If you are unsure whether something is on the list, it is not on the list. STOP.** And **if you later
discover you missed something in this inventory, say so at once and stop then** — a late correction is
worth far more than a tidy first answer.

**Why an allow-list.** A clause that stopped on *any* unfetched material could never be cleared, because
this harness has injected some scaffolding into every session observed so far. The allow-list narrows what
stops you; **it does not narrow what you report, and it hands you no judgment** — you match, you do not
assess. It works by detection, not prevention: **it cannot stop you being given something; it can stop you
deriving from it.**

## 0. Terms, explained before anything rests on them

A reader of this brief knows music theory and knows nothing about this project. Every project term is
explained here, once, before it is used; standard music theory is used in its standard sense.

- **The analysis** — the harmonic-analysis software this project builds: given a notated score, it
  decides the tonality, the chords, and the moments at which one chord gives way to the next, and reads
  further facts off that decision. **How it CURRENTLY does any of this is exactly what this session must
  not know.**
- **A deriving session** — one that writes what the analysis SHOULD do for one subject, from music
  theory, from published research, and from the ruled material it is given — WITHOUT reading what this
  project's code or this project's specifications say it DOES. Such a session is **implementation-blind**,
  or **blind**.
- **A layer** — one stage of the analysis, responsible for one question, consuming only what earlier
  layers published. **L0** is the notated record (not a layer: the input contract); **L1** finds the
  moments at which a harmony may begin and says what the notation shows at each; **L2** makes the one
  entangled decision — the tonality at each moment, where each harmony gives way to the next, which
  sounding notes belong to the harmony and which elaborate it, and the chord over each span; **L3** is
  this session's subject.
- **A charter** — the ratified statement of one layer's job: the question it answers, what it may
  consume, and what it publishes. Charters were derived and ratified in an earlier phase and are
  **given**.
- **The input contract** — the ratified specifications of the layers beneath L3: one file for L0 and L1,
  one file for L2. Together they state what L3 receives from the layers beneath it (§3.1). **Given.**
- **The boot pack** — the ten files that replace, for this session, everything this project would
  otherwise have a session read. §3 names them.
- **A statement** — one atomic sentence of the derived answer, in the six-field form of §4.
- **Mass** — the term the L2 input contract uses for the weight it publishes beside each rival reading.
  Its meaning is defined there and is not redefined here.
- **A slice**, **a change point**, **a span**, **a rival**, **an elaboration relation** — defined in the
  charter and in the input contract. They are not redefined here.
- **An exemplar** — a score, or a published analysis of one, staged so that a case can be MET; never a
  sample from which anything is counted (§3).
- **Tonality** — used for what is commonly called "the key". The bare word *key* means tonality and never
  a lookup key; *bar* is the metric unit, never *measure*; *score* means the musical score and never a
  number; *note* is a pitch event and never a remark; *figure* is the figure of a chord (its inversion or
  figured-bass figure) and never a number; *root* is a chord root and never an underlying cause;
  *resolution* is the resolution of a dissonance and never a level of detail.

## 1. What this session is for, in one paragraph

Derive, blind, **how the analysis should read, from a settled tonal reading and from what the notation
shows, the cadence at each phrase end with its type, the grouping of the music into phrases and sections,
the chord symbol, the figured bass and the harmonic rhythm — and how it publishes each of those facts with
its uncertainty** (§2). Write the answer as statements in the six-field form of §4, each carrying its
defense in the same breath. The session produces statements, open questions, a measured-cost record and
an independence record. **It produces no code, no comparison against anything this project already has,
no fitted value, and no verdict on anything this project currently does.**

## 2. The subject, in plain words

**L3's charter question, in the charter's own words:** *given a settled tonal reading, what else does a
harmonic analysis of this music say?* **What it publishes, in the charter's own words:** *the cadence at
each phrase end, with its type; the phrase and section grouping; the chord symbol — root pitch class,
quality and bass note; the figured bass; the harmonic rhythm.* The subject question:

> **How does this layer read each of those facts from what L0, L1 and L2 publish, in what form does it
> publish each fact and its uncertainty, and what does it never do?**

**The charter settles what L3 publishes and what it consumes, and it fixes three things about how**: the
chord symbol is a view and not a decision; the notated phrase evidence is read at L1 and which of it marks
a phrase end is decided at L3; and a read-off fact may never revise the decision it was read off. **The rest
is left to this derivation.**

The faces below are the writing side's decomposition of that question, listed so that none is silently
dropped. **The session is free to find the decomposition wrong and to say so.**

**(a) The chord symbol — root pitch class, quality, bass note.** The charter says it is a view computed
from L2's settled reading and that nothing is settled in computing it. What exactly is read from which
published L2 fact for each of the three parts; what the view does with a chord the L2 reading carries that
a chord symbol cannot express in those three parts; and how the view of a span is published beside L2's
rival readings of that span, so that it is never mistaken for a second decision.

**(b) Where a phrase ends.** The charter says which notated phrase evidence published by L1 marks a phrase
end is decided here, that the decisive further evidence is cadential, and that the phrase span's
boundaries come from the notated cues with the cadence aligned to them, not the reverse. What decides
whether a given piece of evidence is a phrase end; what evidence beyond the notated cues bears on it, and
from which layer; and how a rival placement of a phrase end is carried.

**(c) The cadence at each phrase end, and its type.** Which cadence types are read; how a type is read from
the chords L2 decided at a phrase end L3 decided; what happens at a phrase end where no cadence type
applies; and how L2's rival readings at that place bear on the cadence and its type.

**(d) The grouping of phrases into sections.** What groups phrases into sections, what evidence bears on
it, and how a rival grouping is carried.

**(e) The figured bass.** What the published figured bass is, which published facts it is read from, and
how it stands beside any figures the notation itself carries. **What L0 and L1 carry about notated figures
is given by the input contract; this session derives what L3 does with it and does not re-decide what L0
carries.**

**(f) The harmonic rhythm.** What the published harmonic rhythm is, at what grain, and which published
facts it is read from.

**(g) Uncertainty on every read-off fact.** The charter says every published fact carries its own mass and
its own establishment status, with no separate uncertainty layer. How does each L3 fact carry its
uncertainty, and how does a fact read off L2's committed reading relate to L2's rivals and their mass?

**(h) The boundaries of the layer.** L3 consumes what L0, L1 and L2 publish and nothing else, and may not
revise L2. What L3 does where it wants something a layer beneath it does not publish, or publishes in a
form it cannot use — **that is an open question naming the input-contract statement concerned; L3 never
re-derives a fact a layer beneath it publishes.** And what L3 does where the working span is only part of a
piece.

**Scope.** Common-practice tonal music as notated in a score. **The tonality, the segmentation, the chord
per span, the chord-tone assignment and the elaboration relation are L2's and OUT of scope** — given by
the L2 input contract. **The voice-leading axis described in the charter is OUT of scope**, and so is the
measurement of the analysis. Where a statement here depends on one of them, the dependency is written as a
statement in its own right.

## 3. What the session reads — and the one rule that matters most

**★ EVERYTHING YOU MAY READ IS ATTACHED TO THIS CONVERSATION. NOTHING IS MOUNTED.** There is no project
folder, no device bridge and no repository path. **Your whole read of this project is: this brief, the
ten boot-pack members, the two input-contract files, and the three exemplar files below.** Open the pack
member named `00_READ_THIS_FIRST.md` first among the pack members; it names them and the order to read
them. **The ordinary session-start read of this project is REPLACED, for you, by the pack.** You take no
branch rule, read no commit log, and run nothing.

**Nothing else of this project is opened**, and with nothing mounted there is nothing else you *could*
open: not this project's other specifications, not its architecture document, not its registers, not
any session handoff, dispatch or report, and **above all not any document stating how this project's
analysis currently reads a cadence, a phrase, a section, a chord symbol, a figured bass or a harmonic
rhythm.**

**★ AND YOU DO NOT GO LOOKING.** You do not mount, connect, request or accept a project folder. You do
not list directories. You do not run a shell over project material. You do not search for a project file
by name or by pattern. **Every file you may read is attached and named, so you never need to hunt for
one — and if you find yourself hunting, you have already gone wrong: stop and say so.**

### 3.1 The input contract — two files, given, not re-derived

**`the_l0_l1_specification_the_input_contract.md`** is the ratified specification of L0 and L1, and
**`the_l2_specification_the_input_contract.md`** is the ratified specification of L2. Each is cut for this
session: **passages stating this layer's own ratified or current design have been removed from it**, and
each says so at its head. Together they are the authority on what this layer receives.

- **What L1 publishes** is listed in the L0/L1 file's statement S-50, which says of itself that the list
  is exhaustive; so an absence from that list means L1 does not publish it.
- **What L2 publishes to L3** is stated in the L2 file's statement L2-S45. Read that statement whole,
  including what it says about how its list is to be read.
- A statement of this derivation that uses a published fact of a layer beneath it **cites the
  input-contract statement that publishes it**, and its source class for that part is *given*.
- **Where this session wants something a layer beneath it does not publish, it writes an open question
  naming the input-contract statement that would have to change, and does not fill it.** It does not
  supply the fact by deriving it from the notation or from L2's reading itself: that would be L3
  re-deriving a fact of another layer, which the charter's layer rule forbids.
- The input contract carries identifiers of rulings and decisions standing without content. **Those are
  not pointers you can follow**, and a missing passage is **not** evidence of anything. Do not try to
  reconstruct what was cut.
- The L2 file in places names L3 or says something is left to L3. **Where it does, read it as a statement
  about what L2 hands over, not as a statement of L3's design** — L3's design is what this session derives.

### 3.2 The exemplars — three files, by name

**The session may open these three files, and no other score or analysis:**

| # | File name as attached | What it is |
|---|---|---|
| 1 | `K545-1.mscx` | a notated score **carrying a published analysis inside it** |
| 2 | `analysis_DT.txt` | a second, independent published analysis **of the same piece as file 1** |
| 3 | `op01n08a.mscx` | a notated score **carrying a published analysis inside it** |

**The analyses are what competent human analysts decided about these pieces.** They are in front of you
because L3's question is, in large part, a question they answer. **Read them as the decisions of analysts,
not as a standard this layer is graded against**: grading is a later stage's business and not this
session's.

**Where the analysis sits in each file, and what may be read.**

- **Files 1 and 3:** the published analysis is carried in the score file's `<Harmony>` elements,
  attached to the music. **The session MAY read the `<Harmony>` elements of files 1 and 3**, and every
  other element of those files, including any figures the notation carries.
- **File 2:** a plain-text analysis in its own notation, which the file's own header and syntax explain.
  **Read it whole or in part as needed.** Its bar numbers are its own; establishing how they align with
  file 1 is part of reading it, and any assumption about the alignment is stated.

**★ EXEMPLARS, NOT A CORPUS. THIS BINDS HARDEST ON FILES 1 AND 2.** No measurement is built, designed,
scoped or run over these files; **no count taken from them is evidence for a statement**; **no statement
rests on how often something occurs in them**; and in particular **no count may rest on the two readings
of file 1's piece** — they are there to show that competent readers disagree, never to measure how often.
A file is here so that a case can be met, not so that a case can be counted.

**★ THE SESSION NEED NOT READ ANY EXEMPLAR WHOLE.** It records in §6, for each exemplar, how much it
read — whole, which parts, or none — **and a file it did not open is recorded as unopened rather than
left unmentioned.**

**Nothing is said here about which case any exemplar exhibits, or why each was chosen.** Naming the
phenomenon a file was chosen for would point at the conclusion this session is chartered to derive. Read
the files and find in them whatever is there.

**Where the session wants a case no staged file supplies, it writes the want as an open question, names
the face of §2 it belongs to, and does not fill it.**

## 3a. ★★ HOW YOUR MATERIAL ARRIVES, AND HOW MUCH OF IT YOU CAN HOLD

**You are given your material IN STAGES, and this brief arrives ALONE and FIRST.**

1. **Message one carries this brief and nothing else.** You read it, perform the block-by-block boot
   inventory demanded before §0, and **declare. Then you stop and wait.** You do not ask for the rest,
   you do not look for it, and you do not begin §2.
2. **The rest follows in a later message**: the ten pack members, the two input-contract files, and the
   three exemplars — fifteen files. When they have arrived you read `00_READ_THIS_FIRST.md` first among
   the pack members, then the members in the order it gives, then the input contract, then the exemplars
   as you need them.

**★ EXPECT THE FILES TO ARRIVE ALREADY PARTLY READ. THIS IS NORMAL AND IS NOT A STOP.** This harness
places an attached file's contents into a session's context **before that session's first turn**,
without the session issuing any call and **in an order nobody chose.** On a prior run on record, some
files arrived pre-read whole, two long files arrived pre-read **to their first 2,000 lines only**, and some
files were not pre-read at all and were opened by the session itself. **Do not assume any file was
delivered to you whole; check.** So:

- **A file arriving pre-read, whole or in part, is EXPECTED and is not a stop.** It is still reported in
  §6, by name and by how much you saw.
- **A file you did not expect at all is still a STOP**, pre-read or not — anything that is not this
  brief, a named pack member, one of the two input-contract files, or one of the three exemplars.
- **You still never fetch, mount, list or search for anything.** Waiting is correct when something has
  not arrived; hunting is not.

**★ JUDGE YOUR CAPACITY BEFORE YOU COMMIT IT, AND SAY SO IN YOUR OUTPUT.** The largest files you are
given are the L2 input-contract file (about 218 KB, more than 2,000 lines), the pack's design-intent
member `05_the_ratified_design_intent.md` (about 266 KB) and the L0/L1 input-contract file (about 142 KB).
The research-extracts member, `08_the_seventeen_research_extracts.md`, is about 119 KB and carries
seventeen sources, each under its own heading. **You need not read any of these whole in one pass. Read
them as your statements need them, and record in §6 what you read whole, what in part, and what not at
all** — the extracts member source by source. A source you did not read yields no statement. **Do not
start reading any file you cannot finish in the capacity you have left**; if capacity runs short, stop at
a statement boundary, deliver what is finished as finished, and list what is not.

**Beyond the repository, the session MAY fetch and read published research** — peer-reviewed papers,
published algorithms, public documentation — and MUST label every load-bearing claim it takes from them
FACT (stated or measured in a paper actually fetched and read), THEORY (established published theory),
or CONJECTURE. **A source that could not be fetched yields no statement**; the gap is recorded.

**★ THE STOP-ON-MEETING CLAUSE.** If anywhere — in the pack, in the input contract, or in this brief —
you meet a statement about how THIS project's analysis currently does any part of §2's subject:

- **If you are reading the file yourself and have not yet passed the statement: STOP READING THAT FILE
  AT THAT POINT.** Continue with the remaining files.
- **If the file was already in your context when your turn began, you cannot stop before seeing it, and
  no fault attaches to you for that.** Record it instead.

**Either way, record in §6: which file, where in it (by line or by heading), and how much of it you
saw.** Do not delete, paraphrase or reason about what you saw, and **do not let it enter a statement.**
**A session whose output carries no such record, and no positive statement that nothing was met, is
incomplete.**

## 4. The form of every statement — six fields, one rule per statement

Atomic, because a paragraph cannot be compared against anything. Every statement carries all six
fields; a statement that cannot carry the sixth is marked UNVERIFIABLE rather than left to look
checkable.

1. **The statement** — what the analysis must do, or must be ABLE to do.
2. **The defense** — the music theory, the published research fetched and read, or the kind of
   measurement that would decide it, each load-bearing claim labelled FACT / THEORY / CONJECTURE.
   *"Because the current implementation does this"* is not available to this session and is not a
   defense; a statement supportable only by appeal to what software usually does is marked UNSUPPORTED.
3. **The source class** — *derived* (from theory or research), *given* (fixed by the charter or by the
   input contract, cited to its own words), or *measured* (resting on a measurement or a fit this session
   cannot make — written with the measurement or fit it would need, its establishment status
   UNESTABLISHED, and no value).
4. **The status** — *settled* or *open*.
5. **The premise it rests on, and that premise's false-negative path.**
6. **What would falsify it** — in CODE where the statement is behavioural (name the OBSERVABLE, the
   DECISION RULE over it, and the near-miss it is NOT falsified by); in the RESIDUAL where it is a
   modelling premise with no code site. Name observables in plain terms; leave code sites to a later
   session.

**★ THE *given* SOURCE CLASS HAS THREE SOURCES HERE** — the charter, the L0/L1 input contract and the L2
input contract. A statement one of them already settles is *given* and carries no defense of its own
beyond that source's words. **A session that finds itself marking many statements *given* should say
so**, because that is evidence the subject has already been answered and the derivation is thinner than
the phase expects.

**★ A *measured* VALUE IS NEVER SUPPLIED.** Where an L3 fact would need a value fitted from annotated
music, **no such value is given, guessed or borrowed from a paper as though it were this analysis's own**;
the statement says what would have to be fitted, on what, and with what held back for evaluation.

**What cannot be settled is written as an open question, never filled with the most plausible reading.**

## 5. The measured-cost record

**Declared as the writing side's addition, not as a phase requirement.** Recorded as plain counts and
durations measured as the work goes, never reconstructed at the end: **time before the first statement
was written, separately from time spent writing statements**; **the number of statements and the time per
statement**; **the share marked *open***, and the share the session would put to the user for a ruling,
with the question each would ask; **the share marked *given***, split by charter, L0/L1 input contract and
L2 input contract; **the share whose sixth field could not be written**; **the share resting on a
*measured* source class**; and **which pack members, which input-contract statements, which exemplars and
which fetched sources were actually consulted for each statement, with any pack member consulted by no
statement listed as such.** **No share is reported without its denominator, and no value is estimated.**

## 6. The independence record

The output states: every file the session opened, pack members, input-contract files, exemplars and
fetched sources alike, the last by citation, **each with the extent read** (the extracts member source by
source, §3a); every file it did not open; the stop-on-meeting record of §3a, or the positive statement
that it met no such passage; and **every place where it wanted a case or a published fact of a layer
beneath it and wrote an open question instead** (§3.1, §3.2).

**One reporting bound.** Seventeen sources bearing on this subject are already read at the object and
their extracts are pack member 8. **The session may fetch and read any of those primaries — nothing bars
it — but it records which it re-read and why**, so a later reader can tell a check of a relayed extract
from a duplication of work already done.

**An output with no independence record is incomplete.**

## 7. The output, and what the session does NOT do

**One file, named `cowork_blind_derivation_l3_2026_10_17.md`** (the date is this brief's, fixed in
advance, and says nothing about when the session runs), with the status banner
*DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED*. It is written for a reader who knows music
theory and not this project: terms explained at first use, predicates qualified, no invented labels,
music-theory words in their musical sense only. **Its sections:** terms; the subject and any finding on
the decomposition of §2; the statements, face by face; the open questions; the measured-cost record (§5);
the independence record (§6); and where this brief's decomposition seemed wrong or incomplete.

**★ THE COMPARISON IS NOT THIS SESSION'S ACT.** The phase's method is derive-before-compare: this
project's existing texts are read as untrusted sources **only after each derived statement is written**,
in a later act with its own instruction. This session compares nothing, dispositions nothing, and must
not go looking for the documents it would compare against.

**What the session does NOT do:** it opens nothing beyond §3; it edits no specification and no code; it
runs no build, no test and no measurement tool; **it fits no value**; it creates, flips or discards no
open-items row; it allocates no register identity; it takes no branch rule and reads no commit log; it
derives nothing on any subject but §2's; **it re-derives nothing the input contract states**; and it
decides nothing about the derivation method itself.

**The deriving side is a fresh Cowork session with NOTHING MOUNTED. So the file is DELIVERED INTO THIS
CONVERSATION, not written to any repository path** — the session has no path to write to and must not
seek one. **The user places it; a later dispatch commits it.** The session commits nothing and writes no
status entry, no handover, no report and no close beyond its own output file.

**Write it whole and deliver it once, finished** — or, if capacity forces a stop (§3a), deliver what is
finished with the unfinished faces listed by name. A file delivered in pieces cannot be checked against
§6 as one object.

## 8. The points this brief rests on

- **(P1) The deriving side's identity — a fresh Cowork session, nothing mounted.** Carried from the L0+L1
  brief, where it was ruled (Ruling 13 of 2026-08-31) and amended (2026-09-01, the nothing-mounted
  ruling), and carried to the L2 brief unchanged. **A session that has performed this project's ordinary
  session-start read is disqualified.**
- **(P2) Fetched research — allowed, unbounded**, with the reporting bound at §6. Carried the same way.
- **(P3) Notation and annotation — RULED.** Two scores with their published analyses inline and a second
  published analysis of one of them, chosen for named L3 phenomena, each claim checked at the file (Ruling
  6 of the 2026-10-15 boot-list record; the Ruling of the 2026-10-15 staged-score-set record, option B, its
  condition checked and met).
- **(P4) The output — one file**, on the L0+L1 and L2 precedent; its name at §7.
- **(P5) The pack — RULED and RENDERED** (Rulings 1, 3, 4 and 5 of the 2026-10-15 boot-list record; Ruling 1 of
  the 2026-10-15 first-pass-extracts record; the 2026-10-14 and 2026-10-15 withheld-family records; Ruling
  1 of the 2026-10-15 withheld-documents confirmation record; Ruling 1 of the 2026-10-17 lists record).
- **(P6) The input contract — RULED** (Ruling 2 of the 2026-10-15 boot-list record; Ruling 1 of the
  2026-10-15 cut-lists record).

*(P1, P2 and P4 were not put to the user again for L3. The 2026-09-05 L2 boot-list record states they were
"expected to carry over from `l0-l1` unchanged and were not re-decided", and the L3 rulings follow L2's
shape throughout; no record read by the writing side changes them.)*

## 9. Provenance — for the user and the record; NOT opened by the deriving session

Written by the Cowork writing side, 2026-10-17, in the session that booted on
`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixteen.md` and performed the ordinary
session-start read. **Its form follows `cowork_blind_session_brief_l2.md`, read whole at the file**, which
itself reused the L0+L1 brief's before-§0 declaration, staged delivery, six-field statement form,
stop-on-meeting clause and independence record, so that the phase's subjects are derived under the same
instrument. The ruling behind the L2 brief, `records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md`,
was read whole.

**The changes from the L2 brief, declared as this side's own:** the input contract is two files rather
than one (§3.1), with L2-S45 named as the L2 file's publication statement and the reading rule for the
L2 file's mentions of L3; the exemplar set is three files, every element of which may be read (§3.2),
applying the staged-score-set ruling, which carries no plain-score set; the capacity clause names the
large files by their sizes at this side's staging (§3a); the *given* class has three sources (§4); faces
(a) to (h) of §2 are new.

**The subject statement and the faces of §2 were derived from the L3 charter and the boundary-contract
table as the pack renders them** (`tools/audit/derivation_boot_pack/l3/07_the_charter_the_layers_and_the_decisions.md`,
the L3 section and the contract table, read at the file). **No specification of this project's own L3 and
no code was opened by the writing side in composing them.** The writing side has read this project's
decisions register index, which names several ratified decisions bearing on L3's subject in outline, and
the L2 input-contract file at its statement L2-S45 and its opening; the faces are written to name
questions and not answers, and the user is asked to read them with that in mind.

**What this brief deliberately does NOT say, declared because the omission is a choice.** It does not say
which case any exemplar exhibits or why any was chosen. It does not say what the passages cut from the
input contract or from the pack were about. It does not say what the two readings of file 1's piece
disagree about.

**Sources for the staged set** (not opened by the deriving session). **The user attaches them by name**
from these paths, as for L2 (entry 254 §4 step 4 describes L2's boot this way; `tools/audit/derivation_exemplars/l2/`
held no score at this side's listing, so that L2's scores were attached from their source paths is this side's
reading): file 1 at
`tools/dcml/mozart_piano_sonatas/MS3/K545-1.mscx`; file 2 at
`tools/dcml/when_in_rome/Corpus/Piano_Sonatas/Mozart,_Wolfgang_Amadeus/K545/1/analysis_DT.txt`; file 3 at
`tools/dcml/corelli/MS3/op01n08a.mscx`. K545's `analysis.txt` is **not** attached. The input contract is at
`tools/audit/derivation_exemplars/l3/the_l0_l1_specification_the_input_contract.md` and
`tools/audit/derivation_exemplars/l3/the_l2_specification_the_input_contract.md`; the pack is the ten files
of `tools/audit/derivation_boot_pack/l3/`.

### 9.1 The check at its sources, 2026-10-17 — run in a turn of its own after the first landing

**Checked at the objects and found to hold:** the ten pack files and their names (the `l3` pack directory's
listing); the extracts member's seventeen sources, each under its own top-level heading (a heading search of
that member); the file sizes §3a gives; the L2 input-contract file running past line 2,000; S-50's
exhaustiveness sentence and S-8 standing in the L0/L1 cut copy; L2-S45 standing in the L2 cut copy, and
*mass* defined in that copy; the charter's words quoted in §2 (pack member 7, the L3 section and the
contract table); the Corelli score carrying both `<Harmony>` and `<FiguredBass>` elements (an element search
of the file); the quotation in §8 from the 2026-09-05 L2 boot-list record.

**Six corrections, made at their sites. The former wordings, kept (#12):**

1. The banner said: *"Both conditions the L2 brief waited on — the input contract landed and cut, and the
   user having seen and ruled its cut list — **already hold for L3** (§9)."* "Landed" claimed a git commit
   this side never checked.
2. The banner said: *"which state exactly what this layer receives"*. L2-S45 is ruled not to be a closed
   list, so "exactly" overstated it.
3. §0 said: *"Together they state exactly what L3 receives (§3.1)."* The same overstatement, and L3 also
   consumes L0 directly.
4. §2 said: *"It deliberately leaves the rest to this derivation."* The charter states no intention; that
   was this side's reading.
5. §8 P5 said: *"Rulings 1 to 5 of the 2026-10-15 boot-list record"*. Ruling 2 is the input contract
   (P6), not the pack.
6. §9 said: *"(entry 254 §4 step 4; no Claude Code batch staged L2's scores)"*. The ground offered for the
   second half, the L2 landing report's "Nothing was staged", is about git's staging area, not about
   scores. The sentence now gives the evidence actually held and marks the conclusion as a reading.

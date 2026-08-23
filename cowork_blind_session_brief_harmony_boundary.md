# BRIEF for the blind deriving session — the harmony-boundary subject (the held-out test of the pilot)

> **STATUS: RULED 2026-08-23.** Written by the writing side (Cowork, 2026-08-22, the
> forty-fourth Cowork session) while the pilot-preparation batch
> (`cc_instruction_pilot_preparation_withheld_family.md`) was running on the coding side; refreshed
> to the ruled state by the writing side on 2026-08-23. **It dispatches nothing and boots no
> session.** Both conditions it named are now met: the user has ruled the withheld family at the
> reading file (`cowork_rulings_2026_08_22_withheld_family_sitting.md`, applied and corrected at
> the objects), and the user has ruled this brief — every point of §8 is RULED
> (`cowork_rulings_2026_08_23_brief_validation_sitting.md`). **This is the brief the blind session
> reads; the user opens that session when the user chooses.**
>
> **Who reads this file, and when.** The deriving session reads it FIRST, before it opens the boot
> pack. Everything the session is allowed to read is named in §3; **this brief and that directory
> are the session's whole read, and nothing else in the repository is opened.** The provenance at
> the foot (§9) is for the user and for a later reader of the record; **the deriving session does
> not open any file §9 names.**

---

## 0. Terms, explained before anything rests on them

A reader of this brief knows music theory and knows nothing about this project. Every project
term is explained here, once, before it is used; standard music theory is used in its standard
sense throughout.

- **The analysis** — the harmonic-analysis software this project builds: given a notated score, it
  decides the tonality, the chords, and the moments at which one chord gives way to the next, and
  writes the result into the score as Roman numerals and chord symbols. How it CURRENTLY does any of
  this is exactly what this session must not know.
- **A deriving session** — a session (a Claude Code session or a Cowork session; the user decides
  which) that writes what the analysis SHOULD do for one subject, from music theory, from published
  research it fetches and reads, and from the ruled design intent it is given — WITHOUT reading what
  the project's code or the project's specifications say the analysis DOES. Such a session is called
  *implementation-blind*, or *blind* for short.
- **The boot pack** — the one directory a deriving session reads at boot, generated from a ruled
  reading list and containing six rendered files plus a read-me. It is self-contained by
  construction: every file in it was judged free of statements about how the analysis currently
  works. §3 names the directory.
- **The subject** — the one question this session derives an answer to. It is stated in §2.
- **A statement** — one atomic sentence of the derived answer, in the six-field form of §4. The
  derived answer is a set of statements, not a paragraph.
- **The held-out test** — the reason this session exists. The user has already ruled, on an earlier
  date, what the analysis should do on this subject. That ruling is WITHHELD from this session. After
  the session has written its statements, a separate later session compares them against the withheld
  ruling. If the blind derivation reproduces the ruled intent, or produces a defended alternative the
  user would rank beside it, the derivation method is established; if it produces nothing usable, the
  method is refuted. **The session is told this so it understands why it is kept blind, and for no
  other reason: nothing about the withheld ruling's content is, or may be, inferred from this brief.**
- **The untrusted sources** — the project's current specification text and the code. They are
  opened by the later comparison session, never by this one.
- **Tonality** — used throughout for what is commonly called "the key". In this project the bare
  word *key* is reserved for tonality and is never used for a lookup key or a map key; *bar* is used
  for the metric unit, never *measure*; *score* means the musical score and never a number.

## 1. What this session is for, in one paragraph

Derive, blind, what the analysis should do to decide **where one chord ends and the next begins** in
a notated score, and **what evidence decides it** — and write that answer as statements in the
six-field form, each carrying its defense in the same breath, so that a later session can compare
each statement against the withheld ruling and against the untrusted sources. The session produces
statements and open questions. It produces no code, no specification edit, no comparison, and no
verdict on anything the project currently does.

## 2. The subject, in plain words

**How should a harmonic analysis of a notated score decide the moment at which one chord ends and
the next begins, and what evidence should decide it?**

The question has at least these faces, listed so none is silently dropped; the session is free to
find the list incomplete and to say so:

- **The grain.** What is the smallest stretch of music at which the question "which chord is
  sounding?" is asked at all — and is that grain fixed by the notation (every moment at which any
  note starts or stops; the beat; the bar) or decided by the music?
- **The boundary decision itself.** Given that grain, by what rule are adjacent stretches joined
  into one chord or kept apart as two? Is the decision made stretch by stretch, or over the whole
  passage at once? Is it made before, after, or together with the decision of which chord and which
  tonality?
- **The evidence.** What counts, and in what order of strength, when the evidence disagrees: the
  notes actually sounding (including notes struck earlier and still held), the notes struck at the
  moment, the bass, the notated durations and the metric position, the notated spelling, the
  surrounding chords, the prevailing tonality, the notated key signature, and anything else the
  session can defend from theory or research. Which of these may decide a boundary, which may only
  tie-break, and which may never be consulted?
- **Non-chord tones and ornamentation.** How are passing tones, neighbor tones, suspensions,
  anticipations, pedal points and arpeggiation kept from producing spurious boundaries, or from
  hiding real ones — and is that a separate step, or part of the one decision?
- **What is published.** Does the analysis commit one boundary set, or carry alternatives with their
  relative strength; and what does it do where the evidence is genuinely ambiguous?

**Scope.** Common-practice tonal music as notated in a score, of the kind for which published
Roman-numeral analyses exist. Harmonic rhythm in the broad sense — the chord-change rate — is IN
scope only insofar as it bears on locating boundaries; phrase structure, cadence classification and
the labelling of chords are OUT of scope except where a boundary decision depends on them, in which
case the dependency is stated as a statement in its own right.

## 3. What the session reads — and the one rule that matters most

**The session's whole read is this brief and the directory
`tools/audit/derivation_boot_pack/harmony-boundary/`.** Open its `00_READ_THIS_FIRST.md` first; it
names the six files and the order in which to read them. Nothing outside that directory is opened:
not the project's other governing documents, not the specifications, not the code, not the
open-items register or the decisions register, not any session handoff, dispatch or report. **The
ordinary session-start read of this repository is REPLACED, for this session, by the pack** — that
is a ruled departure, recorded by the user, and the session does not take the branch rule, read the
commit log, or run anything.

**Beyond the repository, the session MAY fetch and read published research** — peer-reviewed papers,
published algorithms, public datasets' documentation — and MUST label every load-bearing claim it
takes from them as the pack's principles prescribe (FACT where the paper actually fetched and read
states or measures it; THEORY where it is established published theory; CONJECTURE otherwise). **A
source that could not be fetched yields no statement**; the gap is recorded instead.

**The annotated scores — staged to the session by name, and nothing else of the corpus (ruled
2026-08-22).** Beside the brief and the pack, the writing side stages these files to the session,
each by its own name and never a directory: for each of the three Bach chorales the project's
snapshot suite already holds — Riemenschneider numbers 001 *Aus meines Herzens Grunde*, 003
*Ach Gott, vom Himmel sieh darein*, 137 *Du, o schönes Weltgebäude* — the score as a MuseScore
XML file (`tools/dcml/bach_chorales/MS3/<number> <title>.mscx`, which carries the notes and no
harmonic annotation), and the published human analysis of the same chorale from the *When in Rome*
anthology (`tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/<number>/analysis.txt`
in RomanText — and, for chorales 001 and 003 only, the `analysis_BCMH.txt` beside it; chorale 137
has none). These are the annotators' own readings as published — the RomanText files name their
analyst and proofreaders and place every chord change at a bar and beat, and some carry the
analyst's own alternative readings marked as variants; nothing the project's analysis wrote is staged, and the session treats the annotation
as what it is — one published human reading, graded against in this project, not a specification.
The three chorales were chosen because they are the snapshot suite's Bach members, selected long
before this test for another purpose; the session may note that three chorales are a narrow
sample and say what it could not test on them.

**The admitted-facts hole, declared.** The pack carries no ledger of empirically established facts
about this project's own data. The session therefore works with none; where it would have wanted
one — a fact about the annotated corpus, a measured rate — it writes the want as an open question and
does not fill it.

**★ THE STOP-ON-MEETING CLAUSE.** If, anywhere in the pack or in this brief, the session meets a
statement about how THIS project's analysis currently decides chord boundaries, or ranks evidence
for that decision — or any statement it recognises as the user's ruled answer to the subject — it
**STOPS READING THAT FILE AT THAT POINT** and records, in its output's independence record (§6),
which file, where in it, and how much of the statement it saw before stopping. It then continues
with the remaining files. It does not delete, paraphrase or reason about what it saw. This record is
what lets the session's blindness be judged rather than assumed; a session whose output carries no
such record, and no positive statement that nothing was met, is incomplete.

## 4. The form of every statement — six fields, one rule per statement

Atomic, because a paragraph cannot be compared against anything. Every statement carries all six
fields; a statement that cannot carry the sixth is marked UNVERIFIABLE rather than left to look
checkable.

1. **The statement** — what the analysis must do, or what it must be ABLE to do (a requirement that
   the implementation not preclude something is a statement of this class).
2. **The defense** — the music theory, the published research fetched and read, or the kind of
   measurement that would decide it, each load-bearing claim labelled FACT / THEORY / CONJECTURE.
   "Because the current implementation does this" is not available to this session and is not a
   defense; a statement the session finds it can support only by appeal to what software usually
   does is marked UNSUPPORTED.
3. **The source class** — *derived* (from theory or research), *salvaged* (taken from a ruled
   design-intent entry in the pack, cited by its identifier), or *measured* (a claim that rests on a
   measurement — which this session cannot make, so any such statement is written with the
   measurement it would need, its establishment status UNESTABLISHED, and no value).
4. **The status** — *settled* (the session defends it without reservation) or *open* (the session
   states both readings and cannot choose on the declared sources).
5. **The premise it rests on, and that premise's false-negative path** — the assumption about the
   music or about the analysis that the statement silently needs, and the case in which that
   assumption would be false without the statement showing it. A statement with no premise says so
   explicitly.
6. **What would falsify it** — in CODE where the statement is behavioural (the session names the
   OBSERVABLE a later reader would look at, the DECISION RULE over it, and the near-miss the
   statement is NOT falsified by); in the RESIDUAL — the pattern of disagreement with human
   annotation — where the statement is a modelling premise that has no code site. The session
   cannot name code sites; it names the observable in plain terms and leaves the site to the
   comparison session.

**What cannot be settled is written as an open question, never filled with the most plausible
reading.**

## 5. The sizing record the session keeps

Beside the statements, the session records, as plain counts and durations it measured itself and
nothing it estimated:

- the time spent per statement, and the number of statements;
- the share of statements marked *open*, and the share the session would put to the user for a
  ruling (with the question each would ask);
- the share whose sixth field could not be written (marked UNVERIFIABLE);
- **the noise measurement** — which files of the pack, and which fetched sources, the session
  actually consulted while writing each statement; a pack file consulted by no statement is listed
  as such.

No share is reported without its denominator.

## 6. The independence record

The output states: every file the session opened (pack files and fetched sources alike, the latter
by citation); every pack file it did not open, if any; and the stop-on-meeting record of §3 — or
the positive statement that it met no such passage. **An output with no independence record is
incomplete.**

## 7. The output, and what the session does NOT do

**One file.** The session writes its statements, open questions, sizing record and independence
record to ONE new file at the repository root, whose name the user fixed on 2026-08-23 (Ruling 3 of the brief-validation sitting):
**`cowork_blind_derivation_harmony_boundary_2026_08_23.md`**, with the status banner *DRAFT — BLIND
DERIVATION, NOT COMPARED, NOT RATIFIED*. It is written for a reader who knows music theory and not
this project: terms explained at first use, predicates qualified (every "depends", "prefers",
"strongest" names its argument), no invented labels, music-theory words in their musical sense only.

**The deriving side is a fresh Cowork session (ruled 2026-08-22).** The file is delivered to the
repository root through the device bridge, hash-verified after re-staging, and committed by the
next ordinary dispatch with a subject that states no verdict and names no comparison. The session
itself commits nothing, runs nothing and writes nothing else: no `STATUS.md` entry, no handover
block, no report, no close, no guard run. *(The Claude Code form this paragraph carried in the
first draft was declined by the user's ruling; the record is
`cowork_rulings_2026_08_22_deriving_side_sitting.md`, Ruling 1.)*

**What the session does NOT do**, stated so nothing is read into silence: it opens no untrusted
source; it compares nothing against anything; it edits no specification and no code; it runs no
build, no test, no measurement tool; it creates, flips or discards no open-items row; it allocates
no finding number; it takes no branch rule and reads no commit log; it derives nothing on any
subject but the one in §2; it does not decide the deriving method's fate — that is the user's
ruling, on the comparison session's evidence, later.

## 8. The points the user rules before this brief is dispatched — ALL RULED as of 2026-08-23

- **(P1) The deriving side's identity — RULED:** a fresh Cowork session
  (`cowork_rulings_2026_08_22_deriving_side_sitting.md`, Ruling 1). Applied in §7.
- **(P2) Fetched research — RULED:** allowed, as §3 is written (Ruling 2 of
  `cowork_rulings_2026_08_23_brief_validation_sitting.md`). The ground: the pilot's ruled inputs
  are independent sources and fetched literature, and a session forbidden research would test a
  different method from the one under test.
- **(P3) Annotated scores — RULED:** the repository's own human-annotation files, staged by name
  (same record, Ruling 3). Applied in §3 with the file list. **The route is settled:** the *When in
  Rome* analysis files sit eight folders below the repository folder and the device bridge stages at
  most seven deep, so the user connected the chorale folder
  `C:\s\MS\tools\dcml\when_in_rome\Corpus\Early_Choral\Bach,_Johann_Sebastian\Chorales` directly in
  the desktop app on 2026-08-22; the five annotation files were then staged and opened by the
  writing side (chorale 137 has no BCMH file). The blind session's desktop must connect the same
  folder, and the repository folder for the three `.mscx` scores and the pack.
- **(P4) The output file's name — RULED:** `cowork_blind_derivation_harmony_boundary_2026_08_23.md`
  (Ruling 3 of the same record). The commit route is settled by Ruling 1 of the deriving-side
  sitting (the next ordinary dispatch commits it).
- **(P5) Passages of the pack that carried withheld content — RULED and EXECUTED:** withheld from
  the pack by the generator as authored inputs (`cowork_rulings_2026_08_22_member_two_leak_sitting.md`,
  widened by Ruling 5 of `cowork_rulings_2026_08_22_withheld_family_sitting.md`;
  `cowork_rulings_2026_08_23_member_two_second_leak_sitting.md`), applied at the objects. This
  brief does not describe any withheld passage; the session must not learn of them from here.

## 9. Provenance — for the user and the record; NOT opened by the deriving session

Written at branch tip `dcbfa5fe32` (read with `git show -s` and `git for-each-ref` at the explicit
hash on the user's machine) while the pilot-preparation dispatch was running; the repository was
read-only to this session. The subject's wording is the forty-third handover block's, which is
Ruling 1 of `cowork_rulings_2026_08_22_pilot_order_sitting.md` in its own words ("how the analysis
should decide where one chord ends and the next begins, and what evidence decides it"). The
six-field form restates plan §7 of `cowork_specification_reconstruction_plan_successor_2026_08_21.md`
(ruled by Ruling 1 of `cowork_rulings_2026_08_21_successor_plan_sitting.md`); **one clause of §7
is deliberately NOT carried into §4** — the sentence naming how many modelling premises the
production layer's ratified specification carries — because it is a statement about the project's
current specification and a blind session may not meet it. The stop-on-meeting clause is the
evaluations' boot list's clause (`cowork_evaluation_boot_list_2026_08_21.md` §2), widened in sense
from "a prior verdict on the plan" to "a statement of what the analysis currently does on this
subject". The admitted-facts hole is Ruling 8 of 2026-08-21 (the ledger is not built; the hole is
declared in the source declaration). The pack's directory and read-me are as Task 1 of
`cc_instruction_pilot_preparation_withheld_family.md` prescribes; if that batch lands them under
another name, this brief's §3 is corrected to match before dispatch and the correction recorded
here. The constraint that a deriving session reads no implementation-derived material and treats
the current text as an untrusted source is §3.2 of
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`. The writing standards
applied are `cowork_design_doc_template.md`'s two (qualified predicates; defined terms, plain
vocabulary, no shorthand), which bind a brief as they bind everything written for the user; the
fourteen-section structure does not bind this kind (a dispatch-like instruction), and the kind is
stated so the exemption is not claimed by silence. The reserved-word conventions bind every line
above: TOWARDS the ultimate objective and TOWARDS the guiding principles.

**Amended the same day, after three rulings** (the member (2) leak; the deriving side; the staged
annotation files — records named in §8): §3 gained the staged-annotation paragraph, §7 lost its
Claude Code branch, §8 was rewritten to the rulings' state. The annotation-file enumeration behind
§3 was taken on the user's machine: `docs/score_inventory.md` read whole from a staged copy; the
DCML chorale clone's `MS3/001 Aus meines Herzens Grunde.mscx` staged and searched — it carries NO
harmony annotation (no `Harmony` element; its two `StaffText` elements are the title and the BWV
number), so the score and the human analysis are separate files by construction, and the inventory's
statement that every DCML clone carries a `harmonies/` folder is false of the chorale clone at this
tree (it has `measures/`, `notes/`, `reviewed/` and no `harmonies/`); the *When in Rome* chorale
folder `001` holds `analysis.txt`, `analysis_BCMH.txt` and `remote.json` and no score file. After the
user connected the chorale folder, all five *When in Rome* files named in §3 were staged and
`001/analysis.txt` read whole (768 bytes: analyst, proofreaders, time signature, form, one line per
bar with beat-positioned Roman numerals, two analyst variants); the `.mscx` scores for 003 and 137
are named and not yet opened by the writing side.

**Amended again 2026-08-23, after the brief-validation sitting** (record
`cowork_rulings_2026_08_23_brief_validation_sitting.md`): the banner set to RULED, §7's output
name fixed by Ruling 3, §8 brought to the rulings' state (P2 and P4 ruled; P5 executed and
extended of record). The same sitting's Ruling 1 orders the pack read-me's boundary wording scoped
so that this brief, the files it stages by name, and fetched research are no longer forbidden by
its letter; that edit is the generator's, made by the dispatch that lands this amendment, and is
recorded here so the correction is not claimed by silence.

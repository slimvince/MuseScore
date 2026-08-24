# BRIEF for the blind deriving session — the SCORING-MODEL subject (the sizing unit of the pilot)

> **STATUS: RULED 2026-08-24.** Written by the writing side (Cowork, 2026-08-24, the forty-fifth
> Cowork session) at branch tip `24d7f0be93`, after the boot pack for this subject was rendered and
> verified at the objects; refreshed to the ruled state the same day at tip `3fbbcb5b5d`. **It
> dispatches nothing and boots no session.** **Every point of §8 is now RULED**
> (`cowork_rulings_2026_08_24_sizing_brief_sitting.md`). **This is the brief the sizing session
> reads; the user opens that session when the user chooses.**
>
> **Who reads this file, and when.** The deriving session reads it FIRST, before it opens the boot
> pack. Everything the session is allowed to read is named in §3; **this brief and that directory
> are the session's whole read inside this repository.** The provenance at the foot (§9) is for the
> user and for a later reader of the record; **the deriving session does not open any file §9
> names.**
>
> **★ THIS UNIT IS NOT HELD OUT, AND THE SESSION IS TOLD SO.** Unlike the pilot's first unit, no
> ruled answer is withheld from this pack and there is no oracle to be compared against. Nothing
> was cut from the pack for this subject (§3). What this unit measures is what a derivation of this
> kind COSTS — the sizing record of §5 is a first-class deliverable, not a by-product.

---

## 0. Terms, explained before anything rests on them

A reader of this brief knows music theory and knows nothing about this project. Every project term
is explained here, once, before it is used; standard music theory is used in its standard sense.

- **The analysis** — the harmonic-analysis software this project builds: given a notated score, it
  decides the tonality, the chords, and the moments at which one chord gives way to the next, and
  writes the result into the score as Roman numerals and chord symbols. **How it CURRENTLY does any
  of this is exactly what this session must not know.**
- **A deriving session** — one that writes what the analysis SHOULD do for one subject, from music
  theory, from published research it fetches and reads, and from the ruled design intent it is
  given — WITHOUT reading what the project's code or the project's specifications say it DOES. Such
  a session is called *implementation-blind*, or *blind* for short.
- **The boot pack** — the one directory a deriving session reads at boot, generated from a ruled
  reading list: six rendered files plus a read-me. §3 names the directory.
- **A statement** — one atomic sentence of the derived answer, in the six-field form of §4. The
  derived answer is a set of statements, not a paragraph.
- **The sizing record** — §5. The measured cost of this derivation, from which the budget for every
  later unit of this project's specification work is set. **No value in it is estimated; every one
  is measured by the session on itself.**
- **Tonality** — used throughout for what is commonly called "the key". In this project the bare
  word *key* is reserved for tonality and is never used for a lookup key or a map key; *bar* is
  used for the metric unit, never *measure*; *score* means the musical score and never a number.

## 1. What this session is for, in one paragraph

Derive, blind, what the analysis should do to **score a candidate chord reading against the
evidence** (§2) — and write that answer as statements in the six-field form, each carrying its
defense in the same breath. **Beside the statements, keep the sizing record of §5 as you go.** The
session produces statements, open questions, the sizing record and the independence record. It
produces no code, no specification edit, no comparison, and no verdict on anything the project
currently does.

## 2. The subject, in plain words

**How should a harmonic analysis of a notated score decide HOW WELL a candidate chord reading fits
the evidence over a stretch of music — what quantities enter that judgment, in what form, and how
are they combined into one comparable quantity?**

The question has at least these faces, listed so none is silently dropped; the session is free to
find the list incomplete and to say so:

- **What is being scored.** A candidate reading of a stretch — a chord label, its quality, its
  inversion, in a tonality — against what actually sounds there. What exactly is the object whose
  fit is judged, and what is the stretch it is judged over?
- **The terms.** What quantities can bear on the fit: the tones present that the chord predicts;
  the tones present that it does not; the tones the chord predicts that are absent; the bass; the
  notated spelling; metric placement; duration; what precedes and follows. Which of these are
  separate terms, and which are one term seen twice?
- **The form of a term.** Is a term a probability, a penalty, a count, a ratio? What makes one form
  right and another wrong — and what does the choice of form commit the analysis to?
- **Combination.** How do terms combine into one quantity: a sum, a product, a weighted sum, a
  lexicographic order? What has to be true of the terms for the chosen combination to be sound?
- **Where the numbers come from.** Which parts of the model are derivable from theory, and which
  are values that must be fitted against annotated music — and what discipline governs fitting, so
  that a value is never set to make one case come out right.
- **Comparability.** Two candidate readings of the same stretch must be comparable; must two
  readings of *different* stretches be comparable, and what breaks if they are not?
- **What the model must NOT do.** Which evidence may never enter a fit judgment, and why.

**Scope.** Common-practice tonal music as notated in a score. Deciding *where* one chord ends and
the next begins is OUT of scope for this unit except where a scoring statement depends on it, in
which case the dependency is stated as a statement in its own right.

## 3. What the session reads — and the one rule that matters most

**The session's whole read inside this repository is this brief and the directory
`tools/audit/derivation_boot_pack/scoring-model/`.** Open its `00_READ_THIS_FIRST.md` first; it
names the six files and the order in which to read them. Nothing else inside this repository is
opened: not the project's other governing documents, not the specifications — **and in particular
not `docs/scoring_model.md`, which is the current specification of this very subject and is
exactly what this session must not read** — not the code, not the open-items register or the
decisions register, not any session handoff, dispatch or report. **The ordinary session-start read
of this repository is REPLACED, for this session, by the pack**; the session does not take the
branch rule, read the commit log, or run anything.

**Nothing was withheld from this pack for this subject** (ruled 2026-08-24). You will see gaps in
the design-intent file's identifiers; those are entries a standing check removed because their own
quoted words carry a path into this project's implementation documents, and **they are evidence of
nothing**. The pack's read-me says the same.

**Beyond the repository, the session MAY fetch and read published research** — peer-reviewed
papers, published algorithms, public datasets' documentation — and MUST label every load-bearing
claim it takes from them as the pack's principles prescribe (FACT where the paper actually fetched
and read states or measures it; THEORY where it is established published theory; CONJECTURE
otherwise). **A source that could not be fetched yields no statement**; the gap is recorded.

**The annotated scores — staged to the session BY NAME, and nothing else of the corpus (ruled
2026-08-24).** Beside the brief and the pack, the writing side stages these files, each by its own
name and never a directory:

* chorale **001** *Aus meines Herzens Grunde* — `tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx`,
  with `tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/001/analysis.txt`
  and `…/001/analysis_BCMH.txt`;
* chorale **003** *Ach Gott, vom Himmel sieh darein* — `…/MS3/003 Ach Gott, vom Himmel sieh darein.mscx`,
  with `…/Chorales/003/analysis.txt` and `…/003/analysis_BCMH.txt`;
* the **BWV 301** score *Du, o schönes Weltgebäude* — `…/MS3/137 Du, o schönes Weltgebäude.mscx`,
  with `…/Chorales/`**`134`**`/analysis.txt` — **paired by CONTENT and never by number**: the two
  corpora number by different schemes, and folder 137 holds a different chorale entirely (ruled
  2026-08-24 at the blind-return sitting; folder 134 matches this score on title, key signature,
  meter and bar count). Folder 134 carries no BCMH file.

**What these are, and what they are not.** They are the annotators' own published readings — one
human reading each, named to its analyst, graded against in this project, and **never a
specification**. They are **EXEMPLARS, NOT A CORPUS**: the session may read what an analyst chose
at a given place and reason about what would make that reading fit, and it may say what three
chorales could not show. **It builds, designs, scopes and runs NO measurement over them** — that
bar is unchanged by their being staged, and a count taken over three chorales is not a measured
fact about this project's data.

**The admitted-facts hole, declared.** The pack carries no ledger of empirically established facts
about this project's own data. The session works with none; where it would have wanted one it
writes the want as an open question and does not fill it.

**★ THE STOP-ON-MEETING CLAUSE.** If, anywhere in the pack or in this brief, the session meets a
statement about how THIS project's analysis currently scores a candidate reading, it **STOPS
READING THAT FILE AT THAT POINT** and records, in its independence record (§6), which file, where
in it, and how much of the statement it saw before stopping. It then continues with the remaining
files. It does not delete, paraphrase or reason about what it saw. **A session whose output
carries no such record, and no positive statement that nothing was met, is incomplete.**

## 4. The form of every statement — six fields, one rule per statement

Atomic, because a paragraph cannot be compared against anything. Every statement carries all six
fields; a statement that cannot carry the sixth is marked UNVERIFIABLE rather than left to look
checkable.

1. **The statement** — what the analysis must do, or what it must be ABLE to do.
2. **The defense** — the music theory, the published research fetched and read, or the kind of
   measurement that would decide it, each load-bearing claim labelled FACT / THEORY / CONJECTURE.
   "Because the current implementation does this" is not available to this session and is not a
   defense; a statement supportable only by appeal to what software usually does is marked
   UNSUPPORTED.
3. **The source class** — *derived* (from theory or research), *salvaged* (taken from a ruled
   design-intent entry in the pack, cited by its identifier), or *measured* (a claim resting on a
   measurement this session cannot make — written with the measurement it would need, its
   establishment status UNESTABLISHED, and no value).
4. **The status** — *settled* or *open*.
5. **The premise it rests on, and that premise's false-negative path.**
6. **What would falsify it** — in CODE where the statement is behavioural (name the OBSERVABLE, the
   DECISION RULE over it, and the near-miss it is NOT falsified by); in the RESIDUAL where it is a
   modelling premise with no code site. The session names observables in plain terms and leaves code
   sites to a later session.

**★ FIVE STATEMENTS OF THIS OUTPUT WILL BE JUDGED FOR THE FORM ITSELF** (the pilot's format test,
ruled 2026-08-21), **and the sample will include a probabilistic factor form and a
conditional-independence premise.** The session is told this so that it writes those two kinds when
the subject calls for them rather than avoiding them; it is NOT told to write them where the
subject does not call for them, and manufacturing a statement to satisfy this paragraph would
defeat what the test measures.

**What cannot be settled is written as an open question, never filled with the most plausible
reading.**

## 5. The sizing record — the measured cost, and a first-class deliverable

**This is the unit the pilot sizes.** The session measures itself as it works and records, as plain
counts and durations it measured and nothing it estimated:

- **the time spent per statement**, and the number of statements — timestamps taken as the session
  goes, never reconstructed at the end;
- **the share of statements marked *open***, and the share the session would put to the user for a
  ruling, with the question each would ask;
- **the share whose sixth field could not be written** (marked UNVERIFIABLE);
- **the share resting on a *measured* source class** — settled as to form but carrying an
  UNESTABLISHED value;
- **the noise measurement** — which files of the pack, and which fetched sources, the session
  actually consulted while writing each statement; **a pack file consulted by no statement is
  listed as such**;
- **the time spent on reading before the first statement was written**, separately from the time
  spent writing statements.

**No share is reported without its denominator. No value here is estimated.** If a measurement was
not taken as the work went, it is reported missing rather than reconstructed.

## 6. The independence record

The output states: every file the session opened (pack files and fetched sources alike, the latter
by citation); every pack file it did not open, if any; and the stop-on-meeting record of §3 — or
the positive statement that it met no such passage. **An output with no independence record is
incomplete.**

## 7. The output, and what the session does NOT do

**One file.** The session writes its statements, open questions, sizing record and independence
record to ONE new file at the repository root, whose name the user fixed on 2026-08-24 (Ruling 3
of the sizing-brief sitting): **`cowork_blind_derivation_scoring_model_2026_08_24.md`**, with the
status banner *DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED*. It is written for a reader
who knows music theory and not this project: terms explained at first use, predicates qualified,
no invented labels, music-theory words in their musical sense only.

**The deriving side is a fresh Cowork session** (ruled 2026-08-24). The file is delivered to the
repository root through the device bridge, hash-verified after re-staging, and committed by the
next ordinary dispatch. The session itself commits nothing, runs nothing and writes nothing else:
no `STATUS.md` entry, no handover block, no report, no close, no guard run.

**What the session does NOT do:** it opens no untrusted source; it compares nothing against
anything; it edits no specification and no code; it runs no build, no test, no measurement tool; it
creates, flips or discards no open-items row; it allocates no finding number; it takes no branch
rule and reads no commit log; it derives nothing on any subject but the one in §2; **it does not
decide anything about the derivation method** — that was ruled established on 2026-08-24 on a
different unit, and this session's business is the subject and the sizing, not the method.

## 8. The points the user rules before this brief is dispatched — ALL RULED on 2026-08-24

- **(P1) The deriving side's identity — RULED:** a fresh Cowork session (Ruling 2 of
  `cowork_rulings_2026_08_24_sizing_pilot_sitting.md`). Applied in §7.
- **(P2) Fetched research — RULED:** allowed, as §3 is written (Ruling 1 of
  `cowork_rulings_2026_08_24_sizing_brief_sitting.md`). The ground: the method's ruled inputs are
  the pack and fetched literature, and a session forbidden research would size a different method
  from the one established.
- **(P3) Annotated scores — RULED:** the three pairs are staged BY NAME (Ruling 2 of the same
  record), applied in §3 with the file list and with the exemplars-not-a-corpus bar restated there.

- **(P4) The output file's name — RULED:** `cowork_blind_derivation_scoring_model_2026_08_24.md`
  (Ruling 3 of the same record). Applied in §7.
- **(P5) The withheld family — RULED EMPTY** (Ruling 1 of the sizing-pilot sitting) and applied:
  nothing is withheld from this pack, and §3 tells the session so.

## 9. Provenance — for the user and the record; NOT opened by the deriving session

Written at branch tip `24d7f0be93` (read with `git for-each-ref` at the explicit hash on the user's
machine), after the `scoring-model` pack was rendered by
`cc_instruction_sizing_pack_preparation.md` and verified at the objects by the writing side: two
subjects in the manifest, the harmony-boundary block byte-unchanged, this subject's family empty at
every field, three leak-listed entries, member (2) carrying zero withheld markers, and the pack's
read-me stating truthfully that nothing was withheld. The pack's directory and read-me are as this
brief's §3 names them, checked at the object rather than assumed.

**The subject's statement in §2 was derived from the TITLE AND BANNER of `docs/scoring_model.md`
ONLY** — the document's first eighteen lines, read at the tip object by the writing side, which
carry its title, its LIVE-MANDATORY-REFERENCE status, and the ruled declaration that its mechanism
content describes a scorer dormant on both production surfaces since 2026-07-26/27. **No mechanism
content of that document was read by the writing side, and none of it is in this brief.** The
subject's faces in §2 are the writing side's own decomposition of the title's plain meaning,
written to be answerable from the domain; a session that finds the decomposition wrong says so.

**One bound, declared because it is invisible from inside the session.** The pilot's FIRST unit
produced a blind derivation on a different subject, which touched scoring in passing. **That output
is NOT staged to this session and is not named to it**, because a session reading another
derivation is not deriving, and the sizing would then measure the wrong thing. Any overlap between
the two outputs is therefore independent, and a later reader may treat it as such.

The six-field form restates plan §7 of
`cowork_specification_reconstruction_plan_successor_2026_08_21.md`; the format-test paragraph in §4
restates Ruling 4(b) of `cowork_rulings_2026_08_21_successor_plan_sitting.md`; the sizing record's
fields are plan §6.1's, with the reading-time split added by this side and declared here as an
addition. The stop-on-meeting clause is the evaluations' boot list's clause, narrowed in sense to
this subject. The admitted-facts hole is Ruling 8 of 2026-08-21. The constraint that a deriving
session reads no implementation-derived material is §3.2 of the phase-definition surface. The
writing standards applied are `cowork_design_doc_template.md`'s two; the fourteen-section structure
does not bind this kind, and the kind is stated so the exemption is not claimed by silence. The
reserved-word conventions bind every line above: TOWARDS the ultimate objective and TOWARDS the
guiding principles.

**Amended 2026-08-24, after the sizing-brief sitting** (record
`cowork_rulings_2026_08_24_sizing_brief_sitting.md`, taken at tip `3fbbcb5b5d`): the banner set to
RULED; §3's annotated-score paragraph replaced by the ruled file list with the
exemplars-not-a-corpus bar restated; §7's output name fixed by Ruling 3; §8 brought to the rulings'
state. **§§0–2, §4, §5, §6 and the whole of §7 but its one name sentence are byte-unchanged**, and
so is everything of §9 above this note. The same sitting ruled that two known prose defects in the
generator's own manifest and docstring are left as reported facts until the generator is next
touched for a substantive reason; **neither reaches this brief or the pack it names**.

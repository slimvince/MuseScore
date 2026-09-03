# Blind derivation — L0, the notated record, and L1, change points, candidates and notated evidence

> **★ THIS IS THE RECORD OF THE BLIND ACT, AND ITS BODY IS NOT REWRITTEN (D-674, branch one; Ruling 63,
> §3br of `cowork_rulings_2026_08_31_decision_surface_sitting.md`).** Written 2026-09-02 by an
> implementation-blind session; compared over 29 outgoing documents in
> `ratification_surfaces/cowork_comparison_l0_l1_reading.md`; its statements dispositioned by Rulings
> 34–62 of that sitting record. **The derived L0/L1 specification as amended by those rulings is
> `cowork_derived_specification_l0_l1_2026_09_03.md`, and that file, not this one, is the text the
> ratification act is put over.** Everything below this banner stands as it was written at blob
> `9b102c575643d672e4747b4cfc23e377cd344c27`.

> **STATUS: DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED.**
>
> Written 2026-09-02 by a fresh Cowork session opened with nothing mounted, under
> `cowork_blind_session_brief_l0_l1.md` (the brief) and the ten-member boot pack it names, with four
> staged scores. The session read no specification, no code and no document of this project other than
> the brief and the pack. It compared nothing and dispositions nothing. What it met that it should not
> have, and how much of each file it read, is in §6.
>
> **How to read this file.** §0 explains every term before it is used. §1 states the subject and the
> verdict on whether L0 and L1 separate. §2 derives L0 as a criterion and a list. §3 derives L1 face by
> face. §4 collects the open questions. §5 is the measured-cost record. §6 is the independence record.
> §7 says where the brief's decomposition seemed wrong or incomplete. Every statement is in the
> six-field form of the brief's §4; the fields are labelled in every statement so none is silently
> dropped.

---

## 0. Terms

Standard music theory is used in its standard sense. Every project-specific term below is used only
after this table. The reserved-word convention of the pack binds: bare *key* means tonality, bare
*measure* is not used (the metric unit is a *bar*), bare *score* is a musical score, bare *note* is a
pitch event, bare *tie* is the notated tie, bare *rest* is the notated silence.

- **The analysis** — the harmonic-analysis software. Its layers are named L0, L1, L2, L3 in the charter
  the pack carries (`07_the_charter_the_layers_and_the_decisions.md`, cited below as "the charter").
- **The charter** — the ratified statement of each layer's question, inputs and outputs. Given; not
  re-decided here. Where a statement below merely restates it, the statement is marked *given*.
- **L0, the notated record** — not a layer: the contract stating what the analysis is handed. The
  charter's own words are quoted at §2.
- **L1** — the first layer. Its charter question: *at which moments MAY a harmony begin, and what does
  the notation say at each?* It consumes L0 only and decides nothing about the music.
- **The notated text** — what a competent reader sees on the page: the notes, rests, signs and
  markings a copyist reproduces. Used in the L0 criterion (§2.1) to separate notation from things a
  file may carry beside it.
- **A record file** — the machine form a score arrives in (here, MuseScore `.mscx`; the same
  statements are meant to hold for MusicXML, MEI or kern). Element names in angle brackets, such as
  `<Harmony>`, are the file's own names and are used only to locate cases.
- **An event** — one sounding pitch with one onset and one release. A note not tied to a predecessor
  starts an event; a group of tied notes is one event (§3.2).
- **Onset** — the metric moment at which an event begins to sound. **Release** — the metric moment at
  which it stops. Both are rational positions on the score's time axis, not clock times.
- **Metric position** — a point on the score's time axis measured in whole-note fractions from the
  start of the piece in notated order, together with the bar it falls in and the offset from that
  bar's start. Given by L0.
- **Change point** — a moment that is the onset or the release of at least one eligible event
  (charter). **Eligible** is defined by §3.1; the charter leaves it to this derivation.
- **Slice** — the charter's term: the stretch between two consecutive change points. The slices are
  ordered, covering, gapless and non-overlapping (charter). The **sounding set** of a slice is the set
  of events whose onset is at or before the slice's start and whose release is after it (§3.3).
- **Silent slice** — a slice whose sounding set is empty.
- **Metric strength class** — an ordinal label per change point naming the highest level of the
  notated metrical hierarchy at which that position is a beat (§3.4). A **level** is one row of that
  hierarchy: the bar, the beat, the divisions of the beat.
- **Tactus** — the beat the time signature names: the denominator's note value in simple meters (a
  quarter in 4/4), the dotted value grouping three denominators in compound meters (a dotted quarter
  in 6/8). Used in its ordinary theory sense.
- **Anacrusis** — an incomplete first bar (or an incomplete bar after a repeat) whose length is less
  than the time signature's bar. A record file usually marks it (MuseScore: `<Measure len="…">` with
  `<irregular>`).
- **Notated boundary evidence** — the charter's five kinds: bar line, fermata, rest, repeat sign,
  double bar. Published per change point as flags (§3.5).
- **Local cadence cue** — one of the charter's three: a falling-fifth or rising-fourth bass motion; a
  leading-tone resolution; the sounding together of the fourth and seventh degrees of a *candidate
  tonality* in the approach. Each is defined tonality-free at §3.6.
- **Candidate tonality** — in the third cue only: the tonality whose tonic (or whose dominant) is the
  bass pitch class at an onset change point. A hypothesis anchored on a note the score gives; never a
  decided tonality (§3.6, S-47).
- **Bass** — at a slice, the lowest sounding pitch of its sounding set. Not a notated voice.
- **Witness** — the notes (by identity in the record file) that make a published predicate true.
  Every cue and flag is published with its witnesses so that L2 can weigh it (§3.7).
- **Notated order** — the order of bars as written, repeats not unfolded. **Unfolded order** — the
  order a performer plays, repeats and endings expanded. Which order the analysis works in is an open
  question (OQ-1).
- **FACT / THEORY / CONJECTURE** — the brief's labels on load-bearing claims: FACT is stated or
  measured in a source this session fetched and read (or read in a pack extract that was read at the
  object and quotes the page); THEORY is established published theory; CONJECTURE is this session's
  reasoning. **RULED** marks a claim fixed by the charter or by a ratified design-intent entry the pack
  carries, cited by identifier.
- **Source class** — *derived*, *given*, or *measured*, as the brief's §4 defines them. This file uses
  *given* for a statement fixed by the charter's words **or** by a ratified design-intent entry in
  `05_the_ratified_design_intent.md` (cited by its D-number); the two are counted separately in §5.
- **UNESTABLISHED** — the status of a value a *measured* statement would need and this session cannot
  supply.
- **OQ-n** — an open question, collected in §4, each naming the face of the brief's §2 it belongs to.

---

## 1. The subject, and the verdict on separation

**The subject** is the brief's two questions. For L0: *what exactly must a notated record supply for
this analysis to run, what may be assumed about it, and what happens when a real score does not supply
it* — answered as a **criterion** first (§2.1) and a list second (§2.2), as the brief requires. For L1:
*how are the moments at which a harmony may begin found, how is what the notation says at each
established, and in what form are both published — given that this layer may decide nothing about the
music* — answered face by face in §3.

**Verdict on separation (the condition attached to Ruling P4 in the brief's §8).** L0 and L1 separate
cleanly. L0 is a data contract: a list of facts and a test for admitting a fact to it, with no
computation. L1 is a computation whose every input is an L0 fact and whose every output is a predicate
over L0 facts with witnesses. The one place they touch is the eligibility predicate of §3.1, which
consumes four L0 facts (pitched, sounds, visible, has metric duration) and belongs to L1 because the
charter defines L1's change point over *eligible* notes and leaves eligibility to L1. Nothing in §2
depends on §3, and nothing in §3 revises §2. **A later act may split this file at the §2/§3 boundary
without rewriting a statement.** The split is left to that act, as the ruling requires.

**Scope.** Common-practice tonal music as notated in a score. Deciding where a harmony actually gives
way to the next is L2's and is out of scope; where a statement depends on that, the dependency is its
own statement (S-53).

---

## 2. L0 — the notated record

The charter's words, which every statement in this section obeys: *"Given: spelled pitch, duration,
voice membership, metric position and bar, time signature, key signature, bar lines, repeats, fermatas,
ties, pedal marks, and whether each note sounds and is visible. What may be assumed about it: that it
is what the notation says, and nothing more. The key signature is a weak prior (C-2), never a fact
about the tonality."* And the boundary contract L0 → L1: *"The notated record, whole … Nothing derived.
L1 may not treat the key signature as the tonality."*

### 2.1 The criterion — the test by which a fact is admitted to L0

**S-1. A fact is admitted to L0 if and only if (i) it is part of the notated text — two competent
copyists transcribing the same source would agree on it, and any disagreement between them would be a
copying error rather than an analytical disagreement — and (ii) it is not a claim about what the music
means: not a tonality, a chord, a function, a boundary, a phrase, or a degree.**
- *Defense.* Condition (i) is the charter's own assumption made testable: *"that it is what the
  notation says, and nothing more"* [RULED — charter, L0]. The copyist test operationalises "what the
  notation says" as inter-transcriber agreement, which is the same test the pack's principle #21 applies
  to ground truth — a fact is what independent readers agree on [THEORY — the pack's principle #21 as
  stated in `02_the_guiding_principles…`]. Condition (ii) is the boundary contract: *"Nothing derived"*
  crosses L0 → L1 [RULED — charter, boundary contracts]. The two conditions are both needed: a key
  signature passes (i) and (ii) — it is on the page and it is a sign, not a claim; a chord symbol
  written above the staff passes (i) and fails (ii) — copyists reproduce it, but it asserts a harmony;
  a "declared mode" tag in a file fails (i) — no copyist reads it off the page. [CONJECTURE — the three
  worked cases are this session's.]
- *Source class.* Derived.
- *Status.* Settled as a criterion; the cases it does not settle are OQ-4, OQ-5, OQ-13.
- *Premise and its false-negative path.* Premise: the analysis's subject is the notated score, not a
  performance or an edition's commentary. False-negative path: a fact that is on the page only in some
  editions (editorial accidentals, editorial ties in brackets) passes (i) for one source and not
  another; the criterion then admits it for the source in hand and publishes nothing about editions.
  A consumer expecting edition-independence would be misled; L0 does not claim it.
- *Falsifier.* RESIDUAL — a modelling premise. It is falsified if a fact that the analysis demonstrably
  needs as input, and that cannot be derived from the notated text, fails the test — the brief's own
  instruction is that such a case is written as an open question, and OQ-13 is one candidate.

**S-2. Applying S-1, a fact present in a record file but failing (i) or (ii) — a chord symbol
(`<Harmony>`), a staff text, a lyric, a declared mode or tonality tag, an editor's analytical mark —
is not part of L0. It may be carried beside L0 as *annotation*, so labelled, and no layer may consume
it as evidence about the music.**
- *Defense.* Follows from S-1 (ii) for chord symbols and analytical marks, and from S-1 (i) for a mode
  tag. Carrying rather than discarding follows the pack's no-information-loss principle (#12) and the
  publish-broadly rule for evidence-class facts [RULED — D-100, as carried in the pack]; the bar on
  consuming it is the charter's *"Nothing derived"* [RULED]. The staged scores exercise the case: the
  Couperin and C. P. E. Bach files carry `<Harmony>` and `<StaffText>` elements this session did not
  read (§6). [FACT about the files — element counts in §6.]
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: a transcriber's annotation is never the notated text. False-negative path: a
  composer's own figured bass under a continuo part is on the page and is a harmonic claim by the
  composer — it passes (i) and arguably fails (ii). Handled at S-8.
- *Falsifier.* CODE. Observable: the set of fields any layer reads. Decision rule: falsified if any
  layer's published fact changes when every annotation-class element is removed from the record file.
  Not falsified by: a presentation layer displaying the annotation beside the analysis.

### 2.2 The list — the facts L0 supplies, each tested

**S-3. L0 supplies, per note: its spelled pitch (letter, accidental, octave — equivalently a tonal
pitch class and an octave), at concert (sounding) pitch; whether it is pitched; its notated duration
as a rational fraction of a whole note, tuplet ratios applied; its metric position (bar index, offset
within the bar, absolute position); its staff and notated voice; whether it is a grace note; whether it
is tied to the preceding note and to the following note; whether it is marked as not to be played;
whether it is visible; whether it is cue-sized; and the ornament and articulation signs attached to
it.**
- *Defense.* Each passes S-1: every item is read from the page or is a mechanical property of the
  file's representation of the page (the tuplet ratio is printed; concert pitch is the printed pitch
  corrected by the printed transposition of the instrument). Spelling, duration, voice and metric
  position are the charter's own list [RULED]. Grace status, tie, played-flag, visibility, cue size and
  ornament signs are added by this derivation because §3 consumes them and each is on the page. The
  staged record files carry every one of them as an element (`<grace16/>`, `<appoggiatura/>`,
  `<Spanner type="Tie">`, `<play>0</play>`, `<visible>0</visible>`, `<small>1</small>`,
  `<Articulation><subtype>ornamentShortTrill</subtype>`) [FACT — read in the files, §6]. The MusicXML
  standard likewise distinguishes a grace note (an element whose content is *"Always empty"* — it
  carries no duration) and a tie (*"The <tie> element indicates sound; the <tied> element indicates
  notation"*) [FACT — MusicXML 4.0 reference, fetched, §6].
- *Source class.* Derived (extends the charter's list; the charter's items are given).
- *Status.* Settled.
- *Premise.* Premise: the record file preserves what the page shows. False-negative path: a file in
  which a tie was drawn as a slur (the Couperin file has ties whose `<next>` points into a different
  chord note, `<notes>1</notes>`, which is a tie; a slur between same pitches would be a false
  negative for the tie fact). L0 supplies what the file says; S-24 handles the disagreement.
- *Falsifier.* CODE. Observable: the per-note record L1 receives. Decision rule: falsified if an
  eligible-note decision in §3.1 or a tie decision in §3.2 needs a per-note fact not in this list.
  Not falsified by: a fact needed only for presentation.

**S-4. L0 supplies, per rest: its duration, metric position, staff and voice, visibility, and any
fermata on it.**
- *Defense.* A rest is notation (S-1). It opens no event, but it carries boundary evidence (fermata
  over a rest; the chorale file has fermatas on notes, and rests in voices) and it makes a release
  explicit, so §3.5 consumes it [CONJECTURE for the consumption; RULED for "rest" as boundary
  evidence — charter L1]. Invisible rests exist in the staged files (`<Rest><visible>0</visible>` in
  the Couperin and the Brandenburg files) [FACT — §6]; visibility is supplied so §3.1 can apply the
  same rule it applies to notes.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: a rest never sounds. False-negative path: none found; a rest under a pedal mark
  is the pedal question, OQ-3.
- *Falsifier.* CODE. Observable: the rest record. Decision rule: falsified if §3.5's rest flag cannot
  be computed from these fields alone. Not falsified by: rests being absent from a voice that is
  simply empty (an empty voice is silence without a rest; §3.3 covers it).

**S-5. L0 supplies, per bar: its nominal length from the time signature in force, its actual length,
whether it is marked irregular (anacrusis or other), the bar-line type at its start and end (single,
double, final, start-repeat, end-repeat with its play count), and any ending (volta) it belongs to
with the ending number(s).**
- *Defense.* All on the page (S-1). Bar lines and repeats are the charter's own items [RULED]; the
  actual length and the irregular mark are needed by §3.4 (anacrusis). The staged files carry
  `<Measure len="1/4">`, `<irregular>1</irregular>`, `<startRepeat/>`, `<endRepeat>2</endRepeat>`, and
  `<Spanner type="Volta">` with `<endings>1</endings>` [FACT — §6].
- *Source class.* Derived (extends the charter's items).
- *Status.* Settled.
- *Premise.* Premise: a bar's actual length is what the file says, and the file is internally
  consistent (the durations in each voice sum to the bar's actual length, or a voice is shorter and
  the remainder is silence). False-negative path: a voice whose durations overflow the bar (a file
  defect); S-10 covers it.
- *Falsifier.* CODE. Observable: the per-bar record. Decision rule: falsified if a metric-strength
  class (§3.4) or a boundary flag (§3.5) needs a per-bar fact not listed. Not falsified by: layout
  facts (system breaks, `<LayoutBreak>`), which S-1 (ii) does not exclude but which nothing consumes.

**S-6. L0 supplies the time signature in force at every position, the key signature in force at every
position, and the position of every change of either.**
- *Defense.* Charter items [RULED]. The chorale file changes time signature twice mid-piece (4/4 →
  3/4 → 4/4) [FACT — §6]; the class hierarchy of §3.4 must be recomputed at each change, so the
  positions of changes are needed, not only the values. The key signature enters L1 nowhere except as
  a spelled context (S-9) and is carried forward for L2 as the charter's weak prior.
- *Source class.* Given (charter), extended by the change positions.
- *Status.* Settled.
- *Premise.* Premise: a key signature is a sign. Its false-negative path is the charter's own: it is
  *"never a fact about the tonality"*, and a Baroque score is often notated one accidental short of
  modern practice [FACT — the pack's ledger, C14], so a consumer that read it as tonality would be
  wrong on a class of scores. L0 publishes it; L1 does not read it (S-9).
- *Falsifier.* CODE. Observable: the signature-in-force lookups. Decision rule: falsified if a
  position between two signature changes returns the wrong signature, or if the metric class at the
  first change point after a time-signature change is computed from the old hierarchy. Not falsified
  by: a signature change notated at a bar line producing a class of "bar" for that change point —
  that is correct.

**S-7. L0 supplies the fermatas, the pedal marks with their spans, and the tremolo marks, each with
its position and the note, rest or bar line it is attached to. L0 does not supply tempo, dynamics,
slurs, beams, stem directions, or layout.**
- *Defense.* Fermatas and pedal marks are charter items [RULED]. Tremolo is added because it changes
  what sounds (a measured tremolo is a written abbreviation for repeated notes; an unmeasured one is
  a sustained sonority) and §3.1 must decide its eligibility — which this session cannot, the staged
  set carrying no tremolo (OQ-2). Tempo, dynamics, slurs, beams and stems pass S-1 but nothing in §3
  consumes them; they are excluded to keep the contract minimal, and a later layer that needs one adds
  it by the same test [CONJECTURE — the minimality is a choice, defended by the pack's one-home
  principle #6: a fact nobody consumes is waste or declared dormancy (D-100)].
- *Source class.* Derived.
- *Status.* Open on tremolo and pedal (OQ-2, OQ-3); settled on the exclusions.
- *Premise.* Premise: a slur carries no harmonic information L1 needs. False-negative path: a slur
  used in place of a tie between identical pitches (S-16) — L0 would then need slurs to repair the tie.
  Recorded, not adopted: the repair is a file-defect concern.
- *Falsifier.* CODE. Observable: the fields L1 reads. Decision rule: falsified if any §3 computation
  reads a slur, beam, stem, dynamic or tempo. Not falsified by: L2 or L3 later admitting one of them
  through S-1.

**S-8. Figured bass and chord symbols written by the composer are annotation under S-2, not L0,
even though they are on the page.**
- *Defense.* They pass S-1 (i) and fail (ii): a figure is the composer's harmonic claim about the
  notes, which is exactly the kind of thing L2 decides [RULED — charter, L2's question]. A layer that
  read a composer's figures as input would be consuming a decision, which the boundary contract
  forbids [RULED]. They are carried beside L0 as annotation of a named kind ("composer's figures"),
  which a measurement layer may later use as a reference — that use is not an analysis input.
  [CONJECTURE on the carrying.]
- *Source class.* Derived.
- *Status.* Settled here; flagged for the user because it excludes a real source of information.
- *Premise.* Premise: the analysis derives harmony from notes alone. False-negative path: for a
  continuo part whose upper voices are not written out, the notes alone under-determine the harmony
  and the figures are the only record of it; the analysis then reads a thinner text than a performer
  does. Recorded as the cost.
- *Falsifier.* RESIDUAL — a modelling premise; falsified only by a ruling that composer's figures are
  input, which would move the boundary contract.

**S-9. L1 reads from L0 everything of S-3 to S-7 except the key signature, which L1 does not read.**
- *Defense.* The boundary contract: *"L1 may not treat the key signature as the tonality"* [RULED].
  Every L1 computation in §3 is defined without a tonality; the key signature could enter only as a
  tonality proxy, and the clearest way to keep it out is not to read it. The third cadence cue (S-41)
  anchors its candidate tonality on a note, not on the signature, for this reason.
- *Source class.* Given (charter), sharpened.
- *Status.* Settled.
- *Premise.* Premise: no L1 output needs the signature. False-negative path: spelling. Spelled pitch is
  given per note, so L1 never needs the signature to spell a note; if a record file gave only
  pitch-class-with-accidental-relative-to-signature, L1 would need it. L0 requires spelled pitch (S-3),
  so the path is closed at L0.
- *Falsifier.* CODE. Observable: L1's inputs. Decision rule: falsified if any L1 output changes when the
  key signature is replaced by a different one, all spelled pitches held fixed. Not falsified by: L2's
  outputs changing.

### 2.3 What may be assumed, and what happens when a real score does not supply it

**S-10. L0 assumes internal consistency of the record: durations in a voice do not overlap within the
voice; a bar's contents fit its actual length. Where a file violates this, L0 supplies what the file
says and attaches a defect flag to the offending bar and voice; L1 computes over the positions as
given and carries the flag on every change point inside the offending bar.**
- *Defense.* The charter allows assuming *"that it is what the notation says, and nothing more"*
  [RULED]; a defect is where the file says something the notation cannot mean. Carrying the flag
  rather than repairing follows #12 (no information loss) and the pack's stop-on-surprise discipline
  (#13): a repair silently chooses a reading [RULED — principles as carried]. The staged files use
  `<location>` offsets to place a voice's later notes after an implicit gap (the chorale file, in
  bars with a voice that rests without a written rest) [FACT — §6]; a gap is not a defect, it is
  silence, and S-11 covers it.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: defects are rare enough that flagging suffices. False-negative path: a corpus
  converted from a format that systematically overflows bars would flag every bar and the flag would
  carry no information; the pack's ledger warns of exactly this shape (C21, C22 — a mechanism whose
  population is total is inert). The remedy is a measurement over the corpus, UNESTABLISHED.
- *Falsifier.* CODE. Observable: the defect flag. Decision rule: falsified if a bar with overlapping
  same-voice durations, or a voice exceeding the bar's actual length, reaches L1 without the flag. Not
  falsified by: cross-voice overlap, which is polyphony.

**S-11. A voice that is empty over a stretch, or that ends before its bar does, is silent there. No
rest need be written for L0 to supply the silence; the absence of any event is the silence.**
- *Defense.* Notation practice: in keyboard and choral writing a secondary voice is often left blank
  where it is silent [THEORY — standard engraving practice]. The chorale file places a voice's
  continuation with a `<location>` offset after an unwritten gap, and the Couperin file writes
  invisible rests for the same purpose [FACT — §6]. Two notations of one meaning must yield one L0
  fact (the pack's #6).
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: blank means silent. False-negative path: none in common-practice notation; a
  tablature or a shorthand where blank means "continue" is outside scope.
- *Falsifier.* CODE. Observable: the sounding set of the slices over the gap. Decision rule: falsified
  if the two notations (unwritten gap; invisible rest) produce different slices or different flags.
  Not falsified by: the visible rest producing a rest flag (§3.5) that the unwritten gap does not — that
  difference is on the page and is information (S-39).

**S-12. Where a score does not supply a time signature, L0 supplies each bar's actual length as its
nominal length and marks the score "unmetered"; L1 then publishes the metric strength class "bar" at
bar starts and "unmetered" elsewhere.**
- *Defense.* The charter fixes that metric strength is a class read from the notation and not a
  judgment [RULED]; where the notation gives no hierarchy, the only notated fact is the bar line.
  Publishing "unmetered" rather than inferring a meter keeps L1 inside *decides nothing*. Inferring
  meter is the stage the charter's L0 section excludes for notated input (*"Meter is given"*) [RULED].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: unmetered notation is rare in the repertoire. False-negative path: an unmeasured
  prelude notated without bar lines (the Couperin file is a *mesuré* prelude and has bar lines, so
  it does not exercise this) would yield one bar and one "bar" class; L2 would receive almost no metric
  evidence — which is the truth of the notation.
- *Falsifier.* CODE. Observable: the class published for a score with no `<TimeSig>`. Decision rule:
  falsified if any class other than "bar" or "unmetered" appears. Not falsified by: a later
  signature change re-enabling the hierarchy from its position.

**S-13. Where a score does not supply voice membership beyond "one voice per staff", L0 supplies the
staff as the voice. L0 supplies *notated* voices only; a contrapuntal voice that the notation does not
mark is derived, not given, and no L1 computation may need it.**
- *Defense.* The charter: *"Voice membership is given … Here the voices are in the file"* [RULED],
  and S-1 (i): a notated voice is on the page, a contrapuntal line inferred through a chordal texture
  is not. The Brandenburg file has nine parts each on its own staff; the keyboard files have two
  notational voices per staff [FACT — §6]. §3.6's leading-tone cue is defined over notated voices and
  falls back to "any note" where the voice is not marked (S-46).
- *Source class.* Given (charter), sharpened.
- *Status.* Settled.
- *Premise.* Premise: notated voice is a usable proxy for a line. False-negative path: keyboard
  notation in which one notated voice carries a chord (the chorale file writes soprano and alto as
  two `<voice>` elements of one staff; a piano reduction might write both as one chord). The cue
  then sees a chord, not a line, and S-46's fallback fires. This is the pack's #17(d) proxy hazard,
  declared rather than hidden.
- *Falsifier.* CODE. Observable: the voice field. Decision rule: falsified if any L1 output depends on
  a voice assignment the record file does not carry. Not falsified by: L2 later deriving lines.

**S-14. Where a note's spelling is absent (a record with pitch numbers only), L0 refuses the score:
spelling is a required input and L0 does not infer it.**
- *Defense.* The charter's design point *"Spelling is given, not inferred"* [RULED]. Refusing rather
  than inferring keeps the input contract honest: an inferred spelling is derived and may not cross
  L0 → L1 (*"Nothing derived"*).
- *Source class.* Given (charter).
- *Status.* Settled.
- *Premise.* Premise: every score in scope carries spelling. False-negative path: MIDI-derived scores.
  Out of scope by the charter's own words.
- *Falsifier.* CODE. Observable: the L0 acceptance decision. Decision rule: falsified if a score with an
  unspelled note passes L0. Not falsified by: a score with a spelling the analysis later judges wrong —
  spelling is read, not judged.

---

## 3. L1 — change points, candidates and notated evidence

The charter's words, obeyed throughout: L1 *"Consumes: L0 only"*; publishes *"the ordered, covering,
gapless and non-overlapping list of slices — the stretches between consecutive change points, where a
change point is every onset and every release of an eligible note; per change point, its metric
strength class; per change point, the notated boundary evidence at it: bar line, fermata, rest, repeat
sign, double bar; the local cadence cues"*; and *"Decides nothing about the music. It bounds the search
and hands the next layer its covariates."* The charter's ground for releases — *"the identity of a
slice is the sounding note set rather than the octave-folded pitch-class set: a unison or octave shrink
is a real change though the pitch classes are unchanged"* — is given and is used at S-33.

### 3.1 Face (a) — what counts as a note event

**S-15. A notated note is *eligible* — it opens a change point at its onset and at its release, and it
belongs to the sounding set of every slice between them — if and only if it is pitched, it is not
marked as not to be played, it is visible, it is not a grace note, and its notated duration is
greater than zero. A tied continuation note is eligible but opens no onset (S-23).**
- *Defense.* Each condition is one L0 fact of S-3, and each removes a class the charter's *eligible*
  must exclude for the change-point set to mean *moments at which the sounding set changes*. Pitched:
  an unpitched sound has no place in a harmony (S-20). Played: a note marked silent does not sound,
  and the partition-point construction is defined over sounding pitches — *"the set of pitches
  currently sounding in the music changes by the onset or offset of one or more notes"* [FACT —
  Pardo & Birmingham 2002, pp. 28–29 and 35, as quoted in the pack's extract]. Visible: the analysis
  reads the notated text (S-1); an invisible note is not on the page and is a playback or layout
  device (S-18). Grace: a grace note has no metric duration of its own [FACT — MusicXML 4.0: the grace
  element's content is always empty; and Temperley 2009 p. 7 treats grace notes as *"extrametrical"*
  notes with *"an extremely low, but non-zero, probability"* of onset off the beat grid], so it has
  no position at which a sounding set could change distinct from its host's (S-16). Positive
  duration: a zero-duration non-grace note is a file defect (S-22).
- *Source class.* Derived.
- *Status.* Settled for the five conditions; the cases the conditions do not reach are OQ-2 (tremolo),
  OQ-4 (cue passages), OQ-5 (ossia), OQ-13 (invisible but played).
- *Premise.* Premise: the five L0 flags are reliable in the record file. False-negative path: a file
  that marks an editorial realisation of an ornament as visible, small and played (the C. P. E. Bach
  file marks such notes invisible and small, one of them not played [FACT — §6]); such a note would be
  eligible under S-15 and would open change points the page does not show. S-19 declares size alone
  insufficient to exclude it; the residual is OQ-4.
- *Falsifier.* CODE. Observable: the change-point set of a score. Decision rule: falsified if a
  change point exists whose only witnesses are ineligible notes, or if an eligible note's onset or
  release is absent from the set. Not falsified by: a change point witnessed by both an eligible and
  an ineligible note at the same position.

**S-16. A grace note opens no change point and belongs to no sounding set. It is published as an
*ornamental attachment* of its host note — the following main note for a grace before the beat or on
the beat, the preceding main note for a grace written after it — carrying its spelled pitch and its
notated form (slashed or unslashed, appoggiatura or acciaccatura where the file says).**
- *Defense.* No duration in the record (S-15's ground) [FACT — MusicXML; the staged files write
  `<grace16/>` and `<appoggiatura/>` chords with a `<durationType>` that is a display value and no
  place in the bar's duration sum — FACT, §6]. Music theory: an appoggiatura on the beat takes its
  time from its host, so its sounding onset *is* the host's onset; a pre-beat acciaccatura takes its
  time from the preceding note and sounds before the host's onset by an amount the notation does not
  fix [THEORY — standard performance-practice teaching; the MusicXML attributes
  `steal-time-previous` and `steal-time-following` encode exactly these two conventions, FACT]. Either
  way the notation supplies no rational position for the grace's own onset, so a change point there
  would be a performance decision, which L1 may not take [RULED — *decides nothing*]. Publishing the
  attachment keeps the information (#12): an on-beat appoggiatura a step above its host is dissonance
  evidence L2 will want [CONJECTURE on L2's want].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: a harmony never changes *at* a grace note as distinct from its host. False-
  negative path: a long appoggiatura written as a grace (eighteenth-century practice, the Couperin
  file's `<appoggiatura/>` cases) may sound for half the host's value; the harmony it belongs to
  begins at the host's onset regardless, and the appoggiatura's own pitch is in the attachment, so no
  harmonic fact is lost — only the sounding duration split, which is not notated.
- *Falsifier.* CODE. Observable: the change-point set and the attachments. Decision rule: falsified if
  a grace note's position appears as a change point, or if a grace note is absent from every
  attachment. Not falsified by: a grace note whose host is a rest (attach to the next eligible event;
  if none, to the marks list of S-41 — recorded as a corner, not a failure).

**S-17. An ornament sign on a note (trill, mordent, turn, and their variants) leaves the note the
event: the note's onset and release are the change points, and the sign is published as an
attribute of that event, by name, with no realisation.**
- *Defense.* The sign is on the page (S-1); its realisation — which auxiliary pitches sound, when,
  how many — is performance practice and varies by period and treatise [THEORY]; L1 realising it
  would be deciding [RULED]. The sounding-set argument of S-15 holds for the principal note: the
  ornament's auxiliaries are sung *around* it and the harmony is read on the principal. The Couperin
  and C. P. E. Bach files carry `ornamentShortTrill`, `ornamentTurn`, `ornamentTurnInverted` as
  articulations on ordinary chords [FACT — §6].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: the principal note is the harmonic note. False-negative path: a trill whose
  upper auxiliary is the chord tone and whose principal is an appoggiatura (the Baroque trill
  beginning on the upper note) — the harmony is still read on the principal at L1, and L2 receives
  the sign and may weigh the auxiliary; L1 publishes both (the sign names the auxiliary's diatonic
  relation, and the spelled pitch of the auxiliary is not in the notation, so it is not published).
- *Falsifier.* CODE. Observable: events and attributes. Decision rule: falsified if an ornament sign
  produces an event, a change point, or a member of any sounding set. Not falsified by: a written-out
  ornament in ordinary notes, which is ordinary notes.

**S-18. A note marked not to be played, and a note marked invisible, are ineligible (S-15). They are
carried beside L1's output as *silent notes*, labelled by which flag excluded them, and no layer
consumes them as evidence.**
- *Defense.* The played flag: a note the file says does not sound is not in the sounding set [the
  partition-point construction, FACT as at S-15]. The visible flag: the analysis reads the notated
  text (S-1 (i)), and a note the page does not show is not part of it. The staged C. P. E. Bach file
  shows the two flags used together on the same notes (`<visible>0</visible>`, `<small>1</small>`,
  and on the first of the group `<play>0</play>`) [FACT — §6]. Carrying rather than dropping: #12.
- *Source class.* Derived.
- *Status.* **Open** as to whether visibility governs when the played flag says the note sounds
  (OQ-13). Settled that a not-played note is ineligible.
- *Premise.* Premise: an invisible note is never part of the composer's text. False-negative path:
  a transcriber who hides a note for layout reasons (a doubled unison written once and hidden in one
  voice) — the note is in the text and would be lost. Its unison partner is visible, so the sounding
  set is unchanged; the loss is a voice-membership fact only.
- *Falsifier.* CODE. Observable: the sounding sets. Decision rule: falsified if a not-played note is in
  any sounding set. Not falsified by: OQ-13 being ruled the other way for invisible notes, which
  changes the rule and not the observable.

**S-19. Cue size (a note written small) does not by itself change eligibility. A small note that is
visible, played, pitched and of positive duration is eligible.**
- *Defense.* Size is a layout property; nothing on the page says a small note does not sound. In a
  full score a cue-sized passage marks a cue for a player, whose harmonic content duplicates another
  part; in a keyboard score small notes mark an editorial realisation or an *ossia*. The two cases
  have opposite right answers for the sounding set (a cue in an extracted part should not sound; a
  written-out realisation should), and the notation distinguishes them only by context [THEORY —
  engraving convention]. L1 may not read context to decide (RULED); so size is published as an
  attribute and eligibility is left to the flags. The remainder is OQ-4 and OQ-5.
- *Source class.* Derived.
- *Status.* Open (OQ-4, OQ-5).
- *Premise.* Premise: the record file's played flag is set correctly for cues. False-negative path:
  a cue passage exported with play on — then L1 would sound a duplicate of another part's music,
  which changes no pitch-class content but changes doubling and the bass where the cue is below the
  real bass. Declared.
- *Falsifier.* CODE. Observable: eligibility of small notes. Decision rule: falsified if a small note
  meeting S-15's five conditions is excluded. Not falsified by: a ruling on OQ-4 adding a sixth
  condition.

**S-20. An unpitched note (percussion, a rhythm-only staff) is ineligible and enters no sounding set.
It is not published by L1 at all.**
- *Defense.* A harmony is a set of pitches; an unpitched sound contributes none [THEORY]. Its onset
  might be metric evidence, but L1's metric strength class is read from the time signature (S-36), not
  from onsets, so nothing is lost that L1 publishes. Publishing it broadly for a future consumer
  (D-100's evidence-class rule) was considered and declined: nothing harmonic could be read from it
  and the charter's L1 outputs do not name it. [CONJECTURE — the decline is this session's.]
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: no later layer wants percussion onsets. False-negative path: a phrase-grouping
  consumer at L3 might; it may admit them through S-1 then. Declared dormancy is not claimed.
- *Falsifier.* CODE. Observable: sounding sets. Decision rule: falsified if an unpitched note is in
  one. Not falsified by: a pitched timpani note, which is pitched.

**S-21. Tremolo. This session does not derive the eligibility of tremolo-marked notes: no staged file
carries one (declared in the brief), and the two notational cases — a measured tremolo abbreviating
repeated notes, and an unmeasured tremolo sustaining a sonority — have different sounding sets. Written
as OQ-2 (face (a)); L1 publishes the mark (S-7) and treats the notated note as one event until ruled.**
- *Defense.* None beyond the brief's own instruction that a want the staged set does not supply is
  written as an open question and not filled.
- *Source class.* Derived (the interim treatment).
- *Status.* Open.
- *Premise.* Premise: the interim treatment (one event per notated note) is the less harmful default
  because it adds no change points the notation does not show. False-negative path: a two-note
  tremolo (two half-notes tremolo'd against each other) sounds as an alternation whose sounding set
  the interim treatment renders as a dyad; L2 sees an interval that never sounds together.
- *Falsifier.* RESIDUAL until ruled.

**S-22. A non-grace note with zero notated duration is a record defect: it is ineligible, and the
bar carries a defect flag (S-10).**
- *Defense.* A note of no duration cannot be in a sounding set over any slice, and treating it as an
  instantaneous onset would create a change point with nothing sounding after it — a slice of zero
  length, which S-30 excludes.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: such notes are always defects. False-negative path: a format that encodes grace
  notes as zero-duration notes without a grace flag — then they are graces (S-16), and L0 should map
  them so before L1; recorded.
- *Falsifier.* CODE. Observable: eligibility. Decision rule: falsified if a zero-duration non-grace
  note opens a change point. Not falsified by: the defect flag.

### 3.2 Face (b) — what a tie does

**S-23. A group of notes joined by ties is one event. Its onset is the first note's onset; its
release is the last note's release; its spelled pitch is the first note's; its voice is the first
note's. Only the first note opens an onset change point; only the last note opens a release change
point; the intermediate notes open nothing.**
- *Defense.* The tie's meaning in notation: one sound whose duration is the sum of the tied values
  [THEORY]. The MusicXML standard states it as a sound fact: *"The <tie> element indicates sound"*
  [FACT — fetched]. The partition-point construction is over sounding pitches beginning and ending
  [FACT — Pardo & Birmingham, as at S-15]: a tied continuation neither begins nor ends a sound.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: the record links tied notes explicitly. In the staged files every tie is a
  `<Spanner type="Tie">` with `<next>` and `<prev>` locations, including ties into the next bar and
  ties to a specific note of a following chord (`<notes>1</notes>`) [FACT — §6]. False-negative
  path: a tie drawn as a slur (S-24).
- *Falsifier.* CODE. Observable: the change-point set. Decision rule: falsified if the boundary between
  two tied notes is a change point with no other witness. Not falsified by: that boundary being a
  change point because another voice moves there.

**S-24. A tie link in the record counts as a tie only if the two notes have the same spelled pitch,
are in the same notated voice (or, across a staff change in one part, the same part), and are
adjacent in that voice with no event between them. A link failing any of these is not a tie: the two
notes are two events, and the bar carries a defect flag naming the link.**
- *Defense.* A tie joins the same pitch; a curve joining different pitches is a slur [THEORY]. A file
  can encode either as either; the pitch test is the only notated fact that separates them. Refusing to
  merge different pitches keeps the sounding set true to the page; refusing to repair the flag keeps L1
  from deciding what the transcriber meant [RULED — *decides nothing*].
- *Source class.* Derived.
- *Status.* Settled, with one open corner: a tie across an enharmonic respelling (the same sounding
  pitch, different letter, across a key-signature change) — OQ-7.
- *Premise.* Premise: same spelled pitch is the right test. False-negative path: OQ-7 exactly — an
  enharmonic tie fails the test and is split into two events with a release and an onset the music
  does not have. The defect flag makes the split visible.
- *Falsifier.* CODE. Observable: events formed from links. Decision rule: falsified if two notes of
  different spelled pitch are merged into one event. Not falsified by: OQ-7's ruling adding an
  enharmonic-equivalence clause.

**S-25. A tie whose continuation is missing (the file marks a tie start with no tie end, or the
linked note does not exist) ends the event at the first note's notated release; the bar carries a
defect flag.**
- *Defense.* The notated release is the only position the record supplies; extending the sound to an
  unknown end would invent a duration. A tie into nothing is common at the end of a repeat section
  where the continuation is the section's first bar (S-27) and at an *l.v.* (let vibrate) mark, where
  the release is genuinely unnotated; both are covered by publishing the notated release and the
  flag, so L2 can weigh it.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: a missing continuation is either a defect or a let-vibrate. False-negative path:
  a tie continuing into a bar outside the working span (S-53) — the flag would fire on a span edge
  that is not a defect; L1 marks span-edge ties as "cut by the span", not as defects.
- *Falsifier.* CODE. Observable: events and flags. Decision rule: falsified if a dangling tie extends an
  event past the first note's release. Not falsified by: the span-edge case carrying its own mark.

**S-26. A tie across a bar line creates no change point at the bar line. The bar line's boundary
evidence is then not attached to a change point but to the positioned marks list (S-41), and the
metric class of the bar's start is published there too.**
- *Defense.* Change points are onsets and releases only [RULED — charter]; a sustained sound crosses
  the bar line without either. The chorale file has such ties (a dotted half tied into a fermata half
  in the next bar) [FACT — §6]. Nothing about the music is lost: a harmony cannot begin where nothing
  begins, so the bar line is not a candidate; but the notation's *fact* that a bar began there is
  information for L2's weighing of the next change point and for L3's phrase reading, so it is
  published where it can be found (S-41). [CONJECTURE on the consumers.]
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: a harmony never changes with no note beginning or ending. It is the charter's
  own premise, and its false-negative path is the one the charter names as impossible by construction
  (*"a real harmony change can never be missed"*); this derivation adds none.
- *Falsifier.* CODE. Observable: change points at bar lines. Decision rule: falsified if a bar line with
  every voice tied across it is a change point. Not falsified by: a bar line where one voice's tie
  continues and another voice moves — that is a change point, with the bar-line flag on it.

**S-27. A tie whose continuation lies across a repeat sign or in a different ending is honoured as
the record links it: the event's release is the linked note's release, in notated order. Whether the
analysis works in notated or unfolded order is OQ-1; until ruled, L1 publishes over notated order and
additionally publishes the *junction adjacencies* the repeat structure implies (for each end-repeat
and each ending, which slice would follow which on which pass), so that L2 can read across a repeat
without L1 having decided the order.**
- *Defense.* The C. P. E. Bach file ties a note in a first-ending bar into the following bar, and its
  end-repeat bar carries `<endRepeat>2</endRepeat>` [FACT — §6]. In notated order the link is
  honoured as written. Publishing the junctions rather than unfolding follows *decides nothing*: an
  unfolding is a performance reading; the DCML Mozart-sonatas corpus reports that its harmony labels
  *"had to be unfolded according to the repeat structures of the individual movements"* [FACT —
  Hentschel et al., TISMIR, fetched — the sentence only; the article defines no procedure], which
  shows that published ground truth may be in either order and that the choice is consequential for
  measurement.
- *Source class.* Derived.
- *Status.* Open (OQ-1).
- *Premise.* Premise: notated order loses no harmonic fact that the junction list cannot restore.
  False-negative path: a tie from an end-repeat bar into the section's first bar on the repeated pass
  exists only in unfolded order; in notated order the tie start dangles (S-25 flags it) and the
  junction list says where it goes. A consumer that reads neither would miss the sustained note on the
  second pass.
- *Falsifier.* CODE. Observable: events near repeat signs. Decision rule: falsified if an event's
  release is placed at a position other than its linked note's release. Not falsified by: OQ-1 being
  ruled for unfolded order, which changes the time axis and not the linking rule.

### 3.3 Face (c) — the change-point set and the slices

**S-28. Two onsets or releases are the same change point if and only if their metric positions are
equal as rational numbers. There is no tolerance: two events a thirty-second apart are two change
points, and the slice between them is a slice.**
- *Defense.* The record gives positions as exact fractions (MuseScore's `<Division>480` ticks and
  `<fractions>` locations; MusicXML's divisions) [FACT — §6]. The charter's set is *exhaustive*: *"every
  moment at which the sounding set changes opens a candidate"* [RULED]. A tolerance would merge
  distinct moments and could delete a real candidate, which the charter's construction exists to make
  impossible. The cost — very short slices in florid textures — is L2's to weigh, not L1's to
  pre-empt; Pardo & Birmingham bound the count at twice the note count and report 341 partition points
  in a 21-bar Sinfonia [FACT — extract, p. 36].
- *Source class.* Derived (the charter fixes exhaustiveness; this fixes the equality test).
- *Status.* Settled.
- *Premise.* Premise: the record's positions are exact. False-negative path: a record produced from a
  performance (MIDI) would carry jitter and every near-coincidence would split; the charter's L0
  excludes performance input (*"Meter is given"*), so the path is closed at L0.
- *Falsifier.* CODE. Observable: the change-point set. Decision rule: falsified if two eligible events
  with unequal onset positions share a change point, or two with equal positions do not. Not falsified
  by: a grace note's display position differing from its host's — the grace has no position (S-16).

**S-29. A slice is the half-open interval from its change point to the next: a change point belongs
to the slice it starts. The sounding set of the slice starting at t is the set of eligible events
whose onset is at or before t and whose release is after t.**
- *Defense.* An event sounds at its onset and does not sound at its release [THEORY — the meaning of a
  notated duration: a quarter note starting at beat 1 occupies [1, 2), and the next note in that voice
  starts at 2]. The two facts together force the half-open convention: the alternative (a change point
  belonging to the slice it ends) would put a note's release inside the slice in which it still sounds
  and its onset in the slice before it sounds. The convention is therefore not a choice but a
  consequence of what onset and release mean. It also makes *covering, gapless, non-overlapping*
  hold by construction. [CONJECTURE only in the claim that no other convention is consistent; the
  derivation is elementary.]
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: releases are instantaneous. False-negative path: none for notation.
- *Falsifier.* CODE. Observable: the sounding set at a change point. Decision rule: falsified if an
  event whose release equals t is in the sounding set of the slice starting at t, or an event whose
  onset equals t is absent from it. Not falsified by: a tied continuation (S-23), which has no onset
  or release at the tie boundary.

**S-30. No slice has zero length. This holds by construction, since change points are distinct
positions (S-28) and grace notes have none (S-16); L1 asserts it as an invariant and treats a
violation as an internal error, never as a case to handle.**
- *Defense.* Follows from S-28 and S-16. The brief asks what is done if the notation implies a
  zero-length slice; the answer is that the notation cannot: every candidate for one (a grace, a
  zero-duration note) is excluded from the change-point set before slices are formed (S-16, S-22).
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: S-16 and S-22 are complete over the zero-duration cases. False-negative path: a
  format with a zero-duration *chord symbol* or *breath mark* encoded as a note — excluded by S-2 and
  S-7 respectively.
- *Falsifier.* CODE. Observable: slice lengths. Decision rule: falsified if any published slice has
  length zero. Not falsified by: two consecutive silent slices of positive length.

**S-31. A silent slice — one whose sounding set is empty — is published as a slice like any other,
with its empty set, and is not merged into a neighbour.**
- *Defense.* *Covering* and *gapless* require it [RULED — charter]. Silence is a notated fact and
  strong boundary evidence (the charter names *rest* among the five) — merging it away would lose the
  evidence and would decide that the harmony before the silence continues through it, which is L2's
  question. [RULED — *decides nothing*.]
- *Source class.* Given (the charter's *covering, gapless*) and derived (the non-merging).
- *Status.* Settled.
- *Premise.* Premise: L2 can consume an empty sounding set. False-negative path: a consumer that
  divides by the set's size; a specification concern for L2, recorded.
- *Falsifier.* CODE. Observable: the slice list over a general pause. Decision rule: falsified if the
  slices do not cover the pause or if the pause is absorbed into an adjacent slice. Not falsified by:
  the pause being one slice rather than several — it has one change point at each end.

**S-32. The published slice list covers the working span exactly. Its first change point is the span's
start; its last is the span's end. If no eligible event begins at the span's start, the first slice is
a silent slice or a slice whose sounding set consists of events that began before the span (marked
*entered sounding*); events that release after the span's end are marked *cut by the span*.**
- *Defense.* The analysis works on a selection and whole-score analysis is the degenerate case
  [RULED — D-030, D-031]; the covering property is relative to the span [RULED — charter]. Marking
  entered and cut events keeps the span's edges honest (#12) and lets L2 know that the first slice's
  onsets are not real onsets.
- *Source class.* Given (D-030/D-031 and the charter), derived in the marking.
- *Status.* Settled.
- *Premise.* Premise: the span is a contiguous stretch in the working order. False-negative path: a
  span in unfolded order crossing a repeat junction (OQ-1).
- *Falsifier.* CODE. Observable: the first and last change points. Decision rule: falsified if they
  differ from the span's ends, or if an event sounding across the span's start lacks the *entered*
  mark. Not falsified by: a span starting at a real onset, where the mark is simply absent.

**S-33. Slice identity is the set of events (by note identity), not the set of pitch classes and not
the set of pitches: a unison or octave doubling beginning or ending is a change point, and two slices
with the same pitch-class content but different event sets are different slices.**
- *Defense.* The charter's own words, quoted at the head of §3 [RULED]. Nothing is added.
- *Source class.* Given.
- *Status.* Settled.
- *Premise.* The charter's; its false-negative path (a change point that L2 will always find
  harmonically inert) is by design harmless — L2 may keep the harmony across it.
- *Falsifier.* CODE. Observable: change points at doubling onsets. Decision rule: falsified if an
  octave doubling's onset is not a change point. Not falsified by: L2 merging across it.

### 3.4 Face (d) — metric strength

**S-34. L1 derives, from each time signature in force, a *notated metrical hierarchy*: an ordered list
of levels, each a period and a phase within the bar, from the bar downward. For a simple meter with
numerator 2 or 3: the bar; the beat (the denominator's value); then successive halvings of the beat.
For a simple meter with numerator 4: the bar; the half-bar; the beat; then halvings. For a compound
meter (numerator 6, 9, 12 over 8 or 16): the bar; for 12, the half-bar; the dotted beat (three
denominators); the denominator; then halvings. For other numerators (5, 7, and additive signatures)
L1 publishes only the bar and the denominator levels. Halvings continue down to the finest notated
division present in the score.**
- *Defense.* The hierarchy of beats and their regular subdivision is the content of the notated meter
  in common-practice theory: the time signature names the beat and the bar, and Western notation
  divides the beat in twos, or in threes for compound meter [THEORY — the metrical hierarchy of
  Lerdahl & Jackendoff's generative theory, and standard textbook meter; not fetched — book sources].
  Temperley's model assumes the sub-tactus level *"duple, given that in Western music a triple
  division of the sub-tactus level is extremely rare"* [FACT — Temperley 2009, p. 7, fetched], which
  is why halvings are the default below the beat. The half-bar level for 4/4 and 12/8 is the standard
  reading of those signatures as two groups of two beats (the third beat is stronger than the second
  and fourth) [THEORY]. Irregular numerators have no standard grouping without a grouping annotation,
  which the notation may not supply, so only the two levels the signature itself names are published
  (S-1: nothing not on the page).
- *Source class.* Derived.
- *Status.* Settled for the named signatures; open for additive and irregular meters beyond the two
  levels (OQ-8 also covers a mid-bar signature change).
- *Premise.* Premise: the notated signature's conventional hierarchy is what the composer's meter is.
  False-negative path: 3/2 written for a passage in 6/4 feel, or 6/8 written for a passage in 3/4 feel
  (hemiola): the hierarchy is then wrong about the sounding accent. L1 publishes the notated hierarchy
  and says so (S-38); the sounding accent is derived and not L1's.
- *Falsifier.* CODE. Observable: the level list per signature. Decision rule: falsified if, for 4/4, beat
  3 receives the same level as beat 2, or for 6/8, the fourth eighth receives the same level as the
  second. Not falsified by: a different number of halving levels below the beat, which depends on the
  score's finest division.

**S-35. The metric strength class of a change point is the *highest* level of the hierarchy in force
at which the change point's position is a beat of that level; it is published as an ordinal (0 for
the bar, 1 for the next level down, and so on) together with the level's period, so that classes from
different signatures are comparable by period as well as by rank. A position on no level (a tuplet
subdivision that aligns with no halving) receives the class *off-grid*, ranked below every level.**
- *Defense.* The charter fixes that this is a class read from the time signature, the bar line and
  the position within the bar, not a judgment [RULED]. The "highest level" rule is the standard
  definition of metrical strength: a beat's strength is the number of levels at which it is a beat
  [THEORY — Lerdahl & Jackendoff's metrical grid; Temperley's levels 0–3 with the tactus at level 2,
  FACT — Temperley 2009 p. 7]. The charter's own evidence that this class carries information is stated
  over exactly three levels: harmonic change at 71.5% of the beats at the level above the tactus,
  22.3% at the tactus, 2.4% at the level below [FACT — Temperley 2009 Table 1, p. 5, fetched; the
  charter carries the same figures after its 2026-08-31 correction]. Publishing the period beside
  the rank is needed because a rank-1 class in 3/4 (the beat) and in 4/4 (the half-bar) are not the
  same thing; a consumer comparing scores needs the period. *Off-grid* rather than "nearest level":
  rounding would assert a beat the notation does not write.
- *Source class.* Derived (the charter gives that it is a class).
- *Status.* Settled.
- *Premise.* Premise: the three-level evidence generalises to more levels and to the half-bar level.
  False-negative path: the measured evidence is on the Kostka–Payne excerpts, spanning Bach through
  Tchaikovsky [FACT — Pardo & Birmingham's description of the same corpus, extract p. 27, 31]; for
  Baroque continuous textures the gradient may be flatter. A measurement over this project's own
  ground truth would decide it — UNESTABLISHED; L1 publishes the class regardless, and L2's weighting
  is where the measurement bites.
- *Falsifier.* CODE. Observable: the class per change point. Decision rule: falsified if a change point
  at a bar start in a metered score receives any class but 0, or if a change point at beat 3 of 4/4
  receives the same class as beat 2. Not falsified by: a score in 4/4 whose finest division is the
  eighth having only four levels.

**S-36. In an anacrusis — a bar marked irregular whose actual length is shorter than the signature's
bar — positions are assigned to levels by aligning the bar's *end* with the end of a nominal bar: the
offset used for the hierarchy is (nominal length − actual length + offset from the bar's start). The
bar's start is therefore not class 0 unless the alignment makes it so, and the first full bar's start
is class 0.**
- *Defense.* An anacrusis is the tail of a notional bar whose downbeat is the first full bar's start
  [THEORY — the meaning of a pickup]. The chorale file opens with a one-quarter bar (`len="1/4"`) and
  the Couperin file with a two-quarter bar marked `<irregular>1</irregular>` [FACT — §6]; in both,
  the notation's own downbeat is the next bar line, and a class-0 label on the pickup would contradict
  the page. The same rule serves an incomplete bar after a repeat sign or a double bar (the chorale's
  `len="3/4"` bars before its signature changes) — where such a bar is the *head* of a notional bar
  rather than its tail, the alignment is from the start; the record marks which by the bar's position
  relative to the signature change and the repeat, and where it does not, the case is OQ-8.
- *Source class.* Derived.
- *Status.* Settled for the leading anacrusis; OQ-8 for ambiguous short bars.
- *Premise.* Premise: an irregular short bar at a piece's start is always a pickup. False-negative
  path: a piece that begins on a downbeat with a deliberately short first bar (rare; a notational
  quirk) — the alignment would shift its downbeat. Declared.
- *Falsifier.* CODE. Observable: the class of the first change point of the chorale file. Decision
  rule: falsified if it is class 0. Not falsified by: the first full bar's start being class 0.

**S-37. At a time-signature change, the hierarchy in force changes at the change's position; a change
point at that position takes its class from the new hierarchy; the bar containing the change is
measured from the change's position.**
- *Defense.* The signature governs what follows it [THEORY — notation]. The chorale file changes
  signature at bar starts [FACT — §6]. A change mid-bar is OQ-8.
- *Source class.* Derived.
- *Status.* Settled for changes at a bar line; OQ-8 otherwise.
- *Premise.* Premise: signature changes fall on bar lines. False-negative path: OQ-8.
- *Falsifier.* CODE. Observable: classes after a change. Decision rule: falsified if the first bar after
  4/4 → 3/4 publishes a half-bar level. Not falsified by: the change-point at the change being class 0.

**S-38. L1 publishes the *notated* metric strength class only. Where the sounding accent disagrees with
the notated meter (hemiola, syncopation, a written meter that differs from the felt one), L1 publishes
nothing about it: the disagreement is a reading of the music and belongs to a later layer.**
- *Defense.* *"a CLASS and not a judgment"* [RULED — the brief's restatement of the charter]; *decides
  nothing* [RULED]. Temperley & Sleator's system infers meter from onsets and reports an unsolved
  circularity between meter and harmony as a result [FACT — extract, p. 25]; the charter's ground for
  giving meter is to avoid exactly that, and a sounding-accent reading at L1 would reintroduce it.
- *Source class.* Given (charter), derived in the consequence.
- *Status.* Settled.
- *Premise.* Premise: L2 can recover a hemiola from the notated class plus the notes. False-negative
  path: it cannot from L1's outputs alone if it needs the felt accent as an input; then a metric-
  reading layer would be owed, admitted by the charter's three gates for a new layer (D-034). Recorded.
- *Falsifier.* CODE. Observable: L1's outputs on a hemiola passage. Decision rule: falsified if any L1
  output differs between the passage and a re-notation of it with the same signature and the same
  positions but different beaming or stem direction. Not falsified by: the outputs differing when the
  signature is changed — that is the notated meter.

### 3.5 Face (e) — the notated boundary evidence

**S-39. Per change point, L1 publishes a set of boundary flags, each with its witnesses: BAR-LINE
(the change point is a bar start; carrying the bar-line type — single, double, final); REPEAT (a
start-repeat, an end-repeat with its count, an ending start, an ending end, at this position);
FERMATA (an event bearing a fermata *releases* at this change point; or a fermata-bearing rest's
silence *ends* here; or a fermata stands on the bar line at this position); REST-BEGINS (a notated
voice's silence begins at this change point, by rest or by unwritten gap, naming the voice); and
ALL-SILENT (the slice starting here is a silent slice).**
- *Defense.* The five kinds are the charter's [RULED]. The placement rules are this derivation's,
  from what each sign means: a fermata prolongs the note it sits on, so the boundary it signals is
  where that note *ends* [THEORY]; a fermata over a rest prolongs the silence, so its boundary is
  where the silence ends [THEORY]; a rest marks where a voice stops, which is the change point at the
  preceding event's release [THEORY]. The chorale file's fermatas sit on the final note of each
  phrase, some of them tied notes whose release is the change point [FACT — §6]. Publishing the voice
  with REST-BEGINS keeps the difference between one voice resting and all resting, which the charter's
  bare *rest* does not separate and a phrase reader needs.
- *Source class.* Given (the five kinds), derived (placement and witnesses).
- *Status.* Settled.
- *Premise.* Premise: a fermata's boundary is at the release. False-negative path: a fermata on the
  *first* chord of a phrase (a held opening sonority) — its release is a change point too, and the flag
  fires there, which is where the hold ends; a phrase reader would then see a flag at a non-boundary.
  The flag is evidence, not a decision; the near-miss is L3's to weigh.
- *Falsifier.* CODE. Observable: flags at the chorale's phrase ends. Decision rule: falsified if a
  fermata-bearing note's release change point lacks FERMATA, or if a fermata attaches to that note's
  onset. Not falsified by: an onset and a release coinciding at one change point, carrying both a
  FERMATA (from the releasing note) and no fermata from the starting one.

**S-40. Several marks at one change point are published as several flags in the set; nothing is
collapsed to a single "boundary strength". A repeat sign coinciding with a double bar and a fermata
yields three flags.**
- *Defense.* Combining flags into one number would be a judgment of their joint weight [RULED — decides
  nothing], and would lose the parts (#12). The chorale file's end-repeat bar carries a fermata and
  a repeat sign together [FACT — §6].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: L2 and L3 weigh the flags. Its false-negative path is none at L1.
- *Falsifier.* CODE. Observable: the flag set at that bar. Decision rule: falsified if fewer flags than
  marks are published. Not falsified by: a flag carrying two witnesses.

**S-41. A boundary mark that stands at a position that is not a change point — a double bar mid-bar,
a fermata over a bar line every voice ties across, a repeat sign at a bar line under a held chord —
is published in a *positioned marks list*: each mark with its position, its kind and its witnesses,
and with the metric strength class of its position. The marks list is a second L1 output beside the
per-change-point flags, and the two never duplicate a mark.**
- *Defense.* #12: a notated mark is information, and attaching it to the nearest change point would
  misplace it (a decision), while dropping it would lose it. Metric class is published with it
  because the class of a bar start under a held chord (S-26) is otherwise unpublished, and the
  charter's *"per change point"* wording leaves the case open rather than forbidding the list. This
  extends the charter's output shape; it is written as a derived statement for ruling. [CONJECTURE on
  the extension's acceptability.]
- *Source class.* Derived.
- *Status.* Settled as a proposal; flagged for ruling because it adds an output.
- *Premise.* Premise: consumers will read two structures. False-negative path: a consumer that reads
  only the per-change-point flags misses every mark under a held chord. Declared; the alternative
  (attaching to the next change point with a "displaced" mark) was considered and declined because it
  places a mark at a moment the page does not show it.
- *Falsifier.* CODE. Observable: both outputs. Decision rule: falsified if a mark appears in both or in
  neither. Not falsified by: the list being empty on a score where every mark is at a change point.

**S-42. A repeat whose ending differs on the second pass (voltas) is published as REPEAT flags at the
ending's start and end, with the ending numbers, and as junction adjacencies (S-27). L1 does not
publish which ending "follows" the repeated section; both do, on different passes, and the flags say
which pass.**
- *Defense.* The C. P. E. Bach file has a first ending (`<Volta>… <endings>1</endings>`) spanning
  bars before its end-repeat, and a second ending after [FACT — §6]. The notation gives both; choosing
  one is unfolding (OQ-1).
- *Source class.* Derived.
- *Status.* Open with OQ-1.
- *Premise.* Premise: ending numbers are in the record. False-negative path: a file with voltas drawn as
  text; then the ending is annotation (S-2) and the repeat structure is incomplete — a defect flag.
- *Falsifier.* CODE. Observable: flags at the volta. Decision rule: falsified if either ending lacks its
  REPEAT flags with numbers. Not falsified by: OQ-1's ruling.

**S-43. This derivation proposes two additions to the charter's five kinds, as evidence and not as
decisions: a TIME-SIGNATURE-CHANGE flag and a KEY-SIGNATURE-CHANGE flag at the position of a change.
Both are notated, both are commonly used by composers to mark a section, and the second is the one
place a key signature enters L1 — as the *fact that it changed*, never as its value.**
- *Defense.* Both pass S-1 and both are section-level notation in common practice [THEORY]. The
  key-signature-change flag does not read the signature's value, so S-9's bar is respected: the flag
  is true when the signature-in-force changes and says nothing about the tonality before or after.
  The chorale file's two signature changes fall at phrase boundaries with fermatas [FACT — §6; a
  single file, not evidence of a rate].
- *Source class.* Derived — an extension, for ruling.
- *Status.* Open (an addition to a ratified list is the user's).
- *Premise.* Premise: the flag conveys no tonality. False-negative path: a consumer that reads "key
  signature changed" as "tonality changed" — it would be consuming a sign as a decision; the flag's
  name and its establishment status (S-52) say it is a sign.
- *Falsifier.* CODE. Observable: L1 outputs under a key-signature change with all pitches respelled to
  keep the notes identical. Decision rule: falsified if any L1 output beyond this flag changes. Not
  falsified by: the flag itself.

### 3.6 Face (f) — the local cadence cues

**S-44. Cues are computed at onset change points only (a release is never a cadential arrival), and
every cue is defined over the *bass*, which at a slice is the lowest sounding pitch of that slice's
sounding set — not a notated voice.**
- *Defense.* A cadence arrives on an attack [THEORY]. Bigo et al. compute their features at each beat
  for an arrival Z and anchor them on *"the bass of Z"*, finding the preparation by *"the latest beat
  before Y whose lowest sounding note has a different pitch (modulo octave) than the lowest note of
  Y"* [FACT — extract, §2.3–2.4] — the lowest sounding note, not a voice. With voice membership given
  (S-13) a notated bass voice exists in most scores, but the lowest sounding pitch is the harmonic bass
  even when a voice crosses below it, and it is defined on every score.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: the lowest sounding pitch is the harmonic bass. False-negative path: an Alberti
  or arpeggiated texture where the lowest pitch of a short slice is not the harmony's bass (the
  pack's ledger, C32 and C38, records this shape as measured); the cue then fires or fails on a
  passing bass. The cue carries its witnesses and the slice's length, and the weighing is L2's. This
  is the pack's #17(d) proxy hazard, declared.
- *Falsifier.* CODE. Observable: cue firings. Decision rule: falsified if a cue fires at a release-only
  change point. Not falsified by: a cue firing at a change point that is both a release and an onset.

**S-45. BASS-FALLS-A-FIFTH (equivalently rises a fourth): at onset change point Z, let Y be the latest
earlier slice whose bass pitch class differs from Z's bass pitch class, searched back no further than
the cue window (S-48). The cue is true when Y's bass pitch class is seven semitones above Z's bass
pitch class modulo twelve (Y = Z + 7). Published with witnesses: the two bass notes, the register of
the motion (down a fifth, up a fourth, or across an octave), and the slices Y and Z. The cue is not
computed when no such Y exists in the window.**
- *Defense.* Falling fifth and rising fourth are the same pitch-class relation and differ only in
  register, which is why the charter names them together [THEORY]. Bigo et al.'s
  `Y-Z-bass-moves-compatible-V-I` is this relation between the bass of Y and the bass of Z [FACT —
  extract, §2.1–2.4]; the anchor Y by *differing bass* rather than *previous slice* is theirs too (X is
  found by the same rule one step further back). Register is published rather than folded because a
  bass leap down a fifth and up a fourth are the same harmonically but not the same in voice leading,
  and Sears et al. found that cadential bass motion *in isolation* is less predictable than stepwise
  motion [FACT — extract, §6.1.3], so a consumer may want the registral form.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: the previous *differing* bass is the right Y. False-negative path: a cadence whose
  dominant bass is decorated by a lower neighbour immediately before the arrival — Y is then the
  neighbour and the cue fails; the pack's C41 shape (evidence arrives after the moment). L2 can look
  two steps back with the published slices; the cue is one pattern, not the only evidence.
- *Falsifier.* CODE. Observable: the cue on a plain V–I in root position. Decision rule: falsified if it
  is false there, or true on a I–IV. Not falsified by: it being true on a IV–♭VII in another tonality —
  the cue is tonality-free by design.

**S-46. LEADING-TONE-RESOLVES: at onset change point Z, the cue is true when some eligible event in the
slice before Z, in a notated voice, is a semitone below Z's bass pitch class (modulo twelve), and an
event in the same notated voice onsets at Z on Z's bass pitch class (in any octave). Published with
witnesses: the two notes and the voice. Where the record carries no voice below the staff (S-13), the
same-voice condition is relaxed to *any note* and the relaxation is published as part of the cue.**
- *Defense.* A leading tone is the pitch a semitone below a tonic, resolving up to it [THEORY]. Without
  a tonality the only tonic available is a hypothesis, and the charter's own third cue supplies the
  hypothesis: the bass of the arrival (S-47). Bigo et al.'s `Z-β-comes-from-α` features are voice-
  leading features of the arrival — *"an immediate resolution of one degree to another"* — relative to
  the arrival chord [FACT — extract, §2.1–2.4]. Requiring the same notated voice makes it a
  *resolution* rather than a coincidence; the relaxation is declared because S-13 says notated voice
  is a proxy.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: the resolving voice is a notated voice. False-negative path: keyboard textures
  where the leading tone and its resolution are in one voice that carries chords; the relaxation fires
  and the cue becomes weaker. The published relaxation flag lets L2 weigh it.
- *Falsifier.* CODE. Observable: the cue on a V–I with the leading tone in the soprano resolving to the
  tonic. Decision rule: falsified if false there, or true when the semitone-below note resolves
  elsewhere in its voice. Not falsified by: it being true on a deceptive resolution's leading tone —
  the bass at Z is then not the tonic and the cue is false; if it is true, the bass IS the pitch the
  leading tone resolved to, which is what it detects.

**S-47. FOURTH-AND-SEVENTH-IN-THE-APPROACH: at onset change point Z, for each of two candidate
tonalities — T_I, whose tonic is Z's bass pitch class, and T_V, whose dominant is Z's bass pitch class
(tonic = bass − 7 modulo twelve) — the cue is true when both the fourth degree and the seventh degree
of that candidate (tonic + 5 and tonic + 11 modulo twelve) sound among the eligible events of the
slices within the cue window before Z. Published as two flags, each named by its anchor (*I-anchored*,
*V-anchored*), with witnesses. The candidate tonality is the anchor and nothing more: L1 publishes no
tonality.**
- *Defense.* This is Bigo et al.'s `Z-bass-compatible-with-I` and `-with-V`: *"Both notes 4 and 7 of the
  tonality that would be implied by the bass of Z are present in the four beats before Z"* [FACT —
  extract, §2.1]; the pack's extract records that *"the phrase candidate tonality is therefore not
  loose — it names a hypothesis anchored on a note the score gives, which is what keeps the cue inside
  L1's decides nothing rule."* The V-anchor is the half-cadence hypothesis; the charter's evidence that
  the half cadence is weak on local cues (F .29 and .41) [FACT — extracts, Bigo Table 3 and
  Karystinaios & Widmer Table 2] is a reason to publish the V-anchored flag as weak evidence, not a
  reason to omit it: omitting would decide. The seventh degree here is the major seventh above the
  tonic in both modes (the leading tone), because the cue is about dominant function, which uses the
  raised seventh in minor [THEORY].
- *Source class.* Derived.
- *Status.* Settled as to definition; the window is S-48.
- *Premise.* Premise: the leading tone (tonic + 11) is the right seventh in minor. False-negative
  path: a modal or Phrygian cadence in which the seventh is not raised — the cue is false there, which
  is correct for a cue named after dominant function; but a consumer expecting "any cadence" would
  miss it. The name of the flag says what it detects.
- *Falsifier.* CODE. Observable: the I-anchored flag at the arrival of a plain ii–V–I. Decision rule:
  falsified if false there (the fourth is in ii and the seventh in V), or true when neither degree has
  sounded in the window. Not falsified by: it being true at a non-cadential tonic arrival — the cue is
  evidence, and its false-positive rate is L2's to learn.

**S-48. The cue window — how far before Z the approach is searched, for S-45's Y and for S-47's
degrees — is a parameter L1 carries. Its value is UNESTABLISHED for this project's repertoire. The
measurement that would set it: over the ground-truth corpora, the distribution of the distance in
tactus beats from the last sounding of the fourth and seventh degrees to the annotated cadential
arrival, and the recall of S-45 as a function of the look-back. Until measured, L1 carries the
published values — four beats for the degrees, one bar for the bass anchor — as declared stand-ins.**
- *Defense.* Bigo et al. use four beats before Z for the degree features and one bar for the Y search,
  with a beat unit chosen per corpus — a quarter for Haydn, an eighth for Bach *"to cope with the faster
  harmonic rhythm"* [FACT — extract, §2.1, §2.3, Figure 3]. That per-corpus choice is itself evidence
  that the window is repertoire-dependent and must be measured here, not copied; the pack's principle
  #19 forbids trusting a copied value, and #17's desk-simulation rule marks a hand-declared stand-in as
  provisional.
- *Source class.* Measured — UNESTABLISHED, no value asserted.
- *Status.* Open (a measurement is owed; a ruling on the stand-in is the user's).
- *Premise.* Premise: a fixed window in beats is the right shape. False-negative path: the window
  should perhaps be in slices or in bars; the measurement above would show it if recall depends on
  texture more than on beats. Declared.
- *Falsifier.* RESIDUAL until measured; thereafter CODE: the window in use equals the ruled value.

**S-49. Every cue is published together with the interval content above the bass at Y and at Z — the
set of pitch classes sounding in each slice, expressed as semitone distances above the slice's bass —
so that a consumer can read the bass motion *in relation to what sounds above it*. L1 publishes the
set; it names no chord.**
- *Defense.* Sears et al. found that the cadential bass leap considered in isolation is *less*
  predictable than stepwise motion, and that only viewpoints modelling *"the interaction between the
  bass and the upper voices"* recover the expected direction [FACT — extract, §6.1.3]; the pack's
  extract routes to the L1 detail specification the statement *"a cue defined over the bass alone can
  have the wrong sign; the cue is the bass motion IN RELATION to what sounds above it."* Bigo et al.'s
  Y features (`Y-has-7`, `Y-in-V7`) read the same content [FACT — extract, §2.1–2.4]. Publishing the
  raw interval set rather than a quality label keeps L1 from deciding a chord.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: the interval set is recoverable from L1's published sounding sets anyway, so this
  is a convenience, not new information; it is published once here so consumers do not re-derive it
  (D-100). False-negative path: none; if it were dropped, L2 would compute it from the sounding set.
- *Falsifier.* CODE. Observable: the published set at a slice. Decision rule: falsified if it names a
  quality or a root, or if it differs from the sounding set's pitch classes minus the bass. Not
  falsified by: the same set being published for two slices with different event sets.

### 3.7 Face (g) — the form of what is published, and the bar on deciding

**S-50. L1 publishes exactly: the slice list (S-29–S-33) with each slice's sounding set by event
identity; per change point, its metric strength class (S-35) and its boundary flag set (S-39); the
positioned marks list (S-41); the junction adjacencies (S-27); per onset change point, the cue flags
(S-45–S-47) with the interval content (S-49); the ornamental attachments and ornament attributes
(S-16, S-17); the silent-notes and annotation carriers (S-2, S-18); and the defect flags (S-10, S-24,
S-25). Every predicate is published with its witnesses. No published field is named *boundary*,
*cadence*, *phrase*, *chord*, *key*, *tonality*, *degree* or *function*.**
- *Defense.* The charter's list, plus the additions each derived above [RULED for the list; derived
  for the additions, each flagged where it stands]. The naming bar operationalises *decides nothing*:
  a field's name is what a consumer will treat it as, and a flag named *cadence* would be consumed as
  a decision however it was computed. The pattern names (BASS-FALLS-A-FIFTH) say what was detected and
  nothing about what it means.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Premise: naming discipline is enforceable. False-negative path: a consumer that re-labels
  the flag internally — outside L1's reach; recorded.
- *Falsifier.* CODE. Observable: L1's output schema. Decision rule: falsified if a field bears one of the
  barred names or if a predicate lacks witnesses. Not falsified by: documentation using the word
  *cadence* to explain what a cue is evidence for.

**S-51. The test for whether an L1 output is a *claim* the charter forbids: an output is a candidate or
evidence, not a claim, if and only if it is computable from L0 facts with no tonality, chord or
boundary as input, and it is published under a name that states the pattern detected rather than a
musical conclusion. By this test a cue is not a claim, a metric strength class is not a claim, an
anchored candidate tonality is not a claim, and a decided boundary or a tonality label would be.**
- *Defense.* The charter's own reason for placing the cues at L1: they are *"computable from the
  notation without knowing the tonality"*, and a detector that reads a resolved tonality and then
  votes on it is circular [RULED — charter, L1]. The two-part test makes that reason mechanical; the
  naming half is S-50's.
- *Source class.* Derived (from the charter's ground).
- *Status.* Settled.
- *Premise.* Premise: computability without a decision is the right line. False-negative path: a
  cue so specific that it is a decision in disguise (a flag true only at textbook perfect authentic
  cadences would function as a cadence label). S-47's V-anchored flag and the interval sets of S-49
  keep the cues general; a later, sharper cue must pass the same test and the pack's #17(d).
- *Falsifier.* RESIDUAL — a modelling premise; the CODE half is S-50's falsifier.

**S-52. Every published item carries an establishment status: *notated* for a fact read from L0,
*computed* for a predicate over notated facts, and *provisional* for anything resting on an
UNESTABLISHED parameter (the cue window, S-48). A consumer may not put a provisional item under
load until the parameter is established.**
- *Defense.* The pack's publish-broadly rule requires establishment status on every evidence-class
  fact and forbids a consumer relying on an unestablished one [RULED — D-100 as carried; principle #19].
- *Source class.* Given (D-100, #19).
- *Status.* Settled.
- *Premise.* Premise: three statuses suffice. False-negative path: a *notated* fact from a bar with a
  defect flag (S-10) is notated and doubtful; the defect flag travels with it, which is the fourth
  status in effect.
- *Falsifier.* CODE. Observable: the status field. Decision rule: falsified if any published item lacks
  one, or if a cue computed with the stand-in window is marked other than provisional. Not falsified
  by: every item in a clean score being *notated* or *computed*.

**S-53. Nothing L1 publishes depends on anything L2 decides. Where a statement above would have
wanted L2's answer — which slice is the harmonic arrival (S-44), whether a lowest pitch is the
harmonic bass (S-44), whether a silence continues a harmony (S-31), which pass of a repeat is being
read (S-27) — the want is met by publishing the candidates and the evidence and leaving the decision
to L2. L1 is therefore computable in one forward pass over the working span, and the working span is
the only thing a caller supplies beyond L0.**
- *Defense.* The boundary contract: L1 → L2 forward only; *"L2 receives candidates and evidence, never
  decisions"* [RULED]; D-030's bounded-context rule fixes the span as the caller's [RULED]. Each cited
  statement above shows where the dependency was avoided.
- *Source class.* Given (charter and D-030), derived in the enumeration.
- *Status.* Settled.
- *Premise.* Premise: the enumeration of wants is complete. False-negative path: a want this session
  did not notice; the falsifier below would surface it.
- *Falsifier.* CODE. Observable: L1's inputs. Decision rule: falsified if L1 reads any L2 output or any
  value not in L0 plus the span. Not falsified by: a caller passing a span computed by an earlier L2
  run — that is the caller's act, not L1's input.

**S-54. Pedal marks. A release is the notated release of the event, whatever pedal mark spans it; the
pedal mark is published in the marks list (S-41) with its span, and every change point inside the
span carries a PEDAL-HELD attribute. Whether a sustained-pedal span should instead extend releases to
the pedal lift is OQ-3 (faces (a) and (c)); no staged file carries a pedal mark (declared in the brief),
and this derivation does not fill it.**
- *Defense.* Harmonic analysis reads notated durations; a pedal instruction is a performance direction
  whose sounding effect (which notes actually ring, and how loudly) is not notated [THEORY]. Extending
  releases would make every pedalled bar one slice and would delete the change points the charter
  makes exhaustive; publishing the span keeps the information for L2, which may treat a pedalled
  arpeggio as one sonority. The pack's design intent defines a pedal *point* voice-independently
  (D-207) — a different thing (a held tone in the harmony) from a pedal *mark* (a damper instruction);
  the two words are kept apart here.
- *Source class.* Derived (interim); open.
- *Status.* Open (OQ-3).
- *Premise.* Premise: the notated release is the safer default. False-negative path: a pedalled
  arpeggio whose bass leaves the sounding set at its notated release, so that the bass of later slices
  in the bar is an inner note — S-44's proxy hazard, sharpened. PEDAL-HELD on those change points lets
  L2 see it.
- *Falsifier.* RESIDUAL until ruled; thereafter CODE: releases inside a pedal span equal the notated
  releases (or the lift, if ruled so).

---

## 4. Open questions

Each names the face of the brief's §2 it belongs to and the statement that raises it. None is filled
with a plausible reading. The seven marked ★ are the ones this session would put to the user for a
ruling, with the question it would ask.

- **OQ-1 ★ (faces (c), (e); S-27, S-42, S-32).** Does the analysis work over the score in *notated*
  order or in *unfolded* (performed) order? *The question for the user:* is the working span a stretch
  of notated bars, or a stretch of the performed sequence — and is the published ground truth this
  project measures against aligned to one or the other? Until ruled, L1 works in notated order and
  publishes junction adjacencies.
- **OQ-2 (face (a); S-21).** Eligibility and sounding set of tremolo-marked notes, measured and
  unmeasured. No staged file carries a tremolo (declared in the brief). Interim: one event per
  notated note.
- **OQ-3 ★ (faces (a), (c); S-54).** Under a sustained-pedal mark, is an event's release its notated
  release or the pedal lift? No staged file carries a pedal mark (declared). *Question:* does the
  analysis read the pedalled bar as one sonority (releases extended) or as the notated succession
  (releases notated, PEDAL-HELD attribute published)?
- **OQ-4 (face (a); S-19).** Cue-sized passages in extracted parts, and editorial realisations
  written as small notes: which are eligible? The notation distinguishes them only by context.
- **OQ-5 (face (a); S-19).** *Ossia* staves and alternative passages: which alternative sounds?
- **OQ-6 (face (a); S-3).** Concert pitch is required by S-3; where a record file carries a
  transposing part without its transposition, L0 cannot supply spelled sounding pitch. Refuse, as
  S-14 does for unspelled input, or flag? Not settled here.
- **OQ-7 (face (b); S-24).** A tie across an enharmonic respelling (same sounding pitch, different
  letter, typically across a key-signature change). S-24's same-spelling test splits it into two
  events with a flag. Should the test admit enharmonic equivalence for ties only?
- **OQ-8 (face (d); S-34, S-36, S-37).** A time-signature change mid-bar; additive and irregular
  signatures beyond the bar and denominator levels; a short bar after a repeat or double bar that is
  neither clearly a tail nor a head.
- **OQ-9 (face (e); S-39).** Are a caesura, a breath mark, a section break or a *segno* boundary
  evidence? The charter names five kinds; these pass S-1 and are not in the list. Not added here
  (S-43 adds only the two signature changes, which the staged files exercise).
- **OQ-10 (face (f); S-48).** The cue window's value for this repertoire. A measurement, UNESTABLISHED.
- **OQ-11 (face (d); S-35).** Whether an *off-grid* position under a tuplet should instead receive the
  class of the nearest level, and by what rule. This session holds that rounding asserts a beat the
  notation does not write.
- **OQ-12 (face (a); S-13, S-46).** Which "voice" the leading-tone cue reads where a notated voice
  carries chords. S-46's relaxation is the interim.
- **OQ-13 ★ (face (a); S-18).** A note marked invisible but played. The C. P. E. Bach file carries
  invisible small notes, one of them also marked not played; the others are invisible and, by the
  file, sound. This derivation excludes them on visibility (the analysis reads the page). *Question:*
  does visibility or the played flag govern eligibility when they disagree?
- **OQ-14 ★ (face (e); S-41).** The positioned marks list is an output the charter does not name.
  *Question:* is a second output beside the per-change-point flags admitted, or must every mark be
  attached to a change point with a displacement?
- **OQ-15 ★ (face (e); S-43).** *Question:* are TIME-SIGNATURE-CHANGE and KEY-SIGNATURE-CHANGE
  admitted to the boundary-evidence kinds?
- **OQ-16 ★ (L0; S-8).** *Question:* are a composer's own figured-bass figures input to the analysis
  or annotation beside it? This derivation says annotation, and names the cost for continuo parts.
- **OQ-17 ★ (face (f); S-48).** *Question:* is the stand-in window (four beats; one bar) acceptable as
  a declared provisional value until the measurement of OQ-10 runs?

---

## 5. The measured-cost record

Recorded as measured, not reconstructed. Where a quantity was not measured it is said to be
unmeasured; nothing is estimated.

- **Wall-clock stamps (UTC, from `date` in the session's workspace).** Reading of the pack and the
  scores finished and writing began at **2026-09-02T06:54:54Z**. The last statement (S-54) was written
  at **2026-09-02T07:03:07Z**. The turn's start was not stamped, so **time before the first statement
  is unmeasured**; the time from the start of writing to the end of the statements is **8 min 13 s**.
  The time spent on §§4–7 after the statements is stamped at the end of §6.
- **Statements: 54** (S-1 to S-54). Time per statement over the writing interval: 8 min 13 s / 54 =
  **9.1 s per statement** (a ratio of two measured values; the writing interval includes §0 and §1,
  which were written in the same interval, so the per-statement figure is an upper bound on statement
  time only if those sections are counted as statements, which they are not — the figure is reported
  as the interval divided by the count and nothing finer was measured).
- **Share marked *open*: 9 of 54** (S-7, S-18, S-19, S-21, S-27, S-42, S-43, S-48, S-54).
- **Share the session would put to the user for a ruling: 7 of 54** — S-8 (OQ-16), S-18 (OQ-13),
  S-27 (OQ-1), S-41 (OQ-14), S-43 (OQ-15), S-48 (OQ-17), S-54 (OQ-3); the question each would ask is
  at its OQ in §4.
- **Share marked *given*: 3 of 54 purely given** (S-14, S-33, S-52), and **8 of 54 given-with-
  derivation** (S-6, S-9, S-13, S-31, S-32, S-38, S-39, S-53), 11 of 54 in all. Of the 11, **9 rest on
  the charter** and **2 rest on a ratified design-intent entry** (S-32 on D-030/D-031 with the
  charter; S-52 on D-100 and principle #19). The brief asks a session marking many statements *given*
  to say so: 11 of 54 is not many, and the derivation is not thin — the charter fixes the outputs and
  leaves their construction, which is where the 42 derived statements sit.
- **Share whose sixth field could not be written: 0 of 54.** Six carry a RESIDUAL falsifier rather
  than a CODE one (S-1, S-8, S-21, S-48, S-51, S-54); none is marked UNVERIFIABLE.
- **Share resting on a *measured* source class: 1 of 54** (S-48).
- **Pack members consulted, per statement.** `07_the_charter…`: S-1–S-3, S-5–S-6, S-8–S-9, S-12–S-16,
  S-26, S-28, S-31–S-33, S-35, S-38–S-39, S-44, S-47, S-50–S-53. `08_the_five_research_extracts`:
  S-15, S-23, S-28, S-35, S-38, S-44–S-49. `09_the_empirical_findings_ledger`: S-6 (C14), S-10 (C21,
  C22), S-44 (C32, C38), S-45 (C41). `02_the_guiding_principles…`: S-1 (#21), S-2 (#12), S-7 (#6),
  S-10 (#12, #13), S-13 (#17d), S-19, S-20 (#6), S-28, S-41 (#12), S-44 (#17d), S-48 (#17, #19), S-52
  (#19). `05_the_ratified_design_intent` (lines 1–700 only, §6): S-2 (D-100), S-20 (D-100), S-32
  (D-030, D-031), S-38 (D-034), S-49 (D-100), S-52 (D-100), S-53 (D-030), S-54 (D-207).
  `03_the_writing_standards`: the form of this file, consulted by no statement.
  **Consulted by no statement:** `00_READ_THIS_FIRST`, `01_the_phase_definitions`,
  `04_the_dispatch_protocol`, `06_the_defect_type_catalog` (read; DT-shapes were checked against, none
  cited).
- **Fetched sources consulted, per statement.** MusicXML 4.0 reference, `<grace>`: S-3, S-15, S-16.
  MusicXML 4.0 reference, `<tie>`: S-3, S-23. Temperley 2009 (JNMR), fetched from the author's site:
  S-15, S-34, S-35. Hentschel et al., *The Annotated Mozart Sonatas* (TISMIR): S-27. music21
  `Stream.chordify` documentation: **fetch failed (404), no statement rests on it.**
- **Staged scores consulted, per statement (as cases met, never as counts):** the Couperin file:
  S-3, S-4, S-11, S-16, S-17, S-23, S-36; the chorale: S-5, S-6, S-10, S-11, S-13, S-26, S-36, S-37,
  S-39, S-40, S-43; the C. P. E. Bach file: S-3, S-5, S-15, S-17, S-18, S-27, S-42; the Brandenburg
  file: S-4, S-13.

---

## 6. The independence record

### 6.1 What arrived, and how much of each was read

**Message one** carried the brief alone, pre-read whole (543 lines) before the session's first turn.
The boot inventory was declared in the session's first message; everything received was on the
expected list; no project folder was connected at any time; no folder was requested or accepted; no
directory was listed; no shell was run over project material (the shell was used only for `date` and
for writing and editing this file in the session's own workspace).

**Message two** carried the ten pack members and the four scores. **Nine of the fourteen were
pre-read into context before the turn began** (expected under §3a of the brief; recorded):

| File | How it arrived | Extent read |
|---|---|---|
| `00_READ_THIS_FIRST.md` | pre-read | whole, 58 lines |
| `01_the_phase_definitions.md` | pre-read | whole, 243 lines |
| `02_the_guiding_principles_and_the_conventions.md` | pre-read | whole, 694 lines |
| `03_the_writing_standards.md` | pre-read | whole, 190 lines |
| `04_the_dispatch_protocol.md` | read by the session | whole, 1386 lines, in two calls (1–820, 821–1386) |
| `05_the_ratified_design_intent.md` | read by the session | **lines 1–700 only**, one call; the file is 290.2 KB (the tool's figure); the rest was NOT opened — see §6.2 |
| `06_the_defect_type_catalog.md` | pre-read | whole, 34 lines |
| `07_the_charter_the_layers_and_the_decisions.md` | pre-read | whole, 396 lines |
| `08_the_five_research_extracts.md` | read by the session | whole, 1119 lines, in two calls |
| `09_the_empirical_findings_ledger.md` | pre-read | whole, 676 lines |
| `02_second_prelude.mscx` (Couperin) | pre-read | lines 1–2000 only; nothing further opened |
| `011 Jesu, nun sei gepreiset.mscx` (chorale) | pre-read | lines 1–2000 only; nothing further opened |
| `wq55n02a.mscx` (C. P. E. Bach) | read by the session | lines 130–259, 2360–2469, 3670–3849; plus element-name searches returning line numbers only (§6.3) |
| `bwv1049_03_presto.mscx` (Brandenburg) | read by the session | lines 5490–5559; plus element-name searches returning line numbers and part names only |

Reading order followed `00_READ_THIS_FIRST.md` for the members the session opened itself; the
pre-read members arrived in an order nobody chose, as the brief's §3a says to expect.

### 6.2 The stop-on-meeting record — by file and location, without paraphrase

Statements about how THIS project's analysis currently does something in §2's subject were met at the
locations below. None was paraphrased above and none entered a statement. Where a file was already in
context whole, the record is of location and extent, as the brief's amended clause directs.

- **The brief** (pre-read whole): line 19; lines 282–284; lines 459–462; lines 500–506. Seen whole.
- **`02_the_guiding_principles…`** (pre-read whole): lines 323–335 (the "founding instance" paragraph
  of the never-work-from-memory convention, which names two specification locations and states their
  content on slice identity and note collection); lines 426–428 (three named decisions, the third on a
  boundary convention); lines 528–535 (a family of open items and what they read); lines 591–600
  (candidate admission — L2's subject, recorded because it names a mechanism). Seen whole. **A note
  on S-29:** the convention at line 428 was in context before S-29 was derived. S-29's defense rests on
  the meaning of onset and release and would be written the same way had the line not been seen; a
  reader weighing S-29 should know the line was seen.
- **`04_the_dispatch_protocol`** (read by the session, in two calls): lines 1008–1013 (a named removed
  mechanism concerning a declared mode at a piece's start — L0's subject) and lines 1187–1189 (three
  named files, one a notation-bridge source file). Both were inside the second call's output
  (821–1386), which arrived whole; the file ended there, so nothing further was read.
- **`05_the_ratified_design_intent`** (read by the session): the first call returned lines 1–700 at
  once. Within them, entries stating how the analysis currently reads or slices a score, or what its
  fact layer carries: **D-023 (89–98), D-024 (101–111), D-033 (220–231), D-057 (262–270), D-207
  (589–600), D-221 (617–626), D-224 (658–669), D-229 (673–694).** Several other entries in the same
  span describe the implementation on subjects outside §2 (D-002, D-005, D-010, D-095, D-114, D-131,
  D-132, D-220, D-222, D-223) and are recorded as seen. **The session stopped reading the file at line
  700 under the stop-on-meeting clause and did not open lines 701 to the end.** The pack's own note
  says three passages were cut from `07` and five sections from `08` for this subject; nothing says
  `05` was filtered beyond the withheld family, and what remained in its first 700 lines was met.
  The design-intent entries the derivation *uses* (D-030, D-031, D-034, D-100, D-207 as a
  contrast) are within the read span; D-207 is cited only to keep "pedal point" apart from "pedal
  mark".
- **`06_the_defect_type_catalog`** (pre-read whole): line 24, DT-16, names a class of eligibility
  rules a consumer might hold. Seen whole.
- **`07_the_charter…`** (pre-read whole): line 62 and lines 71–86 concern the charter's own drafting
  history and correction; lines 208–213 of `08` restate the charter's ground for releases as this
  project's own. These are charter provenance, not implementation, and are recorded so the reader can
  judge the classification rather than take it.
- **`09_the_empirical_findings_ledger`** (pre-read whole): lines 345–351 (C14's "not admitted"
  clause naming a handling and a decision identifier — L0's subject). Seen whole.
- **`01`, `03`, `08` (beyond the above), `00`:** no statement about how this project's analysis
  currently does §2's subject was met.

**Positive statement:** apart from the locations above, no such passage was met in any pack member,
and no such passage was met in any score file.

### 6.3 The two elements not read, per staged file

Counts were obtained by a search for the element names over each file; the search returned line
numbers only, and no line inside a `<Harmony>` or `<StaffText>` element was read by the session.

| File | `<Harmony>` | `<StaffText>` | Note |
|---|---|---|---|
| Couperin, `02_second_prelude.mscx` | 48, at lines 3025–4679 | 0 | none read; the pre-read extent (1–2000) precedes the first |
| Chorale, `011 Jesu…mscx` | 0 | 2, at lines 85–90 | **both were inside the pre-read extent and were seen**; their content did not enter any statement |
| C. P. E. Bach, `wq55n02a.mscx` | 167, at lines 11859–18379 | 13, at lines 1405, 3431, 8321, 8433, 11552, 12064, 12227, 12669, 12891, 13505, 14008, 14209, 16874 | none read; every window the session opened (130–259, 2360–2469, 3670–3849) lies between them |
| Brandenburg, `bwv1049_03_presto.mscx` | 0 | 0 | — |

The counts are records of what was passed over; **no count is evidence for any statement** (the
brief's §3), and no statement above rests on how often anything occurs in the staged set.

### 6.4 Fetched sources, and the primaries not re-read

- **MusicXML 4.0 reference, `<grace>` and `<tie>` element pages (w3.org).** Fetched and read through
  the fetch tool's prompted extraction; the quotations at S-3, S-15, S-16, S-23 are as the tool
  returned them. Grade: web-fetch, prompted extraction — not page images.
- **Temperley 2009, "A Unified Probabilistic Model for Polyphonic Music Analysis", JNMR**, the PDF
  on the author's site. Fetched and read through prompted extraction; quotations at S-15, S-34, S-35
  carry the page numbers the tool returned (pp. 3, 5, 7, 8). Grade: web-fetch, prompted extraction.
  This is the primary behind the charter's metric-strength figures and is **not** one of the five
  papers whose extracts are pack members. It was fetched to check the level structure behind the
  charter's Table 1 figures before building S-34/S-35 on them; the figures returned (71.5 / 22.3 /
  2.4 by level 3 / 2 / 1) agree with the charter's corrected wording.
- **Hentschel, Neuwirth & Rohrmeier, "The Annotated Mozart Sonatas", TISMIR.** Fetched; the tool
  returned that the article defines no note-extraction or unfolding procedure and one sentence on
  unfolding labels, quoted at S-27. Grade: web-fetch, prompted extraction; a thin yield, declared.
- **music21 `Stream.chordify` documentation.** Fetch returned 404. **No statement rests on it**; the
  gap is recorded rather than filled.
- **The five primaries whose extracts are pack members** (Pardo & Birmingham 2002; Temperley & Sleator
  1999; Bigo et al. 2018; Karystinaios & Widmer 2022; Sears et al. 2018): **none was re-read.** The
  claims this derivation takes from them — the partition-point definition; the input contract of the
  preference-rule system and its circularity; the cadence feature definitions, the anchors Y and X and
  the four-beat window; the half-cadence figures; the bass-in-isolation finding — are quoted verbatim
  with page or section in the extracts, which were read at the object. A re-read would have been a
  duplication of that work, not a check of it, and the brief's §6 asks that the difference be
  recorded; it is. Every FACT taken from an extract is labelled as such at its statement.

### 6.5 Where notation was wanted and an open question was written instead

OQ-2 (tremolo), OQ-3 (pedal mark), OQ-4 (cue passages in parts), OQ-5 (ossia), OQ-7 (enharmonic tie),
OQ-8 (mid-bar signature change; irregular meters), OQ-13 (invisible-but-played — a case met in the
C. P. E. Bach file but not resolvable from the notation alone). The two gaps the brief declared
(tremolo, pedal) are OQ-2 and OQ-3.

### 6.6 What this session did not do

It opened no untrusted source, edited no specification and no code, ran no build, test or measurement
tool, created no open-items row, allocated no identifier, took no branch rule, read no commit log,
derived nothing on any subject but §2's, compared this file against nothing, and decided nothing about
the derivation method. This file is delivered into the conversation; the session writes it to no
repository path.

*Closing stamp for §5:* the end of writing is recorded in the delivery message, taken from `date` at
the moment of delivery.

---

## 7. Where the brief's decomposition seemed wrong or incomplete

The brief invites the session to say so. Five places:

1. **Face (e) is stated per change point, but marks fall where no change point is.** A bar line every
   voice ties across, a double bar mid-bar and a fermata over such a bar line have no change point to
   attach to. The decomposition does not name the case; S-41 adds an output for it and OQ-14 puts the
   addition to the user.
2. **Face (b) folds an ordering question into ties.** "What happens when a tie crosses a repeat" is
   not a tie question but the question whether the analysis reads notated or unfolded order (OQ-1),
   which also governs face (c)'s slice list and face (e)'s repeat flags. It deserves its own face.
3. **Face (f)'s three cues are under-specified without the upper voices.** The pack's own extracts
   carry the finding that a bass-only cue can have the wrong sign; S-49 publishes the interval content
   above the bass beside every cue, which the charter's cue list does not name.
4. **The L0 question "what happens when a real score does not supply it" is mostly a file-defect
   question**, and the decomposition has no face for defects. S-10, S-22, S-24 and S-25 answer it with
   a defect-flag discipline rather than repairs; that discipline is a small contract of its own.
5. **"Voice" is used in one sense by the charter and in two by the notation.** The charter gives voice
   membership; a record file gives *notated* voices, which in keyboard music are not lines. S-13 and
   S-46 carry the distinction and its proxy hazard; the decomposition would be clearer with the two
   senses named in face (a).

One place the decomposition was right and this session first doubted it: face (g)'s question "is a
metric strength class a claim?" looked rhetorical and was not — S-51's test had to be written to
answer it, and the test also settled the candidate-tonality anchor of S-47.

*End of file.*

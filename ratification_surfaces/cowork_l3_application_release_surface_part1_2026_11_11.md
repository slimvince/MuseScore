# Release surface for the L3 application dispatch — part 1 of several (2026-11-11)

## What this file is

This is the first part of the surface that puts to the user the questions that must be answered before the L3
application dispatch can be released to Claude Code. It explains five questions from scratch, weighs the alternatives,
and says for each one whether it only files documentation or also changes the algorithm as the specification defines it.

It decides nothing. The choice questions are put later, one decision per turn, in plain text. Where this part says
"[checked]", this sitting read the passage at its own file. Where it says "[relayed]", the passage is quoted from the
working list named below and was not opened by this sitting.

The later parts will carry the rest of what the working list sends to the release (named at the end of this file).

## The background, explained once

**The dispatch.** `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` is the written instruction
that Claude Code will carry out to apply the user's L3 rulings to the record. Its banner says NOT YET RELEASED, and it
stays unreleased until every question on this surface is answered.

**The reading file and its rows.** `ratification_surfaces/cowork_comparison_l3_reading.md` lists, one by one, the
statements of the old (outgoing) design documents that concern L3, the layer that publishes cadences, phrases, sections,
chord symbols, figured bass and similar readings built on L2's key-and-chord decision. Each such statement is a "row",
numbered like "Row 7.115", and a row may be split into parts marked (i), (ii), (iii). For each row, the reading file
proposed one word saying where the statement goes. When the dispatch runs, Claude Code writes beside each row a "line":
one sentence giving the word the user's rulings settled on.

**The seven words** (the reading file's §5, lines 382–396 [checked], quoted in short):

- **ADOPTED — carried**: a derived L3 statement already carries the content (named by its number, "L3-S" plus a
  number).
- **ADOPTED — proposed**: no derived statement carries it, and it is not describing the code, not another layer's,
  not history and not dropped by the worth test. It is *"a PROPOSAL to the user that the outgoing content be added to
  the derived specification"*.
- **RELOCATED**: the content belongs to another layer or area. The row names it in `FRAMEWORK.md` §5's own words, and
  the statement goes onto the transfer list at the reading file's §10.
- **QUARANTINED**: it says how the code currently works.
- **DISCARDED**: dropped under the worth test, with the finding, the date and the reason.
- **HISTORICAL**: *"it records an event, a build state, a superseded plan, or a status; not a rule."*
- **UNPLACED**: not a seventh word. It is *"the honest default"*, a row the user places.

The places a RELOCATED row can name are (the reading file's lines 398–401 [checked]): L0, the notated record; L1,
change points, candidates and notated evidence; L2, the tonal reading; the second axis, voice leading; the uncertainty
surface; and the measurement of the analysis. **None of these is a display.**

**STOP-and-report.** Where the dispatch gives Claude Code no line it can write for a row, Claude Code stops at that row
and reports it instead of guessing.

**The working list.** `ratification_surfaces/cowork_l3_application_release_points_2026_11_09.md` gathers every point
the release has to deal with and sorts each one. It found that the five questions below cannot be settled from the
record. This surface draws on its items (vii), (xiii), (xvii), (xxv) to (xxviii) and its section A4.

**What the five questions have in common.** Questions 2 to 5 only file documentation: they decide which word stands
beside some rows. Question 1 is the only one that touches the algorithm.

---

## Question 1 — The evaded cadence (Row 7.115, part (i))

**What the old text said** (reading file line 5008 [checked]): *"Evaded cadence — admitted when a dominant set up to
cadence has its expected tonic arrival replaced by a non-tonic continuation or a re-launched phrase (distinct from the
deceptive cadence, where the dominant resolves to the submediant — here the arrival itself is abandoned); carried at
lower confidence by rule."* Part (i) is the first half: the evaded cadence is admitted on that definition. Part (ii),
the lower confidence, is not part of this question.

**What has been ruled.** The cadence type record (`records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md`),
Ruling 3, item c, line 89 [checked]: *"Row 7.115 (i): the evaded cadence published as type not computable with its
reason until OQ-L3-5."* In plain words: for now, L3 does not name an evaded cadence as a cadence type. It says that the
type cannot be computed and gives the reason, until open question OQ-L3-5 is answered.

**OQ-L3-5 and its answer.** OQ-L3-5 asked which layer publishes the relation that says one stretch of music restates
an earlier one, transposed or not, and its text names the evaded cadence among the things that need that relation
(the thematic-parallelism record, `records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md`,
lines 14–18 [checked]). That record's Ruling 1 answered it: L1 publishes the restatement relation over the notes, its
similarity measure is measured, and L3 reads it (line 56 [checked]). But the same record leaves open, among the points
it carries as UNSETTLED, *"which statement carries the evaded cadence named in OQ-L3-5's text, not located by this
sitting"* (line 104 [checked]).

**So the time limit in item c has run out, but nothing has replaced it.** No later ruling places the row again. The
working list's item (vii) says a search of the dispatch for "7.115" and "evaded" met only §L.6, §L.7's part (ii) and
§L.11's note [relayed]. Until the user rules, the row is STOP-and-report.

**The currently decided method**: the evaded cadence is published as *type not computable*, with its reason. The
derived statement L3-S17 says a type that needs *"the evaded cadence's expectation"* is one that none of the features
holds, and that the reason stays named (reading file lines 5018–5020 [checked]). That method was ruled with an end
point, OQ-L3-5, and that end point has now been reached. What is to replace it has not been decided.

**The alternatives:**

- **A. The evaded cadence stays "type not computable" for good.** The row gets a HISTORICAL line that quotes item c
  without its *"until OQ-L3-5"*. The old "admitted" rule is then recorded as superseded.
  - **What it changes:** documentation, and also the algorithm in one respect: a method ruled as temporary becomes the
    standing method, with no end point. It adds no new method.
  - **Towards the ultimate objective (how well the analysis infers):** it fixes, for now, that L3 does not name an evaded
    cadence, even though L1 will now publish the restatement relation that OQ-L3-5 said the evaded cadence needs. It
    can be reopened later, but nothing in the record would then point at it as open.
  - **Towards the principles:** HISTORICAL would declare the old rule superseded while the later record says outright
    that the evaded cadence's carrier is not settled. The working list reads that as a claim wider than the record
    supports.
  - **What it gives Claude Code:** a line for the row, so one STOP-and-report goes away.
- **B. The carrier is settled first.** The row stays UNPLACED, gets no line, and is listed in Claude Code's report
  among the points left open. Which L3 statement carries the evaded cadence, now that L1 publishes the restatement
  relation, goes onto a later surface as an algorithm question of its own.
  - **What it changes:** nothing now, in the documentation or the algorithm. An algorithm question stays open, and it
    is named.
  - **Towards the ultimate objective:** it leaves the way open for L3 to name evaded cadences once it can read the
    relation, so a cadence type the analysis might be able to infer is not shut out by default.
  - **Towards the principles:** it matches the route ruling, as relayed in entry 291 §3 (rows no ruling reaches stay
    proposals), and it claims nothing the record does not say.
  - **What it gives Claude Code:** the dispatch needs to say "no line; list in the report" for this row instead of
    STOP-and-report. That is a documentation edit to the dispatch.

**The writing side's reading:** B is closer to both the objective and the principles. A is simpler for the release.
Nothing in the record forces either one.

---

## Question 2 — Roman numerals against the governing key: what is left of Row 3.5, part (iii)

**What the old text said** (reading file lines 1814–1821 [checked]): a key area closes only where the next region's key
differs and clears a confidence test. A region that differs without clearing the test *"keeps its own key reading … while
being grouped into the enclosing area, so the annotation emitter writes Roman numerals against the key that actually
governs the passage rather than against a momentary wobble."* Part (iii) is that last claim: *"the annotation emitter
writes Roman numerals against the key that governs the passage."* The reading file proposed it UNPLACED.

**What has been ruled, as the working list's item (xiii) reports it [relayed]:**

- the grouping into an enclosing area, which the old text's suppression of the wobble rested on, was decided against
  (key-areas Ruling 2);
- the step-one remainder record states the method as *"each span's governing key is its own tonality in L2's reading
  and a Roman numeral is L2's degree against it"*;
- the pivot-label record calls what remains of part (iii) *"consistent with L2's publication, a display matter"*;
- the matching L2 row, Row 22.92 (iii), was ruled RELOCATED to L3 by the L2 chord-as-degree record's Ruling 2, which
  left to L3 *"whether L3 offers a view relative to an enclosing key area"*.

**The currently decided method**, unchanged by any answer here: each span's governing key is its own tonality in L2's
reading, and a Roman numeral is L2's degree against it.

**The alternatives** (each only files documentation; none changes the algorithm):

- **A. RELOCATED to L2, naming L2's statement L2-S27.** As the working list quotes it from the L2 reading file, L2-S27
  says *"L2 decides the chord as degree, quality, figure and applied target, read against the span's tonality"*
  [relayed].
  - **For it:** this fits the content as it now stands, since the numeral is L2's degree.
  - **Against it:** it sends back to L2 a row the L2 ruling sent to L3, without giving the answer that ruling left to
    L3. The record also calls it a display matter, which is not part of L2's charter.
- **B. RELOCATED to a display destination.**
  - **For it:** this is the record's own word, "a display matter".
  - **Against it:** a display is not among the places §5 lets RELOCATED name, and the working list reports that §10 has no display heading [relayed]. Whether
    RELOCATED may name such a place is the working list's question A6, which goes on a later part. So B cannot be
    completed until A6 is answered.
- **C. HISTORICAL.**
  - **For it:** the wobble suppression it served was decided against.
  - **Against it:** the record does not call the remainder superseded, and the L2 ruling declined HISTORICAL for the
    matching L2 row because *"it would drop a ratified display idea L3 may still want"* [relayed]. Whether that idea
    survives key-areas Ruling 2 is the user's to judge.

**Towards the ultimate objective:** none of the three affects what the analysis infers. **Towards the principles:** A
gives the content one home where its method already lives. B keeps the record's own reading. C is defensible only if
the display idea is judged gone.

Until the user rules, this part gets no line and is listed in the report. The dispatch already provides for that.

---

## Question 3 — Three chord-name notations in Row 4.17

**What the old text said** (reading file line 2321 [checked], and as the working list's item (xvii) quotes it): a
planned "Notation convention:" list, *"lead sheet ("Cmaj7"), Nashville ("1maj7"), Roman numeral ("IM7"), figured bass
(for baroque contexts …)"*.

**What has been ruled, as item (xvii) reports it [relayed]:** the figured-bass item is settled. It is HISTORICAL where
it treats the figured bass as a formatting choice, and ADOPTED — carried by L3-S27 for the rest (*"a display may still
render it (L3-S27's views)"*). No record read for this site places the other three items: lead sheet, Nashville and
Roman numeral. The nearest pattern is Rows 4.6, 4.18 and 4.19, other display conventions from the same old list. The
display-family ruling placed those *"Outside every charter, carried for a display's own specification"*, with no
disposition word.

**The currently decided method**, unchanged by any answer here: L1 publishes, at every slice, the spelled intervals
above its lowest sounding pitch. L3 publishes a second figured bass at the continuo grain, read off that publication
and named separately from the span figure. L3-S25's span figure is unchanged. The full figure is the published fact,
and short forms are views under a named convention (L3-S27).

**The alternatives** (each only files documentation; none changes the algorithm):

- **A. Treat the three as Rows 4.6, 4.18 and 4.19 were treated.** They are outside every charter and carried for a
  display's own specification. How such items are then written in the reading file (no line, or a line of some other
  form) is the working list's question A5, on a later part.
  - **For it:** it follows a pattern already ruled for the same old list.
  - **Against it:** the display-family ruling does not name these three, and whether it reaches items it does not name
    is the user's to say.
- **B. Give them a ruling of their own on a later surface.**
  - **For it:** nothing is read into a ruling that does not name them.
  - **Against it:** one more question to put. The working list proposes no candidate word, and this sitting did not
    weigh one.

**Towards the ultimate objective:** neither affects what the analysis infers. **Towards the principles:** A reuses one
ruled treatment for like items. B avoids stretching a ruling past its words.

Until the user rules, the three items get no line and are listed in the report.

---

## Question 4 — "Not to be settled by drift": the rest of Row 24.6

**What the old text said** (reading file line 33308 [checked]): *"The choice between one store and two by declared
design is not to be settled by drift: it is made, explicitly, when the component that queries this catalog is built."*
"The catalog" is the reference collection of named progressions and idioms that L3 reads and matches against. The
choice is whether that catalog and L2's table of chord-to-chord pairs are one store or two.

**What has been ruled, as the working list's item (xxvii) reports it [relayed]:** the timing half (*"made … when the
component … is built"*) is HISTORICAL. The rulings made the choice explicitly: two stores, with the pair table L2's and
the catalog the reference L3 reads. What is left is the words *"is not to be settled by drift"*, which the surface
calls met by the rulings. The record names no word for that rest.

**The currently decided method**, unchanged by any answer here: L2 decides key and chord together, and its
progression term is a table of chord-to-chord pairs. L3 reads the catalog and does not own it. Whether DP-O (the
still-open design point on L2's progression term) also draws on the catalog stays open.

**The alternatives** (each only files documentation; none changes the algorithm):

- **A. ADOPTED — proposed.** This proposes adding to the derived specification a rule on how a choice is to be made,
  when the rulings have already made that choice.
- **B. HISTORICAL.** This reads the requirement, now met, as a status. But §5 gives HISTORICAL to what is *"not a
  rule"*, and the sentence is worded as a rule.

The other words do not fit: no derived statement carries it, it concerns the catalog L3 reads, it does not describe
the code, and the worth test has given no finding.

**Towards the ultimate objective:** neither affects what the analysis infers. **Towards the principles:** A keeps a
rule that has nothing left to govern. B records accurately that the requirement has been met, at the cost of stretching
HISTORICAL's definition.

Until the user rules, the row is STOP-and-report. Question 5's Row 24.4 has a part of the same kind, so the answer here
bears on it.

---

## Question 5 — Rows that follow in part now and wait for the rest: a line now, or none yet? (the working list's A4)

**The situation.** Some rows have a part the rulings say follows now, and another part that waits for something not yet
settled, mostly the catalog's final content or DP-O's catalog term. The question is whether Claude Code writes a line
now for the part that follows, or writes nothing until the rest is settled. The working list cites its items (xx) to
(xxiv) as settled by a sentence in their surfaces saying each row's disposition is written when what it waits for is
settled. This sitting did not read those items. The rows below have no such sentence.

**The rows** [relayed from the working list's items (xxv) to (xxviii)]:

- **Nine idiom-tag rows** (44.11, 57.535 (ii), 57.518, 57.533, 57.519 to 57.523). The catalog entry carries an idiom
  tag and two cross-attributes, and the values wait for the catalog's final content. You ratified that surface's
  proposals, among them a note saying it follows the substitution form (*"the user may prefer the lead-rows form; the
  placement would not change, only the table"*).
- **21 idiom-tag rows of part 2** (53.1 to 53.21, in the parts the surface lists). Their record places them by the
  nine rows' placement in terms, so they take whatever the nine take.
- **Rows 24.4 and 38.79 (ii).** Each has a part that follows, a part that waits for DP-O's catalog term, and a
  HISTORICAL part. The record names no word for the part that follows.
- **Row 46.14, its catalog-entries part** (*"Entries like any other; whether the final catalog holds them waits on the
  catalog's final content"*).

**The alternatives** (each only files documentation; none changes the algorithm):

- **A. No line now.** Each row keeps its proposed UNPLACED until what it waits for is settled, as the rows of items
  (xx) to (xxiv) are reported to.
  - **For it:** this is the substitution form you ratified for the nine rows. No line has to be revisited later.
- **B. A line now, ADOPTED — proposed, for the part that follows.** The waiting values are left to be settled later.
  This is how the lead-rows form already treats its catalog-entry rows: the dispatch's §L.30 gives them an ADOPTED —
  proposed line now [relayed].
  - **For it:** the record shows now what has been ruled to follow.
  - **Against it, for two rows:** for Rows 24.4 and 38.79 (ii), the part that follows has no word named, so B needs one
    chosen for it. For Row 24.4 that part is of the same kind as Row 24.6's rest, so Question 4's answer is the natural
    candidate (this sitting's reading). For Row 38.79 (ii) that part states L2's method, and the record proposes no word.

**What the record leaves unclear:** the surface you ratified for the nine rows told you that the two forms give the same
placement. Whether choosing the substitution form also chose "no line now" is not said.

**The currently decided method**, unchanged by any answer here: L2 decides key and chord together, and its progression
term is a table of chord-to-chord pairs. DP-O stays open, with the catalog term among its unmeasured candidates. L3
publishes the catalog matches once the application act amends `FRAMEWORK.md`. *"The matcher is the same for every idiom;
no preset chooses the catalog; L3's own method uses no tag."* [relayed from items (xxv) and (xxvii)]

**Towards the ultimate objective:** neither affects what the analysis infers. **Towards the principles:** A writes
nothing that is not yet complete. B records partial placements now and needs two words chosen.

Until the user rules, all these rows are STOP-and-report.

---

## What this part does not cover (for later parts)

These come from the working list (entry 727 §3 step 5 names them):

- Part B's wordings: (xxxii)'s line form, (xlix)'s form (b) wording, (liv)'s line wording, (lxxvii)'s §10 line wording
  and (lxxxi)'s line wording.
- The audit-list point of (xliii), (xlv) and (xlvi).
- (lxxv)'s Task 0 fact, with Part C.
- A1 and A2's rules, with (lxxx)'s fact on Row 40.61.
- The weak points of (l), (li), (lii), (liv), (lvi), (lvii), (lviii) and (lix) to (lxxxiii), each to be ratified with
  its item.

Questions A5 and A6, which Questions 2 and 3 depend on, also belong there. Part B's authored settlements are listed at
the working list's lines 4107–4128. The facts taken at release (Part C) are not put to the user.

*Provenance: Cowork, 2026-11-11 (Stockholm), the sitting booted on handoff entry 727. Read at the objects: the working
list at lines 1–130, 250–264, 344–369, 438–465, 658–826 and 4100–4139; the reading file's §5 (lines 379–401) and Rows
3.5, 4.17, 7.115 and 24.6 at their headings; the cadence type record at its Ruling 3; the thematic-parallelism record at
lines 12–19 and 98–111; the dispatch by a search for "type not computable" and its §L headings. The user's words: the
opening instruction; "shortened".*

# Release surface for the L3 application dispatch — part 2b (2026-11-11)

## What this file is

This is the second file of part 2 of the surface that puts to the user the questions that must be answered before the L3
application dispatch (`records/cc/instructions/cc_instruction_l3_application_2026_11_08.md`, the dispatch) can be
released to Claude Code. Part 1 (`ratification_surfaces/cowork_l3_application_release_surface_part1_2026_11_11.md`) and
part 2a (`ratification_surfaces/cowork_l3_application_release_surface_part2a_2026_11_11.md`) were ruled: Rulings 1 to 5
of `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part1_sitting.md` and Rulings 1 and 2 of
`records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md` (the part 2 ruling record).
This file is written site by site; each site is added only after the one before it has landed and been proved.

It decides nothing. The choice questions are put later, one decision per turn, in plain text. **[checked]** means this
sitting read the passage at its own file; **[relayed]** means it is quoted from the working list
(`ratification_surfaces/cowork_l3_application_release_points_2026_11_09.md`) and was not opened by this sitting.

The background (the dispatch, the reading file and its rows, the disposition words, STOP-and-report) is explained in part
1's section "The background, explained once" and is not repeated here, except where a question needs it.

---

## Site 1 — Question B-xlix: when two records each give lines to the same row, does the dispatch's rule work row by row or part by part?

**Documentation only. It does not change the algorithm as the specification defines it.** It decides how Claude Code
writes lines into the reading file, nothing about what the analysis does.

### What the question is, from scratch

The reading file lists every statement of the old design as a numbered row (for example Row 38.79). Some rows hold
several claims, written as parts (i), (ii) and so on, and a ruling can place one part of a row and leave the rest. When
the dispatch is run, Claude Code writes, beneath each row a ruling places, a line saying which disposition word the
ruling gave (for example **HISTORICAL**, "decided against"; **RELOCATED**, "belongs to another layer"; **ADOPTED —
proposed**, "to be added to L3") and which ruling gave it. The dispatch's "form (b)" is the instruction for those lines.

Form (b) has a rule for a row that two different ruling records both give lines to. As it now reads [checked: dispatch
lines 157–159]:

> A row named by two records gets both records' lines, in ledger order, and is listed in the report under *rows named by
> more than one record*; where the two lines' dispositions differ, that row is a STOP-and-report and gets neither.

("STOP-and-report" means Claude Code writes nothing at that row and lists it for the user instead.)

The question is whether "differ" is judged over the whole row or part by part. Three rows turn on it: Rows 38.79 (i),
24.2 and 57.454. Each gets lines from two records, on different parts, with different words. Read row by row, each would
be a STOP-and-report and get no line at all. The dispatch's own ledger entry for that ruling (§L.36, *Open* point (4))
leaves the choice to the releasing sitting [checked: dispatch lines 3125–3128].

### What the record already says

The working list sorted this as a derivation, not a question (its item (xlix)) [relayed: working list lines 1839–1897,
read by this sitting]. Its grounds, each checked here where marked:

1. **The dispatch already treats the part as the unit.** Form (b) gives a split row a line naming one claim (*"the line
   names that claim"*), and form (b-H) gives a decided-against part its own HISTORICAL line while *"the rest of the row
   keeps what the record says of it"* [checked: dispatch lines 159–164]. One record already gives one row lines with
   different words: Row 38.22 (ii) gets an ADOPTED — proposed line, a HISTORICAL line and a RELOCATED line, all from the
   idiom-tags record [checked: dispatch line 3073]. Read by row, the rule would stop a row when two records split it,
   but let it through when one record splits it the same way. Nothing in form (b) gives a reason for that difference.
2. **The two records divide these rows between them in terms.** The earlier record hands a part over and gives it no
   line, and the later record places exactly that part:
   - Row 38.79 (i): the lead-rows record decides against the row *"in so far as a preset selects the catalog L3 reads"*,
     *"the remainder ("idiom-specific") going with the idiom-tag rows"*, and *"The remainder gets no line from this
     record"* [checked: dispatch line 2563].
   - Rows 24.2 and 57.454: the recognition part 2 record says *"the idiom weighting moved to the idiom-tag surface"* and
     *"the idiom filter and weight vector moved to the idiom-tag surface"* [checked: dispatch line 2737].
   - The idiom-tags part 1 record ratifies *"the 8 pieces moved to this surface by the lead-rows, recognition part 1 and
     2, further-rows and substitution part 2 rulings"* [checked: dispatch line 3052].

   A row-by-row reading would leave unwritten what the user ratified in both records.
3. **The three rows, part by part** [relayed: working list (xlix)]. No part of any of the three gets two lines with
   different words:
   - Row 38.79 (i): HISTORICAL from the lead-rows record for the preset-selects-catalog part; from the idiom-tags record,
     HISTORICAL for *"a catalog per idiom decided against"* and ADOPTED — proposed for *"entries specific to idioms"* as
     their tags. The ADOPTED line falls on the remainder the lead-rows record handed over.
   - Row 24.2: from recognition part 2, RELOCATED for *"the prior"* and ADOPTED — proposed for *"the annotation"*; from
     the idiom-tags record, RELOCATED for *"the weighting as evidence"* and HISTORICAL for *"a weight deciding which
     matches L3 publishes"*, which falls on the idiom weighting part 2 moved.
   - Row 57.454: from recognition part 2, ADOPTED — proposed for *"the decided chords and the catalog as inputs"*; from
     the idiom-tags record, HISTORICAL for the filter *"in so far as it selects the catalog L3 reads"* and RELOCATED for
     *"the weight vector"*, both on what part 2 moved.
4. **Other rows that waited on this point do not change.** Rows 57.107 (ii), 38.26 and 40.40 got the same word on both
   parts, so they stand either way; Row 57.118's two RELOCATED lines from two records on different parts are both
   written, each to its own destination [relayed: working list (xlix)].

Applying D-599 (the standing principles first; only what they leave is the user's choice): the substance follows from
the dispatch's own forms and the two ratified records. **What is the user's is the wording**, which is the writing
side's, as all of the dispatch's line forms are, and which the user may overrule before Task 0.

### The wording the writing side proposes (the working list's item (xlix))

In place of the sentence quoted above, form (b) would read:

> A row named by two records gets each record's lines, in ledger order, and is listed in the report under *rows named by
> more than one record*. The rule is applied by part, a part being what a record's line names: where two records' lines
> fall on the same part with differing dispositions, that part is a STOP-and-report and gets neither of those lines;
> lines on different parts are each written. A part a record says it moves to another record gets no line from the
> record that moves it.

Form (d)'s sentence *"A row one record names by a ruled line and another by a recorded line follows form (b)'s two-record
rule"* [checked: dispatch line 177] then reads part by part too, with no change of its words.

### The currently decided method

Unchanged. As the idiom-tags part 1 record states it [relayed: working list (xxv), quoting that record's lines 54–59]:
L2 decides key and chord together; the open decision point DP-O stays open, with the catalog among its unmeasured
candidates; L3 publishes the catalog matches once the application act amends `FRAMEWORK.md`; *"The matcher is the same
for every idiom; no preset chooses the catalog; L3's method uses no tag."*

### The alternatives, weighed towards the ultimate objective and the principles

- **A — Ratify the derivation and the wording as proposed.** *Towards the objective:* neutral; the analysis is
  untouched. *Towards the principles:* every part the user placed gets its line in the ruling's own words; a real clash
  (two words on the same part) still stops; the rule matches what forms (b) and (b-H) already do for a single record.
- **B — Ratify the derivation, with other wording.** Only needed if something in the wording above reads wrongly.
- **C — Keep the rule row by row.** Rows 38.79 (i), 24.2 and 57.454 become STOP-and-reports and get no line.
  *Towards the principles:* it leaves unwritten what the user ratified in two records, and treats two records splitting a
  row differently from one record splitting it, with no ground in the dispatch for that difference.

**The record settles the substance (A or B); C goes against two ratified records.** What is the user's is whether the
wording stands.

**To do at release** [relayed: working list (xlix)]: replace form (b)'s sentence (dispatch lines 157–159) with the
wording; change §L.36's *Open* point (4) (dispatch lines 3125–3128) to point to the ruling; former wordings kept.

---

## Site 2 — Question B-liv: what line, if any, do Rows 8.23, 8.35 (i) and 8.113 (ii) get, now that a ruling holds them?

*Added by the sitting booted on entry 732.*

**Documentation only. It does not change the algorithm as the specification defines it.** It decides what Claude Code
writes beneath three rows of the reading file, nothing about what the analysis does.

### What the question is, from scratch

The three rows, as the working list describes them [relayed: working list (liv), lines 2140–2143]: Row 8.23 is a
glossary entry, *"Caplinian formal functions [MT — out of L6's scope]"*, with the sentence and the period; Row 8.35's
claim (i) says the layer does not do Caplin's formal functions; Row 8.113's claim (ii) says periods and sentences are
out of the grouping's core. ("Sentence" and "period" are Caplin's names for two kinds of theme.) The reading file
proposes each as **ADOPTED — carried (L3-S24)**: already carried by the L3 derivation, at its statement L3-S24, *"L3
publishes the grouping (boundaries, nesting and rivals) and not form-function names"* [relayed: the same lines].

The sections ruling of 2026-11-03 (`records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md`, Ruling 3)
then decided that L3 does work out form-function names, and said of these three rows [checked: that record, lines
155–158]:

> **Rows 8.23, 8.35(i) and 8.113(ii)** concern Caplin's theme types (sentence, period), not the sonata labels […];
> their proposed disposition, *"ADOPTED — carried (L3-S24)"*, no longer stands as proposed, and they are **held,
> travelling with the naming-scheme question**.

Its *"Not decided by this ruling"* begins *"which naming scheme (sonata-form labels, Caplin's theme types, or both)"*
(line 161); its check correction (1) says the three rows' *"placement travels with the naming-scheme question rather than
being decided against"* (lines 167–168); its §4 carries them forward with that question (lines 186–187) [checked].

The dispatch's ledger entry for that record (§L.12) gives the three rows no disposition word (table line 949) and leaves
the line to the releasing sitting [checked: dispatch lines 970–972]:

> (3) Rows 8.23, 8.35 (i), 8.113 (ii): *"held"* is not a word of the reading file's §5, and the record says their
> proposal no longer stands; what line, if any, they get is to be settled before release.

Until it is settled, those rows are STOP-and-report (lines 973–974) [checked].

### What the record already says

The working list sorted this as a derivation, not a question (its item (liv)) [relayed: working list lines 2137–2181,
read by this sitting]. Its steps:

1. **No disposition word fits.** Not HISTORICAL ("decided against"): the record's correction (1) declines that in terms,
   and whether Caplin's theme types are named at all is open. Not ADOPTED — carried: the record says that proposal no
   longer stands, and the L3-S24 text it rests on is to be rewritten. Not ADOPTED — proposed ("to be added to L3"):
   that would decide the open naming scheme. Neither the reading file nor the record proposes RELOCATED, QUARANTINED or
   DISCARDED for them. And UNPLACED is, by the reading file's §5, not a disposition but a row the user places. So form
   (b), the line with a disposition word, cannot be used.
2. **Writing no line does not fit either.** At the working list's item (li), held rows got no line, because their
   proposal (UNPLACED) stayed true. Here each proposal is an ADOPTED word that the record says no longer stands; with no
   line, the reading file would go on showing it standing, against the record's words, and would not say where the rows
   went.
3. **So the line takes the kind ruled for item (xxxii)** (Ruling 1 of the part 2 ruling record: a ruled line with no
   disposition word, giving the record's placement in its words; form (c) at dispatch lines 169–171 is the dispatch's
   own model of a ruled line with no word [checked]). Item (xxxii)'s opening words *"Outside every charter"* are not
   used, because this ruling does not say them.
4. **No second record.** A search of the dispatch for the three row numbers meets them only in §L.12 (lines 945, 949,
   970 and 998) [checked]; line 945 is the other claims of Rows 8.35 and 8.113, (ii) and (i), placed by Ruling 1 of the
   same record. So form (b)'s two-record rule (Ruling 3 of the part 2 ruling record) is not met.

Applying D-599 (the standing principles first; only what they leave is the user's choice): the record and the dispatch's
own forms leave no disposition word. **What is the user's:** the line's wording, which is the writing side's, as all of
the dispatch's line forms are; and the weak point below.

### The wording the writing side proposes (the working list's item (liv))

ONE line added beneath each row's `*PROPOSED DISPOSITION.*` paragraph, naming claim (i) for Row 8.35 and claim (ii) for
Row 8.113 (form (b)'s split-row rule):

> `*RULED PLACEMENT (cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3).* Held, travelling with the
> naming-scheme question — "their proposed disposition, "ADOPTED — carried (L3-S24)", no longer stands as proposed".`

No disposition word is written; the row is not counted in the ruled distribution and is listed in Claude Code's report
as held by ruling. The proposed paragraph is kept as it stands.

### The weak point, stated by the working list

That a held row whose proposal the record withdraws gets a line with no word, and not no line as at (li), is the
writing side's reading. If the user prefers no line, each row keeps its proposed ADOPTED — carried (L3-S24) with
nothing at the row saying it no longer stands, and the report lists the three [relayed: working list lines 2170–2173].

### The currently decided method

Unchanged by this question. As Ruling 3 of the sections record states it [checked: lines 135–138]: *"L3 works out, for
each section at every level of the nesting, a form-function name where the chosen naming scheme has one (e.g.
exposition, second theme, development, recapitulation), "no name" being a possible reading; each name is published with
its rival names and their mass, carrying its establishment status — UNESTABLISHED until measured against a ground
truth."* Which naming scheme (sonata-form labels, Caplin's theme types, or both) stays open.

### The alternatives, weighed towards the ultimate objective and the principles

- **A — Ratify the derivation and the wording as proposed.** *Towards the objective:* neutral; the analysis is
  untouched. *Towards the principles:* the reading file says at each row, in the ruling's own words, that the proposal
  no longer stands and where the row went; no word is written that the ruling did not give.
- **B — Ratify the derivation, with other wording.** One thing in the wording may read badly: the record's phrase is
  put in double quotation marks and itself contains double quotation marks around *ADOPTED — carried (L3-S24)*, so the
  marks nest. B would keep the content and change only how the quotation is marked.
- **C — No line.** *Towards the principles:* each row would go on showing ADOPTED — carried (L3-S24), which the ruling
  says no longer stands, with nothing at the row to say so; only the report would list them.

**The record settles that no disposition word is written.** What is the user's is the line, A or B, against no line, C.

**To do at release** [relayed: working list (liv)]: change §L.12's *Open* point (3) (dispatch lines 970–972) to point to
the ruling, and write the line into the §L.12 table's line for the three (dispatch line 949); former wordings kept.

---

## Site 3 — Question B-lxxvii: Row 7.67, re-marked as carried by L3, and the line added beneath its transfer-list entry

*Added by the sitting booted on entry 733.*

**Documentation only. It does not change the algorithm as the specification defines it.** It decides what Claude Code
writes beneath one row of the reading file and beneath one entry of the reading file's transfer list, nothing about what
the analysis does. The algorithm change behind it (L3 may ask for more music at the edge of the selection) was ruled on
2026-11-03 and is not decided here.

### What the question is, from scratch

Row 7.67 of the reading file is one claim of the old design: *"A decision whose span is cut by the **selection edge**
before any of (i)–(iii) holds fires this layer's **extension request** per the one cross-layer extension spec"*
[relayed: working list (lxxvii), lines 3651–3653]. In plain words: when the edge of the selected music cuts a decision
short, the layer asks for more music. The reading file proposes it **RELOCATED** to L2 ("belongs to another layer"),
because whether L3 may itself ask was then an open question (OQ-L3-10) [relayed: the same lines].

The edge-of-span ruling of 2026-11-03 (`records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md`,
Ruling 1) answered that question: *"L3 may ask the caller for more music where its in-selection phrase or section reading
depends on music beyond the edge"* (record line 50), and its documentation paragraph says *"OQ-L3-10 closed"* (line 76)
and [checked: record lines 78–80]:

> Row 7.67 (proposed RELOCATED to L2 only because L3's right to ask was open) may be re-marked ADOPTED — carried
> (L3-S40). The re-marking is the application dispatch's act.

("ADOPTED — carried (L3-S40)" means the L3 derivation already carries this content, at its statement L3-S40.)

The dispatch's ledger entry for that record (§L.15) quotes the sentence at the row (table line 1197) and leaves two
things to the releasing sitting [checked: dispatch lines 1209–1213]: whether *"may be"* orders the line or only allows
it, and, if the line is written, that *"the row comes off the transfer list at §10 if it is there"*. Its check note
says *"Points (1) and (2) stand."* (lines 1225–1226) [checked].

The transfer list (the reading file's §10) is where every RELOCATED row is listed for the layer it goes to [checked: the
reading file's §5, lines 387–388]. It carries Row 7.67 in one entry with seven other rows, under the L2 heading
[checked: the reading file, lines 79125 and 79178–79179]:

> - Rows 7.60, 7.61, 7.64, 7.65, 7.66, 7.67, 7.277 and 7.278 — the slice, the key-span and the decision-context span,
>   with its extent and its extension request. *(L3-S40 AGREES at Row 7.67, citing L2-S22.)*

As the dispatch stands, nothing reaches that entry: Task 3 (c) item 5 appends RELOCATED rows only, and item 6 adds its
*LEAVES L3* line only beneath entries whose rows are placed by four other records [checked: dispatch lines 5204–5216].

### What the record already says

The working list sorted this as a derivation, not a question (its item (lxxvii)) [relayed: working list lines
3641–3714, read by this sitting]. Its steps:

1. **The record orders the line.** (a) Its next sentence gives the re-marking to this act in terms: *"The re-marking is
   the application dispatch's act."* (b) The sentence stands in the same *Documentation* paragraph as the rows *"Recorded
   as decided against"* (record lines 76–78), which the dispatch writes as lines (dispatch lines 1195–1196), and A was
   put *"stating that it changes the algorithm and also files documentation"* (record lines 22–23) [checked]. (c) The
   parenthesis gives the RELOCATED proposal's only ground, that L3's right to ask was open, and Ruling 1 closed it. So
   *"may"* says the bar has gone, not that the act chooses; the act takes no ruling and weighs no position, so a mere
   permission would leave it nothing it could write.
2. **The word is ADOPTED — carried (L3-S40).** The reading file's §5 defines it as content *"a derived statement already
   carries … in substance (named by its L3-S-number)"* [checked: line 382]; the row AGREES with L3-S40, and the ruling
   confirms L3-S40 as written (A was put as *"L3-S40 as written"*, record lines 19–20 [checked]). RELOCATED no longer
   fits, because Ruling 1 gives L3 the asking, so the content no longer belongs to another layer. The other words each
   fail at their own definitions [relayed: working list (lxxvii)].
3. **The row's line** is form (b)'s, quoting the record:
   `*RULED DISPOSITION (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1).* **ADOPTED — carried (L3-S40)** — "Row 7.67 (proposed RELOCATED to L2 only because L3's right to ask was open) may be re-marked ADOPTED — carried (L3-S40). The re-marking is the application dispatch's act."`
   It does not say *as proposed* (the row was proposed RELOCATED), and names no part (the row is one claim).
4. **One record only.** A search of the dispatch for *"7.67"* meets it at §L.15 (lines 1190, 1197, 1199, 1209, 1221) and
   in the check row (line 20) [checked]. So form (b)'s two-record rule (Ruling 3 of the part 2 ruling record) is not met.
5. **The transfer-list entry gets one added line.** Left as it is, the entry would go on listing for L2 a row whose own
   line says L3 carries it. No §10 entry is deleted or edited (Task 3 (c) item 6's own manner, every text kept). Item
   6's *LEAVES L3* form does not fit, for it would say the row leaves L3, and the ruling keeps it there. So the line takes
   a form of its own, beneath that entry, naming Row 7.67 only, the other seven rows untouched.

Applying D-599 (the standing principles first; only what they leave is the user's choice): the row's word and line follow
from the record and the reading file's own definitions. **What is the user's:** the wording of the new transfer-list
line, which is the writing side's, as item 6's own form is, and which the working list sends to this surface with Part B
(item B7, Task 3's items); and the weak point below.

### The wording the writing side proposes for the transfer-list line (the working list's item (lxxvii))

ONE line added beneath the entry at reading-file line 79178, at the entry's indentation:

> `*STAYS AT L3 (cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1).* — Row 7.67, re-marked ADOPTED —
> carried (L3-S40): "proposed RELOCATED to L2 only because L3's right to ask was open".`

### The weak point, stated by the working list

That *"may be re-marked"*, read with *"The re-marking is the application dispatch's act"*, orders the line is the
writing side's reading, as it was the dispatch writer's. If the user reads *"may"* as a permission only, the row keeps
its proposed RELOCATED as a proposal, gets no line, and stays on the transfer list as it is, its proposal resting on a
question Ruling 1 has answered; it is then listed among *the points that are not this batch's* [relayed: working list
lines 3700–3704].

### The currently decided method

Ruling 1 of the edge-of-span record, already ruled [checked: record lines 50–53]: L3 may ask the caller for more music
where its in-selection phrase or section reading depends on music beyond the edge; it stops when its own in-selection
phrases and sections stop changing between successive enlargements, under the same safety cap (D-624), and marks its
publication truncated if the cap ends the loop (D-263); units cut by the edge carry their mark. Not changed by this
question.

### The alternatives, weighed towards the ultimate objective and the principles

- **A — Ratify the derivation, the row's line, and the transfer-list line as proposed.** *Towards the objective:*
  neutral; the analysis is untouched. *Towards the principles:* the row says what the user ruled, in the record's own
  words; the transfer list stops offering L2 a row L3 keeps, with every text kept.
- **B — Ratify the derivation and the row's line, with other wording for the transfer-list line.** Only needed if the
  label *STAYS AT L3* or the quoted words read wrongly.
- **C — Read *"may"* as a permission only: no line at the row, nothing added to the transfer list.** *Towards the
  principles:* the row would go on showing a RELOCATED proposal whose only ground the ruling has removed, and the
  transfer list would go on listing it for L2.

**The record settles that the row is re-marked ADOPTED — carried (L3-S40), on the writing side's reading of "may".** What
is the user's is that reading (A or B against C) and the transfer-list line's wording (A against B).

**To do at release** [relayed: working list (lxxvii)]: change §L.15's *Open* point (1) (dispatch lines 1209–1213), the
check note's *"Points (1) and (2) stand."* (lines 1225–1226) for point (1), and the check row's *"§L.15 points (1) and
(2)"* (line 20) for point (1), to point to the ruling; write the word into the §L.15 table's line for Row 7.67 (dispatch
line 1197); add to Task 3 (c) item 6 the transfer-list line for Row 7.67, pointing to the ruling; former wordings kept.

---

## Site 4 — Question B-lxxxi: the line for Row 32.1, the product's core scope, placed clause by clause

*Added by the sitting booted on entry 734.*

**Documentation only. It does not change the algorithm as the specification defines it.** It decides what Claude Code
writes beneath one row of the reading file, nothing about what the analysis does.

### What the question is, from scratch

Row 32.1 of the L3 reading file is one sentence of the old design, `ARCHITECTURE.md` §16, *Core — Must Be Implemented*:
a list of everything the whole product must have, from *"Harmonic analysis (functional, modal, extended tonal, jazz)"*
and *"monophonic chord inference"* through *"musical language detector and graceful degradation"* to localization and
accessibility. The reading file says the L3 derivation is silent on it and proposes it **UNPLACED** (no disposition
word yet; a row the user places) [checked: L3 reading file, lines 36092–36111]. It is one claim; §6 does not split it.

The presets-scope ruling of 2026-11-07
(`records/cowork/rulings/cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md`, Ruling 1, part 2C, the user's
word *"yes"*) placed it clause by clause [checked: record lines 49–53]:

> **2C — as its twin L2 Row 34.1 is ruled (1):** Row 32.1, the product's core scope (`ARCHITECTURE.md` §16). The
> *"musical language detector and graceful degradation"* clause RELOCATED to *the uncertainty surface*, travelling with
> Row 1.19 and D-498; the modal and jazz clauses recorded as answered; the homes recorded beside the row as L2 records
> them; *"monophonic chord inference"* recorded UNSETTLED beside the row; the rest, including *"functional"*,
> HISTORICAL as the product's scope status. The product scope stays at `ARCHITECTURE.md` §16.

("Its twin" is the same sentence as it appears in the L2 reading file, there numbered Row 34.1. *The uncertainty
surface* is one of the reading file's destinations that is not a layer: where what concerns confidence and uncertainty
is carried.)

The dispatch's ledger entry for that record (§L.44) quotes this at the row (table line 3820) and leaves to the releasing
sitting how the parts with no disposition word are written, *"as text within the line, or not at all"*, noting that
*"The L2 twin's ruled line was not read by that sitting"* [checked: dispatch lines 3856–3861]. Its check note leaves the
point standing (lines 3870–3874) [checked].

### What the record already says

The working list sorted this as a derivation, not a question (its item (lxxxi)) [relayed: working list lines 3904–3977,
read by this sitting]. Its steps, each checked here where marked:

1. **The row does not stop.** §L.44's point feared a STOP-and-report where §6's claims do not meet the record's
   clauses. §6 has no claims to meet: the row is one sentence, and every clause the record names stands in it word for
   word [checked: L3 reading file, lines 36094–36101]. *Findings in this batch* stops a row only where its content
   *"does not match what the record says of it"* [checked: dispatch lines 222–224]; it matches.
2. **At L2 the parts with no word were written as text inside the one ruled line.** The twin's ruled line [checked: L2
   reading file, line 47551] gives **RELOCATED to *the uncertainty surface* (NOT A LAYER)** for the detector clause and
   **HISTORICAL** for *"the rest of the sentence, as the product's scope status"*, and then, in the same line, quotes the
   clauses recorded as answered (with the ruling that answers each), the six homes, the UNSETTLED clause and *"The
   product scope itself stays at `ARCHITECTURE.md` §16."*
3. **So the L3 line does the same.** The record places the row *"as its twin L2 Row 34.1 is ruled"* and orders the
   items *"recorded beside the row"*, the homes *"as L2 records them"*; L2 records them in its ruled line. Writing them
   nowhere would drop what the record orders recorded. They carry no disposition word, so the row has the two words the
   record names, as at L2. Ruling 2 of the part 2 ruling record already took a twin's ruled line as the model for part 2A
   of the same record.
4. **"Row 1.19" means the L2 row.** The words *"travelling with Row 1.19 and D-498"* are the L2 ruling's, quoted. L2
   Row 1.19 is *"the tension with the abstention target at §5.7a"*, ruled RELOCATED to *the uncertainty surface* beside
   D-498's owed display decision [checked: L2 reading file, lines 767–786]. The L3 reading file's Row 1.19 is a
   different sentence (G1: commit, inherit or abstain per slice), proposed QUARANTINED [checked: L3 reading file,
   lines 735–747], and no ledger entry places it. Read in L3's numbering, the quoted words would tie the clause to the
   wrong row. So the line keeps the record's words and says in brackets that the row is L2's.
5. **One record only.** A search of the whole dispatch for *"32.1"* and *"1.19"* meets them only inside §L.44 (lines
   3814 to 3882) [checked]. So form (b)'s two-record rule (Ruling 3 of the part 2 ruling record) is not met.
6. **The transfer list gets one entry, by the dispatch's own rule.** The detector clause is placed RELOCATED out of
   UNPLACED, so Task 3 (c) item 5 appends it under its destination heading [checked: dispatch lines 5204–5209]. The
   transfer list (§10) has the heading *"To *the uncertainty surface* (NOT A LAYER)."* (line 79701), and no entry under
   it names Row 32.1 (lines 79703–79795, read through) [checked]. Nothing new is needed for this; it follows from item 5.

Applying D-599 (the standing principles first; only what they leave is the user's choice): the two words, the parts
and where the recorded items go follow from the record and the twin's ruled line. **What is the user's:** the line's
wording, which is the writing side's, as all of the dispatch's line forms are; and the weak points below.

### The wording the writing side proposes (the working list's item (lxxxi))

ONE line beneath the row's `*PROPOSED DISPOSITION.*` paragraph, in form (b) (the dispatch's form for a ruled line with a
disposition word: `*RULED DISPOSITION (<record file>, Ruling N).* **<disposition>** — <placement in the record's
words>.`, dispatch line 156 [checked]):

> `*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md, Ruling 1).* **RELOCATED to *the
> uncertainty surface*** for its clause "musical language detector and graceful degradation", "travelling with Row 1.19
> [the L2 reading file's Row 1.19] and D-498", and **HISTORICAL** for "the rest, including "functional", … as the
> product's scope status" — "as its twin L2 Row 34.1 is ruled". Recorded beside the row, as L2 records them: recorded as
> answered, the "modal" clause, by tonality-vocabulary Ruling 1 of 2026-10-04 (the named increment), and the "jazz"
> clause, by chord-vocabulary Ruling 2 of 2026-10-05 (the named increment); homes, "voice leading analysis and
> optimization": the second axis — voice leading; "ornamentation (analysis …)": L2's elaboration relations; "enharmonic
> spelling" and "pickup bars and anacrusis": L0 — The notated record; "chord symbol input": comparison material only
> (`FRAMEWORK.md` §3.1); "incremental analysis cache": C-8 and working-span Ruling 3 of 2026-10-09; "extensible style
> system, initial five styles": the style family; UNSETTLED, "monophonic chord inference" ("No home was found, and this
> filing decides nothing about it."). "The product scope stays at `ARCHITECTURE.md` §16."`

The answering rulings, the homes and the UNSETTLED sentence are the twin's ruled line's words [checked against line
47551]. Three things in the twin's line are not in the L3 record and are left out: *"placed from UNPLACED"*, *"(L2-S6)"*
and its sentence on D-498's register standing. The row was proposed UNPLACED, so the line does not say *as proposed*.

### The weak points, stated by the working list, and one this sitting adds

[relayed: working list lines 3971–3977, except (d)]

- **(a) One line or two.** The line carries two disposition words, each naming its part, as the twin's does. At item
  (lviii) the writing side wrote one line per part instead. If the user prefers that shape, the row gets two lines, the
  recorded items beside the second; the words filed do not change.
- **(b) Whose words.** The homes, the answering rulings and the UNSETTLED sentence are quoted from the twin's L2 line; the
  L3 record gives them only by reference (*"as L2 records them"*). If the user wants the L3 record's words only, the line
  says *"the homes recorded beside the row as L2 records them"*, naming L2 Row 34.1's ruled line, and lists nothing.
- **(c) "The rest".** Which clauses *"the rest"* covers is the record's wording and the twin's, quoted and not judged
  here.
- **(d) Added by this sitting: "(NOT A LAYER)".** The twin's line and the §10 heading both write the destination as
  *the uncertainty surface* **(NOT A LAYER)**; the proposed line, like the L3 record, writes it without those words.
  The destination is the same either way; adding them would only match the twin and the heading.

### The currently decided method

Unchanged. As the record states it [checked: record lines 60–65]: L2 decides key and chord together and publishes the
chord as a degree in its tonality, and the tonality as tonic and mode; L3 publishes facts read off it (chord symbol,
figured bass, harmonic rhythm, cadence with type at each phrase end, phrase and section grouping, key areas, the pivot
re-expression, the modal counts per key area, and, once the application act amends `FRAMEWORK.md`, the catalog matches);
no preset, style label or idiom mixture reaches L2; no preset chooses the catalog L3 reads, and L3's method uses no idiom
tag; a display turns published facts into text; L3 owns the answers to its own questions.

### The alternatives, weighed towards the ultimate objective and the principles

- **A — Ratify the derivation and the line as proposed.** *Towards the objective:* neutral; the analysis is untouched.
  *Towards the principles:* every part the user placed is written at the row, in the words the ruling points to; the L2
  row number cannot be misread as L3's; the row matches its twin.
- **B — Ratify the derivation, with other wording or shape.** Any of weak points (a), (b) or (d): two lines instead of
  one; or the L3 record's words only, with no list; or *(NOT A LAYER)* added.
- **C — The two disposition words only, the recorded items written nowhere.** *Towards the principles:* drops what the
  record orders *"recorded beside the row"*, and the row then says less than its twin.

**The record settles the two words and that the row does not stop.** What is the user's is the line's wording and shape
(A or B), against writing the recorded items nowhere (C).

**To do at release** [relayed: working list (lxxxi), lines 4022–4027]: change §L.44's *Open* point (2) (dispatch lines
3856–3861) and the check note's *"point (2) stands"* (line 3874) and *"Points (1) to (3) stand."* (line 3878) for point
(2), to point to the ruling; write the line into the §L.44 table's line for Row 32.1 (dispatch line 3820); former
wordings kept.

---

## Site 5 — The audit-list point of items (xliii), (xlv) and (xlvi): does the act bring the reading file's list of audit questions into line with the rows it places?

*Added by the sitting booted on entry 735.*

**Documentation only. It does not change the algorithm as the specification defines it.** It decides what Claude Code
writes in one section of the reading file, nothing about what the analysis does.

### What the question is, from scratch

The reading file has a list of audit questions, §11, headed *"The AUDIT QUESTIONS — every QUARANTINED row"*. Its
opening reads: *"Each tabulated member appends its QUARANTINED rows here, in the commit that tabulates it, each with the
audit question its row writes."* [checked: L3 reading file, lines 79980–79983]. (QUARANTINED is the disposition word for
a sentence that says how the current code works, or a measured property of it. Such a row writes one question for a
later audit of the code to answer [checked: §5, lines 390–391].) The entries run member by member, in row order.

The transfer list, §10, has the same kind of opening for RELOCATED rows: *"Each tabulated member appends its RELOCATED
rows here, by target charter, in the commit that tabulates it"* [checked: lines 78925–78928].

The application act writes a ruled line beneath every row a record places. Some rows that were proposed QUARANTINED get
another word, and some rows proposed with another word are ruled QUARANTINED. The dispatch keeps §10 in step with such
changes: Task 3 (c) item 5 adds rows newly placed RELOCATED to §10, and item 6 adds a *LEAVES L3* line beneath the §10
entries of rows that four records say leave [checked: dispatch lines 5204–5223]. **For §11 the dispatch says nothing.**
A search of the dispatch for *"audit list"*, *"§11"* and *"AUDIT QUESTIONS"* meets nothing [checked]. Its check before
the commit (Task 3 (f)) also allows only certain kinds of change to the reading file, and any other kind is a
STOP-and-report and is removed. A §11 addition is not one of the kinds it allows [checked: lines 5248–5252]. So, as
the dispatch stands, the act cannot touch §11.

The working list found four row-parts where this shows [checked: working list, (xliii) lines 1504–1511, (xlv) lines
1646–1655, (xlvi) lines 1716–1722]:

- **Going out of QUARANTINED:** Row 35.154, proposed QUARANTINED, is filed HISTORICAL by the fifth cut. Its question
  stands on §11 [checked: lines 81363–81364]. The fifth-cut surface, ratified with the cut, says *"Row 35.154's audit
  question leaves the reading file's audit list with it"* and that filing HISTORICAL *"takes this row's audit question
  off the reading file's audit list"* [checked: `ratification_surfaces/cowork_l3_s38_fifth_cut_surface_2026_11_03.md`,
  lines 94 and 115–116]. It does not say how.
- **Coming into QUARANTINED:** Rows 43.105 (iii) and 43.124 (ii) (cut 7) and 45.16 (i) (cut 8), each proposed
  RELOCATED, are filed QUARANTINED. Each line quotes its twin's audit question whole [relayed: working list (xlv), (xlvi)].
  None of them is on §11. The member 43 entries go from Row 43.103 to Row 43.109 and from Row 43.123 to Row 43.125. The
  member 45 entries go from Row 45.15 (iv) to Row 45.16 (iii), which is a different claim, to Row 45.17 (i)
  [checked: lines 81914–81926 and 81957–81960].

The four are not the only rows affected. The dispatch's line for the first cut alone re-files five rows *"from
QUARANTINED"* to HISTORICAL [checked: dispatch line 1850], and the dispatch quotes audit questions in rows placed
QUARANTINED out of another proposal elsewhere too (for example lines 1599 and 4670) [relayed: working list (xlv)]. This
sitting did not count how many row-parts there are in all.

### What the record already says

- **What §11 is, by its own words:** a list of *every* QUARANTINED row, each with its question. After the act, a row
  ruled QUARANTINED writes its question in its ruled line, and a row ruled HISTORICAL no longer has one. If §11 is not
  touched, it no longer matches its own heading.
- **The dispatch has two models for a list built from the proposals.** §10 is kept current: rows are added, and lines
  are added beneath entries, with nothing deleted (items 5 and 6). §13, the table of counts, is kept as the proposals'
  table, with one sentence added beneath its heading to say so, and the ruled counts go in a new derived section,
  §13a [checked: Task 3 (d), lines 5225–5234]. §11 opens with the same wording as §10, not as §13.
- **What softens the loss of an audit question:** an audit also runs from the contract side to the code (D-549, as the
  fifth-cut surface quotes it at lines 99–101) [relayed].

Applying D-599: no principle or ruling says which model §11 follows, or whether the act or a later act does it. **#12**
(no text deleted) holds either way. **What is the user's:** which treatment, and the wording, which is the writing
side's as in all the dispatch's line forms.

### The wording the writing side proposes

A new item 7 in Task 3 (c), written on items 5 and 6:

> **7. QUARANTINED placements and the audit questions, §11.** No §11 entry is deleted or edited (#12). (a) Every row-part
> a §L entry places QUARANTINED, out of another proposal, that §11 does not already carry is added to §11 under its
> member's heading, at its place in row order, in §11's own entry form (`- Row n.m — <the audit question>`). The audit
> question is quoted as the row's line quotes it, and the record and ruling go in a parenthesis:
> `*(<record file>, Ruling N.)*`. Check each at §11 by row number and claim before adding it. A member with no block in
> §11 is a STOP-and-report for that row, and no heading is made. (b) Beneath each §11 entry whose row-part a §L entry
> places with a disposition word other than QUARANTINED, ONE line is ADDED at the entry's indentation:
> `*NOT QUARANTINED (<record file>, Ruling N).* — placed **<disposition>** at the row.` A §11 entry naming another claim
> of the row is not touched. A row-part whose line carries no disposition word (a placement outside every charter, a
> held row, a flagged item answered), or which is a STOP-and-report, gets nothing at §11. The rows reached are listed in
> the report under *audit questions added* and *audit questions no longer quarantined*.

And in Task 3 (f) and E3, the kinds of change allowed in the reading file gain *"an audit-question addition or a
NOT QUARANTINED line under (c) item 7"*.

*NOT QUARANTINED* is a label the writing side made for this, on the model of item 6's *LEAVES L3*. It is not a
disposition word. It only says that the row's question no longer stands, and it leaves the entry above it as written.

### Weak points the writing side fixed before putting this

- **Which lines trigger it.** Item 7 uses item 5's words, *"a §L entry places"*, so §11 and §10 are reached by the same
  rule, whatever that rule covers.
- **Rows with no disposition word.** These are named and get nothing. Their proposals still stand, so their §11 entries
  stay true.
- **Leaving §11 untouched with no mark is not offered.** The file would then say every QUARANTINED row is listed when it
  is not. That option is replaced by C below, which says so in the file.

**What remains:** how many row-parts item 7 reaches is not counted here. The act finds them at the rows.

### The currently decided method

Unchanged. As the rulings this dispatch applies leave it, among them for these rows nothing-from-L3 Rulings 1 and 2 and
the L3-S38 ratification [relayed: working list (xli) to (xlvi)]: L2 decides the boundary, the tonality, the chord and
the assignments in one decision; cadential confirmation enters L2 through the progression term over the chords L2
proposes; L3 publishes facts read off L2's reading.

### The alternatives, weighed towards the ultimate objective and the principles

- **A — Item 7 as proposed (§11 treated as §10 is, both ways, for every §L entry).** *Towards the objective:* slightly
  favourable. A later audit that works from §11 finds every question that stands after the act, and is told which ones
  no longer do. *Towards the principles:* §11 matches its own heading, and no text is deleted (#12). The cost is that
  the act does more, by a number of rows not counted here.
- **B — Only the four row-parts the working list names.** 35.154 gets the *NOT QUARANTINED* line, and the other three
  are added. *Towards the objective:* the same as A for these four, but the other re-filed rows (for example the first
  cut's five) leave §11 out of step. *Towards the principles:* the rule depends on which rows one sitting happened to
  meet, not on what the rows say.
- **C — §11 left to a later act, marked as the proposals' list.** One sentence goes beneath its heading, as §13 is
  treated: *"The entries below are the audit questions of the PROPOSALS; rows carrying a RULED or RECORDED line are
  placed as that line says."* The (f) check is widened for that one sentence only. *Towards the objective:* neutral to
  slightly unfavourable. The questions for rows newly ruled QUARANTINED are found only at the rows until a later act
  lists them. *Towards the principles:* honest about the file's state, and the act does the least.

**The record settles** that nothing is deleted and that §11 cannot be left silently out of step with its own heading.
What is the user's is A, B or C.

**To do at release** (A or B): add item 7, or its four-row form, to Task 3 (c) after item 6. Add its kinds to Task 3 (f)
and to E3. Change the working list's notes at (xliii), (xlv) and (xlvi) to point
to the ruling. Former wordings kept. (C): add the sentence to Task 3 (d) beside §13's sentence, and widen (f) and E3 for
it. Former wordings kept.

---

## Site 6 — Item (lxxv) with Part C: the bibliography edit of 2026-11-03 and Task 0's path list

*Added by the sitting booted on entry 736.*

**Documentation only. It does not change the algorithm as the specification defines it.** It decides which file Claude
Code lands in git at Task 0, and what the dispatch says about one *Open* point. Nothing about what the analysis does.

### What the question is, from scratch

`docs/research_papers/BIBLIOGRAPHY.md` is the repository's list of research papers. Each row has a *Local* cell saying
whether the paper's PDF is held in that folder. On 2026-11-03 the user placed four PDFs there, and a Cowork sitting (the
one booted on entry 497) updated the file for them: three Local cells marked ✓, one corrected, two rows added. At the
file as it stands on disk [checked]: the four rows carry a ✓ Local cell (`A10383.pdf` line 120, `Camb_MusPerc2006.pdf`
line 121, `CMA2016.pdf` line 123, `20068.pdf` line 124), and the file's own note records the update by that sitting
(lines 181–194).

Two things in the dispatch touch this.

1. **§L.11's *Open* point (3)** asks whether the carry list names those Local cells as this act's work. The
   thematic-parallelism record calls them *"a later step"* (dispatch lines 884–886 [checked]; the record's lines 92–93
   [relayed: working list (lxxv)]). The working list's item (lxxv) answers it as a derivation, not a question: the carry
   list does not name the file (a search of the carry list for *"BIBLIOGRAPHY"*, *"Local cell"* and *"research_papers"*
   meets nothing [checked]); the step is already done, at the file (above); and the act could not write the file anyway,
   since it is outside the dispatch's write set (*"The landed paths of Task 0, the successor, … the Task-5 files and the
   report are the whole write set."*, dispatch lines 5556–5558 [checked]).
2. **A fact for Task 0, which item (lxxv) left to release (Part C).** Entry 496 §1 lists, among what is not in git,
   *"the `BIBLIOGRAPHY.md` edit of 2026-11-03; the next dispatch's Task 0 lands them"* [checked: entry 496, lines 18–19].
   The dispatch's Task 0 does not name the file. Its path list covers the rulings folder, `ratification_surfaces/`, the
   handoff folder and the dispatch itself, and its search for paths it does not name looks only in those three folders
   [checked: dispatch lines 4898–4956]. A search of the dispatch for *"BIBLIOGRAPHY"* meets only §L.11 and §L.12
   (lines 838, 884, 891, 990) [checked]. So if the edit is still not in git, Task 0 would neither land it nor report it.

**Whether the edit is in git now is not known on this side.** Several batches have run since 2026-11-03. The "not in
git" lists of later entries start again from later points (entry 602 §1 from entry 586, entry 728 §1 likewise), and
neither names the bibliography [checked: entry 602 lines 22–23; entry 728 lines 29–31]. That is silence, not proof that
it was landed. This side runs no shell and no git, so the releasing sitting cannot find out either. Claude Code can.

### What the record already says

- **The record orders the landing.** Entry 496 §1 sends the edit to *"the next dispatch's Task 0"*. That is the standing
  clause (a change not in git lands at the next dispatch's Task 0).
- **Part C of the working list settles who fixes Task 0's path list:** *"Task 0's path list and range, brought up to the
  last entry and record"* is a fact taken at release, *"not put to the user"* [checked: list lines 4130–4134].
- **Item (lxxv)'s answer to §L.11 (3)** is a derivation from the record, the carry list and the write set, each checked
  above.

Applying D-599: the principles and the record decide this. Nothing here is a choice between methods. What is put to the
user is only the ratification of the derivation and of the wording the writing side chose, which is the writing side's
as in all the dispatch's line forms.

### The wording the writing side proposes

A new item 5 in Task 0's path list, after item 4:

> 5. **`docs/research_papers/BIBLIOGRAPHY.md`, only if it carries a change not in git.** Handoff entry 496 §1 lists
> *"the `BIBLIOGRAPHY.md` edit of 2026-11-03"* as not in git, for the next dispatch's Task 0; whether a batch since has
> landed it is not established by the writing side, which runs no git command. Act: `git status --porcelain --
> docs/research_papers/BIBLIOGRAPHY.md; echo "exit:$?"`. No output: already committed — reported, not landed. A line
> starting ` M` or `M` (modified) or `??` (untracked): landed as it stands on disk, never edited. Any other output: a
> STOP-and-report for this path, the rest landed. No other file of `docs/research_papers/` is named or landed.

And three changes beside it, each keeping its former wording:

- Act (3) gains, after *"(plus the families file if it moved)"*: *"(plus item 5's file if its act found it modified or
  untracked)"*.
- E0 gains: *"item 5's path accounted for as landed, already committed or STOP-and-report"*.
- §L.11's *Open* point (3) (lines 884–886), its check note's sentence on point (3) (lines 890–893) and the check row's
  *"§L.11 point (3) (the carry list not read)"* (line 20) point to the ruling, as item (lxxv)'s *To do at release* says.

### Weak points the writing side fixed before putting this

- **Who finds out whether the file is in git.** Item (lxxv) left the fact to the releasing sitting. That sitting runs no
  git, so the check is given to Claude Code, at the object, with a fixed reading of each answer.
- **Task 0's own rule for tracked files.** Act (1) lands a path found already tracked only if it is the families file.
  Item 5 therefore has its own act, and act (3) and E0 are extended by name, so no other tracked file comes in by this
  route.
- **The four PDFs are not named.** Entry 496 lists only the bibliography edit. And the file marks one of the four PDFs
  *"rule 3 binds, do not redistribute"* (line 121), so pushing PDFs to the central repository is not something to add
  without a ruling. Item 5 lands the one file only.
- **Whether the report mentions it.** Item (lxxv)'s own weak point was that §L.11 (3), being settled, is not listed in
  the report. With item 5, the report carries the file's standing anyway, under Task 0's account (E0). So nothing more
  is needed for that.

**What remains:** whether the file is in git now. Claude Code's act settles it, and either answer is handled.

### The currently decided method

Unchanged. Ruling 1 of the thematic-parallelism record is itself an algorithm change, ruled on 2026-11-03, not decided
here [relayed: working list (lxxv)]: L1's published list (IC-L1 S-50) gains a restatement relation over the notes, its
matching measure UNESTABLISHED until measured; the charter's L1 → L3 row gains the relation; L3-S23's family (iv),
*thematic return*, reads it; and L3's bar on computing the relation itself stands.

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. A releasing sitting cannot establish the file's standing in git, and leaving it out leaves
a change the record ordered landed possibly never landed, with nothing to report it. Both of those are worse towards the
principles (the record's order not carried out, and a fact asserted without being checked), and neither touches the
objective. So the derivation and the wording above are put for ratification, not as a menu. If the user wants something
different (for example, the PDFs landed too, or the file left out), that is his overrule.

**To do at release:** write item 5 into Task 0 after item 4; extend act (3) and E0 as above; change §L.11's *Open* point
(3), its check note's sentence on point (3) and the check row's words for it to point to the ruling; former wordings
kept.

---

## Site 7 — A1 and A2: which ADOPTED word a line writes, and when it says *as proposed*, with (lxxx)'s fact on Row 40.61

*Added by the sitting booted on entry 737.*

**Documentation only. It does not change the algorithm as the specification defines it.** It fixes how Claude Code
copies a ruling's word into the reading file's line for each row. Nothing about what the analysis does.

### What the question is, from scratch

The L3 reading file (`ratification_surfaces/cowork_comparison_l3_reading.md`) gives every outgoing statement a proposed
disposition, in a paragraph opening `*PROPOSED DISPOSITION.*`. Its §5 has two ADOPTED words [checked: lines 382–386]:

- **ADOPTED — carried**: *"a derived statement already carries this content in substance (named by its L3-S-number)"*;
- **ADOPTED — proposed**: *"no derived statement carries it"*; a proposal to the user that the content be added.

§5 also says UNPLACED *"is NOT a sixth disposition — it is a row the user places"* (line 396). And beside each row stands
a *current-text axis*, one verdict per derived statement named at the row; §5 defines *AGREES* as *"the derived statement
and the outgoing statement say the same thing in substance"* and *THE DERIVATION IS SILENT* as *"no derived statement
speaks to this outgoing statement"* (lines 374–377) [checked].

The dispatch's form (b) writes each ruled line as `*RULED DISPOSITION (<record file>, Ruling N).* **<disposition>** —
<placement in the record's words>.` and says *"A row the record places "as proposed" still gets its line, saying as
proposed."* (dispatch lines 155–157) [checked].

Two groups of the dispatch's *Open* points ask what that means in practice.

1. **A1, which ADOPTED word?** Many records write a bare *"ADOPTED"*, or *"carried"*, or *"ADOPTED, carried by"* an added
   statement, without saying which of the two words. Sites, each read at its line [checked]: §L.5 (1) (line 566), §L.8 (1)
   (754), §L.13 (1) (1051), §L.25 (1) (2152), §L.26 (1) (2247), §L.27 (1) (2344), §L.28 (1) (2426), §L.40 (1) (3493),
   §L.41 (1) (3590), §L.42 (1) (3684), §L.51 (1) (4516).
2. **A2, *as proposed* or not?** Other records name **ADOPTED — proposed** in full. Each *Open* point asks whether the line
   says *as proposed*, or something else, which turns on each row's own proposed word. Sites [checked]: §L.30 (1) (line 2600),
   §L.31 (1) (2684), §L.32 (1) (2778), §L.33 (1) (2858), §L.34 (1) (2939), §L.35 (1) (3019), §L.36 (1) (3121), §L.38 (1)
   (3301), §L.39 (2) (3410–3411).

Until these are settled, the dispatch makes every row they name a STOP-and-report (stopped and listed for the user, with
nothing written).

### What the record already says

The working list's Part A gives A1 and A2 a derivation, not a question, rules (i) to (v) [checked: list lines 136–152].
In short: (i) a bare *"ADOPTED"* with no L3-S number takes the row's own proposed word, and says *as proposed*; (ii) an
L3-S number named by the record gives **ADOPTED — carried** with that number; (iii) *"carried by"* an added statement gives
**ADOPTED — proposed**, since an added statement has no L3-S number and is not a derived statement; (iv) where the ruling
adopts narrower content than the proposal (§L.27 part E, Rows 38.47 and 38.48; §L.28, Row 36.106 (i)), the line does not
say *as proposed*; (v) where the row's proposed word *"is anything but an ADOPTED word"*, or the row has no
`*PROPOSED DISPOSITION.*` paragraph, the row is a STOP-and-report.

**The weak point, found at the rows: rule (v) would stop rows the user has ruled ADOPTED.** Some of these rulings were
made on rows the reading file left UNPLACED, and rule (v) treats UNPLACED as *"anything but an ADOPTED word"*. Read at
the rows by offset [checked]:

- §L.30's Rows 46.16 and 44.2, which the record places **ADOPTED — proposed** in full: both proposed **UNPLACED** (reading
  file lines 63797, 60957).
- §L.40's Row 40.61: proposed **UNPLACED**, *"Derived statements that speak to it. None."*, axis **THE DERIVATION IS
  SILENT** (lines 55090–55094). This is (lxxx)'s fact [checked: list lines 3871–3876]: as the rules stand, Row 40.61's
  ADOPTED line meets rule (v).
- §L.40's Row 48.19: proposed **UNPLACED**; axis *"L3-S5: **AGREES**"* (lines 66120–66125). Row 48.20 (ii): proposed
  **UNPLACED**; axis *"(ii) L3-S5: **AGREES**"* (lines 66142–66149).
- §L.41's Row 57.377: axis **THE DERIVATION IS SILENT** (lines 75071–75073); its proposal line not read.
- §L.51's Row 12.35 (iii): proposed **UNPLACED**; axis **THE DERIVATION IS SILENT** (lines 19556–19566).

So, written as it stands, rule (v) would turn rulings the user made on UNPLACED rows into STOP-and-reports. That works
against the rulings, and against §5's own sentence that an UNPLACED row is one the user places. How many rows that is
was not counted.

**What §5 settles instead.** When a ruling adopts an UNPLACED row without naming the word, §5's definitions name it from
the row's current-text axis, with no new choice. *AGREES* (*"say the same thing in substance"*) is the condition
*ADOPTED — carried* states (*"already carries this content in substance"*). *THE DERIVATION IS SILENT* means no
derived statement carries the content, which is the condition of *ADOPTED — proposed*. *DIFFERS*, or more than one
derived statement named, does not settle it. Applying D-599: the principles and §5 decide the words. What is put to the
user is the ratification of the derivation and of the wording, which is the writing side's.

### The wording the writing side proposes

In form (b), after *"A row the record places "as proposed" still gets its line, saying as proposed."*, this paragraph is
added, the wording above it untouched:

> **Which ADOPTED word, and when *as proposed* is written.** For each row-part a record places ADOPTED, read the row's
> `*PROPOSED DISPOSITION.*` paragraph and its *Current-text axis* for that part; a row with no `*PROPOSED DISPOSITION.*`
> paragraph is a STOP-and-report. Then:
> (1) **The record names the word in full** (*ADOPTED — proposed*, or *ADOPTED — carried* with its L3-S number): that word.
> (2) **The record names an L3-S number as carrying the content**: **ADOPTED — carried** with that number.
> (3) **The record says the content is *"carried by"* an added statement** (form (a)): **ADOPTED — proposed**, the placement
> quoting the record's *"carried by …"* words. An added statement has no L3-S number and is not a derived statement. If
> the axis for that part names a derived statement, the row is a STOP-and-report.
> (4) **The record writes a bare *"ADOPTED"* or *"carried"* and names no L3-S number:** if the row's proposed word for that
> part is an ADOPTED word, that word. Otherwise the word is read at the axis for that part: exactly one derived statement
> named, **AGREES**, gives **ADOPTED — carried** with its number; **THE DERIVATION IS SILENT** gives **ADOPTED —
> proposed**; anything else is a STOP-and-report.
> The line says *as proposed* only where its word, and its number if any, are the row's own proposed word for that part,
> and the record adopts the content as proposed. Otherwise *as proposed* is not written, and the placement is given in
> the record's words. That includes a row proposed UNPLACED, and a ruling that adopts narrower content than the proposal
> (§L.27 part E, Rows 38.47 and 38.48; §L.28, Row 36.106 (i)). No other wording (such as *"placed from"*) is added.
> Applied row by row; the rows reached are listed in the report under *ADOPTED words read at the row*.

And beside it, each keeping its former wording: every A1 and A2 *Open* point listed above points to the ruling. That
includes §L.51 (1)'s question whether a row may be *carried* by an added statement (answered: no, by (3)). It also
includes §L.40 (1) for Rows 48.19, 48.20 (ii) (first half) and 40.61. By (4) those read as **ADOPTED — carried (L3-S5)**,
**ADOPTED — carried (L3-S5)** and **ADOPTED — proposed**, none *as proposed*. That reading is the writing side's
reading of the axis, not applied by this sitting.

### Weak points the writing side fixed before putting this

- **Rule (v) and the UNPLACED rows**, above: replaced by (4)'s axis test, the STOP-and-report kept for a row with no
  proposal paragraph, for *DIFFERS*, and for more than one derived statement named.
- **A2's *"placed from"***: form (b) has no such wording. Ruling 6 of the part 2 ruling record states its two lines are
  *"not as proposed (the row was proposed UNPLACED)"*, and the lines themselves add no such wording. So the paragraph says *as proposed* is written or not, and
  adds nothing else.
- **Rule (iii) where a derived statement also speaks to the part**: the word *ADOPTED — proposed* would then contradict
  §5's *"no derived statement carries it"*, so that case is a STOP-and-report, not a guess.
- **Report:** the rows reached are listed, so the user sees each word that was read at a row and not given by a record.

**What remains:** which word each row gets is read by Claude Code at the row. A row the paragraph cannot settle stops
and is listed.

### The currently decided method

Unchanged: the paragraph changes no record's ruling, only how its word is copied. As one example, the display-family
record's method, relayed from the working list (lxxx): L2 decides
key and chord together and publishes the chord as a degree in its tonality; L3 publishes facts read off it; L3
publishes no tonic / subdominant / dominant summary and writes nothing into the score; a display turns published facts
into text.

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The working list's rules as written would leave the rulings on the rows above, and on any
like them, unapplied as STOP-and-reports, though §5 settles their words. That is worse towards the principles (rulings made and not carried
out), and towards the objective it only delays. Settling each row's word by a question to the user would ask what §5
already answers (D-599). So the derivation and the paragraph above are put for ratification, not as a menu. If the user
reads *AGREES* and *ADOPTED — carried* as not the same test, that is his overrule, and the UNPLACED rows with an AGREES
axis stay STOP-and-reports.

**To do at release:** add the paragraph to form (b) after its *"as proposed"* sentence; change each A1 and A2 *Open*
point listed above to point to the ruling; change the working list's A1 and A2 *To do at release* (list line 151) to point
there; former wordings kept.

---

## Site 8 — Item (l): Rows 19.39 (ii) and 57.511, placed HISTORICAL by one ruling and left UNPLACED by a later one

*Added by the sitting booted on entry 738.*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles which line, if any,
two rows of the reading file get. Nothing about what the analysis does.

### What the question is, from scratch

Two rows of the L3 reading file carry the old sentence that a chord span always lies inside one phrase (*"chord-spans ⊂
punctuation-spans"*: every phrase end would then also be a boundary of L2's harmonic spans) [checked]:

- **Row 19.39, claim (ii)** (line 24495). Its axis: *"(ii) L3-S8: **DIFFERS**"*; the difference: L3-S8 says *"Every
  change point and both span edges are candidate phrase ends"*. Proposed: *"(ii) **UNPLACED** — read: the two texts
  above."* (lines 24501, 24505–24509). The row has five claims; the others are not part of this question.
- **Row 57.511** (one claim, the same sentence in another document). Axis *"L3-S8: **DIFFERS**"*; proposed **UNPLACED**,
  *"as Row 19.39 (ii)"* (lines 75229–75237).

Two ruling records speak to these rows, and they say different things:

1. **The chord-span pair record** (`cowork_rulings_2026_11_08_l3_chord_span_pair_group_sitting.md`, its sitting booted on
   entry 589), Ruling 1, the user's word *"yes"* [checked: lines 19, 25–40]: *"Rows 19.39 (ii) and 57.511 — Recorded as
   decided against by phrase-ends Ruling 1 of 2026-11-02 (L3-S8 as derived: "Every change point and both span edges are
   candidate phrase ends"; "no item of evidence forces or forbids a phrase end") and DP-J"*. It also says: *"Phrase-ends
   Ruling 1's candidate set already admits a phrase end inside a harmonic span."*
2. **The disposition-words record** (`cowork_rulings_2026_11_08_l3_disposition_words_sitting.md`, its sitting booted on
   entry 606, so later), Ruling 1, the user's word *"yes"* [checked: line 35]: *"§6: Rows 19.39 (ii) and 57.511 stay
   **UNPLACED**; the act marks them STOP-and-report."*

The dispatch, as it stands, writes no line for either row: §L.2 lists them as *"UNPLACED — STOP-and-report"* (lines
335–336), §L.48's table gives the HISTORICAL line and then says *"as the form now reads, both rows are STOP-and-report"*
(line 4189), and §L.48's *Open* point (1) leaves to the releasing sitting *"Which governs"* (lines 4221–4231) [checked].
(*STOP-and-report*: the row is stopped and listed for the user, with nothing written. *HISTORICAL*: the reading file's
word for a superseded plan; *form (b-H)* is the dispatch's line for a row a record decided against, quoting the record's
sentence, lines 162–167.)

### What the record already says

**The later ruling gives its own ground, and it is a fact it had not checked.** Its surface
(`ratification_surfaces/cowork_l3_disposition_word_surface_2026_11_08.md`), §6, read whole [checked: lines 84–87]:
*"Neither record places them. Whether L3-S8 decides against the nesting depends on whether L1's change points can fall
inside one of L2's chord spans. This sitting did not check that. **They stay UNPLACED, the honest default**; the act marks
them STOP-and-report."* Its §8 lists *"whether L1's change points fall inside L2's chord spans"* under *"Not checked"*
(lines 125–126). *"Neither record"* means the two early phrase records its §0 names, the phrase-ends and phrase-units records
(lines 14–15). The surface and its record were searched for the chord-span pair record (*"chord-span pair"*,
*"chord_span_pair"*, *"589"*) and neither names it [checked].

**The earlier ruling settled exactly that fact.** *"Phrase-ends Ruling 1's candidate set already admits a phrase end inside
a harmonic span"* (chord-span pair record, line 40), and on that ground placed the rows as decided against.

**What UNPLACED is.** The reading file's §5: UNPLACED *"is NOT a sixth disposition — it is a row the user places"* (line
396) [relayed from site 7 of this file]. So the later ruling names no disposition for the rows; it leaves them for the user to place,
because the two records it had read did not place them. The user had placed them, on the very fact the later sitting left open.

**The word follows from a ruling already made.** The application-surface record
(`cowork_rulings_2026_11_08_l3_application_surface_sitting.md`, its sitting booted on entry 601), Ruling 1, the user's word
*"yes"* [checked: lines 24–27]: *"every row an L3 ruling record says it decides against is re-marked **HISTORICAL** by the
application act, its line quoting the record's own placement in the record's words. Where a record decides against only a
part of a row, the line names that part only."* The chord-span pair record's lines 25 and 29 are the two hits of form
(b-H)'s search for *"decided against"* in it (§L.48, line 4198) [checked at the record].

**The two-record rule is not met.** Form (b), as Ruling 3 of the part 2 ruling record words it, applies by part and stops
a part *"where two records' lines fall on the same part with differing dispositions"*. The disposition-words record
gives these rows no line: UNPLACED is not a disposition. So only one record gives a line, and the two-record rule does not stop it.
Each row is still listed in the report under *rows named by more than one record* (form (b)'s own sentence), with both
records' words, so the user sees both.

Applying D-599: the records decide this. The later ruling's STOP-and-report rests on a ground it states, an unchecked fact;
a ruling the user had already given answers that fact. What is put to the user is the ratification of that derivation and
of the lines below.

### The wording the writing side proposes

The rows get form (b-H) lines from the chord-span pair record, each beneath the row's `*PROPOSED DISPOSITION.*` paragraph,
the proposed paragraph kept:

> Row 19.39: `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_chord_span_pair_group_sitting.md, Ruling 1).* (ii) **HISTORICAL** — "Recorded as decided against by phrase-ends Ruling 1 of 2026-11-02 (L3-S8 as derived: "Every change point and both span edges are candidate phrase ends"; "no item of evidence forces or forbids a phrase end") and DP-J".`

> Row 57.511: `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_chord_span_pair_group_sitting.md, Ruling 1).* **HISTORICAL** — "Recorded as decided against by phrase-ends Ruling 1 of 2026-11-02 (L3-S8 as derived: "Every change point and both span edges are candidate phrase ends"; "no item of evidence forces or forbids a phrase end") and DP-J".`

The disposition-words record's *"stay UNPLACED; the act marks them STOP-and-report"* gives no line and does not stop these
rows; it is recorded in the ruling as answered by the chord-span pair record's Ruling 1. That record is not edited. Row
19.39's other claims keep what other entries say of them. The added sentence the chord-span pair record orders
(*"Harmonic spans and phrase units cut across each other: …"*, §L.48 amendment 1) is not touched.

### Weak points the writing side fixed before putting this

- **The list's weak point, stated plainly:** the derivation reads a ruled sentence (*"the act marks them
  STOP-and-report"*) as answered by a ruling that sentence does not mention. Checked at the objects above: the sentence
  carries its own ground (*"This sitting did not check that"*), and the earlier ruling answers that ground. This cannot be
  fixed further on the writing side: whether the user meant the later sentence to stand regardless is his to say. That is
  named below as his overrule, not offered as an option of equal standing.
- **A place the list's *To do* did not name:** the dispatch's check row (line 20) ends one passage with *"Left for the
  releasing sitting: §L.48 point (1)."* [checked]. Added to the *To do* below. The pointers at §L.26 (line 2233) and
  §L.55 (line 4890) send the reader to §L.48's *Open* point (1), which will point to the ruling, so they need no change.
- **The lines themselves:** the list gives the placement, not the full lines; they are written out above, in form (b-H)'s
  template, with the record's sentence quoted as the record writes it (its bold left out), Row 19.39's line naming claim
  (ii) only (form (b)'s split-row rule).

### The currently decided method

Unchanged: the chord-span pair record's method [checked: lines 41–46]. L2 divides the working span into harmonic spans,
each with one chord and one tonality, with rivals and their mass, no two adjacent spans sharing both; L3 decides where
phrases end as a weighed choice among every change point and both span edges, published with rivals and their mass, no
item of evidence forcing or forbidding a phrase end; the phrase reading tiles the working span; a change of tonality may
fall inside a phrase unit and a phrase may end without one; L3 never revises L2.

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. Keeping the STOP-and-report would send the two rows back to the user in Claude Code's report,
to be placed by him, when he has already placed them on the fact the STOP waited for. Towards the principles, that leaves
a ruling made and not carried out; towards the objective, it only delays. So the derivation and the two lines are put for
ratification, not as a menu. If the user reads his *"yes"* to the later §6 as standing whatever had been ruled before, that
is his overrule, and both rows stay STOP-and-report.

**To do at release:** change §L.48's *Open* point (1) (dispatch lines 4221–4231) to point to the ruling; in §L.48's table
line (line 4189), the sentence *"See *Rows named by more than one record*: as the form now reads, both rows are
STOP-and-report."*; §L.2's line for the two rows (lines 335–336); §L.55's table line and notes for them (lines 4848,
4863–4864 and 4887–4888); and the check row's *"Left for the releasing sitting: §L.48 point (1)."* (line 20), each to
point to the ruling; change the working list's (l) *To do at release* (its lines 1957–1960) to point there; former
wordings kept.

---

## Site 9 — Item (li): Rows 7.48 (i), 7.294 (v) and 7.331, held by ruling with DP-O: a line saying UNPLACED, or no line

*Added by the sitting booted on entry 739.*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles whether three rows
of the reading file get a line, and which. Nothing about what the analysis does.

### What the question is, from scratch

Four rows of the L3 reading file carry the old function-layer design's sentences placing prolongational reduction (the
reading of a passage as the elaboration of fewer, deeper harmonies, as in Schenkerian analysis) outside the layer, or in
*"a later layer"* [checked at the reading file, each found by the row-heading search]:

- **Row 7.47** (line 3903): reduction *"out of scope"*. Proposed **UNPLACED** (line 3912).
- **Row 7.48, claim (i)** (line 3918): reduction *"belongs to a later layer"*. Proposed *"(i) **UNPLACED** — travelling
  with Row 7.47"* (line 3930). Its claim (ii) is proposed ADOPTED — carried (L3-S16) and is not part of this question.
- **Row 7.294, claim (v)** (line 7712): *"no prolongational reduction here"*. Proposed *"(v) **UNPLACED** — travelling
  with Row 7.47"* (lines 7735–7736). Its claims (i) to (iv) are not part of this question.
- **Row 7.331** (line 8277): reduction *"explicitly a later layer, not this one"*. Proposed **UNPLACED** — *"travelling
  with Row 7.47"* (line 8286).

The four rows touch DP-O, the framework's open question whether the analysis commits to a hierarchical reading of
harmony, which `FRAMEWORK.md` §9 leaves *"open, and deliberately not foreclosed"* [relayed from the record's §0;
`FRAMEWORK.md` not opened].

**The ruling.** The prolongational-reduction record
(`cowork_rulings_2026_11_08_l3_prolongational_reduction_group_sitting.md`, its sitting booted on entry 588), read whole
[checked]. The user chose alternative A, *"mirror the L2 ruling row for row"* (lines 26–27, 32–36): Row 7.47 is RELOCATED
to L2, carried there by L2-S31, *"It means "not adopted in this specification"; it does not foreclose DP-O"* (lines
37–39); and

> **Rows 7.48 (i), 7.294 (v), 7.331 — held UNPLACED, travelling with DP-O**, as their L2 twins Rows 5.53 (i), 5.303 (v)
> and 5.342 are. They are not placed and not lost: whoever takes up DP-O reads them with the L2 rows. (lines 40–41)

Its count: *"4 of 4 reached — one placed, three held by ruling"* (line 43).

**What the dispatch writes now** [checked]. §L.47's table gives the three held rows a form (b) line, **UNPLACED**, *as
proposed*, quoting the hold sentence (dispatch line 4092). Its *Open* point (1) calls that *"The writing side's reading
of form (b); challengeable"* (lines 4132–4142), and the check row leaves it to the releasing sitting (*"Left for the
releasing sitting: §L.47 points (1) and (2)."*, line 20). Row 7.47's own line (line 4091) is not in question.

(*Form (b)*: the dispatch's template for a ruled line, `*RULED DISPOSITION (<record file>, Ruling N).* **<disposition>**
— <placement in the record's words>.`, line 156: a disposition word in the bold place. *Held by ruling*: a ruling keeps
the row out of every disposition until an open question is answered.)

### What the record already says

**UNPLACED is not a disposition.** The reading file's §5 [checked: lines 395–396]: *"**UNPLACED** — this session cannot
defend one disposition in one sentence at the two texts. … **This is the honest default and it is NOT a sixth
disposition** — it is a row the user places."* A form (b) line puts a disposition word in its bold place. A ruled line
with **UNPLACED** there would write, as a ruled disposition, a word §5 says is not one, for rows the user said are *"not
placed"*.

**With no line, each row still reads true.** Each of the three proposals is UNPLACED, and the ruling keeps them
unplaced. So nothing at the row goes false if no line is added. This is the difference the part 2 ruling record's
Ruling 4 turned on: there, three held rows (Rows 8.23, 8.35 (i), 8.113 (ii)) got a line with no disposition word
because their proposal was an ADOPTED word that the record said *"no longer stands"*; part 2b's site 2, which the user
ratified as Ruling 4, gave as its reason that at item (li) *"held rows got no line, because their proposal (UNPLACED)
stayed true"* (this file, lines 174–177) [checked].

**The L2 twins got no line.** At the L2 reading file [checked, each row found by the row-heading search]: Row 5.52
carries score-decomposition Ruling 4's ruled line (line 4899); Row 5.53's only ruled line names claim (ii) (line 4925),
none for (i); Row 5.303's lines name claims (i) to (iv) (lines 9141–9147, the entry ending at line 9149), none for (v);
Row 5.342 has no line beneath its proposal (lines 9711–9713). The L2 application dispatch
(`cc_instruction_l2_application_2026_10_10.md`) wrote it so [checked: its lines 2200–2201]: *"**No line from this
record:** Rows 5.53(i), 5.303(v), 5.342 and 6.113 (… — each keeps its proposal, UNPLACED)"*. Writing no line at L3
leaves the L3 copies of the same sentences as their L2 copies stand.

**"Not lost" holds without a line.** Each of the three proposals reads *"travelling with Row 7.47"* (above), and Row
7.47 gets its RELOCATED line, carrying *"it does not foreclose DP-O"* (dispatch line 4091) [checked].

**The disposition-words record's STOP does not reach these rows.** Its *"the act marks them STOP-and-report"* is said
of Rows 19.39 (ii) and 57.511, and the part 2 ruling record's Ruling 10 answered it for those two [checked at the part 2
ruling record's Ruling 10, which quotes it; the disposition-words record not opened by this sitting]. *Open* point (1)'s comparison with it therefore decides
nothing for these three.

**No other word is derived** [relayed from the working list (li), lines 1997–2000; the surface
`cowork_l3_prolongational_reduction_group_surface_2026_11_08.md` not opened]: its §3A weighed RELOCATED and HISTORICAL for
these three and the user did not choose them; QUARANTINED and DISCARDED are proposed by neither §6 nor the record.

Applying D-599: the reading file's own definition and the ruling's own words leave no disposition word for these rows,
and the user's Ruling 4 already rests on the distinction that sends them to no line. What is put to the user is the
ratification of that derivation.

### The wording the writing side proposes

- **At the rows:** no line from this record. Rows 7.48 (i), 7.294 (v) and 7.331 each keep their proposed UNPLACED, the
  proposed paragraph untouched. They are not counted in the ruled distribution.
- **In the report:** each of the three is listed in Claude Code's report as held by ruling (the listing Ruling 4 names for its rows),
  with the record's hold sentence quoted: *"held UNPLACED, travelling with DP-O, as their L2 twins Rows 5.53 (i), 5.303 (v)
  and 5.342 are. They are not placed and not lost: whoever takes up DP-O reads them with the L2 rows."*
- **In §L.47's table** (dispatch line 4092): the line for the three rewritten as *"No line from this record"*, quoting the
  same sentence, each row keeping its proposed UNPLACED and listed in the report as held by ruling; the check sum (lines
  4094–4095) rewritten to read one row given a line and three held by ruling with no line, 1 + 3 = 4.

### Weak points the writing side fixed before putting this

- **The report.** The working list's item (li) (lines 1969–2015, read whole) says nothing about the report, so the three rows would have been
  findable only by reading the dispatch's ledger. They are now listed under *held by ruling*, as Ruling 4's rows are.
- **A place the list's *To do* did not name:** the check row's *"Left for the releasing sitting: §L.47 points (1) and
  (2)."* (line 20) [checked]. Added to the *To do* below for point (1) only; point (2) (Row 10.123) is not part of this
  site. Also the check note's *"Points (1) and (2) stand."* (line 4153) [checked], for point (1) only.
- **The list's own weak point, stated plainly:** that *"mirror the L2 ruling row for row"* reaches the form of the
  reading-file line, and not only the placement, is the writing side's reading; the record says *"Only the form
  remained"* (line 23) of the placement question, and the L2 dispatch's *"No line from this record"* was the writing
  side's handling there, not a ruling. This does not decide the question by itself: the derivation above rests on §5's
  definition and on the distinction Ruling 4 turned on, which hold whatever *"row for row"* reaches.

### The currently decided method

Unchanged: the prolongational-reduction record's method [checked: lines 45–49]. DP-O stays open: no hierarchical reading
of harmony is adopted, and none is foreclosed. L3 publishes the cadence at each phrase end with its type, the phrase and
section grouping (sections may nest), the chord symbol as a view of the decided chord, the figured bass and the harmonic
rhythm; which notated marks end a phrase is decided at L3, the decisive further evidence being cadential; a read-off fact
never revises the decision it was read off; L3 contains no reduction of harmony.

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The dispatch's present line, the alternative, would write UNPLACED in the place of a
disposition, against §5's definition, and would treat these three held rows differently from the three held rows of
Ruling 4 on a ground Ruling 4 itself drew. Towards the objective, neither choice changes the analysis, and with the
report listing in place, neither loses the rows. So the derivation and the wording above are put for ratification, not as
a menu. If the user wants a line at each row anyway, that is his overrule: the dispatch's present form (b) line stays, or
a line with no disposition word in Ruling 4's form is written; either is his to name.

**To do at release:** change §L.47's *Open* point (1) (dispatch lines 4132–4142), the check note's *"Points (1) and (2)
stand."* (line 4153) for point (1), and the check row's *"Left for the releasing sitting: §L.47 points (1) and (2)."*
(line 20) for point (1), to point to the ruling; in the §L.47 table, rewrite the line for the three rows (line 4092) and
the check sum (lines 4094–4095) as above; change the working list's (li) *To do at release* (its lines 2012–2015) to
point there; former wordings kept.

---

## Site 10 — Item (lii): Rows 36.5 (ii), 45.14 (i) and 45.15 (i), which a ruling says "stay proposals": a line saying RELOCATED *as proposed*, or no line

*Added by the sitting booted on entry 740.*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles whether three
row-parts of the reading file get a line. Nothing about what the analysis does.

### What the question is, from scratch

Three row-parts of the L3 reading file quote old documents that publish a confidence as a *"Class-M"* margin (the
confidence contract's old class for a declared margin), where the derived statement L3-S32 makes L3's mass *"the model's
own distribution, not calibrated"*. Each is marked **DIFFERS** against L3-S32 and each is proposed **RELOCATED** to *the
uncertainty surface* (the framework's home for how uncertainty is shown, which is not a layer) [checked at the reading
file, each row found by the row-heading search]:

- **Row 36.5, claim (ii)** (row at line 39959): the boundary-strength profile's published form is *"a **Class-M boundary
  confidence**"*. Proposed *"**RELOCATED** — to ***the uncertainty surface***, as Row 8.78 (i) placed the grouping's
  declared confidence"* (lines 39976–39977). Its claim (i) is proposed RELOCATED to L1 and is not part of this question.
- **Row 45.14, claim (i)** (row at line 62710): the chord decision's confidence, a squashed composite declared *"M
  (declared-composite)"*. Proposed *"**RELOCATED** — to ***the uncertainty surface***, as Row 43.7 (ii), departing from
  Row 10.137 — placement (l)"* (lines 62738–62739). Its claims (ii) to (v) are not part of this question.
- **Row 45.15, claim (i)** (row at line 62748): the function decision's confidence, the cadence's among it, also *"M
  (declared-composite)"*. Proposed *"**RELOCATED** — to ***the uncertainty surface***, as Row 43.7 (ii)"* (line 62777).
  Its claims (ii) to (v) are not part of this question.

**The ruling.** The mass-and-status record (`cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md`), read whole
[checked]. Its §2 sorts the sixteen DIFFERS row-parts of L3-S32 and L3-S34. For these three, §2 (e) reads (lines 74–75):

> **(e) Open at both sides, the L3 proposals standing:** 36.5(ii) (twin 40.5 proposed to L3's read-off facts), 45.14(i)
> (twin 52.12(i) proposed QUARANTINED), 45.15(i) (twin 52.13(i) proposed QUARANTINED). No ruling on either side.

(*Twin*: the same sentence of the same old document, as read in the L2 reading file.) Ruling 2 (the user's word
*"yes"*) ratifies L3-S32 to L3-S36 *"With them, the row placements of §2 (a) to (e)"* (lines 123–124), and its
documentation sentence reads (lines 129–130): *"the rows re-marked as §2 lists, by the application dispatch, not now.
Rows 36.5(ii), 45.14(i), 45.15(i) stay proposals."*

**What the dispatch writes now** [checked]. §L.19's table gives the three no line, *"On the writing side's reading"*
(dispatch line 1602). Its *Open* point (1) leaves open *"whether a ratified "stay proposals" is a placement to be lined"*
(lines 1623–1627). Its check note says that until point (1) is settled, Task 3 (a) *"gives the three rows no line and
lists them in the report under *rows the act could not place*"* (lines 1640–1641). The check row leaves *"§L.19 point
(1) (Rows 36.5 (ii), 45.14 (i), 45.15 (i), no line until settled)"* to the releasing sitting (line 20).

(*Form (b)*: the dispatch's template for a ruled line, `*RULED DISPOSITION (<record file>, Ruling N).*
**<disposition>** — <placement in the record's words>.` (line 156). Its next sentence: *"A row the record places "as
proposed" still gets its line, saying *as proposed*."* (line 157).)

### What the record already says

**The record does not place the three.** Form (b)'s *"as proposed"* sentence is for a row the record places as
proposed. This record says the three are *"Open at both sides"*, with *"No ruling on either side"*, and its own
documentation sentence sets them apart from *"the rows re-marked"*. What Ruling 2 ratified for them is therefore that
they are not re-marked. A line **RELOCATED** *as proposed* would write, as a ruled disposition, a placement of which the record
says *"No ruling on either side"*.

**"Stay proposals" is the route ruling's wording**, which the dispatch's ruling ledger quotes and reads: *"Rows no family
reaches stay proposals." So a row no record names gets NO line.* (dispatch lines 101–102) [checked at the dispatch; the
route record relayed, not opened]. That the mass-and-status record means the same handling by the same words is the
writing side's reading. The working list notes the same handling in three earlier items, (xl), (xlvii) and (li)
[relayed from the list (lii), lines 2039–2043]; (li) is now ruled that way (the part 2 ruling record's Ruling 11).

**With no line, each row still reads true.** Each part's proposal is RELOCATED to *the uncertainty surface* and the
record leaves it standing, so nothing at the row goes false.

**§10 (the transfer list) needs nothing** [checked]. Row 36.5 (ii) stands in the entry at line 79725 and Rows 45.14 (i)
and 45.15 (i) in the entry at line 79772, under the heading *"To *the uncertainty surface* (NOT A LAYER)."* (line 79701).
Task 3 (c) item 5 appends only row-parts a §L entry *places* RELOCATED and that §10 does not already carry (dispatch
lines 5204–5209); item 6 adds a *LEAVES L3* line only for a row with a ruled line from the four records it names
(lines 5210–5216). Neither reaches these three. With no line, each proposal and its §10 entry agree.

**The case that went the other way, stated** [relayed from the list (lii), lines 2044–2047; neither the figured-bass
record nor the §L.16 table read by this sitting]. §L.16 gives RELOCATED lines *as proposed* on the figured-bass record's
*"Their proposals stand"*. The words quoted there carry neither *"open at both sides"* nor *"no ruling"*; this record
carries both.

Applying D-599: the record's own words (*"No ruling on either side"*; *"stay proposals"*, set apart from *"the rows
re-marked"*) and form (b)'s own condition (*"A row the record places "as proposed""*) leave no line for these rows. What
is put to the user is the ratification of that derivation.

### The wording the writing side proposes

- **At the rows:** no line from this record. Rows 36.5 (ii), 45.14 (i) and 45.15 (i) each keep their proposed
  RELOCATED, to *the uncertainty surface*, as a proposal, the proposed paragraph untouched. They are not counted in the
  ruled distribution. Their §10 entries stand as they are.
- **In §L.19's table** (dispatch line 1602): *"On the writing side's reading, **no line**. See the note below the
  table."* replaced with *"No line from this record"*, pointing to the ruling.
- **In the report:** no listing of its own (see the first weak point below).

### Weak points the writing side fixed before putting this

- **The report.** The working list's (lii) ends *"Whether the report lists the three, and under which heading, goes
  with A13"* (list line 2070). A13's list of sites does not name §L.19 point (1) (list lines 101–108; its sorting
  heading, lines 2464–2472) [checked], so that pointer does not reach this point. Read at the dispatch [checked]: Task 3 (a) lists in
  the report under *rows the act could not place* only a row-part an *Open* note leaves STOP-and-report, *"unless … a
  settlement the releasing sitting writes into that entry says otherwise"* (lines 5159–5161), and once point (1) points
  to the ruling, the three are not STOP-and-report. The full close that Task 5 appends to `records/cowork/handoff/cowork_away_returns.md`
  restates *"every §L entry's *Open* points"* as *"The points that are not this batch's"* (lines 5506–5521), so §L.19
  point (1), naming the three rows and pointing to the ruling, reaches the user there. No further listing is needed, and the check note's *rows the act could not place* sentence is overtaken. The
  list's A13 sentence is added to the *To do* below.
- **A place the list's *To do* did not name:** the check row's *"§L.19 point (1) (Rows 36.5 (ii), 45.14 (i), 45.15 (i),
  no line until settled)"* (line 20) [checked]. Added to the *To do* below for point (1) only. The same sentence's
  *"and point (3)'s report listing"* is not part of this site.
- **The list's own weak point, stated plainly** [checked at the reading file and the record]: Rows 45.14 (i) and 45.15
  (i) are proposed *"as Row 43.7 (ii)"*, and the same §2, at (c), moves Row 43.7 (ii) from its proposed RELOCATED to
  **HISTORICAL** (record lines 61–66), which Ruling 2 ratifies. So after the act, two of these proposals will name, as
  their model, a row placed otherwise. The record made that choice itself: it moved Row 43.7 (ii) and, in the same
  section, kept the three open *"at both sides"*. Writing a line would not mend it; it would add a ruled placement the
  record withholds.

### The currently decided method

Unchanged: the mass-and-status record's method [checked: Ruling 1, lines 96–98; Ruling 2, lines 127–129]. Every L3
rival of an L3 decision is published with both masses under distinct names: its mass given L2's principal reading (the
conditional) and its marginal mass over L2's published readings (the overall), with the unaccounted remainder
published. L3's mass and status rules are as L3-S32 to L3-S36 give them. Against the older documents, the confidence
contract's Class-M margins, max-normalised strengths and squashed composites are replaced, for L3, by the model's own
distribution.

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The other choice, a form (b) line **RELOCATED** *as proposed* at each row, would write a
ruled placement for rows the record says carry *"No ruling on either side"*, and would treat these three differently
from the rows the route ruling leaves as proposals. Towards the objective, neither choice changes the analysis, and with
§L.19 point (1) restated in the close, neither loses the rows. So the derivation and the wording above are put for
ratification, not as a menu. If you want a line at each row anyway, that is your overrule, and you would name its form.

**To do at release:** change §L.19's *Open* point (1) (dispatch lines 1623–1627), its check note's *"Point (1) stands for
the releasing sitting; until it is settled, Task 3 (a) gives the three rows no line and lists them in the report under
*rows the act could not place*"* (lines 1640–1641), and the check row's *"§L.19 point (1) (Rows 36.5 (ii), 45.14 (i),
45.15 (i), no line until settled)"* (line 20), for point (1), to point to the ruling; in the §L.19 table's line for the
three rows (line 1602), replace *"On the writing side's reading, **no line**. See the note below the table."* with *"No
line from this record"*, pointing to the ruling; change the working list's (lii) *To do at release* (its lines
2065–2070), its A13 sentence included, to point there; former wordings kept.

---

## Site 11 — Item (lvi): fourteen travelling row-parts the display record names and does not rule: a line following each lead row, or no line

*Added by the sitting booted on entry 741.*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles whether fourteen
row-parts of the reading file get a line. Nothing about what the analysis does.

### What the question is, from scratch

In the L3 reading file, some rows do not argue their own proposal but point to another row and say they go with it.
The writing side's word for these is *travelling rows*, and the row they point to is their *lead row*. Fourteen such
row-parts are at issue here. Each is proposed **ADOPTED — proposed**, which the reading file's §5 defines as *"a
PROPOSAL to the user that the outgoing content be added to the derived specification"* (lines 383–385). Each names its
lead [checked at the reading file, each row found by the row-heading search, its proposal line read]:

- *"travelling with Row 8.12"*: Rows 8.17 (line 8991), 8.29 (9193), 8.46 (9489), 8.63 claim (ii) (9756), 8.74 (9950)
  and 8.79 claim (i) (10043).
- *"travelling with Row 8.52 (ii)"*: Rows 8.53 (9597), 8.76 (9979), 8.82 (10086), 8.117 (10654) and 8.145 (11080).
- *"travelling with Row 7.63"*: Rows 7.69 (4263) and 7.70 claim (ii) (4279).
- *"as Row 7.108"*: Row 7.303 (7875).

The other claim of each of Rows 8.63, 8.79 and 7.70 is proposed **ADOPTED — carried** and is not part of this question.

**The record.** The display record (`cowork_rulings_2026_11_04_l3_display_sitting.md`), read whole [checked]. Its §2,
*"Carried, not decided by this ruling"*, lists seventeen travelling row-parts *"not named in the records that placed
their lead rows"*, these fourteen among them, and says (lines 53–56): *"On the reading file's travelling convention each
follows its lead row at the application act (the S38 ratification record's precedent for Row 3.15, line 39). Not ruled
here."* Its Ruling 1 places 25 other row-parts and none of these. The other three of the seventeen (Rows 8.48 (i), 8.89
and 8.91, lead Row 8.31 (i)) are named by a later ruling, which is the list's item (lvii); they are not part of this
site.

**What the dispatch writes now** [checked]. §L.25 lists the seventeen under *"Rows the record mentions and does not
place"* and writes *"No line from this record for any of them"* (dispatch lines 2134–2145). Its *Open* point (3) asks
whether the act lines them after their lead rows *"on the reading file's travelling convention"*, or they *"stay
proposals"* under the route record (lines 2158–2165). The check note says *"Points (1) and (3) stand."* (line 2171).
The check row leaves *"§L.25 points (1) and (3)"* to the releasing sitting (line 20). Point (1) is a different question
(which ADOPTED word §L.25's 25 placed rows take), and Ruling 9 of the part 2 ruling record governs it; it is not part of
this site.

### What the record already says

**No ruling the dispatch carries places the fourteen.** The display record says of them *"Not ruled here"*. Its surface's §1 and §10 say the
same [relayed from the list (lvi), lines 2283–2285; the surface not opened by this sitting]. A search of the whole
dispatch for the fourteen row numbers [checked] meets them only at §L.25 (lines 2135–2137 and 2148–2149), at Row 8.76 in
§L.13 (lines 1038, 1042 and 1071, each listing the row as not of that record's population or *"for a later surface"*),
at Row 8.63 in §L.15 (lines 1191 and 1202–1203, *"Rows the record mentions and does not place"*), and at the check row
(line 20). None of those places a row, so no record gives any of the fourteen a line, and form (b)'s two-record rule
(Ruling 3) does not arise.

**"Stay proposals" is what the route ruling does with rows no ruling reaches.** The route record's §2 step 1 ends *"Rows
no family reaches stay proposals."* (line 58), and step 2 has the application act re-mark *"the ruled rows"* (line 59)
[checked]. The dispatch's ruling ledger reads it: *"So a row no record names gets NO line."* (lines 101–102) [checked].
Task 3 (a) gives no line from a record to a row-part listed under *"Rows the record mentions and does not place"*
(dispatch lines 5157–5159) [checked], which is where §L.25 lists these.

**The "travelling convention" is not written in the reading file.** The reading file's §5 and the two reading rules at
the head of its §6 (lines 366–444) [checked] state no rule that a travelling row follows its lead. *"travelling with"*
is wording inside each row's proposal. The display record's *"On the reading file's travelling convention"* names a
rule that is not stated there.

**In the two cases read here where a ruling reached a travelling row, it named the row.** The S38 ratification record's ratified text names Row
3.15 itself: *"Rows 3.5(ii) and 3.15 as key-areas Ruling 2 decides them (decided against; 3.15 by travel with 3.5(ii),
this side's derivation)"* (its lines 39–40) [checked]. The key-areas record places Rows 3.4 and 8.75, each
*"travelling"*, by number (as §L.13 quotes it at dispatch lines 1027–1029 [checked at the dispatch; the key-areas
record relayed, not opened]). The display record cites the S38 precedent but places nothing itself.

**With no line, each row still reads true.** Each row's proposal is ADOPTED — proposed, a proposal to the user, and it
names its lead, so the reading file still says where the row is meant to go. Nothing at the row goes false.

Applying D-599: the display record's own words (*"Not ruled here"*), the route ruling (*"Rows no family reaches stay
proposals"*), and form (b)'s template, which needs a record and a ruling number to write (`*RULED DISPOSITION (<record
file>, Ruling N).*`, dispatch line 156 [relayed from site 10; that line not read by this sitting]), leave no line for these rows: there is no ruling to name.
This is the handling Ruling 12 ratified for rows a ruling leaves as proposals, and Ruling 11 for held rows. What is put
to the user is the ratification of that derivation.

### The wording the writing side proposes

- **At the rows:** no line from the display record. Rows 8.17, 8.29, 8.46, 8.63 (ii), 8.74, 8.79 (i), 8.53, 8.76, 8.82,
  8.117, 8.145, 7.69, 7.70 (ii) and 7.303 each keep their proposed ADOPTED — proposed, as a proposal, the proposed
  paragraph untouched. They are not counted in the ruled distribution.
- **In §L.25:** the sentence *"No line from this record for any of them"* (dispatch line 2145) stands. *Open* point (3)
  points to the ruling for the fourteen, and to §L.53's *Open* point (1) for the other three.
- **In the report:** no listing of its own. Once point (3) points to the ruling, the fourteen are not STOP-and-report, so
  Task 3 (a)'s listing under *rows the act could not place* (dispatch lines 5159–5161) does not reach them. The full
  close restates every §L entry's *Open* points as *"The points that are not this batch's"* (lines 5518–5521), so §L.25
  point (3), naming the fourteen and pointing to the ruling, reaches the user there.

### Weak points the writing side fixed before putting this

- **Two places the list's *To do* did not name** [checked]: the check note's *"Points (1) and (3) stand."* (dispatch
  line 2171) and the check row's *"§L.25 points (1) and (3)"* (line 20). Both are added to the *To do* below, for point
  (3) only.
- **The report.** The list's (lvi) says nothing of the report. Answered above.

### The weak point, stated by the working list

The display record and its surface both expect these rows to follow their leads at the application act. If the user
reads that expectation, with the S38 precedent, as enough to line them, each line would take its word from its lead.
Read at the dispatch [checked]: the leads 8.12 and 7.108 each take an ADOPTED word whose kind is still read at the row
under Ruling 9 (§L.13's table, line 1033; §L.5's, line 558). The leads 8.52 (ii) and 7.63 each get two lines, the phrase
half **ADOPTED — carried (L3-S8)** and the tonality half **UNPLACED**, because the key-areas record does not reach them
(§L.3, line 402; §L.13, lines 1045–1048; §L.55, line 4844). So for the seven rows travelling with 8.52 (ii) and 7.63,
*"follows its lead row"* would not give one word, and which half each follows would need saying. Such a line would also
have no ruling to name in form (b)'s template. With no line, neither problem arises.

### The currently decided method

Unchanged: the display record's method [checked: its lines 45–49]. L2 publishes the decided chord as a degree in its
tonality, with the tonality. L3 publishes structured facts read off it: the chord symbol, the figured bass as the full
figure, the harmonic rhythm, the cadence with its type at each phrase end, the phrase and section grouping, the key
areas, and the pivot re-expression with its flag. L3 publishes no tonic / subdominant / dominant summary and writes
nothing into the score. A display turns published facts into text.

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The other choice, a line at each row following its lead, would write a ruled disposition no
ruling gives (the record says *"Not ruled here"*). It would rest on a convention the reading file does not state, and
for seven of the fourteen it would need a further choice of half. Towards the objective, neither choice changes the
analysis. With §L.25 point (3) restated in the close and each proposal naming its lead, neither loses the rows. So the
derivation and the wording above are put for ratification, not as a menu. If you want a line at each row anyway, that
is your overrule, and you would name its form and, for the seven, which half.

**To do at release:** change §L.25's *Open* point (3) (dispatch lines 2158–2165) to point to the ruling for the
fourteen and to §L.53's *Open* point (1) for Rows 8.48 (i), 8.89 and 8.91; change the check note's *"Points (1) and (3)
stand."* (line 2171) and the check row's *"§L.25 points (1) and (3)"* (line 20), each for point (3), to point the same
way; the sentence *"No line from this record for any of them"* (line 2145) stands; change the working list's (lvi) *To
do at release* (its lines 2316–2318) to point to the ruling; former wordings kept.

---

## Site 12 — Item (lvii): Rows 8.48 (i), 8.89 and 8.91, which a ruling names as following their lead row: a QUARANTINED line following the lead, or no line

*Added by the sitting booted on entry 742.*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles whether three
row-parts of the reading file get a line, and which. Nothing about what the analysis does.

### What the question is, from scratch

As at site 11, a *travelling row* is a row of the L3 reading file that does not argue its own proposal but says it goes
with another row, its *lead row*. Three such row-parts are at issue here. Each is proposed **ADOPTED — proposed** and
names the same lead, Row 8.31 claim (i) [checked at the reading file, each row found by the row-heading search and read
by offset]:

- Row 8.48 claim (i), the open marks *"surfaced in the grouped view"*: *"**ADOPTED — proposed** — travelling with Row
  8.31 (i)"* (line 9524). Its claim (ii) is proposed ADOPTED — carried (L3-S38) and is not part of this question.
- Row 8.89, an open mark on a unit *"surfaced on the punctuation-span and key-area that contain that unit"*: the same
  (line 10207).
- Row 8.91, a span *"composed entirely of units carrying **no open mark** (that is the whole test — no confidence
  threshold is involved) is reported as fully resolved"*: the same, with a clause of its own, *"a unit reported fully
  resolved exactly when none of its spans carries the mark, no confidence threshold entering the test"* (lines
  10235–10236).

An *open mark* (the reading file also says *unresolved mark*) is the old design's flag on a place where the function
layer left its reading unresolved. Rows 8.89 and 8.91 carry the heading mark *WITHHELD — D-460* (lines 10197, 10225);
that mark is not touched here.

The lead, Row 8.31 (i), *"the function layer's unresolved marks pass through to the grouped output unchanged"*, was
proposed **ADOPTED — proposed** (line 9226). The record-placed rows ruling places it **QUARANTINED** instead.
QUARANTINED, in the reading file's §5, is for a statement of *"how the implementation currently works, or a measured
property of it"*, and the row writes *"the audit question in one sentence"* (lines 390–391): the question someone would
put to the built code.

**The record.** The record-placed rows record (`cowork_rulings_2026_11_08_l3_record_placed_rows_sitting.md`), read whole
[checked]. Its Ruling 1 (the user's word *"confirmed"*) says, inside its *As ruled* text (lines 34–37):

> Row 8.31 (i) — QUARANTINED, with the audit question "does any built code hand the function layer's open marks to a
> grouping step, and does that step pass them unchanged?", as the key-areas record §2c places it (…). Its travelling
> Rows 8.48 (i), 8.89 and 8.91 follow it at the application act (display ruling record §2, lines 53–56).

Its title and its §0 speak of *"six row-parts"* (lines 1 and 13); the three travelling rows are named as following the
sixth, not counted among the six.

**What the dispatch writes now** [checked]. §L.53's table lines the six (dispatch lines 4668–4673), and its check sum
reads 3 + 1 + 1 + 1 = 6 (line 4675). The three are listed under *"Rows the record mentions and does not place by its own
ruling"* (lines 4712–4714). Its *Open* point (1) asks whether the sentence *"settles §L.25's Open point (3) for these
three rows, or only restates the display record's carry"*, and leaves it to the releasing sitting (lines 4720–4723).
The check note says *"Point (1) is settled by no Task and stands."* (line 4734), and the check row leaves *"§L.53 point
(1)"* to the releasing sitting (line 20, found by a bounded search). Until it is settled, §L.25 makes them
STOP-and-report: *"Until (1) to (3) are settled, those rows and additions are STOP-and-report."* (line 2165). Ruling 13
already points §L.25's *Open* point (3) for these three to §L.53's *Open* point (1).

### What the record already says

**A ruling names these three by number, unlike the fourteen of site 11.** Site 11's fourteen were named only by the
display record, which says *"Not ruled here"* (display record line 56) [checked]; no ruling the dispatch carries placed
them, so they stay proposals (Ruling 13). These three are named again, later, inside the ratified text of record-placed
rows Ruling 1, with what the act does with them: *"follow it at the application act"*. The surface that was ratified
proposed the same (`ratification_surfaces/cowork_l3_record_placed_rows_surface_2026_11_08.md`, §4, lines 127–128: *"its
travelling Rows 8.48 (i), 8.89 and 8.91 following it at the application act"*) [checked]. So the route ruling's *"Rows
no family reaches stay proposals."*, which Ruling 13 applied to the fourteen, does not reach these three: a ruling
reaches them. That the sentence cites the display record, which ruled nothing, does not undo this: the later ruling took
the carry into its own ratified text.

**What "follow it" gives: QUARANTINED, with the lead's audit question.** The same Ruling 1 uses travel in that sense in
its first item: *"Rows 21.27, 21.28, 21.29 — QUARANTINED, travelling with L2's Row 23.72 and its audit question"*
(record line 27) [checked]: the travelling rows take the lead's word and its question. Each of the three proposals takes
its word from its lead (*"travelling with Row 8.31 (i)"*). The lead's ADOPTED — proposed is replaced by a ruled
QUARANTINED; writing ADOPTED — proposed for the three would keep for them the proposal the ruling replaced for their
lead. The three are not re-judged against §5 here.

**One record gives them a line.** A search of the whole dispatch for the three row numbers [checked; *"8.48"*, *"8.89"*
and *"8.91"* not preceded by a digit or a point] meets them at §L.25 (lines 2136, 2140) and §L.53 (lines 4683, 4706,
4709, 4712, 4713, 4720), and at no other line of the dispatch. §L.25 gives them no line (*"No line from this record for
any of them"*, line 2145). So form (b)'s two-record rule (Ruling 3) is not met at these rows. The lead, Row 8.31 (i),
has a recorded line at §L.13 (line 1035) and a ruled line at §L.53 (line 4673), both QUARANTINED; the three carry
§L.53's only.

**The line's shape.** Form (b) (dispatch lines 155–160) [checked]: `*RULED DISPOSITION (<record file>, Ruling N).*
**<disposition>** — <placement in the record's words>.`; a split row's line names its claim, `(i) **…**`. Each row is
proposed ADOPTED — proposed, not QUARANTINED, so the line does not say *as proposed*; Ruling 9's paragraph is for rows a
record places ADOPTED and does not reach these. §L.53's own line for the lead quotes the audit question whole (line
4673), and the three do the same.

**The audit list follows by Ruling 7.** The reading file's §11 has a block for member 8, `cowork_layer6_grouping_design.md`
(lines 80151–80176), and the block as read carries no entry for Row 8.31, 8.48, 8.89 or 8.91 [checked, §11 read by
offset from its heading at line 79980]. Task 3 (c) item 7 (Ruling 7) adds to §11, under its member's heading, every
row-part a §L entry places QUARANTINED out of another proposal that §11 does not already carry. So, once lined, the
three (and their lead) are added there by that item's own rule. Nothing further is decided here.

Applying D-599: the ruling's own sentence, its first item's use of *"travelling with … and its audit question"*, and
each proposal's *"travelling with Row 8.31 (i)"* leave one line for each row. What is put to the user is the
ratification of that derivation.

### The wording the writing side proposes (the working list's item (lvii))

- **At the rows:** each of the three gets ONE form (b) line beneath its `*PROPOSED DISPOSITION.*` paragraph, the
  proposed paragraph kept; for Row 8.48 the line names claim (i) only and begins `(i) **QUARANTINED**`. Not *as
  proposed*:

> `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_record_placed_rows_sitting.md, Ruling 1).* **QUARANTINED** — following Row 8.31 (i): "Its travelling Rows 8.48 (i), 8.89 and 8.91 follow it at the application act"; audit question: "does any built code hand the function layer's open marks to a grouping step, and does that step pass them unchanged?"`

- **In §L.53:** a line for the three beneath its table (after line 4673) with the words above; the check sum (line
  4675) reads 3 + 1 + 1 + 1 = 6 row-parts the ruling places, the record's *"six row-parts"*, plus the 3 travelling rows
  it names as following Row 8.31 (i), 9 lines in all; the paragraph *"Rows the record mentions and does not place by its
  own ruling"* (lines 4712–4714) points to the ruling.
- **In the report:** nothing of its own. With §L.53's *Open* point (1) pointing to the ruling, the three are not
  STOP-and-report; their §11 additions are listed under *audit questions added* by Task 3 (c) item 7.

### Weak points the writing side fixed before putting this

- **Two places the list's *To do* did not name** [checked]: §L.53's check note *"Point (1) is settled by no Task and
  stands."* (dispatch line 4734) and the check row's *"Left for the releasing sitting: §L.53 point (1)."* (line 20).
  Both added to the *To do* below.
- **The audit list.** The list's (lvii) does not name §11. Answered above: Ruling 7 reaches the three.
- **The check sum.** The list's *"6 + 3 = 9 lines"* is written so as to keep the record's own *"six row-parts"*.

### The weak points, stated by the working list

(a) **Does the sentence place the three, or only restate the display record's carry?** The ruling's title and §0 count
six; the three are named as following the sixth. And the carry it cites rests, through the display record, on *"the
reading file's travelling convention"*, which site 11 found is not stated in the reading file's §5 or at the head of its
§6 [relayed from site 11; those lines not read by this sitting]. If the user reads the sentence as a restatement and not
a placement, the three stay proposals, ADOPTED — proposed, as at site 11, and §L.53's *Open* point (1) points to the
ruling saying so.

(b) **Row 8.91 and D-460.** Row 8.91's outgoing sentence is the content of D-460, LIVE at the register: *"A group counts
as fully resolved exactly when no unit in it carries an unresolved mark — no confidence threshold enters the test"*
(`DECISIONS.md` line 463) [checked]. QUARANTINED is §5's word for a statement of how the implementation currently works.
A QUARANTINED line places the row; it does not change D-460's register status, which is not decided here. On the
writing side's reading, the audit question (whether marks are handed on and passed unchanged) fits Row 8.91's
resolved-test loosely.

### The currently decided method

Unchanged: the record's method [checked: its lines 45–48]. L3 publishes, per bar and per phrase unit, L2's boundaries
with their metric strength and change classes; L2 reads none of it; L3 publishes no separate root-and-quality grouping;
a key area is a maximal run of spans sharing one tonality in L2's principal reading; *"No L3 fact may change an L2 fact,
a rival or a mass"*; L2 publishes no "uncertain" flag.

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The other reading, no line, would treat a sentence inside a ratified ruling, naming the
three and saying what the act does with them, as placing nothing; and it would keep for the three the proposal the
ruling replaced for their lead. Towards the objective, neither choice changes the analysis: QUARANTINED sends the three
to an audit question about built code, and §11 then lists them; with no line they would stay proposals, findable through
§L.53's *Open* point. So the derivation and the line above are put for ratification, not as a menu. If you read the
sentence as a restatement only, that is your overrule, and the three stay proposals as at site 11.

**To do at release:** change §L.53's *Open* point (1) (dispatch lines 4720–4723), its check note's *"Point (1) is settled
by no Task and stands."* (line 4734) and the check row's *"Left for the releasing sitting: §L.53 point (1)."* (line 20)
to point to the ruling; add beneath §L.53's table (after line 4673) the line for the three; rewrite the check sum (line
4675) as above; point the paragraph *"Rows the record mentions and does not place by its own ruling"* (lines 4712–4714)
to the ruling; change the working list's (lvii) *To do at release* (its lines 2382–2386) to point to the ruling;
§L.25's *Open* point (3) is pointed to §L.53 (1) for the three by Ruling 13's to-do; former wordings kept.

---

## Site 13 — Item (lviii): Row 46.43, which a ruling says "travels with" Row 38.22 (ii)'s behaviour half: a line per part placed, or a STOP-and-report

*Added by the sitting booted on entry 743.*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles which lines one
row of the reading file gets. Nothing about what the analysis does.

### What the question is, from scratch

Row 46.43 of the L3 reading file is one bold sentence from the old design's *Crosscutting concepts* section:
*"**Style behavior is the consumer's.**"* It is proposed **UNPLACED**, *"read as at Row 44.1: the consumer is the older
stack's recognition consumer, whose recognition no charter of `FRAMEWORK.md` §5 names"* (reading file lines
64249–64259) [checked, the row found by the row-heading search and read by offset]. The sentence is not split into
numbered claims at §6.

The sentence leads a bullet, Row 46.44, which names the behaviour: *"the **preset selects** the active subset, the
**style weighting** (a graded prior — not a hard filter, since styles blend) and the **threshold** are the consumer's,
and **style detection** is a future classifier"* (lines 64263–64271) [checked].

A neighbouring row says the same thing at more length. Row 38.22 claim (ii): *"the genre *labels* live in the component
while genre-aware *behavior* (selection, weights, detection) lives at the consumer"*, proposed **UNPLACED** (lines
46970–46986) [checked]. The *component* is the old design's catalog of named progressions; the *consumer* is the code
that uses it.

**The record.** The idiom-tags part 1 record (`cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md`), read
whole [checked]. Its Ruling 1 (the user's word *"ratified"*) ratifies *"the splits of §3.3 … as written"* (lines 32–33)
and tables, under §3.3 (lines 43–46):

> 38.22 (ii) — the labels ADOPTED — proposed, selection decided against as above, weights RELOCATED to L2 with key
> Ruling 2's candidate, detection waiting on the open question the L2 tail-style-and-idiom record §1 holds; 46.43 —
> travels with 38.22 (ii)'s behaviour half;

*"As above"* points to the line before, Row 46.44 (i): *"the preset selecting the active subset decided against in so
far as it selects the catalog L3 reads"* (line 44). The ratified surface
(`ratification_surfaces/cowork_l3_catalog_idiom_tags_part1_surface_2026_11_07.md`, §3.3) [checked, lines 169–187] gives
Row 46.43's row as *"the whole sentence | travels with 38.22 (ii)'s behaviour half, its three parts placed as there"*
(line 181), and 38.22 (ii)'s three behaviour parts as *selection* **decided against in so far as it selects the catalog
L3 reads**, *weights* **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.***, travelling with key
Ruling 2's candidate, and *detection* waiting on that open question (lines 178–180).

**What the dispatch writes now** [checked]. §L.36's table gives Row 38.22 (ii) one line per part placed (HISTORICAL for
selection, RELOCATED for weights) and *"No line for "detection …""* (dispatch line 3073). For Row 46.43 it writes *"No
disposition word named by the record"* and sends it to *Open* point (3) (line 3074), which reads: *"which line or lines
Row 46.43 gets is not stated by the record. STOP-and-report until fixed."* (lines 3123–3124). The check note adds that
the surface gives the three parts *"placed as there"*, but *"which lines that gives a row of one sentence is still not
stated, so the point stands"* (lines 3137–3140); the check row says the same and leaves §L.36 points (1) to (4) to the
releasing sitting (line 20, found by a bounded search).

### What the record already says

**A ruling names the row by number, and says how it follows.** As at site 12, the route ruling's *"Rows no family
reaches stay proposals."* does not reach a row that a ratified text names and places. Ruling 14 ratified a derivation reading
travel, in the record-placed rows ruling, as taking the lead's word. Here the lead is placed part by part, and the ratified surface
says so in terms: *"its three parts placed as there"*. So Row 46.43 takes Row 38.22 (ii)'s three behaviour placements,
one per part.

**Where the three parts come from.** Row 46.43's sentence does not name selection, weights or detection. They come from
38.22 (ii)'s parenthesis, carried over by the recognition part 1 surface's finding that 46.43 is *"the same claim as Row
38.22 (ii)'s second half"*, as the idiom-tags surface quotes it (line 181) [relayed: the idiom-tags surface marks it
checked there; the recognition part 1 surface not read by this sitting]. Row 46.44, the bullet the sentence leads, names
the three (the preset's selection, the style weighting, style detection), with the threshold beside the weighting
[checked at the row].

**What each part gets.**

- *Selection:* the record's *"decided against"*, so **HISTORICAL** by form (b-H) (dispatch lines 162–164: where a record
  decides against part of a row, the line names that part). Form (b-H)'s search would not find this part at Row 46.43:
  the record's words for 46.43 (line 46) do not say *"decided against"*; the hit at line 45 is 38.22 (ii)'s. So the line
  is written from this derivation.
- *Weights:* **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.***, the record's *"weights
  RELOCATED to L2 with key Ruling 2's candidate"* (line 45). The heading is the surface's (line 179); Row 46.44 (ii) is
  proposed RELOCATED to the same heading (lines 64278–64280) [checked].
- *Detection:* no line, as 38.22 (ii)'s detection part gets none (dispatch line 3073). The part keeps the row's proposed
  UNPLACED. §L.36's *Open* points (1) to (5) raise none for 38.22 (ii)'s detection part, and none is needed for
  46.43's.

**Not *as proposed*.** The row is proposed UNPLACED, so neither line says *as proposed* (Ruling 9's paragraph is for
rows a record places ADOPTED and does not reach these lines).

**One record gives the row lines.** A search of the whole dispatch for *"46.43"* not preceded by a digit or a point
[checked] meets it at the check row (line 20), §L.31's table (line 2657: *"No line from this record."*, the record moving
the row *"to the idiom-tag surface"*), §L.31's note (line 2680), and §L.36 (lines 3074, 3082, 3095, 3108, 3123–3124,
3138–3139), and at no other line of the dispatch. Form (b)'s two-record rule as ruled (Ruling 3) says *"A part a record
says it moves to another record gets no line from the record that moves it"*; so only the idiom-tags record gives the
row lines, and the rule is not met. One record giving one row lines with different words on different parts is what
§L.36's table already does for 38.22 (ii) itself (line 3073).

**The transfer list follows by Task 3 (c) item 5.** The weights part is placed RELOCATED out of UNPLACED. Item 5
(dispatch lines 5204–5209) [checked] appends every such row-part under its destination heading in §10 unless §10
already carries it, checked by row number first. Whether §10 carries Row 46.43 was not read by this sitting (no search
over the reading file was run); item 5 handles both cases. Nothing further is decided here.

Applying D-599: the ratified *"its three parts placed as there"*, read with 38.22 (ii)'s ruled placements, leaves two
lines and one part with no line. What is put to the user is the ratification of that derivation.

### The wording the writing side proposes

- **At the row:** TWO form (b) lines beneath Row 46.43's `*PROPOSED DISPOSITION.*` paragraph, the proposed paragraph
  kept, each naming its part in 38.22 (ii)'s word (the row has no numbered claims, so the part is named in words):

> `*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (selection) **HISTORICAL** — "46.43 — travels with 38.22 (ii)'s behaviour half"; as there, "selection decided against as above", that is, "decided against in so far as it selects the catalog L3 reads".`

> `*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md, Ruling 1).* (weights) **RELOCATED** — to ***L2 — The tonal reading. The one entangled decision.***: "46.43 — travels with 38.22 (ii)'s behaviour half"; as there, "weights RELOCATED to L2 with key Ruling 2's candidate".`

- **No line for the detection part**, which keeps the row's proposed UNPLACED.
- **In §L.36's table** (dispatch line 3074): the two lines above, with *"No line for the detection part"*.
- **In the report:** nothing of its own. With §L.36's *Open* point (3) pointing to the ruling, the row is not
  STOP-and-report.

### Weak points the writing side fixed before putting this

- **The selection line's quotation.** The working list's proposed line quoted *"decided against in so far as it selects
  the catalog L3 reads"* as the record's words for 38.22 (ii). The record's words for that part are *"selection decided
  against as above"* (line 45); the longer phrase is the record's line for Row 46.44 (i) (line 44), which *"as above"*
  points to. The line now quotes both, in that order.
- **Ruling 3 since the list was written.** The list judged the two-record rule *"by its present wording or by (xlix)'s"*.
  Ruling 3 has since ruled (xlix)'s wording; its sentence on moved parts is the one that applies, and it is quoted above.
- **The check row.** The list's (lviii) *To do* did not name the check row's *"Left for the releasing sitting: §L.36
  points (1) to (4)"* (line 20). Added to the *To do* below, for point (3).

### The weak points, stated by the working list

(a) **One sentence, three parts.** Splitting the sentence uses 38.22 (ii)'s parenthesis, carried over by the
recognition part 1 surface's *"the same claim"*, which this sitting did not read. If the user reads *"travels with"* as
giving the whole sentence one word, no one word exists, since the three parts carry three different placements; the row
then stays a STOP-and-report, as §L.36's *Open* point (3) has it now.

(b) **The sentence names none of the three.** The HISTORICAL part decides against it only in so far as its *"style
behavior"* includes a preset choosing the catalog L3 reads; Row 46.44, the bullet the sentence leads, says it does
(*"the **preset selects** the active subset"*) [checked at the row].

(c) **Detection.** Row 46.44 (iii), *"style detection is a future classifier"*, is proposed HISTORICAL at §6, and the
surface told the user he could place 38.22 (ii)'s detection there (its line 180). Ruling 1 accepted the surface's
proposals *"as proposed, none changed"* (record line 33), so the detection part waits and gets no line here.

### The currently decided method

Unchanged: the record's method [checked: its lines 54–59]. L2 decides key and chord together; its progression term is a
table of chord-to-chord pairs; DP-O stays open, the catalog term among its unmeasured candidates. L3 publishes the
cadence at each phrase end with its type, the phrase and section grouping, the chord symbol, the figured bass, the
harmonic rhythm, and the catalog matches once the application act amends `FRAMEWORK.md`. *"The matcher is the same for
every idiom; no preset chooses the catalog; L3's method uses no tag."*

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The other reading, one word for the whole sentence, finds no word that fits all three parts,
so it leaves the row a STOP-and-report and the ratified *"its three parts placed as there"* unapplied. Towards the
objective, neither choice changes the analysis: the lines record decisions already taken for Row 38.22 (ii) (no preset
chooses the catalog L3 reads; style weights belong with L2's candidate), and the STOP-and-report would leave the same
content findable at §L.36. So the derivation and the two lines above are put for ratification, not as a menu. If you
read *"travels with"* as one word for the whole row, that is your overrule, and the row stays a STOP-and-report.

**To do at release:** change §L.36's *Open* point (3) (dispatch lines 3123–3124), its check note's sentence on point
(3) (lines 3137–3140) and the check row's *"Left for the releasing sitting: §L.36 points (1) to (4)"* (line 20), for
point (3), to point to the ruling; write the two lines into the §L.36 table's line for Row 46.43 (line 3074), with *"No
line for the detection part"*; change the working list's (lviii) *To do at release* (its lines 2460–2462) to point to the
ruling; former wordings kept.

---

## Site 14 — Group 1, rows a ruling leaves as proposals (no line; each row keeps its proposal): items (lxv), Rows 36.41 and 36.118, (lxvi), Row 10.123, (lxvii), Rows 7.97 (ii) and 7.118, (lxxix), Row 44.19 (i) and (ii), and (lxxxii), seven further row-parts of member 23 with Rows 23.1 and 23.44

*Added by the sitting booted on entry 744.* A group site, on the user's ruling of 2026-11-11 (*"As many as will fit in
sessions."*, entry 744 §2 item 3): items of one kind go in one site, one after another, and each item's choice question
is put on its own. Group 1 is the items whose rows no ruling places, so that each row gets no line, keeps its proposal,
and §10 stays as it stands: the kind of Rulings 12 and 13. Its items, sorted from the list's headings alone: (lxv),
(lxvi), (lxvii), (lxxix) and (lxxxii). The sitting booted on entry 744 added (lxv), the sitting booted on entry 745
added (lxvi), the sitting booted on entry 746 added (lxvii), the sitting booted on entry 747 added (lxxix), and the
sitting booted on entry 748 added (lxxxii); with it, group 1 is complete. *(Former wording, kept: "… and the sitting
booted on entry 747 added (lxxix); the others are named in "What this file does not yet carry", for later sittings to
add here." Former heading, kept: "… and (lxxix), Row 44.19 (i) and (ii)".)* *(Former wording, kept: "… and
the sitting booted on entry 746 added (lxvii); the others are named …". Former heading, kept: "… and (lxvii), Rows 7.97
(ii) and 7.118".)* *(Former wording, kept: "The sitting booted on entry 744 added (lxv), and the
sitting booted on entry 745 added (lxvi); the others are named …". Former heading, kept: "… and (lxvi), Row 10.123".)*
*(Former wording, kept: "This sitting adds (lxv); the others are named in "What this file does not yet carry", for later sittings
to add here." Former heading, kept: "… item (lxv), Rows 36.41 and 36.118".)*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles whether two rows
of the reading file get a line, and how the dispatch carries them to the user. Nothing about what the analysis does.

### Item (lxv) — Rows 36.41 and 36.118

#### What the question is, from scratch

Rows 36.41 and 36.118 of the L3 reading file come from the old phrase-boundary design. Row 36.41 states the formula by
which each cue profile's strength at a note onset is computed, the *"local-change rule"*: for a value `x` with a
neighbour on each side, a left and a right change-ratio, and the strength `x · (left + right)` (reading file lines
40721–40728) [checked]. Row 36.118 is the same rule's glossary entry, which adds that each profile is then scaled so its
largest value is 1 (*"max-normalised to [0,1]"*) (lines 42239–42244) [checked]. Each is one claim; the derivation is
silent on each; each is proposed **RELOCATED** — to ***L1 — Change points, candidates and notated evidence***, *"as Rows
10.8 (ii) and 20.23 placed the boundary-strength profile and the primitive"* (lines 40734–40735, 42250–42251) [checked].
L1 is the layer that works out, from the notation, where something changes.

**The record.** The phrase-end evidence record (`cowork_rulings_2026_11_08_l3_phrase_end_evidence_family_sitting.md`,
its sitting booted on entry 587), read whole [checked]. Its Ruling 1 places six other row-parts. Its §2, *"Carried, not
decided by this ruling"*, says (lines 59–61):

> **Rows 36.41 and 36.118** are proposed at the L3 reading file as RELOCATED to *L1*. On this side's reading that does
> not fit L0/L1 Ruling 49, which places the local-change transform at the consumer. They are not this family's. They go
> to the application act with the surface's §3B note.

The note (`ratification_surfaces/cowork_l3_phrase_end_evidence_family_surface_2026_11_08.md`, lines 222–227) [checked]
says the same and adds that they go to the act *"for the row-by-row re-reading the route ruling gives that act **[this
side's reading; not tested at Rows 10.8 (ii) and 20.23, which were not opened]**"*. L0/L1 Ruling 49 was not read by this
sitting; what it says is relayed from the record and the surface (line 215: *"one model family among those the methods
catalog ranks, a research choice the picker owns"*).

**What the dispatch writes now** [checked]. §L.46 says no ruling places the two, so under the route ruling they get no
line, and sends them to *Open* point (2) (dispatch lines 4037–4041), which reads: *"Rows 36.41 and 36.118: what the act
does with "the surface's §3B note" is not stated by the record, and the note was not read by the sitting that wrote this
entry; at most the report lists the two rows and the record's sentence for the user."* (lines 4044–4046). The check note
read the §3B note, found that it *"names no line to write"*, and left the point standing (lines 4054–4061); the check row
leaves *"§L.46 points (1) to (3)"* to the releasing sitting (line 20, found by a bounded search).

#### What the record already says

**No line: no ruling places them.** The record says *"They are not this family's"* and places neither. A search of the
whole dispatch for *"36.41"* and *"36.118"*, not preceded by a digit or a point, meets them at lines 4027, 4037, 4044 and
4057, all within §L.46's text as read (lines 4020–4067), and at no other line of the dispatch [checked]. So the route
ruling governs: *"Rows no family reaches stay proposals."* (route record line 58) [checked], which the dispatch's ledger
reads *"So a row no record names gets NO line."* (lines 101–102) [checked]. This is Ruling 12's case: a ruling names rows
and does not place them, so they stay proposals, and with no line each row still reads true.

**The note orders nothing the act can write.** Its *"row-by-row re-reading the route ruling gives that act"* is marked by
its own writer as that side's reading. The route record's step 2 has the act re-mark *"the ruled rows"* (lines 59–60)
[checked]; step 1 leaves the rest proposals. The note names no word and no line.

**§10 needs nothing.** Both rows already stand on the reading file's §10 transfer list, under the L1 heading (line
79008), in the entry at lines 79041–79046, with 21 other row-parts of the graded boundary-strength profile, marked *"As
Rows 10.8 (ii) and 20.23"* [checked]. Task 3 (c) item 5 reaches only row-parts a §L entry places RELOCATED (dispatch
lines 5204–5209) [checked], and item 6 only rows lined from §L.21 to §L.24 (lines 5210–5216) [checked]; neither reaches
these two. With no line, each row's proposal and its §10 entry agree.

**The open question reaches the user through the close, as at Rulings 12 and 13.** The record names a gap between the
rows' proposal and Ruling 49 and decides nothing about it. Task 5's full close restates *"every §L entry's *Open*
points"* under *"The points that are not this batch's"* (dispatch lines 5518–5521) [checked]. So §L.46's *Open* point
(2), rewritten to name the two rows, the record's sentence and the §3B note and to point to the ruling, reaches the user
there, as Ruling 12 has §L.19's point (1) do and Ruling 13 §L.25's point (3).

**The proposal's precedents are proposals.** Rows 10.8 (ii) and 20.23 are themselves proposed RELOCATED to L1 (lines
14599–14602; 26005–26007) [checked]. That the dispatch meets them only at line 4056, quoting the note, is relayed from the
list's (lxv); this sitting's search was for 36.41 and 36.118 only. Whether they, and the other row-parts of the §10
entry, fit Rulings 48 and 49 is not this site's and is not judged here.

**Two records.** No §L entry gives either row a line, so form (b)'s two-record rule (Ruling 3) does not arise.

Applying D-599: the route ruling and Ruling 12 leave the rows with no line, as proposals; the record's sentence reaches
the user through §L.46's *Open* point (2) and the close. What is put to the user is the ratification of that derivation.

#### The wording the writing side proposes

- **At the rows:** no line from this record. Rows 36.41 and 36.118 each keep their proposed **RELOCATED** to ***L1 —
  Change points, candidates and notated evidence***, as a proposal, the proposed paragraph untouched; they are not
  counted in the ruled distribution; their §10 entry (reading file lines 79041–79046) stands as it is.
- **§L.46's *Open* point (2)** is rewritten to point to the ruling, naming the two rows and quoting the record's sentence
  (record lines 59–61) and the §3B note's clause, so that Task 5's restatement under *"The points that are not this
  batch's"* carries them to the user.
- **In the report:** no listing of its own. The rows are not STOP-and-report, so Task 3 (a)'s *rows the act could not
  place* does not reach them.

#### Weak points the writing side fixed before putting this

- **The list's extra naming in Task 5.** The list's (lxv) also proposed naming §L.46's point (2), the rows, the sentence
  and the note inside Task 5's bullet, *"so that pointing §L.46's Open point (2) here does not drop it"*. Rulings 12 and
  13, ruled since, hold that an *Open* point pointing to its ruling is still restated by that bullet, which restates every
  §L entry's *Open* points. The separate naming would repeat it and set this item apart from those rulings, so it is
  dropped; the rewritten point (2) carries the reach.
- **The check row.** The list's (lxv) *To do* did not name the check row's *"Left for the releasing sitting: §L.46 points
  (1) to (3)"* (line 20). Added to the *To do* below, for point (2).

#### The weak point, stated by the working list

That the record's *"They go to the application act with the surface's §3B note"* asks for the rows to be carried to the
act, and not for the act to re-mark them, is the writing side's reading, resting on the route ruling's step 2. If you read
it as an order to re-mark them, the act still has no word: RELOCATED to L1 as proposed, which the record reads as not
fitting Ruling 49, or a placement at L3 like Row 56.24's, which no ruling gives these two. The word would then be a
question for you. Documentation only either way.

#### The currently decided method

Unchanged: the record's method [checked: its lines 45–53]. L2 decides key and chord together and publishes the chord as
a degree in its tonality; L3 publishes facts read off it. L3 decides where phrases end as a weighed choice over every
candidate position; the notated flags and the re-homed strength profile enter as evidence with fitted weights, and no
item forces or forbids a phrase end. No preset or style label reaches L2. As the record and its surface relay L0/L1 Ruling
49 [relayed], the local-change transform is the consumer's, a research choice the picker owns.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. A line needs a ruling to name and a word to write, and the record gives neither. Towards the
objective, no line changes nothing in the analysis and drops none of what the record says: the rows keep their proposal,
§10 keeps them, and the open question of where the local-change rule belongs reaches you at the close. So the derivation
is put for ratification, not as a menu. If you read the record's sentence as an order to re-mark the rows, that is your
overrule, and the word for them becomes a question of its own.

**To do at release:** change §L.46's *Open* point (2) (dispatch lines 4044–4046), the check note's sentences on point
(2) (lines 4054–4057) and its *"Points (1) to (3) stand."* (line 4061), and the check row's *"Left for the releasing
sitting: §L.46 points (1) to (3)"* (line 20), each for point (2), to point to the ruling; change the working list's (lxv)
*To do at release* (its lines 2865–2869) to point to the ruling; former wordings kept.

### Item (lxvi) — Row 10.123

*Added by the sitting booted on entry 745.*

#### What the question is, from scratch

Row 10.123 of the L3 reading file comes from the old chord-layer design. Its one claim is *"Only short figuration
within the window is named here; a phrase-length prolongation of one harmony is a reduction judgment beyond this
layer."* (reading file lines 16298–16299) [checked]. In plain words: the chord layer names only brief decoration inside
its window; judging that one harmony is drawn out over a whole phrase is a judgment of reduction, which the old design
put outside the layer. No derived statement speaks to it; the derivation is silent on it; it is proposed **RELOCATED** —
to ***L2 — The tonal reading. The one entangled decision.*** (lines 16301–16305) [checked]. L2 is the layer that decides
key and chord together.

**The record.** The prolongational-reduction record (`cowork_rulings_2026_11_08_l3_prolongational_reduction_group_sitting.md`,
its sitting booted on entry 588), read whole [checked]. Its Ruling 1 places four other rows: Row 7.47 RELOCATED to L2,
and Rows 7.48 (i), 7.294 (v) and 7.331 held UNPLACED, travelling with DP-O (lines 37–41). DP-O is the framework's open
question whether it commits to a hierarchical reading of harmony (lines 18–19). Its §2, *"Carried for the application
act, not decided here"*, says (lines 57–59):

> **L3 Row 10.123** (*"a phrase-length prolongation of one harmony is a reduction judgment beyond this layer"*, line
> 16296) is proposed RELOCATED to L2. Its L2 twin, Row 6.113, is held with DP-O by the same L2 ruling. On this side's
> reading, the proposal does not fit that ruling. It is on no family's list.

The L2 ruling is L2 score-decomposition Ruling 4, named at the record's line 20 [checked]
(`records/cowork/rulings/cowork_rulings_2026_10_07_l2_score_decomposition_sitting.md`; the user's word *"Confirmed"*,
its line 92 [checked]), which reads *"**Held UNPLACED, travelling with DP-O (4):** Rows 5.53(i), 5.303(v), 5.342, 6.113 —
not placed, and not lost"* (its lines 105–106) [checked]. The record's surface
(`ratification_surfaces/cowork_l3_prolongational_reduction_group_surface_2026_11_08.md`), at its §5 (lines 198–201)
[checked], says the same and adds that the row *"goes to the application act with this note"*.

**What the dispatch writes now** [checked]. §L.47 lists the row under *"Rows the record carries to this act without
placing them"*: no ruling places it, so under the route ruling it gets **no line**, and it is sent to *Open* point (2)
(dispatch lines 4120–4124). Point (2) reads: *"Row 10.123: the record finds its proposal does not fit L2
score-decomposition Ruling 4 (its twin Row 6.113 is held with DP-O). At most the report lists the row and the record's
sentence for the user."* (lines 4142–4143). The check note found *"no Task names Row 10.123"* and left the point standing
(line 4153); the check row leaves *"§L.47 points (1) and (2)"* to the releasing sitting (line 20, found by a bounded
search). Point (1) is answered by Ruling 11 of the part 2 ruling record.

#### What the record already says

**No line: no ruling the dispatch carries places it.** The record's Ruling 1 places four rows, not this one; its §2
carries it. A search of the whole dispatch for *"10.123"*, not preceded by a digit or a point, meets it at line 20 (the check row), at lines
4107, 4109, 4121, 4142 and 4153 within §L.47, and at lines 4256, 4326, 4447 and 4513 in §L.48 to §L.51 [checked]. Lines
4326 and 4513–4514 carry it on *"as §L.47 states them"* and add nothing [checked]; lines 4256 and 4447, as the search
returned them, name it among rows carried *"unchanged"* or from group 1's record, and place nothing in the text the
search returned. So the route ruling
governs: *"Rows no family reaches stay proposals."* (route record line 58) [checked], which the dispatch's ledger reads
*"So a row no record names gets NO line."* (lines 101–102) [checked]. This is Ruling 16's case: a record carries a row
to the act without placing it.

**The note orders nothing the act can write.** The record marks the misfit as its writer's reading (*"On this side's
reading"*) and names no word and no line. The route record's step 2 has the act re-mark *"the ruled rows"* (line 59)
[checked]; step 1 leaves the rest proposals.

**§10 needs nothing.** The row already stands on the reading file's §10 transfer list, under the L2 heading (line 79125)
[checked], in the entry at lines 79252–79257 (*"the chord layer's inputs, its window and its two readings, … and the joint
choices it deferred or declined"*), with 47 other row-parts [checked: counted at the entry]. Task 3 (c) item 5 reaches
only row-parts a §L entry places RELOCATED (dispatch lines 5204–5209) [checked], and item 6 only rows lined from §L.21
to §L.24 (lines 5210–5216) [checked]; neither reaches this row. With no line, the row's proposal and its §10 entry agree.

**The open question reaches the user through the close, as at Rulings 12, 13 and 16.** Task 5's full close restates
*"every §L entry's *Open* points"* under *"The points that are not this batch's"* (dispatch lines 5518–5521) [checked].
So §L.47's *Open* point (2), rewritten to name the row and the record's sentence and to point to the ruling, reaches the
user there. That is also the most the point itself says the act does (*"At most the report lists the row and the
record's sentence for the user"*).

**Not held with DP-O by this act.** Ruling 11 gave Rows 7.48 (i), 7.294 (v) and 7.331 no line because each was proposed
UNPLACED and the record holds them UNPLACED by its own word. This row is proposed RELOCATED, and no ruling the dispatch
carries holds it with DP-O; the record says only that its proposal does not fit the twin's ruling. Writing it as held would be a placement that
neither this record nor any ruling the dispatch carries gives.

**Two records.** No §L entry gives the row a line, so form (b)'s two-record rule (Ruling 3) does not arise.

Applying D-599: the route ruling and Rulings 12 and 16 leave the row with no line, as a proposal; the record's sentence
reaches the user through §L.47's *Open* point (2) and the close. What is put to the user is the ratification of that
derivation.

#### The wording the writing side proposes

- **At the row:** no line from this record. Row 10.123 keeps its proposed **RELOCATED** to ***L2 — The tonal reading.
  The one entangled decision.***, as a proposal, the proposed paragraph untouched; it is not counted in the ruled
  distribution; its §10 entry (reading file lines 79252–79257) stands as it is.
- **§L.47's *Open* point (2)** is rewritten to point to the ruling, naming the row and quoting the record's sentence
  (record lines 57–59), so that Task 5's restatement under *"The points that are not this batch's"* carries it to the
  user. §L.47's bullet for the row (dispatch lines 4120–4124), which already says *"no line"*, stands.
- **In the report:** no listing of its own. The row is not STOP-and-report, so Task 3 (a)'s *rows the act could not
  place* does not reach it.

#### Weak points the writing side fixed before putting this

- **The list's extra naming in Task 5.** The list's (lxvi) also proposed naming §L.47's point (2), the row and the
  record's sentence inside Task 5's bullet *"The points that are not this batch's"* (list lines 2913–2915 and 2931–2932).
  Rulings 12, 13 and 16, ruled since, hold that an *Open* point pointing to its ruling is still restated by that bullet,
  which restates every §L entry's *Open* points; Ruling 16 dropped the same naming for item (lxv). So it is dropped here;
  the rewritten point (2) carries the reach.
- **The check row.** The list's (lxvi) *To do* did not name the check row's *"Left for the releasing sitting: §L.47
  points (1) and (2)."* (line 20). Added to the *To do* below, for point (2); Ruling 11 points it for point (1).

#### The weak point, stated by the working list

That the record's *"Carried for the application act"* asks for the row to be carried to the act, and not for the act to
re-mark it, is the writing side's reading, as at item (lxv). If you read it as an order to re-mark the row, the act still
has no word for it: RELOCATED to L2 as proposed, which the record reads as not fitting the twin's ruling, or held with
DP-O as the twin is, which no ruling the dispatch carries gives this row. The word would then be a question for you. Documentation only
either way (list lines 2917–2922).

#### The currently decided method

Unchanged: the record's method [checked: its lines 45–49]. DP-O stays open: no hierarchical reading of harmony is
adopted, and none is foreclosed. L3 publishes the cadence at each phrase end with its type, the phrase and section
grouping (sections may nest), the chord symbol as a view of the decided chord, the figured bass and the harmonic rhythm;
which notated marks end a phrase is decided at L3, the decisive further evidence being cadential; a read-off fact never
revises the decision it was read off; L3 contains no reduction of harmony.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. A line needs a ruling to name and a word to write, and the record gives neither. Towards the
objective, no line changes nothing in the analysis and drops none of what the record says: the row keeps its proposal,
§10 keeps it, and the open question of whether its proposal fits the twin's ruling reaches you at the close. So the
derivation is put for ratification, not as a menu. If you read the record's sentence as an order to re-mark the row,
that is your overrule, and the word for it becomes a question of its own.

**To do at release:** change §L.47's *Open* point (2) (dispatch lines 4142–4143), the check note's *"On point (2): no
Task names Row 10.123 (the search above). Points (1) and (2) stand."* (line 4153) for point (2), and the check row's
*"Left for the releasing sitting: §L.47 points (1) and (2)."* (line 20) for point (2), to point to the ruling; change the
working list's (lxvi) *To do at release* (its lines 2930–2933) to point to the ruling; former wordings kept.

### Item (lxvii) — Rows 7.97 (ii) and 7.118

*Added by the sitting booted on entry 746.*

#### What the question is, from scratch

Two rows of the L3 reading file come from the old design's cadence section, where each cadence cast a weighted vote for
the tonic.

- **Row 7.97** (reading file lines 4686–4700) [checked] has two claims: (i) an authentic cadence does not require the
  dominant's seventh; (ii) *"the seventh raises the cadence's vote weight"*. No derived statement speaks to either; the
  derivation is silent on both. Claim (i) is proposed ADOPTED — proposed and has its line at §L.6 (dispatch line 634)
  [checked]; it is not this item. Claim (ii) is proposed **RELOCATED** — to ***L2 — The tonal reading. The one entangled
  decision.***, *"as Row 7.53"*.
- **Row 7.118** (lines 5062–5074) [checked] is one claim: the vote weight is *"a weighted sum … of the evidence-strength
  cues … and the salience cues …, minus the per-type lower-confidence discount for half/plagal/evaded cadences"*. The
  derivation is silent; it is proposed **RELOCATED** to the same L2 heading, *"travelling with Row 7.117"*.

Rows 7.53 and 7.117 are the cadence's vote for the tonic. They stand **QUARANTINED**, each with its twin's audit
question, by the S38 first cut's derivation, as amended by the second-cut ruling (first-cut record lines 49–50 and
55–58) [checked]. So the two rows' proposals point at leads whose own placement has since changed.

**The record.** The remaining-cadence-type record (`cowork_rulings_2026_11_08_l3_remaining_cadence_type_group_sitting.md`,
its sitting booted on entry 591), read whole [checked]. Its Ruling 1 places two other rows, 7.96 and 7.110 (ii) (lines
27–41). Its §2, *"Carried, not decided by this ruling"*, says (lines 61–62):

> From the surface's §7, for the application act: Rows 7.97 (ii) and 7.118 carry proposals pointing at *"as Row 7.53"*
> and *"travelling with Row 7.117"*, which now stand QUARANTINED; whether another record places either was not searched.

**What the dispatch writes now** [checked]. §L.49 lists the two under *"Rows the record carries to this act without
placing them"*: no ruling places either, so under the route ruling each gets **no line**, and it sends them to *Open*
point (1) (dispatch lines 4317–4325). Point (1) reads: *"Rows 7.97 (ii) and 7.118 keep proposals that point at rows now
QUARANTINED. The route ruling leaves them as proposals; whether the report lists them for the user with the record's
sentence is the releasing sitting's. Their proposals were not read at the reading file by the sitting that wrote this
entry."* (lines 4328–4330). The check note found that no Task names them and left the point standing (lines 4338–4339);
the check row leaves *"§L.49 point (1)"* to the releasing sitting (line 20, found by a bounded search). Point (2) is
answered by its check note (lines 4339–4340).

#### What the record already says

**No line: no ruling the dispatch carries places them.** The record's Ruling 1 places two other rows; its §2 carries
these two and says another record was not searched for. A search of the whole dispatch for *"7.97"* and *"7.118"*, not
preceded by a digit or a point, meets them at line 20 (the check row), at §L.4 (line 497: *"7.97"* among the rows its
record mentions and does not place, *"No line from this record"*), at lines 563 and 789 (Row 7.97 (i), named), at lines
634 and 643 in §L.6 (Row 7.97 (i), placed), within §L.49 (lines 4303–4338), and at lines 4447 and 4513 in §L.50 and
§L.51 [checked; lines 563, 643, 789, 4447 and 4513 as the search returned them]. Lines 4447 and 4513 carry the two on,
*"unchanged"* and *"without placing them"*; no hit the search returned places claim (ii) of Row 7.97 or Row 7.118. So the
route ruling governs: *"Rows no family reaches stay proposals."*, which the dispatch's ledger reads *"So a row no record
names gets NO line."* (lines 101–102) [checked]. This is Rulings 16 and 17's case: a record carries rows to the act
without placing them. The working list's wider search, over the L3 ruling records and the surfaces it names (list lines
2938–2945), meeting the two only where they are carried on, is relayed; this sitting did not repeat it.

**Travel does not carry the leads' QUARANTINED to them.** Ruling 14 gave three travelling rows their lead's QUARANTINED
because a ruled text named them by number and said what the act does with them. Ruling 13 kept fourteen travelling rows
as proposals because no ruling named them. These two are Ruling 13's case: the first-cut filing that quarantines Rows
7.53 and 7.117 does not name them (first-cut record lines 45–59) [checked], and the record that names them carries them
without placing them.

**The note orders nothing the act can write.** The record's §2 names no word and no line; the route record's step 2 has
the act re-mark *"the ruled rows"* [relayed from Ruling 17].

**§10 needs nothing.** Both rows stand on the reading file's §10 transfer list, in the entry at lines 79174–79177
[checked] (*"the cadence's vote for the tonic, its weight, and the key-layer aggregation that absorbs a passing
motion"*), under the L2 heading (line 79125) [relayed from Ruling 17]. Task 3 (c) item 5 appends row-parts a §L entry
places RELOCATED (dispatch lines 5204–5209) [checked]; item 6 adds a *LEAVES L3* line beneath an entry whose row carries
a ruled line from the §L.21 to §L.24 records, and *"Where one §10 entry lists several rows, the line names the rows it
covers"* (lines 5210–5216) [checked]. So a line written beneath this entry for Rows 7.53 and 7.117 names those rows and
leaves the two untouched. With no line, each row's proposal and its §10 entry agree.

**The open question reaches the user through the close, as at Rulings 12, 13, 16 and 17.** Task 5's full close restates
*"every §L entry's *Open* points"* under *"The points that are not this batch's"* (dispatch lines 5518–5521) [checked].
So §L.49's *Open* point (1), rewritten to name the two rows and the record's sentence and to point to the ruling, reaches
the user there. That is what the point itself asks (*"whether the report lists them for the user with the record's
sentence"*).

**Two records.** No §L entry gives claim (ii) of Row 7.97 or Row 7.118 a line, so form (b)'s two-record rule (Ruling 3)
does not arise. Row 7.97 (i)'s line at §L.6 names claim (i) and does not touch claim (ii).

Applying D-599: the route ruling and Rulings 13, 16 and 17 leave the two with no line, as proposals; the record's sentence
reaches the user through §L.49's *Open* point (1) and the close. What is put to the user is the ratification of that
derivation.

#### The wording the writing side proposes

- **At the rows:** no line from this record. Row 7.97's claim (ii) and Row 7.118 each keep their proposed **RELOCATED**
  to ***L2 — The tonal reading. The one entangled decision.***, as a proposal, the proposed paragraph untouched; they are
  not counted in the ruled distribution; their §10 entry (reading file lines 79174–79177) stands as it is.
- **§L.49's *Open* point (1)** is rewritten to point to the ruling, naming the two rows and quoting the record's sentence
  (record lines 61–62), so that Task 5's restatement under *"The points that are not this batch's"* carries it to the
  user. §L.49's bullet for the two (dispatch lines 4318–4325), which already says *"no line"*, stands.
- **In the report:** no listing of its own. The rows are not STOP-and-report, so Task 3 (a)'s *rows the act could not
  place* does not reach them.
- **A citation corrected, an apparent error (the user's rule of 2026-09-22):** §L.49 cites §L.4's mention of *"7.97"* as
  *"line 489"* (dispatch lines 4302 and 4321), and the check row's account of that correction does the same (line 20,
  found by a bounded search). Line 489 is a table line for other rows; the mention is at line 497, in the
  sentence that opens at line 496 [checked]. Each becomes *"lines 496–497"*, former wordings kept.

#### Weak points the writing side fixed before putting this

- **The list's extra naming in Task 5.** The list's (lxvii) also proposed naming §L.49's point (1), the two rows and the
  record's sentence inside Task 5's bullet *"The points that are not this batch's"* (list lines 3011–3013). Rulings 16
  and 17 dropped the same naming for items (lxv) and (lxvi): an *Open* point pointing to its ruling is still restated by
  that bullet. So it is dropped here; the rewritten point (1) carries the reach.
- **The check row.** The list's (lxvii) *To do* did not name the check row's *"Left for the releasing sitting: §L.49
  point (1)."* (line 20). Added to the *To do* below.
- **The check row's copy of the wrong citation.** The list named the *"line 489"* citation at dispatch lines 4302 and
  4321 only; the check row carries it too. Added.

#### The weak point, stated by the working list

That the record's surface's *"The application act re-reads both at their entries"* [relayed: list lines 2955–2956; the
surface not opened by this sitting] is an expectation and not an order is
the writing side's reading, as at items (lxv) and (lxvi). If you read it as an order to re-mark the rows, the act still
has no word for them: RELOCATED to L2 as proposed, pointing at leads now QUARANTINED; or QUARANTINED following the leads,
which no ruling gives the two. One fact bears on Row 7.118 alone: its sentence ends with the per-type lower-confidence
discount, and the record's method states that a cadence's mass comes *"with no fixed, by-rule lowering"* (record lines
48–50) [checked]; cadence-mass Ruling 1 decided that content against for the rows it names, and the list's search found
that it does not name Row 7.118 [relayed: list lines 2999–3002]. Whether it reaches the clause is not judged here. The
word would then be a question for you. Documentation only either way (list lines 2995–3003).

#### The currently decided method

Unchanged: the record's method [checked: its lines 45–50]. L3 publishes a cadence only at a phrase end it has decided,
reading six features off lower layers in the tonality L2 decided; each declared vocabulary's type is computed from those
features, side by side, none principal (which vocabularies are declared is not yet decided); the perfect/imperfect split
is published in two views; a type that cannot be computed carries its reason; a cadence's mass comes only from doubt
already counted, with no fixed, by-rule lowering; L3 reads no voice-leading fact in this specification; L2 reads nothing
L3 publishes.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. A line needs a ruling to name and a word to write, and the record gives neither. Towards the
objective, no line changes nothing in the analysis and drops none of what the record says: the rows keep their
proposals, §10 keeps them, and the open question, that their proposals point at leads now QUARANTINED, reaches you at
the close. So the derivation is put for ratification, not as a menu. If you read the surface's sentence as an order to
re-mark the rows, that is your overrule, and the word for them becomes a question of its own.

**To do at release:** change §L.49's *Open* point (1) (dispatch lines 4328–4330), the check note's *"Point (1) stands."*
(line 4339) and the check row's *"Left for the releasing sitting: §L.49 point (1)."* (line 20) to point to the ruling;
correct *"line 489"* to *"lines 496–497"* at dispatch lines 4302 and 4321 and in the check row (line 20); change the
working list's (lxvii) *To do at release* (its lines 3010–3015) to point to the ruling; former wordings kept.

### Item (lxxix) — Row 44.19 (i) and (ii)

*Added by the sitting booted on entry 747.*

#### What the question is, from scratch

One row of the L3 reading file comes from the old design's note on recognising named progressions (the catalog of
stock chord patterns), its section *"2. Placement — no new layer"*.

- **Row 44.19** (reading file lines 61252–61272) [checked] has three claims: (i) the recognition's evidence enters as
  one feature of the old function layer's plausibility selection, and through the override path; (ii) the old function
  layer is the re-ranker; (iii) no stage is added for the recognition. The derivation is silent on all three (lines
  61264–61265). Parts (i) and (ii) are each proposed **RELOCATED** — to ***L2 — The tonal reading. The one entangled
  decision.*** (lines 61267–61270); part (iii) is proposed **UNPLACED** (lines 61270–61272).

**The record.** The lead-rows record (`cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md`, its sitting booted
on entry 542), read whole [checked]. Its Ruling 1 ratifies its surface's placements of *"the 25 lead row-parts"* (line
19). Under *"§3.1, follow wholly (13)"* it says (lines 35–36):

> RELOCATED to L2 (*The tonal reading. The one entangled decision.*): 44.19 (iii), with parts (i) and (ii) of the same
> row.

and *"Surface §3.1 note 3 stands with the ruling: Row 44.19 (iii) is wholly the use as evidence"* (lines 47–48).

**What the dispatch writes now** [checked]. §L.30 gives part (iii) its RELOCATED line (dispatch line 2562). Its check
sum closes at the 25 without parts (i) and (ii), which *"are not among the 25 and get no line from this record (*Open*
point (2))"* (lines 2568–2572). Point (2) reads: *"Row 44.19 (iii)'s "with parts (i) and (ii) of the same row": whether
the record places (i) and (ii) too, or says they already stand there, is not stated; they are not among the 25. To be
read at §6 and at the surface before release; until then (i) and (ii) get no line from this record."* (lines
2603–2606). The check note left it standing: the surface *"does not say either whether parts (i) and (ii) of Row 44.19
already stand RELOCATED"* (lines 2618–2619); the check row leaves *"§L.30 points (1) and (2)"* to the releasing
sitting (line 20, found by a bounded search).

#### What the record already says

**Parts (i) and (ii) already stand RELOCATED to that L2 heading, as proposals.** That is what point (2) asked to be
read at §6, and the row answers it (lines 61267–61270) [checked]. So *"with parts (i) and (ii) of the same row"* says
that part (iii) goes to the destination where (i) and (ii) are already proposed.

**The record counts part (iii) and not the other two.** Its *"follow wholly (13)"* is the eleven ADOPTED rows, Row 44.19
(iii) and Row 38.79 (i) (record lines 34–37) [checked]; its population is *"the 25 lead row-parts"* (line 19), and
§L.30's check sum closes at 25 without (i) and (ii). The surface's table line is for *"44.19 (iii)"* (surface line 75)
[checked], and its note 3 grounds the placement in what (iii) shares with them: the stage not added *"is on the evidence
path into the old function layer"* (surface lines 89–91), the subject of claim (i) [checked]. The record, read whole,
names no word for (i) and (ii) and says nothing of what the act does with them.

**No line: no ruling the dispatch carries places them.** A search of the whole dispatch for *"44.19"*, not preceded by
a digit or a point, meets it at line 20 (the check row: *"Row 44.19 (i) and (ii) are named and not placed"*), at line
2495 (part (iii) only, among rows the catalog key record names and does not place; §L.29, as the working list names
it) and within §L.30 (lines 2562–2619) [checked; line 20 as the search returned it]. No hit the search returned places
part (i) or (ii). So the route ruling governs: *"Rows no family reaches stay proposals."*, which the dispatch's ledger
reads *"So a row no record names gets NO line."* (lines 101–102) [checked]. This is Rulings 16, 17 and 18's case: a
record names rows and does not place them.

**Not Ruling 14's case.** Ruling 14 gave three rows a line because the ruled text named them by number and said what
the act does with them (*"follow it at the application act"*). Here the ruled text names parts (i) and (ii) to say
where part (iii) goes; it gives them no word and orders no act.

**§10.** Task 3 (c) item 5 appends row-parts a §L entry places RELOCATED *"out of UNPLACED or against its proposal"*
(dispatch lines 5204–5209) [checked]; it reaches part (iii), proposed UNPLACED, and not parts (i) and (ii), which get no
line. Item 6 reaches rows lined from the §L.21 to §L.24 records (lines 5210–5216) [checked], not this row. Whether §10
carries any part of Row 44.19 was not read by this sitting; with no line for (i) and (ii), this item writes nothing
there.

**The open question reaches the user through the close, as at Rulings 12, 13, 16, 17 and 18.** Task 5's full close
restates *"every §L entry's *Open* points"* under *"The points that are not this batch's"* (dispatch lines 5518–5521)
[checked]. So §L.30's point (2), rewritten to name the two parts and to point to the ruling, reaches the user there.

**Two records.** No §L entry gives part (i) or (ii) a line, so form (b)'s two-record rule (Ruling 3) does not arise.

Applying D-599: the route ruling and Rulings 16 to 18 leave parts (i) and (ii) with no line, as proposals; part (iii)'s
ruled line sends it to the same L2 heading. What is put to the user is the ratification of that derivation.

#### The wording the writing side proposes

- **At the row:** no line from this record for parts (i) and (ii). Each keeps its proposed **RELOCATED** to ***L2 — The
  tonal reading. The one entangled decision.***, as a proposal, the proposed paragraph untouched; they are not counted
  in the ruled distribution. Part (iii)'s line from §L.30 (dispatch line 2562) is not touched.
- **§L.30's *Open* point (2)** is rewritten to point to the ruling, naming the two parts and saying that they stand
  proposed RELOCATED to the same L2 heading (reading file lines 61267–61270), so that Task 5's restatement under *"The
  points that are not this batch's"* carries it to the user.
- **In the report:** no listing of its own. The parts are not STOP-and-report, so Task 3 (a)'s *rows the act could not
  place* does not reach them.

#### Weak points the writing side fixed before putting this

- **The check row.** The list's (lxxix) *To do* did not name the check row's *"Left for the releasing sitting: §L.30
  points (1) and (2)"* (line 20). Added to the *To do* below, for point (2).
- **The ledger line.** The list relayed the ledger's *"So a row no record names gets NO line"* (dispatch line 101)
  without reading it; this sitting read it at lines 101–102.
- **No extra naming in Task 5** is proposed by the list's (lxxix), so nothing is dropped here (as it was under Rulings
  16 to 18).

#### The weak point, stated by the working list

That *"with parts (i) and (ii) of the same row"* describes where part (iii) joins them, and does not place them, is the
writing side's reading, resting on the record's count and §6 (list lines 3817–3820). If you read it as placing them,
each gets a form (b) line, **RELOCATED** to the same L2 heading, *as proposed*, the word each part already proposes; the
word and the destination stay the same, and only whether a ruled line is written, and whether the two parts are counted
in the ruled distribution, would change. Documentation only either way.

#### The currently decided method

Unchanged: the record's method [checked: its lines 50–54]. L2 decides key and chord together; its progression term is a
table of chord-to-chord pairs; DP-O stays open, the catalog term among its unmeasured candidates. L3 publishes the
cadence at each phrase end with its type, the phrase and section grouping, the chord symbol, the figured bass, the
harmonic rhythm, and, by the key sitting's Ruling 1, the catalog matches once the application act amends
`FRAMEWORK.md`.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. A line needs a ruling that places the part, and the record places part (iii) alone. Towards
the objective, no line changes nothing in the analysis: all three parts point to the same L2 heading, (iii) by ruling
and (i) and (ii) by proposal, and the open question reaches you at the close. So the derivation is put for
ratification, not as a menu. If you read the record's words as placing (i) and (ii), that is your overrule, and each
gets a RELOCATED line *as proposed*.

**To do at release:** change §L.30's *Open* point (2) (dispatch lines 2603–2606), the check note's *"Point (2) stands:
…"* (lines 2618–2619) and the check row's *"Left for the releasing sitting: §L.30 points (1) and (2)"* (line 20), for
point (2), to point to the ruling; change the working list's (lxxix) *To do at release* (its lines 3828–3829) to point
to the ruling; former wordings kept.

### Item (lxxxii) — seven further row-parts of member 23, with Rows 23.1 and 23.44

*Added by the sitting booted on entry 748.*

#### What the question is, from scratch

Member 23 of the L3 reading file is the old design's section on the style system (`ARCHITECTURE.md` §6), among it the
user-facing preset layer (§6.8): how a preset is named, how its mixture of idioms is measured or declared, what may be
claimed of a chosen mixture, and which values the licence rule reaches. Family 6's ruling placed seven of its rows
outside the framework at §6.8, as their L2 twins are placed. Nine other row-parts of the member, all read at their rows
by this sitting (each found by the row-heading search) [checked], are not placed by it:

- **Rows 23.30 (ii), 23.32, 23.33, 23.34 and 23.35** (genre names as labels over mixtures; coverage in three tiers; a
  mixture measured, or declared with its theory reason; the analysis moving away from the starting mixture) — each
  proposed **RELOCATED** to ***L2 — The tonal reading. The one entangled decision.*** (lines 32790–32791, 32820–32822,
  32835–32836, 32849–32850, 32863–32864).
- **Rows 23.36 (ii) and 23.38** (a chosen point's evidence status) — each proposed **RELOCATED** to ***the uncertainty
  surface*** (lines 32883–32884, 32915).
- **Row 23.1** (a style's harmonic-language dimension) — proposed **RELOCATED** to the same L2 heading (lines
  32337–32339).
- **Row 23.44** (the licence rule reaching the per-idiom anchors, not a user's mixture) — proposed **RELOCATED** to the
  same L2 heading, travelling with Row 23.43 (lines 33008–33009).

**The record.** The presets-scope record (`cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md`, its sitting
booted on entry 562), read whole [checked]. Its §2, *"Carried, not decided by this ruling"* (lines 71–74):

> The surface's §4: seven other row-parts of member 23 (Rows 23.30 (ii), 23.32, 23.33, 23.34, 23.35, 23.36 (ii), 23.38)
> are proposed at L3 otherwise than their L2 twins, which Ruling 1 placed at §6.8 — five sent to L2, two to the
> uncertainty surface; Row 23.44 not read; Row 23.1 differs from its twin's proposal. None is UNPLACED. Whether they go to
> the application act as noted or onto a later surface is for after family 6, judged against the plan.

Its surface's §4 (lines 220–246) [checked] lists the same rows and adds *"This side's reading, not tested: the L2-bound
ones look like the 2A derivation; the two evidence-status ones may fairly stay with the uncertainty surface."*

**What the dispatch writes now** [checked]. §L.44 gives none of the nine a line; its table (lines 3816–3820) places only
the record's 2A, 2B and 2C rows, and its note says the parts (ii) of Rows 23.30 and 23.36 *"get no line from this
record"* (lines 3829–3831). Its *Open* point (3) reads: *"The record's §2 carries seven further row-parts of member 23 to
"after family 6, judged against the plan" (carry list §8 item 9); this record writes nothing for them."* (lines
3862–3863). The check note ends *"Points (1) to (3) stand."* (line 3878); the check row leaves *"§L.44 points (1) to
(3)"* to the releasing sitting (line 20, found by a bounded search).

#### What the record already says

**The record places none of the nine.** It carries them under *"Carried, not decided by this ruling"* and leaves where
they go *"for after family 6, judged against the plan"*. It names no word for any of them and orders no act. Its surface
marks its own lean as *"not tested"*.

**No line: no ruling the dispatch carries places them.** A search of the whole dispatch for the nine row numbers, not
preceded by a digit or a point, meets them only within §L.44 (lines 3818, 3819, 3826, 3829, 3839, 3884–3886) [checked],
none of which places them. A search of the two release ruling records of 2026-11-11 (part 1 and part 2) for the same
numbers, *"member 23"* and *"family 6"* meets nothing [checked]. That the ten L3 ruling records of 2026-11-08 meet none
of them is relayed from the working list (its lines 3989–3990). So the route ruling governs: *"Rows no family reaches stay
proposals."*, which the dispatch's ledger reads *"So a row no record names gets NO line."* (lines 101–102) [checked].
That is the case of Rulings 12, 16, 17, 18 and 19: a record names rows and does not place them. The batch may not choose
a word itself: *"Nothing is repaired, re-read into a different placement, or placed by this batch's own judgment."*
(*Findings in this batch*, lines 227–228) [checked].

**Not Ruling 14's case.** Ruling 14 gave rows a line because the ruled text named them and said what the act does with
them. Here the record says the opposite: that whether they go to this act at all is still to be judged.

**§10 already carries all nine** [checked]. Under §10's L2 heading (line 79125): Row 23.1 (lines 79356–79357); Rows
23.19 (i), 23.20 and 23.30 (ii) (79364–79365); Rows 23.32 to 23.35 (79366–79368); Rows 23.43 and 23.44 (79369–79371).
Under the uncertainty-surface heading (line 79701): Rows 23.36 (ii) and 23.38 (79722–79724). (These entries were read at
lines 79350–79393 and 79719–79724; that no other heading falls between line 79125 and line 79350 rests on Ruling 17,
which found Row 10.123's entry under the same L2 heading at line 79252.) Task 3 (c) item 5 reaches only row-parts a §L
entry places (lines 5204–5209) [checked], so it appends nothing for any of the nine, and nothing needs appending.

**The open question reaches the user through the close, as at Rulings 12, 13 and 16 to 19.** Task 5's full close
restates *"every §L entry's *Open* points"* under *"The points that are not this batch's"* (lines 5518–5521) [checked].
So §L.44's point (3), rewritten to name the nine and quote the record's §2 sentence, reaches the user there.

**Two records.** No §L entry gives any of the nine a line, so form (b)'s two-record rule (Ruling 3) does not arise.

Applying D-599: the route ruling and Rulings 16 to 19 leave all nine with no line, as proposals, with §10 as it stands.
What is put to the user is the ratification of that derivation.

#### The wording the writing side proposes

- **At the rows:** no line from this record. Each of the nine keeps its proposed **RELOCATED** (to the L2 heading for
  Rows 23.1, 23.30 (ii), 23.32 to 23.35 and 23.44; to *the uncertainty surface* for Rows 23.36 (ii) and 23.38), as a
  proposal, the proposed paragraph untouched; none is counted in the ruled distribution; their §10 entries stand as they
  are.
- **§L.44's *Open* point (3)** is rewritten to point to the ruling, naming the seven row-parts with Rows 23.1 and 23.44
  and quoting the record's §2 sentence whole, so that Task 5's restatement under *"The points that are not this
  batch's"* carries it to the user.
- **In the report:** no listing of its own. The rows are not STOP-and-report, so Task 3 (a)'s *rows the act could not
  place* does not reach them.

#### Weak points the writing side fixed before putting this

- **The extra naming in Task 5.** The list proposes naming §L.44's point (3) separately in Task 5's bullet. Not used, as
  under Rulings 16 to 18: the rewritten point already reaches the close.
- **The check row.** The list's *To do* did not name the check row's *"§L.44 points (1) to (3)"* (line 20). Added
  below, for point (3).
- **A stale line citation (the user's rule of 2026-09-22).** The check note cites the carry list's §8 item 9 as *"lines
  188–189"* (dispatch line 3868). At the carry list as it now stands, item 9 is at lines 191–199, the presets-scope part
  at lines 196–197, and lines 188–189 are items 7 and 8 [checked]. Added to the *To do*: *"lines 191–199"*.
- **§10 read.** The list did not look for the five L2-bound rows at §10; this sitting found all nine there (above).
- **The ledger line** (dispatch line 101), which the list relayed, was read at lines 101–102.
- **The list's *"No ruling record in the rulings folder's listing is dated after 2026-11-08"*** is overtaken: the two
  release records of 2026-11-11 now stand there. Both were searched (above) and name none of the nine.

#### The weak point, stated by the working list

That *"Whether they go to the application act as noted or onto a later surface"* leaves the choice open, and does not
send the rows to this act, is the writing side's reading, resting on the route ruling (list lines 4008–4013). If you
read it as sending them here, the act still has no word for them: the record gives none, and their own proposals are
the ones its surface says may conflict with family 6's placement of their twins. The word would then be a question for
you. Documentation only either way.

#### Not decided here

Whether the five L2-bound rows should follow their twins outside the framework, as the record's surface leans
untested, is not decided. Nor is the fact that the axis of Rows 23.36 (ii) and 23.38 reads L3-S33 **AGREES**, and Row
23.44's reads L3-S14 **AGREES**, while each is proposed RELOCATED; with no line, Ruling 9 does not arise.

#### The currently decided method

Unchanged: the record's method [checked: its lines 60–65]. L2 decides key and chord together and publishes the chord as
a degree in its tonality, and the tonality as tonic and mode; L3 publishes facts read off it (chord symbol, figured
bass, harmonic rhythm, cadence with type at each phrase end, phrase and section grouping, key areas, the pivot
re-expression, the modal counts per key area, and, once the application act amends `FRAMEWORK.md`, the catalog
matches); no preset, style label or idiom mixture reaches L2; no preset chooses the catalog L3 reads, and L3's method
uses no idiom tag; a display turns published facts into text; L3 owns the answers to its own questions.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. A line needs a ruling that places the row, and the record places none of the nine. Towards
the objective, no line changes nothing in the analysis: each row keeps its proposal, §10 already lists each, and the
open question, with the record's sentence whole, reaches you at the close. So the derivation is put for ratification,
not as a menu. If you read the record as sending the rows to this act, that is your overrule, and the word for each
becomes a question of its own.

**To do at release:** change §L.44's *Open* point (3) (dispatch lines 3862–3863), the check note's *"Points (1) to (3)
stand."* (line 3878) and the check row's *"Left for the releasing sitting: §L.44 points (1) to (3)."* (line 20), for
point (3), to point to the ruling; correct the check note's *"lines 188–189"* (line 3868) to *"lines 191–199"*; change
the working list's (lxxxii) *To do at release* (its lines 4022–4027), for point (3), to point to the ruling; former
wordings kept.

---

## Site 15 — Group 2, points with nothing written, listed for the user among the points that are not this batch's: items (lxi), the L2-S38 observation, (lxii), the two sets the pairwise-grammar record hands to the act, (lxix), carry list §9 points 1 to 4, (lxxii), the DP-O note, and (lxxiv), the phase-definition surface's amendment

*(Former heading, kept: "… (lxix), carry list §9 points 1 to 4, and (lxxii), the DP-O note". (lxxiv) added.)* *(Former heading, kept: "… (lxii), the two sets the pairwise-grammar record hands to the act, and (lxix), carry list §9
points 1 to 4". (lxxii) added.)* *(Former heading, kept: "… items (lxi), the L2-S38 observation, and (lxii), the two sets the pairwise-grammar record
hands to the act". (lxix) added.)*

*Added by the sitting booted on entry 749.* The second group site, on the user's ruling of 2026-11-11 (*"As many as will
fit in sessions."*, entry 744 §2 item 3). Group 2 is the items where nothing is written and the point is listed for the
user among *"The points that are not this batch's"*, as entry 744 §2 item 4 sorted them from the list's headings alone:
(lxi), (lxii), (lxxii), (lxxiv) and (lxix). They are taken here in list order, by their lines in the list: (lxi) at 2579,
(lxii) at 2631, (lxix) at 3097, (lxxii) at 3312, (lxxiv) at 3470 [relayed from entry 744 §2 item 4, except (lxi), checked
by this sitting]. The sitting booted on entry 749 added (lxi), the sitting booted on entry 750 added (lxii), the
sitting booted on entry 751 added (lxix), the sitting booted on entry 752 added (lxxii), and the sitting booted on
entry 753 added (lxxiv), each its line checked by that sitting; with (lxxiv), group 2 is complete. (lxix) differs
from the first two in one respect: the act already writes one of its four points (point 2, at S-50), as the dispatch
says; what the release adds for them is nothing. *(Former wording, kept: "… the sitting booted on entry 751 added
(lxix), and the sitting booted on entry 752 added (lxxii), each its line checked by that sitting; (lxxiv) is named in
"What this file does not yet carry", for a later sitting to add here.")* *(Former wording, kept: "The sitting booted on entry 749 added (lxi),
the sitting booted on entry 750 added (lxii), and the sitting booted on entry 751 added (lxix), each its line checked
by that sitting; the others are named in …")* *(Former wording, kept: "The sitting booted on entry 749 added (lxi), and the sitting booted on entry 750 added
(lxii), its line checked by that sitting; the others are named in …")* *(Former wording, kept: "The sitting booted on
entry 749 added (lxi); the others are named in …")*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles that the release
adds nothing for points records carry open, send back to the user or leave without a site, and how the dispatch
carries them to the user. Nothing about what the analysis does. *(Former wording, kept: "… adds nothing for points
records carry open or send back to the user, and how …" (lxxii) added.)* *(Former wording, kept: "It settles that the act writes nothing for points records
carry open with no words for the act, and how …" (lxix) added.)* *(Former wording, kept: "… writes nothing for one observation the fit-and-rest
record carries open, and how the dispatch carries it to the user." (lxii) added.)*

### Item (lxi) — the L2-S38 observation

*Added by the sitting booted on entry 749.*

#### What the question is, from scratch

L2-S38 is a statement of the L2 specification, amended by L2 fit Ruling 1 [relayed from the record; L2-S38 was not read
by this sitting]. The fit-and-rest record (`cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md`, its sitting booted on
entry 517), read whole [checked], ratified three L3 statements: L3-S14 (every weight of the phrase model fitted from
annotated phrase boundaries, held out by piece, with its capacity declared before the fit), L3-S41 and L3-S42. Its first
cut noticed something about L2 on the way, and the record carries it as the first bullet under *"Not decided by this
ruling, carried:"* (lines 59–61):

> The observation of the first cut's §5: the amended second sentence of L2-S38 (L2 fit Ruling 1) no longer contains
> *"on held-out folds, with its capacity budget declared in advance"*. Principle #20 binds L2 directly. Left for the
> application act or a later L2 coherence pass.

In plain words: when L2's statement was amended by an earlier ruling, a clause requiring held-out testing with a capacity
budget fixed in advance dropped out of its second sentence. The record says principle #20 binds L2 anyway, and leaves the
matter to either the application act or a later tidying of the L2 documents. The carry list lists it as §9 point 9 (its
lines 219–220) [checked].

**What the dispatch writes now** [checked]. §L.24 places the record's four carried bullets, quoted whole, beside L3-S14
(amendment 2, lines 2020–2022); this observation is the first of them. Its *Open* point (2) (lines 2063–2067) reads, in
part: *"The record does not order it, and this batch's standing bars bar it from writing any specification statement's
words, so on the writing side's reading this act writes nothing at L2-S38 and lists the observation in its report. To be
confirmed before release."* The check note says *"the confirmation it asks for stays with the releasing sitting"* (lines
2072–2073), and the check row leaves *"the confirmation point (2) asks for"* to the releasing sitting (line 20, found by
a bounded search).

So the question is that confirmation: does the act write nothing at L2-S38, and where in its report does the
observation go?

#### What the record already says

**The record orders nothing.** The bullet stands among what Ruling 1 does not decide; it names two possible homes and
gives no words for either.

**The dispatch bars the act from writing at L2-S38** [checked]: the standing bars, *"no derivation of any specification
statement — an amendment is the record's words placed, never this batch's"* (line 201); Task 4's *What this Task does
not do*, *"It does not edit … `cowork_derived_specification_l2_2026_10_10.md` or IC-L2"* (lines 5432–5433); and *What
this batch does NOT do*, which names the same two again (lines 5553–5554) and closes the write set (lines 5556–5558).
With no words from the record and no L2 document open to the act, of the record's two homes only the later L2 pass is
left. So the writing side's reading in point (2) follows from the dispatch and the record, with no new choice.

**The observation still reaches the successor**, by §L.24's amendment 2 (above). Nothing here changes that.

**Where it is listed** [checked]. Task 3 (c) item 4 and Task 5's report heading *points answered by a record's own
derivation, nothing written* (lines 5201–5203, 5512) are for a point a record answers by its own derivation (item 4's
case: *"§9 point 5 is answered by L3-S30"*). This record answers nothing here, so listing it there would describe it as
answered. Task 5's full close restates *"every §L entry's *Open* points"* under *"The points that are not this batch's"*,
as NOT YOURS (lines 5518–5521). §L.24's point (2), rewritten to point to the ruling, is one of them, so the observation
reaches the user there, as Rulings 12, 13 and 16 to 20 have it for their points.

**No later ruling answers it.** A search of the two release ruling records of 2026-11-11 for *"L2-S38"*, *"coherence
pass"*, *"held-out folds"* and *"§L.24"* meets nothing [checked]. A search of the whole dispatch for the first three meets
them only within §L.24 (lines 2063, 2064, 2066, 2087) [checked].

**No rows.** The site places no reading-file row, so form (b)'s two-record rule (Ruling 3) and §10 do not arise.

Applying D-599: the dispatch's bars and the record leave nothing written at L2-S38 and the point open for the user. What
is put to the user is the ratification of that derivation.

#### The wording the writing side proposes

- **At L2-S38:** nothing is written; the act edits no L2 document, as the dispatch already says.
- **§L.24's *Open* point (2)** is rewritten to point to the ruling, quoting the record's bullet whole and saying that the
  act writes nothing at L2-S38, so that Task 5's restatement under *"The points that are not this batch's"* carries it
  to the user.
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written*.

#### Weak points the writing side fixed before putting this

- **The extra naming in Task 5.** The list proposes naming the observation separately in Task 5's bullet (its lines
  2620–2622). Not used, as under Rulings 16 to 18 and 20: the rewritten point already reaches the close.
- **The check row.** The list's *To do* did not name the check row's *"the confirmation point (2) asks for"* (line 20).
  Added below, for point (2).
- **The test the list leans on.** The list grounds the listing on its items (lix) and (lx) (*"(lix) and (lx) set the
  test"*, its lines 2598–2600), which the part 2 ruling record, read whole, does not answer (they are group 3 of entry
744 §2 item 4). Here the
  listing rests instead on Task 3 (c) item 4's own words and on the close, as Rulings 12, 13 and 16 to 20 applied them.

#### The weak point, stated by the working list

That the report lists the observation among the points not this batch's, and not under a heading of its own, is the
writing side's reading of Task 5's wording (list lines 2609–2611). If you want a heading of its own, only the report's
heading changes. Documentation only either way.

#### Not read, not decided here

L2-S38 was not read at the L2 successor or at any L2 record, and the first cut's surface, where the observation comes
from, was not opened. Whether principle #20 binding L2 directly makes the dropped clause immaterial is the record's
sentence and is not judged. Whether a later L2 coherence pass is planned was not searched. §L.24's *Open* point (1) is
not touched.

#### The currently decided method

Unchanged: the record's method [checked: its lines 73–78]. L3's phrase model has no hand-set numbers; every number is to
be fitted from licence-clear music with marked phrase boundaries, held out by piece, with a capacity declared first, and
until that fit exists the model is provisional. L3 is deterministic: widening the selection or editing the score gives
the same result as one fresh run over the final music. L3's phrases cut across all the voices and follow one another
without gaps or overlaps; L3 reads nothing from the voice-leading side; thematic restatement comes from L1; grading
against annotations is the measurement stage's. L2's fit, as L2 fit Ruling 1 amended it, is not touched and was not read.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. Writing at L2-S38 is barred by the dispatch itself and the record gives no words, so the act
writes nothing; the point stays open and reaches you at the close. Towards the objective, nothing in the analysis
changes, and the dropped clause is not lost from view: it stands beside L3-S14 in the successor and in your list at the
close. So the derivation is put for ratification, not as a menu. A heading of its own in the report is the one variant,
and it changes only where the point is printed.

**To do at release:** change §L.24's *Open* point (2) (dispatch lines 2063–2067), its check note's *"the confirmation it
asks for stays with the releasing sitting"* (lines 2072–2073) and the check row's *"Left for the releasing sitting: …
the confirmation point (2) asks for"* (line 20), for point (2), to point to the ruling; change the working list's (lxi)
*To do at release* (its lines 2618–2622) to point to the ruling, its proposed Task 5 naming not used; former wordings
kept.

### Item (lxii) — the two sets the pairwise-grammar record hands to the act

*Added by the sitting booted on entry 750.*

#### What the question is, from scratch

The pairwise-grammar record (`cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md`, its sitting booted on
entry 552), read whole [checked], ratified the placements of fifteen row-parts about the old catalog of named
progressions and the old yes/no test of which chord successions are "licensed" (its Ruling 1). Under *"Carried, not
decided by this ruling"* it hands the application act an item with two sets of rows (lines 69–73):

> For the application act (surface §2): the L2 twins of Rows 57.396, 57.398, 57.405, 57.451 and 57.493 to 57.496 are
> proposed RELOCATED to L3, not ruled, and differ from the HISTORICAL placements here; and the L3 reading file proposes
> Rows 7.77, 7.78 (i), 7.81 to 7.84, 46.1 (ii) and 57.396 (i) RELOCATED to L2 while L2 Ruling 1 placed L2's own rows on
> the yes/no test HISTORICAL (established for Row 7.77's sentence, L2 Row 5.83; the others not checked). Those rows are
> not this family's.

In plain words: in each set, rows carry proposals that pull against a ruling. The first set is eight rows of the L2
reading file, the L2 twins, which the record's surface names as L2 Rows 50.9, 50.22, 50.7, 53.62, 53.61, 53.63, 53.64 and
53.79 (i) [checked at the surface, lines 96–97; the L2 reading file not opened]. They are proposed as moving to L3, while
this record placed their L3 rows HISTORICAL. The second set is eight row-parts of the L3 reading file on the licensed root
motions and the grammar that owned them. They are proposed as moving to L2, while L2's own ruling made the yes/no test
HISTORICAL on L2's side. The record answers neither difference.

**What the dispatch writes now** [checked]. §L.38's *Open* point (3) (lines 3304–3310) quotes the item and says: *"The
record hands these to this act but does not say what the act writes for them; the first set are rows of the L2 reading
file. What this act does with them is to be fixed before release; until then nothing is written for them."* Its check
note says *"Points (1) to (3) stand."* (line 3319), and the check row leaves *"§L.38 points (1) to (3)"* to the releasing
sitting (line 20, found by a bounded search).

So the question is what the act writes for each set, and where the item goes in its report.

#### What the record already says

**The first set: the act cannot write there** [checked]. The dispatch's *"The reading file"* is the L3 one (line 78),
and *"the reading file's additions"* are among the paths that are *"the whole write set"* (lines 5556–5558); the L2
reading file is not among them. Three other §L entries say the same of their records' L2 rows: *"Those are rows of the
L2 reading file, a different reading file; this act writes nothing for them from this record"* (§L.37, lines
3193–3195; in the same terms at §L.42, lines 3681–3682, and at lines 3937–3939, which the list places in §L.45
[the section relayed]). The record orders nothing for the
twins and rules none of them.

**The second set: no ruling the dispatch carries places any of the eight** [checked]. At §6 each is proposed
**RELOCATED** to ***L2 — The tonal reading. The one entangled decision.***, each read at the line the list gives, its heading seen there: Row
7.77 at line 4383 (*"which chord successions are licensed bears on the chord decision"*); Rows 7.78 (i), 7.81, 7.82, 7.83
and 7.84 at lines 4403, 4445, 4461, 4475 and 4489, *"travelling with Row 7.77"*; Row 46.1 (ii) at line 63513; Row 57.396
(i) at line 75766. The record places none of them. A search of the whole dispatch for the eight numbers, not
preceded by a digit or a point, meets Rows 7.77, 7.78 and 7.81 to 7.84 only within §L.38; claim (ii) of Row 46.1 only
within §L.38 (its claim (i) is at §L.30, and the bare number stands in lists); and Row 57.396 (i) within §L.38 and in
§L.33's note naming §L.38 (line 2855). A search of the two release ruling records of 2026-11-11 for *"§L.38"* meets
Ruling 9's list of A1 and A2 points (point (1)) and the part 1 record's ruling on Rows 24.4, 24.6 and 38.79 (ii) (point
(2)), and nothing on point (3). So the route ruling's *"Rows no family reaches stay proposals."*, read by the ledger as
*"So a row no record names gets NO line."* (lines 101–102), governs, as at Rulings 12, 13 and 16 to 20. The act may not
choose a word itself: *"No ruling taken"*, *"No derivation of any statement"* (lines 5546–5548). Task 3 (c) item 5
reaches RELOCATED placements a §L entry makes, and §L.38 makes none (its check note, lines 3318–3319), so nothing is
appended at §10.

**It is not Ruling 14's case.** There the ruled text named the rows and said what the act does with them. Here the
record names the rows to say *"Those rows are not this family's"* and gives no word; the route record's step 2 re-marks
*"the ruled rows"* only [relayed from Ruling 16].

**Where it is listed** [checked]. As Ruling 21 has it for (lxi): Task 3 (c) item 4 and Task 5's report heading *points
answered by a record's own derivation, nothing written* (lines 5201–5203, 5512) are for a point a record answers, and
this record answers neither difference. Task 5's full close restates *"every §L entry's *Open* points"* under *"The
points that are not this batch's"*, as NOT YOURS (lines 5518–5521). §L.38's point (3), rewritten to point to the ruling,
is one of them, so the item reaches the user there.

**No line, so no two-record question.** Form (b)'s two-record rule (Ruling 3) does not arise. The rows' other claims are
not touched: Row 7.78 (ii) (proposed HISTORICAL at §6, line 4404), Row 46.1 (i) (§L.30) and Row 57.396 (ii) (§L.38's
table, line 3263).

Applying D-599: the write set leaves nothing to write for the first set, and the route ruling and the dispatch's bars
leave no line for the second; the item stays open for the user. What is put to the user is the ratification of that
derivation.

#### The wording the writing side proposes

- **The first set (the eight L2 twins):** nothing is written; the L2 reading file is outside the act's write set, and
  the twins' proposals stand untouched.
- **The second set (the eight L3 row-parts):** no line. Each keeps its proposed **RELOCATED** to ***L2 — The tonal
  reading. The one entangled decision.***, as a proposal, the proposed paragraph untouched; none is counted in the ruled
  distribution; nothing is appended at §10.
- **§L.38's *Open* point (3)** is rewritten to point to the ruling, naming both sets, quoting the record's item whole
  and saying that the act writes nothing for either, so that Task 5's restatement under *"The points that are not this
  batch's"* carries it to the user.
- **In the report:** no listing of its own; the rows are not STOP-and-report, so Task 3 (a)'s *rows the act could not
  place* does not reach them; and not under *points answered by a record's own derivation, nothing written*.

#### Weak points the writing side fixed before putting this

- **The extra naming in Task 5.** The list proposes naming §L.38's point (3) separately in Task 5's bullet (its lines
  2686–2688). Not used, as under Rulings 16 to 18, 20 and 21: the rewritten point already reaches the close.
- **The check row.** The list's *To do* did not name the check row's *"§L.38 points (1) to (3)"* (line 20). Added below,
  for point (3).
- **The test the list leans on.** The list grounds the listing on *"the test (lix) to (lxi) set"* (its lines 2661–2662).
  (lix) and (lx) are not ruled (group 3 of entry 744 §2 item 4). Here the listing rests instead on Task 3 (c) item 4's
  own words and on the close, as Ruling 21 applied them.

#### The weak point, stated by the working list

The record's surface says of the L3 rows *"The application act re-marks them"* (surface line 113). That sentence stands
among the surface's facts (its §2), not its placements (its §3, which Ruling 1 ratified: *"the 15 row-parts' placements
RATIFIED as the surface states them"*), and the record carries the item as not decided. So it is read here as the
writing side's expectation, not an order. If you read it as an order, the act still has no word for the rows: RELOCATED
to L2 as proposed, or HISTORICAL following L2 Ruling 1, which the record established for Row 7.77's sentence only. The
word would then be a question for you. Documentation only either way.

#### Not read, not decided here

The L2 reading file and the L2 tonality-and-progression-terms record were not opened. The reading file's §10 was not
read, so whether it carries any of the eight is not stated. Whether the L3 proposals stand against L2 Ruling 1, and
whether L2's twins are amended, is left to a later ruling; this item decides neither. §L.38's *Open* points (1) and (2)
and §L.45's *Open* point (1) are not touched.

#### The currently decided method

Unchanged: the record's method [checked: its lines 52–58]. L2 decides key and chord together; its progression term is a
table of chord-to-chord pairs counted once from annotated music, so a longer progression is weighed one pair at a time;
DP-O stays open, the catalog among its unmeasured candidates. L3 publishes the cadence at each phrase end with its type,
the phrase and section grouping, the chord symbol, the figured bass, the harmonic rhythm, and the catalog matches once
the application act amends `FRAMEWORK.md`. The matcher is the same for every idiom; no preset chooses the catalog.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The act may not write in the L2 reading file, and no record gives the L3 rows a word, so
the act writes nothing for either set; the item stays open and reaches you at the close. Towards the objective, nothing
in the analysis changes, and the two differences are not lost from view: they stay in §L.38's point (3) and in your list
at the close. So the derivation is put for ratification, not as a menu. A heading of its own in the report is the one
variant, and it changes only where the item is printed.

**To do at release:** change §L.38's *Open* point (3) (dispatch lines 3304–3310), its check note's *"Points (1) to (3)
stand."* (line 3319) and the check row's *"Left for the releasing sitting: §L.38 points (1) to (3)"* (line 20), for
point (3), to point to the ruling; change the working list's (lxii) *To do at release* (its lines 2685–2688) to point to
the ruling, its proposed Task 5 naming not used; former wordings kept.

### Item (lxix) — carry list §9 points 1 to 4: how they come back to the user

*Added by the sitting booted on entry 751.*

#### What the question is, from scratch

Four of the points the L3 ruling records leave open are worded as coming back to the user *with* or *by* the
application act, not before it. The carry list (`ratification_surfaces/cowork_l3_application_carry_list_2026_11_08.md`)
names them as its §9 points 1 to 4 (its lines 205–209) [checked], each read here at its record [checked]:

1. **Feature (3)'s wording** (one of the six features a cadence is read from, *"the tonality before the phrase"*):
   *"For the application act to bring back to the user."* (cadence-features record, lines 79–81).
2. **The highest-pitch rewording of IC-L1 S-50** (the L1 interface contract's list of published facts gains the
   highest sounding pitch per slice): *"the rewording is the application dispatch's act"*, *"brought back to the user
   with it"* (the same record, lines 104–105).
3. **The phrase-boundary sentence's exact text** (the charter's sentence on where a phrase's boundaries come from): *"its
   exact text is not ruled by this record and comes to the user with that act"* (phrase-ends record, lines 110–111).
4. **One cadence type per vocabulary** (how to read the charter's singular *"the cadence at each phrase end, with its
   type"*): *"this side's reading, not ruled; for the application act to bring back to the user"* (cadence-type record,
   lines 67–68).

The application-surface record (`cowork_rulings_2026_11_08_l3_application_surface_sitting.md`, its sitting booted on
entry 601), read whole [checked], leaves one thing open about them, at its §2a (lines 62–63): *"The carry list §9 points
1 to 4 come back to the user with or by the application act (the surface §3); whether on one surface or one at a time is
written nowhere this sitting read."* Its surface (`ratification_surfaces/cowork_l3_application_dispatch_surface_2026_11_08.md`),
read whole [checked], says the same at its §3 (lines 142–143).

**What the dispatch writes now** [checked]. §L.54's *Open* point (1) (lines 4786–4789) quotes §2a and says that how the
points *"are then put to him is not fixed by this record"*. Its check note ends *"how the points are then put to the
user is fixed by no Task, and the point stands"* (line 4797), and the check row leaves *"§L.54 point (1)"* to the
releasing sitting (line 20, found by a bounded search).

So the question is: does the release add anything to the dispatch for these four points, and where and how do they
come back to you?

#### What the record already says

**What the act does with each point is already written, and agrees with the records** [checked]. The head block: the
four *"are written by this act where the records say and listed in its report for the user. They are not yours to
settle."* (lines 47–49). Point 1: the act writes nothing at feature (3) and *"lists it in its report"* (§L.5, lines
546–548). Point 2: the act writes the record's words at S-50 and lists the item for the user (§L.5, lines 539–544; Task
4's *"Also listed for the user, as **written**"*, lines 5425–5426). Point 3: a STOP-and-report, listed under *charter
and contract amendments left to the user* (Task 4's *Not written* list, heading at line 5404, item 1 at lines
5409–5410). Point 4: nothing written, listed there too (§L.6, lines 614–618; Task 4's item 7, line 5423). Points 1 to 3
concern a wording the act writes or stops on, which can be put only once the act has run (the surface's §3, lines
138–139), and the records say *with* or *by* the act (the carry list's §11, lines 235–236). So nothing needs adding to
the dispatch for the points themselves.

**Where they come back: the ratification act, by the route ruling** [checked]. The route ruling (the user's word *"A"*,
2026-11-02) has three steps, the third *"The ratification act over that new file, its granularity decided first."*
(route record line 62; the dispatch's §L.1 names the step at line 270). Task 5's close names it as the place: *"the
ratification act is a separate decision surface over the successor … where the points above return"* (lines
5522–5524). So *"one surface or one at a time"* is a question of that act's granularity, which by the route ruling is
decided first, at that act, after this one. Neither §2a nor the surface's §3 cites step 3 for this point, though the
surface's sitting read the route record whole (its provenance, line 167).

**How they are put then is the user's standing form, not a new choice.** A self-contained surface in its own turn, each
point said to be documentation only or an algorithm change; the choice questions in later turns, one decision per turn,
no widget; where the record already settles a point, say so rather than ask (entry 665 §3 step 3, lines 53–55 [checked];
that it restates the user's rulings of 2026-08-17 and 2026-08-21 relayed from the list). So each of the four is put by
itself in any case; what is left, whether they share one surface file with the ratification act's other points, is that
act's granularity.

**No release ruling answers it** [checked]. A search of the two release ruling records of 2026-11-11 for *"§L.54"*, *"§9
point"*, *"granularity"*, *"feature (3)"* and *"ratification act"* meets only the last, at the part 1 record's lines 206,
212 and 238 (seen as the search returned them), on the catalog's final content and not on these points. A search of the
whole dispatch for *"ratification act"*, *"feature (3)"*, *"§9 point"* and *"carry list §9"* returns hits, each seen with
up to sixty characters either side; none of them, as seen, fixes how the four are put beyond the places above. The
section names §L.5, §L.6, §L.54, Task 4 and Task 5 rest on their headings, found by a search (lines 515, 583, 4745,
5270, 5460).

**No rows.** The site places no reading-file row, so form (b)'s two-record rule (Ruling 3) and §10 do not arise.

Applying D-599: the dispatch already writes and lists the four as the records say, and the route ruling sends *"one
surface or one at a time"* to the ratification act. What is put to the user is the ratification of that derivation.

#### The wording the writing side proposes

- **For the four points:** nothing is added to the dispatch; the act writes and lists them as §L.5, §L.6 and Task 4
  already say.
- **§L.54's *Open* point (1)** is rewritten to point to the ruling, naming the four points one by one and saying that
  they come back at the ratification act, its granularity decided first there, so that Task 5's restatement under *"The
  points that are not this batch's"* carries all four to the user by name.
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written*. No naming in Task 5's bullet is added (the list proposes none for this item).

#### Weak points the writing side fixed before putting this

- **Point 1 could miss the close.** §L.5 says the act lists feature (3)'s wording *"in its report"* (line 548) and names
  no report heading, while Task 5's close carries the report's lists *"under the report sections the Tasks name"* (lines
  5510–5514). The list notes this and does not act on it, saying point 1 *"stands in the report above the *plan lines*
  bullet"* (its lines 3139–3141); that bullet is one of the close's, as Task 5 item 2 writes it (lines 5506–5524),
  not a report section. Fixed by naming the four points one by one
  in the rewritten §L.54 point (1): that point is restated in the close under *"The points that are not this batch's"*
  (lines 5518–5521), so point 1 reaches the close whatever heading the report gives it.
- **A wrong line citation.** §L.54's check note says point 1 *"is listed in the report by §L.5 (lines 538–540)"* (line
  4796); at the dispatch the sentence is at lines 546–548, and lines 539–540 open point 2's paragraph. Corrected below,
  under the user's rule of 2026-09-22, as at Rulings 18 and 20.
- **The check row.** The list's *To do* did not name the check row's *"Left for the releasing sitting: §L.54 point
  (1)."* (line 20). Added below.
- **The test the list leans on.** The list grounds *"Not listed again"* on *"the test (lix) to (lxviii) set"* (its
  line 3134). Of those, (lix), (lx), (lxiii), (lxiv) and (lxviii) are not ruled (this file's "What this file does not yet
  carry"; the part 2 ruling record, read whole). Here the ground is instead that the dispatch already lists the four for
  the user (above) and that §L.54's point (1), pointing to the ruling, reaches the close, as Rulings 21 and 22 applied it.

#### The weak point, stated by the working list

That the route ruling's *"its granularity decided first"* covers how the four points are put, and that Task 5's *"the
points above return"* takes in all four, are the writing side's readings (list lines 3142–3145); the second is made firm
by the first fix above. If you want the four put on a surface of their own before the ratification act's other points,
that is a working-practice choice only: it files no documentation and changes no algorithm.

#### Not read, not decided here

IC-L1 and `FRAMEWORK.md`'s charter were not read. The wording of each of the four is not touched; each stays as its
record leaves it. Which report heading point 1 falls under is not fixed here. The rulings folder's listing names no L3
ratification-granularity record (a check of file names only). §L.54's other parts and carry list §9 points 5 to 9 are
not touched.

#### The currently decided method

Unchanged. The four points stand as their records leave them: feature (3)'s wording UNSETTLED (cadence-features record,
lines 78–81 [checked]); L1 publishes per slice the highest sounding pitch of its sounding set, under that name, S-50's
wording brought back (cadence-features Ruling 2, lines 97 and 103–105 [checked]); a phrase end may fall wherever the
evidence as a whole puts it, including at a cadence with no notated cue, the charter sentence's exact text unruled
(phrase-ends Ruling 2 [relayed from the list; lines 102–111 read]); every declared vocabulary's types are published side
by side, none principal, the charter's singular read as one type per vocabulary by the writing side, not ruled
(cadence-type record, lines 60–68 [checked]).

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The dispatch already writes and lists the four as the records say, and the route ruling
leaves *"one surface or one at a time"* to the ratification act, decided first there; the standing form puts each point
by itself in any case. So the release adds nothing for them, and the point reaches you at the close. Towards the
objective, nothing in the analysis changes, and the four stay in view: each is named in §L.54's point (1) and in your
list at the close. So the derivation is put for ratification, not as a menu. The one variant, a surface of their own
before the ratification act's other points, is a working-practice choice and changes only when they are put.

**To do at release:** change §L.54's *Open* point (1) (dispatch lines 4786–4789) to point to the ruling, naming the four
points; change its check note's *"how the points are then put to the user is fixed by no Task, and the point stands"*
(line 4797) and the check row's *"Left for the releasing sitting: §L.54 point (1)."* (line 20) to point to the ruling;
correct the check note's *"§L.5 (lines 538–540)"* (line 4796) to *"§L.5 (lines 546–548)"*; change the working list's
(lxix) *To do at release* (its lines 3153–3155) to point to the ruling; former wordings kept.

### Item (lxxii) — the DP-O note: where the catalog term is recorded, and whether this act writes it

*Added by the sitting booted on entry 752.*

#### What the question is, from scratch

DP-O is one of the framework's open design questions: whether harmony is read as a hierarchy (a tree) or as a flat
chain; `FRAMEWORK.md` leaves it *"open, and deliberately not foreclosed"*, adding that *"what chord follows what is
inside L2's charter"* (lines 895 and 901–902) [checked]. The catalog-key record
(`cowork_rulings_2026_11_06_l3_catalog_key_sitting.md`, its sitting booted on entry 540), read whole [checked], has two
rulings. Its Ruling 2 (the user's word *"yes"*) says that using the catalog of named progressions as evidence when L2
chooses chords *"is added to the DP-O note as a named candidate, beside the longer chord-to-chord memory, the
cadential-formula term, the sequence term and harmonic rhythm"*, and that this is *"Documentation only. Algorithm: no
change."* (record lines 64–72). The record names no file or line for *"the DP-O note"*, gives no further text, and says
its rulings *"edit no tracked document"* (its §4, line 95).

**What the dispatch writes now** [checked]. §L.29's *Open* point (3): *"The DP-O note: its site, its text and whether
this act writes it are not stated by the record. Until (2) and (3) are settled, those amendments are STOP-and-report."*
(lines 2514–2516). Its check note adds that a search of the Tasks finds the note nowhere in them, *"So as the Tasks
stand it reaches the report only as this entry's own STOP-and-report (Task 1 (c) item 6)"* (lines 2522–2525). The check
row says the same (*"Found while checking §L.29, not settled: …"*) and leaves *"§L.29 points (1) and (3)"* to the
releasing sitting (line 20, both found by a bounded search). Point (2), the three charter amendments, is settled by Task
4's *Not written* item 2 (lines 5411–5413), as the check note says.

So the question is: where is the catalog term's addition recorded, does this act write it anywhere, and how does the
point reach you?

#### What the record already says

**The site is the L2 nothing-from-L3 record's note** [checked]. The four candidates Ruling 2 names beside the catalog
term are exactly those of the section *"A note for whoever takes up DP-O — recorded on the user's instruction"* in
`cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md` (its lines 88–106): *"a longer chord-to-chord memory, a
cadential-formula term, or the sequence term"* (lines 97–98), and harmonic rhythm in its paragraph *"Added by Ruling
4:"* (lines 103–104). The catalog-key surface names that record's note as the one meant (*"Its recorded note for DP-O
names, as candidates to measure inside L2, …"*, lines 63–65; *"What the DP-O note does not say"*, line 76).

**Where the addition is recorded: in the catalog-key record itself** [checked]. The precedent is the note's own earlier
addition: Ruling 4 of the L2 record wrote *"Harmonic rhythm is added to the DP-O note above"* (line 166) in that record,
and the note carries it there. The catalog-key record states its addition whole in Ruling 2's bold sentence, with what
it changes and what travels with it (lines 64–81), and gives no other text. So the addition is on record now; no text
is needed and none is made up here.

**This act may write it at none of the places found** [checked]. Each place this sitting found for it is closed to
the act:

- the L2 successor (`cowork_derived_specification_l2_2026_10_10.md`), where the L2 application dispatch ordered the
  note quoted whole beside L2-S31: Task 4 says this act *"does not edit … `cowork_derived_specification_l2_2026_10_10.md`
  or IC-L2"* (lines 5432–5433);
- `FRAMEWORK.md`'s DP-O: the act edits that file *"at Edits 1 to 3 and their notes only"* (line 5430), and DP-O carries
  no list of candidate terms to join (lines 894–904);
- a ruling record is not edited by the act;
- the L3 successor: it would need words no record orders, and the standing bars exclude them (*"an amendment is the
  record's words placed, never this batch's"*, line 201 [relayed from Ruling 21; that line not read by this sitting]);
  the term is an L2 term in any case (Ruling 2 rates *"each competing reading"* in L2's choice of chords).

This is Ruling 21's case: a point at L2 the dispatch bars the act from writing. So point (3) leaves no amendment
STOP-and-report: none is ordered, and Task 1 (c) item 6 (lines 5066–5068) does not reach it. Nor does it belong under
Task 4's *charter and contract amendments left to the user*: the note is neither a charter nor an interface contract.

**What is left for you, and how it reaches you.** The L2 application dispatch's item 4 had the L2 record's note quoted
whole beside L2-S31 in the L2 successor, *"the record being its home either way"* (its lines 2276–2285) [checked at the
L2 dispatch; whether it was so written is relayed, the L2 successor not opened]. The note in the L2 record, as read
(lines 88–106), does not name the catalog term, so a copy made from it as that dispatch ordered (2026-10-10) would not
either; whether anything has updated the copy since was not checked. Neither the catalog-key record nor this dispatch
says whether that copy is brought up to date, or by which act. That is a point this act may not settle. With §L.29's
*Open* point (3) rewritten to point to the ruling, naming it, Task 5's full close restates it under *"The points that
are not this batch's"* (lines 5518–5521), and it reaches you there, as Rulings 21 to 23 have it.

**No release ruling answers it** [checked]. The part 2 ruling record, read whole, has no ruling on §L.29; a search of
the part 1 record for *"DP-O"*, *"§L.29"*, *"catalog term"* and *"catalog key"* meets *"DP-O"* and *"catalog term"* only
in its method sentences and on rows (its lines 166, 201–202, 235, 243 and 247, seen as the search returned them), not
on §L.29's point (3).

**No rows.** The site places no reading-file row, so form (b)'s two-record rule (Ruling 3) and §10 do not arise. A
search of the whole dispatch for *"DP-O note"*, *"takes up DP-O"* and *"catalog term"* (hits seen with up to sixty
characters either side) meets them at the check row (line 20), within §L.29 (lines 2456, 2484, 2486, 2515, 2522–2523,
2536), at lines 3261 and 3264, and at lines 4092 and 4114; none of them, as seen, writes the note. That lines 3261 and
3264 fall in §L.38 and lines 4092 and 4114 in §L.47 is relayed from the line ranges Rulings 22 and 11 give for those
entries; their headings were not seen.

Applying D-599: the record gives no site and no words, the addition is on record in the record itself, and each place
this sitting found for it is closed to the act. What is put to you is the ratification of that derivation.

#### The wording the writing side proposes

- **For the DP-O note:** nothing is written by this act, at any document.
- **§L.29's *Open* point (3)** is rewritten to point to the ruling: the DP-O note meant is the L2 nothing-from-L3
  record's; the catalog term's addition is recorded in the catalog-key record's Ruling 2, quoted; this act writes it
  nowhere; and the L2 successor's copy of the note, which does not name the term, is L2's to bring up to date, by an act
  not named here. Its sentence *"Until (2) and (3) are settled, those amendments are STOP-and-report"* then holds for
  point (2)'s amendments only, which Task 4's *Not written* item 2 already lists.
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written* (Task 3 (c) item 4), which is for a point a record answers. No naming in Task 5's bullet is added.

#### Weak points the writing side fixed before putting this

- **The test the list leans on.** The list grounds the listing on *"the test (lix) to (lxxi) set"* (its line 3349). Of
  those, (lix), (lx), (lxiii), (lxiv), (lxviii), (lxx) and (lxxi) are not ruled (this file's "What this file does not
  yet carry"; the part 2 ruling record, read whole). The ground here is instead Ruling 21's: a point at L2 the act is
  barred from, carried to you by its *Open* point and the close.
- **The extra Task 5 naming.** The list proposes naming the point in Task 5's bullet (its lines 3354–3355 and
  3371–3372). Not used, as at Rulings 21 to 23: §L.29's point (3), pointing to the ruling, is restated in the close.
- **Two passages of the check row, not one.** The list's *To do* names *"the check row's sentence on it (line 20)"*.
  The check row carries two: *"Found while checking §L.29, not settled: …"* and *"Left for the releasing sitting: …
  §L.29 points (1) and (3)."* Both are named below, the second for point (3) only.
- **The STOP-and-report sentence.** §L.29 point (3) ends *"Until (2) and (3) are settled, those amendments are
  STOP-and-report"*. Settling (3) as *no amendment* leaves that sentence for (2)'s amendments only; the rewrite says so,
  so the act does not look for a DP-O amendment to stop on.

#### The weak point, stated by the working list

That *"the DP-O note"* Ruling 2 means is the L2 record's note, and not a new note in L3's own documents, is the writing
side's reading. It rests on the catalog-key surface's naming of that note and on the four candidates Ruling 2 lists
beside the catalog term, which are that note's (list lines 3359–3363). If you want the addition written somewhere by
this act, the home this sitting finds open to it is the L3 successor, with words you supply at release; that would file documentation
only and change no algorithm.

#### Not read, not decided here

The L2 successor was not opened; whether its copy of the note was written as the L2 dispatch's item 4 ordered, and
whether it names the catalog term, is relayed from the list. Whether a later L2 act brings that copy up to date, and
which, is not decided here. §L.29's *Open* point (1) (the list's (lxx), not ruled) and point (2) are not touched. The
catalog-key surface was read at lines 60–77 only.

#### The currently decided method

Unchanged. As Ruling 2 states it (record lines 72–75) [checked]: L2 decides key and chord together; its progression term
is a table of chord-to-chord pairs counted once from annotated music, so a progression longer than two chords is weighed
link by link, not whole; DP-O stays open, its named candidates (the longer chord-to-chord memory, the cadential-formula
term, the sequence term, harmonic rhythm and the catalog term) unmeasured and unadopted; adopting a catalog term after a
measurement would be its own ruling.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The record gives no site and no words; the addition is on record in its Ruling 2, as the
note's earlier addition is in its own record; and each place this sitting found for it is closed to the act. So
the act writes nothing, and the point reaches you at the close, named. Towards the objective, nothing in the analysis
changes, and the candidate stays in view for whoever takes up DP-O: it is on record, and the stale L2 copy is named for
you. So the derivation is put for ratification, not as a menu. The one variant, words of yours placed in the L3
successor at release, files documentation only.

**To do at release:** change §L.29's *Open* point (3) (dispatch lines 2514–2516) to point to the ruling, as worded
above; change its check note's *"Found, not settled"* passage (lines 2522–2525), the check row's *"Found while checking
§L.29, not settled: …"* passage and its *"Left for the releasing sitting: … §L.29 points (1) and (3)."* (line 20), for
point (3), to point to the ruling; change the working list's (lxxii) *To do at release* (its lines 3369–3372) to point to
the ruling, its proposed Task 5 naming not used; former wordings kept.

### Item (lxxiv) — the phase-definition surface's amendment: whether this act carries it

*Added by the sitting booted on entry 753.*

#### What the question is, from scratch

The research-registry record (`records/cowork/rulings/cowork_rulings_2026_11_03_research_registry_sitting.md`, its
sitting booted on entry 492), read whole [checked], is not an L3 family record. It rules on the order of work only: the
user's research registry is the main input to the research iteration ruled on 2026-10-07, which comes after the last
layer's detail specification is ratified and before the measurement-design phase opens. It says of itself *"It files a
plan only: it changes no specification and no algorithm as any specification defines it."* (record lines 4–5). Among
what it does not do, its §2 hands on one sentence: *"Whether the phase-definition surface's text is amended to name the
step is left to the application act; this record and the 2026-10-07 record are the step's home until then."* (record
lines 89–90). The phase-definition surface is the document that defines the project's phases; the record names neither
which application act it means nor any words for the amendment.

**What the dispatch writes now** [checked]. §L.10 enters the record *"because of one sentence and for no other reason"*
(dispatch line 815) and gives it no amendment, charter, contract, row or register work (lines 817–818). Its note
*"Open, for the releasing sitting:"* reads: *"the record does not say which application act it means, and the
phase-definition surface is not an L3 document. Whether this dispatch carries that amendment is to be checked at the
carry list before release (the carry list not read by the sitting that wrote this entry). If the carry list does not
name it, this entry orders nothing and the sentence stays with the record."* (lines 823–826). The check row says the
note stands, *"the carry list not read by this sitting either"* (line 20, found by a bounded search).

So the question is: does this act write the amendment, and how does the point reach you?

#### What the record already says

**The carry list does not name it** [checked]. The carry list
(`ratification_surfaces/cowork_l3_application_carry_list_2026_11_08.md`), read whole, has no item for the
phase-definition surface or the research registry, and a search of it for *"phase-definition"*, *"phase definition"*,
*"registry"* and *"research"*, in any case, returns no hit. Its own method accounts for that: it searched *"every L3
ruling record in `records/cowork/rulings/` dated 2026-11-02 to 2026-11-08 (the file names carrying `l3_`)"* (carry list
lines 16–17), and the research-registry record's file name carries no `l3_`, as §L.10 says (line 815). So the condition
§L.10's note sets is met, and by the note's own words the entry orders nothing.

**The write set excludes the surface either way** [checked]. *"The landed paths of Task 0, the successor, the
derivation's banner, the reading file's additions, the four `FRAMEWORK.md` sites, S-50, the Task-5 files and the report
are the whole write set."* (*What this batch does NOT do*, lines 5556–5558, its heading at line 5544 found by a search).
The phase-definition surface is none of these. So this act may not write the amendment, whichever application act the
record means; the question which act it means need not be settled for this act.

**No other place the search meets carries it** [checked]. A search of the whole dispatch for *"phase-definition"*,
*"research registry"*, *"research-registry"* and *"§L.10"*, in any case, with up to sixty characters either side of each
hit, meets them at line 14 and the check row (line 20), both seen only as the search returned them; at line 253, in
§L's opening (read at lines 248–257; the heading *"§L — The ledger"* at line 230 found by a search), which cites §L.10's
precedent for not entering two other records; within §L.10 (lines 807, 811, 820, 823); and at line 2447 (read at lines
2444–2449), which quotes another record's *"The four statements stand open to the research iteration (research-registry
Ruling 1 of 2026-11-03)"* and settles nothing. None of them, as seen, orders an edit to the phase-definition surface.

**The step keeps its home.** The record names the step's home until any amendment: *"this record and the 2026-10-07
record"*. Nothing here changes that.

**How it reaches you.** The record leaves open whether the surface is amended, handing that to an act it does not
name, and this act may not write it. That is the case of Rulings 21 and 24 (a point the dispatch bars the act from
writing, carried to you by its *Open* note and the close). It is not a point *answered by a record's own derivation*
(Task 3 (c) item 4), for the record derives no answer; nor an *amendment with no words from the record*, for the record
orders no amendment, it leaves open whether one is made; nor a *charter and contract amendment left to the user*, for
the surface is neither. With §L.10's *Open* note rewritten to point to the ruling, Task 5's full close restates every §L
entry's *Open* points under *"The points that are not this batch's"* (lines 5518–5521, under Task 5's heading at line
5460, found by a search), and it reaches you there, as Rulings 21 to 24 have it.

**No release ruling answers it** [checked]. The part 2 ruling record, read whole, has no ruling on §L.10; a search of
the part 1 release record for *"§L.10"*, *"phase-definition"*, *"phase definition"* and *"research registry"* (either
spelling), in any case, returns no hit.

**No rows.** The site places no reading-file row, so form (b)'s two-record rule (Ruling 3) and §10 do not arise.

Applying D-599: the carry list does not name the amendment, the write set excludes the surface, and the record gives no
words. What is put to you is the ratification of that derivation.

#### The wording the writing side proposes

- **For the phase-definition surface:** nothing is written by this act; nothing is added to the dispatch for it.
- **§L.10's *Open* note** is rewritten to point to the ruling: the carry list does not name the amendment, so by the
  note's own condition the entry orders nothing; the write set excludes the surface whichever act the record means; the
  record's sentence (record lines 89–90) is quoted whole, the step's home staying with that record and the 2026-10-07
  record.
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written*. No naming in Task 5's bullet is added.

#### Weak points the writing side fixed before putting this

- **The test the list leans on.** The list grounds the listing on *"the test (lix) to (lxxii) set"* (its line 3494). Of
  those, (lix), (lx), (lxiii), (lxiv), (lxviii), (lxx) and (lxxi) are not ruled (this file's "What this file does not
  yet carry"; the part 2 ruling record, read whole). The ground here is instead that of Rulings 21 and 24, which the
  list's *"(lxi)'s and (lxxii)'s case"* (its line 3497) now names as ruled.
- **The extra Task 5 naming.** The list proposes naming §L.10's note in Task 5's bullet *"so that pointing §L.10's
  *Open* note here does not drop it"* (its lines 3500–3502 and 3516–3518). Not used, as at Rulings 21 to 24: the note,
  pointing to the ruling, is restated in the close with the other *Open* points.

#### The weak point, stated by the working list

That which application act the record means need not be settled before release is the writing side's reading, resting
on the write set, which excludes the surface either way (list lines 3504–3508). One reading of the writing side's
besides: §L.10's note is headed *"Open, for the releasing sitting:"* and is not numbered, and that Task 5's *"every §L
entry's *Open* points"* takes it in is this side's reading of the close. If you read the record's sentence as meaning
this act and want the amendment made by it, the dispatch would need the surface added to its write set and words for
the amendment, which the record does not give (it says only *"to name the step"*). That would file documentation only.

#### Not read, not decided here

The phase-definition surface and the 2026-10-07 research-iteration record were not opened. Which application act the
record means is not decided here. What the record carries as *"Still UNSETTLED"* (the form of the main pass's snapshot;
whether the 2026-08-30 bar on the workbook is touched; record lines 68–70), which §L.10 says the batch settles nothing
of (dispatch lines 828–830), is not touched.

#### The currently decided method

Unchanged. As the record states it (its lines 86–88) [checked]: the phase order detail specifications → research
iteration (2026-10-07) → measurement design → audit → fix plan; L3's method is `FRAMEWORK.md` §5's L3 block with DP-I
(*"split — cues at L1, type at L3"*).

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The carry list does not name the amendment, so §L.10's own condition orders nothing; the
write set excludes the surface; and the record gives no words. So the act writes nothing, and the point reaches you at
the close, with the record's sentence. Towards the objective, nothing in the analysis changes, and the step stays on
record in its two homes. So the derivation is put for ratification, not as a menu. The one variant, the surface added to
the write set with words of yours, files documentation only.

**To do at release:** change §L.10's *Open* note (dispatch lines 823–826) and the check row's *"its *Open* note stands
(the carry list not read by this sitting either)"* (line 20) to point to the ruling, as worded above; change the
working list's (lxxiv) *To do at release* (its lines 3514–3518) to point to the ruling, its proposed Task 5 naming not
used; former wordings kept.

---

## Site 16 — Group 3, the reading file's §9 points, nothing written at §9: items (lix), points 2 and 8, and (lx), point 1

*(Former heading, kept: "… nothing written at §9: item (lix), points 2 and 8". (lx) added.)*

*Added by the sitting booted on entry 754.* The third group site, on the user's ruling of 2026-11-11 (*"As many as will
fit in sessions."*, entry 744 §2 item 3). Group 3 is the items on the L3 reading file's §9 where nothing is written at
§9, as entry 744 §2 item 4 sorted them from the list's headings alone: (lix), points 2 and 8, at list line 2498, and
(lx), point 1, at list line 2540 [both lines checked by this sitting]. Entry 744 says the group *"Could join group 2"*;
group 2 is complete without it (Rulings 21 to 25), so it is a site of its own. They are taken in list order. The sitting
booted on entry 754 added (lix), and the sitting booted on entry 755 added (lx), its line checked by that sitting; with
(lx), group 3 is complete. *(Former wording, kept: "The sitting booted on entry 754 added (lix); (lx) is named in "What
this file does not yet carry", for a later sitting to add here.")*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles which of the
reading file's §9 points the act's report lists under *points answered by a record's own derivation, nothing written*:
not points 2 and 8, whose answers you have ruled; point 1, whose answer is a record's own derivation, beside point 5.
And how the dispatch's notes on them read. Nothing about what the analysis does. *(Former wording, kept: "It settles
whether the act's report lists §9 points the user has already answered, and how the dispatch's note on them reads."
(lx) added.)*

### Item (lix) — the reading file's §9 points 2 and 8

*Added by the sitting booted on entry 754.*

#### What the question is, from scratch

The L3 reading file (`ratification_surfaces/cowork_comparison_l3_reading.md`) has a §9 [checked: lines 78856–78923].
It quotes the blind derivation's §7, eight places where the brief's split of L3's work into "faces" *"seemed wrong or
incomplete"*, each followed by one sentence on what the old documents say to it, and *"No verdict is given on whether
the derivation's §7 is right."* (line 78862). Two of the eight are this item's:

> Point 2: *"Faces (b) and (c) share an unnamed object: the alignment of the cadential arrival to the phrase end."*
> (lines 78875–78877) — in plain words: where the cadence arrives and where the phrase ends need not be the same chord.

> Point 8: *"The charter's sentence on phrase boundaries meets a hard case at elided cadences (OQ-L3-3 ★). The faces do
> not anticipate a phrase end with no notated cue."* (lines 78920–78921) — in plain words: a phrase can end where the
> page marks nothing, which the charter's wording does not allow for.

**What the dispatch writes now** [checked]. §L.3, the phrase-units record's entry, has a note (lines 448–452): item b
names §9 point 2, item j answers §9 point 8, *"No form above writes a line at the reading file's §9, so nothing is
written there for either. **Open, for the releasing sitting:** Task 3 item 4 lists the reading file's §9 point 5 for the
user (§L.18); whether these two points are listed the same way is not fixed by this dispatch."* The check row records
that note as added *"with an *Open* point for the releasing sitting"* (line 20, found by a bounded search).

Task 3 (c) item 4 (lines 5201–5203) is the listing that note means: §9 point 5 is answered by the harmonic-rhythm
record's own derivation, *"No form writes at §9 and nothing is written there. The record's sentence is listed in the
report for the user under *points answered by a record's own derivation, nothing written*."*

So the question: are points 2 and 8 listed under that report heading, as point 5 is?

#### What the record already says

**You have ruled both answers.** The phrase-units record (`cowork_rulings_2026_11_02_l3_phrase_units_sitting.md`, its
sitting booted on entry 482), read whole [checked], names *"the reading file's §9 points 2 and 8"* among what was put
(§0, line 16). Its Ruling 2 (your word *"yes"*, lines 75–79) ratifies items a to k as derivations, among them:

> **b.** Row 8.84 (i) and §9 point 2 — the cadential arrival (L3-S10) is not held to a fixed window; … Algorithm:
> changes against the old text. (lines 86–90)

> **j.** §9 point 8 answered by Ruling 2 of the morning's record; L3-S11 and L3-S13 have no DIFFERS rows and stand as
> derived until ratified with their statements. (lines 112–113)

*"The morning's record"* is the phrase-ends record of the same day (`cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md`,
its sitting booted on entry 481 [checked: its line 3–4]), whose Ruling 2 (your word *"yes"*, line 96) reads: *"A phrase
end may fall wherever the evidence as a whole puts it, including at a cadence with no notated cue"* (line 98), the case
point 8 names.

**Point 5 is different** [checked]. The harmonic-rhythm record (`cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md`)
answers it at its §2, headed *"Settled by the record — this side's derivation, not a ruling (documentation only)"*
(line 55): *"§9 point 5 is answered by L3-S30."* (line 74). The dispatch carries that answer as *"not ruled;
challengeable"* (§L.18's amendment 2, lines 1481–1483). So item 4 brings back to you an answer you have not ratified.
Points 2 and 8 carry answers you have ratified; listing them under that heading would describe them as unruled. This
agrees with how Rulings 21 and 22 read item 4: a heading for a point a record answers by its own derivation.

**Where the answers already reach the successor** [checked]. Item b is quoted whole, its *"§9 point 2"* included,
beside L3-S10 by §L.3's amendment 3 (lines 376–377). Item j's first clause is not among §L.3's amendments (amendment 6
quotes its second clause only, lines 382–383), but the answer it names is written at OQ-L3-3 by §L.2's amendment 3,
*"OQ-L3-3 ANSWERED (Ruling 2)"*, with phrase-ends Ruling 2's bold sentence (lines 297–299). No form writes at §9, as §L.3's
note says.

**No later ruling answers it.** The part 2 ruling record, read whole [checked], names (lix) within Rulings 21 to 25
only, each saying the list's ground there is not relied on or not ruled. A search of the part 1 release ruling record
for *"§9 point"*, *"phrase-units"*, *"§L.3"*, *"item 4"*, *"Part B"* and *"B7"* meets one line, on another record's Part
B (its line 204), and nothing on this point [checked].

**No rows.** The item places no reading-file row, so form (b)'s two-record rule (Ruling 3) and §10 do not arise.

Applying D-599: your rulings answer both points, item 4 is for answers you have not ruled, and nothing is written at §9.
What is put to you is the ratification of that derivation.

#### The wording the writing side proposes

- **At §9:** nothing is written for points 2 and 8; no form writes there.
- **In the report:** points 2 and 8 are not listed under *points answered by a record's own derivation, nothing written*.
- **§L.3's *Open* point on §9** (dispatch lines 451–452) is rewritten to point to the ruling: both points answered by
  rulings you gave (phrase-units Ruling 2, items b and j; phrase-ends Ruling 2), their answers carried into the successor
  by §L.3's amendment 3 and §L.2's amendment 3, nothing written at §9, not listed under item 4. Like every §L entry's
  *Open* points, the rewritten note is restated in Task 5's full close under *"The points that are not this batch's"*
  (dispatch lines 5518–5521); no listing of its own.

#### Weak points the writing side fixed before putting this

- **The check row.** The list's *To do* (its lines 2534–2535) names §L.3's note only. The check row's *"with an *Open*
  point for the releasing sitting"* (line 20) is added below.
- **The list's own *To do*.** The list does not say its own (lix) *To do* is to point to the ruling, as Rulings 21 to 25
  had for their items; added below.
- **Where the points still reach you.** The list says *"the report needs no list entry for either point"*. True for item
  4's heading; but the rewritten note itself is restated at the close, as every *Open* point is. Said so in the wording
  above, so it is not read as the points vanishing.

#### The weak point, stated by the working list

Item 4's heading is the writing side's wording (the list's B7, at its line 4120, naming Task 3 (c) items 1 to 6; the
list's Part B heading was not read). If you read *"a record's own derivation"* as also covering a derivation you have ratified, points 2 and
8 go into that list with point 5. Documentation only either way.

#### Not read, not decided here

The blind derivation's §7, and L3-S10 and OQ-L3-3 at the derivation, were not read. Item (lx), §9 point 1, is not decided
here; §L.19's check note (dispatch line 1643) and the check row's §L.19 passage, which call §9 point 1's listing *"the
same question as §L.3's"* note, are for (lx). §L.3's other parts and amendments are not touched.

#### The currently decided method

Unchanged, as the records state it [checked: phrase-units record lines 47–48 and 86–90; phrase-ends record line 98]. The
phrase reading tiles the working span with phrases and the stretches between them, each unit carrying its kind
(phrase-units Ruling 1); the cadential arrival is not held to a fixed window (item b); a phrase end may fall wherever the
evidence as a whole puts it, including at a cadence with no notated cue, the charter's sentence to be reworded by the
application act (phrase-ends Ruling 2).

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. You have ruled both answers, so listing them under a heading for unruled answers would
misdescribe them; and no form writes at §9. Towards the objective, nothing in the analysis changes, and both answers
stand in the successor. So the derivation is put for ratification, not as a menu. The one variant, both points listed
with point 5, changes only where they are printed in the report.

**To do at release:** change §L.3's *Open* point on §9 (dispatch lines 451–452) and the check row's *"with an *Open*
point for the releasing sitting"* (line 20) to point to the ruling, as worded above; change the working list's (lix)
*To do at release* (its lines 2534–2535) to point to the ruling; former wordings kept.

### Item (lx) — the reading file's §9 point 1

*Added by the sitting booted on entry 755.*

#### What the question is, from scratch

The L3 reading file's §9 (see item (lix) above) has a point 1 [checked: lines 78864–78871]:

> Point 1: *"Views and decisions are mixed across the faces."* … *"a view's mass is a sum over L2's readings (L3-S34),
> and a decision's mass composes L2's rivals with L3's own model (L3-S35)."* (lines 78866–78869) — in plain words: some
> of L3's outputs are views read straight off L2's readings and others are L3's own decisions, and the mass of each is
> formed differently.

§9's sentence on it (line 78871) ends: none of the twelve rows a search found *"names the mass of a view as a sum over
the readings it is read off"*.

**What the dispatch writes now** [checked]. §L.19, the mass-and-status record's entry, *Open* point (3) (lines
1630–1632): *"The reading file's §9 point 1: §2 (g) answers it, and §2 (g) is not among the items Ruling 2 ratifies, so
the answer stands as this side's derivation. As at §L.18's *Open* point (1), no form above writes a line at the reading
file's §9."* Its check note (lines 1642–1644): *"Point (3): no form writes at the reading file's §9, so nothing is
written for §9 point 1. Task 3 (c) item 4 lists only §9 point 5 in the report; whether §9 point 1 is listed the same way
is the same question as §L.3's *Open* note on §9 points 2 and 8, and stands with it."* The check row (line 20, found by
a bounded search) records it as *"point (3) nothing written, its report listing the same question as §L.3's §9 note."*

Task 3 (c) item 4 (lines 5201–5203) lists §9 point 5 under *points answered by a record's own derivation, nothing
written*; Task 5's close names that report section (lines 5510–5512).

So the question: is point 1 listed under that heading, as point 5 is?

#### What the record already says

**The answer is the record's own derivation, not a ruling** [checked: the record read whole]. The mass-and-status
record (`cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md`, its sitting booted on entry 502) names the point among
what was put (§0, lines 12–14). It answers it at its §2, headed *"Settled by the record — this side's derivation, not a
ruling (documentation only); challengeable at the rows"* (line 50), item (g) (lines 78–80): *"§9 point 1 is answered by
the split between L3-S34 (a view's mass a sum over L2's readings) and L3-S35 (a decision's mass composes L2's rivals
with L3's model); none of the twelve rows the reading file's search found names a view's mass as such a sum."* Ruling 2
(your word *"yes"*, line 120) ratifies the five statements and *"With them, the row placements of §2 (a) to (e)"*
(lines 122–125); (g) is not among them. The questions put were Ruling 1's and Ruling 2's (lines 26–28 and 119–120).
§L.19's own paragraph says the same (dispatch lines 1565–1568).

**That is point 5's case, and Ruling 26 has drawn the line.** Point 5's answer is the harmonic-rhythm record's own
derivation, under a §2 headed *"Settled by the record — this side's derivation, not a ruling (documentation only)"*
(as §L.18 quotes it, dispatch lines 1469–1471), and item 4 lists it. Ruling 26 kept points 2 and 8 out of item 4 because
you ruled their answers: *"Task 3 (c) item 4's heading is for a point a record answers by its own derivation, as Rulings
21 and 22 read it"* (part 2 ruling record, line 1372). Point 1's answer is a record's own derivation, unratified, so
item 4 reaches it. Nothing is written at §9 (no form writes there).

**What is ratified and what is not.** L3-S34 and L3-S35 themselves are ratified by Ruling 2 (L3-S35 in Ruling 1's form,
both masses per rival). Only §2 (g)'s sentence linking them to §9 point 1 is not. Listing the sentence puts that link
before you; it reopens neither statement.

**No later ruling answers it.** The part 2 ruling record, read whole [checked], names *"(lx)"* only at Rulings 21, 22,
23 and 26: the first three say the list's ground there is not relied on or not ruled; Ruling 26 leaves §L.19's check
note and the check row's §L.19 passage to (lx). A search of the part 1 release record for *"§9 point"*, *"§L.19"*,
*"mass-and-status"*, *"item 4"*, *"§2 (g)"*, *"L3-S34"* and *"L3-S35"* meets nothing [checked].

**No rows.** The item places no reading-file row, so form (b)'s two-record rule (Ruling 3) and §10 do not arise.

Applying D-599: the record answers point 1 by its own derivation, item 4 lists such answers, and Ruling 26 has said
whose answers stay out. What is put to you is the ratification of that derivation.

#### The wording the writing side proposes

- **At §9:** nothing is written for point 1.
- **Task 3 (c) item 4** (dispatch lines 5201–5203): its heading becomes *"The reading file's §9 points 5 and 1 (§L.18
  *Open* point (1); §L.19 *Open* point (3))"*, and after its last sentence this is added:

  > §9 point 1 likewise: the mass-and-status record answers it by its own derivation, which its Ruling 2 does not
  > ratify (§2 (g): *"§9 point 1 is answered by the split between L3-S34 (a view's mass a sum over L2's readings) and
  > L3-S35 (a decision's mass composes L2's rivals with L3's model); none of the twelve rows the reading file's search
  > found names a view's mass as such a sum."*). Nothing is written at §9. The record's sentence is listed under the
  > same heading.

- **§L.19's *Open* point (3)** (its sentences at dispatch lines 1630–1632), **its check note's sentences on point (3)**
  (lines 1642–1644) and **the check row's §L.19 passage** *"point (3) nothing written, its report listing the same
  question as §L.3's §9 note"* (line 20) are rewritten to point to the ruling: point 1 listed under item 4 with §2 (g)'s
  sentence; nothing written at §9. Like every §L entry's *Open* points, the rewritten point is also restated in Task 5's
  full close under *"The points that are not this batch's"* (dispatch lines 5518–5521).

#### Weak points the writing side fixed before putting this

- **The words for item 4.** The list's *To do* says *"add the reading file's §9 point 1 with the record's §2 (g) sentence
  beside point 5"* and gives no words; worded above, (g) quoted whole.
- **The check row.** The list's *To do* names §L.19's point (3) and its check note only; the check row's §L.19 passage is
  added.
- **The list's own *To do*.** The list does not say its own (lx) *To do* is to point to the ruling; added below.
- **The list's ground.** The list rests on its own (lix) (*"(lix) found the list under item 4 to be for an answer the
  user has not ratified"*). (lix) is now Ruling 26; its words are used above, not the list's.
- **An ambiguous sentence at §L.19.** Its opening (dispatch line 1555), *"Two rulings, on L3-S32 to L3-S36 and the
  reading file's §9 point 1, and one block of derivations"*, can be read as a ruling on point 1. Narrowed at release to
  *"Two rulings, on L3-S32 to L3-S36, and one block of derivations, which also answers the reading file's §9 point 1"*,
  former wording kept. The rest of the sentence is not touched.

#### The weak point, stated by the working list

If you read Ruling 2's ratification of L3-S34 and L3-S35 as also settling that they answer §9 point 1, point 1 goes with
points 2 and 8 and is not listed. Item 4 is the writing side's wording: the list's B7 (its line 4120) names Task 3 (c)
items 1 to 6 under its Part B, *"the writing side's authored settlements, overrulable before Task 0"* (its heading, line
4107). Documentation only either way.

#### Not read, not decided here

The blind derivation's §7, and L3-S34 and L3-S35 at the derivation, were not read; nor were the twelve rows of §9's
search. §L.19's *Open* points (1) (Ruling 12) and (2) (answered by its check note) and §L.3's note (Ruling 26) are not
touched.

#### The currently decided method

Unchanged, as the record states it [checked: mass-and-status record lines 96–98 and 127–129]. Every L3 rival of an L3
decision is published with both masses, under distinct names: its mass given L2's principal reading (the conditional)
and its marginal mass over L2's published readings (the overall), with the unaccounted remainder published (Ruling 1);
L3's mass and status rules as L3-S32 to L3-S36 give them, the confidence contract's Class-M margins, max-normalised
strengths and squashed composites replaced, for L3, by the model's own distribution (Ruling 2).

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. Point 1's answer is a record's own derivation, which is what item 4 lists, and Ruling 26 has
already said the heading is for that. Towards the objective, nothing in the analysis changes; listing puts an unratified
link before you rather than letting it pass as settled. So the derivation is put for ratification, not as a menu. The
one variant, point 1 not listed (the weak point above), changes only what the report prints.

**To do at release:** in Task 3 (c) item 4 (dispatch lines 5201–5203), extend the heading and add the paragraph, as
worded above; change §L.19's *Open* point (3) (lines 1630–1632), its check note's sentences on point (3) (lines
1642–1644) and the check row's §L.19 passage (line 20) to point to the ruling; narrow §L.19's opening sentence (line
1555) as above; change the working list's (lx) *To do at release* (its lines 2569–2572) to point to the ruling; former
wordings kept.

---

## Site 17 — Group 4, the successor gains no statement from this act: items (lxx), §L.29's point (1), the catalog matches, and (lxxi), §L.34's point (4), the substituted member

*(Former heading, kept: "… from this act: item (lxx), §L.29's point (1), the catalog matches". (lxxi) added.)*

*Added by the sitting booted on entry 756.* The fourth group site, on the user's ruling of 2026-11-11 (*"As many as will
fit in sessions."*, entry 744 §2 item 3). Group 4 is the items where the amended L3 specification (the successor) gains
no statement from this act, as entry 744 §2 item 4 sorted them from the list's headings alone: (lxx), §L.29 (1), at list
line 3172, and (lxxi), §L.34 (4), at list line 3229 [both lines checked by this sitting]. They are taken in list order.
The sitting booted on entry 756 added (lxx), and the sitting booted on entry 757 added (lxxi), its line checked by that
sitting; with (lxxi), group 4 is complete. *(Former wording, kept: "The sitting booted on entry 756 added (lxx); (lxxi)
is named in "What this file does not yet carry", for a later sitting to add here.")*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles that this act
writes no statement in the successor for the new published facts two records add to what L3 publishes (the catalog
matches; the substituted member and its operation in each match), and how the dispatch carries each point to the user.
Nothing about what the analysis does. *(Former wording, kept: "It settles that this act writes no statement in the
successor for a new published fact a record adds to L3's charter, and how the dispatch carries the point to the user."
(lxxi) added.)*

### Item (lxx) — §L.29's point (1): does the successor gain a statement for the catalog matches?

*Added by the sitting booted on entry 756.*

#### What the question is, from scratch

The catalog-key record (`cowork_rulings_2026_11_06_l3_catalog_key_sitting.md`, its sitting booted on entry 540) is
the first of the catalog records in the dispatch's §L, at §L.29 (dispatch lines 2451–2538, its heading found by a
search). Its Ruling 1, an algorithm change you ratified on 2026-11-06, gives L3 a new published fact [checked: record
lines 32–35]:

> *"L3 publishes, as a read-off fact, which entries of the catalog of named progressions fit which stretches of L2's
> decided chords: per match, the entry's name and the stretch of decided chords it covers, overlapping matches all
> published."*

In plain words: when a known named progression from the catalog fits a stretch of the chords L2 decided, L3 says so,
naming the entry and the stretch.

Among what this act writes are the charter (`FRAMEWORK.md`, the ratified framework, at named sites) and the successor
(the derived L3 specification as amended). The record orders three charter amendments for the matches. The question is
about the successor.

**What the dispatch writes now** [checked]. §L.29's *Open* point (1) (lines 2511–2514): *"The successor: Ruling 1 gives
L3 a new published fact (the matches), and the record orders the framework's amendment only. Whether the successor also
gains a statement for it — as the key-areas record ordered for key areas (§L.13) — is not stated by this record; on the
writing side's reading it orders none, and whether a later catalog record does is met at its entry."* Its check note
(lines 2521–2522): *"Point (1) stands; §L.34 meets it again."* The check row (line 20, by a bounded search): *"Left for
the releasing sitting: §L.27 point (1) and part E's text; §L.28 point (1); §L.29 points (1) and (3)."*

So the question: does this act write a statement for the matches in the successor, and what becomes of point (1)?

#### What the record already says

**For the matches, the record orders the charter only** [checked: the record read whole; its Ruling 2, on the DP-O
note, is Ruling 24's and not this item's]. Ruling 1: *"The ratified framework is amended
at three places (the writing is the application act's)"* (line 37): the L3 *Consumes* line, the L3 *Publishes* line and
§3.2's last sentence (lines 38–45). It orders no text for the derivation or the successor; §L.29's *Successor* line says
the same (dispatch lines 2463–2465). What is still to be specified about the matches it leaves, in terms, to *"the
amendment and L3's detail design"*, under the words *"not decided here"* (record lines 53–60). Its §4: the rulings
*"edit no tracked document (the framework's amendment is the application act's)"* (lines 95–96).

**Position B, which Ruling 1 ratifies by name, puts the detail later** [checked: the record's surface,
`ratification_surfaces/cowork_l3_catalog_key_surface_2026_11_06.md`, lines 138–151]: *"A detail specification of the
matching follows in L3's detail-specification work."* (lines 150–151).

**Where a record wanted a statement, it said so** [checked: the carry list, lines 36–149]. The key-areas and
modal-counts records: *"the derivation to gain a statement for them"* (carry list §4 item 5, lines 113–114). The
bass-role record: *"the L3 charter's Publishes list (`FRAMEWORK.md` §5) and the amended L3 specification gain the item,
a new L3 statement being written there"* (§2 item 8, lines 61–63; §5, line 126). Each of those orders both the charter
amendment and the statement. The catalog-key record stands in the carry list's §2 (item 6, lines 55–58), the charter
list, and not in §4 item 5 or in §5's ruled statements.

**The act may not write one itself** [checked]. The standing bars: *"no derivation of any specification statement — an
amendment is the record's words placed, never this batch's"* (dispatch line 201). A statement for the matches would need
words no record gives.

**No later catalog record in the dispatch's §L orders one** [checked: a search of the dispatch for `^\*\*Successor`, each hit read with the
two lines after it, and the §L headings found by a search]. The *Successor* lines of §L.30 to §L.38, the catalog records
that follow §L.29 (lines 2551, 2643, 2725, 2816, 2898, 2979, 3058, 3165, 3249), each read *"no amendment"* or *"no
amendment ordered"*; several name the matches as published *"once the application act amends `FRAMEWORK.md`"*. §L.39
(line 3344) adds one statement, the chord-suggestion tool's: *"It may read L3's published matches and the same catalog
L3 reads"* (lines 3345–3346). It presupposes the matches and is not a statement for them. §L.34's *"See *Open* point
(4)"* (line 2898) is item (lxxi), not decided here.

**The new fact already reaches you** [checked: dispatch lines 5404–5413]. The three charter amendments carry no new text,
so each is a STOP-and-report under form (e), listed in the report under *charter and contract amendments left to the
user*: Task 4's *Not written* item 2, *"The catalog matches at three places"* (lines 5411–5413).

**How the point itself reaches you.** As Rulings 21 to 25 have it for points the act writes nothing for: §L.29's *Open*
point (1) is rewritten to point to the ruling, and Task 5's full close restates every §L entry's *Open* points under
*"The points that are not this batch's"* (dispatch lines 5518–5521). It is not listed under *points answered by a
record's own derivation, nothing written* (Task 3 (c) item 4): Ruling 26 reads that heading as *"for a point a record
answers by its own derivation"*, and what answers point (1) here is the record's ratified Ruling 1 and the standing bar,
not a derivation of the record's.

**No ruling of the two release records answers it** [checked]. The part 2 ruling record, read whole, names §L.29 in Ruling 19 (a line of
§L.29 cited for another row) and in Ruling 24 (point (3), the DP-O note), which says *"§L.29's *Open* points (1) and (2)
are not touched"*. A search of the part 1 release record for *"§L.29"*, *"catalog-key"*, *"catalog key"*, *"catalog
matches"*, *"successor gains"* and *"(lxx)"* meets two method sentences (its lines 167 and 248, seen as the search returned them),
neither on point (1).

**No rows.** The item places no reading-file row, so form (b)'s two-record rule (Ruling 3) and §10 do not arise.

Applying D-599: for the matches the record orders the charter only and leaves the matching's detail to later work, the bars forbid the
act to write words no record gives, and Rulings 21 to 25 fix how such a point reaches you. What is put to you is the
ratification of that derivation.

#### The wording the writing side proposes

- **In the successor:** no statement for the catalog matches is written by this act. Nothing is added to the dispatch
  for it.
- **§L.29's *Open* point (1)** (dispatch lines 2511–2514), **its check note's *"Point (1) stands"*** (line 2521), and
  **the check row's *"§L.29 points (1) and (3)"*** (line 20), for point (1), are rewritten to point to the ruling: for
  the matches the record orders the charter amendments only and leaves the matching's detail specification to *"the amendment and L3's
  detail design"* (record lines 53–60); the act writes no statement for the matches in the successor; the new fact
  reaches the user under Task 4's *Not written* item 2. The rewritten point reaches the user in Task 5's full close under
  *"The points that are not this batch's"* (lines 5518–5521).
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written*.

#### Weak points the writing side fixed before putting this

- **The check row.** The list's *To do* names §L.29's *Open* point (1) and its check note only; the check row's *"§L.29
  points (1) and (3)"*, for point (1), is added (Ruling 24 points it for point (3) only).
- **The list's own *To do*.** The list does not say its own (lxx) *To do* is to point to the ruling; added below.
- **The list's ground.** The list rests on *"the test (lix) to (lxix) set"* (its line 3201), items unruled when it was
  written. Rulings 21 to 26 are used above in its place, as Rulings 23 to 25 did with the same ground.
- **The weak point's comparison.** The list says that on the other reading the point would be a STOP-and-report *"as
  at (lxii)"* (its line 3209). (lxii) is now Ruling 22, which made its rows not STOP-and-report; the comparison is
  dropped below.

#### The weak point, stated by the working list

That *"L3's detail-specification work"* is a later act, and not this act's successor, is the writing side's reading
(the list's line 3206). If you read it as this act's successor, the successor would need a statement in words no record
gives, which the standing bars exclude. Either way this act writes no statement for the matches, and §L.29's point (1)
reaches you in Task 5's close. Documentation only either way.

#### Not read, not decided here

The L3 reading file was not opened; the item places no row. `FRAMEWORK.md` and the derivation were not read. §L.39's
statement was read at lines 3344–3346 only. §L.29's *Open* points (2) (settled by Task 4's *Not written* item 2, as its
check note says) and (3) (Ruling 24), and §L.34's *Open* point (4) (item (lxxi)), are not touched. Which of the
record's seven *"not decided here"* items the later detail work takes up is not decided here.

#### The currently decided method

Unchanged by this item. Ruling 1 of the catalog-key record is itself an algorithm change, ruled on 2026-11-06, not
decided here [checked: record lines 32–35]: L3 publishes, as a read-off fact, which catalog entries fit which stretches
of L2's decided chords, per match the entry's name and the stretch, overlapping matches all published; how a match is
shown to an end user, and whether a preset filters what is shown, is presentation, decided later and separately. Ruling
2's method [checked: record lines 72–75]: L2 decides key and chord together; its progression term is a table of
chord-to-chord pairs counted once from annotated music; DP-O stays open, the catalog term among its named candidates,
unmeasured and unadopted.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. No record gives words for a statement, and the bars forbid the act to write its own; so on
either reading of *"L3's detail-specification work"* the act writes nothing in the successor. Towards the objective,
nothing in the analysis changes; the new fact and the open point both reach you in the report. So the derivation is put
for ratification, not as a menu. The one variant, words of yours for a statement now, would be a ruling of its own and
an algorithm-level text, outside this item.

**To do at release:** change §L.29's *Open* point (1) (dispatch lines 2511–2514), its check note's *"Point (1) stands"*
(line 2521) and the check row's *"§L.29 points (1) and (3)"* (line 20), for point (1), to point to the ruling, as
worded above; change the working list's (lxx) *To do at release* (its lines 3219–3221) to point to the ruling; former
wordings kept.

### Item (lxxi) — §L.34's point (4): does the successor gain a statement for the substituted member and its operation, and are the charter's words given?

*Added by the sitting booted on entry 757.*

#### What the question is, from scratch

The substitution part 1 record (`cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md`, its sitting booted
on entry 547) is at the dispatch's §L.34 (dispatch lines 2882–2967, its heading found by a search). Its Ruling 1, an
algorithm change you ratified on 2026-11-06, adds to the catalog matches of item (lxx) [checked: record lines 28–32]:

> *"Where a named progression appears in the music with one of its chords replaced by a substitute, L3 recognises it as
> that progression, matched through the catalog's substitution mappings under the same exact test as any match (members
> in order and contiguously, nothing skipped or inserted), and the published match states, beside the entry's name and
> the stretch of decided chords, which member was filled by a substitute and by which operation. L2's chord and Roman
> numeral are unchanged."*

In plain words: when a named progression from the catalog appears with one of its chords replaced by a substitute the
catalog maps, L3 still recognises it, and the published match also says which chord of the progression was the
substitute and by which operation (the kind of substitution). L2's chord is not changed.

**What the dispatch writes now** [checked]. §L.34's *Open* point (4) (lines 2943–2945): *"The successor and the
charter: the ruling adds to what L3 publishes (the substituted member and its operation in each match). As at §L.29's
*Open* point (1), whether the successor gains a statement for it is not stated; and the charter's words are not given
(above)."* Its check note (line 2952): *"Points (1) to (4) stand."* The check row (line 20, by a bounded search):
*"Left for the releasing sitting: §L.34 points (1) to (4)"*.

The point has two halves. The successor half: does this act write a statement in the amended L3 specification (the
successor) for the substituted member and its operation? The charter half: the record gives no words for `FRAMEWORK.md`.
So the question: what does this act write for each half, and what becomes of point (4)?

#### What the record already says

**It orders no text for the successor** [checked: the record read whole]. Of where the method is written it says:
*"Where the application act writes it is that act's (surface §1.3, marked as this side's reading: with key Ruling 1's
amendment to the L3 *Publishes* line and §3.2)."* (record lines 40–41). Its §3: it *"edits no tracked document (the
framework's amendment is the application act's)"* (line 77). A search of the record for *"successor"* and
*"specification"*, in any case, meets nothing. §L.34's *Successor* line says the same: *"no amendment ordered. The record
orders no text for the derivation or the successor. See *Open* point (4)."* (dispatch line 2898). The record's surface
(`ratification_surfaces/cowork_l3_catalog_substitution_part1_surface_2026_11_06.md`, read at lines 100–144 and by a
search for *"successor"*, *"amended L3 specification"* and *"derived specification"*, in any case) places the writing
the same way: *"If B is ratified, the application act states it with key Ruling 1's amendment to the L3 *Publishes*
line and §3.2 **[my reading of where it is written]**"* (surface lines 135–137). That search meets *"the amended L3
specification"* once, at line 116, as where the catalog's final content is *"confirmed"*, not as where the method is
written.

**It names the carrier form as waiting** [checked]. Among what the record names as *"Not decided, named as waiting"*:
*"the carrier form"* (record line 52), which the surface gives as *"part 1 §3.2's (per match, or a non-tiling span
kind)"* (surface line 128). How a match carries the substituted member is itself open, so a statement written now would
decide a point the ruling names as waiting.

**Item (lxx), now Ruling 28, is the same case for the matches themselves** [checked: the part 2 ruling record, read
whole]. Ruling 28 ratified that the act writes no statement in the successor for the catalog matches: the catalog-key
record orders the charter amendments only; where a record wanted a statement it said so (carry list §4 item 5 and §2
item 8); the standing bars forbid words no record gives; the new fact reaches you under Task 4's *Not written* item 2.
It left §L.34's point (4) untouched, naming it item (lxxi).

**The carry list names this record in its charter list, at one line** [checked: a search of the whole carry list for
*"substitut"*, in any case, meets line 57 alone]. That line is in §2 item 6, the catalog matches' charter item:
*"Substitution part 1 lines 40–41: where the substitution matches are written "is that act's""* (lines 55–58). The record
is not in §4 item 5 (lines 113–114) or in §5's ruled statements (lines 116–130), read at those lines.

**The act may not write a statement itself** [checked]. The standing bars: *"no derivation of any specification
statement — an amendment is the record's words placed, never this batch's"* (dispatch line 201).

**No later catalog record in the dispatch's §L orders one** [checked: the search of the dispatch for `^\*\*Successor`,
each hit read with the two lines after it, and the §L headings found by a search]. The *Successor* lines of §L.35 to
§L.38 (lines 2979, 3058, 3165, 3249) each read *"no amendment"*. §L.39 (lines 3344–3346) adds the chord-suggestion tool's
statement, *"It may read L3's published matches and the same catalog L3 reads"*, which presupposes the matches and is
not a statement for them or for the substituted member; its other addition is a list for the notes, *"without adding
them to the specification itself"* (lines 3347–3351).

**The charter half is already settled by the dispatch** [checked]. Form (e): *"where the record gives no words, that
amendment is a STOP-and-report, the rest applied"* (lines 183–184). §L.34's own *Charter* paragraph: *"Under form (e),
STOP-and-report unless the Task supplies words as authored and overrulable."* (line 2906). Task 4 supplies none for the
matches: its Edit 1, at the L3 *Publishes* line, appends three other items, the form-function names, the key areas and
the pivot label (lines 5310–5315); its Edits 2 to 4 are at other sites (their headings, lines 5324, 5346 and 5373). Its
list headed *"Not written — listed in the report for the user, under *charter and contract amendments left to the user*"*
(line 5404) reads at item 2: *"The catalog matches at three places — the L3 *Consumes* line, the L3 *Publishes* line, and
§3.2's last sentence (§L.29, which says what is to change and gives no new text; §L.34 places the substitution matches'
writing with them). Carry list §2 item 6."* (lines 5411–5413). This is how §L.29's check note settled §L.29's point (2):
*"Point (2) is settled by Task 4 *Not written* item 2: no words, STOP-and-report, listed for the user."* (lines
2520–2521). So *"the charter's words are not given"* is answered by the dispatch as it stands: the act writes no charter
words for the substitution matches, and the item, §L.34 named in it, reaches you in the report.

**How the point itself reaches you.** As Rulings 21 to 25 and 28 have it for points the act writes nothing for: §L.34's
*Open* point (4) is rewritten to point to the ruling, and Task 5's full close restates every §L entry's *Open* points
under *"The points that are not this batch's"* (dispatch lines 5518–5521). It is not listed under *points answered by a
record's own derivation, nothing written* (Task 3 (c) item 4): Ruling 26 reads that heading as *"for a point a record
answers by its own derivation"*, and what answers point (4) is the record's ratified Ruling 1, Ruling 28, the standing
bar and Task 4's *Not written* item 2.

**No ruling of the two release records answers it** [checked]. The part 2 ruling record, read whole, names §L.34 in
Ruling 9 (its *Open* point (1), dispatch line 2939) and in Ruling 28 (*"§L.34's *Open* point (4) (item (lxxi)) are not
touched"*); a search of it for *"§L.34"*, *"(lxxi)"*, *"substitution part 1"* and *"substituted member"*, in any case,
meets those two places and Ruling 24's quotation of the list's *"the test (lix) to (lxxi) set"*. A search of the part 1
release record for *"§L.34"*, *"(lxxi)"*, *"substitut"* and *"successor gains"*, in any case, meets its lines 216, 218
and 223 (on rows that follow in part) and 249 (a method sentence naming *"any substituted member with its operation"* as
published once the application act amends `FRAMEWORK.md`), none on point (4).

**No rows.** The item places no reading-file row, so form (b)'s two-record rule (Ruling 3) and §10 do not arise.

Applying D-599: the record orders no successor text and leaves the carrier form waiting; the bars forbid the act to
write words no record gives; Ruling 28 settled the same question for the matches; the dispatch already lists the charter
item for you; and Rulings 21 to 25 and 28 fix how such a point reaches you. What is put to you is the ratification of
that derivation.

#### The wording the writing side proposes

- **In the successor:** no statement for the substituted member and its operation is written by this act. Nothing is
  added to the dispatch for it.
- **In the charter:** nothing beyond what the dispatch already does. Task 4's *Not written* item 2 stands as it is.
- **§L.34's *Open* point (4)** (dispatch lines 2943–2945), **its check note's *"Points (1) to (4) stand."*** (line 2952),
  and **the check row's *"Left for the releasing sitting: §L.34 points (1) to (4)"*** (line 20), for point (4), are
  rewritten to point to the ruling: the record orders no text for the successor and leaves the carrier form waiting; the
  act writes no statement for the substituted member and its operation in the successor, as Ruling 28 has it for the
  matches; the charter half is settled by Task 4's *Not written* item 2, which names §L.34. The rewritten point reaches
  you in Task 5's full close under *"The points that are not this batch's"* (lines 5518–5521).
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written*.

#### Weak points the writing side fixed before putting this

- **The check row.** The list's *To do* names §L.34's *Open* point (4) and its check note only; the check row's
  *"§L.34 points (1) to (4)"*, for point (4), is added.
- **The list's own *To do*.** The list does not say its own (lxxi) *To do* is to point to the ruling; added below.
- **The list's ground.** The list rests on *"the test (lix) to (lxx) set"* (its line 3276), items unruled when it was
  written. Rulings 21 to 26 and 28 are used above in its place.
- **The weak point's comparison.** The list says that on the other reading the point would be a STOP-and-report *"as
  at (lxii)"* (its line 3284). (lxii) is now Ruling 22, which made its rows not STOP-and-report; the comparison is
  dropped below.
- **What the list relayed from (lxx).** The list relayed from its unruled (lxx) that the record is in neither the carry
  list's §4 item 5 nor its §5. This sitting read those lines and uses Ruling 28 in place of (lxx).

#### The weak points, stated by the working list

(a) As at (lxx): that the later detail-specification work, and not this act's successor, is where the matching's
specification goes is the writing side's reading. If you read it as this act's successor, the successor would need a
statement in words no record gives, which the standing bars exclude. Either way this act writes no statement, and
§L.34's point (4) reaches you in Task 5's close. (b) The record itself marks the placement of the writing with key
Ruling 1's charter amendments as the surface's reading (*"marked as this side's reading"*), and Task 4's item 2,
*"§L.34 places the substitution matches' writing with them"*, rests on that. If you want the substituted member named as
a charter item of its own, that changes which item the report lists it under, not what the act writes, which is nothing
in either case. Documentation only either way.

#### Not read, not decided here

The L3 reading file was not opened; the item places no row. `FRAMEWORK.md` and the derivation were not read. The
catalog-key surface was not opened by this sitting; its position B is relayed from Ruling 28. The substitution part 1
surface was read at lines 100–144 and by the search named above. The *Successor* lines after §L.39 were seen only as
the search returned them, each with the two lines after it. Task 4's Edits 2 to 4 were seen at their headings only. §L.34's
*Open* points (1) (Ruling 9), (2) and (3) are not touched. Which of the record's waiting points the later detail work
takes up is not decided here.

#### The currently decided method

Unchanged by this item. Ruling 1 of the substitution part 1 record is itself an algorithm change, ruled on 2026-11-06,
not decided here [checked: record lines 28–32 and 36–40]: L3 recognises a named progression with one chord replaced by
a mapped substitute, under the same exact test as any match, and the published match states, beside the entry's name
and the stretch, which member was filled by a substitute and by which operation; L2's chord and Roman numeral are
unchanged. With it stands key Ruling 1's matches, as at (lxx) (Ruling 28): per match, the entry's name and the stretch
of decided chords, overlapping matches all published. No change to L2: L2 decides key and chord together, its
progression term a table of chord-to-chord pairs; DP-O stays open with the catalog term an unmeasured candidate.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. No record read here gives words for a statement, the record names the carrier form as waiting, and
the bars forbid the act to write its own; so on either reading of where the detail is specified the act writes nothing
in the successor. The charter half is already settled by the dispatch. Towards the objective, nothing in the analysis
changes; the new fact and the open point both reach you in the report. So the derivation is put for ratification, not as
a menu. The one variant, words of yours for a statement or a charter item now, would be a ruling of its own and an
algorithm-level text, outside this item.

**To do at release:** change §L.34's *Open* point (4) (dispatch lines 2943–2945), its check note's *"Points (1) to (4)
stand."* (line 2952) and the check row's *"Left for the releasing sitting: §L.34 points (1) to (4)"* (line 20), for
point (4), to point to the ruling, as worded above; change the working list's (lxxi) *To do at release* (its lines
3298–3300) to point to the ruling; former wordings kept.

---

## Site 18 — Group 5, L2 rows paired with L3 rows, nothing written for the L2 rows: items (lxiv), the language-model twins, and (lxviii), §L.50's point (3), the chord-as-degree rows

*(Former heading, kept: "… nothing written for the L2 rows: item (lxiv), the language-model twins". (lxviii) added.)*

*Added by the sitting booted on entry 758.* The fifth group site, on the user's ruling of 2026-11-11 (*"As many as will
fit in sessions."*, entry 744 §2 item 3). Group 5 is the items where an L2 row is paired with an L3 row and nothing is
written for the L2 row, as entry 744 §2 item 4 sorted them from the list's headings alone (*"L2 rows paired with L3
rows, nothing written, not listed"*): (lxiv), at list line 2753, and (lxviii), §L.17's eleven L2 rows, at list line 3027
[entry 744 line 63 checked by this sitting; list line 2753 checked; line 3027 relayed from entry 758 §3 step 2]. They
are taken in list order. The sitting booted on entry 758 added (lxiv), and the sitting booted on entry 759 added
(lxviii), its list line checked by that sitting; with (lxviii), group 5 is complete. *(Former wording, kept: "The
sitting booted on entry 758 added (lxiv); (lxviii) is named in "What this file does not yet carry", for a later sitting
to add here.")* The sort's *"not listed"* is from the headings; item (lxiv) below finds the
point reaches you in Task 5's close all the same, as Rulings 21 to 25, 28 and 29 have it.

**Documentation only. It does not change the algorithm as the specification defines it.** It settles that this act
writes nothing for the L2 rows of the pair, and how the dispatch carries the point to you. Nothing about what the
analysis does.

### Item (lxiv) — §L.45's point (1): the L2 twins ruled RELOCATED to L3 while their L3 rows are now HISTORICAL

#### What the question is, from scratch

Five passages in the old documents describe a language model, at run time in the finished product, being handed the
analysis as context: the sentence *"The LLM does not re-derive harmony from raw pitch data — it receives pre-digested
musical context."* (`ARCHITECTURE.md` §19.3), and four lines of `docs/llm_integration.md` listing what it is handed
(chord symbols; chord symbols and Roman numerals per measure; key and mode; where the chords change). Each passage has a
row in both reading files; at L3 the first is split into two claims.

- **At L2** they are Rows 36.1 and 54.1 to 54.4. You ruled all five **RELOCATED to *L3 — The read-off facts*** on
  2026-10-07, in Ruling 5 of the L2 nothing-from-L3 record (`cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md`),
  which placed 160 row-parts *"as the comparison proposed them"*, put as filing only and as not deciding L3's design
  (below).
- **At L3** the same sentences are Rows 57.124 (two claims, (i) and (ii)) and 57.498 to 57.501, six row-parts. You
  ruled all six **HISTORICAL — a superseded plan** on 2026-11-08, in Ruling 1 of the language-model family record
  (`cowork_rulings_2026_11_08_l3_language_model_family_sitting.md`), because the run-time language-model design they
  belong to was superseded by the test-only ruling of 2026-11-07.

That record's §2, under *"Carried, not decided by this ruling"*, says: *"The L2 twins (Rows 36.1, 54.1 to 54.4) were
ruled RELOCATED to L3 by nothing-from-L3 Ruling 5 **[relayed]**. This ruling decides nothing about L2."* (record lines
62–63) [checked: the record read whole].

**What the dispatch writes now** [checked]. §L.45 (dispatch lines 3891–3968; its heading found by a search, line 3891)
gives the six L3 row-parts their HISTORICAL line (its table, line 3914), and of the twins says: *"this act writes
nothing for them from this record, as at §L.37."* (lines 3937–3939). Its *Open* point (1) (lines 3941–3943): *"the L2
twins stand ruled RELOCATED to L3 while their L3 rows are now HISTORICAL; the record carries this and decides nothing
about L2 (its §2). Whether that pairing needs anything beyond the record's own carrying is not this act's."* Its check
note: *"a search of the whole dispatch for "§L.45" finds it in no Task; Task 1 (c), Task 3 (c) and Task 4's *Not
written* list do not settle it. Point (1) stands."* (lines 3957–3959). The check row (line 20, by a bounded search):
*"point (1) is settled by no Task. Left for the releasing sitting: §L.45 point (1)."*

So the question: does the pairing need anything written, at L2 or at L3, and what becomes of point (1)?

#### What the record already says

**The twins' ruling, read at the rows** [checked: the L2 reading file at Rows 36.1 (lines 47766–47777) and 54.1 to
54.4 (lines 72487–72539), each found by the row-heading search]. Each of the five carries the line *"RULED DISPOSITION
(cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md, Ruling 5). **RELOCATED to *L3 — The read-off facts*** — as
proposed (the surface's §A.5: "Readers of the published record")"* (lines 47777, 72497, 72511, 72525, 72539). Their
transfer-list entries stand at the L2 reading file's §10, lines 75670–75671 (Row 36.1) and 75838–75840 (Rows 54.1 to
54.4) [checked at those lines; the §10 heading above them relayed from the list, not read].

**How Ruling 5 was put** [checked: the nothing-from-L3 record, lines 181–198]: *"Stated with the question: filing only,
no change to L2's algorithm as its statements define it; and, as this side's reading, relocating a claim to L3 does not
decide L3's design."* (lines 186–188). Your word: *"confirmed"* (line 190). What is ruled: *"the 160 parts are placed as
the comparison proposed, unchanged."* (line 192).

**The L3 rows are the L2 relocation arriving at L3** [checked: the L3 reading file at Row 57.124 (lines 73527–73558)
and Row 57.498 (lines 75088–75116), read through, and Rows 57.499 to 57.501 at their first lines (75119–75124,
75150–75155, 75181–75186), each found by the row-heading search]. Each of the five L3 entries opens with *"The L2
entry."*, quoting its twin's §10 entry with the locator *"§10, lines 75670–75671"* (Row 57.124) or *"§10, lines
75838–75840"* (Rows 57.498 to 57.501). So the L3 row-parts exist because the L2 rows were relocated to L3, and the
language-model record's HISTORICAL is the L3 placement of exactly those sentences.

**So the two rulings do not conflict.** Ruling 5 was put as filing, and as not deciding L3's design; the language-model
record's Ruling 1 is L3's own placement. Each of the five twins carries its ruled line at the L2 reading file, and each
of the six L3 row-parts is placed by a ruling, its line written by the act from §L.45's table; none of the eleven is
left unplaced. On this derivation, neither ruling needs a further ruling to stand with the other.

**Nothing can be written for the twins by this act** [checked]. The reading file the dispatch edits is
`ratification_surfaces/cowork_comparison_l3_reading.md` (dispatch line 78), and the write set is *"The landed paths of
Task 0, the successor, the derivation's banner, the reading file's additions, the four `FRAMEWORK.md` sites, S-50, the
Task-5 files and the report"* (lines 5556–5558); the L2 reading file is not in it. Neither the language-model record
(read whole) nor nothing-from-L3 Ruling 5 (read at lines 181–198) orders a note at L2 saying the L3 rows are now
HISTORICAL. The standing bars forbid the act to write words no record gives (dispatch line 201, relayed from Ruling 21).

**This is (lxii)'s first set again, now Ruling 22** [checked: the part 2 ruling record, read whole]. Ruling 22 ruled
that for the L2 twins of the pairwise-grammar rows *"nothing is written; their proposals stand untouched"*, on the
ground that they are rows of the L2 reading file outside the write set, *"as §L.37, §L.42 and §L.45 already say of their
own L2 rows"* (record line 1122). The case here differs in one way: (lxii)'s twins were proposals, these are ruled.

**One §L entry names the rows** [checked: a search of the whole dispatch for the six L3 row numbers and the
five twins' numbers, not preceded by a digit or a point and not followed by a digit, with only-matching output]. Every
hit is inside §L.45 (lines 3899, 3914, 3920, 3929, 3937, 3955–3957). So form (b)'s two-record rule (Ruling 3) is not
met, and this item adds no line at any row: the six L3 row-parts get their HISTORICAL lines from §L.45's table as it
stands.

**How the point reaches you.** As Rulings 21 to 25, 28 and 29 have it for points the act writes nothing for: §L.45's
*Open* point (1) is rewritten to point to the ruling, and Task 5's full close restates every §L entry's *Open* points
under *"The points that are not this batch's"* (dispatch lines 5518–5521, read). It is not listed under *points
answered by a record's own derivation, nothing written* (Task 3 (c) item 4): Ruling 26 reads that heading as for a point
a record answers by its own derivation, and what answers point (1) is two rulings of yours and the write set.

**No ruling of the two release records answers it** [checked]. A search of the part 2 ruling record for *"§L.45"*,
*"(lxiv)"*, the twins' numbers, *"language-model"* and *"nothing-from-L3"*, in any case, meets Ruling 22 (lines 1110,
1122 and 1148, the last: *"§L.45's *Open* point (1) are not touched"*) and Ruling 23 (line 1208: *"(lxiv) and (lxviii)
are not ruled"*). The same search of the part 1 release record meets nothing.

Applying D-599: both placements are ruled and stand together; the act cannot write at L2 and no record orders a note
there; Ruling 22 settled the same shape for (lxii)'s twins; and Rulings 21 to 25, 28 and 29 fix how such a point reaches
you. What is put to you is the ratification of that derivation.

#### The wording the writing side proposes

- **For the L2 twins (Rows 36.1, 54.1 to 54.4):** nothing is written; their ruled RELOCATED lines stand untouched.
  Nothing is added to the dispatch for them.
- **For the six L3 row-parts (Rows 57.124 (i) and (ii), 57.498 to 57.501):** nothing beyond §L.45's table line as it
  stands (HISTORICAL, form (b)).
- **§L.45's *Open* point (1)** (dispatch lines 3941–3943), **its check note's *"Point (1) stands."*** (line 3959), and
  **the check row's *"Left for the releasing sitting: §L.45 point (1)."*** (line 20) are rewritten to point to the
  ruling: the twins stand ruled RELOCATED to L3 (nothing-from-L3 Ruling 5, put as filing that does not decide L3's
  design) and their L3 rows ruled HISTORICAL (the language-model record's Ruling 1); the two rulings do not conflict;
  the act writes nothing for the twins. The rewritten point reaches you in Task 5's full close under *"The points that
  are not this batch's"* (lines 5518–5521).
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written*.

#### Weak points the writing side fixed before putting this

- **"Not listed."** The list's heading says the pairing *"is not listed in the report"*. Task 5's full close restates
  every §L entry's *Open* points, so a rewritten point (1) reaches you there in any case, as Ruling 22 has it for
  (lxii)'s first set. The list's contrast with (lxii) is dropped; the case is (lxii)'s, as above.
- **The check row.** The list's *To do* names §L.45's *Open* point (1) and its check note only; the check row's
  *"Left for the releasing sitting: §L.45 point (1)."* is added.
- **The list's own *To do*.** The list does not say its own (lxiv) *To do* is to point to the ruling; added below.
- **The list's ground.** The list rests on *"the test (lix) to (lxiii) set"* (its line 2780), items unruled when it was
  written. Rulings 21, 22 and 26 are used above in its place.
- **Two over-wide phrasings.** The list says the act's write set *"holds the L3 reading file only"*: narrowed above to
  what dispatch lines 78 and 5556–5558 say (the reading file the act edits is the L3 one; the L2 reading file is not in
  the write set). The list says RELOCATED to L3 *"says only that the sentence is L3's to place"*: replaced above by the
  words Ruling 5 was put with.
- **The §10 heading.** The list places the twins' §10 entries *"under its L3 heading"*; this sitting read the entries,
  not the heading, so the heading is marked relayed.

#### The weak point, stated by the working list

That your *"confirmed"* took in the sentence put with Ruling 5 (*"relocating a claim to L3 does not decide L3's
design"*) is the writing side's reading; the ruling itself reads *"placed as the comparison proposed, unchanged"*. If
you read the record's §2 carry as an open point instead, it reaches you in Task 5's close in the same way. Either way
nothing is written at either reading file by this item. Documentation only.

#### Not read, not decided here

The language-model family surface was not opened; the record says it *"stands alone"*. §L.37, to which §L.45's *L2
sides* sentence points (*"as at §L.37"*), was not read. The nothing-from-L3 record was read at lines 181–209 only. The
L2 reading file's §10 heading above lines 75670 and 75838 was not read. Rows 57.499 to 57.501 were read at their first
six lines only. `ARCHITECTURE.md` and `docs/llm_integration.md` were not read; the superseded banners are §L.45's point
(2), answered by its check note, and not touched. The record's other carried items (the departure from §6.33's and
§6.51's listings; the surface's §7G) are not touched. Whether a later L2 act notes at its rows that their L3 twins are
HISTORICAL is not decided here.

#### The currently decided method

Unchanged by this item [checked: the language-model record, lines 52–56]: L2 decides key and chord together and
publishes the chord as a degree in its tonality; L3 publishes facts read off it (chord symbol, figured bass, harmonic
rhythm, cadence with type at each phrase end, phrase and section grouping, key areas, the pivot re-expression, the modal
counts per key area, and, once the application act amends `FRAMEWORK.md`, the catalog matches); no language model is
part of L2's or L3's method. *"HISTORICAL adds nothing to L3."* (line 52). Nothing-from-L3 Ruling 5 changed nothing in
L2's algorithm (*"filing only"*, line 187).

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. Both placements are yours and stand together; the act cannot write at L2, no record read
here orders a note, and the point reaches you in Task 5's close whichever way the list's weak point is read. Towards the
objective, nothing in the analysis changes, and no row is left unplaced on either side. So the derivation is put for
ratification, not as a menu. The one variant, a note at the L2 rows that their L3 twins are HISTORICAL, would need words
no record gives and an act outside this one's write set: a ruling of its own, outside this item.

**To do at release:** change §L.45's *Open* point (1) (dispatch lines 3941–3943), its check note's *"Point (1)
stands."* (line 3959) and the check row's *"Left for the releasing sitting: §L.45 point (1)."* (line 20) to point to
the ruling, as worded above; change the working list's (lxiv) *To do at release* (its lines 2797–2799) to point to the
ruling; former wordings kept.

### Item (lxviii) — §L.50's point (3): the twelve L2 rows the chord-as-degree ruling relocated to L3, "not checked against" the L3 reading file's member 57

*Added by the sitting booted on entry 759.* Its list item opens at list line 3027 [checked]; its read list is the
paragraph just above it (list lines 3016–3026).

#### What the question is, from scratch

On 2026-10-08 you ruled, in Ruling 1 of the L2 chord-as-degree record
(`cowork_rulings_2026_10_08_l2_chord_as_degree_sitting.md`, read whole), that twelve L2 row-parts go **RELOCATED to *L3
— The read-off facts*** (record lines 33–34): Rows 6.163, 6.205 (ii), 10.12, 17.25 (i), 17.44 (ii), 17.52 (ii), 23.340,
30.26 (ii), 48.40 (i), 49.17 (i), 49.20 (ii) and 49.38. They are part of the record's family under the L2 statement
L2-S27 (record line 13). The record calls the ruling *"documentation only"* (line 29), says *"L2's algorithm as its
statements define it is unchanged"* (line 39) and *"Meta level: filing labels only"* (line 53); its method, as stated
with the question: *"L3 computes the chord symbol from L2's answer and publishes it, and may not use it to revise L2"*
(lines 46–47).

The L3 chord-symbol record (`cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md`, read at lines 85–152), in the check
of its own surface before the question, found: *"(8) **omission** — the twelve rows the L2 chord-as-degree Ruling 1
RELOCATED to L3 (…), not checked against the L3 comparison's member 57"* (lines 102–104), and carried it: *"§3 (8)
unchecked"* (line 133). It does not say what the check was to establish.

**What the dispatch writes now** [checked]. §L.17, the chord-symbol record's entry (heading at dispatch line 1344, found
by a search), lists the twelve among *"Rows the record mentions and does not place"*: *"**No line from this record** for
any of them."* (lines 1417–1422). §L.50, the bass-role record's entry (heading at line 4353, found by a search), says of
L2 Row 49.17 (i): *"This act writes nothing for it from this record."* (line 4418), and its *Open* point (3) reads:
*"§L.17's twelve unchecked L2 rows: for Row 49.17(i), this record supplies the L3 twin; the other eleven are not touched
by it."* (lines 4429–4430). Its check note: *"Point (3) is settled by no Task; it stands as written."* (line 4438). The
check row (line 20, by a bounded search): *"point (3) settled by no Task. Left for the releasing sitting: §L.50 point
(3)."* The carry list names the point at §8 item 9 (its lines 198–199) [checked].

So the question: does the act write anything for the twelve, and what becomes of point (3)?

#### What the record already says

**The twelve L2 lines, read at the rows** [checked: the L2 reading file, each row found by the row-heading search, its
ruled line read by offset below the heading]. Each carries *"RULED DISPOSITION
(cowork_rulings_2026_10_08_l2_chord_as_degree_sitting.md, Ruling 1)."* with **RELOCATED to *L3 — The read-off facts***
*"— as proposed"*, naming the part where the ruling names one: Rows 6.163 (line 12549), 10.12 (24174), 23.340 (40469)
and 49.38 (68169) whole; claim (ii) of Rows 6.205 (13139), 17.44 (30087), 17.52 (30242), 30.26 (45655) and 49.20
(67913); claim (i) of Rows 17.25 (29743), 48.40 (67268) and 49.17 (67869).

**Where each reaches L3** [checked: the L3 reading file's §6.57]. §6.57 lists the L2 transfer list's block *"To *L3 —
The read-off facts*"*, *"the block whose bullets are B1 to B123 above and whose named rows are Rows 57.1 to 57.537"*
(lines 72665–72666), and gives a table *"The lines, one per named L2 row"* (head at lines 72109–72113), whose last column
names an L3 row or reads **FULL ROW BUILT**. For the twelve: L2 Row 6.163 → Row 10.181; 6.205 (ii) → Row 10.221; 10.12 →
Row 42.6; 17.25 (i) → Row 15.23; 17.44 (ii) → Row 15.42; 17.52 (ii) → Row 15.50 (lines 72180–72189); 23.340 → Row 21.191
(line 72219); 30.26 (ii) → **FULL ROW BUILT**, Row 57.119 itself (line 72232; read at lines 73487–73510, where it is
proposed **ADOPTED — proposed**, *"as Row 21.205, travelling with it and with Row 21.191"*, line 73508); 48.40 (i) → Row
49.26 (line 72480); 49.17 (i) → *"Rows 48.9 to 48.15 (§6.48) — the quotation joins the items those rows tabulate one by
one, with an elision"*; 49.20 (ii) → Rows 48.18, 48.19 and 48.20; 49.38 → Row 48.24 (lines 72498–72500). So each of the
twelve stands at L3 under a named row. That is the check correction (8) names, made at the object by this side. The
chord-symbol record's own list of what it read (its §7, lines 144–148) does not name §6.57; that §7 also points to the
figured-bass record's §7, not read.

**Nothing can be written for the twelve by this act** [checked]. The reading file the dispatch edits is
`ratification_surfaces/cowork_comparison_l3_reading.md` (dispatch line 78), and the write set (lines 5556–5558) does not
include the L2 reading file. Neither the chord-as-degree record (read whole) nor the chord-symbol record (lines 85–152)
orders a note at the twelve. Ruling 30 settled the same shape for the language-model twins, and Ruling 22 for (lxii)'s
first set.

**This item places no L3 row.** The L3 rows named above get their lines, if any, from the §L entries that name them;
what those give them is not judged here. A search of the whole dispatch for the twelve L2 row numbers (not preceded by a
digit or a point, not followed by a digit) meets them only at §L.17 (line 1420) and §L.50 (lines 4406–4429) [checked].
So form (b)'s two-record rule (Ruling 3) does not arise.

**One wording in point (3) is wider than its record.** Point (3) says the bass-role record *"supplies the L3 twin"* of
Row 49.17 (i). The record names L2 Row 49.17 (i) as the twin of its own row, Row 48.15 (*"Twin: L2 Row 49.17 (i)"*,
bass-role record line 36), whose sentence is *"the bass chord-factor role per event"* (lines 30–31). At the L2 reading
file, claim (i) of Row 49.17 is a list of derived chord facts ending with that item (line 67861); §6.57 puts the
claim's quotation over Rows 48.9 to 48.15 (line 72498). So Row 48.15 is the L3 row for one item of the claim, not for
the whole claim. An apparent error, fixed at release under your rule of 2026-09-22.

**How the point reaches you.** As Rulings 21 to 25 and 28 to 30 have it: §L.50's *Open* point (3) is rewritten to point
to the ruling, and Task 5's full close restates every §L entry's *Open* points under *"The points that are not this
batch's"* (dispatch lines 5518–5521, read). It is not listed under *points answered by a record's own derivation,
nothing written* (Task 3 (c) item 4): Ruling 26 reads that heading as for a point a record answers by its own
derivation, and here no record answers it; the writing side's check at §6.57 does.

**No ruling of the two release records answers it** [checked]. A search of the part 2 ruling record for *"(lxviii)"*,
*"§L.50"*, *"§L.17"*, *"chord-as-degree"*, *"member 57"*, *"48.15"* and *"49.17"*, in any case, meets Ruling 18 (line
892, §L.50 named for other rows) and Ruling 23 (lines 1207–1208, *"(lxviii) … not ruled"*). The same search of the part
1 release record meets line 46 only, on Row 22.92.

Applying D-599: the twelve are ruled at L2 and are outside the act's write set; the check the record left open is a
check of fact, and the fact stands in the L3 reading file; Rulings 22 and 30 settled the same shape; and Rulings 21 to
25 and 28 to 30 fix how such a point reaches you. What is put to you is the ratification of that derivation.

#### The wording the writing side proposes

- **For the twelve L2 rows:** nothing is written; their ruled RELOCATED lines stand untouched. Nothing is added to the
  dispatch for them.
- **For the L3 rows named at §6.57:** nothing from this item.
- **§L.50's *Open* point (3)** (dispatch lines 4429–4430), **its check note's *"Point (3) is settled by no Task; it
  stands as written."*** (line 4438) and **the check row's *"Left for the releasing sitting: §L.50 point (3)."*** (line
  20) are rewritten to point to the ruling: the twelve stand ruled RELOCATED to L3 by chord-as-degree Ruling 1; the
  check the chord-symbol record left open is made at the L3 reading file's §6.57, which names an L3 row for each of the
  twelve; the act writes nothing for them. In point (3), *"this record supplies the L3 twin"* is corrected to say that
  the record names L2 Row 49.17 (i) as Row 48.15's twin and that §6.57 puts the claim's quotation over Rows 48.9 to
  48.15. The rewritten point reaches you in Task 5's full close under *"The points that are not this batch's"* (lines
  5518–5521).
- **At §L.17's sentence on the twelve** (dispatch lines 1419–1422): a pointer to the ruling is added.
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written*.

#### Weak points the writing side fixed before putting this

- **"Not listed."** The list says the point is *"not named in Task 5's "The points that are not this batch's""*. Task
  5's full close restates every §L entry's *Open* points, so the rewritten point (3) reaches you there in any case, as
  Ruling 30 has it for (lxiv).
- **The check row.** The list's *To do* names point (3) and its check note only; the check row's *"Left for the
  releasing sitting: §L.50 point (3)."* is added.
- **The list's own *To do*.** The list does not say its own (lxviii) *To do* is to point to the ruling; added below.
- **The list's ground.** The list rests on *"the test (lix) to (lxvii) set"* (its line 3058), items unruled when it was
  written. Rulings 22, 26 and 30 are used above in its place.
- **Two over-wide phrasings.** The list says the act's write set *"holds the L3 reading file only"*: narrowed above to
  what dispatch lines 78 and 5556–5558 say. The list says a relocation to L3 *"says only that the sentence is L3's to
  place"*, from the bass-role surface: replaced above by the chord-as-degree record's own words.
- **A gloss.** The list describes each relocated part as concerning *"the chord symbol, the numerals or the facts derived
  from the decided chord"*, each with L2-S27 AGREES; this sitting read the twelve ruled lines and Row 49.17's whole
  entry, not each row's axis, so that description is not used. It also explains §6.57's last column from the table's
  head; the head as read (lines 72109–72113) explains the *Bullet* and *Document and locator* columns only, so the
  column is described above by what it holds.
- **The Row 49.17 correction narrowed.** The list calls Row 48.15 *"the twin of the claim's bass-role item"*; above it
  is stated at what was read: the record's own *"Twin"* line, the claim's list ending with the bass-role item, and
  §6.57's span.

#### The weak point, stated by the working list

That §6.57's table answers the chord-symbol record's *"not checked against … member 57"* is the writing side's reading;
the record does not say what the check was to establish. If you read it as asking more (for example, whether each L3
row named above is placed in a way that fits the L2 ruling), that comparison belongs to those rows' own entries, not to
this act, and it reaches you in Task 5's close in the same way. Documentation only either way.

#### Not read, not decided here

The L3 rows named at §6.57 (other than Row 57.119) and their §L entries were not read. The twelve L2 rows' axes were not
read, except Row 49.17's. The chord-symbol surface and the bass-role surface were not opened. One count-only search of
the whole L2 reading file was run (declared at this sitting's close). Ruling 2 of the chord-as-degree record (Rows
47.17 (iv) and 47.18 (i), travelling with Row 49.17 (i)) is not part of this point and is not touched. §L.50's *Open*
points (1) and (2) (settled by its check note) and §L.17's *Open* points are not touched.

#### The currently decided method

Unchanged by this item [checked: the bass-role record, lines 53–60, as that record states it]: L1 publishes, per slice, the lowest sounding pitch
with its witness note, and the spelled intervals above it (both ruled, not yet applied). L2 publishes per span the chord
(degree, quality, figure, applied target) in its tonality, and per sounding note the chord-tone assignment. L3 publishes
the chord symbol whose bass note is the structural bass L2's figure names (L3-S4); the span figured bass; the
continuo-grain figured bass; and, per slice, which member of L2's chord the lowest sounding note is, or that it is not a
chord tone, named apart from the structural bass. L3 never re-derives a fact a lower layer publishes (L3-S39).
Chord-as-degree Ruling 1 changed nothing in L2's algorithm (record line 39).

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The twelve are ruled at L2; the act cannot write at L2 and no record orders a note there;
the check left open is a fact now found at the L3 reading file; and the point reaches you in Task 5's close whichever way
the list's weak point is read. Towards the objective, nothing in the analysis changes, and each of the twelve stands at
L3 under a named row. So the derivation is put for ratification, not as a menu. The one variant, comparing each named
L3 row's placement with the L2 ruling, belongs to those rows' own entries, not to this item.

**To do at release:** change §L.50's *Open* point (3) (dispatch lines 4429–4430), its check note's *"Point (3) is
settled by no Task; it stands as written."* (line 4438) and the check row's *"Left for the releasing sitting: §L.50
point (3)."* (line 20) to point to the ruling, as worded above, with the Row 49.17 correction; add a pointer to the
ruling at §L.17's sentence on the twelve (lines 1419–1422); change the working list's (lxviii) *To do at release* (its
lines 3084–3088) to point to the ruling; former wordings kept.

---

## Site 19 — Group 6, a line written as ruled, with something listed beside it: items (lxiii), Row 19.59 (i)'s condition, and (lxxxiii), Row 40.12 (iii)'s L0 question

*(Former heading, kept: "… with something listed beside it: item (lxiii), Row 19.59 (i)'s condition". (lxxxiii) added.)*

*Added by the sitting booted on entry 760.* The sixth group site, on the user's ruling of 2026-11-11 (*"As many as will
fit in sessions."*, entry 744 §2 item 3). Group 6 is the items where a row's line is written as ruled and something
about it is listed for you beside it, as entry 744 §2 item 4 sorted them from the list's headings alone (*"a line
written as ruled, with something listed beside it"*): (lxiii), Row 19.59 (i), at list line 2696, and (lxxxiii), Row
40.12 (iii), at list line 4037 [entry 744 lines 65–66 checked by this sitting; both list lines checked by a search for
the item numbers]. They are taken in list order. The sitting booted on entry 760 added (lxiii), and the sitting booted
on entry 761 added (lxxxiii), its list line checked by that sitting; with (lxxxiii), group 6 is complete. *(Former
wording, kept: "This sitting adds (lxiii); (lxxxiii) is named in "What this file does not yet carry", for a later
sitting to add here.")*

**Documentation only. It does not change the algorithm as the specification defines it.** It settles the wording of
one row's line in the reading file ((lxiii)), and how the dispatch carries to you a ruled condition ((lxiii)) and an L0
question a record leaves open ((lxxxiii)). Nothing about what the analysis does. *(Former wording, kept: "It settles the
wording of one row's line in the reading file and how the dispatch carries a ruled condition to you.")*

### Item (lxiii) — §L.43's point (2): Row 19.59 (i)'s HISTORICAL, and the condition the ruling attached to it

Its list item opens at list line 2696 [checked]; its read list is the paragraph just above it (list lines 2689–2695).

#### What the question is, from scratch

Row 19.59 of the L3 reading file is a sentence from the old architecture text: *""Six" is the *current* decomposition
of the **harmonic spine**, not a ceiling: …"*, followed by a list of further named elements (reading file lines
24828–24836). The reading file splits it into four claims; claim (i) is *"six is the current decomposition of the
harmonic spine and not a ceiling, the architecture carrying more named elements"* (line 24837), proposed **UNPLACED**
(*"read: the outgoing sentence; a rule of the framework's decomposition, as at Row 19.56 (i)"*, line 24850)
[checked: the row found by the row-heading search, read at lines 24825–24855].

On 2026-11-07 you ratified, in Ruling 1 of the decomposition-rules record
(`cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md`, read whole), Parts 2A, 2B and 2C *"as the
surface derives them"*. Its 2B reads in full (record lines 40–42):

> **2B — HISTORICAL (1):** Row 19.59 (i), *"Six" is the current decomposition of the harmonic spine, not a ceiling*: a
> status of the layering superseded by Ruling 2 of 2026-08-29. Its rule content (*not a ceiling*) has its one home at
> Row 19.57 (ii) in 2C. It follows from 2C; if 19.57 (ii) is ever placed otherwise, 19.59 (i) is re-tested with it.

So the HISTORICAL comes with a condition: if Row 19.57 (ii) (*"their count is not a cap"*, reading file lines 24788–24789) is
ever placed other than as 2C placed it, *"outside every charter, carried for the framework"*, Row 19.59 (i) is to be
re-tested with it.

**What the dispatch writes now** [checked]. §L.43 (dispatch lines 3714–3792; its heading found by a search, line
3714) gives the row a form (b) **HISTORICAL** line whose placement quotes 2B's first sentence only (its table, line
3741), naming claim (i) only. Its *Open* point (2) (lines 3775–3776): *"2B's HISTORICAL is conditional in the record's
own words: "if 19.57 (ii) is ever placed otherwise, 19.59 (i) is re-tested with it"; the line is written as ruled, and
the condition is carried for the user, not acted on."* Its check note ends *"Points (1) and (2) stand."* (line 3785).
The check row (line 20, by a bounded search): *"Left for the releasing sitting: §L.43 points (1) and (2)."*

So the question: is the line written as the table has it, or with 2B quoted whole, the condition included; and what
becomes of point (2)?

#### What the record already says

**The condition is ruled, not open** [checked]. Ruling 1 ratifies 2B *"as the surface derives them"* (record line 27).
The surface (`ratification_surfaces/cowork_l3_decomposition_rules_family_surface_2026_11_07.md`) states the same
dependency in its 2B: *"**2B therefore follows from 2C.** If 19.57 (ii) is placed otherwise, 19.59 (i) is re-tested
with it."* (lines 172–173), and its check calls 2B *"a derivation that follows from 2C, not a separate choice"* (§6
item 6, lines 300–302). So the condition is part of what you ratified. It asks nothing now; it says what a later act
must do if one ever places Row 19.57 (ii) otherwise.

**This act does not meet the condition** [checked]. Row 19.57 (ii) is one of 2C's nine rows (§L.43's table, line 3742).
Ruling 1 of the part 2 ruling record (part 2a's Question A5, your word *"A"*) gives every row-part a ruling places outside
every charter one line, `*RULED PLACEMENT (<record file>, Ruling N).* Outside every charter — <the record's placement
in its words>; listed in the successor's notes.`, with no disposition word, and its *To do at release* names §L.43's
*Open* point (1) and the table line 3742 (ruling record lines 27–31 and 44–46). That is the placement 2C ratified, not
an *"otherwise"*. A search of the whole dispatch for *"19.57"* (not preceded by a digit or a point, not followed by a
digit) meets it at lines 3742, 3748, 3760 and 3775, all within §L.43. So nothing is re-tested, and the HISTORICAL stands
as ruled.

**Where the condition can be kept.** Form (b)'s line is
`*RULED DISPOSITION (<record file>, Ruling N).* **<disposition>** — <placement in the record's words>.` (dispatch line
156). The record states 2B's placement in three sentences: the status and what superseded it; where the rule content
has its home; and when the row is re-tested. Quoting all three puts the condition in the reading file, beside the row
it would re-test, as well as in the record. The words are the record's, so the act derives nothing (the standing bars,
dispatch line 201: *"an amendment is the record's words placed, never this batch's"*). The record's §2 says of 2C:
*"The nine rows of 2C wait there"*, at *"the framework's and the ratification act's"* (record lines 67–68); this act
takes no ruling (the standing bars, dispatch lines 209–210: *"no ruling taken, no position weighed"*), so it does not
place Row 19.57 (ii) otherwise.

**Not *as proposed*** [checked]. The row was proposed UNPLACED (reading file line 24850), so the line does not say *as
proposed* (form (b), dispatch line 157).

**One record gives this claim a line** [checked: a search of the whole dispatch for *"19.59"*, bounded as above]. It
meets the row at §L.43 (lines 3741, 3748, 3756, 3760–3761, 3775) and at §L.12's table (line 945), which names claim
(iv), among the sections record's twelve rows. Different claims, so form (b)'s two-record rule, as Ruling 3 has it
(applied by part), is not met.

**How the point reaches you.** As Rulings 21 to 25 and 28 to 31 have it: §L.43's *Open* point (2) is rewritten to point
to the ruling, and Task 5's full close restates every §L entry's *Open* points under *"The points that are not this
batch's"* (dispatch lines 5518–5521, read). It is not listed under *points answered by a record's own derivation,
nothing written* (Task 3 (c) item 4): Ruling 26 reads that heading as for a point a record answers by its own
derivation, and here the condition is part of your Ruling 1, and a line is written.

**No ruling of the two release records answers it** [checked]. A search of the part 2 ruling record and of the part 1
release record for *"(lxiii)"*, *"§L.43"*, *"19.59"*, *"19.57"*, *"decomposition-rules"*, *"decomposition rules"* and
*"re-tested"*, in any case, meets the part 2 record only: Ruling 1 (line 18, the decomposition-rules record among A5's
sites; line 46, §L.43's point (1)), Ruling 23 (line 1207, *"(lxiii) … not ruled"*) and Ruling 30 (line 1652, the list's
ground quoted). None answers point (2).

Applying D-599: the HISTORICAL and its condition are both ruled; this act places Row 19.57 (ii) as 2C ratified, so the
condition is not met; form (b) takes the placement in the record's words, and the record words it in three sentences;
and Rulings 21 to 25 and 28 to 31 fix how such a point reaches you. What is put to you is the ratification of that
derivation.

#### The wording the writing side proposes

- **Row 19.59's line** (the §L.43 table's line, dispatch line 3741), naming claim (i) only, not *as proposed*:

> `*RULED DISPOSITION (cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md, Ruling 1).* (i) **HISTORICAL** — "Row 19.59 (i), "Six" is the current decomposition of the harmonic spine, not a ceiling: a status of the layering superseded by Ruling 2 of 2026-08-29. Its rule content (not a ceiling) has its one home at Row 19.57 (ii) in 2C. It follows from 2C; if 19.57 (ii) is ever placed otherwise, 19.59 (i) is re-tested with it."`

  The record's italics are not carried into the quotation, as the table's line already drops them.
- **§L.43's *Open* point (2)** (dispatch lines 3775–3776), **its check note's *"Points (1) and (2) stand."*** (line
  3785), for point (2), and **the check row's *"Left for the releasing sitting: §L.43 points (1) and (2)."*** (line 20),
  for point (2), are rewritten to point to the ruling: 2B's HISTORICAL and its condition are both ruled (decomposition-
  rules Ruling 1); this act places Row 19.57 (ii) as 2C ratified (part 2 Ruling 1), so the condition is not met and
  nothing is re-tested; the line quotes 2B whole, so the condition stands beside the row. The rewritten point reaches
  you in Task 5's full close under *"The points that are not this batch's"* (lines 5518–5521).
- **In the report:** no listing of its own, and not under *points answered by a record's own derivation, nothing
  written*.

#### Weak points the writing side fixed before putting this

- **A ground the list used before it was ruled.** The list says Row 19.57 (ii) takes its placement *"by (xxxvi)'s
  line"*. (xxxvi) was ruled as part of Question A5, now Ruling 1 of the part 2 ruling record; its words are used above.
- **The two-record rule.** The list cites form (b)'s rule *"by its present wording or by (xlix)'s"*; (xlix) is now
  Ruling 3, and Ruling 3 is used above.
- **Naming in Task 5's bullet.** The list proposes naming §L.43's point (2) in Task 5's bullet. Task 5's full close
  restates every §L entry's *Open* points, so the rewritten point reaches you there in any case; the separate naming is
  not used, as Rulings 21 to 25 and 28 to 31 have it.
- **The list's ground.** The list rests on *"the test (lix) to (lxii) set"* (list line 2721), items unruled when it was
  written. Rulings 21 to 26 and 28 to 31 are used above in its place.
- **The check row.** The list's *To do* names §L.43's *Open* point (2) and its check note only; the check row's
  *"Left for the releasing sitting: §L.43 points (1) and (2)."*, for point (2), is added.
- **The list's own *To do*.** The list does not say its own (lxiii) *To do* is to point to the ruling; added below.

#### The weak point, stated by the working list

That the record's second and third sentences belong to *"the placement in the record's words"* is the writing side's
reading of form (b). If you want the line as the §L.43 table now has it (the first sentence only), the condition stays
in the record and reaches you through the rewritten point (2) only, and the row's line says nothing of it.
Documentation only either way.

#### Not read, not decided here

The decomposition-rules surface was read at its headings, its 2B (lines 157–180) and its §6 (lines 282–311) only.
Row 19.57 was read at lines 24785–24797. §L.12's other rows, and claims (ii) to (iv) of Row 19.59, are not touched.
§L.43's *Open* point (1) is Ruling 1's and is not touched here. Whether Δ7 is ruled, which the record leaves to the
framework and the ratification act, is not decided here.

#### The currently decided method

Unchanged by this item [checked: the decomposition-rules record, lines 56–61]: L2 decides key and chord together and
publishes the chord as a degree in its tonality, and the tonality as tonic and mode, two modes only; L3 publishes facts
read off it (chord symbol, figured bass, harmonic rhythm, cadence with type at each phrase end, phrase and section
grouping, key areas, the pivot re-expression, the modal counts per key area, and, once the application act amends
`FRAMEWORK.md`, the catalog matches); no mode label is published; a display turns published facts into text; L3 owns
the answers to its own questions (Δ2).

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The HISTORICAL and its condition are both yours; this act does not meet the condition;
form (b) takes the record's words for the placement; and the point reaches you in Task 5's close either way. Towards the
objective, quoting 2B whole puts the ruled condition beside the row it concerns, in the reading file, as well as in the
record; the first sentence alone would leave it in the record and in this batch's report, and not at the row. Nothing in the analysis changes either way. So the derivation is put for ratification, not as a menu. The one
variant, the line as the table now has it, is the list's weak point above.

**To do at release:** in the §L.43 table's line for Row 19.59 (i) (dispatch line 3741), quote the record's 2B entry
whole (record lines 40–42), as worded above; change §L.43's *Open* point (2) (lines 3775–3776), its check note's
*"Points (1) and (2) stand."* (line 3785) and the check row's *"Left for the releasing sitting: §L.43 points (1) and
(2)."* (line 20), each for point (2), to point to the ruling, as worded above; change the working list's (lxiii) *To do
at release* (its lines 2740–2744) to point to the ruling; former wordings kept.

### Item (lxxxiii) — §L.46's point (3): Row 40.12 (iii)'s RELOCATED to L0, and the L0 question the record leaves open

Its list item opens at list line 4037 [checked]; its read list is the paragraph just above it (list lines 4028–4036)
[checked].

#### What the question is, from scratch

Row 40.12 of the L3 reading file is a sentence from the old architecture text listing six further facts of the score,
from grace notes to part names, each with a use (reading file lines 54224–54249) [checked: the row found by the
row-heading search, read at those lines]. The reading file splits it into six claims. Claim (iii) is *"lyrics and verse
structure as chorale phrase structure, probably redundant with fermatas"* (lines 54231–54232); its current-text axis is
**THE DERIVATION IS SILENT** (line 54239); it was proposed **UNPLACED**, *"a source of phrase evidence that no derived
statement names; read: L3-S9's four families, and `FRAMEWORK.md` §5's list of what L0 gives, which names no lyrics"*
(lines 54243–54245).

On 2026-11-08 you ratified, in Ruling 1 of the phrase-end evidence record
(`cowork_rulings_2026_11_08_l3_phrase_end_evidence_family_sitting.md`, read whole), *"family 8 placed as the surface
derives it"*. Its placement of claim (iii) reads (record line 33):

> **RELOCATED to *L0 — The notated record*** (whether L0 carries lyrics); beside the row: if it does, they enter L3 as a
> candidate term under L3-S9 (iv)'s held-out rule

And under *"Carried, not decided by this ruling"* the record says (lines 62–63): *"The L0 question of 3C: whether the
notated record carries lyrics. It belongs to L0's input contract. An addition to a charter's list is the user's (S-43,
**[relayed]**)."*

In plain words: the row is sent to L0, the notated record, because L3 reads only what L0, L1 and L2 publish (the
surface's 3C, citing L3-S37, surface line 236); if L0 ever carries lyrics, they enter L3 *"as a candidate term under
L3-S9 (iv)'s held-out rule"*, which the surface describes, quoting phrase-units Ruling 2 item d, as a term *"admitted
only if a held-out measurement repays it"* (surface lines 242–243). Whether L0 carries lyrics is left open, and the
record names an addition to a charter's list as yours.

**What the dispatch writes now** [checked]. §L.46 (dispatch lines 3970–4068; its heading found by a search, line 3970)
gives claim (iii) a form (b) **RELOCATED** line naming claim (iii) only and carrying the record's *"beside the row"*
words (its table, line 3998). Its *Open* point (3) (lines 4046–4048): *"Row 40.12 (iii)'s RELOCATED to L0 rests on an
L0 question the record carries: "whether the notated record carries lyrics. It belongs to L0's input contract. An
addition to a charter's list is the user's"; the line is written as ruled, and nothing is added to L0's list."* Its
check note says that Task 3 (c) item 5 reaches the row, that *"whether §10 has a heading for *L0 — The notated record*
or for the preset layer outside the framework was not read"*, and ends *"Points (1) to (3) stand."* (lines 4058–4061).
The check row (line 20, by a bounded search for *"§L.46"*): *"on points (1) and (3), Task 3 (c) item 5 reaches the two
RELOCATED rows, §10's headings not read. Left for the releasing sitting: §L.46 points (1) to (3)."*

So the question: is the line right as the table has it; is anything added to L0's list; what happens at the transfer
list (§10); and how does the open L0 question reach you?

#### What the record already says

**The line is already the record's words** [checked]. The table's quotation is record line 33's placement word for
word. Form (b) is `*RULED DISPOSITION (<record file>, Ruling N).* **<disposition>** — <placement in the record's
words>.` (dispatch line 156), and a split row's line names the claim (lines 159–160). The row was proposed UNPLACED
(reading file line 54243), so the line does not say *as proposed* (line 157). Nothing in the line needs to change.

**The destination is one of the reading file's charters** [checked]. §5 of the reading file lists *"***L0 — The
notated record*** (the input contract)"* among the charters a row relocates to (line 398). So Ruling 2 of the part 2
ruling record (part 2a's Question A6: a RELOCATED line may name a home outside that list where a ruling gives the word
and names the home) does not arise here.

**The words beside the row state a condition this act does not meet** [checked]. *"If it does"* asks whether L0 carries
lyrics. This act takes no ruling (the standing bars, dispatch lines 209–210: *"no ruling taken, no position weighed"*)
and writes no words a record does not give (line 201: *"an amendment is the record's words placed, never this
batch's"*). The record orders no amendment of L0's list. So the act neither answers the L0 question nor adds a candidate
term at L3. This is Ruling 32's case (item (lxiii)): a condition that is part of a ratified ruling, written in the line,
not met by this act. The record's surface says the same: 3C *"adds nothing to L3 unless L0 later carries lyrics"*
(surface line 325).

**Nothing is added to L0's list** [checked]. Beyond the record ordering none: the write set (dispatch lines 5556–5558)
names the landed paths of Task 0, the successor, the derivation's banner, the reading file's additions, the four
`FRAMEWORK.md` sites, S-50, the Task-5 files and the report; Task 4 edits `FRAMEWORK.md` *"at Edits 1 to 3 and their
notes only"* and the derived L0/L1 specification *"at S-50 only"* (lines 5430–5431). A search of the whole dispatch for
*"lyric"* and *"Lyric"* meets lines 3978, 3998, 4033 and 4047, all within §L.46.

**The transfer list (§10)** [checked]. The row-part is placed RELOCATED out of UNPLACED, so Task 3 (c) item 5 reaches
it (dispatch lines 5204–5209): it is appended under its destination heading unless §10 already carries it, and a
destination with no heading is a STOP-and-report. §10's heading *"To *L0 — The notated record* (the input contract)."*
stands at reading file line 78930; its entries run from line 78932 to line 79006, the L1 heading at line 79008. That
block, read whole, carries Row 40.12 (vi) (the entry at line 78977) and does not name claim (iii). So item 5 appends
claim (iii) under the L0 heading by its own rule, and its STOP for a missing heading does not arise. That answers, for
point (3), what the check note left unread. Whether a §10 heading exists for claim (iv)'s preset layer is point (1)'s,
under Ruling 2, and is not touched.

**One record gives this row lines** [checked: a search of the whole dispatch for *"40.12"*, not preceded by a digit or
a point and not followed by a digit]. It meets the row at lines 3991–4058 only, all within §L.46. Claim (iv)'s line is
from the same record, on another claim. So form (b)'s two-record rule, as Ruling 3 has it (applied by part), does not
arise.

**How the open L0 question reaches you.** As Rulings 21 to 25 and 28 to 32 have it: §L.46's *Open* point (3) is
rewritten to point to the ruling, and Task 5's full close restates every §L entry's *Open* points under *"The points
that are not this batch's"* (dispatch lines 5518–5521, read). It is not listed under any of the report's other headings
(lines 5510–5513):
- not *points answered by a record's own derivation, nothing written* (Task 3 (c) item 4, lines 5201–5203), which
  Ruling 26 reads as for a point a record answers by its own derivation; the record answers nothing here, it carries the
  question open;
- not *charter and contract amendments left to the user*: that heading is Task 4's *Not written* list, *"Each is a
  STOP-and-report under form (e) because the record gives no words"* (lines 5404–5407), that is, amendments a record
  orders without words; this record orders none, as Ruling 25 found for the phase-definition surface;
- not *amendments with no words from the record*, for the same reason.

**No ruling of the two release records answers it** [checked]. A search of the part 2 ruling record and of the part 1
release record for *"(lxxxiii)"*, *"§L.46"*, *"40.12"*, *"lyric"*, *"phrase-end evidence"*, *"(xxxviii)"* and
*"(xxxix)"*, in any case, meets the part 2 record only: Ruling 2 (lines 85–86, §L.46's point (1) and the items' lines
*"(xxxvii) to (xxxix)"*) and Ruling 16 (§L.46's point (2)). None answers point (3).

Applying D-599: the RELOCATED line and its condition are ruled; the line in the dispatch is the record's words; the
destination is on §5's list; the act cannot answer the L0 question or add to L0's list; item 5 places the row-part at
§10 by its own rule; and Rulings 21 to 25 and 28 to 32 fix how the open question reaches you. What is put to you is the
ratification of that derivation.

#### The wording the writing side proposes

- **Row 40.12's line:** as the §L.46 table gives it (dispatch line 3998), unchanged; in form (b)'s shape, naming claim
  (iii) only, not *as proposed*:

> `*RULED DISPOSITION (cowork_rulings_2026_11_08_l3_phrase_end_evidence_family_sitting.md, Ruling 1).* (iii) **RELOCATED to *L0 — The notated record*** — "(whether L0 carries lyrics); beside the row: if it does, they enter L3 as a candidate term under L3-S9 (iv)'s held-out rule".`

- **§L.46's *Open* point (3)** (dispatch lines 4046–4048), **its check note's** sentence on §10's headings (lines
  4059–4061) and *"Points (1) to (3) stand."* (line 4061), each for point (3), and **the check row's** *"on points (1)
  and (3), Task 3 (c) item 5 reaches the two RELOCATED rows, §10's headings not read. Left for the releasing sitting:
  §L.46 points (1) to (3)."* (line 20), for point (3), are rewritten to point to the ruling: the line is written as
  ruled, the record's words beside it; this act does not meet the condition and adds nothing to L0's list, which the
  record does not order; the L0 question stays open, the record's §2 sentence quoted whole (record lines 62–63); §10 has
  the L0 heading (reading file line 78930) and its block does not carry claim (iii), so Task 3 (c) item 5 appends it
  there. The rewritten point reaches you in Task 5's full close under *"The points that are not this batch's"* (lines
  5518–5521).
- **In the report:** no listing of its own, and none under the other headings named above.

#### Weak points the writing side fixed before putting this

- **Grounds the list used before they were ruled.** The list leans on *"as at (lxiii)"*, *"as at (xxxix)"* and
  *"(lxxiv)'s case"*. (lxiii) is now Ruling 32, (xxxix) was ruled with part 2a's Question A6 as Ruling 2, and (lxxiv) is
  now Ruling 25; their words are used above, and §5's line 398 is read for A6's question.
- **The list's ground.** The list rests on *"the test (lix) to (lxxxii) set"* (list line 4074), items unruled when it
  was written. Rulings 21 to 26 and 28 to 32 are used above in its place.
- **The two-record rule.** The list cites form (b)'s rule *"by its present wording or by (xlix)'s"*; (xlix) is now
  Ruling 3, used above.
- **Naming in Task 5's bullet.** The list proposes naming §L.46's point (3) in Task 5's bullet. Task 5's full close
  restates every §L entry's *Open* points, so the rewritten point reaches you there in any case; the separate naming is
  not used, as Rulings 21 to 25 and 28 to 32 have it.
- **The check note's and check row's "not read".** The list answers the §10 heading question but does not name those
  two passages in its *To do*; they are added, for point (3).
- **The list's own *To do*.** The list does not say its own (lxxxiii) *To do* is to point to the ruling; added below.

#### The weak points, stated by the working list

(a) If you read the L0 question as a charter amendment left to you, it is listed under *charter and contract amendments
left to the user* instead; only the report's heading changes. The derivation above reads that heading at Task 4's own
words (amendments a record orders without words) and so does not use it. (b) The record's surface names, and does not
test, whether L0/L1 Ruling 50's *"every performance and phrasing mark"* already takes in lyrics (surface lines
252–253). If it does, the L0 question may already be answered; this item does not judge that. Documentation only either
way.

#### Not read, not decided here

The record's surface was read at its 3C (lines 234–260), §4 (lines 320–339), §5 (lines 341–350) and §7G (lines
432–436) only. Ruling 50, S-43, `FRAMEWORK.md` §5's L0 list, L3-S9 and L3-S37 were not opened; their words are relayed
through the record, its surface and the reading file. Row 40.12's other claims, §L.46's *Open* points (1) (Ruling 2) and
(2) (Ruling 16), and the §10 entry at line 78977 are not touched. Whether L0 should carry lyrics is not decided here.

#### The currently decided method

Unchanged by this item [checked: the phrase-end evidence record, lines 45–53]: *"One possible change is carried, not
decided: if L0 later carries lyrics, a candidate term at L3, under a rule already ratified."* L2 decides key and chord
together and publishes the chord as a degree in its tonality; L3 publishes facts read off it (chord symbol, figured
bass, harmonic rhythm, cadence with type at each phrase end, phrase and section grouping, key areas, the pivot
re-expression, the modal counts per key area, and, once the application act amends `FRAMEWORK.md`, the catalog
matches); L3 decides where phrases end as a weighed choice over every candidate position, the notated flags and the
re-homed strength profile entering as evidence with fitted weights, no item forcing or forbidding a phrase end; no
preset or style label reaches L2; no language model is part of L2's or L3's method.

#### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. The line and its condition are yours already and the dispatch writes them in the record's
words; the act cannot answer the L0 question; §10 takes the row-part by item 5's own rule; and the open question reaches
you in Task 5's close. Towards the objective, the lyrics question stays visible and unanswered rather than being settled
by default, and if L0 later carries lyrics, they enter L3 as a candidate term *"under a rule already ratified"* (record
line 45).
Nothing in the analysis changes either way. So the derivation is put for ratification, not as a menu. The one variant,
the report heading, is the list's weak point (a) above.

**To do at release:** change §L.46's *Open* point (3) (dispatch lines 4046–4048), its check note's sentence on §10's
headings (lines 4059–4061) and *"Points (1) to (3) stand."* (line 4061), and the check row's *"on points (1) and (3),
Task 3 (c) item 5 reaches the two RELOCATED rows, §10's headings not read. Left for the releasing sitting: §L.46 points
(1) to (3)."* (line 20), each for point (3), to point to the ruling, as worded above; the §L.46 table's line for Row
40.12 (iii) (line 3998) stands; change the working list's (lxxxiii) *To do at release* (its lines 4094–4098) to point to
the ruling; former wordings kept.

---

## Site 20 — Item (lxxiii): §L.27's part E, the added statement's text: the record's quoted sentence by Task 1 (c) item 3 (i), or the surface's part by item 3 (ii)

*Added by the sitting booted on entry 762. One item on its own, as entry 744 §2 item 4 puts it [checked: entry 744 lines
52–68, (lxxiii) §L.27 part E, list line 3381].*

Its list item opens at list line 3381 [checked: a search for the item number]; its read list is the paragraph just above
it (list lines 3376–3380) [checked].

**Documentation only. It does not change the algorithm as the specification defines it.** It settles which text the act
copies into the amended L3 specification for one statement the user has already ratified. Nothing about what the
analysis does.

### What the question is, from scratch

On 2026-11-04 you ratified Ruling 1 of the architecture-rules record
(`cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md`, read whole), headed *"parts A to F RATIFIED as
derivations, part E in the narrower wording"* (record line 25). The record says of the six parts *"Each part stands as
the surface states it after the check. In short:"* (line 27), and gives part E as (lines 48–53):

> **E (2 row-parts: 38.47, 38.48) — ADOPTED in the narrower wording.** *"A reading missing from L3's own candidate
> readings is remedied inside L3, by widening its candidate set; a backward edge is not the remedy, except as the
> deliberate, surfaced, measured and documented exception D-466 admits."* The reading file's proposal sentence (*"…and
> never by a backward edge"*) is not adopted as written: it is wider than **D-466** (line 294, LIVE, 2026-08-04 · user)
> and than L3-S38 as ratified on 2026-11-03 (*"It is a question for a measured backward edge."*). The rows' own text is
> carried as written.

Its documentation sentence: *"six statements (parts A to F) to be added to the amended L3 specification"* (lines 59–60).

The act writes part E into the amended L3 specification as an added statement. The question is only which text it
copies; what part E says is ruled and is not reopened here.

**What the dispatch writes now** [checked]. §L.27's amendment 1 (dispatch lines 2281–2293) gives part E as *"the
quoted sentence"* above, and ends *"See *Open* point (2), settled by Task 1 (c) item 3."* Task 1 (c) item 3 (lines
5045–5057) gives the text of each added statement by three rules:

> **(i)** where the record quotes the statement's text, or gives it as an *"As ruled"* sentence, that text, quoted
> whole; **(ii)** where the record says a part *"stands as the surface states it after the check"*, that part as the
> surface file the record names states it, quoted whole, located by the part's heading there, with the record's *"In
> short"* words for the part quoted beneath it as a sub-item; **(iii)** where neither (i) nor (ii) locates a text, that
> addition is a STOP-and-report, the rest applied.

Part E fits both (i) and (ii). §L.27's check note says so and leaves it open (lines 2362–2365): *"Point (2) is settled by
Task 1 (c) item 3 for parts A to D and F under its (ii), as at §L.25 and §L.26. For part E, both item 3 (i) (the record
quotes the sentence) and (ii) (the part stands as the surface states it) describe it, and item 3 does not say which
governs when both do; for the release surface, not settled here."* §L.27's *Open* point (2) (lines 2348–2351) ends
*"part E alone is given by the record as a quoted sentence. If neither is fixed as the text, each addition is a
STOP-and-report under form (a)."* The check row (line 20, by a bounded search for *"part E"*) names it in two passages:
*"§L.27 point (2) settled by Task 1 (c) item 3 (ii) for parts A to D and F, while part E is described by both item 3 (i)
and (ii) and item 3 does not say which governs — for the release surface"*, and *"Left for the releasing sitting: §L.27
point (1) and part E's text"*.

So the question: for part E, does the act copy the record's quoted sentence (rule (i)) or the surface's part E section
(rule (ii))?

### What the record already says

**Task 1 (c) already says what decides it** [checked]. The settlements of Task 1 (c) open: *"Each is the writing side's
settlement, overrulable before Task 0; where a record's own words and this settlement differ, the record governs and the
difference is reported."* (dispatch lines 5029–5030). So the record's own words decide which rule fits part E.

**The record gives part E's text as the wording you ratified** [checked]. The ruling's heading names *"part E in the
narrower wording"* (record line 25); §0 says the question put was *"ratification as derivations, part E in a narrower
wording"* (lines 19–20); part E is *"ADOPTED in the narrower wording"*, followed by that wording in quotation marks
(lines 48–50); the documentation sentence repeats *"Rows 38.47 and 38.48 in part E's wording"* (line 59). That is rule
(i)'s case: the record quotes the statement's text.

**Rule (ii) would copy a sentence the ruling declines** [checked]. The surface
(`ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md`) has part E under the heading *"## 6.
Part E — a reading missing from L3's own candidates is remedied inside L3 (2 row-parts; narrower wording)"* (its line
162), running to line 195. That section quotes Row 38.47's proposal, *"that a reading missing from L3's own candidate
readings be remedied inside L3, by widening its candidate set, and never by a backward edge."* (surface lines 165–166),
the sentence the record says *"is not adopted as written"* (record line 50). Rule (ii) copies the part *"quoted
whole"*, so it would put that sentence inside the added statement. Rule (i) does not.

**Rule (i) and the surface's own derived wording** [checked]. The surface's own derived wording (lines 185–187) is *"that a
reading missing from L3's own candidate readings be remedied inside L3, by widening its candidate set; a backward edge is
not the remedy, except as the deliberate, surfaced, measured and documented exception D-466 admits."* The record's
sentence differs from it only at its start (*"A reading missing … is remedied"* in place of *"that a reading missing …
be remedied"*): a proposal turned into a statement. The surface's check, in the turn after it landed, says *"part E's
narrowing stands"* (line 292). The surface's grounds and weak points stay in the surface, which, the record says,
*"stands alone and is not reproduced here (#6)"* (record line 16).

**§L.27's amendment 1 already names that sentence** [checked]. It gives part E as the
quoted sentence (dispatch lines 2287–2289). Parts A to D and F stay under rule (ii), as the check note settles (lines
2362–2363); this item does not touch them.

**The rows' lines are Ruling 9's, not this item's** [checked: the part 2 ruling record, Ruling 9, lines 400–403].
Ruling 9 names this case by its rows: the line does not say *as proposed* where *"a ruling … adopts narrower content
than the proposal (§L.27 part E, Rows 38.47 and 38.48; …)"*, and the placement is given in the record's words. This
item is about the statement's text, not the rows' lines, and does not change them.

**One record, no row placed here.** This item places no row, so form (b)'s two-record rule (Ruling 3) and §10 do not
arise.

**No ruling of the two release records answers it** [checked]. A search of the part 2 ruling record and of the part 1
release record for *"part E"*, *"§L.27"*, *"38.47"*, *"38.48"*, *"(lxxiii)"*, *"architecture-rules"*, *"architecture
rules"* and *"item 3 (i)"*, in any case, meets the part 2 record only: Ruling 9 (line 371, §L.27's A1 and A2 point at
dispatch line 2344; line 403, quoted above). Neither answers which rule gives part E's text.

Applying D-599: the record names part E's text as the wording you ratified and gives it as a quoted sentence; the
dispatch's own rule says the record governs where its words and the settlement differ; rule (ii) would copy the
sentence the ruling declines. What is put to you is the ratification of that derivation.

### The wording the writing side proposes

- **Task 1 (c) item 3**, at its end, after its last sentence (*"… and the name is listed in the report for the user."*,
  dispatch line 5057), this sentence is added:

  > For §L.27's part E, which (i) and (ii) both describe, **(i) governs**: the record quotes part E's text as the
  > wording the user ratified (*"part E in the narrower wording"*), and (ii) would copy the reading file's proposal
  > sentence the record says *"is not adopted as written"*. Part E's statement is the record's quoted sentence, quoted
  > whole, with no sub-item beneath it (part 2 ruling record, Ruling 34).

- **§L.27's *Open* point (2)** (dispatch lines 2348–2351), **its check note's** sentence *"For part E, both item 3 (i)
  … not settled here."* (lines 2363–2365), and **the check row's** two passages quoted above (line 20), each for part E,
  are rewritten to point to the ruling: rule (i) governs for part E, the record's quoted sentence is the statement's
  text, and Task 1 (c) item 3 says so.
- **In the report:** no listing of its own. Task 5's full close restates *"the settlements of Tasks 1 to 4"* under *"The
  points that are not this batch's"* (dispatch lines 5518–5521), and the added sentence, as part of Task 1 (c), reaches
  you there.

### Weak points the writing side fixed before putting this

- **Grounds the list used before they were ruled.** The list puts the rows under *"A1 and A2 rule (iv)"* (list line
  3412). Ruling 9 replaced the list's rules (i) to (v) with its own paragraph (*"The working list's rules (i) to (v) are
  not written into form (b); this paragraph takes their place."*, Ruling 9, line 406), and names §L.27 part E's rows in
  it (line 403); Ruling 9 is used
  above in place of rule (iv).
- **Where the sentence goes.** The list says *"after (iii)"* (list line 3427). Item 3 does not end at (iii): after it
  comes a sentence on §L.50's statement (dispatch lines 5054–5057). The sentence is placed at the end of item 3, so that
  it does not fall between (iii) and the §L.50 sentence. The list gives no words for the sentence; the wording above is
  the writing side's, put for ratification.
- **The list's *To do* left out three places.** It names the check note only. §L.27's *Open* point (2), which ends on
  part E, and the check row's two passages on part E are added, for part E.
- **The list's own *To do*.** The list does not say its own (lxxiii) *To do* is to point to the ruling; added below.

### The weak point, stated by the working list

That (i) governs where both (i) and (ii) describe a part is the writing side's reading, from (c)'s rule and the record's
words; item 3 itself states no order between them (list lines 3415–3416). If you want (ii) for part E, the statement
would carry the surface's §6 whole, the record's sentence beneath it, and the declined proposal sentence inside it as a
quotation (list lines 3416–3418). Documentation only either way.

### Not read, not decided here

The surface was read at its headings, its §6 (lines 162–195) and, by a search, at its lines 6, 191, 241, 254–255 and 292
as the search returned them. The reading file, Rows 38.47 and 38.48, D-466, L3-S38, form (a) and the successor were not
opened. Whether a part described by both (i) and (ii) elsewhere should follow the same order is not decided here; the
added sentence names part E only. §L.27's *Open* points (1) (Ruling 9) and (3), parts A to D and F, and §L.28's mention
of part E (dispatch line 2390) are not touched.

### The currently decided method

Unchanged by this item [checked: the architecture-rules record, lines 62–67]: L3 reads everything L2 publishes (its
reading, its rivals with mass) plus L0's and L1's published facts, and nothing else; never revises L2, and L2 reads
nothing L3 publishes; a backward edge is tested by measurement as soon as there is reason to suspect it helps; L3's cost
scales with the working span and its publication covers exactly the working span; a ruled-out reading is published, not
dropped; evidence-class facts are published broadly, each with its establishment status; which effort dials exist, and
their defaults, is deferred (D-202).

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. Rule (ii) would put into L3's specification, as part of a ratified rule, a sentence the
ruling declined (*"never by a backward edge"*), which the record finds *"wider than **D-466** … and than L3-S38 as
ratified"* (record lines 50–52); the surface derived the narrower wording from those two and from *"The user's rule of
2026-10-07: no design rule may block the ultimate objective in the long run."* (surface line 181). Rule (i) writes the
wording ratified, and nothing else. Nothing in the analysis changes either way; what changes is whether the
specification's text for part E carries a sentence the ruling did not adopt. So the derivation is put for ratification,
not as a menu. The one variant is the list's weak point above.

**To do at release:** in Task 1 (c) item 3, after its last sentence (dispatch line 5057), add the sentence above; change
§L.27's *Open* point (2) (lines 2348–2351), its check note's sentence *"For part E, both item 3 (i) … not settled
here."* (lines 2363–2365) and the check row's two passages on part E (line 20), each for part E, to point to the ruling;
change the working list's (lxxiii) *To do at release* (its lines 3426–3428) to point to the ruling; former wordings kept.

---

## Site 21 — Item (lxxvi): §L.12's points (5) and (6), the sections record's amendment 3 and the check sum of its 36 rows

*Added by the sitting booted on entry 763. One item on its own, as entry 744 §2 item 4 puts it [checked: entry 744 lines
67–68, (lxxvi) §L.12 (5) and (6), list line 3570].*

Its list item opens at list line 3570 [checked: a search for the item number] and runs to line 3634; its read list is the
paragraph just above it (list lines 3565–3569) [checked].

**Documentation only. It does not change the algorithm as the specification defines it.** It settles two open points of
one ledger entry: where an amendment the dispatch already handles is handled, and which of the sections record's 36
rows the entry's table does not name. No row gets a new line and nothing about what the analysis does changes.

### What the question is, from scratch

On 2026-11-03 you gave three rulings in the sections record (`cowork_rulings_2026_11_03_l3_sections_sitting.md`, read
whole): sections are a weighed L3 decision over whole phrases (Ruling 1), sections may contain sections (Ruling 2), and
L3 works out form-function names (Ruling 3). The record names its rows at §0 (lines 16–19): the reading file's §7,
*"27 DIFFERS — 26 at L3-S22, 1 at L3-S23, 0 at L3-S24 — and 9 AGREES"*, 36 rows in all.

The dispatch's ledger entry for that record is §L.12 (dispatch lines 901–1000, its heading found by a search). Its
*Open* note leaves two points for this sitting [checked: lines 973–974]:

> (5) Amendment 3: see §L.11's *Open* point (1). (6) The check sum above. Until (1) to (4) and (6) are settled, those
> rows and amendments are STOP-and-report.

Its check note ends *"Points (1), (3), (5) and (6) stand."* (line 980).

**Point (5)** is about amendment 3 (lines 921–923): the record's *"L3-S23's family (iv) to be updated from "not filled"
to reading L1's relation."*, with *"No replacement wording"*, and *"This is the same amendment §L.11 amendment 4 orders,
ordered by two records; it is ONE amendment, and §L.11's handling binds it."*

**Point (6)** is about the check sum (lines 951–954):

> **Check sum at the rows:** the table places 12 + 4 + 1 + 10 + 3 = 30 row entries. The record also names Rows 57.352
> and 19.39 (iii) as agreeing with Ruling 1's item (2), and places neither. **Whether these 32 are the 36 of §0, and
> which rows of the 36 the record leaves unnamed, is not established by this entry** (the reading file's §7 not read by
> the sitting that wrote it; whether the four section-side rows are among the 36 is not stated by the record).

So two questions: is point (5) already handled elsewhere in the dispatch, and which rows of the 36 does §L.12's table
leave out, and what do they get?

### What the record already says

**Point (5) is already settled in the dispatch** [checked]. §L.11's check note says *"Point (1) is settled by Task 1 (c)
item 1: STOP-and-report, no words supplied."* (dispatch lines 886–888). Task 1 (c) item 1 names this amendment under
both entries, *"L3-S23 family (iv)'s "not filled" (§L.11 amendment 4 and §L.12 amendment 3, one amendment)"*, and says
of each amendment it lists: *"STOP-and-report, as form (a) already fixes"*, *"No words are supplied by this
dispatch"*, *"Each is listed in the report under *amendments with no words from the record*, with the record's sentence
that orders it"* (lines 5032–5040). The record itself gives no replacement words (its line 67). So §L.12's point (5) is
a pointer to a point Task 1 (c) item 1 settles.

**The 36 rows, read at the reading file's §7** [checked: lines 78591–78604]:

- L3-S22: AGREES 4 (Rows 19.39 (iii), 38.61, 38.72, 57.352); DIFFERS 26.
- L3-S23: AGREES 2 (Rows 36.50, 40.5 (iii)); DIFFERS 1 (Row 7.34).
- L3-S24: AGREES 3 (Rows 8.23, 8.35 (i), 8.113 (ii)); DIFFERS 0.

4 + 26 + 2 + 1 + 3 + 0 = 36, which is the record's 27 DIFFERS and 9 AGREES.

**The table's 30 row entries are 30 of the 36** [checked: §L.12's table, lines 943–949, against §7 line 78594]. L3-S22's
26 DIFFERS are the table's twelve overtaken rows, its four section-side rows and the ten rows of the record's Ruling 2:
12 + 4 + 10 = 26, each of the 26 found in line 78594's list and none of that list left over. So the four section-side
rows are among the 36, at L3-S22. The table's Row 7.34 is L3-S23's one DIFFERS. The table's Rows 8.23, 8.35 (i) and
8.113 (ii) are L3-S24's three AGREES; the record holds them (its Ruling 3, lines 155–158), and part 2 ruling record
Ruling 4 gives them their held line.

**The other six of the 36 are AGREES rows the table does not name:**

- Rows 57.352 and 19.39 (iii), named by the record inside Ruling 1's item (2): *"a section boundary is always a phrase
  boundary, phrases and sections read as one consistent grouping (L3-S22; the derivation's §7 point 6; rows 57.352 and
  19.39(iii) agree)"* (record lines 52–54), and again in its check correction (4), on quotations joined across the two
  (line 86).
- Rows 36.50, 38.61, 38.72 and 40.5 (iii), named by the record only in its list of rows read (§7, lines 213–215), as a
  search of the record for the four numbers shows (line 214 alone).

**The record places none of the six** [checked]. Its documentation paragraphs list the rows to be re-marked (lines
62–69, 111–113 and 154–159), and none of the six is among them. Item (2) names the two rows as rows that agree with it,
and orders no act for them. That is Ruling 19's case (a ruled text that names rows to say something else, and orders no
act for them), not Ruling 14's (a ruled text that says what the act does with rows it names).

**No ruling the dispatch carries places any of the six** [checked]. A search of the whole dispatch for *"36.50"*,
*"38.61"*, *"38.72"* and *"40.5"* not preceded by a digit or a point and not followed by a digit meets nothing. The
same search for *"57.352"* meets the check row (line 20) and §L.12 (lines 951 and 956). For *"19.39"*, claim (iii) is met
in the check row (line 20), at §L.12 (lines 952, 956 and 962), and in other entries' notes on Row 19.39's claims (lines
2244, 2673, 4204 and 4870), each giving claim (iii) as §L.12's, as the search returned them; none of those places it. So the route ruling's
*"Rows no family reaches stay proposals."*, which the ledger reads *"So a row no record names gets NO line."* (dispatch
lines 101–102), governs, as at Rulings 12, 13 and 16 to 20.

**The dispatch already gives the six no line, and says how** [checked]. §L.12's *"Rows the record mentions and does not
place"* (lines 956–958) names Rows 57.352 and 19.39 (iii) and *"the rows its §7 lists as read"*, with *"**No line from
this record** for any of them."* Task 3 (a) says *"A row-part a §L entry lists under *Rows the record mentions and does
not place* … gets no line from that record."* (lines 5157–5159). The four rows named only at the record's §7 fall under
*"the rows its §7 lists as read"*, but the sentence does not name them.

**What each of the six proposes, read at §6** (each found by the row-heading search, read by offset):

- Row 19.39 (iii): **ADOPTED — carried** (L3-S22) (line 24509); its axis, L3-S22 **AGREES** — *"A section boundary is
  always a boundary of the phrase reading."* (lines 24501–24502).
- Row 57.352: **ADOPTED — carried** (L3-S22), *"as Row 19.39 (iii)"* (line 74554); its axis, L3-S22 **AGREES** — *"A section boundary is always a
  boundary of the phrase reading."* (line 74552).
- Row 38.61: **ADOPTED — carried** (L3-S22), *"read beside Row 3.3"* (lines 47653–47654).
- Row 38.72: **ADOPTED — carried** (L3-S22) (line 47824).
- Row 40.5 (iii): **ADOPTED — carried** (L3-S23) (line 54110).
- Row 36.50: **RELOCATED** — to ***L1 — Change points, candidates and notated evidence***, *"whose rule IC-L1 S-43
  states, as L3-S23 cites it"* (lines 40900–40901); its axis L3-S23 **AGREES** (line 40898).

With no line, each keeps its proposal as a proposal, and each still reads true.

**One record; no line written.** Row 19.39's other claims have their lines from other entries ((ii) by Ruling 10;
the others as §L.12's own list says, lines 960–962). Claim (iii) and the other five get no line, so form (b)'s
two-record rule (Ruling 3) does not arise for them.

**No ruling of the two release records answers it** [checked]. A search of the part 2 ruling record and of the part 1
release record for *"§L.12"*, *"36.50"*, *"38.61"*, *"38.72"*, *"40.5"*, *"57.352"*, *"19.39"* and *"7.34"* meets the
part 2 record only: Ruling 4 (§L.12's point (3), the three held rows), Ruling 10 (Row 19.39 (ii)) and Ruling 32 (§L.12's
line 945, Row 19.59 (iv)). None answers point (5) or (6).

Applying D-599: the dispatch settles point (5) through Task 1 (c) item 1; the reading file's §7 closes the check sum;
the record places none of the six; the route ruling and Task 3 (a) give them no line. What is put to you is the
ratification of that derivation and of the wording below.

### The wording the writing side proposes

- **§L.12's *Open* point (5)** (dispatch line 973) is rewritten to point to the ruling: *"(5) Amendment 3 is §L.11's
  amendment 4, one amendment; it is settled by Task 1 (c) item 1 (STOP-and-report, no words supplied, listed under
  *amendments with no words from the record*), as §L.11's point (1) is."*
- **§L.12's *Open* point (6)** (lines 973–974) is rewritten to point to the ruling: *"(6) The check sum closes at the
  reading file's §7; the six rows of the 36 the table does not name get no line."* The sentence *"Until (1) to (4) and
  (6) are settled, those rows and amendments are STOP-and-report."* then holds for points (1) and (2) only, point (3)
  pointing to Ruling 4 by that ruling's *To do* and point (4) being settled by the check note.
- **The check sum's sentence** *"Whether these 32 are the 36 of §0, … is not established by this entry (…)"* (lines
  952–954) is replaced, the former wording kept, with:

  > These 30 row entries and the two named rows are 32 of the 36 of §0, read at the reading file's §7 (lines
  > 78591–78604): L3-S22's 26 DIFFERS are the twelve overtaken rows, the four section-side rows and Ruling 2's ten;
  > L3-S23's one DIFFERS is Row 7.34; L3-S24's three AGREES are Rows 8.23, 8.35 (i) and 8.113 (ii), held. The other
  > four of the 36 are AGREES rows the record names only in its §7 list of rows read: Rows 38.61 and 38.72 (at L3-S22)
  > and Rows 36.50 and 40.5 (iii) (at L3-S23). So the six rows of the 36 the table does not name are Rows 57.352,
  > 19.39 (iii), 36.50, 38.61, 38.72 and 40.5 (iii), all AGREES at §7; the record places none of them (part 2 ruling
  > record, Ruling 35).

- **In *"Rows the record mentions and does not place"*** (lines 956–958), after *"and the rows its §7 lists as read"*,
  this is added: *"— among them, of the 36, Rows 36.50, 38.61, 38.72 and 40.5 (iii), which the record names nowhere
  else (part 2 ruling record, Ruling 35)"*. *"No line from this record"* stands.
- **The check note's** *"Points (1), (3), (5) and (6) stand."* (line 980) and **the check row's** *"Left for the
  releasing sitting, as the entries say: … §L.12 points (1), (2), (3), (5) and (6)."* (line 20), each for points (5) and
  (6), are rewritten to point to the ruling.
- **In the report:** no listing of its own. Amendment 3 is listed under *amendments with no words from the record* by
  Task 1 (c) item 1, as it already is. The six rows are not STOP-and-report once point (6) points to the ruling, so Task
  3 (a)'s *rows the act could not place* does not reach them. Task 5's full close restates every §L entry's *Open*
  points under *"The points that are not this batch's"* (dispatch lines 5518–5521), and points (5) and (6) reach you
  there, as Rulings 12, 13 and 16 to 20 have it.

### Weak points the writing side fixed before putting this

- **Four rows the list had not read.** The list read only Rows 19.39 and 57.352 at §6 and said of the other four that
  *"their proposals are not stated here"* (list lines 3621–3622). They are read above. Three propose an ADOPTED word;
  **Row 36.50 proposes RELOCATED to L1**, not an ADOPTED word. That changes nothing here: none of the six gets a line,
  whatever it proposes.
- **Grounds the list used before they were ruled.** The list says *"The 30 rows take their lines as this list sorts them
  ((x), (xi), (liii), (liv), and the table's form (b-H) line for Ruling 2's ten)"* (list lines 3613–3614). Items (x),
  (xi) and (liii) are not ruled in either release ruling record: a search of both for *"§L.12"* and for the item
  numbers *"(x)"*, *"(xi)"* and *"(liii)"* meets only Rulings 4 and 32 of the part 2 record, neither on them. So this
  item says nothing about how the 30 are lined: that is §L.12's table and its points (1) to (3), point (3) ruled by
  Ruling 4, and none of them is touched here. The accounting calls the three L3-S24 rows *"held"*, as Ruling 4 does, not
  *"placed"*.
- **The dispatch line the list relayed.** The list cites line 101 as relayed. It is read above (lines 101–102).
- **Where the four rows are named.** The list proposes to *"name Rows 36.50, 38.61, 38.72 and 40.5 (iii) as the rows of
  the 36 that its §7 lists as read"* (list lines 3633–3634). The record's §7 list of rows read also names rows outside
  the 36 (for example Rows 3.2, 3.4 and 41.63, within its *"3.1 to 3.4"* and its *"41.63"*, lines 213–215), so *"the rows its §7 lists
  as read"* is kept and the four are named beside it, not in its place.
- **The list's *To do* left out a place.** It does not name the check row's *"Left for the releasing sitting, as the
  entries say: … §L.12 points (1), (2), (3), (5) and (6)."* (line 20). Added, for points (5) and (6).
- **The list's own *To do*.** The list does not say its own (lxxvi) *To do* is to point to the ruling; added below.

### The weak point, stated by the working list

That the record's *"rows 57.352 and 19.39(iii) agree"* names the two rows as support for item (2) and does not place
them is the writing side's reading, resting on the documentation paragraphs, which list the rows to be re-marked and
not these two (list lines 3617–3619). If you read it as placing them, each would get a line **ADOPTED — carried
(L3-S22)**, the word each already proposes; only whether a ruled line is written would change. Documentation only either
way.

### Not read, not decided here

The reading file was read at §7's L3-S22 to L3-S24 entries and at the six rows' §6 entries; the derivation and the
successor were not opened. §L.12's *Open* points (1) and (2) (the list's items (liii), (x) and (xi)), its point (3)
(Ruling 4) and its point (4) (settled by its check note), the table's lines for the 30, Row 41.63, and Row 19.39's other
claims are not touched. How the 30 rows are lined is not decided here.

### The currently decided method

Unchanged by this item [checked: the sections record, lines 50–57, 95–97 and 135–138]: sections are a weighed L3
decision over groups of whole phrases, on L3-S23's four families of evidence, no single item forcing or forbidding a
section boundary, published with rivals and their mass; a section boundary is always a phrase boundary; sections may
contain sections to any depth, each level tiling the level above, how many levels a passage has left to the evidence and
the measured weights, UNESTABLISHED until measured; L3 works out, for each section at every level of the nesting, a
form-function name where the chosen naming scheme has one, "no name" a possible reading, each published with rival names
and their mass, UNESTABLISHED until measured against a ground truth; which naming scheme stays open.

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. Point (5) is already settled by Task 1 (c) item 1, and §L.12 says of the amendment
*"§L.11's handling binds it"*; leaving it open in §L.12 keeps open a point Task 1 (c) item 1 settles. Point (6) is a count, and the reading
file's §7 answers it; leaving it open would keep a STOP-and-report on rows the dispatch already gives no line. Nothing in
the analysis changes either way; what changes is whether §L.12 says which of its 36 rows it leaves as proposals. So the
derivation is put for ratification, not as a menu. The one variant is the list's weak point above.

**To do at release:** rewrite §L.12's *Open* points (5) and (6) (dispatch lines 973–974) as worded above, pointing to
the ruling; replace the check sum's sentence (lines 952–954) with the accounting above; add the four rows beside
*"the rows its §7 lists as read"* (lines 956–958); change the check note's *"Points (1), (3), (5) and (6) stand."*
(line 980) and the check row's *"… §L.12 points (1), (2), (3), (5) and (6)."* (line 20), each for points (5) and (6), to
point to the ruling; change the working list's (lxxvi) *To do at release* (its lines 3629–3634) to point to the ruling;
former wordings kept.

---

## Site 22 — Item (lxxviii): §L.23's point (2), the 20 rows you placed before L3-S38 was ratified: their earlier ruling's line only, or also a line naming the ratification record's Ruling 1

*Added by the sitting booted on entry 764. One item on its own, as entry 744 §2 item 4 puts it [checked: entry 744 lines
67–68, (lxxviii) §L.23 (2), list line 3721].*

Its list item opens at list line 3721 [checked: a search for the item number]; its read list is the paragraph just above
it (list lines 3715–3720) [checked].

**Documentation only. It does not change the algorithm as the specification defines it.** It settles how many lines the
act writes beneath 20 rows of the L3 reading file that you have already placed HISTORICAL. Nothing about what the
analysis does.

### What the question is, from scratch

L3-S38 is the L3 statement *"L3 never revises L2, and L2 reads nothing L3 publishes."* (its first sentence, as the
ratification record quotes it, lines 28–29). 100 row-parts of the L3 reading file read DIFFERS against it (the
ratification surface, line 32, citing the reading file's §7). They were filed in eight batches, called cuts. You placed 20 of them yourself, in two rulings of
2026-11-03:

- **First-cut Ruling 1** (`cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md`, read whole), your word *"a"*: twelve
  rows HISTORICAL — Rows 2.3 claim (i), 7.15, 7.28 claim (ii), 7.55, 7.130, 7.131, 7.132, 7.149, 7.150, 7.191, 7.194 and
  7.311 (record lines 25–29).
- **Second-cut Ruling 1** (`cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md`, read whole), your word *"A"*: eight
  rows HISTORICAL — Rows 10.23 claim (i), 10.147 claim (ii) and 10.178, and five rows of the first cut *"re-filed from
  QUARANTINED"*: Rows 7.13 claim (i), 7.17 claim (i), 7.46, 7.56 and 7.135 (record lines 31–37).

Both rulings place their rows in the words *"HISTORICAL — rules of a superseded design"*, from the comparison's
proposal RELOCATED to *L2 — The tonal reading. The one entangled decision.* 12 + 8 = 20.

The same day you ratified L3-S38 itself, by Ruling 1 of the ratification record
(`cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md`, read whole), your word *"yes"*. It ratifies the statement
with (record lines 33–36):

> **the 100 DIFFERS** as the eight cuts file them — HISTORICAL 89, QUARANTINED 9, RELOCATED 2 (Row 2.6 to L2 naming
> L2-S30; Row 10.206 to L2 naming L2-S43); 20 of them by the user's earlier rulings (first-cut Ruling 1, second-cut
> Ruling 1), the other 80 this side's derivation in their grounds, ratified with the statement as boundaries Ruling 2
> did for its rows;

**What the dispatch writes now** [checked]. §L.21's table gives the twelve a form (b) line naming first-cut Ruling 1
(dispatch line 1779). §L.22's table gives the eight a form (b) line naming second-cut Ruling 1 (lines 1849–1850). For the
five re-filed rows §L.21's table says *"**No line from this record.**"* and *"the line is §L.22's"* (line 1783). §L.23's
table gives *"The 20 DIFFERS ruled earlier"* as *"**HISTORICAL**; the lines are §L.21's and §L.22's"* (line 1934), and
§L.23 says of the others *"So the 80 derived rows get ruled lines, form (b), naming this record's Ruling 1"* (lines 1913–1914).
But §L.23's *Open* point (2) leaves the 20 to you (lines 1977–1979):

> (2) The 20 rows ruled earlier: on the writing side's reading each gets its earlier ruling's line only, because the
> record counts them as ruled already and ratifies *"the other 80"* with the statement. Whether they also get a line
> naming this Ruling 1 is to be confirmed before release.

Its check note: *"Ruling 1's "the 100 DIFFERS as the eight cuts file them" reaches the 20 earlier rows by count, not by
row, which does not settle whether they also get a line naming it."* (lines 1994–1996). The check row (line 20, by a
bounded search) lists it among what is *"Left for the releasing sitting"*: *"(2) (whether the 20 earlier rows also get a
line naming the ratification record's Ruling 1)"*.

So the question: does each of the 20 rows get one line (its earlier ruling's), or two (its earlier ruling's, and a second
naming the ratification record's Ruling 1)?

### What the record already says

**The ratification record names other rulings as the source of the 20** [checked]. Its words *"20 of them by the user's
earlier rulings (first-cut Ruling 1, second-cut Ruling 1), the other 80 this side's derivation in their grounds,
ratified with the statement"* (record lines 33–36) set the 20 apart: it names their rulings, and what it ratifies *"in
their grounds"* is the 80. The strongest point against it, as put, concerns the 80 only: *"ratifying with the placements
ratifies the 80 derived groundings too; each stays challengeable at its row"* (lines 45–47); its surface
(`ratification_surfaces/cowork_l3_s38_ratification_surface_2026_11_03.md`) says the same, *"80 of the 100 DIFFERS
filings are this side's derivation, not the user's word"* (surface lines 98–99), and its table counts the 20 in a column
headed *"Ruled by the user"*: *"12 by first-cut Ruling 1 ("a"); 5 more by second-cut Ruling 1"* and *"3 by second-cut
Ruling 1 ("A")"*, total 20 (surface lines 38–41, 48). The record names none of the twenty row numbers [checked: read
whole].

**"As the eight cuts file them" points, for the 20, to those rulings** [checked]. The first-cut record's §1b, as amended
by second-cut Ruling 1, files the cut as *"the twelve of Ruling 1, the five of that ruling, and the twelve derived"* (its
lines 55–59). The second-cut record's §2 files *"the three of Ruling 1"* (line 66) and, for the first cut, *"the five of
this Ruling 1"* (line 75). So the filing the ratification adopts is, for these 20, the placements of those two rulings.

**Each earlier record orders the re-marking of its own rows** [checked]. First-cut record: *"The rows are re-marked, and
the 33 rows other than 2.6 taken off the reading file's §10 row by row, by the application dispatch, not now."* (lines
69–70). Second-cut record: *"The rows are re-marked, and taken off the reading file's §10 row by row, by the application
dispatch, not now."* (lines 89–90). The ratification record's own documentation sentence, *"the 100 DIFFERS and Rows
3.5(ii), 3.15 re-marked, and the rows the reading file's §10 carries taken off it row by row, by the application
dispatch, not now"* (lines 54–55), counts the 20 among the rows re-marked. The record does not say which line re-marks
them; §L.21's and §L.22's lines do.

**Why the 80 are different** [checked at the dispatch and the record]. §L.23 gives the 80 a line naming Ruling 1 (lines
1913–1914; its table, lines 1935–1936): the record counts them as *"this side's derivation in their grounds, ratified
with the statement"*, not as placed by your earlier rulings. For each of the 20 the record names a ruling of yours.

**The transfer list (§10): item 6 reaches the 20 through their one line** [checked: Task 3 (c) item 6, dispatch lines
5210–5216]. Item 6 adds ONE
*LEAVES L3* line beneath each §10 entry whose row carries a ruled line from §L.21, §L.22, §L.23 or §L.24, quoting that
record's sentence. The 20 carry §L.21's or §L.22's line, so item 6 reaches them with those records' sentences, each of
which orders the taking-off (quoted above). Whether and where each of the 20 stands on §10 was not read by this sitting.

**One record's line per row; form (b)'s two-record rule does not arise** [checked]. A search of the whole dispatch for
the twenty row numbers, not preceded by a digit or a point and not followed by a digit, meets them at §L.21 (lines
1765, 1779, 1783, 1809), at §L.22 (lines 1835, 1849, 1850, 1877) and at §L.19 (lines 1607, 1616); the two §L.19 hits
name L2 Row 7.13 (ii), a row of the L2 reading file. Lines 1765 and 1835 fall inside alternatives the rulings declined.
The five re-filed rows are named at both §L.21 and §L.22; the first-cut record's amendment hands them to the second-cut
ruling (its lines 55–59), so they take §L.22's line only, as §L.21's table says (line 1783). With no line from the
ratification record, each of the 20 carries one line.

**No ruling of the two release records answers it** [checked]. A search of the part 2 ruling record for *"§L.21"* to
*"§L.23"*, *"L3-S38"*, *"first cut"* and *"second cut"* (either spelling), *"s38"*, *"ratification record"* and the item
numbers *"(xli)"*, *"(xlii)"*, *"(xliv)"*, *"(lv)"* and *"(lxxviii)"*, in any case, meets Ruling 7 (lines 272, 277,
306), Ruling 13 (lines 583, 601), Ruling 18 (lines 875–876, 895), Ruling 21 (on L2-S38) and Ruling 34 (line 1910), none
on §L.23's point (2). A search of the part 1 release record for *"§L.21"* to *"§L.23"*, *"L3-S38"*, *"first-cut"*,
*"second-cut"*, *"s38"* and the item numbers *"(xli)"* to *"(xlvi)"* and *"(lv)"*, in any case, meets nothing; its
rulings, found by a heading search, are on Questions 1 to 5.

Applying D-599: the ratification record itself names first-cut Ruling 1 and second-cut Ruling 1 as the source of the
20; those records order the re-marking; §L.21's and §L.22's lines carry it; a second line would repeat the same word on
the same claim under a ruling that names other rulings for these rows. What is put to you is the ratification of that
derivation.

### The wording the writing side proposes

- **At the rows:** each of the 20 keeps the one form (b) line §L.21 or §L.22 already gives it (dispatch lines 1779,
  1849–1850); no line naming the ratification record's Ruling 1 is added. The five re-filed rows take §L.22's line only,
  as §L.21's table says (line 1783).
- **§L.23's *Open* point (2)** (dispatch lines 1977–1979) is rewritten to point to the ruling: *"(2) The 20 rows ruled
  earlier get their earlier ruling's line only, from §L.21 or §L.22: the record names first-cut Ruling 1 and second-cut
  Ruling 1 as their source; no line naming this Ruling 1 is added (part 2 ruling record, Ruling 36)."*
- **Its check note's** *"Points (1) and (2) stand for the releasing sitting"* (line 1994), and the clause that follows on
  point (2) (lines 1995–1996), and **the check row's** *"and (2) (whether the 20 earlier rows also get a line naming the
  ratification record's Ruling 1)"* (line 20), each for point (2), are rewritten to point to the ruling.
- **In the report:** no listing of its own. The rows are not STOP-and-report and carry one record's line each, so
  neither *rows the act could not place* nor *rows named by more than one record* reaches them on this point. Task 5's
  full close restates every §L entry's *Open* points under *"The points that are not this batch's"* (dispatch lines
  5518–5521), and point (2), pointing to the ruling, reaches you there, as Rulings 12, 13 and 16 to 20 have it.

### Weak points the writing side fixed before putting this

- **Grounds the list used before they were ruled.** The list contrasts the 20 with *"the 45 of cuts 3 to 8"*, saying
  *"(xli) to (xlvi) gave each of the 45 a line naming Ruling 1"* (list lines 3745–3746), and with item *"(lv)"* (lines
  3750–3752). Neither release record has a ruling on items (xli) to (xlvi) or (lv) as items (the searches above); the
  subject of the part 2 record's Ruling 7 is the audit-list point of (xliii), (xlv) and (xlvi) (its heading, line 265). The contrast is made above from §L.23's
  own words (line 1914 and its table, lines 1935–1936), checked on 2026-11-09, which give the 80 derived rows a line
  naming Ruling 1; (xli) to (xlvi) and (lv) are not relied on.
- **A sentence of the record the list did not quote.** The ratification record's documentation sentence (lines 54–55)
  counts all 100 among the rows re-marked by the act. It is quoted above, with the reason it does not call for a second
  line: §L.21's and §L.22's lines re-mark the 20.
- **The list's *To do* left out a place.** It names §L.23's *Open* point (2) and the check note. The check row's passage
  on point (2) (line 20) is added.
- **The list's own *To do*.** The list does not say its own (lxxviii) *To do* is to point to the ruling; added below.

### The weak point, stated by the working list

That *"as the eight cuts file them"* gives the 20 the earlier rulings' lines, and not also a line of its own, is the
writing side's reading of *"20 of them by the user's earlier rulings"* (list lines 3764–3766). If you read Ruling 1 as
placing all 100 itself, each of the 20 gets a second form (b) line naming it, **HISTORICAL**, the same word on the same
claim; under form (b) (as Ruling 3 has it, by part) both are written, the row is listed under *rows named by more than one
record*, and nothing stops (list lines 3766–3768). Documentation only either way.

### Not read, not decided here

The L3 reading file was not opened: the 20 rows' entries, §6 and §10 were not read. The six cut surfaces, the first-
and second-cut surfaces, the boundaries record and L3-S38 at the derivation were not opened. §L.23's *Open* points (1)
(the 45 rows of cuts 3 to 8, sorted at the list's (xli) to (xlvi), not ruled), (3) and (4) (answered by its check note),
§L.21's and §L.22's lines and *Open* points, and the L2 twins the three records carry open are not touched.

### The currently decided method

Unchanged by this item [checked: the ratification record, lines 49–53]: *"**No change against the currently decided
method**"*: L3 reads everything L2 publishes (its reading, its rivals with mass) plus L0's and L1's published facts, and
nothing else (L3-S37, ratified); never revises L2; L2 reads nothing L3 publishes; a backward edge is tested by
measurement as soon as there is reason to suspect it helps; key areas read off L2's principal reading, a new one at every
change of tonality (key-areas Ruling 2). *"No inference changes."*

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. Nothing in the analysis changes either way, and either way each of the 20 reads HISTORICAL
in the same words. A second line would add, beneath each row, a ruling that itself names another ruling as the row's
source, and would put 20 rows under *rows named by more than one record* for a repetition, not for two records that each
place them; one line keeps one home for each placement (#6). So the derivation is put for ratification, not as a menu.
The one variant is the list's weak point above.

**To do at release:** rewrite §L.23's *Open* point (2) (dispatch lines 1977–1979) as worded above, pointing to the
ruling; change its check note's *"Points (1) and (2) stand for the releasing sitting"* and its clause on point (2)
(lines 1994–1996) and the check row's passage on point (2) (line 20), each for point (2), to point to the ruling; change
the working list's (lxxviii) *To do at release* (its lines 3774–3776) to point to the ruling; former wordings kept.

---

## Site 23 — Item (lxxx): §L.40's point (4), Row 40.61 and the *⚠gap* mark on D-522's home: what the mark means, and whether the act writes anything for it

*Added by the sitting booted on entry 765. One item on its own, as entry 744 §2 item 4 puts it [checked: entry 744 lines
67–68, (lxxx) §L.40 (4), D-522's gap mark, list line 3838].*

Its list item opens at list line 3838 [checked: a search for the item number meets lines 3442, 3838, 3999 and 4240; the
item's heading is at 3838]; its read list is the paragraph just above it (list lines 3830–3837) [checked].

**Documentation only. It does not change the algorithm as the specification defines it.** It settles what the act does
about a mark in the decisions register's index beside the decision one row rests on. Nothing about what the analysis
does.

### What the question is, from scratch

**The row.** Row 40.61 of the L3 reading file is the sentence *"If the evidence trail behind every inference is
published — which pitch classes drove the key, which cadence vote confirmed the modulation, which margin separated the
winner from the runner-up, why the analyzer abstained — then "show me why" is a late-bound DISPLAY consumer of facts that
already exist, not a new analysis."* (reading file lines 55085–55088) [checked: found by the row-heading search, line
55083, read to line 55102]. In plain words: if the analysis publishes the evidence behind each answer, then explaining an
answer to the user is a display job, not a new analysis.

**The ruling.** The display-family record (`cowork_rulings_2026_11_07_l3_display_family_sitting.md`, read whole), your
word *"yes"*, places it: *"ADOPTED (3): … Row 40.61, on D-522 (its home marked *⚠gap* at the index, not opened)."*
(record lines 32–33), and carries open *"What D-522's *⚠gap* mark at the index means (not opened)."* (line 57).

**The decision it rests on.** D-522 is the entry of the decisions register (the project's list of standing decisions,
each with a number) that says the same thing: *"Explaining an inference to the end user is a late-bound DISPLAY consumer
of facts that already exist — not a new analysis"*. Its line in the register's index, `DECISIONS.md`, ends with the home
column *"`cowork_evidence_inventory.md` §8b ⚠gap"* (line 302) [checked].

**What the dispatch writes now** [checked]. §L.40's table gives Row 40.61 a form (b) line quoting the record (dispatch
line 3460). Its *Open* point (4): *"Row 40.61 rests on D-522, whose home is marked *⚠gap* at the index; the record did
not open it."* (lines 3497–3498). Its check note ends *"Points (1) to (4) stand."* (line 3507). Its *Carried open* note
quotes the record's *"What D-522's ⚠gap mark at the index means (not opened)"* (line 3512). The check row (line 20, by
bounded searches) ends its §L.40 passage *"Left for the releasing sitting: §L.40 points (1) to (4)."*

So the question: does the *⚠gap* mark put the row's placement in doubt, and does the act write anything because of it?

### What the record already says

**What the mark is, read at the register** [checked]. The index's columns are *"ID | Decision | Status | Entry ratified |
Home"* (`DECISIONS.md` line 250), so the mark stands in the home column. The register's own key to that column, under
its heading *"How to read an entry"* (line 30): *"A decision about how a layer should work belongs in that layer's
section of `ARCHITECTURE.md`, and a decision about anything else belongs in the specification that owns it. Where the
home is neither, the entry says which of five cases it is: a **documentation gap** (a decision that governs a layer or a
component, not findable from that layer's section — it carries an `OPEN_ITEMS.md` row)"* (lines 55–59). D-522's full
entry (`decisions/group_C.md`, lines 1000–1023, read through) says it in those words: *"**Home.**
`cowork_evidence_inventory.md:215-224`  ⚠ **home is not the specification that owns it** — a documentation gap; see
`OPEN_ITEMS.md`."* (line 1019), and its home section *"§8b — `## 8b. Declared future consumers, named by the user
(2026-07-13)`"* is one that *"RECORDS FINDINGS"* (line 1021). The register's counts give *"— of which a documentation
gap | 19"* (line 151). So the mark says where D-522 is written: in a findings section of the evidence inventory, not in
a specification.

**The mark leaves the decision standing** [checked]. D-522's full entry: *"**Status.** LIVE · decided 2026-07-13 ·
ratified by user"* (line 1017), its *Why* recorded (line 1015). The index's *Entry ratified* column shows *"—"* (line
302); the key keeps that column apart from the decision: *"when this REGISTER ENTRY was reviewed and ratified … This is
a different event from the decision itself"* (lines 47–48). The entry's own *Provenance* ends *"NOT ratified — it enters
with the record's own status and goes to the user in this wave's ratification queue."* (line 1023), which is the same
register-entry event the *"—"* shows, not the decision, whose status line says *"ratified by user"*.

**So the record's method holds for the row** [checked]. The record adopts Row 40.61 by the architecture-rules ruling's
method, rows lying in the home of a LIVE register entry adopted on that entry (its surface,
`ratification_surfaces/cowork_l3_display_family_surface_2026_11_07.md`, R4, lines 82–86, and §2A, line 101). The reading
file records that the register homes D-522 at the evidence inventory's lines 215 to 224, *"the whole of range 9, on
which this row's sentence lies"* (reading file lines 55098–55102), and the register's entry gives the same lines (line
1019). D-522 is LIVE. The mark changes neither fact. The surface's own weak point, *"D-522's home is marked ⚠gap at the
index (what the gap is was not opened by this sitting)"* (line 101), is answered at the register.

**Nothing for the act to write from the mark** [checked]. The record *"allocates no decisions-register identity"* and
*"edits no tracked document"* (its §3, lines 64–66), and §L.40's *Register* note reads *"none"* (dispatch line 3509). A
search of `OPEN_ITEMS.md` for *"D-522"* meets nothing; the row the key speaks of was not looked for under any other term,
and the archive and the register's detail files were not searched. Whether placing the row bears on D-522's home class
is the register's and is not judged here.

**One record; form (b)'s two-record rule does not arise** [checked]. A search of the whole dispatch for *"40.61"*, not
preceded by a digit or a point and not followed by a digit, meets lines 3460, 3473, 3493, 3497 and 3505, all within
§L.40; a search for *"D-522"* meets lines 3445, 3460, 3497, 3509 and 3512, within §L.40 (its heading at line 3437, the
next at 3517), and line 2368, in a list of register identities that the list and Ruling 34 place in §L.27's *Register*
note, naming D-522 as a ground and placing no row [relayed: line 2368 seen only as the search returned it].

**No ruling of the two release records answers it** [checked]. A search of the part 2 ruling record for *"D-522"*,
*"40.61"*, *"§L.40"*, *"gap"*, *"(lxxx)"*, *"display-family"* and *"display family"*, in any case, meets Ruling 1 (lines
18, 42, 46: §L.40's point (2)), Ruling 9 (lines 363–413: §L.40's point (1), with *"(lxxx)'s own answer to §L.40 (4) is
not ruled here"*, line 409), Ruling 7 (line 272, *"gaps"* in another sense), Ruling 21 (line 1090, the same) and Ruling
28 (line 1475, a heading search list); none on point (4). A search of the part 1 release record for *"D-522"*,
*"40.61"*, *"§L.40"*, *"⚠gap"*, *"(lxxx)"*, *"display-family"* and *"display family"*, in any case, meets line 102 only,
the display-family record named on Rows 4.6, 4.18 and 4.19; nothing on point (4).

Applying D-599: the register's own key and D-522's own entry say what the mark means; the decision is LIVE; the row lies
in its home; the record's placement rests on those facts, and the mark changes none of them; the dispatch bars the act
from writing words no record gives. What is put to you is the ratification of that derivation.

### The wording the writing side proposes

- **At the row:** nothing changes. Row 40.61 keeps the one form (b) line §L.40's table gives it (dispatch line 3460);
  nothing is added for the mark. Which ADOPTED word that line writes is Ruling 9's, not this site's.
- **§L.40's *Open* point (4)** (dispatch lines 3497–3498) is rewritten to point to the ruling: *"(4) Row 40.61 rests on
  D-522, whose home is marked *⚠gap* at the index. Read at the register, the mark says D-522 is written outside the
  specification that owns it, in a findings section of the evidence inventory (a documentation gap: `DECISIONS.md`
  lines 55–59; `decisions/group_C.md` line 1019); D-522 is LIVE (group_C.md line 1017) and the row lies in its home. The
  record's ADOPTED placement on D-522 stands; nothing is added to the dispatch for the mark (part 2 ruling record,
  Ruling 37)."*
- **Its check note's** *"Points (1) to (4) stand."* (line 3507), **the *Carried open* note's** *"What D-522's ⚠gap mark
  at the index means (not opened)"* (line 3512), and **the check row's** *"Left for the releasing sitting: §L.40 points
  (1) to (4)."* (line 20), each for point (4), are rewritten to point to the ruling.
- **In the report:** no listing of its own; the row is not STOP-and-report on this point. Task 5's full close restates
  every §L entry's *Open* points under *"The points that are not this batch's"* (dispatch lines 5518–5521), and point
  (4), pointing to the ruling, reaches you there, as Rulings 12, 13 and 16 to 20 have it.

### Weak points the writing side fixed before putting this

- **A fact the list sent to A1, now ruled.** The list's paragraph *"A fact found at the row, for A1, not settled here"*
  reads Row 40.61 under A1's rules (i) to (v) and finds it meets rule (v) (list lines 3871–3876). Ruling 9 replaced those
  rules (*"The working list's rules (i) to (v) are not written into form (b); this paragraph takes their place"*) and
  took the fact up for §L.40's point (1) (*"Row 40.61 **ADOPTED — proposed**"*, the writing side's reading, not
  applied). It is not relied on here.
- **A sentence of D-522's entry the list did not quote.** The entry's *Provenance* ends *"NOT ratified"* (group_C.md
  line 1023). It is quoted above, with why it does not reach the decision: it is the register-entry event, kept apart by
  the key.
- **The list's *To do* left out a place.** It names §L.40's *Open* point (4), the check note and the *Carried open*
  note. The check row's *"Left for the releasing sitting: §L.40 points (1) to (4)."* (line 20) is added.
- **The list's own *To do*.** The list does not say its own (lxxx) *To do* is to point to the ruling; added below.

### The weak point, stated by the working list

That the record's *"(not opened)"* asked only what the mark means, which the register's key answers, is the writing
side's reading (list lines 3880–3883). If you read it as a bar (no row adopted on a decision whose home is a
documentation gap until that gap is closed), the row stays a STOP-and-report and the question is yours. The record's
alternatives offered do not name Row 40.61. Documentation only either way.

### Not read, not decided here

`cowork_evidence_inventory.md` was not opened, nor the `OPEN_ITEMS.md` row the key says a documentation gap carries.
Whether placing the row bears on D-522's home class, and whether that gap is closed, are the register's and are not
decided here. §L.40's *Open* points (1) (Ruling 9), (2) (Ruling 1) and (3), Row 40.61's §10 standing, and D-522's
register entry are not touched.

### The currently decided method

Unchanged by this item [checked: the display-family record, lines 47–51]: L2 decides key and chord together and
publishes the chord as a degree in its tonality; L3 publishes facts read off it (chord symbol, figured bass, harmonic
rhythm, cadence with type at each phrase end, phrase and section grouping, key areas, the pivot re-expression); L3
publishes no tonic / subdominant / dominant summary and writes nothing into the score; the augmented-sixth sub-type is
L2's chord kind; a display turns published facts into text. *"The ruling adds no published fact, field, evidence or
check."*

### The alternatives, weighed towards the ultimate objective and the principles

They have collapsed to one. Nothing in the analysis changes either way. The mark is answered by the register's own key
and D-522's own entry; holding the row back for it would stop a placement you ratified on a fact that leaves its ground
untouched, and writing anything for the mark would put words no record gives into the act (the standing bars). So the
derivation is put for ratification, not as a menu. The one variant is the list's weak point above.

**To do at release:** rewrite §L.40's *Open* point (4) (dispatch lines 3497–3498) as worded above, pointing to the
ruling; change its check note's *"Points (1) to (4) stand."* (line 3507), the *Carried open* note's *"What D-522's ⚠gap
mark at the index means (not opened)"* (line 3512) and the check row's *"Left for the releasing sitting: §L.40 points (1)
to (4)."* (line 20), each for point (4), to point to the ruling; change the working list's (lxxx) *To do at release* (its
lines 3889–3892) to point to the ruling; former wordings kept.

---

## What this file does not yet carry

Nothing of entry 744 §2 item 4 [checked: entry 744 lines 52–68]: groups 1, 2, 3, 4, 5 and 6 are complete, and the four
items it puts on their own are taken by sites 20 to 23. *(Former wording, kept: "The rest of part 2, for later sites or
files, in the groups of entry 744 §2 item 4: the weak point of (lxxx), with its item, which entry 744 §2 item 4 puts on
its own [checked: entry 744 lines 67–68]. Groups 1, 2, 3, 4, 5 and 6 are complete." (lxxx) taken by site 23.)*
*(Former wording, kept: "… the weak points of (lxxviii) and (lxxx), each with its item, which entry 744 §2
item 4 puts on their own [checked: entry 744 lines 67–68]." (lxxviii) taken by site 22.)* *(Former wording, kept: "… the weak points of (lxxvi), (lxxviii) and (lxxx), each with its
item, which entry 744 §2 item 4 puts on their own [checked: entry 744 lines 67–68]." (lxxvi) taken by site 21.)*
*(Former wording, kept: "… the weak points of (lxxiii), (lxxvi), (lxxviii) and
(lxxx), each with its item, which entry 744 §2 item 4 puts on their own [relayed from entries 756 to 761]." (lxxiii)
taken by site 20.)* *(Former wording, kept: "… (lxxviii) and (lxxx), each with its item; and group
6's (lxxxiii), for site 19. Groups 1, 2, 3, 4 and 5 are complete." (lxxxiii) taken by site 19.)* *(Former wording, kept: "… the weak points of (lxiii), (lxxiii), (lxxvi), (lxxviii), (lxxx) and (lxxxiii),
each with its item. Groups 1, 2, 3, 4 and 5 are complete." (lxiii) taken by site 19.)*
*(Former wording, kept: "… the weak points of (lxiii), (lxviii), (lxxiii), … Groups 1, 2, 3 and 4 are complete; group
5's (lxviii) is for site 18." (lxviii) taken by site 18.)* *(Former wording, kept: "… the weak points of (lxiii), (lxiv), (lxviii),
… Groups 1, 2, 3 and 4 are complete." (lxiv) taken by site 18.)* *(Former wording, kept: "… the weak points of (lxiii), (lxiv), (lxviii), (lxxi), (lxxiii), … Groups 1, 2
and 3 are complete; group 4's (lxxi) is for site 17." (lxxi) taken by site 17.)* *(Former wording, kept: "… the weak points of (lxiii), (lxiv),
(lxviii), (lxx), (lxxi), … Groups 1, 2 and 3 are complete." (lxx) taken by site 17.)* *(Former wording, kept: "… the weak points of (lx), (lxiii), … Groups 1 and 2 are complete; group
3's (lx) is for site 16." (lx) taken by site 16.)* *(Former wording, kept: "… the weak points of (lix), (lx), (lxiii), …
Groups 1 and 2 are complete." (lix) taken by site 16.)* *(Former wording, kept: "… (lxxi), (lxxiii), (lxxiv), (lxxvi), … each with its item. Group
1 is complete; group 2's (lxxiv) is for site 15." (lxxiv) taken by site 15.)* *(Former wording, kept: "… (lxviii), (lxx) to (lxxiv),
… group 2's (lxxii) and (lxxiv) are for site 15." (lxxii) taken by site 15.)* *(Former wording, kept: "… the weak points of (lix), (lx),
(lxiii), (lxiv), (lxviii) to (lxxiv), … group 2's (lxix), (lxxii) and (lxxiv) are for site 15." (lxix) taken by site
15.)* *(Former wording, kept: "… the weak points of (lix),
(lx), (lxii) to (lxiv), … group 2's (lxii), (lxix), (lxxii) and (lxxiv) are for site 15." (lxii) taken by site 15.)*
*(Former wording, kept: "… the weak points of
(lix) to (lxiv), (lxviii) to (lxxiv), (lxxvi), (lxxviii), (lxxx) and (lxxxiii), each with its item. Group 1 is
complete." (lxi) taken by site 15.)*
*(Former wording, kept: "… item 4: group 1's (lxxxii), for site 14; and the weak points of …" (lxxxii) taken by site
14.)* *(Former wording, kept: "… group 1's (lxxix) and (lxxxii), for site 14; …" (lxxix)
taken by site 14.)* *(Former wording, kept: "… group 1's (lxvii), (lxxix) and (lxxxii), for site 14; …"
(lxvii) taken by site 14.)* *(Former wording, kept: "… group 1's (lxvi), (lxvii), (lxxix) and (lxxxii), for site
14; …" (lxvi) taken by site 14.)* *(Former wording, kept: "The rest of part 2, for later sites or files: the weak points of
(lix) to (lxxxiii) other than (lxxv), (lxxvii) and (lxxxi), each with its item." (lxv) taken by site 14.)* *(Former wording, kept: "The rest of part 2, for later sites or
files: the weak points of (lviii) and (lix) to (lxxxiii) …" (lviii) taken by site 13.)* *(Former wording, kept: "The rest of part 2, for later sites or
files: the weak points of (lvii), (lviii), …" (lvii) taken by site 12.)* *(Former wording, kept: "The rest of part 2, for later sites or
files: the weak points of (lvi), (lvii), …" (lvi) taken by site 11.)* *(Former wording, kept: "The rest of part 2, for later sites or
files: the weak points of (lii), (lvi), …" (lii) taken by site 10.)* *(Former wording, kept: "The rest of part 2, for
later sites or files: the weak points of (li), (lii), (lvi), …" (li) taken by site 9.)* *(Former wording, kept: "The rest of part 2, for
later sites or files: the weak points of (l), (li), (lii), …" (l) taken by site 8.)* *(Former wording, kept: "The rest of part 2, for
later sites or files: A1 and A2's rules with (lxxx)'s fact on Row 40.61; the weak points of …" A1 and A2 with (lxxx)'s
fact taken by site 7; (lxxx)'s own weak point stays with the rest.)* *(Former wording, kept: "The rest of part 2, for later sites or files: (lxxv)'s Task 0 fact with Part C; A1 and A2's
rules …; the weak points of … (lix) to (lxxxiii) other than (lxxvii) and (lxxxi), each with its item." (lxxv) and its
Task 0 fact taken by site 6.)* *(Former wording, kept: "The rest of part 2, for later sites or files: the audit-list point
of (xliii), (xlv) and (xlvi); (lxxv)'s Task 0 fact with Part C; …" The audit-list point taken by site 5.)* *(Former wording, kept: "Part B's
other wordings ((lxxxi)'s line wording); … the weak points of (l), (li), (lii), (lvi), (lvii), (lviii) and (lix) to
(lxxxiii), each with its item." (lxxxi) taken by site 4.)* *(Former wording, kept: "Part B's other wordings ((liv)'s line wording, (lxxvii)'s §10 line wording,
(lxxxi)'s line wording); … the weak points of (l), (li), (lii), (liv), (lvi), (lvii), (lviii) and (lix) to (lxxxiii),
each with its item." (liv) taken by site 2.)* *(Former wording, kept: "Part B's other wordings ((lxxvii)'s §10 line
wording, (lxxxi)'s line wording)". (lxxvii) taken by site 3.)*

*Provenance: Cowork, 2026-11-11 (Stockholm), the sitting booted on entry 731. The user's words: the opening instruction;
"Shortened".* *Site 2 added by the sitting booted on entry 732; the user's words: the opening instruction; "shortened".
Site 1 was ruled as Ruling 3 of the part 2 ruling record.* *Site 3 added by the sitting booted on entry 733; the user's
words: the opening instruction; "shortened". Site 2 was ruled as Ruling 4 of the part 2 ruling record.* *Site 4 added
by the sitting booted on entry 734; the user's words: the opening instruction; "shortened". Site 3 was ruled as Ruling 5
of the part 2 ruling record.* *Site 5 added by the sitting booted on entry 735; the user's words: the opening
instruction; "shortened". Site 4 was ruled as Ruling 6 of the part 2 ruling record.* *Site 6 added by the sitting
booted on entry 736; the user's words: the opening instruction; "Shortened". Site 5 was ruled as Ruling 7 of the part 2
ruling record.* *Site 7 added by the sitting booted on entry 737; the user's words: the opening instruction; "Shortened".
Site 6 was ruled as Ruling 8 of the part 2 ruling record.* *Site 8 added by the sitting booted on entry 738; the user's
words: the opening instruction; "Shortened". Site 7 was ruled as Ruling 9 of the part 2 ruling record.* *Site 9 added
by the sitting booted on entry 739; the user's words: the opening instruction; "Shortened". Site 8 was ruled as Ruling
10 of the part 2 ruling record.* *Site 10 added by the sitting booted on entry 740; the user's words: the opening
instruction; "shortened". Site 9 was ruled as Ruling 11 of the part 2 ruling record.* *Site 11 added by the sitting
booted on entry 741; the user's words: the opening instruction; "shortened". Site 10 was ruled as Ruling 12 of the
part 2 ruling record.* *Site 12 added by the sitting booted on entry 742; the user's words: the opening instruction;
"shortened". Site 11 was ruled as Ruling 13 of the part 2 ruling record.* *Site 13 added by the sitting booted on
entry 743; the user's words: the opening instruction; "shortened". Site 12 was ruled as Ruling 14 of the part 2 ruling
record.* *Site 14 added by the sitting booted on entry 744, the first group site (group 1, item (lxv)); the user's words:
the opening instruction; "shortened". Site 13 was ruled as Ruling 15 of the part 2 ruling record.* *Site 14's item (lxvi)
added by the sitting booted on entry 745; the user's words: the opening instruction; "shortened". Item (lxv) was ruled
as Ruling 16 of the part 2 ruling record.* *Site 14's item (lxvii) added by the sitting booted on entry 746; the user's
words: the opening instruction; "shortened". Item (lxvi) was ruled as Ruling 17 of the part 2 ruling record.* *Site
14's item (lxxix) added by the sitting booted on entry 747; the user's words: the opening instruction; "shortened". Item
(lxvii) was ruled as Ruling 18 of the part 2 ruling record.* *Site 14's item (lxxxii) added by the sitting booted on
entry 748; the user's words: the opening instruction; "shortened". Item (lxxix) was ruled as Ruling 19 of the part 2
ruling record; with (lxxxii), group 1 is complete.* *Site 15 added by the sitting booted on entry 749, the second
group site (group 2, item (lxi)); the user's words: the opening instruction; "shortened". Item (lxxxii) was ruled as
Ruling 20 of the part 2 ruling record.* *Site 15's item (lxii) added by the sitting booted on entry 750; the user's
words: the opening instruction; "shortened". Item (lxi) was ruled as Ruling 21 of the part 2 ruling record.* *Site
15's item (lxix) added by the sitting booted on entry 751; the user's words: the opening instruction; "shortened". Item
(lxii) was ruled as Ruling 22 of the part 2 ruling record.* *Site 15's item (lxxii) added by the sitting booted on
entry 752; the user's words: the opening instruction; "shortened". Item (lxix) was ruled as Ruling 23 of the part 2
ruling record.* *Site 15's item (lxxiv) added by the sitting booted on entry 753; the user's words: the opening
instruction; "shortened". Item (lxxii) was ruled as Ruling 24 of the part 2 ruling record; with (lxxiv), group 2 is
complete.* *Site 16 added by the sitting booted on entry 754, the third group site (group 3, item (lix)); the user's
words: the opening instruction; "shortened". Item (lxxiv) was ruled as Ruling 25 of the part 2 ruling record.* *Site
16's item (lx) added by the sitting booted on entry 755; the user's words: the opening instruction; "shortened". Item
(lix) was ruled as Ruling 26 of the part 2 ruling record; with (lx), group 3 is complete.* *Site 17 added by the
sitting booted on entry 756, the fourth group site (group 4, item (lxx)); the user's words: the opening instruction;
"shortened". Item (lx) was ruled as Ruling 27 of the part 2 ruling record.* *Site 17's item (lxxi) added by the
sitting booted on entry 757; the user's words: the opening instruction; "shortened". Item (lxx) was ruled as Ruling 28
of the part 2 ruling record; with (lxxi), group 4 is complete.* *Site 18 added by the sitting booted on entry 758, the
fifth group site (group 5, item (lxiv)); the user's words: the opening instruction; "shortened". Item (lxxi) was ruled
as Ruling 29 of the part 2 ruling record.* *Site 18's item (lxviii) added by the sitting booted on entry 759; the
user's words: the opening instruction; "shortened". Item (lxiv) was ruled as Ruling 30 of the part 2 ruling record;
with (lxviii), group 5 is complete.* *Site 19 added by the sitting booted on entry 760, the sixth group site (group 6,
item (lxiii)); the user's words: the opening instruction; "shortened". Item (lxviii) was ruled as Ruling 31 of the part
2 ruling record.* *Site 19's item (lxxxiii) added by the sitting booted on entry 761; the user's words: the opening
instruction; "shortencontinueed" (read as "shortened" and "continue"). Item (lxiii) was ruled as Ruling 32 of the part 2
ruling record; with (lxxxiii), group 6 is complete.* *Site 20 added by the sitting booted on entry 762, item (lxxiii) on
its own; the user's words: the opening instruction; "Shortened". Item (lxxxiii) was ruled as Ruling 33 of the part 2
ruling record.* *Site 21 added by the sitting booted on entry 763, item (lxxvi) on its own; the user's words: the
opening instruction; "Shortened". Item (lxxiii) was ruled as Ruling 34 of the part 2 ruling record.* *Site 22 added by
the sitting booted on entry 764, item (lxxviii) on its own; the user's words: the opening instruction; "Shortened". Item
(lxxvi) was ruled as Ruling 35 of the part 2 ruling record.* *Site 23 added by the sitting booted on entry 765, item
(lxxx) on its own; the user's words: the opening instruction; "Shortened". Item (lxxviii) was ruled as Ruling 36 of the
part 2 ruling record.*

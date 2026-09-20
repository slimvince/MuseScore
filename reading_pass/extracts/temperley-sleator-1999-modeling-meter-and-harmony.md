# EXTRACT — Temperley & Sleator 1999, "Modeling Meter and Harmony: A Preference-Rule Approach" — Task B candidacy row 7, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All eighteen printed pages (pp. 10–27) were read AT THE OBJECT: the held PDF staged
> through the bridge and read with the file tools as page images. **No relay, no web-fetch read.**
> Every quotation carries its printed page.
>
> **Why this paper.** Row 7 of `reading_pass/candidacy_upgrades.md`, ADMITTED there because it
> *"decides meter and harmony together by preference rules — a rival shape for the L1/L2 division, and
> for how metric strength enters."* It is the second member of the L1 slice that **Ruling 10** made the
> phase's first needed reading.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**
>
> **★ CORRECTED 2026-09-20, under the standing rule of handoff entry 198 §7 as narrowed by entry 200 §1
> item 2**: where the second independent extraction's cross-check found this file departing from the
> page and no value, finding or verdict moves, the departure is corrected at its site with the former
> wording preserved (#12). Eight departures at six sites, each site marked "★ CORRECTED 2026-09-20" and
> each departure resolved at the page images; the ground is the second extract's §9.3
> (`reading_pass/extracts_second_pass/temperley-sleator-1999-modeling-meter-and-harmony.md`). Two further
> places, inside or beside a finding or a verdict, were **not** corrected and stand with the user (that
> extract's §9.4).
> *(★ The sentence above was made stale the same day: the user ruled alternative A for both places — his
> words, "I agree with A for both" — and both are now corrected at their sites, finding (2) and the
> "Adapt — the line of fifths" verdict, with the former wording kept (#12).)*

## Identity

David Temperley & Daniel Sleator, "Modeling Meter and Harmony: A Preference-Rule Approach", *Computer
Music Journal* **23:1**, pp. 10–27, Spring 1999. © 1999 Massachusetts Institute of Technology.
Temperley — School of Music, Ohio State University; Sleator — School of Computer Science,
Carnegie-Mellon University.

**File:** `docs/research_papers/temperley_sleator_1999_cmj_meter_harmony_preference_rules.pdf`.

## Claims, labeled

### What the system is, and the shape of its division of labour

**[FACT, p. 10]** One program producing two structures at once: *"a representation showing a metrical
structure (consisting of several levels of beats) and a harmonic structure (consisting of a
partitioning of the piece into segments, each labeled with a root). (There are important reasons for
combining the metrical and harmonic systems into a single program, which we will explain.)"*

**[FACT, p. 10]** The method is a **preference-rule system**: *"Preference rules are criteria for
selecting an analysis of a piece out of many possible ones. The preferred analysis is the one which,
on balance, best satisfies the rules."* Contrasted by the authors with *procedural* systems, whose
output cannot be described as satisfying a stated criterion.

**★ [FACT, p. 11] THE INPUT CONTRACT, AND IT IS THE OPPOSITE OF OURS.** *"The input we assume is a
'note list,' giving the pitch (in integer notation, middle C = 60) and the on-time and off-time (in
milliseconds) of a series of notes. … The program requires no information beyond this: in particular,
it does not require other information commonly available in scores, such as bar lines, key signatures,
rhythmic notation, and the spellings of pitches."*

### The metrical half

**[FACT, p. 12]** Three metrical preference rules, the authors' own wording: the **event rule** —
*"prefer a structure that aligns beats with event onsets"*; the **length rule** — *"prefer a structure
that aligns strong beats with onsets of longer events"*; and (p. 14) the **regularity rule** —
*"prefer beats at each level to be maximally evenly spaced."*

**[FACT, p. 13]** "Length" is not notated duration: the authors define **registral inter-onset
interval** — the interval to the next event within nine semitones — and take an event's length as
*"the maximum of its duration and its registral IOI."*

**★ [FACT, p. 14] Quantization and meter-finding are ONE process, not two.** *"an important recent
realization of music artificial intelligence has been that quantization and meter finding are really
part of the same process."* The input is quantized to 35-msec **pips**, a value *"simply found to be
optimal through trial and error"*; beats may fall only at pip starts.

**[FACT, pp. 13–15]** Five metrical levels prove sufficient *"for the great majority of pieces"* (p. 15);
the tactus is level 2, with two levels above and two below (p. 15). The regularity requirement is a
preference, not a well-formedness constraint (p. 14), so the system tracks tempo change: *"we cannot
simply infer the metrical structure at the beginning of a piece and extrapolate it metronomically
through the rest of the piece"* (p. 13).
*(★ CORRECTED 2026-09-20, at the page. FORMER WORDING, PRESERVED (#12): "**[FACT, p. 15]** Five metrical
levels prove sufficient; the tactus is level 2, with two levels above and two below. The regularity
requirement is a preference, not a well-formedness constraint, so the system tracks tempo change:" —
two defects: the page's qualifier "for the great majority of pieces" was dropped, and the quotation
stands on p. 13 and the preference sentence on p. 14, not p. 15.)*

### The harmonic half

**[FACT, p. 15]** The output is **chord spans** labelled with roots **in absolute terms**: *"whereas a
Roman-numeral analysis represents each root relative to the current key, the current program simply
labels roots in absolute terms."* No key, no mode, no Roman numeral.

**[FACT, p. 16]** Four harmonic preference rules in the authors' wording: the **compatibility rule** —
*"prefer roots that result in certain pitch-root relationships"*, preferred in the order 1, 5, 3, ♭3,
♭7, ♭5, ♭9, ornamental; the **ornamental dissonance rule** — *"in labeling events as ornamental, prefer
events that are (1) closely followed by another event a half-step or whole-step away in pitch, and (2)
metrically weak"* *(★ CORRECTED 2026-09-20, at the page. FORMER WORDING, PRESERVED (#12): "a half-step
or whole-step away, and (2)" — the words "in pitch" were dropped from inside the quotation with no
ellipsis.)*; the **harmonic variance rule** — *"prefer roots such that roots of nearby chord spans
are close together on the line of fifths"*; and (p. 17) the **pitch-variance rule** — *"prefer spellings
for pitch events such that nearby events are close together on the line of fifths."*

**[FACT, p. 16]** Pitches are represented as **tonal pitch classes** on an infinite **line of fifths**,
not as the twelve neutral pitch classes: *"It is our view that these spelling distinctions are an
important aspect of tonal harmony, and must be represented."* Spelling is therefore **inferred by this
system**, and harmony feeds back into it: *"harmonic considerations may force a pitch spelling that
would be less preferred given the pitch-variance rule alone. In this way, harmonic considerations
'feed back' to influence pitch spelling"* (p. 17).

**★ [FACT, p. 17] THE STRONG-BEAT RULE, AND IT IS THE PAPER'S OWN REASON FOR ONE PROGRAM.**
*"**Strong-beat rule**—prefer to start chord spans on strong beats"*, immediately followed by: *"This
important rule explains the motivation for incorporating the harmonic and metrical programs into a
single program. Since harmonic analysis requires metrical information, it is useful to be able to use
the output of the metrical program as input to the harmonic program. There is a problem here, however,
as metrical analysis sometimes requires harmonic information."*

**★ [FACT, p. 17] Chord-span boundaries are restricted to a metrical grid.** *"we divide the piece into
segments based on the lowest level of the metrical structure (usually on the order of 100–300 msec),
and stipulate that chord-span boundaries can only occur at these segment boundaries."* The root space
is bounded arbitrarily: *"we arbitrarily limit it to a range of 48 roots on the line of fifths."*

### The search

**[FACT, pp. 18–19]** Dynamic programming over a table whose columns are segments and whose rows are
candidate roots; the best-so-far analysis ending in each root is carried forward. The authors name the
consequence and treat it as a virtue: *"In this way, the system naturally handles the 'garden-path'
effect: the phenomenon of revising one's initial interpretation of a segment based on what follows."*

**★ [FACT, p. 19] The exact table is intractable and is PRUNED.** *"To incorporate the harmonic variance
rule and the pitch-variance rule … we end up with a four-dimensional table … In practice, the computation
described above is intractable, because the four-dimensional table gets too large. We handle this by
pruning the table for a given segment immediately after the table for that segment is constructed. We
simply keep only those elements that are within some constant of the highest score in the table. We have
found a value for this constant that maintains a reasonable speed for the system without compromising
accuracy."* **The claim that accuracy is not compromised is stated, not measured** — see the next
section.

### ★ The circularity — the [FACT] the framework's L0 section cites, verified at the object

**[FACT, p. 25]** *"Making use of the harmonic analysis is another approach to improving the performance
of the metrical program on the higher levels. … The idea, then, is to let the harmonic analysis influence
the metrical analysis by favoring strong beats at changes of harmony. This presents a serious
chicken-and-egg problem, however, since meter is crucial as input to harmony. One solution would be to
compute everything at once, optimizing over both the metrical and harmonic rules, but we have not yet
found an efficient way of doing this. Another solution, which we are currently exploring, is to first
run the piece through the harmonic program, generating a provisional harmonic analysis, then run the
output of that through the meter program, which is now modified to prefer strong beats at points of
harmonic change, and finally run this output through the harmonic program again to generate the final
harmonic analysis."*
*(★ CORRECTED 2026-09-20, at the page. FORMER EMPHASIS, PRESERVED (#12): the two sentences from "This
presents a serious chicken-and-egg problem" through "an efficient way of doing this." were set in bold
inside the quotation; the page prints them in roman, and the emphasis was this extract's, unmarked.)*

## Measured results, as the paper states them

**★ THERE ARE NONE. This is the single most consequential fact in the paper for our purposes, and it is
stated as an absence rather than inferred.** The paper reports **no corpus, no metric and no accuracy
value anywhere in its eighteen pages.** Its evidence is four worked examples discussed in prose: Bach's
Cello Suite No. 3 Courante (Figures 6–7) and Beethoven's Op. 13 II (Figures 8–9), each with an output
listing; Schubert's *Moment Musical* No. 6 (Figure 10), with the program's analysis shown as chord symbols
on the score; and Schumann's Op. 15 No. 2 (Figure 11), shown as the score alone.
*(★ CORRECTED 2026-09-20, at the page. FORMER WORDING, PRESERVED (#12): "Its evidence is four worked
examples shown as output listings and discussed in prose: Bach's Cello Suite No. 3 Courante (Figures
6–7), Beethoven's Op. 13 II (Figures 8–9), Schubert's Moment Musical No. 6 (Figure 10) and Schumann's Op.
15 No. 2 (Figure 11)." — only two of the four are output listings (p. 22: for the Schubert, "rather than
showing the output, we simply show the program's analysis as chord symbols on the score").)* The scope of
testing is given only as *"We have tested the program on a number of pieces and sections of pieces …
Most are pieces from the common-practice (Bach to Brahms) era, mainly piano pieces; there are also a
number of unaccompanied melodies"* (p. 19).

**The parameters are hand-set.** [FACT, p. 20] *"Both the metrical and harmonic programs involve a
number of parameters. The weight of each preference rule relative to the others must be specified. Many
rules also involve internal parameters … We have simply adjusted these parameters on a trial-and-error
basis. After many tests and adjustments, we have found a set of values that seems to produce generally
good results."*

**The authors' own catalogue of failures, from the worked examples** [FACT, pp. 22–25]: no knowledge of
**pedals**, so the chord over a pedal or bass in measures 7 and 15 of the Schubert is not read as such —
measure 7 analyzed *"reasonably, as an E♭ chord with several appoggiaturas"*, measure 15 *"bizarrely
labeled as a B♭ chord"* (p. 24); the German sixth in measures 16–17 *"incorrectly labeled as an F♭
dominant seventh"*, with its D misspelled E♭♭, and no knowledge of **voice leading**, which the page ties
to that misspelling and which *"results in a fair number of spelling mistakes"* (p. 24); **no
anticipations or escape tones**;
*(★ CORRECTED 2026-09-20, at the page. FORMER WORDING, PRESERVED (#12): "no knowledge of **pedals**, so a
chord over a pedal is misread (measures 7 and 15 of the Schubert); no knowledge of **voice leading**,
which *"results in a fair number of spelling mistakes"* and misreads a German sixth as a dominant
seventh;" — two defects: the page calls measure 7's reading reasonable, not misread; and it states the
German sixth's mislabeling as an error of its own, tying voice leading to the D/E♭♭ spelling that
follows, not to the dominant-seventh label.)* upper metrical levels are weak — *"The
performance on the upper levels is weaker, especially on level 4. Frequently the program correctly
identifies level 4 as duple, which it usually is, but chooses the incorrect phase"*; and the output
*"indicates only the roots of chords, without further information such as mode (major or minor),
extension (triad or seventh), and inversion."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A note list of pitch, on-time and off-time in milliseconds, and
**nothing else** — explicitly not bar lines, key signature, rhythmic notation or spelling (p. 11). It
accepts unquantized live-performance input and handles tempo fluctuation by design (pp. 14, 22).

**What it HANDS downstream.** Three things: a metrical structure of five beat levels; a partition into
chord spans each labelled with an absolute root; and a tonal-pitch-class spelling for every pitch event.
It hands on **no key, no mode, no chord quality, no extension, no inversion, no Roman numeral, no
cadence and no phrase grouping.**

**Its own STATED SCOPE and limits.** Western tonal music, particularly common-practice art music (p. 10).
Grouping structure is named as the missing piece that would fix the upper metrical levels, and the authors
report their own attempt failed: *"getting a computer to recognize grouping boundaries proves to be a very
difficult problem, and our preliminary efforts have been unsuccessful"* (p. 25).
*(★ CORRECTED 2026-09-20, at the page. FORMER WORDING, PRESERVED (#12): "getting a computer to determine
grouping boundaries" — the page prints "recognize".)* The meter-harmony
circularity is unresolved in the joint form (p. 25, quoted above). No evaluation is claimed.

## What an L1 or L2 detail specification could adopt, adapt, or must argue against

- **Must argue against — the metrical grid as the boundary set.** This system's chord-span boundaries can
  fall only on lowest-level metrical beats, 100–300 msec apart. That is DP-C's *before*-a-grid rival in its
  metrical form, and the L1 charter's ground against it — that a window not respecting harmonic or metrical
  boundaries counts evidence belonging to the next harmony as evidence for the current one — applies to it
  directly. **Our change points are onsets and releases; theirs are metrical pips.**
- **Must argue against — the division itself.** This is the cleanest published statement that meter and
  harmony are mutually dependent, and its authors could not optimise them jointly. Our L0 removes the
  dependency by *giving* meter rather than inferring it. The rival is not that we should infer meter; the
  rival is the claim that a system which does not must still carry the dependency somewhere.
- **Adapt — the line of fifths as the space for root and spelling proximity.** A spatial model in which
  proximity is computed by a recency-weighted centre of gravity is a live candidate for any term over
  neighbouring spans; the advantage the authors give is that, *"rather than a circular space"*, the line
  of fifths *"permits this easy way of calculating spatial proximity"* (p. 18).
  *(★ CORRECTED 2026-09-20 on the user's ruling of that date (alternative A), at the page. FORMER WORDING,
  PRESERVED (#12): "and it is unbounded rather than circular, which the authors give as its advantage
  (p. 18)." — the page names the easy calculation of proximity as the advantage, not the unboundedness.
  The verdict "Adapt" is unchanged.)*
- **Adapt — the ornamental dissonance rule's two conditions** (closely followed by a step, and metrically
  weak) as a chord-tone-assignment term. Note this is DP-D's territory and this system decides ornamental
  status *inside* the same optimisation as the root, not before it.
- **Note, do not adopt — the prune.** The pruned dynamic-programming table is a published precedent for
  exactly the mechanism **D-098** records as declared and never adopted; the authors' claim that it does
  not compromise accuracy is unmeasured.

## ★ Findings, routed and not applied

**(1) The framework's L0 meter [FACT] VERIFIES at the object, with its wording earned.** §5, L0 carries:
*"Systems that take a piano roll must infer metrical structure, and one such system reports an unsolved
circularity between meter and harmony as a result. [FACT.]"* This is that system and that report. The
authors call it *"a serious chicken-and-egg problem"*, state they *"have not yet found an efficient way"*
of optimising jointly, and offer a three-pass workaround they were *"currently exploring"*. **"Unsolved"
is fair at the page**: what is unsolved is the joint optimisation, and the workaround is offered as an
alternative to it rather than as a solution to it. **No correction is owed.**

**(2) ★ THE RIVAL SHAPE FOR THE L1/L2 DIVISION IS UNEVALUATED, AND THAT IS A FINDING ABOUT THE RIVAL.**
The candidacy derivation admitted this row as *"a rival shape for the L1/L2 division"*. Read whole, the
rival **reports no accuracy value of any kind** — no corpus, no metric, no comparison. Its parameters are
hand-tuned by trial and error until, in the authors' words, they *"found a set of values that seems to
produce generally good results"* (p. 20). *(★ CORRECTED 2026-09-20 on the user's ruling of that date
(alternative A), at the page. FORMER WORDING, PRESERVED (#12): "hand-tuned by trial and error until the
output looked good." — the page does not print "until the output looked good". The finding is
unchanged.)* **A rival with no measured performance cannot
be preferred to a chosen design point on evidence, and cannot falsify one.** This is not a criticism of a
1999 paper; it is the fact that decides what weight the rival carries in a detail specification.
*(Independently corroborated inside our own read set: Pardo & Birmingham 2002, read at the object as row 4,
say of this same system that its authors "do not give any statistical analysis of the performance of their
system when compared to an outside measure" — two primaries agreeing, one of them the rival's own.)*

**(3) A second instance of the fitting pathology already recorded once.** The findings surface records row
19 as *"a concrete instance of what principles #20 and D-096 exist to prevent"* — parameters introduced
until known-correct outputs were reproduced, with no held-out discipline. **This paper is a second instance
of the same shape**, milder in form (trial-and-error weights rather than added parameters) and identical in
kind: no split, no held-out set, no reported metric. **Recorded as a finding, routed to measurement design;
nothing is written to any surface here.**

**(4) One passage that SUPPORTS a chosen L2 clause rather than rivalling it.** The L2 charter forbids
discarding a rival *"before the whole sequence of spans has been scored"*, on the ground that a wrong
reading can be a local optimum. This system's dynamic programming produces exactly that behaviour and its
authors name it — the garden-path effect, an initial reading of a span revised by what follows (p. 19).
**A rival system's own design corroborating a chosen point is worth recording; it is support, not a
falsifier, and nothing is amended.**

**(5) A relevance to R-8, recorded because the gap is already declared.** The authors close by naming
Krumhansl's key-profile model as the well-known proposal for key and stating its weakness: *"it has no
mechanism for handling modulation"* (p. 27). **R-8 records that the tonality-profiles primary is not held
and is unfetchable**; this is a second-hand characterisation and **nothing is carried out of it** beyond
the fact that this remark exists.

**(6) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**CENTRAL.** Its claims carry load against a design point — it is the named rival shape for the L1/L2
division, and finding (2) bears directly on how much weight that rival can carry. **A second independent
extraction is therefore owed** under the original commission's §4 central-source rule. It has not been
performed and is recorded here as owed.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched, and findings (2) and (3) are routed rather
than written anywhere. It opens no code, touches no measurement tool, no corpus, no golden and nothing
under `tools/`. It writes no open-items row and allocates no decisions-register identity.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. Read for this
extract, at the files: both reading-pass commissions whole, `reading_pass/candidacy_upgrades.md` whole,
`FRAMEWORK.md` §5 and §9 whole, and the findings surface's §1, §2 and §3.2–§3.3; the row-4 extract of this
same slice. The paper itself was read at the object as page images, pp. 10–27. No shell command was run on
the repository or on any staged copy of it for content or for listings; the container copy used for writing
this file is declared. Every value above is the paper's own, quoted with its printed page (#17f, D-431).*

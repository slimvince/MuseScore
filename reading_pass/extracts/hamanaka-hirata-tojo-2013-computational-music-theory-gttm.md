# EXTRACT — Hamanaka, Hirata & Tojo 2013, "Computational Music Theory and Its Applications to Expressive Performance and Composition" — population row 19 (the GTTM computational line), CENTRAL, first pass

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (session 3 of the reading pass,
> 2026-08-31).** Written under `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **★ THE GRADE, AND IT IS THE STRONGEST IN THIS PASS.** The user supplied this chapter as a PDF —
> the same route by which row 15's STOP was resolved. **All thirty pages were read AT THE OBJECT**:
> the file staged through the bridge and read with the file tools as page images. **No relay, no
> prompted extraction, no web-fetch bound.** Every quotation below was read from the page. Contrast
> the other central rows of this pass, whose reads are RELAYED and whose read tool was measured
> contradicting itself three times (`reading_pass/population.md` §3b).
>
> **★ THIS ROW WAS BLOCKED AND IS NOW UNBLOCKED.** Row 19's only open copy of the primary the
> population named — Hamanaka, Hirata & Tojo, JNMR 35(4) — is a scan with no text layer, unreadable
> in this environment, and the publisher's copy is paywalled. The chapter read here is **a later and
> fuller account of the same line by the same three authors**; see "What this does and does not
> close" at the foot.

## Identity

Masatoshi Hamanaka, Keiji Hirata & Satoshi Tojo, "Computational Music Theory and Its Applications to
Expressive Performance and Composition", **chapter 8** of A. Kirke & E. R. Miranda (eds.), *Guide to
Computing for Expressive Music Performance*, Springer-Verlag London, **2013**, **pp. 205–234**.
DOI `10.1007/978-1-4471-4123-5_8`.

Affiliations as printed: Hamanaka — Intelligent Interaction Technologies, University of Tsukuba;
Hirata — Faculty of Systems Information Science, Future University Hakodate; Tojo — School of
Information Science, JAIST.

**File as supplied:** `external resarch summary/Computational Music Theory and Its.pdf` —
**not moved** (see the foot of this file).

## Claims, labeled

### What the systems are

**[FACT, p. 206]** Two analysis systems built on GTTM are named: **ATTA** (automatic time-span tree
analyzer) and **FATTA** (fully automatic time-span tree analyzer). *"ATTA and FATTA can generate a
time-span tree as the result of a GTTM analysis."*

**[FACT, p. 209]** GTTM consists of four subtheories — grouping-structure analysis, metrical-structure
analysis, time-span reduction, and prolongational reduction — and *"attempts to simulate the listening
insights of an 'experienced listener.'"*

**★ [FACT, p. 209] THE PROLONGATIONAL REDUCTION — THE ONE SUBTHEORY THAT IS ABOUT HARMONY — IS NOT
IMPLEMENTED.** The chapter states which three it implements and then, verbatim: *"The prolongational
reduction is still evolving and is currently more controversial; hence we have not implemented it at
present."* And on p. 209 the prolongational reduction is precisely the one described as *"a tree
structure representing subordinate relationships between chords – doing so by explicitly indicating
harmonic retention and change."*
*(A prolongational tree EDITOR exists in the interactive analyzer for manual work, and p. 217 says
"A prolongation tree analyzer is also being developed" — under development, not measured.)*

### Why GTTM as published cannot be run, in the authors' own words

**★ [FACT, p. 210] THREE NAMED DEFECTS, EACH BLOCKING EXECUTION.**
- *Ambiguous concepts defining preference rules* — *"GTTM has rules for selecting structures in
  discovering similar melodies (called parallelism) but does not have a clear definition of
  similarity."*
- *Conflict between preference rules* — *"Conflict between rules often occurs and results – there is
  no strict order for applying the preference rules, causing ambiguities in the analysis."*
- *Lack of algorithmic form* — *"GTTM provides few descriptions of the reasoning and algorithms needed
  to compute analysis results."*

**★ [FACT, pp. 211–212] THE REMEDY IS 46 HAND-ADDED PARAMETERS.** exGTTM externalises and
parameterises the theory: **15 parameters for grouping-structure analysis (Table 8.1), 18 for
metrical-structure analysis (Table 8.2), 13 for time-span reduction (Table 8.3)** — and p. 216 states
the total in terms: *"Because there are 46 parameters, a significant amount of time is needed to
calculate all parameter combinations."*

**★ [FACT, p. 211] THE PARAMETERS ARE CLASSIFIED, AND THE THIRD CLASS IS THE ONE TO NOTICE.**
*Identified* — already in GTTM but with no concrete value. *Implied* — only implied by GTTM, made
explicit (the per-rule priorities). *Unaware* — verbatim: *"we develop parameters that are not
utilized in the original theory, because they lack clear musicological meaning."*

**[FACT, p. 211]** The method of setting them is stated plainly: *"Whenever we find a correct result
that exGTTM cannot generate, we introduce new parameters and give them appropriate values so that
exGTTM can then generate this result. In this way, we repeatedly externalize and introduce new
parameters until we have obtained all of the results that are generally considered correct."*

### The harmonic dependency — the most load-bearing coupling fact in the chapter

**★ [FACT, pp. 214–216] GPR7 IS IMPLEMENTED THROUGH LERDAHL'S TONAL PITCH SPACE, SO THE GROUPING
ANALYSIS CONSUMES A HARMONIC AND TONAL ANALYSIS.** D_GPR7 (eq. 8.1) is built from
`distance(p(i), s(i))` — *"the distance between notes x and y in the tonality of the piece – as
defined using Lerdahl's tonal pitch space"* — and that distance (eq. 8.2) is
**δ(x → y) = i + j + k**, where *"i is region distance, j is chord distance, and k is basic space
difference"*, the region distance being *"the smallest number of steps along the regional circle of
fifths"* and the chord distance *"the smallest number of steps along the chordal circle of fifths
between the roots of C1 and C2 within each region."* p. 223 states it directly: *"The region of the
melody and chord progression are estimated in GPR7 here by applying tonal pitch space methods."*

**★ AND THAT HARMONIC INPUT IS NOT AUTOMATED.** p. 220, verbatim: *"there is no automated analyzer
for tonal pitch space [22] in the interactive GTTM analyzer; however, attempts have been made to
implement the tonal pitch space system, so those results can be used as an input."* p. 217 confirms
the same from the other side: *"Although the GTTM includes rules that require the analysis results of
chord progression, the ATTA utilizes rules based on the results of the tonal pitch space approach."*

**[FACT, p. 220] The theory carries feedback links, and they are why analysis is iterative.**
*"the GTTM contains feedback links from higher- to lower-level structures … Therefore, analysis
involving feedback-linked rules requires a number of analysis processes by trial and error."* Named:
**GPR7** is *"a link from the time-span and prolongational trees to the grouping structure"* and
**MPR9** *"(time-span interaction) is a link from the time-span tree to the metrical structure"*
(p. 221).

**★ THE READING THIS FORCES, STATED PLAINLY.** In the most developed implementation of the time-span
reduction line, **the hierarchy sits DOWNSTREAM of tonality and harmony, not upstream of them** — the
grouping rule that most influences tree quality needs region and chord distances, and those come from
outside the system, by hand. A proposal to use a GTTM-style hierarchy *to help decide* harmony meets a
circularity that this implementation resolves by requiring the harmony first.

### Measured results

**[FACT, p. 228]** The measurement is an **F-measure**, `F = 2PR/(P+R)` (eq. 8.7).

**[FACT, pp. 228, 230] The ground truth.** *"A hundred sections of 8-bar-length, monophonic, classical
music pieces were collected. Musicology experts manually analyzed them utilizing GTTM and using the
manual-edit mode of the interactive GTTM analyzer to assist in developing the grouping structure,
metrical structure, and time-span tree. Three other further experts crosschecked these manually
produced results."* p. 233 records the dataset as *"300 pairs of scores and analysis results"*
published at `http://music.iit.tsukuba.ac.jp/hamanaka/gttm.htm`, and calls it *"the largest database
of analyzed results of GTTM thus far."*

**★ TABLE 8.4 (p. 230), total over the 100 melodies — the numbers row 19 exists to supply:**

| Analyzer | Baseline (default parameters) | Manually configured parameters |
|---|---|---|
| Grouping structure | **0.46** | **0.77** |
| Metrical structure | **0.84** | **0.90** |
| Time-span tree | **0.44** | **0.60** |

Baseline defaults as printed: S^rules = 0.5, T^rules = 0.5, Ws = 0.5, Wr = 0.5, Wl = 0.5, σ = 0.05.

**★ AND THE FULLY AUTOMATIC ARM, p. 230, verbatim:** *"Next, the set of parameters was optimized using
FATTA. The average F-measures became **0.48, 0.89, and 0.49** for grouping, metrical, and time-span
tree structures, respectively – thus still outperforming the baseline performance."*

**★ [FACT, p. 230] WHAT THE MANUAL COLUMN COST.** *"It took an average of approximately 10 min per
piece to find each plausible tuning for the set parameters"*, and *"the parameters were configured
manually because the optimal values of the parameters depend on the piece of music."*

**THE READING OF THOSE THREE ROWS TOGETHER, WHICH IS THE ROW'S WHOLE YIELD.** On monophonic eight-bar
classical excerpts with expert ground truth: **automatic time-span-tree analysis reaches F ≈ 0.49, and
ten minutes of per-piece hand-tuning by the system's own authors raises it to 0.60.** Metrical
structure is the easy axis (0.84 at defaults). Grouping is where tuning buys most (0.46 → 0.77) and
where automation recovers almost none of that gain (0.48).

**[FACT, p. 231, Table 8.5]** Operation time over 100 melodies: interactive GTTM analyzer **575 s**
against the GTTM manual editor **891 s**.

**[FACT, p. 231] The melody-morphing evaluation is a consistency check, not an accuracy measure.**
Ten pairs of melodies; all extrapolative melodies satisfied the ordering condition (eq. 8.8). No
ground-truth comparison.

**[FACT, p. 222] A speed bound stated as a design constraint.** *"To be able to predict notes using
GTTM, FATTA must run in real time. However, several minutes are needed to finish an analysis."* The
remedy is approximation: reusing the previous melody's optimal parameters as the initial set, and an
analysis window of *"the longest group length within 16 measures"*.

### Scope, stated by the authors

**★ [FACT, p. 222] MONOPHONIC ONLY.** *"The FATTA system only deals with monophonic western tonal
music. Thus, the expectation method can predict only monophonic musical structures for western tonal
music as well."* Reinforced p. 227: *"FATTA [8] can generate a time-span tree from the score
automatically but can only deal with monophonic input."*

**[FACT, p. 209] Grouping and metrical analysis are described over homophony** — *"Grouping-structure
analysis hierarchically divides a series of notes in a homophony into phrases or motives"* — while the
implemented and measured pipeline is monophonic per p. 222.

**[FACT, p. 222] The stability level cannot start early.** *"The level of stability can only begin to
be calculated after the third note because GTTM analysis requires at least four notes."*

### Theory and conjecture

**[THEORY]** GTTM itself (Lerdahl & Jackendoff 1983, ref. 9) and Tonal Pitch Space (Lerdahl 2001,
ref. 22) are adopted published theory, not established here.

**[CONJECTURE, p. 220]** That history recording *"can be used to improve automated analyses"* and may
yield *"an analysis knowledge base"* — hoped for, not measured.

**[CONJECTURE, p. 233]** Further systems for harmonizing, voicing and ad-lib using time-span trees —
planned, not built.

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** a **MusicXML** score (p. 215 fig. 8.6 shows MusicXML in), **monophonic** for the
automatic arm, at least four notes; and — load-bearing — **a tonal-pitch-space analysis supplying
region and chord information, which the system does not compute** (p. 220). For the expectation-piano
application the MIDI stream is quantized by an *"adaptive quantization method"* (ref. 26) before
MusicXML is built (p. 223).

**HANDS downstream:** grouping structure, metrical structure and a **time-span tree**, as XML —
p. 217: *"An XML format is used for all the input and output data structures in the interactive GTTM
analyzer."* Fig. 8.6 names GroupingXML, MetricalXML, Time-spanXML. **No chords, no keys, no Roman
numerals, no harmonic labels of any kind leave this system**, the one harmony-bearing subtheory being
unimplemented. **No rivals and no confidence are published** — the analyzer commits one structure, and
where a user edit breaks well-formedness the process editor offers a small candidate menu (pp. 220–221)
to a human, not to a consumer.

**STATED SCOPE:** Western tonal music, monophonic for the automatic arm, eight-bar classical excerpts
in the evaluation; three of GTTM's four subtheories; parameters that must be tuned per piece for the
better numbers.

## Bearing on the framework — flagged, not decided (verdicts belong to Task 4)

**Read against `FRAMEWORK.md` §9 (DP-O) and §11 (R-7), both read at the file this session.**

**★ R-7's THIRD NAMED UNREAD ALTERNATIVE IS NOW READ.** R-7 names three: *"a tonality estimated at
every window size at once"* (row 17, Sapp — read), *"a time-span reduction tree"* (**this row**), and
*"tonality in a transform space rather than as a discrete label"* (row 18, Wavescapes — read).
**With this chapter, all three are read at a primary.** Whether that discharges R-7 is Task 4's; what
is established is that the reading gap R-7 names is closed.

**DP-O — this row supplies NEITHER support NOR a falsifier, and the reason is sharper than "no
measurement".** DP-O asks whether the framework commits to *a hierarchical reading of harmony*, and
names its falsifier as *a tree model beating a matched-capacity sequence model on this repertoire's
ground truth*. This chapter:

1. **does not model harmony hierarchically at all** — the prolongational reduction, the subtheory that
   *"explicitly indicat[es] harmonic retention and change"*, **is the one it did not implement** (p. 209);
2. **is monophonic**, where this project's repertoire is four-voice chorales;
3. **reports no comparison against any sequence model**, matched-capacity or otherwise;
4. and its trees are **reductions of a melody**, graded against expert GTTM annotations — a different
   object and a different ground truth from DP-O's.

**So DP-O stays open exactly as it was, and this row cannot move it.** *NOT claimed:* that no GTTM-line
paper could bear on DP-O; the prolongational analyzer was *"being developed"* in 2013 and later work in
the line (σGTTM, deepGTTM) is unread here.

**★ WHAT THE ROW DOES CONTRIBUTE, AND IT IS NOT NOTHING — two facts about the shape of the problem.**

- **The dependency direction.** The best-developed time-span-reduction implementation puts its
  hierarchy **downstream of tonality and harmony**, needs region and chord distances to run its most
  consequential grouping rule, and **does not compute them**. Any future proposal that hierarchy should
  inform the tonal reading meets this as evidence about the direction the one working implementation
  had to take.
- **The cost of executing a hierarchical theory.** A celebrated theory required **46 parameters** —
  a third of them admitted to *"lack clear musicological meaning"* — introduced by iterating against
  results already considered correct, and still reaches **F ≈ 0.49 automatically** on monophonic
  eight-bar excerpts. **That is a measured statement about tractability**, and it is the same shape as
  HarmTrace's parse-space finding (row 5) from a different direction: a rich hierarchical formalism
  becomes runnable by having something taken out of it or bolted onto it.

**L3 grouping (the framework's read-off facts) — one item worth routing.** The metrical-structure
analyzer scores **0.84 at default parameters**, against grouping's 0.46. Metrical structure is, on this
evidence, much the more mechanically recoverable of the two. Read beside V5's finding that removing
metrical-accent features costs about six points of F-measure in a segmental analyser, it is
consistent — the metrical layer is both recoverable and useful — but **these are different corpora,
different objects and different metrics, and no arithmetic joins them.**

**NO FALSIFIER CANDIDATE against any chosen design point.** Every point this row touches — DP-O — is
underived and open, so nothing here is a STOP under the commission's §6.

## Bibliographic by-catch, routed here and written into no register

**The chapter's own reference [6] is the paper row 19 was flagged on**, and it disagrees with our
records twice. As printed on p. 234: *"Hamanaka M, Hirata K, Tojo S (2007) Implementing 'a generating
theory of tonal music'. J New Music Res (JNMR) 35(4):249–277."*

- **Year: the chapter says 2007**; `reading_pass/additions.md` and the population say **2006**.
- **Title: the chapter prints "a generating theory of tonal music"** — almost certainly its own
  misprint for *generative*, Lerdahl & Jackendoff's title being *A Generative Theory of Tonal Music*
  (the chapter's own reference [9] prints it correctly). **Our records have the title right.**
- **Page range 249–277 is new to our records** and is carried here.

*This joins the four citation findings already recorded by this pass. All belong to the bibliography
reconciliation the commission's Task 2 defers to its own act; nothing is amended here.*

**Also noted for a later reader:** the chapter names ATTA's own primaries — ref. 7, ISMIR 2005
pp. 358–365 (*"ATTA: automatic time-span tree analyzer based on extended GTTM"*), and ref. 8, ICMC
2007 vol. 1 pp. 153–156 (*"FATTA: full automatic time-span tree analyzer"*). **Neither is read**; both
are named here so a successor need not rediscover them.

## What this does and does not close

**CLOSES:** the reading of row 19's subject at a primary of the line, **at the object, whole**, by the
same three authors, later and fuller than the flagged 2006/2007 JNMR paper — which is exactly the shape
of row 15's resolution, and by the same route (the user supplied the file).

**DOES NOT CLOSE:** the specific JNMR paper stays unread, and **nothing is carried out of it**. Whether
row 19's state flips to read on this chapter, or the JNMR paper is still owed, is a small call left to
the user; the honest position is that the line's implementation account is now held at the strongest
grade this environment offers.

**A note on the second-pass obligation.** Row 19 is marked CENTRAL, which makes a second independent
extraction owed. **This read is AT THE OBJECT**, a materially stronger footing than the doubled relayed
reads the other central rows carry, and the double-pass exists to catch relay error. Whether that
substitutes for a second pass is not decided here — it is stated so the next session does not assume
either way.

*Provenance: session 3 of the reading pass, 2026-08-31. Read at the object, thirty pages, from
`external resarch summary/Computational Music Theory and Its.pdf`, staged through the bridge.
`FRAMEWORK.md` §9 and §11 read at the file for the bearing section. No specification derived, no
document amended, no code opened, no register row or entry written. **The workbook beside this PDF in
the same folder was not opened.***

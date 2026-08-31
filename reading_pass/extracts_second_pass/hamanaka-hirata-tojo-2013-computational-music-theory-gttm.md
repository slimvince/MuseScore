# EXTRACT (SECOND PASS) — Hamanaka, Hirata & Tojo 2013, "Computational Music Theory and Its Applications to Expressive Performance and Composition" — population row 19, CENTRAL

> **STATUS: THE INDEPENDENT SECOND EXTRACTION REQUIRED BY THE COMMISSION'S §4 FOR A CENTRAL PAPER,
> PERFORMED 2026-08-31 UNDER THE USER'S RULING OF THE SAME DAY** (Option A on the row-19 residual
> decision surface). Written under `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **Route: the commission's SECOND route** — *"a cleanly separated re-read that does not consult the
> first extract"* — performed by a separated reader given the paper, the population table's routing
> metadata and `FRAMEWORK.md`, and barred from every file carrying the first extract's content. Its
> independence declaration is at the foot of the banner below.
>
> **Grade: AT THE OBJECT, WHOLE, on both sides of this pair** — the only pair in the pass with no
> relay on either side.
>
> **★ READ THE CROSS-CHECK FIRST:** `reading_pass/cross_checks/cross_check_row19.md`. It resolves the
> one disagreement between the two extracts (this one is right), **corrects one arithmetic error in
> §4.5 below** (Table 8.5's Total is lower than THREE of the five itemised rows, not four — the
> conclusion stands, the count does not), and records a paper-internal contradiction that **neither**
> extract caught. **This file is left otherwise unedited, under #12.**

## Banner

**Title as printed:** "Computational Music Theory and Its Applications to Expressive Performance and
Composition" (chapter number **8**, printed in the margin of the title page, p. 205).

**Authors as printed:** Masatoshi Hamanaka, Keiji Hirata, and Satoshi Tojo (p. 205).
Affiliations as printed on p. 205:
- M. Hamanaka (corresponding, ✉): Intelligent Interaction Technologies, University of Tsukuba, 1-1-1 Tenodai, Tsukuba 305-8577, Japan — hamanaka@iit.tsukuba.ac.jp
- K. Hirata: Faculty of Systems Information Science, Future University Hakodate, 116-2 Kamedanakano-cho, Hakodate, Hokkaido 041-8655, Japan — hirata@fun.ac.jp
- S. Tojo: School of Information Science, Japan Advanced Institute of Science and Technology, 1-1 Asahidai, Nomi, Ishikawa, Japan — tojo@jaist.ac.jp

**Book / publisher line as printed (p. 205 footer):** "A. Kirke and E.R. Miranda (eds.), *Guide to
Computing for Expressive Music Performance*, 205 / DOI 10.1007/978-1-4471-4123-5_8, © Springer-Verlag
London 2013".

**Page range:** printed pages 205–234 (30 PDF pages; PDF p.1 = printed p.205, PDF p.30 = printed p.234).

**DOI as shown:** 10.1007/978-1-4471-4123-5_8

**Read grade: AT THE OBJECT, WHOLE — PDF page images.** Every one of the 30 PDF pages was read as a
page image via the `Read` tool `pages` parameter (pages 1–15 and 16–30), including all figures, all
tables, the "Questions" section (p. 233) and the complete 26-entry reference list (p. 234).

**Date:** 2026-08-31.

**Independence statement:** This is an **independent second extraction**, produced without consulting
the first extract or anything summarising it. No file under `reading_pass/extracts/`,
`reading_pass/extracts_second_pass/`, `reading_pass/cross_checks/`, `reading_pass/population.md`,
`reading_pass/additions.md`, `reading_pass/continuation.md`, `cowork_reading_pass_findings_*`,
`cowork_handoff*`, `ratification_surfaces/` or `docs/research_papers/` was opened. The spreadsheet
`external resarch summary/external research.xlsx` was not opened. The only repository file read was
`C:\s\MS\FRAMEWORK.md` (staged copy), and only §5 (layers), §9 (DP-O) and §11 (R-7), as the task
permits. No shell was used on repository content; Bash was used once only to `mkdir /tmp/rp5`.

---

## 1. What the paper is and what it claims to do

This is a **survey/system chapter** describing the authors' own line of work, not a single-experiment
paper. Its abstract (p. 205) states: "This chapter describes a musical analysis system based on a
generative theory of tonal music (GTTM). … Given its ability to formalize musical knowledge, GTTM is
considered here to be the most promising theory among the many that have been proposed because it
captures the aspects of musical phenomena based on the gestalt in the music and follows relatively rigid
rules. This chapter also describes music expectation and melody morphing methods that can use the
analysis results from the music analysis system." (p. 205)

The stated **goal** (p. 206, §8.1 opening): "Our goal is to create a system that will enable a musical
novice to manipulate a piece of music (an ambiguous and subjective medium) according to his/her
intentions." Two requirements are listed: "1. Easily manipulate a piece of music / 2. Capture the user's
intentions" (p. 206).

The chapter names its own prior systems: "Systems for music analysis have been developed called ATTA
[6, 7] and FATTA [8] based on a music theory called generative theory of tonal music (GTTM) [9]. ATTA
and FATTA can generate a time-span tree as the result of a GTTM analysis." (p. 206)

**Organization as the paper states it** (p. 208): §8.2 describes GTTM, "discuss[es] the problems with
implementing GTTM and how to solve them, and then propose[s] our exGTTM as extension of GTTM"; §8.3 an
interactive analyzer combining ATTA (automatic time-span tree analyzer) with a GTTM manual editor; §8.4
the melody expectation method for improvisation assistance; §8.5 melody morphing; §8.6 evaluation; §8.7
conclusion.

The **five main results** the paper claims for itself (p. 232–233, §8.7): *Extended GTTM* (exGTTM);
*Implemented Music Analyzer* (the interactive GTTM analyzer = ATTA + manual editor + process editor);
*Experiments with Human-Verified Analyses*; *Melody Expectation Method*; *Melody Morphing Method*.

Contextual framing on why music theory rather than statistical learning (p. 208): "With the statistical
learning approach, the predictions depend on the characteristics of the data used for learning, for
example, composer, genre, period, country, etc. … However, with the music theory approach, the
predictions do not depend on the characteristics of the data used for learning. It can thus be applied
more successfully to novel melodies."

Why GTTM specifically (p. 208): "Although many music theories have been proposed [18–21], GTTM is the
most suitable for predicting notes in a melody because it can be used to represent multiple musical
elements in a single framework."

---

## 2. Method — what is implemented, what is not, and how

### 2.1 The theory being implemented and the explicit non-implementation

p. 208 (§8.2 opening): "GTTM is a music theory consisting of four subtheories: grouping-structure
analysis, metrical-structure analysis, time-span reduction, and prolongational reduction. It attempts to
simulate the listening insights of an 'experienced listener.'"

**The load-bearing non-implementation, verbatim (p. 209):**
> "Methodologies for implementing three of the four subtheories are presented in this section:
> grouping-structure analysis, metrical-structure analysis, and time-span reduction [6–8, 23, 24]. The
> prolongational reduction is still evolving and is currently more controversial; hence we have not
> implemented it at present."

Prolongational reduction is described (p. 209) as "generat[ing] a tree structure representing subordinate
relationships between chords – doing so by explicitly indicating harmonic retention and change." That
is, **the one GTTM subtheory whose objects are chords is the one not implemented.**

Later qualifications on the same point:
- p. 216: "A prolongation tree analyzer is also being developed."
- p. 230: "The prolongational tree was not included in this, because its analyzer is still under
  development."
- p. 219 (§8.3.1.4) describes a **prolongational tree *editor*** (manual), not an analyzer.

### 2.2 exGTTM — externalization and parameterization

Three implementation problems are named (p. 210, §8.2.1), each in italic heading form:
1. *"Ambiguous Concepts Defining Preference Rules."* — "GTTM has rules for selecting structures in
   discovering similar melodies (called parallelism) but does not have a clear definition of similarity
   for such rules." (p. 210)
2. *"Conflict Between Preference Rules."* — "Conflict between rules often occurs and results – there is
   no strict order for applying the preference rules, causing ambiguities in the analysis." (p. 210)
   Fig. 8.4 (p. 210) illustrates GPR3a ("register") between notes 3 and 4 vs GPR6 ("parallelism")
   between notes 4 and 5.
3. *"Lack of Algorithmic Form."* — "Knowledge represented in the GTTM rules is, in general,
   declarative. … GTTM provides few descriptions of the reasoning and algorithms needed to compute
   analysis results." (p. 210)

The solution (p. 210, §8.2.2): "We have extended the GTTM theory through externalization and
parameterization, devising a machine-executable extension of GTTM: exGTTM. The externalization includes
introducing an algorithm for generating the hierarchical structure of a time-span tree in a mixed
top-down/bottom-up manner. Such an algorithm has not previously been available for GTTM. The
parameterization includes a parameter for controlling the priorities of rules to avoid conflicts among
them, as well as parameters for controlling the shape of the hierarchical time-span tree."

Two kinds of ambiguity are distinguished (p. 210–211): "one involving musical understanding by humans
and the other involving the representation of music theory. The former kind of ambiguity derives from the
ambiguity in music itself. The latter type of ambiguity – a part of GTTM – is due to the lack of a
mechanization concept or of it only being presented in an implicit way. The former (musical) kind of
ambiguity leads us to assume there is more than one correct result. We attempt to avoid the latter
(analysis) type of ambiguity through full externalization and parameterization."

**Parameter counts (p. 211):** "In total, we have introduced 15 parameters for grouping-structure
analysis (Table 8.1), 18 for metrical-structure analysis (Table 8.2), and 13 for time-span reduction
(Table 8.3)." (15+18+13 = 46; the paper independently states "there are 46 parameters" on p. 216.)

Parameters are grouped into three categories (p. 211): **Identified** ("already been identified in GTTM
but is not assigned concrete values"), **Implied** ("only implied by GTTM. We make it explicit"), and
**Unaware** ("parameters that are not utilized in the original theory, because they lack clear
musicological meaning. For example, GPR6 in exGTTM requires extra parameters for controlling the
properties of parallel segments, including the weighting of pitch-oriented matching versus
timing-oriented matching.").

Intermediate variables *D* and *B* (p. 211): "The domain of all the intermediate variables is
constrained to the range 0–1, and to ensure this, such variables are normalized at every computation
stage."

Table 8.1 (p. 212) lists the 15 grouping parameters by name: S_GPRR for R ∈ {2a, 2b, 3a, 3b, 3c, 3d, 4,
5, and 6}; σ (0 ≤ σ ≤ 0.1) "Standard deviation of a Gaussian distribution, the average of which is the
GPR2a boundary"; W_m; W_l; W_s; T_GPR4; T^low.
Table 8.2 (p. 212) lists the 18 metrical parameters: S_MPRR for R ∈ {1, 2, 3, 4, 5a, 5b, 5c, 5d, 5e, and
10}; W_m; W_l; W_s; T_MPRR for R ∈ {4, 5a, 5b, 5c}.
Table 8.3 (p. 212) lists the 13 time-span parameters: S_TSRPRR for R ∈ {1, 2, 3, 4, 5a, 5b, 5c, 5d, 5e,
and 10}; W_m; W_l; W_s.

### 2.3 The hierarchy algorithm

p. 213 (§8.2.2.2): "The problem of analyzing hierarchical structures in the grouping-structure/
metrical-structure analyses and the time-span tree reduction can be regarded as a constraint satisfaction
problem (CSP). This is because the GTTM rule form only represents the properties to be satisfied within
the hierarchical. Neither constraints nor order of the generation hierarchical structures is determined
in advance in GTTM."

Constraints split local/global (p. 213): "The former includes GPR2 (proximity) and TSRPR1 (strong
metrical position). The latter includes GPR5 (symmetry) and MPR1 (parallelism)." The developed
algorithm: "we develop algorithms for generating hierarchical structures for exGTTM so that nodes are
generated either from the bottommost nodes or from the topmost node incrementally and so that each time
the nodes in a layer are calculated, global information is recalculated before moving onto an adjacent
layer." Fig. 8.5 caption (p. 213): "a global constraint is inevitably dynamic".

### 2.4 ATTA → FATTA

p. 214 (§8.2.3): "We have implemented a time-span tree analyzer, called the automatic time-span
analyzer (ATTA), utilizing exGTTM. Although ATTA can automatically acquire a time-span tree, the
parameters are manually controlled – and it takes too much time to find a set of optimal parameters.
Therefore, we have also developed a method for automatically estimating the optimal parameters [8]."

**Two GTTM rules not in ATTA, verbatim (p. 214):**
> "There are two preference rules in GTTM [9] not implemented in ATTA – GPR7 and TSRPR5. These rules
> require that information from later processes, such as time-span/prolongational reductions, be
> utilized in earlier processes"

The rule texts as boxed on p. 214: "GPR7 (time-span and prolongational stability): Prefer a grouping
structure that results in a more stable time-span and/or prolongational reduction." / "TSRPR5 (metrical
stability): When choosing the head of time-span T, prefer a choice that results in a more stable choice
of metrical structure."

FATTA = "the ATTA and a loop for the GPR7 and TSRPR5" (p. 214); Fig. 8.6 (p. 215) is the processing flow
for the "fully automatic time-span tree analyzer (FATTA)", showing MusicXML → GroupingXML → MetricalXML
→ Time-spanXML with a "FATTA Feedback loop" around the "ATTA" box, applying GPR7 and TSRPR5 to compute a
"Level of time-span tree stability".

D_GPR7 (Eq. 8.1, p. 214) is defined as a size²-weighted mean of `distance(p(i), s(i))` over time-span
heads, where "Distance(x, y) indicates the distance between notes x and y in the tonality of the piece –
as defined using Lerdahl's tonal pitch space [22]. This distance is normalized here between 0 and 1. …
When calculating D_GPR7, the square of size (i) is used for the weighting (for empirical reasons)."

The tonal pitch space chord distance (Eq. 8.2, p. 214–216): "δ(x → y) = i + j + k, where i is region
distance, j is chord distance, and k is basic space difference."

D_TSRPR5 (Eq. 8.3, p. 216) is a size²-weighted count over heads where `dot(p(i)) ≥ dot(s(i))`, "where
dot(x) indicates the number of metrical dots for note x."

**Optimization procedure (p. 216, §8.2.3.3), verbatim:**
> "The optimal set of ATTA parameters is obtained by maximizing the average of D_GPR7 (0 ≤ D_GPR7 ≤ 1)
> and D_TSRPR5 (0 ≤ D_TSRPR5 ≤ 1). The parameters and default values are S_rules = 0.5, T_rules = 0.5,
> Ws = 0.5, Wr = 0.5, Wl = 0.5, and σ = 0.05. Because there are 46 parameters, a significant amount of
> time is needed to calculate all parameter combinations."

The stated minimisation algorithm (p. 216): "1. Maximize average of D_GPR7 and D_TSRPR5 through changing
a parameter from its minimum to its maximum value. 2. Repeat (8.1) for all parameters. 3. Iterate (8.1)
and (8.2) as long as the average of D_GPR7 and D_TSRPR5 is higher than that of the previous iteration."
(The cross-references "(8.1)" and "(8.2)" in steps 2 and 3 appear to point at the numbered list items,
not at Eqs. 8.1/8.2 — see §8 below.)

### 2.5 Interactive GTTM analyzer (§8.3)

p. 216: "It consists of an ATTA [6, 7], a GTTM manual editor, and a GTTM process editor. The ATTA is made
up of analyzers for grouping structure, metrical structure, and time-span tree. A prolongation tree
analyzer is also being developed."

Fig. 8.8 (p. 217) shows: ATTA {grouping structure analyzer, metrical structure analyzer, time-span tree
analyzer, prolongational tree analyzer} ↔ GTTM process editor ↔ GTTM manual editor {grouping structure
editor, metrical structure editor, time-span tree editor, prolongational tree editor, Tonal Pitch Space
editor}.

p. 217, on how chord information is obtained: "Although the GTTM includes rules that require the analysis
results of chord progression, the ATTA utilizes rules based on the results of the tonal pitch space
approach."

p. 217: "An XML format is used for all the input and output data structures in the interactive GTTM
analyzer. Each analyzer and editor of the system work independently, but they are integrated through the
XML-based data structure."

Manual editors: grouping-structure editor with four operations "(1) divide this group and create
subgroup, (2) divide this group, (3) delete, and (4) delete descendant" (p. 218); metrical-structure
editor by dragging bars up/down (p. 218); time-span tree editor where "the user moves the head by
dragging another branch" with head types "(1) ordinary, (2) fusion, (3) transformation, and (4) cadential
retention" (p. 219); prolongational tree editor (p. 219); tonal pitch space editor (p. 219) — "A tonal
pitch space editor is included in the interactive GTTM analyzer because it provides quantitative grounds
for the prolongational tree to be hierarchical."

GTTM process editor (p. 220) has three functions: data input, history recording, process control. Data
input: "For example, there is no automated analyzer for tonal pitch space [22] in the interactive GTTM
analyzer; however, attempts have been made to implement the tonal pitch space system, so those results
can be used as an input [25]." Process control repairs "broken" structures against well-formedness rules
MWFR2 (p. 220, Fig. 8.11) and GWFR3 (p. 221, Fig. 8.12), and ranks the top-ten candidates by similarity
to the edit history.

p. 221: "In this section, we omit the details of the implementation of GPR7 and MPR9 due to space
limitations."

### 2.6 Melody expectation (§8.4)

Method (p. 222): "The melody expectation method presented here predicts candidate notes using their
level of stability in a time-span tree defined in FATTA. A single expected, following tone cannot always
be specified; thus, our 'expectation piano' simply suggests multiple candidates from among pitch events
with higher stability."

Real-time extension (p. 222, §8.4.1.1): "To be able to predict notes using GTTM, FATTA must run in real
time. However, several minutes are needed to finish an analysis. Hence, the algorithm needed adjustment
for real-time operation. To speed up the iteration described in Sect. 8.2.2, the set of optimal parameter
values for the previous melody is reused as an initial parameter set. This is an approximation because
the previous melody is one note shorter than the present melody. To further increase speeds, an analysis
window is utilized by ATTA. The size of the window is the longest group length within 16 measures from
the present position. This length is acquired through preprocessing using the grouping-structure analyzer
in ATTA. If there is no grouping boundary within 16 measures from the present position, 16 measures is
used as the window size."

Stability (p. 222, §8.4.1.2): "FATTA is used to evaluate the appropriateness of a candidate melody by
calculating its stability. The average of D_GPR7 and D_TSRPR5 is used as the level of stability. … The
level of stability can only begin to be calculated after the third note because GTTM analysis requires at
least four notes."

Expectation piano hardware (pp. 222–224): MIDI signal quantized with an adaptive quantization method
[26]; MusicXML fed into FATTA; "a 32 × 25 full-color LED matrix" under a semitransparent acrylic lid;
"The 32 lights represent two measures when the resolution is a sixteenth note; 25 is the number of keys
on the keyboard"; "When the level of stability is high, the LED shows yellow; when it is low, it shows
black; and when it is neither, it shows red. There is also a 32 × 20 blue LED matrix that displays the
bar lines for the piano roll." (p. 223) Construction: "The piano is 953 mm long and 710 mm wide … The LED
display is 630 mm long and 390 mm wide. The colors of the LEDs are controlled using MAX6972, which is a
16-output, 12-bit pulse-width-modulation (PWM) LED driver. There is a 5-mm gap between the LEDs and piano
lid… The LED drivers are controlled using the computer via a network cable, which sends the data for the
LED colors through the user datagram protocol." (pp. 223–224)

### 2.7 Melody morphing (§8.5)

Inputs and four constraints (p. 224): "The melody morphing system takes as input an initial melody A and
a target 'nuance' melody B and gives a resulting morphed melody C. The system utilizes the following
constraints (constraints 1 and 2 are for melody C; 3 and 4 are methodological constraints): 1. The
similarity between A and C must be closer than that of A and B, and the similarity between B and C must
be closer than that of A and B. 2. If B is the same as A, C will be the same as A. 3. The features of
melody C depend on parameters that decide the level of influence of melodies A and B. 4. If A and B are
monophonic, then C is monophonic."

Primitive operations (p. 224): "a set of primitive operations are used: the subsumption relation (written
as ⊑), meet (written as ⊓), and join (written as ⊔), as proposed in Hirata [13]." Example relation:
TF ⊑ TE ⊑ TD (Eq. 8.4, p. 224).

Meet/join (p. 225): "The meet operator for two melodies extracts the largest common part or the most
common information from the time-span trees of the two melodies, in a 'top-down' manner… The join
operator joins two time-span trees in a top-down manner as long as the structures of two time-span trees
are consistent."

Octave handling (p. 227): "If octave notes are discriminated (e.g., C4 and C3) are distinguished. If they
are not distinguished, the result is just C, that is, abstracted of the octave information. For the
system here a note and the octave note are regarded as different notes because processing is found to be
more difficult if the octave information is not defined."

Melody division reduction (p. 227, §8.5.4), three steps: "Step 1: Define the Level of Abstraction — A
user sets the parameter value L that determines the level of abstraction of the melody. L ranges from 1
to the number of notes in the difference information of the time-span trees that are included in T_A but
not included in T_A ⊓ T_B. Step 2: Abstraction of Notes in the Difference Information — This step selects
and abstracts a note which has the fewest number of dots in the difference information. The number of
dots can be acquired from the GTTM analysis results [3]. If two or more notes have the fewest dots, the
first one in the list is selected. Step 3: Iteration — Iterate step 2 L times." Subsumption chain Eq. 8.5.

Combining (p. 228, §8.5.5): "The simple join operator is not sufficient for combining T_C and T_D,
because T_C ⊔ T_D is not necessarily monophonic, even if T_C and T_D are monophonies. In other words, the
result of the operation has chords when the time-span structures are overrides and the pitches of the
notes are different. Thus, the result would violate condition 4 in Sect. 8.3. To avoid this problem, a
special operator [n1, n2] is introduced, which outputs note n1 or note n2, as a result of n1 ⊔ n2. Then,
the result of T_C ⊔ T_D is all combinations of monophonic melodies produced by the operator."

Fig. 8.18 (p. 229) shows the divisional reduction for L_A = 1 … 8, i.e. the worked example from the text
on p. 228: "In Fig. 8.17, there are nine notes included in T_A but not included in T_A ⊓ T_B. Therefore,
the value of n is 8, and eight kinds of melodies Cm (m = 1, 2, …, n) can be acquired between T_A and T_A
⊓ T_B (Fig. 8.18)."

ShakeGuitar demonstration (p. 231, §8.6.4): "the ShakeGuitar has been developed as a demonstration system
for the melody morphing method. It works with the iPhone/iTouch… Shaking the iPhone/iTouch with varying
degrees of strength influences the level of guitar-melody difficulty. This smoothly changes in real time
from soft backing to heavy soloing using the melody morphing method."

---

## 3. Stated scope and limits (the authors' own words)

This section collects the authors' own restrictive statements. Verbatim quotes, with pages.

**3.1 A whole subtheory is not implemented — and it is the harmonic one.**
> "Methodologies for implementing three of the four subtheories are presented in this section:
> grouping-structure analysis, metrical-structure analysis, and time-span reduction [6–8, 23, 24]. **The
> prolongational reduction is still evolving and is currently more controversial; hence we have not
> implemented it at present.**" (p. 209)

Reinforced: "A prolongation tree analyzer is also being developed." (p. 216); "The prolongational tree
was not included in this, because its analyzer is still under development." (p. 230).

Prolongational reduction is the subtheory that concerns chords: "The prolongational reduction method
generates a tree structure representing subordinate relationships between chords – doing so by explicitly
indicating harmonic retention and change." (p. 209)

**3.2 Two GTTM preference rules are absent from ATTA.**
> "There are two preference rules in GTTM [9] not implemented in ATTA – GPR7 and TSRPR5." (p. 214)

They are added only in FATTA's feedback loop. Their implementation details are withheld:
> "In this section, we omit the details of the implementation of GPR7 and MPR9 due to space
> limitations." (p. 221)

**3.3 Monophonic only — stated twice, unambiguously.**
> "**The FATTA system only deals with monophonic western tonal music. Thus, the expectation method can
> predict only monophonic musical structures for western tonal music as well.**" (p. 222)

> "Note that from this point on in this chapter, all melodies discussed will be assumed to be monophonic.
> **FATTA [8] can generate a time-span tree from the score automatically but can only deal with monophonic
> input.**" (p. 227)

Also, morphing constraint 4 (p. 224): "If A and B are monophonic, then C is monophonic," and the
admission that join can produce non-monophonic output requiring the special [n1, n2] operator (p. 228).

The evaluation corpus is likewise monophonic: "A hundred sections of 8-bar-length, **monophonic**,
classical music pieces were collected." (p. 228)

**3.4 GTTM's own gaps that the authors could not close, only parameterize.**
> "GTTM uses some imprecisely defined terms that can create ambiguities in the analysis. For example,
> GTTM has rules for selecting structures in discovering similar melodies (called parallelism) but does
> not have a clear definition of similarity for such rules." (p. 210)

> "Conflict between rules often occurs and results – there is no strict order for applying the preference
> rules, causing ambiguities in the analysis." (p. 210)

> "Knowledge represented in the GTTM rules is, in general, declarative. A system is required to perform
> automatic reasoning using the declaratively described knowledge. **GTTM provides few descriptions of the
> reasoning and algorithms needed to compute analysis results.**" (p. 210)

> "**GTTM contains few descriptions of the algorithms needed to compute actual analysis results, in
> particular with the time-span and prolongational trees.**" (p. 220)

**3.5 The parallelism rule has more than one legitimate implementation and they chose one.**
> "For example, grouping preference rule 6 (GPR6) is a rule for parallelism in a grouping structure;
> however, the GTTM does not define the decision criteria for deciding whether two or more segments are
> parallel. **Therefore, multiple implementations of GPR6 are possible, although our system utilizes only
> one.**" (p. 220)

**3.6 Parameters have no musicological ground in one of the three categories.**
> "For the third category (Unaware), we develop **parameters that are not utilized in the original theory,
> because they lack clear musicological meaning.**" (p. 211)

And an internal weighting is admitted to be empirical rather than principled:
> "When calculating D_GPR7, the square of size (i) is used for the weighting (**for empirical reasons**)."
> (p. 214)

**3.7 Parameters are piece-dependent — and hand-tuned in the headline experiment.**
> "**In this test, the parameters were configured manually because the optimal values of the parameters
> depend on the piece of music.** When a user changes the parameters, the hierarchical structures change
> as a result of the new analysis." (p. 230)

> "**It took an average of approximately 10 min per piece to find each plausible tuning for the set
> parameters set (Tables 8.1, 8.2, 8.3).**" (p. 230)

And the reason FATTA exists at all: "Although ATTA can automatically acquire a time-span tree, the
parameters are manually controlled – and it takes too much time to find a set of optimal parameters."
(p. 214); "Because there are 46 parameters, a significant amount of time is needed to calculate all
parameter combinations." (p. 216)

**3.8 The automatic analyzer cannot be relied on to match a human reading.**
> "**The ATTA may not always produce a result which reflects the user's interpretation.** When a user
> desires to adjust the analysis result according to preference, they can use the GTTM manual editor."
> (p. 218)

And on the metrical editor: "Although the metrical-structure analyzer in the ATTA performs fairly well
[24], a user may still desire to perform minor edits on the resulting metrical analyses." (p. 218)

Also: "While editing beat strength, a user may also distort hierarchical metrical structures. In other
words, the results of the metrical-structure editor may sometimes contradict the metrical preference
rules." (p. 219)

**3.9 There is no automated tonality/tonal-pitch-space analyzer in the system.**
> "For example, **there is no automated analyzer for tonal pitch space [22] in the interactive GTTM
> analyzer**; however, attempts have been made to implement the tonal pitch space system, so those results
> can be used as an input [25]." (p. 220)

The Tonal Pitch Space editor is listed only on the manual-editor side of Fig. 8.8 (p. 217).

**3.10 Real-time operation is an admitted approximation.**
> "To be able to predict notes using GTTM, FATTA must run in real time. **However, several minutes are
> needed to finish an analysis.** Hence, the algorithm needed adjustment for real-time operation. … the set
> of optimal parameter values for the previous melody is reused as an initial parameter set. **This is an
> approximation** because the previous melody is one note shorter than the present melody." (p. 222)

**3.11 A minimum-length precondition on analysis.**
> "The level of stability can only begin to be calculated after the third note because **GTTM analysis
> requires at least four notes.**" (p. 222)

**3.12 Comparison to other systems is declined.**
> "**It is difficult to compare the performance of this system with that of previous systems because the
> approaches taken are so different.** The method used here, based on music theory, evaluates the
> appropriateness of the notes from a musical point of view. Hence, the evaluation approach will be to
> quantitatively evaluate each step in the method and then detail an example result." (p. 228)

**3.13 The morphing method's evaluation and final system are declared future work.**
> "The actual final development of an interactive melody generator and **the evaluation of the melody
> morphing method are planned in future work.**" (p. 233)

(Note the tension with §8.6.3's ten-pair test — see §8 below.)

**3.14 Repertoire.** Where stated, "classical music pieces" (p. 228) and "western tonal music" (p. 222).
The named example pieces (Tables 8.4 and 8.5, pp. 230–231) are common-practice European repertoire:
Moments Musicaux, Wiegenlied, Traumerei, An die Freude, Barcarolle, Grande Valse Brillante, Turkish
March, Anitras Tanz, Valse du Petit Chien. **No composer attributions, no editions and no key/metre
information are printed for any of them.** The evaluation excerpts are "8-bar-length" sections (p. 228).

**3.15 Ambiguity in music itself is accepted as irreducible.**
> "The former (musical) kind of ambiguity leads us to assume there is more than one correct result. We
> attempt to avoid the latter (analysis) type of ambiguity through full externalization and
> parameterization." (p. 211)

Note that the ground truth is nevertheless treated as a single "correct" analysis in §8.6.1 (p. 228,
"the availability of a 'correct' analysis"). The paper does not reconcile these.

---

## 4. Measured results

The paper reports **four** evaluation items (§8.6, pp. 228–232). All values below are transcribed
exactly as printed; nothing is rounded, converted or inferred.

### 4.1 Metric definition

Eq. 8.7 (p. 228): **F_measure = 2 × (P × R)/(P + R)**, introduced as: "The performance of the music
analyzer was analyzed using an F-measure given by the weighted harmonic mean of precision and recall (as
utilized in pattern recognition system evaluation)." (p. 228)

**The paper does not define P or R** — it does not state what counts as a true positive for a grouping
boundary, a metrical dot, or a time-span-tree branch. (See §8.)

### 4.2 Ground truth / corpus for the ATTA and FATTA evaluation (§8.6.1)

> "This evaluation required the availability of a 'correct' analysis grouping structure, metrical
> structure, and time-span tree. **A hundred sections of 8-bar-length, monophonic, classical music pieces
> were collected. Musicology experts manually analyzed them utilizing GTTM and using the manual-edit mode
> of the interactive GTTM analyzer to assist in developing the grouping structure, metrical structure, and
> time-span tree. Three other further experts crosschecked these manually produced results.**" (pp.
> 228–230, sentence spans the page break)

Baseline definition (p. 230): "To evaluate the baseline performance of the system, the following default
parameters were used in the analysis: S^rules = 0.5, T^rules = 0.5, Ws = 0.5, Wr = 0.5, Wl = 0.5, and
σ = 0.05."

### 4.3 Table 8.4 — "F-measure of analyzer outperformed the baseline" (p. 230)

Column structure as printed: three analyzer column-groups (Grouping-structure analyzer /
Metrical-structure analyzer / Time-span tree analyzer), each split into "Baseline performance" and
"System with configured parameters".

| Melodies (row label as printed) | Grouping: Baseline | Grouping: Configured | Metrical: Baseline | Metrical: Configured | Time-span: Baseline | Time-span: Configured |
|---|---|---|---|---|---|---|
| 1. Moments Musicaux | 0.18 | 0.56 | 0.95 | 1.00 | 0.71 | 0.84 |
| 2. Wiegenlied | 0.76 | 1.00 | 0.83 | 0.85 | 0.54 | 0.69 |
| 3. Traumerei | 0.60 | 0.87 | 0.76 | 1.00 | 0.50 | 0.63 |
| 4. An die Freude | 0.12 | 0.73 | 0.95 | 1.00 | 0.22 | 0.48 |
| 5. Barcarolle | 0.04 | 0.54 | 0.72 | 0.79 | 0.24 | 0.60 |
| **Total (100 melodies)** | **0.46** | **0.77** | **0.84** | **0.90** | **0.44** | **0.60** |

The table prints two rows of vertical ellipsis dots between row 5 and the Total row, i.e. rows 6–100 are
elided.

**Headline totals, stated in the terms of the table:** over 100 melodies, grouping structure went from
**0.46** (baseline, default parameters) to **0.77** (manually configured parameters); metrical structure
from **0.84** to **0.90**; time-span tree from **0.44** to **0.60**.

Text summary (p. 230): "After configuration, the F-measures of our analyzer outperformed the fully manual
baseline (Table 8.4)."

### 4.4 FATTA (fully automatic parameter optimization), same corpus (p. 230, running text — NOT in a table)

> "Next, the set of parameters was optimized using FATTA. **The average F-measures became 0.48, 0.89, and
> 0.49 for grouping, metrical, and time-span tree structures, respectively – thus still outperforming the
> baseline performance.**" (p. 230)

Mapping, in the paper's own order: grouping **0.48**, metrical **0.89**, time-span tree **0.49**.
These are to be read against the Table 8.4 Total row baselines (0.46 / 0.84 / 0.44) and the
manually-configured totals (0.77 / 0.90 / 0.60). The paper compares them only to the baseline.

### 4.5 Table 8.5 — "Operation time of interactive GTTM analyzer and GTTM manual editor" (p. 231)

Corpus (p. 230, §8.6.2): "The time taken to perform an analysis with the interactive GTTM analyzer was
compared to the GTTM manual editor without an ATTA. For the analysis, **100 pieces from the 300 scores
(with human-validated grouping-structure analysis, metrical structure, and time-span tree) were
utilized.** The prolongational tree was not included in this, because its analyzer is still under
development."

Units as printed: "(in seconds)".

| Melodies (row label as printed) | Interactive GTTM analyzer (in seconds) | GTTM manual editor (in seconds) |
|---|---|---|
| 1. Grande Valse Brillante | 326 | 624 |
| 2. Moments Musicaux | 541 | 791 |
| 3. Turkish March | 724 | 1,026 |
| 4. Anitras Tanz | 621 | 915 |
| 5. Valse du Petit Chien | 876 | 1,246 |
| **Total (100 melodies)** | **575** | **891** |

The table prints one row of vertical ellipsis dots between row 5 and the Total row.

Note on reading the "Total" row: the row is labelled "Total (100 melodies)" but the values 575 and 891
are lower than four of the five itemised rows, so they behave as **averages** per piece, not sums. The
paper does not say which; it only says (p. 231) "that the interactive GTTM analyzer outperformed the GTTM
manual editor without an ATTA (Table 8.5)." **This is the paper's ambiguity, not an inference of mine.**

### 4.6 Melody morphing evaluation (§8.6.3, p. 231)

Criterion, Eq. 8.8 (p. 231): **{R(A,M) < R(A,B) and R(B,M) < R(A,B)}**, introduced as "One method of
evaluating the melody morphing M is to test that any extrapolative melody M is an interpolative melody of
melodies A and B."

Similarity measure, Eq. 8.9 (p. 231): **R_N(X, Y) = |meet(X,Y)| / max(|X|_N, |Y|_N)**, "the R_N(X, Y)
measure in (8.9), defined by Hirata [13], is used. It indicates how much information is lacking from the
two melodies as a result of the meet operation… where |X|_N denotes the number of notes in melody X."

Result, verbatim (p. 231): "**Ten pairs of sample melodies were selected for A and B. It was found that
all the extrapolative melodies M from melodies A and B satisfied expression (8.8).**"

No numeric values are printed for this experiment — only the pass/fail verdict on 10 pairs. No corpus is
named. No composer or source is given for the ten pairs.

### 4.7 ShakeGuitar (§8.6.4, p. 231)

Presented as "a demonstration system for the melody morphing method". **No measurement, no user study,
no numbers.**

### 4.8 Claim about the dataset's standing (p. 233)

> "The experiment results showed that, with preconfigured parameters, the music analyzer outperformed the
> baseline F-measure. **One hundred expert-verified analyses were performed, which is the largest database
> of analyzed results of GTTM thus far.**"

---

## 5. Datasets, tools and URLs the paper publishes

- **Dataset + tool release (p. 233):** "As a contribution to the research of music analysis, **the
  interactive GTTM analyzer and a dataset of 300 pairs of scores and analysis results by musicologists are
  available on the website http://music.iit.tsukuba.ac.jp/hamanaka/gttm.htm**." (URL printed as a live
  link in the text.)
- **Corpus described but not separately released:** the 100 8-bar-length monophonic classical sections
  with expert grouping / metrical / time-span analyses, cross-checked by three further experts (p. 228,
  230). The relation between "300 pairs" (p. 233), "300 scores" (p. 230) and "One hundred expert-verified
  analyses" / "A hundred sections" (pp. 228, 233) is not explained by the paper.
- **Formats (p. 217, Fig. 8.6 p. 215):** MusicXML input; GroupingXML, MetricalXML, Time-spanXML
  intermediate/output. "An XML format is used for all the input and output data structures in the
  interactive GTTM analyzer."
- **Systems named:** ATTA (automatic time-span tree analyzer), FATTA (fully automatic time-span tree
  analyzer), the interactive GTTM analyzer (ATTA + GTTM manual editor + GTTM process editor), the
  expectation piano (Fig. 8.1, p. 207), ShakeGuitar (Fig. 8.19, p. 232).
- **Hardware component named:** MAX6972, "a 16-output, 12-bit pulse-width-modulation (PWM) LED driver"
  (pp. 223–224). Transport: user datagram protocol over network cable (p. 224).
- **Third-party URL in references (p. 234):** ref [1] "Apple – GarageBand (2012).
  http://www.apple.com/ilife/garageband/".
- **No source-code repository, no licence, and no software version number are printed anywhere.**

---

## 6. The paper's own reference list entries for its predecessor systems

Transcribed exactly as the reference list on **p. 234** prints them (numbering, author initials,
punctuation, venue abbreviations and page ranges as printed):

> **4.** Hirata K, Hiraga R (2003) Ha-Hi-Hun plays Chopin's Etude. In: Working notes of IJCAI-03 workshop
> on methods for automatic music performance and their applications in a public rendering contest,
> Acapulco, pp 72–73

> **5.** Hirata K, Matsuda S (2003) Interactive music summarization based on generative theory of tonal
> music. J New Music Res (JNMR) 32(2):165–177

> **6.** Hamanaka M, Hirata K, Tojo T (2007) Implementing "a generating theory of tonal music". J New
> Music Res (JNMR) 35(4):249–277

> **7.** Hamanaka M, Hirata K, Tojo S (2005) ATTA: automatic time-span tree analyzer based on extended
> GTTM. In: Proceedings of the 6th international conference on music information retrieval conference
> (ISMIR2005), London, pp 358–365

> **8.** Hamanaka M, Hirata K, Tojo S (2007) FATTA: full automatic time-span tree analyzer. In:
> Proceedings of the 2007 international computer music conference (ICMC2007), Copenhagen, vol 1, pp
> 153–156

> **9.** Lerdahl F, Jackendoff R (1983) A generative theory of tonal music. MIT Press, Cambridge, MA

> **13.** Hirata K, Aoyagi T (2003) Computational music representation based on the generative theory of
> tonal music and the deductive object-oriented database. Comput Music J 27(3):73–89

> **14.** Hamanaka M, Hirata K, Tojo S (2009) Melody extrapolation in GTTM approach. In:Proceedings of the
> 2009 international computer music conference (ICMC2009), Montreal, pp 89–92

> **15.** Hamanaka M, Hirata K, Tojo S (2008) Melody morphing method based on GTTM. In:Proceedings of the
> 2008 international computer music conference (ICMC2008), Belfast, pp 155–158

> **22.** Lerdahl F (2001) Tonal pitch space. Oxford University Press, New York

> **23.** Hamanaka M, Hirata K, Tojo S (2004) Automatic generation of grouping structure based on the
> GTTM. In: Proceeding of 2004 international computer music conference (ICMC2004), Miami, pp 141–144

> **24.** Hamanaka M, Hirata K, Tojo S (2005) Automatic generation of metrical structure based on the
> GTTM. In: Proceeding of 2005 international computer music conference (ICMC2005), Barcelona, pp 53–56

> **25.** Sakamoto S, Tojo S (2009) Harmony analysis of music in tonal pitch space. Information Processing
> Society of Japan SIG technical report, vol 2009 (in Japanese)

> **26.** Hamanaka M, Goto M, Asoh H, Otsu N (2003) A learning-based quantization: unsupervised estimation
> of the model parameters. In: Proceedings of the 2003 international computer music conference (ICMC2003),
> Singapore, pp 369–372

**Three transcription hazards our records may have got wrong, flagged at the object:**
1. Ref **[6]** prints the third author as **"Tojo T"** — a different initial from "Tojo S" used in every
   other Hamanaka–Hirata–Tojo entry ([7], [8], [14], [15], [23], [24]) and from the chapter's own byline
   ("Satoshi Tojo", p. 205). As printed, this is an inconsistency in the paper's own reference list.
2. Ref **[6]**'s title is printed as **"Implementing 'a generating theory of tonal music'"** — *generating*,
   not *generative*. Transcribed as printed.
3. Ref **[7]** prints the venue as **"the 6th international conference on music information retrieval
   conference (ISMIR2005)"** — the word "conference" appears twice, as printed.
   Refs **[23]** and **[24]** print "**Proceeding** of" (singular) where [8], [14], [15], [26] print
   "Proceedings of".

Also note refs [14] and [15] print "In:Proceedings" with no space after the colon, as transcribed above.

---

## 7. Bearing on R-7, DP-O and L3 grouping

The framework text I read for this section: FRAMEWORK.md §5 "L3 — The read-off facts" and "The boundary
contracts"; §9 "DP-O"; §11 "R-7". Observations only below — **no verdicts taken.**

### 7.1 R-7 ("the literature behind this document is not coverage")

R-7 names, among the hierarchical/multi-resolution alternatives that "were **not read**", "a time-span
reduction tree", and says "DP-O is left open partly for that reason."

**Observations:**
- **This paper is now read at the object, and it is a time-span-reduction-tree system.** ATTA and FATTA
  implement grouping-structure analysis, metrical-structure analysis and time-span reduction (p. 209),
  and FATTA produces a time-span tree fully automatically (p. 214). The "not read" condition of R-7 is
  discharged for this one item, on this one reading.
- **Supports R-7's caution in an unexpected direction:** the time-span reduction tree, as this line
  instantiates it, **is not a harmonic analysis at all.** It publishes grouping boundaries, metrical
  strengths and a binary head-selection tree over notes. It publishes **no chord label, no root, no
  quality, no key, no figured bass, no cadence.** The one GTTM subtheory whose objects are chords —
  prolongational reduction — is explicitly not implemented (p. 209) and its analyzer is "still under
  development" (p. 230). So the alternative R-7 names does not, in this instantiation, compete with the
  framework's L2 decomposition; it is a different question with a different output type.
- **Cuts against treating the time-span tree as a cheap alternative:** the tree it does produce is
  measured, on the paper's own corpus, at **F-measure 0.44 baseline / 0.60 with hand-configured
  parameters / 0.49 fully automatic** (Table 8.4 Total row and p. 230 running text), on **8-bar
  monophonic** excerpts. This is the paper's own number for its own best output, and it is the weakest of
  its three analyzers.
- **Silent** on the other two alternatives R-7 names (tonality at every window size at once; tonality in a
  transform space). Nothing in the chapter addresses either. Tonal pitch space [22] is used as a
  *distance* inside D_GPR7 (p. 214), and the region/chord/basic-space decomposition δ = i + j + k (p. 214)
  is a discrete-label space, not a continuous transform space — but the paper does not treat this as a
  tonality-estimation question at all, and there is **no automated tonal pitch space analyzer** (p. 220).

### 7.2 DP-O (does the framework commit to a hierarchical reading of harmony?)

DP-O's falsifier as the framework states it: "a tree model beating a matched-capacity sequence model on
this repertoire's ground truth, measured on the same corpus and the same axis."

**Observations:**
- **The paper is silent on DP-O's falsifier, and the silence is total.** There is no sequence-model
  comparison of any kind, no matched-capacity control, and no shared corpus with any sequence model. The
  paper *declines* comparison explicitly: "It is difficult to compare the performance of this system with
  that of previous systems because the approaches taken are so different." (p. 228). It therefore
  neither triggers nor weakens DP-O's falsifier. **This is silence, not support.**
- **The paper's hierarchy is over notes, not over harmony.** The time-span tree's nodes are notes with
  heads (Fig. 8.3, p. 209; head types "ordinary, fusion, transformation, cadential retention", p. 219).
  DP-O asks about a hierarchical reading *of harmony* — recursive function, a chord serving as tonic in
  one tonality and dominant in another. The paper's tree makes no such claim about any chord. So it does
  not bear on DP-O's "for it" side either.
- **One point that cuts against, mildly:** the paper's own account of why the harmonic tree is absent is
  that prolongational reduction "is still evolving and is currently more controversial" (p. 209). That is
  a 2013 practitioner statement that the *harmonic*-hierarchy part of the best-formalized hierarchical
  music theory was, at that date, the part its own implementers judged not ready to mechanize. This is
  evidence about maturity, not about accuracy, and it does not touch the falsifier.
- **A second point that cuts against, on architecture rather than accuracy:** the hierarchy this paper
  builds requires **backward feedback links** — GPR7 from time-span/prolongational reduction back into
  grouping, TSRPR5 from metrical structure back into head choice, MPR9 as "a link from the time-span tree
  to the metrical structure" (p. 221). The chapter states this drives "a number of analysis processes by
  trial and error" (p. 220). The framework's boundary contracts (§5) are **forward only**, with "L3 → L2:
  **Nothing.**" A hierarchical reading of the GTTM kind, as implemented here, is not achievable under a
  forward-only contract without dropping GPR7/TSRPR5/MPR9 — which is exactly what ATTA-without-FATTA does
  (p. 214), and FATTA's fully-automatic figures (0.48 / 0.89 / 0.49, p. 230) are the price paid for
  closing the loop automatically rather than by hand. This is an observation about compatibility cost, not
  a verdict on DP-O.
- **Silent** on whether induced categories correspond to textbook harmonic functions (the framework's
  "against it" clause), because the paper induces no categories — its rules are hand-written from GTTM.

### 7.3 L3 grouping (phrase and section grouping among the read-off facts)

The framework places "the **phrase and section grouping**" among L3's published facts, with the reasoning
that "the decisive further evidence is cadential" and that the span's boundaries come from notated cues
while the cadence is aligned to them (§5, L3).

**Observations — this is where the paper bears most directly:**
- **Direct measurement of an automatic grouping analyzer exists here.** Table 8.4 (p. 230) Total row:
  grouping-structure F-measure **0.46** with default parameters, **0.77** with manually configured
  parameters; and p. 230 running text: **0.48** fully automatic under FATTA. Corpus: 100 sections of
  8-bar-length monophonic classical pieces, ground truth by musicology experts using the manual editor,
  cross-checked by three further experts (p. 228, 230).
- **The load-bearing observation for L3:** the gap between 0.77 (hand-tuned per piece, ~10 min/piece,
  p. 230) and 0.48 (fully automatic) is the whole of the system's grouping performance above its 0.46
  default baseline. **Fully automatic grouping recovers essentially none of the hand-tuning gain**
  (0.48 vs baseline 0.46) on this corpus. This cuts against any expectation that a GTTM-style
  grouping analyzer supplies L3's phrase/section grouping without human parameter setting. Stated as the
  paper states it, not as an inference: the paper reports 0.48 and calls it "still outperforming the
  baseline performance" (p. 230), and it does not remark on the size of the margin.
- **The evidence base is disjoint from the framework's.** GTTM grouping preference rules as used here are
  GPR2a/2b (proximity), 3a–3d (change: register, dynamics, articulation, length), 4 (intensification), 5
  (symmetry), 6 (parallelism) — Table 8.1, p. 212. **Cadence is nowhere in the grouping analyzer's rule
  set.** GPR7 (the only rule that reaches back to reduction stability) is not in ATTA (p. 214) and its
  implementation is omitted from the chapter (p. 221). So the paper is **silent** on the framework's
  actual claim about L3 grouping — that cadential evidence is decisive for which notated cues are phrase
  ends. It neither supports nor falsifies that claim; it simply builds grouping from gestalt cues without
  cadence and reports what that gets you.
- **Notated-cue evidence does appear**, in the framework's L1 sense: GPR2a is "slur/rest", GPR2b
  "attack-point", GPR3a "register" (Fig. 8.4, p. 210), and the σ parameter is "the standard deviation of a
  Gaussian distribution, the average of which is the GPR2a boundary" (Table 8.1, p. 212). This is
  consistent with the framework's placement of notated boundary evidence at L1 and the boundary
  *decision* elsewhere — but the paper does not make an architectural claim about this and I do not read
  one into it.
- **Scope mismatch is severe for the section-grouping half of L3.** All measurement here is on **8-bar**
  excerpts (p. 228). "Section grouping" over a whole movement is not measured, not discussed, and not
  claimed. **Silent.**
- **Monophonic-only is a hard scope bar** (pp. 222, 227, 228). The framework's L3 grouping operates on
  notated scores that are in general polyphonic. Nothing in this paper's measured grouping performance
  transfers to polyphonic input on the paper's own terms.
- **The interactive-analyzer timing result** (Table 8.5, p. 231: 575 vs 891, "in seconds", 100 pieces) is
  about human editing throughput, not analysis accuracy. It bears on tooling ergonomics for a
  human-in-the-loop annotation workflow, not on L3's specification. Note that even at 575 (whatever its
  aggregation), producing one GTTM analysis of one 8-bar piece is on the order of **ten minutes of human
  time**. That is an observation about the cost of building GTTM ground truth, which may bear on any plan
  that would use this line's dataset.

### 7.4 Where the paper is simply silent, and why

- **On chord labels, roots, qualities, inversions, figured bass, harmonic rhythm** — the L3 publication
  list minus grouping and cadence. The paper produces none of these. Silent because the subtheory that
  would produce them is not implemented (p. 209).
- **On cadence, of any type.** The words "authentic", "half cadence", "perfect", "deceptive" do not appear
  anywhere in the chapter. "Cadential retention" appears once, as one of four head *types* selectable in
  the time-span tree editor (p. 219) — a GTTM structural label, with no criterion, no detection method
  and no measurement attached. **Silent.**
- **On key/tonality estimation.** The tonality of the piece is *assumed* in Eq. 8.1 ("the distance between
  notes x and y in the tonality of the piece", p. 214) and estimated only informally via GPR7 ("The region
  of the melody and chord progression are estimated in GPR7 here by applying tonal pitch space methods",
  p. 223), with no automated analyzer (p. 220) and no measurement. **Silent** on L2's core question.
- **On abstention / no-chord (DP-Q territory).** Not addressed at all.
- **On annotation disagreement as a ceiling.** The paper acknowledges musical ambiguity gives "more than
  one correct result" (p. 211) yet evaluates against a single "correct" analysis (p. 228) with no
  inter-annotator agreement figure. It does not quantify the ceiling. **Silent.**

---

## 8. What I could not determine

Written at length deliberately; each item is something I actively looked for.

1. **Precision and recall are never defined.** Eq. 8.7 (p. 228) gives the F-measure formula but the
   chapter nowhere states what a true positive is for grouping structure (a boundary at the right
   position? at the right hierarchical level? both?), for metrical structure (a dot count per beat? a
   level assignment?), or for the time-span tree (a branch? a head? a whole subtree?). Without this, the
   Table 8.4 numbers cannot be compared to any figure from another system, and the paper's own refusal to
   compare (p. 228) may partly rest on this. **Not found in the chapter.**

2. **Whether Table 8.5's "Total (100 melodies)" row is a mean or a sum.** The values 575 and 891 are
   smaller than four of the five itemised rows, so they cannot be sums; but the row is labelled "Total"
   and the paper never says. I have recorded them exactly as printed and flagged the reading, but I
   cannot resolve it. The same "Total (100 melodies)" label is used in Table 8.4, where the values are
   clearly averages of F-measures. **Ambiguous in the paper.**

3. **The relationship among "300 pairs", "300 scores" and "100".** p. 230 says "100 pieces from the 300
   scores (with human-validated grouping-structure analysis, metrical structure, and time-span tree)";
   p. 233 says "a dataset of 300 pairs of scores and analysis results by musicologists" and, in the same
   paragraph, "One hundred expert-verified analyses were performed, which is the largest database of
   analyzed results of GTTM thus far." Whether the 300 are all expert-verified, whether the 100 of §8.6.1
   and the 100 of §8.6.2 are the same 100, and whether the "8-bar-length sections" (p. 228) are the same
   objects as the "pieces"/"melodies" of Tables 8.4 and 8.5 — **none of this is stated.** I could not
   resolve it from the chapter.

4. **Whether the FATTA figures (0.48 / 0.89 / 0.49) were measured on the same 100 sections as Table 8.4.**
   The sentence follows immediately after the Table 8.4 discussion and says "Next, the set of parameters
   was optimized using FATTA" (p. 230), which reads as the same corpus, but the paper does not say so and
   I have not assumed it. Likewise, whether any held-out split was used anywhere — **the chapter never
   mentions train/test separation, cross-validation, or held-out data.** Given that the ATTA parameters
   were hand-tuned per piece against the same expert analyses used as ground truth (p. 230), the 0.77
   grouping / 0.90 metrical / 0.60 time-span "configured" figures may be fitted on the graded data. The
   paper does not address this. **Not found.**

5. **The composers, editions, keys and provenance of every named piece.** Tables 8.4 and 8.5 give title
   fragments only ("Traumerei", "Anitras Tanz", "Valse du Petit Chien", …). No composer is printed
   anywhere in the chapter for any of them, and no source edition. **Not found.**

6. **The corpus for the melody-morphing evaluation.** "Ten pairs of sample melodies were selected for A
   and B" (p. 231) — no titles, no composers, no lengths, no selection criterion, and no numeric R values.
   The result is a bare pass on all ten. **Not found.**

7. **The word "extrapolative" in §8.6.3.** p. 231 reads "test that any extrapolative melody M is an
   interpolative melody of melodies A and B" and then "all the extrapolative melodies M … satisfied
   expression (8.8)". Given Eq. 8.8's content (M closer to each of A and B than A and B are to each other)
   and the chapter's framing of morphing as producing *interpolative* melodies (pp. 224, 233), the word
   "extrapolative" appears to be a slip, possibly carried from ref [14] "Melody extrapolation in GTTM
   approach". **I could not determine which is meant and have transcribed as printed rather than
   correcting it.**

8. **Whether the melody morphing method was or was not evaluated.** §8.6.3 (p. 231) reports an evaluation;
   §8.7 (p. 233) states "the evaluation of the melody morphing method are planned in future work." The
   chapter does not reconcile these. My best reading is that §8.6.3 is a formal-property check and §8.7
   means a perceptual/user evaluation, but **the paper does not say this** and I have not written it as
   fact.

9. **Numbering slip at p. 216, §8.2.3.3.** Steps 2 and 3 of the optimization algorithm read "Repeat (8.1)
   for all parameters" and "Iterate (8.1) and (8.2)…", where (8.1) and (8.2) are the equation numbers for
   D_GPR7 and δ(x→y). Read against the list, they must mean list items 1 and 2. **Ambiguous as printed.**

10. **No wall-clock or complexity figure for ATTA/FATTA analysis itself.** The paper says "several minutes
    are needed to finish an analysis" (p. 222) and "a significant amount of time is needed to calculate all
    parameter combinations" (p. 216) and "approximately 10 min per piece to find each plausible tuning"
    (p. 230, human time). **No machine specification, no complexity bound, no runtime table.** Not found.

11. **No inter-annotator agreement figure.** Four experts were involved (one analyst plus "three other
    further experts crosschecked", p. 230) but no agreement rate, no disagreement rate, and no description
    of how disagreements were resolved. **Not found.** This means the ground-truth ceiling for the 0.46 /
    0.84 / 0.44 → 0.77 / 0.90 / 0.60 figures is unstated.

12. **No statistical treatment anywhere.** No confidence intervals, no standard deviations, no significance
    tests, no per-piece variance beyond the five displayed rows. **Not found.**

13. **The number of parameters FATTA actually optimizes.** p. 216 says "there are 46 parameters" and the
    algorithm sweeps "a parameter from its minimum to its maximum value … for all parameters", but the
    default list given is only six symbols (S_rules, T_rules, Ws, Wr, Wl, σ), which are families rather
    than individual parameters. Note also that **"Wr" appears in the default lists on pp. 216 and 230 but
    is not a row in Tables 8.1–8.3** (which list W_m, W_l, W_s). Whether Wr is a typo for W_m, or a
    parameter omitted from the tables, **I could not determine.**

14. **Whether the released dataset includes the time-span trees, or only grouping/metrical.** p. 233 says
    "a dataset of 300 pairs of scores and analysis results"; p. 230 says the 300 scores have
    "human-validated grouping-structure analysis, metrical structure, and time-span tree". The
    prolongational trees are excluded (p. 230), but the file formats and contents of the release are not
    described. **Not found in the chapter.** I did not attempt to fetch the URL.

15. **Any licence, version, or availability statement for ATTA/FATTA source.** **Not found.**

16. **The publication status of the chapter's dataset URL.** The URL is printed as
    `http://music.iit.tsukuba.ac.jp/hamanaka/gttm.htm` (p. 233), which does not match the domain form of
    the corresponding author's email host (`iit.tsukuba.ac.jp`) in any way that lets me check it from the
    page. I transcribed it character by character from the page image and did not verify it resolves.

17. **Refs [10]–[12] and [16]–[21] are cited as classes** ("Many previous music systems [10–12] have their
    own approach to musical analysis", p. 207; "although many music theories have been proposed [18–21]",
    p. 208) **with no per-item discussion.** The chapter gives no comparative evaluation against any of
    them. I list them here only so the omission is on record, not as content.

18. **What "the GTTM manual editor without an ATTA" means operationally** in Table 8.5 — whether the
    human started from a blank analysis, and whether the same annotators did both conditions, and in what
    order. Order effects are not addressed. **Not found.**

19. **Whether the paper anywhere claims applicability to polyphony as future work.** The conclusion's
    future-work paragraph (p. 233) says "It is planned to develop further systems, using time-span trees
    and the results of the music analyzer, for musical tasks such as harmonizing, voicing, ad-lib, etc."
    — "harmonizing" and "voicing" imply polyphonic output, but the chapter **never states that the
    analyzer will be extended to polyphonic input**, and the monophonic bars on pp. 222 and 227 are
    stated without a future-work qualifier. **Ambiguous.**

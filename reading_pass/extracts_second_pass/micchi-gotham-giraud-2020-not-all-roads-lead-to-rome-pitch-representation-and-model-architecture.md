# Second extraction — Micchi, Gotham & Giraud, "Not All Roads Lead to Rome: Pitch Representation and Model Architecture for Automatic Harmonic Analysis"

> **WHAT THIS FILE IS.** The SECOND independent extraction of row 45 of `reading_pass/candidacy_upgrades.md`,
> made under `cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, and following the eight-step
> order the hundred-and-sixty-ninth handoff entry's §3 records. It is written from the paper itself. **The
> first extract — `reading_pass/extracts/micchi-gotham-giraud-2020-not-all-roads-lead-to-rome-pitch-representation-and-model-architecture.md`
> — was NOT opened before this file's §0 to §7 had been written, read back, swept and landed**, which is
> step 7 of that order.
>
> **EVERY LOCATION IN THIS FILE IS GIVEN BY THE PAPER'S OWN PRINTED SECTION NUMBER, TABLE NUMBER, FIGURE
> NUMBER OR FOOTNOTE NUMBER**, together with the printed journal page where that is useful. The held file's
> PDF page *n* is the journal's printed page *n + 41*: PDF page 1 is printed page 42 and PDF page 13 is
> printed page 54.
>
> **CLAIMS ARE LABELED.** `[FACT]` — stated or measured in this paper, at the place named. `[THEORY]` —
> established published theory the paper invokes. `[CONJECTURE]` — the paper's own expectation,
> presumption or proposal, with no measurement behind it in this paper. **A label is about what THIS PAPER
> gives, never about whether the claim is true.**

---

## §0 — What was read, and the bound on this read's independence

**The held file** is `docs/research_papers/micchi_gotham_giraud_2020_tismir_not_all_roads_lead_to_rome.pdf`,
**1,906,114 bytes**, established at this sitting's own staging call and at a listing of
`docs/research_papers/`.

**The page count was established AT THE TOOL**, by a deliberately out-of-range page request, which answered
**"PDF has 13 pages"**. It was not taken from any record. It agrees with the progress record's own row for
row 45, which is a match and not the source.

**What was read:** all thirteen pages, in three requests — pages 1–5, 6–9 and 10–13. **Every image was
checked for presence and legibility at the image itself, not at the call's success line.** Pages re-opened
at the read-back are named in §8.1.

**THE INDEPENDENCE BOUND, DECLARED RATHER THAN CLAIMED AWAY.** This side booted on a handoff entry and read
the session-start material, so it is not innocent of this project's record. Specifically, before this paper
was opened this side had read: the hundred-and-seventy-ninth and hundred-and-sixty-ninth handoff entries
whole; `CLAUDE.md` at its six ruled spans; `DECISIONS.md` whole; `STATUS.md`; the derived gating answer;
the progress record at its banner, gate paragraph and the table rows around row 18's and row 45's; and row
45's own candidacy line. **The progress record's own row for row 45 states a verdict about this paper** —
that it is central because a ratified item rests on it, and that its best configuration requires notated
spelling — **and that is contamination of this read, written down here rather than denied.** What this side
did NOT read before writing §0 to §7: row 45's first extract, `FRAMEWORK.md` at any point, `population.md`,
the slice derivation, the findings surface, either commission, and any other extract's content.

**One further bound.** `reading_pass/extracts_second_pass/sheh-ellis-2003-…-em-trained-hidden-markov-models.md`
— row 18's second extract, this line's most recent — was opened **at its section headings alone**, by a
heading search, so that this file takes the line's own section form rather than inventing one. **No content
line of that file was read.**

---

## §1 — What the paper is, and the identity axis

**THE IDENTITY AXIS IS FULLY ESTABLISHED AT THE DOCUMENT'S OWN FACE**, and this is worth saying plainly
because the member before this one could not be so established.

Printed in the header of PDF page 1: *"Micchi, G., et al. (2020). Not All Roads Lead to Rome: Pitch
Representation and Model Architecture for Automatic Harmonic Analysis. Transactions of the International
Society for Music Information Retrieval, 3(1), pp. 42–54. DOI: https://doi.org/10.5334/tismir.45"*. The
article kind is printed as **RESEARCH**.

- **Title**, printed in full: *"Not All Roads Lead to Rome: Pitch Representation and Model Architecture for
  Automatic Harmonic Analysis"*.
- **Authors**, printed: **Gianluca Micchi\***, **Mark Gotham†** and **Mathieu Giraud\***.
- **Affiliations**, printed at the foot of page 1: *\* Univ. Lille, CNRS, Centrale Lille, UMR 9189 –
  CRIStAL – Centre de Recherche en Informatique Signal et Automatique de Lille, Lille, FR*; *† Cornell
  University, Ithaca, NY, US*. **Corresponding author:** Gianluca Micchi (gianluca.micchi@univ-lille.fr).
- **Venue, volume, issue, year, pagination and DOI** are all printed, on page 1 and again in the *How to
  cite this article* box on page 13.
- **Dates, printed on page 13:** Submitted **04 December 2019**; Accepted **23 March 2020**; Published
  **12 May 2020**.
- **Licence, printed on page 13:** *"© 2020 The Author(s). This is an open-access article distributed under
  the terms of the Creative Commons Attribution 4.0 International License (CC-BY 4.0)"*. The same box
  prints that TISMIR *"is a peer-reviewed open access journal published by Ubiquity Press"*.
- **Running heads** are printed on every page from PDF page 2 onward, carrying *"Micchi et al: Not All
  Roads Lead to Rome"* and the printed page number.

**So the held file establishes at its own face that it is the published journal text**, and nothing this
read needs about its provenance has to be inferred.

**Keywords, printed:** *Roman numeral analysis; functional harmony; machine learning; pitch encoding;
corpus.*

**The document carries six numbered figures and seven numbered tables across its thirteen pages.**
*(ADOPTED AT THE CROSS-CHECK FROM ROW 45's FIRST EXTRACT, which states it where this file did not; checked
here against the figure and table numbers this file itself cites, which run to Figure 6 and Table 7.
§9.4, item 3.)*

**What the paper says it does**, from its own abstract, quoted: *"We report on three main developments.
First, we provide a new meta-corpus bringing together all existing Roman numeral analysis datasets; this
offers greater scale and diversity, not only of the music represented, but also of human analytical
viewpoints. Second, we examine best practices in the encoding of pitch, time, and harmony for machine
learning tasks. The main contribution here is the introduction of full pitch spelling to such a system, an
absolute must for the comprehensive study of musical harmony. Third, we devised and tested several neural
network architectures and compared their relative accuracy."*

And its own summary of the result, quoted: *"Altogether, our best representation and architecture produce a
small but significant improvement on overall accuracy while simultaneously integrating full pitch spelling.
This enables the system to retain important information from the musical sources and provide more
meaningful predictions for any new input."*

**The software is stated to be public**, at §1.4: *"All software developed for this project is freely
available under an open-source licence at https://gitlab.com/algomus.fr/functional-harmony."* §3.5 adds
that the code *"was initially forked from Chen and Su (2018), but all dataset conversions, encodings, and
models are original work."* **Nothing in this repository was checked against that claim and nothing was
fetched.**

---

## §2 — The method, as the paper states it

### §2.1 The task, and the three entangled decisions the paper names

The paper's subject is **Roman numeral (RN) analysis**, which it distinguishes from chord-symbol
description at §1.1: *"Like other representations of tonal harmony, Roman numeral (hereafter 'RN') analysis
focuses on recording chords, specifying the triad quality (major, minor …), seventh (where applicable),
inversion (bass note), and any modifications (such as added and altered notes). Unlike most systems, RNs
also specify an analytical view of the local and global keys to which those chords belong and so also their
harmonic functions (hence the term 'functional analysis')."*

**★ THE PAPER STATES THE ENTANGLEMENT OF THE ANALYTICAL DECISIONS IN ITS OWN WORDS, AND IT NAMES THREE.**
At §1.1, of the descriptive/analytical case: *"there may be many, different, equally credible readings of
the same passage. This stems from the ambiguity inherent in mutually informative decisions over:"* — and
the paper then prints three bullets, quoted verbatim:

- *"whether and where to change chords,"*
- *"whether and where to change keys, and"*
- *"which notes in the score should be represented in the harmonic reduction at all."*

It continues: *"In practice then, while experienced analysts will generally agree over simple contexts,
their analyses may vary widely for more complex cases. In short, our intuitive notions of what is 'in' the
harmony hides a sophisticated set of judgement calls."*

**`[FACT]`** — that this paper states those three decisions as mutually informative, at §1.1, printed page
43. **`[CONJECTURE]`** — everything about what follows for a system's design; the paper draws no design
conclusion from it at that point.

**The paper also states a reductive-view claim** at §1.1: *"Whatever the representation system used, a
chordal description of music involves a reductive view of the total pitch information for all but the
simplest of cases. That is, in both prescriptive and descriptive contexts there will be 'non-harmonic'
pitches that are in the music but not represented in the chords."* **`[THEORY]`**.

**§2's own subject is why the task is hard, and it is argued at two worked examples rather than asserted.**
The section opens by quoting four preference rules it attributes to **Tymoczko et al. (2019)**, printed as
a numbered list — quoted verbatim:

1. *"harmony changes on metrically strong positions and at regular intervals;"*
2. *"to analyse similar material in similar ways;"*
3. *"to identify as 'harmonic' notes that do not belong to any common species of non-harmonic tone (e.g.
   notes that are both leapt-to and leapt-from); and"*
4. *"harmonic analyses that are more consistent with standard harmonic theory."*

**First worked example — J.S. Bach, Prelude in C, BWV846.** Figure 1 (printed page 43) prints measures
1–11 of the score with an RN analysis under the lowest stave. The paper says the rules *"align neatly"*
here, *"pointing in this case to harmony changes once per measure"*, and that *"There may be some
disagreement about where to mark the changes of key (see discussion in section 4), but the changes and
membership of the chords are mostly straightforward."* It then names the first place they are not: *"there
are arguably no non-harmonic tones until measure 23 (see Figure 2). Here, in order to separate harmonic
from non-harmonic, we have to select between two (or more) possible options: F minor (with F, A♭, and C in
the chord, excluding B, D) or B diminished 7th (with B, D, F, and A♭ in the chord, and C eliminated). The
preference for leaping to consonant notes would guide us towards the latter view, though credible arguments
can be (and have been) made on both sides on the basis of the wider progression."* Figure 2 prints measures
22–24 of the same prelude.

**Second worked example — Schubert, 'Einsamkeit', *Winterreise* (D.911, No.12), measures 34–35.** Figure 3
prints the score with three parallel analyses written as lyrics, A1, A2 and A3 from top to bottom; Table 2
summarises them against the four rules. The paper's own conclusion, quoted: *"In cases like this, we will
all have views on how to proceed but no one can claim to have the single, definitive, and unequivocally
'correct' answer."*

**★ AND THE PAPER STATES IN TERMS THAT NO RULE HIERARCHY WILL WORK.** Quoted from §2, printed page 45:
*"The Bach example begins to show that more complex contexts can run these rules into self-contradiction.
It quickly becomes impossible to determine a system of priorities among those rules that will generalise to
all musical cases. Instead, analysts may take these rules for 'in principle' guidance, but must make
complex judgement to arrive at a preferred solution, knowing that it is one among several viable options.
This is a strong incentive for exploring automated systems which can similarly handle such ambiguity,
without depending on a hierarchy among explicit, deterministic rules."* **`[CONJECTURE]`** — the incentive
sentence; the paper measures nothing about rule hierarchies.

### §2.2 The meta-corpus

**`[FACT]`** §3.1: *"We prepared a meta-corpus of harmonic analyses, combining all previously published
corpora of RN analyses as discussed above and itemised in Table 1. To bring these corpora together, we
developed a set of new open source converter tools which we offer to the community."* The four member
datasets are named at §1.3 as **'TAVERN' (Devaney et al., 2015)**, **'ABC' (Neuwirth et al., 2018)**,
**'BPS-FH' (Chen and Su, 2018)** and **'Roman-Text' (Tymoczko et al., 2019)**.

**`[FACT]`** §3.1: *"Altogether, the corpus comprises 201 scores and over 70,000 RN annotations."* Table 1's
own totals are transcribed at §5.1 and checked at §6.1 and §6.2.

**`[FACT]`** §3.1: *"We sought to convert each representation standard directly, without changing or
interpreting those analyses except in case of clear errors."* And: *"In all cases, the .rntxt files set out
the identity of analysts, proof-readers, and converters involved, and the original datasets are available
online for comparison."* For ABC the paper states it used *"the version reported by Tymoczko et al.
(2019)"*.

**★ MULTIPLE ANALYSES OF THE SAME MUSIC ARE TREATED AS INDEPENDENT, AND THE PAPER SAYS SO AND SAYS WHY IT
IS NOT QUITE RIGHT.** Quoted from §3.1, *Different Annotators*, printed page 46: *"Among these datasets,
'TAVERN' is the only one to include more than one alternative reading of the same piece by different
annotators… In this study, for the sake of simplicity, we have elected to treat each of these analyses
independently. It is clearly not quite right to treat multiple analyses of the same music as equivalent to
analyses of separate pieces, and doing so will likely introduce some bias in the model; however, we
consider this a small detraction relative to the gain in variance afforded by the alternative readings."*
**`[FACT]`** that TAVERN is the only one of the four with alternative readings by different annotators, as
this paper states it; **`[CONJECTURE]`** that the bias is small relative to the gain — the paper measures
neither side of that comparison.

**★ AND IT NAMES A CONFOUND IT DOES NOT CONTROL.** Quoted: *"each of the original datasets focuses on a
different style, and so there is a non-separable correlation between annotators and musical genres. Future
work could explore inter-annotator stylistic variance, in order to get a data-driven sense of the variety
of approaches and how best to balance them as the provision of corpora continues to grow."* **`[FACT]`**
that the paper declares the correlation non-separable in its data.

### §2.3 The three data formats, and the six properties of the tabular one

**`[FACT]`** §3.1, *Data Formats*: three formats, each with a stated role — *"For analysis input, we
recommend the human-readable and music21-parseable 'Roman text' (.rntxt) format (Tymoczko et al., 2019);
for the presentation of results aligned with scores, we offer .json files that can be interpreted and
visualised by Dezrann (Giraud et al., 2018); and for machine learning, we prefer a tabular representation
based on that originally proposed by Chen and Su (2018)."*

**`[FACT]`** The tabular format's six properties, printed as a numbered list at §3.1 and quoted here in
compressed form with the paper's own defining clauses kept verbatim:

1. **Start offset** — *"the beginning of the annotation in question as measured from the start of the score
   in 'quarter length' (1 = 1 quarter note)"*;
2. **End offset** — *"an equivalent for where the annotation ends (usually coincident with the start of the
   next entry)"*;
3. **Key** — *"tonic, specifying full pitch spelling (so that G♯ ≠ A♭) and mode (uppercase for major;
   lowercase for minor)"*;
4. **Quality** — *"for example, major or minor triad; major, minor, or dominant seventh"*;
5. **(Scale) Degree** — *"from 1 (the tonic) to 7 with the potential for accidental modifications (e.g. ♯4)
   and/or secondary, 'tonicised' degrees (e.g. '5/5')"*;
6. **Inversion** — *"counting from 0 (root position: bass note = chord root) to a maximum of 3 (thus
   supporting all inversions of seventh chords, but no ninths)."*

**★ THERE ARE TWO DIFFERENT SIXES IN THIS PAPER AND THEY ARE NOT THE SAME SIX.** The tabular format's six
PROPERTIES above are *Start, End, Key, Degree, Quality, Inversion*. The network's six OUTPUT LABELS, at
§3.2, are *Key, Degree 1, Degree 2, Quality, Inversion, Root* — no start or end offset, the single Degree
split into two, and Root added. **This read met no sentence that sets the two sixes side by side**, and a
reader who carried "six sub-labels" from one to the other would be wrong about three of the six. Recorded
here because the record's own use of this paper turns on the six output labels.

### §2.4 Time encoding

**`[FACT]`** §3.2, *Time*: the paper names two approaches and states its choice. The first, attributed to
**Oore et al. (2018)**, *"represents the score as a series of three possible event types: note on, note
off, and time shift (following MIDI conventions)"* — of which the paper says *"This representation overcomes
certain problems particularly common in music generation tasks, but it can conceal the music's metrical
structure, which is important in harmonic analysis."*

The second: *"Much better represented in the literature is the alternative 'frame-based' encoding method,
where each input vector is an individual time frame. Most studies on symbolic music opt for some
factor-of-two multiple for the smallest slice (1/8th, 1/16th, or 1/32nd notes) and accept the errors that
this will entail for shorter values and for all triplets (which are quantised to binary positions)."*

**`[FACT]`** The choice, quoted: *"We follow this latter practice for equal-duration, binary division
frames. In our case, we use a 32nd note for input encoding (notes) and 8th note for the output (chords), as
the harmonic rhythm is almost always (much) slower than the surface rhythm. Finally, we divide all scores in
segments of equal quarter-note duration and pad with zeroes to the right when needed."*

**`[FACT]`** The triplet loss is accepted in terms rather than measured: the sentence above says such
systems *"accept the errors that this will entail"*, and **this read met no measurement of that error in
the pages as read**.

### §2.5 Pitch encoding — two dimensions, six options

**`[FACT]`** §3.2, *Pitch*: *"The options for pitch encoding may be set out in two dimensions. The first
concerns pitch spelling. Here we must choose between using pitch class representations (12 per octave, and
no difference between the enharmonic equivalent pairs like G♯ and A♭), or maintaining the full pitch
spelling (with 21 possibilities per octave for single sharps/flats, and 35 for double)."*

**`[FACT]`** The second dimension, quoted: *"The other dimension concerns registral information. Keeping
octave information leads to richer data, but excluding it would be more compact. We propose a third,
'compromise' option reflecting the special role of the bass in tonal harmony in defining both chordal
inversion and other important matters for harmonic progression. In this case, music is encoded with two
vectors per frame: one with the lowest note and another with the total pitch content. The fact that the
lowest note may not be indicative of the bass is one of the many tasks that the system would need to
learn."*

**★ THAT LAST CLAUSE IS THE PAPER'S OWN CAVEAT ON ITS BEST CONFIGURATION**, and it is stated and not
measured: the encoding that wins on every axis (see §5.5 and §5.6) is the one whose "bass" vector the paper
itself says is only the **lowest sounding note**, not the bass in the harmonic sense. **`[FACT]`** that the
paper says so; **`[CONJECTURE]`** that the system learns the difference — the paper offers no measurement of
that.

**`[FACT]`** The six options and their input dimensions are Table 4, transcribed at §5.4.

**`[FACT]`** The frame matrix, quoted: *"Regardless of the pitch space chosen, we define a Boolean matrix
with time frames on one axis and pitches on the other: The value is 1 if the pitch is present in that
frame, and 0 otherwise. In this encoding, multiple pitches may be activated in the same time frame where
they sound simultaneously in the source (as in chords, for example). This data representation reduces to the
familiar piano roll notation when using CPf for the pitch space."*

**★ AND THE ONE THING THE ENCODING DELIBERATELY THROWS AWAY IS NAMED, WITH THE REASON STATED AS AN
EXPECTATION.** Quoted: *"One potential shortcoming of such a frame-based encoding is that it fails to
distinguish between repeated and held notes. Hadjeres et al. (2017) and Liang et al. (2017) include special
symbols to disambiguate this on voice-separated music. When the number of voices is not fixed, one symbol
per note is required, doubling the size of the input vector. We decided not to encode that information
partly due to the loss of compactness, but also because we do not expect distinguishing tied from repeated
notes to be especially important for harmonic analysis."* **`[CONJECTURE]`**, explicitly — *"we do not
expect"* — **and this read met no measurement of it in the pages as read.**

### §2.6 The six output labels, and the sum-against-product argument

**`[FACT]`** §3.2, *RN Output Labels*: *"Continuing to follow Chen and Su (2018) we output the harmonic
analysis with six labels: Key, Degree 1, Degree 2, Quality, Inversion, and Root. The two labels for scale
degrees handle cases of tonicisations in the format 'Degree 2/Degree 1'."*

**`[FACT]`** The label spaces depend on the input encoding, quoted: *"The labels for keys and chord roots
depend on the choice of the input representations. For all CP cases there are 12 possible chord roots and 24
keys (12 major and 12 minor). When the input is in a PS encoding, the number of possibilities increases:
there are 35 roots and thus 70 keys for the double sharp/flat condition."* Footnote 15 immediately qualifies
the 70: *"However, not all those keys can actually be used because some diatonic pitches would have triple
flats or sharps. We will discuss more about what keys we actually use in the next section."*

**★ THE PASSAGE THE CANDIDACY LINE POINTS THIS PROJECT AT, QUOTED WHOLE.** §3.2, printed page 47. *(That
this passage is the one the record uses is a **RELAY**: `reading_pass/candidacy_upgrades.md` line 117, read
at that file, calls this paper *"the source of DP-A's self-contradiction quotation"*. **What DP-A says, and
how it uses the quotation, was not checked — `FRAMEWORK.md` was not opened by this read at any point** —
so nothing below is a statement about the record.)*

> *"There is some redundancy built into this system as it is possible to derive the root unambiguously from
> other features. However, learning redundant variables can be helpful to the algorithm's success. The
> division of each RN label into six independently-computed sub-labels reduces the complexity of the task,
> since the total number of possible outputs for our best-performing representation is Σᵢcᵢ = 123 ≪ ∏ᵢcᵢ ≈
> 22·10⁶, where cᵢ is the number of output classes for each separate target label. It also improves the
> interpretability of the results, allowing one to focus on each aspect separately."*
>
> *"This comes at the cost of a potential for self-contradictory outputs in which the six sub-labels have
> different ideas about the chord. In practice, we find that this is only rarely a problem, arising in the
> particular case of the 'no chord' label used by the ABC dataset (only) for passages with rests and/or
> single line melodies. Given the inconsistency in the source data, we do not include a provision for the
> 'no chord' case. Instead, we fill any such gap with a continuation of the foregoing chord, except in the
> case of beginnings, for which we start the first chord early."*

**WHAT THAT PASSAGE DOES AND DOES NOT ESTABLISH, STATED EXACTLY.**

- **`[FACT]`** The two numbers, 123 and ≈ 22·10⁶, and that they are of the best-performing representation.
  Both are re-derived at §6.3 from Figure 5's own printed class counts and both close.
- **`[FACT]`** That the paper reports self-contradictory outputs as *"only rarely a problem"*.
- **★ BUT THE RARITY CLAIM CARRIES NO MEASUREMENT IN THIS PAPER.** No rate, no count and no population is
  met anywhere in the thirteen pages as read. *"In practice, we find"* is the whole of its support as
  printed.
- **★ AND THE CLAUSE THAT FOLLOWS NARROWS IT FURTHER THAN A READER MIGHT CARRY IT.** The paper does not say
  that contradictions are rare in general; it says the problem arises *"in the particular case of the 'no
  chord' label used by the ABC dataset (only)"*. **The one instance of the cost that sentence names is a
  data-coverage gap in one of the four datasets**, and the remedy it gives is a gap-filling rule, not a
  consistency mechanism.
- **`[FACT]`** §3.5 states in terms that no consistency is enforced: *"we did not enforce consistency
  between labels."* §5.1 lists enforcing it as **future work**: *"one could also explore a combination of
  learned and/or deterministic post-processing to enforce the kind of consistency between labels discussed
  above."*

### §2.7 Transposition augmentation, and the two constraints that bound it

**`[FACT]`** §3.3: *"In practice, keys are not used equally. It is common in both analysis and generation
tasks to augment the dataset by transposing it to multiple keys (Huang et al., 2018; Chen and Su, 2019).
While a single piece in two transpositions should not be considered equivalent to two distinct pieces (for
reasons somewhat analogous to the status of multiple analyses of the same piece discussed above),
transposition does stand to augment considerably the overall size of the dataset."*

**★ AND THE PAPER STATES THE STRUCTURAL CONSEQUENCE OF SPELLING FOR AUGMENTATION IN ONE SENTENCE.** Quoted:
*"While working within the 'CP' encoding space (as is the case for all work based on MIDI), there are only
12 distinct transpositions: one for each distinct pitch class."* And: *"When including pitch spelling,
transposition moves not through a circle, but a spiral, potentially infinitely."* **`[THEORY]`**.

**`[FACT]`** The two constraints, quoted:

- **On pitches:** *"Our first constraint limits the pitches to double flats/sharps from F♭♭ to B♯♯. To
  enforce this constraint, we need to retrieve the 'chromatic ambitus' of each piece, delimited by the
  'flattest' and 'sharpest' pitches used. For instance, Schubert's 'Einsamkeit' (Figure 3) ranges from E♭ to
  E♯, meaning that it can be transposed by 12 further steps in the flat direction and 8 steps sharpwards
  while still remaining within the set limit of double sharps and flats."*
- **On keys:** *"Our second constraint limits the keys to a narrower range from C♭ to C♯ majors and their
  relative minors (A♭ to A♯) such that the diatonic pitches are limited to single flats/sharps. We do this
  to reduce the computational load without losing actual information, as real pieces very rarely go outside
  these key boundaries."*

Both constraints are re-derived against the paper's own worked example at §6.4 and §6.5; both close exactly.

**`[FACT]`** The measured spread of the augmentation is **Figure 4**, whose caption reads *"The distribution
of work transpositions that remain within the set limits of F♭♭ – B♯♯ for pitches and C♭ – C♯ for keys."*
The paper's own reading of it, quoted: *"The majority of pieces can be transposed 10–13 times, within an
overall range from as few as 3 transpositions (for highly chromatic works) to as many as 15 (for pieces that
never leave their home key or its relative). The more harmonically adventurous pieces are thus also the
least numerously represented."* **What this read does and does not take from Figure 4 is at §5.8.**

**`[CONJECTURE]`** The paper's own proposed remedy, unmeasured: *"As a possible, partial solution, one could
transpose segments of the score separately. As the chromatic and key range of each segment is necessarily
less than (or occasionally equal to) that of the overall work, these sections would be transposed more
times."*

### §2.8 The network architecture

**`[FACT]`** §3.4, the two-part division, quoted: *"We propose a neural network architecture that divides
the process of RN analysis into two separate but interconnected parts (see Figure 5). The first part
analyses the local context with a window size of 2 quarter notes. This corresponds to the human analyst
distinguishing between harmonic and non-harmonic tones, producing a chordal reduction and deriving the
Quality, Inversion, and Root labels. The second part, in turn, focuses on the more global matters of chord
progressions and key selection. The RN analysis emerges from the structure and pattern of those
progressions, expressed in the Key, Degree 1, and Degree 2 labels."*

**★ THE ASSIGNMENT OF THE SIX LABELS TO THE TWO PARTS IS THE ARCHITECTURE'S OWN CLAIM ABOUT WHICH QUESTIONS
ARE LOCAL AND WHICH ARE GLOBAL** — Quality, Inversion and Root local; Key, Degree 1 and Degree 2 global —
**and the paper states it as a correspondence to what a human analyst does, not as a measured result.**
**`[CONJECTURE]`** as to the correspondence; **`[FACT]`** as to what the architecture does.

**`[FACT]`** The local part, quoted: *"The local part (Conv) is a 1-D implementation of the convolutional
architecture 'DenseNet' (Huang et al. 2016). We convolve along the time domain and encode pitches as
different feature maps on independent channels (analogous to different colour channels in image analysis).
One particularly distinctive and relevant feature of DenseNet is the preservation of the same feature maps
for multiple convolutional layers in order to analyse the same information at successive levels of
abstraction. This allows the network to keep some important information in memory instead of having to learn
it anew every time. The DenseNet also contains pooling layers that we use to pass from the time resolution
of the input notes to those of the output chords."*

**`[FACT]`** The two alternatives for the global part:

- **Dilated convolution (Dil)** — *"the type introduced by Yu and Koltun (2015) and adapted to 1-D data by
  Oord et al. (2016). We use a non-causal dilated convolution, meaning that we allow the system to use both
  past and future events when determining each chord. The convolution is made of 4 layers with 64 kernels
  each of size 3 and a dilation of 3ˡ, where l is the layer index. This means that each prediction can use
  information from a total context of 3⁴ = 81 eighth notes: the present one as well as 40 from the past and
  40 from the future. In most cases, this should be ample context for analysing chord progressions. This
  architecture is fast and scales well with the length of the input segment, both in terms of speed and
  reliability."*
- **Bidirectional recurrent network with gated recurrent units (GRU)** — *"(Cho et al., 2014). Being
  bidirectional, this method also uses information from both past and future frames, though the process
  differs from that of the dilated architecture. The hidden state is made of 64 neurons per direction and
  uses a dropout rate of 0.3. This architecture is more expressive than the dilated convolution since it
  allows for correlations of theoretically infinite length. Further, the gated internal structure is more
  sophisticated than those in dilated convolutions, allowing for the discovery of more complex
  correlations. That said, it is also harder to train and scales poorly with the length of the given input
  segments."* Footnote 16 gives the choice of cell: *"We prefer GRUs over LSTM cells due to their greater
  compactness."*

**`[FACT]`** The segment length, and the reason given for it: *"Therefore one needs to strike a balance in
terms of segment length: segments must be long enough to take advantage of the recurrent nature of the
network, but short enough to make training feasible. We elected to divide the scores in non-overlapping
segments of 80 quarter notes' duration."*

**`[FACT]`** The head, quoted: *"With either architecture, the second part ends with a fully connected layer
of 64 neurons. Each label is predicted by a fully connected layer with softmax activation, whose size is
determined by the number of classes for the label at hand. The network is trained end-to-end to ensure
strong connection between the local and global tasks. The loss function used is the standard categorical
cross-entropy loss. This is computed on each of the six target labels separately before the results are
added, with an equal weighting."*

**`[FACT]`** The baseline, quoted: *"As a baseline for comparison of these two approaches, we also trained a
standard GRU model without local context analysis. We refer to this as PoolGRU as it is preceded by pooling
layers to reduce the resolution on the time axis."*

### §2.9 Training, the split, and the two training modes

**`[FACT]`** §3.5, the split, quoted: *"We randomly allocated 90% of the available scores to the training
set, reserving the remaining 10% for validation. Importantly, we implemented this proportion not only for
the corpus overall, but for each of the corpora individually. For the special case of TAVERN, those works
assigned to the training set included the score and both of the corresponding analyses; pieces in the
validation by contrast included only one of the analyses (randomly selected). In order to provide direct
comparison with Chen and Su (2018, 2019), we also calculated results using only their dataset, divided in
the same way."*

**★ THE PAPER CALLS ITS HELD-OUT TENTH THE *VALIDATION* SET, AND THIS READ MET NO SEPARATE TEST SET IN THE
PAGES AS READ.** Every accuracy reported in §4 is stated against that validation set, and §4.2 names it as
such (*"different from that of the validation corpus"*). **What is reported is therefore a validation
figure on the paper's own naming, and this read met no description of a held-out set beyond it.**

**★ AND THE UNIT OF THE SPLIT IS THE SCORE, SO NO SCORE SITS IN BOTH HALVES.** §3.5's own words are *"90%
of the available **scores**"*. *(ADOPTED AT THE CROSS-CHECK FROM ROW 45's FIRST EXTRACT, which states the
unit where this file had recorded only the proportion; verified here at §3.5's own sentence. §9.4, item 1.)*

**`[FACT]`** The two training modes, quoted: *"We trained in two ways. In the first (global) approach, all
six labels are predicted at the end of the second part (Dil or GRU). In the second (local) method, the
Quality, Inversion, and Root labels are determined at the end of the first, local part of the network and
used to determine the key and degree. As discussed, we did not enforce consistency between labels. Given the
lack of local context, PoolGRU can only be trained in global mode."*

**`[FACT]`** The implementation and cost, quoted: *"The network was encoded in Python v3.7 using Tensorflow
v1.14… Our best model has about 94,000 trainable weights in total: 33,000 for the local part, 43,000 for the
global, and the remaining 18,000 for the fully connected layers. Depending on the model, the total training
time ranges from 20 minutes to 3 hours, when run on a CPU-only high-performance-computing server."*

---

## §3 — Coupling facts

The commission's §4 makes these mandatory: what the work assumes upstream, what it hands downstream, and
its own stated scope. **Everything here is the paper's, at the place named. Nothing is inferred about what
this project should do with it.**

### §3.1 What it ASSUMES about its upstream

- **A symbolic score, not audio.** The input is a frame matrix of pitches derived from a score (§3.2,
  *Pitch* and *Time*). **This read met no audio, no chromagram and no transcription step in the pages as
  read.**
- **★ NOTATED PITCH SPELLING, FOR THE CONFIGURATIONS THAT USE IT — AND THE PAPER SAYS WHICH INPUT FORMATS
  CAN SUPPLY IT.** Footnote 14, quoted whole: *"Systems using MIDI are necessarily limited to the former;
  the latter is only available to richer input formats like \*\*kern, MusicXML, and MEI."* The *former* is
  chromatic pitch, the *latter* pitch spelling. **So the paper's own best configuration is unavailable on
  MIDI input by its own statement.** §4.1 states the condition on the conclusion in the same terms: *"we
  conclude that the spelling representation is preferable where the data is available."*
- **Quantisable rhythm.** §3.2 assumes the score can be divided into equal 32nd-note frames and accepts the
  quantisation error for triplets and shorter values.
- **A ground-truth RN analysis for training, in one of four published corpora**, convertible to .rntxt
  (§3.1). The analyses are taken *"without changing or interpreting"* them *"except in case of clear
  errors"*.
- **A key and chord vocabulary bounded in advance.** Keys are limited to 15 majors and their relative minors
  (§3.3); Quality, Inversion, Degree and Root each have a fixed class count (Figure 5).
- **NOT assumed:** voice separation (§3.2 states the repeated/held distinction is deliberately not encoded);
  metrical strength (§5.1 reports it was tried informally and is not in the encoding); dynamics, texture or
  other score indications (§5.1, named as future work).

### §3.2 What it HANDS downstream

- **Six labels per output frame** — Key, Degree 1, Degree 2, Quality, Inversion, Root — at a time
  resolution of an **eighth note** (§3.2, *Time*; §3.2, *RN Output Labels*).
- **Each label as a softmax over its own class set** (§3.4). **`[FACT]`** that a distribution exists at the
  output layer by construction; **the paper reports no use of it** — no confidence, no ranked alternative,
  no abstention and no margin was met defined, reported or consumed in the thirteen pages as read.
- **★ NO CONSISTENCY GUARANTEE BETWEEN THE SIX.** §3.5: *"we did not enforce consistency between labels."*
  §3.2 states the cost as *"a potential for self-contradictory outputs in which the six sub-labels have
  different ideas about the chord."* **So what is handed downstream can be internally contradictory, and the
  paper provides no mechanism that detects or marks it.**
- **NO segmentation object.** Chord spans are implied by runs of equal labels across eighth-note frames;
  **nothing in the method as the paper describes it predicts a boundary, span or segment as a thing in its
  own right**, and §4.2 names the consequence as the most common error type (see §5.7 and §7.3).
- **NO non-chord-tone labelling.** The local part is described as *"corresponding to"* the analyst's
  harmonic/non-harmonic distinction (§3.4), but **no note-level harmonic/non-harmonic output is produced or
  evaluated.**
- **A 'no chord' state is NOT handed downstream**: §3.2 states in terms that no provision for it is
  included, and that gaps are filled with a continuation of the foregoing chord.

### §3.3 Its own STATED scope and limits

- **Repertoire**, as Table 1 states it: Mozart, Beethoven, Bach and *"Various (19th C.)"* — **201 scores,
  every one of them Western classical**, with the wider-repertoire datasets named at §1.3 explicitly NOT
  part of the meta-corpus (*"datasets on harmonic analysis of that wider repertoire do not generally include
  functional labels"*).
- **The accuracy metric is declared inadequate by the authors themselves.** §5.1, quoted: *"A simple
  right/wrong accuracy metric is not the best way to measure the performance of an RN analysis algorithm, as
  several different readings are often equally viable. Even taking that into account, the 43% total accuracy
  that we report is still far from ideal."*
- **The spelling result is declared not statistically significant.** §4.1, quoted: *"On the other axis of
  pitch representation, using full pitch spelling generally leads to slightly higher results overall, but
  the results are not statistically significant."*
- **The local/global comparison is declared ambiguous.** §4.1, quoted: *"Comparing local and global training
  yields a much more ambiguous result that invites further study. The difference in the total result is
  statistically not significant."*
- **Three error classes are named and one is declared most common** (§4.2; see §5.7 and §7.3).
- **A fourth class is named as unacceptable rather than as ambiguity** — §4.2's closing paragraph on
  Beethoven's sixth sonata.
- **The corpus's own quality is not warranted.** Footnote 12, quoted: *"See https://github.com/DCMLab/ABC/issues
  for ongoing discussion over issues with the original corpus. Both Tymoczko et al. and Neuwirth et al. have
  plans to release a corrected and updated version of this corpus; that would effectively provide a second
  multiple-annotator dataset with which to study inter-annotator variance."*

---

## §4 — Claims, labeled

Each claim is given once, at the place the paper prints it. **The label says what THIS paper supplies.**

| # | Claim | Label | Where |
|---|---|---|---|
| C1 | RN analysis records chord quality, seventh, inversion and modifications, and additionally an analytical view of local and global keys — hence *functional* analysis | `[THEORY]` | §1.1, p. 42–43 |
| C2 | A chordal description is a reductive view of the total pitch information in all but the simplest cases | `[THEORY]` | §1.1, p. 43 |
| C3 | Three decisions are mutually informative and jointly ambiguous: whether/where to change chords, whether/where to change keys, and which notes enter the harmonic reduction at all | `[FACT]` that the paper states it; the entanglement itself is `[THEORY]` | §1.1, p. 43 |
| C4 | No hierarchy among explicit deterministic preference rules generalises to all musical cases; the rules run into self-contradiction | `[CONJECTURE]` — argued at two examples, not measured | §2, p. 45 |
| C5 | A single passage can carry several credible readings, and no one can claim the single definitive correct answer | `[THEORY]`, argued at the Schubert example and Table 2 | §2, p. 45 |
| C6 | An automatic system returning full RN analysis is a defining benchmark for automatic harmonic analysis | `[CONJECTURE]` | §1.4, p. 44 |
| C7 | The meta-corpus comprises 201 scores and over 70,000 RN annotations, drawn from four published corpora | `[FACT]` | §3.1 and Table 1, p. 44 |
| C8 | Treating multiple analyses of the same piece as independent will likely introduce some bias, but the bias is small relative to the gain in variance | `[CONJECTURE]` — neither side measured | §3.1, p. 46 |
| C9 | There is a non-separable correlation between annotators and musical genres in this corpus | `[FACT]` as a declared property of the data | §3.1, p. 46 |
| C10 | Frame-based encoding is better represented in the literature than event-based, and conceals less of the metrical structure | `[FACT]` about the literature as the paper reports it; `[CONJECTURE]` as to the consequence | §3.2, p. 46 |
| C11 | 32nd-note input frames and 8th-note output frames suffice, because harmonic rhythm is almost always much slower than surface rhythm | `[CONJECTURE]` — the premise is asserted, the sufficiency unmeasured | §3.2, p. 46–47 |
| C12 | Distinguishing tied from repeated notes is not expected to be especially important for harmonic analysis | `[CONJECTURE]`, explicitly *"we do not expect"* | §3.2, p. 47 |
| C13 | Splitting the RN label into six independently-computed sub-labels reduces task complexity from ∏ᵢcᵢ ≈ 22·10⁶ to Σᵢcᵢ = 123, and improves interpretability | `[FACT]` for the two numbers; `[CONJECTURE]` for "reduces the complexity" as a claim about learnability | §3.2, p. 47 |
| C14 | The cost of the split is a potential for self-contradictory outputs, which in practice is only rarely a problem, arising in the particular case of ABC's 'no chord' label | `[CONJECTURE]` — **no rate, count or population was met in the pages as read** | §3.2, p. 47 |
| C15 | With pitch spelling, transposition moves through a spiral rather than a circle and is potentially infinite; two constraints bound it | `[THEORY]` for the spiral; `[FACT]` for the two constraints as implemented | §3.3, p. 47–48 |
| C16 | Real pieces very rarely go outside the key boundaries C♭–C♯ major and A♭–A♯ minor, so the constraint loses no actual information | `[CONJECTURE]` — asserted, with Figure 4 showing the transposition spread but no count of pieces excluded | §3.3, p. 48 |
| C17 | The local part corresponds to the human analyst distinguishing harmonic from non-harmonic tones; the global part to progressions and key selection | `[CONJECTURE]` — an interpretive correspondence, not a measured one | §3.4, p. 48 |
| C18 | Each dilated-convolution prediction sees a total context of 3⁴ = 81 eighth notes, 40 past and 40 future, which should be ample for chord progressions | `[FACT]` for the arithmetic; `[CONJECTURE]` for *"should be ample"* | §3.4, p. 48 |
| C19 | The GRU is more expressive than the dilated convolution but harder to train and scales poorly with segment length | `[THEORY]`, with the measured comparison at Table 6 | §3.4, p. 48–49 |
| C20 | ConvGRU is the best-performing architecture, significantly better than PoolGRU (p < 10⁻²) | `[FACT]` | §4.1 and Table 6, p. 49–50 |
| C21 | Including bass information markedly improves performance not only on inversion but on all tasks (p < 10⁻²) | `[FACT]` | §4.1 and Table 6, p. 49–50 |
| C22 | Full pitch spelling leads to slightly higher results overall, but **not statistically significantly**; since it performs a harder and more musically relevant task without being worse, it is preferable where the data is available | `[FACT]` for the non-significance; `[CONJECTURE]` for the preference conclusion | §4.1, p. 49–50 |
| C23 | The local/global comparison is ambiguous: the total difference is not significant, but the difference on the intermediate (local) labels such as quality is (p < 10⁻⁶) | `[FACT]` | §4.1, p. 50 |
| C24 | The best model achieves a small but significant improvement over the previous state of the art while taking full pitch spelling into account | `[FACT]` as to the figures in Table 5; the word *significant* is supported by the t-tests the paper reports, which are on the architecture axis, the bass axis and the quality label across training modes — not on the Table 5 comparison itself | §4.1 and Table 5, p. 49 |
| C25 | Divergences centre on three types: segmentation errors, mislabeling of rare chords, alternative readings — and segmentation *"appears to be the most common discrepancy"* | `[CONJECTURE]` for the ranking — **no per-class count or rate is given** | §4.2, p. 50 |
| C26 | The predictions tend to change chord more frequently than human analyses, particularly in more complex passages, presumably to allow a cleaner reading in small spans | `[FACT]` for the tendency, exhibited at Table 7; `[CONJECTURE]` for the *"presumably"* explanation | §4.2 and Table 7, p. 50–51 |
| C27 | The system is highly reluctant to identify secondary/tonicised and chromatic chords such as augmented sixths, presumably because they are relatively rare in the corpus | `[FACT]` for the reluctance, exhibited at the Schubert case; `[CONJECTURE]` for the cause | §4.2, p. 50 |
| C28 | Corpora with multiple readings of the same music would be especially helpful, offering a list of viable options rather than one correct answer | `[CONJECTURE]` | §4.2, p. 50 |
| C29 | Informal testing of metrical strength did not yield significant gains | `[FACT]` as a reported negative result, **with no protocol, figure or population given** | §5.1, p. 51 |
| C30 | A musically relevant loss function, using a distance metric between chords of the same function, could improve evaluation | `[CONJECTURE]` | §5.1, p. 51 |
| C31 | Learned and/or deterministic post-processing could enforce consistency between labels | `[CONJECTURE]`, and it is the paper's own acknowledgement that consistency is not enforced now | §5.1, p. 51 |
| C32 | Systems using MIDI are limited to chromatic pitch; spelling is available only to richer formats such as \*\*kern, MusicXML and MEI | `[FACT]` | Footnote 14, p. 52 |

---

## §5 — Measured results, with corpus, measure and value as the paper states them

**Every value below is transcribed from the printed table or figure named, and nothing is converted,
rounded or re-expressed.** Arithmetic this read performed on these values is kept apart, in §6.

### §5.1 Table 1, transcribed — the meta-corpus

Caption, quoted: *"The contents of our meta-corpus, drawing together existing harmonic analysis datasets.
The relative size of each corpus is given by the total, combined number of RNs in the analyses, the number
of measures in the scores, and also the 'Quarter length': a metric for the total length in quarter notes."*

| Dataset | Composer/s | Movements or equivalent | Quarter length | Measures | RNs |
|---|---|---|---|---|---|
| TAVERN | Mozart | 10 theme and variations sets | 7 712 | 2 773 | 8 779 |
| | Beethoven | 17 theme and variations sets | 12 840 | 5 128 | 15 959 |
| ABC | Beethoven | 16 string quartets, 70 movements | 48 811 | 15 881 | 29 652 |
| BPS-FH | Beethoven | 32 piano sonata first movements | 30 992 | 9 420 | 11 337 |
| Roman Text | Bach | 24 preludes | 3 168 | 819 | 2 165 |
| | Various (19th C.) | 48 romantic songs | 8 326 | 2 791 | 5 283 |
| **Totals** | | **201 scores** | **111 859** | **36 812** | **73 175** |

### §5.2 Table 2, transcribed — the three readings of the Schubert passage

Caption, quoted: *"Different interpretations of measures 34 and 35 of Schubert's 'Einsamkeit' (see Figure
3). The analyses are written in .rntxt format (Tymoczko et al., 2019), as explained in Section 3.1. The
'rules' in the second and third column are set out at the beginning of Section 2."*

| | RN | Rules followed / *broken* |
|---|---|---|
| A1 | m34 b: i / m35 i | rules 1 and 4 / *rule 3* |
| A2 | m34 b: i b1.5 Ger42 / m35 Ger42 | rules 3 and 2 / *rule 1* |
| A3 | m34 b: i / m35 G: I | rules 1 and 4 / *rule 3* |

**★ A1 AND A3 CARRY IDENTICAL RULE VERDICTS IN THIS TABLE** — both *"rules 1 and 4"* followed and *"rule
3"* broken — **while differing in their analysis**: A1 stays in B minor at m35, A3 reads m35 as G major.
**So the paper's own rule set does not separate two of its own three readings**, which is a demonstration of
C4 stronger than the prose states, and the prose does not point it out.

### §5.3 Table 3, transcribed — the Bach extract in both representations

Caption, quoted: *"The RN and tabular representations used corresponding to the Bach extract in Figure 1.
The first column sets out RNs in Tymoczko et al. (2019)'s 'Roman text' format, and the remaining columns
unpack that information according to our adaptation of Chen and Su (2018)'s tabular standard."*

| RNTXT | Start | End | Key | Degree | Quality | Inv. |
|---|---|---|---|---|---|---|
| m1 C: I | 0.0 | 4.0 | C | 1 | M | 0 |
| m2 ii42 | 4.0 | 8.0 | C | 2 | m7 | 3 |
| m3 V65 | 8.0 | 12.0 | C | 5 | D7 | 1 |
| m4 I | 12.0 | 16.0 | C | 1 | M | 0 |
| m5 vi6 | 16.0 | 20.0 | C | 6 | m | 1 |
| m6 G: V42 | 20.0 | 24.0 | G | 5 | D7 | 3 |
| m7 I6 | 24.0 | 28.0 | G | 1 | M | 1 |
| m8 IV42 | 28.0 | 32.0 | G | 4 | M7 | 3 |
| m9 ii7 | 32.0 | 36.0 | G | 2 | m7 | 0 |
| m10 V7 | 36.0 | 40.0 | G | 5 | D7 | 0 |
| m11 I | 40.0 | 44.0 | G | 1 | M | 0 |

**Note on what this table shows about the format:** every span is exactly 4.0 quarter notes, one per
measure, and every `End` equals the next row's `Start` — so the representation is a contiguous tiling with
no gaps, which is what §3.2's gap-filling rule exists to guarantee.

### §5.4 Table 4, transcribed — input vector dimensions

Caption, quoted: *"Total dimension of input vector for each pitch encoding option (limited to 7 octaves and
double sharps/flats)."*

| | |
|---|---|
| Chromatic pitch, full (CPf) — 7 × 12 = 84 | Pitch spelling, full (PSf) — 7 × 35 = 245 |
| CP class + bass (CPb) — 12 + 12 = 24 | PS class + bass (PSb) — 35 + 35 = 70 |
| CP class (CPc) — 12 | PS class (PSc) — 35 |

### §5.5 Table 5, transcribed — the headline comparison

Caption, quoted whole: *"Comparison of the percent accuracy between models. The two rows above the internal
division report on our best model – ConvGRU with pitch spelling and bass (PSb) and with global training. The
first row reports on training with all available data; the second reduces the available data to the smaller
corpus used by Chen and Su (2018). Rows below the internal dividing line provide comparison data for the
performance of Chen and Su (2018, 2019), as well as a baseline key detection using pitch profiles by
Temperley (1999). 'Degree' registers as correct only when the predictions match the corpus entry for both
Degrees 1 and 2; 'RN' is correct only when all four of the previous columns match in that way."*

| | Key | Degree | Quality | Inversion | RN |
|---|---|---|---|---|---|
| **ConvGRU + PSb + global (all data)** | **82.9** | **68.3** | **76.6** | **72.0** | **42.8** |
| ConvGRU + PSb + global | 80.6 | 66.5 | 76.3 | 68.1 | 39.1 |
| *— internal dividing line —* | | | | | |
| Chen and Su (2019) | 78.4 | 65.1 | 74.6 | 62.1 | *(blank)* |
| Chen and Su (2018) | 66.7 | 51.8 | 60.6 | 59.1 | 25.7 |
| Local model after Temperley (1999) | 67.0 | *(blank)* | *(blank)* | *(blank)* | *(blank)* |

**★ TWO CELLS ARE BLANK AND THIS READ MET NO ACCOUNT OF WHY.** Chen and Su (2019) carries no RN value, and
the Temperley (1999) baseline carries only a Key value. **The caption accounts for neither, and this read
met no account of either elsewhere in the pages as read.** A later reader must not take a blank for a zero
or for a value withheld.

**★ AND THE TWO COMPARISONS IN THIS TABLE ARE NOT LIKE FOR LIKE IN THE SAME WAY.** The row that is
comparable with Chen and Su is the **second** — *"ConvGRU + PSb + global"* on their smaller corpus, **39.1
RN** — while the number the paper's own abstract and §5.1 carry forward is the **first**, **42.8**, trained
on all data. **The paper states this in its caption and does not restate it where the figure is used.**

### §5.6 Table 6, transcribed — the four averaged axes

Caption, quoted whole: *"Results obtained by averaging the accuracy of several models on four different
axes: architecture, input registral information, input spelling, and global/local training. Column labels
are the same as for Table 5, and the first row likewise relates once again to the best performing model. Each
sub-table thereafter shows the average performance of several models. For example, the ConvGRU row shows the
average of 12 models with the same architecture row but using different input representations and registral
information. The values in the first row of each sub-table represent the percentage accuracy of the
corresponding averaged models as a reference; each line thereafter shows the +/− difference in accuracy from
the reference. There are only 6 PoolGRU models, as they can be trained only globally (not locally)."*

| | *n* | Key | Degree | Quality | Inversion | RN |
|---|---|---|---|---|---|---|
| **ConvGRU + PSb + global** | | **82.9** | **68.3** | **76.6** | **72.0** | **42.8** |
| ConvGRU | 12 | **81.9** | **67.4** | **74.6** | **67.9** | **37.8** |
| ConvDil | 12 | −2.4 | −1.8 | −0.8 | −0.5 | −1.7 |
| PoolGRU | 6 | −2.3 | −3.0 | −1.6 | −1.8 | −4.1 |
| bass | 10 | **80.8** | **66.6** | **74.3** | **70.1** | **39.2** |
| full | 10 | −0.7 | −0.9 | −0.6 | −3.5 | −3.7 |
| class | 10 | −0.1 | −0.7 | −0.1 | −4.7 | −4.7 |
| spelling | 15 | **80.6** | **66.2** | **74.1** | **67.6** | **36.5** |
| chromatic | 15 | −0.3 | −0.3 | −0.2 | −0.5 | −0.4 |
| global | 15 | 80.6 | **66.8** | **75.4** | 66.7 | 36.9 |
| local | 15 | **+0.3** | −0.7 | −2.4 | **+2.0** | **+0.2** |

*(The bold in the source marks the better of each pair; it is reproduced here as printed and carries no
meaning this read adds.)*

**The reference rows are absolute percentages; every row beneath a reference row is a signed difference from
it.** So, for example, the ConvDil Key figure is not −2.4 % accuracy but 81.9 − 2.4 = 79.5.

### §5.7 Table 7, transcribed — corpus against system output on the Bach prelude

Caption, quoted: *"A comparison between the corpus analysis (left, reproducing Table 3) and our system's
output (right). Discrepancies between the input and output analyses are highlighted in italics."*

*Italicised cells — the paper's own marking of a discrepancy — are marked with \* here.*

| RN | Corpus: Start–End, Key, Degree, Quality, Inv. | Output: Start–End, Key, Degree, Quality, Inv. |
|---|---|---|
| m1 C: I | 0.0–4.0, C, 1, M, 0 | 0.0–4.0, C, 1, M, 0 |
| m2 ii42 | 4.0–8.0, C, 2, m7, 3 | 4.0–4.5, C, 2, m7, \*0\* · 4.5–7.0, C, 2, m7, \*1\* · 7.0–7.5, C, 2, \*D7\*, \*0\* · 7.5–8.0, C, \*5\*, \*D7\*, \*0\* |
| m3 V65 | 8.0–12.0, C, 5, D7, 1 | 8.0–8.5, C, 5, D7, 1 · 8.5–9.5, C, 5, \*M\*, 1 · 9.5–10.0, C, 5, D7, 1 · 10.0–11.0, C, 5, \*M\*, 1 · 11.0–12.0, C, 5, D7, 1 |
| m4 I | 12.0–16.0, C, 1, M, 0 | 12.0–16.0, C, 1, M, 0 |
| m5 vi6 | 16.0–20.0, C, 6, m, 1 | 16.0–16.5, C, \*1\*, m, \*0\* · 16.5–17.0, C, 6, m, \*0\* · 17.0–20.0, C, 6, m, 1 |

**What the table exhibits, stated at the table and not beyond it:** of the corpus's five one-measure spans,
**two are reproduced exactly** (m1 and m4) and **three are fragmented into three, four or five output spans
each**; every fragmentation keeps the Key correct; the Degree is wrong on two fragments; the Quality
oscillates within m3 between D7 and M across five fragments of one corpus span. **This is the paper's own
exhibit for error class 1, segmentation**, and it is the one place in the pages as read where that
behaviour is shown rather than described.

### §5.8 Figures 4 and 5, as read — and what this read declines to transcribe

**Figure 4** is a bar chart. Its x-axis is labelled *"number of transpositions"* and runs from **3 to 15**;
its y-axis is labelled *"number of pieces transposed"* and its gridlines are at 0, 10, 20, 30, 40 and 50.
**The tallest bar stands at 12.** **★ NO BAR CARRIES A PRINTED VALUE, SO NO PER-BAR COUNT IS TRANSCRIBED
HERE AND NONE IS DERIVED.** Reading heights off an unlabelled chart would produce numbers that look like
transcriptions and are not, and the paper's own prose already states the range (3 to 15) and the bulk
(10–13).

**Figure 5** is the architecture diagram, and its printed numbers ARE transcribable because they are
printed as text inside the boxes:

- **Conv — 33k weights** *or* **Pool — no weights** (short-range);
- **GRU — 43k weights** *or* **Dil — 46k weights** (long-range);
- **Fully connected — 8k weights (GRU) / 4k weights (Dil)**;
- **Outputs, with their class counts:** Quality **12**, Inversion **4**, Root **35**, Key **30**, Degree 1
  **21**, Degree 2 **21**.

Caption, quoted: *"Architecture of the neural network model in the 'local' training mode. When 'global',
Quality/Inversion/Root outputs are computed after the fully connected layer instead. The numbers in the
boxes refer to the number of categories for each output label in the PSb case (see Table 4)."*

### §5.9 The protocol constants, as the paper states them

| Constant | Value | Where |
|---|---|---|
| Input frame | 32nd note | §3.2, *Time* |
| Output frame | 8th note | §3.2, *Time* |
| Local window | 2 quarter notes | §3.4 |
| Training segment | 80 quarter notes, non-overlapping | §3.4 |
| Dilated convolution | 4 layers, 64 kernels, kernel size 3, dilation 3ˡ | §3.4 |
| Dilated context | 3⁴ = 81 eighth notes (40 past, present, 40 future) | §3.4 |
| GRU hidden state | 64 neurons per direction | §3.4 |
| GRU dropout | 0.3 | §3.4 |
| Final fully connected layer | 64 neurons | §3.4 |
| Loss | categorical cross-entropy, per label, summed with equal weighting | §3.4 |
| Train / validation split | 90 % / 10 %, applied per corpus as well as overall | §3.5 |
| Pitch limits | F♭♭ to B♯♯ | §3.3 |
| Key limits | C♭ to C♯ major and relative minors A♭ to A♯ | §3.3 |
| Best model weights | ≈ 94,000 total: 33,000 local, 43,000 global, 18,000 fully connected | §3.5 |
| Training time | 20 minutes to 3 hours, CPU-only HPC server | §3.5 |
| Software | Python 3.7, Tensorflow 1.14 | §3.5 |

### §5.10 The reference list, transcribed

Given in the printed order, compressed to author(s), year, title, venue. **DOIs and URLs printed in the list
are not reproduced.**

Briot, Hadjeres & Pachet 2020, *Deep Learning Techniques for Music Generation*, Springer · Chen & Su 2018,
functional harmony recognition with multi-task RNNs, ISMIR 2018 · Chen & Su 2019, Harmony Transformer, ISMIR
2019 · Cho, van Merriënboer, Gulcehre, Bahdanau, Bougares, Schwenk & Bengio 2014, RNN encoder–decoder,
arXiv:1406.1078 · Clendinning & Marvin 2016, *The Musician's Guide to Theory and Analysis*, 3rd edn ·
Cohn 1999, "As wonderful as star clusters", *19th-Century Music* 22(3) · Cohn 2012, *Audacious Euphony*, OUP ·
Cross 1997, "Pitch schemata", in Deliège & Sloboda (eds.) · Cuthbert & Ariza 2010, music21, ISMIR 2010 ·
de Clercq & Temperley 2011, corpus analysis of rock harmony, *Popular Music* 30(1) · De Haas, Rohrmeier,
Veltkamp & Wiering 2009, generative grammar of tonal harmony, ISMIR 2009 · Devaney, Arthur, Condit-Schultz &
Nisula 2015, TAVERN, ISMIR 2015 · Duinker 2019, plateau loops and hybrid tonics, *MTO* 25(4) · Euler 1739,
*Tentamen Novae Theoriae Musicae* · Giraud, Groult & Leguy 2018, Dezrann, TENOR 2018 · Hadjeres, Pachet &
Nielsen 2017, DeepBach, ICML 2017 · Harasim, Rohrmeier & O'Donnell 2018, generalized parsing framework,
ISMIR 2018 · Heinichen 1711, *Neu erfundene und gründliche Anweisung* · Holtzman 1977, a program for key
determination, *Interface* 6 · Huang, Vaswani, Uszkoreit, Shazeer, Simon, Hawthorne, Dai, Hoffman,
Dinculescu & Eck 2018, Music Transformer, arXiv · Huang, Liu, van der Maaten & Weinberger 2016, densely
connected convolutional networks, arXiv · Illescas, Rizo & Iñesta 2007, harmonic, melodic and functional
automatic analysis, ICMC 2007 · Ju, Condit-Schultz, Arthur & Fujinaga 2017, non-chord tone identification
with deep neural networks, DLfM 2017 · Ju, Howes, McKay, Condit-Schultz, Calvo-Zaragoza & Fujinaga 2019,
interactive workflow for chord labels, ISMIR 2019 · Krumhansl & Kessler 1982, tracing dynamic changes in
perceived tonal organisation, *Psychological Review* 89(2) · Kröger, Passos & Sampaio 2008, Rameau, ICMC
2008 · Laitz 2016, *The Complete Musician*, 4th edn · Lerdahl & Jackendoff 1983, *A Generative Theory of
Tonal Music* · Lewin 1987, *Generalized Musical Intervals and Transformations* · Liang, Gotham, Johnson &
Shotton 2017, BachBot, ISMIR 2017 · Madsen & Widmer 2007, key-finding with interval profiles, ICMC 2007 ·
McFee & Bello 2017, structured training for large-vocabulary chord recognition, ISMIR 2017 · Nápoles López,
Arthur & Fujinaga 2019, key-finding based on a hidden Markov model and key profiles, DLfM 2019 · Neuwirth,
Harasim, Moss & Rohrmeier 2018, the annotated Beethoven corpus, *Frontiers in Digital Humanities* 5 ·
Oettingen 1866, *Harmoniesystem in dualer Entwicklung* · Oord, Dieleman, Zen, Simonyan, Vinyals, Graves,
Kalchbrenner, Senior & Kavukcuoglu 2016, WaveNet, arXiv · Oore, Simon, Dieleman, Eck & Simonyan 2018, this
time with feeling, *Neural Computing and Applications* · Paiement, Eck & Bengio 2005, a probabilistic model
for chord progressions, ISMIR 2005 · Pardo & Birmingham 2002, algorithms for chordal analysis, *CMJ* 26(2) ·
Robine, Rocher & Hanna 2008, improvements of key-finding methods, ICMC 2008 · Rocher, Robine, Hanna &
Strandh 2009, dynamic chord analysis for symbolic music, ICMC 2009 · Rohrmeier 2011, towards a generative
syntax of tonal harmony, *JMM* 5(1) · Sapp 2005, visual hierarchical key analysis, *Computers in
Entertainment* 3(4) · Schenker 1935, *Der freie Satz* · Schoenberg, *Structural Functions of Harmony*,
Williams and Norgate *(the year field as printed is transcribed at §7.1, item 5)* · Steedman &
Longuet-Higgins 1971, on interpreting Bach, *Machine Intelligence* 6 · Temperley 1997, an algorithm for
harmonic analysis, *Music Perception* 15(1) · Temperley 1999, what's key for key?, *Music Perception* 17(1) ·
Tymoczko 2011, *A Geometry of Music*, OUP · Tymoczko, Gotham, Cuthbert & Ariza 2019, the RomanText format,
ISMIR 2019 · Yu & Koltun 2015, multi-scale context aggregation by dilated convolutions, arXiv.

**THE BOUND ON THIS TRANSCRIPTION:** it is this read's enumeration of the printed list across PDF pages
11–13, and it comes to **fifty-one entries**. That count is derived by counting the entries written above,
not read off anything the paper prints — **the paper prints no count of its own references** — so it is
this read's count and a miscount is possible.

### §5.11 The two named error cases, as the paper describes them

*(Added at the read-back, which found §5 carried the error CLASSES without the two cases the paper works
through. §8.2 records the addition.)*

**The Schubert case**, §4.2, printed page 50, quoted: *"Once again, the extract from Schubert's
'Einsamkeit' (discussed in Section 2 and shown in Figure 3) offers a neat example of all three issues. Our
reference analysis corresponds broadly to analysis A2. Regarding issue 1, the prediction for measures 34 and
35 is made of four different chord labels, while in the reference dataset there are only two. This is
strictly connected to issue 2, as the 'mis'-labeled chord is a German sixth, unidentified by our system.
Lastly, 'the different but acceptable' reading is pertinent in the case of measures 36 and following, which
the dataset analyses in terms of G minor, the system views in G major, and is in fact an ambiguous mixture
of the two (as discussed in Section 2)."*

**★ NOTE WHAT THAT SAYS ABOUT THE PAPER'S OWN §2.** §2's Table 2 offers A1, A2 and A3 as three readings of
the same two measures; §4.2 states that **the reference analysis corresponds broadly to A2** — the reading
Table 2 records as breaking rule 1 while following rules 3 and 2. **So the corpus the system is graded
against is, at this passage, the reading the paper's own rule 1 argues against**, and the paper does not
draw that out.

**The Beethoven case**, §4.2, printed page 50, quoted: *"Finally, we found some cases we consider
unacceptable readings, where the most compelling musical reading diverges from the statistically normative
case. For example, in Beethoven's sixth sonata (op.10 no.2, Figure 6), the exposition includes a theme in C
major which from measure 41 is repeated in the parallel key of C minor. Perhaps because this lasts for only
four measures, the system is reluctant to identify a full modulation, preferring instead to remain in C
major."* Figure 6's caption reads *"Beethoven's piano sonata no.6, m.40–43."*

**★ THIS IS A FOURTH CLASS AND THE PAPER DOES NOT NUMBER IT.** §4.2 sets out three numbered classes and
then adds this one in prose, calling it **unacceptable** rather than an alternative reading — the
distinction being that the system's answer is statistically normative and musically wrong. **`[FACT]`** that
the paper draws the distinction; **`[CONJECTURE]`** for the *"Perhaps because"* explanation, which the paper
marks as a guess itself.

---

## §6 — Arithmetic this read performed on the paper's own printed values

**Nothing in this section is a value taken from the paper; everything is a computation over values that are.
Where a computation disagrees with a printed total, the disagreement is reported and no printed value is
altered.**

### §6.1 ★ TABLE 1's QUARTER-LENGTH COLUMN DOES NOT SUM TO ITS OWN PRINTED TOTAL, BY TEN

The six printed row values, added in the printed order:

7 712 + 12 840 = 20 552 · + 48 811 = 69 363 · + 30 992 = 100 355 · + 3 168 = 103 523 · + 8 326 = **111 849**

**The printed total is 111 859.** The difference is **10**, and the computed sum is the smaller.

**WHAT THIS IS AND IS NOT.** It is a **defect of the paper**, not of either extract of it. **It moves no
result this read met**: the quarter-length column is a size statistic of the corpus, and no accuracy,
comparison or conclusion met in the pages as read rests on it. **Nothing is proposed.** The other two
numeric columns and the score count all close exactly (§6.2), so this is one column of four and not a
general failure of the table.

### §6.2 Table 1's other columns close exactly

- **Measures:** 2 773 + 5 128 + 15 881 + 9 420 + 819 + 2 791 = **36 812**, the printed total. ✔
- **RNs:** 8 779 + 15 959 + 29 652 + 11 337 + 2 165 + 5 283 = **73 175**, the printed total. ✔ It is also
  consistent with §3.1's prose, *"over 70,000 RN annotations"*.
- **Scores:** the *Movements or equivalent* column names 10 + 17 theme-and-variations sets, 70 movements, 32
  first movements, 24 preludes and 48 songs = **201**, the printed total. ✔ *(This takes ABC's contribution
  as its 70 movements rather than its 16 quartets; taking the 16 instead gives 147, so 70 is the reading on
  which the column closes.)*

### §6.3 The sum-against-product argument closes at Figure 5's own class counts

Figure 5 prints the six class counts for the PSb case: Quality 12, Inversion 4, Root 35, Key 30, Degree 1
21, Degree 2 21.

- **Σᵢcᵢ** = 12 + 4 + 35 + 30 + 21 + 21 = **123**, which is the number §3.2 prints. ✔
- **∏ᵢcᵢ** = 12 × 4 × 35 × 30 × 21 × 21 = **22 226 400**, which is **≈ 22·10⁶**, the value §3.2 prints. ✔

**So the paper's own headline argument for the six-way split is arithmetically exact at its own figure**, and
this read establishes that rather than relaying it.

### §6.4 The 35 spellings and the 30 keys close against the stated limits

- **35 spellings.** Seven letter names × five accidental states (♭♭, ♭, ♮, ♯, ♯♯) = 35, and the stated range
  **F♭♭ to B♯♯** is exactly those 35 positions on the line of fifths, endpoints included. ✔ Table 4's PSf
  entry, 7 × 35 = 245, and its PSb entry, 35 + 35 = 70, both follow. ✔
- **30 keys.** Majors from **C♭ to C♯** on the line of fifths are C♭, G♭, D♭, A♭, E♭, B♭, F, C, G, D, A, E,
  B, F♯, C♯ — **fifteen**; their relative minors from **A♭ to A♯** are A♭, E♭, B♭, F, C, G, D, A, E, B, F♯,
  C♯, G♯, D♯, A♯ — **fifteen**. Total **30**, which is exactly Figure 5's Key box. ✔ **This is what
  reconciles §3.2's "70 keys" with the architecture's 30, and footnote 15's forward pointer is the one
  place this read met the paper connecting them.**
- **24 keys in the CP case** = 12 major + 12 minor, as §3.2 states. ✔

### §6.5 The Schubert transposition example closes in both directions

Numbering the line of fifths F♭♭ = 1 … B♯♯ = 35: **E♭ = 13** and **E♯ = 27**.

- Flatward room: 13 − 1 = **12 steps**, which is the paper's *"12 further steps in the flat direction"*. ✔
- Sharpward room: 35 − 27 = **8 steps**, which is the paper's *"8 steps sharpwards"*. ✔

And for the key constraint, numbering the same way: **B minor = 21**, against the minor limit **A♯ = 26** →
**5 steps**, the paper's figure ✔; **C minor = 16**, against the minor limit **A♭ = 12** → **4 steps**, the
paper's figure ✔.

**So all four of the example's numbers are exact.** *(And the sentence's own labels are right too: it calls
B minor the **sharp-most** key used and C minor the **flatmost**, which is the correct way round. This
read's first writing asserted the opposite and struck it at the read-back — §8.2, item 1.)*

### §6.6 The dilated convolution's context closes, and the layer index must start at zero

*"4 layers with 64 kernels each of size 3 and a dilation of 3ˡ"*, giving *"a total context of 3⁴ = 81 eighth
notes: the present one as well as 40 from the past and 40 from the future."*

- 3⁴ = **81** ✔ and 1 + 40 + 40 = **81** ✔.
- The receptive field of four kernel-size-3 layers with dilations 3⁰, 3¹, 3², 3³ is 1 + 2(1 + 3 + 9 + 27) =
  1 + 2(40) = **81**. ✔ **So the context closes only if the layer index l runs 0 to 3**; if it ran 1 to 4
  the field would be 1 + 2(3 + 9 + 27 + 81) = 241. **The paper does not say where l starts**, and 81 is what
  it prints, so l starts at 0. Derived here, not stated there.
- **A second thing follows from the same sentence and the paper does not draw it:** 40 eighth notes is **20
  quarter notes** in each direction, against a training segment of **80 quarter notes** (§3.4). So the
  dilated arm's context is a quarter of the segment on each side, while the GRU arm's is the whole segment —
  which is the concrete content of the expressiveness difference §3.4 argues in words.

### §6.7 The weight decomposition closes in the text and does NOT close against Figure 5

- §3.5's own decomposition: 33 000 + 43 000 + 18 000 = **94 000**, the total it states. ✔
- **★ BUT FIGURE 5 PRINTS "Fully connected — 8k weights" FOR THE GRU CASE, WHERE §3.5 SAYS 18 000 REMAIN
  FOR THE FULLY CONNECTED LAYERS.** The figure's local and global boxes agree with the text's 33k and 43k;
  only the fully connected figure differs, and **this read met no reconciliation of the two numbers in the
  pages as read.** *(NOT
  CLAIMED: that either number is wrong. A reading on which both stand — the figure's box counting one layer
  and the text counting that layer together with the six per-label output layers — is available, and **the
  paper does not state it**, so this read does not assert it.)*

### §6.8 ★ THREE OF TABLE 6's FOUR AXES PARTITION THE SAME THIRTY MODELS; THE FOURTH CANNOT

The model population is stated at §4.1: *"we have trained on all possible combinations of the six pitch
encodings, the two architectures (and the baseline), and the two training types (except for PoolGRU, which
is only applicable for global training)."* That gives 6 × 2 × 2 = 24 ConvGRU and ConvDil models, plus 6
PoolGRU models, **thirty in all**.

- **Architecture axis:** 12 + 12 + 6 = **30** ✔, and the caption's *"There are only 6 PoolGRU models"* is
  exactly this.
- **Registral axis:** each encoding appears in 30 ÷ 6 = 5 models, and each registral class covers 2 of the 6
  encodings, so 2 × 5 = **10** per class; 10 + 10 + 10 = **30** ✔, matching the printed 10, 10, 10.
- **Spelling axis:** 3 encodings per class × 5 = **15** per class; 15 + 15 = **30** ✔, matching the printed
  15, 15.
- **★ TRAINING AXIS — THE PRINTED COUNTS ARE 15 AND 15, AND NO READING OF THE POPULATION GIVES THAT.** If
  the six PoolGRU models are included, global holds 6 + 6 + 6 = **18** and local 6 + 6 = **12**. If they are
  excluded, it is **12** and **12**. **Halving thirty gives fifteen and fifteen, and this read can
  construct no other route to those two numbers** — and halving is what the caption's own sentence forbids,
  since it says in terms that PoolGRU trains only globally.

**WHAT THIS IS.** A **defect of the paper**, in the counts column of one sub-table. **It does not move a
measured value**: the accuracies in those two rows are averages whose denominators are not printed, so what
is in doubt is how many models each average is over, not any figure the paper concludes from. **The paper's
own conclusion from that sub-table is that the difference is not significant**, which is the weakest
conclusion this read met it drawing, and this read met nothing else in the pages as read that leans on that
sub-table. **Nothing is proposed.**

### §6.9 The pagination closes against the tool

Printed pages 42 to 54 inclusive is **13 pages**, which is the count the tool returned. ✔

### §6.10 What the "small but significant improvement" is, at the cells

The comparison the caption says is like-for-like is the **second** row of Table 5 — the same model trained on
Chen and Su's smaller corpus — against the rows below the dividing line. Subtracting at the cells:

| Against | Key | Degree | Quality | Inversion | RN |
|---|---|---|---|---|---|
| Chen and Su (2019) | +2.2 | +1.4 | +1.7 | +6.0 | *not comparable — no RN value printed* |
| Chen and Su (2018) | +13.9 | +14.7 | +15.7 | +9.0 | +13.4 |
| Temperley (1999) baseline | +13.6 | — | — | — | — |

**★ SO THE GAIN OVER THE MOST RECENT PRIOR SYSTEM IS BETWEEN 1.4 AND 6.0 POINTS, AND ON THE FULL TASK IT
CANNOT BE COMPUTED AT ALL**, because Table 5 prints no RN figure for Chen and Su (2019). *"Small but
significant"* is therefore an accurate description of what is comparable, **and the headline 42.8 is not a
figure any row BELOW the dividing line can be differenced against** — it is the all-data row, and every comparison row
is on the smaller corpus.

### §6.11 Table 7's corpus column reproduces Table 3 exactly

All five rows of Table 7's left half — m1 to m5 — agree cell for cell with the first five rows of Table 3,
in start, end, key, degree, quality and inversion. ✔ Checked at the two tables, not assumed from the
caption's *"reproducing Table 3"*.

### §6.12 Table 3 tiles its span with no gap and no overlap

Every row's End equals the next row's Start, from 0.0 to 44.0 across eleven spans of 4.0 each: 11 × 4.0 =
**44.0**. ✔ The representation is a contiguous tiling, which is what §3.2's gap-filling rule guarantees for
the general case.

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

**None of these moves a result of the paper, and nothing is proposed about any of them.** They are recorded
because a later reader who carries a figure out of this paper needs to know which of its statements its own
pages refute.

1. **★ TABLE 1's QUARTER-LENGTH COLUMN IS TEN SHORT OF ITS OWN PRINTED TOTAL** (§6.1). The other two numeric
   columns and the score count close exactly.
2. **★ TABLE 6's TRAINING-AXIS COUNTS, 15 AND 15, ARE UNREACHABLE FROM THE POPULATION THE SAME CAPTION
   DESCRIBES** (§6.8). Global is 18 and local 12 if PoolGRU is in; 12 and 12 if it is out.
3. **★ STRUCK AT THE READ-BACK — THIS ITEM WAS THIS READ'S OWN ERROR AND NOT THE PAPER'S. FORMER WORDING,
   PRESERVED (#12):** "**§3.3 APPEARS TO EXCHANGE THE LABELS 'FLATTEST' AND 'SHARP-MOST' ON ITS OWN WORKED
   EXAMPLE.** The sentence names **B minor** and **C minor** as the extremes of the Schubert example's key
   range. B minor carries two sharps and sits at 21 on the line of fifths; C minor carries three flats and
   sits at 16. **So B minor is the sharper of the two and C minor the flatter**, and the step counts the
   sentence gives — 5 to the sharp limit for B minor, 4 to the flat limit for C minor (§6.5) — are each
   correct only for the opposite label to the one attached."
   **WHAT THE PAGE ACTUALLY PRINTS**, read a second time at printed page 48: *"In the Schubert example, by
   whatever reading, the sharp-most key used is B minor (5 steps away from the limit of A♯ on the spiral of
   fifths), and the flatmost key is C minor (4 steps away from A♭)."* **B minor is called sharp-most and C
   minor flatmost, which is right**; both labels and both step counts are correct. **The error was this
   side's, in the first writing, and it is recorded rather than quietly removed** (§8.2, item 1).
4. **★ FIGURE 5's "8k" AND §3.5's "18,000" DESCRIBE THE SAME FULLY CONNECTED LAYERS AND DIFFER**, and the
   this read met no reconciliation of them in the pages as read (§6.7).
5. **★ THE SCHOENBERG REFERENCE CARRIES TWO YEARS IN ONE FIELD, AND THE IN-TEXT CITATION USES THE OTHER
   ONE.** The reference list prints, at printed page 53: *"Schoenberg, A. (1954 – op.posth, published
   1948). Structural Functions of Harmony. Williams and Norgate, London."* The only citation of it in the
   text is **footnote 17**, at printed page 52, which prints *"Schoenberg (1948)"*. **So the list sorts the
   work under 1954 and the text cites it as 1948**, and a reader matching citation to entry by year finds
   no match. Both pages were read a second time at the read-back. **No value of the paper moves.**
6. **FOOTNOTE 17's PARENTHESES DO NOT BALANCE AS PRINTED**: *"For historical examples, see (Heinichen
   (1711); Euler (1739); Oettingen (1866); Schoenberg (1948); and for more models, see (Lewin (1987); Cross
   (1997); Cohn (1999); Cohn (2012))."* Two opening parentheses and one closing at the outer level. A
   typographic fault, recorded because this line records them, and it changes no reading.
7. **TABLE 5 CARRIES TWO UNEXPLAINED BLANKS** — no RN figure for Chen and Su (2019), and only a Key figure
   for the Temperley baseline. The caption accounts for neither, and this read met no account of either in
   the pages as read (§5.5). **The 2019 blank is the one with a consequence**, because it is what makes the
   full-task comparison against the most recent prior system impossible (§6.10).
8. **TABLE 2 GIVES ANALYSES A1 AND A3 IDENTICAL RULE VERDICTS** while they differ in their reading (§5.2).
   The paper's argument is that the rules underdetermine the analysis, and this is a sharper instance of it
   than the prose claims — **and the surrounding prose does not point it out**, so a reader could take the
   table as distinguishing three analyses where on its rule columns it distinguishes two.
9. **THE PAPER USES "SIX" FOR TWO DIFFERENT SETS** — the tabular format's six properties and the network's
   six output labels — **which differ in three of six members** (§2.3). **This read met no sentence in the
   pages as read that sets the two side by side.**
10. **§4.2's RANKING OF THE ERROR CLASSES CARRIES NO COUNT.** *"This appears to be the most common
    discrepancy"* is the whole of its support in the pages as read; no per-class rate, count or population
    is printed in them.

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered

- **The rate of self-contradictory outputs.** §3.2 says it is *"only rarely a problem"*. **No rate, count or
  population was met in the thirteen pages as read** (§2.6).
- **The size of any of the three error classes** (§4.2), including the one called most common.
- **The quantisation error accepted for triplets and sub-32nd values** (§3.2). Named, accepted, unmeasured.
- **The cost of not distinguishing tied from repeated notes** (§3.2). An expectation, unmeasured.
- **The metrical-strength result.** §5.1 reports that *"informal testing of metrical strength did not yield
  significant gains"* — **with no protocol, no figure, no population and no definition of the feature
  tested.** It is a reported negative with nothing behind it that a reader can check.
- **Uncertainty on the headline figures.** Tables 5 and 7 print single values with no interval, no repeated
  runs and no seed variance. *(What the paper DOES report is significance testing on the averaged axes of
  Table 6 — p < 10⁻² for architecture and for bass, p < 10⁻⁶ for the quality label across training modes.
  So the axis comparisons carry a test and the headline accuracies do not.)*
- **How many pieces the key constraint excludes.** §3.3 asserts that *"real pieces very rarely go outside
  these key boundaries"*; Figure 4 shows how many transpositions survive, **not how many pieces were
  dropped or truncated**, and no such count is printed.
- **Any per-corpus accuracy.** Table 1 gives per-corpus sizes; Tables 5 and 6 give no per-corpus breakdown,
  so nothing in the paper says whether the result is carried by one of the four datasets.
- **The size of the validation set in scores.** The split is stated as 90/10 per corpus, by score; **no
  count of validation scores, measures, frames or RNs is printed.**
- **★ AND WHAT SEPARATES MODEL SELECTION FROM EVALUATION — NOTHING DOES.** With no third partition, the
  comparison across the six pitch encodings, the two architectures and the two training modes was made on
  **the same data every headline figure is reported over**. So the thirty-model comparison of Table 6 and
  the accuracies of Table 5 share a population. *(ADOPTED AT THE CROSS-CHECK FROM ROW 45's FIRST EXTRACT,
  which states this point where this file had recorded only the absence of a test set. §9.4, item 2. **NOT
  claimed: that any figure is thereby wrong** — what is stated is what the design does and does not
  separate.)*
- **Any segmentation measure.** Segmentation is named as the most common error class and **no boundary
  metric of any kind is defined or reported** — the six labels are scored frame-wise and that is all.
- **Inter-annotator agreement.** Named as desirable at §3.1 and at footnote 12; **this read met no
  measurement of it in the pages as read.**

### §7.3 What is both measured and structural here

Four things in this paper are measured on its own corpus AND are about the shape of the problem rather than
about one system's tuning. They are listed because that is the class a detail specification could cite.

1. **★ A TWO-VECTOR ENCODING THAT SEPARATES THE LOWEST SOUNDING NOTE BEATS BOTH FULL REGISTRAL INFORMATION
   AND BARE PITCH CLASS — ON EVERY COLUMN, NOT ONLY ON INVERSION.** Table 6's registral sub-table: *bass* is
   the reference at 80.8 / 66.6 / 74.3 / 70.1 / 39.2, and both *full* (−0.7 / −0.9 / −0.6 / −3.5 / −3.7) and
   *class* (−0.1 / −0.7 / −0.1 / −4.7 / −4.7) sit below it everywhere. §4.1 attaches p < 10⁻² to it. **The
   structural content: what helps is not more registral detail but the separation of the bass as its own
   channel**, and the paper's own caveat is that its "bass" is merely the lowest sounding note (§2.5).
2. **★ LOCAL CONTEXT ANALYSIS PAYS, AND THE MEASURED SIZE IS ON THE FULL TASK.** ConvGRU against PoolGRU —
   the same recurrent global part with and without the convolutional local part — is **−4.1 RN points**, the
   largest single movement in Table 6's architecture sub-table, with p < 10⁻² reported for exactly that
   comparison. **The structural content: a global sequence model alone does not recover what a local
   harmonic reduction supplies.**
3. **★ SPELLING IS NOT A GAIN; IT IS A HARDER TASK PERFORMED NO WORSE — AND THE PAPER'S OWN ARGUMENT IS
   THAT THIS IS THE STRONGER RESULT.** Table 6's spelling sub-table gives *chromatic* as −0.3 / −0.3 / −0.2
   / −0.5 / −0.4 against *spelling*, and §4.1 states the difference is **not statistically significant**.
   The paper's argument, quoted at C22, is that spelling enlarges the label space — 35 roots and 30 keys
   against 12 and 24 — **so equal accuracy over more classes is not equal performance.** **This is an
   argument, not a measurement, and the paper presents it as one.**
4. **★ THE TRAINING MODE TRADES BETWEEN LABELS RATHER THAN DOMINATING.** Table 6's last sub-table: against
   *global*, *local* is **+0.3 Key, −0.7 Degree, −2.4 Quality, +2.0 Inversion, +0.2 RN**. The total
   difference is declared not significant; the per-label differences on the intermediate labels are declared
   significant at p < 10⁻⁶. **The structural content: where in the network a label is decided changes which
   labels are decided well, and the aggregate hides it** — which is the same shape as the paper's own
   complaint about right/wrong accuracy at §5.1.

**And one thing that is exhibited rather than measured, worth as much:** **Table 7 shows the failure mode of
a frame-wise label with no segmentation object** — three of five corpus spans fragmented into three, four
and five pieces, with the quality oscillating inside a single correct harmony (§5.7). **The paper's
proposed remedy is someone else's segmenter layer** (Chen and Su, 2019), named at §4.2 and not built here.

### §7.4 What this paper's reference list gives the record, checked at the candidacy file

**The check that was run, stated exactly:** the names in this paper's reference list (§5.10) were searched
against `reading_pass/candidacy_upgrades.md` with one targeted search over a name list this read chose.
**That is not an exhaustive cross-check of fifty-one references against every row of that file**, and no
claim of completeness is made.

**What the search established at that file's own lines:**

- **★ THIS PAPER REACHES AN ADMITTED-BUT-NOT-HELD ROW — AND BOTH READS FOUND IT INDEPENDENTLY.** Row 6 of the
  candidacy file is **Temperley, *Music Perception* 17(1) 1999, "What's Key for Key?"**, marked **ADMITTED**
  with the held column reading **—** and the reason *"A key-finding model. **Paywalled and not held.**"*
  **This paper cites Temperley (1999) and reports a baseline built after it** — Table 5's *"Local model
  after Temperley (1999)"*, Key **67.0** on this paper's own corpus.
  *(★ NARROWED AT THE CROSS-CHECK. FORMER WORDING, PRESERVED (#12): "**★ THE ONE FINDING OF THIS
  SUBSECTION: THIS PAPER REACHES AN ADMITTED-BUT-NOT-HELD ROW.**" — **row 45's first extract reaches the
  same finding, as its own finding (8)**, so a heading that reads as a claim of novelty is refuted by the
  doubling. §9.2 and §9.3.)*
  **THE BOUND, WHICH MATTERS MORE THAN THE FINDING:** 67.0 is **this paper's own implementation of a
  pitch-profile key detector described as being after Temperley (1999)**, measured on this paper's corpus.
  **It is not a figure from row 6, it is not row 6's own reported accuracy, and it supplies no bibliographic
  content of row 6 at all.** What it supplies is a measured comparison point for that family on classical
  symbolic data, obtained from a held source.
- **Row 9** — *"Temperley 2001, Temperley 2007, Krumhansl 1990 (books)"*, **ADMITTED, AND UNREADABLE FROM
  HERE** — **is not reached.** This paper cites **Krumhansl and Kessler (1982)**, a different work from
  Krumhansl 1990, and cites neither Temperley 2001 nor Temperley 2007.
- **Rows of the candidacy table that this paper's reference list does contain**, by the candidacy file's own
  numbering: **4** (Pardo & Birmingham 2002), **6** (Temperley 1999), **21** (Harasim, Rohrmeier &
  O'Donnell 2018), **22** (Rohrmeier 2011), **34** (Illescas, Rizo & Iñesta 2007), **35** (Ju,
  Condit-Schultz, Arthur & Fujinaga 2017), **41** (Hadjeres, Pachet & Nielsen 2017), **42** (Liang, Gotham,
  Johnson & Shotton 2017), **46** (Chen & Su 2018), **47** (Chen & Su 2019, the Harmony Transformer half of
  that two-paper row), **53** (Devaney et al. 2015, TAVERN), **54** (Neuwirth et al. 2018, ABC), **60** (de
  Clercq & Temperley 2011).
- **★ ONE NEAR-MISS THAT A LATER READER COULD TAKE FOR A HIT.** Candidacy row **27** is **Rocher, Robine,
  Hanna & Oudre, ISMIR 2010**, *concurrent estimation of chords and keys* — the member this line's second
  extractions began with. **This paper cites Rocher, Robine, Hanna & Strandh, ICMC 2009, *dynamic chord
  analysis for symbolic music*** — overlapping authors, adjacent year, different paper and different
  venue. **It also cites Robine, Rocher & Hanna, ICMC 2008, *improvements of key-finding methods*.**
  **Neither is row 27**, and neither appears in the candidacy file at the lines this search returned.
- **Nothing else in this paper's list matched a row at the lines the search returned**, and that negative is
  bounded to the name list searched.

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

**The read-back is the second of the two acts the procedure puts between writing and landing.** It reads the
finished text back against the paper, at the paper, for every value and every claim about the paper that
this file asserts. **It ran after §0 to §7 were written and before anything was landed.**

**Pages re-opened, named rather than counted:** printed page **44** (PDF 3), for Table 1's six row values
and its three printed totals; printed page **46** (PDF 5), for Table 3 cell by cell, for the *Different
Annotators* and *Data Formats* paragraphs and for the six numbered properties; printed page **47** (PDF 6),
for Table 4, for the pitch and registral paragraphs, and for the §3.2 passage this file quotes whole at
§2.6; printed page **48** (PDF 7), for the Schubert key sentence, for Figure 4's axes and caption, and for
Figure 5's box figures and output class counts; printed pages **49 and 50** (PDF 8 and 9), for Table 5 cell
by cell, for Table 6 cell by cell including its counts column, for §4.1's three significance statements and
for §4.2's three error classes and two worked cases; printed page **52** (PDF 11), for footnotes 1 to 17 and
for the first block of the reference list; printed page **53** (PDF 12), for the Schoenberg entry and the
rest of the reference list.

**Every re-opened image was present and legible, checked at the image.** **The pages NOT re-opened are
printed 42, 43, 45, 51 and 54** (PDF 1, 2, 4, 10 and 13) — the abstract and §1.1, §1.2 and §1.3, §2's prose
and Table 2, §5 and Figure 6 and Table 7, and the last page of the reference list. **Said plainly:** what
stands in place of a second look at those is that this file quotes them rather than paraphrasing them, and
that the identity facts on printed page 42 are independently repeated in the *How to cite* box on printed
page 54. **That is weaker than a second look and is not claimed to be equivalent to one.**

**★ TWO OF THOSE PAGES WERE ADDED TO THE RE-OPENED LIST BECAUSE THIS SECTION'S FIRST WRITING GOT ITS OWN
ACCOUNT WRONG.** As first written, §8.1 said *"three of the thirteen pages were not re-opened"* and then
listed five, while §8.4 said five — **a count of this side's own acts, wrong against the list beneath it, in
the section whose whole job is to report those acts.** Correcting it showed that printed pages 46 and 47 —
carrying Table 3, Table 4 and the passage this file treats as the load-bearing one — **were among the
unread**, so they were re-opened before this sentence was written, and both tables and that passage are
confirmed word for word and cell for cell. **The count is now right because the act was done, not because
the sentence was adjusted.**

### §8.2 What the read-back and the sweep struck in this side's own writing

Named rather than counted. **Every correction is at its own site above with the former wording preserved
where a claim was struck (#12).**

1. **★ THE ONE FINDING AGAINST THE PAPER THAT WAS THIS SIDE'S OWN ERROR, AND IT IS THE WORST OF THESE.**
   §7.1's item 3 asserted that §3.3 exchanges the labels *flattest* and *sharp-most* on its Schubert
   example. **The page refutes it**: the paper calls B minor the sharp-most key used and C minor the
   flatmost, which is the correct way round, and both step counts are right. **The claim was written from a
   first reading of the page and was wrong about what the page says.** Struck at its site with the former
   wording preserved; §6.5's pointer to it rewritten. **Carry this: a defect asserted AGAINST a source is
   the kind of claim that most needs the second look, because it is the kind a later reader will repeat.**
2. **A SELF-CONTRADICTION BETWEEN THIS FILE'S OWN SECTIONS.** Claim C24 said the word *significant* is
   supported by t-tests reported *"only for the architecture and bass axes"*, while §7.2 and §7.3 of this
   same file both record a third one — p < 10⁻⁶ on the quality label across training modes. **The cell is
   corrected to name all three and to say that none of them tests the Table 5 comparison itself.**
3. **A SECTION THAT CARRIED THE CLASSES AND NOT THE CASES.** §5 set out the three error classes from §4.2
   and omitted the two passages the paper works through in support of them. **§5.11 was added**, carrying
   the Schubert and Beethoven cases verbatim — and writing it produced one finding this file did not have
   before: that the reference analysis at the Schubert passage corresponds to A2, the reading the paper's
   own Table 2 records as breaking rule 1.
4. **A RELAY PRESENTED AS A FINDING ABOUT THE RECORD.** §2.6's heading called its quotation *"THE
   LOAD-BEARING PASSAGE OF THIS PAPER FOR THIS PROJECT'S RECORD"*. **`FRAMEWORK.md` was not opened by this
   read at any point**, so what DP-A does with that passage is not established here. The heading now says
   what it is — the passage the candidacy line points at — and marks the relay at its site.
5. **ABSOLUTES AND UNBOUNDED NEGATIVES, SWEPT AT EVERY HIT AND READ AT ITS LINE.** The sweep searched this
   file for *anywhere*, *nowhere*, *never*, *none*, *always*, *exhaustive*, *the only* and *no other*, and
   every hit was read in place rather than counted. **What was rewritten, named:** six negatives of the form
   *"appears anywhere in this paper"* or *"anywhere in the thirteen pages"*, now *"met nowhere in the pages
   as read"*; *"the paper never reconciles the two numbers"* and *"the paper reconciles them nowhere"*, both
   now bounded to what this read met; *"Nothing in the caption or the text accounts for either blank"*;
   *"the only place in the paper where the behaviour is shown"*; *"the only reading on which the column
   closes"*, now stating what the alternative reading gives (147); *"the only place the paper connects
   them"*; *"fifteen and fifteen is reachable only by halving thirty"*, now *"this read can construct no
   other route"*; *"the weakest conclusion it draws anywhere"*; *"the word test does not appear … anywhere
   in the thirteen pages"*; *"the headline 42.8 is not a figure any row of this table can be differenced
   against"*, which was **false as written** — the two rows above the dividing line can be differenced
   against each other — and now reads *"any row BELOW the dividing line"*; *"no boundary, span or segment is
   predicted as a thing in its own right"*; *"nothing about its provenance has to be inferred"*; and *"the
   paper never says in one place that these two sixes differ"*.
6. **ONE PLACE WHERE THE SWEEP CHANGED NOTHING, SAID BECAUSE IT IS EVIDENCE ABOUT THE SWEEP.** §7.3's claim
   that *full* and *class* sit below *bass* **everywhere** in Table 6's registral sub-table was checked at
   all five columns of both rows and stands as written; so does §7.3's claim that −4.1 is the largest
   movement in the architecture sub-table, checked at all ten of its cells.

### §8.3 The degradation tells, reported unprompted

The user's standing rule of 2026-08-15 asks a session to name its own degradation tells rather than wait to
be asked. **The instances are named and deliberately not totalled.**

- **Tell A — a count, a proportion, a ranking or a superlative put on this side's own reading or on the
  source without deriving it.** *(i)* §7.3's *"the largest single movement in Table 6's architecture
  sub-table"* was written before the ten cells were compared; **it survived the check**, but it was an
  assertion first and a derivation second, which is the wrong order. *(ii)* §5.10's *"fifty-one entries"*
  is a count of this side's own transcription, and it is stated **with** its derivation and its risk of
  miscount at the same place — recorded here as an instance of the shape even though it carries its bound.
  *(iii)* The struck absolutes at §8.2 item 5 are the same tell in its negative form: a negative over a
  whole document is a claim about a population this read did not enumerate. *(iv)* **★ AND IT FIRED INSIDE
  §8.1 ITSELF**, the section written to report this side's own acts: it said *"three of the thirteen pages
  were not re-opened"* over a list of five, and contradicted §8.4 two subsections below. **Caught by
  checking the sentence against its own list**, which then showed that two load-bearing pages were among the
  unread; they were re-opened and the section rewritten (§8.1). *(vi)* **★ AND IT FIRED AGAIN AT THE
  CROSS-CHECK, IN THE HARDEST FORM.** §9.6's first writing said *"thirty-nine agreements at the cells"* —
  **a count this side never made, and the exact figure the hundred-and-seventy-ninth entry records for ROW
  18's cross-check**, which this side read whole at boot. **A number belonging to another member, attached
  to this one, in a sentence about how little the agreements establish.** Caught in the act of writing the
  sentence after it; struck at its site with the former wording preserved. **This instance also answers
  Tell B's description — a figure carried from an entry rather than derived here — and is named once rather
  than counted twice.**
- **Tell B — citing a summary instead of the source, or presenting a relay as established.** *(v)* §2.6's
  heading, at §8.2 item 4: a statement about what this project's record does with a passage, written from
  the candidacy line and the progress record rather than from `FRAMEWORK.md`, which was not opened.
  **Caught at the sweep and marked as a relay at its site.**
- **★ AND ONE INSTANCE THAT ANSWERS NEITHER DESCRIPTION EXACTLY BUT BELONGS HERE.** §8.2 item 1 — a defect
  asserted against the paper that the paper refutes — is not a count, a ranking or a relay. **It is a claim
  about a source written from one reading of it.** It is named here because it is the instance of this
  sitting that would have done the most damage had it landed: a later reader would have carried "this paper
  gets its own worked example backwards" out of a file whose whole purpose is to be checkable.

**What the threshold means here, stated plainly.** **What fired is TWO of the user's named tells**, with
the instances named above and not added up, plus the one instance that fits neither exactly. **Every one was
caught by a pass of this side's own, and that does not lower the count** — the entries this side read whole
this sitting, the hundred-and-seventy-ninth and the hundred-and-sixty-ninth, each record the same thing of
their own sittings.

### §8.4 The bound on this section

**The read-back and the sweep are further passes over the same writing by the same side.** The read-back
caught what the writing did not; the sweep caught what the read-back did not; **and nothing here says a
further pass would come back empty.** Five of the thirteen pages were not re-opened (§8.1). The cross-check
against the first extract had not been run when this section was written; **what it found is at §9**, which
is a separate act.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**Step 7 of the procedure: only after this file's §0 to §8 were written, read back, swept and landed was the
first extract opened.** It is
`reading_pass/extracts/micchi-gotham-giraud-2020-not-all-roads-lead-to-rome-pitch-representation-and-model-architecture.md`,
**58,313 bytes** at this sitting's own staging call, **read whole in one call**. It is dated 2026-09-06 and
records itself as the twelfth reading session of L2's slice, booted at tip
`911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb`.

**THE INDEPENDENCE BOUND IS AT §0 AND IS NOT WEAKENED HERE.** This side had read the progress record's own
row for row 45 and the candidacy line before opening the paper, so the centrality verdict and the
requires-spelling characterisation were known. **What was NOT known before the paper was read is everything
in the first extract's own text**, which was opened for the first time at this step.

**★ AND THE TWO READS ARE NOT COMPARABLE OVER THE SAME GROUND, WHICH MATTERS MORE THAN THE AGREEMENTS.**
The first extract's work divides in two. Its **paper half** — identity, tables, quotations, coupling facts —
is comparable with this file. Its **record half** — `FRAMEWORK.md` at DP-A (lines 671–683) and §S4(a)
(lines 1548–1577), `reading_pass/population.md` at V3 to V13, the slice derivation, the findings surface,
the bibliography, and its eleven routed findings — **this read opened none of those files at any point.**
**On that half this is silence, not a second opinion**, and no verdict of this file bears on it, including
on its finding (1), which it grades STOP-shaped and puts to the user.

### §9.2 What both reads transcribed, and where they agree

**The agreement is broad and it is digit for digit where both transcribe.** Named rather than counted:

- **Table 5, every printed cell of every row**, including both blank patterns.
- **Table 6, every printed cell AND every count in its *n* column** — 12, 12, 6; 10, 10, 10; 15, 15; 15, 15.
- **Figure 5's six class counts** — 12, 4, 35, 30, 21, 21 — and the two derived values **123** and
  **22,226,400 ≈ 22·10⁶**, which **both reads derived independently from those six boxes and both closed.**
- **Table 4's six encodings and all six dimension arithmetics.**
- **Table 1's four printed totals** — 201 scores, 111,859, 36,812, 73,175.
- **The identity axis in full** — title, subtitle, three authors, both affiliations, corresponding author,
  TISMIR 3(1) 2020, pp. 42–54, DOI 10.5334/tismir.45, the three dates, CC-BY 4.0, Ubiquity Press — and the
  held file's size, **1,906,114 bytes**, established by each side at its own listing.
- **Every protocol constant** of §5.9: the two frame rates, the 2-quarter-note window, the 80-quarter-note
  segment, the dilated convolution's four parameters and its 3⁴ = 81 context with 40 each side, the GRU's
  64 neurons per direction and 0.3 dropout, the 64-neuron head, the 90/10 split, 94,000 = 33,000 + 43,000 +
  18,000, the 20-minutes-to-3-hours range, Python 3.7 and Tensorflow 1.14.
- **Both transposition limits**, F♭♭–B♯♯ and C♭–C♯ major with A♭–A♯ minor; and **Figure 4's range 3 to 15
  with the bulk at 10–13**. **Neither read transcribed a bar height from Figure 4**, both for the same
  stated reason.
- **Table 7's fragmentation**, reached by each side separately: the corpus's m2 becomes **four** output
  rows, m3 **five**, m5 **three**.
- **§4.2's three named error classes, and the fourth named apart from them**, the Beethoven case.
- **The absence of a held-out test set beyond the validation tenth**, and the absence of any ± value,
  interval or spread on any cell of Tables 5 and 6 against the presence of three reported p-values.
- **★ AND ONE FINDING THE TWO READS REACHED INDEPENDENTLY AND IDENTICALLY:** that Table 5's
  *"Local model after Temperley (1999)"* row, Key 67.0, is **these authors' own implementation** after a
  method the record holds as **candidacy row 6, admitted and NOT held** — and that nothing is carried out of
  Temperley (1999) itself. This file has it at §7.4; the first extract has it as its finding (8).
  **The doubling corroborates it rather than producing it.**

### §9.3 ★ The disagreements, and all of them go against the first extract

**Four places where the paper goes against the first extract. Three are words inside quotations; one is a
dropped word. None moves a transcribed value. That file is UNTOUCHED** — the ground being this line's own:
rewriting another read's text destroys what the doubling compares.

**(a) ★ A WORD INSIDE A QUOTATION THAT STRENGTHENS THE AUTHORS' OWN CLAIM, AND THE FIRST EXTRACT LEANS ON
IT TWICE.** It quotes §3.1's *Different Annotators* paragraph as *"doing so will **surely** introduce some
bias in the model"*, at its claims section and again inside its finding (5). **The paper prints *"will
**likely** introduce some bias in the model"***, established at printed page 46 at the whole read, again at
the read-back, and a third time at a separate opening at this cross-check. **The substitution moves a
hedge to a certainty in a sentence the first extract's finding (5) routes to measurement design beside
D-474 and OI-179.** No value moves and the finding's substance stands.

**(b) ★ A WORD INSIDE A QUOTATION THAT CHANGES THE SENSE OF THE SENTENCE, AND IT IS THE ONE OF THE FOUR A
LATER READER WOULD CARRY WRONG.** It quotes §4.2's fourth error class as *"where the most compelling
**machine** reading diverges from the statistically normative case"*. **The paper prints *"the most
compelling **musical** reading"***, established at printed page 50 at the whole read, again at the
read-back, and a third time at a separate opening here. **The two readings say opposite things about whose
reading is compelling:** the paper's sentence is that the *musically* best reading differs from the
statistically normal one — which is why the authors call these cases **unacceptable** rather than
alternatives — whereas *"machine reading"* makes the sentence say the system's own output is the compelling
one, which would make the class unintelligible. **No value moves, and the first extract's surrounding
treatment of the class is unaffected**; what is wrong is the word.

**(c) A SUBSTITUTION THAT CHANGES NOTHING.** It quotes §4.1 as *"enharmonically equivalent keys **such
as** G♯ and A♭"*; the paper prints *"enharmonically equivalent keys **like** G♯ and A♭"*. Printed page 50,
read three times.

**(d) A DROPPED WORD IN A QUOTATION OF §4.1.** It quotes *"all possible combinations of the six
encodings"*; the paper prints *"all possible combinations of the six **pitch** encodings"*. Printed page
49, established at two openings of that page rather than three. **The sense is unchanged** — the six are
the pitch encodings either way — **but it is the same class of defect as (a) to (c).**

**★ AND WHAT THE COMPARISON PRODUCED AGAINST THIS SIDE: ONE NARROWING, NOT A CONTRADICTION.** §7.4's first
bullet was headed *"THE ONE FINDING OF THIS SUBSECTION"* of the Temperley-baseline datum. **The first
extract reached the same finding independently** (§9.2), so the heading, while true of this file's own
subsection, reads as a claim of novelty the doubling refutes. **Corrected at its site with the former
wording preserved (#12).** **This side found nothing in its own text that the paper contradicts.**

### §9.4 What the first extract has that this read did not, adopted here and marked

**Three precisions come FROM the first extract and are adopted into this file at their own sites, each
marked as adopted.**

1. **★ THE SPLIT IS BY SCORE, SO NO SCORE SITS IN BOTH HALVES.** This file recorded the 90/10 proportion
   and that it is applied per corpus; the first extract states the unit. It is right at §3.5's own words —
   *"90% of the available scores"* — and it is the thing that makes the split meaningful.
2. **★ AND THE SHARPER POINT THAT FOLLOWS, WHICH IS THIS SIDE'S DEBT TO THAT READ:** model selection across
   the six encodings, the two architectures and the two training modes **was made on the same data every
   headline figure is reported over.** With no third partition, the thirty-model comparison and the reported
   accuracy share a population. **That is a stronger statement of §7.2's no-test-set point than this file
   had**, and it is adopted at §7.2 rather than left in the other file.
3. **Six figures and seven tables** — a structural fact of the document this file nowhere states, and one a
   later reader uses to know whether an extract covered the whole.

### §9.5 What this read has that the first extract does not

**Named rather than counted. The four that bear on how a printed value or a stated claim of the paper is
read are marked ★.**

- **★ TABLE 1's QUARTER-LENGTH COLUMN IS TEN SHORT OF ITS OWN PRINTED TOTAL** (§6.1). The first extract
  transcribes the four totals and says in terms that the per-row values *"are not restated here beyond the
  totals"* — **it never added the column.**
- **★ TABLE 6's TRAINING-AXIS COUNTS CANNOT BE RIGHT** (§6.8). The first extract transcribes 15 and 15 and
  reproduces the caption's PoolGRU sentence in a parenthesis directly beneath them, **without checking one
  against the other.**
- **★ FIGURE 5's "8k" AGAINST §3.5's "18,000"** (§6.7). The first extract quotes §3.5's decomposition and
  does not transcribe Figure 5's weight boxes, so the two numbers never meet in it.
- **★ §4.2's REFERENCE ANALYSIS OF THE SCHUBERT PASSAGE IS A2** (§5.11) — the reading the paper's own Table
  2 records as **breaking rule 1**. The first extract quotes the *"four different chord labels"* sentence
  from the same paragraph and does not carry the sentence before it.
- **The Schoenberg reference's two years, against footnote 17's single one** (§7.1, item 5); the first
  extract's closing list carries *"Schoenberg 1954"* and does not meet footnote 17's *"Schoenberg (1948)"*.
- **Table 2 transcribed**, with A1 and A3 carrying identical rule verdicts (§5.2 and §7.1, item 8). The
  first extract describes §2's three analyses and does not transcribe the table.
- **The two different "sixes"** — the tabular format's properties against the network's output labels
  (§2.3).
- **The dilated convolution's receptive field derived**, which closes only if the layer index starts at
  zero, and the 40-eighth-note context expressed as 20 quarter notes against the 80-quarter-note segment
  (§6.6).
- **The 35 spellings and the 30 keys derived from the stated limits**, and all four numbers of the Schubert
  transposition example closed (§6.4, §6.5).
- **Table 3's tiling closed at 44.0**, and Table 7's corpus column verified cell for cell against Table 3
  rather than taken from its caption (§6.11, §6.12).
- **The like-for-like differences computed at the cells**, and with them the point that **the full-task
  comparison against the most recent prior system cannot be computed at all**, Table 5 printing no RN value
  for Chen and Su (2019) (§6.10). The first extract makes the like-for-like/not-like-for-like distinction in
  words and computes no difference.
- **The reference list transcribed and enumerated** (§5.10) — **which the first extract declines in terms**:
  *"No count of reference entries is asserted here; the list was not enumerated."* **So this side's
  fifty-one is uncorroborated by the doubling**, and §5.10's own bound on it stands.
- **The candidacy-file cross-check of that list** (§7.4), including the near-miss between this paper's
  Rocher et al. 2009 and candidacy row 27's Rocher et al. 2010.

### §9.6 What the cross-check does NOT establish

- **It does not reach the first extract's record half at all** (§9.1). Its eleven routed findings, its
  centrality argument, its adopt-or-argue section and its finding (1)'s STOP grading are **untouched and
  unjudged here.**
- **It is not exhaustive over the paper half either.** It ran over what both files carry. Where only one
  carries something, there is nothing to compare, and §9.5's list is what this side noticed rather than a
  derived difference.
- **It establishes nothing about the first extract's searches.** That file's banner records five `Grep`
  passes over the staged tree and concludes the record cites this paper in six places. **This side ran no
  sweep of the repository for this paper** and takes no position on that count.
- **Both reads could be wrong together.** That two independent transcriptions of the same printed tables
  agree cell for cell is evidence that they agree; **it is not evidence that either read the tables
  correctly.**
  *(★ CORRECTED IN THE ACT OF WRITING THIS SECTION. FORMER WORDING, PRESERVED (#12): "**Thirty-nine
  agreements at the cells** are evidence that two independent transcriptions of the same printed table
  agree". **This side never counted the agreeing cells**, and thirty-nine is the figure the
  hundred-and-seventy-ninth entry records for ROW 18's cross-check, which this side read whole at boot. **A
  number carried out of another member's account and attached to this one is the plainest form of the tell
  this file reports at §8.3**, and it is recorded at §8.3 as instance (vi).)*

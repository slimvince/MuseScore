# EXTRACT — Micchi, Gotham & Giraud, "Not All Roads Lead to Rome: Pitch Representation and Model Architecture for Automatic Harmonic Analysis" — Task B candidacy row 45, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All thirteen pages of the held PDF were read AT THE OBJECT: staged through the
> bridge and read with the file tools as page images. **No relay, no web-fetch read, no prompted
> extraction.** The held document prints journal page numbers 42–54 and a running header, so every
> location below is given as the printed section, table or figure number together with the journal
> page.
>
> **★ ROW 45 OPENS GROUP 3 OF THE PROPOSED ORDER** ("the scoring architecture and its fitting",
> `reading_pass/candidacy_upgrades.md` line 177). It is the first row read since row 18 on which a
> **ratified `[FACT]` rests** — derived, not relayed: only row 47 was read between the two, and its
> own extract states that no `[FACT]` in the record names either of its papers. That verification was
> performed FIRST, before anything else was extracted — see "The verification target" below.
>
> **Where the record cites this paper, established by `Grep` of the staged tree BEFORE extracting,
> never inherited.** **The searches actually run, in order, and what each found:** *(1)* the bare
> word **"Micchi"** — hits at `reading_pass/candidacy_upgrades.md` line 117 (the row),
> `cowork_l2_task_b_slice_derivation_2026_09_05.md` line 80 (the placement),
> `docs/research_papers/BIBLIOGRAPHY.md` lines 64 and 80 (its own row, and the unrelated *When in
> Rome* meta-corpus row), `FRAMEWORK.md` **line 1559** (§S4(a)'s sealed first-stage text),
> `reading_pass/population.md` **line 110** (the V9 verification row), plus this line's own files
> (the progress record, the hundred-and-twenty-seventh handoff entry, and the row 47 extract, which
> cites the paper as a work *its* papers cite); *(2)* **"Roads" / "self-contradictor" /
> "sub-labels"** — the same set plus `FRAMEWORK.md` **line 676**, the LIVE DP-A ground, which quotes
> the passage **without naming the paper or its authors**; *(3)* the bare word **"Giraud"** — six
> files, `cowork_reading_pass_findings_2026_08_31.md` **not among them**; *(4)* **"V9" / ".462" /
> "462" / "sub-labels"** over the findings surface alone — lines 136 and 613, which name the V9
> verdict and **name neither the paper nor its authors**; *(5)* **"Rome" / "Gotham" / "tismir.45" /
> "not_all_roads"** — no file beyond those already found. **Bare words were searched as well as
> phrases**, on the method fact the row 47 read carried forward (a phrase can be split across a line
> break); here no phrase was split, and searches (1) and (2) already found everything (5) did.
>
> **So the record cites this paper in SIX places, outside this line's own working files:** the candidacy row (line 117); the
> slice derivation (line 80); the bibliography (line 64); `FRAMEWORK.md` §S4(a) (lines 1559–1561),
> which names *"Micchi and colleagues"*; `FRAMEWORK.md` DP-A (line 676), which quotes it
> **anonymously**; and `reading_pass/population.md` V9 (line 110), which is the only place in the
> record that gives the quotation a page. **The bound on that claim:** it is a claim about the files
> in this session's staged tree — the governing surfaces, the reading-pass files and this line's own
> files — and not about every file in the repository; the tree searched is the one enumerated in the
> provenance below.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## ★ The verification target — the ratified `[FACT]`, VERIFIED VERBATIM, with two precisions

`reading_pass/l2_slice_reading_progress.md`'s carried item (a) names one thing to do before
anything else: locate the quotation DP-A and §S4(a) both carry, verify it word for word at its own
page, and record what the paper's own numbers for the self-contradiction are.

**VERIFIED, at page 47, §3.2 "RN Output Labels", right column.** The sentence reads, verbatim:

> *"This comes at the cost of a potential for self-contradictory outputs in which the six sub-labels
> have different ideas about the chord."*

That is the quotation as `FRAMEWORK.md` DP-A (line 676) and §S4(a) (line 1560) carry it, word for
word, and `reading_pass/population.md` V9's location — *"quote verbatim at Micchi, Gotham & Giraud
2020 (TISMIR 3(1)), p. 47"* — is **correct at the object, page included**. **Nothing is owed to the
`[FACT]` as a quotation.**

**PRECISION (1) — THE PAPER'S NEXT SENTENCE BOUNDS IT, AND THE RECORD CARRIES NO BOUND.** The
quoted sentence is followed immediately, in the same paragraph, by:

> *"In practice, we find that this is only rarely a problem, arising in the particular case of the
> 'no chord' label used by the ABC dataset (only) for passages with rests and/or single line
> melodies. Given the inconsistency in the source data, we do not include a provision for the 'no
> chord' case. Instead, we fill any such gap with a continuation of the foregoing chord, except in
> the case of beginnings, for which we start the first chord early."*

So the authors declare a **potential** cost and then report that in their own practice it is **rare**
and **localised to one dataset's 'no chord' label**. Neither the live DP-A text nor §S4(a) carries
that half.

**PRECISION (2) — THE PAPER GIVES NO NUMBER FOR IT, ESTABLISHED BY A WHOLE READ.** Carried item (a)
asks what the paper's own numbers for the self-contradiction are. **There are none.** No figure for
label inconsistency, incoherence or contradiction appears anywhere in the thirteen pages — not in
Table 5, not in Table 6, not in Table 7, not in §4.2's three named error types (which are
segmentation, rare-chord mislabelling and alternative readings — inconsistency is not among them),
and not in §5. The only statement of magnitude is the words *"only rarely a problem"*. **This is
stated as an absence established by reading the whole paper, not as an assertion about an unexamined
thing.**

**PRECISION (3) — THE PAPER ARGUES FOR THE DIVISION, AND ITS ARGUMENT IS QUANTIFIED WHERE THE COST
IS NOT.** The quoted sentence's *"This"* refers back to the two sentences immediately above it, which
give the authors' reason for dividing the label:

> *"There is some redundancy built into this system as it is possible to derive the root
> unambiguously from other features. However, learning redundant variables can be helpful to the
> algorithm's success. The division of each RN label into six independently-computed sub-labels
> reduces the complexity of the task, since the total number of possible outputs for our
> best-performing representation is Σᵢcᵢ = 123 ≪ ∏ᵢcᵢ ≈ 22·10⁶, where cᵢ is the number of output
> classes for each separate target label. It also improves the interpretability of the results,
> allowing one to focus on each aspect separately."*

**The arithmetic closes at the object and is derived here rather than taken on trust:** the six label
sizes Figure 5 prints for the best-performing PSb representation are Quality 12, Inversion 4, Root
35, Key 30, Degree 1 21, Degree 2 21; their sum is **123** and their product is **22,226,400 ≈
22·10⁶**. Both of the paper's own figures reproduce. **That arithmetic is itself the cross-check on
the six transcribed cells**: no other reading of Figure 5's boxes gives both 123 and ≈22·10⁶, so the
two printed values in §3.2 and the six boxes in Figure 5 confirm each other.

**What follows for the record, and what does not.** The quotation is accurate and stays accurate.
What the record does not carry is that its source **chose** the six-head division deliberately, on a
stated and quantified ground, and reported the incoherence cost as rare. This bears on how DP-A's
ground reads and is written up as finding (1); **no verdict is moved and nothing is amended.**

## Identity — NO finding

Gianluca Micchi (Univ. Lille, CNRS, Centrale Lille, UMR 9189 – CRIStAL – Centre de Recherche en
Informatique Signal et Automatique de Lille, Lille, FR), Mark Gotham (Cornell University, Ithaca,
NY, US) and Mathieu Giraud (same Lille affiliation); corresponding author Gianluca Micchi
(`gianluca.micchi@univ-lille.fr`).

**Printed title, page 42:** *"Not All Roads Lead to Rome: Pitch Representation and Model
Architecture for Automatic Harmonic Analysis"*, marked **RESEARCH**. The journal's citation block is
printed at the head of page 42: *"Micchi, G., et al. (2020). Not All Roads Lead to Rome: Pitch
Representation and Model Architecture for Automatic Harmonic Analysis. Transactions of the
International Society for Music Information Retrieval, 3(1), pp. 42–54. DOI:
https://doi.org/10.5334/tismir.45"*. The back matter on page 54 repeats it under *"How to cite this
article"* and adds *"Submitted: 04 December 2019   Accepted: 23 March 2020   Published: 12 May
2020"* and *"Copyright: © 2020 The Author(s). This is an open-access article distributed under the
terms of the Creative Commons Attribution 4.0 International License (CC-BY 4.0)…"*, published by
Ubiquity Press, marked OPEN ACCESS.

**The bibliography's row** (`docs/research_papers/BIBLIOGRAPHY.md` line 64) names *Micchi, Gotham &
Giraud, "Not All Roads Lead to Rome," TISMIR 3(1), 2020*, URL
`https://transactions.ismir.net/articles/10.5334/tismir.45`, held ✓, tier **CC**.

**What matches, at the object.** Authors, venue, volume, issue, year and licence tier all match; the
DOI printed twice resolves to the row's URL; and the row's title is the printed title's **leading
phrase** — the row gives the short title and the paper prints title plus subtitle, the same
prefix-match shape row 47's 2019 paper had. The printed pagination 42–54 is not in the row, which
carries no pages for any entry. **The identity check closes with NO finding.**

**Keywords printed:** *Roman numeral analysis; functional harmony; machine learning; pitch encoding;
corpus.*

**The input, established at §3.2, page 46 and page 47: SYMBOLIC ONLY.** Frame-based encoding of a
score; the authors state at footnote 14 that full pitch spelling *"is only available to richer input
formats like **kern, MusicXML, and MEI"* and that *"Systems using MIDI are necessarily limited to
the former"* (chromatic pitch). **No audio anywhere.** So **no domain caveat under the candidacy
derivation's consequence (ii) applies to this row**: it is symbolic Western classical music, our own
input kind, and its best-performing configuration **requires notated spelling to be available** — a
consumer of L0's given spelling, as the progress record records rows 29 and 30 to be and as row 5's
spelled variant is. **No count and no "only" is asserted**: those extracts were not opened this
session, and what is established here is this paper's own requirement.

**Structure of the held document:** five numbered sections — 1 Introduction, Motivation, Previous
Work (§1.1 Key, Chords and Functional Harmony; §1.2 Previous Computational Approaches; §1.3 Analysis
Datasets; §1.4 Aim and Contents); 2 On Functional Harmonic Analysis; 3 Method (§3.1 Meta-corpus;
§3.2 Encoding Input and Outputs; §3.3 Data Augmentation by Transposition; §3.4 Network
Architecture; §3.5 Network Training); 4 Results (§4.1 Overall Metrics; §4.2 A Closer Look at the
Music); 5 Future Work (§5.1 Improvements; §5.2 Applications) — then Notes (17), Acknowledgements,
Competing Interests and References. Six figures, seven tables. Thirteen pages, 42–54. **No count of
reference entries is asserted here; the list was not enumerated.**

**File:** `docs/research_papers/micchi_gotham_giraud_2020_tismir_not_all_roads_lead_to_rome.pdf`
(1,906,114 bytes at this session's `docs/research_papers/` listing).

## Claims, labeled

### The corpus (§3.1, Table 1, page 44)

**[FACT — Table 1, page 44.]** The meta-corpus draws together four existing RN corpora: **TAVERN**
(Mozart, 10 theme-and-variations sets; Beethoven, 17 theme-and-variations sets), **ABC** (Beethoven,
16 string quartets, 70 movements), **BPS-FH** (Beethoven, 32 piano sonata first movements) and
**Roman Text** (Bach, 24 preludes; Various 19th-century, 48 romantic songs). Totals: **201 scores,
111,859 quarter-note length, 36,812 measures, 73,175 RNs**. The per-corpus quarter lengths, measures
and RN counts are printed per row and are not restated here beyond the totals.

**[FACT — §3.1, page 45.]** *"We sought to convert each representation standard directly, without
changing or interpreting those analyses except in case of clear errors."* New open-source converter
tools were written; the RN annotations and tools are at `https://gitlab.com/algomus.fr/functional-harmony`.

**[FACT — §3.1 "Different Annotators", page 46.]** *"Among these datasets, 'TAVERN' is the only one
to include more than one alternative reading of the same piece by different annotators… In this
study, for the sake of simplicity, we have elected to treat each of these analyses independently. It
is clearly not quite right to treat multiple analyses of the same music as equivalent to analyses of
separate pieces, and doing so will surely introduce some bias in the model; however, we consider
this a small detraction relative to the gain in variance afforded by the alternative readings."*
And: *"there is a non-separable correlation between annotators and musical genres"*, each original
dataset focusing on a different style. Inter-annotator stylistic variance is named as **future
work**.

### The output labels — six heads (§3.2, page 47; Figure 5, page 48)

**[FACT — §3.2 "RN Output Labels", page 47.]** *"Continuing to follow Chen and Su (2018) we output
the harmonic analysis with six labels: Key, Degree 1, Degree 2, Quality, Inversion, and Root. The
two labels for scale degrees handle cases of tonicisations in the format 'Degree 2/Degree 1'."*

**[FACT — Figure 5, page 48, PSb case.]** The class counts per head: **Quality 12, Inversion 4, Root
35, Key 30, Degree 1 21, Degree 2 21.**

**[FACT — §3.2, page 47.]** For chromatic-pitch (CP) input there are **12 roots and 24 keys**; for
pitch-spelling (PS) input with double sharps and flats there are **35 roots and 70 keys** — reduced
in practice by the transposition constraint of §3.3 (see below), which is why Figure 5 prints 30 keys.

**[FACT — the tabular annotation format, §3.2, page 46.]** Six properties, following Chen and Su
(2018): start offset, end offset, **key (specifying full pitch spelling, so that G♯ ≠ A♭; uppercase
major, lowercase minor)**, quality, (scale) degree from 1 to 7 with accidental modifications and/or
secondary tonicised degrees, and **inversion from 0 to a maximum of 3** — *"thus supporting all
inversions of seventh chords, but no ninths."*

### The input encodings (§3.2, Table 4, page 47)

**[FACT — Table 4, page 47, limited to 7 octaves and double sharps/flats.]** Six encodings, the
total input-vector dimension for each: **CPf** chromatic pitch, full 7 × 12 = **84**; **PSf** pitch
spelling, full 7 × 35 = **245**; **CPb** CP class + bass 12 + 12 = **24**; **PSb** PS class + bass 35
+ 35 = **70**; **CPc** CP class **12**; **PSc** PS class **35**.

**[FACT — §3.2 "Pitch", page 47.]** Two dimensions of choice: **spelling** (12 pitch classes against
21 per octave for single sharps/flats, 35 for double) and **registral information** (full octave
information; or none; or a *"'compromise' option reflecting the special role of the bass in tonal
harmony in defining both chordal inversion and other important matters for harmonic progression. In
this case, music is encoded with two vectors per frame: one with the lowest note and another with
the total pitch content."*)

**[FACT — §3.2 "Time", pages 46–47.]** *"We follow this latter practice for equal-duration, binary
division frames. In our case, we use a 32nd note for input encoding (notes) and 8th note for the
output (chords), as the harmonic rhythm is almost always (much) slower than the surface rhythm.
Finally, we divide all scores in segments of equal quarter-note duration and pad with zeroes to the
right when needed."* The Boolean matrix has **time frames on one axis and pitches on the other**;
value 1 if the pitch is present in that frame.

**[FACT — §3.2 "Pitch", page 47, a declared limitation.]** *"One potential shortcoming of such a
frame-based encoding is that it fails to distinguish between repeated and held notes… We decided not
to encode that information partly due to the loss of compactness, but also because we do not expect
distinguishing tied from repeated notes to be especially important for harmonic analysis."*

### Transposition (§3.3, pages 47–48; Figure 4, page 48)

**[FACT.]** Two constraints on the augmentation: **pitches** limited to the range **F♭♭ to B♯♯**; and
**keys** limited to *"from C♭ to C♯ majors and their relative minors (A♭ to A♯) such that the diatonic
pitches are limited to single flats/sharps."* Figure 4: the number of transpositions per piece ranges
from **3 to 15**, most pieces at **10–13**. *"This procedure favours pieces with limited
modulations… The more harmonically adventurous pieces are thus also the least numerously
represented."* Transposing sections of a score separately is named as a possible partial remedy and
not done.

### The architecture (§3.4, pages 48–49; Figure 5, page 48)

**[FACT.]** The network *"divides the process of RN analysis into two separate but interconnected
parts."* **The local part (Conv)** is a 1-D DenseNet with a **window size of 2 quarter notes**, which
*"corresponds to the human analyst distinguishing between harmonic and non-harmonic tones, producing
a chordal reduction and deriving the Quality, Inversion, and Root labels."* Its pooling layers *"pass
from the time resolution of the input notes to those of the output chords."* **The global part** is
one of two alternatives: a **non-causal dilated convolution (Dil)** — *"4 layers with 64 kernels each
of size 3 and a dilation of 3ˡ"*, so *"each prediction can use information from a total context of
3⁴ = 81 eighth notes: the present one as well as 40 from the past and 40 from the future"* — or a
**bidirectional GRU** with *"64 neurons per direction"* and *"a dropout rate of 0.3"*. The global part
*"focuses on the more global matters of chord progressions and key selection. The RN analysis
emerges from the structure and pattern of those progressions, expressed in the Key, Degree 1, and
Degree 2 labels."*

**[FACT — §3.4, page 49.]** *"We elected to divide the scores in non-overlapping segments of 80
quarter notes' duration."* Each label is predicted by *"a fully connected layer with softmax
activation, whose size is determined by the number of classes for the label at hand."* The loss is
*"the standard categorical cross-entropy… computed on each of the six target labels separately
before the results are added, with an equal weighting."*

**[FACT — §3.4/§3.5.]** The baseline is **PoolGRU**, *"a standard GRU model without local context
analysis… preceded by pooling layers to reduce the resolution on the time axis"*, trainable in
**global mode only**.

**[FACT — §3.5, page 49.]** Two training modes. *"In the first (global) approach, all six labels are
predicted at the end of the second part (Dil or GRU). In the second (local) method, the Quality,
Inversion, and Root labels are determined at the end of the first, local part of the network and
used to determine the key and degree. As discussed, we did not enforce consistency between
labels."*

**[FACT — §3.5, page 49.]** *"Our best model has about 94,000 trainable weights in total: 33,000 for
the local part, 43,000 for the global, and the remaining 18,000 for the fully connected layers.
Depending on the model, the total training time ranges from 20 minutes to 3 hours, when run on a
CPU-only high-performance-computing server."* Encoded in Python v3.7 using Tensorflow v1.14.

### Fitting and evaluation (§3.5, page 49)

**[FACT, quoted in full because it is what the fit/evaluation reading rests on.]** *"We randomly
allocated 90% of the available scores to the training set, reserving the remaining 10% for
validation. Importantly, we implemented this proportion not only for the corpus overall, but for
each of the corpora individually. For the special case of TAVERN, those works assigned to the
training set included the score and both of the corresponding analyses; pieces in the validation by
contrast included only one of the analyses (randomly selected). In order to provide direct
comparison with Chen and Su (2018, 2019), we also calculated results using only their dataset,
divided in the same way."*

**No third, held-out test set is named anywhere in the paper**, and every figure in §4 is reported on
the validation split. **The split is by SCORE**, so a score is not in both halves. §4.1 states what
was compared on that split: *"we have trained on all possible combinations of the six encodings, the
two architectures (and the baseline), and the two training types (except for PoolGRU, which is only
applicable for global training)."*

### The measured results (§4.1, Tables 5 and 6, pages 49–50)

**[FACT — Table 5, page 49.]** *"Comparison of the percent accuracy between models."* Columns: Key,
Degree, Quality, Inversion, RN. The caption states the two grading conventions: *"'Degree' registers
as correct only when the predictions match the corpus entry for both Degrees 1 and 2; 'RN' is
correct only when all four of the previous columns match in that way."*

| Row, as Table 5 prints it | Key | Degree | Quality | Inversion | RN |
|---|---|---|---|---|---|
| ConvGRU + PSb + global (all data) | **82.9** | **68.3** | **76.6** | **72.0** | **42.8** |
| ConvGRU + PSb + global (Chen & Su's smaller corpus) | 80.6 | 66.5 | 76.3 | 68.1 | 39.1 |
| Chen and Su (2019) | 78.4 | 65.1 | 74.6 | 62.1 | *(none printed)* |
| Chen and Su (2018) | 66.7 | 51.8 | 60.6 | 59.1 | 25.7 |
| Local model after Temperley (1999) | 67.0 | *(none)* | *(none)* | *(none)* | *(none)* |

**Two readings of that table that must not be confused, stated because the second is easy to
mis-cite.** The **first** row is measured on the new meta-corpus; the **second** is the same model
*"reduc[ing] the available data to the smaller corpus used by Chen and Su (2018)"* and is the row
that compares like with like against the two rows below it. And the last row is **the authors' own
baseline built after Temperley (1999)** — the caption calls it *"a baseline key detection using
pitch profiles by Temperley (1999)"* — **not a figure reported by Temperley (1999)**, which is
candidacy row 6 and is not held.

**[FACT — Table 6, page 50.]** *"Results obtained by averaging the accuracy of several models on
four different axes: architecture, input registral information, input spelling, and global/local
training."* The first row of each sub-table is an absolute percentage; **each line beneath it is a
+/− difference from that reference**, and the number beside the name is how many models were
averaged. Transcribed as printed:

| Axis | n | Key | Degree | Quality | Inversion | RN |
|---|---|---|---|---|---|---|
| *(reference)* ConvGRU + PSb + global | | 82.9 | 68.3 | 76.6 | 72.0 | 42.8 |
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

*(The caption states there are only 6 PoolGRU models *"as they can be trained only globally"*.)*

**[FACT — §4.1, pages 49–50, the three statistical statements the paper itself makes.]**
*(i)* *"a t-test on the significance of the difference for the full task (the column 'RN' in Table 6)
yielded a p-value < 10⁻² against the null hypothesis of ConvGRU and PoolGRU giving the same
result."*
*(ii)* *"including the bass information (CPb/PSb) results in markedly higher performance not only in
identifying the correct inversions, but for all of the tasks (again, p-value < 10⁻²)."*
*(iii)* On spelling: *"using full pitch spelling generally leads to slightly higher results overall,
but the results are not statistically significant."* And on local against global: *"The difference in
the total result is statistically not significant. However, when one looks at specific (local)
labels such as the quality, one finds that the differences in the intermediate steps taken by the two
architectures are significant (with a p-value against the null hypothesis smaller than 10⁻⁶)."*

**[FACT — §4.1, page 50, the authors' own reading of the spelling axis.]** *"we must remember that
analyses without pitch spelling cannot distinguish between enharmonically equivalent keys such as G♯
and A♭. As such, the inclusion of spelling means introducing more keys and chord roots and thus
amounts to a more difficult task where proportionately fewer answers will be correct. As pitch
spelling yields performances that are not worse while performing a harder, more musically relevant
task, we conclude that the spelling representation is preferable where the data is available."*

**★ UNCERTAINTY: NO cell in Table 5 or Table 6 carries a ± value, a standard deviation or an
interval.** What the paper does carry is the three p-values above, on three named comparisons. This
is recorded because carried item (e) asks for it: the paper is **not** of row 47's 2021 kind (a
spread on every figure), and it is **not** of the kind that carries no uncertainty statement at all —
it reports significance on the comparisons it draws conclusions from and prints no spread on the
cells. **How many rows of the slice fall on each side is not counted here.** **No
difference is read here as a result where the paper itself declines to call it significant**, which
is why the spelling axis is recorded above in the authors' own words rather than as a measured gain.

### The error analysis (§4.2, pages 50–51; Table 7, page 51)

**[FACT — §4.2, page 50.]** *"more properly, divergences between the input corpus and prediction —
appear to centre on three main types"*:

1. ***Segmentation errors:*** *"differences in the timing of chord changes (see Bach prelude, Table
   7). This appears to be the most common discrepancy. More specifically, we notice that the
   predictions tend to change more frequently than the human analyses, particularly in more complex
   passages. This is presumably on the basis of an attempt to divide the music into small enough
   segments to allow a cleaner reading of the chord in those small spans. **Strategies such as the
   segmenter layer proposed by Chen and Su (2019) may help.**"*
2. ***Mislabeling of rare chords:*** *"the system is highly reluctant to identify secondary/tonicised
   chords or chromatic chords like the augmented sixths, presumably because they are relatively rare
   in the corpus."*
3. ***Alternative readings:*** *"moments where the system opts for a reading that is different from
   that of the validation corpus, but which is nonetheless a perfectly acceptable alternative.
   Corpora with multiple readings of the same music would be especially helpful here because they
   offer the system not a single 'correct' answer, but a list of viable options."*

**[FACT — Table 7, page 51.]** A side-by-side of the corpus analysis and the system output on the
opening of the Bach prelude of Figure 1, discrepancies italicised. The shape of the discrepancy is
visible in the row structure rather than in any single value: the corpus's **m2 ii42, 4.0–8.0**
becomes **four** output rows (4.0–4.5, 4.5–7.0, 7.0–7.5, 7.5–8.0); the corpus's **m3 V65, 8.0–12.0**
becomes **five** (8.0–8.5, 8.5–9.5, 9.5–10.0, 10.0–11.0, 11.0–12.0); and the corpus's **m5 vi6,
16.0–20.0** becomes **three** (16.0–16.5, 16.5–17.0, 17.0–20.0). Each of those three counts is
derived by counting the printed output rows against the single corpus row they face; **no other
count of Table 7 is asserted.** §4.2 gives one further quantification of the same kind, on the
Schubert passage of Figure 3: *"the prediction for measures 34 and 35 is made of four different
chord labels, while in the reference dataset there are only two."*

**[FACT — §4.2, page 50, the fourth class, named apart from the three.]** *"we found some cases we
consider unacceptable readings, where the most compelling machine reading diverges from the
statistically normative case. For example, in Beethoven's sixth sonata (op.10 no.2, Figure 6), the
exposition includes a theme in C major which from measure 41 is repeated in the parallel key of C
minor. Perhaps because this lasts for only four measures, the system is reluctant to identify a full
modulation, preferring instead to remain in C major."*

### Ambiguity as the paper's own subject (§2, pages 44–45; Figure 3 and Table 2, page 45)

**[FACT.]** §2 works one passage — measures 34–35 of Schubert's *Einsamkeit* (D.911 No.12) — into
**three different analyses (A1, A2, A3)**, tabulated in Table 2 against the four preference rules §2
quotes from Tymoczko et al. (2019). The section closes: *"In cases like this, we will all have views
on how to proceed but no one can claim to have the single, definitive, and unequivocally 'correct'
answer."* And earlier, page 43: *"while experienced analysts will generally agree over simple
contexts, their analyses may vary widely for more complex cases. In short, our intuitive notions of
what is 'in' the harmony hides a sophisticated set of judgement calls."*

**[FACT — page 43, the three axes of that ambiguity, printed as a list]:** *"whether and where to
change chords, whether and where to change keys, and which notes in the score should be represented
in the harmonic reduction at all."*

### Future work (§5.1, pages 51–52)

**[FACT.]** *"A simple right/wrong accuracy metric is not the best way to measure the performance of
an RN analysis algorithm, as several different readings are often equally viable. Even taking that
into account, the 43% total accuracy that we report is still far from ideal."*

**[FACT.]** *"the evaluation of output could be improved, perhaps through the definition of relative
distance in functional terms. This would entail a distance metric between chords to write a more
'musically relevant' loss function which considers chords of the same function (such as ii7 and IV)
to be closer to one another than to those of a different function (V7). This could also prove
helpful for cases with multiple annotators, providing a metric for the relative divergence between
those readings."*

**[FACT — a negative result, reported informally.]** *"for the repertoires discussed here, metrical
position, dynamics, texture, and other score indications are also strongly attested to have a
bearing on harmonic analysis. Including those parameters may improve performance, though **informal
testing of metrical strength did not yield significant gains**, and the quality of machine-readable
score encoding often prohibits a serious analysis of parameters like dynamics."*

**[FACT.]** *"Finally, one could also explore a combination of learned and/or deterministic
post-processing to enforce the kind of consistency between labels discussed above. It may be that
approaches combining machine learning, deterministic algorithms, and a human-in-the-loop achieve
results surpassing those accomplished by each of these methods separately."*

**[FACT — §5.1, on the time encoding.]** *"comparisons could include assessing the relative
performance of the 'frame-based' approach with the alternative 'variable length' convention (Oore et
al., 2018). This latter allows representation of arbitrarily short and long time spans and would save
on training time (by virtue of it reducing the total number of entries). It may also better reflect
the human experience of music, which does not proceed in granular units, but centres on the
information density of events and changes."*

## Coupling facts (mandatory)

**What the method ASSUMES about its upstream.**
- A **notated symbolic score** in a format that carries pitch spelling — the paper's own footnote 14
  names **\*\*kern, MusicXML and MEI**, and states that MIDI-based systems are limited to chromatic
  pitch. **Spelling is an input requirement of the best-performing configuration**, not something the
  method infers.
- A **fixed frame grid**: 32nd notes for the input encoding, 8th notes for the output, with the score
  divided into non-overlapping segments of 80 quarter notes and zero-padded.
- **No voices, no ties, no dynamics, no metrical strength.** Repeated and held notes are deliberately
  not distinguished; metrical strength was tested informally and not included.
- For TRAINING: RN annotations in the six-property tabular format, from which all six labels are
  derived.

**What it HANDS downstream.**
- **Six labels per 8th-note frame** — Key, Degree 1, Degree 2, Quality, Inversion, Root — each from
  its own softmax, **with no consistency enforced between them** (§3.5 in terms).
- **No segmentation decision of any kind.** There is no boundary variable, no segment, no
  change/stay decision: a chord boundary exists only where two adjacent frames carry different
  labels. The authors name the resulting over-segmentation as their most common error class.
- **No rivals, no confidence, no posterior.** Six softmaxes exist and nothing is published from any
  of them. **The progress record records the same absence at rows 11, 19, 20 and 18 and at both of
  row 47's papers; those rows are named and no count is asserted**, and their extracts were not
  opened this session.
- **No chord-tone or elaboration output**, although the local part is described as *"the human
  analyst distinguishing between harmonic and non-harmonic tones"*; no figured bass; no cadence; no
  harmonic-rhythm read-off; **no 'no chord' provision at all** (gaps are filled by continuing the
  foregoing chord).

**Its own STATED SCOPE and limits.**
- **Domain:** Western classical RN analysis, 201 scores, four corpora, Mozart to the 19th-century
  song repertoire.
- **Decision scope:** what key, what degree (with tonicisation), what quality, what inversion and
  what root, per 8th-note frame. **Not** where the harmony changes; **not** which notes are
  harmonic.
- **Fitting:** 90 % train / 10 % validation by score, per corpus; **no held-out test set**; every
  reported figure is a validation figure.
- **The authors' own bound on their metric:** *"A simple right/wrong accuracy metric is not the best
  way to measure the performance of an RN analysis algorithm"*, and *"the 43% total accuracy that we
  report is still far from ideal."*

## What an L2 detail specification could adopt, adapt, or must argue against

- **★ MUST ARGUE AGAINST — and this is the paper the record's own argument quotes.** The six
  independently-computed heads with no enforced consistency are exactly DP-A's rival, and this paper
  is where §S4(a) gets its sentence. **What a detail specification must now meet is the paper's own
  argument FOR the division, which the record does not carry:** the division *"reduces the complexity
  of the task"* from a product of about 22 million joint outputs to a sum of 123, and *"improves the
  interpretability of the results."* **Row 47's 2021 paper states the same cost in the
  same terms** — *"enlarges its output vocabulary size"*, of its own 5040-way composite — read at
  that extract itself this session. Whether the slice holds further statements of it is **not
  established here**: the other extracts were not opened. So the record's chosen "no" at DP-A, and
  D-526's scale-degree-valued chord axis, choose the expensive side of a trade-off **two held
  primaries of this lineage state in the same terms**, and the detail specification owes the cost
  argument and not only the coherence argument. Routed to L2's detail specification and to the
  findings surface's DP-A block.
- **★ MUST ARGUE AGAINST — a "before"-shaped rival with NO segmentation decision at all, whose
  authors diagnose the consequence themselves.** DP-C's three-way question is before / with / after.
  This method is further from "with" than any row of the slice so far: there is no boundary decision
  anywhere, only a per-frame label. And §4.2 names the resulting **over-segmentation as the most
  common discrepancy**, points at *"the segmenter layer proposed by Chen and Su (2019)"* — **row
  47's own 2019 paper** — as a possible remedy, and does so on **symbolic classical input**. This is
  a rival's self-report of the failure the chosen "with" exists to prevent. Routed to the findings
  surface's DP-C block and to L2's detail specification, **unmerged** with row 18's finding (3),
  which stays open with the user.
- **A DATUM FOR THE BASS FACTOR (D-449), measured and significant.** The class-plus-bass encodings
  measure *"markedly higher performance not only in identifying the correct inversions, but for all
  of the tasks"* at p < 10⁻²; Table 6's registral axis reads bass **80.8 / 66.6 / 74.3 / 70.1 /
  39.2** against full **−0.7 / −0.9 / −0.6 / −3.5 / −3.7** and class **−0.1 / −0.7 / −0.1 / −4.7 /
  −4.7**. Two things follow: the bass is worth its own channel (D-449's per-event bass factor, row
  19's explicit one-hot bass, row 3's decoded bass chain), and **carrying the bass alongside the
  pitch-class content beat carrying the full register** on inversion and on the whole task. Routed to
  L2's detail specification.
- **A DATUM FOR THE SPELLING CONTRACT (DP-F, D-450, and the L0 "spelling is given" bullet).** Full
  pitch spelling is *"not worse while performing a harder, more musically relevant task"* — the
  difference is **not statistically significant** by the authors' own statement — and their
  conclusion is that *"the spelling representation is preferable where the data is available."*
  **This is a different kind of support for the record's spelling position than V3's** (Temperley
  2002's 83.8 → 87.4 with spelling, called *"cheating"* for a model of perception, row 5): here
  spelling costs a larger label space and pays for itself, and the argument is about what the output
  means rather than about accuracy. Routed to L2's detail specification and beside V3.
- **A DATUM, NOT A CANDIDATE — the two-stage 'local' training mode.** In local mode Quality,
  Inversion and Root are decided at the end of the local part and **used** to determine key and
  degree; in global mode all six come out together. The paper measures the total difference as **not
  significant** while the intermediate labels differ significantly (p < 10⁻⁶). **That is a published
  measurement of exactly DP-B's question shape** — decide part of the chord first, then the tonality
  — on symbolic classical input, and it comes out **inconclusive at the whole-task level**. It is not
  DP-B's own experiment (which is tonality-first, and whose primary is row 27), and it is not offered
  as one; it is recorded so a later reader does not mistake it for one. Routed to the findings
  surface's DP-B block **as a datum with that bound stated**.
- **ADAPT — the authors' own proposal for a function-aware evaluation distance.** §5.1 proposes a
  loss and an evaluation metric under which *"chords of the same function (such as ii7 and IV)"* are
  closer to one another than to *"those of a different function (V7)"*, and names the same metric as
  the way to measure divergence between multiple annotators. That is a published statement of the
  thing principle #21, D-474 and OI-179 are about, from inside the lineage. Routed to measurement
  design.
- **MUST ARGUE AGAINST — the fixed frame grid**, 32nd in and 8th out, against the L1 charter's
  change-point grid; with the authors' own alternative named (*"variable length"*, Oore et al. 2018)
  and left as future work. Routed to the L1 and L2 detail specifications beside rows 19's and 1's
  fixed-grid instances.

## ★ Findings, routed and not applied

**(1) ★ A CORRECTED STRUCTURAL CLAIM ON DP-A's LIVE RECORDED GROUND — THE RECORD'S OWN SOURCE
QUALIFIES THE COST IT IS QUOTED FOR, AND MEASURES NOTHING.** `FRAMEWORK.md` DP-A (lines 671–683)
reads, at the sentence that carries this paper's words:

> *"Those heads are not stages: they sit on one shared encoder and are decided in one pass, and **the
> papers measure what happens when they are allowed to disagree** — 'potential for self-contradictory
> outputs in which the six sub-labels have different ideas about the chord', and a passage genuinely
> ambiguous between two readings drawing an incoherent composite of the two."*

**At the object, three things are true and none of them is in the record.** *(i)* This paper
**measures nothing** about the six heads disagreeing: it reports no figure of any kind for label
inconsistency, anywhere in thirteen pages. *(ii)* Its very next sentence says the problem is *"only
rarely a problem, arising in the particular case of the 'no chord' label used by the ABC dataset
(only)"*. *(iii)* The authors **chose** the division and give a quantified reason for it — 123
against ≈22·10⁶ possible outputs, plus interpretability — so the quoted clause is the declared cost
of a defended design choice, not a pathology the authors report against themselves.

**What follows and what does not.** The word *"measure"* is carried by the same sentence as two items
that are **not** measurements: this quotation, and RNBert's `I`/`vi6`→`I6` example. The other items
DP-A's ground names — the AugmentedNet re-fusion, and the three measured pairs .462→.491, .503→.516
and .762→.859 — belong to the NEXT sentence and to other papers, and `reading_pass/population.md`
V9 records each as verified at its own primary.
**So DP-A's verdict is not moved, no value moves, no rival re-opens, and nothing is amended** — what
is corrected is a structural claim about what this source does. **The exclusion argument would be
stronger, not weaker, stated accurately**: an author who defends the division on a quantified
complexity ground and finds the incoherence rare is a better rival to argue against than one who
merely reports a pathology.

**★ THE GRADING, STATED SO IT CAN BE OVERRULED.** The remedial commission §5's STOP is *"a CORRECTED
structural claim that moves a design-point verdict"*. This line has applied that test once before, at
row 18's finding (3), which was graded a STOP **because it corrected a chosen design point's own LIVE
recorded ground** — and it moved no value either. **This finding is of that same shape: it corrects a
clause of DP-A's live recorded ground.** It is therefore **reported as STOP-shaped, written up here on
its own, and put to the user with this session's close; nothing is applied, and the next act does not
wait on his answer.** Against that grading, and recorded because an excluded reading is evidence about
the choice: what is corrected is a *characterisation of a quotation's source*, not a measured claim,
and DP-A's exclusion rests on four verified figures that this finding does not touch — a reader could
grade it a precision rather than a STOP. **The facts above are the same either way and nothing rests
on the grading.**

**(2) §S4(a)'s SEALED UNIVERSAL IS TRUE OF THIS PAPER — recorded beside row 47's open finding and
NOT merged with it.** `FRAMEWORK.md` §S4(a) line 1553 reads *"Every system from Chen and Su 2018
onward predicts key, primary degree, secondary degree, quality and inversion as separate heads, and
the later ones add root…"*. **This paper is exactly that**: six heads — Key, Degree 1, Degree 2,
Quality, Inversion **and Root** — the root being the addition §S4(a)'s own clause anticipates.
**Row 47's finding (3)** — that the same universal is FALSE of Chen & Su's own 2021 system, which
publishes two outputs — is open with the user and is **neither applied, restated as settled, nor
built on here**. The two are recorded side by side: the universal holds for the lineage's baseline
and fails for one later member of it. Routed to the user's open finding, unmerged.

**(3) THE LINEAGE'S BASELINE ALREADY PROPOSES THE MACHINERY §S4(a) ATTRIBUTES TO ITS SUCCESSORS.**
§S4(a) reads *"Every later system adds machinery to undo the separation"* and names AugmentedNet,
ChordGNN, AnalysisGNN and RNBert. **This paper's own §5.1 proposes it as future work**: *"one could
also explore a combination of learned and/or deterministic post-processing to enforce the kind of
consistency between labels discussed above."* That **strengthens** §S4(a)'s narrative rather than
correcting it — the successors did what the baseline said should be done — and it is recorded because
the record currently reads as though the baseline was unaware of the cost. Routed to the findings
surface's DP-A block.

**(4) NO HELD-OUT TEST SET; EVERY REPORTED FIGURE IS A VALIDATION FIGURE.** §3.5 allocates 90 % of
scores to training and *"the remaining 10% for validation"*, and §4 reports on that split. There is no
third partition. The paper does not claim one, and the split is by score, so no score is in both
halves — but **model selection across the six encodings, two architectures and two training modes was
made on the same data every headline figure is reported over**. **The progress record's own findings
paragraphs record a fit-on-the-evaluation-data concern at rows 5, 8, 19, 20, 30 and 47. Those rows
are named and NO COUNT is asserted**; none of their extracts was opened this session, so nothing is
carried from them here beyond the fact that the record notes them. Routed to measurement design
beside D-097, D-574, principle #20 and D-661.

**(5) THE ANNOTATOR-VARIANCE BIAS THE AUTHORS DECLARE, AND THE ONE THEY DO NOT.** §3.1 states that
treating TAVERN's multiple analyses of one piece as independent *"will surely introduce some bias in
the model"* and accepts it *"relative to the gain in variance"*; and that *"there is a non-separable
correlation between annotators and musical genres"*, since each source corpus focuses on a different
style. **Both are the authors' own words, and both bear on principle #21 and OI-179 from a new
angle:** this is a held, on-repertoire source stating that annotator identity and repertoire are
**confounded in the data itself**, which is a bound on any agreement figure computed across such a
meta-corpus. Routed to measurement design beside D-474, OI-179 and D-500.

**(6) THE PAPER'S OWN THREE-WAY STATEMENT OF WHAT IS AMBIGUOUS IN HARMONIC ANALYSIS.** Page 43 names
the three axes of analytical disagreement — *"whether and where to change chords, whether and where
to change keys, and which notes in the score should be represented in the harmonic reduction at
all"* — and §2 works one Schubert passage into **three** published-quality readings (Figure 3, Table
2) against four preference rules quoted from Tymoczko et al. (2019). **Those three axes are DP-C,
DP-E and DP-D**, named together, in that order, by a source of the record's own lineage. Recorded as
an ENRICHES-shaped datum for all three blocks; **no verdict touched**. Routed to the findings
surface.

**(7) AN INFORMAL NEGATIVE RESULT ON METRICAL STRENGTH, AND WHY IT IS NOT SET AGAINST V5.** §5.1:
*"informal testing of metrical strength did not yield significant gains."* The L1 charter's
metric-strength `[FACT]` rests on V5, which `reading_pass/population.md` line 106 states as
*"Removing metrical-accent features costs about six points of F-measure"*, verified there at Masada
& Bunescu 2019's Table 5, **F-measure 77.6 → 71.2 (−6.4; accuracy 83.6 → 77.7)**, on a semi-CRF with
and without accent-based features — read at that row of `population.md` this session, not from any
summary of it. **The two do not meet**: V5's is a measured ablation inside a model whose segment
features are accent-weighted; this is an unquantified, self-described **informal** test inside a
frame-wise network with no segments at all, reported in a future-work sentence with no experiment,
no corpus split and no figure. **It is recorded as a datum with its bound and is NOT reported as
evidence against V5** — an informal negative carrying no number cannot bear on a measured positive
that carries one. Routed to the L1 and L2 detail specifications beside V5.

**(8) A SECOND-HAND DATUM ON THE UNHELD ROW 6, WITH NOTHING CARRIED OUT OF IT.** Table 5's last row
is *"Local model after Temperley (1999)"*, Key **67.0**, and the caption calls it *"a baseline key
detection using pitch profiles by Temperley (1999)"*. **That is these authors' own implementation
following row 6's method, measured on their corpus — NOT a figure reported by Temperley (1999)**,
which is candidacy row 6, PAYWALL and not held. Nothing is carried out of Temperley (1999) itself.
The datum is that a key-profile baseline built after it measures 67.0 where this paper's own best
model measures 82.9 on the same data. Routed to the row 6 record and to L2's detail specification as
a datum only.

**(9) A BIBLIOGRAPHY-RECONCILIATION DATUM.** `reading_pass/population.md` line 110, inside the V9
row, attributes the .462→.491 figure to *"ChordGNN 2023, Table 1, BPS set … the learned coherence
post-processing of **Micchi et al. 2021**"*. **A Micchi et al. 2021 is not in
`docs/research_papers/BIBLIOGRAPHY.md`** and is not this paper, which is 2020. Whether the record
means a distinct 2021 publication or has mis-dated this one is not establishable from what is held.
Routed to the bibliography reconciliation beside the routed points of rows 3, 10, 11, 18, 28, 29, 30
and 47. **No verdict; the V9 figure itself is ChordGNN's and was verified there.**

**(10) THE LENGTH-TERM QUESTION, ANSWERED: NO LENGTH TERM AND NO LENGTH VARIABLE.** Carried item (d)
asks which of the slice's worked shapes this method has. **It has none of them**: there is no segment,
no duration distribution, no maximum segment length, no change/stay variable and no transition cost —
the output is a label per 8th-note frame and a boundary is wherever two frames differ. It therefore
falls with row 47's two papers in the *model the length not at all* shape, and **within that shape it
is the more extreme member**: row 47's Harmony Transformer at least decides chord changes with a
supervised head, and this method decides nothing about boundaries at all. **The rows are named; no
count is asserted.** Routed to L2's detail specification beside DP-C.

**(11) FIGURE 5's LABEL SIZES AND THE PAPER'S OWN ARITHMETIC BOTH REPRODUCE.** 12 + 4 + 35 + 30 + 21
+ 21 = **123**, and 12 × 4 × 35 × 30 × 21 × 21 = **22,226,400**, which is the paper's *"≈ 22·10⁶"*.
Recorded because it is the one derivation in the paper this reader could close independently, and
because it establishes that Figure 5's boxes and §3.2's sentence are the same six labels. **The
derivation is this reader's; the two printed values are the paper's.**

## Centrality — CENTRAL, and a second independent extraction is OWED

**CENTRAL**, with the ground on which NOT CENTRAL could be argued stated in full so the verdict is
challengeable at this row.

*The ground for CENTRAL.* The commission's test is a paper *"whose claims would carry load in a
detail specification or against a design point"*. **A ratified `[FACT]` rests on this paper**: the
six-sub-labels quotation is carried at DP-A's live recorded ground (line 676) and at §S4(a) (line
1560), and `reading_pass/population.md` V9 attributes it to this paper by page. **Its words are
quoted inside DP-A's own exclusion argument** — whether any other row's words appear inside another
design point's ground was not checked here, so no "only" is claimed. A detail specification arguing
DP-A's chosen "no" must quote it, and — on finding (1) — must now quote it with the two halves the
record omits. That is load, and it is the same footing on which the progress record's centrality
column records rows **5, 8, 10, 11, 18 and 19** as CENTRAL: in each of those six a ratified `[FACT]`
rests on the paper. The six are derived by reading that column, and no other count is asserted.

*The ground on which NOT CENTRAL could be argued.* None of the other items DP-A's ground cites — the
AugmentedNet re-fusion and the three measured pairs — is this paper's; the quotation is a report, not
a measurement, and this read has just established that the paper measures nothing about it. Its architecture is a frame-wise multi-head network with no
segmentation, no rivals and no confidence — nothing an L2 detail specification would adopt as
machinery. And the pass has already verified V9 at its five primaries, so the figure work is done.
**Against that:** the quotation IS the first item of DP-A's exclusion argument, and a correction to
how the record characterises its source is exactly the class of claim a detail specification carries.
**CENTRAL is chosen on the ratified-`[FACT]` ground, which is the ground the six rows named above
were graded CENTRAL on.**

*What follows.* **A second independent extraction is OWED**, by the original commission's §4 rule and
by its two routes, joining the owed second passes the progress record's "What is NOT done" section
names — rows 27, 28, 1, 8, 26, 30, 5, 10, 11, 19, 20 and 18, **twelve**, derived by counting that
sentence's own list. The verdict is challengeable at the progress record.

## What this extract does NOT do

It amends no document. It moves no verdict in `reading_pass/candidacy_upgrades.md`, no placement in
`cowork_l2_task_b_slice_derivation_2026_09_05.md`, no design point in `FRAMEWORK.md` — live or
sealed — no row of `reading_pass/population.md` and nothing in
`cowork_reading_pass_findings_2026_08_31.md`. It writes no open-items row and no decisions-register
entry. It lifts no gate: Ruling 1 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps *no
derivation before L2's slice of Task B is read*, and 20 of the 36 rows are still unopened after this
row. **Row 18's finding (3) and row 47's two corrected structural claims are open with the user and
are neither applied, restated as settled, nor built on here**; where this row's own text bears on
them it is recorded beside them, unmerged (findings (2) and the second bullet of the adopt-or-argue
section). It fetches nothing: the four source corpora, the authors' GitLab repository at
`https://gitlab.com/algomus.fr/functional-harmony`, the Dezrann viewer, and every one of the works
this paper cites — Chen & Su 2018 and 2019, Tymoczko et al. 2019, Tymoczko 2011, Devaney et al. 2015,
Neuwirth et al. 2018, Temperley 1997 and 1999, Krumhansl & Kessler 1982, Madsen & Widmer 2007, Robine
et al. 2008, Nápoles López et al. 2019, Pardo & Birmingham 2002, Rocher et al. 2009, Illescas et al.
2007, Kröger et al. 2008, Harasim et al. 2018, Rohrmeier 2011, De Haas et al. 2009, Sapp 2005,
Lerdahl & Jackendoff 1983, Schenker 1935, Ju et al. 2017 and 2019, Hadjeres et al. 2017, Liang et al.
2017, de Clercq & Temperley 2011, Huang et al. 2016 and 2018, Cho et al. 2014, Yu & Koltun 2015, Oord
et al. 2016, Oore et al. 2018, Briot et al. 2020, Cuthbert & Ariza 2010, Giraud et al. 2018,
McFee & Bello 2017, Paiement et al. 2005, Steedman & Longuet-Higgins 1971, Holtzman 1977, Duinker
2019, Cohn 1999 and 2012, Cross 1997, Lewin 1987, Euler 1739, Heinichen 1711, Oettingen 1866,
Schoenberg 1954, Clendinning & Marvin 2016 and Laitz 2016 among them — **were not fetched and are not
read; only the held file was.**

---

*Provenance: Cowork, 2026-09-06, the twelfth reading session of L2's slice, booted on
`cowork_handoff_entry_one_hundred_and_twenty_seven.md` at tip
`911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb` (both ref files read with the file tools). Read before
this extract: the ordinary session-start read (`CLAUDE.md` whole, loaded by the harness;
`DECISIONS.md` whole, 862 lines; `STATUS.md` whole; the derived gating answer — 244 open, 219
gating, 25 non-gating, and the `gating_ids` list whole); the hundred-and-twenty-seventh handoff
entry whole; the hundred-and-eighteenth entry whole for its bridge-fault section;
`reading_pass/l2_slice_reading_progress.md` whole; `reading_pass/candidacy_upgrades.md` whole;
`cowork_reading_pass_commission_2026_08_30.md` whole and
`cowork_reading_pass_remedial_commission_2026_08_31.md` whole;
`cowork_l2_task_b_slice_derivation_2026_09_05.md` whole; `docs/research_papers/BIBLIOGRAPHY.md`
whole; the row 47 (2021) extract at its heading list, banner, identity, coupling facts,
adopt-or-argue, first two findings, centrality and closing sections, for the form; `FRAMEWORK.md` at
DP-A and the design-point opening (lines 665–704) and at §S4(a) (lines 1548–1577);
`reading_pass/population.md` at its verification rows V3 to V13; and
`cowork_reading_pass_findings_2026_08_31.md` at its V9 lines. The staged tree was searched by `Grep`
before extracting, in the order recorded in the banner, bare words as well as phrases. The held PDF
was read as page images, all thirteen pages. Every file was read with the file tools from
bridge-staged copies; no shell read repository content or any staged copy of it. No figure of this
project's own measurement is restated (#17f, D-431); every arithmetic derivation in this file states
that it is this reader's and names the printed values it is derived from.*

# Ju, Howes, McKay, Condit-Schultz, Calvo-Zaragoza & Fujinaga 2019 — "An Interactive Workflow for Generating Chord Labels for Homorhythmic Music in Symbolic Formats" — SECOND INDEPENDENT EXTRACT

> **STATUS: READING-PASS EXTRACT, SECOND PASS. NOTHING HERE IS RULED.** Written 2026-09-19 by the Cowork
> session that booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred.md`, under the
> second-pass rule of `cowork_reading_pass_commission_2026_08_30.md` §4 **as handoff entry 169 §3 quotes
> it** (a CENTRAL source is extracted in a second independent pass and the two extracts cross-checked)
> and the eight-step order of that same §3, as amended at its naming point by Ruling 2 of entry 186 §2.
> **This session did not open the commission itself**; the form below follows entry 169 §3 step 3 and
> the form of row 35's second extract, which was read for that purpose (§0). **The paper is Task B,
> L2's slice, row 58** — the row number is the progress table's
> (`reading_pass/l2_slice_reading_progress.md`, line 110); the candidacy file that table takes its row
> numbers from was not opened by this side. Held file:
> `docs/research_papers/ju_et_al_2019_ismir_interactive_workflow_chord_labels.pdf`, 782,959 bytes at a
> listing of `docs/research_papers/` and at this session's staging call; it is the one file name in that
> listing that carries this paper's first author, year and title words. **8 pages, established at the
> tool** by a deliberately out-of-range request (pages 40–41 refused with "PDF has 8 pages"). Read whole
> in one request, pages 1–8; **the eight page images were present** (checked at the images, not at the
> call's success line).
>
> Page numbers below are the PDF's own (1–8). The pages print 862 to 869 at their feet, so PDF page *n*
> is printed page 861 + *n*.

## §0 — Declarations of independence and its bound

- **What this side read before opening the paper, that bears on it:** the progress table was searched,
  not read. Five searches were run over it *(★ CORRECTED at the user-ordered check, §10. FORMER WORDING,
  PRESERVED (#12): "Three searches were run over it" — two were left out, the two that returned only
  bare cells)*: one returned each table row's row-number cell and its
  second cell where the line was short enough to be shown; one returned each table row's row-number
  cell with up to 90 characters after it; one returned each line's text around the words "OWED" and
  "owed", up to 60 characters either side; one returned bare *"| OWED |"* cells for some lines and one
  returned a bare *"|"* for some lines, neither with other text. **Of row 58's line (line 110) this side therefore saw two
  strings.** The first is the opening of its identity cell: the six authors' surnames and *"— the held
  file, printing on p"*. The second is the tail of its centrality cell and its "Second pass" cell:
  *"the two experiments — is stated in full in the extract) | OWED (flips to not owed if the user takes
  the NOT CENTRAL read"* (cut at both ends by the search). **So this side knew, before opening the
  paper, that the first extract states a ground on which the paper could be read as not central, that
  its author did not take that reading, and that the cell's last words before the dash are "the two
  experiments".** It did not know what any finding says or how many there are. The same searches
  returned fragments of the same kind for the other rows of the table; this side met this paper's name
  in none of the fragments it saw.
  `docs/research_papers/BIBLIOGRAPHY.md` was opened at one line, line 82, which is this paper's row
  (*"Ju et al., "An Interactive Workflow for Generating Chord Labels…," ISMIR 2019"*, a URL, a check
  mark, and a last cell reading CC). The bibliography's column headings were not read.
- **Name-only look-up, declared under Ruling 2 (entry 186 §2):** `reading_pass/extracts/` was listed by
  file name at boot, to verify two other extracts' sizes, and that listing was reused to find the first
  extract's name:
  `ju-howes-mckay-conditschultz-calvozaragoza-fujinaga-2019-an-interactive-workflow-for-generating-chord-labels.md`
  (85,207 bytes, modification time 1789203100034). **It was not opened before §9.** The file name
  carries authors, year and the paper's own printed title, which the paper supplies. Its size says the
  first extract is long; nothing else was taken from it.
- **Contamination from the record's own text, beyond those strings:** of the records read at boot (entry
  200 whole; entries 186 and 169 whole; 188 at §4–§5; 198 at §7; 152 at its lines 55–69; 118 at its
  lines 27–86; `CLAUDE.md` at its six spans; `DECISIONS.md` whole; `STATUS.md` whole; the gating
  answer's identity list), none summarizes this paper's content; entry 200 §3 names row 58 by its six
  authors. **Four index lines of the decisions register, read at boot, bear on the paper's SUBJECT and
  not on the paper**, and are named because a reader who knows them may read this paper with them in
  mind: D-527 (this project has no live stage that removes non-chord tones; each tone is emitted by
  category inside the one decode); D-023 with the register's own definition of *slice* (a span during
  which exactly the same notes sound, beginning when any note starts **or stops**); D-294 (the one
  ground truth is the human annotation, and no self-annotation enters a measurement); and D-501 (a
  written chord symbol is read as a comparison label and not as analyzer input). No memory tool call
  was made in this sitting. The listing of the user's Cowork memory store that the system delivers at
  session start shows, by one-line description alone, a file about a deferred design analysis of
  non-chord-tone detection in this project; **it was not opened.** `FRAMEWORK.md`, `population.md`, the
  findings surface, the slice derivation and the candidacy file were **not** opened.
- **Row 35's second extract was read for its form** — its lines 1–112 (banner, §0, §1 and the opening
  of §2) and its section headings by search. **This paper's reference [11] names that paper's four authors and its title**, at a different venue
  from the one row 35's held file prints *(★ CORRECTED at §9.5. FORMER WORDING, PRESERVED (#12): "That
  paper is this paper's reference [11]" — wider than the page: [11] cites a workshop proceedings, pages
  13–16, and the held file prints a two-page late-breaking text)*, and it
  shares three authors with this one (Ju, Condit-Schultz, Fujinaga). From those lines this side knows
  that paper's identity, that it calls itself a demo, and that it concerns identifying non-chord tones
  with a neural network. Nothing about row 35's paper is used below except where this paper itself
  cites [11].
- **General knowledge is the larger contamination and is named as such:** this side knows support vector
  machines, feedforward neural networks, the ADAM optimizer, cross-entropy losses, k-fold cross
  validation, Student's t-test, voting ensembles, the Humdrum `**kern` format and the music21 toolkit
  from outside this repository, and cannot exclude having met this paper in training. **Mechanism statements
  below are therefore located to a page, a section, a figure, a table or a footnote**, and a statement this side could make from general
  knowledge but could not find on a page is written as ABSENT (§7), not as a fact.
- **What this file is not:** it is not a record-facing extract. What `FRAMEWORK.md` or any design point
  says about this paper, and the paper's centrality verdict, are the first extract's half and are not
  re-derived here (entry 169 §5(vii)).

## §1 — Identity, checked at page 1

- **§1.1 Title, as printed:** *"AN INTERACTIVE WORKFLOW FOR GENERATING CHORD LABELS FOR HOMORHYTHMIC
  MUSIC IN SYMBOLIC FORMATS"* (page 1, head, in capitals over two lines). The attribution box at the
  foot of page 1 prints it in mixed case: *"An Interactive Workflow for Generating Chord Labels for
  Homorhythmic Music in Symbolic Formats"*.
- **§1.2 Authors and affiliations, as printed (page 1):** Yaolong Ju (1), Samuel Howes (1), Cory McKay
  (2), Nathaniel Condit-Schultz (3), Jorge Calvo-Zaragoza (4), Ichiro Fujinaga (1). (1) Schulich School
  of Music, McGill University, Canada; (2) Department of Liberal and Creative Arts, Marianopolis
  College, Canada; (3) School of Music, Georgia Institute of Technology, USA; (4) Department of Software
  and Computing Systems, University of Alicante, Spain. Six e-mail addresses are printed beneath.
- **§1.3 Venue, as printed:** attribution box, foot of page 1, left column: *"20th International Society
  for Music Information Retrieval Conference, Delft, The Netherlands, 2019."* The same box prints a
  Creative Commons Attribution 4.0 International License (CC BY 4.0) in the six authors' names. Pages 2
  to 8 carry the running head *"Proceedings of the 20th ISMIR Conference, Delft, Netherlands, November
  4-8, 2019"*. Printed pages 862–869.
- **§1.4 Match to the bibliography row:** the row (line 82) gives *"Ju et al."*, the title shortened with
  an ellipsis after *"Chord Labels"*, and *"ISMIR 2019"*. The printed title matches as a prefix; the
  first author matches; the venue and year match. The row's last cell reads CC and the page prints a
  CC BY 4.0 licence. This side did not read the bibliography's column headings, so what that cell grades
  is not stated here. **No identity finding.**
- **§1.5 Length and structure:** 8 pages, of which page 7 carries the acknowledgement and references [1]
  to [21], and page 8 carries the running head, references [22] to [24] and the page number, and nothing else. Sections as printed:
  Abstract; 1 Introduction and Basic Methodology; 2 Details of Methodology (2.1 Input Data Encoding and
  Processing; 2.2 Input Features; 2.3 Rule-Based Algorithms; 2.4 Machine Learning Algorithms); 3
  Experiments (3.1 Data; 3.2 Experiment 1, with 3.2.1 and 3.2.2; 3.3 Experiment 2, with 3.3.1 and
  3.3.2); 4 Discussion; 5 Conclusion and Future Research; Acknowledgement; 6 References. Figures 1 to 5
  (pages 1, 3, 4, 4 and 6); Tables 1 and 2 (page 5). Twelve footnotes, numbered 1 to 12 (pages 2, 3, 4
  and 5). No numbered equation was met in the pages as read. Twenty-four references.

## §2 — Claims, labeled

The label NAMES are the commission's as entry 169 §3 step 3 carries them; the definitions that follow
are worded as row 35's second extract words them at the head of its §2, and the commission's own wording
was not opened. **FACT** = stated or measured in the paper, with its location; **THEORY** = established
published theory the paper invokes; **CONJECTURE** = the paper's own speculation, or a claim it makes
without a measurement or a citation. Quotations are verbatim from the page as rendered, printed slips
included.

### §2.1 The problem the paper sets, and its headline claim (Abstract and §1, pages 1–2)

- **[FACT — the paper's statement of its problem]** Abstract, page 1: *"Automatic harmonic analysis is
  challenging: rule-based models cannot account for every possible edge case, and manual annotation is
  expensive and sometimes inconsistent, undermining the training and evaluation of machine learning
  models."*
- **[FACT — the headline, as the Abstract prints it]** *"First, a rule-based model was used to generate
  preliminary, consistent chord labels in order to pre-train three machine learning models. These four
  models were grouped into an ensemble that generated chord labels by voting, achieving 91.4% accuracy
  on a reserved test set. A domain expert then corrected only those chords that the ensemble did not
  agree on unanimously (20.9% of the generated labels). Finally, we used these corrected annotations to
  re-train the machine learning models, and the resulting ensemble attained an accuracy of 93.5% on the
  reserved test set, a 24.4% reduction in the number of errors."* **Which cells of Table 2 these three
  percentages come from is worked at §4.4; they do not come from one classifier family.**
- **[FACT — the paper's definition of its task]** §1, page 1: *"In general, harmonic analysis refers to
  the identification of harmonies from the musical surface."*
- **[THEORY invoked, uncited beyond names]** §1, page 1: *"many prominent music theorists (e.g., Rameau,
  Riemann, Schenker) have proposed different approaches to harmonic analysis. This means it is often
  possible to analyze the same passage in numerous legitimate ways."*
- **[FACT — the paper's two named styles]** §1, page 1: *"some analysts prefer interpretations with
  fewer chords, while others prefer interpretations with more frequent harmonic changes. We characterize
  these general strategies as "melodic" and "harmonic", respectively"*. Figure 1 (page 1) sets the two
  under one four-voice passage of two bars in one sharp and common time, with a third line called
  *"Mixed"*. As read from the rendered image (small glyphs; the alignment of labels to beats was not
  measured): Melodic, seven labels — G, D7, Em, Am, G, A, D; Harmonic, thirteen labels — G, Em7, D, D7,
  C, Em, Am, F#o, G, GM7, A, A7, D; Mixed, nine labels — G, D7, Em, Am, F#o, G, A, A7, D. Caption: *"A
  passage with important differences between melody-oriented (blue) and harmony-oriented (red) analyses.
  The final analysis (black) mixes the two styles. Such inconsistencies are quite common, even between
  expert analyses."* The last sentence of the caption carries no citation at its site.
- **[FACT, cited]** §1, page 1: *"analysts often disagree, and are not always internally consistent
  [12]."* Reference [12] is Koops et al., *Journal of New Music Research* 48, 2019, whose printed title
  concerns annotations of popular music.
- **[FACT — the paper's account of the two existing approaches, with its citations]** Page 2, left
  column. Rule-based models, citing [4, 8, 10, 21–23]: *"Although these approaches generate chord labels
  that are internally consistent, they often fail to produce correct analyses for even moderately
  exceptional passages, as it is extremely complicated to define rules that are comprehensive enough to
  account for all possibilities."* Manual annotation, citing [2, 5, 6, 9, 16, 17], used to train machine
  learning models, citing [3, 11, 14, 15, 18, 20, 24]: *"manual harmonic annotations require an enormous
  amount of time and expertise, and can be inconsistent [12], which may undermine a ML model's
  effectiveness, especially when limited amounts of training data are available."* Neither sentence
  carries a measurement at its site.
- **[CONJECTURE — the generality claim]** Page 2, right column: *"This workflow is not limited to Bach
  chorales. With an adapted RB model (Model 4 in Fig. 2), it can easily be applied to other genres of
  music in a fully automatic way (ending with Analysis 1) or interactively if an expert analyst is
  available (ending with Analysis 3)."* The experiments are on Bach chorales (§3.1); no other repertoire
  is measured in the pages as read.
- **[FACT]** Page 2, right column: source code, data and results are said to be at a shortened URL
  (`https://bit.ly/2QUdGwH`). This side followed no URL.

### §2.2 The workflow, in the paper's four steps (§1, page 2; Figure 2, page 3)

- **[FACT]** Step 1: *"we use an existing RB model [4] to generate preliminary, consistent chord labels
  according to a particular analytical style."* Reference [4] is Condit-Schultz, Ju & Fujinaga, ISMIR
  2018.
- **[FACT]** Step 2: *"These analyses are used to pre-train three ML models, which together with the RB
  model form an algorithm ensemble, where each model within the ensemble labels all the chords. The
  most-preferred chord labels are then output as Analysis 1."* Footnote 3 (page 2), whole: *"If there is
  a tie, prefer the label for which the rule-based algorithm voted."*
- **[FACT]** Step 3: *"a human expert examines only those chords for which the ensemble did not agree
  unanimously, and corrects them as needed. We call this process "partial manual modification"."* The
  corrected result is *Analysis 2*. Figure 2 shows Analysis 2 as the join of *"Original unanimous
  analyses"* and *"Manual analyses"*: the labels the four models agreed on pass into Analysis 2
  unexamined.
- **[FACT]** Step 4: *"we re-train the ML models. The most-preferred chord labels from the new ensemble
  are chosen as the final chord labels (Analysis 3)"*. In Part 2 of Figure 2 the rule-based model stays
  in the ensemble, fed by the symbolic data and not by Analysis 2.
- **[FACT]** Page 2: *"This paradigm of manually modifying the generated data and re-training the ML
  models is known as "interactive machine learning" [1,7]."*
- **[FACT — the three trainable models, Figure 2's caption, page 3]** *"Models 1 and 2 both use a machine
  learning algorithm (MLA) to identify and remove non-chord tones (NCTs). After this, Model 1
  (MLA-NCT+H-CL) uses a heuristic (H) algorithm and Model 2 (MLA-NCT+MLB-CL) uses a ML algorithm (MLB)
  to infer chord labels (CL) from the remaining chord tones. We term this process "NCT-first harmonic
  analysis" … Model 3 (MLC-CL) uses a single ML algorithm (MLC) to infer chord labels (CL) directly from
  the pitch-class collections, without removing NCTs. We term this process "direct harmonic
  analysis""*. Figure 3 (page 4) pictures the two routes side by side on one passage.

### §2.3 The input, the label and the slice (§2.1, page 2; Figure 4, page 4)

- **[FACT]** Input format: *"The workflow currently accepts music encoded in Humdrum's \*\*kern symbolic
  representation. Any other formats that can be faithfully converted to \*\*kern can also be used."*
- **[FACT — the label vocabulary]** *"Each chord label consists of the letter-name of the root and the
  quality of the chord (e.g., C major). Triads can be major, minor, or diminished; and seventh chords
  can be major, minor, dominant, half-diminished, or fully diminished. Functional Roman numerals are not
  used, and chordal inversions are not specified."* That is three triad qualities and five seventh-chord
  qualities. The number of distinct labels that results is not printed (§7).
- **[FACT — the unit]** *"Chord labels are appended to the original \*\*kern file for each chorale and
  aligned with the music as "onset slices" [11,13] … An onset slice is formed whenever a new note onset
  occurs in* any *musical voice, and consists of a list of all pitch classes sounding at that moment."*
  Figure 4's caption (page 4): *"Any note sustained from a previous slice becomes an "artificial onset"
  in the new slice (right, circled)."* **The cut is at note onsets; a note's release is not named as a
  cut point in the pages as read.**
- **[FACT — transposition]** *"all chorales and corresponding chord labels were transposed to the same
  key to make the tonal relationships between pitch classes consistent across the dataset."* Footnote 4,
  whole: *"The built-in key transposition function from music21 was used, with the Aarden-Essen key
  profile (https://bit.ly/2FSIwQY). Chorales were transposed to C major or A minor depending on their
  mode."* So the key of each chorale is estimated by a profile method before anything is learned; that
  it is one key for a whole chorale is this side's reading of *"Chorales were transposed"*, not a
  sentence on the page. The paper names the key-finding as a limitation (§2.7).

### §2.4 The features (§2.2, pages 2–3), whole, as printed

- **[FACT]** *"Each onset slice is mapped to a feature vector for processing by Model 1, Model 2, and
  Model 3 of the workflow."*
  1. *"**PC12** : A 12-D binary vector of enharmonic pitch classes present in the slice."*
  2. *"**M**: A 3-D indication of the metrical context of the slice (down-beat, on-beat, off-beat)."*
  3. *"**O**: A 12-D vector indicating which PC12 pitch classes are real onsets and which are artificial
     (see Fig. 4)."*
  4. *"**Wn**: A variable size vector containing the (non-Wn) features from the n previous and following
     slices (e.g., W1 indicates that features for the directly preceding and directly following slices
     are included in the features of the current slice). These surrounding slices are called "contextual
     windows"."*
- **[FACT]** Footnote 5: *"A multi-label one-hot schema was used to encode the features as inputs for the
  ML algorithms."* Page 3: *"a "PC12M" configuration indicates a 15-D vector, with O and Wn features
  omitted."*
- **What the three metrical values mean is not defined in the pages as read** (§7). The spelling of a
  pitch is not among the features: PC12 is over *"enharmonic pitch classes"*.

### §2.5 The rule-based model and the learners (§2.3 and §2.4, page 3)

- **[FACT]** *"We use an existing RB model [4] to generate preliminary chord labels (Model 4 in Fig. 2).
  This tool is publicly accessible online."* (footnote 6, a URL). *"A "harmonic" rather than "melodic"
  style of analysis is used (see Fig. 1), which prefers more chord changes and fewer non-chord tones
  (NCTs) [19], and is better-suited to the typical chorale texture."* This side met no measurement
  behind the last clause in the pages as read; reference [19] is Quinn 2010. The specific heuristics of the style, and the heuristic
  algorithm H-CL of Model 1, are each given as a URL and not in the text. **So the rules that produce
  the pre-training labels are not on these pages.**
- **[FACT]** *"MLA treats NCT identification as a multi-label problem; the output of MLA is a
  12-dimensional vector specifying which pitch classes are both present and identified as NCTs; MLB and
  MLC treat chord labeling as a multi-class problem; they output similar vectors identifying the
  predicted chord label among all candidates."*
- **[FACT]** *"We tested Support Vector Machines (SVMs) and Deep Neural Networks (DNNs) as MLA, MLB, and
  MLC classifiers. For DNN, we used three hidden layers, each with 300 hidden units. Adaptive Moment
  Estimation was used as an optimizer, with loss functions of binary cross-entropy for MLA and
  categorical cross-entropy for MLB and MLC. SVM used a linear kernel function."*

### §2.6 The data and the two experiments' designs (§3.1, §3.2.1, §3.3.1, pages 3–4)

- **[FACT]** Data: *"a modified dataset of Bach chorales originally produced by Craig Sapp. This modified
  dataset consists of 369 chorales."* Footnote 7: *"Some corrections were made to the music and Chorale
  150 was added to the dataset. Chorales 130 and 316 were excluded, since the original \*\*kern files
  and the music21-parsed results are different."*
- **[FACT — the reserved test set]** *"39 chorales were randomly chosen before the experiments began and
  partitioned into a set reserved for final testing in Experiment 2. These reserved chorales had their
  chords hand-labelled in their entirety by a human expert."* 369 − 39 = 330, and the paper prints 330.
- **[FACT — what the 330 are labeled with]** *"The initial "ground truth" for these remaining 330
  chorales consisted of the labels predicted by the RB model (Model 4), which was found to be quite
  effective, if not perfect [4]. This imperfect "ground truth" was used in Experiment 1"*. The paper
  puts *ground truth* in quotation marks in both of these sentences and in Table 1's caption; §3.2.2's
  *"imperfect ground truth"* and §3.3.2's *"artificial ground truth"* are printed without them.
- **[FACT — Experiment 1's design]** Ten-fold cross-validation on the 330. For the DNN, folds of 80 %
  training, 10 % validation, 10 % internal testing; for the SVM, 90 % training (*"the union of the DNN
  training and validation sets"*) and 10 % internal testing, *"matching the DNN internal test sets"*.
  With W features, *"n was set to 1 for MLA and MLC, and to 2 for MLB (represented as W1/2)."* Both the
  training labels and the labels the accuracies are graded against are the rule-based model's.
- **[FACT — Experiment 2's design]** Pre-training on the rule-based labels as in Experiment 1. For the
  DNN, 90 % of the 330 for training and 10 % for validation, in *"a cross-validation-like training
  scheme"*: *"we conducted 10 experiments by training 10 models with rotated training and validation
  folds, while the testing fold (39 reserved chorales) remained the same. All 330 non-reserved chorales
  were used to train each of the SVM classifiers. Only the PC12MOW1/2 input features … were used in
  Experiment 2."* Then: *"the human expert manually corrected only those chords that the ensemble did
  not agree on unanimously. The corrected labels (Analysis 2) were then used to re-train Models 1, 2,
  and 3. The 39 manually-labelled reserved test chorales were then used to test the original pre-trained
  models, and then the re-trained models."*

### §2.7 The paper's own reading of its results, and its stated limits (§3.2.2, §3.3.2, §4, §5; pages 4–6)

- **[FACT with a test]** §3.2.2: *"The highest classification value of 90.1% was achieved by Model 2
  using PC12MOW1/2 input features. Results show that the addition of a small contextual window (feature
  Wn) improved the performances of Model 2 and Model 3 significantly."* Footnote 9: *"p<0.05 in
  Students' t-tests comparing all Model 2 and 3 accuracies for PC12 and PC12M with those of PC12W1/2 and
  PC12MW1/2."* Model 1 is not named in that sentence or that footnote.
- **[THEORY invoked, uncited]** *"This reflects the general music theoretical understanding that, in
  cases of ambiguous harmony (e.g., an incomplete chord), a chord's immediate context is essential to
  label it properly."*
- **[FACT — the paper's own bound on Experiment 1]** *"these Experiment 1 findings are based on imperfect
  ground truth (see Section 3.1), and so must be interpreted more as preliminary indications rather than
  as confirmed truth."*
- **[FACT]** §3.3.2: *"the original RB algorithm (Model 4 in Fig. 2) attains a chord accuracy of 90.7%,
  which serves as our baseline. The highest accuracy obtained by the pre-trained ensemble is 91.4%,
  using PC12MOW1/2, SVM classifiers, and voting."*
- **[CONJECTURE, marked as such by the paper's "perhaps"]** *"It is of interest that CAVote here is
  higher than CA4, even though the classifiers in CAVote were trained on the RB output; this is perhaps
  because the RB model is overfitting the theoretical model underlying it, and that the pre-trained
  ensemble trained on it may in fact be smoothing out some of this overfitting to result in a slightly
  more general model."* This side met no measurement in the pages as read that tests this explanation. The rule-based model is
  itself one of the four voters in CAVote (Figure 2), which the sentence does not mention.
- **[CONJECTURE]** *"A comparison of Table 1 and Table 2 indicates that the Table 1 performance with
  artificial ground truth is quite similar to the performance of Table 2 pre-trained classifiers on the
  proper test set; this encouragingly suggests that there is little or no overfitting."* The two tables'
  values for the same feature set are set side by side at §4.3.
- **[FACT with a test]** *"Table 2 also shows that performance improved after re-training in most
  cases."* Footnote 10: *"p<0.05 in Students' t-tests comparing results before and after re-training for
  CA1, CA2, CA3, and CAVote, but not PUA."* The footnote does not say which classifier family it covers;
  Table 2 prints no spread for the SVM rows.
- **[FACT with a test]** *"The best-performing configuration attains an accuracy of 93.5%, using voting
  DNNs trained on PC12MOW1/2 features."* Footnote 11: *"p<0.05 in Students' t-tests comparing results of
  CAVote to CA1, CA2, CA3, and CA4."*
- **[FACT, derived by the paper]** *"the expert analyst is only required to provide manual analyses for
  about 20.9% of all slices."* Footnote 12, whole: *"This value is inferred from Table 2: 100% - PUA."*
  **Table 2's caption says its values are on the reserved test set. So the 20.9 % is a test-set figure
  — on footnote 12's own reading of PUA (§4.2), the share of test-set slices on which the four models
  were not unanimous. The share of slices the expert examined in the 330 chorales that were corrected
  is met nowhere in the pages as read** (§4.4, §7). *(★ CORRECTED at the user-ordered check, §10. FORMER
  WORDING, PRESERVED (#12): "So the 20.9 % is the share of test-set slices on which the four models were
  not unanimous; the share of slices the expert examined in the 330 chorales that were corrected is not
  printed" — firmer than §4.2 allows, which records two readings of PUA and resolves neither.)*
- **[FACT — §4's own chain of the three accuracies, page 5]** *"It was found that quite good performance
  could be achieved with our rule-based model (90.7% on the reserved test data), that performance could
  be improved slightly using the RB model to self-train a classifier ensemble (91.4% on the test data),
  and that still greater improvements resulted from partial manual modification and re-training (93.5%
  on the test data)."* And, after the fractional reductions below: *"Of particular importance, the first
  two approaches require no human intervention, and the third requires much less expert labor than full
  manual annotation."*
- **[FACT — §4's fractional error reductions]** *"they represent meaningful fractional decreases in the
  error rate (drops of 7.5% comparing pre-trained CAVote to RB, 30.1% comparing re-trained CAVote to RB,
  and 24.4% comparing re-trained CAVote to pre-trained CAVote)."* Preceded by: *"Although these
  improvements may seem small in absolute terms, they are statistically significant"*. Worked at §4.4.
- **[FACT — Figure 5 and the paper's reading of the errors, page 6]** Figure 5 shows bars 9 to 12 of BWV
  315 (*"Gib dich zufrieden und sei stille"*), 24 onset slices, labeled by a DNN-based ensemble with
  PC12MOW1/2 features, with a last column *"No. of Errors"*. As read from the rendered image (small
  glyphs): the rule-based model 2; pre-trained Models 1, 2 and 3: 7, 8 and 8; Analysis 1: 5; re-trained
  Models 1, 2 and 3: 6, 4 and 6; Analysis 3: 1. **In this excerpt the pre-trained ensemble's Analysis 1
  has more errors than the rule-based model alone (5 against 2).** §4: *"Upon examining the errors, we
  find that some of them are reasonable alternative versions of the ground truth: chords with the same
  roots, but with or without an added seventh (slices 1, 11, 17, and 19); or chords that are subsets of
  the ground truth chords (slices 20 and 21). … We still count them as mistakes, however, because
  consistency in analytical style is one of the goals of this work."* How common such errors are across
  the test set is not measured in the pages as read.
- **[FACT — three limitations the paper names, §5, page 6]** (i) *"music21's automatic key-finding may
  not be ideal for our dataset (early tonal music), and may have resulted in reduced performance due to
  faulty transpositions. Instead of transposing all chorales to the same key, a better, but more
  complicated solution would be to augment our data by transposing all chorales to all 12 possible
  keys."* (ii) *"the RB model can be improved to include chords of other qualities (e.g.,
  augmented-sixth chords)."* (iii) *"the ground-truth annotations were prepared by a single expert
  annotator, and it would be better to repeat this process using annotations from multiple experts."*
- **[CONJECTURE — future work, §5]** Other analytical styles *"can be done simply by specifying different
  heuristics in the RB model"*; homophonic music *"poses a challenge to our RB model because more
  individual onset slices are harmonically ambiguous, requiring larger contextual windows to correctly
  interpret the harmony"*; and *"we will investigate training and evaluation protocols that permit
  multiple valid chord labels per slice."*

## §3 — Coupling facts (mandatory)

- **What it assumes upstream.** (a) Symbolic input in `**kern`, with voices and with note onsets and
  durations as notated (§2.1). (b) A metrical position for each slice, in three values (§2.2, feature
  M); where those come from is not said, and the notated meter is this side's reading, not the page's.
  (c) **One key per chorale, estimated by a key-profile method** (footnote 4), used to transpose the
  music and its labels to C major or A minor before learning. (d) An existing rule-based labeler [4],
  configured to one analytical style, whose output is both the pre-training target and one of the four
  voters. (e) For the interactive half, a human expert.
- **What it hands downstream.** One chord label per onset slice: a root letter-name and one of eight
  qualities (§2.3). No inversion and no Roman numeral, by the paper's own statement (§2.3). A key, a
  modulation or a non-chord-tone label is not described as an output in the pages as read (Models 1 and
  2 identify non-chord tones internally; the workflow's output as described is the chord label). Nor is
  a confidence value or a ranked list of alternatives: the ensemble outputs *"the most-preferred"*
  label, and unanimity among the four voters is used as a two-valued signal of where
  the expert looks.
- **Its stated scope.** *"a set of largely homorhythmic Bach chorales"* (page 2); footnote 1 defines
  homorhythm as *"a texture where all parts share a very similar rhythm"*. The "harmonic" analytical
  style alone is tested. The paper claims wider use as a possibility (§2.1 above, CONJECTURE) and names
  homophonic music as a harder case it has not addressed (§5).
- **What is evaluated against what.** Experiment 1: learners against the rule-based model's labels, on
  the 330. Experiment 2: the four models, the vote and the re-trained models against one expert's hand
  labels on 39 chorales. The unit of accuracy is the onset slice (Table 1's and Table 2's captions);
  no weighting by duration is mentioned in the pages as read.

## §4 — Measured results, as the paper states them

### §4.1 Table 1, whole, as printed (page 5)

Caption: *"Experiment 1 cross-validation classification accuracies, averaged across folds. Uncertainty
values indicate standard error across folds. Values indicate the percentage of onset slices "correctly"
classified by Model 1 (CA1), Model 2 (CA2), and Model 3 (CA3), based on the Model 4 "ground truth".
Columns indicate features (see Section 2.2) and rows indicate machine learning algorithms (see Section
2.4). The best performance in each column is highlighted in bold."*

| Model | Metric | PC12 | PC12M | PC12W1/2 | PC12MW1/2 | PC12MOW1/2 |
|---|---|---|---|---|---|---|
| SVM | CA1 | **81.7±1.4%** | 81.6±1.4% | 82.7±1.0% | 83.0±1.0% | 83.5±0.9% |
| SVM | CA2 | 73.0±1.5% | 73.1±1.6% | 85.4±1.3% | 86.1±1.5% | 87.4±1.5% |
| SVM | CA3 | 74.9±1.6% | 75.6±1.5% | 85.4±1.3% | 85.9±1.3% | 87.7±1.5% |
| DNN | CA1 | 81.0±1.5% | **81.7±1.5%** | 85.3±0.9% | 85.6±0.9% | 85.8±0.9% |
| DNN | CA2 | 74.2±1.8% | 75.1±1.6% | **88.5±1.3%** | **89.6±1.3%** | **90.1±1.5%** |
| DNN | CA3 | 74.6±1.8% | 75.3±1.4% | 87.5±1.7% | 88.3±1.7% | 89.0±2.0% |

Bold is the page's. Each bold cell is the largest value in its column as printed.

### §4.2 Table 2, whole, as printed (page 5)

Caption: *"Experiment 2 classification accuracies on the reserved test set. DNN values are averaged
across models trained using different training/validation sets, and uncertainty values indicate standard
error across these folds. Values indicate how many onset slices were correctly classified by Model 1
(CA1), Model 2 (CA2), Model 3 (CA3), Model 4 (CA4), the ensemble as a whole (CAVote), and just those
CAVote predictions that were unanimous (PUA). "PC12MOW1/2" indicates the input features (see Section
2.2. "Pre-trained" indicates performance before manual correction (i.e., Analysis 1 in Fig. 2), and
"Re-trained" indicates performance after re-training on the corrected data (i.e., Analysis 3 in Fig.
2). The best performance in each column is highlighted in bold."* (The parenthesis after *"Section 2.2"*
is not closed on the page.)

| Model | Metric | PC12MOW1/2 Pre-trained | PC12MOW1/2 Re-trained |
|---|---|---|---|
| SVM | CA1 | 85.9% | 87.0% |
| SVM | CA2 | 88.6% | 89.8% |
| SVM | CA3 | 87.7% | 89.3% |
| SVM | CAVote | **91.4%** | 92.7% |
| SVM | PUA | 79.1% | 79.0% |
| DNN | CA1 | 85.4±0.2% | 88.1±0.2% |
| DNN | CA2 | 88.9±0.3% | 91.3±0.4% |
| DNN | CA3 | 87.9±0.7% | 90.5±0.3% |
| DNN | CAVote | 90.9±0.2% | **93.5±0.2%** |
| DNN | PUA | 80.4±1.2% | 79.7±0.4% |
| RB | CA4 | 90.7% (one cell spanning both columns) | |

**What PUA is.** The caption's words are *"just those CAVote predictions that were unanimous (PUA)"*,
under a sentence that says the values *"indicate how many onset slices were correctly classified"*.
Footnote 12 uses 100 % − PUA as the share of slices the expert must examine, which reads PUA as the share
of slices on which the four models were unanimous. **The pages do not expand the letters PUA, and the
two readings differ**: a share of slices that were unanimous, or a share of slices that were unanimous
and correct. Footnote 12's arithmetic fits the first reading; the caption's sentence fits the second.
Recorded, not resolved.

### §4.3 The two tables side by side at PC12MOW1/2 (this reader's arrangement; the values are the page's)

| | Table 1 (330, against rule-based labels, ten-fold) | Table 2 pre-trained (39 reserved, against the expert) |
|---|---|---|
| SVM CA1 | 83.5±0.9 | 85.9 |
| SVM CA2 | 87.4±1.5 | 88.6 |
| SVM CA3 | 87.7±1.5 | 87.7 |
| DNN CA1 | 85.8±0.9 | 85.4±0.2 |
| DNN CA2 | 90.1±1.5 | 88.9±0.3 |
| DNN CA3 | 89.0±2.0 | 87.9±0.7 |

The two columns differ in at least these things at once: the music, the reference labels, and how much
data trained the model (Experiment 2's SVM trains on the 330 whole, its DNN on 90 % against 80 %). The paper's *"quite similar"* (§2.7) is
over these pairs.

### §4.4 Arithmetic over the printed values (this reader's, not the paper's; done by hand)

- **Error rates from Table 2** (100 − accuracy): rule-based 9.3; SVM vote 8.6 before and 7.3 after
  re-training; DNN vote 9.1 before and 6.5 after.
- **The paper's three fractional reductions reproduce, and show which cells they use.** 7.5 %: (9.3 −
  8.6) / 9.3 = 0.0753 — rule-based against the **SVM** pre-trained vote. 30.1 %: (9.3 − 6.5) / 9.3 =
  0.3011 — rule-based against the **DNN** re-trained vote. 24.4 %: (8.6 − 6.5) / 8.6 = 0.2442 — the
  **SVM** pre-trained vote against the **DNN** re-trained vote.
- **So the Abstract's 91.4 %, 20.9 % and 93.5 %, and its 24.4 %, join two classifier families**: 91.4
  and 20.9 (100 − 79.1) are the SVM ensemble before re-training; 93.5 is the DNN ensemble after. §4's
  own wording for the 24.4 % is *"comparing re-trained CAVote to pre-trained CAVote"*, without naming
  that the two are different families.
- **Within one family**, from the same table: DNN, 9.1 → 6.5, a reduction of 2.6 / 9.1 = 0.2857 (28.6
  %); SVM, 8.6 → 7.3, a reduction of 1.3 / 8.6 = 0.1512 (15.1 %). The paper prints neither.
- **The pre-trained DNN vote against the rule-based model:** 90.9±0.2 against 90.7, a difference of 0.2
  with a printed standard error of 0.2 on one side and none on the other. The paper's sentence that
  CAVote is higher than CA4 is made of the SVM's 91.4.
- **The share not unanimous, by footnote 12's formula, for each cell:** SVM 20.9 before and 21.0 after;
  DNN 19.6 before and 20.3 after. The share rises slightly after re-training in both families;
  footnote 10 says the PUA change is not significant.
- **Context-window gain in Table 1**, PC12 → PC12W1/2: SVM CA2 +12.4, SVM CA3 +10.5, DNN CA2 +14.3, DNN
  CA3 +12.9; Model 1: SVM +1.0, DNN +4.3. From PC12 to PC12M (adding M alone) the six rows move by
  −0.1, +0.1, +0.7, +0.7, +0.9 and +0.7, in the table's row order.
- **When the vote can depart from the rule-based label** (derived from Figure 2's four voters and
  footnote 3's tie-break, not printed; it reads *"most-preferred"* as the label with the most votes):
  with four votes, and a tie going to the rule-based model's label, the vote differs from the rule-based
  label where another label gets more votes than it — that is, where the three learners agree on one
  other label, or two of them do and the third does not side with the rule-based model. Two learners
  against the rule-based model and the third learner is a tie, and the rule-based label stands; so it
  does where the learners split three ways or one alone dissents.

### §4.5 What is not among the measured results

Accuracy by chord quality or by label; a confusion table; accuracy of the unanimous labels taken alone
(unless PUA is that, §4.2); the number of labels the expert changed; the expert's time; agreement between
the expert and a second annotator; accuracy of the key estimate used for transposition; a result on any
music other than the Bach chorales. Each is met nowhere in the pages as read.

## §5 — What the paper states about uncertainty, reproducibility and ground truth (against #24, #16, #21)

- **Uncertainty (#24).** Table 1 prints a standard error across ten folds for each cell. Table 2 prints
  a standard error for the DNN rows, across ten models trained on rotated training/validation splits
  and tested on one fixed test set — so that spread is over training splits, not over test music. The
  SVM rows and the rule-based row print no spread. Three footnotes (9, 10, 11) report Student's t-tests
  at p < 0.05; what the paired or unpaired samples were, and how a test was run on the SVM rows that
  print single values, is not said.
- **Reproducibility (#16).** Code, data and results are said to be at a shortened URL (page 2); the
  dataset and its source at two more (footnotes 7 and 8); the rule-based tool, its style heuristics and
  the H-CL heuristic at three more (§2.3 and footnote 6). The pages print no commit, version, random seed
  or software library for the learners. The 39 reserved chorales are said to be chosen at random *"before
  the experiments began"*; which chorales they are is not printed.
- **Ground truth (#21).** The paper separates two things it calls ground truth and marks the first with
  quotation marks at three of the five places §2.6 names: the rule-based model's labels on the 330 (*"imperfect"*, *"artificial"*), and one
  expert's hand labels on the 39. It names the single annotator as a limitation (§2.7). No agreement
  measurement between annotators is reported. The paper's own Figure 1 and its citation of [12] state
  that expert analyses differ; its answer is to fix one style and to count a defensible alternative as
  an error (§2.7, Figure 5's discussion).

## §6 — Terms the paper uses, in the paper's sense

- **Onset slice** — formed at each new note onset in any voice; holds the pitch classes sounding then
  (§2.3). Cut at onsets.
- **Artificial onset** — a pitch class in a slice that is sustained from an earlier slice and not newly
  struck (Figure 4; feature O).
- **Melodic / harmonic (style of analysis)** — fewer chords and more non-chord tones, against more
  frequent chord changes and fewer non-chord tones (§2.1, §2.5).
- **NCT-first / direct harmonic analysis** — remove non-chord tones and then label, against label from
  the pitch-class collection as it stands (Figure 2's caption).
- **Analysis 1, 2, 3** — the pre-trained ensemble's vote; that vote with the non-unanimous labels
  corrected by the expert; the re-trained ensemble's vote.
- **Partial manual modification** — the expert's correction of the non-unanimous labels alone.
- **CA1 to CA4, CAVote, PUA** — accuracies of Models 1 to 4 and of the vote; PUA at §4.2.
- **Pre-train / re-train** — train on rule-based labels; train again on Analysis 2.
- **Homorhythm** — footnote 1: *"a texture where all parts share a very similar rhythm"*.

## §7 — Stated ABSENT: things a reader might supply from the method class that the pages do not say

Each of the following is met nowhere in the eight pages as read.

- The number of onset slices in the 330 chorales or in the 39.
- The number of distinct chord labels (output classes) the learners choose among, and what label a slice
  gets when its pitch classes fit none of the eight qualities or when it holds fewer than three pitch
  classes.
- The share of labels in the 330 chorales on which the ensemble was not unanimous, and the number the
  expert changed. The 20.9 % is from the test set (§2.7).
- Which ensemble's non-unanimous labels the expert corrected — the SVM ensemble's, the DNN ensemble's, or
  each in a separate pass — and whether the ten DNN models of Experiment 2 each had their own correction
  pass.
- Whether the expert who labeled the 39 is the expert who made the corrections; what instructions on
  analytical style the expert had; whether the expert saw the rule-based labels while labeling the 39.
- A definition of down-beat, on-beat and off-beat, and the source of the metrical value.
- Learning rate, batch size, number of epochs, the early-stopping rule's setting, the SVM's
  regularization setting, and the software used for the learners.
- How the features of a contextual window are filled at the first and last slices of a chorale.
- Any use of pitch spelling, of voice identity, or of bass identity as a feature. The label's root is a
  *"letter-name"*; how a letter-name is chosen from enharmonic pitch classes is not said.
- Any weighting of accuracy by duration.
- The rules of the rule-based model and of the H-CL heuristic (URLs and reference [4] stand in for them).
- A measurement behind *"better-suited to the typical chorale texture"* (§2.5) or behind the
  overfitting explanation (§2.7).

## §8 — The read-back and the sweep (steps 4 and 5 of entry 169 §3), written after the text above was finished

### §8.1 The read-back against the pages

Run with the eight page images of the first request still held, and with pages 5 and 6 requested a second
time and read again (both images present). What it checked and what it changed:

- **Tables 1 and 2** were compared cell by cell with page 5 at the second request: the thirty cells of
  Table 1 with their ± values and the five bold cells; the twenty-one cells of Table 2 with the two bold
  cells and the spanning 90.7 %. No cell changed.
- **Figure 5's error column** was read again at page 6: 2; 7, 8, 8; 5; 2; 6, 4, 6; 1. Unchanged. These
  are single small digits in a rendered image, and the chord labels of Figures 1 and 5 are small glyphs;
  this side did not transcribe Figure 5's label rows for that reason.
- **Added at the read-back:** §4's sentence chaining 90.7 %, 91.4 % and 93.5 %, and its sentence on which
  approaches need no human (both at §2.7), which the first writing had left out; and §4.4's last item on
  when the vote can depart from the rule-based label. **That item was first written wrongly** — it said
  two learners agreeing on another label is enough — and was corrected before landing: two learners
  against the rule-based model and the third learner is a tie, which footnote 3 gives to the rule-based
  label.
- *(★ CORRECTED at the user-ordered check, §10: the next item's heading "Located again at their pages"
  claimed a separate pass that was not run. The page locations in it were assigned while writing, from
  the page images of the first request; the read-back re-requested pages 5 and 6 and no others. The
  item stands as a list of where those things are, not as a second look.)*
- **Located again at their pages:** the four workflow steps and footnotes 1 to 5 (page 2); Figure 2 and
  its caption, §2.3, §2.4 and §3.1 with footnotes 6 to 8 (page 3); Figures 3 and 4, §3.2 and §3.3.1 with
  footnote 9 (page 4); §3.3.2, §4 and footnotes 10 to 12 (page 5); §4's end and §5 (page 6); references
  [4], [11], [12] and [19] (page 7).
- **URLs** are as read from the rendered page; mixed-case shortened URLs are easy to misread, and none
  was followed.

### §8.2 The sweep for absolutes

One search was run over this file for *only, never, nowhere, every, all, none, always, alone, each,
whole, entire, exhaustive, complete, any, nothing, both, exactly, must, cannot*, and each hit was read at
its line. Hits inside quotations from the paper were left. Of this side's own sentences, these were
changed: *"none of them names this paper"* (§0) became a statement about the fragments this side saw;
*"Every mechanism statement below is therefore located to a page"* (§0) was narrowed to what §2 to §4
do; *"at each of these uses"* (§2.6, of the quotation marks round *ground truth*) was replaced by the
three places that carry them and the two that do not; *"No numbered equation"* (§1.5), *"The last clause
carries no measurement"* (§2.5) and §3's list of what is not handed downstream were each bounded to the
pages as read; *"Adding M alone moves each row by at most 0.9"* (§4.4) was replaced by the six
differences. Left standing after being read: *"Each bold cell is the largest value in its column as
printed"* (§4.1, checked column by column); *"The "harmonic" analytical style alone is tested"* (§3;
§5 of the paper names the other style as a next step); the two *"met nowhere in the pages as read"*
lists (§4.5, §7), which are negatives over eight page images and no wider.

### §8.3 What this file rests on, and what it does not

It rests on the eight pages of the held file, read as page images, and on nothing behind the paper's
URLs or references. It did not open reference [4], which is held and has an extract in this repository, nor row 35's
held paper, whose authors and title reference [11] names *(★ CORRECTED at §9.5. FORMER WORDING,
PRESERVED (#12): "It did not open reference [4] or reference [11], although both are held and both have
extracts in this repository." — whether the held row-35 file is the publication [11] cites is not
established)*. The arithmetic at §4.4 was done by hand and not by a program. The
statements in §7 are negatives over the pages as read. §0 to §7 were written before the first extract
was opened; §9, when it is written, is the cross-check against it.

## §9 — The cross-check against the first extract (step 7 of entry 169 §3), written after §0–§8 had landed

### §9.1 What was compared, and its bound

§0 to §8 landed at 48,436 bytes (modification time 1789799718879) before the first extract was opened.
The first extract
(`reading_pass/extracts/ju-howes-mckay-conditschultz-calvozaragoza-fujinaga-2019-an-interactive-workflow-for-generating-chord-labels.md`,
85,207 bytes, 959 lines) was then read whole, in two calls. The comparison ran over what both files
carry from the paper: the identity, the quotations, both tables cell by cell, the footnotes, the
reference numbers both name, and the arithmetic both derive. **It did not run over the first extract's
record-facing half** — its cross-primary check, its sweeps of the staged tree, its routings to design
points and ledger entries, its reference mapping against the candidacy rows, and its centrality verdict
— which has no counterpart here (§0). Each disagreement was taken to the page: page 4 and page 5 were
each opened alone for this, page 2 alone, and page 6 had been opened twice already (each image present).
**No claim is made that the comparison was exhaustive**: it found the ten sites of §9.3 and §9.4, and a
later reader may find more.
**Both reads are reads of rendered page images by a language model; where the two disagree about what a
page prints, a person looking at the PDF settles it in seconds, and §9.4 says where to look.**

### §9.2 Where the two reads agree

The identity on each axis (title, six authors and four affiliations, venue, year, licence, printed pages
862–869, eight pages, five figures, two tables, twelve footnotes, twenty-four references). Table 2 in
each of its twenty-one cells, with both bold cells. Table 1 in twenty-nine of its thirty cells, with the
five bold cells. The feature definitions, the label vocabulary, the classifier settings, the data counts
(369, 39, 330), both experimental designs, footnotes 3, 4, 7, 9, 10, 11 and 12 as each file quotes them.
The arithmetic on Table 2: the error rates 9.3, 8.6, 7.3, 9.1 and 6.5; the reconstruction of 7.5 %,
30.1 % and 24.4 % and the observation that they join the SVM and DNN families; the within-family 28.6 %
and 15.1 %. **Both reads reached that observation independently** (the first at its finding (9), this
one at §4.4).

### §9.3 Where the page goes against the first extract and no value, finding or verdict moves — six sites, corrected under the standing rule

Each was resolved at the page. Under the standing rule of handoff entry 198 §7 (the user's ruling of
2026-09-19), each is corrected in the first extract at its site with the former wording preserved
(#12), without a surface.

- **(a)** Workflow step 1 (its claims section): the first extract read *"we use an existing, consistent
  RB model [4]"*; page 2 prints *"we use an existing RB model [4] to generate preliminary, consistent
  chord labels"*. One *"consistent"* was inserted.
- **(b)** §2.1's sentence on onset slices and Figure 4's caption: the page prints *any* in italics in
  both (pages 2 and 4); the first extract's two quotations do not show it. A remark, no change of words.
- **(c)** §3.2.2 (its claims section): *"rather than confirmed truth"*; page 4 prints *"rather than as
  confirmed truth"*.
- **(d)** Table 2's caption: the first extract closes the parenthesis after *"Section 2.2"*; page 5 does
  not.
- **(e)** §3.3.2 (its claims section): *"One can see from Table 2"*; page 5 prints *"One can see in
  Table 2"*.
- **(f)** §5's first limitation (its claims section): *"might not be ideal"*; page 6 prints *"may not be
  ideal"*.

### §9.4 ★ Where the page goes against the first extract and a value or a numbered finding is touched — four sites, NOT corrected, with the user

- **(g) A table value, and a difference derived from it inside finding (5).** Table 1, SVM, CA1, column
  PC12W1/2: the first extract has **82.0±1.0**; this side read **82.7±1.0** at three openings of page 5
  (the whole-paper request, the read-back, and page 5 alone for this check). Finding (5) derives from
  that cell *"SVM 81.7±1.4 → 82.0±1.0, +0.3"*; with 82.7 the difference is **+1.0**. Finding (5)'s
  sentence that Model 1 moves much less than Models 2 and 3, and unequally in the two families, holds
  with either value (+1.0 against +4.3 for the DNN, and against +10.5 to +14.3 for Models 2 and 3). **To
  look: printed page 866, Table 1, first data row, third value.**
- **(h) Finding (10), whole.** The first extract reports that Figure 3's caption prints *"first
  identifies and removes chord tones from the score, and then generates chord labels from the remaining
  chord tones"* and records it as a printing inconsistency, having opened page 4 a second time to check.
  This side read the same caption at two openings of page 4, the second of them alone and for this
  check, as: *"The former identifies chords directly from the score, while the latter first identifies
  and removes non-chord tones from the score, and then generates chord labels from the remaining chord
  tones."* **As this side reads the page, the caption is consistent with the diagram, with §2.4 and with
  Figure 2's caption, and there is no printing inconsistency to record.** The first extract itself says
  nothing is carried out of that caption, so no other finding rests on (10). **To look: printed page
  865, Figure 3's caption, its last sentence.**
- **(i) A quotation inside finding (3).** Finding (3) quotes §3.2.2 as *"more as preliminary indications
  rather than confirmed truth"*; the page prints *"rather than as confirmed truth"* (the same slip as
  (c)). No value or sense moves.
- **(j) A quotation inside finding (12).** Finding (12) quotes §5 as *"might not be ideal"*; the page
  prints *"may not be ideal"* (the same slip as (f)). No value or sense moves.

**What this side proposes, and does not do:** correct (g), (i) and (j) at their sites with the former
wording preserved; withdraw finding (10) with its first writing kept whole beneath the withdrawal (the
form row 46's finding (6) took under the user's ruling of 2026-09-16). These stand with the user because
the standing rule reserves to him a value, and a word inside or beside a finding.

### §9.5 What the first extract shows about this one

- **This file did not transcribe Figure 3's caption**, which the first extract quotes in part. It is
  given at §9.4(h) as read here. Its first sentence, as read at page 4: *"Comparison of "direct harmonic
  analysis" (left, used by Model 3 in Fig. 2) and "NCT-first harmonic analysis" (right, used by Model 1
  and Model 2 in Fig. 2) approaches to automatic harmonic analysis."*
- **§0 and §8.3 of this file said more about reference [11] than the page supports, and are corrected at
  their sites.** Reference [11] names the four authors and the title of row 35's paper at the
  *Proceedings of the 4th International Workshop on Digital Libraries for Musicology*, pages 13–16,
  2017. Row 35's held file prints the late-breaking session of ISMIR 2017 and two pages. The first
  extract's finding (6) records that whether these are one work in two forms or two publications cannot
  be established from what is held; this file had called them the same paper.
- **Things the first extract carries from the paper that this file does not:** that Models 1 and 2 share
  one non-chord-tone remover (MLA), so an MLA error reaches two of the four votes; Model 2 against Model
  3 cell by cell in both tables; the gain from feature O column by column; footnote 1's second sentence;
  the references mapped one by one.
- **Things this file carries that the first extract does not:** that the 20.9 % comes from Table 2,
  whose values are on the reserved test set, and not from the 330 chorales the expert corrected (§2.7); the two readings of PUA
  (§4.2); Figure 5's error column, in which Analysis 1 has more errors than the rule-based model in that
  excerpt (§2.7); the pre-trained DNN vote at 90.9±0.2 against the rule-based 90.7 (§4.4); Figure 1's
  three label rows; when the vote can depart from the rule-based label (§4.4); the two tables side by
  side (§4.3). None of these was checked against the first extract's findings for consequence; that is
  the record-facing half.

### §9.6 The act under the standing rule

The first extract was corrected at the six sites of §9.3, each with a "★ CORRECTED 2026-09-19" remark
outside the quotation and the former wording preserved, and carries a banner remark naming the four
sites of §9.4 as standing with the user. Its Table 1, its findings (3), (5), (10) and (12) and its
centrality verdict were not touched. The landing figures of both files are in the handoff entry of this
sitting.

**★ MADE STALE BY THE RULING BELOW AND LEFT STANDING (#12).** §9.4's heading (*"NOT corrected, with the
user"*), its closing paragraph and the sentence above that Table 1 and findings (3), (5), (10) and (12)
*"were not touched"* were true when written.

### §9.7 ★ The ruling on §9.4's four sites, and the act under it

**The ruling, 2026-09-19, the user's words: "I agree with recommendation."** It came in reply to the
surface itself; the separate choice question had been announced and had not yet been put. The
recommendation was §9.4's closing paragraph: correct (g), (i) and (j) at their sites with the former
wording preserved, and withdraw finding (10) with its first writing kept whole beneath. **Whether the
user looked at the two pages before ruling is not known to this side.**

**The act, in the first extract:** Table 1's SVM CA1 cell under PC12W1/2 now reads 82.7±1.0, with a remark
under the table carrying the former 82.0±1.0; finding (5)'s *"82.0±1.0, +0.3"* now reads *"82.7±1.0,
+1.0"*, former wording preserved; the quotations inside findings (3) and (12) are corrected, former
wordings preserved; finding (10) is withdrawn, its first writing kept whole beneath the withdrawal; the
banner records the ruling; and the *"+0.3"* that the first extract's own second fact-check section
quotes carries a remark and is otherwise left. **No other value, finding or verdict was touched, and the
paper was not re-opened for the act**; the ground is §9.4.

## §10 — ★ The user-ordered check after landing, written in the act that ran it

The user ordered, after §0–§9.6 had landed: *"Fact check what you have written"*. **This file was re-read
whole at the landed copy staged back (57,703 bytes, 716 lines; four calls for lines 1–709, the last
seven lines at an earlier call)** against the page images held
from this sitting's requests, and its arithmetic was done again by hand. **It did not come back empty.**
Each correction is at its site; where the former wording is not given at the site it is given here.
Named rather than counted:

- **An underived count of this side's own acts:** §0 said three searches were run over the progress
  table; five were. Corrected at the site.
- **A check written down as run that was not run as written:** §8.1's item *"Located again at their
  pages"*. Marked at the site.
- **A claim firmer than its own section allows:** §2.7 said what the 20.9 % *is*, where §4.2 leaves PUA
  at two readings. Corrected at the site; §9.5's echo of it reworded (formerly *"that the 20.9 % is
  measured on the reserved test set and not on the 330 chorales the expert corrected"*).
- **A gloss standing beside a quotation without its mark:** *"one key per chorale"* (§2.3) is now marked
  as this side's reading of footnote 4 (formerly *"So the key of each chorale is estimated by a profile
  method, one key per chorale, before anything is learned; the paper names this as a limitation"*).
- **Negatives and counts wider than the look behind them:** *"Neither sentence carries a measurement in
  this paper"* (§2.1) is now *"at its site"*; *"No measurement in the pages tests this explanation"*
  (§2.7) is now bounded to the pages as read; *"differ in three things at once"* (§4.3) is now *"at
  least these things"*, with the DNN's 90 % against 80 % added; §5's *"marks the first with quotation
  marks"* now says at three of the five places §2.6 names; §9.1 now says the comparison is not claimed
  to be exhaustive.
- **A line range one short:** entry 152 was read at lines 55–69, not 55–68 (§0).

**What the check confirmed and did not strike:** both tables cell by cell against page 5 as last opened;
the five bold cells as column maxima; each figure of §4.4, including the six PC12 → PC12M differences
and the four share-not-unanimous values; the vote derivation case by case (three learners agreeing; two
agreeing with the third elsewhere; two agreeing with the third on the rule-based label; a three-way
split; one dissenter); Figure 5's error column as read; the quotations of §2.1, §2.2, §2.3 and §2.7 one by one
against the held page images, and those of §2.4, §2.5 and §2.6 through the cross-check, the first
extract carrying the same passages; the counts of footnotes, figures, tables, references and Table 2's twenty-one cells; §9.2's
twenty-nine of thirty, by comparing the first extract's Table 1 row by row.

**What it did NOT do:** request any page again (it used the images already held, so a misreading shared
by each look at one image survives it); re-open the first extract's record-facing half; check Figure 1's
label rows or the URLs beyond what §2.1 and §8.1 already bound. **It is the writer's own check. Nothing
here says a further pass would come back empty.**

# Ju, Condit-Schultz, Arthur & Fujinaga 2017 — "Non-chord Tone Identification Using Deep Neural Networks" — SECOND INDEPENDENT EXTRACT

> **STATUS: READING-PASS EXTRACT, SECOND PASS. NOTHING HERE IS RULED.** Written 2026-09-19 by the Cowork
> session that booted on `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_eight.md`,
> under the second-pass rule of `cowork_reading_pass_commission_2026_08_30.md` §4 **as handoff entry 169 §3
> quotes it** (a CENTRAL source is extracted in a second independent pass and the two extracts
> cross-checked) and the eight-step order of that same §3, as amended at its naming point by Ruling 2 of
> entry 186 §2. **This session did not open the commission itself**; the form below follows entry 169 §3
> step 3 and the form of row 17's second extract, which was read for that purpose (§0). **The paper is
> Task B, L2's slice, row 35** — the row number is the progress table's
> (`reading_pass/l2_slice_reading_progress.md`, line 106); the candidacy file that table takes its row
> numbers from was not opened by this side. Held file:
> `docs/research_papers/ju_conditschultz_arthur_fujinaga_2017_ismirlbd_nct_dnn.pdf`, 447,585 bytes at this
> session's staging call (entry 198 §3 records the same size at a folder listing; this side did not list
> that folder); **2 pages, established at the tool** by a deliberately out-of-range request (page 20
> refused with "PDF has 2 pages"). Read whole in one request, pages 1–2; **both page images were
> present** (checked at the images, not at the call's success line).
>
> Page numbers below are the PDF's own (1–2). No page number is printed on either page as rendered.

## §0 — Declarations of independence and its bound

- **What this side read before opening the paper, that bears on it:** the progress table was searched,
  not read. Two searches were run: one returned, for each table row, its row-number cell with up to 160
  characters of the cell after it; the other returned each line's text around the words "OWED" and "not
  owed". **Of row 35's line (line 106) this side therefore saw two strings.** The first is the opening of
  its identity cell, which names the four authors and begins quoting the printed title. The second is the
  tail of its centrality cell and its "Second pass" cell: *"…igure and no comparison, a binary question
  per voice under a given key and grid — is stated in full in the extract) | OWED (flips to not owed if
  the user reads findings (4) and (5) as settled by the e…"* (cut at both ends by the search). **So this
  side knew, before opening the paper, that the first extract numbers at least five findings, that it
  states a ground on which the paper could be read as not central, and that that ground includes the
  words "no comparison" and "a binary question per voice under a given key and grid".** It did not know
  what any finding says. The same search returned, at the table's line 2827, the words *"14's, 17's AND
  35's flipping the OTHER WAY — from owed to not owed — if"*, which says the same thing about the "Second
  pass" cell. `docs/research_papers/BIBLIOGRAPHY.md` was searched for the first author's surname; line 49
  is this paper's row (authors, a title, a venue, a URL, a check mark, and a last cell reading LINK), and
  lines 50, 81 and 82 are other papers sharing an author. The bibliography's column headings were not
  read.
- **Name-only look-up, declared under Ruling 2 (entry 186 §2):** `reading_pass/extracts/` was listed by
  file name at boot, to verify another extract's size, and that listing was reused to find the first
  extract's name:
  `ju-conditschultz-arthur-fujinaga-2017-non-chord-tone-identification-using-deep-neural-networks.md`
  (46,124 bytes, modification time 1789151182710). **It was not opened before §9.** The file name carries
  authors, year and the paper's own printed title, which the paper supplies.
- **Contamination from the record's own text, beyond those strings:** of the records read at boot (entry
  198 whole; entries 186 and 169 whole; 188 at §4–§5; 152 at its lines 55–68; 118 at its lines 27–51;
  `CLAUDE.md` at its six spans; `DECISIONS.md` whole; `STATUS.md` whole; the gating answer's identity
  list), none summarises this paper's content; entry 198 §3 names row 35 by its authors and its held file
  name, whose last words are *"nct_dnn"*. **One record read at boot bears on the paper's SUBJECT and not
  on the paper:** the decisions register's index line for D-527, which says this project has no live
  stage that removes non-chord tones and that each tone is emitted by category inside the one decode. It
  is named here because a reader who knows that line may read a paper about identifying non-chord tones
  with it in mind. Two files of the user's Cowork memory store were read at the start of the sitting (a
  project preferences file and a remark on working without a shell); neither mentions this paper. The
  listing of that store shows, by its one-line description alone, a file about a deferred design analysis
  of non-chord-tone detection in this project; **it was not opened.** `FRAMEWORK.md`, `population.md`,
  the findings surface, the slice derivation and the candidacy file were **not** opened.
- **Row 17's second extract was read for its form** — its lines 1–140 (banner, §0, §1 and the opening of
  §2) and its section headings by search. Row 17's paper shares one author with this one (Fujinaga).
  Nothing about row 17's paper is used below.
- **General knowledge is the larger contamination and is named as such:** this side knows feedforward
  neural networks, the ADAM optimiser, binary cross-entropy, precision, recall and F1, k-fold cross
  validation, and the usual music-theory classes of non-chord tone (passing tone, neighbour tone,
  suspension and so on) from outside this repository. **Every mechanism statement below is therefore
  located to a page**, and a statement this side could make from general knowledge but could not find on
  a page is written as ABSENT (§7), not as a fact.
- **What this file is not:** it is not a record-facing extract. What `FRAMEWORK.md` or any design point
  says about this paper, and the paper's centrality verdict, are the first extract's half and are not
  re-derived here (entry 169 §5(vii)).

## §1 — Identity, checked at page 1

- **§1.1 Title, as printed:** *"NON-CHORD TONE IDENTIFICATION USING DEEP NEURAL NETWORKS"* (page 1, head,
  in capitals over two lines). The attribution box at the foot of page 1 prints it in mixed case:
  *"Non-chord Tone Identification Using Deep Neural Networks"*.
- **§1.2 Authors and affiliation, as printed:** Yaolong Ju, Nathaniel Condit-Schultz, Claire Arthur,
  Ichiro Fujinaga; Centre for Interdisciplinary Research in Music Media and Technology (CIRMMT), Schulich
  School of Music, McGill University, Montréal, Canada; e-mail
  `{yaolong.ju, nathaniel.condit-schultz, claire.arthur, ichiro.fujinaga}@mcgill.ca` (page 1).
- **§1.3 Venue, as printed** (attribution box, foot of page 1, left column): *"Extended abstracts for the
  Late-Breaking Demo Session of the 18th International Society for Music Information Retrieval
  Conference, Suzhou, China, 2017."* The same box prints a Creative Commons Attribution 4.0 licence (CC
  BY 4.0) in the four authors' names.
- **§1.4 Match to the bibliography row:** the row (line 49) gives the title as *"Non-chord Tone
  Identification Using Deep Neural Networks,"* — it matches the attribution box's form. The authors match
  by surname and order. The row's venue reads *"ISMIR-LBD/DLfM 2017"*. **The first half is on the page
  (the late-breaking demo session of ISMIR 2017); "DLfM" is met nowhere on the two pages as read.** The
  row's last cell reads LINK, where the next row's (line 50, a different paper) reads CC; this side did
  not read the bibliography's column headings, so what that cell grades is not stated here. The page
  itself prints a CC BY 4.0 licence. Both recorded, not graded.
- **§1.5 Length and structure:** 2 pages. Sections as printed: Abstract; 1 Introduction; 2 Dataset; 3
  Method; 4 Evaluation; 5 Conclusion; 6 References. Figure 1 (page 1, right column, a four-staff music
  example with vectors above and below it); Tables 1 and 2 (page 2, left column); Figure 2 (page 2, right
  column, three systems of four staves with up to three lines of text under each system). Two footnotes: footnote 1
  (page 1) is a URL for the data; footnote 2 (page 2) is a funding acknowledgement. No numbered equation.
  The reference list (page 2) has four entries, numbered [1] to [4].
- **§1.6 The paper calls itself a demo and preliminary.** *"This demo addresses…"* (Abstract); *"In this
  demo, we construct…"* (§1); *"suitable for our preliminary research"* (§1, page 1 right column); *"In
  this demo, a non-chord tone identification model … is proposed"* (§5).

## §2 — Claims, labeled

The label NAMES are the commission's as entry 169 §3 step 3 carries them; the definitions that follow are
worded as row 17's second extract words them at the head of its §2, and the commission's own wording was
not opened. **FACT** = stated or measured in the paper, with its location; **THEORY** = established
published theory the paper invokes; **CONJECTURE** = the paper's own speculation, or a claim it makes
without a measurement or a citation. Quotations are verbatim from the page as rendered, printed slips
included.

### §2.1 The problem the paper sets, and its headline claim (Abstract and §1, page 1)

- **[FACT, p. 1 Abstract]** What the paper says it does: *"This demo addresses the problem of harmonic
  analysis by proposing a non-chord tone identification model using deep neural networks (DNNs)."*
- **[CONJECTURE, p. 1 Abstract]** *"By identifying non-chord tones, the task of harmonic analysis is much
  simplified."* No measurement or citation is attached to it on the page; §1 repeats it in a stronger
  form (below).
- **[FACT, p. 1 Abstract]** The headline result: *"Trained and tested on a dataset of 140 Bach chorales,
  the DNN model was able to identify non-chord tones with F1-measure of 72.19% using pitch-class, metric
  information, and a small contextual window around each input sonority as input features."*
- **[CONJECTURE, p. 1 Abstract]** *"These results suggest that DNNs offer an innovative and promising
  approach to tackling the problem of non-chord tone identification, as well as harmonic analysis."* This
  reader met no harmonic-analysis result on the two pages (§4, §7), so the last five words rest on no
  measurement met there.
- **[FACT, p. 1 §1 — the paper's definition]** *"Non-chord tones are elaborative notes, created by
  idiomatic step-wise melodic contours, which do not belong to the local structural harmony."* (The
  first two words are set in italics on the page.) No source is cited for the definition.
- **[FACT, p. 1 §1, with citations]** *"Identifying non-chord tones is essential to many music analytic
  tasks, including polyphonic music retrieval [4], harmonization [1], and harmonic analysis [3]."* The
  three citations name a task each; the page does not say what any of the three sources states about
  non-chord tones.
- **[CONJECTURE, p. 1 §1]** *"Although the theoretical difficulty and importance of non-chord tone
  identification are addressed, few scholars have proposed complete, dedicated non-chord tone
  identification models."* No citation is attached; this reader met no earlier non-chord-tone model named
  or compared against on the two pages.
- **[FACT, p. 1 §1]** What is built: *"we construct a non-chord tone identification model based on deep
  neural networks (DNNs), trained on chorale music by J.S. Bach."*
- **[CONJECTURE, p. 1 §1 — the argument for the approach, in three sentences]** *"Machine learning of
  harmonic analysis is difficult due to the large number of chord classes, which require large amounts of
  training data to learn. In contrast, the relatively simple task of non-chord tone identification
  requires much less training data. Once non-chord tones are identified, harmonic analysis becomes a
  relatively simple task, which can be accomplished by a rule-based algorithm."* **None of the three
  carries a measurement or a citation on the page.** No count of chord classes is given, no
  training-data comparison is reported, and no rule-based algorithm is presented or named; whether one of
  the four references describes such an algorithm is not said on the pages.
- **[FACT, p. 1 §1, citing [2] He, Zhang, Ren & Sun]** *"Deep learning has achieved substantial success
  in numerous complex tasks, and sometimes even surpassing human performance [2]."* Reference [2] is an
  image-classification paper by its printed title.
- **[CONJECTURE, p. 1 §1]** *"DNNs are nonetheless relatively simple, suitable for our preliminary
  research."*

### §2.2 The data (§2, page 1)

- **[FACT, p. 1 §2]** *"This project draws on a convenient dataset, Rameau [3], consisting of 140 Bach
  chorales with expert harmonic annotations."* Footnote 1 gives where it was obtained: *"Available at
  https://github.com/kroger/rameau/tree/master/rameau-deps/genos-corpus."* The word *"convenient"* is the
  paper's own; this reader met no other stated reason for the choice of data. *(★ Corrected at the
  user-ordered check, §10; former wording, preserved (#12): "is the paper's own description of why this
  data was used" — the page calls the data set convenient and does not say that is why it was used.)*
- **[FACT, p. 1 §2]** How the labels sit on the music: *"Harmonic labels in the Rameau dataset are
  aligned with the music as salami-slices: a "salami-slice" is formed whenever a new note onset occurs in
  any musical voice."* (*"salami-slices"* and *"any"* are in italics on the page.) **The slice is defined
  by onsets alone**; the sentence says nothing about a note ending.
- **[FACT, p. 1 §2]** Transposition: *"To make the tonal relationships between picth-classes consistent
  across the dataset, we also transposed all the chorales into the same key."* (*"picth-classes"* is the
  page's spelling.) Which key, how the key of each chorale was known, and what was done with chorales in
  minor are not stated (§7).
- **[FACT, p. 1 §2]** Where the non-chord-tone labels come from: *"Non-chord tones can be identified and
  labeled from each chord label associated with the slice."* **This sentence is what this reader
  found on the pages about how the ground truth for the model's target was made**; Figure 2's caption and
  §4 name that ground truth and add no account of its making. The procedure is not given (§7).

### §2.3 The model's input and output (§3, pages 1–2; Figure 1, page 1)

- **[FACT, p. 1 §3]** Input: *"each slice is represented by a vector of twelve ones or zeros,
  representing which pitch classes (C, C#/Db, D, D#/Eb, etc.) are present (1) or absent (0) in the
  slice."* The enharmonic pairs are written as one class each, so spelling is not in the input.
- **[FACT, pp. 1–2 §3]** Metric information: *"Also, metric information about each slice was added to
  each input vector, specifically whether the current slice is on beat (1) or off (0)."*
- **[FACT, p. 2 §3]** Output: *"For the DNN's output we use a similar vector of length four, indicating
  which, if any, of the four voices contains a non-chord tone."*
- **[FACT, p. 2 §3 — the worked example]** *"The third slice in the second measure contains the
  pitch-classes D, G, A, and B, represented by the input vector [0,0,1,0,0,0,0,1,0,1,0,1]. The
  corresponding output vector for this slice [0,0,1,0] indicates that the pitch (A), which is the third
  "1" from the left in the input vector, is a non-chord tone."*
- **Two descriptions of the output stand on the page, recorded and not reconciled.** The general
  sentence says the four output positions are the four VOICES. The worked example explains the same
  output by counting the ones in the INPUT vector from the left — that is, by the order of the pitch
  classes present, which is not an order of voices. The two coincide in this example only if the voice
  holding the A is the third in whatever voice order the output uses; the page does not state that
  order, and this reader did not establish from Figure 1's notes, at the size rendered, which voice
  holds the A. Which of the two the model's output in fact encodes is therefore not settled by the
  pages as read.
- **[FACT, p. 1 Figure 1]** The figure prints, above a four-staff example labeled Soprano, Alto, Tenor,
  Bass: *"Input of DNN: [1,0,0,0,1,0,0,1,0,0,0,0] …… [0,0,1,0,0,0,0,1,0,1,0,1] ……"*; below the staves, a
  line *"Chord:"* with chord symbols under the slices, a line *"Non-chord tone:"* with the letter A under
  the second measure, and *"DNN output: [0,0,0,0] …… [0,0,1,0] ……"*. Caption: *"Figure 1. Non-chord tones
  in the first two measures of BWV 30/6 (transposed), and the corresponding DNN inputs and outputs."*
  **Both input vectors in the figure have twelve positions**; the on/off-beat value the text says was
  added is not shown in either. The chord symbols, as far as this reader could make them out at the size
  rendered (not load-bearing, and not checked a second way): first measure *C, G/B, C, Am/C, D, Bm/D*;
  second measure *C/E, D7, G/D, G/D, Am7/C, D, D7/C*.
- **[FACT, p. 2 §3]** *"The experimental settings were determined empirically (shown in Table 1)."* What
  was tried, and on which portion of the data the choice was made, is not stated.
- **[FACT, p. 2 §4]** The context window: *"Note that one slice adjacent (before and after) to the current
  one were added to the input vector, creating a windowed input that allows the model to consider
  context."*

### §2.4 The settings (Table 1, page 2) — whole, as printed

| Setting | Value, as printed |
|---|---|
| Network structure | 2 hidden layers, 200 nodes each |
| Optimizer | ADAM (Adaptive Moment Estimation) |
| Loss function | Binary cross-entropy |
| Data division | 8:1:1 (training:validation:test) |
| Evaluation metric | Precision, recall, F1-measure |
| Evaluation method | 10-fold cross validation |

Caption: *"Table 1. The DNN settings."* The word *"feedforward"* is met once on the two pages, in §5
(*"using feedforward DNN"*).

### §2.5 The paper's own reading of its results (§4 and §5, page 2)

- **[FACT, p. 2 §4]** Why these metrics: *"Because of the significant imbalance between the number of
  chord tones and non-chord tones (92% and 8%), we report the metrics of precision, recall, and
  F1-measure."* Beyond the count of chorales, the 92% and 8% are the one quantity this reader met on the
  pages about the data; what is being counted (notes, or voice positions per slice) is not stated.
- **[FACT, p. 2 §4]** *"As we can see, the model achieved F1-measure of 72.19%."*
- **[FACT, p. 2 §4, about Figure 2]** *"As we can see, the model is correct for the first six measures,
  with some errors in the rest of the chorale."* This reader checked that sentence against Figure
  2 only coarsely: at the size rendered, the second and third lines of text under the first system (a
  small numeral stands at the head of the second and of the third system, which this reader makes out
  as 4 and 7, so three measures to a system) appear to carry
  the same letters; under the second system no second or third line is visible; under the third system
  the two lines differ at some places. That is consistent with the sentence. The letters were not
  compared one by one, being too small for that.
- **[CONJECTURE, p. 2 §4]** *"Experienced music analysts will see that many of the "errors" in fact
  represent plausible analytical choices."* No count of such cases and no analyst's judgment is
  reported. **The sentence stands directly after the account of Figure 2 and speaks of the errors in that
  one illustrated chorale**; the page does not say it of the evaluation behind Table 2. Within that scope
  it is the paper's own statement that what it scores as an error can be a defensible reading (§5
  below). *(★ Corrected at the user-ordered check, §10; former wording, preserved (#12): "The sentence is
  the paper's own statement that its ground truth is one reading among several (§5 below)." — wider than
  the page, which attaches the sentence to Figure 2's chorale.)*
- **[FACT, p. 2 Figure 2 caption]** *"Figure 2. The first nine measures of BWV 389 "Nun lob, mein Seel,
  den Herren." The first line of text underneath the score is the original chord labels. The second line
  is the non-chord-tone ground truth (note names). The third line is the model's predicted non-chord
  tones."* Whether BWV 389 was in a training portion or a test portion when the shown output was
  produced is not stated.
- **[CONJECTURE, p. 2 §5]** *"With an F1-measure of 72.19%, we hope that better performances will be
  achieved with more higher-quality data."*
- **[FACT, p. 2 §5 — stated intent]** *"Thus, we intend to complete the whole Bach chorale dataset with
  371 chorales fully annotated with harmonic/contrapuntal labels."* And: *"Not only will this dataset
  help to train and test our model further, it will be useful for many other music analytical tasks."*

## §3 — Coupling facts (mandatory)

- **What the method assumes upstream (each located above):**
  - symbolic music in four voices (the output has four positions, §2.3; the data are Bach chorales,
    §2.2);
  - a segmentation into slices at each new onset in any voice, taken from the data set as given (§2.2);
  - **a chord label already attached to each slice by expert annotators** — the labels are the source of
    the target, so the model learns to reproduce a distinction that a human harmonic analysis has
    already made (§2.2);
  - **the key of each chorale, taken as known**: the chorales are transposed *"into the same key"* before
    training and testing, and the pages name no source for the key (§2.2, §7);
  - the metric position of each slice, as on the beat or off it (§2.3);
  - pitch classes without spelling (§2.3).
- **What the input does not carry, by the page's own description:** which voice holds which pitch class.
  The input is presence or absence of each of twelve pitch classes, plus the beat value, for the current
  slice and one slice each side. The output, by the general sentence at §2.3, is per voice. How a
  per-voice answer is to be got from an input with no voice information is not discussed on the pages.
  This is this reader's observation over the page's two descriptions; it is tied to the unreconciled
  point at §2.3 and is not a claim about what the authors' code did.
- **What it hands downstream:** for each slice, four values saying which voices hold a non-chord tone.
  The paper's stated purpose for that output is a harmonic analysis by *"a rule-based algorithm"* (§2.1);
  this reader met no such algorithm on the pages, and no downstream step is reported as built or measured.
- **Its stated scope:** Bach chorales; one data set of 140; a demo and *"preliminary research"* (§1.6).
  No claim about other repertoire was met on the two pages as read.

## §4 — Measured results, as the paper states them

### §4.1 Table 2, whole, as printed (page 2)

| Input features | PC + B + WS1 (D:42) |
|---|---|
| Precision | 86.02±3.35% |
| Recall | 63.14±10.81% |
| F1-measure | 72.19±7.68% |

Caption: *"Table 2. Model performances with a combination of input features. (PC: pitch-class; B: on/off
beat feature; WS: window size; D: dimension of the feature vector)."* **The table has one column of
results.** The caption's *"a combination of input features"* is singular, and no other combination's
result is printed on the two pages.

### §4.2 What the pages say the ± values are

Nothing that this reader found. The table prints a ± after each of the three values; neither the caption, §4 nor Table 1 says
whether it is a standard deviation over the ten folds, a standard error, or a range. Table 1's *"10-fold
cross validation"* makes a spread over folds the natural reading; that is this reader's inference and is
not on the page.

### §4.3 Arithmetic over the printed values (this reader's, not the paper's; done by hand)

- **The printed F1 is not the F1 of the printed precision and recall.** 2 × 86.02 × 63.14 ÷ (86.02 +
  63.14) = 10,862.6 ÷ 149.16 = 72.83 (to two places). The table prints 72.19. A difference of that kind
  is what results when each value is averaged over folds separately, since an average of per-fold F1
  values need not equal the F1 of the averaged precision and recall; **the page does not say how the
  three values were aggregated**, so that explanation is offered and not established.
- **The printed feature dimension does not follow from the text's description by this reader's count.**
  The text describes, per slice, twelve pitch-class values and whether the slice is on the beat *"(1) or
  off (0)"*, which reads as one value: thirteen per slice. A window of the current slice and one each
  side is three slices: 3 × 13 = 39. Table 2 prints *"D:42"*. 42 = 3 × 14, which would be fourteen values
  per slice, one more than the text describes; what the extra value would be is not said (a beat feature
  of two values is one possibility, and the pages do not single it out). *(★ Corrected at the user-ordered
  check, §10; former wording, preserved (#12): "that is, two values for the beat feature and not one" —
  one decomposition offered as if it were the only one, the same defect §9.3(c) finds in the first
  extract.)* The pages do not say how the beat
  feature is encoded beyond the sentence quoted at §2.3, so the difference of three is recorded and not
  explained.
- **Recall is the low value and carries the widest ±.** 63.14 ± 10.81 against 86.02 ± 3.35: by the
  printed values the model misses more than a third of the labeled non-chord tones on average (100 −
  63.14 = 36.86), and recall carries the largest of the three ± values. The paper does not remark on the
  difference between precision and recall.

### §4.4 What is not among the measured results

No baseline, no comparison with any other method or with a rule-based identifier, no result by
non-chord-tone type, no result by voice, no harmonic-analysis result, no result on any music outside the
140 chorales, no training or running time. Each of these is "met nowhere on the two pages as read".

## §5 — What the paper states about uncertainty, reproducibility and ground truth (against #24, #16, #21)

- **Uncertainty (#24):** each of the three values carries a ±, undefined (§4.2). No significance test is
  reported; no comparison between two systems or two settings is printed, so the pages hold no pair of
  values such a test would apply to.
- **Reproducibility (#16):** the data's location is given as a URL (footnote 1). Table 1 gives six
  settings. No code location is given. Not stated: the activation function, the learning rate, the
  number of training passes, any stopping rule, any regularisation, the threshold turning an output value
  into a yes or no, the software used, and any random seed (§7).
- **Ground truth (#21):** the chord labels are described as *"expert harmonic annotations"* from the
  Rameau data set [3]; the number of annotators, their procedure and any agreement between them are not
  stated on these pages. The non-chord-tone labels are derived from those chord labels by a procedure
  the pages do not give (§2.2). **The paper itself says, of the errors in the one chorale Figure 2 illustrates, that many are
  *"plausible analytical choices"* (§2.5)** — so by its own account some of what it scores as error there
  is disagreement between two defensible readings. No count is given, and the page does not say whether
  the same holds of the errors behind Table 2. *(★ Corrected at the user-ordered check, §10; former
  wording, preserved (#12): "The paper itself says that many of the model's "errors" are "plausible
  analytical choices" (§2.5) — so by its own account a portion of what Table 2 counts as error is
  disagreement between two defensible readings, and the size of that portion is not measured." — the page
  attaches the sentence to Figure 2's chorale, not to Table 2; the first extract's finding (4) has the
  scope right.)*

## §6 — Terms the paper uses, in the paper's sense

| Term | The paper's sense, with location |
|---|---|
| non-chord tone | *"elaborative notes, created by idiomatic step-wise melodic contours, which do not belong to the local structural harmony"* (p. 1 §1). This reader met no named type of non-chord tone on the pages. |
| salami-slice | the span *"formed whenever a new note onset occurs in any musical voice"* (p. 1 §2) |
| DNN | deep neural network (p. 1 Abstract); in Table 1, two hidden layers of 200 nodes; called *"feedforward"* once (p. 2 §5) |
| PC, B, WS, D | pitch-class; on/off beat feature; window size; dimension of the feature vector (Table 2 caption). *"WS1"* in the table is not expanded in the caption; §4's sentence about one slice before and after is this reader's ground for reading it as a window of one slice each side. |
| Rameau | the data set of 140 Bach chorales with harmonic annotations, cited as [3], whose printed title is *"Rameau: a system for automatic harmonic analysis"* |

## §7 — Stated ABSENT: things a reader might supply from the method class that the pages do not say

Each line below is "met nowhere on the two pages as read", not "printed nowhere".

- How a non-chord tone is decided from a chord label (for instance, whether a sounding pitch class
  outside the labeled chord's tones is the test, and what is done with sevenths, with added tones, or
  with a slice whose label is itself in doubt).
- The key the chorales were transposed to, where each chorale's key came from, and the treatment of
  chorales in minor. Figure 1's example, marked *"(transposed)"*, shows no key signature at the size
  rendered and its first chord symbol is C; that is one example and not a statement of the rule.
- Whether the division into training, validation and test portions was made by whole chorale or by
  slice. **This bears on what the 72.19% means**: if slices of one chorale fall on both sides of the
  division, neighbouring and repeated passages are seen in training and in test. The pages do not say.
- How *"8:1:1"* and *"10-fold cross validation"* combine (Table 1 lists both).
- The number of slices, of notes, and of non-chord tones in the data; this reader met *"140"* chorales and *"92% and
  8%"* and no other count of the data used.
- What unit the 92% and 8% count.
- The meaning of the ± values (§4.2) and how precision, recall and F1 were aggregated (§4.3).
- How the on/off-beat feature is encoded so that the dimension comes to 42 (§4.3).
- The voice order of the four output positions, and the reconciliation of §2.3's two descriptions.
- How slices at the start and end of a chorale, which lack a neighbour on one side, are given a window.
- Activation function, learning rate, training length, stopping rule, regularisation, output threshold,
  software, seed (§5).
- Any type of non-chord tone by name (passing, neighbour, suspension, anticipation and so on). The
  definition at §1 speaks of *"step-wise melodic contours"* and this reader met nothing further.
- Any earlier non-chord-tone identification method, by name or by citation.
- Any statement about tied or held notes. The slice definition is by onsets, and the input is pitch-class
  presence *"in the slice"*; whether a note struck earlier and still sounding counts as present is not
  stated.

## §8 — The read-back and the sweep (steps 4 and 5 of entry 169 §3), written after the text above was finished

### §8.1 The read-back against the pages

Both pages were requested a second time after §0–§7 were written, both images were present, and the text
above was checked against them: the quotations in §1 and §2, Table 1 and Table 2 cell by cell, the two
figure captions, the vectors printed in Figure 1, the two footnotes and the four references' titles as
used. **The quotations and the table cells that were checked agreed with the pages as written; this side
changed no quotation and no value at the read-back.** That is a statement about the places looked at.
What the read-back did change, each a defect of this side's own:

- **A description of Figure 2 wider than the image.** §1.5 said three lines of text stand under each of
  the figure's three systems. At the second look, no second or third line is visible under the second
  system. Now *"up to three lines"*.
- **A refusal that was too quick.** §2.5 said this reader did not check the paper's sentence about the
  first six measures against Figure 2. At the second look a coarse check was possible and is now
  recorded there, with its bound.
- **A musical judgment resting on small print.** §7 said Figure 1's chord symbols were *"consistent with
  C major"*. The symbols were read at a size this side itself calls not load-bearing; the sentence now
  says what is visible (no key signature at the size rendered; first symbol C).
- **Two assertions about an object not examined.** §0 and §1.4 called the bibliography row's last cell
  *"the tier"*. This side did not read the bibliography's column headings; it had the word from row 17's
  second extract. Both places now say what the cell reads and that its meaning was not read. This is the
  tell of citing a summary in place of the source, and it is counted as one.
- **A spread asserted from an undefined ±.** §4.3 said recall *"varies most"*. The ± is undefined (§4.2),
  so the sentence now says recall carries the largest of the three ± values.

### §8.2 The sweep for absolutes

The file was searched for *only, never, nowhere, every, all, none, nothing, anything, any, whole, always,
each, no*, and each hit was read at its line. Changed as wider than the act behind them, in the order met:
*"The pages print no harmonic-analysis result of any kind … rest on nothing measured"* (§2.1); *"no
earlier model is named or compared against anywhere on the two pages"* (§2.1); *"no rule-based algorithm
is presented, named or cited"* (§2.1 — this side does not know what the four references contain);
*"This is the whole of what the pages say"* (§2.2); *"the only description of the data's content"* (§2.5);
*"nothing downstream is built or measured here"* and *"The paper makes no claim about other repertoire"*
(§3); *"Nothing."* as the whole answer at §4.2; *"nothing is compared with anything"* (§5); *"No types are
distinguished anywhere on the pages"* (§6); *"only "140" chorales and "92% and 8%" are printed"* and *"the
pages go no further"* (§7). Each now says what this reader met on the two pages as read. Left standing
after being read at their lines: the banner's *"NOTHING HERE IS RULED"*; *"Every mechanism statement below
is therefore located to a page"* (§0 — a statement of this file's own method, and the read-back found no
mechanism statement without a location); the absences at §4.4 and §7, which carry the bound *"met nowhere
on the two pages as read"* at the head or foot of their lists; and the words inside quotations.

### §8.3 What this file rests on, and what it does not

- The two page images, read twice. No text layer of the PDF was read; every quotation was typed from the
  image, so a slip of this side's in typing is possible and the cross-check at §9 is one test of that.
- The arithmetic at §4.3 was done by hand and repeated once: 86.02 × 63.14 = 5,431.30; doubled,
  10,862.61; divided by 149.16, 72.83. 3 × 13 = 39; 3 × 14 = 42.
- Nothing outside the two pages was consulted about this paper: no web access, no other copy, none of
  the four references.
- The first extract had not been opened when this section was written.

## §9 — The cross-check against the first extract (step 7 of entry 169 §3), written after §0–§8 had landed

### §9.1 What was compared, and its bound

§0–§8 landed first (34,393 bytes, modification time 1789785448060, proved at content and at its last
line). Then the first extract — the same file name under `reading_pass/extracts/`, 46,124 bytes,
modification time 1789151182710 — was read whole, 537 lines, in one call. Page 1 was then requested a
third time and the disagreements below were read at its image; page 2's were read at the two earlier
images of it. **The comparison ran over what both extracts carry about the paper's pages.** The first
extract's record-facing half — what `FRAMEWORK.md`'s design point DP-D, `population.md` V11, D-527 and the
other records say about this paper, its routings, its cross-primary check and its centrality verdict —
was read and **not checked**: of those records this side read the decisions register's index line for
D-527 (§0) and opened no other (entry 169 §5(vii)). *(★ Corrected after the second landing, at this
side's own re-read of §9; former wording, preserved (#12): "this side opened none of those records" —
wider than the fact, since D-527's index line was read at boot and is declared at §0.)*

### §9.2 Where the two reads agree

At each place the comparison reached, the values both reads transcribed agree: Table 2's three cells with
their ± values and its column heading; Table 1's six rows; both vectors of the worked example and both
input vectors of Figure 1; 140 chorales; 92% and 8%; 371 chorales; the 72.19% at the Abstract, §4 and §5;
the four references. Both reads, apart, found "DLfM" on neither page, found a CC BY 4.0 licence printed
against the bibliography row's LINK, found the ± undefined and the table to hold one configuration, found
the rule-based-analysis sentence of §1 stated and neither built nor measured, and read the "plausible
analytical choices" sentence as unquantified. Both derived, apart, that about 37% of labeled non-chord
tones are missed (100 − 63.14).

### §9.3 Where the paper goes against the first extract — three sites, none moving a value, a cell, a derived number, a finding or a verdict

Line numbers are the first extract's before the act of §9.6. *(★ Corrected at the user-ordered check,
§10; this sentence formerly pointed at §9.5, which is not the act.)*

- **(a) Inside a quotation, line 172:** *"between pitch-classes consistent"* for the page's *"between
  picth-classes consistent"* — the page's misspelling silently corrected.
- **(b) Outside quotations, lines 178–181:** under the words *"Three things this states in terms"*, the
  first extract says a note is a non-chord tone in the ground truth *"exactly when it is outside the
  annotated chord of its slice"*, and that Figure 1's non-chord-tone line *"is read off"* its chord line.
  The page says non-chord tones *"can be identified and labeled from each chord label"* and states no
  criterion. That the labels are derived from the chord labels is on the page; the criterion is not. The
  first extract's finding (5) rests on the first of those and is untouched.
- **(c) Outside quotations, lines 191–193:** the first extract explains Table 2's *"D:42"* as *"three
  slices of 12 + 1 + 1 = 14"*, marked as derived. The page gives twelve pitch-class values and one
  on/off-beat value per slice; the second *"+ 1"* has no referent on the page. This side's §4.3 found the
  same 42 and left it unexplained (3 × 13 = 39). The paper settles neither reading; what it goes against
  is the first extract's *"is that"*.

A rendering remark, not counted as a site: the first extract sets Table 1's values in italics, lowercased
and with *"(Adaptive Moment Estimation)"* dropped after ADAM. They are not in quotation marks and no
value differs.

### §9.4 ★ Three wordings NOT corrected, because they stand inside or beside numbered findings — with the user

The standing rule (entry 198 §7) keeps for the user what touches a finding. Each of these is a word the
page does not print, standing in the first extract as if the page's; none moves a value.

- **The key's source — finding (9), and lines 295–297 and 357–358.** Finding (9) reads *"THE KEY IS AN
  ORACLE. §2 in terms"*; the coupling facts say *"an oracle key, never decided by the system and never
  changing within a chorale"*; the design-point paragraph says *"with the key supplied by hand"*. The
  page says *"we also transposed all the chorales into the same key"* and names no source for the key —
  which the first extract itself says in the same sentence of its coupling facts (*"its source
  unstated"*, line 296) *(★ corrected at the user-ordered check, §10; former wording, preserved (#12):
  "says two lines earlier" — the words are in the same sentence as "an oracle key", and about sixty lines
  before "supplied by hand")*. That a key is taken as
  given is on the page; *"oracle"*, *"supplied by hand"* and *"never changing within a chorale"* are not.
  **This is the same shape as the item entry 198 §9 leaves with the user for row 17's first extract**
  (*"supplied by hand"* there too), and the two are best put to him together.
- **The unit of the 8% — finding (10), and lines 221–227.** The first extract reads the 92% and 8% as
  shares of *"voice-slice slots"*. The page's words are *"the number of chord tones and non-chord tones"*;
  the unit is not stated further. The first extract's derived error shares (about 5.05%, 2.95%, 0.82%,
  3.8%) are arithmetic over the printed values and this side re-did them by hand and agrees with them as
  arithmetic; their unit inherits the gloss.
- **The output's indexing — finding (8).** Finding (8) reads *"THE OUTPUT IS PER VOICE, FOR FOUR VOICES.
  §3 in terms."* The general sentence of §3 does say so in terms. The worked example on the same page
  explains the same output by the position of a one in the INPUT vector (this file's §2.3), which the
  first extract quotes and does not remark on. The finding is not refuted by this; it is less settled by
  the page than *"in terms"* suggests.

### §9.5 What the first extract shows about this one

Nothing that this side found to correct here: no value, quotation or location in §0–§8 is contradicted
by the first extract. *(★ Corrected at the user-ordered check, §10, and left standing (#12): that sentence
missed one. The first extract's finding (4) scopes the "plausible analytical choices" sentence to Figure
2's one chorale, which is what the page does; this file's §2.5 and §5 read it more widely, as if of Table
2's errors, and the cross-check did not notice. Corrected at both sites.)* Two differences of treatment, recorded: the first extract files the three-sentence
argument of §1 under a FACT heading as the paper's stated design and marks its last sentence CONJECTURE
separately, where this file marks all three CONJECTURE; both say the same of their standing (stated, not
measured). And this file carries two pieces of arithmetic the first does not (the F1 of the printed
precision and recall, 72.83 against the printed 72.19; and 39 against 42), while the first carries one
this file did not (the error shares above).

### §9.6 The act under the standing rule

Sites (a), (b) and (c) were corrected in the first extract at their sites, each with a "★ CORRECTED
2026-09-19" note outside any quotation and the former wording preserved (#12), and a banner note records
the ruling. At (c) the sentence was left standing and the correction is the note. The three wordings of
§9.4 were not touched. The landing figures of both files are in handoff entry 199.

*(★ Made stale the same day, and left standing (#12). The user ruled on §9.4's item on 2026-09-19 — his
words, in reply to the surface that recommended it: "I agree with your recommendation." — and the three
wordings of §9.4 were then corrected in the first extract at their sites, each with a note and the former
wording preserved. §9.3 and §9.4 above are unchanged, and their line numbers are the first extract's
before either act. The account and the landing figures are in handoff entry 199 §8.)*

## §10 — ★ The user-ordered check after landing, written in the act that ran it

On the user's instruction (fact- and source-check what was written, for completeness, coherence,
correctness and misuse of absolutes), this file was re-read WHOLE, 527 lines in one call, at the device's
landed copy staged back (41,875 bytes). The page images were not requested again; the two earlier
requests of page 2 and the three of page 1 were still before this side, and the claims below were checked
against them and against the first extract as read. **It did not come back empty.** Corrected at their
sites with the former wording preserved:

- **A claim wider than the page, and the one that matters.** §2.5 and §5 read the *"plausible analytical
  choices"* sentence as the paper's account of its errors generally, §5 naming Table 2. The page attaches
  it to the one chorale of Figure 2. The first extract's finding (4) has that scope right, and this
  file's §9.5 had said the first extract contradicted nothing here; that sentence is corrected too.
- **One decomposition offered as the only one.** §4.3 said 42 = 3 × 14 means *"two values for the beat
  feature"*. The pages do not single that out.
- **A gloss on one word.** §2.2 said *"convenient"* was the paper's description of why the data was used.
- **Two pointers wrong.** §9.3 pointed at §9.5 for the act, which is §9.6; §9.4 said *"two lines earlier"*
  of words that stand in the same sentence. And §9.4's *"findings (9)"* is now *"finding (9)"*.

**Read at their lines again and left:** the absences at §4.4 and §7 under their bound; §1.5's *"No
numbered equation"* and §2.4's *"met once"*, both over two pages read whole at the images; §3's
observation that the input carries no voice information, which is marked there as this reader's.
**What the check did not do:** re-request the pages, re-read the first extract (its corrected sites were
proved at content when they landed), or open any record not already read. Nothing here says a further
pass would come back empty.

# Second extraction — Sailor, "RNBERT: Fine-Tuning a Masked Language Model for Roman Numeral Analysis"

> **STATUS: SECOND INDEPENDENT EXTRACTION.** This file is the second of two independent reads of
> one paper, written under the reading commission's rule that a CENTRAL source is extracted in a
> second pass that does not consult the first extract, the two then cross-checked, and every
> disagreement resolved at the paper or recorded as unresolved. ***★ THAT STATEMENT OF THE RULE IS
> A RELAY and is marked as one at its own site: it is taken from the hundred-and-sixty-ninth handoff
> entry's §3, which quotes the commission's §4. **Neither commission was opened by this side.***
>
> **WHAT IT IS NOT.** It is not a summary of the first extract, not a review of it, and not a
> correction of it. Where the two disagree, §9 records the disagreement and where the paper
> settles it.
>
> **THE FORM THIS FILE FOLLOWS IS A RELAY AND IS DECLARED AS ONE.** Neither the original reading
> commission nor the remedial one was opened by this side. The eight-step procedure and the
> required content of an extract — claims labeled FACT / THEORY / CONJECTURE, the coupling facts
> mandatory, measured results as the paper states them, the closing section absent until the
> read-back has run — were taken from the hundred-and-sixty-ninth handoff entry's §3, read whole
> at a staged copy this sitting. **This is the ninth sitting running whose compliance with the
> commission's own form is a relay rather than a reading of it**, the count for the eight before
> it being relayed through the hundred-and-eighty-second entry, which says eight.
>
> **THE SECTION FORM** is this line's own, taken from row 49's second extract at its section
> headings alone, by a heading search. **No content line of that file was read.**

---

## §0 — What was read, and the bound on this read's independence

### What was read for this extract

- **The paper whole, all eight pages**, as page images over a staged copy of
  `docs/research_papers/sailor_2024_ismir_rnbert.pdf` — **707,204 bytes** at this sitting's own
  staging call. Requested as pages 1–4 and 5–8. **Every image was checked at the image itself and
  not at the call's success line**, and all eight were present and legible.
- **The page count was established AT THE TOOL** by a deliberately out-of-range request, which
  answered *"PDF has 8 pages"*. **It had a relayed figure to match against and it matches**: the
  hundred-and-eighty-second entry's table gives this file's size, and eight pages is what that
  entry's own member ran to. *(The size matches at the byte; the page count is established here
  and is corroborated by no entry, no entry of the line stating one for this row.)*
- **Row 49's second extract at its SECTION HEADINGS ALONE**, by a heading search, to take this
  line's own section form rather than invent one. **No content line of that file was read.**

### What was NOT read, and the contamination that is declared rather than claimed away

- **Row 50's first extract was NOT opened.** Its path and size are known from the
  hundred-and-eighty-second entry's published table —
  `reading_pass/extracts/sailor-2024-rnbert-fine-tuning-a-masked-language-model-for-roman-numeral-analysis.md`,
  **65,160 bytes** — and the file itself stays closed until step 7. **This file is landed at the
  matching name in `reading_pass/extracts_second_pass/` before that step**, which this line's
  convention requires and which the previous sitting could not do, having no published name to
  use.
- **`reading_pass/candidacy_upgrades.md` was NOT opened.** The hundred-and-eighty-second entry
  publishes row 50's identity, so the reason column that would say why the record values this
  paper never reached this side. That entry states in terms that a next side taking row 50 from
  its table need not open that file and should not.
- **`reading_pass/l2_slice_reading_progress.md` was NOT opened at all**, so no verdict cell about
  this paper reached this side.
- **No sweep of the repository was run for this paper** — not for its author, not for its title,
  not for its model name, not for any of its values. **This side therefore asserts nothing about
  what the record says of it.**

### ★ THE CONTAMINATION THAT IS REAL, STATED EXACTLY

**The boot put a neighbouring paper's content in this side's head, and this paper reports figures
for that very paper.** The hundred-and-eighty-second entry, read whole here, is the second
extraction of row 49 — Karystinaios & Widmer's *ChordGNN* — and **ChordGNN is one of the two
prior models whose results this paper transcribes into its own Table 4.** That entry carries
statements about ChordGNN's post-processing gains, its table's uncertainty column and its task
count.

Two consequences, and both are bounds rather than mitigations:

1. **No ChordGNN value is imported into this file.** Table 4's lines 1 and 2 are transcribed from
   this paper's own printed page and from nowhere else, and this read takes no position on
   whether they agree with what those prior papers print. **That comparison is available to a
   later reader and was not made here.**
2. **★ ONE METHOD IN THIS FILE IS NOT THIS READ'S OWN IDEA, AND IT IS DECLARED AT ITS SITE AS WELL
   AS HERE.** The test at §6.1 — checking a composite Roman-numeral accuracy against the product
   of its own component accuracies — **came from the hundred-and-eighty-second entry**, which
   records the previous member's read finding that shape and itself declares that it took the idea
   from the entry before it. **The arithmetic here is this read's own on this paper's printed
   values; the idea of looking is not.** It is now a method travelling down a handoff line by
   relay, which is worth a next side's notice: the boot transmits another member's methods as well
   as its numbers.

### The independence bound, stated plainly

This side read the newest handoff entry before opening the paper, as the boot requires. That entry
names this paper's author, model, venue and year, and the size of its held file. **So the
member's IDENTITY was known before the paper was opened, and §1.1 records the identity as a
confirmation at the document's own face rather than as a discovery.** Nothing else about this
paper's content reached this side from any source before the paper was read.

---

## §1 — What the paper is, and the identity axis

### §1.1 The identity, as the document itself prints it

- **Title, as printed:** "RNBERT: FINE-TUNING A MASKED LANGUAGE MODEL FOR ROMAN NUMERAL ANALYSIS".
  *(The title is set in capitals throughout, so its capitalisation of the model name is not
  evidence of a spelling — see §7.1.)*
- **Author:** **Malcolm Sailor**, a single author. **Affiliation: Yale University.** Contact
  address printed beneath it.
- **Licence and venue, from the attribution box on page 1:** "© M. Sailor. Licensed under a
  Creative Commons Attribution 4.0 International License (**CC BY 4.0**). **Attribution:** M.
  Sailor, "RNBert: Fine-Tuning a Masked Language Model for Roman Numeral Analysis," in *Proc. of
  the 25th Int. Society for Music Information Retrieval Conf.*, San Francisco, United States,
  2024."
- **Code release, footnote 1 on page 1:** "We release the code to reproduce our results at
  `https://github.com/malcolmsailor/rnbert`."
- **What is NOT printed anywhere in the eight pages as read:** no DOI, no proceedings pagination,
  no running header, and no printed page number. **This is a bounded negative over the eight pages
  as read and not a claim about the published record.**

**★ THE IDENTITY AXIS CLOSES CLEANLY HERE, AND THAT IS A DIFFERENCE FROM THE MEMBER BEFORE IT.**
The register's description of this row — *Sailor, ISMIR 2024, RNBERT* — names an **author**, a
**venue**, a **year** and a **model**, and **all four are confirmed at the document's own face**:
the author on the title block, the venue and year in the attribution box, and the model name in
the title and throughout the body. **The hundred-and-eighty-second entry records that its own
member's register row named no author at all and gave the paper only by its model name**, so that
identity closed against the document alone. **This one does not**, and the tie between the row and
the held file — which that entry declares to be its own matching and not a tie any source states —
**is therefore confirmed at the paper's own face here, exactly as that entry asks a next side to
do.**

### §1.2 ★ WHAT THE IDENTITY AXIS LEAVES OWED

- **The proceedings copy, not an arXiv deposit.** The attribution box is the ISMIR
  camera-ready form and no arXiv stamp appears in the eight pages as read. *(This differs from the
  member before it, whose held file the previous entry records as the arXiv deposit. **No claim is
  made here about whether an arXiv version of this paper exists.**)*
- **The venue string is "25th Int. Society for Music Information Retrieval Conf.", San Francisco,
  2024.** The register's "ISMIR 2024" is confirmed at the document's own face and not merely at
  the register.
- **★ THE MODEL'S SPELLING IS SETTLED BY THE DOCUMENT, AND THE CONTRARY CLAIM THIS FILE FIRST MADE
  WAS STRUCK AT THE READ-BACK.** The **body prints RNBert without exception**, and so does the
  attribution box in the licence footnote. The **title** prints RNBERT, but the title is set in
  capitals throughout, so it is not evidence of a distinct spelling; the code repository is
  lower-case `rnbert`, which is ordinary for a repository name. **There is no inconsistency**, and
  the register's *RNBERT* is the title's capitalisation.
  *(★ CORRECTED AT THE READ-BACK, page 1 re-opened. **FORMER WORDING, PRESERVED (#12):** "The
  model's spelling is not settled by the document. See §7.1." — together with a §7.1 entry claiming
  the name was "spelled two ways in the document" and naming the attribution box as one of them.
  **The attribution box prints RNBert, the same as the body.** The defect was this side's, found by
  re-opening page 1 — **the page the previous sitting's own check records itself as having failed to
  re-open.**)*

### §1.3 What the paper is about, in the paper's own frame

The paper's own statement of what it does, from the abstract: *"this paper applies pretraining
methods to a music theory task by fine-tuning a masked language model, MusicBERT, for roman
numeral analysis. We apply token classification to get a chord label for each note and then
aggregate the predictions of simultaneous notes to achieve a single label at each time step. The
resulting model substantially outperforms previous roman numeral analysis models."*

The gap it says it fills, from its §1 and §2, in its own terms:

- **Roman numeral analysis models are trained from scratch on scarce labeled data**, while
  symbolic music itself is plentiful.
- **Pretrained symbolic-music models exist but have been fine-tuned on sequence-level tasks** —
  composer, genre, emotion classification — *"requiring little explicit music theory"*.
- **The two have not been joined**: *"As far as we know, none of these pretrained models have been
  applied to Roman numeral analysis, or any other problem involving the prediction of explicit
  music-theoretical labels."*

Its own statement of why pretraining should help, from §1: *"in order to perform a self-supervised
task, the model can be expected to learn latent representations of music theory concepts like
chords and scales: if you need to predict a given musical note, you will do a lot better if you
can estimate the expected key and chord."*

And its own framing of the problem's difficulty, from §2: Roman numeral analysis of symbolic music
is *"both an easier and a harder problem"* than audio chord recognition — *"Easier, because
working with symbolic data means the model does not need to devote capacity to identifying the
sounding pitches, but harder, because Roman numeral analysis requires not only identifying chords
but also describing their harmonic function within their tonal context (e.g., rather than simply
labeling a chord as "E major", labeling it as "V6/vi in C major")."*

---

## §2 — The method, as the paper states it

*Every subsection names the paper's own section and the PDF page it was read at. **The PDF prints
no page numbers of its own**, so every page reference in this file is a position in the eight-page
file as staged, counted from the title page as 1.*

### §2.1 The lineage the paper places itself in (its §2, PDF pages 1–2)

- **Audio chord recognition** has an extensive literature and is set aside as a different problem.
- **Roman numeral analysis of symbolic music** is the smaller body of work this paper joins.
- **The deep-learning lineage, in the paper's own grouping:** *"recurrent models [4–7],
  transformers [8, 9], and, most recently, graph-based architectures [10]."*
- **The paper names the two best prior performances in the literature as it sees it:**
  *"As far as we know, the best performance in the existing literature has been obtained by
  AugmentedNet [6,7] and ChordGNN [10], and we compare our results below with those reported in
  [6, 10]."*
  **★ THE LOAD-BEARING WORDS ARE *those reported in*.** Table 4's lines 1 and 2 are figures this
  paper takes from those two papers. **They are not re-measurements by this paper, and nothing in
  the eight pages as read says the prior models were re-run here.** A consumer of Table 4 must
  carry that: two of its six lines are quotations.
- **One prior result is excluded from comparison and the reason is given**, at footnote 2:
  *"Unfortunately, the results of [7] are reported in a manner that makes them difficult to compare
  directly with these other papers and with our own results."*
- **The pretraining lineage:** MusicBERT [11] — the model used here — and MidiBERT-Piano [12]
  pretrain BERT-like encoder-only transformers on a masked language modeling task; [14] adds a
  GPT-like causal language modeling task.

### §2.2 The corpus (its §3.1, PDF page 2)

- **The claim it opens with:** *"To our knowledge, the corpus used in this study is the largest yet
  assembled for Roman numeral analysis."*
- **Its named components:** the corpora released by the Digital and Cognitive Musicology Lab
  [15–17]; the **TAVERN** set of theme and variations by Beethoven and Mozart [18]; the Beethoven
  Piano Sonatas first movements introduced in [4]; and the other items in the **When in Rome**
  meta-corpus [19], *"including analyses of Bach preludes and chorales, and a large number of 19th
  century lieder, including works of women composers."*
- **Two datasets are used**, and Table 1 gives both (transcribed at §5.1): the full corpus ("All")
  and a subset called **"AugmentedNet v1"**.
- **Why the subset exists:** *"For a fair comparison with [6, 10], we also train and evaluate on
  the subset of our data used in those papers, employing the same training/validation/testing
  splits."*
- **★ THE SUBSET IS NOT A PLAIN SUBSET, AND THE PAPER'S OWN NEXT SENTENCES SAY SO.** *"Note that,
  for scores having two analyses (in particular, the scores of the TAVERN dataset, where each score
  was analyzed by two separate annotators), AugmentedNet v1 includes both versions (following [6]),
  whereas in the full corpus, we randomly choose only one of the two versions for inclusion.
  AugmentedNet v1's note count is substantially increased by the inclusion of these duplicate
  TAVERN scores, which comprise 106,981 notes."* So the thing called *the subset of our data*
  contains analysis material the full corpus deliberately excludes. See §6.7.
- **Seven scores were dropped, and the direction of the resulting bias is stated**, at footnote 3:
  *"7 scores from AugmentedNet v1 were excluded because of preprocessing errors (for example,
  because they include time signatures not supported by MusicBERT's OctupleMIDI encoding scheme).
  These scores exclusively came from the training split and so, if their omission has any effect on
  RNBert's performance relative to that of the other models trained on the AugmentedNet v1 dataset,
  it should bias it downwards."*
- **A deliberate refusal to sub-set further:** *"Unlike some prior work (e.g., [6, 9]), we do not
  experiment with training and/or evaluating on smaller, more homogenous subsets of our corpus (for
  example, the Beethoven piano sonatas only). Our goal is to train the best and most general Roman
  numeral analysis model we can and we expect that such a model will be best obtained and evaluated
  by using as much data as possible."*

### §2.3 The data representation and the preprocessing chain (its §3.2, PDF pages 2–3)

**The input formats and the conversion.** *"The scores associated with the analyses in our dataset
are encoded in a variety of formats, such as MusicXML (.xml or .mxl), MuseScore (.mscx), or
Humdrum (.krn). We convert these into a tabular format, illustrated in Table 2, labeling each note
with the associated key and chord annotation."*

**The preprocessing chain, in the paper's own order and with its own reasons.**

1. **Quantization.** *"First, following MusicBERT, the score is quantized at the 64th note level."*
2. **Salami-slicing.** *"Second, we "salami-slice" the score: at each timestep with one or more
   onsets or releases, we split any ongoing notes into two, in order to obtain a purely homophonic
   rhythmic texture in which all onsets and releases are synchronized across all parts. (The term
   "salami-slicing" is due to [20].)"*
   **Its stated purpose:** *"Salami-slicing is necessary to ensure that each note belongs to only
   one chord. Otherwise, a note may persist through multiple changes of chord, either because it is
   a common tone among each of the chords (like the alto D in Figure 1), or because it realizes a
   suspension or similar dissonant idiom (like the soprano G in Figure 1)."*
   **Its stated harmlessness, which is an argument and not a measurement:** *"Fortunately for our
   purposes, salami-slicing should not affect harmonic analysis, because it does not change the
   pitch content of the score. Moreover, musical idioms like suspensions and pedal tones that cross
   changes of chord are analyzed the same whether or not they are tied or sounded anew at the onset
   of the new chord."* **No measurement of this is reported in the eight pages as read.**
3. **Dedoubling.** *"Third, we dedouble the notes of the score, removing any notes that have the
   same pitch, onset, and release (regardless of whether they are performed by the same
   instrument)."*
   **Two stated advantages:** it reduces the sequence length; and *"it produces a more homogeneous
   texture between music for small ensembles, where pitch doubling is less common, and music for
   large ensembles like orchestras, where pitch doubling is ubiquitous."*
   **Its stated motivation, which is a generalisation argument:** *"Such homogeneity is particular
   desirable since nearly all the available labeled scores are small-ensemble works like piano
   sonatas and string quartets, but we would like our model to generalize to large-ensemble works
   like symphonies and operas."* **Whether it does so generalize is not measured in the eight pages
   as read** — the corpus is the labeled small-ensemble material throughout.
4. **Cropping.** *"MusicBERT has a maximum sequence length of 1000 tokens. Therefore, in both
   training and evaluation, we crop scores into segments of 1000 tokens, stepping through the score
   with a hop size of 250."*

**Pitch is unspelled, and the paper says why:** *"Note that, because we use a model that was
pretrained on MIDI data, which does not specify pitch-spelling, our pitch inputs are not spelled
(that is, they use midi numbers like "78" rather than pitch names like "F#5")."*

**Figure 1 and Table 2** are the worked example of the chain and are transcribed at §5.2.

### §2.4 The task decomposition (its §3.3, PDF page 3)

**What a Roman numeral is, in the paper's own account:** integers indicating the chord's root with
respect to the scale of the current key; figured-bass numerals appended for inversion; quality
alterations by several conventions (case for major/minor, "+" or "o" for augmented or diminished,
figured-bass numerals with accidentals); accidental prefixes for altered scale degrees; secondary
Roman numerals after a slash for tonicizations; **and the key, because *"since the Roman numeral
only indicates a harmony with respect to some key, for a Roman numeral to be meaningful, we need to
indicate the key as well."***

**★ THE DECOMPOSITION, AND THE COST THE PAPER ATTACHES TO IT.** *"Since a complete Roman numeral
consists of multiple distinct elements, the combinatorial space of these elements is very large.
Encoding each distinct combination as a token, would require a large and sparse vocabulary, posing
challenges for training and generalization. Therefore, the approach adopted here and elsewhere is
to treat Roman numeral analysis as a multitask learning problem, where we **predict the key,
quality, inversion, and degree separately**. (The degree is sometimes further decomposed into
"primary" and "secondary" components, but in the current work, we predict these jointly.)"*

**So the task set is FOUR: key, quality, inversion, degree** — with the root added as a fifth only
for the AugmentedNet v1 comparison (§2.12). **The count is stated once and enumerated once and the
two agree**, and it agrees again with §4's own restatement — *"RN₋root refers to the conjunction of
degree, quality, inversion, and key"*. **This is checked because the neighbouring member's paper
fails exactly this check**, and this one does not.

**★ THE DECOHERENCE PROBLEM, WHICH IS THE PAPER'S OWN NAMED COST AND IS THE DESIGN PRESSURE BEHIND
ITS §3.6.** *"It should be noted, however, that this multitask approach **may obtain** a smaller
vocabulary size at the expense of some coherence among the different elements of the Roman numeral.
For example, suppose there is a passage that is ambiguous between I and vi6 (two chords which share
two of their three pitch-classes as well as the same bass note). If the model distributes the
probability roughly equally between the two possibilities it may equally occur that the inversion
and degree predictions "decohere" and we end up with a plainly incorrect prediction like I6 (rather
than I) or vi (rather than vi6)."*

*(★ **CORRECTED AT THE CROSS-CHECK, AGAINST THIS SIDE. FORMER WORDING, PRESERVED (#12):** "this
multitask approach **obtains** a smaller vocabulary size". **The paper prints *may obtain***,
established at a third opening of page 3, and the first extract had it right. **The error is not
neutral in kind: it turned the author's HEDGE into an assertion**, in the one sentence where the
paper concedes what its own decomposition costs. **The read-back did not catch it** — that pass
checked that the passage said what this file said it said, not that the quotation was exact, which
is a different act.)*

*(★ **AND ONE WORD OF THE SAME SENTENCE IS RECORDED UNRESOLVED.** This read has *"it may **equally**
occur"* at three openings of page 3; the first extract has *"it may **easily** occur"*. **This side
does not claim it.** The clause *"roughly equally"* stands eight words earlier, which is exactly the
condition under which a reader repeats a word it has just read — so the priming risk here falls on
THIS side's reading and not on the other's, the reverse of the *works of women composers* case at
§9.3(d). **The sense is unchanged either way and no value moves.** Recorded as unresolved at the
paper, which the commission's own rule provides for.)*

*(The worked example closes: in a major key, **I** is the tonic triad and **vi6** is the submediant
triad in first inversion; in C major those are C–E–G and A–C–E, which share C and E — two of three
pitch classes — and both have C in the bass. **Checked at the paper's own words and not imported.**)*

### §2.5 Pitch spelling (its §3.3.1, PDF page 3)

**The difference from prior work is named:** *"One difference between our approach and some prior
work (e.g., [5, 7]) is that MusicBERT uses unspelled pitch inputs (midi numbers like "67") rather
than letter names (like "F#5"). Our output key predictions are therefore also unspelled (e.g.,
pitch-class 6, rather than F-sharp), because, with unspelled inputs, the output spelling is
undefined."*

**Footnote 4 gives the ground for calling it undefined:** *"This is because the only difference
between enharmonically equivalent keys like F-sharp and G-flat is how they are notated. Certain
pieces of music, such as Fugue no. 8 of Bach's Well-tempered Clavier, Book 1, have even been
variously printed in two enharmonically equivalent keys [22]."*

**★ THE PAPER'S DEFENCE OF THE LOSS IS TWO CLAIMS, BOTH UNMEASURED, AND THEY ARE SEPARABLE.**
*"We consider our model's inability to predict spelled keys unimportant. Given spelled inputs
(e.g., pitches like "Db5" rather than MIDI numbers like "61") and an unspelled key (e.g., "1
major"), predicting a spelled key (e.g., "Db major") is trivial and could likely be performed with
perfect accuracy by a rule-based algorithm (e.g., taking the enharmonically equivalent key closest
to the centroid of the spelled pitches on the "line of fifths" [23]). Moreover, keys with plausible
enharmonic equivalents (like F-sharp major or E-flat minor) are rarely used. Their classification is
therefore unlikely to significantly affect validation/test performance."*

The two claims are: **(a)** a rule-based recovery *"could likely be performed with perfect
accuracy"*; and **(b)** enharmonically ambiguous keys are *"rarely used"* so their misclassification
is *"unlikely to significantly affect"* the reported figures. **Neither carries a number, a
measurement, or a citation to one, anywhere in the eight pages as read.** Both are labeled at §4.

### §2.6 Data augmentation (its §3.4, PDF page 3)

- **Transposition:** *"we transpose each score to all 12 keys of the chromatic scale."*
- **Duration scaling:** *"we create a version of each score with the durations scaled by a factor
  of 2. If the mean duration in the score is greater than the mean duration of the training set as
  a whole, we scale the durations down by 2; if it is less, we scale them up by 2."*
- **Synthetic data was tried and rejected, with a reason offered:** *"We experimented with adding
  synthetic data similar to the procedure introduced in [6,7] and also adopted in [10]. However, we
  did not find that it improved the model performance. It is possible that synthetic data was less
  helpful in our case than with AugmentedNet [7] because, whereas for that model, the inputs consist
  of pitch-vectors at each time step, for our model, the inputs are simply the notes of the score,
  and therefore the difference between synthetic and real data is more apparent to the model."*
  **The negative result is stated without a figure**, and the explanation is offered as a
  possibility, in the paper's own words.

### §2.7 The pretrained model and its encoding (its §3.5.1, PDF pages 3–4)

**What MusicBERT is, in the paper's words:** *"The model that we fine-tune, MusicBERT [11], is a
bidirectional transformer encoder pretrained on a masked language modeling task. The dataset for
pretraining is a corpus of over 1 million midi files, 3 orders of magnitude larger than our Roman
numeral dataset. This difference in scale motivates the use of a pretrained model."*

**Why this pretrained model and not another, with the alternative named:** *"We chose MusicBERT for
our experiments because, of the pretrained symbolic music models of which we are aware, it used the
largest pretraining dataset (by comparison, [12] pretrains on fewer than 5,000 scores of exclusively
piano music) and also because of the elegance of the OctupleMIDI scheme MusicBERT uses to encode its
inputs. A more detailed comparison fine-tuning symbolic music models for Roman numeral analysis will
have to await further work."*

**★ THE OCTUPLEMIDI ENCODING, AND THE PLACE WHERE THE PAPER'S COUNT AND ITS OWN LIST DISAGREE.**
The paper prints: *"In the OctupleMIDI encoding, **eight** features of a musical note are first
embedded individually: time signature, tempo, bar number, metric position within the bar, pitch,
duration, and velocity. To obtain a single input at each time step, these **eight** embeddings are
concatenated and then projected to the model's embedding dimension."*

**The list beside the word *eight* names SEVEN items** — time signature, tempo, bar number, metric
position within the bar, pitch, duration, velocity — **and the eighth is named nowhere in the eight
pages as read.** The count is given twice and the enumeration once, so the disagreement is inside
one sentence and its successor. **This read does not supply the missing member**: naming it would
mean importing a fact about the OctupleMIDI scheme from outside the paper, which this extract does
not do. It is recorded at §7.1 as an internal inconsistency and at §7.2 as something the paper
leaves without a value.

**Why the encoding is said to help:** *"OctupleMIDI reduces the sequence length when compared with
other encoding schemes like Midi-like [24,25], REMI [26], or Compound Word [27]. This reduction
occurs because in OctupleMIDI, tokens and notes are in one-to-one correspondence, whereas the other
schemes use tokens for other items such as time-signatures or barlines. For our use case, the fact
that all tokens correspond to notes has the added virtue that we do not waste computations
classifying non-note tokens."*

**A field of the encoding carries no information in this corpus**, at footnote 5: *"Midi velocity is
encoded in the OctupleMIDI format but is absent from the symbolic scores of our dataset. Therefore,
we use a default value of 96 for all note velocities in our dataset."* **So one of the encoding's
per-note features is a constant throughout this work.**

**The architecture, as stated:** *"we use the MusicBERT "base" architecture, whose hyperparameters
are modeled on those of the BERT base architecture ([13]), with a hidden dimension of **768**, **12
layers**, and **12 attention heads**. We use the pretrained checkpoint provided by [11]."*

**★ A PREMISE THE PAPER STATES AND ARGUES FOR RATHER THAN MEASURES — THE PRETRAINING/TASK DOMAIN
MISMATCH.** *"MusicBERT is not trained solely or even mainly on Classical music, whereas our
annotated data consists entirely of Classical music. This does not seem likely to be a problem,
because in the first place, a great deal of the tonal idiom (i.e., keys, chords) is shared between
different styles of tonal music, and tonal music surely predominates in MusicBERT's training set.
Moreover, to pretrain on only classical music would mean greatly reducing the amount of training
data, as it's extremely unlikely that 1,000,000 distinct midi files of Classical music exist. ([20]
is based on what is to our knowledge the largest corpus of Classical midi files in existence and
features under 15,000 files.)"*

**Note what the second half of that argument does and does not do.** It establishes that a
Classical-only pretraining corpus of the same scale is not available; **it does not bear on whether
the mismatch costs anything**, which is what the first half asserts. **No ablation against a
Classical-only or domain-matched pretraining is reported in the eight pages as read.**

### §2.8 Token classification and the heads (its §3.5.2, PDF page 4)

- **The approach:** *"To perform Roman numeral analysis, we adopt a token classification approach,
  predicting the key and Roman numeral for each token in the input. Since each token corresponds to
  a note, this amounts to predicting the chord during which each note occurs."*
- **Training loss is per note; evaluation aggregates over the slice:** *"While training, we
  calculate the loss on a per-token basis. In evaluation, in order to obtain a single prediction for
  each salami slice, we average the logits of simultaneous notes."*
  **★ The aggregation is over LOGITS and not over labels or probabilities**, and the paper states it
  that way twice — here and at §3.7.
- **The heads:** *"The token-classification heads are two-layer multilayer perceptrons (MLPs) whose
  inner dimension is the embedding dimension of the model (768, in our experiments)."*
- **The multi-task loss, and a rejected alternative with its measured direction:** *"To obtain the
  overall loss, we simply take the mean of the cross-entropy loss for each individual task. We tried
  learning a weighting of the contribution of each task to the global loss, following the approach
  introduced by [28] and implemented in an MIR context by [29], but observed a small degradation in
  model quality when doing so."* **"A small degradation" carries no figure.**

### §2.9 The fine-tuning procedure (its §3.5.3, PDF page 4)

- **Freezing, and why:** *"In our fine-tuning experiments, we found it important to freeze parts of
  the model to reduce the number of trainable parameters and avoid overfitting. **Freezing the first
  9 layers of MusicBERT** seemed to give the best results."* *(Against the 12 layers of §2.7, that
  leaves three unfrozen.)*
- **The optimizer schedule:** *"We used a learning rate of **2.5 × 10⁻⁴** with a linear warmup of
  **2500 steps** followed by a linear decay of the learning rate to 0."*
- **The step budgets:** *"When training on multi-task Roman numeral classification, we fine-tuned
  for **50,000 steps**. When training on key classification only (see Section 3.6), we fine-tuned
  for **25,000 steps**."*
- **A robustness claim, stated without a figure:** *"When experimenting with varying these
  hyperparameters, we did not typically find their precise values to have much effect on the
  performance of the model. This implies that the fine-tuning is fairly robust to different
  hyperparameter choices."* **No sweep, range or spread is reported.**
- **Parameter counts** are Table 3, transcribed at §5.3.

### §2.10 Key conditioning (its §3.6, PDF pages 4–5)

**★ THIS IS THE PAPER'S ANSWER TO ITS OWN DECOHERENCE PROBLEM, AND ITS MOTIVATION IS AN OBSERVATION
ABOUT WHERE ENTROPY CONCENTRATES.** *"In preliminary versions of RNBert, we found that high entropy
of the output probabilities for the degree task seemed to mainly occur in two distinct scenarios.
The first scenario involved unusual or hard-to-analyze chords, where high entropy is to be expected.
The second scenario involved chords that, given a key, were straightforward to analyze, but where
the model appeared to be uncertain about the choice of key."*

**The observation is reported with no measurement**: *"seemed to mainly occur"* carries no
proportion, no threshold and no count, and no entropy figure appears anywhere in the eight pages as
read.

**The worked illustration, quoted because it is the mechanism in miniature:** *"suppose we are
analyzing a passage, and we recognize an A minor chord, but we are uncertain whether the key is C
major or G major. In that case, though we will not know whether to label it with "vi" or "ii", this
uncertainty isn't about the chord itself, but only about the key. If the model distributes the
probability mass roughly evenly between the two possibilities, it may emit an incoherent composite
prediction like "ii of C major" (a D minor chord) or "vi of G major" (an E minor chord). In general,
the degree task depends on the key task in this way."*

*(The example closes at every step: A minor is vi in C major and ii in G major; ii of C major is D
minor and vi of G major is E minor — **neither of which is the A minor chord the passage contains**,
which is exactly the incoherence the paper is illustrating. **Checked at the paper's own words.**)*

**Footnote 6 records a theoretical position and declines to develop it:** *"We do not have space to
discuss this further, but there are music theoretic reasons to think that a certain degree of
uncertainty about key annotations is inevitable because the key of certain passages, especially
transitional ones, can be analyzed in more than one way."*

**The mechanism:** *"we embed the key tokens with a two-layer MLP with hidden and output dimensions
of **256** and GELU activation. We then concatenate this key embedding with the output from
MusicBERT to obtain the input to the Roman numeral classification heads."*

**Footnote 7 records a design choice, an unexplained empirical result and a conjecture about it:**
*"In principle, we should be able to replace this MLP with a simple embedding layer and obtain the
same results. In practice, however, we found that using a simple embedding layer barely improved
performance above the unconditioned baseline, even with teacher forcing. **We suspect that this
occurs because the loss landscape of the MLP has better training dynamics.** After training, on the
other hand, it should be possible to replace the MLP with an embedding table that simply encodes the
output of the MLP for each key. However, the MLP contributes such a small proportion of the model's
overall parameter count that we did not bother to do so."*

**★ THE TRAIN/EVALUATE ASYMMETRY, WHICH IS WHAT MAKES TABLE 4's LINES 5 AND 6 DIFFERENT THINGS.**
*"In training, we employ teacher forcing, that is, we condition on the ground-truth key annotations
from the labeled data. In evaluation, we first predict the key with a separately fine-tuned model,
then condition the chord predictions on these predicted keys."* **So the deployed configuration
conditions on a PREDICTED key (line 5), and line 6 conditions on the GROUND-TRUTH key and is a
sanity check rather than a deployable result** — which §4.1 says in its own words.

**A neighbouring approach is named, tried and rejected, with the direction stated and no figure:**
*"Another attempt to encourage coherence between key and Roman numeral predictions is [21], who use
a neural autoregressive distribution estimator (NADE). Their approach extends beyond ours insofar as
it conditions each sub-task of the Roman numeral classification on the previous tasks. In preliminary
experiments applying a similar approach to RNBert, **we observed a small decline in performance
across all metrics.** We defer to future work a qualitative evaluation of these predictions and
further similar experiments."*

### §2.11 The post-processing steps (its §3.7, PDF page 5)

- **Segment collation:** *"we collate the predictions from each segment, combining the overlapping
  logits of adjacent segments by linearly interpolating between them. (By analogy to audio signal
  processing we could say that we cross-fade between the logits of neighboring segments.)"*
  **This is the counterpart of the 1000-token crop with hop 250 at §2.3: the hop is what creates the
  overlap this step interpolates across.**
- **Slice aggregation:** *"We then average the logits of simultaneous notes to obtain a single set
  of logits for each salami-slice."*
- **★ KEY DECODING IS A SEPARATE DYNAMIC-PROGRAMMING STEP WITH A HAND-SET TRANSITION MATRIX.** *"To
  avoid implausibly brief key changes of one or two salami-slices' duration (which otherwise
  sometimes occur at transitions between keys, when the model estimates both keys to be
  approximately equiprobable), we use a dynamic programming approach to decode the key predictions.
  Specifically, we employ the Viterbi algorithm, using RNBert's output probabilities as the emission
  probabilities and **defining a transition probability matrix that is uniform, except for
  self-transitions, whose probabilities are upweighted.**"*
  **The upweighting factor is not stated anywhere in the eight pages as read**, so the one free
  parameter of this step carries no value in the paper.
- **Its stated effect is a claim without a figure:** *"This decoding scheme has a **negligible
  effect on the measured accuracy of the predictions**, while effectively eliminating implausibly
  brief key changes."* **The accuracy effect was measured — the sentence says *measured* — and the
  measurement is not printed.**

### §2.12 The evaluation measure and the composite labels (its §4, PDF page 5)

**The measure, inherited:** *"Table 4 provides our results, expressed following [6] as **the
proportion of time that the predicted labels are accurate, with 32nd-note resolution**."*

**★ TWO GRIDS ARE IN PLAY AND THE PAPER DOES NOT RECONCILE THEM.** The score is quantized at the
**64th-note** level (§2.3) and the salami-slices sit on that grid; the evaluation counts time at
**32nd-note** resolution. **What happens to a slice shorter than a 32nd note, or to a label change
falling on an odd 64th, is not stated anywhere in the eight pages as read.**

**The two composite labels, defined by the paper:** *"RN₋root refers to the conjunction of degree,
quality, inversion, and key, while RN₊root adds to these the chord root."*

**★ THE PAPER ESTABLISHES ITS OWN GROUND FOR TREATING THE ROOT AS CARRYING NO INDEPENDENT
INFORMATION, AND §6.1 USES IT.** *"Predicting the root is redundant: **the root of a Roman numeral
is a deterministic function of the degree and key** (e.g., the root of #iv in C major is F-sharp).
There is hence no need to include it in the composite Roman numeral, or indeed, to predict it at
all."*

**Why both are nonetheless reported on the subset:** *"Therefore, when training RNBert on our full
dataset, we do not predict the root and report only RN₋root. When training on the AugmentedNet v1
data subset, in contrast, in order to ensure a fair comparison with the prior models, both of which
predict the root, we train RNBert to predict the root and report the results for both RN₊root and
RN₋root. It can be seen that the inclusion or exclusion of the root makes almost no difference, as
one would expect."*

**A third composite the paper reports but did not train:** *"Finally RN_alt refers to an alternate
task learned in [6, 10], replacing the quality, degree, and root predictions with a vocabulary of
**the 75 most common Roman numerals** in the AugmentedNet v1 training set. **We did not train RNBert
on this task**, but we report the prior results on it to facilitate comparison with our results."*

---

## §3 — Coupling facts

*The three coupling questions the extract form makes mandatory: what the work assumes about what
comes before it, what it hands to what comes after it, and the scope it claims for itself. **Every
item here is read at the paper and nothing is inferred from any other source.***

### §3.1 What it ASSUMES about its upstream

- **A symbolic score already exists and is already correct.** No audio, no transcription, no
  score-following step. The formats named are MusicXML, MuseScore and Humdrum.
- **A human Roman-numeral and key annotation already exists for every training and evaluation
  score.** The whole method is supervised; the paper's opening premise is that this material is
  scarce.
- **The annotation can be attached to individual NOTES.** The conversion to the tabular form labels
  *"each note with the associated key and chord annotation"*. **A chord annotation that could not be
  distributed over notes has no place in this representation.**
- **Rhythm can be quantized to a 64th-note grid without loss that matters here.** Assumed, not
  argued: the step is taken *"following MusicBERT"*.
- **Segmentation is GIVEN, not inferred.** After salami-slicing, the unit of analysis is a stretch
  during which the sounding set does not change, and the model predicts a label for each such
  stretch. **The model is never asked to LOCATE a chord boundary as such**: it labels a given slice,
  and a chord boundary appears wherever two consecutive slices receive different labels. This is the
  paper's most consequential upstream assumption and it is not framed as one.
  *(★ NARROWED AT THE SWEEP. **FORMER WORDING, PRESERVED (#12):** "**The model is never asked where
  one chord ends and the next begins.**" — **too strong: the labelling does determine the boundaries,
  it merely never searches for them**, and the distinction is the whole point of the observation.)*
- **Pitch spelling is not available and is assumed not to be needed** (§2.5).
- **Dynamics carry nothing**: velocity is absent from the sources and is set to a constant 96.
- **An EXACT doubling carries nothing**: notes sharing pitch, onset and release are removed before
  the model sees them, so a doubling of that exact shape is invisible to it. **A pitch doubled at a
  different onset or with a different release survives dedoubling**, so this is not a claim that the
  model cannot see doubling at all.
  *(★ NARROWED AT THE SWEEP. **FORMER WORDING, PRESERVED (#12):** "**Doubling carries nothing**:
  notes identical in pitch, onset and release are removed before the model sees them, so the model
  cannot know how many voices sound a pitch." — **the second clause over-reaches the first**, which
  names three conditions that must all hold.)*
- **A pretrained MusicBERT checkpoint exists and is usable**, and its pretraining corpus is assumed
  to be tonally representative enough for Classical material (§2.7).

### §3.2 What it HANDS downstream

- **Per-salami-slice labels on four axes** — key, degree, quality, inversion — optionally a fifth,
  the root, which the paper itself calls redundant.
- **An unspelled key**: a pitch class plus a mode, not a notated key name.
- **A key sequence that has been Viterbi-decoded** with a hand-set self-transition upweighting, so
  the published key path is not the per-slice argmax of the model's own probabilities. *(The word
  the paper uses is "decode"; it does not describe the selection rule at the other three axes,
  which are not decoded this way.)*
- **NOTHING ABOUT UNCERTAINTY IS PUBLISHED.** The model produces probabilities — the paper reasons
  about their entropy at §3.6 and uses them as Viterbi emissions at §3.7 — **but no confidence,
  margin, entropy or ranked alternative is reported, tabulated or offered as an output** anywhere
  in the eight pages as read. What is handed on is a single committed label per axis per slice.
- **No segmentation, no cadence, no phrase, no voice-leading and no non-chord-tone labelling.** The
  conclusion names non-chord-tone analysis and melody harmonization as things the approach *could*
  be extended to, which is a statement that they are not delivered here.
- **No spelled output of any kind**, and therefore no notated Roman numeral in the usual
  orthography without a further step the paper describes but does not build (§2.5).

### §3.3 Its own STATED scope and limits

- **The annotated data is entirely Classical**, and the paper says so in terms while arguing the
  pretraining mismatch does not matter.
- **The evaluation unit is time, at 32nd-note resolution**, inherited from [6].
- **Comparison with [7] is declared not directly possible** (footnote 2).
- **RN_alt was not trained**, and the figures reported for it are other papers' (§2.12).
- **★ THE CEILING THE PAPER PUTS ON ITS OWN MEASURE**, from §4.2: *"These considerations may place a
  ceiling on the accuracy of all Roman numeral analysis models."* The considerations are that a
  passage often admits more than one correct analysis — modulation against tonicization being its
  worked case — so that a valid alternate reading counts as an error. **The ceiling is asserted, not
  measured, and no value is proposed for it.**
- **What the paper claims is delivered**, from §5: *"our results imply that, by fine-tuning
  pretrained models, we can obtain state-of-the-art performance on music theory tasks"*, and *"we
  suggest that Roman numeral analysis models have now matured to the point where they are ready to
  be used in large-scale musicological studies."* **The second is a readiness claim attached to no
  threshold and to no figure**, and it stands in the same paper as the ceiling clause above and as
  a best composite figure of .624.

---

## §4 — Claims, labeled

*Every load-bearing claim in the paper, labeled **FACT** (stated or measured in this paper, with the
place it is printed), **THEORY** (established published theory the paper invokes), or **CONJECTURE**
(offered by the paper without a measurement or a citation that settles it). **The label is about
what THE PAPER establishes, not about whether the claim is true.***

| # | Claim | Label | Where, and on what |
|---|---|---|---|
| 1 | Fine-tuning a pretrained masked language model on Roman numeral analysis outperforms models trained from scratch **on degree, quality and both composite Roman numerals — and does NOT lead on inversion or key** | **FACT** | Table 4 lines 1–3, on the AugmentedNet v1 splits. Line 3's inversion .796 is below line 2's .803 and its key .825 below line 1's .829. **The paper is itself careful here** — its own sentence claims only *"substantially outperforms the prior models on degree and quality"*. The comparison is like-for-like by construction; the prior figures are quoted from [6, 10] and not re-measured (§2.1). *(★ NARROWED AT THE SWEEP. **FORMER WORDING, PRESERVED (#12):** "…outperforms models trained from scratch, on the shared subset and splits" — **an unqualified win over a block in which it loses two of six columns**.)* |
| 2 | RNBert exceeds the earlier models by an even larger margin when trained on the complete dataset | **CONJECTURE** | §4, against Table 4 lines 4–6 vs 1–2. **The dataset changes between the two halves and the test split for lines 4–6 is not stated in the eight pages as read** (§6.8) |
| 3 | The larger margin on the composite RN than on the components implies more coherence among RNBert's predictions | **FACT as arithmetic, CONJECTURE as explanation** | The margin is in Table 4 and closes (§6.1); *"Such coherence may be due to the robustness of the representations MusicBERT learns in its pretraining"* is the paper's own hedged wording |
| 4 | More internally consistent predictions are "more likely to be useful" to a human even when they disagree with the annotator | **CONJECTURE** | §4. No user study, no downstream task, no measurement of usefulness anywhere in the paper |
| 5 | Salami-slicing does not affect harmonic analysis | **THEORY**, argued from pitch content | §2.3. The argument is that pitch content is unchanged and that suspensions and pedal tones are analysed the same whether tied or restruck. **Not measured here** |
| 6 | Dedoubling produces a more homogeneous texture between small- and large-ensemble music, aiding generalization to symphonies and operas | **CONJECTURE** | §2.3. The generalization target is named as a wish; **no large-ensemble evaluation exists in this paper**, the corpus being the labeled small-ensemble material |
| 7 | Spelled keys can be recovered from unspelled ones by a rule-based algorithm, likely with perfect accuracy | **CONJECTURE** | §2.5. A method is sketched, citing the line of fifths [23]; **no implementation and no measurement** |
| 8 | Enharmonically ambiguous keys are rare enough that misclassifying them does not significantly affect the reported figures | **CONJECTURE** | §2.5. **No count of such keys in the corpus is given**, though the corpus is in hand and the count is computable |
| 9 | The pretraining/task domain mismatch does not matter, because tonal idiom is shared across styles and tonal music predominates in MusicBERT's training set | **CONJECTURE** | §2.7. **No ablation against a domain-matched pretraining is reported** |
| 10 | A Classical-only pretraining corpus of comparable scale does not exist | **FACT**, bounded by its own hedge | §2.7, citing [20] as *"to our knowledge the largest corpus of Classical midi files in existence"* with *"under 15,000 files"* |
| 11 | Predicting the key, quality, inversion and degree separately costs coherence among them | **FACT** | §3.3 states the mechanism; **§6.1's arithmetic measures how much coherence survives** and the answer is: much more than independence would give |
| 12 | The root is a deterministic function of the degree and the key, so predicting it adds nothing | **THEORY**, and confirmed numerically here | §2.12 states it; Table 4 line 3's RN₊root .574 against RN₋root .575 is the paper's own confirmation (§6.3) |
| 13 | High degree-entropy arises mainly in two scenarios, the second being key uncertainty | **CONJECTURE** | §3.6, *"seemed to mainly occur"*. **No entropy value, threshold, count or proportion appears in the paper** |
| 14 | Conditioning the Roman numeral prediction on the key improves the coherence of the composite | **FACT**, on a small margin | Table 4 lines 4 and 5: RN₋root .620 → .624 with degree falling .762 → .749. **The paper does not say whether +.004 exceeds any uncertainty**, and no uncertainty is reported anywhere in Table 4 (§7.2) |
| 15 | Conditioning on the ground-truth key raises degree accuracy sharply and leaves quality and inversion almost untouched, as expected because those tasks do not depend on the key | **FACT** | Table 4 line 6 against lines 4–5: degree .859 vs .762/.749; quality .865 vs .867/.864; inversion .872 vs .872/.872 (§6.6) |
| 16 | Replacing the key-embedding MLP with a simple embedding layer barely improves on the unconditioned baseline, because the MLP's loss landscape has better training dynamics | **FACT** as the observation, **CONJECTURE** as the explanation | Footnote 7. The paper's own word is *"We suspect"*; no figure is given for *"barely improved"* |
| 17 | A NADE-style approach conditioning each sub-task on the previous ones gives a small decline across all metrics | **FACT**, unquantified | §3.6. **The word is *"all metrics"* and no figure is printed**, so the claim cannot be checked against anything in the paper |
| 18 | Learning a weighting of the per-task losses degrades model quality slightly | **FACT**, unquantified | §3.5.2. No figure |
| 19 | Synthetic training data did not improve performance here, possibly because this model's inputs are raw notes rather than pitch vectors | **FACT** as the negative result, **CONJECTURE** as the explanation | §2.6, the paper's own *"It is possible that"*. No figure for the negative result |
| 20 | The Viterbi key decoding has a negligible effect on measured accuracy while removing implausibly brief key changes | **FACT**, and the figure is withheld | §2.11. The sentence says the accuracy effect was *measured*; **the measurement is not printed and the transition-matrix upweighting is not stated** |
| 21 | Fine-tuning is fairly robust to hyperparameter choice | **CONJECTURE** | §2.9. *"we did not typically find their precise values to have much effect"*; no sweep or spread reported |
| 22 | A high proportion of RNBert's "inaccurate" predictions are acceptable alternate analyses | **CONJECTURE** | §4.2, offered *"On a priori grounds, as well as based on qualitative sampling"*. **The sampling is not reported: no count, no protocol, no proportion** |
| 23 | Multiple acceptable analyses may place a ceiling on the accuracy of all Roman numeral analysis models | **CONJECTURE** | §4.2. No value proposed, no measurement attempted |
| 24 | Key prediction is easier on the AugmentedNet v1 subset because it holds less late-19th-century music, which modulates more widely | **CONJECTURE** | §4. The direction in Table 4 is real and closes (§6.5); **the stated cause is not measured** — no repertoire breakdown, no modulation-rate figure in the eight pages as read |
| 25 | This is the largest corpus yet assembled for Roman numeral analysis | **FACT**, hedged by the paper itself | §3.1, *"To our knowledge"*. Table 1's counts are given; no comparison table against other corpora is printed |
| 26 | Roman numeral analysis models are now ready for large-scale musicological studies | **CONJECTURE** | §5. **Attached to no threshold and to no figure**, and standing in the same paper as claim 23 and a best composite of .624 |
| 27 | The approach extends readily to other note-level music theory tasks (non-chord-tone analysis, melody harmonization) | **CONJECTURE** | Abstract and §5. Nothing of the kind is built or measured here |

---

## §5 — Measured results and printed values, transcribed as the paper prints them

*Transcribed from the page images. **Every table is given whole, cell for cell, including blank
cells, and the paper's own decimal forms are kept exactly** — the paper prints some values with two
decimals and some with three, and that is reproduced rather than normalised.*

### §5.1 Table 1, transcribed whole (PDF page 2)

| Data subset | Scores | Notes | Chords |
|---|---|---|---|
| All | 1,404 | 1,289,888 | 161,473 |
| AugmentedNet v1 | 347 | 701,703 | 77,570 |

**Caption, verbatim:** *"Table 1. Overall contents of the datasets used for training and
evaluation."*

**Printed in prose beside it:** the duplicate TAVERN scores in AugmentedNet v1 *"comprise 106,981
notes"*; and *"7 scores from AugmentedNet v1 were excluded because of preprocessing errors"*
(footnote 3).

**★ NO UNCERTAINTY, NO SPLIT SIZES.** Table 1 gives totals only. **The sizes of the
training/validation/testing splits are not printed anywhere in the eight pages as read**, for
either dataset.

### §5.2 Figure 1 and Table 2, transcribed whole (PDF page 2)

**Figure 1** is a hypothetical two-bar example on one staff, shown twice: *Raw* and *Salami-sliced*.
The analysis printed beneath both versions is **G:I6** then **V**.

**Caption, verbatim:** *"Figure 1. A hypothetical musical example and its analysis, before and after
salami-slicing."*

**Table 2, transcribed whole** — the columns are the note-rows of the tabular format, one column per
note:

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| **Onset** | 0 | 0 | 0 | 2 | 2 | 2 | 3 | 3 | 3 |
| **Release** | 2 | 2 | 2 | 3 | 3 | 3 | 4 | 4 | 4 |
| **Pitch** | 59 | 67 | 79 | 62 | 69 | 79 | 62 | 69 | 78 |
| **RN** | I6 | I6 | I6 | V | V | V | V | V | V |
| **Key** | G | G | G | G | G | G | G | G | G |

**Caption, verbatim:** *"Table 2. The example from Figure 1 in tabular format after salami-slicing.
Time signatures, tempi, and bar lines are omitted."*

**What the table shows when read against the figure, derived here and not stated by the paper:**
three salami-slices of three notes each, at onsets 0, 2 and 3. **The chord labelled V spans two
slices**, because the soprano moves from 79 to 78 within it — which is the suspension the paper
names in its prose (*"like the soprano G in Figure 1"*). The alto 69 and bass 62 persist unchanged
across those two slices, and the split is entirely the doing of the soprano's release. **This is
exactly the mechanism the prose describes, and the table confirms it at the cell.**

### §5.3 Table 3, transcribed whole (PDF page 4)

| Model | Total | Trainable |
|---|---|---|
| Base | 108,805,598 | 26,782,729 |
| Key conditioned | 111,023,816 | 28,859,891 |

**Caption, verbatim:** *"Table 3. RNBert parameter counts."*

### §5.4 Table 4, transcribed whole (PDF page 6) — this is the paper's results table

*The table has a spanning header "Accuracy" over the first four numeric columns. The two data
blocks are labelled in italic within the table body. **Blank cells are blank in the paper and are
shown as "—" here, with that convention stated so no reader takes a dash for a printed value.***

| Line | Model | Degree | Quality | Inversion | Key | RN₊root | RN₋root | RN_alt |
|---|---|---|---|---|---|---|---|---|
| | ***AugmentedNet v1 data subset*** | | | | | | | |
| 1 | AugmentedNet [6] | .67 | .797 | .788 | **.829** | .464 | — | .515 |
| 2 | ChordGNN+(Post) [10] | .714 | .784 | **.803** | .813 | .518 | — | .529 |
| 3 | RNBert (key conditioned) | **.731** | **.819** | .796 | .825 | **.574** | **.575** | — |
| | ***All data*** | | | | | | | |
| 4 | RNBert (unconditioned) | .762 | .867 | .872 | .822 | — | .620 | — |
| 5 | RNBert (key conditioned) | .749 | .864 | .872 | .823 | — | .624 | — |
| 6 | RNBert (key conditioned, teacher forcing) | .859 | .865 | .872 | N/A | — | N/A | — |

**Caption, verbatim:** *"Table 4. Accuracy of RNBert and two prior models. The meanings of RN₊root,
RN₋root, and RN_alt are described in Section 4. In the model comparison of lines 1–3, we indicate
the best metric in bold type. Because the teacher-forcing model on line 6 does not predict key, and
RN prediction involves key prediction, we do not report RN results for this model."*

**Two cells read "N/A" rather than being blank** — line 6's Key and its composite — and the caption
gives the reason.

**★ A FIDELITY POINT ABOUT HOW LINES 4–6 ARE TYPESET, RECORDED BECAUSE THE TABLE ALONE DOES NOT
ASSIGN THEIR COMPOSITE TO A COLUMN.** On lines 1–3 the two composite values sit in their own
columns — line 3 prints .574 under RN₊root and .575 under RN₋root, plainly two cells. **On lines
4, 5 and 6 a SINGLE value is printed, centred across the RN₊root/RN₋root region rather than under
either heading.** It is the paper's PROSE that assigns it — *"when training RNBert on our full
dataset, we do not predict the root and report only RN₋root"* — and the transcription above follows
the prose. **A reader taking the table without the prose could not tell which of the two columns
those three values belong to.**

*(★ CORRECTED AT THE READ-BACK. **FORMER WORDING, PRESERVED (#12):** "**Every other empty cell is
blank.**" — **an absolute about the table's cells that its own typesetting refutes**, lines 4–6
carrying a centred value across two column positions rather than a filled cell and an empty one.)*

**★ ONE CELL IS PRINTED TO A DIFFERENT PRECISION FROM EVERY OTHER — ADOPTED FROM THE FIRST EXTRACT
AT THE CROSS-CHECK AND CHECKED HERE AT THIS FILE'S OWN TRANSCRIPTION.** **AugmentedNet's Degree cell
reads .67, to two decimals**; every other numeric cell in the table carries three. **This read had
not noticed it.** Checked across all twenty-nine numeric cells of the transcription above: .67 is
the only one. *(Adopted, not copied — the claim was tested at the table rather than accepted from
the other file, which is the standing rule for an adoption.)*

**★ THE ONE VALUE OF THIS TABLE THAT IS NOT PRINTED ANYWHERE IN IT: AN UNCERTAINTY.** Table 4
carries no standard deviation, no confidence interval, no seed count and no repetition count.
**Nothing in the eight pages as read says whether any figure in it is a single run.** See §7.2.
**Both reads reached this independently and both name it as a bound** (§9.2).

### §5.5 Figure 2, transcribed whole (PDF page 6)

**Caption, verbatim:** *"Figure 2. Beethoven, String Quartet in F major, op. 18, no. 1, iv, mm. 7–8.
Arguably incorrect predictions that do not agree with the human annotations are printed in italic
type and serve to illustrate the discussion in Section 4.2. The prediction printed in strikethrough
type is straightforwardly incorrect and illustrates the discussion in Section 4.1."*

**The three label rows beneath the music, transcribed position by position:**

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| **Ground truth** | F:V | V⁶₅ | C:IV | V⁶₅/V | I⁶₄ | V⁷ | I |
| **RNBert (unconditional)** | F:V⁶ | V⁶₅ | I | V⁶₅/ii | I⁶₄ *(struck through)* | V⁷/V | V |
| **RNBert (conditioned)** | F:V⁶ | V⁶₅ | I | V⁶₅/ii | I⁶₄/V | V⁷/V | V |

**The key changes printed in the rows:** the ground-truth row changes key once, at position 3, from
F to C. **Neither RNBert row prints a key change at all** — both carry F: at position 1 and nothing
thereafter — which is the tonicization reading §4.2 describes.

### §5.6 The values printed in prose and in no table

- **MusicBERT pretraining corpus:** *"over 1 million midi files, 3 orders of magnitude larger than
  our Roman numeral dataset"*; MidiBERT-Piano by comparison *"pretrains on fewer than 5,000 scores
  of exclusively piano music"*; the largest Classical midi corpus known to the paper *"features
  under 15,000 files"*.
- **Architecture:** hidden dimension **768**, **12** layers, **12** attention heads. Head MLPs are
  two-layer with inner dimension **768**. The key-embedding MLP is two-layer with hidden and output
  dimensions **256**, GELU activation.
- **Preprocessing and training constants:** quantization at the **64th note**; sequence length
  **1000** tokens, hop **250**; transposition to all **12** keys; duration scaling by a factor of
  **2**; velocity constant **96**; first **9** layers frozen; learning rate **2.5 × 10⁻⁴**; warmup
  **2500** steps; **50,000** fine-tuning steps for multi-task, **25,000** for key-only.
- **The evaluation grid:** **32nd-note** resolution.
- **The RN_alt vocabulary:** the **75** most common Roman numerals in the AugmentedNet v1 training
  set.
- **The duplicate TAVERN material:** **106,981** notes. **Seven** scores excluded for preprocessing
  errors.
- **★ WHAT IS NOT PRINTED, and each of these is a value the paper's own prose leans on:** the
  Viterbi self-transition upweighting; the entropy figures behind §3.6's two scenarios; the size of
  the *"small degradation"* from learned task weighting; the size of the *"small decline"* from the
  NADE-style approach; the size of the *"negligible effect"* of the Viterbi decoding; the proportion
  behind *"a high proportion"* of acceptable alternate analyses; and the split sizes of either
  dataset.

---

## §6 — Arithmetic this read performed on the paper's own printed values

*Every input is a cell of §5. **Nothing here is imported from any other source**, and where a
derivation needs a fact about the paper's own definitions it cites the paper's own sentence.*

### §6.1 ★ THE COMPOSITE ROMAN NUMERAL IS FAR MORE ACCURATE THAN INDEPENDENT COMPONENTS WOULD GIVE, IN EVERY ROW THAT PRINTS BOTH — AND THE EXCESS RISES EXACTLY WHERE THE PAPER SAYS COHERENCE DOES

**The method is declared and is not this read's own idea** — see §0. **The arithmetic is this
read's own on this paper's cells.**

**What is being asked.** RN₋root is defined by the paper as *"the conjunction of degree, quality,
inversion, and key"*. If a model's errors on those four axes fell independently, the probability of
all four being right at once would be the product of the four accuracies. **So the product is what
independence predicts, and the printed composite is what actually happens.**

| Line | Model | Degree × Quality × Inversion × Key | Product | Composite printed | Excess over the product |
|---|---|---|---|---|---|
| 1 | AugmentedNet | .67 × .797 × .788 × .829 | **.3488** | .464 (RN₊root) | **+.1152 → 11.5 points** |
| 2 | ChordGNN+(Post) | .714 × .784 × .803 × .813 | **.3654** | .518 (RN₊root) | **+.1526 → 15.3 points** |
| 3 | RNBert (key cond.) | .731 × .819 × .796 × .825 | **.3932** | .574 (RN₊root) | **+.1808 → 18.1 points** |
| 3 | RNBert (key cond.) | *same product* | **.3932** | .575 (RN₋root) | **+.1818 → 18.2 points** |
| 4 | RNBert (uncond.) | .762 × .867 × .872 × .822 | **.4735** | .620 (RN₋root) | **+.1465 → 14.6 points** |
| 5 | RNBert (key cond.) | .749 × .864 × .872 × .823 | **.4644** | .624 (RN₋root) | **+.1596 → 16.0 points** |

*(Line 6 is excluded: its key and composite cells read N/A.)*

**★ THE COMPARISON IS EXACT AT THREE ROWS AND IS A LOWER BOUND AT THE OTHERS, AND THE DIRECTION OF
THE BOUND IS STATED BECAUSE IT MATTERS.** Where the composite is **RN₋root** — line 3's second row,
and lines 4 and 5 — the product is over exactly the four conjuncts the paper's own definition names,
and the comparison is apples for apples. Where the composite is **RN₊root** — lines 1, 2 and line
3's first row — the composite requires a FIFTH prediction to be right as well, and Table 4 prints no
root accuracy for any model, so the product here is over four of five conjuncts. **A four-way
product is greater than or equal to the five-way one, so the excesses reported for those rows are
LOWER BOUNDS on the true excess over independence.** They are computed identically across the three
rows and are therefore comparable with one another.

**What it means, stated at the width the arithmetic supports.** Errors on the four axes **co-occur
strongly rather than compounding**: a slice the model gets wrong tends to be wrong on several axes
at once, and a slice it gets right tends to be right on all. **At line 3, independence would put
RN₋root at .393 where the paper prints .575.** *(★ NARROWED AT THE SWEEP. **FORMER WORDING,
PRESERVED (#12):** "Independence would put **the best composite** at .393 where the paper prints
.575." — **.575 is the best composite of the like-for-like block only**; line 5's .624 is higher and
sits against a different product, .464, so the superlative was wrong read across the whole table.)*
Nothing here says how much of that co-occurrence is
the model's doing and how much is a property of the task — a passage that is hard is plausibly hard
on every axis at once — and this read takes no position on that.

**★ AND THE QUANTITY THE PAPER ASSERTS BUT NEVER MEASURES IS EXACTLY THIS ONE.** The paper writes,
of the like-for-like block: *"it outperforms the earlier models by a much more substantial margin
when predicting the composite Roman numeral RN₊root. **This implies that there is more coherence
among the various dimensions of its predictions.**"* It offers no number for that coherence.
**The excess above is a number for it, computed the same way in all three rows of that block, and it
rises monotonically in exactly the order the paper claims:**

> **AugmentedNet 11.5 → ChordGNN+(Post) 15.3 → RNBert 18.1 points.**

**This CONFIRMS the paper's own claim and strengthens it from the paper's own cells.** *(What it
does not do: establish the paper's explanation for the coherence — *"may be due to the robustness of
the representations MusicBERT learns in its pretraining"* — which remains the CONJECTURE §4 labels
it.)*

### §6.1a ★ A SECOND, MORE LITERAL TEST OF THE SAME COHERENCE CLAIM — ADOPTED FROM THE FIRST EXTRACT AT THE CROSS-CHECK AND RE-DERIVED HERE AT THIS FILE'S OWN TABLE

**The first extract tests the paper's *"much more substantial margin"* sentence differently, and its
test is the more literal one.** The paper's claim is about MARGINS over the prior models, so the
test is whether the composite's margin exceeds every single component's margin. **Re-derived here
from §5.4's cells rather than copied:**

| Comparison | Degree | Quality | Inversion | Key | **Composite (RN₊root)** |
|---|---|---|---|---|---|
| **Line 3 − line 2** (RNBert − ChordGNN+(Post)) | +.017 | +.035 | **−.007** | +.012 | **+.056** |
| **Line 3 − line 1** (RNBert − AugmentedNet) | +.061 | +.022 | +.008 | **−.004** | **+.110** |

**On both comparisons the composite margin exceeds every component margin** — .056 against a largest
component margin of .035, and .110 against .061 — **which is exactly what the paper's sentence
asserts and does not quantify.** **Two of the eight component margins are negative**, so RNBert is
behind on inversion against ChordGNN and behind on key against AugmentedNet while leading on the
composite by a wide margin, which sharpens the point rather than softening it.

**★ THE TWO TESTS ARE DIFFERENT AND BOTH CONFIRM THE CLAIM, WHICH IS WHY BOTH ARE KEPT.** §6.1 asks
whether the composite beats what INDEPENDENCE would give and finds it does, by a margin that rises
across the three models. This one asks whether the composite's LEAD over the rivals beats its
components' leads, and finds it does. **Neither subsumes the other**: the first is a statement about
one model's internal error structure, the second about the gap between models. *(The idea of this
one is the first extract's; the arithmetic is this read's own on this read's own transcription.)*

### §6.2 ★ A SECOND, SMALLER ARITHMETIC FINDING AT TABLE 3: THE KEY-CONDITIONED MODEL FREEZES 141,056 PARAMETERS THE BASE MODEL DOES NOT, AND NOTHING IN THE PAPER ACCOUNTS FOR IT

Table 3 prints totals and trainable counts. **The frozen count is their difference, and the paper
never prints it:**

| Model | Total | Trainable | **Frozen (derived)** |
|---|---|---|---|
| Base | 108,805,598 | 26,782,729 | **82,022,869** |
| Key conditioned | 111,023,816 | 28,859,891 | **82,163,925** |
| **Difference** | **+2,218,218** | **+2,077,162** | **+141,056** |

**The only freezing the paper describes in the eight pages as read is of MusicBERT's first 9
layers** (§2.9), and those layers
are the same layers of the same checkpoint in both rows. **On that description the frozen count
should be identical in the two rows, and Table 3's own numbers say it is not:** the key-conditioned
model carries **141,056** more frozen parameters. Equivalently, of the 2,218,218 parameters the
key-conditioning machinery adds, **141,056 are not trainable.**

**This read proposes no cause and names none.** The arithmetic is certain; what is absent is any
sentence in the eight pages as read that would account for it. Recorded at §7.1 and §7.2.

### §6.3 The root claim closes, and its direction is forced

The paper writes *"the inclusion or exclusion of the root makes almost no difference, as one would
expect."* Line 3 is the only row printing both: **RN₊root .574, RN₋root .575, a difference of
.001.** The claim closes.

**The direction is not a coincidence and is worth stating:** RN₊root demands everything RN₋root
demands and the root besides, so **RN₊root ≤ RN₋root necessarily**, and .574 ≤ .575 satisfies it. The
gap of one thousandth is the model's root prediction disagreeing with the value the degree and key
already determine — which the paper's own sentence says is a deterministic function — **on about a
tenth of a percent of the time on which the other four axes are right.**

### §6.4 The "greatly exceed" claim closes on three axes and rests on a single row on the fourth

The paper writes that *"the models on lines 4 and 5 greatly exceed the performance of the models on
lines 1–3 on degree, quality, inversion, and RN₋root prediction"*. Against the best of lines 1–3 in
each column:

| Axis | Best of lines 1–3 | Line 4 | margin | Line 5 | margin |
|---|---|---|---|---|---|
| Degree | .731 (line 3) | .762 | **+3.1** | .749 | **+1.8** |
| Quality | .819 (line 3) | .867 | **+4.8** | .864 | **+4.5** |
| Inversion | .803 (line 2) | .872 | **+6.9** | .872 | **+6.9** |
| RN₋root | .575 (**line 3 only**) | .620 | **+4.5** | .624 | **+4.9** |

**The claim holds in direction at every one of the eight comparisons.** Two precisions:

- **★ THE RN₋root LIMB NAMES THREE ROWS AND CAN ONLY BE CHECKED AGAINST ONE.** Lines 1 and 2 print
  **nothing** in the RN₋root column; only line 3 carries a value there. So *"the models on lines
  1–3"* over-names its own comparison set on that axis by two.
- **The weakest instance is +1.8 points** (line 5's degree against line 3's). *"Greatly exceed"* is
  a judgment and this read does not grade it; the eight margins are given above so a reader can.

### §6.5 The key-prediction observation closes exactly, exception included

The paper writes: *"when it comes to key prediction, the AugmentedNet v1-trained models actually
perform better (with the exception of the ChordGNN model)."*

AugmentedNet v1-trained: line 1 **.829**, line 2 **.813**, line 3 **.825**. Full-data: line 4
**.822**, line 5 **.823**.

- Line 1 (.829) beats both full-data models. ✓
- Line 3 (.825) beats both full-data models. ✓
- Line 2, ChordGNN (.813), beats neither — which is exactly the exception the sentence names. ✓

**The claim closes cell for cell, and the parenthetical exception is necessary and sufficient.**
*(The stated CAUSE — less late-19th-century music, which modulates more widely — is measured nowhere
in the eight pages as read and is labeled CONJECTURE at §4, claim 24. No repertoire breakdown of
either dataset is printed there. **§6.7 records a SECOND difference between the two datasets that
the paper does not mention**, so the stated cause is not the only candidate available from the
paper's own tables.)*

### §6.6 The key-conditioning claims close, and one of them rests on four thousandths

**Teacher forcing (line 6) against the deployable models (lines 4, 5):**

| Axis | Line 6 | Line 4 | Line 5 | What the paper says |
|---|---|---|---|---|
| Degree | .859 | .762 | .749 | *"a large effect"* — **+9.7 and +11.0 points** ✓ |
| Quality | .865 | .867 | .864 | *"little effect"* — **−0.2 and +0.1** ✓ |
| Inversion | .872 | .872 | .872 | *"little effect"* — **identical to the printed precision in all three rows** ✓ |

**★ The inversion column reads .872 on lines 4, 5 and 6 alike.** That is a stronger result than the
paper claims for it: not merely little effect, but **no movement at three decimal places across the
three All-data rows — unconditioned, conditioned on a predicted key, and conditioned on the true
key** — which is what its stated reason predicts: *"a first-inversion minor chord is a
first-inversion minor chord regardless of the key in which it occurs."* *(★ BOUNDED AT THE SWEEP.
**FORMER WORDING, PRESERVED (#12):** "no movement at all at three decimal places **across the whole
key-conditioning axis**" — **the observation covers lines 4 to 6 and not lines 1 to 3**, which are
different models on different data, so *the whole axis* named more than the three rows checked.)*

**Conditioned on a PREDICTED key (line 5) against unconditioned (line 4):**

| Axis | Line 4 | Line 5 | Difference | The paper's account |
|---|---|---|---|---|
| Degree | .762 | .749 | **−1.3 points** | *"The unconditional model does better predicting degree"* ✓ |
| RN₋root | .620 | .624 | **+0.4 points** | *"the conditioned model does better predicting the composite RN₋root"* ✓ |
| Quality | .867 | .864 | −0.3 | not mentioned |
| Key | .822 | .823 | +0.1 | not mentioned |

**Both claims close in direction.** **★ BUT THE COMPOSITE LIMB RESTS ON FOUR THOUSANDTHS, AND
WHETHER THAT EXCEEDS THE NOISE CANNOT BE ASSESSED FROM THE EIGHT PAGES AS READ**, which report no
uncertainty, no repetition count and no seed anywhere in Table 4 (§7.2). The paper then builds an explanatory
argument on that difference — that key conditioning makes the two predictions more coherent —
**which is exactly the shape a difference within noise would also produce.** Nothing here says the
difference is noise; what is said is that the paper supplies nothing that would settle it.

### §6.7 The corpus arithmetic: what Table 1 gives, what it does not, and where the word *subset* fails

**Derived from Table 1's six cells:**

| Quantity | All | AugmentedNet v1 | v1 as a share of All |
|---|---|---|---|
| Scores | 1,404 | 347 | **24.7 %** |
| Notes | 1,289,888 | 701,703 | **54.4 %** |
| Chords | 161,473 | 77,570 | **48.0 %** |
| **Notes per score** | **918.7** | **2,022.2** | v1's are **2.20 ×** longer |
| **Chords per score** | **115.0** | **223.5** | v1's carry **1.94 ×** as many |
| **Notes per chord** | **7.99** | **9.05** | v1's chords hold **13 %** more notes |

**★ THE SUBSET IS A QUARTER OF THE SCORES AND MORE THAN HALF THE NOTES.** The paper does not remark
on this. It bears directly on claim 24 at §4 — the paper's explanation of why key prediction is
easier on the subset is about *repertoire*, and Table 1 shows the two datasets also differ sharply
in the LENGTH and the harmonic density of their scores. **This read proposes no alternative
explanation and measures neither; it records that a second difference exists and is unaddressed.**

**★ AND THE WORD *subset* IS REFUTED BY THE PAPER'S OWN NEXT SENTENCES.** §3.1 calls AugmentedNet v1
*"the subset of our data used in those papers"* and then states that v1 includes **both** analyses
of doubly-annotated TAVERN scores while the full corpus keeps only one at random, those duplicates
comprising **106,981 notes — 15.25 % of v1's note count.** So:

- **v1 contains 106,981 notes of analysis material the full corpus excludes by construction**, and
  is therefore not a subset of it as note populations.
- Excluding those duplicates leaves **594,722** notes, which is **46.1 %** of the full corpus's
  notes — **if** all of them are in it, which the paper does not state.

**Two further things Table 1 does not settle, each of which a reproduction would need:**

- **Whether the "Scores" column counts scores or (score, analysis) pairs.** For TAVERN, v1 holds two
  analyses of one score; whether that is one row or two in the 347 is not stated.
- **Whether 347 is before or after the seven exclusions of footnote 3.** The footnote says seven
  scores *"were excluded"*; Table 1 gives 347 with no note attached.

### §6.8 ★ THE FULL-CORPUS COMPARISON CROSSES A CHANGED DATASET, AND THE TEST SPLIT FOR LINES 4–6 IS STATED NOWHERE IN THE EIGHT PAGES AS READ

The paper is explicit that lines 1–3 exist **to be** the like-for-like comparison: *"on lines 1 to 3,
training on the dataset and training/validation/testing splits used by [6, 10] **for a fair
comparison with these prior papers**, and on lines 4 to 6, training on our complete dataset."*

It then writes, of lines 4–6: *"RNBert exceeds the performance of the earlier models by an even
larger margin, especially when predicting the composite Roman numeral."*

**The earlier models are lines 1 and 2, which exist only on the AugmentedNet v1 splits.** So the
comparison invited by that sentence sets a full-corpus-trained model against subset-trained
baselines. **Two things change at once** — the training data and, so far as the paper says anything,
the evaluation data — and the paper has already named the other block as the fair one.

**★ THE PRECISE GAP: the sentence quoted above states what lines 4–6 are TRAINED on and says nothing
about what they are EVALUATED on.** §3.1 gives the splits for the subset by reference to [6, 10];
**it states no split of the full corpus anywhere in the eight pages as read.** So a reader cannot
tell whether line 4's .620 and
line 1's .464 were measured on the same music. **This read does not assert they were not**, and it
takes no position on how large the true margin is; **what it records is that the paper does not
supply what the comparison needs.**

*(Note the paper's own care in the adjacent case: it explains at length why comparison with [7] is
not direct, and it built lines 1–3 precisely so that one comparison would be sound. The looser
sentence sits one paragraph away from both.)*

### §6.9 Figure 2's disagreements, counted — and one of them is not explained by the divergence the paper attributes them to

The paper writes: *"Either analysis is acceptable, but **the divergence** means that **nearly all
labels** in RNBert's analysis do not agree with the ground truth, in spite of being arguably
correct."*

**Counted at the figure, position by position, against the conditioned row (§5.5):**

| Position | Ground truth | RNBert (conditioned) | Agrees? | If not, on what |
|---|---|---|---|---|
| 1 | F:V | F:V⁶ | **no** | **inversion — same key, same degree** |
| 2 | V⁶₅ | V⁶₅ | **yes** | — |
| 3 | C:IV | I | no | key and degree |
| 4 | V⁶₅/V | V⁶₅/ii | no | key and secondary target |
| 5 | I⁶₄ | I⁶₄/V | no | key |
| 6 | V⁷ | V⁷/V | no | key |
| 7 | I | V | no | key and degree |

**One of seven agrees, so *"nearly all"* holds.**

**★ BUT POSITION 1's DISAGREEMENT IS NOT THE DIVERGENCE'S DOING.** Both rows read the key as F at
position 1 and both call the chord V; they differ on whether it is in root position or first
inversion. **The modulation-against-tonicization divergence begins at position 3 and cannot reach
backwards to position 1.** So of the six disagreements, **five are explained by the divergence the
paper names and one is an ordinary inversion error** — and the sentence attributes all of them to
the divergence. **The effect on the paper's argument is small and in the direction of overstating
its own case**, since the excerpt's disagreement rate is offered as evidence that disagreement
overstates error.

### §6.10 ★ THE CHAIN OF SECONDARY LABELS IN RNBert's OWN READING NAMES TWO DIFFERENT TARGETS, AND WHETHER THAT IS AN ERROR TURNS ON A CONVENTION THE PAPER DOES NOT STATE

In F major, **ii is G minor** and **V is C major**. RNBert's reading prints, in order, **V⁶₅/ii**
(position 4) and then **V⁷/V** (position 6). Read as applied dominants, the first targets G and the
second targets C: **D⁷ → G⁷ → C**, an idiomatic chain, and the chord arriving on G is the G⁷ of
position 6.

**The tension:** the label *"/ii"* names a degree whose diatonic quality in F major is **minor**,
while the chord that actually arrives on that degree in RNBert's own analysis is a **major-minor
seventh**. The ground truth avoids this by having modulated: in C, its *"V⁶₅/V"* targets the V of C,
which is major by definition.

**Whether *"/ii"* commits the annotation to the target's quality, or merely names the scale degree
of its root, is an annotation convention — and the paper states no such convention anywhere in the
eight pages as read.** So **this read records the tension and does not call it an error.** It is
noted because the paper calls both RNBert readings *"arguably correct"* without remarking on it.

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

*These are defects of the PAPER. **None of them moves a value this paper prints** — each was checked
against the printed tables one by one — and nothing is proposed. They are **named rather than
counted**, and this list is not claimed to be everything the eight pages hold. *(★ NARROWED AT THE
SWEEP. **FORMER WORDING, PRESERVED (#12):** "**None of them moves any result of it**" — *result* is
wider than *printed value*, and the Table 3 finding does bear on how the paper's own parameter
counts are to be read even though it changes none of them.)**

**Of substance — each is a place where the paper's own text disagrees with itself or with its own
figure:**

- **★ THE OCTUPLEMIDI FEATURE COUNT DOES NOT CLOSE.** The text says *"eight features"* twice and
  enumerates **seven**: time signature, tempo, bar number, metric position within the bar, pitch,
  duration, velocity. **The eighth is named nowhere in the eight pages as read** (§2.7).
- **★ TABLE 3's OWN NUMBERS IMPLY A FREEZING THE PAPER DOES NOT DESCRIBE.** The key-conditioned
  model carries **141,056** more frozen parameters than the base model, although the only freezing
  described is of MusicBERT's first 9 layers, which are identical in both (§6.2).
- **★ §4.1's "the annotated key is F" IS REFUTED BY ITS OWN FIGURE ON THE PAPER'S USUAL SENSE OF
  *annotated*.** The sentence reads: *"the unconditioned analysis gives I64, which is incorrect,
  since this is a C major chord, and the annotated key is F."* **Figure 2's ground-truth row prints
  C: from position 3 onward**, so the HUMAN annotation's key at the cadential 6-4 is **C, not F**.
  The sentence is true only if *"annotated"* means *annotated by the unconditional model* — and the
  paper uses *annotation* for the human labels throughout, including two sentences earlier in the
  same paragraph (*"the ground-truth key annotations from the labeled data"*, *"the key of the
  annotation"*). **The intended sense is put beyond doubt two sentences later**, where the paper
  writes *"in spite of being incorrect **with respect to its predicted key**"* — which is the
  model's key and not the annotator's. **The word is nonetheless used against its own established
  sense in the clause that carries the argument, and the figure printed six lines above it supplies
  the contradiction.**
  *(★ SHARPENED AT THE READ-BACK. **FORMER WORDING, PRESERVED (#12):** "The intended sense is
  recoverable from the next sentence, which says the model's own key and Roman numeral predictions
  do not cohere." — **it is the sentence after that one, and it settles the sense explicitly rather
  than by implication**; this side had not located it exactly before writing the clause.)*
- **★ THE FIGURE-2 CAPTION AND §4.2 GIVE THE SAME CELLS OPPOSITE ADJECTIVES.** The caption says the
  italicised predictions are *"Arguably incorrect"*; §4.2 says of the same predictions that they
  disagree with the ground truth *"in spite of being arguably correct."* Both can be defended
  separately — the caption's contrast is with the strikethrough cell, called *"straightforwardly
  incorrect"* — **but a reader meeting the two within one page is given the same predictions under
  opposite words.**
- **★ "the models on lines 1–3" OVER-NAMES ITS COMPARISON SET ON THE RN₋root AXIS**, where only line
  3 prints a value (§6.4).
- **★ *"the subset of our data"* IS REFUTED BY THE SAME PARAGRAPH**, which records 106,981 notes of
  duplicate analyses that the full corpus excludes (§6.7).
- **★ THE DIVERGENCE IS CREDITED WITH A DISAGREEMENT IT CANNOT HAVE CAUSED** — Figure 2's position
  1, an inversion difference inside a shared key reading (§6.9).
- **TWO EVALUATION GRIDS ARE USED AND NOT RECONCILED**: quantization at the 64th note, evaluation at
  32nd-note resolution (§2.12).

**Typographic and grammatical slips, recorded because they are in the record and NOT because they
bear on anything. None affects a value, an argument or a result:**

- *"Such homogeneity is particular desirable"* (§3.2) — for *particularly*.
- *"Encoding each distinct combination as a token, would require"* (§3.3) — a comma between subject
  and verb.
- *"we made the Roman numeral prediction by conditional on the key"* (§3.6) — *by conditional on*.
- *"the unconditonal RNBert (line 4)"* (§4.1) — for *unconditional*.
- **"roman numeral analysis" is lower-cased throughout the abstract** — four occurrences, all
  lower-case — and capitalised as *"Roman numeral analysis"* from §1 onward.
- **The RN_alt column carries no bold cell**, although the caption's rule as written is *"In the
  model comparison of lines 1–3, we indicate the best metric in bold type"* and .529 is the larger
  of that column's two values. **Defensible — RNBert has no entry in that column, so there is no
  model comparison to mark — but the caption states the rule without the exception.**
- **The RN₋root column's single value, line 3's .575, IS bolded as the best of lines 1–3**, where
  lines 1 and 2 print nothing in that column. **A cell with no competitor is marked best.**

*(★ ONE ENTRY WAS STRUCK FROM THIS LIST AT THE READ-BACK. **FORMER WORDING, PRESERVED (#12):**
"**The model's own name is spelled two ways in the document**: the title and the running text of
the attribution box use forms differing in case from the body's consistent **RNBert**, and the code
repository is **rnbert**." — **Refuted at page 1: the attribution box prints RNBert**, the same as
the body. §1.2 carries the corrected statement.)*

**In the reference list** — see §7.4, where they are listed with the entries they belong to.

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered elsewhere in the eight pages

*Each of these is a quantity the paper's own prose depends on and does not print. **The negative is
bounded to the eight pages as read** and says nothing about a supplement, a repository or a later
version.*

- **★ ANY UNCERTAINTY ON ANY FIGURE IN TABLE 4.** No standard deviation, no interval, no seed count,
  no repetition count. **Nothing says whether a figure is one run.** Two of the paper's own arguments
  turn on differences of **.004** and **.001**.
- **The split sizes** — training, validation and testing — for either dataset.
- **What lines 4–6 were EVALUATED on** (§6.8).
- **The Viterbi transition matrix's self-transition upweighting** — the one free parameter of the key
  decoding step.
- **The size of the *"negligible effect"*** the Viterbi decoding has on measured accuracy, although
  the sentence says it was measured.
- **The entropy figures** behind §3.6's two scenarios, and any threshold separating them.
- **The size of the *"small degradation"*** from learned task-loss weighting.
- **The size of the *"small decline"*** from the NADE-style approach, said to be *"across all
  metrics"*.
- **How much *"barely improved"*** the simple key-embedding layer was (footnote 7).
- **Any figure at all for the synthetic-data experiment** that *"did not improve the model
  performance"*.
- **The proportion behind *"a high proportion"*** of inaccurate predictions being acceptable
  alternates, and any account of the *"qualitative sampling"* it rests on — its size, its selection
  rule, or who judged.
- **Any value for the ceiling** §4.2 proposes.
- **The count of enharmonically ambiguous keys in the corpus**, on which claim 8 rests and which is
  computable from material the author holds.
- **A root accuracy for any model**, which the composite RN₊root conjoins.
- **The eighth OctupleMIDI feature** (§7.1).
- **Any account of the 141,056 extra frozen parameters** (§6.2).

### §7.3 ★ WHAT IS BOTH MEASURED AND STRUCTURAL HERE, for a reader deciding what this paper can bear

*This subsection says what the paper establishes firmly enough to be leaned on, and what it does
not. **It takes no position on what this project's record says about this paper: no sweep was run
and no surface of the record was opened for it** (§0). Where a term of this project is named below,
it is cited to the one line this side actually read this sitting and to nothing else.*

**What it can bear:**

- **That a pretrained masked language model, fine-tuned, beats from-scratch models on this task
  under a like-for-like protocol.** Lines 1–3 are the same data and the same splits, and the
  improvement is on every axis the block compares except inversion and key. **This is the paper's
  strongest result and it is properly constructed.**
- **That decomposing a Roman numeral into separately-predicted components costs coherence, and that
  the cost is far smaller than independence would predict.** §6.1's arithmetic is the measured form
  of this and is derived entirely from printed cells.
- **That quality and inversion do not depend on the key, measured rather than argued.** The
  inversion column is identical to three decimals across the unconditioned, key-conditioned and
  teacher-forced models (§6.6). **That is a clean structural result about which sub-problems the key
  decision reaches.**
- **That a key decision made separately and fed forward changes what the chord decision can be.**
  Line 6 against lines 4–5 is a sanity check by the paper's own description, but it bounds the size
  of the prize: **knowing the key raises degree accuracy from .762 to .859**, so roughly a tenth of
  the degree errors of the deployed model are downstream of a key error.

**What it cannot bear:**

- **Any claim about large-ensemble or non-Classical music.** The corpus is Classical and
  small-ensemble throughout; the generalization to symphonies and operas is a stated wish (claim 6).
- **Any claim that the full-corpus figures beat the prior models by a stated margin** (§6.8).
- **Any claim about calibrated confidence.** The model's probabilities are used internally and
  published nowhere (§3.2).
- **Any claim that unspelled output costs nothing.** Claims 7 and 8 are both unmeasured, and the
  second is measurable from material in hand.
- **Any figure for how much of the residual is genuine error rather than an acceptable alternate
  reading.** §4.2 argues the distinction matters and measures nothing about it.

**Two points of contact with this project's own vocabulary, named and left there:**

- **The paper's salami-slice and this project's *slice* are defined by the same condition.** The
  paper: *"at each timestep with one or more onsets or releases, we split any ongoing notes into
  two"*. The decisions register's own terms table, read at `DECISIONS.md` line 186 this sitting:
  *"slice — The smallest stretch of music analysed: a span during which exactly the same notes are
  sounding. It begins when any note starts or stops and ends at the next such moment."* **The
  defining condition is the same in both. This read records the coincidence of definitions and
  asserts nothing further** — it has not read any layer specification and takes no position on
  whether the two are the same object in use.
- **The evaluation units are differently constructed.** The paper counts *"the proportion of time
  that the predicted labels are accurate, with 32nd-note resolution"* — duration-weighted on a
  fixed grid. `DECISIONS.md` line 201, read this sitting, describes this project's robust unit as
  cutting *"at every boundary either we or the annotator placed"* so that *"a change in how finely
  we cut cannot move the number"*. **Both weight by time; one uses a fixed grid and the other the
  union of both parties' boundaries.** Named, and nothing is concluded from it.

### §7.4 The reference list, transcribed, and the bound on what it shows

**The list runs [1] to [29]**, printed on PDF pages 7 and 8. Transcribed in full:

| # | Entry, as printed |
|---|---|
| [1] | J. Pauwels, K. O'Hanlon, E. Gomez, and M. B. Sandler, "20 Years of Automatic Chord Recognition from Audio," in *Proceedings of the International Society for Music Information Retrieval Conference*, 2019. |
| [2] | E. Aldwell, C. Schachter, and A. C. Cadwallader, *Harmony & Voice Leading*, 4th ed. Schirmer/Cengage Learning, 2011. |
| [3] | S. M. Kostka and D. Payne, *Tonal Harmony, with an Introduction to Twentieth-Century Music*, 5th ed. McGraw-Hill, 2004. |
| [4] | T.-P. Chen and L. Su, "Functional harmony recognition of symbolic music data with multi-task recurrent neural networks." in *Proceedings of the International Society for Music Information Retrieval Conference*, 2018, pp. 90–97. |
| [5] | G. Micchi, M. Gotham, and M. Giraud, "Not All Roads Lead to Rome: Pitch Representation and Model Architecture for Automatic Harmonic Analysis," *Transactions of the International Society for Music Information Retrieval*, vol. 3, no. 1, pp. 42–54, 2020. |
| [6] | N. N. López, M. Gotham, and I. Fujinaga, "AugmentedNet: A Roman Numeral Analysis Network with Synthetic Training Examples and Additional Tonal Tasks." in *Proceedings of the International Society for Music Information Retrieval Conference*, 2021, pp. 404–411. |
| [7] | N. N. López, "Automatic Roman Numeral Analysis in Symbolic Music Representations," Ph.D. dissertation, McGill University (Canada), 2022. |
| [8] | T.-P. Chen and L. Su, "Harmony Transformer: Incorporating chord segmentation into harmony recognition," in *Proceedings of the International Society for Music Information Retrieval Conference*, 2019. |
| [9] | ——, "Attend to Chords: Improving Harmonic Analysis of Symbolic Music Using Transformer-Based Models," *Transactions of the International Society for Music Information Retrieval*, vol. 4, no. 1, pp. 1–13, 2021. |
| [10] | E. Karystinaios and G. Widmer, "Roman Numeral Analysis with Graph Neural Networks: Onset-wise Predictions from Note-wise Features," in *Proceedings of the International Society for Music Information Retrieval Conference*. arXiv, 2023. |
| [11] | M. Zeng, X. Tan, R. Wang, Z. Ju, T. Qin, and T.-Y. Liu. (2021) MusicBERT: Symbolic Music Understanding with Large-Scale Pre-Training. [Online]. Available: http://arxiv.org/abs/2106.05630 |
| [12] | Y.-H. Chou, I.-C. Chen, C.-J. Chang, J. Ching, and Y.-H. Yang. (2021) MidiBERT-Piano: Large-scale Pre-training for Symbolic Music Understanding. [Online]. Available: http://arxiv.org/abs/2107.05223 |
| [13] | J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," 2019. [Online]. Available: http://arxiv.org/abs/1810.04805 |
| [14] | Z. Li, R. Gong, Y. Chen, and K. Su, "Fine-Grained Position Helps Memorizing More, a Novel Music Compound Transformer Model with Feature Interaction Fusion," *Proceedings of the AAAI Conference on Artificial Intelligence*, vol. 37, no. 4, pp. 5203–5212, 2023. |
| [15] | M. Neuwirth, D. Harasim, F. C. Moss, and M. Rohrmeier, "The Annotated Beethoven Corpus (ABC): A Dataset of Harmonic Analyses of All Beethoven String Quartets," *Frontiers in Digital Humanities*, vol. 5, p. 16, 2018. |
| [16] | J. Hentschel, M. Neuwirth, and M. Rohrmeier, "The Annotated Mozart Sonatas: Score, Harmony, and Cadence," *Transactions of the International Society for Music Information Retrieval*, vol. 4, no. 1, pp. 67–80, 2021. |
| [17] | J. Hentschel, Y. Rammos, M. Neuwirth, and M. Rohrmeier, "An Annotated Corpus of Tonal Piano Music from the Long 19th Century," 2022. [Online]. Available: https://zenodo.org/records/10171721 |
| [18] | J. Devaney, C. Arthur, N. Condit-Schultz, and K. Nisula, "Theme And Variation Encodings with Roman Numerals (TAVERN): A New Data Set for Symbolic Music Analysis." in *Proceedings of the International Society for Music Information Retrieval Conference*, 2015, pp. 728–734. |
| [19] | M. Gotham, G. Micchi, N. N. López, and M. Sailor, "When in Rome: A Meta-corpus of Functional Harmony," *Transactions of the International Society for Music Information Retrieval*, vol. 6, no. 1, pp. 150–166, 2023. |
| [20] | C. W. White and I. Quinn, "The Yale-Classical Archives Corpus," *Empirical Musicology Review*, vol. 11, no. 1, pp. 50–58, 2016. |
| [21] | G. Micchi, K. Kosta, G. Medeot, and P. Chanquion, "A deep learning method for enforcing coherence in Automatic Chord Recognition." in *Proceedings of the International Society for Music Information Retrieval Conference*, 2021, pp. 443–451. |
| [22] | P. Badura-Skoda, *Interpreting Bach at the Keyboard*. Oxford University Press, 1995. |
| [23] | D. Temperley, "The Line of Fifths," *Music Analysis*, vol. 19, no. 3, pp. 289–319, 2000. |
| [24] | C.-Z. A. Huang, A. Vaswani, J. Uszkoreit, N. Shazeer, I. Simon, C. Hawthorne, A. M. Dai, M. D. Hoffman, M. Dinculescu, and D. Eck, "Music Transformer," 2018. [Online]. Available: http://arxiv.org/abs/1809.04281 |
| [25] | S. Oore, I. Simon, S. Dieleman, D. Eck, and K. Simonyan, "This time with feeling: Learning expressive musical performance," *Neural Computing and Applications*, vol. 32, no. 4, pp. 955–967, 2020. |
| [26] | Y.-S. Huang and Y.-H. Yang, "Pop Music Transformer: Beat-based Modeling and Generation of Expressive Pop Piano Compositions," in *Proceedings of the 28th ACM International Conference on Multimedia*, 2020. |
| [27] | W.-Y. Hsiao, J.-Y. Liu, Y.-C. Yeh, and Y.-H. Yang, "Compound Word Transformer: Learning to Compose Full-Song Music over Dynamic Directed Hypergraphs," *Proceedings of the AAAI Conference on Artificial Intelligence*, 2021. |
| [28] | L. Liebel and M. Körner. (2018) Auxiliary Tasks in Multi-task Learning. [Online]. Available: http://arxiv.org/abs/1805.06334 |
| [29] | J. Qiu, C. L. P. Chen, and T. Zhang. (2022) A Novel Multi-Task Learning Method for Symbolic Music Emotion Recognition. [Online]. Available: http://arxiv.org/abs/2201.05782 |

**Defects in the list, named rather than counted. None of them moves a value or an argument of the
paper**, and they are recorded because a reference list is part of what a paper publishes:

- **A sentence-final period stands INSIDE the quoted title, before *"in"***, at **[4]**, **[6]**,
  **[18]** and **[21]** — four entries sharing one slip. **Every other entry carrying a quoted title
  uses a comma there instead**, which was checked entry by entry across the whole list at the
  read-back and not assumed from a sample.
- **[10] gives a publisher of "arXiv" for a paper it places in conference proceedings**, and puts a
  period after the proceedings name: *"in Proceedings of the International Society for Music
  Information Retrieval Conference. arXiv, 2023."* **The venue and the deposit are run together in
  one field.**
- **Page numbers are present for some proceedings entries and absent for others** — present at [4],
  [6], [18], [21]; absent at [1], [8], [26], [27].
- **Two styles are used for the same kind of online preprint.** At **[11]**, **[12]**, **[28]** and
  **[29]** the year comes in parentheses BEFORE the title and the title carries **no quotation
  marks**; at **[13]**, **[17]** and **[24]** the title is quoted and the year follows it. **The two
  groups are internally consistent**, so this is one split and not seven separate slips.
- **[17] carries no venue of any kind**, only a year and a Zenodo address.

**★ THE BOUND ON WHAT THIS LIST SHOWS, STATED BECAUSE IT IS EASY TO OVERREAD.** **Every entry above
is transcribed from the printed page and checked against nothing.** No reference was followed, no
DOI resolved, no title verified against its source, and no web access was used at any point. **So
this read establishes what the list PRINTS and not whether any entry is correct.**

**One observation of the list's composition, offered as an observation:** the paper cites, by
number, several works that are themselves separate members of this project's reading population —
**[4]**, **[5]**, **[6]** and **[10]** among them — and it transcribes results from two of those
into its own Table 4. **This read opened none of those papers and none of their extracts**, and
takes no position on any relationship between them beyond what this paper itself prints.

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

**Every one of the eight pages was re-opened**, as four requests of two pages each — 1–2, 3–4, 5–6,
7–8 — and every image was present and legible, checked at the image and not at the call's success
line. The whole text was then read against what this file had written of it, table by table and
quotation by quotation, including the reference list entry by entry.

**★ PAGE 1 WAS RE-OPENED DELIBERATELY, AND THAT IS NOT A CREDIT TO THIS SIDE.** The previous
sitting's own user-ordered check found that its read-back had covered pages 2 through 8 and **not**
page 1 — the page carrying the title, the authors, the licence block and the abstract — so that its
identity section rested on a single reading. **That fault was named for this side in the entry it
booted from, and re-opening page 1 is this side following an instruction rather than noticing
anything.** It is recorded because **the re-opening is what found this file's largest defect**
(§8.2, item a), which would otherwise have stood.

**The sweep** was a pattern search over this file for absolutes and for words that carry an
unstated quantifier — *only, never, nowhere, every, all, none, always, exhaustive, complete,
comprehensive, total, entirely, cannot, must, certain, proves, establishes* — with **every hit read
at its own line** and judged against what this side had actually done or checked. A count of hits
is not that sweep and no count is offered as one.

**A third pass, not required by the procedure and run anyway:** every cross-reference of the form
§n.m inside this file was listed and read against the heading it names.

### §8.2 What the read-back and the sweep struck in this side's own writing

**Named rather than counted. Every correction stands at its own site with the former wording
preserved (#12).**

**Struck at the read-back — the pages, re-opened, refuted the writing:**

- **(a) ★ THE LARGEST ONE. This file claimed the model's name was "spelled two ways in the
  document" and named the attribution box as one of the two.** Page 1, re-opened, prints **RNBert**
  in the attribution box — **the same spelling the body uses without exception.** The claim was
  written from one reading of page 1 and is refuted by the second. **There is no inconsistency**,
  and §1.2 now says so. *(This is an assertion about a thing this side had looked at once and then
  described from memory of the looking — §8.3, tell B.)*
- **(b) *"Every other empty cell is blank"* of Table 4 is refuted by Table 4's own typesetting.**
  Lines 4–6 print a single composite value **centred across the RN₊root/RN₋root region** rather than
  one filled cell beside one empty one. The transcription's assignment of those values to RN₋root is
  correct, but it comes from the paper's prose and not from the table. §5.4 now records both.
- **(c) *"The intended sense is recoverable from the next sentence"* was wrong about where.** It is
  the sentence after that one, and it settles the sense **explicitly** — *"in spite of being
  incorrect with respect to its predicted key"* — rather than by implication. The clause had been
  written without locating the sentence it appealed to.

**Struck at the sweep — absolutes and quantifiers this side had not derived:**

- **(d) *"Independence would put THE BEST COMPOSITE at .393"*** — a superlative true of the
  like-for-like block and false across the table, where line 5's .624 is higher against a different
  product. Narrowed to name line 3.
- **(e) *"The model is never asked where one chord ends and the next begins"*** — too strong. The
  labelling does determine the boundaries; what it never does is search for them, and that
  distinction is the whole point of the observation.
- **(f) *"the model cannot know how many voices sound a pitch"*** — over-reaching its own preceding
  clause, which names three conditions (same pitch, same onset, same release) that must ALL hold
  before a note is removed.
- **(g) Claim 1 of §4 recorded an unqualified win** over a block in which the model loses two of six
  columns — **and the paper's own sentence is more careful than this file's was**, claiming only
  degree and quality.
- **(h) *"None of them moves any result of it"*** — *result* is wider than *printed value*, and the
  Table 3 finding bears on how the paper's parameter counts are read.
- **(i) *"no movement at all across the whole key-conditioning axis"*** — named more rows than were
  checked; the observation covers the three All-data rows.
- **(j) Four negatives were left unbounded and are now bounded to the eight pages as read** — at
  §6.2, §6.5, §6.6 and §6.8. A negative over a paper is *met nowhere in the pages as read*, never
  *printed nowhere*.

**Struck at the cross-reference pass:**

- **(k) FOUR references pointed at the wrong subsection of §6** — one in §2.2 and three in the §4
  claims table — each naming a neighbouring subsection because the numbering shifted while §6 was
  being built. **All four are corrected.** None of them changed a claim; all four would have sent a
  reader to the wrong evidence.

**ADDED at the read-back rather than struck, because re-reading found things the first pass had not
seen:**

- The RN_alt column carries **no bold cell** although the caption's rule as written would bold .529;
  and RN₋root's single value **is** bolded as best with no competitor in its column (§7.1).
- The centred-cell fidelity note at §5.4 (b above).
- The sentence that settles the *"annotated key"* ambiguity (c above).
- That the year-first reference group also **drops quotation marks**, so the list carries one style
  split rather than seven slips (§7.4).
- That §6.7's corpus arithmetic supplies a **second** candidate difference between the two datasets,
  which bears on the paper's stated cause at claim 24 (§6.5).

### §8.3 ★ TWO CANDIDATE FINDINGS WERE DROPPED BECAUSE THIS SIDE COULD NOT ESTABLISH THEM, AND THEY ARE RECORDED AS DROPPED RATHER THAN LEFT OUT

- **★ A SUSPECTED WRONG WORD IN §4.1 THAT THIS READ WILL NOT ASSERT.** At both openings of page 6,
  the sentence describing Figure 2 read to this side as *"with tonicized dominant chords at the half
  cadence that concludes **the discussion**"*, where §4.2's parallel sentence about the same half
  cadence reads *"that concludes **the example**"*. **This side does not assert it as a defect.**
  The reason is exact: *discussion* occurs **twice more on the same page**, in the Figure 2 caption,
  which is precisely the condition under which a reader completes a familiar word into a slot — and
  **two readings of the same page image are not two independent measurements**, they are the same
  pixels read twice by the same side. **Recorded here so that a later reader can settle it at the
  document; nothing in this file rests on it.**
- **★ THE ITALIC MARKING OF FIGURE 2's CELLS COULD NOT BE RESOLVED AT THE IMAGE.** The caption says
  arguably-incorrect predictions are printed in italic; which individual cells carry it cannot be
  told apart from the surrounding type at this rendering. **No claim in this file rests on it** —
  §6.9's finding rests on the printed symbols, which are legible, and on nothing else.

### §8.4 The degradation tells, reported unprompted

**The user's standing rule of 2026-08-15 asks that a side name its own degradation tells rather than
wait to be asked. Two of the named tells fired in this side's own writing. The instances are NAMED
and deliberately NOT totalled.**

- **Tell A — a count, a proportion, a ranking or a superlative put on this side's own reading or its
  own findings without deriving it.** *(i)* **(d)** above, a superlative over Table 4's composites
  that the table refutes. *(ii)* **(b)**, an absolute about a table this side had itself transcribed
  and which that table's typesetting refutes. *(iii)* **(h)**, a quantifier over a defect list at a
  width wider than the one checked. *(iv)* **(i)**, an absolute naming more rows than were examined.
- **Tell B — an assertion about a thing this side had not examined.** *(v)* **(a)**, a statement
  about what the attribution box prints, written from one reading and refuted by the second — **the
  most serious of the set**, because it asserted an inconsistency in the paper that does not exist.
  *(vi)* **(c)**, a statement about where in the paper a sentence sits, written without locating it.

**What this means, stated without inflation.** **What fired is TWO named tells**, not several
different ones, and this side claims nothing more than that. **That every instance was caught by a
pass of this side's own does NOT lower the count** — the hundred-and-eightieth, the
hundred-and-eighty-first and the hundred-and-eighty-second each record exactly that of their own
sittings, the last of those read whole by this side and the first two relayed through it.

**★ AND THE DIRECTION IS WORTH A NEXT SIDE'S NOTICE: FIVE OF THE SIX ARE OVER-CLAIMS AND ONE IS
NOT.** Item **(g)** is the opposite shape — this file recorded a *win* the paper itself states more
narrowly, which is an over-claim on the PAPER'S behalf rather than on this side's. **A check looking
only for this side's own inflation would have passed it**, which is the same asymmetry the previous
sitting's second pass recorded of itself in the other direction.

### §8.5 The bound on this section

**The read-back re-opened every page; it is still a further pass over the same writing by the same
side, and nothing here says a further one would come back empty.** **The sweep is a pattern search
followed by reading each hit at its own line — a claim the pattern does not match is not looked at
by it**, so the sweep bounds what it found and not what the file contains. **The cross-reference
pass reads only references of the form §n.m inside this file** and says nothing about references to
the paper's own sections, which were checked at the read-back instead. **No claim is made that the
three passes together are complete.**

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**The first extract was opened for the first time AFTER this file had been landed and proved**, at
`reading_pass/extracts/sailor-2024-rnbert-fine-tuning-a-masked-language-model-for-roman-numeral-analysis.md`,
**65,160 bytes** at this sitting's own staging call — **matching to the byte the figure the
hundred-and-eighty-second entry's table relays**, which is the first independent confirmation of any
cell of that table. **It was then read whole.**

**The independence is evidenced by the order of acts and not claimed:** this file's first landing,
proved at 112,458 bytes, happened before that path was staged. **What contamination exists is
declared at §0 and is about a NEIGHBOURING paper, not this one.**

**What the comparison reached, and what it did not.** It reached everything both files say about
**this paper**: every transcribed cell, every quotation, every protocol constant, the identity
items, and every arithmetic derivation. **It did NOT reach the first extract's statements that point
INTO this project's record** — its verification of `FRAMEWORK.md` DP-A, §S4(a) and the entanglement
argument, of `population.md` V9, its eight-places claim, its two sweeps, its bibliography and tier
findings, its routing of thirteen findings, and its whole adopt-or-argue section. **This side opened
none of those objects.** On that half **this is silence and not a second opinion**, and a reader must
not take this file's silence there for agreement.

### §9.2 What both reads reached independently, which is the strongest thing this cross-check produced

**Recorded first because it is not a defect and would otherwise go unrecorded.** Neither read saw the
other.

1. **EVERY PRINTED CELL BOTH READS TRANSCRIBED AGREES.** Table 1 whole (six cells); Table 3 whole
   (four cells); **Table 4 whole — all six lines and every column, including which cells carry bold,
   which are blank and which read N/A.** Not one numeric disagreement anywhere.
2. **Both derived the deployable key-conditioning difference identically, to five values:** line 5
   minus line 4 gives Degree **−.013**, Quality **−.003**, Inversion **0.000**, Key **+.001**,
   RN₋root **+.004**.
3. **Both derived the teacher-forcing difference identically:** line 6 minus line 4 gives Degree
   **+.097**, Quality **−.002**, Inversion **0.000**.
4. **Both single out the inversion invariance** — 0.000 across the key-conditioning rows — and both
   attribute it to the paper's own stated reason, that a first-inversion minor chord is one
   regardless of key.
5. **Both record that Table 4 carries NO uncertainty of any kind**, and both name it as a bound on
   what any argument may lean on. The first extract cites principle #24 for it; this read reaches it
   from the table.
6. **Both record the same set of claims the paper makes without a figure:** the Viterbi decoding's
   *"negligible effect"*, the *"small degradation"* from learned task weighting, and the *"small
   decline"* from the NADE-style approach.
7. **Both record that the paper discards pitch spelling and argues the loss away without measuring
   it**, and both name the rule-based-respelling argument and the rarity argument as the two halves
   of that defence.
8. **Both record the paper's own ceiling statement at §4.2 and both refuse to carry a value out of
   it**, on the same ground: it rests on a priori argument plus unreported qualitative sampling.

**That is eight agreements, counted off the list above and not asserted separately.** **Seven of the
eight are about what the paper SAYS and DOES NOT SAY; the first is about what it prints.**

### §9.3 ★ The disagreements — three against the first extract, one against this side, one unresolved

**Each was resolved at the paper and not at the other file.** Every page carrying a disagreement was
opened a **third** time for it.

**(a) ★ THE ONE WITH REAL WEIGHT: A CHANGED WORD THAT CHANGES THE MECHANISM, AT §3.5.2.** That file
quotes: *"In evaluation, in order to obtain a single prediction **for each token in the input**, we
average the logits of simultaneous notes."* **The paper prints *"in order to obtain a single
prediction FOR EACH SALAMI SLICE, we average the logits of simultaneous notes"***, established at a
third opening of page 4.

**Why it matters, stated exactly.** *A single prediction for each token in the input* describes **no
aggregation at all** — a token is a note, and the whole point of the sentence is that the per-note
predictions are collapsed to one per slice. **The paper's own abstract, which that same extract
quotes three pages earlier, says the opposite of its quotation:** *"aggregate the predictions of
simultaneous notes to achieve a single label at each time step."* **And §3.7, which that same extract
also quotes, says it again:** *"we average the logits of simultaneous notes to obtain a single set of
logits for each salami-slice."* **So that file contains the refutation of its own quotation twice
over.** No transcribed value moves, and the extract's substantive account of the method is not built
on the wrong phrase — but **it is a mechanism reported wrongly inside a quotation**, which is the one
class the doubling most needs to catch.

**★ AND IT IS THE EXACT SHAPE THE METHOD POINT THIS SIDE WAS HANDED PREDICTED.** The
hundred-and-eighty-second entry relays, from the entry before it, that *the other read's prose
summary of a protocol is where a mechanism defect hides, because a cell is copied while a mechanism
is paraphrased.* **Here every cell of four tables is copied exactly and one mechanism inside a
quotation is not.** The point fired on its first application, and this side records that it was
looking for this shape because it had been told to.

**(b) THE ABSTRACT DOES NOT PRINT THE MODEL'S NAME AT ALL.** That file states: *"The title and
abstract print RNBERT; the body text and footnotes print RNBert."* **The abstract names MusicBERT and
never names this paper's own model**, established at a third opening of page 1. **Its conclusion
survives** — the title does print RNBERT and the body prints RNBert, so both spellings are the
paper's own and neither record spelling is an error — **but the evidence offered for it is wrong at
one of its two named places.**

**(c) THE ATTRIBUTION BOX IS TRANSCRIBED WITH THE WRONG SPELLING, IN THE SAME IDENTITY SECTION.**
That file renders it as *"M. Sailor, 'RNBERT: Fine-Tuning a Masked Language Model…'"*. **The box
prints RNBert**, established at a third opening of page 1. **This is the same word as (b) and a
different act** — (b) is a claim about where a spelling appears, (c) is a quotation that does not
match. **No value moves.**

**★ (b) AND (c) ARE WHERE THIS SIDE'S OWN WORST DEFECT SAT TOO, AND THE CONVERGENCE IS THE FINDING.**
This file's read-back struck a claim of its own about the attribution box's spelling — in the
opposite direction, and equally wrong (§8.2, item a). **Both reads mis-stated page 1's name evidence
independently.** That is not a coincidence to wave at: **page 1 carries the identity block, both
reads treated it as the easy part, and both got it wrong** — and the previous sitting's own check
records that its read-back skipped page 1 entirely. **Two consecutive sittings of this line have now
had a page-1 identity defect, and a third instance sits in this paper's first extract, written by an
earlier session altogether.** The remedy this file can offer is small and concrete: **re-open the
identity page at the read-back, and quote the licence box rather than describing it.**
*(★ CORRECTED AT THE USER-ORDERED CHECK. **FORMER WORDING, PRESERVED (#12):** "**Three consecutive
sittings** have now had a page-1 identity defect." — **an underived count that conflated a SITTING
with an INSTANCE.** Two sittings are establishable here; the first extract's instance is a third
INSTANCE and not a third consecutive sitting, its file dating from an earlier session. **What the
sittings before the previous one record on this axis is unknown to this side, which did not open
them.**)*

**(d) A CHANGED WORD INSIDE A §3.1 QUOTATION: *"works BY women composers"* for *"works OF women
composers"*.** Established at a third opening of page 2. The sense is unchanged and no value moves.
**The reason this side is willing to call it** — rather than recording it unresolved like (f) below —
**is that the direction of the risk runs the other way here:** *works by* is the idiomatic phrase and
*works of* the unusual one, so a reader completing from habit would produce *by*. **This side read
the less idiomatic word three times, which is evidence of reading rather than completing.**

**(e) ★ AGAINST THIS SIDE — A CHANGED WORD THAT TURNED THE AUTHOR'S HEDGE INTO AN ASSERTION, AT
§3.3.** This file quoted the decoherence passage as *"this multitask approach **obtains** a smaller
vocabulary size at the expense of some coherence"*. **The paper prints *"may obtain"***, established
at a third opening of page 3, **and the first extract had it right.** **Corrected at §2.4 with the
former wording preserved.** It is the sentence in which the paper concedes what its own decomposition
costs, so removing the hedge misreports the author's own confidence in the trade. **The read-back did
not catch it, and the reason is worth carrying: that pass checked that the passage said what this
file said it said, which is a different act from checking that the quotation is exact.**

**(f) ★ ONE WORD IS RECORDED UNRESOLVED AT THE PAPER, WHICH THE COMMISSION'S RULE PROVIDES FOR.**
Inside the same §3.3 sentence, this read has *"it may **equally** occur"* at three openings and the
first extract has *"it may **easily** occur"*. **This side does not claim it.** *"roughly equally"*
stands eight words earlier, which is precisely the condition under which a reader repeats a word it
has just read — **so here the priming risk falls on THIS side, the reverse of (d)** — and the paper
carries enough uncorrected slips elsewhere that the clumsy repetition is in character. **Sense
unchanged, no value moves, and a later reader with a searchable text can settle it in one act.**

### §9.4 What the first extract has that this read did not — adopted here and marked at its site

**Three, each tested at the paper or at this file's own transcription before being taken in, never
accepted from the other file.**

1. **AugmentedNet's Degree cell .67 is the only two-decimal value in Table 4.** Checked across all
   twenty-nine numeric cells of §5.4's transcription. **Adopted at §5.4.**
2. **The margin test of the paper's coherence claim** — the composite's lead over each rival exceeds
   every component's lead. **Re-derived at this file's own table and adopted as §6.1a**, beside §6.1's
   independence test rather than in place of it, because the two ask different questions.
3. **The two difference sets that support it** — line 3 minus line 2 and line 3 minus line 1, ten
   values. **Re-derived and adopted with (2).**

**And one thing this read can CONFIRM only half of.** That file's cross-primary check states that
Table 4's lines 1 and 2 reproduce row 49's own table on twelve values. **Its RNBERT half is correct
against this read's own transcription** — .829 / .67 / .797 / .788 / .464 / .515 and .813 / .714 /
.784 / .803 / .518 / .529 are exactly §5.4's lines 1 and 2. **Its ChordGNN half is cited to row 49's
extract, which this side did not open.** **So: half confirmed here, half silence.**

### §9.5 What this read has that the first extract does not

**Named rather than counted.** The four that bear on how a printed value or a stated claim of the
paper is read are given first.

- **★ TABLE 3's OWN NUMBERS IMPLY 141,056 FROZEN PARAMETERS THE PAPER NEVER DESCRIBES** (§6.2). That
  file transcribes Table 3 and derives nothing from it. **It is the one item of this list with no
  counterpart of any kind in the other read — the rest are things that read did not remark on, this is
  a derivation it did not make.** *(★ NARROWED AT THE USER-ORDERED CHECK. **FORMER WORDING, PRESERVED
  (#12):** "**This is the largest thing this read has that the other does not.**" — **a ranking over
  this read's own findings, on no stated measure and never derived.**)*
- **★ THE OCTUPLEMIDI FEATURE COUNT DOES NOT CLOSE** — *"eight features"* twice over a list of seven
  (§2.7, §7.1). That file does not discuss the encoding's feature list at all.
- **★ THE FULL-CORPUS COMPARISON CROSSES A CHANGED DATASET AND THE TEST SPLIT FOR LINES 4–6 IS
  STATED NOWHERE IN THE EIGHT PAGES AS READ** (§6.8). That file's fit-and-evaluation finding records
  the inherited splits for lines 1–3 and does not name what lines 4–6 are evaluated on.
- **★ §4.1's *"the annotated key is F"* IS REFUTED BY ITS OWN FIGURE ON THE PAPER'S USUAL SENSE OF
  *annotated*** (§7.1). **That file quotes the whole sentence verbatim and does not remark on it.**

And, more briefly: the composite-against-independence arithmetic (§6.1); the corpus arithmetic and
the refutation of the word *subset* (§6.7); Figure 2's disagreement count and the position whose
disagreement the divergence cannot explain (§6.9); the secondary-label target question (§6.10); the
two evaluation grids (§2.12); the caption's *"arguably incorrect"* against §4.2's *"arguably
correct"*; Table 4's centred composite cells and its two bolding irregularities (§5.4, §7.1); and
the typographic slips at §7.1.

### §9.6 What the cross-check does NOT establish

- **It does not establish that either read is better.** Step 8 is discharged in the settled form in
  one direction — the first extract is left untouched and its three items stand with the user — and
  performed on one wording in the other, this side's §2.4 quotation being corrected at its site.
  **That is a split, not a verdict**, and one of the two sides' corrections went each way.
- **It does not reach the first extract's record-facing half at all** (§9.1). **Silence there is
  silence.**
- **It is not exhaustive.** It ran over what both files carry about this paper; a later reader may
  find more, and the six items of §9.3 are named rather than offered as a complete set.
- **It changed no transcribed value in either file.** The one change on this side is a quotation's
  wording; the one word left open is (f).

---







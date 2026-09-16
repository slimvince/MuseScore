# Second extraction — Korzeniowski & Widmer, "Improved Chord Recognition by Combining Duration and Harmonic Language Models"

**Row 20 of Task B's L2 slice**, at `reading_pass/candidacy_upgrades.md` line 82, read at that line
this sitting. The row reads: *"Korzeniowski & Widmer, ISMIR 2018, combining duration and harmonic
language models"*, held, **ADMITTED**, on the reason the line itself gives — *"A segment-duration
model beside a chord language model — directly a candidate for how L2 scores segment length, which
the charter leaves to detail."*

**This is the SECOND independent extraction** required by
`cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, for a source the record classes
CENTRAL. It was written without opening the first extract. The independence bound is at §0.

---

## §0 — What was read, and the bound on this read's independence

**The paper was read whole, all eight pages**, as page images, from a bridge-staged copy of
`docs/research_papers/korzeniowski_widmer_2018_ismir_duration_harmonic_language_models.pdf`. The
held file is **384,606 bytes**, established twice — at one listing of `docs/research_papers/` and at
this sitting's own staging call, which returned the same figure.

**The page count was established AT THE TOOL**, by a deliberately out-of-range page request, which
answered *"PDF has 8 pages"*. No progress-record value was available to check it against: the
progress record was not opened in this sitting.

**THE INDEPENDENCE BOUND, STATED AND NOT CLAIMED AWAY.** The first extract,
`reading_pass/extracts/korzeniowski-widmer-2018-improved-chord-recognition-by-combining-duration-and-harmonic-language-models.md`,
**46,899 bytes at a listing, was NOT opened before this file's §0 to §8 were written and landed.**
Its existence, its exact path and its size were seen at a directory listing and nothing else was
taken from it. What contaminates this read, and is written down rather than claimed away:

- The handoff line this session booted from names this paper's **row number, its authors, its year,
  its venue and its subject**, and carries the candidacy line's own stated reason for admitting it.
  That is the record's framing of what the paper is FOR, and it was in front of this read before the
  paper was opened.
- The section form of this file was taken from **row 19's second extract's section headings alone**,
  by a heading search. **No content line of that file was read.**
- **Nothing else of the record was opened for this paper.** No sweep of the repository was run for
  its authors, its title or any of its values, so **this read asserts nothing about what the record
  says of it** — with the single exception at §7.4, which is a check of this paper's own reference
  list against `reading_pass/candidacy_upgrades.md`, run deliberately and reported with its own
  bound there.

**WHAT THIS READ DID NOT DO.** It did not open `FRAMEWORK.md`, the findings surface,
`reading_pass/population.md`, the slice derivation, the progress record,
`docs/research_papers/BIBLIOGRAPHY.md`, either commission, or any other extract's content. It takes
**no position on this paper's centrality verdict**, which is the first extract's half of the
doubling.

---

## §1 — What the paper is, and the identity axis

**Title, as printed on page 1:** *"IMPROVED CHORD RECOGNITION BY COMBINING DURATION AND HARMONIC
LANGUAGE MODELS"*.

**Authors, as printed:** Filip Korzeniowski and Gerhard Widmer.

**Affiliation, as printed:** Institute of Computational Perception, Johannes Kepler University,
Linz, Austria; contact address `filip.korzeniowski@jku.at`.

**Venue, as printed in the running header of pages 2 to 8:** *"Proceedings of the 19th ISMIR
Conference, Paris, France, September 23-27, 2018"*.

**Printed page numbers:** 10 to 17. Page 1 carries the number 10 at its foot; pages 2 to 8 carry 11
to 17 in the running header.

**Licence and attribution, as printed at the foot of page 1's left column, beside a Creative Commons
badge:** *"© Filip Korzeniowski and Gerhard Widmer. Licensed under a Creative Commons Attribution
4.0 International License (CC BY 4.0). **Attribution:** Filip Korzeniowski and Gerhard Widmer.
"Improved Chord Recognition by Combining Duration and Harmonic Language Models", 19th International
Society for Music Information Retrieval Conference, Paris, France, 2018."*

**★ THE IDENTITY AXIS COMES BACK CLEAN, AND THE FINDING IS THAT THERE IS NONE.** Every axis the
candidacy row carries — the two authors, the year, the venue and the subject — is printed in the
held document and agrees with the row. The document additionally prints its affiliation, its printed
page range, its conference dates and a full attribution string with an explicit licence. **This is
the held article, not a preprint**, on the evidence of the ISMIR proceedings running header and the
printed page numbers.

*(Bound: the axes checked are the ones the candidacy row carries, plus the licence and page range
the document volunteers. No other identity claim of the record was opened.)*

---

## §2 — The method, as the paper states it

### §2.1 The problem the paper says it is solving, and the gap it claims

The paper's own framing, §1: chord recognition faces *"the two key problems of extracting meaningful
information from noisy audio, and casting this information into sensible output"*, which it
translates into **acoustic modelling** — *"how to predict a chord label for each position or frame in
the audio"* — and **temporal modelling** — *"how to create meaningful segments of chords from these
possibly volatile frame-wise predictions"*.

The gap it claims is about the temporal half, and it is stated twice. The abstract: *"temporal
models have been shown to only smooth predictions, without being able to incorporate musical
information about chord progressions."* §1 gives the diagnosis: first-order models *"are not capable
of learning meaningful musical relations, and only smooth the predictions"*, and more powerful models
such as RNNs *"do not perform better than their first-order counterparts"*. The paper's own
explanation is **the hierarchical level, not the model class**: *"both approaches are limited by the
low hierarchical level they are applied on: the temporal model is required to predict the next symbol
for each audio frame. This makes the model focus on short-term smoothing, and neglect longer-term
musical relations between chords, because, most of the time, the chord in the next audio frame is the
same as in the current one."*

*(★ ONE WORD CORRECTED AT THE CROSS-CHECK. FORMER WORDING, PRESERVED (#12): *"the low hierarchical level
they are applied **to**"*. **The paper prints *"applied on"***, established at a third opening of page 1.
The sense does not change; the first extract has the word right and this read did not.)*

The three contributions, as §1 numbers them: *"i) we describe a probabilistic model that allows for
the integration of chord-level language models with frame-level acoustic models, by connecting the
two using chord duration models; ii) we develop and apply chord language models and chord duration
models based on RNNs within this framework; and iii) we explore how these models affect chord
recognition results, and show that the proposed integrated model out-performs existing temporal
models."*

### §2.2 The factorisation of the sequence model

The task is set up as sequence labelling: assign a categorical label `y_t ∈ Y` (a chord from a chord
alphabet) to each member of an observed sequence `x_t` (an audio frame), so that `y_t` is the
harmonic interpretation of the music represented by `x_t`. **Equation 1** is

> ŷ_{1:T} = argmax over y_{1:T} of P(y_{1:T} | x_{1:T}).

Assuming the generative structure of Figure 1, the paper factorises

> P(y_{1:T} | x_{1:T}) ∝ ∏_t [ 1 / P(y_t) ] · P_A(y_t | x_t) · P_T(y_t | y_{1:t−1}),

with `P_A` the acoustic model, `P_T` the temporal model, and `P(y_t)` the label prior, *"which we
assume to be uniform as in [31]"*.

**Figure 1's caption, as printed:** *"Generative chord sequence model. Each chord label y_t depends
on all previous labels y_{1:t−1}."*

### §2.3 The split of the temporal model into a language model and a duration model

This is the paper's structural move. `P_T` is disentangled into *"a harmonic language model P_L and a
duration model P_D, where the former models the harmonic progression of a piece, and the latter models
the duration of chords."*

**The language model** is defined as `P_L(ȳ_k | ȳ_{1:k−1})`, where `ȳ_{1:k} = C(y_{1:t})` and `C(·)`
is *"a sequence compression mapping that removes all consecutive duplicates of a chord"*. The paper's
own worked example is printed: `C((C,C,F,F,G)) = (C,F,G)`. *"The frame-wise labels y_{1:t} are thus
reduced to chord changes, and P_L can focus on modelling these."*

**The duration model** is defined as `P_D(s_t | y_{1:t−1})`, where `s_t ∈ {c,s}` *"indicates whether
the chord changes (c) or stays the same (s) at time t"*. The paper states its division of labour
explicitly: *"P_D thus only predicts whether the chord will change or not, but not which chord will
follow—this is left to the language model."*

**★ AND THE PUBLISHED DEFINITION IS WIDER THAN THE IMPLEMENTED ONE, BY THE PAPER'S OWN SENTENCE.**
*"This definition allows P_D to consider the preceding chord labels y_{1:t−1}; in practice, we restrict
the model to only depend on the preceding chord changes, i.e. P_D(s_t | s_{1:t−1}). Exploring more
complex models of harmonic rhythm is left for future work."* So the framework admits a
chord-conditioned duration model and the paper's own experiments do not contain one. This is recorded
here and again as a coupling fact at §3.3, because a design adopting the framework inherits the wider
form and the evidence only covers the narrower one.

**Equation 2**, the factorised temporal model, as printed:

> P_T(y_t | y_{1:t−1}) =
> — P_L(ȳ_k | ȳ_{1:k−1}) · P_D(c | y_{1:t−1})   if y_t ≠ y_{t−1}
> — P_D(s | y_{1:t−1})                            else

### §2.4 The chord-time lattice

**Figure 2's caption, as printed:** *"Chord-time lattice representing the temporal model P_T, split
into a language model P_L and duration model P_D. Here, ȳ_{1:K} represents a concrete chord sequence.
For each audio frame, we move along the time-axis to the right. If the chord changes, we move
diagonally to the upper right. This corresponds to the first case in Eq. 2. If the chord stays the
same, we move only to the right. This corresponds to the second case of the equation."*

The paper then states the decoding obstacle in its own words: *"This model cannot be decoded
efficiently at test-time because each y_t depends on all predecessors. We will thus use either models
that restrict these connections to a finite past (such as higher-order Markov models) or approximate
inference methods for other models (such as RNNs)."*

### §2.5 The acoustic model

§3.1. A VGG-style convolutional neural network, *"similar to the one presented in [23]"*. Three
convolutional blocks, as printed: the first *"consists of 4 layers of 32 3×3 filters (with
zero-padding in each layer), followed by 2 × 1 max-pooling in frequency"*; the second *"comprises 2
layers of 64 such filters followed by the same pooling scheme"*; the third *"is a single layer of 128
12×9 filters"*. Each block is followed by feature-map-wise dropout with probability 0.2; each layer by
batch normalisation and an ELU activation. *"Finally, a linear convolution with 25 1×1 filters followed
by global average pooling and a softmax produces the chord class probabilities P_A(y_t | x_t)."*

**The input**, as printed: *"a 1.5 s patch of a quarter-tone spectrogram computed using a
logarithmically spaced triangular filter bank"* — audio at a sample rate of 44 100 Hz, STFT with a
frame size of 8192 and a hop size of 4410; a triangular filter bank of 24 filters per octave between
65 Hz and 2100 Hz applied to the STFT magnitude; then the logarithm of the resulting magnitudes *"to
compress the input range"*.

**Two over-confidence mitigations**, with the paper's own reason: *"Neural networks tend to produce
over-confident predictions, which in further consequence could over-rule the predictions of a temporal
model [9]."* First, training with uniform smoothing — *"we assign a proportion of 1 − β to other classes
during training"*. Second, at inference, the **temperature softmax** in place of the standard softmax
in the final layer, *"Higher values of τ produce smoother probability distributions."* The values used
are **β = 0.9 and τ = 1.3**, *"as determined in preliminary experiments"*.

### §2.6 The language model

§3.2. `P_L` *"predicts the next chord, regardless of its duration, given the chord sequence it has
previously seen."* The paper does not develop this model here: *"As shown in [21], RNN-based models
perform better than n-gram models at this task. We thus adopt this approach, and refer the reader to
[21] for details."* The set-up is next-chord prediction following [28], with the inputs `z_k` being the
chord symbols given by `C(y_{1:T})`.

*(★ CORRECTED AT THE CROSS-CHECK, AND THE FIRST EXTRACT'S HAVING IT RIGHT IS WHAT EXPOSED IT. FORMER
WORDING, PRESERVED (#12): `C(y_{1:t})`. **The paper prints a capital T in this sentence**, established
at a third opening of page 3; the lower-case `t` appears elsewhere in the paper — at `ȳ_{1:k} =
C(y_{1:t})` on page 2 and at the hash function on page 4 — and both of those are transcribed correctly
above. This read's first pass carried the lower-case form into this one sentence.)*

**Figure 3's caption, as printed:** *"Sketch of a RNN used for next step prediction, where z_k refers
to an arbitrary categorical input, v(·) is a (learnable) input embedding vector, and h_k is the hidden
state at step k. Arrows denote matrix multiplications followed by a non-linear activation function. The
input is padded with a dummy input z_0 in the beginning. The network then computes the probability
distribution for the next symbol."*

### §2.7 The duration model

§3.3. `P_D` *"predicts whether the chord will change in the next time step. This corresponds to
modelling the duration of chords."*

**The paper's argument against the implicit duration models of HMMs**, as printed: *"Existing temporal
models induce implicit duration models: for example, an HMM implies an exponential chord duration
distribution (if one state is used to model a chord), or a negative binomial distribution (if multiple
left-to-right states are used per chord). However, such duration models are simplistic, static, and do
not adapt to the processed piece."*

**And its argument against the one existing explicit duration model it names**, [4]: that approach
stored beat-synchronised chord durations as discrete distributions, and is *"useful for beat-synchronised
models, but impractical for frame-wise models—the probability tables would become too large, and data too
sparse to estimate them. Since our approach avoids the potentially error-prone beat synchronisation, the
approach of [4] does not work in our case."*

**Its own choice**, with the reason it gives: recurrent networks, because *"These models are able to
adapt to characteristics of the processed data [21], and have shown great potential in predicting
periodic signals [1] (and chords do change periodically within a piece)."* The training task is
next-step prediction, *"identical in principle to the set-up for harmonic language modelling: the
network has to compute the probability of a chord change in the next time step, given the chord changes
it has seen in the past."*

### §2.8 Decoding — hashed beam search

§3.4. The paper states the cost of its own choice plainly: dynamic models *"consider all previous
observations when predicting the next one"* and so adapt to the piece — *"The flip side of the coin is,
however, that this property prohibits the use of dynamic programming approaches for efficient decoding.
We cannot exactly and efficiently decode the best chord sequence given the input audio."*

It therefore uses **hashed beam search** [32]. Plain beam search keeps only the `N_b` best solutions up
to the current time step — in this case the `N_b` best paths through all possible chord-time lattices —
but *"the beam might saturate with almost identical solutions, e.g. the same chord sequence differing
only marginally in the times the chords change. Such pathological cases may impair the final estimate."*
Hashed beam search *"forces the tracked solutions to be diverse by pruning similar solutions with lower
probability."*

**The hash function is the paper's own modification, and the paper says why.** *"For our purpose, we
define the hash function of a solution to be the last N_h chord symbols in the sequence, regardless of
their duration; formally, the hash function f_h(y_{1:t}) = ȳ_{(k−N_h):k}."* And: *"In contrast to the
hash function originally proposed in [32], which directly uses y_{(t−N_h):t}, our formulation ensures
that sequences that differ only in timing, but not in chord sequence, are considered similar."*

The summary sentence, as printed: *"we approximately decode the optimal chord transcription as defined
in Eq. 1 using hashed beam search, which at each time step keeps the best N_b solutions, and at most
N_s similar solutions."*

---

## §3 — Coupling facts

### §3.1 What it ASSUMES about its upstream

- **The input is AUDIO, and nothing in the pages as read admits any other input.** The acoustic model
  consumes a quarter-tone spectrogram of a 44 100 Hz waveform. There is no symbolic path, no score input
  and no note-level representation anywhere in the pages as read. **Every experiment reported in the
  pages as read is an audio experiment.**
- **It assumes a frame grid, and that grid is fixed by the audio front end**, not by the music: the STFT
  hop size of 4410 samples at 44 100 Hz fixes the time step. The temporal model's `s_t ∈ {c,s}` decision
  is taken once per such frame.
- **It assumes NO beat or metrical analysis**, and says so as a design choice rather than an omission:
  *"our approach avoids the potentially error-prone beat synchronisation"*. This is what it gives as the
  reason the one prior explicit duration model it names, [4], does not transfer to its setting.
- **It assumes a fixed, closed chord alphabet decided upstream of the model** — 25 classes, formed by
  mapping every chord containing a minor third to minor and all others to major, *"following [7]"*.
- **It assumes a label prior**, explicitly, and assumes it uniform: *"P(y_t) the label prior which we
  assume to be uniform as in [31]"*.
- **It assumes an acoustic model whose output is a distribution, and one that can be deliberately
  blunted.** The over-confidence mitigations of §2.5 are not incidental: the paper's own reason is that
  an over-confident frame-level distribution *"could over-rule the predictions of a temporal model"*.

### §3.2 What it HANDS downstream

- **A frame-wise chord label sequence over a major/minor alphabet** — one label per audio frame, from
  which chord segments follow by the compression mapping `C(·)`.
- **A segmentation, as a derived rather than a published object.** The paper reports *"a measure of
  segmentation"* in Table 3, but the segments are what `C(·)` produces from the frame labels; nothing in
  the pages as read has the model emit a boundary as a first-class object.
- **NO key, NO mode, NO Roman numeral, NO inversion, NO bass, NO function.** The output vocabulary is
  the 25 major/minor classes and nothing else. The paper makes no tonality claim in the pages as read.
- **NO published uncertainty.** The decode returns a best path under hashed beam search; the paper
  reports no per-segment confidence, no alternative readings and no margin. The beam holds `N_b = 25`
  solutions at each step, but nothing in the pages as read publishes them.
- **★ AND NO POSTERIOR COULD BE PUBLISHED EVEN IN PRINCIPLE — A PRECISION ADOPTED FROM THE FIRST EXTRACT
  AT THE CROSS-CHECK AND MARKED HERE.** That file states it in its own coupling facts: *"No exact
  normaliser exists (the model is not exactly decodable, §2, §3.4)."* **This read had recorded that the
  paper publishes no uncertainty; it had not recorded that the model's own structure forbids it.** The
  two cited sections are the ones this read transcribes at §2.4 and §2.8, so the precision follows from
  material both reads carry — it is the reading of it that this read lacked.
- **A learned chord embedding with structure the paper describes but does not consume.** §4.2's four
  observations about the embedding are presented as findings about the trained network, and the paper
  states in terms that it cannot explain them; no later section uses them.

### §3.3 Its own STATED scope and limits

- **Scope: audio chord recognition over a major/minor alphabet, on popular music.** All four evaluation
  corpora are popular music — Beatles, Queen, Zweieck, RWC Popular, Robbie Williams and McGill Billboard
  — and the additional training material is rock, US pop, jazz standards and Chinese pop. **No corpus
  named in the pages as read is classical or Baroque, and those pages carry no claim about any
  repertoire the paper did not test.**
- **The duration model implemented is NARROWER than the duration model defined.** `P_D(s_t | y_{1:t−1})`
  is the definition; `P_D(s_t | s_{1:t−1})` is what is built, and the paper labels the difference as
  future work: *"Exploring more complex models of harmonic rhythm is left for future work."*
- **Decoding is approximate and the paper says so.** *"We cannot exactly and efficiently decode the best
  chord sequence given the input audio."* What that approximation costs is bounded only empirically, and
  only for the n-gram language models with the negative binomial duration distribution.
- **One duration parametrisation per chord, declared as a simplification with a cited justification.**
  *"We assume a single parametrisation for each chord; this ostensible simplification is justified,
  because simple temporal models such as HMMs do not profit from chord information, as shown by [4,7]."*
  **The justification is about HMMs; the model under test is not an HMM** — see §7.1.
- **The paper states its own improvements are modest.** *"Although the improvements are modest, they are
  consistent."*

---

## §4 — Claims, labeled

**FACT** = stated or measured in this paper, at a place read in this sitting. **THEORY** = an
established published result the paper leans on, or a mechanism claim it argues rather than measures.
**CONJECTURE** = a forward or explanatory claim the paper makes without measuring it. **ASSUMPTION** =
declared by the paper as an assumption.

| # | Claim | Label | Where |
|---|---|---|---|
| 1 | The four language models score average log-probability of the correct next chord at −1.293 (GRU-512), −1.576 (GRU-32), −1.887 (4-gram), −2.393 (2-gram). | FACT | Table 1 |
| 2 | *"The GRU models predict chord sequences with much higher probability than the baselines."* | FACT | §4.2 |
| 3 | The four duration models score average log-probability of chord durations at −2.014 (GRU-256), −2.868 (GRU-16), −3.946 (negative binomial), −4.003 (exponential). | FACT | Table 2 |
| 4 | *"As seen in the table, both GRU models clearly out-perform the baselines."* | FACT | §4.3 |
| 5 | The standard model scores Root 0.812, Maj/Min 0.795, Seg. 0.804; the best model scores 0.821, 0.805, 0.814. | FACT | Table 3 |
| 6 | *"Although the improvements are modest, they are consistent, as shown by a paired t-test (p < 2.487 × 10⁻²³ for all differences)."* | FACT | §4.4 |
| 7 | *"Better language and duration models directly improve chord recognition results, as the WCSR increases linearly with higher log-probability of each model."* | THEORY — a mechanism claim argued from Figure 6, not separately measured | §4.4 |
| 8 | *"As this relationship does not seem to flatten out, further improvement of each model type can still increase the score."* | CONJECTURE — an extrapolation beyond the four and three points plotted | §4.4 |
| 9 | *"the approximate beam search does not impair the result by much compared to exact decoding."* | FACT, bounded — the exact arm exists only for the n-gram language models with the negative binomial duration distribution | §4.4 |
| 10 | A GRU duration model adapts to the harmonic rhythm of a piece; static models cannot. | THEORY — argued from one worked passage in Figure 5 | §4.3 |
| 11 | GRU-128 *"reliably remembers the period over large gaps in which the chord did not change (between seconds 61 and 76)."* | FACT, of one excerpt | §4.3, Fig. 5 |
| 12 | *"the peaks decay differently for different multiples of the period, which indicates that the network simultaneously tracks multiple periods of varying importance."* | CONJECTURE — the paper's own reading of a curve | §4.3 |
| 13 | The negative binomial *"statically yields a higher chord change probability that rises with the number of audio frames since the last chord change."* | FACT, of the distribution's form | §4.3 |
| 14 | GRU-16 adapts to the harmonic rhythm but its predictions between peaks are noisier and it fails to remember the period across the gap without chord changes. | FACT, of one excerpt | §4.3 |
| 15 | The learned chord embedding shows four named regularities: three clusters around the centre with minor chords farther out; same-root major and minor grouped, the roots a minor third apart; circle-of-fifths motion preserved as clockwise motion in the projection; and grouping corresponding to the Tonnetz. | FACT, of the trained networks the paper inspected | §4.2, Fig. 4 |
| 16 | *"At this time, we cannot provide an explanation for these automatically emerging patterns."* | The paper's own declared limit | §4.2 |
| 17 | Existing temporal models only smooth; RNNs at frame level do not beat first-order models; the cause is the low hierarchical level they are applied at. | THEORY, cited to [4,7,24] | §1 |
| 18 | An HMM implies an exponential chord duration distribution with one state per chord, or a negative binomial with several left-to-right states. | THEORY — used to justify the choice of the two baselines | §3.3, §4.3 |
| 19 | The label prior is uniform. | ASSUMPTION, declared | §2 |
| 20 | A single duration parametrisation per chord is justified because simple temporal models do not profit from chord information. | ASSUMPTION, declared, with a cited justification that is about HMMs | §4.3 |
| 21 | *"The results in this paper indicate that chord transitions modelled on the chord level, and connected to audio frames via strong duration models, indeed have the capability to improve chord recognition results."* | CONJECTURE — the conclusion's own forward statement | §5 |
| 22 | The neglect of language and duration models in prior work *"was due to the improper assumption that temporal models applied on the time-frame level can appropriately model musical knowledge"* — marked by the paper as a belief: *"we believe (see [24] for some evidence)"*. | CONJECTURE, so marked by the paper | §5 |

---

## §5 — Measured results, with corpus, measure and value as the paper states them

### §5.1 The data, transcribed from §4.1

Evaluation is **4-fold cross-validation** over a compound dataset assembled from four sources.

| Source | Contents, as printed | Audio, as printed |
|---|---|---|
| **Isophonics** | 180 songs by the Beatles, 19 songs by Queen, 18 songs by Zweieck | 10:21 hours |
| **RWC Popular [15]** | 100 songs in the style of American and Japanese pop music | 6:46 hours |
| **Robbie Williams [13]** | 65 songs by Robbie Williams | 4:30 |
| **McGill Billboard [3]** | 742 songs sampled from the American billboard charts between 1958 and 1991 | 44:42 hours |
| **Compound, as the paper states it** | *"1125 unique songs"* | *"a total of 66:21 hours of audio"* |

**★ NEITHER COMPOUND FIGURE REPRODUCES FROM THE PAPER'S OWN LISTED COMPONENTS.** The arithmetic is at
§6.1.

**Additional training data for the language and duration models only**, *"(with duplicate songs
removed)"*: 173 songs from the **Rock [11]** corpus; a subset of **160 songs from UsPop2002** for which
chord annotations are available; **291 songs from Weimar Jazz**, *"with chord annotations taken from lead
sheets of Jazz standards"*; and **Jay Chou [12]**, *"a small collection of 29 Chinese pop songs"*. The
paper states no total for these four.

**The chord vocabulary**, as printed: *"We focus on the major/minor chord vocabulary, and following [7],
map all chords containing a minor third to minor, and all others to major. This leaves us with 25
classes: 12 root notes × {major, minor} and the 'no-chord' class."*

*(★ ONE HYPHEN CORRECTED AT THE CROSS-CHECK, AT BOTH SITES THAT CARRY THE SENTENCE — here and at §6.6.
FORMER WORDING, PRESERVED (#12): *"the 'no chord' class"*. **The paper prints *'no-chord'***: the word
breaks across a line as *"no-"* / *"chord"*, and a two-word *"no chord"* would carry no hyphen at that
break. The first extract has it right and this read did not. No value moves.)*

### §5.2 Table 1, transcribed — the language models

**Caption, as printed:** *"Language model results: average log-probability of the correct next chord
computed by each model."*

| | GRU-512 | GRU-32 | 4-gram | 2-gram |
|---|---|---|---|---|
| log-P | **−1.293** | **−1.576** | **−1.887** | **−2.393** |

Four values. Less negative is better on this measure.

### §5.3 Table 2, transcribed — the duration models

**Caption, as printed:** *"Duration model results: average log-probability of chord durations computed
by each model."*

| | GRU-256 | GRU-16 | Neg. Binom. | Exp. |
|---|---|---|---|---|
| log-P | **−2.014** | **−2.868** | **−3.946** | **−4.003** |

Four values.

### §5.4 Table 3, transcribed — the integrated result

**Caption, as printed:** *"Results of the standard model (2-gram language model with negative binomial
durations) compared to the best one (GRU language and duration models)."*

| Model | Root | Maj/Min | Seg. |
|---|---|---|---|
| 2-gram / neg. binom. | 0.812 | 0.795 | 0.804 |
| GRU-512 / GRU-256 | **0.821** | **0.805** | **0.814** |

Six values. The second row is printed in bold in the paper.

**The significance statement, as printed:** *"Although the improvements are modest, they are consistent,
as shown by a paired t-test (p < 2.487 × 10⁻²³ for all differences)."*

### §5.5 Figure 6's axes, transcribed

Figure 6 is the only place in the pages as read where the WCSR of any combination **other than** Table
3's two rows appears at all. Its caption, as printed: *"Effect of language and duration models on the
final result. Both plots show the same results from different perspectives."*

**Top plot.** Horizontal axis *"Language Model Log-P"*, four printed ticks reading, left to right,
**2.393, 1.887, 1.576, 1.293**, labelled above the plot **2-Gram, 4-Gram, GRU-32, GRU-512**. Vertical
axis *"WCSR (maj/min)"*. Legend *"Duration Model"*: Neg. Binomial Exact; Neg. Binomial; GRU-16; GRU-256.

**Bottom plot.** Horizontal axis *"Duration Model Log-P"*, three printed ticks reading, left to right,
**3.946, 2.979, 2.014**, labelled above the plot **Neg. Binomial, GRU-16, GRU-256**. Vertical axis
*"WCSR (maj/min)"*. Legend *"Language Model"*: 2-Gram; 4-Gram; GRU-32; GRU-512; 2-Gram Exact; 4-Gram
Exact.

**★ THE BOTTOM PLOT'S MIDDLE TICK DISAGREES WITH TABLE 2.** The check is at §6.2.

**A BOUND THIS READ PUTS ON ITSELF: no WCSR value is transcribed from Figure 6.** The plotted points
carry no printed numbers, and a value read off a curve is not a value the paper states. What is
transcribed above is the axis tick labels, which are printed. Where this file needs a WCSR figure it
takes it from Table 3.

### §5.6 The evaluation measures, as stated

**The main measure, as printed:** *"we use the weighted chord symbol recall (WCSR) over the major/minor
chord alphabet, as defined in [30]. We thus compute WCSR = t_c/t_a, where t_c is the total duration of
chord segments that have been recognised correctly, and t_a is the total duration of chord segments
annotated with chords from the target alphabet."*

**Also reported:** *"chord root accuracy and a measure of segmentation (see [16], Sec. 8.3)."* **Neither
is defined in the pages as read** — the segmentation measure is delegated to a cited dissertation at a
named section, and the root accuracy is named without a definition and without a citation.

### §5.7 The hyper-parameters and training protocol, as stated

**Language model.** Grid search on the validation score of the first fold over: number of layers ∈ {1,2,3};
number of units ∈ {256, 512}; unit type ∈ {GRU, LSTM}; input embedding ∈ {one-hot, R⁸, R¹⁶, R²⁴}; learning
rate ∈ {0.001, 0.005}; skip connections ∈ {on, off}. Fixed for all trials: 100 epochs, stochastic gradient
descent, mini-batches of size 4, the Adam update rule, and from epoch 50 the learning rate linearly annealed
to 0. Two data augmentations: random key shift, and a random-length sub-sequence instead of the complete
chord sequence. **Footnote 7, as printed:** *"Due to space constraints, we cannot present the complete grid
search results."*

**The selected language model, as printed:** *"a single-layer network of 512 GRUs, with a learnable
16-dimensional input embedding and without skip connections, trained using a learning rate of 0.005."* It is
compared against *"a smaller, but otherwise identical RNN with 32 units"* and against a 2-gram and a 4-gram
model, the n-grams trained by maximum likelihood estimation with Lidstone smoothing, using the key-shift
augmentation only — *"sub-sequence cropping is futile for finite context models"*.

**Duration model.** Grid search on the first fold over recurrent unit type ∈ {vanilla RNN, GRU, LSTM} and
number of recurrent units ∈ {16, 32, 64, 128, 256} for the LSTM and GRU, and {128, 256, 512} for the vanilla
RNN, with one recurrent layer *"for simplicity"*. **Selected: 256 GRU units**, with the paper's own caveat —
*"although this indicates that even bigger models might give better results, for the purposes of this study,
we think that this configuration is a good balance between prediction quality and model complexity."*
Training: 100 epochs, Adam, learning rate linearly decreasing from 0.001 to 0, mini-batches of 10, sequences
cut into excerpts of 200 time steps (20 s), and gradient clipping at a value of 0.001.

**Acoustic model.** 300 epochs, 200 parameter updates per epoch, mini-batch size 512, Adam with standard
parameters, learning rate linearly decayed to 0 in the last 100 epochs.

**Decoding.** Hashed beam search with beam width **N_b = 25**, at most **N_s = 4** similar solutions, and
**N_h = 5** chords in the hash function. *"These values were determined by a small number of preliminary
experiments."*

---

## §6 — Arithmetic this read performed on the paper's own printed values

Every computation below is over values printed in the paper and transcribed at §5. Nothing here is
taken from outside the paper.

### §6.1 ★ NEITHER COMPOUND CORPUS FIGURE REPRODUCES FROM THE PAPER'S OWN LISTED COMPONENTS

**The song count.**

| Component | Songs, as printed |
|---|---|
| Isophonics — Beatles | 180 |
| Isophonics — Queen | 19 |
| Isophonics — Zweieck | 18 |
| RWC Popular | 100 |
| Robbie Williams | 65 |
| McGill Billboard | 742 |
| **Sum** | **1124** |
| **The paper's stated compound total** | **1125** |

**The sum of the paper's own six listed components is 1124. The paper states 1125. The difference is
one song, and the paper offers no reconciliation.**

**★ AND THE EXPLANATION THE SENTENCE ITSELF SUGGESTS RUNS THE WRONG WAY.** The paper's word is
*"1125 unique songs"*, and *unique* invites the reading that duplicates were removed. **Removing
duplicates can only take the total BELOW the sum of the components, never above it**, so
de-duplication cannot account for a stated total that exceeds the sum. *(The de-duplication clause the
paper does write — *"with duplicate songs removed"* — is attached to the four ADDITIONAL training
corpora, not to these four.)*

**The audio total.**

| Component | Audio, as printed |
|---|---|
| Isophonics | 10:21 |
| RWC Popular | 6:46 |
| Robbie Williams | 4:30 |
| McGill Billboard | 44:42 |
| **Sum** | **66:19** |
| **The paper's stated compound total** | **66:21** |

Carried out in full: 10:21 + 6:46 = 17:07; 17:07 + 4:30 = 21:37; 21:37 + 44:42 = 66:19, the minutes
being 37 + 42 = 79 = 1 h 19 min carried onto 21 + 44 = 65 hours. **The difference is two minutes.**

**Why both are worth reporting rather than waving through.** They are two independent figures in one
sentence, each failing to reproduce from the components printed two sentences above it, in the section
that defines what every number in the paper was measured on. **No value this read transcribed at §5 is
expressed per song or per hour**, and the cross-validation is over the compound set however large it is,
so **no figure in Tables 1, 2 or 3 moves with either total.** *(Stated at that width deliberately: this
read checked the three tables and the surrounding text, not every sentence of the paper, so the claim is
about the transcribed values and not about the paper as a whole.)* What it affects is a later reader's
ability to reconstruct the evaluation set.

**One derivation of this read's own, stated as such because the paper gives no total for it:** the four
additional language- and duration-model training corpora sum to **173 + 160 + 291 + 29 = 653 songs**.
The paper prints no total for these, so this is arithmetic over its components and not a check of any
figure it states.

### §6.2 ★ FIGURE 6's DURATION-MODEL AXIS DISAGREES WITH TABLE 2 AT ONE OF ITS THREE TICKS

Figure 6's bottom plot places its three duration models on a *"Duration Model Log-P"* axis whose tick
values are printed. Table 2 gives the same three models' log-probabilities. Set side by side, as
magnitudes, since the axis is printed unsigned:

| Model | Table 2 | Figure 6's printed tick | Agree? |
|---|---|---|---|
| Neg. Binomial | −3.946 | 3.946 | **yes** |
| GRU-16 | −2.868 | **2.979** | **NO — differs by 0.111** |
| GRU-256 | −2.014 | 2.014 | **yes** |

**Two of the three reproduce exactly; the middle one does not.** No value of Table 2 moves and no
result of the paper moves with it — the figure's purpose is to show a trend, and the trend's direction
is unaffected by 0.111 on one abscissa.

**★ WHAT WAS DONE TO SEPARATE THIS FROM A MISREADING OF THE PAGE, STATED AS ACTS RATHER THAN AS
CONFIDENCE.** Two things, and neither is an argument from likelihood. **First, the tick was re-read at a
SECOND, SEPARATE opening of page 6, and Table 2 was re-read at a second, separate opening of page 5**;
both came back as first read. §8.1 records those acts. **Second, the same figure's other axis is a
control that this read did not choose after the fact**: the top plot's four printed ticks reproduce
Table 1 exactly (§6.3), so of the seven ticks the two axes carry, six reproduce their own table and one
does not.

**What this read does NOT claim about it:** that a misreading is impossible, or that the odds favour one
explanation over another. What is established is that the two numbers were each read twice, at separate
openings, and disagree.

**What this read does NOT claim:** which of the two numbers is the correct one. The paper prints both and
reconciles neither, and nothing in the paper says which was computed from which.

### §6.3 Figure 6's language-model axis reproduces Table 1 at all four ticks

| Model | Table 1 | Figure 6's printed tick | Agree? |
|---|---|---|---|
| 2-Gram | −2.393 | 2.393 | yes |
| 4-Gram | −1.887 | 1.887 | yes |
| GRU-32 | −1.576 | 1.576 | yes |
| GRU-512 | −1.293 | 1.293 | yes |

Four of four.

### §6.4 Table 3's differences, computed

| Axis | Standard model | Best model | Difference |
|---|---|---|---|
| Root | 0.812 | 0.821 | **+0.009** |
| Maj/Min (WCSR) | 0.795 | 0.805 | **+0.010** |
| Seg. | 0.804 | 0.814 | **+0.010** |

**So the whole gain the paper reports for replacing a 2-gram language model and a negative binomial
duration model with two GRUs is one percentage point on the headline measure, and nine tenths of one on
root.** The paper's own word for this is *"modest"*, and its claim about the difference is consistency
rather than size.

### §6.5 The frame rate, and the 200-time-step excerpt — an internal check that PASSES

The paper states a sample rate of 44 100 Hz and an STFT hop size of 4410 samples. **4410 / 44 100 = 0.1
seconds per frame, i.e. ten frames per second.** Against that:

- §4.3 states that sequences were *"cut in excerpts of 200 time steps (20 s)"*. **200 × 0.1 s = 20 s** —
  the paper's own parenthesis reproduces exactly.
- §3.1's *"1.5 s patch"* of spectrogram is therefore **15 frames** wide.

Two independently stated quantities of the paper constrain each other here, and they agree. *(§6.6 and
§6.11 are two further checks of the same kind. This read does not claim to have enumerated every
constraint of this sort the paper contains — it ran the ones its transcription happened to make
available.)*

### §6.6 The chord alphabet — an internal check that PASSES

*"25 classes: 12 root notes × {major, minor} and the 'no-chord' class."* **12 × 2 = 24; 24 + 1 = 25.**
Reproduces. It is also consistent with §3.1's final layer — *"a linear convolution with 25 1×1
filters"*.

### §6.7 The two grid searches, sized from the paper's own stated sets

**The language-model search**, as §4.2 states its axes: 3 layer counts × 2 unit counts × 2 unit types ×
4 embeddings × 2 learning rates × 2 skip-connection settings = **192 configurations**. The paper states
no count, and footnote 7 says the complete results cannot be presented.

**The duration-model search**, as §4.3 states its axes: 5 unit counts for the GRU + 5 for the LSTM + 3
for the vanilla RNN, at one recurrent layer = **13 configurations**. The paper states no count.

**★ AND TWO OF THE PAPER'S OWN REPORTED MODELS SIT OUTSIDE WHAT THOSE SETS CONTAIN OR REPORT.**

- **GRU-32, one of the four models in Table 1, is not in the language-model search space.** That search
  covers unit counts {256, 512}; 32 is not among them. The paper does not present it as a search result
  — it calls it *"a smaller, but otherwise identical RNN with 32 units"*, so it is a deliberate extra
  arm. **But a reader reconstructing §4.2's search would not produce it**, and the paper does not say so.
- **GRU-128, the model Figure 5 is drawn from, is in the duration search space but in NO table.** Table 2
  reports GRU-256 and GRU-16; Table 3 and Figure 6 use GRU-256, GRU-16 and the negative binomial.
  **GRU-128's log-probability is stated nowhere in the pages as read.** This matters because §4.3's
  mechanism argument — the
  paper's explanation of *"the reason why the GRU performs so much better than the baselines"* — is made
  entirely at GRU-128. See §7.1.

### §6.8 The label prior is inert under the paper's own assumption

Equation 1's factorisation carries the factor ∏_t [ 1 / P(y_t) ]. The paper assumes P(y_t) uniform. **A
uniform prior makes that factor a constant — the same for every candidate label sequence — so it cannot
change the argmax of Equation 1.** Under the paper's own stated assumption the term is therefore inert
for decoding.

**This is not a defect and is not reported as one.** The factor is written because the factorisation is
general; it becomes load-bearing the moment a non-uniform label prior is used, and a design adopting this
framework with a non-uniform prior inherits a term the experiments reported in the pages as read never
exercise.

### §6.9 One quantity the paper does not print, derived here and flagged as derived

The paper states 24 filters per octave between 65 Hz and 2100 Hz; the pages as read state no count of
frequency bins. **2100 / 65 = 32.31, and log₂(32.31) = 5.01 octaves, so 24 × 5.01 ≈ 120 bins.** This is
**this read's arithmetic and not a value the paper states**, and it is recorded only so that a later
reader knows the quantity is absent rather than overlooked.

### §6.10 How many integrated combinations were run, and how many were tabulated

§4.4 names its arms: *"For language modelling, these are the GRU-512, GRU-32, 4-gram, and 2-gram models;
for duration modelling, these are the GRU-256, GRU-16, and negative binomial models."* **4 × 3 = 12
combinations**, plus the exact-decoding arm, which §4.4 scopes to *"the n-gram language models in
combination with the negative binomial duration distribution"* — **2 more**, for **14 measured
configurations**.

**Table 3 tabulates two of them.** The other twelve appear as plotted points in Figure 6, whose markers
carry no printed values. **So twelve of the paper's fourteen integrated measurements are published as
positions on a curve and, in the pages as read, as numbers nowhere.**

### §6.11 The chord embedding's own description closes on itself — an internal check that PASSES

§4.2 reports *"three clusters"* in the learned embedding, and that within a cluster *"the distance
between the roots are minor thirds (e.g. C, E♭, F♯, A)"*. **A cycle of minor thirds closes after four
roots** — C, E♭, F♯, A is the paper's own example and returns to C — **so three such clusters account for
3 × 4 = 12 roots, which is exactly the root count of the 25-class alphabet.** Figure 4's caption is
consistent with this: *"If projected into 3D (not shown here), the chord clusters split into a lower and
upper half of four chords each"* — four major and four minor per cluster, 3 × 8 = 24 triads, plus the
no-chord class at the centre = 25.

**This is the paper's own description reproducing exactly, and it is recorded because §4.2 offers these
observations without arithmetic and a later reader may wonder whether they cover the alphabet. They do.**

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

**(1) The compound corpus totals do not reproduce from the paper's own components — two figures in one
sentence.** §6.1. No result moves; what is lost is a later reader's ability to reconstruct the evaluation
set.

**(2) Figure 6's duration-model axis contradicts Table 2 at GRU-16.** §6.2. Two of three ticks reproduce;
one differs by 0.111. The same figure's other axis reproduces its table at four ticks of four.

**(3) ★ THE PAPER'S MECHANISM ARGUMENT IS MADE AT A MODEL IT SCORES IN NO TABLE.**
§4.3 opens its explanation with *"Figure 5 shows the reason why the GRU performs so much better than the
baselines: as a dynamic model, it can adapt to the harmonic rhythm of a piece, while static models are not
capable of doing so."* The GRU it then describes — the one that *"reliably remembers the period over large
gaps"* — **is GRU-128**, named in the text and in the figure's legend. **GRU-128 appears in none of the
paper's three tables**: Table 2 scores GRU-256, GRU-16, the negative binomial and the exponential, and
§4.4 states that the duration models carried into the integrated experiment *"are the GRU-256, GRU-16,
and negative binomial models"*. So the qualitative evidence for *why* the GRU duration model works is
drawn from one configuration, and the quantitative evidence that it works is drawn from two others.
**Neither is wrong; they are simply not the same model**, and the pages as read do not remark on it.

*(What is NOT claimed: that GRU-128 behaves differently from GRU-256 or GRU-16. The paper gives no
evidence either way, which is the point. §4.3 does separately show GRU-16 in Figure 5 and describes it as
adapting but more noisily, so the figure carries two of the three sizes.)*

**(4) ★ THE JUSTIFICATION FOR THE ONE-PARAMETRISATION-PER-CHORD SIMPLIFICATION IS ABOUT HMMs AND IS
APPLIED TO A MODEL THAT IS NOT AN HMM.** The paper writes: *"We assume a single parametrisation for each
chord; this ostensible simplification is justified, because simple temporal models such as HMMs do not
profit from chord information, as shown by [4,7]."* **The model whose simplification is being justified is
an RNN duration model, not an HMM**, and the paper's own §2.3 says in terms that the framework ADMITS
chord-conditioned durations and that exploring them is *"left for future work"*. So the cited evidence
establishes something about the class of models the paper is arguing against, and is used to license an
assumption inside the class it is arguing for. **No value moves**, and the assumption may well be
harmless — but the paper's stated ground for it does not reach the case.

**(5) The linearity claim is asserted over four points and three points, with no fit and no uncertainty.**
Claim 7 — *"the WCSR increases linearly with higher log-probability of each model"* — is read off Figure 6.
The paper reports no fitted line, no correlation coefficient and no residual. Claim 8 then extrapolates
beyond the plotted range: *"As this relationship does not seem to flatten out, further improvement of each
model type can still increase the score."*

**(6) No value in any of the three tables carries a spread, a standard deviation or an interval.** The
paper's only uncertainty statement anywhere in the pages as read is the paired-t-test bound *"p < 2.487 ×
10⁻²³ for all differences"*, which is stated for Table 3's three differences and for nothing else. Tables
1 and 2 carry no uncertainty at all, and the evaluation is 4-fold cross-validation, so per-fold spread
exists and is not reported.

**(7) An observation about two adjacent numbers, reported rather than explained.** §4.3 states that the
duration models were trained with *"a learning rate linearly decreasing from 0.001 to 0"* and, one
sentence later, that *"We also applied gradient clipping at a value of 0.001"*. **The two values are
numerically identical**, and the paper states no relation between them. This read makes **no claim that
either is wrong** — it records the coincidence because a reader reproducing the setup would want to
confirm both at the source.

**(8) The WCSR definition as printed is about whole segments.** *"t_c is the total duration of chord
segments that have been recognised correctly"*. Read literally, that credits the duration of segments
recognised correctly rather than the duration over which the label is correct. **The paper delegates the
definition to [30]**, which this read did not open, so the authoritative form lives there. Recorded as a
wording observation, bounded to the sentence as printed.

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered

- **★ THE APPROXIMATION COST IS BOUNDED ONLY FOR THE ARM THAT EXCLUDES THE HEADLINE MODEL.** The paper's
  Claim 9 — that approximate beam search *"does not impair the result by much compared to exact
  decoding"* — rests on the exact-decoding arm, and §4.4 states exactly which combinations that arm covers:
  *"we evaluate exact decoding results for the n-gram language models in combination with the negative
  binomial duration distribution."* **The best model is GRU-512 with GRU-256, and it has no exact arm** —
  by the paper's own argument at §3.4 it cannot have one, because dynamic models *"prohibit the use of
  dynamic programming approaches for efficient decoding"*. **So nothing in the pages as read bounds what
  the approximation costs the configuration the headline result is taken from.** A design that adopted
  this decode would inherit that gap; this read makes no claim about how large it is, and ranks it
  against nothing else in this list.
- **No per-corpus breakdown of any figure.** Tables 1, 2 and 3 carry one column set each and no corpus
  axis at all. Which of the four evaluation corpora moved, and by how much, is not recoverable from the
  pages as read.
- **No per-fold results.** The protocol is 4-fold cross-validation and only the aggregate is reported.
- **No count of chord segments, chord changes or frames** in either the evaluation or the additional
  training data. The data are sized in songs and hours only.
- **No grid-search results.** Footnote 7 states they cannot be presented for reasons of space.
- **No definition, in this paper, of the segmentation measure or of root accuracy.** Both are named and
  cited out.
- **No GRU-128 log-probability**, although it is the model the mechanism argument is made at (§7.1(3)).
- **No timing, memory or complexity figure** for the hashed beam search, and no sensitivity analysis over
  N_b, N_s or N_h; the three values are said to come from *"a small number of preliminary experiments"*.
- **No chord-conditioned duration model.** Defined, declared future work, not built, not measured.
- **★ NO MAXIMUM SEGMENT LENGTH — A PRECISION ADOPTED FROM THE FIRST EXTRACT AT THE CROSS-CHECK AND
  MARKED HERE.** That file's coupling facts state: *"The candidate boundary set is every frame edge; no
  maximum segment length is stated anywhere in the held document."* **This read transcribed the frame
  grid and the change/stay formulation without noticing that the formulation implies no length cap and
  that the paper states none.** Restated at this read's own width: **no maximum segment length appears in
  the pages as read.** It matters for a design that would adopt the term, because a per-step change
  probability places no upper bound on a segment and the paper neither imposes one nor measures what
  happens without one.

### §7.3 What is both measured and structural here, for a design that would adopt this formalism

- **★ THE PART THAT CARRIES WITHOUT THE AUDIO IS THE FACTORISATION, NOT THE NETWORKS.** Equation 2 splits
  the temporal model into *when does the chord change* (`P_D`, evaluated once per analysis step) and
  *which chord comes next* (`P_L`, evaluated once per chord), joined by a lattice in which a change costs
  one factor from each and a non-change costs one factor from `P_D` alone. **Equation 2 and the two
  definitions it rests on name no audio quantity** — they are stated over `y_t`, `s_t` and `C(·)` alone,
  and an audio frame enters only through `P_A`, which is a separate factor of Equation 1. Its measured
  support is Table 3: one percentage point of WCSR, and nine tenths on root, over the combination an HMM
  implicitly gives.
- **★ AND THE DURATION MODEL IS A PER-STEP CHANGE PROBABILITY, NOT A DISTRIBUTION OVER SEGMENT LENGTHS —
  A DISTINCTION A DESIGN MUST NOT COLLAPSE.** `P_D(s_t | s_{1:t−1})` answers *"does the chord change at
  this step, given the changes so far"*. A segment-length distribution is what that induces, not what it
  is. The paper's own baselines make the difference visible: the exponential and negative binomial
  baselines ARE length distributions, and the paper's argument against them is precisely that a length
  distribution cannot condition on where the piece is. **A design that reads this paper as supplying a
  segment-length prior would be adopting the baseline rather than the contribution.**
- **★ THE COMPRESSION MAPPING HAS A STRUCTURAL COST THE PAPER DOES NOT DISCUSS.** `C(·)` *"removes all
  consecutive duplicates of a chord"*, and the paper's own worked example is `C((C,C,F,F,G)) = (C,F,G)`.
  **A chord that is genuinely restated — the same chord beginning a new segment immediately after itself —
  is therefore not representable in the language model's input at all**, because it is indistinguishable
  from the same chord continuing. For an audio system over a 25-class alphabet this is nearly costless. For
  a symbolic analysis in which a repeated harmony across a boundary is a real event, it is a structural
  limit that arrives with the formalism, and it is inherited silently unless it is named.

  *(Bound: the paper states the mapping and its example and says nothing about this consequence. That the
  consequence follows is this read's own reading of the definition, not a claim the paper makes.)*
- **The hash function is the reusable decode idea.** Hashing a beam solution on *the last N_h chord symbols
  regardless of their timing* is what stops a beam from filling with the same chord sequence at slightly
  different times. It is stated in three lines and is independent of everything else in the paper.
- **The uniform label prior is inert here and would not be elsewhere.** §6.8.
- **★ AND THE EVIDENCE DOES NOT REACH THIS PROJECT'S REPERTOIRE OR ITS INPUT.** Every measured value in
  the pages as read is audio, popular music, and a 25-class major/minor alphabet. **Those pages carry no
  symbolic claim, no classical or Baroque claim, and no claim about any richer chord vocabulary.** Any
  carry into a symbolic Baroque setting is the record's own inference, and this read takes no position on
  whether the record makes it.

### §7.4 What this paper's reference list gives the record, checked at the candidacy file

This check was run deliberately, on the previous sitting's finding that a paper's reference list is worth
reading against `reading_pass/candidacy_upgrades.md`. **The bound is stated first: it was a pattern search
of that file for a named set of author surnames drawn from this paper's reference list, not a whole read
of it.** A candidacy row whose entry does not carry one of the surnames searched for would not appear.

- **★ REFERENCE [26] IS A SLICE ROW THE RECORD CALLS ADMITTED AND NOT HELD, AND THIS PAPER CARRIES ITS
  FULL BIBLIOGRAPHIC RECORD.** This paper prints: *"M. Mauch and S. Dixon. Simultaneous Estimation of
  Chords and Musical Context From Audio. IEEE Transactions on Audio, Speech, and Language Processing,
  18(6):1280–1289, August 2010."* `candidacy_upgrades.md` **row 44** reads *"Mauch & Dixon, TASLP 18(6)
  2010, simultaneous estimation of chords and musical context"*, **ADMITTED**, with the note *"Not held
  (the register records the author copy as image-only)."* **The volume, issue, year and journal agree; what
  this paper adds is the page range 1280–1289 and the month.** It does not make the row readable and
  nothing is proposed — it is recorded because a row the record cannot read is one whose identity is worth
  having pinned from a second source.
- **Reference [11] is candidacy row 60.** This paper prints *"Trevor de Clercq and David Temperley. A
  corpus analysis of rock harmony. Popular Music, 30(01):47–70, January 2011."* Row 60 reads *"de Clercq &
  Temperley, Popular Music 30(1) 2011, a corpus analysis of rock harmony"*, **NOT ADMITTED**. The two
  agree; nothing follows.
- **★ THE EVIDENCE FOR THE PAPER'S LANGUAGE-MODEL CHOICE IS DELEGATED TO A WORK THE CANDIDACY FILE DOES
  NOT CARRY.** Stated exactly: the paper DOES give this model's hyper-parameter search, its selected
  configuration and its measured log-probability. What it delegates is the ground for choosing an RNN at
  all, and the model's own details. §3.2
  says *"As shown in [21], RNN-based models perform better than n-gram models at this task. We thus adopt
  this approach, and refer the reader to [21] for details."* Reference [21] is *"Filip Korzeniowski, David
  R. W. Sears, and Gerhard Widmer. A Large-Scale Study of Language Models for Chord Prediction. In 2018
  IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Calgary, Canada, April
  2018."* **The search this read ran returned no candidacy row for it.** Two further works of the same
  authors carry load in this paper and likewise returned no row: **[24]**, *"On the Futility of Learning
  Complex Frame-Level Language Models for Chord Recognition"* (AES Semantic Audio, Erlangen, June 2017),
  which is the cited evidence for the paper's central diagnostic claim, and **[25]**, *"Automatic Chord
  Recognition with Higher-Order Harmonic Language Modelling"* (EUSIPCO 2018), cited as the ground for using
  n-grams in a higher-order HMM.
- **What follows, stated narrowly.** A design that took this paper's *reason for using an RNN language
  model* as evidence would be resting on [21], which this paper does not reproduce and the record — on the
  search this read ran — does not hold. **The duration-model half is argued and measured inside this
  paper; the language-model half leans outward.** Nothing is proposed, and no verdict is moved.
- **What the search returned, counted.** Of this paper's thirty-three references, the search matched **two
  entries of `candidacy_upgrades.md`: row 44, which is a member of the slice (ADMITTED, not held), and row
  60, which is NOT ADMITTED and so is not a slice member.** So this paper's reference list puts **one
  slice row** inside its own citations. *(The previous member's entry records three slice rows inside its
  reference list; that figure is a relay from that entry and was not checked at its extract here.)*

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

**The read-back re-opened all eight pages, after §0 to §7 were written and before anything was landed.**
Named rather than counted: page 6 alone; then page 5 alone; then page 4 alone; then pages 1 to 3 in one
request; then pages 7 and 8 in one request.

**Every page of this paper has therefore had two passes, and three of them have had the second pass
singly** — pages 4, 5 and 6, which are the three that carry every value this file transcribes. **So no
claim in this file rests on a page read once.**

**Every page image was checked for presence and legibility at the image itself, not at the call's
success line.** One further request — the deliberately out-of-range one that established the page count —
returned the refusal it was made for and no image. **None of this is evidence the page-image fault is
gone.**

**Why pages 6 and 5 were re-opened first and singly.** The disagreement at §6.2 sits between Figure 6
(page 6) and Table 2 (page 5). Each was re-read at its own separate opening, so the two numbers were
established at four page openings in total rather than at one. **Both came back exactly as first read:
Figure 6's duration axis at 3.946, 2.979, 2.014; Table 2's GRU-16 at −2.868.**

### §8.2 What the read-back and the sweep struck in this side's own writing

**Named rather than counted. Everything below was struck BEFORE this file landed at all**, and the two
of them that are degradation tells are also at §8.3.

**The read-back struck:**

- **A citation marker dropped from inside a quotation.** §2.5 quoted the paper's over-confidence sentence
  as ending *"…could over-rule the predictions of a temporal model."* **The paper prints *"…of a temporal
  model [9]."*** Restored. **This is precisely the class of defect this line has been reporting against
  first extracts**, and it was in this read's own text.
- **A statement of what the paper delegates, wider than the fact.** §7.4 said the paper's language model
  was *"delegated whole"* to [21]. **It is not:** the paper gives that model's grid search, its selected
  configuration and its measured log-probability. What it delegates is the ground for choosing an RNN and
  the model's own details. Corrected to say exactly that.
- **A miscount of this read's own search result** — §7.4 said the reference list put *"two slice rows"*
  inside this paper's citations. **Row 60 is NOT ADMITTED and is therefore not a slice member; the count
  is one.** See §8.3, instance (iii).
- **An incomplete statement of Table 2's own contents.** §7.1(3) said *"Table 2 scores GRU-256 and
  GRU-16"*. **Table 2 scores four models** — those two, the negative binomial and the exponential. The
  sentence is now stated at the table's actual width, and the claim it supports (that GRU-128 is in none
  of the three tables) is unaffected.

**The sweep struck** — run over §0 to §7 for absolutes, every hit read at its own line:

- **An argument from likelihood standing where a statement of acts belonged.** §6.2 read *"A reading
  error would not be expected to land on exactly the one tick of seven that fails."* **That is a claim
  about odds, and this read derived no odds.** Replaced by what was actually done — two separate page
  openings for each of the two numbers — and by an explicit statement of what is not claimed.
- **Four absolutes about the paper stated wider than the act that produced them**, each now bounded to
  *the pages as read*: that nothing in the paper admits a non-audio input; that the paper makes no claim
  about untested repertoire; that nothing in the paper bounds the approximation cost; and that GRU-128's
  log-probability is stated nowhere.
- **An unbounded negative about the paper's structure** — §7.3's *"That structure does not mention audio
  anywhere"* — replaced by a statement of what Equation 2 and its two definitions actually name, and where
  audio does enter.
- **A claim about the whole paper where only the transcribed values were checked** — §6.1's *"Nothing else
  in the paper depends on either total"*. Now stated over the values §5 transcribes, with the narrowing
  said out loud.
- **An inference presented as an observation** — §7.2's *"Every value in Tables 1, 2 and 3 is over the
  compound dataset"*. **The paper does not state that**; the three tables simply carry no corpus axis.
  Replaced by the checkable statement.
- **An assertion of uniqueness over a class this read never enumerated**, twice: §6.5's *"the one place
  where two independently stated quantities of the paper constrain each other"*, and §6.1's *"the one
  explanation the sentence itself suggests"*. See §8.3, instances (ii) and (iv).
- **A ranking of this read's own findings against one another** — §7.2's *"the gap of this paper most
  likely to matter to a design that would adopt the decode"*. See §8.3, instance (i).
- **A consequence of the paper's own definition presented without saying whose reading it is** — §7.3's
  point about the compression mapping and restated chords. A bound was added naming it as this read's
  reading of the definition rather than a claim the paper makes.
- **One heading softened from a claim of uniqueness to a claim of fact** — §7.3's *"THE TRANSFERABLE
  OBJECT IS THE FACTORISATION"*, which asserts that nothing else transfers, a thing this read did not
  establish.

### §8.3 The degradation tells, reported unprompted

The user's standing rule of 2026-08-15 asks this side to recognise its own degradation and say so
unprompted. **Two of his named tells fired in this sitting's writing.**

**TELL A — a count, a proportion or a ranking put on this side's own reading or its own findings without
deriving it. Its instances are NAMED and deliberately not totalled here**, because the three entries
before this one each record that every total they put on their own tells went stale at the next pass.

**★ AND THIS LIST IS NOT THE WHOLE OF THEM — §10 CARRIES A LATER ONE, AND THE POINTER IS WRITTEN HERE
BECAUSE A TELL TALLY IS WHERE A HURRIED READER TAKES THE COUNT FROM.** The four named below were caught
before this file's first landing; **§10 records a fifth, found in §9.4 by a sweep run after this file had
landed twice**, in the section written to report the cross-check. **Read §8.3 and §10 together, never
§8.3 alone.**

- *(i)* **§7.2's *"the gap of this paper most likely to matter to a design that would adopt the
  decode"*** — **a ranking of this read's own findings against one another, on nothing.** Caught at the
  sweep, before this file landed.
- *(ii)* **§6.5's *"the one place where two independently stated quantities of the paper constrain each
  other"*** — **refuted by two later sections of this same file**, §6.6 and §6.11, each of which is a
  check of exactly that kind. Caught at the sweep.
- *(iii)* **§7.4's *"two slice rows"*** — a count of this read's own search result, where one of the two
  rows the search returned is NOT ADMITTED and so is not a slice member. Caught at the read-back.
- *(iv)* **§6.1's *"the one explanation the sentence itself suggests"*** — a uniqueness claim over the set
  of possible explanations, which this read did not enumerate. Caught at the sweep.

**TELL B — citing a summary instead of the source, and an unmarked relay presented as established. Its
instances are in the CONVERSATION and not in this file**, and they are recorded here because the three
entries before this one each record a defect that lived in a message and in no landed file.

- **The capacity judgment sent to the user before the paper was opened gave the recent members' page
  counts as *"six, six, nine, twelve, nineteen and eight"*.** Of those six values, **this side read four
  at their own entries' texts** — six at the hundred-and-sixty-ninth, nineteen at the
  hundred-and-seventy-fifth, eight at the hundred-and-seventy-sixth and eight at the
  hundred-and-seventy-seventh. **The remaining values are a relay through the hundred-and-seventy-sixth's
  own sentence, and the message did not say so.** **This is the same defect the hundred-and-seventy-seventh
  records at its own (xiii)**, in a message of the same kind, and this side made it having read that
  record.
- **The same message said the two previous sittings *"each recorded that eight pages 'was not close'"*.**
  **One of them printed those words** — the hundred-and-seventy-seventh. The hundred-and-seventy-sixth
  printed *"was not in doubt"*. **A quotation attributed to two entries where one carries it.**

**★ WHAT THE THRESHOLD MEANS HERE, STATED PLAINLY AND WITHOUT INFLATION.** The user's rule is that when
two or more of the named tells appear, this side reports it and recommends handover at a verified stop.
**TWO named tells fired — the count-and-ranking one, four times in this file, and the
summary-instead-of-source one, twice in the conversation's messages — and this side claims nothing more
than that.** It does not claim that other tells fired, and it does not rank these two against each other.
**That every instance was caught by a pass of this side's own, before this file landed, does NOT lower
the count**: the four entries before this one each record that it does not.

**The recommendation is handover at this member's boundary**, once the member is complete through the
eight-step procedure and both files are landed and proved. It is not a recommendation that work be
abandoned mid-thing.

### §8.4 The bound on this section

**THE SWEEP RAN OVER §0 TO §7 AND THEN, DELIBERATELY, OVER §8 AS WELL.** The hundred-and-seventy-seventh
records as a structural finding that a sweep run at step 4 cannot reach the sections written at step 5 —
so the sections in which a file reports its own checking are precisely the ones no sweep has passed over.
**This sitting read that finding at that entry's own text and acted on it: §8 was swept after it was
written**, and the one thing that sweep struck inside §8 was a sentence calling instance (i) *the
sharpest of the four*, which is Tell A's own shape inside the section reporting Tell A. It is struck, and
the four instances are named without being ranked.

**WHAT THIS SECTION DOES NOT ESTABLISH.** That this file is clean. Every pass recorded here is a further
pass over the same writing by the same side. **The read-back caught defects the writing did not, and the
sweep caught defects the read-back did not, and §8's own sweep caught one more** — which is evidence that
each pass finds something, not evidence that the next would come back empty.

**AND THE CROSS-CHECK HAD NOT YET RUN WHEN THIS SECTION WAS WRITTEN.** §0 to §8 were written and landed
without the first extract being opened. What the cross-check found is at §9, written in the act that ran
it.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**The first extract was opened for the first time AFTER §0 to §8 had been written and landed**, at step 7
of the eight-step procedure. It was read **whole**, at a bridge-staged copy, **46,899 bytes**, which is
the size the listing of `reading_pass/extracts/` reported before it was staged.

**Every disagreement below was resolved AT THE PAPER**, not by preferring one text to the other. **Pages
1, 2 and 3 were re-opened a third time for that purpose** — page 3 singly — and page 4's two contested
strings were re-read at the read-back's own opening of that page.

### §9.2 Every value TAKEN FROM THE PAPER that both extracts transcribed agrees, digit for digit

**All three of the paper's tables, in full and in both files:** Table 1's four values, Table 2's four,
Table 3's six — **fourteen values, no disagreement.**

**Three differences both files derived independently from Table 3's cells, and both got the same:**
+0.009 root, +0.010 maj/min, +0.010 segmentation.

**One further quantity both files derived independently from the same two printed numbers, and both got
the same:** that a hop of 4410 samples at 44 100 Hz is one frame per 0.1 s. The first extract marks it
*"(Derived, this extract's arithmetic …)"*; this read carries it at §6.5 with the 200-time-step check
built on it.

**Every corpus figure:** 180, 19, 18 and 10:21; 100 and 6:46; 65 and 4:30; 742 and 44:42; the stated
compound 1125 and 66:21; and the four additional corpora at 173, 160, 291 and 29. **No disagreement.**

**Every protocol value:** β = 0.9, τ = 1.3; 44 100 Hz, frame size 8192, hop 4410, 24 filters per octave,
65 Hz to 2100 Hz, the 1.5 s patch; both grid-search axis sets in full; 100 epochs, mini-batches of 4 and
of 10, the 200-time-step excerpts, gradient clipping 0.001, the acoustic model's 300 epochs, 200 updates
and mini-batch of 512; N_b = 25, N_s = 4, N_h = 5; the t-test bound p < 2.487 × 10⁻²³; 25 classes.
**No disagreement.**

**The held file's size:** 384,606 bytes in both.

**★ AND BOTH READS INDEPENDENTLY REACH THE SAME IDENTITY FINDING, WHICH IS THAT THERE IS NONE.** Both
establish the printed title, both authors, the affiliation, the ISMIR running header, the printed page
range 10–17 and the CC BY 4.0 licence line at page 1, and both find them matching what the record's row
carries.

**★ AND BOTH READS INDEPENDENTLY IDENTIFY THE SAME TWO REFERENCES AGAINST THE CANDIDACY FILE.** The first
extract names reference [26] as *"(candidacy row 44, unheld)"* and reference [11] as *"candidacy row 60"*.
**This read reached both by a targeted search of `candidacy_upgrades.md` without having opened the first
extract** (§7.4). The two reads agree on both.

**★ THE BOUND ON THIS AGREEMENT, STATED BECAUSE IT DOES NOT REACH THE WHOLE OF THE FIRST EXTRACT.** That
file carries a large body of statements that point **INTO this project's record** — `FRAMEWORK.md` at the
L2 and L3 charters and at DP-B to DP-H, the findings surface's DP-C block, `population.md`'s §3
verification table, the bibliography's line 34, the slice derivation's line 67, the progress record, both
commissions, the rows 11 and 19 extracts, and the classification of this paper's duration model against
row 11's own test. **This read opened NONE of those objects** (the one exception is the candidacy file,
at row 20's line and at a targeted search). **So on that half this is not a second opinion but silence**,
and the digit-for-digit agreement above must not be read as reaching it. **This read takes no position on
this paper's CENTRAL verdict**, which is the first extract's own and is challengeable where that file
says.

### §9.3 The disagreements, named rather than counted, and the directions are not symmetrical

**FIVE go against the first extract and THREE go against this read. None moves a value.**

**★ AGAINST THE FIRST EXTRACT.**

**(a) ★ ONE WORD SUBSTITUTED INSIDE A QUOTATION, AND IT IS THE ONE OF THE FIVE WHOSE SUBSTITUTE MEANS
SOMETHING DIFFERENT.** The first extract quotes §3.3's justification for choosing recurrent networks as
*"have shown great potential in **processing** periodic signals [1]"*. **The paper prints *"predicting
periodic signals"***, established at page 3 at this read's whole read, at its read-back and again at a
third opening at the cross-check. **Why it matters:** the model being justified is a **next-step
predictor** — the paper's own sentence three lines later sets up *"a next-step-prediction task"* — so
*predicting* is the capability the citation is offered for, and *processing* is a weaker and different
claim that does not support the choice. The cited work, [1], is a beat-tracking paper, which is
prediction of a periodic quantity. **No value moves.**

**(b) A WORD INSERTED INSIDE A QUOTATION, IN TWO PLACES.** The first extract quotes §2's
non-decodability sentence as *"because each y_t depends on all **its** predecessors"*, at two of its own
places. **The paper prints *"depends on all predecessors"***, established at page 2 twice. **No value
moves and the sense does not change.**

**(c) A WORD INSERTED INSIDE A QUOTATION.** The same passage is quoted as *"or **use** approximate
inference methods for other models"*. **The paper prints *"or approximate inference methods for other
models"***. **No value moves and the sense does not change.**

**(d) A CLAUSE INSERTED AT THE HEAD OF A QUOTATION.** The first extract quotes §3.2 as *"**In our case,**
the inputs z_k are the chord symbols given by 𝒞(y_{1:T})."* **The paper's sentence is *"Figure 3 shows an
RNN in a general next-step prediction task, the inputs z_k are the chord symbols given by C(y_{1:T})."***
The phrase *"In our case,"* is printed in the paper, but in a different sentence on the following page.
**No value moves and the sense does not change.**

**(e) A WORD INSERTED INSIDE A QUOTATION OF THE CORPUS SENTENCE.** The first extract quotes *"65 songs by
Robbie Williams, 4:30 **hours** of audio"*. **The paper prints *"4:30 of audio"***, the only one of its
four corpus entries that omits the word. **No value moves**, and the inserted word is true of the figure.

**★ AGAINST THIS READ — AND ALL THREE WERE EXPOSED BY THE FIRST EXTRACT HAVING THE TEXT RIGHT.**

**(f) A WORD SUBSTITUTED INSIDE A QUOTATION.** This read wrote §1's diagnosis as *"the low hierarchical
level they are applied **to**"*. **The paper prints *"applied on"***. Corrected at its site with the
former wording preserved (§2.1).

**(g) A SUBSCRIPT CHANGED INSIDE A QUOTATION.** This read wrote §3.2's sentence with *"C(y_{1:**t**})"*.
**The paper prints a capital T there**, established at a third opening of page 3. The lower-case form is
correct at two other places in the paper, and this read transcribed both of those correctly; it carried
the lower-case form into the one sentence that does not take it. Corrected at its site with the former
wording preserved (§2.6).

**(h) A HYPHEN DROPPED FROM INSIDE A QUOTATION, AT TWO SITES.** This read wrote the chord-vocabulary
sentence as *"the '**no chord**' class"*. **The paper prints *'no-chord'***. Corrected at both sites with
the former wording preserved (§5.1, §6.6).

**★ WHAT THIS SAYS ABOUT BOTH FILES.** **Three of this read's own quotation defects survived the writing,
the read-back and the sweep, and were caught only because a second reader had the same sentences right.**
That is the doubling doing exactly the thing it exists for, and it is recorded here rather than softened.
**It is also the same shape this line has reported against first extracts at other rows**, now found in
this read's own text — so the five items at (a) to (e) are not offered as a one-sided ledger. *(No count
of those other rows is asserted here; the handoff line carries them and this read did not re-derive
them.)*

**THE FIVE AGAINST THE FIRST EXTRACT ARE NOT CORRECTED AND THAT FILE IS UNTOUCHED.** The standing ground
is this line's own: rewriting another read's text destroys what the doubling is comparing. **They stand
with the user.**

### §9.4 What the doubling produced that neither read had alone, in both directions

**★ ONE RESULT OF THE CROSS-CHECK IS A CONFIRMATION RATHER THAN A DISAGREEMENT: BOTH READS INDEPENDENTLY
FOUND THE FIGURE 6 ANOMALY, AND ONLY ONE OF THEM COULD READ THE VALUE.** The first extract records: *"One
cell flagged rather than transcribed: the middle tick label of Figure 6's lower x-axis (the duration-model
log-probability axis) reads at the image as a value that does not match Table 2's GRU-16 entry (−2.868);
it could not be read with certainty and is recorded as a flag."* **This read reached the same place
independently and read the tick as 2.979, at two separate openings of page 6, with Table 2 re-read at two
separate openings of page 5** (§6.2, §8.1).

**So the doubling turns a flag into a finding.** Two readers, reading independently, both saw that the
axis and the table disagree; one could not resolve the value and said so, and the other resolved it. **The
first extract's caution is vindicated rather than contradicted** — it declined to transcribe a value it
could not read, which is the right act — and **this read's value is what the flag was waiting for.**

**★ WHAT THE FIRST EXTRACT HOLDS THAT THIS READ DOES NOT**, besides the whole record-side half at §9.2's
bound: **two precisions, both adopted into this file at the cross-check and marked at their sites** — that
**no maximum segment length is stated** (adopted at §7.2), and that **no exact normaliser exists, so the
model could not publish a posterior even in principle** (adopted at §3.2). It also carries a
classification of this paper's duration model against row 11's own test, which rests on an extract this
read did not open and on which this read therefore takes no position.

**★ WHAT THIS READ HOLDS THAT THE FIRST DOES NOT.** Named rather than counted, the substantial ones
first:

- **★ NEITHER OF THE PAPER'S TWO COMPOUND CORPUS FIGURES REPRODUCES FROM ITS OWN LISTED COMPONENTS**
  (§6.1): the six song counts sum to 1124 against a stated 1125, and the four durations sum to 66:19
  against a stated 66:21. **The first extract transcribes both stated totals and computes neither sum.**
- **★ THE PAPER'S EXACT-DECODING ARM EXCLUDES ITS OWN HEADLINE MODEL** (§7.2). Both files record that the
  exact arm covers the n-gram-plus-negative-binomial combinations, and both record that the best model is
  GRU-512 with GRU-256. **Only this read draws the consequence**: the configuration Table 3's headline row
  reports has no exact arm and, by the paper's own argument, can have none — so nothing in the paper bounds
  what the approximation costs it. The first extract instead records the measured bound as *"a measured
  bound on ITS data and model, not on L2's"*, which is a different and record-side point.
- **★ THE JUSTIFICATION FOR THE LABEL-INDEPENDENT DURATION TERM IS ABOUT HMMs AND THE MODEL IS NOT AN
  HMM** (§7.1(4)). The first extract quotes the same sentence and records the label-independence as a
  choice with a cited ground; it does not note that the cited ground concerns the class of model the paper
  is arguing against.
- **The label prior is inert under the paper's own uniformity assumption** (§6.8), which neither file's
  transcription had drawn out.
- **The compression mapping cannot represent a restated chord** (§7.3) — a structural consequence a
  symbolic design would inherit.
- **GRU-32 sits outside the language-model grid the paper states** (§6.7). *(The first extract lists the
  grid and names the 32-unit model as a baseline in the same paragraph, and does not remark on it.)*
- **Twelve of the paper's fourteen integrated measurements are published only as plotted points** (§6.10).
  *(Both files record that the per-combination values are untabulated; only this read counts them.)*
- **The embedding's own description accounts for exactly the 25-class alphabet** (§6.11).

**★ AND ONE THING BOTH READS REACHED INDEPENDENTLY THAT IS WORTH NAMING AS AGREEMENT:** that Figure 5 is
drawn from a 128-unit duration model while the tables report 256 and 16. **The first extract records it
twice** — at its Figure 5 paragraph and at its finding (12). **This read records it at §7.1(3)** and adds
that the paper's mechanism argument for the GRU duration model is therefore made entirely at a
configuration none of its three tables scores.

### §9.5 What the cross-check does NOT establish

- **It does not establish that either file is complete.** It ran over what both files carry. A claim
  present in one and absent from the other was compared only where this read noticed the absence.
- **It does not reach the first extract's record-side half at all** (§9.2's bound). Its centrality
  verdict, its fifteen routed findings, its citations into `FRAMEWORK.md`, the findings surface,
  `population.md`, the bibliography, the slice derivation, the progress record, both commissions and the
  rows 11 and 19 extracts were **checked at no object by this read**.
- **It changed no value of the paper.** Every correction it forced, in either direction, is a quotation
  or a subscript or a hyphen.
- **It did not touch the first extract.** That file is byte-unchanged; the five items at §9.3(a) to (e)
  stand with the user.

---

## §10 — The user-ordered fact- and source-check, run after this file had landed twice

**The user's standing rule of 2026-09-12 extends the pre-landing check to landed work on four axes —
completeness, coherence, correctness, and misuse of hyperbole and absolutes — and his opening instruction
to this sitting ordered it over everything this side has written.**

**WHAT IT REACHED IN THIS FILE, AND HOW FAR.** **§9 was swept, because §9 was written after §8's sweep ran
and had therefore had no pass at all** — which is the structural finding the hundred-and-seventy-seventh
records, met here for the second time in one sitting. **§0 to §8 were NOT re-read whole at this check**:
they had already had the writing, the read-back, the sweep, §8's own sweep and the cross-check, and this
pass did not go over them again.

**WHAT THE §9 SWEEP FOUND — one item, named:**

- **★ A RANKING OF THIS READ'S OWN FINDINGS AGAINST ONE ANOTHER, IN §9.4.** The heading read **"THE
  CROSS-CHECK'S CLEAREST RESULT IS A CONFIRMATION"**, preserved here (#12). **Nothing in this file ranks
  the cross-check's results, and no such ranking was derived.** It now reads *"One result of the
  cross-check is a confirmation rather than a disagreement"*, which is what the section establishes. **It
  is Tell A again, in the section written to report the cross-check — the same shape §8.4 records finding
  inside the section written to report Tell A.**

**WHAT THIS CHECK DOES NOT ESTABLISH.** That this file is clean. **§9 had one pass before this sweep and
now has two; §0 to §8 have the passes §8 records and no more.** **Every pass this sitting ran found
something the passes before it had left standing**, and nothing here says the next would come back empty.

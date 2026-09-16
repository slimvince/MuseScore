# EXTRACT — Korzeniowski & Widmer, "Improved Chord Recognition by Combining Duration and Harmonic Language Models" — Task B candidacy row 20, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All eight pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.** The
> held document prints page numbers 10–17 (the proceedings' pagination); **every location below is the
> printed page number and the section, equation, figure or table number as printed.**
>
> **Why this paper and its place in L2's slice.** It is row 20 of `reading_pass/candidacy_upgrades.md`
> (line 82), ADMITTED there as *"A segment-duration model beside a chord language model — directly a
> candidate for how L2 scores segment length, which the charter leaves to detail."*
> `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 (line 67) places it in L2's slice: *"How L2
> scores segment length, which the charter leaves to detail. Noted: harmonic rhythm is L3's publication,
> but the method is a scoring term inside the decode, not a read-off."* It is fourth in group 2 of the
> proposed reading order ("segmentation decided with the labelling": rows 10, 11, 19, 20, 18, 4, 47).
> **The record cites this paper at NO ratified place and NO verified figure.** A `Grep` of the staged
> tree for "Korzeniowski" and "Widmer" before extracting found the first name in `FRAMEWORK.md` nowhere,
> in `cowork_reading_pass_findings_2026_08_31.md` nowhere, and in `reading_pass/population.md` nowhere
> (that file's two "Widmer" matches, lines 107 and 109, are Karystinaios & Widmer, rows V6 and V8); its
> only occurrences are the bibliography's row (line 34), the candidacy row, the slice derivation's row,
> the progress record's "Next" section and the hundred-and-twenty-fourth handoff entry. **So no [FACT]
> rests on this paper, and there is nothing to re-verify; what the read establishes is what the method
> IS.** The progress record carries two things from rows 11 and 19 to this row (its "Next" section):
> class the paper's duration model by row 11's §2.3 factorization test, and establish at page 1 whether
> the input is audio or symbolic. Ruling 1 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps
> the gate: no derivation before L2's slice of Task B is read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — NO finding; the input is AUDIO

Filip Korzeniowski and Gerhard Widmer, Institute of Computational Perception, Johannes Kepler
University, Linz. Printed title: **"IMPROVED CHORD RECOGNITION BY COMBINING DURATION AND HARMONIC
LANGUAGE MODELS"** (p. 10). The running header on pp. 11–17 prints *"Proceedings of the 19th ISMIR
Conference, Paris, France, September 23-27, 2018"*; the licence block on p. 10 prints *"© Filip
Korzeniowski and Gerhard Widmer. Licensed under a Creative Commons Attribution 4.0 International License
(CC BY 4.0)"* with the attribution line naming *"19th International Society for Music Information
Retrieval Conference, Paris, France, 2018"*. The bibliography's row (`docs/research_papers/BIBLIOGRAPHY.md`
line 34) names *Korzeniowski & Widmer, "Improved Chord Recognition by Combining Duration and Harmonic
Language Models," ISMIR 2018*, the ISMIR archive URL, held ✓, tier *CC*. **Title, authors, venue, year
and licence tier all match at the object.** Eight printed pages (10–17); seven numbered sections (1
Introduction; 2 Chord Sequence Modelling; 3 Models, with §3.1 Acoustic Model, §3.2 Language Model, §3.3
Duration Model, §3.4 Model Integration; 4 Experiments, with §4.1 Data, §4.2 Language Models, §4.3
Duration Models, §4.4 Integrated Models; 5 Conclusion and Discussion; 6 Acknowledgements; 7 References,
33 entries); six figures, three tables, two numbered equations, seven footnotes.

**The carried question (b) is answered at page 1: the input is AUDIO.** §1's first sentence (p. 10):
*"Chord recognition methods recognise and transcribe musical chords from audio recordings."* The
Abstract: *"Chord recognition systems typically comprise an acoustic model that predicts chords for each
audio frame, and a temporal model that casts these predictions into labelled chord segments."* So the
paper is admitted for its METHOD with the audio domain travelling as a caveat under the derivation's
consequence (ii), exactly as rows 27, 3 and 26 were. Nothing in the record's characterisation of the
paper is contradicted by its identity.

**File:** `docs/research_papers/korzeniowski_widmer_2018_ismir_duration_harmonic_language_models.pdf`
(384,606 bytes at the listing).

## Claims, labeled

### What the method decides, and from what

**★ [FACT, p. 11 §2, eq. 1 and the factorisation beneath it] The task is frame-wise sequence labelling
over audio frames, decoded as one best chord-label sequence; the model factorises into an ACOUSTIC model
per frame, a TEMPORAL model over the label history, and a uniform label prior.** *"Chord recognition is
a sequence labelling task, i.e. we need to assign a categorical label y_t ∈ 𝒴 (a chord from a chord
alphabet) to each member of the observed sequence x_t (an audio frame), such that y_t is the harmonic
interpretation of the music represented by x_t."* ŷ_{1:T} = argmax_{y_{1:T}} P(y_{1:T} | x_{1:T}) (eq.
1); P(y_{1:T} | x_{1:T}) ∝ ∏_t (1/P(y_t)) · P_A(y_t | x_t) · P_T(y_t | y_{1:t−1}), *"where P_A is the
acoustic model, P_T the temporal model, and P(y_t) the label prior which we assume to be uniform as in
[31]."* Figure 1 (p. 11) draws the generative structure with *"each chord label y_t depend[ing] on all
previous labels y_{1:t−1}"*.

**★ [FACT, p. 11 §2] THE PAPER'S CONTRIBUTION IS TO DISENTANGLE THE TEMPORAL MODEL INTO TWO: a
HARMONIC LANGUAGE MODEL over the chord sequence with consecutive duplicates removed, and a DURATION MODEL
that predicts, per frame, only whether the chord CHANGES or STAYS.** *"To enable this, we disentangle
P_T into a harmonic language model P_L and a duration model P_D, where the former models the harmonic
progression of a piece, and the latter models the duration of chords."* The language model: *"P_L is
defined as P_L(ȳ_k | ȳ_{1:k−1}), where ȳ_{1:k} = 𝒞(y_{1:t}), and 𝒞(·) is a sequence compression mapping
that removes all consecutive duplicates of a chord (e.g. 𝒞((C, C, F, F, G)) = (C, F, G)). The frame-wise
labels y_{1:t} are thus reduced to chord changes, and P_L can focus on modelling these."* The duration
model: *"P_D is defined as P_D(s_t | y_{1:t−1}), where s_t ∈ {c, s} indicates whether the chord changes
(c) or stays the same (s) at time t. P_D thus only predicts whether the chord will change or not, but not
which chord will follow—this is left to the language model P_L. This definition allows P_D to consider
the preceding chord labels y_{1:t−1}; in practice, we restrict the model to only depend on the preceding
chord changes, i.e. P_D(s_t | s_{1:t−1}). Exploring more complex models of harmonic rhythm is left for
future work."* The combination (eq. 2, p. 11): P_T(y_t | y_{1:t−1}) = P_L(ȳ_k | ȳ_{1:k−1}) · P_D(c |
y_{1:t−1}) if y_t ≠ y_{t−1}; = P_D(s | y_{1:t−1}) otherwise. Figure 2 (p. 11) draws this as a
*"chord-time lattice"*: *"For each audio frame, we move along the time-axis to the right. If the chord
changes, we move diagonally to the upper right … If the chord stays the same, we move only to the right."*

**★ [FACT, p. 11 §2; p. 12 §3.4] The model is NOT exactly decodable, by the authors' own statement, and
the paper decodes it APPROXIMATELY by hashed beam search.** *"This model cannot be decoded efficiently at
test-time because each y_t depends on all its predecessors. We will thus use either models that restrict
these connections to a finite past (such as higher-order Markov models) or use approximate inference
methods for other models (such as RNNs)."* (§2.) *"The flip side of the coin is, however, that this
property prohibits the use of dynamic programming approaches for efficient decoding. We cannot exactly
and efficiently decode the best chord sequence given the input audio. Hence we have to resort to
approximate inference. In particular, we employ hashed beam search [32] to decode the chord sequence."*
(§3.4.) The beam keeps *"the N_b best paths through all possible chord-time lattices"*; because *"the
beam might saturate with almost identical solutions, e.g. the same chord sequence differing only
marginally in the times the chords change"*, the hash function is defined (p. 13) as *"the last N_h chord
symbols in the sequence, regardless of their duration; formally, the hash function f_h(y_{1:t}) =
ȳ_{(k−N_h):k}"* — *"our formulation ensures that sequences that differ only in timing, but not in chord
sequence, are considered similar"* — and the beam keeps *"the best N_b solutions, and at most N_s similar
solutions."*

**★ [FACT, p. 11–12 §3.1] The acoustic model is a VGG-style convolutional network over a 1.5 s patch of
a quarter-tone spectrogram, producing a 25-class softmax per frame, smoothed against over-confidence.**
Three convolutional blocks (4 layers of 32 3×3 filters with 2×1 max-pooling in frequency; 2 layers of 64;
one layer of 128 12×9 filters), feature-map-wise dropout 0.2, batch normalisation, ELU; *"a linear
convolution with 25 1×1 filters followed by global average pooling and a softmax produces the chord
class probabilities P_A(y_t | x_t)."* Input: *"a 1.5 s patch of a quarter-tone spectrogram computed using
a logarithmically spaced triangular filter bank … a sample rate of 44 100 Hz using the STFT with a frame
size of 8192 and a hop size of 4410 … 24 filters per octave between 65 Hz and 2 100 Hz"*, log-compressed.
(Derived, this extract's arithmetic: a hop of 4410 samples at 44 100 Hz is one frame per 0.1 s.) Against
over-confidence: *"first, we train the model using uniform smoothing (i.e. we assign a proportion of 1 −
β to other classes during training); second, during inference, we apply the temperature softmax function
… In this paper, we use β = 0.9 and τ = 1.3, as determined in preliminary experiments."*

**★ [FACT, p. 12 §3.2] The language model is a recurrent network predicting the next chord symbol from
the chord symbols seen, following the authors' own earlier study [21].** *"The language model P_L
predicts the next chord, regardless of its duration, given the chord sequence it has previously seen. As
shown in [21], RNN-based models perform better than n-gram models at this task."* Figure 3 (p. 12) is
the generic next-step-prediction sketch; *"In our case, the inputs z_k are the chord symbols given by
𝒞(y_{1:T})."*

**★ [FACT, p. 12 §3.3] The duration model is a recurrent network over the CHANGE/STAY event sequence,
and the paper states in terms what the static alternatives are and why it rejects both them and the
beat-synchronous explicit-duration alternative.** *"Existing temporal models induce implicit duration
models: for example, an HMM implies an exponential chord duration distribution (if one state is used to
model a chord), or a negative binomial distribution (if multiple left-to-right states are used per
chord). However, such duration models are simplistic, static, and do not adapt to the processed piece."*
*"An explicit duration model has been explored in [4], where beat-synchronised chord durations were
stored as discrete distributions. Their approach is useful for beat-synchronised models, but impractical
for frame-wise models—the probability tables would become too large, and data too sparse to estimate
them. Since our approach avoids the potentially error-prone beat synchronisation, the approach of [4]
does not work in our case."* *"Instead, we opt to use recurrent neural networks to model chord durations.
These models are able to adapt to characteristics of the processed data [21], and have shown great
potential in processing periodic signals [1] (and chords do change periodically within a piece). To
train a RNN-based duration model, we set up a next-step-prediction task, identical in principle to the
set-up for harmonic language modelling: the network has to compute the probability of a chord change in
the next time step, given the chord changes it has seen in the past. We thus simplify P_D(s_t | y_{1:t−1})
≙ P_D(s_t | s_{1:t−1}), as mentioned earlier."* **So the segment-length term is LABEL-INDEPENDENT by
choice, and its context is the whole history of change events in the path being decoded.**

**★ [FACT, p. 12 §3.4] The stated reason for a recurrent temporal model is that it ADAPTS TO THE PIECE
BEING DECODED — including its harmonic rhythm.** *"Dynamic models such as RNNs have one main advantage
over their static counter-parts (e.g. n-gram models for language modelling or HMMs for duration
modelling): they consider all previous observations when predicting the next one. As a consequence,
they are able to adapt to the piece that is currently processed—they assign higher probabilities to
sub-sequences of chords that they have seen earlier [21], or predict chord changes according to the
harmonic rhythm of a song (see Sec. 4.3)."*

### The experimental setting (p. 13–15, §4.1–§4.4)

**★ [FACT, p. 13 §4.1] Data: audio, popular music, 1125 songs in 4-fold cross-validation; the language
and duration models additionally trained on four chord-annotation corpora without audio; a 25-class
major/minor vocabulary.** *"We use the following datasets in 4-fold cross-validation. Isophonics: 180
songs by the Beatles, 19 songs by Queen, and 18 songs by Zweieck, 10:21 hours of audio; RWC Popular [15]:
100 songs in the style of American and Japanese pop music, 6:46 hours of audio; Robbie Williams [13]: 65
songs by Robbie Williams, 4:30 hours of audio; and McGill Billboard [3]: 742 songs sampled from the
American billboard charts between 1958 and 1991, 44:42 hours of audio. The compound dataset thus comprises
1125 unique songs, and a total of 66:21 hours of audio."* *"Furthermore, we used the following data sets
(with duplicate songs removed) as additional data for training the language and duration models: 173
songs from the Rock [11] corpus; a subset of 160 songs from UsPop2002 for which chord annotations are
available; 291 songs from Weimar Jazz, with chord annotations taken from lead sheets of Jazz standards;
and Jay Chou [12], a small collection of 29 Chinese pop songs."* *"We focus on the major/minor chord
vocabulary, and following [7], map all chords containing a minor third to minor, and all others to major.
This leaves us with 25 classes: 12 root notes × {major, minor} and the 'no-chord' class."* (Reference
[11] as printed is de Clercq & Temperley 2011, candidacy row 60 — the Rock corpus's chord annotations are
consumed here as language- and duration-model training data; recorded as printed, no verdict.)

**★ [FACT, p. 13 §4.2, Table 1] Language models: hyperparameters by a restricted grid search on the
first fold's validation score; two data augmentations, one of them RANDOM KEY SHIFT with the stated
reason; the best model a single-layer 512-unit GRU; evaluated by average log-probability of the correct
next chord.** *"To increase the diversity in the training data, we use two data augmentation techniques,
applied each time we show a piece to the network. First, we randomly shift the key of the piece; the
network can thus learn that harmonic relations are independent of the key, as in roman numeral analysis.
Second, we select a sub-sequence of random length instead of the complete chord sequence; the network
thus has to learn to cope with varying context sizes."* Grid: layers ∈ {1, 2, 3}, units ∈ {256, 512},
unit type ∈ {GRU, LSTM}, input embedding ∈ {one-hot, ℝ⁸, ℝ¹⁶, ℝ²⁴}, learning rate ∈ {0.001, 0.005}, skip
connections ∈ {on, off}; 100 epochs, mini-batches of 4, Adam, learning rate annealed linearly to 0 from
epoch 50. *"The best model turned out to be a single-layer network of 512 GRUs, with a learnable
16-dimensional input embedding and without skip connections, trained using a learning rate of 0.005."*
Baselines: a 32-unit GRU, a 2-gram and a 4-gram (*"Both can be used for chord recognition in a
higher-order HMM [25]"*), the n-grams by maximum likelihood with Lidstone smoothing as in [21]. Table 1,
every cell as printed:

| | GRU-512 | GRU-32 | 4-gram | 2-gram |
|---|---|---|---|---|
| log-P | −1.293 | −1.576 | −1.887 | −2.393 |

**[FACT, p. 13–14 §4.2, Figure 4] The learned 16-d chord embedding, projected by PCA, reproduces
circle-of-fifths and Tonnetz relations — reported as an observation without explanation.** *"We observe
i) that chords form three clusters around the center, in which the minor chords are farther from the
center than major chords; ii) that the clusters group major and minor chords with the same root, and the
distance between the roots are minor thirds (e.g. C, E♭, F♯, A); iii) that clockwise movement in the
circle of fifths corresponds to clockwise movement in the projected embedding; and iv) that the way
chords are grouped in the embedding corresponds to how they are connected in the Tonnetz. At this time,
we cannot provide an explanation for these automatically emerging patterns."*

**★ [FACT, p. 14 §4.3, Table 2, Figure 5] Duration models: the best a single-layer 256-unit GRU;
two static baselines derived from HMM structure, each with ONE parametrisation for all chords, with the
stated justification; measured by average log-probability of a chord duration; the GRU shown adapting
to the piece's harmonic rhythm.** Grid: unit type ∈ {vanilla RNN, GRU, LSTM}, units ∈ {16, 32, 64, 128,
256} for LSTM and GRU and {128, 256, 512} for the vanilla RNN, one recurrent layer; *"We found networks
of 256 GRU units to perform best; although this indicates that even bigger models might give better
results, for the purposes of this study, we think that this configuration is a good balance between
prediction quality and model complexity."* Trained 100 epochs, Adam, learning rate 0.001 decreasing
linearly to 0, mini-batches of 10, sequences cut into *"excerpts of 200 time steps (20 s)"*, gradient
clipping 0.001. The baselines: *"The first baseline we consider is a negative binomial distribution. It
can be modelled by a HMM using n states per chord, connected in a left-to-right manner, with transitions
of probability p between the states (self-transitions thus have probability 1 − p). The second, a special
case of the first with n = 1, is an exponential distribution; this is the implicit duration distribution
used by all chord recognition models that employ a simple 1-state-per-chord HMM as temporal model. Both
baselines are trained using maximum likelihood estimation."* *"We assume a single parametrisation for
each chord; this ostensible simplification is justified, because simple temporal models such as HMMs do
not profit from chord information, as shown by [4, 7]."* Table 2, every cell as printed:

| | GRU-256 | GRU-16 | Neg. Binom. | Exp. |
|---|---|---|---|---|
| log-P | −2.014 | −2.868 | −3.946 | −4.003 |

Figure 5 (p. 14) plots P_D(s_t | s_{1:t−1}) over 55–80 s of one song for three models — its legend
prints *Negative Binomial*, *GRU-16* and *GRU-128* (a 128-unit model, where Table 2 and the text report
the 256-unit one; recorded as printed) — with true chord changes as dashed lines. The paper's reading:
*"as a dynamic model, it can adapt to the harmonic rhythm of a piece, while static models are not
capable of doing so. We see that a GRU with 128 units predicts chord changes with high probability at
periods of the harmonic rhythm. It also reliably remembers the period over large gaps in which the chord
did not change (between seconds 61 and 76). During this time, the peaks decay differently for different
multiples of the period, which indicates that the network simultaneously tracks multiple periods of
varying importance. In contrast, the negative binomial distribution statically yields a higher chord
change probability that rises with the number of audio frames since the last chord change. Finally, the
smaller GRU model with only 16 units also manages to adapt to the harmonic rhythm; however, its
predictions between the peaks are noisier, and it fails to remember the period correctly in the time
without chord changes."*

**★ [FACT, p. 15 §4.4, Table 3, Figure 6] Integrated models: every combination of four language and
three duration models decoded by hashed beam search (N_b = 25, N_s = 4, N_h = 5), plus EXACT decoding
for the n-gram/negative-binomial combinations; metric WCSR (duration-weighted), plus root accuracy and a
segmentation measure; the gain of the best combination over the standard one is MODEST and
SIGNIFICANT by a paired t-test; the gain grows LINEARLY with each sub-model's log-probability and does
not flatten; the beam's cost against exact decoding is small.** The acoustic model: 300 epochs of 200
updates, mini-batches of 512, Adam, learning rate decayed to 0 over the last 100 epochs. *"We compare
all combinations of language and duration models presented in the previous sections. For language
modelling, these are the GRU-512, GRU-32, 4-gram, and 2-gram models; for duration modelling, these are
the GRU-256, GRU-16, and negative binomial models. (We leave out the exponential model, because its
results differ negligibly from the negative binomial one.)"* *"Additionally, we evaluate exact decoding
results for the n-gram language models in combination with the negative binomial duration distribution.
This will indicate how much the results suffer due to the approximate beam search."* The metric: *"we
use the weighted chord symbol recall (WCSR) over the major/minor chord alphabet, as defined in [30]. We
thus compute WCSR = t_c / t_a, where t_c is the total duration of chord segments that have been
recognised correctly, and t_a is the total duration of chord segments annotated with chords from the
target alphabet. We also report chord root accuracy and a measure of segmentation (see [16], Sec.
8.3)."* Table 3, every cell as printed (bold in the paper marks the better row):

| Model | Root | Maj/Min | Seg. |
|---|---|---|---|
| 2-gram / neg. binom. | 0.812 | 0.795 | 0.804 |
| GRU-512 / GRU-256 | **0.821** | **0.805** | **0.814** |

Derived differences, best model minus standard model (this extract's arithmetic from the cells): root
+0.009, maj/min +0.010, segmentation +0.010. The paper's reading: *"Although the improvements are modest,
they are consistent, as shown by a paired t-test (p < 2.487 × 10⁻²³ for all differences)."* On Figure 6
(p. 15), which plots WCSR against each sub-model's log-probability from both perspectives: *"Better
language and duration models directly improve chord recognition results, as the WCSR increases linearly
with higher log-probability of each model. As this relationship does not seem to flatten out, further
improvement of each model type can still increase the score. We also observe that the approximate beam
search does not impair the result by much compared to exact decoding (compare the dotted blue line with
the solid one)."* **The per-combination WCSR values exist only as plotted points in Figure 6 and are not
tabulated; they are not transcribed here.** One cell flagged rather than transcribed: the middle tick
label of Figure 6's lower x-axis (the duration-model log-probability axis) reads at the image as a value
that does not match Table 2's GRU-16 entry (−2.868); it could not be read with certainty and is recorded
as a flag.

### The paper's own conclusion and its stated position (p. 10 §1; p. 15 §5)

**[FACT, p. 10 §1] The position is stated at the outset, with its two cited grounds:** *"First-order
models are not capable of learning meaningful musical relations, and only smooth the predictions [4,
7]. More powerful models, such as RNNs, do not perform better than their first-order counterparts [24].
In addition to the fundamental flaw of first-order models (chord patterns comprise more than two chords)
both approaches are limited by the low hierarchical level they are applied on: the temporal model is
required to predict the next symbol for each audio frame. This makes the model focus on short-term
smoothing, and neglect longer-term musical relations between chords, because, most of the time, the
chord in the next audio frame is the same as in the current one."* The stated contribution (i): *"we
describe a probabilistic model that allows for the integration of chord-level language models with
frame-level acoustic models, by connecting the two using chord duration models"*.

**[FACT, p. 15 §5]** *"We described a probabilistic model that disentangles three components of a chord
recognition system: the acoustic model, the duration model, and the language model. We then developed
better duration and language models than have been used for chord recognition, and illustrated why the
RNN-based duration models perform better and are more meaningful than their static counterparts
implicitly employed in HMMs. … Finally, we showed that improvements in each of these models directly
influence chord recognition results."* And the position: *"These aspects have been neglected because
they did not show great potential for improving the final result [4, 7]. However, we believe (see [24]
for some evidence) that this was due to the improper assumption that temporal models applied on the
time-frame level can appropriately model musical knowledge. The results in this paper indicate that
chord transitions modelled on the chord level, and connected to audio frames via strong duration models,
indeed have the capability to improve chord recognition results."* (Reference [24] as printed is the
authors' own *"On the Futility of Learning Complex Frame-Level Language Models for Chord Recognition"*,
AES 2017 — unheld, not read, nothing carried out of it.)

**[THEORY, as the paper cites it]** Sigtia, Boulanger-Lewandowski & Dixon 2015 [32] for hashed beam
search; Mikolov et al. 2010 [28] for the recurrent language model set-up; the authors' own [21]
(Korzeniowski, Sears & Widmer, ICASSP 2018) for the language-model comparison and Lidstone smoothing;
Chen et al. 2012 [4] for duration-explicit HMMs; Cho & Bello 2014 [7] for the major/minor mapping and
the finding that HMM temporal models do not profit from chord information; Pauwels & Peeters 2013 [30]
for WCSR; Harte 2010 [16] §8.3 for the segmentation measure; Renals et al. 1994 [31] for the uniform
label prior; Böck & Schedl 2011 [1] for recurrent networks on periodic signals; Mauch & Dixon TASLP 2010
[26] (candidacy row 44, unheld) as a hand-designed Bayesian-network temporal model.

**[CONJECTURE — the authors' own, labelled as such here]** That the neglect of temporal modelling in the
literature was *"due to the improper assumption"* about frame-level models (§5, *"we believe"*); that
*"even bigger models might give better results"* (§4.3); that the linear WCSR-versus-log-probability
relation continues beyond the models tried (§4.4, *"does not seem to flatten out"*); and the four
embedding observations' meaning (§4.2, *"we cannot provide an explanation"*).

## Coupling facts (mandatory)

**What the method ASSUMES about its upstream.**
- Audio, sampled at 44 100 Hz, framed at 0.1 s (derived) into a quarter-tone spectrogram; NO notes, NO
  spelling, NO beat grid (the paper explicitly avoids beat synchronisation, §3.3), NO meter, NO voices,
  NO key signature. The acoustic model's output per frame, a 25-class distribution, is the only thing the
  temporal model reads about the music.
- Training data as frame-labelled chord sequences over a 25-class major/minor-plus-no-chord alphabet;
  for the language and duration models, chord-symbol sequences without audio suffice (four such corpora
  are added, §4.1), and the training sequences are key-shifted at random (§4.2).
- The candidate boundary set is every frame edge; no maximum segment length is stated anywhere in the
  held document.

**What it HANDS downstream.**
- One best frame-labelled chord sequence — equivalently, a segmentation into chord regions each carrying
  one of 25 labels — chosen by beam search, with the timing of each change on the 0.1 s frame grid.
- In principle the N_b = 25 beam paths; the paper reports only the best and publishes no rival readings
  and no confidence. No exact normaliser exists (the model is not exactly decodable, §2, §3.4).
- No tonality, no scale degree, no inversion, no bass, no chord tones, no chord beyond major/minor.

**Its own STATED SCOPE and limits.**
- **Domain:** audio; popular music (Beatles, Queen, Zweieck, RWC Popular, Robbie Williams, Billboard),
  with rock, pop and jazz chord sequences added for the symbolic sub-models.
- **Decision scope:** the chord label and where it changes; tonality is not decided anywhere, and the
  chord vocabulary is major/minor only, by the authors' choice following [7].
- **Cost:** exact decoding impossible for the chosen model; beam search with N_b = 25, N_s = 4, N_h = 5.
- **Fitting:** each sub-model fitted separately (the acoustic model discriminatively; the language and
  duration networks by next-step prediction; the n-gram and HMM-duration baselines by maximum
  likelihood), then combined by the product of eq. 1's factorisation with NO combination weights fitted
  and the label prior assumed uniform; hyperparameters by grid search on the first fold's validation
  score; β, τ, N_b, N_s and N_h by *"preliminary experiments"*; a paired t-test reported for Table 3's
  differences; 4-fold cross-validation on 1125 songs.
- **Coupling:** segmentation and label decided together in one path score; the label-transition term
  (the language model) and the segment-length term (the duration model) are SEPARATE factors with
  separate inputs, and the length term is conditioned on the change history only, never on the label.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adopt (the factorisation of the temporal score into a label-sequence term and a length term):** eq.
  2 separates "which chord follows" (P_L, over the deduplicated chord sequence) from "does the chord
  change here" (P_D, over frames). The record's own chord-transition table (D-532, D-533) is already a
  term over the chord SEQUENCE and not over frames, so the record's shape agrees with the paper's stated
  position that *"chord transitions modelled on the chord level"* are what carries musical knowledge; what
  the record does NOT yet fix is the length term, which is exactly what the charter leaves to detail and
  what this paper isolates and measures.
- **Adapt (the duration model as an explicit, measured, label-independent length term):** the paper
  gives three shapes for the length term with a measured log-probability for each — exponential (the
  one-state HMM's implicit prior), negative binomial (the n-state HMM's), and a recurrent model over the
  change history — and shows the recurrent one adapting to the harmonic rhythm of the piece (Figure 5).
  An L2 detail specification deciding how to score segment length has here the only held primary in the
  slice whose SUBJECT is that term.
- **Adapt, with the classification carried from row 11 (finding 3 below):** the exponential baseline IS
  row 19's linear-in-length self-transition term and needs no segmental decode; the negative binomial
  needs no segmental decode either but multiplies the state space by n; the recurrent model needs neither
  a frame decode nor a segmental one — it needs approximate inference, because its context is unbounded.
  So the paper's chosen term is outside both families row 11's test distinguishes, and adopting its SHAPE
  would cost L2 its exact decode.
- **Must argue against (approximate decoding):** the L2 charter's "may not … discard a rival before the
  whole sequence of spans has been scored" forbids exactly what beam search does. The paper measures the
  cost of its approximation on the combinations where exact decoding exists and reports it small (Figure
  6, the dotted against the solid line, values not tabulated) — a measured bound on ITS data and model,
  not on L2's. A detail specification adopting an unbounded-history length term would have to meet this
  charter clause, and the paper's own remedy (hashed beam search keyed on the last N_h chord symbols) is
  a rival practice the specification must argue against, not adopt.
- **Must argue against (the grid and the input):** every boundary this system can place is a 0.1 s frame
  edge, against the L1 charter's change-point grid and the L2 charter's "boundaries are a subset of L1's
  change points"; the input carries no notes at all. Its measured figures are therefore for a decision on
  a different candidate set from L2's and are not comparable with any figure the record publishes.
- **Must argue against (the label-independent length term):** the paper conditions segment length on
  the change history only, justified by [4, 7]'s finding that HMM temporal models do not profit from
  chord information, and leaves *"more complex models of harmonic rhythm"* to future work. Whether L2's
  length term should depend on the chord (or the tonality, or the cadence cue) is a question the paper
  raises and does not answer; a detail specification takes a position on it with its own defense.

## ★ Findings, routed and not applied

**(1) IDENTITY: NO finding; the input is AUDIO.** Printed title, authors, venue, year and CC BY 4.0
licence all match the bibliography's row 34 at page 1 and the running header. The carried question (b)
is answered: audio, popular music. The domain travels as a caveat under the derivation's consequence
(ii); the ADMITTED verdict is for the method and stands. No verdict.

**(2) NO [FACT] RESTS ON THIS PAPER, confirmed by `Grep` of the staged tree and not inherited.** The
name occurs in no ratified text and in no verified figure; the hundred-and-twenty-fourth entry's report
that `population.md` §3 names no Korzeniowski primary is CONFIRMED (its two "Widmer" matches are
Karystinaios & Widmer). So this read re-verifies nothing and establishes what the method is. No verdict.

**(3) The question carried from rows 11 and 19 is ANSWERED at the object: the paper's duration model
classes OUTSIDE both families row 11's §2.3 test distinguishes, and its two baselines class cleanly on
the does-not-need-the-segmental-decode side.** Row 11's test: a segment-length term needs the segmental
decode if and only if it is not a sum of per-frame terms. **The classification below is this extract's,
applying that test; what the paper itself states is the HMM form of each baseline and the
all-predecessors dependence of its chosen model.** (a) The EXPONENTIAL baseline — *"the implicit
duration distribution used by all chord recognition models that employ a simple 1-state-per-chord HMM"*
— is a constant per-frame self-transition term, linear in length as a log-score: row 19's shape, no
segmental decode needed. (b) The NEGATIVE BINOMIAL baseline is, by the paper's own statement, *"modelled
by a HMM using n states per chord, connected in a left-to-right manner"* — expressible with per-frame
terms over an n-fold expanded state, so no segmental decode needed, at the cost of n times the state
space. (c) The CHOSEN recurrent model P_D(s_t | s_{1:t−1}) is a per-frame factor whose value depends on
the ENTIRE history of change events in the path — not a local per-frame term, and not a per-segment
term seeing only the previous segment either; the paper says so in terms (*"each y_t depends on all its
predecessors"*, *"cannot exactly and efficiently decode"*). So it is neither an order-1 CRF term nor a
semi-CRF term; it is a higher-order term that forces approximate inference. **The slice now holds three
worked shapes for the length term: linear (row 19, exponential here — no segmental decode), Gaussian
(row 11's example — segmental decode), and unbounded-history (here — neither; approximate decode), plus
the negative binomial as a bounded-state frame-level shape.** Routed to L2's detail specification beside
row 11's finding (4), row 19's finding (5) and D-004; no verdict.

**(4) The temporal score is FACTORISED into a chord-level language term over the deduplicated chord
sequence and a frame-level change/stay term, and the paper's stated position is that frame-level
temporal models cannot carry musical knowledge.** The record's chord-transition table (D-532, D-533)
is a chord-level term of the first kind; the paper is a published, measured instance of that separation
with the length term isolated. Routed to L2's detail specification beside D-532 and D-533; no verdict.

**(5) The segment-length term is LABEL-INDEPENDENT by the authors' choice, with a cited ground ([4, 7])
and "more complex models of harmonic rhythm" left to future work.** Whether L2's length term should read
the chord, the tonality or a cadence cue is a question this paper raises and does not answer. Routed to
L2's detail specification as a question; no verdict.

**(6) The duration model ADAPTS TO THE PIECE'S HARMONIC RHYTHM inside the decode (Figure 5, §3.4),
which the slice derivation's own note anticipated: harmonic rhythm is L3's PUBLICATION in the framework
(§5 L3: *"the harmonic rhythm"* among L3's read-off facts), but here a learned model of it is a SCORING
TERM inside the segmentation decision.** CONFIRMED at the object as the derivation states it — a term,
not a read-off. The record's layer division puts harmonic rhythm downstream of L2 as a fact read off the
settled reading; this paper puts a model of it upstream as evidence for where boundaries fall. That is a
rival placement for one fact the framework already homes, and a detail specification that wanted a
periodicity term in L2's length score would have to state how it differs from L3's read-off (one is a
prior over where changes are likely; the other is a description of where they were decided). Routed to
L2's and L3's detail specifications and to the findings surface's DP-C block; no verdict.

**(7) Exact decoding is GIVEN UP for the chosen model, replaced by hashed beam search keyed on the last
five chord symbols regardless of timing, with the approximation's cost measured small on its own data
(Figure 6, untabulated).** An instance of the practice the L2 charter's no-early-discard clause forbids,
with a measured bound that does not transfer. Beside D-098 (the exact-decode reserve), D-004 and the
charter's third "may not". Routed to L2's detail specification; no verdict.

**(8) The measured gain of the best language-and-duration pair over the standard HMM-implied pair is
+0.009 root, +0.010 maj/min WCSR and +0.010 segmentation (Table 3, this extract's differences), which
the authors call MODEST and establish by a paired t-test (p < 2.487 × 10⁻²³); the per-component
contributions are plotted (Figure 6) and not tabulated.** The size bounds how much load the method's
measured benefit can carry: the duration model's own contribution is not separable from the plot with
certainty. Routed to the findings surface's DP-C block as a datum beside the other segmental gains
(V10), with the domain and the untabulated split stated; no verdict.

**(9) A published segmentation-and-labelling design that decides boundaries WITH the labels in a
frame-level lattice (Figure 2) — DP-C's "with" in a form that is NOT semi-Markov** — every frame carries
a change/stay variable decoded jointly with the label, on a fixed 0.1 s candidate grid. DP-C's candidate
list reads *"with (semi-Markov, measured)"*; this is a second measured form of "with", frame-lattice
rather than segmental, which row 3's three-chain HMM also has. Routed to the findings surface's DP-C
block as a precision to the candidate list's parenthesis; no verdict.

**(10) KEY-SHIFT augmentation makes the language model transposition-invariant, and the paper says why
in the record's own terms: *"the network can thus learn that harmonic relations are independent of the
key, as in roman numeral analysis."*** A published ground for a transposition-pooled chord-transition
term, beside row 3's transposition-pooled conditional and the record's scale-degree-valued chord axis
(D-526). Routed to L2's detail specification as a datum; no verdict.

**(11) The learned chord embedding reproduces circle-of-fifths and Tonnetz relations without being
told them (Figure 4), reported as unexplained.** A datum for the style system and the knowledge base
(the Tonnetz as a learned rather than declared structure), not for L2's decision. Routed to the style
system's owner as an observation; no verdict.

**(12) Fit/evaluation and uncertainty, at the object:** 4-fold cross-validation on 1125 songs with the
first fold's validation score used for every grid search; the language and duration models trained on
additional symbolic corpora, one of which (the Rock corpus, [11]) is candidacy row 60 and is used here
as TRAINING data; five constants (β, τ, N_b, N_s, N_h) set by *"preliminary experiments"* on an unnamed
set; a paired t-test reported for Table 3; Figure 5 drawn from a 128-unit model where Table 2 reports a
256-unit best. Routed to measurement design beside rows 8's, 26's, 30's, 5's, 10's and 19's fit
findings; no verdict.

**(13) The metric is DURATION-WEIGHTED (WCSR = t_c / t_a) with a separate segmentation measure from
Harte 2010 §8.3** — the same duration-weighting the robust unit uses (D-115), and the same segmentation
convention row 19's mir_eval score descends from. Routed to measurement design beside D-115 and row 19's
finding (12); no verdict.

**(14) No rivals, no confidence, no normaliser.** The beam holds 25 paths and the paper publishes one;
the model has no exact normaliser to publish from. The same datum as rows 11's and 19's, now on a model
that could not publish a posterior even in principle. Beside D-006, D-008 and DP-K; no verdict.

**(15) No falsifier.** Nothing read contradicts any CHOSEN design point, and no [FACT] rests on the
paper. Its frame-lattice "with" (finding 9) is a precision to DP-C's candidate list, not a measurement
against DP-C; its approximate decoding (finding 7) is a rival practice, not evidence against the charter.
**No STOP fires** under the remedial commission's §5.

## Centrality

**CENTRAL, on a narrow ground, challengeable at the progress record.** No ratified text rests on this
paper, so the ground rows 27, 5, 10, 11 and 19 carried does not apply. The ground here is the original
commission's §4 test — a paper *"whose claims would carry load in a detail specification"* — applied to
the term the candidacy row admits it for: **it is the ONLY held primary in the slice whose SUBJECT is
the segment-length term itself**, and it supplies a measured comparison of three shapes for that term
(exponential, negative binomial, recurrent) with the recurrent one shown adapting to harmonic rhythm.
An L2 detail specification deciding how to score segment length — which the charter leaves to detail
in terms — would cite this paper directly, whether to adapt its factorisation (findings 3 and 4) or to
argue against its approximate decode and its label-independent term (findings 5 and 7); the criterion's
"have to argue against" admits a rival, and a rival for a decision the specification must take is a
claim carrying load. **The ground on which NOT CENTRAL could be argued, stated so the challenge is easy
to make:** no ratified text cites it (rows 3 and 29 were NOT CENTRAL on that ground among others); its
domain is audio popular music on a 25-class vocabulary with no tonality; its measured gain is a hundredth
of WCSR and the duration model's own share of it is not tabulated; and its chosen mechanism would cost L2
its exact decode, so what a specification could adopt from it is the factorisation and the three-shape
comparison rather than the system. Against that: rows 3 and 29 were NOT CENTRAL because every design
element they exhibited had a primary or an owner elsewhere in the record — and the segment-length term
has neither. **A second independent extraction is therefore OWED** on this verdict.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`
and `cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (14) are routed and
written nowhere else. It does not fetch the authors' cited [21], [24] or [25], Sigtia et al. 2015, Chen
et al. 2012, Cho & Bello 2014, Harte 2010, Pauwels & Peeters 2013, or any of the eight audio and
chord-annotation corpora. It opens no code, touches no measurement tool, no corpus, no golden and nothing
under `tools/`. It writes no open-items row and allocates no decisions-register identity. It reads no
other paper and takes no decision about the order of the remaining slice.

---

*Provenance: written 2026-09-06 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_twenty_four.md`, on the user's opening instruction naming row 20,
after the ordinary session-start read (`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md` whole, the
derived gating answer). Read for this extract, at the files: `reading_pass/candidacy_upgrades.md` whole
(row 20 at line 82), `cowork_l2_task_b_slice_derivation_2026_09_05.md` at line 67,
`docs/research_papers/BIBLIOGRAPHY.md` at line 34, `FRAMEWORK.md` at lines 386–439 (the L2 and L3
charters) and 685–720 (DP-B to DP-H); the findings surface at lines 156–205 (the DP-C block);
`reading_pass/population.md` at lines 96–115 (the §3 verification table); the progress record whole;
both commissions whole; and the row 19 extract whole, for the form and for the carried items. The
staged tree was searched with `Grep` for "Korzeniowski" and "Widmer" before extracting. The paper itself
was read at the object as page images, all eight pages. No shell command was run on the repository or on
any staged copy of it for content or for listings; the saved root listing was consulted by `Grep` only.
No figure of this project's own measurement is restated (#17f, D-431); every value above is the paper's
own, and every derived difference or sum is marked as this extract's arithmetic.*

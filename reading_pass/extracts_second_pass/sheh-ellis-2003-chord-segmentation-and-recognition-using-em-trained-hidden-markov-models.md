# Second extraction — Sheh & Ellis, "Chord Segmentation and Recognition using EM-Trained Hidden Markov Models"

**WHAT THIS FILE IS.** The second independent extraction of candidacy row 18, written under
`cowork_reading_pass_commission_2026_08_30.md` §4's fourth bullet — *"CENTRAL sources … are extracted in
a SECOND independent pass (a fresh session, or a cleanly separated re-read that does not consult the
first extract) and the two extracts cross-checked; disagreements are resolved at the paper or recorded
as unresolved."* The eight-step order it was written under is the hundred-and-sixty-ninth handoff
entry's §3 and is not restated here (#6).

**WHAT IT IS NOT.** It is not a ruling, not a design, not a proposal, and not a verdict on the paper's
candidacy. It records what the paper says, what this read checked at the paper's own printed values,
and what the paper leaves open. Nothing in it authorises a fix, a build or an inference change.

**THE READ THAT PRODUCED IT.** A hundred-and-seventy-ninth Cowork sitting, 2026-09-14, at the
repository tip `0f69cc6b79610c962a8400cdaba3dfc12facfe55`.

---

## §0 — What was read, and the bound on this read's independence

**The held file.** `docs/research_papers/sheh_ellis_2003_ismir_chord_segmentation_em_hmm.pdf`,
**109,996 bytes**, established at this sitting's own staging call. Its page count was established **at
the tool** by a deliberately out-of-range page request, which answered *"PDF has 7 pages"*. **No
progress-row value was available to match that against** — the progress record was not opened at any
point in this sitting.

**What was read of the paper.** All seven pages, as page images, whole. Page 6 was then opened a second
time, singly, to transcribe Table 4's six confusion matrices cell by cell. **Every image was checked at
the image itself and not at the call's success line**, which is cadence 4 of the hundred-and-sixty-ninth
entry's list; every one was present and legible.

**★ THE INDEPENDENCE BOUND, DECLARED RATHER THAN CLAIMED AWAY.** This read is not independent of the
record in the way a wholly fresh reader would be, and the contamination is written down:

- The booting session read the hundred-and-seventy-eighth and hundred-and-sixty-ninth handoff entries
  whole. Neither summarises this paper.
- `reading_pass/candidacy_upgrades.md` line 80 was read before the paper was opened. **It states a
  verdict and a reason**, and the reason names two numbers: *"DP-C's 68.8-against-23.3 primary, and its
  method is the boundaries-given-versus-found design that measurement is about."* **So this read went to
  the paper knowing two of its figures and one characterisation of its method.** That is contamination
  on the independence axis and it is recorded, not argued away.
- **The first extract was NOT opened before step 7** — not read, not searched, not staged, not listed.
- The section form of this file was taken from the section HEADINGS ALONE of row 20's second extract,
  by a heading search. **No content line of that file was read.**

**★ AND THE OTHER HALF OF THE BOUND, WHICH IS LARGER.** **No sweep of this repository was run for this
paper** — not for its authors, not for its title, not for any of its values. `FRAMEWORK.md` was not
opened at all; neither was the findings surface, `population.md`, the slice derivation, the
bibliography, either commission, or the progress record. **So this file asserts nothing about what the
record says of this paper, about DP-C, or about the paper's centrality, beyond the one candidacy line it
read at the object.** The one exception, declared because it is an exception:
`reading_pass/candidacy_upgrades.md` was opened at row 18's own line, at the four lines around it, and at
the hits of one targeted search of it against this paper's reference list (§7.4).

---

## §1 — What the paper is, and the identity axis

**Title, as printed:** *Chord Segmentation and Recognition using EM-Trained Hidden Markov Models*.

**Authors, as printed:** Alexander Sheh and Daniel P.W. Ellis.

**Affiliation, as printed:** LabROSA, Dept. of Electrical Engineering, Columbia University, New York NY
10027 USA; contact addresses `{asheh79,dpwe}@ee.columbia.edu`.

**Keywords, as printed:** audio, music, chords, HMM, EM.

**The rights line, as printed on page 1:** *"Permission to make digital or hard copies of all or part of
this work for personal or classroom use is granted without fee provided that copies are not made or
distributed for profit or commercial advantage and that copies bear this notice and the full citation on
the first page. ⓒ2003 Johns Hopkins University."*

**★ THE IDENTITY AXIS — WHAT THE DOCUMENT ESTABLISHES AND WHAT IT DOES NOT.** The held document prints
the title, both authors, the affiliation, the contact addresses and a 2003 rights line naming the
institution. **It does NOT print, anywhere in the pages as read, the conference name, the conference
dates, a running header, a DOI, or a page number.** So the document establishes its own title, authors
and year at its own face, and **it does not establish at its own face that this is the ISMIR 2003
proceedings article** as against a preprint or an author copy. The venue attribution in the candidacy
row is the record's, not the document's.

*What is NOT claimed:* that the document IS a preprint; that the venue attribution is wrong; or that
some page not in this file carries a header. This read states what the seven pages carry.

**The subject, in the paper's own words (abstract).** *"In this work, we build a system for automatic
chord transcription using speech recognition tools. For features we use "pitch class profile" vectors to
emphasize the tonal content of the signal, and we show that these features far outperform cepstral
coefficients for our task. Sequence recognition is accomplished with hidden Markov models (HMMs)
directly analogous to subword models in a speech recognizer, and trained by the same
Expectation-Maximization (EM) algorithm. Crucially, this allows us to use as input only the chord
sequences for our training examples, without requiring the precise timings of the chord changes — which
are determined automatically during training. Our results on a small set of 20 early Beatles songs show
frame-level accuracy of around 75% on a forced-alignment task."*

**★ THE ONE THING A READER OF THIS PROJECT MUST HOLD BEFORE ANYTHING ELSE: THIS IS AN AUDIO SYSTEM, NOT
A SYMBOLIC ONE.** Its input is a waveform read from CD, downsampled to 11025 Hz. It has no score, no
notated pitch spelling, no bar line, no voice and no onset list. **Every accuracy figure in §5.3 is a
frame-level audio measurement**, and none of them is a measurement over notated music.

*(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**Every quantity in §5 is a frame-level
audio measurement**". False of §5.1, §5.2, §5.6 and §5.7, which are a song list, an alphabet, a
constants table and a reference list — none of them a measurement of any kind.)*

---

## §2 — The method, as the paper states it

### §2.1 The problem the paper says it is solving, and the analogy it rests on

The paper's stated ground is an analogy between chords and words. In its own words, from the abstract:
*"Chords also have the attractive property that a piece of music can (mostly) be segmented into time
intervals that consist of a single chord, much as recorded speech can (mostly) be segmented into time
intervals that correspond to specific words."* And from §1: *"By making a direct analogy between the
sequence of discrete, non-overlapping chord symbols used to describe a piece of music, and the word
sequence used to describe recorded speech, much of the speech recognition framework can be used with
minimal modification."*

**The load-bearing consequence the paper draws from the analogy, in its own words:** *"In particular, no
timing alignment is required between the chord labels and the training audio — using the constraints of
the chord sequence alone, the EM approach converges to find optimal segmentations."*

**Its stated relation to the two nearest prior works.** On features, §1 credits Fujishima (1999) with
the pitch class profile and notes that *"Fujishima's system uses nearest-neighbor classification to
chord templates, and performed well on samples containing a single instrument."* On models, §1 places
the work beside Raphael (2002): *"Our system has parallels with the work by Raphael (2002), who also
uses HMMs trained by EM to transcribe music in terms of chord labels. However, since his ultimate goal
is note-level transcription, his "chord" vocabulary distinguishes between each different combination of
simultaneous notes, in contrast to our approach of having a single model for "A minor" etc. This huge
state space precludes direct training of models for each chord, and instead structural information about
the harmonics expected for any given note combination are used to select among a relatively small set of
model 'factors', from which the desired chord models may be assembled. His system is applied to clean
recordings of solo piano music."*

**★ THE CONTRAST IS THE PAPER'S OWN STATEMENT OF ITS DESIGN CHOICE, AND IT IS ABOUT STATE-SPACE SIZE:**
one model per chord CLASS ("A minor"), against one model per simultaneous-note COMBINATION. The paper's
stated reason for the choice is trainability — a per-combination state space *"precludes direct training
of models for each chord."*

*(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**IT IS THE ONE STRUCTURAL POINT OF THIS
PAPER THAT IS ABOUT STATE-SPACE SIZE**". A uniqueness claim over a set this read never enumerated.)*

### §2.2 The feature — the pitch class profile, in 24 dimensions

**The signal front end, as stated (§2.1).** *"Monophonic music recordings x[n] sampled at 11025 Hz are
divided into overlapping frames of N = 4096 points and converted to a short-time Fourier transform
(STFT) representation."* Equation (1) is the STFT, *"where k indexes the frequency axis with 0 ≤ k ≤
N−1, n is the short-time window center, and w[m] is an N-point Hanning window."*

**The mapping to pitch classes, as stated.** The paper describes the traditional pitch class profile as
*"12-dimensional vectors, with each dimension corresponding to the intensity of a semitone class
(chroma)"*, and states what the collapse does: *"The procedure collapses pure tones of the same pitch
class, independent of octave, into the same PCP bin; for complex tones, the harmonics also fall into
particular, related bins. Frequency to pitch mapping is achieved using the logarithmic characteristic of
the equal temperament scale."*

**The paper's own departure from twelve dimensions, and its stated reason.** *"Our experiments use a
finer grained PCP vector of 24 dimensions to give some flexibility in accounting for slight variations
in tuning. A step size of 100ms, or 10 PCP frames per second, is employed."*

**The two equations that define the mapping.** Equation (2) maps STFT bins to PCP bins as
`p(k) = ⌊24 · log₂(k/N · f_sr/f_ref)⌋ mod 24`, *"where f_ref is the reference frequency corresponding to
PCP[0] and f_sr is the sampling rate."* Equation (3) is the accumulation,
`PCP[p] = Σ_{k : p(k)=p} |X[k]|²`, introduced by the sentence *"For each time slice, we calculate the
value of each PCP element by summing the magnitude of all frequency bins that correspond to a particular
pitch class i.e. for p = 0,1,···,23."*

**★ THE TEXT AND THE EQUATION DISAGREE HERE, AND IT IS RECORDED AS THE PAPER'S OWN DISAGREEMENT.** The
sentence says the element is the sum of the **magnitude** of the contributing bins; equation (3) sums
`|X[k]|²`, which is magnitude **squared** — power, not magnitude. **The two are different quantities and
the paper states both.** Which one the implementation used is not settled by the pages as read. Carried
to §7.1.

### §2.3 The model — one Gaussian-emitting state per chord

**The state space, as stated (§2.2).** *"PCP vectors are used as features to train a hidden Markov model
(HMM) with one state for each chord distinguished by the system."* The paper then restates the Markov
property and points the reader at Gold and Morgan (1999) for an introduction.

**The emission, as stated.** *"To model the PCP vector distribution for each state, we assume a single
Gaussian in 24 dimensions, described by its mean vector μ_i and covariance metric Σ_i We additionally
assume that the features are uncorrelated with each other, so that Σ_i consists only of variances, i.e.
all off-diagonal elements are zero. To specify the model we need to determine the 24 dimension mean
vector μ_i and the 24 dimension variance vector diag(Σ_i) associated with the emitting state, and the
transition probabilities."*

*(The word* metric *and the missing sentence break are the paper's own printing and are quoted as
printed. Carried to §7.1.)*

**★ SO THE PARAMETER SET PER CHORD, AS THE PAPER ITSELF ENUMERATES IT, IS: a 24-dimensional mean, a
24-dimensional diagonal variance, and the transition probabilities.** In the seven pages as read the
paper states no mixture, no full covariance and no duration distribution. Its §4.1 names Gaussian
mixtures as **future** work: *"we could try training with more model parameters, such as Gaussian
mixtures rather than single Gaussians."*

### §2.4 Training — EM with the chord sequence known and the timings hidden

**The paper's statement of what it does and does not require of its training data (§2.2).** *"If we knew
which state (i.e. chord) generated each observation in our training data, the model parameters could be
directly estimated. Hand-marked chord boundaries could provide the necessary information, but it is
extremely time-consuming to create these files. In our case, we assume only that the chord sequence of an
entire piece is known, but treat the chord labels of each frame as hidden values within the EM framework.
This frees the researcher from the laborious and problematic process of manual annotation."*

**The algorithm, as stated (§2.3).** The paper writes the complete-data likelihood `P(X,Q|Θ)` *"where X
represents the observed feature vectors, Q stands for the unknown chord labels, and Θ holds the current
model parameters"*, and gives equation (4) as
`E[logP(X,Q|Θ)] = Σ_Q P(Q|x,Θ_old) logP(X|Q,Θ)P(Q|Θ)`.

*(The lower-case* x *inside equation (4), where the observed feature vectors are* X *everywhere else, is
the paper's own printing. Carried to §7.1.)*

**What the paper claims for EM, in its own words:** *"EM guarantees that the estimates will improve at
each step, resulting in a locally optimal set of parameters, though not necessarily the globally optimal
solution. Thus, the EM solution reasonably estimates a set of parameters that maximizes the complete-data
likelihood, which implements the original MAP decision rule."* And the stopping rule: *"This process is
iterated until the expected improvement is no larger than some ε."*

**The specialisation to an HMM, and the object the constraint lives in.** *"The specific application of
EM to find maximum-likelihood parameter estimates for a hidden Markov model is known as the Baum-Welch,
or forward-backward, algorithm. The update equations derived from maximizing equation 4 amount to setting
model parameters to the sample averages of the training features, weighted by the posterior probability of
each feature being associated with each particular hidden label, p(q…|X,Θ_old,M), where M is the model
comprising the constraints on observations X, constructed by concatenating the states specified in the
known chord sequence into a single composite HMM for each song."*

**★ A FLAG INSIDE THAT QUOTATION, RECORDED RATHER THAN TRANSCRIBED WITH FALSE CONFIDENCE.** The symbol
elided above as `q…` carries **both a subscript n and a superscript t**, and at three openings of page 2
this read could not resolve which of the two sits where with certainty. **It is therefore not
transcribed**, and a reader who needs it should go to the page rather than to this file. **Nothing in
this file depends on the arrangement.**

**★ THAT LAST CLAUSE IS WHERE THE WHOLE DESIGN SITS: THE KNOWN CHORD SEQUENCE IS IMPOSED AS THE TOPOLOGY
OF A PER-SONG COMPOSITE MODEL**, so the sequence is a hard constraint and the boundaries are what the
training recovers.

### §2.5 Decoding — the two arms, boundaries-given and boundaries-and-labels-found

**Forced alignment, as stated (§2.4 continued on page 3).** *"in forced alignment, observations are
aligned to a composed HMM whose transitions are limited to those dictated by a specific chord sequence,
as in training i.e. only the chord-change times are being recovered, since the chord sequence is known."*

**Recognition, as stated.** *"In recognition, the HMM is unconstrained, in that any chord may follow any
other, subject only to the Markov constraints in the trained transition matrix."*

**Why the paper runs both, in its own words.** *"We perform both sets of experiments to demonstrate that
even when pure recognition performance is quite poor, a reasonable accuracy under forced alignments
indicates that the models have succeeded in learning the desired chord characteristics to some extent."*

**What the decode emits.** *"The output of the Viterbi algorithm is the single state-path labeling with
the highest likelihood given the model parameters. This best-path assigns a chord to every 100ms time
slice, resulting in a time-aligned song transcription."*

**How each arm's network is built at test time (§3).** *"In the case of alignment, the chord sequence file
is used to generate a simple composite HMM with allowable transitions determined by the song's
progression. Recognition must be able to accommodate any sequence drawn from the set of training song
chords. An appropriate chord loop is derived from the chord sequence files of all training songs. The
Viterbi algorithm will determine the best path in this chord network. Each PCP frame is assigned a chord
class such that the likelihood of the entire path is maximized."*

**★ THE TWO ARMS ARE THE PAPER'S OWN SEPARATION OF THE SEGMENTATION QUESTION FROM THE LABELLING
QUESTION**, and they are measured separately in Table 3. The paper commits the single best path in both
arms and publishes no alternative, no margin and no per-frame posterior.

### §2.6 The weighted averaging of rotated PCP vectors

This is the paper's one refinement of the trained models, and it is the change that moves its headline
figures.

**What it does, as stated (§2.5).** *"The outcome of the EM training is a set of model parameters
including means and variances in PCP feature space for each of the defined chord states. These values
define our initial chord models, however, an improvement can be made by calculating a weighted average of
the models for every chord family (major, minor, maj7 etc.) across all root chromas (A, A#, B, C, etc.).
This involves rotating the PCP vectors from each chroma until PCP[0] is the root pitch class, computing a
weighted average across all the chromas (weighted by frequency of chord occurrence), then un-rotating the
weighted average PCP vectors back to their original positions to construct new, regularized models for
each chord."*

**The arithmetic, as printed.** With *"f"* indexing chord families and *"c"* the *"numerical offset of
each chroma relative to A in quarter tones (e.g. A ↦ 0, A# ↦ 2, B ↦ 4 etc.)"*, equation (5) is
`μ̄_f[p] = ( Σ_c μ_{f,c}[(p−c) mod 24] · N_{f,c} ) / ( Σ_c N_{f,c} )`, *"where μ_{f,c} is the original
mean vector for one specific chord family/chroma combination, N_{f,c} is the number of frames assigned to
that state in the training data, and p indexes the 24 PCP bins."* Equation (6) puts the pooled family mean
back on each chord: `μ_{f̄,c}[p] = μ̄_f[(p + c) mod 24]`. The paper then adds, in one parenthesis,
*"(Variances are similarly pooled.)"*

**The paper's stated reasons.** *"The motivation is that by using values characteristic to the entire
family, a derived state model avoids overfitting its particular chord data. There is also the advantage of
increasing each individual chord's training set to the union of all chord family members. The results
below show that this simple approach gave very significant improvements."*

**When it runs, as stated (§3).** *"After all the training songs have been processed, the total set of
statistics is used to re-estimate the parameters of the individual chord models. At this point,
averaged-rotated PCP models are combined as described in section 2.5."* **So it is one act after
training, not a step inside the EM loop.**

**★ WHAT THIS MECHANISM IS, IN PLAIN TERMS, BECAUSE IT IS THE CHANGE THE PAPER'S OWN §3.1 CREDITS WITH
ITS LARGEST IMPROVEMENT:** it replaces each
chord's own learned template with the transposition of a single per-family template pooled over all
twenty-one roots, weighted by how many training frames each root received. It is a tying of parameters
across transposition — the assumption that a chord family's spectral signature is transposition-invariant
in pitch-class space.

### §2.7 The chord alphabet, and the system diagram

**The alphabet.** Table 2's caption reads *"Definition of the 147 possible chords that can appear as HMM
states. The label "X" is given to chords not covered by this set. In practice, only 32 labels occurred in
our data."* Its three rows are transcribed at §5.2.

**Where the labels come from.** *"The chord sequences for each song were produced by mapping the
progressions from a standard book of Beatles transcriptions (Paperback Song Series: The Beatles, 1995) to
a simpler set of chords as shown in table 2."*

**The system diagram.** Figure 1, captioned *"System Overview"*, draws the chain: Input Signal → STFT →
DFT frames (axis marked 11kHz at the top, 440Hz below it, 0 at the bottom) → normalized sum → PCP frames
(axis labelled A, A#, B, C, C#, D, D#, E, F, F#, G, G# from the bottom up) → EM → Chord Models (three
boxes, drawn as C, Am and E7) → Viterbi → Transcription / Alignment (drawn as the label run
`C C C C AmAmAm`).

---

## §3 — Coupling facts

The commission's §4 form makes these mandatory: what a source assumes of what comes before it, what it
hands to what comes after it, and the scope it claims for itself. They are given here at the paper's own
statements.

### §3.1 What it ASSUMES about its upstream

- **A waveform, not a score.** *"The songs were read from CD then downsampled and mixed into mono files
  at 11025 Hz sampling rate."* **At no point the seven pages describe does anything symbolic enter the
  system except the chord-label sequences themselves.**
- **A chord sequence per training song, WITHOUT timings.** This is the paper's central upstream
  assumption and the thing its design is built to exploit: *"we assume only that the chord sequence of an
  entire piece is known, but treat the chord labels of each frame as hidden values within the EM
  framework."*
- **That the chord sequence is a sequence of discrete, non-overlapping symbols**, which is the analogy's
  own premise: *"the sequence of discrete, non-overlapping chord symbols used to describe a piece of
  music."*
- **A published transcription as the source of those sequences**, reduced to the paper's own alphabet:
  the Paperback Song Series book *"mapp[ed] … to a simpler set of chords as shown in table 2."* The
  mapping itself is not printed.
- **Hand-marked chord BOUNDARIES for the test songs only**, produced with a named tool: *"for these songs
  the actual chord boundaries were hand-labeled using WaveSurfer; this provided the ground-truth used to
  determine frame error rates."*
- **A reference frequency for the pitch mapping**: *"a subsequent PCP mapping using reference frequency
  440 Hz (A4)."*

**★ THE ASYMMETRY IN THAT LIST IS THE POINT OF THE PAPER.** Training needs a chord SEQUENCE and no
timings; evaluation needs TIMINGS, and the paper pays for them by hand on two songs.

### §3.2 What it HANDS downstream

- **One chord label per 100 ms frame, for a whole song**, from a single committed Viterbi path — *"This
  best-path assigns a chord to every 100ms time slice, resulting in a time-aligned song transcription."*
- **Two kinds of output from the same machinery**: a boundary alignment of a chord sequence already
  known, and a recognised chord sequence — *"the Viterbi algorithm is applied to generate either a
  boundary alignment of an existing chord sequence or recognize a new chord sequence."*
- **Trained per-chord models** — a 24-dimensional mean and a 24-dimensional diagonal variance per chord,
  plus a transition matrix — and, after §2.5, **a pooled per-family template** whose plot is Figure 3.

**★ WHAT IT DOES NOT HAND DOWNSTREAM, STATED BECAUSE A CONSUMER WOULD LOOK FOR IT.** In the pages as
read the system publishes no ranked alternative, no per-frame posterior or likelihood, no confidence of
any kind, no key, no Roman numeral, no inversion, no bass note and no segment-duration model. The output
is a label per frame.

### §3.3 Its own STATED scope and limits

- **The corpus is twenty songs from three early Beatles albums**, of which two are the test set (Table 1,
  transcribed at §5.1).
- **The implementation is a speech toolkit**: *"The Hidden Markov Model Toolkit (Young et al., 1997) was
  used to implement our chord recognition system."*
- **The paper's own verdict on the recognition arm, from §5:** *"Although recognition accuracy is not yet
  sufficient to provide usable chord transcriptions of unknown audio, the ability to find time alignments
  for known chord progressions may be useful in itself."*
- **The paper's own statement of what the whole result shows, from §5:** *"Our experiments show that HMM
  models trained by EM on PCP features can successfully recognize chords in unstructured, polyphonic,
  multi-timbre audio."*
- **Its own named frequency-resolution limit (§4.1):** *"our recognition system most likely does not have
  enough frequency resolution … This issue is particularly serious at low frequencies, when the spacing of
  adjacent FFT bins becomes greater than one quarter-tone. Currently we assign all energy in these low bins
  to a single chroma, but better results might be obtained by spreading it across several PCP dimensions in
  proportion to their overlap with the FFT bin frequency range."*
- **Its own named data limit (§4.1):** *"a larger and more diverse collection of training data should also
  improve accuracy and applicability of the system. The most significant obstacle to obtaining this data is
  finding a reliable source for the associated chord sequences."*
- **Its own named tuning limit (§4.1):** *"One argument for using 24-dimensional PCP vectors was to
  accommodate slight variations in tuning."* The paper's proposal is *"to estimate the precise tuning used
  in a particular song, and center the PCP feature definition accordingly."*

  *(★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "and cent[ering] the PCP feature
  definition accordingly". **The paper prints* "and center"*, and the bracketed inflection altered a word
  inside a quotation** — which is the defect class this line reports of other reads, made here.)*

---

## §4 — Claims, labeled

Each load-bearing claim of the paper is labeled by what supports it **inside this paper**: **FACT** where
the paper states a measurement of its own and prints it; **THEORY** where it rests on established
published work it cites; **CONJECTURE** where the paper asserts or proposes without a measurement here.
**The labels are about this paper's own support for its own claims**, and they are not verdicts on
whether the claim is true.

1. **FACT** — Averaged-rotated PCP models reach 68.8 % and 83.3 % frame accuracy on the two test songs
   under forced alignment with the train18 models (Table 3, §5.3).
2. **FACT** — The same models reach 23.3 % and 20.1 % under recognition with train18 (Table 3). **The
   alignment-against-recognition gap is the paper's own measured separation of the two arms.**
3. **FACT** — Averaged-rotated PCP beats every MFCC configuration and the base PCP configuration at every
   cell of Table 3 except those of recognition trained on train20, which the paper names as its exception
   (§5, and checked at §6.6).
4. **FACT** — Forced alignment scores above recognition at every one of Table 3's twenty comparable pairs
   (checked at §6.5; the paper states it as *"Forced alignment always outperforms recognition"*).
5. **FACT** — The base PCP configuration gains from including the test songs in training and the
   averaged-rotated one does not; the paper reads the second as evidence of not overfitting: *"if including
   the test data in the training set does not significantly increase performance, we can at least be
   confident that the models are not overfitting the data."*
6. **THEORY** — That EM/Baum-Welch converges to a locally optimal parameter set, and that the forward-
   backward update has the stated form. Cited to Gold and Morgan (1999).
7. **THEORY** — That the pitch class profile is a usable harmonic representation of audio. Cited to
   Fujishima (1999) and to Bartsch and Wakefield (2001), and the paper states the assumption in terms:
   *"The assumption is that this representation captures harmonic information in a more meaningful way,
   thereby facilitating chord recognition."*
8. **THEORY** — That the speech-recognition framework transfers with *"minimal modification"* once the
   chord-word analogy is granted. The transfer is argued, and the implementation with a speech toolkit is
   the paper's demonstration of it.
9. **CONJECTURE** — That a chord family's PCP signature is transposition-invariant, so that one pooled
   template rotated to each root is a better model than each root's own. **The paper argues it from
   overfitting and training-set size and measures its EFFECT (Table 3), not its premise.**
10. **CONJECTURE** — That the major/minor confusion is caused by insufficient frequency resolution, and
    that a longer window would reduce it: *"Better discrimination of these chords might be achieved by
    increasing the system's frequency resolution."* **No measurement of this is reported, and §6.10 sets
    out what the paper's own numbers say about where that limit bites.**
11. **CONJECTURE** — That the drop of recognition on *"Every Little Thing"* under train20 *"may reflect
    some pathological case in the local maximum found by EM."* The paper's own hedge is in the sentence.
12. **CONJECTURE** — Every item of §4's future work: Gaussian mixtures, a longer Hanning window, adaptive
    tuning, and autocorrelation-based features. Each is proposed and none is measured here.

---

## §5 — Measured results, with corpus, measure and value as the paper states them

Every value below is transcribed from the page image. Nothing in this section is computed; the arithmetic
this read performed is kept apart, in §6, so that a later reader can tell the two apart at a glance.

### §5.1 The corpus, transcribed from Table 1

Table 1's caption: *"Corpus of 20 early Beatles songs used in the experiments."* Its three columns are
Album, Song and Set.

| Album | Song | Set |
|---|---|---|
| Beatles for Sale | Eight days a week | test |
| | Every little thing | test |
| | I don't want to spoil the party | train |
| | I'll follow the sun | train |
| | I'm a loser | train |
| Help | Help | train |
| | I've just seen a face | train |
| | It's only love | train |
| | Ticket to ride | train |
| | Yesterday | train |
| | You're going to lose that girl | train |
| | You've got to hide your love away | train |
| A Hard Day's Night | A hard day's night | train |
| | And I love her | train |
| | Can't buy me love | train |
| | I should've known better | train |
| | I'm happy just to dance with you | train |
| | If I fell | train |
| | Tell me why | train |
| | Things we said today | train |

*(Song titles are given in the table's own capitalisation.)*

### §5.2 The chord alphabet, transcribed from Table 2

Caption: *"Definition of the 147 possible chords that can appear as HMM states. The label "X" is given to
chords not covered by this set. In practice, only 32 labels occurred in our data."*

| | |
|---|---|
| **Chord families** | maj, min, maj7, min7, dom7, aug, dim |
| **Roots** | A♭, B♭, C♭, D♭, E♭, F♭, G♭, A, B, C, D, E, F, G, A♯, B♯, C♯, D♯, E♯, F♯, G♯ |
| **Examples** | Amaj, C♯min7, G♭dom7 |

### §5.3 Table 3, transcribed

Caption: *"Percent Frame Accuracy results. Within each row, the first subrow refers to "Eight Days a
Week" and second subrow to "Every Little Thing". Columns show the frame accuracy for forced alignment and
recognition, using the train18 (excluding test cases) and train20 (including test cases) sets."*

| Feature | Test song | Align, train18 | Align, train20 | Recog, train18 | Recog, train20 |
|---|---|---|---|---|---|
| MFCC | Eight Days a Week | 27.0 | 20.9 | 5.9 | 16.7 |
| MFCC | Every Little Thing | 14.5 | 23.0 | 7.7 | 19.6 |
| MFCC_D | Eight Days a Week | 24.1 | 13.1 | 15.8 | 7.6 |
| MFCC_D | Every Little Thing | 19.9 | 19.7 | 1.5 | 6.9 |
| MFCC_0_D_A | Eight Days a Week | 13.9 | 11.0 | 2.2 | 3.8 |
| MFCC_0_D_A | Every Little Thing | 9.2 | 12.3 | 1.3 | 2.5 |
| PCP | Eight Days a Week | 26.3 | 41.0 | 10.0 | 23.6 |
| PCP | Every Little Thing | 46.2 | 53.7 | 18.2 | 26.4 |
| PCP_ROT | Eight Days a Week | 68.8 | 68.3 | 23.3 | 23.1 |
| PCP_ROT | Every Little Thing | 83.3 | **83.5 — SEE THE FLAG BELOW** | 20.1 | 13.1 |

*(The test-song column is not printed as a column in the paper; it renders the caption's own subrow rule,
and no value is moved by rendering it that way.)*

**★ A FLAG ON ONE CELL, ADDED AT THE CROSS-CHECK (STEP 7) AND UNRESOLVED.** **This read transcribes the
PCP_ROT / forced alignment / train20 / "Every Little Thing" cell as 83.5, at three separate openings of
page 4. The first extract of this row transcribes it as 83.0, at two separate readings of the same
image.** **The paper's prose settles neither digit** — see §9.3, where the attempt to settle it is set
out — **so the cell is recorded as carrying two readings, and no figure in this file rests on it without
saying so.** Every other cell of Table 3 is transcribed identically by both reads.

**★ THE TWO FIGURES THE CANDIDACY ROW NAMES ARE HERE, AND THEY ARE IN ONE ROW:** 68.8 is PCP_ROT, forced
alignment, train18, "Eight Days a Week"; 23.3 is PCP_ROT, recognition, train18, the same song. **So
DP-C's "68.8-against-23.3" is a same-feature, same-training-set, same-song pair separated only by which
arm ran** — which is what makes it a statement about boundaries-given against boundaries-and-labels-found
rather than about two different systems. *(That the record's row says so is read at the candidacy file;
what is established HERE is only that the paper prints both values in that one position.)*

### §5.4 Table 4, transcribed

Caption: *"Confusion matrices for recognition of "Eight Days a Week", PCP_ROT, train18. Enharmonic
equivalent chords have been combined."* Six matrices are printed, headed *"A MAJOR"*, *"D MAJOR"*, *"G
MAJOR"*, *"B MINOR"*, *"E MAJOR"* and *"X CHORD"*, each subtitled *"Eight Days a Week"*. Every matrix has
the seven columns Maj, Min, Maj7, Min7, Dom7, Aug, Dim and twelve rows of root names; each matrix's rows
begin at its own root and run upward through the chromatic circle, except the X matrix, whose rows begin
at A.

**Only the cells carrying a legible digit string are transcribed. Every other cell is either blank or
carries a small centred dot, and the paper does not say what the dot means; both are treated here as
carrying no count, and §6.1 is what tests that treatment.**

**"A MAJOR"** — A: Maj 4, Min 17, Dom7 49 · D: Min 3 · E/F♭: Maj 17, Min 5, Dom7 1 · E♯/F: Maj 1 ·
F♯/G♭: Min 9

**"D MAJOR"** — D: Maj 30, Min 119, Min7 5, Dom7 49 · E/F♭: Maj 18, Min 34, Min7 41 · E♯/F: Maj 7 ·
F♯/G♭: Min 42, Maj7 15 · A: Maj 19, Min 6, Dom7 76 · A♯/B♭: Min7 52 · B/C♭: Min 20 · C♯/D♭: Maj 1

**"G MAJOR"** — G: Maj 122, Min 35 · A: Maj 11 · B/C♭: Min 24, Maj7 3 · D: Maj 13, Min 17, Min7 2,
Dom7 1 · E/F♭: Maj 1, Min 104, Maj7 26 · F♯/G♭: Min 12

**"B MINOR"** — B/C♭: Min 72 · D: Min 3 · E/F♭: Maj 8, Min 51, Min7 41 · E♯/F: Maj 3, Min 3 · F♯/G♭:
Min 12, Maj7 6 · G: Maj 2 · A: Dom7 1 · A♯/B♭: Min 9

**"E MAJOR"** — E/F♭: Maj 158, Min 115, Min7 9 · E♯/F: Maj 9 · F♯/G♭: Maj7 11 · G: Maj 3 · A: Maj 9,
Dom7 1 · B/C♭: Maj 8 · C♯/D♭: Min 20 · D: Min 14

**"X CHORD"** — A: Maj 19 · B/C♭: Min 21 · D: Min 35 · F♯/G♭: Maj7 1

**How the matrices are oriented, read from the cells rather than from a statement.** The paper does not
state the orientation. Each matrix is headed by one chord; its cells give a root (the row) and a family
(the column). **The reading this file uses is that the heading names the ground-truth chord and the cells
name what the recogniser produced**, so that the cell at the heading's own root and family is the correct
one. *(That reading is not taken on plausibility: §6.1 tests it against Table 3's own printed value, and
it holds.)*

**The X matrix has no X column — and neither has any other matrix, because the columns are the seven
chord FAMILIES and the rows the twelve root classes, and *"X"* is neither.** **So the table's layout holds
no cell in which an X OUTPUT could be shown at all.** What the table therefore shows is X as one of the
labels the authors' own hand annotation uses — §3.2's *"which we label with only 5 chords plus "X""* —
and **it shows nothing either way about whether the system can emit X.** §7.2 carries that as an open
question.

*(★ NARROWED AT THE CROSS-CHECK. FORMER WORDING, PRESERVED (#12): "**The X matrix has no X column.** So a
frame whose ground truth is *"X"* — a chord outside the 147 — **cannot be labelled correctly by this
system as the table is printed**." **The layout is what excludes an X cell, not a property of the
system**, and the former sentence read as a statement about the system. The correction was forced by
comparing this passage against the first extract's opposite claim — §9.4(c).)*

### §5.5 The two figures, as read

**Figure 1** is described at §2.7.

**Figure 2**, captioned *"Illustration of PCP features vectors, ground truth labels, forced alignment
output, and recognition output, for a brief segment of "Eight Days a Week""*, is titled on the plot
*"Beatles - Beatles For Sale - Eight Days a Week (4096pt)"*. Its horizontal axis is labelled *"time /
sec"* and runs **from 16.27 to 24.84**. Its vertical axis is labelled *"pitch class"* and is ticked A, ♯,
B, C, ♯, D, ♯, E, F, ♯, G, ♯ from the bottom up. An intensity scale to its right is ticked 0, 20, 40, 60,
80, 100, 120 and labelled *"intensity"*. Beneath the plot are three label rows: **true** — E, G, D, Bm,
G; **align** — E, G, D, Bm, G; **recog** — E, G, Bm, Am, Em7, Bm, Em7.

**Figure 3**, captioned *"Mean vectors for the PCP_ROT average chord family templates"*, is titled on the
plot *"PCP_ROT family model means (train18)"*. Its horizontal axis runs from 0 to 25 and its vertical axis
from 0 to 0.4. Its legend carries five entries: **DIM, DOM7, MAJ, MIN, MIN7**.

**★ A NOTE ON FIGURE 3'S LEGEND, RECORDED BECAUSE IT IS A COUNT THAT DOES NOT MATCH.** Table 2 defines
**seven** chord families; Figure 3's legend names **five** of them, and **maj7 and aug are not among the
five**. The paper does not say why, and this read proposes nothing about it.

### §5.6 The protocol constants, as stated

| Quantity | Value, as the paper prints it | Where |
|---|---|---|
| Sampling rate | 11025 Hz | §2.1 and §3 |
| STFT frame length | N = 4096 points | §2.1 |
| Window | N-point Hanning | §2.1; §3 gives *"a STFT of Hanning length 4096"* |
| PCP dimensions | 24 | §2.1 |
| Frame step | 100 ms, *"or 10 PCP frames per second"* | §2.1 |
| Reference frequency | 440 Hz (A4) | §3 |
| Emission | a single Gaussian, diagonal covariance | §2.2 |
| EM iterations | *"EM proceeds for 13 to 15 iterations."* | §3 |
| EM stopping rule | *"until the expected improvement is no larger than some ε"* — ε is not given a value | §2.3 |
| Initialisation | *"HMM state chord models were initialized with global mean and variance values from the entire dataset (so called flat-start EM initialization)"*, after *"the uniform segmentation and chord labeling of every training song"* | §3 |
| Training sets | train18 (*"excluding test cases"*) and train20 (*"including test cases"*) | Table 3's caption; §3 |
| Toolkit | HTK, the Hidden Markov Model Toolkit (Young et al., 1997) | §3 |
| Test ground truth | chord boundaries hand-labelled with WaveSurfer, on the two test songs | §3 |

### §5.7 The reference list, transcribed

Bartsch, M. A. and Wakefield, G. H. (2001). *To catch a chorus: Using chroma-based representations for
audio thumbnailing.* In Proc. IEEE Workshop on Applications of Signal Processing to Audio and Acoustics,
Mohonk, New York. · Fujishima, T. (1999). *Realtime chord recognition of musical sound: A system using
common lisp music.* In Proc. ICMC, pages 464–467, Beijing. · Gold, B. and Morgan, N. (1999). *Speech and
Audio Signal Processing: Processing and Perception of Speech and Music.* John Wiley & Sons, Inc. · Logan,
B. (2000). *Mel frequency cepstral coefficients for music mode ling.* In Proc. Int. Symposium on Music
Inform. Retriev. (ISMIR), Plymouth. · *Paperback Song Series: The Beatles* (1995). Hal Leonard
Corporation. · Raphael, C. (2002). *Automatic transcription of piano music.* In Proc. Int. Symposium on
Music Inform. Retriev. (ISMIR), Paris. · Young, S., Odell, J., Ollason, D., Valtchev, V., and Woodland, P.
(1997). *HTK Hidden Markov Model Toolkit.* Entropic Research Laboratories Inc., Cambridge University.

*(The line break inside* "mode ling" *is the paper's own and is quoted as printed.)*

---

## §6 — Arithmetic this read performed on the paper's own printed values

**Nothing in this section is a value the paper prints.** Every figure here is computed from §5's
transcriptions, and each item says what it establishes and what it does not.

### §6.1 ★ TABLE 3's 23.3 IS AN ACCURACY AND NOT AN ERROR RATE, ESTABLISHED FROM TABLE 4

**Why the question arises.** Table 3's caption says *"Percent Frame Accuracy results"*, and the body twice
says the opposite kind of quantity was computed: *"this provided the ground-truth used to determine frame
**error** rates"* (§3) and *"we can calculate the frame **error** rate"* (§3). **A later reader lifting
23.3 out of this paper needs to know which of the two it is**, and the two differ by 53.4 points.

**The arithmetic that settles it.** Table 4 is the confusion of exactly the configuration Table 3's
PCP_ROT / recognition / train18 / first subrow reports: *"recognition of "Eight Days a Week", PCP_ROT,
train18"*. Summing every legible cell of its six matrices gives **1,655 frames**, made up per matrix as
106 + 534 + 371 + 211 + 357 + 76. The cells lying at each matrix's own root and family — the correct
labels — are A major 4, D major 30, G major 122, B minor 72 and E major 158, **386 frames**; the X matrix
has no X column and contributes none.

**386 / 1,655 = 23.32 %**, which prints as **23.3**, the value in Table 3's cell. The complement, 1,269
frames off the diagonal, is **76.68 %**. **So Table 3 reports ACCURACY**: under the error-rate reading,
23.3 would make 1,269 frames correct, and 1,269 is exactly the count of the frames that carry a label
other than the ground truth.

**★ AND THE SAME ARITHMETIC SETTLES A SECOND QUESTION THE PAPER DOES NOT ADDRESS: THE FRAMES WHOSE GROUND
TRUTH IS "X" ARE IN THE DENOMINATOR, AND CAN NEVER BE CORRECT.** Excluding the X matrix's 76 frames gives
386 / 1,579 = **24.45 %**, which prints as 24.4 and is not the value in the cell. So the 4.6 % of this
song that falls outside the 147-chord alphabet is counted against the system.

**★ AND THE PAPER'S OWN SENTENCE SAYS THE DENOMINATOR IS THE WHOLE SONG**, which this read did not rely
on for the arithmetic above but which agrees with it: §3.2 says *"Table 4 presents the confusion matrices
for every frame in "Eight Days a Week"."*

**What this establishes, stated exactly.** Three things at once, and they hold each other up: that Table
3's figures are accuracies; that Table 4's matrices are oriented ground-truth-by-output as §5.4 reads
them; and that this read's cell-by-cell transcription of Table 4 is very unlikely to carry a mis-read
digit, since a mis-read digit would have to leave a 1,655-frame total still agreeing with an
independently printed percentage to three significant figures. **What it does NOT establish:** anything
about the second test song, whose confusion is not printed; or that the dot-marked cells carry no count —
it makes that treatment the one consistent with Table 3, which is weaker than reading the dots.

*(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "that this read's cell-by-cell transcription
of Table 4 **is right**, since a mis-read digit **would not** leave a 1,655-frame total agreeing…". A
coincidence is improbable, not impossible — two compensating mis-reads would survive the check — so the
claim is stated at the strength the argument carries.)*

### §6.2 The frame count and the playing time of "Eight Days a Week", derived

At the paper's own *"10 PCP frames per second"*, the 1,655 frames of §6.1 are **165.5 seconds, or 2
minutes 45.5 seconds**. **The paper prints no song duration and no frame count anywhere**, so both
figures are this read's and are flagged as derived. Nothing outside the paper was consulted to check
them.

### §6.3 The chord alphabet closes, in two independent ways

**Seven families × twenty-one roots = 147**, which is the number Table 2's caption states. The root list
transcribed at §5.2 is seven flats, seven naturals and seven sharps.

**And the twenty-one spellings collapse to exactly the twelve rows Table 4 prints.** Table 4's caption
says *"Enharmonic equivalent chords have been combined"*, and its rows are A, A♯/B♭, B/C♭, B♯/C, C♯/D♭,
D, D♯/E♭, E/F♭, E♯/F, F♯/G♭, G, G♯/A♭. Counting the spellings those twelve rows carry — three of them
single (A, D, G) and nine paired — gives 3 + 18 = **21**, every one of Table 2's roots and no other.
**Both checks PASS.**

### §6.4 The corpus counts close

Table 1 lists **5 + 7 + 8 = 20** songs, of which **2** are marked test and **18** train. That is the
*"Twenty songs from three early Beatles albums"* of §3 and the two training sets the paper names
**train18** and **train20**. **The check PASSES**, and the set names are the counts.

### §6.5 Forced alignment scores above recognition at every one of Table 3's twenty pairs

The paper states it: *"Forced alignment always outperforms recognition."* Table 3 holds five features ×
two test songs × two training sets = **twenty positions at which an alignment figure and a recognition
figure stand for the same configuration**. Every one of the twenty has the alignment figure the higher.
**The check PASSES**, and **the narrowest margin is 3.4 points** — MFCC, train20, "Every Little Thing",
where alignment is 23.0 and recognition 19.6.

### §6.6 ★ ONE OF THE PAPER'S TWO EXCEPTION CLAUSES IS EXACT AND THE OTHER IS REFUTED BY A CELL IT DOES NOT NAME

**The first clause, refuted.** §3.1 says *"models trained using the base PCP features perform better than
models trained using MFCCs in all cases except one (recognition of the first test example using MFCC_D
and train18)"*. Comparing the PCP row against each of the three MFCC rows at all eight positions gives
twenty-four comparisons, and **PCP loses TWO of them, not one**:

- **recognition, train18, "Eight Days a Week": MFCC_D 15.8 against PCP 10.0** — the exception the paper
  names.
- **forced alignment, train18, "Eight Days a Week": MFCC 27.0 against PCP 26.3** — **a second exception,
  which the sentence does not name and which its "all cases except one" excludes.**

**So the clause as printed is false of the paper's own table**, by a margin of 0.7 points at one cell. *No
value moves, and no other sentence read here restates the claim:* the comparison the abstract rests on is
the one below, which holds.

*(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "no other sentence **of the paper** depends
on it" — an unbounded negative over a dependency this read never traced.)*

**The second clause, exact.** §3.1 says PCP_ROT *"outperform[s] all MFCC-trained ones, as well as the base
PCP models in all cases except, curiously, recognition based on train20."* PCP_ROT is compared here
against all four other feature rows at all eight positions — thirty-two comparisons — and **it loses
exactly three**: against MFCC at recognition/train20/"Every Little Thing" (19.6 against 13.1), and against
base PCP at both of recognition/train20 (23.6 against 23.1, and 26.4 against 13.1). **All three lie inside
the one condition the clause names.** **The check PASSES**, and it passes in the stronger reading — the
exception covers the MFCC comparison as well as the PCP one, which a reader could easily take to apply
only to the second.

### §6.7 The "four times better" claim, located at its cell

§3.1 ends *"with the PCP_ROT models performing as much a four times better than the best MFCC
counterparts."* Taking the best MFCC-family figure at each of the eight positions and dividing the
PCP_ROT figure by it gives ratios of 2.55, 4.19, 3.27, 3.63, 1.47, 2.61, 1.38 and 0.67. **The claim is a
maximum and it is reached at one position: forced alignment, train18, "Every Little Thing", where 83.3
against MFCC_D's 19.9 is a factor of 4.19.** At the other end of the same eight, **the ratio falls below
one** — recognition, train20, "Every Little Thing", where PCP_ROT's 13.1 is 0.67 of MFCC's 19.6, the cell
§6.6's second clause already names.

*(★ ONE OF THE EIGHT RATIOS RESTS ON THE FLAGGED CELL (§5.3): the 3.63 is 83.5 ÷ 23.0, and on the first
extract's reading of that cell it would be 3.61. **The claim this section is about — the maximum — is at a
different position and does not move.**)*

*(The missing letter in* "as much a four times" *is the paper's own printing. Carried to §7.1.)*

### §6.8 ★ THE ABSTRACT'S "AROUND 75%" IS NOT A VALUE THE PAPER PRINTS ANYWHERE — DERIVED HERE, AND FLAGGED AS DERIVED

The abstract says *"Our results on a small set of 20 early Beatles songs show frame-level accuracy of
around 75% on a forced-alignment task."* **No cell of Table 3 holds 75, and the paper states no
averaging rule.** The two readings that land there are the unweighted mean of the PCP_ROT forced-alignment
pair: **(68.8 + 83.3) / 2 = 76.05** for train18, and **(68.3 + 83.5) / 2 = 75.9** for train20.

*(★ THE TRAIN20 MEAN RESTS ON THE FLAGGED CELL (§5.3); on the first extract's reading of it the train20
mean is (68.3 + 83.0) / 2 = **75.65**. **The train18 mean, 76.05, rests on no flagged cell, and both reads
derive it independently and agree** — §9.5.)*

**A frame-weighted mean cannot be computed from the paper**, because only one test song's frame count is
recoverable (§6.2) and *"Every Little Thing"*'s is printed nowhere. **So which of the two the abstract
means, and whether it means a weighted figure at all, is not settled by the pages as read**, and a later
reader who needs the headline number should take the cell rather than the abstract.

### §6.9 The analysis window, the hop and the bin spacing, derived

From the paper's own constants — N = 4096 points at f_sr = 11025 Hz — the analysis window is
**4096 / 11025 = 371.5 ms** and the DFT bin spacing is **11025 / 4096 = 2.692 Hz**. Against the stated
100 ms step, consecutive windows overlap by **271.5 ms, or 73 %** of the window. **The paper prints none
of these three figures**; all are this read's.

**Why they are worth deriving:** the window is nearly four times the hop, so each 100 ms label in the
system's output is decided on a spectrum that draws on roughly 370 ms of audio. **A chord boundary is
therefore smeared across about three or four output frames by the front end alone**, before any model
sees it — which bears directly on a measure whose unit is the 100 ms frame. *(That consequence is this
read's reasoning from the two printed constants, not a statement of the paper's.)*

### §6.10 ★ WHERE THE PAPER'S OWN FREQUENCY-RESOLUTION LIMIT ACTUALLY BITES, ON ITS OWN CONSTANTS

§4.1 names the limit in terms of bin spacing: *"This issue is particularly serious at low frequencies,
when the spacing of adjacent FFT bins becomes greater than one quarter-tone."*

**On the paper's own criterion.** A quarter-tone step at frequency *f* spans *f* × (2^(1/24) − 1) = *f* ×
0.02930. Setting that equal to the 2.692 Hz bin spacing gives **f ≈ 91.9 Hz** — so the regime §4.1
describes is **below about 92 Hz, which is just under F♯2**. The same arithmetic for a **semitone** —
*f* × (2^(1/12) − 1) = *f* × 0.05946 — gives **f ≈ 45.3 Hz**, just under F♯1. **So on the bin-spacing
criterion the paper states, a semitone is separated at every pitch above roughly F♯1.**

**★ AND THE PAPER'S OWN CRITERION UNDERSTATES ITS OWN LIMIT, BY ESTABLISHED THEORY IT DOES NOT INVOKE.**
Bin spacing is the sampling of the spectrum, not its resolution: for the Hanning window the paper
specifies, the main lobe of the window transform is **four bins wide**, so two partials are separated only
when they lie about **4 × 2.692 = 10.77 Hz** apart. Repeating both calculations against that figure moves
the quarter-tone limit to **f ≈ 367 Hz — just under F♯4** — and the semitone limit to **f ≈ 181 Hz,
between F3 and F♯3**.

**What that means for the paper's claim 10, stated carefully.** §3.2 attributes the major/minor confusion
to frequency resolution, and §4.1 proposes a longer window as the remedy. **On the bin-spacing criterion
the paper itself uses, that explanation would reach only the bass register.** **On the main-lobe
criterion it reaches much of the register in which the thirds of these chords sound**, and the remedy
§4.1 names — doubling the Hanning length to 8192 — would halve both limits, to about 184 Hz and 91 Hz.
**So the paper's conjecture is better supported than its own stated criterion makes it look: the
criterion understates the limit it is offered as, and the conjecture is not weakened by the arithmetic.**

**The bound, which is the part that matters.** The four-bin main-lobe width is standard theory about the
Hanning window and is not measured here; nothing in this read measures the system's actual discrimination
of a major from a minor third; and **no arithmetic here separates this mechanism from the others that
could produce the same confusion** — harmonics of other chord tones landing on the third's bins, the
pooling of §2.5 across roots, or the flat-start EM initialisation. **This is an observation about the
paper's own criterion, not a diagnosis of its system.**

### §6.11 ★ THE AGGREGATE 23.3 HIDES A RANGE FROM 0 % TO 44 %, AND THE PAPER PRINTS ONLY THE AGGREGATE

Table 4's six matrices carry, per ground-truth chord, both how much of the song it covers and how much of
it the recogniser got right. Neither split is printed; both follow from §5.4's cells.

| Ground-truth chord | Frames | Share of the song | Correct | Accuracy on that chord |
|---|---|---|---|---|
| A major | 106 | 6.4 % | 4 | **3.8 %** |
| D major | 534 | 32.3 % | 30 | **5.6 %** |
| G major | 371 | 22.4 % | 122 | **32.9 %** |
| B minor | 211 | 12.7 % | 72 | **34.1 %** |
| E major | 357 | 21.6 % | 158 | **44.3 %** |
| X | 76 | 4.6 % | 0 | **0 %** |
| **All** | **1,655** | **100 %** | **386** | **23.3 %** |

**So the chord the system handles worst of the five is also the one covering the largest share of the
song** — D major, 32.3 % of the frames at 5.6 % accuracy — and the reported 23.3 is not representative of
any one of the six. *(Derived from §5.4; the paper states none of it.)*

### §6.12 The major/minor confusion, at the cells, is stronger than "frequent" at two of the four majors

§3.2 says *"Notice the frequent confusion between major chords and their minor version, which differ only
by the semitone between the major and minor third intervals."* At each major matrix, setting the
same-root minor cell beside the correct same-root major cell:

| Matrix | Correct, same-root major | Same-root minor | Which is larger |
|---|---|---|---|
| A major | 4 | 17 | **the minor, by more than four times** |
| D major | 30 | 119 | **the minor, by nearly four times** |
| G major | 122 | 35 | the correct reading |
| E major | 158 | 115 | the correct reading |

**At two of the four major matrices the same-root MINOR is the majority reading of the chord** — the
system's commonest answer for that chord is its parallel minor. The paper's word is *frequent*, and it
does not say this. **And the confusion runs one way in this data as printed:** the B minor matrix's own
root row carries a minor count and no major count at all, so no B-minor frame was read as B major.

*(Bound: this is one song, one feature configuration and one training set — the only confusion the paper
prints.)*

### §6.13 Figure 2's segment closes against its own caption

Figure 2's time axis runs 16.27 to 24.84 seconds, a span of **8.57 seconds beginning 16.27 seconds into
the song**; §3.4 describes it as *"an eight-second segment of the song "Eight Days a Week" taken about 16
seconds into the song."* **The check PASSES.** At 10 frames per second the segment is about 86 frames,
which the paper does not print.

### §6.14 All five feature configurations do come to twenty-four dimensions, as §3 claims

§3 states the constraint: *"In each case, the total model dimensions were kept at 24 to match the number
of parameters in the PCP systems."* The three cepstral configurations are described separately and the
arithmetic is left to the reader:

- **MFCC** — *"we used 24 MFCCs"* → 24.
- **MFCC_D** — *"just 12 MFCCs but included their deltas"* → 12 + 12 = 24.
- **MFCC_0_D_A** — *"7th order MFCCs including the c₀ (average log energy) term, along with deltas and
  accelerations for each dimension"* → (7 + 1) × 3 = 24.
- **PCP** and **PCP_ROT** — *"both in 24 dimensions"* → 24.

**All five reach 24, so the check PASSES** and the comparison in Table 3 holds the parameter count fixed
across every row. *(The three cepstral sums are this read's; the paper prints the constraint and the
ingredients, and not the arithmetic.)*

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

Named rather than counted. **None of them moves a measured value of the paper**, except the first, which
is a claim about the values rather than a value.

- **★ A COMPARISON CLAIM REFUTED BY THE PAPER'S OWN TABLE.** §3.1's *"in all cases except one"* for base
  PCP against MFCC is false at a second cell the sentence does not name — forced alignment, train18,
  "Eight Days a Week", MFCC 27.0 against PCP 26.3. Established at §6.6. **This is the one item here that
  a later reader could carry as a wrong statement of fact**, and the margin at that cell is 0.7 points.
- **A TEXT AND AN EQUATION THAT DEFINE THE SAME QUANTITY DIFFERENTLY.** §2.1's sentence computes each PCP
  element by *"summing the magnitude"* of the contributing bins; equation (3) sums `|X[k]|²`, which is
  power. **Magnitude and power are different quantities**, and which the implementation used is not
  settled by the pages as read. The choice is not cosmetic: it changes the relative weight of strong and
  weak partials inside a chroma bin, and so the shape of the templates Figure 3 plots.
- **A HEADLINE FIGURE THAT IS PRINTED NOWHERE IN THE BODY.** The abstract's *"around 75%"* matches no
  cell and rests on an averaging rule the paper does not state (§6.8).
- **THE MEASURE IS NAMED TWO WAYS.** Table 3's caption says *"Percent Frame Accuracy"*; §3 twice says the
  quantity computed is the *"frame error rate"*. §6.1 settles which the table holds, by arithmetic on
  Table 4; **the paper itself does not.**
- **A WORD USED IN A SENSE OPPOSITE TO ITS MUSICAL ONE, IN A PAPER ABOUT POLYPHONY.** §2.1 opens
  *"Monophonic music recordings x[n] sampled at 11025 Hz"*, where §5 describes the subject as
  *"unstructured, polyphonic, multi-timbre audio"*. **The intended sense is the channel count**, settled
  at §3's *"downsampled and mixed into mono files"* — but the sentence as printed says the music is
  monophonic, which is what the whole paper is about not being.
- **A COUNT IN A FIGURE THAT DOES NOT MATCH THE ALPHABET.** Table 2 defines seven chord families; Figure
  3's legend plots five, omitting maj7 and aug, with no statement of why (§5.5).
- **PRINTING FAULTS, QUOTED AS PRINTED AND NAMED RATHER THAN COUNTED.** *"covariance metric Σ_i We
  additionally"* (§2.2 — the standard term is *matrix*, and the sentence break is missing); the lower-case
  *x* inside equation (4) where the observed features are *X* everywhere else (§2.3); *"calculated using
  HTK We included MFCCs"* (§3 — sentence break missing); *"as much a four times better"* (§3.1 — a missing
  letter); Figure 2's caption *"PCP features vectors"*; the reference list's *"music mode ling"*; and, in
  the conclusion, a sentence with no main clause of its own — *"This is a challenging instance of
  extracting complex musical information from a complex input signal has many practical applications"* —
  followed two sentences later by *"Because our system uses only the raw audio. it should be applicable
  over a wide range of circumstances"*, where the full stop stands in a comma's place.

  *(★ THE LIST WAS HEADED* "FOUR PRINTING FAULTS" *AND THEN NAMED FIVE; CORRECTED AT THE READ-BACK, WHICH
  ALSO FOUND THREE MORE. FORMER WORDING, PRESERVED (#12): "**FOUR PRINTING FAULTS, QUOTED AS PRINTED.**"
  **A count of this read's own findings, put on the sentence before the findings were finished** — and
  wrong against its own list at the moment it was written.)*

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered

- **The mapping from the songbook's chords to the paper's alphabet.** §3 says the progressions were
  *"mapp[ed] … to a simpler set of chords as shown in table 2"*, and the mapping itself is not printed.
  **So how a songbook's slash chord, added ninth or suspension became one of the 147 is unrecoverable
  from this paper**, and with it the question of how much harmonic information the ground truth discards
  before the system ever runs.
- **What "X" is, mechanically.** Table 2 gives X to *"chords not covered by this set"*. Whether X is an
  HMM state, whether it can be emitted, and whether it is one of the *"only 32 labels [that] occurred in
  our data"* are all unstated. **Table 4's X matrix having no X column is consistent with X never being
  emitted, and is not a statement that it cannot be.**
- **The pooling of variances.** §2.5 gives equations (5) and (6) for the means and disposes of the
  variances in a parenthesis — *"(Variances are similarly pooled.)"* **The rotation of a variance vector
  is not the same operation as the rotation of a mean vector under a frequency-weighted average, and the
  paper writes down neither the formula nor the weighting.**
- **The value of ε**, the EM stopping threshold (§2.3), against the stated *"13 to 15 iterations"* (§3).
  Which of the two actually stopped training is not said.
- **The number of emitting states per chord model.** §2.2 says *"one state for each chord"*; whether a
  chord model has internal structure of any kind is not discussed.
- **The transition matrix itself.** It is estimated and it constrains recognition, and **no transition
  value, no prior over chords and no structure of that matrix is printed or plotted in the seven pages.**
- **Any uncertainty on any figure.** Every number in Table 3 is a point value over **two test songs**,
  with no interval, no variance across songs, and no repeat of the EM run — while §5 explicitly names EM's
  local optimum as a possible cause of one result. **So nothing in the paper bounds how much of any
  difference in Table 3 is run-to-run or song-to-song variation.**
- **The frame count and duration of "Every Little Thing"**, which is why §6.8 cannot resolve the
  abstract's figure.
- **Whether the two test songs are representative**, in any sense the paper argues for. They are the two
  for which boundaries were hand-labelled, and the paper gives no other ground for the choice.

### §7.3 What is both measured and structural here

Stated as what the paper carries, for a reader who has to decide later what to do with it. **This section
proposes nothing and takes no position on the paper's candidacy.**

1. **★ THE SEPARATION OF THE TWO QUESTIONS IS THE PAPER'S STRUCTURAL CONTRIBUTION, AND IT IS MEASURED.**
   Forced alignment answers *where do the chords change, given which chords they are*; recognition answers
   *which chords, and where*. **The same trained models, the same features and the same decoder run both**,
   so the difference between the two columns is attributable to the constraint and not to a change of
   system. That is what makes 68.8 against 23.3 a measurement of what knowing the chord sequence is worth,
   rather than a comparison of two methods.
2. **THE COST OF NOT HAVING BOUNDARIES IN THE TRAINING DATA IS MEASURED AS ZERO HERE — because the paper
   never pays it.** Its whole design is that boundaries are hidden variables, and it reports no arm trained
   on hand-marked boundaries to compare against. **So the paper demonstrates that EM-without-timings
   works; it does not measure what it gives up against EM-with-timings.**
3. **PARAMETER TYING ACROSS TRANSPOSITION IS THE CHANGE THAT MOVES THE NUMBERS.** Base PCP to
   averaged-rotated PCP raises forced alignment from 26.3 and 46.2 to 68.8 and 83.3 on train18 — **a rise
   of 42.5 points at one cell, which is the largest change that one step produces at any of Table 3's
   eight positions** (the other seven are +37.1, +27.3, +29.8, +13.3, +1.9, −0.5 and −13.3) — and it
   comes from pooling each chord family's template over all twenty-one roots rather than from any change
   of feature, model or decoder.

   *(★ THIS CLAIM WAS WRONG TWICE AND IS CORRECTED AT ITS SITE, WITH BOTH FORMER WORDINGS PRESERVED
   (#12). **First wording:** "the largest movement **anywhere in Table 3**" — a superlative over the whole
   table, underived. **Second wording, written at the sweep to narrow the first:** "the largest movement
   Table 3 records **between any two of its five feature rows at one position**" — **which the arithmetic
   refutes**: at forced alignment, train18, "Every Little Thing" the five rows span 9.2 to 83.3, a range
   of 74.1 points. **A narrowing that introduced a second false superlative** is recorded as such, and the
   claim now names only the step it is about.)*
4. **AND THE SAME CHANGE COSTS SOMETHING ON THE OTHER ARM.** At recognition with train20 the pooled models
   fall below the unpooled ones on both test songs (23.6 → 23.1 and 26.4 → 13.1). **The paper calls this
   *"curious"* and offers a local-optimum conjecture for one of the two.** So the tying is measured to help
   the constrained arm and, in that one condition, to hurt the unconstrained one.
5. **THE MEASURE IS A DURATION-WEIGHTED, FIXED-GRID ONE.** Accuracy is the share of 100 ms frames carrying
   the right label — not a count of segments, not a boundary-placement error, and not anything invariant to
   how finely the music is cut.
6. **★ THE PAPER'S SILENCE ABOUT SEGMENT LENGTH IS A COMMITMENT AND NOT A GAP — ADOPTED AT THE
   CROSS-CHECK FROM THE FIRST EXTRACT (§9.5).** §2.2 states *"one state for each chord distinguished by
   the system"*, and a hidden Markov model with one emitting state per label carries an implicit
   **exponential** segment-length distribution, fixed by that state's self-transition probability. **So
   the system does have a duration model; it is the weakest available one, and it is never named as a
   modelling choice.** *(The implication is standard theory about first-order Markov chains; the paper
   states the one-state-per-chord structure and states nothing about duration. §7.2's entry on the
   unpublished transition matrix is the other side of the same point: the one parameter that sets the
   length distribution is the one the paper never prints.)*

**★ THE BOUND ON ALL FIVE, WHICH GOVERNS EVERYTHING THIS SECTION SAYS.** **This is an audio system
measured on audio.** Its input is a waveform; its features are spectral; its errors are, on the paper's
own account, partly failures to resolve two frequencies. **None of its measured values is a measurement
over notated music, and no figure in §5 can be read as one.** What can travel is the shape of the
experiment — two arms differing only in whether the label sequence is given — and the shape is not a
number.

### §7.4 What this paper's reference list gives the record, checked at the candidacy file

**One targeted search was run** over `reading_pass/candidacy_upgrades.md` for the surnames and the
distinguishing words of this paper's seven references (§5.7). **The result is negative, and the negative
is the finding: no reference of this paper is a row of that file.**

**The one near-miss, named because a later reader would otherwise re-check it.** This paper cites
**Raphael, C. (2002), *Automatic transcription of piano music*, ISMIR, Paris**. The candidacy file holds
**row 1, Raphael & Stoddard, ISMIR 2003**; **row 2, Raphael & Stoddard, CMJ 28(3) 2004**, recorded
ADMITTED and NOT HELD; and **row 31, Teodoru & Raphael, ISMIR 2007**, recorded NOT ADMITTED. **The cited
2002 paper is none of the three** — a different paper, a year earlier, single-authored, on piano
transcription.

**So this paper supplies no bibliographic record for any admitted-but-not-held row.** *(That rows 2, 6, 9
and 44 are the admitted-but-not-held ones is a **RELAY** through the hundred-and-seventy-eighth handoff
entry and was checked at no source here; what IS established here is that none of this paper's seven
references matches any row of the candidacy file, whatever that row's holding status. Row 2's own line
was read at the object and does record it as **not held**.)*

*(Contrast is available in the record: the hundred-and-seventy-eighth entry reports its own member's
reference list pinning row 44 from a second source. **That is a relay through that entry; nothing of it
is checked here.**)*

**What the near-miss does give, and it is small.** This paper's §1 characterises Raphael's 2002 method in
a sentence — one model per simultaneous-note combination, assembled from harmonic 'factors', on solo
piano — and contrasts it with one model per chord class. **That is a third-party account of a method by
the first author of rows 1 and 2, of a different paper**, and it is recorded here as exactly that and
nothing more.

**The bound on this section.** It is a negative over one targeted search of one file for the names in one
reference list. **No other file of the record was searched, and the candidacy file was not read whole.**

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

**The read-back set this file's finished §0 to §7 against the paper, quotation by quotation and value by
value.** Its openings were deliberately batched differently from the whole read, so that each observation
is made at a fresh call rather than at a remembered one: the whole read took pages **1–4** and **5–7**;
the read-back took **1–3** together, then **4** singly, then **5** singly, then **7** singly.

**★ ONE PAGE WAS NOT RE-OPENED AT THE READ-BACK, AND IT IS SAID PLAINLY RATHER THAN SMOOTHED: PAGE 6.**
It had already been opened twice — inside the whole read's 5–7 batch, and then singly to transcribe Table
4 cell by cell — and a third opening was not made. **What stands in its place is not another look but an
arithmetic check that no look could give**: §6.1 derives 386/1,655 = 23.3 % from the transcribed cells and
lands on a percentage printed independently on page 4. **That is a stronger test of the transcription than
re-reading it would be, and it is not the same act.** A later reader who wants page 6 checked by eye should
know it was checked by eye twice and not three times.

**The sweep** then went over this file's own writing for absolutes and for underived counts, rankings and
proportions, **every hit read at its own line** rather than counted by a search.

### §8.2 What the read-back and the sweep struck in this side's own writing

Named rather than counted. **Every one is corrected at its own site with the former wording preserved
(#12).**

**Two quotation defects, both caught by the read-back:**

- **A WORD ALTERED INSIDE A QUOTATION.** §3.3 carried the paper's tuning proposal as *"and cent[ering]
  the PCP feature definition accordingly"*; **the paper prints *"and center"***. **This is precisely the
  defect class this line reports of other reads**, made here, and it was made by a bracketed inflection
  that reads as correct English on its own — which is why it survived the writing.
- **A SYMBOL TRANSCRIBED WITH CONFIDENCE THIS READ DOES NOT HAVE.** §2.3 rendered the posterior in the
  Baum-Welch sentence as `p(q^t_n|…)`. **Three openings of page 2 did not resolve which of the subscript
  and the superscript sits where**, so the symbol is now elided and flagged at its site rather than
  transcribed.

**Absolutes and over-wide statements, struck at their lines:**

- **§0** said this file *"asserts nothing whatever about what the record says of this paper"* — false of
  §5.3 and §7.4, which both reach the candidacy file. Narrowed to what the one line read at the object
  carries.
- **§1** said *"Every quantity in §5 is a frame-level audio measurement"* — false of a song list, an
  alphabet, a constants table and a reference list. Narrowed to §5.3's accuracy figures.
- **§2.3** said the paper states no duration distribution *"of any kind"*, and **§7.2** said the transition
  matrix is printed or plotted *"anywhere"*. Both bounded to the seven pages, which is the act that
  produced them.
- **§3.1** said *"Nothing symbolic enters the system at any point"* — refuted by the paper's own design,
  in which the chord-label sequences are exactly what does enter it.
- **§6.1** said the Table 4 transcription *"is right"* because a mis-read digit *"would not"* survive the
  check. **Two compensating mis-reads would survive it**; the claim now stands at the strength the
  argument carries.
- **§6.6** said *"no other sentence of the paper depends on it"* — an unbounded negative over a dependency
  this read never traced. Narrowed to the sentences read here.
- **§6.10** said *"the criterion is what is wrong rather than the conjecture"* — a verdict wider than the
  arithmetic. Narrowed to what the arithmetic shows, which is that the criterion understates the limit.

### §8.3 The degradation tells, reported unprompted

The user's standing rule of 2026-08-15 names the tells and requires that two or more be reported
unprompted, with a recommendation to hand over at a verified stop. **Two of the named tells fired in this
read's own writing. They are named and deliberately NOT totalled**, for the reason the two entries this
side read whole both give: every total a sitting puts on its own tells goes stale at its next pass.

**Tell A — a count, a proportion or a ranking put on this read's own reading or its own findings without
deriving it.**

- *(i)* **§2.1 called the state-space contrast *"the ONE structural point of this paper that is about
  state-space size"*** — a uniqueness claim over a set this read never enumerated. **Caught at the sweep.**
- *(ii)* **§2.6 introduced the rotation-averaging mechanism as *"THE PAPER'S MAIN RESULT"*** — a ranking
  of the paper's results against one another, on nothing. **Caught at the sweep.**
- *(iii)* **§7.3's bound carried the words *"AND IT IS THE LARGEST SENTENCE IN THIS FILE"*** — a ranking of
  this file's own sentences. **Tell A's own shape inside the sentence written to keep the section
  honest.** **Caught at the sweep.**
- *(iv)* **§7.3's third item called the base-to-rotated rise *"the largest movement anywhere in Table
  3"*** — a superlative over the whole table, underived. **Caught at the sweep.**
- *(v)* **★ AND THE NARROWING WRITTEN TO FIX (iv) WAS ITSELF FALSE.** It read *"the largest movement Table
  3 records between any two of its five feature rows at one position"*, and **the arithmetic refutes it**:
  at forced alignment, train18, "Every Little Thing" the five rows span 9.2 to 83.3, a range of 74.1
  points against the 42.5 the sentence claimed. **Caught by checking the correction rather than by
  trusting it**, in the same pass that wrote it. *(This instance also answers the description of a
  different named tell — successive refuted shortcuts — and it is named once here rather than counted
  twice.)*
- *(vi)* **§7.1 headed a list *"FOUR PRINTING FAULTS"* and then named five** — a count of this read's own
  findings, **wrong against its own list at the moment it was written**, and made false again by the
  read-back, which found three more. **Caught at the read-back.**

**Tell B — citing a summary instead of the source, and an unmarked relay presented as established.**

- *(vii)* **§7.4 concluded that this paper *"supplies no bibliographic record for any admitted-but-not-held
  row"*, where the membership of that class — rows 2, 6, 9 and 44 — was taken from the
  hundred-and-seventy-eighth handoff entry and checked at no source.** The negative this read actually
  established is wider and simpler: no reference of this paper is any row of the candidacy file. **Caught
  at the sweep and marked as a relay at its site.**
- *(viii)* **★ AND IT FIRED A SECOND TIME, IN §9 ITSELF, AND WAS CAUGHT ONLY BY THE USER-ORDERED CHECK.**
  §9.3 closed by calling the disputed cell *"the one cell in Table 3 that the paper never restates in
  words"* — **the first extract's own characterisation, repeated here as though it were a finding of this
  read, and refuted by the table**, which leaves most of its forty cells unrestated in the prose.
  **Inside the section written to report the cross-check.** **Caught at the user-ordered check and
  corrected at its site** (§10).

**★ WHAT THE THRESHOLD MEANS HERE, STATED PLAINLY AND WITHOUT INFLATION.** **What fired is TWO named
tells** — the count-and-ranking one repeatedly, and the summary-instead-of-source one twice — **not
several different tells, and nothing more than that is claimed.** Under the rule, this read reports it and
**recommends handover at a verified stop**. **That every one was caught by a pass of this side's own does
NOT lower the count**: the hundred-and-seventy-eighth and hundred-and-sixty-ninth entries each record that
it does not, read at their own texts here.

### §8.4 The bound on this section

**This section reports what two passes of this side's own writing found, and nothing establishes that a
further pass would come back empty.** The read-back caught what the writing did not; the sweep caught what
the read-back did not; and **the sweep's own correction of instance (iv) was itself false and was caught
only because the correction was checked**. **Each of those is a further pass over the same writing by the
same side.**

**★ THIS PARAGRAPH SPOKE ABOUT THIS SITTING'S OWN STATE AND WENT FALSE WHILE THE SITTING RAN; IT IS
CORRECTED AT ITS SITE.** *(FORMER CLOSING CLAUSE, PRESERVED (#12): "…and **the one pass of a different
kind — a second reader with the same pages — has not happened yet: it is step 7, and §9 is where it will
be recorded.**")* **Step 7 has since run, and §9 records it** — and it caught a mechanism this side had
stated too strongly (§5.4) that three passes of this side's own had left standing. **Tell B's second
instance, (viii) above, was then caught by none of those: it took the user-ordered check, which is §10.**
So the passes over this file are four, of three kinds, and **nothing establishes that a fifth would come
back empty.**

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**The first extract was opened for the first time at this point and not before** — step 7 of the
hundred-and-sixty-ninth entry's §3, with §0 to §8 of this file already written, swept and landed at
77,067 bytes. It is
`reading_pass/extracts/sheh-ellis-2003-chord-segmentation-and-recognition-using-em-trained-hidden-markov-models.md`,
**43,240 bytes**, staged and read whole. Its own provenance dates it 2026-09-06.

**What was compared.** Every value and every quotation this read could set side by side — which is not
the same as every one the two files carry, and §9.6 states the bound. **Where they disagreed, the paper
was re-opened** — page 4 singly and page 5 singly, each a further opening beyond the whole read and the
read-back.

*(★ NARROWED AT THE USER-ORDERED CHECK, §10. FORMER WORDING, PRESERVED (#12): "**Every value and every
quotation the two files both carry.**" **Contradicted by §9.6's own bound five subsections later**, which
says the comparison is not exhaustive.)*

**★ THE ASYMMETRY THAT GOVERNS THIS SECTION.** **The first extract reaches deep into this project's own
record** — `FRAMEWORK.md` at DP-C, §S4(d) and DP3; `reading_pass/population.md`'s V10 row;
`docs/research_papers/BIBLIOGRAPHY.md` row 32 with its URL and its tier; the slice derivation; the
findings surface; and several neighbouring rows' extracts. **This read opened none of them.** So on that
whole half **this is not a second opinion but silence**, and nothing below should be read as agreement or
disagreement with it. **In particular this read takes no position on the first extract's centrality
verdict, on its reading of DP-C's recorded ground, or on any of the twelve findings it routes** — except
where a finding's PAPER half is checkable here, which is §9.5's subject.

### §9.2 What both reads transcribed, and where they agree

**Table 3 — thirty-nine of its forty cells are transcribed identically by the two reads.** The fortieth is
§9.3.

**Every other value both files carry agrees**, named rather than counted: the held file's size, 109,996
bytes; the seven chord families and the twenty-one spelled roots of Table 2, and its caption's 147 and 32;
the corpus of twenty songs, two test and eighteen train; the 11,025 Hz rate, the 4,096-point Hanning
window, the 24 PCP dimensions, the 100 ms step and ten frames per second, and the 440 Hz reference;
the single Gaussian with diagonal covariance and its 24 means and 24 variances; the 13-to-15 EM
iterations and the flat start; the five feature configurations and their compositions; Figure 2's axis,
16.27 to 24.84 seconds; and **Figure 2's three label strips, read independently and identically by both —
true E, G, D, Bm, G; align E, G, D, Bm, G; recog E, G, Bm, Am, Em7, Bm, Em7.**

**Three things both reads found independently, which is what the doubling is for.**

- **The text-against-equation disagreement inside §2.1** — the prose *"summing the magnitude"* against
  equation (3)'s `|X[k]|²`. **Both reads found it, both recorded it as the paper's own, and neither
  resolved it.**
- **The identity finding** — that the held document prints no venue, no conference line, no running header
  and no page number, so it does not establish at its own face whether it is the proceedings text. **Both
  reads reach it independently**, and the first extract adds from the record side that the bibliography's
  own tier already says *author copy*, which this read cannot confirm and does not.
- **The abstract's 75 % is not a table cell, and the train18 forced-alignment mean is 76.05.** **Both
  reads derive that figure independently and agree to the digit.**

### §9.3 ★ THE ONE DISAGREEMENT ON A TRANSCRIBED VALUE, AND IT IS RECORDED UNRESOLVED

**The cell.** Table 3, PCP_ROT, forced alignment, train20, *"Every Little Thing"*. **This read: 83.5. The
first extract: 83.0.**

**What each side did.** This read transcribed it at the whole read (pages 1–4 together), again at the
read-back (page 4 singly) and again at the cross-check (page 4 singly) — **three openings, 83.5 each
time**. The first extract records **two separate readings of the image, 83.0 each time**, and — this is the
part that matters — **it flagged that very cell in advance as the weakest-supported one in its table**:
*"The one cell with no prose cross-check of its own is PCP_ROT / align / train20 / "Every Little Thing","
read as 83.0 at two separate readings of the image."*

**The attempt to resolve it at the paper, and why it fails.** The first extract offers a corroboration:
the authors' *"PCP_ROT achieves no benefit from training on the test set"* is said to require the train20
alignment figures to sit at or just below the train18 ones, *"68.3 < 68.8 and 83.0 < 83.3"*. **That
argument does not carry the weight put on it.** The sentence is qualitative, and **the paper's own
parenthesis locates where the loss is** — *"(and even does significantly worse on recognizing "Every
Little Thing")"*, which names RECOGNITION, not alignment. A rise of 0.2 points on alignment is *no
benefit* in any ordinary reading of that sentence. **So the prose corroborates neither digit.**

*(★ A CLAIM STRUCK HERE AT THE USER-ORDERED CHECK, §10. FORMER WORDING, PRESERVED (#12): "…**and the one
cell in Table 3 that the paper never restates in words is the one the two reads differ on.**" **That is
the first extract's own characterisation, repeated here as though established, and the table does not
support it**: the paper's prose restates a handful of cells — the 15.8 against 10.0, the 23.1 and 13.1
against 23.6 and 26.4, and the 83.3 against 19.9 — and **leaves most of the forty unrestated**, so the
disputed cell is one of many with no prose cross-check rather than the only one. **This read takes no
position on why the first extract flagged that cell in particular; it records that it did.**)*

**★ AND NO FURTHER ROUTE WAS AVAILABLE WITHIN THE RULES.** The obvious move — rendering that region of the
page larger with a script — is a read of working-tree content through a shell, which the standing rule
forbids whatever utility spells it. **No such read was made.** Fetching the publisher's copy would be a
web fetch, and none was made either.

**SO THE DISAGREEMENT IS RECORDED AS UNRESOLVED**, which is the disposition the commission's own §4
provides for: *"disagreements are resolved at the paper or recorded as unresolved."*

**What it moves, stated exactly and completely.** Three places in this file, all of them marked at their
sites: **§5.3**, where the cell is flagged; **§6.7**, where one of eight ratios is 3.63 on this reading and
3.61 on the other, while the maximum the section is about sits at a different position and does not move;
and **§6.8**, where the train20 mean is 75.9 on this reading and 75.65 on the other, while the train18
mean of 76.05, which is the figure both reads actually use, rests on no flagged cell. **It moves no
headline value, neither of DP-C's two figures, and no verdict of either file.**

### §9.4 The disagreements against the first extract, named

**None of the four moves a transcribed value.** Each was resolved at the paper, at the openings §9.1
names. **That file is untouched** — the standing ground being this line's own: rewriting another read's
text destroys what the doubling compares.

**(a) A DROPPED WORD INSIDE A QUOTATION, AT TWO OF THAT FILE'S OWN PLACES.** It quotes §3.2 as *"which
differ only by the semitone between major and minor third intervals"*, in its Table 4 paragraph and again
in its finding (12). **The paper prints *"between the major and minor third intervals"***, established at
page 5 at the whole read and again at a separate opening at the cross-check. **No value moves and the
sense does not change.**

**(b) ★ A MECHANISM MISDESCRIBED, AND IT IS THE ONE OF THE FOUR THAT A DESIGN CONSUMER WOULD CARRY.** The
first extract states that the *"X"* label *"appears as a state in the confusion matrices of Table 4"* and,
in its candidate-admission section, that it is *"decoded like any other state and appears in the confusion
matrices"* — offered there as **a published precedent for an explicit none-of-the-above candidate**, and
routed to L2's detail specification where the admission rule lives.

**At the paper, Table 4 shows nothing of the kind.** Its columns are the seven chord FAMILIES and its rows
the twelve root classes, so **there is no cell anywhere in the table in which an X output could be
shown**; and §3.2 says what the six matrix headings are — *"Table 4 presents the confusion matrices for
every frame in "Eight Days a Week", which we label with only 5 chords plus "X""* — **the labels the
authors' own hand annotation uses.** So *"X"* appears in Table 4 as a GROUND-TRUTH heading, and the table
is silent on whether the system can emit it. **Whether X is an HMM state at all is unstated in the seven
pages** (§7.2).

**Why it is worth reporting rather than waving through.** The claim is not decorative: it is the evidence
on which that extract offers the paper as a precedent for an out-of-vocabulary candidate class. **A later
reader taking it up would believe this paper demonstrates decoding such a class, which it does not show.**
*(What is NOT claimed here: that the system cannot emit X. The paper does not say, and neither does this
file.)*

**(c) A LOCATOR ERROR.** The first extract attributes the passage *"If we knew which state (i.e. chord)
generated each observation…"* to **§2.3**. **At the page it is the last paragraph of §2.2**, standing above
the §2.3 heading. That file's own banner undertakes to give every location by printed section number, so
the locator is the thing it claims to supply. **No value moves.**

**(d) AN ABSOLUTE CONTRADICTED BY THAT FILE'S OWN COUPLING-FACTS SECTION.** Its identity section says
*"There are no notes, no score and no symbolic input anywhere in the method."* **Its own coupling-facts
section then states the opposite for training** — *"For TRAINING: a chord SEQUENCE per song, without
timings"* — and the chord sequences are symbolic. **The paper agrees with the coupling-facts section**:
the sequences are what composes the training HMM. **No value moves.** *(Recorded with the note that this
side wrote the same over-wide sentence in its own §3.1 and struck it at its own sweep, at §8.2 — so this
is not a defect one read was immune to.)*

### §9.5 What the doubling produced that neither read had alone, in both directions

**★ FROM THE FIRST EXTRACT'S SIDE, AND THIS READ TAKES NO POSITION ON IT.** That file holds the whole of
what the RECORD says of this paper — `FRAMEWORK.md`'s DP-C, §S4(d) and DP3, `population.md`'s V10 row,
the bibliography's row 32 and its tier, and the slice derivation's placement — **and this read opened
none of those objects, so on that half this is silence and not a second opinion** (§9.1).

**★ BUT ONE HALF OF ITS LOAD-BEARING FINDING IS CHECKABLE HERE, AND IT IS CONFIRMED.** Its finding (3)
turns on a claim about the PAPER: that in the 68.8 condition it is the **chord sequence** that is given
and that the boundaries are found in **both** conditions. **This read reached the same reading
independently, before the first extract was opened** — §2.5 and §7.3's first item say it in this file's
own words — **and it rests on three separate statements of the paper**: §2.4's *"only the chord-change
times are being recovered, since the chord sequence is known"*; §3.1's *"the basic chord sequence is
already known in forced alignment which then has only to determine the boundaries"*; and §3's *"In the
case of alignment, the chord sequence file is used to generate a simple composite HMM with allowable
transitions determined by the song's progression."* **So the paper half of that finding survives an
independent read. The record half is untouched here and no verdict is taken on it.**

**★ AND THE FIRST EXTRACT CARRIES ONE PRECISION THIS READ LACKED**, adopted into this file at the
cross-check and marked there: **that a hidden Markov model with one emitting state per chord carries an
implicit EXPONENTIAL segment-length distribution** — so the paper's silence about duration is not a gap
but a commitment. §7.3 now carries it.

**★ GOING THE OTHER WAY, ELEVEN THINGS ARE IN THIS READ AND NOT IN THE FIRST.** **The first four are the
ones that bear on how a printed value or a stated claim of the paper is read; the rest are checks that
close.**

*(★ NARROWED AT THE USER-ORDERED CHECK, §10. FORMER WORDING, PRESERVED (#12): "**ELEVEN THINGS ARE IN
THIS READ AND NOT IN THE FIRST**, named rather than counted. **The first four are the substantial
ones.**" **Two defects:** the phrase* named rather than counted *stood over a sentence that counts them,
and* the substantial ones *was a ranking of this read's own findings with no stated test. The count is
kept because it is read off the list beneath it, and the test is now stated.)*

1. **§6.1 — Table 3's figures are ACCURACIES and not error rates**, established by summing Table 4 and
   landing on 23.3. **The paper names the quantity both ways** — its caption says *"Percent Frame
   Accuracy"* and its body twice says *"frame error rate"* — **and the first extract transcribes both
   namings without noticing that they are different quantities.** A reader lifting 23.3 needs this.
2. **§6.6 — §3.1's *"in all cases except one"* is false at a second cell the sentence does not name**:
   forced alignment, train18, "Eight Days a Week", MFCC 27.0 against PCP 26.3. **The first extract uses
   that same clause as a transcription check and accepts it as exhaustive.**
3. **§5.4, §6.11 and §6.12 — Table 4 transcribed cell by cell**, which the first extract does not attempt
   at all, and the two things that follow from it: that the aggregate 23.3 spans a per-chord range from
   0 % to 44.3 %, and that at two of the four major matrices the same-root MINOR is the system's majority
   reading of the chord rather than merely a *"frequent"* confusion.
4. **§6.10 — the paper's own frequency-resolution criterion understates its own limit.** On the
   bin-spacing criterion §4.1 states, the quarter-tone limit sits near 92 Hz; on the Hanning window's
   four-bin main lobe it sits near 367 Hz. **This strengthens the paper's conjecture rather than
   weakening it**, and neither figure is in the first extract.
5. **§6.2** — the song's frame count, 1,655, and its playing time.
6. **§6.3's second half** — that the twenty-one root spellings collapse to exactly the twelve rows Table 4
   prints.
7. **§6.9** — the 371.5 ms analysis window against the 100 ms hop, and what a 73 % overlap does to a
   boundary measured on a 100 ms grid.
8. **§6.13 and §6.14** — Figure 2's segment closing against its own caption, and all five feature
   configurations coming to twenty-four dimensions.
9. **§5.5** — Figure 3's legend plotting five of Table 2's seven families, omitting maj7 and aug.
10. **§7.1** — the *"Monophonic music recordings"* collision in a paper about polyphony; the conclusion's
    sentence with no main clause; and the stray full stop in *"only the raw audio. it should be"*.
11. **§7.4** — that no reference of this paper is any row of the candidacy file, with the Raphael 2002
    near-miss named.

### §9.6 What the cross-check does NOT establish

- **It does not establish that either file is clean.** Defects of this side's own had already been struck
  at the read-back and the sweep before the first extract was opened, and they are at §8.2 with the
  degradation tells at §8.3.
- **It does not reach the record half of the first extract at all** (§9.1), which is the larger half of
  that file.
- **It did not settle the one value the two files differ on** (§9.3).
- **It is not exhaustive.** It ran over what the two files both carry; a later reader may find more.
- **It changed no transcribed value of this file, no byte count, no modification time and no row number**,
  and **it left the first extract untouched.**

---

## §10 — The user-ordered fact- and source-check, run after this file had landed and re-landed

The user's standing rule of 2026-09-12 extends the pre-landing check to landed work on four axes —
completeness, coherence, correctness, and misuse of hyperbole and absolutes — **and his opening
instruction to this sitting ordered it over everything this side has written, the closing report
included.**

**Where it reached in this file.** **§9 in full**, which was written after the sweep of §8 and had
therefore never been swept; **§0 to §8 were not re-swept**, having already had the read-back, the sweep,
and the cross-check's own passage through them. **So a next side should treat this file's §0 to §8 as
carrying those three passes and its §9 as carrying one.**

**What it found in §9, corrected at their sites with the former wordings preserved (#12):**

- **A STATEMENT CONTRADICTED BY THIS FILE'S OWN BOUND FIVE SUBSECTIONS LATER.** §9.1 said the comparison
  ran over *"Every value and every quotation the two files both carry"*, where §9.6 says in terms that it
  is not exhaustive.
- **★ THE FIRST EXTRACT'S OWN CHARACTERISATION, REPEATED AS THOUGH ESTABLISHED, AND REFUTED BY THE
  TABLE.** §9.3 ended by calling the disputed cell *"the one cell in Table 3 that the paper never restates
  in words"*. **That is the first extract's sentence, not a finding of this read**, and the table refutes
  it: the paper's prose restates a handful of cells and leaves most of the forty unrestated. **This is the
  summary-instead-of-source tell, inside the section written to report the cross-check** — and it is
  added to §8.3 as an instance.
- **A COUNT STANDING UNDER THE WORDS THAT SAY IT IS NOT COUNTED, AND A RANKING WITH NO TEST.** §9.5 read
  *"ELEVEN THINGS ARE IN THIS READ AND NOT IN THE FIRST, named rather than counted"* — which counts them
  — and then *"The first four are the substantial ones"*, a ranking of this read's own findings with no
  stated test. The count is kept, being read off the list; the test is now stated.

**★ AND A SECOND PASS WAS ORDERED AFTER THAT, OVER BOTH FILES AGAIN.** **In this file the second pass was
TARGETED, not whole** — at §10's own account of itself, and at the sites the handover entry was found to
contradict. **What it found here is one thing, and it is about the pair rather than about this file:**

- **★ A CLAIM STRUCK IN THIS FILE AND LEFT LIVE IN THE OTHER.** §9.3's correction — that calling the
  disputed cell *"the one cell in Table 3 that the paper never restates in words"* is the first extract's
  characterisation and not a finding of this read — **had not reached the handover entry, which was still
  carrying the sentence as established at two of its own sites.** Both are corrected there. **Nothing in
  THIS file changed on that account**; what the pass establishes is that **correcting a claim in one file
  does not correct it in the other, and a next side should read the two against each other after a
  correction rather than each against itself.**
- **AND §10's OWN HEADING COUNTED THIS FILE'S LANDINGS** — *"after this file had landed twice"* — **which
  a further landing made false by construction.** Now written in the non-counting form.

**★ WHAT NEITHER PASS DID.** Neither fetched a page image, re-opened the first extract, ran web access or
swept a repository, and **neither changed a transcribed value, a byte count of another file, a
modification time, a row number or a verdict.** **Neither settled the disputed cell of §9.3**, and both
left the first extract untouched, so **the four items standing with the user are exactly as §9.4 records
them.** **Their yield has the shape every pass of this sitting has had: every defect is in this side's
account of its own acts, of what the other read says, or of how far its own reading reaches — none is in a
value taken from the paper.** **And nothing here says a third pass would come back empty.**

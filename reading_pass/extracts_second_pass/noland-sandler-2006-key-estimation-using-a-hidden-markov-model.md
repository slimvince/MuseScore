# Second extraction — Noland & Sandler 2006, "Key Estimation Using a Hidden Markov Model"

> **STATUS: SECOND INDEPENDENT EXTRACTION.** Row 26 of the Task B reading list. **That row 26 sits in
> the L2 slice is a RELAY** — it is taken from the handoff line's table order and from the first
> extract, and neither `reading_pass/l2_slice_reading_progress.md` nor the slice derivation was opened
> in this sitting. Written in the form the reading-pass commission of 2026-08-30 sets at its §4 (claims
> labeled, coupling facts mandatory, measured results with corpus, metric and value as the paper states
> them), read whole at that file in this sitting before any of this was written. This extraction did
> not consult the first extract,
> `reading_pass/extracts/noland-sandler-2006-key-estimation-using-a-hidden-markov-model.md`, which was
> not opened before the cross-check this file's §9 records.
>
> **Nothing in this file is ruled, and it authorizes nothing.** It records what one read of one paper
> found.

---

## §0 — What was read, and the bound on this read's independence

**The object.** `docs/research_papers/noland_sandler_2006_ismir_key_estimation_hmm.pdf`, **417,537
bytes**, staged through the bridge and read as page images with the file tools. **Six pages**, and the
page count was established AT THE TOOL by a deliberately out-of-range request, which answered *"PDF
has 6 pages"*. All six page images were present and legible, checked at the images themselves and not
at the call's success line.

**How pages are cited below.** By their position in the held file, 1 to 6. No printed page number was
visible in the images as read, so a citation here is to the sheet and not to a journal pagination.
*(This is stated rather than assumed; it is one of the things the read-back re-checks.)*

**Identity, checked at page 1 before anything was extracted.** The printed title is *Key Estimation
Using a Hidden Markov Model*; the printed authors are Katy Noland and Mark Sandler, Centre for
Digital Music, Queen Mary, University of London; the copyright line reads *© 2006 University of
Victoria*, which is the ISMIR 2006 host. These match the row's own description at
`reading_pass/candidacy_upgrades.md` line 88 — *"Noland & Sandler, ISMIR 2006, key estimation using a
hidden Markov model"*. **No identity finding.**

**THE INDEPENDENCE BOUND, DECLARED RATHER THAN CLAIMED AWAY.** The doubling compares two reads that
did not consult each other, so what this read already knew about the first one must be written down.

- **This side read the hundred-and-eighteenth handoff entry in the boot**, for its bridge-fault
  section, and the call that returned that section also returned the account of that sitting's own
  work, which was **row 26's FIRST extraction**. So before writing a word of this file, this side had
  seen that entry's statement of the first extract's headline conclusion — that the paper is
  *CENTRAL on a narrow ground* by that extract's own reasoning, together with the ground it names —
  and had seen that the first extract cites `FRAMEWORK.md` §S4(b) as the record's one citation of this
  paper. **That is contamination of this read's independence and it is recorded, not argued away.**
- **What this side did NOT see.** The first extract itself was not opened. `reading_pass/l2_slice_reading_progress.md`
  — the progress record, whose cells state each first extract's conclusion — **was not opened at all
  in this sitting**, so none of its verdict text reached this read. `FRAMEWORK.md` **was not opened
  at all either**, so no wording of it reached this read — though the hundred-and-eighteenth entry did
  name §S4(b) as the section that cites this paper, which is part of the contamination recorded in the
  bullet above and not separate from it.
- **What follows from the bound.** Where this file and the first extract agree, the agreement is
  weaker evidence than a clean doubling would give, on exactly the one point named above — the
  paper's centrality and its narrow ground. On the paper's content, its values, its tables and its
  omissions, this side had nothing from the first extract at all.

**No sweep of the repository was run for this paper** — not for its authors, not for its title, not
for any of its values — so this file asserts nothing about what the rest of the record says of it.

---

## §1 — What the paper is

A six-page conference paper proposing a method that decides the **tonality** of a piece of music from
a stream of **chord symbols**. It works at two grains at once: a per-frame likelihood for every
tonality, and a single overall tonality for the whole track.

The machinery is a **hidden Markov model** — a model with a set of hidden states that cannot be seen
directly, each of which emits something that can be seen. Here the hidden states are the tonalities
and what they emit are chords. The paper's own words, page 2: *"The music-theoretic notion that a
sounded chord sequence can strongly imply an underlying key, or allude to more than one key, fits
well into the HMM structure, which consists of a set of underlying, unobservable states that emit
observable data."*

Two things distinguish it from the work it cites.

1. **The observed thing is a PAIR of consecutive chords, not a single chord.** Page 2: *"It was
   decided that a pair of consecutive chords should be used for each observation, instead of a single
   chord, in order to extend the temporal dependency across a greater number of frames."*
2. **The starting values of the model come from published listening-test results rather than from
   counts.** Page 2, of the related work: *"The algorithms described in this section have all
   successfully used prior musical knowledge to aid extraction of harmonic information, but all base
   their analysis on single chords. This paper introduces further temporal dependency into the task of
   key estimation by using an HMM on chord transitions rather than single chords, as well as making
   use of listening test results for initialisation, in order to represent expected relationships
   between chords and keys."*

---

## §2 — The method, as the paper states it

### §2.1 The state space

**FACT (page 2).** Twenty-four hidden states, one per major and minor tonality. *"Only 3 keys are
shown in the figure for clarity, but the 24 possible major and minor keys are included in the actual
calculations. Each state represents a key, and the model is fully connected so that any key can move
to any other key, or stay the same."* Figure 1 on page 3 is the simplified diagram of that model, and
it is labelled with the observation as *"Observation = chord transition"*.

**FACT (page 2).** The chord vocabulary is triads only, plus a symbol for no chord: *"The two chords
that make up each chord transition can be any major, minor, augmented or diminished triad, or no
chord, which occurs during silence or entirely percussive sections."*

**FACT (page 2) — the paper's own defense for that restriction, quoted because it is a design ground
and not an aside.** *"More complex chords have been excluded from the model since chords that are not
based on triads are very rare in the Western music repertoire for which this analysis is intended,
and it was considered that the sequence of underlying triads, excluding extensions, is sufficient to
define the key."*

**FACT (page 2) — and this one is a coupling fact, not a detail.** *"All inversions of the same chord
are treated identically, which means that the choice of bass note does not affect the estimated key."*

### §2.2 The three things that get starting values

**FACT (page 2).** *"There are three HMM parameters that require initialisation."* They are the
initial state probabilities, the state transition probabilities, and the observation probabilities.

**Initial state probabilities — FACT (page 2).** *"The initial state probabilities reflect any prior
information that we may have about the most likely key, before any of the music has been heard.
However, there is no reason to prefer any key above any other, so the initial probabilities for all
states are set equally, to 1/24."*

**State transition probabilities — FACT (page 2 into page 3).** The starting tonality-to-tonality
matrix is built from Krumhansl's correlations between tonality profiles, the values reproduced in the
paper's own Table 2. The construction, quoted whole because its clauses carry the assumptions named
just below it:
*"The initial key transition matrix was created using the key profile correlations in Table 2 in the
Appendix, which give numerical values to our intuitions. The values were circularly shifted to give
the transition probabilities for keys other than C major and C minor; an operation that assumes G is
to G major as C is to C major, etc.. The values were all made positive by adding 1, then they were
normalised to sum to 1 for each key. This gave the final 24 × 24 transition matrix."*

Those four sentences carry assumptions the paper treats very differently, and each one is named here
rather than totalled. **Transposition invariance** — that the tonality space repeats
identically at every transposition — is **declared in terms**, in the *"G is to G major as C is to C
major"* clause. **A correlation between two profiles standing in for the probability of moving
between the two tonalities** is gestured at once, in *"which give numerical values to our
intuitions"*, and is not argued. **That adding 1 and renormalising preserves whatever ordering the
correlation carried** is not discussed at this passage. *Which of the three the passage treats how is
this side's reading of it; the words quoted are the paper's.*

**Observation probabilities — FACT (page 3).** *"The initial observation probabilities should reflect
the human expectation of the key(s) implied by a certain chord transition. We are assuming that there
is a strong correlation between the key implied by a chord transition, and the likelihood of the
transition occurring in that key."*

**FACT (page 3) — the paper's evidence for that assumption, with its values.** *"This assumption is
supported by Krumhansl [1] p. 195, and by finding the correlation between the chord transition
ratings and the corresponding number of transitions present in our test data. Correlations of 0.39
for major keys and 0.22 for minor keys were found, both highly significant given the respective 40
and 154 degrees of freedom."*

**FACT (page 3) — the worked illustration the paper gives, quoted because it is the clearest statement
of what the emission is supposed to mean.** *"So, the chord transition B major to E major strongly
implies the key of E major, since it forms a perfect cadence, so the probability of state E major
emitting B-E will be very high. However, both chords are also contained in the key of B major, so the
probability of state B major emitting B-E will be almost as high. Neither chord is contained in B♭
major, so the probability of state B♭ major emitting B-E will be very low."*

**FACT (page 3) — how the emission table was actually filled, which is four rules and not one.**

1. Diatonic chord transitions within a major key take their pre-normalised value from the chord
   transition ratings in the paper's Table 3.
2. Staying on the same chord takes its value from the single-chord ratings in the paper's Table 4,
   *"artificially boosted because repeated chords on either a frame-by-frame or beat-by-beat level
   are very likely. The approximate optimal increase was experimentally found to be 2. For example,
   the pre-normalised figure for emitting a transition from A minor to A minor in the key of C major
   was 3.62 + 2 = 5.62."* **★ CORRECTED AT THE CROSS-CHECK. FORMER WORDING, PRESERVED (#12): "…on
   either a frame-by-frame or a beat-by-beat level…"** — this side had inserted an article the paper
   does not print. The first extract had it right; resolved at page 3. Recorded at §9.
3. *"Pre-normalised values for transitions involving one or more non-diatonic chord are set uniformly
   low, to 1."*
4. *"For minor keys the ratings for major keys corresponding to the same scale degrees were used."*

Then: *"The emission matrix was then normalised so that the observation probabilities summed to 1 for
each key. The final emission matrix, then, had dimensions (48 + 1)² × 24 = 2401 × 24, since there are
48 possible chords and the possibility of no chord to form the chord transitions, in 24 possible
keys."*

*The value 3.62 in rule 2 is A Minor in the C Major context of the paper's Table 4, and it is that
value there. The arithmetic (48 + 1)² = 2401 is the paper's own and it holds.*

### §2.3 Training

**FACT (page 3).** *"The expectation maximisation (E-M) algorithm, described in [9], was used to
learn the HMM parameters for each individual song."*

**FACT (page 3) — and this is the statement Table 1 is the experiment for, which is why it is quoted
whole rather than summarised.** *"If the
observation probabilities, which model the relationship of each chord transition to each key, were
subject to training, we could no longer be certain that the hidden states represent keys. To verify
this, experiments were conducted with various combinations of HMM parameters trained."* The experiment
that verifies it is Table 1, recorded at §5 below.

**FACT (page 3).** How a chord sequence becomes training data: *"The training data was a sequence of
chord transitions, so for a chord sequence Dm-Bdim-C the first chord transition would be Dm-Bdim, and
the second Bdim-C. For each key, each chord transition was given a numerical index from 1 to 2401.
These were circularly shifted to give the values for other keys, with the exception of transitions
involving a no chord, which has the same function in every key and so was kept at the end of the
sequence."*

### §2.4 Decoding

**FACT (page 3).** *"The Viterbi algorithm was used to find the most likely sequence of keys, and
standard HMM decoding [9] was used to calculate the posterior state probabilities, giving the
likelihood of being in any key at each time frame."* So the method produces two things, not one: a
single hard path, and a full per-frame distribution over all twenty-four tonalities.

---

## §3 — Coupling facts

The commission's §4 makes these mandatory, because a method's admissibility at one layer depends on
what its neighbours must then be.

### §3.1 What it ASSUMES about its upstream

- **A stream of chord labels with start and end times.** FACT, page 3: *"The algorithm was tested on
  hand annotations of the start and end times of every chord in all of the first 8 Beatles albums,
  provided by Harte (see [13], [14])."*
- **Those labels reduced to four triad types plus a no-chord symbol.** FACT, page 3: *"Only simple
  triads were used: triad extensions were ignored, and non-triadic chords were mapped to the closest
  triad type according to their correlation with 4 chord templates, for major, minor, augmented and
  diminished chords."*
- **The stream resampled onto a fixed time grid.** FACT — **the sentence straddles two sheets: it
  begins at the foot of page 3 and the clause quoted here is at the head of page 4.** *"the chord
  sequence was sampled at equal time intervals of 100 ms, such that sample times that fell between a
  chord start and end time were given the corresponding chord label, and any others were labelled N,
  for no chord."* (page 4.) The paper states the reason as simulating what audio would give: *"To
  simulate the kind of signal that would be obtained from audio data, with a view to future extension
  of the algorithm to work from audio…"* (page 3 into page 4).
  **★ CORRECTED AT THE CROSS-CHECK. FORMER WORDING, PRESERVED (#12): "FACT, page 3:"** — this side
  cited the 100 ms clause to page 3, where only the first half of the sentence sits. The first extract
  cites it correctly to page 4. This is the wrong-page class the hundred-and-seventieth entry's own
  check names, and the whole page-citation discipline exists against it. Recorded at §9.
- **NO bass and NO inversion information is required, and none is used.** FACT, page 2, quoted at
  §2.1 above. This is an assumption about the upstream in the negative direction: the method is
  indifferent to a distinction its upstream may have worked to establish.
- **NO metrical or phrase position is required, and none is used.** This is FACT by the paper's own
  admission in two places rather than by its silence — page 4: *"It is expected that this type of
  error would occur less frequently if the chords' position relative to the musical phrases were
  taken into account"*; and page 5: *"These two cases would benefit from longer temporal dependencies
  in the model, based on phrase lengths, since it is usually the chord or cadence at the end of a
  phrase that defines the key."*

### §3.2 What it HANDS downstream

- **A per-frame distribution over all twenty-four tonalities.** FACT, page 3 (decoding) and page 4:
  *"the output matrix containing the likelihood of each key at each time frame."* This is a full
  ranked surface with weights, not a point estimate, and it is what the upper plots of the paper's
  Figures 2 and 3 display.
- **A hard most-likely tonality sequence for the whole piece**, from Viterbi. FACT, page 3, and it is
  what the lower plots of Figures 2 and 3 display.
- **One overall tonality for the track.** FACT, page 4: *"the output matrix … was summed across the
  time domain, giving an overall likelihood value for each key. The key with the largest likelihood
  value was taken to be the key of the song."*
- **A segmentation, as a by-product and not as a separate output.** The paper treats the hard path as
  a segmentation and shows it as one, but reports no segmentation output format of its own.

### §3.3 Its own STATED scope and limits

- **Western repertoire where triads suffice.** FACT, page 2, quoted at §2.1.
- **Twenty-four major and minor tonalities only — modes do not fit.** FACT, page 4: *"several of the
  songs are modal, and do not directly fit this model of major and minor keys. Lydian and Mixolydian
  modes were treated as major, and Dorian and Aeolian as minor."* That mapping was applied to the
  ground truth for the evaluation; it is not a capability of the model.
- **The paper states that no ground truth for the per-frame half is available to its knowledge**, which
  is its own hedge and is kept here rather than hardened. FACT, page 4: *"Ground truth for the key changes
  in the Beatles' songs is not available to our knowledge, but the figures show that the algorithm is
  capable of extracting meaningful structure."* So the segmentation half is demonstrated and not
  measured.
- **The ground truth for the overall half is subjective and sometimes plural.** FACT, page 4: *"A
  subjectively-assessed ground truth is available at [15], which gives a musicological analysis of the
  Beatles' songs"*; and *"It should be noted that the ground truth often mentioned more than one key,
  in which case the first was taken to be the most important."*
- **The reported accuracy is not claimed to survive the move to audio.** FACT, page 5: *"The 91%
  accuracy reported here will almost certainly not hold when working with audio, but we will have an
  understanding of how audio-to-chord and chord-to-key errors differ."*
- **The stated weakness, in the paper's own words.** FACT, page 4, on the short spurious E major
  section: *"This demonstrates one of the weaknesses of our approach, that although the chords were
  most closely related to E major, the key of E major was not firmly established."*

---

## §4 — Claims labeled

**FACT — stated or measured in the paper, with its location.**

- F1. The hidden states are the twenty-four major and minor tonalities; the model is fully connected.
  (Page 2.)
- F2. An observation is an ordered pair of consecutive chords drawn from 48 triads plus a no-chord
  symbol, giving an emission table of 2401 × 24. (Pages 2 and 3.)
- F3. Initial state probabilities are uniform at 1/24. (Page 2.)
- F4. The starting tonality-transition matrix is derived from Krumhansl's tonality-profile
  correlations by circular shift, adding 1, and row normalisation. (Pages 2–3.)
- F5. The starting emission table is built from Krumhansl's chord-transition ratings, with same-chord
  values taken from the single-chord ratings and raised by 2, and every transition involving a
  non-diatonic chord set to 1 before normalisation. (Page 3.)
- F6. Minor-key emission values are copied from the major-key ratings at the same scale degrees.
  (Page 3.)
- F7. The correlation between the chord-transition ratings and the transition counts in the test data
  is 0.39 for major tonalities and 0.22 for minor, at 40 and 154 degrees of freedom respectively.
  (Page 3.)
- F8. Training is per song, by expectation-maximisation. (Page 3.)
- F9. Decoding produces both a Viterbi path and per-frame posterior probabilities. (Page 3.)
- F10. The evaluation corpus is 110 Beatles songs with hand-annotated chords, resampled at 100 ms.
  (Pages 1, 3 and 4.)
- F11. The accuracy values of Table 1, recorded at §5 below. (Page 5.)
- F12. Ten listeners took the probe-tone test. (Page 2, Box 1.)

**THEORY — established published theory the paper leans on rather than establishes.**

- T1. The hidden Markov model itself, its training by expectation-maximisation and its decoding by
  Viterbi, cited to Rabiner [9] and Cox [10]. (Pages 2 and 3.)
- T2. Krumhansl's probe-tone profiles, the correlations between them, the chord-transition ratings and
  the harmonic-hierarchy ratings, all cited to [1] at pages 38, 171, 193 and 195. (Page 2, Box 1, and
  the Appendix on page 6.)
- T3. Ordinary tonal music theory, cited to Taylor [11] and [12]. (Page 2.)

**CONJECTURE — asserted by the paper without a measurement or a citation that settles it.**

- C1. **That observing chord PAIRS models more temporal dependency than observing single chords, to
  the method's benefit.** This is the paper's headline design claim, stated in the abstract and again
  on page 2, and **no experiment comparing the pair model against a single-chord model is met anywhere
  in the six pages as read.** See §7, question Q1.
- C2. That triads without extensions are sufficient to define the tonality. (Page 2 — *"it was
  considered that"*, which is the paper's own signal that this is a judgment.)
- C3. That the increase of 2 applied to same-chord emissions is approximately optimal. Page 3 calls it
  *"experimentally found"*, and no experiment, range or sensitivity is reported.
- C4. That the pattern of about 16 s visible in the posterior plot corresponds to the repeated verse.
  (Page 4 — an observation on one plot of one song.)
- C5. That the errors attributed to phrase position would be reduced by a phrase-aware model.
  (Pages 4 and 5 — stated as an expectation.)

---

## §5 — Measured results, with corpus, metric and value as the paper states them

**The corpus.** Hand annotations of every chord in the first eight Beatles albums, provided by Harte
[13], [14] (page 3); the evaluated set is *"a data set of 110 Beatles songs"* (page 1 abstract) and
*"the 110 songs in the first 8 Beatles albums"* (page 4).

**The metric.** Percentage of songs whose single overall tonality, obtained by summing the per-frame
posterior over time and taking the largest, matches the first tonality named in Pollack's
musicological analysis [15].

**The values — the paper's Table 1, transcribed whole (page 5), captioned *"Percentage of songs
correctly classified with varying training"*.** The first three columns are which probabilities were
subject to training.

| Prior | Transition | Emission | Percent correct |
|---|---|---|---|
| yes | yes | yes | 27 |
| yes | yes | no | **91** |
| yes | no | yes | 18 |
| yes | no | no | 87 |
| no | yes | yes | 28 |
| no | yes | no | **91** |
| no | no | yes | 18 |
| no | no | no | 87 |

**The table's last row**, printed across the first three columns rather than under them: *"Expected
value for random choice of key"* — **4**.

**What the paper says about that table (page 5), quoted rather than summarised because the reading of
it is the paper's own.** *"The results in Table 1 verify the proposition that fixing the emission
probabilities gives the most accurate representation of the song, since allowing adjustment alters
the meaning of the hidden states. Training the prior state probabilities had little effect on the
number of songs correctly classified. This is most likely due to the step where the key probabilities
across the whole song were summed: the prior probabilities will only affect the first few frames and
will therefore have limited effect on key estimation. The suitability of the perception-based
initialisation was confirmed by the case with no training, where 87% of songs were correctly
classified. Training the transition probabilities for each song gave the optimum result of 91% of
songs correctly classified."*

**Two readings of that table that the paper does not make, and they are this side's arithmetic over
the paper's own values rather than the paper's statements.**

- Every value in the table is a percentage, and **no raw count of songs is met anywhere in the six
  pages as read.** 91% of 110 is 100.1, so the count behind the headline value cannot be read off the
  percentage alone. *(It can be reached another way: the discussion's enumeration of the errors names
  ten of them, and 100 correct out of 110 is 90.9%, which rounds to the reported 91. That route is set
  out at the end of this section, and it is this side's arithmetic over the paper's own sentences.)*
  **★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "…so the count behind the headline
  value is not recoverable from what is printed."** That contradicted this same section's own error
  enumeration four paragraphs below it.
- The emission column moves the result further than the other two: the four emission-trained rows
  stand at 27, 18, 28 and 18 against 91, 87, 91 and 87 for the four that fix it, a spread of 63 to 69
  points (§7.3). **What the other two columns do, stated at the values rather than as a bound over
  them:** with the emission FIXED, turning transition training on moves 87 to 91, four points, and
  turning prior training on moves nothing at all (91 against 91, 87 against 87). With the emission
  TRAINED, turning transition training on moves 18 to 27 and 18 to 28, nine and ten points, and
  turning prior training on moves 28 to 27 and leaves 18 at 18.
  **★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "Training the emission costs more
  than every other choice combined".** A comparison stated as a superlative where the values state it
  plainly.
  **★ AND CORRECTED AGAIN AT THE USER-ORDERED CHECK — §10. FORMER WORDING, PRESERVED (#12): "…while
  the prior and transition columns together never move a value by more than four points."** That is
  **false at this file's own transcription of Table 1**: with the emission trained, transition
  training moves 18 to 27 and 18 to 28, which is nine and ten points. The four-point reading holds
  only for the emission-fixed rows, and the sentence stated it over all of them.

**The confusion matrix.** FACT, page 4: *"Figure 4 shows the confusion matrix for the case where the
transition and prior probabilities were trained, but the observation probabilities were not. Only the
incorrect estimates are shown in the figure."* Its caption on page 5 adds *"Minor keys follow their
parallel major along the horizontal axis."* **This side did not count the plotted points and states
no count**; what the plot is for is named here, not tabulated.

**The paper's own account of every error (page 5), quoted because it is an enumeration and this side
did not verify it against the data.** *"Closer inspection of the ground truth and confusion matrix
reveal that all of the incorrect estimates can be explained, and none is unreasonably far from the
ground truth."* Then: three modal songs — two Mixolydian mistaken for the major tonality on their
fourth degree, *"due to their flattened 7th"*, and one with Dorian inflexions mistaken for the major
tonality on its seventh degree, *"due to its flattened 3rd and 7th"*; one song in A major mistaken for
E major, its dominant, where *"the chords that make up the song are B, E, A and D majors, which imply
both keys equally when there is no context"*; one song in A major mistaken for its subdominant,
*"explained by the particular stress on the flattened 7th degree of the scale, used here to give a
blues feel rather than a move to the subdominant key"*; and *"The remaining five incorrect key
estimates are for songs where more than one key is mentioned in the ground truth for the home key,
and it is one of these alternative keys that has been selected by the algorithm."*

*Those named classes sum to ten. Ten errors out of 110 songs leaves 100 correct, and 100 out of 110 is
90.9%, which rounds to the reported 91%. **That arithmetic is this side's**, the paper states neither
the sum nor the count. (★ CORRECTED AT THE USER-ORDERED CHECK — §10. FORMER WORDING, PRESERVED (#12):
"ten errors out of 110 songs is 90.9%", which names the error count and then gives the share of
CORRECT songs, as though they were the same quantity.)*

**The segmentation demonstration — no metric, and the paper says so.** Two songs are shown. In *I'll
Cry Instead*, page 4: *"the two bridge passages in D major, at 42 s to 52 s and 72 s to 82 s, have
been clearly separated."* In *I'm Happy Just to Dance With You*: *"the choruses (C♯ minor) and verses
(E major) have been extracted"*, with a spurious short E major section *"at about 103 to 105 s"* which
the paper presents as a weakness, and a repeated pattern in the posterior plot *"of approximately 16 s
in duration that is repeated once."*

---

## §6 — The perceptual-test tables, transcribed

The paper's Appendix on page 6 reproduces three tables from Krumhansl [1]. They are transcribed here
in full because the model's starting values are read directly out of them, so a later reader
comparing this project's own tables against a published source needs the numbers and not a pointer.

### §6.1 Table 2 — *"Krumhansl's correlations between key profiles (see [1], p. 38)"*

| Profile | C Major | C Minor |
|---|---|---|
| C major | 1.000 | 0.511 |
| C♯/D♭ major | −0.500 | −0.158 |
| D major | 0.040 | −0.402 |
| D♯/E♭ major | −0.105 | 0.651 |
| E major | −0.185 | −0.508 |
| F major | 0.591 | 0.241 |
| F♯/G♭ major | −0.683 | −0.369 |
| G major | 0.591 | 0.215 |
| G♯/A♭ major | −0.185 | 0.536 |
| A major | −0.105 | −0.654 |
| A♯/B♭ major | 0.040 | 0.237 |
| B major | −0.500 | −0.298 |
| C minor | 0.511 | 1.000 |
| C♯/D♭ minor | −0.298 | −0.394 |
| D minor | 0.237 | −0.160 |
| D♯/E♭ minor | −0.654 | 0.055 |
| E minor | 0.536 | −0.003 |
| F minor | 0.215 | 0.339 |
| F♯/G♭ minor | −0.369 | −0.673 |
| G minor | 0.241 | 0.339 |
| G♯/A♭ minor | −0.508 | −0.003 |
| A minor | 0.651 | 0.055 |
| A♯/B♭ minor | −0.402 | −0.160 |
| B minor | −0.158 | −0.394 |

### §6.2 Table 3 — *"Krumhansl's chord transition ratings (see [1], p. 193)"*

Rows are the first chord, columns the second. The rightmost column and the bottom row are headed *Ave*
in the table as printed. *(Whether those averages are Krumhansl's or the authors' is not stated at the
table and is not established here. ★ CORRECTED AT THE USER-ORDERED CHECK — §10. FORMER WORDING,
PRESERVED (#12): "are the paper's own averages", which attributed them to Noland and Sandler where the
table is captioned as Krumhansl's.)*

| First chord | I | ii | iii | IV | V | vi | vii | Ave |
|---|---|---|---|---|---|---|---|---|
| I | — | 5.10 | 4.78 | 5.91 | 5.94 | 5.26 | 4.57 | 5.26 |
| ii | 5.69 | — | 4.00 | 4.76 | 6.10 | 4.97 | 5.41 | 5.16 |
| iii | 5.38 | 4.47 | — | 4.63 | 5.03 | 4.60 | 4.47 | 4.76 |
| IV | 5.94 | 5.00 | 4.22 | — | 6.00 | 4.35 | 4.79 | 5.05 |
| V | 6.19 | 4.79 | 4.47 | 5.51 | — | 5.19 | 4.85 | 5.17 |
| vi | 5.04 | 5.44 | 4.72 | 5.07 | 5.56 | — | 4.50 | 5.06 |
| vii | 5.85 | 4.16 | 4.16 | 4.53 | 5.16 | 4.19 | — | 4.68 |
| Ave | 5.68 | 4.83 | 4.39 | 5.07 | 5.63 | 4.76 | 4.76 | — |

**The diagonal is blank in the printed table** — every cell where the first and second chord are the
same degree. That matters and it is taken up at §7, defect D3.

### §6.3 Table 4 — *"Krumhansl's harmonic hierarchy ratings for major, minor and diminished chords (see [1], p. 171)"*

| Chord | C Major context | C Minor context |
|---|---|---|
| C Major | 6.66 | 5.30 |
| C♯/D♭ Major | 4.71 | 4.11 |
| D Major | 4.60 | 3.83 |
| D♯/E♭ Major | 4.31 | 4.14 |
| E Major | 4.64 | 3.99 |
| F Major | 5.59 | 4.41 |
| F♯/G♭ Major | 4.36 | 3.92 |
| G Major | 5.33 | 4.38 |
| G♯/A♭ Major | 5.01 | 4.45 |
| A Major | 4.64 | 3.69 |
| A♯/B♭ Major | 4.73 | 4.22 |
| B Major | 4.67 | 3.85 |
| C Minor | 3.75 | 5.90 |
| C♯/D♭ Minor | 2.59 | 3.08 |
| D Minor | 3.12 | 3.25 |
| D♯/E♭ Minor | 2.18 | 3.50 |
| E Minor | 2.76 | 3.33 |
| F Minor | 3.19 | 4.60 |
| F♯/G♭ Minor | 2.13 | 2.98 |
| G Minor | 2.68 | 3.48 |
| G♯/A♭ Minor | 2.61 | 3.53 |
| A Minor | 3.62 | 3.78 |
| A♯/B♭ Minor | 2.56 | 3.13 |
| B Minor | 2.76 | 3.14 |
| C Dim | 3.27 | 3.93 |
| C♯/D♭ Dim | 2.70 | 2.84 |
| D Dim | 2.59 | 3.43 |
| D♯/E♭ Dim | 2.79 | 3.42 |
| E Dim | 2.64 | 3.51 |
| F Dim | 2.54 | 3.41 |
| F♯/G♭ Dim | 3.25 | 3.91 |
| G Dim | 2.58 | 3.16 |
| G♯/A♭ Dim | 2.36 | 3.17 |
| A Dim | 3.35 | 4.10 |
| A♯/B♭ Dim | 2.38 | 3.10 |
| B Dim | 2.64 | 3.18 |

**Table 4 carries major, minor and diminished triads and NO augmented triads** — thirty-six rows,
twelve of each of three types. The model's vocabulary is forty-eight chords, which is twelve of four
types. Taken up at §7, item D4, where the first writing of this point was withdrawn as a defect at the
read-back and what survives of it is recorded as a note.

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

**D1 — Box 1 states the probe-tone scale in the direction opposite to the one the model's own use
requires.** Box 1 on page 2 reads: *"Ten listeners were asked to judge how well each semitone fit
within a given major or minor key context, on a scale of 1 (very good) to 7 (very bad)."* On that
labelling a **higher** number is a **worse** fit. But page 3 takes the single-chord ratings of Table 4
and uses them directly as pre-normalised probabilities, higher meaning more likely, and Table 4 gives
C Major in the C Major context its highest value of the whole table, 6.66. **Under Box 1's stated
direction the tonic triad would be the worst-fitting chord in its own tonality.** The two cannot both
stand. *Which of them is wrong is not established here — that would need Krumhansl [1], which is not
held and was not read. The CONJECTURE, marked as one, is that Box 1's two parenthetical labels are
transposed.* **The bound this leaves: Box 1's stated direction is not usable as established, and a
later reader who needs the direction has to settle it at [1].** *(★ CORRECTED AT THE READ-BACK. FORMER
WORDING, PRESERVED (#12): "Nothing in this project may take the direction from Box 1 without settling
this at [1]." That wrote a rule for this project, and an extract states findings and rules nothing.)*

**D2 — Box 1 states two different scale ranges and calls the second one the same as the first.** Under
*Chord transition ratings*: *"Listeners were asked to judge the fit on a scale of 1 to 7."* Under
*Single chord ratings*, four lines later: *"listeners were asked to judge how well single chords fit
within a key, using the same scale of 0 to 7."* **1 to 7 and 0 to 7 are not the same scale.** No value
printed in Table 3 or Table 4 is below 2.00 — the lowest in Table 3 is 4.00 and the lowest in Table 4
is 2.13, both checked at the page — so the printed values do not discriminate between the two ranges.

**D3 — Box 1 claims the chord-transition test covered the no-transition case, and Table 3 shows no
such cell.** Box 1: *"Ratings were given for all possible diatonic chord transitions within a major
key, including the case where no transition is made, e.g. dominant-dominant or tonic-tonic."* **Table
3's diagonal is blank at every one of the seven positions.** And the paper's own method on page 3
takes the same-chord values from Table 4 instead — *"The pre-normalised probabilities for staying on
the same chord, for diatonic chords within a key, were taken from the ratings of individual chords
within a key, given in Table 4 in the Appendix"* — which is what a reader would do precisely because
Table 3 does not carry them. **So the paper's own construction contradicts Box 1's claim about its
own source test.**

**D4 — WITHDRAWN AT THE READ-BACK AS A DEFECT, AND WHAT SURVIVES IS A NOTE.** The observation stands:
the vocabulary is forty-eight chords, twelve each of four triad types, and Table 4 rates thirty-six,
twelve each of three — the augmented triads have no rating. **But the paper flags the gap and fills
it**, which the first writing of this section did not acknowledge. Page 3: *"These cover only the
diatonic chords of major keys, but the model includes all major, minor, augmented and diminished
triads as well as the possibility of there being no chord, so some additional numerical values were
required."* And rule 3 of the construction sets every transition involving a non-diatonic chord to 1,
which reaches every augmented triad. **What survives as a note, and it is a small one:** the flagging
sentence is written about Table 3 and the diatonic chords of major keys, and no sentence of the paper
names the augmented triads specifically, so the reader has to see for himself that rule 3 covers them.

*★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "**D4 — the chord vocabulary is
forty-eight and the rating table covers thirty-six.** The model admits major, minor, augmented and
diminished triads (page 2); Table 4 rates major, minor and diminished only. The paper does not remark
on this. It is not a contradiction, because every augmented triad is non-diatonic and rule 3 on page 3
sets every non-diatonic transition to 1 — but **the paper never states that this is why**, and a reader
checking the construction against the table finds twelve chords with no source value and no sentence
covering them." Its claim that the paper does not remark on the gap is refuted by the page-3 sentence
quoted above, which this side had already transcribed into §2.2 of this same file — so it was
contradicted from inside the file before the read-back reached it.*

**D5 — WITHDRAWN AT THE READ-BACK. THE DOUBT WAS MANUFACTURED AND THE PAPER SETTLES IT.** Page 4 reads
*"Table 1 shows the percentage of correctly assigned overall keys for the 110 songs in the first 8
Beatles albums, with different HMM parameters trained."* That is a definite description of the whole
album set, not of a subset drawn from it, and it stands beside page 3's *"every chord in all of the
first 8 Beatles albums"* without tension.

*★ FORMER WORDING, PRESERVED (#12): "**D5 — the paper's count of the songs and the count of the
annotations are not stated to be the same set.** Page 3 says the annotations cover *"every chord in all
of the first 8 Beatles albums"*; page 4 says the evaluation used *"the 110 songs in the first 8 Beatles
albums"*. Whether 110 is all of them or a subset that survived some filter is not said."*

**D6 — two degrees-of-freedom values are reported and the asymmetry between them is not explained.**
Page 3 gives 40 for major tonalities and 154 for minor, for correlations computed the same way — *"the
correlation between the chord transition ratings and the corresponding number of transitions present
in our test data"* — and the second is nearly four times the first. The paper says what was correlated
with what; what it does not say is what differs between the major and minor cases such that the two
populations are of such different sizes.

*★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "…a ratio of nearly four, with no
statement of what was correlated against what in each case." The paper does state what was correlated
against what, in the sentence now quoted above; only the asymmetry is unexplained.*

### §7.2 What the paper leaves without a value — the questions a later reader must not assume are answered

**Q1 — THE PAPER'S CENTRAL DESIGN CLAIM IS NOT MEASURED ANYWHERE IN THE PAGES AS READ.** The abstract
and page 2 both assert that observing chord pairs extends the temporal dependency further than
observing single chords. **A comparison of a pair-observation model against a single-chord-observation
model is met nowhere in the six pages as read.** Table 1 varies only which of the three parameter sets
are trained; every row of it is the pair model. So the value of the paper's own novelty is left without
a value by the paper. *Stated as an absence over the six pages as read, which is the only population
this side examined. (★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "This is the
sharpest thing this read found" — a superlative over this side's own acts, which cadence 6 forbids.)*

**Q2 — no held-out separation is met in the pages as read, and the question is not discussed there.**
Training is per song, by expectation-maximisation, on the song being decoded, and the accuracy is
reported over the same 110 songs. The paper states the procedure plainly, and whether fitting and
grading on the same material affects the reported value is raised nowhere in the pages as read.
*Recorded as what the paper does and does not say. No verdict is taken here on what it implies.*

**Q3 — no uncertainty is attached to any reported value in the pages as read.** No confidence
interval, no repeat run and no variance across albums or songs is met in them. With 110 songs, the
difference between 87% and 91% is a handful of songs, and the paper calls 91% *"the optimum result"*
without saying whether that difference is distinguishable from noise.

**Q4 — the cost of the 100 ms frame grid is not measured in the pages as read.** The grid is chosen to
simulate audio. Whether the same model on a beat grid, a chord-event grid or any other grid does
better or worse is not reported in them, although page 3 mentions the beat-by-beat level in passing
when justifying the same-chord boost.

**Q5 — the boost of 2 has no experiment reported behind it.** Page 3 calls it *"experimentally found"*,
and neither the experiment, the range searched, nor the sensitivity of the result to it is reported in
the pages as read.

**Q6 — the segmentation half carries no metric in the pages as read.** The paper states that no ground
truth for tonality change is available to its knowledge. The segmentation claims this side met are the
two hand-inspected songs of pages 3 and 4, and no other evidence for that half is met in the six pages
as read.

**Q7 — nothing about computational cost is met in the pages as read.** The emission table is 2401 × 24
and is trained per song; no timing, no complexity statement and no statement of how long a song takes
is met in them.

**Q8 — what "no chord" does to the tonality estimate is not examined in the pages as read.** The
no-chord symbol enters the vocabulary, is given the same function in every tonality (page 3), and is
assigned to every unlabelled 100 ms sample. No result separating songs by how much no-chord they carry
is met in them.

### §7.3 The result in this paper that is both measured and structural

**Fixing the emission table is worth between 63 and 69 percentage points on this corpus**, read off
Table 1 by pairing each emission-trained row against the row that differs from it only in that column:
27 against 91 is 64; 18 against 87 is 69; 28 against 91 is 63; 18 against 87 is 69. *The pairing and
the subtraction are this side's; the eight values are the paper's.*

**★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "worth between 59 and 73 percentage
points".** Neither bound was derived from the four differences, which are 63, 64, 69 and 69. This was
a number put on this side's own reading without deriving it. *(★ CORRECTED AGAIN AT THE USER-ORDERED
CHECK — §10. FORMER WORDING, PRESERVED (#12): "…and it is the one defect of that class the read-back
struck in this file." It was not: §8.2 item 7 records a second instance of the same class, found
inside §8.1 in the same sweep, and §10 records a third. The sentence went false inside this file.)*

The paper's own explanation is that training the emission destroys the identification of the hidden
states with tonalities (page 3, quoted at §2.3), which is a statement about what the states MEAN
rather than about how well the model fits. **What the paper establishes is the accuracy gap; it makes
no statement about the trained model's likelihood, and none is made here either.**

*★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "the model trained end to end fits
the data better in the likelihood sense and answers the question worse." The first half of that is a
property of the training algorithm that the paper does not state and this read did not check; only
the second half is the paper's.*

This is the result in this paper that both carries a measured value and bears on how a decoder of
this kind should be fitted, rather than on how well this particular decoder does. *That it is the only
such result is not claimed — it is the only one this read found, across the six pages as read.*

---

## §8 — The read-back and the sweep, written in the act that ran them

This section was absent when §1 to §7 were first written, and it is added as its own edit, which is
what the procedure asks: the closing section records what the read-back and the sweep found, so it
cannot be written before they have run.

### §8.1 What the read-back was

**Every one of the six pages was re-opened**, in three requests — pages 1–2, then 3–4, then 5–6 — and
every transcribed value, every quoted sentence and all three appendix tables were compared at the
page. **All six pages carry a value, a table or a quoted sentence, so no page was left out of the
read-back.** Every image was present and legible at each request, checked at the images and not at
the calls' success lines.

**No transcribed value of the paper's moved.** Named rather than counted, what was checked digit for
digit: Table 1's eight accuracy values and its random-choice value; Table 2's twenty-four rows at two
values each; Table 3's forty-two rated cells (seven rows by seven columns, less the seven blank
diagonal positions), its fourteen averages (one per row and one per column, the corner where those two
meet being blank) and the blank diagonal itself; Table 4's
thirty-six rows at two values each; the correlations 0.39 and 0.22 with their 40 and 154 degrees of
freedom; the worked emission example 3.62 + 2 = 5.62 and its source value in Table 4; the matrix
dimensions (48 + 1)² × 24 = 2401 × 24; the uniform initial probability 1/24; the 100 ms sampling
interval; the 110 songs; the 91% and 87% accuracies; and the times 42 s, 52 s, 72 s, 82 s, 103 s,
105 s and the 16 s repeated pattern.

**One thing the read-back confirmed rather than corrected:** no printed page number is visible on any
of the six sheets, so §0's statement that pages are cited by position in the held file stands, checked
at all six rather than assumed from the first.

### §8.2 What the read-back and the sweep struck in THIS side's own writing

**The corrections are named rather than counted, and each is made at its own site above with the
former wording preserved (#12).** *(★ The first writing of this line opened "Six corrections"; a
seventh was then found inside §8.1 and is item 7 below, so the count went stale in the act of being
written. Former wording preserved (#12): "**Six corrections, named rather than counted**" — which also
stated a count in the same breath as the rule against stating one.)*

1. **A NUMERIC ERROR OF THIS SIDE'S.** §7.3 claimed that
   fixing the emission table is worth *"between 59 and 73 percentage points"*. The four differences
   are 64, 69, 63 and 69, so the range is **63 to 69**. Neither printed bound came from the values.
   **This is a number put on this side's own reading without deriving it** — the degradation tell the
   hundred-and-seventy-first entry reports firing repeatedly across both of its members — and it is
   recorded here as the same tell rather than as a slip.
2. **A MANUFACTURED DEFECT, WITHDRAWN.** D5 claimed the paper does not say whether its 110 songs are
   all the songs of the first eight albums. Page 4 says *"the 110 songs in the first 8 Beatles
   albums"*, which settles it. The defect was this side's and not the paper's.
3. **AN OVERSTATED DEFECT, CORRECTED TO A NOTE.** D4 claimed the paper *"does not remark"* on its
   rating table covering thirty-six chords against a vocabulary of forty-eight. It does remark on the
   gap, in a page-3 sentence **this side had already transcribed into §2.2 of this same file** — so the
   claim was contradicted from inside the file before the read-back reached it.
4. **A NARROWING.** D6 claimed the paper gives *"no statement of what was correlated against what"*
   behind its two degrees-of-freedom values. It does state that; what it does not explain is the
   asymmetry between 40 and 154.
5. **AN INTERNAL CONTRADICTION OF THIS SIDE'S, TWO PARAGRAPHS WIDE.** §5 said the raw count of
   correctly classified songs *"is not recoverable from what is printed"*, and four paragraphs below it
   this same section recovers it from the paper's own enumeration of the ten errors.
6. **A RULE WRITTEN WHERE A BOUND BELONGED.** D1 closed with *"Nothing in this project may take the
   direction from Box 1 without settling this at [1]"*, which legislates. An extract states findings
   and rules nothing, so it now states the bound instead.
7. **★ AND THE TELL OF ITEM 1 FIRED AGAIN INSIDE THIS SECTION.** The first writing of §8.1 above said
   the read-back checked *"Table 3's fifty-six rated
   cells, its fifteen averages"*. **Table 3 has forty-two rated cells and fourteen averages** — seven
   rows by seven columns less the seven blank diagonal positions, and one average per row and per
   column with the corner between them blank. Both numbers were stated without being derived, in the
   very paragraph that reports the tell, and neither matches the table this side had just transcribed
   in full at §6.2. **The corrected sentence now carries the derivation beside each number rather than
   the number alone.** *Nothing here establishes that this is the last instance; it is the last one
   this sweep found.*

### §8.3 What the sweep for absolutes changed

The absolutes this sweep met were read at their lines. **The ones that were left standing are the ones
an object establishes:** the six page images present, the three tables transcribed in full, Table 3's
blank diagonal at all seven positions, and the lowest printed values of Tables 3 and 4 — each checked
at the page at the read-back.

*★ CORRECTED AT THE USER-ORDERED CHECK — §10. FORMER WORDING, PRESERVED (#12): "Every absolute in this
file was read at its line." **That claim is refuted by §10 itself**, which found an absolute this sweep
did not reach — the "never move a value by more than four points" sentence in §5 — and which is
therefore evidence that this sweep's reach was narrower than the word "every" states.*

**The ones that were rewritten were negatives over the paper**, and each now says *met nowhere in the
six pages as read* rather than *never*, *nowhere* or *not anywhere in the paper*. That reach is the
one this side actually has: six pages, read whole twice. The rewritten sites are Q1, Q2, Q3, Q4, Q5,
Q6, Q7 and Q8, the raw-count sentence in §5, and C1 in the labeled-claims list.

**The superlatives over this side's own acts were struck**, on cadence 6's rule that a superlative not
derived is not asserted, and they are named rather than totalled: *"This is the sharpest thing this
read found"* at Q1; *"Training the emission costs more than every other choice combined"* at §5,
replaced by the values that state the comparison plainly; and *"the one result in this paper"* at §7.3,
which now says what it can support — the only one this read found. *(★ CORRECTED AT THE USER-ORDERED
CHECK — §10. FORMER WORDING, PRESERVED (#12): "**Two superlatives over this side's own acts were struck
outright**", which opened with a count of two and then named three.)*

**One claim was struck because it is not this paper's and was not checked:** §7.3's assertion that the
end-to-end trained model *"fits the data better in the likelihood sense"*. That is a property of the
training algorithm, not a statement the paper makes, and this read did not check it.

### §8.4 The bound on this section

**The read-back and the sweep are this side re-reading its own writing against the paper.** They
establish what they found and not that there is nothing left to find: the same side wrote the text and
checked it, which is not an independent read. The independent read is the cross-check against the
first extract, which is step 7 of the procedure and came after this file had landed; **its record is
§9 below.** *(★ CORRECTED AT THE USER-ORDERED CHECK — §10. FORMER WORDING, PRESERVED (#12): "…and that
has not happened yet — it is step 7 of the procedure, it comes after this file has landed, and its
record will be this file's §9." True when written, and made false by §9's arrival — the staleness class
rather than the count class.)*

---

## §9 — The cross-check against the first extract, written in the act that ran it

The first extract, `reading_pass/extracts/noland-sandler-2006-key-estimation-using-a-hidden-markov-model.md`,
**25,525 bytes**, was opened for the first time AFTER this file had landed at 50,600 bytes, which is
step 7 of the procedure and the whole point of the ordering. It is dated 2026-09-05 and declares itself
read at the object, all six pages, as page images.

**The paper was re-opened to resolve disagreements, in two requests — pages 3–4, then page 1.** Every
disagreement below was settled at the page, never by preferring one extract to the other. *(★ CORRECTED
AT THE USER-ORDERED CHECK — §10. FORMER WORDING, PRESERVED (#12): "**Two pages of the paper were
re-opened… — page 1 and pages 3–4.**" Two REQUESTS were made and they cover THREE sheets; the sentence
counted the requests and called them pages.)*

### §9.1 Every numeric value both extracts transcribed agreed, digit for digit

Named rather than counted: Table 1's eight accuracy values and its random-choice value; the
correlations 0.39 and 0.22 with their 40 and 154 degrees of freedom; the matrix dimensions (48 + 1)²
× 24 = 2401 × 24; the worked emission example 3.62 + 2 = 5.62; the uniform initial probability 1/24;
the 100 ms sampling interval; the 110 songs of the first eight albums; the held file's 417,537 bytes;
the six pages; the Table 2 values the first extract quotes — **nine of them**: 0.651, 0.591, 0.591 and
0.536 in the C major column, and 0.651, 0.536, 0.511 and 0.339 twice in the C minor column — each
checked against this file's own full transcription of that table at §6.1; and the times 42 s, 52 s,
72 s, 82 s, 103 s, 105 s and the 16 s repeated pattern. **Not one numeric disagreement was found.**

*★ CORRECTED AT THE USER-ORDERED CHECK — §10. FORMER WORDING, PRESERVED (#12): "the eight Table 2
values the first extract quotes". **The parenthesis beside that word listed nine**, and nine is what
the first extract quotes. A count stated without being derived, contradicted by the list standing in
the same sentence — the third instance in this file of the tell §8.2 reports.*

### §9.2 The disagreements — none is a value transcribed from the paper, and they run in both directions

*★ CORRECTED AT THE USER-ORDERED CHECK — §10. FORMER WORDING, PRESERVED (#12): "none of them carries a
digit". **The fifth disagreement below is a page citation, which is exactly a numeral** — page 3
against page 4 — so the digit test was refuted by this section's own list. What holds is that no value
transcribed from the paper disagreed.*

**THREE GO AGAINST THE FIRST EXTRACT. This file does not correct them there**, on the standing ground
that rewriting another read's text destroys what the doubling compares. They stand with the user.

- **A word altered inside a quotation.** The first extract quotes, cited to page 1 §1, *"This paper
  describes a novel technique for estimating the key of a musical recording…"*. **Page 1 prints *"a
  new technique"***. *Novel* is the abstract's word — *"A novel technique to estimate the predominant
  key in a musical excerpt is proposed"* — imported into the introduction's sentence. Resolved at page
  1, re-opened for this.
- **A second word altered inside a quotation.** The first extract quotes *"the likelihood of that
  transition occurring in that key"*. **Page 3 prints *"the likelihood of the transition occurring in
  that key"***. Resolved at page 3, re-opened for this.
- **★ A QUOTATION TRUNCATED MID-SENTENCE AND CLOSED WITH A FULL STOP, WITH NO ELLIPSIS — AND THIS IS
  THE ONE OF THE THREE THAT COULD COST A LATER READER SOMETHING.** The first extract quotes *"More
  complex chords have been excluded from the model since chords that are not based on triads are very
  rare in the Western music repertoire for which this analysis is intended."* The paper does not stop
  there: it continues *", and it was considered that the sequence of underlying triads, excluding
  extensions, is sufficient to define the key."* **The dropped clause is where the paper marks its own
  sufficiency claim as a judgment** — *"it was considered that"* — and it is on that marking that this
  file labels the sufficiency claim CONJECTURE at C2. A reader of the first extract alone sees the
  vocabulary restriction defended by a rarity claim and does not see that the paper itself flags the
  second half as a consideration. **No value moves**, which is what separates this from the
  load-bearing case the hundred-and-seventy-first entry records on row 8.

**TWO GO AGAINST THIS SIDE, AND BOTH ARE CORRECTED ABOVE AT THEIR SITES WITH THE FORMER WORDINGS
PRESERVED (#12).**

- **An inserted word inside a quotation.** This side wrote *"on either a frame-by-frame or a
  beat-by-beat level"*; **page 3 prints *"on either a frame-by-frame or beat-by-beat level"***. The
  first extract had it right. Corrected at §2.2.
- **A quotation cited to the wrong page.** This side cited the 100 ms sampling clause to page 3. **The
  sentence begins at the foot of page 3 and the quoted clause is at the head of page 4**, which is
  where the first extract cites it. Corrected at §3.1.

### §9.3 What the doubling produced that neither read had alone

**★ WHAT THE FIRST EXTRACT HAS AND THIS ONE DID NOT — AND IT IS THE FINDING THAT MAKES THE PAPER
CENTRAL.** The first extract reads a DIRECTION out of Table 2 that this read transcribed without
interpreting: in the C major column the highest value after C major itself is **A minor at 0.651**,
ahead of **F major and G major at 0.591 each**; in the C minor column the highest after C minor itself
is **E♭ major at 0.651**. So the initial tonality-transition matrix makes **the relative minor the
nearest change from a major tonality, ahead of both the dominant and the subdominant, and the relative
major the nearest change from a minor tonality.**

**This side verified that reading at the object rather than accepting it.** The values are in this
file's own §6.1 transcription and agree digit for digit — nine of them, named at §9.1; and the
construction the paper states —
add 1 to every value, then normalise each row to sum to 1 — is monotone, so it preserves the ordering
the correlations carry, and the conclusion follows from the table. **CONFIRMED.** *That this side
transcribed the table and drew nothing from it is a gap in this read, not a disagreement, and it is
recorded as a gap.*

**Two smaller things the first extract has and this one lacks:** the observation that the per-song
training is unsupervised, so the transition table being fitted on the song it decodes involves no
label leakage even though no held-out split exists — a precision this file's Q2 does not carry; and
the counts of the paper's sections, references, figures and tables.

**WHAT THIS READ HAS AND THE FIRST EXTRACT DOES NOT.** Named rather than counted: the three
inconsistencies inside and around Box 1 (D1, the probe-tone scale direction against the model's own
use; D2, *"a scale of 1 to 7"* then *"the same scale of 0 to 7"*; D3, Box 1's claim that the
transition test covered the no-transition case against Table 3's blank diagonal); **Q1, that the
paper's headline design claim — chord pairs over single chords — is measured nowhere in the six pages
as read**; the full transcription of Tables 2, 3 and 4; and the four row pairings of Table 1 that put
the worth of fixing the emission at 63 to 69 percentage points.

**AND ONE DERIVED VALUE THAT TWO BLIND READS REACHED INDEPENDENTLY.** Neither the raw count of
correctly classified songs nor the count of errors is printed anywhere in the paper. Both extracts
derive **ten errors** from the discussion's own enumeration — three modal, one dominant, one
subdominant, five plural-ground-truth. The first extract states it as *"The ten errors"*; this file
derives it at §5 and reconciles it against the reported 91%. **Two reads, written without sight of
each other, reaching the same underived-in-the-paper value.**

### §9.4 What the first extract asks of a second pass, and what this check did not do

**The first extract poses no explicit question to the second pass.** Its centrality section states
that a second extraction is OWED and names the ground; its finding (4) states a bound rather than a
question — that the Krumhansl tables printed here are a secondary reproduction and nothing is carried
out of them as an established fact of Krumhansl 1990. **This side manufactures no question where the
first extract asked none**, and it takes no position on that bound, `FRAMEWORK.md` and the R-8 row
being unopened here.

**Nor does this side check the half of the first extract that reaches outside the paper.** That
extract's findings reach `FRAMEWORK.md` §S4(b), the candidacy row, the slice derivation, the design
points and the legacy register entries D-347, D-348 and D-525. **This side opened none of those and
takes no position on any of it.** What is checked here is the two reads against the paper, and nothing
else.

**This check fetched no page image beyond the two re-reads named at the head of this section, opened
no source of either extract, ran no web access, swept no repository, and edited no file but this one.
It moved no verdict, routed nothing, flipped no row, and changed no transcribed value.**

---

## §10 — The user-ordered fact- and source-check, run after this file had landed

The user's standing rule of 2026-09-12 extends the pre-landing check to landed work on four axes:
completeness, coherence, correctness, and misuse of hyperbole and absolutes. He ordered it on this
sitting's writing after this file had landed at **59,760 bytes**, and **this file was re-read WHOLE as
landed, at the device's own copy staged back**, not at this side's container copy.

**What it found, corrected above at their sites with every former wording preserved (#12).**

- **★ A CLAIM REFUTED BY THIS FILE'S OWN TRANSCRIPTION OF TABLE 1, and it is the most substantive
  thing this check struck.** §5 read *"the prior and transition columns together never move a value by
  more than four points."* **With the emission trained, turning transition training on moves 18 to 27
  and 18 to 28 — nine and ten points.** The four-point reading is true only of the emission-fixed
  rows. The sentence is replaced by the values themselves in both conditions, which is what the rule
  against unstated bounds asks for.
- **★ THE COUNT TELL, A THIRD TIME, AND THIS ONE CONTRADICTED THE LIST BESIDE IT.** §9.1 said the
  cross-check checked *"the eight Table 2 values the first extract quotes"* — and the parenthesis in
  the same sentence listed **nine**. §9.3 carried the same eight. Both now say nine and name them.
  **§8.2 item 1 recorded the first instance, item 7 the second, and this is the third; §7.3's claim to
  have struck "the one defect of that class" is corrected there too.**
- **An absolute about this side's own sweep, refuted by this check.** §8.3 opened *"Every absolute in
  this file was read at its line."* The four-point sentence above is an absolute that sweep did not
  reach, so the claim is narrowed to what it can support.
- **A count of two followed by three named members.** §8.3's *"Two superlatives … were struck
  outright"*, which then named three.
- **A count of requests called a count of pages.** §9's *"Two pages of the paper were re-opened … page
  1 and pages 3–4"* — two requests, three sheets.
- **A quantity named and then given as its complement.** §5's *"ten errors out of 110 songs is 90.9%"*
  — ten is the error count and 90.9% is the share of correct songs.
- **A sentence made false by §9's own arrival.** §8.4 still said the cross-check *"has not happened
  yet"*. Staleness rather than the count tell, and recorded as such.
- **Three overstatements of attribution or weight, none of them numeric**: *"the paper's most
  load-bearing structural statement"* at §2.3; *"quoted whole because each clause carries an
  assumption"* at §2.2, where not every clause does; and Table 3's *Ave* column and row called *"the
  paper's own averages"* at §6.2, where the table is captioned as Krumhansl's and the paper does not
  say whose the averages are.
- **A relay stated as established.** The banner called this row 26 of the Task B L2 slice; that
  membership comes from the handoff line and the first extract, and neither the progress record nor
  the slice derivation was opened here. Now marked as a relay.
- **A formatting artifact.** Table 1's last row carried a stray asterisk in the transcription, a
  footnote marker with no footnote; it is now set out as the printed row it is.
- **★ A TEST THAT THE LIST BESIDE IT REFUTED, found when this check reached the handoff entry that
  carries the same sentence.** §9.2 was headed *"none of them carries a digit"* over a list whose fifth
  member is **a page citation — page 3 against page 4, which is exactly a numeral**. The claim the
  sentence was reaching for is that no value transcribed from the paper disagreed, and it now says
  that. **This is the second time in this file that a general statement was refuted by the enumeration
  standing next to it** — the first being the *"eight Table 2 values"* above — and the two together are
  the shape a next side should look for: a summary sentence written over a list, and not checked
  against it.

**What this check did NOT do.** It fetched no page image, opened no paper, opened the first extract
not at all, ran no web access, swept no repository, and **edited no file but this one**. It moved no
verdict, routed nothing, flipped no row, and **changed no transcribed value of the paper's**: every
value in Tables 1 to 4, every quotation, every correlation and every time stands exactly as it was
first landed. **It reaches this file and nothing else.**

**The bound.** It is a second pass over this side's own writing by the same side, not an independent
read, so **it establishes what it found and not that there is nothing left**. That is not a formality
here: this check found a claim the pre-landing sweep had walked past, in a section whose own sentence
said every absolute had been read at its line.

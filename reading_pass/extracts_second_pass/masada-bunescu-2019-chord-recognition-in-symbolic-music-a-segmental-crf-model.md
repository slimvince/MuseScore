# Second extraction — Masada & Bunescu, "Chord Recognition in Symbolic Music: A Segmental CRF Model, Segment-Level Features, and Comparative Evaluations on Classical and Popular Music"

**Row 10 of Task B's L2 slice. Second independent pass, written under
`cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, by the eight-step procedure of the
hundred-and-sixty-ninth handoff entry's §3.**

---

## §0 — What was read, and the bound on this read's independence

**What was read at the object.** The held file
`docs/research_papers/masada_bunescu_2019_tismir_segmental_crf_chord_recognition.pdf`, 1,289,352
bytes at a listing of `docs/research_papers/` this side ran, staged through the bridge and read as
page images with the file tools. **All nineteen pages, whole.** The page count was established at
the tool by a deliberately out-of-range request, which answered *"PDF has 19 pages"*. Every page
image was checked for presence and legibility at the image itself, never at the call's success line.

**What was NOT opened before this file's first landing.** The first extract of this row —
`reading_pass/extracts/masada-bunescu-2019-chord-recognition-in-symbolic-music-a-segmental-crf-model.md`,
**50,006 bytes** at the same kind of listing — was not opened, searched or staged before step 7. Its
size and its file name are all this side knew of it while §1 to §7 were written.

**The independence bound, written down rather than claimed away.** This read is not blind, and the
contamination is named:

- **The candidacy row was read, and it states a conclusion.** `reading_pass/candidacy_upgrades.md`
  line 72 gives this row as *"Masada & Bunescu, TISMIR 2(1) 2019, chord recognition in symbolic
  music: a segmental CRF model"*, admitted, with the reason *"The segmental CRF; the machinery of
  DP-C's chosen answer and the source of V5 and of DP-C's segmental gains. Symbolic, on our
  repertoire's kind of input."* That sentence was read in the act of finding out what row 10 is, and
  it carries a judgment about the paper's place in the record. **This side could not have identified
  the row without it.**
- **Four predecessor handoff entries were read whole at boot** — the hundred-and-sixty-ninth,
  hundred-and-seventy-second, hundred-and-seventy-third and hundred-and-seventy-fourth. **This side
  met no mention of this paper, its authors or its content in any of the four as read**; the members
  they describe are rows 27, 26, 30 and 5. *(★ CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING,
  PRESERVED (#12): "None of the four names this paper, its authors or anything about its content".
  **A negative over four whole entries stated as a search result where the act was a reading.**)*
- **The progress record was NOT opened**, at all. Its verdict cells would state the first extract's
  conclusion; they were not read. `reading_pass/l2_slice_reading_progress.md` is untouched by this
  side.
- **`FRAMEWORK.md` was NOT opened, at all**, nor the slice derivation, nor the findings surface, nor
  `docs/research_papers/BIBLIOGRAPHY.md`. **So on the whole half of the question that asks what the
  RECORD says about this paper, this read is silent — not a second opinion.** DP-C and V5 are named
  in the candidacy row above and are checked at no object here; this read takes no position on
  either.
- **No sweep of the repository was run for this paper** — not for its authors, not for its title,
  not for any of its values.

**The bound on every negative statement in this file.** Where this file says the paper does not
state something, the claim reaches **the nineteen pages as read** and no further. It is not a claim
about the published version of record, which this side did not obtain (see §1's identity finding).

---

## §1 — What the paper is, and one finding at the identity axis

**Printed title, page 1:** *"Chord Recognition in Symbolic Music: A Segmental CRF Model,
Segment-Level Features, and Comparative Evaluations on Classical and Popular Music"*.

**Authors:** Kristen Masada and Razvan Bunescu, both marked with an asterisk resolved in the page-1
footnote as *"School of Electrical Engineering and Computer Science, Ohio University, Athens, OH"*.

**★ THE HELD OBJECT IS A PREPRINT, NOT THE PUBLISHED ARTICLE THE RECORD'S ROW NAMES.** Three things
on page 1 establish it, and they are quoted rather than summarised:

- The left margin carries **`arXiv:1810.10002v2 [cs.SD] 26 Oct 2018`**.
- The citation header reads *"Masada, K. and Bunescu, R. (**2018**). … Transactions of the
  International Society for Music Information Retrieval, **V(N), pp. xx–xx**, DOI:
  https://doi.org/**xx.xxxx/xxxx.xx**"* — **the year is 2018 and the volume, issue, page range and
  DOI are unfilled placeholders.**
- The type slug above the title reads **`ARTICLE TYPE`**, itself an unfilled placeholder.

**The record's row calls it TISMIR 2(1) 2019.** That may well be correct of the published article;
what is established here is only that **the held file is not it**. Stated at the width of the act
that produced it: **a volume, an issue, a page range and a DOI are met nowhere in the nineteen pages
as read, and the only year the object gives itself is 2018.** Consequences a later reader needs:
**no printed page number of the published article can be cited from this object** — this file
therefore cites by the preprint's own page numbers, 1 to 19 — and **any difference between preprint
and published text is unmeasured here.**

*(★ CORRECTED AT THE SWEEP, BEFORE THIS FILE LANDED. FORMER WORDING, PRESERVED (#12): "**no page of
the held file carries a volume, an issue, a page range, a DOI or the year 2019**". **That is a
negative over nineteen pages stated wider than the act that produced it** — this read met no such
value, which is not the same as having searched every page for one. Cadence 7's own class.)*

**A second, smaller inconsistency in how the paper names itself.** The running head on pages 2
through 19 reads *"A Segmental CRF Model for Chord Recognition in Symbolic Music"* — the two halves
of the page-1 title in the reverse order, and without the second and third clauses. **So the object
carries TWO distinct forms of its own title**: the full one, printed identically at the page-1 title
and inside the citation header above it, and the running head's shortened, reversed form. No value
moves on this; it is recorded because a later reader citing "the title" must say which one.

*(★ CORRECTED AT THE USER-ORDERED CHECK, AGAINST PAGE 1 RE-OPENED. FORMER WORDING, PRESERVED (#12):
"**Three forms of the title therefore appear in one object**: the page-1 title, the citation header's
copy of it, and the running head." **The citation header's copy is word-for-word the page-1 title**,
so counting it as a third FORM counted an identical copy as a variant. There are two forms in three
places.)*

**Abstract, quoted whole because the body sections develop it:** *"We present a new
approach to harmonic analysis that is trained to segment music into a sequence of chord spans tagged
with chord labels. Formulated as a semi-Markov Conditional Random Field (semi-CRF), this joint
segmentation and labeling approach enables the use of a rich set of segment-level features, such as
segment purity and chord coverage, that capture the extent to which the events in an entire segment
of music are compatible with a candidate chord label. The new chord recognition model is evaluated
extensively on three corpora of classical music and a newly created corpus of rock music.
Experimental results show that the semi-CRF model performs substantially better than previous
approaches when trained on a sufficient number of labeled examples and remains competitive when the
amount of training data is limited."*

**Keywords, as printed:** harmonic analysis, chord recognition, semi-CRF, segmental CRF, symbolic
music.

**Structure.** Nine numbered sections over twelve pages — introduction and motivation; the semi-CRF
model; chord recognition labels; chord recognition features; datasets; experimental evaluation;
related work; future work; conclusion — followed by notes, acknowledgments, references, and **three
appendices over pages 13 to 19**: A, types of chords in tonal music; B, figuration heuristics; C,
the chord recognition features in full. **The appendices are not supplementary matter here: the
whole feature definition lives in Appendix C, and §4 of the body is a one-paragraph summary that
points at it.**

---

## §2 — The method, as the paper states it

### §2.1 The unit the model works on, and where boundaries may fall

*"Since harmonic changes may occur only when notes begin or end, we first create a sorted list of all
the note onsets and offsets in the input music, i.e. the list of partition points (Pardo and
Birmingham 2002) … A basic music event (Radicioni and Esposito 2010) is then defined as the set of
pitches sounding in the time interval between two consecutive partition points."* (p. 2)

So: **the atomic unit is the constant-sonority interval between two consecutive onsets-or-offsets**,
and **a chord boundary can fall only at a partition point.** The paper states the two alternatives it
is choosing between — quantisation to a fixed musical period such as half a measure (attributed to
Raphael and Stoddard 2003) against construction from consecutive onsets and offsets (attributed to
Radicioni and Esposito 2010) — and takes the second.

A *segment* is a run of consecutive events sharing one chord label: *"a segment sk = ⟨sk.f, sk.l⟩ is
identified by the positions sk.f and sk.l of its first and last events"* (p. 2).

**Table 1 (p. 2) is the worked input representation**, for measure 12 of Beethoven WoO68: segment s₁
labelled G7 over events e₁ (pitches G3, B3, D4, G5; length 1/8), e₂ (G3, B3, D4, F5; 1/8), e₃ (B4,
D5; 3/16), e₄ (B4, D5; 1/16); segment s₂ labelled C over e₅ (C4, C5, E5; 1/8), e₆ (G3, C5, E5; 1/8),
e₇ (E3, G4, C5, E5; 1/8), e₈ (C3, G4, C5, E5; 1/8). The caption states *"G7 stands for G:maj:add7,
and C stands for C:maj"*.

**One carried fact is stated in prose and not in the table, and it matters downstream:** *"Not shown
in this table is a boolean value for each pitch indicating whether or not it is held over from the
previous event. For instance, this value would be false for C5 and E5 appearing in event e₅, but
true for C5 and E5 in event e₆."* (p. 2) **The struck-versus-held distinction is therefore carried on
the input, per pitch per event**, and the figuration heuristics of Appendix B consume it.

### §2.2 The model

A semi-Markov CRF (attributed to Sarawagi and Cohen 2004) over segmentations and their labels:

- Equation 1: **P(s, y | x, w) = e^{wᵀF(s,y,x)} / Z(x)**, with **Z(x) = Σ_{s′,y′} e^{wᵀF(s′,y′,x)}**.
- Equation 2: **F(s, y, x) = Σ_{k=1}^{K} f(s_k, y_k, y_{k−1}, x)**, with *"label y₀ set to a constant
  'no chord' value"*.

**The model actually used is the WEAK form**, and the paper says so and cites it: *"Following Muis
and Lu (2016), for faster inference, we further restrict the local segment features to two types:
segment-label features **f**(s_k, y_k, x) that depend on the segment and its label, and label
transition features **g**(y_k, y_{k−1}, x) that depend on the labels of the current and previous
segments."* (p. 2–3) This gives Equations 3 to 5 and **two parameter vectors, w for segment-label
features and u for transition features**.

**The consequence of the weak form is stated by the paper itself, in Appendix B, and it is a real
structural cost:** *"because the weak semi-CRF features shown in Equation 4 do not have access to the
candidate label y_{k−1} of the previous segment s_{k−1}, we need a heuristic to determine whether an
anchor note is harmonic whenever the anchor note belongs to the previous segment."* (p. 15) The
heuristic is given in full at §2.5 below.

### §2.3 The two assumptions the factorization rests on

Named by the paper and attributed, rather than left implicit (p. 3):

- **Stationarity** — *"the segment-label feature distribution does not change with the position in
  the music"*.
- **The Markov assumption** — *"the label of a segment depends only on its boundaries and the labels
  of the adjacent segments"*.

The paper places both in a company it names: linear CRFs (Lafferty et al. 2001), semi-CRFs (Sarawagi
and Cohen 2004), HMMs (Rabiner 1989), structural SVMs (Tsochantaridis et al. 2004), and the
structured perceptron (Collins 2002) *"used in HMPerceptron"*. *"These assumptions lead to summing
the same feature over multiple substructures in the overall output score, which makes inference and
learning tractable using dynamic programming."*

### §2.4 Inference and learning

**Inference** (Equations 6 to 9, p. 3) is a semi-Markov analogue of Viterbi, attributed to Sarawagi
and Cohen 2004:

**V(i, y) = max_{y′, 1 ≤ l ≤ L} V(i − l, y′) + wᵀ**f**(⟨i − l + 1, i⟩, y, x) + uᵀ**g**(y, y′, x)**

with base cases **V(0, y) = 0** and **V(j, y) = −∞ if j < 0**. The paper states the cost as *"linear
in the length of the input"* and says the best labelled segmentation is recovered *"in linear time by
following the path traced by max_y V(|x|, y)"*.

**★ L IS A MAXIMUM SEGMENT LENGTH, AND ITS VALUE IS NOWHERE IN THE NINETEEN PAGES AS READ.** The
paper introduces it twice — *"The maximum is taken over all possible labeled segmentations of the
input, up to a maximum segment length"* and *"Let L be a maximum segment length"* (both p. 3) — and
then never gives it a value, in the model section, in the evaluation section, or in Appendix C. It is
listed at §7.2 among the quantities a later reader must not assume are answered.

**Learning** (Equations 10 and 11, p. 3): maximise the likelihood over a training set **T = {x_n,
s_n, y_n}_{n=1}^{N}** by minimising the negative log-likelihood plus an **L2 regularization term**,
**(λ/2)(‖w‖² + ‖u‖²)**. *"This is a convex optimization problem, which is solved with the L-BFGS
procedure in the StatNLP package used to implement our system. The partition function Z(x) and the
feature expectations that appear in the gradient of the objective function are computed efficiently
using a dynamic programming algorithm similar to the forward-backward procedure."* (p. 4) **λ's value
is not stated anywhere in the pages as read** (§7.2).

### §2.5 The figuration heuristics, which are rules and not learned

Appendix B (p. 15) defines four kinds of figuration note, each as a conjunction of conditions on
anchor notes. They are quoted in substance because §4's figuration-controlled features are defined
by subtraction from them.

- **Passing.** Two anchor notes n₁ and n₂ with: n₁'s offset at n's onset; n₂'s onset at n's offset;
  n₁ one scale step below n and n₂ one step above, or the reverse; n no longer than either anchor;
  **n's accent value strictly smaller than n₁'s**; at least one anchor in segment s; n non-harmonic
  with respect to chord y — *"i.e. n is not equivalent to the root, third, fifth, or added note of
  y"*; both anchors harmonic with respect to the segments they belong to.
- **Neighbor.** As passing, except that **n₁ and n₂ are both either one scale step below or one step
  above n**.
- **Suspension.** n is in the **first** event of segment s; an anchor m in the previous event (the
  last event of the previous segment) has the same pitch; n is **either tied with m or restruck**;
  n no longer than m; n non-harmonic with respect to y while m is harmonic with respect to the
  previous chord.
- **Anticipation.** n is in the **last** event of segment s; an anchor m in the next event (the first
  event of the next segment) has the same pitch; m is either tied with n or restruck; n no longer
  than m; n non-harmonic with respect to y while **m is harmonic relative to all other notes in its
  event**.

**The harmonicity heuristic forced by the weak factorization** (p. 15), quoted because it is the
paper's own patch for the model's blind spot: *"The heuristic simply looks at the other notes in the
event containing the anchor note: if the event contains 2 or more other notes, at least 2 of them
need to be consonant with the anchor, i.e. intervals of octaves, fifths, thirds, and their
inversions; if the event contains just one note other than the anchor note, it has to be consonant
with the anchor."*

**The paper marks its own limits here, and the sentence is worth carrying verbatim:** *"We emphasize
that the rules mentioned above for detecting figuration notes are only approximations. We recognize
that correctly identifying figuration notes can also depend on subtler stylistic and contextual cues,
thus allowing for exceptions to each of these rules."* (p. 15)

### §2.6 What an accent value is here

*"The accent value is determined based on the metrical position of a note or event, e.g. in a song
written in a 4/4 time signature, the first beat position would have a value of 1.0, the third beat
0.5, and the second and fourth beats 0.25. Any other eighth note position within a beat would have a
value of 0.125, any sixteenth note position strictly within the beat would have a value of 0.0625,
and so on."* (p. 16) It is computed by **the `beatStrength()` function in Music21**, cited in a
footnote to the Music21 site (p. 15), and **derived from the notated meter** rather than induced
(p. 6).

---

## §3 — Coupling facts

The commission's §4 makes these mandatory: what the method assumes about its upstream, what it hands
downstream, and its own stated scope. Each is given here **from the paper alone**.

### §3.1 What the method ASSUMES about its upstream

- **A symbolic input with onsets, offsets, pitches and metrical position.** *"In this work, we
  consider the music to be in symbolic form, i.e. as a collection of notes specified in terms of
  onset, offset, pitch, and metrical position. Symbolic representations can be extracted from formats
  such as MIDI, kern, or MusicXML."* (p. 1) *(★ The opening words "In this work," were restored at the
  user-ordered check against page 1 re-opened; the quotation had begun mid-sentence with no ellipsis.
  No word inside it changed.)*
- **A notated meter it trusts.** The accent values come from Music21's `beatStrength()` over the
  notated meter (§2.6). The paper is explicit that this is a difference from the systems it compares
  against, which use meter induced by Melisma, and it names the risk to itself: *"The more accurate
  notated meter could favor the semi-CRF system"* (p. 6).
- **Spelled pitch, at least for the scale-step tests.** The passing and neighbor heuristics are
  defined on *"one scale step"* relations (p. 15) and the augmented-sixth definitions on sharpened
  scale degrees (p. 14), neither of which is available from pitch class alone.
- **NO key.** This is the load-bearing assumption and the paper states it as a design choice, with
  its ground: *"Because the labels do not encode for function, the model does not require knowing the
  key in which the input was written."* (p. 4)
- **NO voice or stream assignment**, and none is used anywhere in Appendix C's features.
- **Enharmonically normalised chord LABELS**, supplied by the dataset preparation and not by the
  model (§5.1 below). The paper is careful that this touches the labels only: *"The actual chord
  notes used in the music are left unchanged."* (p. 5)

### §3.2 What it HANDS downstream

- **A single labelled segmentation of the whole input** — jointly the segment boundaries and one
  chord label per segment. *"semi-CRF always predicts one label per segment"* (p. 10). **No ranked
  alternatives, no per-segment confidence and no abstention are described anywhere in the pages as
  read.**
- **A label of the form root × mode × added note**, where mode is one of major, minor, diminished
  (plus the augmented-sixth, suspended and power modes where those label sets are enabled), and added
  note is one of none, fourth, sixth, seventh (p. 4).
- **Explicitly NOT handed:** inversion, function, and the type of a seventh. The paper says each is
  recoverable afterwards rather than absent by accident. On inversion: *"the chord labels used in our
  system do not distinguish among inversions of the same chord. However, once the basic triad is
  determined by the system, finding its inversion can be done in a straightforward post-processing
  step, as a function of the bass note in the chord."* (p. 14) On the seventh: *"there is only one
  generic type of added seventh note, irrespective of whether the interval is a major, minor, or
  diminished seventh, which means that a C major seventh chord and a C dominant seventh chord are
  mapped to the same label"*, with the recovery procedure given in full — determine whether the chord
  contains a non-figuration note *"that is 11, 10, or 9 half steps from the root, respectively,
  inverted or not, modulo 12"*, then read off the seventh-chord type from the mode (p. 4).
- **A statement that the analysis is incomplete without what it does not hand:** *"we recognize that
  harmonic analysis is not complete without functional analysis."* (p. 4)

### §3.3 Its own STATED scope and limits

Each of these is the paper's own statement about itself, not this read's inference.

- **(a) The key is excluded, and the paper states what that costs, with a mechanism.** *"In
  particular, the chord transition features that we define in Appendix C.4 depend on the absolute
  distance in half steps between the roots of the chords. However, a V-I transition has a different
  distribution than a I-IV transition, even though the root distance is the same. Chord transition
  distributions also differ between minor and major keys. As such, using key context could further
  improve chord recognition."* (p. 4)
- **(b) Why the key was excluded is given as a mixed ground, and the first limb is about the data
  rather than about the method:** *"The decision to not use the key context was partly motivated by
  the fact that 3 of the 4 datasets we used for experimental evaluation do not have functional
  annotations (see Section 5)."* The second limb is about the difficulty of key annotation itself —
  *"Key changes
  occur gradually, thus making it difficult to determine the exact location where one key ends and
  another begins (Papadopoulos and Peeters 2009). This makes locating modulations and tonicizations
  difficult and also hard to evaluate (Gómez 2006)."* (p. 4)

  *(★ TWO QUOTATION DEFECTS OF THIS READ'S OWN, CORRECTED HERE AT THE USER-ORDERED CHECK AGAINST
  PAGE 4. FORMER WORDING, PRESERVED (#12): "3 of the 4 datasets used for experimental evaluation do
  not have functional annotations." **The word "we" was dropped from inside the quotation**, and the
  parenthetical "(see Section 5)" was cut at the tail **with no ellipsis**. Neither moves a value and
  neither changes the sense, but both are the class this file reports against the first extract at
  §9.3, and they were missed by this read's read-back, its sweep AND the cross-check. **The first
  extract has this sentence right at both points**, which is how they were found. And in (a) above,
  the opening words "In particular," were restored at the same check.)*
- **(c) Performance is stated as conditional on training data.** The abstract's own formulation:
  *"performs substantially better than previous approaches when trained on a sufficient number of
  labeled examples and remains competitive when the amount of training data is limited."* The KP
  Corpus is the paper's own worked case of the second half (§5, §6 below).
- **(d) Manual feature engineering is named as a limitation of the approach, by the authors.**
  *"Manually engineering features for chord recognition is a cognitively demanding and time consuming
  process that requires music theoretical knowledge and that is not guaranteed to lead to optimal
  performance, especially when complex features are required."* (p. 12)
- **(e) The figuration rules are approximations** (§2.5, quoted there).
- **(f) One evaluation is declared not fully comparable, by the authors, with the reason.** Against
  the HarmAn algorithm: *"it is important to note that these results are still not fully comparable:
  sometimes HarmAn predicts multiple labels for a single segment, and when the correct label is among
  these, Pardo and Birmingham divide by the number of labels the system predicts and consider this
  fractional value to be correct. In contrast, semi-CRF always predicts one label per segment."*
  (p. 9–10)
- **(g) Chord ambiguity is acknowledged as unresolved by the labels alone**, with the German sixth /
  F dominant seventh case and the {D, F, A, C} case as the paper's own examples, and with the claim
  that the model addresses it *through* bass features and chord bigrams rather than by resolving it
  in the label set (p. 15).

---

## §4 — Claims, labeled

**FACT** = stated or measured in this paper and readable at its own pages. **THEORY** = established
published theory the paper invokes and attributes. **CONJECTURE** = the paper's own expectation,
explanation or recommendation, not measured in it. The labels are this read's; the sentences are the
paper's.

**F-1 [FACT]** The model performs segmentation and labelling **jointly**, under one semi-Markov CRF,
rather than labelling events and joining equal labels afterwards (p. 2, Equations 1 to 5).

**F-2 [FACT]** The model used is the **weak** semi-CRF of Muis and Lu 2016: segment-label features
cannot see the previous segment's label (p. 2–3), and the paper's own figuration heuristic needs a
patch because of it (p. 15).

**F-3 [FACT]** The label set encodes **root, mode and added note, and not function, not inversion,
and not the type of the seventh** (p. 4). 144 triad labels; 36 augmented-sixth labels; 48 suspended
and power labels (p. 4).

**F-4 [FACT]** The features **do not test for the chord root**, and the paper gives the consequence:
*"the number of parameters in our model is largely independent of the number of labels … which also
enables the system to recognize chords that were not seen during training."* (p. 4)

**F-5 [FACT]** Five kinds of feature are used — segment purity, chord coverage, bass, chord bigram,
metrical accent — defined in full in Appendix C (p. 4, p. 15–19).

**F-6 [FACT]** Every real-valued feature is **discretized into K+2 Boolean features** over a bin set,
with the default **B = [0, 0.1, …, 0.9, 1.0]** and two extra Booleans for the boundary cases f = 0
and f = 1 (p. 16).

**F-7 [FACT]** Each of segment purity, chord coverage and bass has a **figuration-controlled
variant** that substitutes the non-figuration notes for the notes of the segment (pp. 16, 18).

**F-8 [FACT]** The chord bigram template abstracts away the absolute roots and keeps **mode, added
note, and the interval in semitones between the two roots**, generating **4,332 distinct features**,
pruned to *"only the (mode.added)–(mode.added)′–interval combinations that appear in the manually
annotated chord bigrams from the training data"* (p. 19).

**F-9 [FACT]** Only features **whose counts in the training data were at least 5** were used, and the
counts were taken *"using only the true segment boundaries and their labels"* (p. 7).

**F-10 [FACT]** On BaCh the semi-CRF beats both HMPerceptron versions on every reported measure, and
its **sample standard deviations are about one order of magnitude smaller** (p. 7, Table 3).

**F-11 [FACT]** On the KP Corpus, **Melisma — a rule-based system with hand-set weights — beats both
machine-learning systems at root level** (p. 9, **Table 11**, which is the one carrying all three
systems; Table 9 shows the same against the semi-CRF alone, HMPerceptron not being evaluated there).

**F-12 [FACT]** Removing the accent-based features from the semi-CRF costs it **5.9 points of
event-level accuracy and 6.4 points of segment-level F-measure** on one BaCh fold set (p. 7,
Table 5; the subtraction is this read's, the two rows are the paper's).

**F-13 [FACT]** Augmented-sixth features improve the KP Corpus result on all four reported measures,
and suspended-and-power features improve the Rock result on all four (Tables 8 and 12).

**T-1 [THEORY]** Semi-Markov CRFs and their Viterbi-analogue inference, attributed to Sarawagi and
Cohen 2004; linear-chain CRFs to Lafferty et al. 2001; factor graphs to Kschischang et al. 2001; the
weak restriction to Muis and Lu 2016.

**T-2 [THEORY]** The event construction from partition points is attributed to Pardo and Birmingham
2002 and Radicioni and Esposito 2010; the middle-ground label set to Radicioni and Esposito 2010; the
chord-bigram abstraction likewise (p. 19).

**T-3 [THEORY]** The music theory the appendices rest on is attributed — chords and augmented sixths
to Aldwell et al. 2011, suspended chords to Taylor 1989, power chords to Denyer 1992, and the claim
that chord changes attract accent to Aldwell et al. 2011 (pp. 13–19).

**C-1 [CONJECTURE]** *"using key context could further improve chord recognition"* (p. 4) — argued
from the transition-distribution mechanism, **not measured anywhere in the paper**.

**C-2 [CONJECTURE]** The explanation offered for the TAVERN gap between event accuracy and segment
F-measure: many segments whose first event does not contain the root, where an event-based system
mislabels the first event and *"a single wrongly labeled event invalidates the entire segment"*
(pp. 8–9). The mechanism is exhibited on two figures, not counted over the corpus.

**C-3 [CONJECTURE]** The explanation offered for the KP Corpus result — smaller training set, and
*"the textbook excerpts are more diverse, as they are taken from 11 composers and are meant to
illustrate a wide variety of music theory concepts, leading to mismatch between the training and test
distributions"* (p. 10). Not measured.

**C-4 [CONJECTURE]** *"Semi-CRF most likely predicts the correct label because of its ability to
heuristically detect figuration"* (p. 11) — the 'Let It Be' case, stated with its own hedge.

**C-5 [CONJECTURE]** The whole of §8, Future Work: segmental RNNs after Kong et al. 2016, and jointly
solving several music analysis tasks. Plans, not results.

**★ ONE CLAIM THIS READ SEPARATES OUT, BECAUSE IT IS A PRIORITY CLAIM AND NOT A MEASUREMENT.** *"The
semi-CRF approach described in this paper is the first to take advantage of both learning the weights
and performing a joint segmentation and labeling of the input."* (p. 11) It is stated over the four
systems the related-work section compares — Melisma, HarmAn, HMPerceptron and this one, sorted by the
two questions the paper poses there — and **the paper offers no survey evidence for the wider claim**.
This read did not test it and takes no position on it; it is recorded as **[CONJECTURE]** on the
ground that a first-ness claim needs a derivation the paper does not give, not on the ground that it
is doubted.

---

## §5 — Measured results, with corpus, metric and value as the paper states them

### §5.1 The four corpora, and what each one's ground truth is

**BaCh.** *"the Bach Choral Harmony Dataset, a corpus of 60 four-part Bach chorales that contains
**5,664 events and 3,090 segments** in total (Radicioni and Esposito 2010)."* Annotated **by a human
expert** — singular — with the triad label set. *"Of the 144 possible labels, **102 appear in the
dataset and of these only 68 appear 5 times or more**."* Enharmonic pairs in the manual annotation are
normalised to canonical roots chosen for the fewest sharps or flats: **{C, Db, D, Eb, E, F, Gb, G,
Ab, A, Bb, B} for the major mode** and **{C, C♯, D, D♯, E, F, F♯, G, G♯, A, Bb, B} for minor and
diminished**. *"After performing enharmonic normalization on the chords in the dataset, **90 labels
remain**."* (p. 5)

**TAVERN.** *"a corpus of 27 complete sets of themes and variations for piano, composed by Mozart and
Beethoven. It consists of **63,876 events and 12,802 segments** overall (Devaney et al. 2015)."*
Composition: **17 works by Beethoven (181 variations) and 10 by Mozart (100 variations)**, divided
into **1,060 phrases, 939 in major and 121 in minor**. Chords annotated with Roman numerals in the
Humdrum `**harm` representation. **★ The two-annotator design is described as the intention and the
single-annotator reality as the fact:** *"When finished, each phrase will have annotations from two
different experts, with a third expert adjudicating cases of disagreement between the two. … However,
many pieces do not currently have the second annotation or the adjudicated version. Consequently, we
only used the first annotation for each of the 27 sets."* The Roman numerals were translated to the
key-independent label set by a script the authors wrote, and because *"the TAVERN annotation does not
mark added fourth notes"* only sixths and sevenths were generated, giving **108 possible labels of
which 69 appear** (p. 5).

**KP Corpus.** *"the Kostka-Payne corpus … a dataset of 46 excerpts compiled by Bryan Pardo from
Kostka and Payne's music theory textbook. It contains **3,888 events and 911 segments** (Kostka and
Payne 1984)."* Seventh-chord variants are mapped to the generic added seventh and ninths dropped;
with augmented-sixth labels added the set is **12 roots × 3 modes × 2 added notes + 12 bass notes × 3
aug6 modes = 108 possible labels, of which 76 appear**. Unlabelled opening sections were omitted from
evaluation **and from the event and segment counts**. **★ The source data required repair, and the
repair came from outside:** *"Bryan Pardo's original MIDI files for the KP Corpus also contain several
missing chords, as well as chord labels that are shifted from their true onsets. We used chord and
beat list files sent to us by David Temperley to correct these mistakes."* (p. 5)

**Rock.** *"a corpus of **59 pop and rock songs** that we compiled from Hal Leonard's The Best Rock
Songs Ever (Easy Piano) songbook. It is **25,621 events and 4,221 segments** in length."* Label set
extended with suspended second, suspended fourth, dominant seventh suspended fourth and power chords:
**12 roots × 3 triad modes × 4 added notes + 12 roots × 4 sus and pow modes = 192 possible labels,
with only 48 appearing**. **★ Its provenance is optical music recognition plus hand correction, and
the paper says so plainly:** *"we converted printed sheet music to MusicXML files using the optical
music recognition (OMR) software PhotoScore. We noticed in the process of making that dataset that
some of the originally annotated labels were incorrect. For instance, some segments with added note
labels were missing the added note, while other segments were missing the root or were labeled with
an incorrect mode. We automatically detected these cases and corrected each label by hand, considering
context and genre-specific theory."* Two of the original 61 songs were omitted — *"'Takin' Care of
Business' … because of its atonality and … 'I Love Rock 'N Roll' … because of a high percentage of
mistakes in the original labels."* Songs containing the no-chord label were split around it and
*"subsections less than three measures long"* discarded (pp. 5–6).

### §5.2 The two measures, and the strictness of the segment one

- **Event-level accuracy (Acc_E)**: *"the percentage of events for which the system predicts the
  correct label out of the total number of events in the dataset."*
- **Segment-level precision (P_S)**: correct predicted segments over all predicted segments.
  **Recall (R_S)**: correct predicted segments over all annotated segments. **F-measure (F_S)** =
  2·P_S·R_S / (P_S + R_S).
- **★ The criterion, quoted because everything about the gap between the two measures follows from
  it:** *"Note that a predicted segment is considered correct if and only if both its boundaries and
  its label match those of a true segment."* (p. 6)

### §5.3 The protocols, which differ per corpus

- **BaCh**: 10-fold cross-validation, **repeated 10 times with re-shuffled folds**, results pooled
  within each experiment and then averaged over the 10 experiments, with the **sample standard
  deviation over the same 10 values**. The repetition is there for a stated reason: *"we noticed that
  the performance of HMPerceptron could vary significantly between two different random partitions of
  the data into folds."* (p. 6)
- **TAVERN**: a **fixed** training-test split — testing on Beethoven B063, B064, B065, B066, B068,
  B069 and Mozart K025, K179, K265, K353; training on the remaining 11 Beethoven and 6 Mozart sets
  (p. 8).
- **KP Corpus**: **11 folds** over 46 songs (nine of 4 songs, two of 5) for the augmented-sixth
  comparison; **leave-one-out** over the 36 songs without augmented sixths, *"Because of the reduced
  number of songs available for training"* (p. 9).
- **Rock**: **10 folds** over 59 songs (nine of 6, one of 5); for the 51-song comparison, **nine folds
  of 5 test songs and 46 training songs, plus one of 6 and 45** (p. 10).
- **Significance**: every significance claim this read met is a **one-tailed Welch's t-test** — at
  averaged p-values of **0.001 and 0.002** on BaCh's two full-chord comparisons and at **0.01** on the
  BaCh root, TAVERN and Rock comparisons (pp. 7, 8, 10). **No significance test is reported for any KP
  Corpus comparison**, and none is reported for the accent ablation of Table 5.

*(★ CORRECTED AT THE USER-ORDERED CHECK. TWO FORMER WORDINGS, PRESERVED (#12). FIRST: "ten folds of 5
test songs and 46 training songs plus one of 6 and 45", **which totals eleven folds where the paper
states ten** — nine of five test songs and one of six, summing to the 51 songs. SECOND: "a one-tailed
Welch's t-test **throughout**, at averaged p-values of 0.001 and 0.002 on BaCh's two headline
comparisons and at **0.01 elsewhere**". **"Throughout" and "elsewhere" are absolutes this read did not
derive, and they are wrong**: the KP Corpus carries no significance claim at all, so "elsewhere"
asserted a test the paper never reports.)*

### §5.4 Table 2, the summary — transcribed, with one caveat that belongs beside it

Table 2 (p. 7), *"Dataset statistics and summary of results (event-level accuracy Acc_E and
segment-level F-measure F_S)"*, all values per cent:

| Dataset | Events | Seg.'s | Labels | semi-CRF Acc_E / F_S | HMPerceptron Acc_E / F_S | ROOT semi-CRF Acc_E / F_S | ROOT HMPerceptron Acc_E / F_S | ROOT Melisma Acc_E / F_S |
|---|---|---|---|---|---|---|---|---|
| BaCh | 5,664 | 3,090 | 90 | **83.2 / 77.5** | 77.2 / 69.9 | **88.9 / 84.2** | 84.8 / 77.0 | 84.3 / 74.7 |
| TAVERN | 63,876 | 12,802 | 69 | **78.0 / 64.0** | 57.0 / 22.5 | **86.0 / 71.4** | 69.2 / 33.2 | 76.7 / 41.5 |
| KPCorpus | 3,888 | 911 | 76 | **73.0 / 53.0** | 72.9 / 45.4 | 79.3 / 59.0 | 79.0 / 51.9 | **81.9 / 62.2** |
| Rock | 25,621 | 4,221 | 48 | **70.1 / 55.9** | 61.3 / 34.6 | **86.1 / 65.1** | 80.7 / 42.9 | 77.9 / 36.3 |

**★ THE CAVEAT, ESTABLISHED BY COMPARING THIS TABLE AGAINST THE TABLES IT SUMMARISES, IS AT §7.1 (2):
on the KPCorpus and Rock rows the statistics columns and the results columns are over DIFFERENT SONG
SETS.**

### §5.5 The per-corpus tables, transcribed

**BaCh, full chord (Table 3, p. 7)** — standard deviations as printed beneath each value:

| System | Acc_E | P_S | R_S | F_S |
|---|---|---|---|---|
| semi-CRF | **83.2** (0.2) | **79.4** (0.2) | **75.8** (0.2) | **77.5** (0.2) |
| HMPerceptron₁ | 77.2 (2.1) | 71.2 (2.0) | 68.8 (2.2) | 69.9 (1.8) |
| HMPerceptron₂ | 77.0 (2.1) | 71.0 (2.0) | 68.5 (2.3) | 69.7 (1.8) |

HMPerceptron₁ normalises enharmonically on training and test data; HMPerceptron₂ is *"the original
system from Radicioni and Esposito (2010) that does enharmonic normalization only on test data"*
(p. 7).

**BaCh, root only (Table 4, p. 7):** semi-CRF **88.9 / 85.4 / 83.0 / 84.2**; HMPerceptron 84.8 /
78.0 / 76.2 / 77.0; Melisma 84.3 / 73.2 / 76.3 / 74.7.

**BaCh, metrical accent ablation (Table 5, p. 7),** on *"a random fold set"* rather than the ten:
with accent **83.6 / 79.6 / 75.9 / 77.6**; without accent **77.7 / 74.8 / 68.0 / 71.2**.

**TAVERN, full chord (Table 6, p. 8):** semi-CRF **78.0 / 67.3 / 60.9 / 64.0**; HMPerceptron 57.0 /
24.5 / 20.8 / 22.5.

**TAVERN, root only (Table 7, p. 8):** semi-CRF **86.0 / 74.6 / 68.4 / 71.4**; HMPerceptron 69.2 /
38.2 / 29.4 / 33.2; Melisma 76.7 / 42.3 / 40.7 / 41.5.

**KP Corpus, 46 songs, full chord (Table 8, p. 9):** semi-CRF₁ (no augmented-sixth features) 72.0 /
59.0 / 49.2 / 53.5; semi-CRF₂ (with them) **73.4 / 59.6 / 50.1 / 54.3**.

**KP Corpus, 46 songs, root only (Table 9, p. 9):** semi-CRF 80.7 / **66.3** / 56.2 / 60.8; Melisma
**80.9** / 60.6 / **63.3** / **61.9**. Events belonging to true augmented-sixth segments are ignored
for both systems here, *"as augmented 6th chords technically do not contain a root note"*.

**KP Corpus, 36 songs, full chord (Table 10, p. 9):** semi-CRF **73.0 / 55.6 / 50.7 / 53.0**;
HMPerceptron 72.9 / 48.2 / 43.6 / 45.4.

**KP Corpus, 36 songs, root only (Table 11, p. 9):** semi-CRF 79.3 / **61.8** / 56.4 / 59.0;
HMPerceptron 79.0 / 54.7 / 49.9 / 51.9; Melisma **81.9** / 60.7 / **63.7** / **62.2**.

**Rock, 59 songs, full chord (Table 12, p. 10):** semi-CRF₁ (no suspended or power features) 66.0 /
49.8 / 47.3 / 48.5; semi-CRF₃ (with them) **69.4 / 62.0 / 54.9 / 58.3**.

**Rock, 59 songs, root only (Table 13, p. 10):** semi-CRF **85.8 / 70.9 / 63.2 / 66.8**; Melisma
77.4 / 29.5 / 44.0 / 35.3.

**Rock, 51 songs, full chord (Table 14, p. 10):** semi-CRF **70.1 / 58.8 / 53.2 / 55.9**;
HMPerceptron 61.3 / 41.0 / 29.9 / 34.6.

**Rock, 51 songs, root only (Table 15, p. 10):** semi-CRF **86.1 / 68.6 / 61.9 / 65.1**;
HMPerceptron 80.7 / 51.3 / 36.9 / 42.9; Melisma 77.9 / 30.6 / 45.8 / 36.3.

**One comparison reported in prose and in no table:** against HarmAn (Pardo and Birmingham 2002),
which *"achieves a 75.8% event-level accuracy on the KP Corpus"*; under the modified evaluation
described at §3.3(f), *"semi-CRF obtains an event-level accuracy of 75.3%"* (pp. 9–10).

**One ablation reported in prose and in no table:** HMPerceptron on a random BaCh fold set with
Melisma's metrical accent against Music21's — *"with Melisma accent the event accuracy was 79.8% for
an F-measure of 70.2%, whereas with Music21 accent the event accuracy was 79.8% for an F-measure of
70.3%"* (p. 8).

---

## §6 — Arithmetic this read performed on the paper's own printed values

Every check below is over values printed in the paper. Where a check closes, it is evidence the two
printed things agree; where it does not, the failure is reported at §7.1.

**§6.1 Every label-set count this read met closes, including the one the paper states without its
product.**
- Triads: 12 roots × 3 modes × 4 added notes = **144** ✓ (p. 4).
- Augmented sixths: 12 lowest notes × 3 types = **36** ✓; suspended and power: 12 roots × 4 types =
  **48** ✓ (p. 4).
- KP Corpus: 12 × 3 × 2 + 12 × 3 = 72 + 36 = **108** ✓ (p. 5).
- Rock: 12 × 3 × 4 + 12 × 4 = 144 + 48 = **192** ✓ (p. 6).
- Chord bigram template: (3 × 4 + 3 + 3 + 1)² × 12 = 19² × 12 = 361 × 12 = **4,332** ✓ (p. 19).
- **TAVERN, where the paper prints the result and not the product.** It says the translation script
  generated added chords *"containing sixths and sevenths"* only, *"This results in a set of 108
  possible labels"* (p. 5). With the added note restricted to none, sixth and seventh, 12 roots × 3
  modes × 3 added notes = **108** ✓. **The reconstruction of the product is this read's**; what the
  paper prints is the total.

**§6.2 The TAVERN composition closes.** 939 major + 121 minor = **1,060 phrases** ✓; 17 Beethoven +
10 Mozart = **27 sets** ✓ (p. 5).

**§6.3 Both relative-error-reduction values close, and the paper shows its own working for one.**
Footnote 1 (p. 7) prints *"27% = (83.2 − 77.0)/(100 − 77.0)"*, which is 6.2 / 23.0 = 0.2696 → **27.0 %**
✓. The root-level claim of the same size is not shown but closes the same way: (88.9 − 84.8) /
(100 − 84.8) = 4.1 / 15.2 = 0.2697 → **27.0 %** ✓.

**§6.4 Every stated improvement is a difference of two printed values, and all of them close.**
BaCh full chord 6.2 (83.2 − 77.0) ✓, 7.8 (77.5 − 69.7) ✓, 7.6 (77.5 − 69.9) ✓; BaCh root 4.1, 4.6,
7.2, 9.5 ✓; TAVERN 21.0, 41.5, 16.8, 9.3, 38.2, 29.9 ✓; KP 36 songs 7.6 (53.0 − 45.4) ✓ and the
*"marginal"* 0.1 ✓; KP 46 songs root 0.2 and 1.1 ✓; Rock 59 root 8.4 and 31.5 ✓; Rock 51 full 8.8 and
21.3 ✓; Rock 51 root 5.4, 8.2, 22.2, 28.8 ✓. **Every improvement named above is the difference of
the two values printed beside it, and the members are named here rather than totalled.**

*(★ CORRECTED AT THE SWEEP, BEFORE THIS FILE LANDED. FORMER WORDING, PRESERVED (#12): "**Sixteen
stated improvements, every one of them the difference of the two values printed beside it.**"
**Sixteen is a count this read never derived, and it is wrong**: counted at the sentence it closed,
**twenty-five values are listed, of which twenty-three are improvements the paper states** and two —
the 0.1 on the KP Corpus and the 0.2 at its root level — are this read's own differences behind the
paper's word *"marginal"*. **The two relative error reductions of §6.3 are in neither count**, being
recorded there. **This is the first of the user's named degradation tells — a count put on this side's
own reading without deriving it — and it is recorded at §8.3 rather than quietly replaced.**)*

**§6.5 The F-measure definition reproduces the printed F_S at every cell this read tested, within the
rounding of the printed precision and recall.** Worked at four: BaCh full chord semi-CRF,
2 × 79.4 × 75.8 / 155.2 = 77.56 against a printed 77.5; BaCh root, 2 × 85.4 × 83.0 / 168.4 = 84.18
against 84.2; TAVERN full chord, 2 × 67.3 × 60.9 / 128.2 = 63.94 against 64.0; TAVERN root,
2 × 74.6 × 68.4 / 143.0 = 71.37 against 71.4. **None of the four is out by more than the rounding of
its own inputs**, so this is agreement and not a discrepancy. **The other F_S cells were not
recomputed**, and nothing is claimed about them.

**§6.6 The accent ablation's two gaps, derived here and marked as derived.** Table 5 gives no
difference column. With accent minus without: event-level **5.9** (83.6 − 77.7) and segment-level
F-measure **6.4** (77.6 − 71.2). The paper's own word for it is *"a substantial decrease"*; the two
values are this read's subtraction.

**§6.7 Two counts over the BaCh label set, derived here and marked as derived.** The paper prints
that **102 of the 144 possible labels appear in the dataset**, that **68 of those appear five times
or more**, and that **90 labels remain after enharmonic normalisation**. Two differences follow and
neither is printed: the normalisation collapses **12** of the appearing labels, and **34** of the
appearing labels occur fewer than five times. **Both subtractions are this read's.**

*A distinction this read keeps separate, because the same number 5 appears in two unrelated places:*
the *"appear 5 times or more"* above is a count of **label occurrences in the corpus** (p. 5), while
the *"features whose counts were at least 5"* of F-9 is a threshold on **feature counts in the
training data** (p. 7). **The paper draws no connection between them and neither does this read.**

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Inconsistencies and defects inside the paper

**(1) The held object is a preprint whose citation header is unfilled, and the paper names itself in
three different forms.** Both are established and stated at §1 and are not restated here.

**(2) ★ IN TABLE 2, TWO OF THE FOUR ROWS PAIR WHOLE-CORPUS STATISTICS WITH REDUCED-SUBSET RESULTS,
AND THE CAPTION SAYS NOTHING ABOUT IT.** This is the one finding of this read that could mislead a
later reader into carrying a wrong number, so it is established cell by cell.

- **The KPCorpus row's statistics are the 46-excerpt corpus's**: 3,888 events and 911 segments are
  **the paper's §5** values for the corpus of 46 excerpts, and 76 labels is **the paper's §5.3**
  count, *"of these, 76 appear in the dataset"*.
- **The KPCorpus row's results are the 36-song subset's, every one of them.** Full chord 73.0 / 53.0
  and 72.9 / 45.4 are Table 10 exactly; root 79.3 / 59.0, 79.0 / 51.9 and 81.9 / 62.2 are Table 11
  exactly. **The 46-song values printed in Tables 8 and 9 — 73.4 / 54.3 for semi-CRF and 80.7 / 60.8
  against Melisma's 80.9 / 61.9 at root — appear nowhere in Table 2.**
- **The Rock row's statistics are the 59-song dataset's**: 25,621 events, 4,221 segments and 48
  labels are **the paper's §5 and §5.4** values for the 59 songs.

*(★ On the section numbers in these two bullets: at the user-ordered check they were qualified as the
PAPER's, because this file has sections of the same numbers and a reader would otherwise look for them
here. No value or verdict changed.)*
- **The Rock row's results are the 51-song subset's, every one of them.** Full chord 70.1 / 55.9 and
  61.3 / 34.6 are Table 14 exactly; root 86.1 / 65.1, 80.7 / 42.9 and 77.9 / 36.3 are Table 15
  exactly. **The 59-song values printed in Tables 12 and 13 — 69.4 / 58.3 and 85.8 / 66.8 — appear
  nowhere in Table 2.**
- **The BaCh and TAVERN rows carry no such split**: their statistics and their results are over the
  same material.

**Why it matters rather than being a presentational slip.** The reduced sets are not arbitrary
subsets: the 36 KP songs are *"the songs that do not contain augmented 6th chords"* and the 51 Rock
songs are those *"that do not contain suspended or power chords"* (pp. 9, 10), so each was chosen to
make a comparison against HMPerceptron possible. **A reader lifting Table 2 gets the comparison-set
result attached to the whole corpus's size**, and on the KP Corpus that is the row where the paper's
own system does WORSE than the rule-based Melisma. *The direction of the difference is small on the
values themselves* — 73.0 against 73.4 and 70.1 against 69.4 — *and this read makes no claim that the
choice was made to flatter anything;* what it establishes is that the row mixes two populations
silently.

**(3) The predicted label of Figure 6 is spelled two ways, one of them off the paper's own
convention.** The body text says HMPerceptron *"incorrectly produces the label G:maj:add6"* (p. 11)
while the caption and the figure itself read **G:maj6**. The paper's stated label convention is
root-mode-added, as in its own *"C:maj:add7"* (p. 4), which the caption's form does not follow. **No
value moves on it.**

**(4) A third name for the compared system appears in two captions, and this read met it defined
nowhere.** Figures 4 and 5 (p. 8) both read **"HMPtron"**; every other occurrence this read met — in
the body text, in the table rows and in the related-work section — reads **"HMPerceptron"**,
including the caption of Figure 6, which is the third figure naming that system.

**(5) The enumeration at the head of §6 does not cover what §6 does.** It names three systems — the
semi-CRF, HMPerceptron and Melisma — and §6.3 then compares against a fourth, HarmAn, at p. 9–10.

**(6) ★ THE STATED RULE FOR CHOOSING CANONICAL ROOTS LEAVES ONE DEGREE UNDETERMINED IN EACH MODE, AND
THE TWO ARE RESOLVED IN OPPOSITE DIRECTIONS.** The rule is *"we selected the one with the fewest
sharps or flats in the corresponding key signature"* (p. 5), and by its own clause it is exercised
only *"When two enharmonic chords are available for a given scale degree"* — **the five degrees whose
canonical root is a sharp or a flat.** Applied to the printed sets, **it decides four of those five in
each mode and leaves one**, because there the two spellings carry the same number of accidentals:

- **Major: G♭ against F♯**, six flats against six sharps. The printed major set takes **G♭**.
- **Minor: D♯ against E♭**, six sharps against six flats. The printed minor and diminished set takes
  **D♯**.

**So the two ties are broken toward the flat side in one mode and the sharp side in the other, and
this read met no tie-break stated anywhere.** A later reader reconstructing the normalisation from
the stated rule alone can determine twenty-two of the twenty-four entries and **not those two**.
**No result moves on it** — the sets themselves are printed and this read transcribed them as
printed, at §5.1. *(The accidental counts behind the two ties are this read's, taken at the standard
key signatures: G♭ major six flats against F♯ major six sharps; D♯ minor six sharps against E♭ minor
six flats. The minor tie is computed on the minor key signatures, which is the reading the paper's
own clause "for the minor and diminished modes" supports. The other four in each mode are decided by
a margin: in major, D♭ 5 flats against C♯ 7 sharps, E♭ 3 against D♯ 9, A♭ 4 against G♯ 8, B♭ 2 against
A♯ 10; in minor, C♯ 4 sharps against D♭ 8 flats, F♯ 3 against G♭ 9, G♯ 5 against A♭ 7, B♭ 5 flats
against A♯ 7 sharps.)*

*(★ CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING, PRESERVED (#12): the heading read "**DOES
NOT DETERMINE TWO OF THE TWELVE**" and the body "**it decides ten of the twelve scale degrees in each
mode and leaves two undecided**". **Both are wrong and they contradict this same finding's own closing
sentence**, which says twenty-two of twenty-four are determined: ten decided plus two undecided per
mode would leave four undetermined across the two sets, not two. **The rule is exercised at five
degrees per mode, not twelve** — its own clause says so — **and it leaves exactly one of those five
undecided in each mode.** The two named ties, the printed sets and the conclusion are unchanged; what
was wrong was the arithmetic describing the rule's reach.)*

**(7) One comparative sentence does not name the level it holds at.** §6.3.1 opens *"Both machine
learning systems struggled on the KP corpus, with Melisma performing better on both event-level
accuracy and segment-level F-measure."* **Melisma is evaluated on the KP Corpus at root level only**
— Tables 9 and 11 — and **no full-chord Melisma value appears for the KP Corpus, or for any corpus,
anywhere in the nineteen pages as read.** The sentence is true of the root-level tables; read without
that qualification it claims something the paper never measured.

**(8) Printed language defects, named rather than counted.** Figure 5's caption carries *"(bottom)"*
twice in one sentence. The type slug at the head of page 1 reads **ARTICLE TYPE**, an unfilled
template placeholder. **Neither moves a value.**

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered

Each of these is a quantity the paper's own method requires or its own claims would rest on, and
**none of them is printed anywhere in the nineteen pages as read**.

- **L, the maximum segment length**, on which the inference recursion of Equation 9 depends. Named
  twice on p. 3, valued nowhere.
- **λ, the L2 regularization coefficient** of Equation 11.
- **The number of features actually used**, on any corpus, before or after the count-5 pruning. **The
  only feature count this read met** is the bigram template's **4,332 before pruning**.
- **Any procedure for choosing λ, the bin set B, the count threshold, or L** — and **no development
  or validation split is described in the pages as read**. The test folds are held out; the
  settings' provenance is not stated.
- **Training or inference time**, for any system, although speed is the stated ground for adopting
  the weak model (p. 2–3).
- **The event and segment counts of the reduced 36-song and 51-song sets**, which are the populations
  Table 2's KPCorpus and Rock results are measured on (§7.1 (2)).
- **Any uncertainty on any value except Table 3's.** Standard deviations are printed for the BaCh
  full-chord table alone; **Tables 2, 4 to 15 and both prose comparisons carry none.** The
  significance tests are reported as p-values without the underlying spreads.
- **Any per-label, per-mode or per-corpus-section error breakdown.** **The paper has four
  error-analysis sections** — §6.1.1, §6.2.1, §6.3.1 and §6.4.1 — **and all four treat the errors
  qualitatively**, naming kinds of case and exhibiting figures: *"a non-trivial number of cases"*,
  *"many segments where the first event did not contain the root"*. **What they do count is not
  errors**: §6.4.1 counts *"three of the songs"* whose modes were blues-influenced, and §6.3.1
  compares corpus sizes, *"less than a third compared to BaCh, and less than a tenth compared to
  TAVERN"*.

  *(★ CORRECTED AT THE SWEEP, BEFORE THIS FILE LANDED. FORMER WORDING, PRESERVED (#12): "**Both
  error-analysis sections are qualitative: they name kinds of case and exhibit figures, and count
  nothing.**" **Two defects in one sentence.** *Both* is a count this read never derived and the
  paper carries four such sections — the second instance of the same tell, recorded at §8.3. And
  *count nothing* is **refuted by two of the four**, at the two places now quoted above.)*

  *(On the word* figures *in both wordings: it means the paper's own numbered illustrations,
  Figures 1 to 11 — neither the musical sense `CLAUDE.md`'s Conventions reserve the bare word for
  nor the numerical sense they forbid it in. It is kept for that use alone in this file, and
  numerical quantities are called values or numbers throughout.)*
- **Inter-annotator agreement, on any corpus.** BaCh is annotated *"by a human expert"*, singular;
  TAVERN's second annotation and adjudication exist by design but *"many pieces do not currently
  have"* them and **only the first annotation was used**; the KP Corpus labels are a textbook's, with
  corrections supplied by a third party; the Rock labels are a songbook's, machine-read and
  hand-corrected by the authors.

### §7.3 What is both measured and structural here

These are the places where the paper's evidence bears on a design decision rather than on its own
performance claim.

- **(a) The segment-level measure and the event-level measure come apart, widely, and the paper names
  the cause.** On TAVERN the semi-CRF reports **78.0 event-level accuracy against 64.0 segment-level
  F-measure**, and HMPerceptron **57.0 against 22.5**. The cause is the criterion quoted at §5.2 —
  both boundaries and the label must match — together with the mechanism at C-2: one wrong event
  invalidates its whole segment. **The gap is a property of the measure, not only of the systems.**
- **(b) Enabling a label family pays, measurably, on the corpus that contains it.** Augmented-sixth
  features: 72.0 / 53.5 → **73.4 / 54.3** on all four measures (Table 8). Suspended and power
  features: 66.0 / 48.5 → **69.4 / 58.3**, the segment-level F-measure moving **9.8** points
  (Table 12; the subtraction is this read's). **Both are ablations of the label set and its features
  together, not of the features alone.**
- **(c) Metrical accent pays about six points on both measures** (§6.6), on one fold set. **★ WHAT
  THE ABLATION REMOVES IS THE WHOLE ACCENT FAMILY AND NOT THE ONE CHORD-CHANGE TERM** — the paper's
  words are *"with and without ALL accent-based features"* (p. 8, emphasis this read's), which
  reaches f₃₆ and every accent-weighted purity, coverage and bass feature alike. *(This precision
  was added at the cross-check, §9.4: the first extract had it and this read's first writing did
  not.)*
- **(d) A rule-based system with hand-set weights beats both learned systems at root level on the
  smallest corpus**, and the paper's explanation is training-set size and train/test mismatch
  (§5, Tables 9 and 11, C-3). **The KP Corpus has fewer than a third of BaCh's segments and fewer
  than a tenth of TAVERN's**, which is the paper's own comparison (p. 10).
- **(e) The weak factorization's blind spot is patched by a hand-written consonance heuristic**
  (§2.5), not by widening the model. **This is a structural cost of the chosen factorization, stated
  by the authors.**
- **(f) The key is excluded by design, and the cost is argued and not measured** (§3.3(a), C-1). The
  paper's own mechanism for the cost — that V-I and I-IV share a root distance while differing in
  distribution, and that transition distributions differ between major and minor — is a claim about
  **what a root-distance-only transition feature cannot represent**.
- **(g) The inversion and the seventh type are recoverable after the fact, by stated procedures**
  (§3.2), so their absence from the label set is a factorization choice rather than a loss.

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it did not re-open

**Eight of the nineteen pages were re-opened as images after §1 to §7 were written** — **pages 4 to
8 and pages 9 to 11** — chosen as the pages carrying the transcribed values and the sentences the
findings of §7.1 rest on. Every re-opened image was checked for presence and legibility at the image.

**Eleven pages were NOT re-opened: 1, 2, 3 and 12 to 19.** The claims of this file that rest on them,
named so a later reader knows which sentences carry one pass and not two:

- **§1's identity findings** — the arXiv line, the unfilled citation header, the three forms of the
  title (page 1, and the running head, which appears on every re-opened page as well).
- **§2.2, §2.3 and §2.4** — the equations, the weak-model restriction, the two named assumptions, and
  the two sentences that introduce **L** without valuing it (pages 2 and 3).
- **§2.5 and §2.6** — the four figuration definitions, the consonance heuristic, and the accent
  values (pages 15 and 16).
- **§3.2's inversion sentence** (page 14).
- **F-6, F-7 and F-8**, and the chord-bigram arithmetic of §6.1 (pages 16 to 19).

### §8.2 What the read-back and the sweep struck in this side's own writing

Named rather than counted, and each corrected at its site with the former wording preserved (#12)
where a claim changed:

- **An underived count at §6.4** — *"Sixteen stated improvements"* over a list of twenty-five values.
  Struck at the sweep. **It is a degradation tell and is at §8.3.**
- **An underived count and a false claim in one sentence at §7.2** — *"Both error-analysis sections
  … count nothing"*, where the paper has four such sections and two of them count something. **The
  count half is the same tell; the false half was refuted by re-reading the two sections at their
  pages.**
- **A negative stated wider than the act that produced it, at §1** — *"no page of the held file
  carries a volume, an issue, a page range, a DOI or the year 2019"*, where this read met no such
  value and never searched for one. **Cadence 7's own class**, and it is the reason every negative
  in §7.2 now carries the phrase *in the pages as read*.
- **Three claims narrowed at the sweep without a former wording being load-bearing:** *"every later
  section is a development of it"* (softened to the body sections); *"the only feature count in the
  paper"* (bounded to what this read met); and *"the body, the tables and the related-work section
  all read HMPerceptron"* (bounded to the occurrences met — and the re-reading then **strengthened**
  the finding, because Figure 6's caption turned out to read HMPerceptron, so the two HMPtron
  captions are two of the three figure captions naming that system and not a uniform caption style).
- **One transcription error caught during the writing, before any of it was read back:** Table 7's
  semi-CRF recall was first taken down as 60.9 — which is Table 6's recall for the same system — and
  corrected to **68.4** against the page while §5.5 was being written. **The printed value is 68.4**,
  confirmed again at the read-back of page 8.
- **One conflation caught during the writing:** the number 5 appears in the paper as a threshold on
  label occurrences (p. 5) and as a threshold on feature counts (p. 7), and a first draft of §6.7
  ran them together. **The two are now held apart in that section**, and no connection between them
  is claimed.
- **One completeness gain rather than a defect:** the read-back added the TAVERN label-count check to
  §6.1, which the first writing had passed over because the paper prints that total without its
  product.

### §8.3 The degradation tells, reported unprompted

**★ ONE OF THE USER'S NAMED TELLS FIRED THREE TIMES IN THIS SITTING'S OWN WRITING, AND THE THIRD
INSTANCE WAS INSIDE THE CORRECTION OF THE FIRST.**

**The tell: a count put on this side's own reading without deriving it.** The three instances,
named rather than totalled a second time:

1. **§6.4's *"Sixteen stated improvements"***, over a list this side had itself just written. Caught
   at the sweep, before the file landed.
2. **§7.2's *"Both error-analysis sections"***, where the paper carries four. Caught at the same
   sweep. **The same sentence also asserted that those sections count nothing, which two of them
   refute** — so this instance is both the count tell and a claim refuted by the object.
3. **★ *"twenty-three"*, written INSIDE the correction of instance 1**, where recounting the listed
   values gives twenty-five, of which twenty-three are improvements the paper states. Caught by
   recounting at the sentence, within the same act. **This is the shape the hundred-and-seventy-second
   entry records of itself — a count defect written inside the very paragraph reporting a count
   defect — and it is recorded rather than quietly fixed.**

**What this side does NOT claim.** That three instances of one named tell are the same thing as three
different tells firing; they are not, and the hundred-and-seventy-second's sitting met the same
shape — one tell, three instances — and closed at one member on it. **And that all three were caught
before the file landed is not a defence**: the hundred-and-seventy-fourth's close records in terms
that catching a tell before landing does not lower its count.

**The consequence under the user's standing rule of 2026-08-15**, stated here and carried into the
handoff entry: **this sitting reports the tell unprompted, closes at the member boundary, and
recommends that the next member be taken by a fresh session.** The stop is a verified one — the
member is complete through all eight steps and both files are landed and proved — so the
recommendation is not that work be abandoned mid-thing.

**One further class the sweep struck, recorded because it is not a tell but is adjacent:** the
over-wide negative at §1 above. A negative stated wider than the act that produced it is a defect of
bound rather than of derivation, and cadence 7 is what catches it.

**★ AND ONE MORE OF THE SITTING'S OWN-STATE CLASS WAS FOUND AFTER THIS SECTION WAS WRITTEN, AT THE
PROOF OF THE SECOND LANDING.** §9.5 said two pages had been re-opened at the cross-check step; **they
had not** — they had been read earlier in the sitting, and the cross-check opened no page at all. It
is corrected at its own site with the former wording preserved, and it is recorded here so that this
section's account of what the passes caught is not itself stale. **What caught it was reading the
landed copy's own last lines rather than searching them**, which is the hundred-and-seventy-third
entry's §3 point 1 working exactly as that entry says it does.

### §8.4 The bound on this section

**This section reports what two passes by this side over this side's own writing found.** Both passes
are by the same reader who wrote the text, one of them the day's only reader of the paper. **Nothing
here establishes that the remainder is clean** — two of the defects above had already survived the
act of writing them and the act of reading the paragraph they sit in, and one of them survived into
the correction of another. **Eleven pages carry claims that have had one pass and not two**, named at
§8.1.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**The first extract was opened only after this file had landed** — step 7 of the procedure — staged
from `reading_pass/extracts/masada-bunescu-2019-chord-recognition-in-symbolic-music-a-segmental-crf-model.md`
at **50,006 bytes** and read whole. It records itself as written **2026-09-06**, all nineteen pages
read at the object, by the session that booted on the hundred-and-twenty-first handoff entry.

**The two reads are independent on the paper and NOT independent on the record.** The first extract
reaches `FRAMEWORK.md` §5, §9's DP-C, §S4(d), DP3 and §14.1, the findings surface's V5 and V10 rows,
`reading_pass/population.md` §3, the slice derivation, the bibliography row and the ratifying ruling.
**This read opened none of those objects.** So on the whole question of what the RECORD says about
this paper — and on both ratified statements resting on it — **this is not a second opinion but
silence**, and nothing below should be read as confirming or disputing that half.

### §9.2 Every value both extracts transcribed agrees, digit for digit

Checked value by value across both files: **Tables 3, 4 and 5 in full, including every standard
deviation; Tables 6 and 7 in full; Tables 8 to 11 in full; Tables 12 to 15 in full; the two prose
comparisons (HarmAn 75.8 against semi-CRF 75.3; the HMPerceptron accent side-measurement 79.8 / 70.2
and 79.8 / 70.3); all four corpora's event, segment and label counts; the three BaCh label counts
102, 68 and 90; the chord-bigram template's 4,332; and the held file's 1,289,352 bytes.**

**No disagreement anywhere among them.** Both reads also independently derive the same differences
behind the paper's stated improvements — the first extract's finding (3) works +7.6, +38.2, +41.5,
+21.3 and +31.5 from the same printed cells this file's §6.4 does, and they agree.

**Both reads independently reach the same identity finding:** the held file is the
arXiv:1810.10002v2 preprint of 26 October 2018 with the TISMIR template unfilled, against a record
row naming TISMIR 2(1) 2019.

### §9.3 The disagreements, named rather than counted

**★ (1) ONE GOES AGAINST THE FIRST EXTRACT, AND IT MOVES A CLAIM ABOUT THE PAPER.** The first
extract quotes page 8 as *"The results from Table 5 show a **statistically significant** decrease in
accuracy when the accent-based features are removed from the system."* **The paper prints
"substantial", not "statistically significant"** — *"The results from Table 5 show a substantial
decrease in accuracy when the accent-based features are removed from the system."* **Established
twice at the page**, at this sitting's whole read of pages 1 to 10 and again at its read-back of
pages 4 to 8.

**Why it is not a harmless slip.** The first extract's finding (2) builds a criticism on the
substituted words: *"the significance is asserted in prose with no p-value or a standard deviation in
the table"*. **The paper asserts no significance there at all.** So a defect inside a quotation
produced a stated precision against the paper that the paper does not support. **No transcribed value
moves** — Table 5's four values are identical in both files, and the six-point difference stands in
both — but a claim about what the authors assert does.

**That file is untouched**, on the standing ground that rewriting another read's text destroys what
the doubling compares. **The question of whether it is corrected at its own site is the user's.**

**(2) ONE IS GENUINELY UNRESOLVED AT THE PAPER, AND IT IS RECORDED AS UNRESOLVED RATHER THAN
DECIDED.** The two reads say opposite things about whether the method assumes a spelling.

- **The first extract:** *"It does not assume a key, a voice assignment, a spelling (the labels are
  enharmonically collapsed; the notes' spelling is 'immaterial')"*.
- **This file, at §3.1:** spelled pitch is assumed *"at least for the scale-step tests"*, because the
  passing and neighbor heuristics are defined on *"one scale step"* relations and the augmented-sixth
  definitions on sharpened scale degrees.

**Resolved as far as the paper goes, which is not all the way.** The *"immaterial"* sentence (p. 5)
is about **matching sounding notes to a chord label** — its own clause says *"as long as they are
enharmonic with the root, third, fifth, or added note of the labeled chord"* — and it does not reach
the step relations. The step relations (p. 15) are stated in spelled terms and **the paper nowhere
says how a step is computed**, which it would have to for a system that declines to know the key.
**So the two statements are about different things and neither is refuted; what the paper leaves open
is how a scale step is determined without a key.** Page 15 has had one pass in this read (§8.1).

**(3) Nothing else went against either side.** No claim of this file was refuted by the first
extract, and no value of the first extract was refuted by this read.

### §9.4 What the doubling produced that neither read had alone, in both directions

**The first extract has, and this read lacks:**

- **The whole record half** — every ratified statement resting on this paper, and the two
  verification rows it re-verifies (§9.1).
- **The precision that the accent ablation removes the WHOLE accent family**, not the single
  chord-change term: *"all accent-based features"*, reaching f₃₆ and every accent-weighted purity,
  coverage and bass feature. **This read's first writing did not carry it; it is adopted into §7.3(c)
  at this cross-check, with the adoption marked there.**
- **The reading that the accent SOURCE matters less than the accent USE**, drawn from the paper's own
  side-measurement — HMPerceptron scoring 70.2 against 70.3 with the two accent sources, where the
  semi-CRF loses 6.4 points when the accent family is removed. **This read transcribed both values
  and drew nothing from the pair.**
- **The correction of an attribution on the record side** (its finding (3)), which this read could
  not have made with the record unopened.

**This read has, and the first extract lacks — four findings, each established at the paper:**

- **★ Table 2's KPCorpus and Rock rows pair whole-corpus statistics with reduced-subset results**
  (§7.1(2)). The first extract's own summary table keeps the 46/36 and 59/51 populations properly
  apart, so it holds the right values — **but it does not record that the paper's own summary table
  mixes them**, and a reader lifting Table 2 gets the mixture.
- **★ The canonical-root rule leaves two of its twenty-four entries undetermined, and the two ties
  are broken in opposite directions** (§7.1(6)). The first extract quotes the rule and does not test
  it.
- **The paper's three forms of its own title, and the two naming inconsistencies** — *"HMPtron"* in
  two of the three figure captions naming that system, and *"G:maj:add6"* in the body against
  *"G:maj6"* in Figure 6's caption and in the figure itself (§7.1(3), (4)).
- **The TAVERN label-count product, reconstructed** (§6.1's last bullet), which the paper states as a
  total only.

### §9.5 What the cross-check does NOT establish

**It compared two files, and it opened no page of the paper at all.** Both disagreements were
resolved against readings of pages 5 and 8 **already made earlier in this sitting** — each of those
two pages having been read twice, at the whole read and again at the read-back — and **no page image
was requested at this step.** **It opened none of the record objects** the first extract reaches, so
the whole of that file's record half stands unchecked here. **It changed no transcribed value in
either file**, and it changed nothing at all in the first extract, which is untouched.

*(★ CORRECTED AT THE PROOF OF THE SECOND LANDING, WHICH IS WHERE READING THE LANDED COPY'S LAST LINES
CAUGHT IT. FORMER WORDING, PRESERVED (#12): "**It did not re-read the whole paper a third time —
pages 8 and 5 were re-opened for the two disagreements above, and no other page was opened at this
step.**" **That states an act this side did not perform at that step.** The two pages were read
earlier in the sitting and the cross-check worked from those readings; writing "re-opened" was a
claim about this side's own acts taken from the memory of having read the pages rather than checked
against which call opened them, which is the never-work-from-memory failure applied to a sitting's
own record of itself. **The resolution of both disagreements is unaffected** — page 8 was read twice
before the cross-check and page 5 twice — **and no value moves.**)*

**And it is not a clean bill for either file.** Both reads are by readers working from the same
nineteen pages; where both are silent on the same thing, the doubling says nothing about it.

---

## §10 — The user-ordered fact- and source-check, run after this file had landed three times

The user's standing rule of 2026-09-12 extends the pre-landing check to landed work on four axes:
completeness, coherence, correctness, and misuse of hyperbole and absolutes. **This file was re-read
WHOLE as landed at 73,091 bytes, at the device's own copy staged back**, and **page 1 was re-opened**
— the one page image this check fetched. Every correction is at its own site above with the former
wording preserved (#12). Named rather than counted:

### §10.1 Two quotation defects of this read's own, at §3.3(b)

**A word dropped from inside a quotation and a parenthetical cut from its tail without an ellipsis**,
in the sentence giving the authors' first reason for excluding the key. **This is the same class this
file reports against the first extract at §9.3(1)**, and the first extract has that sentence right at
both points — which is how the defects were found, the two texts having been compared again on this
pass. **They survived this read's read-back, its sweep and the cross-check.** Neither moves a value.

### §10.2 Two arithmetic or counting errors about the paper's own structure

- **§7.1(6) described the canonical-root rule as reaching twelve scale degrees per mode and leaving
  two undecided**, which contradicted that finding's own closing sentence. The rule is exercised at
  five degrees per mode and leaves one in each. **The finding itself — the two ties, broken in
  opposite directions — is unchanged.**
- **§1 counted three forms of the paper's title where there are two**, the citation header's copy
  being word for word the page-1 title. Established at page 1 re-opened.

### §10.3 Two absolutes this read had not derived, at §5.3

*"A one-tailed Welch's t-test **throughout** … and at 0.01 **elsewhere**"*. **The KP Corpus carries no
significance claim at all**, so *elsewhere* asserted a test the paper does not report. Now stated as
the comparisons that carry one, with the KP Corpus and the Table 5 ablation named as carrying none.

### §10.4 One protocol miscount, at §5.3

The Rock 51-song split was given as *"ten folds of 5 test songs … plus one of 6"*, **which is eleven
folds where the paper states ten**. Corrected to nine of five plus one of six, which sums to 51.

### §10.5 One negative and two cross-references bounded

**§0's *"None of the four names this paper…"*** was a negative over four whole entries stated as
though a search had been run; it is now bounded to what this side met as read. **§7.1(2)'s references
to §5, §5.3 and §5.4** were qualified as **the paper's**, this file having sections of the same
numbers. **F-11's citation** was narrowed to Table 11, the only table carrying all three systems.

### §10.6 What this check did NOT do, and what it does not establish

It opened **one page image, page 1**, and no other. It did not re-read the paper, **did not re-open
the first extract as a file** — the comparison at §10.1 was made against the passages of it quoted in
§9 — ran no web access, swept no repository, and **changed no transcribed value of the paper's, no
byte count, no modification time and no verdict.** The eleven pages named at §8.1 still carry claims
that have had one pass and not two, **page 1 excepted, which this check re-opened**.

**And it is a further pass over the same writing by the same side.** **Its sharpest finding is that
this file carried two quotation defects of exactly the class it reports against the other read** —
through a read-back, a sweep and a cross-check — **so nothing about its yield says the remainder is
clean.**

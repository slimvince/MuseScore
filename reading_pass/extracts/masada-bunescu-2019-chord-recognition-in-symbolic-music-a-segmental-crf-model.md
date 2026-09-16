# EXTRACT — Masada & Bunescu, "Chord Recognition in Symbolic Music: A Segmental CRF Model, Segment-Level Features, and Comparative Evaluations on Classical and Popular Music" — Task B candidacy row 10, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All nineteen pages of the held PDF were read AT THE OBJECT: staged through the bridge
> and read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.**
> The held file is the arXiv preprint (see Identity below); **every location below is the held
> document's own printed page number** (1–19) and its section or table.
>
> **Why this paper and its place in L2's slice.** It is row 10 of `reading_pass/candidacy_upgrades.md`
> (line 72), ADMITTED there as *"The segmental CRF; the machinery of DP-C's chosen answer and the source
> of V5 and of DP-C's segmental gains. Symbolic, on our repertoire's kind of input."*
> `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 (line 57) places it in L2's slice: *"DP-C's chosen
> answer's machinery — segmentation decided with the chord identity."* It is first in group 2 of the
> proposed reading order ("segmentation decided with the labelling": rows 10, 11, 19, 20, 18, 4, 47) and
> **its reading opens group 2.** **The record cites this paper at three ratified places and two verified
> figures:** `FRAMEWORK.md` §5, the L1 charter's "Why metric strength earns its place" paragraph (lines
> 352–356): *"removing metrical-accent features from a segmental analyser costs about six points of
> F-measure. [FACT — both.]"* (restated in the sealed first-stage text at lines 1684–1687, which still
> carries the former V4 wording beside it); `FRAMEWORK.md` §9 DP-C (lines 690–701): *"a jointly-decoding
> segmental model beating event-level tagging by 7.6 to 38.2 points of segment F-measure on one corpus
> and 21.3 to 31.5 on another"* [FACT], restated at §S4(d) (lines 1596–1598) and named at DP3 (line
> 1805) as one of the two measurements excluding "before"; and §14.1 (lines 1008–1010), *"the two
> symbolic systems built on it whose measured gains over event-level tagging are quoted at DP-C"*. The
> findings surface's verification table carries **V5 VERIFIED** (line 609; `reading_pass/population.md`
> line 106: Table 5, F 77.6 → 71.2) and **V10 VERIFIED** with the segmental gains attributed to this paper
> (`population.md` line 111). Ruling 1 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the
> gate: no derivation before L2's slice of Task B is read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — a finding of the row-3 shape

Kristen Masada and Razvan Bunescu, School of Electrical Engineering and Computer Science, Ohio
University, Athens OH. Printed title: "Chord Recognition in Symbolic Music: A Segmental CRF Model,
Segment-Level Features, and Comparative Evaluations on Classical and Popular Music". **The held file
is the arXiv preprint, not the published journal article.** The left margin of page 1 prints
*"arXiv:1810.10002v2 [cs.SD] 26 Oct 2018"*; the TISMIR header block at the top of page 1 is the
journal's template with its fields UNFILLED: *"Masada, K. and Bunescu, R. (2018). … Transactions of the
International Society for Music Information Retrieval, V(N), pp. xx–xx, DOI: https://doi.org/xx.xxxx/xxxx.xx"*.
The bibliography's row (`docs/research_papers/BIBLIOGRAPHY.md` line 24) names *TISMIR 2(1), 2019*,
the TISMIR article URL (`10.5334/tismir.18`) and, in parentheses, *arXiv:1810.10002*, tier *CC (TISMIR
CC BY)*. **Title and authors match the row; the venue, volume and year printed on the held document
do not — the held document is the second arXiv version dated 2018, and whether the TISMIR 2(1) 2019
text differs from it is not establishable from what is held.** No licence line is printed on the held
document. Routed to the bibliography reconciliation beside rows 28's, 3's and 29's findings. Nineteen
pages; nine sections (Introduction and Motivation; Semi-CRF Model for Chord Recognition; Chord
Recognition Labels; Chord Recognition Features; Chord Recognition Datasets; Experimental Evaluation;
Related Work; Future Work; Conclusion), notes, acknowledgments, references, and three appendices
(A Types of Chords in Tonal Music; B Figuration Heuristics; C Chord Recognition Features); eleven
figures, fifteen tables, eleven numbered equations.

**File:** `docs/research_papers/masada_bunescu_2019_tismir_segmental_crf_chord_recognition.pdf`
(1,289,352 bytes at the listing).

## Claims, labeled

### What the method decides, and from what

**★ [FACT, p. 1 Abstract; p. 2 §2] The method decides a SEGMENTATION of the piece into chord spans and
a CHORD LABEL per span, TOGETHER, in one decode — and decides NO tonality.** *"a new approach to
harmonic analysis that is trained to segment music into a sequence of chord spans tagged with chord
labels. Formulated as a semi-Markov Conditional Random Field (semi-CRF), this joint segmentation and
labeling approach enables the use of a rich set of segment-level features"* (p. 1). *"The maximum is
taken over all possible labeled segmentations of the input, up to a maximum segment length."* (p. 3.)
The key is neither an input nor an output: *"Because the labels do not encode for function, the model
does not require knowing the key in which the input was written."* (p. 4.)

**★ [FACT, p. 4 §3] The authors' own reason for leaving the key out, and their own statement that key
context would help.** *"The decision to not use the key context was partly motivated by the fact that
3 of the 4 datasets we used for experimental evaluation do not have functional annotations (see Section
5). Additionally, complete key annotation can be difficult to perform, both manually and automatically.
Key changes occur gradually, thus making it difficult to determine the exact location where one key
ends and another begins (Papadopoulos and Peeters, 2009). This makes locating modulations and
tonicizations difficult and also hard to evaluate (Gómez, 2006). At the same time, we recognize that
harmonic analysis is not complete without functional analysis. Functional analysis features could also
benefit the basic chord recognition task described in this paper. In particular, the chord transition
features that we define in Appendix C.4 depend on the absolute distance in half steps between the
roots of the chords. However, a V-I transition has a different distribution than a I-IV transition,
even though the root distance is the same. Chord transition distributions also differ between minor
and major keys. As such, using key context could further improve chord recognition."* (p. 4.)

**★ [FACT, p. 2 §2; p. 1 Figure 1] The candidate grid is the set of PARTITION POINTS — every note onset
and offset — and an EVENT is the set of pitches sounding between two consecutive partition points;
segments are runs of consecutive events.** *"Since harmonic changes may occur only when notes begin or
end, we first create a sorted list of all the note onsets and offsets in the input music, i.e. the list
of partition points (Pardo and Birmingham, 2002) … A basic music event (Radicioni and Esposito, 2010)
is then defined as the set of pitches sounding in the time interval between two consecutive partition
points."* (p. 2.) Each event carries, per pitch, *"a boolean value … indicating whether or not it is
held over from the previous event"* (p. 2). A note spanning several events has *"length … the sum of
the length of all events that span the duration of that note"* (p. 16).

**★ [FACT, p. 2–3 §2, eqs. 1–5; p. 3] The model: a semi-Markov CRF (Sarawagi & Cohen 2004) over
labeled segmentations, restricted to the "weak" form of Muis & Lu 2016 — segment-label features that
see the segment and its label but NOT the previous label, plus separate label-transition features.**
P(s, y | x, w, u) = exp(wᵀF(s,y,x) + uᵀG(s,y,x)) / Z(x) (eq. 3), F the sum over segments of
f(s_k, y_k, x) (eq. 4), G the sum over segments of g(y_k, y_{k−1}, x) (eq. 5). *"Following Muis and Lu
(2016), for faster inference, we further restrict the local segment features to two types: segment-label
features f(s_k, y_k, x) that depend on the segment and its label, and label transition features g(y_k,
y_{k−1}, x) that depend on the labels of the current and previous segments."* (pp. 2–3.) Two stated
assumptions: stationarity (features do not change with position) and the Markov assumption (a segment's
label depends only on its boundaries and the adjacent segments' labels) (p. 3).

**★ [FACT, p. 3 §2, eqs. 6–9] Inference is exact by a semi-Markov Viterbi recursion with a maximum
segment length L; the best labeled segmentation is recovered in linear time.** *"Let L be a maximum
segment length. … V(i, y) = max over y′, 1≤l≤L of V(i−l, y′) + wᵀf(⟨i−l+1, i⟩, y, x) + uᵀg(y, y′, x)"*
(eq. 9), base cases V(0, y) = 0 and V(j, y) = −∞ for j < 0. *"Their number is exponential in the length
of the input, which rules out a brute-force search."* (p. 3.) **The value of L is not stated anywhere in
the held document.**

**★ [FACT, p. 3–4 §2, eqs. 10–11] Learning: maximise the regularised conditional log-likelihood by
L-BFGS (StatNLP package); the partition function and expectations by a forward–backward analogue.**
*"minimizing the negative log-likelihood −L(T; w, u) and an L2 regularization term"* (eq. 11); *"This is
a convex optimization problem, which is solved with the L-BFGS procedure"* (p. 4). **The regularisation
constant λ is not valued in the held document.** Feature pruning: *"we only used features whose counts
were at least 5"* in the training data, counted *"using only the true segment boundaries and their
labels"* (p. 7).

### The label set (p. 4 §3; Appendix A, pp. 13–14)

**★ [FACT, p. 4] The core label is root × mode × added note — 12 roots × {major, minor, diminished} ×
{none, fourth, sixth, seventh} = 144 labels — with NO inversion and ONE generic seventh.** *"Note that
there is only one generic type of added seventh note, irrespective of whether the interval is a major,
minor, or diminished seventh, which means that a C major seventh chord and a C dominant seventh chord
are mapped to the same label."* The seventh's quality and the inversion are stated to be recoverable by
*"a simple post-processing step"* from the notes and the bass (p. 4; Appendix A.1, p. 14: *"finding its
inversion can be done in a straightforward post-processing step, as a function of the bass note in the
chord"*). Augmented sixths: 36 labels (12 lowest notes × Italian/German/French); suspended and power
chords: 48 labels (12 roots × sus2/sus4/7sus4/pow) (p. 4). *"the number of parameters in our model is
largely independent of the number of labels … because we design the chord recognition features … to not
test for the chord root, which also enables the system to recognize chords that were not seen during
training."* (p. 4.)

**★ [FACT, p. 5 §5.1] The labels are normalised ENHARMONICALLY because the system is key-agnostic; the
notes are not.** *"Reliably producing one of two enharmonic chords cannot be expected from a system that
is agnostic of the key context. Therefore, we normalize the chord labels and for each mode we define a
set of 12 canonical roots, one for each scale degree … we selected the one with the fewest sharps or
flats in the corresponding key signature. … The actual chord notes used in the music are left unchanged.
Whether they are spelled with sharps or flats is immaterial, as long as they are enharmonic with the
root, third, fifth, or added note of the labeled chord."* Of BaCh's 144 possible labels 102 appear (68
five or more times); after normalisation 90 labels remain (p. 5).

### The features (p. 4 §4; Appendix C, pp. 15–19)

**★ [FACT, p. 4 §4] Five feature families, every one a function of the CANDIDATE SEGMENT and the
CANDIDATE LABEL.** *"Segment purity features compute the percentage of segment notes that belong to a
given chord … Chord coverage features determine if each note in a given chord appears at least once in
the segment … Bass features determine which note of a given chord appears as the bass in the segment …
Chord bigram features capture chord transition information … Finally, we include metrical accent
features for chord changes, as chord segments are more likely to begin on accented beats."* (p. 4.)

**[FACT, Appendix C.1–C.3, pp. 16–18] The purity, coverage and bass features each come in a plain, a
duration-weighted and an ACCENT-weighted form; real-valued features are discretised into K+2 Boolean
bins (default bins 0, 0.1, …, 1.0).** Purity f₁ = |{n ∈ s.Notes : n ∈ y}| / |s.Notes|; f₂ weights by
note length, f₃ by accent value (p. 16). Coverage f₄–f₆ test root, third, fifth present; f₇ tests all
chord notes present; f₈/f₉ test the added note present/absent; f₁₀ fires when the added notes' total
length exceeds the root's (p. 16); f₁₁–f₁₉ their duration- and accent-weighted forms (p. 17). Bass:
two definitions of the segment's bass — *"the lowest note of the first event in the segment"* (f₂₀–f₂₃)
and *"the lowest note in the entire segment"* (f₂₄–f₂₇) — plus duration-weighted forms over events
(f₂₈–f₃₅) (p. 18). Parallel families for augmented sixths (as₁–as₁₇) and suspended/power chords
(sp₁–sp₁₉) (pp. 17–19).

**★ [FACT, Appendix B and C.1.1/C.2.3/C.3.3, pp. 15–19] The CHORD-TONE / FIGURATION decision is made
INSIDE the segment scoring, relative to the candidate label, by four heuristics — passing, neighbor,
suspension, anticipation — each defined by anchor notes, step relations, length and accent; every
purity, coverage and bass feature has a "figuration-controlled" twin that ignores the notes so
detected.** *"We designed a set of heuristics to determine whether a note n from a segment s is a
figuration note with respect to a candidate chord label y."* (p. 15.) Passing: two anchors a step above
and below (or below and above), the note not longer than either anchor, its accent strictly smaller than
the first anchor's, at least one anchor in the segment, the note non-harmonic and both anchors harmonic
with respect to the segments they belong to (p. 15). Neighbor, suspension and anticipation are defined
in the same style (p. 15). *"because the weak semi-CRF features … do not have access to the candidate
label y_{k−1} of the previous segment s_{k−1}, we need a heuristic to determine whether an anchor note is
harmonic whenever the anchor note belongs to the previous segment"* — consonance with the other notes of
its event (p. 15). *"We emphasize that the rules mentioned above for detecting figuration notes are only
approximations."* (p. 15.)

**[FACT, Appendix C.4, p. 19] Chord bigrams: (mode, added) of both chords and the root interval in
semitones — 4,332 possible, only those seen in training used.** g₁(y, y′) = 1[(y.mode, y′.mode) ∈ M×M
∧ (y.added, y′.added) ∈ {∅,4,6,7}² ∧ |y.root − y′.root| ∈ {0,…,11}]; *"y.root is replaced with y.bass
for augmented 6th chords"* (p. 19).

**★ [FACT, Appendix C.5, p. 19; p. 15–16] The metrical-accent feature is ONE feature: the accent value
of the first event of the candidate segment, the accent being Music21's `beatStrength()` from the
NOTATED meter.** *"a new feature is defined as the accent value of the first event in a candidate
segment: f₃₆(s, y) = s.e₁.acc"* (p. 19). *"The accent value is determined based on the metrical position
of a note or event, e.g. in a song written in a 4/4 time signature, the first beat position would have a
value of 1.0, the third beat 0.5, and the second and fourth beats 0.25. Any other eighth note position
within a beat would have a value of 0.125, any sixteenth note position strictly within the beat would
have a value of 0.0625, and so on."* (p. 16.) **The V5 measurement removes "all accent-based features"
(p. 8) — f₃₆ AND the accent-weighted forms f₃, f₁₄–f₁₆, f₁₈, f₃₂–f₃₅ and their augmented-sixth and
suspended/power twins — not f₃₆ alone.**

### The data (p. 5–6 §5)

**[FACT, p. 5, Table 2 p. 7] Four corpora.** BaCh (Radicioni & Esposito 2010): 60 Bach chorales,
5,664 events, 3,090 segments, 90 labels. TAVERN (Devaney et al. 2015): 27 sets of theme and variations
(17 Beethoven, 10 Mozart), 63,876 events, 12,802 segments, 69 labels — *"we only used the first
annotation for each of the 27 sets"* (p. 5), the Roman-numeral annotation translated by script into the
key-independent label set. KP Corpus (Kostka & Payne 1984, as compiled by Bryan Pardo): 46 excerpts,
3,888 events, 911 segments, 76 labels; *"Bryan Pardo's original MIDI files for the KP Corpus also contain
several missing chords, as well as chord labels that are shifted from their true onsets. We used chord
and beat list files sent to us by David Temperley to correct these mistakes."* (p. 5.) Rock: 59 songs
from Hal Leonard's *The Best Rock Songs Ever (Easy Piano)*, 25,621 events, 4,221 segments, 48 labels,
made by optical music recognition (PhotoScore) with labels corrected by hand (p. 6).

### The evaluation protocol and the comparators (p. 6–7 §6)

**★ [FACT, p. 6 §6] Two measures: event-level accuracy and segment-level F-measure, where a predicted
segment is correct ONLY if both its boundaries and its label match a true segment.** *"Note that a
predicted segment is considered correct if and only if both its boundaries and its label match those
of a true segment."* (p. 6.) Precision, recall and F over segments, pooled over all songs.

**[FACT, p. 6–7] The comparators are HMPerceptron (Radicioni & Esposito 2010, an event-level HMM
trained by perceptron) and Melisma (Temperley & Sleator 1999, hand-set weights); the authors' own
caveats on the comparison.** *"HMPerceptron and semi-CRF are data driven … Both approaches are agnostic
of music theoretic principles such as harmony changing primarily on strong metric positions, however
they can learn such tendencies to the extent they are present in the training data."* *"Both Melisma
and HMPerceptron use metrical accents automatically induced by Melisma, whereas semi-CRF uses the
Music21 accents derived from the notated meter."* (p. 6.) BaCh: 10-fold cross-validation repeated ten
times with reshuffled folds, means and standard deviations over the ten runs (pp. 6–7). TAVERN: one
fixed split, 6 Beethoven and 4 Mozart sets held out (p. 8). KP: 11 folds on 46 songs; leave-one-out on
the 36 songs without augmented sixths (p. 9). Rock: 10 folds on 59 songs; 10 folds on the 51 songs
without suspended or power chords (p. 10). **Held-out evaluation throughout; hyper-parameters (L, λ)
not stated.**

### The results, as the paper states them (Tables 2–15, pp. 7–10)

**★ [FACT, Table 3, p. 7] BaCh, full chord: semi-CRF Acc_E 83.2 (s.d. 0.2), P_S 79.4, R_S 75.8, F_S 77.5
(s.d. 0.2); HMPerceptron₁ 77.2 (2.1) / 71.2 / 68.8 / 69.9 (1.8); HMPerceptron₂ 77.0 (2.1) / 71.0 / 68.5 /
69.7 (1.8).** *"a 6.2% improvement in event-level accuracy over the original model HMPerceptron₂, which
corresponds to a 27.0% relative error reduction … a 7.8% absolute improvement in F-measure over the
original HMPerceptron₂ model, and a 7.6% improvement in F-measure over the HMPerceptron₁ version, which
is statistically significant at an averaged p-value of 0.002, using a one-tailed Welch's t-test."*
(p. 7.) *"The standard deviation values … are about one order of magnitude smaller for semi-CRF than for
HMPerceptron, demonstrating that the semi-CRF is also more stable."* (p. 7.)

**[FACT, Table 4, p. 7] BaCh, root only: semi-CRF 88.9 / 85.4 / 83.0 / 84.2; HMPerceptron 84.8 / 78.0 /
76.2 / 77.0; Melisma 84.3 / 73.2 / 76.3 / 74.7.** Semi-CRF *"improves upon the event-level accuracy of
HMPerceptron by 4.1%, producing a relative error reduction of 27.0%, and that of Melisma by 4.6%. …
F-measure that is 7.2% higher than HMPerceptron and 9.5% higher than Melisma … p-value of 0.01"* (p. 7).

**★ [FACT, Table 5, p. 7; p. 8] BaCh, metrical accent ablation of semi-CRF (V5): with accent Acc_E
83.6, P_S 79.6, R_S 75.9, F_S 77.6; without accent 77.7, 74.8, 68.0, 71.2.** *"We verified empirically the
importance of metrical accent by evaluating the semi-CRF model on a random fold set from the BaCh corpus
with and without all accent-based features. The results from Table 5 show a statistically significant
decrease in accuracy when the accent-based features are removed from the system."* (p. 8.) **V5
RE-VERIFIED at the object: F 77.6 → 71.2, a difference of 6.4 points, "about six points" as the framework
states.** Two precisions: the measurement is on *"a random fold set"*, not the ten-times-repeated
cross-validation of Table 3 (whose with-accent F is 77.5, not 77.6), and the significance is asserted
without a p-value or a standard deviation in the table. And the companion finding, in the same paragraph:
*"we ran an evaluation of HMPerceptron on a random fold set from BaCh in two scenarios: HMPerceptron with
Melisma metrical accent and HMPerceptron with Music21 accent. The results did not show a significant
difference: with Melisma accent the event accuracy was 79.8% for an F-measure of 70.2%, whereas with
Music21 accent the event accuracy was 79.8% for an F-measure of 70.3%. This negligible difference is
likely due to the fact that HMPerceptron uses only coarse-grained accent information, i.e. whether a
position is accented (Melisma accent 3 or more) or not accented (Melisma accent less than 3)."* (p. 8.)

**★ [FACT, Tables 6 and 7, p. 8] TAVERN, fixed split: full chord semi-CRF 78.0 / 67.3 / 60.9 / 64.0
against HMPerceptron 57.0 / 24.5 / 20.8 / 22.5; root only semi-CRF 86.0 / 74.6 / 68.4 / 71.4 against
HMPerceptron 69.2 / 38.2 / 29.4 / 33.2 and Melisma 76.7 / 42.3 / 40.7 / 41.5.** *"semi-CRF outperforms
HMPerceptron by 21.0% for event-level chord evaluation and by 41.5% in terms of chord-level F-measure …
improves upon HMPerceptron's event-level root accuracy by 16.8% and Melisma's event accuracy by 9.3%.
Semi-CRF also produces a segment-level F-measure value that is 38.2% higher than that of HMPerceptron
and 29.9% higher than that of Melisma … p-value of 0.01"* (p. 8).

**[FACT, Tables 8–11, p. 9] KP Corpus: full chord, 46 songs, semi-CRF₁ (no augmented-sixth features)
72.0 / 59.0 / 49.2 / 53.5, semi-CRF₂ (with them) 73.4 / 59.6 / 50.1 / 54.3; root only, 46 songs,
semi-CRF 80.7 / 66.3 / 56.2 / 60.8 against Melisma 80.9 / 60.6 / 63.3 / 61.9; full chord, 36 songs
(leave-one-out), semi-CRF 73.0 / 55.6 / 50.7 / 53.0 against HMPerceptron 72.9 / 48.2 / 43.6 / 45.4;
root only, 36 songs, semi-CRF 79.3 / 61.8 / 56.4 / 59.0 against HMPerceptron 79.0 / 54.7 / 49.9 / 51.9
and Melisma 81.9 / 60.7 / 63.7 / 62.2.** *"Melisma outperforms both machine learning systems for root
only evaluation. Nevertheless, the semi-CRF is still competitive with Melisma"* (p. 9). Against
HarmAn (Pardo & Birmingham 2002), on their 45-song protocol ignoring rare labels: *"semi-CRF obtains an
event-level accuracy of 75.3%, demonstrating that it is competitive with HarmAn [75.8%]. However …
these results are still not fully comparable: sometimes HarmAn predicts multiple labels for a single
segment, and when the correct label is among these, Pardo and Birmingham divide by the number of labels
the system predicts and consider this fractional value to be correct. In contrast, semi-CRF always
predicts one label per segment."* (pp. 9–10.) The authors' own reading of KP: *"Both machine learning
systems struggled on the KP corpus … the smaller dataset, and thus the smaller number of training
examples … the textbook excerpts are more diverse … leading to mismatch between the training and test
distributions"* (p. 10).

**★ [FACT, Tables 12–15, p. 10] Rock: full chord, 59 songs, semi-CRF₁ 66.0 / 49.8 / 47.3 / 48.5,
semi-CRF₃ (with suspended and power-chord features) 69.4 / 62.0 / 54.9 / 58.3; root only, 59 songs,
semi-CRF 85.8 / 70.9 / 63.2 / 66.8 against Melisma 77.4 / 29.5 / 44.0 / 35.3; full chord, 51 songs,
semi-CRF 70.1 / 58.8 / 53.2 / 55.9 against HMPerceptron 61.3 / 41.0 / 29.9 / 34.6; root only, 51 songs,
semi-CRF 86.1 / 68.6 / 61.9 / 65.1 against HMPerceptron 80.7 / 51.3 / 36.9 / 42.9 and Melisma 77.9 /
30.6 / 45.8 / 36.3.** *"an 8.4% improvement in event-level root accuracy and a 31.5% improvement in
segment-level F-measure over Melisma"* (p. 10, 59 songs); *"an 8.8% improvement in event-level chord
accuracy and a 21.3% improvement in F-measure over HMPerceptron … a 5.4% improvement in event-level root
accuracy over HMPerceptron and a 8.2% improvement over Melisma … a 22.2% improvement in F-measure over
HMPerceptron and a 28.8% improvement over Melisma … p-value of 0.01"* (p. 10, 51 songs).

### The error analyses, in the authors' words (pp. 8–11)

**★ [FACT, p. 8 §6.1.1] On BaCh, the annotation itself is named as a source of disagreement, and
multi-annotator adjudication as the remedy.** *"Error analysis revealed wrong predictions being made on
chords that contained dissonances that spanned the duration of the entire segment (e.g. a second above
the root of the annotated chord), likely due to an insufficient number of such examples during training.
Manual inspection also revealed a non-trivial number of cases in which we disagreed with the manually
annotated chords, e.g. some chord labels were clear mistakes, as they did not contain any of the notes in
the chord. This further illustrates the necessity of building music analysis datasets that are annotated
by multiple experts, with adjudication steps akin to the ones followed by TAVERN."*

**★ [FACT, p. 8–9 §6.2.1, Figures 4–5] On TAVERN, the segment-level features are credited for
segments whose FIRST event lacks the root.** *"Error analysis on TAVERN revealed many segments where the
first event did not contain the root of the chord … For such segments, HMPerceptron incorrectly assigned
chord labels whose root matched the bass of this first event. Since a single wrongly labeled event
invalidates the entire segment, this can explain the larger discrepancy between the event-level accuracy
and the segment-level performance. In contrast, semi-CRF assigned the correct labels in these cases,
likely due to its ability to exploit context through segment-level features, such as the chord root
coverage feature f₄ and its duration-weighted version f₁₁."* Figure 4 (Mozart K025 m. 55): semi-CRF
A:maj7, HMPerceptron C♯:dim; Figure 5 (Mozart K179 m. 280): semi-CRF C:maj for the whole bar,
HMPerceptron E:min then C:maj.

**★ [FACT, p. 10–11 §6.4.1, Figure 6] On Rock, two failure classes both systems share, and one
figuration success credited to segment information.** Roots *"appearing in the first few repetitions"*
of a repeated pattern *"but disappearing later on"* — *"Due to their inability to exploit larger scale
patterns, neither system could predict the correct label for such segments."* Blues-influenced songs
with *"the major third … purposefully swapped for a minor third"* — *"again both systems struggled"*.
And Figure 6 ('Let It Be' mm. 14–15): *"Semi-CRF most likely predicts the correct label because of its
ability to heuristically detect figuration: the E5 on the first beat of measure 15 is a suspension,
while the E5 on the fourth beat is a neighboring tone. It would be difficult for an event-based approach
to recognize these notes as nonharmonic tones, as detecting figuration requires segment information."*
(p. 11.)

### Related and future work (pp. 11–12, §7–§8)

**[FACT, p. 11 §7] The authors' own two-axis placement of the four systems.** *"1. Are the weights
learned from the data, or prespecified by an expert? HMPerceptron and semi-CRF train their parameters,
whereas Melisma and HarmAn have parameters that are predefined manually. 2. Is chord recognition done as
a joint segmentation and labeling of the input, or as a labeling of event sequences? HarmAn and semi-CRF
are in the segment-based labeling category, whereas Melisma and HMPerceptron are event-based."* And:
*"The dynamic programming algorithm used in Melisma is actually an instantiation of the same general
Viterbi algorithm … HarmAn, on the other hand, uses the Relaxation algorithm … whose original quadratic
complexity is reduced to linear through a greedy approximation."* (p. 11.) Feature correspondences
stated: Melisma's compatibility rule ↔ coverage features; HarmAn's positive evidence and HMPerceptron's
asserted-notes ↔ coverage; HarmAn's negative evidence ↔ purity; Melisma's ornamental dissonance rule ↔
the figuration heuristics (p. 11).

**[FACT, p. 12 §8] Future work: segmental RNNs (Kong et al. 2016) to learn the features; and JOINT
models of interdependent analysis tasks.** *"Music analysis tasks are mutually dependent on each other.
Voice separation and chord recognition, for example, have interdependencies, such as figuration notes
belonging to the same voice as their anchor notes. Temperley and Sleator (1999) note that harmonic
analysis, in particular chord changes, can benefit meter modeling, whereas knowledge of meter is deemed
crucial for chord recognition. This 'serious chicken-and-egg problem' can be addressed by modeling the
interdependent tasks together, for which probabilistic graphical models are a natural choice.
Correspondingly, we plan to develop models that jointly solve multiple music analysis tasks."* Code:
*"made publicly available on the first author's GitHub"* (p. 12, note 7).

**[THEORY, as the paper cites it]** Sarawagi & Cohen 2004 (row 11) for the semi-CRF; Lafferty et al.
2001 (row 12) for the linear CRF; Muis & Lu 2016 for the weak semi-CRF; Kschischang et al. 2001 for factor
graphs; Pardo & Birmingham 2002 (row 4) for partition points and HarmAn; Radicioni & Esposito 2010 for
events, the BaCh corpus and HMPerceptron; Temperley & Sleator 1999 (row 7) for Melisma; Aldwell,
Schachter & Cadwallader 2011 for the chord types and the accent claim; Devaney et al. 2015 (row 53) for
TAVERN. Carried as citations only.

## Measured results, as the paper states them (summary; the full tables are above)

| Corpus | Protocol | Semi-CRF, full chord (Acc_E / F_S) | Comparator, full chord | Semi-CRF, root only (Acc_E / F_S) | Comparators, root only |
|---|---|---|---|---|---|
| BaCh, 60 chorales | 10-fold, repeated 10× | 83.2 / 77.5 | HMPerceptron₁ 77.2 / 69.9 | 88.9 / 84.2 | HMPerceptron 84.8 / 77.0; Melisma 84.3 / 74.7 |
| BaCh, one random fold set | accent ablation | with 83.6 / 77.6; without 77.7 / 71.2 | — | — | — |
| TAVERN, 27 sets | one fixed split (10 test sets) | 78.0 / 64.0 | HMPerceptron 57.0 / 22.5 | 86.0 / 71.4 | HMPerceptron 69.2 / 33.2; Melisma 76.7 / 41.5 |
| KP, 46 excerpts | 11 folds | 73.4 / 54.3 | — | 80.7 / 60.8 | Melisma 80.9 / 61.9 |
| KP, 36 excerpts | leave-one-out | 73.0 / 53.0 | HMPerceptron 72.9 / 45.4 | 79.3 / 59.0 | HMPerceptron 79.0 / 51.9; Melisma 81.9 / 62.2 |
| Rock, 59 songs | 10 folds | 69.4 / 58.3 | — | 85.8 / 66.8 | Melisma 77.4 / 35.3 |
| Rock, 51 songs | 10 folds | 70.1 / 55.9 | HMPerceptron 61.3 / 34.6 | 86.1 / 65.1 | HMPerceptron 80.7 / 42.9; Melisma 77.9 / 36.3 |

**Held-out evaluation for every figure; the KP and Rock label-normalisation and omission rules stated;
no figure for modulation, key, inversion or seventh quality (none is decided); no ablation of any feature
family other than the accent family; L and λ unstated.**

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score as notes with onset, offset, pitch and metrical
position (MIDI, kern or MusicXML); the partition points (every onset and offset) and the events between
them, each note carrying a held-over flag; the notated meter, from which Music21's `beatStrength()`
supplies the accent value of every note and event; a maximum segment length L; and, for training, chord
labels with their boundaries. **It does not assume a key, a voice assignment, a spelling (the labels are
enharmonically collapsed; the notes' spelling is "immaterial"), or any prior segmentation.**

**What it HANDS downstream.** One labeled segmentation of the piece: segment boundaries at partition
points, and per segment ONE label of root (12, canonical per mode), mode (major/minor/diminished, or an
augmented-sixth or suspended/power type) and added note (none/4/6/7) — no inversion, no seventh quality
(both left to *"a simple post-processing step"*), no tonality, no degree, no chord-tone list (the
figuration heuristics are internal to the features and are not output), no rivals (Viterbi returns the
single best labeled segmentation) and no calibrated probability (the model is a normalised conditional
distribution, but no posterior is published or evaluated).

**Its own STATED SCOPE and limits.**
- **Domain:** symbolic music in four corpora — Bach chorales, Beethoven and Mozart piano variations,
  textbook excerpts of common-practice tonal music, and pop/rock piano arrangements; *"performs
  substantially better than previous approaches when trained on a sufficient number of labeled examples
  and remains competitive when the amount of training data is limited"* (Abstract).
- **Vocabulary:** 144 core labels plus 36 augmented-sixth and 48 suspended/power labels; the paper's own
  admission that the labels *"do not encode for function"*.
- **Granularity:** segments of consecutive events, boundaries only at partition points, length ≤ L.
- **Coupling:** segmentation and chord label decided TOGETHER; tonality ABSENT by design, with the
  authors' statement that key context *"could further improve chord recognition"*; the figuration
  decision INSIDE the scoring relative to the candidate label, by heuristics; the previous label reaches
  the current segment only through the bigram features (the weak semi-CRF).
- **Fitting:** discriminative (conditional likelihood), L2-regularised, L-BFGS; features pruned below
  five occurrences; held-out evaluation throughout; the weights of ALL features fitted (no counted
  tables frozen).
- **Complexity:** linear in the input length for a fixed L (p. 3); the number of parameters *"largely
  independent of the number of labels"* (p. 4).

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adopt or adapt (the machinery of DP-C's chosen "with"):** the semi-Markov Viterbi over labeled
  segmentations on the partition-point grid with a maximum segment length, exactly the shape DP-C
  chooses and §14.1 names; and the paper's own two-axis account of why it beats event-level tagging —
  segment-level features (purity, coverage, bass over the whole candidate span) and the invalidation of
  a whole segment by one wrong event.
- **Adapt (the evidence unit — the framework's L1 grid confirmed at a second primary):** partition
  points = every onset and offset, events between them, the held-over flag per pitch — the same
  construction the L1 charter's change points and the V8 [FACT] rest on (Pardo & Birmingham's term used
  by this paper too).
- **Adapt (segment-level feature families as candidate terms of L2's score):** purity (the share of the
  segment's notes that belong to the candidate chord), coverage (which chord tones sound at all, with
  duration and accent weights), bass (two definitions, first-event bass and lowest-in-segment), an
  added-note-longer-than-root guard, and the chord-change accent term; each discretised into bins so the
  fitted weight is per bin rather than linear.
- **Adapt or argue against (the chord-tone decision inside the decode — DP-D's shape, done by
  heuristic):** the four figuration rules and the figuration-controlled twins are a published instance
  of deciding the non-chord tone relative to the candidate label inside the joint decode; D-527 does the
  same thing by a per-tone EMISSION with melodic and metric covariates rather than by hand rules, and
  the paper's own words that the rules *"are only approximations"* are the argument for the emission
  form.
- **Must argue against:** NO tonality anywhere (DP-B's and DP-E's question is not asked; the authors
  themselves say key context would help — so the paper is a rival to L2's entangled decision by
  omission, not by an opposite choice); enharmonically collapsed labels and *"immaterial"* spelling (the
  framework's L0 bullet reads the spelling); a label set without inversion or seventh quality, left to
  post-processing (L2 publishes the chord over each span with its notes; D-526's degree-valued chord axis
  needs the tonality this paper lacks); the single-best output with no rivals (DP-K); a root-interval
  bigram as the only transition knowledge, which the authors themselves say conflates V–I with I–IV; and
  all weights fitted discriminatively with no frozen counted table (the opposite of D-525's staged fit —
  a published, measured, held-out instance of the alternative).

## ★ Findings, routed and not applied

**(1) IDENTITY: the held file is the arXiv:1810.10002v2 preprint (26 Oct 2018) with the TISMIR header
unfilled; the bibliography names TISMIR 2(1) 2019.** Title and authors match; venue, volume and year
printed on the held document do not; whether the published text differs is not establishable from what
is held. The same shape as row 3's finding (the held preprint of a journal article). Routed to the
bibliography reconciliation, with the tier precision that no licence line is printed on the held
document. No verdict.

**(2) V5 RE-VERIFIED at the object, with two precisions.** Table 5: F 77.6 with accent, 71.2 without —
6.4 points, *"about six points"* as `FRAMEWORK.md` lines 352–356 and 1686–1687 state. Precisions: the
measurement is on *"a random fold set"* of BaCh, not the repeated cross-validation of Table 3 (so its
with-accent value 77.6 is not Table 3's 77.5); the significance is asserted in prose with no p-value in
the table; and what was removed is *"all accent-based features"* — the chord-change accent feature f₃₆
AND every accent-weighted purity, coverage and bass feature — so the six points measure the accent
INFORMATION, not the one boundary-accent term. Nothing is owed to the [FACT] as written. Routed to the
findings surface's V5 row as a datum; no verdict.

**(3) V10's segmental gains RE-VERIFIED at the object, with one precision to `population.md`'s
attribution.** BaCh +7.6 chord-F (77.5 − 69.9, Table 3, vs HMPerceptron₁); TAVERN +38.2 root-F (71.4 −
33.2, Table 7, vs HMPerceptron) and +41.5 chord-F (64.0 − 22.5, Table 6); Rock +21.3 chord-F (55.9 − 34.6,
Table 14, **vs HMPerceptron**, 51 songs) and +31.5 root-F (66.8 − 35.3, Table 13, **vs Melisma**, 59
songs). The framework's DP-C sentence — *"7.6 to 38.2 points … on one corpus and 21.3 to 31.5 on
another"* — has its values at the object, with the already-recorded wording imprecision (two corpora
compressed into "one"); the precision added here is that `population.md` line 111 reads *"Rock +21.3
chord-F and +31.5 root-F vs Melisma"*, where the 21.3 is against HMPerceptron (Melisma has no full-chord
evaluation in the paper) and the 31.5 against Melisma, on different song counts (51 and 59). Both
comparators are event-level systems by the authors' own classification (p. 11), so the framework's
*"event-level tagging"* holds for both. Routed to the findings surface's V10 row and to `population.md`
§3 as a precision; no verdict.

**(4) The candidacy row's reason CONFIRMED, with one precision of a NEW shape for the slice.** *"The
machinery of DP-C's chosen answer"*: yes — segmentation and label decided together, at the object, on
our repertoire's kind of input. The precision: **the method decides NO tonality**, by the authors'
stated design choice, and they say themselves that key context would improve it. So on L2's entangled
decision (tonality, boundary, chord tones, chord — one decision) the paper answers the boundary–chord
half and is SILENT on the tonality half — neither DP-B's rival (tonality first) nor the chosen point
(tonality with the chords), but tonality absent. It is the mirror of group 1's four rival-shape members
(rows 26, 29, 30, 5), which decided tonality alone and no chord. The ADMITTED verdict and the group 2
placement stand; recorded so the paper is not later read as evidence for or against DP-B or DP-E, on
which it is silent by construction. Shown, not ratified.

**(5) A published instance of DP-D's chosen SHAPE done by hand rules, with the authors' own caveat.**
The chord-tone/figuration question is answered inside the joint decode, relative to the candidate label
(Appendix B, the figuration-controlled features), and the authors call the rules *"only
approximations"*; the Rock error analysis credits exactly this mechanism for a correct suspension and
neighbor reading (Figure 6). D-527 places the same decision inside the decode as a fitted per-tone
emission. ENRICHES-shaped for DP-D's chosen point (the decision belongs inside L2's one decision) and a
datum beside D-527 on HOW (rules versus emission). Routed to the findings surface's DP-D block and to
L2's detail specification; no verdict.

**(6) The partition-point grid at a second symbolic primary.** Onsets and offsets as the only admissible
boundaries, events between them, a held-over flag per pitch — the L1 charter's change-point construction
and the V8 [FACT] have a second published instance here, with Pardo & Birmingham's own term. Nothing is
owed; routed to the findings surface's V8 row as a datum.

**(7) A measured, held-out instance of the OPPOSITE of D-525's staged fit.** Every feature weight is
fitted discriminatively by conditional likelihood with L2 regularisation; no table is counted from ground
truth and frozen; the result beats a perceptron-trained HMM on three corpora and is competitive on the
smallest. This is neither for nor against D-525 — the paper fits no emission table at all — but it is the
published shape an L2 detail specification designing its fit must argue against, beside DP-P's
fit-to-the-metric question (the paper fits likelihood, not the metric). Routed to L2's detail
specification beside D-525 and DP-P; no verdict.

**(8) Segment-level F-measure with boundary-AND-label correctness — a measurement convention.** *"a
predicted segment is considered correct if and only if both its boundaries and its label match"*: a
strict boundary-placement metric, beside event accuracy, both reported. A datum for measurement design
beside D-606 (modulation correctness, not agreement percentage) and the robust unit (boundary-invariant
by construction): the paper's convention is the boundary-SENSITIVE one, and the paper's own TAVERN
analysis shows how much the two can diverge (78.0 event accuracy against 64.0 segment F). Routed to
measurement design; no verdict.

**(9) The annotation named as an error source and multi-annotator adjudication as the remedy, at a
fourth primary.** *"a non-trivial number of cases in which we disagreed with the manually annotated
chords … This further illustrates the necessity of building music analysis datasets that are annotated
by multiple experts, with adjudication steps"*; and the TAVERN protocol's own adjudicated second
annotation used for only some pieces. Routed to measurement design beside principle #21, D-474 and
OI-179, as the record already carries rows 37's, 38's and 39's; no verdict.

**(10) The authors' own statement of the modulation/tonicization placement difficulty, as the reason
for leaving the key out.** *"Key changes occur gradually … locating modulations and tonicizations
difficult and also hard to evaluate."* A datum beside D-211, D-656 and DP-E's chosen point (a tonality
change located at a harmonic boundary) — the one paper in the slice that declines to decide the tonality
gives this as its reason. Routed to the findings surface's DP-E block; no verdict.

**(11) The accent source matters less than the accent USE, on the paper's own side-measurement.**
HMPerceptron with Melisma accent 70.2 F against 70.3 with Music21 accent — no difference — where semi-CRF
loses 6.4 with accent removed; the authors attribute the difference to HMPerceptron's binary use of the
accent. A datum for the L1 charter's metric-strength term: what earns the six points is a graded accent
value read by segment-level features, not the presence of an accent bit. Routed to the findings surface's
L1 block beside V5; no verdict.

**(12) Two failure classes both systems share, in the authors' words: a root that sounds only in the
first repetitions of a pattern, and a blues-swapped third.** *"Due to their inability to exploit larger
scale patterns"* — a bounded-context finding on the chord axis; and a genre-idiom finding for the style
system. Routed to L2's detail specification (the first) and to the style system (the second); no
verdict.

**(13) The label set's OMISSIONS — inversion and seventh quality — left to post-processing.** A
publication-surface datum: the paper's chord label is coarser than what L2 publishes, and the paper
states the two are recoverable from the notes and the bass after the decode. Routed to L2's detail
specification beside D-526 (the derived chord symbol) and D-536 (LEGACY, bass and chord chosen together);
no verdict.

**(14) No falsifier.** Nothing read contradicts any CHOSEN design point. Both ratified [FACT]s resting
on this paper (V5, and DP-C's segmental gains) are re-verified at the object. The paper's silence on
tonality is a bound on what it can be cited for, not a contradiction of DP-B or DP-E. **No STOP fires**
under the remedial commission's §5.

## Centrality

**CENTRAL, on two grounds, challengeable at the progress record.** First, **ratified text rests on it
at two places**: the L1 charter's metric-strength [FACT] (V5) and DP-C's segmental-gains [FACT] (part of
V10), both re-verified here — the original commission's §4 makes a paper *"whose claims would carry load
in a detail specification or against a design point"* central, and this paper's claims already carry
load in a chosen design point's ground. Second, **it is the published machinery of DP-C's chosen
answer on symbolic input**: the semi-Markov decode over labeled segmentations on the partition-point
grid with segment-level features, which §14.1 names as what the framework builds on; an L2 detail
specification adopting or adapting that machinery cites this paper for it (Sarawagi & Cohen, row 11,
supplies the formalism; this paper supplies the musical features and the measured instance). **The
ground on which NOT CENTRAL could be argued, stated so the challenge is easy to make:** both figures the
record rests on were already read at the object by the pass (`population.md` §3, V5 and V10 "VERIFIED"),
so this whole-paper read adds precisions and no new verification; the formalism's primary (row 11) is
held and is next in the order; and the paper decides no tonality, so it cannot carry load on the half
of L2's decision the charter calls entangled. **A second independent extraction is therefore OWED** on
this verdict.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`
and `cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (13) are routed and
written nowhere else. It does not fetch the TISMIR 2(1) 2019 published version, the first author's
code, Muis & Lu 2016, Radicioni & Esposito 2010, or the BaCh, TAVERN, KP or Rock data. It opens no
code, touches no measurement tool, no corpus, no golden and nothing under `tools/`. It writes no
open-items row and allocates no decisions-register identity. It reads no other paper and takes no
decision about the order of the remaining slice.

---

*Provenance: written 2026-09-06 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_twenty_one.md`, on the user's opening instruction naming row 10,
after the ordinary session-start read (`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived
gating answer). Read for this extract, at the files: `reading_pass/candidacy_upgrades.md` whole (row 10
at line 72), `cowork_l2_task_b_slice_derivation_2026_09_05.md` whole (row 10 at line 57),
`docs/research_papers/BIBLIOGRAPHY.md` at line 24, `FRAMEWORK.md` at lines 340–364 (the L1 charter's
grid and metric-strength paragraphs), 685–714 (DP-B to DP-E), 1000–1019 (§14.1), 1590–1601 (§S4(d)),
1680–1689 and 1798–1809 (the sealed first-stage text), located by a `Grep` of the staged file for the
authors' names, "segmental", "semi-CRF", "semi-Markov" and "accent"; the findings surface at lines
140–189 (DP-B and DP-C blocks) and 598–630 (the verification table); `reading_pass/population.md` at
lines 95–120 (§3, the load-bearing table); the progress record whole; both commissions whole; and the
row 5 extract whole, for the form. The paper itself was read at the object as page images, all nineteen
pages. No shell command was run on the repository or on any staged copy of it for content or for
listings, with one declared exception recorded in the handoff entry (a Python read of the harness-saved
directory-listing tool result, to locate two file names). No figure of this project's own measurement is
restated (#17f, D-431); every value above is the paper's own.*

# EXTRACT — Ju, Margot, McKay, Dahn & Fujinaga 2020, "Automatic Figured Bass Annotation Using the New Bach Chorales Figured Bass Dataset" — Task B candidacy row 36, first pass, AT THE OBJECT



## Identity

Yaolong Ju, Sylvain Margot, Cory McKay, Luke Dahn & Ichiro Fujinaga, "Automatic Figured Bass Annotation
Using the New Bach Chorales Figured Bass Dataset", *Proceedings of the 21st International Society for
Music Information Retrieval Conference (ISMIR 2020)*, Montréal, pp. 640–646. Schulich School of Music,
McGill University; Department of Liberal and Creative Arts, Marianopolis College; School of Music, The
University of Utah. CC BY 4.0 (640).



## Claims, labeled

### What the paper contributes, in its own list (§1, 640)

**[FACT, §1]** Four contributions: (1) the Bach Chorales Figured Bass dataset (BCFB), *"139 chorales
composed by Johann Sebastian Bach"* drawn from the cantatas, passions, motets and the Christmas
Oratorio; (2) the digitization method; (3) *"a comparative study of automatic figured bass annotations
of BCFB, using both rule-based and machine learning approaches"*; (4) applications of figured bass
annotation, *"especially in connection with converting figured bass to chord labels"*.

**[FACT, §1]** The state of the field as the authors found it: two earlier papers on automatic figured
bass, both rule-based — Barthélemy and Bonardi, who *"treated figured bass as a harmonic reduction and
devised rules to identify and remove ornamental notes, permitting them to cluster the remaining chord
tones as figures"*, and Wead and Knopke, who *"manually designed a decision tree to determine the
figured bass for a given bass line"* — with *"no open-source code and a lack of quantitative results"*.
*"we are not aware of any previous applications of machine learning to figured bass, nor of any existing
digital dataset with figured bass annotations"* (640).

### The dataset (§2, 641–642)

**[FACT, §2]** 139 four-voice chorales *"that include his own figured bass, based on the Neue Bach
Ausgabe (NBA) critical edition"*, encoded in MusicXML, \*\*kern and MEI. A reference table of all 420
chorales attributed to Bach was cross-referenced with the NBA to find the 139 (§2.1).

**[FACT, §2.2]** 109 of the 139 came from existing \*\*kern encodings in the KernScores repository,
converted to MusicXML with music21 (v. 5.1.0) and corrected to match the NBA; the remaining 30 were
entered by hand. MusicXML is the master format; editing in MuseScore 3. Changes to match the NBA
included *"adding a continuo line and/or instrumental voices; transposing; changing the meter, pitch,
and duration of certain notes; etc."* (footnote 5).

**[FACT, §2.3]** Conversion to the other formats: MusicXML to \*\*kern with *musicxml2hum*, *"except for
the continuation lines"*; \*\*kern to MEI with Verovio. Direct MusicXML-to-MEI conversion lost
accidentals, slashes and continuation lines, so continuation lines were added to the \*\*kern files by
hand before converting to MEI (641–642).

### The task and the evaluation metric (§3, 642–643)

**[FACT, §3, footnote 12]** *"The generated FBAs use flats and sharps to respectively indicate lowered
and raised intervals, and do not contain continuation lines."* (FBA is the paper's abbreviation for
figured bass annotation.)

**[FACT, §3.1]** 120 of the 139 chorales were used to train and test. Excluded: 12 chorales with
*"elaborate instrumental interludes between phrases"*, five *"that are barely figured"*, and BWV 8.06 and
BWV 161.06 *"because they feature irregular textures, such as having an obbligato continuo and/or
instrumental part"* (642).

**★ [FACT, §3.2.1] The unit of analysis is the note-onset slice.** *"First, the music is segmented into
a series of note onset slices [8,9]. A new slice is formed whenever a new note onset occurs in any musical
voice, and each slice consists of the vertical set of notes sounding at that moment."* A note held from
an earlier slice belongs to the later slice's sounding set (the 3.3.2 example marks notes as "held").
The paper's *sonority* is *"the set of pitch classes present in a note onset slice"* (footnote 19).

**[FACT, §3.2.1]** The simple rule-based algorithm labels every interval above the bass. Its exact match
with Bach's figures: *"the percentage of exact matches was only 3%"* — *"partly because Bach did not
explicitly label all the intervals above the bass in his FBAs"* (642).

**[FACT, §3.2.2]** The evaluation metric treats musically equivalent figures as equivalent. The rules,
*"inspired by Arnold [11]"*:
- a "3" can be omitted *"unless there is a 4th in the sonority, or unless the 3rd is the resolution of a
  4–3 suspension"*;
- a "5" can be omitted unless there is a 6th in the sonority, the 5th resolves a 6–5 suspension, or the
  5th has an accidental;
- an "8" can be omitted unless there is a 9th in the sonority, the 8th resolves a 9–8 suspension, or the
  8th has an accidental;
- a "6" can be omitted *"if the sonority forms a "6/4/3" or a "6/4/2" chord"* (642).

**[FACT, §3.2.3]** Under that metric the simple algorithm agrees with Bach's figures at **64.5%** (643).

**[FACT, §3.2.3]** The improved rule-based algorithm adds two rules: (1) omit the figure for an
upper-voice note if *"the note is labelled in the previous slice"* and *"the pitch class of the bass in
the current slice remains the same as in the previous slice"*; (2) on fractional beats, look for
*"ornamental notes, such as passing tones, neighbour tones, escape tones, and anticipations, which are
all approached or departed by step. If such a note is in an upper voice, its corresponding number is
removed from the figure; if such a note is in the bass, the slice is left entirely unfigured"* (643).
With these, **85.3%** agreement (643).

**★ [FACT, footnote 20] The rules were chosen on the data they are graded on.** *"The rules were
proposed by observing the generated FBAs and were evaluated against the ground truth FBAs from BCFB. We
selected the rules that yielded higher accuracy."* No held-out split is stated for the rule-based
results in the pages as read.

**[FACT, §3.2.3]** The authors stopped adding rules: *"none were readily obvious from the perspective of
music theory or performance practice, and we wanted to avoid overfitting our rules"* (643).

### The machine-learning method (§3.3, 643–644)

**[FACT, §3.3.1]** Each figure is converted to a 12-element interval-class vector *"that includes all
the notes above the bass that are sounding in the current slice"*. The interval class is ORDERED, from
the bass to the upper voice, ranging 0 to 11 (footnote 21). Where a figure does not specify the exact
interval (a "6" could be major or minor), *"we rely on the score to determine the exact interval using
heuristics-based post-processing"*; the score's pitch spelling is likewise used to convert vectors back
to figures (e.g. 3 semitones as "♭3" or "♯2"; "2" versus "9" decided by finding the actual note above the
bass and comparing its pitch with the bass's: *"If they are one octave apart, the generated figure will
be "9", and "2" otherwise"*, footnote 22).

**[FACT, §3.3.2]** Input per slice: three binary vectors — interval classes (12), onsets (12: which notes
above the bass have onsets in this slice rather than being held), metrical context (3: downbeat, another
beat, or a fractional beat) — 27 dimensions; with the previous and following slices concatenated
(zero-padded at the ends), 81 dimensions (644).

**[FACT, §3.3.3]** Decision trees (scikit-learn `DecisionTreeClassifier`, default settings, *"an
optimized version of CART"*, footnote 24) and a feedforward network of three hidden layers of 300 units,
Adam, binary cross-entropy, hyper-parameters tuned on the validation set (footnote 25). Output: a
12-dimensional binary vector of the semitones above the bass that are figured (644).

**[FACT, §3.3.4]** Ten-fold cross-validation. Network: 80% training, 10% validation (also used for early
stopping, footnote 27), 10% test. Trees: 90% training, 10% test, *"matching the DNN test sets"* (644).
**What a fold is cut by — chorale or slice — is not stated in the pages as read.**

**[FACT, §3.3.5]** *"The Decision Trees and Deep Neural Networks respectively achieved classification
accuracies of 84.3±0.5% and 85.9±0.6% on BCFB."* The ± is *"standard error across cross-validation
folds"* (footnote 28). The accuracies are *"calculated based on the evaluation metrics proposed in
Section 3.2.2"* (644).

**What the accuracy counts is not defined in the pages as read** — per slice is the natural reading of
a per-slice classifier, but no sentence states the unit. *(CONJECTURE, not carried.)*

### The discussion (§4, 644–645)

**[FACT, §4]** One common error: missing *"figures that indicate the resolution of a suspension, such as
the 9–8 shown in Fig. 4(a), m. 8.4. This may be because the features we used did not contain sufficient
voice-leading information to detect such suspensions."*

**[FACT, §4]** Two disagreements the authors judge *"theoretically acceptable"*: a generated "♯" at BWV
145.05 m. 2.3 where Bach wrote none (the D is sharpened in the soprano), and a generated "♯7" at m. 3.2
(644).

**[FACT, §4]** Bach's own inconsistency, three kinds: accidentals (the first "♯" unlabelled at m. 2.3, the
second labelled at m. 3.3), suspensions (*"sometimes labelled … and sometimes omitted them"*), and the
same chord labelled sometimes 4/2 and sometimes 6/4/2. *"So, one cannot expect 100% agreement to be
achievable, given such variability. Bach, like everyone, was sometimes inconsistent with himself, which
imposes an artificial performance ceiling on our models [12]."* (644)

**[FACT, Fig. 4 caption, 645]** The best-performing model's figures are produced by predicting interval
classes and generating the figure *"based on the intervals between the bass note and each predicted
interval class"*.

### The conclusion (§5, 645)

**[FACT, §5]** *"our models achieved classification accuracies of 85.3% and 85.9% on BCFB,
respectively. A potential reason the machine learning models did not outperform the rule-based model may
be the relatively small size of BCFB."*

**★ [FACT, §5] The direction the authors propose for harmonic analysis.** Existing methods *"tend to
either identify chords directly from the music [13–15], or identify and remove non-chord tones from the
score and then generate chord labels from the remaining chord tones [16,17]. A new approach would be to
first generate figured bass automatically from the music and then convert the figures to chord labels;
this would allow a chord classifier to take advantage of knowledge implicitly learned from Bach's ground
truth FBAs by a figured bass annotator during its training."* **[CONJECTURE — the authors' proposal; no
such system is built or measured in the paper.]**

**[FACT, §5]** Named refinements: add voice-leading information; improve the rule-based model by
analysing the trained decision trees; add figured bass from other Bach works and other Baroque composers.

## Measured results, as the paper states them

| Method | Metric | Value | Where |
|---|---|---|---|
| Simple rule-based (every interval above the bass) | exact match with Bach's figures | **3%** | §3.2.1, 642 |
| Simple rule-based | equivalence metric of §3.2.2 | **64.5%** | §3.2.3, 643 |
| Improved rule-based (two added rules; rules selected on BCFB itself, footnote 20) | equivalence metric | **85.3%** | §3.2.3, 643; §5 |
| Decision trees, ten-fold cross-validation | equivalence metric | **84.3 ± 0.5%** (standard error across folds) | §3.3.5, 644 |
| Feedforward network, ten-fold cross-validation | equivalence metric | **85.9 ± 0.6%** | §3.3.5, 644 |

Corpus for all rows: BCFB, 120 of its 139 chorales (§3.1). Ground truth: Bach's own figures as printed in
the NBA.

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score of **four-voice, largely homorhythmic
chorales** with **separated voices and an identified bass** (rule (1) and the ornamental-note rule both
need to know which voice a note is in and whether it moves by step); **note-onset slices** with each
note marked as struck or held (§3.3.2); **metrical position** at three levels — downbeat, other beat,
fractional beat; and the score's **pitch spelling**, used to turn interval classes back into figures with
the right accidentals and the right number (§3.3.1). It assumes **no key, no chord, no root and no
segmentation into chords**. Everything it reads is in the notated score.

**What it HANDS downstream.** For each note-onset slice, a **set of intervals above the bass** — the
predicted interval classes — rendered as figures with flats and sharps for lowered and raised intervals
and **no continuation lines** (footnote 12). A slice can be left unfigured. It hands on **no chord, no
root, no quality, no key and no inversion as a label**; the figures are intervals above the bass, and
the figure follows what Bach wrote, which includes suspension figures (4–3, 9–8) and omits ornamental
notes.

**Its own STATED SCOPE and limits.** Bach's four-voice chorales with Bach's own figures; 120 chorales
after exclusions; the authors name the dataset's small size as a possible reason the machine-learning
models did not beat the rules (§5), name missing voice-leading features as the likely cause of missed
suspension figures (§4), and state that Bach's own inconsistency sets an artificial ceiling (§4).



# EXTRACT — Bigo, Feisthauer, Giraud & Levé 2018, "Relevance of Musical Features for Cadence Detection" — Task B candidacy row 37, first pass, AT THE OBJECT



## Identity

Louis Bigo, Laurent Feisthauer, Mathieu Giraud & Florence Levé, "Relevance of Musical Features for
Cadence Detection", *Proceedings of the 19th International Society for Music Information Retrieval
Conference (ISMIR 2018)*, Paris, pp. 355–361. CRIStAL UMR 9189, CNRS, Université de Lille; MIS,
Université de Picardie Jules Verne. CC BY 4.0.



## Claims, labeled

### ★ The two exclusions

**[FACT, §1.3]** *"The proposed strategy avoids chord segmentation, which is itself a difficult MIR
problem."* And **[FACT, §2]**: *"We therefore do not start from a complete harmony analysis nor a chord
segmentation, that can be error-prone. Even when the methods finding Y(Z) and X(Z) return approximate
onsets, the computed features may be relevant."*

**★ [FACT, §2.1]** *"we do not perform tonality estimation … because of the usual difficulty of
algorithms to disambiguate adjacent tonalities in the circle of fifths."* **The features reach for
tonality only as a hypothesis anchored on the bass of the arrival chord, never as a decided key.**

### What the method is

**[FACT, abstract, §2]** **44 binary, musical, local cadential features**, computed at **each beat** of
the score, turning cadence detection into a per-beat classification task. Features describe three
onsets: **Z**, the candidate arrival beat; **Y**, the chord preceding it; and **X**, the cadence
preparation.

**[FACT, §2.3]** Y is found heuristically: *"the latest beat preceding Z for which the bass voice
includes a sounding note, limited to one measure in the past."* Beat resolution for the search depends
on the corpus — quarter note for Haydn, eighth for Bach, *"to cope with the faster harmonic rhythm"*
(Figure 3).

**[FACT, §2.4]** X is *"the latest beat before Y whose lowest sounding note has a different pitch
(modulo octave) than the lowest note of Y."*

**★ [FACT, §2.1]** *"Z-bass-compatible-with-I (resp.
Z-bass-compatible-with-V): Both notes 4 and 7 of the tonality that would be implied if the bass of Z is I
(resp. V) are present in the four beats before Z"* (357). A companion feature, `Z-bass-compatible-with-I-scale`, asks whether
*"The 8 previous beats exhibits the whole scale of the same implied tonality."*

**[FACT, §2.1–2.4]** The other feature families, in the paper's own groupings: chord constitution at Z
(perfect triad, sus4, highest note is the tonic or the third); **voice-leading** features
`Z-β-comes-from-α` and `Z-α-moves-to-β` (an immediate resolution of one degree to another); **rhythmic
and break** features `R-Z-strong-beat`, `R-Z-same-rhythm`, `R-Z-sustained-note`, `R-after-Z-rest-*`;
features on Y (`Y-has-7`, `Y-in-V7`, `Y-Z-bass-moves-compatible-V-I`, `Y-Z-bass-same-voice`); and on X
(`X-Y-bass-moves-2nd-min`, `-2nd-Maj`, `-4th`).

**[FACT, §3]** A linear **SVM**, with **leave-one-piece-out** cross-validation for hyper-parameters —
chosen deliberately: *"the traditional Leave-One-Out (LOO) cross-validation approach that would consist
in leaving only one beat of one piece out of the training set would result here in overfitting due to
intra-piece musical repetitions."* Classes are unbalanced (about 98% non-cadential), so cadential beats
are weighted more heavily. *k*-nearest-neighbour and decision trees *"turned out to provide comparable
or inferior results."*

## Measured results, as the paper states them

**Corpora (Table 1).** `bach-wtc-i`: 24 fugues of the Well-Tempered Clavier book I, 2 to 5 voices, 4739
beats, PAC 63 (23 final), rIAC 24, HC (5). `haydn-quartets`: 42 expositions from Haydn string quartet
movements in sonata form, 4 voices, 7173 beats, PAC 99 (21), rIAC (8), HC 70. *"Cadences are labeled at
about 2% of the beats."* Bach annotations from the authors' own earlier fugue work; Haydn annotations
from Sears and colleagues.

**Table 3 — detection on the test sets, all features:**

| Corpus | Target | beats | ref | TP | FP | FN | F₁ |
|---|---|---|---|---|---|---|---|
| haydn-quartets (21 quatuors) | PAC | 3583 | 51 | 42 | 28 | 9 | **0.69** |
| haydn-quartets | HC | 3583 | 32 | 18 | 73 | 14 | **0.29** |
| bach-wtc-i (12 fugues) | PAC | 2357 | 36 | 26 | 3 | 10 | **0.80** |
| bach-wtc-i | PAC+rIAC | 2357 | 46 | 30 | 12 | 16 | **0.68** |

**Table 4 — F₁ by feature subset** (haydn PAC / haydn HC / bach PAC / bach PAC+rIAC): all features XYZR
0.69 / 0.29 / 0.80 / 0.68; YZR 0.69 / 0.27 / 0.71 / 0.68; ZR 0.59 / 0.24 / 0.52 / 0.34; XYZ 0.72 / 0.25
/ 0.74 / 0.54.

**[FACT, §4.4]** *"The detection of PAC is good, with more than 75% PAC detected and a low false
positive rate (< 1%)."* And, recorded because it is the authors' own caution about an earlier number:
*"Note that we previously reported 82% of PAC detection in fugues [9] but with manual hard-coded rules
that may have resulted in overfitting."*


**★ [FACT, §4.2] The stated reason the half cadence is hard.**
*"We also notably lack strong significant features for HC. Indeed, the Y-Z bass move in a HC is variable
(it is typically similar to X-Y moves in PAC)."* **[FACT, §4.4]** *"The detection of HC is difficult
(Haydn corpus), as there is not a single feature applicable to every case. Half of them are detected,
with about 2% FP."*

**[FACT, §4.4]** Of 28 PAC false positives in Haydn, *"at least 5 FP can be seen as actual cadences"* —
the annotation itself is contestable at the margin.

**[FACT, §4.4]** The authors write: *"Rhythmic features (R) bring an improvement especially for HC, in
particular with R-Z-strong-beat that correctly filters out more than half of the beats."* Their Table 4
gives, from features XYZ to XYZR: Haydn HC 0.25 → 0.29, Haydn PAC 0.72 → 0.69, Bach PAC 0.74 → 0.80, Bach
PAC+rIAC 0.54 → 0.68.

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score with **voices** (files were voice-separated
`.krn`; *"the features proposed here could also apply to non-separated files, except for after-Z-rest-*
and Y-Z-bass-same-voice"*), **metric position** (`R-Z-strong-beat` needs to know which beats are strong
for the time signature), **a bass voice**, and **durations**. It assumes **no key**, **no chord
segmentation** and **no harmonic analysis**. Features are extracted with music21; classification with
scikit-learn.

**What it HANDS downstream.** A per-beat binary verdict — this beat is or is not the arrival point of a
cadence of the trained type (PAC, PAC+rIAC or HC) — and, in the
study itself, the per-feature significance
tallies of Table 2. It hands on **no chord, no key, no segmentation and no cadence type beyond the class
trained for.**

**Its own STATED SCOPE and limits.** Two corpora, Bach fugues and Haydn quartet expositions; the
annotations *"model cadences in the light of a global analysis of the form"* while the detection is
local, which the authors state as a known mismatch: *"we have used them as a benchmark on our local
feature-based detection."* The authors were *"expecting to find more suspensions for both PAC and HC"*,
which *"do not appear significantly in these corpora."* The conclusion names the shape of the fix: *"Cadence
preparations could for example be described by features regarding contiguous 'spans' of onsets rather
than single onsets X and Y, in order to improve the harmony relevance of the model. Research along these
lines could significantly improve HC detection."*



# EXTRACT — Karystinaios & Widmer 2022, "Cadence Detection in Symbolic Classical Music using Graph Neural Networks" — Task B candidacy row 38, first pass, AT THE OBJECT



## Identity

Emmanouil Karystinaios & Gerhard Widmer, "Cadence Detection in Symbolic Classical Music using Graph
Neural Networks", *Proceedings of the 23rd International Society for Music Information Retrieval
Conference (ISMIR 2022)*, Bengaluru. arXiv:2208.14819v1, 31 Aug 2022. Institute of Computational
Perception, Johannes Kepler University Linz; LIT AI Lab. CC BY 4.0.



## Claims, labeled

### What the method is

**[FACT, §1, §3]** Cadence detection is posed as **imbalanced node classification on a graph**. The
score becomes a *homogeneous* graph: every note **and every rest** is a node; three kinds of undirected
edge join them — `E_on` between notes sharing an onset, `E_cons` between consecutive notes, and `E_dur`
between a longer note and notes whose onsets fall during it.

**[FACT, §3.1]** **135 features per node**, in three categories: general note-wise features (onset in
score-relative beats, duration in beats, MIDI pitch, plus **global attributes such as time signature and
key signature assigned to each note** (the key signature: Figure 1's caption, p. 2), and interval vectors
with binary chord-type indicators);
graph-aware features (the first 20 eigenvectors of the Laplacian of the adjacency matrix); and
cadence-related note features *"similar to those in [4]"*


**★ [FACT, §3.1]** *"in contrast to
[4], we restrict these to only consider the immediate local context of a note instead of using positional
features relating to predefined past 'cadence anchor points'. In this way, we wish to demonstrate the
generality of our representation and learning approach, which will hopefully learn more long-distance
aspects automatically."* And: *"we do not use any information about events that occur on previous beats
… While these features are more restricted compared to [4] they are also more general, since we make no
assumptions on and reference to 'cadence anchor points' (e.g., the occurrence of the preceding subdominant
and dominant harmony), which in [4] are identified with specialized heuristics."*


**[FACT, §5]** The model is **Stochastic GraphSMOTE**: a GraphSAGE encoder, a SMOTE layer applied in the
encoder's *latent* space to force a 1:1 class balance per batch, a decoder generating edges for the
synthetic nodes, and a GraphSAGE classifier over the generated adjacency. The total loss is cross-entropy
plus a weighted edge-reconstruction loss.

**★ [FACT, §1, §6.1] Prediction granularity is a property of the representation, not of the task.** *"our
model can provide predictions at three different levels, note-wise, onset-wise and beat-wise predictions
(the latter two simply by aggregation)"*, whereas *"The reference model [4] can only classify at the beat
level."*


## Measured results, as the paper states them

**Corpora (Table 1).** Bach Fugues — 24 pieces, 24,567 nodes, 229,107 edges, PAC 237, rIAC 78, HC 15.
Haydn String Quartets — 45 pieces, 38,661 nodes, 441,491 edges, PAC 434, rIAC 24, HC 340. Mozart String
Quartets — 31 pieces, 68,190 nodes, 762,796 edges, PAC 1,089, HC 1,930. *"Cadence nodes constitute less
than 2% of all nodes."* Scores from kern.ccarh.org, parsed with partitura.

**Table 2 — half for training, half for testing; F₁ for the positive (cadence) class:**

| Dataset | Model | F₁ Note | F₁ Onset | F₁ Beat | Prec. Beat | Recall Beat |
|---|---|---|---|---|---|---|
| Bach Fugues (PAC) | Bigo et al. | – | – | **0.80** | **0.89** | 0.72 |
| | Stochastic GraphSMOTE | 0.85 | 0.75 | 0.73 | 0.70 | 0.77 |
| | Pretrained SGSMOTE | **0.90** | **0.83** | **0.80** | 0.74 | **0.89** |
| Bach Fugues (rIAC) | Bigo et al. | – | – | 0.68 | 0.71 | 0.65 |
| | Stochastic GraphSMOTE | **0.87** | **0.75** | **0.73** | **0.75** | 0.72 |
| | Pretrained SGSMOTE | 0.87 | 0.73 | 0.71 | 0.62 | **0.82** |
| Haydn String Quartets (PAC) | Bigo et al. | – | – | **0.69** | **0.60** | **0.82** |
| | Stochastic GraphSMOTE | 0.77 | 0.56 | 0.59 | 0.47 | 0.78 |
| | Pretrained SGSMOTE | **0.81** | **0.63** | 0.64 | 0.54 | 0.78 |
| Haydn String Quartets (HC) | Bigo et al. | – | – | 0.29 | 0.19 | **0.56** |
| | Stochastic GraphSMOTE | 0.65 | 0.32 | 0.30 | 0.33 | 0.27 |
| | Pretrained SGSMOTE | **0.69** | **0.44** | **0.41** | **0.41** | 0.41 |



**★ [FACT, §6.1] The authors' own summary of that table.** *"Our model matches or slightly surpasses the
state of the art in rIAC detection in Bach fugues and on HCs in Haydn string quartets but does not reach
the reference model's F1 results in PAC detection."* Pre-training on the other dataset *"is the price we
pay for the generality of the graph representation and the consequent size (number of parameters) of the
deep network."* And the comparison of error shapes: *"In the PAC detection tasks, in particular, we
observe comparable or higher recall of our model compared to the reference, but lower precision."*

**★ [FACT, §6.1] The agreement with [4] — a different method on shared data.** *"Generally, our results
agree with [4] in implying that half cadences (HC) seem significantly harder to identify than authentic
cadences, both perfect and imperfect."* The paper uses *"two datasets also used by Bigo et al. [4]"*
(p. 3) and *"the same data and train/test setup"* (p. 4).


**Table 3 — three-class classification (no cadence / PAC / rIAC or HC), 5-fold cross-validation, macro-averaged F₁**, comparing all features against *general* (excluding the cadence-specific engineered
category): Bach Fugues general 0.602 note / 0.667 beat against all 0.653 / 0.702; Haydn general 0.542 /
0.610 against all 0.648 / 0.663; Mozart general 0.584 / 0.569 against all 0.588 / 0.606. The authors'
reading: the engineered features help, *"However, also the general-purpose category 1 and 2 features
alone support non-trivial cadence recognition and discrimination performance, which implies that the
relational graph representation in combination with a convolutional approach manages to enrich highly
local features with relevant non-local score context."*

**Table 4 — neighbour-convolution depth on Bach PAC** (F₁ note / onset / beat): none 0.833 / 0.671 /
0.667; 1-hop 0.854 / 0.707 / 0.701; **2-hop 0.869 / 0.737 / 0.732**; 3-hop 0.836 / 0.706 / 0.659. *"Best
results are achieved when using a convolution depth of 2. Increasing the receptive field beyond that
level, we observed some instabilities emerging in the learning model, …"* — the page continues *"which
could be attributed to the common vanishing gradient problem in deep GCNs [22]"* (p. 6).


**[FACT, §6.2] The false positives are diagnosed, not just counted.** *"many false positive predictions
resemble cadences, in terms of tonal structure or implications, and could be considered and annotated as
such, but lack some main components."* One of the three worked cases is Haydn Op. 54 No. 1 II, mm. 33–45 (the
others: fugue no. 19 of WTC I at bar 23, and the passage of [4]'s Figure 4), where a
modulating melodic and harmonic sequence ends each statement with a cadential pattern: *"A harmonic
analysis of these bars indicates a proper PAC preparation with text-book voice leading on the cadence
arrival point in every occasion. These two false positive PACs form part of a modulating melodic and
harmonic sequence; whether to classify them as cadences is a matter of higher-level musicological
considerations."* And the stated boundary of the method: *"by design cannot consider high-level
musical considerations such as, e.g., whether PAC-like patterns that occur in sequence should count as
PACs or not."*


## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A parsed symbolic score giving, per note and per rest, onset in
score-relative beats, duration in beats and MIDI pitch, **plus the time signature and the key signature
as global attributes attached to every node**. Notes and rests both. No chord segmentation, harmonic
analysis or decided tonality is described in the pages as read — **but the key signature is used as a
feature**.


**What it HANDS downstream.** A cadence label per **note**, and by aggregation per onset and per beat —
binary in the first experiment, three-class in the second. No chord, key or segmentation is described as
an output; the classifier's softmax values, which the page calls *"the predicted class probabilities"*
(p. 4), are not said to be published.

**Its own STATED SCOPE and limits.** Baroque and Classical cadences, three corpora, focused on PAC with
rIAC and HC *"where our annotated datasets permit"*. The Bach HC count is 15 and the Haydn rIAC count 24,
and the paper says in a footnote that it ignores *"the HC in Bach and rIAC in Haydn, because of their low
numbers."* The best beat-wise figures in three of Table 2's four blocks are the model's pre-trained on the
other dataset; in the Bach rIAC block they are the model's without pre-training. Convolution beyond 2-hop
destabilises. By design the method *"cannot consider high-level musical considerations such as, e.g.,
whether PAC-like patterns that occur in sequence should count as PACs or not"* (p. 6).




# EXTRACT — Sears, Pearce, Caplin & McAdams 2018, "Simulating melodic and harmonic expectations for tonal cadences using probabilistic models" — Task B candidacy row 39, first pass, AT THE OBJECT



## Identity

David R. W. Sears, Marcus T. Pearce, William E. Caplin & Stephen McAdams, "Simulating melodic and
harmonic expectations for tonal cadences using probabilistic models", *Journal of New Music Research*,
DOI 10.1080/09298215.2017.1367010. McGill University; Queen Mary University of London. **The held file
is the journal's online version: its pages are numbered 1–24, the first page's header reads
*"JOURNAL OF NEW MUSIC RESEARCH, 2017"*, and no volume, issue or print page range is printed on it; the
date 22 November 2017 on its margin is a download stamp (*"Downloaded by [Queen Mary University of
London] at 02:52 22 November 2017"*), not a publication date.**



## Claims, labeled

### What the method is

**[FACT, abstract, §1]** The model is **IDyOM** — a finite-context (*n*-gram) model that predicts the
next event in a musical stimulus by unsupervised statistical learning of sequential structure — applied
to the terminal melodic and harmonic events of **245 exemplars** of the five most common cadence
categories in the classical style.

**[FACT, §3, §5.2]** Events are represented in Conklin's **multiple viewpoints** framework. The melodic
viewpoints are chromatic pitch (`cpitch`), melodic interval (`melint`), chromatic scale degree (`csd`)
and an optimised combination (`selection`); the harmonic ones are vertical interval class combination
(`vintcc`) and chromatic scale-degree combination (`csdc`), the latter *"intended to approximate Roman
numerals"*; and `composite` is the joint probability of the melodic and harmonic models.

**[FACT, §4]** Probabilities come from maximum-likelihood *n*-gram counts smoothed by **Prediction by
Partial Match**, in the variable-order **PPM\*** variant with interpolated smoothing and Moffat's escape
method C. The reported quantity is **information content**, IC = log₂(1/p), in bits.

**[FACT, §5.3]** Only the **long-term model** (LTM+) is used: *"the STM should be irrelevant for the
present purposes, since cadences exemplify the kinds of inter-opus patterns that listeners are likely to
store in long-term memory."*

**[FACT, §5.4]** Evaluation is **10-fold cross-validation**, the corpus serving as both training and
test set.

### Its own preprocessing, recorded because it bounds what the figures mean

**[FACT, §5.1]** *"To ensure that each instrumental part would qualify as monophonic … all trills,
extended string techniques, and other ornaments were removed."* Double and triple stops were reduced to
the note events preserving the voice leading. Chord events are formed by **full expansion**, duplicating
overlapping note events at every unique onset time.

**[FACT, §5.2]** Rhythmic and metric viewpoints were **deliberately excluded**: *"the terminal events at
the moment of cadential arrival appear in strong metric positions, and few of the cadences feature
unexpected durations or inter-onset intervals at the cadential arrival, so we have excluded viewpoint
models for rhythmic or metric attributes from the present investigation."*

## Measured results, as the paper states them

**Corpus (§5.1, Tables 2–3).** 50 sonata-form expositions from Haydn's string quartets (1771–1803),
Opp. 17–76, from KernScores. 270 cadences annotated, 25 excluded (15 where the cadential bass or soprano
is absent from cello or first violin; 10 implying more than one category), leaving **245 cadences**:
PAC 122, IAC 9, deceptive 19, evaded 11, half cadence 84. Note events: violin 1 14,506; violin 2 10,653;
viola 9156; cello 8463; expanded chord events 20,290.

**Experiment 1 — are cadential terminal events more predictable than non-cadential ones?** For the first
violin, mean IC increased significantly from PAC to non-cadential contexts for `melint`, `csd` and
`selection`, but not for the baseline `cpitch` (Table 4). **For the cello the direction reversed**: mean
IC *decreased* in every model from PAC to the non-cadential levels — *"contrary to our predictions, the
terminal events in the cello from cadential contexts were actually less predictable than those from
non-cadential contexts."* For the chord viewpoints `vintcc`, `csdc` and `composite`, cadential terminal
events were more predictable than non-cadential ones, `composite` showing *"an ascending staircase"*
from PAC through tonic to non-tonic.

**★ [FACT, §6.1.3] The authors' own explanation of the cello reversal, and it is a fact about the
evidence rather than about the model.** *"since the leap in the bass by descending fifth (or ascending
fourth) in perfect authentic cadential contexts occurs less frequently than motion by smaller intervals
in any other context …, it may also be that cadential bass lines are simply less predictable than their
stepwise, non-cadential counterparts when considered in isolation. For the viewpoints that explicitly
model the interaction between the bass and the upper voices, however (e.g. `vintcc`, `csdc`, or
`composite`), IDyOM produced considerably lower IC estimates for cadential successions like 5̂–1̂ than
for non-cadential successions like 1̂–1̂, 2̂–1̂, or 7̂–1̂."*

**★ [FACT, §6.1.3] The half cadence, measured by a third method.** *"half-cadential contexts generally
failed to elicit lower mean IC estimates compared to non-cadential root-position dominants. Thus,
according to IDyOM, the terminal events from the HC level are no more (or less) predictable than any
other instance of root-position dominant harmony selected at random from the corpus."* **★ The bound the
paper's own Table 5 (p. 14) sets on that sentence:** HC against
random root-position dominants is not significant for every cello viewpoint and for `vintcc`, `csdc` and
`composite`; **for the first violin it IS significant under `cpitch` (p .024), `melint` (.007) and
`selection` (.008)** — the HC terminal events there being more predictable — and not under `csd`. The
text at p. 12 says the same. The paper's *"generally"* is its own hedge; the *"Thus …"* sentence is wider
than its table.

**Experiment 2 — do the IC estimates order the cadence categories as a typology predicts?** The
*Prospective Schemas* ordering PAC→IAC→HC→DC→EV fits better than the *1-Schema* ordering
PAC→IAC→DC→EV→HC; for `composite` the Prospective model *"accounted for roughly 55% of the variance …
which represents the largest effect demonstrated across all of the polynomial contrasts from every
viewpoint model"* (Table 6). Genuine cadence categories received lower mean IC than the cadential
deviations in every model.

**★ Experiment 3 — where the boundary evidence actually sits.** [FACT, §6.3] The two hypotheses tested
are *"(1) that the terminal event of a group is the most expected (i.e. predictable) event in the
surrounding sequence; and (2) that the next event in the sequence is comparatively unexpected (i.e.
unpredictable)"*, on the ground that *"unexpected events engender prediction errors that lead the
perceptual system to segment the event stream into discrete chunks."* Results (Table 7, Figure 6): for
the first violin, *"the mean IC estimates … increased significantly following the predicted boundary for
every cadence category in the collection"*, and for PAC, IAC, HC and DC the increase from the terminal
event to the following one was significant. For the **evaded** category the significant increase occurs
*at* rather than after the expected terminal event, which the authors give as the predicted behaviour
for a cadential deviation. The framing sentence: *"the strength of the potential boundary between two
sequential events results in part from the increase in information content (or decrease in probability)
from the first to the second event."*

**The authors' own stated limitations** [FACT, §7]: *"the rather meager sample size for three of the
five cadence categories … casts some doubt upon the generalisability of the reported findings"*; the
melodic models assume listeners expect *specific* intervals rather than small ones generally, which is
*"theoretical, rather than empirical"*; only contiguous *n*-grams were used, which *"is particularly
acute for corpus studies of tonal harmony, where the musical surface contains considerable repetition,
and many of the vertical sonorities from the notated score do not represent triads or seventh chords,
thereby obscuring the most recurrent patterns"*; and *"IDyOM benefited from human annotations of tonal
information in `csd`."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score reduced so that each instrumental part is
monophonic (ornaments and multiple stops removed); **a hand-annotated key, mode, modulation and pivot
boundary track**; and **a hand-annotated cadence collection** typed under Caplin. It assumes no
segmentation of its own and performs none.

**What it HANDS downstream.** Per-event information content in bits, per viewpoint — a scalar of
*predictedness*, not a label, not a boundary and not a decision. Nothing in its output is a fact about
the music that another layer could consume as evidence without first deciding what an IC value means.

**Its own STATED SCOPE and limits.** One composer, one genre, one form section: Haydn string-quartet
sonata-form expositions. Rhythm and meter excluded by design. The object of study is the listener.



# EXTRACT — Illescas, Rizo & Iñesta, "Harmonic, Melodic, and Functional Automatic Analysis" (ICMC 2007 by the bibliography's row; the file prints no venue and no year) — Task B candidacy row 34, first pass, AT THE OBJECT



---

## 3. What the paper actually does — stated in the paper's own structure

**The pipeline as page 2's §2 enumerates it, five steps.** (1) A melodic analysis tags each note harmonic
or non-harmonic, allowing several tags per note where the rules conflict, to be *"disambiguated later"*.
(2) A vertical analysis: *"after segmenting each bar into a number of time windows, all possible chords
are obtained from the notes in each individual window"*. (3) For each window, the tonalities among the 24
that are feasible given the accidentals are kept. (4) A weighted directed acyclic graph, layered by
window, whose nodes are chords-with-tonal-functions-in-a-tonality and whose edges are valid progressions
weighted by importance — *"e.g. perfect cadences are scored higher than half cadences"*. (5) Dynamic
programming finds the best path; the output is the Roman-numeral analysis with a tonality segmentation;
*"having this harmonic information, those notes still having a multiple melodic analysis are
disambiguated."*

**§2.1 Melodic analysis (pages 2–3).** *"based only on the melodic information, leaving aside any harmonic
vertical information"*. The rules are written in the *JBoss Drools* rule engine (footnote 1) — an expert
system, not a fitted model — *"based on meter, pulse, duration, and pitch interval information"*.
Definitions 2.1–2.10 define relative duration (to the beat), a duration ratio to the neighbours, pitch
name and pitch class, a pitch interval written as *degree-steps.semitones* (unison 1.00, tritone 4.06),
previous and next intervals, a sub-beat flag, a strong-beat flag (quaternary: beats 1 and 3; ternary: beat
1), and a tie flag. *"There are 38 different rules"* (page 2), summarised for four kinds in Table 1 (page
3): appoggiatura (strong, approached by unison, left by a step), suspension (strong, tied, approached by
unison, left by a step), passing tone (weak, ratio ≤ 1, approached and left by step in the two sign
patterns Table 1 prints), neighbour tone (weak, ratio ≤ 1, approached and left by step in the other two
sign patterns) — the direction words are not this side's reading, which stops at the table's own
interval sets. The caption adds that *"a passing tone starting in a weak beat or sub-beat is allowed using
a low confidence."* Each rule assigns one of the four confidences. **The rules are hand-written (*"a series
of rules written by the authors based on the music theory applicable to the baroque period"*, page 2); no
rule was learned from data.**

**§2.2 Chord extraction (page 3).** *"For each of the bars, the duration of the shortest figure or rest
is selected as the time resolution for that bar. Then, the bar is divided into windows of that
duration for all the voices in the score."* For each window the sounding set S_w is built and the
candidate chord set C_w is every ordering of note names, octave dropped, in which adjacent notes are a
third or a fifth apart (condition (1): the pitch interval is in {3.s, 5.s}), found by backtracking.
**Two consequences the paper states itself:** *"the backtracking process reorders all notes in the
chords. This means that, even if the original positions of the notes suggest an inversion, this process
deletes it and returns the root note of the chord to the lowest note position"*; and the window grid is
per-bar and fixed before any harmonic decision.

**§2.3 Accidental analysis (page 3).** For each window, the 24 tonalities are filtered to those in which
every sounding note is diatonic — where diatonic is defined by Table 2's semitone sets from the tonic,
which admit the Neapolitan second in both modes (the *(1)* cell), the raised third in minor (the *(4)*
cell, *"the Picardy ending"*) and both forms of the sixth and seventh degrees in minor. K_w is the set of
tonalities surviving the filter.

**§2.4 Tonal functions (page 4).** *"all notes, all chords, all music fulfill"* the tension–relaxation
principle; a relation degree → function is fixed by Table 3: I → T; II → S; III → S, T, D; IV → S; V → D,
T; VI → S, T; VII → S, D. *"The V degree has a tonic function to allow half cadences"*. III and VI take
their function from their harmonic neighbours: a complete III (with the fifth altered in minor) before a
tonic is dominant *"with a high level of confidence"*; an incomplete III after a dominant is tonic; **and
the authors state of III as subdominant: *"To the best of our knowledge, this treatment is not found in
the music theory literature, however, we attribute this function to it because we consider the tonal
functions as levels of tension and musical stability"*** — a theoretical choice the paper marks as its own.
VI is subdominant after a tonic or subdominant, tonic after a dominant.

**§2.5 The weighted acyclic directed graph (pages 4–5).** G = (V, E, D); the vertices are partitioned
into |W| disjoint layers, one per window, and an edge runs only from layer i to layer i+1. Each node
carries a feasible (tonality, chord, function) — the paper writes the node labels as the tonal functions
f drawn from F_{w,k}(c_i). Edges between successive layers carry a weight d(f_a, f_b) from Table 5 (page
5): within a tonality, T→D 26, T→S 75, T→T 1, S→D 100, S→T 145, S→S 1, D→S −101, D→D 1, and D→T split by
the chords forming the cadence — a perfect V triad with minor seventh to I or i 2500, to VI or vi 2100, a
perfect V triad to I or i 1900, a diminished vii with minor seventh to I 2300, a diminished vii with
diminished seventh to i 2300, a diminished vii triad to I 1600, and so on down to 1500 — read off the page
image, where several paired rows share one printed weight cell and are read here as sharing the value.
**The paper's own statement of provenance for these numbers, whole: *"The values in Table 5 have been established
empirically. A negative value is assigned to reflect the tonal regression D → S."*** No procedure, no
data, no held-out set and no search is described for them. Cadences are Table 4 (page 5): perfect
authentic, imperfect, interrupted, plagal, dominant half and subdominant half, each as a degree pattern.
*"Tonality changes are allowed only when a cadence in a new tonality is found. Not feasible
progressions (those specified in section 2.4) are weighted with −∞."* Figure 3 (page 6) shows *"an
extract of a graph for the tenth bar"* of chorale #25; it is not reproduced.

**§2.5.2 Best path (page 5).** *"the selection of the best path is reduced to the classical problem of
the computation of the best path in a graph by dynamic programming [2]"* — [2] is Brassard & Bratley's
algorithms textbook. The nodes on the best path give *"tonal functions, degrees, and tonality changes"*.

**§2.6 Melodic disambiguation (page 5).** After the best path is fixed, notes left with conflicting tags
*"are tagged as NHT when they do not belong to the current chord at each moment."* So the harmonic
decision feeds back into the melodic tagging once, for the ambiguous notes only — the notes tagged
without conflict in step (1) are not revisited.

**§3 Experiments (pages 5–6).** Input from Kern Scores; six chorales; comparison against *"a relevant
work named MTW (Music Theory Workbench) [12]"* — Taube 1999; *"A full report of the obtained results can
be downloaded from http://grfia.dlsi.ua.es/cm"*. **The paper's own statement of why no
figure is reported, whole: *"Since two different analyses sometimes can be both valid we cannot give
success percentages in order to compare to those reported by MTW."*** Its qualitative claims: MTW *"fails
in some tonal function progressions and seems to make mistakes when analyzing alternative tonalities by
not solving the chord cadence (e.g. BWV 2-6 at bar 3, beats 2, 3, and 4)"*; *"Our system corrects those
errors by means of the cadence scoring. However, we must correct some errors the MTW does not make.
Anyway, our system has failed only in two chords in the analysis of choral #25."* Runtime *"a few
seconds"* on a named machine (an Apple G4).

**§4 Discussion (pages 6–7).** The input requirements quoted at §2; *"Other related works in the
literature are able to work without meter [13]"* (Temperley & Sleator); results *"comparable"* to
MTW with the advantage of *"being ready to work with monodic melodies only adding more possibilities of
analysis at each layer of the graph"*. Limitations the authors state: windowing splits chords that
should be merged (compaction is *"working on"*); *"Currently the system does not show the inversion of
chords"*; double neighbour, cambiata, escape tone and fux tags defined but not implemented; *"Modulation
points are currently displaced in a ±one chord distance. This is due to the dynamic programming
algorithm. Hopefully, this problem will be solved by the use of a harmonic rhythm and a modulation
subsystem."* Future work: *"the construction of a larger corpus of tagged pieces to be able to learn the
scoring of the tonal function progressions from that corpus"* — the authors themselves name the hand-set
Table 5 as the thing to be replaced by learning; and new rules for other genres, *"the romantic period
seems to be the hardest one"*.

---

## 9. What the paper does NOT claim

**The paper does not claim** an accuracy; a comparison against human annotation; a learned model of any
kind; a treatment of inversion; a treatment of modulation beyond cadence-gated tonality change; polyphonic
input beyond the requirement of correct spelling and meter; or that its III → S mapping is from the
literature — it says the opposite.



---



# EXTRACT — de Clercq, "A Model for Scale-Degree Reinterpretation: Melodic Structure, Modulation, and Cadence Choice in the Chorale Harmonizations of J. S. Bach" — Task B candidacy row 40, first pass, AT THE OBJECT



---

## What the paper is, in its own structure

Five parts, by the paper's own headings: an untitled introduction (pages 188–191) setting up Gauldin's
pedagogical problem; **METHODS AND METHODOLOGICAL ISSUES** (192–196); **SOME SPECIFIC RESULTS**
(196–198); **A MODEL FOR SCALE-DEGREE REINTERPRETATION** (198–202); **DISCUSSION** (202–204); then
**NOTES** (204–205) and **REFERENCES** (205–206).

**The problem it addresses is a teaching problem, and the paper says so.** Gauldin (2009) reports that
graduate students harmonizing a chorale melody suffer *"tunnel vision"* — they interpret melodic
fragments in the global tonic only, so their harmonizations lack Bach's tonal variety. Gauldin's
remedy is the concept the paper's title takes: **scale-degree reinterpretation**, reading the melody's
notes as diatonic degrees in some key other than the tonic. The paper's stated objection to that
remedy is that it enlarges the student's problem space — *"With scale-degree reinterpretation, the
cadential possibilities increase significantly"* (page 189) — so the paper sets out to measure which
of those possibilities Bach actually used.

**What it encodes, per event.** The unit is the **fermata event**. For each one the paper records
three things in a shorthand of its own (page 194): **(1) the local key area**, written as an
upper- or lower-case Roman numeral *"as reconciled with the global tonic"*; **(2) the cadence
classification**, a two-letter abbreviation over the standard American textbook categories — perfect
authentic (PA), imperfect authentic (IA), half (HF), phrygian (PH), plagal (PL), deceptive (DE) — plus
**one category the paper reintroduces**, McHose's (1947) *"plagal half cadence"*, which the paper
renames the **subdominant stop (SS)** *"to avoid confusion with other cadence types"*; and **(3) the
chordal member of the soprano note at the cadential arrival**, an Arabic number. The example the paper
gives: *"the notation 'III-IA3' in the key of G minor represents an imperfect authentic cadence in Bb
major with the third of the chord (D) in the soprano at the point of cadential arrival."* Inversion is
indicated by a slash *"if the final chord of a cadential gesture was inverted, but this feature was
rarely needed."* A problematic event gets **"NC" (no cadence)**.

Separately, the **melody** is encoded as the scale-degree content **for the last three beats up to and
including the cadence**, measured against the **global** tonic, *"universally measured in terms of a
parallel major scale, with flats and sharps indicating raised or lowered versions (e.g., scale-degree
3 in a minor key was encoded as 'b3')"* (page 193).

**Scale.** *"In total, the corpus is encoded with 2,124 unique fermata events"* (page 196). Repeat
signs are ignored throughout. The encoded files are released: note [8] gives
`http://www.midside.com/publications/chorales/`.

---

## The paper's own claims, labelled

Each is **FACT** where the paper states or measures it, **THEORY** where it is established published
theory the paper leans on, and **CONJECTURE** where the paper offers it as its own suggestion without
measuring it — the labelling the theory-grounding corollary to #1/#2 requires.

**(1) [FACT — stated of the method, page 195.]** The cadence categorization was performed **by ear at
the piano** by the author, one person, over the whole corpus.

**(2) [FACT — measured and stated, page 195, carried verbatim because its wording is load-bearing.]**
*"One final concern is that some cadences are inherently ambiguous. The classic case of tonicization
versus modulation comes to mind, where it may not be clear, for instance, whether we have a half
cadence in the key of tonic or an authentic cadence in the key of the dominant. To explore this issue
somewhat (i.e., the degree to which cadence analysis is a subjective task), I asked another Ph.D. in
music theory (David Temperley) to analyze a portion of the chorales using the same encoding method
described above. Within the test subset (about 10% of the total), we had identical encodings for over
95% of the cadence events. It was found that our primary differences did, in fact, concern the issue
of tonicization versus modulation."* The author's own gloss, continuing onto page 196: *"while our
agreement level fell short of the 100% ideal, it seemed good enough to indicate confidence that music
scholars generally classify cadential events within the chorales in highly similar ways."*

**What that figure IS and IS NOT, stated here so no later reader has to re-derive it.** It **is** a
published, two-annotator agreement figure, on **Bach chorales** — symbolic Baroque repertoire — whose
encoding unit contains a **local key area** as its first component, with the disagreement class named
(**tonicization versus modulation**). It **is not**: per-axis (the >95% is agreement on the composite
token, and the paper reports no separate figure for the key component, the cadence component or the
soprano-member component); a Roman-numeral-per-chord agreement (it covers **fermata events only**,
about one per phrase ending, not every chord); exactly quantified (*"about 10%"* of the corpus, *"over
95%"*, with no count of events compared, no denominator and no interval of any kind); or independent
of the author (one of the two annotators **is** the author).

**(3) [FACT — Table 2, page 190, and it is NOT this paper's measurement.]** The paper reproduces
Boyd's (1967/1999) cadence analysis of 371 Bach chorales: Authentic 1,452 (73.0%), Half 415 (21.0%),
Plagal 44 (2.0%), Deceptive 33 (1.5%), Others 50 (2.5%). **This is a table adapted from another
author's book and is labelled as such; no figure of it is this paper's own.**

**(4) [FACT — Table 3, page 196.]** Of the **90** unique instances in the Bach chorales of the melodic
phrase ending 6-6-5 (measured against the global tonic), the distribution of cadence types is: V-PA1
83.3%, I-PL5 8.9%, iii-IA3 4.4%, V-DE3 1.1%, IV-HF5 1.1%, NC 1.1%, and **zero** for I-HF1, I-IA5,
V-IA1, iii-DE5 and iii-PL3. Note [9] states the consequence plainly: *"Of the 90 instances of the
melodic phrase ending 6-6-5 in the chorales of J. S. Bach, none are harmonized with a half cadence in
tonic."* **The paper's rhetorical point is that the tonic half cadence is the reading a tunnel-visioned
student would reach and Bach never reaches it here.**

**(5) [FACT — Table 4, page 197.]** Excluding final cadences, of the **153** non-final fermata events
with the melodic pattern 2-2-1, (I or i)-PA1 accounts for 93.5%, (I or i)-DE3 for 3.9%, NC for 1.3%,
and (vi or VI)-IA3 and VII-HF5 for under 1.0% each; the remaining six listed categories are zero. The
paper's reading: *"over 97% of the 153 non-final fermata events given the melodic pattern 2-2-1 involve
a cadence in the tonic key. Scale-degree reinterpretation thus seems like an appropriate technique in
certain situations, less appropriate in others."*

**(6) [FACT — Tables 5 and 6, pages 197–198, every cell re-derived here in both directions.]**
Non-final cadences by the soprano's scale degree at the cadential arrival.
**Table 5, major-key chorales**, columns *most common (#)* / *second-most common (#)* / *others (#)* /
*total*: degree 1, I-PA1 156 / vi-IA3 35 / 57 / 248; degree 2, I-HF5 110 / ii-PA1 28 / 19 / 157;
degree 3, I-IA3 100 / ii-HF5 36 / 27 / 163; degree 4, IV-PA1 16 / ii-IA3 10 / 10 / 36; degree 5, V-PA1
151 / I-PL5 12 / 49 / 212; degree 6, vi-PA1 21 / I-SS3 9 / 13 / 43; degree 7, V-IA3 36 / vi-HF5 17 / 8
/ 61. **Column sums 590 / 147 / 183 and row sum 920 — both derived here and both closing.**
**Table 6, minor-key chorales:** degree 1, i-PA1 151 / i-DE3 15 / 31 / 197; degree 2, i-HF5 111 /
VII-IA3 32 / 18 / 161; degree b3, III-PA1 110 / i-IA3 9 / 22 / 141; degree 4, iv-PA1 22 / III-HF5 20 /
7 / 49; degree 5, III-IA3 52 / v-PA1 47 / 101 / 200; degree b6, iv-IA3 6 / VI-PA1 2 / 1 / 9; degree b7,
VII-PA1 37 / v-IA3 11 / 8 / 56; degree 7, i-HF3 28 / i-PH3 10 / 0 / 38. **Column sums 517 / 146 / 188
and row sum 851 — both derived here and both closing.**
The paper's own reading of the pair: *"the most-common and second-most-common cadences account for
about 80% of the non-final cadential events in the Bach chorales"* — **(590+147+517+146) / (920+851) =
1400/1771 = 79.05%, derived here**, so *about 80%* is the paper's own rounding of a figure its tables
support. It also observes that *"30 different cadence types is a lot for a student to remember"*; **the
30 is 7 degrees × 2 columns in Table 5 plus 8 degrees × 2 in Table 6 = 30, derived here at the tables.**

**(7) [FACT — Tables 7 and 8, pages 198–199. THIS IS THE MODEL.]** The simplified model keeps only
PA1, HF5 and IA3 cadences and maps them onto closely-related key areas, the key areas ordered left to
right by typicality. **Table 7, major-key:** soprano degrees 1/2/3 → the **tonic** key (I-PA1, I-HF5,
I-IA3); degree 1 also → the **submediant** (vi-IA3); degrees 5/6/7 → the **dominant** (V-PA1, V-HF5*,
V-IA3); degrees 6/7 → the **submediant** (vi-PA1, vi-HF5); degrees 4/5/6 → the **subdominant** (IV-PA1,
IV-HF5*, IV-IA3*); degrees 2/3/4 → the **supertonic** (ii-PA1, ii-HF5, ii-IA3). **Table 8, minor-key:**
degrees 1/2 → the **tonic** (i-PA1, i-HF5); degrees b3/4/5 → the **mediant** (III-PA1, III-HF5,
III-IA3); degree b3 also → the tonic (i-IA3); degrees 1/2 → the **subtonic** (VII-HF5*, VII-IA3);
degree b7 → the subtonic (VII-PA1); degrees 5/b7 → the **dominant** (v-PA1, v-IA3), with (n/a) at
degree b6; degrees 4/5/b6 → the **subdominant** (iv-PA1*, iv-HF5, iv-IA3). Asterisks mark
model/data mismatches. The paper states the model's content in one sentence: *"a harmonization default
is to interpret the soprano note at the fermata as scale degree 1 (via a perfect authentic cadence), 2
(via a half cadence), or 3 (via an imperfect authentic cadence) in tonic or some closely-related key
area, with the tonic, dominant, and submediant keys being more likely destinations (in that order)
than the subdominant or supertonic."* For minor it records that *"there is a tendency to modulate to
the relative major whenever possible"*, which is why the **mediant** is the left-most column of Table 8.

**(8) [FACT — page 199, and its arithmetic re-derived here.]** *"Its success rate sits at 80.6% overall
(1761 internal cadences, 1420 model matches): a good result, but not great."* **1420/1761 = 80.64%,
derived here.**

**(9) [FACT — Table 9, page 199.]** The simplified model's success rate by the generic melodic interval
leading into the cadential arrival: descending 2nd, 1084 instances / 968 matches / **89.3%**; ascending
2nd, 456 / 346 / **75.9%**; descending 3rd, 137 / 85 / **62.0%**; ascending 3rd, 1 / **".."** / ".."; 
descending 4th, 14 / 8 / ".."; ascending 4th, 22 / 4 / ".."; unison, 47 / 12 / **25.5%**. **The
instances column sums to 1,084+456+137+1+14+22+47 = 1,761, derived here, and that is exactly the
"1761 internal cadences" of claim (8) — so Table 9 partitions the model's own denominator.** The
paper's reading: *"most melodies descend by step into the cadential arrival … and the model fares
noticeably better in this situation, with a success rate of roughly 90%."*

**★ THE ".." CELLS ARE A PRACTICE AND ARE RECORDED AS ONE.** The paper prints ".." rather than a
percentage for the three intervals with the smallest instance counts (1, 14 and 22) and says why:
*"there are simply not enough instances in the Bach chorales to make any meaningful estimate of a
typical solution."* **It declines to report a rate on a small denominator rather than reporting one
and letting the reader discount it.**

**(10) [FACT — pages 200–201, with two significance tests.]** Four special cases are added to the core
three. **The deceptive cadence**, 2.5% of cadences overall, used *"primarily to add harmonic variety to
adjacent melodic phrases that end on the same note"*, with **a significantly higher incidence as the
penultimate cadence (p < .01; Fisher's exact test**, note [11] stating the test's exact form). **The
plagal cadence**, 2.8% overall, whose most common type, PL5, typically arises *"out of melodic upper
neighbor motion around scale-degree 5"*. **The subdominant stop**, 2.7% of all fermata events, *"especially more probable
within the tonic key than in any other key (p < .001; FET)"*, note [12] stating that form. And
**"expansion to the octave"**, an ascending melodic line against a descending bass line, each moving by
step into the final chord, which *"tidily encompasses a few different cadence types, including certain
classes of imperfect authentic, half, and phrygian cadences"* — the paper notes that *in every case of
expansion to the octave, there is half-step motion in one of the outer voices at the cadential
arrival.*

**(11) [FACT — Figure 18 and page 202.]** With those four special cases the flowchart *"achieves a
success rate of 92.2% in accounting for cadence choices in the chorales."* The flowchart's first test
is whether a minor melody ends on the leading tone; then it branches on the melodic interval at the
phrase-final event — unison, descending 3rd, descending 2nd, ascending 2nd — and within the descending
2nd branch on whether there is melodic upper-neighbour motion.

**(12) [FACT — page 192, Figure 5.]** *"As a rule, fermatas were taken to delineate phrases but not
necessarily to indicate the exact location of the cadential arrival."* The displacement is stated as a
conditional rule: most commonly the final chord of the cadence falls under the fermata on beat 3 in
4/4; where the fermata falls on a weak beat, *"Bach exhibits a clear tendency to shift the cadential
arrival to the strong beat when possible"* — possible **when the weak-beat fermata is preceded by a
unison or a fall of a third**, because those intervals can be contained within one harmony, and
**impossible when it is preceded by a step**, in which case the arrival is displaced forward onto the
weak beat to coincide with the fermata. The operational rule the study used: *"cadence locations were
determined on a case-by-case basis, with the cadential arrival (if any) taken as the last change of
harmony at or before the fermata"* (page 193).

**(13) [FACT — page 194, a stated definition and a stated caveat.]** *"In this paper, I will use the
term 'cadence' to mean 'the harmonic event at the phrase ending as indicated by the fermata,' if only
because the former is less clumsy."* The
paper states that this is contestable: *"Some readers – especially those with Schenkerian leanings
(see Caplin 2004) – may feel that the subdominant stop is not truly a cadence at all. This feeling may
extend to the plagal cadence or the deceptive cadence as well."* Its own justification is that the
study's question is about **what harmonizations a melodic phrase ending engenders**, so the
Schenkerian question is *"somewhat moot"* for it — *"we could say that we seek knowledge about
'fermata events,' some of which may be true cadences in the Schenkerian sense, some of which may be
not."*

**(14) [FACT — pages 196–197, on final cadences.]** *"166 of the 177 major-key chorales end with a
I-PA1; moreover, 99% end with a cadence in the tonic key."* Excluding minor-key chorales with Phrygian
melodies (all of which end on a dominant chord in relation to the home key), *"99% of those that end on
scale-degree 1 end also with a perfect authentic cadence on tonic."* In minor-key chorales, final tonic
cadences with Picardy thirds (I#-PA1) *"outnumber those without a Picardy third (i-PA1) by a 10-to-1
ratio."*

**(15) [THEORY, taken from others and not measured here — page 195.]** On modal melodies, the paper
reports Burns (1993, 1994, 1995) showing that *"chorales with modal melodies can be successfully
analyzed by replacing characteristic tonal voice-leading paradigms with modal paradigms"*, against
Renwick (1997), who *"argues that it is only the melody of a chorale, analyzed in isolation of the
harmony as a single line, that is modal; otherwise, Bach sets the melody in a patently tonal harmonic
context."* **The paper takes NEITHER position and says so in effect: it sets the question aside on the
ground that its own encoding makes the answer inert for it** — *"the impact of modal melodies on this
study is considered to be relatively low since the melodic encoding scheme captures any chromatic
content. So whether, for example, the melodic fragment b7-6-5 is drawn from a Mixolydian melody, a
Dorian melody, or a major (Ionian) melody with some chromaticism, this fragment represents a
particular category of melodic structure that is tracked via the melodic encoding scheme described
earlier."*

**(15a) [FACT — page 195.]** On the global key: *"Other
analytical issues involved the tonality of the chorale. In some cases, the global key of the chorale is
not entirely clear. This situation was found to be fairly rare, though. Moreover, as I hope to show,
**the global key turns out to be less important than the local key implications in terms of what cadence
type to expect given a particular melodic pattern**."*

**(16) [CONJECTURE — page 204, the paper's own closing suggestion, measured nowhere in it.]** *"It would
be interesting in a future study, therefore, to investigate what types of bass patterns associate with
particular melodic patterns. Studying cadential bass patterns would add a more objective element to the
somewhat subjective task of cadence classification. The results of such a study may even suggest new or
overlapping cadence categories beyond those considered here."*

**(17) [FACT — pages 203–204, three stated limits of the study, in the author's own voice.]** That the
study **ignores the text of the hymns**, citing Pirro (1907/2010) on the close relationship between
Bach's chorales and their words, and conceding *"it may be that some chords and progressions are only
possible to reconcile through an analysis of the lyrics"*. That it **assumes the hymn tunes were
pre-compositional** — *"the actual scenario (at least in some cases) may be the reverse"*, since Bach
sometimes varies the hymn melody from one setting to another. And that it addresses only *"the small
slice of the harmonization process that is cadence choice"*, leaving the voice leading of inner parts
and the bass patterns unexamined.

**(18) [FACT — pages 196 and 203, a claim about tonic-key tunnel vision that runs against the paper's
own framing.]** Having introduced the paper as a corrective to tunnel vision, the author twice reports
evidence in the other direction: *"tonic-key tunnel vision is not always a bad thing"* (page 196), and,
against Salzer and Schachter's advice to avoid consecutive tonic cadences, *"Salzer and Schachter's
implicit advice to avoid consecutive tonic cadences is rather poor, as over a third of the chorales
include consecutive tonic cadences. (Chorales 86 and 323 have five authentic cadences in tonic in a
row!) Here again, we find evidence that tonic-key tunnel vision is not necessarily a bad thing;
rather, the modulation strategy is dependent on the melodic structure."*

**(19) [FACT — page 191, a stated judgment about a family of systems.]** Surveying the automated chorale-harmonization projects — constraint-based systems drawing on
theory treatises (Ebcioğlu 1988, 1990), neural networks trained on their own analyses (Hörnel & Menzel
1998), and Markov chains (Thorpe 1998; Biyikoglu 2003; Allan & Williams 2005) — the paper writes: *"Some
of these models have been fairly successful at creating convincingly stylistic harmonizations.
Unfortunately, these studies have limited benefits for music theory pedagogy; even when these models are
successful, **it is difficult to infer any practical advice to a music student since a wide variety of
parameters and settings are involved**."*

**(20) [A SECOND-HAND CHARACTERISATION, OUT OF WHICH NOTHING IS CARRIED — page 191.]** The paper
characterises an unheld work in one line: *"Rohrmeier and Cross (2008), for example, have used the
chorales to investigate fundamental aspects of tonality and harmonic syntax, showing that only a few
elements control most of the musical structure."*

**(21) [AN ERROR OF THE PAPER, minor, recorded so a later reader is not sent to the wrong figure —
page 199.]** Discussing the rarity of I-HF3 cadences, the paper writes *"(This finding is a notable
exception to the list of common cadences that Gauldin proposes shown in **Figure 5**.)"*  **Gauldin's
proposed cadences are Figure 4** — its caption reads *"Fig. 4. Typical cadential formulas from Gauldin
1988/1995 (p. 44)"* (page 191) — while **Figure 5's caption reads *"Fig. 5. Different cadential arrivals
(*) in the opening bars of four Bach chorales"*** (page 192). Both captions were read at their pages.
**The cross-reference is to the wrong figure; nothing else turns on it.**

---

## Coupling facts (mandatory)

**How this paper's own decisions couple, in its own evidence.**

- **Key area ↔ cadence type are chosen together, not in sequence.** They are one encoded token, made in
  one act by one annotator. The paper never reports one without the other, and the model is a map to the
  pair.
- **Melodic degree → (key area, cadence type).** The paper's whole empirical claim is that the soprano's
  scale degree at the cadential arrival strongly constrains the pair — Tables 5 and 6 show the two
  commonest pairs covering about 80% of non-final events, and Tables 7 and 8 reduce that to three
  cadence types over **five** key areas in each table — Table 7's columns are tonic, dominant,
  submediant, subdominant and supertonic; Table 8's are mediant, tonic, subtonic, dominant and
  subdominant.
- **Melodic interval → the model's own reliability.** Table 9 is the paper's statement that its model's
  success is not uniform: it holds at 89.3% on descending 2nds, which are most of the data, and falls to
  25.5% on unisons. **The paper publishes where its own model fails, by condition.**
- **Fermata ↔ cadential arrival are NOT identical, and the offset is conditioned on the melody.** Claim
  (12): the arrival shifts to the strong beat before a weak-beat fermata when approached by unison or a
  falling third, and does not when approached by step.
- **Tonicization ↔ modulation is where the two annotators disagreed.** Claim (2). The paper names this
  as the locus of subjectivity in its own data.
- **The label vocabulary ↔ the theory of cadence.** Claim (13): the paper's categories are the American
  textbook set plus one reinstated category, and it states that a Schenkerian reader would deny that
  three of them are cadences.

---

## What this extract does NOT do

It **applies nothing**. It amends no `FRAMEWORK.md` text, no `CLAUDE.md` principle, no register entry
and no charter. It moves no verdict in `candidacy_upgrades.md` and no placement in the slice
derivation. It creates, flips or discards **no `OPEN_ITEMS.md` row** and allocates **no `D-NNN`**. It
lifts no gate, opens no stage, and touches no `src/` file, no build, no test, no golden and no corpus.
It fetches nothing from the web and it did not open the released data files note [8] names.

It does **not** establish that the record is silent about this paper anywhere outside the files this
session staged, which are named in the banner. It does **not** establish which of the two readings of
principle #21's FACT-of-absence is right — that is Finding (1), put to the user. It does **not** settle
the arithmetic residues of the section above. It does **not** claim that row 40's model supplies a
ceiling, a threshold or a term for any layer. And it does **not** re-decide the L2/L3 boundary: the
placement section answers the question the slice-derivation row left open about **this paper**, and
nothing wider.

---



# EXTRACT — Feisthauer 2021, the Lille thesis (modulations and cadences for sonata form) — population row 16, first pass



## Claims, labeled

- **[FACT — ch. 5]** A three-criterion dynamic-programming key tracker — cadential anchoring
  (V→I strength), diatonic note compatibility, and Weber-distance key proximity, over
  beat × 24-key states — reaches about 85% per-beat key accuracy on annotated Mozart string
  quartets, with the modulation/tonicization boundary acknowledged "porous" and no per-criterion
  ablation.
- **[FACT — ch. 6]** Descriptor-based cadence classification reproduces the published
  asymmetry: PAC F1 0.80 (Bach fugues) / 0.69 (Haydn, precision > 80%) against HC F1 0.29
- **[FACT — ch. 6]** Medial-caesura detection from abstract descriptors locates the caesura
  correctly for HALF the corpus on a very small training set — sonata-form structure detection
  is measured hard even with hand-crafted descriptors.
- **[FACT — ch. 2 §2.2]** The dual-tonality reading is stated as a principle: at every moment
  the score carries TWO defensible key labels — the modulation's and the tonicization's — and
  the thesis's specialized corpus annotates both.
- **[FACT — structure]** Key estimation and cadence detection are engineered as SEPARATE
  problems; their mutual dependence is noted theoretically and left unformalized.
- **[CONJECTURE — ch. 7]** That the local/global tonality interplay can be refined and the
  approach scaled to full sonata-form analysis — stated future work.

## Coupling facts (mandatory)

- **Assumes upstream (ch. 5 model):** the symbolic score with beats; nothing else — chords are
  not presupposed; (ch. 6 classifier): descriptor extraction over the score, cadence labels for
  training.
- **Hands downstream:** a key per beat + modulation points; cadence-arrival decisions; a
  medial-caesura location.
- **Stated scope:** classical string quartets and keyboard works; French-theory framing;
  no chord-level output anywhere — the thesis analyzes tonality and structure WITHOUT a chord
  layer.



# EXTRACT — Hamanaka, Hirata & Tojo 2013, "Computational Music Theory and Its Applications to Expressive Performance and Composition" — population row 19 (the GTTM computational line), CENTRAL, first pass



## Identity

Masatoshi Hamanaka, Keiji Hirata & Satoshi Tojo, "Computational Music Theory and Its Applications to
Expressive Performance and Composition", **chapter 8** of A. Kirke & E. R. Miranda (eds.), *Guide to
Computing for Expressive Music Performance*, Springer-Verlag London, **2013**, **pp. 205–234**.
DOI `10.1007/978-1-4471-4123-5_8`.

Affiliations as printed: Hamanaka — Intelligent Interaction Technologies, University of Tsukuba;
Hirata — Faculty of Systems Information Science, Future University Hakodate; Tojo — School of
Information Science, JAIST.



## Claims, labeled

### What the systems are

**[FACT, p. 206]** Two analysis systems built on GTTM are named: **ATTA** (automatic time-span tree
analyzer) and **FATTA** (fully automatic time-span tree analyzer). *"ATTA and FATTA can generate a
time-span tree as the result of a GTTM analysis."*

**[FACT, p. 209]** GTTM consists of four subtheories — grouping-structure analysis, metrical-structure
analysis, time-span reduction, and prolongational reduction — and *"attempts to simulate the listening
insights of an 'experienced listener.'"*

**★ [FACT, p. 209] THE PROLONGATIONAL REDUCTION — THE ONE SUBTHEORY THAT IS ABOUT HARMONY — IS NOT
IMPLEMENTED.** The chapter states which three it implements and then, verbatim: *"The prolongational
reduction is still evolving and is currently more controversial; hence we have not implemented it at
present."* And on p. 209 the prolongational reduction is precisely the one described as *"a tree
structure representing subordinate relationships between chords – doing so by explicitly indicating
harmonic retention and change."*
*(A prolongational tree EDITOR exists in the interactive analyzer for manual work, and p. 217 says
"A prolongation tree analyzer is also being developed" — under development, not measured.)*

### Why GTTM as published cannot be run, in the authors' own words

**★ [FACT, p. 210] THREE NAMED DEFECTS, EACH BLOCKING EXECUTION.**
- *Ambiguous concepts defining preference rules* — *"GTTM has rules for selecting structures in
  discovering similar melodies (called parallelism) but does not have a clear definition of
  similarity."*
- *Conflict between preference rules* — *"Conflict between rules often occurs and results – there is
  no strict order for applying the preference rules, causing ambiguities in the analysis."*
- *Lack of algorithmic form* — *"GTTM provides few descriptions of the reasoning and algorithms needed
  to compute analysis results."*

**★ [FACT, pp. 211–212] THE REMEDY IS 46 HAND-ADDED PARAMETERS.** exGTTM externalises and
parameterises the theory: **15 parameters for grouping-structure analysis (Table 8.1), 18 for
metrical-structure analysis (Table 8.2), 13 for time-span reduction (Table 8.3)** — and p. 216 states
the total in terms: *"Because there are 46 parameters, a significant amount of time is needed to
calculate all parameter combinations."*

**★ [FACT, p. 211] THE PARAMETERS ARE CLASSIFIED, AND THE THIRD CLASS IS THE ONE TO NOTICE.**
*Identified* — already in GTTM but with no concrete value. *Implied* — only implied by GTTM, made
explicit (the per-rule priorities). *Unaware* — verbatim: *"we develop parameters that are not
utilized in the original theory, because they lack clear musicological meaning."*

**[FACT, p. 211]** The method of setting them is stated plainly: *"Whenever we find a correct result
that exGTTM cannot generate, we introduce new parameters and give them appropriate values so that
exGTTM can then generate this result. In this way, we repeatedly externalize and introduce new
parameters until we have obtained all of the results that are generally considered correct."*

### The harmonic dependency — the most load-bearing coupling fact in the chapter

**★ [FACT, pp. 214–216] GPR7 IS IMPLEMENTED THROUGH LERDAHL'S TONAL PITCH SPACE, SO THE GROUPING
ANALYSIS CONSUMES A HARMONIC AND TONAL ANALYSIS.** D_GPR7 (eq. 8.1) is built from
`distance(p(i), s(i))` — *"the distance between notes x and y in the tonality of the piece – as
defined using Lerdahl's tonal pitch space"* — and that distance (eq. 8.2) is
**δ(x → y) = i + j + k**, where *"i is region distance, j is chord distance, and k is basic space
difference"*, the region distance being *"the smallest number of steps along the regional circle of
fifths"* and the chord distance *"the smallest number of steps along the chordal circle of fifths
between the roots of C1 and C2 within each region."* p. 223 states it directly: *"The region of the
melody and chord progression are estimated in GPR7 here by applying tonal pitch space methods."*

**★ AND THAT HARMONIC INPUT IS NOT AUTOMATED.** p. 220, verbatim: *"there is no automated analyzer
for tonal pitch space [22] in the interactive GTTM analyzer; however, attempts have been made to
implement the tonal pitch space system, so those results can be used as an input."* p. 217 confirms
the same from the other side: *"Although the GTTM includes rules that require the analysis results of
chord progression, the ATTA utilizes rules based on the results of the tonal pitch space approach."*

**[FACT, p. 220] The theory carries feedback links, and they are why analysis is iterative.**
*"the GTTM contains feedback links from higher- to lower-level structures … Therefore, analysis
involving feedback-linked rules requires a number of analysis processes by trial and error."* Named:
**GPR7** is *"a link from the time-span and prolongational trees to the grouping structure"* and
**MPR9** *"(time-span interaction) is a link from the time-span tree to the metrical structure"*
(p. 221).

**★ THE READING THIS FORCES, STATED PLAINLY.** In the most developed implementation of the time-span
reduction line, **the hierarchy sits DOWNSTREAM of tonality and harmony, not upstream of them** — the
grouping rule that most influences tree quality needs region and chord distances, and those come from
outside the system, by hand. A proposal to use a GTTM-style hierarchy *to help decide* harmony meets a
circularity that this implementation resolves by requiring the harmony first.

### Measured results

**[FACT, p. 228]** The measurement is an **F-measure**, `F = 2PR/(P+R)` (eq. 8.7).

**[FACT, pp. 228, 230] The ground truth.** *"A hundred sections of 8-bar-length, monophonic, classical
music pieces were collected. Musicology experts manually analyzed them utilizing GTTM and using the
manual-edit mode of the interactive GTTM analyzer to assist in developing the grouping structure,
metrical structure, and time-span tree. Three other further experts crosschecked these manually
produced results."* p. 233 records the dataset as *"300 pairs of scores and analysis results"*
published at `http://music.iit.tsukuba.ac.jp/hamanaka/gttm.htm`, and calls it *"the largest database
of analyzed results of GTTM thus far."*

**★ TABLE 8.4 (p. 230), total over the 100 melodies:**

| Analyzer | Baseline (default parameters) | Manually configured parameters |
|---|---|---|
| Grouping structure | **0.46** | **0.77** |
| Metrical structure | **0.84** | **0.90** |
| Time-span tree | **0.44** | **0.60** |

Baseline defaults as printed: S^rules = 0.5, T^rules = 0.5, Ws = 0.5, Wr = 0.5, Wl = 0.5, σ = 0.05.

**★ AND THE FULLY AUTOMATIC ARM, p. 230, verbatim:** *"Next, the set of parameters was optimized using
FATTA. The average F-measures became **0.48, 0.89, and 0.49** for grouping, metrical, and time-span
tree structures, respectively – thus still outperforming the baseline performance."*

**★ [FACT, p. 230] WHAT THE MANUAL COLUMN COST.** *"It took an average of approximately 10 min per
piece to find each plausible tuning for the set parameters"*, and *"the parameters were configured
manually because the optimal values of the parameters depend on the piece of music."*

**THE READING OF THOSE THREE ROWS TOGETHER.** On monophonic eight-bar
classical excerpts with expert ground truth: **automatic time-span-tree analysis reaches F ≈ 0.49, and
ten minutes of per-piece hand-tuning by the system's own authors raises it to 0.60.** Metrical
structure is the easy axis (0.84 at defaults). Grouping is where tuning buys most (0.46 → 0.77) and
where automation recovers almost none of that gain (0.48).

**[FACT, p. 231, Table 8.5]** Operation time over 100 melodies: interactive GTTM analyzer **575 s**
against the GTTM manual editor **891 s**.

**[FACT, p. 231] The melody-morphing evaluation is a consistency check, not an accuracy measure.**
Ten pairs of melodies; all extrapolative melodies satisfied the ordering condition (eq. 8.8). No
ground-truth comparison.

**[FACT, p. 222] A speed bound stated as a design constraint.** *"To be able to predict notes using
GTTM, FATTA must run in real time. However, several minutes are needed to finish an analysis."* The
remedy is approximation: reusing the previous melody's optimal parameters as the initial set, and an
analysis window of *"the longest group length within 16 measures"*.

### Scope, stated by the authors

**★ [FACT, p. 222] MONOPHONIC ONLY.** *"The FATTA system only deals with monophonic western tonal
music. Thus, the expectation method can predict only monophonic musical structures for western tonal
music as well."* Reinforced p. 227: *"FATTA [8] can generate a time-span tree from the score
automatically but can only deal with monophonic input."*

**[FACT, p. 209] Grouping and metrical analysis are described over homophony** — *"Grouping-structure
analysis hierarchically divides a series of notes in a homophony into phrases or motives"* — while the
implemented and measured pipeline is monophonic per p. 222.

**[FACT, p. 222] The stability level cannot start early.** *"The level of stability can only begin to
be calculated after the third note because GTTM analysis requires at least four notes."*

### Theory and conjecture

**[THEORY]** GTTM itself (Lerdahl & Jackendoff 1983, ref. 9) and Tonal Pitch Space (Lerdahl 2001,
ref. 22) are adopted published theory, not established here.

**[CONJECTURE, p. 220]** That history recording *"can be used to improve automated analyses"* and may
yield *"an analysis knowledge base"* — hoped for, not measured.

**[CONJECTURE, p. 233]** Further systems for harmonizing, voicing and ad-lib using time-span trees —
planned, not built.

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** a **MusicXML** score (p. 215 fig. 8.6 shows MusicXML in), **monophonic** for the
automatic arm, at least four notes; and — load-bearing — **a tonal-pitch-space analysis supplying
region and chord information, which the system does not compute** (p. 220). For the expectation-piano
application the MIDI stream is quantized by an *"adaptive quantization method"* (ref. 26) before
MusicXML is built (p. 223).

**HANDS downstream:** grouping structure, metrical structure and a **time-span tree**, as XML —
p. 217: *"An XML format is used for all the input and output data structures in the interactive GTTM
analyzer."* Fig. 8.6 names GroupingXML, MetricalXML, Time-spanXML. **No chords, no keys, no Roman
numerals, no harmonic labels of any kind leave this system**, the one harmony-bearing subtheory being
unimplemented. **No rivals and no confidence are published** — the analyzer commits one structure, and
where a user edit breaks well-formedness the process editor offers a small candidate menu (pp. 220–221)
to a human, not to a consumer.

**STATED SCOPE:** Western tonal music, monophonic for the automatic arm, eight-bar classical excerpts
in the evaluation; three of GTTM's four subtheories; parameters that must be tuned per piece for the
better numbers.



# EXTRACT — Lazzari 2023, "Knowledge-Based Chord Embeddings" (the Modal Harmony Ontology) — population row 7, CENTRAL-adjacent, first pass



## Identity

**Nicolas Lazzari, "Knowledge-Based Chord Embeddings"**, Master thesis in Knowledge Engineering,
Artificial Intelligence, Department of Computer Science and Engineering, **Alma Mater Studiorum —
Università di Bologna**, academic year 2021–2022, session 4. Supervisor **Valentina Presutti**,
co-supervisor **Andrea Poltronieri**. 129 pages; the file's own production date is January 2023.



**The list's description is confirmed on both halves, at the object.**

- *"the Modal Harmony Ontology"* — the abstract, verbatim: **"We design and implement the Modal
  Harmony ontology (MHO), using OWL (the standard web ontology language). It formalises one of the
  most important theories used to interpret western music: the Modal Harmony Theory."**
- *"all seven modes formalized"* — §4.1: **"Seven scales are defined by TMH: Ionian, Dorian, Phrygian,
  Lydian, Mixolydian, Aeolian, and Locrian."**
- *"multiple modal interpretations returned per progression"* — **Table 4.1**, §4.3.1. See below.



## Claims, labeled

### The theory formalised

**[FACT, §4.1]** MHO formalises **Modal Harmony Theory (TMH)**, sourced to *The Jazz Theory Book*
(Levine) and *Music in Theory and Practice Vol. 1* (Benward). Verbatim: **"the theory of Tonal
Harmony, based only on Major and Minor scales, is a proper subset of the theory of Modal Harmony."**

**[FACT, §4.1]** Each of the seven scales is built from a degree of the major scale, and a scale
carries both a **root** and a **tonality** — E Phrygian has root E and tonality C. The seven positions
are named **tonic, supertonic, mediant, subdominant, dominant, submediant, leading-tone**, and a chord
built on a position takes that role. Verbatim: *"each chord can be classified with a role based on the
context it is interpreted in. This allows the classification of a chord based on its function (i.e.
its role) within a scale and is the basis of Functional Harmonic Analysis."*

### The ontology, and how it is built

**[FACT, §4.2]** MHO **imports and extends two existing ontologies** — the **Chord Ontology** and the
**Music Theory Ontology (mto)**. The extension adds **24 missing intervals** (mostly compound) and
**56 additional chord qualities**.

**[FACT, §4.2]** **Chord quality is inferred from constituent notes by OWL reasoning**, not asserted.
Quoted axiom: `Class: MajorTriad EquivalentTo: (chord:interval value mto:MajorThirdInterval) and
(chord:interval value mto:PerfectFifthInterval)`. A Tristan-chord axiom is given as a worked case
(augmented fourth + augmented sixth + augmented ninth). Inference runs in the **OWL-EL profile**,
*"able to perform inference in polynomial time"*.

**[FACT, §4.2.1]** The scale-to-chord relation cannot be inferred by domain and range axioms alone, so
the ontology uses the **rolification** technique — property-chain axioms encoding *if-then* rules in
OWL2. **Algorithm 1** automates the rolification, at **O(|P|)** in the number of properties; it needs
inverse properties, hence **OWL-DL** in general, though some reasoners allow inverses under EL.

**[FACT, §4.2.1]** *"The final ontology is automatically generated by using the music21 library to
retrieve the association between a modal scales and its notes."* **A total of 6,344 axioms.**

**[FACT, §4.2.1] Quality restrictions are declared to be genre-dependent and editable:** *"They can be
updated by domain experts and eventually refined given the domain of application of the ontology …
the concept of tonic chord is slightly different between Rock music and Jazz."*

### The knowledge graph and what it answers

**[FACT, §4.3]** The KG's entities are extracted from **ChoCo** loaded into Stardog under EL reasoning. **7,651 chord individuals.**

**[FACT, §4.2/§4.3]** Six competency questions, each answered by a SPARQL query given in full: which
notes are in a mode; what is the role of a note in a mode; in which role can a note be classified;
which chords are in a mode; which are the roles of a chord; which chords absolve a role.

### ★ Table 4.1 — the row's own description, at the object

**[FACT, §4.3.1]** For the progression **C:maj – G:maj – A:min – F:maj**, the query returns **ten scale
readings with their Roman annotations**:

| Scale | Roman annotation |
|---|---|
| F Lydian Mode | V ii iii I |
| D Dorian Mode | °vii IV V iii |
| A Aeolian Mode | iii °vii I vi |
| F♯ Minor Scale | iii °vii I vi |
| G Dorian Mode | IV ii °vii |
| G Mixolydian Mode | IV I ii °vii |
| E Phrygian Mode | vi iii IV ii |
| B Locrian Mode | ii vi °vii V |
| C Ionian Mode | I V vi IV |
| C Major Scale | I V vi IV |

*Partial annotations — where a scale contains only a subset of the progression's notes — were
manually removed.* The thesis's gloss: *"The traditional I - V - vi - IV annotation is correctly
retrieved by the query, alongside many other annotations. Each of this can be seen as a different way
to musically interpret the chord sequence."*

**★ [FACT] THE ENUMERATION CARRIES NO MASS, NO RANKING AND NO CONFIDENCE.** Ten readings are returned
as a set, derived from scale membership; nothing in the method prefers one over another, and the
traditional reading is one row among ten with no marker distinguishing it.

**★ [FACT — the author's own bound, and it governs how any of this may be quoted] IT IS A PROOF OF
CONCEPT, NOT AN EVALUATED METHOD.** Verbatim: *"the query in Listing 4.11 can only handle simple
notations and should be seen as a proof of concept of applying the KG to the roman annotation task.
We claim, however, that by extending the presented query into a proper annotation system it would be
possible to obtain a method that is directly comparable to the related works. We will investigate
this option in future works."* **There is NO evaluation of the Roman-notation inference anywhere in
the thesis** — no corpus, no ground truth, no accuracy. Complex Roman notations such as parallel
chords are explicitly out.

**[FACT, §4.3.1] One property worth carrying: the query needs nothing but the chords.** *"does not
require any additional information besides the chord progression itself"* — contrasted in the same
paragraph with music21, for which *"a prior knowledge of the reference scale within which the
progression should be interpreted needs to be explicitly provided."*

### ★ What the headline 0.86 actually measures — established at §5.1, not taken from the abstract

**[FACT, §5.1]** The abstract's *"chord classification … accuracy: 0.86"* is the **Odd One Out**
intrinsic embedding metric: given a set of chords and one outsider, does the embedding place the
outsider furthest from the set's mean. **k = 4, 1,000 runs, 10 randomly sampled sets; random baseline
E[acc] = 1/5 = 0.2.**

**★ AND THE CLASSIFICATION IT IS SCORED AGAINST IS THE ONTOLOGY'S OWN.** Verbatim: *"The
classification is performed using the Knowledge Graph described in Chapter 4. In particular, we
consider 10 sets C by randomly sampling scales and the corresponding chord functions from the KG."*
**So 0.86 measures how well an embedding reproduces the knowledge graph that generated its labels.
It is an internal-consistency figure, not an accuracy against any human annotation**, and it must
never be quoted as one.

**[FACT, §5.1]** Training data: ≈16,000 chord progressions, over 1M chord instances, from ChoCo
(>20,000 tracks, 18 datasets), parsed to JAMS and converted to Harte notation.

### Structure segmentation — Chapter 6

**★ [FACT, §6.1.1] IT IS SECTIONAL FORM SEGMENTATION, NOT HARMONIC BOUNDARY SEGMENTATION**, and the
thesis draws the distinction itself: musical form study *"can be divided in two main categories:
phrase-structure segmentation and global segmentation"*, and from that point *"we refer to global
music structure segmentation as music structure segmentation"* — *"identifying and labelling key
music segments (e.g. chorus, verse, bridge)"*. Also: *"A correct segmentation does not necessarily
assign the correct labels to each section … but rather focuses on the correct estimation of the
boundaries of each section."*

**[FACT, §6.1.3]** Data: the **Billboard** dataset, **889 expert-annotated tracks**, chords in Harte
format with section labels; 80 unique section labels reduced to **11**. Model: a stacked **LSTM**, 5
layers, hidden dimension 256, dropout 0.2, binary cross-entropy.

**[FACT, §6.1.4] Table 6.2, pairwise precision/recall/F1 and the entropy-based under/over-segmentation
scores, all via `mir_eval`:**

| Model | P | R | F1 | S_U | S_O | S_F1 |
|---|---|---|---|---|---|---|
| FORM_raw | **0.673** | 0.337 | 0.420 | 0.673 | 0.337 | 0.420 |
| FORM_simple | 0.663 | 0.340 | 0.423 | 0.663 | 0.340 | 0.423 |
| fasttext | 0.616 | 0.604 | 0.596 | 1 | 1 | 1 |
| pitchclass2vec | 0.617 | 0.591 | 0.586 | 1 | 1 | 1 |
| **rdf2vec** (the ontology-only embedding) | 0.619 | 0.584 | **0.581** | 0.962 | 0.926 | 0.944 |
| **meta-embedding** | 0.624 | **0.608** | **0.598** | 1 | 1 | 1 |

**[FACT, §6.1.2]** FORM is named as *"the only approach proposed in literature for global music
segmentation on symbolic harmonic content"* — a suffix-tree method over chord strings, re-implemented
by the author for comparison.

**[FACT, §6.1.4] Label leaking is identified and addressed:** the embeddings were retrained from
scratch on a ChoCo subset **with the whole Billboard dataset removed**, because training embeddings on
Billboard could leak section information.

**[FACT, §6.1.4]** Against audio: *"State-of-the-art results are obtained by approaches based on
Convolutional Neural Networks, with a pairwise F1 scores of 58.09 ± 15.77 which is a similar result to
the one obtained on Table 6.2."* **The thesis reports no variance for its own figures**, so the
"similar result" comparison is against a mean with a ±15.77 spread and no significance test.

**★ [OBSERVATION — FLAGGED, NOT ASSERTED AS AN ERROR] Three of the six models score exactly 1.000 on
all three entropy-based measures (S_U, S_O, S_F1) while their pairwise F1 sits near 0.59.** The thesis
does not remark on it. It is recorded here because the thesis's own Figure 6.3(c) warns that
*"Pairwise metrics can be misguiding in absence of S_O and S_U"* — so the measures brought in as the
corrective are the ones reading saturated. **This side has not established a cause and does not claim
one; a reader relying on those columns should look at them before quoting them.**

### Theory and conjecture

**[THEORY]** Modal Harmony Theory itself, and the OWL/description-logic machinery (rolification,
EL/DL profiles) are established published work applied here, not established by this thesis.

**[CONJECTURE, ch. 7–8]** Extending MHO to model melodies; expanding the Roman-notation query into a
proper annotation system; using the embeddings to enhance automatic chord transcription and
cover-song detection. All stated as future work.

**[FACT, ch. 7 footnote]** Two further Polifonia artefacts are named: the **Modal Tonal ontology** and
the **Tonalities pilot**. **Neither is read**, and neither is added to the population here.

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** **chord LABELS in Harte notation** and nothing else. **No notes, no score, no
metre, no voices, no key, no segmentation.** For the ontology's classification: a chord expressed
through the Chord Ontology (root plus intervals). For the Roman-notation query: the chord progression
alone — explicitly *not* a reference scale. For the segmentation model: a chord sequence plus section
labels for training.

**HANDS downstream:** a SPARQL-queryable knowledge graph; per-chord role classifications within a
named scale; **an unranked, unweighted enumeration of scale readings with their Roman annotations**;
chord embedding vectors; and, from Chapter 6, section boundaries and labels. **No confidence and no
mass on anything.**

**ITS OWN STATED SCOPE:** Western tonal and modal music at the **chord-label level**; the
Roman-notation inference is a proof of concept handling simple notations only; the segmentation
evaluation is **popular music** (Billboard). It infers no chord from notes and estimates no key.



# EXTRACT — Nápoles López, Feisthauer, Levé & Fujinaga 2020, "On Local Keys, Modulations, and Tonicizations" (DLfM 2020) — population row 13, first pass (single pass; not central)



## Claims, labeled

- **[FACT — §5]** Evaluated symbolic local-key models track TONICIZATION-level ground truth
  better than MODULATION-level ground truth — "an inclination toward the tonicization
  predictions… unexpected, as most researchers do not describe their local-key-estimation models
  as 'tonicization finders'."
- **[FACT — §2]** The same music yields TWO defensible onset-level key ground truths (a
  modulation column and a tonicization column), and annotation traditions differ enormously in
  how much they tonicize (41.63% of onsets in Rimsky-Korsakov's textbook vs 15.97% Tchaikovsky
  vs far fewer in three others).
- **[FACT — §2]** The proposed scoring is duration-weighted with either exact-match or graded
  MIREX weights (dominant/subdominant 0.5, relative 0.3, parallel 0.2); graded weighting adds
  roughly 10–20 points.
- **[FACT — theory, quoted from Kostka & Payne]** "The line between modulation and tonicization
  is not clearly defined in tonal music." — carried by the paper as its framing premise.
- **[FACT — §3]** A released CC BY dataset exists: 201 textbook excerpts, 2,002 labels, dual
  modulation/tonicization annotations (github.com/DDMAL/key_modulation_dataset).
- **[CONJECTURE — §4.3]** That the models would do better trained on this data — stated, dataset
  too small to test.

## Coupling facts (mandatory)

- **Assumes upstream (of the methodology):** a symbolic score, a model emitting one local key
  per onset, and roman-numeral-bearing annotations from which the two ground-truth columns are
  derived.
- **Hands downstream:** a per-onset dual-column evaluation with duration weighting and graded
  key-distance credit.
- **Stated scope:** evaluation methodology and dataset; three models compared untrained;
  tonicization columns partly supplied by the authors where textbooks omitted numerals.

## Measured results

As relayed (approximate, Figure 3): M1/M3 similar shape and better on tonicization columns; M2b
worst and modulation-leaning; exact values not carried.



# EXTRACT — McLeod & Rohrmeier 2021, "A Modular System for the Harmonic Analysis of Musical Scores using a Large Vocabulary" (ISMIR 2021) — population row 1, CENTRAL, first pass



## Claims, labeled

- **[FACT — Table 1]** On the authors' internal corpus (742 pieces), the modular system (best
  variant CSM-T) reaches CSR root 77.6 / root+type 70.0 / +inversion 62.8 / key 70.2 / full 46.9
  against the end-to-end baseline (Micchi, Gotham & Giraud 2020) at 57.0 / 47.7 / 37.6 / 64.9 /
  29.0. On the Functional-Harmony corpus (201 pieces): CSM-T full 45.9 vs baseline full 42.8.
- **[FACT — Table 1 + discussion]** The end-to-end baseline's KEY column is competitive with the
  modular system's (64.9 vs 66.9–70.2 internal) while its chord columns are far behind; the
  authors' own diagnosis, verbatim: *"the key depends on outputs from the other components,
  adding noise to the process, which isn't a factor for the end-to-end baseline."*
- **[FACT — §system]** The chord label is decided HOLISTICALLY over 1540 whole symbols, not as
  separate root/type/inversion heads, with the stated reason that separate per-field outputs can
  combine inconsistently.
- **[FACT — §system]** Segmentation is part of the search: beam search ranges over segmentations
  consistent with the transition model's thresholds, jointly with chord and key labels; a merge
  rule was added because the transition model OVER-SEGMENTS and its thresholds were hard to tune.
- **[FACT — §system]** Applied chords are represented as brief, potentially recursively embedded
  KEY CHANGES, not as a separate chord-label field.
- **[FACT — §results]** Chord-vocabulary invariance in the sequence model (CSM-I/CSM-T) helps
  mainly the KEY column, on the smaller F-H corpus (full 40.5 → 45.9); on the internal corpus the
  three variants sit within ≤2.0 CSR.
- **[FACT — §results]** Inversion accuracy falls steeply below root position: 71.5 / 54.4 / 38.3
  / 40.5 (root/1st/2nd/3rd).
- **[FACT — §scope]** The output lacks suspensions, altered chordal tones and pedal tones by the
  paper's own statement; these are named future work.
- **[THEORY]** None carried — the paper is a system-and-measurement paper; its design arguments
  are positions, not established theory.
- **[CONJECTURE — §discussion]** That modules can be retrained per input format (MIDI/audio:
  retrain CTM+CCM only) while the rest carries over — stated, not measured.

## Coupling facts (mandatory)

- **Assumes upstream:** a SPELLED symbolic score (A♯ ≠ B♭), polyphonic, notes with octave,
  onset/offset, duration, and METRICAL LEVELS (downbeat/beat/sub-beat/other) already present; no voice
  membership required. Quantization implicit.
- **Hands downstream:** a segmentation (chord windows), an absolute chord symbol (spelled root,
  type, inversion) per segment, a local key (spelled tonic, mode) per segment. No chord-tone
  assignment, no elaboration relations, no rivals published (beam holds alternatives during
  search and commits one)
- **Stated scope:** notated Western tonal repertoire, 16th–20th c. corpus; Roman-numeral-style
  ground truth; suspensions/alterations/pedals excluded from the label space.

## Measured results (corpus, metric, value)

See Table 1 as carried in the fetched content record: CSR at five widths, two corpora, the
Micchi et al. 2020 baseline and three CSM variants; inversion-position accuracies; minor 44.6 vs
major 40.9 CSR.



# EXTRACT — BACHI (arXiv:2510.06528v2), boundary-aware symbolic chord recognition — population row 12, first pass (single pass; not central)



## Claims, labeled

- **[FACT — §architecture]** Boundaries are a SEPARATELY SUPERVISED signal (binary boundary
  sequence predicted by an MLP) that CONDITIONS the encoder by feature-wise modulation — not a
  decoded variable of the labeling search.
- **[FACT — §architecture]** The chord label is factored root × quality × bass and filled by
  confidence-ordered masked iterative decoding (three commits, highest confidence first, no
  autoregression).
- **[FACT — §results]** On a ~1,500-piece classical corpus (When-in-Rome + DCML, converted to
  absolute labels): full-chord macro-accuracy 68.1 vs Harmony Transformer v2 62.1, ChordGNN
  58.5, AugmentedNet 57.2, rule-based 28.4. On corrected POP909-CL: 82.4 vs 82.2 (HT v2).
- **[FACT — §ablation]** The boundary and iterative-decoding machinery moves the FULL-chord
  (joint-consistency) column (66.1 → 68.1) while the per-element columns barely move — the gain
  is coherence between the separately-predicted elements, not per-element accuracy.
- **[FACT — §discussion]** The learned decoding ORDER differs by repertoire: quality-first
  chains dominate on classical (33.2% quality→root→bass), bass-first on pop (56.4%
  bass→root→quality).
- **[FACT — §data]** The original POP909 annotations carried large systematic defects (40.6%
  start-beat misalignment; 14.2% missing key-signature changes)
- **[CONJECTURE — §discussion]** That the human-ear-training analogy explains the gains —
  interpretive framing, not measured causation.

## Coupling facts (mandatory)

- **Assumes upstream:** an UNSPELLED piano-roll (MIDI pitch, 88 keys, quantized 12 frames/beat).
  No spelling, no voice membership, no metrical strength input relayed.
- **Hands downstream:** absolute chord labels (root, quality, bass) per frame/segment; no key
  output in the main system (a key-detection variant ablated at 67.6); no rivals, no chord-tone
  assignment.
- **Stated scope:** pop and classical symbolic corpora, absolute chord labels (not Roman
  numerals, not tonality-bearing analysis).

## Measured results

Tables in the fetched content record (two corpora × five systems × four columns; ablations).



# EXTRACT — Hentschel, Moss, McLeod, Neuwirth & Rohrmeier 2021, "Towards a Unified Model of Chords in Western Harmony" (MEC 2021) — population row 3, CENTRAL, first pass



## Claims, labeled

- **[FACT — §model]** The model keeps generic, spelled and enharmonic pitch classes as DISTINCT
  TYPES with one-directional conversion (spelled → enharmonic/generic, never back), and treats
  octave and enharmonic equivalence as explicit flags — never destructive normalization.
- **[FACT — §model]** Mode is a first-class interval collection (named diatonic modes AND
  arbitrary interval sets), and a key is tonic + mode + an optional hierarchy type
  (global/local/secondary).
- **[FACT — §model]** A chord is a graph over explicit properties; theories that specify less are
  still representable, with missing properties induced only where derivable.
- **[FACT — §model]** Suspensions are representable as per-note functions naming what is
  suspended; non-chord tones are ignorable per annotation standard.
- **[FACT — §scope]** This paper does NOT discuss the cadential six-four as a standards
  flashpoint.
- **[THEORY]** The representational distinctions themselves (spelled vs enharmonic pitch,
  scale degree vs interval) are standard music theory formalized, not new claims.
- **[CONJECTURE — §future]** That the model can serve as a generalized interchange standard —
  offered as "a first step," unmeasured.

## Coupling facts (mandatory)

- **Assumes upstream:** nothing computational — it is a REPRESENTATION, not an algorithm; it
  assumes only that "chord" as a pitch collection is meaningful in the style.
- **Hands downstream:** a typed representation whose queries (graph patterns) can express
  musicological questions; conversion/induction operations between levels.
- **Stated scope:** Western harmony broadly (classical, jazz, rock, pop annotation standards);
  explicitly not exhaustive.

## Measured results

None — no experiments; a representation paper.



# EXTRACT — McLeod & Rohrmeier 2024, "Detecting chord tone alterations and suspensions" (JNMR 52(5)) — population row 2, CENTRAL, first pass



## Claims, labeled

- **[FACT — §method]** The method takes the chord label AS GIVEN — "takes as input a chord label
  (and the notes present in the score for the duration of that label)" — with boundaries, root,
  quality, inversion and a local-key major/minor flag all upstream inputs; it is offered as "a
  post-processing step given the output of any harmonic analysis model."
- **[FACT — §method]** Its stated ground for deriving alterations AFTER a base chord rather than
  enlarging the label space: an alteration feature multiplies vocabulary size and "reduces the
  possible training data per label and weakens predictive power."
- **[FACT — §results]** With ground-truth chords, per-note chord-tone detection reaches 89.2%
  overall (full vocabulary) vs 76.1% for a heuristic baseline (p < .001); under NOISY upstream
  chords (the 2021 system's classification module) it holds 73.2% vs 61.1%.
- **[FACT — §results]** Accuracy on the NON-DEFAULT pitch classes — the alterations themselves —
  is low in absolute terms in every condition (28.8–39.2% for the method; the baseline is
  sometimes higher on that column while far lower overall).
- **[FACT — §results]** Vocabulary reduction costs the method only ~4% under noisy input against
  ~11% under ground-truth input — the stated robustness result.
- **[FACT — §positioning]** Differences from Ju et al. 2017 as the paper states them: Ju et al.
  need four-part chorales, use 12 unspelled pitch classes (vs 35 spelled), and take no hypothesis
  chord label as input.
- **[CONJECTURE — §future]** That explicit search for suspension resolutions would improve
  performance; that reduced-vocabulary labeling plus inferred alterations may improve overall
  label accuracy — both stated as intent/possibility, not measured.

## Coupling facts (mandatory)

- **Assumes upstream:** a completed harmonic analysis — segmentation, chord root/quality/
  inversion, and local-key mode — plus the spelled score for the label's duration. This is the
  load-bearing coupling fact: **the method cannot run before the chord decision and does not
  revise it.**
- **Hands downstream:** per-note chord-tone/non-chord-tone decisions, merged pitch-class vectors,
  and an enriched chord label carrying added/replaced tones and suspensions.
- **Stated scope:** Western tonal repertoire of the 924-piece corpus (Beethoven, Mozart, Corelli,
  internal); alterations defined by example rather than formally; failure under substantially
  wrong chord labels not deeply analyzed; joint-versus-sequential deciding of chord and tones not
  taken up beyond a practical justification of the sequential shape.

## Measured results (corpus, metric, value)

924 pieces (ABC + Mozart Sonatas + 36 Corelli trio sonatas + internal), 80/10/10; per-note
accuracy split default/non-default/overall; six conditions (3 vocabularies × ground-truth/noisy);
full table in the fetched content record.



# EXTRACT — Sapp 2005, "Visual Hierarchical Key Analysis" (keyscapes) — population row 17, CENTRAL, first pass



## Claims, labeled

- **[FACT — §method]** The keyscape computes a key estimate at EVERY window size at once
  (beat-to-whole-piece, sliding, centre-plotted) and displays them as one triangular picture —
  there is no committed segmentation anywhere in the method.
- **[FACT — §examples]** A single whole-window analysis can hide structure a split reveals
  (Schubert case: A major r 0.86 over F♯ minor r 0.78 across a real two-key form) — the paper's
  own ground for multi-resolution.
- **[FACT — §examples]** Key-profile CHOICE changes the reading materially: Krumhansl weights
  over-emphasize the dominant key, Aarden's the subdominant; on Bach BWV 1007 the
  Krumhansl-profile whole-piece key is wrong (D major for G major) and Aarden's is right.
- **[FACT — §evaluation]** The paper carries NO systematic accuracy measurement — validation is
  qualitative against a handful of worked pieces.
- **[THEORY]** The foreground/background hierarchy analogy (Schenker; Lerdahl & Jackendoff) is
  adopted framing, not established by this paper.
- **[CONJECTURE]** That stable colour regions indicate analytic certainty and colour shifts
  modulation boundaries — an interpretive reading of the picture, unmeasured.

## Coupling facts (mandatory)

- **Assumes upstream:** a note stream with durations (histogram per window); no spelling
  requirement stated; no meter or voice needs.
- **Hands downstream:** a picture — thousands of window-key estimates; NOT a decided analysis:
  no boundaries, no committed keys, no chords, no uncertainty calculus beyond r-values.
- **Stated scope:** visualization/exploration of Western art music; explicitly not an evaluated
  key-detection system.

## Measured results

None systematic (see fetched record for the worked examples' numbers).



# EXTRACT — de Haas, Magalhães, Wiering & Veltkamp 2013, "Automatic Functional Harmonic Analysis" (HarmTrace; CMJ 37(4)) — population row 5, CENTRAL, first pass



## Claims, labeled

- **[FACT — §model]** HarmTrace consumes chord LABELS plus a GIVEN key and never sees notes or
  voicing ("For simplicity, we ignored voice-leading"); its output is a functional parse tree
  over those labels.
- **[FACT — §model]** Modulation is EXCLUDED from the shipped grammar, on the paper's own
  measured-ambiguity ground, verbatim: "even with a constrained modulation specification that
  allows modulation only to specific other keys, and restricts the number of modulations, the
  total number of ambiguous analyses quickly explodes." Only parallel-mode change (root fixed)
  is expressible; multi-key pieces are to be pre-segmented by an external key finder.
- **[FACT — §parsing]** Error-correcting parsing (delete/insert to depth three, fewest
  corrections preferred) makes the parser total: on 5,028 real-world sequences it "never crashes
  or refuses to produce valid output" (3.38 deletions, 9.85 insertions per song; deleted chords
  under 6% of chords parsed).
- **[FACT — §evaluation]** The analyses themselves are NOT evaluated against ground truth — only
  parse statistics and worked examples; "we evaluate its parsing performance."
- **[FACT — §model]** Ambiguity is managed by constraining rule application (typed grammar,
  precedence), with residual multiple analyses accepted and exponential growth acknowledged.
- **[THEORY]** The grammar's basis — Riemann's three functions; Rohrmeier's generative syntax
  (2007, 2011); hierarchical recursion — is established published theory adopted, not
  established here.
- **[CONJECTURE]** Applicability beyond the jazz-biased corpus (a Bach chorale is shown, no
  measurement).

## Coupling facts (mandatory)

- **Assumes upstream:** the tonality (key) DECIDED, and the chord labels DECIDED — a completed
  chord-level analysis; single-key stretches (or an upstream segmentation into them).
- **Hands downstream:** a hierarchical functional reading over given labels; corrected
  (deleted/inserted) chords as a byproduct.
- **Stated scope:** label-level functional analysis, jazz-biased vocabulary, no modulation, no
  inversions/voicing concern, phrase structure deferred to post-processing.

## Measured results (corpus, metric, value)

Parse statistics on 72 and 5,028 sequences (table in the fetched content record); runtime
10 ms / 76.5 ms per song. No harmonic-accuracy measurement.



# EXTRACT — de Berardinis et al. 2023, "ChoCo" (Scientific Data 10) — population row 8 (with the Polifonia ontology members it carries), first pass (single pass; not central)



## Claims, labeled

- **[FACT — §workflow]** Converting Roman numerals to absolute chord labels LOSES the
  functional information, and ChoCo's own rule is therefore ADDITIVE — the converted annotation
  is added beside the Roman-numeral original, never replacing it ("the Roman Numerals contain
  information that would otherwise be lost").
- **[FACT — §workflow]** Cross-notation conversion is acknowledged one-of-several-possible —
  "the generated conversion, although correct, may only be one of several possible conversions."
- **[FACT — §data]** Scale of the integration: 18 datasets, 20,086 files, 1.58M chord
  occurrences, 7,281 unique chord classes, dual audio/symbolic time bases in one JAMS schema;
  RDF via the JAMS Ontology + Roman Chord Ontology (Polifonia Ontology Network).
- **[CONJECTURE]** None carried — a resource paper.

## Coupling facts (mandatory)

- **Assumes upstream:** existing annotation datasets; per-family parsers.
- **Hands downstream:** one harmonized corpus + knowledge graph; additive multi-notation
  annotations.
- **Stated scope:** representation and integration; no analysis algorithm, no evaluation of any
  analysis.



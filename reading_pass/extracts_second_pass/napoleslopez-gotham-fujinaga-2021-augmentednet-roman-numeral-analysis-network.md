# Second extraction — Nápoles López, Gotham & Fujinaga, "AugmentedNet: A Roman Numeral Analysis Network with Synthetic Training Examples and Additional Tonal Tasks"

**What this file is.** An independent second extraction of the paper held at
`docs/research_papers/napoleslopez_gotham_fujinaga_2021_ismir_augmentednet.pdf`, written under the
second-pass rule of `cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet: a CENTRAL source
is extracted in a second independent pass that does not consult the first extract, and the two extracts
are then cross-checked, disagreements being resolved at the paper or recorded as unresolved.

**The paper is row 48 of Task B's L2 slice.** It was the next member owed in the read order the
hundred-and-eightieth handoff entry publishes at its head item (1) — 48, then 49, 50, 52, 46 — and it
was taken for that reason and not for its length.

**Locations in this file are given by the paper's own printed section number, table number or figure
number, and by the PRINTED page number where one is useful — never by a coordinate of this read's
own.** The printed pages run 404 to 411 and the PDF pages run 1 to 8; where both are meant, both are
given.

---

## §0 — What was read, and the bound on this read's independence

**Read at the object, by this side, in this sitting:**

- The whole paper, all eight PDF pages, as page images: pages 1–4 in one request and 5–8 in another.
  Every image was checked for presence and legibility at the image itself, not at the call's success
  line (the standing page-image caution).
- The page count was established AT THE TOOL by a deliberately out-of-range request, which answered
  *"PDF has 8 pages"*. The progress record's own row is relayed by the hundred-and-eightieth entry as
  eight pages, so the tool's answer MATCHES that figure — a match, not a source. This side did not open
  the progress record.
- The held file's size, **773,071 bytes**, established at this sitting's own staging call, matching the
  figure the hundred-and-eightieth entry records from its own directory listing.
- A listing of `reading_pass/extracts_second_pass/`, which established that no second extract for this
  paper existed before this sitting — so the member was owed at the folder, and not merely on the
  progress record's say-so.

**NOT read, not searched, not staged, by this side:** this paper's first extract (opened only at step 7
of the eight-step procedure, after this file's §0 to §8 had landed); `FRAMEWORK.md`; `population.md`;
the slice derivation; the findings surface; `docs/research_papers/BIBLIOGRAPHY.md`;
`reading_pass/candidacy_upgrades.md`; `reading_pass/l2_slice_reading_progress.md`; and every other
paper and every other extract's content. **No sweep of the repository was run for this paper** — not
for its authors, not for its title, not for any of its values.

**THE INDEPENDENCE BOUND, STATED AND NOT CLAIMED AWAY.** This side booted on the hundred-and-eightieth
handoff entry, which names this paper's authors, venue, year, title, page range, licence, page count
and held-file size, and states that it is symbolic-input-only and spelled, CENTRAL, and owed a second
pass. That is contamination on the IDENTITY axis and it is written down here rather than denied. What
that entry does NOT carry, and what this read therefore reached on its own: any value printed in this
paper, any claim it makes, any defect in it, and any conclusion of its first extract. The first extract
was not opened until after this file's §0 to §8 had landed.

**A second bound, on the neighbouring member.** The immediately preceding sitting extracted row 45 —
Micchi, Gotham & Giraud 2020, *"Not All Roads Lead to Rome"* — and this paper's reference [20] IS that
paper, cited by this paper as the basis of its input representation, its transposition scheme, its six
conventional tasks and their class counts, and as one of the models it compares against. This side read
the hundred-and-eightieth entry whole and therefore carries that entry's account of row 45. **Every
statement in this file about the Micchi et al. paper is taken from what THIS paper prints about it, at
this paper's own pages, and from nowhere else**; no claim is made here about what the Micchi et al.
paper itself says, and row 45's extracts were not opened.

---

## §1 — What the paper is, and the identity axis

**Title, as printed on page 1:** "AUGMENTEDNET: A ROMAN NUMERAL ANALYSIS NETWORK WITH SYNTHETIC
TRAINING EXAMPLES AND ADDITIONAL TONAL TASKS".

**Authors and affiliations, as printed on page 1:**

- Néstor Nápoles López — McGill University, CIRMMT — nestor.napoleslopez@mail.mcgill.ca
- Mark Gotham — Universität des Saarlandes — mark.gotham@uni-saarland.de
- Ichiro Fujinaga — McGill University, CIRMMT — ichiro.fujinaga@mcgill.ca

**Venue, licence and pagination, as printed.** The foot of page 1 carries the Creative Commons mark and
the sentence *"© N. Nápoles López, M. Gotham, and I. Fujinaga. Licensed under a Creative Commons
Attribution 4.0 International License (CC BY 4.0)."*, followed by a labelled **Attribution:** line —
*"N. Nápoles López, M. Gotham, and I. Fujinaga, "AugmentedNet: A Roman Numeral Analysis Network with
Synthetic Training Examples and Additional Tonal Tasks", in Proc. of the 22nd Int. Society for Music
Information Retrieval Conf., Online, 2021."* Pages 2 through 8 carry the running header
**"Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021"**. Printed page numbers run
**404** (page 1) to **411** (page 8), one per page, at the foot.

**THE IDENTITY AXIS CLOSES AT THE PAPER'S OWN FACE, WITH ONE ABSENCE NAMED.** The document establishes
at its own face: its title, all three authors, their affiliations and contact addresses, the venue and
its dates, the year, the licence, the attribution string and its own page range. **No DOI is printed in
the eight pages as read**, and no submission or acceptance date is printed in them either. Nothing on
this axis required the record's own account of the paper. **Against what the hundred-and-eightieth
handoff entry records of this row — the three authors, ISMIR 2021, the title, pp. 404–411, CC BY 4.0,
symbolic-and-spelled input, eight pages — every item is confirmed at the paper's own face by this
read.** No other account of this paper was consulted.

**A code and data release is stated in the paper's own §1:** *"we release all of our preprocessed
datasets, data splits, experiment logs, and the full source code of our network at
https://github.com/napulen/AugmentedNet."* **This side did not visit that address** — no web access was
made at any point — so nothing about what is there is asserted.

**The input is symbolic and spelled, established at the paper.** The network's inputs are a spelled
bass note and spelled chroma features sampled from the score at regular note-duration values (§3.1).
**Audio is met nowhere in the method as described in the eight pages as read.** *(Stated exactly: the
word "audio" does occur in those pages — in §1's general framing of ACR systems, and in the title of
reference [7] — but at no point in the paper's account of its own inputs, which are §3.1's. No search of
the paper for the word was run; this is a statement about the method sections as read, not a count of
occurrences.)* The outputs carry pitch spelling as
well: the key task distinguishes enharmonic keys, and the chord-root and bass tasks have 35 classes
each, described by the paper as "a pitch spelling".

---

## §2 — The method, as the paper states it

### §2.1 The problem as the paper frames it

The paper's §1 distinguishes **Automatic Chord Recognition (ACR)** from **functional harmony**: ACR
systems "typically seek to predict the root and quality of the chords throughout a piece via either an
audio or a symbolic representation", whereas functional harmony "requires other adjacent tasks to be
solved simultaneously, notably including the detection and identification of key changes (modulations
[1,2]) and tonicizations [3]".

It states the compactness argument for Roman numeral annotation and gives its own worked example:
*"For instance, an annotation like **C:vii^o6/V** encodes the local key (C-major), quality of the chord
(diminished triad), chord inversion (first), and any existing tonicization (G-major)."*

It then states the decomposition that the whole architecture rests on: *"This 'modular' nature of Roman
numeral annotations has been beneficial to MIR research. In recent years, functional harmony has been
approached by dividing the main task in several sub-tasks. Thus, as a machine learning problem,
functional harmony can be expressed as the task of correctly predicting sufficient sub-tasks to
reconstruct the full Roman numeral label."*

And it states the standing position of the field, in its own words: *"Yet, despite these developments
and the growing interest in the field, the performance of functional harmony models for predicting
Roman numeral labels remains relatively low."*

### §2.2 The lineage the paper places itself in (its §2)

The paper's related-work section is short and its claims are attributions rather than measurements.
Transcribed for what it attributes to whom:

- *"For a summary of general ACR strategies, see Pauwels et al. [7]."*
- *"The first computational works on Roman numeral analysis were by Winograd [8] and Maxwell [9]."*
- *"Later, the independent efforts by Temperley, Sleator, and Sapp led to the first end-to-end automatic
  Roman numeral analysis system: a program named Melisma [10–12]."*
- *"Notable subsequent studies include Raphael and Stoddard [13], Illescas et al. [14], and Magalhães
  and de Haas [15], who proposed Hidden Markov Models (HMMs), dynamic programming, and grammar-based
  approaches, respectively."*
- *"Chen and Su [6] were the first to introduce 'multitask learning' (MTL) [16] to the problem as a
  suitable way for the neural network to share representations between related tonal tasks."* Their
  model is described as "a bidirectional LSTM [17] followed by task-specific dense layers"; the same
  work "introduced the 'Beethoven Piano Sonata Functional Harmony' dataset".
- *"The MTL layout outperformed single-task configurations, and it has continued to be the best-performing
  approach in subsequent deep learning studies."*
- The same authors "have adopted Transformer-based networks to deal with functional harmony and ACR
  [18,19]", work that "has explored the capability of attention mechanisms to improve the performance of
  ACR, paying special consideration to chord segmentation and its evaluation".
- *"Micchi et al. [20], in turn, proposed a convolutional recurrent neural network (CRNN)"*, whose
  recurrent component is "a bidirectional GRU [21] connected to task-specific dense layers, similar to
  those of Chen and Su [6]"; in their experiments "a DenseNet-like [22] convolutional component
  outperformed other configurations (e.g., dilated convolutions or a GRU with pooling)".
- On pitch spelling, attributed to Micchi et al.: they *"demonstrated the positive effect of using pitch
  spelling in the inputs and outputs. This confers at least two advantages: it provides a more
  informative output (e.g., not only the correct key, but the correct spelling between two enharmonic
  keys), and it increases the theoretical number of transpositions available for data augmentation."*

The paper's own placement, verbatim: *"Here, we propose improvements along the line of CRNNs. Due to
our focus on extended data augmentation and tonal tasks, we named our network AugmentedNet."*

**Note for a reader of this record.** Reference [20] is *Micchi, Gotham and Giraud, "Not all roads lead
to Rome: Pitch representation and model architecture for automatic harmonic analysis," Transactions of
the International Society for Music Information Retrieval, vol. 3, pp. 42–54, 2020* — transcribed from
this paper's own reference list, page 7. That is the paper this line extracted as row 45. **This file
takes no position on what that paper says**; it records only that THIS paper names it as the design it
is closest to and the representation it modifies.

### §2.3 The three things the paper says are new in the architecture

§3, first paragraph, verbatim: *"The AugmentedNet is a similar network in size and design to the one by
Micchi et al. [20]. It is characterized by a different layout of the convolutional layers, a new
representation of pitch spelling, and a separation of the bass and chroma inputs into independent
convolutional blocks."*

So three architectural differences are claimed against [20], and two further contributions are claimed
elsewhere: the five additional MTL tasks (§3.4.1) and the texturized synthetic training data (§3.5.2).

### §2.4 Time encoding — the reference note per timestep

§3.1, verbatim: *"The input to the network consists of a sequence of timesteps, which are sampled from
the score at symbolically regular note duration values. In this study, we use the thirty-second note
('demisemiquaver') as this atomic value (i.e., eight timesteps per quarter note in the score), in order
to match the most fine-grained frame sampling seen in previous work. The length of the sequence is set
by a fixed number. Following Micchi et al., we set that number at 640 frames (or 80 quarter notes) per
sequence example."*

So: **one timestep = one thirty-second note; eight timesteps per quarter note; 640 timesteps per
sequence example; 80 quarter notes per sequence example.**

§3.3 adds the constraint that fixes what the model emits: *"Throughout the entire network, the
dimensionality of the timesteps axis remains constant. That is, our input and output sequences have the
same length, and the model predicts one Roman numeral label per timestep."*

### §2.5 Pitch encoding — the 19-feature two-hot vector

§3.1, verbatim: *"The representation of each timestep is conceptually the same as in Micchi et al. [20],
a vector containing a spelled bass note and spelled chroma features. However, the length of our vectors
is different. In the Micchi et al. representation, each timestep has 70 features: 35 for the bass and 35
for the chroma features. We consolidate this information in 38 features: 19 for the bass, and 19 for the
chroma features. The reduction in number of features is due to an alternative encoding of pitch spelling,
which we explain below."*

And the encoding itself, verbatim: *"We split the representation of a pitch spelling into two components:
the pitch class (0–12) and the generic note letter (A–G). Each spelled pitch thus leads to a two-hot
encoded vector with 19 features (1 of 12 pitch classes, and 1 of 7 note names). This reduces the number
of parameters in the network without any observable compromise in performance. Furthermore, the spelled
bass and chroma inputs are connected to the network separately, in their own convolutional blocks. The
input to each block is a tensor of pitch spelling sequences."*

*(The printed range **(0–12)** against the printed count **1 of 12 pitch classes** is treated at §7.1.)*

### §2.6 The convolutional block

§3.2 gives the design rationale and the mechanism. The rationale, verbatim: *"Using the feature maps of
previous layers as an input to a convolutional layer has proven beneficial, for instance, by
strengthening feature propagation and reducing the number of parameters [22]. Moreover, DenseNet-like
architectures have shown to work well for the specific task of functional harmony [20]."*

The observation that drives the layout, verbatim: *"In our preliminary experiments, we noticed that
different tonal tasks have different time dependencies. For example, losing information about a specific
timestep often leads to poor performance in predicting the inversion, whereas losing long-term context
hinders the performance in key estimation."*

The mechanism, verbatim: *"Our architecture implicitly prioritizes short-term dependencies in the initial
convolutional layers, by having more filters and covering less timesteps. Going further, the convolutions
provide more context about future timesteps, but output less filters. These increments (in window size)
and decrements (in number of filters) are done in powers of 2. Using six convolutional layers in each
block (as shown in Figure 1), the first layer convolves a window of a single timestep (a thirty-second
note), whereas the sixth layer utilizes a window of 32 timesteps (a whole note). The output shape of each
block is the original length of the sequence, with 82 features per timestep."*

Figure 1's caption states the same rule mechanically: *"A convolutional block has six 1D convolutional
layers. Each layer doubles the length of the convolution window and halves the number of output filters."*

### §2.7 Dense and recurrent layers

§3.3, verbatim: *"Two time-distributed dense layers are applied to the concatenated outputs of the
convolutional blocks. The dense layers help to reduce the number of features before the GRU layers.
These have 64 and 32 neurons, respectively. Two bidirectional GRU [21] layers are applied after the
second dense layer. Both GRU layers return outputs at every timestep."*

### §2.8 The multitask layout and its eleven tasks

§3.4, verbatim: *"The output of the network follows an MTL approach with hard parameter sharing, similar
to the one by Chen and Su [6]. For each of the output tasks, a time-distributed dense layer is attached
to the second GRU and used to predict its corresponding task. In the past, MIR researchers have
reconstructed Roman numeral annotations using six tasks: the (local) key, the primary and secondary
degrees, the chord quality, the chord inversion, and the chord root [6,20]. In our network, these six
'conventional' tasks are learned as well, plus five new additional ones."*

On the class counts, verbatim: *"All the conventional tasks, except for the key, have the same number of
output classes described by Micchi et al. [20]. The key includes four additional classes: {F♭, G♯, d♭,
e♯}. These were included because our dataset, larger than previous ones, revealed modulations reaching
G♯ major. Thus, the number of allowed key signatures was extended by one sharp and one flat, in both
modes."*

The MTL motivation, verbatim from §3.4.1: *"It is argued that MTL may improve the performance of a model
by preferring representations that are useful to related tasks, acting as an implicit form of data
augmentation and regularization method [16]."* And the paper's own hypothesis, verbatim: *"We
hypothesize that these additional tasks (e.g. pitch class sets) improve the accuracy of the model because
of the MTL layout, even if they are not explicitly used to predict the Roman numeral."*

The division of labour among the five new tasks, verbatim: *"One of these, CommonRNs, was used to design
an alternative method to reconstruct the full Roman numeral label. The remaining four are included to
strengthen the shared MTL layers."*

### §2.9 The five additional tasks, each as the paper defines it

- **CommonRNs.** *"during data exploration, we found that, when inversions were removed and synonyms
  (e.g., ♭II₆ and N₆) were standardized, a set of 75 Roman numeral classes spanned ~98% of all the
  annotations across the training set (see Table 1). This was a motivation to predict these classes
  directly as an additional task. The correct prediction of this new task is equivalent to predicting the
  primary and secondary degrees, chord root, and chord quality simultaneously. As an additional
  experiment (see Section 4.3), we tested an alternative new method to reconstruct the Roman numeral
  labels, using the key, inversion, and CommonRNs tasks. We refer to this method as RN_alt."*
- **Harmonic Rhythm.** *"a binary classification task that indicates whether a Roman numeral annotation
  starts at a given timestep. It may be relevant for chord segmentation."*
- **Bass.** *"a multiclass classification task that indicates the bass note in the Roman numeral label.
  This task has 35 output classes representing a pitch spelling, as in the chord root task [20]. It is an
  alternative chord inversion task."*
- **Tonicization.** *"a multiclass classification task that indicates a tonicized key implied by the
  Roman numeral label (if any). The output classes are 34 keys, as in the key task, and it is an
  alternative way to learn the secondary degrees."*
- **Pitch Class Sets.** *"a multiclass classification task that indicates the set of pitch classes
  implied by the Roman numeral chord. The number of classes (93) results from computing all pitch class
  sets in all diatonic triad and seventh chords, plus all augmented sixth chords in all keys. This task is
  related to the chord quality, primary degree, and to non-chord tones [23]."*

### §2.10 Data augmentation — transposition

§3.5.1, verbatim: *"As in most automatic tonal music analysis research, we transpose each piece to
different keys as a form of data augmentation. Particularly, we transpose to all the keys that lie
within a range of key signatures, in both modes. When we transpose a piece, we verify that all the
modulations within the piece fall in the target range of key signatures. This process of transposition
and data augmentation was introduced and described by Micchi et al. [20]. In our data exploration, we
found G♯ major to be the furthest key to the center of the line-of-fifths [24] in the training set.
Thus, we transposed each piece across the keys with 8-flats and 8-sharps in their key signatures."*

**The verification clause is the load-bearing one for a consumer of this method:** a transposition is
admitted only where every modulation inside the piece also lands inside the target range. That makes
the available transposition count piece-dependent, and no distribution for it is printed in the pages
as read.

### §2.11 Data augmentation — synthetic examples and texturization

§3.5.2, verbatim on the synthesis: *"In addition to transposition, we implemented a variation of a
previous data-augmentation technique by Nápoles López and Fujinaga [25]. Starting with the Roman numeral
analyses of our dataset, we synthesized 'new' training examples by realizing the chords implied by each
Roman numeral annotation. The synthesis was done using the music21 Python library [26], which converts
RomanText [4] files into scores of block chord realizations."*

Verbatim on why block chords were not enough: *"We found the default block chord texture of the
synthetic examples to be only slightly beneficial for the model, possibly because it did not capture the
complex texture of real keyboard music, for example. In order to account for this difference, we
artificially 'texturized' the generated training examples, departing from the default block chords. The
texturization was done by applying three note patterns recursively (see Figure 2). These patterns were
designed intuitively, pursuing certain goals in the resulting texture."*

The three patterns and the mixture, each verbatim:

- **Bass-split (measure 1):** *"a pattern where the original chord duration is divided by half, playing
  the bass in the first half, and the remaining notes in the second. The goal is to occasionally separate
  the bass from all other notes."*
- **Alberti bass (measure 2):** *"a 4-note melodic pattern with a pitch contour of low-high-middle-high.
  The goal is to occasionally play chords using a monophonic texture."*
- **Syncopation (measure 3):** *"a pattern where the highest note is played first, followed by the rest
  of the notes, played in syncopation. The goal is to occasionally shift the onset of the bass from the
  onset of the Roman numeral label."*
- **Mixture (measure 4):** *"we applied the three patterns randomly and recursively. For example, the
  mixture in measure 4 displays a bass-split pattern over the whole-note chord, followed by a syncopation
  pattern applied over the three upper notes, in the second half of the measure."*

The two constraints on the randomization, verbatim: *"As part of the randomization, some chords were
left unaltered (e.g., the anacrusis of Figure 2), and the patterns were applied across different
duration values. To constrain the depth of the recursion, we applied these patterns only to the slices
of the score that contained 3–4 simultaneous notes. This process resulted in the generation of 'new
pieces' that showed improvements in the learning process of the model, further than the block chord
synthetic scores."*

**Figure 2, as read.** Three systems labelled *a) original*, *b) synthesized (block chord)* and
*c) synthesized (texturized)*, in F minor, with the Roman numeral line under system (c) reading
**f: i — i — i — V6/5 — V6/5**, and the pattern names *bass-split*, *Alberti*, *syncopation* and
*mixture* printed above the measures they apply to. The caption, verbatim: *"An example of texturization.
The block chord texture (b) was synthesized using music21 [26] from an input RomanText file [4]. The
texturized output (c) was generated by recursively applying note patterns to the block chord scores. The
three musical patterns of bass-split, Alberti bass, and syncopation are indicated in measures 1–3,
respectively. The original music score (a) is shown for reference: mm. 1–4 of Beethoven's Piano Sonata
Op.2 No.1."*

### §2.12 The training procedure

§4.2, verbatim on epochs: *"We set a fixed number of 100 epochs in all experiments. We found that the use
of early stopping was unreliable to determine the end of the training process. Instead, we saved the
weights after each epoch. At the end, we selected the weights that maximized the mean accuracy across the
six conventional tasks."*

Verbatim on the other hyper-parameters: *"Each of the layers in the network is accompanied by batch
normalization [30] before the activation function. In the recurrent layers, we apply the batch
normalization after the activation function. All convolutional and dense layers use the rectified linear
unit (ReLU) as their activation function. However, the two GRU layers use a hyperbolic tangent. In all of
our experiments, we used 16 sequences per batch and the rmsprop optimizer [31], with a learning rate of
10⁻³."*

Verbatim on computing time and size: *"The network was trained on a personal laptop² with a Linux
operating system, Tensorflow v2.4.1 [32], and GPU acceleration. With these hardware and software
conditions, the training times are approximately 30 minutes (BPS only), 40 minutes (BPS+WTC), and 250
minutes (Full dataset). The number of trainable parameters in the network is close to 90,000. This
number already includes all the parameters introduced by the additional output tasks. Therefore, the
model is similar in size to recent approaches [19,20]."* Footnote 2 gives the machine: *"Intel i7 10750h,
Nvidia RTX 2070, 32 GB DDR4."*

### §2.13 The split protocol and the data-leakage clause

§4.1, verbatim: *"For all datasets, the same procedure was followed regarding data splits. Training,
validation, and test splits were produced randomly (except in BPS, where they were provided by Chen and
Su [6]). Preliminary experiments were conducted in the training set, using the validation set to assess
the performance, adjust the hyperparameters, and inform the design of the network architecture. The
best-performing version of our model was run once in the test set, this time including the validation
portion as part of the training. The results obtained for all the rows labeled Full dataset in Table 4
report the results obtained on the corresponding test split."*

Verbatim on augmentation and leakage: *"For every training example, we synthesized and texturized an
additional file, using only the Roman numeral annotations (and ignoring the original score). The original
and texturized training examples were transposed to different keys for further data augmentation. Both
forms of data augmentation were applied to the training set of a particular experiment, leaving the
validation and test sets intact, in order to prevent any data leakage."*

---

## §3 — Coupling facts

*(Mandatory under the commission's §4: what the method assumes about its upstream, what it hands
downstream, and its own stated scope and limits. Everything in this section is at the paper.)*

### §3.1 What it ASSUMES about its upstream

- **A symbolic score, already parsed into notes with durations.** The input is "sampled from the score
  at symbolically regular note duration values" (§3.1); no audio input is described in §3.1.
- **Pitch spelling is present and correct in that score.** The input encoding splits each pitch into a
  pitch class and a generic note letter (§3.1). A source that carries no spelling cannot fill the
  seven-way letter component.
- **A metrical grid fine enough for a thirty-second note.** Eight timesteps per quarter note is the
  atomic sampling rate (§3.1); anything shorter than a thirty-second note has no timestep of its own.
- **A bass voice identifiable at every timestep.** One of the two input blocks is the spelled bass
  (§3.1). The paper does not say how the bass is determined from the score.
- **For training only: Roman numeral annotations in RomanText [4] form.** The synthetic-data route
  converts RomanText files into block-chord scores with music21 (§3.5.2), so the annotation format is
  an upstream requirement of the augmentation, not of inference.
- **For training only: every modulation inside a piece must fall within the target key-signature range**
  for a transposition to be admitted (§3.5.1).

### §3.2 What it HANDS downstream

- **One label per timestep, on eleven parallel tasks**, the timestep being a thirty-second note (§3.3,
  §3.4). The output sequence has the same length as the input sequence.
- **A full Roman numeral label, reconstructed by one of two methods** — RN_conv from the six
  conventional tasks, or RN_alt from key, inversion and CommonRNs (§3.4.1, §4.3).
- **Spelled outputs**: the key task distinguishes enharmonic keys (34 classes), and the root and bass
  tasks carry a pitch spelling (35 classes each) (§3.4, §3.4.1).
- **A per-timestep harmonic-rhythm bit** — whether a Roman numeral annotation starts at this timestep
  (§3.4.1) — which the paper says "may be relevant for chord segmentation".
- **A tonicization key and a pitch-class set per timestep** (§3.4.1).

### §3.3 Its own STATED scope and limits

- **Chord segmentation is NOT assessed.** §5, verbatim: *"Although we present these general improvements
  in accuracy, we have not yet assessed the chord segmentation of our model, leaving that for future
  work."*
- **The CommonRNs task has a stated ceiling.** §4.3, verbatim: *"For this task, note that the maximum
  achievable accuracy is ~98%, because any class that is not present in the set of 75 CommonRNs will be
  misclassified."*
- **The repertoire is not stated as a limit anywhere in the pages as read.** What the paper does state
  is §1's framing of Roman numeral annotation as "particularly popular in Western music theory for the
  analysis of 'common-practice' tonal music", and the six datasets it uses (§4.1). Of those six, the
  composer is named by this paper only for four — the Annotated Beethoven Corpus (reference [27]'s own
  title says "all Beethoven string quartets"), the Beethoven Piano Sonatas, the Haydn "Sun" Quartets and
  the Well-Tempered Clavier; **what TAVERN and When-in-Rome contain is not stated in these eight
  pages.** **That the method
  is bounded to that repertoire is this read's inference from the material used and is NOT a claim the
  paper makes.**
- **The key vocabulary is bounded by key signature**, at 8 flats to 8 sharps in both modes (§3.5.1,
  §3.4).
- **The texturization is declared as intuition, not as a validated model of texture.** §3.5.2: the
  patterns "were designed intuitively"; §5: *"We developed this method based on observation and music
  theory domain-knowledge. A more sophisticated approach could offer better texturization outputs."*
- **The field's own standing is stated as low.** §1: *"the performance of functional harmony models for
  predicting Roman numeral labels remains relatively low"*; §5: *"current models have yet to reach the
  expectations of MIR researchers and musicologists alike"*.

---

## §4 — Claims, labeled

*(FACT = stated or measured in this paper as read. THEORY = established published theory the paper
invokes. CONJECTURE = proposed, hypothesised or asserted without a measurement in this paper. The label
is about what THIS paper establishes, not about whether the claim is true.)*

1. **FACT.** The network is a convolutional recurrent network with two independent convolutional blocks
   — one for spelled bass, one for spelled chroma — concatenated, then two dense layers, then two
   bidirectional GRU layers, then eleven task-specific time-distributed dense heads (§3, §3.2, §3.3,
   §3.4, Figure 1).
2. **FACT.** Each convolutional block has six 1D convolutional layers; each layer doubles the
   convolution window and halves the number of output filters; the block's output is 82 features per
   timestep (§3.2, Figure 1 caption).
3. **FACT.** A spelled pitch is encoded two-hot in 19 features — one of 12 pitch classes and one of 7
   note names — giving 38 input features per timestep against the 70 of the representation the paper
   attributes to Micchi et al. (§3.1).
4. **FACT.** Eleven tasks are learned: six conventional (key 34, primary degree 21, secondary degree 21,
   quality 15, inversion 4, root 35) and five new (CommonRNs 75, harmonic rhythm 2, bass 35,
   tonicization 34, pitch class set 93) (§3.4, §3.4.1, Figure 1).
5. **FACT.** The key task has four more classes than the representation attributed to Micchi et al. —
   {F♭, G♯, d♭, e♯} — because the dataset revealed modulations reaching G♯ major (§3.4).
6. **FACT.** A set of 75 Roman numeral classes, with inversions removed and synonyms standardized,
   spanned ~98% of all annotations across the training set (§3.4.1, Table 1).
7. **FACT.** Training used 100 fixed epochs, weights saved each epoch, and the weights selected were
   those maximizing the mean accuracy across the six conventional tasks (§4.2).
8. **FACT.** Trainable parameters are "close to 90,000", including those introduced by the additional
   output tasks (§4.2).
9. **FACT.** Six datasets were used — ABC, BPS, HaydnSun, TAVERN, WiR, WTC — with 241 training files
   (1424 sequences), 56 validation files (333 sequences) and 56 test files (329 sequences) (§4.1,
   Table 2).
10. **FACT.** Four configurations were each trained on each of the six datasets individually, for 24
    experiments; Table 3 reports each configuration's accuracy averaged across the six datasets (§4.3).
11. **FACT, WITH THE BOUND AT §7.1(a).** The paper states that AugmentedNet₁₁₊ "is the best-performing
    configuration" based on the reported accuracy values (§4.3). Table 3's own figures put it highest on
    five of the six printed columns and **below** AugmentedNet₆₊ on the inversion column.
12. **FACT.** Reconstructing the Roman numeral from key, inversion and CommonRNs (RN_alt) yields a
    higher accuracy than reconstructing it from the six conventional tasks (RN_conv) in **every**
    AugmentedNet row of Table 4 (§4.3; the per-row comparison is derived at §6.6).
13. **FACT, WITH ITS POPULATION NAMED.** In the directly comparable rows of Table 4, AugmentedNet's
    RN_conv exceeds the Roman numeral accuracy of **every model that prints one in a comparable row** —
    Micchi et al. 2020 (42.8 and 39.1), Chen and Su 2021 (41.7 and 26.0) and Chen and Su 2018 (25.7).
    **The Chen and Su 2019 row prints no Roman numeral value at all**, so it is outside the comparison
    rather than beaten by it (§4.3, Table 4).
14. **FACT.** In the WTC 4-fold cross-validation replication, AugmentedNet's key accuracy is 85.1 (s.d.
    4.0) against CS21's 56.3 (s.d. 2.5), and its RN_conv is 42.9 (4.2) against CS21's 26.0 (1.7)
    (Table 4).
15. **FACT.** Both forms of data augmentation were applied only to the training split of each
    experiment, the validation and test splits being left intact (§4.1).
16. **THEORY.** Multitask learning may improve a model by preferring representations useful to related
    tasks, acting as an implicit form of data augmentation and regularization — attributed to Ruder [16]
    (§3.4.1).
17. **THEORY.** Reusing earlier feature maps in later convolutional layers strengthens feature
    propagation and reduces parameter count — attributed to the DenseNet work [22] (§3.2).
18. **THEORY.** Pitch spelling in inputs and outputs gives a more informative output and increases the
    number of transpositions available for augmentation — attributed to Micchi et al. [20] (§2).
19. **CONJECTURE.** That the five additional tasks improve the model's accuracy through the MTL layout,
    "even if they are not explicitly used to predict the Roman numeral" — the paper states this as a
    hypothesis (§3.4.1). **Table 3's own no-synthetic pair does not support it; see §6.5.**
20. **CONJECTURE.** That the block-chord synthetic texture was only slightly beneficial "possibly
    because it did not capture the complex texture of real keyboard music" — the paper marks its own
    reason as possible (§3.5.2).
21. **CONJECTURE.** That harmonic rhythm "may be relevant for chord segmentation" (§3.4.1) — no
    segmentation measurement is reported anywhere in the paper (§5, and §7.2 of this file).
22. **CONJECTURE.** That the texturized-synthetic idea "may have the most potential impact on functional
    harmony research, because the data is still scarce and expensive to annotate" (§5).
23. **CONJECTURE.** That triad-vs-seventh classification, tonal function (T, D, SD) and cadence
    detection are further tasks that could be examined (§5).

---

## §5 — Measured results and printed values, with corpus, measure and value as the paper states them

### §5.1 Figure 1, transcribed — the tensor shapes through the network

Read at the diagram on page 3 (printed 406). The convolutional block, expanded at the top of the figure,
carries these shapes in order:

| Position in the block | Printed shape |
|---|---|
| Input (`Bass ‖ Chroma`) | 640×19 |
| after Conv1D (1) | 640×32 |
| after Concatenate (1) | 640×51 |
| after Conv1D (2) | 640×16 |
| after Concatenate (2) | 640×67 |
| after Conv1D (3) | 640×8 |
| after Concatenate (3) | 640×75 |
| after Conv1D (4) | 640×4 |
| after Concatenate (4) | 640×79 |
| after Conv1D (5) | 640×2 |
| after Concatenate (5) | 640×81 |
| after Conv1D (6) | 640×1 |
| after Concatenate (6) | 640×82 |

The window marks above the six convolutional layers are note-value glyphs, printed as `W=` followed by a
note symbol, increasing left to right — consistent with the caption's rule that each layer doubles the
window, and with §3.2's statement that the first layer's window is a single thirty-second note and the
sixth layer's is 32 timesteps (a whole note). **This read does not transcribe the six glyphs
individually**; at the available resolution the thirty-second, sixteenth and eighth flags are not
separable with certainty, and the text states the two endpoints in words.

The main path, below the expanded block:

| Stage | Printed shape |
|---|---|
| `Chroma` input | 640×19 |
| `Bass` input | 640×19 |
| each Convolutional block's output | 640×82 |
| after Concatenate | 640×164 |
| after Dense (1) | 640×64 |
| after Dense (2) | 640×32 |
| after Bidirectional GRU (1) | 640×60 |
| after Bidirectional GRU (2) | 640×60 |

The eleven heads, each printed with its class count in parentheses:

| Group, as the figure labels it | Task (classes) |
|---|---|
| *Conventional tasks* | Key (34), PrimDegree (21), SecDegree (21), Quality (15), Inversion (4), Root (35) |
| *Additional new tasks* | CommonRNs (75), HarmRhythm (2), Bass (35), Tonicization (34), PitchClassSet (93) |

### §5.2 Table 1 — what it is, what this read transcribes, and what it declines

Table 1 is headed by five column labels — **1–15, 16–30, 31–45, 46–60, 61–75** — each column carrying
fifteen Roman numeral classes, for **75 classes in all**. Its caption, verbatim: *"CommonRNs. The 75
most-common Roman numeral classes found across the training set. Note that the inversion has been
omitted and learned as a separate task."* The order is evidently by descending frequency: the first
column begins **I, V⁷, V, i, IV, ii, vi, iv**.

**WHAT THIS READ DECLINES TO TRANSCRIBE, AND WHY IT IS DECLINED RATHER THAN APPROXIMATED.** The table is
set in a small face in which the superscript **°** (fully diminished) and **∅** (half-diminished) marks,
and the distinction between some upper- and lower-case numerals at that size, are not separable with
certainty at the resolution available to this read. Transcribing them anyway would put a symbol in this
record with a confidence this read does not have. **So the seventy-five cells are NOT transcribed cell
by cell here.** What is established at the table and stated above is its shape (five columns of
fifteen), its total (75), its caption, its stated coverage (~98% of the training set's annotations,
§3.4.1), and its opening run.

**What IS legible at the table and bears on the record**, stated at the level this read can support: the
75 classes include applied and secondary chords in quantity (numerous entries of the form `V/x`,
`V⁷/x`, `vii.../x`), the Neapolitan (`N`), the Italian and German augmented sixths (`It`, `Ger`), a
cadential six-four entry written in the applied form (`Cad/V`), and a ninth chord (`V⁹`). **The French
augmented sixth (`Fr`) also appears.** No claim is made here about which of the three augmented-sixth
spellings occupy which positions.

### §5.3 Table 2, transcribed — the six datasets and their splits

Caption, verbatim: *"The functional harmony datasets used in our experiments. The splits were generated
randomly (except for BPS). For each split, the number of files and the number of sequences (in
parentheses) are indicated."*

| Dataset | Training | Validation | Test |
|---|---|---|---|
| ABC [27] | 50 (448) | 10 (97) | 10 (99) |
| BPS [6] | 18 (155) | 7 (75) | 7 (82) |
| HaydnSun [28] | 16 (91) | 4 (19) | 4 (19) |
| TAVERN [29] | 38 (404) | 8 (68) | 8 (64) |
| WiR [4,5] | 107 (301) | 21 (61) | 21 (51) |
| WTC [4] | 12 (25) | 6 (13) | 6 (14) |
| **Total** | **241 (1424)** | **56 (333)** | **56 (329)** |

A sequence is 640 frames (§4.1), each frame a thirty-second note (§3.1).

**★ FOOTNOTE 1 SAYS THE SIX DATASETS ARE NOT NECESSARILY SIX DISJOINT COLLECTIONS, AND THE PAPER DOES
NOT SAY WHAT WAS DONE ABOUT IT.** *(Adopted into this read at the cross-check from row 48's first
extract, which flagged this footnote; the wording below is quoted from the paper at printed page 407
rather than from that file — see §9.3(a).)* The footnote attached to the When-in-Rome entry of §4.1
reads, verbatim: *"Note that, in practice, WiR is also a meta-collection and standardization effort,
where several of these datasets (e.g., ABC) have been converted into a common representation. Here, we
list the academic sources of the datasets. For the annotation files, please refer to the relevant
literature [4, 5] as well as the accompanying source code of this paper."*

**What follows from it, and what does not.** The paper states that **several** of its other five
datasets are also inside WiR, and names ABC as its example. *(★ MADE EXACT AT THE USER-ORDERED CHECK:
as first written this sentence said "at least one", which understates the footnote's own word and
disagreed in strength with the handoff entry's account of the same footnote.)* §4.1's data-leakage clause addresses **augmentation only** — *"Both forms
of data augmentation were applied to the training set of a particular experiment, leaving the validation
and test sets intact"* — and **the pages as read say nothing about whether a piece appearing in two of
the six datasets was removed from one of them, or about whether a piece in one dataset's training split
can appear in another dataset's test split.** The splits were "produced randomly" per dataset (§4.1).
*(NOT claimed: that any such overlap occurred in the reported experiments, or that any figure is
affected. What is established is that the paper raises the overlap in its own footnote and does not say
what was done about it. Establishing more would need the released splits, which this read did not
open.)* **It bears on §6.7**, since the composite "Full test set" row pools six test splits that the
paper's own footnote says need not be disjoint.

### §5.4 Table 3, transcribed — the four configurations

Caption, verbatim: *"Average accuracy (in %) of four configurations of our model, where {6, 11} indicate
the number of MTL tasks and '+' indicates the use of synthetic training data."*

| Model | Key | Deg. | Qual. | Inv. | Root | RN |
|---|---|---|---|---|---|---|
| AugN₆ | 82.7 | 64.4 | 76.6 | 77.4 | 82.5 | 43.3 |
| AugN₆₊ | 83.0 | 65.1 | 77.5 | **78.6** | 83.0 | 44.6 |
| AugN₁₁ | 81.3 | 64.2 | 77.2 | 76.1 | 82.9 | 43.1 |
| AugN₁₁₊ | **83.7** | **66.0** | **77.6** | 77.2 | **83.2** | **45.0** |

Bold marks are as printed in the table. **The six column maxima are bolded, and the inversion column's
maximum is AugN₆₊'s 78.6 and not AugN₁₁₊'s 77.2.**

The population behind these figures, from §4.3: each of the four configurations was "trained on each of
the six datasets individually, for a total of 24 experiments", and "the accuracy reported is the average
accuracy obtained by each model configuration across all six datasets". **No uncertainty is printed for
any cell of this table.**

### §5.5 Table 4, transcribed — the comparison against other models

Caption, verbatim: *"Accuracy of five functional harmony models: Chen and Su (2018, 2019, and 2021),
Micchi et al. (2020), and AugmentedNet₁₁₊. In the WTC test set, the comparison against CS21 replicated
the 4-fold cross validation [19]. In this case, the standard deviation is indicated in parentheses. For
all other rows, the results report the performance on the held test set. The values in the RN_alt column
indicate the performance using an alternative method for reconstructing the full Roman numeral, as
explained in Section 3.4.1."*

| Test set | Training set | Model | Key | Degree | Quality | Invers. | Root | ComRN | RN_conv | RN_alt |
|---|---|---|---|---|---|---|---|---|---|---|
| Full test set | Full dataset | AugN | 82.9 | 67.0 | 79.7 | 78.8 | 83.0 | 65.6 | 46.4 | 51.5 |
| WiR | Full dataset | AugN | 81.8 | 69.2 | 85.9 | 90.3 | 90.3 | 70.2 | 56.4 | 62.4 |
| HaydnSun | Full dataset | AugN | 81.2 | 62.9 | 80.2 | 82.7 | 86.5 | 60.4 | 48.6 | 52.1 |
| ABC | Full dataset | AugN | 83.6 | 65.6 | 78.0 | 76.9 | 78.9 | 62.6 | 44.5 | 48.4 |
| TAVERN | Full dataset | AugN | 88.7 | 60.0 | 77.4 | 78.8 | 81.5 | 66.3 | 42.6 | 52.9 |
| WTC | Full dataset | AugN | 77.2 | 69.7 | 75.0 | 74.4 | 82.7 | 61.7 | **46.2** | 47.9 |
| WTC_crossval | BPS+WTC | AugN | **85.1**₍₄.₀₎ | 62.9₍₅.₅₎ | **69.1**₍₁.₉₎ | 70.1₍₃.₇₎ | 79.2₍₁.₈₎ | 59.9₍₃.₄₎ | **42.9**₍₄.₂₎ | 46.9₍₄.₇₎ |
| WTC_crossval | BPS+WTC | CS21 | 56.3₍₂.₅₎ | – | – | – | – | – | 26.0₍₁.₇₎ | – |
| BPS | Full dataset | AugN | **85.0** | **73.4** | **79.0** | **73.4** | 84.4 | 68.3 | **45.4** | 49.3 |
| BPS | All data | Mi20 | 82.9 | 68.3 | 76.6 | 72.0 | – | – | 42.8 | – |
| BPS | BPS+WTC | AugN | **82.9** | 70.9 | 80.7 | 72.0 | 85.3 | 67.6 | **44.1** | 47.5 |
| BPS | BPS+WTC | CS21 | 79.0 | – | – | – | – | – | 41.7 | – |
| BPS | BPS | AugN | **83.0** | **71.2** | **80.3** | **71.1** | 84.1 | 68.5 | **44.0** | 47.4 |
| BPS | BPS | Mi20 | 80.6 | 66.5 | 76.3 | 68.1 | – | – | 39.1 | – |
| BPS | BPS | CS19 | 78.4 | 65.1 | 74.6 | 62.1 | – | – | – | – |
| BPS | BPS | CS18 | 66.7 | 51.8 | 60.6 | 59.1 | – | – | 25.7 | – |

Bold marks and en-dashes are as printed. Parenthesised figures are the standard deviations across the
four folds, printed only on the two WTC_crossval rows. Single horizontal rules in the printed table
"delimit experiments that are directly comparable" (§4.3).

### §5.6 The protocol constants, as the paper states them

| Constant | Value | Where |
|---|---|---|
| Atomic timestep | thirty-second note | §3.1 |
| Timesteps per quarter note | 8 | §3.1 |
| Frames per sequence example | 640 | §3.1 |
| Quarter notes per sequence example | 80 | §3.1 |
| Input features per timestep | 38 (19 bass + 19 chroma) | §3.1 |
| Features per spelled pitch | 19 (1 of 12 pitch classes, 1 of 7 note names) | §3.1 |
| Convolutional layers per block | 6 | §3.2, Figure 1 |
| Features out of each convolutional block | 82 | §3.2 |
| Dense layer widths | 64, then 32 | §3.3 |
| Recurrent layers | 2 bidirectional GRU | §3.3 |
| Output tasks | 11 | §3.4 |
| Epochs | 100, fixed, in all experiments | §4.2 |
| Weight selection | weights maximizing the mean accuracy across the six conventional tasks | §4.2 |
| Batch size | 16 sequences | §4.2 |
| Optimizer | rmsprop | §4.2 |
| Learning rate | 10⁻³ | §4.2 |
| Activation, convolutional and dense | ReLU | §4.2 |
| Activation, GRU | hyperbolic tangent | §4.2 |
| Batch normalization | before activation, except in recurrent layers where it is after | §4.2 |
| Transposition range | key signatures from 8 flats to 8 sharps, both modes | §3.5.1 |
| Texturization scope | slices containing 3–4 simultaneous notes | §3.5.2 |
| Trainable parameters | close to 90,000 | §4.2 |
| Training time, BPS only | ≈30 minutes | §4.2 |
| Training time, BPS+WTC | ≈40 minutes | §4.2 |
| Training time, Full dataset | ≈250 minutes | §4.2 |
| Software | Tensorflow v2.4.1 | §4.2 |
| Hardware | Intel i7 10750h, Nvidia RTX 2070, 32 GB DDR4 | footnote 2 |

### §5.7 The reference list, transcribed

Thirty-two numbered references, pages 7–8 (printed 410–411). Transcribed because this paper's
bibliography is one of the things a reading pass is for.

**ONE NORMALIZATION, DECLARED RATHER THAN LEFT TO BE NOTICED.** Author names, titles, volume, issue,
page and year fields are transcribed exactly as printed, **including reference [4]'s printed spelling
"numerial"**. Venue names are shortened uniformly — the paper's "Proceedings of the …" becomes
"Proc. …" and "International Society for Music Information Retrieval Conference" becomes "ISMIR" — so
the venue strings below are NOT verbatim. Reference [32]'s author list is abbreviated, and that is said
again at its own entry.

1. L. Feisthauer, L. Bigo, M. Giraud, F. Levé, "Estimating keys and modulations in musical pieces,"
   *Proc. Sound and Music Computing Conf.*, 2020.
2. H. Schreiber, C. Weiss, M. Müller, "Local key estimation in classical music recordings: A
   cross-version study on Schubert's Winterreise," *Proc. IEEE ICASSP*, 2020, pp. 501–505.
3. N. Nápoles López, L. Feisthauer, F. Levé, I. Fujinaga, "On local keys, modulations, and
   tonicizations: A dataset and methodology for evaluating changes of key," *Proc. 7th Int. Conf. on
   Digital Libraries for Musicology*, 2020, pp. 18–26.
4. D. Tymoczko, M. Gotham, M. S. Cuthbert, C. Ariza, "The RomanText format: A flexible and standard
   method for representing roman numerial analyses," *Proc. ISMIR*, 2019, pp. 123–129.
5. M. Gotham and P. Jonas, "The openscore lieder corpus," *Poster at the Music Encoding Conference*,
   2021.
6. T.-P. Chen and L. Su, "Functional harmony recognition of symbolic music data with multi-task
   recurrent neural networks," *Proc. ISMIR*, 2018, pp. 90–97.
7. J. Pauwels, K. O'Hanlon, E. Gómez, M. Sandler, "20 Years of automatic chord recognition from audio,"
   *Proc. ISMIR*, 2019.
8. T. Winograd, "Linguistics and the computer analysis of tonal harmony," *Journal of Music Theory*,
   vol. 12, no. 1, pp. 2–49, 1968.
9. H. J. Maxwell, "An expert system for harmonizing analysis of tonal music," *Understanding Music with
   AI: Perspectives on Music Cognition*. Cambridge, MA, USA: MIT Press, 1992, pp. 334–353.
10. D. Temperley, *The Cognition of Basic Musical Structures*. MIT Press, 2004.
11. D. Sleator, "The melisma music analyzer," https://www.link.cs.cmu.edu/music-analysis/, Accessed:
    2021-07-02.
12. C. Sapp, "tsroot manpage," http://extras.humdrum.org/man/tsroot/, Accessed: 2021-08-01.
13. C. Raphael and J. Stoddard, "Functional harmonic analysis using probabilistic models," *Computer
    Music Journal*, vol. 28, no. 3, pp. 45–52, 2004.
14. P. R. Illescas, D. Rizo, J. M. I. Quereda, "Harmonic, melodic, and functional automatic analysis,"
    *Proc. Sound and Music Computing Conf.*, 2007.
15. J. P. Magalhães and W. B. de Haas, "Functional modelling of musical harmony: an experience report,"
    *ACM SIGPLAN Notices*, vol. 46, no. 9, pp. 156–162, 2011.
16. S. Ruder, "An overview of multi-task learning in deep neural networks," *arXiv:1706.05098*, 2017.
17. S. Hochreiter and J. Schmidhuber, "Long short-term memory," *Neural Computation*, vol. 9, no. 8,
    pp. 1735–1780, Nov. 1997.
18. T.-P. Chen and L. Su, "Harmony Transformer: Incorporating chord segmentation into harmony
    recognition," *Proc. ISMIR*, 2019, pp. 259–267.
19. ——, "Attend to chords: Improving harmonic analysis of symbolic music using Transformer-based
    models," *Transactions of the International Society for Music Information Retrieval*, vol. 4, no. 1,
    2021.
20. G. Micchi, M. Gotham, M. Giraud, "Not all roads lead to Rome: Pitch representation and model
    architecture for automatic harmonic analysis," *Transactions of the International Society for Music
    Information Retrieval*, vol. 3, pp. 42–54, 2020.
21. K. Cho, B. Van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, Y. Bengio, "Learning
    phrase representations using RNN encoder-decoder for statistical machine translation,"
    *arXiv:1406.1078*, 2014.
22. G. Huang, Z. Liu, L. V. D. Maaten, K. Q. Weinberger, "Densely connected convolutional networks,"
    *2017 IEEE Conf. on Computer Vision and Pattern Recognition*, 2017, pp. 2261–2269.
23. Y. Ju, N. Condit-Schultz, C. Arthur, I. Fujinaga, "Non-chord tone identification using deep neural
    networks," *Proc. 4th Int. Workshop on Digital Libraries for Musicology*, 2017, pp. 13–16.
24. D. Temperley, "The line of fifths," *Music Analysis*, vol. 19, no. 3, pp. 289–319, 2000.
25. N. Nápoles López and I. Fujinaga, "Harmonic reductions as a strategy for creative data augmentation,"
    *Late-Breaking Demo at 21st ISMIR Conference*, 2020.
26. M. S. Cuthbert and C. Ariza, "music21: A toolkit for computer-aided musicology and symbolic music
    data," *Proc. ISMIR*, 2010, pp. 637–642.
27. M. Neuwirth, D. Harasim, F. C. Moss, M. Rohrmeier, "The Annotated Beethoven Corpus (ABC): A dataset
    of harmonic analyses of all Beethoven string quartets," *Frontiers in Digital Humanities*, vol. 5,
    2018.
28. N. Nápoles López, "Automatic harmonic analysis of classical string quartets from symbolic score,"
    Master's thesis, Universitat Pompeu Fabra, 2017.
29. J. Devaney, C. Arthur, N. Condit-Schultz, K. Nisula, "Theme and variation encodings with Roman
    numerals (TAVERN): A new data set for symbolic music analysis," *Proc. ISMIR*, 2015, pp. 728–734.
30. S. Ioffe and C. Szegedy, "Batch normalization: Accelerating deep network training by reducing
    internal covariate shift," *Proc. Int. Conf. on Machine Learning*, 2015, pp. 448–456.
31. S. Ruder, "An overview of gradient descent optimization algorithms," *arXiv:1609.04747*, 2016.
32. M. Abadi et al., "Tensorflow: A system for large-scale machine learning," *Proc. 12th USENIX Conf.
    on Operating Systems Design and Implementation*, 2016, pp. 265–283.

*(Reference 32's author list is printed in full — Abadi, Barham, Chen, Chen, Davis, Dean, Devin,
Ghemawat, Irving, Isard, Kudlur, Levenberg, Monga, Moore, Murray, Steiner, Tucker, Vasudevan, Warden,
Wicke, Yu, Zheng — and is abbreviated here only in this transcription, which is declared rather than
left to be assumed.)*

### §5.8 The acknowledgments, as printed

§6, verbatim: *"This research has been supported by the Social Sciences and Humanities Research Council
of Canada (SSHRC) and the Fonds de recherche du Québec–Société et culture (FRQSC). We would also like to
thank user ClassicMan from the MuseScore community, who allowed us to use their MusicXML scores of all
Piano Sonatas by Beethoven. This saved us a great deal of time during this research."*

---

## §6 — Arithmetic this read performed on the paper's own printed values

*(Every figure below is computed here from values transcribed in §5. Nothing in this section is quoted
from the paper except where marked.)*

### §6.1 Table 2 closes exactly, in all six sums

| Sum | Computed | Printed |
|---|---|---|
| Training files | 50+18+16+38+107+12 = **241** | 241 |
| Training sequences | 448+155+91+404+301+25 = **1424** | 1424 |
| Validation files | 10+7+4+8+21+6 = **56** | 56 |
| Validation sequences | 97+75+19+68+61+13 = **333** | 333 |
| Test files | 10+7+4+8+21+6 = **56** | 56 |
| Test sequences | 99+82+19+64+51+14 = **329** | 329 |

**All six close with no residual.**

### §6.2 The convolutional block's widths close exactly against the stated rule

Figure 1's caption states that each layer halves the number of output filters, and §3.2 that the block
emits 82 features. Taking the 19-feature input and the printed filter counts:

| Layer | Filters | Concatenated width |
|---|---|---|
| 1 | 32 | 19+32 = **51** |
| 2 | 16 | 51+16 = **67** |
| 3 | 8 | 67+8 = **75** |
| 4 | 4 | 75+4 = **79** |
| 5 | 2 | 79+2 = **81** |
| 6 | 1 | 81+1 = **82** |

**Every one matches the printed shape at that point in the diagram**, and the final 82 matches §3.2's
prose. The filter sequence 32, 16, 8, 4, 2, 1 halves at each step as the caption says, and the six
windows 1, 2, 4, 8, 16, 32 timesteps double at each step; **32 timesteps at eight timesteps per quarter
note is four quarter notes, which is the whole note §3.2 names for the sixth layer.** The two blocks'
outputs concatenate as 82+82 = **164**, which is the printed 640×164.

### §6.3 The pitch encoding closes in both directions

12 pitch classes + 7 note names = **19** features per spelled pitch, as printed. 19 for the bass + 19 for
the chroma = **38** input features per timestep, as printed. The representation attributed to Micchi et
al. closes too: 35 + 35 = **70**, as printed.

### §6.4 The key vocabulary closes against the transposition range, in both directions

Key signatures from 8 flats to 8 sharps inclusive number 8 + 1 + 8 = **17**; at two modes each that is
**34**, which is exactly the key task's printed class count and the tonicization task's. Read the other
way: a range of 7 flats to 7 sharps gives 15 signatures and 30 classes, and §3.4's "extended by one
sharp and one flat, in both modes" adds two signatures, hence **four** classes — which is exactly the
count and the membership of the printed set **{F♭, G♯, d♭, e♯}**, those being the major and minor keys
with eight flats and eight sharps. **The transposition range, the four added classes and the task's 34
outputs are three statements of one fact, and they agree.**

### §6.5 ★ TABLE 3's OWN PAIRS: THE SYNTHETIC DATA HELPS ON EVERY AXIS; THE ADDITIONAL TASKS, ALONE, DO NOT

Differencing the four printed rows against each other, one change at a time:

| Change | Key | Deg. | Qual. | Inv. | Root | RN |
|---|---|---|---|---|---|---|
| add synthetic data, 6 tasks (AugN₆ → AugN₆₊) | +0.3 | +0.7 | +0.9 | +1.2 | +0.5 | +1.3 |
| add the 5 tasks, no synthetic (AugN₆ → AugN₁₁) | **−1.4** | **−0.2** | +0.6 | **−1.3** | +0.4 | **−0.2** |
| add synthetic data, 11 tasks (AugN₁₁ → AugN₁₁₊) | +2.4 | +1.8 | +0.4 | +1.1 | +0.3 | +1.9 |
| add the 5 tasks, with synthetic (AugN₆₊ → AugN₁₁₊) | +0.7 | +0.9 | +0.1 | **−1.4** | +0.2 | +0.4 |

**Synthetic data raises all six columns in both task settings. The five additional tasks, added without
synthetic data, LOWER four of the six columns** — key, degree, inversion and the Roman numeral itself —
and raise quality and root. Added with synthetic data they raise five and lower inversion.

**This bears directly on the paper's own hypothesis at §3.4.1** — *"We hypothesize that these additional
tasks (e.g. pitch class sets) improve the accuracy of the model because of the MTL layout, even if they
are not explicitly used to predict the Roman numeral."* **The AugN₆ against AugN₁₁ pair is the paper's
own test of that hypothesis with the other variable held fixed, and it does not support it.** The paper
does not difference these two rows anywhere, and draws no conclusion from the pair.

**THE BOUND ON THIS, STATED SO IT IS NOT OVERREAD:** Table 3 prints no uncertainty for any cell, so
whether any of these movements exceeds sampling noise is not established by the paper and is not
established here. What is established is what the printed values are and what differencing them gives.
Across the twenty-four differences tabulated above, the largest rise is the **+2.4** on key from adding
synthetic data to the eleven-task configuration, and **the largest fall is −1.4, which occurs TWICE** —
on key when the tasks are added without synthetic data, and on inversion when they are added with it.
*(Both extremes are named because naming one of a tie as "the largest" would be false against the table
standing beside it.)*

### §6.6 ★ RN_alt EXCEEDS RN_conv IN EVERY AugmentedNet ROW OF TABLE 4, AND THE MARGIN VARIES BY A FACTOR OF SIX

| Row | RN_conv | RN_alt | RN_alt − RN_conv |
|---|---|---|---|
| Full test set / Full dataset | 46.4 | 51.5 | +5.1 |
| WiR / Full dataset | 56.4 | 62.4 | +6.0 |
| HaydnSun / Full dataset | 48.6 | 52.1 | +3.5 |
| ABC / Full dataset | 44.5 | 48.4 | +3.9 |
| TAVERN / Full dataset | 42.6 | 52.9 | **+10.3** |
| WTC / Full dataset | 46.2 | 47.9 | **+1.7** |
| WTC_crossval / BPS+WTC | 42.9 | 46.9 | +4.0 |
| BPS / Full dataset | 45.4 | 49.3 | +3.9 |
| BPS / BPS+WTC | 44.1 | 47.5 | +3.4 |
| BPS / BPS | 44.0 | 47.4 | +3.4 |

**Ten rows, ten positive margins**, which supports the paper's claim at §4.3 and §5 that RN_alt is the
better reconstruction. **The margin is not uniform:** it is +10.3 on TAVERN and +1.7 on WTC, a spread of
8.6 points between the two extremes. The paper reports the advantage without reporting its spread and
offers no account of why it varies.

**★ AND ON THE ONE ROW THAT PRINTS A SPREAD, THE MARGIN IS SMALLER THAN THE SPREAD.** *(Adopted into
this read at the cross-check from row 48's first extract, which makes this comparison; the figures are
re-read here at Table 4 — see §9.3(b).)* The WTC_crossval row is the only AugmentedNet row of Table 4
carrying standard deviations, and there the **+4.0 margin sits under the standard deviation printed on
each of the two cells it is taken from, 4.2 and 4.7.** *(Stated exactly: a standard deviation across
four folds is not a significance test, and this is a bound on that one row and not a finding against the
other nine — those carry no spread to read a margin against, which is itself the bound on them.)*

### §6.7 ★ THE FIRST ROW OF TABLE 4 IS NOT THE AVERAGE OF THE OTHER SIX, UNDER EITHER OF THE TWO OBVIOUS READINGS

§4.3 describes the first row as "a composite test set that includes all six datasets", which is an
evaluation and not an aggregation. This read checked whether it nonetheless reproduces as an aggregate
of the six per-dataset *Full dataset* rows (WiR, HaydnSun, ABC, TAVERN, WTC and BPS), on two weightings:
unweighted, and weighted by each dataset's printed test-sequence count from Table 2 (ABC 99, BPS 82,
HaydnSun 19, TAVERN 64, WiR 51, WTC 14; total 329).

| Column | Printed | Unweighted mean | Residual | Sequence-weighted | Residual |
|---|---|---|---|---|---|
| Key | 82.9 | 82.92 | −0.02 | 84.25 | +1.35 |
| Degree | 67.0 | 66.80 | −0.20 | 67.03 | +0.03 |
| Quality | 79.7 | 79.25 | −0.45 | 79.36 | −0.34 |
| Invers. | 78.8 | 79.42 | +0.62 | 78.70 | −0.10 |
| Root | 83.0 | 84.05 | +1.05 | 83.14 | +0.14 |
| ComRN | 65.6 | 64.92 | −0.68 | 65.75 | +0.15 |
| RN_conv | 46.4 | 47.28 | +0.88 | 46.51 | +0.11 |
| RN_alt | 51.5 | 52.17 | +0.67 | 51.86 | +0.36 |

**Neither reading reproduces the row.** The sequence-weighted reading lands within 0.36 on seven of the
eight columns and misses key by 1.35; the unweighted reading matches key to the printed precision and
misses root by 1.05 and RN_conv by 0.88. **The finding is not that the row is wrong** — the paper says
it is a separate evaluation on pooled data, and residuals of this size are what that reading predicts,
sequences being a proxy for frames and the last sequence of a file being of unstated fill. **The finding
is for a later reader: the first row of Table 4 may not be treated as a summary of the six rows beneath
it.** Its agreement with the unweighted mean on the key column, to the printed precision, is not
evidence that the row IS an unweighted mean — the same reading misses root by 1.05 and RN_conv by 0.88
in the same row.

### §6.8 ★ THE RECONSTRUCTION ACCURACIES ARE FAR ABOVE WHAT INDEPENDENT SUB-TASKS WOULD GIVE

Reconstructing the full Roman numeral requires every contributing sub-task to be right at that timestep.
If the sub-tasks' errors were independent, the reconstruction accuracy would be the product of the
sub-task accuracies. On the Full test set row:

- **RN_alt** is built from key, inversion and CommonRNs (§3.4.1): 0.829 × 0.788 × 0.656 = **0.4285**, or
  42.9 %. **Printed: 51.5** — higher by **8.6 points**.
- **RN_conv** is built from the six conventional tasks: 0.829 × 0.670 × 0.797 × 0.788 × 0.830 =
  **0.2895**, or 29.0 %. **Printed: 46.4** — higher by **17.4 points**.

**So the sub-task errors co-occur substantially rather than compounding.** A timestep the model gets
wrong tends to be wrong on several axes at once, which is why reconstructing from fewer, larger classes
(RN_alt) loses less than the arithmetic of independence would suggest.

**TWO BOUNDS ON THIS DERIVATION, BOTH LOAD-BEARING.** *First*, Table 4 prints ONE "Degree" column while
the six conventional tasks include TWO degree tasks (primary and secondary); this computation treats the
printed column as the joint accuracy of both, which is the reading that makes the six-task product
computable at all, and the paper does not say whether that is what the column reports. If the column is
one of the two tasks alone, the independence product is lower still and the gap wider. *Second*, this is
arithmetic over per-column marginals, not a measurement of the joint distribution, which the paper does
not publish; it establishes that the errors are not independent and it does not quantify by how much.

### §6.9 The experiment count and the pagination close

Four configurations across six datasets is 4 × 6 = **24**, which is the total §4.3 states. Printed pages
404 to 411 inclusive is 411 − 404 + 1 = **8**, which is the page count the tool returned.

### §6.10 The CommonRNs ceiling and the reported values are consistent

§3.4.1 puts the 75 classes' coverage of the training set's annotations at ~98 %, and §4.3 states the
task's maximum achievable accuracy as ~98 % for that reason. **The ten printed ComRN values run from
59.9 (the WTC cross-validation) to 70.2 (WiR)**, so every one of them sits at least 27 points under the
stated ceiling. The class-coverage ceiling is therefore not what limits the reported CommonRNs accuracy.

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

**(a) ★ THE "BEST-PERFORMING CONFIGURATION" CLAIM IS REFUTED ON ONE OF ITS SIX AXES BY THE TABLE IT
CITES, AND BY THAT TABLE'S OWN BOLDING.** §4.3 states: *"Based on the reported accuracy values, the
AugmentedNet₁₁₊ (with additional tasks and synthetic training examples) is the best-performing
configuration."* In Table 3, AugN₁₁₊ carries the highest value in the key, degree, quality, root and RN
columns — and **77.2 in the inversion column against AugN₆₊'s 78.6, which the table itself sets in
bold as that column's maximum.** The sentence is right on five of six and wrong on the sixth, and **no
sentence in the pages as read notes the exception.** **The choice matters downstream**: Table 4's own
caption names AugmentedNet₁₁₊ as the model in every AugN row of that table.

**(b) THE PRINTED PITCH-CLASS RANGE CONTRADICTS THE PRINTED PITCH-CLASS COUNT IN THE SAME PARAGRAPH.**
§3.1 writes *"the pitch class (0–12)"* and, two sentences later, *"a two-hot encoded vector with 19
features (1 of 12 pitch classes, and 1 of 7 note names)"*. A range 0–12 inclusive holds thirteen values,
which with seven note names would give twenty features and not nineteen. **The nineteen is corroborated
three ways** — by the printed 19, by 19+19 = 38, and by the diagram's 640×19 input — **so the count is
right and the printed range is the defect**; the intended range is evidently 0–11. It moves no value.

**(c) TABLE 3's "RN" COLUMN DOES NOT SAY WHICH RECONSTRUCTION METHOD IT REPORTS, AND THE TWO METHODS
ARE NOT BOTH AVAILABLE TO ALL FOUR ROWS.** Table 4 splits the Roman numeral into RN_conv and RN_alt;
Table 3 prints a single "RN". **RN_alt is reconstructed from key, inversion and CommonRNs (§3.4.1), and
CommonRNs is one of the five additional tasks — so the AugN₆ and AugN₆₊ configurations cannot produce
it at all.** Their RN values are therefore necessarily RN_conv. Whether the AugN₁₁ rows' RN values are
RN_conv or RN_alt is not stated anywhere. **If they were RN_alt, the column would be comparing two
different reconstruction methods down its own length**, and the margin found at §6.6 would account for
most of the reported gain. This read cannot settle it at the paper, and records it as unsettled rather
than choosing a reading.

**(d) TABLE 4's BOLD MARKS FOLLOW NO STATED CONVENTION, AND TWO OF THEM HAVE NO COMPARATOR.** The
caption explains the parenthesised standard deviations and the RN_alt column but says nothing about the
bolding. Most bolded values sit on an AugmentedNet row that has a comparison row directly beneath it and
are the better of that pair — the BPS blocks read that way throughout. **Two do not.** *(i)* The
**WTC_crossval row's quality value, 69.1, is bolded although the CS21 row beneath it prints no quality
value at all**, and 69.1 is not that column's maximum (85.9, on the WiR row, is). *(ii)* The **WTC /
Full dataset row's RN_conv value, 46.2, is bolded although that row has no comparison row at all** —
it sits above the horizontal rule that opens the cross-validation block — and 46.2 is likewise not the
column's maximum (56.4, on the WiR row, is). Neither moves a value; they are marks, not figures.

**(e) THE PAPER'S OWN HYPOTHESIS ABOUT THE ADDITIONAL TASKS IS NOT SUPPORTED BY THE ONE PAIR OF ROWS
THAT TESTS IT.** §3.4.1 hypothesizes that the additional tasks improve accuracy through the MTL layout;
Table 3's AugN₆ against AugN₁₁ pair holds the synthetic data fixed and moves only the tasks, and four of
the six columns fall (§6.5). The paper neither differences the pair nor comments on it, and the abstract
states the improvement as achieved: *"The additional tonal tasks strengthen the shared representation
learned through multitask learning."* **This is a claim about the paper's own reported values, not about
what is true of the method**, and the bound of §6.5 applies: no uncertainty is printed, so neither the
fall nor the rise is shown to exceed noise.

**(f) THE UNIT OF "ACCURACY" IS NOT DEFINED AT EITHER TABLE.** Table 3's caption says "Average accuracy
(in %)" and Table 4's says "Accuracy of five functional harmony models", and **neither states the
denominator**. §3.3 establishes that the model emits one label per timestep and §3.1 that a timestep is
a thirty-second note, so a per-timestep reading is the natural one — **but neither caption says so, no
frame count is printed beside any accuracy in either table, and the evaluation unit used by the models
being compared against is not restated in the pages as read.**

**(g) TWO SMALL PRINTING FAULTS, RECORDED SO THAT THIS FILE'S OWN TRANSCRIPTION IS NOT READ AS A
MISTAKE.** *(i)* Reference [4]'s title is printed as *"The RomanText format: A flexible and standard
method for representing roman numerial analyses"* — **"numerial"**, which §5.7 transcribes as printed.
*(ii)* §1's worked example says that *"an annotation like C:vii°6/V encodes the local key (C-major),
quality of the chord (diminished triad), chord inversion (first), and any existing tonicization
(G-major)"* — **a list of four components that omits the scale degree**, which is the numeral itself and
which the paper's own §3.4 later counts as two of the six conventional tasks. *(Stated exactly: the
sentence does not claim its list is exhaustive, so this is an incompleteness in an illustration and not
a false statement. It is recorded because the illustration is the paper's only worked example of what a
Roman numeral label carries.)* The gloss itself is correct: `vii°6` in C major is a first-inversion
diminished triad, and `/V` makes G major the tonicized key.

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered

- **★ NO ACCURACY IS REPORTED FOR FOUR OF THE FIVE NEW TASKS, IN THE EIGHT PAGES AS READ.** Harmonic
  rhythm, bass, tonicization and pitch class set are defined at §3.4.1 and appear as heads in Figure 1,
  and **no number for any of them appears in Table 3, in Table 4, or in the running text of §4.3 or
  §5.** Only CommonRNs has a column. So the four tasks introduced to "strengthen the shared MTL layers"
  are visible in the results only through their effect on the other tasks, and that effect is the
  aggregate one differenced at §6.5. *(The paper's §1 states that preprocessed data, splits, experiment
  logs and source code are released at a repository; this read did not visit it, so nothing is asserted
  about what is reported there.)*
- **Chord segmentation is not evaluated at all**, which the paper states itself (§5) — and the harmonic
  rhythm task, the one output that bears on segmentation, is among the four with no reported accuracy.
- **No uncertainty is printed** for Table 3 at all, nor for any Table 4 row except the two WTC
  cross-validation rows.
- **The size of the augmented training set is not given in the pages as read.** Table 2 counts files
  and sequences, and §4.1's wording places augmentation after the split, so those counts are evidently
  pre-augmentation; the number of transposed copies actually admitted — which §3.5.1 makes
  piece-dependent, since every modulation must fall inside the target range — and the number of
  texturized copies are not reported, jointly or per dataset.
- **The three texturization patterns are not ablated separately.** §3.5.2 reports that block chords were
  "only slightly beneficial" and that texturized examples improved on them; the contribution of
  bass-split against Alberti against syncopation is not measured.
- **How the bass is determined from the score is not stated in the pages as read.** One of the two
  input blocks is the spelled bass (§3.1), and §3.1 does not say how it is extracted from a polyphonic
  texture.
- **Table 3 carries no per-dataset breakdown**, only the six-dataset average, so which datasets drive
  the movements differenced at §6.5 cannot be recovered.
- **★ WHICH DATA THE PER-EPOCH WEIGHT SELECTION USED IN THE FINAL RUNS IS NOT STATED.** §4.2 says the
  selected weights are those "that maximized the mean accuracy across the six conventional tasks", and
  §4.1 says that for the reported runs the model "was run once in the test set, this time including the
  validation portion as part of the training". **So in the runs Table 4 reports, the validation split is
  inside the training data, and the paper does not say what data the epoch-selection criterion was
  computed on.** *(NOT claimed: that the selection was made on the test split. The paper does not say
  either way, and the sentence about running "once in the test set" is equally consistent with selection
  on the training data. What is established is that the paper leaves it open.)*
- **The GRU layer widths are not stated in the prose.** §3.3 gives the two dense widths (64 and 32) and
  says only that two bidirectional GRU layers follow; the diagram prints 640×60 after each.

### §7.3 What is both measured and structural here

For a reader of this record deciding what this paper supplies that a design could rest on, as against
what is only reported:

1. **Spelled input and spelled output throughout, at a cost the paper measures as nil.** The two-hot
   19-feature encoding (12 pitch classes + 7 letters) replaces a 35-way spelled encoding "without any
   observable compromise in performance" (§3.1) while reducing the input width from 70 to 38. **The
   claim of no compromise is the paper's own and no ablation supporting it appears in the pages as
   read** — Table 3's four configurations vary the task count and the synthetic data, not the encoding.
2. **The separation of bass from chroma into independent convolutional blocks**, which is one of the
   three differences the paper claims against its closest predecessor (§3).
3. **A label per thirty-second note, with segmentation unevaluated** — the granularity is structural,
   the segmentation question is open by the paper's own statement.
4. **The reconstruction result**: decomposing the Roman numeral differently — key, inversion and one
   75-way class — beats the conventional six-task decomposition in every printed row (§6.6). **This is
   a result about the DECOMPOSITION rather than about the network**, so it does not depend on this
   particular architecture. *(NOT claimed: that it is the only finding here that transfers. No
   enumeration of what transfers was made, and this list is a selection rather than a partition.)*
   **★ ONE BOUND ON IT, NARROWED HERE AT THE CROSS-CHECK (§9.4).** §4.2 says the saved weights chosen
   for each run are those "that maximized the mean accuracy across the six conventional tasks" — so
   **the weights at which RN_alt is compared against RN_conv were selected on the conventional tasks'
   own criterion**, CommonRNs having no part in the selection. The comparison is therefore made on the
   other method's terms, which makes the ten positive margins a conservative reading of RN_alt rather
   than a favourable one. *(NOT claimed: that a CommonRNs-aware selection would widen them. The paper
   runs no such selection and this read measures nothing.)*
5. **The sub-task errors are strongly correlated** (§6.8), derived here from the paper's own marginals.
   A design that treats sub-task accuracies as independent will underestimate joint accuracy
   substantially — by 8.6 points on the three-task reconstruction and by 17.4 on the six-task one, on
   this paper's own Full test set row.
6. **The transposition-admission rule**: a transposed copy is admitted only if every modulation in the
   piece stays inside the target key-signature range (§3.5.1). This makes augmentation depth depend on
   a piece's tonal range, and no distribution for it is reported in the pages as read.

### §7.4 What this paper's reference list gives, and the bound on that statement

The reference list transcribed at §5.7 names, among others: the RomanText format paper [4]; the ABC [27],
TAVERN [29] and BPS [6] dataset papers; the openscore lieder corpus [5]; Micchi, Gotham and Giraud 2020
[20]; three Chen and Su papers [6,18,19]; Temperley's *The Cognition of Basic Musical Structures* [10]
and "The line of fifths" [24]; Raphael and Stoddard [13]; Illescas et al. [14]; Magalhães and de Haas
[15]; Winograd [8]; Maxwell [9]; the non-chord-tone paper of Ju et al. [23]; and the Melisma pointers
[11,12].

**THE BOUND: this read did not open `docs/research_papers/BIBLIOGRAPHY.md`, `reading_pass/candidacy_upgrades.md`,
the slice derivation, `population.md` or the findings surface, and ran no search of the repository.** So
this file asserts NOTHING about which of these references the record already holds, which are already
candidacy rows, or which would be new. That half is the first extract's, and this side takes no position
on it. The list above is a transcription of what this paper prints and nothing more.

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

After §0 to §7 were written and before anything was landed, this read went back to the paper and
re-opened, as fresh page-image requests, **every one of the eight pages**: page 3 before Table 1 and
Figure 1 were transcribed; pages 5 and 6 for Tables 2, 3 and 4; page 2 for the pitch-encoding paragraph,
which carries a claimed defect; pages 7 and 8 for the reference list; page 4 for §3.5 and Figure 2; and
page 1 for the title block, the licence line, the abstract and §1. **No page of the eight went
un-re-opened**, which is said plainly because the previous two sittings of this line each had to record
pages that did not get a second look.

**The page-image fault did not fire.** Page-image requests are named rather than totalled: pages 1–4 and
5–8 for the whole read; then 3; then 5–6; then 2; then 7–8; then 4; then 1. **Every image was present
and legible, checked at the image and not at the call's success line.** One further request — the
deliberately out-of-range one that established the page count — returned the refusal it was made for and
no image. **None of this is evidence the fault is gone.**

**What the read-back confirmed rather than changed.** Table 2's thirty-six cells and six totals, Table
3's twenty-four cells and its six bold marks, Table 4's whole grid including its en-dashes and its
parenthesised standard deviations, Figure 1's thirteen block shapes and eight main-path shapes and
eleven class counts, the thirty-two references, and every quotation in §2 — all as this file had them.
**The only figure the read-back moved is named at §8.2, item 10, and it is a bold mark and not a value.**

### §8.2 What the read-back and the sweep struck in this side's own writing

Named rather than counted. Every one is corrected above.

1. *"Every location in this file is given by the paper's own printed section number…"* — an absolute
   about this file's own practice. Narrowed, and the practice stated as the rule it is.
2. *"Audio appears nowhere in the method"* and *"Nothing in the method reads audio"* — two unbounded
   negatives over a document this read did not search. Both bounded to the method sections as read, with
   the two places the word does occur named.
3. *"Nothing here required the record's own account of the paper, and nothing here contradicts it"* — a
   claim of agreement with a record this read never opened. Replaced by an item-by-item comparison
   against the one entry this side actually read, and by a sentence saying no other account was
   consulted. **This is the tell reported at §8.3(iii).**
4. The licence line had been quoted in part, as a "mark" plus a copyright line. Re-read at page 1 and
   given as the sentence the paper prints, with its labelled Attribution line separated from it.
5. §3.3's repertoire bullet asserted that the repertoire **is** common-practice Western tonal music "by
   the six datasets used". **That is this read's inference and not the paper's claim**, and the six
   datasets do not all name their content: the composer is named by this paper for four of them and not
   for TAVERN or When-in-Rome. Both corrections made at the bullet.
6. Claim 13 said the model's Roman numeral accuracy exceeds "every model it is compared against". **The
   Chen and Su 2019 row prints no Roman numeral value**, so it is outside the comparison rather than
   beaten by it. The population is now named with its figures.
7. §6.5 named *"the largest fall is the −1.4 on key"*. **−1.4 occurs twice in the same table of
   differences** — on key and on inversion — so naming one of a tie as the largest is false against the
   table standing beside it. Both are now named. **This is the tell reported at §8.3(ii).**
8. §6.7 called the key column's agreement with the unweighted mean *"a coincidence of that column and
   not a method"* — a statement about cause where what this read has is a residual. Replaced by the two
   residuals that refute the unweighted reading.
9. §6.10 said every ComRN value lies *"far below"* the ceiling. Replaced by the range (59.9 to 70.2) and
   the margin (at least 27 points), so the reader can see the size rather than take the adjective.
10. **★ §7.1(d) said ONE bolded value in Table 4 has no comparator. The read-back at page 6 found a
    SECOND** — the WTC / Full dataset row's RN_conv 46.2, bolded on a row that has no comparison row at
    all. **The item is widened, and it is the one place where the read-back changed a finding rather
    than a wording.**
11. §7.1(a)'s *"the paper does not note the exception"* — an unbounded negative over the document.
    Bounded to the pages as read.
12. §7.1(f) said the accuracy unit is *"never defined at any table"*. Bounded, and the two captions
    quoted so a reader can see what they do say.
13. Four bullets of §7.2 asserted that something is "never given" or "not stated" without a bound. All
    bounded to the eight pages as read. The augmented-training-set bullet was additionally wrong in
    form: that Table 2's counts are pre-augmentation is an inference from §4.1's ordering, and is now
    stated as one.
14. **★ §7.3 item 4 called the reconstruction result *"the one finding of this paper that transfers
    without the architecture"*** — a uniqueness claim over a set this read never enumerated, in a list
    that is a selection and not a partition. Struck, with the NOT-claimed said at the site. **This is
    the tell reported at §8.3(i).**
15. §7.3 item 1 said the no-compromise claim *"carries no ablation in the text"*. Bounded, and what
    Table 3's four configurations actually vary is now named.
16. §5.7 had silently shortened the printed venue names. **The normalization is now declared at the head
    of that section**, together with the fact that reference [4]'s printed misspelling is transcribed as
    printed and that reference [32]'s author list is abbreviated.

**And two items were ADDED by the read-back rather than struck**, both at §7.1(g): reference [4]'s
printed *"numerial"*, and §1's worked example listing four components of a Roman numeral label while
omitting the scale degree — recorded as an incompleteness in an illustration, with the explicit note
that the sentence does not claim to be exhaustive and that its gloss is otherwise correct.

### §8.3 The degradation tells, reported unprompted

The user's standing rule of 2026-08-15 asks that a side recognise when its own work has degraded and say
so without being asked, on named tells. **Two of the named tells fired in this side's own writing, and
the instances are named rather than totalled.**

**Tell A — a count, a proportion, a ranking or a superlative put on this side's own reading or its own
findings without deriving it.**

- *(i)* **§7.3 item 4 called one result *"the one finding of this paper that transfers without the
  architecture"*** — a uniqueness claim over a set never enumerated, written inside a list that is
  explicitly a selection. **Caught at the sweep.**
- *(ii)* **§6.5 named *"the largest fall"* over a table of differences in which that value occurs
  twice** — a superlative refuted by the table printed immediately above the sentence. **Caught at the
  sweep.** It is the same shape as (i) in the opposite direction: a ranking asserted rather than read
  off.

**Tell B — citing a summary instead of the source, and an unmarked relay presented as established.**

- *(iii)* **§1 closed with *"nothing here contradicts [the record's own account of the paper]"*** — a
  statement about agreement with a record this read did not open, written from the handoff entry that
  booted this session. **Caught at the sweep and replaced by a comparison against the one entry actually
  read, item by item, with the reach of that comparison stated.**

**WHAT THE THRESHOLD MEANS HERE, STATED WITHOUT INFLATION.** **What fired is TWO named tells** — the
count-and-ranking one twice, and the summary-instead-of-source one once — **not several different tells,
and nothing more than that is claimed.** The instances are named above and are not ranked against one
another. **That all three were caught by a pass of this side's own does NOT lower the count**: the
hundred-and-eightieth and hundred-and-seventy-ninth entries each record exactly that of their own
sittings, read at those entries' own texts here. **The recommendation that follows is the one the two
preceding sittings made: hand over at a verified stop rather than take a second member.**

### §8.4 The bound on this section

**The read-back and the sweep are further passes over the same writing by the same side.** The
read-back caught what the writing did not; the sweep caught what the read-back did not. **Nothing here
says a third pass would come back empty**, and the cross-check recorded at §9 is the only pass in this
file's history made against a reading that is not this one's.

**What these two passes did not do.** They did not open this paper's first extract — that is step 7 of
the procedure and happens after this file lands. They opened no other paper, no other extract, and no
file of the record. They ran no web access and swept no repository. **They changed no value transcribed
from the paper**: every correction at §8.2 is in this side's account of its own reach, of what is absent
from the paper, or of a ranking among its own findings, except item 10, which is a bold mark read again
at the page.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**After §0 to §8 had been written and landed**, and not before, row 48's first extract was staged and
read whole: `reading_pass/extracts/napoleslopez-gotham-fujinaga-2021-augmentednet-roman-numeral-analysis-network.md`,
**52,811 bytes** at this sitting's own staging call, dated 2026-09-06 in its own banner. That is step 7
of the eight-step procedure, and it is the first time in this sitting that any account of this paper
other than the paper itself was opened, the boot entry's identity lines excepted (§0).

**THE ASYMMETRY OF WHAT COULD BE COMPARED, STATED BEFORE THE RESULT.** That file has two halves. One is
about the paper, and this read can meet it at the paper. **The other points INTO this project's record
— `FRAMEWORK.md` at DP-A and §S4(a), `population.md`'s V9 and its row 13, the slice derivation, the
bibliography, the findings surface, the candidacy file, and the eleven findings it routes — and this
side opened none of those.** On that half this file is **silent, and silence is not a second opinion**:
nothing below confirms, disputes or is evidence about any of it, including that file's CENTRAL verdict,
its seven-places claim, and its own record of a defect it corrected after landing.

### §9.2 What both reads transcribed, and where they agree

**Every printed value the two reads both transcribed agrees.** Named rather than counted:

- **Identity in full** — all three authors, their affiliations and e-mail addresses, the printed title,
  the attribution box word for word, the CC BY 4.0 licence, the running header, the printed page range
  404–411, eight pages, and the held file at **773,071 bytes**.
- **Table 2's totals** — 241 files (1424 sequences) training, 56 (333) validation, 56 (329) test.
- **The input encoding** — 640 frames, 80 quarter notes, the thirty-second-note timestep, 19 features
  per spelled pitch as 12 + 7, 38 per timestep, and the 70 = 35 + 35 attributed to Micchi et al.
- **All eleven task class counts** — Key 34, PrimDegree 21, SecDegree 21, Quality 15, Inversion 4,
  Root 35, CommonRNs 75, HarmRhythm 2, Bass 35, Tonicization 34, PitchClassSet 93 — and the four added
  key classes {F♭, G♯, d♭, e♯}.
- **Table 3 in full** — all twenty-four cells, **and the bolding, cell for cell**, including the 78.6 on
  AugN₆₊'s inversion.
- **Every Table 4 cell the first extract transcribes** — its six comparator rows and the AugmentedNet
  rows beside them — against this read's transcription of the whole grid.
- **The ten RN_alt − RN_conv differences, derived independently by both reads and identical in all ten:**
  +5.1, +6.0, +3.5, +3.9, +10.3, +1.7, +4.0, +3.9, +3.4, +3.4.
- **Every protocol constant** — 100 epochs, batch 16, rmsprop, 10⁻³, ReLU with tanh in the GRUs, the
  three training times, the ~90,000 parameters, the 8-flat-to-8-sharp range, the 3–4-note texturization
  scope, and both footnotes.
- **Reference [3] in full**, including its pagination, and reference [20]'s and [23]'s identification.
- **Every quotation the two files share from §3.1, §3.4, §3.4.1, §3.5, §4.1, §4.2, §4.3 and §5.**

**★ AND TWO AGREEMENTS REACHED INDEPENDENTLY THAT ARE WORTH NAMING AS SUCH.** *(i)* **Both reads
transcribed the pitch-class range as the paper prints it, "(0–12)", and both transcribed the count as
"1 of 12 pitch classes"** — so the string this read reports as a defect at §7.1(b) is confirmed at a
second, independent transcription of the same sentence. *(That file records the string without
remarking on it; the remark is this read's.)* *(ii)* **Both reads independently reached the Table 3 "RN"
column's ambiguity and both reasoned to it the same way** — that the six-task configurations have no
CommonRNs head, so their RN cells must be RN_conv, and that the paper does not say what the eleven-task
rows' cells are. Two reads arriving separately at one unstated thing is the strongest agreement in this
comparison.

### §9.3 ★ The disagreements — three, all against the first extract, and none moves a transcribed value

**(a) A QUOTATION WHOSE WORDS ARE NOT THE PAPER'S, IN THE FOOTNOTE THIS READ THEN ADOPTED.** That file
quotes footnote 1 as *"Note that, in practice, WiR is also a meta-collection and standardization effort,
where several of these datasets **are contained**"*. **The paper prints *"…where several of these
datasets (e.g., ABC) **have been converted into a common representation**."*** — established at printed
page 407 at the whole read and again at a separate opening of that page at the read-back. **The gloss
that file draws from it survives**: the footnote does say that other datasets of the six are inside WiR.
**The quoted words are not what the page carries**, and the paper's actual wording is the stronger
evidence, naming ABC specifically. No value moves. *(This read adopted the footnote at §5.3 from that
file's flag and quoted it from the page, which is why the disagreement was met at all.)*

**(b) ★ A MECHANISM STATED AGAINST THE PAPER'S OWN NEXT SENTENCE, AND IT IS THE ONE OF THE THREE A
DESIGN CONSUMER WOULD CARRY WRONG.** That file states: *"Batch normalization **before every
activation**; ReLU everywhere except the two GRU layers (hyperbolic tangent)"*. **The paper's §4.2 says
the opposite of half of that, in two consecutive sentences: *"Each of the layers in the network is
accompanied by batch normalization [30] before the activation function. In the recurrent layers, we
apply the batch normalization after the activation function."*** — established at printed page 408 at
the whole read and again at a separate opening at the read-back. **So the recurrent layers are the
paper's own stated exception, and "before every activation" is false of them.** The ReLU half of the
sentence is right. No measured value moves, and nothing in either file's findings rests on it — **but a
later reader reproducing this network from that sentence would place two of its layers' normalization on
the wrong side of the activation**, which is why it is reported rather than waved through.

**(c) A LOCATOR IMPRECISION, AT THREE OF THAT FILE'S CITATIONS.** That file cites §3.1 as *"pages
405–406"* and §3.2–§3.3 as *"pages 406"*. **In the copy as read, §3.1, §3.2 and §3.3 are printed whole
on page 405**; page 406 opens with Figure 1 and carries §3.4 and §3.4.1, which that file cites
correctly. That file's own banner undertakes that *"every location below is given as the printed
section, table or figure number together with the proceedings page"*. The sense is unchanged and no
value moves.

**WHY THE THREE ARE REPORTED AND NOT WAVED THROUGH.** By the test this line has been using, **all three
belong with the ones that move no value** — rather than with the dropped parenthesis and the wrong F₁
that other rows of this line record. **(b) is the one with a consequence beyond its wording**, because
it is a statement about what the network does rather than about where a sentence sits. *(Said of the
members whose nature this side read an account of — **rows 45's, 18's, 8's and 30's**. Row 45's four
items are at the hundred-and-eightieth entry's own (xi), and row 18's at the hundred-and-seventy-ninth's,
both of which this side read whole; **rows 8's and 30's are a RELAY through those entries' watch lines.**
No comparison is made with any other row, whose natures this side read no account of.)*

**AND THE FIRST EXTRACT IS UNTOUCHED.** Nothing in that file was edited. The standing ground is this
line's own: rewriting another read's text destroys what the doubling is comparing. **The three
disagreements stand with the user as the question whether that file's defects are corrected at their own
sites.**

### §9.4 What the first extract has that this read did not — adopted here and marked at its site

Three, each carried into this file at the place it belongs and marked there as adopted:

1. **Footnote 1's statement that the six datasets need not be disjoint** — adopted at **§5.3**, quoted
   from the page rather than from that file (§9.3(a)), and developed there into what the paper does and
   does not say about overlap between the splits.
2. **That the +4.0 margin on the one row with printed spreads sits under both of them** — adopted at
   **§6.6**, with the figures re-read at Table 4.
3. **That the saved-weight selection maximizes the mean accuracy across the six CONVENTIONAL tasks, so
   the RN_alt-against-RN_conv comparison is made at weights chosen on the conventional method's own
   criterion** — adopted at **§7.3 item 4** as a bound on that item. This is the sharpest of the three
   and this read had the constituent fact (§2.12, §5.6) without drawing the consequence.

### §9.5 What this read has that the first extract does not

Named rather than counted, and the four that bear on how a printed value or a stated claim of the paper
is read are marked ★:

- **★ That §4.3's "best-performing configuration" sentence is refuted on one of its six axes by Table
  3's own bolding** — AugN₆₊'s 78.6 against AugN₁₁₊'s 77.2 on inversion (§7.1(a)). That file transcribes
  the table with the same bolding and does not remark on it.
- **★ That Table 4's first row is not the aggregate of the six dataset rows beneath it under either an
  unweighted or a test-sequence-weighted reading**, with the residual on every column both ways (§6.7).
- **★ That the reconstruction accuracies far exceed the product of their sub-task accuracies** — by 8.6
  points for RN_alt and 17.4 for RN_conv on the Full test set row — so the sub-task errors co-occur
  rather than compound (§6.8), with the two bounds that derivation carries.
- **★ That four of the five new tasks have no reported accuracy anywhere in the eight pages** (§7.2).
  That file records that the harmonic-rhythm head is consumed by nothing; it does not state that
  harmonic rhythm, bass, tonicization and pitch class set alike are never scored.
- Figure 1's thirteen convolutional-block shapes and eight main-path shapes transcribed (§5.1), and the
  block's widths checked against the caption's own halving rule, closing at every step and at 82 and 164
  (§6.2).
- Table 2's six column sums closed against their printed totals (§6.1).
- The key vocabulary closed in both directions — 17 signatures × 2 modes = 34, and the four added
  classes being exactly the eight-flat and eight-sharp keys in both modes (§6.4).
- Table 4's two bolded values that have no comparator and are not column maxima (§7.1(d)).
- That neither table's caption defines the accuracy's denominator (§7.1(f)).
- Reference [4]'s printed misspelling *"numerial"*, and §1's worked example listing four components of a
  Roman numeral label while omitting the scale degree (§7.1(g)).
- The reference list transcribed entry by entry with venues, volumes and pagination (§5.7); that file
  transcribes reference [3] in full and names the rest.
- The ten printed ComRN values read against the stated ~98 % ceiling, all at least 27 points under it
  (§6.10).
- Table 3's four rows differenced in both directions with both extremes named (§6.5) — that file
  differences three of the same four pairs and reaches the same signs on every cell they share, which is
  a further agreement rather than a difference.
- Table 1's shape, caption and coverage recorded with an explicit refusal to transcribe its
  seventy-five cells at the resolution available (§5.2).

### §9.6 What the cross-check does NOT establish

- **It does not reach the half of the first extract that points into this project's record**, which is
  most of that file's own findings. This side opened none of those files and takes no position on any of
  them (§9.1).
- **It is not exhaustive.** It ran over what the two files both carry, and a later reader comparing them
  again may find more. No claim is made that the three disagreements at §9.3 are all there are.
- **It establishes nothing about which read is the more reliable.** Three disagreements went one way
  this time; the narrowing at §7.3 item 4 went the other, and the three adoptions at §9.4 are things
  this read did not have.
- **It changed no value in this file taken from the paper.** What it changed is recorded at §9.4 as
  three additions and one narrowing, each at its own site.
- **It is the only pass in this file's history made against a reading that is not this one's** (§8.4).
  Every other pass — the read-back, the sweep — is this side re-reading itself.

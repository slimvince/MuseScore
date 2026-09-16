# EXTRACT — Ni, McVicar, Santos-Rodríguez & De Bie, "An End-to-End Machine Learning System for Harmonic Analysis of Music" (the held arXiv preprint of the TASLP 2012 paper) — Task B candidacy row 3, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-05).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All six pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.** The
> held document prints no page numbers; every location below is the page's position in the held file
> (p. 1 to p. 6) and the paper's own section.
>
> **Why this paper and its place in L2's slice.** It is row 3 of `reading_pass/candidacy_upgrades.md`,
> ADMITTED there as *"An end-to-end system deciding chord and key; a whole-chain candidate to compare
> L2's charter against. Audio domain, carried as a caveat under (ii)."*
> `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 places it in L2's slice: *"Chord and key decided
> end to end; the row admits it as a whole-chain comparison for L2's charter. Audio; the domain travels
> as a caveat."* It is sixth in group 1 of the proposed reading order ("the joint tonality-and-chord
> decision") and the fifth member read (rows 2 and 44 being unreadable from here). **The record cites
> this paper nowhere else**: a `Grep` of the staged tree for the authors' names and for "end-to-end"
> found only the bibliography row, the candidacy row and the slice derivation row. Ruling 1 of
> `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate: no derivation before L2's slice of
> Task B is read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — with one finding

Yizhao Ni, Matt McVicar and Tijl De Bie (Intelligent Systems Lab, Dept. of Engineering Mathematics,
University of Bristol) and Raul Santos-Rodríguez (Signal Theory and Communications Dept., Universidad
Carlos III de Madrid), "An End-to-End Machine Learning System for Harmonic Analysis of Music". **The
held document is the arXiv preprint: the margin stamp reads `arXiv:1107.4969v1 [cs.SD] 25 Jul 2011`,
the licence block reads *"© 2010 The Authors"* under Creative Commons BY-NC-SA 3.0, and no journal,
volume or page appears anywhere in it.** Six pages; five sections (Introduction; System description —
2.1 Loudness based chromagram, 2.2 HP HMM topology, 2.3 Search space reduction; Experiments — 3.1 to
3.4; Conclusions and future work; References, twenty entries); three figures and three tables.

**File:** `docs/research_papers/ni_mcvicar_santosrodriguez_debie_2012_taslp_end_to_end_harmonic_analysis.pdf`
(424,217 bytes at the listing). `docs/research_papers/BIBLIOGRAPHY.md` line 17 names *"arXiv:1107.4969
(IEEE TASLP 20(6), 2012)"* in one row with the arXiv link; the file name carries "2012_taslp". **What is
held is the 2011 preprint; whether the journal version differs from it is not establishable from what is
held.** Routed to the bibliography reconciliation as an identity finding of the same shape as row 28's
(see finding (1) below).

## Claims, labeled

### What the method decides, and how it decides it jointly

**★ [FACT, p. 1, Abstract]** *"We present a new system for simultaneous estimation of keys, chords, and
bass notes from music audio. It makes use of a novel chromagram representation of audio that takes
perception of loudness into account. Furthermore, it is fully based on machine learning (instead of
expert knowledge), such that it is potentially applicable to a wider range of genres as long as
training data is available."*

**★ [FACT, p. 1, §1] The joint decision is the authors' stated motive, and the system is named for it.**
*"Since chords and keys are musical attributes closely related to each other in western tonal music [8],
the idea to learn both progressions of a song simultaneously comes naturally."* The system is the
*"Harmony Progression (HP) system"*, *"a simultaneous key/chord predictor that also identifies bass
notes"* (p. 2). The authors place it against expert-knowledge systems (their "Approach A") as a
machine-learning system (their "Approach B") with every parameter *"learnt via maximum likelihood
estimation (MLE)"* (Figure 2 caption, p. 2) from annotated training data — **supervised, not
unsupervised** as row 1's model is.

**★ [FACT, p. 3, §2.2] THREE HIDDEN CHAINS — KEY, CHORD, BASS — AND TWO OBSERVED CHROMAGRAMS.** *"The
hidden variables correspond to the key K, the chord C and the bass annotations B … Under this
representation, a chord is decomposed into two aspects: chord label and bass note. Take the chord
A:maj/3 for example, the chord state is c = A:maj and the bass state is b = C#. Accordingly, the
observed chromagrams are decomposed into two parts: the treble chromagram X^c which is emitted by the
chord sequence c and the bass chromagram X^b which is emitted by the bass sequence b. The reason of
applying this decomposition is that different chords can have the same bass note, resulting in similar
chromagrams in low frequency domain."* The joint probability (p. 3, the unnumbered formula after Θ) is
p_i(k₁) p_i(c₁) p_i(b₁) ∏ₜ p_t(kₜ | kₜ₋₁) p_t(cₜ | cₜ₋₁, kₜ) p_e(X^c_t | cₜ) p_t(bₜ | bₜ₋₁) p_t(bₜ | cₜ)
p_e(X^b_t | bₜ). Emissions are *"12-dimensional Gaussians"* per state, means and covariances learnt by
MLE.

**★ [FACT, p. 3, §2.2] THE KEY–CHORD COUPLING IS A CONDITIONAL IN THE CHORD CHAIN, POOLED BY
TRANSPOSITION.** *"Since the chord transition is strongly influenced by the underlying key [13], this
probability is modelled as key dependent. Under the assumption that relative chord transitions are key
independent, we transposed all sequences to a common key k and learn p_t(c | c̄, k) from the transposed
sequences. This allowed us to get 12 times as much information from the data source"*. The key chain
itself is a plain first-order transition p_t(k | k̄), learnt by counting. **No chord is vetoed under any
key by the model; the coupling is a probability.** (The hard constraints below are a decoding
approximation, stated as such.)

**[FACT, p. 3, §2.2 and footnote 2] The bass chain is coupled to the chord by a second conditional,
and the authors state the factorisation is not a proper one.** p_t(b | c) *"models the probability of a
bass note under a chord label so as to capture chord inversions"*; p_t(b | b̄) *"is also added, with the
purpose of modelling the continuity of bass notes and capturing ascending and descending bassline
progressions."* Footnote 2: *"Note that we use p_t(bₜ | bₜ₋₁, cₜ) = p_t(bₜ | cₜ) p_t(bₜ | bₜ₋₁), which
from a purely probabilistic perspective is not correct. However, this simplification reduces
computational and statistical cost and results in better performance in practice."*

**★ [FACT, p. 3, §2.3] Decoding is joint Viterbi over the three chains, and its cost is stated —
O(|A_k|²|A_c|²|A_b|²|T|) — with three search-space reductions, two of them HARD ZEROES imposed at
decode time.** *(2.3.1)* the key transition constraint: a key transition seen fewer than γ times in
training gets probability zero; *(2.3.2)* the chord-to-bass constraint: only the τ most frequent bass
notes per chord are permitted (*"When τ = 3, the constraint is equivalent to using root position, first
and second inversions of a chord"*); *(2.3.3)* the chord alphabet constraint: *"using a simple HMM with
only chords as the hidden chain, we first apply a max-Gamma decoder [17] to a song and obtain the most
probable chords A'_c. Then, we force the HP HMM chord transition probability to be zero for chords that
are absent in this output."* Figure 3 (p. 5): the reductions cut decoding time *"dramatically while
retaining a high performance"*; the chord alphabet constraint *"did not decrease the performance (in
fact it had a slight improvement)"*.

### The front end

**[FACT, p. 2, §2.1 and p. 4, §3.2]** A loudness-based chromagram: constant-Q spectrum → sound power
level in dB → A-weighting → summed per pitch class → min–max normalised per song. Preprocessing:
mono at 11025 Hz, harmonic/percussive separation, tuning, a bass chromagram over A1–G♯3 (55–207.65 Hz)
and a treble chromagram over A3–G♯6 (220–1661.2 Hz), beat tracking, and **the median chroma between
consecutive beats as one frame**, with the annotations beat-synchronised by majority label.

### The experiments, as stated

**[FACT, p. 3–4, §3.1–3.3] Corpus and protocol.** The MIREX 2010 chord-detection dataset, 217 songs,
ground-truth keys and chords from isophonics.net, bass notes *"extracted directly from the ground truth
chord annotations"*. Major/minor task: 24 keys, 25 chords (12 major, 12 minor, no-chord), 13 bass
states; two-thirds of each album for training, one-third for testing, *"repeated 102 times to access
variance"*; metrics chord overlap ratio (OR) and chord weighted average overlap ratio (WAOR) as in
MIREX 2010, predominant-key accuracy (key-P: the first key of the ground truth against the most
prevalent predicted key), and frame-based bass accuracy.

**★ [FACT, p. 4, Table 1] Major/minor results, reproduced.**

| System | Chord OR % | Chord WAOR % | Key-P % | Bass F-acc % |
|---|---|---|---|---|
| HMM-C (chord only, treble+bass chroma concatenated) | 77.82** | 77.22** | — | — |
| HMM-B (bass only) | — | — | — | 73.62** |
| K-HMM (key-specific HMM [9]) | 78.22** | 77.62** | 76.88* | — |
| HP (this paper) | **79.37** | **78.82** | **77.36** | **83.81** |
| HP-P (trained and tested on the whole set) | 81.52 | 81.37 | 83.33 | 85.15 |

Caption: *"The improvement of HP is significant at a level < 10⁻⁴⁰ and < 10⁻¹ over the performances
marked by ** and * respectively."* Text: *"Table 1 also indicates that increasing the complexity of
models helps harmonic estimation, and that the HP system achieves the best performance on all
evaluations."* The best MIREX 2010 pre-trained system (MD1) is quoted at 80.22 OR / 79.45 WAOR against
HP-P's 81.52 / 81.37, with the authors' own caveat that HP-P *"is subject to overfitting the data"* and
that no paired test was possible. **Read against the L2 question:** the chord gain from adding the key
chain (HMM-C → K-HMM) is 0.40 OR; from adding the bass chain on top (K-HMM → HP) 1.15 OR; the key gain
from adding the bass chain 0.48 key-P. **There is no key-only baseline**, so the paper measures no
"separate key estimation" figure of the kind DP-B rests on.

**[FACT, p. 4–5, §3.4, Tables 2–3] Full-chord task.** 121 chords (12 roots × maj, min, maj/3, maj/5,
maj6, maj7, min7, 7, dim, aug, plus N); compared with Chordino (CH) since the musical probabilistic
model (MP) is not public; τ = 3, γ = 10. Table 3: CH 50.31 chord precision / 52.35 note-based chord
precision / 76.94 WAOR; HP-L (leave-one-out) 63.63 / 65.24 / 81.05; HP-P 70.26 / 71.96 / 82.98.
Table 2: HP faster and lighter than MP on two songs (58 s against 131 s; 0.48 GB against 6 GB). The
authors attribute CH's low precision to its predicting *"many complex chords (notably 7ths)"*.

**[FACT, p. 6, §4] Named future work:** *"We will also move towards discriminative approaches using the
same HMM topology, which might lead to a more robust and powerful harmonic analysis tool."*

## Measured results, as the paper states them

Tables 1 and 3 above, with the corpus (MIREX 2010 / isophonics, 217 songs, pop audio), the metrics and
the protocol as stated. The only ablation is the model ladder HMM-C → K-HMM → HP on the major/minor
task; no ablation of the search-space reductions beyond Figure 3's curves; no held-out figure for
HP-P by construction.

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** Audio; a beat tracker (the frame is a beat); a tuning step;
harmonic/percussive separation; annotated training data for every parameter (keys, chords and bass per
song). It reads no score, no notes, no spelling, no metre beyond beats, no voices.

**What it HANDS downstream.** Per beat, one (key, chord, bass) triple as the single Viterbi path —
chord as an absolute label (A:maj), bass as a pitch class — and nothing else: no scale degree or
Roman numeral, no chord-tone assignment, no cadence, no figured bass, **no alternatives and no
confidences.**

**Its own STATED SCOPE and limits.**
- **Domain:** audio, pop (the Beatles-centred MIREX set); the authors' own generality claim is
  conditional — *"potentially applicable to a wider range of genres as long as training data is
  available"* (p. 1).
- **Vocabulary:** major/minor keys; 25 or 121 chords; 13 bass states.
- **Granularity:** one frame per beat; no sub-beat harmonic change.
- **Coupling:** chord conditioned on key by a pooled conditional; bass conditioned on chord and on the
  previous bass by an admittedly improper product; two hard constraints (key transitions and chord
  alphabet) imposed at decode time as approximations, with their inertness on performance shown by
  curves rather than tables.
- **Fitting:** supervised MLE; the train/test split is by album with repeated random splits, and the
  authors state the whole-set figure is an overfit upper bound.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adopt (as a corroborating instance of the charter's coupling form):** the chord transition
  conditioned on the key, learnt pooled by transposition — the same conditional-not-veto shape as
  row 1's and row 27's, here in a supervised audio system. The pooling-by-transposition argument is the
  same as row 1's translation-invariance assumption, stated here as an assumption with the data gain
  named.
- **Adapt (a design the record already carries, in another form):** the BASS as a third hidden chain
  coupled to the chord by p(b | c) and to itself by p(b | b̄), so that inversion is decoded jointly with
  chord identity and bass continuity is a term. The record's legacy decision D-536 ("the bass note and
  the chord are chosen TOGETHER") and the live emission's bass factor (D-449) are neighbours of this
  design; this paper is a published precedent for making the bass a decoded variable rather than a
  factor, and for the improper-product simplification the authors chose over the correct joint.
- **Adapt (for DP-C's search question):** the two-stage chord-alphabet constraint — a cheap first pass
  to prune the vocabulary, then the full joint decode over the pruned set — reported as inert or slightly
  positive on accuracy. An L2 detail specification that prunes must argue for or against this shape;
  the paper gives only curves, no table.
- **Adapt (for DP-P):** the authors' closing intention to move to discriminative fitting on the same
  topology is a stated direction, not a result; nothing is carried out of it.
- **Must argue against:** the beat grid as the only harmonic boundary (L1's change points); absolute
  chord labels with no degree relative to the tonality (D-526); a key chain that is a bare first-order
  Markov chain with hard-zeroed rare transitions at decode time (a veto, though a decoding one); the
  single-path output; and the audio front end, which supplies nothing to a notated-input system.

## ★ Findings, routed and not applied

**(1) IDENTITY: the held file is the 2011 arXiv preprint, not the 2012 TASLP article the bibliography
row and the file name also name.** The stamp, the licence line and the absence of any journal marking
establish which version is held; whether the journal version differs is not establishable from what is
held. Same shape as row 28's finding; routed to the bibliography reconciliation. Nothing in the record
cites this paper for any claim, so nothing is affected.

**(2) A second measured instance for DP-B's question, of small size and without the separate-key
baseline that DP-B's ground has.** Adding the key chain to a chord-only HMM gains 0.40 points of chord
overlap on this corpus (Table 1, HMM-C → K-HMM); the paper measures no separate key estimation, so it
supplies no figure for the key side. Row 27's primary reports about 2 and about 5 points on the same
kind of corpus. This is a datum beside DP-B's ground, not a verdict on it, and the metric and system
differ; routed to the findings surface's DP-B block with that bound.

**(3) A published precedent for the bass as a decoded chain, with the authors' own admission that
their bass factorisation is improper.** Routed to L2's detail specification beside D-449 and the legacy
D-536; no verdict.

**(4) Hard zeroes at decode time as an approximation, defended by curves only.** Two of the three
reductions veto states outright during the search; the authors show decoding time and WAOR curves and no
table. Bears on the L2 charter's boundary condition (every candidate reachable) as an instance of the
opposite practice adopted for speed, not for accuracy; routed to L2's detail specification.

**(5) No falsifier.** Nothing read contradicts any CHOSEN design point; the paper is corroborative of
the conditional coupling and silent on everything the charter fixes for notated input. **No STOP
fires** under the remedial commission's §5.

## Centrality

**NOT CENTRAL.** No ratified text cites this paper; its measurements are on pop audio with metrics the
record does not use; and every design element it exhibits that an L2 detail specification could cite
(the chord-given-key conditional; pooling by transposition; the bass as a decoded chain) has a primary
already read at the object in this slice or an owner in the record. What it adds is corroboration and
one small datum (finding (2)). A second independent extraction is therefore **not owed** under the
original commission's §4 central-source rule; this verdict is challengeable at the progress record.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (4) are routed and written
nowhere else. It does not fetch or read the TASLP 2012 journal version. It opens no code, touches no
measurement tool, no corpus, no golden and nothing under `tools/`. It writes no open-items row and
allocates no decisions-register identity. It reads no other paper and takes no decision about the order
of the remaining slice.

---

*Provenance: written 2026-09-05 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_fifteen.md`, in the sitting after it read and landed row 8, after
the ordinary session-start read (`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived
gating answer). Read for this extract, at the files: `reading_pass/candidacy_upgrades.md` whole (row 3
at its line 65), `cowork_l2_task_b_slice_derivation_2026_09_05.md` at its row 3,
`docs/research_papers/BIBLIOGRAPHY.md` at line 17, and a `Grep` of the staged tree for "McVicar",
"Ni," and "end-to-end", which found no citation of this paper in `FRAMEWORK.md` or the findings
surface. The paper itself was read at the object as page images, all six pages. No shell command was run
on the repository or on any staged copy of it for content or for listings. No figure of this project's
own measurement is restated (#17f, D-431); every value above is the paper's own.*

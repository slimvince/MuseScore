# EXTRACT — Noland & Sandler, "Key Estimation Using a Hidden Markov Model" (ISMIR 2006) — Task B candidacy row 26, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-05).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All six pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.** The
> held document prints no page numbers; every location below is the page's position in the held file
> (p. 1 to p. 6) and the paper's own section.
>
> **Why this paper and its place in L2's slice.** It is row 26 of `reading_pass/candidacy_upgrades.md`,
> ADMITTED there as *"A tonality-deciding method with an explicit transition structure; DP-E's* where
> may the tonality change *is that structure's question."* `cowork_l2_task_b_slice_derivation_2026_09_05.md`
> §4 places it in L2's slice: *"Tonality with an explicit transition structure — DP-E's* where may the
> tonality change*."* It is eighth in group 1 of the proposed reading order ("the joint
> tonality-and-chord decision") and the sixth member read (rows 2 and 44 being unreadable from here).
> **The record cites this paper in exactly one place besides the bibliography, the candidacy row and
> the slice row:** `FRAMEWORK.md` §S4(b), where it is the provenance of the EXCLUDED time-scale
> decomposition — *"Noland and Sandler, who estimate tonality downstream of a completed chord
> transcription."* A `Grep` of the staged tree (`FRAMEWORK.md`, the findings surface, the bibliography,
> the candidacy derivation, the slice derivation) for "Noland" and "Sandler" found no other citation.
> Ruling 1 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate: no derivation before
> L2's slice of Task B is read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — confirmed, no finding

Katy Noland and Mark Sandler, Centre for Digital Music, Queen Mary, University of London, "Key
Estimation Using a Hidden Markov Model". The permission block reads *"© 2006 University of Victoria"*,
which is the ISMIR 2006 host. **The printed title, the authors and the venue match the bibliography's
row** (`docs/research_papers/BIBLIOGRAPHY.md` line 40: *"Key Estimation Using a Hidden Markov Model,"
ISMIR 2006*). Six pages; six sections (Introduction; Model of Key Space — 2.1 Initialisation, 2.2
Training, 2.3 Decoding; Sample Segmentation Results; Evaluation Technique; Discussion; Conclusion),
fifteen references, four figures, four tables, and an appendix reproducing three of Krumhansl's tables.

**File:** `docs/research_papers/noland_sandler_2006_ismir_key_estimation_hmm.pdf` (417,537 bytes at
the listing).

## Claims, labeled

### What the method decides, and what it takes as given

**★ [FACT, p. 1, Abstract] The method decides the KEY ONLY, from CHORD SYMBOLS already given.** *"The
key space is modelled by a 24-state Hidden Markov Model (HMM), where each state represents one of the
24 major and minor keys, and each observation represents a chord transition, or pair of consecutive
chords."* The chords are not decided by the method: *"This paper describes a novel technique for
estimating the key of a musical recording from chord symbols on both a frame-by-frame and a per-track
basis"* (p. 1, §1); the chord symbols are *"hand annotations of the start and end times of every chord in
all of the first 8 Beatles albums, provided by Harte"* (p. 3, §3); and the Conclusion states *"Working
from chord symbols is intended as a means of testing the harmonic model without the problems associated
with audio analysis"* (p. 5, §6), audio-to-chord being planned future work.

**★ [FACT, p. 2, §2] The observation is a PAIR of consecutive chords, not a chord.** *"It was decided
that a pair of consecutive chords should be used for each observation, instead of a single chord, in
order to extend the temporal dependency across a greater number of frames."* Chord vocabulary: major,
minor, augmented and diminished triads, plus *no chord*; *"More complex chords have been excluded from
the model since chords that are not based on triads are very rare in the Western music repertoire for
which this analysis is intended."* **Inversions are discarded by construction:** *"All inversions of the
same chord are treated identically, which means that the choice of bass note does not affect the
estimated key."* (p. 2, §2.)

**★ [FACT, p. 2, §2] THE TRANSITION STRUCTURE — the reason the candidacy row admitted it.** *"Each state
represents a key, and the model is fully connected so that any key can move to any other key, or stay
the same. At each time step the key generates an observable chord transition."* **The key may therefore
change at EVERY time step, and the time step is a fixed sampling interval, not a chord boundary:** *"the
chord sequence was sampled at equal time intervals of 100 ms, such that sample times that fell between a
chord start and end time were given the corresponding chord label, and any others were labelled N, for
no chord"* (p. 4, §3).

### How the three parameter sets are initialised (p. 2–3, §2.1)

**[FACT, p. 2, §2.1.1] Initial state probabilities uniform**, 1/24: *"there is no reason to prefer any
key above any other."*

**★ [FACT, p. 3, §2.1.2] THE KEY-TRANSITION MATRIX IS BUILT FROM KRUMHANSL'S KEY-PROFILE CORRELATIONS.**
*"Intuitively it is most likely that the music will stay in the same key, and if it does change key it
is most likely to move to one that is closely related and contains many of the same chords. The initial
key transition matrix was created using the key profile correlations in Table 2 in the Appendix, which
give numerical values to our intuitions. The values were circularly shifted to give the transition
probabilities for keys other than C major and C minor … The values were all made positive by adding 1,
then they were normalised to sum to 1 for each key. This gave the final 24 × 24 transition matrix."*
The Appendix's Table 2 reproduces Krumhansl's correlations (attributed to [1], p. 38); read from it, the
C-major row's highest off-diagonal values are **A minor 0.651**, then **F major 0.591 and G major
0.591**, then E minor 0.536; the C-minor row's highest are **E♭ major 0.651**, then A♭ major 0.536, then C
major 0.511, then F minor and G minor at 0.339 each. **So in the initial matrix
the most probable tonality change from a major key is to its relative minor, ahead of its dominant and
subdominant; and from a minor key to its relative major.** *(The Table 2 values are Krumhansl's,
printed at second hand in this paper; see finding (4).)*

**★ [FACT, p. 3, §2.1.3 and §2.1.3 cont.] THE EMISSION MATRIX IS BUILT FROM KRUMHANSL'S CHORD-TRANSITION
RATINGS AND SINGLE-CHORD RATINGS, and its premise is measured against the test data.** *"We are assuming
that there is a strong correlation between the key implied by a chord transition, and the likelihood of
that transition occurring in that key. This assumption is supported by Krumhansl [1] p. 195, and by
finding the correlation between the chord transition ratings and the corresponding number of transitions
present in our test data. Correlations of 0.39 for major keys and 0.22 for minor keys were found, both
highly significant given the respective 40 and 154 degrees of freedom."* Worked example: *"the chord
transition B major to E major strongly implies the key of E major, since it forms a perfect cadence …
Neither chord is contained in B♭ major, so the probability of state B♭ major emitting B-E will be very
low."* Construction details: Table 3's ratings cover only the diatonic chords of major keys; *"For minor
keys the ratings for major keys corresponding to the same scale degrees were used"*; the stay-on-the-
same-chord value is taken from Table 4's single-chord ratings *"and artificially boosted because
repeated chords on either a frame-by-frame or beat-by-beat level are very likely. The approximate optimal
increase was experimentally found to be 2"* (example: A minor in C major, 3.62 + 2 = 5.62); transitions
involving one or more non-diatonic chords are *"set uniformly low, to 1"*; the matrix is normalised per
key and has dimensions **(48 + 1)² × 24 = 2401 × 24**.

### Training and decoding (p. 3, §2.2–2.3)

**★ [FACT, p. 3, §2.2] TRAINING IS PER SONG, UNSUPERVISED (EM), AND THE EMISSIONS ARE DELIBERATELY
NOT TRAINED — because training them destroys what the hidden states mean.** *"The expectation
maximisation (E-M) algorithm … was used to learn the HMM parameters for each individual song. If the
observation probabilities, which model the relationship of each chord transition to each key, were
subject to training, we could no longer be certain that the hidden states represent keys. To verify
this, experiments were conducted with various combinations of HMM parameters trained."* The training
data is the song's own chord-transition sequence, each transition given an index 1 to 2401, circularly
shifted per key (except *no chord* transitions, which *"have the same function in every key"*).

**[FACT, p. 3, §2.3] Decoding:** Viterbi for the most likely key sequence, and *"standard HMM decoding"*
(the posterior state probabilities) *"giving the likelihood of being in any key at each time frame."*

### The segmentation examples (p. 4, §3, Figures 2 and 3) — no ground truth

**[FACT, p. 4, §3] No key-change ground truth exists for the corpus, so segmentation is illustrated,
not measured.** *"Ground truth for the key changes in the Beatles' songs is not available to our
knowledge, but the figures show that the algorithm is capable of extracting meaningful structure."*
Examples: in *I'll Cry Instead* the two bridge passages in D major at 42–52 s and 72–82 s are separated
(Figure 2); in *I'm Happy Just to Dance With You* the choruses (C♯ minor) and verses (E major) are
extracted (Figure 3).

**★ [FACT, p. 4, §3] THE AUTHORS' OWN STATEMENT OF THE METHOD'S WEAKNESS.** On a modified final chorus
that produces a short E-major section at about 103–105 s: *"This demonstrates one of the weaknesses of
our approach, that although the chords were most closely related to E major, the key of E major was not
firmly established. It is expected that this type of error would occur less frequently if the chords'
position relative to the musical phrases were taken into account."* And, in the Discussion (p. 5, §5),
of two errors: *"These two cases would benefit from longer temporal dependencies in the model, based on
phrase lengths, since it is usually the chord or cadence at the end of a phrase that defines the key."*

**[FACT, p. 4, §3]** The posterior plot shows a repeated pattern of about 16 s in the first E-major
section of *I'm Happy Just to Dance With You* that the hard classification cannot show — offered as
structure-extraction potential, further research.

### The evaluation, as stated (p. 4–5, §4–§5)

**[FACT, p. 4, §4] Protocol.** Overall key of a song = the key whose per-frame likelihood, summed across
the whole song, is largest. Ground truth: a *"subjectively-assessed"* musicological analysis of the
Beatles' songs (Pollack, [15]); *"the ground truth often mentioned more than one key, in which case the
first was taken to be the most important"*; modal songs: *"Lydian and Mixolydian modes were treated as
major, and Dorian and Aeolian as minor."* Corpus: the 110 songs of the first 8 Beatles albums.

**★ [FACT, p. 5, Table 1] Percentage of songs correctly classified, with varying training — reproduced.**

| Prior trained | Transition trained | Emission trained | Percent correct |
|---|---|---|---|
| yes | yes | yes | 27 |
| yes | yes | no | **91** |
| yes | no | yes | 18 |
| yes | no | no | 87 |
| no | yes | yes | 28 |
| no | yes | no | **91** |
| no | no | yes | 18 |
| no | no | no | 87 |
| Expected value for random choice of key | | | 4 |

**[FACT, p. 5, §5] The authors' reading of the table.** *"fixing the emission probabilities gives the
most accurate representation of the song, since allowing adjustment alters the meaning of the hidden
states. Training the prior state probabilities had little effect … The suitability of the
perception-based initialisation was confirmed by the case with no training, where 87% of songs were
correctly classified. Training the transition probabilities for each song gave the optimum result of
91%."*

**[FACT, p. 5, §5 and Figure 4] The ten errors, all explained by the authors.** Three modal songs (two
Mixolydian mistaken for the major key on their fourth degree, one with Dorian inflexions mistaken for the
major key on its seventh degree) — *"comparable to errors between relative major and minor keys"*; one
A-major song mistaken for its dominant E major (chords B, E, A, D imply both keys); one A-major song
mistaken for its subdominant (a blues flattened seventh); *"The remaining five incorrect key estimates
are for songs where more than one key is mentioned in the ground truth for the home key, and it is one
of these alternative keys that has been selected by the algorithm."* Figure 4 is the confusion matrix
for the prior-and-transition-trained case, incorrect estimates only.

**[FACT, p. 5, §6] Named future work:** audio-to-chord front end (*"The 91% accuracy reported here will
almost certainly not hold when working with audio"*); *"A more detailed exploration of segmentation
possibilities is also planned."*

## Measured results, as the paper states them

Table 1 above: the corpus (110 Beatles songs, first 8 albums, hand-annotated chord symbols, Pollack's
key analysis as ground truth), the metric (overall song key correct, first-named key, modes folded to
major/minor), the values as printed. The correlations 0.39 (major) and 0.22 (minor) between Krumhansl's
transition ratings and the corpus's transition counts. **No measurement of key-change placement exists
in the paper** — the segmentation is illustrated on two songs without ground truth.

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A complete, correct, time-aligned chord-symbol transcription
(here hand annotations); a triad vocabulary (extensions dropped, non-triadic chords mapped to the
nearest of four triad templates); a fixed 100 ms sampling grid over the transcription. It reads no
notes, no spelling, no bass (inversions collapsed), no metre, no phrase structure — the last being
the omission its own authors name as the cause of its errors.

**What it HANDS downstream.** Per 100 ms frame, one key (major or minor, 24 values) as the Viterbi
path, AND the full posterior over all 24 keys per frame; per song, one overall key by summing the
posteriors. No chord decision (chords are input), no degree, no confidence beyond the posterior itself.

**Its own STATED SCOPE and limits.**
- **Domain:** popular music (the Beatles); the vocabulary is *"the Western music repertoire for which
  this analysis is intended"*, triads only.
- **Vocabulary:** 24 major/minor keys; modal songs folded into major or minor at evaluation.
- **Granularity:** a key change may occur at any 100 ms frame — not tied to a chord boundary, a beat, a
  phrase or a cadence.
- **Coupling:** none in the model's decision — the chords are given; the key is decided AFTER and FROM
  them, and cannot revise them.
- **Fitting:** the emission and prior tables are from perceptual data, frozen; the transition matrix is
  initialised from theory and then re-fitted PER SONG by unsupervised EM on the song being decoded. No
  held-out split exists and none is needed for labels (no labels are used in training), but the
  transition table used to decode a song is fitted on that song.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adapt (a precedent for the tonality-change cost):** a key-transition table initialised from a
  published key-distance measure — here Krumhansl's key-profile correlations, offset and normalised —
  so that staying is most probable, and a change is graded by relatedness. The L2 charter leaves the
  score's terms and tables to the detail specification; this paper is a published instance of one term
  of that kind, on a rival architecture. **Note what the table says about direction:** in its initial
  matrix the nearest change from a major key is to its RELATIVE MINOR, ahead of the dominant and
  subdominant (see finding (2)).
- **Adapt (a staged-fit precedent, with a measured reason):** emission tables from a fixed external
  source and NOT trained, transitions trained — with Table 1 measuring that training the emissions
  collapses accuracy from 91% to 27–28% because the hidden states stop meaning keys. The record's D-525
  (factor tables counted and frozen, only combination weights fitted) is a neighbour of this design;
  this is a published, measured instance of why one part of a generative model is frozen while another
  is fitted.
- **Adapt (for DP-E, as the authors' own evidence):** the two error classes the authors attribute to
  the absence of phrase position and cadence — *"it is usually the chord or cadence at the end of a
  phrase that defines the key"* — are a rival system's own report that a tonality decided frame by frame
  from chords, with no phrase or cadence context, mislocates short key sections.
- **Must argue against:** the tonality decided AFTER and FROM a completed chord transcription (the
  decomposition `FRAMEWORK.md` §S4(b) EXCLUDES, with this paper as its provenance — confirmed at the
  object, see finding (1)); a key change admissible at any fixed 100 ms frame rather than at a harmonic
  boundary (DP-E's rival, *"an independent tonality track changing anywhere"*); inversions and bass
  discarded by construction; the triad-only chord vocabulary; per-song unsupervised re-fitting of the
  transition table on the material being decoded; and the single-path key output as the headline
  (though the posterior is also published, which the record's rivals-with-mass form can express).

## ★ Findings, routed and not applied

**(1) The record's one characterisation of this paper is CONFIRMED at the object.** `FRAMEWORK.md`
§S4(b) names Noland and Sandler as *"who estimate tonality downstream of a completed chord
transcription."* Read at pp. 1, 3 and 5: chord symbols are the input (hand annotations), the key is
decoded from chord transitions, and audio-to-chord is future work. No correction owed. **No falsifier.**

**(2) A SECOND published-theory position that the relative major/minor is the NEAREST tonality change,
this time carried into a working model's transition matrix.** Row 28's extract routed one such position
(distance one for the relative major/minor). Here the initial key-transition matrix is built from
Krumhansl's key-profile correlations, in which C major's nearest key is A minor (0.651) ahead of G and F
major (0.591 each), and C minor's nearest is E♭ major (0.651). The direction is again OPPOSITE to the
legacy D-347 cost (a large extra penalty on the relative major/minor switch) and does not match the
legacy D-348 measure (circle-of-fifths distance, under which the dominant and subdominant would be
nearest). Both legacy entries are ⚠LEGACY; the live L2 tonality-change cost is not yet derived. Routed
to L2's detail specification beside row 28's finding, with no verdict.

**(3) A measured instance of a fixed-emission, fitted-transition staged fit — 91% against 27–28% when
the emissions are also trained (Table 1).** The authors' stated mechanism is that training the
emissions alters what the hidden states mean. Routed to L2's detail specification beside D-525 as a
published precedent for freezing the tables that carry meaning and fitting only the rest; and to
measurement design as an instance of a fit whose transition table is re-fitted per song on the song
being decoded (unsupervised, no label leakage, but the fit/evaluation separation of #20 is not
established at the object for the transition table).

**(4) The R-8 gap is TOUCHED AT SECOND HAND, and nothing is carried out of it.** This paper's Appendix
reprints three of Krumhansl's tables — the key-profile correlations (attributed to [1] p. 38), the chord
transition ratings ([1] p. 193) and the harmonic hierarchy ratings ([1] p. 171). `FRAMEWORK.md` R-8
records the tonality-profiles primary as not on disk, and row 9 of the candidacy derivation carries it
as unreadable from here. **The values printed here are a secondary reproduction and are not the
primary; under the theory-grounding corollary nothing is carried out of them as an established fact of
Krumhansl 1990.** What IS established at this object is what Noland and Sandler DID with those values
(finding (2) and the emission construction), which is this paper's own method. Routed to the R-8 row as
a datum — a held secondary source prints the tables — with no change to R-8's status.

**(5) The authors' own attribution of their errors to the absence of phrase position and cadence
context.** Two statements (p. 4 §3, p. 5 §5) that a key decided frame by frame from chords mislocates
short key sections because *"it is usually the chord or cadence at the end of a phrase that defines the
key."* ENRICHES-shaped for DP-E's chosen point (a tonality change located at a harmonic boundary,
decided with the chords) and for the L1/L3 cadence split, as a rival's self-report. Routed to the
findings surface's DP-E block. No verdict moved; DP-E does not rest on this paper.

**(6) The candidacy row's reason is CONFIRMED and one precision is added.** The row admits the paper
for *"an explicit transition structure"*; at the object the structure is fully connected with a change
admissible at every 100 ms frame, so what the structure decides about *where* is "anywhere on a fixed
grid, weighted by relatedness" — the rival's answer to DP-E's question, not the chosen one. This
sharpens the row's reason without changing its ADMITTED verdict or the paper's group placement (group
1's question is the joint tonality-and-chord decision; this paper decides tonality alone, downstream of
chords, which is the group's rival shape, and a rival is admitted under the derivation's own
consequence (i)).

**(7) No falsifier.** Nothing read contradicts any CHOSEN design point; the paper is the excluded
decomposition's own provenance and reads exactly as the record characterises it. **No STOP fires** under
the remedial commission's §5.

## Centrality

**CENTRAL, on a narrow ground, challengeable at the progress record.** No ratified text rests a [FACT]
figure on this paper, and its one citation is confirmed. What makes it central is finding (2) with
finding (4): the design of a tonality-change cost from a published key-distance measure is a term an L2
detail specification must specify, the primary for that measure (Krumhansl 1990) is unreadable from here
(R-8), and this paper is the held object at which a working instance of that term — with its direction
(relative major/minor nearest) and its measured outcome (Table 1) — can be cited. A claim of that kind
would carry load in a detail specification, which is the original commission's §4 test. A second
independent extraction is therefore **OWED**. The narrowness: everything else the paper exhibits (a
downstream tonality decision, a fixed-grid change, a triad vocabulary) is the rival the record already
excludes on other primaries.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (6) are routed and written
nowhere else. It does not fetch Krumhansl 1990 and carries no value out of the Appendix as an
established fact of that book. It opens no code, touches no measurement tool, no corpus, no golden and
nothing under `tools/`. It writes no open-items row and allocates no decisions-register identity. It
reads no other paper and takes no decision about the order of the remaining slice.

---

*Provenance: written 2026-09-05 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_seventeen.md`, after the ordinary session-start read (`CLAUDE.md`
whole, `DECISIONS.md` whole, `STATUS.md`, the derived gating answer — 244 open, 219 gating, 25
non-gating, unchanged). Read for this extract, at the files: `reading_pass/candidacy_upgrades.md` whole
(row 26 at its line 88), `cowork_l2_task_b_slice_derivation_2026_09_05.md` at its row 26 (line 71),
`docs/research_papers/BIBLIOGRAPHY.md` at line 40, `FRAMEWORK.md` at the L2 charter (§5), the design
points DP-A to DP-K (§9) and §S4(b) (line 1573), the remedial commission whole, the original commission
whole, the row 3 extract whole for the form, and a `Grep` of the staged tree for "Noland" and "Sandler".
The paper itself was read at the object as page images, all six pages. No shell command was run on the
repository or on any staged copy of it for content or for listings. No figure of this project's own
measurement is restated (#17f, D-431); every value above is the paper's own.*

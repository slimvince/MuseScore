# EXTRACT — Catteau, Martens & Leman, "A Model based approach to scale and chord estimation" (the held object for the bibliography's "A Probabilistic Framework for Audio-Based Tonal Key and Chord Recognition", GfKl 2006) — Task B candidacy row 28, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-05).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All 24 printed pages of the held document (pp. 1–24) were read AT THE OBJECT: the held
> PDF staged through the bridge and read with the file tools as page images. **No relay, no web-fetch
> read, no prompted extraction.** Every quotation below was read from the page and carries the printed
> page number of the held document.
>
> **★ READ THIS FIRST — THE HELD OBJECT IS NOT THE DOCUMENT THE BIBLIOGRAPHY NAMES.** The bibliography
> row (`docs/research_papers/BIBLIOGRAPHY.md`, "Core joint-model / factor-form sources") names *"A
> Probabilistic Framework for Audio-Based Tonal Key and Chord Recognition," GfKl 2006*, a Springer
> chapter (`10.1007/978-3-540-70981-7_73`), marked held (✓) and PAYWALL. **The held file
> `docs/research_papers/catteau_martens_leman_2006_gfkl_key_chord_recognition.pdf` carries a different
> title — "A Model based approach to scale and chord estimation" — and is a 24-page document with no
> proceedings header, no volume, no year and no page range beyond its own 1–24, which calls itself a
> "report" (p. 7: *"that is beyond the scope of this report"*).** The three authors and the two
> affiliations match the citation. **Whether the held document is a version of the cited chapter, or a
> different document by the same authors, is NOT establishable from what is held**; the cited chapter
> was not fetched and is not read here. Everything below is about the held object, and no claim is
> carried out of it as a claim about the GfKl chapter. This is a citation finding of the class the
> original commission's R-9 names (a named file containing a different document) and is ROUTED to the
> bibliography reconciliation (finding (1) below).
>
> **Why this paper and why second in L2's slice.** It is row 28 of `reading_pass/candidacy_upgrades.md`,
> ADMITTED there as *"A joint key-and-chord probabilistic framework — the same decision L2 owns, done
> another way."* `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 places it in L2's slice with the
> same reason. It is second in group 1 of the proposed reading order ("the joint tonality-and-chord
> decision"), and `reading_pass/l2_slice_reading_progress.md` names it as next, carrying one question
> from row 27's finding (2): whether this paper reports anything of the sign the sealed first-stage
> draft attributes to it. Ruling 1 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the
> gate: no derivation before L2's slice of Task B is read. This is the second member of that slice read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Benoit Catteau and Jean-Pierre Martens (ELIS — Digital Speech and Signal Processing Group, Universiteit
Gent) and Marc Leman (IPEM — Institute for Psychoacoustics and Electronic Music, Universiteit Gent),
"A Model based approach to scale and chord estimation", 24 pages, six sections (Introduction;
Algorithmic approach; Segmentation; Test results; Discussion; Conclusion) and eight references. No date
is printed on the document; the latest reference is 2005 (p. 24). The document uses the word **scale**
throughout for what this project calls the **tonality** (tonic and mode); this extract keeps the paper's
word inside quotations and uses the project's word outside them.

**File:** `docs/research_papers/catteau_martens_leman_2006_gfkl_key_chord_recognition.pdf` (944,281
bytes at the listing).

## Claims, labeled

### What the method decides, and how it decides it jointly

**★ [FACT, p. 1, §1] The stated contribution, in the authors' words:** *"In this paper, we propose an
algorithm for analysing Western tonal music. Our point of departure is the theory of Lerdahl. We use a
chroma vector representation to link the theory with the acoustic observations. The chroma vectors are
used to segment the audio and to estimate the chord and scale of those segments simultaneously by means
of a one-stage Viterbi search, followed by a backtracking step to retrieve the scale and chord sequence."*

**[FACT, p. 1, §1] The sequential design is named as prior work, not adopted:** *"Recently, [2]
described an algorithm with chord detection first, scale detection then and chord enhancement as a
final step."* — the paper's [2] is Shenoy & Wang 2005 (p. 24). The paper measures nothing against it.

**★ [FACT, pp. 1–2, §2] The unit of decision is a PAIR, and the objective is the joint posterior.**
*"we are interested in maximizing P(S, C | O), where O is the vector of observations, S the vector of
associated scales and C the vector of associated chords."* Bayes' rule and the omission of P(O) give
P(S, C | O) ∼ P(S, C) · P(O | S, C) (eq. 2); with the likelihood factored per event and *"The assumption
that a chord/scale couple only depends on the previous chord/scale couple"*, the model is
P(S, C | O) ∼ ∏ₙ P(Sₙ, Cₙ | Sₙ₋₁, Cₙ₋₁) · P(Oₙ | Sₙ, Cₙ) (eq. 4, p. 2). The hidden state is the
(scale, chord) couple; the search is a single Viterbi pass over that joint state.

**★ [FACT, pp. 8, 12–14, §2.1 and §2.4] The coupling between tonality and chord is a SOFT factor
inside the path probability — a probability P(C | S), never a constraint.** The transition factor is
split two ways (eqs. 5–8, p. 8): when the tonality is unchanged, P(Sₙ, Cₙ | Sₙ₋₁, Cₙ₋₁) =
P(Sₙ | Cₙ) · P(Cₙ | Cₙ₋₁) (eq. 34, p. 14); otherwise P(Cₙ | Sₙ) · P(Sₙ | Sₙ₋₁) (eq. 35). *"we consider
P(Cₙ | Sₙ) and P(Sₙ | Cₙ) as equal (and not depending on the event, n)"* (p. 8). That factor —
*"denoting how good a chord fits within a scale"* — is the normalised inner product of the chord
profile and the Temperley scale profile, P(C | S) = Σ CPᵢ·TPᵢ / √(Σ CPⱼ² · Σ TPₖ²) (eq. 16, p. 12).
**No chord is excluded from any tonality; a non-diatonic chord is merely less probable.** *(The paper
also writes P(Cₙ | Sₙ) as a product over the chord's three pitch classes, eq. 28, p. 13; which form
produced the reported results is not stated.)*

**[FACT, pp. 3–8, §2.1] The transition distances are Lerdahl's, taken from published theory and not
fitted.** The paper walks through Lerdahl's *Tonal Pitch Space* (2001; the paper's [8]) from
Krumhansl's multidimensional scaling: the five-level cone (root, fifths, triadic, diatonic, chromatic
levels; Figs. 3–4), the diatonic circle of fifths (Fig. 6) and the chromatic circle of fifths (Fig. 8).
A chord change within one tonality costs the number of changed pitch classes plus the moves on the
diatonic circle — C to F in C major *"is bridging a distance equal to 5 (= 4 pitch classes + 1
translation)"* (p. 5); a tonality change adds the moves on the chromatic circle of fifths, and *"when
the music modulates from Major to minor or vice versa, one only has to measure the number of
translations needed to move to the relative Major scale. Thus, the distance on the chromatic scale from
C Major to D minor is the same as from C Major to F Major and equals one"* (p. 6; footnote 6 defends
this because the relative major uses all the harmonic-minor pitch classes but one). **Table 1 (p. 7)**
is the 12×12 chord-root distance matrix within a major scale, rows and columns in fifths order (the
diatonic-to-diatonic entries take values among 0, 5, 7 and 8; two symbols γ and δ stand for transitions
involving the five non-diatonic roots); **Table 2 (p. 8)** is the distance between tonalities, four rows
(from major or minor, to major or minor) over the same fifths ordering. *(The individual cells of the two
tables are not transcribed here; the page images are the record.)* The authors state the simplification openly: *"the recipe
to create those distances is so complex that we considered to simplify the model"* (p. 23), and *"To
change from one scale to another, there is more theory, but that is beyond the scope of this report"*
(p. 7).

**[FACT, pp. 13–14, §2.4] Distances become probabilities by an exponential, and every constant is
hand-set or derived from a stated presumption — nothing is fitted to data.** P(Cₙ | Cₙ₋₁) =
exp(−d(Cₙ, Cₙ₋₁)/d_norm,C), P(Sₙ | Sₙ₋₁) = exp(−d(Sₙ, Sₙ₋₁)/d_norm,S) (eqs. 36–37, p. 14). The
non-diatonic symbols: *"δ = 2·γ. And γ has to be larger than any transition to a diatonic chord, so it's
chosen to be 9"* (p. 14). The two normalisers rest on a presumption stated in words: *"we have presumed
that a modulation is as hard as moving three times from one chord to another"* (eq. 38, p. 14); with the
mean distances over the two matrices — printed as *"d_norm,C = 8.93 and d_μ,S = 15.17"* (p. 14; the
first subscript as printed) — this gives d_norm,S / d_norm,C ≈ 0.55 (eq. 40), and
*"We have chosen d_norm,S to be 11 and d_norm,C 20 so that the exponential function can discriminate
well between far and near scales or chords."* (An earlier passage, p. 13, gives a different
parametrisation of the same factors — a stay probability 1−α with α = 0.3 giving γ = 0.3, and α = 0.5
giving λ = 0.43 for the chord factor, eqs. 19–31; the paper does not say which parametrisation
produced the results.)

**[FACT, pp. 11–13, §2.3–§2.4] The observation model.** Temperley's key profiles (Table 3, p. 11:
major 5.0 2.0 3.5 2.0 4.5 4.0 2.0 4.5 2.0 3.5 1.5 4.0; minor 5.0 2.0 3.5 4.5 2.0 4.0 2.0 4.5 3.5 2.0
1.5 4.0) and four binary chord profiles — major, minor, diminished, augmented — on pitch class 0 as
root (Table 4). *"Those profiles (CP) have to be seen as masks: they will generate scale dependent
chord profiles (V) out of Temperley's profiles (TP)"*: Vᵢ = TPᵢ · CPᵢ (eq. 15, p. 12), and the
observation probability is the normalised inner product of the chroma vector with V (eq. 17). A second
observation model is stated beside it (p. 13): a normal distribution μ = 0, σ = 0.13 for pitch classes
that should be absent, and for the chord's three pitch classes a Gaussian μ = 0.33, σ = 0.13 below
0.33 with a uniform above, giving P(O | S, C) ≈ P(O | C) = ∏ P(Oₗ | C) (eqs. 32–33). **Which of the two
produced the reported results is not stated.**

**★ [FACT, p. 15, §3] Segmentation is decided BEFORE the joint decision, by a threshold, and the
decision is then taken per segment.** *"this algorithm is not frame based. If we would analyse every
frame, a second step would be required to merge all the similar frames into one event. Here, we segment
the music on the basis of the chroma vectors. A decision will be taken only after a segment has been
recognised. All the frames belonging to it, are accumulated and based on this result, a more confident
decision about the observed scale/chord is expected."* The boundary test is the change of the first
moment of the accumulated chroma vector, μ₁ = (1/M) Σ accᵢ·i (eq. 41); *"the difference should be
greater than 0.5. A value of 0.6 for the threshold, seems sufficient."*

**[FACT, pp. 8–10, §2.2] The chroma front end (audio-specific).** Frames of 150 ms with 130 ms overlap
(*"We prefer this rather long frame to obtain a reliable frequency analysis and to prevent short events,
such as a drum kicks from having a major effect"*), Hamming window, STFT, mapping to a log-frequency
scale C1–C8 (85 semitone bins), background removal by a moving Hamming window keeping only spectral
peaks (eq. 11), A-curve weighting (eq. 12), a harmonic sum over I = 5 partials with γ = 0.8 and
h = {12, 19, 24, 28, 31} (eq. 13), and folding into one octave (eq. 14). A diapason of 440 Hz is assumed
(p. 23).

### The unit of the reported figures

**[FACT, p. 16, §4.1]** Output is *"a list of events"* — end time in seconds, chord, tonality. Scoring
is by a comparison tool reporting *"Total cost"*, insertions, deletions, *"% of correct chords"* and
*"% of correct scale"*; how the percentage is computed over events of unequal length is not stated. A
silence produced a spurious first event, and *"we added a second step, to evaluate if the energy was
high enough, in order to be a real segment"* and to bundle consecutive identical events (pp. 16–17).

## Measured results, as the paper states them

**Corpus 1 — synthesised cadences (p. 15, §4.1):** IV→V→I, VI→V→I and II→V→I *"in all of the 24
scales, yielding 72 files"*, first in Shepard tones (*"the emphasis is put on the transitions (Lerdahl's
theory) rather than on the template matching"*, p. 15). Result (p. 16): total cost 7.07889, 1 insertion,
0 deletions, **80 % correct chords, 100 % correct scale**. The same sequences rendered MIDI-to-WAV,
arpeggiated, and as seventh chords (pp. 17–18) are shown as event lists only, with no aggregate figure.

**Corpus 2 — synthesised modulations (pp. 18–19, Tables 5–6):** ten chord sequences from C major or
C minor, eight modulating (to G major, A♭ major, A minor, D minor, F minor, C♯ minor, C major, G♯ major),
two not, in Shepard tones and MIDI-to-WAV. **Shepard: 90.1515 % correct chords, 85.1515 % correct
scale** (cost 18.637, 0.7 insertions, 0 deletions). **MIDI-to-WAV: 75.134 % chords, 86.655 % scale**
(cost 37.9343, 0.9 insertions, 0.2 deletions) — *"the number of correct chords is not that elevated
any more, because a new difficulty has been introduced: the building tones have now certain
harmonics"* (p. 20). Sequence 5's worked example (p. 20): the algorithm *"decides to make a modulation
along F Major"* and reads D diminished for B diminished.

**Monophonic input (p. 21):** a rendered C major scale up and down is read as chords of C major (C, F,
G) and, from A upward, as A minor with non-diatonic F diminished and F minor — *"the output is not very
good. Although we cannot be unhappy with the result … the played note is always present in the chord."*

**Corpus 3 — real audio (p. 22, §4.2, Table 7):** ten 60-second fragments of popular recordings,
annotated by the authors with chord and tonality (one, Live's "I Alone", modulating G♭ major → E♭
major). **No figure is reported:** *"the program detects a lot more events than there really are. This
means that a strict comparison of the processed output to the reference is not relevant here"*;
graphically, *"the algorithm is capable of detecting most of the chords, but that the scale changes too
often"* (pp. 22–23).

**MIREX 2005 training data (p. 23, §4.3):** a routine determining the mean tonality of each of 96
fragments; **82 % with a crisp count and 90 % with the MIREX cost measure.**

**Discussion figures (p. 23):** the counts of pitch-class appearances in Lerdahl's schematic major
scale (5 1 2 1 3 2 1 4 1 2 1 2) correlate 96.2 % with Temperley's profile and 97.2 % with Krumhansl's.

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** An audio signal reduced to chroma vectors per 150 ms frame —
no notes, no onsets, no spelling, no voices, no metre, no key signature, and a fixed 440 Hz tuning
(p. 23). The segmentation is derived from the chroma stream by a threshold before any harmonic decision
(§3); the harmonic decision consumes accumulated chroma per segment. It assumes the music is at every
moment in one of 24 tonalities (12 major, 12 harmonic minor — *"the classic choice"*, p. 2) and on one
of 48 triads (12 roots × major, minor, diminished, augmented; Table 4); nothing outside that vocabulary
is representable.

**What it HANDS downstream.** A list of events, each with an end time, a chord (root and one of four
triad types) and a tonality (tonic and major/minor), as the joint state on the single most probable
path after backtracking. The degree of the chord within the tonality is derived for display (Figs. 13,
16) and is not an output of the decision. It hands on **no** inversion or bass (*"this representation
cannot handle chord inversions"*, p. 23), no seventh or extension (a seventh is reduced to a triad,
p. 18), no chord-tone assignment, no cadence, no figured bass, and **no alternatives or confidences** —
one path only.

**Its own STATED SCOPE and limits.**
- **Vocabulary:** 48 triads, 24 tonalities; *"Our model only includes top down knowledge about triads,
  no other chords are considered"* (p. 23).
- **No training:** *"This algorithm is model based and conceived in such a way that there is no
  training needed. There are however some parameters that have to be tuned"* (p. 15). Every constant
  is hand-set (the threshold 0.6; γ = 9, δ = 18; d_norm,S = 11, d_norm,C = 20; the Gaussian σ = 0.13) or
  derived from a stated presumption (modulation = three chord moves).
- **Corpora:** synthetic cadences and modulations, ten popular-music fragments without a reported
  figure, and the MIREX 2005 tonality set; **no classical notated repertoire and no annotated corpus of
  frequent modulation**.
- **Weaknesses the authors state (§5, pp. 23–24):** chroma cannot see inversions; only triads;
  fixed diapason; the model "should not be that difficult to make … even more stable in the detection
  of the scale: modulating from one scale to another should be harder than changing the chord"; the
  cosine distance-to-probability step *"is not the desired one to express stability"* and should move
  to an exponential; and *"The segmentation works quite well with the synthetic examples, but is far too
  active in real world examples. There are two approaches possible. Or there should be another decision
  rule, or a second pass can be adopted to collect the similar events into one bag."*
- **Conclusion (p. 24):** *"We have shown that departing from a model, we are able to detect chords and
  scales in a confident and straightforward way."* — a qualitative claim; the paper reports no
  comparison against any other system and no joint-versus-separate ablation.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adopt (as a shape, a second published instance):** the joint (tonality, chord) hidden state decoded
  in one Viterbi pass — the same shape as row 27's system, the framework's one entangled decision and
  D-001. Unlike row 27, it is written as a probability model (eq. 4), so its factors are probabilities
  rather than an additive integer cost.
- **Adopt (as the charter's boundary condition, exhibited):** the tonality–chord coupling as a
  probability factor P(C | S) inside the path — a **cost, never a veto**: no chord is unreachable in any
  tonality. This is the charter's position exhibited by a second system, without the charter's
  quotation, which is not in this document (finding (2)).
- **Adapt:** the factoring of the joint transition into a stay-or-change-tonality branch (eqs. 34–35),
  which gives one probability for a chord move inside a tonality and a separate one for a modulation;
  and the un-fitted, theory-derived distance tables with a **stated presumption converting one scale to
  the other** ("a modulation is as hard as three chord moves"). For DP-P (how L2's score terms are
  combined and fitted) this is a second un-fitted joint decode that reports working figures on
  synthetic data only.
- **Adapt (a fact to weigh in the tonality-distance table):** Lerdahl's chromatic circle as this paper
  applies it puts the **relative major/minor at distance one — the nearest possible tonality change**
  (p. 6 and footnote 6). The record's legacy tonality-change cost puts *"a large extra penalty on the
  relative major/minor switch"* (D-347, LEGACY). The two are opposite in direction; neither is measured
  on our repertoire, and nothing is concluded here — it is recorded so the detail specification meets
  both.
- **Must argue against:** segmentation decided **before** the harmonic decision by a chroma-moment
  threshold, with no note-derived boundaries (L1's change points are absent by construction — the paper
  is audio), which the authors themselves report over-segments real music (p. 24); the single-path
  output with no rivals and no confidence (the L2 charter publishes rivals with their mass, including
  boundary rivals); the 48-triad vocabulary with no degree, inversion, seventh or chord-tone assignment;
  and the harmonic-minor-only minor mode, which cannot represent the natural or melodic minor
  collections.

## ★ Findings, routed and not applied

**(1) IDENTITY — the held file is not the document the bibliography names.** Stated in full in the
banner. The bibliography row names the GfKl 2006 Springer chapter *"A Probabilistic Framework for
Audio-Based Tonal Key and Chord Recognition"*; the held file is titled *"A Model based approach to
scale and chord estimation"*, is 24 pages, undated, and calls itself a report. Same authors, same
affiliations, same subject; **whether it is a version of the chapter is not establishable from what is
held.** Every use of this row in the record — `candidacy_upgrades.md` row 28, the L2 slice derivation
row 28, and the sealed first-stage draft's by-name attribution — cites the chapter's title. **ROUTED to
the bibliography reconciliation** (the remedial commission §4 names it as its own act; this extract
performs none of it). The candidacy verdict (ADMITTED, "the same decision L2 owns, done another way")
is TRUE of the held object as read.

**(2) THE QUESTION ROW 27 LEFT — ANSWERED AT THE OBJECT: the held document reports NOTHING of the
sign the sealed first-stage draft attributes to Catteau and colleagues.** `FRAMEWORK.md` Appendix B,
§S5 "The derived decomposition", subsection "The layers", the L2 block, reads *"Rocher and colleagues
measured joint estimation beating separate estimation, and Catteau and colleagues report the opposite
for their own system — 'an incorrect chord selected may discard the correct key (and vice versa) …
adding a compatibility between chords and keys has led to a decrease of accuracy'"* (lines 1721–1724 at
this reading, located at the heading list). **Read whole, the held document contains no
joint-versus-separate comparison, no compatibility constraint tried or declined, no statement that
coupling the two axes decreased accuracy, and none of the quoted words.** Its coupling is soft by
construction (eq. 16) and its only statements about the interaction of the two axes are that
non-diatonic chords are less probable under a tonality and that the tonality *"changes too often"* on
real audio (p. 22). The quoted words were established at row 27 as Rocher et al. 2010 §2.2.3, p. 143.
**So the pass's V7 correction — both halves of the charter's "two studies" are ONE paper — stands and
is now established from both ends:** the words are in Rocher, and they are not in the held Catteau
document. **Bound:** the GfKl chapter itself is not held or read (finding (1)); whether IT contains a
statement of that sign is not established. Appendix B is the preserved first-stage draft, *"whole and
unedited"*, and is not a statement to be corrected; the live §5 charter's "another" is what the pass's
correction already addresses, and this finding adds to it that the named second study, as held,
contains nothing of the kind. **ROUTED, NOT APPLIED** — `FRAMEWORK.md` and the findings surface are
untouched.

**(3) DP-B — a second joint system, SUPPORTS-shaped in structure, adding NO measured figure.** The
held document is a second published (tonality, chord) joint decode, and it names the sequential design
(chord first, then tonality, then chord enhancement — Shenoy & Wang 2005) as the prior work it departs
from (p. 1). But it measures nothing against that design and runs no ablation, so **DP-B's measured
ground (the 1.8- and 4.6-point costs) remains Rocher's alone**; nothing here strengthens or weakens
the value. Routed to the findings surface's DP-B block as a structural instance without a figure.

**(4) DP-C — a second author's report that a boundary-first design OVER-SEGMENTS real music.** The
findings surface's DP-C block records row 1's *"the CTM was over-segmenting the input"* as *"direct
primary evidence about boundary-first designs"*. The held document is a second, independent instance
of the same shape: segmentation decided before the harmonic decision by a threshold (§3), *"far too
active in real world examples"* by the authors' own statement (p. 24), and the remedies they name are
exactly a second pass or another rule bolted after it. It carries **no value** (the real-audio corpus
has no reported figure). **ENRICHES-shaped evidence for the chosen "with"; not a falsifier of
anything.** Routed to the findings surface's DP-C block and to L2's detail specification.

**(5) A fact for the tonality-distance term of L2's score: relative major/minor at distance ONE.**
Stated under "Adapt" above. Lerdahl's chromatic circle of fifths, as this paper applies it, makes the
move C major → A minor the cheapest tonality change there is (distance 1, the same as C major →
F major or → G major), on the ground that the relative major shares all but one pitch class with the
harmonic minor (p. 6, footnote 6). The record's legacy L3 design (D-347, LEGACY) went the opposite
way. No verdict; a published-theory position the detail specification must meet. Routed to L2's detail
specification as a FACT of this paper.

**(6) No falsifier.** Nothing read contradicts any CHOSEN design point: DP-B's chosen "no" is exhibited
by the paper's own joint design; DP-C's chosen "with" is supported by the authors' own report of the
rival; the L2 charter's coupling clause is exhibited without its quotation. **No STOP fires** under the
remedial commission's §5. The one thing found that the record states otherwise — the by-name
attribution — sits in a sealed draft and is already covered by a routed correction.

## Centrality

**CENTRAL, on a narrow ground.** Its measured results carry no load anywhere in the record: they are
on synthetic material and on a ten-fragment corpus without a figure, and no design point cites them.
What does carry load is what the record SAYS about this paper — the sealed first-stage draft names it
as the source of the charter's second "sign" — and this read's finding that the held document says
nothing of the kind bears on the L2 charter's [FACT — both] sentence and on V7. A second independent
extraction under the original commission's §4 central-source rule is therefore **owed**, and its one
decisive question is narrow: does the held document anywhere state that coupling the two axes, or a
compatibility between them, lowered accuracy? It has not been performed and is recorded here as owed.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`cowork_reading_pass_findings_2026_08_31.md` and `docs/research_papers/BIBLIOGRAPHY.md` are untouched;
findings (1) to (5) are routed and written nowhere else. It fetches nothing: the GfKl chapter the
bibliography names was not fetched and is not read. It opens no code, touches no measurement tool, no
corpus, no golden and nothing under `tools/`. It writes no open-items row and allocates no
decisions-register identity. It reads no other paper and takes no decision about the order of the
remaining slice.

---

*Provenance: written 2026-09-05 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_thirteen.md` and performed the ordinary session-start read
(`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived gating answer). Read for this
extract, at the files: `reading_pass/l2_slice_reading_progress.md` whole,
`cowork_reading_pass_remedial_commission_2026_08_31.md` whole,
`cowork_reading_pass_commission_2026_08_30.md` whole, the row 27 extract
`reading_pass/extracts/rocher-robine-hanna-oudre-2010-concurrent-estimation-of-chords-and-keys.md` whole
as the form to match, `reading_pass/candidacy_upgrades.md` and
`cowork_l2_task_b_slice_derivation_2026_09_05.md` at their row 28 lines (located with `Grep` on the
staged copies), `docs/research_papers/BIBLIOGRAPHY.md` lines 1–45, `FRAMEWORK.md` §5 L2 and L3 (lines
386–450), §9 DP-B and its neighbours (lines 676–707) and the Appendix B L2 block (lines 1714–1727), and
`cowork_reading_pass_findings_2026_08_31.md` §DP-B (lines 138–154), §DP-C (lines 156–178) and its
verification-table row V7. The paper itself was read at the object as page images, all 24 pages. No
shell command was run on the repository or on any staged copy of it for content or for listings. No
figure of this project's own measurement is restated (#17f, D-431); every value above is the paper's
own, quoted with its printed page.*

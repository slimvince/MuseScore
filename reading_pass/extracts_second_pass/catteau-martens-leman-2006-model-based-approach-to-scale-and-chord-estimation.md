# Catteau, Martens & Leman — "A Model based approach to scale and chord estimation"

## SECOND INDEPENDENT EXTRACTION — Task B slice row 28

> **What this file is.** The second of the two independent extractions the original reading-pass
> commission's §4 fourth bullet requires of a CENTRAL source
> (`cowork_reading_pass_commission_2026_08_30.md`, lines 106–110, read whole at the object this
> sitting): *"CENTRAL sources — any paper whose claims would carry load in a detail specification
> or against a design point — are extracted in a SECOND independent pass (a fresh session, or a
> cleanly separated re-read that does not consult the first extract) and the two extracts
> cross-checked; disagreements are resolved at the paper or recorded as unresolved. The population
> file marks which papers are central."*
>
> **The route taken is the second of the two the bullet names** — a cleanly separated re-read that
> does not consult the first extract. The first extract,
> `reading_pass/extracts/catteau-martens-leman-2006-model-based-approach-to-scale-and-chord-estimation.md`
> (29,138 bytes at a bridge listing), **was not opened before this text was written and landed.**
>
> **THE INDEPENDENCE BOUND, DECLARED RATHER THAN CLAIMED AWAY.** This session read the
> hundred-and-sixty-ninth handoff entry whole at boot, and read the progress table's row 28 — whose
> cells carry the first extract's *candidacy verdict* (**CENTRAL**, on the narrow ground *what the
> record says about it, not its figures*) and its reading grade (**AT THE OBJECT**, whole, all 24
> printed pages). That much of the first pass's conclusion reached this side before it read the
> paper, and it is contamination. **What did NOT reach it:** any statement of the first extract's
> content, any figure it carries, any claim it labels, and any judgment it reaches beyond the
> candidacy verdict named above. The hundred-and-sixty-ninth entry deliberately summarises the
> content of no paper.
>
> **Everything in §2 through §7 below is read at the paper's own page images this sitting**, staged
> through the bridge and opened with the file tools. **The two statements from the record that §1
> cites** — the bibliography's row for these authors, and the progress table's row 28 — **were read
> at those two files themselves this sitting** and are named where they appear. Nothing here is
> taken from any other extract.

---

## §1 — Identity, and what the held document actually is

**The held file** is `docs/research_papers/catteau_martens_leman_2006_gfkl_key_chord_recognition.pdf`,
**944,281 bytes** — the only file in that folder whose name carries these authors' names, read at a
bridge listing of the folder; the byte figure re-confirmed at the staging result.

**Its page count was established AT THE TOOL, not taken from the record** — a deliberately
out-of-range page request returned *"PDF has 24 pages"*. All 24 were then read, in two calls of
twelve, and **the page images were checked to be present and legible rather than the calls' success
lines being taken as the check** (the live page-image fault, hundred-and-sixty-ninth entry, cadence 4).

**What the document prints of its own identity (page 1):**

- **Title:** *A Model based approach to scale and chord estimation*
- **Authors:** Benoit Catteau¹, Jean-Pierre Martens¹, Marc Leman²
- **¹** ELIS-Digital Speech and Signal Processing Group, Universiteit Gent, B-9000 Gent, België
- **²** IPEM-Institute for Psychoacoustics and Electronic Music, Universiteit Gent, België
- Page 1 continues directly into **§1 Introduction**.

**★ AN IDENTITY OBSERVATION, RECORDED AS WHAT WAS AND WAS NOT MET IN THE PAGES AS READ.** The
document carries **no venue line, no conference or proceedings name, no year, no copyright notice
and no abstract** anywhere in the 24 pages as read. The bibliography's row for these authors
(`docs/research_papers/BIBLIOGRAPHY.md`, read at that row's line) names a different title —
*"A Probabilistic Framework for Audio-Based Tonal Key and Chord Recognition," GfKl 2006* — and marks
the row PAYWALL. **So the held document is not established at the object as the bibliography's GfKl
2006 chapter**, and this extract makes no claim either way about their relationship: it is an
extraction of the document actually held. *(The progress table's row 28 already words the row in
exactly that two-titled way; that this side met the same thing at the pages is a confirmation of the
row's wording, not a new finding.)*

**The latest-dated work in its own reference list is 2005**, and §4.3 reports on data from the
**MIREX contest 2005**, so the document postdates 2005 by its own contents. **No year is printed in
it.** The `2006` in the file name is the repository's naming and is not evidence from the document.

**What was read:** all 24 pages whole, and then a second time for pages **3–5, 7–8, 11–14 and
16–23** — every page carrying a value, a table or a quoted sentence this extract transcribes — as
the read-back that preceded this landing.
**What was NOT done:** no sweep of the repository was run for this paper — not for its authors, not
for its title, not for any of its values — so **this extract asserts nothing about what the record
elsewhere says of it.** The candidacy verdict's narrow ground (*what the record says about it*) is
therefore only half met here: this half is the paper; the other half lives wherever the record's own
statements are gathered, and this side did not gather them.

---

## §2 — What the method is, in plain words

The paper proposes one search that decides, for each stretch of audio, **a chord and a tonality
together**, rather than deciding one and then the other.

**The paper's word for the tonality is *scale***. Throughout this extract that word is used only as
the paper uses it, and it means a key — one of twelve Major keys or twelve harmonic-minor keys. Where
this extract needs the word in any other sense it says so.

The chain, as the introduction states it (page 1): *"We use a chroma vector representation to link
the theory with the acoustic observations. The chroma vectors are used to segment the audio and to
estimate the chord and scale of those segments simultaneously by means of a one-stage Viterbi search,
followed by a backtracking step to retrieve the scale and chord sequence."*

Three parts follow from that sentence and the sections under it:

1. **A segmenter** that groups frames into events on a chroma criterion (§3 of the paper, page 15),
   so that a decision is taken per event and not per frame.
2. **A transition model** over (scale, chord) couples, built from distances Lerdahl's *Tonal Pitch
   Space* supplies — one distance table between chords inside a scale, one between scales.
3. **An observation model** that matches the accumulated chroma vector of an event against a profile
   for each candidate (scale, chord) couple.

---

## §3 — Claims, labeled

### 3.1 The probabilistic frame

**[FACT — page 1, §2, equations (1)–(4)]** The quantity maximised is **P(S, C | O)**, where **O** is
the vector of observations, **S** the vector of associated scales and **C** the vector of associated
chords. Bayes' rule is applied and **P(O)** dropped as not affecting the maximisation:

- (1) `P(S,C|O) = P(S,C)·P(O|S,C) / P(O)`
- (2) `P(S,C|O) ~ P(S,C)·P(O|S,C)`

**[FACT — page 2, equation (3)]** The likelihood is assumed to factorise per event,
`P(O|S,C) = ∏ₙ P(Oₙ|Sₙ,Cₙ)`, giving
`P(S,C|O) ~ ∏ₙ P(Sₙ,Cₙ | S₁…Sₙ₋₁, C₁…Cₙ₋₁) · P(Oₙ|Sₙ,Cₙ)`.

**[FACT — page 2, equation (4)]** A **first-order assumption** is then stated in the paper's own
words — *"The assumption that a chord/scale couple only depends on the previous chord/scale couple"* —
yielding `P(S,C|O) ~ ∏ₙ P(Sₙ,Cₙ|Sₙ₋₁,Cₙ₋₁) · P(Oₙ|Sₙ,Cₙ)`.

**★ THIS IS THE STRUCTURAL CLAIM OF THE PAPER AND IT IS WORTH STATING WITHOUT THE ALGEBRA.** The
state whose transitions are modelled is the **couple** (scale, chord), not the scale with the chord
hanging off it and not the chord with the scale hanging off it. One Viterbi pass over that coupled
state is what produces both sequences, and the backtracking step recovers them.

### 3.2 The tonal space the transition costs come from

**[FACT — page 2, §2.1]** The candidate space is deliberately narrow and the paper says so: scales
are restricted to **the Major scale and the harmonic minor scale** — *"(the classic choice)"* — and
chords to **triads**, *"the minimum of three notes"*.

**[FACT — page 3]** Four triad types are enumerated, each with an example inside C: **major** (major
third then minor third — C in C Major, G in C minor); **minor** (minor third then major third — Am in
C Major, Cm in C minor); **diminished** (two minor thirds — B° in C Major, D° in C minor);
**augmented** (two major thirds — E♭+ in C minor).

**[FACT — page 4, Figure 2 and its caption]** The triads built on the C Major scale are, by degree:
**C (I), Dm (II), Em (III), F (IV), G (V), Am (VI), B° (VII)**. On the C minor scale: **Cm (I),
D° (II), E♭+ (III), Fm (IV), G (V), A♭ (VI), B° (VII)**. The caption states the consequence the paper
draws from this: the Major scale's chords are major, minor and diminished, while *"The C minor scale
has also an augmented chord on the third degree."*

**[FACT — page 3]** The paper draws an inference from that asymmetry: *"Within the diatonic context …
one can deduce what scale the musical piece is written in, just by detecting triads which point to a
unique scale. Should the composer only use diatonic notes, the detection of an augmented chord for
instance would point directly to a minor scale."*

**[THEORY — pages 3–4, cited to Lerdahl [8] and Krumhansl [7]]** The distance geometry is imported,
not derived here. Krumhansl's multidimensional scaling produced a cone (Figure 3); Lerdahl inverted
it, added a level and repeated each level's notes in the levels beneath, giving **five levels**:
**root level, level of fifths, triadic level, diatonic level, chromatic level** (Figures 3 and 4).

**[FACT — pages 4–6]** Two circles are used. The **diatonic circle of fifths** (Figure 6) orders the
seven diatonic pitch classes and labels each with its degree: **0(I), 5(IV), 7(V), 11(vii°), 2(ii),
4(iii), 9(vi)**. The **chromatic circle of fifths** (Figure 8) is introduced for modulation, where
*"the numbers indicate the root of the scale"*.

**[FACT — page 5]** A worked distance is given: changing the C chord to the F chord **inside** the
scale of C costs **5**, stated as *"4 pitch classes + 1 translation"*.

**[FACT — page 6, with footnote 6]** For a change of scale, *"when the music modulates from Major to
minor or vice versa, one only has to measure the number of translations needed to move to the
relative Major scale. Thus, the distance on the chromatic scale from C Major to D minor is the same
as from C Major to F Major and equals one."* Footnote 6 defends the choice: the relative Major scale
uses all the pitch classes of the minor scale but one — the leading note of the harmonic minor scale
is lowered again (g rather than gs, comparing A minor with C Major).

**[FACT — pages 6–7] THE DELIBERATE SIMPLIFICATION, IN THE PAPER'S OWN WORDS.** Having shown that a
distance could be computed for every transition, the paper declines to do so: *"This though, would
assume the theory to be perfect and give the algorithm less freedom, making it unable to include
other conditions. We have decided to adopt general results presented by Lerdahl: the distance between
diatonic chords within the same scale, and the distance between the different scales, which will
serve to model P(Sₙ,Cₙ|Sₙ₋₁,Cₙ₋₁)."*

### 3.3 The two distance tables, transcribed as printed

**[FACT — page 7, Table 1]** *"The chord matrix for major scales: on (x,y) roots of Cₙ₋₁ and Cₙ
respectively."* Rows and columns are both indexed by the fifths sequence **0 7 2 9 4 11 6 1 8 3 10 5**.
Transcribed from the page image:

| from ↓ / to → | 0 | 7 | 2 | 9 | 4 | 11 | 6 | 1 | 8 | 3 | 10 | 5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 5 | 8 | 7 | 7 | 8 | γ | γ | γ | γ | γ | 5 |
| **7** | 5 | 0 | 5 | 8 | 7 | 7 | γ | γ | γ | γ | γ | 8 |
| **2** | 8 | 5 | 0 | 5 | 8 | 7 | γ | γ | γ | γ | γ | 7 |
| **9** | 7 | 8 | 5 | 0 | 5 | 8 | γ | γ | γ | γ | γ | 7 |
| **4** | 7 | 7 | 8 | 5 | 0 | 5 | γ | γ | γ | γ | γ | 8 |
| **11** | 8 | 7 | 7 | 8 | 5 | 0 | γ | γ | γ | γ | γ | 5 |
| **6** | γ | γ | γ | γ | γ | γ | 0 | δ | δ | δ | δ | γ |
| **1** | γ | γ | γ | γ | γ | γ | δ | 0 | δ | δ | δ | γ |
| **8** | γ | γ | γ | γ | γ | γ | δ | δ | 0 | δ | δ | γ |
| **3** | γ | γ | γ | γ | γ | γ | δ | δ | δ | 0 | δ | γ |
| **10** | γ | γ | γ | γ | γ | γ | δ | δ | δ | δ | 0 | γ |
| **5** | 5 | 8 | 7 | 7 | 8 | 5 | γ | γ | γ | γ | γ | 0 |

**[FACT — page 7]** The two symbols are explained at the table: *"One remarks two new parameters γ and
δ. They originate from the fact that there exist five pitch classes that don't belong to a diatonic
scale. It is clear that they will have a value larger than the diatonic possibilities."*

**[FACT — page 8, Table 2]** *"The distance between different scales."* Both halves are indexed by the
same fifths sequence:

| to **Major** | 0 | 7 | 2 | 9 | 4 | 11 | 6 | 1 | 8 | 3 | 10 | 5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| from major | 0 | 7 | 14 | 14 | 16 | 23 | 30 | 23 | 16 | 14 | 14 | 7 |
| from minor | 7 | 14 | 21 | 21 | 23 | 23 | 21 | 16 | 9 | 7 | 10 | 14 |

| to **minor** | 0 | 7 | 2 | 9 | 4 | 11 | 6 | 1 | 8 | 3 | 10 | 5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| from major | 7 | 14 | 10 | 7 | 9 | 16 | 21 | 23 | 23 | 21 | 21 | 14 |
| from minor | 0 | 7 | 14 | 14 | 16 | 23 | 30 | 23 | 16 | 14 | 14 | 7 |

**★ A PROPERTY VISIBLE IN THE TABLE AS PRINTED, DERIVED HERE AND NOT STATED BY THE PAPER.** The
*from major → to Major* row and the *from minor → to minor* row are **identical, value for value**
(`0 7 14 14 16 23 30 23 16 14 14 7`). That is what one would expect of a table indexed by relative
displacement rather than by absolute tonic, and it is recorded because a reimplementation would need
to know it. **The paper does not remark on it**, so this is a reading of the printed values and not a
claim the paper makes.

### 3.4 The two approximations, and which one fires when

**[FACT — page 8, equations (5)–(8)]** The coupled transition is expanded two ways, and both are kept:

- (5) `P(Sₙ,Cₙ|Sₙ₋₁,Cₙ₋₁) = P(Sₙ|Cₙ,Sₙ₋₁,Cₙ₋₁) · P(Cₙ|Sₙ₋₁,Cₙ₋₁)`
- (6) `P(Sₙ,Cₙ|Sₙ₋₁,Cₙ₋₁) = P(Cₙ|Sₙ,Sₙ₋₁,Cₙ₋₁) · P(Sₙ|Sₙ₋₁,Cₙ₋₁)`
- (7) neglecting `Sₙ₋₁,Cₙ₋₁` in the first factor of (5): `= P(Sₙ|Cₙ) · P(Cₙ|Sₙ₋₁,Cₙ₋₁)`
- (8) the same neglect applied to (6): `= P(Cₙ|Sₙ) · P(Sₙ|Sₙ₋₁,Cₙ₋₁)`

**[FACT — page 8] THE SWITCH IS ON WHETHER THE SCALE CHANGED, AND THE PAPER STATES IT IN ONE
SENTENCE:** *"Now, we will use both approximations, in different situations, plus we consider
P(Cₙ|Sₙ) and P(Sₙ|Cₙ) as equal (and not depending on the event, n). The first approximation can be
used, if we know that Sₙ = Sₙ₋₁, applying the first results from Lerdahl's theory 1. If not, we used
the second formula, neglecting Cₙ₋₁, so again Lerdahl can be applied 2."*

So: **where the scale is held, the chord-to-chord table (Table 1) carries the transition; where the
scale changes, the scale-to-scale table (Table 2) carries it** and the previous chord is dropped from
the conditioning.

**[FACT — page 8]** Page 8 closes the section by saying what the profiles are needed for: *"In order to
calculate P(Cₙ|Sₙ), we need profiles to characterize the different chords and scales. The same profiles
will be used to compare the observation with the possible chord/scale couples."*
**[FACT — page 12]** The factor itself is described there: *"The two approximations have a factor
P(Cₙ|Sₙ) = P(Sₙ|Cₙ) denoting **how good a chord fits within a scale**."*

> *★ PAGE CORRECTED AT THE USER-ORDERED CHECK (§10).* This paragraph formerly cited the phrase *"how
> good a chord fits within a scale"* to **page 8**. It is printed on **page 12**. The two sentences are
> now given at their own pages.

### 3.5 The observation model

**[FACT — pages 8–9, §2.2, equations (9)–(14), Figure 9]** The observation is a **chroma vector**
(footnote 7: *"the reduction of the total energy spectrum to a vector containing the amount of chroma
present per pitch class"*). The chain from audio to chroma, as printed:

- **Framing:** frames of **150 ms** with **130 ms overlap**, with the paper's own reason — *"We prefer
  this rather long frame to obtain a reliable frequency analysis and to prevent short events, such as
  a drum kicks from having a major effect on the harmonic analysis."*
- **(9)** Hamming window, then the short-term power spectrum by STFT.
- **Log-frequency mapping** from **C1 to C8** (MIDI notes) by **linear interpolation**, reduced to
  **12 values per octave over 7 octaves, retaining 85 values** (*"7 times 12 semitones plus 1"*).
- **(10)** `Q(l) = (1-α_l)·|P(k-1)|² + α_l·|P(k)|²`, `l = 1…85`, `α_l ∈ (0,1)`.
- **(11)** `R(l) = max(Q(l), M(l)) - M(l)` — a moving Hamming window over the spectrum gives the
  background `M(l)`, which is removed so that only peaks remain.
- **(12)** `S(l) = R(l)·A(l)`, `l = 1…85` — **A-curve** weighting, *"because the auditive sensitivity
  is frequency dependent"*.
- **(13)** `T(l) = Σ_{i=1}^{I} S(l)·S(l+h(i))·e^{γ·i}` with **I = 5, γ = 0.8, h = {12, 19, 24, 28, 31}** —
  a harmonic sum favouring fundamentals.
- **(14)** `O(n) = Σ_{m=1}^{N} T(12·m)`, `n = 0,1,…11` — folding into one octave.

### 3.6 The profiles

**[FACT — page 10, §2.3] THE CHOICE OF PROFILE IS DEFENDED AND THE DEFENCE IS RECORDED WITH IT:**
*"The retrieved chroma vectors are ordered by fifths and can be used to be compared with the profiles
from Temperley's theory. We prefer Temperley's profiles, because they have been developed in order to
be used in computational, and not in psychological research. They express the amount the different
notes match to the considered scale."*

**[FACT — page 11, Table 3]** *"The profiles (TP) resulting from Temperley's reasoning"*, printed
under the header **Pitch classes 0 1 2 3 4 5 6 7 8 9 10 11**:

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Major** | 5.0 | 2.0 | 3.5 | 2.0 | 4.5 | 4.0 | 2.0 | 4.5 | 2.0 | 3.5 | 1.5 | 4.0 |
| **minor** | 5.0 | 2.0 | 3.5 | 4.5 | 2.0 | 4.0 | 2.0 | 4.5 | 3.5 | 2.0 | 1.5 | 4.0 |

**[FACT — page 11, Table 4]** *"The profiles used for the chords, built upon pitch class 0 as root"*,
printed under the header **0 1 2 3 4 5 6 7 8 9 10 11**:

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **major** | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **minor** | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| **diminished** | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| **augmented** | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |

**[FACT — page 11, Figure 10 and its caption]** *"The Temperley profile of the Major scale (black
line). The diamonds describe the profiles deduced from the Temperley profile in combination with the
major chord profile."* Read at the image, three diamonds sit on the plotted line at **approximately
positions 0, 4 and 7** of the horizontal axis, which the axis label names *Pitch classes*. *(This is a
reading of marker positions on a plotted curve, not of printed values, and is recorded as such.)*

**[FACT — page 11]** The role of Table 4 is stated: *"Those profiles (CP) have to be seen as masks:
they will generate scale dependent chord profiles (V) out of Temperley's profiles (TP)."*

**★ AN INTERNAL INCONSISTENCY IN THE PRINTED TABLES, STATED WITH BOTH READINGS AND LEFT UNRESOLVED
BECAUSE THE PAPER DOES NOT SETTLE IT.** Equation (15) below multiplies Table 3 and Table 4 **index by
index**, which requires both to be in the same column ordering. As printed they are not:

- **Table 3 is in semitone order.** Its Major row's three largest values fall at indices **0, 4, 7**
  (5.0, 4.5, 4.5), and its minor row's at **0, 3, 7** (5.0, 4.5, 4.5) — the tonic, third and fifth of
  a major and a minor triad read in semitones. Figure 10's diamonds agree, sitting at approximately
  0, 4 and 7.
- **Table 4's ones do not form a triad in semitone order.** Its major row's ones fall at indices
  **0, 1, 4**, which in semitones would be C, C♯ and E. Read instead in the **fifths order the text on
  page 10 announces and Table 1's own header uses** — 0 7 2 9 4 11 6 1 8 3 10 5 — indices 0, 1, 4
  select pitch classes **0, 7, 4**, a major triad. The same reading turns the minor row (indices
  0, 1, 9) into 0, 7, 3; the diminished row (0, 6, 9) into 0, 6, 3; and the augmented row (0, 4, 8)
  into 0, 4, 8.
- **The paper states no ordering for Table 4's columns**, and does not remark on the difference.

This is recorded because it is exactly the kind of thing a reimplementation would get wrong silently,
and because it bears on nothing else in this extract: **no value in §5 depends on which reading is
right.**

**[FACT — page 12, equations (15)–(17)]**

- **(15)** `V_i = TP_i · CP_i`, `i = 0,…,11` — the scale-dependent chord profile.
- **(16)** `P(C|S) = Σ_i CP_i·TP_i / sqrt( Σ_j CP_j² · Σ_k TP_k² )` — a **normalised inner product**.
  *(The discussion on page 24 uses the phrase *"the 'cosine distance'"* of the distance-to-probability
  step; it names no equation number, so tying that phrase to this equation is this extract's reading
  and not the paper's statement.)*
- **(17)** `P(Oₙ|Sₙ,Cₙ) = Σ_i o_i·V_i / sqrt( Σ_j o_j² · Σ_k V_k² )` — the same form, matching the
  observed chroma against the generated profile.

### 3.7 From distances to probabilities, and the constants

**[FACT — pages 12–13, equations (18)–(31)]** The conditions that make the transitions proper
distributions are written down, and the free constants are solved against them:

- **(19)** `P(Sₙ|Sₙ₋₁,Cₙ₋₁) ≈ P(Sₙ|Sₙ₋₁) = 1-α ⇔ Sₙ = Sₙ₋₁`
- **(20)** `P(Sₙ|Sₙ₋₁,Cₙ₋₁) = exp(-γ·d(Sₙ,Sₙ₋₁))`
- **(21)** `Σ_k P(Sₙ=k|Sₙ₋₁) = 1` and **(22)** `1-α + Σ_k exp(-γ·d(Sₙ=k,Sₙ₋₁)) = 1`
- **(23)** `P(Cₙ|Sₙ₋₁,Sₙ,Cₙ₋₁) ≈ P(Cₙ|Sₙ,Sₙ₋₁) ⇔ Sₙ ≠ Sₙ₋₁`
- **(24)** `P(Cₙ|Sₙ₋₁,Sₙ,Cₙ₋₁) ≈ P(Cₙ|Cₙ₋₁,Sₙ) ⇔ Sₙ = Sₙ₋₁`
- **(25)** `P(Cₙ|Sₙ₋₁,Sₙ,Cₙ₋₁) ≈ P(Cₙ|Sₙ)/P(Cₙ) ⇔ Sₙ ≠ Sₙ₋₁`
- **(26)** `P(Cₙ|Sₙ₋₁,Sₙ,Cₙ₋₁) ≈ P(Cₙ|Sₙ)·P(Cₙ|Cₙ₋₁)/P(Cₙ) ⇔ Sₙ = Sₙ₋₁`
- **(28)** `P(Cₙ|Sₙ) = ∏_{m=1}^{3} P(PC_m|Sₙ)`, `PC_m = pitch classes` — a chord's fit with a scale is
  the product over its **three** pitch classes, which is where the triads-only restriction enters the
  arithmetic.
- **(29)** `Σ_k P(Cₙ=k|Sₙ) = 1`, **(31)** `Σ_k P(Cₙ=k|Cₙ₋₁) = 1`
- **(30)** `P(Cₙ|Cₙ₋₁) = exp(λ·d(Cₙ,Cₙ₋₁))`, introduced as *"The last probability is known through
  Lerdahl's theory"*.

**[FACT — page 13] THE CONSTANTS, SOLVED AGAINST THE CONDITIONS AND NOT FITTED TO DATA:** *"Together
with the conditions, we can solve all of the parameters. We have set **α = 0.3** and this gives
**γ = 0.3**. The other one λ is determined in the same way. Here though, **α is set to 0.5**, which
yields **λ = 0.43**."*

> **★ CORRECTED AT THE CROSS-CHECK (§9), FORMER WORDING PRESERVED (#12).** This paragraph's opening
> formerly read *"THE FITTED CONSTANTS, AS THE PAPER STATES THEM"*. **The word *fitted* was wrong at
> the paper and the first extract was right against it.** Page 15 states *"This algorithm is model
> based and conceived in such a way that there is **no training needed**. There are however some
> parameters that have to be tuned"*, and the sentence quoted immediately above says the parameters are
> **solved** together with the normalisation conditions of equations (21), (22), (29) and (31). Nothing
> in the paper is estimated from data. The distinction is not cosmetic here: a constant solved against
> a normalisation condition and a constant fitted to a corpus have different standing under #19, and
> calling this one *fitted* would have credited the paper with an establishment it never claims.

**[FACT — page 13] THE OBSERVATION-MATCHING DISTRIBUTION:** *"we have suggested a normal distribution
with **μ = 0** and **σ = 0.13** for pitch classes where their presence should be zero. For the three
pitch classes belonging to the chord, we suggest a complex distribution: a gaussian distribution,
**μ = 0.33** and **σ = 0.13** for values under 0.33, above, there is a uniform distribution, value
**α = 1/(0.5 + 0.67/(√(2π)·σ)) = 0.3912**."* This leads to **(32)** `P(O|S,C) ≈ P(O|C)` and **(33)**
`P(O|S,C) ≈ ∏_{l=1}^{12} P(O_l|C)`.

**[FACT — page 14, equations (34)–(37)]** The two forms actually computed are

- **(34)** `P(Sₙ,Cₙ|Sₙ₋₁,Cₙ₋₁) = P(Sₙ|Cₙ)·P(Cₙ|Cₙ₋₁) ⇔ Sₙ = Sₙ₋₁`
- **(35)** `P(Sₙ,Cₙ|Sₙ₋₁,Cₙ₋₁) = P(Cₙ|Sₙ)·P(Sₙ|Sₙ₋₁)`

with the first factor computed by the inner product (16) and the second obtained by turning a distance
into a likelihood:

- **(36)** `P(Cₙ|Cₙ₋₁) = exp( -d(Cₙ,Cₙ₋₁) / d_norm,C )`, the distance taken from **Table 1**
- **(37)** `P(Sₙ|Sₙ₋₁) = exp( -d(Sₙ,Sₙ₋₁) / d_norm,S )`, the distance taken from **Table 2**

**★ A SIGN DISAGREEMENT BETWEEN TWO PRINTED EQUATIONS FOR THE SAME QUANTITY, RECORDED AS PRINTED.**
Equation **(30)** prints `P(Cₙ|Cₙ₋₁) = exp( **λ**·d(Cₙ,Cₙ₋₁) )` with a **positive** exponent on the
distance, while equation **(36)** prints the same left-hand side as `exp( **-**d/d_norm,C )` with a
**negative** one; and equation (20), the scale counterpart, also prints a negative exponent. A
positive exponent on a distance would make a **more** distant chord **more** probable, which runs
against the direction the sentences around these equations state — page 24 asks for *"an exponential
function so it is far more difficult to change scale, or chord."* **No remark on the discrepancy was
met in the pages as read, and this extract does not resolve it**; it is recorded as a defect of the
printed text, with both signs at their equations.

**[FACT — page 14] THE NON-DIATONIC CELL VALUES:** *"Because δ models the transition from one
non-diatonic chord to another and given the exponential relation between d(Cₙ,Cₙ₋₁) and P(Cₙ|Cₙ₋₁) it
is chosen as **δ = 2·γ**. And γ has to be larger than any transition to a diatonic chord, so it's
chosen to be **9**."* So Table 1's γ cells hold **9** and its δ cells **18**.

**★ ONE LETTER, THREE MEANINGS — STATED BECAUSE IT IS A TRAP FOR ANY READER CARRYING A VALUE OUT OF
THIS PAPER.** Three unrelated senses of the symbol **γ** were met in the pages as read: **γ = 0.8**,
the decay of the harmonic sum in equation (13), page 9; **γ = 0.3**, the exponential rate on scale
distance in equations (20) and (22), page 13; and **γ = 9**, a cell value in Table 1, page 14. The
symbol **δ** was met only in the third of those senses (**δ = 18**). **No remark distinguishing them
was met in the pages as read**, and a value quoted as "γ" out of this paper without its equation
number is not interpretable.

**[CONJECTURE — page 14, the paper's own presumption, labeled as such because the paper offers no
measurement or citation for it]** *"we have presumed that **a modulation is as hard as moving three
times from one chord to another**."* From that presumption:

- **(38)** `exp( -d_μ,S / d_norm,S ) = exp( -d_μ,C / d_norm,C )³`
- **(39)** `d_norm,S / d_norm,C = (1/3)·( d_μ,S / d_μ,C )`
- **(40)** `d_norm,S / d_norm,C ≈ 0.55`

**[FACT — page 14]** The mean distances are given as *"When computing the mean over the two matrices,
see 1 and 2, we have **d_norm,C = 8.93** and **d_μ,S = 15.17**"*.

> **★ A TRANSCRIPTION-LEVEL DEFECT IN THAT SENTENCE, RECORDED WITH THE EVIDENCE THAT SETTLES IT.**
> The sentence names the first quantity **d_norm,C**, but the value 8.93 is used as **d_μ,C** in
> equation (39) one line below, and the sentence's own clause — *"the mean over the two matrices"* —
> is a statement about mean distances, not about the normalisers. The arithmetic confirms it:
> `(1/3)·(15.17 / 8.93) = 0.566`, which is the **≈ 0.55** equation (40) prints, whereas the
> normalisers chosen in the next sentence are 11 and 20. **So `d_norm,C` in that sentence is a
> misprint for `d_μ,C`.** This is stated as a reading of the printed arithmetic, and the printed
> wording is preserved above so that a later reader sees what the page actually says.

**[FACT — page 14]** *"We have chosen **d_norm,S to be 11** and **d_norm,C 20** so that the
exponential function can discriminate well between far and near scales or chords."* (Their ratio is
0.55, consistent with (40).)

### 3.8 The segmenter

**[FACT — page 15, §3] THE DESIGN CHOICE IS STATED AS A REJECTION OF THE ALTERNATIVE:** *"this
algorithm is not frame based. If we would analyse every frame, a second step would be required to
merge all the similar frames into one event. Here, we segment the music on the basis of the chroma
vectors. A decision will be taken only after a segment has been recognised. All the frames belonging
to it, are accumulated and based on this result, a more confident decision about the observed
scale/chord is expected."*

**[FACT — page 15, equation (41)]** The criterion is the **first moment of the chroma vector** and its
derivative: `μ₁ = (1/M)·Σ acc_i·i`, `M = Σ acc_i`, where `acc_i, i = 0…11` are the elements of the
accumulated chroma vector. *"The derivative of the first moment should be a good measure of the
harmonic content."*

**[FACT — page 15] THE THRESHOLD AND THE REASONING BEHIND IT, WHICH THE PAPER GIVES IN FULL:** *"When
there's one pitch class detected, then the first moment will coincide with the pitch class number. If
the next event is the adjacent pure tone, the difference between the two moments is equal to 1. So, to
be sure that there is another tone detected, the difference should be greater than 0.5. **A value of
0.6 for the threshold, seems sufficient.**"*

---

## §4 — Coupling facts (mandatory under the commission's §4, second bullet)

### 4.1 What the method ASSUMES about its upstream

**[FACT — pages 8–9, 15, 23]**

- **The input is AUDIO**, not a symbolic representation: a waveform, framed and Fourier-transformed.
  The observation the model consumes is a **12-element chroma vector** — equation (14) produces
  `O(n), n = 0…11`, and equation (17) matches `o_i, i = 0…11` against the candidate profile.
- **A diapason of 440 Hz is assumed.** The discussion states this plainly and states its limit:
  *"There is a diapason of 440 Hz assumed. Although there is a possibility to change this, the
  algorithm itself does not detect what the optimal choice should be."* (page 23)
- **A usable frequency range of C1 to C8**, and framing at 150 ms with 130 ms overlap — so the method
  assumes harmonic events that survive a 150 ms window, and says so in its own justification (short
  events such as drum kicks are deliberately suppressed).
- **No training corpus is assumed.** *"This algorithm is model based and conceived in such a way that
  there is no training needed. There are however some parameters that have to be tuned."* (page 15)
  The tuned parameters are the ones enumerated in §3.7 above.
- **No segmentation is assumed from outside**: the method finds its own event boundaries (§3.8).

### 4.2 What the method HANDS downstream

**[FACT — pages 16–18, 21, 23]** *(Page range corrected at the user-ordered check (§10): it formerly
read "pages 16–18, 22", which omitted the two pages this section actually cites — 21 for the monophonic
listing's extra column and 23 for the inversion sentence — and named page 22, which it does not use.)*

- **A sequence of events, each carrying a (chord, scale) pair and an end time in seconds.** The
  printed output listings on pages 16, 17 and 18 carry exactly those three columns, for example
  `1.26 F dim Ds min` (page 16). **The monophonic listing on page 21 carries a fourth column, and it
  is a leading one**: the name of the played note, ahead of the end time — for example
  `A 4.66 F Maj A min`. Whether that column is program output or was added for the page is not
  stated there.
- **The chord vocabulary handed on is the four triad types on twelve roots**, and nothing else.
  Seventh chords are not emitted: §4.1's final experiment tests *"whether the algorithm is capable to
  reduce seventh chords to the right triad, e.g. C7 to C"* (page 18).
- **The scale vocabulary handed on is 24 members** — twelve Major, twelve harmonic minor.
- **No inversion information is handed on, and the paper says why it cannot be:** *"We have used
  chroma vectors, this representation cannot handle chord inversions."* (page 23)
- **Silence is a late addition, not an original output category.** *"the algorithm does not reveal
  silences. That's why it names a silence so that the transition cost is as low as possible. To solve
  this problem, we added a second step, to evaluate if the energy was high enough, in order to be a
  real segment. The output will now indicate silences, as well as if there are two consecutive events
  labelled with the same chord/scale, they are bundled into one."* (page 16)

### 4.3 The method's own STATED SCOPE and limits

**[FACT — pages 1–2, 23, 24]** *(Page range corrected at the user-ordered check (§10): the scope
sentence the first bullet rests on is on page 1, and the range formerly began at page 2.)*

- **Western tonal music** — the introduction's own scope sentence, *"In this paper, we propose an
  algorithm for analysing Western tonal music"* (page 1), restated at page 2 as *"We consider the
  Western tonal system"*.
- **Major and harmonic minor scales only** — *"(the classic choice)"* (page 2).
- **Triads only:** *"Our model only includes top down knowledge about triads, no other chords are
  considered."* (page 23)
- **Inversions are outside what the representation can carry** (page 23, quoted above), with the
  paper noting both sides of the trade: *"On one hand it is good to represent every possible voicing
  with the same chroma vector, but on the other hand, it can be interesting how the chords are played
  in order to link one chord voicing to the next."*
- **The distance geometry is a deliberate simplification of Lerdahl's**, and the paper names the
  reason: *"the recipe to create those distances is so complex that we considered to simplify the
  model."* (page 23)
- **The segmenter is declared inadequate on real audio by the authors themselves:** *"The segmentation
  works quite well with the synthetic examples, but is far too active in real world examples."*
  (page 24)
- **The transform from distance to probability is declared not the right one:** *"For simplicity, the
  'cosine distance' has served quite well. But the cosine characteristic curve is not the desired one
  to express stability. We should move to an exponential function so it is far more difficult to
  change scale, or chord."* (page 24)

---

## §5 — Measured results, with corpus, metric and value as the paper states them

**The metric.** Every percentage below comes from *"a small tool"* the authors implemented *"to
compare the output of the algorithm with a reference list"* (page 16). Its printed output has five
lines — **Total cost**, **# of insertions**, **# of deletions**, **% of correct chords**, **% of
correct scale** — and **no definition of any of the five was met in the pages as read**: no cost
function, no alignment rule, no statement of what a percentage is taken over. That absence is
recorded as part of the measurement, not as an aside.

### 5.1 The cadence database (synthetic, Shepard tones)

**[FACT — pages 15–16]** **Corpus:** three cadences — `IV→V→I`, `VI→V→I`, `II→V→I`, *"the same cadences
as those Krumhansl used"* — *"constructed … in all of the 24 scales, yielding **72 files**"*,
synthesised from **Shepard tones** (chosen because *"the problem of harmonics is not present in this
database"*, so *"the emphasis is put on the transitions (Lerdahl's theory) rather than on the template
matching"*).

**Result, for the whole cadence database:**

| | value |
|---|---|
| Total cost | **7.07889** |
| # of insertions | **1** |
| # of deletions | **0** |
| % of correct chords | **80** |
| % of correct scale | **100** |

**[FACT — page 16]** The worked example is `I→II→V→I` in D♯ minor. The algorithm's output and the
reference are printed side by side:

| algorithm | reference |
|---|---|
| `0.12 Silence` | `0.50 Ds min Ds min` |
| `0.66 Ds min Ds min` | `1.10 F dim Ds min` |
| `1.26 F dim Ds min` | `1.70 As Maj Ds min` |
| `1.86 As Maj Ds min` | `2.30 Ds min Ds min` |
| `2.42 Ds min Ds min` | |

> **★ A TENSION BETWEEN THE PROSE AND THE LISTING IT DESCRIBES, RECORDED AND NOT RESOLVED.** The prose
> beneath the listing says *"The program says that there is a D min chord that last till 0.12
> seconds"*, and then explains that a silence is there instead and that a second energy step was added
> to fix it. **The listing as printed already reads `0.12 Silence` on that line** — that is, it appears
> to show the output *after* the remedy the prose is about to describe. The paper does not say which
> state of the program each listing came from. This matters for anything read out of these listings,
> which is why it is recorded here rather than left for a reader to trip over.

### 5.2 The cadence database, MIDI-to-WAV synthesised

**[FACT — page 17]** *"After good results with this primitive database we have done the same
experiment, but now with a MIDI to WAV synthesized version. This means that there will also be other
harmonics in play."* The printed result is a four-line listing and **no percentage table is given for
this run**:

```
0.2      Silence
2.02     Ds min Ds min
5.62     As Maj Ds min
7.25999  Ds min Ds min
```

**[FACT — page 18]** Two further experiments are reported as listings with **no percentages**: an
**arpeggio** test (*"the notes of the chord played after each other"*), whose listing runs seven lines
and includes `3.04 D dim Ds min`, `3.46 B dim Ds min`, `4.24 D dim Ds min`, `4.66 B dim Ds min`; and a
**seventh-chord** test, whose printed listing is **identical, line for line, to the MIDI-to-WAV
listing quoted immediately above**. *(That identity is stated because it is what the two pages print,
not because the paper claims it.)*

### 5.3 The modulation database

**[FACT — pages 18–19]** **Corpus:** *"10 files – once in Shepard tones, once MIDI to WAV synthesized –
illustrating no modulation, easy and difficult modulations"*, using **only C Major and C minor as a
starting point**, *"just like in Krumhansl's second experiment [3]"*. Table 5 holds the ten chord
sequences; Table 6 the scales they move between. The paper states the design: the first chord
indicating the modulation is set in bold; pivot chords appear where the new scale is near
(*"sequence 3: B min is the seventh degree of C major and the third of G major"*); and *"To accomplish
a more difficult modulation the highlighted chords are non-diatonic."*

**[FACT — page 19, Table 6]** The scale sequences, transcribed in full:

| | from → to |
|---|---|
| sequence 1 | C major → C major |
| sequence 2 | C minor → C minor |
| sequence 3 | C major → G major |
| sequence 4 | C major → A♯ major |
| sequence 5 | C major → A minor |
| sequence 6 | C major → D minor |
| sequence 7 | C minor → F minor |
| sequence 8 | C minor → C♯ minor |
| sequence 9 | C minor → C major |
| sequence 10 | C minor → G♯ major |

*(The paper writes sharps as a trailing `s` — `As major`, `Cs minor`, `Gs major` — per its own
convention; they are rendered here as ♯.)* The caption states *"the first two don't modulate!"*, which
Table 6's first two rows show.

**[FACT — page 19, Table 5]** The ten chord sequences are printed as **nine chords each** (counted at
the page on the read-back), with the modulating chord in bold. **The bolded chord per sequence is:**
sequence 3 **B min**, 4 **G min**, 5 **E maj**, 6 **A♯ maj**, 7 **C♯ maj**, 8 **A maj**, 9 **A min**,
10 **D♯ maj**; sequences 1 and 2 carry no bold, consistent with their not modulating.
**A BOUND ON THIS ROW: the un-bolded cells of Table 5 are not transcribed here**, because no claim in
this extract rests on them. A later reader who needs them reads them at page 19.

> **★ A THIRD INTERNAL TENSION, AT THE SAME PLACE AND RECORDED WITHOUT A VERDICT.** Page 18 says of
> the easiest modulation: *"Sometimes, when the new scale is not far off, the chord fits with both
> scales, as in sequence 3: **B min is the seventh degree of C major** and the third of G major. Those
> chords are so-called pivot chords."* **By the paper's own Figure 2 (page 4), the triad on the seventh
> degree of the C Major scale is B°, a diminished triad, and not B minor** — Figure 2's own label for
> that degree is `B°`. The paper does not reconcile the two, and this extract takes no verdict; it
> records that a reader carrying the pivot-chord example out of this paper is carrying a sentence its
> own Figure 2 contradicts.
>
> *★ NARROWED AT THE USER-ORDERED CHECK (§10); FORMER WORDING PRESERVED (#12).* This note formerly
> opened by setting that sentence against a second one in the same paragraph — *"To accomplish a more
> difficult modulation the highlighted chords are non-diatonic"* — and asserted: **"Both cannot hold of
> sequence 3 at once — a chord cannot be non-diatonic and be a degree of the starting scale."**
> **That was this side's own manufactured contradiction and it is withdrawn.** The paper's sentence is
> conditioned on *a more difficult modulation*; on its plain reading it says that where a **harder**
> modulation is wanted the highlighted chord is non-diatonic, which says nothing about sequence 3, the
> case the very next sentence offers as the **easy** one. The tension that survives the check is the
> Figure 2 one alone, and it stands on its own.

**Results.** For the **Shepard tones** version:

| | value |
|---|---|
| Total cost | **18.637** |
| # of insertions | **0.7** |
| # of deletions | **0** |
| % of correct chords | **90.1515** |
| % of correct scale | **85.1515** |

For the **MIDI to WAVE rendered** files:

| | value |
|---|---|
| Total cost | **37.9343** |
| # of insertions | **0.9** |
| # of deletions | **0.2** |
| % of correct chords | **75.134** |
| % of correct scale | **86.655** |

**[FACT — page 20] THE AUTHORS' OWN READING OF THAT PAIR:** *"We can see that the number of correct
chords is not that elevated any more, because a new difficulty has been introduced: the building tones
have now certain harmonics. But, we do see that we have an equally high performance for scale."*
*(Their two scale values are 85.1515 and 86.655; their two chord values 90.1515 and 75.134.)*

**[FACT — page 20]** A qualitative observation on sequence 5: *"the algorithm decides to make a
modulation along F Major. A more subtle difference is the detection of D diminished instead of B
diminished; two notes coincide for those two chords, so it is not really a huge mistake."*

### 5.4 Monophonic input

**[FACT — page 21]** **Corpus:** one ascending and descending **C major scale**, MIDI rendered to WAV.
The printed output runs sixteen lines, of which the paper's own reading is:

*"Given the fact that the input was a simple C major scale, the output is not very good. Although we
cannot be unhappy with the result. Although the input was monophonic, the algorithm has tried to fit
chords under it. And it has chosen to use chords mainly from C Major. What's more, we see the most
common chords of the scale: C Major itself, F Major and G Major. This means that the algorithm is
capable to retain the relationship between C Major as a scale and the possible chords. From A on, it
changes to the relative minor scale, but it uses chords here different than the diatonic chords: F
diminished and F minor, where the diatonic chord is F Major. Still, the played note is always present
in the chord. We can even see that the output contains the same symmetry as the input."*

**No percentage is reported for this test.** The listing's scale column reads `C Maj` for the first six
lines, `A min` for the middle five (from the note A onward), and `C Maj` for the last five.

### 5.5 Real audio fragments

**[FACT — page 22, §4.2]** **Corpus:** *"a small database of **10 fragments, of 60 seconds each**"*,
annotated by the authors with chords and scales. Table 7, transcribed in full:

| | artist | title | key |
|---|---|---|---|
| test song 1 | Creedence Clearwater Revival | Proud Mary | D Major |
| test song 2 | Creedence Clearwater Revival | Who'll stop the rain | G Major |
| test song 3 | Creedence Clearwater Revival | Bad moon rising | D Major |
| test song 4 | America | Horse with no name | E Minor |
| test song 5 | Dolly Parton | Jolene | C♯ Minor |
| test song 6 | Toto Cutugno | L'Italiano | A Minor |
| test song 7 | Iggy Pop | The passenger | A Minor |
| test song 8 | Marco Borsato | Dromen zijn bedrog | C Minor |
| test song 9 | Live | I Alone | G♭ Major → E♭ Major |
| test song 10 | Ian McCulloch | Sliding | C Major |

**★ NO NUMERICAL RESULT IS REPORTED FOR THIS CORPUS, AND THE PAPER STATES WHY:** *"Because of the fact
that the complexity of the input now has changed dramatically, the program detects a lot more events
than there really are. This means that a strict comparison of the processed output to the reference is
not relevant here. Still, we can compare the output and the reference graphically, see figure 17."*
The reported outcome is therefore qualitative: *"the algorithm is capable of detecting most of the
chords, but that the scale changes too often. In another example (Live - I alone), there is a
modulation, and we can see that the modulation is detected, but the scale detection sort of moves
around the right scale."*

**This corpus is the only one in the paper stated to be recordings rather than synthesised material,
and it carries no reported value.** *(The MIREX fragments of §5.6 are the paper's one other corpus that
is not stated to be synthesised — but the paper says nothing at all about what they are, so this
extract makes no claim about them either way. That qualification was added at the user-ordered check
(§10); the sentence formerly read "the paper's only non-synthesised music apart from the MIREX
fragments of §5.6", which credited the paper with a statement about the MIREX material it never
makes.)* It is not alone in carrying no value: the MIDI-to-WAV cadence run (§5.2), the
arpeggio and seventh-chord tests, and the monophonic test (§5.4) also report listings without
percentages. What is particular here is that the paper states a **reason** for reporting none — the
segmenter over-produces so far that the comparison would not mean anything. That is recorded as a
property of the evidence, not as a criticism.

### 5.6 The MIREX 2005 scale figures

**[FACT — page 23, §4.3]** *"Because of the data available for the MIREX contest 2005, we have
implemented a routine that determines what the **mean scale** of the input is. That way we were able to
see whether our algorithm succeeds in estimating the scale of the **96 fragments present in the
training database**. After testing, we applied the cost measure as presented on the site. We obtained
**82% with a crispy count** and **90% after using the cost measure**."*

**Three qualifications the sentence itself carries, and they travel with the values:**

1. The quantity measured is a **mean scale of the whole input**, produced by a **routine implemented
   for the contest**, not the per-event scale sequence the rest of the paper is about.
2. The set is the **training database** of that contest, 96 fragments.
3. The **82%** and the **90%** are two measurements of the same run under two different counting rules
   — a plain count and the contest's own cost measure — **not two systems and not two corpora**.
   Quoting one without the other, or either without its rule, misstates what was measured.

### 5.7 The profile-correlation aside

**[FACT — page 23, §5, with footnote 8]** In arguing that Lerdahl's and Temperley's top-down knowledge
share an origin in Krumhansl's research, the paper counts how often each pitch class appears in
Lerdahl's schematic representation of the major scale — *"**5 1 2 1 3 2 1 4 1 2 1 2**"* — and
correlates that count vector with the profiles: *"When computing the correlation of this simple
deduction with the Temperley profiles we obtain **96.2%**. Even compared to Krumhansl's profiles we
have of correlation of **97.2%**."* Footnote 8 states the measurement used: *"again the correlation is
measured by computed the normalised inner product"* — **the same form equations (16) and (17) use, and
not a Pearson correlation**, which is what the word *correlation* would ordinarily be taken to mean.
The footnote's own wording is printed as quoted. *(This sentence formerly read "the cosine of equation
(16)"; the footnote names no equation, so it is stated as the same form rather than as that equation —
narrowed at the user-ordered check, §10.)*

---

## §6 — What the paper concludes, in its own words

**[FACT — page 24, §6]** The whole of the conclusion is one sentence: *"We have shown that departing
from a model, we are able to detect chords and scales in a confident and straightforward way."*

**[FACT — pages 23–24, §5]** The discussion, by contrast, names things to improve, and they are named
here rather than counted: the inversion-blindness of chroma; the triads-only vocabulary; the assumed
and undetected diapason; the cosine transform that *"is not the desired one to express stability"*; and the segmenter
that is *"far too active in real world examples"*, for which two remedies are floated — *"Or there
should be another decision rule, or a second pass can be adopted to collect the similar events into
one bag."*

**★ THE GAP BETWEEN THOSE TWO IS ITSELF WORTH RECORDING.** The conclusion claims a confident and
straightforward detection of chords and scales; the discussion immediately above it, and §4.2, record
that on the real-audio songs the segmenter over-produces so far that no value could be reported.
Both are the paper's own statements, at their pages, and this extract takes no verdict between them.

---

## §7 — The reference list, and the citation defects met in the pages as read

**[FACT — page 24]** The reference list holds **eight** entries:

1. TEMPERLEY, D. (1999): *What's Key for Key? the Krumhansl-Schmuckler Key-Finding Algorithm
   Reconsidered.* Music Perception, 17(1), 65–100.
2. SHENOY, A., WANG, Y. (2005): *Key, chord, and Rhythm Tracking of Popular Music Recordings.*
   Computer Music Journal, 29(3), 75–86.
3. KRUMHANSL, C.L., KESSLER, E.J. (1982): *Tracing the Dynamic Changes in Perceived Tonal Organization
   in a Spatial Representation of Musical Keys.* Psychological Review, 89, 334–368.
4. PAUWS, S. (2004): *Musical key Extraction from Audio.* Proceedings of the 5th ISMIR 2004,
   Barcelona, 96–99.
5. İZMIRLI, Ö. (2005): *Tonal similarity from audio using a template based attractor model.*
   Proceedings of the 6th ISMIR 2005, London, 540–545.
6. BELLO, J.P., PICKENS, J. (2005): *A robust mid-level representation for harmonic content in music
   signals.* Proceedings of the 6th ISMIR 2005, London, 304–311.
7. KRUMHANSL, C.L. (1978): *Concerning the applicability of geometric models to similarity data: The
   interrelationship between similarity and spatial density.* Psychological Review, 85, 445–463.
8. LERDAHL, F. (2001): *Tonal Pitch Space.* Oxford University Press, New York.

**★ TWO CITATION DEFECTS WERE MET IN THE PAGES AS READ, AND EACH IS RECORDED AT BOTH ITS ENDS.**

**(1) A wrong reference number for Lerdahl's book.** Page 1 reads *"The book written by Lerdahl is
regularly being referred to as well, see **[5]**."* Reference **[5]** is İzmirli 2005, a conference
paper on tonal similarity; **Lerdahl's book is reference [8]**.

**(2) Reference [7] is called a dissertation, and it is a journal article.** Page 3 reads *"One of
the famous results of **the dissertation by Krumhansl[7]** is the multidimensional scaling."*
Reference **[7]** is *Krumhansl, C.L. (1978), Concerning the applicability of geometric models to
similarity data …, Psychological Review, 85, 445–463.* Figure 3 on page 5 carries its own source line
inside the left-hand drawing, crediting a **Krumhansl Stanford dissertation** — **its year is printed
too small to read reliably at the resolution used here and is therefore not stated**. So the work the
text leans on for the multidimensional scaling and the work reference [7] names are not evidently the
same document, and the paper does not reconcile them.

**The citations this side checked and found to match their entries** are **[2]** (Shenoy & Wang, cited
on page 1 for the chord-then-scale-then-enhancement algorithm), **[6]** (Bello & Pickens, cited on
page 1 for HMM chord estimation), **[4]** (Pauws, cited on page 1 for profile-matching key extraction)
and **[3]** (Krumhansl & Kessler, cited on pages 15 and 18 for the two experimental designs §4.1
reproduces). **[1]** and **[8]** carry no numbered in-text citation this side met; Temperley and
Lerdahl are referred to by name.

**★ AND TWO BARE NUMERALS ON PAGE 8 WHOSE REFERENT THE PAPER DOES NOT STATE**, recorded at the
user-ordered check (§10) because a reader may take them for citations. The sentence that switches
between the two approximations ends its clauses *"applying the first results from Lerdahl's theory
**1**. If not, we used the second formula, neglecting Cₙ₋₁, so again Lerdahl can be applied **2**."*
The numerals sit where a reference marker would sit, but **[1]** is Temperley and **[2]** is Shenoy &
Wang, neither of which is Lerdahl. Read instead as labels for *the first* and *the second* of Lerdahl's
two adopted results — the within-scale chord distance and the between-scale distance, which the
paragraph on pages 6–7 names in that order — they are consistent with the text. **The paper states
neither reading**, and this extract takes no verdict.

**Which references the method actually rests on**, as opposed to mentions: **[8]** Lerdahl, for the
distance geometry of §2.1 and Tables 1 and 2; **[7]** Krumhansl 1978, for the multidimensional
scaling the cone comes from — subject to defect (2) above; **[1]** Temperley, for the profiles of
Table 3; and **[3]** Krumhansl & Kessler, for the two experimental designs §4.1 reproduces (the
cadence set and the modulation set).

---

## §8 — The read-back and the sweep, written in the act that ran them

*This section was added as its own edit after §1–§7 were finished and before the first landing, which
is the order the procedure requires: the text is written, then read back against the paper and swept,
and only then does the record of those two acts go in.*

### 8.1 The read-back

**Every page carrying a value, a table or a quoted sentence this extract transcribes was opened a
second time** — pages **3–5, 7–8, 11–14 and 16–23** — and each transcription compared against the
page. **What was checked, named rather than counted:** Table 1's twelve rows; Table 2's four rows and
both headers; Tables 3 and 4; Figure 10's marker positions; equations (5)–(8), (15)–(17), (19)–(31)
and (34)–(40); the constants α, γ, λ, μ, σ and the uniform-branch value; δ = 2·γ and γ = 9;
d_norm,S = 11 and d_norm,C = 20; the cadence result block; the D♯-minor example and its reference
listing; the MIDI-to-WAV cadence listing; the arpeggio listing; the seventh-chord listing; Table 5's
bolded chords and its nine-chords-per-row shape; Table 6's ten rows; both modulation result blocks;
the monophonic listing and its scale column; Table 7's ten rows; the MIREX sentence; the
pitch-class count vector and the two correlation percentages; and the reference list.

**No transcribed value moved.** Every table, listing and constant above reproduced at the page
exactly as §3 and §5 print it.

**What the read-back ADDED**, because a second pass over a page sees what a first pass writing from it
does not:

- **The tension at the pivot-chord example** (§5.3's third boxed note) — page 18 calls sequence 3's
  B min *the seventh degree of C major*, while the paper's own Figure 2 puts **B°** on that degree.
  *(This bullet formerly described the tension as one between two sentences of that paragraph; the
  user-ordered check (§10) withdrew that half, and the bullet now names what survives.)*
- **The second citation defect** (§7, defect 2) — reference [7] called a dissertation in the text and
  printed as a Psychological Review article in the list, with Figure 3's own source line crediting a
  Stanford dissertation.
- **The fourth column in the monophonic listing** (§4.2) — the played note's name, which the other
  listings do not carry.

### 8.2 The sweep for absolutes

The finished text was swept for absolute and totalising words — *only, never, nowhere, every, all,
none, always, any, exhaustive, complete, comprehensive, total, whole, entire, first, unique, nothing,
cannot, impossible, independent, resolved, identical, exactly* — and **every hit was read at its own
line** rather than counted. Hits inside quotations from the paper were left as the paper writes them.

**What the sweep corrected, each named with what was wrong with it:**

- *"Nothing in it is relayed from the record"* — **false as written**, and contradicted by the
  independence bound six lines above it, which records that the candidacy verdict did reach this side.
  Replaced by a statement of which two record statements §1 cites and that both were read at their
  own files.
- *"visible in every printed output listing"* — **false**: the monophonic listing on page 21 carries a
  leading note-name column the others do not. Corrected, and the extra column is now recorded.
- *"the repertoire closest to unconstrained input in the whole paper … the one on which the paper
  reports no value at all"* — **two defects in one sentence**: the MIREX fragments of §5.6 are real
  audio too, and four other tests also report listings without percentages. Replaced by what is
  actually particular here, which is that the paper states a reason for reporting none.
- *"on the only non-synthetic repertoire tested"* — the same error in §6, corrected there too.
- *"The paper flags none of this"* and *"The paper does not remark on the discrepancy"* — negatives
  over the whole document asserted as facts about the document. Both rewritten as **met nowhere in
  the pages as read**, which is what a whole read establishes.
- *"The symbol γ carries three unrelated values in three places"* — an enumeration presented as
  exhaustive without a search establishing it. Now **three senses met in the pages as read**; the
  same for δ.
- *"Every observation the model ever sees"* — an absolute where the two equations that settle it
  serve better. Replaced by the equations.
- *"the paper defines none of the five"* — same shape, same correction.
- *"the paper's whole argument is that distant chords and scales should be discouraged"* — a claim
  about the paper's whole argument, where what is evidenced is the direction of the sentences around
  those equations. Narrowed to that.
- *"the discussion lists five things to improve"* — a count of the paper's items where naming them
  costs nothing and asserts less. Named instead.
- *"for the whole distance geometry of §2.1"* — overstated: Krumhansl 1978 supplies the
  multidimensional scaling that geometry is built on. Narrowed.
- *"exactly one file of that name in that folder"* — trivially true of a name and not the claim meant.
  Replaced by the claim that was meant: the only file there whose name carries these authors' names.
- *"twice over for the pages the read-back names (§8)"* — a forward reference to a section that did
  not exist at the time it was written. Replaced by the page numbers themselves.
- *"one citation defect in the text"* in §7's heading — **falsified by the read-back**, which found a
  second. The heading no longer carries a count.

**What the sweep did NOT do.** It reached this extract's own prose and nothing else. It did not
re-open the paper's sources, ran no web access, touched no other file, and **did not compare this
extract against the first extract** — that is §9's act, and §9 is not written at this landing.

### 8.3 What this extract does not establish

- **It does not establish the held document's identity as the bibliography's GfKl 2006 chapter.**
  §1 records what the document prints of itself and what the bibliography row says, and stops there.
- **It does not report what the record elsewhere says about this paper.** No repository sweep was run
  for it. The candidacy verdict's narrow ground is therefore half met, and §1 says which half.
- **It resolves none of the defects it records in the paper** — the Table 3 / Table 4 ordering; the
  sign disagreement between equations (30) and (36); the prose-against-listing tension at the D♯-minor
  example; the seventh-degree tension at the pivot-chord example; the two citation defects of §7; and
  the two bare numerals on page 8. Each is recorded with both readings at their pages, which is what
  the commission's *"resolved at the paper or recorded as unresolved"* provides for. *(This bullet
  formerly said "the four internal defects"; the count was made wrong by the user-ordered check (§10),
  which added two records and narrowed one, so the members are named instead.)*
- **It takes no verdict on the paper's standing as a candidate** for any charter or design point, and
  routes nothing. That is the findings surface's act, not an extract's.

---

## §9 — The cross-check against the first extract

*Added as its own edit AFTER §1–§8 had been landed and proved on disk. The first extract,
`reading_pass/extracts/catteau-martens-leman-2006-model-based-approach-to-scale-and-chord-estimation.md`
(29,138 bytes, unchanged on the device since 2026-09-05), was opened for the first time at this step
and read whole. Everything §1–§8 says was written before it was opened.*

### 9.1 Where the two reads agree

**Every NUMERIC value both extracts transcribed agreed, digit for digit.** Named rather than counted —
and the qualifier matters, because §9.2 below reports a disagreement over a **scale name**, which
carries no digits. *(This sentence formerly read "Every value both extracts transcribed agreed", which
§9.2's own heading falsified two paragraphs later. Narrowed at the user-ordered check, §10; former
wording preserved here, #12.)*

- Temperley's Major and minor profiles (Table 3), all twenty-four values.
- The cadence result block — cost 7.07889, 1 insertion, 0 deletions, 80 % chords, 100 % scale.
- Both modulation result blocks — 18.637 / 0.7 / 0 / 90.1515 / 85.1515, and
  37.9343 / 0.9 / 0.2 / 75.134 / 86.655.
- The MIREX sentence — 96 fragments, 82 % on a plain count, 90 % under the contest's cost measure.
- The discussion's count vector 5 1 2 1 3 2 1 4 1 2 1 2, and 96.2 % / 97.2 %.
- Every constant: α = 0.3 → γ = 0.3; α = 0.5 → λ = 0.43; γ = 9 and δ = 2·γ; d_norm,S = 11 and
  d_norm,C = 20; the printed *"d_norm,C = 8.93 and d_μ,S = 15.17"* including its printed first
  subscript, which both reads flagged independently; ≈ 0.55; μ = 0 / σ = 0.13, and μ = 0.33 /
  σ = 0.13 with a uniform branch; the 0.6 segmentation threshold and the 0.5 it is argued from.
- The front end: 150 ms frames with 130 ms overlap, C1–C8, 85 values, I = 5, γ = 0.8,
  h = {12, 19, 24, 28, 31}.
- The corpora: 72 cadence files over 24 scales; ten modulation sequences, eight of them modulating;
  ten real-audio fragments of 60 seconds; 96 MIREX fragments.
- The structural reading: the hidden state is the (scale, chord) **couple**; one Viterbi pass with
  backtracking; equations (34) and (35) as the two branches, switched on whether the scale is held;
  the coupling as a probability factor and not a constraint; distances taken from Lerdahl and not
  estimated from data; 24 scales and four triad types; no inversions, no sevenths, no alternatives.

**The first extract transcribes the cells of none of Tables 1, 2 and 4.** For Tables 1 and 2 it says so
in terms — *"The individual cells of the two tables are not transcribed here; the page images are the
record."* For **Table 4 it says nothing of the kind**: it names the four chord profiles and their root
without giving their cells. Either way those transcriptions in §3.3 and §3.6 are carried by this
extract alone and were not doubled. *(The sentence formerly put Table 4 inside the first extract's own
disclaimer, which covers only Tables 1 and 2 — corrected at the user-ordered check, §10.)*
**What the first extract does say about Table 1 is checkable against them and holds:** rows and columns
in fifths order, and *"the diatonic-to-diatonic entries take values among 0, 5, 7 and 8"* — which is
exactly the set of values in the six-by-six diatonic block of §3.3's transcription.

### 9.2 The one value disagreement, resolved at the paper — the FIRST extract is wrong

**The disagreement.** Listing the eight modulation targets of Table 6, the first extract writes
*"(to G major, **A♭ major**, A minor, D minor, F minor, C♯ minor, C major, G♯ major)"*. This extract's
§5.3 renders the same two rows as **A♯ major** (sequence 4) and **G♯ major** (sequence 10). Seven of
the eight agree; **sequence 4's target does not.**

**Resolved at the paper, at three places that fix the convention.** The paper writes a flat with a
trailing **b** and a sharp with a trailing **s**, and it does both in the same document:

1. **Page 3** names the augmented triad of C minor as *"the **Eb+**"*, and **Figure 2** on page 4
   labels the same chord **E♭+** and the sixth degree **A♭** — flats, written with *b*.
2. **Table 7** on page 22 gives test song 9's key as *"**Gb** Major → **Eb** Major"* — flats again with
   *b*.
3. **Table 7** gives test song 5, Dolly Parton's *Jolene*, as *"**Cs** Minor"*. That recording is in
   C♯ minor, so *s* is a sharp.

**So Table 6's *"As major"* is A♯ major, pitch class 10 — enharmonically B♭ major — and not A♭ major,
pitch class 8.** The reading is confirmed by the sequence itself: Table 5's sequence 4 ends
`… G min, Ds maj, F maj, As maj`, which read at pitch classes 7, 3, 5, 10 is the vi, IV, V and I of
B♭ major. Under the first extract's reading, sequence 4's target and sequence 10's target would both
be pitch class 8, and the paper's table distinguishes them.

**Nothing in either extract depends on the corrected value** — no percentage, no constant and no
structural claim rests on which of two scales sequence 4 modulates to. It is recorded because it is a
transcription defect in a landed extract, and because correcting another read's text is not this
side's act: **the first extract is left untouched, and whether it is corrected at its own site is the
user's to decide** — the same question the hundred-and-sixty-ninth entry leaves standing for row 27.

### 9.3 The one place the FIRST extract corrected THIS one

**The word *fitted*.** This extract's §3.7 formerly opened *"THE FITTED CONSTANTS"*. The first extract
states, correctly and repeatedly, that **nothing in the paper is fitted to data** — the constants are
hand-set or solved against the normalisation conditions, and page 15 says *"there is no training
needed"*. **Corrected at its site in §3.7, with the former wording preserved there (#12).** Two further
uses of the word elsewhere in this extract were corrected in the same act.

### 9.4 The decisive question the first extract left for this pass — answered, and the answer agrees

The first extract's *Centrality* section names the one question a second extraction is owed:
*"does the held document anywhere state that coupling the two axes, or a compatibility between them,
lowered accuracy?"* Its own finding (2) answers no, and records that the words attributed to these
authors in a sealed first-stage draft are Rocher's.

**This side read all 24 pages whole without knowing that the question had been asked, and met nothing
of that sign.** No comparison against any other system; no ablation of the coupling; no compatibility
constraint tried, declined or reported to lower accuracy; and none of the attributed words. The only
statements about the interaction of the two axes met anywhere in the pages are that a chord outside the
scale is less probable rather than forbidden (equations 16 and 28), and that on real audio *"the scale
changes too often"* (page 22).

**So two independent whole reads of this document, written without sight of each other, both met
nothing of that sign.** That is what the question was asked for. *(This sentence formerly also called
it "the strongest thing the doubling produced here" — a superlative over this side's own acts that
nothing derived it; struck at the user-ordered check, §10.)* **The bound stays exactly where the first
extract put it:** the GfKl chapter
the bibliography names is not held and has not been read, so **nothing is established about what IT
contains**, and neither extract claims otherwise.

### 9.5 A difference of characterisation, recorded without a verdict

The first extract states, under what the method hands downstream, *"no seventh or extension (a seventh
is reduced to a triad, p. 18)"*. At page 18 the reduction is the stated **aim** of the final experiment
— *"The aim is to see whether the algorithm is capable to reduce seventh chords to the right triad,
e.g. C7 to C"* — and what follows is a four-line listing of triads with **no sentence assessing whether
the reduction was right**. The output is triads either way, so the two readings differ in what they
credit the paper with having shown, not in what the paper prints. Recorded; neither extract is edited
for it.

### 9.6 What this extract carries that the first does not, and what the first carries that this does not

**Met only by this read** (and therefore undoubled): the full cells of Tables 1, 2 and 4; the identity
of Table 2's *from major → to Major* and *from minor → to minor* rows; the ordering inconsistency
between Table 3 and Table 4; the sign disagreement between equations (30) and (36); the three senses of
γ; the prose-against-listing tension at the D♯-minor example; the seventh-degree tension at the
pivot-chord example; the two citation defects and the two bare numerals on page 8; the fourth column in
the monophonic listing; and the seventh-chord listing being identical, line for line, to the
MIDI-to-WAV cadence listing.

**Met only by the first read**, and confirmed at the paper here: the document **calls itself a report**
— page 7, *"that is beyond the scope of this report"* — which strengthens §1's identity observation and
is adopted into the record by this sentence rather than by editing §1.

**The first extract also carries claims about the RECORD** — where this paper is cited, what a sealed
first-stage draft attributes to it, which design points it bears on, and what an L2 detail
specification could adopt or must argue against. **This side ran no repository sweep and checked none
of that half.** Those claims are neither confirmed nor contradicted here; §1 already declares that this
extract asserts nothing about what the record says.

### 9.7 What the cross-check did not do

It re-opened no source of either extract, ran no web access, swept no repository, and **edited no file
other than this one**. It moved no verdict, routed nothing, and amended neither the findings surface
nor the progress record. **The progress record's *Second pass* cells for rows 27 and 28 both still read
OWED**, and flipping them is a later act.

---

## §10 — The user-ordered fact- and source-check, run AFTER this extract had already landed

**The user's standing rule of 2026-09-12** extends the pre-landing check to landed work on four axes:
**completeness, coherence, correctness, and the misuse of hyperbole and absolutes.** He ordered it on
this sitting's writing. **This extract was re-read WHOLE as landed at 68,246 bytes**, at the device's
own copy staged back rather than at this side's container copy, and was re-swept.

**What it found, every item corrected at its own site with the former wording preserved (#12):**

**Correctness**

- **A quotation cited to the wrong page.** *"how good a chord fits within a scale"* was cited to page 8
  in §3.4; it is printed on **page 12**. Page 8 carries a different sentence, which now stands in its
  place. **This is the defect class the whole page-citation discipline exists against**, and it
  survived both the read-back and the first sweep.
- **A contradiction this side manufactured and the paper does not carry.** §5.3's third note set the
  pivot-chord sentence against *"To accomplish a more difficult modulation the highlighted chords are
  non-diatonic"* and declared that **"Both cannot hold of sequence 3 at once"**. That sentence is
  conditioned on *a more difficult modulation* and says nothing about sequence 3, which the next
  sentence offers as the easy case. **Withdrawn.** What survives is the Figure 2 tension alone, which
  stands on its own evidence.
- **Two section headers with wrong page ranges** — §4.2 named page 22, which it does not use, and
  omitted pages 21 and 23, which it cites; §4.3 began at page 2 where its first bullet rests on page 1.

**Coherence**

- **An internal contradiction two paragraphs wide.** §9.1 opened *"Every value both extracts
  transcribed agreed, digit for digit"*, and §9.2's own heading is *"The one value disagreement"*.
  Narrowed to **numeric** value, with the non-numeric disagreement named at the same place.
- **A disclaimer stretched over a table it does not cover.** §9.1 put Table 4 inside the first
  extract's own *"the individual cells of the two tables"* sentence, which covers Tables 1 and 2 only.

**Absolutes and hyperbole**

- ***"the strongest thing the doubling produced here"*** (§9.4) — a superlative over this side's own
  acts, derived from nothing. Struck.
- ***"the paper's only non-synthesised music apart from the MIREX fragments"*** (§5.5) — credited the
  paper with a statement about the MIREX material that it never makes. Narrowed to what the paper does
  state, with the gap declared.
- ***"the cosine of equation (16)"*** (§5.7) and ***"which the discussion later calls the cosine
  distance"*** (§3.6) — two places where this side's identification of an unnumbered phrase with a
  numbered equation was written as the paper's own statement. Both now stated as this extract's
  reading.
- ***"the four internal defects it records"*** (§8.3) — a count made wrong by this very check. The
  members are named instead, and the two new records are among them.

**Completeness**

- **Two bare numerals on page 8** — the *1* and *2* closing the two clauses of the approximation-switch
  sentence — were not recorded at all. They sit where reference markers sit, and **[1]** and **[2]** are
  not Lerdahl. Now recorded in §7 with both readings and no verdict.

**What this check did NOT do.** It did not re-open the paper — no page image was fetched for it, and
every correction above was settled either at text already quoted in this extract or, for the page-8
and page-12 sentences, at the page images this sitting had already read and which the extract quotes
at both ends. It opened no source of either extract, ran no web access, swept no repository, and
**edited no file but this one — the first extract is still untouched.** It moved no verdict, routed
nothing, and changed no transcribed value: **every table, listing, constant and percentage in §3 and §5
stands exactly as it was landed.**

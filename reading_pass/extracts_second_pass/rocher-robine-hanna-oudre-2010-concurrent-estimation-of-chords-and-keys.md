# Second extraction — row 27: Rocher, Robine, Hanna & Oudre 2010, concurrent estimation of chords and keys from audio

> **STATUS: SECOND INDEPENDENT EXTRACTION.** Written 2026-09-13 by the Cowork session that booted on
> `cowork_handoff_entry_one_hundred_and_sixty_eight.md`, under the original commission's §4 fourth
> bullet — *"CENTRAL sources … are extracted in a SECOND independent pass (a fresh session, or a
> cleanly separated re-read that does not consult the first extract) and the two extracts
> cross-checked; disagreements are resolved at the paper or recorded as unresolved."* This is the
> second of the two routes that bullet names.
>
> **THE INDEPENDENCE BOUND, DECLARED RATHER THAN CLAIMED.** The first extract
> (`reading_pass/extracts/rocher-robine-hanna-oudre-2010-concurrent-estimation-of-chords-and-keys.md`)
> was NOT opened by this side at any point, before or during this writing. What this side HAD met
> before reading the paper is the progress record's own table row for row 27
> (`reading_pass/l2_slice_reading_progress.md`), which states the row's grade, its extract's path and
> its CENTRAL verdict, and carries no account of the paper's content beyond the grade cell's words
> *"AT THE OBJECT, whole, pp. 141–146"*. **So this extract is independent of the first extract and
> not of the fact that the first pass graded the paper CENTRAL.** It is not a clean blind read and is
> not offered as one.
>
> **The cross-check the commission requires is NOT performed here.** It is a separate act, taken after
> this file lands, so that opening the first extract cannot reach back into this one.
>
> **The read.** The held file `docs/research_papers/rocher_robine_hanna_oudre_2010_ismir_concurrent_chords_keys.pdf`
> (1,168,137 bytes at this session's staging result), read WHOLE — all 6 pages, in one call, every page
> image confirmed present rather than the call's success line trusted (the page-image fault the
> hundred-and-sixty-eighth entry records). The page count was established at the tool by a request for
> page 40 that returned an out-of-range error naming 6.

---

## 1. Identity, at the object

Printed on page 1, with the venue running head on all six pages:

- **Title**: *"CONCURRENT ESTIMATION OF CHORDS AND KEYS FROM AUDIO"* (printed in capitals).
- **Authors**: **Thomas Rocher, Matthias Robine, Pierre Hanna** (LaBRI, University of Bordeaux, 351
  cours de la Libration, 33405 Talence Cedex, France) and **Laurent Oudre** (Institut TELECOM,
  TELECOM ParisTech, 37-39 rue Dareau, 75014 Paris, France). **Four authors, two institutions.**
- **Venue**: *"11th International Society for Music Information Retrieval Conference (ISMIR 2010)"*,
  the running head of every page.
- **Pagination**: 141–146, printed at the foot of each page.
- **Rights**: the classic permission box — *"Permission to make digital or hard copies of all or part
  of this work for personal or classroom use is granted without fee provided that copies are not made
  or distributed for profit or commercial advantage and that copies bear this notice and the full
  citation on the first page."* — and *"© 2010 International Society for Music Information
  Retrieval."*

**Against the bibliography's row 41** (`Rocher, Robine, Hanna & Oudre, "Concurrent Estimation of
Chords and Keys from Audio," ISMIR 2010`, URL `laurentoudre.fr/publis/RRHO-ISMIR-10.pdf`, tier **LINK
(author copy)**): the four authors in the row's own order, the title in full, the venue and the year
all match at page 1, and the row carries no pagination where 141–146 is established here.

**★ NO open licence of any kind was met on any of the six pages as read** (a reader's negative over
page images). The permission box is a personal-and-classroom-use grant with a no-commercial clause,
which is not a Creative Commons licence, so **the LINK tier is the correct conservative reading and no
tier correction is owed**; the copy stays private and nothing of it is redistributed.

**★ One identity gap, recorded and not graded.** The row's tier calls the file an *author copy* and
its URL is the fourth author's own site, while the held file presents as the **proceedings text** —
the ISMIR running head and continuous pagination on every page. Whether the author-site file is
byte-identical to the proceedings text is not establishable from what is held.

---

## 2. Coupling facts — mandatory (the user's ruled widening)

### What the method ASSUMES about its upstream

- **The input is AUDIO** — established at the abstract, §2.1 and §3.1: an audio file at 44,100 Hz,
  represented as sequences of chroma vectors.
- **Nothing symbolic is met as a required or consumed input**: no notes, no spelling, no note letter, no
  meter, no bar lines, no voices, no key signature, no onsets and no durations are met as inputs on
  any of the six pages as read.
- **No training data.** §1, in the authors' own words: *"The proposed method is both template-based
  and music-based and no training is required."* The chord templates, the key profiles and the
  transition cost are all fixed in advance.
- **A frame grid is imposed, not discovered**: the audio is divided into frames of approximately
  100 ms (4,096 audio samples) for evaluation (§3.2), and the chromagrams carry their own window and
  hop sizes (§3.3).
- **Ground-truth annotations are required for evaluation only**, not by the method.

### What it HANDS downstream

- **One pair per frame: (chord, local key).** The chord is drawn from **24 major and minor triads**
  (§2.2.1, *"The chords studied here are major and minor triads (12 major and 12 minors)"*); the
  tonality from **24 major and minor keys** (§2.2.2).
- **What is NOT decided, established by reading the method and the label spaces rather than by any
  statement of absence in the paper**: no seventh or extended chord type, no inversion, no bass, no
  Roman numeral, no scale degree, no functional label, no segmentation (the grid is fixed), no
  chord-tone assignment, no non-chord-tone decision, and no chord/no-chord distinction.
- **A single best path is outputted, with no alternatives and no confidence.** §2.4: *"The final
  selected path is the path minimizing its total cost along its edges. This path is outputted by the
  program."* No ranked carry, no per-frame mass and no uncertainty value is met anywhere in the six
  pages as read.
- **The output is then edited by a post-smoothing pass** (§2.5, §3.3.4) before it is reported, so what
  the system publishes is not the decoded path itself.

### Its own STATED SCOPE and limits, in the paper's words

- **Silence and no-chord are excluded**: §3.2 — *"Silences and no-chords (part of a song when no chord
  is defined) are ignored, as the chord/no-chord detection issue has not yet been addressed in the
  proposed system."*
- **The ground truth is degraded to the system's label space**: §3.2 — *"All the ground truth chords of
  the database have thus been mapped to min/maj triads. When the chord has no third and cannot be
  mapped to a min/maj triad, only the root note is considered."*
- **Future work names the gaps** (§4): *"analysis of different chord types, silence and no-chord
  detection as well weighing the harmonic graph of the proposed method in a probabilistic approach."*
  So the authors themselves place the extended chord vocabulary, the no-chord decision and any
  probabilistic reading of the graph outside what is delivered.

---

## 3. The method, in the paper's own structure

**§2, four steps plus one** (§2, with Figure 1's four panels): chroma vectors computed from the audio;
a set of harmonic candidates selected per frame (Fig. 1(a)); a weighted acyclic graph built over them
(Fig. 1(b)); a dynamic process selecting one incoming edge per candidate (Fig. 1(c)) and the best
whole path outputted (Fig. 1(d)); then a post-filtering step over the outputted sequence.

**§2.1 Chroma.** Computed per frame. Tuning is handled **without a tuning analysis**: chroma is
computed on **36 bins** and shifted per frame according to possible tuning variation, so that two
chords played at different tunings give different 36-bin chromas but almost the same 12-bin chroma
(the authors credit [5], Gómez's thesis). The stated reason for avoiding tuning analysis is that
*"tuning analysis assumes a stationarity"*. **Multi-scale**: a set of chromagrams rather than one, each
with its own parameters but all sharing a common multiple hop size so information at the same instants
can be combined — *"Longer chromas may bring out information for key analysis, and different set of
sizes for shorter chromas may fit different tempos and carry out different information useful for
chord identification."* **Filter**: median filtering across several
frames, against noise, transients and sharp edges.

**§2.2 Candidates.** A harmonic candidate is a pair (C_i, K_i). Chord templates are the two
triad profiles rotated to all 24; the correlation is a plain scalar product, C_{T,V} = Σ_{i=1..12}
T[i]·V[i]. Key profiles are taken from [18] (Temperley, *The Cognition of Basic Musical Structures*,
1999) and printed as **Major = (5, 2, 3.5, 2, 4.5, 4, 2, 4.5, 2, 3.5, 1.5, 4)** and **Minor = (5, 2,
3.5, 4.5, 2, 4, 2, 4.5, 3.5, 2, 1.5, 4)**; keys are correlated over a larger time frame than chords
*"as keys have a larger time persistence than chords"*. The candidate set is the **full cross product**
— n chords × m keys.

**★ A tried-and-rejected alternative is recorded in the paper itself** (§2.2.3): constraining the
cross product to *compatible* chord/key pairs was tried and *"has led to a decrease of accuracy"*,
because *"an incorrect chord selected may discard the correct key (and vice versa), because the two
are not compatible."* **No value is printed for that decrease.**

**§2.3 The graph and its cost.** Every candidate of one frame is joined to every candidate of the next.
The edge cost is **Lerdahl's distance** [11], defined in the paper as δ(x → y) = i + j + k, where i is
the distance between the two keys on the circle of fifths, j the distance between the two chords on the
circle of fifths, and **k the number of non-common pitch classes in the basic space of y compared to
those in the basic space of x**.

> **★ CORRECTED 2026-09-13 AT THE CROSS-CHECK, AND THE ERROR WAS THIS EXTRACT'S OWN.** *(FORMER
> WORDING, PRESERVED (#12): "k the number of non-common pitch classes in the basic space of x compared
> with those of y".)* **The direction of the comparison was reversed.** Printed page 143, right column:
> *"k is the number of non-common pitch classes in the basic space of y compared to those in the basic
> space of x"*. The first extract carries the direction correctly and this one did not; the
> disagreement was resolved at the page, against this file. Recorded at §9.

The paper notes the resulting integer cost runs **0 to 13** and states its own objection:
*"this distance offers a small range of possible values. As we need to compare different paths between
harmonic candidates, this small range induces a lot of equality scenarios."* The cost is therefore
**modified to i^α + j^β + k**, with **α = 1.1 and β = 1.01** — *"After experiment, α and β have been
set to 1.1 and 1.01."* α > 1 and
β > 1 are chosen *"to discourage immediate transitions between distant keys, and encourage progressive
key changes"*.

**§2.4 Best path.** Dynamic programming [1]. Left to right, one incoming edge is kept per candidate —
the one minimizing the total cost of the path reaching it. The number of final paths equals the number
of candidates in the last frame, and the reported path is the cheapest of those.

**§2.5 Post-smoothing.** A pattern rewrite over the outputted chord sequence. The worked reason given is
a blue note: a flattened third sounded against a major chord can make one frame read minor between runs
of major. §3.3.4 states the rewrite: sequences of the form *…AABAA…* (respectively *…AAABCAAA…*) are
corrected to *…AAAAA…* (respectively *…AAAAAAAA…*).

---

## 4. What it reports — the values as the paper states them

*(No claim is made that this section carries every number the paper prints; no enumeration of the
paper's numbers was run against it.)*

**The corpus** (§3.1): the **Beatles audio discography, 174 songs**, at 44,100 Hz. Stated corpus
properties: average **69 chord changes** per song; average **7.7 different chords** per song; **average
number of different local keys per song 1.69**. Chord transcriptions checked by Christopher Harte and
the MIR community; key annotations from the Centre for Digital Music (C4DM); both at
`http://www.isophonics.net`.

**The evaluation** (§3.2): frames of approximately 100 ms; the estimated chord compared to the ground
truth at the time corresponding to the **center** of the frame; a song's score is matching frames over
frames analyzed; the local-key procedure is identical. The other components follow the **2009 MIREX
audio chord detection task**.

**Chroma sizes** (§3.3): *long* — 32,768 samples window (≈0.8 s), 8,192 hop (≈0.2 s); *medium* — 8,192
window (≈0.2 s), 8,192 hop (≈0.2 s); *short* — 4,096 window (≈0.1 s), 4,096 hop (≈0.1 s).

### Table 1 — filtering and the number of chord candidates (long chromas)

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **No filtering** — ratio of correct. (%) | 58.3 | 71.5 | 78.6 | 82.9 |
| **No filtering** — system (%) | 58.3 | **64.9** | 64.1 | 62.2 |
| **Filtering** — ratio of correct. (%) | 68.4 | 79.1 | 85.5 | 88.9 |
| **Filtering** — system (%) | 68.4 | **70.0** | 64.3 | 59.3 |

The *ratio of correctness* is defined in §3.3.1 as the number of frames for which the correct chord is
among the selected candidates, over the total number of frames — *"This ratio represents the system
theoretical maximum accuracy, and is reached if every correct chord candidate is present in the final
chord sequence outputted."* Best filtering is a window of **9 chromas** centered on the chroma
considered.

### Table 2 — the multi-scale combinations

**Tri-candidate (1 long and 2 short chromas)**

| Filtering | none | long | short | both |
|---|---|---|---|---|
| Ratio of correct. (%) | 69.8 | 78.2 | 76.6 | 79.1 |
| Distinct chords (av.) | 1.86 | 1.95 | 1.43 | 1.36 |
| System (%) | 64.5 | 72.2 | 71.8 | **73.7** |

**Bi-candidate (1 long and 1 medium chromas)**

| Filtering | none | long | medium | both |
|---|---|---|---|---|
| Ratio of correct. (%) | 65.1 | 75.1 | 73.5 | 76.7 |
| Distinct chords (av.) | 1.38 | 1.46 | 1.29 | 1.23 |
| System (%) | 62.8 | 71.6 | 70.7 | **72.8** |

**Post-smoothing** (§3.3.4): applied to the 73.7 % tri-candidate configuration, *"chord detection
reaches a **74.9%** accuracy."*

### Table 3 — against a state-of-the-art method

| Method | Root | Root and Mode |
|---|---|---|
| OGF2 (%) | **78.9** | 72.3 |
| Proposed System (%) | 77.9 | **74.9** |

Caption: OGF2 *"scored 1st (resp 2nd) in the 2009 MIREX Audio Chord Detection "root estimation" task
(resp. root and mode task)"*. The text states the direction in both places: *"On the root estimation
only, OGF2 is 1% more accurate than the proposed method (78.9% compared to 77.9%). On the root and mode
estimation, the proposed system performs better … (74.9% compared to 72.3%)."*

### Table 4 — local key against a direct template-based method

| Key estimation | Correct | Rel. | Nei. | Oth. |
|---|---|---|---|---|
| System (%) | **62.4** | 2.9 | 17.4 | 17.3 |
| DTBM (%) | 57.6 | 1.6 | 18.9 | 21.9 |

Window size approximately **30 s**; **3 key candidates per frame** for the proposed method. *Relative*
keys share a key signature; a *neighbor* key differs by one accidental, each key having two.

### Table 5 — the reciprocal benefit of estimating both together

| Harmonic candidate | Chord only | Key only | Both |
|---|---|---|---|
| System (%) | 73.1 | 57.8 | **74.9** (chord), **62.4** (key) |

Text: *"Chord estimation accuracy drops of almost 2% (74.9 compared to 73.1) and key estimation
accuracy drops of almost 5% (62.4 compared to 57.8)."* When only chord (respectively key) candidates
are used, the edge cost is edited to take only that half into account.

---

## 5. Claims, labeled

**FACT** (stated or measured in the paper, with its location):

- **F1.** Estimating the chord and the local key **together** measures better on both axes than
  estimating either alone, on this corpus and this system: chord 74.9 against 73.1, key 62.4 against
  57.8 (Table 5, §3.5).
- **F2.** On **root and mode** together the system measures 74.9 % against the OGF2 comparison method's
  72.3 %; on **root alone** it measures 77.9 % against OGF2's 78.9 % (Table 3, §3.3.5).
- **F3.** Raising the number of chord candidates per frame raises the theoretical ceiling monotonically
  (68.4 → 79.1 → 85.5 → 88.9 with filtering) while the achieved accuracy **peaks at two candidates and
  then falls** (68.4 → 70.0 → 64.3 → 59.3) (Table 1, §3.3.1–§3.3.2).
- **F4.** *"In 80% of the frames, top 2 correlated chord candidate have a distance less or equal to 1
  on the circle of fifths"* (§3.3.2) — a measured statement about how alike the leading candidates are.
- **F5.** Median filtering of the chromagram raises the ratio of correctness by about 6 % at four
  candidates (82.9 → 88.9) and by more than 10 % at one (58.3 → 68.4) (§3.3.1).
- **F6.** Drawing the candidates from **differently sized** chromagrams rather than several from one
  chromagram narrows the gap between the ceiling and the achieved accuracy: 5.4 points (79.1 − 73.7)
  tri-candidate and 2.9 points (76.7 − 72.8) bi-candidate, against more than 9 points (79.1 − 70.0)
  for two candidates from one long chromagram (§3.3.3, reading Tables 1 and 2 together as the paper
  does).
- **F7.** The average number of different local keys per song in this corpus is **1.69** (§3.1).
- **F8.** Constraining the chord/key cross product to compatible pairs **lowered** accuracy (§2.2.3).
  **No value is given**, so this is a stated outcome without a measurement attached.

**THEORY** (established published theory the paper adopts rather than establishes):

- **T1.** **Lerdahl's tonal pitch space** and its chord/key distance [11], adopted as the transition
  cost and cited, not re-derived.
- **T2.** **Temperley's key profiles** [18], adopted verbatim as the key templates.
- **T3.** The **chroma / pitch-class profile** as an octave-independent tonal representation, credited
  to [5].
- **T4.** **Dynamic programming** over an acyclic graph as the path-finding method [1].

**CONJECTURE** (asserted in the paper without measurement in it):

- **C1.** That *"chords bring out information about local key and vice versa"* is offered in §1 as the
  contribution's motivation. Table 5 measures the **outcome** of joint estimation; the causal reading
  is the authors' interpretation of it.
- **C2.** That α = 1.1 and β = 1.01 *"discourage immediate transitions between distant keys, and
  encourage progressive key changes"*. The exponents are stated to be set *"after experiment"*, and no
  measurement of that behavioral effect is printed.
- **C3.** The explanation offered for why more candidates hurt — the closeness of the leading
  candidates — is supported by F4 but not tested against the alternative that the cost function
  discriminates poorly among near candidates.
- **C4.** §4's suggestion that *"harmonic information may be helpful for estimating the musical
  structure of pieces since changes of local key generally occur at the beginning of new patterns"* is
  stated with nothing measured behind it in this paper.

---

## 6. What the read did NOT do, and the bounds on every negative here

- **The first extract was not opened**, so nothing here is checked against it and no agreement or
  disagreement with it is asserted.
- **No sweep of the repository was run for this paper** — not for its name, not for its
  characterisation, not for any of its printed values. **So this extract makes NO claim about whether
  the record cites this paper, rests on it, or reports any of its numbers.** Every such question is
  open here and belongs to the cross-check.
- **`FRAMEWORK.md` was not opened by this side at all this sitting**, and no design point was read. So
  nothing here states what any design point takes from this paper.
- **No cited work was fetched.** The eighteen reference-list entries are recorded at §7 below as
  printed, and no claim of any of them is carried out of this paper.
- **No web access of any kind was made.** The `isophonics.net` corpus, the MIREX 2009 results page the
  footnote names, and the author-site URL the bibliography row carries were not visited.
- Negatives in this file about the paper's own contents are written as **reader's negatives over the
  six pages as read** — *met nowhere in the six pages as read* — rather than as claims that the paper
  prints no such thing. That is the standard this side wrote to; it is not a verified property of
  every sentence here, no enumeration of this file's own negatives having been run, and a later
  reader who finds one stated wider than the act should read it at the narrower strength.

---

## 7. The reference list, as printed at §5

Eighteen entries. Recorded in full because three of them are members of this project's own reading
population and one is the comparison method's own paper.

1. R. Bellman. *Dynamic Programming*. Princeton University Press, 1957.
2. J.P. Bello and J. Pickens. A robust mid-level representation for harmonic content in music signals. ISMIR 2005, pp. 304–311, London.
3. W. Chai and B. Vercoe. Detection of key change in classical piano music. ISMIR 2005, pp. 468–473, London.
4. J. Stephen Downie. The music information retrieval evaluation exchange (2005–2007). *Acoustical Science and Technology*, 29(4):247–255, 2008.
5. E. Gómez. *Tonal Description of Music Audio Signals*. PhD thesis, University Pompeu Fabra, Barcelona, July 2006.
6. C. Harte and M. Sandler. Automatic chord identification using a quantised chromagram. AES, Barcelona, 2005.
7. C. Harte, M. Sandler, S. Abdallah, A. Samer. Symbolic representation of musical chords: A proposed syntax for text annotations. ISMIR 2005, pp. 66–71.
8. O. Izmirli. Audio key finding using low-dimensional spaces. ISMIR 2006, pp. 127–132, Victoria.
9. K. Lee. Automatic chord recognition from audio using enhanced pitch class profile. ISMIR 2006, Victoria.
10. K. Lee and M. Slaney. Acoustic chord transcription and key extraction from audio using key-dependent HMMs trained on synthesized audio. *IEEE Trans. on Audio, Speech and Language Processing*, 16(2):291–301, 2008.
11. F. Lerdahl. *Tonal Pitch Space*. Oxford University Press, 2001.
12. M. Mauch and S. Dixon. Simultaneous estimation of chords and musical context from audio. *IEEE Trans. on Audio, Speech and Language Processing*, 2010.
13. K. Noland and M. Sandler. Key estimation using a hidden markov model. ISMIR 2006, pp. 121–126, Victoria.
14. L. Oudre, Y. Grenier, and C. Févotte. Template-based chord recognition: influence of the chord types. ISMIR 2009, pp. 153–158, Kobe.
15. H. Papadopoulos and G. Peeters. Large-scale study of chord estimation algorithms based on chroma representation and HMM. CBMI 2007, pp. 53–60, Bordeaux.
16. M.P. Ryynänen and A.P. Klapuri. Automatic transcription of melody, bass line, and chords in polyphonic music. *Computer Music Journal*, 32(3):72–86, 2008.
17. A. Sheh and D.P.W. Ellis. Chord segmentation and recognition using EM-trained hidden Markov models. ISMIR 2003, pp. 185–191, Baltimore.
18. D. Temperley. *The Cognition of Basic Musical Structures*. The MIT Press, 1999.

**Three of these are held rows of this project's own reading population**, matched by author, title and
venue as printed here: **[13] Noland & Sandler 2006** is row 26; **[17] Sheh & Ellis 2003** is row 18;
**[12] Mauch & Dixon** is held under `mauch_dixon_2010_approximate_note_transcription.pdf`, whose title
as filed differs from the title printed here, so that identification is **NOT asserted** and is left
for the cross-check.

**★ [14] Oudre, Grenier & Févotte is the OGF2 comparison method of Table 3, and Laurent Oudre is the
fourth author of this paper.** Recorded as a fact about the comparison, with no verdict attached: the
state-of-the-art method the paper measures itself against is one of its own authors' prior systems, and
the paper does not remark on that.

---

## 8. What the whole reading and the absolutes sweep found — written after both ran

**This section was absent when the sections above were written.** It was added by a separate edit after
this file had been read whole against the six pages and swept for absolutes, which is the order the
handoff entry's cadence 9 requires. Six items about the paper, three about this file's own writing.

### About the paper

**(1) THE ABSTRACT'S CLAIM IS WIDER THAN THE MEASUREMENT, AND IT IS WIDER ON EXACTLY THE AXIS THIS
PROJECT GOVERNS BY.** The abstract states *"Results show that it performs better than state-of-the art
chord analysis algorithms while providing a more complete harmonic analysis."* Table 3 measures the
comparison on two axes and the sign differs between them: on **root and mode** the system is ahead
(74.9 against 72.3), on **root alone** it is **behind** (77.9 against 78.9). The body says so plainly in
both directions; the abstract carries only the favourable half. **Recorded here because this project's
own hard regression stop is root-governed, so the axis on which this paper loses is the axis the
project's own measurement is decided on.** No verdict is attached and no design point is named — this
side opened no ratified text this sitting.

**(2) TABLE 5's JOINT-BENEFIT MARGIN MAY BE PARTLY THE POST-SMOOTHING, AND THE PAPER DOES NOT SAY.**
The *both* cell for chord reads **74.9**, which §3.3.4 establishes is the **post-smoothed** figure
(post-smoothing takes 73.7 to 74.9). The *chord only* cell reads **73.1**, and **whether that
configuration was post-smoothed is stated nowhere in the six pages as read.** If it was not, the
like-for-like comparison is 73.7 against 73.1 — **0.6 of a percentage point, not the *"almost 2%"* the
text claims.** If it was, the text's figure stands. **The paper does not settle which**, so the size of
the chord-side reciprocal benefit is not established at the object. The key-side comparison (62.4
against 57.8) carries no such ambiguity, post-smoothing being described as a treatment of the chord
sequence.

**(3) THE PAPER CARRIES AN UN-DE-ANONYMISED SELF-REFERENCE.** §2 opens: the method *"is adapted for
audio from the proposed system in [anonymous self-reference]"*. The review-time placeholder survived
into the printed text, so **the earlier system this one is adapted from cannot be identified from the
paper**, and it is absent from the eighteen-entry reference list. Anything that would follow from
knowing what the predecessor did — in particular whether it was symbolic — is unavailable here.

**(4) NO UNCERTAINTY OF ANY KIND, AND THE PARAMETERS WERE CHOSEN ON THE CORPUS THE RESULTS ARE
REPORTED ON.** No spread, no confidence range, no significance test and **no held-out split** was met
anywhere in the six pages as read. **No repetition, averaging over runs or resampling is described
anywhere in the six pages as read**, so the values of Tables 1 to 5 read as single runs over the same
174-song set; *that they ARE single runs is the reader's inference from that silence and is not stated
by the paper.* Several quantities are explicitly selected by comparison on that same set: the number of chord
candidates (Table 1), the filtering window of 9 chromas (§3.3.1), the multi-scale combination
(Table 2), and the exponents α and β, which §2.3 says were *"set after experiment"*. **So the reported
accuracies are fitted-and-self-measured in the sense principle #20 names**, and the paper states no
protection against it.

**(5) THE COVERAGE DENOMINATOR IS NOT PUBLISHED.** §3.2 excludes silences and no-chords from the
evaluation, and **the fraction of the corpus that removes is stated nowhere in the six pages as read.**
Every percentage in the paper is therefore over a denominator whose size the reader cannot recover.

**(6) THE LOCAL-KEY RESULT HAS NO TRIVIAL BASELINE BESIDE IT, AND THE CORPUS SUGGESTS ONE WOULD BE
HIGH.** §3.1 gives the average number of different local keys per song as **1.69**, so a large share of
each song is spent in one tonality. Table 4 compares the system to a direct template-based method and
to nothing else; **no always-predict-the-global-key baseline is reported**, and none is computable from
what the paper prints. The 62.4 % is therefore not readable as a measure of how well local key *change*
is tracked — which is what the paper's own contribution claim is about.

### About this file's own writing

**(7) THREE QUOTATION DEFECTS, FOUND BY THE READING AND CORRECTED AT THEIR SITES.** The multi-scale
quotation at §3 and the ratio-of-correctness quotation at §4 were each **truncated mid-sentence with no
ellipsis**, so both read as complete quotations of the paper and were not; both now carry the printed
sentence in full. The α/β clause carried *"set after experiment"* **inside quotation marks**, which is
this side's paraphrase and not the paper's words; the printed sentence — *"After experiment, α and β
have been set to 1.1 and 1.01."* — replaces it. **A paraphrase inside quotation marks is the worse of
the three**, because a later reader has no way to see that it is one.

**(8) THREE ABSOLUTES STRUCK BY THE SWEEP, EACH OVERREACHING THIS SIDE'S OWN ACT.** *"Nothing symbolic
is required or consumed anywhere"* asserted a property of the method beyond the pages read, and now
reads *met as a required or consumed input*. The §4 heading read *"every value as the paper states
it"*, claiming a completeness no enumeration of the paper's numbers established; it now disclaims that
in terms. And §6 read *"Every negative in this file … is a reader's negative"*, which is a verified
property of this file that was never verified; it now states the standard written to rather than a
property achieved.

**(9) WHAT THE SWEEP READ AND LEFT STANDING**, so a later reader knows what was judged rather than
missed: *"all six pages"* and *"all 6 pages"*, both derived at the tool and at the images; *"NO open
licence of any kind was met on any of the six pages as read"*, already at the reader's strength;
*"the ISMIR running head and continuous pagination on every page"*, derived by looking at each page;
*"Every candidate of one frame is joined to every candidate of the next"* and *"rotated to all 24"*,
both the paper's own statements of its method; and *"`FRAMEWORK.md` was not opened by this side at all
this sitting"*, which is a statement about this side's own calls and is true of them.

---

## 9. The cross-check against the first extract — written in the act that ran it

**This section was written after §1 to §8 had landed** at 30,227 bytes, proved at content in both
directions and at size. The first extract was opened only then, so nothing it says reached back into
the sections above. This is the second half of the original commission's §4 fourth bullet — *"and the
two extracts cross-checked; disagreements are resolved at the paper or recorded as unresolved."*

### What agrees

**Every value that BOTH reads transcribed agrees between them.** *(★ CORRECTED 2026-09-13 at the
user-ordered check. FORMER WORDING, PRESERVED (#12): "Every value transcribed from the paper agrees
between the two reads." That claimed agreement over values only one extract carries — the first prints
the major-triad profile's digits, which this one describes without printing — so the comparison could
not have reached them.)* All sixteen cells of Table 1;
both blocks of Table 2, including the average-distinct-chord rows; Tables 3, 4 and 5 entire; the corpus
figures (174 songs, 69 chord changes, 7.7 chords, 1.69 local keys); both key profiles digit for digit;
the three chroma window and hop sizes; the 0-to-13 cost range; α = 1.1 and β = 1.01; the 80 %
circle-of-fifths statement; the 9-chroma filter window; the ≈30 s key window and 3 key candidates; the
100 ms / 4,096-sample frame; and the 73.7 → 74.9 post-smoothing movement. **Two independent
transcriptions of this paper's numbers agree at every cell either of them carries.** That is the one
thing the doubling exists to establish, and it holds here.

The two reads also agree, independently, on the substance of the corpus caveat: both note that 1.69
local keys per song makes the local-key task on this corpus close to a global-key task.

### What disagrees, each resolved at the page

**(a) THE DIRECTION OF LERDAHL'S k TERM — RESOLVED AGAINST THIS EXTRACT.** The first extract reads
*"the basic space of y compared to those in the basic space of x"*; this extract had written *x
compared with those of y*. Printed page 143, right column, carries the first extract's direction.
**This extract was wrong and is corrected at its site in §3**, the former wording preserved. **This is
the substantive find of the cross-check, and it is a defect of the second read, not the first.**

**(b) AN INSERTED WORD INSIDE A QUOTATION IN THE FIRST EXTRACT.** It quotes §2.1.2 as *"Longer chromas
may bring out different information for key analysis…"*. Printed page 142 reads *"Longer chromas may
bring out information for key analysis"* — **without *different***. The word appears in the preceding
sentence of the paper (*"These chromagrams bring out different kinds of information"*), which is the
likely source of the slip. Resolved at the page against the first extract.

**(c) A PLURAL FOR A SINGULAR INSIDE A QUOTATION IN THE FIRST EXTRACT.** It quotes *"but with larger
time frames as keys have a larger time persistence than chords"*. Printed page 143, §2.2.2, reads
*"but with larger time frame"* — singular. Resolved at the page against the first extract.

**No disagreement found by this comparison is left unresolved**, and (b) and (c) are quotation defects
rather than defects of fact, neither moving any value or any verdict. **That is not a claim that the
comparison was exhaustive:** it ran over what the two extracts both carry, and a later reader may find
more.

**★ THE FIRST EXTRACT IS NOT AMENDED BY THIS ACT.** Its two quotation defects are recorded here and
left standing in their own file, because rewriting another read's text would destroy the record of what
that read actually said, which is the thing the doubling is comparing. **Whether they are corrected at
their own site is not this side's call and is put to the user.**

### What the second read adds that the first does not carry

None of these contradicts the first extract; each is a bound or a fact it does not record.

- **The abstract is wider than the measurement on the root axis** (§8(1)). The first extract records
  Table 3's values correctly, including that OGF2 leads on root, but does not remark that the
  abstract's *"performs better than state-of-the art chord analysis algorithms"* holds on root-and-mode
  and not on root.
- **Table 5's chord margin may be partly the post-smoothing** (§8(2)). The first extract computes the
  differences as *"1.8 and 4.6 points"* — arithmetically right — but compares a post-smoothed 74.9
  against a 73.1 whose smoothing status the paper does not state. **This bears directly on the first
  extract's own finding (1)**, which carries 1.8 and 4.6 as a precision on a ratified item.
- **The un-de-anonymised self-reference at §2** (§8(3)), absent from the first extract.
- **The fit-and-self-measure point** (§8(4)). The first extract lists the same tuned quantities under
  its scope section; it does not draw the consequence that they were selected on the corpus the results
  are reported on, with no held-out split anywhere.
- **The coverage denominator is unpublished** (§8(5)). The first extract records that silences and
  no-chords are ignored; neither read can recover what fraction that removes.
- **No always-predict-the-global-key baseline is reported** (§8(6)) — the sharpening of the caveat both
  reads reached.
- **The comparison method OGF2 is by a co-author of this paper** (§7). The first extract names *"OGF2
  (Oudre et al.)"* without remarking that Laurent Oudre is its fourth author.

### What the first extract carries that this read did not reach

Everything measured against this project's own record: its findings (1), (2), (3) and (5) check the
paper against `FRAMEWORK.md` §5 and §9, Appendix B, the findings surface's V2 and V7, and DP-B's
ground. **This side opened no ratified text this sitting**, so none of that is checked here, none of it
is contradicted here, and the cross-check reaches none of it. A reader wanting the against-the-record
half reads the first extract; a reader wanting the paper checked twice reads both.

### What this cross-check did NOT do

It did not amend the first extract. It did not open `FRAMEWORK.md`, the findings surface, the slice
derivation or any decisions-register entry, so no claim of the first extract about the record is
verified or disputed. It re-opened the paper at pages 2 and 3 only, to resolve (a), (b) and (c). It ran
no web access. It moved no verdict: **row 27's CENTRAL grade is untouched**, and the flip of the
progress record's *Second pass* cell for row 27 from OWED is **not performed here** — that file carries
a read-whole-before-rewrite rule and is 396,426 bytes, which is its own act.

---

## 10. The user-ordered fact- and source-check, run after §1 to §9 had landed — written in the act that ran it

The user's standing rule of 2026-09-12 extends the pre-landing check to landed work, on four axes:
completeness, coherence, correctness, and misuse of hyperbole and absolutes. **It was run over this
file as landed at 37,019 bytes**, by a targeted search for absolute constructions with every hit read at
its line, **not by a third whole reading** — this file has been read whole once, at §8, and swept twice.
Saying which is part of the record.

**Three corrections, each made at its site with the former wording preserved (#12):**

- **§9 claimed agreement over *"every value transcribed from the paper"*.** The comparison could only
  reach values **both** extracts carry, and they do not carry the same set — the first prints the
  major-triad profile's digits, which this one describes without printing. Corrected to what the act
  established.
- **§8(4) asserted that every value in Tables 1 to 5 *"is a single run"*.** The paper does not say so.
  What is established is the **silence**: no repetition, averaging or resampling is described in the six
  pages as read. The single-run reading is the reader's inference from that silence, and now says so.
- **§9's *"No disagreement is left unresolved"* read as a claim about the two extracts** rather than
  about this comparison, which would assert an exhaustiveness the comparison never had. Now bounded.

**What this check did not do:** it did not re-open the paper, did not re-open the first extract, ran no
web access, and reaches this file's own writing and nothing else.

# Second extraction — Feisthauer, Bigo, Giraud & Levé 2020, "Estimating keys and modulations in musical pieces"

> **What this file is.** The SECOND independent extraction of row 30 of Task B's L2 slice, written
> under `cowork_reading_pass_commission_2026_08_30.md` §4 and its central-source clause, and under
> the eight-step order recorded at the hundred-and-sixty-ninth handoff entry's §3. It is written
> from the paper's own pages, read as page images with the file tools over a bridge-staged copy.
>
> **The first extract of this paper was NOT consulted while §0 to §8 of this file were written.**
> Whatever this file says about the paper is this read's own, right or wrong, and the point of the
> doubling is that the two reads be comparable. The cross-check against the first extract is §9,
> and nothing above §9 was written with that file open.

---

## §0 — What was read, and the bound on this read's independence

**The paper, at the object.** `docs/research_papers/feisthauer_bigo_giraud_leve_2020_smc_keys_modulations.pdf`,
**541,934 bytes**, staged through the bridge by the one matching file name in a non-recursive
listing of `docs/research_papers/`. **The page count was established AT THE TOOL**, by a
deliberately out-of-range page request, which answered *"PDF has 9 pages"*. **All nine pages were
read whole**, in two requests (pages 1–5 and 6–9), and **every image was checked for presence and
legibility at the image itself, not at the call's success line** — the page-image fault the line
records is live and a successful call is not evidence of a delivered image.

**What the nine PDF pages are.** Page 1 is a HAL deposit cover sheet: it carries the title, the four
authors, the citation, the HAL identifier and a licence line, and no part of the article's body. The
paper proper runs on PDF pages 2 to 9, and page 2's own footer gives its
printed pagination: *"Sound and Music Computing Conference (SMC 2020), Torino, 2020, pp. 323–330"* —
**eight printed pages.** Throughout this file a page number is a PDF page number unless it says
*printed*.

**Identity check, made before anything was extracted.** The cover sheet and the article's own head
agree on title, on all four authors and on venue: *Estimating keys and modulations in musical
pieces*; Laurent Feisthauer, Louis Bigo, Mathieu Giraud, Florence Levé; Sound and Music Computing
Conference (SMC 2020), Torino, June 2020. The HAL identifier is `hal-02886399`, version 2,
submitted 9 September 2020. **They match, so there is no identity finding.**

**One disagreement inside the held document, recorded because it is a disagreement and not because
anything turns on it.** The HAL cover sheet states the deposit is *"Distributed under a Creative
Commons CC0 1.0 - Universal - International License"*; the article's own page-2 footer states
*"Creative Commons Attribution 3.0 Unported License"*. **These are two different licences.** This
read takes no position on which governs, and nothing in this file depends on either.

**What else this side read before writing this file, so the independence bound is stated and not
claimed away.** The hundred-and-seventy-second, hundred-and-seventy-first, hundred-and-seventieth
and hundred-and-sixty-ninth handoff entries; `CLAUDE.md` at its six ruled session-start spans;
`DECISIONS.md`; `STATUS.md`; the derived gating answer; the hundred-and-eighteenth entry's
bridge-fault section; the hundred-and-fifty-second entry's lettered departures; both reading-pass
commissions whole.

**The contaminations, named rather than counted or denied:**

1. **`reading_pass/candidacy_upgrades.md` was opened at row 30's own line**, to learn what row 30
   is. That line carries the admission reason: *"A modulation-deciding method on symbolic classical
   music, our own repertoire and input kind."* **So this side knew, before opening the paper, that
   the record classes this as a modulation-deciding method on symbolic classical music.** That is a
   one-line characterisation and not a summary of the paper's content, but it is not nothing.
2. **Row 26's second extract was opened for its SECTION HEADINGS ALONE**, by a heading search, to
   take this line's own section form rather than invent a numbering scheme — which `CLAUDE.md`
   Conventions forbid. **No content line of that file was read**, and that file is about a different
   paper.
3. **`reading_pass/l2_slice_reading_progress.md` was NOT opened at all.** The hundred-and-sixty-ninth
   entry's §3 warns that its verdict cells state each first extract's conclusion and that reading
   them is contamination. **This side did not read them**, so on this member that particular
   contamination did not occur.

**What this side did NOT read, and therefore asserts nothing about.** This paper's first extract —
**not opened before §9**. `FRAMEWORK.md` — at all. `docs/research_papers/BIBLIOGRAPHY.md`.
`reading_pass/population.md`. The slice derivation. The findings surface. Every other extract but
row 26's headings. **No sweep of the repository was run for this paper** — not for its authors, not
for its title, not for any of its values — **so this file asserts nothing whatever about what the
record elsewhere says of this paper**, and the reader must not take silence here for absence there.

**Nothing in `docs/research_papers/polyph9-release/` was opened, staged, listed or searched by this
side.** It appears as a directory name in the one listing of `docs/research_papers/` that located
this paper's file, and that is the whole of this side's contact with it.

---

## §1 — What the paper is

**The problem it takes on.** The paper's own framing, at the close of its §1.2 (PDF page 3), quoted
whole so that neither its subject nor its citation is lost:

> *"These algorithms are fairly accurate when it comes to detecting global keys and possibly long
> term local keys. However, they are not designed to precisely identify **where the modulations
> occur** and what actually makes the modulations, with the notable exception of work by Chew [19]."*

The paper positions itself against that gap: it is about key CHANGE, not about the global key.

*(★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): the sentence was introduced as
"existing symbolic key-finding work" and the quotation then began at "are fairly accurate", which
replaced the printed subject "These algorithms" with a singular paraphrase the verb no longer agreed
with, and it closed at "work by Chew" with the citation "[19]" dropped and no ellipsis. A quotation
must not be trimmed at its head so that a paraphrase supplies its subject, and a dropped bracket is
the defect class this line has already recorded twice in first extracts.)*

**What it delivers, in its own summary (§1.3, PDF page 3).** *"We present here an original approach
to model key change with the help of musicological knowledge-based features used by an algorithm
estimating the tonal plan of a piece."* Concretely: two features (the **current diatonic pitch
set** and a **heuristic for V → I progressions**), a third measure of **distance between keys**
taken from Weber's 1817 table, and a **dynamic-programming algorithm** that combines the three by a
weighted sum and returns one key per beat for the whole piece.

**The shape of the output.** A *tonal plan* k₁…k_B: for a piece of B beats, one key k_b chosen for
each beat b, out of 42 candidate keys. Modulations are wherever the plan changes key.

**The evaluation, in one line.** 38 movements of Mozart's string quartets, with manual key
annotation, reporting **84.8% of beats assigned the correct key** with the best weights; and one
movement, the third of quartet No. 3 (K 157), examined case by case.

**Why this paper could carry load for us, stated as this read's own judgment and not as a finding
of the record.** It is a key decision made over time by minimising an explicit additive cost over a
per-beat key sequence, with a transition term between adjacent keys — the same shape as a decode
with a key-change cost — and its transition term is taken from a published key-relationship table
rather than from the circle of fifths.

*(★ CORRECTED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "It is also the only reading in this
line so far, as far as this side's own reading reaches, whose transition term is taken from a
published key-distance table rather than from the circle of fifths." That was a uniqueness claim
over a population this side has not read — no other paper of this slice was opened here — and the
hundred-and-eighteenth entry, which this side DID read, describes row 26's paper as a working
instance of a tonality-change cost built from a published key-distance measure. So the claim was not
merely underived; it was contradicted by something already in front of this side.)*

---

## §2 — The method, as the paper states it

### §2.1 The candidate key set and the analysis grid

**42 candidate keys** (§3, PDF page 6): *"We consider that there are 42 possible keys that
correspond to all the triplets: {C, D, E, F, G, A, B} × {♯, ♮, ♭} × {Major, minor}"*. Seven pitch
names times three accidentals times two modes. **This read's arithmetic: 7 × 3 × 2 = 42, which is
the number the paper prints.**

**The grid is the beat**, and its size is fixed per piece by the time signature (§4.1, PDF page 6):
*"The beat granularity used is the quarter note for binary time signatures and the dotted quarter
note for ternary time signatures. We consider this to be sufficient to model most of the harmonic
rhythm in this repertoire."* **The sufficiency is stated as a judgment, and a measurement of it is
met nowhere in the nine pages as this side read them.**

### §2.2 Measure one — pitch compatibility, by the current diatonic pitch set

**The idea, in the paper's words (§2.1.1, PDF page 3).** *"Each note sounding in a score confirms or
modifies our perception of the current tonality. Suppose that we are used to hearing C♮. When one
hears a C♯, the perception of the diatonic scale may change. If we now hear only C♯, we are likely
to think we are in a tonality including this pitch. Of course, approaches based on pitch profiles
consider statistics on C♮ and C♯, but they do not take into account the **directedness** of music:
one or a few C♯ can alter our perception, no matter how many C♮ there were before."*

**This is the paper's stated reason for not using a pitch profile at all**, and it is a claim about
what a histogram cannot represent: recency and direction, as against prevalence.

**The construction.** N is the set of the seven pitch names, *"N = {C, D, E, F, G, A, B}"*. Then
(PDF page 4):

> *"The current diatonic pitch set CS(b) is a vector with 7 values built by associating to each of
> the pitch names in N the last encountered accidental (♭♭, ♭, ♮, ♯, ♯♯) on b or right before."*

Three further rules are given at the same place:

- *"It can thus have theoretically 5⁷ different values, even if many of these values are not
  musically relevant."*
- *"If one of the 7 pitches was not used before b, we consider the accidental suggested by the key
  signature of the piece."*
- *"The current diatonic pitch set is evaluated at each beat. If two accidentals are encountered for
  the same pitch name between two beats, only the last one is considered."*

**So the object is a spelling state, not a count.** It carries one accidental per letter name,
always exactly seven values, and it is overwritten by the most recent accidental. It is introduced
by citation to the authors' own earlier work: *"we introduced the current diatonic pitch set, also
called current diatonic scale, in [23]"*, reference [23] being Feisthauer, Bigo and Giraud,
*"Modeling and learning structural breaks in sonata forms"*, ISMIR 2019.

**The expected pitch set of a key** (§2.1.2, PDF page 4):

> *"for the major keys, pitches of the usual major scale, as {C, D, E, F, G, A, B} for C Major,"*
> *"for the minor keys, pitches of the minor harmonic scale, as {C, D, E♭, F, G, A♭, B(♮)} for
> C minor."*

**A minor key is represented by the harmonic minor form alone.** A natural or melodic minor variant,
and any mechanism by which a minor key's sixth or seventh degree could take more than one value, are
met nowhere in the nine pages as this side read them. **This read flags that now because the paper's own §4.3 later attributes its
weaker minor-mode results to exactly that degree of freedom; the two statements are set against
each other at §7.3.**

**The distance and the measure** (§2.1.3, PDF page 4):

> *"Given any two diatonic pitch sets S and S′, we define the distance d_diat(S, S′) as the number
> of differently altered notes between them: d_diat(S, S′) = |{n ∈ N with S[n] ≠ S′[n]}|"*

and the proximity used at a beat is **d_diat(CS(b), S(k))** — the current spelling state against the
key's expected spelling. **Its range is 0 to 7 by construction**, which is why the combination later
divides it by 7.

**The paper's two worked values, both verified by this read at the paper's own definitions.** With
CS(2) = {C♯, D, E♭, F♯, G, A, B♭} (the value the paper gives for beat 2 of measure 27 in Figure 1):

- *"d_diat(CS(2), S(G minor)) = |{C}| = 1"*. Harmonic G minor is G A B♭ C D E♭ F♯, which as a
  per-name vector is C♮ D♮ E♭ F♯ G♮ A♮ B♭. Against CS(2) only the C differs. **CONFIRMED.**
- *"d_diat(CS(2), S(C minor)) = |{C, F, A, B}| = 4"*. Harmonic C minor is C D E♭ F G A♭ B♮, that is
  C♮ D♮ E♭ F♮ G♮ A♭ B♮. Against CS(2) the C, F, A and B differ. **CONFIRMED.**

The paper draws the point from them: *"The measure captures that having recently heard an F♯ makes
a G minor more relevant than a C minor."*

**The Figure 2 worked values, also verified by this read.** *"At the cadence in D minor, we have
CS(b) = {C♯, D, E, F, G, A, B♭}"* — which is exactly the harmonic D minor vector — *"and the same
CS(b) is still found at measure 8. The C♮ at measure 10 yields a scale which is exactly S(F Major):
CS(c) = {C, D, E, F, G, A, B♭}"* — which is exactly the F major vector. **Both CONFIRMED against the
paper's own definitions of S(k).**

### §2.3 Measure two — tonality anchoring, by a V → I heuristic

**Why V → I** (§2.2.1, PDF page 4): *"The most stable harmonic progression for a key is the one
from the dominant (fifth scale degree, V) to the tonic (first scale degree, I). Such V → I
progressions are a good confirmation that a modulation occurs. However, a V → I progression can
occur on another scale degree than the first one (what is called a **tonicization**, as in Figure
1). Due to tonicization, modulations can thus not be solely based on V → I, but such progressions
are nevertheless important contributions to modulations."*

**The heuristic itself**, quoted whole because it is the paper's one structural definition of what
counts as a dominant-to-tonic arrival (§2.2.1, PDF page 4):

> *"Our heuristic to detect a V → I progression in key k is when there are at least two of the three
> following voice leadings:*
> *① the third of V (also known as the leading tone) going to the tonic of I,*
> *② the seventh of V going to the third of I,*
> *③ the root from V going to the root from I."*

**Two of three, and the three are voice motions, not chord labels.** This read reads that as meaning
the detector needs the individual moving parts and needs the key k whose degrees define V and I, and
does NOT need any upstream chord identification. That reading is this read's own and is set out with
its consequences at §3.1.

**The paper states its own false positives at the same place**, which is worth carrying because a
method's declared failure mode is a coupling fact:

> *"Note that this heuristic produces false positives for **homonym** keys. In Figure 2 again, the
> V → I on the cadence on measure 8 is a cadence in D minor, but the heuristic also falsely detects
> it as a V → I in D Major, because two of the three voice leadings characteristic of D Major are
> found. The heuristic will also falsely consider I → IV movements as V → I."*

**The measure built on it** (§2.2.2, PDF pages 4–5). The paper proposes that the proximity of a key
be *"harmonically minimal"* when a dominant-to-tonic progression is occurring in it, and otherwise
grow with the distance in beats from the last one:

> c_{V⌣I}(b, k) = 0 — *"if the harmony at b is the V or the I of a V → I progression in k"*
> c_{V⌣I}(b, k) = min[c, c_{V⌣I}(b − 1, k) + 1] — *"otherwise"*

and: *"To avoid values that are too high, we bound this value by a constant c = 20. Note that the
value 0 is given at the moment the V occurs, because it triggers the modulation."*

**So it is a saturating count of beats since the last detected V → I in that key**, floored at 0 and
capped at 20. The cap is declared and no derivation of the value 20 is given.

### §2.4 Measure three — tonality proximity, by Weber's table

**Why not the circle of fifths** (§2.3, PDF page 5): *"While working on Mozart's string quartets, we
noticed that Mozart often switched between Major and minor modes of the same key. The circle of
fifths is not designed for this behavior, whereas it is present in the table of relationships
between keys introduced in 1817 by Gottfried Weber in Versuch einer geordneten Theorie der
Tonsetzkunst [26] (see Figure 3). This Weber's table is actually one of the spaces that **Lerdhal**
deduces from his tonal pitch space framework [8]."* **The spelling *Lerdhal* is the paper's own at
this place and is reproduced as printed; it is inconsistent with two other places in the same paper,
which is D-21.**

*(★ CORRECTED AT THE CROSS-CHECK, THE PAPER GOING AGAINST THIS SIDE. FORMER WORDING, PRESERVED (#12):
"the spaces that Lerdahl deduces". This read silently repaired the paper's misspelling inside a
quotation. Repairing a source's error without marking it destroys the evidence that the source is
inconsistent, and it is what would have hidden D-21 altogether. The first extract had it right and
marked it as reproduced as printed.)*

**The measure:**

> *"We define d_W(k, k′), our measure of proximity between two keys k and k′, as the Euclidean
> distance between those two keys in Weber's table: d_W(k, k′) = min( √(|x_{k′} − x_k|² +
> |y_{k′} − y_k|²), w ) where (x_k, y_k) and (x_{k′}, y_{k′}) are the coordinates of both keys in
> the table and w = 10 is a bounding constant."*

**Its worked values:** *"d_W(D minor, F Major) = 1 whereas d_W(D minor, C) = √2. It is more common in
the classical era to modulate from D minor towards F Major, as in Figure 2, than towards C Major."*

**The paper bounds its own choice here**, and the bound is quoted because it is a scope statement:
*"Note that other distances could also be defined on the Weber's table. Moreover, this table seems to
be relevant mostly for the classical period. Modulations are more daring from the romantic era,
favoring enharmonic and chromatic modulations."*

**Figure 3's caption tells the reader how to read the table:** *"Extract of the Table of the
relationship of keys from [26]. Major keys are uppercase, minor keys are lowercase."* **The figure is
an extract, and the whole table and the coordinate assignment (x_k, y_k) the measure uses are met
nowhere in the nine pages as this side read them.** So the numeric value of d_W for a pair of the 42
keys that the text does not work out cannot be recomputed from what those pages print. **That is
this read's observation and is recorded as a gap at §7.2.**

### §2.5 The combination, and the algorithm

**The cost of a whole tonal plan** (§3, PDF pages 5–6):

> D(k₁…k_B) = Σ_{b∈[1,B]} [ α · c_{V⌣I}(b, k_b)/c + β · d_diat(CS(b), S(k_b))/7 ]
> + Σ_{b∈[2,B]} γ · d_W(k_{b−1}, k_b)/w

*"where the divisions by c, 7, and w normalize each of the three measures to obtain values between 0
and 1. The weights α, β, and γ further ponder the relative importance of the three measures."*

**So two of the three terms are per-beat and the third is per-transition**, and the whole is one
additive cost to be MINIMISED.

**The recurrence** (§3, PDF page 6), with D(1, k) = 0 and, for b ≥ 2:

> D(b, k) = α · c_{V⌣I}(b, k)/c + β · d_diat(CS(b), S(k))/7 + min_{k′} [ γ · d_W(k, k′)/w + D(b − 1, k′) ]

**The array is B × 42** and the plan is recovered by backtracking from the last beat. The paper's own
description of the backtracking is quoted verbatim here, including a defect in it that is reported
at §7.1:

> *"• for the last beat b_B, choose the key k_B that minimizes D(b_B, k_B);*
> *• for the preceding beat b_{B−1}, choose the key k_{B−1} ; that minimizes d_W(k_{B−1}, k′) +
> D(b_{B−1}, k_{B−1})*
> *• repeat until the first beat b₁."*

**What the algorithm is, in plain words:** a Viterbi-style shortest-path over a trellis whose states
are the 42 keys and whose stages are the beats, with an emission-like per-beat cost made of two
knowledge-based features and a transition cost taken from a key-relationship table. **This sentence
is this read's characterisation and not the paper's: the words Viterbi, trellis, emission and
transition are met nowhere in the nine pages as this side read them, and the pages were read as
images rather than searched as text, so that negative is a reader's negative and not a search
result.**

---

## §3 — Coupling facts

*These are the commission's mandatory three: what the method assumes about its upstream, what it
hands downstream, and its own stated scope and limits. Where a line is this read's inference from
the paper rather than the paper's own statement, it says so.*

### §3.1 What it ASSUMES about its upstream

**(a) Full pitch spelling, and the paper says so in terms** (§2, PDF page 3):

> *"These measures are designed for scores with **full pitch spelling** information. We strongly
> believe that when it comes to tonal music, it provides information not only about pitch but also
> about its function – "sharpening" or "flattening" a pitch is a thoughtful choice by the composer,
> important for the analysis. On data without such information, pitch spelling algorithms [22] could
> be applied first but the pitches which are the most difficult to spell are precisely the
> challenging ones for key and modulation estimation."*

**That last clause is the load-bearing half and it is the paper's own.** It says that the fallback —
spell the pitches algorithmically first — is weakest exactly where this method needs it most. **A
consumer of this method on unspelled input is therefore told by the paper itself that the
substitution is not neutral.**

**(b) A metrical grid with a known time signature**, since the beat is the analysis unit and its size
is chosen by whether the signature is binary or ternary (§4.1).

**(c) A key signature for the piece**, used to fill the accidental of any of the seven pitch names not
yet sounded before beat b (§2.1.1). **Derived from that rule: the current diatonic pitch set has a
defined value at every beat, including the first, because any letter not yet heard takes the
signature's accidental.** **This read's judgment, offered as judgment: the key signature is therefore
a required input and not merely a hint** — at the start of a piece, before many letters have been
heard, the state is largely the signature's.

**(d) Separable voices, for the V → I heuristic.** The three tests are voice leadings — one pitch
*going to* another. **This read's inference: the detector needs note-to-note motion in parts, so it
needs the score's voices and not only the sounding pitch-class set.** The paper does not state this
requirement in its own words; it is inferred from the heuristic's own wording.

**(e) NO upstream chord analysis, and no upstream key DECISION — though the key signature is
required, per (c), and a signature is not nothing.** **This read's inference, stated with its
ground:** the heuristic defines V and I by the scale degrees of the candidate key k, and detects the
progression from voice leadings alone, so no chord label need arrive from anywhere; and the
algorithm searches all 42 keys rather than being handed one. **A statement that the method takes
chord labels as input, and any named chord-identification step, are met nowhere in the nine pages as
this side read them.** The measure c_{V⌣I}'s own wording — *"if the harmony at b is the V or the I of
a V → I progression in k"* — uses the word *harmony* but defines the progression by the voice-leading
heuristic immediately above it. **A reader who wanted to build on this should note that this is an
inference and not a printed statement.**

*(★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "NO upstream chord analysis, and NO
upstream key." The second half was too wide: the key signature IS an upstream input under (c), and
writing "no upstream key" invites a reader to carry this method as needing nothing tonal from
upstream, which the signature requirement refutes.)*

*(★ AND THE PLACEMENT WAS CORRECTED AT THE USER-ORDERED CHECK OF 2026-09-12: the read-back's
correction note had been inserted in the middle of this paragraph, leaving its closing sentence
stranded below the note and beginning with the bare words "The measure". **No word of either the
paragraph or the note changed in the move.**)*

**(f) A reference key annotation, for evaluation only** (§4.1). The corpus carries *"manual annotation
of keys and cadences"*.

### §3.2 What it HANDS downstream

**(a) One key per beat for the whole piece** — the tonal plan k₁…k_B, drawn from the 42 candidates.

**(b) Modulation positions, implicitly.** A separate modulation output is defined nowhere in the nine
pages as this side read them; a
modulation is where the plan changes key. **So what is handed on is a segmentation into key regions,
derived from the per-beat plan and not published as its own object.**

**(c) A per-beat cost for every one of the 42 keys**, the array D(b, k). **The paper itself uses the
margin of that array**: Figure 7 plots *"the difference D(k, b) − min_{k′} D(k′, b)"*. **So the
material for a ranked candidate list with margins exists inside the algorithm.** The paper does not
publish it as an output, does not name it a confidence, and does not calibrate it.

**(d) What it does NOT hand down**, as far as this read found in the nine pages: no probability and
no quantity the paper calls a confidence; no chord; no Roman numeral; no cadence label — although
the corpus carries cadence annotation, the algorithm neither consumes nor produces one; and no
alternative tonal plan beside the best one.

### §3.3 Its own STATED scope and limits

**(a) Repertoire.** Evaluated on Mozart string quartets alone. The paper's own qualification on the
key-distance table is broader than the evaluation: Weber's table *"seems to be relevant mostly for
the classical period"*, and *"Modulations are more daring from the romantic era"* (§2.3).

**(b) Minor keys are the harmonic minor form only** (§2.1.2). No alternative minor collection is
offered.

**(c) The weights were fitted on the corpus the results are reported on, and the paper states this in
terms** (§4.3, PDF page 7):

> *"The best coefficients α, β, and γ were tracked by evaluating combinations of values between 0 and
> 4 (with increments of about 0.002 for α, 0.02 for β, and 0.5 for γ) on an annotated corpus of 38
> Mozart's string quartets. Although no training set was separated from the corpus, we felt that
> overfitting was a minor risk due to the size of the corpus and the very small number of
> parameters."*

**No held-out split, and the paper says so.** The reason given is a judgment — *"we felt that
overfitting was a minor risk"* — and no measurement of that risk is reported. **This read ranked no
scope limit against another and does not claim this one is the largest; what it does claim is that
the 84.8% cannot be read as a held-out result, which is a bound on the value itself and not on its
surroundings.** It is carried into §5 and §7.2 rather than left here.

*(★ CORRECTED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "This is the single most consequential
scope limit in the paper for any use we would make of the 84.8%." A superlative over the paper's
limits, from a comparison this read never made — cadence 6's own prohibition.)*

**(d) No comparison against any other key-finding algorithm.** The paper's own conclusions place this
in future work: *"Perspectives include a more accurate V → I detection and **more complete
benchmarks, including comparisons with alternative key finding algorithms** and other theories on
tonality"* (§5, PDF page 8). **Every baseline this side met in the nine pages is one of the paper's
own ablations — the three non-best rows of Table 2.**

**(e) No corpus-level measurement of WHERE a modulation was placed.** From §5: *"as well as **an
evaluation of the detected position of each modulation**."* **The paper's stated motivation is where
modulations occur, and its results tables report only whether each beat's key is right, never how
far a detected boundary sits from the annotated one.** The one positional statement this side met in
the nine pages is about a single movement, is given in prose rather than in any table, and is quoted
at §5.

*(★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "The position of a modulation is not
evaluated" and "the paper does not measure where they were placed". Both were refuted by the paper's
own sentence at §4.3, which states that on K157.3 the modulations are found "at most within 2 beats"
of the annotated place — that IS a positional statement, and the true claim is that there is no such
measurement over the corpus.)*

**(f) The declared failure modes of the V → I heuristic**: homonym (parallel) keys, and I → IV
movements read as V → I (§2.2.1), both restated as measured at §5.

**(g) Two bounding constants, c = 20 and w = 10, are declared and not derived.** The paper gives a
reason of form — *"To avoid values that are too high"* — and no reason for either value.

**(h) The combination is declared simple and provisional.** *"The combination of the measures is still
very simple – improved combinations, possibly involving machine learning, could improve the raw
results"* (§5).

---

## §4 — Claims labeled

*FACT = stated or measured in this paper, with its location. THEORY = established published theory
the paper invokes. CONJECTURE = asserted without a measurement or a citation carrying it. The label
is about what THIS paper establishes, never about whether the claim is true.*

**F-1 [FACT].** The corpus is 38 movements of Mozart's string quartets with manual annotation of keys
and cadences, in `**kern` format with full pitch spelling, retrieved from KernScores, and the
reference annotation is available at `www.algomus.fr/data`. §4.1, PDF page 6.

**F-2 [FACT].** The corpus is *"an enhancement of the corpus used and described in previous works on
sonata forms [23, 29]"* — that is, an enhancement of a corpus of the same research group. §4.1, PDF
page 6.

**F-3 [FACT].** The implementation is in Python, within the music21 framework. §4.1, PDF page 6.

**F-4 [FACT].** With the best weights the algorithm assigns the correct key to **84.8%** of beats on
the corpus. Table 2, PDF page 8; the same value is in the abstract.

**F-5 [FACT].** The best weights are α = 0.016, β = 0.3, γ = 4.0. §4.3 and Table 2.

**F-6 [FACT].** The pitch-compatibility measure alone (α = 0, β = 1, γ = 0) gives **67.3%** correct;
the anchoring measure alone (α = 1, β = 0, γ = 0) gives **16.3%**; the no-modulation baseline
(α = 0, β = 0, γ = 1) gives **50.0%**. Table 2, PDF page 8.

**F-7 [FACT].** On the single movement K157.3, the best d_diat value describes the correct key for
**243 of 252 beats**. §4.2.1, PDF page 7.

**F-8 [FACT].** On K157.3, the anchoring measure by itself predicts correctly **66 of the 252
beats**. §4.2.3, PDF page 7.

**F-9 [FACT].** On K157.3, the full combination with the optimal weights gets **248 of the 252
beats**. §4.3 continuation, PDF page 8.

**F-10 [FACT].** On K157.3, the reference annotation contains **38** V → I movements; the heuristic
detects **116**, of which **29** are true positives and **87** false positives. §4.2.2 and Table 1,
PDF page 7.

**F-11 [FACT].** Restricted to the two most present keys of K157.3, C Major and G Major, the false
positives are **12 of 39** predictions. §4.2.2, PDF page 7.

**F-12 [FACT].** Over the 30 movements whose main key is major, the algorithm's totals are 10333
reference beats, 10333 predicted, 8998 true positives, 1335 false positives, 1335 false negatives,
F₁ = 0.87. Over the 8 movements whose main key is minor: 3172 reference, 2462 true positives, 710
false positives, 710 false negatives, F₁ = 0.78. Table 3, PDF page 8. **The minor half's predicted
total is printed as 172 and is not carried here as a value; it is treated at §6.3 and §7.1 D-1.**

**F-13 [FACT].** The algorithm's F₁ is highest on the main key itself — 0.92 for I with a major main
key, 0.88 for i with a minor main key. **The degrees the paper groups as subdominant-related carry
0.12 for ii and 0.63 for IV with a major main key, and 0.62 for iv with a minor main key.** Table 3,
PDF page 8. **In the major table ii's 0.12 is the lowest value printed, and IV's 0.63 is NOT — v is
lower at 0.58.** In the minor table iv's 0.62 is the lowest printed.

*(★ CORRECTED AT THE USER-ORDERED CHECK OF 2026-09-12. FORMER WORDING, PRESERVED (#12): "and lowest
on the subdominant-related degrees, 0.12 for ii and 0.63 for IV with a major main key, and 0.62 for
iv with a minor main key." **Refuted by this file's own transcription of Table 3 two sections away:
the v row carries 0.58, below IV's 0.63**, so *lowest on the subdominant-related degrees* is false of
the major table. The paper's grouping is the paper's; the ranking was this read's and it was wrong.)*

**F-14 [FACT].** The V → I heuristic requires at least two of three named voice leadings. §2.2.1,
PDF page 4.

**F-15 [FACT].** The heuristic produces false positives on homonym keys and on I → IV movements, and
the paper demonstrates the first at a specific place in Figure 2 (the cadence at measure 8, detected
also in D Major). §2.2.1, PDF page 4.

**F-16 [FACT].** No training set was separated from the corpus on which the weights were fitted.
§4.3, PDF page 7.

**F-17 [FACT].** The candidate key set is 42 keys. §3, PDF page 6.

**F-18 [FACT].** The bounding constants are c = 20 for the anchoring measure and w = 10 for the key
distance. §2.2.2 and §2.3.

**T-1 [THEORY].** That a dominant-to-tonic progression is the strongest confirming signal of a key is
carried by citation to Rimski-Korsakov's *Practical Manual of Harmony* [21], as is the claim that for
the classical period a composer's chosen keys are associated with the scale degrees of the main key,
prioritising the dominant, or the relative major for a minor main key. §2, PDF page 3.

**T-2 [THEORY].** Weber's 1817 table of key relationships, and Lerdahl's deduction of it from tonal
pitch space, are invoked by citation ([26] and [8]) as the ground for using a two-dimensional key
space rather than the circle of fifths. §2.3, PDF page 5.

**T-3 [THEORY].** The historical account of tonality — Rameau 1722, Choron's 1810 coining of the
term, the two-mode restriction of "modern tonality", Riemann — is given by citation. §1.1, PDF page
2.

**T-4 [THEORY].** The sonata-form claim, that the exposition's two themes are in different keys and
that the modulation between them is often accompanied by a medial caesura, is carried by citation to
Hepokoski and Darcy [3]. §1.1, PDF page 2.

**C-1 [CONJECTURE].** That the chosen beat granularity *"is sufficient to model most of the harmonic
rhythm in this repertoire"* (§4.1). No measurement of what it misses is reported.

**C-2 [CONJECTURE].** That overfitting is *"a minor risk due to the size of the corpus and the very
small number of parameters"* (§4.3). The paper reports no held-out measurement and no estimate of the
risk; the words it uses are *"we felt"*.

**C-3 [CONJECTURE].** That pitch profiles cannot capture the directedness of music (§2.1.1). The
paper argues it and cites no measurement of it; the argument is the ground the paper gives for its
pitch-compatibility feature.

**C-4 [CONJECTURE].** That the weaker minor-mode results are *"mostly explained by the floating 6th
and 7th scale degrees of the minor scale"* (§4.3). An explanation is offered; no measurement
separating that cause from any other is reported.

**C-5 [CONJECTURE].** That the false positives of the V → I heuristic are what keeps c_{V⌣I} from
helping — *"c_{V⌣I} is generally high and does not significantly help the detection here, probably
due to the false positives"* (§4.3). The paper's own word is *"probably"*.

**C-6 [CONJECTURE].** That the value 20 for c and the value 10 for w are the right bounds. Declared,
not derived.

---

## §5 — Measured results, with corpus, metric and value as the paper states them

**Corpus A — the whole corpus.** 38 movements of Mozart's string quartets, manually annotated with
keys; 30 of the movements have a major main key and 8 a minor one (Table 3's caption). Metric: the
percentage of beats assigned the correct key, and per-degree precision/recall/F₁.

| Method, as Table 2 names it | α | β | γ | Correct (% of beats) |
|---|---|---|---|---|
| only d_diat | 0 | 1 | 0 | **67.3** |
| only c_{V⌣I} | 1 | 0 | 0 | **16.3** |
| no modulation | 0 | 0 | 1 | **50.0** |
| best coefficients | 0.016 | 0.3 | 4 | **84.8** |

Table 2's own caption: *"Correct key prediction (percentage of beats) on the corpus. When α = β = 0,
then D(b, k) is minimal when each beat is in the main key: This baseline algorithm considers that no
modulations occur."*

The paper's reading of the table (§4.3): *"Table 2 shows that although the current diatonic pitch set
measure alone (β = 1) yields good results, adding the others **measures** improves the local key
detection by 17.5%."*

*(★ CORRECTED AT THE CROSS-CHECK, THE PAPER GOING AGAINST THIS SIDE. FORMER WORDING, PRESERVED (#12):
"adding the others improves the local key detection by 17.5%". This read dropped the word *measures*
from inside a quotation, silently and without an ellipsis. **No value moves** — but the dropped word
is also the one that makes the phrase ungrammatical, so dropping it tidied the paper's text, which a
transcription may not do. The first extract had the word.)*

**Table 3, transcribed whole. Main key in major mode (30 movements):**

| key | ref | pred | TP | FP | FN | F₁ |
|---|---|---|---|---|---|---|
| I | 5801 | 5999 | 5451 | 548 | 350 | 0.92 |
| V | 2851 | 2846 | 2525 | 321 | 326 | 0.89 |
| vi | 469 | 410 | 330 | 80 | 139 | 0.75 |
| IV | 386 | 382 | 241 | 141 | 145 | 0.63 |
| i | 204 | 217 | 159 | 58 | 45 | 0.76 |
| v | 152 | 129 | 81 | 48 | 71 | 0.58 |
| ii | 130 | 18 | 9 | 9 | 121 | 0.12 |
| ♭III | 102 | 84 | 63 | 21 | 39 | 0.68 |
| others | 238 | 248 | 139 | 109 | 99 | – |
| **total** | **10333** | **10333** | **8998** | **1335** | **1335** | **0.87** |

**Main key in minor mode (8 movements):**

| key | ref | pred | TP | FP | FN | F₁ |
|---|---|---|---|---|---|---|
| i | 1268 | 1038 | 1012 | 26 | 256 | 0.88 |
| I | 544 | 543 | 462 | 81 | 82 | 0.85 |
| ♭III | 421 | 654 | 385 | 269 | 36 | 0.72 |
| V | 262 | 234 | 213 | 21 | 49 | 0.86 |
| iv | 247 | 133 | 118 | 15 | 129 | 0.62 |
| v | 177 | 230 | 155 | 75 | 22 | 0.76 |
| others | 253 | 340 | 117 | 223 | 136 | – |
| **total** | **3172** | **172** | **2462** | **710** | **710** | **0.78** |

**The printed pred total of the minor table is 172 and this read reports it as printed.** **The
arithmetic showing the paper's own columns inconsistent with it is at §6.3**, and it is reported as a
defect at §7.1 D-1.

Table 3's caption: *"Key detection accuracy over the 30 Mozart string quartets movements in a major
key (top), and in the 8 movements in a minor key (bottom), with the best coefficients. The results
are gathered by keys. Each key is identified by how its tonic relates to the scale degrees of the
main key of each movement. Major key are uppercase while minor key are lowercase."*

**Corpus B — one movement, K157.3**, the third movement of Mozart's String Quartet No. 3, K 157,
*"in rondo form and its main key is C Major"* (§4.2). §1.3 names the same movement the *Presto*.
**The movement's length of 252 beats is not stated as such anywhere this side read; it is the
denominator of the per-beat results below, each of which is printed as a fraction of 252.**

| Quantity | Value | Location |
|---|---|---|
| Beats where the best d_diat value describes the correct key | **243 of 252** | §4.2.1 |
| Beats the anchoring measure alone predicts correctly | **66 of 252** | §4.2.3 |
| Beats the full combination gets right | **248 of 252** | §4.3 continuation, PDF page 8 |
| V → I movements in the reference annotation | **38** | §4.2.2 |
| V → I movements the heuristic detects | **116** | §4.2.2 |
| True positives among them | **29** | §4.2.2, Table 1 |
| False positives among them | **87** | §4.2.2, Table 1 |
| False positives in C Major and G Major together | **12 of 39** | §4.2.2 |

**Table 1, transcribed whole**, whose caption is *"V → I progressions in K157.3, in the reference
annotation (ref), predicted by the heuristic (pred), among which false negatives and positives (FN
and FP), and associated F₁ measure."*

| key | ref | pred | TP | FN | FP | F₁ |
|---|---|---|---|---|---|---|
| C Major | 28 | 34 | 24 | 4 | 10 | 0.77 |
| C minor | 4 | 26 | 2 | 2 | 24 | 0.13 |
| G Major | 4 | 5 | 3 | 1 | 2 | 0.67 |
| G minor | 0 | 3 | 0 | 0 | 3 | · |
| E♭ Major | 2 | 0 | 0 | 2 | 0 | · |
| others | 0 | 48 | 0 | 0 | 48 | · |
| (C♭ minor) | 0 | 0 | 0 | 0 | 0 | · |

**The four keys the figures follow**, given at §4.2 so the reader knows what the curves are:
C Major, the main key; G Major, the dominant, *"modulation at measures 17 through 32"*; C minor, the
parallel key, *"modulation at measures 49-56 and 61-64"*; and C♭ minor, *"an intentional distant key
to confirm the pertinence of each measure"*.

**The one positional statement this side met in the nine pages**, quoted exactly because it is the
only place they say WHERE a modulation was placed (§4.3 continuation, PDF page 8):

> *"The proposed method manages to find the main key of C Major and all modulations (G Major, C
> minor, and – not shown – E♭ Major), **at most within 2 beats of the place the modulation occurs in
> the reference analysis.**"*

**It is about one movement**, it is stated in prose and not in any table, and the paper's own §5
lists evaluating modulation position as future work.

**A second qualitative observation the paper reports as a result** (§4.2.1, PDF page 7):

> *"Starting from beat 100, only d_diat(b, C minor) provides a value of zero for a few beats. In this
> region, Mozart progressively modulates by gradually introducing notes of the upcoming key C minor.
> The current diatonic pitch sets retrieved in this region do not exactly fit with any of the keys
> but still favor this key of C minor in a few beats. Note that between beats 112 and 119, the key of
> the reference annotation E♭ Major is correctly detected, although the corresponding curve is not
> shown in the figure for clarity."*

**And the stated reason the combination beats d_diat alone on that movement:**

> *"Indeed, the computation of D, including d_W, favors some stability in the predicted keys,
> preventing the algorithm from switching keys for only 1 or 2 beats when a nonchord tone do appear."*

---

## §6 — Arithmetic this read performed on the paper's own printed values

*Nothing in this section is a measurement of the method. Every line is a check of the paper's printed
numbers against each other, run because the commission's form asks for measured results as the paper
states them and a table that does not close is not a value that can be carried.*

### §6.1 Table 1 closes at every check this read ran on it

Column sums: ref 28+4+4+0+2+0+0 = **38**, which is the number the prose gives for the reference
annotation. pred 34+26+5+3+0+48+0 = **116**, the number the prose gives for detections. TP
24+2+3+0+0+0+0 = **29**. FP 10+24+2+3+0+48+0 = **87**. FN 4+2+1+0+2+0+0 = **9**, and 38 − 29 = 9.

Row identities: ref = TP + FN and pred = TP + FP hold on every one of the seven rows.

F₁ recomputed from the counts: C Major 0.774, C minor 0.133, G Major 0.667 — against the printed
0.77, 0.13, 0.67. **Agreement at the printed precision.**

The prose's *"few false positives (12/39)"* for C Major and G Major: FP 10 + 2 = **12**, pred 34 + 5 =
**39**. **CONFIRMED.**

### §6.2 Table 3's major-mode half closes at every check this read ran on it

Column sums: ref = **10333**, pred = **10333**, TP = **8998**, FP = **1335**, FN = **1335** — each
equal to the printed total. Row identities ref = TP + FN and pred = TP + FP hold on all nine rows.
F₁ recomputed per row: 0.924, 0.886, 0.751, 0.628, 0.755, 0.577, 0.122, 0.677 — against the printed
0.92, 0.89, 0.75, 0.63, 0.76, 0.58, 0.12, 0.68. **Agreement at the printed precision.** The total F₁
0.871 against the printed 0.87, and it is an equality case: false positives equal false negatives, so
precision equals recall.

### §6.3 Table 3's minor-mode half closes at every check this read ran EXCEPT the printed pred total

*The checks run in §6.1 to §6.3 are these, and no others: each column summed against its printed
total; the identities ref = TP + FN and pred = TP + FP on each row; F₁ recomputed from each row's own
counts; and the prose figures that cite the table checked against it. **A check this read did not
run: whether the counts themselves are right, which would need the corpus and the reference
annotation, neither of which this side holds.***

Column sums: ref = **3172**, TP = **2462**, FP = **710**, FN = **710** — each equal to its printed
total. Row identities hold on all seven rows. F₁ recomputed per row: 0.878, 0.850, 0.716, 0.859,
0.621, 0.762 — against the printed 0.88, 0.85, 0.72, 0.86, 0.62, 0.76. **Agreement at the printed
precision.**

**The pred column sums to 3172** — 1038+543+654+234+133+230+340 — **and the table prints 172.** The
printed total F₁ of 0.78 is itself the evidence: precision is TP/pred, so a pred total of 172 against
2462 true positives would give a precision above 1, which is impossible, whereas 2462/3172 = 0.776,
which rounds to the printed 0.78. **This is reported at §7.1 as a printed defect.**

### §6.4 The headline 84.8% against Table 3's own totals

Pooling both halves of Table 3: correct beats 8998 + 2462 = **11460**; reference beats 10333 + 3172 =
**13505**; the proportion is **0.8486**, that is **84.86%**. The printed headline is **84.8%**.

**This read does not call that a defect.** 84.86 truncated rather than rounded gives 84.8, and the
difference is 0.06 percentage points. **What this read does record is that a statement of whether the
headline percentage is pooled over all beats or averaged over movements is met nowhere in the nine
pages as this side read them**, and Figure 6's
caption uses the words *"Average accuracies"*, which is the other of the two readings. The two
readings need not give the same number, and the paper does not say which it used. **Recorded as a gap
at §7.2, not as an error.**

### §6.5 The paper's "17.5%" is a difference of percentage points

84.8 − 67.3 = **17.5**, so the paper's *"adding the others measures improves the local key detection
by 17.5%"* is the arithmetic difference of two percentages.

*(★ CORRECTED AT THE USER-ORDERED CHECK OF 2026-09-12. FORMER WORDING, PRESERVED (#12): "adding the
others improves the local key detection by 17.5%". **The cross-check corrected this quotation at §5
and did not reach the second copy of it here** — the same sentence stood in the file twice, corrected
in one place and not the other. A correction that fixes one instance of a repeated quotation and
leaves the other is a defect of its own.)* **Expressed as a relative improvement it
would be 17.5/67.3 = 26.0%.** The paper writes the percentage-point difference with a per-cent sign.
**Recorded at §7.1 as a wording defect and not as a wrong value** — the value 17.5 is right for what
it is.

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

*Each is stated with what refutes it, and each is a defect of this paper's own text, not a judgment
of its method.*

**D-1. Table 3's minor-mode `pred` total is printed as 172 and its own column sums to 3172.** The
missing leading 3 is established two ways: by the column sum, and by the printed total F₁ of 0.78,
which is only reachable with a denominator of 3172. **This is a defect in a printed number itself,
where the items below it are defects of wording, notation or argument.**

*(★ CORRECTED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "This is the one defect in the paper
that touches a printed value." That was a uniqueness claim over this read's own list of findings,
which is not the same thing as a claim about the paper, and this read ran no derivation entitling it
to either.)*

**D-2. The corpus is 38 MOVEMENTS in §4.1 and 38 QUARTETS in two later places.** §4.1 says *"The
corpus gathers 38 movements of Mozart's String Quartets"*; §4.3 says the weights were fitted *"on an
annotated corpus of 38 Mozart's string quartets"*; Figure 6's caption says *"over the 38 Mozart's
string quartets"*. **Table 3's caption settles it against the later two**: *"the 30 Mozart string
quartets movements in a major key … and the 8 movements in a minor key"*, and 30 + 8 = 38 movements.
**That a quartet has several movements is established inside this paper rather than assumed**: it
names *"the third movement of the string quartet No 3"* (§4.2) and *"Mozart's first movement of
String Quartet No. 13"* (Figure 1's caption). So 38 quartets and 38 movements are different
populations and cannot both be the corpus.

**D-3. The three measures are named one way in the list that introduces them and another way in the
section headings that define them.** The list at §2 names them *pitch compatibility*, *harmonic
anchoring* and *relationship proximity*; the headings are §2.1 *Pitch Compatibility*, §2.2 *Tonality
Anchoring*, §2.3 *Tonality Proximity*. **Two of the three names change between the introduction and
the definition**, two pages apart.

**D-4. The same key relation is called *homonym* in one section and *parallel* in another.** §2.2.1
says the heuristic *"produces false positives for homonym keys"*; §4.2 speaks of *"the parallel C
minor"* and §4.2.2 of false positives *"on parallel keys"*. **They name the same relation — same
tonic, other mode — and a sentence joining the two names is met nowhere in the nine pages as this
side read them.**

**D-5. Figure 2's caption says three diatonic pitch sets are discussed in the text and the text
discusses two.** The caption reads *"The diatonic pitch sets a, b, and c are discussed in the text"*;
§2.1.3 gives values for CS(b) and CS(c) and **says nothing about a**. The label a is drawn on the
figure.

**D-6. The backtracking step is garbled.** The printed second bullet is *"for the preceding beat
b_{B−1}, choose the key k_{B−1} ; that minimizes d_W(k_{B−1}, k′) + D(b_{B−1}, k_{B−1})"*. It
carries a stray semicolon splitting the sentence, and the expression to be minimised is over a
variable k′ that the bullet does not bind, while the key being chosen appears on both sides.
**The step a reader would have to reconstruct is not printed.** This read does not reconstruct it
here, because doing so would put this side's guess where the paper's statement belongs.

**D-7. The cost array is called a likelihood while being minimised.** §3 says *"the value D(b, k)
estimates the likelihood from this key k on the beat b"*, and the other statements about D this read
met — the whole plan's cost, the backtracking, *"optimally minimizes"* — treat it as a cost, where a
larger value means a worse key. **A likelihood that is minimised is the wrong word, not merely an unusual
one.**

**D-8. Table 2's caption asserts a minimality that the paper's own definitions do not give.** The
caption says *"When α = β = 0, then D(b, k) is minimal when each beat is in the main key"*. **Derived
from the paper's own recurrence:** with α = β = 0 the per-beat terms vanish and D(b, k) =
min_{k′}[γ · d_W(k, k′)/w + D(b−1, k′)]; since d_W(k, k) = 0 and D(1, k) = 0 for every k, induction
gives **D(b, k) = 0 for every beat and every one of the 42 keys**. Every constant tonal plan then has
cost zero, and so does the array everywhere. **So the minimum does not single out the main key, or
any key**, and the reported 50.0% must rest on a tie-breaking rule the paper does not state. **This
is this read's derivation from the paper's printed equations, and it bears on a reported number** —
the 50.0% baseline.

**A second site of the same subject, found at the read-back.** §4.2 states *"We thus do not evaluate
independently d_W, but together with D in the next section."* **Table 2's third row sets α = β = 0
and γ = 1, which is d_W evaluated on its own**, under the name *no modulation*. The paper's sentence
and its own table disagree about whether that evaluation was made. **This read takes the table's
row as the act and the sentence as the one that is wrong**, but records both rather than choosing
silently.

**D-9. The initial value of the anchoring measure is stated only in the evaluation section.** §2.2.2
defines c_{V⌣I}(b, k) by a case at b and a recursion on b − 1 and never gives a value at the first
beat; §4.2.3 then asserts *"c_{V⌣I}(0, k) = 0 for all keys"*. **The initialisation is given two
sections after the definition, and at beat 0, where the cost sum and the recurrence both run from
beat 1.**

**D-10. The argument order of D is reversed in Figure 7's caption.** The recurrence and the text
write D(b, k) — beat first; Figure 7's caption writes *"the difference D(k, b) − min_{k′} D(k′, b)"*.
**The body text one column away writes D(b, k) for the same object.**

**D-11. d_diat is written with two different argument kinds.** It is defined on pitch sets,
d_diat(S, S′), and used correctly as d_diat(CS(b), S(k)) in §2.1.3 and in Figure 4's caption; §4.2.1
then writes *"d_diat(b, C♭ minor)"* and *"The best d_diat(b, k) value"*, whose first argument is a
beat and not a pitch set.

**D-12. A key is named without its mode in a worked value.** §2.3 gives *"d_W(D minor, C) = √2"* and
the next sentence calls the same key *"C Major"*. Since the paper's key set contains both C Major and
C minor, the bare name does not identify the argument.

**D-13. The paper's "17.5%" is a difference of percentage points written with a per-cent sign.** See
§6.5. The number is right for what it is; the unit is not what the symbol says.

**D-14. Printed language defects, named rather than counted, recorded because the commission's form
asks for the paper as it stands and not as it was meant.** The abstract's opening, *"Modulations, the
moments where key change"*; *"see, at the end of this paper, Table 3 and discusion"* (§2); *"when a
nonchord tone do appear"* (§4.3 continuation); and *"Note that keys that mostly used by Mozart in the
corpus"* (§4.3). **None of them changes a claim.**

*(★ CORRECTED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "Three printed language defects", above
a list of four. **This is the count tell the user's standing rule of 2026-08-15 names — a number put
on this side's own reading without deriving it — and it is reported at §8.2 and was reported to the
user in the conversation.** Cadence 6 asks for the members to be named and not totalled, and the
heading now names them.)*

**D-15. The paper's own explanation of its 87 false positives is not established by its own table.**
§4.2.2 says *"most of the 87 false positives are on parallel keys and on I → IV progressions"*.
**Table 1 puts 48 of the 87 in an `others` row that names no key at all**, and 24 more in C minor.
The prose does name examples — *"spurious V → I are detected in F Major, F minor, A♭ Major and in
A♭ minor while they are in fact I → IV in C Major and E♭ Major"* — **but it does not say how many of
the 48 those four keys account for.** So the table cannot say what relation 48 of the 87 stand in to
the main key, and the word *"most"* is not checkable at the evidence the paper prints beside it.
**This read takes no position on whether the sentence is true.**

*(★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): the item said only that the `others`
row names no key, and omitted that the prose immediately after it names four example keys. Leaving
that out made the paper look more silent on the point than it is.)*

**D-16. The abstract and §1.3 disagree about what the third measure measures, and §2's own gloss
agrees with §1.3 against the abstract.** The abstract says *"We design three proximity measures to
assess how close the music is from each key."* §1.3 says *"we design two proximity measures to assess
how close the music is from a given key. We also design a measure assessing the smoothness of a
modulation from one key to another."* §2 then says *"We introduce thus three proximity measures to
determine at a beat b "how far" we are from a key k. The first two measures look at previous pitches
and chords, and the third one assesses the plausibility of modulation."* **The third measure, d_W, is
a distance between two KEYS and takes no argument from the music at all** — which §1.3 states
correctly and the abstract does not. **This matters beyond wording**: a reader who takes the
abstract at its word will expect three per-beat music-to-key measures and will not find the
transition term at all — and the transition term is the one §7.3 S-3 shows to be worth about nine
beats of spelling evidence per key change.

*(★ CORRECTED AT THE USER-ORDERED CHECK OF 2026-09-12. FORMER WORDING, PRESERVED (#12): "the
transition term, which is the term the fitted weights make the heaviest (§7.3 S-3)". **Made false
inside this file by the sweep's own correction to S-3**, which struck precisely the reading that a
large γ makes that term the heaviest. A cross-reference that survives the correction of the thing it
points at is the staleness the hundred-and-seventy-first entry's own check reports.)*

**D-17. Table 1 and Table 3 print their false-positive and false-negative columns in opposite
orders.** Table 1's header runs ref, pred, TP, **FN, FP**, F₁; Table 3's runs ref, pred, TP, **FP,
FN**, F₁. **The two tables are three pages apart and their headers are the only thing distinguishing
the columns.** No check this read ran on either table failed on this account (§6.1 to §6.3); the
hazard is for a reader who carries a value across from one table to the other without re-reading the
header, who will swap two quantities.

**D-18. A sufficiency claim is drawn from one movement and the corpus figure for the same feature is
in the paper's own next table.** §4.2.1 closes: *"The current diatonic pitch set alone, therefore,
appears to be sufficient to detect the key at beat b."* The *therefore* points at 243 of 252 beats on
K157.3. **Table 2 measures that same feature alone — its `only d_diat` row, α = 0, β = 1, γ = 0 — at
67.3% on the corpus.** The sentence carries no restriction to the movement it was derived on.

**D-19. §4.2 says Figures 4 and 5 show something they do not carry.** *"Figures 4 and 5 show, for
each beat, the d_diat and c_{V⌣I} measures for a set of selected keys as well as **the combined
optimal measure**."* Figure 4's caption is the pitch compatibility measure, Figure 5's is the
tonality anchoring measure, and **the combined measure is Figure 7, two pages later.**

**D-20. The reference list gives the same conference label two different years.** Entry [16] reads
*"in International Society for Music Information Retrieval Conference (ISMIR 2018), 2018, pp.
90–97"*; entry [17] reads *"in International Society for Music Information Retrieval Conference
(ISMIR 2018), 2019, pp. 259–267"*. **Within one list the label ISMIR 2018 carries the year 2018 in
one entry and 2019 in the next.** This read does not say which is right — it has opened neither
cited paper — only that the two entries cannot both be.

**D-21. The paper spells Lerdahl's name two ways, and the wrong one stands at the place the name is
load-bearing.** §1.2 (PDF page 3) prints *"whereas **Lerdahl** introduced tonal pitch space [8]"*;
reference [8] prints *"F. **Lerdahl**, "Tonal pitch space""*; §2.3 (PDF page 5) prints *"one of the
spaces that **Lerdhal** deduces from his tonal pitch space framework [8]"*. **Three places, two
spellings, and the odd one out is the sentence that grounds this paper's choice of key space.**
*(Found at the cross-check: the first extract had the §2.3 spelling right where this read had
silently repaired it, and putting the three places side by side is what turned one misspelling into
an inconsistency.)*

### §7.2 What the paper leaves without a value — the questions a later reader must not assume are answered

**Q-1. How good is this method against any other key-finding method?** **A comparison against another
algorithm is met nowhere in the nine pages as this side read them**, and §5 lists such comparison as
future work. The three non-best rows of Table 2 are ablations of the paper's own combination.
**So nothing this side met in this paper places its 84.8% against the field.**

**Q-2. How accurately are modulations LOCATED, over the corpus?** Unmeasured. The one positional
statement this side met is *"at most within 2 beats"* on one movement (§4.3 continuation), stated in
prose rather than in a table, and §5 names *"an evaluation of the detected position of each
modulation"* as future work. **The paper's stated motivation is where modulations occur; what its
tables report is whether each beat's key is right, which is a different quantity.**

**Q-3. What does the method cost to run?** A complexity statement, a running time and a memory
figure are met nowhere in the nine pages as this side read them. The array is B × 42 and the
recurrence takes a minimum over 42 predecessors per cell, which
would make it O(B · 42²), **but that is this read's arithmetic from the printed recurrence and the
paper does not state it.** The paper does remark of Chew's approach that *"The complexity of the
approach increases with the number of modulations"* (§1.2) — a comparative point this side met
nowhere applied to its own.

**Q-4. How reliable is the reference annotation?** The corpus carries *"manual annotation of keys and
cadences"* (§4.1), and **an annotator count, an annotator background, an independent second
annotation, an agreement measure and a validation procedure are met nowhere in the nine pages as this
side read them.** The corpus is also the
authors' own, enhanced from their previous work (F-2). **So the ceiling this evaluation is measured
against is not a quantity this paper supplies.**

**Q-5. What would the 84.8% be on held-out data?** Unmeasured, and the paper says so (F-16, C-2).

**Q-6. Is the headline figure pooled over beats or averaged over movements?** Not stated; the two
readings are both present in the paper's own wording. See §6.4.

**Q-7. What are the coordinates (x_k, y_k) of the 42 keys in Weber's table?** Not printed. Figure 3
is *"an extract"*. **So no value of d_W can be recomputed from this paper alone for a pair the text
does not work out.**

**Q-8. Is γ = 4.0 an optimum or the edge of the search?** §4.3 says the search ran over *"values
between 0 and 4"* and reports the best γ as **4.0** — **the upper end of the range searched.**
Figure 6's third panel plots γ over 0 to 4 and shows that curve rising steeply and then flattening
toward its right edge, which is consistent with a plateau, **but no value above 4 was searched and so
nothing is established about what lies there.** α = 0.016 and β = 0.3 sit inside their ranges.
**A second thing about that figure, recorded because it bears on the same question:** its α and β
panels are plotted over 0 to 1, not over the 0 to 4 the text says was searched, so the figure shows
the whole searched range for γ alone.

**Q-9. Where do c = 20 and w = 10 come from?** Declared, not derived (C-6). The paper gives no
sensitivity analysis for either.

**Q-10. Does the method need an upstream chord analysis?** A statement that it does, and a named
chord-identification step, are met nowhere in the nine pages as this side read them, and its V → I
detector is defined on voice leadings. **The negative is not stated in those pages either**, so the
answer at §3.1(e) is this read's inference and not the paper's statement.

**Q-11. What happens on music whose spelling is absent or wrong?** Unmeasured. The paper states the
requirement and states that algorithmic spelling is weakest on the hardest pitches (§3.1(a)), and
reports no experiment on unspelled input.

**Q-12. What does the per-beat margin mean?** Figure 7 plots D(b, k) − min_{k′} D(b, k′) and the
paper reads it qualitatively. **No calibration, no threshold, no statement that the margin is
comparable between pieces or between beats.**

### §7.3 The results in this paper that are both measured and structural

*These are the places where a measured value in this paper says something about how an analysis
should be BUILT, rather than only how well this system did.*

**S-1. A recency-based spelling state beats a no-modulation baseline by a wide margin, alone.** The
pitch-compatibility measure by itself gives 67.3% against the no-modulation baseline's 50.0%
(F-6) — and it does so **with no pitch profile, no histogram and no chord** (§5: *"without any
computation of a pitch profile"*). **What is structural here is the object, not the number**: the
feature is a seven-slot spelling state overwritten by the most recent accidental, and the paper's
claim is that directedness beats prevalence. **That claim is argued and not measured against a
profile-based rival** (C-3, Q-1), so what the 67.3% establishes is that the feature is strong on its
own, and not that it is stronger than a profile.

**S-2. The transition term is what buys temporal stability, and the paper's account of why is
specific.** *"the computation of D, including d_W, favors some stability in the predicted keys,
preventing the algorithm from switching keys for only 1 or 2 beats when a nonchord tone do appear"*
(§4.3 continuation). On K157.3 the combination gets 248 of 252 beats against d_diat alone's 243
(F-7, F-9). **The mechanism named is the transition cost suppressing one- and two-beat key
flicker**, which is a structural role, not a tuning one.

**S-3. What the fitted weights buy, converted into the unit the objective is actually paid in.** The
three weights multiply three quantities each normalised to the interval from 0 to 1, so a weight's
size alone does not say how much a term moves the objective — the term's typical VALUE matters as
much. **This read therefore did the conversion, from the paper's printed weights and printed
constants, and states the arithmetic so it can be checked:**

- **One modulation of Weber-distance 1 costs γ · (1/w) = 4.0 × 0.1 = 0.4.**
- **One beat whose spelling state differs from the candidate key in one letter costs β · (1/7) =
  0.3 ÷ 7 ≈ 0.0429.**
- **So a key change of one step must be repaid by about nine beats each improving by one letter
  before the algorithm will take it** — 0.4 ÷ 0.0429 = 9.3.
- **The anchoring term's ENTIRE range moves a beat's cost by at most α = 0.016**, against at most
  β = 0.3 for the spelling term: a factor of 18.75.

**That last line is the derived form of what the paper says in words** — *"c_{V⌣I} is generally high
and does not significantly help the detection here"* (§4.3) — **and it is stronger than the paper's
wording, because it bounds the term's whole reach rather than describing its typical behaviour.**

*(★ CORRECTED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "The weighted combination is dominated
by the transition term … So the system that gets 84.8% is, by its own fitted weights, principally a
key-transition model with a spelling-compatibility term and an almost inert harmonic term." The
ratios quoted there were right, but reading dominance out of them was not: the transition term is
paid once per key change while the spelling term is paid on every beat, so a large γ does not make
the objective principally a transition model. The arithmetic above replaces the claim with what the
weights actually buy.)*

**S-4. A voice-leading V → I detector, used alone, is a poor key signal — and the paper measures how
poor.** 16.3% on the corpus and 66 of 252 beats on K157.3 (F-6, F-8), with 87 false positives against
29 true positives on that movement (F-10). **The structural cause the paper names is that the
detector cannot separate a key from its parallel, nor V → I from I → IV** (F-15). **The two failure
modes are exactly the ambiguities a detector defined on two of three voice motions cannot resolve**,
and that is a fact about the construction rather than about the corpus.

**S-5. The paper names a direction-specific weakness — the subdominant-related degrees — and its own
table does not rank exactly the way the name implies.** F₁ of 0.12 for ii and 0.63 for IV under a
major main key, and 0.62 for iv under a minor main key (F-13). **ii's 0.12 is the lowest value in the
major table; IV's 0.63 is not, v standing lower at 0.58.** The
paper reports the weakness and declines to explain it:

*(★ CORRECTED AT THE USER-ORDERED CHECK OF 2026-09-12. FORMER WORDING, PRESERVED (#12): "The
subdominant direction is where this method is weakest, on both main modes." Refuted by the v row of
this file's own transcription, exactly as F-13's former wording was, and it is the same error written
twice.)* *"the algorithm has more trouble finding subdominant
related keys (ii, iv and IV), and further research could investigate this behaviour"* (§4.3).
**This read offers no cause either.** It is recorded because it is a measured, direction-specific
weakness in a method whose transition term is a symmetric distance.

**What this read can establish about that, with its ground and its bound.** d_W is a Euclidean
distance, and a Euclidean distance is symmetric, so d_W(k, k′) = d_W(k′, k) for every pair. **In the
extract of Weber's table printed as Figure 3, each column runs downward by descending fifths** — the
third column of the printed rows reads C, F, B♭, E♭, A♭, D♭ — **so a key's subdominant sits one step
below it and its dominant one step above it, at equal distance.** A symmetric measure on that table
therefore assigns the same transition cost to a move to the dominant and a move to the subdominant.
**The paper itself states the asymmetry that its measure cannot express**: for the classical period,
*"the keys that a composer tends to employ are generally associated with the scale degrees of the
main key, prioritizing the dominant, or the relative major for a minor main key"* (§2, citing [21]).
**The bound on this: Figure 3 is an extract, this read inferred its axes from the rows printed
there, and no experiment here connects that property to the measured subdominant weakness.** It is
offered as an observation about what the transition term can and cannot represent, not as the cause
of F-13.

**S-6. The minor mode is weaker, and the paper's own explanation points at its own representation.**
Total F₁ 0.78 on minor-main-key movements against 0.87 on major (F-12), explained as *"mostly
explained by the floating 6th and 7th scale degrees of the minor scale"* (C-4). **The method
represents a minor key by the harmonic minor form alone** (§2.2, §3.3(b)). **So the paper's stated
cause of its minor-mode weakness is a degree of freedom its own expected-pitch-set definition does
not carry.** The paper does not join those two statements; this read does, and offers it as an
observation rather than as a measured cause, because no experiment separating that cause from any
other is reported.

---

## §8 — The read-back and the sweep, written in the act that ran them

*★ THIS SECTION WAS PLACED WRONGLY AT THE FIRST LANDING AND THE MISPLACEMENT IS RECORDED RATHER THAN
SILENTLY REPAIRED (#12). It was inserted between §7.3's S-5 and S-6, splitting §7.3 in two, because
the edit that added it anchored on the end of S-5 instead of on the end of the file. **The landing
proof found it** — the read of the landed copy's last lines showed S-6 standing after §8.4 — and S-6
is now back inside §7.3 where it belongs. **No word of S-6 or of §8 was changed in the move.***

*This section was absent when §0 to §7 were first written, and was added as its own edit after those
two acts, which is the order the hundred-and-sixty-ninth entry's §3 sets. Everything below is about
THIS SIDE'S OWN WRITING, not about the paper.*

### §8.1 What the read-back was

**Every content page of the paper was re-opened against the finished text** — pages 2 to 5 in one
request, 6 to 8 in a second, and 9 alone in a third — because on this paper each of the eight content
pages carries a value, a table or a sentence this file quotes, and page 9 carries the reference
entries §2.2, F-2 and T-1 to T-4 rely on. **Every image was again checked for presence and legibility
at the image.** No page image request made in this sitting returned a missing or illegible image; the
one out-of-range request returned the refusal it was made for and no image. **None of that is
evidence the page-image fault is gone.**

**What the read-back did NOT do:** it opened no other paper, **it did NOT open this paper's first
extract**, it ran no web access, and it swept no repository.

*(★ CORRECTED AT THE USER-ORDERED CHECK OF 2026-09-12. FORMER WORDING, PRESERVED (#12): "it opened no
other paper, opened this paper's first extract, ran no web access, and swept no repository." **A
dropped negation inside a list of negatives, which made the sentence assert the one act the
independence rule forbids before step 7** — and assert it against §0, §9.1 and this file's own
opening block, all of which record that the first extract was not opened until after the second
landing. **The act did not happen; the sentence said it did.**)*

### §8.2 What the read-back and the sweep struck in this side's own writing

**Every correction is made at its own site above, with the former wording preserved (#12), and each
is named here rather than counted.**

**Quotation defects of this side's own making.** The §1.2 quotation was trimmed at its head so that a
paraphrase of this side's supplied the printed subject *"These algorithms"*, leaving a verb that no
longer agreed, and it was closed at *"work by Chew"* with the citation *"[19]"* dropped and no
ellipsis. **A dropped bracket inside a quotation is the exact defect this line has twice recorded
against first extracts**, and it appeared here in this side's own writing on the first attempt.

**A uniqueness claim contradicted by something this side had already read.** §1 asserted that this was
the only paper in the line whose transition term comes from a published key-distance table. This side
has opened no other paper of the slice, and the hundred-and-eighteenth entry — which this side read
at boot — describes row 26's paper as an instance of a tonality-change cost built from a published
key-distance measure. **Struck.**

**A superlative from a comparison never made.** §3.3(c) called the missing held-out split *"the single
most consequential scope limit in the paper"*. **Struck and replaced by what this read can actually
say about the 84.8%.**

**A claim about the paper refuted by the paper two pages away.** §3.3(e) said the position of a
modulation *"is not evaluated"* and that the paper *"does not measure where they were placed"*. The
paper's §4.3 states that on K157.3 the modulations are found *"at most within 2 beats"* of the
annotated place. **The true claim — no corpus-level positional measurement — is now what stands, and
Q-2 was brought into line with it in the same act.**

**An overstated negative about the paper's own evidence.** D-15 said the `others` row names no key,
and omitted that the prose beside it names four example keys. **Corrected.**

**A wrong statement about the held document.** §0 said page 1 *"carries none of the paper's
content"*; it carries the title, the authors and the citation. **Corrected to what it does carry.**

**A structural claim whose ratios were right and whose conclusion did not follow.** §7.3 S-3 read
dominance out of γ being large relative to α and β, without allowing that the transition term is paid
once per key change and the per-beat terms on every beat. **Replaced by the derived arithmetic of
what the weights buy** — the nine-beat repayment figure and the bound on the anchoring term's whole
range — **which is a stronger statement than the one it replaces and rests on the same printed
values.**

**An underived assertion about a symmetric distance.** §7.3 S-5 asserted that a symmetric key distance
cannot prefer the dominant over the subdominant without showing why the two sit at equal distance.
**The ground is now given from Figure 3's own printed rows, with the bound that the figure is an
extract and that no experiment here connects the property to the measured weakness.**

**Negatives stated wider than the act that produced them.** A number of sentences said the paper
*"never"* states a thing or that a thing appears *"nowhere in the paper"*, where what this side did
was read nine page images. **Each is now written in the form the hundred-and-sixty-ninth entry's
cadence 7 asks for — met nowhere in the pages as read — and §2.5's is marked explicitly as a reader's
negative over images rather than a text search**, which this side did not run.

**Counts put on this side's own acts where the members should have been named.** §0's contaminations,
§6.3's list of checks, and D-14's own closing sentence. **All now name rather than total** (cadence
6).

**★ AND ONE DEFECT THE READ-BACK AND THE SWEEP BOTH WALKED PAST, FOUND ONLY AT THE LANDING PROOF.**
**This whole section was landed in the wrong place** — inserted between §7.3's S-5 and S-6, so that
S-6 stood after §8.4 and §7.3 was split in two. Neither the read-back nor the sweep saw it, because
both were passes over the TEXT and this was a defect of the file's structure. **What found it was
reading the landed copy's own last lines as part of proving the landing**, which is a check the
landing step carries for a different purpose. **Carry that:** a proof of content at the head, the
middle and the last line will show a section in the wrong place only if you actually read what the
last line says, rather than searching for a string you expect to be there. Corrected at the second
landing, with the account left at §8's own head.

### §8.3 The degradation tell, reported unprompted

**The user's standing rule of 2026-08-15 asks that a degradation tell be reported without being asked
for. One fired in this sitting, in one instance, and it is the same class the two previous sittings
report: a count put on this side's own reading without deriving it.**

**The instance: §7.1's D-14 was headed *"Three printed language defects"* above a list of four.** It
was caught by the sweep, **before the file landed at all**, and it is corrected at its site with the
former wording preserved.

**What this side did in consequence:** reported it to the user in the conversation **before this file
landed at all**, and did not take a second member this sitting. **The capacity judgment made before the paper
was opened had already fixed one member as this sitting's plan**, so the tell did not change that
plan; it is reported because the rule asks for it and because a next side should know the class is
live on this line for a third sitting running.

**What is NOT claimed:** that the sweep caught every instance. **It is a second pass over the same
writing by the same side, so it establishes what it found and not that there is nothing left.**

### §8.4 The bound on this section

**This section reaches this side's own writing of §0 to §7 and nothing else.** It moved no transcribed
value of the paper's: every figure, table cell, quoted measurement, page number and printed constant
above stands as it was first written, and **the read-back changed no number this file takes from the
paper.** What moved were this side's own claims about the paper, its quotations of the paper, and its
statements about its own acts.

**What this section does not reach:** the first extract of this paper, which is unopened until §9;
any other paper; the repository; and the correctness of the paper's own counts, which would need the
corpus and the reference annotation, neither of which this side holds.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**The first extract was opened for the first time AFTER this file had landed twice** — step 7 of the
hundred-and-sixty-ninth entry's §3 — and was read whole. It is
`reading_pass/extracts/feisthauer-bigo-giraud-leve-2020-estimating-keys-and-modulations-in-musical-pieces.md`,
**34,902 bytes**, written 2026-09-05 by the session that booted on the hundred-and-nineteenth handoff
entry, and it too was read at the object, all nine pages as page images.

**Every disagreement below was resolved AT THE PAPER**, by re-opening the page that carries it: page 5
for the Weber paragraph, pages 7 and 8 for the evaluation sections and Tables 1 to 3. **Nothing was
resolved by preferring one extract to the other.**

**The independence bound, stated rather than claimed away.** The two reads were made in different
sessions under the same commission and by the same kind of reader, which is what the commission's
second route buys and all it buys; and this side had read the record's one-line admission reason for
row 30 before opening the paper (§0). **What this side had NOT read, and the first extract had:** the
progress record, the slice derivation, `FRAMEWORK.md`, the bibliography, row 16's thesis extract, and
rows 26, 28 and 29's extracts. **So on everything that depends on the record, this is not a second
opinion at all — it is silence**, and the first extract is the only read of that half.

### §9.2 One transcribed value disagrees, and the paper goes against the first extract

**This is the first disagreement over a value in this line that this side is aware of from the entries
it read**, and it is recorded plainly.

**Table 3, major main keys, the IV row's F₁.** The first extract lists the per-key values as *"I 0.92,
V 0.89, vi 0.75, **IV 0.68**, i 0.76, v 0.58, ii 0.12, ♭III 0.68"*. **The paper prints 0.63 for IV**
(PDF page 8, Table 3, row IV: 386, 382, 241, 141, 145, **0.63**).

**Resolved at the paper, and established twice over:** the printed cell reads 0.63; and the row's own
counts give precision 241/382 = 0.6309 and recall 241/386 = 0.6244, whose F₁ is 0.6276, which rounds
to 0.63 and cannot round to 0.68. **The first extract's value is wrong**, and the shape of the error
is visible in its own list: it gives 0.68 for IV and 0.68 for ♭III, and 0.68 is ♭III's printed value.

**What it costs.** The IV row is one of the three the paper's own discussion singles out — *"the
algorithm has more trouble finding subdominant related keys (ii, iv and IV)"* — so the wrong value
makes the subdominant weakness look milder than the paper measures it. **A later reader lifting 0.68
would be lifting a value the paper does not print.**

**That file is untouched**, on the standing ground that rewriting another read's text destroys what
the doubling compares. **Whether it is corrected at its own site is the user's**, and it is the same
question this line already carries for rows 27, 28, 1, 8 and 26.

### §9.3 The disagreements inside quotations, in both directions

**Two go against this side, both corrected above at their sites with the former wordings preserved
(#12).**

- **A name silently repaired.** §2.4 quoted *"one of the spaces that Lerdahl deduces"* where the paper
  prints **Lerdhal** at that place. The first extract had it right and marked it as reproduced as
  printed. **Repairing it hid an inconsistency**, which is now D-21.
- **A word dropped from inside a quotation, with no ellipsis.** §5 quoted *"adding the others improves
  the local key detection by 17.5%"* where the paper prints *"adding the others **measures** improves"*.
  **No value moves**, and the dropped word is the one that makes the phrase ungrammatical, so the
  omission tidied the source. The first extract had the word.

**Two go against the first extract, and that file is untouched.**

- **A word inserted and a word dropped in one sentence.** The first extract quotes *"Note finally that
  keys mostly used by Mozart in the corpus are the ones that are directly aside the main key in the
  Weber's table"*. **The paper prints** *"Note that keys that mostly used by Mozart in the corpus are
  the ones that are directly aside the main key in the Weber's table"* (PDF page 8). So *finally* is
  inserted and the second *that* is dropped — **and dropping it removes the grammatical defect that
  made the sentence worth quoting as printed.** **No value moves.**
- **A key named with a mode the formula does not carry.** The first extract writes *"d_W(D minor, C
  major) = √2"*. **The paper prints** *"d_W(D minor, C) = √2"* (PDF page 5), bare. The sentence
  immediately after does say *"towards C Major"*, so the expansion is almost certainly what the
  authors meant — **but it is an unmarked completion inside a value expression, and this paper's key
  set contains both C Major and C minor.** **No value moves.**

**A fifth disagreement that is not a quotation but a characterisation, and the paper goes against the
first extract.** The first extract says Figure 6 plots *"average accuracy against each coefficient
with the other two held at their optimum"*. **The paper's own sentence is** *"Figure 6 shows the
average prediction accuracy of key detection when one coefficient is constant and the two others
changes"* (§4.3). **Held at their optimum and changing are not the same thing**, and the paper's
sentence — whatever exactly it means, and it is not clear — does not say the other two are fixed.
This read's own §7.2 Q-8 describes only what the panels plot and makes no claim about the other two
coefficients, which is what it was entitled to.

### §9.4 What both reads found independently, agreeing

*Recorded because an agreement between two blind reads is evidence, and because the agreements are
what bound the disagreements above.*

- **Every other value both extracts transcribe agrees, digit for digit** — the four Table 2
  percentages and the fitted weights; the Table 1 figures the first extract carries (38, 116, 29 and
  87) and its three F₁ values; Table 3's major-mode totals and its minor-mode totals; the per-key F₁
  values of both halves of Table 3 **except the IV row of §9.2**; and the K157.3 per-beat results
  **243, 66 and 248, each of 252**.

  *(★ CORRECTED AT THE USER-ORDERED CHECK OF 2026-09-12. FORMER WORDING, PRESERVED (#12): "…and every
  K157.3 figure (243, 66, 248, 38, 116, 29, 87 of 252)." **That put 38, 116, 29 and 87 under the
  denominator 252, which is not theirs** — they are V → I counts, not beats — and it said "the Table 1
  counts" where the first extract carries four of that table's figures and not its cells.)*
- **Both reads independently found the printed `172`** where Table 3's minor-mode predicted total
  should read 3172, **and both declined to carry it as a value**, each stating the arithmetic beside
  it. **Neither knew the other had found it.**
- **Both reads independently read Weber's table the same way from Figure 3's extract** — that a key's
  parallel, its relative, its dominant and its subdominant all stand at distance 1. The first extract
  states it as the table's structure; this read draws the consequence (§7.3 S-5).
- **Both reads independently recorded the fit's lack of a held-out split** and quoted the authors'
  own sentence for it.
- **Both reads independently recorded that the paper's own Conclusions name modulation-position
  evaluation as future work**, and that the *"within 2 beats"* statement is about one movement.
- **Both reads independently recorded the paper's 17.5% as a difference in percentage POINTS.**
- **Both reads independently recorded that no comparison with another key-finding algorithm is made.**

### §9.5 What the doubling produced that neither read had alone

**Going one way — what the first extract has and this read has not.** Everything that depends on the
record: the relation of this paper to Feisthauer's 2021 Lille thesis and the 24-keys-against-42-keys
precision that follows from it; that the record cites this paper nowhere but the bibliography, the
candidacy row and the slice row, established by a repository-wide search; the licence-tier precision
for the bibliography; the routing of each finding to a design point; and the placement of the paper
against rows 26, 28 and 29. **This side opened none of those objects and takes no position on any of
it** — this is the half where the doubling bought nothing, and saying so is the point of §9.1's
bound. The first extract also counts the paper's own furniture — seven figures, three tables,
thirty-one references, eight printed pages — which this read did not.

**Going the other way — what this read has and the first extract has not.** Defects inside the paper,
**named rather than counted, and this is not the whole of §7.1 — the notational items D-9 to D-13 and
the evidence item D-15 are there too and are not repeated here**: the corpus given as 38 movements in one section and 38 quartets in two others (D-2); the three
measures named differently in the list that introduces them and in the headings that define them
(D-3); *homonym* and *parallel* used for the same relation (D-4); Figure 2's caption naming three
diatonic pitch sets where the text discusses two (D-5); the garbled backtracking bullet (D-6); a cost
called a likelihood while being minimised (D-7); the abstract's three proximity measures against
§1.3's two-plus-one (D-16); the two tables' opposite FP/FN column orders (D-17); the sufficiency
claim drawn from one movement against the corpus figure for the same feature (D-18); Figures 4 and 5
said to show the combined measure (D-19); the reference list's two years for one venue label (D-20);
and the Lerdahl/Lerdhal inconsistency (D-21), which needed the first extract's correction of this
read to become visible at all.

**And two things that bear on a reported number.** **(i) D-8**: with α = β = 0 the paper's own
recurrence gives D(b, k) = 0 for every beat and every key, so Table 2's caption is wrong that the
minimum puts each beat in the main key, and the 50.0% baseline rests on an unstated tie-break. **The
first extract carries the caption's claim as fact**, listing the row as *"no modulation (γ = 1 alone,
every beat in the main key)"* and, in its results table, as *"main key everywhere"*. **(ii) §7.3
S-3**: converting the fitted weights into the objective's own units gives the figure neither extract
had — **about nine beats of one-letter spelling improvement to repay one Weber-step modulation**, and
a ceiling of 0.016 on what the whole range of the anchoring term can move a beat's cost. The first
extract reads the weights qualitatively (γ *"the largest weight"*); this read converts them.

**The two directions are not symmetrical, and the shape of the asymmetry is worth carrying:** the
first extract is stronger on everything the record says and on routing; this read is stronger on the
paper's internal consistency and on arithmetic derived from its own printed equations. **That is
close to what a reader would predict from the two sessions' declared reach**, and it is not evidence
that either pass is better run.

### §9.6 What the first extract asks of a second pass, and what this check did not do

**The first extract poses one explicit question**, at its Centrality section: it grades the paper
**CENTRAL on a narrow ground** and writes *"A second independent extraction is therefore OWED on this
verdict"*, setting out beside it the ground on which NOT CENTRAL could be argued.

**What this read can answer, and what it cannot.** The centrality argument has two halves. **The half
that rests on the paper alone, this read supports independently**: the paper is a held, working
instance of a key-transition cost built from a published key-relationship construction, with its
weight fitted, its contribution measured term by term, and an outcome on symbolic classical input
with full spelling — and §7.3's S-2 and S-3 are the kind of statement an L2 detail specification
designing a tonality-change term would have to cite or argue against. **This read reached that
judgment without having seen the first extract's verdict.** **The half that rests on the record —
that no ratified text cites the paper, how it stands against rows 26, 28 and 29, and what it does to
DP-K's ground — this side checked NONE of**, and takes no position on it. **So this read confirms the
verdict's paper-side ground and leaves its record-side ground exactly as the first extract left it.**

**The first extract's own stated bound, which this read does not disturb:** its finding (10), that
nothing read contradicts any chosen design point and that no STOP fires. **This read opened no design
point and so neither confirms nor disputes it.**

**What this cross-check did NOT do.** It re-read no page of the paper except the three that carry a
disagreement (pages 5, 7 and 8); it opened no other extract, no other paper, and no file of the
record; it ran no web access and no repository search; and **it edited no file but this one.** It
moved no verdict, routed nothing, and flipped no row. **It is one reader comparing two texts, so it
establishes what it found and not that the two extracts agree everywhere else.**

---

## §10 — The user-ordered fact- and source-check, run after this file had landed three times

**The user's standing rule of 2026-09-12 extends the pre-landing check to landed work on four axes:
completeness, coherence, correctness, and misuse of hyperbole and absolutes, with the corrections
made where needed.** **This file was re-read WHOLE as landed at 91,296 bytes, at the device's own copy
staged back**, and every correction below is made at its own site with the former wording preserved
(#12). **It changed no value transcribed from the paper.**

**★ THE ONE THAT MATTERS MOST: A DROPPED NEGATION THAT MADE THIS FILE CLAIM AN ACT THE INDEPENDENCE
RULE FORBIDS.** §8.1's list of what the read-back did not do read *"it opened no other paper, opened
this paper's first extract, ran no web access…"*. **The second item had lost its negative**, so a
list of negatives asserted that the first extract was opened during the read-back — which would have
broken the eight-step order's step 7, and which this file's own §0, §9.1 and opening block each
contradict. **The act did not happen. The sentence said it did**, and it survived a read-back and a
sweep.

**Two defects of correctness about the paper's own table, and they are the same error written twice.**
F-13 said the algorithm's F₁ is *"lowest on the subdominant-related degrees"* and S-5's heading said
*"The subdominant direction is where this method is weakest"*. **Both are refuted by this file's own
transcription of Table 3, two sections above each: the v row carries 0.58, below IV's 0.63.** What is
true, and now stands at both sites, is that ii's 0.12 is the lowest value in the major table, iv's
0.62 the lowest in the minor, and IV's 0.63 is neither — and that *subdominant-related* is the
paper's own grouping and not this read's ranking.

**A quotation corrected in one place and left standing in another.** The cross-check corrected §5's
quotation of the paper's 17.5% sentence to carry the printed word *measures*. **The same sentence is
quoted again at §6.5, and the correction did not reach it.** Now corrected there too.

**A cross-reference made false by this file's own earlier correction.** D-16 closed by calling the
transition term *"the term the fitted weights make the heaviest"* and citing §7.3 S-3 for it — **where
the sweep had already struck exactly that reading out of S-3.** Replaced by what S-3 now says.

**A sentence left stranded by where a correction note was inserted.** §3.1(e)'s closing sentence had
been cut off from its paragraph by the read-back's own correction note and began with the bare words
*"The measure"*. Moved back, with nothing reworded.

**Two defects in this file's account of what the two reads share.** §9.4's first bullet put four
V → I counts under the denominator 252, which is not theirs, and called them *"the Table 1 counts"*
where the first extract carries four of that table's figures rather than its cells. §9.5's list of
defects this read found and the first did not was given without a bound, reading as the whole of §7.1
when it names neither D-9 to D-13 nor D-15.

**One piece of invented vocabulary.** §9.1 said the two reads *"share a reader's institution"*, which
is a phrase of this side's own making for a thing the record has plainer words for. **`CLAUDE.md`
Conventions forbid self-invented jargon**; replaced with what it was reaching for.

**A grammatical defect introduced by an earlier correction.** D-7's subject was changed from singular
to plural at the sweep and its verb was not.

**A pointer that named the wrong section.** §5 said the minor table's printed total is *"discussed at
§7.1"*; the arithmetic that shows it inconsistent is at §6.3, and §7.1 is where it is reported as a
defect. Both now named.

**What this check did NOT do.** It fetched no page image, opened no paper, **opened the first extract
not at all**, ran no web access, swept no repository, and **edited no file but this one and an
amendment to the hundred-and-seventy-third handoff entry**, whose (xi) carried a first-ness claim
wider than the entries this side had read. It moved no verdict, routed nothing, and flipped no row.
**Every figure, table cell, quoted measurement, page number and printed constant this file takes from
the paper stands exactly as it was landed.**

**What it does NOT establish.** **It is a further pass over the same writing by the same side.** It
found what it found — including two defects that a read-back and a sweep had both walked past, one of
them a reversed statement about this side's own compliance — and **nothing about it establishes that
the remainder is clean.**

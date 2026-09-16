# EXTRACT — Chew, "The Spiral Array: An Algorithm For Determining Key Boundaries" (the held document, for the bibliography's ICMAI 2002 chapter) — Task B candidacy row 29, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-05).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All fourteen pages of the held PDF were read AT THE OBJECT: staged through the bridge
> and read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.**
> The held document prints no page numbers; every location below is the page's position in the held
> file (p. 1 to p. 14) and the paper's own section.
>
> **Why this paper and its place in L2's slice.** It is row 29 of `reading_pass/candidacy_upgrades.md`,
> ADMITTED there as *"A method that places tonality boundaries — DP-E's question — in a continuous
> space rather than over discrete labels."* `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4
> places it in L2's slice: *"Places tonality boundaries — DP-E's question."* It is ninth in group 1 of
> the proposed reading order ("the joint tonality-and-chord decision") and the seventh member read
> (rows 2 and 44 being unreadable from here). **The record cites this paper nowhere else:** a `Grep` of
> the staged tree (`FRAMEWORK.md`, the findings surface, the bibliography, the candidacy derivation, the
> slice derivation) for "Chew" and "spiral array" found only the bibliography row, the candidacy row
> and the slice row. Ruling 1 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate:
> no derivation before L2's slice of Task B is read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — with one finding

Elaine Chew, University of Southern California, Integrated Media Systems Center, Daniel J. Epstein
Department of Industrial and Systems Engineering, "The Spiral Array: An Algorithm For Determining Key
Boundaries". **The printed title and author match the bibliography's row** (`docs/research_papers/
BIBLIOGRAPHY.md` line 43: *Chew, "The Spiral Array: An Algorithm for Determining Key Boundaries," ICMAI
2002 | (Springer LNAI 2445) | ✓ | PAYWALL*). **The held document prints NO venue, NO year, NO
copyright line and NO page numbers anywhere** — it is set in the Springer LNCS/LNAI typeface and
structure (numbered Definitions, "Fig." captions, a Springer-style reference list) but carries no
running head or chapter marking. Fourteen pages; six sections (Introduction; A Mathematical Model for
Tonality — 2.1; An Algorithm For Finding Key-Change Boundaries — 3.1, 3.2; Two Examples — 4.1, 4.2;
Conclusions; Acknowledgements), five figures, twenty-two references, no tables.

**File:** `docs/research_papers/chew_2002_spiral_array_key_boundaries.pdf` (189,010 bytes at the
listing). **Whether the held document is the LNAI 2445 chapter as published, or an author's version
of it, is not establishable from what is held.** Routed to the bibliography reconciliation as an
identity finding of a milder shape than rows 28's and 3's (title and author match; only the version is
unestablished); see finding (1) below. The bibliography row's own two cells — held (✓) and PAYWALL —
are noted there too.

## Claims, labeled

### What the method decides, and from what

**★ [FACT, p. 1, Abstract and §1] The method decides WHERE THE KEY CHANGES, for a GIVEN number of
changes, and the key of each resulting segment; it decides no chord.** *"This paper proposes a
Boundary Search Algorithm (BSA) for determining points of modulation in a piece of music using a
geometric model for tonality called the Spiral Array. For a given number of key changes, the
computational complexity of the algorithm is polynomial in the number of pitch events."* (p. 1.)
*"This paper proposes a method for segmenting a piece of music into its respective key areas using the
Spiral Array model."* (p. 1, §1.) And, in the Conclusions: *"The BSA does not explicitly use chord
functions to determine the key areas. Chord membership and functional relations to each key area are
incorporated into the Spiral Array model by design."* (p. 12, §5.)

**★ [FACT, p. 7, §3.1] The input is a collection of pitch events with pitch and duration, and NOTHING
ELSE — no order, no beat.** *"A musical passage consists of a collection of pitch events, each comprising
pitch and duration information."* The centre of effect of N notes is the duration-weighted average of
their Spiral Array positions: **c = Σᵢ (dᵢ/D)·pᵢ, D = Σᵢ dᵢ.** The Conclusions state the omission in
terms: *"the c.e. defined in Section 3.1 summarizes only pitch and duration information. The method
does not account for pitch order within each data set, nor does it incorporate beat information."*
(p. 12, §5.)

**★ [FACT, p. 3, §2.1] The pitch representation is SPELLED — indexed by perfect fifths from C on a
spiral, not a toroid — so the method CONSUMES spelling.** *"Each pitch class is indexed by its number of
perfect fifths from an arbitrarily chosen reference pitch, C (set at position [0,1,0]). An increment in
the index results in a quarter turn along the spiral. Four quarter turns places pitch classes related by
a major third interval in vertical alignment with each other. Strict enharmonic equivalence would
require that the spiral be turned into a toroid. The spiral form is assumed so as to preserve the
symmetry in the distances among pitch entities."* Definition 1 (p. 4): P(k) = [r sin(kπ/2), r cos(kπ/2),
kh].

### The tonality representation (p. 4–6, §2.1, Definitions 2–4)

**[FACT, p. 4, Definition 2]** A major triad is the convex combination of its root, fifth and third
positions, C_M(k) = w₁·P(k) + w₂·P(k+1) + w₃·P(k+4), with w₁ ≥ w₂ ≥ w₃ > 0 summing to 1; a minor triad
C_m(k) = u₁·P(k) + u₂·P(k+1) + u₃·P(k−3) likewise. *"The weights are constrained to be monotonically
decreasing from the root, to the fifth, to the third to mirror the relative important of each pitch to
the chord."*

**★ [FACT, p. 5, Definition 3] A major key is the convex combination of its I, V and IV chord
representations,** T_M(k) = ω₁·C_M(k) + ω₂·C_M(k+1) + ω₃·C_M(k−1), ω₁ ≥ ω₂ ≥ ω₃ > 0 summing to 1 —
*"The weights are constrained to be monotonically decreasing from I to V to IV."* **[FACT, p. 5–6,
Definition 4]** A minor key is T_m(k) = v₁·C_m(k) + v₂·[α·C_M(k+1) + (1−α)·C_m(k+1)] + v₃·[β·C_m(k−1) +
(1−β)·C_M(k−1)], with α and β modelling *"the relative importance and usage of V versus v and iv versus
IV chords respectively in the minor key."*

**★ [FACT, p. 6, §2.1] The parameter values used, and their justification — hand-set, by stated
conditions, not fitted.** *"For the two examples in this paper, the key representations in the Spiral
Array were generated by setting the weights (w, u, ω, v) to be the same and equal to [0.516, 0.315,
0.168], h = √(2/15) (r = 1). α is set to 1 and β to 0. These weights satisfy perceived interval
relations, such as, pitches related by a distance of a perfect fifths being closer than those a major
thirds apart, and so on. In addition, these assignments also satisfy two other conditions: two pitches
an interval of a half-step apart generates a center that is closest to the key of the upper pitch; and,
the coordinates of a pitch class is closest to the key representation of the same name."*

### The algorithm (p. 7–8, §3)

**★ [FACT, p. 7, §3.1] The key of a passage is the NEAREST key representation to its centre of effect;
the distance is the likelihood indicator.** *"the most likely key of the passage is given by: arg
min_{T∈𝐓} ‖c − T‖, which can be readily implemented using a nearest neighbor search. The likelihood that
the pitch collection is in any given key is indicated by its proximity to that key."* d^min = min_T ‖c − T‖.

**★ [FACT, p. 8, §3.2] THE BOUNDARIES AND THE KEYS ARE DECIDED TOGETHER BY ONE OBJECTIVE — the sum over
segments of each segment's minimum distance — for a GIVEN m, by enumeration.** *"Suppose that m
boundaries have been chosen … Our hypothesis is that the best boundary candidates will segment the
piece in such a way as to minimize the distances d^min_(Bᵢ,Bᵢ₊₁), i = 0, …, m. Hence, the goal is to find
the boundaries (B₁, …, B_m) that minimize the sum of these distances."* The system: min Σᵢ₌₀^m
d^min_(Bᵢ,Bᵢ₊₁) subject to each segment's c.e. being the duration-weighted mean of its own pitch events
and Bᵢ < Bᵢ₊₁. *"A naive and viable approach to the problem is to enumerates all possible sets of
boundaries and evaluates each objective function value numerically … the computational complexity of
this approach is O(nᵐ)"*, n being *"the number of event onsets"* (p. 2, §1). **The candidate boundary
positions are therefore the note onsets, and the number of key changes m is an INPUT, not a decision:**
*"Realistically speaking, the number of key changes, m, is typically a small number in relation to the
number of event onsets, n. The two Bach examples each contain one point of departure and one return to a
primary key area, that is to say, m = 2."* (p. 3, §1.)

**[FACT, p. 8, §3.2] Two constraints from "music knowledge and a little common sense":** adjacent key
areas distinct (Tᵢ ≠ Tᵢ₊₁), and for a complete piece the first and last key areas the same (T₁ = T_{m+1}).
The reduced m = 2 instance (p. 9) adds T₁ = T₃ ≠ T₂ and 0 = B₀ < B₁ < B₂ < B₃ = L.

**[FACT, p. 12, §5] A real-time form is sketched, not built:** *"in a real-time system, analyses can
be performed at each time increment and the number of boundaries, m, allowed to increase by at most
one."*

### The two examples (p. 9–12, §4) — no measurement

**★ [FACT, p. 9, §4] The whole evaluation is two pieces against one human expert, with no figure.**
*"In both instances, the BSA method identified the correct keys, T₁(= T₃) and T₂(≠ T₁), and determined
the boundaries B₁ and B₂. These boundaries are compared to a human expert's choices. The BSA's boundaries
(A1, A2) and the expert's choices (EC1, EC2) are close but not identical in both cases."*

**[FACT, p. 9–11, §4.1, Minuet in G.]** Middle section in D major. **A1** is placed at the beginning of
bar 20, where the D-major context is *"established conclusively"*; **EC1** is earlier, at bar 19, which
*"is heard retroactively as being in the key of D major rather than G"* and which *"prioritizes phrase
symmetry by delineating a 2-bar + 2-bar phrase structure."* The author's own words on A1: *"This choice,
in fact, agrees with the textbook definition of modulation."* (p. 10.) On the return: **EC2** at the
barline after bar 24 (the expert *"waited for the latest phrase to end"*, locking to the four-bar
period); **A2** groups beats two and three of bar 24 with the final G-major section, *"a choice that is
closer in spirit to the textbook solution"* — *"the C♮ is the first note that belongs to G major and not
D. Thus, the textbook boundary would start the G major area on beat three of bar 24."* The author's
verdict: *"Both the algorithm's and the expert's choices for modulation boundaries are valid for
different reasons. The human expert's choices involved retroactive decisions that framed past
information in the light of present knowledge. The human's choices were also influenced by phrase
structure … The BSA considered only the pitch events, taking the pitches literally."* (p. 10–11.)

**[FACT, p. 11–12, §4.2, Marche in D.]** *"a less than perfect example with which to test an algorithm
that looks for boundaries between only three parts"* — the return from A major passes through hints of G
major, E minor and B major before D major returns in bar 18. **A1 ≈ EC1** at bar 6 (the BSA *"breaks up
the phrase structure in bar 6 to include the last beat in the new A major section"*; the author notes a
textbook boundary would begin at the G♯ on the first beat of bar 6). **A2 (bar 16) and EC2 (bar 18)**
*"differed quite a bit"*: the expert followed the sequential pattern from the middle of bar 13 to the
climax in bar 16; *"The BSA, on the other hand, did not account for figural groupings and sequential
patterns in the notes. It chose, instead, to begin the last D major section as soon as the note material
of the third part agreed with the pitch collection for D major."*

**★ [FACT, p. 3 §1; p. 12–13 §5] The author's stated conclusion about human key-boundary perception.**
*"the human's perception of key boundaries is influenced by phrase structure"* (p. 3); *"The mind also
organizes music data into figural groupings and phrase structures, and it can sometimes revise prior
assessments based on new information."* (p. 13.)

## Measured results, as the paper states them

**None in the sense the commission's form asks for.** No corpus, no metric, no value: two pieces from
the *Little Notebook for Anna Magdalena Bach*, m = 2 given, keys reported correct and boundaries compared
qualitatively (bar and beat) with one expert's and with "the textbook" placement. The weight vector is
hand-set by stated conditions (p. 6), not fitted. The author's own scope statement: *"the algorithm
works best when n is large and m is small"* (p. 2).

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** Spelled pitch events (the spiral is indexed by fifths and is
deliberately not a toroid) with durations; a passage whose number of key changes m is supplied; for a
complete piece, that it begins and ends in the same key. It reads no chords, no beat, no metre, no
pitch order within a segment, no phrase structure and no voices.

**What it HANDS downstream.** m boundary positions (at note onsets) and m+1 key labels (major or minor,
nearest key representation), with each segment's minimum distance as a likelihood indicator. No chord,
no degree, no chord-tone assignment, no alternatives (the enumeration scores every boundary set but the
paper reports only the minimiser), no probability.

**Its own STATED SCOPE and limits.**
- **Domain:** notated music; the examples are two short Bach keyboard pieces.
- **Vocabulary:** 24 major/minor keys (the finite set 𝐓); triads only in the representation.
- **Granularity:** a boundary may fall at any note onset; the number of boundaries is given, not decided.
- **Coupling:** tonality decided ALONE, from pitch-and-duration content, with no chord decision anywhere
  — *"does not explicitly use chord functions"* — so there is no tonality–chord coupling to be soft or
  hard.
- **Fitting:** none; the parameters are set by stated perceptual conditions and used unchanged on both
  examples.
- **Complexity:** O(nᵐ) by enumeration; polynomial for fixed m.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adapt (a precedent for deciding boundaries WITH labels on the tonality axis by one objective):** the
  BSA scores every candidate boundary set on a summed per-segment fit and takes the global minimiser —
  DP-C's "with" shape applied to tonality, and an instance of the L2 charter's rule that no rival is
  discarded before the whole sequence is scored. What it lacks — a decided m, a decided chord, any
  transition cost between keys — is exactly what an L2 detail specification would have to add.
- **Adapt (a tonality-distance construction that is a REPRESENTATION, not a fitted table):** key as a
  convex combination of I, V and IV chord points in a fifths-indexed space, with distance as the
  likelihood indicator. The criterion admits a paper for its method, not its representation; what is
  adoptable here is the method's stated property that the distance is a likelihood indicator without a
  probability, which an L2 score would have to relate to its other terms.
- **Adapt (a consumer of L0's given spelling):** the spiral, not a toroid, uses the spelled pitch; a
  design that consumes spelling as the L0 contract supplies it has a published precedent here (DP-F's
  chosen position, that spelling is given, is what makes this usable).
- **Must argue against:** tonality decided alone and first, from pitch content, with no chord decision —
  the excluded time-scale decomposition (`FRAMEWORK.md` §S4(b), DP-B) in its purest form; the number of
  key changes supplied as input; a boundary admissible at any note onset with no reference to a harmonic
  boundary (DP-E's rival, *"an independent tonality track changing anywhere"*, here restricted to onsets);
  pitch order and beat discarded; no key-transition cost of any kind (every change is free, and only the
  given m limits their number); the single-minimiser output.

## ★ Findings, routed and not applied

**(1) IDENTITY: the held document prints no venue, year or copyright line.** Title and author match the
bibliography's ICMAI 2002 / LNAI 2445 row; whether the held file is the chapter as published or an
author's version is not establishable from what is held. The bibliography row records it as both held
(✓) and PAYWALL, which is consistent only if the held file is not the publisher's copy. Routed to the
bibliography reconciliation beside rows 28's and 3's findings. Nothing in the record cites this paper
for any claim, so nothing is affected.

**(2) The candidacy row's reason is CONFIRMED and two precisions are added.** The row admits the paper
as a method that *"places tonality boundaries … in a continuous space rather than over discrete
labels."* At the object: (a) the boundaries are placed jointly with the key labels by one objective, but
**the number of boundaries is an input**, so the method answers DP-E's *where* only after being told
*how many*; and (b) **it decides no chord at all**, so its answer to DP-E's *"decided with the
chords?"* is the rival's (tonality alone), and its place in group 1 ("the joint tonality-and-chord
decision") is as the group's rival shape — the same precision recorded for row 26. The ADMITTED verdict
stands (a rival is admitted under the derivation's own consequence (i)); the group placement is left as
it stands, "stated, not ruled".

**(3) A joint boundary-and-label objective on the tonality axis, solved exactly, with no transition
cost.** A published precedent for DP-C's "with" shape carried onto the tonality decision, and for the
charter's no-early-discard rule; also a published instance of the opposite of a change cost — every key
change is free and only the supplied m bounds their number. Routed to L2's detail specification beside
rows 26's and 28's tonality-change-cost findings, with no verdict.

**(4) A SECOND statement that key-boundary placement is governed by phrase structure and retroactive
re-hearing, this time from a symbolic-input method compared bar by bar against an expert.** Row 26's
extract carries the first (the authors' attribution of their errors to missing phrase and cadence
context, from a chord-symbol input). Here the author states it
as her conclusion and shows it at four boundaries on two pieces: the expert's boundaries lock to phrase
periods and re-hear a bar retroactively, the algorithm's fall where the pitch content first agrees with
the new key. ENRICHES-shaped for DP-E's chosen point (a tonality change located at a harmonic boundary,
decided with the chords) and for the L1/L3 phrase evidence split; routed to the findings surface's DP-E
block and to the phrase-boundary primitive's owner.

**(5) The expert's boundary and "the textbook" boundary DIFFER on both pieces, by the author's own
account.** On the Minuet the algorithm's bar-20 choice *"agrees with the textbook definition of modulation"*
while the expert's is at bar 19; and *"the textbook boundary would start the G major area on beat three
of bar 24"* while the expert's is at the barline after bar 24 and the algorithm's at beat two. This is a direct, on-repertoire instance of
the record's DP-K further ground that annotation traditions differ in where a key is placed, and of
principle #21 (the ground truth is a measurement tool with its own variance) — here with n = 1 expert and
no agreement figure. Routed to measurement design beside OI-179; no verdict.

**(6) No measurement, so bounded weight.** Two pieces, one expert, no metric, hand-set weights, m
supplied. As with row 7, this decides how much load the paper can carry rather than criticising it: it
can stand as a precedent for a design shape (finding (3)) and as a rival instance (finding (2)), not as
evidence of accuracy.

**(7) A property of the representation, stated by the paper, that bears on C36 — recorded as an
OBSERVATION with no verdict.** The paper's stated conditions include that *"the coordinates of a pitch
class is closest to the key representation of the same name"*, and its key point is a convex combination
weighted most heavily (0.516) on the tonic chord, itself weighted most on its root. C36 (`FRAMEWORK.md`
§4.2, cited at DP-B) argues that a tonality model rating candidates by characteristic and leading tones
rates the true tonality lowest where the tonic triad is prolonged. A representation whose key point is
built mostly from the tonic triad does not have that failure mode by construction. **This is this
reader's reading of the geometry, not a claim the paper makes, and it is unmeasured — CONJECTURE.**
Routed to L2's detail specification as a question to check if a tonality-distance term is ever designed;
it moves nothing at DP-B.

**(8) No falsifier.** Nothing read contradicts any CHOSEN design point; the paper is a pure instance of
the excluded tonality-first decomposition and of DP-E's rival, and reports no measurement against which
any chosen point's ground could be tested. **No STOP fires** under the remedial commission's §5.

## Centrality

**NOT CENTRAL, challengeable at the progress record.** No ratified text cites this paper; it reports no
measured result; its parameters are hand-set; and the design elements it exhibits that an L2 detail
specification could cite have primaries or owners elsewhere — the joint boundary-and-label objective
(rows 10 and 11, the segmental and semi-Markov formalisms, DP-C's primaries), the tonality-distance idea
(the R-8 primary and row 5), the phrase-structure finding (row 26). What is distinctively its
own — the Spiral Array geometry — is a representation, which the criterion says is not itself an
upgrade, and its primary is the author's dissertation ([6], Chew 2000), which is not in the bibliography.
**The ground on which this could be argued CENTRAL, stated so the challenge is easy to make:** row 26
was graded central because it is a held, working instance of a tonality-distance term whose primary is
the R-8 gap; this paper is a held, working instance of a different tonality-distance construction whose
primary is likewise not held. The difference taken here is that row 26's construction is built from the
R-8 primary's own tables and carries a measured outcome, while this paper's is built from its own
unheld dissertation and carries none. A second independent extraction is therefore **not owed** on
this verdict.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (7) are routed and written
nowhere else. It does not fetch the LNAI 2445 chapter or Chew 2000. It opens no code, touches no
measurement tool, no corpus, no golden and nothing under `tools/`. It writes no open-items row and
allocates no decisions-register identity. It reads no other paper and takes no decision about the order
of the remaining slice.

---

*Provenance: written 2026-09-05 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_seventeen.md`, in the sitting after it read and landed row 26 and
the hundred-and-eighteenth entry, on the user's "continue", after the ordinary session-start read
(`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived gating answer). Read for this
extract, at the files: `reading_pass/candidacy_upgrades.md` row 29 (line 91; the file read whole earlier
this session), `cowork_l2_task_b_slice_derivation_2026_09_05.md` at its row 29 (line 74),
`docs/research_papers/BIBLIOGRAPHY.md` at line 43, the progress record whole (its landed copy, re-staged
and read back), and a `Grep` of the staged tree for "Chew" and "spiral array", which found no citation of
this paper in `FRAMEWORK.md` or the findings surface. The paper itself was read at the object as page
images, all fourteen pages. No shell command was run on the repository or on any staged copy of it for
content or for listings. No figure of this project's own measurement is restated (#17f, D-431); every
value above is the paper's own.*

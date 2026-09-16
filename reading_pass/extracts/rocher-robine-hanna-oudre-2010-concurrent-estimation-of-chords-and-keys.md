# EXTRACT — Rocher, Robine, Hanna & Oudre 2010, "Concurrent Estimation of Chords and Keys from Audio" — Task B candidacy row 27, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-05).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All six printed pages (pp. 141–146) were read AT THE OBJECT: the held PDF staged
> through the bridge and read with the file tools as page images. **No relay, no web-fetch read, no
> prompted extraction.** Every quotation below was read from the page and carries its printed page
> number.
>
> **Why this paper and why first in L2's slice.** It is row 27 of `reading_pass/candidacy_upgrades.md`,
> ADMITTED there as *"the primary of DP-B and of the soft-versus-hard coupling the L2 charter fixes …
> admitted for the coupling design, not the figures."* It heads group 1 of that file's proposed reading
> order ("the joint tonality-and-chord decision"), and `cowork_l2_task_b_slice_derivation_2026_09_05.md`
> §4 places it in L2's slice as *"the primary of DP-B and of the soft-versus-hard coupling the L2 charter
> fixes."* Ruling 1 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate: no derivation
> before L2's slice of Task B is read. This is the first member of that slice read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Thomas Rocher, Matthias Robine, Pierre Hanna (LaBRI, University of Bordeaux) and Laurent Oudre
(Institut TELECOM, TELECOM ParisTech), "Concurrent Estimation of Chords and Keys from Audio",
*Proceedings of the 11th International Society for Music Information Retrieval Conference (ISMIR
2010)*, pp. 141–146. © 2010 International Society for Music Information Retrieval.

**File:** `docs/research_papers/rocher_robine_hanna_oudre_2010_ismir_concurrent_chords_keys.pdf`.

## Claims, labeled

### What the method decides, and how it decides it jointly

**★ [FACT, p. 141]** The stated contribution, in the authors' words: *"The main contribution of this
paper relies on the fact that both chord and key can benefit from each other's estimation, as chords
bring out information about local key and vice versa. We present a new system estimating simultaneously
both chord and key sequences from audio. The proposed method is both template-based and music-based and
no training is required."*

**[FACT, p. 141–142]** Four steps: chroma vectors computed from audio; a set of harmonic candidates
selected per frame; a weighted acyclic graph of harmonic candidates built; a dynamic-programming pass
selects the best path, and the chord and key sequences along it are output (§2, Figure 1). A
post-filtering of the output sequence corrects some remaining errors (p. 142, §2.5 p. 143).

**★ [FACT, p. 142, §2.2] The unit of decision is a PAIR.** *"A harmonic candidate is a pair (C_i, K_i),
where C_i (resp. K_i) represents a potential chord (resp. local key) for the ith frame of audio
signal."* The state the search runs over is the joint chord-and-key state, not either alone.

**[FACT, p. 142–143, §2.2.1–§2.2.2] How the candidates on each axis are found — independently.**
Chords: 24 templates (12 major and 12 minor triads), binary profiles, e.g. major triad
`(1,0,0,0,1,0,0,1,0,0,0,0)`, scored against a 12-dimensional chroma vector by scalar product
`C_{T,V} = Σ_{i=1}^{12} T[i]·V[i]`; the *n* highest-correlated chords become the chord candidates for the
frame. Keys: the same approach with the key profiles of Temperley 1999 (the paper's [18]), *"but with
larger time frames as keys have a larger time persistence than chords"* — Major
`(5, 2, 3.5, 2, 4.5, 4, 2, 4.5, 2, 3.5, 1.5, 4)`, Minor `(5, 2, 3.5, 4.5, 2, 4, 2, 4.5, 3.5, 2, 1.5, 4)`;
24 keys.

**★ [FACT, p. 143, §2.2.3] The candidate set is the full product, and a compatibility filter was
tried and rejected — in the authors' own words.** *"The harmonic candidates finally enumerated are all
the possible combination of previously selected keys and chords. If n chords and m keys are selected
for a given audio frame, n × m pairs are enumerated. … A different choice can be made, by considering
a compatibility between chords and keys. But an incorrect chord selected may discard the correct key
(and vice versa), because the two are not compatible. For this reason, adding a compatibility between
chords and keys has led to a decrease of accuracy."* **The sentence carries no value** — no table and
no figure accompanies it; it is a stated outcome of a variant the authors declined.

**★ [FACT, p. 143, §2.3] The coupling lives in the TRANSITION COST, and it is a theory-derived
distance, not a fitted table.** Each edge between consecutive frames' candidates is weighted by
Lerdahl's distance (the paper's [11], *Tonal Pitch Space*, 2001) from `x = (C_x, K_x)` to
`y = (C_y, K_y)`: `δ(x → y) = i + j + k`, *"where i is the distance between K_x and K_y in the circle of
fifths, j is the distance between C_x and C_y in the circle of fifths and k is the number of non-common
pitch classes in the basic space of y compared to those in the basic space of x."* It *"provides an
integer cost from 0 to 13"*. Because the integer range *"induces a lot of equality scenarios"*, the cost
is modified to `i^α + j^β + k` with `α > 1` *"to discourage immediate transitions between distant keys,
and encourage progressive key changes, since modulations often involve two keys close to each other in
the circle of fifths"*, and `β > 1` for the same reason with chords. *"After experiment, α and β have
been set to 1.1 and 1.01."*

**[FACT, p. 143, §2.4]** The best path is found by dynamic programming (Bellman); per candidate, only
the incoming edge minimising the accumulated cost is kept; the final path is the minimum-total-cost path
over the whole piece. *"This path is outputted by the program."*

**[FACT, p. 143, §2.5]** Post-smoothing: a short run of a different label inside a run of one label
(the paper's example `…AABAA…` → `…AAAAA…`, `…AAABCAAA…` → `…AAAAAAAA…`) is overwritten. Its motivating
case is a *"blue note"* flattened third making a major passage read minor for a frame.

### The input representation (audio-specific; the domain caveat of the admission)

**[FACT, p. 142, §2.1]** Input is chroma from audio: 36-bin chroma with a per-frame shift for tuning
variation (§2.1.1); several chromagrams of different window sizes sharing one hop size (§2.1.2, the
*multi-scale* approach), because *"Longer chromas may bring out different information for key analysis,
and different set of sizes for shorter chromas may fit different tempos …"*; median filtering over a
window of 9 chromas (§2.1.3; best window at p. 144). The three scales used for chords (p. 144, §3.3):
long 32768 samples (≈0.8 s) with 8192 hop; medium 8192 (≈0.2 s) with 8192 hop; short 4096 (≈0.1 s)
with 4096 hop.

## Measured results, as the paper states them

**Corpus (pp. 143–144, §3.1):** the Beatles audio discography, **174 songs**, 44100 Hz; *"the average
number of chord changes by song is 69, with an average of 7.7 different chords by song. The average
number of different local keys by song is 1.69."* Chord transcriptions by Harte and the MIR community;
key annotations by C4DM; both at isophonics.net.

**Evaluation (p. 144, §3.2):** only the root and the major/minor mode of a chord are scored; every
ground-truth chord is mapped to a major or minor triad, and one without a third is compared on root
alone; silences and no-chords are ignored (*"the chord/no-chord detection issue has not yet been
addressed"*). Frames of approximately 100 ms (4096 samples); the estimate is compared to the ground
truth at the frame centre; the score is the proportion of frames matching. **The local-key evaluation
is identical in form.**

**Table 1, p. 144 — chord: number of candidates per frame against filtering (long chromas).** *Ratio
of correctness* is the proportion of frames where the correct chord is among the candidates — the
system's theoretical maximum; *System* is the output accuracy.

| | n = 1 | n = 2 | n = 3 | n = 4 |
|---|---|---|---|---|
| No filtering — ratio of correctness % | 58.3 | 71.5 | 78.6 | 82.9 |
| No filtering — system % | 58.3 | **64.9** | 64.1 | 62.2 |
| Filtering — ratio of correctness % | 68.4 | 79.1 | 85.5 | 88.9 |
| Filtering — system % | 68.4 | **70.0** | 64.3 | 59.3 |

**★ [FACT, p. 144, §3.3.2] Admitting more candidates from the SAME chroma lowers the output accuracy
while raising the ceiling.** *"we notice the drop of the system's performance when the number of
selected candidates per frame exceeds two. This can be explained by the close relationship existing
among the highest correlated chord candidate of a given chroma vector. Indeed, chord templates of two
major and minor chords sharing the same root note often induce a close correlation score for a given
chroma. The same goes for any couple of chords close to each other in terms of Lerdahl's distance. In
80% of the frames, top 2 correlated chord candidate have a distance less or equal to 1 on the circle of
fifths."*

**Table 2, p. 145 — candidates drawn from chromas of different sizes.** Tri-candidate = the two best
candidates from the two adjacent short chromas centred in a long chroma, plus the long chroma's best;
bi-candidate = the medium chroma's best plus the long chroma's best.

| Tri-candidate | none | long | short | both |
|---|---|---|---|---|
| Ratio of correctness % | 69.8 | 78.2 | 76.6 | 79.1 |
| Distinct chords (avg.) | 1.86 | 1.95 | 1.43 | 1.36 |
| System % | 64.5 | 72.2 | 71.8 | **73.7** |

| Bi-candidate | none | long | medium | both |
|---|---|---|---|---|
| Ratio of correctness % | 65.1 | 75.1 | 73.5 | 76.7 |
| Distinct chords (avg.) | 1.38 | 1.46 | 1.29 | 1.23 |
| System % | 62.8 | 71.6 | 70.7 | **72.8** |

The authors' reading (p. 145): the gap between ceiling and output is 5.4 points in the tri-candidate
configuration and 2.9 in the bi-candidate one, against more than 9 points with two candidates from one
chroma (Table 1) — *"This decrease means fewer chord candidates to consider for the system, thus
decreasing the likelihood to select an incorrect chord."* Post-smoothing (§3.3.4) raises 73.7 to
**74.9**.

**Table 3, p. 145 — against the 2009 MIREX method OGF2 (Oudre et al.), same database and procedure:**
root, OGF2 **78.9** against proposed 77.9; root and mode, OGF2 72.3 against proposed **74.9**.

**Table 4, p. 146 — local key, against a direct template-based method (DTBM), key window ≈30 s, 3 key
candidates per frame (p. 145, §3.4):**

| Key estimation | Correct | Relative | Neighbour | Other |
|---|---|---|---|---|
| System % | **62.4** | 2.9 | 17.4 | **17.3** |
| DTBM % | 57.6 | 1.6 | 18.9 | 21.9 |

*Relative* keys share a signature (C major / A minor); a *neighbour* key differs by one accidental.

**★ Table 5, p. 146 — the reciprocal-benefit ablation (§3.5), the measurement DP-B and the L2 charter
carry.** The same system run with the edge cost restricted to the chord axis only, to the key axis
only, and with both:

| Harmonic candidate | Chord only | Key only | Both |
|---|---|---|---|
| System % | chord **73.1** | key **57.8** | chord **74.9**, key **62.4** |

*"We note that both key and chord estimation are better when the harmonic candidate is the (chord,key)
pair. Chord estimation accuracy drops of almost 2% (74.9 compared to 73.1) and key estimation accuracy
drops of almost 5% (62.4 compared to 57.8)."* **The exact differences are 1.8 and 4.6 points.**

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** An audio signal, reduced to chroma vectors per frame — no
notes, no onsets, no spelling, no voices, no metre, no key signature (§2.1). The frame grid is fixed
(hop 4096 or 8192 samples); **there is no note-derived boundary anywhere in the system** — segmentation
is whatever the frame grid and the path's label changes produce. Tuning variation is handled inside the
chroma stage (§2.1.1). It assumes the music is in one of 24 major or minor keys and one of 24 major or
minor triads at every frame; nothing outside that vocabulary is representable.

**What it HANDS downstream.** Per frame, one chord (root pitch class and major/minor quality) and one
local key (tonic and major/minor mode), as the joint state on the minimum-cost path; after
post-smoothing, sequences of these. It hands on **no** Roman numeral or degree, no inversion or bass,
no chord-tone assignment, no seventh or extension, no cadence, no figured bass, and **no alternatives or
confidences** — only the single selected path is output (§2.4). The candidate lists per frame exist
inside the search and are not published.

**Its own STATED SCOPE and limits.**
- **Vocabulary:** 24 major/minor triads and 24 major/minor keys (§2.2.1–§2.2.2); the ground truth is
  mapped onto that vocabulary for scoring (§3.2).
- **No training:** template-based and theory-based; the only tuned quantities are the two exponents
  `α = 1.1`, `β = 1.01`, set *"after experiment"* (§2.3), the candidate counts, the filter window, and
  the key window.
- **Corpus:** one repertoire (Beatles), audio, with on average **1.69 local keys per song** (§3.1) — so
  the local-key task on this corpus is close to a global-key task, and the paper's key result says
  little about tracking frequent modulation.
- **Future work named by the authors (§4, p. 146):** different chord types, silence and no-chord
  detection, *"weighing the harmonic graph of the proposed method in a probabilistic approach"*, and
  using local-key changes for structure since they *"generally occur at the beginning of new patterns."*
- **Post-smoothing is a heuristic overwrite of the decoded path** (§2.5), applied after the search rather
  than inside it, and it moves the headline chord figure by 1.2 points (73.7 → 74.9).

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adopt (as a shape):** the joint state `(chord, key)` per unit, scored as one path — the same shape
  as the framework's one entangled decision and the decisions register's D-001. This paper is the
  published, measured instance that the joint form beats either axis alone on the same system
  (Table 5).
- **Adopt (as a boundary condition, already the charter's):** the coupling as a **cost inside the path
  score**, with the authors' own report that a hard chord–key compatibility filter *decreased* accuracy
  (§2.2.3). The charter's "cost, never a veto" is this paper's position, stated by the authors as the
  reason for their design.
- **Adapt:** a theory-derived transition cost — Lerdahl's tonal pitch space distance — used **without
  fitting**, with a small exponent to break integer ties and to make distant key moves dearer than
  stepwise ones. For DP-P (how L2's score terms are combined and fitted) this is evidence that an
  un-fitted, published-theory cost carries a working joint decode; its two exponents are hand-set.
- **Adapt (evidence for the candidate-admission rule the L2 charter says carries its own defense):**
  Tables 1 and 2 measure the trade the admission rule makes — widening the candidate set from the same
  evidence raises the ceiling (ratio of correctness) but lowers the output, because near-duplicates of
  the best candidate dilute the search; widening it with candidates from *different* evidence (other
  time scales) raises both. The paper measures this on audio chroma; the shape of the trade is what
  travels.
- **Must argue against:** the frame grid as the unit of decision, with no note-derived boundaries
  (L1's change points are absent by construction — the paper is audio); the single-path output with
  no rivals and no confidence (the L2 charter publishes rivals with their mass, including boundary
  rivals); the 24-triad vocabulary with no degree, inversion or chord-tone assignment; and the
  post-hoc smoothing that overwrites the decoded path outside the score.

## ★ Findings, routed and not applied

**(1) V2 VERIFIED at the object, with the exact values.** The findings surface's V2 reads *"Separate
chord/tonality estimation costs ≈2 and ≈5 points over 174 pieces"*; DP-B's ground in `FRAMEWORK.md` §9
reads *"the measured 5-point tonality and 2-point chord cost of separating them"*. Table 5, p. 146:
chord 74.9 against 73.1 (**1.8**), key 62.4 against 57.8 (**4.6**); the authors' own words are *"almost
2%"* and *"almost 5%"*. **No correction is owed to the finding; a precision is recorded:** the paper's
figures are 1.8 and 4.6 points, and "5-point" in DP-B rounds 4.6 up. The 174-song corpus is at §3.1.

**(2) V7 — the "two studies" wording — REPRODUCED at the object, and the pass's correction stands.**
The L2 charter reads *"One study measured joint estimation beating separate estimation; another reports
the opposite for its own system"* (`FRAMEWORK.md` §5, L2), and Appendix B's first-stage draft names the
second study: *"Rocher and colleagues measured joint estimation beating separate estimation, and
Catteau and colleagues report the opposite for their own system"* (Appendix B, §S5 "The derived
decomposition", subsection "The layers", the L2 block — lines 1721–1722 at this reading, located at the
heading list rather than from where the passage was found). **At the object, both halves are in this one paper**: the measurement is Table 5
(§3.5, p. 146) and the quoted warning — *"an incorrect chord selected may discard the correct key (and
vice versa) … adding a compatibility between chords and keys has led to a decrease of accuracy"* — is
Rocher et al. §2.2.3, p. 143, about a hard-compatibility variant the same authors declined. The
findings surface already records this (its DP-B block: *"Both halves live in ONE paper … 'Two studies'
is wrong; the conclusion is right and better grounded than stated"*), and it is routed to the user
there. **This read adds one precision to that routed finding: Appendix B attributes the quotation to
Catteau and colleagues BY NAME, not only as "another".** Appendix B is headed *"The first-stage draft,
whole and unedited"*, so the by-name attribution there is the preserved draft's and is not a statement
to be corrected; the live statement is the §5 charter's "another", which the pass's correction already
addresses. Whether Catteau, Martens & Leman 2006 reports
anything of that sign is a question for row 28's read, next in the proposed order; nothing is carried
about that paper here. **ROUTED, NOT APPLIED** — `FRAMEWORK.md` is untouched.

**(3) A precision on the [FACT — both] label, recorded so it is not over-read.** The first half of the
charter's "both signs" is a measurement with values (Table 5). The second half is a **stated outcome
without a value** — the paper gives no table, no figure and no procedure for the hard-compatibility
variant, only the sentence at §2.2.3. It is a FACT that the authors report it; the *size* of the
decrease is not in the paper and may not be carried as one. **No verdict moves**: the charter's
conclusion (cost, not veto) rests on the sign, which the paper does state.

**(4) A domain and corpus bound on DP-B's measured ground, stated at the object.** The 1.8- and
4.6-point costs are frame accuracies on audio chroma, over a 24-triad vocabulary, on a corpus averaging
**1.69 local keys per song**. The direction of the result is what DP-B carries; its magnitude on
notated classical music with frequent modulation is not measured by this paper. The candidacy
derivation's own consequence (ii) — *"A domain bound is a caveat, not a disqualifier"* — applies, and
the caveat is now stated with the paper's own numbers.

**(5) Evidence bearing on the L2 charter's SECOND boundary condition — the candidate-admission rule —
that the record does not currently cite from this paper.** The charter fixes that the admission rule
*"bounds every claim the analysis can make about its own ceiling"*. Table 1 measures exactly that
ceiling (*ratio of correctness*) beside the output accuracy, and shows them moving in opposite
directions as more candidates from the same chroma are admitted (ceiling 58.3 → 82.9, output
58.3 → 64.9 → 62.2), with the authors' explanation that the added candidates are near-duplicates of the
best one (p. 144). **This is measured evidence that the admission rule's defense must weigh dilution of
the search against the ceiling, not the ceiling alone.** Routed to L2's detail specification as a FACT
of this paper; not applied to any document.

**(6) No falsifier.** Nothing read contradicts any CHOSEN design point: DP-B's chosen "no" is the
paper's own measured position, and the L2 charter's coupling clause is the paper's own design reason.
**No STOP fires** under the remedial commission's §5.

## Centrality

**CENTRAL.** Its claims carry load against a design point (DP-B's measured ground) and in the L2
charter itself (the coupling clause's quotation and both of its "signs"), and an L2 detail
specification would adopt or argue against its joint-state shape, its un-fitted theory cost and its
candidate-admission trade. **A second independent extraction is therefore owed** under the original
commission's §4 central-source rule, by one of that commission's two routes. It has not been performed
and is recorded here as owed.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (2), (3) and (5) are routed and
written nowhere else. It opens no code, touches no measurement tool, no corpus, no golden and nothing
under `tools/`. It writes no open-items row and allocates no decisions-register identity. It reads no
other paper and takes no decision about the order of the remaining slice.

---

*Provenance: written 2026-09-05 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_twelve.md` and performed the ordinary session-start read
(`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived gating answer). Read for this
extract, at the files: `cowork_reading_pass_remedial_commission_2026_08_31.md` whole,
`cowork_reading_pass_commission_2026_08_30.md` whole, `reading_pass/candidacy_upgrades.md` §"The
verdicts — core joint-model and factor-form sources", §"The count", §"Proposed reading order" and
§"READING PROGRESS", `cowork_l2_task_b_slice_derivation_2026_09_05.md` whole, `FRAMEWORK.md` §5 L2 and
L3 (lines 386–450), §9 DP-B (lines 685–688) and the Appendix B L2 block (lines 1716–1726),
`cowork_reading_pass_findings_2026_08_31.md` §DP-B (lines 138–147) and its verification-table rows V2 and
V7, and the L1-slice extract `reading_pass/extracts/pardo-birmingham-2002-algorithms-for-chordal-analysis.md`
as the form to match. The paper itself was read at the object as page images, pp. 141–146. No shell
command was run on the repository or on any staged copy of it for content or for listings. No figure of
this project's own measurement is restated (#17f, D-431); every value above is the paper's own, quoted
with its printed page.*

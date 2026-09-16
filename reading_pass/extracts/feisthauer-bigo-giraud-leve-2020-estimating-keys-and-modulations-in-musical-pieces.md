# EXTRACT — Feisthauer, Bigo, Giraud & Levé, "Estimating keys and modulations in musical pieces", SMC 2020 — Task B candidacy row 30, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-05).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All nine pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.** The
> held file is the HAL deposit: page 1 is the HAL cover sheet, pages 2–9 are the paper as printed,
> SMC 2020 pp. 323–330. **Every location below is the paper's own printed page number** (p. 323 is held
> page 2, and so on) and the paper's own section.
>
> **Why this paper and its place in L2's slice.** It is row 30 of `reading_pass/candidacy_upgrades.md`
> (line 92), ADMITTED there as *"A modulation-deciding method on symbolic classical music, our own
> repertoire and input kind."* `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 (line 75) places it
> in L2's slice: *"A modulation-deciding method on symbolic classical music — tonality per span."* It is
> tenth in group 1 of the proposed reading order ("the joint tonality-and-chord decision") and the
> eighth member read (rows 2 and 44 being unreadable from here). **The record cites this paper nowhere
> else:** a `Grep` of the staged tree (`FRAMEWORK.md`, the findings surface, the bibliography, the
> candidacy derivation, the slice derivation, the handoff entries) for "Feisthauer", "SMC 2020" and
> "Estimating Keys" found only the bibliography row (line 44), the candidacy row, the slice row and the
> hundred-and-nineteenth handoff entry's naming of it as next. **What the record DOES cite from the same
> author group** is different work: `FRAMEWORK.md` DP-K's two further grounds (lines 745–750) cite
> *Feisthauer 2021, the Lille thesis* (population row 16, DECLARED PARTIAL, chapter level) and *Nápoles
> López, Feisthauer, Levé & Fujinaga 2020* (RELAYED); the findings surface's §3.1 chain table (line
> 553) carries the thesis as "16 — Feisthauer … Key per beat, cadences, medial caesura — no chords
> anywhere". The relation of this paper to that thesis is stated at finding (1) below. Ruling 1 of
> `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate: no derivation before L2's slice
> of Task B is read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — no finding

Laurent Feisthauer¹, Louis Bigo¹, Mathieu Giraud¹, Florence Levé²·¹ (¹ Université de Lille, CNRS,
Centrale Lille, UMR 9189 CRIStAL; ² Université de Picardie Jules-Verne, MIS, Amiens), "Estimating keys
and modulations in musical pieces". The printed first page's own citation line: *"Sound and Music
Computing Conference (SMC 2020), Torino, 2020, pp. 323–330"*, with the footer *"Creative Commons
Attribution 3.0 Unported License"*. The HAL cover sheet: hal-02886399, version 2, submitted 9 Sep 2020,
*"Sound and Music Computing Conference (SMC 2020), Simone Spagnol; Andrea Valle, Jun 2020, Torino,
Italy"*. **Title, authors, venue and year all match the bibliography's row** (`docs/research_papers/
BIBLIOGRAPHY.md` line 44: *Feisthauer, Bigo, Giraud & Levé, "Estimating Keys and Modulations in Musical
Pieces," SMC 2020 | https://hal.science/hal-02886399 | ✓ | LINK (HAL)*). Eight printed pages; five
sections (Introduction; Three Measures for a Modulation — 2.1, 2.2, 2.3; Estimating the Tonal Plan and
the Modulations by Combining the Three Measures; Evaluation and Discussion — 4.1, 4.2, 4.3;
Conclusions) plus references; seven figures, three tables, thirty-one references.

**File:** `docs/research_papers/feisthauer_bigo_giraud_leve_2020_smc_keys_modulations.pdf` (541,934
bytes at the listing). One precision for the bibliography reconciliation, NOT an identity finding: the
row's redistribution tier reads LINK (HAL), while the printed paper carries a CC BY 3.0 Unported licence
line, which is the bibliography's own CC tier; noted at finding (9).

## Claims, labeled

### What the method decides, and from what

**★ [FACT, p. 323 Abstract; p. 327 §3] The method decides ONE KEY PER BEAT over a whole piece — the
"tonal plan" — and the modulations are read off where that key changes; it decides no chord.** *"we
introduce new ways to model modulations with the help of features based on musicological knowledge, as
well as an algorithm estimating the tonal plan of a piece."* (p. 323.) *"Computing a tonal plan
k₁ … k_B of a piece of B beats requires to select a key k_b for each beat b ∈ [1, B]. The tonal plan
returned by the algorithm optimally minimizes a combination of the three measures for the whole
piece."* (p. 327, §3.) No chord label, degree, chord tone or segmentation is output anywhere in the
paper; the only chord-shaped object is the V→I detection heuristic of §2.2.1, which is consumed as a
feature (below) and never published as an analysis. The Conclusions: *"these techniques successfully
estimate the tonal plan, with more than 80% correct predictions on some classical string quartets —
without any computation of a pitch profile."* (p. 330, §5.)

**★ [FACT, p. 324 §2; p. 327 §4.1] The input is a SPELLED symbolic score with beats.** *"These measures
are designed for scores with full pitch spelling information. We strongly believe that when it comes to
tonal music, it provides information not only about pitch but also about its function — 'sharpening'
or 'flattening' a pitch is a thoughtful choice by the composer, important for the analysis. On data
without such information, pitch spelling algorithms [22] could be applied first but the pitches which
are the most difficult to spell are precisely the challenging ones for key and modulation estimation."*
(p. 324, §2.) The corpus is **kern *"with full pitch spelling information"*; the implementation is in
music21; *"The beat granularity used is the quarter note for binary time signatures and the dotted
quarter note for ternary time signatures. We consider this to be sufficient to model most of the
harmonic rhythm in this repertoire."* (p. 327, §4.1.)

**★ [FACT, p. 327 §3] The key vocabulary is 42 SPELLED keys — seven letter names × {♯, ♮, ♭} × {major,
minor} — so enharmonic keys are distinct.** *"We consider that there are 42 possible keys that
correspond to all the triplets: {C, D, E, F, G, A, B} × {♯, ♮, ♭} × {Major, minor}."*

### The three measures (p. 324–326, §2)

**★ [FACT, p. 324–325, §2.1] Pitch compatibility — the "current diatonic pitch set" against a key's
usual diatonic set; an ORDER-DEPENDENT, recency-based feature, explicitly NOT a pitch profile.**
*"approaches based on pitch profiles consider statistics on C♮ and C♯, but they do not take into account
the directedness of music: one or a few C♯ can alter our perception, no matter how many C♮ there were
before."* (p. 324.) The current diatonic pitch set 𝒞𝒮(b) is *"a vector with 7 values built by associating
to each of the pitch names in 𝒩 the last encountered accidental (♭♭, ♭, ♮, ♯, ♯♯) on b or right before.
… If one of the 7 pitches was not used before b, we consider the accidental suggested by the key
signature of the piece."* Evaluated at each beat; *"If two accidentals are encountered for the same pitch
name between two beats, only the last one is considered."* (p. 325, §2.1.1.) The usual diatonic set
𝒮(k): the major scale for major keys and **the harmonic minor** for minor keys (p. 325, §2.1.2). The
distance d_diat(𝒮, 𝒮′) is the number of pitch names whose alteration differs; the measure at beat b for
key k is d_diat(𝒞𝒮(b), 𝒮(k)). Worked example (Figure 1, K173.1 mm. 27–29): d_diat to G minor = 1, to
C minor = 4 — *"having recently heard an F♯ makes a G minor more relevant than a C minor."* (p. 325.)

**★ [FACT, p. 325–326, §2.2] Tonality anchoring — beats since the last V→I progression in key k,
bounded; the V→I detector is a VOICE-LEADING heuristic, not a chord labeller.** *"Our heuristic to
detect a V→I progression in key k is when there are at least two of the three following voice leadings:
① the third of V (also known as the leading tone) going to the tonic of I, ② the seventh of V going to
the third of I, ③ the root from V going to the root from I."* (p. 325, §2.2.1.) Its stated false
positives: *"this heuristic produces false positives for homonym keys"* (a V→I in D minor also read as
one in D major) and *"The heuristic will also falsely consider I→IV movements as V→I."* (p. 325.) The
measure: c_{V→I}(b, k) = 0 if the harmony at b is the V or the I of a V→I progression in k, otherwise
min(c, c_{V→I}(b−1, k) + 1), *"bound[ed] … by a constant c = 20"*; *"the value 0 is given at the moment
the V occurs, because it triggers the modulation."* (p. 325–326, §2.2.2.) The authors' own theory
statement beside it: *"a V→I progression can occur on another scale degree than the first one (what is
called a tonicization …). Due to tonicization, modulations can thus not be solely based on V→I, but
such progressions are nevertheless important contributions to modulations."* (p. 325, §2.2.1.)

**★ [FACT, p. 326, §2.3] Tonality proximity — the Euclidean distance between two keys in WEBER's 1817
table of key relationships, bounded; chosen OVER the circle of fifths for a stated repertoire reason.**
*"While working on Mozart's string quartets, we noticed that Mozart often switched between Major and
minor modes of the same key. The circle of fifths is not designed for this behavior, whereas it is
present in the table of relationships between keys introduced in 1817 by Gottfried Weber … This Weber's
table is actually one of the spaces that Lerdhal deduces from his tonal pitch space framework [8]."*
(the paper's own spelling of the name, reproduced as printed)
d_W(k, k′) = min(√(|x_k − x_{k′}|² + |y_k − y_{k′}|²), w), w = 10. Worked values: **d_W(D minor, F
major) = 1, d_W(D minor, C major) = √2** — *"It is more common in the classical era to modulate from D
minor towards F Major … than towards C Major."* In Figure 3's extract of the table, a key's four
nearest neighbours at distance 1 are its parallel key, its relative key, and (vertically) the keys a
fifth away in the same mode; a major key's dominant and subdominant are therefore at distance 1 too.
Scope caveat in the authors' words: *"this table seems to be relevant mostly for the classical period.
Modulations are more daring from the romantic era, favoring enharmonic and chromatic modulations."*

### The algorithm (p. 326–327, §3)

**★ [FACT, p. 326–327, §3] A weighted sum of the three normalised measures, minimised exactly over
the whole piece by dynamic programming over a B × 42 table; the Weber term is a TRANSITION cost between
consecutive beats' keys.** D(k₁ … k_B) = Σ_b [α·c_{V→I}(b, k_b)/c + β·d_diat(𝒞𝒮(b), 𝒮(k_b))/7] +
Σ_{b≥2} γ·d_W(k_{b−1}, k_b)/w; *"the divisions by c, 7, and w normalize each of the three measures to
obtain values between 0 and 1."* The recurrence: D(1, k) = 0; for b ≥ 2, D(b, k) = α·c_{V→I}(b,k)/c +
β·d_diat(𝒞𝒮(b),𝒮(k))/7 + min_{k′}[γ·d_W(k, k′)/w + D(b−1, k′)]; the plan is recovered by backtracking
from the last beat's minimiser. The stated interpretation: *"the value D(b, k) estimates the likelihood
from this key k on the beat b, assuming that the tonal plan calculated until there is optimal."* One
plan is returned; nothing else is published from the table.

### The evaluation (p. 327–329, §4) — measured, on our repertoire, with no held-out split

**★ [FACT, p. 327, §4.1] The corpus:** *"38 movements of Mozart's String Quartets, with manual
annotation of keys and cadences … an enhancement of the corpus used and described in previous works on
sonata forms [23, 29] … available at www.algomus.fr/data."* Thirty movements in a major key and eight in
a minor key (Table 3's captions, p. 329).

**★ [FACT, p. 328, §4.3] THE FIT: a grid search of α, β, γ over the SAME 38 movements the accuracy is
reported on, with the authors' own acknowledgement.** *"The best coefficients α, β, and γ were tracked
by evaluating combinations of values between 0 and 4 (with increments of about 0.002 for α, 0.02 for β,
and 0.5 for γ) on an annotated corpus of 38 Mozart's string quartets. Although no training set was
separated from the corpus, we felt that overfitting was a minor risk due to the size of the corpus and
the very small number of parameters."*

**★ [FACT, p. 329, Table 2] The headline figures — per-beat key agreement, percentage of beats correct
over the corpus:** only d_diat (β = 1): **67.3**; only c_{V→I} (α = 1): **16.3**; no modulation (γ = 1
alone, every beat in the main key): **50.0**; best coefficients **α = 0.016, β = 0.3, γ = 4: 84.8**. The
running text: *"although the current diatonic pitch set measure alone (β = 1) yields good results,
adding the others measures improves the local key detection by 17.5%"* (p. 328, §4.3) — the difference
84.8 − 67.3 in percentage POINTS, stated by the authors as a percentage. And: *"The optimal values …
reflect that, even after bounding and normalization, c_{V→I} is generally high and does not significantly
help the detection here, probably due to the false positives."* (p. 328.) Figure 6 (p. 328) plots
average accuracy against each coefficient with the other two held at their optimum; read from the
figure, not stated in text, the accuracy falls as α grows from near zero and rises steeply as γ grows from
zero — recorded here as a reading of a plotted curve, approximate, and not as a value.

**[FACT, p. 329, Table 3] Per-key results, keys named by the tonic's scale degree relative to each
movement's main key.** Major-mode movements (30): total ref 10333, pred 10333, TP 8998, FP 1335, FN
1335, **F₁ 0.87**; per key, I 0.92, V 0.89, vi 0.75, IV 0.68, i 0.76, v 0.58, ii 0.12, ♭III 0.68.
Minor-mode movements (8): total ref 3172, TP 2462, FP 710, FN 710, **F₁ 0.78**; per key, i 0.88, I 0.85,
♭III 0.72, V 0.86, iv 0.62, v 0.76. **One cell is recorded as printed and flagged:** the minor-mode
total's "pred" cell prints as **172** at the image, where TP + FP = 3172 and the major-mode table's pred
total equals its ref total; the printed value is not transcribed as a fact and the arithmetic is stated
beside it. The authors' reading: *"The algorithm shows also better results on pieces in major main keys
than in minor main keys. This is a known issue in key detection and is mostly explained by the floating
6th and 7th scale degrees of the minor scale. … the algorithm has more trouble finding subdominant
related keys (ii, iv and IV) … Note finally that keys mostly used by Mozart in the corpus are the ones
that are directly aside the main key in the Weber's table (with the exception of V when the main key
is in minor mode)."* (p. 329.)

**[FACT, p. 327–329, §4.2 and §4.3, the K157.3 worked example]** On the third movement of the third
quartet (C major, rondo, modulations to G major and to C minor): the best d_diat value alone names the
correct key on **243 of the 252 beats**; c_{V→I} alone predicts correctly **66 of 252**; the reference
annotation contains **38** V→I movements, the heuristic detects **116**, of which **29** are true
positives (Table 1: C major F₁ 0.77, C minor 0.13, G major 0.67; the 87 false positives *"on parallel
keys and on I→IV progressions"*); the combined method is correct on **248 of 252** beats and *"manages
to find the main key of C Major and all modulations (G Major, C minor, and – not shown – E♭ Major), at
most within 2 beats of the place the modulation occurs in the reference analysis"*; *"the computation of
D, including d_W, favors some stability in the predicted keys, preventing the algorithm from switching
keys for only 1 or 2 beats when a nonchord tone do appear."* (p. 329.)

**★ [FACT, p. 330, §5] The position of a modulation is NOT evaluated — by the authors' own statement it
is future work.** *"Perspectives include a more accurate V→I detection and more complete benchmarks,
including comparisons with alternative key finding algorithms and other theories on tonality, as well as
an evaluation of the detected position of each modulation."* Every reported figure is per-beat key
agreement; the "within 2 beats" statement is about one movement.

**[FACT, p. 324, §1.2] The authors' own placement against row 29 (Chew).** *"These algorithms are fairly
accurate when it comes to detecting global keys and possibly long term local keys. However, they are not
designed to precisely identify where the modulations occur … with the notable exception of work by Chew
[19]. … The complexity of the approach increases with the number of modulations."* Consistent with row
29's extract (m is an input; O(nᵐ)).

**[THEORY, p. 324 §1.1 and p. 326 §2.3, as the paper cites it]** Weber 1817's table of key
relationships [26]; Lerdahl's tonal pitch space [8] deriving that table as one of its spaces; the V→I
progression as the strongest confirmation of a key (Rimski-Korsakov [21]); the circle of fifths
(Diletski, Heinichen). Carried as the paper's citations; none of these primaries is read here.

**[CONJECTURE, p. 330 §5, the authors' own]** *"improved combinations, possibly involving machine
learning, could improve the raw results."*

## Measured results, as the paper states them

| Corpus | Metric | Value |
|---|---|---|
| 38 Mozart string-quartet movements, manual key annotation (Algomus), **kern | per-beat key correct, d_diat alone | 67.3 % |
| same | per-beat key correct, c_{V→I} alone | 16.3 % |
| same | per-beat key correct, main key everywhere | 50.0 % |
| same | per-beat key correct, α = 0.016, β = 0.3, γ = 4 (fitted on the same corpus) | 84.8 % |
| 30 major-mode movements | per-key F₁ overall | 0.87 |
| 8 minor-mode movements | per-key F₁ overall | 0.78 |
| K157.3 (252 beats) | beats whose best d_diat names the reference key | 243 |
| K157.3 | beats correct, c_{V→I} alone | 66 |
| K157.3 | V→I: reference / detected / true positive | 38 / 116 / 29 |
| K157.3 | beats correct, combined | 248 |

**No held-out data; no comparison to any other key-finding method; no measurement of modulation
position.**

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score with full pitch spelling and a key signature
(the current diatonic pitch set defaults to the signature's accidental for a pitch name not yet heard);
a beat grid (quarter or dotted quarter by time signature); voices sufficient for the V→I heuristic's
three voice-leading tests; an annotated main key only for reporting (Table 3 groups by the main key —
the algorithm itself is not told the main key). No chords, no cadence labels at run time, no phrase
structure.

**What it HANDS downstream.** One key (of 42, spelled, major or minor) per beat; the modulations are
the beats where that key changes. No chord, no degree, no chord-tone assignment, no segmentation, no
rivals (the B × 42 cost table exists but only the backtracked minimiser is published; Figure 7 plots
D(b, k) − min_{k′} D(b, k′) for four keys as an illustration), no probability, no confidence.

**Its own STATED SCOPE and limits.**
- **Domain:** notated classical music; *"the table seems to be relevant mostly for the classical
  period"*; developed on and fitted to Mozart string quartets.
- **Vocabulary:** 42 spelled major/minor keys; the harmonic minor as the minor collection.
- **Granularity:** one key per beat; a key change admissible at any beat; segment length is not a
  decoded variable — the Weber transition cost between consecutive beats is what discourages short
  segments.
- **Coupling:** tonality decided ALONE — no chord decision anywhere, so no tonality–chord coupling
  exists to be soft or hard; the only chord-shaped evidence (V→I) is a heuristic feature with a measured
  low precision (29 of 116 on one movement).
- **Fitting:** three weights, grid-searched on the evaluation corpus; no held-out split, stated.
- **Complexity:** dynamic programming, B × 42 states, linear in beats.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adapt (a working, measured, on-repertoire instance of a tonality-change cost built from a
  published key-distance):** the Weber-table Euclidean distance as a transition cost, weighted (γ = 4,
  the largest weight), chosen over the circle of fifths for the stated reason that Mozart switches
  between parallel modes, and reported to be what keeps short-lived key switches from firing on a
  non-chord tone. Its direction on the relative and parallel relations (both at distance 1, nearest) is
  finding (3) below.
- **Adapt (a spelled, order-dependent pitch-compatibility term that is not a pitch profile):** the
  current diatonic pitch set — the last accidental per letter name — against a key's diatonic set,
  measured alone at 67.3 % per beat. A candidate emission-side term on the tonality axis that consumes
  L0's given spelling (DP-F's chosen position is what makes it usable) and reads the score's accidentals
  as evidence with recency rather than as counts.
- **Adapt (cadence evidence INSIDE the tonality decision):** the V→I anchoring term is an existence
  proof that a cadence-shaped cue can feed the key decision rather than be read off it — the L1-cue
  direction of DP-I — together with its measured cost here: a heuristic that is *"generally high and does
  not significantly help"* because of its false positives on parallel keys and on I→IV.
- **Must argue against:** tonality decided alone and first, with no chord decision — the excluded
  tonality-first decomposition (DP-B) in its purest form, as for row 29; a key admissible at every beat
  of a fixed grid, independent of any harmonic boundary (DP-E's rival, *"an independent tonality track
  changing anywhere"*, here on a beat grid); a beat grid fixed before any harmonic decision (DP-C's
  "before" on the tonality axis); the single-minimiser output with no rivals (DP-K's rival); a fit with
  no held-out data (#20); and a per-beat agreement figure standing in for modulation correctness where
  the paper itself says modulation position is unevaluated (D-606's distinction).

## ★ Findings, routed and not applied

**(1) The record's cited Feisthauer work is the Lille thesis; this paper is the published primary of
that thesis's key-tracking chapter, read at the object, and the relation is stated so the two are not
run together.** `FRAMEWORK.md` DP-K cites the thesis (row 16 of `population.md`, DECLARED PARTIAL) for
the dual-tonality principle, and the row 16 extract records its ch. 5 as *"a three-criterion
dynamic-programming key tracker — cadential anchoring (V→I strength), diatonic note compatibility, and
Weber-distance key proximity, over beat × 24-key states — reaches about 85% per-beat key accuracy on
annotated Mozart string quartets"*. At this paper's object the three criteria, the beat grid, the
dynamic programme, the Mozart corpus and the 84.8 % all match, with ONE difference: **this paper's state
space is 42 spelled keys, not 24** — whether the thesis chapter uses 24 or 42 is not establishable
here, since the thesis was read at chapter level by a prompted extraction and not at the object. **Nothing
in the record cites this paper, and nothing this paper says touches DP-K's ground** (the dual-tonality
principle is not stated in it; its nearest statement is that a V→I can be a tonicization). Routed to the
row 16 record as a precision on its "24-key" wording, with no verdict, and to the bibliography
reconciliation as a cross-reference between the thesis row and this row.

**(2) The candidacy row's reason is CONFIRMED with two precisions, of the same shape as rows 26's and
29's.** The row admits it as *"A modulation-deciding method on symbolic classical music, our own
repertoire and input kind."* At the object: symbolic, spelled, classical (Mozart), beat-gridded — the
input kind is ours and the repertoire is adjacent to ours (string quartets; not Bach). The two precisions:
(a) **it decides no chord at all**, so its answer to DP-E's *"decided with the chords?"* is the rival's
(tonality alone), and its place in group 1 ("the joint tonality-and-chord decision") is as the group's
rival shape — the third such member after rows 26 and 29; and (b) **a key change is admissible at every
beat**, so its answer to DP-E's *where* is the rival's (anywhere on a fixed grid), with the Weber
transition cost as the only thing weighting one position over another. The ADMITTED verdict stands (a
rival is admitted under the derivation's own consequence (i)); the group placement is left as it stands,
"stated, not ruled".

**(3) A THIRD published position that the relative major/minor is a nearest tonality change — this
time carried into a working model's transition cost AND measured on our repertoire's kind of input,
with the PARALLEL major/minor equally nearest.** In Weber's table as the paper uses it, a key's parallel
and relative keys are both at distance 1 (D minor → F major = 1; and the table's rows place C major
beside c minor and a minor), while the circle of fifths is rejected in terms because it *"is not designed
for"* Mozart's parallel-mode switching. This stands beside row 28's (published theory: relative at
distance one) and row 26's (Krumhansl-correlation transition matrix: relative nearest) findings, and is
opposite in direction to the legacy D-347 cost (a large extra penalty on the relative switch) and unlike
the legacy D-348 measure (circle-of-fifths distance). What this instance adds to the two before it: a
measured outcome on symbolic classical input (γ = 4 the largest fitted weight; the main-key-everywhere
baseline at 50.0 % against 84.8 % with the transition cost in the model), and the parallel relation
placed at the same distance as the relative. Routed to L2's detail specification beside rows 26's and
28's findings, with no verdict.

**(4) Cadence evidence feeding the tonality decision, with its measured cost.** The V→I anchoring term
is the paper's own instance of a cadence-shaped cue used INSIDE the key decision (the DP-I upstream-cue
direction, and the thesis extract's "existence proof"), and the paper measures it: alone 16.3 % per beat;
on K157.3, 116 detections for 38 reference progressions and 29 true positives; the authors' verdict that
it *"does not significantly help the detection here, probably due to the false positives"*; and the
optimal α = 0.016 against β = 0.3 and γ = 4. **This is a bound on how much a voice-leading V→I heuristic
can carry as a tonality cue when it cannot tell a tonicization from a modulation or a parallel key from
its homonym** — which is the charter's own reason for splitting cadence cues (L1) from cadence type
(L3). ENRICHES-shaped for DP-I's chosen split and for DP-E's chosen point; routed to the findings
surface's DP-I and DP-E blocks.

**(5) A spelled, recency-based pitch-compatibility term measured alone at 67.3 % per beat, explicitly
against the pitch-profile family.** The current diatonic pitch set reads accidentals as directed
evidence (*"one or a few C♯ can alter our perception, no matter how many C♮ there were before"*), consumes
L0's given spelling, uses the harmonic minor as the minor collection, and defaults to the key signature
for an unheard letter name. A precedent for an L2 tonality-axis emission term that is neither a
Krumhansl-style profile nor a count; its minor-collection choice (harmonic minor) is a design decision
the paper does not defend beyond the choice itself. Routed to L2's detail specification with no verdict;
the key-signature default is also a datum beside D-450/D-528 (the signature as an initial-state prior)
with nothing moved.

**(6) The fit is on the evaluation corpus with no held-out split, by the authors' own statement, and
the binding metric for a modulation detector is not measured.** Three weights grid-searched on the 38
movements reported on (#20 not satisfied — stated, not hidden); every figure is per-beat key agreement;
*"an evaluation of the detected position of each modulation"* is named as future work. Under this
project's own convention (D-606: a modulation detector is judged on modulation correctness, not on the
agreement percentage), the 84.8 % is a per-beat key-agreement figure and NOT a modulation-detection
figure, and the paper says so in its own words. Routed to measurement design beside the fit/evaluation
findings of rows 8 and 26 and beside D-606; no verdict.

**(7) The Weber transition cost is reported as the term that suppresses one- or two-beat key switches
on a non-chord tone — an instance of segment stability bought by a transition cost rather than by a
decoded segment length.** *"the computation of D, including d_W, favors some stability in the predicted
keys, preventing the algorithm from switching keys for only 1 or 2 beats when a nonchord tone do
appear."* The chosen DP-C shape lets segment length be a decoded variable; this paper achieves the same
effect on the tonality axis by a first-order transition cost on a fixed grid, without decoding length.
A rival mechanism for the same stability, with a measured outcome on one movement; routed to L2's
detail specification beside finding (3), no verdict.

**(8) A precision to reading group 1's own membership, in the same terms as rows 8, 26 and 29.** Three
of the group's read members (26, 29, 30) decide tonality alone and no chord; by the order's own group
definitions their place in "the joint tonality-and-chord decision" is as the rival shape. Shown to the
user and applied nowhere; the order is "stated, not ruled".

**(9) Bibliography precision, not an identity finding.** The printed paper carries a CC BY 3.0
Unported licence line; the bibliography row's tier reads LINK (HAL). The bibliography's own CC tier is
defined as *"openly licensed (CC BY or equivalent)"*. Routed to the bibliography reconciliation as a
tier precision; nothing else in the row is affected.

**(10) No falsifier.** Nothing read contradicts any CHOSEN design point. The paper measures no
joint-versus-separate comparison, decides no chord, and publishes no rivals, so DP-A, DP-B, DP-C, DP-D
and DP-K are untouched by its measurements; its tonality-alone decomposition is an instance of the
excluded rival, not evidence for it. DP-K's two further grounds cite the thesis and the ISMIR 2020
methodology paper, not this paper, and nothing here bears on them. **No STOP fires** under the remedial
commission's §5.

## Centrality

**CENTRAL, on a narrow ground, challengeable at the progress record.** No ratified text cites this
paper, and its design shapes — a tonality track on a beat grid, a transition cost, a compatibility term —
have primaries or owners elsewhere. What earns the verdict is the ground row 26 was graded central on,
here met more strongly: **a held, working instance of a tonality-change cost built from a published
key-distance construction (Weber 1817 — a public theory, not the R-8 gap), with its direction stated,
its weight fitted, and a measured outcome, on symbolic classical input with full spelling — the same
input kind as ours.** An L2 detail specification that designs a tonality-change term will have to cite
this paper's transition cost and its measured contribution, whether to adopt its shape or to argue
against it; and finding (3) is the third and strongest member of a line of evidence (rows 28, 26, 30)
that runs opposite to a legacy decision (D-347) a detail specification must dispose of. **The ground
on which NOT CENTRAL could be argued, stated so the challenge is easy to make:** as with row 29, no
ratified text cites the paper, its fit has no held-out split, its measurement is not the binding metric
for a modulation detector, and its distinctive object — Weber's table — is a representation, which the
criterion says is not itself an upgrade. The difference taken here from row 29's verdict is that this
paper carries a measured outcome on a corpus of our input kind and row 29 carries none; and that its
method's contribution is measured term by term (Table 2), which is what a detail specification would
cite. **A second independent extraction is therefore OWED** on this verdict.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `docs/research_papers/BIBLIOGRAPHY.md`,
`cowork_reading_pass_findings_2026_08_31.md` and the row 16 thesis extract are untouched; findings (1)
to (9) are routed and written nowhere else. It does not fetch the Lille thesis, Weber 1817, Lerdahl 1988
or the Algomus corpus. It opens no code, touches no measurement tool, no corpus, no golden and nothing
under `tools/`. It writes no open-items row and allocates no decisions-register identity. It reads no
other paper and takes no decision about the order of the remaining slice.

---

*Provenance: written 2026-09-05 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_nineteen.md`, after the ordinary session-start read (`CLAUDE.md`
whole, `DECISIONS.md` whole, `STATUS.md`, the derived gating answer), the hundred-and-eighteenth entry's
bridge-fault section, the progress record whole, both commissions whole, the row 29 extract whole for
the form, and `reading_pass/candidacy_upgrades.md` whole. Read for this extract, at the files:
`candidacy_upgrades.md` row 30 (line 92), `cowork_l2_task_b_slice_derivation_2026_09_05.md` row 30
(line 75), `docs/research_papers/BIBLIOGRAPHY.md` line 44, `FRAMEWORK.md` at the L2 charter (§5, lines
386–424) and DP-B to DP-K (§9, lines 685–750), the findings surface at §3.1 (line 553), the row 16 thesis
extract whole, the row 28 extract at its finding (5) and the row 26 extract at its finding (2) — read
at the extracts themselves, not from the progress record's one-line summaries, before finding (3) above
cited them — and a `Grep` of the staged tree for "Feisthauer", "SMC 2020" and "Estimating Keys". The
paper itself was read at the object as page images, all nine pages of the held file. No shell command
was run on the repository or on any staged copy of it for content or for listings. No figure of this
project's own measurement is restated (#17f, D-431); every value above is the paper's own.*

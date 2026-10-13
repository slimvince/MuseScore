# How fast distant music stops mattering, and reading with a bounded delay — a targeted reading of the public research for L2-S22 — 2026-10-07

> **STATUS: RESEARCH READING AND ITS CHECK §B, written for the record; nothing is ruled, applied or asked here.** Cowork, 2026-10-07
> (Stockholm), the sitting that booted on `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_nineteen.md`.
> It answers the user's question put with Ruling 2 of
> `records/cowork/rulings/cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md`: *"should we reread public
> research on the subject or have anything useful for this specific problem been considered?"* **It does not reopen
> Ruling 2**, which fixes the structure of L2's stopping rule; it informs the values decided at the effort setting's
> build (D-202, DEFERRED) and the step-size test already owed. Labels, under the theory-grounding corollary to #1/#2
> (D-473): **FACT** = stated in a text this sitting fetched, quoted; **THEORY** = established published theory or
> elementary mathematics, named as such; **CONJECTURE** = this side's reasoning, including every application to L2.
> **No equation is carried out of a text that was not fetched.** Marks for the record: *checked* = read at the object
> by this sitting; *relayed* = taken from another text and not read at its own source.

---

## 0. How the texts were read — a bound on every FACT below

- **Web access was used**, declared to the user before the first search. Earlier sittings used none, as practice.
- **Every fetched text passed through the fetch tool's own summarising model.** Each request asked for verbatim
  quotation only, and the tool returns quotations in segments of at most 125 characters. So every FACT below is *a
  quotation as that tool returned it*; no PDF was opened as page images by this side. A mis-transcription by the tool
  would not be visible here. Where the tool said a passage was absent, that is recorded as "not found in the text as
  returned", never as "not in the paper".
- **Two extractions, cross-checked (§B).** The corollary asks for central sources to be extracted independently two
  or three times and cross-checked. §3 is this side's first extraction. The second was made by four fresh subagents,
  one per source, each given only the source's address and the extraction form, not the first extract; their reports
  were treated as unverified, and each disagreement was settled at the source. *(Former wording, preserved (#12):
  "**First extraction only.** … This document is the first extraction of each; **the second is OWED** (§6).")* The
  subagents used the same fetch tool, so the bound above holds for both passes: the doubling guards against a reading
  error by one pass, not against the tool itself.
- No shell was used. Nothing of the shipped program was read.

## 1. The questions it serves

From the ruling record (*checked*) and entry 319 §3 (*checked*):

1. **Does the top setting's "unchanged" test settle before the safety cap?** Ruling 2: at the top effort setting L2
   stops "when its in-span publication — the readings, the span-rivals and their masses — is the same after an
   enlargement as before it"; D-624's cap ends a loop that does not settle, and the publication is marked truncated
   (D-263). The record carries this as "unestablished … a measurement at the build".
2. **What does a tolerance on the masses mean**, for the settings below the top?
3. **What does the step size mean** — the risk recorded at the surface's §A.5 point 5: one enlargement adds music that
   changes nothing, while the decisive music lies one step further.

What L2's masses are, so that the theory can be matched to them: **L2-S40** — "*Mass* is the probability the fitted,
whole-reading-normalised model (L2-S35) assigns. A span-rival's mass is the marginal: the total mass of all whole
readings that contain that span …" (`cowork_blind_derivation_l2_2026_09_27.md`, *checked*). L2-S35: "the masses of all
readings of the working span sum to one" (*checked*). So L2's masses are **marginals of a normalised distribution over
whole readings of a chain** — the quantity the theory below calls the *smoothed* (or *smoothing*) distribution. L2's
principal reading is the best whole reading — the quantity the theory calls the *Viterbi path*.

## 2. What was searched, and what was found

Searched (web, this sitting): online Viterbi decoding; exponential forgetting and filter stability of hidden Markov
models, including the Hilbert projective metric and Birkhoff's contraction; fixed-lag smoothing; online decoding
under a latency limit; and, for music, local key estimation and context length, real-time key finding with
look-ahead, and bidirectional context in harmonic analysis.

| Source | What it is about | Fetched? |
|---|---|---|
| Šrámek, Brejová & Vinař, *On-line Viterbi Algorithm and Its Relationship to Random Walks*, arXiv:0704.0062 (2007) | when the best path's early part can be output exactly before the sequence ends | **Yes** |
| Ye, Ma & Qian, *Estimate Exponential Memory Decay in Hidden Markov Model and Its Applications*, arXiv:1710.06078 | how fast a hidden Markov model forgets, and how long a stretch is needed for a given error | **Yes** |
| Shue, Anderson & Dey, *Exponential Stability of Filters and Smoothers for Hidden Markov Models*, ECC 1997 (author copy, Maynooth repository) | forgetting of filters **and fixed-lag smoothers** | **Yes** (venue from the ANU repository record, *checked*) |
| Garg & Pichkhadze, *Online Markov Decoding: Lower Bounds and Near-Optimal Approximation Algorithms*, arXiv:1810.07301 (NeurIPS 2019) | what any decoder with a fixed look-ahead can and cannot guarantee | **Yes** |
| Narasimhan, Viola & Shilman, *Online Decoding of Markov Models under Latency Constraints*, ICML 2006 | committing a label when a certainty measure allows, instead of a fixed window | **No** — the PDF host refused the fetch. Only the anthology page's abstract was seen, and the tool paraphrased most of it. **Nothing is carried out of it.** |
| Le Gland & Mevel (2000); Atar & Zeitouni (1997); Collet & Leonardi | the theorems Ye, Ma & Qian cite | **No** — *relayed* through Ye, Ma & Qian only |

**For music specifically, nothing was found that addresses L2's question** — when a joint reading of tonality and
chord stops depending on music outside the selection. The music hits were window-size choices for key tracking and
general harmonic-analysis models (e.g. a DAFx 2009 local-key paper, Sapp's keyscapes, an ISMIR 2006 paper); none was
opened, so this is a negative over the search results as listed, not over the field.

## 3. What the sources state

### 3.1 Šrámek, Brejová & Vinař (2007) — the exact early output of the best path

- **FACT** (§2): "Left of the coalescence point, there is only a single candidate for the initial segment of the most
  probable state path." / "Therefore we can output this segment and remove all edges and nodes of the tree up to the
  coalescence point." The coalescence point is "a node … that does not have an ancestor with at least two children".
- **What that means in plain words.** The Viterbi search keeps, for each possible state at the newest position, the
  best path ending there (the *survivors*). Whatever music comes later can only choose *among* the survivors. Where all
  survivors share the same early stretch, no later music can change that stretch of the best path. **This is a proof,
  not a guess**: the early stretch is final. *(This side's reading of the quoted sentences; neither pass found a
  sentence stating in so many words that the output equals the classical Viterbi result.)*
- **FACT** (§2), on the older fixed-delay method: Forney's algorithm "after processing D symbols … checks whether … a
  coalescence point has been reached"; "If the coalescence point was not reached, one potential initial segment is
  chosen heuristically." The paper gives no guarantee for the heuristic case (not found in the text as returned).
- **FACT** (§3.1, two-state symmetric model only), on how long the undecided stretch is: with `t` the probability of
  changing state and `e` the probability of a misleading observation, `K = [2 (log(1−t) − log t) / (log(1−e) − log e)]`
  (the bracket's exact form — rounding or ceiling — came back differently in two fetches and is not established);
  "the expected length of a run … is K-1" (Lemma 1, for a uniformly random input); "the larger is K, the more memory is
  required"; "The worst case is achieved as e approaches 1/2." **In plain words: the rarer a change of state, and the
  weaker the evidence, the longer the stretch that stays undecided.**
- **FACT** (§1, §2): "In the worst case, our algorithm still requires Θ(nm) memory" — that is, there are inputs on which
  nothing coalesces until the end. Real data (gene finding): "the length of the table did not exceed 222,000 on any of
  the 20MB human segments"; average 11,000.
- **FACT** (§3.1, §4): the logarithmic growth is shown for symmetric two-state models; for more states it is stated as a
  conjecture supported by experiments ("We conjecture that this trend extends to more complex cases").

### 3.2 Ye, Ma & Qian — how fast a hidden Markov model forgets, and the stretch needed for a given error

- **FACT** (Theorem 2.1, attributed to Le Gland et al.): "If Markov transition matrix is primitive and the emission
  distribution p(y_n|x_n) is strictly positive", the difference between two runs started from different states shrinks
  exponentially (their eq. 7). **FACT** (Theorem 2.2, attributed to Atar & Zeitouni; Collet & Leonardi): the exact rate
  is "λ2 − λ1", the gap between the top two Lyapunov exponents (eq. 8); "this gap is strictly negative when the
  transition matrix is primitive and the emission distribution is positive". The paper's own wording is not
  consistent here: the displayed formula is an equality ("the exact convergence rate"), the sentence after it says the
  rate "is upper bounded by the gap" (second extraction, *checked* at its quotation). **FACT** (at Theorem 2.3, the
  Furstenberg–Kesten result): the top Lyapunov exponent "exists almost surely, moreover, it is nonrandom quantity and
  independent of the choice of metric and initial condition"; and "Lyapunov spectrum doesn't depend on the choice of
  sequence almost surely" — stated in a setting where the random matrices are taken as independent and identically
  distributed. *(Former wording, preserved (#12): "**FACT** (Theorem 2.3): the rate "is nonrandom quantity and
  independent …"" — the sentence is about the Lyapunov exponent, not stated of the rate; that the gap is nonrandom
  follows from the second sentence, in that setting.)*
- **FACT** (§2, worked example): for their three-state example, "the estimated gap is λmax = −0.1944 with data of 10000";
  "the length B needed for ε = 10^−15 is about 178" (both passes; ln(10^−15)/0.1944 ≈ 177.7, so the 178 omits the
  constant C). **In plain words: in that one example, about 178 steps took the remaining dependence down to near the
  computer's rounding level.**
- **FACT** (abstract; eq. 10): "The length of subsequences B given the controlled error ε is B = log(ε)/(λ2 − λ1)";
  eq. 10 bounds the difference by `C exp((λ2 − λ1) n)` times the initial difference. **FACT, a caution the tool
  reported:** the length formula is stated with "≈" and an unspecified constant `C`, so it is not a guarantee at a
  finite length.
- **FACT** (Appendix A, definitions; §2, the rate): a computable bound from the transition matrix alone. Appendix A
  defines `φ(M) = min over p,q,r,s of (M_pq M_rs)/(M_rq M_ps)` (eq. 24) and `τ(M) = (1 − √φ(M)) / (1 + √φ(M))`
  (eq. 25). §2, citing Peres: the gap "is upper bounded by log τ(M)", and "When M is positive, … the exponential
  forgetting of the prediction filter follows with convergence rate log τ(M)". **The rate is stated for the
  *prediction filter* — the forward direction — not for the smoothed masses**; this paper as returned states no
  theorem on smoother decay (not found, both passes). *(Former wording, preserved (#12): "**FACT** (Appendix A): … "the
  exponential forgetting … log τ(M)"" — the sentence stands in §2, not Appendix A, and the forward-only scope was not
  stated.)* **THEORY**, to read it:
  `τ(M) < 1` only if every entry of `M` is positive (otherwise `φ = 0` and `τ = 1`, no contraction in one step); a
  model with zero entries has to be bounded over several steps together.
- **FACT** (§2): "the memory loss property requires the Markov chain to be irreducible and aperiodic and the emission
  distribution to be positive".

### 3.3 Shue, Anderson & Dey (ECC 1997) — the same holds for smoothers

- **FACT** (abstract): "we demonstrate exponential forgetting for both the recursive filters and smoothers, and obtain
  overbounds on the rate of forgetting."
- **FACT** (§1): "the rate of increase of benefit from smoothing falls off exponentially as [the lag] increases, with the
  same rate as the forgetting rate of the HMM filter, which is, furthermore, at least as fast as that of the original
  hidden Markov signal model." *(The tool's text drops Greek letters and ligatures; "[the lag]" stands where a symbol is
  missing.)*
- **FACT** (§3.1): "all the improvement that can be gained by smoothing is attained after some finite [lag], and no
  significant gains can be made as the lag is extended further."
- **FACT** (§2.3, footnote 1): a product of positive matrices "may become dyadic as r → ∞", where "dyadic means that a
  matrix is of rank 1". **So the forgetting is stated in the limit.** The paper as returned gives no closed-form rate
  ("rates are computable [8]") and **no statement that the dependence reaches zero at a finite lag** (not found).
- **FACT** (§3.2.2): conditions — the transition and observation matrices "are strictly positive". §2.3: "Similar
  convergence properties also exist when the conditions A > 0 and C > 0 are relaxed" (primitivity, footnote 2).
- **FACT** (§4, added from the second extraction and *checked* at its quotations): a computable estimate of the lag a
  fixed-lag **smoother** needs. "The lag required for the smoothing error variance to reach steady-state can be estimated
  by using the so-called Birkhoff coefficient …, which is a measure of how close a given matrix is to having rank 1";
  "an approximate bound is" the Birkhoff coefficient of the transition matrix `A` alone, "whereas a tighter bound can be
  found by grouping three terms at a time". The criterion's equation came back garbled; the tool reconstructed it as
  "the coefficient to the power ℓ_crit/4 equals 1/e" — **reconstruction, no equation carried from it**. Their Table 1
  (two-state examples) gives ℓ_crit from about 2 (transition matrix [0.6 0.4; 0.4 0.6]) to 38 (stickier, [0.95 0.05;
  0.05 0.95]); §4.1: ℓ_crit is "an adequate, albeit slightly pessimistic, bound". §5: "Other indirect applications
  include the Viterbi algorithm, where the concept of a crit may help to guide the choice of truncation point". **In
  plain words: the stickier the states, the longer the lag; and the bound can be computed from the model.**
- **FACT** (§1), the engineering precedent they cite for the Kalman filter: "with [lag] equal to four or five times the
  dominant time constant of the Kalman filter practically all the benefit derivable from smoothing is achieved [2]".

### 3.4 Garg & Pichkhadze (NeurIPS 2019) — what a fixed look-ahead can guarantee

- **FACT** (§2): "We say an algorithm has latency L if L is the smallest B such that the algorithm needs to access at most
  B+1 observations … to generate the label for observation w_i". The comparison is the ratio of the optimal offline
  total to the online total ("competitive ratio ρ … defined as the ratio OPT/ON"), over rewards built from the model's
  log-probability terms.
- **FACT** (Theorem 1): their method's ratio is at most `1 + Θ(log L / (L − Δ̃ + 1))` for an ergodic chain of
  diameter Δ, for `L ≥ Δ + n − 1`. **FACT** (Theorem 5): "The competitive ratio of any deterministic online algorithm on
  nth order (time-varying) Markov chain models with diameter Δ for latency L is greater than" `1 + (Δ̃/L)(…)`; Theorem 6
  (randomised) is likewise stated for "(time-varying)" models. Whether the lower bounds hold for a model that does not
  vary with time is not found in the text as returned (both passes). **In plain words: for every fixed look-ahead,
  there are time-varying models and inputs on which no decoder with that look-ahead matches the best reading.** That an
  exact match is impossible is this side's reading of the lower bound, not a sentence of the paper (neither pass found
  one). *(Former wording, preserved (#12): "their method reaches `ρ = 1 + …`" and "for every fixed look-ahead, there are
  inputs (the theorem is for time-varying models) …" — the bound is an upper limit, and the qualifier belongs in the
  claim itself.)*
- **FACT** (§7): on genome data, their decoder "agreed with the Viterbi labels on more than 95% of the sites" at a
  latency "of only about 20". The PDF as returned is headed "Preprint. Under review."; whether it is the NeurIPS 2019
  version is not established.

## 4. What this means for L2 — every point here is CONJECTURE (this side's reasoning)

**4.1 Question 1 — does the top setting's test settle before the cap?** Two different answers for the two parts of
what L2 publishes.

- **The masses.** L2's masses are smoothed marginals (§1). The sources state that the effect of distant evidence on
  them dies out *exponentially* and reaches its limit *as the distance goes to infinity* (§3.2, §3.3). **THEORY:** a
  product of invertible matrices is invertible, so if L2's step matrices (transitions weighted by the evidence) are
  invertible and positive, the product never becomes rank one at a finite length — **in exact arithmetic the masses
  would in general change, by ever smaller amounts, at every enlargement that adds evidence, and "the same after an
  enlargement" would in general not be met before the safety cap.** *(Former wording, preserved (#12): "would change
  … at every enlargement, and … would never be met" — an absolute; an enlargement whose evidence favours no state over
  another changes nothing, and L2's expanded span model may have singular step matrices.)* It is met only because the computer rounds: once the change falls below the precision
  computed, two runs give the same numbers. L2-S43 already reads equality as "equal … to the precision computed" for
  ties (*checked*); read the same way, the top setting's test settles where the remaining change falls below rounding.
  By Ye, Ma & Qian's formula, that distance is of the order of `ln(ε) / (λ2 − λ1)` with ε the rounding precision — a
  fixed number of slices for a given fitted model, **with no value known until the model is fitted** (and the formula
  is approximate, §3.2). So: the top setting settles before the cap if the cap is longer than that distance; whether
  it is cannot be said before the build — the record's own carried unknown, now with a formula for it.
- **The principal reading.** Here the research offers more than the record assumed: an **exact certificate**. If all
  survivors of the search at the far edge of the loaded music agree on the in-span part of the best reading, no music
  beyond that edge can change it (§3.1). That is stronger than "unchanged after one enlargement": it cannot be fooled
  by a step that adds nothing while decisive music lies one step further — **the risk the surface's §A.5 point 5
  recorded, for the principal reading.** Three cautions: (a) the source proves it for a plain chain read in one
  direction; L2 is read in both directions, by spans (semi-Markov), and whether agreement must hold over every pair of
  edge states at once has **not been derived here**; (b) coalescence can take long, longest where changes of state are
  rare and evidence weak (§3.1's `K`) — the musical analogue is a long passage that does not reveal its tonality; (c)
  the worst case is no coalescence before the end (§3.1).

**4.2 Question 2 — what a mass tolerance means.** The sources give two different quantities a tolerance could be set
on: **(i)** the change observed between two successive enlargements (Ruling 2's wording), or **(ii)** a *bound* on all
further change from any music beyond the edge — estimated from the model by a Birkhoff coefficient, as Shue, Anderson &
Dey do for the fixed-lag smoother's lag (§3.3, their §4: an *approximate*, "slightly pessimistic" bound, whose exact
inequality was not legible). *(Former wording, preserved (#12): "computable from the model (§3.2's `τ(M)` raised to the
distance, under its conditions)" — Ye, Ma & Qian state that rate for the forward prediction filter, not for smoothed
masses; the smoother-side source is Shue, Anderson & Dey.)* Neither source gives a proven bound for the smoothed masses
that this side could quote whole, so (ii) is a direction to work out at the build, not a ready formula. (i) is cheaper but carries §A.5 point 5's risk; (ii) cannot be fooled by a quiet step, but needs the
bound's conditions to hold for L2's model (L2-S36 admits readings of zero mass, so some entries may be zero and the
one-step bound would then be `τ = 1`, useless alone). Which to use is a value-and-method question for the effort
setting's build; **it does not change Ruling 2's structure** — both fit "a tolerance on the change in mass".

**4.3 Question 3 — the step size.** The exponential decay means each further slice matters less than the one before;
so a step that changes nothing at the rounding precision is strong evidence — but only *in the masses*, and only past
the distance of 4.1. For the principal reading the decay theorems say nothing; the coalescence certificate (4.1) is
what removes the step-size dependence there. **The step-size independence test already owed (D-264; Rows 45.24, 45.72)
stays the test.** Garg & Pichkhadze's lower bound (§3.4) adds one thing: no *fixed* forward limit — for example "stop
at the next cadence" — can match the best reading on every input, proven for time-varying models (whether L2's model
counts as one in their sense is not settled here). *(Former wording, preserved (#12): ended at "on every input", without
the theorem's scope.)* That supports what the record already says: such a
limit belongs to a lower effort setting, not the top (the surface's §A.5 point 2).

**4.4 What the theory cannot settle.** The rate `λ2 − λ1` depends on L2's fitted model and on the music (Ye, Ma & Qian
treat the Lyapunov spectrum as nonrandom in a setting of independent, identically distributed matrices, §3.2; music is
not that, so whether one rate holds across a piece is not known here). *(Former wording, preserved (#12): "Theorem 2.3
calls the rate nonrandom; the full conditions of that theorem were not returned by the tool".)* Shue, Anderson & Dey's
Table 1 shows the size of the effect in small examples: the lag grows from about 2 to 38 steps as the states get
stickier (§3.3). Whether ordinary
repertoire forgets within a few bars or a few pages is a measurement at the build. The sources' conditions (primitive
transitions, positive evidence) are not established for L2's model.

## 5. What this reading recommends — nothing is asked

Nothing here needs a ruling now; it informs the effort setting's build and the owed step-size test. Recorded for that
build: (a) the top setting's "the same" is met at the precision computed, at a distance the fitted model's forgetting
rate fixes (§4.1); (b) an exact coalescence test exists for the principal reading and answers §A.5 point 5's risk for
it, two-sided form not derived (§4.1); (c) a bound-based tolerance is an alternative to an observed-change tolerance,
as a direction to work out rather than a ready formula (§4.2). **Whether (b) should be written into L2-S22 is an algorithm question and is not put here.**

## 6. Owed

- *(Former first item, preserved (#12): "**The second, independent extraction** of the four fetched sources (§3.1 to
  §3.4), cross-checked against this one." — done, §B.)*
- A reading of the four sources at their pages, should any of them come to carry load: both passes went through the
  same fetch tool (§0).
- Narasimhan, Viola & Shilman (2006) and Le Gland & Mevel (2000) are not fetched; a reader with access may close them.
- No bibliography row is added; `docs/research_papers/BIBLIOGRAPHY.md` was not edited by this sitting.

## §B The check, and the cross-check of the two extractions

Run in the turn after the user's "put this research-iteration in the plan as you suggested, then carary on". The
second extraction of each source (§0) was compared with §3 claim by claim; every quoted value both passes carry
**agrees** — the coalescence sentences, the definition of `K`, Lemma 1, the worst-case memory, the gene-finding figures;
Theorems 2.1 and 2.2 and eqs. 10, 24, 25; Shue, Anderson & Dey's abstract, §1, §3.1 and footnote 1; Garg & Pichkhadze's
latency definition and Theorems 1 and 5. The document was then swept for absolutes (never, every, all, no, nothing,
only, exact, proof), each read against what established it. **Corrections, at their sites, former wordings kept:**

1. **§3.2, a sentence placed at the wrong section and its scope left out.** The `log τ(M)` rate stands in §2, citing
   Peres, and is stated for the forward prediction filter, not for smoothed masses.
2. **§3.2, a statement attributed to "the rate" that the source makes of the Lyapunov exponent**, in an i.i.d. setting.
3. **§3.4, an upper bound written as an equality, and the theorem's time-varying scope kept outside the claim.**
4. **§4.1, an absolute** ("would change … at every enlargement", "would never be met").
5. **§4.2, a bound for the smoothed masses attributed to a source that states it for the filter.** Re-based on Shue,
   Anderson & Dey's §4, as an approximate estimate.
6. **§4.3 and §4.4**, the time-varying scope and the nonrandom rate, carried through to the reasoning.

**Added from the second extraction:** Ye, Ma & Qian's worked example (about 178 steps to 10^−15); Shue, Anderson &
Dey's §4 lag estimate, Table 1 and their suggestion for Viterbi truncation; the Kalman precedent; Garg & Pichkhadze's
genome result and the preprint caution; the uncertain bracket in `K`. Also noted, not carried: a DOI the Ye, Ma & Qian
extractor found on a reformatted page and flagged as unconfirmed.

**None of the corrections moves §5's three points**; point (c) is now worded as a direction, not a formula.

**What the check did not do.** It did not read any source at its pages (§0), did not fetch the two unfetched sources,
and did not test the CONJECTURE of §4 against L2's model, which is not yet fitted.

*Provenance: Cowork, 2026-10-07 (Stockholm), the sitting booted on entry 319. The user's words: the opening instruction;
"put this research-iteration in the plan as you suggested, then carary on."*

# Research grounding — how published key-tracking avoids drifting (the OI-141 direction)

> **Cowork, 2026-07-12.** The user's direction at the OI-141 diagnosis: *"let us solve
> the incorrect drifting. Do a specific target search and read algorithms, software,
> research etc to see how others avoid drifting."* This document is that targeted (#2)
> search's result: findings cited, claims labeled by how they were verified, honest
> uncertainty flags at the end. It GROUNDS the coming design conversation; it decides
> and builds nothing. Sources: the repository's own prior research holdings FIRST
> (`contrapunctus_findings.md`, compiled 2026-06-20/26 — mined after the user caught
> this search starting on the web instead of at home), then the literature.

## 1. The measured problem this answers (our own facts, all from committed artifacts)

- Against the expert LOCAL key line our analyzer agrees on **65.72 / 62.49 / 65.39 %**
  of duration (Baroque/Jazz/Default); against the HOME key **71.29 / 67.49 / 70.52 %**
  (the ratified post-correction baselines). The home column exceeding the local column
  quantifies our dominant behavior: **stickiness — we under-follow local tonal
  motion.** On top of it, the diagnosis measured **wrong-key-area drift** (settling in
  the dominant's / subdominant's / a distant area) as the largest genuine error class,
  ahead of relative-key confusion.
- One drift mechanism is hand-traced (`bwv369@10080`): the correct key was among the
  carried candidates at the run's edges and **fell off the short carried list
  mid-run**, unable to return.
- The key layer's decision constants — the mode priors, emission weights, change
  costs, hysteresis margins — are **hand-set and unfit** (register rows OI-91/OI-97);
  the carried alternatives are unranked and unconsumed (OI-75/OI-81); the
  phrase-boundary view and the cadence/modulation machinery exist, **built and
  dormant** (the layer-5 audit; `phraseboundaryview` gated off).

## 2. The core published recipe (VERIFIED IN-PAPER: Temperley, "A Bayesian Approach to Key-Finding", ICMAI 2002 — fetched and read in full)

- **The shape:** per-segment key-profile scores + ONE "change penalty", combined
  additively; the optimal ANALYSIS OF THE WHOLE PIECE (a key label per segment) found
  by **dynamic programming over the full key lattice — all 24 keys, every segment, no
  pruning**. In his words: "key has a kind of inertia; once we are in a key, we prefer
  to remain in that key unless there is strong evidence to the contrary." The inertia
  is ONE explicit, tunable constant — and he TUNED it on the evaluation corpus for
  optimal performance (83.8 % segment accuracy on Kostka–Payne).
- **His error taxonomy, 2002, is OURS, 2026:** the model's errors were (1) **wrong
  modulation rate — "it sometimes modulated where the correct analysis did not
  (perhaps treating something only as a … 'tonicization'), or vice versa"** — our
  tonicization-versus-modulation class, verbatim; (2) chromatic harmonies (augmented
  sixths) mis-keying; (3) pitch spelling: a **spelling-aware (tonal-pitch-class)
  variant scored HIGHER (87.4 % vs 83.8 %)** — spelling is key evidence (our OI-15
  spelling-channel thesis, corroborated at the source).
- **Input weighting:** his flat-input form (a pitch class counts once per segment,
  presence not weight) **substantially beat** duration/repetition weighting —
  repeated notes over-weight a single degree. Corpus- and segmentation-specific, but
  a cheap check against our emission scoring's weighting.
- **Ambiguity as near-ties:** an ambiguous passage is one where several key analyses
  are "more or less tied for first place" — the principled basis for publishing the
  runner-up margin we currently discard.

## 3. The software evidence

- **Contrapunctus** (the repository's own dossier, `contrapunctus_findings.md` —
  their published claims, methodology unusually rigorous, not independently re-run):
  - **"Never learn keys; do learn the chord label."** Learned key detectors improved
    per-beat key accuracy yet **regressed chord identification by 5–9 points**,
    because what chord analysis needs is the **STRUCTURE of the key timeline — long,
    phrase-aligned key spans** — and a learned detector's short spurious segments
    each poison several chords around them. Stability is a first-class objective;
    per-beat correctness is not the target. This is the sharpest published statement
    of the drift problem found anywhere in this search.
  - Their **single biggest inter-release win (+10.9 points on Brahms)** came from a
    key-detection fix aligning key spans to phrase boundaries ("pseudo-fermata").
    **Phrase-aligned key runs are their working recipe** — and our phrase-boundary
    machinery exists, dormant.
  - Architecture: **rule-based key detection** (three detectors — HMM / hybrid /
    heuristic — routed per piece by a texture classifier), rule-based candidates, a
    small learned re-ranker for the CHORD label only.
- **music21** (public code): windowed Krumhansl–Schmuckler key analysis, window by
  window, **no transition penalty, no global optimization** — the naive baseline; in
  Contrapunctus's benchmark it places last even when handed the key. Useful only as
  the floor that shows why inertia/penalty structure matters.
- **Melisma (Temperley & Sleator, public code):** the reference implementation of
  the §2 recipe — the one public codebase implementing full-lattice DP key tracking
  with a change penalty. Worth reading at source when the design conversation opens.

## 4. The wider field (abstract-level — see the flags)

- **Local-key estimation is a named subfield** with the same struggle we measured:
  predicted local keys do not map cleanly onto theorists' modulation-versus-
  tonicization distinction. **Nápoles López et al., "On Local Keys, Modulations, and
  Tonicizations" (DLfM 2020)** built an annotated dataset connecting the three
  concepts and evaluated whether algorithmic local keys align better with modulations
  or tonicizations — external validation of our dual-column decision, and a possible
  calibration corpus for our tonicization boundary (`github.com/DDMAL/key_modulation_dataset`).
- **Feisthauer et al., "Estimating keys and modulations in musical pieces" (SMC
  2020):** three key-proximity measures — including the **current diatonic pitch
  set** and a **dominant-to-tonic progression heuristic** (cadence-shaped evidence) —
  combined by **dynamic programming into an optimal "tonal plan"** with key-change
  costs; 84.8 % keys correct on 38 Mozart quartet movements. Cadence evidence inside
  the key decision, published and quantified.
- **The HMM tradition** (Noland & Sandler on chord-sequence key tracking; Schreiber &
  Müller on local key in audio; Chai & Vercoe on key-change detection): transition
  matrices structured by **key proximity** (neighboring keys likelier), decoded by
  Viterbi; smoothing/segment-minimization is standard. One caution our diagnosis
  adds: our drift lands exactly on NEIGHBORS (dominant/subdominant areas), so
  neighbor-friendly transition priors alone do not prevent our failure mode — the
  discriminating evidence must come from elsewhere (cadences, phrase ends, spelling).

## 5. What this grounds for our key layer (implications, each tied to the facts above)

1. **Pin the mechanism before any design (a #17 ledger item, checkable at code):**
   the literature's decoders run the FULL key lattice — nothing can fall out of the
   search, only be outranked. Our hand-traced failure was a key falling off a short
   CARRIED list. Whether our layer-3 decode itself is full-lattice while only the
   carry is pruned, or the search itself prunes, decides the fix's shape — verify at
   the code, not from memory, before the design conversation.
2. **The change penalty / hysteresis is THE central constant of the whole tradition —
   and ours is hand-set.** Temperley tuned his on data; ours (the change costs,
   hysteresis margins, mode priors — OI-91/OI-97) have never been fit. The
   **local-key column now exists as the honest fitting objective** for exactly these
   constants at the fitting stage. This is the cheapest grounded lever: fit before
   restructuring.
3. **Both our failure modes are the same knob's two directions:** stickiness
   (under-following local motion — the home-versus-local gap) and area-drift
   (wandering and staying) are under- and mis-penalized transitions. The literature's
   single-penalty-plus-strong-evidence design says: make the evidence better and fit
   the penalty, rather than adding mechanism.
4. **The grounded evidence enrichments, in order of external support:** phrase-
   boundary alignment of key spans (Contrapunctus's biggest win; our view exists,
   dormant); dominant-to-tonic / cadence evidence in the key decision (Feisthauer,
   published; our cadence machinery exists, dormant, certified); spelling as key
   evidence (Temperley, verified in-paper, +3.6 points; our OI-15 channel). All three
   consume things we already compute.
5. **Rank and publish the near-ties:** ambiguity-as-near-ties (Temperley) is the
   principled form of the carried-alternatives ranking the register has tracked as
   waste (OI-75/OI-81) — the runner-up margin is the natural confidence for any
   future consumer.
6. **Do not learn the key layer** (Contrapunctus's benchmarked negative result, their
   strongest-worded rule) — consistent with our architecture; effort goes to evidence
   quality, span structure, and fitted constants.

## 6. Uncertainty flags (honest, #1)

- Temperley 2002 is **verified in-paper** (fetched, read). Melisma and music21 are
  public code but were NOT re-read in this pass — code-level claims about them are
  from documentation and the dossier.
- Feisthauer, Nápoles López, and the HMM/audio line are **abstract-level**: the HAL
  repository blocks automated fetching; percentages and mechanism details are from
  abstracts and result summaries, not full texts. Do not cite their internals as
  established without a full-text read.
- All Contrapunctus figures and negative results are **their own published claims**
  (the dossier's standing caveat); rigorous methodology, not independently re-run.
- The flat-input-beats-weighted finding is specific to Temperley's corpus and
  segment scheme — check against our emission scoring before importing.
- The "our decode may already be full-lattice" question in §5 is deliberately left
  OPEN — it is the first checkable premise of the design conversation, not a fact.

*Cross-references: OI-141 (the question), OI-91/OI-97 (unfit constants), OI-75/OI-81
(unconsumed ranking facts), OI-15 (spelling channel), OI-94 (notated key change not
re-anchored), the OI-142/OI-143 re-baseline (the honest columns this work will be
measured against), `contrapunctus_findings.md` §2/§5/§10,
`cc_key_mode_inference_diagnosis_report.md` (the failure taxonomy).*

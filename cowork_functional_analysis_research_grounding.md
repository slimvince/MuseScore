# Research grounding — functional-harmony selection, the joint key/chord step, and the correctness-signal question

> **Purpose:** published-fact grounding (principle #1) for the engage arc's upcoming design work — how Layer 5
> should select among candidate chord readings, how the owed joint key-and-chord step should be built, and
> what functional signal could eventually recover the corrections the fine-grain override gave up. **Scope:
> specific research targeting our open questions (#2), not a general survey.** Provenance: two parallel
> web-research passes (Cowork, 2026-07-06), cite-only-what-was-found, uncertainty flagged. Feeds the Layer 5
> engagement design dispatch (engage arc #4+) and the eventual joint-step design.

## 1. The correctness-signal question — the literature CORROBORATES our finding

Our Phase-3 measurement found that a licensed-progression-plausibility signal (counting V→I / ii→V-type
motions) is **uncorrelated with chord-root correctness** — it tidies the functional story while overriding
vertically-correct roots. The published record independently supports this, which means our result is a
**#1/#3 diagnosis confirmed, not an anomaly**:

- **Korzeniowski & Widmer, ISMIR 2018** ("Automatic Chord Recognition with Higher-Order Harmonic Language
  Modelling" [arXiv 1808.05341] + "Improved Chord Recognition by Combining Duration and Harmonic Language
  Models" [arXiv 1808.05335]): chord-**transition** language models mostly *smooth* predictions and give only
  **marginal** accuracy gains; when they disentangled the temporal model, the useful part was chord
  **duration**, not chord **transition**. This is close corroboration — progression-likelihood is a known
  weak/misleading correctness signal.
- **Vuvan et al., Music Perception 39(1), 2021** ("Effects of Chord Inversion and Bass Patterns on Harmonic
  Expectancy"): n-gram progression frequency explained listener expectancy **only in some progressions, not
  all** — a conditional, uneven predictor. Used as a global correctness signal it will over-fire exactly where
  it carries no information (our observed failure mode).

**What IS predictive of the correct root** (the principled path to eventually recover the 53 corrections — a
signal, not another hand-tuned progression bonus):

- **Bass note / inversion — a strong, semi-independent evidence channel.** Vuvan et al. (2021) experimentally
  *dissociate* bass pattern from pitch-class content and show both independently drive harmonic expectation
  (listeners rank inversions of the true chord above a triad sharing only the bass). This is why AugmentedNet
  gives bass its own input block and the graph models carry a bass sub-task. **Likely our best lever against
  wrongly-overridden roots.**
- **Pitch spelling** — disambiguates enharmonic roots that pitch-class-blind vertical fit cannot (Micchi et
  al. 2020; McLeod & Rohrmeier 2021). Directly relevant to our symmetric-chord rotation churn.
- **Metric position / harmonic rhythm** — core node features in the current best models (ChordGNN 2023;
  AnalysisGNN 2025), used as *features*, not hand-weighted priors.
- **Joint consistency across key/root/inversion/bass** — see §2.

## 2. How Layer 5 selection should work (choosing among candidate readings by context)

- **The decisive published lesson: select by JOINT CONSISTENCY, not by strengthening any single score.**
  ChordGNN (Karystinaios & Widmer, ISMIR 2023) *wins* on the full Roman-numeral label while scoring *lower*
  on the individual key/degree/quality heads — the payoff is making the reading mutually consistent across
  key/root/inversion/bass, not a stronger vertical or progression score. AnalysisGNN (2025) confirms: a
  logit-fusion layer that reconciles the task heads improves both harmony and cadence. This is the direct
  analog of our selection problem and a strong steer for the Layer 5 objective.
- **Modern ML shape:** multi-task shared representation predicting key + degree + quality + inversion + root
  together (Chen & Su 2018; Micchi et al. 2020; AugmentedNet, Nápoles López et al. 2021). AugmentedNet also
  predicts **root redundantly** and reports the redundancy *helps* — an interesting counter to strict
  no-duplication at the learning level (a modeling choice, not a code-duplication issue).
- **Classic model-based options give principled confidence:** HMM with Viterbi/forward-backward posteriors
  (Raphael & Stoddard 2004); Bayesian posteriors (Temperley); grammar-derivation probabilities (Rohrmeier
  2011; Harasim et al. 2018). McLeod & Rohrmeier (2021) is the closest published architecture to a
  candidate-scoring + context-selector pipeline (separate probabilistic modules per aspect, each emitting a
  probability) — worth studying for the Layer 5 structure.
- **Calibration — we are AHEAD of the field here.** No music-specific calibration/reliability study for
  Roman-numeral analysis was found; softmax posteriors are known to be over-confident/uncalibrated. Our
  Stage-5 isotonic reliability-map work is exactly what the published field lacks — a point of confidence in
  our confidence-contract direction, and a reason to treat any learned model's raw scores as uncalibrated.

## 3. The owed joint key-and-chord step (Q2)

- **Joint beats sequential, and the win is concentrated where OUR errors are.** The uniform theme (Raphael &
  Stoddard 2004; Pauwels & Martens 2014; Wu & Yoshii 2022) is that jointly modeling the key↔chord mutual
  dependency disambiguates **hard/ambiguous cases** — symmetric/ambiguous chords whose root only resolves once
  the key is chosen. That is precisely where our residual errors concentrate.
- **The coupling that recurs:** model P(chord | key) together with a **key-transition prior that penalizes
  rapid key flip-flop** (Raphael & Stoddard; Temperley). Raphael & Stoddard use a single hidden state
  `(tonic, mode, chord-function)` — key and chord are *one* state, and they note modulations mirror chord
  moves (V/V represented as momentary modulation).
- **The design taxonomy for our exact choice:** Wu & Yoshii (2022, APSIPA) build and compare **parallel /
  branching / sequential** couplings — the sequential one infers chord then key-from-chord-only, exactly the
  pipeline we're trying to escape. (Flag: their winning percentages were behind a paywall/truncated — the
  taxonomy is verified, the exact deltas are not.)
- **Avoid the documented failure mode:** a hard early decision that truncates the downstream hypothesis space
  (Pardo & Birmingham's independent segmentation; our key-then-chord). The fix that recurs: **carry a beam of
  (key, chord) hypotheses and let downstream chord evidence re-rank the key** — literally our "reconsider the
  chord under alternative candidate keys, and vice versa."
- **Magnitude realism:** where quantified (AugmentedNet), the joint/multi-task uplift is **low single-digit
  points per task**, concentrated in the reconstructed full label; often joint modeling buys the *second*
  variable at near-zero cost to the first (Papadopoulos & Tzanetakis). The big win is qualitative
  (hard-case disambiguation), which is the right expectation to set for the joint step's payoff.

## 4. Implications for our design

1. **Recovering the fine-grain override's lost corrections is a bass/inversion + spelling + joint-consistency
   problem, NOT a better progression count.** The literature says the signal we lacked is there — in the bass
   channel, spelling, and mutual consistency — but it is emphatically not a stronger licensed-progression
   term. This is the principled path (#4) and it keeps us off the dead-end we already hit (#3).
2. **Layer 5's selection objective should reward joint consistency across key/root/inversion/bass, not
   maximize one vertical or progression score.** Grounded in ChordGNN/AnalysisGNN — design it this way from
   published fact rather than inventing (#1).
3. **The joint key-chord step should carry a beam of (key, chord) hypotheses with a key-transition penalty,
   not commit to key first.** Directly grounds the owed joint step; matches where our errors live.
4. **The bass note is a high-value, well-grounded, semi-independent lever** — worth foregrounding in both the
   Layer 5 selection and the joint step.
5. **Our calibration work is ahead of the field** — a reason to keep the confidence-contract discipline and to
   treat any imported model's raw scores as uncalibrated.

## Uncertainty flags (honest, #1)
- Pauwels & Martens (2014) and Wu & Yoshii (2022) — architectures and joint-vs-sequential *framing* verified;
  exact percentage deltas NOT verified (paywalled/truncated). Do not cite specific numbers from these.
- Mauch & Dixon (2010) 71% is from the paper record, not a within-paper joint-vs-sequential ablation.
- Calibration guidance is inferred from general ML (no music-specific study found).
- Vuvan et al. (2021) cited by article record; first-author attribution by the article URL.

## Sources (verified by the research passes)
Korzeniowski & Widmer, ISMIR 2018 (arXiv 1808.05341, 1808.05335) · Vuvan et al., Music Perception 39(1), 2021 ·
Chen & Su, ISMIR 2018 / TISMIR 2021 · Micchi, Gotham & Giraud, TISMIR 2020 · Nápoles López, Gotham & Fujinaga
(AugmentedNet), ISMIR 2021 · Karystinaios & Widmer (ChordGNN ISMIR 2023; AnalysisGNN arXiv 2509.06654, 2025) ·
Raphael & Stoddard, ISMIR 2003 / CMJ 28(3) 2004 · Pardo & Birmingham (HarmAn), CMJ 2002 · Temperley (Bayesian
key-finding; Unified Model, JNMR 2009) · Rohrmeier, J. Math & Music 2011; Harasim et al., ISMIR 2018 · McLeod &
Rohrmeier, ISMIR 2021 · Mauch & Dixon, 2010 · Papadopoulos & Tzanetakis (Markov Logic), 2012/2017 · Pauwels &
Martens, JNMR 2014 · Wu & Yoshii, APSIPA Transactions 11(1), 2022.

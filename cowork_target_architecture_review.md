# Target Architecture Review — Mode / Functional-Chord / Actual-Chord Inference

*Cowork, 2026-06-10. Documents-only review (no source code read for this exercise).*
*Inputs: `docs/redesign_plan.md`, `docs/scoring_model.md`, `docs/layer_architecture_audit.md`,
`ARCHITECTURE.md` (§2.2, §2.14, §4.1, §4.2, §5.2, §5.3, §5.6, §5.8), `docs/unified_analysis_pipeline.md`,
`COWORK_HANDOFF.md`, plus published literature for comparison.*

**Question asked:** If the goal is maximally *correct* inference of (a) mode/key, (b) functional
chord, and (c) actual sounding chord — is the proposed target architecture and its algorithms
the correct choice?

**Short answer:** The layering, the evidence-forwarding principle, and the engineering discipline
are right. The algorithmic core — greedy left-to-right commitment with hand-calibrated additive
bonuses and post-hoc correction gates — is not the correct end state, and the documents
themselves contain the proof. The system has spent ~97 iterations hand-building, gate by gate,
an approximation of what joint segmentation-plus-labeling via global optimization (dynamic
programming over a candidate lattice) provides by construction. Phase E as currently sketched
risks becoming another generation of bespoke local signals rather than the structural fix.

---

## 1. What the target architecture actually is

Distilled from the documents:

1. **Key/mode layer** (`KeyModeAnalyzer`): 12 tonics × 21 modes = 252 candidates scored per
   windowed context (duration/beat/bass-weighted, exponential decay), hand-set mode priors,
   ranked output — of which only `.front()` is consumed (ranked list discarded; Step 3 shelved).
2. **Segmentation**: greedy-expand regions on simultaneity changes, Pass 2/2b sub-region
   splitting, absorb/coalesce repair passes, exploration scored by the production pipeline in
   `ScoringPhase::Segmentation`.
3. **Vertical oracle** (`analyzeChord`): 17 tertian templates × 12 roots × bass candidates,
   additive bonuses/penalties + multiplicative factors, ~30 hand-calibrated constants.
4. **Competition pipeline** (`applyHarmonicFunction`): progression signals (rcb, w_seq, w_dim,
   step bonuses, Gate R), cross-bass winner selection. Single commit path (Phase E Step 5, done).
5. **Post-scoring gates A–L + Iter 86/91 + pedal pass**: post-hoc winner corrections.
6. **Inter-region channel**: committed identity + (since Steps 1–2) confidence metadata
   forwarded to the next region's context. Strictly left-to-right; one-step lookahead
   (`nextRootPc` etc.) computed cold.
7. **Phase E (planned)**: symmetric forward context, cadence confirmation, voice-leading
   resolution signals, arpeggiated-predecessor rcb suppression, "inter-region revision",
   eventual functional labels (secondary dominants, aug6, tonicization). §2.14 adds optional
   iteration depth (quality levels 0–2).

The architecture principle ("every layer passes full evidence forward, not just the committed
winner; passing a lie is the anti-pattern") is sound and matches how the research literature
has framed this problem for 25 years. The question is what *consumes* that evidence.

---

## 2. The central criticism: the missing algorithm is global decoding, not richer features

### 2.1 Your own documents converge on it

Three independent threads in the project's own analysis all point at the same structural gap:

- **Δ=+7a verdict** (`redesign_plan.md`): *"confidence can't encode 'right now, wrong in 240
  ticks'… when the next region's evidence contradicts the committed predecessor identity,
  revise the predecessor. This is architectural, not a gate."*
- **Δ=+7b mechanism**: oracle near-tie (1.92 vs 1.92), rcb is the sole tiebreaker, and the
  discriminating signal is *which reading makes the better progression* — a property of the
  path, not the region.
- **Finding 7** (`layer_architecture_audit.md`): *"Two-thirds of `applyPostScoringGates` is
  solving one problem… each gate is correct in isolation; the cascade is the symptom of an
  unresolved architectural problem."*

"Revise a committed predecessor when later evidence contradicts it" has a standard name:
**decoding a sequence model**. Viterbi backtracking *is* predecessor revision — every local
commitment is provisional until the globally best path is selected over the whole piece (or a
beam window). The Δ=+7 cluster, the rcb dead ends (Iter 98, predecessor-confidence survey),
and the B/C/D→G-B/C/D→H-B/C/D cascade pattern are all instances of the same defect: **local,
irrevocable argmax with first-order patch-up**, where the literature does **joint global argmax**.

### 2.2 The published baseline did this decades ago

- **Temperley & Sleator (Melisma, 1997/1999)**: harmonic analysis as dynamic programming
  (Viterbi) over root/key states with compatibility and ornamental-dissonance preference rules.
  Hand-built rules, like yours — but *globally decoded*. Near-ties are resolved by path score;
  "wrong in 240 ticks" is impossible by construction because nothing is committed until the
  whole path is scored.
- **Pardo & Birmingham (HarmAn, 2002)**: template scoring (six template classes — a direct
  ancestor of your 17-template oracle) with **segmentation chosen by optimizing total segment
  score over the piece**, not by greedy expansion plus repair passes (absorb, coalesce,
  sub-region splitting).
- **Masada & Bunescu (2017/2019, segmental CRF)**: joint segmentation + labeling in one
  model, exactly the "segmentation ↔ chord" circularity §2.14 worries about — dissolved by
  optimizing both simultaneously. Weights *learned* from labeled data rather than hand-tuned.
- **Nápoles López et al. / key analysis HMMs**: local key as a hidden state sequence with
  transition penalties — modulation detection and key smoothing fall out of the decode, no
  hysteresis/`promoteWinnerInPlace` machinery (which your own Step 3 investigation found
  produces unreliable `normalizedConfidence`).

Your oracle ≈ their emission model. Your rcb/resolution/step bonuses ≈ their transition
model. Your gates ≈ hand-coded re-ranking that DP makes unnecessary. The mapping is nearly
one-to-one — except the decoder.

### 2.3 Why this matters for each of the three inference targets

**Mode/key.** Scoring 252 candidates per window is more ambitious than most published systems
(which do 24–48 keys); the windowed weighting is close to standard profile methods. But key is
committed per window with ad-hoc smoothing, the ranked distribution is discarded, and a wrong
key poisons every diatonic-sensitive term downstream with no recovery path. A key HMM (states =
key×mode, emissions = your existing window scores, transitions = modulation penalty by
circle-of-fifths distance) is strictly better-suited to the stated goal and reuses your scoring
intact. It also gives `KeyArea` spans (already wanted by `unified_analysis_pipeline.md`) as the
natural output of the decode rather than a post-grouping.

**Actual chord.** The vertical oracle is genuinely good and worth keeping — the joint
(bass,root,template) grid, TPC-aware spelling, the dim7 rotation selector, `hasStructuralBass`
are real domain knowledge that any framework would want as features. The weakness is not the
oracle; your own Δ=+7a dump proved the oracle prefers the right answer in the present-root
slice. The weakness is what happens *between* regions.

**Functional chord.** This is where the current plan is thinnest. The corpus analysis already
established the ceiling: `key_disagree` 15.4% (~9,440 regions), Maj→Dom7 and Min↔Maj closed as
"convention gaps" because DCML labels *implied/functional* harmony while the system labels
*sounding* harmony. Function is a property of a chord's role in a progression toward a cadence
— inherently a sequence-level inference. Phase E's sketch (cadence-confirmation bonus,
voice-leading signal, arpeggiated-predecessor rcb gate) adds more local features to a greedy
pipeline. The published treatments model function explicitly: as a state machine / grammar over
T–S–D functions (Rohrmeier's harmonic grammar; functional-harmony models in the
Chen & Su / AugmentedNet lineage that predict key, degree, quality, inversion *jointly*). A
functional layer that is itself a sequence decode (chord candidates × functional states) gets
secondary dominants, tonicization-vs-modulation, and cadence detection as path properties —
not as N more gates.

### 2.4 The calibration trap

`scoring_model.md` §8 is a list of fourteen load-bearing constraints, four of them "dead ends —
do not re-attempt." Every constant (0.40, 0.75, 0.35, kStepBudget≈0.21, caps 2.5/0.6/2.0…) is
hand-calibrated against ~51 Bach chorales plus a Jazz preset, with documented combinatorial
interactions (B1, B2×4, B3 failures; four individually load-bearing guards on one 0.10 bonus).
The trajectory is classic local-optimum behavior: Baroque BIR=false 188→13 over ~97 iterations,
and the remaining 13 are *all* classified "Phase E only" or structural. Marginal cost per fix is
rising steeply; the BIR hard-stops (correctly) freeze the current optimum in place.

Two consequences:

1. **Generalization is unproven.** Cross-corpus root agreement 53.8%, rn_agree 27.6%. For
   rough orientation: strict full-RN accuracy (key+degree+quality+inversion all correct) for
   recent neural systems (AugmentedNet 2021, ChordGNN 2023, RNBert 2024) is in the ~45–50%+
   range on multi-corpus benchmarks. The comparison is *not* apples-to-apples (different
   alignment, label vocabularies, corpora) — but the direction and size of the gap is
   informative, and your own metric froze: "rn_agree secondary metric largely frozen without
   Phase E."
2. **Weights should be fitted, not hand-tuned.** You already own everything needed for
   supervised weight calibration: a differentiable-free structured objective (BIR / rn_agree),
   aligned DCML ground truth for 10+ corpora, and a deterministic scoring function. A
   structured perceptron / coordinate search over the ~30 constants against the corpus would
   replace iteration-by-anecdote with fitting — and in a lattice/DP formulation this becomes
   standard CRF-style training (HMPerceptron and the segmental CRF papers did exactly this with
   rule-like features).

### 2.5 An internal contradiction worth resolving

`ARCHITECTURE.md` §2.14 says: *"The correct architecture is layers WITH iteration between
them"* (key↔chord, segmentation↔chord are "intrinsic circular dependencies that a purely
feedforward pipeline cannot resolve"). `redesign_plan.md` (newer) says: *"Iteration is not a
design premise… a single comprehensive pass with symmetric forward/backward scoring addresses
these."* Both documents are circling the same insight without landing on it: the standard
resolution of these circularities is neither feedforward-with-more-features nor ad-hoc
iteration — it is **joint inference over a hypothesis lattice**. DP over (segmentation ×
chord × key) hypotheses *is* "a single comprehensive pass" in the only sense that matters,
and it *is* the fixpoint that iteration would converge to, computed exactly. The two documents
should be reconciled by naming the actual target.

---

## 3. What is right and should be kept

- **The oracle/competition split (E2d) and the single commit path (Step 5).** This is exactly
  the emission/transition factorization a decoder needs. The last two months of refactoring are
  *prerequisites* for a lattice decoder, whether or not that was the intent. The just-completed
  `ScoringPhase` unification means segmentation hypotheses and final scoring share one model —
  also a precondition for joint segmentation+labeling.
- **Evidence forwarding ("don't pass a lie").** Correct, and the literature agrees — that's
  what a lattice is: *all* the evidence, none of the premature commitment.
- **Domain heuristics as features.** dim7 rotation selection via non-diatonic ♭♭7, TPC
  spelling consistency, `hasStructuralBass`, duration/metric NHT weighting (which matches
  Melisma's ornamental-dissonance treatment) — these survive any re-architecture as emission/
  transition features. Nothing is wasted.
- **The evaluation infrastructure.** Aligned DCML comparison across 10 corpora, BIR hard
  stops, byte-identity refactor discipline, dead-end documentation. This is better experimental
  hygiene than many published papers, and it is precisely what makes a decoder migration or
  weight-fitting verifiable.
- **Interface-based ML substitutability (§2.2)** — keeps all options open.
- **The quality-level concept (§2.14)**: real-time level 0 = greedy/beam-1 decode; deeper
  levels = wider beam / exact DP. The decoder framing makes the quality knob principled
  (beam width) instead of "which feedback loops are on."

---

## 4. Honest verdict and recommendation

**Is the proposed target architecture the correct choice for maximal correctness?** As layering
and as evidence philosophy: yes. As algorithm: no — not in its current trajectory, where
Phase E is sketched as more locally-applied signals (cadence bonus, arpeggio-predecessor
detection, voice-leading checks) feeding the same greedy left-to-right commitment.

**Recommendation, in order of leverage:**

1. **Make Phase E a decoder, not a feature pack.** Target: the oracle emits per-region ranked
   candidates (it already does — `ScoringSnapshot` / `results[]`); transition scores = rcb +
   resolution + step + cadence/functional patterns; decode the best chord path per piece with
   Viterbi/beam over regions. This *subsumes* Gate R, the rcb dead ends, Iter 91, and the
   planned "inter-region revision" in one mechanism, and it directly fixes the documented
   Δ=+7a/Δ=+7b failure mode class. Existing gates remain as a comparison baseline during
   migration; BIR/byte-identity infrastructure verifies each step.
2. **Key as a path, not a point.** Key HMM over the existing 252-candidate window scores;
   `KeyArea` spans fall out. Resolves the Step-3 dead end (ranked list discarded) without
   trusting the broken `normalizedConfidence` — the decode uses raw scores.
3. **Fit the weights.** Once scoring is a path objective, calibrate the constants against the
   DCML corpora by structured learning or even plain coordinate descent, with the existing
   hard-stop metrics as constraints. Stop hand-tuning.
4. **Functional layer as sequence labeling over the decoded chord path** (T/S/D states,
   secondary-dominant and aug6 patterns, tonicization vs modulation from the key path). This
   is the only credible route to closing key_disagree (15.4%) and the implied-harmony
   convention gaps — they are unreachable from vertical evidence by your own closed
   investigations.
5. **If maximum corpus accuracy ever becomes the overriding goal**, the ceiling is a neural
   proposal model (AugmentedNet/ChordGNN/RNBert class) decoded with the same lattice machinery
   — RNBert itself decodes with a CRF on top of a transformer. The §2.2 interfaces make this a
   drop-in. The rule-based lattice system remains the explainable, training-data-free,
   incremental-editing-friendly default — legitimate product reasons to keep it primary.

**Risk assessment of the recommendation:** lower than it appears. The expensive assets (oracle,
corpus tooling, tests, golden snapshots) are unchanged; the decoder replaces exactly the parts
the project's own audits flag as accumulating debt (gate cascades, rcb patches, greedy
commitment). The biggest genuine cost is re-verifying the Baroque calibration under a new
objective — which the BIR/byte-identity infrastructure was built to do.

---

## 5. Literature references used for comparison

- D. Temperley, "An Algorithm for Harmonic Analysis," *Music Perception* 15(1), 1997
  (Melisma / Viterbi DP; preference rules).
- B. Pardo, W. Birmingham, "Algorithms for Chordal Analysis," *Computer Music Journal* 26(2),
  2002 (HarmAn: template scoring + global segmentation optimization).
- K. Masada, R. Bunescu, "Chord Recognition in Symbolic Music: A Segmental CRF Model…,"
  *TISMIR* 2019 (joint segmentation+labeling, learned weights; comparative eval vs Melisma,
  HarmAn, HMPerceptron).
- N. Nápoles López, M. Gotham, I. Fujinaga, "AugmentedNet: A Roman Numeral Analysis Network…,"
  ISMIR 2021 (multi-task key/degree/quality/inversion; multi-corpus RN benchmark).
- E. Karystinaios, G. Widmer, "Roman Numeral Analysis with Graph Neural Networks (ChordGNN),"
  ISMIR 2023.
- M. Sailor, "RNBert: Fine-Tuning a Masked Language Model for Roman Numeral Analysis,"
  ISMIR 2024 (transformer + CRF decoding — note: even the neural SOTA uses sequence decoding).
- M. Rohrmeier, "Towards a generative syntax of tonal harmony," *JMM* 2011 (functional
  grammar; context for the functional-label layer).

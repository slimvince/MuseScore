# Architectural Layer 3 — KEY/MODE — Architecture & Design

> **Status: SIGNED (user, 2026-06-22)** — conditional sign-off met by stating the recognized mode vocabulary
> explicitly (Section 1). **WIRED — AS-BUILT, Step 1 (2026-06-22): the decoder is the live key/mode path.** The
> read-only audit, the decoder build, the unification extraction (the shared `pitchContextOverSpan` view), the
> characterization + causal-decomposition diagnostics, and the bounded sweep are committed and pushed
> (`c453315faa`, `b368f3c631`, `1538193d4d`, `2203ad9fda`). The **Step-1 wiring** — the decoder replaces the
> per-region resolver at the `regionanalyzer.cpp` seam (duration-majority per coarse region; S2 segmentation-stable
> seed; `excludeStaves` + `partialSignatureCorrection` + C1 emission-confidence fidelity fixes) — is committed
> locally (`a6b08af3fe`) under the two-tier BIR gate (the Jazz +1 is an accepted interim class-(a) case, CLAUDE.md).
> **Deferred follow-ups (tracked):** the Step-2 scaleMembership reweight (KEY-metric-gated, chord/BIR-flat); the P4
> tick-local path (still on the resolver → P4-redecode); re-split (c) for within-region modulation; S1 full
> seed-retire; and the sequence-margin confidence redesign. The resolver + `collectPitchContext` remain only as the
> diagnostic/grading baseline. The
> formalized architecture document for the key/mode layer; follows the standard section structure in
> `cowork_design_doc_template.md`. The order the code will be built in (coding increments) is delivery sequencing and
> lives in the delivery plan (`cowork_layer3_keymode_impl_design.md`), not in this architecture document. *(Two template sections do not apply:
> "Deployment view" and "Human-interface design" — backend analysis code, no separate deployment, no user
> interface.)*

## 1. Introduction & purpose
**What Architectural Layer 3 is.** It is the **sole owner of key/mode inference *from the notes***: for each slice
produced by Architectural Layer 2 it ranks the candidate key/modes by how well they fit the pitch evidence, decided
**for the whole run of music at once, as one consistent sequence over time** rather than slice-by-slice. It commits to
a key/mode wherever the note evidence is decisive; where it is not, it records the ranked alternatives and marks the
slice "uncertain" — it does **not** force an answer the notes cannot support.

**The responsibility boundary — stated precisely (because Architectural Layer 3 is NOT the final mode authority for
every case).** Architectural Layer 3 owns two things outright: the **candidate space** (the 252 key/modes) and the
**note-evidence model** — how well each candidate fits the pitch content and the sequence. No other architectural layer
infers key/mode from the notes, and no other architectural layer generates or re-scores key/mode candidates. What
Architectural Layer 3 does **not** own is the *final arbitration of the cases the notes alone cannot decide* (relative
major versus minor; a modulation/tonicization seam): that residual — handed forward as the ranked alternatives plus the
"uncertain" mark — is settled by Architectural Layer 5 using **functional evidence** (chord, cadence,
function) that Architectural Layer 3 structurally cannot have. So key/mode inference is split along an **evidence
boundary**: Architectural Layer 3 contributes the note evidence and resolves everything the notes can resolve; the
gated step contributes the functional evidence and resolves only the flagged residual — by **selecting among
Architectural Layer 3's carried alternatives**, never by inventing a candidate or re-scoring from the notes (that
note-evidence model has exactly one home). Knowing *where the note evidence runs out* is itself part of Architectural
Layer 3's job; the "uncertain" mark is the explicit hand-off token. *(Open item O1, resolved and user-ratified
2026-06-24: that resolver is Architectural Layer 5 (function) itself, performed at its gated entry — not a distinct
box between the note-layers and Layer 5. Same name used in the Layer-4 spec. Evidence:
`cowork_uncertain_resolver_investigation.md`.)*

**A *confident* key is also overturnable (the confidence-weighted override; user-ratified 2026-06-26).** The hand-off
above covers the *flagged* residual. The ratified architecture-wide principle goes further: a key this layer committed
**confidently** can still be overturned by Architectural Layer 5 when a cadence in a candidate key is decisive (the
cadence-confirmed modulation — Layer 5 has cadential evidence this layer structurally cannot). As everywhere, Layer 5
resolves it by **selecting among this layer's carried alternative keys**, never by re-deriving; where the confirming key
was never carried, that is a *coverage* miss widened inside this layer. **Requirement this places on Layer 3 (being
closed byte-identically, 2026-06-26):** the layer already *computes* ranked alternative keys + a confidence on every
slice, but the slice→region reduction currently **drops them** (the region carries only the single chosen key). The
region must **carry the ranked alternative keys + confidence forward** so the override has a menu to select among; this
is an additive forward-carry of already-computed data (no production consumer yet → byte-identical), with a lock-in test.
Full mechanism: `cowork_layer5_function_design.md` §8/§9-D7; `cowork_target_architecture.md` control-flow contract;
close-out: `cc_instruction_l3_keyalt_forwardcarry.md`.

**What music Architectural Layer 3 operates on.** The slices from Architectural Layer 2, over the notes from
Architectural Layer 1, for the user-selected part of the score.

**Why Architectural Layer 3 exists, and why it decides the whole sequence at once.** Deciding the key/mode one
region at a time, in isolation, is the cause of the two largest key/mode errors: (a) it cannot tell **relative major
from relative minor** (those two keys contain exactly the same notes, so a single region has no way to choose
between them); and (b) it **misreads brief tonicizations as real modulations, and sometimes misses real
modulations** (a short borrowed passage looks like a key change to a region that cannot see that the music returns
to the original key right afterward). Both can only be resolved by weighing the surrounding music — which is exactly
what deciding the whole sequence at once does. (The per-region code this replaces is described in Section 13.)

**Scope — what Architectural Layer 3 does:** assign each slice a key/mode, together with ranked alternative
key/modes, a confidence, and an "uncertain" mark where the evidence is genuinely ambiguous.

**What Architectural Layer 3 explicitly does NOT do** (stated because each boundary matters):
- It does **not** name chord symbols (Architectural Layer 4) or function / Roman numerals (Architectural Layer 5).
- It does **not** detect cadences — a cadence is a function-level event, decided later (it tells brief from real
  modulation using its change cost instead).
- It does **not** group equal slices for display (Architectural Layer 6), and does **not** read or change the notes
  or slices (Architectural Layers 1 and 2).
- It does **not** force a single answer on the genuinely ambiguous cases — it marks them "uncertain" and leaves them
  for Architectural Layer 5.
- It does **not** treat the written key signature as the truth (only as a weak hint), and does **not** read back any
  chord, function, or already-decided key.

**Which key/modes Architectural Layer 3 recognizes.** A key/mode is one of the **12 tonal centres** (the twelve
pitch classes) combined with one of **21 modes**, giving 252 possible key/modes. The 21 modes are the seven-note
modes of three parent scales:
- **The seven modes of the major scale:** Ionian (major), Dorian, Phrygian, Lydian, Mixolydian, Aeolian (natural
  minor), Locrian.
- **The seven modes of the melodic-minor scale:** melodic minor, Dorian ♭2, Lydian augmented, Lydian dominant,
  Mixolydian ♭6, Aeolian ♭5 (Locrian ♮2), and Altered (super-Locrian).
- **The seven modes of the harmonic-minor scale:** harmonic minor, Locrian ♮6, Ionian ♯5, Dorian ♯4, Phrygian
  dominant, Lydian ♯2, and the altered-dominant 𝄫7 mode (harmonic-minor mode 7).

**Which key/modes Architectural Layer 3 does NOT recognize.** Any scale that is **not** one of those 21 seven-note
modes — in particular pentatonic and blues scales, the whole-tone scale, the octatonic (diminished) scale, and any
non-Western or microtonal scale (maqam, raga, and so on). A passage genuinely in one of these is reported as the
**closest** of the 21 recognized modes, not as the unrecognized scale. (Recognizing all 21 modes does not mean all
21 can be *measured*: the human Roman-numeral ground truth used to grade this layer, Section 10, is major/minor
only, so modal readings beyond major/minor can be produced but cannot be checked against that ground truth — see
Section 11.)

## 2. Constraints
- **Key/mode only;** the only evidence it may use is the notes — which pitches sound, and how much each is
  emphasised (by being in the bass, on a strong beat, or sounding often). It may **not** use chord symbols,
  function, or cadence detection, because those are decided in later architectural layers and using them here would
  reverse the dependency order.
- **Its output states its own certainty.** It commits to a key/mode where the note evidence is decisive, and where
  the evidence is genuinely ambiguous it instead records ranked alternatives and marks the slice "uncertain" rather
  than forcing a single answer. The genuinely ambiguous cases (relative major/minor, and modulation boundaries) are
  exactly the cases that need chord evidence to settle, which happens in Architectural Layer 5 — so forcing
  an answer here would be both premature and would block that later step.
- **It changes analysis output** (unlike Architectural Layers 1 and 2, which do not), so it is judged by accuracy
  measurements, not by producing byte-for-byte identical output; the pinned analysis snapshots are refreshed only
  after a change is confirmed correct.
- **Works on the user's selected music, at any size and in any musical style** (its *structure* makes no assumption
  about style).
- **This is the first architectural layer where the user's style preset (Standard / Baroque / Jazz / …) is used.**
  Architectural Layers 1 and 2 are pure facts and use no preset. The preset enters here as a **weak prior on which
  of the 21 modes are likely in this style** — the per-mode bias values in the scorer (Baroque pushes the prior
  toward major and minor; Jazz raises the modal and altered modes; "Standard" sits between). It is deliberately
  weak: the note evidence is primary and overrides it, so the preset only tips genuinely ambiguous cases (the same
  stance taken toward the written key signature). The preset is used again in later architectural layers (chord
  symbols, function); this layer is only where it *first* applies.
- **It may need more music than the user selected.** To judge the opening of a selection, it sometimes needs to see
  the key the music was in **earlier in time than the point where the selection begins**. When it does, it asks
  **Architectural Layer 1 to widen the analysed span earlier in time** and supply those earlier notes. Architectural
  Layer 3 is the *requester* of more music; Architectural Layer 1 is the *supplier*. This reach-back **is an extension
  request** in the bounded-context contract (`cowork_bounded_context_design.md`): direction = earlier in time, stop
  condition = *"the prevailing key before the selection is in view,"* hard bound = a maximum reach, terminating at the
  score start. **(Built — gated OFF by default. The reach-back loop is built in the orchestrator
  (`regionanalyzer.cpp:585–666`): trigger = the selection's leading-edge slice is unsettled, action = ask
  Architectural Layer 1 to `extend(Earlier)` → re-slice (Layer 2) → re-decode (Layer 3), repeated until the
  leading-edge key stops changing, the hard bound (max reach) is hit, or the score start is reached; output = the
  selection only. It rides on Architectural Layer 1's `extend` (now built). It is a **parameter** on `analyzeRegions`
  (`opts.reachBack.enabled`, default false), so the production path stays whole-score and reach-back never fires
  there. The scenarios and glossary below describe the as-built behaviour.)**
- **It is not responsible for noticing when the score has been edited.** Deciding that the analysis is out of date
  and must be re-run is the caller's responsibility, not Architectural Layer 3's.
- **The score's written key signature is treated as a weak hint only, not as the truth** — the key/mode is inferred
  primarily from the notes.

## 3. Context & scope (external view)
**What Architectural Layer 3 reads (its inputs):** the slices from Architectural Layer 2; the notes from
Architectural Layer 1 (to score how well each candidate key/mode fits the notes in and around a slice); the existing
per-window key/mode scorer (reused unchanged); and Architectural Layer 3's own tunable settings.
**What Architectural Layer 3 offers (the operations other code calls):**
- *Decide the key/mode sequence* — given the slices, return one result per slice: the chosen key/mode, its ranked
  alternatives, a confidence, and the "uncertain" mark.
- *Re-decide a sub-range* — re-run the decision over just part of the sequence, holding fixed the key/mode at the
  two ends of that part, so that after a small score edit only the edited neighbourhood is re-decided rather than
  the whole piece.
**Who uses Architectural Layer 3 (its consumers):** the region analyzer (the code that asks for the key/mode of each
region); Architectural Layer 4 (it reads each slice's chosen key/mode as a starting assumption for the chord
symbol); and Architectural Layer 5 (function), which settles the cases Architectural Layer 3 marked "uncertain."
**What Architectural Layer 3 deliberately does not read:** chord symbols, function, cadences, or any already-decided
key fed back to it.

**Implementation (source files).** The decoder is `src/composing/analysis/key/keymodesequence.{h,cpp}`
(`KeyModeSequenceDecoder`, `SliceKeyMode`, the decoder-private settings `KeyModeSequencePreferences`). The per-slice
scoring window is built by the shared, indexed derived view `pitchContextOverSpan` in
`src/composing/analysis/engravingbridge/regiontoneprimitives.cpp` (declared in `regiontonecollector.h`, beside
`weightedPcView` / `soundingAt`). The per-window scorer it reuses unchanged is `KeyModeAnalyzer`
(`keymodeanalyzer.{h,cpp}`), with the additive `keyModeSignatureFifths` accessor for labelling each candidate's
key signature. The read-only grading diagnostic is `batch_analyze --decode-keymode`.

## 4. Solution strategy
Place the slices left-to-right in time. For each slice, the existing scorer rates every candidate key/mode by how
well it fits the notes in and just around that slice (a **local-fit score**). Picking one key/mode per slice and
reading them left-to-right gives a **sequence**. Architectural Layer 3 chooses the single best sequence: the one
with the highest total local-fit, minus the cost of every key/mode change along the way — **both measured on one
common scale** (the change cost is expressed in the same units as the local-fit score, so the single sum is
meaningful). The change cost makes keeping the current key/mode cheap and changing it expensive — more expensive the
further the new key is from the current one, **measured as circle-of-fifths (key-signature) distance** (the number of
signature steps between the two keys' parent tonics; `C`→`F♯` and `C`→`G♭` both = 6 — not semitone distance and not a
count of differing scale tones), and most expensive of all between relative major and relative minor (the hardest
pair). The effect: a brief excursion is not worth the change cost over so few slices, so it stays in the original key;
a sustained modulation is worth it, so the key changes; and the relative-major-versus-minor choice is settled by which
reading fits the whole run of music, not one ambiguous slice. **There is no "how many slices" threshold for
brief-versus-sustained — it is purely this fit-versus-cost arithmetic** (a duration threshold a reader might expect
does not exist). The best sequence is found with the standard, fast
best-sequence algorithm (described in Section 5). This is the well-established way key-finding handles local keys and
modulation, applied here on Architectural Layer 2's slices and reusing our existing scorer.

## 5. Building-block view (static / internal structure)
Deciding the sequence has four steps:
1. **Local-fit scoring.** For each slice, score every candidate key/mode using the existing scorer, reading the
   notes in and just around that slice **through the Architectural Layer 1 note model's indexed query** ("which
   notes sound between A and B") — **not** through the older direct-score-walk pitch collector, which would scan the
   notes from the start each time and bring back the O(N²) cost the indexing was added to remove. Keep only a short
   list of the best-scoring candidates **plus the key/mode the sequence is currently in** — keeping the current
   key/mode on the list even when a single slice scores something else higher is what stops a brief excursion from
   throwing away the established key.
2. **Change cost.** Define the cost of moving from one key/mode to another between consecutive slices: zero to stay;
   otherwise a base "change penalty" plus an amount that grows with how far apart the two keys are, plus an extra,
   large penalty for the relative-major/relative-minor switch specifically.
3. **Best whole sequence.** Find the single sequence of per-slice key/modes with the highest total (local-fit minus
   change cost) using the standard best-sequence algorithm — it sweeps once from the first slice to the last,
   keeping, for each candidate at each slice, the best running total that ends there, and then traces the best
   ending back to recover the winning sequence. The work grows only in proportion to the number of slices.
4. **Per-slice results.** Read off, for each slice: its chosen key/mode; its ranked alternatives (the other surviving
   candidates); a **confidence** — how much better the winning sequence is than the best sequence that is forced to
   pick a *different* key/mode at that slice; and an **"uncertain" mark** when that confidence is low.
**Reaching back for more music:** if the opening of the selection has no settled key, Architectural Layer 3 asks
Architectural Layer 1 to widen the span **earlier in time** and re-decides, until the prevailing earlier key is in
view or a set limit is reached. **Re-deciding part of the sequence:** the same sweep can be run over a sub-range with
the key/mode at its two ends held fixed, so a score edit re-decides only its neighbourhood.

## 6. Runtime view (scenarios)
- **A stable passage:** the scores favour one key/mode and the cheap-to-stay rule keeps it → one key/mode throughout.
- **Relative major versus minor:** the per-slice scores are nearly tied, but the whole-run fit plus the large
  relative-pair change penalty pick one consistently; where the two readings are closest, the confidence is low and
  the slice is marked "uncertain."
- **A brief tonicization:** a few slices score the temporary key higher, but the change cost is not repaid over so
  few slices → the original key/mode is kept.
- **A real modulation:** the new key persists, so the accumulated better fit repays the change cost → the key/mode
  changes.
- **A selection that begins in the middle of a passage:** the opening has no settled key → Architectural Layer 3
  asks Architectural Layer 1 to widen the span earlier in time until the prevailing earlier key is visible.
- **A small score edit:** only the edited neighbourhood is re-decided, with the key/mode at its two ends held fixed.

## 7. Data design
Each slice's result holds: the chosen key/mode; the ranked alternative key/modes; the confidence number; and the
"uncertain" yes/no mark. Internally, the decision uses, per slice, the short candidate list (the best-scoring
candidates plus the current key/mode), and a running table over (slice × candidate) recording the best total ending
at each candidate together with a back-pointer to recover the winning sequence. Architectural Layer 3's settings —
how many candidates to keep, the change-cost amounts, the size of the per-slice scoring window, and the
confidence level below which a slice is marked "uncertain" — are tunable values.

## 8. Crosscutting concepts
- **Certainty is part of the output** — every slice carries ranked alternatives, a confidence, and an "uncertain"
  mark; ambiguity is recorded, never hidden, and it is what Architectural Layer 5 and Architectural Layer 4 use.
- **It annotates, it does not transform** — the slices and notes are unchanged; the chosen key/modes are added as an
  annotation; the alternatives are kept so the decision can be revisited later.
- **Speed and incremental editing** — the decision grows only with the number of slices; the Architectural Layer 1
  look-up index keeps the per-slice note reads fast; re-deciding only a sub-range keeps editing responsive.
- **Reaching back for context** — Architectural Layer 3 is the first architectural layer that asks an earlier
  architectural layer (Architectural Layer 1) for more music than the user selected; this is separate from the small
  fixed per-slice scoring window.
- **Ready for a future "effort" preset (quick / normal / ambitious).** The cost-driving choices — the candidate
  count kept per slice, the scoring- and reach-back-window sizes, and whether to run the optional keyscape
  refinement — are all **settings**, not hardcoded constants, and the keyscape refinement is a **separable on/off
  stage**. So a future effort preset can scale them without changing this layer's structure (it is added after the
  implementation can be profiled). Routing the per-slice scoring through Architectural Layer 1's indexed query is
  *not* an effort dimension — it is the correctness/performance floor; effort scales only the optional work above it.

## 9. Architecture decisions (with the alternatives we weighed)
- **Decide key/mode before chord symbol.** Alternatives considered: decide chord symbols first, or decide both
  together. Chosen: key/mode first — key/mode needs only the notes, while naming chords adds nothing the notes do
  not already carry for key-finding (this matches the key-finding literature and our own measurements). *(The
  corrections that shaped this are in Section 13.)*
- **Decide the whole sequence at once, not one region at a time.** Reason: deciding regions in isolation is the
  measured ceiling on relative-pair and modulation accuracy.
- **Commit where sure, mark "uncertain" where not — do not force an answer.** Reason: the ambiguous cases genuinely
  need chord evidence, which arrives at Architectural Layer 5; forcing an answer now would block that step.
- **Reuse the existing key/mode scorer** (which scores all 252 combinations of the 12 tonics and 21 modes).
  Alternative considered: a simpler standard key profile. Chosen: ours, because it covers all modes and so works in
  any musical style.
- **Change cost = cheap-to-stay + grows-with-key-distance + a large relative-pair penalty.** Alternative considered:
  a single flat "don't flip too easily" margin. Chosen: the standard key-finding shape (a flat margin cannot make a
  near modulation cheaper than a remote one, nor guard the relative pair specifically); the starting amounts are
  taken from the existing margin values and tuned later.
- **Confidence = how much better the winning sequence is than the best different-key sequence at that slice** (not
  the gap between the top two scores at the slice on its own). Reason: the decision is the whole sequence, so the
  meaningful confidence compares whole sequences; the near-tied cases are exactly the ones to mark "uncertain."
- **A dedicated best-sequence decoder for key/mode.** Alternative considered: reuse the existing chord decoder.
  Chosen: a dedicated one — the existing decoder is specific to chords and cannot be reused.

## 10. Quality & testing
- **Compared against human analyses (the main judge).** Architectural Layer 3 is the first architectural layer that
  can be compared against human ground truth, because published Roman-numeral analyses state a local key/mode for
  every position. We compare Architectural Layer 3's key/mode against those, on a **held-out set of pieces it was
  not tuned on**. The bar: full agreement on the cases where the human analyses are unambiguous; on the genuinely
  ambiguous cases, either Architectural Layer 3's answer is among the defensible readings or it marked the case
  "uncertain."
- **Behaviour tests** (independent of the scorer): a single-key passage stays one key; a relative-pair near-tie is
  resolved consistently; a brief excursion stays; a sustained excursion switches; a near modulation is preferred to
  a remote one when the note evidence is equal.
- **Scenario, consistency, and determinism tests:** the Section 6 scenarios including reach-back; re-deciding a
  sub-range gives the same result as that part of a full decision; the same input always gives the same output.
  Every branch of the code is exercised.
- **Safety net (a hard stop):** the project-wide accuracy metric must not get worse on either of the two tuning
  presets; the pinned analysis snapshots are refreshed only after a change is confirmed correct.
- **Two quality goals, measured separately.** (1) *Accuracy on the resolvable cases* — agreement with the human
  analyses where the notes decide; and (2) *calibration of uncertainty* — whether the "uncertain" mark and the
  confidence actually land on the genuinely ambiguous slices (a reliability curve over confidence; the precision and
  recall of the "uncertain" mark on the error set; and whether the true key is carried among the alternatives). The
  second goal is what backs the claim that Architectural Layer 3 is clearer about ambiguity than a single forced
  label, so it is graded in its own right, not folded into accuracy.
- **Regression tests (source).** `src/composing/tests/decode_keymode_tests.cpp` (synthetic emission / change-cost
  behaviour, the scenario fixtures, `redecodeRange` equals the matching slice of a full decode, determinism, and full
  branch coverage); plus the corpus diagnostics `batch_analyze --decode-keymode` graded by
  `tools/cc_layer3_keymode_baseline.py` (the held-out direct metric, with its `--characterize` calibration and
  `--decompose` causal-decomposition modes).

## 11. Risks & technical debt
- **The accuracy numbers, and even the way they are defined, are provisional.** Architectural Layer 3 is judged by
  whether the genuine errors drop compared with the **current per-region code**, measured on the held-out set — not
  by reaching a fixed target — because the numbers and the measurement will shift as the later architectural layers
  are rebuilt; the only fully meaningful comparison is against the finished pipeline.
- **A genuine error must be told apart from a limitation of the human ground truth.** Many apparent "misses" on
  modal music are cases where Architectural Layer 3's modal reading is defensible but the major/minor-only human
  analysis cannot represent it; those are not errors to optimise away.
- **Several values are left to be tuned:** how many candidates to keep, the change-cost amounts, the per-slice
  scoring-window size, and the "uncertain" confidence level.
- **The hardest cases are deliberately left marked "uncertain"** for Architectural Layer 5 — they are
  not solved in Architectural Layer 3.
- **The key/mode-recoverable headroom is small and bounded (measured, 2026-06-22).** A causal decomposition of the
  decoder's errors found that only about 7–12% of its misses (roughly 11.5% Baroque, 7.4% Jazz) are genuinely fixable
  within key/mode from the notes alone — a strongly-present distinguishing pitch the scorer under-weighted in a stable
  region, plus short modulations the change cost over-smoothed. Most apparent "scorer-recoverable" errors are in
  modulation regions, where a present pitch cannot be told from a tonicization tone; that distinction is a
  function-level call and belongs to a later architectural layer, not here.
- **The residual is handed on, with a concrete specification.** What Architectural Layer 3 cannot decide from the
  notes, and hands to Architectural Layer 5 (function), is: (i) **tonicization-versus-modulation
  arbitration** — the largest share, needing cadence/function to decide whether a sounded accidental opens a key area
  or merely tonicizes; (ii) **same-collection tonal-centre selection** — the relative major/minor and the modal
  rotations that share one pitch collection, needing a cadential cue to pick the tonic; and (iii) a small
  **chord-identity / spelling** need for the symmetric sonorities (diminished-seventh, augmented, whole-tone). This is
  the boundary, recorded here as the spec for that later layer.
- **The change-cost tuning is partly entangled with the later layer.** Whether a one-to-two-measure passage is an
  extended tonicization or a short modulation is itself a function-level judgment, so lowering the change cost to
  recover real modulations also un-suppresses tonicizations; the cost can only be set to a defensible trade-off point,
  not cleanly optimised, until Architectural Layer 5 (function) can arbitrate that boundary.
- **Uncertainty is currently under-claimed.** As built, the "uncertain" mark is high-precision but low-recall — when
  it fires it is usually justified, but it catches only a small share of the actual errors (most wrong slices are
  decided with high confidence). Raising the recall is a later tuning of the "uncertain" confidence level, weighed
  against keeping its precision. The correct key is, however, carried among the alternatives on roughly three-quarters
  of the misses, so the dominant remaining error is selection, not coverage.
- **★ Brittle leading-tone presence-gate — a non-Bach key regression (diagnosed 2026-06-25; verified at source).** The
  characteristic-pitch and true-leading-tone scorer terms are **hard-gated** on a `>0.1` window weight
  (`keymodeanalyzer.cpp:344,374`): a key's leading tone that is *present but weak* (below the gate) is treated as
  **absent**, so the key is denied its anchors *and* penalized. On the Mozart K279 opening the C-major leading tone
  (B♮) carries weight **0.093** — a hair under the gate — so C major is flipped to **F major** (whose leading tone E
  is C's ever-present third). The old 24-beat resolver cleared the gate; the wired 4-beat window does not, and the
  window-width relation is **non-monotonic**, so simply widening it is not a clean fix. This is a **general
  non-Bach-opening fragility**, structurally **invisible to the Bach-only BIR gate** (the notation tests are the guard
  that caught it). The **scale-membership lever does NOT fix it** (measured: 15× the scale penalty never flips F→C —
  the char/lt terms are *presence-gated*, not weight-scaled). **Fix = de-brittle the gate (weight-scale the char/lt
  terms); a Layer-3 emission increment scheduled for **Phase B (B2)** of the stabilization plan — leading-tone
  de-brittling is inference-quality, behind the inference firewall, *not* the Phase-4 tpc-capability foundation —
  not a foundation patch.** Full diagnosis: `cc_keyregression_diagnosis_report.md`.
- **One key/mode fix is deferred to wiring.** The fix for the stable-region under-weighting is a change to the shared
  per-window scorer; because that scorer is also used by the current per-region resolver, changing it now would move
  production output, so it is specified and deferred to the wiring increment — when the decoder replaces the resolver
  and the scorer can be tuned once for both.
- **The decoder-private settings are exhausted (sweep, 2026-06-22).** A bounded sweep of every decoder-private
  setting found none that moves the clean set net-positive: widening the per-slice window recovers stable regions but
  destroys modulation tracking; lowering the change cost is net-negative on Baroque (a Jazz-only gain that would need
  preset-conditioning the decoder settings — deferred); the candidate count is already saturated; the
  alternatives-kept count is output-only. So the bounded-headroom fix is **not** a decoder knob — it is the one shared
  lever below.
- **The identified shared-scorer lever, measured.** The stable-region under-weighting is carried by the scorer's
  *scale-membership* term, not its (inert) leading-tone term. Sharpening the out-of-candidate-scale penalty lifts
  *both* stable and modulation accuracy with no trade-off (measured decode-only, +57…+73 Baroque / +38…+68 Jazz);
  raising the leading-tone weight instead collapses accuracy. This is the change handed to the wiring increment, where
  it is applied once to the shared scorer and must clear the project BIR gate and the snapshots (its production-side
  magnitude is a wiring-time calibration; only its direction is validated so far).

## 12. Glossary
*(Only terms we coined or use in a specific way — standard musical terms are assumed known.)*
**Key/mode** — the tonal centre together with its mode (for example C-major, F-mixolydian). **Slice** — a span of
constant sounding-tonal notes (from Architectural Layer 2). **Local-fit score** — for one slice, a score for each
candidate key/mode saying how well it fits the notes in and around that slice. **Sequence** — the chosen key/mode
for each slice, read left-to-right in time, chosen as one whole. **Change cost** — the penalty for changing the
key/mode from one slice to the next; sized by **circle-of-fifths (key-signature) distance** between the two keys (plus
a large extra penalty for the relative-major/minor switch), and expressed in the **same units as the local-fit score**
so the two combine on one scale. **Best-sequence algorithm** — the standard one-pass method for finding the
single highest-scoring sequence given per-slice scores and change costs. **Confidence (sequence margin)** — how much
better the winning sequence is than the best sequence forced to pick a different key/mode at that slice. **"Uncertain"
mark** — set on a slice whose confidence is low (a near-tie). **Reach-back** — asking Architectural Layer 1 to widen
the analysed span earlier in time to gain context.

## 13. Background: what Architectural Layer 3 replaces, and corrections on record (NOT needed to understand the layer)
*Kept separate so Sections 1–12 describe only Architectural Layer 3 itself.*
- **What it replaces:** the current per-region key/mode resolver — it picks the single best key/mode for one coarse
  region at a time, with a small "don't flip too easily" margin and a fixed look-back/look-ahead window. Deciding
  one region at a time is the measured ceiling on relative-pair and modulation accuracy (the held-out baseline it
  must beat is roughly 87% on the Baroque test set and roughly 61% on the Jazz test set).
- **Correction — an early draft put chord symbols before key/mode.** That was wrong: it confused "key-finding
  benefits from harmonic evidence" with "key-finding needs the chord-symbol layer." Key/mode depends only on the
  notes.
- **Correction — a later draft put cadence detection inside this layer.** That was also wrong: a cadence is a
  function-level event (a V→I), so it belongs after key and chord; brief-versus-real modulation is handled here by
  the change cost, and cadence-confirmed key refinement is Architectural Layer 5.
- **On naming:** "Increment C" was a label for a unit of *delivery*, not an architectural layer; the build sequence
  is in the delivery plan, not in this architecture document.

## 14. Related work & external sources (what we borrowed, discarded, and why)
*The project's aim is to be the best key/mode inferrer it can be, so we survey the field, adopt the best ideas, and
say plainly which we rejected and why.*
- **Built on — the deciding method:** the standard **hidden-Markov / Viterbi key path with a high
  self-transition** (keep the current key unless the evidence to change is strong and sustained). *(This is the
  **per-layer** key-path decode — internal to Layer 3 — not the rejected **global cross-layer** joint Viterbi/beam
  decode; cf. ARCHITECTURE.md §2.14.)* Sources:
  HMM key-finding with key profiles (Nápoles López, *Key-Finding Based on a Hidden Markov Model and Key Profiles*,
  DLfM 2019; the `justkeydding` implementation); and *A regularization algorithm for local key detection*
  (Gedizlioğlu & Erol, 2024).
- **Built on — the per-slice evidence (local-fit score):** **key-profile correlation** — Krumhansl & Schmuckler,
  with later profile variants (Temperley; Aarden-Essen; Bellman-Budge). Our scorer is a richer, mode-complete
  descendant (all 12 tonics × 21 modes), so it works in any musical style, not only major/minor.
- **Built on — the dependency order (key before chord):** Temperley/Melisma (key from a pitch profile, separate from
  root-finding); Pardo & Birmingham (key-free chord identification); and the Contrapunctus benchmark's finding that,
  given the right key, the rest is largely solved — all support deciding key/mode first, from the notes.
- **Available refinements (optional, not core):** multi-timescale **keyscapes** (Sapp) as a principled
  passing-versus-structural test; Chew's **Spiral Array / Center-of-Effect** as an efficient real-time
  key-boundary alternative if needed.
- **Considered and discarded / deferred:** **joint or multitask neural models** that predict key and chord together
  (AugmentedNet — Nápoles López, ISMIR 2021; Chen & Su, ISMIR 2018; AnalysisGNN/ChordGNN) — the highest-accuracy
  approach, but it co-predicts key and chord in one opaque step; we **defer** it to Architectural Layer 5 (function)
  rather than use it in this decomposed layer. A **bare Krumhansl profile** — rejected in favour of our richer
  mode-complete scorer. **Chord-first ordering** and **cadence detection inside this layer** — rejected (Section 13).
- **Corpora / datasets used:** for the direct key/mode-versus-human-analysis metric, the **Roman-numeral analysis
  corpora** — When-in-Rome and the DCML corpora — read for their stated local key/mode at each position; a
  fixed **held-out split** so the metric is out-of-sample; and the project's **Bach** and **Jazz** tuning presets.

## 15. To do — deferred enhancements (this layer is built; these are revisions on record)
- **★ Use the notated spelling (tonal pitch class) as key evidence.** As built, Architectural Layer 3 works in **pitch
  class** — it is spelling-blind. The **maximal-information** principle (target architecture, 2026-06-22) says it must
  also use the notated tpc that Architectural Layer 1 carries: the spelling of an accidental (`G♯` vs `A♭`) is a
  **modulation-direction** clue (sharp-side vs flat-side) the pitch-class emission currently discards, so reading it
  should sharpen the key/mode inference (not the dim7 rotation churn — that is a chord-root/Architectural-Layer-4
  concern, resolved there by spelling). **Shape of the retrofit:** the per-slice emission reads tpc-aware evidence
  alongside pitch class; the decoder structure is unchanged; gated on the BIR + key-inference metrics and the
  byte-identity discipline, applied where the scorer is tuned (the wiring/scorer path). **Status:** deferred — the
  layer is wired and live (`a6b08af3fe`); recorded here so the now-governing principle and the as-built do not
  silently disagree. (Recorded per user, 2026-06-22.)
  **Cross-layer when built:** (i) **shared primitive** — Architectural Layer 4 also reads the notated tpc (for the
  chord root); the spelling-reading/interpretation must be **one shared derived view** used by both, not duplicated
  per layer (the unification rule). (ii) **downstream re-validation** — a sharper key prior shifts Architectural
  Layer 4's output (for the better), so re-run Architectural Layer 4's snapshots + metrics after this retrofit; the
  forward-only layering keeps that a bounded re-check, not a redesign. (iii) The chord layer needs **no change** to
  benefit — it improves automatically through the diatonic prior; this retrofit is decoupled from building Layer 4.
  **MEASURED (read-only, 2026-06-22, `cc_layer3_tpc_keymeasure_report.md`):** a decode-only line-of-fifths tpc term is
  **genuine spelling signal** (its modulation-gain/stable-loss frontier beats a change-cost control on both presets)
  and helps modulation regions cleanly (+2–8 pts), **but** as a *standalone Layer-3* term it is only **marginal
  overall** (best net +0.5 Baroque / +0.6 Jazz at a low weight) because it **hurts stable regions** — it over-switches
  on tonicizations. That stable cost is exactly the **tonicization-vs-modulation discriminator that function (Layer 5)
  supplies**, and the term is structurally **blind to same-signature ambiguity** (relative-pair / modal rotation). So
  the right home for this retrofit is **Architectural Layer 5 (function)**, where function gates the
  spelling signal — admitting the clean modulation gain without the stable cost — **not** a standalone Layer-3 emission
  patch. This is why L4-first is the disciplined order (no clean standalone L3 win is being skipped). (Upper-bound
  caveat: engraved corpus; MIDI spelling would see less.)
- **★ Dominant-implication key evidence in the emission (review amendment A-3, ratified 2026-07-02).** As built, the
  per-slice emission is **collection-fit only**: it scores how well a slice's pitch content matches each candidate
  key/mode's scale, and carries no evidence from the *shape* of the sounding sonority. But a sonority shaped like a
  dominant seventh or leading-tone seventh is strong **note-level** evidence for the key it implies (its tritone
  resolves into exactly one major and one minor tonic pair) — evidence readable from the notes alone, **before and
  without any chord decision**, so it belongs in this layer's emission without breaking the evidence split (Layer 5
  still owns *resolution-confirmed* evidence — the cadence votes). The gap is what the external review's Tristan
  simulation exposed (F-10: keys established by **dominant implication**, tonic arrivals denied → collection-fit is
  near-flat and the decoder rides on inertia → systematic under-modulation), and it also bears on the measured
  relative-pair floor (the implied tonic disambiguates the shared collection). **Shape:** a sonority-shape term in the
  per-slice emission (pitch-set → implied-tonic fit contribution); decoder structure unchanged; weight
  precision-phase. **Status:** deferred — design-first, measured before wiring like every increment (the tpc-term
  lesson above applies: measure the stable-region cost, not just the modulation gain). Source:
  `cowork_architecture_review_2026_07.md` §7/§9 (F-10, A-3).

# Comprehensive architecture review — the layered inference architecture (external Cowork review)

> **Status: REVIEW DELIVERED (Cowork, 2026-07-02); AMENDMENTS A-1…A-10 RATIFIED (user, 2026-07-02).** The user
> additionally ratified **corpus expansion** — gate-grade jazz GT and Wagner-class (and similar) DCML material; in
> general more non-Bach, non-Baroque ground truth (folded into A-7/A-8; recorded in `docs/implementation_roadmap.md`).
> Findings are folded into: `docs/implementation_roadmap.md` (the ratified-amendments block), `COWORK_HANDOFF.md`
> (review-delivered note), `STATUS.md` (session-21 entry), and the L3/L4/L5/consumer specs' open-item sections.
> The full external review prepared for in the 2026-07-01 REVIEW HANDOVER (`COWORK_HANDOFF.md` top block). Scope: the
> **architecture and its documentation** — principles adherence, separation of concerns, algorithm/method quality vs
> public research, precision-optimality, plus review perspectives from standard frameworks and a worst-case (Tristan)
> simulation. **Not** an implementation/code audit (deferred, gated on the two OWED refactors) and **not** inference
> tuning. Method and evidence basis in §1. Findings are numbered F-1…F-18 (severity-tagged), amendments A-1…A-10 (§9).
> External-source claims are marked **[verified]** (fetched/confirmed this session) or **[reported]** (search-snippet /
> prior-knowledge level — re-confirm before load-bearing use), per the verify-at-source rule.

---

## 1. Review scope, method, and frameworks

**Documents reviewed (read this session, host-side file tools):** `ARCHITECTURE.md` (§2 principles incl. §2.14/§2.15,
§3.3 layer map), `docs/implementation_roadmap.md` (current-state + forward plan), `STATUS.md` (sessions 10–20),
`COWORK_HANDOFF.md` (full), the seven layer/primitive specs (L1, L2, L3, L4, L5, L6, L1.5 phrase-boundary), the
Harmonic Vocabulary spec + recognition-consumer design, the idiom-discovery findings / style-taxonomy proposal /
entry mapping, and `cowork_polyphony_phrase_harmony_research.md`. Mechanism sections (§4/§5) of L3/L4/L5/L6 were read
in full; L1/L2 as-built specs at header + ARCHITECTURE §3.3 depth.

**Frameworks applied** (the "other useful perspectives" the review was asked for):
- **ATAM-style scenario analysis** (quality-attribute scenarios + sensitivity/tradeoff points) — the Tristan
  simulation in §7 is run as an ATAM stress scenario; the sensitivity points it exposes are F-9…F-14.
- **ISO/IEC 25010 quality attributes** — used as the checklist behind §8 (maintainability, reliability, performance
  efficiency, functional suitability).
- **arc42/template compliance** — the project's own `cowork_design_doc_template.md` is arc42-shaped; §8.4 checks the
  docs against it.
- The project's **own standing rules** (qualified predicates, total unification, verifiability, doc-sync) are treated
  as first-class review criteria — an architecture should pass its own laws first.

**Overall verdict up front.** The architecture is **sound, unusually well-documented, and internally honest**. The
forward-only six-layer spine with ranked-alternatives + honest abstention is a defensible, evidence-ratified shape;
the dormant-build/byte-identical discipline is exemplary and rare. The review found **no structural fault requiring a
redesign**. It found **two coherence gaps at the architecture level** (the cross-layer confidence contract, F-1; the
unbounded "engage deferred indefinitely", F-2), **one evaluation-layer gap** (F-8), and a cluster of **capability gaps
that the Tristan stress case makes concrete** (F-9…F-14) — all addressable as amendments within the existing shape.

---

## 2. Adherence to stated principles (§2.15 contracts + standing rules)

Checked contract by contract. Verdict format: **PASS / PASS-with-gap / GAP**.

| Principle / contract | Verdict | Evidence & notes |
|---|---|---|
| Finest-grain analysis; coarser = derived views | **PASS** | L2 slices are the atomic unit end-to-end; L6 groups; the batch-region legacy granularity survives only in the *gate metric* (see F-8). |
| Universality in fact layers; style only in calibration | **PASS** | L1/L2 verified style-free by construction; style enters via preset/idiom weights only. The Baroque-tuned Gates A–L violate this *in the legacy path only*, which is scheduled to dissolve (Stage 5, OWED). |
| Forward-only + confidence-weighted forward-override | **PASS-with-gap** | No back-edge found anywhere in the rebuilt spine (L4 §8, L5 §5.4/§8, L6 read-only — all re-verified in the specs). The gap is not the direction but the *arithmetic*: the override compares a contradiction strength against an earlier layer's confidence, and no cross-layer confidence semantics exists → **F-1**. |
| Span typology; "region" unqualified banned | **PASS** | L5 §5.0 and L6 §0/§3 are exemplary post-rename. Residual boundary-sense "phrase" usages are tracked and deliberate (L6 §15-7). |
| Verifiability contract | **PASS-with-gap** | Honored in structure (L6 keeps flat because the oracle is flat; hierarchy excluded for stated reasons). Gap: the *validated* ground truth is Bach-chorale-centric; idioms 3–5 (jazz/pop/coloristic) rest on research corpora that are not gate material, and no doc yet carries the "empirically-unvalidated" mark for the constants that only Baroque data has calibrated → **F-7**. |
| Bounded context (R1–R3) | **PASS (spec) / dormant (build)** | Designed coherently (L2 clip, L3 reach-back, L4 window, §5.4 bounded recompute). `redecodeRange`/incremental re-slice are dormant/deferred — tracked, acceptable. |
| Single responsibility, minimality + maximal info | **PASS** | See §3. |
| Qualified predicates in specs | **PASS-with-gap** | The layer specs are rigorously qualified (multiple language-mechanical passes on record). The one **unqualified load-bearing predicate found sits above the specs**: "engage **deferred indefinitely**" names no argument — deferred *until what*? → **F-2**. |
| Total unification (one path per concern; retirement named) | **PASS-with-gap** | Temporary coexistences are all tracked (legacy spine, dual tpc reader, legacy cadence detector). Gaps: (a) **three** cadence implementations now coexist (`sectioncadencedetection` legacy, `cadencekeyanchor` instrument, L5 `functioncadence`) with no single retirement map; (b) L5's §5.0 pairwise grammar and the Harmonic Vocabulary are **two progression-knowledge stores** whose relation ("vocabulary extends pairwise") is asserted but the single-store/two-store decision is not yet made at the consumer design → **F-5, F-6**. |
| Doc-sync / doc drift as defect | **PASS** | The 2026-06-29/07-01 governance passes brought ARCHITECTURE.md canonical + current; known-pending items are explicitly flagged. Minor: STATUS.md's one-paragraph-per-session format is at the edge of usability (F-17, cosmetic). |
| Knowledge-based coding / investigate-first | **PASS** | The record is outstanding: beam widening, whole-score cache, key-path HMM, tonicization crediting, joint decode — each *measured before building*, several correctly falsified. This is the architecture's strongest process asset. |

**F-1 (HIGH, coherence). No cross-layer confidence/calibration contract.** Every layer emits "a confidence", and the
architecture's signature mechanism (the §8 forward-override) *numerically compares* confidences across layers — yet:
L3's confidence is a sequence-margin (unbounded score difference re-expressed per slice), L4's is a composite
(margin + sufficiency + membership cleanliness), L5's `FunctionConfidence.combined` is an **unbounded additive** score
while §8's `earlierConfidence` is **[0,1]-clamped** (the L5-close D3 finding — currently disjoint, but they meet at
engage). There is no document defining, per layer: the confidence's definition, range, semantics (rank-margin vs
probability), and how a consumer may combine or compare it. Without this, every override bar and every "scaled to its
confidence" threshold is apples-vs-oranges arithmetic that Stage-5 fitting cannot repair (fitting weights over
incommensurable inputs just hides the incoherence in the constants). → **A-1**.

**F-2 (HIGH, governance). "Engage deferred indefinitely" is an unqualified predicate.** The mission posture (build +
validate dormant against frozen references) is sound, but "indefinitely" names no completion condition. Consequence:
the live product runs legacy L4/L5 (Baroque-tuned gates, the known ~7× per-beat error understatement) while a
measured-better spine sits dormant; the dual spine is maintained twice; and the total-unification rule's "temporary
coexistence" has no terminus. This is the project's own qualified-predicates rule applied to its top-level plan.
→ **A-2** (define the engage *criteria* — a measurable bar — even if the *date* stays open).

---

## 3. Separation of concerns

**Verdict: exemplary overall.** The three-kind taxonomy (representation / inference / assembly) is clean and honestly
policed (L6 "decides nothing new"; L2 "a fact, never a guess"). Specific judgments:

- **L4 owning chord + non-chord-tone as ONE decision** is correct and independently corroborated: AnalysisGNN's NCT
  module gates all downstream heads on chord-tones **[verified — arXiv 2509.06654]**, i.e. the field also treats
  membership as inseparable from labeling. The three-tier stepwise/metric membership rule is a faithful encoding of
  the classical NCT taxonomy with the right override order (structure over metric weight).
- **The L3/L5 evidence split for key** (notes-evidence vs function-evidence, residual carried as ranked alternatives)
  is the architecture's most elegant seam: it dissolves the old circularity without a back-edge. Its cost is that
  **two layers may move the local key** (L3 change-cost arbitration; L5 cadence-confirmed override). The split is
  principled, but it is exactly where F-1 bites: "L5 overrides L3 when cadence evidence crosses a bar scaled to L3's
  confidence" is only as sound as the two confidences' comparability.
- **The cadence detector's key-agnosticism** (it votes for the key; never reads one) is the right call and the
  documented key-agnostic limit (plain V→I ≡ transposed I→IV) is handled honestly (seventh strengthener, phrase gate,
  weak-vote absorption). Note the **phrase gate couples cadence admission to L1.5 surface punctuation** — sound for
  chorales, a sensitivity point for punctuation-poor textures (F-11, Tristan).
- **Residual naming debt** (not new, restated for the gap-analysis): the misnamed `harmonicfunctionlayer` (actually
  the chord-competition pipeline) renames at engage; the physical `chordanalyzer.cpp` split (Stage 3.5 OWED) is what
  will make L4's *legacy* seam physically auditable.

**F-3 (MEDIUM, SoC). L5 carries three distinguishable sub-responsibilities** — (i) derivation + relational labeling
(RN), (ii) cadence detection + key arbitration (§5.2–§5.4), (iii) abstention resolution/override (§5.5 + §8). The spec
itself keeps them in separate §5.x units with clean interfaces, and the build mirrored that (separate dormant units) —
so this is *not* a defect, but the admission-gate test (§2.15: separation of concerns is sufficient on its own) would
*permit* splitting (ii) into its own layer/component if L5 grows further. Recommendation: record as a watch-item, no
action now (proportionality gate correctly says don't split yet).

**F-4 (LOW). L1.5 is load-bearing but half-titled.** The phrase-boundary primitive gates cadence admission (L5) and
defines L6's spans; the spelling view feeds L4's symmetric pin. These are inference-adjacent *facts* correctly kept
out of the decision layers — but L1.5 has no §3.3-style consolidated statement of everything it owns (it is described
across three docs). A one-page L1.5 inventory would close it (fold into A-10 doc riders).

**F-5 (MEDIUM, unification). Three cadence implementations coexist** (legacy circular `detectCadences`; the committed
`cadencekeyanchor` diagnostic instrument; L5's `functioncadence`). Each has a reason; no single doc names which
retires when. → fold into A-2's engage criteria (retirement map).

**F-6 (MEDIUM, unification). Two progression-knowledge stores** (L5 §5.0 pairwise licensed-progression grammar; the
Harmonic Vocabulary's multi-chord catalog). The consumer design says the vocabulary "extends" the pairwise grammar —
but whether the pairwise motions ultimately *live in* the vocabulary (single store, L5 queries it) or stay a separate
primitive (two stores by design) is undecided. Decide it at the recognition-consumer build, explicitly. → **A-6**.

---

## 4. Algorithms and methods vs public research

Per layer, against the located literature (project's own research docs + this session's searches):

- **L1 (lossless tie-resolved note model) + L2 (change-point slicing).** Matches the field consensus: harmony in
  symbolic analysis is computed at the **onset/verticality level** (ChordGNN onset-wise predictions **[reported —
  arXiv 2307.03544]**; music21 `chordify`), and our L2 slices are exactly that grid, with a cleaner
  eligibility/losslessness story than most published pipelines. **Best practice; no change.**
- **L3 (key/mode as Viterbi over slice-level emissions with circle-of-fifths transition costs + relative-pair
  penalty).** This is the canonical key-HMM shape of the literature (Temperley-style profiles; HMM key tracking).
  Two distinguishing choices are defensible: the 252-candidate tonic×mode space (unusually rich — an asset for modal
  repertoire, a calibration burden elsewhere) and the forced-different-key **sequence-margin confidence** (better than
  a local top-2 gap; the deferred "confidence redesign" item should fold into A-1). **Gap vs the music, not vs the
  literature:** the emission model is *collection-fit only* — it carries no **dominant-implication** evidence (a
  sonority shaped like a dominant seventh / leading-tone seventh is strong note-level evidence *for the key it
  implies*, even before any chord decision). Standard key-finding practice includes such cues; ours defers all of it
  to L5's cadence votes, which require *resolutions* — see F-10/A-3.
- **L4 (template scoring + rule-based NCT membership + commit/inherit/abstain).** The template lineage is
  HarmAn/Pardo–Birmingham-class **[reported]**; the membership tiers encode the textbook NCT taxonomy; the
  abstain-with-named-open-question contract is genuinely novel-in-practice and better than anything published for
  *explainable* pipelines. The field's accuracy frontier here is learned emission (AnalysisGNN's NCT gating
  **[verified]**); the project's A-vs-B posture (hand-built until a measured ceiling; interfaces producer-agnostic so
  a learned emission can drop in) is the right hedge — **preserve B-swap readiness as a stated design property**
  (it currently holds: L5 units are hand-injectable; L4 decoder is scorer-independent).
- **L5 (rule grammar + event-pair feature-scored cadences + weighted tonic votes + hysteresis modulation).** The
  closest published relative is the preference-rule tradition (Temperley/Melisma) — respectable, explainable, and the
  weights are Stage-5-fittable. The current SOTA does cadence detection with GNNs (note-graph classification
  **[reported — arXiv 2208.14819]**) and full-RN with multi-task nets (AugmentedNet, RNBert, AnalysisGNN
  **[verified: these are the benchmarked SOTA line]**); published full-RN accuracy on mixed corpora sits meaningfully
  above the current hand-built pipeline's RN agreement (the project's own part-1 review put the gap at roughly
  45–50% vs high-20s/low-30s — figures from project docs, **re-verify before load-bearing use**). The architecture's
  answer (explainability + no-training-data + B-as-triggered-fallback) is ratified and evidence-based; the review's
  only demand is that the **triggers stay live** (the OQ-1 re-open gate: non-Bach decomposition + samples) and that
  Stage-5 fitting not slip indefinitely, since the meta-principle itself locates precision in emission + calibration.
- **L6 (flat grouping over DCML `{}`).** Matches the oracle and the Contrapunctus reminder (SOTA-competitive with no
  grouping layer). Correctly thin.
- **Architecture-level (forward-only vs joint/end-to-end).** The 2026-06-29 reconciliation (joint decode measured
  inert; forward + gated override) is consistent with the project's own Contrapunctus finding (joint key detector
  regressed chord-ID) and with the general observation that end-to-end nets buy their joint inference with data, not
  with search. Given the explainability constraint, the chosen shape is sound. The **evaluation methodology** is where
  the project is currently *behind its own architecture* — see F-8.

**F-7 (MEDIUM, verifiability).** Calibration and validation are Baroque/Bach-heavy; idioms 3–5 and the jazz preset
have no gate-grade ground truth. The contract's "empirically-unvalidated" mark exists in the spec but is not yet
*applied* to the affected constants/presets in the docs. → **A-7**.

**F-8 (MEDIUM-HIGH, evaluation).** The BIR gate remains at **batch-region granularity**, measured ~7× coarser than
user-visible per-beat error; the **granularity-robust union-of-boundaries metric is already built** (L0–L1 primitives,
committed) but is not the gate. For a precision-first mission the evaluation unit is itself architecture: the
finest-grain principle should apply to the *metric* as it does to the analysis. The two-tier class-(a)/(b) policy and
case-identity sets are excellent and should carry over unchanged. → **A-8**.

---

## 5. Is this the best architecture for the most precise, correct inference?

**Within its constraints (explainable, no training-data dependency, verifiable) — yes, with four provisos.** The
shape (fact layers → decision layers with ranked alternatives + honest abstention → assembly; style only in
calibration; forward-only with a gated override; a gated joint step for the genuinely-coupled minority) is the
correct precision architecture *for a hand-built system*: it puts modeling effort exactly where the project's own
measurements located the headroom (emission quality, functional labeling, calibration — not search).

The provisos, i.e. where precision is currently capped by something other than emission quality:

1. **Calibration is the unfunded mandate.** Nearly every §5 rule ends in "weights are precision-phase constants."
   That is correct sequencing (structure first), but it means today's precision is bounded by hand-set constants, and
   the machinery to fit them (Stage 5) plus the confidence semantics they need (F-1) do not exist yet. Precision-wise,
   **Stage 5 + A-1 are the critical path**, not more structure.
2. **The evaluation unit** (F-8) — you cannot optimize what you measure 7× too coarsely.
3. **Key-evidence breadth** (F-10 below) — the one *emission-level* gap the review found in the rebuilt spine.
4. **The residual joint step is named but unspecified** — the gated key↔chord joint decision (Stage 5) has no design
   doc; its trigger ("the flagged minority") is a qualified predicate only informally. Acceptable now; must be
   specified before Stage 5. (Fold into A-1's contract: the joint step consumes exactly the calibrated confidences.)

---

## 6. Process/quality perspectives (ISO 25010 + governance)

- **Reliability/regression safety: outstanding.** Byte-identity bridges, case-identity gates, two-tier policy,
  dormant-build discipline, stop conditions honored — materially better than industry norm.
- **Maintainability: good with two known debts** — the `chordanalyzer.cpp` monolith (Stage 3.5 OWED) and the dual
  spine (F-2). Naming debt tracked. Test coverage objective stated and partially discharged per layer (L1/L2 100%
  branch on new code; coverage-measurement pass still owed).
- **Performance efficiency: adequate and honest** — P3 envelope measured; R1–R3 scale requirements stated; the
  decoder is O(slices); the effort-preset is correctly a calibration knob. Watch: L2 slice counts on dense chromatic
  textures (Tristan-class) multiply L4 work — within O(n) but constants matter; the effort preset covers it.
- **Observability: excellent** — the read-only dump/diagnostic pattern (`--dump-l5` etc.) is a model.
- **Governance: excellent** — ratification records ≈ ADRs; instruction-file discipline; verified-facts culture.
  **F-17 (LOW):** STATUS.md's giant single-paragraph entries are increasingly hard to consume; consider a fixed
  header schema per entry (gate / HEAD / commits / next) above the prose. Cosmetic, optional.

---

## 7. The worst-case simulation — Tristan Prelude (mm. 1–17 and the texture at large)

Why Tristan: near-continuous chromatic flow, suppressed surface punctuation ("unendliche Melodie"), systematically
**denied resolutions** (the tonic A is withheld; dominants resolve deceptively or dissolve), long accented
appoggiaturas and suspension chains as the *normative* texture, enharmonic reinterpretation as a modulation device,
and a 150-year analytical controversy over its very first sonority (F–B–D♯–G♯: half-diminished? French-sixth variant
with G♯→A appoggiatura? a linear/energetic event per Kurth? — the literature never settled it). Ground truth in the
DCML format exists nearby: **DCML publishes `wagner_overtures` (v2.1) in the Distant Listening Corpus [verified —
github.com/DCMLab/distant_listening_corpus]**; whether the Tristan Prelude specifically is included must be checked at
the repo **[unverified]** — if yes, this stress case is *measurable* with existing tooling.

Layer-by-layer walk:

- **L1/L2 (facts): PASS.** Losslessness, tie handling, grace notes, and slicing are texture-independent. Effect:
  very fine slices, most containing one-note changes — a cost, not a correctness problem (effort preset).
- **L1.5 (phrase boundaries): DEGRADES.** The opening's rest-separated fragments actually score well; but from the
  sustained texture onward, fermatas/rests/double-bars are deliberately absent and the graded profile goes flat.
  Everything gated on phrase boundaries (cadence admission, half-cadence identity, L6 spans) starves. **F-11.**
- **L3 (key): DEGRADES, two ways.** (i) The chromatic saturation flattens collection-fit emissions → the decoder
  rides on transition costs → strong inertia; with near-flat evidence the *cheap-to-stay* rule can lock a wrong
  opening key for a long span. (ii) Tristan's keys are established by **dominant implication** (E7 means "we are in
  a minor" without any A arriving) — and collection-fit carries no dominant-shape term, while the cadence votes that
  would supply it (L5) require resolutions the music denies. Net: systematic under-modulation and low-confidence keys
  — the honest marks will fire (good), but the committed labels will lean wrong. **F-10.**
- **L4 (chord + membership): PARTIALLY DEGRADES, honestly.** The Tristan chord itself: the notes are a symmetric-ish
  share-tone sonority; the spelling-pin reads F–B–D♯–G♯; G♯ is approached by leap and left by step (one-sided) → the
  tie goes to metric weight, and Wagner's long accented appoggiaturas are *metrically asserted* → the membership rule
  will tend to read appoggiaturas as chord tones. That reproduces one legitimate side of the scholarly debate (fine),
  but it means the **calibration** of the one-sided tie-breaker is style-dependent (late-romantic style inverts the
  chorale-era convention). Structure survives; constants must move per idiom — exactly what the
  style-only-in-calibration contract anticipates. **F-12.** In suspension-chain stretches the "prevailing harmony"
  anchor (nearest metrically-strong *committed* chord) is itself often uncertain → inherit/abstain cascades → an
  output dense with open marks: *honest, but a product question* (what does the user see when 40% of slices are
  uncertain?). **F-13.**
- **L5 (function/cadence/modulation): THE BINDING CONSTRAINT.** The detector's typology actually covers Tristan's
  signature move (m.16–17, E7→F **deceptive** cadence — admitted by the spec's deceptive rule, given a boundary).
  But: cadence-*confirmed* modulation (§5.3's necessary gate) almost never fires in a texture that evades cadences →
  the default-tonicize rule keeps the home key across genuinely modulating spans → RNs computed against wrong keys.
  The §5.2 phrase gate (F-11) compounds it. Tristan's actual key-defining machinery — **dominant prolongation without
  arrival, sequences (transposition chains), enharmonic pivots** — has no confirmation channel in §5.3. **F-10/F-14.**
  Enharmonic reinterpretation (German-6th ↔ V7 pivots, key-spans respelled mid-flow) is handled at the single-chord
  level (spelling-aware §5.6; L4 pin defers on contradiction) but **no rule addresses enharmonic identity at the
  key-span level** (is the span in G♭ or F♯; when does a span's spelling frame flip?). **F-14.**
- **L6 (grouping): degrades gracefully** — few spans, sparse alignments; correct behavior given its inputs.
- **The missing axis is the real answer.** Tristan's harmony is voice-leading-driven; the two recorded future items —
  the **non-chord-tone filter as an L4 lever** and the **voice-leading axis** — are precisely what this repertoire
  needs. The simulation upgrades their priority from "recorded" to "the known path to the hard half of the
  romantic repertoire." **F-9.**

**Is Tristan the worst case?** It is the worst case **for the inference layers within the tonal model class** — it
maximally stresses exactly the three mechanisms the architecture leans on (cadence votes, cadence-gated modulation,
punctuation-gated grouping) while staying inside key+RN annotatability (DCML annotates Wagner). It is *not* the
absolute worst case: (i) **late Scriabin / early atonality** breaks the model class itself — the correct output is a
confident "outside tonal vocabulary" verdict, and the architecture currently has no explicit out-of-domain stance
(confidence collapse would happen, but nothing *interprets* it) — **F-15**; (ii) **implied harmony in unaccompanied
monophony** (Bach cello suites) stresses L4's window/membership differently (the field also finds this hard); (iii)
**quartal/modal-static jazz** hits vocabulary gaps (quartal templates deferred, F4). Tristan remains the right
*named* stress scenario because it is measurable, in-scope, and touches the most mechanisms at once.

---

## 8. Findings register (consolidated)

| # | Severity | Finding | Home |
|---|---|---|---|
| F-1 | HIGH | No cross-layer confidence/calibration contract; incompatible scales already observed (L5 D3) | §2 |
| F-2 | HIGH | "Engage deferred indefinitely" unqualified; dual-spine has no terminus; no retirement map | §2 |
| F-3 | LOW | L5 internally three-responsibility; watch-item only | §3 |
| F-4 | LOW | L1.5 lacks a consolidated ownership statement | §3 |
| F-5 | MEDIUM | Three coexisting cadence implementations, no retirement map | §3 |
| F-6 | MEDIUM | Two progression-knowledge stores; single-store decision unmade | §3 |
| F-7 | MEDIUM | Baroque-centric calibration/validation; "empirically-unvalidated" mark not applied to presets/idioms 3–5 | §4 |
| F-8 | MED-HIGH | Gate still batch-granularity; built granularity-robust metric not yet the gate | §4 |
| F-9 | HIGH (capability) | Voice-leading axis + NCT-filter lever are the known path to romantic-repertoire precision; currently future-items | §7 |
| F-10 | HIGH (capability) | No dominant-implication key evidence (L3 emission) and no cadence-less key-confirmation channel (L5 §5.3) → systematic under-modulation on resolution-denying music | §7 |
| F-11 | MEDIUM | Phrase gate starves in punctuation-poor textures; no specified fallback when the graded profile is flat | §7 |
| F-12 | LOW (calibration) | One-sided membership tie-breaker is style-sensitive (appoggiatura-normative styles) | §7 |
| F-13 | MEDIUM (product) | No stated display/UX policy for dense-abstention output | §7 |
| F-14 | MEDIUM | No enharmonic-identity policy at key-span level | §7 |
| F-15 | LOW-MED | No explicit out-of-tonal-domain stance | §7 |
| F-16 | MEDIUM | Gated joint step (Stage 5) named but unspecified | §5 |
| F-17 | LOW | STATUS.md entry format usability | §6 |
| F-18 | LOW | Preserve B-swap readiness as a stated design property (currently true, nowhere pinned) | §4 |

---

## 9. Proposed amendments (ranked; each ratification-gated; none is code)

- **A-1 (from F-1, F-16). Write the cross-layer confidence & calibration contract** — one doc: per layer the
  confidence's definition, range, semantics, and consumption rules; the §8 override arithmetic stated once over those
  definitions; the Stage-5 joint-step trigger expressed in the same terms; calibration measured at Stage 5. *Highest
  leverage per page in the whole review.*
- **A-2 (from F-2, F-5). Define engage criteria + the retirement map.** A measurable bar (e.g. dormant spine ≥ legacy
  on the granularity-robust metric, zero class-(b), coverage sealed, docs synced), plus the explicit list of what
  retires at engage (legacy chord path, legacy cadence detectors, dual tpc reader, `harmonicfunctionlayer` rename).
  "Indefinitely" becomes "until CRITERIA, date open."
- **A-3 (from F-10). Add dominant-implication evidence to the L3 emission** (a note-level sonority-shape term:
  dominant-seventh / leading-tone-seventh shapes contribute fit to their implied tonic) — keeps L3 key-agnostic of
  chords-as-decisions, measured before wiring like every increment.
- **A-4 (from F-10, F-14). Specify cadence-less key-confirmation channels in §5.3** — sustained dominant emphasis
  (arrival-denied dominants), recognized transposition sequences (the recognition consumer as a §5.3 input — synergy
  with the already-planned consumer), and an enharmonic-identity rule for key-spans. Design-only now; Tristan-class
  corpus as the measurement bed.
- **A-5 (from F-11). Specify the phrase-gate fallback** for flat boundary profiles (relax admission with vote-weight
  scaling instead of starving; the graded profile already carries the needed signal).
- **A-6 (from F-6). Decide the progression-knowledge store question** at the recognition-consumer build (fold §5.0
  pairwise motions into the Vocabulary, or two stores by declared design).
- **A-7 (from F-7). Apply the "empirically-unvalidated" mark** to the Jazz preset constants and idioms 3–5 in the
  affected docs; name the validation path (JHT/McGill-class corpora already inventoried by the idiom study).
- **A-8 (from F-8). Move the gate to the granularity-robust unit** (union-of-boundaries, duration-weighted), keeping
  case-identity + two-tier policy; and adopt a small **chromatic stress sub-corpus** (`wagner_overtures`; verify
  Tristan-Prelude presence) as research-tier material.
- **A-9 (from F-13, F-15). Write the product stance for dense abstention and out-of-domain input** (what the user
  sees; when the system says "this is outside my tonal vocabulary"). Product-level, small, prevents the honest-marks
  design from becoming a UX failure.
- **A-10 (from F-4, F-12, F-17, F-18). Doc riders**: L1.5 consolidated ownership page; record the membership
  tie-breaker as an idiom-calibrated constant; pin B-swap readiness as a design property; (optional) STATUS entry
  header schema.

**Priority read:** A-1 and A-2 are architecture-coherence and should precede the CC gap-analysis (they change what
"spec" means for the comparison). A-3/A-4/A-5 are the Tristan-derived capability track — design-first, measure-first,
after the current forward sequence's L6/consumer steps or interleaved by user priority. A-6…A-10 ride with existing
planned work.

**Input to the CC gap-analysis (next step per the user):** the gap-analysis should compare implementation ↔ spec for
L1–L5 + L1.5 + Vocabulary as specced today, and *additionally* verify the five spec-level claims this review leaned
on at source: (1) no production back-edge anywhere in the rebuilt spine; (2) the L4→L5 carried-readings contract
fields all populated; (3) the §8 override's confidence inputs (which scale each site actually uses — F-1 evidence);
(4) the three cadence implementations' call graphs (F-5); (5) B-swap readiness (producer-agnostic seams) in the
as-built interfaces (F-18).

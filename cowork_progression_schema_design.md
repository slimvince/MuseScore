# Progression-schema recognition (design) — the Layer-5/6 consumer of the Harmonic Vocabulary

> **Status: design, v1 draft (2026-06-29).** A **deferred, scaffolding-first** extension: build the structural mechanism
> now (dormant, additive, byte-identical), and leave the fuzzy-matching judgment to the precision phase (the firewall).
> This design is a **consumer** of the **Harmonic Vocabulary** component (`cowork_progression_schema_dictionary.md`); it
> does not own that catalog. Placement and research: `cowork_layer6_grouping_research.md`, `contrapunctus_findings.md`,
> target-architecture §2 (the span typology, the verifiability contract, the future voice-leading layer).

## 1. The core principle
Progression-schema knowledge is **multi-chord functional knowledge**: it extends Layer 5's **pairwise** licensed-
progression grammar (descending-fifth / descending-third / ascending-second / applied resolution / cadence) to the
**recurring multi-chord patterns and substitutions** that musical styles use — the content of the Harmonic Vocabulary. The
same knowledge is read two ways here: read **forward** over the committed chord stream it is an **inference prior** (it
disambiguates an uncertain chord); read as a **recognised unit** it is an **annotation** (it labels "this is a ii–V–I, a
Prinner, a tritone sub"). It detects nothing the lower layers did not commit — it **recognises patterns in their output**,
and where its evidence is decisive it **overrides** a contradicted local reading through the existing §8 mechanism.

## 2. Placement — no new layer
Published systems treat a progression model as a **harmonic language model that re-ranks local chord recognition** (a
higher-order language model improves chord recognition; skip-grams capture cadential progressions), not as a separate
parsing stage. That maps onto our decomposition directly:
- **The prior → Layer 5 (function).** The Vocabulary's patterns are the multi-chord extension of the §5.0 licensed
  progression. They feed the **§5.5 resolver** (prefer the reading that completes a recognised schema) and fire the **§8
  forward-override** when a *confident* slice contradicts a strongly-recognised schema. Layer 5 **is** the re-ranker; no
  separate stage is added.
- **The annotation → Layer 6 (grouping).** A recognised schema is a **sequence span** (the span typology) — a span type
  that **cross-cuts** phrases (a schema may straddle a phrase boundary; a phrase may hold several schemas). It is **not** a
  phrase. Layer 6 carries it as a read-only, additive grouping label.
- **The catalog → the Harmonic Vocabulary**, queried, not owned (§3).

**Scope: the harmonic skeleton.** Voice-leading is a different dimension (held by the future voice-leading layer); a schema
conventionally defined by voice-leading is recognised here only by its **harmonic pattern**, and the complete schema is
recognised by combining this harmonic recognition with the voice-leading dimension when that exists.

## 3. Inputs and outputs (the contract)
**Consumes** (all already produced):
- the **Layer-5 committed progression** — the ordered chord identities + base Roman numerals + the per-region local key
  (from `functionoutput`);
- the **Harmonic Vocabulary** — queried for matches over the committed progression (the active **style** subset selected
  by the preset);
- the **preset** — the active style subset and the per-style match weights.

**Produces — additive over Layer 5, the literal Roman numeral unchanged:**
- a **schema annotation** per recognised span: the matched pattern's name, its style, the span it covers, the match score,
  and — where a member is a substitution — the **underlying function** it realises (e.g. "`bII7` here is a `subV7/I`, a
  tritone-subbed dominant");
- a **disambiguation contribution** to the §5.5 resolver / §8 override for the slices a recognised schema covers (a
  *prior* — it **selects or overrides among the carried readings**, and never re-scores from the notes);
- nothing where nothing is recognised (the honest residual is unchanged).

## 4. The rules
### 4.1 Recognition
Query the Harmonic Vocabulary's **recognise** form (§4 of its spec) over the committed chord/function stream; it returns
the patterns the stream realises, ranked by match score. The **conservative recogniser (this build)** keeps only the
**clear, near-exact** matches (a high score threshold); the **fuzzy / partial / metric-sensitive** matching is a
precision-phase threshold change at this consumer, deferred (the firewall). Where matches overlap, the longer and more
specific is preferred, but **all** plausible matches are carried (a schema is evidence, not an exclusive claim).

### 4.2 Substitution inversion
Where the Vocabulary marks a surface chord as the **substituted form** of an underlying function (its substitution
mapping), record the underlying function: a `bII7→I` is read as a `subV7/I` (dominant function); a recognised schema
**tolerates** a substituted member (a ii–V–I with a tritone-subbed V is still a ii–V–I). The **literal** Roman numeral is
unchanged; the substitution is recorded only as the **annotation** ("`bII7` = `subV7/I`").

### 4.3 The prior (disambiguation, through the existing mechanisms)
Where a Layer-5 slice is **uncertain** (a carried-reading abstention, §5.5), prefer the reading that **completes a
recognised schema**; where a slice is **confidently** committed but contradicts a **strongly**-recognised schema, fire the
**§8 forward-override** at its confidence-scaled threshold (the schema is the "later evidence"). Both reuse the existing
resolver and override — this adds a **prior**, not a new feedback path.

### 4.4 The annotation
Emit each recognised schema as a **sequence-span** label for Layer 6 (name, style, span, match score, and the
underlying-function read-out for any substituted member). Read-only, additive, cross-cutting phrases.

## 5. Where the style behavior lives
The Harmonic Vocabulary carries the **style label** on each pattern; the style **behavior** is this consumer's:
- the **preset selects** the active style subset;
- the **per-style match weights** are **precision-phase** constants applied as a **graded prior** — not a hard filter,
  since styles blend, so a Baroque cadence stays recognisable inside a jazz analysis;
- **style detection** from the score is a future classifier (the preset supplies the style until it exists).

The matcher framework is **style-general**; only the catalog content and the weights are style-specific. The style
vocabulary is the **shared canonical taxonomy** (the Vocabulary's §6 and §12 — common-practice / jazz / vernacular
families, hierarchical), the same set the presets select on.

## 6. Architecture decisions (with the alternatives weighed)
- **D1 — A prior plus an annotation, not a new layer.** Progression knowledge is functional knowledge → Layer 5 (the
  re-ranker our §8/§5.5 already provide) + a Layer-6 sequence-span annotation. *Rejected:* a standalone progression-parsing
  stage — it would duplicate Layer 5's function role and the §8 mechanism.
- **D2 — Harmonic-skeleton scope; voice-leading is a separate dimension.** Layer 5 recognises the harmonic pattern; the
  voice-leading half is the future voice-leading layer, combined when present. *Rejected:* full voice-leading-schema
  recognition in Layer 5 — that is a different dimension with its own home.
- **D3 — Scaffolding now; the fuzzy matcher and the weights are precision-phase.** Build the recogniser and the additive
  annotation dormant, at a conservative threshold; the substitution-tolerant matching and the style weights are tuned
  later. *Rejected:* tuning the fuzzy matcher now — that is accuracy work, firewalled.
- **D4 — Additive; the literal Roman numeral is never changed.** The schema/substitution is an annotation and a
  disambiguation prior; it annotates, it does not relabel. *Rejected:* rewriting the Roman numeral to the underlying
  function — it loses the literal label the ground truth scores.

## 7. Quality & validation
- **What this consumer can measure depends on the available ground truth.** It can measure its use of the common-practice
  and galant patterns against the chorale ground truth (schema precision/recall where the corpus annotates cadences/
  schemata); it **cannot yet** measure its use of the jazz/pop patterns — there is **no jazz/pop ground truth**. That is a
  limit on *this consumer's measurement*, not on the patterns (which are sound theory by provenance). A jazz/pop ground
  truth is a named want.
- **The disambiguation contribution** is the change in Roman-numeral accuracy on the slices a recognised schema covers —
  its only accuracy claim, expected to be small on full-voiced corpora and larger on sparse/idiomatic material (per the
  research). The annotation's value is **explainability** — coverage and correctness of the named schemas — not Roman-
  numeral accuracy.
- **Dormant + byte-identical** until engagement (deferred): no production consumer; the corpus gate stays 53/24/53 by
  construction.

## 8. Risks & technical debt
- **Fuzzy matching is the hard part** — patterns are prototypes with substitutions and variants; the threshold/weights
  that handle them are precision-phase, deferred.
- **Substitution ambiguity** — when is a `bII7` a tritone-sub dominant, a Neapolitan seventh, or a chromatic chord? The
  resolution/function context decides; that is inference, not lookup (the same class as the `V/iv` over-trigger).
- **No jazz/pop ground truth** — the load-bearing styles are the ones this consumer cannot yet measure its use of;
  mitigated by the patterns' provenance, with the named want.
- **Catalog completeness is asymptotic** — the recogniser must degrade gracefully on the unrecognised.

## 9. Open items
1. **The conservative recogniser + the additive annotation** — the dormant scaffolding build (this design's first step).
2. **The fuzzy / substitution-tolerant matcher and the per-style weights** — the precision-phase build (deferred).
3. **A jazz/pop ground truth** — the named want that would let this consumer measure its use of the jazz/pop patterns.
4. **The future voice-leading layer** — the prerequisite for combining voice-leading into complete-schema recognition.
5. **The suggestion consumer** — a future, separate tool that reads the same Vocabulary predictively (out of scope here).

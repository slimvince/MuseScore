# Progression recognition (design) — the Layer-5/6 consumer of the Harmonic Vocabulary

> **Status: v4 — FOR RATIFICATION (Cowork, 2026-07-02).** v2 folded the owed items (D5 one-store; §4.6 sequences as
> key evidence; §4.5 idiom weighting; D6/D7); v3 was the plain-vocabulary + qualified-predicate rewrite; **v4 adds
> the §0 TERMS block (every term used is defined there or cited to the document that defines it — the L6 §0
> discipline) and removes remaining shorthand ("iff", "carried", "slot", schema names used without definition).**
> This is a specification: a word that is not defined or cited WILL be misunderstood. Scaffolding-first: build
> dormant/additive/byte-identical; every numeric constant is precision-phase (the firewall). Component spec it
> consumes: `cowork_progression_schema_dictionary.md`. Ratification asks: D5, D6, the §4.5 weighting shape, the
> §4.6 channel + its frame obligation.
> **How to answer each ask (user question, 2026-07-02):** **D5 and D6** are decisions — approve Cowork's proposal
> or pick a stated alternative (each now lists its alternatives with pros/cons). **§4.5 and §4.6** are
> approve/reject — there is no alternative to choose; "approved" ratifies the written rule.
> **§4.5: APPROVED (user, 2026-07-02 — "What is written is good").**
> **★ FULLY RATIFIED (user, 2026-07-02): D5 ratified (with the explicit-dependency-map rider); D6 resolved =
> `progression-schema-span`; §4.5 approved; §4.6 settled (always-emit corroboration + substitute channel).**
> The build instruction follows just-in-time.

## 0. Terms (each defined here, or cited to the document that defines it — nothing below is used before this table)

- **Named progression** — a chord progression with a conventional name and a catalog entry in the Harmonic
  Vocabulary (`cowork_progression_schema_dictionary.md` §5): cadence formulas, ii–V–I, turnarounds, the galant
  schemata, bass-line patterns, substitution operations. **Member** — one chord position in such an entry's
  sequence; each member specifies the scale degree and quality (and, for a bass-line entry, the bass degree) that a
  chord must realise to fill it.
- **Prinner** — one of the galant schemata in that catalog (dictionary §5.2, from Gjerdingen's schema inventory): a
  stock four-stage answer phrase, melody descending 6̂–5̂–4̂–3̂ over a bass descending 4̂–3̂–2̂–1̂. Used in this document
  only as an example of an entry **defined by its melodic/bass lines** (see D7).
- **Substitution** — a chord standing in for another chord of the same function, per the catalog's substitution
  mappings (dictionary §5.3); the standard case here is the **tritone substitution** (`♭II7` standing in for `V7`).
- **The committed progression** — Layer 5's §7 output for a region: the ordered chords the layers COMMITTED (each
  with root, quality, bass, extensions), their base Roman numerals, and the local key
  (`cowork_layer5_function_design.md` §7).
- **Resolved and unresolved chords.** For each chord position, Layer 4 either **committed** one reading (its
  `Commit`/`Inherit` decision) or **abstained** — publishing instead its **ranked candidate readings** (the
  possible chords, ranked, with the open question named) for Layer 5's §5.5 selection
  (`cowork_layer4_chordsymbol_design.md` §7). This document says **"ranked candidate readings"** for those
  published alternatives, and **"committed reading"** for a `Commit`. (Elsewhere the project calls the former "the
  carried readings" — same thing.)
- **Composite confidence** — Layer 4's published [0,1] confidence on a decision, per the cross-layer confidence
  contract (`cowork_confidence_contract.md` §3, row L4).
- **The §8 override and frame F-B** — Layer 5's mechanism for correcting a committed reading on later evidence:
  the override fires **if and only if** the contradiction quantity exceeds the threshold, where the threshold
  scales with the committed reading's composite confidence; a tie holds the incumbent; a decision is overridden at
  most once per pass (`cowork_layer5_function_design.md` §8; the quantities compared are declared as frame **F-B**
  in the confidence contract §4).
- **Functional-plausibility score** — the fixed feature score Layer 5 §5.5 uses to select among ranked candidate
  readings (`cowork_layer5_function_design.md` §5.5, the "close" rule).
- **Match score** — the Vocabulary's recognition score for "this stretch of the committed progression realises this
  entry"; in the Vocabulary's v1 matcher it is 1.0 for an exact realisation and entries are otherwise not returned
  (dictionary §4).
- **Idiom / IdiomSet / Mode / Chromaticism / voiceLeadingDefined** — the ratified five-idiom tags and
  cross-attributes on every catalog entry (`cowork_style_taxonomy_proposal.md`, executed `0e155154fc`).
- **Prior strength** — this consumer's weight for one recognised entry, defined in §4.5. **Admission** — prior
  strength above the declared admission threshold (§4.5). **Seed** — the user's preset expressed as idiom weights,
  the starting value of the mixture before the score's own evidence moves it (§4.5 phase 2); all-equal when no
  preset is given.
- **Punctuation-span** — Layer 6's flat grouping span (`cowork_layer6_grouping_design.md` §0). **Progression-schema-span** —
  the span a recognised named progression (a progression schema, i.e. one catalog entry realised) covers, emitted
  for Layer 6 (D6; "schema-span" elsewhere in this document is shorthand for this full name).
- **Harmonic sequence** — the same progression repeated at successive transpositions (Monte, Fonte, a
  descending-fifths sequence).
- **Key** — in this document ALWAYS the tonality (a tonic plus a mode, as in "the local key"); NEVER the everyday
  sense "important/crucial". (**Multiple-meaning words rule:** every word with more than one plausible reading is
  used in exactly ONE sense in this document, declared in this table. The other such words here: **sequence** —
  always the harmonic sequence above, never "an ordered series" (for that, this document says "ordered chords" or
  "the committed progression"); **member** — always a chord position in a catalog entry (§0 row above), never a
  person or element generally; **substitution** — always the chord-for-chord sense above, never text replacement.)

## 1. The core principle
This component recognises **named progressions — including substitutions within them** — in the committed
progression. Layer 5's own §5.0 test covers only adjacent chord pairs (descending-fifth root motion, and so on);
named progressions span several chords, and that knowledge lives in the Harmonic Vocabulary. A recognised
progression is used two ways: as **evidence** where Layer 4 abstained (prefer the ranked candidate reading that
fills the recognised entry's member position — §4.3), and as a **name** in the output ("this is a ii–V–I; its ♭II7
is a tritone-substituted V7" — §4.4). The component reads no notes and detects nothing new — it recognises
progressions in what the layers already decided — and where §4.3's override condition is met it corrects a
committed reading through the §8 mechanism.

## 2. Placement — no new layer
Published systems do not parse progressions as a separate stage: they use progression knowledge as **context that
re-ranks the per-chord decision** — a model of which chords follow which, conditioned on more than just the
immediately preceding chord, and matched even when other chords intervene (a cadential formula is still recognised
with a passing chord inside it). That maps onto our decomposition directly:
- **The evidence → Layer 5.** One feature of the §5.5 functional-plausibility score, plus the §4.3 override path
  through §8/F-B. Layer 5 is the re-ranker; no stage is added.
- **The name → Layer 6.** A schema-span, cross-cutting punctuation-spans (a progression may straddle a punctuation
  boundary; one punctuation-span may hold several progressions). Read-only, additive.
- **The catalog → the Harmonic Vocabulary**, queried, not owned (D5).

**Scope: chords only.** An entry defined by its melodic or bass lines (the Prinner) is recognised here only by its
chord skeleton and marked as such (D7); the voice-leading half is the future voice-leading layer's.

## 3. Inputs and outputs (the contract)
**Consumes:** the committed progression; the Harmonic Vocabulary (queried, filtered per §4.5); the idiom-mixture
weight vector (§4.5).
**Produces — additive over Layer 5; the literal Roman numeral is never changed:**
- one **schema-span** per recognised progression (§4.4);
- the **evidence contribution** to §5.5 / §8 for the chord positions a recognised progression covers (§4.3);
- the **harmonic-sequence output** for Layer 5's key arbitration (§4.6);
- nothing where nothing is recognised.

## 4. The rules

### 4.1 Recognition
Query the Vocabulary's recognise form over the committed progression. **This build admits only exact realisations**
(match score 1.0 — the Vocabulary's v1 matcher; substitution-aware per dictionary §4.2); partial and variant
matching is a precision-phase extension at this consumer, deferred. Where recognised progressions overlap: prefer
the longer span, then the more specific entry (the Vocabulary's ranking order); carry **all** recognitions that pass
admission (§4.5) — a recognition is evidence, not an exclusive claim.

### 4.2 Substitutions
Where the Vocabulary marks a member as filled by a substitution, record what the chord stands in for: `♭II7`
resolving to `I` = a tritone-substituted dominant (`subV7/I`); a ii–V–I with a tritone-subbed V is still a ii–V–I.
The literal Roman numeral is unchanged; the substitution is recorded only in the annotation ("`♭II7` = `subV7/I`").

### 4.3 The evidence contribution (both conditions fully stated)
- **Where Layer 4 abstained:** "this ranked candidate reading fills the member position of an admitted recognised
  progression" enters as **one additional feature of the §5.5 functional-plausibility score**, weighted by that
  recognition's prior strength. The §5.5 selection rule is otherwise unchanged.
- **Where Layer 4 committed:** if an admitted recognised progression's member position demands a **different root
  or quality** than the committed reading, the recognition's prior strength enters the **same contradiction
  quantity frame F-B already compares** (the functional-plausibility difference), and the committed reading is
  overridden **if and only if** that quantity exceeds the §8 threshold scaled to the committed reading's composite
  confidence — the same threshold rule, the same tie-holds-the-incumbent rule, and the same
  overridden-at-most-once-per-pass rule as every other F-B firing (§0). The correction **selects** an existing
  reading (a ranked candidate, or the recognised member's realisation where it is one) — never a reading built from
  the notes. No new comparison frame is introduced.

### 4.4 The annotation
Emit each recognised progression as a **schema-span** for Layer 6: entry name, idiom set, span, match score, and —
for any substituted member — what the chord stands in for. Read-only, additive, cross-cutting punctuation-spans.

### 4.5 The idiom-mixture weighting (structure and directions fixed here; every value Stage-5)
The consumer holds a weight vector `w` with one weight per idiom. **`w` is DISCOVERED from the score, seeded by the
user's preference (user-ratified model, 2026-07-02), in three phases — forward-only, no loop:**
1. **Recognise (weight-free).** Run §4.1 recognition over the committed progression. In v1 this step does not
   depend on `w` at all (matches are exact; `w` weights only the *use* of a recognition, not its finding) — which is
   what makes phase 2 loop-free.
2. **Estimate the mixture.** Build the score's **idiom-evidence histogram**: each phase-1 recognition contributes
   its match score to every idiom in its entry's IdiomSet. Then `w = blend(seed, histogram)` where the **seed** is
   the user's preset expressed as idiom weights (or all-equal when no preset is given), and the blend moves from the
   seed toward the histogram as recognised evidence accumulates — with **no** recognised evidence, `w` = the seed;
   with abundant evidence, the histogram dominates (direction fixed here; the blend rate is one Stage-5 constant).
3. **Weight and emit.** Apply `w` to admission and prior strength (below), then emit the §4.3/§4.4/§4.6 outputs.
Phase 2's input is phase-1 output only — never phase-3's — so estimation feeds forward and nothing cycles. *(When
partial matching arrives at Stage 5, phase 1 gains a `w`-dependence; the declared resolution is to keep estimating
from the exact-match subset only, preserving the loop-freedom — revisit then, recorded in §9.)* The **deferred
auto-detection feature** (roadmap forward-sequence step 5) is then just the *exposure* of this phase-2 estimate as
the score's idiom classification (for presets and display); the estimation mechanism itself is specified here.
- **Prior strength of a recognition** = `match score × max(w[i] over the entry's IdiomSet)`. The **max**, not the
  sum: an entry tagged with several idioms is not thereby advantaged.
- **Admission**: prior strength above one declared admission threshold.
- **Mode cue**: if the entry's `Mode` tag contradicts the local key's mode at the recognised span, multiply the
  prior strength by one declared factor less than 1 (never zero — modes mix). **`Chromaticism`**: no v1 behavior
  (recorded, unused).
- **`voiceLeadingDefined` entries**: recognisable by their chord skeleton alone; the schema-span carries the
  **"chords-only"** mark (D7) and the prior strength is multiplied by one declared factor less than 1 (an entry
  defined by its lines is under-identified by its chords alone).

### 4.6 Harmonic sequences as evidence of the local key (the Layer-5 §5.3 channel; review A-4)
A recognised harmonic sequence implies **motion of the local key** (the tonality — see the §0 "key" row). The consumer exposes each as a typed output
`{progression, transposition step, span, number of repetitions, prior strength}`. **U1 ruling (2026-07-02): a sequence requires ≥2 transposed statements of the SAME recognised entry** — that is
what "repeated at successive transpositions" (§0) means; a run's `repetitions` counts the matched windows, and the
evidence weight scales with it (more repetitions → stronger; direction fixed, values Stage-5). A **single**
recognition of an internally-sequential entry (circle-of-fifths, Monte, Fonte) emits **no** §4.6 sequence — its
key-motion implication is already carried by its schema-span (the entry's internal transposition structure is
catalog knowledge, readable by the F-C consumer when that wiring is designed; recorded in §9 so it is decided
there, not lost). **The consumer ALWAYS emits it —
evidence is never discarded** (the no-information-loss and use-every-clue principles; user-directed correction
2026-07-02, replacing an earlier "only where no cadence exists" gate that threw corroboration away). Layer 5 §5.3
uses it in two roles: **(i) corroboration, always** — sequence evidence agreeing with a confirming cadence raises
the candidate key's vote, disagreeing tempers it; **(ii) the substitute confirming channel** for condition (a)
**only where no authentic cadence confirms the candidate key**, at a weight **below** the cadence channel's
(ordering fixed; values Stage-5) — the cadence remains the stronger confirmation wherever it exists, by weight, not
by suppressing the other evidence. **Frame obligation:** comparing sequence evidence against the home-key
confidence is a NEW comparison; it must be declared in the confidence contract §4 (frame **F-C**) **before** the
§5.3 wiring is built. The consumer's own build (the annotation + the §5.5 feature) does not need it.

## 5. Where the idiom behavior lives *(post-swap, `0e155154fc`)*
The Vocabulary carries the idiom tags; the idiom **behavior** — the weight vector, the admission threshold, the two
soft-cue factors — is this consumer's, and only this consumer's (directions fixed in §4.5; values Stage-5). The
matcher is idiom-general: the weights grade, they never hard-filter (a functional cadence stays recognisable inside
a coloristic analysis — the empirical study found genre organizes harmony only weakly).

## 6. Architecture decisions (with the alternatives weighed)
- **D1 — Evidence plus a name, not a new layer.** *Alternatives weighed and rejected:* a standalone progression-parsing stage — it would
  duplicate Layer 5's role and the §8 mechanism.
- **D2 — Chords-only scope** (§2). *Alternatives weighed and rejected:* recognising line-defined schemata here — a different dimension with
  its own future home.
- **D3 — Exact matches now; partial/variant matching and all values Stage-5.** *Alternatives weighed and rejected:* building the fuzzy
  matcher now — accuracy work, firewalled.
- **D4 — Additive; the literal Roman numeral is never changed.** *Alternatives weighed and rejected:* rewriting the numeral to the
  substituted-for function — it loses the literal label the ground truth scores.
- **D5 — where does progression knowledge live? ✅ RATIFIED (user, 2026-07-02) — with the user's rider: the
  dependency map below is made EXPLICIT in code and specs at BOTH sites.**
  **The dependency map (what changes where — every reader must be able to answer this):**
  - *Changing the GRAMMAR* (which root motions are licensed at all) → change `functionprogression` (Layer 5) ONLY.
    The catalog never needs an edit for a grammar change — but the consistency test re-runs, and a catalog entry
    that now fails it is flagged (the entry was leaning on the old grammar).
  - *Changing the CATALOG* (add/edit a named progression or substitution) → change the Vocabulary ONLY. The grammar
    never needs an edit — but the new entry must PASS the consistency test (every adjacent pair licensed); a
    failure means the entry is mis-encoded OR a genuine grammar gap was found (escalate, don't tag around it).
  - *The two are NOT derived from each other* (grammar licenses more than convention names; the catalog is
    enumerative and grows from evidence) — the consistency test is the ONLY coupling, and it runs one way
    (catalog → grammar).
  **Build riders (the user's make-it-VERY-clear directive):** a cross-referencing comment block at BOTH code sites
  (`functionprogression.h`: "the Vocabulary holds the NAMED progressions; changing grammar here never requires a
  catalog edit; the consistency test in <test file> couples them one-way" — and the mirror in
  `harmonicvocabulary.h`), + the dictionary §5.1 owner note, + this map restated in the L5 spec §5.0 and the
  dictionary §1. All ride the consumer build instruction.
  *(The original question and alternatives, for the record:)*
  **The question.** Two places in the system know about chord successions: Layer 5's §5.0 licensing test ("is this
  root motion one of the licensed functional motions?" — a yes/no rule checked on every adjacent chord pair during
  analysis) and the Vocabulary's catalog of named progressions. The gap-analysis found the dictionary's §5.1 *also
  lists* the licensed pair motions — the same knowledge in two places; the standing one-owner rule demands a
  decision.
  **The decision (Cowork's proposal): one owner per item.** The **pair-motion licensing test** is owned by
  `functionprogression` (Layer 5) — grammar, evaluated at every transition. The **named progressions and
  substitutions** are owned by the Vocabulary — knowledge, queried. The dictionary's §5.1 list stays as descriptive
  context and gains a one-line note naming `functionprogression` as the licensing owner, so no reader mistakes the
  list for a second implementation (a doc rider at this consumer's build).
  **Alternative A — move the pair test into the Vocabulary** (licensing as catalog entries). *Pro:* literally one
  store for everything. *Con:* a rule evaluated on every chord transition of every analysis becomes a catalog
  lookup — the wrong shape for a hot-path yes/no test; and grammar (how function may move) is not a named
  convention (what musicians call a ii–V–I) — merging them blurs the knowledge/test distinction both specs rely on.
  **Alternative B — move the named progressions into Layer 5** (schemas as hardcoded analysis rules). *Pro:* no
  query indirection. *Con:* the future composition tool must use the same progression knowledge; hardcoded inside
  the analysis layer it is trapped there, forcing a second copy later — exactly the duplication the rule forbids.
  **How the Layer-5 side is actually held (user question, 2026-07-02):** NOT as a list — as **pure predicates on
  root motion** (about five interval rules computed from the two roots and qualities; size O(1), no table;
  `functionprogression`, built without constants). **The containment relation (user observation) — MEASURED, and
  Cowork's original premise CORRECTED (2026-07-02):** the assertion "every adjacent pair inside every catalog entry
  satisfies the predicate — both are built from the same grammar" was **falsified on first contact**: **6 entries /
  11 motions fail** (measured + pinned in the test — Cowork's earlier "12" was arithmetic error, U2; the plagal and
  other ascending-fifths incl. I→V; the Andalusian's descending seconds; the
  circle's diatonic diminished-fifth link) — all **musically correct**; what is narrow is the §5.0 licensed set,
  which descends from the old scoring-bonus signals, not from a complete functional grammar. **Ruled grammar gaps,
  L5-owned** (the §5.0 grammar-completion amendment — license ascending-fifth/plagal, descending-second, the
  diatonic diminished-fifth — Cowork-written, ratification-gated, its own dormant L5 increment). Deriving the
  predicate FROM the catalog stays rejected (enumerative/incomplete vs generative/complete — a missing entry would
  silently un-license legitimate grammar). The **consistency test** ships scoped to the TRUE containment: every
  pair is licensed OR on the explicit 6-entry known-gap list (any 7th failure = red); when the grammar amendment
  lands, the list empties and the test tightens to the clean assert.
- **D6 — what to NAME the span a recognised progression covers — RESOLVED BY PREFIXING (user direction, 2026-07-02):
  `progression-schema-span`.** The prefix answers the last collision standing: bare "schema" reads as *data* schema
  to any coder, while **"progression schema" is already this component family's own name** (this design and the
  dictionary are the progression-schema docs) — so the span is named by exactly what covers it: a recognised
  progression schema. Multi-word span names have precedent (decision-context span). §0's "Schema-span" row and all
  uses in this document read accordingly; the propagation rider (ARCHITECTURE §2.15 latent list + L6 §3/§5.5)
  carries the full name. *(The alternatives evaluated, for the record:)*
  **Not a new span type.** The §2.15 span typology already anticipated this span — it appears there as the *latent*
  "sequence-span", never yet instantiated; this design instantiates it. The only question is its **name**.
  **The problem with "sequence-span":** "sequence" already has a fixed music-theory meaning — the *harmonic
  sequence* (a progression repeated at successive transpositions), which this very document uses in that correct
  sense (§4.6). But the span in question covers **any** recognised named progression — a ii–V–I or a cadence
  formula, which are *not* sequences. "Sequence-span" would therefore promise something narrower than what it holds.
  **The decision (Cowork's proposal): `schema-span`** — named by its criterion (the span a recognised schema/named
  progression covers), consistent with its siblings key-span and punctuation-span, and colliding with nothing.
  Propagation rider: the typology's latent-list entry (ARCHITECTURE §2.15) + L6 §3/§5.5 — rides the next Cowork doc
  pass. **Alternative — keep "sequence-span":** *Pro:* no propagation edit. *Con:* the collision above, permanent.
  **Alternative — "progression-span" (user suggestion, 2026-07-02):** *Pro:* plainer than "schema"; no collision
  with the harmonic sequence. *Con:* this document (and Layer 5's output) already uses "the committed
  **progression**" for the WHOLE analysed chord stream — "progression-span" therefore reads as "any span of the
  committed progression", which every span is; the name fails to say *recognised named progression*. If that
  ambiguity is acceptable, progression-span works; Cowork's proposal remains schema-span because it collides with
  neither existing use ("schema" = a catalog entry, §0 "named progression" row).
  **Alternative — "chord-sequence-span" (user test, 2026-07-02):** evaluated and recommended against — "chord
  sequence" in plain language IS an ordered series of chords, i.e. the committed progression again (the same
  collision as progression-span, plus the word "sequence" back inside the name next to the harmonic-sequence sense
  §4.6 uses). Longer without disambiguating the one thing the name must say: *recognised NAMED progression*.
- **D7 — line-defined entries carry the "chords-only" mark** (§4.5) — the verifiability contract's explicit-mark
  path; the mark retires per entry when the voice-leading layer supplies the other half.

## 7. Quality & validation
- **Measurable now:** the common-practice and galant entries against the cadence/schema ground truth on the dev
  beds — precision/recall of recognised spans, and the evidence contribution measured as Roman-numeral accuracy
  change on exactly the chord positions a recognised progression covers (its only accuracy claim).
- **Not yet measurable:** the jazz/pop entries — no score-aligned ground truth (the census Tier-J want,
  user-ratified); until then those recognitions carry the "empirically-unvalidated" mark per the verifiability
  contract.
- **Dormant + byte-identical** until engagement: no production consumer; the corpus gate stays 53/24/53 by
  construction.

## 8. Risks & technical debt
- **Partial/variant matching is the hard part** — real music interpolates and alters members; the exact-match v1
  will under-recognise, and the §7 measurement will size by how much. Deferred deliberately (D3).
- **Substitution ambiguity** — whether a `♭II7` is a tritone-substituted dominant or a Neapolitan seventh is
  decided by its resolution context; that decision is Layer 5's (the same class as the `V/iv` over-trigger).
- **Catalog completeness is asymptotic** — on an unrecognised progression the consumer emits nothing (§3); it never
  guesses.

## 9. Open items
1. The dormant scaffolding build (recogniser + annotation + §5.5 feature) — this design's first step. **Includes
   the D5 consistency test** (every adjacent pair of every catalog entry passes `isLicensedProgression`).
2. Partial/variant matching + every §4.5/§4.6 value — precision-phase (Stage 5). **Its named FIRST FORM (user,
   2026-07-02): the pair-indexed weighted lookup** — for an unresolved chord, query the entries whose member-pair
   matches (this chord + its neighbour), weight each by its §4.5 prior strength, and feed the weighted list as §4.3
   evidence even where no full progression is recognised (more clues used, per the use-every-clue principle).
   Deferred with the rest of partial matching because it moves accuracy (measured, never shipped on plausibility)
   and consumes `w` — **when it lands, re-confirm §4.5's loop-freedom** (the declared resolution: mixture
   estimation stays on the exact-match subset only). Note the asymmetry ruling (D5): a licensed pair in no catalog
   entry is NOT a catalog gap (grammar licenses more than convention names); frequent corpus pairs absent from the
   catalog are the `idiom_discovery/` pipeline's evidence for growing it.
3. Jazz/pop ground truth — census Tier J (user-ratified 2026-07-02).
4. The voice-leading layer — prerequisite for the line-defined half of the D7-marked entries.
5. The composition-tool consumer of the same Vocabulary — out of scope here.
6. The one-store question — **RULED (D5), pending user ratification**; closes on sign-off.
7. The §5.3 key channel — **specified (§4.6), pending user ratification**; frame F-C declared before wiring
   (L5 spec §15-10 cross-reference).

## 10. QA record (the prescribed audits — Cowork, 2026-07-02; re-run on the v4 rewrite)
**(i) The three design-doc standards.** *Specify-by-rule:* exact-match admission (§4.1); overlap preference order
(§4.1); the prior-strength formula with max-not-sum (§4.5); the admission threshold, mode-cue factor, and
chords-only factor — each named as one declared constant with direction fixed (§4.5); both §4.3 conditions stated
in full; the §4.6 admission condition and weight ordering. Deferred items defer values only, never decision
structure. *Code-free body:* mechanisms named by role; identifiers confined to the header, §0 citations, D5, §9.
*Standard vocabulary + defined terms:* the §0 table defines or cites every term used — including the previously
undefined "Prinner", the project term "carried readings" (restated as **ranked candidate readings** with the L4 §7
citation), and the frame/confidence terms; "iff" and other shorthand removed.
**(ii) Language-mechanical pass:** "committed" → an L4 `Commit` with its composite confidence (§0, §4.3);
"contradicts" → the member position demands a different root or quality (§4.3); "overridden" → the full F-B test
restated with threshold-scaling, tie, and once-per-pass rules (§0, §4.3); "admitted" → prior strength above the
declared threshold (§0, §4.5); "exact" → match score 1.0 (§0, §4.1); "below the cadence channel's weight" →
ordering fixed, value deferred (§4.6). No pointer word in the body lacks its argument.
**(iii) Cross-architecture consistency:** forward-only (committed stream in; §5.5 feature + §8 selection-only
override + L6 annotation out; no note access, no back-edge); frame discipline (rides F-B; the one new frame F-C
declared before wiring, per contract §4); span typology (schema-span cross-cuts punctuation-spans, matching L6
§3/§5.5; rename rider D6); one owner per concern (D5; no second matcher/detector; the Vocabulary stays
decision-free); verifiability (dev-bed-measurable for common-practice/galant; jazz/pop marked until Tier J);
bounded context (committed-stream-only; no extension requests); proportionality (no new layer; dormant; engage
criteria unaffected — G1 excludes the consumer).

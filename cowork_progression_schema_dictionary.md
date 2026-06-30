# The Harmonic Vocabulary — progression & substitution knowledge base (component spec)

> **Status: component spec, v1 draft (2026-06-29).** A reference catalog of harmonic conventions, queried by other tools.
> Specified by rule and content. Companion consumer design: `cowork_progression_schema_design.md`; architecture placement:
> `cowork_target_architecture.md` §2.

## 1. What this component is
The Harmonic Vocabulary is a **curated reference catalog of harmonic conventions** — the named chord **progressions** and
the chord **substitutions** of tonal music. It is **knowledge, not a tool that acts**: it stores the conventions and
answers questions about them; it analyses no score and composes no music. It keeps **no information about any particular
piece of music** — it returns the same answers no matter what is being analysed or written, and remembers nothing between
queries.

Its **consumers** query it:
- the **analysis tool** — to *recognise* a written progression and *disambiguate* a chord by the pattern it completes;
- a future **composition tool** — to *suggest* progressions and substitutions from what is already written.

It is built **shareable** for both. Because every consumer **queries** it and it acts on nothing itself, it is **not one
of those tools** — it is the reference they consult.

## 2. What it does, and does not do
**It does:** hold the catalog (§5) and answer the four queries of §4 — *browse*, *recognise*, *suggest*, *expand* — each
returning a **ranked list of candidate entries**.

**It does not:**
- **Decide anything.** The matching threshold, the style weighting, and the choice of what to do with a candidate are the
  **consumer's**; the component only supplies ranked candidates.
- **Hold voice-leading.** It is the **harmonic** vocabulary — chords and functions. Voice-leading (the motion of
  individual voices — for example the melodic lines that, together with the harmony, complete a galant schema) is a
  **different dimension**, held elsewhere (a future voice-leading layer, or a separate voice-leading vocabulary). A schema
  conventionally defined by voice-leading is present here **only by its harmonic pattern**; its voice-leading is held
  elsewhere and combined when the complete schema is recognised.
- **Select or detect a style.** The active style is chosen by the **preset** (or, in future, inferred by a style
  classifier); the component only carries a **style label** on each entry.

## 3. The entries — what an entry is
An **entry** is one record in the catalog: a single named harmonic convention. There are **two kinds**:
- A **progression entry** — a named, recurring chord progression (a *schema*): for example `ii–V–I`, a turnaround, a
  circle-of-fifths sequence, the harmonic pattern of a Prinner, or a single generative slot such as `V7/x → x`. It is
  represented by its **functional skeleton**.
- A **substitution entry** — a named substitution *operation*: for example the tritone substitution, or modal interchange.
  It is represented by its **substitution mapping** — the rule by which a substituted chord stands for the function it
  replaces.

Every entry carries:
- **Name** — its conventional name.
- **Style tags** — one or more values of the **canonical style taxonomy** (§6, the same vocabulary the presets select on),
  multi-valued because a convention can belong to several styles.
- **Functional skeleton** (progression entries) — the pattern as a **key-relative** sequence of (scale-degree,
  chord-quality) pairs, or, for the bass-line and galant entries, of bass/melody scale-degrees. Being key-relative, one
  entry instantiates in every key; being **degree-parameterised**, a generative slot instantiates at every target degree.
- **Substitution mapping** (substitution entries) — the rule mapping the substituted surface chord to the underlying
  function (e.g. `subV7/x` stands for the dominant of `x`).
- **Provenance** — the established source the entry is drawn from (§11).

## 4. The query interface — what a consumer supplies, and gets back
A consumer issues a **read-only query**: it **supplies an input**, and the component **returns a ranked list of candidate
entries**. The component never changes a consumer's state. This section fixes the interface **by meaning** — each query's
input and output; the concrete signatures and data types follow the build (§12). **Every query takes one common input —
the active style subset** (the styles the preset has selected; default = all).

A **span**, used below, means **a contiguous run of one or more committed chords**, each chord with its decided function
and key — the form the analysis tool produces. A single chord is a span of length one.

The four queries:
- **Browse** — *input:* nothing beyond the style subset. *Output:* every entry in the active styles (used to load the
  active catalog).
- **Recognise** *(the analysis direction)* — *input:* a span. *Output:* the **progression entries** whose functional
  skeleton that span realises, each with the substitution mapping for any substituted member.
- **Suggest** *(the composition direction)* — *input:* a span from the score **and** a direction. *Output* by direction:
  - **follow** → **progression entries** that could continue *from* the span;
  - **precede** → **progression entries** that could lead *into* the span;
  - **replace** → **substitution entries** applicable to the span, plus same-function diatonic alternatives.
- **Expand** — *input:* a scale degree `x`. *Output:* the generative slots for `x` (§5.1: `V7/x`, `viio7/x`, `IIm7/x`,
  `subV7/x`, and the sub's related ii).

**Every returned entry carries a match score** — the component's structural measure of how well the input realises (or,
for *suggest*, is realised by) the entry — and the list is **ranked** by it (secondarily by specificity, then length). The
consumer applies its own style weighting and its own threshold; there is no binary match/no-match, only the score (as the
inference layers carry ranked alternatives with confidence). **The list may be empty** — for *recognise* (nothing
matches), for *suggest follow/precede* (no progression fits), and for *suggest replace* (no substitution applies) — and a
consumer must handle an empty result, never assuming a non-empty one.

**Suggesting substitutions and progressions (what the component answers, and what it leaves to the consumer).** A *suggest
replace* query returns substitutions for **whatever span it is given** — so a consumer may ask for substitutions on the
**score's own chords** (reharmonise what is written), **or** on the chords of a **progression it was just suggested** (vary
a suggestion), **or both**; the component answers each request identically and **does not itself combine them**. Chaining —
"suggest a progression, then substitute within it" — is the **consumer's** logic. **Progressions are suggested in their
plain form** (the functional skeleton, no substitution applied); substitutions are separate entries the consumer may then
apply. So from these two query results a consumer can offer a plain progression, a substitution on existing chords, or a
substitution within a suggested progression — composed at the consumer, not here.

## 5. The content — organisation and catalog
The catalog is **generative where it can be** (a small set of slot-types instantiated per target degree) and **enumerated
where it must be** (the named recurring patterns). **The lists below are a first pass, not exhaustive** — a registry to
extend (§12). Style tags are placeholders pending the canonical taxonomy (§6).

### 5.1 The function map — the systematic spine
The diatonic, secondary, and substitute functions form a **systematic, generative spine**: parameterised by a **target
degree `x`**, the same slots instantiate per degree. **This is general tonal harmony, not a style-specific vocabulary** —
the diatonic and secondary functions underlie common-practice and jazz alike; only the tritone *substitute* dominants are
chiefly a jazz device. (Its systematic *presentation* follows Ramos's *Mapping Tonal Harmony*, a teaching tool; the
*content* is the shared functional system, not a jazz-only set.)
- **Diatonic functions** `[all styles]` — Tonic family `I, vi, iii`; pre-dominant family `IV, ii (+ vi)`; dominant family
  `V, viio (+ iii)`. The functional flow is T → (T) → SD → D → T; the licensed pairwise root motions are the descending
  fifth, the descending third, and the ascending second.
- **Secondary functions, per non-tonic diatonic `x`** `[common-practice + jazz]` — the secondary dominant `V7/x`; the
  secondary leading-tone `viio7/x` (or `viiø7/x`); the related ii `IIm7/x`, giving the applied ii–V `IIm7/x → V7/x → x`.
- **Substitute dominants, per `x`** `[chiefly jazz; the common-practice cousin is the German sixth]` — the tritone
  substitute `subV7/x` (in C, `subV7/I = bII7 = D♭7`, resolving down a semitone to `x`) and its related ii. *(The
  `subV7/I` is enharmonically the German sixth — the common-practice chord the analysis tool already separates by spelling,
  L5 §5.6.)*
- **Modal interchange (parallel-mode borrowing)** `[all styles]` — in major, borrow from parallel minor (`iv, iiø7, bVI,
  bVII, bIII, bII` Neapolitan, minor `v`, `viio7`); in minor, borrow from parallel major (Picardy `I`, raised `IV`).

### 5.2 Named progressions & schemas
- **Cadential** `[common-practice + jazz]` — authentic `V(7)→I` (perfect/imperfect by inversion), half `…→V`, deceptive
  `V→vi` (`→bVI` in minor), plagal `IV→I`, Phrygian half (minor, `iv6→V`). *(Already detected by L5 §5.2; listed for
  completeness.)*
- **The ii–V family** `[jazz + common-practice]` — `IIm7–V7–Imaj7`; minor `iiø7–V7–i`; the incomplete `ii–V` (no
  resolution) as its own unit.
- **Turnarounds** `[jazz]` — `I–vi–ii–V` (and the secondary-dominant'd `I–VI7–ii–V`), `iii–vi–ii–V`, the rhythm-changes
  A-section.
- **Sequences** `[common-practice + jazz]` — circle-of-fifths (`…iii–vi–ii–V–I`; fully `I–IV–viio–iii–vi–ii–V–I`);
  descending-thirds (`I–vi–IV–ii…`); the stepwise galant Monte/Fonte skeletons (below).
- **Bass-line and pop loops** `[common-practice + pop]` — lament bass / descending tetrachord (minor `1̂–7̂–6̂–5̂`, chromatic
  variant `1̂–♭7̂–♭6̂–5̂`); Andalusian cadence `i–bVII–bVI–V`; doo-wop `I–vi–IV–V`; Axis `I–V–vi–IV` (and rotations);
  Pachelbel `I–V–vi–iii–IV–I–IV–V`.
- **Galant schemata — harmonic pattern only** `[galant]` — Prinner (melody `6̂–5̂–4̂–3̂` over bass `4̂–3̂–2̂–1̂`); Romanesca
  (descending bass, `I–V–vi–iii…`); Monte (ascending sequence); Fonte (descending sequence of applied-resolution pairs);
  Ponte (a dominant pedal); Do-Re-Mi (opening, melody `1̂–2̂–3̂`); Quiescenza (a tonic-pedal closing schema). *(Each is
  conventionally defined by voice-leading and metric placement; this component holds only the harmonic pattern — see §2.
  The complete schema is recognised by combining it with the voice-leading dimension held elsewhere.)*
- **Advanced jazz cycles** `[jazz]` — Coltrane changes (a major-thirds key cycle); backdoor `bVII7→I`.

### 5.3 Substitution operations
**Substitution is not dominant-only — it operates on every functional family.** The **tonic** (`I↔vi↔iii`, the deceptive
`vi`, chromatic-mediant and modal-interchange tonics), the **pre-dominant** (`ii↔IV`, the borrowed `iv`/`iiø7`, the
Neapolitan `bII`), and the **dominant** (the tritone sub, `viio7`, the backdoor) each have substitutes. Only the **tritone
substitution** is *dominant-specific* (it exploits the dominant seventh's tritone) — and even it applies to a dominant of
**any** degree (`subV/ii`, `subV/IV`, …), the per-degree "substitute dominants" slot of §5.1. Each operation below is over
the skeleton — analysis *inverts* it (recognises the substituted surface as the underlying function); composition *offers*
it (proposes the substituted form):
- **Secondary dominant / tonicization** `[common-practice + jazz]` — tonicize any diatonic `x` with `V7/x` or `viio7/x`.
- **Related ii–V** `[jazz]` — precede any `V7/x` (or `subV7/x`) with its `IIm7`.
- **Tritone substitution (subV)** `[jazz]` — replace any dominant `V7/x` with `subV7/x` (a tritone away); canonical cases:
  the `V` in ii–V–I, the `VI7` in I–VI–ii–V, the `ii`.
- **Diatonic (functional) substitution** `[common-practice + jazz]` — replace a chord with a same-function diatonic chord
  sharing tones (`I↔iii↔vi`, `IV↔ii`, `V↔viio`).
- **Modal interchange** `[all styles]` — substitute a parallel-mode chord (§5.1).
- **Diminished approach** `[common-practice + jazz]` — insert a passing/auxiliary diminished seventh between diatonic
  chords (`I–#io7–ii`).
- **Deceptive resolution** `[common-practice + jazz]` — resolve a dominant to a non-tonic (`V→vi`, `V→bVI`).
- **Line cliché** `[common-practice + jazz + pop]` — a chromatic inner line over a held chord (`i–i(maj7)–i7–i6`); the line
  itself is voice-leading and lives elsewhere (§2); held here by its harmonic pattern.
- **Upper-structure / voicing substitution** `[jazz]` — a *voicing* device (rootless, upper-structure triads, sus); it is
  a voicing, not a function, so it is **outside this component** (noted only so it is not mistaken for a function-level
  substitution).

## 6. Crosscutting concepts
- **Bidirectionality (analysis ⇄ composition).** Every entry is usable in both directions; the component privileges
  neither, and new entries are added with both readings in mind.
- **One canonical style taxonomy, shared with the presets.** Entries tag from a **single style vocabulary** that the
  presets also select on — not a vocabulary private to this component (which would need a brittle preset→tag mapping). The
  taxonomy's values, granularity, and any hierarchy (Baroque within common-practice; bop within jazz) are a **shared
  decision with the preset system**; the §5 tags are **placeholders** until it is fixed (§12).
- **Style behavior is the consumer's.** The component carries the style **label**; the **preset selects** the active
  subset, the **style weighting** (a graded prior — not a hard filter, since styles blend) and the **threshold** are the
  consumer's, and **style detection** is a future classifier. One encyclopedia, not per-style silos — a shared convention
  (`ii–V–I`; `subV` = the enharmonic German sixth) is a single entry, its cross-style links visible.
- **The firewall line.** The component holds **structural content** and returns **ranked structural matches**; the
  weighting, the threshold, and the decision are **precision-phase, at the consumer**. Adding or correcting an entry is a
  content change here; tuning how strongly an entry fires is a precision-phase change there.

## 7. Component decisions (with the alternatives weighed)
- **D1 — An independent component, queried by the tools, not part of any of them.** *Rejected:* embedding the catalog in
  the analysis tool — it stores nothing about any one piece, and a future composition tool consumes it without the
  analysis tool at all.
- **D2 — Bidirectional: it serves analysis and composition equally.** *Rejected:* an analysis-only catalog — the same
  patterns and substitutions are what a composition tool needs read predictively; an analysis-only catalog would force a
  duplicate.
- **D3 — Generative where possible, enumerated where necessary.** The secondary/substitute apparatus is parameterised by
  target degree; only the named recurring patterns are enumerated. *Rejected:* a fully enumerated flat list (combinatorial,
  and it hides the systematic structure).
- **D4 — One style taxonomy, shared with the presets; style behavior at the consumer.** *Rejected:* a tag set private to
  this component (it would drift from the presets); per-style silos (duplicate shared entries); a hard style filter
  (styles blend).
- **D5 — Harmonic scope; voice-leading is a separate dimension held elsewhere.** *Rejected:* holding voice-leading here —
  it is a different dimension with its own future layer; this component holds the harmonic pattern, combined with the
  voice-leading dimension when a complete schema is recognised.

## 8. Quality, provenance & validation
- **The component's quality is the correctness, coverage, and provenance of its entries** — each traceable to an
  established source (§11), not invented. That is what makes an entry true.
- **Validation belongs to the consumer** — how well a consumer *uses* the knowledge, measured where a ground truth exists:
  for analysis, schema precision/recall and the disambiguation contribution to Roman-numeral accuracy; for composition,
  the idiomaticity of suggestions against the style's corpus.
- **A missing ground truth is a consumer limitation, not an entry property.** The analysis tool can measure its use of the
  common-practice and galant entries against the chorale ground truth, but cannot yet measure its use of the jazz and pop
  entries — there is no jazz/pop ground truth. That bears on the consumer's measured accuracy, not on the entries' truth.
  A jazz/pop ground truth is a named consumer want (§12).

## 9. Risks & technical debt
- **Completeness is asymptotic** — a registry to extend; a consumer must degrade gracefully on the unrecognised and never
  assume the catalog is exhaustive.
- **The galant and other voice-leading-defined entries are present only by their harmonic pattern** — a consumer must not
  read them as full schema recognition; the complete schema needs the voice-leading dimension combined in (§2).
- **No jazz/pop ground truth for the consumer** — the consumer cannot yet measure its use of the load-bearing jazz/pop
  entries (the entries are sound theory by provenance); the named want is §12.
- **Matching candidates is the component's; deciding is the consumer's** — a consumer must not treat a returned candidate
  as a decision.

## 10. Glossary
- **Progression** — an ordered succession of chords/functions.
- **Schema** — a named, recurring multi-chord progression (a progression conventional enough to have a name).
- **Substitution** — an operation replacing a chord with another that fills the same functional slot (e.g. a tritone sub
  for a dominant).
- **Entry** — one catalog record: a single named convention. Two kinds — a **progression entry** (a schema, by its
  functional skeleton) and a **substitution entry** (an operation, by its substitution mapping).
- **Functional skeleton** — a progression entry's key-relative, degree-parameterised (scale-degree, quality) sequence.
- **Substitution mapping** — a substitution entry's rule mapping a substituted surface chord to the function it replaces.
- **Span** — a contiguous run of one or more committed chords (each with its function and key); the input to *recognise*
  and *suggest*.
- **Style tag** — the style label(s) on an entry, from the canonical style taxonomy (§6, shared with the presets),
  multi-valued.
- **Generative slot** — a secondary/substitute function defined per target degree `x` (`V7/x`, `subV7/x`, …), instantiated
  on demand rather than enumerated.
- **Match score** — the component's structural measure of how well a query input realises (or is realised by) an entry;
  the return is ranked by it and the consumer thresholds and weights it.
- **The two directions** — *analysis* (read an existing progression to recognise/disambiguate) and *composition* (read a
  span to suggest what could follow, precede, or replace it).

## 11. Related work & sources
Mapping Tonal Harmony (Ariel J. Ramos / mDecks — the systematic presentation of the function map: diatonic functions,
secondary functions `V7/x · viio7/x · IIm7/x`, substitute dominants `subV7/x` + their related ii). Jazz reharmonization
literature (tritone sub, modal interchange, diatonic sub, related ii–V, diminished approach, backdoor, Coltrane changes).
Galant schemata — Gjerdingen, *Music in the Galant Style*; Katsiavalos (ISMIR 2019). Progression-as-language-model (the
inference grounding the consumer relies on) — Korzeniowski & Widmer 2018; Sears et al.; Tymoczko. Cross-refs:
`cowork_progression_schema_design.md`, `cowork_layer6_grouping_research.md`, `contrapunctus_findings.md`,
target-architecture §2.

## 12. Open items
1. **★ The canonical style taxonomy — proposed, pending joint ratification with the preset system.** One style vocabulary
   tags the entries and the presets select on it, defined **once** in a shared home (not privately here). The **inclusion
   rule** (the durable part): a style is listed iff it has a **distinct functional-harmonic vocabulary**; non-functional
   idioms (free jazz, atonal) are excluded — they have no progression catalog. **Hierarchical** (family → style), so an
   entry or preset tags at the granularity it needs and the graded prior can use the hierarchy. **Proposed list
   (research-grounded 2026-06-29, extensible):**
   - **Common-practice:** Baroque · Classical/galant · Romantic.
   - **Jazz:** trad (New Orleans/Dixieland) · swing/songbook · bebop · hard-bop · cool · modal.
   - **Vernacular/popular:** blues · ragtime · gospel/soul-R&B · rock · pop · folk · barbershop.
   The §5 tags are placeholders until this is ratified and promoted to its shared home; the exact set is a **joint decision
   with the presets**, not this component's call alone. The hand-made list is a **theory-based v1**; **empirical grounding**
   — deriving the taxonomy *and* the per-style weights by clustering corpora — is committed future work
   (`cowork_style_clustering_plan.md`), to refine or replace it when picked up.
2. **Fill the catalog** across styles (the ongoing registry work, especially the jazz set).
3. **A jazz/pop ground truth** — the named consumer want: it would let a consumer measure its use of the jazz/pop entries.
4. **A voice-leading vocabulary / the voice-leading layer** — the separate concern holding the voice-leading dimension of
   the galant (and other) schemata, combined with this component when a complete schema is recognised; not content here.
5. **The composition/suggestion consumer** — the future tool that reads this component predictively; built shareable for
   it, but the suggestion logic is its own design, not this spec's.
6. **The entry-schema serialisation and the syntactic query API** — the on-disk form of an entry and the concrete query
   signatures (a build-time decision; the entry schema §3 and the semantic query contract §4 are fixed here, their
   syntactic form is not).

# The product-tool register — what can be built on the inferrers, and what the inferrers must note now

> **Status: RESEARCH NOTE (Cowork, 2026-07-03; user-directed).** A durable register of candidate product tools
> for the composer / analyst / arranger / engraver, built on the analysis architecture (with or without the
> chord track), PLUS the inferrer-side requirements they imply. Companion to
> `cowork_candidate_lever_register.md` (inference levers). **Nothing here is commissioned**; product work is
> out of scope until the architecture/algorithm/refactoring completion (standing rule) and each tool would get
> its own design. The register exists so product pull is *known while inferrer contracts are still cheap to
> shape*.
>
> Grounding: the **chord track exists** (`populateChordTrack()` / `implodeToChordTrack`, the implode bridge —
> ARCHITECTURE §3); the user-named seed ideas (analysis/experimentation chord track; circle-of-fifths / map
> visualizations for progressions+subs; contrapuntal warnings/suggestions; score annotation with chord symbols /
> RN / Nashville / key+mode) are taken as given and not repeated below.

## 1. Candidate tools (by persona; each names the inferrers it stands on)

### Composer

- **T-1 Harmonization / reharmonization assistant.** Melody (or bass) in → ranked, idiom-conditioned harmonic
  progressions out; substitution suggestions from the Harmonic Vocabulary ranked by the same scorers that
  analyze. Stands on: L3 key, L5 grammar, Vocabulary + idiom mixtures, VL-H for realization. Needs: E-2, E-3,
  E-9.
- **T-2 Continuation suggestion ("what could come next").** The licensed-progression grammar + schema priors run
  generatively from the current context. Needs: E-2, E-9.
- **T-3 Modulation planner.** Key-to-key path-finding with pivot-chord suggestions (L3/L5 tonicization machinery
  inverted; the R-3 tonal-distance spaces are natural cost functions). Needs: E-2, E-3.
- **T-4 Schema templates.** Insert a Prinner / Monte / Fonte skeleton and fill it in — VL-F inverted;
  Gjerdingen-style pedagogy meets composition. Needs: VL-F built, E-3.
- **T-5 Texture realization.** "Realize this chord track as Alberti / chorale / pianistic / comping" — the
  axis-2 texture classes as generation targets. Needs: VL-G (voicing models), the axis-2 motion models as
  generators, E-3.
- **T-6 Cadence assistant.** Detect weak/missing closure at phrase ends; suggest cadence types fitting the idiom.
  Stands on: L5 cadences + L1.5/L6. Needs: E-4.

### Analyst / educator

- **T-7 Explainable-analysis inspector.** Click any label → the ranked alternatives, margins, licensing,
  schema membership, and the evidence that decided it. Stands on: the zero-information-loss carried-alternatives
  contract (ratified) + provenance. Needs: E-1, E-7.
- **T-8 Ambiguity heatmap.** Calibrated uncertainty rendered on the score — honest abstention as a feature.
  Needs: E-4.
- **T-9 The piece map.** One overview: key-spans, punctuation-spans, cadence plan, schema spans, texture spans
  (keyscape-style multi-scale option). Stands on: L6 + axis-2. Needs: E-6.
- **T-10 Analysis grading (pedagogy).** Student RN vs reference, diffed on the granularity-robust unit — the A-8
  machinery is structurally a grading engine. Needs: E-4, E-10.
- **T-11 Corpus search.** "Every deceptive cadence / Fonte / tritone substitution in my library." Needs: E-10.
- **T-12 Counterpoint pedagogy.** Species exercises checked live; fugue entry detection (subject/answer via
  VL-D/E). Stands on: VL-H, VL-D/E. Needs: those components built.

### Arranger

- **T-13 Lead-sheet extraction.** Full score → melody (stream separation) + chord symbols (L4/L5). Needs: VL-D,
  E-8 (symbols as first-class objects).
- **T-14 Lead sheet → arrangement.** The inverse: chord track + texture/idiom choice → realized parts. Needs:
  T-5's stack + VL-H.
- **T-15 Orchestration hints.** Which lines are melodic / harmonic / static per passage (texture functions) →
  instrument assignment support. Stands on: axis-2 (+ the Couturier-syntax bed as validation). Needs: VL-C
  per-span (§15-1).
- **T-16 Range-aware re-keying.** Key choice minimizing instrument/vocal awkwardness under the analysis. Needs:
  E-3 (conditioning on forced key).

### Engraver

- **T-17 Notation QA.** Enharmonic respelling from key context; courtesy accidentals at key-span boundaries;
  **symbol-vs-sound warnings** ("this Cm7 chord symbol disagrees with the sounding notes"). Stands on: L3/L4
  spelling machinery. Needs: E-8.
- **T-18 Auto chord symbols.** L4/L5 → chord-symbol layer (lead sheets, worship, jazz parts). Needs: E-4, E-8.
- **T-19 Voice/staff cleanup.** Re-notate implied polyphony into proper voices — VL-D inverted (the
  cluster-and-separate literature is the method line). Needs: VL-D.
- **T-20 Figured-bass generation.** For Baroque editions — lever R-4 inverted. Needs: R-4's evidence channel.

### Intonation / tuning (the already-built consumer — user-recalled 2026-07-03, verified at `tuning_system.h`)

The intonation subsystem already encodes the tuning-over-time design: the retune-susceptibility hierarchy
(P0 protected anchor → P1 held notes → P2 bass → P3 analyzer root), anchors (zero offset, never retuned/split),
and the drift policy (`FreeDrift` accumulate-then-reset via markers, `backlog_drift_reset.md`, vs tonic-anchored
JI). It consumes the LEGACY analysis path today — see the engage note under E-13.

- **T-21 Analysis-driven adaptive just intonation.** The tuning hierarchy fed by the new spine: L4 chord identity
  → correct just ratios; **per-note chordal-vs-NCT status → vertical purity for chord tones, melodic tuning for
  NCTs** (the L4 NCT filter is audibly load-bearing here); L3 key-spans → tonic anchors; modulations → re-anchor
  events; **cadences → musically-motivated drift-reset points** (replacing arbitrary markers); VL-A lines → the
  held-note tier + a principled horizontal-smoothness cost. Method line for the optimizer: the adaptive-tuning
  family balancing vertical purity / melodic stability / global drift (deLaubenfels' spring model; Hermode as the
  commercial precedent) **[reported — re-confirm before load-bearing use]**. Note: **enharmonic spelling is
  audible in JI** (G♯≠A♭) — the spelling-aware chord work directly serves this consumer.
- **T-22 Drift visualization / reset planner.** Show accumulated drift over time; suggest reset points at
  cadences / section boundaries / key-span edges. Stands on: L5 cadences, L6 spans, the tuning engine.
- **T-23 Style-aware temperament defaults.** Idiom/era machinery suggesting the temperament (Werckmeister/
  Kirnberger for Bach, meantone for early repertoire, adaptive JI for chorale singing…). Stands on: the idiom
  layer + the existing TuningRegistry.
- **T-24 Performer intonation guidance.** Already a stated ARCHITECTURE purpose ("intonation guidance for
  performed music") — per-part expected-intonation cues from T-21's stack.

### From the second sweep (2026-07-03; adjacent tool spaces + confirmed gaps)

**Market references mined** (what exists, to learn from, none of it score-integrated with real analysis):
Synfire/Cognitone (harmony workstation; claims "the most comprehensive voice-leading algorithm in the
industry"), Liquid Notes/Re-Compose (reharmonization by substitution), RapidComposer (phrase-based composing,
auto-harmonize), Scaler / Captain Chords (chord assistants), Mapping Tonal Harmony Pro (interactive functional
maps), Hooktheory/Hookpad (progression+melody pedagogy), Opusmodus (Lisp composition environment with analysis
tools). **[reported]**

**The MuseScore-ecosystem landscape (GitHub probe, 2026-07-03 — [reported]):** upstream `musescore/MuseScore`
carries NO automatic-analysis engine work (all RN activity is the manual text element; PR search for
engine work empty). The plugin ecosystem is the closest cousin — `Chord ID and Roman Numeral Analysis` (fork of
`Chord Identifier Pop & Jazz`), the jwmatthys theory plugins — and its self-declared limits map onto our layers:
no automatic key detection (L3), manual "harmonic pedal markers" to glue broken chords/Alberti (L2 slicing +
NCT/texture), vertical stack-matching only (no L5 function/cadence), no confidence/alternatives. Sustained
demand signal: plugins forked and re-ported across 4.3→4.6; a decade-old "Implementing harmonic analysis" wish
thread. Caveat: GitHub does not index most forks' code; private branches invisible — no-evidence, not
proof-of-absence. The closest full system remains Contrapunctus (standalone, non-MuseScore).

**Confirmed gaps (users ask; no adequate software found):**
- **G-1** Melody↔harmony *relation* — forum-stated: the chord assistants "don't relate melody with harmony". Our
  per-note membership/NCT machinery does exactly this natively.
- **G-2** A score-anchored analysis-overlay workbench with synced playback (color regions, RN/function labels,
  play-and-highlight) — researchers name iAnalyse (Mac-only) and report **no Windows equivalent**.
- **G-3** Real notation-proofreading *software* — the market is human proofreading services; no analysis-backed
  checker exists (T-17's space is empty).

**New tool candidates (beyond T-1…T-24):**
- **T-25 Melody↔harmony conformance view (G-1).** Per melody note: chordal / tension / NCT-kind against the
  accompaniment, live while composing. Stands on: L4 membership + NCT (E-11), VL-A lines.
- **T-26 The analyst's overlay workbench (G-2).** Score + colored analytical overlays + annotation layers +
  synced playback + **publication/teaching export** (analysis figures). The natural home of the user-named
  visualization ideas; in-MuseScore = the gap-filler.
- **T-27 The harmonic what-if debugger (no precedent found).** Step through the analysis like a debugger:
  inspect any decision's evidence, **pin an alternative reading** ("treat this as ii°6"), watch the analysis
  re-flow downstream. Stands on: E-1 (alternatives), E-3 (clamping), E-7 (evidence trail), bounded incremental
  re-analysis (E-5).
- **T-28 Harmonic diff / analysis version control (no precedent found).** Diff two revisions of a piece
  functionally ("what did my edit change harmonically"); arrangement-vs-original comparison. Stands on: the A-8
  diff machinery (structurally a differ), E-10.
- **T-29 Ensemble-idiom & playability conformance (G-3 extension).** Range, voice-crossing, tessitura, texture
  conventions per ensemble (SATB / brass / strings) — the analysis-backed proofreader the market lacks. Stands
  on: axis-2 + notation QA (T-17).
- **T-30 The piece's-journey map.** Not an abstract circle-of-fifths/MTH map (those exist) but the **actual
  piece's trajectory** plotted through the map — key-span path, schema/cadence landmarks, confidence-weighted.
  Stands on: L3/L6 + R-3 spaces.
- **T-31 Repertoire-derived pedagogy.** Ear-training/theory exercises generated from the user's OWN library
  ("name this cadence" drawn from pieces they play). Stands on: E-10 + the analysis outputs.
- **T-32 Difficulty/complexity grading.** Harmonic/contrapuntal complexity estimation per piece/passage
  (idiom + chromaticism + texture axes) — repertoire selection for educators. Stands on: both axes + calibration.
  **★ License caveat (union search, ratified 2026-07-04):** every real piece→grade label source found
  (CIPI/Henle, PSyllabus/exam boards, pianosyllabus.com) is research-only or proprietary at origin — a
  COMMERCIAL grading feature needs a negotiated license path or own-built labels; CIPI+Mikrokosmos cover
  research validation only. Record: `cowork_union_search_record.md` §3.

## 2. Inferrer-side requirements to note NOW (the product pull on contracts)

- **E-1 Ranked alternatives everywhere** — ratified (zero information loss); every suggestion tool consumes the
  lists. Keep enforcing at every new layer boundary. *(Status: in force.)*
- **E-2 The audition API.** Every judgment layer exposes its **scoring function over externally proposed
  candidates** ("score this substitution in this context") without full re-analysis. Largely true internally;
  declare it a stable per-layer contract at each layer's next touch.
- **E-3 Conditioning/clamping.** Decoders accept pinned variables (fixed melody note, forced key, locked bass):
  harmonization/experimentation = *conditioned inference*. Spelling pins are the existing precedent; generalize
  deliberately, per layer, at design time.
- **E-4 Calibrated confidence is a product prerequisite** (suggestion ranking, heatmaps, grading) — the Stage-5
  Class-P work carries product weight, not just internal hygiene. *(Status: the active runway.)*
- **E-5 Interactive latency budget.** Bounded-context incremental re-analysis (R2) gains a product latency
  target (drag-a-chord loops): note budgets at engage-time perf work (G3's neighbor).
- **E-6 Stable annotation identity across edits.** Analysis objects need identities that survive score editing
  (an L1 anchoring scheme) — cheap to design early, painful to retrofit. A data-design item for the engage arc.
- **E-7 The evidence trail as a public contract.** Provenance (cues, licensing, schema, frames) becomes stable
  output, not debug info — the "why" inspector's substrate. Trending this way already; declare when first
  consumed.
- **E-8 Notated chord symbols as INPUT evidence.** Lead sheets carry symbols; the analyzers should consume them
  as strong priors (today the pipeline is notes-only). A named future L4-evidence channel (parallel to R-4
  figured bass — both are composer-stated harmony).
- **E-9 Diverse k-best.** Suggestion lists want diversity across substitution *families*, not five variants of
  one idea — a decoding concern to note before Stage-5 fixes ranking behavior.
- **E-10 A persistent, indexable analysis store.** Corpus search and grading need per-library cached analysis —
  a storage/product concern outside the analysis layers; noted so it is designed as a consumer, never wired into
  inference.
- **E-11 Per-note chordal-membership / NCT status at the boundary.** The tuning consumer (T-21) needs, per note,
  "chord tone of X" vs "non-chord tone (kind)" — the L4 membership output + the future NCT filter, declared as a
  consumable boundary output (with confidence, per the contract).
- **E-12 Key-span / modulation / cadence anchors as declared consumable outputs.** T-21/T-22 consume them as
  tuning re-anchor and drift-reset events — already produced (L3/L5/L6); declare the consumer-facing form when
  first wired.
- **E-13 ★ ENGAGE RIDER — the tuning bridge is a consumer-migration site.** `notationtuningbridge`
  (`applyTuningAtNote`/`applyRegionTuning`, the P3 analyzer-root tier) consumes the LEGACY analysis path; when
  the segment-first spine retires at E4 (retirement map R6), the tuning bridge must migrate to the new spine's
  outputs — the same class of item as R2's cadence-detector bridge call-sites, but not yet named in the
  retirement map. **Surface at the engage checkpoint** (add to the R-map at its next natural edit).
- **E-14 ★ ZERO INFORMATION LOSS TO THE END USER (user-stated principle, 2026-07-03).** The future visual
  tool(s) must be ABLE to display **everything we see and infer**: every span family, the full ranked
  alternative lists with weights, confidences and their classes, abstentions and their reasons, provenance and
  denial marks, both axes. Progressive disclosure is a UI freedom; **structural hiding is not** — no inferred
  object may lack a displayable form. This is the display-side mirror of the ratified carried-alternatives
  contract, and it binds every analysis output's data design NOW: if it can't be rendered, it isn't done.
  (T-7/T-8/T-26/T-27 are the principle's first consumers.)

## 3. Relations

- Levers ↔ tools: R-4 ↔ T-20 · R-7 ↔ T-1/T-2 · R-3 ↔ T-3 · VL-F ↔ T-4 · VL-G ↔ T-5/T-14 · VL-D ↔ T-13/T-19 ·
  VL-H ↔ T-12/T-14 · A-8 machinery ↔ T-10.
- The chord track is the natural HOME for T-1/T-2/T-5/T-14 experimentation (analysis-side, not score-mutating —
  consistent with the "no score modification without explicit user action" principle, ARCHITECTURE §2).

## 4. Sweep sources (2026-07-03, second sweep — [reported] level)

- Harmony workstations: Synfire/Harmony Navigator vs Liquid Notes (re-compose.desk.com FAQ;
  https://www.re-compose.com/new-features-in-liquid-notes-make-music-production-more-intelligent-and-better.html) ·
  RapidComposer (https://musicdevelopments.com/) · Mapping Tonal Harmony Pro (https://mdecks.com/mapharmony.phtml) ·
  Opusmodus (https://opusmodus.com/)
- Gap evidence: melody↔harmony relation unserved (KVR forum, https://www.kvraudio.com/forum/viewtopic.php?t=604220) ·
  no-Windows analysis-overlay workbench (ResearchGate,
  https://www.researchgate.net/post/Whats-the-best-software-tool-to-present-musical-analyses) · notation
  proofreading = human services only (https://musicnotationhub.com/sheet-music-services/proofreading/) · SMT
  software list (https://discuss.societymusictheory.org/discussion/514/list-of-music-theory-software-draft.html)
- Research visualizations: MelodyVis (arXiv 2407.05427), MoshViz, Visual Musicology (visual-musicology.com)

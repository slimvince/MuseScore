# The voice-leading axis (axis 2) — architecture and foundation components (design)

> **★ Status: AS-BUILT (VL-A/B/C foundation, 2026-07-03 — `cc_vl_foundation_build_report.md`).** The dormant
> foundation is built, tested, and gate-proven (composing 1083 / notation 53 / snapshots 11 no refresh; gate 53/24/53
> case-identity sets byte-identical on all three presets; dormancy grep-proven; study-parity float-exact on the pinned
> sample). *(★ The gate named in that sentence is the SUPERSEDED batch case-identity stop — a true record of
> what this build was proven against on 2026-07-03, and NOT the criterion a later change is judged by; the
> standing stop is `CLAUDE.md` gate block (A). Corrected in place 2026-08-11, §0's terms bullet carrying the
> full account; the sentence itself is preserved, #12.)* **Two build declarations owed by the design are now closed:** **(§15-2)** the "parallel" interval-preservation
> convention is **SEMITONE-EXACT** — replicated from `voiceleading2.py` `_motion` at source (`parallel` iff both voices
> move the same direction AND the *signed* pitch difference in semitones is preserved: `(pu1−pv1)==(pu0−pv0)`; a
> same-direction move whose semitone interval changes is `similar`), NOT generic-diatonic. **(§5.3)** the feature space
> is the **z-scored concatenation (ABz)** — decided by measurement (`run_vl_feature_space.py`): nearest-centroid in ABz
> reproduces the ratified AB K=4 partition at **ARI 0.791 / accuracy 0.918**, vs two-stage 0.716 and motion-only 0.258
> (raw concatenation rejected a priori for the measured dilution). The shipped reference set (mean/std + 4 z-space
> centroids + the precision-phase floor defaults) is the generated `textureclassifierreference.h`.
>
> **Status: SIGNED (user, 2026-07-03 — asks A1–A8 ratified in full).** Ratification rode one clarification,
> folded into §5.3/§7 before signing: every inference output carries the **full ranked alternative list with
> weights** (zero information loss — the ARCH §2.15 carried-alternatives contract made explicit here); facts
> carry no alternatives by construction, but fact-level choices (the reduction rule) are declared per-query
> parameters recomputable at zero loss from the lossless L1 notes. Next step: the VL-A/B/C dormant-build CC
> instruction, written just-in-time.
>
> **(Original draft banner follows.)** The first design document of the **voice-leading axis** — the
> second, orthogonal analysis dimension confirmed empirically by the idiom-discovery program
> (`cowork_idiom_discovery_findings.md` v2.0: orthogonality formally measured, cross-ARI(voice-leading, harmonic) =
> 0.030 on 1,283 dual-view pieces; study record `cc_vl_idiom_discovery_report.md`, ratified 2026-07-03). Roadmap
> home: `docs/implementation_roadmap.md`, forward-increment step 4 (the discovery half is ✅ done; this document is
> the remaining spec half). Specified by **rule and direction**; numeric calibration is the later precision phase
> (the firewall). Build target: **dormant + byte-identical** — nothing in this design touches the harmonic spine's
> behavior or the corpus gate (Baroque 53 / Jazz 24 / Default 53), by construction. Ratification asks: §16.
>
> **QA record (2026-07-03):** the template's two writing-standard sections (qualified predicates; defined terms /
> plain vocabulary / one-sense-per-word / no shorthand) were run on the **full current text**. Load-bearing facts
> verified at source this session: findings v2.0 + the study report (§2 feature definitions, §3 ablation/confound
> numbers, §4 orthogonality, §6 caveats), ARCHITECTURE §2.15 (span typology, layer taxonomy, admission gates),
> roadmap step 4, the confidence and bounded-context contracts, and the six `voiceLeadingDefined` entries at the
> built catalog (`harmonicvocabulary.cpp` §5.2 block + line-cliché substitution: Prinner, Romanesca, Do-Re-Mi,
> Monte, Fonte, line cliché — Ponte/Quiescenza/lament-variant are declared deferrals, not built).
> **Independent fresh-eyes audit (2026-07-03, user-directed — the spec-polish rigor):** a separate-context
> adversarial audit against the writing standards, all cited sources, the contracts, and the built objects
> returned **24 findings (3 HIGH / 11 MED / 10 LOW)** — all folded into this revision (the HIGHs: the §3
> L3-key-reader contradiction; the fit floor added so off-taxonomy abstention is actually deliverable by the
> §5.3 mechanism; the classification feature space made an explicit at-build measured declaration) — except one
> **rejected with evidence**: the catalog field is `bool voiceLeadingDefined` (`harmonicvocabulary.h`, struct
> declaration); `vlDefined` is its constructor parameter. Verdict quoted: "the document's empirical spine is in
> excellent shape … nothing requires re-measurement or a structural redesign."
>
> *(Per the template convention: arc42 Deployment view and Human-interface design are N/A — a backend analysis
> module, no deployment topology, no UI. Stated once here.)*

## 0. Terminology (read first) — accepted music theory vs. this design's operational terms

Every term is marked **[MT]** (accepted music theory, used in its accepted sense) or **[VL]** (operational, defined
by this design — not standard vocabulary). Where the operational use of an [MT] term differs from the textbook
concept, the difference is stated. Nothing below is used before it is defined here.

**One-sense declarations (the multiple-meaning-words rule):**

- **"voice"** is used in this document ONLY for the **notated voice** — the (staff, voice) line the score writes
  (an L1 fact). In MuseScore's concrete model (user-stated, 2026-07-03): a staff holds one to four engraving
  voices, and a part may hold several staves (piano: two, one per hand). The *inferred* perceptual line is always
  called a **stream**, never a voice.
- **"phrase"** is used ONLY for the accepted **melodic phrase [MT]** (defined below) — which, on this axis, is IN
  scope. The harmonic-grouping unit is always the **punctuation-span** (Layer 6's object,
  `cowork_layer6_grouping_design.md` §0), never "phrase".
- **"bar"** is used ONLY for the metric unit of notation; a threshold is always called a "floor" or a "bound",
  never a "bar". **"measure" / "measured"** is used ONLY as the empirical verb (to quantify by experiment), never
  for the metric unit.
- **"key"** is used ONLY for tonality (the local key Layers 3/5 commit), never in the sense "important".
- **"sequence"** (the harmonic device) does not appear in this document; an ordered series is called a "series".
- **"margin"** is used ONLY for the Class-M best-vs-second-best decision statistic (the confidence contract's
  sense), never in the sense "edge / borderline".

**Project terms used below (cited, not re-defined here):**

- **Dormant** — built and regression-tested but wired into no user-facing path (the harmonic spine's L4/L5/L6
  convention; engagement is a separate, deferred event).
- **Byte-identical / the corpus gate** — the standing regression discipline: after a change, the project's
  hard regression stop reproduces. **★ WHICH STOP THAT IS WAS CORRECTED 2026-08-11** (CC,
  `cc_instruction_return_continuation_11.md` Task 1; `OPEN_ITEMS.md` OI-276 (3)). **THE STOP IS THE
  ROBUST-UNIT ONE — `CLAUDE.md` gate block (A), the granularity-robust union-of-boundaries unit — and it is
  the ONE authority for what this term means here; no criterion is restated in this document (#6, D-431).**
  The batch case-identity gate this bullet formerly named was re-baselined on 2026-07-05 and **SUPERSEDED IN
  WHOLE at R10-b on 2026-07-06**, `CLAUDE.md` block (C) retaining it as historical reference only. **FORMER
  WORDING, preserved (#12):** *"the frozen Bach corpus's BIR case-identity sets (Baroque 53 / Jazz 24 /
  Default 53) reproduce exactly after a change (CLAUDE.md; STATUS.md)."* **Why this correction is the sharp
  one of its row's three:** the stale sentence is not a description of the past, it is an ACCEPTANCE
  CRITERION a future build would try to satisfy — and it cited two governing documents as its authority,
  neither of which has carried it since R10-b.
- **Precision phase / the firewall** — numeric calibration is deferred behind structural design (the roadmap's
  Stage-5 weight fitting); specs are written rule-and-direction first.
- **Census / corpus wave** — corpora enter the project only through the enumerated census and its waves
  (`cowork_score_census.md`; the roadmap's standing re-discovery trigger).
- **CC instruction** — a written dispatch executed by the implementing Claude Code session (the project's
  Cowork-designs / CC-executes split, `COWORK_HANDOFF.md`).

### Accepted music-theory terms [MT]

- **Voice leading [MT].** How simultaneous musical lines move from sonority to sonority — the linear, horizontal
  dimension of part-writing: interval succession within each line and the motion relations between lines. The
  subject of this axis.
- **Motion types [MT] — parallel / similar / contrary / oblique.** The standard counterpoint classification of how
  two voices move between two consecutive time points: **parallel** = same direction, harmonic interval preserved;
  **similar** = same direction, harmonic interval changes; **contrary** = opposite directions; **oblique** = exactly
  one of the two voices moves. (The operational sampling rule that decides "consecutive time points" for real
  scores is defined under motion profile [VL] below.)
  **★ "INTERVAL PRESERVED" IS SEMITONE-EXACT, NOT GENERIC DIATONIC SIZE — CLOSED AT BUILD, 2026-07-03.** Two lines
  count as **parallel** only when they move the same direction AND the SIGNED SEMITONE distance between them is
  unchanged; a same-direction move whose semitone interval changes is **similar**. So a pair moving from a major
  third to a minor third is similar motion, not parallel, although both are thirds on the staff. *Why this reading
  and not the generic-diatonic one:* it was settled by REPLICATION rather than by choice — the convention was read
  off the exploratory study's own motion classifier at source and reproduced exactly in the production
  classification, which is oracle-tested against it, and reproducing the study's features is what this design
  requires of the production implementation. *(This bullet formerly closed: "whether 'interval preserved' is counted
  in semitones or in diatonic generic size is an implementation declaration owed at build — §15-2." That statement
  was true when written and is FALSE at HEAD — the declaration was closed at build, and §15-2 records the closure.
  The former wording is preserved here (#12), and the tracking line in §15 is untouched.)*
- **Texture [MT].** The relationship among the concurrent lines of a passage — standardly: **monophony** (one
  line), **homophony** (one leading line with accompaniment; the lines move as one), **polyphony / counterpoint**
  (several independent lines). Operationally this design classifies texture from measured motion-type rates
  (texture classification [VL] below), which is narrower than the full textbook concept (it does not, for
  example, distinguish monophony as a separate class in v1).
- **Melodic phrase [MT] (in this document: "phrase").** The accepted music-theory phrase: a broadly *melodic /
  linear* unit, essentially monophonic in conception (in homophonic or polyphonic textures it is carried by a
  line), conventionally closed by a cadence or breath/gesture, and — when sung — usually coinciding with a text
  phrase. (Ref: Caplin 1998 for the cadence-defined phrase.) **This axis is the phrase's home** (the L6 §0
  terminology ruling): the harmonic spine's Layer 6 deliberately does *not* segment it. In contrapuntal textures
  phrases are **concurrent, overlapping, and out of phase across voices** (a fugue's staggered subject entries) —
  a per-voice object, not a texture-wide partition.
- **Implied polyphony / compound melody [MT].** A single notated line that projects two or more perceptual lines
  (e.g. a Bach solo-violin or keyboard figuration alternating between registers). The reason stream separation
  [VL] exists as a task.
- **Galant schemata [MT].** The stock phrase-level patterns of eighteenth-century galant style catalogued by
  Gjerdingen (*Music in the Galant Style*, 2007) — Prinner, Romanesca, Monte, Fonte, Ponte, Do-Re-Mi, Quiescenza,
  and kin. Each is defined primarily by a **paired outer-voice scale-degree skeleton** (with a conventional
  harmonic support), i.e. by voice leading — which is why their primary identity belongs to this axis
  (`cowork_idiom_entry_mapping.md`, the voice-leading-defined flag).
- **Line cliché [MT].** A chromatic stepwise line (usually an inner voice) moving against a static harmony
  (e.g. the descending chromatic line over a sustained minor triad). Voice-leading-defined; carried today as a
  Harmonic Vocabulary substitution entry flagged for this axis.
- **Cadence [MT].** As in the harmonic spine (L5 detects; this axis does not re-detect cadences — §3).

### This design's operational terms [VL]

- **The voice-linear view [VL] (component VL-A).** The representation that reorganizes the L1 note model into
  per-voice event series ordered by onset — the linear reading of the same lossless notes. A voice whose events
  are chords is recorded as a **chordal voice** (a fact); any reduction of a chordal voice to a single line for
  feature purposes is a **declared reduction rule** (a named parameter of the view, never silent — §5.1).
- **Stream [VL] (component VL-D).** An *inferred* perceptual line recovered from implied polyphony by stream
  separation. Always marked inferred, with per-note membership confidence; never conflated with a notated voice.
- **Motion profile [VL] (component VL-B).** The voice-pair motion-type rates `[parallel, similar, contrary,
  oblique]` of a span, computed by the study's simultaneity rule: for each concurrent voice pair, sample at the
  merged set of the two voices' note onsets; a voice's pitch at a sample is its most recent onset at-or-before
  that time (piecewise-constant hold); classify the motion type between consecutive samples, dropping samples
  where neither voice moves; aggregate rates over all voice pairs (rates are length-normalized by construction).
- **Interval profile [VL] (component VL-B).** The per-voice melodic-interval statistics of a span: the
  |interval|-in-semitones histogram (bins 0–11, ≥12) plus repeat/step/leap rates (repeat = 0, step = 1–2, leap ≥ 3
  semitones). The pilot's feature, unchanged (`idiom_discovery/parsers/voiceleading.py`, `vl_profile`).
- **Texture classification [VL] (component VL-C).** The assignment of a span to one of the empirically robust
  voice-leading idioms (below), from its motion profile (primary) and interval profile (secondary), with a
  Class-M confidence (`cowork_confidence_contract.md` §2).
- **Voice-leading idiom [VL].** One of the data-derived texture classes of findings v2.0:
  **{contrapuntal part-writing, homophonic-classical (keyboard figuration), homophonic-pianistic
  (romantic/virtuosic), moderate/mixed}** — the axis-2 analogue of the five harmonic idioms. Names are post-hoc
  readings of cluster signatures, provisional in the same way the harmonic idiom names are.
- **Voice-leading-span [VL] (the §2.15 latent span, given its criterion here).** The span one texture
  classification prevails over — a maximal run of the analysed span carrying one voice-leading idiom. This
  document is the criterion's home; ARCHITECTURE §2.15 lists the span as a latent family member.
- **Phrase-span [VL] (component VL-E; design-gated).** A per-voice span holding one melodic phrase [MT]. Phrase-
  spans of *different voices* may overlap and be out of phase by construction; within one voice, consecutive
  phrases are *expected* to tile its line, but strict tiling is not asserted — phrase **elision** (the cadence
  tone of one phrase simultaneously beginning the next, standard theory per the Caplin reference) makes shared
  boundary notes a real case, recorded as a VL-E design question (§15-9), as is the treatment of rests between
  phrases. This is a **per-voice span kind** — deliberately outside the harmonic axis's flat,
  texture-wide span families (§16 ask A5: its admission into the §2.15 typology as a new kind).
- **Axis [project term].** An orthogonal analysis dimension with its own components/layers (ARCHITECTURE §2.15,
  the layer-taxonomy bullet: growth is by axis and by component). Axis 1 = the harmonic spine (L1–L6); axis 2 =
  this design.

## 1. Introduction & purpose

**What this is.** The architecture of the **voice-leading axis** — the second analysis dimension of the composing
module — and the build-level specification of its three **foundation components**: the voice-linear view (VL-A),
the motion & interval profiles (VL-B), and texture classification (VL-C). The axis's further components — stream
separation (VL-D), melodic phrase segmentation (VL-E), voice-leading-schema recognition (VL-F), chord
voicing / arrangement analysis (VL-G), and part-writing checking & suggestion (VL-H) — are **named, scoped, and
staged** here but design-gated: each gets its own
design document (and, where required, its own measurement) before any build (§5.4, §9-D5).

**Why it exists (the problem).** The harmonic spine answers "what are the chords, keys, functions?" It is
structurally blind to the *linear* dimension: how the lines move. That dimension is (a) **a real, independent
organizer of the music** — measured: voice-leading clusters are statistically independent of harmonic-idiom
clusters (cross-ARI 0.030), chorales that scatter across harmonic idioms are 98% voice-leading-tight, and one
harmonic idiom (Steely Dan / Piazzolla / Hiromi) splits into several voice-leading identities; (b) **the home of
real analysis objects that today have no owner** — the melodic phrase [MT], the fugue's overlapping per-voice
phrases, the galant schemata and line cliché (six Harmonic Vocabulary entries carry a voice-leading-defined flag
waiting for this axis), and chord voicing/arrangement (excluded from the harmonic dictionary's scope); and (c)
**the named path to measured harmonic residuals** — the non-chord-tone filter, the field's lever for counterpoint
accuracy, is an L4 (harmonic-emission) concern *informed by* this axis; the dormant full-spine measurement
(`cc_e0doubleprime_report.md`) attributed ≈45% of the exact-match cap to seventh/extension over-emission
dominated by non-chord tones read as chord extensions.

**Scope — in:** the axis decomposition and its cross-axis contract; build-level rules for VL-A/VL-B/VL-C; the
staging and claims of VL-D/E/F/G/H. **Scope — out:** any harmonic inference change (the non-chord-tone filter
remains L4's, not built now); any production wiring (dormant build only); numeric thresholds and weights
(precision-phase); the deferred components' internal designs (their own documents).

**Status:** design, for user sign-off. Nothing here is built; no CC instruction exists yet (instructions are
written just-in-time after ratification).

## 2. Constraints

The axis obeys the same architecture the harmonic spine obeys:

- **Forward-only analysis.** Inference flows forward within the axis; cross-axis reads obey the acyclicity rule of
  §9-D6. No backward inference edge anywhere; a sanctioned exception would follow §2.14's surfaced/measured/gated
  protocol.
- **Universality in the fact layers; style only in calibration** (ARCHITECTURE §2.15). VL-A and VL-B are
  style-agnostic, lossless-derived **facts** and carry no confidence. Judgment enters only at VL-C and later
  components.
- **Any notated score, any size, any style** (the product constraint the harmonic spine carries): the components
  run on whatever notated score the user opens; style enters only through calibration parameters (the VL-C
  reference set), never through structure.
- **The bounded-context contract** (`cowork_bounded_context_design.md`): every component analyses the selection,
  requests append-only extension from L1 with a stop condition and hard bound when its reasoning needs more, and
  carries the denial/truncation provenance honestly (§8).
- **The confidence contract** (`cowork_confidence_contract.md`): every published confidence is [0,1],
  class-declared, attached to a named decision; no new cross-layer comparison frame exists until declared in the
  contract's §4 (none is declared by this design — §8).
- **Dormant + byte-identical.** The build changes no harmonic-spine behavior; the corpus gate is untouched by
  construction; dormancy is proven by source search, as for L4/L5/L6. *(★ The parenthetical formerly here
  named the batch `53/24/53` case-identity sets, which R10-b superseded in whole on 2026-07-06; the standing
  stop is `CLAUDE.md` gate block (A) and §0's terms bullet carries the account. Corrected 2026-08-11,
  `OPEN_ITEMS.md` OI-276 (3); the former parenthetical is preserved there, #12.)*
- **Verifiability with honest marks.** What lacks ground truth is built (if at all) with an alternative-confidence
  path and an **empirically-unvalidated** mark, never silently trusted (ARCHITECTURE §2.15; applied per component
  in §10).
- **Total unification.** The axis reuses the shared primitives (the one L1 note model; the L1.5 phrase-boundary
  primitive as evidence for VL-E; the discovery pipeline as validation harness); every build increment reports
  reuse-vs-new and what retires.
- **Knowledge-based coding.** Every inference component's build is gated on the measurement that earns its design
  (the VL-C per-span question has a named exploratory study — §5.3, §15-1).

## 3. Context & scope (external view)

**Imports / dependencies.**
- **The L1 note model** (axis-neutral, shared): notes with onset/duration, pitch + notated spelling, metric
  weight, and (staff, voice) — everything VL-A needs, already carried losslessly. **The axis adds no second note
  model** (total unification).
- **The L1.5 phrase-boundary primitive** (its graded profile + per-part cue/scope provenance; evidence for VL-E
  when designed): the per-part cues (breath, caesura, fermata) are natural per-voice phrase evidence; VL-E
  consumes the existing primitive rather than re-detecting the cues.
- **The committed L3 key** (VL-F and VL-H, when designed): schema recognition and tendency-tone rules need scale
  degrees, which need the local key. This is the axis's only planned *kind* of harmonic-inference read (§9-D6
  for why it is safe).
- **NOT imported:** L2 slices (the axis's sampling is by voice-pair onsets, not verticalities); L4/L5/L6 outputs
  (v1 reads nothing from them).

**Exports / public API (design-level).**
- VL-A: the per-voice event series (with chordal-voice facts and any declared reduction rule named per query).
- VL-B: motion profile + interval profile over a requested span (pure functions of VL-A).
- VL-C: voice-leading-spans with an idiom classification and a Class-M confidence.
- Later components (design-gated): streams (VL-D), per-voice phrase-spans (VL-E), recognized voice-leading
  schemata (VL-F), voicing/arrangement descriptors (VL-G).

**Consumers (who reads the axis, and for what).**
1. **The 2-D style structure.** The full style structure is **≥ 2-D**: (harmonic idiom) ⟂ (voice-leading idiom)
   + mode + chromaticism (findings v2.0 — "at least": further axes are possible). VL-C supplies the second
   coordinate — eventually a calibration context for the
   judgment layers' priors (style lives only in calibration), and an input to the roadmap's idiom auto-detection
   step.
2. **The future L4 non-chord-tone filter** (harmonic axis; not built now): consumes VL-A/VL-B **facts** (lines and
   motion), not VL judgments — see §9-D6.
3. **The Harmonic Vocabulary / recognition consumer:** VL-F claims the six entries carrying the
   voice-leading-defined flag — verified at the built catalog (`harmonicvocabulary.cpp`, the §5.2 galant-schemata
   block + the line-cliché substitution): **Prinner, Romanesca, Do-Re-Mi, Monte, Fonte, line cliché** — whose
   harmonic-idiom tags are declared placeholders. (Ponte, Quiescenza, and the lament variant are declared catalog
   deferrals, not built; they join the claim if and when they enter the catalog — a per-item deferral-vs-gap
   ruling on the vocabulary side is owed per the gap-analysis rider.)
4. **The part-writing advisory (VL-H, design-gated):** rule checking + suggestion (parallel perfect intervals,
   awkward vocal leaps, tendency-tone resolution) consuming VL-B's per-sample motion events and per-voice
   interval facts — the axis's product-advisory consumer (§5.4).
5. **The user-facing annotation** (eventually): texture labels, phrases, schema names — engagement out of scope,
   like the rest of the dormant stack.

**Implementation & test locator:** deferred — no component is built; added at each component's build per the
template convention.

## 4. Solution strategy

**Mirror the harmonic spine's discipline on the linear dimension, and build only what the evidence has already
earned.** The spine's shape — lossless facts → mechanical derived views → judgment layers with declared confidence
— transfers unchanged: VL-A is the axis's "L1 view", VL-B its "L1.5", VL-C its first inference layer. Three
empirical results fix the design's priorities: **(1) motion type leads** — voice-pair motion-type rates alone
recover the texture structure (ARI 0.37–0.46) where interval profiles alone do not (≤0.20), so the primary
discriminator is *how voices move together*, with the interval profile as a secondary melodic-complexity
descriptor; **(2) texture is the organizer** — the axis's natural first inference target is the texture
classification (confounds ruled out: voice-count ARI 0.034–0.046, source 0.07–0.11); **(3) the axis works on
notated voices without stream separation** — the study discriminated textures from notated (staff, voice) lines
directly, so VL-D is an enrichment for per-voice detail in keyboard textures, not a prerequisite. Everything the
evidence has *not* yet earned (per-span texture granularity, phrase segmentation, schema matching) is staged
behind its own measurement or design gate.

## 5. Building-block view

The components, in dependency order. **Specified for build now (dormant): VL-A, VL-B, VL-C** — *this document is
their design document*: the ratified study supplies their complete empirical footing, so their build-level rules
are written here (§5.1–§5.3). **Named + staged, design-gated: VL-D, VL-E, VL-F, VL-G, VL-H** — named only,
because their footing (ground truth, measurements, algorithm selection) does not exist yet; each gets its own
design document written just-in-time (§5.4), where its algorithm is chosen from the §14 candidates against the
then-current evidence.

### 5.1 VL-A — the voice-linear view (representation; facts)

**Owns:** the *per-voice linear reorganization* contribution to the axis — nothing else. It reorders the same L1
notes by (staff, voice) and onset; it decides nothing.

Rules:
- **Lossless and axis-neutral — a partition, not a detection:** every L1 note appears in **exactly one** voice's
  series (the notated (staff, voice) fact decides membership; nothing is inferred); tie chains are already
  resolved by L1 (the tie-resolved note model, `cowork_layer1_note_model_design.md` — a tied chain is one
  sounding event) and the view inherits that resolution; nothing is dropped or merged. Round-trip (view → notes)
  reproduces the L1 content of the span. A note
  serving two perceptual lines (a compound-melody pivot, a voice crossing) is a **stream**-tier phenomenon —
  whether one note may belong to two streams is a recorded VL-D design question (§15-8), never a VL-A one.
- **Chordal voices are a recorded fact,** not an error: a voice whose events carry multiple simultaneous pitches
  (keyboard writing) is marked chordal per event.
- **Reduction is declared, uniform, and per-query — never silent, never per-source.** A consumer needing one line
  from a chordal voice names a reduction rule (v1 provides exactly one: **top-note** — the highest sounding pitch
  per event, the study's curated-branch rule). The rule is a parameter of the *query*, carried in the output's
  provenance. This single uniform rule is what retires the study's per-source explosion asymmetry (its View-A
  caveat) when the production extractor is built.
- No confidence (facts carry none).

### 5.2 VL-B — motion & interval profiles (derived views; facts)

**Owns:** the *mechanical voice-leading statistics* contribution — deterministic functions of VL-A over a
requested span, exactly as the ratified study computed them (§0: motion profile, interval profile).

Rules:
- **Motion profile** per the simultaneity rule (§0), aggregated over all concurrent voice pairs of the span;
  **interval profile** per voice, aggregable over voices. Both length-normalized rates.
- **The per-sample motion-event series is part of the export, not only the rates.** The profile is an aggregation
  of classified motion events (voice pair, sample time, motion type, the two harmonic intervals before/after);
  the event series itself is a fact and is exposed. The rates are all VL-C needs; the events are what a future
  part-writing checker needs (a parallel fifth/octave is parallel motion at a perfect harmonic interval *at a
  specific event* — VL-H, §5.4) — cheap to expose at build, structural to retrofit.
- **Deterministic, no tunable thresholds, no judgment, no confidence** (the fixed step/leap cut and histogram
  binning are study-pinned feature definitions, part of what "the same feature" means — not calibration). The
  only declarations owed at build: the
  interval-preservation convention for "parallel" (semitone vs generic — §15-2) and the treatment of chordal
  voices (which declared reduction the profile query uses; default top-note, per §5.1). **★ AS-BUILT: both closed —
  (a) SEMITONE-EXACT parallel (`(pu1−pv1)==(pu0−pv0)` on signed MIDI pitches; §15-2 CLOSED, verified at
  `voiceleading2.py` `_motion`); (b) default TOP-NOTE reduction. The profile-eligibility filter is the verified
  per-(staff,voice) line-view filter `plays && visible && staffEligible` (the `phraseboundaryview.cpp` precedent —
  the instruction's 2-flag parenthetical reconciled to the verified 3-flag existing-derived-view filter).**
- **Parity duty:** the production implementation must reproduce the study pipeline's features
  (`idiom_discovery/parsers/voiceleading.py` `vl_profile`, `voiceleading2.py` View B) on a pinned sample of
  study pieces within declared tolerance — the axis-2 analogue of the music21↔L1/L2 neutral-extractor
  cross-check (§10).

### 5.3 VL-C — texture classification (inference; the first judgment component)

**Owns:** the *measured-motion evidence* contribution to the question "what texture is this span?" — and only
that. It does not own era, composer, instrument, or genre claims (era correlates ride the interval profile and
are declared interpretation, not decisions); it does not own any harmonic decision.

Rules and direction (numeric calibration precision-phase):
- **Input:** the span's motion profile (primary) + interval profile (secondary), per the measured hierarchy (§4).
- **Output — the committed class PLUS the full ranked alternative list (zero information loss; ratification
  clarification, user 2026-07-03):** the span's voice-leading idiom from the four-class taxonomy (§0) is the
  TOP of a **fully ranked list of ALL class fits, each carried with its weight** — nothing below the top is
  discarded; a downstream consumer (and Stage-5 calibration) sees everything VL-C saw. This is the ARCH §2.15
  minimality-plus-maximal-information contract applied here (the same carried-alternatives discipline as L4's
  ranked chord readings). The **Class-M confidence** on the named decision *texture-of-span* is squashed to
  [0,1] per the contract (the margin between the best and second-best class fits, where "fit" is distance to a
  reference centroid under a distance metric that is a declared build-time choice recorded with the reference
  set's provenance; the squash-map shape is declared in the confidence contract with the build — §10 doc-sync).
- **v1 granularity: the whole analysed selection is ONE span.** The study's evidence is per-piece; whether
  windowed motion profiles recover *within-piece* texture changes (the per-span refinement that would make
  voice-leading-spans plural within a selection) is **unmeasured** — so, per the knowledge-based-coding rule, v1
  classifies the selection as one voice-leading-span, and the per-span refinement is gated on a named exploratory
  measurement (§15-1). The output *type* is already a series of voice-leading-spans, so the refinement changes
  cardinality, not shape.
- **Class assignment is nearest-centroid against fitted references, in a feature space that is a STRUCTURAL
  declaration, not a tunable.** The study's ablation forces the care: raw concatenation of the two views
  measurably dilutes the motion signal (the 16 interval dimensions outvote the 4 motion dimensions), yet the
  ratified four-class table was fitted on the concatenated space. So the space is decided **at build by
  measurement** among three named candidates — motion-profile-only, two-stage (motion space for the
  contrapuntal/homophonic split, interval space for the melodic-complexity refinement), and z-scored
  concatenation (raw concatenation is rejected, measured dilution) — the criterion being the §10(b) requirement:
  reproduce the ratified cluster memberships within declared tolerance. **★ AS-BUILT: the winner is the z-scored
  concatenation (ABz)** — measured by `run_vl_feature_space.py` (nearest-centroid reproduction of the ratified AB K=4
  partition, cap=80/source, seed 0): **ABz ARI 0.791 / accuracy 0.918**, two-stage 0.716, motion-only 0.258 (raw
  concatenation rejected a priori). The declared tolerance was met with margin (ABz reproduces > 0.90 of the
  memberships, decisively ahead of the alternatives), so no §10(b) STOP. The reference set (mean/std over the fit set
  + the 4 z-space centroids + the precision-phase floor defaults) is the generated `textureclassifierreference.h` with
  full provenance (run, corpus state, K, seed, sklearn version) — a shipped parameter, refit under the discovery
  protocol at corpus waves, like the idiom taxonomy itself.
- **Honest marks — the three declared floors (named once here, used by these names everywhere):** the
  **evidential floor** (minimum motion-sample count for a profile to support a decision), the **margin floor**
  (minimum best-vs-second-best margin), and the **fit floor** (minimum absolute fit of the best class).
  Abstention (uniform semantics, contract U5) fires when the margin is below the margin floor **or** the best fit
  is below the fit floor — the second clause is what makes a span resembling *no* reference class abstain rather
  than be forced to its nearest class (a relative margin alone cannot deliver that). All three constants are
  precision-phase. Coverage marks per §10 (e.g. a single-voice selection has no voice pairs — the motion profile
  is undefined and VL-C abstains with a *no-pair* reason rather than classifying on the interval profile alone,
  v1).

### 5.4 The staged components (named, scoped, design-gated — each gets its own design doc before build)

- **VL-D — stream separation (inference).** Recover streams from implied polyphony / compound melody, so keyboard
  and solo-string textures get per-line detail. Methods to lean on: Chew & Wu contig-mapping, VISA, Temperley's
  streams, the IJCAI-2023 link-prediction formulation, the `partitura`/`music21` voice tools
  (`cowork_polyphony_phrase_harmony_research.md` §2/§6). **Verifiability is strong on the merged-voices proxy:**
  hide notated voice assignments and score recovery against them — the literature's standard evaluation,
  available on our own corpora at zero annotation cost. The implied-polyphony *target* itself (one notated line
  projecting several streams) has no notated ground truth — that half carries the empirically-unvalidated mark
  until a labeled bed exists (a census item, §15-4). Output: streams with per-note membership confidence
  (Class M), always marked inferred (§0 one-sense rule). Not a prerequisite for VL-A/B/C (§4).
- **VL-E — melodic phrase segmentation (inference).** Per-voice (and, post-VL-D, per-stream) segmentation into
  phrase-spans — overlapping and out of phase across voices by construction (the fugue case). Evidence: the
  line's own grouping cues (GTTM grouping preference rules; the melodic-segmentation literature) + the L1.5
  phrase-boundary primitive's per-part cues (breath/caesura/fermata with cue+scope provenance — reused, not
  re-detected). Ground
  truth: onboarding a phrase-annotated melodic corpus is a **census item** (standing census rule — no corpus
  enters outside the census); the 2026-07-03 sweep named the standard candidate (the Essen Folksong Collection,
  ~6,236 songs with expert phrase-boundary marks — research doc §6b; monophonic-folk coverage caveat). VL-E's
  build is gated on that footing or carries the empirically-unvalidated mark.
- **VL-F — voice-leading-schema recognition (inference).** Recognize the voice-leading-defined patterns — the six
  flagged Harmonic Vocabulary entries (verified at the built catalog: **Prinner, Romanesca, Do-Re-Mi, Monte,
  Fonte, line cliché**) — from their defining feature: outer-voice/inner-voice scale-degree
  skeletons under a conventional harmonic support. Consumes VL-A lines (+ VL-D streams where needed) and the
  committed L3 key (the scale-degree frame); its recognition output's hosting (alongside the harmonic
  progression-schema-spans in L6, or axis-locally) is a decision FOR its design doc, not made here. **This is the
  component that discharges the mapping's "the future layer claims them" flag** — until it exists, the entries'
  harmonic-idiom tags remain the declared placeholders they are today. **Footing found (2026-07-03 sweep,
  research doc §6b):** an expert schema-annotation dataset exists for the Mozart sonatas (ISMIR 2020; 244 at
  the paper snapshot, **273 at the Wave-2 pin — ONBOARDED 2026-07-03**, `cc_corpus_wave2_report.md` §1; the bed
  ships its own self-contained score bundle — same 54 movements as the DCML sonatas, distinct encoding), plus
  a published method line (skipgram candidate enumeration + feature classifier) whose measured lessons — extreme
  candidate imbalance; structural-note status is relational, not local; rejection usually means "a better
  explanation of the context exists" — are design input for VL-F's doc.
- **VL-G — chord voicing / arrangement analysis.** Named in ARCHITECTURE §2.15 as living on this axis, and the
  dictionary's declared exclusion (upper-structure / voicing substitution, dictionary §5.3) waits here. Scoped
  only as a claim; no design.
- **VL-H — part-writing checking & suggestion (advisory; user-named 2026-07-03).** Check and suggest voice
  leading against the contrapuntal and vocal-writing rules: parallel perfect fifths/octaves and kin (detectable
  directly on VL-B's per-sample motion events — parallel motion at a perfect harmonic interval), awkward melodic
  leaps for singers (tritone and other hard-to-pitch intervals — per-voice interval facts), and tendency-tone
  resolution (leading tone resolves up, chordal seventh down — needs scale degrees, hence the committed L3 key, a
  D6-checked cross-axis read like VL-F's). Precedent: Contrapunctus ships Fux species-counterpoint checking
  (`cowork_polyphony_phrase_harmony_research.md` §3); the MuseScore plugin ecosystem carries parallel-interval
  checkers (§6b) — **read as demand evidence, not as a quality bar** (user, 2026-07-03: the plugins cover only a
  few of the contrapuntal rules; the theory itself is settled and fully specifiable, so VL-H's design target is
  comprehensive rule coverage from the theory, not parity with existing plugins). **This is the axis's
  product-advisory consumer — advice
  generation, not analysis — and a distinct output kind**, so it is a claim with an owner, design-gated like the
  rest; its rule set, severity model, and how suggestions surface in the composing workflow are its design doc's
  questions. It consumes VL-A/B facts (and VL-D streams, when built, for implied-polyphony textures); it decides
  nothing upstream of itself.

## 6. Runtime view (scenarios)

*(Illustrative, not limiting: per the template, this section shows the rules' behavior on the main flow plus the
important edge cases — it is not an enumeration of supported inputs. The components run on **any** notated score
(the any-score/any-style constraint, §2); what IS a closed enumeration is VL-C's four-class taxonomy, which is
data-derived like the five harmonic idioms, handles off-taxonomy spans by the fit-floor abstention (§5.3 — a
span resembling no reference class abstains rather than being forced to its nearest), and is revised only by a
ratified taxonomy-revision event riding the idiom re-discovery waves.)*

1. **Chorale (four notated voices).** VL-A yields four monophonic series; VL-B's motion profile is
   contrary/similar-elevated with low oblique and ~64/21 step/leap rates (the full-coverage measurement; pilot
   65/21); VL-C
   classifies *contrapuntal part-writing* (the signature sits deep in that class's measured profile — the
   margin is expected well above the margin floor). No reduction rule fires (no chordal voices).
2. **Classical keyboard sonata (two staves, chordal left hand).** VL-A records chordal voices; the profile query
   applies the declared top-note reduction; VL-B shows oblique-dominant motion; VL-C classifies
   *homophonic-classical*. Per-line detail (the Alberti bass as a compound line) would need VL-D — v1 does not
   pretend to have it: the chordal-voice fact + reduction provenance say exactly what the classification was
   computed on.
3. **Fugue.** v1: VL-A/B/C see independent notated voices and classify *contrapuntal part-writing*. The subject
   entries and their overlapping per-voice phrases are VL-E territory (staged); nothing in v1 claims them.
4. **Bounded selection.** A user selects eight bars mid-movement. VL-A serves the loaded span (the L1 selection
   machinery, shared); VL-B computes profiles over the selection; VL-C classifies. If the selection is a short
   fragment whose profile rests on fewer samples than the evidential floor, the §8 extension cue fires (or,
   denied, the output abstains with truncation provenance).

## 7. Data design

Plain-data, test-constructible (the L6 build convention):

- **VoiceLine** — voice identity (staff, voice), ordered events (onset, duration, pitches, spelling, chordal
  flag, and the L1 eligibility flags), losslessly derived from L1. Metric weight is NOT copied into the event:
  it stays with the shared metric-weight machinery (`scoreharvest`) and is read on demand by any consumer that
  needs it (total unification — no second store of a derived quantity; §2 amendment at signing, 2026-07-03).
- **MotionProfile** — the four rates + sample count + the voice-pair inventory it aggregated + the reduction rule
  used (provenance).
- **IntervalProfile** — histogram bins + repeat/step/leap rates + note count, per voice or aggregated.
- **VoiceLeadingSpan** — range (ticks), the committed idiom class + the **full ranked list of all class fits
  with their weights** (the carried alternatives — §5.3), Class-M confidence [0,1], abstention/coverage marks,
  truncation provenance (`clipped-by-selection-edge` / `cue-denied` where applicable), reference-set provenance.
- *(Design-gated types sketched, not fixed: Stream + membership confidences; PhraseSpan per voice; SchemaMatch.)*

Ownership/lifetime: computed per analysis run over the selection, like every other layer output; nothing persists
in the score.

## 8. Crosscutting concepts

- **Bounded context.** VL-A is a *view* over the loaded span (L1 owns loading). VL-B computes over what is loaded.
  **VL-C's discovery rule:** when the selection's profile rests on fewer samples than the evidential floor AND
  the classification margin is below the margin floor (§5.3's floors, reused — one set of constants), VL-C
  requests extension (direction: both — later first, earlier only if the stop condition is still unmet;
  increment: bars — the smallest span that adds enough new motion samples to move a rate statistic; stop
  condition: the classification and its margin stop changing under further context — the *direct* convergence
  check of the contract's item 6, no domain proxy needed at this scale; hard bound: a settings cap). Denied or at
  score boundary: proceed truncated with item-10 provenance. A classification whose margin already clears the
  margin floor requests nothing (the decision-relevance sharpening, `cowork_bounded_context_design.md` §5, the
  L4 role).
- **Confidence.** Exactly one published confidence in v1: *texture-of-span*, Class M, squashed. **No new §4
  comparison frame is declared** — nothing compares a voice-leading confidence against a harmonic one; any future
  wiring (e.g. VL-informed non-chord-tone evidence, a schema-recognition prior) must add its frame row to the
  contract before build (contract §4's standing requirement).
- **Determinism.** VL-A/B are pure functions; VL-C is deterministic given its fitted reference set (a shipped
  parameter, seeded/fitted offline under the discovery protocol — no run-time stochasticity).
- **Coverage declaration (honest, structural).** The axis analyses **notated music only** — lead-sheet sources
  carry no voices, so the voice-leading coordinate of the 2-D style structure is simply *undefined* for them
  (undefined, not zero, in every consumer). This is a representational fact, not a corpus accident.
- **Style discipline.** The idiom taxonomy and reference centroids are data-derived shipped parameters
  (calibration); VL-A/B carry no style anywhere (universality).

## 9. Architecture decisions (alternatives weighed)

- **D1 — an axis, not a seventh spine layer.** The three co-equal admission gates (ARCHITECTURE §2.15): **(1)
  separation of concerns** — linear structure is a distinct responsibility no spine layer may absorb (L6 §2
  explicitly excludes it); **(2) verifiability** — VL-B is fact (oracle by construction), VL-C validates under the
  discovery protocol + declared lenses, VL-D against notated voices, VL-E/F against footing named-or-marked
  (§10); **(3) proportionality** — the axis buys the second style coordinate (measured orthogonal, hence
  non-redundant information by construction), the owner for phrase/schemata/voicing objects that are otherwise
  homeless, and the evidence base for the sized L4 non-chord-tone lever (the §1 ≈45% attribution).
  *Alternative rejected:* folding motion features into L1.5 as "just another derived view" — it puts judgment
  (texture, phrases) with no home and mixes axis-2 concerns into the harmonic spine's half-tier.
- **D2 — motion-type-led features.** Measured (§4): the ablation is decisive, and the motion view is the
  extraction-robust one (it never explodes chords; it grouped exploded chamber corpora with the chorales, ruling
  out an encoding artifact). *Alternative rejected:* interval-profile-led (the pilot's view) — weaker (≤0.20) and
  partly a chordal-density artifact by the study's own caveat.
- **D3 — two-tier voice model: notated voice = fact; stream = inference.** Never conflated; enforced by the §0
  one-sense rule and the type system (VoiceLine vs Stream). *Alternative rejected:* a single "voice" concept with
  a quality flag — exactly the silent fact/judgment mixing the universality principle forbids.
- **D4 — texture classification is v1's only judgment, at whole-selection granularity.** The evidence is
  per-piece; a per-span claim would be assumption-based code. The refinement is a named cheap measurement first
  (§15-1). *Alternative rejected:* shipping windowed per-span classification now — knowledge-based-coding
  violation.
- **D5 — staged components behind design gates.** VL-D/E/F/G/H are claims with owners, not builds; each clears its
  own design + footing before an instruction exists. This is the proportionality gate applied *inside* the axis —
  no slot-filling (the Contrapunctus reminder). *Alternative rejected:* one monolithic axis build.
- **D6 — the cross-axis dependency rule (acyclicity by declaration).** Cross-axis reads are admissible only where
  the combined two-axis dependency graph stays acyclic, checked at each wiring: (a) harmonic layers may consume
  axis-2 **facts** (VL-A/B, L1-derived only) freely — e.g. the future L4 non-chord-tone filter — because facts
  depend on no harmonic inference; (b) an axis-2 component may consume a **committed harmonic output** (VL-F
  reads L3's key) provided nothing that harmonic layer depends on, directly or transitively, consumes that
  axis-2 component. VL-F→L3 is safe (L3 consumes no axis-2 output; the planned L4 filter consumes only VL-A/B,
  which don't depend on VL-F). Each future wiring re-states this check in its instruction. *Alternative
  rejected:* a blanket "axis 2 reads nothing harmonic" — it would make schema recognition impossible for no
  structural gain.
- **D7 — reuse the discovery pipeline as the validation harness** (total unification): the study's extractors and
  protocol (multi-seed stability, cap-robustness, confound gate) are the fitting/validation tooling for VL-C's
  reference set, not a parallel new rig.

## 10. Quality & testing

- **VL-A:** unit tests — losslessness round-trip, tie handling mirrors L1, chordal-voice marking, reduction-rule
  provenance; every branch covered (the full-coverage standing objective applies from birth).
- **VL-B:** the motion classification is pure arithmetic — hand-built two-voice fixtures give an oracle by
  construction (each motion type, holds, both-static drops, chordal-voice reduction); plus the **study-parity
  check**: reproduce the Python pipeline's profiles on a pinned sample of study pieces within declared tolerance
  (the neutral-extractor cross-check pattern).
- **VL-C:** (a) fixture tests — synthetic profiles at and away from the reference centroids, margin/abstention
  behavior, no-pair abstention; (b) **corpus validation under the discovery protocol** — classification of the
  study corpus reproduces the ratified cluster memberships within declared tolerance, confound gate re-run (the
  lens maps stay post-hoc interpretation, never fit input); (c) the honest limits: per-piece texture ground truth
  does not exist in-corpus — the lens maps are per-source and approximate at the category boundaries (the
  study's declared caveat) — so VL-C carries **empirically-unvalidated at per-piece granularity** until a
  labeled bed exists (a census question, standing rule).
- **Dormancy + gate:** no harmonic-spine source is touched; dormancy grep-proven; the corpus gate reproduced
  byte-identically as the no-contamination proof — the same acceptance shape as every dormant build. *(★ The
  parenthetical formerly here named the batch `53/24/53` case-identity sets. As a record of what THIS build
  was proven against on 2026-07-03 that was true; as a statement of the gate a later change reproduces it is
  not, R10-b having superseded that stop in whole on 2026-07-06. The standing stop is `CLAUDE.md` gate block
  (A) and §0's terms bullet carries the account. Corrected 2026-08-11, `OPEN_ITEMS.md` OI-276 (3); the former
  parenthetical is preserved there, #12.)*
- **Documentation sync:** ARCHITECTURE §2.15 (the voice-leading-span criterion + the axis status), the roadmap
  step-4 status, **`cowork_confidence_contract.md`** (a §3 per-layer-inventory row for *texture-of-span* + the R5
  squash-map shape declaration — required before the boundary confidence exists), and this document flip to
  as-built with the build — one increment, per the standing rule.

## 11. Risks & technical debt

- **Ground-truth scarcity** for texture (per-piece), phrases, and schemata — the axis's inference components lean
  on the verifiability contract's alternative-confidence path more than the harmonic spine did. Mitigation: the
  census items (§15-4), the hide-notated-voices oracle for VL-D, and honest marks throughout.
- **Reduction-rule sensitivity.** Motion profiles of chordal textures depend on the declared reduction; the
  curated-arrangement study branch was uniformly oblique-dominant partly *because* of top-note reduction (the
  study's caveat). The uniform declared rule + provenance makes this inspectable, not invisible; alternative
  reductions are a v-next comparison (§15-3).
- **The interval profile's era signal is partly an artifact** (chordal-density/explosion — study caveat). VL-C's
  secondary use of it inherits the caveat; the primary discriminator is deliberately the motion profile.
- **Single-voice and sparse textures:** no voice pairs → no motion profile → v1 abstention. A single-line
  selection is a real use case (a melody); serving it belongs to VL-D/E territory (streams, phrases), not to a
  degraded v1 guess.
- **Scope-creep risk:** the axis names many future objects (phrases, schemata, voicing). The D5 design gates are
  the guard — nothing builds without its own doc + footing.

## 12. Glossary — see §0

(All terms defined or cited in §0; no separate glossary is maintained, the L6 convention.)

## 13. Background

The axis was **predicted** (chorale "Baroque-ness" lives in voice-leading, not chords — the v1/v1.1 finding that
chorales refuse to form a harmonic idiom), **piloted** (2026-06-30: chorale-vs-piano ARI 0.683 on the interval
view; pilot-number note: 0.595 under the study machine's sklearn, feature-identical — KMeans-init drift only, and
the split strengthens to 0.821 at full coverage), and **confirmed + measured** by the axis-2 study (2026-07-03,
ratified: 2,102 pieces / 45 note-level sources; texture-organized; motion-type-led; orthogonality cross-ARI
0.030). It replaces nothing — it is the first construction on a dimension the architecture reserved (ARCHITECTURE
§2.15 named the axis, the voice-leading-span, and the melodic-phrase/voicing homes before this design existed).

## 14. Related work & external sources

**Borrowed / built on:** the motion-type and interval feature definitions and the texture taxonomy
(`cc_vl_idiom_discovery_report.md`, pipeline `idiom_discovery/parsers/voiceleading.py` + `voiceleading2.py`); the
discovery protocol (multi-seed stability, cap-robustness, confound gate — `cowork_idiom_discovery_design.md`);
the 2026-07-03 targeted sweep's verified finds (research doc §6b): the DCML schema-annotation dataset + skipgram
recognition line (VL-F), the per-bar Mozart texture annotations + descriptor baselines (VL-C validation, §15-1),
voice-separation SOTA/tooling updates (Foscarin et al. 2024; `partitura`), Essen phrase-boundary ground truth
(VL-E), and the music21/MuseScore-plugin part-writing-checking precedents (VL-H);
Gjerdingen, *Music in the Galant Style* (2007) — the schemata VL-F claims; Caplin, *Classical Form* (1998) — the
cadence-defined phrase; GTTM (Lerdahl & Jackendoff 1983) grouping preference rules — VL-E evidence; the voice-
separation literature for VL-D: Chew & Wu contig-mapping (2005), VISA (ISMIR 2007), Temperley "Voice and Stream"
(2008), Voice Separation as Link Prediction (IJCAI 2023, arXiv 2304.14848), `partitura`/`music21` voice tools;
the melodic segmenter (arXiv 1811.05688). Full citations and confidence marks:
`cowork_polyphony_phrase_harmony_research.md` §7.

**Considered and discarded/deferred:** interval-profile-led features (rejected — §9-D2); folding the axis into
L1.5 (rejected — §9-D1); per-span texture now (deferred behind measurement — §9-D4); chordify-based extraction
(the study used true note-level per notated (staff,voice) — chordify is voicing-noisy and slow, retained only
where the harmonic study needed lead-sheet-less sources).

**Corpora:** the study's 45 note-level sources (DCML/DLC `notes/`, music21 chorales, the 47 curated arrangements)
— research-tier, per the census/registry discipline; the frozen gate corpus is untouched by this axis.

## 15. Open items & deferred refinements

1. **The per-span texture measurement (gates the §5.3 refinement).** Exploratory, read-only: windowed motion
   profiles over pieces with known internal texture changes — does the window statistic recover the change points?
   Decides whether voice-leading-spans become plural within a selection, and at what window unit. Written
   just-in-time as a CC instruction when it is the next dispatch. **The 2026-07-03 sweep found a ready reference
   for it:** the per-bar texture annotations on the DCML Mozart sonatas (§15-4 candidate) provide exactly the
   within-piece change points this measurement needs, on scores already in our clones.
2. **The "parallel" interval-preservation convention** (semitone-exact vs generic-diatonic) — ✅ **CLOSED at build
   (AS-BUILT, 2026-07-03): SEMITONE-EXACT.** Verified at `voiceleading2.py` `_motion`: `parallel` iff both voices
   move the same direction AND `(pu1−pv1)==(pu0−pv0)` on signed MIDI pitches (a same-direction move whose semitone
   interval changes is `similar`). Replicated exactly in `voiceleadingprofiles.cpp classifyMotion` (oracle-tested).
3. **Alternative declared reductions** for chordal voices (bass-note, per-stream post-VL-D) — comparison deferred
   until a consumer needs one; top-note is the single v1 rule.
4. **Census items — ★ THREE OF FOUR ONBOARDED at corpus Wave 2 (2026-07-03, `cc_corpus_wave2_report.md`;
   research-tier, hash-pin-only, held-out, under `corpora/annot/`):** the phrase-boundary bed (VL-E — the
   **Essen** CCARH kern edition, pin `2d0ca75e`: 8,473 tunes, europa 6,213, 100% phrase-marked; monophonic-folk
   coverage caveat); the texture-labeled bed (VL-C validation — the ISMIR-2022 per-bar annotations, pin
   `3dce4ab8`: 1,164 bar labels keyed (K-id, mn) directly to our DCML Mozart clone; also the §15-1 reference);
   the schemata bed (VL-F — DCML `schema_annotation_data`, pin `76f810a1`: 273 instances at pin / 244 at the
   paper snapshot; self-contained score bundle, same works as the DCML sonatas, distinct encoding). **Still
   open:** an implied-polyphony stream-labeled bed (VL-D's target task). **★ Union-search update (ratified
   2026-07-04, `cowork_union_search_record.md` §1):** the NOTATED-polyphony half now has ratified acquisition
   candidates — piano_svsep (393 pieces, per-note voice+staff GT over DCML piano scores we hold), MCMA (~475,
   CC-BY, hand-exploded Baroque voices), vocsep_ijcai2023 (1,054, notation-derived) — acquisition rides the
   next corpus dispatch; the IMPLIED-polyphony half is a **confirmed-final negative** (VoiSe/Gray-Bunescu
   never released). VL-D's design decides whether notated-voice GT suffices for its v1 target (add to §15-8's
   decision list). Also held: protovoice-annotations (38, reduction-encoded, partial).
   **★ ACQUIRED (2026-07-04, `cc_acquisition_round_report.md`):** all three N9 beds cloned + pinned + verified —
   piano_svsep @ `1462e7c2` (MIT code; GT graphs fetched at runtime from `fosfrancesco/piano_corpora_dcml`),
   MCMA @ `2bdb12e2` (475 `.mxl`, split 153/239/83 verified; **license CORRECTED to CC-BY-NC-SA-4.0** — the
   above "CC-BY" was the record's error, the NC clause matters for VL-H's downstream commercial posture),
   vocsep_ijcai2023 @ `82152a95` (MIT — not "unstated"; ~1,054 graphs built at runtime from bach-370-chorales +
   Haydn/Mozart SQ + MCMA). All held-out; VL-D's §15-8 notated-voice-suffices decision now has the beds on disk.
5. **VL-D/E/F/G/H design docs** — each written just-in-time when it is the next dispatch, per §5.4's gates.
6. **The static-harmony/motion-type feature** recorded by the study as the natural home of the harmonic study's
   deferred "wobbly sixth" (modal/static jazz) — a *harmonic-axis* taxonomy refinement informed by axis-2
   features; it rides a future idiom re-discovery wave, not this axis's build.
7. **ARCHITECTURE §2.15 propagation** (with the build, per §10 doc-sync): the voice-leading-span criterion
   pointer, the axis's status line, and — if A5 is ratified — the per-voice span kind.
8. **The VL-D shared-note question** (user-raised 2026-07-03): may one note belong to two streams (compound-melody
   pivots, voice crossings)? The separation literature mostly assigns each note to one stream; the answer — and
   its consequences for stream-tier profiles — is a VL-D design-doc decision, recorded here so it is not lost.
9. **The VL-E within-voice boundary questions** (audit finding, 2026-07-03): may one note belong to two
   phrase-spans of the same voice (phrase elision — the cadence tone beginning the next phrase)? And do rests
   between phrases sit inside a phrase-span or between phrase-spans? Both are VL-E design-doc decisions, parallel
   to §15-8.
10. **VL-H validation GT = BUILD, NOT DOWNLOAD (user-ratified ruling, 2026-07-04,
    `cowork_union_search_record.md` §5).** No public part-writing-error/exercise dataset exists (the commercial
    platforms Harmonia/Artusi hold exactly this data, closed — also demand evidence). VL-H's design doc owns the
    construction, two named routes: (i) transcribe the REAL-music positive seeds — Luke Dahn's manuscript-checked
    46 consecutive-5th/8ve instances in the Bach chorales (categorized fermata/NCT/chordal) + Fitsioris-Conklin's
    18 parallel-5th passages — with the remaining chorales as near-negatives; (ii) a synthetic-violation corpus
    (mutate correct solutions, auto-label the injected violation — every checker precedent's internal strategy).
    Tooling precedents recorded: music21 theoryAnalyzer, FuxCP, Palestrina Pal, the Check-Fux plugin.

## 16. Ratification asks

- **A1 — admit the axis** with the §5 decomposition and the three co-equal gates as argued (§9-D1).
- **A2 — the staged build order:** VL-A → VL-B → VL-C as the one dormant foundation build (a single CC increment,
  instruction just-in-time); VL-D/E/F/G design-gated (§5.4).
- **A3 — the two-tier voice model** (notated voice = fact; stream = inference; one-sense enforcement) (§9-D3).
- **A4 — the voice-leading-span criterion** ("the span one texture classification prevails over"; owner VL-C;
  v1 = whole selection until §15-1 measures the refinement).
- **A5 — the typology extension:** admit the **per-voice span kind** (phrase-spans: overlapping across voices by
  construction, tiling within one voice) into ARCHITECTURE §2.15 — needed before VL-E's design can be written
  against the typology.
- **A6 — the coverage declaration:** the axis is notated-music only; the voice-leading style coordinate is
  *undefined* (not zero) for voiceless sources; unvalidated marks per §10.
- **A7 — the claims registry:** VL-F claims the six voice-leading-defined Vocabulary entries; VL-E claims the
  melodic phrase [MT]; VL-G claims voicing/arrangement (the dictionary §5.3 exclusion); VL-H claims part-writing
  checking & suggestion (the advisory consumer, incl. the VL-B per-sample motion-event export that serves it).
  Recorded as claims with owners, discharged only at each component's own ratified design.
- **A8 — the cross-axis dependency rule** (acyclicity by declaration, re-checked per wiring) (§9-D6).

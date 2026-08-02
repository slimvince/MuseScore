# Decisions group G — Layer 4 — chord identity

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-060 — The legacy chord analyzer is a vertical sonority analyzer - keep the boundary clean

> Do not
> attempt to improve corpus agreement by adding heuristics to `RuleBasedChordAnalyzer`
> that embed contextual assumptions — keep the vertical/contextual boundary clean.

**In plain words.** The chord identifier is meant to say what chord the notes sounding at one moment spell, and nothing more. Improving its score by teaching it about what came before or after was explicitly forbidden.

**Why.** Measurement, ARCHITECTURE.md:2088-2108: the boundary is recorded as empirically validated against DCML annotations over four corpora (2026-04-06), and the residual disagreement is diagnosed rather than assumed - 95.8 % of the bass-is-root disagreements are three-note triads in inversion, which local note content cannot resolve. Improving past that ceiling is stated to need a contextual harmony layer, NOT heuristics inside the vertical analyzer. (The same section then specifies contextual bonuses - open_items/OI-235.)

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2106-2108`

**Provenance.** ARCHITECTURE.md:2082-2108. Contradicted by the same document's §4.1b/§4.1d contextual bonuses, which score a candidate from the neighbouring chords - see OPEN_ITEMS OI-235

### D-061 — Gate thresholds are Baroque-calibrated and must not be loosened for other styles

> They must not be
> loosened to accommodate other styles. When a gate causes regressions in a non-Baroque
> preset, the fix is either (a) a tighter structural entry condition that excludes the
> problematic chord type in all styles, or (b) a preset-specific threshold value

**In plain words.** The adjustable cut-offs in the chord scorer were tuned on Baroque music. If they misbehave on other music, tighten the entry condition for everyone or give that style its own value - never widen the Baroque one.

**Why.** Measurement, ARCHITECTURE.md:1776-1784 and `CLAUDE.md` gate policy: the values are empirically calibrated against the Baroque corpus and are Baroque-specific, so loosening one to accommodate another style silently re-tunes the style they were measured on; the two sanctioned fixes are a tighter structural entry condition that excludes the chord type in all styles, or a preset-specific override leaving the Baroque default unchanged.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1778-1782`

**Provenance.** ARCHITECTURE.md:1776-1784; the same policy is in CLAUDE.md 'Gate threshold and preset policy'

### D-062 — Progression signals are withheld while segmentation is being explored

> the progression signals are withheld
> during `greedyExpandSegmentation`'s internal boundary-exploration calls, which run in
> `ScoringPhase::Segmentation` — prevents the bonus from biasing segmentation
> before the final per-region pass

**In plain words.** While the program is still deciding where one chord ends and the next begins, the bonuses that reward a chord for fitting its neighbours are switched off, so that the answer does not bias the question.

**Why.** Stated constraint, ARCHITECTURE.md:2005-2008 (the withheld signals 'prevent the bonus from biasing segmentation before the final per-region pass') with :641-644: where a boundary falls decides which pitch classes land in each candidate's input, and chord identity is itself a signal for where boundaries should be - so letting progression signals score the exploratory passes would let the answer decide its own input.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2005-2008`

**Provenance.** ARCHITECTURE.md:2005-2008, :1816-1822; the residual coupling is recorded as debt at :2105-2112

### D-063 — Cold context on the tick-local path is the accepted contract

> Cold context on P4 is the **current contract**, documented and accepted (the same
> precedent as the Stage 2.3 diagnose context banner: a path may legitimately analyze with less
> context, provided that is stated, not silent).

**In plain words.** One narrow path analyses a moment without knowing what came before. That is allowed because it is written down, not hidden.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1483-1485`

**Provenance.** ARCHITECTURE.md:1474-1491. Its revisit trigger - 'Stage 3 design must state explicitly what P4 (and the bridge) consume from the decode' (:1299-1300) - has not been discharged by the joint/record design

### D-064 — The chord-scoring presets are a measurement-only artifact

> The
> chord-scoring preset system is currently a **measurement-only artifact** of `batch_analyze`. Do
> **not** silently flip the live product onto preset chordPrefs

**In plain words.** The Baroque and Jazz chord-scoring settings exist only in the measurement tool. The program the user runs has never used them, and switching it over would be a product decision, not a code tidy-up.

**Why.** derivation not recorded.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1546-1549`

**Provenance.** D-003 makes inference preset-independent on the production path, so the divergence this decision manages no longer exists there; it still describes the legacy path

### D-065 — The look-ahead divergence between the two paths is intentional and load-bearing

> **D1 — `excludeLookAheadOnDenseStart`** is **intentionally divergent and load-bearing.**

**In plain words.** One setting deliberately differs between the measurement tool and the program, because making them the same made the program worse on a specific repertoire.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1453`

**Provenance.** ARCHITECTURE.md:1453-1456, restated at :1363-1366

### D-066 — Chord symbols written in the score are never analyzer input

> chord symbols must never be used as analyzer input in
> production because they are user content and may be incorrect.

**In plain words.** The chord names already written in a score are the user's own text and may be wrong. The analysis reads only the notes, the key signature and the settings.

**Why.** Stated constraint, ARCHITECTURE.md:2535-2537: written chord symbols are USER CONTENT and may be incorrect, so reading them back as input would make the analyzer agree with whatever it was given rather than with the notes. The `--inject-written-root` flag is kept as a diagnostic upper bound and is explicitly not a production path.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2536-2537`

**Provenance.** ARCHITECTURE.md:2535-2537, restated as the retirement rationale's 'Core principle' at :2335-2337

### D-067 — Jazz mode (chord-symbol-driven boundaries) is retired

> **Status: Retired** — production analysis paths in commit 02e3733afb, tool-side surfaces in 69716deead. Chord symbols are no longer read by any analysis or tool path.

**In plain words.** The separate jazz analysis mode that took its stretch boundaries from written chord symbols has been removed entirely.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2504`

**Provenance.** ARCHITECTURE.md:2504, retirement rationale at :2324-2339

### D-068 — The chord identifier needs at least three distinct pitch classes

> Minimum 3 distinct pitch classes required. Returns empty vector if insufficient data.

**In plain words.** With fewer than three different pitch names sounding, the chord identifier declines to answer rather than guessing.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1817`

**Provenance.** ARCHITECTURE.md:1817

### D-069 — Two identity modes for merged stretches - harmonic summary and as-written

> **Harmonic summary mode** (status bar, analysis, tuning): region identity = root pitch
> class + quality.

**In plain words.** When neighbouring stretches are merged, they count as the same chord if the root and the major/minor character match. A second mode that would also require the exact voicing to match is designed but not built.

**Why.** derivation not recorded.

**Status.** DEFERRED · decided 2026-04-11 · ratifier not stated

**Home.** `ARCHITECTURE.md:1955-1956`

**Provenance.** ARCHITECTURE.md:1951 'Region identity modes (decided 2026-04-11)'; :1734-1736 records as-written mode deferred

### D-101 — Contextual inversion bonuses fire only for major and minor candidates

> **Safety constraints (lesson from three-attempt history) — ⚠ SUPERSEDED BY ITER 46, see §4.1g.** As
> originally written: bonuses never fire for Diminished, HalfDiminished, Augmented, or Suspended
> candidates — only Major and Minor. The existing `inversionSuspicionMargin` /

**In plain words.** The bonuses that let a neighbouring chord tip an inversion reading were restricted to plain major and minor chords, after three earlier attempts without that restriction all made things worse.

**Why.** Stated constraint, ARCHITECTURE.md:1856-1856: recorded as a hard-won safety constraint, the lesson of a three-attempt history in which the bonuses fired on qualities they were not measured on.

**Status.** SUPERSEDED BY D-102 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1856-1858`

**Provenance.** ARCHITECTURE.md:2160-2168 records Iter 46 extending the same helpers to Augmented and HalfDiminished. The §4.1b statement carries no supersession note - see OPEN_ITEMS OI-236 ★ Verbatim RE-TAKEN 2026-08-02 (the phase-1 truth-sync): the §4.1b passage now carries the supersession note it lacked, and states the constraint that actually survives at HEAD, which differs between the two helper predicates (OPEN_ITEMS OI-236 discharged). The decision's own words are preserved in place, marked 'As originally written'.

### D-102 — Augmented and half-diminished candidates receive the inversion bonuses too (Iter 46)

> Extending these gates put Augmented and
> HalfDiminished inversion candidates on equal footing with Major/Minor.

**In plain words.** The restriction above was later relaxed for augmented and half-diminished chords, because without the bonuses their correct inverted readings never reached the shortlist at all. It was the single largest improvement of that iteration path.

**Why.** Measurement, ARCHITECTURE.md:2160-2168: keeping D-101's constraint made correct inverted readings unreachable, and extending the two helper predicates to augmented and half-diminished was 'the largest single improvement of iteration path 1'.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2167-2168`

**Provenance.** ARCHITECTURE.md:2158-2171 (Iter 46, commit 36bf4738a8)

### D-103 — Pedal-point detection is a second pass, accepted only on two conditions

> **Pass 2** is triggered only when the Pass 1 bass PC is NOT a chord tone of the
> winner.

**In plain words.** When the lowest note does not belong to the chord the upper voices spell, the program re-analyses without it. It accepts that reading only if the upper voices give at least two different pitch names and the answer is clearly better than the next different-rooted one.

**Why.** Stated constraint, ARCHITECTURE.md:3880-3885: a single pass over an organ point either forces a bass-root reading and suppresses the upper-voice harmony, or returns a slash chord with the wrong root when a template accidentally fits. The 'different-root competitor' detail carries its own recorded reason at :3640-3643 - several templates share a root, so a gap measured against rank 2 collapses to about 0.047 and blocks detection for bare triads.

**Status.** SUPERSEDED BY D-207 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3893-3894`

**Provenance.** ARCHITECTURE.md:3871-3906 'Status: Implemented (Session 18, master fb9a27ce9a)'. Suspended on the record arm - see D-021. SUPERSEDED BY D-207 - open_items/OI-194.md:7 records the ratified successor (user, 2026-07-26): the voice-independent pedal-point class replaces this bass-only second pass and the `isPedalPoint`/`pedalBassPc` fact it produces

### D-104 — The bass-is-root bonus is conditioned on corroborating support

> `bassNoteRootBonus` is now conditioned on corroborating root-position support in the
> accumulated tones:

**In plain words.** Being the lowest note no longer counts as strong evidence of being the chord's root unless the chord above actually supports that reading. Without a third or fifth above it, the bonus almost vanishes.

**Why.** Measurement, ARCHITECTURE.md:3656-3675: four corpora (Chopin mazurka, Mozart sonata, Corelli trio sonata, Beethoven quartet) were inspected at the score and found to share ONE mechanism - the bass moves faster than the harmonic rhythm, so each bass note independently takes the bonus and overrides the root the chord tones above already identify. The fix conditions the bonus on corroborating root-position support rather than shrinking it.

**Status.** LIVE · decided 2026-04-09 · ratifier not stated

**Home.** `ARCHITECTURE.md:3674-3675`

**Provenance.** ARCHITECTURE.md:3651-3699; the failure it fixed is documented across four corpora at :3406-3419

### D-105 — The spelling written in the score is read through ONE shared interpreter

> read through the **shared** `engravingbridge::lineOfFifths` primitive (the Layer-1.5 spelling
>   view) — one interpreter, not a per-layer tpc copy.

**In plain words.** How a note is spelt on the page - F sharp versus G flat - is interpreted in one shared place, not re-implemented by each stage that needs it.

**Why.** Stated constraint, ARCHITECTURE.md:1358-1360 - 'one interpreter, not a per-layer tpc copy' (#6): two interpreters of the notated spelling can disagree, and open_items/OI-173 records what that costs when it happens (four inequivalent definitions of the same predicate).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1359-1360`

**Provenance.** ARCHITECTURE.md:1357-1360. ARCHITECTURE.md:1368-1372 records the unification residual: the legacy scorer still carries its own second reader until the legacy path retires

### D-207 — The pedal-point class is defined voice-independently, superseding the bass-only fact

> **The pedal-point class is defined VOICE-INDEPENDENTLY (user-ratified 2026-07-26; DEFERRED to its own
> increment).** The ornament vocabulary carries a **pedal-point** class: a tone sustained — or continuously
> restruck — against changing harmony in **any** voice, sub-labeled by position as **bass**, **internal**, or
> **inverted**. This class supersedes the legacy bass-only pair of published facts, `isPedalPoint` and

**In plain words.** A pedal point is a note held - or struck again and again - while the harmony changes around it, in ANY voice, not only the bass. It is labelled by where it sits: in the bass, inside the texture, or above it. This replaces the older fact, which could only see a pedal in the lowest voice.

**Why.** Stated constraint, open_items/OI-194.md:7: the legacy fact was produced by an unestablished post-pass and retires with the legacy path; the voice-independent class comes from the emission's own non-chord-tone categories, which do not privilege the bass. Two unresolved audit rows are recorded as dispositioned by this ruling.

**Status.** DEFERRED · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:4489-4492`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at open_items/OI-194.md:7, sharpened at the P1 pedal-point ruling, user-ratified 2026-07-26 at the consumption-audit verification (`cowork_notation_adoption_increment.md` §7 + §10). DEFERRED: it lands with the ornament-label publication, its own increment after the notation switch; until then the record arm leaves the pedal fields empty (D-021) and the 'X ped.' annotation is a declared gap. §5.12, which specifies the superseded two-pass detector, now carries a pointer to §7.4. OPEN_ITEMS OI-237 closes on this move

### D-236 — Chord-symbol trust is per symbol, not a per-score preference

> **Per-symbol trust, not per-score preference.** A per-score toggle is explicitly
> rejected — too coarse-grained, since a single score may contain both trusted
> lead-sheet-style annotations and untrusted draft symbols.

**In plain words.** If written chord symbols are ever treated as authoritative input, the authority is carried by each symbol. A single switch for a whole score is rejected.

**Why.** The reason is stated with the decision: one score may carry both trusted lead-sheet annotations and untrusted draft symbols, so a per-score toggle is too coarse-grained (ARCHITECTURE.md:2598-2600).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2598-2600`

**Provenance.** ARCHITECTURE.md:2576 heads the section "Future: Authoritative Chord Symbol Mode"; the current rule is that written symbols are never analyzer input (register entry D-066) ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-237 — Only a symbol marked trusted becomes analyzer input; an untrusted symbol is never read

> **Analyzer semantics:** Only when a `Harmony` element has `trusted = true` does it
> become boundary AND identity input for the harmonic region it opens. The analyzed
> root and quality are taken from the written symbol, not from note-based inference.
> Untrusted symbols remain comparison metadata only and are never read by the analysis
> pipeline.

**In plain words.** Under the planned authoritative-symbol mode, a written chord symbol opens a region and names its chord only when it is marked trusted. An untrusted symbol stays comparison metadata and the analysis never reads it.

**Why.** Derivation not recorded. The record states the semantics but not the evidence or constraint that fixed them.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2609-2613`

**Provenance.** ARCHITECTURE.md:2576 (the section is headed Future); register entry D-066 records the rule in force today ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-238 — Two pitch classes may nominate a chord but may not finalize one; one pitch class may not

> Initial rule:
> - 2 distinct pitch classes may nominate a candidate set
> - 2-PC evidence alone must not finalize a chord without contextual support
> - 1-PC evidence is insufficient for independent chord resolution and may only
>   participate in continuity-preserving abstention logic

**In plain words.** In the monophonic fallback, a slice with only two distinct pitch classes can propose candidates but cannot settle the chord without context; a single pitch class cannot settle one at all and may only keep an existing reading alive.

**Why.** The reason is stated beside the rule: it avoids over-interpretation of isolated tones (ARCHITECTURE.md:2760-2761).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2754-2758`

**Provenance.** ARCHITECTURE.md:2724 heads the section "Phase 1b - Minimal Monophonic Fallback Without Chord Symbols"; ARCHITECTURE.md:3496-3503 records monophonic input as planned ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-239 — Chord identity stays local; expansion is by one neighbouring region and is bounded

> **Bounded expansion in Phase 1b:**
> Chord identity should remain local. When a local group is too weak to resolve,
> the analyzer may expand by one neighboring region and re-score. Expansion is
> bounded and should stop when:
> - confidence crosses threshold
> - top-vs-second margin crosses threshold
> - the same winner survives repeated expansion
> - the hard expansion cap is reached

**In plain words.** When a group of notes is too weak to resolve on its own, the analyzer may take in one neighbouring region and score again. It stops as soon as confidence or the margin crosses its threshold, the winner repeats, or the expansion cap is reached.

**Why.** Derivation not recorded. The stop conditions are stated; the thresholds and the cap are left to be calibrated (see register entry D-240).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2763-2770`

**Provenance.** ARCHITECTURE.md:2724 (the Phase 1b section heading); the stop conditions are stated with the rule ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-240 — The monophonic smoothing terms are tunable parameters, not prose-only rules

> These terms must be implemented as tunable parameters rather than prose-only
> rules.

**In plain words.** The margins and thresholds that govern the monophonic fallback's smoothing are implemented as named settings, so they can be changed and measured rather than being buried in prose.

**Why.** Derivation not recorded. The record states the requirement and names the parameters it produces, but not the incident or principle that forced it.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2780-2781`

**Provenance.** ARCHITECTURE.md:2724 (the Phase 1b section heading); the named parameters are listed at :2783-2790 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-241 — The monophonic local-grouping problem is deferred to Phase 2

> The local grouping problem is intentionally deferred to Phase 2 because it is
> the hardest part of monophonic inference.

**In plain words.** Deciding how to group a single melodic line into harmonic units is left to the later, full monophonic engine rather than attempted in the minimal fallback.

**Why.** The reason is stated with the deferral: local grouping is the hardest part of monophonic inference (ARCHITECTURE.md:2810-2811).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2810-2811`

**Provenance.** ARCHITECTURE.md:2796 heads "Phase 2 - Full Monophonic Engine" ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-242 — Vertical and monophonic raw scores are never compared directly

> The unified layer must not compare vertical and monophonic raw scores directly.
> The two engines use different evidence models and therefore require explicit
> confidence calibration.

**In plain words.** The layer that combines the two chord engines may not put their raw numbers side by side. The two engines weigh different evidence, so their confidences must be calibrated onto a common footing first.

**Why.** The reason is stated with the rule: the two engines use different evidence models (ARCHITECTURE.md:2839-2840). It is the same commensurability constraint the cross-layer confidence contract states generally (register entry D-032).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2838-2840`

**Provenance.** ARCHITECTURE.md:2813 heads "Unified Orchestration Layer", part of the provisional phased plan recorded at :3498-3503 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).


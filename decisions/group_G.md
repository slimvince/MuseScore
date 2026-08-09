# Decisions group G — Layer 4 — chord identity

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-060 — The legacy chord analyzer is a vertical sonority analyzer - keep the boundary clean

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> Do not
> attempt to improve corpus agreement by adding heuristics to `RuleBasedChordAnalyzer`
> that embed contextual assumptions — keep the vertical/contextual boundary clean.

**In plain words.** The chord identifier is meant to say what chord the notes sounding at one moment spell, and nothing more. Improving its score by teaching it about what came before or after was explicitly forbidden.

**Why.** Measurement, ARCHITECTURE.md:2099-2119: the boundary is recorded as empirically validated against DCML annotations over four corpora (2026-04-06), and the residual disagreement is diagnosed rather than assumed - 95.8 % of the bass-is-root disagreements are three-note triads in inversion, which local note content cannot resolve. Improving past that ceiling is stated to need a contextual harmony layer, NOT heuristics inside the vertical analyzer. (The same section then specifies contextual bonuses - open_items/OI-235.)

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2872-2874`

**Provenance.** ARCHITECTURE.md:2093-2119. Contradicted by the same document's §4.1b/§4.1d contextual bonuses, which score a candidate from the neighbouring chords - see OPEN_ITEMS OI-235

### D-061 — Gate thresholds are Baroque-calibrated and must not be loosened for other styles

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> They must not be
> loosened to accommodate other styles. When a gate causes regressions in a non-Baroque
> preset, the fix is either (a) a tighter structural entry condition that excludes the
> problematic chord type in all styles, or (b) a preset-specific threshold value

**In plain words.** The adjustable cut-offs in the chord scorer were tuned on Baroque music. If they misbehave on other music, tighten the entry condition for everyone or give that style its own value - never widen the Baroque one.

**Why.** Measurement, ARCHITECTURE.md:1787-1795 and `CLAUDE.md` gate policy: the values are empirically calibrated against the Baroque corpus and are Baroque-specific, so loosening one to accommodate another style silently re-tunes the style they were measured on; the two sanctioned fixes are a tighter structural entry condition that excludes the chord type in all styles, or a preset-specific override leaving the Baroque default unchanged.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2544-2548`

**Provenance.** ARCHITECTURE.md:1787-1795; the same policy is in CLAUDE.md 'Gate threshold and preset policy'

### D-062 — Progression signals are withheld while segmentation is being explored

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> the progression signals are withheld
> during `greedyExpandSegmentation`'s internal boundary-exploration calls, which run in
> `ScoringPhase::Segmentation` — prevents the bonus from biasing segmentation
> before the final per-region pass

**In plain words.** While the program is still deciding where one chord ends and the next begins, the bonuses that reward a chord for fitting its neighbours are switched off, so that the answer does not bias the question.

**Why.** Stated constraint, ARCHITECTURE.md:2016-2019 (the withheld signals 'prevent the bonus from biasing segmentation before the final per-region pass') with :641-644: where a boundary falls decides which pitch classes land in each candidate's input, and chord identity is itself a signal for where boundaries should be - so letting progression signals score the exploratory passes would let the answer decide its own input.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2771-2774`

**Provenance.** ARCHITECTURE.md:2016-2019, :1816-1822; the residual coupling is recorded as debt at :2105-2112

### D-063 — Cold context on the tick-local path is the accepted contract

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> Cold context on P4 is the **current contract**, documented and accepted (the same
> precedent as the Stage 2.3 diagnose context banner: a path may legitimately analyze with less
> context, provided that is stated, not silent).

**In plain words.** One narrow path analyses a moment without knowing what came before. That is allowed because it is written down, not hidden.

**Why.** SEARCHED 2026-08-09 and the record HOLDS one — two grounds, both in the decision's own home text, which is why an empty field misrepresented it. **(1) A PRECEDENT, named in the decision sentence itself:** *"the same precedent as the Stage 2.3 diagnose context banner: a path may legitimately analyze with less context, provided that is stated, not silent."* The defensible thing is not the reduced context but its being declared. **(2) A SEQUENCING REASON, stated immediately after it:** *"No pre-pass is built now: Stage 3's lattice makes accumulated context a decode product, and any context pre-pass built against the greedy pipeline would be discarded at Stage 3"* — build-it-right before tune-precision (#8), applied to a specific piece of work that a later layer would throw away. The home also carries the FACTS the decision rests on (the fallback fires only when the regional path returns no region, structurally rare, exact live frequency **unmeasured**) and a REVISIT TRIGGER, which the record separately notes has not been discharged. No measured value is carried here (**D-431**).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2249-2251`

**Provenance.** ARCHITECTURE.md:1485-1502. Its revisit trigger - 'Stage 3 design must state explicitly what P4 (and the bridge) consume from the decode' (:1299-1300) - has not been discharged by the joint/record design

### D-064 — The chord-scoring presets are a measurement-only artifact

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> The
> chord-scoring preset system is currently a **measurement-only artifact** of `batch_analyze`. Do
> **not** silently flip the live product onto preset chordPrefs

**In plain words.** The Baroque and Jazz chord-scoring settings exist only in the measurement tool. The program the user runs has never used them, and switching it over would be a product decision, not a code tidy-up.

**Why.** SEARCHED 2026-08-09 and the record HOLDS one, stated in the decision's own home text as the KIND of decision this would be: *"whether the product should expose a chord-scoring style is a deliberate **product decision**, deferred."* The ground is therefore not that the presets are wrong but that flipping the live product onto them is not a code change at all — the home opens by recording the whole thing as *"a **product-level finding**, not a code change"* — so it may not be done silently as tidy-up. A second, doc-sync clause rides with it and belongs to the decision: every document implying that Jazz/Baroque chord tuning ships to users is to be corrected to batch-measurement only, because the live product analyzes chords with struct defaults. No measured value is carried here (**D-431**).

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2312-2315`

**Provenance.** D-003 makes inference preset-independent on the production path, so the divergence this decision manages no longer exists there; it still describes the legacy path

### D-065 — The look-ahead divergence between the two paths is intentional and load-bearing

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **D1 — `excludeLookAheadOnDenseStart`** is **intentionally divergent and load-bearing.**

**In plain words.** One setting deliberately differs between the measurement tool and the program, because making them the same made the program worse on a specific repertoire.

**Why.** SEARCHED 2026-08-09 and the record HOLDS one, and it is a MEASURED one stated in the decision's own home text: *"This is not an oversight: unifying it regresses the bridge/Corelli trio-sonata dominants."* The divergence is kept because the unified setting was tried and made the in-app path worse on a named repertoire — which is the reason the same home restates a second time at the Stage-2.4 block (*"unifying it regresses the Corelli trio-sonata dominants on the bridge"*), adding the disposition *"Keep diverged; keep documented."* The home also names where the flag's contract is written down, which is what makes the divergence declared rather than silent. No measured value is carried here (**D-431**) — the home states the direction of the regression, not a magnitude, and none is invented.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2219`

**Provenance.** ARCHITECTURE.md:1464-1467, restated at :1363-1366

### D-066 — Chord symbols written in the score are never analyzer input

> chord symbols must never be used as analyzer input in
> production because they are user content and may be incorrect.

**In plain words.** The chord names already written in a score are the user's own text and may be wrong. The analysis reads only the notes, the key signature and the settings.

**Why.** Stated constraint, ARCHITECTURE.md:2546-2548: written chord symbols are USER CONTENT and may be incorrect, so reading them back as input would make the analyzer agree with whatever it was given rather than with the notes. The `--inject-written-root` flag is kept as a diagnostic upper bound and is explicitly not a production path.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3302-3303`

**Provenance.** ARCHITECTURE.md:2546-2548, restated as the retirement rationale's 'Core principle' at :2335-2337

### D-067 — Jazz mode (chord-symbol-driven boundaries) is retired

> **Status: Retired** — production analysis paths in commit 02e3733afb, tool-side surfaces in 69716deead. Chord symbols are no longer read by any analysis or tool path.

**In plain words.** The separate jazz analysis mode that took its stretch boundaries from written chord symbols has been removed entirely.

**Why.** SEARCHED 2026-08-09 and the record HOLDS one, in full, at a *Retirement rationale* block in the same specification — which is why an empty field misrepresented it. The block does not argue the retirement directly; it takes the three reasons the mode had EXISTED for and dismantles each. **Reason 1, redundancy** — a value judgment rather than a structural one: symbol-derived boundaries remain computable, so the question was whether their output is BETTER than note-derived output, never whether it is possible. **Reason 2, rootless voicings** — concerns chord IDENTITY and not boundaries, so it never justified symbol-driven boundaries at all; the identity problem exists however stretches are delimited. **Reason 3, monophonic and sparse voicings** — load-bearing only if identity inference from sparse notes also succeeded, and it does not, so boundaries without usable identity yield symbol-echoed output rather than analysis. **And a CORE PRINCIPLE the block states as the ground the three reasons are measured against:** chord symbols are user-written instructions, not analysis results, and analyzer output is a pure function of notes plus key signature plus preferences. That principle is what the tool-side half of the retirement completed. It is stated independently as **D-066**, and is cited here rather than restated (#6).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3270`

**Provenance.** ARCHITECTURE.md:2515, retirement rationale at :2324-2339

### D-068 — The chord identifier needs at least three distinct pitch classes

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> Minimum 3 distinct pitch classes required. Returns empty vector if insufficient data.

**In plain words.** With fewer than three different pitch names sounding, the chord identifier declines to answer rather than guessing.

**Why.** SEARCHED 2026-08-09 and the record holds NO derivation. The home states the rule and its consequence — the minimum, and that the identifier returns an empty result rather than a reading when it is not met — and the sentences around it are about instantiation and dependency injection, not about the threshold. Nothing in the record says why THREE: no alternative is recorded as considered, no measurement is attached, and the musical argument that a triad is the smallest chord whose quality is decidable from pitch classes alone is nowhere stated as this decision's ground. Recorded as an established gap and NOT filled from that argument, which would be a defense written after the fact. **This threshold is the subject of live work and the gap should be read beside it:** what the joint decoder ADMITS as a candidate has no specified form and is tracked at `OPEN_ITEMS.md` OI-226, with the sparse-density family at OI-215 and OI-227 — and `CLAUDE.md` records that candidate admission is COMPLETION rather than refinement, so #8 does not block deriving the correct rule from the model.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2583`

**Provenance.** ARCHITECTURE.md:1828

### D-069 — Two identity modes for merged stretches - harmonic summary and as-written

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **Harmonic summary mode** (status bar, analysis, tuning): region identity = root pitch
> class + quality.

**In plain words.** When neighbouring stretches are merged, they count as the same chord if the root and the major/minor character match. A second mode that would also require the exact voicing to match is designed but not built.

**Why.** SEARCHED 2026-08-09. The record holds NO derivation for the identity rule itself, and it DOES hold a stated ground for the deferral of the second mode plus a consequence the deferral is known to cost. **What is not recorded:** why a merged stretch's identity is root pitch class plus quality — why extensions, inversions and slash-chord bass notes are secondary metadata rather than identity keys. The home states the rule and the two modes' contents, and no alternative is recorded as considered. **What IS recorded, and is not the same thing:** the as-written mode is deferred because it *"requires a mode flag in the implode bridge and a separate merge pass"* — a cost, which is a ground for not building it yet rather than a derivation of the rule that ships. **And the deferral's price is stated with it**, which is why the entry is worth reading whole: the chord-track octave-deduplication limitation is named as *"the primary consequence of this deferral"*. Recorded as an established gap on the identity rule; nothing is invented for it.

**Status.** DEFERRED · decided 2026-04-11 · ratifier not stated

**Home.** `ARCHITECTURE.md:2721-2722`

**Provenance.** ARCHITECTURE.md:1962 'Region identity modes (decided 2026-04-11)'; :1734-1736 records as-written mode deferred

### D-101 — Contextual inversion bonuses fire only for major and minor candidates

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **Safety constraints (lesson from three-attempt history) — ⚠ SUPERSEDED BY ITER 46, see §4.1g.** As
> originally written: bonuses never fire for Diminished, HalfDiminished, Augmented, or Suspended
> candidates — only Major and Minor. The existing `inversionSuspicionMargin` /

**In plain words.** The bonuses that let a neighbouring chord tip an inversion reading were restricted to plain major and minor chords, after three earlier attempts without that restriction all made things worse.

**Why.** Stated constraint, ARCHITECTURE.md:1867-1867: recorded as a hard-won safety constraint, the lesson of a three-attempt history in which the bonuses fired on qualities they were not measured on.

**Status.** SUPERSEDED BY D-102 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2622-2624`

**Provenance.** ARCHITECTURE.md:2171-2179 records Iter 46 extending the same helpers to Augmented and HalfDiminished. The §4.1b statement carries no supersession note - see OPEN_ITEMS OI-236 ★ Verbatim RE-TAKEN 2026-08-02 (the phase-1 truth-sync): the §4.1b passage now carries the supersession note it lacked, and states the constraint that actually survives at HEAD, which differs between the two helper predicates (OPEN_ITEMS OI-236 discharged). The decision's own words are preserved in place, marked 'As originally written'.

### D-102 — Augmented and half-diminished candidates receive the inversion bonuses too (Iter 46)

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> Extending these gates put Augmented and
> HalfDiminished inversion candidates on equal footing with Major/Minor.

**In plain words.** The restriction above was later relaxed for augmented and half-diminished chords, because without the bonuses their correct inverted readings never reached the shortlist at all. It was the single largest improvement of that iteration path.

**Why.** Measurement, ARCHITECTURE.md:2171-2179: keeping D-101's constraint made correct inverted readings unreachable, and extending the two helper predicates to augmented and half-diminished was 'the largest single improvement of iteration path 1'.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2933-2934`

**Provenance.** ARCHITECTURE.md:2169-2182 (Iter 46, commit 36bf4738a8)

### D-103 — Pedal-point detection is a second pass, accepted only on two conditions

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **Pass 2** is triggered only when the Pass 1 bass PC is NOT a chord tone of the
> winner.

**In plain words.** When the lowest note does not belong to the chord the upper voices spell, the program re-analyses without it. It accepts that reading only if the upper voices give at least two different pitch names and the answer is clearly better than the next different-rooted one.

**Why.** Stated constraint, ARCHITECTURE.md:3891-3896: a single pass over an organ point either forces a bass-root reading and suppresses the upper-voice harmony, or returns a slash chord with the wrong root when a template accidentally fits. The 'different-root competitor' detail carries its own recorded reason at :3640-3643 - several templates share a root, so a gap measured against rank 2 collapses to about 0.047 and blocks detection for bare triads.

**Status.** SUPERSEDED BY D-207 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4747-4748`

**Provenance.** ARCHITECTURE.md:3882-3917 'Status: Implemented (Session 18, master fb9a27ce9a)'. Suspended on the record arm - see D-021. SUPERSEDED BY D-207 - open_items/OI-194.md:7 records the ratified successor (user, 2026-07-26): the voice-independent pedal-point class replaces this bass-only second pass and the `isPedalPoint`/`pedalBassPc` fact it produces

### D-104 — The bass-is-root bonus is conditioned on corroborating support

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> `bassNoteRootBonus` is now conditioned on corroborating root-position support in the
> accumulated tones:

**In plain words.** Being the lowest note no longer counts as strong evidence of being the chord's root unless the chord above actually supports that reading. Without a third or fifth above it, the bonus almost vanishes.

**Why.** Measurement, ARCHITECTURE.md:3667-3686: four corpora (Chopin mazurka, Mozart sonata, Corelli trio sonata, Beethoven quartet) were inspected at the score and found to share ONE mechanism - the bass moves faster than the harmonic rhythm, so each bass note independently takes the bonus and overrides the root the chord tones above already identify. The fix conditions the bonus on corroborating root-position support rather than shrinking it.

**Status.** LIVE · decided 2026-04-09 · ratifier not stated

**Home.** `ARCHITECTURE.md:4528-4529`

**Provenance.** ARCHITECTURE.md:3662-3710; the failure it fixed is documented across four corpora at :3406-3419

### D-105 — The spelling written in the score is read through ONE shared interpreter

> read through the **shared** `engravingbridge::lineOfFifths` primitive (the Layer-1.5 spelling
>   view) — one interpreter, not a per-layer tpc copy.

**In plain words.** How a note is spelt on the page - F sharp versus G flat - is interpreted in one shared place, not re-implemented by each stage that needs it.

**Why.** Stated constraint, ARCHITECTURE.md:1369-1371 - 'one interpreter, not a per-layer tpc copy' (#6): two interpreters of the notated spelling can disagree, and open_items/OI-173 records what that costs when it happens (four inequivalent definitions of the same predicate).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1919-1920`

**Provenance.** ARCHITECTURE.md:1368-1371. ARCHITECTURE.md:1379-1383 records the unification residual: the legacy scorer still carries its own second reader until the legacy path retires

### D-207 — The pedal-point class is defined voice-independently, superseding the bass-only fact

> **The pedal-point class is defined VOICE-INDEPENDENTLY (user-ratified 2026-07-26; DEFERRED to its own
> increment).** The ornament vocabulary carries a **pedal-point** class: a tone sustained — or continuously
> restruck — against changing harmony in **any** voice, sub-labeled by position as **bass**, **internal**, or
> **inverted**. This class supersedes the legacy bass-only pair of published facts, `isPedalPoint` and

**In plain words.** A pedal point is a note held - or struck again and again - while the harmony changes around it, in ANY voice, not only the bass. It is labelled by where it sits: in the bass, inside the texture, or above it. This replaces the older fact, which could only see a pedal in the lowest voice.

**Why.** Stated constraint, open_items/OI-194.md:7: the legacy fact was produced by an unestablished post-pass and retires with the legacy path; the voice-independent class comes from the emission's own non-chord-tone categories, which do not privilege the bass. Two unresolved audit rows are recorded as dispositioned by this ruling.

**Status.** DEFERRED · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:5612-5615`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at open_items/OI-194.md:7, sharpened at the P1 pedal-point ruling, user-ratified 2026-07-26 at the consumption-audit verification (`cowork_notation_adoption_increment.md` §7 + §10). DEFERRED: it lands with the ornament-label publication, its own increment after the notation switch; until then the record arm leaves the pedal fields empty (D-021) and the 'X ped.' annotation is a declared gap. §5.12, which specifies the superseded two-pass detector, now carries a pointer to §7.4. OPEN_ITEMS OI-237 closes on this move

### D-236 — Chord-symbol trust is per symbol, not a per-score preference

> **Per-symbol trust, not per-score preference.** A per-score toggle is explicitly
> rejected — too coarse-grained, since a single score may contain both trusted
> lead-sheet-style annotations and untrusted draft symbols.

**In plain words.** If written chord symbols are ever treated as authoritative input, the authority is carried by each symbol. A single switch for a whole score is rejected.

**Why.** The reason is stated with the decision: one score may carry both trusted lead-sheet annotations and untrusted draft symbols, so a per-score toggle is too coarse-grained (ARCHITECTURE.md:2609-2611).

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3387-3389`

**Provenance.** ARCHITECTURE.md:2587 heads the section "Future: Authoritative Chord Symbol Mode"; the current rule is that written symbols are never analyzer input (register entry D-066) ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-237 — Only a symbol marked trusted becomes analyzer input; an untrusted symbol is never read

> **Analyzer semantics:** Only when a `Harmony` element has `trusted = true` does it
> become boundary AND identity input for the harmonic region it opens. The analyzed
> root and quality are taken from the written symbol, not from note-based inference.
> Untrusted symbols remain comparison metadata only and are never read by the analysis
> pipeline.

**In plain words.** Under the planned authoritative-symbol mode, a written chord symbol opens a region and names its chord only when it is marked trusted. An untrusted symbol stays comparison metadata and the analysis never reads it.

**Why.** Derivation not recorded. The record states the semantics but not the evidence or constraint that fixed them.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3398-3402`

**Provenance.** ARCHITECTURE.md:2587 (the section is headed Future); register entry D-066 records the rule in force today ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-238 — Two pitch classes may nominate a chord but may not finalize one; one pitch class may not

> Initial rule:
> - 2 distinct pitch classes may nominate a candidate set
> - 2-PC evidence alone must not finalize a chord without contextual support
> - 1-PC evidence is insufficient for independent chord resolution and may only
>   participate in continuity-preserving abstention logic

**In plain words.** In the monophonic fallback, a slice with only two distinct pitch classes can propose candidates but cannot settle the chord without context; a single pitch class cannot settle one at all and may only keep an existing reading alive.

**Why.** The reason is stated beside the rule: it avoids over-interpretation of isolated tones (ARCHITECTURE.md:2771-2772).

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3543-3547`

**Provenance.** ARCHITECTURE.md:2735 heads the section "Phase 1b - Minimal Monophonic Fallback Without Chord Symbols"; ARCHITECTURE.md:3507-3514 records monophonic input as planned ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3552-3559`

**Provenance.** ARCHITECTURE.md:2735 (the Phase 1b section heading); the stop conditions are stated with the rule ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-240 — The monophonic smoothing terms are tunable parameters, not prose-only rules

> These terms must be implemented as tunable parameters rather than prose-only
> rules.

**In plain words.** The margins and thresholds that govern the monophonic fallback's smoothing are implemented as named settings, so they can be changed and measured rather than being buried in prose.

**Why.** Derivation not recorded. The record states the requirement and names the parameters it produces, but not the incident or principle that forced it.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3569-3570`

**Provenance.** ARCHITECTURE.md:2735 (the Phase 1b section heading); the named parameters are listed at :2783-2790 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-241 — The monophonic local-grouping problem is deferred to Phase 2

> The local grouping problem is intentionally deferred to Phase 2 because it is
> the hardest part of monophonic inference.

**In plain words.** Deciding how to group a single melodic line into harmonic units is left to the later, full monophonic engine rather than attempted in the minimal fallback.

**Why.** The reason is stated with the deferral: local grouping is the hardest part of monophonic inference (ARCHITECTURE.md:2821-2822).

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3599-3600`

**Provenance.** ARCHITECTURE.md:2807 heads "Phase 2 - Full Monophonic Engine" ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-242 — Vertical and monophonic raw scores are never compared directly

> The unified layer must not compare vertical and monophonic raw scores directly.
> The two engines use different evidence models and therefore require explicit
> confidence calibration.

**In plain words.** The layer that combines the two chord engines may not put their raw numbers side by side. The two engines weigh different evidence, so their confidences must be calibrated onto a common footing first.

**Why.** The reason is stated with the rule: the two engines use different evidence models (ARCHITECTURE.md:2850-2851). It is the same commensurability constraint the cross-layer confidence contract states generally (register entry D-032).

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3627-3629`

**Provenance.** ARCHITECTURE.md:2824 heads "Unified Orchestration Layer", part of the provisional phased plan recorded at :3498-3503 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-280 — Gates read structured fields only - never a chord symbol string and never a Roman numeral

> 1. **A gate or scoring rule reads STRUCTURED FIELDS ONLY — never a chord-symbol string, never a
>    Roman numeral.** No chord-symbol string parsing and no Roman-numeral inference anywhere in a
>    gate, a scoring term, or any future change to either. *Why:* stated with the rule — signals
>    derived from a symbol or a Roman numeral are lossy and entangled with the formatter, so they are
>    not reliable inputs to chord classification; and reading the rendered form back in would make
>    the analysis depend on its own presentation layer, which is the one direction this boundary

**In plain words.** Any gate or scoring rule reads structured analysis fields. It never parses a chord-symbol string and never infers from a Roman numeral. Signals derived from symbols or Roman numerals are too lossy and too entangled with the formatter to be reliable inputs to chord classification.

**Why.** The reason is stated with the rule: symbol- and Roman-numeral-derived signals are lossy and entangled with the formatter. It is the inference/presentation boundary (register entries D-016 and D-017) stated as an input restriction - reading the rendered form back in would make an analysis depend on its own presentation layer.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1412-1417`

**Provenance.** docs/iteration_path1_summary.md:74-78, recorded among the architecture decisions of the completed iteration path and stated there as 'now a standing rule for any future gate or scoring change'; no date or ratifier is stated at this home. Distinct from register entry D-066, which forbids chord symbols written in the SCORE as analyzer input; this forbids re-reading our own rendered output. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that this is an INPUT restriction on scoring, which `docs/scoring_model.md` also governs. The user ruled the BOUNDARY RULE: a boundary invariant that binds every reader homes at the boundary's own section, §3.3, and other documents POINT and never copy. Written into §3.3 as the first of two such invariants, in that section's own voice and with its defense; `docs/scoring_model.md` §6 gains a POINTER at it — permitted by the ruling and a pointer only, never a copy (#6). Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/iteration_path1_summary.md:87-91`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 64, "section": "## Architecture decisions made during this path", "label": "“Architecture decisions made during this path”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "contract-home", "class_before_phase1q": "contract-home", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "4. **Gates operate on structured fields only**: no chord-symbol string parsing,
   no Roman-numeral inference. This is now a standing rule for any future gate
   or scoring change. Symbol- and Roman-numeral-derived signals are too lossy
   and too entangled with the formatter to be reliable inputs to chord
   classification." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-284 — Meta-finding: selection/competition is saturated, stop adding re-ranking gates - superseded by the gates doctrine and the adoption

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Selection/competition is saturated** — stop adding re-ranking heuristics/gates; the residual is
>   candidate-generation, key-quality, or floor.

**In plain words.** Stop investing in the legacy scorer’s gate and re-ranking surface; the remaining error lives in candidate generation and key quality. The doctrine lives on generalized in the ratified accumulating-gates rule, and the mechanism it warned about was retired wholesale when the joint estimator replaced the legacy selection surface.

**Why.** Record-derivable: D-036 (accumulating gates are a warning sign - add iteration, not more gates) carries the standing doctrine; D-001/D-010 retired the legacy selection surface on both production paths (compiled-dormant, awaiting the retirement map).

**Status.** SUPERSEDED BY D-036 with D-001/D-010 · date not stated · ratifier not stated

**Home.** `cowork_architecture_reassessment.md:108-109`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§4** — `## 4. Meta-findings to institutionalize (cross-cutting)` (heading at line 104). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Stated 2026-06-20 in cowork_architecture_reassessment.md §4 ('Meta-findings to institutionalize'); put to the user in §5 ('Ratify: …') with NO recorded answer (open_items/OI-270.md, the phase-1d wave's remainder). ★ RULED by the user 2026-08-02 (the OI-270 split, all four recommendations adopted): SUPERSEDED BY the named later ratified decisions — the governing status derives from the record's dates and explicitness, not from resolving the original statement's ambiguity. The second-partition read of the archives is instructed to flag anything refining these. ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

### D-299 — No negative-margin guard may be added - it would break every intentional backward-swap gate

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not add a negative-margin guard.** A rule refusing to let a later correction step overturn
>   the leading reading when the margin against it is negative must not be added. *Why:* structural,
>   and stated with the mechanism — the correction steps that exist promote a reading that was BEHIND
>   on the raw candidate score, so a guard keyed on that margin removes their reason to exist. It
>   would disable every intentional backward-swap gate at once.

**In plain words.** A rule that refuses to let a later correction step overturn the leading reading when the margin against it is negative must not be added. Several correction steps exist precisely to overturn a leading reading, and such a rule would disable all of them.

**Why.** A structural prohibition, stated with the mechanism: the named correction steps promote a reading that was behind on the raw score, so a guard keyed on that margin removes their reason to exist.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1285-1289`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the failure-cluster block). This is the statement the 2026-08-02 residual pass cited as its worked example of a real ruling sitting inside the unresolved residual (`open_items/OI-207.md`, the residual-pass note), now entered. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-08 (CC, `cc_instruction_away_execution.md` Task 2) into `docs/scoring_model.md` §8, which the record itself names as the standing home for scoring dead ends — the archive it lived in is NOT part of the session-start read and is not a home for a standing decision. The archive is untouched (#12). The `ARCHITECTURE.md` chord-layer NAMING is unchanged and is now a pointer to a section that states the rule rather than to a tracking surface. FORMER HOME, PRESERVED (#12): `cowork_handoff_archive.md:4967`. FORMER CLASS, PRESERVED (#12): `unhomed`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Do NOT add a negative-margin guard** — would break Gate J and all other\nintentional backward-swap gates (B/C/D/E/F/G/H/I/K/L, Iter 91)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. The gate letters and the iteration number stay in the archive that recorded them and are not carried into the specification (D-431). **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-300 — Gate M (minor read as diminished) is DEFERRED and must not be retried without a new runtime signal

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not retry reading a minor chord as a diminished one on the same root** unless some new
>   evidence becomes available while the music is being analysed. *Why:* measured — a handful of
>   genuine cases against several times as many wrong firings, and the record states that no field or
>   combination of fields available at analysis time separates them: the genuine cases split into two
>   groups, each sharing an identical structural profile with a large wrong-firing cluster, and the
>   leading-tone hypothesis was tested and falsified on all of them. The counts are in the archive
>   that measured them and are not restated here (D-431).

**In plain words.** A proposed correction rule that would have re-read a minor chord as a diminished one on the same root is abandoned. It is not to be attempted again unless some new evidence becomes available while the music is being analysed.

**Why.** Measured: 8 genuine cases against 25 false positives, and the record states that no field or combination of fields available at analysis time separates the two — the eight genuine cases split into two groups, each sharing an identical structural profile with a large false-positive cluster, and the leading-tone hypothesis was tested and falsified on all eight (`STATUS_ARCHIVE.md:1090-1106`).

**Status.** DEFERRED · decided 2026-05-09 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1290-1296`

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (the Iter-37 carried-forward block and its fenced deferral record at `:1090-1106`). Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-08 (CC, `cc_instruction_away_execution.md` Task 2) into `docs/scoring_model.md` §8. **The entry's own provenance is what settled the owner:** it recorded, checked and not assumed, that §8 — *"the standing home for scoring dead ends"* — did not mention this one; that gap is what has now been closed, and the sentence recording it is superseded in fact by the act it called for. The archive is untouched (#12) and the `ARCHITECTURE.md` chord-layer naming is unchanged. FORMER HOME, PRESERVED (#12): `STATUS_ARCHIVE.md:1147`. FORMER CLASS, PRESERVED (#12): `unhomed`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Gate M (Minor→Diminished TYPE-A): DEFERRED — do not retry.** See Iter 37 entry above.\nRequires DCML harmonic context not available at runtime." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. The measured counts stay in the archive that recorded them and are not carried into the specification (D-431); the gate LETTER is likewise not carried, being an identifier of the machinery awaiting deletion rather than of the prohibition. **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-301 — Gate N (major read as an inverted minor) is DEFERRED and must not be retried without a multi-region model

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not retry reading a root-position major chord as the first inversion of a minor one** without
>   a model that reads several stretches together. *Why:* measured and then diagnosed, which is what
>   closes it rather than merely discouraging it — the pattern is architecturally endemic, because the
>   submediant in first inversion always scores close to the tonic in any major key, so it recurs
>   across a large fraction of the corpus; and neither a diatonic-root check, a key-mode guard nor a
>   tighter margin reduces the wrong firings.

**In plain words.** A proposed correction rule that would have re-read a root-position major chord as the first inversion of a minor chord is abandoned. Six real cases were found against roughly two hundred and seventy wrong firings, so it is not to be attempted again without a model that reads several chords together.

**Why.** Measured and diagnosed: the pattern is architecturally endemic — the submediant in first inversion always scores close to the tonic in any major key, so it recurs across more than 125 corpus pieces, and neither a diatonic-root check, a key-mode guard nor a tighter margin reduces the false-positive count (`STATUS_ARCHIVE.md:1110-1131`).

**Status.** DEFERRED · decided 2026-05-09 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1297-1302`

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (the Iter-39 carried-forward block and its fenced deferral record at `:1110-1131`). Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-08 (CC, `cc_instruction_away_execution.md` Task 2) into `docs/scoring_model.md` §8, the record's own named home for scoring dead ends. The entry's *"Absent from `docs/scoring_model.md` §8 — checked"* is what identified the owner, and that absence is what this act closed. The archive is untouched (#12) and the `ARCHITECTURE.md` chord-layer naming is unchanged. FORMER HOME, PRESERVED (#12): `STATUS_ARCHIVE.md:1149`. FORMER CLASS, PRESERVED (#12): `unhomed`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Gate N (Major→Minor TYPE-A): DEFERRED — do not retry.** See Iter 39 entry above.\nFP:genuine = 45:1 (270:6 at threshold=0.30). Same limitation as Gate M.\nThe 6 genuine cases (vi/3 in major key) remain as unresolvable BIR=true errors." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. The ratio, the threshold and the piece count stay in the archive that measured them and are not carried into the specification (D-431). **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-302 — No further local scoring fix for inversions may be attempted — the remaining divergence is not an analyzer defect

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not attempt any further LOCAL scoring fix for inversions.** Correcting which note of a chord
>   is treated as its root by adjusting the numbers a single sonority earns in isolation is closed as
>   a line of work. *Why:* six weeks of investigation across four corpora and six attempts, with five
>   stated conclusions — the overwhelming majority of the genuine cases are bare three-note triads for
>   which bass-as-root is the statistically correct default; the four-note cases already score
>   correctly; the added-sixth against seventh-chord ambiguity is a data impossibility; **no
>   spelling-bonus window exists**, a bonus large enough to correct the triads breaking every
>   sixth-chord convention; and the remainder is a legitimate divergence between reading a sonority
>   vertically and reading it by its role, **which is not an analyzer defect at all**.

**In plain words.** Trying to correct which note of a chord is treated as its root by adjusting the numbers a single sonority earns in isolation is closed as a line of work. What remains is a genuine difference between reading a sonority on its own and reading it by its role in the music.

**Why.** Six weeks of investigation across four corpora and six fix attempts, with five stated conclusions: 95.8 % of the genuine cases are bare three-note triads for which bass-as-root is the statistically correct default; the four-note cases already score correctly; the added-sixth against seventh-chord ambiguity is a data impossibility; no spelling-bonus window exists (a bonus large enough to correct the triads breaks every sixth-chord convention — 20 catalog regressions against 0 corpus improvements); and the remainder is legitimate divergence between vertical sonority analysis and functional annotation (`STATUS_ARCHIVE.md:2731-2769`).

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1303-1311`

**Provenance.** Recorded in `STATUS_ARCHIVE.md` as the closing statement of the “Inversion Fix — Final Conclusion” block. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-08 (CC, `cc_instruction_away_execution.md` Task 2) into `docs/scoring_model.md` §8, the record's own named home for scoring dead ends; the entry's *"Absent from `docs/scoring_model.md` §8"* identified the owner and that absence is what this act closed. The archive is untouched (#12) and the `ARCHITECTURE.md` chord-layer naming is unchanged. ★ THE HOMED WORDING SAYS *LOCAL* IN TERMS, because the former verbatim's first sentence — that the then-current baseline is the correct production one — is a statement about a baseline that has since been re-based twice, and carrying it into a live specification would have written a stale claim into the compliance surface. What is standing is the prohibition, and the prohibition is on the LOCAL fix. FORMER HOME, PRESERVED (#12): `STATUS_ARCHIVE.md:2779`. FORMER CLASS, PRESERVED (#12): `unhomed`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Current baseline is the correct production baseline. Do not attempt\nfurther local scoring fixes for inversions.**" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. The percentage and the regression counts stay in the archive that measured them and are not carried into the specification (D-431). **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-303 — Non-chord-tone detection is deferred, and if built it must be chord identification that knows about non-chord tones, never stripping after the fact

> **Deciding which sounding notes do not belong to the chord is DEFERRED — and when it is built, the
> knowledge enters the chord decision itself, never a removal afterwards.** Non-chord-tone detection waits
> for the annotated material it needs. Its shape is constrained in advance: chord identification that knows

**In plain words.** Deciding which sounding notes do not belong to the chord is postponed. When it is built, the knowledge must enter the chord decision itself; removing notes from an answer after the chord has been named is ruled out.

**Why.** derivation not recorded

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1875-1877`

**Provenance.** Recorded in `STATUS_ARCHIVE.md`'s “architectural memos retained as guardrails” list. It is load-bearing now: the non-chord-tone filter is the named lever at [[OI-55]] and [[OI-68]], and `docs/nct_detection_design.md` exists on disk. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written into the Layer-4 section of `ARCHITECTURE.md` §3.3 as a deferred capability with its shape constrained in advance. The defense stays 'derivation not recorded' — the record gives none and none was invented. Former home preserved (#12): `STATUS_ARCHIVE.md:963`, the architectural-memos list.

### D-305 — The ban on reading written harmony as analyzer input is decided by what an annotation says, not by how it is stored

> **The ban is decided by WHAT AN ANNOTATION SAYS, not by how the score stores it.** No harmonic
> annotation already written in a score may be read as analyzer input — not a chord symbol, not a
> Roman numeral, not a function, cadence or key label — whatever kind of score object happens to

**In plain words.** Our analysis must not read any harmonic annotation already in the score — not a chord symbol, not a Roman numeral, not a function, cadence or key label — whatever kind of score object holds it. Ordinary notational metadata such as the key signature is still allowed.

**Why.** derivation not recorded

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:3305-3307`

**Provenance.** Recorded in `STATUS_ARCHIVE.md`'s “architectural memos retained as guardrails” list. It sharpens **D-066** (chord symbols written in the score are never analyzer input) from one annotation kind to a content test over all of them. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written beside D-066 in `ARCHITECTURE.md` §4.2, where the chord-symbol ban it generalizes already stood. The defense stays 'derivation not recorded'. Former home preserved (#12): `STATUS_ARCHIVE.md:961`.

### D-312 — The carried alternative readings are inside the byte-identity acceptance contract — same winner with different alternatives is a behavior change

> RULED:
> `alternatives[]` IS inside the byte-identity acceptance contract** — the carried alternatives are a
> load-bearing output surface (the L4 §15 O1b carry contract: L5 overrides select among carried
> readings; E-14 makes them user-visible), so "same winner, different alternatives" is a behavior
> change.

**In plain words.** When a change is claimed to leave the analysis untouched, the claim covers the ranked runner-up readings as well as the chosen one. A change that keeps the same answer but alters the alternatives beneath it is a change in behaviour and must be ratified as one.

**Why.** Grounded in two recorded facts: the function layer selects among the carried readings rather than re-deriving them, so they are an input to a later decision; and they are shown to the user, so altering them alters the product. The founding case measured it — a retirement that was winner-identical on all 352 scores altered the alternatives on 36 of them (`cowork_stage5_fitter_design.md:1299-1308`).

**Status.** LIVE · decided 2026-07-05 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_stage5_fitter_design.md:1003`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§15 Open items & ratification asks”** — `## §15 Open items & ratification asks` (heading at line 908). A delegation at ARCHITECTURE.md:301 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Recorded in `cowork_stage5_fitter_design.md` (SIGNED, user, 2026-07-04) at open item O-11, and again in `STATUS_ARCHIVE.md:186`. It is the origin of the full-output-surface half of principle #15 (**D-178**): the same entry records the evidence-method lesson that inertness evidence must measure the winner AND the carry. Found by the phase-1f final-partition wave, 2026-08-02, reading `cowork_stage5_fitter_design.md` in full (SIGNED, user, 2026-07-04). NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue).

### D-317 — The backward-walk boundary change is a dead end — do not retry it

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not retry the backward-walk boundary change.** Counting notes that stop exactly where a
>   stretch begins as belonging to that stretch was tried, in the hope of recovering a missing chord
>   root. *Why it is closed:* measured — the notes touching the boundary are OTHER chord tones and the
>   root attacks later, so the change would add the wrong pitches and still not add the missing one;
>   and the same backward walk serves a dozen call sites, several of them notation display, where
>   excluding the previous chord's terminal notes is the correct behaviour. **This is a
>   boundary-membership dead end ONLY.**

**In plain words.** LEGACY (the analyzer awaiting deletion): a one-tick boundary fix was tried and closed - counting notes that stop exactly where a stretch begins as belonging to that stretch, in the hope of recovering a missing chord root. Measured: the boundary-touching notes are other chord tones (the root attacks later), and five display paths depend on the current convention. A boundary-membership dead end ONLY - it says nothing about extending the temporal context the analysis reads, which is a decided live capability (the extensible working span, D-030).

**Why.** Measured and named in the record: the notes that touch the boundary are other chord tones, not the root, which attacks a quarter-note later; and the same walk is used at twelve call sites, five of them notation display, where excluding the previous chord's terminal notes is correct.

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1247-1253`

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/redesign_plan.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02) as a LEGACY-scoped dead end with no effect on the going solution; plain restatement rephrased at the user's direction to preclude the temporal-context misreading. ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched. **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-318 — A short-region external merger is a dead end — do not retry it

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not retry a short-region external merger.** A proposed after-the-fact pass merging very short
>   neighbouring stretches was tried and closed. *Why:* measured — the trigger never fires, because
>   the same-root merge already inside the first pass has combined those stretches before any external
>   pass could see them. It was dead code.

**In plain words.** LEGACY (the segmenter awaiting deletion): a proposed after-the-fact pass merging very short neighbouring stretches was tried and closed - measured, its trigger never fires, because the earlier inline same-root merge has already combined them. A prohibition on re-adding one redundant merger pass - nothing about collecting notes over time or extending context.

**Why.** Measured: the spot-check found zero qualifying runs across all thirteen failing Baroque scores, both target cases included — the trigger was dead code, because the existing same-root inline merge inside the first pass already combines the arpeggio micro-stretches (`docs/redesign_plan.md`, the short-region-merger dead-end block, `cc_phase_d_merger_report.md`).

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1254-1257`

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/redesign_plan.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02) as a LEGACY-scoped dead end with no effect on the going solution; plain restatement rephrased at the user's direction to preclude the temporal-context misreading. ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched. **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-319 — Re-analysing the merged aggregate is a dead end — no tone-aggregation approach fixes the arpeggio root failure

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not retry any tone-aggregation approach to the arpeggio root failure.** Pooling an arpeggio's
>   notes and re-reading the chord from the pool was implemented, measured and reverted. *Why:*
>   pooling makes the answer worse — the aggregate is duration-weighted and the wrong pitch sounds
>   longer than the right one, so the wrong root still wins the pooled reading, and the run regressed
>   both presets. **The evidence was never the problem:** the vertical scorer already prefers the
>   correct root over the stretch where that root actually sounds; what is wrong is the predecessor
>   signal.

**In plain words.** Pooling an arpeggio's notes and re-reading the chord from the pool was implemented, measured, and reverted: pooling makes the answer worse, because the wrong note sounds for longer than the right one. The evidence was never the problem.

**Why.** Measured with the full implementation in place: on the two target scores the wrong root still wins the aggregate by 0.15 and 0.225, because the aggregate is duration-weighted and the wrong note carries 720 ticks against the root's 480; the run regressed both presets and was reverted (`cc_phase_d_merger_report.md` Part B+). The vertical scorer already prefers the correct root in the stretch where that root actually sounds.

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1258-1264`

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/redesign_plan.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched. **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-320 — The absent-root guard is REVERTED and must not be retried — 'absent root means wrong reading' is false corpus-wide

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not retry the absent-root guard.** A rule rejecting any chord whose own root is not sounding
>   was built, measured and reverted entirely. *Why:* it fixed fewer cases than it broke, and two of
>   the cases it broke are readings the published human analysis itself makes with an absent root — so
>   **the premise "an absent root means a wrong reading" is false corpus-wide.** A second, structural
>   reason rides with it: any guard that changes a committed root changes the predecessor every later
>   stretch reads, so its effect cascades into regions it never judged. The counts are in the record
>   and are not restated here (D-431).

**In plain words.** A rule that rejected any chord whose own root is not sounding was built, measured, and removed entirely. It fixed two cases and broke four, and the premise behind it is false across the corpus: sometimes the published human analysis names a chord whose root is not sounding.

**Why.** Measured: two fixed against four broken, two of the four being readings the ground truth itself makes with an absent root, and two further cascade regressions from propagating the changed root forward. The cascade is structural — any guard that changes a committed root changes the predecessor every later stretch reads.

**Status.** LIVE · decided 2026-06-08 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1265-1271`

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/redesign_plan.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched. **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-321 — Winner selection compares candidate scores exactly, with no epsilon anywhere in the ranking

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> Winner selection compares candidate scores with **exact `double` comparisons — there is no
> epsilon anywhere in the ranking.** The final per-bass comparator (`harmonicfunctionlayer.cpp`,
> `applyHarmonicFunction`) is, in order:
>
> 1. `a.score != b.score` → higher `score` wins (exact inequality on the raw `double`);
> 2. else lower `tiePriority` wins (`tiePriority` is the template index — see §2 ordering);
> 3. else lower `rootPc` wins.
>
> This is fully deterministic **given identical floating-point evaluation**: the same inputs
> on the same build always produce the same winner. The `tiePriority`-then-`rootPc` keys
> resolve genuine exact score ties (identical PC sets across enharmonic templates, e.g.
> Sus4♭5 ordered before HalfDim). The omission of an epsilon is intentional — an epsilon
> would make the order depend on a threshold that is itself uncalibrated, and would mask
> rather than resolve near-ties.

**In plain words.** Two candidate readings are ordered by comparing their numbers exactly, with no tolerance band; exact ties are broken by a declared order. This is deliberate.

**Why.** Stated with its reason at the home: a tolerance band would make the order depend on a threshold that is itself uncalibrated, and would hide near-ties instead of resolving them. The tie-break keys resolve the genuine exact ties that arise between enharmonically identical readings.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:212-225`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“Floating-point tie policy”** — `### Floating-point tie policy` (heading at line 210). A delegation at CLAUDE.md:989 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

### D-322 — Any change to optimization flags or to the order of the scoring arithmetic requires a full corpus A/B on both presets

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> These could **flip** under any change that re-associates the floating-point arithmetic:
> different compiler / optimization flags (`-ffast-math`, `/fp:fast`, FMA contraction),
> a different platform's libm, or a reordering of the summation in the score expression
> `(basisIndep + bassDep) × complexityFactor × augFactor + wComplete + wSeq [+ wDim] [+ step]`.
> Treat the exact evaluation order as load-bearing: **any change to optimization flags or to
> the order of the scoring arithmetic requires a full corpus A/B on both presets** before it

**In plain words.** Because candidate scores are compared exactly, re-ordering the arithmetic or changing compiler optimization settings can flip a reading that was decided by a hair. Such a change is not trusted to leave the output unchanged until it has been checked against the whole corpus on both tuning presets.

**Why.** Grounded in two named near-tie classes that sit within a hair of each other — the roughly 0.02-margin class and one score at 1.92 against 1.90 — either of which flips under a re-association of the score expression.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:233-238`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“Floating-point tie policy”** — `### Floating-point tie policy` (heading at line 210). A delegation at CLAUDE.md:989 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

### D-324 — Retirement of a post-scoring rule is global — a rule still doing work on any one preset is retained for all

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

>   Baroque but 18 load-bearing Jazz firing sites, §1.2). Retirement is global, so a rule live on ANY
>   carrier is retained.

**In plain words.** A correction rule is either removed everywhere or kept everywhere. If it still changes an answer under any one of the tuning presets, it stays.

**Why.** Applied in the ratified retirement audit: four rules were retired only after each was shown to change zero winners on all three presets and to be output-identical when removed, while four others were retained precisely because they remained load-bearing on at least one preset.

**Status.** LIVE · decided 2026-07-05 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:921-922`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§6a. The unified promotion primitive `promoteToWinner()`”** — `### §6a. The unified promotion primitive `promoteToWinner()`` (heading at line 800). A delegation at CLAUDE.md:989 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

### D-325 — A correction rule that changes a committed chord's identity is retired or folded in BEFORE the search is widened past it

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **A correction rule that can change a committed chord's IDENTITY is retired or folded in BEFORE
>   the search is widened past it.** Where a later rule can change which root, quality or bass was
>   committed, that rule is removed or absorbed into the scoring first; only then may the search be
>   allowed to consider more alternatives. *Why:* stated with the decision — a rule that mutates
>   root, quality or bass feeds the backward-looking evidence, so it cannot be cleanly separated from
>   a wider-beam decode; a wider search would be reading a predecessor a later step is still going to
>   change. The alternative — searching against uncorrected identities with a documented re-decision
>   — was considered and not taken.

**In plain words.** Where a later correction can change which chord was committed, that correction is removed or absorbed into the scoring before the search is allowed to consider more alternatives — otherwise the search would be reading a predecessor that a later step is still going to change.

**Why.** Stated with its reason at the home: a rule that changes a committed root, quality or bass feeds the backward-looking evidence, so it cannot be cleanly separated from a wider search. The alternative — searching against uncorrected identities with a documented re-decision — was considered and not taken.

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1070-1077`

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/decoder_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §8, which exists to collect this document's standing constraints and dead ends, in that document's own voice, with its defense and with the alternative the record says was considered and not taken. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/decoder_design.md:675-678`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 644, "section": "## 13. Open Questions — DECIDED (Cowork ratification, 2026-06-12)", "label": "§13", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "  **DECIDED (Cowork ratification, 2026-06-12):** (a) — identity-mutating gates are
  retired/folded BEFORE the beam widens past them; **3.4 leads 3.2 for those gates** (a
  gate that mutates root/quality/bass feeds backward edges, so it cannot be cleanly
  separated from a wider-beam decode). §12 sequencing note updated to match." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-326 — The chord-path search emits the whole path with every stretch's alternatives and margins, not the committed reading alone

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **The chord-path search emits the WHOLE PATH with every stretch's alternatives and its margins —
>   not the committed reading alone. ⚠ LEGACY / DORMANT, and the dormancy is stated with the rule
>   rather than left to be inferred.** The search hands forward, per node, the chosen reading
>   together with the readings it beat and by how much. *Why:* it is the evidence-forwarding
>   principle applied to the search's own output surface — the function layer above **consumes the
>   alternatives**, so a search that published only its winner would make that selection impossible;
>   the committed reading is the first element of the path by construction, so nothing is lost by
>   publishing the rest. **The mechanism it governs is the dormant staging described above** — the
>   search is not wired, and what becomes of this decoder is open at the retirement map. The rule is
>   recorded here because this section specifies the carry the search would publish into, and a
>   shelved mechanism's rules still belong at the section that owns the mechanism.

**In plain words.** The search hands forward, for each stretch, the chosen reading together with the readings it beat and by how much — because the layer above chooses among them.

**Why.** Stated at the home as the evidence-forwarding principle applied to the search's own output: the function layer consumes the alternatives, and the committed reading is the first element of the path by construction.

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1964-1974`

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/decoder_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that the Layer-4 section describes this search as dormant staging. The user ruled that this is THE SEARCH'S OUTPUT-SURFACE CONTRACT and homes at Layer 4, WITH THE DORMANCY STATED BESIDE IT — a shelved section can be a home, because shelving is a status and not a kind. Written into the Layer-4 section in that section's own voice, with its defense and with the dormancy stated in the same breath rather than left to be inferred. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/decoder_design.md:694-695`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 644, "section": "## 13. Open Questions — DECIDED (Cowork ratification, 2026-06-12)", "label": "§13", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "  **DECIDED (Cowork ratification, 2026-06-12):** emit the full path + per-node alternatives
  + margins (evidence-forwarding) — Stage 6 functional labeling consumes the alternatives;" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-327 — The root-continuity guard reads the reconstructed inversion credit, superseding the designed sounding-third test

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **★ THE DECISION, STATED AS SUCH — the RECONSTRUCTED-CREDIT read is the ratified form of this
> guard, and the originally designed literal sounding-third test is NOT what shipped (re-homed into
> this specification 2026-08-07 on the user's ruling). ⚠ LEGACY subject — the vertical scorer this
> guard belongs to is dormant on both production surfaces.** Gate R asks whether the candidate earned
> **any inversion credit at all**; it does not test directly whether the candidate's third is
> sounding. *Why:* the derivation is the paragraph immediately above and is not repeated (#6) — the
> two tests are provably equivalent everywhere except on Diminished, where the direct test would be
> wrong because the only credit a Dim candidate can earn additionally requires stepwise-bass
> evidence, a temporal condition no vertical test can see. Reading the pipeline's own reconstructed
> credit is therefore the faithful execution of the redesign's intent rather than a compromise, and
> it is what closes the cross-layer dependency the redesign set out to remove. The originally
> designed mechanism text is retained above **for the record**, and a future reader must not mistake
> it for the shipped behaviour.

**In plain words.** The guard that withholds the continue-the-same-root reward asks whether the candidate earned any inversion credit at all, rather than testing directly whether its third is sounding. The two agree everywhere except on diminished chords, where the direct test would be wrong.

**Why.** Derived, not assumed: under the guard's only firing conditions the bass-root bonus is necessarily zero and the smallest inversion bonus strictly exceeds the largest penalty, so the old test fires exactly when no inversion credit was earned. The direct sounding-third test diverges on diminished chords, whose only credit additionally requires stepwise bass — a condition no vertical test can see — producing an output-visible swing.

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:425-437`

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/decoder_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was the two-candidate one D-490 carries. The user ruled THE SCORING-SURFACE RULE: rules, policies, falsifications, dead ends, promotion carries and retirement conditions of the legacy scoring surface home in `docs/scoring_model.md` — the governing document for the scoring pipeline and a mandatory read for scoring sessions, which is criterion C4 at the reader's actual location — with LEGACY and DEFERRED markings riding along unchanged. Written into §4, immediately beside the Gate R block that specifies the guard, in that document's own voice; the derivation already stated there is POINTED AT and not repeated (#6), and the ⚠ LEGACY subject is stated with it. The edit is ADD-ONLY: no existing line of `docs/scoring_model.md` is modified or deleted. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/decoder_design.md:408-416`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 385, "section": "### §6 amendment — Gate R reconstructed-credit (2026-06-12, Stage 3.3 implementation)", "label": "“§6 amendment”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Ratified form (Cowork, 2026-06-12).** Gate R reads the **pipeline-reconstructed full
basisDep** (`cell.basisDep + fn::inversionContextBonus(...)`, which Pass A computes for the
score anyway) via the 3-arg `gateRZeroesRootContinuity` overload. This is byte-identical to
the old proxy on every quality (it reads the same total credit), is fully intra-layer
(closes the cross-layer dependency the redesign set out to remove — audit Finding 6), and
has no Dim gap. The "direct pcWeight third" mechanism was an approximation of the proxy's
true semantics (`cappedInv == 0`); reading the true semantics is the faithful execution of
the redesign's *intent*. The originally designed mechanism text is retained above for the
record but is not what shipped." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-328 — A wider search cannot fix the arpeggio root failure — the wrong reading IS the global optimum, so only re-weighting or joint segmentation can

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **A WIDER SEARCH CANNOT FIX THE ARPEGGIO ROOT FAILURE — the wrong reading IS the global optimum.
>   Recorded dead end; do not retry.** On the arpeggiated-harmony failures the locally wrong reading
>   is not a weak transient a broader search would discard: it is the best-scoring node, so a broader
>   search finds exactly what the narrow one found. Only **re-weighting** or a **different
>   segmentation** can reach it. *Why:* derived from the search lattice and verified three times,
>   including against an independent earlier derivation — on the founding score the continued-root
>   path outscores the correct path, the gap being the root-continuity reward minus the margin, and
>   the premise the earlier verdict rested on (that the transient scores low) is **measured false**.
>   This is the dead end the two *tried and closed — do not retry* lists in `ARCHITECTURE.md` name;
>   they point here and the rule is published once (#6).

**In plain words.** On the arpeggio failures the locally wrong reading is not a weak transient that a broader search would discard: it is the best-scoring reading, so a broader search finds exactly what the narrow one found. Fixing it needs different weights or a different segmentation, not a wider search.

**Why.** Derived from the search lattice and verified three times, including against an independent earlier derivation: on the founding score the wrong path scores 5.775 against the correct path's 5.600, the gap being the continuity reward minus the margin. The premise the earlier verdict rested on — that the transient scores low — is measured false.

**Status.** LIVE · decided 2026-06-13 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:1079-1088`

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/decoder_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1860 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*; the search (at line 315 on 2026-08-03), under *"Tried and closed on the search — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-329 — Completeness of the candidate list is the priority — a chord never listed can never be chosen

⚠ **LEGACY IN ITS LETTER — TRANSFERRED IN ITS PRINCIPLE.** The text of this decision belongs to the dormant pipeline awaiting deletion at the retirement map, and goes with it. Its principle does NOT: a ruling carried that across to the live design, and the plain restatement below names the ruling. Read it before concluding this decision lapsed (marking convention user-ratified 2026-08-02).

> 1. **List the possible chords.** From the slice's pitches, generate **every** tertian chord the pitches could spell —
>    each basic type at each root — and score each by how well the pitches fit it. **Completeness is the priority:** a
>    chord never listed can never be chosen, and the measured dominant error is "the right chord was never on the list,"
>    not "the wrong one was picked among good options." The fit measure is the one stated in §5 (present chord tones
>    credited; absent ones a mild shortfall; extra notes carried to the membership decision, not penalised as wrong

**In plain words.** LEGACY (the per-slice chord decoder awaiting deletion) IN ITS LETTER, LIVE IN ITS PRINCIPLE: for each stretch the analysis first generates every chord the sounding notes could spell, and only then chooses among them. Leaving a chord off the list is the error that matters most, because nothing downstream can recover it. The letter — this listing step of the dormant Layer-4 decoder — goes with that decoder. The PRINCIPLE was transferred to the live joint estimator by the user's OI-275 ruling (2026-08-02, reading 1-with-transfer): candidate admission complete by default, and any prune derived from the model, measured for established loss, and ratified. So this entry is LEGACY-marked for where its text lives, and it is at the same time the family design's ratified admission premise — the marker below must not be read as retiring the principle.

**Why.** Measured: the dominant remaining error is that the right chord was never on the list, not that the wrong one was picked among good options — which is why complete listing is chosen over a strong re-ranker on a cheap partial list, and why a learned re-ranker is a later refinement over the complete list, never a substitute for it.

**Status.** LIVE · decided 2026-06-24 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer4_chordsymbol_design.md:208-212`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. Solution strategy` (heading at line 204). A delegation at ARCHITECTURE.md:1858 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ TRANSFER RULING (user, 2026-08-02, OI-275 reading 1-with-transfer): the PRINCIPLE binds the joint estimator's family design - candidate admission complete by default, any prune derived, measured for established loss, and ratified (the factorization's own reserve clause); the document's letter stays home to the legacy scorer. D-329 is the family design's ratified admission premise (OI-215/226/227/228/243/244).

### D-330 — Never a pooled recompute — the chord is never re-derived from several stretches' notes thrown together

> - **Never a pooled recompute** (the authoritative statement of this prohibition). Membership is judged per slice
>   against the prevailing chord; the layer never pools several slices' pitches into one bag and re-derives a chord from
>   the bag — that over-reads, treating every passing note as a chord tone, and was the failure that motivated the
>   rebuild (§13). The note model stays the lossless source so membership is decided from the real notes, not a lossy
>   aggregate.

**In plain words.** The analysis never gathers the notes of several consecutive stretches into one bag and reads a chord off the bag. Each note's membership is judged in its own stretch against the prevailing chord.

**Why.** Named as the failure that motivated the rebuild: pooling over-reads, because every passing note enters the bag and inflates the chord. Keeping the note model as the lossless source means membership is decided from the real notes rather than from a lossy aggregate.

**Status.** LIVE · decided 2026-06-24 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer4_chordsymbol_design.md:394-398`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8** — `## 8. Crosscutting concepts` (heading at line 386). A delegation at ARCHITECTURE.md:1858 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-331 — Every chord decision carries its ranked alternatives and its confidence — committed, inherited, and abstained alike, never pruned

>   carries its ranked `alternatives` (together with the prevailing chord) and its `confidenceModel` on **every**
>   decision — Commit and
>   Inherit included, filled before the trichotomy and never pruned — so Layer 5 overrides **by selecting among the readings
>   this layer carried** (never by re-deriving), and the carried confidence is the quantity its override threshold scales

**In plain words.** Whatever the chord layer decides for a stretch, it carries the readings it did not choose and how sure it was. That carry is what lets the layer above correct a decision by choosing among readings rather than working the notes out again.

**Why.** Verified at the source when the overturnable-commit principle was ratified: the carry is filled before the commit/inherit/abstain choice is made and is never pruned, which is what makes the override safe, and the carried confidence is the quantity the override threshold scales against. A lock-in test pins the carry.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer4_chordsymbol_design.md:576-579`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§15** — `## 15. Open items & deferred refinements` (heading at line 559). A delegation at ARCHITECTURE.md:1858 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-332 — A carried alternative's added notes are marked UNKNOWN rather than asserted absent — never synthesized

> `extensionsKnown` = true); a carried *alternative*'s extensions are copied from the scorer's own ranked result where
> that cell produced one, else left **honest-carry** (extensions = 0, `extensionsKnown` = **false** — the seventh is
> *unknown*, never asserted absent, and never synthesized). A Layer-5 consumer reads the extensions only when

**In plain words.** When the chord layer carries a reading it did not choose, it states its added notes (the seventh, ninth and so on) only where they were genuinely worked out. Otherwise it says they are unknown — it never claims there are none, and never invents them.

**Why.** The information-loss principle applied to the carry: an unknown that is recorded as an absence would be read downstream as a fact. A consumer reads the added notes only when they are marked known and otherwise stays at triad level, so an honest gap is a coverage limit rather than a wrong answer.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer4_chordsymbol_design.md:366-368`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§7** — `## 7. Data design` (heading at line 349). A delegation at ARCHITECTURE.md:1858 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-333 — The membership tie-break's direction is an idiom-calibrated number, never a branch on style — the three-tier structure is fixed

>   **idiom-calibrated** (the style-only-in-calibration contract, ARCHITECTURE.md §2.15) — record the threshold as a
>   preset/idiom constant at the precision phase (§0), never a structural branch. Source: `cowork_architecture_review_2026_07.md` §7 (F-12, A-10).

**In plain words.** How a note that steps on one side only is judged depends on the style: in chorale writing an accented foreign note is usually a real chord note, in late-romantic writing it usually is not. That difference is carried as a number set per idiom, never as a separate code path per style; the three-tier rule itself does not vary.

**Why.** Grounded in the external architecture review's late-romantic simulation, which found that long accented appoggiaturas are the norm in that idiom, so the same weight evidence should lean the other way — and in the standing contract that style lives only in calibration.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer4_chordsymbol_design.md:606-607`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§15** — `## 15. Open items & deferred refinements` (heading at line 559). A delegation at ARCHITECTURE.md:1858 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-334 — The bare-fifth chord type stays in the catalogue structurally; whether it wins is an idiom-calibrated number

>   honest quality-abstention reading for genuinely third-less textures — E-14 zero information loss), and its
>   **competitiveness is an idiom-calibrated constant** (`kPowerChord3PcPenalty` — the Stage-5 manifest already
>   declares it idiom-varying), never a structural per-idiom branch: a large idiom-#2 value effectively yields the
>   dyad to context-completed triads, a small idiom-#4 value lets C5 stand. **Measured support (Stage-5 Phase 2.1,

**In plain words.** Whether a root-and-fifth with no third counts as a chord is a question music theory itself answers differently by style. The pattern therefore stays available to every style, and how strongly it competes is set per idiom rather than switched on and off by style.

**Why.** Grounded in the theory both ways — common-practice theory requires three pitches for a chord while popular practice treats the power chord as a standard label — and measured: the fit's feasible direction on the Bach data raises the penalty, aligning with the common-practice answer, while the blocked direction gains root agreement only because the objective is quality-silent and adds meaningful functional errors.

**Status.** LIVE · decided 2026-07-05 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer4_chordsymbol_design.md:617-620`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§15** — `## 15. Open items & deferred refinements` (heading at line 559). A delegation at ARCHITECTURE.md:1858 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-378 — Re-deciding a chord under a different tonality is well-defined ONLY on the decoder path — the legacy multi-pass emission cannot be faithfully re-decoded, and a naive re-emit injects a measured ~6 % same-tonality root-flip artifact

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **Faithfulness (the J-key-iii constraint, discharged).** J-key-iii deferred the chord axis because a *faithful*
> per-region re-emission "cannot reproduce the multi-pass pipeline chord" — the legacy production chord is emitted
> mid-pipeline (before Pass-3 tone merging), so a naïve re-emit injects ~6% same-key root-flip artifact `[code]`
> (`regionanalyzer.cpp:388-393`). The **faithful mechanism it named is the engaged `ChordSliceDecoder`**: a **pure
> function of (slices, key)**, so re-decoding under a different key is well-defined and reproducible — no multi-pass
> artifact. **This is why the joint step is E4-adjacent** (§4): it builds on the engaged decoder, not the retiring
> legacy `analyzeChord` seam. On the legacy path a faithful re-decode does not exist; on the decoder path it is
> the decoder's own contract.

**In plain words.** Asking what chord the analysis would name if the tonality were different is a meaningful question only where the chord decision is a pure function of the notes and the tonality. On the older multi-stage path it is not: the chord is emitted part-way through, before a later merging step, so simply re-emitting it produces about six per cent of root changes that have nothing to do with the tonality at all. On the decoder path the same question is well defined and reproducible, because answering it is what that decoder's own contract already promises.

**Why.** Measured: the naive re-emit's artifact rate on the older path is stated as about six per cent of same-tonality root flips, cited at the orchestrator source that records the deferral. The record uses it to discharge a deferral made earlier by name — the earlier wiring deferred the chord axis for want of a faithful mechanism, and this identifies that mechanism as the engaged decoder rather than declaring the problem solved.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_joint_key_chord_design.md:173-180`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§2.2 The chord re-decoded under each carried key”** — `### §2.2 The chord re-decoded under each carried key (the OWED axis)` (heading at line 164). A delegation at cowork_engage_arc_plan.md:44 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_joint_key_chord_design.md` IN FULL. The step the document designs is shelved (**D-278**); this statement is about the two code paths and not about that step. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-380 — The carry's meaningful axis is DISTINCT ROOTS, and every above-threshold root is carried at graded confidence — a carry of winner-plus-one discards the third root on about a quarter of slices

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> The decisive fan-out finding `[data]`: a **≥3rd distinct root clears threshold on 25.1 % / 16.1 % / 24.9 %** of
> slices. This is exactly the **load-bearing exclusion tail** (#12, finding-by-exclusion): the ruled-out and
> low-confidence roots are **information**, not noise — they are where selection (§3) and the eventual joint step
> (§4.3) earn their keep. The contract therefore requires: **carry every above-threshold distinct root, each at its
> graded confidence; carry ruled-out roots at low confidence rather than dropping them.** A carry that surfaces only
> the winner + one alternate (the legacy cap-of-3 + single diff-root append) **discards the ≥3rd root on ~¼ of
> slices** — a #12 violation the engaged carry must not inherit.

**In plain words.** What one stretch of music offers is many candidate spellings of very few chord roots: measured, about five candidate readings but only about two distinct roots. So what is handed forward is a distribution over distinct roots, each with its best voicing, its variant set, and its own confidence. A third distinct root passes the bar on roughly a quarter of stretches, and those ruled-out and low-confidence roots are information, not noise — they are where the later selection and any tonality-chord coupling earn their keep. A carry that offers only the winner and one alternative throws the third root away on a quarter of stretches.

**Why.** Measured on the corpus: per competing stretch the above-threshold set is wide in readings but narrow in roots — median five, four and five readings against median two, one and two distinct roots — and a third distinct root clears the bar on 25.1 %, 16.1 % and 24.9 % of stretches. The record names the principle it serves: principle #12, finding by exclusion — a ruled-out possibility is carried at low confidence rather than dropped.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_engagement_design.md:136-142`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§2.2 The exclusion tail is load-bearing and must be carried”** — `### §2.2 The exclusion tail is load-bearing and must be carried (#12)` (heading at line 135). A delegation at ARCHITECTURE.md:2018 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer5_engagement_design.md` IN FULL. The document's banner records `Status: DESIGN (CC, 2026-07-07)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-CLASSIFIED contract-home 2026-08-02 (CC, phase 1j, under the TRANSITIVE-AUTHORITY refinement of the fifth home case, user 2026-08-02): `cowork_layer5_engagement_design.md` carries a status banner and its authority is the user's transitively — the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arc #9 to it by name (`:41`), arc #11 to it by name (`:46`), and states that the Stage-3 build inventory 'is enumerated at `cowork_layer5_engagement_design.md` §9.2' (`:53-55`). The missing `ARCHITECTURE.md` delegation pointer — the gap the ruling says a missing delegation owes — was written into the Layer-5 section in the same commit.

### D-381 — The carry must cap on DISTINCT ROOTS, not on voicings — the existing voicing-keyed cap gives no structural guarantee that a third root survives

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **The owed guarantee (structure only; R5).** The engaged carry must **preserve distinct roots explicitly**, not as
> a by-product of a voicing cap. The declared *shape*: a **distinct-root-first carry** — for each distinct root above
> threshold, carry its best voicing + its variant set + its confidence, and cap on **distinct roots** (with each
> root's own variant depth bounded), rather than capping on a flat voicing list. The exclusion tail (#12) is carried
> as the low-confidence roots below the primary set. **The exact cap depths (how many distinct roots, how deep each
> root's variant set) are precision-phase constants (R5)** — the fan-out distribution (p90 ≈ 4 roots, max 11)
> informs the *floor*, but the value is fitted later, not here. This is an **owed change to the decoder's carry
> construction** (Layer 4 / E4), named here so the engagement design and E4 agree on the contract; it is not built
> in this pass.

**In plain words.** The limit on how many alternatives are kept counts spellings, not roots, so the allowance can be used up entirely by inversions and template variants of the top two roots before a third root is reached. Keeping a third root is therefore a by-product rather than a guarantee. The shape owed is the other way round: for each distinct root above the bar, carry its best voicing, its variants and its confidence, and set the limit on the number of roots, with each root's variant depth bounded separately.

**Why.** A structural argument, and the record says so explicitly rather than claiming a measurement: the limit being keyed on voicings is what makes the guarantee absent, independently of how many voicings the current limit happens to admit — a count the record notes was not separately measured on that path. The measured fan-out informs only the floor for the eventual limit; the value itself is left to the fitting phase, not chosen here.

**Status.** DEFERRED · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_engagement_design.md:164-172`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§2.3 Does the decoder's governed carry provide this? The distinct-root guarantee is OWED [code]”** — `### §2.3 Does the decoder's governed carry provide this? The distinct-root guarantee is OWED [code]` (heading at line 144). A delegation at ARCHITECTURE.md:2018 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer5_engagement_design.md` IN FULL. Recorded as an OWED change to the chord layer's carry construction, named so that the engagement design and the later build agree on the contract, and explicitly not built in that pass. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-CLASSIFIED contract-home 2026-08-02 (CC, phase 1j, under the TRANSITIVE-AUTHORITY refinement of the fifth home case, user 2026-08-02): `cowork_layer5_engagement_design.md` carries a status banner and its authority is the user's transitively — the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arc #9 to it by name (`:41`), arc #11 to it by name (`:46`), and states that the Stage-3 build inventory 'is enumerated at `cowork_layer5_engagement_design.md` §9.2' (`:53-55`). The missing `ARCHITECTURE.md` delegation pointer — the gap the ruling says a missing delegation owes — was written into the Layer-5 section in the same commit.

### D-385 — Pedal-point detection's home is DECIDED: a reader over the chord layer's carry that annotates a carried reading — never a second analysis that overwrites the winner

> - **Home: a reader over the decoder's Layer-4 carry, emitting a pedal-annotated result — an additive annotation on
>   a carried reading, NOT a mutation of the winner.** Because the material it needs is the carry's distinct-root
>   distribution (§6.2), and chord identity is Layer 4, the reader sits at the **carry side (Layer-4 output / a
>   decoder post-reader)** and feeds L5 selection *one* pedal-annotated candidate. It never owns `results.front()`
>   and never writes back into the decoder's scoring — it reads the carry forward and annotates.

**In plain words.** Deciding that a SUSTAINED NOTE is a pedal - that the real harmony is the chord moving against it - is a chord-identity question, so the detector sits on the chord layer's output side, reading what that layer already carried. THE PEDALED NOTE CAN BE IN ANY VOICE: the bass pedal is the classic case, but the ratified pedal-point class is voice-independent (D-207), and this entry's home decision - an ADDITIVE reader that marks one carried reading as the pedal reading - applies unchanged whichever voice holds the note. It never takes ownership of the winning reading, never writes back into the scoring, and never replaces the set of alternatives; the original reading survives at its own confidence. (The source document's own wording says 'bass' - the legacy-era default; the voice-independent scope is the ruled one, user 2026-08-02 with D-207.)

**Why.** Grounded in what the material actually is: a pedal stretch's notes are the sustained bass together with the chord above it, so the upper-voice reading — root not the bass, template excluding the bass note — is already one of the distinct-root alternatives the carry holds, and the confirmation margin the old code computed by hand is already the carry's own ranking. The record does not assume the equivalence: whether the carried alternative agrees with today's bass-stripped second analysis is flagged as an owed corpus measurement, and the fallback if it does not is named — still a carried attribute, still never a mutation.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_engagement_design.md:410-414`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§6.3 Placement”** — `### §6.3 Placement (#7): a reader-over-carry producing a distinct pedal-annotated result` (heading at line 406). A delegation at ARCHITECTURE.md:2018 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer5_engagement_design.md` IN FULL. Part 1 of the same document had left the home open as a hinge; Part 2 records that it decides it. The build is separately hard-gated on the owed measurement being settled on an established pedal-dense corpus ([[OI-4]]). NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RATIFIED (user, 2026-08-02) with the plain restatement rephrased at the user's direction: the pedaled note can be a note OTHER than the bass - the voice-independent class (D-207) governs; the home decision (additive reader, never an overwriting second analysis) is unchanged by which voice holds the pedal. ★ RE-CLASSIFIED contract-home 2026-08-02 (CC, phase 1j, under the TRANSITIVE-AUTHORITY refinement of the fifth home case, user 2026-08-02): `cowork_layer5_engagement_design.md` carries a status banner and its authority is the user's transitively — the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arc #9 to it by name (`:41`), arc #11 to it by name (`:46`), and states that the Stage-3 build inventory 'is enumerated at `cowork_layer5_engagement_design.md` §9.2' (`:53-55`). The missing `ARCHITECTURE.md` delegation pointer — the gap the ruling says a missing delegation owes — was written into the Layer-5 section in the same commit.

### D-386 — No fourth hand-rolled scan for the best different-root alternative — the pedal reader consumes the carry's own ranking, or the one unified primitive

> The confirmation margin (§6.1 (ii)) is the **"best different-root alternative"** decision the audit catalogues as
> computed 4× (`[audit §1.3]`, FQ-1). Under the engaged carry it is served two-ways-that-are-one: the decoder already
> **reads** the best different-root reading from its carry (`chordslicedecoder.cpp:927-930` `[code]`), and FQ-1
> unifies that scan into one primitive (`[audit]` FQ-1, sequenced into E4 — Stage-1 STOP-reported the four legacy
> scans are *not* byte-identically one, so the unification lands with the decoder, not pre-L5). The pedal reader
> therefore **consumes the carry's distinct-root margin** (or the FQ-1 primitive over the carry) — it adds **no fourth
> scan**. This is the concrete pedal instance of Part 1 §2.2's load-bearing exclusion tail: the ≥2nd distinct root's
> carried confidence *is* the pedal confirmation signal.

**In plain words.** Finding the strongest alternative with a different root is a decision the code already makes in four separate places. The pedal reader adds no fifth: it reads the margin straight off the ranked distinct roots the chord layer already carried, or through the single shared routine that unification replaces the four with. The second-strongest root's carried confidence is the pedal confirmation signal. RULING (user, 2026-08-02, OI-278): the SECOND alternative — 'the one unified primitive' — is STRUCK: measured at the code not to exist (the four scans it presumed one were never one decision, D-403). The FIRST alternative stands: the pedal reader takes its margin from the ranked distinct roots the chord layer already carries.

**Why.** It is principle #6 applied to a duplication the structural audit catalogued and counted: four copies of the same different-root decision. The record also states why the unification lands with the decoder rather than before it — an earlier stage reported that the four existing scans are not byte-identically the same routine, so folding them is a change that must ride the decoder's own build.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_engagement_design.md:445-452`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§6.5 The diff-root need is served by the carry / FQ-1”** — `### §6.5 The diff-root need is served by the carry / FQ-1 — do NOT re-implement a 4th scan (#6)` (heading at line 444). A delegation at ARCHITECTURE.md:2018 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer5_engagement_design.md` IN FULL. The unification it defers to is tracked as [[OI-11]]. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ FLAG (CC, 2026-08-02, the phase-1i full read of `cowork_structural_integrity_audit.md`): the SECOND alternative this entry offers — 'through the one unified primitive' — was measured at the code NOT to exist. The four different-root scans are not one decision (divergent predicate: root-only at three sites, root+quality at the fourth; divergent element type and result-use), and the promote-to-front primitive is not the vehicle; the unification was reported as a STOP and declared for an adjudication the record does not show being made (**D-403**; rowed [[OI-278]]). The FIRST alternative — reading the margin off the carry's own ranking — is untouched. Recorded as a flag, not as a status change: the entry is not withdrawn and nothing is inferred about what replaces the second alternative. ★ ANNOTATED (user ruling 2026-08-02, OI-278): the second alternative struck (D-403's measurement); the first alternative is the decision's operative content. ★ RE-CLASSIFIED contract-home 2026-08-02 (CC, phase 1j, under the TRANSITIVE-AUTHORITY refinement of the fifth home case, user 2026-08-02): `cowork_layer5_engagement_design.md` carries a status banner and its authority is the user's transitively — the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arc #9 to it by name (`:41`), arc #11 to it by name (`:46`), and states that the Stage-3 build inventory 'is enumerated at `cowork_layer5_engagement_design.md` §9.2' (`:53-55`). The missing `ARCHITECTURE.md` delegation pointer — the gap the ruling says a missing delegation owes — was written into the Layer-5 section in the same commit.

### D-402 — The inversion-append is a pure cap artifact that dissolves when the cap is removed; the below-threshold bass promotion is a targeted promotion that stays

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **One honest discrimination (a true cap-artifact vs a legitimate targeted promotion):** Iter 91 (#6) uses
> `kPromoteAppendOnly` with `stopBelowThreshold=false` — it can pull a **below-threshold** bass-rooted target.
> That reach is **not** dissolved by uncapping-at-threshold; it is a genuinely different, deliberate targeted
> promotion (it wants a specific structural target regardless of score). So: the **inversion-append (#4) is a
> pure cap-artifact that dissolves**; Iter 91's below-threshold pull is a targeted promotion that stays. This
> is exactly the VIOLATION-vs-legitimate line the audit must draw.

**In plain words.** The legacy chord path keeps at most three readings per stretch, and a patch was added to reach past that limit and re-insert the best reading with a DIFFERENT root, which the limit was routinely crowding out. Removing the limit makes that patch dead code by construction, because an uncapped build already pushes every above-threshold reading in score order — so limit and patch cancel. One thing does NOT cancel with them: the separate promotion that can pull a bass-rooted reading scoring BELOW the threshold, which wants a specific structural target regardless of score and therefore survives the uncapping as a deliberate rule in its own right.

**Why.** Derived from the code and then measured, not assumed: the append only ever pulls a candidate already at or above the threshold, so an uncapped threshold-only build is a strict superset of what the append can add (§1.2, cited to `harmonicfunctionlayer.cpp:521-547`); and the workaround is load-bearing rather than an edge case — it fires on 36.2 % of Baroque and 36.1 % of Default regions (§1.5, measured over all three per-preset corpora, and declared a floor because the untruncated candidate set is not serialized).

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_structural_integrity_audit.md:87-92`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§1.2** — `### 1.2 The cap→append chain — dissolution hypothesis TESTED at code (CONFIRMED)` (heading at line 69). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**.

**Provenance.** Found by the phase-1i continuation wave, 2026-08-02, reading `cowork_structural_integrity_audit.md` IN FULL. The document's banner records `Status: read-only grounded catalogue (CC, 2026-07-07; Engage arc #6)` — an authored catalogue, not a ratified contract. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1i ratification queue. The same section states the consequence that keeps this from being a free edit: removing the cap changes the SERIALIZED carry, which is a behavior change on `.ours.json` bytes and therefore a ratified adoption under the robust-stop explained-diff and re-baseline discipline (`CLAUDE.md` gate block (A)). Nothing was changed. ★ RATIFIED (user, 2026-08-02, the phase-1i queue). ★ NO DELEGATION IS DRAFTED OR WRITTEN FOR THIS DOCUMENT, AND THAT IS A RULING (user, 2026-08-04, ruling R3, dispatch `cc_instruction_census_delegation_and_commit.md`): this entry stays `gap` deliberately. Its home section §1.2 reports the result of a test run against the code, and the register's own `not_write_list_cases` already rules on that shape — 'A delegation cannot repair that; the remedy is the same as OI-290's — at the document, or by homing those verdicts where the concern is owned.' THE REMEDY IS AT THE DOCUMENT and is not a delegation act. NOT A DEFERRAL: no later wave owes a delegation here.

### D-403 — STOP, not forced: the four best-different-root scans are NOT one decision at code, so the one-decision-four-sites premise over-counts

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **FQ-1 — ⛔ STOP-and-reported (not forced).** At code the four scans are NOT one decision: divergent
>   "differs" predicate (rootPc-only #1/#2/#3 vs `sameChordSymbol` = root+quality #4), element type, and
>   result-use; no byte-identical single primitive exists and `promoteToWinner` (promote-to-front of a
>   *specific* target) is not the vehicle. The "one decision, four sites" premise over-counts at code
>   granularity — declared for Cowork adjudication (report §5).

**In plain words.** The audit had catalogued the search for the strongest reading with a different root as one decision implemented in four places, and queued unifying it as the first portable win. Executing that found the premise false at the code: the four sites do not even ask the same question — three compare roots alone while the fourth compares root AND quality — and they differ in what they operate on and what they do with the answer, so no single primitive reproduces all four unchanged. The unification was reported as a stop rather than forced through, and left for adjudication.

**Why.** Measured at the code during the attempt, and named site by site: the differing predicate (root-only at three sites versus same-chord-symbol at the fourth), the differing element type, and the differing use of the result; and the vehicle proposed for the unification, the promote-to-front primitive, does something else (it promotes a SPECIFIC target to the front) so it cannot carry the scan.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_structural_integrity_audit.md:265-269`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§3.1** — `### 3.1 Stage-1 build status (Engage arc #7, 2026-07-07 — `cc_engage_pre_l5_refactor_report.md`)` (heading at line 251). A delegation at cowork_engage_arc_plan.md:4 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it RECORDS FINDINGS**.

**Provenance.** Found by the phase-1i continuation wave, 2026-08-02, reading `cowork_structural_integrity_audit.md` IN FULL. The document's banner records `Status: read-only grounded catalogue (CC, 2026-07-07; Engage arc #6)` — an authored catalogue, not a ratified contract. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1i ratification queue. The record says this was 'declared for Cowork adjudication (report §5)' and the adjudication is not recorded anywhere this pass read — rowed at [[OI-278]]. It bears on **D-386**, which permits the pedal reader to take its margin either from the carry's own ranking or 'through the one unified primitive': the first alternative stands, the second was measured not to exist at code, and D-386's own record does not say so. ★ RATIFIED (user, 2026-08-02, the phase-1i queue). ★ THE DECLARED ADJUDICATION IS NOW MADE (user, 2026-08-02, OI-278 option (a)): FQ-1 LAPSES WITH THE LEGACY PATH — the four-sites-one-decision premise is measured false, three of the four sites retire at the OI-180 map, and the live concern (the pedal reader's input) is served by D-386's first alternative. The measurement stands as this entry's content (#12); no unification is built.

### D-423 — The gate-retirement stage is the only sanctioned way the post-scoring gates change, and three do-not rules hold through every stage

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Three prohibitions hold through every stage, and the per-gate RETIREMENT STAGE is the only
>   sanctioned way these gates change:** no new gates, no threshold widening, no gating of the
>   root-continuity bonus. *Why:* each prohibition carries its own defense elsewhere — accumulating
>   gates are a warning sign and the answer is iteration rather than more gates; gate thresholds are
>   Baroque-calibrated and are not loosened for another style; gating the root-continuity bonus on a
>   sparse predecessor was measured a dead end (the bullet above). What this constraint adds is the
>   **single sanctioned channel** — the retirement stage's per-gate differential proof obligation —
>   which is what stops the gate layer changing by accretion.

**In plain words.** LEGACY (the chord analyzer awaiting deletion): three prohibitions hold for the whole programme — no new after-the-fact correction rules, no widening of a threshold, and no gating of the root-continuity bonus. The only sanctioned way any of those correction rules changes is the deliberate per-rule retirement stage, where a rule is removed only once the replacement reproduces the fixes it was pinned to.

**Why.** Each prohibition carries its defense elsewhere in the register rather than here: accumulating gates are a warning sign, and the answer is iteration rather than more gates (D-036); gate thresholds are calibrated against the Baroque corpus and must not be loosened for another style (D-061); gating the root-continuity bonus on a sparse predecessor was measured a dead end (D-215). What this statement adds is the single sanctioned channel — the retirement stage's per-gate differential proof obligation (`:414`) — which is what stops the rules changing by accretion.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/scoring_model.md:1090-1097`

**Provenance.** `docs/implementation_roadmap.md`:520-521, in the closing section relating the roadmap to the earlier phase plan, stated as remaining "in force through all stages". No date or ratifier is stated. Its subject is the legacy vertical scorer's post-scoring gate layer, dormant on both production surfaces since 2026-07-26/27, hence the LEGACY mark; the three underlying prohibitions (D-036, D-061, D-215) carry their own scopes. The natural home is `docs/scoring_model.md` §8, where the other standing constraints and dead ends on that layer live, hence the documentation-gap flag. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §8 — three gate prohibitions plus the retirement stage — in that document's own voice, with its defense, and the ⚠ LEGACY marking riding along unchanged as the ruling requires. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/implementation_roadmap.md:609`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 602, "section": "## Relationship to the existing phase roadmap (COWORK_HANDOFF \"Roadmap\")", "label": "“Relationship to the existing phase roadmap”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- The "do not" rules (no new gates, no threshold widening, no rcb gating) remain in force
  through all stages; Stage 3.4 is the only sanctioned way gates change." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-463 — The temporal signals sitting in the vertical scorer are left where they are, and the gate that depends on them must move with them

> - **The temporal signals sitting inside the vertical scorer STAY WHERE THEY ARE, and the gate that
>   depends on one MOVES WITH THEM.** Several signals that look backward or forward in time are
>   computed inside the part of the scorer that is supposed to judge only what sounds at one moment.
>   They are known, documented debt and are **not** to be moved before a scoring-stabilisation phase;
>   when they do migrate, Gate R has to move or adapt **simultaneously**. *Why:* stated with the
>   recommendation and grounded in the mechanism — Gate R's test uses a score component as a stand-in
>   for *this candidate has a sounding third*, and it carries that meaning only because one of those
>   signals is computed where it is. Removing the debt without touching the gate would silently
>   change what the gate tests: a cross-layer dependency invisible to anyone reading the gate's own

**In plain words.** Five signals that look backward or forward in time are computed inside the part of the scorer that is supposed to judge only what sounds at one moment. They are known debt and are not to be moved yet. When they are eventually moved, the gate whose test depends on one of them has to be changed at the same time.

**Why.** Stated with the recommendation and grounded in the mechanism the audit traced: the gate's test uses a score component as a stand-in for "this chord has a sounding third", and it only carries that meaning because one of the five signals is computed where it is. Removing the debt without touching the gate would silently change what the gate tests — a cross-layer dependency invisible to anyone reading the gate's own file.

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1099-1107`

**Provenance.** `docs/layer_architecture_audit.md` Finding 1, an audit written 2026-06-09 and marked superseded only FOR LAYER 1 by the note-model rebuild; this finding is about the chord scorer and is untouched by that supersession. Entered by the phase-1 reads wave 1. Whether the five signals are still where the audit found them was NOT re-checked at the code by this wave. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §8: the temporal signals stay in the vertical scorer and the dependent gate moves with them, which is a standing constraint on this document's own subject. Written in that document's own voice and with its defense. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/layer_architecture_audit.md:65-67`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 40, "section": "## Finding 1 — Oracle temporal contamination (pre-existing, self-documented)", "label": "“Finding 1”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Recommendation:** This debt is stable, documented, and will not be removed until a
scoring stabilisation phase. Do not attempt to move these signals now. When they do
migrate, Gate R needs to move or adapt simultaneously." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-464 — No further progression-level signal may be added to the single-step look-around structure; it goes in the progression context instead

> - **No further PROGRESSION-LEVEL signal may be added to the single-step look-around structure; a
>   progression-level signal goes into the progression-level structure directly.** The struct
>   specified above is a one-step look-around — the immediate previous and next harmonic positions.
>   Four fields describing the previous winner's competition outcome were added to it that belong to
>   the planned progression-level structure instead; **nothing further of that kind goes in**, and
>   the migration of those four is planned **explicitly** when the progression analyzer's design
>   begins, not left to happen. *Why:* stated with the recommendation and grounded in this
>   document's own instruction that the two structures are kept distinct — the finding is that one
>   had been growing into the other with no migration plan written down, which is how a boundary
>   disappears without a decision.

**In plain words.** The structure that carries a chord's immediate neighbours was designed as a one-step look-around, and four fields describing the previous winner's competition outcome were added to it that belong to a planned progression-level structure instead. Nothing further of that kind goes in, and the migration of the four is to be planned explicitly when the progression analyzer's design begins.

**Why.** Stated with the recommendation, and the ground is the canonical specification's own instruction that the two structures are to be kept distinct — the audit's finding is that one has been growing into the other with no migration plan written down.

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:4316-4325`

**Provenance.** `docs/layer_architecture_audit.md` Finding 5, 2026-06-09. Entered by the phase-1 reads wave 1. Whether the four fields are still in that structure at HEAD was NOT re-checked by this wave. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that the rule's other half concerns a planned progression-level structure that has no section. The user ruled that THE PROHIBITION BINDS THE STRUCTURE §5.3 SPECIFIES, and that the redirect half states where new signals go instead — which is what the home text does, without claiming a section for the planned structure. Written into §5.3 in that section's own voice, with its defense. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/layer_architecture_audit.md:186-189`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 167, "section": "## Finding 5 — `ChordTemporalContext` struct boundary (architectural)", "label": "“Finding 5”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Recommendation:** At the start of Phase E (when `ProgressionAnalyzer` design begins),
plan the migration of these four Step 2 fields from `ChordTemporalContext` to the new
`TemporalContext` explicitly. Do not add further progression-level signals to
`ChordTemporalContext`; put them in `TemporalContext` directly." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-465 — The policy for judging a proposed post-scoring gate: another bias correction gets the bias fixed first, a structural condition is sound, and a cascade means the missing thing is functional context

> - **The policy for judging a PROPOSED post-scoring gate — three tests.** (1) If the proposal is
>   another variant of correcting the bass-as-root bias, first ask whether the bias itself can be
>   reduced, or whether functional context would remove the ambiguity; add the gate only if the fix
>   is genuinely local. (2) If it turns on a **structural** condition — pitch-class arithmetic plus a
>   presence constraint, not temporal evidence — it is likely architecturally sound. (3) If it needs
>   the three-step cascade shape, that is a strong signal that the real problem is missing functional
>   context, and the gate is the wrong answer. *Why:* derived from a systematic read of the whole
>   gate population — two thirds of the gates were solving one problem, the scorer's bass-as-root
>   pull, and three separate cascades were each built up step by step for the same shape of failure,
>   which the canonical specification already names as the warning sign that accumulating gates
>   signal an unresolved architectural problem. The two gates that read came out architecturally
>   healthier both turn on structural conditions rather than compensating for the bias, which is
>   where test (2) comes from.

**In plain words.** Three tests decide whether a proposed gate should be added. If it is one more variant of correcting the scorer's pull toward reading the bass as the root, first ask whether the pull itself can be reduced or whether functional context would remove the ambiguity — add the gate only if the fix really is local. If it turns on pitch arithmetic and what is present rather than on what came before or after, it is likely sound. And if it needs the whole three-step cascade shape, that is a strong sign the real problem is missing functional context.

**Why.** Derived from the audit's own catalogue: two thirds of the post-scoring gates are solving one problem, the scorer's bass-as-root pull, and three separate cascades were each built up step by step for the same shape of failure — which the canonical specification already names as a warning sign that accumulating gates signals an unresolved architectural problem. The two gates the audit calls architecturally healthier both turn on structural conditions rather than compensating for the bias, which is where test two comes from.

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1110-1122`

**Provenance.** `docs/layer_architecture_audit.md` Finding 7, added 2026-06-09 after a systematic read of every gate. Entered by the phase-1 reads wave 1. The gate population has moved since (the scoring model records Gates B/C/D as retired and subsumed, and CLAUDE.md records Gate K retired by user ruling 2026-08-02), so the POLICY is entered and none of the audit's gate inventory is; the policy's own do-not-add-more-cascade-gates conclusion stands on the same page. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §8 — the three-test policy for judging a PROPOSED post-scoring gate — in that document's own voice and with its defense, which is the systematic read of the whole gate population the policy was derived from. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/layer_architecture_audit.md:404-413`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 394, "section": "### What this means for future gate decisions", "label": "“What this means for future gate decisions”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**The policy for new gate decisions:**
1. If a proposed gate is another variant of the bass-as-root bias correction (e.g. a
   new enharmonic pair, a new interval relationship) — consider whether the bias itself
   can be reduced first, or whether Phase E can provide the functional context that
   removes the ambiguity. Only add the gate if the fix is genuinely local.
2. If a proposed gate has a structural condition like Gate J or Gate R (specific
   pitch-class arithmetic + presence constraint, not temporal evidence) — it is likely
   architecturally sound.
3. If a proposed gate requires the cascade pattern (temporal B-style → C-style → D-style)
   — this is a strong signal that the underlying problem is missing Phase E context." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-467 — A rebuilt or re-tuned chord scoring must not rely on the held-note repetition bonus the faithful note model removed

> **★ A REBUILT OR RE-TUNED CHORD SCORING MUST NOT RELY ON THE HELD-NOTE REPETITION BONUS THE FAITHFUL
> NOTE MODEL REMOVED (re-homed into this specification 2026-08-08 on the user's ruling).** Before the
> note reader was rebuilt, a note held across a tie was counted more than once, and that spurious extra
> weight happened to push a handful of ambiguous sonorities toward the correct root. The faithful note
> model removed the duplication. **Whatever replaces or re-tunes this layer's scoring must not lean on
> that boost to get those cases right.** *Why:* measured when it surfaced — removing the inflation
> moved a small number of cases the wrong way while the key axis stayed flat, which is what identified
> those cases as having been carried by an artifact rather than by evidence; a correct re-calibration
> is expected to recover them on real evidence. It is exactly the hidden dependency the upstream-first
> rebuild exists to surface. **Whether those cases have since recovered is NOT stated here and was not
> checked** — the constraint binds regardless, because it forbids leaning on the artifact rather than
> asserting anything about the current count.

**In plain words.** Before the note reader was rebuilt, a note held across a tie was counted more than once, and that spurious extra weight happened to push a handful of ambiguous sonorities toward the right root. The faithful note model removed it. Whatever replaces or re-tunes the chord scoring must not lean on that boost to get those cases right.

**Why.** Measured and recorded when it surfaced: removing the inflation moved a small number of cases the wrong way while the key axis stayed flat, which is what identified those cases as having been carried by an artefact rather than by evidence. The document names this as exactly the hidden dependency the upstream-first sweep exists to surface — a correct re-calibration is expected to recover them.

**Status.** LIVE · decided 2026-06-21 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1862-1873`

**Provenance.** `cowork_target_architecture.md` §6.2, recorded 2026-06-21 and citing the Layer-1 implementation report §5.3 as its measurement. Entered by the phase-1 reads wave 1. Whether the ~4 cases have since recovered was NOT checked by this wave. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). ★ ASSUMPTION A4 DISCHARGED BY READING, AND THE ANSWER IS DEMOTED RATHER THAN SUPERSEDED: `ARCHITECTURE.md:502-504` states that `cowork_target_architecture.md` is *"**demoted** to the detailed-rationale reference for those contracts … not a second canonical doc"* and that *"When any doc disagrees with this one, this one wins"*. Demotion is not supersession — the document is retained as the rationale reference — and this entry's content is not one of the cross-cutting contracts it holds the rationale for: it is a measured forward constraint on chord scoring, carried by no other home. It is therefore LIVE and is homed. Routed to the Layer-4 section of `ARCHITECTURE.md`, the layer whose scoring it constrains, immediately beneath that section's tried-and-closed list, with the not-checked clause carried across so no reader takes it for a claim about the current count. FORMER HOME, PRESERVED (#12): `cowork_target_architecture.md:357-358`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 353, "section": "### 6.2 Layer 3 — the analysis (the only place judgment lives)", "label": "§6.2", "delegated": null, "delegation": "ARCHITECTURE.md:861", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**When layer-3 scoring is rebuilt/
  re-tuned, do NOT rely on the held-note repetition bonus**" — note that its *layer-3* is the TARGET architecture's numbering, whose analysis layer is this specification's Layer 4, which is why the home is the chord layer and not the key layer. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-501 — A tool may read a written chord symbol ONLY as a comparison or ground-truth label — never as input that influences what the analyzer computes

> 2. **A written chord symbol in the score may be read ONLY as a comparison or ground-truth label.**
>    Symbols are instructions the user wrote, not analysis results. **Production paths must not read
>    them as input to analysis at all.** A measurement tool may set them beside the analysis to see
>    how far the two agree, and may **never** let them influence what the analyzer computes. *Why:*
>    stated with the principle — a symbol is user content and may be wrong, so reading it as input
>    makes the analysis agree with the user rather than with the music; and in a measurement tool it
>    additionally destroys the measurement, because the tool would then be comparing the annotation
>    with itself.

**In plain words.** Chord symbols printed in a score are instructions the user wrote, not results. Production analysis may not read them at all. A measurement tool may put them beside the program's own answer to see how far the two agree, but it may not let them change what the program computes.

**Why.** Stated with the principle: a symbol is user content and may be wrong, so reading it as input makes the analysis agree with the user rather than with the music — and in a measurement tool it additionally destroys the measurement, because the tool would then be comparing the annotation with itself.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1419-1426`

**Provenance.** The user's operating principle, quoted verbatim at the head of the symbol-input audit and applied as its classification criterion. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) **D-066** and **D-305** carry the production ban; this entry carries the TOOL clause, which is what the audit's categories B and C are graded against and what its category-C resolution (recorded in the audit's closing status line and registered as **D-067**) discharged by deleting the tool-side symbol paths. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that the rule also binds MEASUREMENT TOOLS, which no `ARCHITECTURE.md` section governs. The user ruled it ONE boundary invariant binding every reader INCLUDING measurement tools, homed at §3.3 beside D-280, with `BUILD_AND_TEST.md` gaining a POINTER beside the tool contracts — which it now carries, as a pointer and not a copy (#6). Written into §3.3 in that section's own voice and with its defense; the two invariants are stated with their difference (what a scoring change may READ, versus what any path may read a written symbol AS) so neither is taken for the other. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/symbol_input_audit.md:15-18`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 3, "section": "## Context", "label": "“Context”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "> Symbols are instructions written by the user, not analysis results.
> Production paths must not read them as input to analysis. Tools may
> read them only as comparison/ground-truth labels — never as input that
> influences what the analyzer computes." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-510 — The correct carry is the one that keeps the distinct alternative reading, not the one that appends a near-duplicate of the winner — chosen on the carry's purpose, not on which code is at HEAD

> - **Which carry is correct is decided on the carry's PURPOSE, not on which code happened to be at
>   HEAD: the correct carry is the one that KEEPS the distinct alternative reading.** Two promotion
>   idioms were in use — one swaps a reading already carried in `results[]` to the front, leaving the
>   displaced reading in place; the other builds a fresh copy and appends it. The swap idiom is
>   correct. *Why:* argued from what the carry is FOR, and the design says so in terms — the
>   alternatives exist so the later layer can select among the **distinct** readings, and a copy of
>   the winner is not a distinct reading. Measured on the full output surface across the whole
>   corpus, the append idiom injects that near-copy and displaces the genuinely different partner,
>   which is an information-loss regression under #12. The same principle is already applied
>   elsewhere in this layer, where a non-promoting raw pull is popped so it does not pollute the
>   list. This is explicitly **not** "prefer the idiom that is at HEAD".

**In plain words.** Two ways of promoting a chord to winner were in use. One swaps an alternative already on the list to the front and leaves the displaced reading in place; the other builds a fresh copy and appends it. Measured, the second injects a near-copy of the winner into the alternatives and pushes out the genuinely different reading. The first is therefore the correct behaviour to unify on.

**Why.** Argued from the carry's stated purpose rather than from incumbency, and the document says so in terms: the alternatives exist so that the later layer can select among the DISTINCT readings, and a copy of the winner is not a distinct reading — its presence loses the partner reading, which is an information-loss regression under #12. The same principle is already applied elsewhere in the code, where a non-promoting raw pull is popped so it does not pollute the list.

**Status.** LIVE · decided 2026-07-06 · ratifier not stated

**Home.** `docs/scoring_model.md:831-841`

**Provenance.** The grounded verdict of the Gate-A unification design, measured on the FULL output surface across the whole corpus. Its evidence is the enumerated affected stems and the before/after carry content, which the document nominates as the user-ratification surface under #14. The carry contract it is grounded in is **D-312**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §6a, the section that specifies the unified promotion primitive, in that document's own voice and with its defense — including the explicit statement that the carry was chosen on its PURPOSE and not because one idiom was at HEAD. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_gateA_unification_design.md:184-189`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 170, "section": "### 3.1 Which carry is correct — grounded, not assumed", "label": "§3.1", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Grounded verdict: C_HEAD is the correct carry.** It is the same principle the code already applies at the
Gate G-E raw-pull, where a non-promoting pull is popped so it *"does not pollute results[]"*
(`postscoringgates.cpp:388-392`). The correct unification reproduces C_HEAD — it does **not** adopt the
FM2-append form. (This is not "pick Gate A's idiom because Gate A is at HEAD"; it is "pick the carry that
preserves the distinct readings the contract requires, which the swap idiom produces and the append idiom
destroys.")" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-511 — One promotion primitive with a present-first dedup guard replaces the two ad-hoc promotion idioms; the append branch fires only when the target is genuinely absent

> - **ONE promotion primitive, with a PRESENT-FIRST dedup guard — the append branch fires only when
>   the target is genuinely absent.** The ordering is the whole fix: present-first makes an
>   already-carried partner *swapped* rather than *appended*, so no duplicate can enter. *Why:* the
>   design shows the equivalence rather than claiming it — for the enharmonic flip the caller has
>   already computed the in-`results[]` partner index, and the primitive swaps that exact index, so
>   the produced permutation is byte-identical to the behaviour it replaces. That is what makes
>   retiring the separate rule a no-op on the output rather than a change to be argued about.

**In plain words.** Promoting a chord to winner becomes a single shared operation. If the reading is already among the alternatives it is swapped to the front; only if it is genuinely absent is a fresh one built and appended. That ordering is the whole fix, and it reproduces the existing behaviour exactly where the reading is already present.

**Why.** The design shows the equivalence rather than claiming it: the caller already computes the index of the present partner, so the primitive swaps that exact index and the produced ordering is byte-identical to the behaviour it replaces — which is what makes the retirement of the separate rule a no-op on the output rather than a change to be argued about.

**Status.** LIVE · decided 2026-07-06 · ratifier not stated

**Home.** `docs/scoring_model.md:842-848`

**Provenance.** The single unified path of the same design, together with the collapse of three near-identical builder wrappers into one. It is a Layer-4 consolidation under #6 and is explicitly scoped as introducing no new cross-layer dependency. The build event itself is a separate, user-ratified commit that this document does not take. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §6a beside D-510, in that document's own voice and with its defense. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_gateA_unification_design.md:210-215`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 191, "section": "### 3.2 The unified path", "label": "§3.2", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "The **present-first dedup guard** is the whole fix: it makes the append branch fire **only** when the target is
genuinely absent, so an already-carried partner is *swapped* (clean, Idiom A) rather than *appended* (duplicate,
Idiom B). For the enharmonic flip specifically, the caller already computes the in-`results[]` partner index
(`bestAltIdx`, from the clean-quality bestAlt loop, `postscoringgates.cpp:136-187`); the primitive swaps that
exact index — so the produced permutation is **byte-identical to Gate A's `std::swap(results[0],
results[bestAltIdx])`**." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-512 — Gate A becomes removable only once the unified promotion reproduces its carry byte-for-byte — that reproduction IS the retirement condition, not the winner-inertness that preceded it

> - **The retirement condition for the separate Gate A rule is BYTE-FOR-BYTE REPRODUCTION OF ITS
>   CARRY — not the winner-inertness that preceded it.** Once the flip is one promotion call with
>   present-first branching, the former "partner present" and "partner absent" rules are two branches
>   of the same promotion and the separate rule — its enum member, its guard, its name-map entry and
>   its dedicated fixtures — is redundant. It is removable **because** the primitive reproduces the
>   swap byte-for-byte on the present branch, which leaves winner AND carry byte-identical. *Why:*
>   the condition is quoted from the earlier ruling it discharges — the rule retires when the
>   promotion machinery unifies into one path producing one carry — and the design shows why the
>   earlier winner-only inertness was **not** enough: the naive removal was inert on the winner
>   across the whole corpus while changing the carry on a named subset of scores. That gap is exactly
>   why this document's evidence rule is inertness on the **full** output surface, winner AND
>   alternatives, and never the winner alone (#15).

**In plain words.** The rule could not simply be deleted: deleting it left the winner unchanged but changed the alternatives on a number of scores. It is removable once the shared promotion produces exactly the same alternatives, at which point exactly one rule name survives for the flip.

**Why.** The condition is quoted from the earlier ruling it discharges — the rule retires when the promotion machinery unifies into one path producing one carry — and the design shows why the earlier winner-only inertness was not enough: the removal was inert on the winner across the whole corpus while changing the carry on a named subset. That gap is the reason the full-surface evidence rule exists.

**Status.** LIVE · decided 2026-07-06 · ratifier not stated

**Home.** `docs/scoring_model.md:849-860`

**Provenance.** The retirement analysis of the same design. The binding evidence-method rule the document states for itself — inertness is measured on the full output surface, winner AND alternatives, never the winner alone — is the project's principle #15 applied here, and this case is where it earned its keep. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §6a beside D-510 and D-511 — the retirement condition belongs where the primitive that satisfies it is specified — in that document's own voice and with its defense, which is why this document's full-output-surface evidence rule exists. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_gateA_unification_design.md:233-240`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 231, "section": "### 3.3 How Gate A becomes truly inert and removable", "label": "§3.3", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "Once the flip is one `promoteToWinner` call with present-first branching, **Gate A (the "partner present" half)
and FM2 (the "partner absent" half) are the two internal branches of the same promotion.** The separate `GateA`
rule — its `PostScoringRule::GateA` enum member (`paramoverride.h:75`), its `ruleOff(GateA)` guard
(`postscoringgates.cpp:214`), its name-map entry, and its dedicated fixtures — is redundant: the unified
promotion *is* the flip. Because the primitive reproduces Gate A's swap **byte-for-byte** on the "present"
branch (same `bestAltIdx`, same `std::swap`), removing the `GateA` rule leaves **winner AND carry
byte-identical to HEAD**. That is the condition O-11 named for retirement: *"It retires when the promotion
machinery unifies (one promotion path producing one carry)."* Gate A is then inert on the **full** surface" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-536 — The bass note and the chord are chosen TOGETHER — the winner is the (bass, root, template) triple — replacing the sequential commit-the-bass-then-score pipeline

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **★ THE DECISION THIS SECTION RECORDS, STATED AS A RULE — the bass and the chord are chosen
> TOGETHER, as one (bass, root, template) triple (re-homed into this specification 2026-08-07 on the
> user's ruling). ⚠ LEGACY subject — this scorer is dormant on both production surfaces.** The
> analyzer does **not** commit to a bass and then score chords against it. It enumerates the
> plausible bass candidates and the whole root × template grid against each, and the winner is the
> best **(bass, root, template)** triple under the composite score. *Why:* both defects that forced
> it are diagnosed to the same cause and named with it — a passing note that happens to be the
> absolute lowest pitch wins bass selection over the beat-onset bass a step above it, flipping the
> chord root; and an incomplete slash-chord reading beats a complete root-position triad because
> root-position completeness earned no advantage. **Neither is reachable while the bass is committed
> before the chord is scored**, which is what makes this a structural decision rather than a
> weighting one. The cost is stated with it and judged acceptable: a few times the scoring loop. It
> is the same principle the production estimator carries on its own terms — coupled quantities are
> decided together rather than one being committed early.

**In plain words.** The analyzer used to pick the bass note first and only then score chords against it. Two confirmed misreadings both came from that order. It now enumerates the plausible bass notes and the chord candidates together and takes the best combination.

**Why.** Both defects are diagnosed to the same cause and named: a passing note that happens to be lower wins the bass on absolute pitch regardless of when it entered, flipping the chord root; and an incomplete slash chord beats a complete root-position triad because root-position completeness earned no advantage. Neither is reachable while the bass is committed before the chord is scored. The cost is stated too — a few times the scoring loop, which the document judges acceptable.

**Status.** LIVE · decided 2026-05-16 · ratifier not stated

**Home.** `docs/scoring_model.md:738-751`

**Provenance.** The design of iteration 92, recorded implemented and committed, and named the authoritative reference for the joint formula and its guards. ⚠ Its subject is the LEGACY chord analyzer: the production inference layer on the batch/corpus and notation surfaces is the joint estimator (**D-005**, **D-010**), and this scoring path is reached only through the dormant arm. The principle it embodies — deciding coupled quantities together rather than committing one early — is the same one **D-001** carries for the live design. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §5, the section that specifies the joint (bass, root, template) scoring this decision established, in that document's own voice, with its defense and its ⚠ LEGACY subject. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/iter92_joint_bass_chord_scoring.md:53-68`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 51, "section": "## Design: JOINT (bass, chord) scoring", "label": "“Design: JOINT”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "Replace the sequential two-step with a joint enumeration:

```
for each bass_candidate in bass_register_tones:
    for each (root, template) in 12×16:
        score = base_score(pcWeights, root, template)   // bass-independent matrix
                + bass_delta(bass_candidate, root, template)  // 3 of 7 components
                + w_complete * complete_bonus(bass_candidate, root, template)
                + w_onset   * onset_signal(bass_candidate)
                + w_passing * passing_penalty(bass_candidate)
                + w_stepIn  * stepIn_bonus(bass_candidate, previousBassPc)
                + w_stepOut * stepOut_bonus(bass_candidate, nextBassPc)
        track best (bass_candidate, root, template) triple
```

The winner is the (bass, root, template) triple with highest composite score." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-537 — The completeness bonus fires ONLY for a root-position reading whose three triad tones are all present — the guard that stops it from demoting genuine slash chords

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **★ THE GUARD IS THE DECISION, AND IT IS STRUCTURAL RATHER THAN A THRESHOLD (re-homed into this
> specification 2026-08-07 on the user's ruling). ⚠ LEGACY subject.** The completeness bonus fires
> **only** for a **root-position** reading — the candidate bass IS the triad root — whose three triad
> tones are all present above the presence threshold. A genuine slash chord therefore neither gains
> the bonus nor is beaten by a rival reading that gains it wrongly. *Why:* derived from a measured
> failure rather than chosen. The previous, unconditional version of the same idea caused large
> regressions in both directions because it promoted cases where the slash-chord reading was the
> correct one; the design works the guard through the exact case that failed and shows that a genuine
> slash chord with its own fifth present does not collect the root-position bonus for the rival
> reading. It is an early instance of the standing rule that a correction is given a **structural
> entry condition** rather than a widened threshold (`CLAUDE.md`, the gate and preset policy).

**In plain words.** The bonus that rewards a chord for having all of its notes present applies only when the candidate bass IS the chord's root and all three tones are above threshold. A genuine slash chord therefore neither gains it nor is beaten by a reading that gains it wrongly.

**Why.** The guard is derived from a measured failure rather than chosen: the previous unconditional version of the same idea caused large regressions because it promoted cases where the slash-chord reading was the correct one. The document works the guard through the exact case that failed and shows that a genuine slash chord with its own fifth present does not get the root-position bonus for the rival reading.

**Status.** LIVE · decided 2026-05-16 · ratifier not stated

**Home.** `docs/scoring_model.md:496-506`

**Provenance.** The `w_complete` guard of the same iteration-92 design. ⚠ LEGACY subject, as above. It is an early instance of the standing rule that a correction be given a STRUCTURAL entry condition rather than a widened threshold — the gate policy in `CLAUDE.md`. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §4, which the ruling names — the bonus's own subsection — in that document's own voice, with its defense and its ⚠ LEGACY subject. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/iter92_joint_bass_chord_scoring.md:113-127`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 89, "section": "### JOINT formula weights (calibrated from empirical case data)", "label": "“JOINT formula weights”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "### w_complete guard (prevents Iter 90-style regressions)

The Iter 90 unconditional iii/III flip caused +12/+22 regressions because it promoted
cases where the "complete" triad was genuinely Em/C (correct slash chord) rather than
C major. The `w_complete` guard is more restrictive:

```
complete_bonus applies when:
    distinctPcs >= 3
    AND pcWeight[triad_root] > extensionThreshold
    AND pcWeight[triad_3rd]  > extensionThreshold
    AND pcWeight[triad_5th]  > extensionThreshold
    AND bass_candidate.pc == triad_root
        (root-position reading only — not for slash chord candidates)
```" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-538 — A multi-signal scoring change lands one signal at a time, with the corpus check re-run after each step and any increase in errors a hard stop before the next

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> ## Four-step implementation and validation order
>
> Run corpus check after each step. Each step must not increase total BIR errors before
> proceeding.

**In plain words.** The change was not landed as a whole. Each new signal was added on its own, the corpus was re-measured, and the next signal was only added if the error count had not risen.

**Why.** Stated with the plan and tied to the specific risk it manages: the same document's guard exists because an earlier unconditional version of one signal caused regressions, so the staging is what makes a regression attributable to the signal that caused it rather than to the change as a whole.

**Status.** SUPERSEDED BY D-177 and D-115 · decided 2026-05-16 · ratifier not stated

**Entry ratified.** 2026-08-07 · by user

**Home.** `docs/iter92_joint_bass_chord_scoring.md:190-193`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“Implementation insertion point”** — `## Implementation insertion point` (heading at line 169). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** The four-step implementation and validation order of the same design. ⚠ LEGACY subject. It is an early, concrete form of the discipline the project later stated generally — one revertible provenance-stamped commit per behaviour change (#14) and a measured non-increase before proceeding (the gate block (A) hard stop). Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ RATIFIED AND RULED SUPERSEDED IN THE SAME ACT (user, 2026-08-07, ruling R2, the three-owner-rulings wave). THE SENTENCE IMMEDIATELY ABOVE — 'NOT ratified … goes to the user in this wave's ratification queue' — IS SUPERSEDED BY THIS ACT and is kept only as the record of what the entering wave wrote (#12); the queue it names is the one the user has now answered. The entry is ratified as CORRECTLY RECORDED, and its content is ruled superseded by the general discipline the project later stated — the two successors this field already named before the ruling, and it names them rather than any session nominating them: principle #14, every behaviour change one revertible, provenance-stamped, user-ratified commit (D-177), and gate block (A)'s measured non-increase (D-115). Both are homed in `CLAUDE.md`, so under D-642 the criterion-C1 obligation moves to them and is discharged at their home; NO SPECIFICATION IS EDITED FOR THIS ENTRY, which is the ruling's own point. THE EXCLUDED ALTERNATIVE, RECORDED WITH THE RULING (#12): homing this entry's early concrete form beside gate block (A) would put a second copy of in-force discipline into a live specification (#6), under a ⚠ LEGACY subject a reader could misapply to the live solution. The early concrete form stays in the register verbatim (#12) and the ⚠ LEGACY mark stays. The home, the home class and the verbatim are UNCHANGED by this act.

### D-560 — Voice slots and stem direction are STRUCTURAL notational metadata, not user-written analytical claims, so the analysis may read them

> **★ VOICE SLOTS AND STEM DIRECTION ARE STRUCTURAL NOTATIONAL METADATA, NOT USER-WRITTEN ANALYTICAL
> CLAIMS — SO THIS LAYER MAY READ THEM (re-homed into this specification 2026-08-08 on the user's
> ruling).** Which voice a note was entered in, and which way its stem points, belong to how the
> music was written down — the same category as the key signature, the time signature, a tie or a
> pedal marking, all of which this layer already reads. They are not somebody's claim about the
> harmony. **The analysis may therefore consume them.** *Why:* it is the line the chord-symbol
> prohibition already draws, applied to a new pair of fields — the analysis may read what the score IS
> and may not read what a user has CLAIMED about it — and voice slot and stem direction fall on the
> first side. The rule binds any voice-tracking work whether or not the non-chord-tone detector that
> raised the question is ever built; it decides what such a detector would be ALLOWED to read and
> settles nothing about whether it is built, which is a separate deferral recorded at the chord layer.

**In plain words.** Which voice a note was entered in, and which way its stem points, are part of how the music was written down — the same kind of thing as a time signature or a tie. They are not somebody's opinion about the harmony. So the analysis is allowed to read them, unlike a chord symbol the user typed.

**Why.** The line it draws is the one the chord-symbol prohibition already draws (**D-501**, **D-066**): the analysis may read what the score IS, and may not read what the user has CLAIMED about it. The record places voice slots and stem direction on the first side explicitly, and notes that the existing architecture already consumes notes plus structural metadata of exactly this kind.

**Status.** LIVE · decided 2026-04-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1538-1549`

**Provenance.** `docs/nct_detection_design.md`, the deferred non-chord-tone design; `ARCHITECTURE.md` names the document's existence beside **D-303**, which carries the deferral and the constraint on its shape. This clause is separate from the deferral: it settles what evidence such a detector would be ALLOWED to read, and it binds any voice-tracking work whether or not the detector is built. The record states no ratifier. Read in full by READ WAVE 4, 2026-08-04. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii), which routes this document to *the layer that reads the notation — structural notational metadata*). That layer is Layer 1, the lossless note model: it is the layer that reads the score and already consumes the structural metadata this rule extends. Written into the Layer-1 section in that section's own voice, with its defense stated as the line the chord-symbol prohibition already draws, and with the separation from D-303's deferral stated so no reader takes the rule for a schedule. FORMER HOME, PRESERVED (#12): `docs/nct_detection_design.md:184-189`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 147, "section": "## Voice-leading detection — the piano problem", "label": "“Voice-leading detection”", "delegated": null, "delegation": "ARCHITECTURE.md:1503", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "The structural-data approach is consistent with the analyzer's
existing architecture: it consumes notes + structural metadata
(key signature, time signature, ties, pedal) and infers analytical
content. Voice slots and stem direction belong in the same
\"structural metadata\" category — already in the score, not
user-written analytical claims." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-580 — Two of the twelve post-scoring gates are purely-local vertical refinements and MUST survive the dissolution; the other ten dissolve into the competition

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Two of the post-scoring gates are PURELY-LOCAL VERTICAL refinements and must SURVIVE the
>   dissolution; the others dissolve into the competition. Recorded DEFERRED.** Most of the
>   after-the-fact repair steps exist only because the decision preceding them could not see enough
>   context, and they disappear once that decision can. Two do not: they refine the reading from the
>   notes alone and compensate for nothing, so they are carried across rather than deleted alongside
>   the others. *Why:* measured at the code rather than assumed from the design — of the live gates,
>   ten read context from beyond their own stretch and are compensation by construction, three were
>   already dead code, and the two named ones read nothing outside the sonority. **The dissolution
>   was never executed on this path** — the production estimator replaced the pipeline instead — so
>   the constraint stands DEFERRED and what it says about those two gates is a fact about this code
>   that the retirement map still has to dispose of (#12). One bookkeeping fact a reader needs: the
>   *partner-present* half of one of the two named gates has since been unified into the single
>   promotion primitive (§6a), so the surviving rule name for that flip is FM2; the unification did
>   not perform the dissolution and does not discharge this constraint.

**In plain words.** Most of the after-the-fact repair steps in the old chord path exist only because the decision that preceded them could not see enough context, and they disappear once that decision can. Two do not: they refine the reading from the notes alone and are not compensation for anything. Those two must be carried across, not deleted alongside the others.

**Why.** Measured at the code rather than assumed from the design: of the twelve live gates, ten read context from beyond their own stretch and are therefore compensation by construction, three were already dead code, and the two named ones read nothing outside the sonority. The review records the tally as verified at HEAD.

**Status.** DEFERRED · decided 2026-06-20 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1124-1137`

**Provenance.** `cowork_phase2_architecture_review.md`, the phase-2 architecture review (Cowork-led, reconciled against CC's empirical pass at committed HEAD `a03c2493bb`). Read in full by READ WAVE 4, 2026-08-04. **Its subject is the LEGACY multi-pass pipeline**, which the joint estimator replaced on both surfaces. Recorded as step 5 of the review's fix-first order, gated behind the anchor (**D-579**). **The dissolution was never executed on this path**: the joint estimator replaced the pipeline instead, so the entry is recorded DEFERRED with its subject legacy-marked rather than superseded — what it says about the two gates is a fact about the legacy code that the retirement map still has to dispose of, and #12 keeps it. The record states no ratifier. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md` §8 — which gates survive the dissolution — in that document's own voice, with its defense and with the DEFERRED status riding along unchanged as the ruling requires. One bookkeeping fact is stated with it rather than left to collide with §6a: the partner-present half of one of the two named gates has since been unified into the single promotion primitive, so FM2 is the surviving rule name for that flip; the unification did not perform the dissolution and does not discharge this constraint. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_phase2_architecture_review.md:135-139`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 108, "section": "## §5 — The structural fix-first ORDER (the phase-2 deliverable)", "label": "“§5”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "5. **C2 — dissolve the 10 compensation gates into the competition; PRESERVE Gates A & J [BS, BIG]**
   `[CC-CONFIRMED ~83%]`. Only AFTER the anchor (regions stable + key explicit) — fold the 10 context-reading
   gates into a competition that sees the context up front. **Gates A and J are purely-local vertical and must
   survive** (CC-verified); B/C/D are already dead. The bridge from "patched local decisions" to the joint
   formulation." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-583 — A known deferred loss is KEPT only while it stays characterized EXACTLY, and is re-adjudicated the moment its form changes

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **U2 → KEEP, deferred to the owed joint step (O-18), ON CONDITION it stays characterized EXACTLY.** *"Keep as long as
>   we know exactly what it is."* The exact, standing characterization: on a J-key-iii joint re-key,
>   `region.keyModeResult` is updated but the chord + its `alternatives` are left as Pass-1 artifacts, **not re-ranked
>   under the new key** — a stale-under-new-key chord ranking. This is the architecture-intended future consumer's job
>   (the still-owed joint step); it stays as-is until then. **Not** a should-already gap. (If the joint step's design or
>   this behavior ever changes such that the loss is no longer *exactly* this, re-adjudicate.)

**In plain words.** One loss was left in place deliberately, because the step that will fix it is a planned later piece of work. The condition attached is that its exact shape stays written down — what is stale, under what circumstances, and what is not re-ranked. If the behaviour ever drifts so that the loss is no longer precisely that, the decision to keep it is reopened.

**Why.** Stated with the user's ruling in their own words — keep it as long as we know exactly what it is — and the standing characterization is written out beside it so the condition is checkable. It is what separates a deferral from an unexamined defect: the deferral names its future owner and its exact form, so a later reader can tell whether it is still the thing that was ruled on.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_information_loss_audit.md:152-157`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“The prioritized DEFECT fix-queue”** — `## The prioritized DEFECT fix-queue (each a future separate, ratified, Gate-A-style event)` (heading at line 132). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_information_loss_audit.md`, the engage-arc-#4 information-loss catalogue (Cowork, 2026-07-06; every hit verified at code by CC). Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's adjudication of its item U2, one of three the user ruled the same day (the other two being an uncapping and a queued check). **Its subject is the LEGACY chord path** — the stale-under-new-key ranking after a joint re-key — which the joint estimator replaced; the CONDITION it states is general and is what the entry records.

### D-638 — The symmetric-rotation churn is a chord-layer root ambiguity SURFACED, not caused, by a key change — the proper fix is spelling-aware root selection, never a key-layer change

> Root cause: the rotation churn is a **chord-layer (Layer-4) root ambiguity** *surfaced,
>   not caused,* by a key change; the proper fix is spelling/voice-leading-aware chord-root selection
>   (Layer 4 / Stage 5–6).

**In plain words.** When a change to the key stage makes the analysis flip which note of a symmetric chord it calls the root, the fault is not in the key stage. The chord stage cannot tell those rotations apart from the pitches alone, and the key was only its tie-breaker. The repair belongs to the chord stage, using how the notes are written and how the voices move.

**Why.** It follows from what makes the sonority ambiguous, which the amendment states: a symmetric chord's root is undecidable from pitch class, so the key context was serving as the tie-break and a change to it merely re-rolls a coin the chord stage was never able to call. That is why the tracked class is an interim policy rather than an accepted outcome — it retires when the chord stage can decide the rotation from spelling and voice leading.

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Home.** `CLAUDE.md:826-828`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `CLAUDE.md` gate block (B), the two-tier per-cell class policy, carried over unchanged to the robust unit at R10-b. Its full provenance is `cowork_gate_policy_amendment.md`, read in full by READ WAVE 6, 2026-08-04, whose root-cause-attribution section states the same finding with the four founding cases behind it. **D-191** carries the two-tier policy itself; this is the separate attribution clause it rests on — the reason the tracked class is interim and the reason no key-layer change is the remedy — which D-191's verbatim does not include. Homed at the governing document rather than at the amendment proposal, because that is where the rule binds.


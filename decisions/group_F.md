# Decisions group F — Layer 3 — key and mode

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-051 — The production key/mode path is the sequence decoder, not the per-stretch resolver

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **The production region key/mode path is the decoder, not the per-region resolver.**

**In plain words.** The tonality is worked out for the whole piece at once, as a sequence, rather than separately for each stretch.

**Why.** derivation not recorded.

**Status.** SUPERSEDED BY D-001 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1344`

**Provenance.** The joint estimator now decides key on both surfaces (D-005, D-010). The Layer-3 section still reads 'Built+Live' - see OPEN_ITEMS OI-232

### D-052 — The signature read and declared-mode mapping live in ONE shared function

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> The signature read + declared-mode
> mapping + declared-gated Baroque `partialSignatureCorrection` was lifted verbatim into a shared
> public `resolveKeySignatureContext`, **called by both** the resolver and the wiring — so no
> signature/partial-correction logic is duplicated.

**In plain words.** Reading the printed key signature and turning it into a starting assumption happens in one place that both callers use, so the two cannot drift apart.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1366-1369`

**Provenance.** ARCHITECTURE.md:1291-1296

### D-053 — The tick-local path keeps the older resolver (the ratified P4-defer)

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **P4 tick-local still uses `resolveKeyAndModeRanked` + `collectPitchContext`** (the ratified
>   P4-defer).

**In plain words.** One narrow fallback - answering about a single moment when no surrounding stretch is available - still uses the older method. That was a deliberate deferral.

**Why.** derivation not recorded.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1380-1381`

**Provenance.** On the switched build the note-seam funnel returns from the record arm before this fallback is reachable (notationcomposingbridge.cpp:728-738). The D-P4 revisit trigger (D-063) was never discharged

### D-054 — All 21 modes are scored against all 12 tonics; the harmonic major family is deferred

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> Harmonic major modes are
> significantly rarer as tonal centers than melodic and harmonic minor modes, and the
> validation corpus is unlikely to calibrate them well.

**In plain words.** The key finder considers 21 scale types on each of the 12 possible tonics. The harmonic major family was left out because it is rare and we have no annotated music to calibrate it against.

**Why.** Recorded for the DEFERRAL half only, ARCHITECTURE.md:2459-2463: the harmonic major modes are significantly rarer as tonal centers than the melodic and harmonic minor modes, and the validation corpus is unlikely to calibrate them well. Why the other 21 modes are all scored against all 12 tonics has no recorded derivation.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2547-2549`

**Provenance.** ARCHITECTURE.md:2394-2395 (21 modes), :2213-2217 (harmonic major deferred)

### D-055 — The 21 mode priors are independent and user-configurable

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **21 independent additive priors**, one per mode, user-configurable
>   via `IComposingAnalysisConfiguration::modePrior{ModeName}()`

**In plain words.** How likely each scale type is considered to be is a separate adjustable number per scale type, exposed in the preferences.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2495-2496`

**Provenance.** ARCHITECTURE.md:2408-2410, :3020-3073. Superseded on the production path by D-003 (inference is preset-independent)

### D-056 — Notes always win - the notated key signature is a weak hint, not a bypass

> The key/mode inferrer always runs. The notated key signature's `KeyMode` enum
> (`MAJOR`, `MINOR`, etc.) is no longer a bypass gate — it is passed as a weak hint
> (`declaredMode`) to `analyzeKeyMode()`

**In plain words.** The key printed at the start of the score does not settle the question. It only nudges the answer; what the notes actually do decides.

**Why.** Stated constraint, ARCHITECTURE.md:3382-3384: the notated signature is what the composer wrote down, not what the music does - a piece may modulate, be notated in a partial signature, or contradict its own signature - so it enters as a weak hint the sounding notes can outvote.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3492-3494`

**Provenance.** ARCHITECTURE.md:3380-3392

### D-057 — The priority of evidence - actual sounding notes are the strongest evidence

> | Strongest | Actual sounding notes | what is literally happening now |

**In plain words.** In deciding the key, what is actually sounding right now outranks the surrounding bars, which outrank the printed key signature, which outranks the major/minor tag on it.

**Why.** Stated constraint, ARCHITECTURE.md:3396-3403: the priority table ranks the actual sounding notes the strongest evidence, above the notated signature and above any prior result, for the same reason as D-056.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3510`

**Provenance.** ARCHITECTURE.md:3396-3403. Cited by open_items/OI-228 as the primary source the joint emission departs from. NOT catchable by the harvest's signature net - the reason this adjudication had to read the specifications in full

### D-058 — The piece-start shortcut

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> when the
> analysis tick is within the first 16 quarter-note beats (a separate constant from the 16-beat lookback window below —
> they coincide in value, not by design), no prior result exists (`prevResult == nullptr`),
> and the key signature carries an explicit mode, the function returns the declared mode
> immediately (confidence 0.5) rather than waiting for pitch evidence that cannot yet exist.

**In plain words.** At the very start of a piece there is not yet enough music to judge the key, so if the score declares major or minor the program simply believes it, marked as a middling-confidence answer.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3497-3501`

**Provenance.** ARCHITECTURE.md:3387-3392 calls it 'a deliberate pragmatic choice for the score opening, not a general bypass'. NOT catchable by the harvest's signature net

### D-059 — The temporal window - 16 beats back, 8 beats forward, decayed

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> The bridge uses a 16-beat lookback + 8-beat lookahead window:

**In plain words.** To judge the key at a point, the program looks about four bars back and two bars forward, giving less weight to music further away.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3535`

**Provenance.** ARCHITECTURE.md:3423-3435; legacy-arm only since the switch (D-010). Derivation not recorded: the only stated basis for 16 and 8 is the in-code gloss '~4 measures in 4/4' / '~2 measures ahead' (ARCHITECTURE.md:3428-3429) - no theory citation and no measurement

### D-235 — Tonal-centre disambiguation may break a close tie but may not overturn a stronger raw winner

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> The key-signature path uses a separate focussed `tonalCenterScore` formula for the
> final same-key-signature family decision, independent of the main scoring weights so
> both can be tuned without cross-interference. For diatonic family decisions, tonal-
> centre disambiguation is now guarded by the raw candidate score: it may break close
> same-key-signature ties, but it must not overturn a materially stronger raw winner.

**In plain words.** The same-key-signature family decision is scored by its own formula, separate from the main key weights. On diatonic families that separate decision is allowed to settle a near-tie, but a candidate that already wins the raw scoring by a clear margin stands.

**Why.** The constraint stated in the record: the two formulas are kept independent so both can be tuned without cross-interference; the raw-score guard bounds what the secondary formula may do. The measurement that set the guard's bar is not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:2501-2505`

**Provenance.** ARCHITECTURE.md:2414-2418; the same guard is listed among the key-path scoring terms at :2480-2482 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-287 — Key-as-distribution is SHELVED - its motivating case was already fixed and no live target was found

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> 3. **Key-as-distribution — ⛔ SHELVED.** Motivating case (Corelli op01n08d) already
>    fixed by `81978321e3`. No confirmed live target in corpus. `normalizedConfidence`
>    structurally unreliable as scaling signal. See `docs/redesign_plan.md` §Step 3.

**In plain words.** Carrying a ranked distribution of key candidates forward, instead of one committed key, was withdrawn: the one failure it was designed to fix had already been fixed another way, no other case in the corpus needed it, and the confidence number it would have been weighted by is not trustworthy.

**Why.** Measured and cited in the record: the motivating case (Corelli op01n08d read in G minor instead of C minor) was already fixed by the partial-signature correction `81978321e3`, the resolver returns C minor at rank 0 for every stretch, and no case was found where the correct key sits at rank 1 or 2 (`cc_step3_key_investigation_report.md`). A second reason is recorded beside it: the confidence field is re-ranked without being recomputed, so it reads anywhere from 0.025 to 1.00 on one correctly-keyed piece and cannot scale anything.

**Status.** LIVE · decided 2026-06-08 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_handoff_archive.md:5272`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the redesign-sequence block) and in the 2026-06-08 `STATUS_ARCHIVE.md` entry, both pointing at `docs/redesign_plan.md` Step 3. The shelving names its own re-open condition — a confirmed case where the correct key sits at rank 1 or 2 — so it is a shelving with a stated trigger, not a permanent exclusion. Found by the phase-1e second-partition archive read, 2026-08-02. Note for a future reader: the joint estimator (D-001) carries a full posterior by construction, so the concern this shelving withdrew is met by a different design, not by reviving this one. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-290 — The key-agnostic local cadence approach is FALSIFIED at its precision ceiling

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **★★ CADENCE-PRECISION INVESTIGATION: NEGATIVE — the key-agnostic LOCAL cadence approach has HIT ITS PRECISION CEILING (2026-06-15).**

**In plain words.** Deciding the key from cadences found without knowing the key, one cadence at a time, was tested to its limit and cannot be made accurate enough to use. The remaining errors need either a long-range key decision or a different kind of model - not a better local cadence rule.

**Why.** Measured with a byte-matched reimplementation (the Python re-implementation reproduced the committed analysis exactly on all 326 pieces, so the simulation is trustworthy): the chromatic-leading-tone gate is orthogonal to correctness (about 45 % of true modulations and about 50 % of false ones carry a diatonic leading tone), and the relative-pair signals were already spent by the existing aggregation. Ceiling approximately 50-58 % precision at 18-22 % recall, below the bar the wiring step required.

**Status.** LIVE · decided 2026-06-15 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_handoff_archive.md:3896`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-15 cadence-precision-investigation block), citing `cc_cadence_precision_investigation_dossier.md`. Its scope is stated with it: measured on the Bach ground-truth corpus, non-Bach unmeasured. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-306 — The key layer's backward re-reading stays switched off in the shipped configuration

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **The backward re-reading facility stays SWITCHED OFF in the shipped configuration.** This layer carries a
> facility for returning to an earlier stretch and re-reading it once later evidence has arrived
> (`ReachBackOptions`). It is built, and `enabled = false` is the shipped default; turning it on is reopened

**In plain words.** The key analysis has a facility for going back and re-reading an earlier stretch once later evidence arrives. It is built but switched off, and turning it on is reopened only when a specific piece of evidence has been gathered.

**Why.** Measured and judged insufficient: an A/B run showed the designed effect is material (roughly 35–45 % of interior range queries change, almost all of them anchoring the leading key) but the timing comparison was confounded (one arm cold, the other warm), so the evidence needed to justify switching it on — interleaved timing plus an adjudicated sample of the changed outputs — was named and not yet gathered (`STATUS_ARCHIVE.md:232`).

**Status.** LIVE · decided 2026-07-02 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1335-1337`

**Provenance.** Recorded in `STATUS_ARCHIVE.md` (session 21j). The Layer-3 specification records the reach-back facility but not this shipped-default ruling. Found by the phase-1f final-partition wave, 2026-08-02, reading `STATUS_ARCHIVE.md` lines 119-300 and 930-3,861 in full — the file is now read in full across the phase-1e and phase-1f waves. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written into the Layer-3 section of `ARCHITECTURE.md` §3.3, whose description of the dormant pipeline is the frame this ruling belongs in — the specification recorded the reach-back facility and not the shipped-default ruling, which is the gap the phase-1h note identified. Former home preserved (#12): `STATUS_ARCHIVE.md:232`, session 21j.

### D-323 — Asking whether a pitch belongs to the key is a question about the collection, never about the tonic — the tonic-anchored form must not return

> **⚠ Do not reintroduce `keyTonicPc + scale` for a membership test.** A scale-DEGREE is tonic-relative
> by definition and legitimately uses that pair (`buildChordResult`); a membership question must not.
> Note that `buildChordResult`'s `diatonicToKey` flag and the Gate I / Gate L `invRootIsDiatonic` checks
> (`postscoringgates.cpp`) still answer a *collection* question through the *tonic* pair and so still
> carry the OI-168 defect — they are declared, not fixed (see `OPEN_ITEMS.md` OI-170).

**In plain words.** A test of the form 'is this note in the key' must read the key signature's own collection of notes, never a scale laid out from a tonic. Asking about a scale degree is a different question and may legitimately use the tonic.

**Why.** Measured: until 2026-07-14 both key-consuming scoring terms tested a set built from the mode's own tonic, which equals the signature's collection for nineteen of the twenty-one modes and is a semitone off for two — sharing only two of seven notes there. The correction moved exactly one committed chord and made it agree with the ground truth.

**Status.** LIVE · decided 2026-07-14 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `docs/scoring_model.md:303-307`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“`dim7CharacteristicBonus`”** — `### `dim7CharacteristicBonus` — `kDim7CharacteristicBonus = 0.75`` (heading at line 246). A delegation at CLAUDE.md:698 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

### D-343 — The key/mode layer owns the candidate space and the note-evidence model outright; the residual is SELECTED from its carried alternatives, never re-scored

> Architectural Layer 3 owns two things outright: the **candidate space** (the 252 key/modes) and the
> **note-evidence model** — how well each candidate fits the pitch content and the sequence. No other architectural layer
> infers key/mode from the notes, and no other architectural layer generates or re-scores key/mode candidates. What
> Architectural Layer 3 does **not** own is the *final arbitration of the cases the notes alone cannot decide* (relative
> major versus minor; a modulation/tonicization seam): that residual — handed forward as the ranked alternatives plus the
> "uncertain" mark — is settled by Architectural Layer 5 using **functional evidence** (chord, cadence,
> function) that Architectural Layer 3 structurally cannot have. So key/mode inference is split along an **evidence
> boundary**: Architectural Layer 3 contributes the note evidence and resolves everything the notes can resolve; the
> gated step — Architectural Layer 5's carried-readings resolution, entered under the conditions its own spec states
> (`cowork_layer5_function_design.md` §5.5) — contributes the functional evidence and resolves only the flagged
> residual — by **selecting among
> Architectural Layer 3's carried alternatives**, never by inventing a candidate or re-scoring from the notes (that
> note-evidence model has exactly one home).

**In plain words.** Working out the tonality from the notes happens in exactly one place: that stage owns the list of possible tonalities and the model of how well each fits the notes, and no other stage infers a tonality from the notes or generates or re-scores a tonality candidate. What the notes cannot settle — relative major against relative minor, and where one tonality gives way to the next — is handed on with the ranked runners-up, and the later function stage settles it by choosing one of those runners-up, never by inventing a candidate or scoring the notes again.

**Why.** The record gives the reason with the decision: the split follows an evidence boundary — the later stage has functional evidence (chord, cadence, function) that the note stage 'structurally cannot have', and the note-evidence model 'has exactly one home' (principle #6, one path per concern). The passage cites the open item that settled who resolves the residual: O1, resolved and user-ratified 2026-06-24, evidence `cowork_uncertain_resolver_investigation.md` (`cowork_layer3_keymode_design.md:73-76`).

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:60-72`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§1** — `## 1. Introduction & purpose` (heading at line 52). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-344 — A scale outside the twenty-one recognized modes is reported as the best-fitting recognized mode, never as the unrecognized scale

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **Which key/modes Architectural Layer 3 does NOT recognize.** Any scale that is **not** one of those 21 seven-note
> modes — in particular pentatonic and blues scales, the whole-tone scale, the octatonic (diminished) scale, and any
> non-Western or microtonal scale (maqam, raga, and so on). A passage genuinely in one of these is reported as the
> **best-fitting** of the 21 recognized modes — the candidate with the highest local-fit score under the §5 sequence
> decision, not by any separate scale-distance measure — never as the unrecognized scale itself.

**In plain words.** Music written in a scale the analysis does not know — pentatonic, blues, whole-tone, octatonic, or any non-Western or microtonal scale — is reported as whichever of the twenty-one recognized modes fits the notes best, chosen by the ordinary whole-run decision rather than by any separate similarity measurement. The unrecognized scale is never named as such.

**Why.** derivation not recorded

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:129-133`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§1** — `## 1. Introduction & purpose` (heading at line 52). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`, and the banner adds that the conditional sign-off was met by stating the recognized mode vocabulary explicitly — this passage is the other half of that statement. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-345 — The style preset first enters the analysis at the key/mode layer, as a deliberately weak prior over the modes that the note evidence overrides

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **This is the first architectural layer where the user's style preset (Standard / Baroque / Jazz / …) is used.**
>   Architectural Layers 1 and 2 are pure facts and use no preset. The preset enters here as a **weak prior on which
>   of the 21 modes are likely in this style** — the per-mode bias values in the scorer (Baroque pushes the prior
>   toward major and minor; Jazz raises the modal and altered modes; "Standard" sits between). It is deliberately
>   weak: the note evidence is primary and overrides it, so the preset only tips genuinely ambiguous cases (the same
>   stance taken toward the written key signature). The preset is used again in later architectural layers (chord
>   symbols, function); this layer is only where it *first* applies.

**In plain words.** The user's style setting has no effect on reading the notes or cutting the music into stretches; the first place it acts is the tonality decision, where it nudges which of the twenty-one modes are expected in that style. The nudge is deliberately small: the notes decide, and the setting only tips cases the notes leave genuinely open.

**Why.** The record gives the reason in the same passage: the note evidence is primary and overrides the prior, so the setting only tips genuinely ambiguous cases — the same stance the layer takes toward the written key signature (`cowork_layer3_keymode_design.md:156-158`).

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:153-159`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. Constraints` (heading at line 138). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. **Flagged in the phase-1h report as an instance of the [[OI-275]] question** — it sits against **D-003** (inference is preset-independent; presets are presentation concerns), and the record contains no ruling that names either statement against the other. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RATIFIED (user, 2026-08-02) UNDER THE OI-275 TRANSFER TREATMENT, as offered with the queue and adopted in the blanket ratification: the letter (the preset as a weak mode prior) stays home to the LEGACY Layer-3 path, LEGACY-marked; the live estimator is governed by D-003's measured preset-independence. The second instance of the OI-275 governing question, treated identically.

### D-346 — The candidate set for the whole-run tonality decision is the UNION of every stretch's best candidates, made available at every stretch

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **The candidate set for the sequence decision (the as-built rule,
>    verified at `keymodesequence.cpp` `buildLattice`):** take each slice's top-K best-scoring candidates, and form the
>    **union of those top-K sets across all slices** (plus any pinned candidates a sub-range re-decision must keep,
>    §5's last paragraph); every candidate in that union is then available **at every slice**. This is how the
>    established key survives a brief excursion: a key that made the top K anywhere in the run remains selectable at
>    the slices where it locally scored below the top K, so the change cost — not candidate elimination — decides
>    whether the excursion switches the key. *(A per-slice alternative — explicitly injecting only the incumbent
>    decoded key into each slice's list rather than the whole union — is not decidable by argument against the union;
>    ruled 2026-07-02 (gap-analysis ruling #2, `cc_gap_analysis_report.md`) to be resolved by a decode-only A/B at the
>    next Layer-3-touching increment. The union is the as-built and the spec's normative rule until that measurement rules otherwise.)*

**In plain words.** Each stretch of music proposes its own few best-fitting tonalities; the decision then pools all of those proposals and lets every one of them be chosen at every stretch. That is what lets an established tonality survive a brief excursion — a tonality that scored well anywhere in the passage stays available where it locally scored badly, so the cost of changing tonality, not the loss of the candidate, decides whether the excursion counts as a change.

**Why.** The record states the mechanism as the reason: pooling is how the established tonality survives a brief excursion, so that the change cost — 'not candidate elimination' — decides the outcome. The narrower alternative (injecting only the incumbent tonality into each stretch's list) is recorded as not decidable by argument and is assigned to a measurement: ruled 2026-07-02 (gap-analysis ruling #2, `cc_gap_analysis_report.md`) to be settled by a decode-only A/B at the next key/mode increment, with the pooled rule normative until then.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:230-239`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5** — `## 5. Building-block view (static / internal structure)` (heading at line 224). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The date given is the date of the recorded ruling that the narrower alternative is to be settled by measurement and that the pooled rule is normative until then; the pooled rule itself is recorded as as-built and is not dated in the record. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-347 — The cost of changing tonality is cheap-to-stay plus a term growing with tonal distance plus a large extra penalty on the relative major/minor switch

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Change cost = cheap-to-stay + grows-with-key-distance + a large relative-pair penalty.** Alternative considered:
>   a single flat "don't flip too easily" margin. Chosen: the standard key-finding shape (a flat margin cannot make a
>   near modulation cheaper than a remote one, nor guard the relative pair specifically); the starting amounts are
>   taken from the existing margin values and tuned later.

**In plain words.** Staying in the current tonality costs nothing; changing costs a base amount, plus more the further away the new tonality is, plus a large extra amount for the specific switch between a major key and its relative minor. A single flat 'do not flip too easily' margin was considered and rejected.

**Why.** The record states the reason with the alternative it rejects: a flat margin cannot make a near modulation cheaper than a remote one, nor guard the relative major/minor pair specifically; the shape chosen is the standard one in the key-finding literature (§14 cites the hidden-Markov key path with a high self-transition — Nápoles López, DLfM 2019; Gedizlioğlu & Erol, 2024). The starting amounts are taken from the existing margin values and tuned later.

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:307-310`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives we weighed)` (heading at line 295). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-348 — Tonal distance in the change cost is circle-of-fifths distance — not semitone distance, not differing scale tones — and brief-versus-sustained has no duration threshold at all

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> The change cost makes keeping the current key/mode cheap and changing it expensive — more expensive the
> further the new key is from the current one, **measured as circle-of-fifths (key-signature) distance** (the number of
> signature steps between the two keys' parent tonics; `C`→`F♯` and `C`→`G♭` both = 6 — not semitone distance and not a
> count of differing scale tones), and most expensive of all between relative major and relative minor (the hardest
> pair). The effect: a brief excursion is not worth the change cost over so few slices, so it stays in the original key;
> a sustained modulation is worth it, so the key changes; and the relative-major-versus-minor choice is settled by which
> reading fits the whole run of music, not one ambiguous slice. **There is no "how many slices" threshold for
> brief-versus-sustained — it is purely this fit-versus-cost arithmetic** (a duration threshold a reader might expect
> does not exist).

**In plain words.** How far apart two tonalities are, for the purpose of the change cost, is counted in steps around the circle of fifths — the number of key-signature steps between them — so C to F sharp and C to G flat are both six. It is not the distance in semitones and not a count of how many scale notes differ. And nothing anywhere counts how long an excursion lasts: whether a passage reads as a passing tonicization or as a real change of tonality falls out of the fit-against-cost arithmetic alone.

**Why.** The record states the consequence as the reason: over a few stretches the accumulated better fit does not repay the change cost, so a brief excursion stays; over a sustained one it does, so the tonality changes; and the relative major/minor choice is settled by which reading fits the whole run rather than by one ambiguous stretch. The passage flags the absent duration threshold explicitly because a reader would expect one.

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:212-220`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. Solution strategy` (heading at line 206). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-349 — The key/mode confidence compares whole readings — the winning run against the best run forced to a different tonality there — not the top two candidates at that stretch

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Confidence = how much better the winning sequence is than the best different-key sequence at that slice** (not
>   the gap between the top two scores at the slice on its own). Reason: the decision is the whole sequence, so the
>   meaningful confidence compares whole sequences; the near-tied cases are exactly the ones to mark "uncertain."

**In plain words.** How sure the analysis is about the tonality at one stretch is measured by re-running the whole passage with that stretch forced to a different tonality and seeing how much worse the best such reading is. It is not the gap between the two best-scoring candidates at that stretch on its own.

**Why.** The record states the reason: the decision being made is the whole run, so the meaningful comparison is between whole runs; and the near-tied cases the comparison exposes are exactly the ones the layer should mark uncertain.

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:311-313`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives we weighed)` (heading at line 295). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-350 — Of the layer's two confidence numbers, the whole-run margin is the published one; the per-stretch emission sigmoid is demoted to a gate input and a diagnostic

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> (The **sequence-margin confidence redesign** — which of the two boundary numbers is THE Layer-3
> confidence — is **CLOSED by D-L3a, 2026-07-04**: the sequence margin is declared THE boundary confidence and the
> emission sigmoid demoted to gate-input/diagnostic; only the Stage-5 calibration of the margin remains.)

**In plain words.** The tonality stage computes two different measures of how sure it is. The one that crosses the boundary to any other stage is the whole-run margin; the per-stretch one is kept only as an input to an internal threshold and for diagnosis. Only calibrating the published margin remains to be done.

**Why.** derivation not recorded — the record states the closure and the outcome but gives no defense for choosing the whole-run margin over the per-stretch sigmoid. The neighbouring defense that IS recorded is for the margin's FORM, not for its selection as the published number (**D-349**), and the classification that constrains it is the cross-layer confidence contract's Class M — a ranking margin, never a calibrated probability (**D-267**, `cowork_layer3_keymode_design.md:39`).

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:16-18`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **the opening block (above the first section heading)** — `# Architectural Layer 3 — KEY/MODE — Architecture & Design` (heading at line 1). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it RECORDS FINDINGS**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The record labels the closure `D-L3a` — a label from the document's own design-decision series, not a register identifier. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-351 — The key/mode search is its own decoder; the chord decoder is not reused for it

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **A dedicated best-sequence decoder for key/mode.** Alternative considered: reuse the existing chord decoder.
>   Chosen: a dedicated one — the existing decoder is specific to chords and cannot be reused.

**In plain words.** Finding the best run of tonalities uses a decoder written for that job. Reusing the existing chord decoder was considered and rejected, because that one is specific to chords.

**Why.** The record states the reason with the alternative: the existing decoder is specific to chords and cannot be reused.

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:314-315`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives we weighed)` (heading at line 295). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-352 — The key/mode grading bar splits the cases first: agreement where the published analyses are unanimous, any recorded reading (or an uncertain mark) where they are not

> The bar, with its partition stated: a case counts as **unambiguous** when the ground-truth
>   annotation gives a single local key/mode there, records no alternative reading, and (where more than one published
>   analysis covers the piece) the analyses agree; every other case — a recorded alternative reading, disagreeing
>   published analyses, or a modal passage the major/minor-only ground truth cannot represent (§1) — counts as
>   **genuinely ambiguous**. On the unambiguous cases the bar is agreement with the single reading; on the ambiguous
>   cases the bar is met when the layer's answer equals **one of the recorded readings** (that is what "defensible"
>   means here) or the case is marked "uncertain."

**In plain words.** A case counts as unambiguous when the published human analysis gives one tonality there, records no alternative, and — where more than one published analysis covers the piece — the analyses agree. Everything else counts as genuinely ambiguous: a recorded alternative, disagreeing analyses, or a modal passage the major/minor-only human analysis cannot express. On the unambiguous cases the analysis must match the single reading; on the ambiguous ones it must match one of the recorded readings or declare itself unsure.

**Why.** The record ties the partition to a stated limitation of the reference analyses: they are major/minor only, so a modal reading can be produced but cannot be checked against them (`cowork_layer3_keymode_design.md:133-136`, §11's second bullet). Grading is done on a held-out set of pieces the layer was not tuned on.

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:321-327`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§10** — `## 10. Quality & testing` (heading at line 317). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-353 — The key/mode layer is graded on two goals kept apart — agreement where the notes decide, and whether its own uncertainty lands on the genuinely ambiguous cases

> - **Two quality goals, measured separately.** (1) *Accuracy on the resolvable cases* — agreement with the human
>   analyses where the notes decide; and (2) *calibration of uncertainty* — whether the "uncertain" mark and the
>   confidence actually land on the genuinely ambiguous slices (a reliability curve over confidence; the precision and
>   recall of the "uncertain" mark on the error set; and whether the true key is carried among the alternatives). The
>   second goal is what backs the claim that Architectural Layer 3 is clearer about ambiguity than a single forced
>   label, so it is graded in its own right, not folded into accuracy.

**In plain words.** Two things are measured, and neither is folded into the other. First, does the tonality agree with the published human analysis where the notes settle it. Second, is the layer's own declared uncertainty honest — whether the unsure mark and the confidence actually fall on the genuinely ambiguous stretches, and whether the true tonality is among the runners-up it carried.

**Why.** The record states the reason: the second goal is what backs the claim that this layer is clearer about ambiguity than a single forced label would be, so it is graded in its own right rather than absorbed into the accuracy number.

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:337-342`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§10** — `## 10. Quality & testing` (heading at line 317). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-354 — The key/mode decoder's own settings are exhausted — no setting of its own moves the fixable error set, so the remaining headroom is not a decoder setting

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **The decoder-private settings are exhausted (sweep, 2026-06-22).** A bounded sweep of every decoder-private
>   setting found none that moves the **clean set** (§0; the fixable-within-key/mode miss subset defined in
>   `cc_layer3_error_decomposition_report.md`) net-positive — sweep record: `cc_layer3_sweep_report.md`. Widening the
>   per-slice window recovers the **stable measurement category** (the grading corpus's spans whose ground-truth key is
>   constant) but destroys tracking on the **modulation category** (spans containing a ground-truth key change);
>   lowering the change cost is net-negative on Baroque (a Jazz-only gain that would need
>   preset-conditioning the decoder settings — deferred); the candidate count is already saturated; the
>   alternatives-kept count is output-only. So the bounded-headroom fix is **not** a decoder knob — it is the one shared
>   lever below.

**In plain words.** Every setting private to the tonality decoder was swept, and none of them improves the part of the error that is genuinely fixable from the notes. Widening the per-stretch listening window helps passages of constant tonality but wrecks passages that change tonality; lowering the change cost is a net loss on the Baroque material; the number of candidates kept is already saturated; the number of runners-up carried only affects output. So the remaining headroom lies outside the decoder.

**Why.** Measured: a bounded sweep of every decoder-private setting, 2026-06-22, graded against the fixable-error subset defined in `cc_layer3_error_decomposition_report.md`; sweep record `cc_layer3_sweep_report.md`. The per-setting outcomes are enumerated in the entry itself, so the conclusion is stated with the evidence that produced it.

**Status.** LIVE · decided 2026-06-22 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:402-410`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 349). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-355 — The identified key/mode lever is the shared scorer's scale-membership term, applied once to the shared scorer at the wiring step and gated on the corpus stop and the pinned outputs

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **The identified shared-scorer lever, measured.** The stable-category under-weighting is carried by the scorer's
>   *scale-membership* term, not its (inert) leading-tone term. Sharpening the out-of-candidate-scale penalty lifts
>   *both* stable- and modulation-category accuracy with no trade-off (measured decode-only on the held-out test set at
>   coarse-region granularity: a net +57…+73 regions corrected on Baroque / +38…+68 on Jazz, depending on the sharpen
>   step — `cc_layer3_sweep_report.md` §3);
>   raising the leading-tone weight instead collapses accuracy. This is the change handed to the wiring increment, where
>   it is applied once to the shared scorer and must clear the project BIR gate and the snapshots (its production-side
>   magnitude is a wiring-time calibration; only its direction is validated so far).

**In plain words.** The under-weighting on passages of constant tonality is carried by the term that asks how well the sounding notes belong to a candidate's scale, not by the leading-note term, which is inert. Sharpening the penalty for notes outside the candidate scale improves both constant-tonality and changing-tonality passages with no trade-off; raising the leading-note weight instead collapses accuracy. The change is applied once, to the one shared scorer, at the step that replaces the older per-stretch code, and must clear the project's corpus regression stop and the pinned outputs.

**Why.** Measured decode-only on the held-out test set: a net gain of roughly 57 to 73 corrected stretches on the Baroque material and 38 to 68 on the Jazz material depending on the sharpening step (`cc_layer3_sweep_report.md` §3). The entry states its own limit: only the direction is validated so far, the production-side magnitude being a calibration at the wiring step.

**Status.** LIVE · decided 2026-06-22 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:411-418`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 349). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-356 — The leading-note presence gate is brittle and its fix is a later key/mode emission step, not a foundation patch — and the scale-membership lever is measured NOT to fix it

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **★ Brittle leading-tone presence-gate — a non-Bach key regression (diagnosed 2026-06-25; verified at source).** The
>   characteristic-pitch and true-leading-tone scorer terms are **hard-gated** on a `>0.1` window weight
>   (`keymodeanalyzer.cpp`, the char/leading-tone term gates — cited by function per the no-raw-line-numbers policy): a
>   key's leading tone that is *present but weak* (below the gate) is treated as
>   **absent**, so the key is denied its anchors *and* penalized. On the Mozart K279 opening the C-major leading tone
>   (B♮) carries weight **0.093** — a hair under the gate — so C major is flipped to **F major** (whose leading tone E
>   is C's ever-present third). The old 24-beat resolver cleared the gate; the wired 4-beat window does not, and the
>   window-width relation is **non-monotonic**, so simply widening it is not a clean fix. This is a **general
>   non-Bach-opening fragility**, structurally **invisible to the Bach-only BIR gate** (the notation tests are the guard
>   that caught it). The **scale-membership lever does NOT fix it** (measured: 15× the scale penalty never flips F→C —
>   the char/lt terms are *presence-gated*, not weight-scaled). **Fix = de-brittle the gate (weight-scale the char/lt
>   terms); a Layer-3 emission increment scheduled for **Phase B, item B2** of the stabilization plan
>   (`cowork_l1l3_stabilization_plan.md`) — leading-tone de-brittling is inference-quality, behind the inference
>   firewall (§0), *not* the Phase-4 tpc (tonal pitch class, §0) capability foundation —
>   not a foundation patch.** Full diagnosis: `cc_keyregression_diagnosis_report.md`.

**In plain words.** Two of the scoring terms treat a leading note that is present but faint as if it were absent, so the tonality is denied its anchor and penalised as well. On the opening of Mozart's K279 the C major leading note carries just under the threshold, and C major is read as F major instead. The older wide listening window cleared the threshold and the narrower one in use does not, and the relation to window width is not monotone, so simply widening it is not a clean fix. Making the terms scale with weight instead of switching on a threshold is scheduled as a later tonality-quality step, behind the rule that separates structural work from tuning. Sharpening the scale-membership penalty — the lever that helps elsewhere — was measured at fifteen times its strength and never fixes this case.

**Why.** Measured and verified at source, 2026-06-25: the leading note carries weight 0.093 against a threshold of 0.1; the scale-membership lever was tested at fifteen times the penalty and never flips the reading, because the two terms are gated on presence rather than scaled by weight. Full diagnosis `cc_keyregression_diagnosis_report.md`. The entry also records that this fragility is structurally invisible to the Bach-only corpus stop and was caught by the notation tests instead.

**Status.** LIVE · decided 2026-06-25 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:383-397`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 349). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-357 — Reading the notated spelling as tonality evidence belongs at the function layer, where function gates it — NOT as a standalone key/mode emission patch

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **MEASURED (read-only, 2026-06-22, `cc_layer3_tpc_keymeasure_report.md`):** a decode-only line-of-fifths tpc term is
>   **genuine spelling signal** (its modulation-gain/stable-loss frontier beats a change-cost control on both presets)
>   and helps modulation regions cleanly (+2–8 pts), **but** as a *standalone Layer-3* term it is only **marginal
>   overall** (best net +0.5 Baroque / +0.6 Jazz at a low weight) because it **hurts stable regions** — it over-switches
>   on tonicizations. That stable cost is exactly the **tonicization-vs-modulation discriminator that function (Layer 5)
>   supplies**, and the term is structurally **blind to same-signature ambiguity** (relative-pair / modal rotation). So
>   the right home for this retrofit is **Architectural Layer 5 (function)**, where function gates the
>   spelling signal — admitting the clean modulation gain without the stable cost — **not** a standalone Layer-3 emission
>   patch. This is why L4-first is the disciplined order (no clean standalone L3 win is being skipped). (Upper-bound
>   caveat: engraved corpus; MIDI spelling would see less.)

**In plain words.** Using how an accidental is written — G sharp against A flat — as evidence for the tonality is real signal and helps passages that change tonality cleanly, but on its own at the tonality stage it is barely a net gain, because it over-switches on passing tonicizations and is blind to the cases where two tonalities share the same key signature. Telling a passing tonicization from a real change is exactly what the later function stage supplies, so that is where this evidence is read.

**Why.** Measured read-only, 2026-06-22, `cc_layer3_tpc_keymeasure_report.md`: a decode-only line-of-fifths term beats a change-cost control on both style settings and gains two to eight points on changing-tonality passages, but nets only about +0.5 and +0.6 overall because of what it costs on constant-tonality passages. The entry states its own limit: an engraved corpus is an upper bound, and material without written spelling would see less.

**Status.** LIVE · decided 2026-06-22 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:497-506`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§15** — `## 15. To do — deferred enhancements (this layer is built; these are revisions on record)` (heading at line 480). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The surrounding deferred-enhancement entry is recorded per the user, 2026-06-22; the measured placement conclusion quoted here names no ratifier. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-358 — A sonority shaped like a dominant is note-level evidence for the tonality it implies, and belongs in the key/mode emission — deferred, design-first

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **★ Dominant-implication key evidence in the emission (review amendment A-3, ratified 2026-07-02).** As built, the
>   per-slice emission is **collection-fit only**: it scores how well a slice's pitch content matches each candidate
>   key/mode's scale, and carries no evidence from the *shape* of the sounding sonority. But a sonority shaped like a
>   dominant seventh or leading-tone seventh is strong **note-level** evidence for the key it implies (its tritone
>   resolves into exactly one major and one minor tonic pair) — evidence readable from the notes alone, **before and
>   without any chord decision**, so it belongs in this layer's emission without breaking the evidence split (Layer 5
>   still owns *resolution-confirmed* evidence — the cadence votes). The gap is what the external review's Tristan
>   simulation exposed (F-10: keys established by **dominant implication**, tonic arrivals denied → collection-fit is
>   near-flat and the decoder rides on inertia → systematic under-modulation), and it also bears on the measured
>   relative-pair floor (the implied tonic disambiguates the shared collection). **Shape:** a sonority-shape term in the
>   per-slice emission (pitch-set → implied-tonic fit contribution); decoder structure unchanged; weight
>   precision-phase. **Status:** deferred — design-first, measured before wiring like every increment (the tpc-term
>   lesson above applies: measure the stable-region cost, not just the modulation gain). Source:
>   `cowork_architecture_review_2026_07.md` §7/§9 (F-10, A-3).

**In plain words.** As built, the per-stretch tonality score asks only how well the sounding notes fit each candidate's scale, and carries nothing about the shape of the sonority. But a chord shaped like a dominant seventh or a leading-note seventh points at one major and one minor tonic, and that is readable from the notes alone, before any chord is named — so it belongs in the tonality stage without breaking the evidence split. It is deferred, to be designed and measured before it is wired, and the measurement must include what it costs on passages of constant tonality, not only what it gains on passages that change.

**Why.** Grounded in the external architecture review's Wagner simulation: where tonalities are established by dominant implication and tonic arrivals are withheld, the scale-fit score is near-flat and the decision rides on inertia, giving systematic under-modulation (finding F-10). It also bears on the measured floor for the relative major/minor pair, since the implied tonic distinguishes two readings that share one collection. Source `cowork_architecture_review_2026_07.md` §7/§9.

**Status.** DEFERRED · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:507-520`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§15** — `## 15. To do — deferred enhancements (this layer is built; these are revisions on record)` (heading at line 480). A delegation at ARCHITECTURE.md:1331 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The record states the amendment (A-3) was ratified 2026-07-02 but does not name the ratifier at this home; the amendment set's own document banner is quoted in the phase-1g triage as `AMENDMENTS A-1…A-10 RATIFIED (user, 2026-07-02)`, and that document is in the phase-1h full-read set. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-405 — The full ranked key resolve retained as a segmentation seed is KEPT — adjudicated load-bearing, not dead scoring work

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **FQ-7 — ✅ RESOLVED `56b06462db`.** S8 constants sourced from the shared symbols. **S9 adjudicated
>   KEPT (load-bearing, NOT dead):** the `resolveKeyAndModeRanked@585` feeds `greedyExpandSegmentation@851`
>   + `findTemporalContext@900` (the grid); dropping it would move the grid. Report-only, no change.

**In plain words.** The legacy region path runs the heavy ranked key resolution and appears to use only its top answer as a starting point for cutting the music into regions, which looked like retained work with no purpose. It was checked and kept: its result feeds the region-grid expansion and the neighbour-chord context, so removing it would move the grid — a behavior change, not a cleanup.

**Why.** Adjudicated at the code during the pre-Layer-5 refactor stage, with the two consumers named (the greedy segmentation expansion and the temporal-context walk) and the consequence stated: dropping it would move the grid. Recorded as report-only, with no change made.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_structural_integrity_audit.md:260-262`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§3.1** — `### 3.1 Stage-1 build status (Engage arc #7, 2026-07-07 — `cc_engage_pre_l5_refactor_report.md`)` (heading at line 251). A delegation at cowork_engage_arc_plan.md:4 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it RECORDS FINDINGS**.

**Provenance.** Found by the phase-1i continuation wave, 2026-08-02, reading `cowork_structural_integrity_audit.md` IN FULL. The document's banner records `Status: read-only grounded catalogue (CC, 2026-07-07; Engage arc #6)` — an authored catalogue, not a ratified contract. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1i ratification queue. Recorded in the Stage-1 build-status section beside the resolved constant-sourcing item; the byte-identity of that stage is stated in the same section (0-diff `.ours.json` 352x3, robust stop PASS, the batch case-identity sets 52/24/52). ★ RATIFIED (user, 2026-08-02, the phase-1i queue).


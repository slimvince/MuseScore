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

**Why.** SEARCHED 2026-08-09 and the record holds NO derivation for this decision at its own home. The home text (`ARCHITECTURE.md`, the Layer-3 wiring block) states WHAT the step-1 wiring did — the per-region `resolveKeyAndModeRanked` call replaced by a single whole-score decode — and what that connected (Layer 1's note model and Layer 2's slicer, so neither is isolated any longer). It states no reason for preferring a whole-score sequence decision to a per-region one AT THIS SITE. What stands in its place is a SUPERSESSION, not a defense: this entry is superseded by **D-001**, and the ground for deciding tonality as a sequence lives with the joint estimator's own decisions. Recorded as an established gap in this entry's record rather than filled from D-001, which would attribute to a 2026-06 wiring step a reason written for a later design.

**Status.** SUPERSEDED BY D-001 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1810`

**Provenance.** The joint estimator now decides key on both surfaces (D-005, D-010). The Layer-3 section still reads 'Built+Live' - see OPEN_ITEMS OI-232

### D-052 — The signature read and declared-mode mapping live in ONE shared function

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> The signature read + declared-mode
> mapping + declared-gated Baroque `partialSignatureCorrection` was lifted verbatim into a shared
> public `resolveKeySignatureContext`, **called by both** the resolver and the wiring — so no
> signature/partial-correction logic is duplicated.

**In plain words.** Reading the printed key signature and turning it into a starting assumption happens in one place that both callers use, so the two cannot drift apart.

**Why.** SEARCHED 2026-08-09 and the record HOLDS one, stated as a CONSEQUENCE in the decision's own home text rather than as a separate clause — which is why an empty field misrepresented it. The text ends *"so no signature/partial-correction logic is duplicated"*: the reason for lifting the signature read, the declared-mode mapping and the declared-gated partial-signature correction into one shared public function called by both the resolver and the wiring is that two copies of that logic can drift apart. That is principle #6 (one path per concern) applied at a named seam, and it is the whole of what the record states — no measurement is attached and none is invented.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1832-1835`

**Provenance.** ARCHITECTURE.md:1291-1296

### D-053 — The tick-local path keeps the older resolver (the ratified P4-defer)

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **P4 tick-local still uses `resolveKeyAndModeRanked` + `collectPitchContext`** (the ratified
>   P4-defer).

**In plain words.** One narrow fallback - answering about a single moment when no surrounding stretch is available - still uses the older method. That was a deliberate deferral.

**Why.** SEARCHED 2026-08-09. The record holds NO derivation for the deferral itself — it does not say why the tick-local fallback was left on the older resolver rather than moved with the rest. What it DOES hold, and what is recorded here rather than mistaken for a derivation, is the EVIDENCE that the deferral cost nothing at the increment that made it: the home text states the path was verified *"byte-identical this increment (the `tickLocal` snapshot section is unchanged in all 11 goldens)"* and therefore *"no leak"*, and it names the follow-up that would end the deferral (**P4-redecode**). Evidence that a deferral is currently harmless is not a reason for choosing it, and the two are not conflated. The related contract for what that path may consume — cold context, accepted because stated — is **D-063**, which carries its own defense.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1846-1847`

**Provenance.** On the switched build the note-seam funnel returns from the record arm before this fallback is reachable (notationcomposingbridge.cpp:728-738). The D-P4 revisit trigger (D-063) was never discharged

### D-054 — All 21 modes are scored against all 12 tonics; the harmonic major family is deferred

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> Harmonic major modes are
> significantly rarer as tonal centers than melodic and harmonic minor modes, and the
> validation corpus is unlikely to calibrate them well.

**In plain words.** The key finder considers 21 scale types on each of the 12 possible tonics. The harmonic major family was left out because it is rare and we have no annotated music to calibrate it against.

**Why.** Recorded for the DEFERRAL half only, ARCHITECTURE.md:2459-2463: the harmonic major modes are significantly rarer as tonal centers than the melodic and harmonic minor modes, and the validation corpus is unlikely to calibrate them well. Why the other 21 modes are all scored against all 12 tonics has no recorded derivation.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3323-3325`

**Provenance.** ARCHITECTURE.md:2394-2395 (21 modes), :2213-2217 (harmonic major deferred)

### D-055 — The 21 mode priors are independent and user-configurable

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **21 independent additive priors**, one per mode, user-configurable
>   via `IComposingAnalysisConfiguration::modePrior{ModeName}()`

**In plain words.** How likely each scale type is considered to be is a separate adjustable number per scale type, exposed in the preferences.

**Why.** SEARCHED 2026-08-09. The record holds a ground for WHAT THE DEFAULTS EXPRESS but NO derivation for either half of the decision itself. The home text states that the defaults *"reflect Western tonal frequency"*, naming the ordering that follows from it — which is a musical justification of the default VALUES, and `ARCHITECTURE.md` §17.2 requires exactly that. It is not a reason for the two things this entry actually decides: that the priors are **independent and additive**, one per mode, rather than a shared tier or a single family term; and that they are **user-configurable** through the analysis-configuration interface rather than fixed. Neither choice has a recorded derivation and no alternative is recorded as considered. Recorded as an established gap. **Read beside its reachability finding, which is a different matter and is not restated here:** this entry is the one candidate wrong LEGACY mark the phase-1w verification reports — the preference registration runs unconditionally in production code while the consumer that reads the priors is the legacy key scorer — and that scoping question is tracked at `OPEN_ITEMS.md` OI-302.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3271-3272`

**Provenance.** ARCHITECTURE.md:2408-2410, :3020-3073. Superseded on the production path by D-003 (inference is preset-independent)

### D-056 — Notes always win - the notated key signature is a weak hint, not a bypass

> The key/mode inferrer always runs. The notated key signature's `KeyMode` enum
> (`MAJOR`, `MINOR`, etc.) is no longer a bypass gate — it is passed as a weak hint
> (`declaredMode`) to `analyzeKeyMode()`

**In plain words.** The key printed at the start of the score does not settle the question. It only nudges the answer; what the notes actually do decides.

**Why.** Stated constraint, ARCHITECTURE.md:3382-3384: the notated signature is what the composer wrote down, not what the music does - a piece may modulate, be notated in a partial signature, or contradict its own signature - so it enters as a weak hint the sounding notes can outvote.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4283-4285`

**Provenance.** ARCHITECTURE.md:3380-3392

### D-057 — The priority of evidence - actual sounding notes are the strongest evidence

> | Strongest | Actual sounding notes | what is literally happening now |

**In plain words.** In deciding the key, what is actually sounding right now outranks the surrounding bars, which outrank the printed key signature, which outranks the major/minor tag on it.

**Why.** Stated constraint, ARCHITECTURE.md:3396-3403: the priority table ranks the actual sounding notes the strongest evidence, above the notated signature and above any prior result, for the same reason as D-056.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4361`

**Provenance.** ARCHITECTURE.md:3396-3403. Cited by open_items/OI-228 as the primary source the joint emission departs from. NOT catchable by the harvest's signature net - the reason this adjudication had to read the specifications in full. ★ SCOPE SETTLED 2026-08-11 BY THE USER'S RULING 63 (`cowork_rulings_2026_08_11_fourteenth_stop.md`, closing `OPEN_ITEMS.md` OI-324), AND THIS ENTRY IS NOT AMENDED BY IT: the ranking is CROSS-CUTTING and binds BOTH arms, so OI-228's citation of it for a claim about the joint emission stands. What was unwritten is now written — the same ranking is stated for the production arm at the joint estimator's own section of `ARCHITECTURE.md`, where the emission's evidential contract lives, and §5.2's phase-1z scoping note carries a dated annotation saying that it scopes the MECHANISM and not the ranking. One rule, stated for the arm each section describes, cross-referenced rather than duplicated (#6). The excluded reading, recorded at the ruling: legacy-only, which would override recorded user doctrine on an unestablished extension of a scoping note.

### D-058 — The piece-start shortcut

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **There is no piece-start exception — the opening is note-based.** At piece start
> `resolveKeyAndModeRanked()` runs its ordinary path.

**In plain words.** At the very start of a piece there is not yet enough music to judge the key, so if the score declares major or minor the program simply believes it, marked as a middling-confidence answer.

**Why.** SEARCHED 2026-08-09. The record holds a STATED GROUND but no derivation, and the two are worth separating. The ground is at `ARCHITECTURE.md:3387-3392`, which calls the removed shortcut *"a deliberate pragmatic choice for the score opening, not a general bypass"* — the pragmatic claim being that at the very opening there is not yet pitch evidence to weigh, so the declared mode was believed rather than waited for. **No measurement, no citation and no alternative are recorded**, so the choice of a shortcut over any other opening treatment has no derivation. Read it beside this entry's status: the mechanism was REMOVED from the code on 2026-06-14 and the entry is superseded in fact, so the absent defense is a fact about the record rather than a live gap in the analysis.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4321-4322`

**Provenance.** ARCHITECTURE.md:3387-3392 calls it 'a deliberate pragmatic choice for the score opening, not a general bypass'. NOT catchable by the harvest's signature net ★ SUPERSEDED IN FACT — recorded 2026-08-04 (phase 1z, dispatch cc_instruction_phase1z_commit_and_instrument_record.md Task 3.4; OPEN_ITEMS.md OI-315). The mechanism this decision records was REMOVED from the code in Stage 4b-i on 2026-06-14: src/composing/analysis/key/keyresolver.cpp:291-301 states the removal in its own comment, and docs/key_path_design.md:65-73 dates it and names the re-targeted pins (Composing_KeyresolverTests.PieceStartOpening_NoteBased_DeclaredMinor/_DeclaredMajor). It is NOT falsified: nothing showed the decision wrong, a later BUILD replaced what it governs without a ruling that names it — which is what this register's status vocabulary calls superseded-in-fact. The ⚠ LEGACY mark STAYS: the subject is still the legacy key path, and the mark states what the decision is ABOUT. ★ Verbatim RE-TAKEN 2026-08-04 from the corrected specification text. The sentence this entry quoted — 'when the analysis tick is within the first 16 quarter-note beats (a separate constant from the 16-beat lookback window below — they coincide in value, not by design), no prior result exists (`prevResult == nullptr`), and the key signature carries an explicit mode, the function returns the declared mode immediately (confidence 0.5) rather than waiting for pitch evidence that cannot yet exist.' — was false at HEAD and is corrected in place at ARCHITECTURE.md §5.2, which now states that there is no piece-start exception, that the opening is note-based, and that the removal is tried and closed; the former wording is preserved here rather than deleted (#12). What did NOT change: the decision's own date and ratifier remain 'not stated', and no defense is supplied that the record never had.

### D-059 — The temporal window - 16 beats back, 8 beats forward, decayed

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> The bridge uses a 16-beat lookback + 8-beat lookahead window:

**In plain words.** To judge the key at a point, the program looks about four bars back and two bars forward, giving less weight to music further away.

**Why.** SEARCHED 2026-08-09 and the record holds NO DERIVATION for either number — an established gap, and the search names exactly what stands in place of one. The ONLY stated basis for 16 and 8 anywhere the search reached is an in-code gloss reproduced at `ARCHITECTURE.md:3428-3429`, *"~4 measures in 4/4"* and *"~2 measures ahead"*: a restatement of the values in bars, not a reason for them. There is no theory citation, no measurement, and no alternative window considered. It is one of the founding instances `CLAUDE.md`'s carry-its-defense rule names in its own text. The values are legacy-arm only since the notation switch (**D-010**), which bounds what the gap costs without closing it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4389`

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

**Home.** `ARCHITECTURE.md:3277-3281`

**Provenance.** ARCHITECTURE.md:2414-2418; the same guard is listed among the key-path scoring terms at :2480-2482 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-287 — Key-as-distribution is SHELVED - its motivating case was already fixed and no live target was found

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not revive carrying a ranked distribution of key candidates forward instead of one committed
>   key.** *Why:* measured and cited in the record — the one failure it was designed to fix had
>   already been fixed another way, the resolver returns the correct key at the top rank for every
>   stretch of it, and no case was found anywhere in the corpus where the correct key sits at the
>   second or third rank.

**In plain words.** Carrying a ranked distribution of key candidates forward, instead of one committed key, was withdrawn: the one failure it was designed to fix had already been fixed another way, no other case in the corpus needed it, and the confidence number it would have been weighted by is not trustworthy.

**Why.** Measured and cited in the record: the motivating case (Corelli op01n08d read in G minor instead of C minor) was already fixed by the partial-signature correction `81978321e3`, the resolver returns C minor at rank 0 for every stretch, and no case was found where the correct key sits at rank 1 or 2 (`cc_step3_key_investigation_report.md`). A second reason is recorded beside it: the confidence field is re-ranked without being recomputed, so it reads anywhere from 0.025 to 1.00 on one correctly-keyed piece and cannot scale anything.

**Status.** LIVE · decided 2026-06-08 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1751-1755`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the redesign-sequence block) and in the 2026-06-08 `STATUS_ARCHIVE.md` entry, both pointing at `docs/redesign_plan.md` Step 3. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-08 (CC, `cc_instruction_away_execution.md` Task 2) into the Layer-3 key section, which already NAMED this decision in its *"Tried and closed on this layer"* line without saying what it was — so a reader met the identifier and could not learn the rule. The archive is untouched (#12); the naming is unchanged and now points at a section that states it. THE THREE THINGS THAT RODE ALONG rather than being dropped, each written into the home text: the STRUCTURAL second reason (the confidence field is re-ranked without being recomputed, so it cannot scale anything), the STATED RE-OPEN CONDITION (a confirmed case with the correct key at rank one or two — this is a shelving with a trigger, not a permanent exclusion), and the note for a reader arriving from the joint estimator (that design carries a full posterior by construction, so the concern is met by a different design rather than by reviving this one). FORMER HOME, PRESERVED (#12): `cowork_handoff_archive.md:5272`. FORMER CLASS, PRESERVED (#12): `unhomed`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "3. **Key-as-distribution — ⛔ SHELVED.** Motivating case (Corelli op01n08d) already\n   fixed by `81978321e3`. No confirmed live target in corpus. `normalizedConfidence`\n   structurally unreliable as scaling signal. See `docs/redesign_plan.md` §Step 3." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. The piece identifier, the fixing commit and the confidence range stay in the record that measured them and are not carried into the specification (D-431). **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the key layer (at line 1744 on 2026-08-03), under *"Tried and closed on this layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-290 — The key-agnostic local cadence approach is FALSIFIED at its precision ceiling

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Do not retry deciding the key from cadences found without knowing the key, one cadence at a
>   time.** *Why:* measured to its limit with a byte-matched re-implementation, which is what makes
>   the ceiling a measurement rather than an estimate — the chromatic-leading-tone gate is orthogonal
>   to correctness, since about as many true modulations as false ones carry a diatonic leading tone,
>   and the relative-pair signals were already spent by the existing aggregation.

**In plain words.** Deciding the key from cadences found without knowing the key, one cadence at a time, was tested to its limit and cannot be made accurate enough to use. The remaining errors need either a long-range key decision or a different kind of model - not a better local cadence rule.

**Why.** Measured with a byte-matched reimplementation (the Python re-implementation reproduced the committed analysis exactly on all 326 pieces, so the simulation is trustworthy): the chromatic-leading-tone gate is orthogonal to correctness (about 45 % of true modulations and about 50 % of false ones carry a diatonic leading tone), and the relative-pair signals were already spent by the existing aggregation. Ceiling approximately 50-58 % precision at 18-22 % recall, below the bar the wiring step required.

**Status.** LIVE · decided 2026-06-15 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1762-1766`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-15 cadence-precision-investigation block), citing `cc_cadence_precision_investigation_dossier.md`. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-08 (CC, `cc_instruction_away_execution.md` Task 2) into the Layer-3 key section, which already NAMED it in its *"Tried and closed on this layer"* line without saying what it was. The archive is untouched (#12); the naming is unchanged. **THE SCOPE CAVEAT RODE ALONG AND IS WRITTEN INTO THE HOME TEXT** — measured on the Bach ground-truth corpus, other repertoires unmeasured — because a falsification carried into a specification without its scope reads as wider than it was measured to be. So does the statement of what the remaining errors DO need (a long-range key decision or a different kind of model), which is the half that tells a future design where to look instead. FORMER HOME, PRESERVED (#12): `cowork_handoff_archive.md:3896`. FORMER CLASS, PRESERVED (#12): `unhomed`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **★★ CADENCE-PRECISION INVESTIGATION: NEGATIVE — the key-agnostic LOCAL cadence approach has HIT ITS PRECISION CEILING (2026-06-15).**" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. The precision and recall figures, the corpus size and the percentages stay in the dossier that measured them and are not carried into the specification (D-431). **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the key layer (at line 1744 on 2026-08-03), under *"Tried and closed on this layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-306 — The key layer's backward re-reading stays switched off in the shipped configuration

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **The backward re-reading facility stays SWITCHED OFF in the shipped configuration.** This layer carries a
> facility for returning to an earlier stretch and re-reading it once later evidence has arrived
> (`ReachBackOptions`). It is built, and `enabled = false` is the shipped default; turning it on is reopened

**In plain words.** The key analysis has a facility for going back and re-reading an earlier stretch once later evidence arrives. It is built but switched off, and turning it on is reopened only when a specific piece of evidence has been gathered.

**Why.** Measured and judged insufficient: an A/B run showed the designed effect is material (roughly 35–45 % of interior range queries change, almost all of them anchoring the leading key) but the timing comparison was confounded (one arm cold, the other warm), so the evidence needed to justify switching it on — interleaved timing plus an adjudicated sample of the changed outputs — was named and not yet gathered (`STATUS_ARCHIVE.md:232`).

**Status.** LIVE · decided 2026-07-02 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1771-1773`

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

**Home section.** **“`dim7CharacteristicBonus`”** — `### `dim7CharacteristicBonus` — `kDim7CharacteristicBonus = 0.75`` (heading at line 246). A delegation at CLAUDE.md:1113 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

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

**Home.** `cowork_layer3_keymode_design.md:76-88`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§1** — `## 1. Introduction & purpose` (heading at line 68). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:145-149`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§1** — `## 1. Introduction & purpose` (heading at line 68). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:169-175`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. Constraints` (heading at line 154). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:246-255`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5** — `## 5. Building-block view (static / internal structure)` (heading at line 240). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:323-326`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives we weighed)` (heading at line 311). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:228-236`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. Solution strategy` (heading at line 222). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:327-329`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives we weighed)` (heading at line 311). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-06-22)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-350 — Of the layer's two confidence numbers, the whole-run margin is the published one; the per-stretch emission sigmoid is demoted to a gate input and a diagnostic

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **As-built (D-L3a CLOSED, 2026-07-04): this sequence margin (`HarmonicRegion.keyConfidence`) IS the layer's published boundary confidence**; the per-slice emission sigmoid (`normalizedConfidence`) is an internal gate input (the downstream 0.8 KeyArea/cadence annotate gate) + diagnostic, NOT the boundary confidence.

**In plain words.** The tonality stage computes two different measures of how sure it is. The one that crosses the boundary to any other stage is the whole-run margin; the per-stretch one is kept only as an input to an internal threshold and for diagnosis. Only calibrating the published margin remains to be done.

**Why.** derivation not recorded — the record states the closure and the outcome but gives no defense for choosing the whole-run margin over the per-stretch sigmoid. The neighbouring defense that IS recorded is for the margin's FORM, not for its selection as the published number (**D-349**), and the classification that constrains it is the cross-layer confidence contract's Class M — a ranking margin, never a calibrated probability (**D-267**, `cowork_layer3_keymode_design.md:39`).

**Status.** LIVE · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:55`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§0** — `## 0. Terms (read first — nothing below uses a term before its row)` (heading at line 42). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer3_keymode_design.md` IN FULL. The record labels the closure `D-L3a` — a label from the document's own design-decision series, not a register identifier. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ HOME MOVED 2026-08-11 (CC, `cc_instruction_return_continuation_13.md` Task 1), under the registered homing procedure D-668, by its STEP 1 — the pointer move, tried before any write and taken because it applies. NO TEXT WAS WRITTEN INTO THE SPECIFICATION and none was moved: §0's terms row already STATED this rule, in both of its halves and with the closure label, so writing it a second time somewhere else would have put two copies of one rule into one document (#6). THE FORMER HOME, PRESERVED (#12): `cowork_layer3_keymode_design.md:32-34`, the document's opening STATUS BANNER — whose own authored section judgment says in terms that *the one rule it does carry (which of the two boundary numbers is THE Layer-3 confidence) is a decision recorded in a banner rather than in a rule-stating section*, which is what put this entry in the findings-not-rules item and is what this act discharges. THE FORMER VERBATIM, PRESERVED (#12): "(The **sequence-margin confidence redesign** — which of the two boundary numbers is THE Layer-3\nconfidence — is **CLOSED by D-L3a, 2026-07-04**: the sequence margin is declared THE boundary confidence and the\nemission sigmoid demoted to gate-input/diagnostic; only the Stage-5 calibration of the margin remains.)" ★ WHAT THE NEW HOME DOES NOT CARRY, stated because a pointer move must not narrow an entry silently: the former banner's closing rider — *only the Stage-5 calibration of the margin remains* — is a statement of OUTSTANDING WORK rather than of the rule, and it is untouched where it stands, in the banner and in the plain restatement above. The banner text is not edited by this act. The entry's DEFENSE is likewise not supplied by the move and is not invented: the rationale below records the established gap and names what stands in its place.

### D-351 — The key/mode search is its own decoder; the chord decoder is not reused for it

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **A dedicated best-sequence decoder for key/mode.** Alternative considered: reuse the existing chord decoder.
>   Chosen: a dedicated one — the existing decoder is specific to chords and cannot be reused.

**In plain words.** Finding the best run of tonalities uses a decoder written for that job. Reusing the existing chord decoder was considered and rejected, because that one is specific to chords.

**Why.** The record states the reason with the alternative: the existing decoder is specific to chords and cannot be reused.

**Status.** LIVE · decided 2026-06-22 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer3_keymode_design.md:330-331`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives we weighed)` (heading at line 311). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:337-343`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§10** — `## 10. Quality & testing` (heading at line 333). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:353-358`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§10** — `## 10. Quality & testing` (heading at line 333). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:418-426`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 365). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:427-434`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 365). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:399-413`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 365). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:513-522`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§15** — `## 15. To do — deferred enhancements (this layer is built; these are revisions on record)` (heading at line 496). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer3_keymode_design.md:523-536`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§15** — `## 15. To do — deferred enhancements (this layer is built; these are revisions on record)` (heading at line 496). A delegation at ARCHITECTURE.md:1742 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

### D-494 — RATIFIED AMENDMENT A-4: the function layer must gain key-confirmation channels that do not require a cadence, plus an enharmonic-identity rule for key spans

> - **The layer needs KEY-CONFIRMATION CHANNELS THAT DO NOT REQUIRE A CADENCE (the Layer-5 half of
>   the ratified amendment whose other half — an enharmonic-identity rule for key spans — is at
>   Layer 3; the two cross-point).** Named channels: **sustained dominant emphasis**
>   (arrival-denied dominants) and **recognized transposition sequences**, the latter entering as an
>   input from the recognition consumer this layer is already planned to gain. *Why:* derived from
>   the review's stress simulation and stated with it — on resolution-denying music the
>   cadence-confirmed modulation gate almost never fires, so the default keeps the home key across
>   genuinely modulating spans and every Roman numeral in them is computed against the wrong key. The
>   measurement bed named with the amendment is a resolution-denying repertoire.

**In plain words.** The program only accepts a change of key when a cadence confirms it. Music that deliberately avoids cadences — a sustained dominant that never resolves, a sequence that transposes step by step — therefore keeps being read in the old key. The amendment requires channels that confirm a key without a cadence, and a rule for deciding whether a span is written in one spelling of a key or its enharmonic twin.

**Why.** Derived from the review's own stress simulation and stated with it: on resolution-denying music the cadence-confirmed modulation gate almost never fires, so the default keeps the home key across genuinely modulating spans and the Roman numerals are computed against wrong keys; and enharmonic reinterpretation is handled at the single-chord level while no rule addresses enharmonic identity at the key-span level.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:2154-2162`

**Provenance.** Amendment A-4 of the external architecture review, in a document whose banner records amendments A-1…A-10 as RATIFIED by the user on 2026-07-02. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ NOT A FRESH DECISION, stated so that nothing is counted twice (dispatch cc_instruction_reads_3.md §1.3): the amendment itself was ratified by the user at the 2026-07-02 architecture review, which is what this entry's Status line already records. Ratifying the ENTRY records only that the register transcribes that ratification correctly — it neither re-makes the decision nor adds a second ratification event to it. Its sibling A-3 is already registered as **D-358** (deferred); this amendment has no register entry and no product located by this wave. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`) — SPLIT ACROSS TWO HOMES, on the user's ruling that A-4's two separable obligations each sit at their own layer and cross-point. ★ BOTH HOMES ARE RECORDED HERE, which is what the ruling requires of the register entry: (1) the cadence-less key-confirmation channels are written into the `ARCHITECTURE.md` LAYER-5 section, and that is the home the `home` field anchors, because the amendment's headline obligation is Layer 5's; (2) the enharmonic-identity rule for key spans is written into the `ARCHITECTURE.md` LAYER-3 section, in the block of four Layer-3 rules this wave added, and each of the two blocks names the other so a reader arriving at either finds both. The `home` field carries ONE parseable anchor because the register's own machinery parses it as `file:line-line`; the second home is recorded in this field rather than in a second anchor, and the two blocks' cross-pointing is what keeps the split findable from the specification (criterion C4). Both halves are DESIGN-ONLY and are written as obligations the layers owe, never as mechanisms they have. Assumption A1 discharged for both destinations before writing. FORMER HOME, PRESERVED (#12): `cowork_architecture_review_2026_07.md:320-323`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 307, "section": "## 9. Proposed amendments (ranked; each ratification-gated; none is code)", "label": "§9", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **A-4 (from F-10, F-14). Specify cadence-less key-confirmation channels in §5.3** — sustained dominant emphasis
  (arrival-denied dominants), recognized transposition sequences (the recognition consumer as a §5.3 input — synergy
  with the already-planned consumer), and an enharmonic-identity rule for key-spans. Design-only now; Tristan-class
  corpus as the measurement bed." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-571 — The declared-mode influence becomes a small additive hint, and SMALLNESS IS THE GATE — no separate confidence test is added

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

>   and keep it as the only declared influence on the 252-candidate score. A small magnitude makes it a
>   genuine **tiebreaker**: it can only flip the winner when the raw note-based gap is already within ~1.0
>   (i.e. "when genuinely unsure"), and it cannot override clear note evidence. No explicit confidence
>   gate is needed — smallness *is* the gate. Keep the application point unchanged. (Optionally rename to
>   `declaredHintWeight` for honesty; mechanically identical.)

**In plain words.** The written major/minor declaration used to override note evidence outright. It becomes a small bonus instead. Because it is small, it can only decide a case where the evidence was already almost balanced, and it cannot overturn a clear reading — so no extra rule is needed to say when it may apply. Its smallness is that rule.

**Why.** Stated with the change and argued from the arithmetic: the magnitude is set below the strongest note-based terms, so the hint can only flip a winner when the note-based gap is already within it. The record marks the value itself provisional, to be fitted at the fitting stage.

**Status.** SUPERSEDED IN FACT · decided 2026-06-14 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/stage4b_design.md:69-73`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§2.1** — `### 2.1 The −7 penalty → a small additive declared *hint* (OQ1)` (heading at line 64). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `docs/stage4b_design.md`, the Stage-4b design implementing the user's ratified Stage-4 redirect; the staged approach was chosen by the user 2026-06-14. Read in full by READ WAVE 4, 2026-08-04. **Its subject is the LEGACY key path** (`keymodeanalyzer` / `keyresolver`), which the joint estimator replaced on both surfaces. The demotion landed and was measured (the document's own §2.7, HELD then ratified). Its subject is a scoring term of the legacy key emission, which the production arm no longer runs: the joint estimator takes the signature and declared mode as a weak fitted soft prior with no conditional gate anywhere (**D-528**), and conditions the initial key state only (**D-450**). Recorded *superseded in fact* rather than *superseded by* — no ruling names this decision; a later build replaced what it governs.

### D-572 — The hard post-hoc declared-mode promotion is REMOVED OUTRIGHT rather than kept in a gated form

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **Tried and closed on the declared mode's weight, and it is a SECOND removal at the same increment
> — do not retry; the register carries it with its evidence: D-572 (the hard post-hoc "strong
> declared-mode prior" promotion, which moved the highest-ranked declared-compatible result to the
> front REGARDLESS of the candidate-score gap, REMOVED OUTRIGHT rather than kept in a gated form).**

**In plain words.** A step that took the best reading agreeing with the written major/minor declaration and pushed it to the front regardless of how badly it had scored was deleted, not softened. Keeping any version of it would have made the demotion of the declaration pointless wherever the note evidence had already won.

**Why.** Stated with the change: a veto is incompatible with note-based inference being primary, and leaving a gated version would have made the accompanying demotion a no-op in exactly the cases it was made for. The document puts the choice to the user explicitly and recommends removal.

**Status.** SUPERSEDED IN FACT · decided 2026-06-14 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:4339-4348`

**Provenance.** ★ HOMED 2026-08-04 (CC, dispatch `cc_instruction_guard_fix_and_item1d.md`, Task 2.2) UNDER RULING R2 / register entry **D-644**: where a superseded decision's content is a REMOVAL there is no successor to move the obligation to (D-642's condition cannot be met), so the owning specification STATES THE CURRENT BEHAVIOUR and RECORDS THE REMOVAL AS A TRIED-AND-CLOSED LINE. **This is the precedent's own act, performed for the sibling removal that landed at the same increment:** D-058 was corrected in `ARCHITECTURE.md` §5.2 at phase 1z in exactly this form. Both halves are now present there — §5.2 already stated the current behaviour (the promotion 'was removed in the same increment', with the declared mode reaching the analysis only as a small hint at every tick), written when D-058 was corrected; what this act adds is the tried-and-closed line, in that section's own voice and WITH ITS DEFENSE. The verbatim is RE-TAKEN from that line. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `docs/stage4b_design.md:57-63`, §2.2 'The hard post-hoc promotion → REMOVED (OQ1)'; former class `gap`, cleared because a layer-specification home is not a non-specification home; former verbatim: "- **Current** [code]: `keyresolver.cpp:344-367` (\"Strong declared-mode prior\") promotes the highest-ranked declared-compatible result to the front **regardless of score gap** — a hard veto (\"the composer's intent overrides note-content inference\").\n- **Change:** **remove it outright.** It is incompatible with \"note-based primary.\" Leaving it would make §2.1's demotion a no-op wherever note inference already out-scored the declared mode but got vetoed here. The residual declared influence is now *only* the small hint in §2.1." — from `docs/stage4b_design.md`, the Stage-4b design implementing the user's ratified Stage-4 redirect; the staged approach was chosen by the user 2026-06-14, and the document was read in full by READ WAVE 4, 2026-08-04. **What did NOT change: the STATUS.** It remains `superseded-in-fact`, exactly as D-058's did through the identical act — R2 says what the specification owes, not what the register records. **Its subject is the LEGACY key path** (`keymodeanalyzer` / `keyresolver`), which the joint estimator replaced on both surfaces; the ⚠ LEGACY mark stays, because it states what the decision is ABOUT. Landed at the same event as **D-571**. The piece-start shortcut removed alongside it is **D-058**, already recorded *superseded in fact* (`OPEN_ITEMS.md` OI-315) — the Stage-4b design is a second, independent source for that removal and dates it the same way. **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the declared mode's weight (at line 4340 on 2026-08-09), under *"— do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-575 — The Baroque partial-signature convention is handled by DETECTING it and reinterpreting the signature one step, not by widening the candidate family for every score

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **★ THE BAROQUE PARTIAL-SIGNATURE CONVENTION IS HANDLED BY DETECTING IT AND REINTERPRETING THE
> SIGNATURE ONE STEP, NEVER BY WIDENING THE CANDIDATE FAMILY FOR EVERY SCORE (re-homed into this
> specification 2026-08-08 on the user's ruling). ⚠ LEGACY, AND SUPERSEDED IN FACT: the correction is
> applied inside the legacy resolver, which the production arm no longer runs; no ruling superseded
> it, a later build replaced what it governs. Whether the joint estimator handles the convention AT
> ALL is NOT settled by this entry and is not asserted here.** Baroque scores are often notated with
> one accidental fewer than the modern convention, so the sounding key sits one step to the sharp side
> of anything a signature-faithful reading could name. The adopted handling DETECTS that situation —
> the flattened sixth degree pervasive across the sounding weight and dominating its natural form —
> and reinterprets the written signature one step toward the missing accidental for the whole
> resolution.

**In plain words.** Baroque scores are often written with one accidental fewer than the modern convention, so the true key sits one step to the sharp side of anything the analysis could name. The fix adopted detects that situation — the flattened sixth degree being pervasive and dominating its natural form — and reinterprets the written signature accordingly. The alternative considered and not taken was to let every score choose from two signature families, which would have added a competitor to correctly-written music as well.

**Why.** The alternatives are weighed in the document's own §4 with their risks: the signature-flexible option adds a rival family to every piece including correctly-notated ones and could destabilize them; the cadence-based option is the most defensible musicologically and the largest change; reading the annotation fixes the test corpus and does not generalize. The chosen detector is defended as the narrow one, and the document states in terms that its discriminator must key on the specific degree rather than on any accidental, because the leading note is always an accidental in minor.

**Status.** SUPERSEDED IN FACT · decided 2026-06-03 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1917-1933`

**Provenance.** `docs/key_detection_baroque_partial_signature.md`, the 2026-05-23 read-only investigation and its resolution banner. Read in full by READ WAVE 4, 2026-08-04. The banner records the fix as landed at commit `81978321e3` and verified live on the anchor case. **Its subject is the LEGACY key path** — the correction is applied inside `resolveKeyAndModeRanked`, which the production arm no longer runs. Recorded *superseded in fact*: no ruling names it; a later build replaced what it governs. Whether the joint estimator handles the partial-signature convention at all is NOT settled by this entry and is not asserted here. The record states no ratifier. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii), which routes it to *its legacy family's home, superseded-in-fact status and ⚠ LEGACY mark intact*). That family's home is the Layer-3 section of `ARCHITECTURE.md`, where the 2026-08-07 wave homed **D-616** under the same treatment — a legacy key-path decision written into the key layer's specification with the arm mark on it. BOTH MARKS ARE WRITTEN INTO THE HOME TEXT rather than left in this field: the ⚠ LEGACY scope and the superseded-in-fact status, together with the not-asserted clause about the joint estimator, so a reader of the specification meets them with the rule. THE COMMIT HASH AND THE ANCHOR CASE ARE NOT CARRIED ACROSS — D-307 forbids pinning a specification to a code coordinate, and the thresholds are values, so both stay in the record (D-431). FORMER HOME, PRESERVED (#12): `docs/key_detection_baroque_partial_signature.md:3-14`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 1, "section": "# Key/Mode Detection — Baroque Partial-Signature Weakness", "label": "the opening block (above the first section heading)", "delegated": null, "delegation": "CLAUDE.md:519", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "> **RESOLVED 2026-06-03 by commit `81978321e3` (`fix(keyresolver): Option B
> Baroque partial-signature correction`), in HEAD.** Option B from §4 below was
> implemented: the resolver now detects the partial-signature convention (♭6
> pervasive ≥3% of sounding weight AND dominating ♮6 by ≥2×) and reinterprets the
> signature one step toward the missing accidental (minor −1 flat / major +1 sharp)
> for the whole of `resolveKeyAndModeRanked`. Corelli `op01n08d` is now detected as
> **C minor at rank 0 for every region** (verified live 2026-06-08,
> `cc_step3_key_investigation_report.md` Part C); G minor no longer appears at any
> rank. The body below documents the **pre-fix** state and is retained for history.
> The residual `op01n08d` test symptoms (§\"three remaining symptoms\") are
> quality / inversion / segmentation issues, **not** key detection — see the commit
> message of `81978321e3` for the post-fix status of each." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-587 — A user-facing preset presents as a familiar genre-era label plus exemplars the user knows — never as an idiom name or an obscure exemplar; genre names are LABELS over mixtures, never axes

> - **A preset presents as a familiar genre-era label plus exemplars the user knows — never as an
>   idiom name and never as an obscure exemplar; genre names are LABELS over mixtures, never axes.**
>   A preset is named after a period and style a user recognises, anchored by musicians they know
>   ("60s pop — The Beatles"); it is never named after one of the five idioms, and never after an
>   exemplar most people have not heard of. *Why:* the second half is measured and is §6.7's own
>   result — harmony is not organised by genre, and Baroque, galant and Classical share one idiom —
>   so a genre name cannot be an axis without asserting a structure the data denies. The exemplar half
>   is the user's own reason: an exemplar nobody recognises conveys nothing.

**In plain words.** What a user picks is named after a period and style they recognise, anchored by musicians they know. It is never named after one of the five structural idioms, and never after an exemplar most people have not heard of. The genre name is only a label for a blend of idioms — genre is not one of the things the analysis is organised by.

**Why.** Measured, and the measurement is the study this proposal rests on: harmony is not organised by genre — Baroque, galant and Classical share ONE idiom — so a genre name cannot be an axis without asserting a structure the data denies. The exemplar half is the user's own reason, quoted in the decision: an exemplar nobody recognises conveys nothing.

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5628-5635`

**Provenance.** `cowork_style_taxonomy_proposal.md`, RATIFIED 2026-06-30 and EXECUTED at the StyleTag swap 2026-07-02. Read in full by READ WAVE 5, 2026-08-04. Recorded in §6, the user's EXEMPLAR/GENRE proposal of 2026-07-05, marked RECORDED and DEFERRED product work. **D-131** already carries the five-idiom taxonomy itself; this is the separate rule for how a preset built over it is NAMED, which no other home carries. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). Routed into the style-system family: `ARCHITECTURE.md` §6 gains a section for the user-facing preset layer, §6.8, which is where the five preset-layer decisions now live together. THE RECORDED/DEFERRED STATUS RIDES ALONG and is stated in that section's own status line, so no reader takes a deferred product decision for a built one. FORMER HOME, PRESERVED (#12): `cowork_style_taxonomy_proposal.md:96-99`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 87, "section": "## 6. The user-facing preset layer — the EXEMPLAR/GENRE proposal (user, 2026-07-05; RECORDED, deferred product work)", "label": "§6", "delegated": null, "delegation": "ARCHITECTURE.md:4738", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "2. **Naming: exemplar anchoring, genre-era labels.** A preset presents as a familiar label + exemplars users
   know (\"60s pop — The Beatles\"), never as an idiom name or an obscure exemplar (\"Hiromi means nothing to most
   people\" — user). Genre names are LABELS over mixtures, never axes (the study's own result: era/genre is not
   the structure — Baroque/galant/Classical share idiom #2)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-588 — Preset coverage beyond the analysed corpora is three tiers with NO bare guessing — measured, editorially declared with a stated theory rationale, or self-correcting by detection

> - **Coverage beyond the analysed music is three tiers with NO bare guessing — measured, editorially
>   declared with a stated theory rationale, or self-correcting by detection.** A style we hold
>   annotated music for gets its mixture measured from that music. A style we hold none for gets a
>   mixture written down deliberately with its theory reason stated, and validated when data arrives.
>   Either way the analysis moves away from the starting mixture as it reads the actual music. *Why:*
>   the third tier is what licenses the second — because a preset is only a cold-start prior the music
>   itself refines, a declared mixture that is somewhat wrong degrades gracefully; without the
>   self-correction the declared tier would be an unvalidated shipped value (#19).

**In plain words.** A style we hold annotated music for gets its blend measured from that music. A style we hold none for gets a blend written down deliberately, with the theory reason for it stated, and checked when data arrives. Either way the analysis moves away from the starting blend as it reads the actual score, so a badly chosen preset degrades gently rather than being wrong throughout.

**Why.** The third tier is what licenses the second, and the decision says so: because a preset is only a cold-start prior that the score itself refines, a declared blend that is somewhat wrong degrades gracefully — which is what makes shipping a declared blend acceptable at all. Without the self-correction the declared tier would be an unvalidated shipped value (#19).

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5636-5643`

**Provenance.** `cowork_style_taxonomy_proposal.md`, RATIFIED 2026-06-30 and EXECUTED at the StyleTag swap 2026-07-02. Read in full by READ WAVE 5, 2026-08-04. Recorded in §6-3 of the user's 2026-07-05 proposal, RECORDED and deferred as product work. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)) into `ARCHITECTURE.md` §6.8, the new preset-layer section of the style-system family, with the RECORDED/DEFERRED status stated in that section's own status line. THE NAMED CORPORA AND THE NAMED GENRES ARE NOT CARRIED ACROSS: the rule is what is homed, and a list of which held corpora happen to cover which genre today is a state of the holdings rather than a rule (it stays in the proposal, #12). FORMER HOME, PRESERVED (#12): `cowork_style_taxonomy_proposal.md:100-109`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 87, "section": "## 6. The user-facing preset layer — the EXEMPLAR/GENRE proposal (user, 2026-07-05; RECORDED, deferred product work)", "label": "§6", "delegated": null, "delegation": "ARCHITECTURE.md:4738", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "3. **Coverage beyond the analyzed set — three tiers, no bare guessing:**
   - **Measured:** the held research corpora already cover much of the user's example list — CoCoPops =
     Billboard charts (60s pop, disco); HookTheory = modern pop; the WJD carries per-solo style tags
     (dixieland/swing/bebop/postbop); iRb = the standards/crooner book. Per-genre mixtures are computable
     from existing tags.
   - **Declared:** genres with no held data (metal, shoegaze, grunge, hiphop, funk…) get an EDITORIALLY
     DECLARED mixture with a stated theory rationale (e.g. metal ≈ triadic-modal with high power-chord
     admissibility — the L4 §15 O4 constant is the metal-facing knob), validated when data arrives.
   - **Self-correcting:** the §4-4 auto-detection makes any preset a cold-start prior the score itself
     refines — mis-picked presets degrade gracefully, which is what makes declared mixtures shippable." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-589 — Every idiom mixture is selectable and the discovered cloud is the EVIDENCE MAP, not the boundary — each chosen point carries its evidence status

> - **Every idiom mixture is selectable, and the discovered cloud is the EVIDENCE MAP rather than the
>   boundary — each chosen point carries its evidence status.** Named presets are cluster centroids
>   for progressive disclosure; a custom selector admits any point in the mixture space. Where the
>   chosen point sits relative to the music actually measured decides what may be claimed about it:
>   inside a discovered cluster it is validated, between clusters it is an interpolation, outside the
>   cloud it is still selectable but marked empirically unvalidated. *Why:* two standing rules
>   combined — no information loss (#12), since restricting the user to the discovered centroids would
>   discard every point between them, and the empirically-unvalidated mark, which lets a value outside
>   the measured range be offered without being presented as established (#19).

**In plain words.** A user may set any blend of the five idioms, not only the named ones. Where the chosen blend sits relative to the music we actually measured decides what may be claimed about it: inside a measured cluster it is validated, between clusters it is an interpolation, and outside everything measured it is still selectable but is marked as never having been checked against real music.

**Why.** Two standing rules combined, both named in the decision: no information loss (restricting the user to the discovered centroids would discard every point between them), and the empirically-unvalidated mark (a value outside the measured range is selectable but may not be presented as established) — here the A-7 amendment's marking pattern generalised from a preset constant to a point in mixture space.

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5644-5652`

**Provenance.** `cowork_style_taxonomy_proposal.md`, RATIFIED 2026-06-30 and EXECUTED at the StyleTag swap 2026-07-02. Read in full by READ WAVE 5, 2026-08-04. Recorded in §6a, the bidirectional preset-to-mixture contract, user 2026-07-05. The marking pattern it generalises is **D-497** (the empirically-unvalidated mark applied to the Jazz preset constants). ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)) into `ARCHITECTURE.md` §6.8, with the RECORDED/DEFERRED status stated in that section's own status line. FORMER HOME, PRESERVED (#12): `cowork_style_taxonomy_proposal.md:128-132`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 122, "section": "### 6a. The bidirectional preset⇄mixture contract (user, 2026-07-05; RECORDED with §6)", "label": "§6a", "delegated": null, "delegation": "ARCHITECTURE.md:4738", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **Backward — every mixture is selectable; the discovered cloud is the EVIDENCE MAP, not the boundary.**
  Named presets = cluster centroids (progressive disclosure); a custom selector admits ANY simplex point
  (E-14 zero information loss). Each chosen point carries an evidence status: inside a discovered cluster
  (validated) · between clusters (interpolation) · outside the cloud (extrapolation — selectable, marked
  empirically-unvalidated; the A-7-mark pattern generalized to mixture space)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-590 — The score's own metadata is the PRIMARY home of that score's idiom mixture, and a user-set mixture is never silently overwritten by re-detection

> - **The music's own metadata is the PRIMARY home of that piece's idiom mixture, and a user-set
>   mixture is never silently overwritten by re-detection.** The mixture is stored in the score's own
>   user-defined properties, the mechanism MuseScore already saves beside title and composer, so it
>   travels with the file and a later analysis starts warm rather than cold. The stored value records
>   its provenance — auto-detected, with the analyzer version and date, or user-set: a user-set
>   mixture is never silently replaced, an auto-detected one may be refreshed, and an edit after
>   detection marks the stored mixture refreshable. *Why:* storing it with the music removes the need
>   for a separate registry for per-piece behaviour and turns re-analysis into a warm start; the
>   no-silent-overwrite half is the no-surprise rule. **Two things are recorded rather than assumed
>   away:** custom properties survive the native format but their MusicXML round-trip is only partial
>   and needs its own check before the feature relies on it; and the property layout is an
>   implementation decision at build time. **This sits against §13.1's rule that our data lives in
>   separate files inside the archive and the score file is never touched** — the two are not in
>   conflict on their own terms, since this uses MuseScore's existing property mechanism rather than
>   extending the file's own schema, but a build must reconcile them explicitly and neither record
>   does.

**In plain words.** A piece's blend of idioms is stored inside the piece's own file, using the score properties MuseScore already saves beside title and composer. So it travels with the file and a later analysis starts warm instead of cold. The stored value records whether a person set it or the program detected it: a person's setting is never quietly replaced, a detected one may be refreshed, and editing the score marks it as due for refresh.

**Why.** Stated with the decision: storing it in the file makes the mixture travel with the piece, so no separate registry is needed for per-score behaviour, and re-analysis becomes a warm start rather than a cold one. The no-silent-overwrite requirement is named as the no-surprise rule. One caveat is recorded rather than assumed away: custom metadata survives the native format but its MusicXML round-trip is only partial and needs its own check before the feature relies on it.

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5653-5668`

**Provenance.** `cowork_style_taxonomy_proposal.md`, RATIFIED 2026-06-30 and EXECUTED at the StyleTag swap 2026-07-02. Read in full by READ WAVE 5, 2026-08-04. Recorded in §6a, user 2026-07-05, as RECORDED and deferred product work. It sits against **D-158**, which rules that OUR data lives in separate files inside the score archive and the score file is never touched — the two are not in conflict on their own terms (this uses MuseScore's OWN existing score-property mechanism rather than adding to the score file's schema), but a build would have to reconcile them explicitly and neither record does. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)) into `ARCHITECTURE.md` §6.8, with the RECORDED/DEFERRED status stated in that section's own status line. THE TENSION WITH D-158 IS CARRIED INTO THE HOME TEXT rather than left in this field alone, because a reader of the rule needs to meet it (#12); it is stated as a pointer to §13.1, which is D-158's home, and not as a second copy of that rule (#6). FORMER HOME, PRESERVED (#12): `cowork_style_taxonomy_proposal.md:140-152`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 122, "section": "### 6a. The bidirectional preset⇄mixture contract (user, 2026-07-05; RECORDED with §6)", "label": "§6a", "delegated": null, "delegation": "ARCHITECTURE.md:4738", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **The mixture's PRIMARY persistence home = the score itself (user, 2026-07-05).** Store the score's
  idiom mixture in the score's own metadata — MuseScore already supports user-defined score properties
  alongside title/composer (the metaTag mechanism, saved inside .mscz/.mscx). Consequences: the mixture
  TRAVELS with the file (no separate registry needed for per-score behavior); re-analysis seeds from it
  (the §4-4 cold-start prior becomes a warm start); \"save as named preset\" then reads FROM the score
  property (per-score setting vs reusable preset = two homes for the same mixture object, score-first).
  Requirements recorded now: (1) **provenance on the stored value** — auto-detected (analyzer
  version + date) vs user-set; a USER-set mixture is never silently overwritten by re-detection (the
  no-surprise rule), an auto-detected one may be refreshed; (2) **staleness** — a score edited after
  detection marks the stored mixture refreshable; (3) **interchange caveat** — user-defined properties
  survive the native format; MusicXML round-trip of custom metadata is partial and needs its own check
  before the feature relies on it; (4) the property schema (one namespaced JSON-valued tag vs several
  tags) is an implementation decision at build time, not now." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-591 — The licence split for the style system: the ANCHORS are the shipped licence-constrained fitted parameters, and the mixture weights are free user configuration

> - **The licence split: the ANCHORS are the shipped licence-constrained fitted parameters, and the
>   mixture weights are free user configuration.** The constraint that a value which SHIPS may be
>   fitted only on freely-licensed music reaches the per-idiom anchors, not the mixture a user chooses
>   over them; a user's own mixture carries no constraint at all, and only the mixtures we ship as
>   named preset defaults must be derived from a licensed pool or editorially declared. *Why:* it
>   follows from what each half is — an anchor is a fitted parameter compiled into the product, so the
>   fitting-pool constraint reaches it, while a mixture weight the user selects is configuration
>   derived from no corpus at all. This REFINES the fitting-pool constraint by saying which half of
>   the style system it reaches; it does not weaken it.

**In plain words.** The licensing rule that limits which music our shipped numbers may be fitted on applies to the per-idiom reference values, not to the blend a user chooses over them. A user's own blend carries no constraint at all; only the blends we ship as named defaults must come from freely-licensed music or be declared editorially.

**Why.** It follows from what each half IS, which the decision states: the anchors are fitted parameters compiled into the product, so the fitting-pool licence constraint reaches them; a mixture weight the user selects is configuration and is derived from no corpus at all, so nothing constrains it.

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5669-5677`

**Provenance.** `cowork_style_taxonomy_proposal.md`, RATIFIED 2026-06-30 and EXECUTED at the StyleTag swap 2026-07-02. Read in full by READ WAVE 5, 2026-08-04. Recorded in §6a. It REFINES **D-292** (the fitting-pool licence constraint — values that ship are fitted only on freely-licensed music) by saying which half of the style system that constraint reaches; it does not weaken it. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)) into `ARCHITECTURE.md` §6.8, with the RECORDED/DEFERRED status stated in that section's own status line. The fitting-pool constraint itself is NOT restated at the new home (#6) — it is stated once at the joint estimator's standing rule (e) — and the refinement is written as a refinement. FORMER HOME, PRESERVED (#12): `cowork_style_taxonomy_proposal.md:133-135`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 122, "section": "### 6a. The bidirectional preset⇄mixture contract (user, 2026-07-05; RECORDED with §6)", "label": "§6a", "delegated": null, "delegation": "ARCHITECTURE.md:4738", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **License split, resolved cleanly:** the ANCHORS are the shipped license-constrained fitted parameters;
  MIXTURE WEIGHTS are user configuration (free); only OUR shipped named-preset defaults carry the §6-4
  derivation constraint (licensed-pool-derived or editorially declared, NC-validated)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-598 — The style taxonomy and the per-style weights are ONE data-derived object; VALIDATION is a separate third thing that needs annotated scores and is not delivered by the clustering

> - **The taxonomy and the per-style weights are ONE data-derived object; VALIDATION is a separate
>   third thing the clustering does not deliver.** Discovering which idioms exist and estimating how
>   strongly each one weighs are not two derivations: the clusters and their feature distributions
>   are the same object read two ways. Measuring whether the analysis actually improves when it uses
>   an idiom is a THIRD job, and it needs annotated music — notes together with a published human
>   analysis — which the clustering does not supply. *Why:* it follows from what a cluster is, so no
>   second derivation produces the weights; and the separation is forced by what validation measures,
>   the analysis's USE of an idiom, which cannot be observed without a human analysis to compare
>   against.

**In plain words.** Discovering which styles exist and measuring how strongly each one weighs are not two jobs — they are the clusters and their distributions, one result. Checking whether the analysis actually gets better when it uses a style is a third, separate job, and it needs music with both the notes and a published human analysis, which the clustering does not supply.

**Why.** It follows from what a cluster IS: a cluster and its feature distribution are the same object read two ways, so no separate derivation produces the weights. The separation of validation is forced by what it measures — the analyzer's USE of a style, which cannot be observed without a ground-truth analysis to compare against.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5586-5594`

**Provenance.** `cowork_style_clustering_plan.md`, committed future direction, user-ratified 2026-06-29. Read in full by READ WAVE 5, 2026-08-04. It is why **D-132** records the weights half as the REMAINING empirical grounding after the five-idiom set was ratified: the same clustering delivers both, and only the second is still owed. The document's licensing rule is **D-292** and is not re-entered here (#6). ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). Routed to `ARCHITECTURE.md` §6.7, the section that owns the taxonomy this decision is about, in that section's own voice and with its defense. FORMER HOME, PRESERVED (#12): `cowork_style_clustering_plan.md:16-18`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 9, "section": "## 1. What it is", "label": "§1", "delegated": null, "delegation": "ARCHITECTURE.md:4752", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "The **taxonomy and the weights are one data-derived object** (the clusters and their distributions). **Validation** —
measuring our analyzer's *use* of a style — is a **separate third thing** that needs annotated *scores* (notes + a
ground-truth analysis), not the clustering." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-616 — A global tonic anchor enters key scoring at RESOLVER/SECTION scope — never as one more local term inside the window scorer, which is what re-enters the coupling that defeated the local levers

> - **A global tonic anchor enters key scoring at RESOLVER / SECTION scope — never as one more local
>   term inside the window scorer. ⚠ LEGACY: both mechanisms it names are legacy-scoped.** Evidence
>   about which key a whole section or piece is in is applied where the section is decided — the
>   scope the removed declared anchor occupied — gating the relative-major/minor choice; the
>   per-window candidate scoring is left unchanged. *Why:* measured, at the attempt that failed —
>   local reweighting was shown unable to carry the relative-major/minor decision, because that floor
>   is made of near-ties and any local term strong enough to win them without the mode present also
>   overrides the correct reading when it is present. Adding the anchor as one more local term
>   re-enters exactly that coupling. The design attaches a proof obligation to the rule: show that
>   the anchor reinforces the mode-present cases rather than regressing them. **The LEGACY mark
>   follows a check at the code, not the decision's age:** the window scorer this rule excludes
>   (`KeyModeAnalyzer::analyzeKeyMode`) is reached only through the legacy resolver and this layer's
>   dormant sequence decoder, and the resolver is retired from the production region path — so
>   neither named mechanism is on an arm that runs. The rule about WHERE a section-scoped prior is
>   applied binds any such prior the key axis later gains.

**In plain words.** Evidence about which key a whole passage is in is applied where the passage is decided, not inside the per-window scoring that ranks candidate keys note by note. Adding it as one more local term is what failed before: any local term strong enough to settle a near-tie when the mode is unknown also overrides the correct answer when the mode IS known.

**Why.** Measured, at the attempt that failed: local reweighting was shown unable to carry the relative-major/minor decision, because the floor is made of near-ties and any local term strong enough to win them without the mode present overrides the correct reading when it is present. The scope constraint is the structural remedy for exactly that coupling, and the design attaches a proof obligation to it — show that the anchor reinforces the mode-present cases rather than regressing them.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Home.** `ARCHITECTURE.md:1879-1893`

**Provenance.** `docs/stage4c_cadence_key_design.md` §3, the Stage-4c cadence-to-key design, DRAFT and ratification-gated, 2026-06-14. Read in full by READ WAVE 6, 2026-08-04. Its own §7 puts this scope constraint to the user for approval and the record does not state that the ratification happened, so no ratifier is recorded. ⚠ The mechanism is on the LEGACY key path and the local key-agnostic cadence approach was later FALSIFIED at its precision ceiling (**D-290**) — but this entry is about WHERE a global prior is applied, not about that detector, and the same constraint binds any section-scoped evidence the key axis gains. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed to the Layer-3 section, and the ruling requires the LEGACY mark to follow an ARM CHECK AT THE CODE rather than the entry's age (dispatch assumption A5). ★ THE CHECK WAS RUN BEFORE THE HOME TEXT WAS WRITTEN, and both named mechanisms come back LEGACY-SCOPED: the window scorer the rule excludes, `KeyModeAnalyzer::analyzeKeyMode`, has exactly two non-test callers — the legacy resolver (`src/composing/analysis/key/keyresolver.cpp:314`) and this layer's dormant sequence decoder (`src/composing/analysis/key/keymodesequence.cpp:147`) — and the resolver end, `resolveKeyAndModeRanked`, is retired from the production region path, its remaining production call sites being the legacy arms (`src/composing/analysis/region/regionanalyzer.cpp:443` and `:606`, `src/notation/internal/notationcomposingbridgehelpers.cpp:186`). So the LEGACY mark is written into the home text WITH the check that produced it, and the arm is not mixed. What is NOT legacy-scoped is stated beside it: the rule about WHERE a section-scoped prior is applied binds any such prior the key axis later gains. FORMER HOME, PRESERVED (#12): `docs/stage4c_cadence_key_design.md:62-70`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 60, "section": "## §3 — Feeding key scoring WITHOUT re-entering the §4 coupling (the load-bearing constraint)", "label": "“§3”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "The anchor must act like the declared mode did — a **section/piece-scoped global prior** on tonic+mode that
breaks the relative-pair tie — **NOT** a per-candidate local-salience term inside `analyzeKeyMode`'s
252-candidate window scoring. If it is added as just another local term, it re-enters the coupling and
fails like 4b-ii's levers. Concretely: apply a cadence-anchor bonus at the **resolver / section level**
(the scope the removed declared anchor occupied), gating the relative-pair choice; keep `analyzeKeyMode`'s
per-window scoring unchanged." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-618 — The notated key signature is NOT a hard fact — its fifths were measured to pin wrong about one time in six, so the home key is note-derived and never signature-pinned

> - **The notated key signature is NOT a hard fact, so the home key is derived from the notes and is
>   never signature-pinned.** The signature's fifths were measured against the true home key and pin
>   the wrong one on a substantial minority of the material, concentrated in modal and partial
>   signatures; the signature is therefore soft evidence that leans. *Why:* this is the rule above
>   working rather than an exception to it — a candidate hard constraint measured to pin a wrong
>   answer is demoted to a score. The measured rate is in the record that produced it and is not
>   restated (D-431). **Scope, stated because it decides how the finding is read:** it is a property
>   of the written music and its human analyses, not of any one of our pipelines, so it survives the
>   arm change; the mis-keying case that shows it in the score is recorded with the legacy key path
>   and carries its own ⚠ LEGACY mark there.

**In plain words.** Some evidence is decisive enough to rule readings out outright — which pitches sound, when, how long, and a complete unambiguous triad on a strong beat. The written key signature is not in that class: it names the wrong home key about one time in six, mostly in modal and partial signatures. So the home key is worked out from the notes, and the signature only leans.

**Why.** Measured, and the measurement is what moved it: the signature's fifths were tested against the true home key and pinned wrong on roughly seventeen per cent of the material, concentrated in modal and partial signatures. The demotion is not an exception to the scheme but the scheme working — a candidate hard constraint that is measured to pin a wrong answer becomes a soft score, because a wrong constraint pinning a wrong answer is the failure the hard/soft split exists to prevent.

**Status.** LIVE · decided 2026-06-15 · ratifier not stated

**Home.** `ARCHITECTURE.md:521-530`

**Provenance.** `docs/architecture_joint_inference.md` §2, the constrained-joint-inference architecture direction, investigation-confirmed 2026-06-15 and marked ratifiable-but-not-built. Read in full by READ WAVE 6, 2026-08-04. ⚠ The DOCUMENT is superseded as an architecture proposal — `ARCHITECTURE.md` §2.14 records the joint-decode synthesis as superseded by the effort-preset design and retained only as history, and the ratified estimator is **D-001** — but this measured fact about the key signature is not a proposal and is carried by no other home. It is the same class of finding as **D-575**/the partial-signature mis-keying record. The record states no ratifier. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). ★ ASSUMPTION A4 DISCHARGED BY READING, NOT ASSUMED: the supersession was read at `ARCHITECTURE.md:960-961` — *"The `docs/architecture_joint_inference.md` joint-decode synthesis is **superseded** by this, retained only as history"* — and it reaches the PROPOSAL's shape, not this measurement. The content is therefore LIVE and is homed; the supersession is stated at the new home so no reader takes the surrounding proposal for a specification. Routed to the joint-estimator section of `ARCHITECTURE.md`, in a subsection of its own, with the general rule it is an instance of (D-619) beside it. THE MEASURED RATE IS NOT CARRIED ACROSS (D-431) — the direction and the concentrated class are stated and the number stays in the record. FORMER HOME, PRESERVED (#12): `docs/architecture_joint_inference.md:45-51`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 41, "section": "## §2 — The structure: CONSTRAINED joint inference (hard constraints + soft scores)", "label": "“§2”", "delegated": null, "delegation": "ARCHITECTURE.md:858", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **Hard constraints** — decisive evidence that **disqualifies** alternatives outright or **pins** a
  solution: \"this IS C major, whatever the soft hints say.\" These are the **raw facts** (which pitches
  sound, when, with what duration / metric weight / bass) plus the genuinely-unambiguous analyses (a
  complete clear triad on a strong beat). They **prune** the hypothesis space. **⚠ Note (J-key-i,
  2026-06-15): the notated key signature is NOT among the hard facts** — its fifths were measured to pin
  wrong ~17% (modal/partial signatures), so the home key is soft / note-based, not signature-pinned. The
  safety gate doing its job: a candidate hard constraint that pins wrong is demoted to soft (§5)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-622 — The reach-back convergence PROXY was measured FALSE and dropped — the as-built tracks the leading-edge key itself and stops when it stops changing

> - **The reach-back convergence PROXY was measured FALSE and is dropped; the as-built tracks the
>   leading-edge key itself and stops when that stops changing.** The cheaper stopping rule proposed
>   in design — *a settled, stable prevailing key is in view in the reached-back region* — was
>   measured and disproved: one settled indication of context does not anchor the leading edge, which flips
>   only once a confident earlier key is established over a **run**. So the facility uses the
>   headline criterion directly and no proxy. *Why:* measured at the build, and the methodological
>   reading is recorded with the result — the proxy was an unlabelled assumption, it was measured, it
>   was false, and it was dropped; a determinism test over extension step size is what validates the
>   criterion that replaced it. This is the finding that supersedes the proxy clause of the
>   bounded-context contract's convergence item; that contract now records the clause as tried and
>   closed, and its headline rule — reach back until the answer stops changing, never by a chosen
>   amount — is unchanged.

**In plain words.** When the analysis has to read backwards for context, it needs a rule for when it has read far enough. The cheap rule proposed in design — stop once a settled key appears anywhere in the material read back — was measured and found to stop too early: one settled measure does not fix the key at the edge of the selection, which only settles once a confident earlier key is established over a stretch. So the built code checks the thing that actually matters and stops when that stops moving.

**Why.** Measured at the build, and the measurement is what decided it: the phase-3 measurement showed a single settled context measure does not anchor the leading edge, while a confident earlier key established over a run does. The document states the methodological reading with the result — the proxy was an assumption, it was measured, it was false, and it was dropped — and names the determinism test over extension step size as what validates the criterion that replaced it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1894-1905`

**Provenance.** `cowork_layer3_reachback_design.md` §3, the Layer-3 reach-back detail design, BUILT as a capability gated off by default. Read in full by READ WAVE 6, 2026-08-04. Verified at the code rather than taken from the design: the production source records the proxy as found to stop PREMATURELY at the convergence note above the reach-back loop, and implements the headline criterion directly. The record states neither a date nor a ratifier for this item. ★ **THIS ENTRY IS RECORDED AS SUPERSEDING THE PROXY CLAUSE OF D-261, on the user's ruling of 2026-08-07** (dispatch `cc_instruction_five_rulings.md` §0a R3; `OPEN_ITEMS.md` OI-331, which flips on it). The clause is STRUCK from `cowork_bounded_context_design.md` §3 item 6 and recorded there as tried and closed with this measurement as its evidence; D-261's verbatim is re-taken from the edited home with its former verbatim preserved in its own provenance (#12), and D-261's headline rule and ratified status are unchanged. ★ THE CONTRADICTION THIS ENTRY FORMERLY RECORDED IS RESOLVED, and what it said is kept (#12): '★ **THIS ENTRY CONTRADICTS A LIVE, USER-RATIFIED ENTRY: D-261**, whose verbatim names this same proxy as the worked example of a domain proxy and states that *"the proxy is validated once, in design, to imply convergence"* — a clause the measurement above refuted before D-261 was ratified on 2026-08-02, and which carries no annotation. … Tracked at `OPEN_ITEMS.md` OI-331; NOT resolved here, because which of the two the record means to keep is a ruling.' The user ruled the third of the three remedies that row put: strike the clause and record this entry as superseding it, the rule itself standing. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The SITE was never in doubt — the Layer-3 section owns the mechanism — and what held the entry back was the OPEN user ruling at `OPEN_ITEMS.md` OI-331. THE HOLD IS LIFTED BY THE USER'S RULING, which this act carries out: the entry is written into the Layer-3 section in that section's own voice, with its defense, and the bounded-context contract's annotation points at it, each surface stating its own concern. The supersession this entry records is unchanged and is not re-decided here. FORMER HOME, PRESERVED (#12): `cowork_layer3_reachback_design.md:76-82`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 68, "section": "## 3. The trigger and the convergence stop (no amount-guessing)", "label": "§3", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **Proxy REJECTED by measurement (as-built uses the headline criterion directly).** The earlier draft proposed a
  cheaper proxy — *"a settled, stable prevailing key is in view in the reached-back region"* — "validated once in
  design." Phase-3 measurement **disproved** it: one settled *context* measure does **not** anchor the leading edge;
  the leading-edge key flips only once a confident earlier key is established over a **run** (e.g. a V–I two measures
  back). So the as-built tracks the **leading-edge key across iterations and stops when *it* stops changing** — the
  headline criterion itself, no proxy." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).


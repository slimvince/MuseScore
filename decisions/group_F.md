# Decisions group F — Layer 3 — key and mode

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-051 — The production key/mode path is the sequence decoder, not the per-stretch resolver

> **The production region key/mode path is the decoder, not the per-region resolver.**

**In plain words.** The tonality is worked out for the whole piece at once, as a sequence, rather than separately for each stretch.

**Why.** derivation not recorded.

**Status.** SUPERSEDED BY D-001 · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1271`

**Provenance.** The joint estimator now decides key on both surfaces (D-005, D-010). The Layer-3 section still reads 'Built+Live' - see OPEN_ITEMS OI-232

### D-052 — The signature read and declared-mode mapping live in ONE shared function

> The signature read + declared-mode
> mapping + declared-gated Baroque `partialSignatureCorrection` was lifted verbatim into a shared
> public `resolveKeySignatureContext`, **called by both** the resolver and the wiring — so no
> signature/partial-correction logic is duplicated.

**In plain words.** Reading the printed key signature and turning it into a starting assumption happens in one place that both callers use, so the two cannot drift apart.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1293-1296`

**Provenance.** ARCHITECTURE.md:1291-1296

### D-053 — The tick-local path keeps the older resolver (the ratified P4-defer)

> **P4 tick-local still uses `resolveKeyAndModeRanked` + `collectPitchContext`** (the ratified
>   P4-defer).

**In plain words.** One narrow fallback - answering about a single moment when no surrounding stretch is available - still uses the older method. That was a deliberate deferral.

**Why.** derivation not recorded.

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1307-1308`

**Provenance.** On the switched build the note-seam funnel returns from the record arm before this fallback is reachable (notationcomposingbridge.cpp:728-738). The D-P4 revisit trigger (D-063) was never discharged

### D-054 — All 21 modes are scored against all 12 tonics; the harmonic major family is deferred

> Harmonic major modes are
> significantly rarer as tonal centers than melodic and harmonic minor modes, and the
> validation corpus is unlikely to calibrate them well.

**In plain words.** The key finder considers 21 scale types on each of the 12 possible tonics. The harmonic major family was left out because it is rare and we have no annotated music to calibrate it against.

**Why.** Recorded for the DEFERRAL half only, ARCHITECTURE.md:2459-2463: the harmonic major modes are significantly rarer as tonal centers than the melodic and harmonic minor modes, and the validation corpus is unlikely to calibrate them well. Why the other 21 modes are all scored against all 12 tonics has no recorded derivation.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2460-2462`

**Provenance.** ARCHITECTURE.md:2394-2395 (21 modes), :2213-2217 (harmonic major deferred)

### D-055 — The 21 mode priors are independent and user-configurable

> **21 independent additive priors**, one per mode, user-configurable
>   via `IComposingAnalysisConfiguration::modePrior{ModeName}()`

**In plain words.** How likely each scale type is considered to be is a separate adjustable number per scale type, exposed in the preferences.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2408-2409`

**Provenance.** ARCHITECTURE.md:2408-2410, :3020-3073. Superseded on the production path by D-003 (inference is preset-independent)

### D-056 — Notes always win - the notated key signature is a weak hint, not a bypass

> The key/mode inferrer always runs. The notated key signature's `KeyMode` enum
> (`MAJOR`, `MINOR`, etc.) is no longer a bypass gate — it is passed as a weak hint
> (`declaredMode`) to `analyzeKeyMode()`

**In plain words.** The key printed at the start of the score does not settle the question. It only nudges the answer; what the notes actually do decides.

**Why.** Stated constraint, ARCHITECTURE.md:3382-3384: the notated signature is what the composer wrote down, not what the music does - a piece may modulate, be notated in a partial signature, or contradict its own signature - so it enters as a weak hint the sounding notes can outvote.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3382-3384`

**Provenance.** ARCHITECTURE.md:3380-3392

### D-057 — The priority of evidence - actual sounding notes are the strongest evidence

> | Strongest | Actual sounding notes | what is literally happening now |

**In plain words.** In deciding the key, what is actually sounding right now outranks the surrounding bars, which outrank the printed key signature, which outranks the major/minor tag on it.

**Why.** Stated constraint, ARCHITECTURE.md:3396-3403: the priority table ranks the actual sounding notes the strongest evidence, above the notated signature and above any prior result, for the same reason as D-056.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3400`

**Provenance.** ARCHITECTURE.md:3396-3403. Cited by open_items/OI-228 as the primary source the joint emission departs from. NOT catchable by the harvest's signature net - the reason this adjudication had to read the specifications in full

### D-058 — The piece-start shortcut

> when the
> analysis tick is within the first 16 quarter-note beats (a separate constant from the 16-beat lookback window below —
> they coincide in value, not by design), no prior result exists (`prevResult == nullptr`),
> and the key signature carries an explicit mode, the function returns the declared mode
> immediately (confidence 0.5) rather than waiting for pitch evidence that cannot yet exist.

**In plain words.** At the very start of a piece there is not yet enough music to judge the key, so if the score declares major or minor the program simply believes it, marked as a middling-confidence answer.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3387-3391`

**Provenance.** ARCHITECTURE.md:3387-3392 calls it 'a deliberate pragmatic choice for the score opening, not a general bypass'. NOT catchable by the harvest's signature net

### D-059 — The temporal window - 16 beats back, 8 beats forward, decayed

> The bridge uses a 16-beat lookback + 8-beat lookahead window:

**In plain words.** To judge the key at a point, the program looks about four bars back and two bars forward, giving less weight to music further away.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3425`

**Provenance.** ARCHITECTURE.md:3423-3435; legacy-arm only since the switch (D-010). Derivation not recorded: the only stated basis for 16 and 8 is the in-code gloss '~4 measures in 4/4' / '~2 measures ahead' (ARCHITECTURE.md:3428-3429) - no theory citation and no measurement

### D-235 — Tonal-centre disambiguation may break a close tie but may not overturn a stronger raw winner

> The key-signature path uses a separate focussed `tonalCenterScore` formula for the
> final same-key-signature family decision, independent of the main scoring weights so
> both can be tuned without cross-interference. For diatonic family decisions, tonal-
> centre disambiguation is now guarded by the raw candidate score: it may break close
> same-key-signature ties, but it must not overturn a materially stronger raw winner.

**In plain words.** The same-key-signature family decision is scored by its own formula, separate from the main key weights. On diatonic families that separate decision is allowed to settle a near-tie, but a candidate that already wins the raw scoring by a clear margin stands.

**Why.** The constraint stated in the record: the two formulas are kept independent so both can be tuned without cross-interference; the raw-score guard bounds what the secondary formula may do. The measurement that set the guard's bar is not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2414-2418`

**Provenance.** ARCHITECTURE.md:2414-2418; the same guard is listed among the key-path scoring terms at :2480-2482 ★ RATIFIED (user, 2026-08-02, the residual-pass queue).


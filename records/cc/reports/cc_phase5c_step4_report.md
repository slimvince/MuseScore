# Phase 5c — Step 4 (Layer 5 / FUNCTION): tonicization vs modulation (§5.3) + the modulation recompute (§5.4) + the two standing pins

> **Discipline:** Step 4 of `cowork_phase5c_l5_build_plan.md`, against the SIGNED contract
> `cowork_layer5_function_design.md` §5.3 + §5.4 + §8 + §15-3 + the §5.0 shared defs. Built **DORMANT** (one new
> unit + two pins on dormant/gated-off carries) → **byte-identical on production**. **Default constants only —
> firewall, no tuning (§4).** **REUSE, not re-implement.** This dossier is gitignored.
>
> **Prior HEAD `44e83f2d47`** (Step-3 STATUS entry). **§0 sweep `4f63d2ab40`.** Step-4 code + pins + tests committed
> on top (sha in §Commits).

## 0. Result — GREEN, built, all gates pass

- **§0 sweep:** the unstaged Cowork doc (the §5.5 override-scope / Step-M note in `cowork_layer5_function_design.md`)
  committed local-only `4f63d2ab40` (`docs(cowork): Phase-5c Step-3 ratification + Step-4 prep`).
- **§1 reuse confirm:** every reuse target is consumable and live; the two pins are byte-identically landable → **no STOP.**
- **§2/§3 build + the two pins + §5 tests** committed (see §Commits). **Build clean** (all targets link).
- **`composing_tests` 936 → 942 (+6** FunctionModulation; the lock-in test was *updated* not added). **`notation_tests`
  53** (4 skipped, baseline). **`pipeline_snapshot_tests` 11/11 — NO golden refresh** (the serialized-output byte-identity
  proof). **Corpus 53 / 24 / 53 — overwrite-and-regen byte-identical** on all three presets (`tools/corpus/` git-clean
  after a full regen — the definitive `.ours.json` byte-identity proof for the live-path pin).

---

## §1 — INVESTIGATE-confirm (read-only) — GREEN, no STOP

The reuse landscape is the heart of this step; each target was confirmed at source:

| Reuse target | What it gives Step 4 | Status |
|---|---|---|
| **`localmodulationdetector::detectLocalModulations`** (`section/localmodulationdetector.{h,cpp}`) | the **key-agnostic, established + cadence-confirmed** local-key-span substrate (`LocalKeySpan{startTick,endTick,tonicPc,minorMode,establishmentChords,confirmingCadenceCount,agreesWithAnchor}`); a span commits only on a sustained collection-consistent run (`kEstablishmentMinChords=5`) **with** a confirming cadence | ✅ consumable as the **§5.3 substrate** |
| **`functioncadence::detectFunctionalCadences`** (Step 2) | the §5.2 `FunctionalCadence{tonicPc,minorMode,arrivalTick,tonicVote,type}` stream — the **cadence-confirmation gate (cond a)** + the **accumulated cadential weight (cond b)** | ✅ consumable |
| **`forwardoverride::OnePassClosure`** (Step 3) | the §8 confidence-weighted threshold + one-pass closure + localized forward recompute — **reused as §5.4's second instance** | ✅ consumable, **no back-edge needed** |
| **`jointkeydecision` + the J-key-iii re-key path** (`regionanalyzer::applyJointKeyWiring`, gated on `jointKeyWiringEnabled()`, **default-OFF**) | the §5.4 recompute substrate (override the region key + re-emit) — the **pin-#2** target | ✅ gated-off ⇒ pin byte-identical |
| **The L3 region key-alternatives carry** (`HarmonicRegion::keyAlternatives/keyConfidence`, filled by `regionanalyzer::localKeyForRegion`) | the **v1 placeholder** (representative-slice alternatives) — the **pin-#1** target | ✅ no production consumer ⇒ pin byte-identical |

**The sustained-run-gate ↔ hysteresis difference (the part to adapt, §2):** the detector's persistence is a **fixed
sustained-run gate** (`kEstablishmentMinChords=5` chords — a count). §5.3 specifies persistence as a **change-cost
(hysteresis)** over **duration + accumulated cadential weight**. Resolution (build-detail, §2): the detector's
`kEstablishmentMinChords` floor is left intact as the **candidate floor** (untouched, not re-tuned — modifying it would
move the detector's own diagnostic + test); the **§5.3 hysteresis is layered in the arbiter** over the detector's
committed candidate spans, measured in the span's duration + the §5.2 cadential weight. This adapts the cadence-confirmed
substrate to the spec's persistence form **by reuse, not re-implementation**.

**No input unreachable; no pin un-landable byte-identically; the recompute needs no back-edge → proceeded.**

---

## §2 — BUILD §5.3 (tonicization vs modulation), dormant — `function/functionmodulation.{h,cpp}`

`decideTonicizationVsModulation(detected, cadences, spellingSupport, params)` over the detector's committed candidate
spans:

- **default-tonicize:** `isModulation` is false unless all conditions fire; the home key holds by default.
- **the cadence-confirmation gate (cond a, NECESSARY):** a span is confirmable only if the §5.2 `FunctionalCadence`
  stream has ≥1 cadence voting for the span's `(tonicPc, minorMode)` whose `arrivalTick` falls inside the span. No
  cadence ⇒ tonicization regardless of length (the gate failing, not a cost outweighed).
- **persistence as a change-cost / hysteresis (cond b):** `persistenceEvidence = wDuration·durationWholeNotes +
  wCadentialWeight·accumulatedCadentialWeight + wSpelling·spellingSupport`; `isModulation = !isHomeKey ∧
  cadenceConfirmed ∧ persistenceEvidence > changeCost`. The cost falls as the candidate area's **duration** and
  **accumulated §5.2 cadential weight** grow — the two quantities **trade off against one cost** (so §5.3's "never a
  fixed beat count" is honoured: no standalone duration gate; the duration unit is the fixed whole-note = 1920 ticks).
- **the break-even defaults to tonicization:** the inequality is **strict `>`**, so at the exact break-even the home key
  holds.
- **the notated-spelling key signal (function-gated):** consumed as the optional per-span `spellingSupport` soft input
  to cond (b) (empty ⇒ neutral/false in the dormant unit; wired at engage from each area's accidental/signature
  consistency) — one input to (a)/(b), never a standalone gate.
- **the home/away tag is reused** from the detector (`agreesWithAnchor` ⇒ `isHomeKey`): a home-key span is never a
  modulation candidate.

`detectAndDecideModulations(regions, cadences, fifths, …)` is the concrete reuse path — it **calls
`detectLocalModulations` end-to-end** then `decideTonicizationVsModulation` (the §5 reuse test exercises it).

## §3 — BUILD §5.4 (the modulation recompute, §8 case-4 #1), dormant — REUSE `forwardoverride`

`modulationRecompute(modulation, homeKeyConfidence, first, last, reread, closure, keyDecisionId, params)`:

- fires iff `modulation.isModulation` **and** the cadence is decisive — the **accumulated cadential weight** (the
  cadence-strength term of §5.4) crosses the **§8 bar scaled to `homeKeyConfidence`** via
  `closure.tryOverride(keyDecisionId, homeKeyConfidence, modulation.cadentialWeight)`. (§5.3 owns the persistence/
  duration call; §5.4's §8 bar is **cadence-strength vs key-confidence**, per the spec.)
- on fire: the key decision is **closed for the pass** (no re-open), then a **single forward sweep**
  `closure.forwardRecompute(first, last, …)` re-reads each slice in the new key (`reread(sliceId, newTonicPc,
  newMinor)`). The sweep is **re-entrancy-guarded** (no recursion) and sends **nothing upstream** (no back-edge).
- **REUSE only** — no new mechanism: `OnePassClosure`/`ForwardOverrideParams` are Step-3's. This is the §8 mechanism's
  **second instance**, exactly as the §8 contract anticipates.

### ★ The two standing pins (§15-3) — first tasks of this step, byte-identically landed

**Pin #1 — the region key-alternatives reduction, pinned precisely** (`regionanalyzer::localKeyForRegion` +
`HarmonicRegion`/`RegionKeyReduction` comments + the lock-in test). The byte-identical **v1** carried the *representative
slice's own* ranked alternatives. The **pinned** reduction is the **region-level candidate-key menu the modulation
recompute actually selects among**: every key the region's slices ranked — **each slice's chosen key AND its ranked
alternatives** — bucketed by `(tonicPc, mode)`, weighted by overlap duration, **excluding the chosen region key**, ranked
by accumulated support. Built as a **separate `menu` accumulation** kept apart from the chosen-only `votes` (which still
drives `best`), so the **chosen key and its sequence-margin confidence are bit-identical** — only `keyAlternatives`
changes. (First implementation attempt bucketed *chosen-only* keys, which collapsed a single-key region's menu to empty
and tripped the lock-in test; the corrected reduction aggregates the per-slice alternatives, which is also what the §5.4
override needs — the plausible keys a later cadence could pick.) The lock-in test
(`regionanalysis_tests OverrideReadiness_…`) was **updated** to the pinned reduction: a confident region carries a
non-empty menu of **distinct** candidate keys, each other than the chosen (the region-level bucket property).

**Pin #2 — re-derive the carry in the J-key-iii re-key path** (`regionanalyzer::applyJointKeyWiring` step (d)). The
gated-off joint re-key overrode `region.keyModeResult` **without** updating the carry. It now **re-derives the carry
alongside its override**: `keyAlternatives` ← the region's ranked candidate keys (`perRegionRanked[i]`) **minus the
now-chosen** `(jt, jm)`; `keyConfidence` ← the overridden key's confidence (this path has no L3 sequence-margin, so the
joint emission confidence stands in, on the same `[0,1]` override-bar scale). So the carried menu cannot go stale against
the overridden key.

## §4 — Constants — firewall DEFAULTS, no tuning

`ModulationParams{baseChangeCost 1.0, wDuration 1.0, wCadentialWeight 1.0, wSpelling 0.5, override = kDefaultForwardOverrideParams (baseBar 1.0, confidenceScale 1.0)}`. Only the **directions** are fixed (every evidence term
non-negative — more never lowers the evidence; the break-even tie-direction is the home key, via strict `>`; a
more-confident home key demands a stronger cadence to overturn). No threshold/weight/margin tuned for accuracy.

## §5 — Tests (oracle-asserted) — +6 (composing 936 → 942) + the updated lock-in

`tests/functionmodulation_tests.cpp` (6), each asserted vs the §5.3/§5.4/§8 spec:
- **a tonicization stays home** — a cadence-less away lean: `cadenceConfirmed=false ⇒ isModulation=false`, and the
  recompute does not fire or close the key decision;
- **cadence-confirmed + persistent modulates + recompute re-reads** — `isModulation=true`; the recompute fires (cadence
  strength 2.0 > bar 1.5 at home-confidence 0.5), re-reads `[3..7]` once each in forward order in the new key, and closes
  the key decision;
- **the break-even defaults to tonicization** — evidence == cost exactly ⇒ tonicization (strict `>`); just above the bar
  ⇒ modulation;
- **the relative pair is decided by the tonic-vote** — C major / A minor both sustained equally, only A minor receives a
  cadence ⇒ A minor modulates, C major tonicizes;
- **the §8 closure holds on the recompute** — no re-open (a second override on the closed key id is refused; exactly one
  decision closed) and no recursion (a nested recompute's override evaluates but its forward sweep is **refused (−1)**
  during the active sweep);
- **the convenience path REUSES `detectLocalModulations`** — a raw key-agnostic region stream yields two committed spans
  (the detector was actually invoked); the home span stays, the away cadence-confirmed span modulates.

`regionanalysis_tests OverrideReadiness_…` (the pinned-reduction **lock-in**, updated): a confident region carries a
non-empty ranked `keyAlternatives` of **distinct** keys, each other than the chosen — the region-level menu property.

(All green on the rebuild after the reduction + closure-test fix.)

## §6 — Gate — PASS (dormant + byte-identical)

| Gate | Result |
|---|---|
| Build | clean (all targets link, 0 `error C####`) |
| `composing_tests` | **942/942** (936 + 6; 2 disabled pre-existing) |
| `notation_tests` | **53** passed (4 skipped — baseline) |
| `pipeline_snapshot_tests` | **11/11** PASSED, **NO golden refresh** (1 skipped, 3 disabled — baseline) |
| Corpus **Baroque 53 / Jazz 24 / Default 53** | **unchanged** — full regen of all three presets, `characterise_bir_false` reports 53/24/53, and **`git status tools/corpus/` is clean** after the overwrite (byte-identical `.ours.json`) |

**The two-pin byte-identity proof (the §6 risk):**
1. **No production consumer of the carry.** `grep` of `src/` finds `HarmonicRegion::keyAlternatives` read only by (a) the
   lock-in **test** and (b) `inheritRegionKeyContext`'s parent→child **copy** (pure plumbing — no terminal output sink).
   The notation `context.keyConfidence` reads `keyModeResult.normalizedConfidence` (a different field/source), unaffected.
   So pin #1 changing the carry content cannot move any serialized/scored output.
2. **`jointKeyWiringEnabled()` is default-OFF** (`g_jkdWiringEnabled` seeds from `MUSE_JOINT_KEY_WIRING`, unset in the
   build/test/corpus environment), so `applyJointKeyWiring` (pin #2's site) is not called in production.
3. **`chosen` + `confidence` are bit-identical** — pin #1 keeps the chosen-only `votes` → `best` selection, and returns
   `rep.chosen` / `rep.confidence` unchanged; only `keyAlternatives` changes.
4. **Empirical confirmation** — the full overwrite-and-regen of all three corpora left `tools/corpus/` git-clean and the
   BIR sets at 53/24/53. The live-path pin is inert on production.

## §7 — Stops — none triggered

No pin moved production output (53/24/53 byte-identical); every reuse target was consumable (the arbiter **reuses**
`detectLocalModulations`/`functioncadence`/`forwardoverride`, not a re-implementation); the recompute is forward-only
(re-entrancy-guarded, no back-edge); no threshold/weight tuned (firewall); `upstream` untouched.

## §7b — Build-detail decisions (declared for ratification, not assumed)

1. **The §5.3 hysteresis is layered in the arbiter over the detector's committed candidate spans**, leaving the
   detector's `kEstablishmentMinChords` floor intact as the candidate floor (not re-tuned — modifying it would move the
   detector's own diagnostic/test). The §5.3 persistence is the arbiter's duration + cadential-weight change-cost. This
   is the "adapt the sustained-run gate to the hysteresis form **by reuse**" reading.
2. **§5.4's §8 contradiction strength is the accumulated cadential weight** (cadence-strength vs key-confidence, per the
   §5.4 text), *not* the full persistence evidence; §5.3 owns the duration/persistence call, §5.4 the confidence-scaled
   decisiveness — two distinct gates on distinct evidence, both firewall-default.
3. **The pinned reduction (pin #1) aggregates each slice's chosen key AND its ranked alternatives** into the region-level
   menu (excluding the chosen) — the candidate keys a later cadence could select — not the chosen-only buckets (which
   would be empty for a stable region). Kept apart from the `best`-selecting `votes` so `chosen`/`confidence` stay
   bit-identical.
4. **Pin #2's re-derived `keyConfidence` uses the joint emission confidence** (the J-key-iii path has no L3
   sequence-margin), on the same `[0,1]` override-bar scale. Byte-identical (gated off + no consumer).
5. **The arbiter is producer-agnostic / hand-injectable** (the resolver precedent): it consumes `LocalKeySpan` /
   `FunctionalCadence` / `OnePassClosure` value types, no score/region/decoder engine type — so it compiles free of those
   headers and is exercised by hand-built inputs. The engage step binds `reread` to the J-key-iii re-key path.

## Commits (local, unpushed)
- `4f63d2ab40` — `docs(cowork): Phase-5c Step-3 ratification + Step-4 prep` (the §0 sweep).
- `0e2d3f9319` — `feat(function): L5 tonicization-vs-modulation + the modulation recompute + the two §15-3 pins (Phase 5c Step 4, dormant)`.
- `b3268ad48e` — `docs(status): record session 12 — L5 Phase 5c Step 4 (...)`.

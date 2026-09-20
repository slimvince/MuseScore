# Phase 5c — Step 0 (Layer 5 / FUNCTION): investigate & confirm (read-only)

> **Discipline:** Step 0 of `cowork_phase5c_l5_build_plan.md` — a read-only confirm of the L5 input
> contracts and reuse targets at source, **STOP & report** before any build. Nothing built; no file
> changed except this gitignored dossier. HEAD `334d758d04` (session 9, phrase-boundary primitive).
> Spec: `cowork_layer5_function_design.md` (SIGNED, user 2026-06-26).

## 0. Verdict — GREEN (proceed to Step 1 on ratification)

Every L5 input contract and named reuse target is **consumable at source, as the spec assumes**. No
input is missing; no structural change beyond the dormant layer is needed to build Steps 1–6. The one
input that is a *placeholder* (the L3 key-alternatives carry) is the **v1 representative-slice reduction
the spec already schedules for replacement** as the first task of Step 4 (§15-3) — it does not block
Steps 1–3. Six items are **declared to Cowork** below (§6): two are reuse-landscape surprises Step 0
exists to catch (an unnamed dormant modulation primitive; an unruled ambiguity kind); the rest are
build-scope clarifications, not blockers.

Per the plan, I **STOP here** and do not begin Step 1.

## 1. Inputs — the §3 "Consumes" contract (each confirmed at source)

| Spec input (§3) | As-built source | Status |
|---|---|---|
| **L4→L5 abstain contract** — committed chord, carried readings, named open question, ambiguity kind, confidence components | `chord/chordslicedecoder.h`: `SliceChord` (`chosen`, `alternatives`, `confidence`, `uncertain`, `decision`, `confidenceModel`, `openQuestion`) :380; `OpenQuestionLabel` (`question`, `ambiguity`, `readingA`/`readingB`/`hasReadingB`) :370; `AmbiguityKind` :339; `SliceConfidence` (`margin`/`sufficiency`/`membershipCleanliness`/`composite`) :357 | ✅ Consumable. **Dormant** — `ChordSliceDecoder::decode` is called only by the `--decode-chords` diagnostic (no production/`src` call site). |
| **L3 local key + ranked alternatives + uncertainty** (the override-readiness forward-carry) | `region/harmonicrhythm.h`: `HarmonicRegion::keyAlternatives` + `keyConfidence` :105-106, filled at `regionanalyzer.cpp localKeyForRegion` | ✅ Consumable, **with the documented v1 caveat** (see §6-F3). Comment :101-104 states it has "NO consumer — it exists for Layer 5" and that the v1 reduction is "pinned precisely as the first L5-modulation task (§15-3)". |
| **Layer-1 spelling / bass / voice** (+ shared Layer-1.5 spelling view) | `engravingbridge/spellingview.{h,cpp}` (`lineOfFifths`), already consumed by L4's G4/C1 spelling-pin; `FocalNote::tpc/voice/onset/release` in `chordslicedecoder.h` :416 | ✅ Consumable. Already a live L4 input. |
| **Metric weight of a slice** (§3 prerequisite; §15-0 marked RESOLVED) | `scoreharvest/metricweights.{h,cpp}`; consumed by `regionanalyzer`, `chordslicedecoder` (L4), `keyresolver` | ✅ Confirmed owned + already consumed (matches §15-0 "RESOLVED — no code"). |
| **Phrase boundary + segmentation** (§3 prerequisite; §15-0 marked BUILT-dormant) | `engravingbridge/phraseboundaryview.h`: `phraseBoundaryTicks(score)` :175 (consumer API) + `computePhraseBoundaryProfile` → `PhraseBoundaryProfile{perVoice, textureTicks, textureStrength, pickedTicks}` :132 | ✅ Consumable. Notation-only, **byte-identical on production** (all "ends-a-phrase" consumers dormant/gated per header :62-70). |
| **Top voice** (demoted to optional cue, §5.2 / §15-0) | not a build gate | n/a — optional; not required to build §5.2 (inversion-criterion is the test). |

## 2. Reuse-vs-build map — the named reuse machinery (§13, build-plan Step 0)

| Reuse target (spec) | As-built source | Reuse / build | Plugs into |
|---|---|---|---|
| **Base RN derivation** | `chord/chordanalyzer.h formatRomanNumeral()` :721 (diatonic + chromatic numerals + inline `V/x`,`vii°/x`) + `region::diatonicDegreeForRootPc()` `region/sparsechordrefinement.h:42` | **REUSE** | §5.1 / Step 1 |
| **Aug-6 + chromatic + applied emission** | `chord/chordsymbolformatter.cpp` aug6-nationality block (It/Fr/Ger) :867+, chromatic numeral (incl. `bII`,`bVII`) :448/:832 | **REUSE** (Neapolitan/precedence built on top — §6-F4) | §5.6 / Step 5 |
| **Dormant tonicization labeler** (chromatic-LT guard worth keeping) | `function/tonicizationlabeler.h labelTonicizations()` :153 → `TonicizationLabel` (`<numeral>/<degree>`) | **REUSE + unify** (with the inline formatter path) | §5.6 / Step 5; unify is Phase-5d landing (§15-5) |
| **Key-agnostic cadence frame + salience** (`endsPhrase`, `chromaticLeadingTone`, salience-weighted vote) | `section/cadencekeyanchor.h`: `CadenceRegionInput::endsPhrase` :81; `AuthenticCadence` markers :93-106; `aggregateGlobalAnchor()` salience-weighted vote :155 | **REUSE the frame; BUILD the typology** (authentic-only today — §6-F5) | §5.2 / Step 2 |
| **Proto-functional progression heuristics** | `function/harmonicfunctionlayer.h`: `wSeqBonus` (desc-5th) :133, `wDimBonus` (LT a semitone below next) :139, `resolutionEdgeBonus` (dim→/halfdim→/aug→ targets) :163, `rootContinuityBonus` :127, Gate R :270/:298 | **REUSE** as the §5.0 *licensed-progression* motion tests (note: today they are vertical scoring **bonuses**; §5.0 reuses the same root-motion arithmetic as a *licensing* test, not a score term) | §5.0 / Step 1 |
| **Gate E / Gate J** (Baroque-only post-scoring heuristics) | post-scoring gates, `chord/chordanalyzer.cpp` (preset-gated `preferMinorOverMajorAdd6`) | **CONSULT** (proto-functional priors) | §5.5 / Step 3 |

## 3. The misnamed predecessor + placement (§D6, §13)

- **Confirmed misnamed.** `function/harmonicfunctionlayer.{h,cpp}` (`mu::composing::function`) is the
  **chord-identity competition pipeline** — `applyHarmonicFunction()` is the single winner-selection
  pipeline (rcb / wSeq / wDim / step bonuses / Gate R). Its own header :52-53 states *"E4 (planned):
  cadence detection and functional labeling layer on top of the already-final winner"* — i.e. **L5 is
  that planned, never-built stage.** This is the §13 "layer named for function performs chord-identity
  competition" exactly.
- **Placement (report-only; not now).** The function machinery is **scattered**: competition pipeline +
  tonicization labeler in `analysis/function/`; cadence/anchor/modulation primitives in
  `analysis/section/`; RN/aug6 emission in `analysis/chord/`. The new dormant L5 most naturally lands in
  `analysis/function/` beside `tonicizationlabeler`. The **rename of `harmonicfunctionlayer` + the
  function/ directory consolidation is a Phase-5d structural step** (§15-5), not part of 5c.

## 4. Dormancy / byte-identical guarantee (the firewall holds)

Every reuse-target detector is dormant or gated on the production (`src`) path, so building L5 to consume
them stays byte-identical by construction:
- `ChordSliceDecoder::decode` (L4) — no `src` call site (diagnostic-only).
- `labelTonicizations` — called only by its def + tests in `src` (diagnostic `batch_analyze` in `tools/`).
- `detectAuthenticCadences` / `aggregateGlobalAnchor` — consumed only by `localmodulationdetector` +
  `jointkeydecision`, both on the joint-key path gated by `jointKeyWiringEnabled()` (default **OFF**).
- `phraseBoundaryTicks` — every consumer dormant/gated (header :62-70).

## 5. The detector to retire (Phase 5d, not now)

`section/sectioncadencedetection.cpp detectCadences()` :55 — the **production, key-DEPENDENT, circular**
detector the spec §5.2/§D2 calls out: it gates on `hasAssertiveKeyConfidence()` :74 (silent at floor
near-ties) and reads the **resolved** `keyModeResult` :83-86 (PAC/PC/DC from a key it was supposed to
help decide). It is driven directly by the notation bridge (header :28). The new §5.2 detector is built
**dormant first**; retiring this one is a **Phase-5d engage step**.

## 6. ★ Declared to Cowork (surfaced, not acted on)

- **F1 — `AmbiguityKind::SymmetricRotation` has no §5.5 resolution rule.** L4 emits **6** ambiguity kinds
  (`chordslicedecoder.h:339`): `InsufficientEvidence, TransitionVsContinuation, SymmetricRotation,
  ShareTone, RelativePair, CloseReading`. §5.5 enumerates resolution rules for **5** (transition,
  share-tone, relative-pair, close, insufficient) and asserts "the kinds … are *exactly* the ambiguity
  kinds Layer 4 carries forward; this layer adds no new kind." **Mismatch:** L4 *can* hand L5 a
  `SymmetricRotation` abstain (when the G4/C1 spelling-pin can't resolve a dim7/aug rotation — spelling
  absent/contradicted), and §5.5 names no rule for it. The gate policy already classes symmetric-rotation
  as **class-(a)** (pitch-class-undecidable, coin-flip), so the architecturally-consistent behaviour is to
  **carry it as an honest open mark (§7)** — but the spec's §5.5 rule list should say so explicitly (is it
  "carry honest", or does Cowork intend it folded elsewhere?). *Declared, not assumed.*

- **F2 — an unnamed dormant primitive already implements the §5.3/§5.4 signal.**
  `section/localmodulationdetector.{h,cpp}` (Stage 4d-i) commits a local-key span only when it is
  **ESTABLISHED** (sustained run consistent with the candidate collection) **AND CONFIRMED** (a V→I
  authentic cadence to its tonic inside the span) — *verbatim* the §5.3 cadence-confirmation-gate +
  persistence mechanism, built **key-agnostically** on `detectAuthenticCadences`, dormant
  (`--dump-modulation`; re-key is 4d-ii, gated). It is **not in the Step-0 reuse list**, yet Steps 3–4
  should reuse/unify it (with `jointkeydecision`, the §15-3 J-key-iii re-key path) rather than
  re-implement. Surfaced so the §5.3/§5.4 build map can name it.

- **F3 — the L3 carry is the v1 representative-slice placeholder, and is empty on the live path today.**
  `keyAlternatives`/`keyConfidence` carry only the representative slice's alternatives, and are
  `empty/0.0` until the L3 decode runs on the live `analyzeRegions` key path. Both facts are already
  documented (§15-3 schedules the precise-reduction replacement + the J-key-iii re-derivation as the
  **first tasks of Step 4**). No action for Steps 1–3; flagged so Step 4 honours both pins.

- **F4 — relational-label completeness is build-on-top, not pure reuse.** `formatRomanNumeral` emits the
  diatonic numeral, chromatic numerals (incl. a bare `bII`), the **aug-6 nationality** labels, and inline
  applied labels — but the §5.6 **Neapolitan `bII6` first-inversion convention**, the fixed **precedence**
  (aug6 → Neapolitan → applied → mixture), and **modal-mixture as residual** are L5 build wrapping that
  emission. (Consistent with §13 "unifies, corrects, completes".)

- **F5 — the cadence typology is mostly build.** `cadencekeyanchor` detects **authentic only**
  (descending-5th dominant→tonic). §5.2's PAC/IAC-by-inversion, half (incl. Phrygian), deceptive, plagal,
  evaded, and the **cadential-six-four collapse** are **BUILD**, reusing the key-agnostic frame +
  `endsPhrase` + `chromaticLeadingTone` + the salience-weighted vote + the phrase-gate from
  `phraseboundaryview`. (Matches the plan's Step-2 wording; flagged for scope clarity.)

- **F6 — doc cosmetic (working-tree diff).** The uncommitted edit to `cowork_layer5_function_design.md`
  §15-0 left a **duplicated** "be defined generally (the tool analyzes any instrumentation): the fermata
  is only the *chorale-specific* marker, so" sentence (lines ~558–560). Cowork's doc — flagged, not
  touched.

## 7. Conclusion

Step 0 is **GREEN**. The L1→L4 spine, the L3 forward-carry, the phrase-boundary primitive, the metric
weight, and the named reuse machinery are all consumable at source and dormant on production, so L5 can
be built dormant + byte-identical as the plan requires. **Awaiting Cowork ratification of the F1–F2
declarations before Step 1** (F1 affects §5.5's rule set; F2 affects the Step-3/4 reuse map) — the rest
are scope notes that don't block.

# CC — Architectural Layer 3 (KEY/MODE) WIRING DESIGN dossier (Step 1, BASELINE scorer)

**Status:** READ-ONLY WIRING DESIGN. **No production code changed; no behavior change; no corpus regenerated; no
commit.** Output is this dossier only. **HELD / gitignored** (`/cc_*.md`, `.gitignore:118`). Cowork verifies the
citations + the slice→region mapping + the unification end-state at source; user ratifies; **THEN** §2 wiring code is
written. **STOP after this dossier (instruction §1).**

**Scope (instruction):** Step 1 only — replace the per-region key resolver with the decoder at the region-analyzer
seam, **baseline scorer (NO `scaleMembership` reweight — that is Step 2)**, retire the old path, clear the production
gates. The §3-SPEC reweight (`cc_layer3_sweep_report.md`) is **explicitly NOT in this increment** (instruction §6
stop condition).

**Builds on (does not redo), re-confirmed at HEAD `2203ad9fda` this session:**
- `cc_layer3_decoder_audit_dossier.md` — the pre-build audit (the seam @633, the emission, the cost pins). Cited
  **[audit §X]**.
- `cc_layer3_decoder_build_report.md` — the decoder as committed (`c453315faa`), its public API, §4a reuse-ledger,
  §9 unification follow-ups. Cited **[build §X]**.
- `cc_layer3_sweep_report.md` — the bounded sweep + §3-SPEC (Step 2 reweight). Cited **[sweep §X]**.

**No-assume rule:** every as-is statement cites `file:line` read **this session**. Items not confirmable at source
are tagged `[unverified]` in §8 — never guessed. **Three findings below were NOT in the prior seam audit and are
flagged ★NEW** (the P4 second key path, the confidence-field gap, the excludeStaves/partial-signature gaps); they are
the reason this design step exists.

---

## §0 — Headline findings (decision-relevant)

1. **The region-path seam is confirmed at HEAD** — initial seed `resolveKeyAndModeRanked` @
   [`regionanalyzer.cpp:521-524`](src/composing/analysis/region/regionanalyzer.cpp#L521-L524) + Pass-1 per-region @
   [`633-638`](src/composing/analysis/region/regionanalyzer.cpp#L633-L638); carrier =
   `HarmonicRegion::keyModeResult` @ [`740`](src/composing/analysis/region/regionanalyzer.cpp#L740) /
   [`723`](src/composing/analysis/region/regionanalyzer.cpp#L723). Pass-2/2b **inherit** the parent's key (no
   re-resolution) @ [`785-786`](src/composing/analysis/region/regionanalyzer.cpp#L785-L786) /
   [`994-995`](src/composing/analysis/region/regionanalyzer.cpp#L994-L995). Joint @
   [`393-396`](src/composing/analysis/region/regionanalyzer.cpp#L393-L396) is gated OFF @
   [`1166`](src/composing/analysis/region/regionanalyzer.cpp#L1166). **[audit §1.1] confirmed.**
2. **★NEW — there is a SECOND live production key path the prior seam audit did not enumerate:** the **P4 tick-local**
   path `analyzeHarmonicContextLocallyAtTick` @
   [`notationcomposingbridge.cpp:578-596`](src/notation/internal/notationcomposingbridge.cpp#L578-L596) calls the
   bridge wrapper `resolveKeyAndMode` @ [`595`](src/notation/internal/notationcomposingbridge.cpp#L595), which calls
   `kr::resolveKeyAndModeRanked` @
   [`notationcomposingbridgehelpers.cpp:186`](src/notation/internal/notationcomposingbridgehelpers.cpp#L186). It is a
   **single-tick** resolve, exercised in production (P4 fallback @
   [`688`](src/notation/internal/notationcomposingbridge.cpp#L688) /
   [`724`](src/notation/internal/notationcomposingbridge.cpp#L724)) and **pinned by `pipeline_snapshot_tests` P4** @
   [`pipeline_snapshot_tests.cpp:521`](src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp#L521).
   **Consequence:** "one key path, one builder" (instruction §1/§4) cannot be claimed by wiring only the region path —
   the P4 consumer must be addressed or its residual surfaced. This is the largest scoping decision (§2.3 + §6).
3. **The decoder is callable as-is but has THREE production-fidelity gaps that wiring MUST close** (all source-true):
   (a) **`excludeStaves` is hardcoded empty** in `buildSliceContext` @
   [`keymodesequence.cpp:88-89`](src/composing/analysis/key/keymodesequence.cpp#L88-L89) and `decode()` has **no
   excludeStaves parameter** ([`keymodesequence.h:176-182`](src/composing/analysis/key/keymodesequence.h#L176-L182)) —
   production excludes staves; (b) **no `partialSignatureCorrection`** (the Baroque Dorian-signature fix the resolver
   applies @ [`keyresolver.cpp:260-263`](src/composing/analysis/key/keyresolver.cpp#L260-L263) is **absent** from
   `keymodesequence.cpp` — grep confirms); (c) **the chosen result's `normalizedConfidence` is 0.0** (`stateToResult`
   @ [`keymodesequence.cpp:100`](src/composing/analysis/key/keymodesequence.cpp#L100)) while downstream gates on
   `keyModeResult.normalizedConfidence ≥ 0.8` (§2.5). Each is specified below.
4. **The slice→region mapping is real and non-trivial: the region grid ≠ the L2 slice grid.** The region analyzer
   builds its own boundaries (greedy-expand @
   [`551-554`](src/composing/analysis/region/regionanalyzer.cpp#L551-L554) + onset/bass sub-boundaries Pass-2/2b);
   the decoder consumes `changePointSlices(noteModel)` ([`slicer.h:91`](src/composing/analysis/slicing/slicer.h#L91)),
   which is **not currently called in `regionanalyzer.cpp`** (grep: only `batch_analyze` diagnostics + tests call it).
   Wiring must (i) add the `changePointSlices` call, (ii) run `decode()` once, (iii) map per-slice → per-region,
   (iv) decide the intra-region-disagreement rule. §2.1 specifies; the rule needs ratification.
5. **`collectPitchContext` has exactly one production-library caller, transitively** — `resolveKeyAndModeRanked` @
   [`keyresolver.cpp:300`](src/composing/analysis/key/keyresolver.cpp#L300). So retiring the resolver **from the
   production path** retires `collectPitchContext` **from the production path** — but the resolver also remains the
   **grading baseline** the decoder is measured against ([build §6]) and the tool/diagnostic baseline, so the
   *function* is not deleted. The honest end-state is **one key path + one builder on the production analysis path**,
   with the resolver + `collectPitchContext` surviving **only** for diagnostics/grading (§4 ledger). This is the
   §6-flagged residual, surfaced not hidden.
6. **Predicted production move (from [build §6], not re-measured here):** Baroque unambiguous full-match **−3.0**
   (dur-wt −1.7), Jazz **+17.0**; modulation top-1 **+21.3 Baroque / +11.9 Jazz**. Production key output **will**
   change ⇒ BIR / snapshots / S2 will move; all are HARD-gated in §3. Direction: Baroque stable slightly worse, Jazz +
   modulation much better.

---

## §1 — The seam, re-confirmed at HEAD (what the decoder must reproduce)

### §1.1 — The region-path key decision (the seam)
`analyzeRegions` ([`regionanalyzer.cpp:483-1181`](src/composing/analysis/region/regionanalyzer.cpp#L483-L1181)):

| site | line | role | feeds |
|---|---|---|---|
| **Initial seed** | [`521-524`](src/composing/analysis/region/regionanalyzer.cpp#L521-L524) | `resolveKeyAndModeRanked(…, nullptr)` → `keyFifths`/`keyMode` | greedy-expand segmentation @ [`554`](src/composing/analysis/region/regionanalyzer.cpp#L554) **and** the chord-path decoder seed `findTemporalContext` @ [`600`](src/composing/analysis/region/regionanalyzer.cpp#L600) |
| **Pass-1 per-region** (THE seam) | [`633-638`](src/composing/analysis/region/regionanalyzer.cpp#L633-L638) | `resolveKeyAndModeRanked(…, &prevKeyResult)` → `localKey`/`localKeyFifths`/`localKeyMode` | `analyzeChord` @ [`668-669`](src/composing/analysis/region/regionanalyzer.cpp#L668-L669); `inferNextRootPc` @ [`653-654`](src/composing/analysis/region/regionanalyzer.cpp#L653-L654); `refineSparseChordQualityFromKeyContext` @ [`684-685`](src/composing/analysis/region/regionanalyzer.cpp#L684-L685); `applyTonicPriorToSparseChord` @ [`686-687`](src/composing/analysis/region/regionanalyzer.cpp#L686-L687); output `keyModeResult` @ [`723`](src/composing/analysis/region/regionanalyzer.cpp#L723)/[`740`](src/composing/analysis/region/regionanalyzer.cpp#L740) |
| Pass-2 inherit | [`785-786`](src/composing/analysis/region/regionanalyzer.cpp#L785-L786) | `subKeyFifths/subKeyMode = parentRegion.keyModeResult.{…}` | sub-region `analyzeChord` @ [`884-885`](src/composing/analysis/region/regionanalyzer.cpp#L884-L885); sub `keyModeResult` inherited @ [`943`](src/composing/analysis/region/regionanalyzer.cpp#L943) |
| Pass-2b inherit | [`994-995`](src/composing/analysis/region/regionanalyzer.cpp#L994-L995) | same (parent key) | sub `analyzeChord` @ [`1080-1081`](src/composing/analysis/region/regionanalyzer.cpp#L1080-L1081); inherited `keyModeResult` @ [`1134`](src/composing/analysis/region/regionanalyzer.cpp#L1134) |
| Joint (dormant) | [`393-396`](src/composing/analysis/region/regionanalyzer.cpp#L393-L396) | re-resolve per FINAL region inside `applyJointKeyWiring` | gated OFF @ [`1166`](src/composing/analysis/region/regionanalyzer.cpp#L1166) |

**Key structural fact for the mapping:** the live key is decided **only at the Pass-1 coarse-region granularity**
(seed @521 + per-coarse-region @633). Pass-2/2b sub-regions **inherit** their parent's key — they never re-resolve.
So the decoder's per-slice output must be reduced to **one key per Pass-1 coarse region**; the sub-region inheritance
chain then propagates it unchanged (the wiring does **not** need to touch Pass-2/2b — they read
`parentRegion.keyModeResult`).

**`prevKeyResult` threading** ([`603`](src/composing/analysis/region/regionanalyzer.cpp#L603),
[`635`](src/composing/analysis/region/regionanalyzer.cpp#L635), [`714`](src/composing/analysis/region/regionanalyzer.cpp#L714))
exists only to drive the resolver's per-region **hysteresis** (`keyresolver.cpp:329-345`). The decoder's change cost
**replaces** hysteresis (the whole-sequence Viterbi is the smoothing), so this threading **retires** with the
resolver.

### §1.2 — ★NEW The second live key path (P4 tick-local)
`analyzeHarmonicContextLocallyAtTick` ([`notationcomposingbridge.cpp:578`](src/notation/internal/notationcomposingbridge.cpp#L578))
fills `NoteHarmonicContext.{keyFifths,keyMode,keyConfidence}` via the bridge `resolveKeyAndMode` @
[`595-596`](src/notation/internal/notationcomposingbridge.cpp#L595-L596) →
[`notationcomposingbridgehelpers.cpp:140-192`](src/notation/internal/notationcomposingbridgehelpers.cpp#L140-L192) →
`resolveKeyAndModeRanked` @ [`186`](src/notation/internal/notationcomposingbridgehelpers.cpp#L186);
`outConfidence = chosen.normalizedConfidence` @ [`192`](src/notation/internal/notationcomposingbridgehelpers.cpp#L192).
It is the **P4 fallback** when the regional P3 path yields nothing (called @
[`688`](src/notation/internal/notationcomposingbridge.cpp#L688) /
[`724`](src/notation/internal/notationcomposingbridge.cpp#L724)) and is **snapshot-pinned** (P4) @
[`pipeline_snapshot_tests.cpp:521`](src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp#L521).
**It resolves at a single tick, not a slice sequence** — so the sequence decoder does not drop in trivially. This is
the §2.3 scoping decision.

### §1.3 — The full resolver-call census (the retirement surface)
`resolveKeyAndModeRanked` callers (grep, this session):

| caller | site | class | this increment |
|---|---|---|---|
| `analyzeRegions` initial seed | [`regionanalyzer.cpp:521`](src/composing/analysis/region/regionanalyzer.cpp#L521) | **production (region)** | **replace** (decoder seed) — §2.2 |
| `analyzeRegions` Pass-1 per-region | [`regionanalyzer.cpp:633`](src/composing/analysis/region/regionanalyzer.cpp#L633) | **production (region) — THE seam** | **replace** (decoder lookup) — §2.1 |
| `applyJointKeyWiring` | [`regionanalyzer.cpp:393`](src/composing/analysis/region/regionanalyzer.cpp#L393) | dormant (flag OFF) | leave dormant — §2.4 |
| bridge `resolveKeyAndMode` (P4) | [`notationcomposingbridgehelpers.cpp:186`](src/notation/internal/notationcomposingbridgehelpers.cpp#L186) | **production (P4 tick-local)** | **decide** (§2.3 — surface) |
| batch `inferLocalKey` (→ used @2576) | [`batch_analyze.cpp:490`](tools/batch_analyze.cpp#L490) | **tool** | unchanged (tool baseline) |
| batch `analyzeScore` joint-dump builder | [`batch_analyze.cpp:675`](tools/batch_analyze.cpp#L675) | **tool / diagnostic** | unchanged |
| batch `writeKeyCandidateDump` (`--dump-key-resolve`) | [`batch_analyze.cpp:854`](tools/batch_analyze.cpp#L854) | **tool / diagnostic** | unchanged (the grading baseline) |
| `regionanalysis_tests` | regionanalysis_tests.cpp | test | unchanged |

**Reading:** the **production** library has exactly **two** key paths — the region path (replace) and the P4
tick-local path (decide). The resolver remains as the **diagnostic/grading baseline** (`--dump-key-resolve` is the
exact thing the held-out harness compares the decoder against — [build §6]), so the *function* is not deleted; its
**production use** is what retires.

---

## §2 — The wiring design (specified, NOT coded)

### §2.1 — The slice→region mapping (the central question)
**Data flow (recommended):**
1. `noteModel` already built once @ [`508`](src/composing/analysis/region/regionanalyzer.cpp#L508).
2. **Add** `slices = changePointSlices(noteModel)` (Layer-2 grid) — new call in `analyzeRegions`
   ([`slicer.h:91`](src/composing/analysis/slicing/slicer.h#L91)).
3. **Run `KeyModeSequenceDecoder::decode(slices, noteModel, correctedFifths, declaredMode, keyPrefs, seqPrefs)` ONCE**,
   up front (before the Pass-1 loop) → `std::vector<SliceKeyMode>` (one per slice, whole [domain]).
4. Build a **tick→slice index** (slices are ordered, covering, non-overlapping —
   [`slicer.h:55-60`](src/composing/analysis/slicing/slicer.h#L55-L60)) so a region's `[startTick,endTick)` maps to
   its overlapping slice run in O(log N).
5. **Per Pass-1 coarse region**, derive `localKey` from the decoder's slice run over `[regionStart,regionEnd)`
   (the intra-region rule below), and feed it where `localKey` is read today (§1.1 consumers @668/653/684/686/740).
6. Pass-2/2b inheritance is **untouched** — sub-regions read `parentRegion.keyModeResult` (§1.1), so the decoder key
   propagates with no extra wiring.

**Intra-region disagreement rule (NEEDS RATIFICATION).** A Pass-1 coarse region can span slices the decoder assigns
different keys (a modulation inside one coarse region — exactly the case the decoder exists to catch, [audit §0]).
Three candidate rules:

| rule | behavior | pro | con |
|---|---|---|---|
| **(a) start-slice** | take the decoder key of the slice covering `regionStart` | simplest; matches the resolver's tick-anchored read @633 (resolver resolves AT `regionStart`) | ignores a within-region modulation the decoder found |
| **(b) duration-majority** ★recommended | take the decoder key holding the most ticks within `[regionStart,regionEnd)` | most representative single key for a region; robust to a 1-slice transient at the region edge | a true mid-region modulation is still collapsed to one key |
| **(c) re-split** | split the coarse region at the decoder's key boundary so each part gets its own key | fully exposes the decoder's modulation tracking | **changes the region GRID** (a much larger move: new boundaries → different chord segmentation, large snapshot churn) — not "baseline/conservative first wiring" |

**Recommendation:** **(b) duration-majority** for this baseline increment. It is the conservative single-key reduction
that (i) keeps the region grid byte-stable (no re-split), isolating "decoder replaces resolver" as the single change
(instruction §2), and (ii) is strictly better than (a) when the region's dominant key differs from its first slice.
**Re-split (c) is explicitly deferred** to a later increment (it is the mechanism that surfaces within-coarse-region
modulation, but it changes segmentation — out of scope for a conservative first wiring). **This choice is a STOP/
ratify item** (§6) — if Cowork/user prefer (a) or (c), the dossier is amended before §2 code.

**Note on granularity vs the design thesis.** The decoder's modulation win ([build §6] +21.3/+11.9) is measured at
**slice** granularity; reducing to one key per **coarse region** with rule (b) **caps** how much of that win reaches
production this increment (a within-region modulation is averaged out). That is an accepted, surfaced limitation of the
baseline wiring — the within-region exposure is rule (c), deferred. The cross-region modulation tracking **does** reach
production (each coarse region gets its own duration-majority decoder key, sequence-consistent).

### §2.2 — The initial seed (@521) — two options, surfaced
The seed `keyFifths`/`keyMode` feeds **segmentation** (greedy-expand @554) **and** the chord-path decoder seed (@600).

- **Option S1 (full unification) ★recommended-with-caveat:** seed from the decoder's **first in-range slice** key
  (`decode()` output @ the slice covering `startTick`). Fully retires `resolveKeyAndModeRanked` from the region path.
  **Caveat:** `greedyExpandSegmentation` consumes `keyFifths`/`keyMode` (@554), so a changed seed **can shift the
  coarse boundary grid** → different regions → cascade into BIR/snapshots. This must be **measured** (it may be inert
  if greedy-expand is insensitive to the seed for the affected stems; `[unverified]` — not measured in a read-only
  step).
- **Option S2 (minimal, segmentation-stable):** keep `resolveKeyAndModeRanked` at @521 **only** for the seed (grid
  byte-identical), replace only @633. **Cost:** the resolver + `collectPitchContext` are **not** fully retired from
  production (the seam goal "one key path" is partially unmet — the seed is still resolver-sourced). Surfaced as the
  residual.

**Recommendation:** attempt **S1**; if the segmentation shift causes a BIR regression that S1 cannot clear, fall back
to **S2** and surface the residual (the seed is a single tick-0-ish read; its production weight is far smaller than the
per-region key). The decision is gated by the §3 measurement, not pre-committed here.

### §2.3 — ★NEW The P4 tick-local path — the scoping decision (SURFACE)
The P4 path (§1.2) is a single-tick key resolve. Options:

| option | what | pro | con |
|---|---|---|---|
| **P4-defer** ★recommended | leave P4 on `resolveKeyAndModeRanked` this increment; wire only the region path; **surface** that `collectPitchContext` therefore stays alive for P4 (residual, §4) | smallest attributable change; P4 is a fallback, not the primary display path | "one key path" not fully achieved this increment (explicitly surfaced) |
| **P4-redecode** | run the whole-score `decode()` once and have P4 index the chosen key at its tick | unifies the key path | `decode()` per P4 call is whole-score cost; P4 is the per-note fallback (perf risk); needs a decode cache; larger change |
| **P4-repoint** | keep P4's single-tick resolve but re-point its PitchContext builder onto `pitchContextOverSpan` | retires `collectPitchContext` while keeping the single-tick resolver | changes the resolver's note set (onset-in-window → overlap-in-window, [build §9.1]) = a P4 production change; still two key *algorithms* |

**Recommendation: P4-defer.** This increment is "the decoder replaces the **per-region** resolver" (instruction §2);
folding the single-tick P4 path into a sequence decoder is a distinct architectural step (a cached whole-score decode
the P4 fallback indexes). **The residual is surfaced** per §6 ("`collectPitchContext` cannot be cleanly retired →
surface rather than leave two builders silently"): after this increment, `collectPitchContext` survives **only** as
the P4 + diagnostic/grading builder, **off the region production path**. End-state target "one builder" becomes a
named follow-up (P4 unification), not a silent duplicate.

### §2.4 — The joint-key seam (keep OFF, disentangled)
`jointKeyWiringEnabled()` default OFF (env-gated, `g_jkdWiringEnabled` @
[`jointkeydecision.cpp:137-140`](src/composing/analysis/section/jointkeydecision.cpp#L137-L140); flag check @
[`regionanalyzer.cpp:1166`](src/composing/analysis/region/regionanalyzer.cpp#L1166)). `applyJointKeyWiring` (@352)
runs **after** the merge passes and **re-resolves** per FINAL region via `resolveKeyAndModeRanked` @393 — independent
of the seam. **Design decision: leave it entirely unchanged and OFF.** The decoder replaces @521/@633; @393 stays
dormant. **Do not entangle.** (If ever turned ON, `applyJointKeyWiring` would still call the resolver — that is its
own future reconciliation, out of scope here. Confirmed no shared mutable state with the decoder path.)

### §2.5 — ★NEW The three fidelity gaps wiring MUST close
These are not optional — without them the wired key is wrong vs the as-graded decoder or breaks downstream gates:

1. **`excludeStaves`** — `decode()`/`buildSliceContext` score all staves (empty set hardcoded @
   [`keymodesequence.cpp:88-89`](src/composing/analysis/key/keymodesequence.cpp#L88-L89)); `pitchContextOverSpan`
   **already takes** an `excludeStaves` set ([`regiontonecollector.h:267-273`](src/composing/analysis/engravingbridge/regiontonecollector.h#L267-L273)).
   **Wiring change:** thread `excludeStaves` through `decode()` → `buildLattice` → `buildSliceContext` →
   `pitchContextOverSpan`. (A signature addition to the decoder; the view supports it already.) Without this, the
   production key would include excluded-staff pitches — a divergence from both the resolver and the as-graded decoder
   (the harness graded whole-score with no exclusions; production excludes staves).
2. **`partialSignatureCorrection`** — the resolver corrects the notated fifths one step toward the declared mode for
   the Baroque "one accidental short" convention @
   [`keyresolver.cpp:260-263`](src/composing/analysis/key/keyresolver.cpp#L260-L263) (grep: **absent** from
   `keymodesequence.cpp`). The decoder takes a single `keySigFifths` and anchors both candidate spelling
   (`stateForCandidate` @ [`keymodesequence.cpp:118`](src/composing/analysis/key/keymodesequence.cpp#L118)) and the
   emission's `keySignatureProximity` to it. **Wiring change:** compute `correctedFifths =
   partialSignatureCorrection(...)` once (as the resolver does) and pass it as `decode()`'s `keySigFifths`. This
   preserves the known-load-bearing Baroque behavior (memory `project_key_detection_baroque_partial_signature`); its
   omission would systematically mis-key partial-signature Baroque stems and move BIR/S2. **Surface:** confirm the
   correction is mode-gated (`declaredMode.has_value()` @ [`keyresolver.cpp:260`](src/composing/analysis/key/keyresolver.cpp#L260))
   so it is a no-op where it is today.
3. **`normalizedConfidence`** — `stateToResult` sets it to **0.0** @
   [`keymodesequence.cpp:100`](src/composing/analysis/key/keymodesequence.cpp#L100); the decoder's real confidence is
   the **sequence margin** on `SliceKeyMode.confidence` (unbounded; `kSingleStateConfidence = 1000` @
   [`keymodesequence.cpp:50`](src/composing/analysis/key/keymodesequence.cpp#L50)). Downstream **gates on
   `keyModeResult.normalizedConfidence`**:
   - KeyArea opening ≥ `kAnnotateKeyConfidenceThreshold` (0.8) @
     [`sectionanalyzer.cpp:740-747`](src/composing/analysis/section/sectionanalyzer.cpp#L740-L747);
   - cadence key-stability gate @ [`sectioncadencedetection.cpp:52`](src/composing/analysis/section/sectioncadencedetection.cpp#L52);
   - key-exposure display + merge equality @
     [`notationimplodebridge.cpp:84`](src/notation/internal/notationimplodebridge.cpp#L84) /
     [`307-308`](src/notation/internal/notationimplodebridge.cpp#L307-L308);
   - P3 `keyConfidence` echo @ [`notationcomposingbridge.cpp:280`](src/notation/internal/notationcomposingbridge.cpp#L280).
   If wiring copied `SliceKeyMode.chosen` verbatim, **every region would carry confidence 0.0** → all KeyAreas
   suppressed, all key-confidence-gated cadences suppressed, key-exposure buckets all collapsed → a large, *spurious*
   snapshot move that is an artifact, not the decoder being right. **Wiring change (NEEDS RATIFICATION of the form):**
   populate `keyModeResult.normalizedConfidence` with a **calibrated [0,1]** value. Two source-true options:
   - **C1 ★recommended:** carry the **emission's** `normalizedConfidence` for the chosen state — the same sigmoid the
     resolver produced (`analyzeKeyMode` computes it @
     [`keymodeanalyzer.cpp:771-774`](src/composing/analysis/key/keymodeanalyzer.cpp#L771-L774)); it is on the same
     scale downstream is calibrated for (0.8 threshold). The decoder currently **discards** it (reads only `dump`
     finalScore). Requires the decoder to expose the chosen state's emission `normalizedConfidence` (re-run
     `analyzeKeyMode` top-N for the region's representative slice, or extend `SliceKeyMode`).
   - **C2:** transform the sequence margin → [0,1] via a calibrated map. More faithful to the *decoder's* confidence
     notion but **un-calibrated** against the 0.8 downstream threshold → unpredictable KeyArea/cadence move; rejected
     for a conservative first wiring.
   **Recommendation: C1** (downstream-calibrated, smallest controllable move). The decoder's own
   `SliceKeyMode.uncertain`/sequence-margin remains available for a future confidence-redesign step, not used to gate
   this increment.

### §2.6 — Reach-back (R3) vs the region windowing — no Layer-1 contract change
- `NoteModel::build(score)` builds over the **whole score** @
  [`regionanalyzer.cpp:508`](src/composing/analysis/region/regionanalyzer.cpp#L508); `changePointSlices` tiles the
  **whole** model ([`slicer.h:87-91`](src/composing/analysis/slicing/slicer.h#L87-L91)). The analysis range is
  `[startTick,endTick)`. **For the whole-score case (the corpus/snapshot/batch case), reach-back is free** — the
  earlier slices already exist; `decode()` runs over them and the per-region mapping simply consumes the in-range
  slices ([audit §2.6]). **Wiring does not change the analyzed span** for whole-score analysis, so it stays within
  Layer-1's supply contract (the model is already whole-score).
- **Partial selection** (`startTick > 0`): `decode()` over the whole model already gives earlier-context slices; the
  decoder's first in-range region inherits a sequence-consistent key decided with the earlier slices present. The
  notation-bridge *selection→range rebuild* path is **`[unverified]`** ([audit §6.1]); the composing-side range entry
  is source-confirmed. No change needed for the corpus gates (whole-score).

### §2.7 — Single signature vs per-tick (notated mid-piece key changes)
The resolver reads `keySigEvent(tick)` **per region** ([`keyresolver.cpp:219`](src/composing/analysis/key/keyresolver.cpp#L219));
`decode()` takes a **single** `keySigFifths`/`declaredMode` for the whole decode ([build §4]: read at tick 0). For a
score with a **notated mid-piece key signature change**, the decoder's single-signature anchor differs from the
resolver's per-region read. **Design decision (baseline): accept single-signature** — it matches the decoder exactly
as graded ([build §6]); the change cost lets the decoded key track the new tonal center from the notes even without a
new notated anchor. **Surface** as a known limitation: a per-notated-segment decode (re-anchor `keySigFifths` at each
notated KeySig change) is a clean future refinement, not in scope. (Most of the Baroque/Jazz corpus is single-signature
or zero-signature; the magnitude of affected stems is `[unverified]` and should be reported from the wiring measurement.)

---

## §3 — Predicted production move + the gates (MANDATORY, both presets)

**Why production moves:** the decoder changes the **local key** fed to `analyzeChord` (@668) — and key→chord is the
scoring order — so chord root/quality/inversion can change, plus the `keyModeResult` label + key-relative Roman
numerals + confidence-gated KeyArea/cadence/exposure. From [build §6] (held-out, the directional expectation, **not**
re-measured in this read-only step):

| metric | Baroque | Jazz | where |
|---|---|---|---|
| unambiguous full (tonic+mode) | **−3.0** (dur-wt −1.7) | **+17.0** | stable regions |
| modulation top-1 | **+21.3** | **+11.9** | ambiguous regions |

**The gates (instruction §3 — run at §2, not now):**
1. **BIR case-identity, no regression** — Baroque **57** / Jazz **23** / Default **57**, byte-or-better, via
   `run_bach_preset.py` + `characterise_bir_false.py` per preset (CLAUDE.md). **Any BIR=false increase on ANY preset
   = HARD STOP.** Predicted risk: concentrated where the decoder key differs from the resolver — fifth-displacement
   tonicization regions + relative pairs ([build §6]); the Baroque −3.0 stable move is the most likely BIR pressure.
2. **Both suites pass** — `composing_tests` + `notation_tests` (incl. `pipeline_snapshot_tests`).
3. **Pipeline snapshots (P1–P4)** — keys + key-relative RNs re-spell; the four modulation-heavy goldens (chopin/mozart/
   corelli/schumann) move most, chorales least ([audit §4]); confidence-mapping (§2.5.3) drives KeyArea/cadence
   churn — **C1 is chosen precisely to keep that controllable**. ★ The P4 goldens move **only** if §2.3 chooses
   P4-redecode/repoint; with **P4-defer** the P4 snapshots are **byte-identical** (P4 still uses the resolver). **Do
   NOT silently refresh** — produce the diff, confirm each change is the decoder being *correct*, surface for
   ratification before any `--update-goldens`.
4. **S2 key-inference** — report the move.
5. **Held-out direct metric** — report the wired decoder's production key vs held-out GT per preset; confirm it
   matches the [build §6] diagnostic grading (no wiring-introduced discrepancy — the §2.5 gaps are the prime suspects
   if it diverges, which is exactly why they are mandatory).

**Segmentation-shift watch (§2.2):** if Option S1 changes the coarse grid, BIR/snapshots move from *segmentation*,
not key — measure S1 vs S2 to attribute, prefer the segmentation-stable seed if S1 regresses.

---

## §4 — Unification ledger (instruction §4)

**Reused (no re-implementation):** the committed decoder `keymodesequence.{h,cpp}` (`c453315faa`); its emission
`KeyModeAnalyzer::analyzeKeyMode` + 252-dump; the shared indexed view `pitchContextOverSpan`
([`regiontonecollector.h:267`](src/composing/analysis/engravingbridge/regiontonecollector.h#L267)); `changePointSlices`
(L2); `partialSignatureCorrection` (lifted from the resolver to compute `correctedFifths` once — §2.5.2); the existing
`HarmonicRegion::keyModeResult` carrier; Pass-2/2b inheritance (untouched).

**Newly written (wiring only, §2):** the `analyzeRegions` plumbing — the `changePointSlices` call, the single
`decode()` invocation, the tick→slice index, the per-region duration-majority reduction (§2.1), the confidence
mapping (§2.5.3 C1); an `excludeStaves` parameter added to `decode()`/`buildSliceContext` (§2.5.1); the seed wiring
(§2.2).

**Retires (from the PRODUCTION REGION PATH):** `resolveKeyAndModeRanked` @
[`regionanalyzer.cpp:633`](src/composing/analysis/region/regionanalyzer.cpp#L633) (+ @521 under Option S1) and its
**hysteresis** (`keyresolver.cpp:329-345`) + the `prevKeyResult` threading; `collectPitchContext` as the region
path's builder.

**End-state (honest):** **on the production region path, one key path (the decoder) + one builder
(`pitchContextOverSpan`).** **Two surfaced residuals** (not silent duplicates): (i) the **P4 tick-local** path still
uses `resolveKeyAndModeRanked` + `collectPitchContext` (§2.3 P4-defer) — a named follow-up (P4 unification); (ii) the
resolver + `collectPitchContext` remain compiled as the **diagnostic/grading baseline** (`--dump-key-resolve`, the
held-out harness, `regionanalysis_tests`) — they are the very thing the decoder is graded against, so deleting them is
neither possible nor desirable this increment. **No NEW parallel path or logic duplication is introduced by the
wiring; the remaining duplication is pre-existing (P4) and is surfaced with a named retirement follow-up, per
instruction §6.** (The cleaner phrasing the instruction requests — *"No parallel path or logic duplication was
introduced"* — is **true of the wiring change itself**; the P4 residual is pre-existing and explicitly surfaced rather
than created.)

---

## §5 — The §1 open questions, answered

| instruction §1 question | answer (source) |
|---|---|
| Is @633 + `keyModeResult` still the single production key decision point? | **No — re-confirmed @633 is the single region-path point, but ★NEW the P4 tick-local path (§1.2) is a second live key consumer the prior audit missed.** Carrier `keyModeResult` confirmed (§1.1). |
| Slice→region mapping incl. intra-region disagreement | §2.1 — run `decode()` once; per coarse region use **duration-majority** (rule b); re-split (c) deferred. Pass-2/2b inherit unchanged. **Ratify the rule.** |
| Does the region analyzer already have the L2 slices, or must wiring run the slicer? | **Must run it** — `changePointSlices` is **not** called in `regionanalyzer.cpp` today (grep); wiring adds the call over the existing whole-score `noteModel` (§2.1). |
| Reach-back vs windowing — does wiring change the analyzed span? | **No** for whole-score (model + slices already whole-score @508/`slicer.h`); within Layer-1's supply contract (§2.6). |
| Joint-key seam — does wiring entangle with `jointKeyWiringEnabled`? | **No** — left OFF/unchanged; @393 dormant; no shared mutable state (§2.4). |
| What retires (end-state)? | §4 — region path → decoder + `pitchContextOverSpan`; resolver+`collectPitchContext` survive only for P4 (surfaced) + diagnostics/grading. |
| Predicted production move + per-gate effect | §3 — Baroque stable −3.0 / Jazz +17.0 / modulation +21.3/+11.9; BIR/snapshot/S2 all gated; confidence-mapping + the §2.5 gaps are the move's controllers. |

---

## §6 — Design choices requiring RATIFICATION (the STOP items)

1. **Intra-region reduction rule** — **(b) duration-majority** recommended; (a) start-slice / (c) re-split are the
   alternatives. (Instruction §6: "the slice→region mapping forces a design choice" — here it is, surfaced.)
2. **Initial seed** — **S1 (decoder seed, full retire)** vs **S2 (resolver seed, segmentation-stable)**; recommend
   try-S1-fallback-S2 gated on §3 BIR.
3. **★ P4 tick-local path** — **P4-defer** recommended (surface the `collectPitchContext` residual + name the P4
   unification follow-up) vs P4-redecode / P4-repoint. This is the "one key path" scoping decision and the
   §6-stop-condition residual.
4. **Confidence mapping** — **C1 (carry emission `normalizedConfidence`)** recommended vs C2 (transform sequence
   margin).
5. **Single-signature acceptance** (§2.7) for notated mid-piece key changes — accept for baseline; report affected-
   stem count at §2.

## §7 — `[unverified]` (not confirmable in a read-only step — listed, not guessed)
1. Whether Option S1 (decoder-sourced seed) shifts `greedyExpandSegmentation` boundaries, and on how many stems
   (§2.2) — requires building + measuring.
2. The count of stems with notated mid-piece key-signature changes affected by single-signature decode (§2.7).
3. The notation-bridge **partial-selection** range-rebuild for reach-back (§2.6) — composing-side range confirmed;
   bridge selection→range agent-sourced ([audit §6.1]), not re-read.
4. Whether `decode()` over the whole model + per-region mapping reproduces the [build §6] held-out numbers under
   production `excludeStaves`/`correctedFifths` (the §2.5 gaps) — the held-out re-measure at §2 is the check.

## §8 — Stop-conditions status (instruction §6) — none breached this step
- This is the **read-only design** deliverable; **no wiring code written**, no production/behavior/scoring change, no
  corpus regen, no commit, no snapshot refresh. ✓
- The §3-SPEC `scaleMembership` reweight is **NOT** applied (Step 2). ✓
- Every as-is statement cites `file:line` read this session or is tagged `[unverified]` (§7). ✓
- `collectPitchContext` retirement is **surfaced** (P4 residual + diagnostic baseline), not silently left as two
  builders (§4). ✓
- The slice→region mapping design choice is surfaced for ratification (§6.1), not unilaterally taken. ✓
- `upstream` not involved (no `muse`/#9444 content). ✓

**Next (after Cowork citation-verification + user ratification of §6):** write the §2 wiring code per the ratified
choices, commit **locally (unpushed)**, run the §3 gates on both presets, surface the snapshot diff before any
`--update-goldens`, and do **not** push until Cowork verifies at source and the user ratifies (instruction §5).

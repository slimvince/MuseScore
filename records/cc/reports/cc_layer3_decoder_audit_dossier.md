# CC — Architectural Layer 3 (KEY/MODE) DECODER read-only pre-build audit dossier

**Status:** READ-ONLY pre-build audit complete. **No production code changed; no behavior change; no corpus
regenerated; no production commit.** Output is this dossier only. Cowork verifies the citations + that nothing
production changed; user ratifies; THEN the decoder (Increment C) is implemented.

**Spec:** `cowork_layer3_keymode_design.md` (SIGNED 2026-06-22). **Delivery plan:** `cowork_layer3_keymode_impl_design.md`
(Increment C = the key-path decoder). **Builds on (does not redo):**
- `cc_layer3_keymode_audit_dossier.md` — the prior Layer-3 read-only audit (as-is resolver, R1/R2/R3, the §3 baseline).
  Cited as **[prior-audit §X]**; its line numbers predate the 2026-06-17 refactor splits + the Increment-A/B commits,
  so **every as-is line:number below was re-confirmed at HEAD this session** and supersedes the prior-audit numbers
  where they differ.
- `tools/cc_layer3_keymode_baseline.py` — the Increment-B held-out GT harness (committed `dcbc0bb4e1`). Cited as
  **[harness]**.
- `docs/key_path_design.md` — prior key-path design material (the Viterbi/emission/transition pins). Cited as
  **[key_path_design]**; it was written over the **per-region** window unit, not the L2-slice grid (the one
  reconciliation delta, called out in §2).

**No-assume rule:** every as-is statement cites `file:line` from a source read **this session**. Items not confirmable
at source are tagged `[unverified]` and listed in §6, never guessed.

---

## §0 — Headline findings (decision-relevant)

1. **The production seam is exactly one call site.** In production (joint-wiring flag OFF) the live per-region
   key/mode = the **Pass-1** call `kr::resolveKeyAndModeRanked(... prevKeyResult ...)` at
   [`regionanalyzer.cpp:633-638`](src/composing/analysis/region/regionanalyzer.cpp#L633-L638), seeded by the
   **initial** call at [`regionanalyzer.cpp:521-524`](src/composing/analysis/region/regionanalyzer.cpp#L521-L524).
   The **joint-build** call at [`regionanalyzer.cpp:393-396`](src/composing/analysis/region/regionanalyzer.cpp#L393-L396)
   is inside `applyJointKeyWiring`, gated on `jointKeyWiringEnabled()` (default OFF —
   [`regionanalyzer.cpp:1166-1167`](src/composing/analysis/region/regionanalyzer.cpp#L1166-L1167)) → **dormant.** The
   decoder replaces the per-slice combination of @633 (and seeds @521); it leaves @393 dormant.
2. **The emission is reusable per-slice, unchanged, and note-only.** `KeyModeAnalyzer::analyzeKeyMode` takes a flat
   `vector<PitchContext>` (pitch / durationWeight / beatWeight / isBass) + `keySignatureFifths` + prefs + optional
   declaredMode ([`keymodeanalyzer.h:498-523`](src/composing/analysis/key/keymodeanalyzer.h#L498-L523)) and has **no
   region/chord/function/cadence input**. The window builder `collectPitchContext` reads only `Note::ppitch()`
   ([`regiontoneprimitives.cpp:182`](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L182)). **The
   signed dependency order (key/mode from notes only) holds at source.**
3. **The full 252-candidate emission vector is accessible byte-identically via the diagnostic dump.** Production
   `analyzeKeyMode` returns only **top-3** ([`keymodeanalyzer.h:508-509`](src/composing/analysis/key/keymodeanalyzer.h#L508-L509)),
   but its `dumpOut` parameter fills one `KeyCandidateScore{...finalScore}` per (tonicPc, modeIndex) candidate (252
   total) without changing the winner ([`keymodeanalyzer.h:136-166`](src/composing/analysis/key/keymodeanalyzer.h#L136-L166)).
   **`finalScore == eval.score`** (the ranking score —
   [`keymodeanalyzer.cpp:579-591`](src/composing/analysis/key/keymodeanalyzer.cpp#L579-L591)). This is the decoder's
   per-slice emission accessor. **Feasibility: confirmed.**
4. **`ChordPathDecoder` is chord-specific and NOT reusable** (re-confirmed at source —
   [`chordpathdecoder.h:80-134`](src/composing/analysis/decode/chordpathdecoder.h#L80-L134)): its state is
   `ChordTemporalContext` + `ChordIdentity` + `PostScoringGateContext` + a rolling stepwise counter + a recent-roots
   window, and `commit()` re-expresses `advanceTemporalContext`. The reusable asset is the **beam/Viterbi *pattern*** +
   the `decode/` module location, not the class. A **dedicated key-path decoder** is needed (matches design §9).
5. **Increment A + B are landed and verified.** The O(N²) note-query gap is closed (`NoteQueryIndex`, O(log N+result)
   — [`note_model.h:113-135`](src/composing/analysis/notemodel/note_model.h#L113-L135)); the held-out direct
   key/mode GT harness is committed with a corrected baseline **Baroque 87.3% / Jazz 61.5%** unambiguous full-match.
   The decoder grades against these, **directionally** (impl-design §4).

---

## §1 — As-is at source (the pieces the decoder reuses or replaces)

### §1.1 — The region-analyzer call site to be replaced (the wiring seam)
`regionanalyzer.cpp::analyzeRegions` calls `kr::resolveKeyAndModeRanked` at **three** sites; only one is the live seam:

| Site | line | role | prevResult | production? |
|---|---|---|---|---|
| Initial | [`521-524`](src/composing/analysis/region/regionanalyzer.cpp#L521-L524) | key/mode at range start → seeds `keyFifths`/`keyMode` (the chord-pass seed, [`600`](src/composing/analysis/region/regionanalyzer.cpp#L600)) | `nullptr` | **YES — seed** |
| **Pass-1 per-region** | [`633-638`](src/composing/analysis/region/regionanalyzer.cpp#L633-L638) | once per coarse region; `localKey = ranked.front()` → `localKeyFifths`/`localKeyMode` | `prevKeyResult` threaded ([`603`](src/composing/analysis/region/regionanalyzer.cpp#L603), [`714`](src/composing/analysis/region/regionanalyzer.cpp#L714)) | **YES — the seam** |
| Joint-build | [`393-396`](src/composing/analysis/region/regionanalyzer.cpp#L393-L396) | re-resolve per FINAL region → `JointKeyRegionInput` stream | `prevKey` threaded | **NO — gated OFF [`1166-1167`](src/composing/analysis/region/regionanalyzer.cpp#L1166-L1167)** |

`resolveKeyAndModeRanked` itself is [`keyresolver.cpp:206-359`](src/composing/analysis/key/keyresolver.cpp#L206-L359)
(flow re-confirmed; matches [prior-audit §1.1]).

**What downstream consumes the per-region `localKey`** (so the per-slice decoder must supply the same to each, per
slice/region):

| consumer | line | uses |
|---|---|---|
| `chordAnalyzer->analyzeChord(tones, localKeyFifths, localKeyMode, …)` | [`668-669`](src/composing/analysis/region/regionanalyzer.cpp#L668-L669) | **the chord scorer reads the key** (key→chord order) |
| `inferNextRootPc(…, localKeyFifths, localKeyMode)` | [`653-654`](src/composing/analysis/region/regionanalyzer.cpp#L653-L654) | next-region root for joint scoring |
| `refineSparseChordQualityFromKeyContext(…, localKeyFifths, localKeyMode)` | [`684-685`](src/composing/analysis/region/regionanalyzer.cpp#L684-L685) | sparse-chord quality refinement |
| `applyTonicPriorToSparseChord(…, localKeyFifths, localKeyMode)` | [`686-687`](src/composing/analysis/region/regionanalyzer.cpp#L686-L687) | sparse-chord tonic prior |
| `HarmonicRegion::keyModeResult = localKey` | [`740`](src/composing/analysis/region/regionanalyzer.cpp#L740) (+ preMerge [`723`](src/composing/analysis/region/regionanalyzer.cpp#L723)) | **the per-region OUTPUT** (display/JSON/snapshot `key` field) |
| Pass-2 inheritance: `subKeyFifths/subKeyMode = parentRegion.keyModeResult.{keySignatureFifths,mode}` | [`785-786`](src/composing/analysis/region/regionanalyzer.cpp#L785-L786) | **Pass-2 does NOT re-resolve** — it inherits the parent region's key |

**Seam summary:** the decoder must produce, per slice, a `KeyModeAnalysisResult` (fifths + mode + tonicPc + score +
normalizedConfidence) that feeds the chord scorer (@668), the sparse passes (@684/686), the next-root (@653), and the
output `keyModeResult` (@740). Pass-2 sub-regions then inherit it (@785). This is a **clean, single-typed seam**: the
existing `HarmonicRegion::keyModeResult` is already the carrier.

### §1.2 — The emission scorer (`KeyModeAnalyzer::analyzeKeyMode`) for per-slice reuse
- **Interface** ([`keymodeanalyzer.h:518-523`](src/composing/analysis/key/keymodeanalyzer.h#L518-L523)):
  `analyzeKeyMode(const vector<PitchContext>&, int keySignatureFifths, const KeyModeAnalyzerPreferences& = default,
  optional<KeySigMode> declaredMode = nullopt, vector<KeyCandidateScore>* dumpOut = nullptr)`.
- **Input** `PitchContext = { int pitch; double durationWeight; double beatWeight; bool isBass; }`
  ([`keymodeanalyzer.h:498-503`](src/composing/analysis/key/keymodeanalyzer.h#L498-L503)) — pitch content + emphasis,
  nothing else. Built today by `collectPitchContext` over a window
  ([`regiontoneprimitives.cpp:123-200`](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L123-L200)).
- **Output** up to 3 `KeyModeAnalysisResult{ keySignatureFifths, mode, tonicPc, score, normalizedConfidence }`,
  winner first ([`keymodeanalyzer.h:124-134`](src/composing/analysis/key/keymodeanalyzer.h#L124-L134)).
- **Candidate sweep = 12 tonics × 21 modes = 252**, flat vector
  ([`keymodeanalyzer.cpp:558-593`](src/composing/analysis/key/keymodeanalyzer.cpp#L558-L593)); six orthogonal terms
  summed into `eval.score` (scale membership + triad evidence + key-sig proximity + characteristic pitch + true
  leading tone + mode prior), minus the declared-mode hint
  ([`keymodeanalyzer.cpp:579-591`](src/composing/analysis/key/keymodeanalyzer.cpp#L579-L591)).
- **Full-vector accessor:** the `dumpOut` vector yields all 252 `KeyCandidateScore.finalScore` byte-identically
  (`finalScore == eval.score` post-disambiguation) — the diagnostic-instrument precedent
  ([`keymodeanalyzer.h:136-166`](src/composing/analysis/key/keymodeanalyzer.h#L136-L166)). **The decoder reads the
  per-slice emission via this dump** (top-3 alone cannot keep K>3 candidates + the incumbent alive).
- **Per-slice callable, unchanged:** inputs are a pure `vector<PitchContext>` + fifths + prefs; **no region/chord
  state** is read. Confirmed reusable over any slice's note set. **[prior-audit §1.2] re-confirmed at HEAD.**

**The 21 modes** ([`keymodeanalyzer.h:36-63`](src/composing/analysis/key/keymodeanalyzer.h#L36-L63)) —
**cross-checked against layer-doc §1 vocabulary; exact match (all 21):**
- Diatonic (7): Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian.
- Melodic-minor (7): MelodicMinor, DorianB2, LydianAugmented, LydianDominant, MixolydianB6, AeolianB5, Altered.
- Harmonic-minor (7): HarmonicMinor, LocrianSharp6, IonianSharp5, DorianSharp4, PhrygianDominant, LydianSharp2,
  AlteredDomBB7. (`KEY_MODE_COUNT = 21` — [`keymodeanalyzer.h:66`](src/composing/analysis/key/keymodeanalyzer.h#L66).)

### §1.3 — The preset → mode-prior path (where the user style preset first enters)
The preset reaches the scorer by overriding the 21 `KeyModeAnalyzerPreferences.modePrior…` fields
([`keymodeanalyzer.h:243-267`](src/composing/analysis/key/keymodeanalyzer.h#L243-L267)), which `scoreModePrior`
consumes ([`keymodeanalyzer.cpp:578`](src/composing/analysis/key/keymodeanalyzer.cpp#L578)). Two override paths,
both verified:
- **UI / production bridge:** `prefs.modePrior* = cfg->modePrior*()` at
  [`notationcomposingbridgehelpers.cpp:162-181`](src/notation/internal/notationcomposingbridgehelpers.cpp#L162-L181)
  — the values are the `ComposingConfiguration` settings, written from a named preset via `applyModePriorPreset`
  ([`composingconfiguration.cpp:822-838`](src/composing/composingconfiguration.cpp#L822-L838)).
- **batch_analyze:** `applyPreset(name, keyPrefs)` writes the 21 priors from the named preset table
  ([`batch_analyze.cpp:201-225`](tools/batch_analyze.cpp#L201-L225)), with a special `"Default"` branch
  ([`batch_analyze.cpp:177-199`](tools/batch_analyze.cpp#L177-L199)) that uses the app's registered settings defaults
  (which diverge from the "Standard" preset on 11 of 21 modes — documented at the same lines). Preset table =
  `modePriorPresets()` ([`modepriorpresets.h:41-74`](src/composing/analysis/key/modepriorpresets.h#L41-L74)).

**Decoder consequence:** because the decoder reuses `analyzeKeyMode(ctx, fifths, prefs, …)` with the same `prefs`,
**the preset keeps entering automatically through the emission** — no new wiring. (Layer-doc §2: this is the first
layer where the preset applies, as a weak mode prior; that property is preserved by construction.)

### §1.4 — Today's hysteresis + look-back/look-ahead (the decoder's starting magnitudes)
All re-confirmed at HEAD:

| value | symbol | number | source |
|---|---|---|---|
| Fixed backward look-back | `shv::LOOKBACK_BEATS` | **16** (= 4 whole notes), FIXED / non-lazy | [`metricweights.h:57`](src/composing/analysis/scoreharvest/metricweights.h#L57), used [`keyresolver.cpp:275-278`](src/composing/analysis/key/keyresolver.cpp#L275-L278) |
| Forward look-ahead (init) | `shv::LOOKAHEAD_BEATS` | **8** | [`metricweights.h:58`](src/composing/analysis/scoreharvest/metricweights.h#L58), used [`keyresolver.cpp:296`](src/composing/analysis/key/keyresolver.cpp#L296) |
| Look-ahead weight | `LOOKAHEAD_WEIGHT` | 0.5 | [`metricweights.h:59`](src/composing/analysis/scoreharvest/metricweights.h#L59) |
| Time decay / measure | `DECAY_RATE` | 0.7 | [`metricweights.h:60`](src/composing/analysis/scoreharvest/metricweights.h#L60) |
| Dynamic-LA stop confidence | `dynamicLookaheadConfidenceThreshold` | **0.60** | [`keymodeanalyzer.h:361`](src/composing/analysis/key/keymodeanalyzer.h#L361) |
| Dynamic-LA step | `dynamicLookaheadStepBeats` | **2** | [`keymodeanalyzer.h:362`](src/composing/analysis/key/keymodeanalyzer.h#L362) |
| Dynamic-LA max | `dynamicLookaheadMaxBeats` | **24** | [`keymodeanalyzer.h:363`](src/composing/analysis/key/keymodeanalyzer.h#L363) |
| Anti-flip margin (diff sig) | `hysteresisMargin` | **2.0** | [`keymodeanalyzer.h:373`](src/composing/analysis/key/keymodeanalyzer.h#L373) |
| Anti-flip margin (relative pair, same sig) | `relativeKeyHysteresisMargin` | **2.0** | [`keymodeanalyzer.h:379`](src/composing/analysis/key/keymodeanalyzer.h#L379) |
| Circle-of-fifths per-step penalty (in emission) | `keySignatureDistancePenalty` | **0.60** | [`keymodeanalyzer.h:295`](src/composing/analysis/key/keymodeanalyzer.h#L295) |
| Per-window confidence sigmoid | `confidenceSigmoidMidpoint` / `Steepness` | **2.0 / 1.5** | [`keymodeanalyzer.h:349-350`](src/composing/analysis/key/keymodeanalyzer.h#L349-L350) |
| Declared-mode hint | `declaredModePenalty` | **1.0** | [`keymodeanalyzer.h:324`](src/composing/analysis/key/keymodeanalyzer.h#L324) |

Dynamic-lookahead loop bound (re-derived): `(24−8)/2 + 1 = 9` iterations max
([`keyresolver.cpp:296-315`](src/composing/analysis/key/keyresolver.cpp#L296-L315)). Hysteresis block
[`keyresolver.cpp:329-345`](src/composing/analysis/key/keyresolver.cpp#L329-L345). **Margins are compared directly
against `analyzeKeyMode` scores** (`results.front().score` — [`keyresolver.cpp:333`](src/composing/analysis/key/keyresolver.cpp#L333)),
so **the 2.0 / 2.0 / 0.60 magnitudes are already in emission-score units** — they transfer to the decoder's transition
cost without rescaling (the key reconciliation with [key_path_design]'s `λ≈0.3`, which was a different, margin-inverted
probe scale — §2).

### §1.5 — Dependency check (key/mode uses notes only)
- **PASS at source.** Emission evidence = `Note::ppitch()` + emphasis only
  ([`regiontoneprimitives.cpp:178-198`](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L178-L198));
  `analyzeKeyMode` consumes only `PitchContext`. **No chord symbol / function / cadence feeds the key/mode decision**
  on the live path. The signed dependency order holds.
- **Coupling flagged (same as [prior-audit §0.2/§4.4], unchanged):** the dormant cadence anchor (`cadencekeyanchor`)
  and `localmodulationdetector` consume chord `rootPc`/`quality`, **not** note-level cues — but they feed only
  `decideJointKey`, gated OFF. **The decoder must NOT promote them as-is** (it would invert chord→key). The signed L3
  design already excludes cadence/function from this layer (passing-vs-real modulation is handled by the change cost),
  so this coupling does **not** block the decoder — it stays out of scope (the gated Stage-5 step owns it).
  **No new coupling found this session.**

---

## §2 — Decoder pins (numbers + shape; feasibility, not built)

> Reconciles with [key_path_design] §2 (states/emission/transition/Viterbi). **The one delta:** [key_path_design] ran
> the decode over the **per-region** window unit (`resolveKeyAndModeRanked` per coarse region); the signed L3 design +
> impl-design run it over the **L2-slice grid** (`changePointSlices`, finer). The Viterbi/K/transition math is
> unchanged by that; only the observation count and the emission-window construction differ. Pins below are stated for
> the L2-slice grid.

### §2.1 — A dedicated key-path (Viterbi) decoder
- **Confirmed needed:** `ChordPathDecoder` is chord-specific and not reusable (§0.4;
  [`chordpathdecoder.h:80-134`](src/composing/analysis/decode/chordpathdecoder.h#L80-L134)). A **dedicated key-path
  decoder** over `(tonicPc, mode)` states, living alongside it in `analysis/decode/`.
- **Observation unit = the L2 `Slice`** (`struct Slice{ int start; int end; }`,
  [`slicer.h:77-80`](src/composing/analysis/slicing/slicer.h#L77-L80)) from
  `changePointSlices(noteModel)` ([`slicer.h:91`](src/composing/analysis/slicing/slicer.h#L91)). One Viterbi column
  per slice.
- **State at slice t** = the per-slice pruned candidate set (§2.2) **∪ the running key** (the incumbent — always kept
  so "stay" survives even when it falls out of the slice's top-K; layer-doc §5.1).

### §2.2 — Pruning count K
- **Proposal: K = 8 per slice, ∪ the incumbent (running key).** Matches [key_path_design §2.1] ("top-N per window, N
  default ≈ 5–8, plus the incumbent"; explicit recommendation "**top-8** as a balance; full-252 only if a measured
  case needs it"). K=8 keeps the relative-pair member (always within a few of the winner, same signature) and the
  near circle-of-fifths neighbours alive; the incumbent union guarantees a brief excursion never evicts the
  established key. Lattice cost = O(slices × K²), K≈8 ⇒ negligible vs the chord pass (cost note §2.8).
- Source for the candidate scores to rank-and-prune = the 252-entry dump (§1.2 / §0.3).

### §2.3 — Change-cost shape + starting magnitudes (emission-score units)
`τ(s_{t-1} → s_t)` =
- **stay (same tonic+mode): 0.**
- **switch:** `base + keyDistance + relativePairExtra`, with the starting magnitudes taken from §1.4 (already in
  emission units):
  - `base` = **2.0** (= `hysteresisMargin`).
  - `keyDistance` = **0.60 × cofSteps(s_{t-1}, s_t)** (= `keySignatureDistancePenalty` per circle-of-fifths step — the
    same per-step value the emission already uses, [`keymodeanalyzer.h:295`](src/composing/analysis/key/keymodeanalyzer.h#L295)).
  - `relativePairExtra` = **2.0** when the switch is a relative-major/minor pair (same `keySignatureFifths`, different
    mode) (= `relativeKeyHysteresisMargin`). This is the "large relative-pair penalty" of design §5.2.
- **Why these and not [key_path_design]'s `λ≈0.3`:** that figure came from an inverted-margin probe on an estimated
  scale, **not** from the resolver's live margins. The resolver compares its 2.0/2.0 margins directly against
  `analyzeKeyMode` scores ([`keyresolver.cpp:333`](src/composing/analysis/key/keyresolver.cpp#L333)), so **2.0 / 0.60 /
  2.0 are the source-true starting magnitudes in the emission's own units.** Reconcile-then-tune: start here; the
  impl's held-out sweep (§3) tunes them.

### §2.4 — Emission-window size (per slice)
- Today's window is **asymmetric + large**: fixed 16-beat look-back + dynamic 8→24-beat look-ahead (§1.4). The design
  states the path's change cost now carries the long-range coherence the big look-back faked (layer-doc §13 /
  crosscutting §8), so **the per-slice emission window shrinks.**
- **Proposal: a small symmetric look-around = the slice span ± ~4 beats (≈ one measure each side), no dynamic
  expansion**, decay/look-ahead-weight retained (`DECAY_RATE=0.7`, `LOOKAHEAD_WEIGHT=0.5`). Rationale: enough context
  for a stable local-fit on a short slice; the cross-slice transition penalty (not a fat window) now enforces
  coherence. Tunable; the floor is "the slice itself" and the ceiling is today's 16+24.
- **Feasibility note (R1-relevant):** today's `collectPitchContext` is a **DOM segment walk**
  ([`regiontoneprimitives.cpp:142-144`](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L142-L144)),
  **not** a NoteModel query — so it did **not** benefit from the Increment-A index. Calling it per slice re-walks the
  DOM per slice. **Recommendation for the impl:** build the per-slice `PitchContext` from the now-indexed
  `NoteModel::overlapping` (O(log N + result), [`note_model.h:113-135,158`](src/composing/analysis/notemodel/note_model.h#L113-L135))
  rather than re-walking the DOM, so the per-slice path is genuinely O(N log N). (Either is correctness-equivalent for
  the key score; this is the perf form.) `[verify at impl: PitchContext-from-NoteModel reproduces collectPitchContext's
  beat/bass/decay weighting]`.

### §2.5 — Confidence (sequence margin) + the "uncertain" threshold
- **Computable from the Viterbi tables.** Run forward best-totals `α_t(s)` and backward best-totals `β_t(s)`. Best
  total through state `s` at slice `t` = `α_t(s) + β_t(s)`; winner key `k*` = `argmax_s`. **Sequence margin at t** =
  `max_s(α_t+β_t) − max_{s : key(s) ≠ k*}(α_t+β_t)` — exactly design §5.4 ("how much better the winning sequence is
  than the best sequence forced to pick a *different* key at that slice"). Both tables are produced by one
  forward + one backward sweep ⇒ feasible.
- **"uncertain" threshold — starting value: margin < 1.0** (≈ half the 2.0 base change penalty), tunable; **plus an
  unconditional "uncertain" mark on relative-pair seam slices** (where the two readings are closest — design §6
  scenario 2). This is distinct from, and replaces for the path, the per-window sigmoid confidence (midpoint 2.0,
  steepness 1.5) which stays available per slice from the emission.

### §2.6 — Reach-back (R3): demand → supply protocol
- **The data is already present.** `NoteModel::build(score)` builds over the **whole score**, not the selection
  ([`regionanalyzer.cpp:508`](src/composing/analysis/region/regionanalyzer.cpp#L508)); `changePointSlices` slices the
  whole model. So for the common whole-score analysis the earlier-in-time notes/slices already exist — **reach-back is
  "decode earlier slices," not "fetch more notes."** The analysis *range* is `[startTick, endTick)`
  (`analyzeRegions(score, startTick, endTick, …)`), so the decoder can extend its decode column-set backward before
  `startTick` from the same model.
- **Protocol:** Architectural Layer 3 *detects* an unsettled opening (the first decoded slices have low sequence
  margin / no stable key) and *demands* earlier slices; Architectural Layer 1/2 *supply* them (already built for
  whole-score; for a true partial selection the bridge would widen `[startTick)` backward and rebuild — `[unverified:
  the bridge's partial-selection rebuild path; the composing-side range entry is source-confirmed]`).
- **Backward cap + stop (proposal):** extend backward in measure-sized steps up to a cap of **8 measures**; **stop**
  when the prevailing earlier key is *established* (the decoded key is stable + confident for ≥ a small run, e.g. 3
  consecutive slices) **or** the cap is hit. (Matches [prior-audit §4 R3]: "until the prevailing/home key the passage
  relates to is established.")

### §2.7 — Incremental re-decode (R2)
- **Feasible in the Viterbi formulation.** A sub-range re-decode with the two boundary key/modes pinned = Viterbi over
  `[i, j]` with the start column restricted to the pinned `s_i` (its `α` seeded, others −∞) and the end column's
  trace-back forced to the pinned `s_j`. Linear in the sub-range length. **Property the impl must hold:** a sub-range
  re-decode with endpoints pinned to a full decode's values == the matching slice of that full decode (§5 property
  test).
- **Caveat (honest):** today there is **no** incremental/dirty-span re-analysis wiring — the bridge does whole-cache
  flush + lazy recompute ([prior-audit §2 R2], agent-sourced, **`[unverified]` — not re-read this session**). So R2
  is an **interface-shape** obligation (design the decoder so a pinned sub-range re-decode is *possible*), not a claim
  that the editor drives it yet. Out of scope to wire the editor here.

### §2.8 — Cost (R1)
- Per-slice emission is already paid in spirit (the resolver runs `analyzeKeyMode` per region today); moving to slices
  multiplies the call count by (#slices / #regions). The Increment-A index makes the per-slice **note query**
  O(log N + result) ([`note_model.h:97-107`](src/composing/analysis/notemodel/note_model.h#L97-L107)) **iff** the
  emission window is built from the NoteModel (§2.4 recommendation), not the DOM walk. The added Viterbi is
  O(slices × K²), K≈8 ⇒ negligible. Corpus slice counts are bounded (Layer-2 corpus validation: 29047 non-empty
  slices over 353 stems, max 391/stem — [STATUS session 9e]). **No O(N²) risk remains if §2.4 is followed.**

---

## §3 — Grading readiness

- **The Increment-B held-out harness is ready and committed** (`tools/cc_layer3_keymode_baseline.py`, commit
  `dcbc0bb4e1`; [harness] header lines 1-62). It implements the **direct (tonic, mode) == WiR-local-GT** metric
  (chord-root-independent), with: the **fixed key extractor** (recovers the Jazz 39% parse-fail → our-keyfail 0 both
  presets), a **genuine two-source unambiguous split** (DCML-parser local key ∧ music21 romanText `RomanNumeral.key`
  over the same WiR annotation; limitation stated — two implementations of one annotation, not two annotators), and a
  **deterministic held-out split** (`md5(stem)%100 < TEST_PCT`; all headline numbers out-of-sample).
- **Baseline the decoder must beat directionally:** held-out **unambiguous full (tonic+mode) match = Baroque 87.3%
  (1136/1301) / Jazz 61.5% (766/1245)** ([STATUS session 9g]; the prior-audit's Jazz 91.5% was a 39%-region-drop
  artifact, now corrected). Grading is **directional, not a fixed bar** (impl-design §4, user 2026-06-22): the genuine
  **rotation / relative-pair defects on unambiguous major/minor cases should drop**; the metric definitions will move
  as L4–L6 are rebuilt, so the only fully meaningful comparison is against the finished pipeline.
- **Modal-vs-major/minor-GT caveat (restated, mandatory):** the WiR GT is **major/minor only**. A perfect-fifth
  "displacement" that is a **defensible modal reading** (e.g. `G-mixolydian` where the GT says `C-major`) is **NOT a
  defect to optimise away** — ~69% of Jazz "misses" are exactly this class ([STATUS 9g], impl-design §4). The
  done-criterion is "full agreement where GT is unambiguous; on ambiguous cases, defensible-or-flagged." Do **not**
  chase the major/minor GT on modal readings.
- **Safety net (hard stop):** the **oracle-root KEY tier** on **both** presets, via `tools/oracle_root_metric.py`
  (the standing per-event tiered metric; KEY band split KEY-HARD vs KEY-TONICIZATION —
  [`oracle_root_metric.py:1-45`](tools/oracle_root_metric.py)). A worse number on **either** preset = STOP. Plus
  dual-preset BIR no-regression (CLAUDE.md gate) and the 11/11 pipeline snapshots (refreshed only after verified
  correct, §4).

---

## §4 — The snapshot-golden surface (what will move; do NOT refresh in this audit)

`pipeline_snapshot_tests` pins **11 golden JSON** files
([`src/notation/tests/pipeline_snapshot_tests/snapshots/*.json`](src/notation/tests/pipeline_snapshot_tests/snapshots)):
`bach_bwv806_gigue`, `bach_bwv806_prelude`, `bach_chorale_001`, `bach_chorale_003`, `bach_chorale_137`,
`chopin_bi105_op30_1`, `chopin_bi105_op30_2`, `corelli_op01n08a`, `mozart_k279_1`, `mozart_k280_1`,
`schumann_kinderszenen_n01`.

Each annotation entry carries `{ "key": <local-key string>, "text": <chord symbol OR Roman numeral>, "tick": <int> }`
(verified — [`bach_chorale_001.json:1-60`](src/notation/tests/pipeline_snapshot_tests/snapshots/bach_chorale_001.json)).

**What moves when the per-slice decoder replaces the per-region argmax:**
1. **The `key` field** of every annotation on any slice where the decoder picks a different key/mode than the
   per-region argmax (the direct target).
2. **The Roman-numeral `text`** wherever it is key-relative (e.g. `"vi"`, `"V"`) — the RN re-spells under the new
   local key. (The chord-symbol `text` like `"Em"` is key-independent and moves only if the chord itself changes.)
3. **Region boundary / grouping shifts** if a key change lands on a different slice than the old region boundary
   (the annotation set is per-region; a moved key boundary can split/merge displayed groups).

**Expected concentration:** the four non-Bach-chorale, modulation-heavy goldens (`chopin_*`, `mozart_*`, `corelli_*`,
`schumann_*`) will move most; the chorales (`bach_chorale_*`, single-key) least. **All 11 are candidates** — none is
guaranteed byte-stable, because a relative-pair re-reading can flip even a "stable" chorale's mode label.

**Refresh procedure (for the impl, AFTER verified correct — not now):** `pipeline_snapshot_tests.exe
--update-goldens` then re-run to confirm (CLAUDE.md). **This audit refreshes nothing.**

---

## §5 — Deterministic decoder test fixtures (the impl's coverage spec; author later)

**Fixture mechanism** (per memory `feedback_composing_tests_mscx_fixtures.md`): `composing_tests` cannot import
MusicXML — fixtures are **`.mscx`** in [`src/composing/tests/data/`](src/composing/tests/data) (the existing
`s1c_*` / `nm_*` key+slice fixtures are the template; `s1c_a_minor_amb.mscx`, `s1c_c_major.mscx`, `s1c_c_minor.mscx`,
`s1c_g_minor.mscx` already exist and seed several cases below). Test file pattern = a new `decode_keymode_tests.cpp`
alongside [`decode_tests.cpp`](src/composing/tests/decode_tests.cpp) / [`slicer_tests.cpp`](src/composing/tests/slicer_tests.cpp).

**Behaviour fixtures (each pins the expected per-slice key/mode):**
1. **Single-key passage** → one key throughout, no spurious switches, high confidence. *(Seed: `s1c_c_major.mscx`.)*
2. **Relative-major/minor near-tie with a whole-stretch tilt** → the correct member chosen **consistently** across all
   slices, with **low confidence + "uncertain"** at the seam. *(Seed/extend: `s1c_a_minor_amb.mscx` — the A-minor↔C-major
   ambiguity the §3 baseline shows the per-region argmax flipping.)*
3. **Brief tonicization** (1–2 slices of a `V/V`-style excursion) → **key UNCHANGED** (the change cost is not repaid
   over so few slices).
4. **Sustained, cadence-less modulation** (a long run that settles in the new key, no cadence) → **key CHANGES** (the
   accumulated better fit repays the change cost — note: *no* cadence detection, by design).
5. **Near-vs-remote switch with equal local evidence** → the **near** key (the circle-of-fifths `keyDistance` term
   makes the remote switch cost more).
6. **Selection beginning mid-passage** → **forces reach-back** (unsettled opening → extend backward until the
   prevailing earlier key is established, §2.6).

**Property / consistency / determinism tests:**
- **Sub-range re-decode == full decode (R2):** a sub-range decode with both endpoint key/modes pinned to a full
  decode's values equals the matching slice of the full decode (§2.7).
- **Determinism:** same input model → identical slices → identical decoded sequence + confidences, every run.
- **Branch coverage:** every decoder branch exercised (stay / switch-near / switch-remote / relative-pair switch /
  incumbent-kept / reach-back-triggered / reach-back-cap-hit / uncertain-marked) — the design §10 "every branch
  exercised" bar.

---

## §6 — Deliverables, `[unverified]` items, stop conditions

**Delivered:** this dossier (`cc_layer3_decoder_audit_dossier.md`). **No production code; no behavior change; no corpus
regen; no commit; no snapshot refresh.** Read-only inspection only (Read/Grep/Glob + read-only `git log`/`sed`/`find`
shell reads).

**`[unverified]` (not confirmable at source this session — listed, not guessed):**
1. The bridge's **partial-selection** range-rebuild path for reach-back (§2.6) — the composing-side
   `analyzeRegions(score, startTick, endTick)` entry + the whole-score `NoteModel::build` are source-confirmed; the
   notation-bridge selection→range + rebuild are agent-sourced in [prior-audit §2 R2], not re-read this session.
2. **R2 incremental re-analysis wiring** (whole-cache-flush + lazy recompute; no dirty-span re-run) — [prior-audit §2
   R2], agent-sourced, not re-read. Affects only the *editor-driven* incrementality claim; the Viterbi sub-range
   re-decode itself is source-feasible (§2.7).
3. That a **NoteModel-built per-slice PitchContext reproduces `collectPitchContext`'s** beat/bass/decay weighting
   (§2.4 perf recommendation) — to be confirmed at impl; correctness-equivalent either way.
4. `tick2measure` internal complexity ([prior-audit §2 R1]) — not re-read; per-call window cost otherwise bounded.

**Stop conditions (instruction §7) — status: none breached.**
- No production / behavior / scoring change; no probe altered analysis output (read-only).
- Every as-is item confirmed at source or tagged `[unverified]` above.
- The decoder design does **not** require building the gated joint key-and-chord step (cadence/function stay out of
  scope; the residual is flagged for Stage 5).
- The key/mode evidence is **not** coupled to chord/function/cadence on the live path (§1.5) — the dependency order is
  cleanly severable (the only chord-coupling is in the dormant, flag-OFF cadence/modulation instruments, which the
  decoder does not promote).

**Two corrections on record carried forward from [prior-audit §5]** (still true; not re-litigated here): (a) the
as-built cadence anchor + modulation detector are **chord-symbol-dependent**, not note-level — they stay out of L3;
(b) R2's "edit re-analyzes only the dirty span" is a **target**, not the as-is.

**Next (after Cowork citation-verification + user ratification):** implement Increment C — the dedicated key-path
Viterbi decoder (emission = `analyzeKeyMode` per slice via the 252-dump; transition = the §2.3 cost; window = §2.4;
confidence = §2.5; reach-back = §2.6; sub-range re-decode = §2.7), wired into the @633 seam, graded by the §3 set
(directional held-out + oracle KEY tier + dual-preset BIR), with the §4 snapshots refreshed only after verified
correct.

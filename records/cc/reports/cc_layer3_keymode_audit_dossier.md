# CC — Layer 3 (KEY/MODE) read-only audit dossier

**Status:** READ-ONLY audit complete. **No production code changed; no corpus regenerated.** One read-only
diagnostic was added (`tools/cc_layer3_keymode_baseline.py`, Python, reads existing JSON + rntxt only) — it is
not production and does not affect any analysis output (byte-identical). Cowork verifies the citations + that
nothing production changed; user ratifies; then the impl design.

**Spec:** `cowork_layer3_keymode_design.md` (SIGNED 2026-06-21). This dossier verifies the §3/§4 `[verify]` items
and the §0.2 R1–R3 items at source, establishes the **direct key/mode-vs-ground-truth metric + baseline**, and
specifies (does not build) the path/emission/transition design.

**No-assume rule:** every as-is statement cites `file:line` from a source read this session. Items not confirmable
at source are tagged `[unverified]` and listed, not guessed.

---

## §0 — Headline findings (the decision-relevant ones)

1. **Production key/mode = `resolveKeyAndModeRanked` (per-region argmax + hysteresis) ONLY.** The cadence anchor
   and `localmodulationdetector` feed *only* `decideJointKey`, whose decisions are applied solely under
   `jointKeyWiringEnabled()` — **default OFF** (`jointkeydecision.cpp:137-140`, env `MUSE_JOINT_KEY_WIRING`). They
   are dormant/diagnostic, exactly as the design states.
2. **The resolver's *evidence* is genuinely key-agnostic of chord symbols** (`collectPitchContext` reads raw note
   `ppitch`, never chord identities — `regiontoneprimitives.cpp:178-187`). **But the cadence anchor + modulation
   detector are NOT note-level — they consume chord `rootPc`/`quality`** (`cadencekeyanchor.cpp:51-58`,
   `localmodulationdetector.cpp:100-108`). This **contradicts the design's claim** (§0.1/§3) that "today's
   key-agnostic cadence anchor" is *note-level*. It is key-agnostic *of the resolved key*, but **chord-symbol
   dependent**. Promoting it into L3 as-is would invert the dependency order (chord→key). **Correction on record
   for the design.**
3. **Direct key/mode baseline (NEW metric, this audit):** current resolver vs When-in-Rome **local-key** GT —
   **on the unambiguous (stable-key) regions: 85.5% Baroque / 91.5% Jazz** correct (tonic+mode); **on the
   ambiguous (modulation) regions it follows the modulation only ~8–10% and stays in the home key 75–82%.** This
   is the design's predicted relative-pair + modulation floor, now quantified. (§3.)
4. **Scale (R1):** the resolver's per-region cost is **window-bounded** (`collectPitchContext` starts at the
   window's measure and early-terminates — `regiontoneprimitives.cpp:134-144`), NOT O(N²). **However the note-model
   range queries that feed the L2-slice tone collection (`NoteModel::overlapping`/`onsetIn`) scan `m_notes` from
   the head with no lower-bound → O(prefix-up-to-t1) = O(N) per query → O(N²) over all slices**
   (`note_model.cpp:141-176`). That indexing gap is what L3's slice path must fix, and it is a real cost.

---

## §1 — As-is map (the `[verify]` items, file:line + exact behavior)

### 1.1 `keyresolver.cpp` `resolveKeyAndModeRanked` (lines 206–359)
The full production flow, in order:

| Step | Lines | Behavior |
|---|---|---|
| Key-sig read | 218–221 | `keySigEvent(tick).concertKey()` at the clamped staff → `keyFifths` (= `notatedFifths`). |
| Declared mode | 224–239 | Maps engraving `KeyMode` enum → `KeySigMode` (MAJOR/IONIAN→Ionian, MINOR/AEOLIAN→Aeolian, explicit modes pass through); unknown → `nullopt`. |
| Mode-absent floor | 249–251 | `prefs.ignoreDeclaredMode` (batch `--ignore-declared-mode`) drops declared mode entirely. Default false = no-op. |
| Partial-sig correction | 260–263 | Baroque "one-accidental-short" detector (107–190): duration-weighted histogram over segments sharing the notated signature; if the missing accidental is pervasive (≥3% weight) AND dominant (≥2× its natural), shifts the signature one step. Declared-gated. |
| **Fixed backward lookback** | 275–278 | `windowStart = tick − Fraction(LOOKBACK_BEATS,4)`, **`LOOKBACK_BEATS=16`** (`metricweights.h:57`) = 4 whole notes, clamped to 0. **This is the asymmetric, NON-lazy backward window (R3 gap).** |
| Piece-start opening | 280–290 | Note-based (the former declared-mode short-circuit was removed in 4b-i); `windowStart` clamps to 0 inside the lookback span; `prevResult==nullptr` handled by the hysteresis guard. |
| **Dynamic forward lookahead** | 292–315 | Loop: `windowEnd = tick + Fraction(lookaheadBeats,4)`, init `LOOKAHEAD_BEATS=8`; `collectPitchContext` → `analyzeKeyMode`; stop when `front().normalizedConfidence ≥ dynamicLookaheadConfidenceThreshold` (**0.60**) OR `lookaheadBeats ≥ dynamicLookaheadMaxBeats` (**24**); else `+= dynamicLookaheadStepBeats` (**2**). ⇒ **≤ (24−8)/2 + 1 = 9 iterations.** |
| Fallback | 318–321 | `results.empty()` OR `distinctPitchClasses(ctx) < 3` → `fallbackResult` (notated sig, declared-or-Ionian, conf 0). |
| **Hysteresis** | 329–345 | If `front().mode != prevResult->mode`: margin = `relativeKeyHysteresisMargin` (**2.0**) when same fifths (relative pair), else `hysteresisMargin` (**2.0**); if `front().score < prevResult->score + margin`, promote the prev-mode/prev-fifths candidate to front. |
| Strong prior | 347–356 | **REMOVED in 4b-i** — no hard declared-mode veto remains. |
| `prevResult` threading | call sites | Caller passes the previous region's `ranked.front()` as `prevResult` (see 1.5). |

The declared mode now influences output **only** via the small `declaredModePenalty` hint inside `analyzeKeyMode`
(keyresolver.h:43–45).

### 1.2 `keymodeanalyzer.cpp` `analyzeKeyMode` (lines 530–822) — the EMISSION model
- **Candidate sweep:** 12 tonic × **21 modes** (`ACTIVE_MODE_INDICES`, 71–75) = **252 candidates**, flat vector
  (559–593). MODES table 43–68 (7 diatonic + 7 melodic-minor + 7 harmonic-minor).
- **Six orthogonal terms** summed per candidate (579–580):
  1. scale membership (`scoreScaleMembership` 238–261, four cases in/out candidate×keysig),
  2. triad evidence (`scoreTriadEvidence` 265–313: tonic/third/fifth/true-7th weights, complete-triad bonus,
     missing-tonic penalty, extra-scale diminishing term),
  3. characteristic pitch (`scoreCharacteristicPitch` 321–355, single or require-both),
  4. true leading tone (`scoreTrueLeadingTone` 363–375, `(tonic+11)%12`),
  5. key-sig proximity (`scoreKeySignatureProximity` 411–420, −penalty × circle distance),
  6. mode prior (`scoreModePrior` 378–407, 21 independent priors).
- **Declared-mode hint** (586–591): outside-class candidates lose `declaredModePenalty` (**1.0**). Dropped when
  `declaredMode == nullopt`.
- **Pairwise disambiguation** (`applyPairwiseDisambiguation` 455–488) applied to the **top-2** modes sharing the
  signature (595–621) — relative-pair tonic/complete-triad boosts.
- **Family selection** (633–681): among modes sharing the signature, pick by focused `tonalCenterScore`
  (429–441) but do not let it overturn a materially stronger raw winner (`tonalCenterDeltaThreshold` 0.25;
  diatonic-tiebreak guard 669–678).
- **Confidence** (744–766): sigmoid of (top1−top2) raw-score **gap**: `1/(1+exp(−steepness·(gap−midpoint)))`,
  midpoint 2.0, steepness 1.5.
- **Output:** up to 3 `KeyModeAnalysisResult` (winner first), each `{keySignatureFifths, mode, tonicPc, score,
  normalizedConfidence}`.
- **Emission interface is reusable per-slice (§4):** inputs are a `vector<PitchContext>` (pitch, durationWeight,
  beatWeight, isBass — keymodeanalyzer.h:498–503) + `keySignatureFifths` + prefs + optional declaredMode. It has
  **no dependency on region/chord state** — it can be called over any window/slice's note set. ✓

### 1.3 `cadencekeyanchor.cpp` — cadence detection + home anchor
- `detectAuthenticCadences` (36–98): scans consecutive `CadenceRegionInput` pairs for V→I — dominant must be
  `ChordQuality::Major` (58–60), tonic Major/Minor (64–66), descending-fifth roots (69–71), leading tone
  physically present in the dominant's mask (78–82). Emits `AuthenticCadence{tonicPc, minorMode, endsPhrase,
  chromaticLeadingTone}`.
- `aggregateGlobalAnchor` (122–205): salience-weighted vote (base 1.0 / structural 2.0 / chromatic-LT 1.0 /
  finality-recency 1.0, 115–118); Picardy correction (178–183); confidence = winner weight share.
- **★ Chord-coupling (§4.4 finding):** `CadenceRegionInput` carries `rootPc` and `quality` (51–58, 64–71) — these
  are **chord-analysis outputs**, not note-level features. The detector is key-agnostic *of the resolved key* but
  **depends on chord symbols.** The design's "note-level cadence cue" is **not** what is built today.

### 1.4 `localmodulationdetector.cpp` — establishment → confirmation → commit
- `detectLocalModulations` (113–287): (1) candidates = per-cadence local tonics (120–123); (2) establishment =
  assign each region to nearest consistent cadence's key (151–182, consistency = root is a diatonic degree +
  ≤`kPitchTolerance=2` out-of-collection pcs, 100–108); (3+4) confirmation+commit = maximal same-key runs, commit
  only when `runChords ≥ kEstablishmentMinChords=5` AND ≥1 confirming cadence inside (188–282).
- **Guard / dormancy:** the B2 subdominant guard suppresses a span **only** when `jointKeyWiringEnabled()`
  (275–278). Flag-OFF commits every span for the diagnostic; the result is consumed only by `decideJointKey`
  under the flag → **production never sees it.**
- **★ Same chord-coupling:** reads `rootPc`/`quality`/`pitchClassMask` (the `CadenceRegionInput` fields) — chord
  dependent, not note-level.

### 1.5 `regionanalyzer.cpp` — the per-region call sites (the argmax the path replaces)
Three calls to `kr::resolveKeyAndModeRanked`:
- **Initial** (521–524): key/mode at range start (`prevResult = nullptr`).
- **Per-region Pass-1, with hysteresis** (633–638): once per coarse boundary region, threading
  `prevKeyResult` → `ranked.front()`. **This is the production per-region argmax+hysteresis.** The result
  (`localKeyFifths`/`localKeyMode`) then feeds chord analysis (`inferNextRootPc` 653) ⇒ **key→chord ordering in
  production** (dependency order holds).
- **Joint-build** (393–396): re-resolves per FINAL region to build the `JointKeyRegionInput` stream for
  `decideJointKey` (445) — the **flag-gated** dormant path.

### 1.6 §4.4 key-agnostic-of-chords check
- **Resolver evidence: PASS.** `collectPitchContext` reads only `Note::ppitch()` from ChordRest segments
  (`regiontoneprimitives.cpp:166-198`); `analyzeKeyMode` consumes `PitchContext` (pitch/duration/beat/bass). No
  chord symbol is read.
- **The one production chord-coupling = the resolution UNIT, not the evidence:** key is resolved per **coarse
  chord-segmentation region** (§4.3), and region boundaries come from Pass-1 chord-change detection. L3 fixes this
  by re-homing to the L2 slice grid.
- **Cadence/modulation instruments: chord-coupled** (§1.3/§1.4) — but dormant in production. If L3 promotes them
  (design §5.1 4d-ii), it must either rebuild cadence detection on note-level cues (bass line + leading-tone
  resolution directly from the note model) or accept a controlled preliminary chord-root pass. **Flagged for the
  impl design.**

---

## §2 — Scope / scale / incrementality / extension (R1–R3 at source)

### R1 — complexity (does it hold at full-act scale?)
- **`collectPitchContext` is window-bounded, NOT whole-score.** It starts at `sc->tick2measure(windowStart)`
  (`regiontoneprimitives.cpp:134`) and walks segments with early-termination `s->tick() <= windowEnd`
  (142–144), skipping `segTick < windowStart` (146). Per call cost = O(segments-in-window × nstaves × VOICES) =
  **O(notes-in-window)**, plus one `tick2measure` lookup `[unverified: tick2measure internal complexity — likely
  O(log M) or O(M); not read this session]`.
- **Resolver per region:** ≤9 lookahead iterations (§1.1) × O(window) ⇒ **bounded per region** (window cap =
  16-beat lookback + 24-beat lookahead). The resolver itself is **not** the O(N²) risk.
- **★ The real indexing gap is in the note-model range queries** (feeding L2-slice tone collection, which L3 will
  consume): `NoteModel::overlapping(t0,t1)` and `onsetIn(t0,t1)` iterate `m_notes` **from `begin()`** with an
  upper-bound early-break only and **no `lower_bound` on `t0`** (`note_model.cpp:150-153, 167-170`). Cost =
  O(notes with onset < t1) = **O(N) per query for late windows** ⇒ **O(N²)** across all slices. `weightedPcView`
  calls these (`regiontonecollector.cpp:217,282` `[agent-sourced, not re-read this session]`). **Fix at L3: add a
  `lower_bound` on onset (m_notes is already onset-sorted) → O(log N + k) per query.**

### R2 — edit-trigger / invalidation (selection → analyzed range; region vs whole score)
*(Bridge file:lines below are agent-sourced from `src/notation/internal/notationcomposingbridge*.cpp`; recommend
Cowork spot-verify — I did not re-read these this session. The composing-side entry `analyzeRegions` and the
region call sites ARE source-verified above.)*
- **Selection → range:** `addHarmonicAnnotationsToSelection` reads `Selection::tickStart()/tickEnd()` for a range
  selection, else min/max over `noteList()` `[notationcomposingbridge.cpp:1283-1321, agent-sourced]`. Single-note
  status-bar path uses `note->tick()` `[notationcomposingbridge.cpp:884-896, agent-sourced]`.
- **Never whole-score in production:** paths are (a) ±1-measure expanding window around a clicked note, (b) the
  selected `[startTick,endTick)` (+~8-measure RN lookahead). Whole-score is validation/batch only. All converge on
  `mu::composing::analysis::region::analyzeRegions(score, startTick, endTick, …)` (`regionanalyzer.h:141`,
  source-verified by the call sites).
- **★ No incremental (dirty-span) re-analysis exists.** There is **no automatic re-run on edit**. An edit bumps
  the undo-stack token; a 16-entry MRU **window cache** is guarded by `(score, undo-token, excludeStaves)` and
  **any mismatch flushes the WHOLE cache** (conservative) — re-analysis happens only on the next manual query
  `[notationcomposingbridge.cpp:371-422, agent-sourced]`. ⇒ The design's R2 "edit re-analyzes only the dirty span
  + margin" is **a target, not the as-is**: today it is whole-cache-flush + lazy recompute-on-demand.

### R3 — context extension (the unify/symmetrize target)
- **As-is hybrid confirmed:** fixed backward `LOOKBACK_BEATS=16` (`keyresolver.cpp:275`, `metricweights.h:57`) +
  dynamic forward lazy lookahead (`keyresolver.cpp:296-315`).
- **Gap 1 — asymmetric:** backward is a fixed 16-beat window; only forward is lazy. Key/mode needs **lazy
  backward** too (to reach a cadence further back than 16 beats — the passing-key test).
- **Gap 2 — scattered:** three separate reach-outside mechanisms: the resolver window (keyresolver.cpp:275–315),
  the region next-region lookahead (`regionanalyzer.cpp:643-655`), and the cadence anchor's own region stream
  (cadencekeyanchor). L3 unifies these on the slice grid.

---

## §3 — Direct key/mode-vs-ground-truth metric + baseline (the headline)

### 3.1 The metric (defined + built read-only)
- **Our side:** per-region resolved key string `"key"` in `tools/corpus/<preset>/*.ours.json` (e.g. `"Gmin"`,
  `"Bbmaj"`), with `startTick`/`endTick`. Parsed to `(tonicPc, isMajor)` by `compare_rn._our_key_tonic`.
- **GT side:** **When-in-Rome Bach rntxt local key** via `dcml_parser.find_wir_file` + `parse_rntxt_file`
  (`local_key`/`global_key` per measure/beat), parsed by `compare_rn._dcml_key_tonic`. **Aligned by the SAME
  validated time-overlap aligner** (`compare_analyses.align_dcml_regions`, `DEFAULT_DCML_MATCH_MODE="time-overlap"`)
  that `compare_rn` uses.
- **Direct comparison** = `(our tonic, our mode) == (WiR local tonic, WiR local mode)` — **independent of chord
  root** (unlike the indirect `key_disagree` RN proxy, which only fires when the root coincides).
- **Diagnostic:** `tools/cc_layer3_keymode_baseline.py` (read-only; reads existing `.ours.json` + WiR rntxt; **no
  build, no corpus regen; production byte-identical**).

### 3.2 GT-source decision + the unambiguous/ambiguous split (honest about the limit)
- **The design's two-source "DCML ∧ music21 concur" unambiguous filter cannot be done at LOCAL granularity
  read-only:** the committed `*.music21.json` carries only a **per-piece GLOBAL** key (`key == keyGlobal` for all
  353 stems — verified by the metric agent), so music21 cannot corroborate a *local* key. WiR rntxt is the **only**
  on-disk **local** GT.
- **Operationalized split (single-source proxy):** **unambiguous ≈ regions where WiR `local == global`** (no local
  modulation — both annotators/sources would concur on the global key there); **ambiguous ≈ `local != global`**
  (modulation / tonicization — exactly the relative-pair + modulation hard cases). This is a defensible proxy for
  the design's split; the true two-source-concurrence + held-out version is an impl-time refinement (§3.4).

### 3.3 Baseline numbers (current resolver, per preset)
WiR coverage = **326 / 353** stems each preset (27 uncovered — never scored, never folded into /353).

**Baroque** (10 033 scorable regions; our-keyfail 83):
| Bucket | Result |
|---|---|
| DIRECT (tonic+mode) == local | **55.2%** (5536/10033); duration-weighted 54.8% |
| tonic-only / mode-only match | 55.5% / 74.9% |
| **Unambiguous (stable, 60.0%): full match** | **85.5%** (5146/6021); dur-wt 84.7% |
| **Ambiguous (modulation, 40.0%)** | matched-local **9.7%** / stayed-home **75.4%** / neither 14.9% |

**Jazz** (5 948 scorable regions; **our-keyfail 3839 ⚠**):
| Bucket | Result |
|---|---|
| DIRECT (tonic+mode) == local | **61.5%** (3657/5948); duration-weighted 61.5% |
| tonic-only / mode-only match | 61.8% / 76.1% |
| **Unambiguous (stable, 64.2%): full match** | **91.5%** (3492/3817); dur-wt 91.3% |
| **Ambiguous (modulation, 35.8%)** | matched-local **7.7%** / stayed-home **82.4%** / neither 9.8% |

**Top direct-mismatch patterns** (ours → WiR-local) — the structural story, confirming the design thesis:
- **Relative-major/minor pairs:** Amin→Cmaj (272), Gmin→Bbmaj (225), Amin→Dmin (206), Dmin→Fmaj (186),
  Bmin→Dmaj (158), Emin→Gmaj (153). (Same signature; resolver picks the wrong member of the pair.)
- **Un-followed dominant tonicizations:** Cmaj→Gmaj (210), Amaj→Emaj (146), Dmaj→Amaj (116). (Resolver stays in
  the home key while WiR modulates to V.)

### 3.4 Interpretation + caveats (what the numbers do and do not establish)
- **The "real defect rate today" (the done-criterion target ~100% on unambiguous) is ≈14.5% Baroque / ≈8.5%
  Jazz** (the 85.5% / 91.5% complements). That is the concrete bar L3 must close.
- **The ambiguous bucket is the relative-pair + modulation floor**: the resolver follows a real modulation only
  ~8–10% of the time and stays home 75–82%. *Note:* "stayed home" is **not pure error** — a brief tonicization
  *should not* switch the key, so part of this bucket is correct/defensible. The metric cannot, single-source,
  separate "should-have-switched" from "correctly-stayed"; that needs the passing-vs-structural ground truth the
  design's keyscape/establishment test targets. **This is exactly the residual L3's path + promoted modulation
  detector attacks, and the gated Stage-5 joint step finishes.**
- **⚠ Jazz parse caveat:** **39% of aligned Jazz regions (3839) fail our-key parsing** — the Jazz preset emits key
  strings `_our_key_tonic`'s regex rejects (modal/extended labels `[unverified — not enumerated this session]`).
  The Jazz direct numbers are valid only on the parseable 61%. **Enumerate and fix the parser before relying on
  Jazz direct figures.** (Baroque parse-fail is only 0.8%.)
- **In-sample caveat (the §6.3 held-out requirement is NOT yet met):** these are full-corpus numbers. Mitigation:
  the resolver is tuned to the **BIR root gate**, *not* to WiR key labels, so memorization bias is limited — but a
  proper **held-out split** is mandatory at impl time before claiming the done-criterion.
- **Scope caveat:** GT is **major/minor functional**; the modal palette (Dorian/Mixolydian/…) has no RN GT and is
  unmeasured here (design §6 scope).

---

## §4 — Path / emission / transition feasibility (specify, do not build)

- **Emission = reuse `analyzeKeyMode` per slice.** Confirmed reusable (§1.2): pure `vector<PitchContext>` →
  ranked `KeyModeAnalysisResult`, no region/chord coupling. Run it over each L2 slice's note set (built from the
  note model) to get the 252-candidate emission score per slice.
- **Path = a dedicated key-path decoder (Viterbi/beam over (tonic,mode) states).** Transition = key-distance +
  **self-transition penalty** (the principled hysteresis replacing the `relativeKeyHysteresisMargin` nudge).
  **★ `ChordPathDecoder` is NOT directly reusable:** it is chord-specific — it carries `ChordIdentity`,
  `ChordTemporalContext`, a stepwise counter, and a recent-roots window, and re-expresses
  `advanceTemporalContext` (`chordpathdecoder.h:69-134`). The reusable asset is the **beam/decode *pattern*** (and
  the Stage-3.2 "wider beam" precedent), not the class. A **dedicated key-path decoder** over (tonic,mode) is
  cleaner. State space = 252 raw; prune to in-signature modes + circle-of-fifths neighbors before it grows toward
  the gated-joint design. *(Prior design material exists: `docs/key_path_design.md`, `docs/scoped_joint_design.md`
  — reconcile, not re-derive.)*
- **Passing keys = self-transition penalty + promote `localmodulationdetector` (4d-ii).** Feasible, BUT the
  detector's inputs (`rootPc`/`quality`) are **chord-derived** (§1.3/§1.4) — promotion requires either rebuilding
  cadence detection on note-level cues or a controlled preliminary chord-root pass. Optional keyscape
  multi-timescale persistence check is note-derivable (pitch-class histograms at multiple window sizes). **The
  baseline (§3.3) shows this is the highest-value target: the entire ambiguous bucket lives here.**
- **Output representation (design §1 contract):** the as-is already carries the raw materials — up to 3 ranked
  `KeyModeAnalysisResult` + per-result `normalizedConfidence` (sigmoid gap, keymodeanalyzer.cpp:744-766). L3
  extends this to a **per-slice ranked-alternatives + confidence path**, marking the **flagged residual** =
  low-confidence (small sigmoid gap) ∪ modulation-boundary slices, for L4's prior and the gated Stage-5 joint
  step.
- **Extension protocol (R3):** L3 issues the **demand** ("cannot classify without the prior key → reach back");
  L1/L2 **supply** the grown span. Stop seed = "until the prevailing/home key the passage relates to is
  established." Concrete trigger = a candidate local key whose `local != global` and whose establishment run/cadence
  lies outside the current backward window (the §3.3 ambiguous cases).

### 4.1 Deterministic test cases to specify for the impl (fixtures over the note model)
1. **Clear single-key passage** — path is constant; no spurious switches.
2. **Relative-major/minor pair** (e.g. C major ↔ A minor opening) — the disambiguation the §3.3 patterns show
   failing today (Amin↔Cmaj etc.).
3. **Brief tonicization** (a 1–2 chord V/V) — path must **NOT** switch the key (self-transition penalty holds).
4. **Cadence-confirmed modulation** (sustained run + V→I in the new key, ≥5 chords) — path **MUST** switch.
5. **Selection starting mid-tonicization** — forces **backward extension** until the home key is in view.

---

## §5 — Deliverables, unverified items, stop conditions

**Delivered:**
- This dossier (`cc_layer3_keymode_audit_dossier.md`).
- `tools/cc_layer3_keymode_baseline.py` — the read-only direct key/mode-vs-WiR-local-GT diagnostic. **It is not
  production; it reads only existing `.ours.json` + WiR rntxt; it builds nothing and regenerates no corpus;
  analysis output is byte-identical.** Re-run: `python tools/cc_layer3_keymode_baseline.py` (optional `--json
  <path>`).

**`[unverified]` (not confirmable at source this session — listed, not guessed):**
1. `tick2measure` internal complexity (R1) — not read; per-call window cost otherwise bounded.
2. R2 bridge file:lines (selection→range, the MRU cache, edit invalidation) are **agent-sourced** from
   `notationcomposingbridge*.cpp` — recommend Cowork spot-verify. The composing-side `analyzeRegions` entry and the
   three `resolveKeyAndModeRanked` call sites ARE source-verified.
3. `weightedPcView`'s exact call into `overlapping`/`onsetIn` (`regiontonecollector.cpp:217,282`) is agent-sourced;
   the `overlapping`/`onsetIn` O(prefix) bodies themselves ARE source-verified (`note_model.cpp:141-176`).
4. The exact Jazz key-string forms causing the 39% parse-fail (§3.4) — not enumerated; flagged as a measurement
   caveat to resolve before trusting Jazz direct numbers.

**Stop conditions (design §6) — status:** none breached. No production/behavior/scoring change was made; no
diagnostic altered analysis output; the baseline was produced **from existing scores + annotations + existing
tooling** (no corpus regen); the path design did **not** require building the gated joint key↔chord step.

**For the design, two corrections on record:**
- (a) the as-built cadence anchor + modulation detector are **chord-symbol-dependent**, not "note-level" as
  §0.1/§3 state (§1.3/§1.4/§4.4);
- (b) R2's "edit re-analyzes only the dirty span + margin" is a **target**, not the as-is — today's bridge does
  whole-cache-flush + lazy recompute-on-demand, with no incremental re-run (§2 R2).

**Next (after Cowork verification + user ratification):** the L3 impl design — emission-per-slice + dedicated
key-path decoder (Viterbi/beam, self-transition penalty), the note-level cadence-cue rebuild (sever the chord
coupling), the unified symmetric lazy extension, the `lower_bound` index fix for the note-model range queries, and
the held-out + two-source-concurrence upgrade of the §3 metric.

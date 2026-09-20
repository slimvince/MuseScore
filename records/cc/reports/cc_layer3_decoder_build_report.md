# CC — Architectural Layer 3 (KEY/MODE) DECODER build report (ISOLATED + graded; production byte-identical)

**Status:** BUILT + UNIT-TESTED + GRADED, **isolated** (NOT wired into the live analyzer). Production analysis
output is **byte-identical**; the decoder runs only under the read-only `batch_analyze --decode-keymode`
diagnostic. Committed **locally (unpushed)**; the held WIP (B2 trio + the doc set) stays UNSTAGED. Cowork verifies
isolation + the emission-via-index + the grading methodology; user ratifies; **then** the wiring increment.
**★ Cowork follow-up (the unification items before wiring) is CLOSED — §4a (the reuse-vs-retire ledger) and §9
(the per-slice PitchContext builder lifted into the shared engravingbridge view, the decay length-scale made a
setting, the `cofDistance`-vs-emission split recorded, the Viterbi reuse flag), all byte-identical and NOT wired.**

**Spec:** `cowork_layer3_keymode_design.md` (SIGNED 2026-06-22). **Audit (the verified pins):**
`cc_layer3_decoder_audit_dossier.md`. **Delivery plan:** `cowork_layer3_keymode_impl_design.md`. **Grades against:**
the Increment-B held-out harness (`tools/cc_layer3_keymode_baseline.py`, committed `dcbc0bb4e1`).

---

## §0 — Headline

- **The module is built as a new, self-contained unit** — `src/composing/analysis/key/keymodesequence.{h,cpp}`
  (namespace `mu::composing::analysis::keymodeseq`), a **dedicated key-path Viterbi** over `(tonic × mode)` states
  (the audit confirmed `ChordPathDecoder` is chord-specific and not reusable). It is **NOT wired into the live
  pipeline** — exactly as Layers 1 and 2 were built.
- **Production byte-identical (verified):** composing **576→596** (+20 new decoder tests, all pass; RealDiff
  unchanged: Standard 0 / Jazz 3, both pre-existing), notation **57/57**, pipeline snapshots **11/11 with NO golden
  refresh**, and a 5-stem `.ours.json` byte-identity spot check (`bwv245.15`, `bwv144.6`, `bwv10.7`, `bwv227.7`,
  `bwv60.5` — all IDENTICAL). The only production-file edits are an **additive, uncalled** accessor
  (`keyModeSignatureFifths`) and an **isolated diagnostic** that returns before `analyzeScore`.
- **Emission through the Layer-1 INDEXED query (the §6 STOP condition honored):** the per-slice pitch context is
  built from `NoteModel::overlapping` (O(log N + result)), **not** `collectPitchContext` (the DOM walk). Confirmed at
  source (§2).
- **Every cost-driving value is a SETTING** (`KeyModeSequencePreferences`), seeded with the audit's source-true
  magnitudes — the effort-retrofit hygiene requirement (§3).
- **Held-out directional result (TEST split, out-of-sample), decoder vs the current per-region baseline:**
  - **Jazz unambiguous full-match: 61.5% → 78.5% (+17.0 pts; dur-wt +14.6).** A large win.
  - **Baroque unambiguous full-match: 87.3% → 84.3% (−3.0 pts; dur-wt −1.7).** Near-parity with a per-region
    resolver carrying years of Baroque-specific tuning.
  - **Modulation tracking — the design's core thesis — improves on BOTH presets:** on the **ambiguous
    (modulation/tonicization) regions**, the decoder's top-1 match jumps **Baroque 9.9% → 31.2% (+21.3)** and
    **Jazz 18.9% → 30.8% (+11.9)**. The decoder tracks local modulations ~2–3× better.
  - The genuine **rotation/relative-pair** errors **dropped** (the declared-mode hint settles the pair; §4); the
    residual Baroque misses are **fifth-displacement tonicization-boundary** cases (the design handles these by the
    change cost + the "uncertain" flag) and the **modal-GT-limitation** class the design says NOT to optimize away.

---

## §1 — The module as built (`keymodesequence.{h,cpp}`)

**Public shape** (per layer-doc §3 / impl-design §1, with `declaredMode` added — see §4):

```cpp
struct SliceKeyMode { int sliceIndex; KeyModeAnalysisResult chosen;
                      std::vector<KeyModeAnalysisResult> alternatives; double confidence; bool uncertain; };

struct KeyModeSequencePreferences { int topK; double changeBaseCost, changePerFifthStep, relativePairExtraCost,
                                    windowBeats, decayRate, lookaheadWeight, uncertainThreshold; int maxAlternatives; };

class KeyModeSequenceDecoder {
  struct State { int tonicPc; KeySigMode mode; int keySignatureFifths; int ionianPc; };
  static std::vector<SliceKeyMode> decode(slices, noteModel, keySigFifths, declaredMode=nullopt, keyPrefs, seqPrefs);
  static std::vector<SliceKeyMode> redecodeRange(slices, noteModel, keySigFifths, declaredMode, first, last,
                                                 leftPin, rightPin, keyPrefs, seqPrefs);
  // scorer-independent core (for the synthetic behaviour/branch tests):
  static std::vector<SliceKeyMode> decodeLattice(states, emissions, seqPrefs, pinFirstState=-1, pinLastState=-1);
  static double changeCost(const State& a, const State& b, const KeyModeSequencePreferences&);
};
```

**How it works (the four design steps):**
1. **Local-fit scoring (emission).** Per slice, `buildSliceContext` queries `NoteModel::overlapping(start−win,
   end+win)` (the indexed L1 query), weights each eligible note (duration × time-decay-from-the-slice ×
   look-ahead-weight; beat-type weight at onset; bass = lowest pitch sharing that onset), and calls
   `KeyModeAnalyzer::analyzeKeyMode(ctx, keySigFifths, keyPrefs, declaredMode, &dump)` reading **all 252** candidate
   scores via `dumpOut`.
2. **State set = the GLOBAL UNION of per-slice top-K (∪ the incumbent).** Each union state is scored at **every**
   slice from the 252-dump, so the running/incumbent key — top-K where it prevails, hence in the union — always has a
   state even on a transient slice that scores something else higher. This realizes "keep the incumbent alive"
   **deterministically and path-independently** (the union depends only on emissions, never on the decode), which is
   also what makes a pinned sub-range re-decode reproduce the matching slice of a full decode exactly.
3. **Change cost + Viterbi.** `τ(a→b)` = 0 to stay; otherwise `changeBaseCost + changePerFifthStep ×
   cofSteps(ionianPc_a, ionianPc_b) + (relativePairExtraCost if same signature)`. `cofSteps` = the cyclic
   circle-of-fifths distance between the two parent Ionian pitch classes (the minimal key-signature distance, no
   enharmonic resolution needed). A forward max-sum Viterbi with back-pointers + a traceback recovers the connected
   optimal path; linear in slices.
4. **Per-slice outputs.** chosen key/mode; ranked alternatives (the other surviving states, by whole-sequence total);
   **confidence = the sequence margin** = `top1 − top2` of the `(α_t + β_t)` whole-sequence totals (a forward +
   backward read of the Viterbi tables — design §5.4); **uncertain = confidence < uncertainThreshold**.

`redecodeRange` rebuilds the full lattice (same state set + emissions as a full decode, with the two pins forced into
the state set) and re-runs the Viterbi only over `[first,last]` with the endpoints pinned — reproducing the matching
slice of a full decode by sub-path optimality over an identical lattice (the incremental-emission optimization is the
later editor-wiring step, per the audit's R2 interface-shape obligation).

---

## §2 — Emission-via-index confirmation (the §6 STOP condition)

**Confirmed: the emission goes through the indexed `NoteModel::overlapping`, NOT `collectPitchContext` / a raw-score
walk.**

- The per-slice window is built by the **shared engravingbridge view `pitchContextOverSpan`** (§9.1) over
  `NoteModel::overlapping(start − win, end + win)` — the Increment-A indexed query (`note_model.h`: onset-sorted keys
  + a max-release segment tree, O(log N + result)). It never calls `collectPitchContext` (which the audit §2.4
  flagged as a DOM segment walk that bypasses the index). `buildSliceContext` (keymodesequence.cpp) is now a thin
  slice→window mapper that delegates to that view.
- **Beat-type weight without a segment walk:** the view's `beatWeightForOnsetTick` reproduces
  `scoreharvest::safeBeatType(measure, segment)` using only an **indexed measure lookup** (`Score::tick2measure`) +
  the onset's rtick + `TimeSigFrac(num,den).rtick2beatType(rtick)` — no `next1(SegmentType::ChordRest)` walk. So the
  per-slice path is O(log N) and never re-walks the DOM.
- This resolves the audit's `[verify at impl]` item: the NoteModel-built per-slice `PitchContext` reproduces
  `collectPitchContext`'s beat/bass/decay/look-ahead weighting (duration × `timeDecay(distanceFromSlice)` ×
  `lookaheadWeight` for post-slice notes; beat weight via the time signature; isBass = lowest pitch per onset group),
  sourced from the index — the perf form, correctness-equivalent (audit §2.4).

---

## §3 — Settings list (effort-retrofit hygiene — nothing hardcoded)

Every cost-driving value is a field of `KeyModeSequencePreferences`, seeded with the audit's source-true magnitudes:

| setting | default | source |
|---|---|---|
| `topK` | 8 | audit §2.2 ([key_path_design] top-N) |
| `changeBaseCost` | 2.0 | `hysteresisMargin` (audit §1.4/§2.3) |
| `changePerFifthStep` | 0.60 | `keySignatureDistancePenalty` (audit §1.4/§2.3) |
| `relativePairExtraCost` | 2.0 | `relativeKeyHysteresisMargin` (audit §1.4/§2.3) |
| `windowBeats` | 4.0 | audit §2.4 (slice ± ~1 measure) |
| `decayRate` | 0.7 | `DECAY_RATE` |
| `lookaheadWeight` | 0.5 | `LOOKAHEAD_WEIGHT` |
| `beatsPerDecayUnit` | 4.0 | the time-decay length-scale (one 4/4 measure) — formerly the hardcoded `/4.0` (§9.2) |
| `uncertainThreshold` | 1.0 | audit §2.5 (≈ half the base change penalty) |
| `maxAlternatives` | 4 | (output cap; 0 = keep all) |

The preset's **mode prior** enters automatically through the emission (the decoder reuses `analyzeKeyMode(…, keyPrefs,
…)` with the same `KeyModeAnalyzerPreferences` the per-region path uses), so the user style preset keeps applying with
no new wiring (layer-doc §2 / audit §1.3).

---

## §4 — Tests (composing_tests `Composing_DecodeKeyMode.*` — 20, all pass)

**Scorer-independent (synthetic lattice — design §10 "independent of the scorer"):**
- Change cost (3): stay = 0; near < remote (2.60 vs 5.60); relative pair = 4.00 (the same-signature extra).
- Behaviour (5): single-key → one key, confident; relative-pair near-tie → the correct member **consistently** +
  **uncertain** at the seam; brief tonicization → key **unchanged**; sustained modulation → key **changes** (one
  switch); near-vs-remote on equal evidence → the **near** key.
- Confidence / alternatives / pins / determinism / edges (5): single-state confidence sentinel (not uncertain);
  alternatives ranked + capped; endpoint **pins** force the first/last column (the redecode core); determinism;
  empty lattice → no slices.

**Note-model end-to-end (real `decode()` over L1 models from `.mscx` fixtures — 7):**
- `s1c_c_major` → C major on every slice (single key).
- `s1c_seg_changes` (I–V–vi–IV in C) → **one key across the whole progression** (no spurious modulation to the
  dominant on the V chord — a real "brief excursion stays" case on a note model).
- `s1c_a_minor_amb` → a **consistent** single 0-signature reading of the relative pair.
- **`s1c_modulation_cg` (NEW fixture)** → a note-based sustained modulation C major → G major (NOT in the
  signature): the decoder **opens in C, ends in G** (scenario 4 end-to-end).
- declared-mode **threading**: a strong declared hint pulls the reading toward its class and changes the decoded
  sequence (proves the `declaredMode` parameter reaches the emission).
- **redecodeRange == full decode** (R2 property): a sub-range re-decode with both endpoints pinned to a full
  decode's values reproduces the matching slice (chosen key/mode) of that full decode.
- determinism (same model → identical sequence + confidences).

**The `declaredMode` parameter (added during the build — rationale).** The first grading pass (declaredMode = nullopt)
gave Baroque **−11.0** / Jazz **+9.3**; the Baroque regression was dominated by relative-pair flips (Fmaj↔Dmin,
Cmaj↔Amin) because the pure-note emission dropped the weak declared-mode major/minor tiebreaker the per-region
resolver uses. The signed design §2 treats the signature as a **weak hint to use** (not to ignore), and the
production `analyzeKeyMode` is invoked with a declared mode; passing it (`declaredModePenalty` = 1.0, a tiebreaker, not
a wall) is the **faithful, fair** config. With it, Baroque recovered to **−3.0** AND Jazz **improved further to
+17.0** (the chorale corpus is tonal even under the Jazz preset). The diagnostic reads the notated `<mode>` at tick 0
and passes it; the unit tests pass it explicitly where relevant.

**Branch coverage.** Reasoned (every reachable decoder branch is mapped to a test): change-cost stay/near/remote/
relative-pair; Viterbi forward + traceback + backward; pin-first / pin-last; single-state confidence sentinel vs
multi-state margin; uncertain true/false; alternatives capped vs all; empty lattice; buildSliceContext
inside/look-back/look-ahead distance + eligible/ineligible + per-onset bass; buildLattice empty-context-slice skip +
top-K + forceCands; decode + redecodeRange. The defensive guards (null `Score*`, no-measure / bad-timesig fallback to
SUBBEAT, the broken-traceback fallback) are documented and not chased — matching the Layer-1 coverage-report
precedent. **A formal instrumented coverage pass (VS Dynamic Code Coverage, as in Layer 1) is the recommended
Cowork-verification step.**

---

## §4a — Reuse-vs-retire ledger (the TOTAL-UNIFICATION rule)

**Reused (existing code, NOT re-implemented):**
- `KeyModeAnalyzer::analyzeKeyMode` + its `dumpOut` 252-candidate vector — the emission scorer (the cadence-free
  252-candidate key/mode scorer, unchanged).
- `NoteModel::overlapping` — the Layer-1 Increment-A indexed query.
- `changePointSlices` — the Layer-2 slice grid.
- `scoreharvest::timeDecay` (now parameterized, byte-identical) + `scoreharvest::beatTypeToWeight` — the metric-weight
  helpers (one decay function, one beat-weight map).
- `keyModeIndex` / `ionianTonicPcForMode` / `resolveToFifths` — the mode/signature helpers (the last via the new
  `keyModeSignatureFifths` wrapper, a thin accessor over the existing `resolveToFifths`).
- The existing `declaredModePenalty` path — the weak `<mode>` hint (its shared `= 1.0` default is **unchanged**, so the
  byte-identity of every production caller is real).

**Newly written:**
- The `keymodesequence` module: the `State`/lattice, the forward+backward Viterbi, the sequence-margin confidence,
  and `decode` / `redecodeRange` / `decodeLattice` / `changeCost`.
- `cofDistance` — the state↔state circle-of-fifths transition distance (a **distinct domain** from the emission's
  candidate↔notated-signature distance; §9.3).
- The engravingbridge view `pitchContextOverSpan` (+ `SpanWindowWeights`, `beatWeightForOnsetTick`) — the **shared,
  indexed, span-anchored** PitchContext builder (§9.1).
- The `--decode-keymode` diagnostic; the harness `--decode-dir` extension; `tools/decode_keymode_corpus.py`; the
  `keyModeSignatureFifths` wrapper; the `timeDecay` `beatsPerUnit` parameter.

**Slated to retire at the WIRING increment (recorded, carried into the wiring instruction):**
- The per-region `kr::resolveKeyAndModeRanked` argmax @ [`regionanalyzer.cpp:633`](src/composing/analysis/region/regionanalyzer.cpp#L633)
  (the Pass-1 per-region key decision) **and** its hysteresis block — replaced by the per-slice decoder.
- `collectPitchContext` (the legacy DOM-walk, point-anchored PitchContext builder) — replaced by `pitchContextOverSpan`
  once the decoder is the live key path. **End state: one PitchContext builder.**

---

## §5 — Byte-identity confirmation (production unchanged; the decoder is isolated)

| gate | before | after | note |
|---|---|---|---|
| composing_tests | 576 | **596** | +20 new decoder tests; all pass |
| chord mismatch RealDiff | Std 0 / Jazz 3 | **Std 0 / Jazz 3** | unchanged (pre-existing Jazz convention items) |
| notation_tests | 57 | **57** | pass |
| pipeline snapshots | 11/11 | **11/11** | **no golden refresh** |
| `.ours.json` (5-stem spot check) | — | **byte-identical** | bwv245.15/144.6/10.7/227.7/60.5 |

**Why byte-identical by construction:** the only production-file edits are (a) `keyModeSignatureFifths` — a **new,
additive** accessor in `keymodeanalyzer.{h,cpp}` that **no production scoring path calls** (it wraps the existing
internal `resolveToFifths`; used only by the decoder for labels); and (b) the `--decode-keymode` **diagnostic** in
`batch_analyze.cpp`, which (like `--validate-slices`) **returns before `analyzeScore`** so the analysis pipeline is
never invoked. `keymodesequence.{h,cpp}` is a new module **not wired into the analyzer**. BIR/oracle are a corpus
aggregate of the per-score production output the snapshots pin per-score → unchanged.

---

## §6 — Held-out directional grading (decoder vs the per-region baseline)

Method: `batch_analyze --decode-keymode --preset <P>` over the 353 canonical stems (driver
`tools/decode_keymode_corpus.py`), graded by the extended Increment-B harness
(`cc_layer3_keymode_baseline.py --decode-dir`) — the **same** direct (tonic, mode) == WiR-local-GT metric, the
**same** two-source unambiguous split (DCML-parser ∧ music21 romanText), the **same** deterministic held-out split
(`md5(stem)%100 < 20 = test`). The decoder JSON is emitted in the same region shape, so `cmp.load_analysis` +
`align_dcml_regions` grade it unchanged. **Directional, not a fixed bar** (impl-design §4); metrics provisional until
the full pipeline is rebuilt.

**TEST split (out-of-sample) — UNAMBIGUOUS (stable) full (tonic+mode) match:**

| preset | per-region baseline | decoder (Layer 3) | Δ | Δ dur-wt |
|---|---|---|---|---|
| Baroque | 87.3% (1136/1301) | **84.3% (2933/3478)** | **−3.0** | −1.7 |
| Jazz | 61.5% (766/1245) | **78.5% (2731/3478)** | **+17.0** | +14.6 |

**TEST split — AMBIGUOUS (modulation/tonicization) top-1 match (the modulation-tracking metric):**

| preset | per-region baseline | decoder (Layer 3) | Δ |
|---|---|---|---|
| Baroque | 9.9% (100/1010) | **31.2% (863/2762)** | **+21.3** |
| Jazz | 18.9% (185/977) | **30.8% (852/2762)** | **+11.9** |

(The decoder is per-slice, the baseline per-region, so the scorable counts differ ≈2.7×; the **duration-weighted**
full-match is the granularity-robust comparison — Baroque −1.7, Jazz +14.6 — and the AMBIGUOUS top-1 is a like-kind
percentage.)

**Reading the result (the learning):**
- The decoder's **core thesis is validated**: deciding the whole sequence at once tracks **local modulations** far
  better than the per-region argmax (+21.3 / +11.9 top-1 on the ambiguous regions), on **both** presets.
- **Jazz** improves across the board (+17.0 unambiguous): the sequence coherence + the weak declared-mode hint fix
  rotations the per-region resolver's hysteresis missed.
- **Baroque** is near-parity on **stable** regions (−3.0 / −1.7 dur-wt) — the per-region resolver's heavily
  Baroque-tuned hysteresis + dynamic look-ahead + partial-signature correction still edge out where there is **no**
  modulation. The decoder reaches near-parity there with a **simpler, principled** mechanism (Viterbi + change cost),
  while winning decisively on the modulation regions.

**Modal-vs-major/minor-GT caveat (restated, mandatory).** The residual decoder misses on the UNAMBIGUOUS bucket are
now **fifth-displacements**, not relative-pair flips: Baroque `Gmaj→Dmaj` 101, `Amin→Dmin` 96, `Gmin→Emin` 47,
`Dmin→Gmin` 30; Jazz `Gmaj→Dmaj` 75, `Dmin→Amin` 46, `Amin→Dmin` 46, `Cmin→Gmin` 46. These are the
**tonicization-boundary** class the design handles by the change cost (a brief tonicization to the dominant the
decoder, by design, does not switch to is a **defensible** reading) and, on the Jazz preset especially, the
**defensible modal** perfect-fifth readings the major/minor GT cannot represent. **These are NOT defects to optimize
away** (impl-design §4). The recurring `Gmaj→Abmaj` (~68 both presets) is a GT-parser enharmonic/specific-stem item
worth a separate look, not a decoder rotation defect.

**Held-out ≈ in-sample** (the TRAIN-split numbers track the TEST split within ~1 pt — no memorization).

**Safety net.** Production BIR/oracle are **unchanged** (the decoder is isolated; §5). When the decoder is **wired**
(the next increment), the §3 safety net — oracle-root KEY tier + dual-preset BIR no-regression + the snapshot
goldens — becomes live; this increment does not touch them.

---

## §7 — Deliverables + what is committed vs held

**Committed locally (unpushed), this increment:**
- `src/composing/analysis/key/keymodesequence.{h,cpp}` — the module (`buildSliceContext` now a thin wrapper, §9.1).
- `src/composing/analysis/key/keymodeanalyzer.{h,cpp}` — the additive `keyModeSignatureFifths` accessor only.
- `src/composing/analysis/engravingbridge/{regiontonecollector.h,regiontoneprimitives.cpp}` — the shared
  `pitchContextOverSpan` view (§9.1) **added**; `collectPitchContext` untouched (byte-identical).
- `src/composing/analysis/scoreharvest/metricweights.{h,cpp}` — the byte-identical `timeDecay` `beatsPerUnit`
  parameter (§9.2).
- `src/composing/analysis/CMakeLists.txt` — module wiring.
- `src/composing/tests/decode_keymode_tests.cpp` (+ `CMakeLists.txt`) — the 20 tests.
- `src/composing/tests/data/s1c_modulation_cg.{musicxml,mscx}` — the new sustained-modulation fixture.
- `tools/batch_analyze.cpp` — **only** the `--decode-keymode` diagnostic hunks (the held **B2** subdominant-guard
  hunks in `writeModulationJson` were reverted out before staging and restored after, so the commit carries no B2).
- `tools/cc_layer3_keymode_baseline.py` — the `--decode-dir` decoder-grading extension.
- `tools/decode_keymode_corpus.py` — the decoder corpus driver.

**Held / UNSTAGED (untouched):** the B2 trio (`section/localmodulationdetector.{cpp,h}` + the `batch_analyze.cpp`
B2 hunks), the WIP doc set (ARCHITECTURE.md, STATUS.md, BUILD_AND_TEST.md, CLAUDE.md, COWORK_HANDOFF.md, `docs/*`),
the pre-existing `tools/compare_rn.py` M, and the `cowork_*`/`cc_*` design+report set (the latter gitignored). The
decode corpus (`tools/corpus_decode/`) and this report (`cc_*.md`) are gitignored.

**`upstream` (`musescore/MuseScore`) is NOT targeted** (the CLAUDE.md fork-local-only constraint is unaffected — no
`muse` submodule or #9444 content is involved here).

## §8 — Stop conditions (instruction §6) — status: none breached
- The decoder is **NOT wired** into the live pipeline; production output is **byte-identical** (§5). ✓
- The emission goes through the **indexed `NoteModel::overlapping`**, not `collectPitchContext` / a raw-score walk
  (§2). ✓
- **No cost-driving value is hardcoded** — all are settings on `KeyModeSequencePreferences` (§3). ✓
- The decoder needs **no** chord/function/cadence evidence and **no** gated joint step — the ambiguous residual is
  flagged "uncertain" (the `uncertain` mark + the AMBIGUOUS bucket), left for the later gated step. ✓

**Next (after Cowork verification + user ratification):** the **wiring** increment — replace the per-region
`resolveKeyAndModeRanked` argmax at the `regionanalyzer.cpp` seam with the per-slice decoder, graded against this
harness's held-out metric + the oracle KEY tier + dual-preset BIR (no byte-identity), snapshots refreshed only after
verified correct.

---

## §9 — Unification follow-up (Cowork items closed; byte-identical, NOT wired)

All four items closed without touching correctness. **Production output is unchanged — re-verified after the
extraction:** composing **596**, notation **57**, snapshots **11/11 (no golden refresh)**, `.ours.json` byte-identical
(`bwv10.7`, `bwv245.15` — the `timeDecay` production touch is byte-identical). **The decoder's own output is unchanged
by the refactor** (a pure relocation): `--decode-keymode` on `bwv10.7` (68 slices) and `bwv245.15` (80 slices) is
**byte-identical region-for-region** pre/post extraction.

### §9.1 — `buildSliceContext` → the shared engravingbridge view `pitchContextOverSpan` (§2: extracted now)
The per-note PitchContext assembly (duration × time-decay × look-ahead × beat-weight; lowest-pitch-per-onset bass) is
now **one** function: `engravingbridge::pitchContextOverSpan` — a **note-model-derived view beside
`weightedPcView` / `soundingAt`** (the proper L1-adjacent layer), built over the indexed `NoteModel::overlapping`.
`buildSliceContext` in the decoder is now a **thin slice→window mapper** (computes the ± window + fills
`SpanWindowWeights` from `seqPrefs`, then delegates). The view is **general** — it takes an `excludeStaves` set and an
arbitrary anchor span — so it can also back `collectPitchContext`'s caller at wiring. `collectPitchContext` itself is
**untouched and byte-identical** (still the live resolver's builder); it is **marked for retirement at wiring** (§4a),
when the decoder becomes the live key path and the end state is one builder. (Re-expressing `collectPitchContext` on
the view *now* would change its note set from onset-in-window to overlap-in-window — a production change — so it is
correctly deferred to wiring, not done here.)

### §9.2 — Decay length-scale → a setting; one decay function (§3)
The hardcoded `distBeats / 4.0` is gone. The shared `scoreharvest::timeDecay` now takes a third **defaulted**
`beatsPerUnit = 4.0` parameter (every existing caller — only `collectPitchContext` — is byte-identical); the view
calls `timeDecay(distBeats, decayRate, beatsPerDecayUnit)` and the decoder passes
`KeyModeSequencePreferences::beatsPerDecayUnit = 4.0`. One decay function, the length-scale a setting.

### §9.3 — `cofDistance` vs the emission's distance: NOT shared (recorded decision — different domains)
They compute the circle-of-fifths distance in **two genuinely different domains**, so a shared helper is **wrong**:
- **Emission** (`scoreKeySignatureProximity`): candidate-signature ↔ **NOTATED** signature, anchored to the **exact**
  notated `keySignatureFifths` int. It respells **only the candidate** (`possibleIonianFifthsForPc` → nearest to the
  notated int), so e.g. **C against a 7-sharp notated signature is distance 7**.
- **Decoder** (`cofDistance`): **state ↔ state**, with **no** notated anchor — the minimal cyclic circle-of-fifths
  distance, respelling **both** pcs, so the **same pair is 5** (treating C# as Db = −5).

They differ precisely at enharmonic extremes (a fixed un-respelled reference vs two free pcs). Forcing them through
one helper would change the emission's output there — a **production scoring change**, forbidden this increment. So
they are **intentionally separate** (recorded, not accidental).

### §9.4 — Viterbi reuse flag (for the future Layer-4/5 sequence decoders)
`decodeLattice` is already **scorer-independent** (the emission is injected as `vector<vector<double>>`). It is **not
yet generic** over the state type or the transition cost — the `State` is key-specific (tonic/mode/signature/ionianPc)
and `changeCost` is the key-distance formula. Generalizing it for Layer-4 (chord) / Layer-5 (function) sequence
decoders = **templating the `State` + taking a transition-cost functor** (the emission seam already generalizes).
This is a clean refactor to do **when those layers are built** — full genericity is not required now; the reuse path
is **flagged here** so they reuse the Viterbi rather than re-implement it.

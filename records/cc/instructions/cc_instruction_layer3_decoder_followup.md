# CC Follow-up — Layer 3 decoder (746e3d524f): close the unification items before wiring

> Cowork verified the build at source: **isolation holds** (`--decode-keymode` returns 0 before
> `analyzeScore`/`analyzeRegions`; production byte-identical), **emission is through the index**
> (`NoteModel::overlapping` + `tick2measure`, no `collectPitchContext`), **cost knobs are settings**
> (`KeyModeSequencePreferences`), and the **`<mode>` weak hint sits correctly in L3** (a `declaredMode`
> parameter read from the notated signature, riding the pre-existing `declaredModePenalty = 1.0` — you did
> NOT change that shared default, so byte-identity is real). The graded results are accepted in principle.
>
> Before the **wiring** increment, close the unification items below. None touch correctness — this is the
> standing TOTAL-UNIFICATION rule (one path per concern; no permanent duplicate). Do **not** wire anything.

## 1 — Add the §4a reuse-vs-retire declaration to the build report (REQUIRED — it is missing)
`cc_layer3_decoder_build_report.md` must contain the explicit ledger §4a mandated. Add a section listing:
- **Reused (existing code, not re-implemented):** `KeyModeAnalyzer::analyzeKeyMode` + its `dumpOut`
  252-candidate vector; `NoteModel::overlapping` (Layer-1 index); the Layer-2 `changePointSlices`;
  `scoreharvest::beatTypeToWeight` + the time-decay map; `keyModeIndex` / `ionianTonicPcForMode` /
  `resolveToFifths` (via the new `keyModeSignatureFifths` wrapper); the existing `declaredModePenalty` path.
- **Newly written:** the `keymodesequence` module (states, lattice, Viterbi, confidence), `buildSliceContext`,
  `cofDistance`, the `--decode-keymode` diagnostic, the harness extension, the `keyModeSignatureFifths` wrapper.
- **Slated to retire at wiring:** the per-region `resolveKeyAndModeRanked` @ `regionanalyzer.cpp:633` and its
  hysteresis; **`collectPitchContext`** (the score-walk PitchContext builder) once the decoder is the live key path.

## 2 — `buildSliceContext`: it is a bespoke private builder, not the shared primitive §4a required
§4a was explicit: build the per-slice window as a single reusable **"pitch context over a span, from the note
model"** primitive — **a derived view alongside `weightedPcView` / `soundingAt`** — not a window-builder private
to the decoder. As built, `buildSliceContext` is a static function in the decoder's anon namespace that
re-implements `collectPitchContext`'s per-note assembly (duration × time-decay × look-ahead × beat-weight, plus
lowest-pitch-per-onset bass). So there are now **two `vector<PitchContext>` builders** — `collectPitchContext`
(DOM) and `buildSliceContext` (index).

**Architectural placement (do this in the PROPER layer):** the shared builder belongs as an **engravingbridge
derived view (L1-adjacent)**, beside `weightedPcView` / `soundingAt` — a note-model-derived view — that L3
consumes. It must NOT live inside the L3 decoder.

Pick one and record it in the report:
- **(Preferred) Extract now:** lift the per-note PitchContext assembly into one engravingbridge derived view
  (over `NoteModel::overlapping`), have `buildSliceContext` call it, and re-express `collectPitchContext` on top of
  the same view (or mark it for retirement at wiring). One assembly, two thin callers.
- **(Acceptable, if extraction is risky now) Defer with a binding plan:** keep `buildSliceContext` as-is for this
  isolated increment, but state in the report **and** carry into the wiring instruction that wiring (a) promotes the
  builder to the shared derived view and (b) **retires `collectPitchContext`**. The end state must be one builder.

Either way: do not leave two permanent PitchContext builders.

## 3 — Minor unification / hygiene (fold in, or justify in the report)
- **`cofDistance` vs the emission's distance.** `scoreKeySignatureProximity` already computes a circle-of-fifths
  distance (via `possibleIonianFifthsForPc`). If a single named `circleOfFifthsDistance` helper can serve both,
  share it; if not (different domains — state↔state transition vs candidate↔notated-signature), say so explicitly
  in the report so it is a recorded decision, not an accident.
- **Viterbi reuse flag.** Good that `decodeLattice` is a scorer-independent core. State explicitly in the report
  whether/how it generalizes (state type + a transition-cost functor) for the Layer-4/5 sequence decoders, so they
  reuse it rather than re-implement. Full genericity not required now; the flag is.
- **Hardcoded decay length-scale.** `distBeats / 4.0` in `buildSliceContext` is a hardcoded magic number (the
  beats-per-decay-unit). Move it onto `KeyModeSequencePreferences` (e.g. `beatsPerDecayUnit = 4.0`) for
  effort-retrofit hygiene, or note why it stays fixed.

## 4 — Scope
- This stays the **isolated** increment. **Do not wire.** Wiring (replace the @633 argmax, retire the old resolver
  + `collectPitchContext`) is the next, separately-ratified increment.
- No production output may move. If anything in §2's extraction would touch a production scoring path, STOP and
  surface it — the extraction must be byte-identical too.
- Update `cc_layer3_decoder_build_report.md` in place; re-commit locally (unpushed). Leave held WIP unstaged.

## 5 — Cowork's parallel doc-sync (FYI, not your task)
Once these are settled, Cowork updates the signed L3 layer doc §3 (implementation files: `keymodesequence.{h,cpp}`)
and §10 (regression tests: `decode_keymode_tests.cpp` + the `--decode-keymode` corpus driver), and folds in the
dual **accuracy-on-the-resolvable-subset + calibration-of-`uncertain`** quality goal. That keeps the
all-docs-in-sync rule satisfied as the source stabilizes.

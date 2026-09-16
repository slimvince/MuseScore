# CC Instruction — ARCHITECTURAL LAYER 3 (key/mode) decoder: BUILD (isolated + graded; production byte-identical)

> Architectural Layer 3 (key/mode) is signed (`cowork_layer3_keymode_design.md`) and the decoder pre-build audit is
> done and Cowork-verified (`cc_layer3_decoder_audit_dossier.md`, HELD). **Build the key/mode sequence decoder as a
> new, self-contained module, grade it against the held-out ground-truth harness, but do NOT wire it into the live
> analysis pipeline yet** — exactly as Layers 1 and 2 were built (isolated → validated → wired later). So **production
> analysis output stays byte-identical**; the decoder runs only under a read-only diagnostic. The wiring (replacing
> the per-region key decision) is the **next** increment, separately ratified.
>
> **★ Read first:** the signed layer doc (the spec) and the audit dossier (the verified call-site, numbers, and the
> performance caveat). **No-assume:** anything not confirmable at source → STOP/surface, do not guess.

## §1 — The module
New module `src/composing/analysis/key/keymodesequence.{h,cpp}` (a dedicated decoder — `ChordPathDecoder` is
chord-specific and not reusable, per the audit). Public shape per the layer doc §3:
`SliceKeyMode { int sliceIndex; KeyModeAnalysisResult chosen; std::vector<KeyModeAnalysisResult> alternatives;
double confidence; bool uncertain; }`; `decode(slices, noteModel, keySigFifths, prefs) → vector<SliceKeyMode>`; and
the `redecodeRange(…, first, last, leftPin, rightPin)` signature (the sub-range interface — implement it; the full
editor-incremental wiring is later).

## §2 — How it works (per the signed layer doc §5)
1. **Local-fit scoring (emission) — through the INDEXED note model.** For each slice, build a small pitch-context
   window (slice ± ~4 beats) **from `NoteModel::overlapping` (the Layer-1 indexed query)** and score every candidate
   key/mode with the existing `KeyModeAnalyzer`, reading all **252** candidate scores via its `dumpOut` accessor.
   **Do NOT use `collectPitchContext`** — the audit confirmed it walks the raw score and bypasses the index, which
   would re-introduce the O(N²) cost the indexing removed. Prune to the **top-K (K=8) ∪ the running incumbent
   key/mode** (keep the incumbent even when a transient slice scores it lower).
2. **Change cost.** Stay = 0; switch = **base 2.0 + 0.60 × (circle-of-fifths steps) + 2.0 if the pair is relative
   major/minor** — the source-true magnitudes the audit read (`hysteresisMargin` 2.0, `keySignatureDistancePenalty`
   0.60, `relativeKeyHysteresisMargin` 2.0), in emission-score units. (Ignore the stale `docs/key_path_design.md`
   λ≈0.3.)
3. **Best sequence — a dedicated Viterbi** over the pruned lattice (forward pass + back-pointers), linear in slices.
4. **Outputs.** Per slice: chosen key/mode; ranked alternatives (the other surviving candidates); **confidence =
   the sequence margin** (best total vs the best total forced through a different key at that slice — a
   forward+backward read of the Viterbi tables); **uncertain = confidence < 1.0** (starting threshold).

**★ Effort-retrofit hygiene (mandatory):** K, the three change-cost magnitudes, the window size, and the uncertain
threshold are **settings on a preferences struct (`KeyModeSequencePreferences`), never hardcoded constants** —
seeded with the values above. (This keeps the future "effort" preset a clean retrofit.)

## §3 — Grade it against the held-out ground truth (read-only diagnostic)
Add a **read-only diagnostic** that runs the decoder over the corpus and emits its per-slice key/mode, then grade it
with the Increment-B harness:
- A `batch_analyze --decode-keymode` flag (default OFF, mirrors `--validate-slices`): per score, build the note
  model, slice (Layer 2), run the decoder, and emit the decoder's key/mode per position (align slices to the
  ground-truth positions using the harness's existing time-overlap aligner). Production path untouched (returns
  before `analyzeScore`).
- Extend `tools/cc_layer3_keymode_baseline.py` to grade the **decoder's** key/mode (not the current resolver's)
  against the RN ground truth on the **held-out test split**, per preset — the same direct metric.

## §4 — Gate (this increment: isolated, graded, byte-identical)
- **Production byte-identical:** the decoder is NOT wired into the live analyzer; `composing`/`notation`/snapshot
  tests and BIR/oracle are **unchanged** (the decoder runs only under the diagnostic). If any production metric
  moves → STOP (it got wired in by accident).
- **Behavioural unit tests** (synthetic emission/change-cost, independent of the scorer): single-key → one key;
  relative-pair near-tie with a whole-stretch tilt → the correct one consistently, low confidence at the seam;
  brief tonicization → key unchanged; sustained modulation → key changes; near vs remote with equal local evidence
  → the near key.
- **Property/fixture tests:** the 6 behaviour fixtures over the note model; `redecodeRange` with correct pins ==
  the matching slice of a full `decode`; determinism (same input → same output). **Full branch coverage** of the
  decoder.
- **Directional grading (the learning, not a pass/fail bar):** report the held-out direct metric for the decoder
  vs the current per-region baseline (≈87% Baroque / ≈61% Jazz), per preset — the genuine **rotation/relative-pair
  and modulation errors should drop**. **Do NOT optimise away** the modal "misses" the major/minor ground truth
  cannot represent (the modal-GT caveat). Report the move; this increment is graded by direction + the tests, not by
  reaching a fixed number.

## §4a — Unification (do NOT create PERMANENT duplicate paths)
The project objective is total unification — one path per concern. This isolated build creates **temporary**
coexistence (the old resolver still runs production; the decoder runs only in the diagnostic) — that is fine, like
the slicer's transition. It must NOT create **permanent** duplication:
- **One pitch-context builder.** Build the per-slice scoring window as a single, reusable "build the pitch context
  over a span, from the note model" primitive — a derived view alongside `weightedPcView`/`soundingAt` — **not** a
  bespoke window-builder inside the decoder. This becomes THE pitch-context builder; the old `collectPitchContext`
  (score-walk) is slated to **retire when the decoder is wired in**. Do not leave two pitch-context builders
  permanently.
- **One best-sequence (Viterbi) mechanism.** Write the Viterbi so it CAN be reused for later chord/function
  sequences (parameterized by emission + transition), not a key-only one-off that Architectural Layer 4/5 would
  duplicate. (Full genericity is not required now, but do not preclude reuse, and flag it for L4/L5.)
- **No duplicate helpers.** If circle-of-fifths key-distance (or any other helper) already exists in the codebase,
  reuse it — do not write a second copy.
- **Retirement is the wiring increment's job.** The later wiring increment **replaces and retires** the per-region
  key decision (`resolveKeyAndModeRanked` @633 and its hysteresis), it does not add the decoder alongside.
**In the build report, list exactly which existing code is reused vs newly written, and what is slated to retire at
wiring** — so Cowork can confirm no permanent duplication.

## §5 — Workflow + deliver
Commit **locally (unpushed)**: the `keymodesequence.{h,cpp}` module + its tests + the `--decode-keymode` diagnostic
+ the harness extension + the 6 fixtures. Leave all held WIP unstaged. Write `cc_layer3_decoder_build_report.md`:
the module as built, the emission-via-index confirmation, the settings (not hardcoded) list, the unit/property/
coverage results, the byte-identity confirmation, and the held-out directional numbers (decoder vs baseline, per
preset, with the modal caveat). Cowork verifies isolation + the emission-via-index + the grading methodology; user
ratifies; **then** the wiring increment.

## §6 — Stop conditions
- The decoder gets **wired into the live analysis pipeline**, or any production analysis output moves → STOP (this
  increment is isolated; wiring is the next, separately-ratified increment).
- The emission ends up going through `collectPitchContext` / a raw-score walk instead of the indexed
  `NoteModel::overlapping` → STOP (re-introduces O(N²)).
- Any cost-driving value is hardcoded rather than a setting → fix before proceeding (effort-retrofit hygiene).
- The decoder needs chord/function/cadence evidence, or the gated joint step, to work → STOP (out of scope; the
  ambiguous residual stays flagged "uncertain").

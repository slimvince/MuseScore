# CC — Layer-3 (key/mode) Certification Audit, PASS 1 (blind enumerative) — EG-7 / OI-84

> **Read-only fact-finding.** No production behavior change; no constant tuned; no golden
> refreshed; `tools/robust_stop/` and `tools/corpus/` reference artifacts untouched. This is the
> FIRST of two passes; **certification is NOT granted here** (it needs pass 2 — the signature
> sweep — plus the P6 error-rate establishment). Protocol: `cowork_audit_protocol.md` (P1–P8).
> Instrument: `tools/audit/gen_inventory.py --layer l3`. Dispositions:
> `tools/audit/l3/gen_l3_dispositions.py`. Corpus pin: `c50002fee1`. Inventory HEAD:
> `9e294f398d`.

## 0. Blinding log (protocol P8, first run) — when each withheld file was first opened

Pass 1 enumerated with the known-problem catalog and prior findings withheld (DT-20 strengthening).

| Withheld file | First opened |
|---|---|
| `OPEN_ITEMS.md` | Task 5 (after the Task-4 freeze commit) — the mandatory session-start read was deferred, declared in the instruction preamble; Cowork did the session-start register check for this dispatch |
| `DEFECT_TYPES.md` | Task 5 |
| `STATUS.md` | Task 5 |
| `cowork_handoff.md` | Task 5 |
| `cowork_siloed_facts_audit.md`, `cowork_adjudication_dossier.md` | not opened this pass |
| every `cc_*_report.md` | not opened this pass |

**Safe reads used this pass:** `CLAUDE.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`,
`ARCHITECTURE.md`, `docs/implementation_roadmap.md`, the source under `src/composing/`, the L3
inventory instrument + tables under `tools/audit/`, `tools/param_manifest.json` (a generated
artifact, not a findings file). No `*dispositions*`/`*blind*`/`*errorrate*`/`*compare*`/`sweep_results*`
file under `tools/audit/` was opened.

## 1. The machine inventory (protocol P1) — sizes + manifest

The one pass-1 inventory instrument was **layer-selected** (`--layer l3`), not duplicated (one path
per concern). It refines the base `L3+` tags on the key/mode files into `L3` / `L3-MIXED` and
corrected 3 mis-tags to `L4` (§8). L1/L2 output proven substance-identical (only `note_model.h` line
numbers drift — a pre-existing source change, not this audit's).

- **Deep-audited files: 22** — 15 tagged `L3`, 7 tagged `L3-MIXED`.
- **Rows: 1943** — 77 functions, 12 decls, 957 numeric literals (trivial 0/1 excluded), 301 fields,
  502 branches, 94 cross-layer includes.
- Manifest `tools/audit/l3/manifest.json`: HEAD `9e294f398d`, script blob `09ef75a9…`, corpus
  `c50002fee1`, row counts as above. Establish-the-instrument (#19): `--self-check` prints per-file
  extraction counts; the extractor is heuristic and **over-capture-biased** (a false extra row gets a
  "no issue" disposition; a missed row is the real risk), stated in the module docstring.

**Layer scope (verified at the code, not inherited):**
- **Core L3 (whole file):** `key/keymodesequence.{h,cpp}` (the survivor decoder, LIVE),
  `key/keymodeanalyzer.{h,cpp}` (emission scorer), `key/keyresolver.{h,cpp}` (windowed resolver, R5),
  `key/keymodeformatting.cpp`, `key/modepriorpresets.{h,cpp}`; the section key-evidence detectors
  `section/cadencekeyanchor.{h,cpp}` (R3 diagnostic), `section/localmodulationdetector.{h,cpp}`
  (4d-i diagnostic), `section/jointkeydecision.{h,cpp}` (J-key-iii, gated OFF).
- **Mixed (L3 part in scope, split recorded):** `region/regionanalyzer.{h,cpp}` (the L3 decode seam +
  reach-back + `localKeyForRegion` + `applyJointKeyWiring`, alongside the L4 chord orchestration and
  the L2-legacy `greedyExpand` call), `region/harmonicrhythm.h` (the region DTO carrying L3's
  published key facts), `section/sectionanalyzer.{h,cpp}` (L3 key/mode stabilization + KeyArea
  grouping, alongside the L5 gap/cadence labeling), `section/sectioncadencedetection.cpp` (L5
  cadence/pivot labeling + the one L3 confidence gate), `types/analysistypes.h` (the shared leaf
  holding the L3 `KeyModeAnalyzerPreferences`/`PitchContext`/`KeySigMode` alongside L4 types).

## 2. Dispositions (protocol P2) — every row has a verdict

`tools/audit/l3/pass1_dispositions.{csv,json}` (reproducible via `gen_l3_dispositions.py`). Closed
rubric; "no issue" is a recorded claim with a stated reason. Counts by verdict:

| Verdict | Rows | Meaning |
|---|---|---|
| ESTABLISHED | 556 | FACT/structural constant (music-theory table, pc arithmetic, cardinality, sentinel) |
| UNFIT | 387 | hand-set / empirical tunable (the L3 emission constants + detector weights) |
| NO-ISSUE | 657 | ordinary control-flow branch / plumbing struct member (recorded claim) |
| SURVIVES | 78 | L3 code on the survivor/diagnostic path |
| RETIRES | 1 | `resolveKeyAndModeRanked` (R5-shrink; see §7) |
| PUBLISHED | 30 | L3 derived fact published on the layer's output surface |
| DEFERRED | 140 | L4/L5/L2 part of a mixed file — deferred to the owning layer's audit (split recorded) |
| FORWARD-OK | 76 | cross-layer include respecting the Dependency Rule |
| MIXED-DEFERRED | 11 | L4/L5 include in a mixed orchestrator (its non-L3 part) |
| BACK-EDGE-NOTE | 5 | L3 → `chord/analysisutils.h` for pitch primitives (layering smell — OI-93) |
| BACK-EDGE | 2 | L3 header → heavy `chord/chordanalyzer.h` for an enum in the leaf (OI-93) |

**Zero DEAD constants and zero SILOED/TRAPPED facts were found among the L3-in-scope rows.** No
unpublished derived fact was found trapped: the two currently-unconsumed L3 facts (`keyConfidence`
margin, `keyAlternatives` menu) are **declared dormancy** with their future consumer named (L5), which
the fact-publication corollary permits.

## 3. Contract-direction check (protocol P3) — L3's upward deliverables

From `ARCHITECTURE.md` §"Layer 3" + the roadmap, L3 must deliver per-region key/mode, ranked
alternatives, a boundary confidence, an uncertain flag, KeyArea spans, the signature context, and
passing-vs-real modulation handling. Located in the code:

| Expected deliverable | Status |
|---|---|
| chosen key/mode per region | ✅ `decode()` → `SliceKeyMode.chosen` → `HarmonicRegion.keyModeResult` (duration-majority over the slice run, `localKeyForRegion`) |
| ranked key alternatives | ✅ `SliceKeyMode.alternatives` → `HarmonicRegion.keyAlternatives` (declared dormancy → L5) |
| boundary confidence | ✅ `SliceKeyMode.confidence` (sequence margin) → `HarmonicRegion.keyConfidence` (D-L3a) — **but unconsumed in production (OI-75)** |
| "uncertain" flag | ✅ `SliceKeyMode.uncertain` (drives the dormant reach-back trigger) |
| KeyArea spans | ✅ `analyzeSection` → `out.keyAreas` (confidence-gated) — gate reads the emission sigmoid, not the margin (OI-75) |
| signature context (fifths + declared mode + partial-sig correction) | ✅ shared `resolveKeySignatureContext` |
| declared mode as a weak hint | ✅ `declaredModePenalty = 1.0` (demoted from a wall) |
| passing-vs-real modulation | ✅ via the decoder change cost; the confirmed-modulation-span machinery (`localmodulationdetector`, `jointkeydecision`) is DORMANT by design |
| enharmonic key handling | ✅ `resolveToFifths` / `keyModeSignatureFifths` pick the spelling nearest the reference |
| mid-piece notated key-signature CHANGE | ⚠ **documented deferral** — single-signature anchor at startTick; a notated key change is tracked only via the note-driven change cost (OI-94) |
| A-3 dominant-implication key evidence (roadmap A-3 / L3 §15) | ⚠ **named-future, not built** (OI-94) |

## 4. Behavioral characterization (protocol P4) — fire rates on the pinned corpus

Live decoder measured via the existing default-OFF `batch_analyze --decode-keymode` diagnostic over
all Baroque corpus stems (`tools/corpus/*.xml`, `c50002fee1`); read-only, production byte-identical.
Dormant mechanisms' production fire-rate is derived from the code+wiring, not run.

Measured 352/352 stems (`tools/audit/l3/firerate.json`); 29,080 slices.

| L3 mechanism | Fire rate (Baroque corpus, 352 stems) | Notes |
|---|---|---|
| `KeyModeSequenceDecoder::decode` (the live path) | 352/352 stems; 29,080 slices | one whole-score Viterbi per piece — fires on every piece |
| slice "uncertain" flag | 3,324 of 29,080 slices (**11.43%**) | low-margin flag; feeds the dormant reach-back trigger |
| region key CHANGE (decode commits a switch) | 1,146 of 29,080 (**3.94%**) | the whole-sequence change cost taken (matches the documented smoothing intent — most slices STAY) |
| pieces that modulate (>1 distinct key) | 275 of 352 (**78%**) | |
| `partialSignatureCorrection` (Baroque) | **not measurable via `--decode-keymode`** (instrument-establishment catch, #19) | the dump surfaces the NOTATED signature, not the corrected one (verified on Corelli op01n08d: keySigFifths = −2 with AND without `--ignore-declared-mode`). Its target population is Corelli-class partial/Dorian signatures, absent from the Bach-chorale corpus, so its fire-rate here is ~0 by construction; a proper measurement needs a diagnostic exposing `correctedFifths` or a counter — flagged, deferred |
| reach-back loop (`analyzeRegions`, `ReachBackOptions.enabled`) | **0 (production)** | default OFF; whole-score build has nothing earlier to reach — `extend()` clamps on the first request (derived from code) |
| `applyJointKeyWiring` / `decideJointKey` | **0 (production)** | `jointKeyWiringEnabled()` default OFF (env `MUSE_JOINT_KEY_WIRING`); diagnostic-only (`--dump-joint-key`) |
| `detectLocalModulations` (`localmodulationdetector`) | **0 (production)** | diagnostic-only (`--dump-modulation`); byte-identical (4d-i) |
| `detectAuthenticCadences` / `aggregateGlobalAnchor` (`cadencekeyanchor`) | **0 (production)** | diagnostic-only (`--dump-cadence-anchor`); R3 |
| `redecodeRange` | **0 (production)** | test-only scaffolding (R2, incremental-editor step); declared dormancy |
| resolver hysteresis / `promoteWinnerInPlace` | not aggregated | production region path uses the decoder, not the resolver; the resolver serves the S2 seed + P4 tick-local + the (dormant) joint-key re-resolve — a bounded fire surface, not aggregated this pass |
| emission-internal terms (family-selection tonal-center override, pairwise disambiguation) | not aggregated | derivable from `--dump-key-candidates` (disambiguationDelta ≠ 0 / tonal-center vs raw winner) WITHOUT new instrumentation; per-tick, not aggregated this pass — flagged, not silently skipped |

**Reading:** the decoder is live and fires on every piece; its "uncertain" rate and key-change rate
characterize how often the whole-sequence smoothing is at its margin. Every confirmed-modulation and
joint-key mechanism is **dormant on production by construction** — the correct state for the build
phase (no inference-problem-driven code engaged).

## 5. FINDINGS (blind pass) — plain language, most-load-bearing first

Each is a fact recorded for Cowork; nothing is fixed this session (guiding principle 8). Register rows
opened in the report's commit (§ below, at unblind).

- **OI-91 (medium) — the L3 key/mode scoring constants are not in the Stage-5 parameter manifest.**
  The ~60 `KeyModeAnalyzerPreferences` weights (in `types/analysistypes.h`), the 21×5 `ModePriorPreset`
  mode priors, the `KeyModeSequencePreferences` change-cost/window settings, and the
  cadence-anchor / local-modulation / joint-key weights are all commented "[empirical — Stage-5 fits]",
  yet `tools/param_manifest.json` (the Stage-5 fitter's parameter inventory, whose declared production
  scope is "live rebuilt L1–L3") lists **none of them** — only the section annotate gate
  `kAnnotateKeyConfidenceThreshold` (group G10). The whole L3 emission-scoring surface is an
  un-inventoried block of stated fit-targets. *(Verify at unblind whether this is a deliberate deferral
  in `cowork_stage5_fitter_design.md`; if not, it is a param-manifest coverage gap.)*

- **OI-93 (low-medium) — two L3 headers reach into the heavy L4 chord header for an enum in the leaf.**
  `section/cadencekeyanchor.h:50` and `section/jointkeydecision.h:85` `#include "chord/chordanalyzer.h"`
  solely for the `ChordQuality` enum — but `ChordQuality` lives in the dependency-free types leaf
  `types/analysistypes.h:120`. The types-leaf refactor removed exactly this header back-edge for
  `keymodeanalyzer.h` and `regiontonecollector.h` but left it on these two section-detector headers. A
  one-line include swap would restore the forward-only layering (Dependency Rule / #7).

- **OI-92 (low-medium) — a duplicated chord-template table across C++ and Python, not sync-guarded.**
  `jointkeydecision.cpp:73-88` `kJkdTemplates` (14-entry tertian vocabulary) is comment-declared
  "IDENTICAL to `tools/cc_joint_residual_probe.py` TEMPLATES", so the chord-pinned test reproduces the
  probe's PINNED class — but nothing enforces it (unlike the mode-prior duplication, which a test
  guards). If either copy drifts the two silently diverge. Diagnostic-only, gated OFF.

- **OI-90 (low) — a mis-tag in the committed L1/L2 file table.** `decode/chordpathdecoder.h` is tagged
  "L3 key-mode decoder scaffolding" there, but it is the beam-1 **CHORD-path** decoder (Stage 3.1,
  Layer 4): it includes `chord/chordanalyzer.h` and threads `ChordAnalysisResult`/`ChordIdentity` via
  `advanceTemporalContext`. Corrected to `L4` in this audit's tag map; noted so the L1/L2 file table can
  be corrected.

- **OI-75 (informational, documented) — the production key-confidence gate reads the weaker of L3's two
  confidences.** L3 publishes an emission sigmoid (`keyModeResult.normalizedConfidence`) AND a sequence
  margin (`keyConfidence`, THE boundary confidence, code-noted 2.8–3.1× better calibrated). The
  production 0.8 KeyArea/cadence gate reads the sigmoid; the better margin has no production consumer.
  This is the deliberate **D-L3a** decision (gate input held as the sigmoid pending L5 wiring; the margin
  is carried for L5). Not a defect — surfaced by the contract check as published-unconsumed-by-design.

- **OI-94 (informational, documented) — two acknowledged deferrals in L3's contract:** (a) a mid-piece
  notated key-signature change is not re-anchored (single-signature anchor at start; note-driven change
  cost only — `regionanalyzer.cpp:626-628`); (b) the A-3 dominant-implication key-evidence channel is
  named but not built. Both are design-acknowledged; recorded for negative-space completeness.

- **OI-93 (low) — shared pitch primitives siloed under `chord/`.** Five core-L3 `.cpp` files include
  `chord/analysisutils.h` for `normalizePc`/`diatonicMaskFromFifths`. That header is dependency-free
  (cstdint/map/string only), so it is not a heavy coupling, but pc primitives consumed cross-layer sit
  in the L4 directory. A layering note.

- **OI-95 (housekeeping, out of L3 scope) — the committed L1/L2 inventory artifacts are line-stale.**
  Regenerating `tools/audit/l1l2/{l1l2_functions.csv,l1l2_decls.csv,inventory.json}` shifts
  `note_model.h` rows by +4 lines (source drift since they were committed). Substance identical. An
  L1/L2-artifact reproducibility note.

- **Observation (not a firm finding) — `redecodeRange` sub-range confidence.** For a pinned sub-range
  re-decode the reported sequence-margin (`SliceKeyMode.confidence`) is computed over the pinned span,
  not the full sequence; the header's "reproduces the matching slice of a full decode EXACTLY" holds for
  the **chosen key** (sub-path optimality) but not necessarily for the margin value. `redecodeRange` is
  test-only (dormant), so this has no production effect; flagged for the incremental-editor wiring step.

## 6. Instrument-establishment (#19) + self-check

- **Inventory instrument** established by the `--self-check` per-file extraction cross-check + the
  L1/L2 byte-identity substance proof (only `note_model.h` line drift). Over-capture bias stated.
- **Fire-rate instrument** (`measure_l3_firerate.py`) runs the existing default-OFF diagnostic over the
  pinned inputs (`tools/corpus/*.xml`, `c50002fee1`); no new C++ instrumentation, production
  byte-identical.
- **Self-check of this session's diffs** (§ the CLAUDE.md self-check rule): the touched files are the
  inventory instrument (behavior-preserving for L1/L2, proven), the two new read-only audit scripts, the
  generated artifacts, and this report. No `src/composing/` production file, no constant, no golden, no
  reference artifact was changed. Reasons/verdicts read against the guiding principles, the conventions
  (no self-invented labels — the tags `L3`/`L3-MIXED` mirror the existing L1/L2 file-table vocabulary;
  all other names are the repository's own), and the gate policies.

## 7. RETIRES list + interpretation-check notes (roadmap retirement map)

- **`keyresolver.cpp::resolveKeyAndModeRanked` — R5 SHRINK (not full retire).** The per-window argmax +
  the mode-switch hysteresis retire (the decoder change cost supersedes them on the production region
  path). **KEEP consciously at deletion:** the shared `resolveKeySignatureContext` (signature read +
  declared-mode mapping + the Baroque `partialSignatureCorrection`) — it is called by BOTH the resolver
  and the decoder wiring; and the insufficient-PCs fallback. The resolver's remaining live duties (the
  segmentation S2 seed, P4 tick-local, the grading baseline) must be re-homed before it shrinks.
- **`section/cadencekeyanchor.{h,cpp}` — R3.** Kept as a diagnostic through E4; retire post-E5 review.
  Interpretation to keep: the key-agnostic salience-weighted anchor logic is the note-derived
  replacement for the lost declared-mode global anchor.
- **`region/regionanalyzer.cpp` `greedyExpandSegmentation` call + `denseBoundaryTicks` — R6 (L2-legacy).**
  The segment-first spine retires at E4; the L3 seam that consumes the slicer survives. Deferred to L2's
  concern (already RETIRES-tagged in the L1/L2 file table).
- **`section/sectioncadencedetection.cpp::detectCadences` — R2 (legacy circular cadence detector).**
  Retires after the two notation-bridge call-site migrations; it reads `function.degree` (key-derived),
  which the key-agnostic `cadencekeyanchor` was built to replace. This is L5's concern (deferred).
- **`jointkeydecision` / `localmodulationdetector` — no retirement; DORMANT builds** awaiting their
  ratified production wiring (J-key-iii / 4d-ii).

## 8. Mis-tag corrections made by this audit (Task 1.1)

- `decode/chordpathdecoder.h`: L1/L2 said "L3 key-mode decoder scaffolding" → **L4** (chord-path decoder;
  OI-90).
- `region/sparsechordrefinement.{h,cpp}`: was `L3+` → **L4** (chord-quality refinement that *consumes*
  the L3 key as a prior; deferred to the L4 audit — not L3 key inference).

## 9. Register + type promotion + certification status (Task 5 — unblind)

**Freeze commit (the blinding boundary): `61dabd86d1`.** After it, `OPEN_ITEMS.md`, `DEFECT_TYPES.md`,
and `STATUS.md` were opened (in that order) — the first opening of every withheld file, per §0.

**Findings → register (each finding mapped; existing rows referenced, not duplicated):**

| Finding | Register | Type |
|---|---|---|
| OI-90 mis-tag (`chordpathdecoder.h` = L4; `sparsechordrefinement` = L4) | **OI-90 (new)** | **DT-21 (new)** |
| OI-91 L3 emission constants absent from `param_manifest.json` | **OI-91 (new)** — the L3 twin of OI-87; feeds OI-6/EG-5 | DT-2 |
| OI-92 `kJkdTemplates` C++↔Python dup, not sync-guarded | **OI-92 (new)** | DT-3 |
| L3→`chord/` cross-layer deps (header back-edge for a leaf enum + pc-util silo) | **OI-93 (new)** — sibling of OI-86 | DT-19 |
| OI-75 `keyConfidence`/`keyAlternatives` unconsumed | **existing OI-75** (re-confirmed + D-L3a detail; relates OI-49) | DT-5 |
| OI-94 mid-piece key-sig re-anchor + A-3 not built | **OI-94 (new)**; A-3 = existing OI-68 | — (documented deferrals) |
| OI-95 + the disposition-generator #6 debt | **OI-95 (new)** | DT-12-adjacent / #6 |
| (modepriorpresets dup, sync-guarded/mitigated) | existing **OI-63** (mode-prior single-sourcing) | DT-3 (mitigated) |

**New problem TYPE promoted (P7/P8):** **DT-21 — Layer mis-attribution in the inventory/tag table** (a
deferred-layer tag wrong on deep-read; re-verify every deep tag at the code, never inherit). Founding
instance = OI-90. Same-commit rule honored (promoted in this report's fold commit). No other finding
implied a new type — OI-91/F3/F4/F7 are instances of the existing DT-2/DT-3/DT-19.

**Not a surprise (guiding principle 3):** every finding is a KNOWN class (DT-2/3/19/5) or a
design-acknowledged deferral — the L3 emission-constant manifest gap is the exact L1/L2 pattern (OI-87)
one layer up; the unconsumed key facts were already OI-75. Nothing contradicts the established fact/theory
basis; the L3 spine reproduces its documented design.

**Certification status: WITHHELD.** Pass 1 (blind enumerative, P1–P4) found **no correctness defect** in
the L3 key/mode inference — the decoder is live and clean, the emission scorer is music-theory-grounded,
the dormant confirmed-modulation/joint-key machinery is correctly gated OFF, and the layering is
forward-only except two documented back-edges. But certification requires BOTH passes plus the P6
error-rate (protocol P6/P8): pass 2 (the DT signature sweep with the full catalog, a fresh session) and
the measured residual-error rate are **owed**. Certification is **not self-granted** — it returns to the
user after pass 2, exactly as L1/L2 did (OI-84/OI-89).

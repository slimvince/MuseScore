# CC L1–L4 comprehensive review + tidy — code / tests / test-data (the step-3 QA gate)

> Companion to `cowork_l1l4_review_charter.md` (the gate) and `cowork_l1l4_review_note.md` (Cowork's
> docs + architecture-coherence half). CC owns **code, tests, and test data** on Windows
> (authoritative source + build/run). Every load-bearing claim below is **VERIFIED at source**
> (file:line / commit-sha) unless tagged INFERRED. Standing rule honoured: verified facts only.

**Blunt verdict (front-loaded): L1–L4 code / tests / data are CLEAN.** Suites green, output
byte-identical, no orphaned/dead code masquerading as live, no new duplication from the L4 build, the
dormant scaffolding is honestly commented. The residual items are all **already-tracked, deferred,
ratified engagement/firewall steps** — none is a defect introduced by the L4 build. Tidy applied in 4
gated commits; 4 items flagged-not-fixed (correctly, per the guardrails).

---

## §0 — Preamble sweep
- **`ed1fb2df6f`** `docs(cowork): L1-L4 review charter + engage-with-L5 ratification` — committed the
  unstaged Cowork docs local-only (the review charter + review note + the 7 modified cowork docs:
  `COWORK_HANDOFF.md`, `cowork_l1l3_stabilization_plan.md`, `cowork_l1l4_architecture_audit.md`,
  `cowork_layer4_chordsymbol_design.md`, `cowork_phase5b_l4_build_plan.md`,
  `cowork_tpc_capability_design.md`, `cowork_types_header_design.md`). `scratch_artifacts/` left
  untracked (working scratch — build logs + BIR dumps, not a doc).

---

## §1 — CODE findings (VERIFIED)

### 1.1 Per-layer correctness vs design — CONFORMS
Suites green + the prior per-stage verification + Cowork's architecture-coherence pass (all 5 checks
VERIFIED INTACT, `cowork_l1l4_review_note.md` §1) establish design-conformance. CC re-verified the
load-bearing structural seams at source:
- **L1 `note_model`** — leaf, dependency-free; ARCHITECTURE.md L1 block as-built. (Not re-audited
  line-by-line; covered by `note_model_tests` + prior Layer-1 build.)
- **L1.5 `engravingbridge` / `spellingview`** — the single shared spelling interpreter. VERIFIED:
  `lineOfFifths` is the SOLE tpc→line-of-fifths interpreter (`spellingview.cpp:32-36`);
  `sharpFlatSense`/`spanSpelling` derive from it (`spellingview.cpp:44-58`). The "one interpreter"
  invariant is even unit-pinned (`spellingview_tests.cpp:150-163`).
- **L2 `slicer`** — `changePointSlices` is WIRED into L3 (`regionanalyzer.cpp:579`, `:651`). VERIFIED.
- **L3 `key/*` + reach-back** — `KeyModeSequenceDecoder` is the live region key/mode path; consumes
  L1 model + L2 slices + the L1.5 `pitchContextOverSpan` builder (`keymodesequence.cpp:89`). VERIFIED.
- **L4 `chord/*`** — legacy `analyzeChord`/gates LIVE; new `chordslicedecoder` G1–G6+pin DORMANT
  (see §1.4). VERIFIED.

No divergence between code and design found. No inference accuracy touched (firewall).

### 1.2 Unification / duplication from the L4 build — NO NEW DUPLICATION; residuals tracked
- **New duplication from the L4 build:** none. `chordslicedecoder.{h,cpp}` includes only
  L1/L1.5/L2/L3 + `spellingview` (Cowork-verified, no back-edge).
- **`analysisutils.h` relocation — TRACKED (VERIFIED).** The header is chord/-located
  (`analysis/chord/analysisutils.h`) but its free functions (`ionianTonicPcFromFifths`, `normalizePc`,
  `diatonicMaskFromFifths`, `isDiatonicStep`) are cross-cutting pitch/key utils used by L3 .cpp
  (`keymodeanalyzer.cpp:24`, `keyresolver.cpp`). This is a `.cpp`-level cross-layer include (NOT a
  header back-edge — the types that were the back-edge, `ParameterBound`/`ParameterBoundsMap`, already
  moved to the leaf `analysistypes.h`, audit-Q2). The whole-header relocation (~20 include edits) is a
  deferred follow-up, recorded in **`cowork_types_header_design.md` D1** (lines 31–39) and the
  **completion-ledger A4** (`cowork_l1l4_completion_ledger.md:31`). The header's own comment
  (`analysisutils.h:32-35`) is accurate. ✓
- **Two live segmenters — coexist by design, NOW honestly documented (was stale; tidied).**
  `changePointSlices` (L2) feeds L3; the legacy `collectNoteChangeTicks`/`HarmonicSegmenter` still runs
  for the legacy chord/harmonic-rhythm path (`regionanalyzer.cpp:749` → `harmonicsegmenter.cpp:580` →
  `:583`). Both are live. The `harmonicsegmenter.cpp:155` comment said the slicer "is isolated/not
  wired in" — now FALSE. **Fixed in `c7aa8a21bc`.**
- **Two pitch-context builders — coexist by design, HONESTLY documented (no action).**
  `collectPitchContext` (legacy DOM-walk, → `keyresolver.cpp:311`) + `pitchContextOverSpan` (L1.5
  indexed, → L3 `keymodesequence.cpp:89`). The coexistence is explicitly documented at
  `regiontonecollector.h:230-236` ("this builder is retired once the decoder is the live key path …
  Until then both exist"). ✓ Honest, deferred, not silently dead.

### 1.3 ★ The tpc-fold — NOT folded; a SECOND tpc reader coexists (REPORTED, not folded)
**The tpc-capability spec §3 fold has NOT happened.** VERIFIED at source:
- The L4 **spelling-pin** (in the **dormant** decoder) reads the shared primitive:
  `chordslicedecoder.cpp:553` → `engravingbridge::lineOfFifths(f.tpc)`.
- The **live legacy scorer** `chordanalyzer.cpp` still builds and interprets its **own** per-pc tpc
  array independently: `std::array<int,12> tpcForPc` built at **`chordanalyzer.cpp:1150-1156`**, then
  consumed across **42 sites** — `tpcSpellsAsSharp` (`:296`), `countTpcMatches` (`:516`),
  `tpcConsistencyBonus` (`:667`), `nonBassAdjustment` (`:447-448`), `detectExtensions`
  (`:238/274/293/315`), the augmented-root check (`:865/889`), the sus4 tpc-disambiguation (`:447-453`).
  None of these call `spellingview`.

**Truth: a second tpc reader coexists today.** The pin reads `lineOfFifths`; the legacy cluster
interprets tpc on its own. This is a **tracked unification residual**, NOT a defect: the fold is owed
only when the decoder goes live and the legacy scorer retires (engage-with-L5). It is **REPORTED, not
folded** here — folding now would rewrite the live scorer (a gated behavioural engagement step,
firewall-adjacent). The `spellingview.h` header comment that said the pin "is the next build" was
itself stale (the pin is built/dormant) and now records this truth — **fixed in `c7aa8a21bc`**.

> INFERRED note: `spanSpelling` / `sharpFlatSense` have **zero** consumers anywhere (only
> `spellingview_tests.cpp`) — the Layer-3 key-spelling *term* (Phase B) is genuinely not built, matching
> the spec. (VERIFIED by whole-module grep.)

### 1.4 Dead-vs-staged honesty — ALL comment-accurate (no action)
Each staged-but-dormant construct honestly explains WHY it is not live (VERIFIED at source):
- **`chordslicedecoder`** — `chordslicedecoder.h:135-140` ISOLATION block: "BUILT, unit-tested, and
  GRADED … but NOT wired into the live analysis pipeline. Production analysis output is byte-identical;
  the decoder runs only under the read-only `batch_analyze --decode-chords` diagnostic." 0 production
  callers (only tests). ✓
- **`redecodeRange`** — `chordslicedecoder.h:479-497`; the incremental-contract spec is explicit;
  dormancy inherited from the class. 0 production callers (test `decode_chord_tests.cpp:1309` only). ✓
- **`tonicizationlabeler`** — `tonicizationlabeler.h:42-46` "6-tonic-i SCOPE: this pass is built and
  MEASURED only … does NOT mutate … NOT emitted into production RN … Wiring … is 6-tonic-ii, separately
  ratified." 0 production callers. ✓
- **`DecodeQualityLevel::Normal/Deep`** — `analysistypes.h:99-116` "reserved (Stage 3.2) — NOT yet
  active (behaves as FastBeam1)"; reinforced at `chordpathdecoder.h:108-111` ("recorded but does not
  change commit behavior … no-op"). 0 production uses of Normal/Deep. ✓
- **`redecodeRange`/`DecodeQualityLevel`/`tonicizationlabeler` were NOT deleted or "cleaned up"** — per
  the charter MUST-NOT, they are deferred-engagement scaffolding (their wire-or-remove verdict is the
  joint L4+L5 step).

### 1.5 Stale comments — found, fixed/triaged
| File:line | Comment | Verdict | Action |
|---|---|---|---|
| `harmonicsegmenter.cpp:155` | "It is isolated/not wired in; this Score-based collector keeps running until layer 3 consumes the slicer." | **STALE** — slicer now wired into L3; both run | **Fixed `c7aa8a21bc`** |
| `spellingview.h:40-44` | "the Layer-4 spelling-pin … is the next build" | **STALE** — pin built/dormant; records the tpc-fold truth | **Fixed `c7aa8a21bc`** |
| `slicer.h:67` | "It IS wired into the live analysis pipeline: layer 3 consumes the slices" | **ALREADY ACCURATE** (the charter expected a "NOT wired" stale comment here — it was already corrected) | none |
| `chordslicedecoder.h:136` | "NOT wired into the live analysis pipeline" | **ACCURATE** (decoder is dormant) | none |
| `postscoringgates.cpp:76` | "the dormant F#m7b5 case" | **ACCURATE** — describes a chord candidate, not code-staging | none |
| `chordslicedecoder.cpp:363` | "an isolated note" | **ACCURATE** — describes a melodic note, not wiring | none |

### 1.6 Dead-vocabulary names — inventoried; FLAGGED for the coordinated rename (not done)
The only iteration-vocabulary identifiers in production source (whole-module grep,
`[A-Za-z]Iter[0-9]` / `\biter[0-9]`):
- **`applyIter8691Pedal`** (function) — defined `chordpostpasses.cpp:119`, declared `chordanalyzer.h:616`.
- **`iter8691ChangedWinner`** (member) — `chordanalyzer.h:405`, set `chorddiagnose.cpp:174`.

**FLAGGED, NOT renamed** — see §4 reasoning. Call-site inventory (for the future rename): ~17
production .cpp sites (`regionanalyzer.cpp:885/1108/1305`, `harmonicsegmenter.cpp:390/399/542/739/816/908`,
`regiontoneprimitives.cpp:511/569`, `sectionanalyzer.cpp:417`, `chordpostpasses.cpp:119/262`,
`chorddiagnose.cpp:172/174`), 6 `chordanalyzer.h` sites, ~30 test sites
(`postscoringgates_tests.cpp`, `test_helpers.h:122`, `diagnose_tests.cpp:26`,
`chordanalyzer_musicxml_tests.cpp:744`), and ~15 doc references (`docs/scoring_model.md`,
`docs/decoder_design.md`, `COWORK_HANDOFF.md:72`, `docs/layer_architecture_audit.md`,
`cowork_implementation_review.md`).

---

## §2 — TEST findings

### 2.1 Suites — GREEN (post-tidy, re-run after rebuild)
| Suite | Result |
|---|---|
| `composing_tests` | **862 / 862** (2 disabled) |
| `notation_tests` | **53 / 53** |
| `pipeline_snapshot_tests` | **11 / 11** (3 disabled) — **no golden refresh** (output byte-identical) |

### 2.2 Oracle-quality spot-check — CONTRACT-based, not echo (PASS)
- **`decode_chord_tests.cpp`** — the scorer-independent `decideSlice` tier injects candidate cubes by
  hand and asserts hand-computed contract values: e.g. `Decide_ConfidenceIsMarginToBestDifferentChord`
  (`:139-148`) asserts `confidence == 1.0` (= 3.0 − 2.0, the margin to the best DIFFERENT chord) and
  `uncertain == false` (margin > 0.5 default) — **no dependency on the production scorer** (by design,
  header `:26-29`). ✓ Not an echo.
- **`spellingview_tests.cpp`** — asserts theory line-of-fifths values (`lineOfFifths(G♯)==8`,
  `lineOfFifths(A♭)==−4`, `G♯≠A♭`) and the one-interpreter consistency invariant. ✓ Oracle.

### 2.3 Consolidated surfaced-defect ledger (every `DISABLED_`/xfail + labelled guard)
| # | What | Where | Correct expected | Belongs to |
|---|---|---|---|---|
| 1 | **German flat-bass slash dropped** — `csfIsValidBassNoteName` rejects "Ces"/"Fes" (the 'e' ≠ '#'/'b'), so the slash is lost | `chordsymbolformatter_branch_tests.cpp:295-324` (`RegressionGuard_GermanFlatBass_SlashDropped` pins current bug; `DISABLED_GermanFlatBass_ShouldKeepSlash` holds the correct oracle) | `"C/Ces"` (currently `"C"`) | **Genuine correctness bug — gated ratified fix** (Cowork-flagged; not firewall) |
| 2 | **Nashville `?` placeholder** — out-of-range degree emits `"?"`, not `""`; slash-bass uses crude `semitone%7+1` | `nashville_tests.cpp:30-44` | neither `""` nor `"?"` is a Nashville-system oracle — `"?"` is the code's deliberate placeholder | **Reported, not xfail'd** (no proven oracle); product decision |
| 3 | **Leading-tone key-context gate (Gate G-E)** — live gate | `postscoringgates.cpp:339-347` (`gLeadingTonePc = (keyTonicPc+11)%12`) | n/a — live, correct | **FIREWALL — MUST NOT touch** (the leading-tone gate the charter protects) |
| 4 | **TPC sus4 disambiguation guard** | `chordanalyzer.cpp:446-455` (the `rootTpc>=0 && noteTpc>=0` guard at `:449`) | n/a — live behavioural guard | **FIREWALL — scoring, MUST NOT touch** |
| 5 | Index-perf microbench (intentional, env/manual) | `note_model_tests.cpp:1011` `DISABLED_IDX_PERF_ScalingIndexedVsLinear` | n/a — perf, not a defect | intentional |
| 6–8 | Snapshot perf/diagnostic sweeps (intentional) | `pipeline_snapshot_tests.cpp:1060` (`P3PerfBaseline.DISABLED_Sweep`), `:1264` (`Stage31bAnswerDelta.DISABLED_Sweep`), `:1365` (`Stage31bPerf.DISABLED_ColdWarm`) | n/a — perf/diagnostic | intentional |
| 9 | Divergence-regen guard (env-gated) | `pipeline_snapshot_tests.cpp:1523` `GTEST_SKIP` unless `PIPELINE_OBSERVE_DIVERGENCE_C=1` | n/a | intentional |

Items **1** and **2** are the substantive surfaced defects (correctness + product placeholder). Items
3–4 are firewall-protected live guards (listed so they are not mistaken for defects). Items 5–9 are
intentional perf/diagnostic disables — **none stale, none orphaned.**

### 2.4 Stale / orphaned tests — none (beyond the deleted stub)
The `chord_analysis_test.py` stub (a never-run placeholder Python "test") is covered by the §3 orphan
deletion. No compiled test references removed code; the 2 composing-disabled + 3 snapshot-disabled are
all intentional (above).

---

## §3 — TEST DATA findings

### 3.1 Orphaned fixtures — 3 confirmed, DELETED
Whole-repo verification (per the `mono_smoke_test` lesson — content grep, not per-dir):
- `src/composing/tests/chord_analysis_test.py` — `# …existing code from c:\s\MS\chord_analysis_test.py…`
- `src/composing/tests/chord_analysis_test_expected.json` — `(Expected JSON content moved from …)`
- `src/composing/tests/chord_analysis_test.musicxml` — `(MusicXML content moved from …)`

All three are **pure "content moved" placeholder stubs** (no real test data), **git-tracked**, and
referenced by **no** CMakeLists or test source (whole-repo grep clean). Their pointed-to originals were
at the project root and are gone. **Confirmed orphans → DELETED in `2243e39243`.**

### 3.2 Fixture hygiene — findings (flagged, not changed)
- **`solid theory.musicxml`** (space in filename, `src/composing/tests/data/`) — it is the provenance
  **source** for the converted, test-loaded `nm_solid_theory.mscx` (tests load the `.mscx`:
  `note_model_tests.cpp:96`, `slicer_tests.cpp:426`; comments name `solid theory.musicxml` as the
  source). **NOT an orphan** (deleting it would lose the editable source). It is a genuine hygiene wart
  — space-named + inconsistent with the `nm_<name>.musicxml`/`nm_<name>.mscx` pair convention used by
  every other fixture. **FLAGGED** (a rename → `nm_solid_theory.musicxml` + 2 comment updates is the
  fix); not executed — a fixture rename is outside the charter's "delete confirmed orphans" tidy bucket.
- **Dual encodings (`.musicxml` source + `.mscx` converted)** — intentional and consistent with the
  "composing_tests can't import MusicXML; fixtures must be `.mscx`" constraint (the `.musicxml` is the
  human-editable source). Not a defect.
- **Catalog naming (DOC staleness, not a data defect):** tests load
  `chordanalyzer_catalog_jazz.musicxml` + `chordanalyzer_catalog_standard.musicxml`
  (`chordanalyzer_musicxml_tests.cpp:727/733`). `CLAUDE.md` + `BUILD_AND_TEST.md §7` still reference the
  pre-split `chordanalyzer_catalog.musicxml` (no longer exists). **FLAGGED** — `CLAUDE.md` is
  out-of-scope standing instructions; `BUILD_AND_TEST.md` is borderline (Cowork's doc domain). Not
  edited.

### 3.3 Corpus integrity — intact
Per-preset dirs + `corpus_manifest.json` (Stage 2.2a). No test-data change touched the corpus; the BIR
gate is byte-identical by construction (§5). No contamination signal.

---

## §4 — TIDY commits made (each gated; suites + snapshots + corpus unchanged)
| Commit | Type | What |
|---|---|---|
| **`2243e39243`** | test data | Delete 3 confirmed-orphan `chord_analysis_test.{py,_expected.json,musicxml}` stubs |
| **`c7aa8a21bc`** | code comments | Fix 2 stale comments: `harmonicsegmenter.cpp:155` (slicer now wired + both segmenters coexist) + `spellingview.h:40-44` (pin built/dormant + tpc-fold truth) |
| **`88acb4c9bc`** | doc (owned) | Add ARCHITECTURE.md as-built **Layer-4** section (mirrors L1/L2/L3) |
| **`e89e04042f`** | doc (owned) | Add STATUS.md current-state entry for the COMPLETE-dormant L4 build + this review |

(Plus `ed1fb2df6f` from §0.)

### Flagged — NOT fixed (per the guardrails / firewall)
1. **German flat-bass slash defect** (§2.3 #1) — a genuine correctness bug. Gated ratified step (the
   bass-name validator must accept German flat names); NOT folded silently. The test pair already pins
   current behaviour + the correct oracle.
2. **`applyIter8691Pedal` / `iter8691ChangedWinner` rename** (§1.6) — behaviour-preserving but a
   **~70-site coordinated code+tests+docs refactor** (~15 doc references in Cowork-owned docs;
   `docs/scoring_model.md` has its own mandatory sync rule). Renaming code-only would create exactly the
   doc-drift the project forbids, and it is an **explicitly-planned coordinated step**
   (`COWORK_HANDOFF.md:72` bundles it with the layer-seam work). FLAGGED for that step, not executed
   unilaterally.
3. **tpc-fold** (§1.3) — deferred to engage-with-L5 (rewrites the live scorer; firewall-adjacent).
4. **Nashville `?` placeholder** (§2.3 #2) — a product decision, no proven oracle.
5. **`solid theory.musicxml` rename + catalog doc-staleness** (§3.2) — hygiene/doc; outside the
   delete-orphans tidy bucket / Cowork's doc domain.

---

## §5 — Gate (after all tidy)
- **`composing_tests` 862/862** (2 disabled), **`notation_tests` 53/53**, **`pipeline_snapshot_tests`
  11/11** (3 disabled) — all green, **no golden refresh**. Identical to the pre-tidy baseline.
- **BIR corpus 53/24/53 — unchanged by construction.** The tidy touched only **comments, docs, and a
  non-loaded orphan-stub deletion** — no scoring / gate / template / scorer code. `batch_analyze` is
  built from the unchanged analyzer, so the corpus is byte-identical; the snapshot suite passing with
  **no `--update-goldens`** directly proves output identity on the pinned corpus. Per CLAUDE.md the full
  corpus-regen gate is **scoped to gate/scoring changes** — none here — so it was not re-run (and a
  re-run would be a no-op). No movement → no STOP.

---

## §6 — Verdict
**L1–L4 code / tests / data: CLEAN.** No defect introduced by the L4 build; no dead code mislabelled as
live; no new duplication; the dormant new-L4 path + staged scaffolding are honestly commented and were
left intact (deferred-engagement, not deleted). Architecture intact (Cowork-verified, CC-corroborated
at the seams). **Residual items are all tracked/deferred/ratified, not blockers:** the tpc-fold (a
second tpc reader coexists — REPORTED), the two-segmenter / two-pitch-context coexistence (documented,
joint-L5), the `analysisutils.h` relocation (ledger A4), the German-bass defect + the iteration-vocab
rename (flagged, gated/coordinated), and minor fixture/doc hygiene (`solid theory.musicxml`, catalog
naming). Tidy landed in 4 gated, by-sha-verifiable commits with zero behavioural movement.

→ **Ready for the ✅ L1–L4 COMPLETE sign-off** (modulo the joint-L5 engagement + legacy retirement +
coverage seal). Then L5.

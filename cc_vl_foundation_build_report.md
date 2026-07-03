# CC report — the voice-leading axis (axis 2) foundation build: VL-A / VL-B / VL-C (dormant)

**Dispatch:** `cc_instruction_vl_foundation_build.md` (session 22f). **Spec:** `cowork_voiceleading_axis_design.md`
(SIGNED 2026-07-03; flipped **AS-BUILT** this session). **HEAD at start:** `0dd64660f4`. **All work local/unpushed,
fork-only.**

## 1. What was built (all dormant — no production call site)

New module family `src/composing/analysis/voiceleading/` (namespace `mu::composing::analysis::voiceleading`):

- **VL-A — `voicelinearview.{h,cpp}`** (§5.1, §7). The lossless per-(staff,voice) linear reorganization of the L1
  note model. Input is a built `notemodel::NoteModel` (or a plain `std::vector<NoteEvent>` — the pure core the oracle
  tests inject by hand); it does **not** re-walk the score (total unification). Same-onset same-voice notes group into
  one `chordal` event; every retained note appears in exactly one line's events once; `flattenToNotes` round-trips the
  L1 content. Reduction is a per-query parameter — v1 provides exactly `TopNote` (`reducedPitch`), never mutating the
  view. Metric weight is **not** copied (spec §7 as signed).
- **VL-B — `voiceleadingprofiles.{h,cpp}`** (§5.2, §0). The motion profile (voice-pair parallel/similar/contrary/
  oblique rates over the §0 simultaneity rule), the per-voice + aggregate interval profile (|iv| histogram bins 0–11,
  ≥12 + repeat/step/leap rates), **and the per-sample `MotionEvent` series** (pair, sample tick, type, the two signed
  harmonic intervals) exposed alongside the rates. Deterministic, no tunable thresholds. It replicates the study's
  `voiceleading.py vl_profile` and `voiceleading2.py vl_profile_B` arithmetic exactly.
- **VL-C — `textureclassifier.{h,cpp}` + generated `textureclassifierreference.h`** (§5.3). Texture-of-span
  classification by nearest-centroid in the measured winning feature space (below), emitting the committed class **plus
  the full ranked list of ALL class fits with weights** (zero information loss), a Class-M confidence squashed to
  [0,1], and abstention by the three named floors / no-pair rule. Whole-selection granularity (v1).
- **VL-C requester (Task D)** — `classifySelectionExtending` in `textureclassifier.cpp` (§8). The bounded-context
  discovery rule, coded + tested: cue fires iff samples < evidential floor **and** margin < margin floor; a
  requester-owned loop calls `NoteModel::extend` (later first, then earlier), re-builds view→profiles→classification
  each step, stops on convergence / hard bound / score boundary, and attaches `clippedBySelectionEdge` / `cueDenied`
  provenance. Follows the L4 `decodeSelection` precedent (by-value model, forward re-run, whole-score inertness).
- **Diagnostic + parity (Task E)** — `--dump-vl` in `tools/batch_analyze.cpp` (default OFF, additive, own dispatch
  path returning before `analyzeScore`) dumps the view, profiles, motion events, VL-C output, and the reduced per-line
  tuples; `tools/compare_vl_parity.py` feeds those tuples through the study's own feature functions and diffs.
- **Feature-space measurement** — `idiom_discovery/run_vl_feature_space.py` (read-only; reuses the study's cached
  records + its own `cap`/`matrix`).

## 2. The feature-space measurement (Task C precursor — the knowledge gate, §5.3)

Read-only, in Python, on the study's saved feature data (`$TEMP/vl_records.pkl`, 2,102 pieces). The **reference** is
the ratified four-class taxonomy = `KMeans(K=4, random_state=0, n_init=10)` on the concatenated (AB) space at the
study's confound cap (cap=80/source, n=1409) — reproduced **exactly** (class sizes 360/329/395/325, matching the study
`idiom_table` AB block). Decisive metric = how well **nearest-centroid in each candidate space reproduces that ratified
partition** (ARI + label-aligned accuracy):

| candidate space | nc-ARI | nc-accuracy | free-KMeans4 ARI |
|---|---|---|---|
| motion-only (View B) | 0.258 | 0.545 | 0.219 |
| two-stage (B split → A refine) | 0.716 | 0.881 | — |
| **z-scored concatenation (ABz)** | **0.791** | **0.918** | 0.524 |

(raw concatenation A+B rejected a priori for the measured motion dilution.) **Winner: z-scored concatenation (ABz)** —
decisively ahead. The declared tolerance (winner reproduces > 0.90 of the memberships, clearly best of the three) was
met with margin, so **no §10(b) STOP**. The shipped reference set (mean/std over the fit set + 4 z-space centroids +
precision-phase floor defaults) is the **generated** `textureclassifierreference.h` with full provenance (run, corpus
state, K=4, seed 0, sklearn 1.9.0). Class names are assigned by **signature** (index-independent): Contrapuntal =
lowest oblique/highest contrary+similar; HomophonicPianistic = highest leap; HomophonicClassical = highest oblique of
the rest; ModerateMixed = remainder — confirmed against the raw per-class means.

## 3. The two build declarations the design owed

- **§15-2 — the "parallel" interval-preservation convention: SEMITONE-EXACT.** Read at source
  (`voiceleading2.py _motion`): `parallel` iff both voices move the same direction **and** `(pu1−pv1)==(pu0−pv0)` on
  the *signed MIDI pitch difference* — a same-direction move whose semitone interval changes is `similar`, **not**
  generic-diatonic. Replicated exactly in `classifyMotion` and oracle-tested
  (`ParallelIsSemitoneExactNotGeneric`). **§15-2 CLOSED** (spec updated).
- **Profile-eligibility filter — reconciled and declared.** The instruction's parenthetical named a 2-flag filter
  (`plays && staffEligible`) but bound it to "consistent with the existing derived views." The **verified** filter of
  the direct per-(staff,voice) line-view precedent (`phraseboundaryview.cpp` `isEligibleNote`) is **3-flag**
  `plays && visible && staffEligible` (the project-canonical "eligible voice" test). I used the verified 3-flag filter
  (honoring the binding "consistent with the existing derived views" directive) and declared it in VL-A's header and
  the spec. Grace notes are retained by the lossless view and participate in the top-note reduction exactly as
  `phraseboundaryview` does (they merge into their onset's event). This is a reconciliation of an instruction
  imprecision, not a spec↔instruction contradiction — no STOP warranted.

## 4. Acceptance (ALL required — all met)

1. **Suites green, no snapshot refresh:** composing **1083/1083** (1056 baseline + 27 new; 2 disabled as before) ·
   notation **53/53** · pipeline snapshots **11/11** (no `--update-goldens`). Both suites + snapshots run clean.
2. **Gate proof by measurement:** regenerated all three presets (`run_bach_preset.py` → `characterise_bir_false.py`,
   per-preset dirs `tools/corpus/{baroque,jazz,default}`). BIR=false counts **53 / 24 / 53**, and the **case-identity
   sets are byte-identical to CLAUDE.md** — set-diff empty both directions on all three presets (verified by
   programmatic set comparison against the CLAUDE.md stem@tick lists). The dormant build is proven non-contaminating.
3. **Dormancy grep-proof:** the ONLY files referencing any voiceleading symbol are the 7 module files (self), the test
   `voiceleading_tests.cpp`, and the `--dump-vl` diagnostic in `tools/batch_analyze.cpp`. **No production `src/` file
   outside the module references any VL symbol.**
4. **Parity check passes** on the pinned research-tier sample (10 Bach chorales + Mozart K279-1/2 + Beethoven 01-1 +
   Corelli op01n01a/b): **15/15 float-exact**, worst |diff| A=5.0e-13 / B=5.0e-13 (= the 12-decimal dump rounding,
   ≪ tol 1e-9). Incidental musical sanity (not asserted as ground truth): chorales → Contrapuntal, Mozart/Beethoven →
   HomophonicClassical, Corelli → Contrapuntal — the last matches the study's "Corelli groups with the chorales"
   finding.
5. **Reuse-vs-new + what retires** — §5 below.
6. **Doc-sync (same increment):** ARCHITECTURE §2.15 (axis-2 status line + voice-leading-span criterion pointer);
   `docs/implementation_roadmap.md` step 4 (FOUNDATION ✅ BUILT + DORMANT); `cowork_confidence_contract.md` §3 row +
   R5 squash declaration (*texture-of-span*, Class M); the spec `cowork_voiceleading_axis_design.md` flipped
   **AS-BUILT** carrying the §5.3 feature-space declaration and the §15-2 answer. **CLAUDE.md untouched** (verified).
7. **Commits** — local/unpushed/fork-only, split module / tests / diagnostic+parity / docs (§6 below).

## 5. Reuse-vs-new + what retires

- **Reuses:** the one L1 `NoteModel` (no second note model; VL-A reads `model.notes()`); the `NoteModel::extend`
  bounded-context seam and the L4 `decodeSelection` requester pattern (by-value model, forward re-run, whole-score
  inertness, denial provenance); the standard analysis-view line filter (`phraseboundaryview` 3-flag precedent); the
  batch_analyze dump/JSON idiom; the study's Python pipeline as the validation/fitting harness (the discovery-protocol
  extractors + cached feature matrix) — not a parallel new rig.
- **New:** the axis-2 module family (VL-A/B/C + requester), the generated reference set, `--dump-vl`,
  `compare_vl_parity.py`, `run_vl_feature_space.py`.
- **Retires: NOTHING** — this is a new orthogonal axis, not a replacement. The Python discovery pipeline stays research
  tooling (the fitting/validation harness for VL-C's reference set); it is not superseded by the C++.

## 6. Commits (this session)

Suggested split, all on `master` local/unpushed:
- `feat(voiceleading): VL-A/B/C dormant foundation + generated reference set` — the module + `analysis/CMakeLists.txt`.
- `test(voiceleading): oracle tests for VL-A/B/C + the extension requester` — `voiceleading_tests.cpp` +
  `tests/CMakeLists.txt`.
- `feat(tools): --dump-vl diagnostic + VL study-parity + feature-space measurement` — `batch_analyze.cpp`,
  `compare_vl_parity.py`, `run_vl_feature_space.py`.
- `docs(cowork): VL axis foundation AS-BUILT — spec flip + ARCH/roadmap/confidence-contract sync + report` — the four
  doc-sync targets + the spec + this report (force-added per `/cc_*.md`).

## 7. STOP conditions — none hit. One carry-contract surprise SURFACED (not worked around)

No suite went red, no snapshot refresh was needed, no gate set-diff was nonempty, the feature-space measurement met its
criterion, no spec↔instruction contradiction (the eligibility-filter imprecision is a reconciliation, §3), and every
needed fact was obtainable from the named sources. No inference problems discovered (the build is
architecture/algorithm-driven throughout).

**★ Carry-contract surprise (SURFACED for Cowork, deliberately NOT bundled into my commits):** the working tree
arrived with **pre-existing uncommitted session-22f Cowork docs** that I did NOT author and that are OUTSIDE my
doc-sync scope: `STATUS.md` (the session-22f entry), `COWORK_HANDOFF.md`, and `cowork_polyphony_phrase_harmony_research.md`
(the §6b sweep). The spec itself (`cowork_voiceleading_axis_design.md`) was **untracked** (never committed). Per
acceptance I committed the spec (it must flip AS-BUILT) inside the `docs(cowork):` commit, but I left the three Cowork
narrative files **uncommitted** for Cowork to fold together with the landing STATUS entry (I did not add my own STATUS
entry — that is Cowork's post-verification act). Also left untracked as before: `idiom_discovery/vl_discovery_out.txt`,
`vl_orthogonality_out.txt`, `scratch_artifacts/`. Flagging so the tree state is not a surprise at verification.

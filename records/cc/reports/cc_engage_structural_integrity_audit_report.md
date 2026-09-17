# CC report — Engage arc #6: the STRUCTURAL-INTEGRITY audit (read-only, all built layers)

**Dispatch:** `cc_instruction_engage_structural_integrity_audit.md` (Cowork, 2026-07-06).
**Executed:** CC, 2026-07-07. **HEAD:** `5fa16b77e0113685eb63556ebd13949a11ca78cf` (`master`, fork-only,
ahead 0). **Both regression stops:** GREEN and untouched (read-only — no `src/`, no corpus write, no build,
no fix). **Deliverable:** `cowork_structural_integrity_audit.md` (the grounded catalogue).

---

## 1. Method

- **Task 0 — priors read + extended (not re-derived):** `cowork_l1l4_architecture_audit.md`,
  `cowork_architecture_review_2026_07.md` (F-1…F-18), `cowork_implementation_review.md` (2026-06-10 —
  verified stale-vs-current at code), the owed-refactor records in `cowork_stage5_fitter_design.md`
  (OWED #1 file-split → R9; OWED #2 §6-block dissolution → Stage-5/E4), and `fix_results_cap_exhaustion.md`.
- **Task 1 — the anchor deep-diagnosed by CC directly** at the code (`harmonicfunctionlayer.cpp`,
  `chordpostpasses.cpp`, `postscoringgates.cpp`, `chordslicedecoder.cpp`, `batch_analyze.cpp`,
  `notationcomposingbridge.cpp`), plus a read-only fan-out measurement over the three per-preset corpora.
- **Task 2 — every built layer swept by four parallel read-only agents** (fact layers L1/L1.5/L2; key L3 +
  decode; L4 gates + region + section; L5/L6/VL + tools), each hit re-grounded at file + symbol + line.
- Pattern-class hunted: **(a)** limit→compensating workaround · **(b)** concern-coupling · **(c)**
  duplication · **(d)** workaround-on-a-mechanism · **(e)** cross-layer reach-in · **(+)** other. Each hit
  classified **VIOLATION / OK / UNCLEAR** + severity; over-flagging guard applied (a clean shared structure
  with several consumers, or a dormant-by-design module, is OK — not a violation).

## 2. Layers swept

L1 notemodel · L1.5 engravingbridge (incl. phrase boundaries) · L2 slicing + harmony · L3 key + decode ·
L4 chord (legacy `analyzeChord`+gates path AND the dormant `ChordSliceDecoder`) · L5 function (dormant) +
progression + vocabulary · L6 grouping · the voice-leading axis · the shared region/section/scoreharvest/
types carries · `tools/` (metric scripts + `batch_analyze` caps). **All in scope covered.**

## 3. Counts

- **1 deep-diagnosed anchor** (`results` carry substrate) + **20 swept sites**.
- By class: **6 VIOLATION · 8 UNCLEAR · 6 OK-noted / RESOLVED.**
- By severity: **2 HIGH · 9 MED · 9 LOW.**
- **No new HIGH outside** the anchor and one live-path reach-in (`findTemporalContext`, S1).
- **Progress confirmed (extends the priors):** section-layer-in-notation RESOLVED; `promoteToWinner`
  unification, `kMasks`-from-templates, single-owned metric scripts, and `forwardoverride` all confirmed
  clean; the `progression/`/`vocabulary/`/`grouping/`/`voiceleading/` dirs swept clean.

## 4. The anchor diagnosis (summary)

`std::vector<ChordAnalysisResult> results` is **one structure serving ten consumers/concerns** (winner
`front()`; carry `[1..]`→`alternatives`; cap-of-3 at `harmonicfunctionlayer.cpp:521`; the "guaranteed
inversion alternative" diff-root append at `:530-549`; Iter 86 `chordpostpasses.cpp:135-149`; Iter 91
`:163-188`; pedal detection `:209-281`; the gate flip via the uncapped `gateCtx->rawCandidates`; the batch
serialization cap `batch_analyze.cpp:660/712`; the uncapped bridge view `notationcomposingbridge.cpp:297`).

- **The cap→append dissolution is PROVEN at code:** the append only pulls above-threshold candidates
  (`:543`), so an uncapped threshold-only build is a strict **superset** — the append becomes dead code;
  winner unchanged, only the carried set grows (⟹ a `.ours.json`-byte change ⟹ a ratified re-baseline, not a
  free edit). **One honest discrimination:** Iter 91's `kPromoteAppendOnly` / `stopBelowThreshold=false`
  pull reaches **below** threshold — a legitimate targeted promotion that does **not** dissolve.
- **The pedal concern** clobbers the shared vector (`results = pass2`, `:274`), **re-implements** the
  different-root scan (`:262-269`), and **defensively disables** the append (`:240-241`) — three symptoms of
  a detection concern mutating the winning identity in place.
- **The clean-target is ALREADY BUILT in the dormant decoder** (`chordslicedecoder.cpp:746-789`): a governed
  `topK`-on-distinct-voicings ∪ a principled incumbent-carry, with the different-root reading **read from**
  the carry (`:927-930`) — no cap-exhaustion, no compensating append. (The decoder has **no** pedal
  detection yet — a gap the engage design must fill.)
- **Fan-out (read-only, capped floor):** the append fires on **36.2 % Baroque / 21.5 % Jazz / 36.1 %
  Default** of all regions (serialized `alts=3` ⟺ append fired, since the internal cap is 3 total); bass-root
  winners are 63–67 %. The **true untruncated** ranked-set size needs the `rawCandidates` instrument (flagged
  as a later measured step, per #1).

## 5. ★ The sequencing call

**Verdict: the anchor is a legacy-Layer-4 tangle whose clean-target the dormant decoder already realizes —
so it FOLDS INTO E4, not a standalone pre-L5 refactor — while three portable slices ARE pre-L5 wins.** One
coherent order, cross-referenced to the owed refactors:

1. **PRE-L5 (now; path-independent):** unify the different-root scan into one primitive (FQ-1); relocate
   `findTemporalContext` out of L1.5 (FQ-3, live-path HIGH); the fact-layer duplication cleanups (FQ-5); the
   serialization/display cap-views (FQ-6); source the key-decoder constants from shared symbols (FQ-7).
2. **STAGE-5 / §6-block dissolution (OWED #2, R1):** give quality-from-key one owner (FQ-2, decided with the
   Gates L/G-E dissolution); the F-1 confidence contract (FQ-8/S19).
3. **E4 (legacy chord path retirement; decoder engages):** the anchor (FQ-4) — decoder carry replaces the
   `results` substrate; the audit's clean-target is the engage input (pedal home; exhaustion watch-item;
   Iter 91 re-expression); the two-segmenters / two-pitch-context / tpc-fold migrations (FQ-8); the
   `function/` dir rename.
4. **R9 (after E4 removals; OWED #1):** the `chordanalyzer.cpp` file split — "split once," last.

No new stage is introduced — the audit's fixes slot into the plan the roadmap already has.

## 6. Acceptance check

Priors read + extended ✓ · anchor deep-diagnosed (consumer map, cap→append dissolution tested, concern
separation, clean-target, fan-out measured) ✓ · every built layer swept, each hit grounded + classified +
severity-ranked ✓ · prioritized fix-queue + the **pre-L5-vs-part-of-L5 sequencing call** cross-referenced to
R9 + the §6-block dissolution ✓ · catalogue + this report written ✓ · UNCLEAR rows surfaced for adjudication
(7) ✓ · **no `src`/corpus/build/fix; both stops green; to be pushed fork-only** ✓.

## 7. SHAs / provenance

- HEAD at audit: `5fa16b77e0113685eb63556ebd13949a11ca78cf`.
- Deliverables (this fold commit): `cowork_structural_integrity_audit.md` (catalogue),
  `cc_engage_structural_integrity_audit_report.md` (this report),
  `cc_instruction_engage_structural_integrity_audit.md` (the dispatch, force-added), plus the STATUS.md /
  COWORK_HANDOFF.md / `cowork_stage5_fitter_design.md` §15 (O-22) folds.
- The pending uncommitted `CLAUDE.md` #12 edit was left untouched (a later dispatch folds it), per the
  dispatch.

*CC, 2026-07-07. Read-only structural-integrity catalogue; every fix is its own later ratified refactor.*

# CC report — Engage arc #4: the information-loss audit (read-only catalogue)

**Dispatch:** `cc_instruction_engage_information_loss_audit.md` (Cowork, 2026-07-06). **Mode: READ-ONLY** — no
`src/` change, no corpus write, no build, no fix. The deliverable is a grounded, classified, prioritized
catalogue: **`cowork_information_loss_audit.md`**. Fitter **O-20**.

## Task 0 — state check

- HEAD = `b0acb5c436` ("docs(cowork): Engage arc #3 — GateA promotion-unification design/scoping (read-only)").
  Branch `master`, ahead of `origin/master` by **0** (the arc-#3 fold was pushed). Confirms the dispatch's "HEAD =
  the Gate A build commit *or* `b0acb5c436` if the build has not yet landed" — **the build has not landed; HEAD is
  `b0acb5c436`** (the design/scoping fold).
- Both stops **green by construction** (read-only, untouched — zero `src/` in `git status`; byte-identical to HEAD =
  batch 52/24/52 + robust-unit sandwich identity). No re-measurement run (nothing perturbs them).

## Method (Tasks 1–2)

Four parallel read-only tracing passes over the load-bearing surfaces named in
`cowork_functional_analysis_research_grounding.md` (bass · spelling · distinct alternatives · preserved
uncertainty), each returning file:line-grounded candidate sites + a consumer trace (grep of who reads the
produced value). **Every candidate was then verified at code by CC** before classification — the central axis
(OK-provisioned / DEFECT-lost / DEFECT-should-already / UNCLEAR) is applied **only** on verified consumer status
(#1: no assumed consumers; ambiguous ⟹ UNCLEAR, not guessed). Surfaces swept:

- the carried readings / `alternatives[]` (chord) — legacy `results[]` build, Gate A/FM2 promotion, the 3 `buildResult`
  wrappers, the truncation-to-3, and the dormant L4 `SliceChord` carry;
- confidence / uncertainty values — `analyzeKeyMode` sigmoid, the Layer-3 sequence margin, `SliceConfidence`,
  the F-B override / `forwardoverride` gate;
- the key & chord candidate sets + the key-then-chord truncation — `KeyModeSequenceDecoder`, `regionanalyzer`
  reduction seam, `jointkeydecision`, the owed joint step;
- pitch spelling — `mergeChordAnalysisTones`, `tpcForPc`, the L4 per-note spelling-pin;
- the diagnostic / dump surface — `chorddiagnose`, `batch_analyze` JSON.

**The classification hinge (verified at ARCHITECTURE.md §Layers 4/5):** production runs the **LEGACY** `analyzeChord`
+ gates path; Layer 4 (`ChordSliceDecoder`) and Layer 5 (`functionoutput`) are **Built+Dormant**. Most not-yet-consumed
signals are the dormant path's forward-provisioning (→ OK); the genuine LOST sites are on the legacy path's
user-visible carry surface (O-11: inside the byte-identity contract, E-14, and the L5 selection surface).

## Counts by classification (11 catalogued sites)

| bucket | count | sites |
|---|---|---|
| **DEFECT — LOST** | **2** | L1 (Gate A/FM2 non-unified promotion), L2 (legacy `tpcForPc`/merge spelling collapse) |
| **DEFECT — SHOULD-ALREADY** | **0** | *(empty — informative: the substrate is cleanly forward-provisioned, not mis-wired; the one apparent candidate is a ratified D-L3a deferral)* |
| **OK — PRESERVED (engage-ready)** | **7** | K1 `SliceChord`, K2 `FunctionLayerOutput`, K3 `HarmonicRegion.keyAlternatives/keyConfidence`, K4 `ChordPathNode`, K5 key-alts/dump, K6 `uncertain` (recomputable), K7 `SliceConfidence` components (Agent-flagged, reclassified) |
| **UNCLEAR** | **3** | U1 (top-3 cap — which surface L5 binds), U2 (J-key-iii stale alt-ranking — joint-step anchor), U3 (coalesce bass re-derive) |

Plus 2 LIVE-path overwrite-on-recompute sites **considered and classified OK/not-a-defect** (pedal Pass-2
overwrite — provenance preserved, the discarded reading is the error; sparse-quality refinement — evidence-gated,
ambiguity explicitly kept `Unknown`). Two **new taxonomy forms** recorded: (+1) honest-unknown-carry (the positive
counter-form — `extensionsKnown`/`openMark`/Abstain); (+2) recomputable-collapse (a collapse whose source is
carried/regenerable is lossless — guards against over-flagging).

## Top DEFECT findings

- **L1 — Gate A vs FM2 (HIGH, #4-relevant; already scoped O-19).** `postscoringgates.cpp:214-234`: Gate A's
  `std::swap` (l.217) preserves the winner's distinct enharmonic Major-add6 partner as a carried alternative; FM2's
  `push_back(buildResult(rc))` (l.229-230) appends a **freshly-built near-duplicate of the winner** instead — the
  distinct partner is not equivalently preserved. Consumer is **PRESENT** (`notationcomposingbridge.cpp:298-300` →
  `outContext.chordResults`, user-visible) **and** the future L5. Correct-carry model = the Gate G-E phantom-pop
  `results.pop_back()` (`postscoringgates.cpp:388-392`). Fix = the O-19 `promoteToWinner` unification.
- **L2 — legacy spelling collapse (MEDIUM, #4-relevant; NEW).** `analysisutils.h:175-180` +
  `chordanalyzer.cpp:1229-1240`: same-pitch-class tones with **different TPC** collapse to one spelling, arbitrated by
  **iteration order** (merge: lowest pitch; `tpcForPc`: first-seen), not voice/weight. Destroys a distinct enharmonic
  spelling for the analysis; consumed by the present legacy scorer/namer. The rebuild L4 path already does spelling
  correctly (per-note `FocalNote.tpc` + shared `lineOfFifths`), so the fix is the named **"second tpc reader"
  unification residual** — adopt L4's reader on the live path (closes a #4 loss + a #6 duplication).

Spelling (L2) and distinct-alternatives (L1) are the exact levers
`cowork_functional_analysis_research_grounding.md` §4 names for recovering wrongly-overridden roots — both flagged
high-value.

## Acceptance

- Load-bearing surfaces swept for the a–i(+) loss forms ✓ (taxonomy-coverage table, both new forms recorded).
- Every hit grounded at code and classified on the central axis; **no assumed consumer-status** (3 UNCLEAR recorded
  for adjudication rather than guessed) ✓.
- Catalogue + prioritized DEFECT fix-queue + the OK-provisioned (engage-ready) and UNCLEAR lists + research
  cross-references on the #4-relevant losses ✓.
- No `src/` / corpus / build / fix; both stops green; suites unchanged (no build) ✓.

## SHAs

- Pre-fold HEAD: `b0acb5c436`. Fold commit: `docs(cowork):` — catalogue + this report + STATUS + HANDOFF + fitter
  O-20 + the dispatch (force-add). **Fold commit SHA reported to the user on completion** (it cannot be embedded in
  its own commit); pushed fork-only (`git push origin master`) — the `cfc7eb5e39` upstream HARD STOP honored.

*CC, Engage arc #4, 2026-07-06. On this report: Cowork verifies the catalogue at objects → brings the user the DEFECT
fix-queue (L1/L2) and the UNCLEAR rows (U1/U2/U3) to adjudicate.*

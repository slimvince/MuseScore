# Consolidated Implementation Roadmap — Reviews → Plan

*Written 2026-06-10 (session 5). Owner: Cowork (plan) / CC (execution).*
*Sources: `cowork_target_architecture_review.md` (part 1 — target architecture),
`cowork_implementation_review.md` (part 2 — as-built). This document is the single tracker
ensuring every review conclusion is addressed. Ordering principle: **no surprises** — verify
and pin each layer/gate/method before building on it; every stage has an explicit
verification gate that must pass before the next stage starts.*

**Standing rule for this roadmap:** an item may only be marked done with the evidence listed
in its "verify" column. Stages are sequential; items within a stage can run in any order
unless noted. Baselines (BIR 24/13 Baroque, 35/7 Jazz; 416/52/11 tests) are hard gates
throughout Stages 0–2; Stage 3+ re-baselines deliberately and explicitly.
**(Re-baselined 2026-06-13: the corrected GT parser → gate Baroque 53 / Jazz 24 / Default 53,
a strict superset of the old 13/7/14; the `analyze_inversion_errors` 24/13·35/7 secondary
split was re-measured under the corrected parser → **47/57 Baroque / 81/23 Jazz** (false-halves
= the then-57/23 gate; the L3-wiring delta later moved it → 53/24/53). Authoritative identity
sets: CLAUDE.md gate section.)**

**⛔ TWO DEFERRED STRUCTURAL REFACTORS — DO NOT FORGET (user mandate 2026-06-14):** (1) **Stage 3.5**
the physical split of `chordanalyzer.cpp` along the layer seams + iteration-API renames — DEFERRED until
the layer boundaries stabilize; (2) **Stage 5** the dissolution of the post-hoc gate-correction layer
(Gates A–L) into fitted weights — the gates are still load-bearing (3.4 retired none). Neither blocks the
current Stage-4 key work, but both are OWED and must be surfaced at every planning checkpoint until done.
Mirrored in `cowork_handoff.md` (top standing block).

**★ BACK-HALF VERIFICATION METHOD (user, 2026-06-14): LAYER-BY-LAYER AUDIT.** Once every piece is in its
correct layer, audit each layer in isolation — state its single responsibility, check correct + complete
against THAT responsibility only (inputs assumed correct, consumers ignored), pin gaps as that layer's
obligations. This is the payoff of Stages 0–3 (the seams are now real) and the reason the two deferred
refactors above matter (a layer can't be cleanly audited while physically tangled in `chordanalyzer.cpp`
or smeared across the post-hoc gate layer). Applied per layer as Stages 4–6 land each piece.

---

**★★★ CURRENT STATE + FORWARD INCREMENT PLAN (updated 2026-06-30).** The architecture is the **forward-only six-layer**
target (canonical: `ARCHITECTURE.md`): L1 notes → L2 slicing → L3 key/mode → L4 chord → L5 function → L6 grouping, plus
the **Harmonic Vocabulary** (encyclopedia — an independent queried component) and a **recognition consumer** that wires
it into L5/L6. Every analysis layer is **built dormant and validated byte-identically against the frozen references**
(the legacy path + DCML ground truth); the production switch ("engage") is **deferred indefinitely**.

| Layer / component | Status | Note |
|---|---|---|
| **L1 — note model** | ✅ Built + **LIVE** | lossless tie-resolved note model + derived views |
| **L2 — change-point slicing** | ✅ Built + **LIVE** | consumed by L3 (`regionanalyzer.cpp:579`) |
| **L3 — key/mode** | ✅ Built + **LIVE** | `KeyModeSequenceDecoder` — first rebuilt decision layer to go live |
| **L4 — chord (per-slice decoder)** | ✅ Built + **DORMANT** | not wired; engages with L5 |
| **L5 — function** | ✅ Built + **DORMANT** | Phase 5c complete; uses its own **§5.0 pairwise** licensed-progression grammar — **NOT** the encyclopedia |
| **L6 — grouping** | ◻ **DESIGN v1** (`cowork_layer6_grouping_design.md`) | the next structural build |
| **Harmonic Vocabulary** (encyclopedia) | ✅ Built + **DORMANT** | separate queried component: multi-chord progressions + substitutions |
| **Recognition consumer** (encyclopedia → L5 prior + L6 annotation) | ◻ **DESIGNED, not built** (`cowork_progression_schema_design.md`) | the step that makes L5 actually *use* the encyclopedia |
| **Idiom taxonomy + voice-leading axis** | ✅ **EMPIRICAL STUDY COMPLETE** | 5 idioms (`cowork_style_taxonomy_proposal.md`); voice-leading confirmed a 2nd orthogonal axis (`cowork_idiom_discovery_findings.md`) |

**Forward increment sequence** (ratified order: encyclopedia → L6 → wire consumer; the idiom + voice-leading work folds in):
1. **StyleTag swap** — re-tag the encyclopedia entries with the five idioms (`cowork_idiom_entry_mapping.md`) and swap the
   placeholder `{Baroque, Jazz, Default}` enum. *Mechanical; the per-entry mapping is written; CC handoff ready.*
2. **L6 (grouping)** — ratify the v1 design → build dormant, byte-identical.
3. **Recognition consumer** — build + wire: the encyclopedia becomes L5's multi-chord disambiguation prior (the §5.5
   resolver + the §8 forward-override) and L6's sequence-span annotation. **This is the step where L5 takes advantage of
   the encyclopedia AND the five idioms** (the active idiom-mixture weights the matches). Until this exists, L5 does not
   touch the encyclopedia.
4. **Voice-leading layer (axis 2)** — the fuller voice-leading-idiom discovery (the pilot confirmed the axis, ARI 0.68) →
   the spec's voice-leading layer; it claims the voice-leading-defined catalog entries (galant schemata, line cliché).
   **This is also the home of the accepted (melodic, broadly monophonic) music-theory phrase** — the linear,
   text-coinciding-when-sung unit, and the **concurrent, overlapping, out-of-phase per-voice phrases** of contrapuntal
   textures (fugues) — which are a *melodic/voice-leading* construct, **not** L6's flat harmonic-grouping span (the L6 §0
   terminology correction). **Research foundation to lean on** (`cowork_polyphony_phrase_harmony_research.md`, deep search
   2026-07-01): voice recovery from implied polyphony (Chew & Wu contig-mapping, VISA, Temperley "Voice and Stream", the
   IJCAI-2023 link-prediction GNN, `partitura`/`music21` voice tools) + per-line melodic phrase segmentation (the DNN
   segmenter, GTTM grouping rules). No published system models overlapping per-voice phrases for *harmonic* analysis, so
   this axis is genuinely separate from the harmonic pipeline.
   - **★ Downstream L4 lever recorded here (proper layer = L4 emission), not built now (standing rule).** The field
     absorbs the counterpoint / implied-harmony difficulty via an explicit **non-chord-tone filter** that excludes
     passing/non-functional notes before harmonic labelling (AnalysisGNN's non-chord-tone module; Contrapunctus's
     passing/neighbour/suspension/embellishment classifier). This is an **emission-level (L4)** lever informed by the
     voice-leading axis — consistent with the meta-principle that precision lives in emission + the functional layer, not
     in search — and a natural candidate for the ratified **gated joint step**. Logged as a future L4/joint-step item;
     **no inference problem-fixing until refactoring / architectural design / algorithmic completion is done.**
5. **Idiom auto-detection + instrumentation prior** — read the idiom-mixture off a score's *committed* progressions
   (+ instrumentation as a context prior) to replace/augment the manual preset. **An inference feature → deferred until
   the refactoring / architectural / algorithmic build is complete (standing rule).**
6. **Engage** — wire the dormant layers (L4/L5/L6 + consumer) into production, retire the legacy spine, seal coverage.
   **Deferred indefinitely** — the mission is build + validate every layer dormant against the frozen references first.

**Standing constraints (carried):** no inference problem-fixing until all refactoring / architectural design /
algorithmic completion is done; all amendments in their proper layer; the two OWED structural refactors (Stage 3.5 split
+ Stage 5 gate-dissolution, below) surfaced at every checkpoint; fork-only distribution (never `upstream`).

**★ THE TEMPORAL-EXTENSION COMPLETION CLUSTER (named 2026-07-02, user question at L6 sign-off).** The §2.15
bounded-context machinery ("we are at the edge of what we've read → request more score") is specified across the spine
but **exercised nowhere**; it activates as ONE cluster at engage. Per-layer status: **L1** `extend()` specified+coded,
zero callers · **L2** re-slice-on-extend specified+coded (CP1–CP7); incremental form deferred · **L3** reach-back
trigger specified+coded, gated OFF · **L4** trigger specified, NOT coded — silently truncates (gap-analysis #5, owed
at engage) · **L5** the need is named but the recognition rule (when/how much look-ahead) is the §15-3 engagement pin —
un-pinned, hence un-coded · **L6** edge-truncation provenance + `extension-cue` surfacing (post-sign-off amendment,
2026-07-02). **The system-level gap:** the cues are per-layer; the receiving POLICY (who widens the selection, loop
bound, convergence) exists only for L3's reach-back loop — a unified extension-orchestration contract is owed with this
cluster (it is what makes R1–R3 real product properties). ~~No item here blocks the dormant builds; the cluster rides
G1/E-steps.~~ **★ SUPERSEDED SAME DAY (user directive, 2026-07-02): the cluster is now THE next structural work and a
HARD GATE — L6 (incl. its TSV-oracle infrastructure; that instruction is WITHDRAWN/PARKED) is PROHIBITED until the
extension behavior is specified → CODED → REGRESSION-TESTED for L1–L5. ★ CONSOLIDATION (same day, user directive
against doc sprawl): the pre-existing `cowork_bounded_context_design.md` (DRAFT, never signed — found to already
specify the request→supply→bounded-recompute protocol, superiorly: "the amount is discovered, not chosen",
requester-owned convergence loops) is THE one cross-layer extension spec; the day's duplicate
`cowork_temporal_extension_contract.md` is KILLED into it (merged: L5 discovery rule + PINNED decision-context
extent [also folded into L5 spec §5.0], L4 decision-relevance sharpening, denial provenance, gate-proof framing,
the §11 acceptance list = the L6 gate). Sequence: SIGN `cowork_bounded_context_design.md` → coding+test instruction
(just-in-time) → verify → resume L6.**

**★★ ENGAGE CRITERIA + RETIREMENT MAP (RATIFIED user 2026-07-02; FOLDED here from `cowork_engage_criteria.md`
2026-07-02 — that file is now a tombstone; this roadmap is the single home).** Replaces "engage deferred
indefinitely" with "deferred until these CRITERIA (date open)"; E3 is its own user-ratification event.
- **Gates (all must hold):** **G1** spine complete: L4+L5 dormant-validated (✅) + **L6 built dormant** + the A-1
  contract as-built deltas closed (D-L3a remains). **G2** (measured by the E0 instrument): zero new class-(b) on the
  case-identity gate; class-(a) per the two-tier policy; **RN vs DCML ≥ legacy on the granularity-robust unit**, all
  presets; correct-abstention scored separately from wrong commits. **G3** perf: p95 ≤ legacy×1.10 (✅ measured
  ~3.7× faster). **G4** coverage sealed + snapshot-strategy declared in advance. **G5** docs synced same increment.
  **G6** user ratifies E3.
- **Staged plan:** **E0** dormant full-spine measurement — ✅ DONE 2026-07-02 (E0/E0′/E0″ arc; G2 NOT met today;
  residuals named: L4 NCT ≈45% of the EXACT cap, bass/inversion ≈42%, θ-calibration [D-FS], per-slice key
  feed-forward, L6). **E1** wire default-OFF (byte-identical proof) → **E2** measured A/B + the **broad-corpus
  pre-engage reference frozen at the engage-candidate HEAD** (generalization test on the expanded library;
  dev/held-out discipline: held-out never tuned against, demotion only by recorded decision — the OQ-C1 split,
  registry `split` field) → **E3** default-ON (user event, one revertible commit) → **E4** retirements (below) →
  **E5** coverage seal + doc flip + deliberate gate re-baseline.
- **Retirement map (nothing retires by silence):** R1 legacy chord competition + Gates A–L (E4, or Stage 5 if
  first — the OWED refactor #2); R2 legacy circular cadence detector (needs the two notation-bridge call-site
  migrations first — gap-analysis Rider 4); R3 `cadencekeyanchor` kept-as-diagnostic through E4, retire post-E5
  review; R4 dual tpc reader → the shared spelling view (rides R1); R5 `resolveKeyAndModeRanked`+`collectPitchContext`
  shrink (P4-redecode; seed S2 at E4; grading baseline may persist as diagnostic); R6 segment-first spine (E4);
  R7 `harmonicfunctionlayer` rename (rides R1); R8 legacy confidence sentinels (rides R1/R5); R9 `chordanalyzer.cpp`
  file-split (OWED refactor #1) AFTER E4 removals — split once; R10 batch-region gate superseded by the robust unit
  as primary (with G2/Stage 5), case-identity + two-tier policy carry over.
- **Wording sweep** ("indefinitely" → "until the criteria above, date open") rides the next docs commit.

**★★ EXTERNAL ARCHITECTURE REVIEW — AMENDMENTS RATIFIED (user, 2026-07-02).** The full external review
(`cowork_architecture_review_2026_07.md` — 18 findings F-1…F-18, no structural fault, no redesign) is delivered and its
ten amendments **A-1…A-10 are ratified**. How they slot into this plan (design/plan-level; none is code; every build
step stays measure-first + ratification-gated):

- **Before the CC implementation↔spec gap-analysis (the next CC task):** **A-1** — the **cross-layer confidence &
  calibration contract** — **✅ WRITTEN (DRAFT, ratification-gated): `cowork_confidence_contract.md`** (the two-class
  model M/P, boundary-normalization rules, the §4 comparison frames stating the §8 override arithmetic once, the C3
  joint-step trigger definition, the D-L5a/D-L3a/D-LEG/D-INV as-built close-outs — F-1/F-16); **A-2** — **engage
  CRITERIA + the retirement map** — **✅ WRITTEN (DRAFT, ratification-gated): `cowork_engage_criteria.md`** (gates
  G1–G6, staged plan E1–E5 with E3 the user event, retirement map R1–R10, the "indefinitely" wording sweep — F-2/F-5).
  Both change what "spec" means for the gap-analysis, hence they precede it. The gap-analysis instruction is
  **✅ READY: `cc_instruction_gap_analysis_spec_vs_impl.md`** (read-only; per-layer gap tables + the five review
  riders + the Rider-6 confidence inventory) — **dispatch after A-1/A-2 ratification**.
  **★ A-1 + A-2 RATIFIED (user, 2026-07-02) → the gap-analysis instruction is DISPATCHABLE.** At ratification the
  user added **E0 — the dormant full-spine pre-engage measurement** (`cowork_engage_criteria.md` §3): measure the
  complete dormant chain L1→L2→L3→**L4-decoder**→L5 end-to-end vs legacy AND vs DCML (Step M covered only the legacy
  substrate; the Phase-5b 86-class-(b) decoder override-duty question is answered here), read-only/byte-identical,
  better/worse reported per respect (root/RN, key S1/S2, modulation, abstention + correct-abstention, class-(b)/(a)
  identity deltas, over-trigger families, wall-time). Needs a small chaining harness — **its own CC instruction,
  after the gap-analysis**; the E0 instrument then serves E2.
  **★ E0 instruction WRITTEN + READY: `cc_instruction_e0_fullspine_measure.md`** (Task A: the default-OFF
  `--dump-fullspine` chaining harness, byte-identity-gated, one local unpushed commit; Task B: the nine-measure
  read-only grading incl. the Phase-5b 86-case override-duty answer and the contract D-INV confidence readout).
  Intended dispatch order: gap-analysis first, then E0.
- **★ THE SCORE/CORPUS CENSUS (2026-07-02): `cowork_score_census.md`** — the once-and-for-all, enumerated-to-closure
  census (two evidence appendices: `cowork_score_census_gt_draft.md` ≈85 distinct GT corpora,
  `cowork_score_census_plain_draft.md` ≈52 score collections). Headlines: **~30 unused DCML DLC sub-corpora are
  format-identical to our parser** (beethoven_sonatas, wagner_overtures, liszt, rachmaninoff, monteverdi,
  bartok, schulhoff-jazz …, style span 1600–1930, zero new tooling); cadence GT exists (algomus ×2, Sears, + cadence
  labels ALREADY in our cloned DCML Mozart TSVs); TAVERN's dual-annotator data = A-1 Class-P calibration material;
  KMT targets the key/modulation residual; HookTheory/CoCoPops/OpenEWLD = the score-aligned jazz/pop GT path.
  **Standing process rule instituted:** "a new corpus was discovered" is a **census defect** — add its CONTAINER and
  re-enumerate to closure; yearly re-sweep (mirdata loaders + ismir/mir-datasets + new ISMIR). Decision tiers G/J/C/S/X
  proposed in census §5 (user disposes); CC riders in census §6 (registry schema + the clone/pin instruction).
  **★ Standing trigger (user, 2026-07-02): idiom re-discovery rides each corpus wave.** After each material corpus
  change (each wave; the yearly census re-sweep), re-run the `idiom_discovery/` pipeline under the v1 protocol
  (multi-seed stability, cap-robustness, source-leakage/ARI confound test) on the **dev set + external research
  corpora only** (held-out material excluded — discovery outputs become shipped parameters). Primary question:
  do the five ratified idioms **reproduce**? Falsifiable v2 edges: does #5 Chromatic-coloristic split (the K=6
  candidate) under the new chromatic mass; where do Wagner/Liszt land (#2 vs #5 — the era≠axis re-test); does
  early-modal material (Monteverdi/Sweelinck) separate or fold into #4. A changed cluster set is a **ratified
  taxonomy-revision event** (it propagates to StyleTag values + the vocabulary entry mapping — post-swap it is a
  migration, not a relabel). Plan line only — the instruction is written just-in-time after the triggering wave.
  **★ Wave-1 instruction WRITTEN + QUEUED (2026-07-02): `cc_instruction_corpus_wave1_dlc_onboarding.md`** — complete
  the DLC container (onboard the ~30 missing sub-corpora, hash-pinned, research-tier, per-style baselines, Tristan
  presence check), registry v2 schema, and the Mozart-TSV cadence-label inventory (Task C). **Single-CC sequencing
  (user, 2026-07-02): one CC does both tracks — dispatch Wave 1 AFTER the E0 report lands** (same worktree, no
  parallel instructions). Gate untouched by construction (no `src/`, frozen gate corpus byte-untouched,
  end-of-run 53/24/53 reproduction as the no-contamination proof).
- **Corpus expansion (user-ratified 2026-07-02 — jazz + Wagner-class + more non-Bach/non-Baroque in general):**
  onboard **DCML `wagner_overtures`** (v2.1, Distant Listening Corpus — exists [verified]; Tristan-Prelude presence to
  confirm at the repo) as **research-tier** stress material via the existing sub-repo pipeline (clone + pin +
  validation script per `tools/REPRODUCIBILITY.md`); inventory the rest of the Distant Listening Corpus for further
  late-romantic/chromatic sub-repos; identify **gate-grade jazz GT** (candidates from the idiom study: JHT, ChoCo,
  McGill Billboard — currently research-only) and name its validation path (**A-7**: apply the "empirically-unvalidated"
  mark to the Jazz preset + idioms 3–5 until then). New corpora are research/measurement material first — the frozen
  Bach gate corpus stays the regression gate until a re-baseline is deliberately ratified.
- **Metric:** **A-8** — move the gate to the **granularity-robust union-of-boundaries unit** (already built, L0–L1
  primitives), keeping the case-identity + two-tier class-(a)/(b) policy. Sequenced with Stage 5 (it is that stage's
  mandated metric), may be pulled earlier as a deliberate re-baseline event.
- **Capability track (Tristan-derived; design-first, measure-first; after or interleaved with L6 + the recognition
  consumer):** **A-3** dominant-implication key evidence in the L3 emission (L3 §15); **A-4** cadence-less
  key-confirmation channels + enharmonic key-span identity in L5 §5.3 (L5 §15); **A-5** the phrase-gate fallback for
  flat boundary profiles (L5 §15). The **NCT-filter L4 lever** (step 4 above) and the **voice-leading axis** are
  confirmed by the review as the known path to the romantic repertoire — priority upgraded, sequencing unchanged.
- **At the recognition-consumer build:** **A-6** — decide the progression-knowledge store question (fold the §5.0
  pairwise motions into the Vocabulary, or two stores by declared design) — recorded in
  `cowork_progression_schema_design.md`.
- **Riders (fold into the next natural doc/product passes):** **A-9** product stance for dense-abstention output +
  out-of-tonal-domain input; **A-10** L1.5 consolidated ownership page, the L4 membership tie-breaker recorded as an
  idiom-calibrated constant, **B-swap readiness pinned as a design property**, optional STATUS entry header schema.

---

*(The "upstream-first" snapshot below is the 2026-06-21 state — now **superseded** by the current-state table above
(L3–L6 are built; the encyclopedia, idioms, and voice-leading axis are new). Kept for the L1/L2 build evidence; the
Stage 0–7 plan further below is the original 2026-06-10 decoder-era roadmap, Stages 0–2 done and Stages 3–7
reorganized into the per-layer rebuild — preserved for traceability and the still-OWED items.)*

**★★ UPSTREAM-FIRST LAYER REBUILD (2026-06-21) — the per-layer execution of the ratified target.**
The 4-layer target (`cowork_target_architecture.md`) is being built upstream-first, one layer at a
time, each with its own design → audit → build → coverage cycle:
**note model (L1) → change-point slicing (L2, BUILT — isolated) → per-slice analysis with context (L3) → grouping (LN).**

| Layer | Status | Evidence (verify) |
|---|---|---|
| **L1 — lossless tie-resolved NOTE MODEL** (`composing/analysis/notemodel/note_model.{h,cpp}`; derived views `weightedPcView`/`soundingAt` in `engravingbridge`) | **✅ DONE + RATIFIED + PUSHED (2026-06-21)** | `edd33901ed` standing oracle-root metric tool (+15 tests) · `e30bb45a4f` note model + views · `4055f89082` branch-coverage close (test-only). `origin/master` = `e470e2667e`. Gate: T1–T8 functional + T9–T14 view-branch tests; composing 559 / notation 57 / snapshots 11/11; new-code branch coverage 100% (note_model.cpp + weightedPcView). **Behavior change (not byte-identical):** tie de-inflation + uncapped overlap moved the oracle-root metric **+3/+1/+1 charged** (KEY tier flat, FLOOR byte-flat, BIR −2/+1/−2), ratified as a correct-upstream/frozen-downstream wobble that re-tunes at L3 — proven 100% tie/cap-attributable via a legacy reproduction mode. Reports `cc_layer1_impl_report.md` / `cc_layer1_coverage_report.md` (HELD). |
| **L2 — change-point slicing** (`composing/analysis/slicing/slicer.{h,cpp}` — the deterministic constant-tonal-sonority slicer over the note model) | **✅ DONE + RATIFIED + PUSHED (2026-06-21)** | `changePointSlices(noteModel)` = covering/lossless `[start,end)` partition; boundaries at every eligible onset AND release (eligibility = L1's `plays && visible && staffEligible`, read not re-decided); slice identity = eligible note set; all-rest interior = explicit empty slice; **zero interpretation, no grace/tuplet special case** (verified at source). **Not wired in** (segment-first spine still drives analysis until L3). Gate: `slicer_tests.cpp` 13 tests (audit §3 functional set + edge/eligibility) — composing 572 / notation 57 / snapshots 11/11 (no golden refresh) / BIR-oracle byte-identical by construction (only production touch is a 6-line doc comment; module unreferenced by production); **100% measured line+branch coverage of `slicer.cpp`** (no unreachable branches). `origin/master` = `e470e2667e`. Report `cc_layer2_impl_report.md` (HELD); design `cowork_layer2_slicing_design.md` + audit `cc_layer2_audit_dossier.md`. |
| **L3 — per-slice analysis with context** (scoring) | **NEXT** | this is where the L1 +3/+1/+1 oracle wobble re-tunes; L3 wires in the L2 slicer (over-grab dissolution) and analyzes each slice with look-around context. |
| **LN — grouping for display** | pending | — |

The segment-first spine (`greedyExpandSegmentation` + Pass-1/2/2b) **still runs and drives analysis**,
now consuming `weightedPcView` (it is **transitional**, retiring when L2/L3 land). This upstream-first
arc interleaves with — does not replace — the Stage 0–7 plan below.

---

## Stage 0 — Hygiene and honest ground truth *(zero behavior change, cheap)*

**✅ STAGE 0 COMPLETE (2026-06-10).** Commits: `7bc1609159` (0.1 docs), `a236a0ff21`
(0.2/0.3/0.5/0.6 — kTemplateCount across SIX sites incl. the bassIsTemplateChordTone
bounds check, dead fnCtx fields removed, FP tie policy, divergence docs), `70fd8a686b`
(0.4 — junk files were tracked, swept into an old feature commit; removed + gitignored by
glob, U+F03A names; no generator exists, post-build proof clean). Gate 0→1 passed:
416/416 · 52/52 · 11/11, zero diffs, BIR 13/7 both presets.
**Doc pass complete `af39f28179` (2026-06-10):** CLAUDE.md kTemplateCount + cap truth;
scoring_model §2/§4/§5/§6/§8 reconciled with the Stage-1b verified inventory; handoff
Jazz re-attribution; cap archaeology verdict = **2.5/0.6 never set in committed code**
(aspirational since field introduction `46c76ad67f`; only an uncommitted Baroque
cap=1.0 experiment ever existed). **Residual:** `chordanalyzer.h:402–409` field
doc-comment still claims "Baroque: 2.5 / Jazz: 0.6" and lists removed signals
(nextRoot/consecutive/recentRoot/weakBeat) — 2-line comment fix to ride with the next
code-touching commit.

Make every instrument we will rely on later trustworthy. All items byte-identical.

| # | Item | Source | Verify |
|---|------|--------|--------|
| 0.1 | Doc pass: clear stale `explorationMode`-as-live references in ARCHITECTURE.md (~L368/987/1026–28/1314) and `docs/layer_architecture_audit.md`; commit the audit doc (currently untracked) and the long-standing uncommitted doc edits | pending since `e7d4ba2b1a` | docs grep clean; git status clean for docs |
| 0.2 | Remove dead `HarmonicFunctionContext.keyFifths`/`keyMode` write-only fields | Part 2 Q4 | grep: no references; byte-identical tests |
| 0.3 | Shared `constexpr size_t kTemplateCount` used by the template array, `kDiagTemplates`, all three score matrices, `kMasks` — kills the silent stack-overrun class | Part 2 Q3.3 | compile-time sizes derived from one constant; tests green |
| 0.4 | Delete repo junk (root `"s -ExecutionPolicy…"` file, `C:tmpbuild_out.txt`); confirm `ai-assistant/` stays out of scope | Part 2 Q4 | git status clean |
| 0.5 | Document FP tie policy in `scoring_model.md` (exact-double comparisons + `tiePriority` ordering; no epsilon) and the platform/compiler fragility caveat | Part 2 Q6 | doc section exists |
| 0.6 | Unify or explicitly document `onsetBoundaryThreshold` (batch hard-coded 0.25 vs bridge config) and the duplicated region-collapse logic (`regionanalyzer.cpp:497`/`:694`) | Part 2 Q1.5 | comment or unification; byte-identical |

**Gate 0 → 1:** all tests green, BIR unchanged, working tree contains no unexplained files.

---

## Stage 1 — Pin current behavior *(tests first — verify each existing layer/gate before anything is built on or replaced)*

This is the core of "make sure each layer/gate/method is correct before we build upon them."
These tests are also the **differential-test harness for the Stage 3 decoder migration**:
each gate's pinned behavior is the proof obligation when the decoder later subsumes it.

| # | Item | Source | Verify |
|---|------|--------|--------|
| 1.1 | ✅ DONE `6101a9b2c5` — 48 tests in `postscoringgates_tests.cpp` (composing 487/487). Survey produced the definitive gate inventory (`cc_stage1b_report.md` §1, verified by Cowork on F1 + preset caps). Findings F1–F8: **B/C/D are dead code** (A's fast path always wins — verified in code by Cowork); shared outer guard (suspicionMargin=0 / distinctPcs<3 kills ALL gates); Gate J runs LAST; mixed live/captured winner reads in H/I/K/L; Gate F missing quality/pcWeight guards; G-E threshold-free pull + duplicate push; post-gate unsorted results[]. All → Stage-3 obligations + doc pass | Part 2 Q5.1 | each gate individually toggleable in test; count documented |
| 1.2 | ✅ DONE `757efa5dbf` — 23 tests in `functionlayer_tests.cpp` (composing 439/439). Findings F1–F5 in `cc_stage1a_report.md` §3: F1 §2 Sus4♭5/HalfDim "identical PC sets" wording → doc pass; F2 post-bonus guard first-wins tie scan + F5 threshold-gated diff-root append → Stage 3 obligation list; F3/F4 pinned | Part 2 Q5.2 | scoring_model §8 constraints each have a pinning test |
| 1.3 | ✅ PARTIAL `4656f43258` — pinned: absorbShortRegions root-agnostic (G2: order-coupled with coalesce), inline same-root merge fire/block, clean-changes preservation. **Gate 1→2 exceptions (NOT-PINNED, become HARD obligations when Stage 3 touches these passes):** coalesceShortSameRootRuns, Pass 2/2b boundaries + minGapTicks floor, sub-region bassIsStepwiseToNext (verified-by-inspection only) — emergent triggers, indirect corpus coverage; reasons in `cc_stage1c_report.md` §3 | Part 2 Q5.3 | synthetic region fixtures |
| 1.4 | ✅ DONE `4656f43258` — keyresolver: ranked output, piece-start shortcut (G3: size-1 list!), insufficient-data fallback, partial-signature fix both directions, **promoteWinnerInPlace confidence wart pinned with real numbers (G1: promoted winner carries ≈0.07 — THE Stage-4 rebaseline anchor)**; harmonicsegmenter Round-1 anchors (Round-2/fillGap NOT-PINNED, code-verified). Findings G1–G5 → Stage-4 list (G1/G4/G5), Stage-3 list (G2). Infra: composing tests now load .mscx (engraving env copy in tests/environment.cpp) | Part 2 Q5.4 | |
| 1.5 | ✅ DONE `6101a9b2c5` — all four pinned: Gate J bwv110.7 end-to-end, Sub-9a ordering test (decoy proves historical-bug visibility; arithmetic verified by Cowork), Δ=+7b end-to-end shape (bwv320 mapping), Iter 92 both bugs. Pedal already pinned by 8 existing tests (cross-referenced) | Part 2 Q5.5; audit doc rec. | removing the fix fails the test |
| 1.6 | ✅ DONE `bb48394b52` — 54 unittest tests in `tools/tests/test_metric_scripts.py` + hand-derived fixtures (README with derivations). All claims [code]/[probe]-tagged; non-vacuousness mutation check. Findings F-1 (`extract_quality` misses letter-`o` dim), F-2 (Ger65/N6/It6 mis-parses), F-3 (the "24" is NOT produced by characterise_bir_false.py — provenance untraced) → bundled into Stage 2.2's single re-baseline event | Part 2 Q6 | known-input/known-output fixtures in tools/tests |
| 1.7 | ✅ DONE `757efa5dbf` — exact-tie (tiePriority, rootPc fallback) + 0.02 near-tie FP canary, in `functionlayer_tests.cpp` | Part 2 Q6 | |

**Gate 1 → 2: ✅ PASSED 2026-06-10** (commits `757efa5dbf`, `6101a9b2c5`, `4656f43258`,
`bb48394b52`). Composing 416→498 + 54 Python metric tests. Documented exceptions
(1.3 NOT-PINNED: coalesceShortSameRootRuns, Pass 2/2b boundaries, sub-region
bassIsStepwiseToNext) become hard obligations when Stage 3 touches those passes.
Metric-bug decisions (1.6 F-1/F-2/F-3) deferred into Stage 2.2's re-baseline.

---

## ⚠⚠ META-PRINCIPLE (2026-06-13, two converging verified findings) — PRECISION LIVES IN EMISSION, NOT SEARCH

Two consecutive design investigations falsified an "elegant structural fix," for the SAME
reason:
- **Beam-widening (3.2 design):** a wider/global chord decode does NOT fix Δ=+7a — the
  transient wrong root is the genuine global optimum; search optimizes the objective the
  emission defines.
- **Key-as-path (Stage 4 design):** an HMM key path does NOT fix the S2 bulk — ~85% are
  Class-B "emission consistently prefers the wrong key, correct key never rank-2"
  (bwv244.54: D-minor ×29, F-major never rank-2; 51.6% of S2 has the right key outside
  rank-2). A modulation penalty only adds stickiness; it cannot recover an absent candidate.

**The principle:** inference STRUCTURE (search / path / global decode / beam) cannot move
an error the EMISSION model consistently prefers. Combined with the headroom dossier (95%
of root errors are functional, not vertical), the conclusion is firm: **precision lives in
(a) the emission model — the per-region/window scorer: chord templates, key profiles,
features — and (b) the functional-labeling layer (Stage 6). It does NOT live in the
decode/search machinery.** The part-1 lattice-decoder vision was right as *consolidation*
(the oracle/competition factorization is clean) but its *precision promise* (global decode
fixes hard cases via inter-region revision) is falsified. **Future stages must not reach
for a search/decode fix where the emission is the cause** — verify which it is first
(Method: derive against real candidate margins, as 3.2/Stage-4 did).

---

## ⚠ PRECISION-HEADROOM RE-GROUNDING (2026-06-13, Cowork-verified) — reshapes Stages 4–6

`cc_precision_headroom_dossier.md` measured the REAL (DCML-only, Default config, unfiltered)
error structure. Verified findings (Cowork: the load-bearing identity is structurally exact;
the tooling reproduced the documented A3 27.6%/15.4%/6.3% baseline):

- **95.2% of root errors are functional, not vertical.** `root_err 2706 = all_differ 2576
  (neither we nor music21 reach DCML) + music21_dcml_agree 130 (vertically fixable)`. The
  music21-filtered "13 BIR=false" gate measures only the **4.8% vertical slice** — it has
  optimized a tiny reachable corner while 95% of the root-error mass (cadential 6-4,
  suspensions, applied roots — functional readings) was invisible to it.
- **key_disagree (27.9%, largest axis) splits 63% tonicization-label gap** (root+global-key
  already correct — Stage 6 secondary/tonicization labels, the single biggest slice S1=17.7%,
  LOW regression risk = pure-add labels on correct readings) **/ 37% genuine key error**
  (Stage 4).
- **Headroom by layer:** Stage 6 functional ~35–42% · Stage 4 key path ~20–24% · Stage 5
  emission-reweight 1.3% batch / ~6–7% section (Stage 5 is the *fitter/enabler*, small direct
  yield) · beam/search ≈ 0 (confirmed not where precision lives).

**Re-grounded ordering (recommended, pending ratification):** finish 3.4/3.5 consolidation
(beam-1) → **the DCML-only + granularity-robust METRIC is the immediate next instrument**
(Cowork refinement: it gates Stage 4's AND Stage 6's measurability, not just Stage 5's fit —
"instruments first," Method A) → **Stage 4 (key path + KeyArea) leads the back half** (unlocks
the largest functional slice) → **Stage 6 co-developed** on KeyArea output (S1 is the
low-risk/high-yield first target) → **Stage 5 fitter last**. Beam shelved with a concrete
revisit trigger (dossier §3.3: a non-monotone forward edge where global-best ≠ greedy AND
global-best matches DCML). Joint segmentation deferred past Stage 5.

---

## Stage 2 — One pipeline, one truth *(close the measurement blind spot and path divergences before any redesign)*

After this stage, the measured pipeline IS the user pipeline and the diagnostic tool IS the
production scorer. Without this, Stage 3 results can't be trusted ("no surprises").

| # | Item | Source | Verify |
|---|------|--------|--------|
| 2.1 | ✅ DONE `eeca0dea30` (rider) + `8598cbd245` (move) — `analysis/section/sectionanalyzer.{h,cpp}` (Option D: Pass-0 regions injected, composing stays config/notation-agnostic — chosen for the layer shape Stage 3/E needs and so 2.2's batch can pass its own regions). Byte-identical: snapshots 11/11 zero diffs, Baroque 13. Cadence/pivot tests stayed in notation tests (include updates; allowed alternative). Dead weight/pitch-context shims found (no live caller) — Stage-2 cleanup list. **Jazz "nondeterminism" investigated en route: M3 = shared `tools/corpus` contamination (FAILED-worker stale files + skip_cpp reuse + no preset guard), NOT C++/Python — both proven deterministic (Jazz 7, Baroque 13; 0/353 double-regen, retroactively validating all historical A/B checks).** `cc_jazz_nondeterminism_report.md` | Part 2 Q1.1, Q2.1 | byte-identical on snapshots + corpus; Dependency Rule restored |
| 2.2a | ✅ DONE `e20894c75b` (+ docs `6f1e3dc807`) — per-preset dirs (`tools/corpus/{baroque,jazz}/`), clean-slate + manifest with per-score sha256 fingerprints, fail-loud (regen exit≠0 on incomplete; characterise exit 2 on missing/incomplete/contaminated manifest), `--corpus-dir`/`--wir-dir`; 63 Python tests (+9 incl. the exact M3 scenario → ERROR); CLAUDE.md/BUILD_AND_TEST.md synced. Verified: Baroque 13 + Jazz 7 with exact identity sets; contamination probe errors. **Interim gate RETIRED — "Baroque ≤ 13 / Jazz ≤ 7" regain plain meaning.** Deferred follow-up: `analyze_inversion_errors.py` (secondary metric) still reads legacy flat dir — `--corpus-dir`-ify with 2.2 | M3 fix design (#1+#3) | both presets regenerate side-by-side: Baroque 13 + Jazz 7 with known identity sets; contamination scenario now fails loudly |
| 2.2 | **RESOLVED BY MEASUREMENT (2.2-i A/B, `cc_stage2_2_ab_dossier.md`) — decision: the gate STAYS at batch granularity.** The blind spot was granularity, not identity: section-level barely changes analysis (4 genuine root changes corpus-wide: 3 regressions + 1 both-wrong, all on thin gap/split slices) but the measure-aligned regions surface ~252/238 per-beat disagreements the coarse regions masked (rn corroborates: root_agree flat, all delta in root_err). **The batch gate undercounts user-visible per-beat root errors ~7×** — quantified, documented; granularity-robust metric is now MANDATORY at Stage 5. F-3 closed: 24/13 & 35/7 = `analyze_inversion_errors.py` three-way split; characterise reproduces the 13/7 half. **2.2-ii SHIPPED `75a5815960`+`c7aeb24ae1`+`465450bf49`+`9e52147b04` (gate-neutral verified: 13/24, 7/35 exact identity sets, flag-off byte-identical, 65/65 Python):** `--section-level` diagnostic flag (default off), F-1 letter-`o` fix + F-2 It6→fallback routing (honest residual: dcml_parser still assigns It6 a tonic root — documented, out of scope), Rider 1 (analyze_inversion `--corpus-dir` + line-93 fix), Rider 2 (dead shims removed), docs. Cross-corpus rn numbers (27.6%/53.8%) marked pre-F1-stale; re-measure at Stage 5 entry. Rider 3 (cadence schema) deferred to Stage 6 | Part 2 Q1.1; Stage-1d F1–F3; dossier §6 | gate numbers unchanged (13/24, 7/35 + identity sets); flag-off byte-identity; updated metric tests green |
| 2.3 | **diagnoseChord becomes a view into production**: replay `applyHarmonicFunction` on the real snapshot (with a context dump), or stamp every dump "oracle-only — excludes progression signals" at minimum. Preferred: full replay | Part 2 Q1.4; principle #2 | a Δ=+7b-style case diagnosed via diagnoseChord shows the same winner as production |
| 2.3b | **Wire temporal context into `batch_analyze --diagnose-measures`** (follow-up from 2.3): the diagnose tool currently replays the production pipeline with NULL temporal context (region-in-isolation) — correct and now explicitly bannered in the dump, but rcb-class investigations (Δ=+7 family) need the threaded inter-region context the batch run actually used. Reconstruct it from the run, don't fabricate. Low urgency; do before any Δ=+7a investigation relies on the tool | 2.3 report §2.4/§6 | a Δ=+7a-class dump shows the real rcb feed |
| 2.4 | Document/decide P4 divergence: either feed P4 the accumulated context (pre-pass) or document cold-context as the contract; same decision for bridge cold-predecessor (`findTemporalContext` nullptr context). A full forward pre-pass is its own design — decide, don't drift. **Scope grown by 2.2-i findings:** (a) Pass-0 prefs divergence — notation `analyzeHarmonicRhythm` uses default chordPrefs + `excludeLookAheadOnDenseStart=false` vs batch preset prefs (dossier §7.2); (b) **section-layer preset leak** — `inferGapRegion` analyzed gap slices with `kDefaultChordAnalyzerPreferences` regardless of preset (dossier §2). **Causal hypothesis FALSIFIED by the 2.4 probe**: the 3 Baroque regressions are structural (measure-split/gap-insertion), not pref-caused — Baroque prefs ≈ defaults so the leak was inert there; it was live under Jazz (bwv5.7 healed). Leak fixed in 2.4 (V2) on consistency grounds | Part 2 Q1.2/1.3; dossier §2/§7 | written decision in ARCHITECTURE.md |
| 2.5 | Profile P3 status-bar path (re-analysis per query, no caching) — capture numbers before decoder cost is added | Part 2 Q6 | profile note committed |

**Gate 2 → 3:** snapshots green on the moved code; new corpus baselines committed and
explained; diagnoseChord output verified against production on ≥3 historical cases.

---

## Stage 3 — Phase E as a decoder *(the part-1 core recommendation, made incremental)*

> **Design ratified (Cowork, 2026-06-12), base commit `3aa9db7676`.** `docs/decoder_design.md` is the
> ratified Stage-3 design (one mandatory correction applied: `completeTriadInversionBonus` is
> a temporally-gated emission, not pure emission — §3/§6; all seven Open Questions DECIDED).

Replace greedy left-to-right commitment with lattice + global decode. Incremental, with a
byte-identity bridge so there is a no-surprise verification gate at every step.

| # | Item | Source | Verify |
|---|------|--------|--------|
| 3.1 | **Decoder skeleton, beam = 1**: per-region candidate lattice from the existing oracle output; transitions = existing progression signals (rcb, resolution, wSeq, wDim, steps). **Hard gate: beam-1 must reproduce the current pipeline byte-identically** (it is the same greedy argmax, restructured). **Design opportunity from the 2.5 baseline (`docs/perf_p3_baseline.md`): "decode once, query many."** P3 currently re-runs full Pass-0 per status-bar query (≈99% of a 33–215 ms median / up-to-7 s tail cost); a per-score lattice computed once and queried per tick would make P3 dramatically FASTER post-decoder while simultaneously resolving the D-P4/D-BRIDGE cold-context contract (the per-tick path reads the decoded path state). Stage 3 design must evaluate this — it converts the decoder from a cost into the P3 performance fix | Part 1 rec. 1; 2.5 baseline | 0/353 corpus diff, all snapshots, BIR unchanged |
| 3.2 | ⚠ **THESIS FALSIFIED (3.2 design, 2026-06-13, Cowork-verified against the independent June-9 redesign_plan numbers): a wider beam does NOT fix Δ=+7a.** The transient micro-region is the HIGHEST-scoring node (locally correct — DCML root absent from its tones); the continued-root wrong path is the genuine global optimum (greedy 5.775 > correct 5.600 on bwv102.7; gap = rcb 0.40 − margin 0.225), so a global decode finds the same path greedy does. Re-ranking can't fix it — only re-weighting (Stage-5 rcb reweight + forward-completion edge) or joint segmentation can. Δ=+7a REMOVED from the 3.2 win column → Stage 5. decoder_design §11's "low-scoring transient" premise was wrong (Cowork ratification miss). **Strategic consequence under review: beam-widening's marquee justification is gone; gate-folding + edge-reweighting are beam-1 operations — see handoff.** Original (now void) text: ~~Widen beam… expected wins Δ=+7a (bwv102.7, bwv261) — the "C2/bwv320-class rcb near-tie" row in decoder_design.md §11 cites a DEAD example (bwv320 m27 = the Gate-R-fixed Δ=+7b instance, same tick; reconciled 2026-06-12); that class has no known live instance, so do not promise it.** Δ=+7b trio = must-not-break | Part 1; 2026-06-12 reconciliation | per-case table; no hard-stop regressions at level 0 |
| 3.3 | Migrate oracle temporal signals (resolutionBonus + 4 inversion bonuses, chordanalyzer.h:329 debt) into transition scores; **revisit Gate R's `basisDep ≤ 0` proxy in the same change** (documented coupling) | Part 2 Q2.2; audit F1/F6 | Stage-1 pinning tests green or consciously re-baselined |
| 3.4 | Retire gates A–L one at a time: a gate is removed only when the decoder reproduces its pinned fixes (Stage 1.1 tests are the proof obligations). Gates J and R expected to survive longest (structural, healthy). **Stage-1a obligations:** the post-bonus quality-guard winner scan is first-wins on exact ties (ordering sensitivity), and the diff-root append never appends sub-threshold candidates — the decoder must either reproduce or consciously re-decide both (`cc_stage1a_report.md` F2/F5) | Part 1; audit F7 | per-gate differential report |
| 3.4b | Remove dead Gates B/C/D (provably unreachable — stage1b F1) as part of the gate-retirement work, NOT before (their removal is byte-identical but belongs to the deliberate per-gate retirement audit) | stage1b F1 | byte-identical removal commit |
| 3.5 | Split `chordanalyzer.cpp` along the now-real layer seams; rename iteration-vocabulary APIs (`applyIter8691Pedal` → descriptive names) — the split is motivated here, not before | Part 2 Q3.1/3.2 | file map in ARCHITECTURE.md |

**3.2 ↔ 3.4 ordering (Q3 DECIDED, Cowork ratification 2026-06-12).** For any gate that mutates
root/quality/bass identity, **3.4 retirement of that gate leads 3.2 beam-widening past it** —
the identity entering the lattice must already be gate-corrected before the beam widens, since
the gate's mutation feeds backward edges. The table's numeric order is the default track; this
is a per-gate exception (structural gates that never mutate a committed identity, e.g. J, do not
force the re-order). See `docs/decoder_design.md` §12 sequencing note.

**Gate 3 → 4:** decoder is the production path at all quality levels; gate count reduced;
corpus metrics ≥ Stage-2 baselines on both presets.

---

## Stage 4 — Key as a path *(mode/key correctness)*

| # | Item | Source | Verify |
|---|------|--------|--------|
| 4.1 | Key HMM over existing 252-candidate window scores (emissions = raw scores, transitions = circle-of-fifths modulation penalty). Replaces per-window argmax + `promoteWinnerInPlace` hysteresis; do not consume `normalizedConfidence` (known unreliable) | Part 1 rec. 2 | keyresolver pinning tests (1.4) re-baselined; corpus key_disagree measured before/after |
| 4.2 | `KeyArea` spans emitted from the decode (wanted by `unified_analysis_pipeline.md` for modulation-aware RN) | Part 1 | spans consumed by annotation emitter |
| 4.3 | Evaluate two-level (key path × chord path) joint decode vs sequential — only if 4.1 leaves measurable key-driven chord errors | Part 1 | decision note |

*Note: Stage 4 may be promoted ahead of Stage 3 if a live key-failure case emerges; the two
are independent.*

---

## Stage 5 — Fit the weights *(stop hand-tuning)*

| # | Item | Source | Verify |
|---|------|--------|--------|
| 5.1 | Calibrate emission/transition constants against aligned DCML corpora (structured perceptron or coordinate search), Baroque/Jazz presets as separate fits; existing hard stops as constraints | Part 1 rec. 3 | held-out corpus split; per-preset before/after table |
| 5.2 | Re-baseline BIR/rn_agree; retire constants that fit to zero. **MANDATORY (was optional): granularity-robust metric definition** — the batch-granularity gate undercounts user-visible per-beat errors ~7× (2.2-i dossier §3); the fitting objective must not inherit that bias. **Equally mandatory: a human-only (DCML-only) gate variant** — the current "genuine" filter requires music21∩DCML agreement, i.e. an ALGORITHM adjudicates which DCML disagreements count (music21 is NOT ground truth — user mandate 2026-06-10; see corpus audit C2). The fitting objective must not be filtered by another analyzer's opinion. **Coverage fact (hygiene pass): only 326/353 gate chorales have WiR human annotations at all — 27 scores can never produce a "genuine" error.** The gate's true shape: human-adjudicated coverage of 326, music21-filtered, batch granularity — all three qualifiers must be addressed here. Also re-measure the cross-corpus rn numbers (27.6%/53.8% are pre-F1-metric, stale). **Stage-3.1b added measured evidence:** the P3 window-vs-whole-score A/B (`docs/p3_granularity_ab_3_1b.md`) shows the granularity choice changes per-tick DCML accuracy by **double digits** (window-vs-whole-score combined 59/41 root-correct, Mozart 35/65) — the finer per-tick view is more DCML-accurate, the coarser section view is self-consistent with the chord track; the granularity-robust metric and the P3↔P1 product question are both decided here, not by cache architecture | Part 1; dossier §3/§6; corpus audit; p3_granularity_ab_3_1b | STATUS.md baselines |

---

## Stage 6 — Functional layer *(functional chord correctness — E4)*

| # | Item | Source | Verify |
|---|------|--------|--------|
| 6.1 | Sequence labeling over the decoded chord+key paths: T/S/D states, cadence patterns (consuming the Stage-2.1 relocated cadence detector), secondary dominants, aug6, Neapolitan, tonicization-vs-modulation from KeyArea spans | Part 1 rec. 4; ARCH §5.6 | rn_agree / key_disagree movement vs frozen 27.6% / 15.4% |
| 6.2 | Consolidate the three scattered quality-from-key feedback sites (sparse refinement, forceChordTrackQuality, display stabilization) into this layer | Part 2 Q2.4 | one home; pinning tests green |
| 6.3 | Revisit closed "convention gap" buckets (Maj→Dom7 implied sevenths, Min↔Maj thirdless) — now addressable as functional-label decisions, not sonority changes | Part 1 §2.3 | bucket counts before/after |

---

## Stage 7 — Optional ceiling

| # | Item | Source |
|---|------|--------|
| 7.1 | Neural proposal model (AugmentedNet/ChordGNN/RNBert class) behind §2.2 interfaces, decoded by the same lattice machinery; rule-based remains default | Part 1 rec. 5 |

---

## Traceability — every review conclusion → stage

| Conclusion (part 1 = A, part 2 = B) | Stage |
|---|---|
| A: Phase E = decoder, not feature pack | 3.1–3.4 |
| A: key as HMM path / KeyArea | 4.1–4.2 |
| A: weight fitting vs DCML | 5 |
| A: functional labels as sequence labeling | 6.1 |
| A: keep oracle + heuristics as features; quality level = beam width | 3.1, 3.2 |
| A: §2.14 reconciliation | done 2026-06-10 (docs) |
| A: neural hybrid optional | 7.1 |
| B: analyzeSection in notation / batch metric blind spot | 2.1–2.2 |
| B: diagnoseChord second scorer | 2.3 |
| B: missing unit tests (gates, bonuses, segmentation, keyresolver, pinned bugs) | 1.1–1.5 |
| B: metric scripts untested | 1.6 |
| B: kTemplateCount silent-overrun | 0.3 |
| B: dead fnCtx fields | 0.2 |
| B: repo junk + untracked audit doc + stale doc refs | 0.1, 0.4 |
| B: FP tie policy + tie-stability test | 0.5, 1.7 |
| B: P4/bridge cold-context divergence | 2.4 |
| B: P3 performance | 2.5 |
| B: oracle temporal signals debt + Gate R coupling | 3.3 |
| B: chordanalyzer.cpp size + iteration-named APIs | 3.5 |
| B: quality-from-key scattered (3 sites) | 6.2 |
| B: onsetBoundaryThreshold + region-collapse duplication | 0.6 |

*No review conclusion is unassigned.*

---

## Relationship to the existing phase roadmap (COWORK_HANDOFF "Roadmap")

- Phase A/B/C residuals classified "Phase E only" (Δ=+7a, B1 mMaj7, A2 dominant-in-minor,
  C1 schumann, C2 bwv320) map to Stage 3/6 deliverables — they are the decoder's acceptance
  cases, listed in 3.2.
- B4 (6th-chord templates) and other template work stay frozen until Stage 5 (fitting makes
  template ambiguity tractable).
- The "do not" rules (no new gates, no threshold widening, no rcb gating) remain in force
  through all stages; Stage 3.4 is the only sanctioned way gates change.

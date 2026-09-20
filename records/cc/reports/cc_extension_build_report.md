# CC report — the BOUNDED-CONTEXT / SELECTION-EXTENSION build (L1–L5, the L6 gate)

> **Status: HELD for Cowork ratification.** Read-heavy build against the SIGNED design
> `cowork_bounded_context_design.md` (2026-07-02) + the v2 gap report `cc_gap_analysis_v2_report.md`.
> All commits are local, fork-only, unpushed. No θ, no constant tuning, no inference fixing.
> The L3 activation A/B numbers (§2) are HELD — activation is a SEPARATE ratification (it changes
> live range-query behavior). L6 un-parks only on Cowork's ratification of this report (+ the user's
> separate L3-activation decision).
>
> **HEAD after this build:** `30b23d9f5c`. Base at dispatch: `246e4542e8`.
> **Suites (final):** composing **1015/1015** (2 disabled; was 998 — **+17** new tests), notation
> **53/53**, pipeline_snapshot **11/11 — NO golden refresh**. All green.
> **Corpus gate:** Baroque **53** / Jazz **24** / Default **53** — **EXACT identity sets** (not just
> the integer), diffed against the CLAUDE.md gate sets, zero delta on all three presets.

---

## §0 — Task 0: the consolidated docs commit (docs-only)

**0a — `d39da15d95`** `docs(consolidation): session-21 Cowork docs batch + spec amendments; delete tombstones/superseded/sensitive drafts`
- **Added** (untracked → tracked): `cowork_architecture_review_2026_07.md`, `cowork_confidence_contract.md`,
  `cowork_score_census.md` + `_gt_draft` + `_plain_draft`, `cowork_polyphony_phrase_harmony_research.md`.
- **Updated** (modified): `cowork_bounded_context_design.md` (SIGNED), `cowork_layer{3,4,5,6}_design.md`,
  `cowork_phrase_boundary_design.md` (L1.5 bounded-context stanza), `cowork_progression_schema_design.md`,
  `docs/score_inventory.md` (both pending sections), `docs/implementation_roadmap.md`, `COWORK_HANDOFF.md`,
  `STATUS.md`, `ARCHITECTURE.md`.
- **Deleted** (per v2 §B3): the 2 tombstones `cowork_temporal_extension_contract.md` +
  `cowork_engage_criteria.md` (were untracked stubs → plain-removed); the 2 superseded L3 drafts
  `cowork_layer3_analysis_design.md` + `cowork_layer3_keymode_incrementC_design.md` (`git rm`); the sensitive
  `cowork_github_9444_comment_draft.md` (`git rm`).
- **`scratch_artifacts/`** deliberately NOT committed (a scratch dir; still untracked).

**0b — `50fce9b693`** `fix(tools): re-point cc_e0_fullspine_measure.py docstring off killed engage-criteria doc`
- `tools/cc_e0_fullspine_measure.py:7` "per cowork_engage_criteria.md §3" → the roadmap's ENGAGE CRITERIA
  + RETIREMENT MAP block (E0 stage). Docstring-only, no behavior change. (v2 §B2 finding #3.)

**Inbound-reference confirmation (v2 §B2 said "the three found are fixed — two by Cowork already"):**
- ✔ L6 banner `cowork_layer6_grouping_design.md:5` → now points to `cowork_bounded_context_design.md` §11 (Cowork-fixed, verified).
- ✔ confidence-contract `:60` → now points to `docs/implementation_roadmap.md` ENGAGE block (Cowork-fixed, verified).
- ✔ `tools/cc_e0_fullspine_measure.py:7` → fixed in 0b.
- **⚠ TWO additional inbound references v2 §B2 did NOT list (surfaced, NOT blocked — the deletions are
  explicitly ordered with rationale):**
  1. `COWORK_HANDOFF.md:1266` → `cowork_github_9444_comment_draft.md` (deleted). **Narrative log** inside the
     historical Stage-4b block ("#9444 comment: user takes it themselves (draft ready at …)") — matches v2's
     own "narrative log — no action" category; left as-is (it records a past decision, not a live pointer).
  2. `cowork_target_architecture.md:44` → `cowork_layer3_analysis_design.md` (deleted). A genuine **navigational
     "See … §0.1"** dangler in the *demoted/watch* doc (v2 §B3 #9). NOT in v2 §B2's list. Left unedited: the doc
     is out of this build's batch, and the correct re-point target/section can't be named without guessing (the
     superseded fat-L3 §0.1 decomposed into several specs). **Recommend Cowork re-point it at the A-1 doc-refresh
     pass** (it owns that pass anyway). This is the only real dangling *navigational* pointer the deletions create.

---

## §1 — Task 1: the L1 seam (commit `31a1a883cd`, mostly test)

**Reuse vs new.** The L1 `build(sc, lo, hi)` selection overload + `extend(dir, ticks)` (append-only, clamp,
`boundaryReached()`) already exist and are already covered by EXT1–EXT7. **New:** two read-only accessors
`scoreStart()/scoreEnd()` on `NoteModel` (needed by L4 to distinguish a *selection edge* from the *score
boundary* — §2/§3), and one test.

**Test added — `EXT8_ExtendEquivalence_HoldsAfterEveryStep`.** The GENERAL per-step form of the §4 equivalence
invariant: after ANY extend step, in ANY direction, by ANY amount (including a clamp), the model is
byte-identical (notes + order + both query answers) to a **fresh `build` over the current loaded span**. EXT3
proved only the final-state interior case; EXT8 maintains the invariant across a randomized mixed-direction/amount
walk on every `nm_*` fixture — this is the invariant that outlives the interim whole-score rebuild.

**Idempotent re-request** is the pre-existing `EXT4` (re-request at the boundary = no-op; non-positive amount =
no-op). With the amount-based `extend`, "re-request an already-loaded span" is reachable only at the boundary,
which EXT4 covers.

---

## §2 — Task 2: L3 reach-back — tests + the HELD flag-ON A/B

**Reuse vs new.** L3 reach-back is the already-coded, gated-OFF instance of the extension request
(`regionanalyzer.cpp` reach-back loop; `ReachBackOptions.enabled=false`). Its equivalence-to-full-context (§3.1),
increment-independence (§3.2), score-start truncation (§3.3), and output-is-selection-only (§3.4) already exist.

**(a) Tests added — commit `ee51ab2121`** (`reachback_tests.cpp`):
- **§3.5 `HardBoundTerminatesBeforeScoreStart`** — the §3.7 never-converges cap: trigger forced permanently ON
  (convergence can never fire), a small `maxReachSteps` stops the loop at the hard bound strictly before the score
  start, still emitting a valid selection-only result; deterministic across re-runs.
- **§3.6 `DeterministicAcrossRuns`** — identical (score, selection, settings) ⇒ identical output.
- Union-span equivalence + score-boundary truncation are the pre-existing §3.1/§3.2/§3.3 (equivalence to the
  maximal context ⇒ union equivalence by convergence).

**(b) Flag-ON A/B, read-only — commit `30b23d9f5c`** (`batch_analyze --reachback-ab`, tools-only, diagnostic;
returns before the corpus path, so production/the gate are byte-identical). It runs the SHARED region analyzer over
interior P3-style single-measure ranges (skipping the opening measure) with reach-back OFF vs ON.

**HELD A/B numbers (4 representative scores):**

| Score | ranges | changed | lead-key changed | offMsTotal | onMsTotal |
|---|---|---|---|---|---|
| bach chorale 003 | 11 | 5 | 4 | 310.5 | 132.0 |
| mozart K279-1 | 24 | 9 | 9 | 15636.5 | 267.0 |
| chopin BI16-1 | 24 | 8 | 8 | 1420.3 | 127.0 |
| corelli op01n08d | 24 | 10 | 9 | 910.2 | 175.3 |

**Reading (HELD for ratification):**
- **Output delta is the real signal:** reach-back changes the emitted analysis on **~35–45% of interior
  single-measure range queries**, almost entirely by **anchoring the leading-edge key** (lead-key-changed ≈
  changed-count). This is exactly the designed effect (§5 / §6 scenario 1: an interior selection's opening is
  anchored to the carried-in prevailing key). It confirms activation is a **material, live behavior change** →
  its own ratification, as the instruction states.
- **The wall-time column is CONFOUNDED — do NOT read it as "reach-back is free/faster."** The OFF run executes
  FIRST per range and the ON run SECOND, so ON benefits from warm caches (score traversal / measure layout /
  allocations); the K279-1 `offMsTotal` 15636 ms is a cold-start outlier. A trustworthy cost measurement needs an
  interleaved, warmed, repeated harness — flagged as an Unknown (§7). The A/B here establishes the **output impact**,
  not the cost.

**Not default-ON.** `ReachBackOptions.enabled` stays `false` everywhere on the production path; the A/B is the only
place it is turned on, and only in a diagnostic that never reaches `analyzeScore`. Whole-score paths are provably
untouched (I2, §6).

---

## §3 — Task 3: the L4 starved-window request path (commit `13f80faced`, dormant substrate)

**Reuse vs new.** The L4 decoder is already isolated from production (only reachable via `--decode-chords`); the
window clamp lived in `adaptiveWindow` (`std::max(0,·)/std::min(n-1,·)`). **New, all dormant:**
- `ChordSliceDecoderPreferences`: `enableEdgeExtension` (default **OFF**), `maxEdgeExtendSteps` (hard bound),
  `edgeExtendIncrementSlices` (the natural unit — slices → ticks, §9).
- `SliceChord`: `clippedBySelectionEdge` / `cueDenied` provenance (§3 item 10) — **set only by
  `decodeSelection`**; the core `decode()/decodeWindowed` path never touches them (byte-identical, grep-proof).
- `adaptiveWindow` gains **defaulted-null** clamp-report out-params (the one existing caller stays inert).
- `ChordSliceDecoder::decodeSelection(model /*by value*/, selStart, selEnd, …)` — the requester loop.

**Behavior (§5 sharpened).** `decodeSelection` slices the model's current loaded span (L2), runs a **fresh full
forward decode from slice 0**, and emits **only** the selection slices (§2 — context is evidence). When
`enableEdgeExtension` is ON and a selection-edge slice's window is truncated at the **loaded (non-score) edge**
AND its decision is **not already a full-margin Commit** (decision-relevant), it drives the requester loop —
**L1 `extend` → L2 re-slice → re-decode → re-check** — bounded by `maxEdgeExtendSteps` and the score boundary
(score-boundary ⇒ proceed truncated, no request). The private by-value model copy leaves the caller's model
untouched.

**A design-faithfulness correction made mid-build (worth Cowork's eye):** the first cut used a bounded-look-back
re-decode (`decodeWindowed(selFirst,…)`), which the `redecodeRange` caveat says can diverge from a full decode for
inherit-run slices — EDGE5 caught it. The §4 equivalence invariant demands the result equal *a single fresh run
over the final loaded span*, so `decodeSelection` now **decodes from slice 0** and slices out the selection. This
is the correctness-first / interim-rebuild philosophy (like L1's whole-score rebuild).

**Tests added (`decode_chord_tests.cpp`, EDGE1–EDGE7):**
- **EDGE1** I2 whole-score inertness — `decodeSelection(whole)` == `decode()` slice-for-slice, NO provenance, even
  with extension ON (loaded edges ARE the score bounds ⇒ no clip ⇒ no request).
- **EDGE2** must-FIRE + resolve — a thin (1-PC) decision-relevant edge; OFF stays clipped, ON extends to the score
  boundary and the clip resolves.
- **EDGE3** denial provenance — `maxEdgeExtendSteps=0` ⇒ the request is refused ⇒ clip + `cueDenied`.
- **EDGE4** must-NOT-fire — a full-margin Commit at the edge is not decision-relevant ⇒ no request (ON == OFF).
- **EDGE5** equivalence + output-is-selection-only — selection-windowing of a full decode == full decode restricted.
- **EDGE6** determinism. **EDGE7** step-size independence (§8) — small vs one-big increment over the same final span.

**Stop-condition check (instruction):** the L4 request was obtainable entirely through **L1 `extend` + L2 re-slice
+ L4 re-decode** (the forward re-run). No STOP raised.

---

## §4 — Task 4: the L5 pinned-extent discovery + request (commit `86b2c5b4fc`, dormant)

**Reuse vs new.** The resolver `resolveCarriedReadings(region, cadences, key, params)` is a pure, dormant function
over an in-memory region. **New, all dormant:**
- `L5ForwardExtensionParams` (`enableForwardExtension` default **OFF**, `maxForwardExtendSlices` = K,
  `maxForwardExtendBeats` = B), `ForwardSupply {Supplied, ScoreBoundary, Refused}`, `ForwardExtensionProvider`
  (the supplier abstraction = the L1-extend→L2→L3/L4 forward re-run; hand-injected in tests).
- `ResolvedReading`: `clippedBySelectionEdge` / `cueDenied` (§3 item 10).
- `resolveCarriedReadingsExtending(region /*by value*/, cadences /*by value*/, key, provider, params, ext)`.

**Behavior (§5 / L5 §5.0).** A §5.5 abstain resolution whose **decision-context span** is cut by the selection edge
before any of **(i)** a cadence-anchored function (a cadence `arrivalTick` forward of the slice), **(ii)** a
punctuation boundary (subsumed by (i) for the dormant resolver — a cadence arrival IS the functional punctuation; a
standalone L1.5 boundary tick is an engage input), **(iii)** the **K-slice / B-bound** — requests a forward
extension via the supplier. The region grows **append-only forward** and the resolution **re-runs forward**; output
covers the **original selection only**. Denied (score boundary = clean truncation; driver refusal = a denial) ⇒
the decision resolves on what it saw (the honest open mark) + provenance.

**§8 one-pass closure (no-reopen) — how it holds.** The final pass is a fresh `resolveCarriedReadings` over the
enlarged region ("infer forward again", not a patch). Forward appends can only change the **edge-cut** decisions; a
decision the base pass closed had its forward context already satisfied within the region, so it re-resolves
identically — never re-opened. **Proven by L5EXT5** (an interior closed abstain keeps its reading after the
extension finalizes a later edge decision).

**Tests added (`functionresolver_tests.cpp`, L5EXT1–L5EXT7):** disabled==base (no provenance) · must-fire+resolve ·
refusal→open-mark+denial · score-boundary→clip-not-denied · **no-reopen (§8)** · determinism · **extension ==
fresh run over the final region (§4 equivalence)**.

**Stop-condition check:** the L5 request is obtainable through the supplier = the L1-extend + forward re-run, exactly
the same pattern by which the L4→L5 contract types are hand-injected in tests. No STOP raised. **No new ambiguity
kind, no θ, no constant tuned** (K/B are structural bounds with default seeds; only the existence of a cap is fixed).

---

## §5 — Task 5: system tests + the §11 gate proof

**System properties (distributed across the layer commits, per the design):**
- **Step-size independence (§8):** L1 EXT2 (big vs small steps → same final model), L3 §3.2 (increment-independent),
  L4 EDGE7 (small vs big increment over the same final span). L5 inherits it structurally (the final pass depends
  only on the final region, not the supply schedule — L5EXT7).
- **Determinism:** L1 (fixed-seed walks), L3 §3.6, L4 EDGE6, L5 EDGE… L5EXT6.
- **No-oscillation / termination:** every loop is bounded by its hard bound (`maxReachSteps` /
  `maxEdgeExtendSteps` / K + an absolute round backstop) and each extend strictly grows the loaded span toward a
  boundary — the tests completing is the termination proof; the hard-bound tests (L3 §3.5, L4 EDGE3) exercise the
  cap biting.
- **I2 whole-score inertness:** L1 EXT1 (degenerate build retains all), L4 EDGE1 (`decodeSelection(whole)` ==
  `decode()`, no provenance even with the flag ON). The L5 analog is structural (OFF ⇒ base resolver, L5EXT1).

**The §11 gate proof (the standing obligation):**
- Suites green — composing **1015/1015**, notation **53/53**, pipeline_snapshot **11/11 with NO golden refresh**
  (the snapshot pass is the direct proof that P1–P4 production output is byte-identical; the new substrate is
  dormant).
- Corpus regen — **Baroque 53 / Jazz 24 / Default 53**, verified as **EXACT case-identity sets** (diffed
  `stem@tick` against the CLAUDE.md gate sets; zero delta on all three presets).
- `git status tools/corpus` — clean (the corpus dirs are gitignored; the identity-set match is the substantive
  proof, alongside the snapshot pass).

---

## §6 — the §11 acceptance checklist, item by item

| §11 item | Status | Evidence |
|---|---|---|
| 1. design ratified (SIGNED) | **PASS** | `cowork_bounded_context_design.md` SIGNED 2026-07-02 (committed in 0a) |
| 2. Coded L1: build-selection + extend seam (interim rebuild ok) | **PASS** | pre-existing; §1 (+ scoreStart/End accessors) |
| 2. Coded L2: re-slice-on-extend | **PASS** (pre-existing) | slicer CP1–CP7; reused by decodeSelection/reach-back |
| 2. Coded L3: reach-back as the request (from gated-off) | **PASS as capability; default-OFF** | §2; activation HELD for separate ratification |
| 2. Coded L4: request-or-truncate path + item-10 denial provenance | **PASS (dormant)** | §3, commit `13f80faced` |
| 2. Coded L5: pinned extent + discovery rule | **PASS (dormant)** | §4, commit `86b2c5b4fc` |
| 3. must-fire / must-not-fire fixtures per discovery rule | **PASS** | L4 EDGE2/EDGE4; L5 L5EXT2/L5EXT4; L3 §3.1/§3.3 |
| 3. §4 equivalence invariant (any extension ≡ one fresh run over the final span) | **PASS** | L1 EXT8; L4 EDGE5; L5 L5EXT7; L3 §3.1/§3.2 |
| 3. step-size independence (§8) | **PASS** | L1 EXT2; L3 §3.2; L4 EDGE7; L5 (structural) L5EXT7 |
| 3. denial provenance | **PASS** | L4 EDGE3; L5 L5EXT3/L5EXT4 |
| 3. hard-bound / no-oscillation termination | **PASS** | L3 §3.5; L4 EDGE3; L5 (bounded loop + L5EXT2) |
| 3. determinism | **PASS** | L3 §3.6; L4 EDGE6; L5 L5EXT6; L1 fixed-seed |
| 3. degenerate-case byte-identity with the corpus gate 53/24/53 | **PASS** | §5 — EXACT identity sets; snapshot 11/11 no refresh |
| 4. L6 track resumes | **OPEN** (correctly) | un-parks on Cowork's ratification of this report + the user's L3-activation call |

No item is FAIL. The only OPEN is item 4 (L6), which is the point of the gate.

---

## §7 — Unknowns (stated, never guessed)

1. **L3 reach-back activation cost.** The §2 A/B establishes the *output* impact (~35–45% of interior ranges change)
   but the *wall-time* is confounded by OFF-then-ON cache warming (K279-1's 15.6 s `offMsTotal` is a cold-start
   artifact). A trustworthy overhead figure needs an interleaved / warmed / repeated harness. Not built here (the
   instruction asked for output deltas + wall-time; the deltas are trustworthy, the raw timing is not — reported
   honestly rather than as a favorable "ON is faster").
2. **L5 (ii) punctuation boundary.** In the dormant resolver a cadence arrival stands in for the punctuation stop;
   a standalone L1.5 punctuation-boundary tick is not an input to the region vector today. Wiring the L1.5 boundary
   as a first-class (ii) input is an engage-time step (the resolver has no L1.5 dependency by design).
3. **L5 commit-side edge cut.** The discovery trigger fires on §5.5 *abstain* resolutions (the clear forward-context
   case). A confident *commit* whose §8 override couldn't see forward is the same class but is not triggered here —
   noted as a faithful narrowing, not a gap (the override simply doesn't fire with no forward function).
4. **The two extra inbound doc references** (§0): `COWORK_HANDOFF.md:1266` (narrative log, left as-is) and
   `cowork_target_architecture.md:44` (a real navigational dangler in a demoted doc — recommend Cowork re-point at
   the A-1 pass). Neither blocks the ordered deletions.
5. **`decodeSelection` output `sliceIndex`** is the final-span slice index (post-extension), documented as such;
   tests compare chord identity, not the index. If a consumer at engage needs selection-relative indices, that is a
   trivial renumber (not built dormant).

---

*End of report. All load-bearing claims re-verified at built objects: suites 1015/53/11 (no golden refresh);
corpus EXACT sets 53/24/53 diffed at `stem@tick`; the dormant substrate is grep-provable (enableEdgeExtension /
enableForwardExtension default OFF; decodeSelection / resolveCarriedReadingsExtending have no production caller).
Commits `d39da15d95`(0a) `50fce9b693`(0b) `31a1a883cd`(T1) `ee51ab2121`(T2a) `13f80faced`(T3) `86b2c5b4fc`(T4)
`30b23d9f5c`(T2b) — local, fork-only, unpushed. This report is HELD; L6 un-parks on Cowork's ratification.*

LINE COUNT: this file is 268 lines.

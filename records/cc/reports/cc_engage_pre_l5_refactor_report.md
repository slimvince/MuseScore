# CC Report — Engage arc #7, Stage 1: the PRE-Layer-5 refactor batch (BUILD event)

> **Status: BUILD event (CC, 2026-07-07; Engage arc #7).** Dispatch:
> `cc_instruction_engage_pre_l5_refactor_batch.md`. Ratified plan:
> `cowork_engage_arc_plan.md` (Stage 1). Fix source of truth:
> `cowork_structural_integrity_audit.md` §3 (FQ-1…FQ-7) + the site rows.
>
> **Base HEAD (the byte-identity diff base):** `0d7fcc6c48`, branch `master`, fork-only.
> **After this batch:** ahead 3 → the docs fold (this report + folds) makes it ahead 4+.
> Corpus frozen at `c50002fee1`.

---

## 0. Headline

Stage 1 of the ratified engage-arc plan is the portable pre-Layer-5 unification wins, each a
**byte-identical revertible commit**. Of the five queued items (FQ-1, FQ-3, FQ-5, FQ-6, FQ-7):

| FQ | disposition | commit |
|---|---|---|
| **FQ-5** (fact-layer dedups S5/S7/S10/S11) | ✅ DELIVERED byte-identical | `65764881d0` |
| **FQ-7/S8** (key-decoder constant sourcing) + **S9** (dead-work adjudication) | ✅ DELIVERED byte-identical (S8) + S9 kept (load-bearing) | `56b06462db` |
| **FQ-6** (serialization/display cap-views) | ✅ DELIVERED byte-identical | `5420e6e543` |
| **FQ-1** (unify the "best different-root alternative" scan) | ⛔ **STOP + report** — the four sites do NOT share one code-level decision (divergent predicate / element type / result-use); no byte-identical single primitive exists | — |
| **FQ-3** (relocate `findTemporalContext` out of L1.5) | ⛔ **STOP + defer to E4** (the UNCLEAR-7 adjudication) — doable + decoder-independent, but E4-entangled + most-invasive; folds into E4's temporal-context ownership move | — |

**Every delivered commit is proven byte-identical on the full output surface** (winner **and**
`alternatives[]`, whole `.ours.json`): **0-diff across 352×3** (Baroque/Jazz/Default) vs the
pre-commit HEAD `0d7fcc6c48`; **robust-stop PASS** (class-(b) duration non-increase, +0/-0 all
presets); **characterise 52/24/52**; **suites 1101 / 53(+4 skip) / 11**, no golden refresh.

Two items STOP-and-reported per the dispatch's discipline ("deliver the clean ones, flag the rest;
do NOT force"). Neither was forced. Both are grounded at code below for Cowork adjudication.

---

## 1. Verification apparatus (how byte-identity was proven)

- **Golden reference** regenerated at HEAD `0d7fcc6c48` into a scratch root (`run_bach_preset.py`,
  352 scores × 3 presets). Proven **byte-identical to the committed `tools/corpus/`** (0 differing
  `*.ours.json`) and to the committed robust-stop reference (robust_stop_diff +0/-0 all presets,
  characterise 52/24/52) — so the golden is a valid HEAD baseline.
- **Per-commit check:** rebuild → regenerate the candidate corpus (3 presets) → `cmp` every
  `*.ours.json` candidate-vs-golden (must be 0 differing) → `a8_rebaseline_measure.py` +
  `robust_stop_diff.py` (must PASS) → all three suites (must be 1101 / 53 / 11, no golden refresh).
- `.ours.json` confirmed fully deterministic (golden == committed corpus, byte-for-byte), so the
  `cmp` diff is a true full-surface byte-identity proof, strictly stronger than the summary stops.

---

## 2. FQ-5 — fact-layer duplication cleanups ✅ `65764881d0`

One commit, four unify-to-one-source cleanups, each byte-identical:

- **S5** — `regiontonecollector.cpp` inlined `beatWeight` lambda (`{1.0,0.85,0.75,0.5}` BeatType→weight
  map) → `scoreharvest::regionMetricWeightForBeatType` (single-owned, header already included). Three
  call sites routed. The `regionMetricWeightForBeatType` switch is byte-identical to the deleted lambda.
- **S7** — deleted the redundant `standard.*=` restatement in `modepriorpresets.cpp` (**copy 3 of 3**
  the sync test `StandardMatchesStructDefaultInitializers` had to guard). A default-constructed
  `ModePriorPreset` already carries exactly these "Standard" magnitudes, so the deletion is byte-identical
  and the sync test still passes. **Partial:** full A↔B single-sourcing (make `ModePriorPreset`'s struct
  defaults derive from `kDefaultKeyModeAnalyzerPreferences.modePrior*`) is **deferred** — it couples the
  deliberately-minimal `modepriorpresets.h` (only `<string>/<vector>`, kept minimal so `batch_analyze`
  can use the preset table) to `analysistypes.h`, a **dependency-profile design decision** better ratified
  explicitly than folded into a "trivial" byte-identical batch. Flagged, not forced.
- **S10** — extracted `normalizedConfidenceSigmoid(gap,steepness,midpoint)` into `keymodeanalyzer.h`
  (included by both consumers); routed the per-region winner confidence (`keymodeanalyzer.cpp` ×2) and
  the Layer-3 emission confidence (`keymodesequence.cpp`) through it. Same expression → byte-identical.
- **S11** — extracted file-local `makeChordPathNode(committed, alternatives, gateCtx)` in
  `regionanalyzer.cpp`; routed all three `decoder.recordNode()` commit sites (Pass-1 main loop + the two
  Pass-2/2b subloops) through it. Same field derivations → byte-identical.

Verify: 0-diff 352×3, robust PASS, characterise 52/24/52, suites 1101/53/11.

---

## 3. FQ-7 — key-decoder constant sourcing (S8) + dead-work adjudication (S9) ✅ `56b06462db`

**S8 (delivered, byte-identical):** `keymodesequence.h` `KeyModeSequencePreferences` — the change-cost
and emission-window constants were copied-by-value from the resolver / scoreharvest, so a Stage-5 fit of
either drifts them apart. Sourced from the shared symbols (all `inline constexpr`, so the struct and its
`inline constexpr` default stay literal types; identical magnitudes):

| field | now sourced from | value |
|---|---|---|
| `changeBaseCost` | `kDefaultKeyModeAnalyzerPreferences.hysteresisMargin` | 2.0 |
| `changePerFifthStep` | `kDefaultKeyModeAnalyzerPreferences.keySignatureDistancePenalty` | 0.60 |
| `relativePairExtraCost` | `kDefaultKeyModeAnalyzerPreferences.relativeKeyHysteresisMargin` | 2.0 |
| `decayRate` | `scoreharvest::DECAY_RATE` | 0.7 |
| `lookaheadWeight` | `scoreharvest::LOOKAHEAD_WEIGHT` | 0.5 |

**S9 (adjudicated at code — KEPT, report-only, NO change):** the dispatch asked to drop the
`resolveKeyAndModeRanked` at `regionanalyzer.cpp:585` **only if** it is dead scored work with a
grid-byte-stable replacement. **It is NOT dead.** `keyFifths`/`keyMode` taken from
`initialRanked.front()` (`:587-588`) are consumed by **`greedyExpandSegmentation`** (`:851-854`) **and**
`findTemporalContext` (`:900`) — both drive the segmentation grid. The code documents this itself:
`":585 … kept ONLY to keep the segmentation grid byte-stable (S2)"`. A ranked-resolve fifths can differ
from `keySigCtx.correctedFifths` (the ranked resolve may pick a key other than the notated signature), so
dropping it to a corrected-fifths+declared-mode seed would move the grid. **Kept — load-bearing, not
dead** (dispatch: "do not cut load-bearing work"). The `resolveKeySignatureContext`-computed-twice sub-note
is internal to the retained resolve and untouched.

Verify: 0-diff 352×3, robust PASS, characterise 52/24/52, suites 1101/53/11.

---

## 4. FQ-6 — serialization/display cap-views ✅ `5420e6e543`

The ranked `alternatives` carry was truncated by two independent ad-hoc loops (anchor #9/#10, S20):
batch serialization capped at `altIdx<3` (`batch_analyze.cpp` ×2), the bridge/display view appended all
alternatives uncapped (`notationcomposingbridge.cpp`). Introduced one shared projection
**`appendCappedAlternatives(out, carry, cap)`** in `analyzed_section.h` — the header where the
`alternatives` carry type lives and which **both** consumers already include — and routed all three sites
through it: batch passes `cap=3`, the bridge passes `cap=carry.size()` (uncapped). One explicit projection
over the one carry, not two independent truncations.

**Structural unification ONLY.** Both current values preserved verbatim (batch 3, bridge uncapped); the
**cap-#2 VALUE lift stays DEFERRED to Stage 3** (L5 engagement) per the dispatch. `min(size,cap)` prefix →
byte-identical.

Verify: 0-diff 352×3, robust PASS, characterise 52/24/52, suites 1101/53/11.

---

## 5. FQ-1 — ⛔ STOP + report: the four scans are NOT one code-level decision

**The dispatch:** "Unify the 'best different-root alternative' scan into ONE primitive … route all four
callers through it. Byte-identical per site." **The audit premise:** "one decision, four sites."

**Finding at code: the premise over-counts at code granularity.** The four sites share a *conceptual
motif* ("the best alternative that reads differently from the winner") but do **not** share one code-level
decision — they diverge on the "differs" predicate, the element type, and the result-use, so **no single
byte-identical primitive can serve all four**:

| site | "differs" predicate | element type | what it does with the result |
|---|---|---|---|
| #1 `harmonicfunctionlayer.cpp:531-548` (inversion-append) | `rootPc != winnerRootPc` (root only) | `results[]` (`ChordAnalysisResult`) for the `any_of` **and** `chosenPerBass` (`WorkCand`) for the pull | **builds + appends as a trailing alternative** (NOT front) if none present |
| #2 `chordpostpasses.cpp:262-269` (pedal gap) | `rootPc != p2Root` (root only) | `pass2` (`ChordAnalysisResult`) | reads the alt's **`.score`** for the pedal confidence gap |
| #3 `postscoringgates.cpp:193-204` (FM2 bias gate) | `rootPc != winner.rootPc` **plus** clean-quality filter + HalfDim-inversion exception | `results[]` (`ChordAnalysisResult`) | tracks `bestAltIdx` through a **multi-criteria** scan (root-diff is only the first filter) |
| #4 `chordslicedecoder.cpp:929-932` (open-question) | **`!sameChordSymbol`** = `rootPc == && quality ==` (root **and** quality) | `sc.alternatives` (`ChordSliceCandidate`) | names `readingB` for the open-question label |

Decisive facts:
- **Predicate divergence is real, not cosmetic.** `sameChordSymbol` (decoder, #4) treats a same-root
  different-quality pair (e.g. C vs C7) as a *different reading*; the legacy sites (#1/#2/#3) treat it as
  *same root* (not different). Forcing one predicate on all four **changes bytes** on at least one site.
- **`promoteToWinner` is not the vehicle.** Its contract is "promote a *specific* `(rootPc,quality)`
  target to **winner** (front)". None of the four "find the best *different*-root" scans matches it: they
  don't know the target root a priori, and #1/#4 do not promote to front (they carry/name an alternative).
- The only construct that could span all four is a predicate-and-element-type-parameterized template —
  i.e. `std::find_if` with a per-site lambda. That removes a 2–3-line loop skeleton but leaves each site's
  *actual* decision (predicate + result-handling) intact and per-site, so it does **not** unify "one
  decision"; it is over-abstraction, not total-unification.

**Disposition:** STOP, do not force. Per principle #13 (surface the surprise before building around it) and
the dispatch ("STOP-and-report any item that snags … an entanglement, or that can't be done
byte-identically"), this is **declared to Cowork** for adjudication with the greater architectural context.
If Cowork intends a narrower target than "all four" (e.g. converging the legacy sites onto the decoder's
`sameChordSymbol` notion — a **behavior change**, not byte-identical), that is a Stage-2/E4 decision, not a
Stage-1 byte-identical unification. No code was changed for FQ-1.

---

## 6. FQ-3 — ⛔ STOP + defer to E4 (the UNCLEAR-7 adjudication)

**The dispatch's first step:** "confirm it is **not simpler to fold into the E4 temporal-context ownership
move**. If relocating cleanly now requires decoder internals or would be redone at E4 ⟹ STOP-and-report
(defer to E4) — do not force a pre-L5 relocation that E4 redoes."

**Findings at code (both sides, honestly):**
- **It is byte-identically relocatable and decoder-independent** — NOT blocked. `findTemporalContext`
  (`regiontoneprimitives.cpp:451-592`, L1.5) instantiates the L4 analyzer and runs
  `analyzeChord`+`applyIter8691Pedal`+`applyPostScoringGates` ×2 on the cold prev/next neighbours. The
  clean split (an L1.5 neighbour-tone view + the L4 identity computation + a region-layer composition, or a
  verbatim pure-move of the whole function to a region/L4 unit) uses only existing public API; **no decoder
  internals**. It would be verifiable byte-identical (the analyzer calls are unchanged).
- **But it is E4-entangled, and its final owner is decided by E4.** The `ChordPathDecoder` (Stage 3.1) is
  **already wired** at `regionanalyzer.cpp:899-902`, **seeded by `findTemporalContext`**, and
  `decoder.commit()` is byte-identical to `advanceTemporalContext()` (`decode_tests.cpp:131-165`). The
  decoder is the declared successor to the whole hand-threaded temporal-context state.
  `ARCHITECTURE.md` D-BRIDGE (`:1067-1068`): *"The decoder's path state supersedes `findTemporalContext`'s
  cold walk."* D-P4 (`:1043-1045`): *"any context pre-pass built against the greedy pipeline would be
  discarded at Stage 3."* So **E4 IS the temporal-context ownership move** — it establishes the decoder as
  the owner of the regional temporal context.
- **The relocation is the single most invasive item** (a new region-layer unit + CMakeLists, or bloating
  `regionanalyzer.cpp`; touching the **notation** module wrapper `notationcomposingbridgehelpers.cpp`; and
  **relocating tests** out of `engravingbridge_branch_tests.cpp`), for a live-path HIGH-severity function
  whose regional-path role E4 supersedes and whose *proper L4 owner* (the decoder-owned assembly) is the
  E4 decision.

**Adjudication (UNCLEAR-7 resolved → fold into E4).** Relocating `findTemporalContext` to an **interim**
region/L4 home now, only for E4 to move temporal-context ownership into the decoder-owned assembly, is the
"redone at E4" case the dispatch says not to force. The audit's own hedge is "**A** (confirm not simpler at
E4)"; at code, the confirmation lands on *fold into E4*. **Deferred to E4, not forced.** No code changed.

**Note for Cowork (who holds the definitive E4 scope):** `findTemporalContext` does **survive** E4 in the
P4/bridge cold fallback (D-P4: "the current contract, documented and accepted") and as the decoder's
initial seed — so if the E4 design keeps a cold seed/fallback in a fixed non-decoder home, the L1.5→L4
relocation could still be a lasting pre-L5 win Cowork may choose to re-dispatch. That call needs the E4
architectural context CC does not hold; hence the deferral rather than a unilateral interim relocation.

---

## 7. Principle adherence

- **#6 (one path per concern):** FQ-5/S5/S10/S11, FQ-6 collapse genuine duplications to one source; FQ-7/S8
  single-sources the drifting constants. FQ-1 declined **because** the four sites are *different* concerns
  sharing a motif, not one concern — unifying them would violate byte-identity, not serve #6.
- **#7 (layer adherence):** every delivered fix lands in its proper layer; FQ-3 deferred precisely because
  its proper (E4-decided) owner is not yet built.
- **#12 / #15 (no information loss; verify at objects on the full surface):** byte-identity proven on the
  whole `.ours.json` (winner + carry), not an assertion.
- **#13 (surface a surprise as a STOP):** FQ-1's premise mismatch and FQ-3's E4-entanglement declared to
  Cowork, not built around.
- **#14 / #16 (one revertible provenance-stamped commit; re-baseline discipline):** three such commits; no
  re-baseline needed (byte-identical, reference untouched).

---

*CC, 2026-07-07. Engage arc #7 Stage 1 — pre-Layer-5 portable unification. Delivered FQ-5, FQ-7/S8, FQ-6
(byte-identical, both stops green, suites no-refresh); S9 adjudicated KEPT (load-bearing); FQ-1 and FQ-3
STOP-and-reported (not forced) for Cowork adjudication. Cowork verifies each byte-identity proof at objects
→ then the Layer-5 engagement design (Stage 2) opens.*

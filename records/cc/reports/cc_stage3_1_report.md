# CC Stage 3.1 — Beam-1 Decoder Skeleton (byte-identical) — Report

> Execution of `docs/decoder_design.md` (RATIFIED `e2bdef7e13`) roadmap row 3.1.
> Base commit `3aa9db7676` (HEAD at session start; STATUS.md session 6).
> Deliverable: a beam-1 chord-path decoder behind the quality-level knob, **byte-identical
> on every output**, cache-READY but not cached. Oracle + segmentation untouched.

---

## §1 — Implementation plan (as built)

### 1.1 Where the decoder lives + API

**Location: new `src/composing/analysis/decode/chordpathdecoder.h`** (header-only at 3.1).
Justification: it is a new layer seam — neither the vertical oracle (`chord/`) nor the
per-region competition (`function/`), but the *sequence* commit chain that today lives
inline in `region/regionanalyzer.cpp`. A dedicated `decode/` directory matches the design's
suggested home and pre-stakes the Stage-3.5 file split without dragging the big restructure
forward. Header-only because the decoder is a thin re-expression of the already-inline
`advanceTemporalContext` helpers in `chordanalyzer.h`; no out-of-line definitions are needed.

**Quality-level knob: `enum class DecodeQualityLevel : uint8_t { FastBeam1=0, Normal=1, Deep=2 }`**
defined in `chordanalyzer.h` (full definition, NOT forward-declared), with a new
`ChordAnalyzerPreferences::decodeQualityLevel = DecodeQualityLevel::FastBeam1` field.
Justification for an **enum** (not an int): the levels are a closed, named set (design §9:
0 Fast / 1 Normal / 2 Deep); an enum documents them and makes `level > FastBeam1` reads
explicit. Justification for defining it in `chordanalyzer.h`: identical to the `ScoringPhase`
precedent — `ChordAnalyzerPreferences` needs the complete enum for the `= FastBeam1` default
member initializer, and `chordanalyzer.h` cannot include the decode header (the include runs
the other way). Default = level 0 per design §9 / §12.

**Path-state struct + node/candidate representation (design §5 table).** The decoder owns the
three pieces the loop threaded by hand:

| `ChordTemporalContext` field(s) | Decoder home |
|---|---|
| `previous{Root,Bass,Quality}`, predecessor-confidence fields, rolling window | `m_ctx` (the threaded `ChordTemporalContext`, exposed live via `context()`) |
| `consecutiveBassStepwiseCount` rolling counter | `m_runningStepwiseCount` |
| `recentRootPcs[3]` rolling window | `m_recentRootsBuf` |
| `nextRootPc`/`nextBassPc` (cold lookahead) | **NOT path state** — stays a node-external input written onto `m_ctx` by the loop (AWKWARD-3) |

At **beam 1** the candidate set at each node IS the existing `results[]` (top-3 + diff-root,
same threshold/cap) — produced by the unchanged oracle+competition; the decoder does not
re-derive it. The committed node is recorded as `ChordPathNode { committed, alternatives,
winnerScore, winnerMargin }` (evidence-forwarding, §13 Q5), accumulated in `m_path`.

### 1.2 The interleaving reality — confirmed (design §1 / §4(4))

**Confirmed, not contested.** The beam-1 decoder is a *re-expression of the existing commit
chain*, NOT a post-pass over a finished stream. Concretely: the loop still calls
`analyzeChord → applyIter8691Pedal → applyPostScoringGates → refineSparse[/applyTonicPrior]`
inline (the oracle + per-region competition + post-scoring, all upstream and unchanged); the
decoder replaces only the `advanceTemporalContext(...)` commit at all three sites (Pass 1,
Pass 2, Pass 2b) with `decoder.commit(chosen.identity, gateCtx)`. The path state object
*encapsulates* the threaded `ChordTemporalContext` + the two rolling buffers; `context()`
returns a live reference so every per-region input write and every downstream consumer
(Pass 2/2b reading committed identities, the inline same-root merge, preMerge/postMerge hooks)
is byte-unchanged. Pass 2/2b still consume committed identities; the merge still runs after
commit — all identical.

### 1.3 Cache-readiness WITHOUT caching

The decoder is a constructible object scoped to a region range that **accumulates the decoded
path** (`recordNode` → `m_path`) and exposes it via `path()`. Nothing stores the decoder
across queries; no Pass-0 result is memoized. This is the cache-READY shape (a returnable path
object) with no cache — decode-once/query-many is Stage 3.1b (§13 Q7). At beam 1 `m_path` is
inert: nothing in `regionanalyzer.cpp` reads `decoder.path()`, so it cannot affect output.

### 1.4 The exact arithmetic-order guarantee

**The per-bass score is NOT computed anywhere in the decoder.** It is computed in
`applyHarmonicFunction()` (`harmonicfunctionlayer.cpp`), called inside `analyzeChord()`, which
the loop invokes *before* `decoder.commit()`. The decoder never recomputes, re-associates, or
even reads a per-bass score — it threads the already-selected gate-corrected *identity*
forward. Therefore the FP-sensitive expression
`(basisIndep + rcb + basisDep) × cf × af + wComplete + wSeq [+ wDim] [+ steps]` is in code this
change does not touch, and the documented near-tie tripwires (Δ=+7b 0.02, bwv320 1.92/1.90)
cannot flip. This is the strongest possible byte-identity guarantee: the restructure is purely
control-flow over the commit threading, with zero arithmetic moved.

---

## §2 — Structure map (old → new)

| Site | Old | New |
|---|---|---|
| `chordanalyzer.h` | — | + `enum class DecodeQualityLevel`; + `ChordAnalyzerPreferences::decodeQualityLevel` (default `FastBeam1`) |
| `analysis/decode/chordpathdecoder.h` | — | new header: `ChordPathNode`, `ChordPathDecoder` (owns `m_ctx` + `m_runningStepwiseCount` + `m_recentRootsBuf` + `m_path`; `context()`, `commit()`, `recordNode()`, `path()`, `level()`) |
| `analysis/CMakeLists.txt` | — | + `decode/chordpathdecoder.h` |
| `regionanalyzer.cpp` Pass 1 | `ChordTemporalContext temporalCtx = findTemporalContext(...); int runningStepwiseCount=0; array recentRootsBuf={-1,-1,-1};` … `advanceTemporalContext(temporalCtx, runningStepwiseCount, recentRootsBuf, chosen.identity, gateCtx);` | `ChordPathDecoder decoder(findTemporalContext(...), attemptPrefs.decodeQualityLevel); ChordTemporalContext& temporalCtx = decoder.context();` … `decoder.commit(chosen.identity, gateCtx); + recordNode` |
| `regionanalyzer.cpp` Pass 2 (per parent) | `ChordTemporalContext subCtx; …seed…; int subRunningStepwiseCount=0; array subRecentRootsBuf;` … `advanceTemporalContext(subCtx, …, chosenSub.identity, subGateCtx);` | `ChordPathDecoder subDecoder({}, prefs.decodeQualityLevel); ChordTemporalContext& subCtx = subDecoder.context(); …seed…` … `subDecoder.commit(chosenSub.identity, subGateCtx); + recordNode` |
| `regionanalyzer.cpp` Pass 2b (per parent) | same pattern as Pass 2 | same re-expression |
| `tests/decode_tests.cpp` | — | new: lockstep equivalence + quality-knob pins (see §3) |

`temporalCtx`/`subCtx` are kept as **reference aliases** to `decoder.context()`, so every
intervening per-region input write (`bassIsStepwiseFromPrevious`, `nextRootPc`/`nextBassPc`,
`regionMetricWeight`, parent-scope overrides, the post-commit `nextRootPc/nextBassPc = -1`
resets) is textually unchanged — only the declaration and the commit call changed.

---

## §3 — Equivalence-test form

The legacy commit expression is **replaced in place** (no parallel legacy path is kept — keeping
one would re-introduce the replica anti-pattern §11 warns against). The equivalence test
therefore has two halves:

1. **Unit (`decode_tests.cpp::DecoderCommitMatchesAdvanceTemporalContext`).** A raw
   `ChordTemporalContext` + standalone rolling buffers advanced with `advanceTemporalContext()`
   (the *exact* legacy expression) and a `ChordPathDecoder` are driven through the same scripted
   commit sequence **in lockstep**; every `ChordTemporalContext` field is asserted byte-equal
   after each commit. The script exercises stepwise on/off (rolling-count up/reset), the
   recent-roots window sliding past 3 entries, all `rawCandidates` arities (0/1/2+ →
   `previousWinnerScore`/`Margin` branches), and a winner root absent from `pcWeight`.
2. **Integration (pre-refactor recorded outputs).** Decoder-at-level-0 is pinned against the
   *recorded pre-refactor binary outputs* of the corpus + the 10-score pipeline-snapshot fixtures
   — the 0/353×3 corpus A/B and the 11/11 snapshot goldens. This is the "recorded pre-refactor
   outputs" form named in the instruction, used because the catalog/musicxml composing fixtures
   exercise `analyzeChord` directly (the oracle), not the region-commit chain the decoder
   restructures; the decoder is exercised end-to-end only via `analyzeRegions` (batch + bridge),
   which the corpus and snapshots cover.

Plus quality-knob pins: `DefaultQualityLevelIsFastBeam1` and
`HigherQualityLevelStillBehavesAsBeamOne` (level Normal/Deep commit identically to FastBeam1 —
the no-op pin) and `PathAccumulatesCommittedNodes` (cache-ready plumbing). The existing FP
canaries (1.7 near-tie in `functionlayer_tests.cpp`, Δ=+7b in `gater_tests.cpp`/`diagnose_tests.cpp`,
bwv320) are the tripwires and remain **unmodified**.

---

## §4 — Verification gate

Build: `setup_and_build.bat` exit 0 (CMake reconfigured for the new files; warning-free
on the changed targets).

| Gate item | Target | Result |
|---|---|---|
| Corpus A/B Baroque `.ours.json` diff (vs `/tmp/ab_baseline`) | 0/353 | **0/353** ✅ |
| Corpus A/B Jazz `.ours.json` diff | 0/353 | **0/353** ✅ |
| Corpus A/B Default `.ours.json` diff | 0/353 | **0/353** ✅ |
| Pipeline snapshots (`pipeline_snapshot_tests.exe`) | 11/11 zero diffs | **11/11** ✅ |
| `composing_tests.exe` | green (+4 new decode tests) | **505/505** (501 + 4) ✅ |
| `notation_tests.exe` | 52 green | **52/52** ✅ |
| batch_analyze regression (`test_batch_analyze_regressions.py`) | pass | **pass** ✅ |
| Python metric tests (`unittest discover tools/tests`) | 70 green | **70/70** ✅ |
| BIR Baroque | 13 & 24/13 | **13 & 24/13** ✅ |
| BIR Jazz | 7 & 35/7 (exact set) | **7 & 35/7**, set `{bwv244.15, bwv245.17, bwv245.40, bwv422, bwv432, bwv45.7, bwv74.8}` ✅ |
| BIR Default | 14 (Baroque-13 ∪ {bwv187.7}) | **14**, diff vs Baroque = `+bwv187.7` only ✅ |
| Perf sanity (chorale_001 + K279-1) | per-query p95 within ×1.10 of baseline | **PASS** — see below ✅ |

**Perf sweep (median-of-5, `P3PerfBaseline.DISABLED_Sweep`):**

| Score | median (base) | p95 (base) | ×1.10 p95 ceiling | P4 fb |
|---|---|---|---|---|
| bach_chorale_001 | 92.4 ms (85.7) | 189.2 ms (176.6) | 194.3 → **within** ✅ | 0 |
| mozart_k279_1 | 113.7 ms (105.9) | 2783.5 ms (2754.4) | 3029.9 → **within** ✅ | 0 |

Both per-query p95 are inside the doc's recommended ×1.10 beam-1 gate; P4 fallbacks unchanged
at 0. The ~7–8% median uptick is measurement noise / concurrent session load (the sweep ran
alongside the corpus regen + suites; P3 timings are heavy-tailed and machine-load-sensitive,
per the baseline doc itself), **not** an algorithmic slowdown: the analysis is byte-identical
(0/353×3), the decoder adds no Pass-0 work and lives in the <0.3 ms `analyzeSection` layer
(0.1–0.2% of P3 cost). No caching yet (3.1b), so no improvement was expected. Not a marked
slowdown — no finding.

The chord mismatch report is unchanged (Jazz catalog total=0). The integration half of the
equivalence claim (§3) is the 0/353×3 corpus diff + 11/11 snapshots; the unit half is the
green lockstep `DecoderCommitMatchesAdvanceTemporalContext`.

**Independent byte-identity cross-check:** after regenerating all three preset corpora with
the new binary, `git diff --stat tools/corpus/` is **empty** — the committed `.ours.json` AND
the per-preset `corpus_manifest.json` sha256 fingerprints are unchanged, a second confirmation
of 0/353×3 that does not depend on the `/tmp` snapshot.

---

## §5 — Deviations / unknowns

**Deviations from the ratified design: NONE.** This was ratified-spec execution. Two
clarifications worth recording (neither a design deviation):

1. **Equivalence-test placement (§3).** The instruction's Task 3.1 names "the catalog +
   musicxml fixtures" for the equivalence test. Those fixtures exercise `analyzeChord`
   (the oracle) directly, not the region-commit chain the decoder restructures, so they do
   not exercise the decoder. The decoder is exercised end-to-end only through `analyzeRegions`
   (batch + bridge). The equivalence claim is therefore pinned by (a) a unit lockstep test
   (`decoder.commit()` vs `advanceTemporalContext()`) and (b) the recorded-pre-refactor-output
   form (0/353×3 corpus + 11/11 snapshots) — the alternative the instruction itself offers for
   "if the legacy path is gone." This is a placement choice within the instruction's stated
   options, not a deviation from the design.
2. **`completeTriadInversionBonus` / Gate R / signal migration (design §3/§6, AWKWARD-1..4).**
   Untouched at 3.1, exactly as scoped — these are 3.3 (oracle temporal-signal migration +
   Gate R `basisDep≤0` redesign). The decoder threads the gate-corrected *identity* only; all
   bonus/gate arithmetic stays in `analyzeChord`/`applyHarmonicFunction`/`applyPostScoringGates`.

**Unknowns: none material.** Levels Normal/Deep are defined but inert (pinned no-op);
decode-once caching is deliberately absent (3.1b). The cache-ready `m_path` is inert at beam 1
(nothing reads `decoder.path()`), proven by the 0/353×3 byte-identity.

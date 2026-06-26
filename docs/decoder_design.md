# Stage 3 — Chord-Path Decoder Design

> **Status: RATIFIED (Cowork, 2026-06-12) — design-only, no production code.** No tests
> and no behavior change are implied by this document. It is the Stage 3 design deliverable
> per `docs/implementation_roadmap.md` Stage 3 (rows 3.1–3.5). Ratified subject to one
> mandatory correction (the `completeTriadInversionBonus` temporal-gate reclassification,
> §3/§6) and the seven §13 Open Questions all DECIDED (recommendations accepted). Companion:
> the drafting report `cc_stage3_design_report.md` (probes run, load-bearing claims).
>
> *Written 2026-06-12 (session 6). Base commit `3aa9db7676`. Ratification correction applied
> 2026-06-12. Owner: CC (design) / Cowork + user (ratification).*

Sources this design is built on (all read in full or in the cited section):
`docs/implementation_roadmap.md` Stage 3; `cowork_target_architecture_review.md`
(part-1 mapping table — the skeleton); `docs/redesign_plan.md` "Architecture review
addendum"; `docs/scoring_model.md` §3/§4/§6/§8/§11;
`src/composing/analysis/function/harmonicfunctionlayer.{h,cpp}` (the competition
pipeline = the proto-decoder); `docs/perf_p3_baseline.md`; ARCHITECTURE.md §2.14 +
"Path divergence decisions (Stage 2.4)"; the Stage-1 reports (1a F1–F5, 1b F1–F8,
1c G1–G5).

The central observation, already established by the architecture review and confirmed
here against the code: **the E2d oracle/competition split plus the Step-5 single
commit path already produced the emission/transition factorization a sequence decoder
needs.** `analyzeChord` is the emission model (per-region ranked vertical candidates in
a `fn::ScoringSnapshot`); `applyHarmonicFunction`'s progression signals
(rcb, w_seq, w_dim, step bonuses) are the transition model; the post-scoring gates are
hand-coded re-ranking that a global decode subsumes. Stage 3 restructures the **greedy
left-to-right commit chain** (the `advanceTemporalContext` loop) into a lattice decode,
*without changing the oracle, the segmentation, or — at beam 1 — a single output byte.*

---

## 1. Scope statement

**In scope.** Stage 3 decodes the **CHORD path** over the **existing segmentation**.
The greedy region stream — `greedyExpandSegmentation` (Round 1 anchors + Round 2
`fillGap`), then `regionanalyzer.cpp`'s Pass 1 / Pass 2 / Pass 2b sub-splitting and
Pass 3 `coalesceShortSameRootRuns` + `absorbShortRegions` — **stays exactly as-is**.
The decoder consumes the *final, post-Pass-3* region stream and replaces only what
happens after it: the per-region final-phase competition + the irrevocable
left-to-right commit that threads `ChordTemporalContext` forward.

Concretely, the unit the decoder replaces is the loop body in `analyzeRegions`'
Pass 1 (`cc_stage1c_report.md` §1.1):

```
collectRegionTones → analyzeChord → applyIter8691Pedal → applyPostScoringGates
  → refineSparseChordQualityFromKeyContext → applyTonicPriorToSparseChord
  → advanceTemporalContext (commit identity, thread context to next region)
  → INLINE same-root merge
```

`analyzeChord` (the oracle) and the segmentation passes are upstream and unchanged.
`advanceTemporalContext`'s irrevocable commit is what becomes a decode.

**Out of scope — stated as interfaces, not designed here.**

- **Joint segmentation + labeling.** Optimizing region boundaries *and* chord labels
  in one model (the segmental-CRF target, Masada & Bunescu 2019; ARCHITECTURE.md §2.14
  "segmentation ↔ chord" circularity) is the natural extension *beyond* Stage 3. Stage 3
  decodes labels over fixed boundaries. The C1 schumann case (§11) is the live evidence
  that some residuals need the joint version — flagged, not solved here.
- **Key path (Stage 4).** The decoder consumes the key as a per-region fact frozen into
  `ScoringCell::basisIndep` and `ScoringSnapshot::{scale,keyTonicPc,keyMode}` (exactly
  as `applyHarmonicFunction` does today). Stage 4 will replace per-window key argmax with
  a key HMM; the **interface** is that the chord decoder reads the key emission/`KeyArea`
  the key path commits. Two-level joint key×chord decode is explicitly Stage 4.3, not
  Stage 3.
- **Functional layer (Stage 6).** T/S/D states, secondary dominants, cadence
  confirmation. The chord decoder's output path (one labeled candidate per region, with
  scores/margins retained) is the **input** to Stage 6's sequence labeling. The decoder
  must therefore *emit a path with its alternatives and margins intact*, not just a
  committed winner — that is the evidence-forwarding principle applied to its own output.

**Non-goal at Stage 3.1:** improving any metric. Stage 3.1's only deliverable is a
beam-1 decoder that is **byte-identical** to today. Wins come at Stage 3.2 (wider beam).

---

## 2. Lattice shape

**Nodes.** One node per region in the final post-Pass-3 stream. (Probed region counts,
`--preset Default` = live config, §`cc_stage3_design_report.md` §1: Bach chorale 001 =
40 batch / 43 section regions; Mozart K279-1, the largest perf-corpus score = 84 batch /
141 section regions.)

**Candidates per node.** Each node's candidate set comes from the oracle's
`ScoringSnapshot.cells` for that region — the `(bassPc, rootPc, tiePriority)` cube,
stored bass-outer / root-middle / template-inner (`harmonicfunctionlayer.h:196`). A full
snapshot is `|bassCandidates| × 12 roots × kTemplateCount(17)` cells ≈ 204 per bass
candidate; bass enumeration fires only on bass-motion evidence (§5 of scoring_model;
usually 1–3 bass groups), so ≈ 200–600 cells per region. The current pipeline collapses
this to **top-3 + optional diff-root append** (≤4 emitted `results[]`) per region via the
threshold `(bestScore − bassBonus) × 0.75` and the `results.size() >= 3` cap.

**A path** is a choice of one candidate at every node, end to end. Its score is
Σ(node emission scores) + Σ(edge transition scores) over the path.

**Edges.** An edge connects a candidate at node *i* to a candidate at node *i+1*. Its
weight is the transition score between them (rcb if the root continues; w_seq/w_dim if
the i+1 root stands in the V→I / leading-tone relation; step bonuses if the bass steps).
See §3 for the exact term-by-term assignment, including the two genuinely awkward
properties (rcb is multiplied by the destination cell's `cf×af`; the forward signals are
evaluated against a *cold-precomputed* lookahead, not the decoded successor).

**Candidate-set size control (beam-in).** Two regimes:
- **Beam-1 / byte-identity (Stage 3.1):** the node exposes exactly the candidates the
  current `results[]` builder would — top-3 + diff-root append, gated by the same
  threshold and cap. This is mandatory for byte-identity (§4).
- **Wider beam (Stage 3.2+):** the node exposes a per-region beam of the top-*K* cells
  (or all above a relaxed threshold) so the decode can revise an earlier region on later
  evidence. *K* is the knob; see §9.

**Memory envelope (Mozart-scale, 141 section nodes).** Beam-1: O(nodes) committed path
+ O(nodes × 4) emitted candidates — kilobytes. Wider beam storing the full snapshot per
node for re-decode: 141 nodes × ~250 cells × ~64 B ≈ **2.4 MB**, worst realistic case;
a top-*K*=8 beam-in is ~141 × 8 × 64 B ≈ **72 KB**. Either is negligible. The expensive
resource is **time** (Pass-0 re-analysis to *produce* the snapshots, §8), not lattice
memory. Conclusion: memory is a non-constraint at any beam width these scores reach.

---

## 3. Emission / transition factorization — term by term

The per-bass score the competition pipeline computes today
(`harmonicfunctionlayer.cpp:311–324`) is, exactly:

```
score = (basisIndep + rcb) × complexityFactor × augFactor
        + wCompleteBonus + wSeq [+ wDim] [+ stepIn + stepOut (Pass B)]
```

where `basisIndep` already carries `diatonicRootBonus` + `resolutionBonus` (oracle
temporal debt), and `basisDep` (folded into the first parenthesis as
`(basisIndep + rcb + basisDep)` — see the code) carries `appliedBassBonus` + the four
§4.1b inversion bonuses. Decoder homes:

| Term | §ref | Decoder home | Notes / awkwardness |
|---|---|---|---|
| `scoreTemplateTones`, `scoreExtraNotes` | §3/§4 | **Emission** (node-local) | pure vertical |
| `dim7CharacteristicBonus` (+0.75) | §4 | **Emission** | rotation selector; stays in oracle |
| structural penalties (sus/dom7♭5/power) | §4 | **Emission** | node-local |
| `tpcConsistencyBonus` | §4 | **Emission** | node-local |
| `diatonicRootBonus` (+0.30) | §4 | **Emission** | key-conditioned, node-local |
| `complexityFactor` (×) | §3 | **Emission** (multiplicative) | node-local |
| `augFactor` (×) | §3 | **Emission** (multiplicative) | node-local |
| `w_complete` (+0.50) | §4 | **Emission** | region-local joint term, not progression |
| `appliedBassBonus` / `bassNoteRootBonus` | §4/§5 | **Emission** (bass-dependent) | node-local |
| B2 aug7 guard | §4 | **Emission** (template skip) | node-local |
| `completeTriadInversionBonus` (+0.45) | §4 | **Transition-gated emission** | region-local quality test (complete triad, inverted, 3-PC) ACTIVATED by (back-edge bass-stepwise OR cold-lookahead forward-stepwise), `chordanalyzer.cpp:1613–1622` — migrates in 3.3 with the bundle; at beam 1 the forward half stays cold-lookahead (AWKWARD-3 applies) |
| `maxTotalInversionContextBonus` (cap 2.0) | §4/§5 | **Emission** (inert cap) | never binds (sums 1.85/0.75); carry as-is, note inert (see disposition below) |
| **`rootContinuityBonus`** (+0.40) | §4 | **Transition (back-edge)** | **AWKWARD-1:** folded into `basisIndep` *before* `×cf×af`, so its real edge weight is `0.40 × cf_dest × af_dest`, a *destination-conditioned* edge, not a constant |
| **Gate R** structural condition | §4 | **Transition** (modifies the rcb edge) | **AWKWARD-2:** the `basisDep ≤ 0` proxy couples to the oracle (§6); redesign required when inversion bonuses migrate |
| `resolutionBonus` (+0.35) | §4 | **Transition (back-edge)** today living in emission | on prevQuality→thisRoot; migrate in 3.3 (§6) |
| `stepwiseBassInversionBonus` (+0.50) | §4 | **Transition (back-edge)** today in `basisDep` | on previousBassPc; migrate in 3.3 |
| `stepwiseBassLookaheadBonus` (+0.50) | §4 | **Transition (forward-edge)** today in `basisDep` | on nextBassPc; migrate in 3.3 |
| `sameRootInversionBonus` (+0.40) | §4 | **Transition (back-edge)** today in `basisDep` | on previousRootPc; migrate in 3.3 — **this is the signal Gate R's `basisDep≤0` reads** |
| `w_seq` (+0.20) | §4 | **Transition (forward-edge)** | **AWKWARD-3:** on `ctx.nextRootPc`, a *cold-precomputed* lookahead, not the decoded successor (see below) |
| `w_dim` (+0.15) | §4 | **Transition (forward-edge)** | same cold-lookahead property; plus the global two-variant guard below |
| `w_stepIn` (+0.10) | §4 | **Transition (back-edge)** | on previousBassPc (committed predecessor) |
| `w_stepOut` (+0.10) | §4 | **Transition (forward-edge)** | on nextBassPc (cold lookahead) |
| **wDim post-bonus quality guard** (Iter 97a-v3) | §4 | **AWKWARD-4: node-local but global-across-basses** | two parallel scorings (with/without wDim); accept with-wDim only if its *region* winner is Dim/HalfDim. Stays *inside* node emission (does not cross region edges); 1a-F2 first-wins tie must be reproduced |
| **Pass-B m7-budget guard** | §4 | **Node-local** (within-bass-group competitor scan) | stays in emission; the `>=` boundary (1a-F4) is pinned |
| **score threshold / result cap** | §3/§11 | **Node-local** (candidate-set builder) | sets the beam-in at level 0 (§2); 1a-F5 (diff-root append only above threshold) must be reproduced |
| **Gates A–L** | §6 | **Post-decode re-rank initially → retired per 3.4** | mutate committed identity → feed transitions (see the coupling note) |
| **Iter 86/91 (`applyIter8691Pedal`)** | §1 | **Post-decode re-rank** (runs before gates) | same identity-mutation property |
| **pedal two-pass** | §1/§8 | **Node-local** (re-analyzes upper voices) | within-region; stays |

### The three structural subtleties the decoder must respect

**AWKWARD-1 — rcb is inside the multiply.** Because `rcb` is added to `basisIndep`
*before* `× complexityFactor × augFactor`, the continuation edge does not add a flat
+0.40 — it adds `0.40 × cf_dest × af_dest`. This is still a clean pairwise edge weight
(it depends only on the destination cell's own `cf`/`af` and whether `dest.rootPc ==
src.rootPc`), so it factors. But a decoder that models rcb as a constant +0.40 additive
edge **will not be byte-identical**. The edge-weight function must be
`rcbEdge(src, dest) = (dest.rootPc == src.committedRootPc ? 0.40 : 0) × dest.cf × dest.af`,
with Gate R able to zero the 0.40.

**AWKWARD-2 — Gate R reads `basisDep`.** Gate R withholds rcb when `basisDep ≤ 0` (proxy
for "no sounding third"). `basisDep` carries the inversion bonuses *from the oracle*. If
3.3 migrates those bonuses into the transition layer, `basisDep` stops carrying the
sounding-third signal and Gate R silently breaks. The two changes are one change (§6).

**AWKWARD-3 — forward signals use a cold lookahead, not the decoded successor.** This is
the deepest property and the key to byte-identity. In the current pipeline:
- *Backward* signals (rcb, w_stepIn, and the three back-edge inversion bonuses) read the
  **committed predecessor** identity (`ctx.previousRootPc/previousBassPc`, set by
  `advanceTemporalContext` on the gate-corrected winner).
- *Forward* signals (w_seq, w_dim, w_stepOut, stepwiseBassLookahead) read
  `ctx.nextRootPc/nextBassPc`, which are **independently pre-computed by a one-region
  cold lookahead** (`inferNextRootPc` / `backfillNextRootPc`), *not* the path's decoded
  successor.

The consequence for the decoder is precise and load-bearing (§4): at **beam 1**, the
forward signals must continue to read the cold lookahead — they are effectively
*emission-time features keyed on a fixed external value*, not true lattice edges. Only at
**wider beams** can they become genuine forward edges (against the decoded successor),
which is a deliberate, quality-level-gated *behavior change*, not byte-identical.

### Disposition of the inert cap

`maxTotalInversionContextBonus` (2.0) never binds (the four inversion bonuses sum to
1.85 Baroque/default, 0.75 Jazz — scoring_model §4 "currently inert"). It is computed in
the oracle (`bassDependentContextualBonuses`) and already baked into `basisDep`. The
decoder inherits it transparently and takes **no action**; it is documented as an untuned
safety net the Stage-5 fitting may revisit, not a decoder concern.

---

## 4. Beam-1 byte-identity argument

**Claim.** A beam-1 decoder with the §3 factorization reproduces the current greedy
pipeline byte-for-byte, on every score, both presets and Default.

**Why it holds.** The current pipeline *is already* beam-1 with transitions evaluated
against the committed predecessor and the cold lookahead:

1. **Per-region emission is unchanged.** The decoder calls the same oracle
   (`analyzeChord` → `ScoringSnapshot`) and the same competition body
   (`applyHarmonicFunction`) to produce each node's candidates. At beam 1 the node's
   exposed candidate set is exactly `results[]` (top-3 + diff-root, same threshold/cap).
2. **Backward edges = committed predecessor.** Beam-1 commits each node before moving on
   (greedy argmax). So "rcb edge against the decoded predecessor" and "rcb evaluated
   against `ctx.previousRootPc`" are the *same value* — the decoded predecessor *is* the
   committed predecessor. Identical for w_stepIn and the back-edge inversion bonuses.
3. **Forward edges = cold lookahead, preserved.** Beam-1 keeps w_seq/w_dim/w_stepOut/
   lookahead reading `ctx.nextRootPc/nextBassPc` (the cold pre-pass), *exactly as today*.
   No promotion to decoded-successor edges at level 0.
4. **Post-node corrections preserved and committed.** Per node, after the competition
   argmax the decoder runs `applyIter8691Pedal` then `applyPostScoringGates` (the same
   order as every production call site) and commits the **gate-corrected** identity as the
   predecessor context — exactly as `advanceTemporalContext(..., chosen)` does now. The
   inline same-root merge follows identically.

Because each step is the current code re-expressed, the selected winner and the emitted
alternatives at every node are unchanged.

**Where the equivalence could break — the tripwires.**

- **Floating-point evaluation order (the primary risk).** Winner selection uses **exact
  `double` comparison, no epsilon** (scoring_model §3). Two documented near-tie classes
  flip on a hair: the Δ=+7b ~0.02-margin class and bwv320 (≈1.92 vs 1.90). The decoder
  **must compute the per-bass score in the same arithmetic order**:
  `(basisIndep + rcb + basisDep) × cf × af + wComplete + wSeq [+ wDim] [+ step]`. Any
  re-association (e.g. summing edge weights separately then adding, or applying rcb as a
  post-multiply additive) changes the rounding and can flip a near-tie. This is the one
  place a "cleaner" decoder formulation silently regresses.
- **Tie policy.** The comparator (`score` desc, then `tiePriority` asc, then `rootPc`
  asc; `harmonicfunctionlayer.cpp:386–390`) must be reproduced exactly, including the
  1a-F2 first-wins storage-order tie in the wDim guard scan and the 1a-F5
  threshold-gated diff-root append.
- **Gate-context coupling.** The gates read live-vs-captured winner fields (1b-F4) and
  can leave `results[]` unsorted (1b-F6). Beam-1 must reproduce these as-is, not
  "fix" them (fixing is a conscious 3.4 decision, §7).

> **Gate re-baselined 2026-06-13 (corrected GT parser):** the BIR identity sets below
> (13/7/14) are the Stage-3 historical values; the gate is now **Baroque 53 / Jazz 24 /
> Default 53** (strict superset, see CLAUDE.md; the L3-wiring delta later moved 57/23/57 →
> 53/24/53). Any NEW byte-identity gate must hold against
> 53/24/53, not 13/7/14. The `24/13` `analyze_inversion_errors` figure is stale/pending.

**Verification plan (the Stage-3.1 gate).** Identical to every prior byte-identity gate:
1. **0/353 corpus A/B** on **Baroque + Jazz + Default** (`run_bach_preset.py` per-preset
   dirs + manifest; `.ours.json` diff must be empty on all three).
2. **Pipeline snapshots 11/11 zero diffs** (`pipeline_snapshot_tests.exe`).
3. **All suites green**: composing, notation, batch_analyze regression.
4. **BIR identity sets unchanged**: Baroque 13 / 24/13, Jazz 7 (`{bwv244.15, bwv245.17,
   bwv245.40, bwv422, bwv432, bwv45.7, bwv74.8}`), Default 14 (Baroque-13 ∪ {bwv187.7}).
5. **The Stage-1.7 near-tie FP canary** (`functionlayer_tests.cpp`, 0.02 near-tie) plus
   the Δ=+7b and bwv320 cases as explicit FP tripwire pins.

Any single diff is a hard stop — the restructure is not byte-identical and must be
reconciled before proceeding.

---

## 5. Path state vs `advanceTemporalContext`

`advanceTemporalContext` (chordanalyzer.h:819/849/888) is the greedy commit: it advances
`ChordTemporalContext` from the chosen (gate-corrected) winner — rolling
`consecutiveBassStepwiseCount`, the `recentRootPcs` window, `previous{Root,Bass,Quality}`,
and (the 3-arg+gateCtx overload) the Step-2 confidence fields.

**What replaces it.** The commit chain becomes **path state carried by each decode
hypothesis**. A path's state at node *i* is everything the next node's *backward* edges
and rolling features need:

| `ChordTemporalContext` field | Decoder path-state mapping |
|---|---|
| `previousRootPc` / `previousBassPc` / `previousQuality` | last committed candidate on this path (gate-corrected identity) |
| `consecutiveBassStepwiseCount` | per-path rolling counter (path-dependent at wider beams) |
| `recentRootPcs[3]` | per-path rolling window |
| `regionMetricWeight` | region-local (node property, path-independent) |
| `nextRootPc` / `nextBassPc` | **cold lookahead — NOT path state.** Stays a node-external precomputed value at beam 1 (AWKWARD-3) |
| `bassIsStepwiseFromPrevious` / `…ToNext` | derived: from-prev = path state; to-next = cold lookahead |

At **beam 1** there is one path, so path state ≡ the current single `ctx` — identical.
At **wider beams** each surviving hypothesis carries its own rolling state; this is
exactly what makes "revise an earlier commitment" fall out of backtracking.

**The Step-1/2 confidence fields' fate.** `previousWinnerScore/Margin/RootPcWeight`,
`previousDistinctPcs`, and the Step-1 free-wiring fields (`previousQuality`,
`recentRootPcs`, `consecutiveBassStepwiseCount`, `regionMetricWeight`) are **forwarded to
`HarmonicFunctionContext` but read by no scoring code today** (verified: nothing in
`harmonicfunctionlayer.cpp` consumes them). They are inert plumbing. The decoder keeps
them as **available path-state features for Stage-5 transition-weight fitting**, but at
beam 1 they remain unused → zero byte-identity impact. They are also inert on the bridge
path today (D-BRIDGE) — the decoder's path state *supersedes* that gap (§8).

**Sub-region (Pass 2/2b) handling.** Pass 2/2b sub-splitting and their commits
(`bassIsStepwiseToNext = false`, L621/L823) are **segmentation-internal** and run during
`ScoringPhase::Segmentation` (or as part of region production), *before* the final stream
the decoder consumes. The decoder does **not** touch them. This is the load-bearing
boundary: because segmentation stays as-is, the Stage-1.3 NOT-PINNED items
(`coalesceShortSameRootRuns`, Pass 2/2b boundaries + `minGapTicks` floor, sub-region
`bassIsStepwiseToNext`) are **not** triggered into hard-obligation status by Stage 3 — the
decoder must consume the post-Pass-3 stream and assert it does not alter segmentation
(verified by the segmentation tests in `regionanalysis_tests.cpp` staying green and the
preMergeRegions/postMergeRegions hook streams being unchanged). **If at any point the
decoder is extended to revise boundaries (the joint seg+label extension, §1), those three
NOT-PINNED items immediately become hard obligations** (roadmap 1.3 / Gate 1→2 exception).

---

## 6. Oracle temporal-signal migration (roadmap 3.3)

Five oracle-side signals are progression-flavored but live in `analyzeChord` as
"pre-existing temporal debt" (chordanalyzer.h:329/361 TODO). 3.3 migrates them into the
decoder's transition layer:

| Signal | Current home | Reads | New decoder home |
|---|---|---|---|
| `resolutionBonus` (+0.35) | oracle → `basisIndep` | previous chord *quality* | **back-edge** (prevQuality → thisRoot relation) |
| `stepwiseBassInversionBonus` (+0.50) | oracle → `basisDep` | `previousBassPc` | **back-edge** (bass stepwise from predecessor) |
| `stepwiseBassLookaheadBonus` (+0.50) | oracle → `basisDep` | `nextBassPc` | **forward-edge** (cold lookahead at beam 1) |
| `sameRootInversionBonus` (+0.40) | oracle → `basisDep` | `previousRootPc` | **back-edge** (root continuity, inverted reading) |
| `completeTriadInversionBonus` (+0.45) | oracle → `basisDep` | region-local quality test, but **ACTIVATED by OR-of-edges** (`bassIsStepwiseFromPrevious` ∨ `bassIsStepwiseToNext`); `chordanalyzer.cpp:1613–1622` | **edge-gated emission** — region-local quality *value*, emitted only when either bass edge is stepwise; migrates in 3.3 with the bundle (back half = back-edge gate, forward half = cold-lookahead at beam 1, AWKWARD-3) |

So of the "5 signals," **four are clean single-direction transition edges** (resolutionBonus
back-edge, stepwiseBassInversion back-edge, stepwiseBassLookahead forward-edge,
sameRootInversion back-edge) and the fifth (`completeTriad`) is an **edge-gated emission**
term: a region-local quality *value* emitted only when either bass edge is stepwise
(OR-of-edges, `chordanalyzer.cpp:1613–1622`). **All five migrate** with the inversion-bonus
bundle in 3.3 (the roadmap's "4 inversion bonuses" + resolutionBonus) — the earlier draft's
claim that completeTriad "stays emission" read the region-local *qualifier*
(`qualifiesForCompleteTriadInversionBonus`) and missed the temporal *call-site gate*
(`hasStepwiseBassEvidence`), corrected per the 2026-06-09 layer audit (Finding 1). At beam 1
completeTriad's forward (to-next) half stays cold-lookahead (AWKWARD-3). This interacts with
the Gate R coupling below: completeTriad and `sameRootInversion` both live in `basisDep`, so
migrating them is part of why the `basisDep ≤ 0` proxy must be replaced.

**The Gate R `basisDep ≤ 0` redesign — same change, mandatory.** Gate R uses
`cell.basisDep <= 0` as a proxy for "this continuation has no sounding third," which works
*only* because `sameRootInversionBonus` (fires when the third sounds) is computed in the
oracle and folded into `basisDep` (the cross-layer dependency documented at
`harmonicfunctionlayer.cpp:300–307`). Once `sameRootInversionBonus` migrates out of
`basisDep` into a transition edge, `basisDep` no longer carries the sounding-third signal
and Gate R misfires.

**Replacement condition.** Redesign `gateRZeroesRootContinuity` to test the sounding
third **directly from the snapshot**, not via `basisDep`:

```
withhold rcb  ⇔  rcb > 0
              ∧  the candidate's third is NOT sounding
                   (pcWeight[(rootPc + thirdInterval) mod 12] ≤ presenceThreshold,
                    thirdInterval from the candidate's quality: 4 Maj / 3 min)
              ∧  bass foreign to the candidate's template
                   (bassIsTemplateChordTone == false, unchanged)
```

This preserves the exact discriminator the current proxy encodes (the `Cm7add11/F`
counter-example has a sounding third → spared; the Δ=+7b bare-root continuations have no
sounding third → gated) while removing the dependence on where the inversion bonus lives.
The `gater_tests.cpp` F1/F2 pins and the Δ=+7b end-to-end pins (diagnose_tests,
roadmap 1.5) are the proof obligation for this redesign — they must stay green, or be
consciously re-baselined with a documented reason.

**Sequencing constraint.** 3.3 must not land before the migration of `sameRootInversion`
is in the same commit as the Gate R redesign. Splitting them across commits leaves a
window where Gate R reads a `basisDep` that has lost its signal — a silent regression.

### §6 amendment — Gate R reconstructed-credit (2026-06-12, Stage 3.3 implementation)

> Dated amendment recording the Stage-3.3 implementation outcome. The "Replacement
> condition" above (the literal `pcWeight[third] ≤ presenceThreshold` sounding-third test)
> was **superseded by derivation** during implementation and Cowork-ratified to the
> **reconstructed-credit** form. This supersedes the §6 "Replacement condition" block.

The survey (`cc_stage3_3_report.md` §1) derived the old proxy's exact meaning. Under Gate
R's only firing context (`rcb > 0` ∧ bass foreign), the bass-root bonus is necessarily 0
(it needs `rootPc == bassPc`), so `basisDep_old = nonBassAdjustment + cappedInv`; because
the **minimum inversion bonus (`sameRoot` 0.40) strictly exceeds the maximum penalty
(`kNonBassPenalty` 0.35)**, the old gate fires **⟺ `cappedInv == 0`** (the candidate earned
no inversion credit).

The literal sounding-third pcWeight test matches this for Maj/Min/Aug/HalfDim (all in the
`isInvertedMajMin` set → a sounding third fires `sameRoot`) and for the no-third qualities
(Sus/Power, always gated), but **diverges on Diminished**: Dim is excluded from
`isInvertedMajMin`, so its only credit is `completeTriadInversionBonus`, which additionally
requires a *stepwise-bass* edge — a temporal condition no vertical pcWeight test can
capture. A Dim continuation with foreign bass + sounding third but no stepwise bass earns
no credit (old gate fires) yet shows a sounding third (literal test would spare it): a 0.40
× cf × af, output-visible swing — not byte-identical.

**Ratified form (Cowork, 2026-06-12).** Gate R reads the **pipeline-reconstructed full
basisDep** (`cell.basisDep + fn::inversionContextBonus(...)`, which Pass A computes for the
score anyway) via the 3-arg `gateRZeroesRootContinuity` overload. This is byte-identical to
the old proxy on every quality (it reads the same total credit), is fully intra-layer
(closes the cross-layer dependency the redesign set out to remove — audit Finding 6), and
has no Dim gap. The "direct pcWeight third" mechanism was an approximation of the proxy's
true semantics (`cappedInv == 0`); reading the true semantics is the faithful execution of
the redesign's *intent*. The originally designed mechanism text is retained above for the
record but is not what shipped.

---

## 7. Gate-retirement plan (roadmap 3.4 / 3.4b)

A gate is removed **only** when the decoder reproduces its pinned fixes; the Stage-1.1
`postscoringgates_tests.cpp` tests (48 tests) are the per-gate proof obligations. Until
then every gate stays as a **post-decode re-rank** applied per node (exactly as today),
so the decoder is a drop-in.

| Gate | §6 disposition | Verdict | Proof-obligation tests |
|---|---|---|---|
| Bias correction | decoder-subsumed (proper inversion edges remove the over-fired bass-root bonus when it is the sole decider) | **stays re-rank → retire after 3.3** | bias-bracket tests |
| **A** (Min-add6 ↔ HalfDim7 flip) | enharmonic quality choice on identical PC sets, preset + key-function dependent | **stays re-rank** (likely a Stage-6 functional decision long-term) | Gate A / FM2 fire tests |
| **B / C / D** | provably unreachable (A always wins — 1b-F1) | **retired-dead (3.4b)** — byte-identical removal, *as part of* the deliberate retirement audit, not a hygiene pass | dead-code: removal must keep all suites byte-identical |
| **E** (1st-inv minor → major) | inversion swap | **decoder-subsumed after 3.3** (inversion edges) | Gate E pcWeight-guarded test |
| **F** (2nd-inv → root major) | inversion swap; has **no** winner-quality/alt-root guard (1b-F5) | **decoder-subsumed after 3.3**; the missing guards (F5 asymmetry) are a *conscious re-decide* at retirement | Gate F stepwise test |
| **G-E / G-B/C/D** (Min-add6 ↔ HalfDim7, key-function) | G-E gates on viiø7/iiø7/iiiø7 function | **stays re-rank** → Stage-6 functional layer; G-E's threshold-free pull (1b-F7) + duplicate push (1b-F8) must be reproduced or re-decided | Sub-9a test (G-E), G-B/C/D temporal tests |
| **H** (aug rotation) | rotation selection | **stays re-rank** initially (a wDim-style forward edge may subsume) | Gate H temporal tests; mixed live/captured (1b-F4) |
| **I / K / L** (inversion / aug corrections, margin-gated) | inversion/quality swaps with margin ≤ 0.45 / 0.20 / 0.35 | **decoder-subsumed after 3.3**; the margins become decode tie-breaks | Gates I/K/L margin tests |
| **J** (vii° → V7 completion) | structural 4-PC identity (`{R−4,R,R+3,R+6}` = V7) | **survives longest** (healthy, structural) — eventually an emission/functional decision, not a greedy gate | Gate J bwv110.7 end-to-end (1.5) |
| **Gate R** (rcb bass-chord-tone) | structural transition rule | **absorbed into the rcb edge**, not retired — it *is* the decoder's continuation-edge guard (redesigned per §6) | gater_tests F1/F2, Δ=+7b pins |

**Stage-1a obligations the decoder must consciously honor or re-decide.**
- **1a-F2** (post-bonus quality-guard winner scan is first-wins on exact ties): the wDim
  two-variant guard's accept/reject decision is storage-order-sensitive on an exact tie.
  Beam-1 reproduces it; any decoder re-expression must keep the first-wins semantics or
  document a re-decide.
- **1a-F5** (diff-root append never appends sub-threshold candidates): the "guaranteed
  inversion alternative" is only guaranteed among above-threshold candidates. The
  decoder's candidate-set builder must reproduce this exactly.
- **1b-F4** (mixed live/captured winner reads in H/I/K/L): after a bias re-sort these
  gates can reference *different* candidates than they key on. The decoder, while keeping
  them as re-rank, must reproduce the half-migrated reads — or fix them as a conscious,
  separately-verified re-decide (not silently).

**Retirement gate (per gate).** A per-gate **differential report**: remove the gate,
run the corpus A/B; the gate's pinned tests must be reproduced by the decoder (green
without the gate) and the BIR identity sets must not regress on any of the three configs.

---

## 8. Decode-once, query-many (P3 / P4 / bridge)

This is the design opportunity the 2.5 baseline surfaced (`docs/perf_p3_baseline.md`;
roadmap 3.1 note): the decoder converts P3 from a *cost* into a *performance fix*.

**Today (P3).** Every status-bar query re-runs Pass-0 (`analyzeHarmonicRhythm`) +
`analyzeSection` over an expanding ±measure window, up to 9 times, **with no caching**.
Median 86–215 ms, p95 up to 2.75 s, worst single click ~7 s (Mozart K279-1 m68). **Pass-0
is ~98–99.9% of the cost; `analyzeSection` — the layer the decoder restructures — is
< 0.3 ms.** So the decoder's *own* work is negligible; the win is **caching the analysis**.

**Decode-once.** Compute a **per-score lattice + decoded path once**, cache it, and make
each P3 tick query a **lookup** of the committed candidate at that tick. The first query
pays one whole-needed-window decode (≈ today's cost); every subsequent query is O(log
regions) lookup → **orders below the 33–215 ms medians**. This is the roadmap-3.1
"decode once, query many."

**Cache invalidation — bounded re-decode window, not full incrementality.** A score edit
invalidates a bounded neighborhood, because transitions are local:
- An edit to region *i*'s tones invalidates *i*'s emission (re-run Pass-0 over the edited
  measures) and the decode of regions in *i*'s **edge horizon**: backward edges reach 1
  region; the forward cold-lookahead reaches 1 region; so re-decode `[i−1, i+1]` at beam 1
  (wider at higher beams: `[i−beamHorizon, i+beamHorizon]`).
- The design **does not promise full incremental re-decode** — it promises a bounded
  window proportional to the edit span + a small constant horizon. Anything touching
  segmentation boundaries (note add/remove that changes region count) widens the window to
  the affected segmentation span.

**Before the cache is warm.** The first query (or first after invalidation) computes the
window decode at today's cost. There is **no regression** versus today for the cold case;
the win is entirely on the warm repeat queries (the common interactive case).

**P4 and the bridge consume decoded path state — closing D-P4 / D-BRIDGE.** Both
divergences (ARCHITECTURE.md "Path divergence decisions") are *deferred to Stage 3 by
explicit revisit trigger*. The decoder resolves them:
- **D-P4** (tick-local fallback builds context cold via `findTemporalContext`): under
  decode-once, P4 reads the **decoded path's committed state** at the tick instead of a
  cold neighbor walk. Stage 3 design therefore **states explicitly**: P4 consumes the
  cached decoded path; the cold `findTemporalContext` walk is superseded. (If P4's
  empty-window fallback rate is ever shown non-trivial — currently 0/2231 on the perf
  corpus — the per-tick API would need instrumenting, but that does not change the
  contract.)
- **D-BRIDGE** (predecessor analyzed with null context; Step-1/2 fields inert): the
  bridge consumes the decoded path state, so the inert Step-1/2 confidence fields and the
  cold-predecessor walk are both replaced by the path's committed predecessor. **This is
  the global-decode product the D-BRIDGE decision said Stage 3 would provide — stated
  here as the explicit closure.**

**Open dependency:** decode-once requires deciding cache *scope* (whole-score vs the
needed window) and *ownership* (where the cache lives relative to the bridge). See §13 Q1.

---

## 9. Quality levels ↔ beam width (ARCHITECTURE §2.14)

| Level | Beam | Behavior | Budget |
|---|---|---|---|
| **0** Fast / real-time | **1** | byte-identical to current greedy; forward signals = cold lookahead | per-query p95 ≤ 2.5-baseline × **1.10** (perf doc) — but see decode-once below |
| **1** Normal | small (top-*K*, e.g. K=4–8) | forward signals may become true decoded-successor edges; revises an earlier region on later evidence | background/default export; not interactive-bounded |
| **2** Deep / publication | exact / wide DP | full path optimization | LLM-assisted / academic |

**Budget nuance (state separately, per the instruction).** The perf doc's
`p95 ≤ baseline × 1.10` is the gate for the **decoder's own added latency** assuming the
*current uncached query model*. Because the decoder lives in the < 0.3 ms
`analyzeSection` layer, beam-1 must add < 1 ms per region — trivially within ×1.10. **The
decode-once expectation is the opposite of a regression**: it makes P3 *faster* by
removing the uncached Pass-0 re-analysis. So the level-0 promise is two separate claims:
(a) decoder adds < 1 ms/region to a single analysis; (b) under decode-once, warm P3
queries drop orders below the 86–215 ms medians.

**Where the knob lives.** A quality-level field on `ChordAnalyzerPreferences` (alongside
`scoringPhase`), read by the decoder. No preset coupling (§10).

---

## 10. Config-agnosticism

The decoder takes `ChordAnalyzerPreferences` exactly as the current pipeline does and
contains **no preset logic**. Per D-PASS0 (ARCHITECTURE.md), the chord-scoring presets
are a **batch-tools-only artifact** — the live product runs `kDefaultChordAnalyzerPreferences`
(struct defaults), which matches no named batch preset. The decoder must not branch on
preset; all preset behavior (Jazz's reduced inversion bonuses, etc.) is already encoded in
the `prefs` values the oracle consumes.

**Evaluation column.** The user-relevant configuration is **`--preset Default`** (struct
chord defaults + the app's bespoke mode priors): BIR=false 14 = Baroque-13 ∪ {bwv187.7}
(D-PASS0 V4; **re-baselined 2026-06-13 → Default 53 (L3-wiring delta 2026-06-26), see CLAUDE.md**). The Baroque gate stays the primary calibration gate per CLAUDE.md; Jazz is
the non-Baroque hard-stop. Gate thresholds stay Baroque/Jazz-calibrated — the decoder
does not re-tune them (that is Stage 5).

---

## 11. Acceptance-case roster — classified by what unlocks each

> **⚠ ERRATUM (2026-06-13, applied — was the standing queued rider in COWORK_HANDOFF;
> re-confirmed by the foundations-verification run `cc_foundations_verification_report.md`).**
> The **Δ=+7a** and **C2 / bwv320-class** rows below carry a FALSIFIED verdict. The 3.2
> design (`docs/beam_widening_design.md` §3, Cowork-verified ×3 incl. the independent
> June-9 redesign_plan numbers) proved a wider/global beam does **NOT** fix Δ=+7a: the
> wrong-root micro-region is the **HIGHEST-scoring node** (locally correct — the DCML root
> is absent from its tones), so the continued-root path is the **genuine global optimum** a
> decode finds *exactly as greedy does* (greedy 5.775 > correct 5.600 on bwv102.7; gap =
> rcb 0.40 − margin 0.225). The "rcb edge **from a low-scoring transient** does not survive
> against the path through the correct root" premise is therefore **wrong** — the transient
> is not low-scoring. Re-ranking cannot fix Δ=+7a; only **re-weighting** (Stage-5 rcb
> reweight + forward-completion edge) or **joint segmentation** can. Δ=+7a is **removed from
> the 3.2 beam-win column and routed to Stage 5** (see `implementation_roadmap.md` row 3.2;
> META-PRINCIPLE block; `docs/back_half_design.md` §1). The **C2 / bwv320-class** row's cited
> example is dead (bwv320 m27 = the Gate-R-fixed Δ=+7b instance at the same tick; reconciled
> 2026-06-12) — no known live instance; do not promise it. This also voids the §12 Q2
> ratification's rationale clause "*the Δ=+7a inter-region revision depends on [forward
> decoded-successor edges]*" — the forward-edge promotion may remain desirable on its own
> merits, but Δ=+7a is **no longer its justification**. The **Δ=+7b trio** (next-but-one row)
> is unaffected and remains must-not-break. Rows are retained verbatim below as the
> historical record; this erratum supersedes their Δ=+7a / C2 verdict cells.

| Case | What it is | Verdict | Evidence |
|---|---|---|---|
| **Δ=+7a** bwv102.7, bwv261 | wrong-root **micro-region** (240-tick arpeggio step, root attacks +240t in the future) feeds rcb +0.40 into the *sibling* region, tipping it; the oracle *prefers* the DCML root in the present-root slice (AbMaj7 2.55 > Eb/Ab 2.33) | **Stage 3 (wider beam) should fix** — this is the canonical inter-region revision: a global decode does not irrevocably commit the transient wrong root, so the rcb edge from a low-scoring transient does not survive against the path through the correct root. Gate R is inapplicable (`basisDep > 0`); only the decode fixes it | COWORK_HANDOFF Δ=+7a; redesign_plan Step 4 (Phase D fully exhausted, 3 dead ends) |
| **C2 / bwv320-class rcb near-ties** | rcb +0.40 makes a continued-root reading (G/E 1.92) beat the vertically-correct triad (Cmaj 1.90) by 0.02 | **Stage 3 (wider beam) target** — rcb as an *edge*, not an irrevocable commit, lets the globally-better path win. **Caveat:** the specific Δ=+7b bwv320 instance is already **Gate-R-fixed and pinned** (see next row) — must not be confused or broken; the residual C2 m27 class is the wider-beam target | COWORK_HANDOFF C2 (accepted residual, Iter 98 dead end); scoring_model §4 Gate R |
| **Δ=+7b trio** bwv245.28, bwv296, bwv320 | correct first-inversion triad; near-tie broken by rcb toward the old root; bass = M6 of continued root (foreign to all templates) | **Stage 3 must NOT break** — Gate-R-fixed, pinned (gater_tests F1/F2, diagnose Δ=+7b acceptance). The decoder's rcb edge + §6 Gate-R redesign must reproduce these byte-identically | STATUS Gate R commit `638ced1c12`; scoring_model §4 |
| **A2** dominant-as-major in minor keys | degree-5-in-minor mapped to natural-minor v instead of major V | **Stage 4 + 6** — key/cadence, not vertical. `keyConfidence` has no bimodal gap (267 slices); top-kc tier 29% FP. Needs cadence confirmation (Stage 6) over a key path (Stage 4). **Not a Stage-3 chord-decode win** | COWORK_HANDOFF A2 (full investigation, both discriminators exhausted) |
| **B1** mMaj7 {0,3,7,11} template | bare template misreads Baroque V→i as i(maj9); leading-tone ambiguity | **Stage 6** (cadence confirmation) — needs a voice-leading-resolution signal (is the leading tone resolving?), a functional-role property. A bare template is rejected (project memory `backlog_b1_mmaj7_template`). Not chord-decode-alone | COWORK_HANDOFF B1; ARCHITECTURE §2.14 functional-role↔identity |
| **C1** schumann tick-480 viio7/V (C#°7) | the 240-tick leading-tone dim region is **absorbed by segmentation** before the chord decode sees it | **Joint seg+label (beyond Stage 3) or the absorption exception** — out of Stage-3 chord-decode scope (which keeps segmentation as-is). Also needs nextRootPc into P4 for the wDim rotation. **Not fixable by chord decode over fixed boundaries** | COWORK_HANDOFF C1 (two independent fixes, one is absorption) |
| **bwv187.7** m14.b2 Gm7/F | first known user-experienced error outside every gate; mode-prior-surfaced | **Stage 4** (mode-prior / key-sensitive) — appears in the Default config (mode priors diverge from named presets on 11/21 modes). Key-path territory | ARCHITECTURE D-PASS0 V4 |

**Expected-movement table (beam-1 vs wider beam), Default eval column.**

| Quantity | Beam-1 (Stage 3.1) | Wider beam (Stage 3.2) |
|---|---|---|
| Default BIR=false (Stage-3: 14) | **unchanged, byte-identical** | re-baselined 2026-06-13 → **53** (L3-wiring delta); targets Δ=+7a-class — *measure, do not promise a number* |
| Gate identity sets (Stage-3: Baroque 13 / Jazz 7 / Default 14) | **unchanged** | re-baselined 2026-06-13 → **53 / 24 / 53** (CLAUDE.md; L3-wiring delta); hard-stop: no identity-set regression on any config |
| Pipeline snapshots | **11/11 zero diffs** | refresh only verified-correct output changes |
| Gates fired | **identical** | progressively retired (§7) with per-gate differential |

---

## 12. Migration sequencing + risks

**Design section → roadmap row.**

| Roadmap | Design sections | Deliverable |
|---|---|---|
| 3.1 decoder skeleton, beam-1 | §2, §3, §4, §5 (+ §8 evaluated as opportunity) | byte-identical lattice; 0/353 × 3 configs |
| 3.2 widen beam behind quality level | §9, §11 expected-movement | per-case A/B; no level-0 regression |
| 3.3 migrate oracle temporal signals + Gate R redesign | §6 | one commit; Stage-1 pins green or re-baselined |
| 3.4 / 3.4b gate retirement | §7 | per-gate differential; B/C/D dead removal |
| 3.5 file split + API rename | (interface only — not designed here) | file map in ARCHITECTURE.md |

**Sequencing note (Q3 DECIDED, Cowork ratification 2026-06-12).** For any gate that mutates
root/quality/bass identity, **3.4 retirement leads 3.2 beam-widening past that gate**: the
identity-mutating gate is retired or folded into emission *before* the beam widens past it,
so the identities entering the lattice are already gate-corrected and the backward edges
read a stable predecessor. The table order above is the default track; this exception
re-orders 3.4-before-3.2 on a per-gate basis (a structural gate like J that never mutates a
committed identity does not force the re-order). Option (b) — wider-beam edges against
pre-gate identities with a documented re-decide — was considered and **not** taken.

**Riskiest assumptions (in priority order).**
1. **FP byte-identity under restructuring** (§4) — the near-tie tripwires (Δ=+7b 0.02,
   bwv320). Mitigation: compute the score in the exact current arithmetic order; the
   Stage-1.7 canary + Δ=+7b/bwv320 explicit pins are the tripwires.
2. **Gate-mutates-transition-context coupling at wider beams** (§3/§7) — gates change the
   committed identity, which feeds backward edges, so "decode then gate" cannot be cleanly
   separated at beam > 1. Mitigation: retire-or-fold gates into emission (3.4) *before*
   widening the beam past them, or restrict wider-beam edges to use pre-gate identity with
   a documented re-decide.
3. **Gate R `basisDep ≤ 0` redesign** (§6) — must land atomically with the inversion-bonus
   migration. Mitigation: single commit; gater_tests + Δ=+7b pins.
4. **Decode-once cache invalidation** (§8) — a too-narrow window yields stale labels.
   Mitigation: bounded window proven against the edge horizon; conservative widening on
   segmentation-affecting edits.

**Behind a flag vs in place.** The decoder skeleton lands **behind the quality-level knob
with beam-1 as the default**, so production behavior is byte-identical until a level is
raised. Gate retirement is **in place, one gate at a time**, each its own commit with the
per-gate differential + corpus A/B. The oracle and segmentation are untouched throughout.

**Rollback story (per step).** Each step is an isolated commit gated on byte-identity
(3.1), per-case A/B (3.2), Stage-1 pins (3.3), or per-gate differential (3.4). Any failed
gate → revert that commit; because the decoder is flag-defaulted to beam-1 and gates are
removed one at a time, every prior state is a clean recoverable baseline.

---

## 13. Open Questions — DECIDED (Cowork ratification, 2026-06-12)

Genuine forks where the design carried a recommendation. **All seven decided at
ratification (Cowork, 2026-06-12); every recommendation was accepted.** Original
recommendation text retained for the record; the `DECIDED` line is the binding verdict.

- **Q1 — Decode-once cache scope and ownership.** Whole-score decode cached once, or the
  needed ±window per query? Whole-score is simplest to reason about and gives the biggest
  warm-query win, but costs one full Pass-0 upfront (≈ today's worst single query) and
  needs an invalidation hook on score edits. Where does the cache live — in the bridge, or
  a new per-score analysis cache object? *Recommendation: whole-score decode, cached in
  the bridge, bounded-window invalidation (§8).*
  **DECIDED (Cowork ratification, 2026-06-12):** whole-score decode, cached in the bridge,
  bounded-window invalidation — biggest warm-query win and simplest to reason about; the
  upfront full Pass-0 is the cold case that already exists today, so no regression (§8).

- **Q2 — Forward signals at Level 1.** At beam 1 the forward signals (w_seq/w_dim/
  w_stepOut/lookahead) must stay on the cold lookahead for byte-identity. Should Level 1
  promote them to **true decoded-successor edges** (more correct, but a behavior change),
  or keep the cold lookahead and only widen the *backward* search? *Recommendation:
  promote forward signals to true edges at Level 1 — it is the point of the decode and the
  Δ=+7a fix likely depends on it.*
  **DECIDED (Cowork ratification, 2026-06-12):** Level 1 promotes forward signals to true
  decoded-successor edges — that promotion is the substance of the decode and the Δ=+7a
  inter-region revision depends on it; beam 1 stays on the cold lookahead for byte-identity.

- **Q3 — Gate-mutates-context ordering.** At wider beams, do we (a) **retire/fold gates
  into emission first** (so identities entering the lattice are already gate-corrected),
  or (b) allow wider-beam edges against pre-gate identities with a documented re-decide?
  *Recommendation: (a) — sequence 3.4 gate retirement to lead 3.2 beam-widening for any
  gate that mutates root/quality/bass.* **Decision: yours; affects 3.2/3.4 ordering.**
  **DECIDED (Cowork ratification, 2026-06-12):** (a) — identity-mutating gates are
  retired/folded BEFORE the beam widens past them; **3.4 leads 3.2 for those gates** (a
  gate that mutates root/quality/bass feeds backward edges, so it cannot be cleanly
  separated from a wider-beam decode). §12 sequencing note updated to match.

- **Q4 — 1b-F4 half-migrated live/captured reads (H/I/K/L).** Reproduce the
  storage-order/live-vs-captured artifacts exactly during migration, or **fix them** as a
  conscious re-decide while the gates are being retired anyway? *Recommendation:
  reproduce at beam-1 (byte-identity), then fix-as-retire in 3.4 with a per-gate
  differential.*
  **DECIDED (Cowork ratification, 2026-06-12):** reproduce the 1b-F4 live/captured
  artifacts exactly at beam-1 (byte-identity gate), then fix-as-retire per-gate in 3.4 with
  a per-gate differential — never a silent fix.

- **Q5 — Output interface to Stage 4/6.** Does the decoder emit, per region, the
  **gate-corrected committed identity only**, or the **full ranked path with alternatives
  and margins**? Stage 6 (functional labeling) wants the latter (evidence-forwarding).
  *Recommendation: emit the path + per-node alternatives + margins; the committed identity
  is `path.front()` by construction.*
  **DECIDED (Cowork ratification, 2026-06-12):** emit the full path + per-node alternatives
  + margins (evidence-forwarding) — Stage 6 functional labeling consumes the alternatives;
  the committed identity is `path.front()` by construction.

- **Q6 — Beam-in width at Level 1+.** Top-3 + diff-root (byte-identical emission) is
  mandatory at beam 1. For Level 1, what per-region candidate width *K* (top-K cells, or
  a relaxed threshold)? *Recommendation: start K = 8 (well above the current ≤4) and tune
  at Stage 5.*
  **DECIDED (Cowork ratification, 2026-06-12):** Level-1 beam-in starts at **K = 8**; Stage 5
  tunes it. Top-3 + diff-root stays mandatory at beam 1 (byte-identity).

- **Q7 — Is the P3 perf fix (decode-once) part of Stage 3.1 or a separate track?** The
  roadmap frames it as a 3.1 *design opportunity*; the perf doc calls the uncached-Pass-0
  cost a "separate pre-existing optimization track." They can be decoupled: 3.1 can ship
  the byte-identical decoder *without* caching (proving correctness), and decode-once lands
  as a follow-on. *Recommendation: design the decoder cache-ready in 3.1 but land caching
  as 3.1b after the byte-identity gate passes, so the two risks (correctness, caching) are
  verified independently.*
  **DECIDED (Cowork ratification, 2026-06-12):** 3.1 ships **cache-READY without caching**
  (proving byte-identity correctness in isolation); **decode-once lands as 3.1b** once the
  byte-identity gate passes — correctness and caching risks verified independently.

---

*End of draft. Awaiting ratification addendum before commit (roadmap rule 4).*

---

## §8 amendment — 3.1b outcome (2026-06-12): Q1 re-decided, whole-score shelved

> Dated amendment recording the Stage-3.1b implementation outcome. The §8 "decode-once,
> query-many" design and Q1 (whole-score decode cached in the bridge) were implemented,
> **measured**, and **revised on the evidence**. This supersedes the relevant Q1/§8 text.

**Q1 RE-DECIDED → bounded-window cache.** Q1's ratified answer (whole-score decode) was
implemented and shipped behind the orchestrator, then **shelved** when the answer-delta
A/B (`docs/p3_granularity_ab_3_1b.md`) falsified its premise that whole-score context is
better:
- whole-score changed the displayed P3 chord on **32–40% of ticks** on contrapuntal/large
  scores (0% on small/homophonic);
- the change is **coarser** (batch/section granularity), and **not more DCML-correct** —
  combined root verdict **59/41 in the WINDOW path's favour**, **Mozart 35/65 against
  whole-score**.

3.1b instead ships a **bounded-window cache**: it memoizes the per-window section build
(`buildWindowSection` = Pass-0 + `analyzeSection`) inside the **unchanged** expanding-window
P3 path. Because that build is a pure function of (score, window bounds, excludeStaves) under
a fixed score, memoizing it is **byte-identical** — zero answer-delta, snapshots 11/11 with
**no golden refresh**. The warm win is now **local** (re-click / same-measure neighbour
hits cached window sections); the whole-score variant's cross-measure warm win is forfeited
as the accepted cost of byte-identity. Key: `(windowStart, windowEnd)` under a
`(score, undo-token, excludeStaves)` guard; conservative whole-cache flush on token change.

**D-P4 / D-BRIDGE closure ROLLED BACK.** §8's claim that decode-once closes D-P4/D-BRIDGE
("P4/bridge consume the decoded path state") **depended on the whole-score decode** and is
**rolled back to the 2.4 documented-contract state**. P4 stays on its cold
`findTemporalContext` path (it fires 0/2231 on the perf corpus). Closing D-P4/D-BRIDGE now
depends on the **granularity decision**, not on this cache — deferred with that decision.

**§1.4 erratum (instruction premise).** The Stage-3.1b instruction (and the §8 framing)
assumed the pipeline-snapshot harness "calls the raw functions and stays byte-identical."
The **P3 snapshot (`buildTickRegionalArray`) calls the orchestrator
`analyzeHarmonicContextAtTick`**, so it flows through whatever the orchestrator does. Under
the shelved whole-score variant this made all 11 snapshots drift; under the shipped
bounded-window cache it is byte-identical (the whole point). Recorded so the premise is not
repeated.

**Granularity is a recurring Stage-5 question, not a cache choice.** The window-vs-whole-score
A/B is the 2.2-i granularity finding recurring: the fine per-tick view is more DCML-accurate
per tick; the coarse section view is self-consistent with the chord track. **Whether the
status bar should match the chord track (whole-score) or resolve the chord at the clicked
note (window) is a product/Stage-5 decision** — it needs the granularity-robust metric the
2.2-i dossier mandated, not a cache architecture. Parked accordingly; evidence preserved in
`docs/p3_granularity_ab_3_1b.md`. Do not re-attempt whole-score P3 before that decision.

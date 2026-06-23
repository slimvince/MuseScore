# Stage 3.2 — Beam-Widening Design

> **Status: SHELVED (2026-06-13, Cowork+user) — NOT ratified for implementation.**
> The §3 finding (a wider beam does NOT fix Δ=+7a — verified) removed beam-widening's
> marquee justification; gate-folding and edge-reweighting are beam-1 operations, so
> beam>1 has no current motivating case and is deferred until a "search genuinely
> matters" case appears. This doc is RETAINED for its §3 derivation (the Δ=+7a
> lattice walk) and its gate-fold analysis (§5), both of which feed the
> precision-headroom investigation and any future Stage-5 work. Superseded as the
> next action by `cc_instruction_precision_headroom_investigation.md`.
> *(original draft header below)*
>
> **DRAFT — design-only, no production code.** This is the Stage 3.2 design deliverable per
> `docs/decoder_design.md` §9/§11/§12 and `docs/implementation_roadmap.md` Stage 3 row 3.2.
> It is the **first intentional behavior change** of the Stage-3 plan; everything since the
> reviews has been byte-identical. Companion drafting report: `cc_stage3_2_design_report.md`
> (probes run, the Δ=+7a lattice walk, load-bearing claims, open-question forks).
>
> *Written 2026-06-13 (CC). Base commit `a652dc1ba7` (Stage 3.4-i complete; HEAD
> output-identical to `548adb7b2e`). Owner: CC (design) / Cowork + user (ratification).*

**Sources read in full (or in the cited section):** `docs/decoder_design.md` (the ratified
Stage-3 design — esp. §3 AWKWARD-3 cold-lookahead, §9 quality↔beam, §11 acceptance roster,
§13 Q2/Q3/Q6); `cc_stage3_4i_dossier.md` (the per-gate differential dry-run + C2 roster);
`cc_stage3_4ii_report.md` (the non-chorale spot-check, K/Iter-86 caution, E/F C2′);
`docs/redesign_plan.md` Step 4–5 (Δ=+7a: Phase D's three dead ends, the "inter-region
revision is architectural, not a gate" conclusion); `COWORK_HANDOFF.md` (Δ=+7a / Δ=+7b
distinction, the must-not-break trio); `cc_deltaseven_7a_diagnostic_report.md` (the full
per-cell oracle dump — the lattice walk's source numbers); `docs/scoring_model.md` §3/§4/§6.

**The headline finding, stated up front (§3 derives it).** The part-1 thesis — that a wider
beam dissolves Δ=+7a because "a global decode never irrevocably commits the transient wrong
root" — **does not survive the derivation.** Walked through the actual cell scores, the
transient micro-region is **locally correct and the highest-scoring node in its
neighborhood** (not a low-scoring wrong guess), and the continued-root (wrong) path is the
**global score optimum** a beam decode will find. **At K=8 over the fixed segmentation, the
wider beam does NOT fix bwv102.7 or bwv261.** This is a finding, not a failure papered over;
it reshapes the acceptance roster (§6): Stage 3.2's measurable wins are the **gate-subsumption
set** (Gate I, bias, K, Iter-86, L), not Δ=+7a. Δ=+7a needs Stage-5 edge reweighting / a new
forward-completion edge / joint segmentation — all out of 3.2's scope. The three unlock paths
are documented as ratification forks (§3.4, §10).

---

## 1. Scope and the behavior-change contract

Stage 3.2 widens the chord-path decoder's beam from 1 to *K* behind the **quality-level knob**
(`docs/decoder_design.md` §9). It changes **what the decoder is allowed to do**, not what the
oracle or segmentation do.

**What beam>1 changes.**
- The per-region candidate set grows from top-3 + diff-root (≤4 cells) to the **top-*K* cells**
  (Q6: K=8 start, §7).
- The forward signals (w_seq / w_dim / w_stepOut / stepwiseBassLookahead) stop reading the
  *cold-precomputed lookahead* and read the **decoded successor** (Q2 DECIDED, §2). The lattice
  becomes genuinely two-sided: backward edges (rcb etc.) against the decoded predecessor,
  forward edges against the decoded successor.
- The decode is a **global path optimization** (forward beam + backtrack), so an earlier
  region's label can be revised on later evidence rather than committed greedily.

**What beam>1 must NOT change.**
- **Level 0 (beam-1) stays byte-identical and the default.** The quality knob defaults to
  Level 0; beam>1 is opt-in. Production behavior is unchanged until a level is raised
  (`decoder_design.md` §9/§12). Level 0 is always the rollback fallback.
- **Segmentation and the oracle are untouched.** The decoder still consumes the final
  post-Pass-3 region stream (plus the Pass-1 inline same-root merge it already owns, §2/§4) and
  calls the same `analyzeChord` emission model. Boundaries do not move. The joint
  segmentation+labeling extension stays out of scope (`decoder_design.md` §1) — and §3 shows
  this boundary is exactly what blocks the Δ=+7a fix.
- **No preset branching.** The decoder reads `ChordAnalyzerPreferences`; all preset behavior is
  already in the prefs values (`decoder_design.md` §10).

**The new gate (the contract that replaces byte-identity).** From Stage 3.2 on, BIR and
snapshot changes are **allowed** — but only under three conditions, jointly:
1. **Ratified in advance.** Every case whose output is allowed to change is on the acceptance
   roster (§6), named before the implementation run, with an expected direction.
2. **DCML-adjudicated.** Every changed winner is checked against the DCML (When-in-Rome)
   ground truth — music21 corroborates but is not authoritative (project policy). A change that
   moves a winner *away* from DCML is a regression even if BIR is flat.
3. **Measured, never asserted.** No change ships on a predicted number. The implementation run
   produces the corpus A/B (Baroque + Jazz + Default per-preset dirs + manifest), the snapshot
   diff, and the per-case DCML verdict as the ratification evidence.

Any output change **not** meeting all three is a hard stop, exactly as a byte-identity diff was
through Stage 3.1–3.4. The must-hold set (§4) may not change at all.

---

## 2. What "widen the beam" concretely means here

### 2.1 The lattice (recap, then the widening)

Nodes = the post-Pass-3 regions, **plus the Pass-1 sub-regions the inline same-root merge fuses**
(this matters for Δ=+7a, §3): the unit the decoder replaces is the Pass-1 loop body
*including* the inline merge (`decoder_design.md` §1/§5), so the arpeggio's 240-tick
sub-regions are separate nodes that the decoder labels and *then* merges by root, rather than
pre-merged segmentation facts. Candidates per node = the oracle's `ScoringSnapshot.cells`.

**Beam-in (candidate-set width).**
- **Beam 1:** top-3 + diff-root append, same threshold/cap (byte-identity, mandatory at Level 0).
- **Beam *K*:** the top-*K* cells per node (Q6: K=8). Memory is a non-constraint
  (`decoder_design.md` §2: ~72 KB for K=8 on Mozart-scale; the cost is *time* to produce the
  snapshots, addressed by decode-once, §7).

### 2.2 The decode algorithm

A path is one candidate per node; its score is **Σ emission + Σ transition** over the path
(`decoder_design.md` §2). The decode is a **forward beam (Viterbi-style) with backtrack**:

```
for each node i, for each surviving hypothesis h in beam[i-1]:
    for each candidate c in topK(node i):
        pathScore(h, c) = pathScore(h)
                        + emission(c)
                        + backwardEdge(h.committed, c)      # rcb / w_stepIn / back inversion bonuses
                        + forwardEdge(c, <successor>)        # Level-1: decoded successor (§2.3)
    keep the best K extensions as beam[i]
backtrack the highest-scoring full path; then apply the inline same-root merge to it
```

**The emission and the backward edges are exactly the Stage-3.1/3.3 factorization** — no new
arithmetic, so the FP-order discipline (`decoder_design.md` §4) carries over unchanged. The
per-bass score is still computed in the canonical order
`(basisIndep + rcb + basisDep) × cf × af + wComplete + wSeq [+ wDim] [+ step]`; the **rcb edge
is still the destination-conditioned `0.40 × cf_dest × af_dest` with the Gate-R guard inside
it** (AWKWARD-1; absorbed into `rcbEdge(...)` as of `a652dc1ba7`, §4). Widening the beam does
**not** touch how a single (predecessor, candidate) pair is scored — it only enumerates more
pairs and keeps more hypotheses.

### 2.3 Forward-edge promotion (Q2 DECIDED) — and what it does *not* buy

At beam 1 the forward signals read the cold lookahead (`ctx.nextRootPc/nextBassPc`,
precomputed by `inferNextRootPc`/`backfillNextRootPc`) — AWKWARD-3, the property that makes
beam-1 byte-identical. **Q2 (DECIDED at Stage-3 ratification): Level 1 promotes them to true
decoded-successor edges.** Concretely: when scoring the extension `(h, c)` into node *i*, the
forward edge `forwardEdge(c, successor)` evaluates w_seq/w_dim/w_stepOut/stepwiseBassLookahead
against the **candidate actually chosen at node *i+1* on this path**, not the cold value.

Mechanically this requires either (a) a second backward pass (decode forward with cold
forward-edges, then re-score the forward edges against the committed successors and re-decode
to convergence), or (b) folding the forward edge into the transition between node *i* and *i+1*
so the standard Viterbi recursion sees it as `transition(c_i, c_{i+1})` — the cleaner
formulation, since a forward edge from *i* and a backward edge into *i+1* are the **same
lattice edge** viewed from two ends. (b) is the design's intent: a true two-sided edge
`edge(c_i, c_{i+1}) = backward_into(c_{i+1}) + forward_out_of(c_i)`, both evaluated against the
*decoded* neighbor. The greedy backward edges (rcb) and the promoted forward edges then compose
on one edge.

**Critical caveat the §3 derivation forces:** promoting the *existing* forward signals to
decoded edges is **not** the same as adding a new forward-alignment ("completion") signal. The
existing forward signals are narrow (w_seq on a descending-fifth V→I; w_dim on a dim
resolution; w_stepOut/stepwiseBassLookahead on stepwise bass). §3 shows that on the actual
Δ=+7a successors **none of the differentiating ones fire** (Ab→Bb is a whole step, not a
fifth). So Q2's promotion, while architecturally the substance of the decode, does **not** by
itself rescue Δ=+7a. A *new* symmetric forward edge analogous to rcb (the "Phase E symmetric
context" of `redesign_plan.md` Step 5) would be a new transition term — Stage 5/6, not the
K=8 beam-in.

---

## 3. The Δ=+7a mechanism — derived from the lattice, not asserted

This is the section the instruction demands be *derived*. **The derivation falsifies the
part-1 thesis.** Source numbers are the 2026-06-09 full per-cell oracle dump
(`cc_deltaseven_7a_diagnostic_report.md` Part C), confirmed current at `a652dc1ba7` by a live
`batch_analyze --dump-regions` probe (Stage 3.3 was byte-identical; the probe reproduces the
region structure and scores — report §1).

### 3.1 bwv102.7 — walk the lattice

DCML answer: **AbMaj7** (IVmaj7) at m9 b4.5. We emit **EbMaj7/Ab** (Δ=+7; Eb is the fifth of
Ab). Detected key G-minor (kConf 0.39 — itself mildly wrong; DCML's local context is E♭ major).
The arpeggio splits the single Ab harmony into sub-region nodes:

- **Node A (transient, `{D,Eb,G,Bb}`).** `pcWeight[Ab] = 0.00` — **Ab is entirely absent**, so
  AbMaj7 is not even a candidate here. The oracle correctly reads **EbMaj7, score 3.05**
  (a complete Maj7 of exactly these four tones). Predecessor entering A is Bb (root 10, from
  the prior region), so A earns no rcb. **A is the highest-scoring node in its neighborhood and
  is locally correct.** This is the fact that kills the thesis: the transient is not a
  low-scoring wrong commitment.

- **Node B (present-root, `{C,Eb,G,Ab}`).** Now Ab sounds (it is the bass). Two candidates:
  | | basisIndep | basisDep | raw (×cf·af) | rcb (prev=Eb) | total |
  |---|---|---|---|---|---|
  | **Eb/Ab** (incomplete — no Bb) | 1.425 | 0.900 | **2.325** | **+0.400** | **2.725** |
  | **AbMaj7** (complete) | 1.850 | 0.700 | **2.550** | 0 | 2.550 |

  **Vertically AbMaj7 wins by 0.225.** The rcb edge (+0.40, fired because A committed Eb) flips
  node B to Eb/Ab. Gate R is inapplicable (`basisDep = 0.90 > 0` — Eb/Ab carries a sounding
  third via the inversion bonus, so Gate R correctly spares it).

**The two competing paths (A is locked to Eb — Ab is unscorable at A):**

| Path | Node A | Node B | total |
|---|---|---|---|
| **greedy (wrong)** | EbMaj7 3.05 | Eb/Ab 2.325 + rcb 0.40 = 2.725 | **5.775** |
| **"correct"** | EbMaj7 3.05 | AbMaj7 2.550 + 0 = 2.550 | 5.600 |

**The greedy path is the global optimum by 0.175.** A beam decode searching all paths returns
the greedy path. The only way to reach AbMaj7 at B and beat 5.775 is a path whose node-A
emission exceeds 3.225 — impossible, since Eb (3.05) is the *maximum* emission at A and any
non-Eb choice scores lower while *also* removing the only route to a competitive A. The
0.175 gap is exactly `rcb(0.40) − verticalMargin(0.225)`: a **node-local** contest at B decided
by the rcb edge, with the predecessor root forced by a confident, correct transient. **The beam
has nothing to revise.**

**Forward-edge promotion (Q2) does not help.** The successor after B is Bb (root 10; live
probe). Ab(8)→Bb(10) is a whole step, not a descending fifth → no w_seq, no w_dim. The only
forward signal that fires (stepwise-bass lookahead, Ab→Bb) applies to **both** B candidates
(same bass Ab) and so cannot differentiate them. Closing the 0.175 gap would need a *new*
forward edge that rewards AbMaj7 specifically for completing the chord in the present-root
slice — not available at K=8.

### 3.2 bwv261 — walk the lattice

DCML answer: **F#7** (V7) at m18 b4.5. We emit **C#m/E** (Δ=+7; C# is the fifth of F#). Key
B-minor (kConf 0.69, correct — so the key is not the lever here, unlike bwv102.7). The
arpeggio splits F#7 across ≥3 sub-region nodes:

- **Node S1 (run start, `{C#,E,G,B}`).** C#ø7/E, score 3.35. F#/A# absent.
- **Node S2 (committed, `{C#,E}` only).** C#m/E raw **2.900** (basisIndep 2.0 + basisDep 0.9
  first-inversion) vs F#7/E raw **1.650** (F# absent → 2/4 tones). **C#m wins by 1.25 even
  without rcb** — pure segmentation; F# is simply not in this slice.
- **Node S3 (present-root, `{C#,E,F#,A#}`).** Now F# and A# sound:
  | | basisIndep | basisDep | raw | rcb (prev=C#) | total |
  |---|---|---|---|---|---|
  | **C#m/F#** | 1.425 | **1.400** (stepwise E→F# + sameRoot + completeTriad) | 2.825 | +0.400 | **3.225** |
  | **F#7** (root pos) | 2.150 | 0.700 | **2.850** | 0 | 2.850 |

  **Vertically F#7 wins by 0.025.** C#m/F# reaches near-parity via large first-inversion
  bonuses (basisDep 1.40), then rcb (+0.40) flips it. Gate R inapplicable (basisDep 1.40 > 0).

**Best path over {S2, S3}** (S1=C#ø7 fixed, root C#):

| Path | S2 | S3 | total |
|---|---|---|---|
| **opt1 greedy** | C#m 2.900 + rcb 0.40 | C#m/F# 2.825 + rcb 0.40 | **6.525** |
| opt2 (F#7 target) | C#m 2.900 + rcb 0.40 | F#7 2.850 + 0 | 6.150 |
| opt3 | F#7/E 1.650 + 0 | F#7 2.850 + rcb 0.40 | 4.900 |
| opt4 | F#7/E 1.650 + 0 | C#m/F# 2.825 + 0 | 4.475 |

**opt1 (greedy, wrong) is the global optimum, beating the F#7 target by 0.375.** S2 genuinely
and overwhelmingly prefers C#m (by 1.25 — F# is absent), so any path putting F#7 at S3 still
carries a C#-rooted predecessor whose rcb edge (3.225) outscores F#7 (2.850). Forward-edge
promotion: the successor is C#m7♭5 (root C#); F#(6)→C#(1) is a descending fifth, so a promoted
w_seq (+0.20) *would* favor F#7 at S3 — but +0.20 against a 0.375 gap is insufficient, and the
successor is itself a C#-continuation artifact. **The beam does not fix bwv261.**

### 3.3 Why the thesis failed — the general statement

The part-1 thesis assumed Δ=+7a is *"transient wrong root irrevocably committed, fed forward by
rcb."* The derivation shows the real mechanism is **structurally identical to Δ=+7b**: a
**locally-correct, high-confidence predecessor**, continued by rcb into a near-tie/small-margin
present-root slice that rcb tips the wrong way. The only difference from Δ=+7b is that the
Δ=+7a present-root wrong reading carries `basisDep > 0` (a sounding third / inversion bonus),
so **Gate R cannot gate it** — which is precisely why Gate R fixed Δ=+7b but not Δ=+7a
(`cc_deltaseven_7a_diagnostic_report.md` TL;DR). Because the continued-root path is the genuine
score optimum, a *global* decode finds the *same* optimum a *greedy* decode does. Re-ranking the
search does not change which path scores highest; only **re-weighting the edges** (or changing
the candidate set via segmentation) can. This matches `redesign_plan.md`'s own conclusion —
"confidence can't encode 'right now, wrong in 240 ticks'; the fix requires inter-region revision
… architectural, not a gate" — with the sharpening that **inter-region revision by score
maximization does not revise here, because the wrong reading IS the score maximum.**

### 3.4 What would actually fix Δ=+7a (three forks for ratification, §10)

1. **Edge reweighting (Stage 5).** If the rcb edge weight were < the vertical margin
   (< 0.225 for bwv102.7, < 0.025 for bwv261 — the latter is near-impossible), the present-root
   slice would resolve to the DCML root on the continued path. But rcb is Baroque-calibrated and
   load-bearing for the Δ=+7b/Alberti-continuity cases (the Iter-98 / mozart_k280 dead end:
   every blanket rcb reduction regresses correct continuations). A *contextual* rcb (lower when
   the predecessor is a short/arpeggiated/incomplete slice) is the survey-falsified direction —
   no `(score, margin, distinctPcs, rootWeight)` threshold separates the Δ=+7a predecessors from
   the mozart Alberti control (`cc_phase_e_predecessor_survey_report.md`). This is a Stage-5
   transition-weight *fitting* problem, not a beam-width change.
2. **A new symmetric forward-completion edge (Stage 5/6).** An edge that rewards the path where
   the *complete* chord sounds in the present-root slice (AbMaj7's four tones vs Eb/Ab's three),
   strong enough to overcome rcb. This is `redesign_plan.md` Step 5's "symmetric forward context
   analogous to rcb" — a **new transition term**, designed and fitted, not the promotion of the
   existing narrow forward signals (which §3.1–3.2 show do not fire usefully here).
3. **Joint segmentation+labeling (beyond Stage 3).** Merge the arpeggiated sub-regions into one
   region so {Ab,C,Eb,G} sounds together and AbMaj7 wins outright. Phase-D *duration-weighted*
   aggregation already tried and failed (the aggregate `{Eb:720,…,Ab:480}` still prefers Eb,
   +0.15; `redesign_plan.md` Step 4 dead end 3) — so this needs a *labeling-aware* joint model,
   the segmental-CRF target explicitly deferred past Stage 3 (`decoder_design.md` §1).

**Recommendation:** retarget Stage 3.2 onto the gate-subsumption roster (§6) and route Δ=+7a to
Stage 5 (fork 1+2 together — reweight rcb *and* add the completion edge, fitted jointly against
the Δ=+7b/Alberti must-holds). Do **not** promise a Δ=+7a number at 3.2.

---

## 4. The must-not-break set as hard lattice constraints

Every item here is a Level-0 byte-identity obligation **and** a Level-1 must-hold (the wider
decode may not change them). For each: the wider-decode risk and the guard.

### 4.1 The Δ=+7b trio — bwv245.28, bwv296, bwv320 (Gate R + Gate I coupled)

The correct first-inversion-triad reading, pinned (`gater_tests` F1/F2, the `DeltaPlus7b`
diagnose acceptance). The wider decode must reproduce it byte-for-byte.
- **Risk.** Δ=+7b is fixed by **two** coupled mechanisms: **Gate R** zeroes the bare-root rcb
  (bass foreign, no sounding third → `basisDep ≤ 0`, reconstructed-credit form), and **Gate I**
  selects the first-inversion Major over the root-position Minor (`cc_stage3_4i_dossier.md` §3:
  disabling I fails *both* Δ=+7b Gate-R pins). A wider beam that re-ranks the candidate set could
  surface a different winner if either mechanism's effect is not reproduced on the decoded path.
- **Guard.** Gate R is **already absorbed into the rcb edge** (`a652dc1ba7`) — it is a
  continuation-edge guard the decode evaluates per edge, so it composes with any beam width by
  construction. Gate I must **either** stay a post-decode re-rank **or** have its first-inversion
  selection reproduced as a decode tie-break *before* the beam widens past it (§5). The
  Δ=+7b trio is a per-case A/B pin in the 3.2 acceptance run: any movement is a hard stop.

### 4.2 Gate I's double obligation (the headline 3.2 risk)

Gate I carries **two** proof obligations that the decode must reproduce *together*
(`cc_stage3_4i_dossier.md` §3, the highest-stakes retirement):
1. **5 Jazz fixes** — `Xm7/Y` slash vs DCML major (bwv286, bwv355, bwv386, bwv388, bwv428);
   removing I regresses Jazz 7→12.
2. **The Δ=+7b first-inversion selection** (coupled with Gate R, §4.1).

This is the single most concentrated risk in the whole stage: on the user-facing Default config
gate retirement is BIR-free, and the *only* BIR-relevant gate in the set is **Gate I on Jazz**,
double-coupled to the must-not-break trio (`cc_stage3_4i_dossier.md` §5 headline). **Design
constraint:** I does not retire/fold until the decode reproduces **both** obligations
(expected: Jazz 7 held, Δ=+7b trio unchanged, Baroque 13). Its margin (≤ 0.45) becomes a decode
tie-break only once both are demonstrated. If I proves un-foldable without losing one obligation,
**Gate I stays a post-decode re-rank** and the beam does not widen past it (§10 fork).

### 4.3 The identity sets

> **Re-baselined 2026-06-13 (corrected GT parser) + beam-widening SHELVED.** Two notes for this
> section: (1) beam-widening was falsified for Δ=+7a and is shelved (Δ=+7a → Stage 5), so this
> doc is a parked plan. (2) The 13/7/14 identity sets below are the pre-re-baseline values; the
> gate is now **Baroque 57 / Jazz 23 / Default 57** (strict superset, CLAUDE.md is authoritative).
> Every "Baroque 13 held / Jazz ≤ 7 / Default 14 held" constraint downstream should be read
> against the 57/23/57 sets if this work is ever revived.

- **Baroque-13** (`{bwv102.7@17520, bwv14.5@8160, bwv17.7@46080, bwv174.5@6240, bwv245.17@4800,
  bwv245.40@51360, bwv261@33840, bwv269@20640, bwv301@960, bwv381@4800, bwv422@23040,
  bwv432@5520, bwv45.7@20160}`), **Jazz-7** (`{bwv244.15, bwv245.17, bwv245.40, bwv422, bwv432,
  bwv45.7, bwv74.8}`), **Default-14** (Baroque-13 ∪ `{bwv187.7@m14.b2}`).
- **Constraint.** No identity-set **regression** on any config (a case *leaving* the BIR=false
  set is a win to ratify case-by-case; a case *entering* is a hard stop). The gate is the
  case-identity set, not a bare integer (CLAUDE.md preset policy). Because §3 removes Δ=+7a as a
  3.2 win, the realistic 3.2 expectation is **Baroque 13 held, Default 14 held, Jazz ≤ 7** (the
  bwv74.8 bias over-correction is the one plausible improvement, §6).

### 4.4 The 11 pipeline snapshots

`pipeline_snapshot_tests` pins P1/P2/P3/P4 output. The wider decode may refresh a golden **only**
for a ratified, DCML-verified output change. The bias correction touches **8 of 11** snapshots
(`cc_stage3_4i_dossier.md` §3) — so bias-subsumption (§6) is the change most likely to require
golden refreshes, and each must be DCML-adjudicated before `--update-goldens`.

---

## 5. Gate-retirement sequencing (Q3 — the load-bearing ordering)

**Q3 DECIDED (Cowork ratification):** for any gate that mutates root/quality/bass identity,
**3.4 retirement leads 3.2 beam-widening past that gate.** The 3.4-i dry-run established the
load-bearing fact that **every remaining gate mutates identity** (`cc_stage3_4i_dossier.md` §3,
last column: all "yes → caps beam") — there is no structural non-mutating gate the beam could
widen past early (Gate J is structural but still mutates Dim→V7, so it too caps the beam where it
fires). Therefore **3.2 is fully gated behind the per-gate 3.4 work** for the identity-mutating
set, which is all of them.

The concrete order (gates fold into the lattice in this sequence; the beam widens past each only
after its fold is demonstrated):

1. **Fold into emission / edges first (the decode reproduces them by construction):**
   - **Gate R** — already absorbed into the rcb edge (`a652dc1ba7`). Done.
   - **bias correction** — its inversion deduction is subsumed by **proper inversion edges**
     (the migrated `appliedBassBonus` / inversion-context bonuses on the transition layer remove
     the over-fired bass-root bonus when it is the sole decider; `decoder_design.md` §7). Fold
     before widening: the 8-snapshot Baroque structure must be reproduced (§6).
   - **Iter 91** (forward bass-root promotion) and **H** (aug rotation) — subsumed by a
     wDim-style **forward edge**; fold as the forward-edge promotion (§2.3) lands.
2. **Become decode tie-breaks (margins fold into the path comparison):**
   - **I / K / L** — inversion/quality swaps with margins ≤ 0.45 / 0.20 / 0.35. Their margins
     become decode tie-breaks *against consistent path state*, which dissolves the 1b-F4
     live/captured ambiguity by construction (Q4: reproduce at beam-1, fix-as-retire here;
     `cc_stage3_4i_dossier.md` §4 F4). **I is gated on its double obligation (§4.2); K must
     reproduce its Baroque target without importing the chromatic-romantic mis-fire** (the
     3.4-ii caution: K's sampled non-chorale fire is root-neutral/worse vs DCML — Chopin op24-4;
     `cc_stage3_4ii_report.md` §4). **Iter-86's** non-chorale fire is DCML-correct (K310-1
     `#viio7` root) and must be *reproduced*.
3. **Stay post-decode re-rank → Stage 6 (do not retire at 3.2):**
   - **A, G-E, G-B/C/D** (C4 functional — enharmonic / viiø7 key-function decisions, Baroque-only,
     0 on Default/Jazz) and **J** (C5 structural keeper — vii°→V7, BIR-blind on every config).
     None block 3.2 on the user-facing config; they remain re-ranks until the Stage-6 functional
     layer can express them.
4. **Alternatives-hygiene re-decides (winner-neutral, the decoder's output-assembly owns them):**
   - **E, F** (C2′) — winner-neutral but not byte-identical to remove (E alters alternatives on
     bwv245.3/bwv336; F is redundant with the bias correction on K283-3;
     `cc_stage3_4ii_report.md` §2/§4). Carried by the decode's per-node alternatives assembly
     (Q5: emit the full path + alternatives + margins), which orders alternatives by emission
     score by construction — retiring the F6 unsorted-tail / F8 duplicate-push artifacts for free.

---

## 6. Acceptance roster with measured expected deltas + DCML adjudication

Per case: expected **direction**, the **must-hold / expected-win / measure-and-decide** class,
and how it is DCML-verified. **No promised numbers** — the implementation run measures and
produces the ratification evidence. The roster is the union of `cc_stage3_4i_dossier.md` §5(B)
and `cc_stage3_4ii_report.md` §4, **with Δ=+7a downgraded per §3**.

| Case | Class | Expected direction | DCML adjudication / evidence to produce |
|---|---|---|---|
| **Δ=+7a** (bwv102.7, bwv261) | **NOT a 3.2 win (§3)** | **no change at K=8** — measure to confirm the derivation, then route to Stage 5 | the live lattice walk reproduced; confirm both stay BIR=false (Baroque 13 held). A *fix* here is evidence the decode did something the derivation says it can't — investigate, don't celebrate |
| **Δ=+7b trio** (bwv245.28/296/320) | **must-hold** | unchanged | `gater_tests` F1/F2 + `DeltaPlus7b` diagnose pins green; per-case A/B zero-diff |
| **Gate I** (highest stakes) | **must-hold (both obligations)** | Jazz 7 held; trio unchanged; Baroque 13 | 5 Jazz cases DCML-checked to stay correct; Δ=+7b pins green (§4.2) |
| **bias correction** | **expected-win + must-hold structure** | Baroque 13 + 8 snapshots reproduced; **Jazz ≤ 7** (bwv74.8 over-correction is the upside) | bwv74.8@13440 Em7/D DCML-checked if it changes; 8 snapshot goldens DCML-adjudicated before refresh |
| **K** (C2) | **measure-and-decide** | reproduce Baroque target; **do NOT import** chromatic-romantic mis-fire | Chopin op24-4 (K-enabled worse vs DCML root); reproduce Baroque behavior only |
| **Iter-86** (C2) | **expected-win (reproduce)** | reproduce the ♭7-bass third-inversion stamp | Mozart K310-1 `#viio7` root (DCML-correct; disabling regresses the root) |
| **L** (C2) | **measure-and-decide** | Jazz 18 tie-breaks reproduced; Baroque/Default unchanged | the 18 Jazz regions DCML-spot-checked |
| **E, F** (C2′) | **alternatives-hygiene** | winner unchanged; alternatives ordering owned by decode output | bwv245.3/bwv336 (E), K283-3 (F) — winner-neutral, verify no winner moves |
| **H, Iter 91** (near-dead) | **measure-and-decide** | unchanged ×3 | 3 Baroque aug rotations / 8 Baroque + 3 Default promotions reproduced |

**Distinguishing the three labels:** *must-hold* = any change is a hard stop (Δ=+7b, Gate I both
arms, identity sets). *expected-win* = a ratified, DCML-verified improvement (bias→Jazz bwv74.8;
Iter-86 reproduction). *measure-and-decide* = direction unknown until measured, ratify on the
evidence (K, L, H, Iter 91, and now **Δ=+7a — expected null**).

**The honest headline (§3 + dossier §5):** on the user-facing **Default** config, Stage 3.2 is
**BIR-identity-free** — gate retirement does not move Default's 14, and §3 removes Δ=+7a as a
win. Stage 3.2's measurable value is therefore (a) the **architectural** win (gates dissolved
into the decode; the greedy commit replaced by a global path; the F4/F6/F8 artifacts retired by
construction), and (b) the **Jazz** opportunity (bwv74.8 via bias-subsumption). The user-facing
accuracy win the part-1 thesis promised via Δ=+7a is **deferred to Stage 5**.

---

## 7. Beam width *K*, decode cost, and the perf budget

- **K (Q6 DECIDED): start K = 8** (well above the current ≤4 emitted candidates), tuned at
  Stage 5. Top-3 + diff-root stays mandatory at beam 1 (Level 0 byte-identity).
- **Decode cost.** The decode itself lives in the `< 0.3 ms` `analyzeSection` layer
  (`decoder_design.md` §8); a K=8 Viterbi over ~140 nodes × 8 hypotheses × ~8 candidates is
  microseconds of arithmetic — negligible against Pass-0 (the 98–99.9% cost). **Decode-once
  still applies:** a wider decode is computed once per score and cached, so the cost is paid once
  (`decoder_design.md` §8, shipped as the 3.1b **bounded-window cache** — note Q1 was re-decided
  to bounded-window after the whole-score A/B falsified its premise; `decoder_design.md` §8
  amendment). Level 1 is **not interactive-bounded** (`decoder_design.md` §9 Level-1 budget:
  background/default export), so even a perf-pessimal K is within budget.
- **Memory.** ~72 KB for K=8 on Mozart-scale (`decoder_design.md` §2) — a non-constraint.
- **Budget statement (per §9).** Level 0's `p95 ≤ baseline × 1.10` gate is unaffected (Level 0
  is byte-identical, beam 1). Level 1's wider decode is gated by correctness (the §6 acceptance
  roster), not latency.

---

## 8. Config scope

- **Default** (`kDefaultChordAnalyzerPreferences` — the live product) is the **eval column that
  matters**: BIR=false 14. Per §6 it is BIR-identity-free at 3.2, so the Default validation is a
  **must-hold** (14 unchanged) plus the snapshot/architectural changes.
- **Baroque** is the **primary calibration gate** (CLAUDE.md): the 13 identity set, the 8 bias
  snapshots, the Gate-fold reproductions all measure here.
- **Jazz** is the **non-Baroque hard-stop** and the **only BIR-relevant config** for 3.2 (Gate I:
  5 fixes; bias: bwv74.8; L: 18 tie-breaks). The beam-widening is validated against all three,
  but the BIR action is concentrated on Jazz-Gate-I (`cc_stage3_4i_dossier.md` §5).
- **Thresholds.** No gate threshold is re-tuned at 3.2 (that is Stage 5). The gate *margins*
  (I 0.45, K 0.20, L 0.35) become decode tie-breaks at their stated values — **not** widened,
  **not** made beam-width- or quality-level-dependent. Should any threshold need to become
  quality-level-dependent, CLAUDE.md preset policy still binds (Baroque-tuned values unchanged;
  a non-Baroque edge case gets a structural entry condition or a preset override, never a widened
  Baroque threshold). The recommendation is that **no threshold becomes level-dependent at 3.2**;
  if the bias-fold forces one, it is a §10 fork.

---

## 9. Migration sequencing → roadmap, risks, rollback

**Design section → implementation sub-step.** Per Q3, gate folding leads beam widening:

| Sub-step | Design §| Deliverable |
|---|---|---|
| 3.2-a — fold bias correction into inversion edges | §5(1), §6 | Baroque 13 + 8 snapshots reproduced; Jazz ≤ 7; per-case A/B |
| 3.2-b — promote forward signals to decoded edges (Q2) | §2.3, §5(1) | H / Iter-91 subsumed; **measure that Δ=+7a stays null (§3)**; snapshots held or DCML-refreshed |
| 3.2-c — widen beam-in to K=8 + Viterbi decode | §2, §7 | global path replaces greedy; identity sets held; the decode is the path optimizer §3 walked |
| 3.2-d — fold I / K / L margins into decode tie-breaks | §5(2), §4.2 | **I's double obligation** held (Jazz 7 + trio); K reproduces Baroque-only; L Jazz tie-breaks |
| 3.2-e — alternatives-assembly owns E / F / F6 / F8 | §5(4) | winner-neutral; alternatives score-ordered by construction |

(A, G-family, J defer to Stage 6; Δ=+7a defers to Stage 5 per §3.)

**Riskiest assumptions, in priority order.**
1. **§3 is right that the beam doesn't fix Δ=+7a — and the implementation confirms it.** If a
   live K=8 decode *does* move Δ=+7a, the derivation missed a term (a forward edge that fires, a
   candidate I didn't enumerate) — investigate before celebrating; a "win" the derivation
   forbids is a bug somewhere. Mitigation: 3.2-c measures Δ=+7a explicitly against the §3
   prediction (null).
2. **Gate I un-foldable without losing an obligation** (§4.2). Mitigation: I stays post-decode
   re-rank; the beam does not widen past it (§10 fork). The 5 Jazz cases + trio are pinned.
3. **bias-fold destabilizes the 8 snapshots beyond the DCML-correct delta** (§4.4). Mitigation:
   per-snapshot DCML adjudication before any `--update-goldens`; revert the fold if a snapshot
   moves away from DCML.
4. **Forward-edge promotion (Q2) destabilizes a snapshot** at Level 1. Mitigation: Level 0 stays
   on the cold lookahead (byte-identical); the promotion is Level-1-only and behind the knob.

**Behind the knob vs in place.** Beam>1 is **behind the quality-level knob, default Level 0** —
production is byte-identical until a level is raised. Gate *folds* (bias, I/K/L margins) land
**in place, one at a time**, each its own commit with the per-case A/B + DCML adjudication. The
oracle and segmentation are untouched throughout.

**Rollback (per step).** Each sub-step is an isolated commit gated on its acceptance evidence.
Because Level 0 is the flag default and folds land one at a time, **every prior state is a clean
recoverable baseline** — and the ultimate fallback (Level 0 / beam 1) is byte-identical to
`a652dc1ba7`.

---

## 10. Open Questions for Cowork / user

Genuine forks. Recommendations given; decisions are Cowork/user's.

- **OQ1 — Δ=+7a retargeting (the big one, from §3).** The derivation shows K=8 does not fix
  Δ=+7a. Three unlock paths (§3.4): (1) Stage-5 rcb reweighting, (2) a new symmetric
  forward-completion edge, (3) joint segmentation. *Recommendation: accept §3, retarget 3.2 onto
  the gate-subsumption roster (§6), and route Δ=+7a to **Stage 5 as fork 1+2 jointly** (reweight
  rcb and add the completion edge, fitted together against the Δ=+7b/Alberti must-holds). Do not
  attempt fork 3 (joint segmentation) before the granularity-robust metric (CLAUDE.md Stage-5).*
  **Decision: yours — it sets whether 3.2 ships with a Δ=+7a target at all.**

- **OQ2 — Does Stage 3.2 ship at all without a user-facing BIR win?** Given §6's "Default is
  BIR-identity-free," 3.2's value is architectural (gates → decode, greedy → global) + the Jazz
  bwv74.8 opportunity, not Default accuracy. *Recommendation: ship it — the architectural
  consolidation is the prerequisite for Stage-5 edge fitting (you cannot fit transition weights
  on a greedy commit chain with thirteen post-hoc gates), and it is the substance the redesign
  has been building toward. Frame 3.2 as "the decode that Stage 5 fits," not "the Δ=+7a fix."*
  **Decision: yours.**

- **OQ3 — Gate I: fold or hold?** If I cannot fold without losing one of its two obligations
  (§4.2), it stays a post-decode re-rank and the beam does not widen past it. *Recommendation:
  attempt the fold in 3.2-d with both obligations pinned; if either moves, **hold I as a
  re-rank** — a held gate is cheaper than a regressed must-hold. This is the highest-stakes call
  in the stage.* **Decision: yours, on the 3.2-d evidence.**

- **OQ4 — Forward-edge promotion (Q2) at Level 1 vs a new completion edge.** Q2 promotes the
  *existing* forward signals; §2.3/§3 show those don't rescue Δ=+7a. Should 3.2-b promote the
  existing signals (architecturally correct, low Δ=+7a value) and defer the *new* completion edge
  to Stage 5? *Recommendation: yes — promote the existing signals in 3.2-b (it subsumes H/Iter-91
  and completes the two-sided lattice), and design the new completion edge in Stage 5 alongside
  the rcb reweighting (OQ1 fork 2). Keep them separate: the promotion is byte-checkable against
  the cold lookahead at the regions where it should be inert; the new edge is a fitted term.*
  **Decision: yours.**

- **OQ5 — Threshold/level-dependence (§8).** Recommendation is that no gate threshold becomes
  beam-width- or quality-level-dependent at 3.2. If the bias-fold forces a level-dependent value,
  is that acceptable, or must the fold be structural? *Recommendation: keep thresholds
  level-independent; if forced, prefer a structural entry condition over a level-dependent
  threshold (CLAUDE.md policy).* **Decision: yours, only if 3.2-a hits the wall.**

---

*End of draft. Awaiting ratification addendum before commit (roadmap rule 4).*

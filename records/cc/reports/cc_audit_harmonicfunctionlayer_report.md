# CC Layer Audit #6 — `harmonicfunctionlayer.cpp` (competition + progression scoring) — READ-ONLY findings

*CC primary auditor, 2026-06-17. HEAD `a03c2493bb`. Per `docs/layer_audit_plan.md` §3.
Read-only: no code / behavior / inference change. North star = CORRECT inference vs the
DCML/music21 oracle, not a proxy gate. Reconciles with `cowork_audit_harmonicfunctionlayer.md`
(C1 / S3) and the consolidated obligation map.*

**Evidence tags:** **[src]** read at HEAD source · **[probe]** ran a read-only script over the
committed corpus (`tools/corpus/default`, manifest git `41f7c65f63`, 353/353, music21 9.9.1) ·
**[oracle]** music21 9.9.1 cross-check (inherited from `cc_functional_residual_dossier.md` / audit #5).
Driver: throwaway `C:\tmp\cc_audit6_competition.py` reusing the committed metric machinery verbatim
(`compare_analyses.align_regions` / `align_dcml_regions` / `three_way_classify`, `dcml_parser.parse_rntxt_file`).
This file is the only repo write.

**Base reproduces exactly.** My driver reproduces the dossier / audit-#5 three-way headline to the
case: 326 WiR-covered stems, `all_agree` 7608, `music21_dcml_agree` 212, **`all_differ` 2153**,
root_err 2365, **functional 91.0 %** [probe]. So the residual measured below IS HEAD's residual.

---

## §1 — Responsibility (the contract) — and the multiple-responsibility verdict

`applyHarmonicFunction(snapshot, ctx, prefs, results, chosenResult, gateCtx, phase)` — consume the
oracle's vertical-only `ScoringSnapshot`, re-score every cell with the progression signals, run the
per-bass-group → global competition, select the winner, and emit the ranked `results[]` + the
`gateCtx` for the next (gate) layer. **[src** harmonicfunctionlayer.cpp:345-565**]**

### ★ S3 decomposition — CONFIRMED as a split, but CORRECTED to **TWO in-body jobs, not three**

Cowork (and the map's S3) flag "**three** responsibilities: competition / temporal-scoring /
**function**." My source read **confirms the split but corrects the third member:**

1. **Progression / temporal re-scoring** (Pass A + Pass B). `applyHarmonicFunction` is the *sole owner*
   of all five migrated progression signals — `resolutionEdgeBonus`, `inversionContextBonus` (the
   capped 4-bonus sum), `rootContinuityBonus` + Gate R (`rcbEdge`), `wSeqBonus`/`wDimBonus`, and the
   `wStep*` pair with the surgical m7-family guard (`applyStepBonusGuard`). **[src** :385-442, 38-341**]**
2. **Competition / winner selection** (Pass C + the tail). The with-/without-wDim variant tracking,
   the Iter-97a-v3 post-bonus quality guard, the sort, the `kScoreThresholdRatio` threshold, the
   ≤3 result cap, and the guaranteed diff-root append. **[src** :444-537**]**

3. **`function` is NOT a third in-body responsibility — it is DELEGATED.** The degree/function label
   (`r.function.degree = diatonicDegreeForRootPc(...)`) is assigned inside
   **`buildChordResult` (chordanalyzer.cpp:952)**, which this layer merely *calls* (:504-506). The
   competition layer carries **no** degree logic of its own. **[src]** So the accurate decomposition is
   **(1) temporal-scoring + (2) competition**, both genuinely interleaved in Pass A/C and cleanly
   separable; the "function" job lives in the chord layer (buildChordResult), and the
   key→degree dependency the map attributes "here" is actually inherited *through* buildChordResult.

   A genuine **fourth, lesser concern** the map omits: this layer also **marshals `gateCtx`**
   (:547-564) — copying snapshot metadata + the chosen winner's `rawCandidates` so the *next* layer
   (postscoringgates) can run. That is data-plumbing for a downstream layer, not winner selection — a
   phase-2 seam note (the competition layer knows about the gate layer's input struct).

**Verdict: the multiple-responsibility flag HOLDS** (temporal-scoring and competition are two
separable jobs fused in one function), **but it is a 2-way split, not 3-way**, and the third claimed
member (function/degree) is already in a different layer. Phase-2 decomposition candidate: lift the
six bonus functions + `applyStepBonusGuard` (the "temporal-scoring" job, already free functions) out
of the competition driver.

---

## §2 — Correctness: the rule-reachable share, RE-MEASURED and RE-ATTRIBUTED TO THIS LAYER

This is the audit's verdict-critical measurement. The map's reconciliation target is the
**`[prov ≈ 26–55 %] rule-reachable`** share of the functional residual (carried from the
functional-residual dossier §2.3). **My finding: that figure is a *cross-layer* estimate and must be
re-attributed — the share THIS competition layer can actually reach is much smaller.**

### §2.1 — Why the dossier's 26–55 % is not this layer's number

The competition layer's only power is to **re-rank the candidate roots present in a region**. It
cannot merge regions (segmentation), cannot invent a key/tonicization label (KeyArea / Stage-6
labeler), and cannot root a chord on a pitch class the sonority does not contain. The dossier's
26–55 % "rule-reachable" explicitly **credits segmentation rules, key/applied rules, and a Stage-6
labeler** (`cc_functional_residual_dossier.md` §2.2 criteria) — most of which are *other* layers. To
get THIS layer's reach I attributed every one of the 2153 `all_differ` regions to the layer that
could fix it [probe], mutually exclusive, priority cad64 > held > present > absent:

| attribution bucket | criterion | count | % of all_differ | owning layer |
|---|---|---:|---:|---|
| **ROOT_ABSENT** | WiR root not a sounding tone, not held | **833** | **38.7 %** | floor / functional model (NOT competition) |
| **HELD** | WiR root == our prev- or next-region root | **811** | **37.7 %** | segmentation (over-segmentation; S1/S2) |
| **ROOT_PRESENT** | WiR root IS a sounding tone in our region | **345** | **16.0 %** | **competition (THIS layer)** |
| **CAD64** | WiR root == our bass ≠ our root | **164** | **7.6 %** | competition / Stage-6 labeler |

(ROOT_PRESENT 345 and ROOT_ABSENT 833 match the dossier §2.1 mechanical sizing exactly; the
HELD/CAD64 split differs only because I disposition the cad64∩held overlap to CAD64.)

### §2.2 — ★ The competition layer's genuine reach is ≈ 24 % of the residual, and the pure-rerank slice is ≈ 2 %

- **THIS layer's reachable slice = ROOT_PRESENT (16.0 %) + CAD64 (7.6 %) ≈ 509 regions = 23.6 % of
  the functional residual.** The other **~76 %** is not this layer's to fix: **38.7 % ROOT_ABSENT**
  (the correct root is not even sounding → needs a functional/applied model or is the floor/noise) and
  **37.7 % HELD** (we over-segmented a held harmony → segmentation's job). [probe]
- **The PURE-RERANK slice is tiny.** Of the 345 ROOT_PRESENT cases, the WiR root is among **our own
  emitted top-3 alternatives** in only **36** (10.4 % of present, **1.7 % of all_differ**) — i.e. only
  ~36 regions are ones the competition already ranked and *lost*, fixable by a pure re-weight. Across
  *all* layers, the WiR root is among our alternatives in 247 (11.5 %). [probe]
- **The other ~309 ROOT_PRESENT cases need a candidate we never surfaced — and a second independent
  vertical analyzer agrees with us, not DCML.** In `all_differ`, music21 == ours in 94.1 % (audit #5
  §2.2 [oracle]); so for the present-but-not-ranked roots, promoting them is **not** a vertical
  rescore — it requires a *functional* rule (cadential-6-4, applied target, suspension/NHT awareness),
  which sits at the **boundary** between this competition layer and a Stage-6 functional labeler.

**So I CORRECT `[prov ≈ 26–55 % rule-reachable]` as applied to this layer:** that is the correct
*cross-layer* figure (and I confirm it cross-layer — HELD+CAD64+the present subset ≈ that band), but
**the competition layer specifically owns only ~24 % of the residual (~509 regions), of which only
~1.7 % (36) is a pure re-rank and the rest needs new functional candidates.** This *sharpens* — does
not overturn — Cowork's "rule-reachable / hand-buildable" verdict: the chord-axis obligations are
hand-buildable, but they are **functional rules (cad64 / applied / share-tone), not generic bonus
re-weights**, and a large part of the headline residual belongs to **segmentation** (HELD 37.7 %).

### §2.3 — The TOP wrong-winner patterns at this layer (the actionable obligation list) [probe]

Within the competition-reachable slice (ROOT_PRESENT, by WiR-label base, n=345):

| pattern | signal | size | the missing competition/functional rule |
|---|---|---:|---|
| **Cadential 6-4** | CAD64 bucket (164) + the `i6/4`/`I` cases inside ROOT_PRESENT | **164 + ~20** | I64-over-^5 in a cadential position reads as **V**; we emit the literal tonic triad. The single most concrete rule. |
| **Leading-tone / share-tone (viio↔V7)** | WiR base `vii` = **50** (14.5 % of present) | **50** | among the dim/half-dim share-tone set we pick the wrong root; a viio-vs-V7 / rotation discriminator. |
| **Applied-dominant target present** | WiR label has `/` = **50** (14.5 % of present); 214 (9.9 %) over all_differ | **50** | the applied root is sounding but read with the global key → a labeling question (borders Stage-6), not always a root re-pick. |
| **Bass-anchoring bias** | ROOT_PRESENT ∧ bir=True ∧ WiR root ≠ our bass = **216 / 345** | **216** | in 63 % of present cases we anchor the root on the bass (`appliedBassBonus` + bass-group competition) while DCML roots on an upper voice. The competition's bass-first structure is the mechanism. |

Δ(our − WiR) over all_differ is **classic-functional**: +7 (V-for-I) 23.6 %, +5 14.9 %, +2 14.8 %,
+3 12.5 %, +10 10.1 % [probe] — but the +7 mass concentrates in HELD/ABSENT (held tonic read as a
passing dominant), reinforcing that the dominant↔tonic confusion is largely **segmentation**, not the
competition.

### §2.4 — Heuristic-accretion (structural-quality) note — CONFIRMED, not quantifiable as error

The progression-signal stack is the accreted Iter-86/91/95/96/97 bonuses: `rcb` + Gate R (a
3-condition structural guard with a reconstructed-credit redesign), the with-/without-wDim **dual
competition** + the Iter-97a-v3 post-bonus quality guard, `w_seq`, `w_dim`, the `wStep*` pair + the
surgical m7-family `applyStepBonusGuard`. **[src** :234-341, 467-484**]** Each is a narrow,
case-targeted patch; their interaction (e.g. wDim fires only if the with-variant winner is Dim/HalfDim
*and* survives the quality guard) is hard to reason about locally — the "boiling-frog" complexity
Cowork flags. **This is a STRUCTURAL-quality concern, not a measured error source** (the bonuses are
gate-proven net-positive); I confirm it as a phase-2 "is this the right structure" candidate, not a
correctness obligation.

---

## §3 — Completeness

- **[completeness · chord-axis] Heuristic coverage gaps — CONFIRMED.** No bonus targets the cadential
  6-4 (164, the largest single competition-reachable pattern) or the applied-target labeling — those
  cases fall back to the vertical winner (functionally wrong). The progression bonuses cover
  root-continuity, V→I sequence, dim leading-tone, and stepwise-bass inversion; they do **not** cover
  the §2.3 patterns. The uncovered-rule space IS the ROOT_PRESENT + CAD64 reachable slice. [src+probe]
- **[completeness] Phase split (Segmentation vs Final) — CONFIRMED at source.** In
  `ScoringPhase::Segmentation` the progression signals (`w_seq`/`w_dim`/`wStep*`) and Gate R are
  suppressed; only `rootContinuityBonus` stays active (`applyProgressionSignals` gate, :362, :417-424,
  :439-442, :268). Correctness depends on the caller setting the phase right; a wrong phase silently
  drops signals. A real conditional-correctness surface, but inputs-assumed-correct → phase-2.
- **[completeness] Empty-snapshot / threshold paths.** `chosenPerBass.empty()` → `results` empty,
  `chosenResult` untouched (:495-541); the diff-root append is gated on `inversionSuspicionMargin > 0`
  and winner == bass (:519-522). Handled, no gap found.

---

## §4 — Gaps → obligations (tagged STRUCTURAL vs CORRECTNESS)

| # | obligation | tag |
|---|---|---|
| **H1** | **Cadential-6-4 competition rule.** I64-over-^5 → V. The largest single competition-reachable pattern (CAD64 164 + ~20 present = ~7–8 % of the residual, ~184 regions). | `[CORRECTNESS]` `[priority: chord-axis]` `[fix: behavior-changing — new functional rule; borders Stage-6 labeler]` |
| **H2** | **Leading-tone / viio↔V7 share-tone discriminator.** ~50 ROOT_PRESENT `vii` cases pick the wrong root in the symmetric/share-tone set. Overlaps the audit-#5 symmetric floor (C3) — part hand-buildable (rotation discriminator), part reserved. | `[CORRECTNESS]` `[priority: chord-axis]` `[fix: behavior-changing; partly floor]` |
| **H3** | **Bass-anchoring bias.** In 216/345 (63 %) present cases the competition roots on the bass while DCML roots on an upper voice (the `appliedBassBonus` + per-bass-group structure). The mechanism behind much of the wrong-winner mass. | `[CORRECTNESS]` `[priority: chord-axis]` `[fix: behavior-changing — competition-structure-level]` |
| **H4** | **Applied-dominant labeling** (50 present / 214 all_differ with `/`). The root is often present/correct; the disagreement is a key/label gap → mostly a Stage-6 labeler obligation, NOT a root re-pick at this layer. | `[CORRECTNESS]` `[priority: chord-axis — but downstream of this layer]` `[fix: Stage-6]` |
| **H5** | **The competition layer fuses two responsibilities** (progression/temporal scoring + winner selection). Lift the six bonus functions + `applyStepBonusGuard` out of the driver. | `[STRUCTURAL]` `[priority: phase-2 decomposition]` `[fix: structural refactor — fix-first per the sequencing gate]` |
| **H6** | **gateCtx marshalling couples this layer to the downstream gate layer's input struct** (knows `PostScoringGateContext`'s fields). A seam to revisit in the gate-dissolution (C2). | `[STRUCTURAL]` `[priority: phase-2 — feeds the gate-dissolution]` `[fix: structural]` |
| **H7** | **Heuristic accretion** (Iter-86/91/95/96/97 bonuses + with/without-wDim dual competition + 2 guards). Interaction hard to reason about; phase-2 "right structure?" review. | `[STRUCTURAL — quality]` `[priority: phase-2]` `[fix: structural; not a measured error]` |
| **H8** | **~76 % of the functional residual is NOT this layer's.** 38.7 % ROOT_ABSENT (functional model / floor) + 37.7 % HELD (segmentation over-segmentation). The headline "competition owns the 91 % functional residual" must be re-attributed. | `[scoping finding]` `[priority: routes obligations to segmentation (S1/S2) + the functional-model/floor, not here]` |

---

## §5 — Reconciliation with Cowork's note + the [prov] dispositions

| Cowork / map claim | verdict |
|---|---|
| "**This is where 95 % of root errors live**" | **RE-ATTRIBUTED.** 91.0 % (not 95.2 %) of root errors are *functional*; but only **~24 % of that residual is reachable at THIS layer** — 38.7 % is root-absent (floor/functional model) and 37.7 % is segmentation. The competition layer is where the *winner is chosen*, but it is not where most of the residual is *fixable*. |
| `[prov ≈ 26–55 % rule-reachable]` (B1) | **CONFIRMED cross-layer, CORRECTED for this layer.** The 26–55 % credits segmentation + key + Stage-6 labeler. THIS layer's reach ≈ 24 % of the residual (~509 regions); pure-rerank slice ≈ 1.7 % (36). |
| Three responsibilities (competition / temporal-scoring / **function**) | **CONFIRMED as a split, CORRECTED to 2-way.** In-body: temporal-scoring + competition. **function/degree is delegated to `buildChordResult` (chordanalyzer.cpp:952)** — a different layer. Added: gateCtx marshalling (H6). |
| Wrong-winner is largely rule-reachable / hand-buildable | **CONFIRMED + sharpened** — the reachable part is **functional rules (cad64 / share-tone / applied), not generic bonus re-weights** (the rerank slice is tiny; the rest needs new functional candidates a 2nd vertical analyzer also misses). |
| Heuristic accretion = phase-2 structure concern | **CONFIRMED** (H7) — structural-quality, not a measured error. |
| Function/degree inherits the key → wrong degree if key wrong | **CONFIRMED but RELOCATED** — that inheritance is in buildChordResult, reached *through* this layer's call, not in its body. |

**Net:** the chord-axis-healthy / hand-buildable verdict **HOLDS**. The substantive corrections are
(a) the residual must be **re-attributed across layers** — the competition layer owns ~24 %, not the
headline 91 %; (b) its reach is **functional rules (led by cadential-6-4), not bonus re-weights**; and
(c) the decomposition is **2-way (scoring + competition)**, with "function" already elsewhere.

---

## §6 — Method / unknowns / stop-conditions

- **Method:** byte-identical-corpus reasoning (HEAD = `tools/corpus/default` output; audit #5 proved
  the 4 intervening commits are verbatim splits) + a faithful three-way reproduction reusing the
  committed `compare_analyses`/`dcml_parser` (reproduces the dossier counts exactly: 2153/212/2365,
  91.0 %). Layer attribution from each region's `pitchClassSet`, emitted `alternatives` roots, and
  flanking-region roots. Source claims read at HEAD `a03c2493bb`.
- **Unknowns (surfaced, not guessed):** (1) the HELD/CAD64 boundary depends on the dispositioning of
  the cad64∩held overlap (I route it to CAD64; the dossier routes it to NHT) — moves ~95 regions
  between two non-competition buckets, no effect on this layer's reach. (2) The ROOT_PRESENT
  "needs-a-new-candidate" 309-region slice straddles competition vs Stage-6 labeler — I bound it
  (1.7 % pure-rerank, ~24 % total reach) rather than splitting it precisely; the 94.1 % m21==ours
  signal argues most of it is functional (labeler), shrinking this layer's share further. (3) `vii`
  share-tone (H2) overlaps the audit-#5 symmetric floor — the hand-buildable vs reserved split inside
  it is the floor question, not re-opened here. (4) Bach WiR-rntxt only (the gate corpus); jazz vocab
  unmeasurable read-only (audit #5 §3.3).
- **Stop conditions:** none hit. No production/inference/behavior change; the probe is read-only and
  byte-identical to production (no rebuild). Cross-layer findings (H4 Stage-6, H8 segmentation, H6
  gate-dissolution) recorded as phase-2 notes per the plan.

*Cowork verifies methodology + reconciles; user ratifies. Driver: `C:\tmp\cc_audit6_competition.py`
(+ `cc_audit6_present.csv`), throwaway/untracked. This report is the only repo write.*

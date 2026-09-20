# CC Stage 3.4-i — Gate-Retirement Dry-Run Dossier

**Date:** 2026-06-13 · **Base:** `548adb7b2e` (Stage 3.3 complete) · **Owner:** CC
**Roadmap:** 3.4 / 3.4b (per `docs/decoder_design.md` §7, §13 Q3/Q4)

This run delivers (1) the two pre-authorized byte-identical ships and (2) the per-gate
differential dry-run that measures design §7's "decoder-subsumed after 3.3" hypotheses
instead of executing them. **Nothing behavior-changing is committed in this run** beyond
the two byte-identical ships; everything else is measurement feeding the 3.4-ii / 3.2
decision menu (§5).

**Method note (the §7 correction this run confronts).** At beam 1 the pipeline is
numerically the *old* greedy pipeline (3.3 moved bonuses between layers, changed no
output). The post-scoring gates exist *because* the bonuses they re-rank did not, by
themselves, produce the right winner. So removing a gate at beam 1 changes output
wherever it fired — the §7 retirement verdicts are hypotheses to **measure**, which is
what §3 does.

---

## 1. Ship #1 — remove dead Gates B/C/D (Stage 3.4b)

**Commit:** `da1b440845` — *refactor: remove dead Gates B/C/D (Stage 3.4b — provably
unreachable since 1b-F1)*

**What.** Deleted the three temporal-confirmation blocks (Gate B forward-evidence, Gate C
3-region-window, Gate D consecutive-stepwise) of the Major-add6 ↔ Minor enharmonic flip
from `applyPostScoringGates()` (`chordanalyzer.cpp`), replaced with a historical marker
comment. Updated `docs/scoring_model.md` §6 table (the A–D row → A, B/C/D removed) and the
§8 "Gate A subsumes B/C/D" constraint (now historical, with the forward-looking caveat
that there is no longer a B/C/D safety net under Gate A).

**Why it is byte-identical (the unreachability proof, 1b-F1, re-verified empirically).**
Each of B/C/D guards on `!didEnharmonicFlip` **and** repeats Gate A's exact four core
conditions (`winnerIsMajor && winnerHasAddedSixth && altIsMinor && bestAlt.rootPc ==
(winnerRootPc+9)%12`) plus extra temporal evidence. Gate A has those same four conditions
with *no* temporal requirement and runs first, setting `didEnharmonicFlip = true` whenever
they hold. Therefore whenever B/C/D's conditions could hold, A has already fired and
`!didEnharmonicFlip` is false → B/C/D are unreachable.

**Proof gate — all green, byte-identical:**
- **Corpus A/B sha256: 0/353 diffs on Baroque, Jazz, Default** (per-score manifest
  fingerprints vs the HEAD baseline; the strongest available proof, stronger than the
  required identity-set check).
- Pipeline snapshots **11/11 zero-diff** (no golden refresh).
- composing **505/505**, notation **57/57** green.
- BIR identity sets unchanged: **Baroque 13 / Jazz 7 / Default 14** (exact case sets).

No diff appeared → the unreachability proof was correct (a diff would have been a major
finding and a hard stop).

---

## 2. Ship #2 — absorb Gate R into the rcb edge (+ overload cleanup) (Stage 3.4)

**Commit:** `a652dc1ba7` — *refactor: absorb Gate R into the rcb edge; drop the test-compat
overload (Stage 3.4)*

**What.** Per design §7 ("Gate R is absorbed, not retired"):
1. Encapsulated the Pass A rcb computation and its Gate R zeroing in a single file-local
   helper `rcbEdge(cell, fullBasisDep, previousRootPc, prefs, applyProgressionSignals)` in
   `harmonicfunctionlayer.cpp` (anonymous namespace) — the design's `rcbEdge(src, dest)`
   shape with the reconstructed-credit guard *inside* it. The former separate call-site
   `if (gateRZeroesRootContinuity(cell, fullBasisDep, rcb) && applyProgressionSignals)`
   folds into the helper with the **exact same short-circuit order** (both operands are
   side-effect-free, so the result is invariant). Pass A now calls `rcbEdge(...)` once per
   cell.
2. Deleted the 2-arg `gateRZeroesRootContinuity(cell, rcb)` test-compat overload
   (definition + header declaration); it merely forwarded `cell.basisDep`. The 3-arg
   predicate is now the sole entry point.
3. Re-pinned `gater_tests.cpp`'s four F2 branch tests to the 3-arg form, passing
   `cell.basisDep` explicitly — a **CALL-SHAPE re-pin only**, each branch marked in-place;
   the decision outcomes and the Δ=+7b end-to-end pins are untouched.
4. Updated `docs/scoring_model.md` §4 Gate R (rcbEdge home, overload removal, phase-guard
   location).

**Proof gate — all green, byte-identical:**
- **Corpus A/B sha256: 0/353 diffs on Baroque, Jazz, Default.**
- Pipeline snapshots **11/11 zero-diff** (no golden refresh).
- composing **505/505** (incl. the 9 `Composing_GateRTests` + the `DeltaPlus7b` diagnose
  acceptance pin), notation **57/57** green.
- BIR identity sets unchanged: **Baroque 13 / Jazz 7 / Default 14**.

HEAD after both ships (`a652dc1ba7`) is output-identical to the base `548adb7b2e` on all
353×3, so it is the valid reference baseline for the §3 differential.

---

## 4. The F4 / F6 / F8 re-decide inventory (paper)

For the Stage-1b findings owned by gates that will move, what the *correct* behavior would
be, what changes if fixed, and which retirement event should carry the fix. **No code.**

### F4 — mixed live/captured winner reads (H / I / K / L)

**The artifact.** The Sub-9a fix (`f3e0f5f72c`) migrated only Gate G-E to the captured
pre-bias `originalWinner*` snapshot. The others were left half-migrated:
- **Gate H** keys on captured `winnerBassIsRoot` but requires **live** `winner.quality ==
  Augmented`.
- **Gates I / K / L** key entry on captured `originalWinnerQuality` but compute the margin
  `winner.identity.score − alt.score` against the **live** `results[0]`, whose score may
  have been bias-deducted and whose identity may have been promoted by the bias re-sort.

After a bias correction fires, "the winner" the gate keys on and "the winner" it measures
the margin against can be *different candidates*.

**Correct behavior.** Each gate must read one consistent reference. The two coherent
choices: (a) **all-captured** — entry condition *and* margin both taken from the pre-bias
winner snapshot (the Sub-9a discipline, extended to H/I/K/L); or (b) **all-live** — both
taken from the post-bias `results[0]`. (a) is the better semantics: these gates ask "was
the *originally selected* winner a suspicious inversion?", which is a pre-bias question;
the margin should then be the pre-bias margin too. The current half-migrated read is
neither and has no defensible meaning.

**What changes if fixed.** Only in regions where the **bias correction also fired** on the
same region (the overlap set). There, the live margin differs from the captured margin by
the bias deduction (`bassNoteRootBonus × (1 − inversionBonusReduction)` = up to 0.70), so a
margin that currently sits just inside/outside a gate's bracket (I ≤ 0.45, K ≤ 0.20, L ≤
0.35) can flip the gate's decision. The §3 differential for I/K/L gives each gate's total
footprint; the F4 subset is "gate-region ∩ bias-region", measurable by intersecting the
I/K/L regiondiff with the BIAS regiondiff. Fixing changes a strict subset of those.

**Which retirement event carries the fix.** Per Q4 (DECIDED: reproduce at beam-1, then
fix-as-retire per-gate with a differential — never a silent fix). I/K/L are
"decoder-subsumed after 3.3" (§7): at retirement their margins become decode tie-breaks
against *consistent path state*, so the live/captured ambiguity dissolves by construction —
**the fix is carried by I/K/L retirement (3.4-ii)**. Gate H "stays re-rank initially"
(a wDim-style forward edge may subsume it): the fix is carried at **H's retirement or its
fold into a rotation edge**, whichever lands first. In both cases the re-decide is the
retirement commit's per-gate differential, not a separate hygiene change.

### F6 — gate swaps can leave `results[]` unsorted

**The artifact.** A G-E pull-and-swap can leave `results[]` in non-descending score order
(the Sub-9a fixture ends `[1.7, 1.3, 2.35]`). `results[0]` (the committed winner) is
correct; the **tail** (the alternatives list surfaced to the user / emitted to
`.ours.json`'s `alternatives`) is not score-ordered.

**Correct behavior.** The emitted alternatives should be score-descending after `[0]`. The
winner slot must be preserved (it was chosen by the gate, not by score), so the fix is a
stable sort of `results[1:]` by score — *not* a full re-sort (which could displace the
gate-chosen winner).

**What changes if fixed.** The **alternatives arrays only** (order, never the winner) on
every region where a gate swap left an unsorted tail. This is an output change to
`.ours.json` `alternatives` and the user-facing alternatives list → **not byte-identical**
→ must be a conscious re-decide with refreshed snapshots/corpus, never a silent edit.

**Which retirement event carries the fix.** Per Q5 (DECIDED: the decoder emits the full
path + per-node alternatives + margins, with the committed identity as `path.front()`). The
natural home is the **decoder's output-assembly** (3.4-ii/3.5 output interface): when the
decode emits each node's alternatives it can order them by emission score by construction,
retiring the unsorted-tail artifact without a bolted-on sort. Until then the artifact is
cosmetic (winner correct) and is reproduced at beam-1.

### F8 — G-E can push a duplicate

**The artifact.** When the HalfDim alt is absent from `results[]`, Gate G-E pulls it from
`rawCandidates` and `push_back`s a built result, then may swap it to `results[0]`. Because
its scan starts at `i = 1` and there is no dedup, the pulled candidate can duplicate one
already present (the Sub-9a fixture ends at `results.size() == 3` with a duplicate). (Sibling
finding F7 — the pull has no `gateCtx.threshold` check, unlike FM2 — is adjacent; Task 4 is
scoped to F4/F6/F8 but F7 should ride the same fix.)

**Correct behavior.** Dedup the candidate set: do not append a `rawCandidates` pull that is
identity-equal to an existing entry, and pop the phantom on every non-fire path (the
no-sub-gate-fired pop already exists; the duplicate case is the gap). Combined with F7, the
pull should also respect the emission threshold so a deeply sub-threshold HalfDim cell is
not promoted by key function alone.

**What changes if fixed.** The **alternatives arrays only** (size/content) on G-E-fired
regions; the winner (the swapped HalfDim) is unchanged. Output change → **not
byte-identical** → conscious re-decide.

**Which retirement event carries the fix.** Gate G-E "stays re-rank → Stage-6 functional
layer" (§7) — it is among the longest-surviving gates (it encodes a viiø7/iiø7/iiiø7
*functional* decision). So the duplicate-push artifact persists until **G-E folds into the
Stage-6 functional layer**, where the candidate set is assembled once and deduped by
construction. If an earlier cleanup is wanted, it lands with the F6 alternatives-ordering
re-decide (same output surface, same snapshot/corpus re-pin) — the two are naturally one
"alternatives-list hygiene" re-decide.

---

## 3. Per-gate differential table

**How measured.** One env-driven `gateDisabled("ID")` switch added to every gate's entry
condition (TEMPORARY, never committed; proven inert when `MS_DRYRUN_DISABLE_GATE` is unset:
0/353×3 sha256 + snapshots 11/11). For each gate, *only that gate* was disabled, then:
the composing suite (pins), `pipeline_snapshot_tests` (drift), and a corpus A/B ×3 with
per-region winner diff vs the HEAD baseline + `characterise_bir_false` identity sets.

**Two facts hold across the WHOLE table, and they reframe everything below:**

1. **Every gate is BIR-identity-neutral on Baroque (13) and Default (14).** Not one gate's
   removal changes the Baroque or the user-facing Default BIR identity set. *All* BIR
   movement is on **Jazz only** (a batch-tools-only preset): Gate **I** −5 fixes (7→12 when
   removed), bias correction **+1 harm** (7→6 when removed, i.e. it *causes* bwv74.8). So
   from the user-experienced-error standpoint (Default = the 14-case gate), **gate
   retirement is BIR-free** — the gates earn their keep through snapshot structure and Jazz,
   not the user-facing metric.

2. **The preset-gated block (A, FM2, E, F, G-E, G-B/C/D, H, and the bias *bonus* arm) runs
   ONLY under Baroque.** `batch_analyze.cpp:1397/1411` — Jazz and **Default** both have
   `preferMinorOverMajorAdd6 = false` (verified). So under the user-facing config these
   seven gates **never execute** (every "0" in their Default/Jazz region columns is
   structural, not "didn't happen to fire"). Their retirement is a Baroque-batch-metric
   concern with **zero user-facing impact**.

**Changed-region counts are a footprint upper bound, not direct fire counts** — a gate that
changes one root re-threads `previousRootPc` and the inline same-root merge, splitting/
merging downstream runs (the cascade). The load-bearing signals are the **BIR identity-set
delta** and the **snapshot drift**; the region count is the coarse footprint.

| Gate | Pins that fail w/o it | BIR b / j / d (Δ) | Δregions b / j / d | Snaps | Class | Mutates id? → Q3 |
|---|---|---|---|---|---|---|
| **bias** | 4: BiasCorrection ×3 + Sub9a-ordering | 13 / **6** (−1) / 14 | 59 / 36 / 57 | **8** | **C2** | yes (deduct+resort) → caps beam |
| **A (+FM2)** | 2: GateA_FastPath, GateA_FM2 | 13 / 7 / 14 | 105 / 0 / 0 | 0 | **C4** | yes (Maj→Min swap) → caps beam |
| **E** | 1: GateE_MinorWinnerFlips | 13 / 7 / 14 | **0 / 0 / 0** | 0 | **C1** (would be C2) | yes → caps beam |
| **F** | 1: GateF_MajorWinnerFlips | 13 / 7 / 14 | **0 / 0 / 0** | 0 | **C1** (would be C2) | yes → caps beam |
| **G-E** | 3: GateGE ×2 + Sub9a-ordering | 13 / 7 / 14 | 10 / 0 / 0 | 0 | **C4** | yes → caps beam |
| **G-B/C/D** | 3: GateGB, GateGC, GateGD | 13 / 7 / 14 | 1 / 0 / 0 | 0 | **C4** (near-dead) | yes → caps beam |
| **H** | 2: GateH_+4, GateH_+8 | 13 / 7 / 14 | 3 / 0 / 0 | 0 | **C2** (near-dead) | yes (aug rotation) → caps beam |
| **I** | 3: GateI_Margin **+ both Δ=+7b Gate-R pins** | 13 / **12** (+5) / 14 | 28 / **182** / 32 | **3** | **C2 (load-bearing)** | yes → caps beam |
| **K** | 2: GateK_Margin, GateK_SharpFifth | 13 / 7 / 14 | **0 / 0 / 0** | 0 | **C1** (would be C2) | yes → caps beam |
| **L** | 1: GateL_Margin | 13 / 7 / 14 | 0 / **18** / 0 | 0 | **C2** (Baroque-dead/Jazz-active) | yes → caps beam |
| **J** | 1: GateJ_DimTriad…V65 | 13 / 7 / 14 | **137 / 227 / 143** | 1 | **C5 (structural keeper)** | yes (Dim→V7) → caps beam |
| **Iter 86** | 1: Iter86_BassAtFlatSeven | 13 / 7 / 14 | **0 / 0 / 0** | 0 | **C1** (would be C3) | yes (stamp m7) → caps beam |
| **Iter 91** | 2: Iter91_PatternA, _PatternB | 13 / 7 / 14 | 8 / 0 / 3 | 0 | **C2** (near-dead) | yes (bass→root) → caps beam |

### Per-gate notes (the rows that carry weight)

- **bias correction — C2, large footprint, slightly mis-tuned on Jazz.** 59/36/57 regions,
  **8 of 11 snapshots** drift — the broadest structural footprint of any gate. BIR-neutral
  on Baroque/Default. On Jazz it *introduces* one error (bwv74.8@13440 Em7/D; removing bias
  drops it from BIR=false → 6). §7 calls it decoder-subsumed (proper inversion edges remove
  the over-fired bass-root bonus when it is the sole decider). **3.2 acceptance case**: the
  decoder's inversion edges must reproduce the 8-snapshot Baroque structure; expected delta
  Baroque 13 (hold), Jazz ≤ 7 (the bwv74.8 over-correction is an opportunity, not a
  must-hold). The bonus arm (`kHalfDimFirstInversionBonus`) is Baroque-only; the deduction
  arm runs on all configs (hence Default = 57 regions).

- **Gate I — C2, the highest-stakes retirement.** Two independent proof obligations:
  (a) it fixes **5 Jazz** "our `Xm7/Y` slash vs DCML major" cases (bwv286@2760, bwv355@17640,
  bwv386@9480, bwv388@12360, bwv428@18000) — removing I regresses Jazz 7→12; and (b) it is
  **coupled to the Δ=+7b trio** — disabling I fails BOTH Gate-R Δ=+7b pins
  (`E2E_GateR_DeltaPlus7b_FirstInversionBeatsContinuedRoot`, `DiagnoseTests.DeltaPlus7b…`),
  i.e. Gate R (zeroes the bare-root rcb) and Gate I (selects the first-inversion Major over
  the root-position Minor) **together** produce the bwv245.28/296/320 fix that §11 says
  Stage 3 must NOT break. So I cannot retire until the decoder reproduces *both* — the 5
  Jazz fixes (expected Jazz 7) and the Δ=+7b first-inversion selection (expected the trio
  unchanged). Its margin (≤ 0.45) becomes the decode tie-break (§7).

- **Gate J — C5, structural keeper, and the metric is blind to it.** The single largest
  footprint (137/227/143 regions across all three configs; vii° is ubiquitous in chorales)
  and the only non-preset-gated gate that fires heavily on Default, yet **BIR-identity-
  neutral on every config** and only 1 snapshot drift (mozart_k280_1). vii°→V6/5 is a
  structural 4-PC identity (`{R−4,R,R+3,R+6}` = V7); §7 keeps it longest (eventually an
  emission/functional decision, Stage 6). **Finding: BIR does not see J at all** — its 137
  Baroque region changes are all outside the BIR=false set. Defer; do not retire on the
  strength of a BIR-neutral reading (that would be a false "dead" verdict).

- **C1 dead-in-practice — E, F, K, Iter 86 (0 regions on all 353×3).** Their pinned logic
  still passes (synthetic fixtures), but they fire **nowhere** on the corpus under any
  config. Candidates for immediate removal (listed for ratification; **not shipped here**).
  **Caveat (the C1 risk):** "dead" is scoped to the 353-score Bach-chorale corpus × 3
  configs. E/F (1st/2nd-inversion Minor→Major) and K (1st-inversion Augmented, originally the
  bwv40.6 fix) target classical inversion shapes the *current* pipeline no longer reaches —
  the pipeline has changed massively since their commits (greedy-expand seg, joint scoring,
  Gate R). Before removal, ratification should weigh whether the chorale corpus exercises
  these specific shapes (Iter 86's bass-b7 stamp and K's augmented-inversion are plausibly
  just genuinely superseded; E/F deserve a glance at a non-chorale score if one is on hand).

- **Gate L — C2, Baroque-dead / Jazz-active misalignment.** Calibrated for Baroque
  (bwv144.6 B+→B etc., margin ≤ 0.35), L now fires on **0** Baroque and **0** Default
  regions but **18 Jazz** regions (BIR-neutral). It is not preset-gated, so it survives on
  Jazz while doing nothing for its Baroque target. Low-risk C2 (decode tie-break), but the
  misalignment is worth flagging: its stated rationale no longer matches its footprint.

- **A / G-E / G-B/C/D — C4 (functional), Baroque-only.** A (105 Baroque regions, the second-
  largest footprint, BIR-neutral) is the Major-add6 ↔ Minor enharmonic preference; G-E (10
  regions) gates on viiø7/iiø7/iiiø7 key function; G-B/C/D (1 region, near-dead) are its
  temporal fallbacks. All Baroque-only (0 on Default/Jazz). §7 routes the enharmonic/key-
  function decisions to the **Stage-6 functional layer**. Defer. (A's 105-region Baroque
  footprint with zero BIR effect says the Major-add6↔Minor choice is a labeling preference,
  not an accuracy fix — consistent with C4.)

- **H (3 regions) / Iter 91 (8 Baroque + 3 Default) — C2, near-dead.** Augmented rotation
  (H) and forward-context bass-root promotion (Iter 91); both BIR-neutral, tiny footprints,
  no snapshot drift. Low-risk decode/forward-edge subsumption; effectively retirement-ready
  pending pin reproduction, but not worth a dedicated 3.2 acceptance case.

---

## 5. Decision menu for 3.4-ii / 3.2

**(A) Retire now — the C1 dead-in-practice set (ratification-gated; NOT shipped in this run).**
`E`, `F`, `K`, `Iter 86` — 0 changed regions on all 353 scores × 3 configs. Each removal is
expected byte-identical *on this corpus* (the §3 measurement already shows 0 region change
when disabled). Ship each as its own commit with the corpus A/B + the pin converted to a
historical-logic note or removed. **Blocking question for ratification:** is the 353-score
Bach-chorale corpus representative for these four specific shapes? (Iter 86 bass-b7 stamp
and K augmented-inversion read as genuinely superseded; E/F warrant a non-chorale spot-check
if a score is available.) If yes → four clean removals. If no → keep E/F, remove K + Iter 86.

**(B) 3.2 acceptance cases — the C2 gates, with measured expected deltas.**

| Gate | What the wider beam must reproduce | Expected delta (hold-line) |
|---|---|---|
| **I** *(highest stakes)* | 5 Jazz 1st-inv-Major-over-root-Minor fixes **+** the Δ=+7b first-inversion selection (coupled with Gate R) | Jazz **7** (no regression to 12); Δ=+7b trio unchanged; Baroque 13 |
| **bias correction** | the 8-snapshot Baroque inversion structure via proper inversion edges | Baroque 13 + snapshots reproduced; Jazz ≤ 7 (bwv74.8 over-correction is upside) |
| **L** | the 18 Jazz tie-breaks (margin ≤ 0.35 → decode tie-break) | Jazz 7; Baroque/Default unchanged |
| **H** | the 3 Baroque augmented rotations (wDim-style forward edge) | Baroque 13 unchanged |
| **Iter 91** | the 8 Baroque + 3 Default forward bass-root promotions | unchanged ×3 |

Sequencing (Q3, DECIDED (a)): **every** remaining gate mutates root/quality/bass, so for
each the **3.4 retirement leads 3.2 beam-widening past it** — there is no structural-non-
mutating gate that 3.2 could widen past early. 3.2 is therefore fully gated behind 3.4 for
the identity-mutating set, which is all of them.

**(C) Defer — C4 functional (Stage 6) and C5 structural (Stage 6 emission).**
`A`, `G-E`, `G-B/C/D` (C4, Baroque-only, enharmonic/key-function → Stage-6 functional layer)
and `J` (C5, the structural vii°→V7 keeper, BIR-blind, defer until the functional/emission
layer can express it). None block 3.2 on the user-facing config (A/G-family don't run on
Default; J is BIR-neutral). They remain post-decode re-ranks until their layer exists.

**Headline for 3.2 planning.** On the user-facing Default config, gate retirement is
BIR-identity-free; the only BIR-relevant gate in the whole set is **I on Jazz** (and it is
double-coupled to the must-not-break Δ=+7b trio). So 3.2's beam-widening risk is
concentrated almost entirely in **one gate's two proof obligations**, not spread across
thirteen. That is the single most actionable result of this dry-run.

---

## 6. Unknowns / caveats

1. **Changed-region counts include the merge/temporal cascade.** A gate that changes one
   root re-threads `previousRootPc` and the inline same-root merge, so one gate fire can
   produce several region-level diffs (and J's 137/227/143 is mostly cascade). The counts
   bound the footprint; they are not fire counts. BIR-identity delta + snapshot drift are
   the trustworthy signals.

2. **"Dead-in-practice" is corpus-scoped.** E/F/K/Iter 86 = 0 regions on the 353-score
   Bach-chorale corpus × {Baroque, Jazz, Default}. A different repertoire could exercise
   E/F (classical inversions) or K (augmented). Removal ratification should consider corpus
   representativeness for those specific shapes (see §5(A)).

3. **Default `preferMinorOverMajorAdd6 = false` is verified** (`batch_analyze.cpp:1411`), so
   the preset-gated-block "0 on Default" columns are structural. But the *live product*
   uses `kDefaultChordAnalyzerPreferences`; the batch "Default" reproduces it per D-PASS0 —
   this dossier trusts that equivalence (Stage 2.4 V4), it did not re-derive it.

4. **Gate I × Gate R coupling on Δ=+7b is established but not mechanically dissected here.**
   I confirmed disabling I fails both Δ=+7b Gate-R pins; I did not trace whether I selects
   the first inversion directly or whether its absence shifts the bias sort. The 3.2 work
   that retires I must reproduce the trio, so the exact mechanism is a 3.2 design input, not
   a 3.4-i deliverable.

5. **Pin/gate coupling beyond Δ=+7b.** `Ordering_Sub9a_GateGEUsesPreSortWinnerRoot` fails
   under both bias-disable and G-E-disable (it pins their interaction); not a problem, but a
   note that some pins are joint obligations of two gates, so "which pins fail" is not a
   clean partition.

6. **This run changed nothing behavior-wise** beyond the two byte-identical ships. The
   env-harness is uncommitted and reverted; the working tree is restored to `a652dc1ba7`
   (verified: corpus regenerated env-unset, source harness reverted, suites green).

---

## ADDENDUM — Stage 3.4-ii correction (2026-06-13)

The Stage 3.4-ii non-chorale spot-check + a **byte-level** corpus proof gate falsified the C1
"dead-in-practice" verdict (§5(A)) for **all four** gates. Full write-up:
`cc_stage3_4ii_report.md`. Two corrections to this dossier:

**(i) §3 metric correction — the differential measured WINNER changes only.** The per-gate
"Δregions" column counts per-region **winner** diffs; it is **blind to winner-neutral
alternatives-list changes**. The stricter `.ours.json` **sha256** comparison (the proof-gate
standard) catches them. Consequence: the §3 rows showing **E** and **F** at `0 / 0 / 0`
Δregions and class **C1** are wrong at the byte level — both change the alternatives list on
real Baroque chorales without moving a winner:
- **Gate E** alters `.ours.json` on **bwv245.3** and **bwv336** (Baroque) — winner-neutral
  (region-winner diff empty), reproducible (determinism-checked), isolated to the Gate E block.
- **Gate F** alters `.ours.json` on **bwv245.3-class** alternatives; on the non-chorale set it
  is winner-neutral on Mozart K283-3 (redundant with the bias correction).

**(ii) §5 reclassification — the C1 "retire-now" set is EMPTY.**
- **E → C2′ (alternatives-hygiene)** — was C1. Winner-neutral but not byte-identical to remove
  (bwv245.3, bwv336). The 3.4-ii Gate-E removal was implemented, hit the Baroque corpus
  stop-condition (2/353), and was **reverted**.
- **F → C2′ (alternatives-hygiene)** — was C1. Winner-neutral, redundant with the bias
  correction. Kept.
- **K → C2** — was C1. **Changes winners** on chromatic non-chorale repertoire (Chopin op24-4
  ×3, K333-1 Jazz). Never truly C1.
- **Iter 86 → C2** — was C1. **Changes winners** on Mozart K310-1 (×3); DCML-correct
  (`#viio7` root reproduced). Never truly C1.

No gate was retired in 3.4-ii; the tree remains byte-identical to `a652dc1ba7`. The §5(B)
acceptance table gains K, Iter 86 (C2) and E, F (C2′) — see `cc_stage3_4ii_report.md` §4.

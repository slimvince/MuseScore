# CC report — Stage-5 fitter, Phase 2.2b: verdict evidence completion + the JOINT FIT — candidates + PREPARED verdicts, nothing adopted or retired

**Dispatch:** `cc_instruction_stage5_phase2_2b.md` (Cowork, 2026-07-05) · **Design:** `cowork_stage5_fitter_design.md` (SIGNED, P1-ratified; §4.2/§4.4 family 2, D-7, §15 O-7)
**HEAD at dispatch:** `a31b56639d` · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** the fifth CC increment of the Stage-5 arc — completes the 2.2a audit's scope caveats (cross-carrier, full-corpus, firing-site-level) and runs the P1-ratified JOINT FIT under three declared rule configurations. **NOTHING adopted; no committed constant value changed; NO rule retired.** Produces per-rule VERDICT PROPOSALS + fit CANDIDATES with full decision surfaces; every verdict and every adoption is a separate user-ratified event.

---

## Commit SHAs (this dispatch)

| # | SHA | Type | Contents |
|---|---|---|---|
| 1 — evidence tools + ledgers | **`e5a1bb7a0e`** | `feat(tools):` | the 6 `stage5_2_2b_*.py` drivers (evidence/jointfit/surface/dlc/snapshot/analyze) + the committed ledgers under `tools/fit_ledgers/` (disable-fullcorpus, firing-sites 968, dlc-probe, jointfit ×3, surface ×2). Measurement-only; no `src/`; corpus untouched. |
| 2 — this report | *(this commit)* | `docs(cowork):` | `cc_stage5_phase2_2b_report.md` (force-add; `/cc_*.md` is gitignored) |
| 3 — the fold | *(next commit)* | `docs(cowork):` | STATUS 22p (CC-delivery) · COWORK_HANDOFF · design (O-7 joint-fit-result marker) · `cowork_style_taxonomy_proposal.md` (§6/§6a Cowork record) · `cc_instruction_stage5_phase2_2b.md` (force-add) |

---

## Task 0 — state check

- **HEAD** `a31b56639d`, branch `master`, fork-only, local/unpushed.
- **Dirty set matched the dispatch's expectation exactly:** the three Cowork narrative fold files carrying the session-22p verification+dispatch record (`STATUS.md`, `COWORK_HANDOFF.md`, `cowork_style_taxonomy_proposal.md` — the KNOWN §6/§6a preset-layer Cowork edit) + the deliberately-untracked scratch (`idiom_discovery/vl_*_out.txt`, `scratch_artifacts/`). Nothing else. **No STOP.**
- **Corpus:** baroque/jazz/default each **352 `.ours.json` + 352 `.music21.json` + 352 `.xml`**; manifest `git_hash 0dd64660f4` (unchanged). Reference corpus read-only throughout (every regen to scratch).
- **Binary check:** `batch_analyze.exe` (11:10, the 2.2a mechanism build) honors `disable_rule` — verified live (`param-override: applied 1 overrides (… 1 §6 rules disabled)`); no `src/` change is unbuilt (HEAD `a31b56639d` is a docs-only fold; `7367c7ae96` was tools-only).
- **Suites at entry:** composing 1116 / notation 53 / snapshots 11 (2.2a end-state).

---

## Task 1 — verdict evidence completion (read-only; closes the 2.2a scope caveats)

**Full-corpus baselines (all rules on), reproduced exactly vs the ratified §4.2 baselines:**

| carrier | root % | RN % | key % | batch | clsB dur | clsA dur |
|---|---|---|---|---|---|---|
| Baroque | 63.3234 | 44.5641 | 68.1767 | 53 | 2934800 | 107040 |
| Jazz    | 62.3664 | 42.3990 | 64.5161 | 24 | 2997520 | 122880 |
| Default | 63.2192 | 44.4020 | 67.7736 | 53 | 2938400 | 112080 |

(Baroque 63.32 / Jazz 62.37 / Default 63.22 — the ratified A-8 variant-(b) baselines, batch 53/24/53 — reproduced to 4 dp.)

### Task 1.1 — the cross-carrier, full-corpus disable table (14 rules × 3 carriers = 42 evals + 3 baselines)

Δroot / batch(Δ) / batch added-removed-changed (+/−/~) / clsB-dur-Δ / clsA-dur-Δ, per rule per carrier, on the FULL corpus (the 2.2a audit was fitting-split/Baroque-only). `stage5_rule_disable_fullcorpus.jsonl`.

| rule | Bar Δroot | Bar batch | Bar clsBd | Jaz Δroot | Jaz batch | Jaz clsBd | Def Δroot | Def batch | Def clsBd |
|---|---|---|---|---|---|---|---|---|---|
| **BiasCorrection** | −0.0058 | 52 (−1) | +240 | **+0.0318** | **22 (−2)** | +240 | +0.0029 | 53 (0) | +2640 |
| **FM2** | −0.0521 | **54 (+1)** | +4320 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| GateA | 0 | 53 (0) | 0 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| GateE | +0.0058 | 53 (0) | −480 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| GateF | 0 | 53 (0) | 0 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| GateGE | +0.0058 | 53 (0) | −1920 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| GateGB | 0 | 53 (0) | 0 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| GateGC | 0 | 53 (0) | 0 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| GateGD | **+0.0058** | 53 (0) | −480 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| GateH | +0.0058 | 53 (0) | 0 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| **GateI** | −0.0362 | 53 (0) | +3000 | **−0.3216** | **29 (+5)** | +26880 | −0.0420 | 53 (0) | +3480 |
| GateK | 0 | 53 (0) | 0 | 0 | 24 (0) | 0 | 0 | 53 (0) | 0 |
| **GateL** | 0 | 53 (0) | 0 | **−0.0174** | 24 (0) | +960 | 0 | 53 (0) | 0 |
| **GateJ** | **+0.0752** | 53 (0) | −8160 | **−0.4515** | 24 (0) | +36480 | **+0.0608** | 53 (0) | −6960 |

Denominators: Δroot/batch/clsB-dur are full-corpus variant-(b) duration-weighted; batch is the full-corpus BIR=false case count vs the committed 53/24/53.

**Batch set-diffs (every non-empty diff, explained per case with class):**
- **BiasCorrection off** → Baroque removes `bwv60.5@30960` (b); **Jazz removes `bwv301@1440` (b) + `bwv74.8@13440` (b)** — i.e. BiasCorrection *causes* three pitch-class-decidable class-(b) batch errors across presets (removing the correction fixes them).
- **FM2 off** → Baroque adds `bwv227.7@18000` (b) — FM2 prevents a class-(b) error (load-bearing).
- **GateI off** → **Jazz adds 5 class-(b) batch cases** (`bwv286@2760, bwv355@17640, bwv386@9480, bwv388@12360, bwv428@18000`) — GateI is heavily load-bearing on Jazz.
- All other rows: EMPTY batch set-diff.

**★ Cross-carrier reveals the 2.2a Baroque-fitting-split view could not show:**
1. **GateI is far more load-bearing on Jazz** (−0.3216, **+5 class-(b) batch cases**) than on Baroque (−0.0362, 0 batch). Decisive **retain** evidence.
2. **GateJ is catastrophic to disable on Jazz** (**−0.4515, clsB +36480**) while disable-beneficial on the Baroque/Default root-only objective (+0.0752/+0.0608). The Jazz load-bearing is the decisive Gate-J evidence.
3. **BiasCorrection is class-(b)-harmful**: disabling it *removes* class-(b) batch cases on Baroque (1) and Jazz (2). Net +root when disabled on Jazz/Default.
4. **The preferMinorOverMajorAdd6 structural expectation CONFIRMED (not assumed):** Gates A/E/H (and GateGE/GateGB/GateGC/GateGD) are **structurally zero on Jazz and Default** (0 sites, Δ=0) — they sit behind `preferMinorOverMajorAdd6` = FALSE on those presets. Verified in the table, not asserted.

### Task 1.2 — firing-site extraction (per-cell regen-diff, rule OFF vs baseline ON)

Committed ledger `tools/fit_ledgers/stage5_rule_firing_sites.jsonl` (968 rows). Method: full-corpus regen rule-off vs baseline, union-of-region-boundaries cell grid, a cell whose chosen root_pc OR chord_symbol differs is an effective site (post-scoring gates re-root within fixed boundaries; the diff includes the rootContinuity cascade footprint — the rule's *effective* sites per the dispatch). Merged into runs; each records stem@tick, our-root-ON, our-root-OFF, WiR root + WiR roman numeral (where covered), duration, two-tier class.

Firing-site counts (sites / WiR-covered), per rule per carrier:

| rule | Baroque | Jazz | Default |
|---|---|---|---|
| BiasCorrection | 61 (57) | 35 (35) | 59 (55) |
| FM2 | 16 (16) | 0 | 0 |
| GateA | 0 | 0 | 0 |
| GateE | 2 (1) | 0 | 0 |
| GateF | 0 | 0 | 0 |
| GateGE | 9 (8) | 0 | 0 |
| GateGB | 0 | 0 | 0 |
| GateGC | 0 | 0 | 0 |
| GateGD | 1 (1) | 0 | 0 |
| GateH | 3 (3) | 0 | 0 |
| GateI | 28 (28) | 186 (173) | 30 (30) |
| GateK | 0 | 0 | 0 |
| GateL | 0 | 18 (18) | 0 |
| GateJ | 133 (124) | 248 (227) | 139 (130) |

**Cross-carrier-fully-inert set (0 sites on ALL THREE carriers)** = **{GateA, GateF, GateGB, GateGC, GateK}** (5). The 2.2a fitting-split inert-7 loses **GateGD** (1 Baroque full-corpus site — inert on the fitting split, live on held-out) and **GateL** (18 Jazz sites, load-bearing there) — both "live elsewhere → drop out of the dissolution-candidate set" per the dispatch.

### Task 1.3 — founding-case dispositions (scoring_model §6 "why it exists")

- **Gate K — founding `bwv40.6` (A+ → F♯5/A):** the rule **no longer touches it** (0 firing sites anywhere). Gate K is fully inert; the first-inversion-augmented correction it was built for is now produced upstream (the augmented-rotation handling that survives is Gate H / the scoring templates), not by Gate K's swap.
- **Gate L — founding `bwv144.6` (B+→B), `bwv245.15` (E+→E):** the rule **no longer touches either on Baroque** (0 Baroque sites). Note both are now **in the CLAUDE.md Baroque-53 batch set** — i.e. the founding "fixes" are themselves now BIR=false cases, absorbed/overtaken upstream; Gate L's live work today is on **Jazz** (18 sites), not its Baroque founding cases.
- **Gate J — founding class `{R−4, R, R+3, R+6}` (a root-position vii° voicing the dominant root = V6/5):** the rule is **very much live** (133 Baroque / 248 Jazz / 139 Default sites) and its firing sites are dominated by WiR V-family + share-tone-"other" labels — see the Task 1.4 table. It is the opposite of the inert gates: a structurally load-bearing rule.

The founding-case check is itself evidence: Gates K and L have been **superseded upstream** (their Baroque founding fixes no longer flow through the rule), which is exactly the retirement signal D-7 wants — a rule that no longer changes the case it was built for.

### Task 1.4 — the Gate-J / BiasCorrection / GateE / GateH per-case WiR tables (mechanical only)

At every firing site with WiR coverage (Baroque carrier): our root ON/OFF vs the WiR root, bucketed by the WiR roman-numeral family. The **musical adjudication of individual samples is Cowork/user work**; this is the mechanical comparison only.

**Gate J** — 124 WiR-covered Baroque sites; ON matches WiR at **59**, OFF at **64**:

| WiR family | sites | dur | ON-matches-WiR | OFF-matches-WiR |
|---|---|---|---|---|
| **V-family** | 52 | 34920 | **33** | 20 |
| viio-family | 1 | 240 | 1 | 0 |
| other (share-tone / cascade) | 71 | 58800 | 25 | **44** |

**★ The mechanical Gate-J finding:** at the sites where WiR actually labels a **dominant (V-family, 52 sites)**, Gate J's re-rooting (ON) is **more often WiR-correct (33 vs 20)** — the rule is doing musically-correct work at its true firing sites. The net root-only *penalty* (ON 59 vs OFF 64 overall) comes entirely from the **71 "other" sites** — WiR labels neither V nor vii° there (e.g. IV6/5, I6): these are dominated by the **rootContinuity cascade footprint** (disabling Gate J at region N−1 shifts region N's continuity context), where OFF happens to match WiR more (44 vs 25). So the Baroque root-only objective penalizes Gate J via its cascade ripple, not via its direct dominant-completion firings — consistent with the 2.2a "root-only objective vs structural rule" tension, now resolved mechanically.

**BiasCorrection** — 57 WiR-covered Baroque sites; ON matches WiR at **25**, OFF at **17** (V-family 11 / viio 4 / other 42). Net ON is more WiR-correct (25 vs 17), even though ON *causes* the 3 class-(b) batch errors (Task 1.1) — a net-good correction with specific class-(b) harm.
**GateE** — 1 WiR-covered site (other): OFF matches WiR, ON does not.
**GateH** — 3 WiR-covered sites (1 V-family, 2 other): neither ON nor OFF matches WiR at any (the rotation lands on a third reading).

### Task 1.5 — DLC generalization probe (validation-only, NC data, shapes no value)

`run_dlc_baseline.py --param-override` (the O-8 override-capable runner) on 3 DLC styles, DEFAULT config, `--limit 12`, current binary, all 3 configs re-run this session (only these 3 re-generated — the ~30 other `results.json` entries are stale prior-run data, excluded). Root-agree deltas vs baseline:

| config | corelli | mozart_piano_sonatas | schumann_kinderszenen |
|---|---|---|---|
| baseline root-agree | 75.18 % | 61.75 % | 76.52 % |
| **inert-7 off** (Δ) | +0.00 | +0.00 | **−0.55** |
| **GateJ off** (Δ) | +0.00 | **−0.10** | **+0.21** |

NC/QA only. Small, mixed deltas: the inert candidates are neutral on corelli/mozart (a −0.55 wobble on schumann under Default config, where one of the inert-set members fires); GateJ-off is roughly neutral (−0.10 mozart / +0.21 schumann) — consistent with the full-corpus Default GateJ +0.0608. No large generalization break; shapes no value (A-3).

---

## Task 2 — the JOINT FIT (candidates only; Baroque carrier, fitting split 261)

Coordinate ascent over the 8-row coupled cluster (`kRootToneFactor` · `kSecondToneFactor` ·
`sameRootInversionBonus` · `bassNoteRootBonus` · `tpcConsistencyBonusPerTone` · `rootContinuityBonus` ·
`kWStepIn` · `kPowerChord3PcPenalty`), 5-point local ladder at the 1b step, 2 rounds + halved-step
refinement on movers, under the §4.2 constraints (referenced to the committed all-on fitting-split
baseline) + the Gate-R search bound `sameRootInversionBonus > kNonBassPenalty (0.35)`. Every eval
ledgered (`tools/fit_ledgers/stage5_jointfit_cfg{I,II,III}.jsonl`). **Fitting-split all-on baseline:
63.5026 %, batch 46** (reproduces the 2.1 fitting baseline).

### Config I — all rules enabled (the conservative fit)

**67 evals, 67 min** (~60 s/eval, under the 4×/STOP). Best feasible vector (3 rows moved):

| row | current | fitted | Δ |
|---|---|---|---|
| **bassNoteRootBonus** | 0.70 | **0.775** | +0.075 |
| **sameRootInversionBonus** | 0.40 | **0.475** | +0.075 |
| **kWStepIn** | 0.10 | **0.125** | +0.025 |
| kRootToneFactor | 1.8 | 1.8 | — |
| kSecondToneFactor | 1.2 | 1.2 | — |
| tpcConsistencyBonusPerTone | 0.2 | 0.2 | — |
| rootContinuityBonus | 0.4 | 0.4 | — |
| kPowerChord3PcPenalty | 0.30 | **0.30** | — (see below) |

**Fitting root 63.5026 → 64.0168 (+0.5142)**, batch 46→41 (fitting subset; fewer), **newB=0, clsB dur
−30960, feasible.** RN 45.21, key 68.32 (both up from ~44.8/68.18).

**★ O-7 resolved — the parked power-chord lever does NOT move at the joint optimum.** In the 2-row smoke
`kPowerChord3PcPenalty` moved down to 0.225 (+0.33 fitting, a region the 2.1 coarse step-0.15 ladder
skipped between its infeasible 0.15 and the up-plateau). But in the full **coupled** fit, at the coupled
point (bassNoteRootBonus 0.775 / kWStepIn 0.125 / sameRootInversionBonus 0.475) its whole ladder
[0.20…0.40] is feasible yet **every point scores below the current 0.30** (evals 58–61) — its apparent
standalone leverage is **subsumed by `bassNoteRootBonus`**, which the joint fit assigns the bass/root-tone
correction to instead. So the O-7 "is the power chord an accepted category" lever is inert at the joint
optimum; `bassNoteRootBonus` is the true lever. (This is exactly the coupling P1 staged the joint fit to
expose.)

**★ Coupling surfaced feasibility that 1-D could not:** `sameRootInversionBonus` alone at 0.45 adds a
class-(b) case (smoke eval 6, infeasible), but at bassNoteRootBonus 0.775 / kWStepIn 0.15 it becomes
feasible to 0.475 — the higher bass-root bonus absorbs the class-(b) case the inversion bonus would
otherwise create. The Gate-R bound held throughout (0.30/0.35 rejected on every `sameRootInversionBonus`
ladder).

### Config II — the cross-carrier-inert-5 disabled ({GateA, GateF, GateGB, GateGC, GateK})

**Config membership (Task 1.1 refinement, stated):** the 2.2a fitting-split inert-7 loses **GateGD**
(1 Baroque full-corpus firing site — inert on the fitting split, live on held-out) and **GateL** (18 Jazz
sites, load-bearing there) per "a rule live elsewhere drops out of the disabled set." Config II disables
the **5 cross-carrier-fully-inert** rules.

**Result: Config II ≡ Config I, exactly.** Same best vector (bassNoteRootBonus 0.775 / sameRootInversionBonus
0.475 / kWStepIn 0.125), same **best_root 64.0168 (+0.5142)**, batch 41, clsB −30960, feasible; config
baseline root 63.5026 (identical to all-on). The eval-by-eval trajectory matched Config I (e.g. eval 52 root
63.5388 on both). **This is the confirming result:** disabling the inert-5 leaves the Baroque fitting
landscape byte-transparent — the fit reaches the **identical** optimum with them off, and the dissolution
is not reproducible-vs-not-reproducible: it is a **no-op** on the objective. Direct evidence the inert-5 are
safely retirable. **Dissolution IS reproducible by these weights (trivially — the rules contribute nothing).**

### Config III — Config II + the 4 disable-beneficial ({+BiasCorrection, GateE, GateH, GateJ}) — the maximal-dissolution candidate

Run LAST, gated on Config II being healthy (it was: feasible +0.5142). Disables 9 rules. Config baseline
root 63.572 (+0.0693 — the dissolution alone lifts the Baroque root-only objective, driven by GateJ-off).

**Best feasible vector (Baroque fitting split):** bassNoteRootBonus 0.70→**0.725**, kPowerChord3PcPenalty
0.30→**0.25**, all others unchanged (sameRootInversionBonus **stuck at 0.40** — could not move up).
**Best root 63.8912 (+0.3886)**, batch 43, clsB −20520, feasible.

**★ Maximal dissolution is WORSE than the conservative fit** (+0.3886 vs Config I/II's +0.5142) — despite a
higher starting baseline. Two mechanisms: (1) disabling **BiasCorrection** removes the bass-root deduction
correction, which flips how the bass/root levers couple — `bassNoteRootBonus` now oscillates and only
reaches 0.725, and the class-(b) headroom that let `sameRootInversionBonus` reach 0.475 in Config I/II
**closes** (it stays pinned at 0.40); (2) with the corrections gone, `kPowerChord3PcPenalty` re-enters as a
mover (down to 0.25) but cannot recover the lost headroom. So the dissolution does not "free" the fit — it
**removes coupling structure the weight fit was exploiting**. **This is the honest maximal-dissolution
result: dissolution IS reproducible-and-feasible on the Baroque fitting split, but it is NOT beneficial —
it costs objective headroom** (and, per Task 1.1, the GateJ-off it contains is catastrophic on Jazz — shown
in the Config III surface, §3.1).

### Cost / determinism
Config I 67 evals/67 min · Config II 67 evals/~66 min (Config-I trajectory) · Config III ~67 evals/~66 min
= **~200 evals, ~3.3 h total fit time** (well under the ~6 h cap; every eval ~60 s, under the 4×/STOP).
Deterministic (fixed row order, tie-break toward current, cached). Every eval ledgered
(`stage5_jointfit_cfg{I,II,III}.jsonl`, committed).

**Config-comparison verdict:** the **conservative fit (Config I ≡ Config II) is the candidate** — the same
vector whether or not the inert-5 are dissolved (they contribute nothing), with the largest feasible fitting
gain (+0.5142). Config III (maximal dissolution) is a measured **negative result**: dissolving the
load-bearing/beneficial-4 costs objective headroom on Baroque and (surface §3.1) breaks Jazz.

## Task 3 — the decision surface + PREPARED per-rule verdict proposals

### 3.1 Per-config decision surfaces

**Adoption model (per-preset scope — the correction that matters).** Of the 8 cluster rows, only
`sameRootInversionBonus` is **per-preset** (G3); the rest are **shared**. On adoption the shared params
change on **every** preset; the per-preset `sameRootInversionBonus` changes only on the **adopt targets**
(Baroque = fit target, Default = D-4 adopt-with-Baroque) — **not** Jazz (A-3). The Jazz surface therefore
keeps `sameRootInversionBonus` at Jazz's own default (0.15). (An initial surface run that wrongly forced the
fitted 0.475 onto Jazz overstated the Jazz batch regression as +6 class-(b); corrected below.)

**Config I ≡ Config II candidate** (bassNoteRootBonus **0.775**, sameRootInversionBonus **0.475** [Baroque/
Default only], kWStepIn **0.125**; kPowerChord3PcPenalty 0.30):

| split / carrier | base → cand root | Δroot | RN Δ | key Δ | batch | batch +/−/~ | newB | clsB dur Δ |
|---|---|---|---|---|---|---|---|---|
| **fitting (261)** | 63.5026→64.0168 | **+0.5142** | — | — | 46→41 | — | 0 | −30960 |
| **held-out (65)** | 62.6364→63.2238 | **+0.5874** | — | — | — | — | — | — |
| **Baroque full** | 63.3234→63.8527 | **+0.5293** | +0.386 | +0.061 | 53→49 | +3/−7/~0 | **1** | −41040 |
| **Jazz full** | 62.3664→61.7593 | **−0.6070** | −0.390 | −0.059 | 24→22 | +0/−2/~0 | **0** | **+23120** |
| **Default full** | 63.2192→63.7254 | **+0.5062** | +0.357 | +0.070 | 53→50 | +3/−6/~0 | **1** | −39120 |

- **★ NO overfit — the opposite of the 2.1 candidate.** Held-out **+0.5874 > fitting +0.5142** — the fit
  *generalizes*. (2.1's single-lever fit regressed held-out −0.098; this coupled fit does not.)
- **★ Two adoption blockers, one cause.** Baroque + Default each add the **held-out class-(b) case
  `bwv392@17520`** (bwv392 is a held-out score — the §4.2 held-out exception: the fitting constraint
  newB=0 was satisfied on the 261, the class-(b) surfaces only at the full-corpus adoption check). Under
  R10 (the batch case-identity hard stop) a **new class-(b) case blocks adoption.** And **Jazz root duration
  regresses −0.6070** (clsB dur +23120) from the *shared* bassNoteRootBonus/kWStepIn bumps — though it adds
  **no new Jazz batch case** (newB=0, batch 24→22), so the Jazz *batch hard-stop* is not tripped, only the
  reported duration metric. **Both blockers trace to the aggressive shared `bassNoteRootBonus 0.775`**
  (Config III at 0.725 has neither — see below).
- **D-4 Default: INELIGIBLE** (newB=1, the `bwv392@17520` held-out class-(b)). **Jazz: batch-safe but
  duration-regressed** (the shared-scope cost).
- The 2 new class-(a) cases (bwv437@25440, bwv64.8@20640) are **fitting** scores — symmetric-rotation churn
  the two-tier policy permits (not batch hard-stops).
- **Snapshot preview** (`--preset Default --dump-regions notation`, candidate vs baseline, 11 scores):
  **11/11 DIFFER** → at adoption **all 11 P1–P4 goldens would refresh** (the broad bassNoteRootBonus/kWStepIn
  moves touch the whole notation pipeline — far more than 2.1's 6/11).
- **DLC probe on the candidate** (Task-1.5 machinery, `--param-override` the full vector, DEFAULT config):
  corelli **75.18→76.55 (+1.37)**, mozart_piano_sonatas **61.75→62.29 (+0.54)**, schumann_kinderszenen
  **76.52→76.67 (+0.15)** — the candidate **improves all three DLC styles**, corroborating the held-out
  generalization (+0.59). The Baroque gain generalizes to out-of-corpus common-practice/romantic styles (NC
  data, but a consistent positive signal). `tools/fit_ledgers/stage5_dlc_probe_candidate` (regenerable scratch).

**Config III candidate** (bassNoteRootBonus **0.725**, kPowerChord3PcPenalty **0.25**; the 9-rule dissolution):

| split / carrier | base → cand root | Δroot | batch | newB | clsB dur Δ |
|---|---|---|---|---|---|
| fitting (261) | 63.5026→63.8912 | +0.3886 | 46→43 | 0 | −20520 |
| held-out (65) | 62.6364→63.0699 | **+0.4336** | — | — | — |
| **Baroque full** | 63.3234→63.7213 | **+0.3979** | 53→50 | **0** | −29400 |
| **Jazz full** | 62.3664→62.3215 | **−0.0449** | 24→22 | **0** | +5640 |
| **Default full** | 63.2192→63.5998 | **+0.3805** | 53→51 | **0** | −28440 |

**★ The crux trade — the maximal-dissolution candidate is the SAFER one.** Config III has a **smaller** Baroque
gain (+0.3979 vs +0.5293) **but newB=0 on ALL three carriers** (no R10 trip anywhere), **D-4 Default ELIGIBLE**,
and **Jazz nearly flat (−0.045)**. Its gentler shared `bassNoteRootBonus 0.725` avoids the `bwv392@17520`
held-out class-(b) *and* the Jazz duration hit. **Caveat:** Config III's Jazz-safety is partly coincidental
weight-compensation of the GateJ-off penalty (Task 1.1 GateJ-off-alone Jazz = −0.4515; here the shared bumps +
BiasCorrection-off's −2 Jazz class-(b) roughly cancel it), and its RN still slips on Jazz (−0.094). It is **not**
a reason to dissolve GateJ (retain — §3.2); it shows the dissolution does not by itself break the batch stop.

**Neither candidate is cleanly adoptable as-is:** Config I trips R10 on a held-out case + costs Jazz duration;
Config III requires the GateJ dissolution §3.2 recommends against. The clean adoptable point (surfaced, not
built — a design refinement) is **Config I's rule set (all on) with a gentler shared `bassNoteRootBonus`
(~0.725) and/or `bassNoteRootBonus` made per-preset** so the Baroque gain does not force a Jazz cost — i.e. the
shared-scope tension §4.2 flags. **This is a candidate dispatch; the adoption decision is the user's.**

### 3.2 PREPARED per-rule VERDICT PROPOSALS (D-7) — proposals only; the user rules on each

*(draft, evidence-cited; finalized after the surfaces)*

**RETIRE candidates (5) — inert on ALL THREE carriers (Task 1.1/1.2):** GateA, GateF, GateGB, GateGC, GateK.
0 firing sites B/J/D, Δroot=0, batch unchanged, zero class movement. Gate K's founding case `bwv40.6` is
**no longer touched** by the rule (superseded upstream, Task 1.3). Config II disables all 5 and stays
feasible — removal reproduces the corpus behavior. Fixture disposition: their pinned `postscoringgates_tests`
fixtures are **synthetic** constructions exercising code paths that fire on **zero** corpus cells; retirement
vacates them. **Proposal: RETIRE (per rule, user-ratified).**

**RETAIN-AS-STRUCTURAL (4) — load-bearing (Task 1.1):**
- **GateI** — disabling adds **+5 class-(b) batch cases on Jazz** (bwv286/355/386/388/428) + clsB up on all
  three carriers; the continuous fit does not reproduce its first-inversion-Major-over-root-Minor correction.
- **FM2** — disabling adds the class-(b) case `bwv227.7@18000` (Baroque).
- **GateJ** — disabling is **catastrophic on Jazz (−0.4515 root, clsB +36480)**; the Task-1.4 per-case table
  shows at the **V-family firing sites (52) Gate-J ON is more WiR-correct (33 vs 20)** — right at its true
  firings; the Baroque root-only "+0.0752 when off" is the **rootContinuity cascade** on the 71 "other" sites,
  not evidence the rule is wrong. The rule the roadmap expects to survive longest — confirmed structural.
- **GateL** — inert on Baroque (founding cases superseded) but load-bearing on **Jazz** (18 sites, clsB+960
  when off); retirement is global, so retain.

**DEFER (5) — small/mixed/class-(a) effects; per-case verification needed (blocking interaction named):**
- **BiasCorrection** — net WiR-good (Task 1.4: ON matches 25 vs OFF 17 on 57 sites) but **causes 3 class-(b)
  batch errors** (bwv60.5 Baroque; bwv301, bwv74.8 Jazz). Blocking interaction: net-good vs class-(b) harm;
  the Config-III refit is the test of whether continuous weights reproduce the good without the harm.
- **GateE** — Baroque-only, 2 sites, disable-beneficial; its 1 WiR-covered firing is WiR-wrong (OFF matches).
  Blocking interaction: a documented founding case (F♯m→D/F♯) not observed at the current firing — per-case
  verification needed.
- **GateH** — Baroque-only, 3 sites; at all 3 WiR-covered sites **neither ON nor OFF matches WiR** — the
  augmented-rotation **class-(a)** coin-flip zone a continuous weight cannot resolve. Defer to the
  spelling-aware gate (Stage 5/6).
- **GateGD** — Baroque-only, 1 held-out site, disable-beneficial; dropped from Config II. Tiny; per-case.
- **GateGE** — Baroque-only, 9 sites, the **class-b→class-a reshuffle** (clsB−1920, clsA+1440) — symmetric-
  rotation churn; defer to the spelling-aware gate.

**No coupled/STOP class — all 14 clean (2.2a confirmed).**

**Verdict-proposal summary (14 rules):** **RETIRE (5):** GateA, GateF, GateGB, GateGC, GateK ·
**RETAIN-AS-STRUCTURAL (4):** GateI, FM2, GateJ, GateL · **DEFER (5):** BiasCorrection, GateE, GateH, GateGD,
GateGE. **The joint fit corroborates the retire-5:** Config II (those 5 off) reached the *identical* optimum
as Config I — they contribute nothing. **And corroborates GateJ = retain:** the maximal-dissolution Config
III (GateJ off) is *worse* on the objective (+0.3886 vs +0.5142) and its Jazz-safety is coincidental
weight-compensation, not a reproduction of GateJ's structural correction.

### 3.3 Prepared-not-applied artifacts (described; nothing applied)

**Adoption artifact — Config I/II candidate** (the revertible commit a *separate, user-ratified* adoption
event would apply — NOT in this dispatch):
1. `chordanalyzer.cpp` — `bassNoteRootBonus` 0.70→0.775 (ChordAnalyzerPreferences default, shared);
   `kWStepIn` 0.10→0.125 (harmonicfunctionlayer.h, shared); `sameRootInversionBonus` Baroque 0.4→0.475 +
   Default 0.4→0.475 (per-preset, Jazz unchanged at 0.15) in `batch_analyze.cpp`/preset wiring.
2. `tools/param_manifest.json` — the four rows' `value` + `license_provenance` (§7 fitted-on statement).
3. `docs/scoring_model.md` — the §4 bonus values synced.
4. Rebuild (5 binaries) + `pipeline_snapshot_tests.exe --update-goldens` (**≈11/11 refresh**, §3.1) after
   confirming the delta is the intended fit effect.
5. **BLOCKED by the surface as-is:** the held-out class-(b) `bwv392@17520` (R10) + the Jazz duration cost —
   so this artifact is **prepared but NOT recommended without** either a gentler shared `bassNoteRootBonus`
   or making it per-preset (the surfaced design refinement).

**Per-rule retirement commit shapes (RETIRE-5, each its own user-ratified commit):** for each of GateA/GateF/
GateGB/GateGC/GateK — delete the rule's block in `postscoringgates.cpp`, remove its `PostScoringRule` enum
member + `ruleOff` guard, vacate its synthetic `postscoringgates_tests.cpp` fixtures (they exercise a
never-firing corpus path), and `docs/scoring_model.md` §6 sync. Each carries its differential (0 corpus
cells, Config II ≡ Config I evidence). **NOT applied — each retirement is the user's per-rule ratification.**

## Task 4 — sandwich + suites + fold

### 4.1 Sandwich (end-of-run acceptance)
- **`characterise_bir_false.py` ×3 on the REAL per-preset dirs:** Baroque **53** / Jazz **24** / Default
  **53**. **`tools/corpus/` byte-untouched** (`git status` = 0 dirty; manifest `git_hash 0dd64660f4` on all
  three) — byte-identity ⟹ the stem@tick case-identity sets are **identical to CLAUDE.md, set-diff empty both
  directions**. Every regen (evidence sweep, joint fit ×3, surfaces, DLC, snapshot preview) went to scratch
  (`C:/tmp/…`); the frozen corpus was never written.

### 4.2 Suites
No `src/` change this dispatch (measurement-only; the 11:10 2.2a mechanism binary, honoring `disable_rule`,
was reused). **composing 1116 / notation 53 / snapshots 11, 0 FAILED, no golden refresh** — the pinned P1–P4
goldens all match (the snapshot preview's 11/11 diff is candidate-vs-baseline, NOT applied). Matches the
2.2a end-state exactly.

### 4.3 Reuse-vs-new + what retires
- **Reuses (verbatim):** `run_bach_preset.py` regen + `--param-override`, `a8_rebaseline_measure.py`
  (`--corpus-root`/`--preset`/`--scores`), `characterise_bir_false.py`, `compare_rn`/`compare_analyses`/
  `dcml_parser` primitives, `run_dlc_baseline.py --param-override` (O-8), the frozen corpus,
  `stage5_split_registry.json` (261/65), `stage5_fit_driver` (`evaluate`/`regen`/`measure`), the
  `batch_analyze --param-override`/`disable_rule` mechanism — all Phase-1/2.1/2.2a landings, unmodified.
- **New (committed):** the measurement drivers `stage5_2_2b_evidence.py` (cross-carrier disable + firing-site
  diff), `stage5_2_2b_jointfit.py` (joint coordinate-ascent), `stage5_2_2b_surface.py` (decision surface),
  `stage5_2_2b_dlc_probe.py`, `stage5_2_2b_snapshot_preview.py`, `stage5_2_2b_analyze.py`; the committed
  ledgers `stage5_rule_disable_fullcorpus.jsonl`, `stage5_rule_firing_sites.jsonl` (968 rows),
  `stage5_dlc_probe.jsonl`, `stage5_jointfit_cfg{I,II,III}.jsonl`, `stage5_surface_cfg{I,III}.jsonl` under
  `tools/fit_ledgers/`. The committed driver `stage5_fit_driver.py` was **not** modified (the joint fit is a
  separate orchestrator reusing its `evaluate`).
- **Retires: NOTHING.** This dispatch produces the *evidence + candidates + verdict PROPOSALS*; each retirement
  and each adoption is its own user-ratified commit (D-7).

### 4.4 Fold
`docs(cowork):` — STATUS.md (22p CC-delivery entry) · COWORK_HANDOFF.md · `cowork_stage5_fitter_design.md`
(O-7 joint-fit-result marker) · `cowork_style_taxonomy_proposal.md` (the §6/§6a Cowork record, carried) ·
`cc_instruction_stage5_phase2_2b.md` (force-add).

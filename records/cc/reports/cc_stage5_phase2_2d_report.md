# CC report — Stage-5 Phase 2.2d: the (sameRootInversionBonus, kWStepIn) sub-sweep — is there a feasible slice of the family-2 gain?

**Dispatch:** `cc_instruction_stage5_phase2_2d.md` (Cowork, 2026-07-05) · **HEAD at dispatch:** `64a019511f` · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** the seventh CC increment of the Stage-5 arc. Measurement + candidate surface ONLY — no adoption, no committed value change, no `tools/corpus/` write, no push. Premise (O-11 ii / `cc_stage5_phase2_2c_report.md` Task 4): the coupled family-2 candidate is blocked at every swept `bassNoteRootBonus`, and BOTH blockers are driven by the FIXED `sameRootInversionBonus 0.475 + kWStepIn 0.125` bump (`bwv379@11520` at the fitting split; `bwv392@17520` at the full corpus). This dispatch asks the one remaining cheap question: **does a SMALLER (srib, kw) bump exist that keeps a real gain and blocks NOTHING?**

---

## Commit SHAs (this dispatch)

| # | SHA | Type | Contents |
|---|---|---|---|
| 1 — driver + ledger | `ee59231141` | `feat(tools):` | `tools/stage5_2_2d_sweep.py` (the 2-D sub-sweep) + committed trade-surface ledger `tools/fit_ledgers/stage5_2_2d_sweep.jsonl` |
| — this report | *(this commit)* | `docs(cowork):` | `cc_stage5_phase2_2d_report.md` (force-add) |
| — the fold | *(next commit)* | `docs(cowork):` | STATUS 22s · COWORK_HANDOFF · design (O-11 record) · `cc_instruction_stage5_phase2_2d.md` (force-add) |

---

## Task 0 — state check

HEAD `64a019511f` (the 2.2c fold), branch `master`, fork-only. Dirty set matched the dispatch expectation exactly: the Cowork fold files (`STATUS.md` · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`) + `cowork_candidate_lever_register.md` + known scratch (`idiom_discovery/*`, `scratch_artifacts/`). Corpus `tools/corpus/{baroque,jazz,default}` each 352 `.ours.json`; manifest `git_hash 0dd64660f4` on all three (byte-identical to the RETIRE-4 binary output, per 2.2c). Binary `ninja_build_rel/batch_analyze.exe` = the RETIRE-4 build (Jul 5 19:48). **No STOP at Task 0.**

**Plumbing self-check (smoke, before the grid):** the frozen-corpus baselines reproduced exactly (fitting Baroque **63.5026**/batch 46, full Baroque **63.3234**/batch 53, full Default **63.2192**/batch 53); the grid corner `(srib 0.40, kw 0.10, bnrb 0.70)` — the current values — regenerated **byte-identical** (fitting gain +0.000000, full batch 53, zero new class-(b)), and a bumped point moved (fitting +0.047 at `(0.4625, 0.125)`) — confirming the `--param-override` reaches all three levers and the corner is the true baseline anchor.

## Task 1 — the 2-D sub-sweep (Baroque carrier; fitting split first)

**Anchor (verified on disk).** `sameRootInversionBonus` Baroque/Default struct default **0.40** (Jazz 0.15); `kWStepIn` global initializer **0.10**; `bassNoteRootBonus` **0.70** (all carriers). The O-9 per-carrier delivery (2.2c `6a468f82ac`) writes each per preset in `tools/batch_analyze.cpp` BEFORE the `--param-override` load, so the sweep's override cleanly overrides Baroque/Default while **Jazz is pinned = byte-identical by construction** (no Jazz override written).

**Grid (18 points; `bassNoteRootBonus` fixed 0.70 everywhere):**
`sameRootInversionBonus ∈ {0.40, 0.4125, 0.425, 0.4375, 0.45, 0.4625}` × `kWStepIn ∈ {0.10, 0.1125, 0.125}`. The ratified Gate-R search bound `srib > kNonBassPenalty (0.35)` holds across the whole grid. `bassNoteRootBonus` movement is family-2-closed (2.2c) and NOT swept.

**Denominators (§2.1a — every rate names its denominator).** `fit_root` = variant-(b) DCML-only duration-weighted root-agreement over the **fitting split's 261 WiR-covered, parseable cells**; `fit_gain` vs the committed all-on fitting baseline **63.5026 %**. `bar_full_root`/`def_full_root` = the same objective over the **full 326/352 WiR-covered corpus**; batch counts are the CLAUDE.md `characterise_bir_false.py` case-identity gate (Baroque/Default base **53**). `fit_batch` = the fitting-subset batch count (base **46**). Class-(b) duration on the fitting split's covered cells; class-(a) tracked beside.

**★ The 18-point surface** (`tools/stage5_2_2d_sweep.py`; committed ledger `tools/fit_ledgers/stage5_2_2d_sweep.jsonl`; every eval regen→scratch, frozen corpus read-only). `fit_gain` vs fitting baseline 63.5026; `barB`/`defB` = full-corpus batch count (base 53); `newB` = new class-(b) cases vs the frozen 53/24/53. Full-corpus (Baroque+Default) evaluated only for fitting-feasible points with gain>0 (Task-1.2 cost bound; "—" = not evaluated). **Jazz byte-identical by construction** (srib per-preset → Baroque/Default only; kw O-9 per-carrier → Jazz keeps 0.10; bnrb unchanged) → +0 on every point.

| srib | kw | fit root | fit gain | fit-feas | Baroque full batch | Baroque newB | Default full batch | Default newB | **full-feas** |
|---|---|---|---|---|---|---|---|---|---|
| **0.40** | **0.10** | 63.5026 | +0.0000 | ✓ | 53 | 0 | — | — | *(anchor: byte-identical)* |
| 0.40 | 0.1125 | 63.5172 | +0.0146 | ✓ | **52** | 0 | 52 | 0 | **✓** |
| **0.40** | **0.125** | 63.5391 | **+0.0365** | ✓ | **52** | 0 | 52 | 0 | **✓ (tie-top)** |
| 0.4125 | 0.10 | 63.5026 | +0.0000 | ✗ | 52 | 1 (bwv392) | — | — | — |
| 0.4125 | 0.1125 | 63.5099 | +0.0073 | ✗ | 50 | 0 | — | — | — |
| 0.4125 | 0.125 | 63.5136 | +0.0109 | ✗ | 50 | 0 | — | — | — |
| 0.425 | 0.10 | 63.5355 | +0.0328 | ✗ | 53 | 2 (bwv379,bwv392) | — | — | — |
| 0.425 | 0.1125 | 63.5428 | +0.0401 | ✓ | 51 | 1 (bwv392) | 51 | 1 (bwv392) | ✗ |
| **0.425** | **0.125** | 63.5391 | **+0.0365** | ✓ | **50** | 0 | 50 | 0 | **✓ (tie-top)** |
| 0.4375 | 0.10 | 63.5318 | +0.0292 | ✗ | 54 | 2 (bwv379,bwv392) | — | — | — |
| 0.4375 | 0.1125 | 63.5391 | +0.0365 | ✗ | 53 | 2 (bwv379,bwv392) | — | — | — |
| 0.4375 | 0.125 | 63.5355 | +0.0328 | ✓ | 52 | 1 (bwv392) | 52 | 1 (bwv392) | ✗ |
| 0.45 | 0.10 | 63.5315 | +0.0288 | ✗ | 55 | 2 (bwv379,bwv392) | — | — | — |
| 0.45 | 0.1125 | 63.5388 | +0.0361 | ✗ | 54 | 2 (bwv379,bwv392) | — | — | — |
| 0.45 | 0.125 | 63.5351 | +0.0325 | ✗ | 54 | 2 (bwv379,bwv392) | — | — | — |
| 0.4625 | 0.10 | 63.5388 | +0.0361 | ✗ | 57 | 3 (bwv245.22,bwv379,bwv392) | — | — | — |
| 0.4625 | 0.1125 | 63.5461 | +0.0434 | ✗ | 54 | 2 (bwv379,bwv392) | — | — | — |
| 0.4625 | 0.125 | 63.5497 | +0.0471 | ✗ | 54 | 2 (bwv379,bwv392) | — | — | — |

**Feasible slice EXISTS** (contra the 2.2c family-2 closure at the coupled `bnrb 0.775` point) — **three full-feasible points**, all at `kw` on the high edge:
- **(0.40, 0.1125)** — kw-only, +0.0146, batch 53→52 both carriers, clean. *(dominated: same srib, less gain than (0.40, 0.125), same batch)*
- **(0.40, 0.125)** — kw-only (srib at its 0.40 default), **+0.0365**, batch 53→**52** both carriers, clean.
- **(0.425, 0.125)** — both levers, **+0.0365**, batch 53→**50** both carriers, clean.

**The top fitting gain (+0.0365) is a 2-point TIE** (identical fit_root 63.5391 to 4 dp): **(0.40, 0.125)** and **(0.425, 0.125)**. The driver's `max()` tie-break is iteration order → it reports (0.40, 0.125); the two differ only on the full-corpus footprint (below). The selection rule is fitting-gain-only, so the tie-break is a genuine user call — surfaced in Task 2.

**Tracked-case appearance map** (the two 2.2c blockers, mapped across the grid):
- **`bwv379@11520`** (the fitting blocker) appears at: kw=0.10 → srib∈{0.425, 0.4375, 0.45, 0.4625}; kw=0.1125 → srib∈{0.4375, 0.45, 0.4625}; kw=0.125 → srib∈{0.45, 0.4625}. **Higher kw absorbs it up to a higher srib** — the fitting-feasible frontier (bwv379 absent) rises with kw: srib≤0.40 at kw=0.10, srib≤0.425 at kw=0.1125, srib≤0.4375 at kw=0.125. It never appears in the srib=0.40 column. Its first appearance bounds the fitting-feasible region exactly as the ledger's `fit_feasible` column records.
- **`bwv392@17520`** (the full-corpus blocker) appears across the srib≥0.4125 block (all kw), and is **ABSENT from the entire srib=0.40 column AND from (0.425, 0.125)**. The (0.425, 0.125) exemption is the coupling in action: at srib=0.425, kw=0.1125 has bwv392 but kw=0.125 does NOT — the higher kw absorbs it (mirror of the 2.2b/2.2c bnrb-absorbs-bwv379 coupling, now srib×kw). It never appears in the gentle srib=0.40 column at all.

**Why the srib=0.40 column is clean:** with srib at its default (no inversion-bonus bump), the gain comes purely from `kw` (the stepwise-bass step-in bonus), which does not re-segment the bwv392 region — so no bwv392 at any kw in {0.10, 0.1125, 0.125}. The bwv392 over-grab (the Task-3-verified `Dm/F` iii6 across the WiR `Gm` vi boundary, 2.2c) is driven by the **srib** bump specifically, and is re-absorbed only at the (0.425, 0.125) corner.

**Both §4.2 fitting constraints are active and distinguishable** (not just the no-new-case one): the **srib=0.4125 column is fitting-infeasible on the class-(b) DURATION-non-increase constraint alone** (`fit_clsb_dur_delta` = +960/+480/+240, `fit_new_class_b`=[] — a class-(b) case's disagreement lengthens without crossing the batch case-identity threshold), whereas srib≥0.45 fails on **both** (new `bwv379` *and* +duration). The two tie-top feasible points reduce fitting class-(b) duration by −2400 (0.40,0.125) and −1440 (0.425,0.125). This is the tie's dual-metric character (Task 2): **(0.40,0.125) reduces fitting class-(b) duration more (−2400 vs −1440); (0.425,0.125) reduces the full-corpus batch case-count more (53→50 vs 53→52)** — they tie exactly on the governing fitting-root objective.

## Task 2 — selection + the decision surface

**★ Outcome: a feasible slice EXISTS — the S-3 loop selects a candidate (this is NOT a closure).** The selection rule (highest fitting-split gain whose full-corpus checks add ZERO new class-(b) on any carrier) yields a **top-gain 2-point TIE at +0.0365**: **(srib 0.40, kw 0.125)** and **(srib 0.425, kw 0.125)**. Both pass on every carrier. The full decision surface for **both** tied points (`tools/stage5_2_2d_surface.py`; committed ledger `tools/fit_ledgers/stage5_2_2d_surface.jsonl`; held-out scored ONCE per point; frozen corpus read-only):

| axis (denominator) | (0.40, 0.125) — kw-only | (0.425, 0.125) — srib+kw |
|---|---|---|
| **fitting (261)** root | 63.5026→63.5391 **+0.0365** | 63.5026→63.5391 **+0.0365** |
| **held-out (65)** root | 62.6364→62.6643 **+0.0280** | 62.6364→62.6643 **+0.0280** *(no overfit; held-out < fitting but positive)* |
| **Baroque full** root / RN / key | +0.0347 / +0.0145 / +0.0116 | +0.0347 / **+0.0492 / +0.0319** |
| **Baroque batch** (base 53) | 53→**52** (+0/−1/~0) | 53→**50** (+0/−3/~0) |
| Baroque removed (class) | `bwv244.32@5760` **(b)** | `bwv244.32@5760` **(b)**, `bwv258@10560` **(a)**, `bwv334@6720` **(a)** |
| Baroque clsB / clsA dur Δ | −2400 / −480 | −1920 / −960 |
| **Default full** root / RN / key | +0.0347 / +0.0087 / −0.0058 | **+0.0376** / +0.0492 / +0.0029 |
| **Default batch** (base 53) | 53→**52**, newB=0 | 53→**50**, newB=0 |
| **D-4 Default eligible** | **✓** (root>0, no new class-(b), clsB non-increase) | **✓** |
| **Jazz** | **byte-identical** (spot-verified: no-override regen == frozen, batch 24, cases match) | **byte-identical** (same) |
| new class-(b), any carrier | **0** | **0** |
| **DLC** probe Δ (NC data; corelli/mozart/schumann) | −0.15 / **+0.69** / 0.00 | −0.15 / **+0.78** / −0.07 |
| **Snapshot** goldens differ | **11/11** | **11/11** |

**★ The decisive finding — the tie's *meaningful* improvement is IDENTICAL; the batch gap is class-(a) churn.** Both candidates remove **exactly the same single class-(b) case** (`bwv244.32@5760`) and add **zero** new class-(b) on every carrier. The full-corpus batch gap (52 vs 50) is **entirely class-(a)**: (0.425, 0.125) additionally removes `bwv258@10560` and `bwv334@6720`, both **class-(a)** (symmetric-rotation churn per the two-tier policy — coin-flips, not quality wins; a net class-(a) −2 with zero additions, within the "small, every-case-verified" tolerance). So on the metric the R10 gate actually protects (**class-(b) case-identity**), the two candidates are **equal** — each delivers the same −1/+0. The naive "53→50 beats 53→52" reading is misleading; the class-decomposition is the honest lens.

**The tie's true trade (a genuine user ratification call):**
- **(0.40, 0.125) — minimal / robust.** kw-only (srib stays at its 0.40 default). Achieves the full class-(b) win with the smallest perturbation, touches **one** lever, and **never enters the `bwv392` over-grab region** (bwv392 is absent from the entire srib=0.40 column — the srib bump is what creates it). Reduces fitting class-(b) *duration* more (−2400). This is the driver's own `max()` selection (tie broken toward the first-encountered = lower srib) and the "minimal conservative change" tie-break the fit optimizer uses.
- **(0.425, 0.125) — better tracked-beside RN/key.** RN +0.0492 / key +0.0319 (vs +0.0145 / +0.0116) and a marginally higher Default root (+0.0376). Cost: a second lever moves, it removes 2 class-(a) coin-flips (churn, not a win), and it **only avoids `bwv392` via the fragile kw=0.125 absorption** (at (0.425, 0.1125) bwv392 trips) — a coupling dependence the kw-only point does not have.

**★ Recommendation (CC, evidence-based; the ratification is the user's): (0.40, 0.125).** It secures the identical class-(b) improvement with a minimal, robust, single-lever change that does not rely on the srib→bwv392 absorption coupling. (0.425, 0.125) is the alternative **iff** the better tracked-beside RN/key (+0.049/+0.032, surfaced per §4.2 "never collapsed in") is judged worth the larger perturbation + the class-(a) churn + the coupling dependence. Both are R10-safe on all three carriers and D-4 Default-eligible; neither is adopted here.

**★ vs the 2.2b/2.2c Config-I candidate (the arc's contrast).** The 2.2b joint fit's best (bnrb 0.775 / srib 0.475 / kw 0.125) gave a large fitting gain (+0.5142) but tripped the class-(b) `bwv392@17520` on Baroque+Default (R10 stop) **and** cost Jazz −0.607 duration. The 2.2d sub-sweep trades that away: a **~14× smaller** fitting gain (+0.0365 vs +0.5142) that is **fully adoptable** — zero new class-(b) anywhere, a real class-(b) fix (`bwv244.32@5760`), Jazz **byte-identical** (the O-9 per-carrier delivery removes the shared-scope Jazz cost entirely), held-out-positive, DLC-positive. The family-2 gain was not "no feasible slice" (the pessimistic 2.2c reading of the coupled point) — it was **a much smaller feasible slice reachable only with bnrb held at 0.70 and the bump kept gentle**, exactly the cheap question this dispatch was dispatched to answer.

### Prepared-not-applied adoption artifact (described; NOTHING applied)

The revertible commit a *separate, user-ratified* adoption event would apply (NOT this dispatch), for the recommended **(srib 0.40, kw 0.125)** — the **(0.425, 0.125)** variant adds the bracketed srib deltas:

1. **`tools/batch_analyze.cpp`** (O-9 per-carrier delivery, already the delivery surface since 2.2c `6a468f82ac`): set `presetKWStepIn = 0.125` in the **Baroque + Default** branches (Jazz stays 0.10 → byte-identical). `[variant (0.425,0.125): also `chordPrefs.sameRootInversionBonus = 0.425` in the Baroque + Default branches.]` No shared-struct change — the batch/fitting carriers are covered here.
2. **Production/notation path (O-11 iii — the delivery caveat):** production has no preset-selection moment; it delivers ONLY the Default carrier via the **global initializer** `kWStepIn = 0.10` (`harmonicfunctionlayer.h`). To ship kw=0.125 to production, the initializer changes 0.10→0.125, which **recomputes `kStepBudget`** (`= kWStepIn + kWStepOut + 0.01` → 0.125+0.10+0.01 = **0.235**, up from 0.21). **★ kStepBudget note (O-11/2.2c Task 2):** the `--param-override` loader recomputes kStepBudget automatically at fit time (so every sweep/surface eval above used 0.235 correctly); a **baked** initializer adoption must ensure the same recompute (the static-init references kWStepIn in the same TU, but the adoption must verify 0.235 is delivered and audit any site assuming the 0.21 constant). `[variant: Default srib ships to production via the `sameRootInversionBonus` struct default (`analysistypes.h`); changing it 0.40→0.425 also moves the Standard/Modal/Contemporary carriers, a scope the adoption event must rule on.]`
3. **`tools/param_manifest.json`** — the `kWStepIn` row `value` 0.10→0.125 + `license_provenance` (§7 fitted-on statement; `[variant: + `sameRootInversionBonus` per-preset Baroque/Default 0.40→0.425]`).
4. **`docs/scoring_model.md`** — §4/§6 bonus values synced.
5. **Rebuild** (5 binaries) + **`pipeline_snapshot_tests.exe --update-goldens`** (**11/11 refresh**, measured) after confirming the delta is the intended fit effect.
6. **R10 re-baseline:** Baroque + Default batch **53→52** (remove `bwv244.32@5760` from both identity sets); `[variant: 53→50, also remove the two class-(a) `bwv258@10560`, `bwv334@6720`]`; Jazz unchanged (24). CLAUDE.md identity sets updated in the adoption commit.

**Not applied — this is a candidate + prepared artifact; the adoption (and the tie-break) is the user's ratification event.**

## Task 3 — sandwich + suites + reuse/new

### Sandwich (end-of-run acceptance)
`characterise_bir_false.py` ×3 on the **REAL per-preset dirs**: Baroque **53** / Jazz **24** / Default **53**. The Baroque case-identity set was compared element-wise to the CLAUDE.md ratified 53-set — **0 missing, 0 extra, set-diff empty both directions**. `tools/corpus/` **git-clean** (byte-untouched; manifest `git_hash 0dd64660f4` on all three) — every regen (the 18-point sweep, the Jazz-verify, both candidate surfaces, DLC, snapshot preview) went to `C:/tmp/stage5_2_2d/…` scratch; the frozen corpus was never written. `src/` + `tools/batch_analyze.cpp` **git-clean** (measurement-only; no code touched → the RETIRE-4 binary is unchanged). Byte-identity ⟹ the stem@tick case-identity sets are identical to CLAUDE.md by construction.

### Suites
No `src/` change this dispatch. **composing 1101 / notation 53 / pipeline_snapshot 11 — all PASSED, 0 FAILED, no golden refresh** (the pinned P1–P4 goldens all match; the surface's 11/11 snapshot *diff* is candidate-vs-baseline **preview**, NOT applied). Matches the 2.2c end-state exactly (composing 1101).

### What retires
**NOTHING.** This dispatch produces a *measured candidate + a prepared-not-applied artifact*; the adoption (and the tie-break) is the user's ratification event. No rule retires, no value changes, no goldens refresh.

### Reuse-vs-new
- **Reuses (verbatim):** `stage5_fit_driver.py` (`regen`/`measure`/`write_override`/`split_scores_file`), `run_bach_preset.py` regen + `--param-override`, `a8_rebaseline_measure.py`, `characterise_bir_false.py`, `run_dlc_baseline.py --param-override` (O-8), `batch_analyze --dump-regions notation` + `--param-override`, the frozen corpus, `stage5_split_registry.json` (261/65), the O-9 per-carrier delivery in `batch_analyze.cpp` (2.2c) — all unmodified.
- **New (committed):** `tools/stage5_2_2d_sweep.py` (the 2-D sub-sweep) + `tools/fit_ledgers/stage5_2_2d_sweep.jsonl` (18-point trade surface); `tools/stage5_2_2d_surface.py` (the candidate decision surface) + `tools/fit_ledgers/stage5_2_2d_surface.jsonl` (both tied candidates). The committed `stage5_fit_driver.py` was **not** modified.

## Repo state

Local/unpushed, fork-only. Working tree `src/` == HEAD (RETIRE-4 binary, untouched). **No `tools/corpus/` write** (all regen → `C:/tmp/…` scratch; frozen `git status` clean, manifest `0dd64660f4`). **No push. No fit value adopted. No rule retired. No golden refreshed.** Commits: 1 `feat(tools):` (driver + 2 ledgers), this report `docs(cowork):` (force-add), the fold `docs(cowork):`.

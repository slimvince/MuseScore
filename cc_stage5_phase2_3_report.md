# CC report — Stage-5 Phase 2.3: the retained-rule margins (staging step 3) + the family-4 §15-13 population gate

**Dispatch:** `cc_instruction_stage5_phase2_3.md` (Cowork, 2026-07-06) · **HEAD at dispatch:** `83f41cdd31` (the 2.2e fold) · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** two cheap measurement questions — **NOTHING adopted, no committed value change, no corpus write, no push.** (A) staging step 3: do the three surviving §6-block margins hold any fittable gain at FULL range? (B) family 4's gate: how large is the §15-13 both-licensed fall-through population on the dormant chain?

---

## Task 0 — state check (PASS, no STOP)

- **HEAD** `83f41cdd31` (the 2.2e fold), **branch** `master`, fork-only.
- **Dirty set:** `COWORK_HANDOFF.md`, `STATUS.md`, `cowork_stage5_fitter_design.md` (the Cowork fold files, modified) + `idiom_discovery/vl_*.txt` + `scratch_artifacts/` (known scratch) — exactly the dispatch's "expected dirty."
- **Binary + frozen corpus:** `ninja_build_rel/batch_analyze.exe` present; `tools/corpus/{baroque,jazz,default}` manifests all stamped **`git_hash c50002fee1`, 352/352** (the 2.2e adopted corpus).
- **Sandwich-before:** `characterise_bir_false.py` ×3 (`--corpus-dir tools/corpus/<preset>`) = **52 / 24 / 52**; the full-enumeration `stem@tick` sets diffed element-wise against the re-stamped CLAUDE.md 52/24/52 sets → **set-diff EMPTY both directions on all three presets.** (Manifest-fingerprint-validated per O-12 — not a git-status claim.)

---

## Task A — the retained-rule margins, full-range ladders (staging step 3)

The three surviving §6-block numeric margins (all 1b-dead at ±step; the 2.1 lesson mandates the full range before skip-with-record). One 1-D ladder per margin via the committed driver (`stage5_fit_driver.py fit`), **Baroque carrier, fitting split (261), refine-rounds 0 = a pure ladder**, §4.2 objective/constraints. Baseline fitting-split root reproduced **63.5391** exactly (== the 2.2e fitting-split baseline). Ledgers committed at `tools/fit_ledgers/stage5_fit_<param>.jsonl`.

### kGateIMargin (current 0.45) — range [0.0, 1.0], 6 points; Gate I first-inversion Min→Maj score-gap tolerance

| value | Δroot | rn% | key% | batch | newB | clsB-dur Δ | feasible |
|---|---|---|---|---|---|---|---|
| 0.0 | **−0.0219** | 44.8407 | 68.2952 | 45 | 0 | +1440 | **False** |
| 0.2 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.4 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.6 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.8 | **−0.0073** | 44.8626 | 68.2733 | 45 | 0 | +480 | **False** |
| 1.0 | **−0.0073** | 44.8626 | 68.2733 | 45 | 0 | +480 | **False** |

**No feasible Δ>0.** Best feasible = baseline (`ALREADY-OPTIMAL-AT-THIS-RESOLUTION`). The current 0.45 sits inside a flat feasible plateau [0.2, ~0.6]; the objective DROPS at BOTH extremes — at 0.0 the gate stops firing (`winner−inv > 0` always → skip; class-(b) dur +1440), at 0.8/1.0 the gate fires on wider gaps and adds a small class-(b) increase (+480). **Closure: skip-with-record — no fittable gain; Gate I RETAINED on structural grounds (it is load-bearing in both directions), its constant stays hand-set.**

### kGateLMargin (current 0.35) — range [0.0, 1.0], 6 points; Gate L same-root Aug→Maj score-gap tolerance

| value | Δroot | rn% | key% | batch | newB | clsB-dur Δ | feasible |
|---|---|---|---|---|---|---|---|
| 0.0 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.2 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.4 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.6 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.8 | +0.0000 | 44.8626 | 68.2806 | 45 | 0 | 0 | True |
| 1.0 | +0.0000 | 44.8626 | 68.2806 | 45 | 0 | 0 | True |

**Δ=0 across the ENTIRE range** (root + RN flat; a sub-0.01 key wobble at the top, tracked-beside only). Even at 0.0 (Gate L never fires) the root objective is unchanged — Gate L is objective-INERT on the Baroque root objective across its whole margin range (consistent with the 2.2b finding that GateL was live only on the 18 Jazz sites, dropped from the Baroque inert set). **Closure: skip-with-record — confirmed objective-inert on the Baroque carrier; RETAINED on structural grounds (live on Jazz per 2.2b), constant stays hand-set.**

### kHalfDimFirstInversionBonus (current 0.55, FM2's bonus) — range [0.0, 1.2], 6 points; the half-dim first-inversion promotion under preferMinorOverMajorAdd6

| value | Δroot | rn% | key% | batch | newB | clsB-dur Δ | feasible |
|---|---|---|---|---|---|---|---|
| 0.0  | **−0.0036** | 44.8663 | 68.2733 | 45 | 0 | +240 | **False** |
| 0.24 | **−0.0036** | 44.8663 | 68.2733 | 45 | 0 | +240 | **False** |
| 0.48 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.72 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 0.96 | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |
| 1.2  | +0.0000 | 44.8626 | 68.2733 | 45 | 0 | 0 | True |

**No feasible Δ>0.** Best feasible = baseline (`ALREADY-OPTIMAL`). The current 0.55 sits inside a flat feasible plateau [~0.48, 1.2]; the objective drops only when the bonus is shrunk toward disabling FM2's promotion (v≤0.24: class-(b) dur +240). **Closure: skip-with-record — no fittable gain; FM2 RETAINED on structural grounds (load-bearing when shrunk), its constant stays hand-set.**

### Task A verdict

**All three margins close as skip-with-record: no feasible objective GAIN at any ladder point, on any margin, at full range.** The full-range ladders REFINE (do not contradict) the ±step-dead 1b reading, consistent with the 2.1 lesson: the ±step-dead did NOT extend to global inertness for two of the three (kGateIMargin and kHalfDimFirstInversionBonus move at the extremes; kGateLMargin alone is globally inert). But every non-zero Δ is a LOSS in an INFEASIBLE direction — the current hand-set values sit at or inside the objective-optimal feasible plateau in all three cases. There is no fit to run; each rule is RETAINED on structural grounds and its constant stays hand-set. **This is a legitimate staging-step-3 closure, stated per margin.** No STOP (no committed value change; the fit driver writes only scratch + the committed compact ladgers).

---

## Task B — the §15-13 both-licensed population (family 4's gate; dormant chain, decode-only)

### B.1 The dump was insufficient → one additive, default-off field (byte-identity proven)

The `--dump-fullspine` per-region schema already exposes `ambiguityKind` / `l5Resolved` / `l5OpenMark` / `l5Basis`, but **not** whether both carried readings were licensed (`aIn && bIn`) — the exact bit that separates the §15-13 both-licensed population from the both-*un*licensed fall-throughs (which fall through for a different reason and are NOT the lever's subject). So the dump could not be counted as-is (Step 1's NOT branch).

Added one **additive, behaviour-neutral** field `bool bothLicensed` on `ResolvedReading` (`functionresolver.h`), set from the resolver's OWN `aIn && bIn` at the two §5.5 licensing arms (`functionresolver.cpp`: TransitionVsContinuation :223 and ShareTone :244) — it records what the resolver already computes, changes no control flow, and is read only by the default-off `--dump-fullspine` emit (`l5BothLicensed` in `batch_analyze.cpp` runFullSpine). Since the field lives only on the dormant resolver's output and the production `writeJson` path never touches `ResolvedReading`, the standard `.ours.json` is byte-identical by construction.

**Field validated at the source (4 pinned assertions, `functionresolver_tests.cpp`):**
- `ShareTone_BothLicensedCarriesOpenMark` → `bothLicensed == true`, outcome = open mark ✓
- `Transition_BothLicensedResolvesAsNeighbourWithinPrevailing` → `bothLicensed == true`, outcome = tie-break (NeighbourHarmony) ✓
- `ShareTone_ResolvedByLicensedProgressionIntoNext` (uniquely licensed) → `bothLicensed == false` ✓
- `Transition_ResolvedAsArrivingFunction` (uniquely licensed) → `bothLicensed == false` ✓

**Byte-identity PROVEN** (design's stated bar + the 2.2a/O-9 gold-standard regen-compare): standard full-corpus regen (NO `--dump-fullspine`) of the NEW binary, diffed file-by-file (`cmp`) against the frozen `tools/corpus/<preset>` — **0 differing / 352 on Baroque, Jazz, AND Default.** Plus suites green with **no golden refresh** (composing **1101** / notation **53** / pipeline_snapshot **11**), and the pin count unchanged (assertions added to existing tests). Frozen corpus fingerprint-validated untouched (regens all to scratch).

### B.2 The population (×3 carriers, decode-only, over the frozen 352-score corpus)

The L5 resolver ran over the corpus via `run_bach_preset.py --dump-fullspine --output-dir <scratch>` (352 dumps/preset); counted by the new committed driver `tools/stage5_15_13_population.py`.

| preset | slices | L4-abstain units | **§15-13 both-licensed** | Transition / ShareTone | tie-break / open-mark | dur share (of scored / of abstain) |
|---|---|---|---|---|---|---|
| **Baroque** | 29080 | 18194 | **5544** | 3549 / 1995 | 2659 / 2885 | **16.47 %** / 28.82 % |
| **Jazz** | 29080 | 18271 | **5581** | 3575 / 2006 | 2656 / 2925 | **16.61 %** / 28.92 % |
| **Default** | 29080 | 18194 | **5544** | 3549 / 1995 | 2640 / 2904 | **16.47 %** / 28.82 % |

- **Outcome breakdown (Baroque):** tie-break 2659 = BassDegreePrior 1621 (§5.7 soft prior) + NeighbourHarmony 1038; open mark 2885 (basis None). Internally consistent on every carrier (tie-break + open-mark == both-licensed; None == open-mark exactly; only Transition/ShareTone kinds appear → the field is correctly scoped, no leakage into RelativePair/CloseReading/SymmetricRotation).
- **Per-score distribution (all three):** 351 / 352 scores carry ≥1 both-licensed case; max 87 / score; median (over nonzero scores) 15.
- **Cross-carrier consistency:** Baroque == Default at 5544 (identical Transition/ShareTone split; the ±19 outcome-basis wobble is a handful of §5.7 bass-prior decisions that differ under the two carriers' decoder settings). Jazz +37 (5581) — a few more abstains. All three ≈16.5 % of scored duration.

### B.3 The gate verdict material (design §4.4 family 4)

The design's stated gate is a **size** test: *"if the population is too small for a fit to be evidence-based … the item returns to the user with the number and stays a recorded §15-13 open item."* **The population is LARGE, not small** — 5544/5581/5544 cases, ~16.5 % of scored duration, present in 351/352 scores, with a substantial actionable split (≈48 % currently reach the honest open mark; ≈52 % resolve by a NON-progression structural prior — both are cases a preference-among-licensed order could touch). **By the design's size gate, the §15-13 fit is not noise-limited; it passes the "evidence-based" size threshold.**

**★ One finding DECLARED to Cowork (not decided, not acted on) — the objective-substrate observation.** The §15-13 weight acts on the **DORMANT L5 resolver's** output (this whole population lives on the fullspine chain). That output does **not** enter the current A-8 fitting objective, which measures duration-weighted root agreement on the **production / L4** `.ours.json` (proven here: the L5 field is byte-identical on that path). So while the population is size-viable for a fit, **the fit is not *runnable* under this arc's current objective** — changing the §15-13 preference would move the fullspine (L5) roots on those ~5544 slices but leave the a8 production objective at Δ=0 by construction. Running the fit would require either (a) L5 engagement so the resolver output is what the objective grades, or (b) a dedicated resolver-output objective + its GT. **This is a design/sequencing question for Cowork/user — the number says "big enough"; the substrate says "not against today's objective." No fit runs either way (per the dispatch); the number + this observation are the checkpoint material.**

---

## Task C — sandwich + suites + reuse/new + closures

### C.1 Sandwich (CLOSED)
- **Before AND after** (`characterise_bir_false.py --corpus-dir tools/corpus/<preset>`): **52 / 24 / 52**, full-enumeration `stem@tick` sets diffed element-wise against the re-stamped CLAUDE.md → **set-diff EMPTY both directions, all three presets.**
- Corpus manifests still stamped `git_hash c50002fee1`; `characterise` ran clean (refuse-on-mismatch not tripped) → **fingerprint-validated byte-untouched (O-12 wording; not a git-status claim).** All regens (Task A driver + Task B byte-identity + fullspine) wrote to scratch only.
- **Suites:** composing **1101** / notation **53** / pipeline_snapshot **11** — 0 failed, **no golden refresh**.

### C.2 Reuse-vs-new + what retires
- **Reuses (verbatim):** `stage5_fit_driver.py fit` (the Task-A ladders), `run_bach_preset.py` (regen + `--dump-fullspine`), `characterise_bir_false.py` (sandwich), the fullspine dump schema + `runFullSpine`, the split registry / fitting split, the frozen corpus.
- **New (committed):** `tools/stage5_15_13_population.py` (the population counter); the three Task-A ladder ledgers `tools/fit_ledgers/stage5_fit_{kGateIMargin,kGateLMargin,kHalfDimFirstInversionBonus}.jsonl` (O-8 committed compact ledgers).
- **Modified (committed):** `functionresolver.h`/`.cpp` (the additive `bothLicensed` telemetry) + `functionresolver_tests.cpp` (4 validating assertions) + `batch_analyze.cpp` (the `l5BothLicensed` dump field) — all additive, production byte-identical.
- **What retires:** **nothing** (as expected). Task A retains all three margins on structural grounds; Task B is a decode-only census.

### C.3 Closures
- **Task A (staging step 3):** all three surviving §6-block margins measured at FULL range → **no feasible objective gain anywhere; skip-with-record; each RETAINED, constant stays hand-set.** The full-range ladders refine (do not contradict) the ±step-dead 1b reading (the 2.1 lesson holds — kGateI/kHalfDim move at the extremes, kGateL globally inert), but every non-zero Δ is a loss in an infeasible direction and the current hand-set values sit at/inside the objective-optimal feasible plateau. A legitimate staging-step-3 closure, stated per margin.
- **Task B (family 4 gate):** population measured LARGE (5544/5581/5544; 16.5 % dur; 351/352 scores) — size-viable per the design gate; the objective-substrate finding declared to Cowork (dormant-chain output not in today's a8 objective). No fit run.
- **O-12 discipline followed:** every byte-untouched claim in this report cites manifest-fingerprint validation / an explicit regen-compare, never git status.

---

## Commit SHAs (this dispatch)

| # | type | contents |
|---|---|---|
| 1 | `feat(composing):` | the additive §15-13 instrumentation — `bothLicensed` field + `l5BothLicensed` dump + 4 test assertions + `stage5_15_13_population.py` (production byte-identical, proven 0/352 ×3) |
| 2 | `docs(cowork):` | this report (force-add) + the three Task-A ladder ledgers |
| 3 | `docs(cowork):` | the fold — STATUS (22v) · COWORK_HANDOFF · design (O-13 + staging-step-3 closure) · the instruction (force-add) |

Local/unpushed, fork-only. **No push.**

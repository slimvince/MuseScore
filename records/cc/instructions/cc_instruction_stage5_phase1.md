# CC Instruction — Stage-5 Phase 1: the fitting harness (1a) + the sensitivity screen (1b)

> **ACTIVE DISPATCH (Cowork, 2026-07-04).** Second CC increment of the Stage-5 fitter arc, per the SIGNED
> design `cowork_stage5_fitter_design.md` — read §0 TERMS, §2 (constraints, esp. **4c: optimize for
> idioms only, NEVER for the current user presets** — presets are regression surfaces and delivery
> carriers, never optimization targets), §4.2 (the objective + constraint scoping), §4.3 (this phase),
> §7 (data design), D-3/D-6/D-9/D-11, and the ratified **P0 boundary: 61 rows tunable / 17 frozen, with
> the frozen-row verification rider** (§4.1/§4.3). Also read `cc_stage5_phase0_report.md` (your own
> Phase-0 findings are this phase's premises) and `tools/param_manifest.json`.
>
> **Nature:** 1a is INFRASTRUCTURE — the one sanctioned `src/` touch of the arc (design ask A-6, ratified):
> a flag-gated parameter-override mechanism, **byte-identical when absent, with proof**. 1b is
> MEASUREMENT — decode-only, nothing adopted, no constant changes. NO FIT HAPPENS IN THIS DISPATCH.

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (top entries),
> `C:\s\MS\BUILD_AND_TEST.md`, and — since this session TOUCHES scoring-constant plumbing —
> `C:\s\MS\docs\scoring_model.md` in full.
>
> **Current state (Cowork-verified 2026-07-04):** batch stop **53/24/53** case-identity per CLAUDE.md;
> corpus 352/352 ×3 (manifest git_hash `0dd64660f4`); suites composing 1083 / notation 53 / snapshots 11.
> Expected-dirty tree: the Cowork narrative files in the Task-6 fold list + the known deliberately-
> untracked dumps/scratch (`idiom_discovery/vl_*_out.txt`, `scratch_artifacts/` — STATUS 22e/22g;
> excluded from the dirty-set check by standing ruling). Anything else dirty: STOP.
> **Hard stops:** any behavior change with the override absent (byte-identity is the acceptance);
> any write under `tools/corpus/`; any batch-stop set-diff ≠ empty at the sandwich; any fit/adoption;
> any push.
>
> **VS Code bash rules apply:** `; echo "exit:$?"` on every command; large output → file + `head`.

---

## Task 0 — state check

`git rev-parse --short HEAD`, branch, dirty set vs the expectation above. Report all three.

## Task 1 (1a-i) — the parameter-override mechanism (the sanctioned `src/` touch)

**Requirement (design D-6, shape ratified):** the analysis pipeline accepts an OPTIONAL parameter-override
input (file passed via a new `batch_analyze` flag, e.g. `--param-override <file>`); when absent,
**behavior and output are byte-identical to today** (that is the acceptance, proven, not argued). When
present, it overrides the values of manifest rows by `name`.

**Coverage requirement (your own Phase-0 finding #2):** the mechanism must reach ALL 61 tunable rows —
including the constants with **no runtime surface today**: the file-level `constexpr` scoring constants in
`chordanalyzer.cpp` (G1) and the progression constants in `harmonicfunctionlayer.h` (G6). This will
require converting those `constexpr` declarations to a runtime-readable form. Constraints on that
conversion:
- **Values unchanged**; initialization = the current literals; the override loader is the ONLY writer.
- **Byte-identity proof with override absent** (below) — this is what makes the conversion safe.
- Keep the conversion MINIMAL and mechanical (no restructuring, no renaming beyond what the mechanism
  needs, no gate/logic changes — R9 file-split stays parked; this is plumbing, not refactoring).
- The 17 frozen rows: the override loader must **also** be able to set them (the ratified frozen-row
  verification rider needs it for 1b's read-only perturbation) but the fit driver (Task 3) refuses to
  propose them — enforcement lives in the driver, reach lives in the plumbing.
- If a constant turns out to be structurally impossible to make runtime-readable without a logic change
  (e.g. a template array extent — none is expected; array extents are not manifest rows): STOP and report.

**Doc-sync (same commit):** `docs/scoring_model.md` gains a short note (§1 or §3) that the scoring
constants are readable from an optional override file for Stage-5 fitting, default absent, byte-identical
when absent. **In the same scoring-docs commit, fix the four recorded Phase-0 doc-drift defects** (your
report §"Doc-drift": the missing `kHalfDimFirstInversionBonus` §6 entry; the §4 progression-signal
location drift to `harmonicfunctionlayer.*`; the stale §4 anchors; the stale §6 gate-table anchors) —
discharging the queued fixes in the natural commit.

**Proofs required (before any 1b run):**
1. Flag absent: full-corpus regen (scratch) `.ours.json` **byte-identical** to the frozen corpus per
   preset; `pipeline_snapshot_tests` 11/11 no refresh; composing/notation green.
2. Flag present with an **identity override file** (all 78 rows at their current values): output
   byte-identical again (proves the loader itself perturbs nothing).
3. A unit test for the loader (parse, unknown-name rejection, absent-file = defaults) + coverage of the
   new paths (standing objective).
4. Rebuild required — use the PowerShell Start-Process build per CLAUDE.md.

## Task 2 (1a-ii) — additive instrument flags (pinned instruments; proofs mandatory)

The harness needs two additive capabilities your Phase-0 report identified:
1. `a8_rebaseline_measure.py`: a `--corpus-root <dir>` (read scratch dirs) and a `--preset <name>`
   (single-preset) option. **Default behavior byte-identical** (run without the new flags before/after
   the change; `summary.json` + enumerations byte-identical), self-validation (grid==oracle) intact,
   `tools/tests` green.
2. `characterise_bir_false.py`: verify it already accepts `--corpus-dir` on scratch (it does per Phase 0);
   no change expected — if one IS needed, same proof discipline.

## Task 3 (1a-iii) — the fit driver + the ledger + the split

New `tools/stage5_fit_driver.py` (name at your discretion; report it):
- **Evaluate(vector, carrier-set):** write the override file → regen the affected preset carrier(s) to
  manifest-stamped scratch → objective per design §4.2 (**variant-(b) root-agree duration on the
  FITTING SPLIT's covered cells**; RN + key tracked beside) → constraints (no new class-(b) batch-stop
  case among fitting-split scores, checked against the CLAUDE.md identity subsets; class-(b)
  root-disagree duration non-increase on the fitting split) → one ledger row (design §7 schema: run id ·
  preset(s) · family · vector · objective · tracked respects · constraint results · timestamp ·
  instrument versions).
- **Refuses to propose/accept a vector touching a frozen row** (P0 enforcement) — but exposes a separate
  explicit `--perturb-frozen` mode for 1b's rider measurement (labeled as such in the ledger).
- **Determinism proof:** the identical evaluation run twice → byte-identical ledger rows (timestamps
  excluded by design — put them in a separate column so the comparison is clean).
- **Known-vector fixture:** the current constants evaluated at FULL coverage must reproduce the ratified
  baselines exactly (root-agree 63.32 / 62.37 / 63.22 %); the fitting-split baseline is then recorded
  beside them (new, defined by this task).
- **The split (design §4.3 1a):** define the fitting/held-out split of the 326 WiR-covered scores.
  Requirements: recorded rationale; stratified so both splits carry major AND minor chorales (the §4.4a
  mode strata must exist inside the fitting split); registry `split` field per the OQ-C1 discipline;
  approximately 80/20 unless you find a measured reason otherwise (state it). **The split is
  ratification-gated:** propose it in the report with the stratification numbers; Cowork/user ratify
  before Phase 2 uses it. 1b's screen may run on the PROPOSED split (sensitivity ranking is
  split-robust; state this caveat in the report).

## Task 4 (1b) — the sensitivity screen (decode-only; nothing adopted)

Per design §4.3 1b + the ratified P0 rider:
- **All 78 manifest rows** (61 tunable + **17 frozen, read-only rider**), one at a time, ± a small step
  (default ±10 % of the value; for values in [0,1] use ±0.05 absolute; for the two θ and squash-k rows
  use ±10 %; state the chosen step per row in the output — the step is a screen resolution, not a fit).
- **Carrier scope (constraint 4c):** the screen runs on the **Baroque carrier** (the idiom-#2 primary);
  re-run the **top-10 movers** on the Default carrier (expected near-identical — a divergence is a
  finding); the **Jazz carrier is NOT screened for fitting** (it receives no fit — A-3); shared-scope
  rows get a Jazz **regression spot-check only** (constraint status, not leverage).
- Per row record: objective delta (both directions), constraint status, whether any §6-block rule's
  firing count changed (the interaction warning), the batch-stop subset status.
- **Deliverables:** the leverage ranking; the dead list (Δ≈0 both directions — "fit to zero" candidates,
  roadmap 5.2); the interaction warnings; **the frozen-row findings** (any frozen row with material
  leverage — report, do NOT unfreeze); the manifest's `sensitivity` column filled (a manifest-update
  commit, values only, no other column touched).
- Budget guidance from your own cost numbers: ~78 rows × 2 directions ≈ 156 single-preset evaluations;
  with the Task-2 single-preset a8 mode expect ≈ 45 s each ≈ 2 h — acceptable; if measured cost explodes
  past ~4× that estimate, STOP and report rather than trimming the row set silently.

## Task 5 — sandwich + suites + report

1. End-of-run sandwich: `characterise_bir_false.py` on the REAL dirs ×3 — 53/24/53 set-diff empty both
   directions; frozen corpus byte-untouched (`git status tools/corpus/` = clean).
2. Full suites: composing / notation / snapshots (no refresh) — with the new binary (flag absent).
3. Report `cc_stage5_phase1_report.md` (force-add): the mechanism's shape + the byte-identity proofs ×2
   (flag absent / identity override); the instrument-flag proofs; the driver + determinism + known-vector
   fixture results; the PROPOSED split with stratification numbers (ratification-gated); the full 1b
   deliverables (ranking, dead list, interactions, frozen-row findings); reuse-vs-new + what retires;
   ALL commit SHAs. **The report's checkpoint section addresses Checkpoint P1's decision surface
   explicitly:** optimizer feasibility per D-3 on the measured evaluation cost, the suggested family
   staging from the interaction warnings, and the R-13 data-limitation read.

## Task 6 — the fold (`docs(cowork):`, exact list)

`STATUS.md` (22m entry) · `COWORK_HANDOFF.md` (header) · `cowork_stage5_fitter_design.md` (the post-fold
Cowork edits: the D-10 two-axes note, constraint 4c, the P0-ratified markers) · `cc_instruction_stage5_phase1.md`
(force-add). Nothing else; nothing under `src/` in THIS commit (the src change is its own Task-1 commit).

## STOP conditions

- Byte-identity failure at ANY Task-1 proof (this is the arc's central safety property — no workaround).
- A constexpr conversion that cannot be mechanical (needs logic restructuring) — report the row, do not
  improvise.
- Sandwich mismatch; suite regression; snapshot refresh needed.
- 1b cost >~4× the estimate; >5 rows with indeterminate perturbation semantics.
- Anything requiring a fit, an adoption, or a constant's committed value to change.

## Commit plan (each with SHAs in the report)

1. `feat(analysis):` the override mechanism + loader tests (src + the scoring_model.md note + the four
   drift fixes — the scoring-docs sync rides the same commit per the CLAUDE.md rule).
2. `feat(tools):` the a8/characterise additive flags + proofs.
3. `feat(tools):` the fit driver + ledger + the proposed split (registry field).
4. `feat(tools):` the manifest sensitivity-column update (after 1b).
5. `docs(cowork):` the Task-6 fold.
6. `docs(cowork):` the report (cites all of the above).

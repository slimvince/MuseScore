# CC report — Engage arc #1: the F-B fine-grain override REDESIGN (design/scoping pass)

**Session 24, 2026-07-06. Dispatch:** the engage-arc opener (Stage-5 CLOSED; O-16). **Read-only
architectural design + the ratified-backlog push.** NO `src/` change, NO scoring value, NO corpus write, NO
build, NO θ retune. Design doc: `cowork_fb_redesign_design.md`.

---

## What landed

### Task 0 — the ratified backlog pushed to the fork ✓
`git push origin master`: **`ce509b0961..923f149561  master -> master`**. Ahead-count **76 → 0**.
- **New `origin/master` = `923f14956157d3117988c12e0b51d9c858b9813c`** (= HEAD `923f149561`, the R10-b fold).
- **Fork-only HARD STOP honored:** verified `origin = https://github.com/slimvince/MuseScore`; `upstream`
  (`musescore/MuseScore`) push URL = **`disabled`**; the push command explicitly targeted `origin master`.
  The `cfc7eb5e39` MusicXML-mode patch stays fork-local; nothing moved toward `upstream`.

### Task 1 — F-B characterized at the source ✓ (design §1)
The override is `attemptFineGrainOverride` (`functionresolver.cpp:381`), Phase-2 of `resolveCarriedReadings`.
Every input tied to a source symbol: incumbent = `s.confidence.composite` (`SliceConfidence = min(margin,
sufficiency, cleanliness)`, all vertical — grounded at `chordslicedecoder.h:404-408/120-121`; **"vertical-fit
only" is code-truth**); contradiction = `bestPlaus − committedPlaus` from `plausibility()` (3 unit-weighted
progression/cadence features, ∈ {0,1,2,3}); bar = `1.0 + 1.0·composite` ∈ [1.0, 2.0]; selection = carried
alternatives ∪ neighbour commits, verbatim. **Dormancy verified at source:** the only callers are the unit
tests and `batch_analyze.cpp:3186`'s `--dump-fullspine` (E0) harness — production `.ours.json` byte-identical
without it.

### Task 2 — the 1043/53/809 decomposed into a measured taxonomy ✓ (design §2)
Read-only orchestration over the **existing** `C:/tmp/c1/fs_*` dumps (no regen; the `theta_fit`-sanctioned
"reads existing dump fields" path), reproducing 1043 = 53 corr + 809 harm + 181 neutral exactly. Findings:
- **The documented root-cause is CONFIRMED and strengthened:** harm rate is ~uniform (71–86 %) across every
  stratum — `S`=2 (77.9 %) vs `S`=3 (75.5 %); `C` bands 71.5 %→80.8 % with the **highest** harm at the
  **highest** L4 confidence. The only θ lever (scale bar by `C`) points the wrong way ⟹ code-grounded proof
  of "the best θ disables it."
- **The harm mechanism:** fourth/fifth root moves = 55 % of fires / 58 % of harm (move-7 85.7 %) — exactly
  what `isLicensedProgression` rewards. The override tidies the functional story at the expense of the
  vertical fact L4 had right.
- **The discriminator = NONE:** every measured stratum is net-negative; the 53 corrections are diffuse and
  share the harms' feature signatures.
- **The incumbent-repair premise is REFUTED at data:** even where the selected alternative is vertically ≥
  the committed reading (`g ≤ 0`), harm is still 70.8 % (corr−harm −163). A vertically-fair comparison does
  not reach net-positive — the contradiction is uncorrelated with root-correctness.

### Task 3 — redesign options ✓ (design §3)
disable-baseline (corr−harm 0, +756 recovery, the floor) · gate (degenerates to disable — no net-positive
carve exists) · incumbent-repair (refuted, ≈ −163, large blast radius) · re-frame-annotate (§8 case-3 honest
carry: 0 harm / 0 corr + preserves the 1043 signals) · re-frame-C3 (the correct long-run home; projected
split UNKNOWN — needs a new measurement). Each with layer / theory / projected-split / blast-radius / risk.

### Task 4 — recommendation + build-event surface ✓ (design §4)
**Recommend §3.D-1 (demote to annotation), floored by §3.A (disable); reject gate and incumbent-repair as
measured net-negative.** Build event touches: `functionresolver.cpp` + `ResolvedReading` + confidence
contract §4 F-B + L5 §5.5/§10/§15-2 + `docs/scoring_model.md` sync + the roadmap/fitter engage note.
Acceptance = the robust-unit stop (class-(b) root-disagree DURATION non-increase per preset; dormant ⟹
identity today, must move favorably at engage). The 53 lost corrections require a correctness-correlated
contradiction signal = an inference-quality question, **declared to Cowork, out of scope.**

---

## Grounding sources (the user's "knowledge not assumptions" constraint)
- `[code]`: `functionresolver.cpp/.h`, `forwardoverride.cpp/.h`, `chordslicedecoder.h`, `batch_analyze.cpp`.
- `[data]`: the existing `C:/tmp/c1/fs_baroque` E0 dumps + DCML root GT, joined per `theta_fit.py`; scripts
  `fb_taxonomy.py` / `fb_vertical.py` (scratchpad, read-only).
- `[flag]` items surfaced, not assumed: (1) `l5Basis` does not distinguish carried-alt vs neighbour — the
  1042/1 split is a heuristic `(root,quality)` match; (2) `committed_score` in the vertical-gap band is a
  proxy; (3) the C3 population is **not** in the dump ⟹ §3.D-2's split is UNKNOWN; (4) all numbers are the
  **dormant decode chain**, not production.

## Contract / code drift found
**No implementation drift** — the code faithfully implements the declared Frame F-B. **One
premise-invalidation:** the contract §4 / `functionresolver.cpp:461` rationale *"θ accounts for the missing
progression term (L5 §15-2)"* is empirically refuted (no θ separates corrections from harms; §2.1/§2.4).
Recorded as the design's §1.4 finding (already logged as D-FS / the Phase-3 inference finding; this pass
grounds *why* at the code + stratified data).

## Sandwich (trivial — read-only, by construction)
No `src/` or `tools/corpus/` change (git status: no tracked modifications; only untracked docs + scratch).
Both stops untouched by construction — **batch 52/24/52** and the **robust sandwich identity-PASS** unchanged;
suites unchanged (no build). The only new tracked files are the two docs + the folds below.

## SHAs
- Pre-dispatch HEAD / new `origin/master`: **`923f14956157d3117988c12e0b51d9c858b9813c`**.
- This dispatch's `docs(cowork):` fold commit: **recorded in STATUS.md on commit** (design doc + this report
  force-added; STATUS / HANDOFF / fitter-design O-17 / the instruction folded).

## STOP conditions — none tripped
No `src`/corpus/build/θ-retune. No upstream push. No design step rested on an unverified assumption (the four
gaps above are flagged, not built on). Both stops green.

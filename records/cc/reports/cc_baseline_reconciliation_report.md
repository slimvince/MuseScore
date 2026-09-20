# Baseline reconciliation at committed HEAD `0b42096d75`

**Read-only diagnosis. No code/golden/commit/push changes were made.** All measurements below were
taken on **clean committed HEAD** (or, where HEAD itself does not build, on the last buildable commit
whose existing pipeline is byte-identical to HEAD — see §2).

**Headline:** the documented baseline (CLAUDE.md: **57/23/57**, both suites green) does **not** match
committed reality, and clean HEAD **cannot build the BIR harness at all**. Three independent facts:

1. **Committed HEAD does not compile `batch_analyze`** (the canonical BIR tool). Build break introduced
   by `5f6b9828a5` (L4 Inc B), inherited by HEAD.
2. **Canonical BIR at committed baseline = 53 / 24 / 53** (Baroque/Jazz/Default), not 57/23/57. This is
   the **already-ratified L3-wiring delta** that CLAUDE.md describes *in prose* (−4/+1/−4) but never
   propagated into its gate identity tables — i.e. the tables are stale, not a regression.
3. **5 notation tests fail at clean HEAD** (and at every commit back to the baseline). The "both suites
   green" claim is contradicted; these failures **predate** all of this session's work.

My earlier "53/24/53 + 5 failing tests" was therefore **not** a side-metric or dirty-tree artifact for
the BIR number — 53/24/53 is the *real committed BIR*. (The dirty tree did matter for buildability:
the WIP is what makes `batch_analyze` compile.)

---

## §0 — Working-tree state (the premise check)

**The instruction's premise — "Cowork checked the repo: `git diff` and `git diff --cached` are both
empty, there is no uncommitted WIP" — does NOT hold in my environment.** At session start my working
tree was **dirty**:

- `git rev-parse HEAD` = `0b42096d75f5005aecd9f7216e51872f00956957` ✓
- `git diff --stat` = **2457-line diff across 23 tracked files**, `git diff --cached` = empty (nothing staged).
- Dirty tracked files include **production code**:
  `src/composing/analysis/chord/chordslicedecoder.{cpp,h}`,
  `src/composing/analysis/key/keymodesequence.{cpp,h}`, `keymodeanalyzer.h`,
  `src/composing/analysis/section/localmodulationdetector.{cpp,h}`,
  `src/composing/analysis/engravingbridge/regiontoneprimitives.cpp`,
  **`tools/batch_analyze.cpp`** (the analysis tool the BIR harness builds), plus docs/STATUS/CLAUDE.md.

This means my earlier "baseline" reading was taken on this **dirty tree**. Per §0 I:
- saved the full diff to scratch (`uncommitted_tracked.diff`, 2457 lines),
- **stashed** the tracked WIP: `stash@{0}: On master: baseline-reconciliation: stash dirty tracked WIP …`,
- confirmed HEAD clean: `git status --short | grep -v '^??'` → 0 tracked-dirty lines at `0b42096d75`.

Untracked files (the many `??` entries — new docs/tools/test-data) were left in place (plain `git stash`,
per the instruction); none are part of the committed build.

**Discrepancy to surface:** Cowork and CC are evidently looking at different working-tree states. In my
environment there is substantial uncommitted production WIP; Cowork reported none. (I do not speculate on
the cause — different checkout, or the WIP appeared after Cowork's check — but it must be reconciled,
because some of that WIP is load-bearing for the build; see §1/§4.)

---

## §1 — Both suites at clean HEAD `0b42096d75`

Built test targets directly (`build_tests.bat` for composing+notation; a one-target ninja build for the
snapshot) — these avoid the broken `batch_analyze`.

| Suite | Result at clean HEAD |
|---|---|
| `composing_tests` | **624 / 624 PASS** (1 disabled) — matches expected post-Phase-1a count |
| `notation_tests` | **52 PASS / 5 FAIL** |
| `pipeline_snapshot_tests` | **11 / 11 PASS** (no `--update-goldens`) |
| `batch_analyze` (BIR tool) | **DOES NOT BUILD** — `error C2039: 'tpcKeyFitWeight' is not a member of KeyModeSequencePreferences` at `tools/batch_analyze.cpp:2549` |

**The 5 failing notation tests (real, at clean committed HEAD):**

- `Notation_ImplodeTests.MozartK279OpeningPrefersCMajorOverFLydian`
  — `regions.front().keyModeResult.keySignatureFifths` is **−1**, expected **0** (key inference: got F/1-flat, want C major).
- `Notation_ImplodeTests.CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord`
  — chord symbol **"G"** emitted where **"Gm"** expected (tick 1:960); annotation shows `G / V` where `Gm / i` wanted.
- `Notation_ImplodeTests.PopulateChordTrackEmitsCadenceMarkersOnCorelli`
- `NotationInteractionHarmonyPinning.BehaviorSnapshot_RomanNumeral` — `rows[0].roman` is **"V"**, expected **"I"**.
- `NotationInteractionHarmonyPinning.BehaviorSnapshot_Nashville` — `rows[0].nashville` is **"5"**, expected **"1"**.

So yes — there really are **5 failures at clean HEAD**, not 0. They are key/mode + chord-root behavior
mismatches.

**The build break in detail.** At committed HEAD:
- `tools/batch_analyze.cpp:2549` references `seqPrefs.tpcKeyFitWeight` (the `--seq-tpc-weight` arg handler).
- The committed `KeyModeSequencePreferences` struct in `keymodesequence.h` has **no** `tpcKeyFitWeight` member.
- `git log -S tpcKeyFitWeight` finds the symbol in **no commit** of `keymodesequence.h` — the member exists
  **only in the stashed WIP** (`+ double tpcKeyFitWeight = 0.0;` plus its logic in `keymodesequence.cpp`).

The `--seq-tpc-weight` / `tpcKeyFitWeight` feature is **split across the commit boundary**: the *consumer*
(`batch_analyze.cpp`) was committed in `5f6b9828a5`; the *definition + implementation*
(`keymodesequence.{h,cpp}`) was left uncommitted. A clean checkout of `5f6b9828a5` or HEAD therefore
cannot build `batch_analyze`.

---

## §2 — Canonical BIR, all three presets

**Cannot be measured at clean HEAD** — `batch_analyze` does not build there. Measured instead at the
**last commit where it does build**, `48909fb752` (L4 Inc A). This is a faithful proxy for committed
baseline production because Inc A's only change to `batch_analyze.cpp` is **purely additive**
(`git show --numstat` = `223 0`, a new `--decode-chords` diagnostic that "returns before analyzeScore");
the existing BIR measurement path is byte-identical to the documented-baseline commit `a6b08af3fe`
(the only production change in `a6b08af3fe..48909fb752` is the additive Inc A itself). Each preset run is
353/353 complete with a stamped manifest (git `48909fb752`).

| Preset | Documented (CLAUDE.md tables) | **Measured (committed)** | Net |
|---|---|---|---|
| Baroque | 57 | **53** | −4 |
| Jazz | 23 | **24** | +1 |
| Default | 57 | **53** | −4 |

**Case-identity deltas vs the documented sets:**

- **Baroque 53** — removed `{bwv102.7@17520, bwv122.6@6720, bwv227.7@18120, bwv301@960, bwv336@8640, bwv381@4800}`;
  added `{bwv272@4320 (G♯dim7), bwv289@20160 (A♯dim7)}`. (−6/+2 = −4)
- **Jazz 24** — removed `{bwv244.15@10080}`; added `{bwv272@4320 (G♯dim7), bwv291@17760 (Eø7↔Gm6)}`. (−1/+2 = +1)
- **Default 53** — removed `{bwv102.7@17520, bwv122.6@6720, bwv187.7@19200, bwv301@960, bwv336@8640, bwv352@1440, bwv381@4800}`;
  added `{bwv272@4320, bwv289@20160, bwv387@10560 (G♯dim7/E7♭9)}`. (−7/+3 = −4)

**These deltas are exactly what CLAUDE.md already describes in prose.** The "First accepted class-(a)
interim case (Layer-3 wiring, 2026-06-22)" paragraph states **"Baroque/Default net −4 … Jazz net +1"** and
names the very cases measured here: new `bwv272@4320`, `bwv291@17760`, `bwv289@20160`, `bwv387@10560`, and
`bwv244.15@10080` fixed — all symmetric dim7 / share-tone (class-(a)). So the gate *identity tables*
(57/23/57) are **stale**: they were never updated to reflect the L3-wiring increment the same document
already ratified. Committed reality is the post-L3-wiring state (53/24/53), which is *better* per the
gate's own two-tier policy (the new cases are all verified class-(a)).

Per-preset chord-identity agreement at the committed baseline: Baroque 90.9% (10250/11271 regions).

---

## §3 — Localization

Commit order (oldest → newest), with what each changed in the existing production pipeline:

| Commit | What | Build `batch_analyze`? | notation 5-fail? | BIR |
|---|---|---|---|---|
| `a6b08af3fe` | L3 wiring (last production-key change; 57/23/57 documented at descendant `9b643a454a`) | yes (= Inc A path) | yes (by construction) | 53/24/53 |
| `48909fb752` | **L4 Inc A** — additive only (new `chordslicedecoder.*`, new `--decode-chords`) | **yes** (measured) | **yes (measured)** | **53/24/53 (measured)** |
| `5f6b9828a5` | **L4 Inc B** — modifies `chordslicedecoder.*`, `regiontoneprimitives.cpp`, `metricweights.*`; commits the orphaned `tpcKeyFitWeight` consumer in `batch_analyze.cpp` | **NO — build break enters here** | yes | unmeasurable (no build) |
| `0b42096d75` | **Phase 1a** (HEAD) — `note_model.{cpp,h}` + tests **only** | NO (inherited) | **yes (measured)** | unmeasurable (no build) |

Findings:

- **Build break → `5f6b9828a5` (L4 Inc B), definitively** (`git log -S tpcKeyFitWeight -- tools/batch_analyze.cpp`
  → only `5f6b9828a5`; the matching struct member is in no commit). The commit's "(isolated) / production
  byte-identical" claim is **false for buildability**.
- **BIR 57/23/57 → 53/24/53 is NOT a regression and did NOT enter in this session's commits.** It is the
  committed state at the baseline itself (Inc A's existing path = `a6b08af3fe` byte-identical), i.e. the
  already-accepted L3-wiring delta. The documented identity tables simply lag.
- **The 5 notation failures predate the L4 increments** (present at additive Inc A → therefore at the
  baseline). The affected test files are unchanged since the baseline; the relevant production was last
  touched by **Stage-4b key commits** (`ef30cc70f3` "demote declared-mode wall", `81978321e3` "Baroque
  partial-signature correction", `5299f20964` "correct Corelli … G→Gm"). They are committed, pre-existing,
  and **not** caused by Phase 1a or the L4 work.
- **Phase 1a `0b42096d75` is clean** (note_model + tests only; verified file list) and is correctly
  exonerated for both the notation failures and the BIR delta — but it sits atop the unbuildable Inc B.

---

## §4 — Verdict

Not a single one of the instruction's (a)/(b)/(c) — it is a **combination of (b) + (c)**, and decidedly
**not (a)**:

1. **(c) — committed build break, blocking.** `batch_analyze` (the BIR harness) does not build from a clean
   checkout of HEAD; the break entered at `5f6b9828a5`. Root cause: the `--seq-tpc-weight` feature was
   committed half-and-half — consumer committed, `keymodesequence.{h,cpp}` definition left uncommitted
   (now in `stash@{0}`). Phase 2 cannot measure BIR until this is fixed.

2. **(b) — stale documentation, two places.**
   - The gate **identity tables (57/23/57)** lag the committed reality (**53/24/53**), which is the
     L3-wiring delta CLAUDE.md *already describes in prose* (−4/+1/−4) but never wrote into the tables.
   - The **"both suites green" claim** is contradicted by 5 pre-existing committed notation failures.

3. The earlier **"53/24/53"** is the **real committed BIR**, not a side-metric/dirty-tree artifact. (The
   dirty tree only mattered for buildability — the WIP defines the member that lets `batch_analyze` compile.)

### Recommendation (surface for Cowork + user — do NOT act here; this step is read-only and gated)

- **Before Phase 2 (hard blockers):**
  1. **Fix the build break.** Commit the orphaned `keymodesequence.{h,cpp}` `tpcKeyFitWeight` definition
     that pairs with the already-committed `batch_analyze.cpp` consumer (it sits in `stash@{0}`, entangled
     with larger WIP — needs a clean split), **or** back out the `batch_analyze.cpp` consumer hunk from
     `5f6b9828a5`. Feature defaults to `0.0` (committed pitch-class emission, byte-identical), so either
     direction is behavior-neutral. This belongs to the L3/L4 author, not this read-only step.
  2. **Decide the working-tree premise discrepancy** (§0): Cowork saw an empty `git diff`; CC saw 2457
     lines of production WIP. Establish which tree Phase 2 builds on.
- **Documentation correction (user-ratified, (b)):** update CLAUDE.md's gate identity tables from
  57/23/57 to **53/24/53** with the case sets in §2, citing the already-ratified L3-wiring delta; and
  correct/footnote the "both suites green" claim.
- **Notation 5 failures — triage separately:** pre-existing, not from current work. Determine whether the
  expectations are stale/aspirational (e.g. `5299f20964`'s "G→Gm" target the production doesn't yet reach)
  or a genuine uncaught key/mode regression from the Stage-4b commits. They block "both green" but are
  orthogonal to the Phase 2 build/BIR gate.

**Bottom line:** Phase 2 should **not** build on `0b42096d75` as-is. The tree does not produce a buildable
BIR harness, the documented gate numbers are wrong (should be 53/24/53), and there are 5 pre-existing
notation failures — none caused by Phase 1a, all requiring a decision before Phase 2 proceeds.

---

## §5 — Constraints honored / tree state

- Read-only: **no** code edit, **no** golden refresh, **no** code commit, **no** push. The only writes
  are this report (gitignored, `/cc_*.md`), the per-preset corpus regen under `tools/corpus/` (the tool's
  normal clean-slated output), and a scratch build wrapper + saved diff under the session scratchpad.
- Phase-1a commit `0b42096d75` untouched and unpushed.
- Stashed WIP from §0: **restored** — `git stash pop` reapplied all 23 tracked-dirty files cleanly
  (stash `917487da`, now dropped). The working tree is back to its exact as-found state. A standalone
  copy is also at scratch `uncommitted_tracked.diff` for traceability.
- Final HEAD: `master` @ `0b42096d75` (restored from the temporary detached-HEAD checkout of `48909fb752`
  used only for the §2/§3 measurements).
- **NOTE for Phase 2:** the as-found dirty tree (now restored) is the only state in which `batch_analyze`
  builds — the WIP supplies the missing `tpcKeyFitWeight` member. A clean checkout of HEAD does not build
  the BIR harness (see §1/§4). Do not assume HEAD is buildable for BIR without the build-break fix.

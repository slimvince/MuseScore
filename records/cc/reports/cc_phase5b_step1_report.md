# CC — Phase 5b Step 1: build G1 — commit / inherit / abstain + sufficiency gate (the lever)

**Commit (local, unpushed):** `f21273ce3b` — `feat(composing): L4 G1 — commit/inherit/abstain + sufficiency
gate (Phase-5b Step 1, dormant)`. `git show --stat` lists exactly **three** files: `chordslicedecoder.cpp`,
`chordslicedecoder.h`, `decode_chord_tests.cpp` — decoder + tests only, **no production wiring**. (The
working-tree change to `cowork_phase5b_l4_build_plan.md` is the Step-0 grounded-order doc edit — *not mine*,
left uncommitted in the working tree; it is excluded from this commit.)

**Method:** INVESTIGATE-confirm (§1) → BUILD G1 dormant (§2) → RE-MEASURE new-vs-legacy (§3) → ASSESS (§5).
Build-it-right per the signed spec (`cowork_layer4_chordsymbol_design.md` §4 step 3 / §5 step 4); no
inference-quality tuning (the leading-tone firewall untouched). `upstream` untouched.

---

## TL;DR

1. **The §1 build map is clean — no STOP.** The sufficiency gate's chord-tone source is the chosen candidate's
   **own template-tone presence** (`bassIsTemplateChordTone` over the focal pcs), computable **independent of
   the G2 membership rule**. Inherit source (`prevailing`) and the abstain representation (a `decision` enum +
   `hasChord=false`, distinct from the margin `uncertain` flag) both map cleanly. G1-before-G2 order holds.
2. **G1 built dormant** in `chordslicedecoder` (decoder production-dead): the commit / inherit / abstain
   trichotomy + the ≥3-template-tone sufficiency gate. One `analyzeChord` cube, decision logic on the existing
   ranking — no second scorer.
3. **Production byte-identical (§4 gate PASSED).** Baroque `.ours.json` **353/353 byte-identical** to the
   committed corpus (empirical), `composing 834`, `notation 53`, `pipeline_snapshot_tests 11/11 zero-diff`
   (no goldens refreshed). The decoder is referenced only by `batch_analyze --decode-chords` (returns before
   `analyzeScore`) — confirmed by grep; it is **not** on the live path. Corpus gate **53/24/53 unchanged**.
4. **G1 closed the ENTIRE −15 and surpassed legacy (§3).** Per-slice dur-weighted chord-root **58.4 % → 77.0 %**
   (Baroque AND Default), now **+3.2 / +3.4 pts ABOVE** the legacy per-region baseline (was −15.5 / −15.2).
   Phantom-root misses **1150 → 147 (−87 %)**, thin-slice misses **1186 → 45 (−96 %)**. **The sequence holds —
   proceed to Step 2 (membership G2/G3).** One honest caveat (§3): the +3.2 is accuracy *among the slices G1
   commits*; G1 now **abstains ~53 % of the scored duration** (the "don't guess" tradeoff) — coverage-matching
   is the Step-M engage question, not a Step-1 blocker.

---

## §1 — INVESTIGATE-confirm (the incremental check — build maps cleanly, no STOP)

Read the spec's G1 (`cowork_layer4_chordsymbol_design.md` §4 step 3, §5 step 4) against the as-built
`chordslicedecoder` (commit `9ef7ff312a`). All three required hooks map cleanly:

- **Sufficiency-gate chord-tone source — CONFIRMED independent of G2 (no STOP).** The ≥3-chord-tone gate counts
  the **candidate template's own chord tones present in the slice** via
  `function::bassIsTemplateChordTone(rootPc, tiePriority, pc)` (the `kMasks` table,
  `harmonicfunctionlayer.cpp:183`) — the same one chord-tone oracle the decoder already reuses
  (`isChordToneOfAny`, `classifyMembership`). Counting the distinct focal pcs that are template tones of the
  chosen candidate is a **structural-presence** count: template tones are *always* chord tones (membership never
  removes them), so the count does **not** depend on the G2 extra-note classification (the flat
  weak-OR-stepwise rule). The spec's "after membership has removed the non-chord tones" wording is satisfied by
  counting template tones only — the extras membership reclassifies are *added notes* (6th/9th), which do not
  count toward a complete-triad's-worth anyway. → **G1-before-G2 order holds; sufficiency does not need the
  correct membership first.**
- **Inherit source — CONFIRMED available.** "Prevailing chord" = the previous committed slice's `chosen`, already
  threaded through `decodeWindowed`/`finalizeSlice` as the carried `prevailing` (`if (sc.hasChord) prevailing =
  sc.chosen`), updated on commit/inherit and carried across abstains. It is in scope at the decision point in
  both decode paths.
- **Abstain representation — CONFIRMED distinct.** Today only a margin-only `uncertain` bool exists (every slice
  is still *named*; Step-0: `namedSlices == slicesTotal`). I added an explicit `enum class SliceDecision {
  Commit, Inherit, Abstain }` + a `decision` field, and represent abstain as **`hasChord=false`** (the no-chord /
  open marker), which the existing `--decode-chords` emission already gates `rootPitchClass` on (so the grader
  drops abstained slices from the denominator — no tooling change needed). The margin `uncertain` flag stays as
  one *input* to the decision, no longer the decision itself.

---

## §2 — BUILD G1 (dormant — `chordslicedecoder`, production-dead)

All changes in `chordslicedecoder.{h,cpp}`; one `analyzeChord` cube, decision logic on the existing candidate
ranking (no second scorer). Per the spec:

- **Sufficiency gate** — `ChordSliceDecoder::templateTonePresenceCount(chord, focal)` counts the distinct focal
  pcs that are template tones of the chord. `applyCommitDecision` commits only when `present >=
  sufficiencyChordTones` (default **3**, a complete triad's worth) **and** the margin clears (`!uncertain`).
- **Inherit** — when sufficiency fails but the slice's notes are **all** template tones of the prevailing chord
  (`notesConsistentWithPrevailing`, the **Step-1 conservative template-only** reading — covers the spec's
  documented inherit cases: the single-C♯-over-A-major thin slice whose C♯ is the third, and the dyad subset of
  the prevailing chord), `chosen` is replaced by the prevailing chord and carried forward. *The "... or a
  stepwise embellishment of it" relaxation depends on the membership stepwise machinery and is deferred to the
  G2 increment (Step 2), keeping G1 decoupled from the still-flat membership ladder.*
- **Abstain** — any other slice (insufficient with no consistent prevailing, **or** sufficient but low margin,
  **or** no scorable candidate): `hasChord=false`, `uncertain=true`, `decision=Abstain`; the ranked competing
  readings (`alternatives`) are kept for Layer 5.
- **Master switch** `enableCommitDecision` (default true). OFF reproduces the pre-G1 always-commit behaviour
  EXACTLY (the A/B lever). `applyCommitDecision` is wired into both decode paths (membership two-pass
  `finalizeSlice` — decided *before* membership classification so the per-note split reflects the final chord —
  and the `enableMembership=false` pass-1 path).
- **Decision/membership order:** decideSlice (rank) → applyCommitDecision (G1) → classifyMembership(final
  chosen). On abstain, membership is skipped (no committed chord).

**Honest scope notes recorded in the source:**
- `redecodeRange` exactness is now bounded under inherit (the chosen chord depends on the carried prevailing
  chain); the existing `first=1` test remains exact (the chain seeds from the piece start). Documented in the
  `.h`; a deep `first` mid-inherit-run is only reproduced to the one-slice look-back. Flagged, not expanded
  (unbounded chains) — not Step-1's focus.
- The stale `.h` "INCREMENT A only / membership STUBBED EMPTY" header comment (Step-0 doc-drift flag) is
  corrected to the as-built A+B+G1 state in the same commit.

**New unit tests** (`decode_chord_tests.cpp`, +8 — composing 826 → 834):
`G1_TemplateTonePresenceCount` (sufficiency source: triad→3, extra note doesn't count, dupes once),
`G1_CleanTriadCommits`, `G1_PhantomRootAbstains` (<3 template tones, no prevailing → abstain, hasChord=false,
readings carried), `G1_ThinSliceInheritsPrevailing` (lone C♯ over A major → inherit A), `G1_ThinSliceForeign
ToPrevailingAbstains`, `G1_SufficientButLowMarginAbstains` (sufficient but margin fails → abstain, not commit),
`G1_DisabledReproducesAlwaysCommit`, `G1_DecodeDecisionConsistentWithHasChord` (end-to-end invariant: Abstain ⟺
no committed chord). The existing `Fixture_CompleteCandidateListSurfacedAndRanked` "alternatives ≤ chosen" check
is gated on `decision==Commit` (an inherit replaces chosen with the prevailing chord, which may score below an
alternative).

---

## §3 — RE-MEASURE (the assess-for-amendment checkpoint)

Same Step-0 harness: `--decode-chords` over the 353-stem corpus (Baroque + Default), graded held-out (TEST split,
md5(stem)%100<20), dur-weighted = the granularity-comparable line. **BEFORE** = the Step-0 always-commit decode
(`tools/corpus_decode_chord_step0`); **AFTER** = the G1 decode (fresh, scratch driver — F-6 path fix applied).
Graders: `cc_layer4_chord_baseline.py`, `cc_layer4_residual_decompose.py` (committed, unchanged).

### Chord-root, dur-weighted (TEST split)

| dur-wt chord-root | Baroque BEFORE | Baroque AFTER | Default BEFORE | Default AFTER |
|---|---|---|---|---|
| per-region **legacy** baseline | 73.8 % | 73.8 % | 73.6 % | 73.6 % |
| per-slice **decoder** | **58.4 %** | **77.0 %** | **58.4 %** | **77.0 %** |
| **Δ (decoder − legacy)** | **−15.5** | **+3.2** | **−15.2** | **+3.4** |

**G1 closed the entire −15 deficit and went +3.2 / +3.4 ABOVE legacy.** (Decoder preset-identical Baroque≡Default,
as Step-0 — it scores null-context vertical only.)

### Phantom-root / thin-slice rates (the §5 lever signal) — Baroque (Default identical)

| over ALL misses | BEFORE | AFTER | absolute Δ |
|---|---|---|---|
| total misses | 2815 | 678 | **−2137 (−76 %)** |
| **phantom root** (root∉own notes) | 1150 (40.9 %) | **147** (21.7 %) | **−1003 (−87 %)** |
| **thin slice** (≤2 named chord-tones) | 1186 (42.1 %) | **45** (6.6 %) | **−1141 (−96 %)** |
| wrong root (root∉GT chord-tones) | 1698 (60.3 %) | 436 (64.3 %) | −1262 (−74 %) |
| share-tone / function (root∈GT) | 503 | 80 | −423 |

The phantom-root + thin-slice residual Step 0 named as "the −13 pt deficit" is **gutted in absolute terms**
(−87 % / −96 %). The remaining 678 misses are dominated by genuine **wrong-root COMMITS** (436) — slices that
passed sufficiency+margin and still mis-rooted: Layer-5 / membership-refinement territory (Step 2+), **not** the
phantom-root defect G1 targets.

### Coverage tradeoff (reported transparently)

G1 trades coverage for accuracy by design (commit where it can, abstain where it cannot → Layer 5). Dur-weighted
scored coverage (Baroque): per-slice **1 928 640 → 908 040 ticks** (the decoder now **abstains ~53 % of the
scored duration**). Of the dropped duration, ~1.39 : 1 was *wrong* : *right* — G1 preferentially abstains on
duration it would have mis-named. So the +3.2 is accuracy *among committed slices*, **not** coverage-matched
against the full-coverage legacy baseline. **Coverage-matched comparison is the Step-M engage GO/NO-GO question**,
not a Step-1 measure — flagged here so the engage decision accounts for it.

---

## §4 — Gate (all PASSED)

- **Production byte-identical:** Baroque `.ours.json` **353/353 byte-identical** to the committed
  `tools/corpus/baroque` (fresh regen + `cmp`); `pipeline_snapshot_tests 11/11 zero-diff` (no goldens
  refreshed — the live P1–P4 path is unchanged on the 10-score corpus); `composing 834/834`, `notation 53/53`.
  Decoder confirmed production-dead by grep (only `batch_analyze --decode-chords`, which returns before
  `analyzeScore`; **not** referenced by `regionanalyzer`/`sectionanalyzer`/the notation bridge). → corpus
  **53/24/53 unchanged** (Default/Jazz follow by the same production-dead, preset-agnostic structural argument).
  **No production movement.**
- **New unit tests** for sufficiency / inherit / abstain (oracle-asserted): present (+8, all green).
- **Build green:** clean build, only pre-existing warnings.

## §5 — ASSESS (does the sequence hold? — YES)

- **Expected (plan §5):** G1 closes **most** of the −15 (phantom-root + thin-slice rates drop sharply).
- **Measured:** G1 closed **all** of the −15 and surpassed legacy by +3.2/+3.4; phantom −87 %, thin −96 %
  (absolute). This **exceeds** the prediction. **The grounded order holds — G1 is the lever Step 0 identified.**
- **→ Proceed to Step 2 (membership three-tier ladder + plausibility check, G2/G3).** The remaining miss mass
  (wrong-root commits + the deferred stepwise-embellishment inherit relaxation) is exactly the G2 target. No
  amendment to the spec or the layer decomposition is indicated.
- **Caveat carried forward to Step M (not a Step-1 issue):** the +3.2 is accuracy among committed slices; the
  engage decision must use a coverage-matched comparison (G1 abstains ~53 % of duration). The abstained slices
  are the "uncertain" hand-off to Layer 5 by design.

## §6 — Stops honored
- Sufficiency did **not** need G2 membership first → no STOP (§1 confirmed independent).
- No production movement → no STOP (§4 byte-identical).
- G1 closed the −15 → no STOP (§5 sequence holds).
- No `upstream` push; commit is **local, unpushed** (`f21273ce3b`); decoder + tests only.

## Artifacts (gitignored / untracked, under `scratch_artifacts/`)
- AFTER decode JSONs: `scratch_artifacts/corpus_decode_chord_g1/{baroque,default}` (353/353 each).
- Grading logs: `grade_g1_{before,after}.log`, `decompose_g1_{before,after}.log`.
- Production byte-identity: `corpus_ours_check/baroque` (regen) + 353/353 `cmp` match.
- Scratch decode driver (F-6 path fix): `scratch_artifacts/decode_g1_driver.py`.

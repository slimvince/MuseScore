# CC report — Engage arc #3b: Gate A promotion unification (the BUILD event)

> **Nature.** Build event. One revertible, provenance-stamped `feat(composing):` commit implementing the
> ratified arc-#3 design (`cowork_gateA_unification_design.md` §Task 3/§Task 4). Full-surface byte-identity
> proven at objects (winner AND `alternatives[]`) across all 352 scores × 3 presets. Both regression stops
> green. Suites pass, no golden refresh. Layer 4 only (#7).
>
> **Provenance.** Dispatch `cc_instruction_engage_gateA_unification_build.md` (Cowork, 2026-07-06). Base HEAD
> `1c8ed4b5a3` (= `b0acb5c436` binary — arc #4 was docs-only, `git diff --stat b0acb5c436 HEAD` shows no
> `src/`). Corpus `c50002fee1` (pinned, non-stale). feat commit **`200681a855`**.

---

## 1. What was built (Layer 4 only)

**One promotion primitive replaces the ad-hoc idioms + the three duplicated builder lambdas** (⛔ total
unification / #6; one path per concern):

- **New** `promoteToWinner()` (`chordanalyzer.h` decl / `postscoringgates.cpp` def) — owns both idioms:
  - Idiom A (present-first): swap an already-carried reading to the winner slot (reuse-in-place, no growth,
    no duplicate).
  - Idiom B (append-built): else build the target **once** via the single wrapper `buildResultFromGateCtx()`
    over `buildChordResult()`, append, swap to front.
  - `presentHint` ∈ {concrete index | `kPromotePresentScan` | `kPromoteAppendOnly`}; `stopBelowThreshold` =
    the FM2 inclusion policy; `target.quality == Unknown` = any quality.
- **Enharmonic Major-add6 → Minor7 flip = ONE `promoteToWinner` call** (`presentHint = bestAltIdx`,
  `stopBelowThreshold = true`). The present branch reproduces **Gate A**'s `std::swap(results[0],
  results[bestAltIdx])` (it swaps that exact index iff it is the Minor at `(root+9)%12`); the append branch
  reproduces **FM2**'s above-threshold `rawCandidate` pull. Byte-identical **by construction**.
- **Gate E** → primitive present branch (`presentHint = bestAltIdx`; append unreachable — the guard already
  proves the target present).
- **G-family (G-E / G-D)** → restructured: the key-context test reads only `gExpectedAltRoot` (not the
  object), and the former "scan results[]; else pull from `rawCandidates`; else pop the phantom if no
  sub-gate fires" is exactly the primitive's present-first-else-append with its no-promotion (return-false)
  path (`presentHint = kPromotePresentScan`, `stopBelowThreshold = false`).
- **Iter 91 bass-root pull** → primitive append-built (`presentHint = kPromoteAppendOnly`, any quality, no
  threshold) — reproduces the former direct first-`rootPc==bassPc` pull.
- **Initial build** in `applyHarmonicFunction()` now calls `buildChordResult()` directly (the third builder
  lambda collapsed).

**Retired:** the separate `GateA` §6 rule — `PostScoringRule::GateA` (`paramoverride.h`), its name-map entry
(`paramoverride.cpp` `ruleNameTable`), its `!ruleOff(GateA)` guard. The surviving rule name for the whole
flip is **FM2** (O-11 retirement condition met: the primitive reproduces Gate A's carry byte-for-byte on the
present branch). `PostScoringRule` count 10 → 9.

**Reuse-vs-new / what retires (⛔ total unification):**
| item | before | after |
|---|---|---|
| builder wrappers | 3 duplicated lambdas (postscoringgates / chordpostpasses / harmonicfunctionlayer) | 1 wrapper `buildResultFromGateCtx` (inside the primitive) + direct `buildChordResult` in the initial build |
| promotion idioms | ad-hoc swap-existing + append-built, per-site | 1 primitive `promoteToWinner` (both branches) |
| flip rule | GateA + FM2 (two rules, `if/else`-exclusive) | FM2 (one rule; Gate A retired) |
| §6 rules | 10 | 9 |

## 2. Doc-sync (#10, same commit)

`docs/scoring_model.md`: new **§6a** (the `promoteToWinner` primitive contract); the flip table row rewritten
(present-swap = former Gate A, append = FM2, under FM2); the G-family row (G-E/G-D via the primitive); the
"Gate A — retirement HELD" block replaced with "Gate A — UNIFIED"; execution-order line; disable-audit rule
list (9 rules); the `kHalfDimFirstInversionBonus` / G-E-threshold / outer-guard notes; the historical
"subsumed B/C/D" note; and the `buildChordResult` doc string (now "the single builder for the whole module").
The stale `chordpostpasses.cpp:128` comment ("mirrors … analyzeChord") was removed with the collapsed lambda.

Tests: `postscoringgates_tests` `GateA_DisabledDoesNotFire` → `FM2_DisabledDisablesPresentEnharmonicSwap`
(the present branch is under the FM2 guard); section-header comment updated; behavior fixtures kept (they pass
byte-identically). `paramoverride_tests` name-list 10 → 9 (GateA removed, `isKnownRuleName("GateA")` now
false) and `disable_mixed` `GateA` → `GateE`.

## 3. Verification — full output surface (#14/#15), at objects

**Full-surface whole-file byte-diff** (winner + `alternatives[]` = whole `.ours.json` bytes) of the new
binary vs the frozen HEAD corpus `tools/corpus/{baroque,jazz,default}` (= C_HEAD, corpus `c50002fee1`),
regenerated to a **scratch** dir (committed corpus untouched):

| preset | files compared | byte-diffs | missing | extra | result |
|---|---|---|---|---|---|
| baroque | 352 | **0** | 0 | 0 | IDENTICAL |
| jazz | 352 | **0** | 0 | 0 | IDENTICAL |
| default | 352 | **0** | 0 | 0 | IDENTICAL |
| **total** | **1056** | **0** | 0 | 0 | **BYTE-IDENTICAL** |

`C_unified == C_HEAD` on the FULL surface, **including the 36 Baroque scores** the design flagged. Net
user-visible delta = **zero** (#12 preserved). The by-construction design (present branch keyed to the
caller's `bestAltIdx`, append reproducing FM2) held — no residual diff to investigate.

**Batch stop** (`characterise_bir_false.py`, per-preset scratch dir): **52 / 24 / 52** genuine BIR=false —
matching the committed baseline; set-diff empty (guaranteed by byte-identity of the `.ours.json`).

**Robust stop** (the governing hard stop; `a8_rebaseline_measure.py --corpus-root <scratch>` →
`robust_stop_diff.py --candidate` vs committed `tools/robust_stop/`): **identity-PASS** —

| preset | runs (ref/cand) | class-(b) dur Δ | class-(a) dur Δ | added/removed |
|---|---|---|---|---|
| baroque | 6868 / 6868 | +0 (PASS) | +0 | 0 / 0 |
| jazz | 7036 / 7036 | +0 (PASS) | +0 | 0 / 0 |
| default | 6883 / 6883 | +0 (PASS) | +0 | 0 / 0 |

`a8` self-validated grid==oracle on every covered piece. OVERALL: **PASS**.

**Suites:** composing **1101/1101** (2 disabled); notation **53 + 4 skip**; pipeline_snapshot **11/11 — NO
golden refresh** (the design proved zero overlap with the 36; none moved). Build clean (exit 0).

**Committed reference untouched:** all generation/measurement ran against scratch dirs
(`…/scratchpad/gateA_verify/…`); `tools/corpus/` and `tools/robust_stop/` were not written.

## 4. SHAs

- feat (behavior + doc-sync): **`200681a855`** — `feat(composing): Unify Gate A + FM2 into the promoteToWinner
  primitive; retire the GateA rule`.
- fold (this report + STATUS/HANDOFF/design observation + instruction + info-loss-audit edits): the following
  `docs(cowork):` commit.
- Base: `1c8ed4b5a3` (= `b0acb5c436` binary). Corpus `c50002fee1`.

## 5. For Cowork to verify at objects

The byte-identity proof reproduces with (from a clean HEAD+feat build):
```
python tools/run_bach_preset.py --preset <P> --corpus-dir tools/corpus --output-dir <scratch>/cand/<p>
# byte-diff <scratch>/cand/<p>/*.ours.json  vs  tools/corpus/<p>/*.ours.json   -> 0 diffs (P in Baroque/Jazz/Default)
python tools/characterise_bir_false.py --corpus-dir <scratch>/cand/<p>          # 52/24/52
python tools/a8_rebaseline_measure.py --out-dir <scratch>/a8 --corpus-root <scratch>/cand
python tools/robust_stop_diff.py --candidate <scratch>/a8                        # identity-PASS
```

*CC, 2026-07-06. Engage arc #3b — the ratified build. Byte-identical total-unification (#6) that also closes a
latent information-loss path (#12). Cowork verifies the byte-identity proof at objects.*

# Phase 5c — Step 3 (Layer 5 / FUNCTION): the resolver + the §8 forward-override mechanism + the fine-grain override

> **Discipline:** Step 3 of `cowork_phase5c_l5_build_plan.md`, against the SIGNED contract
> `cowork_layer5_function_design.md` §5.5 + §5.7 + §8 + the §5.0 shared defs. Built **DORMANT** (two new units,
> no production consumer) → **byte-identical on production**. **Default constants only — firewall, no tuning (§4).**
> **Select, never re-derive.** This dossier is gitignored.
>
> **HEAD `44e83f2d47`.** Step-3 code `c5134a67ea`; §0 STATUS catch-up `91aa8e719c`; Step-3 STATUS entry `44e83f2d47`.
> Prior: `254e8c3b0e` (Step-2 amendment).

## 0. Result — GREEN, built, all gates pass

- **§0 sweep:** the Step-2 Cowork docs were **already committed** (`7845328d05` + `254e8c3b0e`, the amendment session) —
  nothing unstaged to commit. The only §0 action outstanding was the **STATUS catch-up** (the living doc lacked the Step-2
  record): committed `91aa8e719c` (`docs(cowork): Phase-5c Step-2 resolution + Step-3 prep`).
- **§2/§3 build + §5 tests** committed `c5134a67ea`. **§7 STATUS Step-3 entry** committed `44e83f2d47`.
- **Build clean** (all 11 targets link); **composing 912 → 936 (+24)**; **notation 53** (4 skipped, baseline);
  **pipeline_snapshot 11/11 — NO golden refresh** (the byte-identical proof). **Corpus 53/24/53 unchanged by
  construction** (no production reach).
- **§1 verdict:** the carried-reading contract, the resolver's evidence, and the §8 mechanism's inputs are all reachable
  and live; no kind's evidence unreachable; the §8 mechanism needs no back-edge → **no STOP.**

---

## §1 — INVESTIGATE-confirm (read-only) — GREEN, no STOP

### (a) The carried-reading contract per ambiguity kind — ✅ reachable AND populated

The L4→L5 forward-carry is declared in the **nested** namespace `mu::composing::analysis::chordslice`
(`chord/chordslicedecoder.h`) and is **live** (populated by the decoder, not a dead type):

| Contract element | Type / source | Populated by |
|---|---|---|
| The named open question + the two competing readings | `OpenQuestionLabel{question, ambiguity, readingA, readingB, hasReadingB}` (`chordslicedecoder.h:370`) | `ChordSliceDecoder::nameOpenQuestion` (`chordslicedecoder.cpp:851`) |
| The ranked alternatives | `SliceChord.alternatives` (`std::vector<ChordSliceCandidate>`, `:384`) | the decoder ranking |
| The ambiguity kind (all six) | `AmbiguityKind{InsufficientEvidence, TransitionVsContinuation, SymmetricRotation, ShareTone, RelativePair, CloseReading}` (`:339`) | `nameOpenQuestion` assigns **all six** (`chordslicedecoder.cpp:864/886/895/903/910/912/914/916`) |
| The composite confidence | `SliceConfidence{margin, sufficiency, membershipCleanliness, composite}` (`:357`) | `computeConfidence` (`:815`, `composite` = `min(...)` `:847`) |

The six §5.5 kinds map exactly to the six `chordslice::AmbiguityKind` values (transition→`TransitionVsContinuation`,
share-tone→`ShareTone`, relative-pair→`RelativePair`, close→`CloseReading`, insufficient→`InsufficientEvidence`,
symmetric-rotation→`SymmetricRotation`). The layer adds **no new kind** (§5.5).

### (b) The resolver's evidence — ✅ reachable

- **The progression model** (Step 1 `functionprogression`): `isLicensedProgression`, `isAppliedResolution`,
  `prevailingHarmonyIndex`, `establishedNextFunctionIndex` over a `Progression`. Consumed directly.
- **The cadence tonic-vote** (Step 2 `functioncadence`): `FunctionalCadence{tonicPc, tonicVote, type, minorMode}` from
  `detectFunctionalCadences`. Consumed directly.
- **The soft bass-scale-degree prior (§5.7):** not previously built; **buildable** from the existing
  `region::diatonicDegreeForRootPc(pc, keyFifths, keyMode)` + the region tonic — so §5.7 is in Step-3 scope (it is named
  for §5.5) and is built here, not deferred.
- **The neighbouring committed harmony:** the adjacent committed slices, via `establishedNextFunctionIndex` (next) + a
  backward scan for the previous committed slice (the previous-committed is **not** `prevailingHarmonyIndex(i)`, which for
  a committed slice returns `i` itself — corrected in the override).

### (c) The §8 override mechanism's needs — ✅ expressible, no back-edge

- **The confidence-weighted threshold** consumes the earlier layer's `SliceConfidence.composite` — present per slice.
- **A one-pass closure flag** is a per-decision-id ledger (`OnePassClosure`); **a localized forward recompute** is a
  forward sweep over the region's slice-index range. Both are expressible **without a back-edge** (forward-only) and
  **without a loop** (a re-entrancy guard refuses a nested recompute).

**No input unreachable; no kind's evidence missing; the §8 mechanism needs no structure beyond a dormant unit →
proceeded.**

---

## §2 — The resolver (§5.5), dormant — `function/functionresolver.{h,cpp}`

For each L4-abstained slice, **select among the carried readings** by the named kind — never re-derive, never invent:

- **transition** (`TransitionVsContinuation`) → the reading forming a **licensed progression INTO** the established next
  function (it "belongs to the arriving function"); else the reading **matching the prevailing harmony** (a passing/
  neighbour figure); else the §5.7 prior, else open.
- **share-tone** (`ShareTone`) → the reading that **participates in a licensed progression into the established next
  function**; else the §5.7 prior, else open.
- **relative-pair** (`RelativePair`) → the **cadence tonic-vote** for each candidate root (which centre receives the
  cadential arrival / phrase-final emphasis / raised LT — all carried by the authentic-cadence vote, §5.2); else the §5.7
  prior, else open.
- **close** (`CloseReading`) → **functional plausibility** (the §5.5 fixed-feature score: licensed-out-of-prevailing +
  licensed-into-next + cadential fit) with the deciding margin a firewall default; tie → the §5.7 prior, else open.
- **insufficient** (`InsufficientEvidence`) → the **same plausibility score**; where it does not separate (or
  `hasReadingB==false`), **carry the open mark** (§7).
- **symmetric-rotation** (`SymmetricRotation`) → the rotation that **resolves as a licensed applied/leading-tone chord
  into the next** (`isAppliedResolution(rotation, next)`), or that a **cadence pins** as its leading-tone chord (a cadence
  whose tonic sits a semitone above the rotation's root); else **carry the open mark** (the gate-policy class-(a), F1 rule)
  — do not guess.
- **Residual:** where the function evidence decides nothing → the **honest open mark** (`reading` = the top reading
  carried for display, `openMark=true`).

**§5.7 soft bass-scale-degree prior** (`degreeFunctionalBias` / `bassScaleDegreeBias`): 1̂/3̂→tonic, 2̂/4̂→pre-dominant,
5̂/7̂→dominant, 6̂/chromatic→none. Used **only** as the close/insufficient/relative-pair **tie-breaker** (prefer the tied
reading whose own root-degree function-class matches the slice's bass-degree bias), **never a gate**; an unbroken tie →
open mark.

**Selection, not re-derivation (verifiable):** every selected `reading` is one of `openQuestion.readingA/readingB`, the
ranked `alternatives`, or a neighbouring committed chord — the resolver never reads the raw notes nor synthesises a chord
the decoder did not carry (the D4 / §2 constraint).

---

## §3 — The §8 mechanism + the fine-grain override, dormant — `function/forwardoverride.{h,cpp}` (+ resolver)

### The shared §8 mechanism (built ONCE, reusable — Step 4 reuses it)

- **The threshold:** `overrideBar(c) = baseBar + confidenceScale·c` (monotone non-decreasing in the earlier layer's
  confidence c, clamped to [0,1]); `overrides(c, strength) = strength > overrideBar(c)` (**strictly greater** — at the
  exact bar the **incumbent holds**, the fixed tie-direction). So a well-founded confident commit demands decisively
  stronger contradiction than a borderline one.
- **The one-pass closure ledger** (`OnePassClosure`): `markFinal`/`isClosed`/`tryOverride` over an opaque decision id.
  `tryOverride` fires **iff not-already-closed AND the threshold crosses**, and on fire **marks the decision final** — so
  a decision is overturned **at most once** and **never re-targeted** in the pass.
- **The localized forward recompute** (`forwardRecompute(first, last, reread)`): a **single forward sweep** over the
  bounded slice range, **re-entrancy-guarded** (a nested `forwardRecompute` invoked from within `reread` returns −1 —
  "one localized forward re-run, never a loop" made structural); empty/inverted ranges return −1. **No back-edge** — it
  only invokes the `reread` callback, never upstream.

### The fine-grain override (§5.5 case-4 / §10) — in the resolver, firing through the §8 mechanism

For a slice with `decision == Commit` whose committed reading the established function/cadence contradicts: compute the
committed reading's plausibility vs the most-plausible **carried alternative or neighbouring committed chord**; the
**contradiction strength** = bestAlt plausibility − committed plausibility. Fire via
`closure.tryOverride(i, confidence.composite, strength)` (the §8 threshold scaled to the L4 commit confidence); on fire,
**SELECT** the corrected carried/neighbour reading (never re-derive), mutate the working progression to the corrected
fact, and run `closure.forwardRecompute(i+1, regionEnd, reread)` to re-read the downstream region (re-resolving its
abstains against the corrected harmony). The §8 closure guarantees the overturned commit is **not re-opened** in the pass.

### Build-detail decisions (declared, not assumed — §7b)

1. **Consume the `chordslice::` contract types directly** (not a parallel set of view types). They ARE the
   representational L4→L5 forward-carry built *for* L5 ("the L4→L5 abstain contract … so L5 selects among them"); §5.5
   fixes "no new ambiguity kind", so a duplicate enum/structs would be pure drift hazard. Brought into the analysis
   namespace via narrow **using-declarations** (the names are unique to `chordslice`, so benign even in the Unity chunk).
   Mirrors the `functionromannumeral` precedent (it includes `chordanalyzer.h` for `ChordIdentity`). The resolver still
   does NOT consume the decoder **engine** / region assembler / any score type — only the value structs + the already-built
   producer-agnostic views (`Progression`, `FunctionalCadence`), so it stays hand-injectable in tests.
2. **The fine-grain override fires on `decision == Commit` only** (the §5.5 case-4 "confidently *committed*" duty) — not
   `Inherit` (a deliberate carry-forward, not a fresh fine-grain commit) nor `Abstain` (case 2, the resolve path). The §8
   threshold (scaled to `composite`) handles the "confident" qualifier — a low-confidence commit has a low bar.
3. **Relative-pair's same-collection cues** (cadential arrival, raised leading tone, phrase-final emphasis) are consumed
   **through the authentic-cadence tonic-vote** (which already integrates the phrase-boundary salience + the LT-resolution
   gate), not via a separate note-level read inside this unit. Where the vote does not separate the two centres → the §5.7
   prior, then the open mark. (A fuller note-level same-collection read is a precision-phase refinement, not built.)
4. **The §5.7 prior is placed in the resolver unit** (exposed `degreeFunctionalBias`/`bassScaleDegreeBias` for the oracle
   test), not a standalone module — it has one consumer today; trivially extractable if the cadence detector later wants
   it.
5. **The fine-grain override's "neighbouring committed harmony" = the ADJACENT committed slices** (the previous committed
   chord via a backward scan + the established next function), **not** `prevailingHarmonyIndex(i)` (which for a committed
   slice returns `i` itself). The abstain resolver keeps `prevailingHarmonyIndex` (correct for a non-committed slice).
6. **Two Unity-build hygiene fixes** (declared so they read as deliberate, not accidental): the helper `norm` was renamed
   `normPc` (collides with `functioncadence.cpp`'s anonymous-namespace `norm` in the Unity chunk), and the two contesting
   readings are named `readA`/`readB` (single-letter `A`/`B` collide with a macro a system/Qt header pulls into the Unity
   chunk). Both are name-only; no behavioural content.

---

## §4 — Constants

All firewall **defaults**, **no tuning**:
- §8 `ForwardOverrideParams{baseBar 1.0, confidenceScale 1.0}` — only the **direction** is fixed (the bar is
  non-decreasing in confidence; strictly-greater tie-direction).
- §5.5 `FunctionResolverParams{wLicensedOut 1.0, wLicensedIn 1.0, wCadentialFit 1.0, decidingMargin 0.5}` + the §8
  threshold — only the directions are fixed (more licensed fit / cadential support ⇒ more plausible).

No threshold/weight/margin was tuned for accuracy.

---

## §5 — Tests (oracle-asserted) — +24

`tests/forwardoverride_tests.cpp` (11) — the §8 mechanism, asserted vs the §8 spec:
- the **threshold** scales with confidence (`overrideBar` monotone; bar(0)=1.0, bar(1)=2.0; clamped off-range); the
  **same contradiction (1.5) overturns a borderline inference but NOT a confident one** (the confidence-scaling
  property); the **tie-direction favours the incumbent** (strict `>`);
- the **one-pass closure**: `markFinal` idempotent per pass; `tryOverride` fires-then-closes so a second override on the
  same decision is **refused** (the §8 no-re-target); a sub-bar attempt does not fire **or** close;
- the **localized forward recompute**: sweeps the range once in forward order; rejects an empty/inverted range; a
  **nested recompute is refused (−1)** while the outer sweep is active (**never a loop**) and the guard clears after;
  a `tryOverride` against a closed trigger from inside the reread is **refused** (**cannot re-target**); `reset` starts a
  fresh pass.

`tests/functionresolver_tests.cpp` (13) — the resolver + override, asserted vs theory:
- the §5.7 **bass/root functional-bias mapping** (1̂/3̂→tonic, 2̂/4̂→pre-dom, 5̂/7̂→dom, 6̂/chromatic→none);
- **one resolution per kind:** share-tone (Am6↔F♯ø7) resolved to F♯ø7 by the licensed progression into V; transition
  resolved as the arriving function (D7 into V) **and** as a neighbour within prevailing (C continuing I); relative-pair
  (C↔Am) resolved to Am by the cadence tonic-vote; close (G vs A♭) by functional plausibility; symmetric-rotation
  (G♯/B/D/F dim7) pinned to G♯dim7 by the resolution into Am;
- the **open mark** (not a guess): an insufficient slice with no second reading; a symmetric rotation into a target
  **no rotation resolves into** (and no cadence pins);
- the **§5.7 prior** breaks an otherwise-exact tie (5̂ bass ⇒ the dominant-class root selected);
- the **fine-grain override**: a confident-but-contextually-wrong commit (A♭) is **overridden by selecting** the carried
  G (the §8 bar crossed at composite 0.5) — `overrodeCommit`, `reading.rootPc==G`, basis `FineGrainOverride`; the **§8
  closure holds** (`isClosed(1)`, a re-attempt refused, exactly one close, recompute unwound — **no recursion**); the
  **same contradiction does NOT fire on a maximally-confident commit** (composite 1.0 ⇒ bar 2.0, strength 2 not `>`);
  plain context-consistent commits **carry through unchanged** (L5 additive).

(All 24 green on the first full test run after the build fixes; no fixture re-shaping needed.)

---

## §6 — Gate — PASS (dormant + byte-identical)

| Gate | Result |
|---|---|
| Build | clean (`/tmp/build_step3c.log`; all 11 targets link, 0 `error C####`) |
| `composing_tests` | **936/936** (912 + 24; 2 disabled pre-existing) |
| `notation_tests` | **53** passed (4 skipped — baseline) |
| `pipeline_snapshot_tests` | **11/11** PASSED, **NO golden refresh** (3 disabled — baseline) |
| Corpus **53/24/53** | **unchanged by construction** — not re-measured (see below) |
| Production reach | **none** — grep of `src/` + `tools/` finds the new identifiers only in the 4 module files, the 2 test files, and the 2 CMakeLists |

**Why the corpus regen was not run** (the Step-1/Step-2 + session-9 precedent + CLAUDE.md scoping): the two new modules
have **no production consumer** (verified by grep), touch **no** scoring/gate/template code, and the pipeline snapshots
refreshed **zero** goldens — so P1–P4 output is byte-identical and the BIR gate cannot move. The corpus-regen gate is
scoped to gate/scoring changes; this is neither.

---

## §7 — Stops — none triggered

No resolver kind requires re-deriving (every path selects from the carried readings / neighbouring committed harmony);
the §8 mechanism needs no back-edge (forward-only sweep, re-entrancy-guarded) and no structure beyond a dormant unit; no
threshold/weight tuned (firewall); no production movement; no `upstream` touched.

## §7b — Note for Cowork (build-detail decisions to ratify)

The six decisions in §3 are surfaced for ratification rather than assumed — especially **(1)** consuming the `chordslice::`
contract types directly (vs a parallel view layer) and **(2)** scoping the fine-grain override to `decision == Commit`.
Two are pure Unity-build hygiene **(6)**. None tunes a constant or moves production. The resolver **only selects** (never
re-derives) and the §8 mechanism is **reusable** (Step 4's modulation recompute is its second instance) + **closure-safe**
(one-pass, forward, re-entrancy-guarded) — both verified by the §5 tests.

## Commits (local, unpushed)
- `91aa8e719c` — `docs(cowork): Phase-5c Step-2 resolution + Step-3 prep` (the §0 STATUS catch-up).
- `c5134a67ea` — `feat(function): L5 resolver + the §8 forward-override mechanism + the fine-grain override (Phase 5c Step 3, dormant)`.
- `44e83f2d47` — `docs(status): record session 11 — L5 Phase 5c Step 3 (...)`.

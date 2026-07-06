# Gate A promotion unification — design & scoping (engage arc #3)

> **Nature.** DESIGN + SCOPING pass, **read-only**. NO `src/` change, NO corpus write, NO build, NO push of a
> behavior change. The unification itself is a *separate*, user-ratified build event (it touches a
> load-bearing, user-visible output surface — the carried alternatives — on 36 Baroque scores). This document
> is the ratification surface: the source-grounded characterization, the measured blast radius on the FULL
> output surface (winner **and** alternatives), the single unified design, and the verification plan.
>
> **Provenance.** Cowork dispatch *Engage arc #3* (2026-07-06), the order-of-operations first step
> (restructuring → architectural design → algorithmic completion → inference-fixing). HEAD `71c0be114a`,
> branch `master`, fork-only, ahead 0. Corpus `c50002fee1` (pinned, non-stale). Both regression stops green
> at entry (batch 52/24/52; robust sandwich identity-PASS). Grounding finding: `cowork_stage5_fitter_design.md`
> **O-11** (the GateA byte-identity ruling, L990-999); measurement of record `cc_stage5_phase2_2c_report.md`
> (Task 1). **Evidence-method rule (binding):** inertness/impact is measured on the FULL output surface —
> **winner AND alternatives, never the winner alone.**

---

## Task 0 — state check

| item | value |
|---|---|
| HEAD | `71c0be114a` (docs-only since the R10-b fold; no `src/` or corpus change intervening) |
| branch / ahead | `master`, ahead 0, fork `origin = slimvince/MuseScore` |
| batch stop | 52/24/52, set-diff empty ×3 (per `tools/robust_stop/manifest.json` batch_stop block + STATUS) |
| robust stop | identity-PASS (class-(b) Δ=0 all presets) |
| corpus fingerprint | `c50002fee1` (`tools/robust_stop/manifest.json` → `provenance.corpus_git_hash`) |
| working tree | clean but for untracked scratch (`idiom_discovery/…`, `scratch_artifacts/`) — no tracked src change |

---

## Task 1 — the duplication at source

### 1.1 One real builder, three thin wrapper lambdas

There is exactly **one** chord-result builder **function**:

- **`buildChordResult(rc, ctx, prefs)`** — declared `chordanalyzer.h:590`, defined `chordanalyzer.cpp:911`.
  Doc string (h:585-593): *"Called from analyzeChord() (main result-building loop) and from
  applyPostScoringGates() (A-FM2 and G-E fallback cell promotion)."* This is the single normalizing builder
  (augmented-root correction, Sus→Major, extension detection, degree labelling). **It is already unified — it
  is not the duplication.**

The duplication is **three thin `buildResult` wrapper lambdas**, each capturing a local context and calling
`buildChordResult`:

| # | site (function) | file:line | input | context source | used by |
|---|---|---|---|---|---|
| 1 | `applyPostScoringGates` | `postscoringgates.cpp:65` | `RawCandidate` | `gateCtx.{pcWeight,tpcForPc,bassPc,bassTpc,keyTonicPc,keyMode,scale}` | FM2 (L229), Gate G-E raw-pull (L350) |
| 2 | `applyIter8691Pedal` | `chordpostpasses.cpp:129` | `RawCandidate` | **same 7 `gateCtx` fields** | Iter 91 promotion (L196) |
| 3 | `applyHarmonicFunction` | `harmonicfunctionlayer.cpp:516` | `WorkCand` → `toRaw()` | `snapshot`-derived `buildCtx` (same 7 fields) | main build loop (L527), guaranteed-inversion append (L545) |

Wrappers **#1 and #2 are byte-identical** — the same lambda body (same 7 `gateCtx` fields, same `prefs`, same
`buildChordResult` call) copied into two files. #3 is the same call reached through a `WorkCand`→`RawCandidate`
adapter (`toRaw`, `harmonicfunctionlayer.cpp:298`) and the equivalent snapshot-sourced context.

**Doc-staleness found (not fixed — read-only):** the comment at `chordpostpasses.cpp:128` says the lambda
*"mirrors the buildResult lambda in applyPostScoringGates / analyzeChord."* `analyzeChord` **holds no such
lambda** — it builds the `ScoringSnapshot` (`chordanalyzer.cpp:1491`) and delegates result-building to
`fn::applyHarmonicFunction(...)` (`chordanalyzer.cpp:1579`). The third real wrapper is in
`applyHarmonicFunction`, not `analyzeChord`. (The dispatch's "third `buildResult` mirror in
`applyPostScoringGates`/`analyzeChord`" resolves to wrapper #1; the analyzeChord half is stale wording.)

### 1.2 The two promotion idioms

A **promotion** re-ranks `results[]` so a chosen reading becomes the winner (`results[0]`). Two distinct
idioms are used ad-hoc across the promotion sites, with **no shared "promote to winner" primitive**:

**Idiom A — swap-two-existing** `std::swap(results[0], results[idx])`.
Promotes a reading **already present in `results[]`** by swapping it to the front. **No object is built; no
entry is added.** The carried set is a *permutation* — the demoted previous winner is retained in place
(its existing object, at `idx`), membership and object provenance unchanged.
- **Gate A** — `postscoringgates.cpp:214-219` (`std::swap(results[0], results[bestAltIdx])`).
- Gate E — `postscoringgates.cpp:255-266`.
- Gate G-E / G-D — `postscoringgates.cpp:366-373`, `381-387`.

**Idiom B — append-built-then-front** `results.push_back(buildResult(rc)); std::swap(results[0], results.back());`.
Pulls a reading **not in `results[]`** from `gateCtx.rawCandidates`, **builds a fresh object**, appends it, and
swaps it to the front. The carried set **grows by one freshly-built object**; the demoted previous winner is
pushed to the back.
- **FM2** — `postscoringgates.cpp:223-235`.
- Iter 91 — `chordpostpasses.cpp:191-199`.
- Gate G-E raw-pull variant — `postscoringgates.cpp:346-356`, with an explicit **phantom-pop cleanup**
  (`results.pop_back()`, L388-392) if no sub-gate ends up firing: *"remove the phantom alternative that was
  pulled from rawCandidates so it does not pollute results[]."* **The codebase already recognizes that a raw
  pull can pollute the carry and cleans up after itself here** — the principle exists; it is just not applied
  uniformly (FM2 has no such guard).

(Adjacent, not a post-scoring promotion: the initial build — `harmonicfunctionlayer.cpp:520-528` — pushes in
score order and relies on `results.front()` = winner ["push_back-then-rely-on-order"]; the guaranteed-inversion
diff-root append is `harmonicfunctionlayer.cpp:530-548`. Same wrapper duplication, different concern.)

The `RawCandidate` struct doc (`chordanalyzer.h:312-315`) states the design intent explicitly: it exists for
*"fallback paths (Gates A-FM2 and G-E) that may need to promote a cell not in the top-N results."* — i.e.
Idiom B is the "cell not carried" path; Idiom A is the "cell already carried" path. **Gate A and FM2 are the
two halves of one flip** (Major-add6 → enharmonic Minor7): Gate A when the partner is already in `results[]`,
FM2 when it is not. They are `if/else`-exclusive at HEAD — FM2 is gated on `!didEnharmonicFlip`
(`postscoringgates.cpp:224`), so on any cell where Gate A fires, FM2 does not.

### 1.3 Why the alternatives differ on the affected slices — the mechanical cause

On the affected slices (see Task 2) the partner **is** already in `results[]`, so **Gate A (Idiom A) fires**:
it swaps the existing partner object to the front and leaves the demoted Major-add6 winner object in the
alternatives (reuse-in-place). If Gate A is removed, the **retained FM2 (Idiom B) covers the identical flip**:
`!didEnharmonicFlip` is now true, FM2 scans `rawCandidates`, finds the same partner, and **builds a fresh
object** which it appends — so the carried alternatives now contain a freshly-built near-duplicate of the
*winner* instead of the distinct Major-add6 partner. **Same winner, different `alternatives[]`.** Object-level
verification of record (`cc_stage5_phase2_2c_report.md` Task 1, `bwv17.7`): *"GateA re-ranks via
`std::swap(results[0], results[bestAltIdx])` (reusing the existing `A6` result object in `alternatives[]`);
with GateA gone, the retained FM2 promotes the same winner via `results.push_back(buildResult(...))` — a
freshly-built object."* Re-confirmed at HEAD in Task 2 below.

---

## Task 2 — blast radius on the FULL output surface

**Method.** Read-only decode with the HEAD binary (`ninja_build_rel/batch_analyze.exe`, no rebuild), Baroque
preset, `--param-override "disable_rule GateA"` (≡ Gate A deletion — 2.2c-established equivalence), written to
a **scratch** dir (frozen `tools/corpus/` untouched). Compared against the frozen `tools/corpus/baroque`
(= C_HEAD, Gate A ON, byte-validated current at HEAD). Winner surface = `WINNER_KEYS`
(`startTick, rootPitchClass, chordSymbol, quality, romanNumeral, bassPitchClass, bassIsRoot, chordScore, key`);
full surface = whole `.ours.json` bytes (winner + `alternatives[]`).

**Result — reproduces the 2.2c count exactly, now enumerated by name:**

| surface | Baroque | reading |
|---|---|---|
| whole-file byte-diff (C_HEAD vs Gate-A-removed) | **36 / 352** | the affected set |
| **WINNER-only diff (all 352)** | **0** | **winner-inert on the FULL set — every diff is `alternatives[]`-only** |
| Jazz / Default | 0 / 0 (2.2c recorded; Gate A is `preferMinorOverMajorAdd6`-gated, Baroque/Standard only) | non-Baroque unaffected |

**The 36 affected Baroque stems** (exact, this pass):
`bwv126.6, bwv139.6, bwv145.5, bwv17.7, bwv177.5, bwv178.7, bwv244.40, bwv245.22, bwv245.40, bwv248.5,
bwv296, bwv297, bwv300, bwv301, bwv310, bwv319, bwv323, bwv325, bwv346, bwv355, bwv356, bwv365, bwv379,
bwv383, bwv389, bwv390, bwv398, bwv40.6, bwv40.8, bwv405, bwv424, bwv437, bwv60.5, bwv64.4, bwv78.7, bwv85.6`.

**The carried-alternatives delta (content, not just count).** Sampled across the set — the pattern is uniform.
On each affected slice the winner is a Minor7 slash chord and the demoted reading is its enharmonic
Major-add6 partner (`(winnerRootPc+9)%12`):

```
bwv17.7 @19680   winner (6, F#m7/A)   BASE alts [A6, A6, A6]     CAND alts [A6, A6, F#m7/A]
bwv300  @26400   winner (11, Bm7/D)   BASE alts [D6, D6, D6]     CAND alts [D6, D6, Bm7/D]
bwv40.6 @5760    winner (7, Gm7/Bb)   BASE alts [Bb6, Bb6, Bb6]  CAND alts [Bb6, Bb6, Gm7/Bb]
bwv379  @6720    winner (9, Am7/C)    BASE alts [C6, C6, C6]     CAND alts [C6, C6, Am7/C]
bwv60.5 @30960   winner (6, F#m7/E)   BASE alts [A6, A6, A6]     CAND alts [A6, A6, F#m7/A]
```

- **BASE (C_HEAD, Gate A / Idiom A):** the alternatives retain the distinct enharmonic **Major-add6 partner**
  (`A6`/`D6`/`Bb6`/`C6`) — reuse-in-place of the demoted winner object.
- **CAND (Gate A removed, FM2 / Idiom B):** the last alternative slot is overwritten by a **freshly-built
  Minor7 near-duplicate of the winner** (`F#m7/A`, `Bm7/D`, …) — the append pollutes the carried readings with
  a copy of the winner and displaces the distinct partner reading.

**Confirmations for the build event:**
- **Winner (and therefore root) unchanged on every score** (0 winner-diffs / 352). Both regression stops are
  root-based ⟹ they stay green **by construction** under any carry-only change.
- **The delta is a content difference in the carried set** (a distinct partner alternative replaced by a
  winner near-duplicate), not merely cosmetic re-ordering. It is confined to `alternatives[]` of the standard
  `.ours.json` — the L5-consumed carry surface.
- **Snapshot reach: none.** The 11 pipeline-snapshot corpus stems (`bach_bwv806_*`, `bach_chorale_001/003/137`,
  `chopin_bi105_*`, `corelli_op01n08a`, `mozart_k279_1`, `mozart_k280_1`, `schumann_kinderszenen_n01`) do **not**
  intersect the 36 `bwv###` scores. No golden can move even under the naive removal; a fortiori none moves under
  the unification (which reproduces C_HEAD — Task 3).

---

## Task 3 — the single unified promotion path (Layer 4, in-layer)

### 3.1 Which carry is correct — grounded, not assumed

The carried alternatives are a **load-bearing output surface**: per the L4 §15 **O1b carry contract**
(`cowork_stage5_fitter_design.md:991-992`), **L5 overrides select among the carried readings**, and E-14 makes
them user-visible. The carry's purpose is therefore to present the **complete set of distinct readings** L5
may choose among.

Measured against that purpose (Task 2 content):
- **C_HEAD (Idiom A / Gate A's swap)** retains the distinct enharmonic **Major-add6 partner** as an
  alternative. This is a genuinely different reading (different root/quality) that L5 may legitimately select.
- **C_delete (Idiom B / FM2's append)** injects a **near-duplicate of the winner** into the carry and
  **displaces** that distinct partner. A copy of the winner is **not a distinct reading** — it cannot be a
  meaningful L5 choice, and its presence *loses* the partner reading (a §12 information-loss regression).

**Grounded verdict: C_HEAD is the correct carry.** It is the same principle the code already applies at the
Gate G-E raw-pull, where a non-promoting pull is popped so it *"does not pollute results[]"*
(`postscoringgates.cpp:388-392`). The correct unification reproduces C_HEAD — it does **not** adopt the
FM2-append form. (This is not "pick Gate A's idiom because Gate A is at HEAD"; it is "pick the carry that
preserves the distinct readings the contract requires, which the swap idiom produces and the append idiom
destroys.")

### 3.2 The unified path

**One promotion primitive (new, chord-layer).** A single helper — `promoteToWinner` — owns both branches
behind one contract, replacing the ad-hoc idioms and the wrapper lambdas:

```
promoteToWinner(results, rawCandidates, target, buildCtx, prefs):
    // target identifies a reading (rootPc, quality[, bass]) to make the winner.
    if target is already present in results[] at index j:
        std::swap(results[0], results[j])          // Idiom A — reuse existing object, no growth
    else if target is findable in rawCandidates above threshold:
        // Idiom B — build ONCE via the single wrapper, but present-first:
        //   never append a reading already carried (the dedup guard).
        results.push_back(buildResultFromGateCtx(target_rc, gateCtx, prefs))
        std::swap(results[0], results.back())
    // postcondition: winner == target; previous winner retained exactly once;
    //   NO duplicate of any already-present reading; single build path.
```

The **present-first dedup guard** is the whole fix: it makes the append branch fire **only** when the target is
genuinely absent, so an already-carried partner is *swapped* (clean, Idiom A) rather than *appended* (duplicate,
Idiom B). For the enharmonic flip specifically, the caller already computes the in-`results[]` partner index
(`bestAltIdx`, from the clean-quality bestAlt loop, `postscoringgates.cpp:136-187`); the primitive swaps that
exact index — so the produced permutation is **byte-identical to Gate A's `std::swap(results[0],
results[bestAltIdx])`**.

**One builder wrapper (collapse the triplication).** The two byte-identical `gateCtx` wrappers
(`postscoringgates.cpp:65`, `chordpostpasses.cpp:129`) collapse into a single free function
`buildResultFromGateCtx(rc, gateCtx, prefs)` in the chord layer; `applyHarmonicFunction`'s `WorkCand` variant
reaches the same function after `toRaw()`. The promotion primitive owns the builder call, so the wrapper
lambdas disappear from the three call sites. `buildChordResult` (already the one normalizing builder) is
unchanged.

**Sites re-pointed to the primitive:** Gate A + FM2 (the two halves of the enharmonic flip →
one `promoteToWinner` call with present-first internal branching), Iter 91 (`chordpostpasses.cpp:191-199`),
and the Gate G-E raw-pull (`postscoringgates.cpp:346-356`, whose phantom-pop becomes the primitive's absent-and-
not-promoted path). Gate E / G-D (pure Idiom-A swaps of an existing index) route through the primitive's
present branch. The initial build (`harmonicfunctionlayer.cpp:520-548`) keeps its score-ordered push but shares
the collapsed builder wrapper.

### 3.3 How Gate A becomes truly inert and removable

Once the flip is one `promoteToWinner` call with present-first branching, **Gate A (the "partner present" half)
and FM2 (the "partner absent" half) are the two internal branches of the same promotion.** The separate `GateA`
rule — its `PostScoringRule::GateA` enum member (`paramoverride.h:75`), its `ruleOff(GateA)` guard
(`postscoringgates.cpp:214`), its name-map entry, and its dedicated fixtures — is redundant: the unified
promotion *is* the flip. Because the primitive reproduces Gate A's swap **byte-for-byte** on the "present"
branch (same `bestAltIdx`, same `std::swap`), removing the `GateA` rule leaves **winner AND carry
byte-identical to HEAD**. That is the condition O-11 named for retirement: *"It retires when the promotion
machinery unifies (one promotion path producing one carry)."* Gate A is then inert on the **full** surface
(not merely winner-inert) and removable. The retained rule name for the flip is **FM2** (already
RETAIN-as-structural, `cc_stage5_phase2_2c_report.md` §Task-1g) — or a single renamed unified rule; **exactly
one** name survives.

### 3.4 Layer discipline

All of this is **Layer 4** (chord-root selection / carry machinery). The promotion sites live in
`src/composing/analysis/chord/` (`postscoringgates.cpp`, `chordpostpasses.cpp`) and the build in
`src/composing/analysis/function/` (`harmonicfunctionlayer.cpp`); `buildChordResult` is already a chord-layer
utility (`chordanalyzer.h`) called by the function layer. The new primitive + collapsed wrapper are chord-layer
utilities in the **same** files/headers. **No new cross-layer dependency is introduced** — the change
*consolidates* existing intra-module calls. Nothing in L1/L2/L3/L5 is touched.

---

## Task 4 — the build-event plan + the ratification surface

*(The build event is a SEPARATE, user-ratified commit — NOT built in this pass.)*

### 4.1 What the refactor touches (all Layer 4)

- **New:** `buildResultFromGateCtx(...)` (one wrapper) + `promoteToWinner(...)` (one primitive) — chord-layer,
  declared in a chord header, defined once.
- **Re-pointed call sites:** the enharmonic flip (Gate A + FM2 → one `promoteToWinner`), Iter 91
  (`chordpostpasses.cpp`), Gate G-E raw-pull, Gate E / G-D swaps; the `applyHarmonicFunction` build shares the
  collapsed wrapper.
- **Retired:** the `GateA` rule — `PostScoringRule::GateA` (`paramoverride.h`), `ruleOff(GateA)`
  (`postscoringgates.cpp`), the name-map entry, the pure-GateA fixtures (2.2c: 5 GateA fixtures were restored at
  un-retire; the FM2 fixtures **stay**), and its `docs/scoring_model.md` §6 line. `docs/scoring_model.md` synced
  in the same commit (mandatory §-sync rule).

### 4.2 Verification on the FULL output surface

- **Winner + alternatives byte-diff across all 352 scores × 3 presets.** **Expected: byte-identical
  everywhere, including the 36** — the present-first primitive reproduces Gate A's swap on the 36 and FM2's
  append on the genuinely-absent cases, so C_unified == C_HEAD by construction. (Equivalently: the dedup guard
  is *dormant behind Gate A at HEAD* — FM2 never runs where Gate A fires — so adding it is byte-identical, and
  removing Gate A afterward is byte-identical because the guarded primitive reproduces its carry.) Any residual
  diff is a defect to diagnose, not accept.
- **Both regression stops green** (roots unchanged): batch **52/24/52** set-diff empty ×3; robust sandwich
  identity-PASS (class-(b) Δ=0 all presets). Green **by construction** (winner/root inert).
- **Suites:** composing (1101 minus the retired pure-GateA fixtures, or re-homed — the build event decides the
  fixture disposition), notation 53 + 4 skip, pipeline_snapshot **11/11 no refresh** (no overlap — §Task 2).

### 4.3 The ratification surface (principle #14)

The **36-score alternatives delta is the user-ratification surface** — enumerated in §Task 2 (the 36 stems +
the before/after carry content). What the user ratifies:

1. **The correct-carry choice** — the unified path lands on **C_HEAD** (retain the distinct enharmonic
   Major-add6 alternative), *not* the FM2-append form (winner near-duplicate; loses the partner). Grounded at
   the O1b carry contract (§Task 3.1).
2. **The refactor** as one revertible, provenance-stamped commit that makes Gate A removable — with the
   full-surface byte-identity proof (expected 0 net move on all 352×3).

Because the design reproduces C_HEAD, the **net user-visible output delta is zero**; the 36 scores are the set
where the promotion *machinery* changes internally, presented so the user can confirm it reproduces the correct
carry rather than silently sliding to the FM2 form (the exact trap the 2.2c STOP caught). This honors #14 (the
load-bearing surface is touched, so it is ratified) and #12 (no information loss — the partner reading is kept).

### 4.4 Reuse-vs-new / what retires

- **New:** one promotion primitive + one collapsed builder wrapper (total-unification consolidation, #6).
- **Retires:** the `GateA` rule (enum/guard/name/fixtures/doc line); the two duplicate `gateCtx` wrapper
  lambdas collapse to one; the append-vs-swap idiom split collapses to one primitive. `buildChordResult` and
  FM2 (as the surviving flip rule) are **retained**.
- **One path per concern** (⛔ total-unification): after the event there is one builder wrapper and one
  "promote to winner" primitive for the whole chord-layer promotion machinery.

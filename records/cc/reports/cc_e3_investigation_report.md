# E3 Architecture Investigation

*Read-only investigation. No code changes, no commits. HEAD `a693b6ba82`.*

Scope read: `harmonicfunctionlayer.{h,cpp}`, `chordanalyzer.h`
(`ChordTemporalContext`, `PostScoringGateContext`, `RawCandidate`,
`BuildChordResultContext`), `chordanalyzer.cpp`
(`applyPostScoringGates` L1885–2458, the `dim7CharacteristicBonus` call site
L2787–2793, `applyIter8691Pedal` L2951+), `regionanalyzer.cpp` Pass-1 chain
(L445–460), and `docs/scoring_model.md` §4/§6/§7/§10/§11.

---

## Q1 — Gate inventory

All line numbers are from `chordanalyzer.cpp` at HEAD. **Crucial structural
fact:** every gate below is nested inside one outer guard at L1912–1916:

```cpp
if (prefs.inversionSuspicionMargin > 0.0
    && prefs.inversionBonusReduction < 1.0
    && results.size() >= 2
    && gateCtx.distinctPcs >= 3) { ... all gates ... }   // closes L2457
```

So *no* gate runs unless `inversionSuspicionMargin > 0`,
`inversionBonusReduction < 1.0`, `results.size() >= 2`, and
`distinctPcs >= 3`. (See Q6 — this couples the structural gates to the
inversion-correction preconditions.)

A second nesting: Gates A–F, the bias-correction deduction, and G-E/G-B/G-C/G-D
are *also* inside `if (winnerBassIsRoot && winnerQualityTargeted)` (L1946,
closes L2264), where `winnerQualityTargeted = winner is Major or Minor`. Gates
H, I, K, L, J sit outside that inner block but inside the outer guard.

| Gate | Lines | One-line description | Reads `context`? | `context` fields used | Class |
|------|-------|----------------------|------------------|-----------------------|-------|
| Pre-sort winner capture | 1931–1936 | Captures `originalWinnerQuality/RootPc/HasAddedSixth` before any swap (Sub-9a fix) | no | — | n/a (setup) |
| **Main bias-correction** | 1946–2177 | If winner is bass-root Maj/Min and margin to best clean alt < `inversionSuspicionMargin` (seventh-exempt), deduct bass bonus + re-sort; HalfDim first-inversion +0.55 sub-bonus | **no** | — (uses `gateCtx.distinctPcs`, `gateCtx.pcWeight`, `prefs`, `results`) | **structural** |
| **A — enharmonic flip (direct)** | 2017–2035 | `preferMinorOverMajorAdd6`: winner Maj+Add6, alt Minor at `(root+9)%12` → swap | no | — | **structural** |
| **A-FM2 — rawCandidate fallback** | 2039–2050 | Pull the Minor `(root+9)` alt from `rawCandidates` above threshold, swap to front | no | — (`gateCtx.rawCandidates`, `gateCtx.threshold`) | **structural** |
| **B** | 2054–2063 | Same flip when next region's root == alt root and bass steps to next | **yes** | `nextRootPc`, `bassIsStepwiseToNext` | **temporal** |
| **C** | 2067–2080 | Same flip when alt root is in 3-region window and bass steps from prev | **yes** | `bassIsStepwiseFromPrevious`, `recentRootPcs` | **temporal** |
| **D** | 2083–2090 | Same flip when ≥2 consecutive stepwise bass moves end here | **yes** | `consecutiveBassStepwiseCount` | **temporal** |
| **E — first-inversion Min→Maj** | 2104–2114 | Winner Minor, alt Major at `(root+8)%12`, stepwise bass → swap | **yes** | `bassIsStepwiseFromPrevious` ‖ `bassIsStepwiseToNext` (+`gateCtx.pcWeight`) | **temporal** |
| **F — second-inversion →Maj** | 2126–2134 | Alt Major at `(root+5)%12`, stepwise bass → swap | **yes** | `bassIsStepwiseFromPrevious` ‖ `bassIsStepwiseToNext` | **temporal** |
| **G-E — key-context** | 2191–2231 | `originalWinner` Min+Add6; find/pull HalfDim7 at `(origRoot+9)%12`; swap if its root is viiø7/iiø7/iiiø7 | **no** | — (`gateCtx.keyTonicPc`, `gateCtx.rawCandidates`) | **structural** |
| **G-B** | 2234–2241 | …swap if next root == HalfDim root and bass steps to next | **yes** | `nextRootPc`, `bassIsStepwiseToNext` | **temporal** |
| **G-C** | 2244–2254 | …swap if HalfDim root in 3-region window and bass steps from prev | **yes** | `bassIsStepwiseFromPrevious`, `recentRootPcs` | **temporal** |
| **G-D** | 2256–2261 | …swap if ≥2 consecutive stepwise bass moves | **yes** | `consecutiveBassStepwiseCount` | **temporal** |
| **H (H-B/H-C/H-D)** | 2276–2317 | Augmented rotation: winner Aug bass-root, alt Aug at `(root+4)`/`(root+8)`; whole block requires `context != nullptr` | **yes** | `nextRootPc`, `bassIsStepwiseToNext`, `bassIsStepwiseFromPrevious`, `recentRootPcs`, `consecutiveBassStepwiseCount` | **temporal** |
| **I — first-inv Maj over root-pos Min** | 2328–2352 | Winner Min bass-root; alt same bass, non-root-pos, root at I4 below bass, diatonic, margin ≤ 0.45 → swap | **no** | — (`gateCtx.keyTonicPc`, `scale`, `pcWeight`) | **structural** |
| **K — first-inv Augmented** | 2364–2388 | Winner Aug bass-root; alt aug-collection at I4 below bass, diatonic, margin ≤ 0.20 → swap | **no** | — (`gateCtx.keyTonicPc`, `scale`) | **structural** |
| **L — Maj over same-root Aug** | 2401–2422 | Winner plain Aug (no 7th); alt Major same root & bass, diatonic, margin ≤ 0.35 → swap | **no** | — (`gateCtx.keyTonicPc`, `scale`) | **structural** |
| **J — vii°→V7 completion** | 2435–2455 | Winner root-pos dim triad (no °7) whose M3-below PC sounds; alt Major+m7 there → swap to inverted V7 | **no** | — (`gateCtx.pcWeight`) | **structural** |

**Classification key.** *Structural* = the swap decision depends only on
`gateCtx`/`prefs`/`results` (no temporal-context field; the gate is meaningful
even with `context == nullptr`). *Temporal* = the swap fires only when
`context != nullptr` and a specific temporal field carries the right evidence.

**Temporal gates:** B, C, D, E, F, G-B, G-C, G-D, H-B, H-C, H-D.
**Structural gates:** bias-correction, A (direct + FM2), G-E, I, K, L, J.

---

## Q2 — `HarmonicFunctionContext` gap analysis

`HarmonicFunctionContext` today carries `keyFifths`, `keyMode`,
`previousRootPc`, `nextRootPc`, `previousBassPc`, `nextBassPc`.

To run *all* temporal gates inside `applyHarmonicFunction`, four
`ChordTemporalContext` fields would have to be added (one already present:
`nextRootPc`):

| Field needed | Type | Gate(s) | Where populated today |
|---|---|---|---|
| `bassIsStepwiseFromPrevious` | `bool` | C, E, F, G-C, H-C | `regionanalyzer.cpp` L406–408 (`isDiatonicStep(previousBassPc, currentBassPc)`) |
| `bassIsStepwiseToNext` | `bool` | B, E, F, G-B, H-B | `regionanalyzer.cpp` L434–436 (`isDiatonicStep(currentBassPc, nextBassPc)`) |
| `recentRootPcs` | `std::array<int,3>` | C, G-C, H-C | rolling buffer in `regionanalyzer.cpp` (L381 `recentRootsBuf`) via `advanceTemporalContext` (`chordanalyzer.h` L692) |
| `consecutiveBassStepwiseCount` | `int` | D, G-D, H-D | `runningStepwiseCount` in `regionanalyzer.cpp` (L380), folded in by `advanceTemporalContext` |
| `nextRootPc` | `int` | B, G-B, H-B | **already present** in `HarmonicFunctionContext`; populated `regionanalyzer.cpp` L431 |

**Important subtlety — the stepwise bools cannot simply be derived from the
existing `previousBassPc`/`nextBassPc`.** The gates' bools use `isDiatonicStep`
(a *diatonic* step, key-aware). The function layer's `wStepIn`/`wStepOut`
helpers (`harmonicfunctionlayer.cpp` L73–89) use a *chromatic* semitone/
whole-tone predicate. They are different predicates, so adding `nextBassPc`
alone is insufficient — either the precomputed diatonic bools must be carried,
or the current bass PC plus a diatonic-step helper must be plumbed in.

Fields *not* needed by any gate: `previousQuality` (only `resolutionBonus`
uses it, elsewhere), `regionMetricWeight`, `nextBassPc`/`previousBassPc` (gates
use the derived bools, not the raw PCs).

---

## Q3 — `dim7CharacteristicBonus` placement assessment

**1. Is it inside the per-cell scoring loop?** It is inside the
**bass-independent** `basisIndep` loop (L2754–2826: `for rootPc` × `for tplIdx`,
no bass dimension). The call is at L2790, summed into
`basisIndepMatrix[rootPc][tplIdx]` alongside `scoreTemplateTones`,
`scoreExtraNotes`, `structuralPenalties`, `tpcConsistencyBonus`, and
`bassIndependentContextualBonuses`. It is computed once per (root, template)
and reused for every bass when the snapshot cells are built (L2906).

**2. Does it use progression context?** **No.** Its signature is
`dim7CharacteristicBonus(tpl, rootPc, pcWeight, keyTonicPc, scale, extThreshold)`
(L1121). It reads only the template, the candidate root, the vertical
`pcWeight`, and the **key** (`keyTonicPc` + `scale`, to test whether the ♭♭7 PC
is diatonic). It does **not** touch `previousRootPc`, `nextRootPc`, bass
motion, or `recentRootPcs`. It is a *vertical + key* term, not a progression
signal.

**3. Should it move to the function layer? Would it change scores?**
The E3 roadmap bullet that lists `dim7CharacteristicBonus` as a
"functional-reasoning rule that does not belong in the scorer" **misclassifies
it.** The E2d redesign (`docs/scoring_model.md` §11) defines the oracle's job
precisely as `basisIndep` — *vertical pitch evidence without any progression
signal* — and explicitly keeps key-dependent vertical terms there. The dim7
bonus is exactly that kind of term (it is a per-rotation tiebreaker decided by
key diatonicity of the ♭♭7, completely determined by the tones + key).

- Moving it would be **architecturally wrong**: it would split vertical scoring
  across two files and put a non-progression term in the progression pipeline.
- It would **not change scores** if done carefully (the function layer already
  has `pcWeight`, `keyTonicPc`, `scale` in the snapshot), because the term is
  deterministic on inputs the snapshot already carries — but there is no
  behavioral benefit to offset the architectural cost.
- It also currently lives in the **anonymous namespace** (the file-local block
  closes at L1739; the bonus is at L1121), so moving it would require promoting
  it to a public symbol — extra friction for zero gain.
- Note `kWDim` (the function-layer dim/HalfDim *progression* bonus that uses
  `nextRootPc`, L250 of the doc) is the term that genuinely belongs in the
  function layer — and it already does. The roadmap likely conflated the two.

**Recommendation: leave `dim7CharacteristicBonus` in the oracle.** The roadmap
bullet is obsolete post-E2d.

---

## Q4 — Architectural assessment

### Q4a — File placement

**Type accessibility (the deciding question for a clean move).**
`applyPostScoringGates` uses: `buildChordResult` (public free fn declared in
`chordanalyzer.h` L770), `RawCandidate` / `BuildChordResultContext` /
`PostScoringGateContext` / `ChordTemporalContext` / `ChordAnalysisResult`
(all in `chordanalyzer.h`), `hasExtension`/`setExtension` (inline in
`chordanalyzer.h` L189/L208), and `std::find`/`std::swap`/`std::stable_sort`.
It uses **no** helper from `chordanalyzer.cpp`'s anonymous namespace
(that block closes at L1739; the gate function starts at L1885 in the public
`mu::composing::analysis` namespace).

`harmonicfunctionlayer.cpp` **already** includes `chordanalyzer.h` and already
references `analysis::RawCandidate`, `analysis::buildChordResult`,
`analysis::BuildChordResultContext`, and `analysis::PostScoringGateContext`
(L113, L289–293, L336–351). Therefore **moving `applyPostScoringGates` to
`harmonicfunctionlayer.cpp` requires promoting *no* types and exposing *no*
anonymous-namespace helpers.** The move is a clean cut-paste plus possibly
relocating the declaration from `chordanalyzer.h` to `harmonicfunctionlayer.h`.

**Argument for keeping it in `chordanalyzer.cpp`:** it operates on
`ChordAnalysisResult` identities and the `PostScoringGateContext` whose home
type is `chordanalyzer.h`; co-locating with `buildChordResult` (also in
`chordanalyzer.cpp`) is defensible.

**Argument for moving it to `harmonicfunctionlayer.cpp`:** the file *is* the
"competition pipeline / functional reasoning" module; the gates are functional
corrections, not pitch scoring; and `analyzeChord` is already a pure oracle
that does not call them. This matches the §10/§11 intent. The move is low-risk
because of the accessibility facts above.

### Q4b — Signal vs gate distinction

The competition signals (`rcb`, `wSeq`, `wDim`, `wStepIn/Out`) and the temporal
gates (B/C/D, G-B/C/D, H) **both** consume prev/next progression context, but
they are mechanically different things:

| | Competition signals | Temporal gates |
|---|---|---|
| **When** | Before any winner exists | After `results[]` (top-3 + diff-root) is built |
| **What** | Add a continuous score delta to **every** cell in the (bass×root×template) cube | Discrete `std::swap`/`stable_sort` on the **already-ranked result list** |
| **Effect on score** | Changes the numeric score; winner emerges from `max` | Does **not** change `rawCandidates`; only reorders `results[]` (the bias-correction deduction is the one exception that mutates a `results[]` score) |
| **Problem solved** | "Which reading does the *evidence* slightly favour?" | "Among readings the vertical score *provably cannot separate* (enharmonic/rotation identical PC sets), which is functionally correct?" |

So they are *adjacent but not the same kind of thing*. `wDim` is the clearest
bridge case — it is literally a dim7-rotation tiebreaker using `nextRootPc`,
i.e. a "signal-ified gate." One could argue the enharmonic gates (A–D, G, H)
are gates *only because* the additive-score mechanism cannot break a perfect
tie (identical PCs → identical vertical score), so a post-hoc categorical swap
is the only tool available. That makes a respectable case that they belong in
the same module as the signals (the function layer) — but **not** that they can
be folded into the same additive `max`-selection step, because their inputs are
provably tied at that step.

### Q4c — Ordering with `applyIter8691Pedal`

At every production call site the order is (regionanalyzer.cpp L446–459):

```
analyzeChord()           // internally runs applyHarmonicFunction() -> results
applyIter8691Pedal()     // Iter 86 (stamp m7), Iter 91 (bass-root promote), pedal Pass-2 replace
applyPostScoringGates()  // Gates A–L, on the post-pedal winner
```

The gates run **after** the pedal pass, by design — they correct the *final*
winner. `applyIter8691Pedal` can (a) stamp `MinorSeventh` on the winner (Iter
86, L2990), (b) swap in a bass-rooted candidate from `rawCandidates` (Iter 91,
L3028–3029), or (c) replace the winner entirely with the upper-voice Pass-2
chord (pedal, L3096+).

**Moving the temporal gates into `applyHarmonicFunction` would change output.**
`applyHarmonicFunction` runs *inside* `analyzeChord`, i.e. **before**
`applyIter8691Pedal`. Several gates read exactly what the pedal pass mutates:

- The bias-correction's seventh-exemption and Gate J both test
  `hasExtension(..., MinorSeventh)`. Iter 86 *adds* that extension. Run gates
  first → they see the pre-stamp winner and may decide differently.
- Iter 91 swaps the winner; gates currently correct the post-swap winner.
- The pedal replace can change the winner's root/quality entirely; gates
  currently see the replaced result.

So merging the temporal gates into `applyHarmonicFunction` is **not
byte-identical** unless the Iter 86/91/pedal pass were *also* relocated to run
before them — a much larger change. This is the strongest constraint on any
"merge" option.

---

## Q5 — Scope recommendation

**Bottom line first:** the E3 roadmap entry was written during E2c, *before*
the E2d redesign, and is largely **overtaken by events**. Its premise —
"functional reasoning lives inside `analyzeChord` and must be lifted out" — is
no longer true: post-E3-extraction + E2d, Gates A–L already live in a separate
free function (`applyPostScoringGates`) called *after* `analyzeChord` returns,
and `analyzeChord` is already a pure oracle. The only residue of the original
goal is that the free function physically resides in `chordanalyzer.cpp`. And
the roadmap's `dim7CharacteristicBonus` bullet is a misclassification (Q3).

**Recommended: Option A (file relocation only), treated as optional tidying —
or defer E3 as effectively complete.**

### Option A — file relocation (recommended if E3 is to be actioned)

Move `applyPostScoringGates` **unchanged** from `chordanalyzer.cpp` to
`harmonicfunctionlayer.cpp`; move its declaration from `chordanalyzer.h` to
`harmonicfunctionlayer.h`.

- **Type promotion required?** **None** (Q4a). All types are already public in
  `chordanalyzer.h` and already used by `harmonicfunctionlayer.cpp`.
- **Files changed:** `chordanalyzer.cpp` (−~573 lines), `harmonicfunctionlayer.cpp`
  (+same), `chordanalyzer.h`/`harmonicfunctionlayer.h` (move 1 declaration).
  If the function is kept in `namespace mu::composing::analysis`, call sites are
  byte-identical (`analysis::applyPostScoringGates`) and need no edit; if moved
  to `function::`, ~6 call sites change qualifier (regionanalyzer ×3,
  harmonicsegmenter, the notation bridges, and the `analyzeWithGates` test
  helper). Recommend keeping the `analysis::` namespace to minimise churn.
- **Byte-identical?** **Yes** — same code, same call order (still after
  `applyIter8691Pedal`). All suites (composing, notation, pipeline snapshots,
  equivalence harness, BIR corpus) should be unchanged.
- **Risk:** very low — only a missing `#include` for `<algorithm>` (used by
  `std::find`/`std::stable_sort`) is plausible.
- **Honest value:** cosmetic. It puts the functional-correction code in the
  functional module, which is where §10/§11 say it belongs, but it changes no
  behaviour and resolves no real coupling problem.

### Option B — merge temporal gates into `applyHarmonicFunction`

**Not recommended.** Two hard blockers:

1. **Ordering (Q4c):** `applyHarmonicFunction` runs before
   `applyIter8691Pedal`; the gates are designed to run *after* it and read what
   it mutates (`MinorSeventh` stamp, winner swap/replace). Merging is **not
   byte-identical** without also relocating the pedal pass.
2. **Mechanism mismatch (Q4b):** the gates operate on the built `results[]`
   list with margin guards and `stable_sort` semantics that depend on the exact
   post-threshold ordering and on `buildChordResult` having already run. This is
   a reimplementation, not a move. It would also require extending
   `HarmonicFunctionContext` with the 4 fields in Q2 (and resolving the
   diatonic-vs-chromatic step predicate mismatch).

Byte-identical is effectively impossible here without dragging the whole
Iter-86/91/pedal tail into the function layer too.

### Option C — what E3 should actually be

Given the above, the most honest framing:

- **Declare the original E3 substantially done.** Gates are already outside the
  oracle; the only open item is physical file location (Option A, optional).
- **Reclassify the roadmap bullets:** `dim7CharacteristicBonus` stays in the
  oracle (Q3); its function-layer cousin `wDim` is already in the right place.
- **If any non-cosmetic E3 work is wanted, target the Q6 coupling defect**
  (structural gates nested under inversion-correction preconditions), which is a
  genuine latent bug surface — independent of where the function lives.

**Recommendation:** do Option A only if the team wants the module boundary to be
physically clean; otherwise close E3 and pick up the Q6 item as its own small,
behaviour-preserving fix.

---

## Q6 — Anomalies / concerns

1. **Structural gates are nested under inversion-correction preconditions
   (highest concern).** Gates H, I, J, K, L are conceptually independent of the
   bias correction, yet they only execute when
   `inversionSuspicionMargin > 0.0 && inversionBonusReduction < 1.0 &&
   results.size() >= 2 && distinctPcs >= 3` (the outer `if` at L1912). Setting
   `inversionSuspicionMargin = 0` to disable *only* the bias correction would
   silently also disable Gate J (vii°→V7), Gate L (Aug→Maj), Gate I, Gate K, and
   Gate H. This is exactly the kind of implicit coupling the E2/E3 refactors are
   trying to remove. **Latent trap:** the pedal Pass-2 path sets
   `pass2Prefs.inversionSuspicionMargin = 0.0` (L3086); it does not currently
   call `applyPostScoringGates` on the Pass-2 result, so there is no live bug —
   but any future code that does would get a silently gate-less analysis. The
   structural gates should have their own preconditions, not inherit the
   correction's.

2. **`distinctPcs >= 3` applied to gates that don't need it.** Gate J fires on
   `{R-4, R, R+3, R+6}` (always ≥4 PCs) and Gates I/K/L are key/diatonic
   relations independent of PC count; gating them on `distinctPcs >= 3` is
   harmless today but is conceptual debt from the shared outer guard.

3. **Gate G-E pulls a HalfDim into `results[]` that may never be promoted.**
   At L2206–2215, when no HalfDim alt is in `results[]`, one is pulled from
   `rawCandidates` and `push_back`-ed, with `halfDimAltIdx = results.size()-1`.
   The subsequent swap only happens if G-E/G-B/G-C/G-D actually fire. If none
   fire, the pulled HalfDim **remains appended at the back of `results[]`** as a
   phantom alternative that was not there before the gate ran — potentially
   polluting the alternatives list (and pushing it past the documented "top-3 +
   diff-root" cap). Contrast Gate A-FM2 (L2044) and Iter 91 (L3028), which
   always swap+break after appending. Worth confirming this is intended.

4. **Float-literal margin comparisons against `double` scores.** Gates I, K, L
   compare `winner.identity.score - inv.identity.score > 0.45f` / `0.20f` /
   `0.35f` (L2348, L2384, L2418). The `f` suffix makes these `float`
   (`0.45f` ≈ 0.45000001) promoted back to `double`, a subtle inconsistency
   with the rest of the file (which uses `double` literals such as `0.70`). The
   thresholds are corpus-tuned so the tiny bias is baked in, but the mixed
   precision is a smell.

5. **Gate F does not constrain the winner's quality the way Gate E does.**
   Gate E checks `winner.identity.quality == Minor`; Gate F (L2126) checks only
   the *alt* (Major at `(root+5)%12`) and stepwise bass. Within the enclosing
   `winnerQualityTargeted` block the winner is Maj or Min, so it cannot fire on
   Aug/Dim — but the asymmetry (E pins winner quality, F does not) is worth a
   comment to confirm it is deliberate rather than an omission.

6. **Stale line-number references in comments.** The Iter-91 comment at L3027
   points to "the FM2 fallback ... line ~2189," and the doc §6/§7 line numbers
   (~L2639/2733/2820/…) no longer match the current file (the table maps to
   `applyPostScoringGates` interior offsets). Minor doc/code drift from the E3
   extraction; not load-bearing.

---

## Summary

E3 as originally scoped is largely overtaken by the E2d redesign: Gates A–L
already live in a standalone `applyPostScoringGates()` called *after* a pure
`analyzeChord()` oracle, so "lift functional reasoning out of the scorer" is
effectively done — the only residue is that the function physically sits in
`chordanalyzer.cpp`. The roadmap's `dim7CharacteristicBonus` bullet is a
misclassification: it is a vertical+key rotation selector with no progression
input and correctly belongs in the oracle (its progression cousin `wDim` is
already in the function layer). A clean Option-A relocation is feasible and
byte-identical with **zero** type promotion (all types are public in
`chordanalyzer.h` and already used by `harmonicfunctionlayer.cpp`), but its
value is purely cosmetic; merging the temporal gates into
`applyHarmonicFunction` (Option B) is **not** byte-identical because the gates
are deliberately ordered after the Iter-86/91/pedal pass and read what it
mutates. The single most valuable non-cosmetic finding is the Q6 coupling
defect — Gates H/I/J/K/L are silently gated behind the inversion-correction
preconditions — which is a real latent-bug surface worth fixing independently
of where the gate code lives.

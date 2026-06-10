# Layer Architecture Audit — composing module
*Written 2026-06-09. Cowork read-only code audit, post-Gate-R.*

---

## What was read

`chordanalyzer.cpp` (full), `chordanalyzer.h` (full), `harmonicfunctionlayer.h` (full),
`harmonicfunctionlayer.cpp` (Pass A + helper), `regionanalyzer.cpp` (L280–870),
`regiontonecollector.cpp` (L749–818), `ARCHITECTURE.md` (§4.1a–§4.1i + design boundary),
`docs/scoring_model.md` (§2, §4, §9), `docs/redesign_plan.md` (full).

---

## Intended layer structure vs. actual

ARCHITECTURE.md describes a clean separation:

```
analyzeChord()           — scoring oracle (vertical evidence only)
applyHarmonicFunction()  — competition pipeline (progression signals + winner selection)
```

E2d (`2917ec7571`) achieved this separation. The competition pipeline genuinely lives in
`harmonicfunctionlayer.cpp`; `analyzeChord` genuinely builds a `ScoringSnapshot` of all
cells before calling it. **The structural split is real.** But several signals that belong
in the competition pipeline are still inside the oracle as documented pre-existing debt —
and one documentation artefact incorrectly claims the oracle is clean.

---

## Finding 1 — Oracle temporal contamination (pre-existing, self-documented)

**Location:** `chordanalyzer.cpp`, `bassIndependentContextualBonuses` (~L1638) and
`bassDependentContextualBonuses` (~L1698).

**What's there:**
- `resolutionBonus` (0.35) — uses `previousQuality` and `previousRootPc`. A progression signal.
- `stepwiseBassInversionBonus` (0.5) — uses `bassIsStepwiseFromPrevious`. Temporal.
- `stepwiseBassLookaheadBonus` (0.5) — uses `bassIsStepwiseToNext`. Temporal.
- `completeTriadInversionBonus` (0.45) — uses `bassIsStepwiseFromPrevious`. Temporal.
- `sameRootInversionBonus` (0.4) — uses `previousRootPc`. Temporal.

All five produce non-zero contributions that land in `basisIndep` or `basisDep` before
the competition pipeline runs. The oracle is not purely vertical.

**Already documented:** `chordanalyzer.h` line 329 says explicitly:
> "TODO (ARCHITECTURE.md §4.1c): These four score-addition signals belong in the
> post-ranking correction layer, not in the vertical sonority scorer. They are left
> here as pre-existing technical debt; do not add further contextual signals to this section."

**Why this matters for Gate R:** Gate R's `basisDep ≤ 0` condition relies on
`sameRootInversionBonus` being in the oracle (a legitimate extended slash chord fires
`sameRootInversionBonus` → `basisDep > 0`; Gate R then spares it). If the oracle
debt is ever cleaned up, Gate R's condition must be revisited at the same time.

**Recommendation:** This debt is stable, documented, and will not be removed until a
scoring stabilisation phase. Do not attempt to move these signals now. When they do
migrate, Gate R needs to move or adapt simultaneously.

---

## Finding 2 — Documentation inaccuracies (low risk, misleading)

### 2a — `harmonicfunctionlayer.h` header comment

**Location:** `harmonicfunctionlayer.h`, `ScoringCell` or `HarmonicFunctionContext`
struct header (the comment describing `basisIndep`).

The comment says "basisIndep WITHOUT any progression signal." This is factually incorrect.
`basisIndep` carries `resolutionBonus`, `stepwiseBassInversionBonus`, and
`stepwiseBassLookaheadBonus` — all temporal signals — baked in before the competition
pipeline sees the cell.

**Action for CC:** Fix the comment to say something like "basisIndep includes the oracle
vertical score PLUS the contextual inversion/resolution bonuses computed in
`bassDependentContextualBonuses` and `bassIndependentContextualBonuses`; see
`chordanalyzer.h:329` for the technical debt note." Low-risk comment-only edit.

### 2b — Stale invariant comment in `chordanalyzer.cpp`

**Location:** `chordanalyzer.cpp` ~L1634.

A comment asserts `bassIndep + bassDependent == contextualBonuses`. This is **false**.
`contextualBonuses` (used only by `diagnoseChord`, L1456) adds `rootContinuityBonus`
directly at L1482. Neither `bassIndependentContextualBonuses` nor
`bassDependentContextualBonuses` add `rootContinuityBonus`. The divergence is intentional
(diagnoseChord needs rcb for diagnostic output; the production path handles rcb in the
competition pipeline via Gate R-aware processing). But the comment implies the invariant
holds everywhere, which will mislead any future reader trying to verify the split.

**Action for CC:** Update the comment at ~L1634 to note that `contextualBonuses` is
used by `diagnoseChord` only and intentionally includes `rootContinuityBonus`, while
`bassIndependentContextualBonuses + bassDependentContextualBonuses` do not.

---

## Finding 3 — Bridge path missing forward lookahead (implementation gap, fixable)

**Location:** `regiontonecollector.cpp`, `findTemporalContext` (~L749–818).

The bridge path constructs temporal context for a single chord. It:
- Looks **backward only** via `seg->prev1()`.
- Cold-analyzes the predecessor chord with `nullptr` context (no temporal chain).
- Sets `previousRootPc`, `previousQuality`, `previousBassPc`, `bassIsStepwiseFromPrevious`.
- Does **NOT** set `bassIsStepwiseToNext`, `nextRootPc`, `nextBassPc`, or any Step 1/2
  fields (`previousWinnerScore`, `previousWinnerMargin`, `previousWinnerRootPcWeight`,
  `previousDistinctPcs`).

**This is NOT a structural constraint.** `seg->next1(SegmentType::ChordRest)` is used
three times elsewhere in `regiontonecollector.cpp` (lines 142, 409, 692) — the API is
available. `findTemporalContext` simply never calls it. All paths should provide the same
temporal context; the missing forward lookahead is an implementation gap.

Result of the gap: `stepwiseBassLookaheadBonus` never fires on the bridge path. The six
snapshot drifts from Gate R are a direct consequence — batch had already stopped awarding
the lookahead bonus to the wrong Δ=+7b candidates, but bridge had never been awarding it
at all, so Gate R changed different things in the two paths.

**What adding forward lookahead to the bridge requires:**
The forward walk would mirror the existing backward walk: call `seg->next1()`, collect
sounding tones, cold-analyze the next chord, extract `nextRootPc` and `nextBassPc`,
compute `bassIsStepwiseToNext = isDiatonicStep(currentBassPc, nextBassPc)`. This is the
same pattern as the backward walk. The "cold" limitation remains (no temporal chain for
the neighbor), but `nextRootPc` is what `wSeqBonus` and `stepwiseBassLookaheadBonus` need.

**What remains harder after the lookahead fix:**
- The backward predecessor is also analyzed cold (`nullptr` context). In the batch path
  the predecessor's own context chain is known; in the bridge it is not. Fixing this
  properly requires a full forward pre-pass over the score before any chord is annotated.
  That is a larger change worth designing separately.
- Step 1/2 fields (`previousWinnerScore`, `previousWinnerMargin`, etc.) require knowing
  the predecessor's competition result — unavailable without a pre-pass.

**Recommended action:** Add a forward-lookahead walk to `findTemporalContext` to populate
`nextRootPc`, `nextBassPc`, `bassIsStepwiseToNext`. This brings the bridge into parity
with the batch path for lookahead signals and eliminates the systematic 6-snapshot drift
class. Write a CC instruction for this; it is a self-contained change to one function.

---

## Finding 4 — Sub-region lookahead always zero (consistent, undocumented)

**Location:** `regionanalyzer.cpp`:
- Pass-2 sub-region context construction (~L618–621): `subCtx.bassIsStepwiseToNext = false`
- Pass-2b sub-region context construction (~L823–826): `subCtx.bassIsStepwiseToNext = false`

`stepwiseBassLookaheadBonus` never fires for sub-regions. This is consistent across both
passes — probably intentional (sub-region boundaries are computed before the parent region
is committed, so the "next" identity is not known yet). But it is undocumented.

**Action:** Add a brief comment at both sites explaining WHY `bassIsStepwiseToNext = false`
(forward context unavailable at sub-region resolution time). Low priority but prevents
future confusion.

---

## Finding 5 — `ChordTemporalContext` struct boundary (architectural)

**Location:** `chordanalyzer.h`, `ChordTemporalContext` struct (~L570).

`ChordTemporalContext` is documented as a "single-step look-around" struct — not a full
progression context. ARCHITECTURE.md line 906 explicitly says a future `TemporalContext`
will carry full progression context (chord history, cadence state) and that "Keep the
names distinct."

However, Steps 1+2 from the redesign added these fields to `ChordTemporalContext`:
- `previousWinnerScore`, `previousWinnerMargin`, `previousWinnerRootPcWeight`,
  `previousDistinctPcs` — these are progression-level data (winner quality, competition
  margin) that logically belong in the planned `TemporalContext` (for `ProgressionAnalyzer`).

These are already documented in `docs/redesign_plan.md` as "infrastructure — foundation
for Phase E." They do not represent a new finding. But the gap is: `ChordTemporalContext`
is growing into something it was not designed to be, with no migration plan to
`TemporalContext` written down.

**Recommendation:** At the start of Phase E (when `ProgressionAnalyzer` design begins),
plan the migration of these four Step 2 fields from `ChordTemporalContext` to the new
`TemporalContext` explicitly. Do not add further progression-level signals to
`ChordTemporalContext`; put them in `TemporalContext` directly.

---

## Finding 6 — Gate R cross-layer dependency (stable but documented)

Gate R (`harmonicfunctionlayer.cpp`, Pass A) uses `cell.basisDep ≤ 0` to distinguish
bare-root continuations from legitimate extended slash chords. This works because:
- A legitimate extended slash chord has a sounding third → `sameRootInversionBonus` fires
  in the oracle → `basisDep > 0` → Gate R spares the chord.
- A bare-root foreign-bass continuation has no sounding third → `basisDep == 0` → Gate R fires.

Gate R is in the correct architectural layer (competition pipeline). But its correctness
depends on `sameRootInversionBonus` remaining in the oracle (Finding 1). This creates a
cross-layer dependency that is currently invisible to anyone reading only `harmonicfunctionlayer.cpp`.

**Action for CC:** Add a comment to Gate R's `basisDep ≤ 0` condition explaining:
"Uses oracle's `basisDep` as a proxy for 'has sounding third via sameRootInversionBonus'.
If oracle temporal debt is ever cleaned up (chordanalyzer.h:329), this condition must be
revisited — `basisDep` would no longer carry that signal."

---

## Should we split code by layers?

**Short answer: selective yes — but not a big-bang refactor now.**

What is already correctly split:
- Key resolver: `keyresolver.{h,cpp}` — separate, clean ✓
- Competition pipeline: `harmonicfunctionlayer.{h,cpp}` — separate, correct ✓
- Region analysis: `regionanalyzer.{h,cpp}` — separate ✓
- Bridge path: `regiontonecollector.{h,cpp}` — separate ✓

What remains mixed in `chordanalyzer.cpp`:
1. **Pure template scoring oracle** — correctly placed
2. **Temporal context bonuses** (the five signals in Finding 1) — wrong layer but are
   pre-existing, self-documented technical debt. Moving them requires Phase E to be ready
   to receive them cleanly.
3. **Post-scoring gates (A–L, Iter 91 temporal gates)** — these are in
   `applyPostScoringGates`. E3 investigation found temporal gates B/C/D/G-B/G-C/G-D
   cannot move cleanly because they run after `applyIter8691Pedal`. Moving any of these
   is a non-trivial refactor.

**The right time for a structural split of `chordanalyzer.cpp`:**
When Phase E lands. At that point:
- The temporal bonuses (Finding 1) should migrate from the oracle into the competition
  pipeline or a new contextual-correction layer.
- The post-scoring temporal gates may have simpler migration paths once the competition
  pipeline has richer context.
- The split would be motivated by specific Phase E needs, not done preemptively.

**What CAN be done now (low-risk, no behavioral change):**
- Extract `ChordSymbolFormatter` to its own file (already flagged in ARCHITECTURE.md §4.1i)
- Fix the pitchClassName / pitchClassNameFromTpc duplication (also flagged §4.1i)
- Fix the two inaccurate comments identified in Finding 2 (comment-only changes)
- Add the bridge-path shallowness comment (Finding 3)

---

## Should we have per-layer regression tests?

**Yes — specifically targeted, not a wholesale testing rewrite.**

Current test coverage gaps that matter:

### 1. `bassIsTemplateChordTone` helper (Gate R) — no unit tests exist

`kMasks` in `harmonicfunctionlayer.cpp` has 17 entries that must stay synchronized with
the 17 templates in `chordanalyzer.cpp`. There are currently zero tests verifying this
table is correct. A template addition that updates the template array but forgets `kMasks`
would produce a silent scoring bug (Gate R would fire on chord-tone bass continuations,
incorrectly zeroing `rootContinuityBonus`).

**Concrete tests to add:**
- For each template 0–16: verify that each interval in the template passes `bassIsTemplateChordTone`.
- For template 0 (Major triad {0,4,7}): verify intervals 1,2,3,5,6,8,9,10,11 all FAIL.
- For template 6 (Diminished {0,3,6}): verify interval 9 fails (the Δ=+7b foreign bass case).
- These are pure-function tests — no score loading needed.

### 2. Gate R fires/does-not-fire on constructed cells — no tests exist

Add synthetic test cases covering the Gate R decision boundary:
- A ScoringCell where `bassPc` is a template chord tone + `basisDep == 0`: Gate R must NOT fire.
- A ScoringCell where `bassPc` is NOT a template chord tone + `basisDep == 0`: Gate R MUST fire.
- A ScoringCell where `bassPc` is NOT a template chord tone + `basisDep > 0` (extended slash): Gate R must NOT fire.
- `ScoringPhase::Segmentation`: Gate R must never fire regardless of bassPc.

This directly pins the behavior of the `basisDep ≤ 0` refinement and the
segmentation-phase guard (`phase == ScoringPhase::Final`) that CC found necessary.

### 3. Regression tests for the three Δ=+7b cases

bwv245.28, bwv296, bwv320 are now fixed. But there are no tests that would fail if Gate R
were removed or if the kMasks table were corrupted. The BIR corpus check catches this at
the corpus level, but a focused unit test would catch it earlier.

These exist naturally as `chordanalyzer_musicxml_tests` cases if those scores are in the
test corpus — if they are not, they should be added.

### 4. What NOT to add right now

- Tests for the oracle temporal signals (Finding 1) — this would just be testing known
  debt; better to wait until they migrate.
- A full competition-pipeline isolation test harness — premature given the cross-layer
  dependency on oracle `basisDep`.
- Bridge-path context construction unit tests — the structural gap (Finding 3) makes
  these fragile; better to document the gap and test observable output.

---

## Summary of recommended CC tasks

Ordered by risk and value:

| Priority | Task | Risk | Benefit | Status |
|---|---|---|---|---|
| ✅ Done | `bassIsTemplateChordTone` unit tests (all 17 templates + boundary cases) | Zero | Pins kMasks against future template additions | `bffb6c4e3d` |
| ✅ Done | Gate R synthetic unit tests (4 branches) | Zero | Documents and pins Gate R's two refinements | `bffb6c4e3d` |
| ✅ Done | Fix `harmonicfunctionlayer.h` basisIndep comment (Finding 2a) | Zero | Removes misleading documentation | `927e8b579d` |
| ✅ Done | Fix stale invariant comment at `chordanalyzer.cpp:1634` (Finding 2b) | Zero | Removes incorrect invariant claim | `927e8b579d` |
| ✅ Done | Add Gate R `basisDep` cross-layer comment (Finding 6) | Zero | Documents the dependency explicitly | `927e8b579d` |
| ✅ Done | Document bridge lookahead gap in `findTemporalContext` (Finding 3) | Zero | Prevents future confusion | `927e8b579d` |
| **High** | **Add forward-lookahead walk to `findTemporalContext` (Finding 3)** — populate `nextRootPc`, `nextBassPc`, `bassIsStepwiseToNext` via `seg->next1()` | **Low** | **Closes systematic bridge/batch divergence for lookahead bonuses** | Pending |
| Low | Extract `ChordSymbolFormatter` to its own file (already in §4.1i backlog) | Very low | Small architecture cleanup | Pending |
| Deferred | Split temporal oracle signals to competition pipeline | High | Wait for Phase E | Deferred |
| Deferred | Migrate Step 2 fields from ChordTemporalContext to TemporalContext | High | Wait for ProgressionAnalyzer design | Deferred |
| Deferred | Move inversion correction from `applyPostScoringGates` to competition pipeline (Finding 7) | High | Replaces B/C/D cascade with passage-context decision | Deferred until Phase E |

---

## Finding 7 — Gate cascade pattern in `applyPostScoringGates` (architectural)

*Added 2026-06-09 after systematic read of all gates in `applyPostScoringGates`
and `applyIter8691Pedal`.*

### What was read

`chordanalyzer.cpp` `applyPostScoringGates` (full), `applyIter8691Pedal` (full),
`harmonicfunctionlayer.cpp` Gate R block, `docs/scoring_model.md` §6.

### The full gate catalog

**`applyIter8691Pedal` (runs first):**
- Iter 86: stamps MinorSeventh when bass is at b7 of root (Am/G → Am7/G)
- Iter 91: promotes bass-as-root when `nextRootPc == bassPc` — Pattern A (Minor, delta=8)
  and Pattern B (Major, delta=9). Forward context required. The mirror-image of the
  inversion-correction gates.
- Two-pass pedal detection: re-analyzes upper voices when bass is non-chord-tone; labels
  as pedal point when confident. A mini-iterative approach that already works correctly.

**`applyPostScoringGates` (runs after):**
- Enharmonic fast path: MajorAdd6 → Minor7 direct swap (preset-gated, no temporal)
- FM2 fallback: scans `rawCandidates` for enharmonic Minor partner
- Gate B: MajorAdd6→Minor via forward evidence (`nextRootPc == altRoot && bassIsStepwiseToNext`)
- Gate C: MajorAdd6→Minor via 3-region window + backward stepwise bass
- Gate D: MajorAdd6→Minor via ≥2 consecutive stepwise bass moves
- Margin correction: deducts bass-root bonus, re-sorts (if no enharmonic flip, narrow margin, no seventh exemption)
- Gate E: first-inversion (Minor winner, Major alt at root+8) + stepwise bass
- Gate F: second-inversion (Major alt at winner root+5) + stepwise bass
- Gate G-E: MinorAdd6 → HalfDim7 via key context (viiø7, iiø7, iiiø7)
- Gate G-B / G-C / G-D: same MinorAdd6→HalfDim7, temporal mirrors of B/C/D
- Gate H-B / H-C / H-D: Augmented root-symmetry, temporal mirrors of B/C/D again
- Gate I: Minor root-pos → diatonic Major first-inversion (I4 interval, margin ≤ 0.45)
- Gate K: Augmented root-pos → Augmented first-inversion (diatonic, margin ≤ 0.20)
- Gate L: Augmented → Major same-root quality fix (diatonic, margin ≤ 0.35)
- Gate J: Diminished triad → inverted dominant-7th when dominant root is sounding

**Competition pipeline (`harmonicfunctionlayer.cpp`):**
- Gate R: withholds `rootContinuityBonus` from bare-root foreign-bass continuation
  (`basisDep ≤ 0 && phase == ScoringPhase::Final && bass ∉ template`)

### The structural pattern

**Two-thirds of `applyPostScoringGates` is solving one problem: the oracle's
bass-as-root bias.** The oracle's scoring model rewards templates whose intervals
match the sounding tones at the bass pitch class. When the bass is E and the chord
is C/E, both E minor (E at root-position) and C/E (inverted C major) are candidates.
E minor gets the bass-root bonus; C/E does not. The entire gate structure above —
all the enharmonic flips, the B/C/D cascade, the G/H repeated cascades, gates E/F/I/K/L
— is compensating for this one systematic bias at the output level.

**The cascade accumulation pattern.** Each cascade was added incrementally:
- B was insufficient → add C → add D (all for MajorAdd6 ↔ Minor)
- Same pattern repeats for MinorAdd6 ↔ HalfDim7 → G-B, G-C, G-D
- Same pattern repeats for Augmented rotation → H-B, H-C, H-D

This is exactly the "accumulating gates as warning sign" from ARCHITECTURE.md §2.14.
Each gate is correct in isolation; the cascade is the symptom of an unresolved
architectural problem.

**Gate J and Gate R are architecturally healthier.** They address structural patterns
with principled conditions rather than compensating for a bias:
- Gate J: four PCs {R-4, R, R+3, R+6} that match a dominant seventh plus the root
  sounding in the score → must be V7 inversion. Tight vertical evidence.
- Gate R: bare-root foreign-bass continuation with no inversion credit → rcb
  has no business firing. Tight progression logic.

Neither of these would grow into a cascade.

**Iter 91 is the mirror image.** It promotes bass-as-root when forward context confirms
it (next region's root == current bass). This shows the oracle's ambiguity is genuine —
sometimes the bass IS the root (Iter 91 cases) and sometimes it is not (most of
applyPostScoringGates). The oracle consistently overweights the bass-as-root hypothesis,
and the whole gate architecture is the response.

### What this means for future gate decisions

**No gate addresses oracle-level vertical failure.** Every gate in `applyPostScoringGates`
assumes the correct candidate is present and competitive — it just needs a nudge via
temporal or key context. If the correct root is absent from the candidate pool (zero
pcWeight) or scores far below the wrong winner on vertical evidence alone, no gate
can help. This is why the Δ=+7a cases (bwv102.7, bwv261) cannot be fixed by a gate:
the oracle is not wrong in the present-root slices (it prefers the correct root), and
in the absent-root slices there is nothing to correct.

**The policy for new gate decisions:**
1. If a proposed gate is another variant of the bass-as-root bias correction (e.g. a
   new enharmonic pair, a new interval relationship) — consider whether the bias itself
   can be reduced first, or whether Phase E can provide the functional context that
   removes the ambiguity. Only add the gate if the fix is genuinely local.
2. If a proposed gate has a structural condition like Gate J or Gate R (specific
   pitch-class arithmetic + presence constraint, not temporal evidence) — it is likely
   architecturally sound.
3. If a proposed gate requires the cascade pattern (temporal B-style → C-style → D-style)
   — this is a strong signal that the underlying problem is missing Phase E context.

### Recommendation

Do not add more B/C/D-style temporal gates. The cascade is already at maximum depth
for the MajorAdd6/Minor and MinorAdd6/HalfDim7 problems. The correct resolution for
new inversion ambiguity cases is Phase E (cadence and functional context), not a new
temporal gate.

The medium-term architectural fix for the bass-as-root bias is to move inversion
correction from `applyPostScoringGates` (chord-by-chord, after scoring) into the
competition pipeline in `harmonicfunctionlayer.cpp` (which has full passage context via
`ScoringSnapshot`). That would replace the cascade with a single well-evidenced decision
using the actual passage context. Defer until Phase E motivates it.

---

## What this audit did NOT find

- No new bugs. Everything found is either pre-existing documented debt, a comment
  accuracy issue, or a structural gap that was already known.
- No layer boundary violations beyond the five temporal signals in Finding 1 (which are
  documented in the code itself).
- No cases where the competition pipeline writes back to the oracle or creates circular
  dependencies.
- The E2d split is sound. The architecture is coherent even with the debt.

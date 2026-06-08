# Step 3 Pre-Investigation — Key-as-Distribution

*CC read-and-diagnose pass, 2026-06-08. HEAD `c8afd0e23c` (Step 2 redesign).
No production code changed; the temporary KEY-DIAG instrumentation in
`regionanalyzer.cpp` was added, measured, and fully removed (working tree for
that file is byte-identical to HEAD — verified empty `git diff`).*

## Headline

**The premise behind Step 3 is stale.** The redesign plan, COWORK_HANDOFF.md, and
`docs/key_detection_baroque_partial_signature.md` all assert that Corelli
`op01n08d` is detected as **G minor instead of C minor**. That was true on
2026-05-23, but it was **fixed on 2026-06-03 by commit `81978321e3`
(`fix(keyresolver): Option B Baroque partial-signature correction`)**, which is in
the current HEAD. The live resolver now returns **C minor at rank 0 for every
region** on both the batch and notation paths. G minor never appears anywhere —
not as a winner, not as a runner-up.

Consequently **key-as-distribution will not fix Corelli `op01n08d`, because the key
is already correct.** The residual `op01n08d` failures are quality/inversion/
segmentation issues, not key-detection issues.

---

## Part A — `fnCtx.keyFifths` / `fnCtx.keyMode`: confirmed DEAD (write-only)

**They are written but never read.**

- **Written** in the oracle at
  [chordanalyzer.cpp:2932-2933](src/composing/analysis/chord/chordanalyzer.cpp#L2932-L2933):
  ```cpp
  fnCtx.keyFifths = keySignatureFifths;
  fnCtx.keyMode   = keyMode;
  ```
- **Never read** in `harmonicfunctionlayer.cpp`. The only `HarmonicFunctionContext`
  (`ctx`) fields read anywhere in that file are:
  - `ctx.previousBassPc` ([:137](src/composing/analysis/function/harmonicfunctionlayer.cpp#L137))
  - `ctx.nextBassPc` ([:140](src/composing/analysis/function/harmonicfunctionlayer.cpp#L140))
  - `ctx.previousRootPc` ([:206](src/composing/analysis/function/harmonicfunctionlayer.cpp#L206))
  - `ctx.nextRootPc` ([:212,214](src/composing/analysis/function/harmonicfunctionlayer.cpp#L212-L214))
- The whole `ctx` is forwarded to one helper, `applyStepBonusGuard`
  ([:122-167](src/composing/analysis/function/harmonicfunctionlayer.cpp#L122-L167)),
  but that helper reads only `ctx.previousBassPc` / `ctx.nextBassPc`. `keyFifths` /
  `keyMode` are not passed to it or to any other helper.
- The two `.keyMode` matches that *do* exist in the .cpp
  ([:291](src/composing/analysis/function/harmonicfunctionlayer.cpp#L291),
  [:340](src/composing/analysis/function/harmonicfunctionlayer.cpp#L340)) are
  **`snapshot.keyMode`**, not `ctx.keyMode` — a different field (`ScoringSnapshot`,
  not `HarmonicFunctionContext`).

**Where key influence actually travels:** through the *snapshot*, not the context.
The oracle sets `snapshot.scale` / `snapshot.keyTonicPc` / `snapshot.keyMode`
([chordanalyzer.cpp:2894-2896](src/composing/analysis/chord/chordanalyzer.cpp#L2894-L2896)),
and the function layer only forwards those into `gateCtx`
([:340](src/composing/analysis/function/harmonicfunctionlayer.cpp#L340)) for the
post-scoring gates — it does no key-dependent *scoring*. By the time
`applyHarmonicFunction` runs, all key influence is already frozen into
`cell.basisIndep`.

**Recommendation:** document `HarmonicFunctionContext::keyFifths` and `::keyMode`
as dead write-only fields (or delete them and the two assignment lines). They are a
trap for Step 3 — the obvious-looking "pass key confidence via `fnCtx`" hook does
nothing, because the function layer is the wrong layer for key scaling.

---

## Part B — `keyTonicPc` and `scale` in the oracle

### Computation

Both are computed once near the top of `analyzeChord`, from the function parameters
`keySignatureFifths` and `keyMode`
([signature at chordanalyzer.cpp:2473-2479](src/composing/analysis/chord/chordanalyzer.cpp#L2473-L2479)):

```cpp
// chordanalyzer.cpp:2729-2742
const int ionianTonicPc = ionianTonicPcFromFifths(keySignatureFifths);          // L2729
const int keyTonicPc    = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;     // L2730
...
const size_t modeScaleIdx = DIATONIC_PARENT_INDEX[keyModeIndex(keyMode)];          // L2741
const std::array<int, 7>& scale = keyModeScaleIntervals(keyModeFromIndex(modeScaleIdx)); // L2742
```

Intermediate variables: `ionianTonicPc` (L2729) and `modeScaleIdx` (L2741).
Note `DIATONIC_PARENT_INDEX` ([L2736-2740](src/composing/analysis/chord/chordanalyzer.cpp#L2736-L2740))
maps every non-diatonic mode to its diatonic key-signature parent, so e.g. Aeolian
(mode 5) and HarmonicMinor (mode 14) **resolve to the same Aeolian `scale`** — this
matters for Part C (the C-minor mode oscillation is harmless to the scale).

### Functions consuming `keyTonicPc` / `scale` in the oracle scoring loop

The scoring loop is the `for (rootPc) { for (tplIdx) { … } }` block at
[chordanalyzer.cpp:~2760-2839](src/composing/analysis/chord/chordanalyzer.cpp#L2760-L2839),
building `basisIndepMatrix`. Inside it, exactly **two** functions receive
`keyTonicPc` / `scale`:

1. **`dim7CharacteristicBonus(tpl, rootPc, pcWeight, keyTonicPc, scale, prefs.extensionThreshold)`**
   — [L2803](src/composing/analysis/chord/chordanalyzer.cpp#L2803). A
   rotation-selection mechanism (uses `scale` to find the non-diatonic ♭♭7 of the
   true enharmonic dim7 rotation). **Do not naively scale this by key confidence** —
   it is a discrete selector, not a smooth bonus; weakening it breaks 6 Jazz catalog
   dim7 entries (per the inline B3 warning at L2790-2799).
2. **`bassIndependentContextualBonuses(tpl, rootPc, keyTonicPc, scale, prefs, context)`**
   — [L2806](src/composing/analysis/chord/chordanalyzer.cpp#L2806). Contains the
   inline **diatonic-root bonus** loop at
   [L1645-1651](src/composing/analysis/chord/chordanalyzer.cpp#L1645-L1651)
   (`for (interval : scale) if ((keyTonicPc+interval)%12 == rootPc) score += prefs.diatonicRootBonus`).
   This is the term the redesign plan calls `diatonicRootBonus`; there is **no
   separately-named function** by that name. This is the clean candidate for
   key-confidence scaling.

**The instruction's known list is complete — there are no other consumers in the
production oracle loop.** Caveats checked and ruled out:
- `contextualBonuses` (the monolithic bass-dependent helper,
  [L1456](src/composing/analysis/chord/chordanalyzer.cpp#L1456)) also takes
  `keyTonicPc`/`scale`, but it is **only called from `diagnoseChord`**
  ([L3271](src/composing/analysis/chord/chordanalyzer.cpp#L3271)), the diagnostic
  path — never from `analyzeChord`. The production bass-dependent delta (`basisDep`)
  does not use `keyTonicPc`/`scale`.
- `diagnoseChord` (L3232-3273) is a separate diagnostic function and re-derives its
  own `keyTonicPc`/`scale`; not part of production scoring.
- The remaining `scale` / `keyTonicPc` references (gate logic at L1822-1838,
  L2355/2394/2428; result building at L1879/3429/3479/3607; tonicization at
  L3523-3548) all read `gateCtx.scale` / `result.function.keyTonicPc` **after** the
  oracle, i.e. they consume the already-frozen snapshot value, not the live oracle
  variable.

**Implication:** to make the oracle key-confidence-aware, the scaling has to be
applied at L2803/L2806 (inside the oracle), not in `applyHarmonicFunction`. This
matches the redesign plan's "Architecture correction (2026-06-08 read pass)."

---

## Part C — Corelli `op01n08d` key-resolver diagnostic

### Method

Temporary `fprintf(stderr, "[KEY-DIAG] …")` added immediately after **both**
`kr::resolveKeyAndModeRanked` calls in `regionanalyzer.cpp` (initial L305, per-region
L411), printing rank, fifths, mode, tonicPc, score, normalizedConfidence for the top
3 candidates. Built, then ran:
- `batch_analyze op01n08d.mscx --preset Baroque` (batch path) → 129 regions
- `batch_analyze … --dump-regions notation` (the path the failing notation tests
  use) → 386 region evaluations

Score: `tools/dcml/corelli/MS3/op01n08d.mscx`. **Notated signature = −2 flats**
(verified: `<accidental>-2</accidental>`), declared `<mode>minor</mode>`. A literal
−2/Aeolian reading is **G minor** (tonicPc 7) — this is the historical bug. DCML
ground truth: **C minor throughout**.

Mode enum decode (from `keymodeanalyzer.h`): 1=Dorian, 2=Phrygian, 5=Aeolian
(natural minor), 14=HarmonicMinor.

### Result — the resolver returns C minor, confidently, everywhere

Rank-0 winner tally across all 129 batch regions:

| Winner | Count | Reading |
|---|---|---|
| `fifths=-3 mode=5  tonicPc=0` | 72 | **C Aeolian (C natural minor)** |
| `fifths=-3 mode=14 tonicPc=0` | 57 | **C harmonic minor** |

- **100% of rank-0 winners are tonicPc=0 (C), fifths=−3 (3-flat / true C-minor
  signature).** The −2 notated signature has been reinterpreted to −3.
- The rank-0 oscillation is only between C Aeolian (mode 5) and C harmonic minor
  (mode 14). Both map to the **same Aeolian `scale`** via `DIATONIC_PARENT_INDEX`
  (Part B), so this oscillation does not change the scale fed to the oracle.
- The piece-start anchor (`INITIAL tick=0`) returns `fifths=-3 mode=5 tonicPc=0
  score=2.0 normConf=0.5` — i.e. the fallback anchor now anchors to **C minor**, not
  the G the old doc describes.
- **G minor (Aeolian, tonicPc=7) never appears at any rank in any region.** The only
  tonicPc=7 candidates are mode=2 **G Phrygian** at rank 1-2 (a diatonic relative of
  Eb/C minor, the dominant region), never a competing key center.
- Notation path confirms the same: key labels are 41×`Cmin` + 30×`Charm`, **zero
  `Gmin`**. (The `G`/`Gm` strings in that JSON are *chord* labels for the dominant of
  C minor, not key labels.)

### Answers to the instruction's three Part-C questions

1. **What does `initialRanked` return? Is rank=0 the wrong key (G minor)?**
   No. Rank 0 = C Aeolian (`fifths=-3 mode=5 tonicPc=0`), the fallback anchor, conf
   0.5. Not G minor.
2. **For early regions, does the correct key (C minor) appear at rank 1/2?**
   The correct key is **rank 0**, not a runner-up. Ranks 1-2 are the *other C-minor
   flavor* (harmonic minor) and **F Dorian** (`mode=1 tonicPc=5`). C minor is the
   winner from the first region onward.
3. **Is G minor genuinely high-confidence, or only marginally ahead of C minor?**
   Neither — **G minor is not in the running at all.** The contest is entirely
   *within* C minor (Aeolian vs harmonic minor); the two are near-ties in `score`
   (e.g. tick=240: 36.16 vs 35.79) but both are C minor, so the tonic is never in
   doubt.

### Why the premise was stale — commit `81978321e3`

`fix(keyresolver): Option B Baroque partial-signature correction` (2026-06-03,
ancestor of HEAD) detects the Baroque partial-signature convention by checking that
the "missing" accidental (♭6 = A♭ in C minor) is pervasive (≥3% of sounding weight)
**and** dominates its natural counterpart (≥2× A♮), then reinterprets the signature
one step toward the missing accidental (−2 → −3) for the whole of
`resolveKeyAndModeRanked` (lookback, anchor, `analyzeKeyMode`, fallback). The
canonical case named in the commit is exactly Corelli `op01n08d`. This is **Option B
from `docs/key_detection_baroque_partial_signature.md`** — that doc (dated
2026-05-23) documents the *pre-fix* state and is now **stale**; it should be marked
as resolved-by-`81978321e3`.

### A second finding: `normalizedConfidence` is unreliable as a scaling factor

`normalizedConfidence` does **not** track the final rank. For the *same stable,
correct* C-minor key it ranges across regions from **0.025 to 1.00** (e.g. rank-0
conf: 0.0797 @tick240, 0.9776 @tick720, 0.0273 @tick1440, 1.0000 @tick12240). Cause:

- It is assigned at `KeyModeAnalyzer` ranking time — winner (i==0) gets a global
  `confidence`; runners-up get a sigmoid of their *score-gap to the next candidate*
  ([keymodeanalyzer.cpp:738-747](src/composing/analysis/key/keymodeanalyzer.cpp#L738-L747)).
- `resolveKeyAndModeRanked` then **re-ranks** via `promoteWinnerInPlace` for
  hysteresis ([keyresolver.cpp:311-321](src/composing/analysis/key/keyresolver.cpp#L311-L321))
  and the declared-mode prior (L329+), **without recomputing
  `normalizedConfidence`**. A promoted candidate carries its old runner-up
  confidence to rank 0.

So Step 3's "minimum viable form" (scale oracle terms by the winning key's
`normalizedConfidence`) is **mechanically unsound as written**: it would throttle the
diatonic bonus to ~3% on regions where C minor is unambiguously correct, injecting
noise into a *correctly* keyed piece. Any confidence-scaling design must first define
a confidence metric that survives the re-ranking (recompute after promotion, or use
the raw winner-vs-runner `score` gap directly).

---

## Implications for Step 3 implementation

1. **Corelli `op01n08d` is no longer a key-detection failure.** The Step 3 target
   case in `redesign_plan.md` (L150, L236-244) and COWORK_HANDOFF.md (L934, L948,
   L972) is obsolete. Key-as-distribution will not change its output, because the
   key is already C minor.

2. **The "open question" the plan posed is answered, but moot:** the correct key is
   not a runner-up — it is the confident winner. The double-run / full-form oracle
   is *not* needed for Corelli, and the minimum-viable form is *not* needed for
   Corelli either.

3. **Residual `op01n08d` failures are not key-driven.** Per commit `81978321e3` and
   `key_detection_baroque_partial_signature.md` §"three remaining symptoms":
   - **m1 b3 / m24 `G`→`Gm`, `F`→`Fm`**: thirdless-dominant / chord-quality on sparse
     V slices. Needs a *key-confidence-gated dominant-quality fix* in
     `sparsechordrefinement` (explicitly deferred; has a chopin_bi105_op30_2
     segmentation cascade). This is quality logic, not key detection. *Note:* this is
     the one place a real key-confidence signal would help — but in
     `sparsechordrefinement`, not in the `diatonicRootBonus` scaling the plan
     proposes.
   - **m2 b3 `G/B`→`G`**: inversion / root-position-preference.
   - **m18**: segmentation (region absorption).

4. **If Step 3 proceeds at all, it needs a different motivating case** — a score
   where the key is *genuinely* ambiguous or wrong with the correct key sitting as a
   runner-up. None was found here. Before building key-as-distribution, run the
   ranked diagnostic across the corpus to find a case that actually exhibits the
   "correct key is rank 1/2" pattern; otherwise Step 3 is infrastructure with no
   live target. (Candidates worth checking: other partial-signature pieces the doc
   lists — op01n03 D/A, op01n09 G, op01n10 G — to confirm Option B fixed them too, or
   surface any it missed.)

5. **Two cleanups orthogonal to Step 3, surfaced by this pass:**
   - Mark `key_detection_baroque_partial_signature.md` as resolved by `81978321e3`
     (or move it to a "history" section) — it currently reads as a live bug.
   - Document / remove the dead `HarmonicFunctionContext::keyFifths` and `::keyMode`
     fields (Part A).

---

## Working-tree state

`regionanalyzer.cpp` restored to HEAD byte-for-byte (empty `git diff`, no KEY-DIAG /
`fprintf` / `cstdio` remnants). The only working-tree changes are the pre-existing
session-start ones (CLAUDE.md, docs/redesign_plan.md, `ai-assistant/*`, `tools/*`),
none touched by this pass. A rebuild was kicked off to restore the production binary
(the build tree had transiently contained the instrumented version). No commits made.

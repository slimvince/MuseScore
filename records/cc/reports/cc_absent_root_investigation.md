# Absent-Root Guard Investigation

**Date:** 2026-06-08 · **HEAD:** `f9ba22157d` · **Preset:** Baroque
**Baselines (confirmed):** pipeline snapshots 11/11 (1 skipped).
**Scope:** read-only investigation. No code changes, no commits.

**Tooling note:** `batch_analyze --diagnose-measures N` emits per-PC weights and the
full root×template scoring breakdown, but only for **beat 1** of each named measure.
`--dump-regions notation` / `notation-premerge` give the production region stream with
per-tone raw weights. The target scores live in `tools/corpus/*.xml` (not
`src/composing/tests/`, which the instruction's example paths assumed).

Region-level summaries were cross-checked against
`tools/iter97_birfalse_cases_data.txt` and `docs/iter97_bir_false_categorization.md`.

---

## Part 1 — bwv174.5 and bwv301 reclassification

`extensionThreshold` (Baroque) = **0.20** (confirmed: `chordanalyzer.h:459`,
default 0.20, range 0.10–0.30). "Present" = pcWeight **> 0.20**.

### bwv174.5 — batch analysis findings

Region m4 b1 (tick 6240), key D major. Diagnostic (`--diagnose-measures 4`):

| PC | weight | role |
|---|---:|---|
| B (11) | 0.60 | present |
| F# (6) | 0.20 | **at threshold** (not > 0.20) |
| G# (8) | 0.20 | **at threshold** (not > 0.20) — this is the bass AND the DCML root |

- **Our emitted chord:** `E/G#` Major (root E, bass G#).
- **Our root PC weight:** E (4) = **0.0 — absent.** ✓ (E is not in {F#,G#,B}.)
- **DCML root:** Ab≡G# (DCML = G#m / "incomplete minor-seventh"). G# weight = **0.20**,
  i.e. exactly **at** the threshold, present only as the bass.
- The diagnostic's own full-region rank-1 is **G#ø7 / G#m7 (root G#)** at 1.89 — i.e.
  the oracle, scoring the whole region, already favours the DCML root. But the
  production winner `E/G#` scores **2.16**, which is *above* the diagnostic's full-region
  maximum (1.89) → the `E/G#` winner does **not** come from main-region scoring; it
  comes from a sub-region call (same shape as bwv14.5, see Part 2).

**Verdict: absent-OUR-root CONFIRMED**, with a caveat — the DCML root G# sits *at* the
threshold (0.20), not above it. The full G#m triad is itself incomplete in the region
(no D#; only G#, B sound, with F# as the m7). So this is a real absent-our-root case,
but the DCML target is only borderline-present.

### bwv301 — batch analysis findings

Region tick 960–1920 (m1 b3), key D minor. The BIR=false region is at **beat 3**, which
`--diagnose-measures` cannot target (it emits beat 1 only), so weights are read from
`--dump-regions notation`:

| PC | raw region weight | role |
|---|---:|---|
| D (2) | 1.25 | present (joint-highest) |
| B (11) | 1.25 | present (joint-highest) — **DCML root** |
| A (9) | 1.05 | present — the bass |
| C (0) | 0.25 | present (weak) |
| Ab/G# (8) | 0.20 | borderline |

- **Our emitted chord:** `G/A` Major (root G, bass A), score 2.16, margin 0.
- **Our root PC weight:** G (7) = **0.0 — absent.** ✓ (G is not in the tone set.)
- **DCML root:** B (11) = **1.25 — strongly present**, well above threshold.
- This score (2.16) matches the region's `chordScore` exactly, so unlike bwv14.5/bwv174.5
  the `G/A` winner here comes from the **main-region** scoring, not a sub-region.

**Verdict: absent-OUR-root CONFIRMED — the cleanest of the three.** Our root G is fully
absent; the DCML root B is strongly present (1.25, joint-highest weight).

### Summary: how many cases does the absent-root guard address?

All **three** target cases are genuine absent-OUR-root cases (our winner's root is absent,
the DCML root is in the pc-set). None is a "DCML-root-not-in-pcs" (Phase-D) case.
This matches the reclassification in `COWORK_HANDOFF.md:540`.

**Important nuance on the DCML-root-present strength** (governs whether the guard can
actually *fix* each case, vs merely reject the wrong winner):

| Case | our root weight | DCML root | DCML root weight | DCML target cleanly available? |
|---|---:|---|---:|---|
| bwv301  | 0.0 (G) | B  | **1.25 (strong)** | B-rooted, but bass=A; no B-rooted candidate surfaces (segmentation) |
| bwv14.5 | 0.0 (G) | Bb | ~0.20 (sub-region, at threshold) | degenerate sub-region; Bb weak, F (5th) absent |
| bwv174.5| 0.0 (E) | G# | **0.20 (at threshold, not above)** | G# present only as bass; G#m triad incomplete |

So the guard's *firing* condition (our root absent) is satisfied by all three, but a
clean present-root *swap target* exists for **none** of them under a strict `> threshold`
test. This is the central risk (see Part 4 and the recommendation).

---

## Part 2 — bwv14.5 sub-region call site

### Which Pass produces the {C,D,Bb} sub-region?

`regionanalyzer.cpp` has three `analyzeChord` call sites:
- **Pass 1** (L446) — coarse boundary regions.
- **Pass 2** (L648) — onset-Jaccard sub-boundaries (`detectOnsetSubBoundaries`).
- **Pass 2b** (L834) — iterative bass-movement sub-boundaries (`detectBassMovementSubBoundaries`).

Both Pass 2 and Pass 2b only subdivide parents **≥ 1920 ticks** (one 4/4 bar):
`kPass2MinRegionTicks = kPass2bMinRegionTicks = 4 × DIVISION` (`metricweights.h:69`).

The `notation-premerge` dump confirms the sub-region exactly:

```
startTick 8160, endTick 8400 (240 ticks = one eighth), chordSymbol "Gm/Bb",
rootPc 7 (G), bassPc 10 (Bb), score 2.66, margin 0
tones: C(w0.2), D(w0.6), Bb(w0.2, bass)   →  pcs = {C, D, Bb}   ✓ matches the brief
```

Both passes are *candidates* to create the 8400 boundary, because at tick 8400 the onset
set changes (a new upper note E + a new bass C enter — onset boundary, Pass 2) **and**
the bass moves Bb→C (bass-movement boundary, Pass 2b). Pass 2 runs first; if its
onset-Jaccard detects the boundary it creates the 240-tick region and Pass 2b then sees a
<1920-tick region and skips it. The in-file comment (L109–113) attributes 240-tick
sub-regions specifically to "Pass 2b's bass-movement splitting," so Pass 2b is the
documented mechanism, but Pass 2 may pre-empt it here.

**Definitive attribution requires a one-line diagnostic** (NOT added — investigation
only): inside Pass 2's else-branch push (after L707) and Pass 2b's push (after L882),
print `subStart.ticks(), subEnd.ticks(), chosenSub.identity.rootPc` guarded by
`subStart.ticks() == 8160`. Whichever pass prints first owns the split. Best assessment:
**Pass 2 (onset) most likely creates the 8160–8400 region**, with Pass 2b as the fallback;
either way the {C,D,Bb} sub-region and its absent-root Gm winner are produced by a Pass-2/2b
sub-region `analyzeChord` call.

### Why does E drop out?

E (MIDI 64) **onsets at tick 8400**, which is the *start of the next* sub-region. The
following premerge region (8400–8640, "Gm6/C") contains E (pitch 64, tpc 18) plus the new
bass C. So E never sounds during 8160–8400; the 240-tick window legitimately contains only
{C, D, Bb}. It is a **tick-range slice**, not a register/voice filter — E is a later
onset, not a different register that got excluded.

### How does the sub-region winner propagate to the parent?

**Outright, unconditionally.** Each pass rebuilds the whole `regions` vector from its
sub-regions (`regions = std::move(pass2Regions)` L712; `…pass2bRegions…` L886). The
sub-region's `chordResult` is set to `chosenSub` — the sub-region's *own* `analyzeChord`
winner (L701 / L876) — completely **replacing** the parent's Pass-1 identity for that span.
It is not stored as an alternative. The only "condition" is the contiguous same-root+quality
merge (L686–696): if the previous sub-region has identical root & quality it is extended;
otherwise a fresh sub-region carrying the new winner is pushed. Gm/Bb differs from its
neighbours (F/A, Adim, Gm6/C), so it survives as a standalone region all the way to the
final (merged) output, which is why it appears as the BIR=false region.

**Consequence for the guard:** because `applyHarmonicFunction` runs *inside* every
`analyzeChord` call (E2d redesign — `STATUS.md` header; regionanalyzer.cpp L666–667,
L853–854), the proposed guard location **is reached by the Pass-2/2b sub-region call** that
produces Gm/Bb. This is the decisive advantage over the previous deduction-block location,
which the sub-region path never exercised for this case.

---

## Part 3 — 5 regression cases from the previous guard

### Regression case identification

The previous attempt placed an absent-root guard in the **inversion-deduction block**
(the `bestAltIdx` swap logic, currently `chordanalyzer.cpp` L1959–2329; the brief's
L2839–2880 are line numbers from an earlier revision). It was **tried and reverted without
being committed** (`COWORK_HANDOFF.md:583–585, 600–603`). There is **no commit or stash** to
diff — the 5 affected scores were never enumerated by name. They are 5 of the **11 DCML-
verified golden scores** in the pipeline-snapshot corpus
(`pipeline_snapshot_tests.cpp:150–191`): Bach chorales 001/003/137, BWV806 prelude & gigue,
Mozart K279-1 & K280-1, Chopin BI105-1 & BI105-2, Corelli op01n08a, Schumann n01.

(There is a *separate*, committed, narrower absent-root guard from earlier: `57511f012f`
"guard Gates E and I against absent-root promotion (Iter 82)" — already in the baseline,
not the reverted attempt.)

### Characterisation of each case (by mechanism — names not recoverable)

The deduction block's entire job is to **swap the winner with a clean different-root
ALTERNATIVE** to correct a mis-rooted inversion (Gates B/C/D/E/F + the bass-bonus deduction,
plus G-E/H/I/K/L downstream). Every gate does `std::swap(results[0], results[bestAltIdx])`.
Crucially, these gates *deliberately* promote alternatives whose root may be weakly present:

- Gate E already requires `pcWeight[altRoot] > extensionThreshold` for its swap (L2116) —
  but the **HalfDim first-inversion path explicitly exempts a root tone below threshold**
  (L1988–1994: bwv187.7, the inversion bass at weight 0.14 < threshold 0.20 is exempted so
  the correct inverted ø7 is not blocked).
- The bass-bonus deduction (L2157–2161) flips to a first-inversion reading on a tight margin.

A blanket "reject if winner root ≤ threshold" guard inserted **here** therefore mis-fires on
exactly these legitimate corrections: the correct first-inversion reading the gate is trying
to install has a root that is a genuine but weakly-sounding chord tone (≤ threshold), so the
guard blocks the swap and the wrong root-position reading stays. That is the regression shape
the handoff describes ("blocked a correct winner swap"). And — as the handoff notes — it did
**not even fix bwv14.5**, because in the parent region the block's `bestAltIdx` pointed at
D Dom7, not Gm (Gm comes from the sub-region, never reaching this block).

### Would they regress at the new location?

**Most likely no — for a structural reason.** The new guard runs in `applyHarmonicFunction`
at the cross-bass winner point (L283), **before** the deduction-block gates execute (those run
later, in `applyPostScoringGates`). For a legitimate inversion-correction case, the winner at
L283 is the **root-position reading, whose root IS present** (it won the vertical competition
precisely because of the bass-root bonus). The correct first-inversion reading is the
*alternative* that the later gates swap in. So at L283 these cases present a **present-root
winner → the absent-root guard does not fire → the later swap proceeds untouched.** The 5
prior regressions should not recur at this location.

**Residual risk (different from the old one):** a case where the *cross-bass winner itself*
at L283 is a correct-but-weak/absent-root reading. That cannot be ruled out from static
analysis; it must be checked by re-running the 11-score snapshot suite after implementation.

---

## Part 4 — Guard location assessment

### applyHarmonicFunction winner-selection point

The 7 steps map cleanly onto `harmonicfunctionlayer.cpp`:

1. Pass A — vertical score + rootContinuity + w_complete + w_seq[+w_dim] per bass (L203–226).
2. Pass B — step-bonus + surgical guard (L229–230).
3. Pass C — local best per variant; track global best per bass group (L232–253).
4. Post-bonus quality guard — pick with-/without-wDim variant; fixes `chosenPerBass`,
   `winBassPc` (L255–272).
5. **Sort the winning bass group (L275–280) → `chosenPerBass.front()` is THE winner cell.**
6. Threshold (L282–286).
7. Build results[] / diff-root append / fill gateCtx (L288–352).

**The single clearly-identified winner cell exists at L283** (`chosenPerBass.front()`),
i.e. after cross-bass selection (step 4) and before results[] is built (step 7) — exactly
the insertion point the brief asks about. A guard would check
`snapshot.pcWeight[chosenPerBass.front().rootPc] <= prefs.extensionThreshold` and, if the
root is absent, scan `chosenPerBass` for the best present-root candidate within margin and
move it to front before the threshold/build steps.

### pcWeight data availability

**Available, no signature change needed.** `ScoringSnapshot` carries
`std::array<double,12> pcWeight` (`harmonicfunctionlayer.h:172`), and the function already
uses it (`buildCtx` L290, `gateCtx->pcWeight` L336). `prefs.extensionThreshold` is in scope
via the `prefs` parameter. The guard has everything it needs in-place.

**One caveat:** at L283 the candidate pool is only the **winning bass group**
(`chosenPerBass`). Best candidates of *other* bass groups are discarded after Pass C
(only `bestPerBassWith/Without` for the global winner survive). A guard that needs to swap
to a present-root candidate on a *different bass* (e.g. bwv301's DCML B-rooted reading,
where the region bass is A) would require retaining per-bass-group bests — extra state.
A within-bass-group-only guard is the simple option but is insufficient for bwv301.

### Gate J interaction (conflict or mutually exclusive?)

**No conflict — mutually exclusive, and temporally separated.** Gate J
(`chordanalyzer.cpp` L2437–2461) fires only when:
1. the winner is a **root-position diminished triad** (root = bass, so its root is present), and
2. `pcWeight[domRootPc] > extensionThreshold` — the dominant root (M3 below) **is present**;
then it swaps to the dom7 at `domRootPc`, whose root is present by construction.

Both Gate J's input winner (present root) and output winner (present dom root) are
present-root. The absent-root guard fires only on **absent-root** winners. The two act on
disjoint winner sets. Additionally, Gate J runs in `applyPostScoringGates`, **after**
`applyHarmonicFunction`, so the guard runs first and Gate J simply sees whatever winner
survives. They cannot conflict.

### Margin calibration for target cases

The score margin between the absent-root winner and the **best present-root alternative**
is **not extractable from current batch output** for any of the three: the present-root
candidates fall below the emitted top-3 (`results[]` only carries the absent-root winner and
its absent-root neighbours), and `--diagnose-measures` cannot target the beat where two of
the three regions live (bwv301 b3; bwv14.5/bwv174.5 sub-regions).

What *is* known:

| Case | winner (absent root) | emitted runner-ups | best present-root alt | margin to present-root alt |
|---|---|---|---|---|
| bwv14.5 | Gm/Bb 2.66 | Am/Bb 2.62, Gb+/Bb 2.36 (both absent-root) | not in top-3; only D is >threshold in sub-region | unknown, > 0.30; target (Bb) is only *at* threshold |
| bwv174.5| E/G# 2.16 | E/G# 2.16 (tie) | G#ø7/G#m7 ~1.89 (full-region oracle); G# at threshold | unknown; sub-region winner 2.16 > oracle max 1.89 |
| bwv301  | G/A 2.16 | G/B 2.16 (same root G) | none surfaces (B-rooted needs bass≠A) | unknown; B strong (1.25) but no candidate |

A simple "reject if root absent" guard is therefore **not safe to calibrate yet**, and a
"within-margin, swap to present-root" guard cannot be tuned without the missing data. To get
it (NOT done — investigation only): add a temporary dump at L283 in `applyHarmonicFunction`
printing, for each candidate in `chosenPerBass`, `rootPc / pcWeight[rootPc] / score`, for the
three target regions, to confirm whether a present-root (>0.20) alternative exists within a
usable margin.

---

## Recommendation

The `applyHarmonicFunction` location is **structurally viable and low-risk to *add***: the
winner cell is cleanly identified at L283, `snapshot.pcWeight` and `extensionThreshold` are
already in scope (no signature change), Gate J is provably non-conflicting (disjoint
conditions, and it runs later), and the 5 prior deduction-block regressions are unlikely to
recur because at L283 those legitimate inversion-correction cases present **present-root**
winners (the weak-root reading is the *alternative* the later gates swap in, not the
cross-bass winner). It is also the *only* location that the bwv14.5/bwv174.5 sub-region calls
actually reach, since `applyHarmonicFunction` runs inside every `analyzeChord`.

**However, the guard is unlikely to *correctly fix* the three target cases as a pure scoring
change, and that is the real open question — not safety.** For all three, our root is cleanly
absent, but **no clean present-root swap target exists above threshold**: bwv301's DCML root
B is strong (1.25) yet has no candidate because the region bass is A (a segmentation
artifact); bwv14.5's sub-region is degenerate (Bb at threshold, its 5th F absent); bwv174.5's
DCML root G# sits *exactly at* 0.20, present only as the bass with an incomplete triad. This
matches `iter97`'s classification of bwv14.5/bwv301 as **segmentation** cases ("no targeted
scoring fix can reach these; they need finer boundaries at the bass-motion ticks") and
bwv174.5 as a Sub-pattern-C rootless-winner.

**The guard should be "within-margin + requires a present-root (>extensionThreshold)
alternative to promote," never a blanket reject** — a blanket reject would either fall to a
wrong present-root (e.g. D in bwv14.5's sub-region) or have no target at all. Remaining
unknowns before an implementation instruction: (1) the actual present-root alternative scores
and margins at L283 for the three regions (needs the one-line diagnostic dump described in
Part 4d); (2) whether a usable present-root candidate exists within the winning bass group at
all, or whether cross-bass-group retention is required (definitely required for bwv301);
(3) empirical confirmation on the 11-score snapshot suite that no correct-but-weak-root
cross-bass winner regresses. **It is safe to proceed to writing an implementation instruction
only after the L283 diagnostic dump is run** — and that dump may well show the guard cannot
correctly fix bwv14.5/bwv301, in which case segmentation (finer boundaries at bass-motion
ticks, so E is not dropped and the bass-transition region is not formed) is the correct fix
rather than an absent-root scoring guard.

---

## Acceptance criteria

| Check | Result |
|---|---|
| bwv174.5 reclassification | **Confirmed** — root E w=0.0 absent; DCML root G# present at 0.20 (at threshold, as bass) |
| bwv301 reclassification | **Confirmed** — root G w=0.0 absent; DCML root B strongly present (1.25) |
| bwv14.5 sub-region caller | **Pass 2/2b** sub-region call; tick **8160–8400** (240t); E drops out because it onsets at 8400 (next sub-region); winner **overrides parent outright** |
| Previous 5 regressions characterised | Deduction-block swap-blocking on legitimate weak-root first-inversion corrections; not name-recoverable (uncommitted); 5 of 11 DCML snapshot goldens |
| applyHarmonicFunction location assessed | Winner at L283; pcWeight in snapshot (no sig change); Gate J non-conflict (disjoint + runs later) |
| Code changes | **None** |
| Commits | **None** |

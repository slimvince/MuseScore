# CC Stage 2.4 — Path-divergence decisions report

**Base:** `fb8b980948`. **Scope:** investigate → draft decisions → one surgical fix (D-GAP)
+ doc riders. **Commits NOT made:** V1 (riders 1–3 + ARCHITECTURE.md decision section) and
V2 (D-GAP fix) are **ratification-gated by design** — they sit in the working tree / this
report awaiting Cowork. V3 (bookkeeping docs) per §6.

Every claim is tagged **[code]** (read the source) or **[probe]** (ran it). Standing rules:
never-guess; investigate-or-state-unknown.

---

## §1 — Task-1 findings

### 1.1 — HEADLINE: the Jazz/Baroque **chord-scoring** preset is a batch-tools-only concept. It never reaches the live product.

**Answer to the gating question — when a user works on a jazz chart in the app, do
Jazz-tuned `ChordAnalyzerPreferences` EVER apply on P1/P2/P3/P4? NO. [code]**

The live notation analysis path **always** scores chords with
`kDefaultChordAnalyzerPreferences` (the bare struct default). The preset-specific
`ChordAnalyzerPreferences` values (Jazz `extensionThreshold=0.12` + reduced inversion
bonuses; Baroque `preferMinorOverMajorAdd6=true`) are constructed in **exactly one place
in the entire tree** — `tools/batch_analyze.cpp:1352–1370` — and are passed only into the
batch region path. They are never wired into the product.

Trace [code]:
- `tools/batch_analyze.cpp:1352–1370` builds `chordPrefs` from `presetName`
  (Jazz/Baroque/Standard/Modal/Contemporary). It flows to `analyzeScore` →
  `analyzeRegions(..., chordPrefs, ...)` (`batch_analyze.cpp:528`). This is the BIR-measured
  path.
- The notation/product entry `analyzeHarmonicRhythm`
  (`notationharmonicrhythmbridge.cpp:131–133`) passes **`kDefaultChordAnalyzerPreferences`
  hardcoded**. The only thing it reads from `IComposingAnalysisConfiguration` is
  `onsetBoundaryThreshold` (a Pass-2 segmentation knob) and the **21 mode priors** → these
  go into `KeyModeAnalyzerPreferences keyPrefs` (key/mode detection), **not** into
  `ChordAnalyzerPreferences`.
- Every other live chord-scoring site is the same hardcoded default:
  `analyzeSection`/`inferGapRegion` (`sectionanalyzer.cpp:607/614/617`), `findTemporalContext`
  bridge walk (`regiontonecollector.cpp:805/812/815/863…`), the P4 tick-local path
  (`notationcomposingbridge.cpp:437/444/447`), the P3 regional snapshot. All
  `kDefaultChordAnalyzerPreferences`.
- **Verified by exhaustive grep [code]:** the ONLY non-default `ChordAnalyzerPreferences`
  constructions in `src/` are in **test files** (`chordanalyzer_tests.cpp`,
  `chordanalyzer_musicxml_tests.cpp`, `postscoringgates_tests.cpp`, `diagnose_tests.cpp`,
  `gater_tests.cpp`, `functionlayer_tests.cpp`). No production `src/` code mutates a single
  `ChordAnalyzerPreferences` field. `composingconfiguration.cpp` exposes **only** mode-prior
  preset helpers (`applyModePriorPreset` / `currentModePriorPreset`).

**The preset-name collision (important and easy to misread). [code]** The app's Preferences
panel *does* have "Standard / Jazz / Modal / Baroque / Contemporary" buttons
(`ComposingAnalysisSection.qml:351–358`, enabled only when `inferKeyMode`). They sit directly
above the 21 mode-prior sliders and call `applyPresetRequested → applyModePriorPreset` — i.e.
they set **only the 21 key/mode priors**. The batch `--preset` of the *same name* sets those
21 priors **plus** `ChordAnalyzerPreferences`. So:

| "Jazz" means… | mode priors (key detection) | ChordAnalyzerPreferences (chord scoring) |
|---|---|---|
| **app Preferences "Jazz" button** | set (21 values) | **untouched → default** |
| **batch_analyze `--preset Jazz`** | set (21 values) | **set** (extThresh 0.12, reduced inversion bonuses, preferMinorOverMajorAdd6=false) |

Consequence: the **BIR Jazz/Baroque gate measures a chord-scoring configuration that no user
can produce in the app.** The live product's chord scoring is not even batch "Standard"
(which sets `preferMinorOverMajorAdd6=true`, `chordanalyzer.h` default is `false`) — it is the
raw struct default. [code]

**This is a product-level finding, not a code bug.** It does not, by itself, mean anything is
wrong — but it decides D-PASS0 (§2) and is material to how the BIR gate is described.

### 1.2 — D-GAP blast radius

`analyzeSection` takes no `ChordAnalyzerPreferences`; its gap-inference lambdas hardcode
`kDefaultChordAnalyzerPreferences` (`sectionanalyzer.cpp:607/614/617`). [code] Threading the
caller's prefs through `analyzeSection → inferGapRegion → analyzeGapWithContext`:

- **(a) notation / snapshot / implode callers** (`notationcomposingbridge.cpp:248,1125`,
  `notationimplodebridge.cpp:1377`, `pipeline_snapshot_tests.cpp:324,723,1069`) pass **default
  prefs anyway** (the live Pass-0 itself uses default — §1.1) → threading changes **nothing**
  there. **Expected: snapshots byte-identical. Confirmed [probe]: 11/11 zero diffs.**
- **(b) batch `--section-level` under a preset** is the only behavior change — the diagnostic's
  gap inference now uses the same preset chordPrefs as its Pass-0 stream instead of silently
  falling to default.
- **BIR gate path is untouched.** The flag-off batch path (`sectionLevel=false`) calls
  `analyzeScore → analyzeRegions`, never `analyzeSection` (`batch_analyze.cpp:528 vs 546`).
  **Expected: byte-identical. Confirmed [probe]: flag-off `--preset Baroque` output on
  bwv187.7/bwv5.7/bwv303 is byte-identical to the committed `tools/corpus/baroque/*.ours.json`
  (generated by the pre-fix binary).**

So D-GAP is **user-neutral and gate-neutral by construction**, both halves now empirically
confirmed. The fix is taken (§3).

### 1.3 — P4 reality check [code]

`analyzeHarmonicContextAtTick` (`notationcomposingbridge.cpp:473–500`) is the per-note entry.
It calls **P3** `analyzeHarmonicContextRegionallyAtTick` first; only if `regional.chordResults`
is **empty** does it fall through to **P4** `analyzeHarmonicContextLocallyAtTick` (`:491–497`).
P3 returns empty only when `analyzeSection` yields **zero regions** for the (expanding) measure
window (`:253` `section.regions.empty()` → empty snapshot). For any tick with sounding notes in
a normally-populated score, P3 succeeds and **P4 does not fire**. P4 is genuine
graceful-degradation for empty/contentless windows.

**Exact live frequency: unknown / unmeasured.** The per-tick API is not exercised by
`batch_analyze` (which uses `analyzeScore`/`analyzeScoreNotation`, not the per-note path), and
the snapshot suite dumps the P4 tick-local view **unconditionally** (not gated on "P3 returned
empty"), so it does not measure the fallback rate. Establishing the real rate needs instrumenting
`analyzeHarmonicContextAtTick` in the live app — not cheaply scriptable. Stated unknown, bounded
by the structural argument above (rare).

### 1.4 — Bridge Step-1/2 field state today [code]

Confirmed as expected. `ChordTemporalContext`'s Step-1/2 progression fields default to
`previousWinnerScore=0.0`, `previousWinnerMargin=-1.0`, `previousWinnerRootPcWeight=0.0`,
`previousDistinctPcs=0` (`chordanalyzer.h:663–675`). The **only** writer is
`advanceTemporalContext` (`chordanalyzer.h:900–905`), called at the `regionanalyzer` commit
sites (batch/region path). The bridge-path builder `findTemporalContext`
(`regiontonecollector.cpp:749`) **never assigns them** — it cold-analyzes both neighbours with
`nullptr` context and writes only `previousRootPc/Quality/BassPc` + `nextRootPc/BassPc` +
`bassIsStepwise*`. Its own comment states this verbatim (`:774–776`: "Still NOT populated: the
Step 1/2 progression fields … which require the neighbour's committed competition result —
unavailable without a full forward pre-pass"). So on the bridge path the predecessor-confidence
signals are **inert** (margin sentinel −1.0, weights 0.0).

---

## §2 — Decision drafts (paste-ready: ARCHITECTURE.md new section "Path divergence decisions (Stage 2.4)")

> The four decisions below are written to be pasted verbatim into ARCHITECTURE.md once Cowork
> ratifies. Each has Facts (evidence-tagged), Decision, Revisit trigger.

---

### Path divergence decisions (Stage 2.4)

Four analysis-path divergences accumulated across the part-2 implementation review, the corpus
audit (Findings 3/4), and the 2.2-i section-level dossier (§2/§7). They are decided here so they
are not rediscovered. The unifying theme: the **batch BIR-measurement path** and the **live
notation path** are not the same configuration, and the **greedy feed-forward pipeline** builds
temporal context per-commit rather than from a global decode. Stage 3 (the lattice decoder) is
where accumulated context becomes a decode product; decisions that would be torn up by Stage 3
are deferred to it rather than pre-built now.

#### D-P4 — tick-local path builds temporal context cold

**Facts.** The P4 tick-local fallback (`analyzeHarmonicContextLocallyAtTick`) builds its
`ChordTemporalContext` via `findTemporalContext`, which cold-analyzes the backward and forward
neighbours with `nullptr` context and no accumulated rolling state [code]. It fires only when
the P3 regional path returns no region for the surrounding window — structurally rare; exact
live frequency unmeasured [code]. The same chord can therefore in principle answer differently
on P4 vs P3.

**Decision.** Cold context on P4 is the **current contract**, documented and accepted (the same
precedent as the Stage 2.3 diagnose context banner: a path may legitimately analyze with less
context, provided that is stated, not silent). No pre-pass is built now: Stage 3's lattice makes
accumulated context a decode product, and any context pre-pass built against the greedy pipeline
would be discarded at Stage 3.

**Revisit trigger.** Stage 3 design **must** state explicitly what P4 (and the bridge) consume
from the decode. If P4's empty-window fallback rate is ever shown to be non-trivial (requires
instrumenting the per-tick API), revisit earlier.

#### D-BRIDGE — bridge predecessor analyzed with null context; Step-1/2 fields inert

**Facts.** `findTemporalContext` analyzes the backward predecessor (and forward successor) with
`nullptr` context [code]. The Step-1/2 confidence fields
(`previousWinnerScore/Margin/RootPcWeight`, `previousDistinctPcs`) are default-initialized
(`-1.0`/`0.0`/`0`) and never written on the bridge path — only `advanceTemporalContext` (region
commit sites) writes them [code]. So predecessor-confidence progression signals are inert on the
bridge path; the bridge populates only the root/quality/bass neighbour fields the downstream
gates need.

**Decision.** Same as D-P4: this is the **current contract**, documented. The forward-lookahead
gap that previously left `nextRootPc=-1` was already closed (`90a52b5fee`); the residual
(Step-1/2 confidence fields) genuinely requires a committed competition result from the
neighbour, i.e. a forward pre-pass over the score — exactly the global-decode product Stage 3
provides. Do not build a bespoke pre-pass now.

**Revisit trigger.** Stage 3 design must state what the bridge consumes. The decoder's path
state supersedes `findTemporalContext`'s cold walk.

#### D-PASS0 — notation Pass-0 uses default prefs + `excludeLookAheadOnDenseStart=false`; batch uses preset prefs + `true`

This divergence has **two independent halves**; Stage 2.4 investigation (§1.1) decides them
separately.

**Half A — chord-scoring preferences (the headline). Facts.** The Jazz/Baroque
`ChordAnalyzerPreferences` are constructed only in `tools/batch_analyze.cpp` and never reach the
product; every live chord-scoring site uses `kDefaultChordAnalyzerPreferences` [code]. The
app's "Jazz/Baroque/…" Preferences buttons set only the 21 mode priors (key detection), not
chord-scoring prefs [code]. The BIR Jazz/Baroque gate therefore measures a chord-scoring
configuration **no user can produce in the app**.

**Decision (Half A).** Record this as a **product-level finding**, not a code change. The
chord-scoring preset system is currently a **measurement-only artifact** of `batch_analyze`. Do
**not** silently flip the live product onto preset chordPrefs — whether the product should expose
a chord-scoring style is a deliberate **product decision**, deferred. Until then, all docs that
imply Jazz/Baroque chord tuning ships to users must be corrected to "batch-measurement only."
The live product analyzes chords with struct defaults (not even batch "Standard").

**Decision (Half B — `excludeLookAheadOnDenseStart`).** Unchanged and intentional. Batch passes
`true`, the bridge defaults `false`; this is the **D1 / Iter-97 load-bearing divergence**
(unifying it regresses the Corelli trio-sonata dominants on the bridge). Keep diverged;
keep documented.

**Revisit trigger (Half A).** Any product initiative to expose a chord-scoring "style" to users;
any Stage-5 metric work that wants the gate to measure the *user* configuration (note: that would
mean re-tuning against `kDefaultChordAnalyzerPreferences`, not the batch preset). Until one of
those, the gate stays as-is and is **described accurately** (batch-measurement configuration).

#### D-GAP — `inferGapRegion` analyzed gap slices with default prefs regardless of caller

**Facts.** `analyzeSection`'s gap inference hardcoded `kDefaultChordAnalyzerPreferences`
(`sectionanalyzer.cpp:607/614/617`) [code]. Under a preset, the section diagnostic mixed
**preset Pass-0 + default gap analysis** — internally inconsistent. The 2.2-i dossier (§7.2)
hypothesized this leak as the likely cause of all 3 genuine Baroque A/B regressions.

**Decision.** **Fixed now** (Stage 2.4 surgical fix — §3): the caller's `ChordAnalyzerPreferences`
are threaded through `analyzeSection → inferGapRegion`. Proven user-neutral + gate-neutral
(snapshots 11/11 zero diffs; flag-off BIR path byte-identical) — the live path passes default and
is unaffected; only the batch `--section-level` diagnostic now measures a consistent preset
pipeline. **Causal note:** the fix does **not** heal the 3 Baroque regressions (§3) — under
Baroque the chordPrefs delta from default is only `preferMinorOverMajorAdd6`, so the leak was
nearly inert there; the 3 regressions are structural (measure-split / gap-insertion), not
gap-pref-caused. So the dossier's §7.2 hypothesis is **not supported** for the Baroque cases.
The fix is justified on consistency + user/gate-neutrality, which was the stated bar (healing was
"expected, not required").

**Revisit trigger.** None for the fix itself. The 3 structural regressions and the section-vs-batch
granularity question fold into the Stage-5 granularity-robust metric (already mandated).

---

## §3 — D-GAP fix + verification

**The fix (3 files, working tree, NOT committed — this is V2, ratification-gated):**

- `src/composing/analysis/section/sectionanalyzer.h` — `analyzeSection` gains a 6th param
  `const ChordAnalyzerPreferences& chordPrefs = kDefaultChordAnalyzerPreferences` (defaulted →
  all existing 5-arg callers compile unchanged and pass default).
- `src/composing/analysis/section/sectionanalyzer.cpp` — definition takes the param; the three
  `kDefaultChordAnalyzerPreferences` uses in `analyzeGapWithContext`
  (`analyzeChord`/`applyIter8691Pedal`/`applyPostScoringGates`) → `chordPrefs` (captured by the
  `[&]` lambdas).
- `tools/batch_analyze.cpp` — the `--section-level` call passes `chordPrefs`; the stale comment
  ("Pass-0 stream remains batch's preset path … NOT the notation-bridge default-chordPrefs
  divergence") updated to reflect the threaded preset pipeline.

**Verification.**

| check | result |
|---|---|
| Build | clean (14/14; 2 pre-existing C4100 warnings in chordanalyzer.cpp, unrelated) |
| **pipeline_snapshot_tests** | **11/11 PASSED — ZERO diffs** [probe] (decisive: exercises `analyzeSection` directly) |
| composing_tests | 501/501 [probe] |
| notation_tests | 52/52 [probe] |
| test_batch_analyze_regressions.py | `batch_analyze regressions passed` [probe] |
| **BIR flag-off byte-identity** | bwv187.7 / bwv5.7 / bwv303 `--preset Baroque` flag-off output **byte-identical** to committed `tools/corpus/baroque/*.ours.json` (pre-fix binary) [probe] |
| **BIR full regen** | **Baroque 13 / Jazz 7 — exact identity sets, both held** [probe] |

### 3.1 — BIR full-corpus regen [probe]

Both presets regenerated clean (353/353, manifest-stamped, `git fb8b980948`) and characterised:

- **Baroque: 13 genuine BIR=false** (`TOTAL genuine BIR=false: 13`, 326 WiR-covered, 0 Mozart).
- **Jazz: 7 genuine BIR=false**, identity set `{bwv244.15, bwv245.17, bwv245.40, bwv422,
  bwv432, bwv45.7, bwv74.8}` — **exactly the canonical gate set**.

Both gates **held unchanged**, as predicted by construction (the BIR path is `sectionLevel=false`
→ `analyzeRegions`, never `analyzeSection`). Total aligned regions Baroque 11267 / Jazz 10910
(unchanged from baseline).

### 3.2 — The 3-case causal probe [probe]

The 3 dossier regressions, re-run under `--section-level` with the **fixed** binary, root at the
target tick:

| case (tick) | dossier OFF (=DCML) | dossier ON (default gap) | **fixed, --preset Baroque** | **fixed, --preset Jazz** |
|---|---|---|---|---|
| bwv187.7 (14400) | F | Gm7/Bb (G) | **Gm7/Bb (G)** — unchanged | Gm7/Bb (G) |
| bwv5.7 (19680) | Bb | Am/C (A) | **Am/C (A)** — unchanged | **Bb (=DCML!)** |
| bwv303 (12000) | D | F#m (F#) | **F#m (F#)** — unchanged | F#m (F#) |

**Reading.** Under **Baroque** (the preset the regressions were measured under) all 3 are
unchanged — because Baroque chordPrefs ≈ default (only `preferMinorOverMajorAdd6` differs), so
the gap-pref leak was nearly inert there. **The dossier's hypothesis that the gap-pref leak
caused the 3 Baroque regressions is therefore NOT supported** — they are structural
(measure-split/gap-insertion), independent of chordPrefs. Under **Jazz** (where the pref delta is
large: extThresh 0.12 + reduced inversion bonuses) the threading materially changes gap analysis
— bwv5.7 t19680 now reads Bb, the DCML-correct root — demonstrating the fix is live and the
divergence it closes is real and largest under Jazz. (Limitation: the pre-fix binary was not
rebuilt, so the Jazz Bb-vs-Baroque-A delta is not fully isolated between Jazz-Pass-0 and
Jazz-gap-prefs; the Baroque result already establishes the threading effect is
preset-magnitude-dependent, which is the point.)

---

## §4 — Rider diffs (V1, ratification-gated — drafted, NOT applied)

### Rider 1 — `CLAUDE.md` (template-addition checklist: drop `kDiagTemplates`, removed in Stage 2.3)

Replace lines 158–171 (the `kTemplateCount` model block):

```diff
-**Template additions — the `kTemplateCount` model (since `a236a0ff21`):** All
-template-related array extents (the `analyzeChord` template array, `kDiagTemplates`,
-the three score matrices, `kMasks` in `harmonicfunctionlayer.cpp`) are derived from
-`analysis::kTemplateCount` in `chordanalyzer.h`, so the compiler enforces size
-consistency — the old silent stack-buffer-overrun failure mode (a missed matrix
-resize, caught in the B1 attempt 2026-06-04) is closed. Adding a template means:
-1. Bump `analysis::kTemplateCount` N→N+1 (auto-resizes the matrices and `kMasks`)
-2. Add the new `TemplateDef` entry in `analyzeChord` AND the byte-identical entry
-   in `kDiagTemplates`
-3. Add the interval bitmask to `kMasks` (a zero mask silently disables Gate R)
-
-Remaining trap: bumping the constant **without** adding the entries
-value-initializes a trailing all-zero template (silent) — always do both in the
-same edit. The authoritative checklist is `docs/scoring_model.md` §9.
+**Template additions — the `kTemplateCount` model (since `a236a0ff21`):** All
+template-related array extents (the `analyzeChord` template array, the three score
+matrices, `kMasks` in `harmonicfunctionlayer.cpp`) are derived from
+`analysis::kTemplateCount` in `chordanalyzer.h`, so the compiler enforces size
+consistency — the old silent stack-buffer-overrun failure mode (a missed matrix
+resize, caught in the B1 attempt 2026-06-04) is closed. (Since Stage 2.3
+`18dc9e1829` the duplicate `kDiagTemplates` array is gone — `diagnoseChord` replays
+the production pipeline, so there is **one** template array, not two.) Adding a
+template means:
+1. Bump `analysis::kTemplateCount` N→N+1 (auto-resizes the matrices and `kMasks`)
+2. Add the new `TemplateDef` entry in `analyzeChord`
+3. Add the interval bitmask to `kMasks` (a zero mask silently disables Gate R)
+
+Remaining trap: bumping the constant **without** adding the `TemplateDef` entry
+value-initializes a trailing all-zero template (silent) — always do both in the
+same edit. The authoritative checklist is `docs/scoring_model.md` §9.
```

### Rider 2 — `ARCHITECTURE.md:861` (`contextualBonuses()` → historical phrasing; helper removed Stage 2.3)

```diff
-**Solution:** Contextual bonuses applied only to non-bass-root Major/Minor candidates,
-using information from neighbouring chords. Three bonuses added to `contextualBonuses()`:
+**Solution:** Contextual bonuses applied only to non-bass-root Major/Minor candidates,
+using information from neighbouring chords. Three bonuses were added (historically via a
+`contextualBonuses()` helper — removed in Stage 2.3 `18dc9e1829` when `diagnoseChord`
+became a view into the production pipeline; the bonuses now live in the competition
+pipeline / function layer):
```

### Rider 3 — `docs/layer_architecture_audit.md:92–94` (mark 2b action DONE-by-2.3)

```diff
-**Action for CC:** Update the comment at ~L1634 to note that `contextualBonuses` is
-used by `diagnoseChord` only and intentionally includes `rootContinuityBonus`, while
-`bassIndependentContextualBonuses + bassDependentContextualBonuses` do not.
+**Action for CC:** ✅ **DONE (Stage 2.3, `18dc9e1829`).** Superseded: `contextualBonuses`
+was removed entirely when `diagnoseChord` was rewritten to replay the production pipeline,
+so the stale invariant comment at ~L1634 went with it — there is no comment left to fix
+(the helper no longer exists).
```

---

## §5 — Unknowns / limits (honest)

1. **P4 live fallback rate (§1.3): unknown.** Bounded structurally (empty-window only) but not
   measured; the per-tick API is not exercised by `batch_analyze` and the snapshot P4 dump is
   unconditional. Would need live-app instrumentation.
2. **3-case Jazz isolation (§3.2): partial.** The pre-fix binary was not rebuilt, so the Jazz
   Bb-vs-Baroque-A delta on bwv5.7 is not cleanly partitioned between Jazz-Pass-0 and
   Jazz-gap-prefs. The Baroque-unchanged result already proves the threading effect is
   preset-magnitude-dependent, which is the load-bearing conclusion.
3. **BIR full regen** done (§3.1): Baroque 13 / Jazz 7 exact identity sets — held. (Was a
   by-construction certainty from the byte-identity spot-check + structural argument; the full
   regen is the belt-and-suspenders confirmation.)
4. **No corpus quality re-measurement** (rn cross-corpus) was run — out of scope and unaffected
   by a diagnostic-only behavior change.

---

## §6 — Commit status

- **V1** (riders 1–3 + the §2 ARCHITECTURE.md decision section): **NOT committed** — ratification-
  gated. Drafts above are paste-ready.
- **V2** (D-GAP fix, §3): **NOT committed** — in working tree, ratification-gated. All green.
- **V3** (bookkeeping: STATUS.md + COWORK_HANDOFF.md + docs/implementation_roadmap.md as they
  stand): may be committed directly per the instruction — see final note.

**STOP per instruction:** V1/V2 await Cowork ratification (which arrives as an addendum
instruction file per trust-model rule 4).

---

## §7 — Ratification + V4 (`--preset Default` measurement) — Stage 2.4 follow-through

Cowork ratified V1 + V2 (this addendum). Committed in order:

| Commit | Hash | Contents |
|---|---|---|
| **V1** | `140ceb1a9e` | §2 path-divergence decisions → ARCHITECTURE.md (under the D1/D2 audit) + Half-A "never corpus-measured" sentence; riders 1–3 (CLAUDE.md `kDiagTemplates`, ARCHITECTURE.md `contextualBonuses()`, layer_architecture_audit.md 2b) |
| **V2** | `1a08e96d8a` | D-GAP threading fix (sectionanalyzer.{h,cpp} + batch_analyze.cpp `--section-level` call) |
| **V4** | _this commit_ | `--preset Default` + user-default-config corpus measurement |

(`docs/implementation_roadmap.md` 2.4-row falsification edit is Cowork's; left **unstaged** in the
working tree — not bundled into V1/V2/V4.)

### 7.1 — App-default mode priors ≠ code defaults ≠ "Standard" [code]

V4 step-1 required matching **the app's out-of-box state**, not the struct defaults. Verified by
reading the three sources:

- **App out-of-box** = the 21 `MODE_PRIOR_*` `setDefaultValue` calls in
  `composingconfiguration.cpp` (`init()`, L214–298).
- **Code/struct defaults** = `KeyModeAnalyzerPreferences` member initializers
  (`keymodeanalyzer.h` L211–235).
- **"Standard" preset** = `modePriorPresets()` (`modepriorpresets.cpp` L33–55).

**Finding:** struct defaults == "Standard" preset **exactly** (all 21). But the **app's registered
settings defaults diverge from both on 11 of 21 modes** — Lydian (0.00 vs −1.50), Mixolydian
(−0.20 vs −0.50), Locrian (−3.50 vs −3.00), LydianAugmented (−1.00 vs −2.00), LydianDominant
(−0.30 vs −1.00), MixolydianB6 (−1.00 vs −1.50), AeolianB5 (−2.00 vs −2.50), LocrianSharp6 (−2.00
vs −2.50), IonianSharp5 (−1.50 vs −2.00), DorianSharp4 (−1.50 vs −2.00), LydianSharp2 (−2.00 vs
−2.50). So the live product's mode priors are their **own distinct set** — no named preset
reproduces them. `--preset Default` mirrors the **app** values (per instruction: "match the app"),
with `ChordAnalyzerPreferences` left at struct defaults (`preferMinorOverMajorAdd6=false` — the app
never mutates a chord-pref field). The 21 values are hardcoded in `batch_analyze.cpp applyPreset()`
with a KEEP-IN-SYNC comment pointing at `composingconfiguration.cpp` (the codebase already
duplicates preset values this way; "Default" is kept out of the shared `modePriorPresets()` so the
app's preset registry / button list and `currentModePriorPreset()` are untouched — the QML button
list is hardcoded and does not enumerate the registry).

### 7.2 — The measurement [probe]

`tools/corpus/default` regenerated clean (353/353, manifest-stamped `preset=Default`, git
`1a08e96d8a`). Third informational column, side by side:

| metric | Baroque (gate) | Jazz (gate) | **Default (user config — NO gate)** |
|---|---|---|---|
| three-way genuine errors (total) | 37 | 42 | **44** |
| `bassIsRoot=true` (BIR=true) | 24 | 35 | **30** |
| `bassIsRoot=false` (BIR=false) | 13 | 7 | **14** |
| `characterise_bir_false` BIR=false | 13 | 7 | **14** (= the BIR=false half, as expected) |
| aligned regions | 11267 | 10910 | 11254 |
| chord-identity agree | — | — | 90.7% |
| corpus git stamp | fb8b980948 | fb8b980948 | 1a08e96d8a |

**STATUS-ready (Cowork writes STATUS):**
> User-default config (no gate, informational): three-way 30/14, characterise BIR=false 14,
> `tools/corpus/default` (git 1a08e96d8a). Identity set = Baroque-13 ∪ {bwv187.7}.

**Identity-set overlaps — the load-bearing read:**

- **Default-14 = Baroque-13 in FULL + `bwv187.7`.** Every one of the 13 canonical Baroque gate
  cases persists under the configuration users actually run; the only extra is `bwv187.7` (m14.b2,
  Gm7/F — notably one of the 3 D-GAP probe cases, surfaced here by the app's mode-prior delta, not
  by chordPrefs). So the **Baroque-13 gate is a 13-of-13 subset of the user-experienced errors**
  (+1) — the gate is a near-exact, slightly-conservative proxy for what users hit.
- **5 of the canonical Jazz-7 persist** under Default: `{bwv245.17, bwv245.40, bwv422, bwv432,
  bwv45.7}`. The two Jazz-only cases `{bwv244.15, bwv74.8}` do **not** appear under the user config
  (they are artifacts of Jazz's aggressive chord prefs / mode priors).
- Net: the live-product configuration is **closest to Baroque** (a 13-of-13 superset, +1), **not**
  to batch "Standard" — confirming D-PASS0 Half A's "not even Standard" while showing the gate the
  product is best-proxied by is the Baroque one.

### 7.3 — Verification [probe]

| check | result |
|---|---|
| Build | clean, exit 0 (all 4 targets) |
| `batch_analyze --help` | lists `…|Contemporary|Default` |
| composing_tests | 501/501 |
| notation_tests | 52/52 |
| pipeline_snapshot_tests | 11/11 (1 report-gen SKIP, as always) |
| test_metric_scripts.py | 67/67 (+2: `TestPresetChoices`) |
| test_batch_analyze_regressions.py | passed |
| **Baroque gate (existing dir, re-validated)** | **13** — held (git fb8b980948) |
| **Jazz gate (existing dir, re-validated)** | **7** — held (git fb8b980948) |

Existing gates **untouched by construction** — V4 adds only a new `else if (presetName ==
"Default")` chord-prefs branch and an `applyPreset` early-return; no Standard/Jazz/Modal/Baroque/
Contemporary code path is altered, so their batch output is byte-identical (re-validation from the
committed dirs confirms 13/7). No stop-condition tripped.

### 7.4 — Files (V4)

- `tools/batch_analyze.cpp` — `applyPreset` "Default" branch (21 app values + sync comment);
  chordPrefs "Default" branch (struct defaults, `preferMinorOverMajorAdd6` stays false); error
  message + `--help`/header preset lists extended.
- `tools/run_bach_preset.py` — `PRESET_CHOICES` module constant (adds "Default"); argparse uses it.
- `tools/tests/test_metric_scripts.py` — `TestPresetChoices` (pins the canonical-5 + "Default").
- `ARCHITECTURE.md` — D-PASS0 Half-A measured-numbers sentence.

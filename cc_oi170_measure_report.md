# OI-170 — the whole-layer tonic-use map of Layer 4: enumeration, classification, magnitude

**Dispatch:** `cc_instruction_oi170_measure.md` (Cowork, 2026-07-13). **Type:** MEASUREMENT build —
default-OFF instrumentation + a default-OFF signature-mask variant. **No fix is promoted.** The
default production path is unchanged and regenerates the committed corpus byte-identically on all
three presets.

**Every figure below is cited from the generated artifact `cc_oi170_measurements.txt`** (#17f — no
hand-transcribed measurement numbers). Instruments: `tools/cc_oi170_measure_artifact.sh` (the
committed assembler that regenerates the artifact end-to-end — §10), driving
`tools/cc_oi168_probe_report.py` (extended for the OI-170 sites; one probe reporter, not a second
one — #6) + `tools/a8_rebaseline_measure.py` + `tools/robust_stop_diff.py`.

> **★ PROVENANCE — every arm was RE-RUN before this report was folded (#16/#19).** The artifact's
> first generation was produced by a binary built at 12:05, *before* the last source edit to
> `chordanalyzer.cpp` at 12:22 — so its stamp to the committed source was **broken**, and no figure
> it carried was established. The tree was rebuilt from the exact source being committed (the
> incremental build recompiled exactly one translation unit, confirming that edit was the only one
> outstanding) and **all nine corpus arms, the three suites, and the hard stop were re-run**. Every
> figure reproduced the earlier generation **exactly** — which *establishes*, rather than assumes,
> that the post-build edit was non-behavioral. The figures below are the re-run ones.

---

## 0. The headline

1. **L4 CANNOT be made fully tonic-independent.** The enumeration found **three** class-(a)
   collection-membership-through-the-tonic sites (exactly the three OI-170 named) — but also
   **seven** class-(b) sites where the tonic is genuinely needed, **three of them live and
   decision-bearing**: Gate G-E (**58 winner swaps on Baroque**), `applyTonicPriorToSparseChord`
   (**172 / 183 / 172** committed-quality overwrites on Baroque/Jazz/Default), and the published
   `degree` itself. The collection/tonic split does not become true by fixing the three; it becomes
   true only for the *collection question*. **And the scope check found a THIRD live chord-deciding
   genuine-tonic site — the first one OUTSIDE L4**: the segmenter's head-gap tonic prior
   (`harmonicsegmenter.cpp:849-852`, §2; the two inside L4 are Gate G-E and
   `applyTonicPriorToSparseChord`). So "make L4 tonic-independent" would not even make the
   *committed chord* tonic-independent.
2. **The three class-(a) sites are FIXABLE, and the fix is metric-neutral.** Under the variant:
   **Baroque and Default are byte-identical (352/352 each)**; **Jazz: 9 files change and the ONLY
   JSON key that changes anywhere in the corpus is `diatonicToKey`** — **22 flags flip, every one
   `false → true`, and NOT ONE committed chord moves** (0 flips on all three presets). The
   robust-stop hard gate is **exactly unmoved**: run-diff **(+0 / −0)** on every preset, class-(b)
   root-disagree duration **δ = 0**, class-(a) **δ = 0**, every key column identical to the digit,
   `robust_stop_diff.py` **OVERALL PASS**.
3. **The `diatonicToKey` "single-sourcing" is NOT byte-identical and NOT a pure read-the-published-
   fact** — because the tree holds **four mutually inequivalent definitions** of the flag and
   **two** of `degree`, and because most re-derivations answer for a **different key** than the one
   L4 committed under. The unification available is one shared *predicate*, not one shared *value*.
4. **A key-layer finding, declared not fixed:** **22 of the 23** Jazz regions whose local key is
   `Altered` contain **no pitch class outside the notated signature's own collection**. The key
   layer emits an `Altered` local key on material that is entirely diatonic to its signature.

---

## 1. Task 0 — the register commit

`git status --porcelain` showed **no waiting Cowork register/handoff edits**: the only modified
tracked file was `cowork_joint_key_chord_design.md` (left unstaged per the dispatch). Nothing to
commit. The untracked scratch outputs already present (`idiom_discovery/*.txt`, `scratch_artifacts/`,
`tools/robust_stop/*_variant_*_root_fail_cells.txt`, a stray file named `key`) were left untouched —
this session added nothing to them and committed none of them.

---

## 2. Task 1 — the enumeration, and its completeness basis

**The basis (mechanical, reproducible — artifact §"SWEEP 1..5").** Every occurrence of every
tonic-derived construction **in the dispatch's L4 scope** was listed by grep, not by recall (and the
scope itself is then checked against the whole tree, below — the two are different claims and the
difference is where OI-175 was hiding):

```
keyTonicPc | keyModeTonicOffset | ionianTonicPcFromFifths | keyModeScaleIntervals | diatonicDegreeForRootPc
```

over `analysis/chord/`, `analysis/function/`, `analysis/region/`, `analysis/section/` and the two
notation bridges — **118 hits**, every one read. Two further sweeps enumerate every **write** and
every **read** of `diatonicToKey` in the tree, and a fifth finds every copy of the 21→7
diatonic-parent table. **The claim this supports is: these are every occurrence of the pattern in
these files** — not "the ones previously found".

**The scope is itself checked, not assumed** (artifact §SWEEP 1b/1c). The same pattern run over the
**whole** composing and notation modules returns **140** hits; the **22**-hit remainder outside the L4
scope is enumerated by file, reconciled arithmetically (`140 − 118 = 22`, and the per-file remainder
sums to 22 — the artifact asserts this and prints a **STOP** if it ever fails to reconcile), and each
hit read. **Twenty are legitimately elsewhere**: `analysis/key/` (`keymodeanalyzer.{cpp,h}` 8 +
`keyresolver.cpp` 3 — the key layer, the *legitimate producer* of a tonic), `notationtuningbridge.cpp`
(4 — tuning), `notationcomposingbridgehelpers.{cpp,h}` (4 — a **pure forwarding wrapper**:
`diatonicDegreeForRootPc` simply `return`s `cra::diatonicDegreeForRootPc(...)`, so it is a re-export of
the one shared helper, not a second definition), one comment in `harmonicvocabulary.h`. **Two are
not** — and the enumeration as scoped does not name them:

> **★ `harmonicsegmenter.cpp:849-852` — a live, chord-DECIDING, genuine-tonic site OUTSIDE Layer 4.**
> Inside `greedyExpandSegmentation` (called on the live region path from `regionanalyzer.cpp`), the
> Iter-74 Fix-B **head-gap tonic prior** builds the mode tonic the same way every δ-bug site does —
> `ionianTonicPcFromFifths(globalKeyFifths) + keyModeTonicOffset(globalKeyMode)` — and, when the
> head-gap winner is not tonic-rooted and its margin is thin (`< 0.4`), **overwrites the synthesized
> head region's `rootPitchClass`, `bassPitchClass` and `quality`** with a tonic-rooted candidate, or
> failing that with the tonic and the modal triad quality outright. It asks *"is this root **the
> tonic**?"* — a genuine tonic question the signature mask cannot answer: **class (b)**.
>
> It is **not a δ-bug** and is **not in this dispatch's L4 file scope** (the segmenter is Layer 2), so
> nothing here is built or changed for it. But it is a **third live site where a genuine tonic decides
> a committed chord identity** — and the **first outside Layer 4** (the two inside are Gate G-E and
> `applyTonicPriorToSparseChord`). It is on **no** register row and surfaced in neither of the two rows
> that scoped this work. **Its fire count is NOT measured** — the probe instruments L4 only, and
> extending it to Layer 2 was outside this dispatch; the site's liveness is established structurally
> (it is on the call path), its magnitude is not. Declared to Cowork as **OI-175**.

**And the scope check's FIRST run was itself defective — recorded, not quietly fixed (DT-26 on
itself).** Its exclusion regex named the two in-scope bridges as bare substrings
(`notationcomposingbridge`), which also matches **`notationcomposingbridgehelpers.{cpp,h}`** — so
**4 hits were silently dropped from the remainder listing**, and the listing summed to 18 while
`140 − 118` demanded 22. Nothing but the arithmetic caught it: the listing looked complete and was
not. The exclusion is now **anchored** on the two exact paths, the remainder listing is **derived from
that same exclusion** rather than a hand-kept file list (so a new out-of-scope file cannot be counted
yet un-listed), and the artifact now **asserts the reconciliation and prints a STOP if it fails**. The
4 dropped hits turned out to be benign (the forwarding wrapper above) — **which is exactly why this is
worth recording: the check that silently drops hits gives the same clean-looking output whether what it
dropped was benign or was a second OI-175.**

**What the sweep found that the OI-170 row did not name** (the gap is itself diagnostic, #3 — my
pre-sweep expectation, recorded before the sweep, was five sites):

- **`applyTonicPriorToSparseChord`** (`sparsechordrefinement.cpp:182-215`), called on the region
  analyzer's **commit path** at `regionanalyzer.cpp:1017` — it overwrites the **committed quality**
  of a thin (Power/Sus2/Sus4) chord with the diatonic triad quality of its **degree**. Live: it
  fires **172 / 183 / 172** times (Baroque/Jazz/Default). This is a tonic-dependent site that
  changes the emitted chord, and no register row named it.
- **`degree` has two inequivalent definitions**: `analyzeChord`/`buildChordResult` numbers degrees
  by the mode's **diatonic PARENT** scale; the shared helper `diatonicDegreeForRootPc`
  (`sparsechordrefinement.cpp:109`) numbers them by the **mode's OWN** scale. They differ for **all
  14 non-diatonic modes**, not merely the two δ≠0 ones (e.g. under HarmonicMinor, a root on the
  raised 7th is `degree = -1` to the first and `degree = 6` to the second).
- **`diatonicToKey` has four definitions** (§4).
- **The 21→7 diatonic-parent table exists three times**: `DIATONIC_PARENT_INDEX`
  (`chordanalyzer.cpp:1397`), `csfTonicizationParent` (`chordsymbolformatter.cpp:799`),
  `CHR_DIATONIC_PARENT` (`chordsymbolformatter.cpp:840`) — byte-identical copies (#6).

---

## 3. Task 2 — the classification

### Class (a) — collection-membership asked through the tonic (the δ-bug; the signature mask replaces them exactly)

| site | code | decision-bearing? | measured (artifact §counters) |
|---|---|---|---|
| **a1 — `buildChordResult`'s diatonic check** → the published `r.function.diatonicToKey` | `chordanalyzer.cpp` "Diatonic check: every sounding pc must be in the scale" | publishes a fact; moves no winner | **399,945 / 397,849 / 399,900** evaluations; the two verdicts differ **0 / 237 / 0** times (Baroque/Jazz/Default) |
| **a2 — Gate I's `invRootIsDiatonic`** | `postscoringgates.cpp`, Gate I block | **YES — swaps the committed winner** | reached **4942 / 4179 / 4930** times; verdicts differ **0 / 1 / 0**; the **swap decision** differs **0 / 0 / 0** |
| **a3 — Gate L's `invRootIsDiatonic`** | `postscoringgates.cpp`, Gate L block | **YES — swaps the committed winner** | reached **29 / 108 / 30** times; verdicts differ **0 / 0 / 0** |

All three ask *"is this pitch class in the key?"* and answer it by membership in
`{ (keyTonicPc + scale[i]) mod 12 }`. That set equals the key signature's own collection **iff**
δ = `keyModeTonicOffset(M) − keyModeTonicOffset(parent(M))` is 0 — true for 19 of the 21
`KeySigMode` values, **false for `Altered` and `AlteredDomBB7`** (the OI-168 derivation). The
signature-mask primitive the repo already has —
`pcInMask(diatonicMaskFromFifths(fifths), pc)`, `analysisutils.h:77-94`, *"depends ONLY on the
notated signature, never a resolved mode"* — answers it with **no tonic and no mode scale**.

**The δ=0 derivation is now verified at runtime, not on paper:** with the variant on, Baroque and
Default regenerate **byte-identical on 352/352 files each**, and every `…Differs` counter is
**0** on both — the two predicates are the same predicate wherever δ=0.

### Class (b) — genuine tonic-use (the primitive CANNOT replace these)

| site | code | decision-bearing? | measured |
|---|---|---|---|
| **b1 — the DEGREE assignment** | `chordanalyzer.cpp`, "Degree assignment" loop | publishes `degree`; feeds the RN formatter and the sparse refinement | runs on every `buildChordResult` (≈400k/preset) |
| **b2 — Gate G-E's ii / iii / vii degree test** | `postscoringgates.cpp:380-385` | **YES — swaps the winner to a HalfDiminished root** | **fires 58 times on Baroque**; 0 on Jazz/Default (preset-gated `preferMinorOverMajorAdd6`) |
| **b3 — `applyTonicPriorToSparseChord`** (degree → diatonic triad quality) | `sparsechordrefinement.cpp:182-215`, on the commit path at `regionanalyzer.cpp:1017` | **YES — overwrites the committed QUALITY** | entered **1802 / 2197 / 1813**; **applied 172 / 183 / 172** |
| **b4 — `refineSparseChordQualityFromKeyContext`** (degree + the Aeolian lone-tonic guard) | `sparsechordrefinement.cpp:122-180`, three commit-path call sites | in principle yes | **0 entries, 0 guard fires** on all three presets — the OI-167 measurement, re-confirmed here |
| **b5 — `forceChordTrackQualityFromKeyContext`** (degree → quality) | `sparsechordrefinement.cpp:217-232` | chord-track/notation only | not on the corpus path |
| **b6 — the Roman-numeral / Nashville labels** | `chordsymbolformatter.cpp:809/837/887-889/930-933/1015` | emits `romanNumeral` | a Roman numeral **is** tonic-relative by definition |
| **b7 — the key-context publication** `r.function.{keyTonicPc,keyMode}` | `chordanalyzer.cpp` | publication | — |

A **degree** is tonic-relative *by definition* — no collection can answer "which scale degree is
this?". So b1/b2/b3/b6 are real dependences, not defects of expression. **b2 and b3 are the
load-bearing ones: they let a tonic decide the committed chord**, 58 + 172 times on Baroque alone.

**Nothing in the L4 scope was left unclassified** — and the scope itself is checked, not assumed
(§2): the one chord-deciding site outside it, the segmenter's head-gap tonic prior, is class-(b)
and declared (OI-175), not swept under. The plumbing sites (`snapshot.{scale,keyTonicPc,keyMode}`,
the `gateCtx` fill in `harmonicfunctionlayer.cpp:560-564`, the `BuildChordResultContext`
reconstruction in `postscoringgates.cpp:63-68`) carry the tonic but decide nothing; they are listed
in the artifact and are not a third class.

### The answer to the dispatch's question

> *The (a)/(b) split is the answer to "can L4 be made fully tonic-independent": all-(a) ⇒ yes; any
> (b) ⇒ a named design constraint remains.*

**Any-(b). L4 CANNOT be made fully tonic-independent.** The named constraint: **L4 today both
publishes a tonic-relative reading (degree, Roman numeral) and lets that reading DECIDE the chord
identity** (Gate G-E, `applyTonicPriorToSparseChord`). The collection question can be made
tonic-free; the degree question cannot, and the degree question is currently wired into the
identity decision.

---

## 4. `diatonicToKey` — four definitions, one reader

**Every write of the flag in the tree** (artifact §SWEEP 3), and what each actually computes:

| definition | sites | predicate |
|---|---|---|
| **D1 — the producer** | `chordanalyzer.cpp` (`buildChordResult`) | degree (**parent** scale) ≥ 0 **AND** every pc with `pcWeight > 0.2` in the **parent-scale set** |
| **D2 — the section / bridge re-derivation** | `sectionanalyzer.cpp:140-157`, `:275-293`; `notationcomposingbridge.cpp:97-115` | degree (**mode's OWN** scale) ≥ 0 **AND** every tone in the **mode's own scale** |
| **D3 — the degree-only shortcut** | `functionromannumeral.cpp:36`, `functionrelationallabel.cpp:49`, `sectioncadencedetection.cpp:241`, `notationcomposingbridge.cpp:1144` | `degree >= 0` — **no membership loop at all** |
| **(the correct question)** | — | every sounding pc in `diatonicMaskFromFifths(keyFifths)` |

D1 ≠ D2 (different scale, different tone set, different threshold) and D3 is strictly weaker than
both. **So "the five consumers re-derive the published fact" is not what the code does — they
compute three different facts.** Worse for the single-sourcing plan: **most of them re-derive for a
DIFFERENT key** — `sectioncadencedetection` for the *incoming* key of a pivot, `notationcomposingbridge:1144`
explicitly only when `romanKeyFifths != perRegionFifths`, `functionromannumeral` /
`functionrelationallabel` for whatever key their caller hands them. For those, "read the published
fact" is not merely non-identical, it is **not well-defined**.

**Corpus consequence: none.** None of the re-derivations runs on the default `batch_analyze` path
(`analyzeSection` is behind `--section-level`; the bridges are UI-side), so the `.ours.json`
`diatonicToKey` is always D1's. This is why the variant's effect on the corpus is exactly site a1's.

**The published fact has ONE reader in the whole tree** (artifact §SWEEP 4):
`notationimplodebridge.cpp:1205` — the non-diatonic (borrowed-chord) UI marker. And
`BaseRomanNumeral::diatonicToKey` (`functionromannumeral.h:84`) is written and **read by nobody** —
under the fact-publication corollary that is either **declared dormancy** (name the future consumer)
or **waste**.

---

## 5. Task 3 — the magnitude of unifying the class-(a) sites

**The variant** (`MU_KEY_COLLECTION_SIGMASK_VARIANT=1`, default-OFF) routes all three class-(a)
sites through `pcInMask(diatonicMaskFromFifths(fifths), pc)`. The `keySignatureFifths` it needs is
carried to the two consumers that lacked it (`ScoringSnapshot::keySigFifths`,
`BuildChordResultContext::keySignatureFifths`); `PostScoringGateContext::keySigFifths` already existed.

### 5.1 Committed-chord flips: **ZERO, on every preset**

| | Baroque | Jazz | Default |
|---|---|---|---|
| regions under an Altered-family local key | 0 | **23** | 0 |
| **committed-chord flips inside them** | **0** | **0** | **0** |
| committed-chord flips anywhere else (structural: must be 0) | **0** | **0** | **0** |
| segmentation differences | 0 | 0 | 0 |

**Per-site attribution** (the counters, not inference): Gate I's membership verdict differed on
exactly **one** candidate across the whole Jazz corpus, and **`gateISwapDiffers = 0`** — another
conjunct of the gate blocked that swap either way. Gate L's verdict never differed. **So neither
decision-bearing gate changes a single committed chord on this corpus.**

### 5.2 The published flag: 22 corrections, all in the right direction

Whole-file byte-identity of the variant corpus vs the committed corpus: **Baroque 352/352,
Default 352/352, Jazz 343/352 — 9 files differ**, and a line-level diff of all nine shows **the only
JSON key that changes anywhere is `diatonicToKey`** (44 changed lines = 22 flips).

All 22 flips are **`false → true`**, all inside `Altered` regions, **0 outside** (the structural
prediction). The regions and their committed chords (artifact §flips):

`bwv135.6@21600 A`, `@23520 G` (C♯alt) · `bwv145.5@11520 E/G♯, @12480 A, @12960 B/E♭, @13920 E,
@14400 A, @15360 B` (D♯alt) · `bwv187.7@6240 Gm7/F, @7200 C/E` (F♯alt) · `bwv245.37@30240 B♭m,
@30720 F` (Aalt) · `bwv314@11040 E, @11520 A/G♯` (D♯alt) · `bwv353@7680 D, @10080 Gm7/F,
@10560 C/E` (F♯alt) · `bwv404@10560 Am, @11040 E` (G♯alt) · `bwv60.5@3360 G♯` (B♯alt) ·
`bwv64.8@21600 Em, @22560 B` (G♯alt).

**The toward-correct check.** Every one of these is a plain diatonic triad or seventh of the local
key's own signature collection (e.g. `C♯alt` has the C-major signature; `A` and `G` are diatonic to
C major). The current code scores them against the C-major collection **transposed up a semitone**
(D♭ major — 2 of 7 pitch classes shared) and therefore publishes `diatonicToKey = false` on chords
that are **entirely inside the key's collection**. The variant publishes `true`. **The variant's
reading is the correct one on all 22.**

### 5.3 The hard stop: exactly unmoved

`a8_rebaseline_measure.py` on the variant corpus + `robust_stop_diff.py` against the committed
reference:

| preset | runs (ref → cand) | class-(b) root-disagree duration | class-(a) | key-agree home / local |
|---|---|---|---|---|
| Baroque | 6506 → 6506 **(+0 / −0)** | 2 714 000 → 2 714 000 **δ=0 PASS** | δ=0 | 71.4182 / 65.9900 — unchanged |
| Jazz | 6688 → 6688 **(+0 / −0)** | 2 783 680 → 2 783 680 **δ=0 PASS** | δ=0 | 67.8274 / 62.9805 — unchanged |
| Default | 6522 → 6522 **(+0 / −0)** | 2 718 080 → 2 718 080 **δ=0 PASS** | δ=0 | 70.6514 / 65.7093 — unchanged |

**`robust_stop_diff.py`: OVERALL PASS**, with zero added and zero removed runs on every preset. The
fix moves **no** measured quantity — root, RN and both key columns are identical to the digit. It is
a **metric-neutral correctness fix**.

### 5.4 The single-sourcing arm

Not implementable as specified, and the reason is a finding, not an obstacle: see §4. The variant
therefore single-sources the **predicate** (all three class-(a) sites now call the same
signature-mask pair) and leaves the consumers' re-derivations in place; they are unreachable from
the corpus path, so this cannot mask a corpus effect.

---

## 6. Predicted vs actual (#17b — the predictions were written before the build)

*Provenance of the pre-registration, verified rather than asserted: the prediction file
(`oi170_predictions.md`, written after the Task-1 **code read** and before any compile or run) is
timestamped **11:59:24**; the build ran at **12:05** and the first measurement at **12:29** — so the
predictions demonstrably predate both, and the table below reproduces them without alteration. The
file lives in a session scratchpad and is not durable; this table is therefore the record (which is
why it reproduces the ranges, confidences and bases, not merely the verdicts).*

| prediction | predicted | actual | verdict |
|---|---|---|---|
| flips on Baroque / Default | **exactly 0 / 0**, byte-identical (HIGH, structural) | **0 / 0**, 352/352 byte-identical | **met — the load-bearing structural claim** |
| committed-chord flips on Jazz, total | 0–2, point estimate **0** (LOW) | **0** | met |
| flips attributable to Gate I / Gate L | 0–1 each | **0 / 0** (Gate I: 1 verdict differed, 0 swaps) | met |
| flips OUTSIDE the Altered regions | **exactly 0** (HIGH, structural) | **0** | **met** |
| `diatonicToKey` flag flips on Jazz | 5–18, point estimate 10; direction mostly false→true | **22** — above the range; **all** false→true | **direction met, magnitude MISSED (22 > 18)** |
| flag flips outside the Altered regions | exactly 0 | **0** | met |
| the `diatonicToKey` single-sourcing is byte-identical | **NO** — predicted not even well-defined | confirmed: four definitions, different keys | met |
| number of tonic-use sites | pre-sweep expectation **5** | **3 class-(a) + 7 class-(b)** | **MISSED — the sweep found more** |
| any class-(b) at all? | **YES** | yes — and three are live and decision-bearing | met |

**The two misses, diagnosed (#3).**

1. **The flag-flip magnitude (22 vs ≤18).** I under-predicted because I assumed an `Altered` local
   key would be emitted over *chromatic* material. It is not: **22 of the 23 Altered regions contain
   no pitch class outside their signature's collection at all**. Nearly every Altered region is
   fully diatonic — so nearly every one flips. The gap is not noise; it is the fingerprint of the
   key-layer finding in §7.
2. **The site count (5 vs 10, and then 11).** The two register rows (OI-167, OI-170) between them
   named five sites; a mechanical sweep found `applyTonicPriorToSparseChord` (live, 172+ commit-path
   quality overwrites), a second definition of `degree`, four definitions of `diatonicToKey`, and
   three copies of the parent table. **This is the third time site-by-site auditing has missed sites
   — and the first time the sweep was mechanical. The lesson is the method, not the count.**
   *And the lesson repeated inside this very report:* the first pass of this enumeration swept only
   the dispatch's named L4 files and would have shipped the claim "nothing was left unclassified"
   while a live, chord-deciding tonic site sat two directories away. It was caught only by running
   the same pattern **tree-wide** and reading the 22-hit remainder (§2). **A scoped sweep proves
   completeness of the scope, never of the question** — the scope check is the part that has to be
   mechanical too.

---

## 7. Declared to Cowork, NOT fixed (inference problems — #8)

1. **The key layer emits `Altered` on fully-diatonic material.** 22 of 23 Jazz `Altered` regions have
   every sounding pitch class inside the notated signature's own collection. An "altered" local key
   over material with no altered tone is a key-layer inference problem. Chord-side, it is now
   harmless (the fix makes the chord layer read the signature's collection whatever mode the key
   layer emits) — but it is evidence the emitted mode is wrong, and it is **not** this dispatch's to
   fix.
2. **`applyTonicPriorToSparseChord` decides the committed QUALITY from a degree** — 172/183/172
   fires, on the commit path, unnamed by any register row until now.
3. **Gate G-E decides the committed ROOT from a degree** — 58 fires on Baroque.
3b. **The SEGMENTER decides a committed ROOT and QUALITY from the tonic — outside L4, on no register
   row** (`harmonicsegmenter.cpp:849-852`, the Iter-74 Fix-B head-gap tonic prior in
   `greedyExpandSegmentation`; §2). **Fire count unmeasured** — instrumenting Layer 2 was outside
   this dispatch. Two questions for the design pass, neither CC's to answer: (i) if the tonic
   decides chord identity in the *segmenter* too, is "tonic-independence" a property of L4 at all, or
   of the whole chord-committing path? (ii) it consumes the **global** key mode, so under OI-174's
   finding (an `Altered` mode emitted on diatonic material) it would prefer a tonic a semitone off
   the real one — the two findings compose.
4. **Two definitions of `degree`; four of `diatonicToKey`; three copies of the parent table** (#6).
5. **`BaseRomanNumeral::diatonicToKey` has no reader** — dormancy or waste.
6. **The `Altered`/`AlteredDomBB7` parent-scale degree is structurally wrong**, not merely
   collection-wrong: `DIATONIC_PARENT_INDEX` numbers their degrees from a scale whose tonic is not
   even a member. The **mode's own scale** (what `diatonicDegreeForRootPc` already uses) is the
   correct basis for a degree; the parent table is the correct basis for **nothing**.

---

## 8. The recommended fix design

**Split the two questions L4 currently conflates into one construction.**

| question | the right primitive | why |
|---|---|---|
| *"is this pitch class **in the key**?"* (a1, a2, a3) | `pcInMask(diatonicMaskFromFifths(keyFifths), pc)` — the existing `analysisutils.h` pair, **no new name** | takes no tonic and no mode scale, so the property is **structural** and cannot lapse when a mode is added to the table (which is exactly how OI-168 and OI-170 arose) |
| *"which scale **degree** is this?"* (b1, b2, b3, b6) | `diatonicDegreeForRootPc(pc, keyFifths, keyMode)` — the **mode's own** scale, the helper the rest of the tree already uses | a degree is tonic-relative by definition; the parent-scale numbering is wrong for all 14 non-diatonic modes |

Then: **retire `DIATONIC_PARENT_INDEX` and its two duplicate copies** — with the collection question
on the mask and the degree question on the mode's own scale, the parent table has no remaining
correct use.

**The fix path (sized, not guessed):**
- **Behaviorally: 0 committed-chord flips, all three presets.** No robust-stop re-baseline is needed
  — the run sets, the hard-stop duration and every column are byte-identical (§5.3, proven).
- **Corpus: 9 Jazz `.ours.json` files change** (22 `diatonicToKey` flags, `false → true`, all
  toward-correct). `tools/corpus/jazz` must be regenerated and the `tools/robust_stop/manifest.json`
  corpus `git_hash` re-stamped via `tools/robust_stop_restamp.py` (which enforces the O-12 snapshot
  mechanically) — the *figures* it re-stamps are unchanged.
- **Goldens: none.** The pipeline-snapshot goldens carry **no `diatonicToKey` field and no
  Altered-family key** (verified, artifact §goldens); Default is byte-identical regardless.
- **Ratification:** it is still a behavior change on a published fact (#14) — one revertible,
  provenance-stamped commit, user-ratified.
- **The degree-basis correction (parent scale → mode's own scale) is a SEPARATE change** with its own
  measurement: it moves `degree`, hence Roman numerals, hence possibly Gate G-E and
  `applyTonicPriorToSparseChord` — i.e. committed chords. **It is not folded into the collection fix.**

**And the design question that outranks both** (for the design pass, not for CC): b2 and b3 let a
**degree** — a tonic-relative reading — decide the **chord identity** inside Layer 4. If the layer
assignment is to hold, that is where the tonic-independence question actually bites; the collection
fix does not touch it.

---

## 9. The OFF path is inert — proven, not argued

| arm (352 scores × 3 presets) | Baroque | Jazz | Default |
|---|---|---|---|
| instrumented binary, **both flags unset** (the required OFF-path proof) | **352/352 identical** | **352/352** | **352/352** |
| instrumented binary, **counters ON**, variant off | **352/352 identical** | **352/352** | **352/352** |

`composing_tests` **1103/1103**, `notation_tests` **53/53**, `pipeline_snapshot_tests` **11/11** — all
green, **no golden refreshed**, `tools/robust_stop` and `tools/corpus` **untouched** (every arm wrote
to a scratch directory). Build warnings: only the two **pre-existing** OI-169 ones
(`structuralPenalties`' `extThreshold`, `formatNashvilleNumber`'s `keySignatureFifths`) — no new
warning introduced.

---

## 10. Reproduce

```
# the three arms (each writes to a scratch dir; the committed corpus is never touched)
python tools/run_bach_preset.py --preset Jazz --output-dir <off>
MU_KEY_COLLECTION_PROBE=1 python tools/run_bach_preset.py --preset Jazz --output-dir <cnt>
MU_KEY_COLLECTION_PROBE=1 MU_KEY_COLLECTION_SIGMASK_VARIANT=1 \
    python tools/run_bach_preset.py --preset Jazz --output-dir <var>

python tools/cc_oi168_probe_report.py byteid   <off> tools/corpus/jazz     # must be 352/352
python tools/cc_oi168_probe_report.py counters <cnt>
python tools/cc_oi168_probe_report.py flips    tools/corpus/jazz <var>     # chord flips + flag flips

# the hard stop on the variant corpus
python tools/a8_rebaseline_measure.py --out-dir <a8> --corpus-root <var-root>
python tools/robust_stop_diff.py --candidate <a8>                          # OVERALL PASS
```

**Rebuild before measuring.** Both flags are read once at static init, so an arm measures whatever
binary is on disk — and a corpus run does **not** rebuild. This report's first draft was measured
against a binary one source-edit stale (see the provenance note at the head); the arms only became
established once re-run on a binary built from the committed source. **Stamp the arm to the build,
not to the working tree.**

**The enumeration sweeps and the artifact assembly are one committed instrument**,
`tools/cc_oi170_measure_artifact.sh` (§SWEEP 1–5 + the three arms + the hard stop + the golden check,
assembled into `cc_oi170_measurements.txt`) — not a scratch script, so the artifact is regenerable by
anyone (#16):

```
bash tools/cc_oi170_measure_artifact.sh <arms-root> <suite-log-dir> [<out>]
```

**Established before use (#19):** it reproduces this artifact **exactly** — regenerating over the same
arms changed **no measured figure**, only the header prose naming the new generator.

**The scope check (SWEEP 1b/1c) is load-bearing and the tool says so.** It is what caught OI-175, and
a future sweep that drops it re-opens exactly the hole this dispatch was written to close. It now
carries its own guard: the exclusion is **anchored** on exact paths, the remainder listing is
**derived from that same exclusion**, and the run **asserts `tree-wide − scoped == Σ remainder` and
prints a STOP on mismatch** — the three things whose absence let this very check silently drop 4 hits
on its first run (§2).

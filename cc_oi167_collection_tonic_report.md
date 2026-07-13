# OI-167 — Does the collection/tonic split hold for the engaged L4?

**Session type:** READ-ONLY premise verification + disposition proposal (Cowork dispatch, 2026-07-13).
**Nothing was built, no `src/` file was edited, no golden refreshed, no retirement applied, no existing
register row re-scoped.** Every disposition below is a **PROPOSAL** for the design pass and the user.

**Headline.** For the engaged `ChordSliceDecoder`, **both** sites OI-167 names are **unreachable** (FACT, at
the code) — Gate G-E and the Aeolian lone-tonic guard are legacy-path-only, and the guard additionally has
**zero fire sites** on all three preset corpora. But the split does **not** come out clean: a **THIRD
tonic-dependent site, inside the engaged decoder, at the exact place OI-167 declares safe** — the two
key-consuming scoring terms of `analyzeChord` — is collection-invariant for only **19 of the 21 modes**
`analyzeChord` accepts. For `Altered` and `AlteredDomBB7` the membership set it builds is the signature's
collection **transposed up a semitone**. `Altered` is **live: 24 emitted regions on the Jazz preset.**

**⛔ STOP (#13).** OI-167's load-bearing claim — *"pure collection-membership tests (the constructed pc-set is
provably identical for all 7 diatonic modes of one signature)"* — is **true as written and insufficient as
used**. It proves the property over the 7 diatonic modes; the function accepts 21, and the key layer emits
non-diatonic ones. This is a **Class-A unverified causal premise (#18, DT-1)**: a checkable claim about our
own system, carrying the whole L3/L4 separation, checked on a third of its domain. Filed **OI-168**.

The split is **RESTORABLE** — the defect and the premise share one fix (§4.3) — but it does not hold
unconditionally today, and the design pass must not build on it until the fix is ratified and measured.

---

## 0. Premise Gate — predictions recorded BEFORE checking (#17b)

Written to the scratchpad before any code was opened; reproduced verbatim.

| # | Prediction (recorded first) | Finding | Diagnosis (#3) |
|---|---|---|---|
| P1 | Gate G-E **legacy-only**, not engaged-reachable (conf. ~0.85). Residual risk named: *"the gates may not ALL be gated on `gateCtxOut`"* | **CONFIRMED.** Legacy-only. The residual risk did not materialize — the gates are not gated on `gateCtxOut` at all; they are a *separate function the decoder never calls* (§1.2), which is stronger than predicted | Prediction held; the mechanism was firmer than assumed |
| P2 | Aeolian guard a **legacy artifact**, **live** on the production path (conf. ~0.6/0.6) | **PARTLY WRONG.** Artifact: supported (§2.3). "Live": **wrong** — it is live *in the legacy path* but has **0 fire sites** on all three corpora (§2.4) | I assumed a coded guard on a live path fires. It does not. Measuring beat the assumption |
| P3 | Split **holds conditionally** on the two named sites; break "held open" but not predicted | **WRONG in substance.** The two named sites are *safe*; the split breaks at an **unnamed third site inside the decoder** | The gap is the finding. I inherited OI-167's site list instead of re-deriving the decoder's tonic reads from the code. Exactly the #19 failure ("trusted because unfalsified") |
| P4 | "At most these two tonic-dependent sites in L4, no third one" (conf. LOW ~0.4, flagged: *"the audit's scope was the decoder, not all of L4"*) | **WRONG — and it is the whole finding.** There IS a third, and it is *in* the decoder | I recorded low confidence for the right reason and then found the thing I doubted. The low confidence was earned, not lucky |

**The diagnostic gap (#3).** Three of four predictions were derived from the register row rather than from the
code. The one prediction I flagged as weak is the one that broke. Per #3 this is a **failure of #1/#19**, not a
curiosity: OI-167 was carrying a FACT label on a claim established over 7 of 21 cases.

---

## 1. Task 1 — Gate G-E (`postscoringgates.cpp:376-397`)

### 1.1 What it is (FACT — code)

```
if (prefs.preferMinorOverMajorAdd6 && originalWinnerQuality == Minor && originalWinnerHasAddedSixth) {
    const int gExpectedAltRoot = (originalWinnerRootPc + 9) % 12;
    const int gLeadingTonePc   = (gateCtx.keyTonicPc + 11) % 12;  // viiø7
    const int gSupertonicPc    = (gateCtx.keyTonicPc + 2) % 12;   // iiø7
    const int gMediantPc       = (gateCtx.keyTonicPc + 4) % 12;   // iiiø7 / mediant
    const bool geKeyContext = (gExpectedAltRoot == gLeadingTonePc || … gSupertonicPc || … gMediantPc);
```
(`postscoringgates.cpp:376-386`.) On fire it calls `promoteToWinner(… HalfDiminished …)` (`:391-396`) — it
**changes the committed chord**. Preset-gated on `preferMinorOverMajorAdd6` (Baroque ON, Jazz OFF).

**Tonic-dependence: GENUINE (FACT).** It is a **scale-degree** test — tonic+11 / +2 / +4. Unlike a
membership test, a degree test does not survive rotation: the same collection with a different tonic selects
different degrees. This cannot be reformulated collection-only without changing what it means.

### 1.2 Reachability in the engaged decoder: **UNREACHABLE (FACT)**

Three independent code facts, each sufficient:

1. **`analyzeChord` does not call the gates.** `chordanalyzer.cpp:1582-1584`: *"Gates A-L, the Iter 86/91
   promotions and the two-pass pedal detection run … at the call site AFTER this function returns. Do NOT
   call them here."* The gates are a **separate function** (`applyPostScoringGates`), invoked by the caller.
2. **The decoder never calls it.** `applyPostScoringGates` has **15 non-test call sites across 7 files**
   (`regionanalyzer.cpp:1000/1218/1408`, `harmonicsegmenter.cpp:395/404/547/744/821/913`,
   `regiontoneprimitives.cpp:516/574`, `sectionanalyzer.cpp:432`, `notationcomposingbridge.cpp:626`,
   `chorddiagnose.cpp:176`, and the header-inline `inferNextRootPc` at `chordanalyzer.h:748`).
   **None is in `chordslicedecoder.cpp`** (grep, whole `src/`).
3. **The decoder's one `analyzeChord` call passes `gateCtxOut=nullptr`** (`chordslicedecoder.cpp:452-454`),
   so it does not even *build* the `PostScoringGateContext` the gates consume; and `decideSlice` takes **no
   key parameter at all** (`chordslicedecoder.h:599-604`).

`ChordSliceDecoder` is referenced only by `tools/batch_analyze.cpp` (the `--decode-chords` diagnostic),
`decode_chord_tests.cpp`, and its own `.cpp` — i.e. **dormant**, engaged at E4, as the audit states.

**Verdict: Gate G-E does NOT threaten the collection/tonic split for the engaged decoder.** Prediction P1 held.

### 1.3 Two corrections to OI-167's characterization (evidence, proposed)

- **`keyTonicPc` is read at four places in the gate block, not one** — Gate G-E (`:380-382`), **Gate I**
  (`:467`, `:475`), **Gate L** (`:512`, `:520`), and the shared builder (`:66`). **OI-167's naming of G-E as
  *the* tonic-dependent gate is nevertheless CORRECT in substance:** Gates I and L use `keyTonicPc` only to
  compute `invInterval` and then test it for membership in `gateCtx.scale` (`:475-479`, `:520-524`) — the
  same collection-invariant construction as §3, so they are collection-only for the 19 modes where that
  construction is sound. **G-E is the only gate whose test is a *degree*.** This *strengthens* OI-167; it is
  offered as a precision note, not a contradiction.
- **Gates I and L inherit the §3 defect.** `gateCtx.{keyTonicPc, scale}` are forwarded from the same snapshot
  (`chordanalyzer.cpp:1497-1498`, `:1546-1547`), so on `Altered`/`AlteredDomBB7` their "diatonic" test uses
  the same semitone-transposed set. Relevant to the §3 finding, not to the decoder (they are gate-block code).

### 1.4 R1 coverage — the sub-rule question OI-167 asks

R1 = *"legacy chord competition + Gates A–L"* (`docs/implementation_roadmap.md:138`). G-E is a Gate-G
sub-rule, so **the letter range covers it** — OI-167's reading is right.

**But R1's coverage of the gate block is not the same as the gate block dying.** Of the 15 call sites, two
sets are **not** "legacy chord competition":
- **`harmonicsegmenter.cpp` (6 sites, L2)** — the **segmenter** runs full `analyzeChord` + gates to *score
  candidate segmentations* (`:391-405`, live).
- **`regiontoneprimitives.cpp` (2 sites, L1.5)** — `findTemporalContext` runs full `analyzeChord` + gates to
  obtain `previousRootPc`/`previousQuality` (`:506-522`, live). Already tracked as OI-165 / OI-12 / OI-86.

If either survives E4 while still calling `applyPostScoringGates`, **Gate G-E keeps firing after the
engagement** — not in L4, but in **L2 and L1.5**, which is a *worse* layer-forward position (the segmenter
and a fact-layer primitive consuming a tonic). This does not break the **L4** split, and it is out of
OI-167's scope, but it is the concrete form of the "confirm at E4" note OI-167 already carries. Recorded as
evidence for OI-13/OI-165, **no row re-scoped**.

---

## 2. Task 2 — the `sparsechordrefinement` Aeolian guard (`sparsechordrefinement.cpp:151-159`)

### 2.1 What it is (FACT — code)

```
// In plain Aeolian, a lone tonic or dominant pitch is too ambiguous to
// harden into a minor triad. Leave it unqualified and let richer later
// evidence decide the quality.
if (uniquePitchClasses == 1 && quality == ChordQuality::Minor
    && keyMode == KeySigMode::Aeolian && (degree == 0 || degree == 4)) {
    return;
}
```
The dispatch's description **reproduces exactly**: a lone A under **A-Aeolian** → `degree==0` → early return,
quality stays `Unknown`; the same lone A under **C-Ionian** → `degree==5`, `diatonicTriadShapeForDegree(5,
Ionian)` → `Minor`, guard does not fire → hardens to **A minor**. Identical collection, identical pitch,
different verdict. **Tonic-dependence: GENUINE (FACT)** — the guard keys on `keyMode` and on a *degree*.

Note the rest of the function is **collection-only**: `diatonicTriadShapeForDegree(degree, keyMode)` returns
the triad quality on a given pc, which is invariant across the rotations of one collection (a triad on A in
the C-major collection is minor whether the key is called C-Ionian or A-Aeolian). **The guard is the sole
tonic-dependent behavior on the quality axis in this file.**

### 2.2 Reachability in the engaged decoder: **UNREACHABLE (FACT)**

`refineSparseChordQualityFromKeyContext` is called from exactly five non-test places —
`regionanalyzer.cpp:1003/1221/1411` (all immediately after the legacy `analyzeChord` + gates + commit),
`sectionanalyzer.cpp:158`, and `notationcomposingbridge.cpp:640` (via the `notation::internal`
pass-through). **`chordslicedecoder.cpp` contains no reference to `sparsechordrefinement` at all** (grep,
whole `src/`). The decoder's decision surface is `decideSlice`, which takes no key (§1.2).

### 2.3 Need or artifact? — **ARTIFACT, on the code's own evidence**

Three code facts, none of them mine:

1. **The function's contract says it is a display concern.** *"Upgrade **user-facing** sparse results from
   Unknown to the diatonic triad quality implied by the resolved key/mode"* (`sparsechordrefinement.h:44-45`).
   It runs **after** the winner is committed (`regionanalyzer.cpp:1001` → `:1003`) and overwrites
   `identity.quality` — this is the DT-4 / OI-10 "quality-from-key single owner" substance OI-102 already
   carries.
2. **A sibling makes the opposite call on the same sonority.** `forceChordTrackQualityFromKeyContext`
   *"does NOT apply the Aeolian lone-tonic/dominant exclusion — appropriate for chord-track annotation where
   annotating even sparse/monophonic regions is desirable"* (`sparsechordrefinement.h:66-70`; impl `:203-218`).
   **The same lone pitch in the same key gets a different quality depending on which presentation surface is
   asking.** A genuine musical need does not change with the consumer; a presentation heuristic does.
3. **Nothing pins it.** No test in `src/composing/tests` references `refineSparseChordQualityFromKeyContext`
   or `applyTonicPriorToSparseChord` (grep). The only test touching this file is
   `pipeline_snapshot_tests.cpp:1475`, on the *sibling* that skips the guard.

**The honest reading.** The guard encodes a real observation — *do not harden a lone pitch into a triad on
thin evidence* — but expresses it in the **wrong currency (the tonic) at the wrong layer**. The evidence-side
formulation ("a single distinct pitch class is not enough to fix a triad quality") needs **no tonic at all**.

### 2.4 Does it fire? — **NO. Zero sites, all three corpora (FACT — measurement)**

Measured over the committed corpora (`tools/corpus/{baroque,jazz,default}`, 352 pieces each) by counting
regions with exactly one distinct pitch class (`popcount(pitchClassSet)==1`):

| preset | lone-pitch-class regions | guard-consistent (Aeolian, degree 0/4, quality `Unknown`) |
|---|---|---|
| Baroque | 4 | **0** |
| Jazz | 3 | **0** |
| Default | 4 | **0** |

**There is not a single `Unknown`-quality lone-pitch-class region in any preset** — every one of the 11
carries a committed quality. The inference is tight on the `regionanalyzer` path: if the guard fires, quality
stays `Unknown` through the immediately following `applyTonicPriorToSparseChord`, which requires quality ∈
{`Power`,`Suspended2`,`Suspended4`} (`sparsechordrefinement.cpp:174-180`) and therefore cannot re-harden an
`Unknown`. **A fired guard ⟹ a committed `Unknown` at a lone-pc region. There are none. The guard never
fired.**

*Honest bound:* this is an **output-surface** measurement (#15), not an instrumented branch counter. It
establishes *no net effect on committed quality*; a direct fire-count needs a build (proposed, §4.4). The
opportunity existed — Aeolian (`min`) is the second most common emitted mode on every preset — the
population (lone-pitch-class regions) is simply almost empty in four-part chorales.

**Verdict: the Aeolian guard does NOT threaten the collection/tonic split for the engaged decoder** — it is
unreachable there, and inert even where it is reachable.

---

## 3. ⛔ THE STOP — a third tonic-dependent site, **inside** the engaged decoder

This is the finding the pass exists to surface. It is **at the site OI-167 declares safe.**

### 3.1 The decoder does consume `keyTonicPc` (FACT)

`decideSlice` takes no key — but the decoder's **candidate generation** does. `candidatesForWindow` calls
`analyzer.analyzeChord(tones, keySignatureFifths, keyMode, …)` (`chordslicedecoder.cpp:452-454`) and consumes
`snapshot.cells` — the scored cube. Inside `analyzeChord`:

```
const int ionianTonicPc = ionianTonicPcFromFifths(keySignatureFifths);
const int keyTonicPc    = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;
…
static constexpr std::array<size_t, 21> DIATONIC_PARENT_INDEX = {
    0, 1, 2, 3, 4, 5, 6,   // diatonic: identity mapping
    1, 2, 3, 4, 5, 6, 0,   // melodic minor family: Dorian…Ionian parents
    5, 6, 0, 1, 2, 3, 4    // harmonic minor family: Aeolian…Mixolydian parents
};
const std::array<int,7>& scale = keyModeScaleIntervals(keyModeFromIndex(DIATONIC_PARENT_INDEX[keyModeIndex(keyMode)]));
```
(`chordanalyzer.cpp:1329-1342`.) `keyTonicPc` and `scale` then feed the two key-consuming scoring terms
(`:1403`, `:1406`), each a membership test over the constructed set
**S = { (keyTonicPc + scale[i]) mod 12 }**:
- `dim7CharacteristicBonus` — `for (int interval : scale) if ((keyTonicPc + interval) % 12 == dim7Pc) return 0.0;` (`:574-578`)
- `diatonicRootContribution` — `for (int interval : scale) if ((keyTonicPc + interval) % 12 == rootPc) return prefs.diatonicRootBonus;` (`:901-905`)

The decoder's own comment already knows these are key-dependent: *"the scorer's chosen ROTATION came from the
**KEY-dependent** `dim7CharacteristicBonus` + diatonic-root term"* (`chordslicedecoder.cpp:704-705`).

### 3.2 The algebra: S = the signature's collection, **transposed by δ** (FACT — derivation)

Write `P(M) = DIATONIC_PARENT_INDEX[M]`. For any **diatonic** mode P, `keyModeTonicOffset(P) + scale_P[i]`
enumerates, over i = 0…6, exactly the seven Ionian degrees — so
`{ ionianTonicPc + offset(P) + scale_P[i] }` **is** the signature's collection. Therefore:

> **S = (the signature's diatonic collection) transposed by δ, where δ = keyModeTonicOffset(M) − keyModeTonicOffset(P(M)).**

The tonic cancels **iff δ = 0**. Checking all 21 modes against `keyModeTonicOffset`
(`keymodeanalyzer.h:81-103`) and `DIATONIC_PARENT_INDEX`:

| mode | parent | offset(M) | offset(parent) | **δ** |
|---|---|---|---|---|
| the 7 diatonic modes | self | — | — | **0** ✅ |
| MelodicMinor…AeolianB5 (7–12) | Dorian…Locrian | 2,4,5,7,9,11 | 2,4,5,7,9,11 | **0** ✅ |
| **Altered (13)** | **Ionian (0)** | **1** | **0** | **+1** ❌ |
| HarmonicMinor…LydianSharp2 (14–19) | Aeolian…Lydian | 9,11,0,2,4,5 | 9,11,0,2,4,5 | **0** ✅ |
| **AlteredDomBB7 (20)** | **Mixolydian (4)** | **8** | **7** | **+1** ❌ |

**19 of 21 modes: δ = 0 — S is exactly the signature's collection, the tonic cancels, and OI-167's claim
holds.** For **`Altered`** and **`AlteredDomBB7`**: **δ = +1**. S is the collection **transposed up a
semitone** — a set that is neither the signature's collection nor the mode's own scale.

**Worked case.** C-Altered ⇒ `ionianTonicPc = 11` (B major), `keyTonicPc = 0`, parent scale = Ionian ⇒
**S = {0,2,4,5,7,9,11}** = the **C-major** collection. The signature's actual collection is B major
= {11,1,3,4,6,8,10}; the true C-altered scale is {0,1,3,4,6,8,10}. **S shares 2 of 7 pitch classes with the
signature's collection and 2 of 7 with the mode's own scale.** The diatonic-root bonus is handed to almost
entirely the wrong roots.

**This is not merely a break of the premise — it is a defect against the code's own stated intent**, which is
in the comment three lines above it: *"Non-diatonic modes are mapped to their diatonic key-signature parent
**so that diatonic-root bonus and scale-membership scoring stay correct** for the parent tonal context"*
(`chordanalyzer.cpp:1333-1335`). **DT-1** (a load-bearing causal claim about our own system, checkable and
unchecked). The construct is *structurally unsatisfiable* for these two modes: their tonic is not a member of
their parent collection (offsets +1 and +8 are not Ionian degrees), so **no** choice of diatonic parent index
can make the anchoring recover the collection.

### 3.3 Is it live? — **YES on Jazz (FACT — measurement + code)**

All 21 modes are enabled: `ACTIVE_MODE_INDICES` / *"All 21 modes are active"* (`keymodeanalyzer.cpp:70-71`).
Emitted region keys across the committed corpora (mode suffix pinned at the code —
`keyModeSuffix(KeySigMode::Altered) == "alt"`, `keymode_branch_tests.cpp:153`):

| mode | Baroque | **Jazz** | Default |
|---|---|---|---|
| **`Altered`** (δ=+1) | 0 | **24 regions** | 0 |
| **`AlteredDomBB7`** (δ=+1) | 0 | 0 | 0 |

And the emitted region key **is** the value handed to the scorer: `localKeyMode = localKey.mode`
(`regionanalyzer.cpp:955-957`) → `analyzeChord(tones, localKeyFifths, localKeyMode, …)` (`:987-988`).

**⇒ On 24 Jazz regions, `analyzeChord` scores with `keyMode = Altered`, and both key-consuming terms
evaluate membership against the C-major-shaped set instead of the signature's collection.** The defect is
**live on the legacy path today and would be live in the engaged decoder**, which calls the same
`analyzeChord`.

*Honest bounds (#19).* (a) The **mechanism** is FACT (algebra + code). (b) The **exposure** is FACT (24
emitted Altered regions; the mode reaches the scorer by the cited call chain). (c) **Whether the corrupted
bonus actually flips a winner on those 24 regions is UNMEASURED** — that needs a build + the robust-stop diff
(§4.4). I am not claiming a magnitude. `AlteredDomBB7` is currently **0-firing** (DT-7) — the defect is real
but dormant for that mode.

### 3.4 What this does to the premise

The collection/tonic split says: **L4 can be decided from the collection alone, before the tonic is fixed.**
For 19 modes that is exactly what the code does — the tonic provably cancels. For `Altered`, the score
depends on **which mode (hence which tonic)** was chosen, because S ≠ the collection. **The engaged decoder's
candidate scores are therefore tonic-dependent on a live, non-empty population.** The split, as OI-167 states
it, is **false for the engaged decoder today.**

---

## 4. Verdict and disposition proposals

### 4.1 The verdict

> **The collection/tonic split holds CONDITIONALLY — but not on the condition OI-167 names.**
>
> The two sites OI-167 names (Gate G-E, the Aeolian guard) are **both unreachable in the engaged decoder**
> and neither threatens the split (§1.2, §2.2). OI-167's stated condition is therefore **already satisfied**.
> But the split **breaks inside the decoder** at the site OI-167 clears — the `keyTonicPc`-anchored
> membership sets of `analyzeChord` — for 2 of the 21 modes it accepts, one of which is live (§3).
>
> **The split is RESTORABLE to unconditional, and by a change that makes it structural rather than
> algebraic** (§4.3). It does not hold today.

### 4.2 Per-site dispositions (PROPOSALS — the call is the user's)

| site | tonic-dependence | engaged-reachable? | proposed disposition |
|---|---|---|---|
| **Gate G-E** (`postscoringgates.cpp:376-397`) | **genuine** (a degree test; not reformulable collection-only) | **NO** — the decoder never calls `applyPostScoringGates` | **RETIRE with R1.** It dies with the legacy path. *Rider:* R1's letter range covers the sub-rule, but confirm at E4 that the **`harmonicsegmenter` (L2, 6 sites)** and **`regiontoneprimitives` (L1.5, 2 sites)** gate call sites die or are re-pointed too (§1.4) — otherwise G-E survives at L2/L1.5. Evidence for OI-13/OI-165; **no row re-scoped** |
| **Aeolian lone-tonic guard** (`sparsechordrefinement.cpp:151-159`) | **genuine** (a mode + degree test) | **NO** — the decoder never calls the file | **RE-HOME** (preferred) — the decision is a *user-facing sparse-quality assignment made after the key is known*; it belongs on the presentation/L5 surface where the tonic is legitimately available, not in L4. This makes L4 tonic-independent **with zero behavior change**. Settles OI-102's carried question (i) in favor of **not-L4**, which also contradicts **OI-90's L4 re-tag** — proposed correction, §5 |
| **`analyzeChord`'s two key-consuming terms** (`chordanalyzer.cpp:1329-1342`, `:574-578`, `:901-905`) — **NEW** | **genuine for `Altered`/`AlteredDomBB7`** (δ=+1); provably absent for the other 19 modes | **YES — this is *in* the decoder** | **FIX, and thereby make the split structural** — §4.3. **Do not build this session** (inference-affecting; #8/#14). Filed **OI-168** |

**Retire vs re-home for the Aeolian guard — the honest trade-off.** Two options; they are *not* equivalent
and I do not recommend choosing blind:
- **RE-HOME** (recommended): move the whole post-commit sparse-quality refinement to the presentation/L5
  surface. **Zero behavior change** (it already runs post-commit). L4 becomes tonic-independent on this axis.
- **RETIRE the tonic-dependence** (reformulate as "a single distinct pitch class never hardens to a triad"):
  cleaner in principle, but it is a **behavior change** — it would also stop the lone-pitch hardening that
  *currently happens* in Ionian (2/1/2 regions harden to a quality today, §2.4). Small, but it must go
  through the robust-stop diff, not be waved through. **Deferred to the design pass with the measurement.**

### 4.3 The proposed fix for §3 — one change kills the defect **and** makes the split structural

The membership set the two terms want **is** the signature's collection. The repository **already has that
function**, and its contract states the property the whole split needs:

```
/// 12-bit mask of the diatonic pitch classes of a key SIGNATURE (Ionian).
/// Key-agnostic: depends ONLY on the notated signature, never a resolved mode.
inline uint16_t diatonicMaskFromFifths(int fifths) noexcept          // analysisutils.h:82-94
```

**Proposal:** replace the `(keyTonicPc + scale[i])` membership loops in `dim7CharacteristicBonus` and
`diatonicRootContribution` with `pcInMask(diatonicMaskFromFifths(keySignatureFifths), pc)`.

- **Byte-identical for all 19 δ=0 modes** — `diatonicMaskFromFifths(fifths)` and `{keyTonicPc + scale[i]}`
  are the same set there (verified: for fifths=0 both are {0,2,4,5,7,9,11}). *Predicted: no change on
  Baroque/Default, which emit zero `Altered` regions.*
- **Corrects `Altered`/`AlteredDomBB7`** to the signature's actual collection.
- **The tonic-independence becomes STRUCTURAL, not algebraic** — after the change these terms *do not take a
  tonic*. The collection/tonic split stops resting on a cancellation that a future mode-table edit could
  silently break (which is exactly how this defect was born), and becomes true by construction — a #17/#19
  posture rather than a coincidence.
- **This is a behavior change on Jazz** (24 regions) ⇒ robust-stop diff, class-(b) duration non-increase per
  preset, explained run-level set-diff, user ratification (#14). **Not this session.**

**Note the residual (#12):** the two terms would then no longer distinguish a *mode's own* scale from its
parent collection — but they never did (they already use the parent's intervals by design,
`chordanalyzer.cpp:1333-1335`). No information is lost; a mis-anchored set is discarded.

### 4.4 Owed measurements (neither run this session — both need a build)

1. **Instrumented fire counts** — an `analyzeChord` counter for `keyMode ∈ {Altered, AlteredDomBB7}`, and a
   branch counter on the Aeolian guard's early return. Converts §2.4 and §3.3 from output-surface inference
   (#15) to direct FACT. The default-OFF fire-count instrument pattern of the L4-2b audit applies.
2. **The §4.3 fix's robust-stop diff** — class-(b) root-disagree duration non-increase per preset + the
   explained run-level set-diff. Predicted: Baroque/Default byte-identical; Jazz moves on ≤24 regions.

---

## 5. Register — one new row; two proposed corrections to existing rows (not applied)

Per the standing register rule (c) — *"every newly discovered issue gets a register row in the same commit
that records the discovery"* — **one new row is added**. The dispatch's "no register re-scope" is honored:
**no existing row is edited.** The two corrections below are recorded here as **proposals with evidence**,
for the design pass to apply.

- **NEW — OI-168** (added this commit): the `Altered`/`AlteredDomBB7` δ=+1 defect (§3). Type **DT-1**
  (Class-A unverified causal premise, #18) with a **DT-7** rider (`AlteredDomBB7` 0-firing).
- **Proposed correction to OI-167** (not applied): its FACT-labeled claim *"pure collection-membership tests
  (…provably identical for all 7 diatonic modes of one signature)"* is **true but insufficient** —
  `analyzeChord` accepts 21 modes and the key layer emits non-diatonic ones; the property fails for 2 of
  them. The row's **conclusion** (the two named sites do not threaten the split) is **confirmed**; its
  **premise** needs the §3 qualification.
- **Proposed correction to OI-90 / OI-102(i)** (not applied): OI-90 re-tagged
  `region/sparsechordrefinement.{h,cpp}` **L4**. The evidence (§2.3 — a post-commit, *user-facing* quality
  overwrite whose sibling makes the opposite call for a different presentation surface, unreferenced by any
  composing unit test) supports **not-L4**. This is the disposition of OI-102's carried question (i).

---

## 6. Self-check against the guiding principles (CLAUDE.md, after re-reading the diff)

- **#1/#2 (fact- and theory-based; specific over general):** every claim is cited to code or to a measurement
  I ran; the algebra in §3.2 is derived, not asserted. **#5:** where facts were scarce (does the guard fire?)
  I measured instead of assuming — and the assumption was wrong.
- **#3/#13 (surprise = STOP):** §3 is surfaced as a STOP **before** anything is built around it, and my
  prediction/finding gap is reported as a failure (§0), not a curiosity.
- **#8 (no inference-problem-driven coding) / dispatch scope:** the §3 defect is **declared, not fixed.** No
  `src/` edit, no build, no golden, no retirement, no existing-row re-scope. The §4.3 fix is a proposal.
- **#15 (verify at objects/data, not assertion):** §2.4 and §3.3 are corpus measurements, and both carry an
  explicit honest bound on what an output-surface count can and cannot establish.
- **#17(f) (no hand-transcribed numbers):** every figure in §2.4 and §3.3 is the direct output of the scripts
  quoted in-place, run this session against the committed corpora.
- **#19 (nothing trusted because merely unfalsified):** the finding *is* an instance — OI-167's claim was
  unfalsified, not established. §4.3 proposes replacing an algebraic cancellation with a structural guarantee
  so the property cannot silently lapse again.
- **Conventions:** American English; no self-invented labels — every name used (`Gate G-E`, `Altered`,
  `DIATONIC_PARENT_INDEX`, `diatonicMaskFromFifths`, R1, DT-1/DT-4/DT-7, OI-90/OI-102/OI-165) already exists
  in the repository.

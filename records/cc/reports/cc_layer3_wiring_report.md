# CC — Layer 3 key/mode WIRING report (Step 1, BASELINE scorer)

**Status: STOP / SURFACE — gates moved the wrong way. Code written + built + measured; NOT committed; NO goldens
refreshed; Step 2 reweight NOT applied.** Held / gitignored (`/cc_*.md`). Cowork verifies at source; user ratifies the
tradeoff (or directs a revision) before any commit. Built at HEAD `2203ad9fda`; corpora stamped `git 2203ad9fda`.

This implements the §2 wiring to the user-ratified choices (intra-region **(b) duration-majority**, seed **S2**,
**P4-defer**, confidence **C1**, single-signature **accept**). It builds clean and is *faithful to the as-graded
decoder* (held-out probe below). It is **held at the §6 stop conditions**: the BIR **case-identity** gate regresses on
**all three presets** (Jazz also crosses the integer 23→24) and **both** notation suites fail. Per the low-risk
directive I did **not** force it, **not** refresh goldens to mask it, and **not** pull Step 2 in to rescue it.

---

## §1 — As-wired data flow (what was built)

All edits are under `src/composing/` (pre-authorized). Five files:

### 1a. Decoder — `keymodesequence.{h,cpp}` (fidelity gaps #1 + #3)
- **`excludeStaves` threaded** (gap #1): added a trailing `const std::set<std::size_t>& excludeStaves = {}` to
  `decode()` and `redecodeRange()`; threaded `decode()/redecodeRange() → buildLattice → buildSliceContext →
  pitchContextOverSpan` (the view already accepted it; it was hardcoded `{}`). Default `{}` keeps every existing caller
  (`batch_analyze.cpp:2141` `--decode-keymode`; `decode_keymode_tests.cpp`) byte-identical.
- **C1 emission confidence** (gap #3): new anon-namespace `populateEmissionConfidence(out, lat, keyPrefs)`, called from
  `decode()`/`redecodeRange()` (which have `keyPrefs` + the lattice). It stamps each `SliceKeyMode.chosen.normalizedConfidence`
  with the analyzeKeyMode **winner sigmoid** (`keymodeanalyzer.cpp:762-767`) re-expressed over the lattice's per-slice
  emission scores: `gap = emission[chosen] − best-competing-emission`, mapped through
  `keyPrefs.confidenceSigmoid{Midpoint,Steepness}`. When the decoder's chosen state IS the local emission argmax (the
  common, agreement case) this is **byte-for-byte** the emission winner confidence (chosen=winner, competitor=runner-up);
  when sequence smoothing overrode the local argmax the gap is ≤0 → ≈0 confidence (the safe direction — a key resting on
  sequence context, not local evidence, does not clear the 0.8 gate). `decodeLattice` stays scorer-independent (still
  0.0), so the synthetic decoder unit tests are untouched.

### 1b. Resolver — `keyresolver.{h,cpp}` (fidelity gap #2, no duplication)
- New public **`resolveKeySignatureContext(score, tick, staffIdx, excludeStaves, prefs)` → {notatedFifths,
  correctedFifths, declaredMode}**. It is the *exact* signature read + declared-mode mapping + declared-gated Baroque
  `partialSignatureCorrection` the resolver already did (lines 218–263), lifted verbatim. `resolveKeyAndModeRanked` was
  refactored to call it (byte-identical — see §3 evidence). The wiring calls the **same** function ⇒ **no duplicated
  signature/partial-correction logic** is introduced.

### 1c. Region path — `regionanalyzer.cpp` (the seam @633)
- Reuses the whole-score `noteModel` (@508). Computes `keySigCtx = resolveKeySignatureContext(startTick, refStaff,
  excludeStaves, keyPrefs)` once.
- Adds `slices = slc::changePointSlices(noteModel)`; runs `KeyModeSequenceDecoder::decode(slices, noteModel,
  keySigCtx.correctedFifths, keySigCtx.declaredMode, keyPrefs, kDefault…, excludeStaves)` **once**, before Pass-1.
- Builds `sliceEnds` for an O(log N) `upper_bound` region→slice-run lookup. `localKeyForRegion(rs,re)` does
  **duration-majority** over the overlapping slice run (ties → lower representative slice index, deterministic), returns
  the representative slice's `chosen` (carrying its C1 `normalizedConfidence`), falling back to the segmentation **seed**
  if a region overlaps no decoded slice.
- **Replaced @633:** the per-region `resolveKeyAndModeRanked(..., &prevKeyResult)` → `localKeyForRegion(...)`. Feeds the
  existing consumers unchanged (`analyzeChord` @668, `inferNextRootPc` @653, `refineSparse…` @684, `applyTonicPrior…`
  @686, `keyModeResult` @723/@740).
- **Retired** from the region production path: the @633 resolver call, its hysteresis, and the `prevKeyResult`
  threading (declaration + per-region update). The seed @521 (S2) and Pass-2/2b inheritance are untouched.

The three fidelity fixes (§2.5) are all in. **Held-out faithfulness verified** (§3): the wired production key matches
the isolated as-graded `--decode-keymode` diagnostic ⇒ the fixes introduced **no** wiring discrepancy.

---

## §2 — Gate results (MANDATORY, both presets) — the STOP

### BIR case-identity (the hard gate) — **REGRESSION on all 3 presets**
Counts dropped, but the gate is the **case-identity set, not the integer** (CLAUDE.md). New BIR=false case identities
appeared on every preset (a case-identity regression = HARD STOP), and Jazz also rose on the integer:

| preset | gate | new total | net | NEW cases (regressions) | FIXED cases (gains) |
|---|---|---|---|---|---|
| Baroque | 57 | **53** | −4 | **bwv272@4320** (Bdim7/D), **bwv289@20160** (C#dim7/E) | bwv102.7@17520, bwv122.6@6720, bwv227.7@18120, bwv301@960, bwv336@8640, bwv381@4800 (6) |
| Jazz | 23 | **24** | **+1** | **bwv272@4320**, **bwv291@17760** | bwv244.15@10080 (1) |
| Default | 57 | **53** | −4 | **bwv272@4320**, **bwv289@20160**, **bwv387@10560** | bwv102.7, bwv122.6, bwv187.7@19200, bwv301@960, bwv336@8640, bwv352@1440, bwv381@4800 (7) |

- **Character of the NEW cases:** all are **symmetric fully-diminished-7th rotation** disagreements (delta +3 = our root
  a m3 above DCML; `bwv272@4320` Bdim7, `bwv289@20160` C#dim7, etc.) — the "root pitch-class-undefined by construction"
  class CLAUDE.md flags as ≈53% of Baroque BIR=false. The decoder changed the local key → a *different (equally valid by
  pitch-class)* dim7 rotation won. `bwv272@4320` is new on **all three** presets (a consistent new region).
- **Character of the FIXED cases:** these look more substantive (not all dim7-symmetric) — a net-positive direction on
  Baroque/Default. But the rule is strict: **any new case = STOP**; Jazz **+1 = STOP**.

### Both suites — **FAIL**
- `composing_tests`: **596/596 PASS** ✓ (incl. `regionanalysis_tests` resolver/hysteresis/normalizedConfidence tests ⇒
  the resolver refactor is byte-identical).
- `notation_tests`: **52/57** — 5 fail (production output moved):
  `MozartK279OpeningPrefersCMajorOverFLydian` (front region fifths 0→−1), `CorelliOp01n08dOpening…DoNotSmearPreviousChord`
  (a beat Gm→G), `PopulateChordTrackEmitsCadenceMarkersOnCorelli` (C1-gated cadence markers moved),
  `BehaviorSnapshot_RomanNumeral`, `BehaviorSnapshot_Nashville` (key-relative RN re-spell).
- `pipeline_snapshot_tests`: **0/11** — all moved.

### Pipeline snapshot diff (produced; NOT refreshed — reverted git-clean)
Full diff generated transiently via `--update-goldens` then **`git checkout` reverted** (goldens confirmed 0 modified;
nothing masked). Per-section attribution (which top-level golden section each file's hunks touch):

| section | moved? |
|---|---|
| `annotation` (P2) | several files |
| `implode` (P1) | several files |
| `implodedChordTrack` | several files |
| `keyAreas` | **all 11** (C1 confidence + key labels) |
| `tickRegional` (P3) | several files |
| **`tickLocal` (P4)** | **NONE — byte-identical in all 11** ✓ |

**P4 goldens are byte-identical (the P4-defer requirement HOLDS) ⇒ no leak.** The moves are exactly the
region-path-derived sections (P1/P2/P3/keyAreas), confirming the change is correctly scoped. Representative value moves:
key `C→F` (mozart_k279), `G→C` (chopin_op30_1), `D→A` (chorale_137), `Cm→Ab/G` (corelli_op01n08a); RN `bVI→VI`,
`I→V`, `i→iv`; keyArea confidences shift (C1).

### S2 segmentation (coarse grid)
**Byte-stable by construction.** The seed @521 is unchanged ⇒ `greedyExpandSegmentation`'s `keyFifths/keyMode` inputs
are unchanged ⇒ `boundaryTicks` (computed before the Pass-1 loop, untouched) is identical. The new BIR sub-region ticks
(`bwv272@4320` etc.) are **Pass-2/2b sub-boundaries**, which run on the (legitimately changed) chord analysis — not a
coarse-grid (S2) violation. (A direct `greedyExpandSegmentation`-output instrument was not added; the construction
argument is airtight for the coarse grid.)

### Held-out direct metric — **wiring is FAITHFUL** (no §2.5 discrepancy)
The decisive bug-vs-move probe. Isolated as-graded `batch_analyze --decode-keymode --preset Baroque` on K279-1 reads the
**entire opening (m1–m3+) as Fmaj** (emission ≈17.4 vs Cmaj ≈14.6; Cmaj the runner-up). My **wired** production output
also reads the K279 opening as F (annotation key `C→F`). ⇒ The C→F flip is the **decoder's own baseline-scorer**
behavior (the build-report-predicted "Baroque unambiguous −3.0"), faithfully wired — **not** a bug in excludeStaves /
correctedFifths / C1. Baroque corpus chord-identity-agree = **90.9%** (10250/11271).

---

## §3 — Diagnosis: this is a *baseline-scorer* limitation, not a wiring bug

- The resolver refactor is byte-identical (composing_tests incl. resolver tests pass; **P4 byte-identical**).
- The wired key == the as-graded decoder key (K279 probe). The §2.5 fidelity fixes are correct.
- ⇒ The regressions (K279 C→F opening; the symmetric-dim7 new cases; Jazz +1) are the **decoder's BASELINE emission**
  preferring the subdominant / a different dim7 rotation where local evidence is thin. This is exactly what the
  **Step-2 `scaleMembership` reweight** (`cc_layer3_sweep_report.md` §3-SPEC) is designed to correct — and it is
  **explicitly out of scope** for this increment (instruction §6: "Tempted to apply the scaleMembership reweight (Step 2)
  → STOP"). I did **not** apply it.

---

## §4 — Unification ledger (instruction §4)

- **Reused (no re-implementation):** the committed decoder `keymodesequence.{h,cpp}`; its emission
  `analyzeKeyMode` + 252-dump; the shared indexed view `pitchContextOverSpan`; `changePointSlices` (L2);
  `partialSignatureCorrection` (now reached via the shared `resolveKeySignatureContext`); the `HarmonicRegion::keyModeResult`
  carrier; Pass-2/2b inheritance (untouched).
- **Newly written (wiring only):** the `analyzeRegions` plumbing (`changePointSlices` call, one `decode()`, the
  `sliceEnds` index, the duration-majority `localKeyForRegion`); the `excludeStaves` decoder param; the C1
  `populateEmissionConfidence`; the shared `resolveKeySignatureContext` (extraction, **shared** by resolver + wiring).
- **Retired (from the production region path):** `resolveKeyAndModeRanked` @633 + its hysteresis + the `prevKeyResult`
  threading; `collectPitchContext` as the region builder.
- **End-state:** on the production region path, **one key path (decoder) + one builder (`pitchContextOverSpan`)**.
  Surfaced residuals (pre-existing, not created): (i) **P4 tick-local** still uses `resolveKeyAndModeRanked` +
  `collectPitchContext` (P4-defer; **verified byte-identical** this run) — named follow-up *P4-redecode*; (ii) the
  resolver + `collectPitchContext` remain compiled as the **seed (@521, S2)** and the diagnostic/grading baseline.
  **No NEW parallel path or logic duplication was introduced; the P4 residual is pre-existing and surfaced with a named
  follow-up.**

## §5 — Single-signature affected-stem count
Not yet enumerated (a separate scan of stems with notated mid-piece KeySig changes). Can be produced on request; the
Bach corpus is overwhelmingly single/zero-signature, so the affected set is expected to be small. Flagged as the one
outstanding §3 report item.

## §5b — STEP 2 brought forward (user-directed) + (a)/(b) classification — does NOT clear the gate

User direction: bring Step 2 forward AND classify the regressing cases (a)/(b) first; the combined increment must
clear the full gate; persistent dim7 churn returns as its own scoped decision (not bundled into "accept").

### (a)/(b) classification of the NEW regressing cases — ALL class (a)
| case | preset(s) | sonority | Δ | class |
|---|---|---|---|---|
| bwv272@4320 | Baroque, Jazz, Default | Bdim7/D | +3 | (a) symmetric fully-dim7 rotation (root pc-undefined) |
| bwv289@20160 | Baroque, Default | C#dim7/E | +3 | (a) symmetric fully-dim7 rotation |
| bwv291@17760 | Jazz | Gm6/Db | +3 | (a) half-dim/m6 ↔ ø7 share-tone rotation |
| bwv387@10560 | Default (Step-1 only; **fixed by Step 2**) | E7b9/G# | +8 | (a) dim7 subset of V7b9 |
| bwv282@12000 | Baroque (**introduced by Step 2**) | FMaj7/C vs Am | +8 | (a) share-tone rotation (FMaj7 ⊃ Am triad) |

**No class (b) (genuine functional key/root) regression appears on any preset.** Every new BIR=false case is a
diminished/share-tone **rotation ambiguity** — the CLAUDE.md "structurally unresolvable by pitch class" class
(≈53% of Baroque BIR=false), key-orthogonal.

### Step 2 = §3-SPEC scaleMembership **sharp1** (`scaleScoreInKeySigOnly −0.20→−0.60`,
`scaleScoreInNeither −0.05→−0.30`), applied **decode-only** in `analyzeRegions` (decoder emission only; the seed @521
and P4 resolver keep un-sharpened weights ⇒ **S2 grid + P4 byte-identical preserved**). Rebuilt clean.

| metric | Step-1 only | Step-1 + Step-2 sharp1 | gate |
|---|---|---|---|
| BIR Baroque | 53 (2 new) | **54 (3 new** — Step-2 fixed nothing here, **added** bwv282@12000; 6 fixed) | 57 / no new |
| BIR Jazz | 24 (2 new, +1) | **24 (2 new, +1** — unchanged) | 23 / no new |
| BIR Default | 53 (3 new) | **52 (2 new** — Step-2 **fixed** bwv387@10560; 7 fixed) | 57 / no new |
| chord-identity agree (Baroque) | 90.9% (10250) | **90.9% (10249)** — flat | — |
| chord-identity agree (Jazz/Default) | 91.7% / 90.8% | **91.7% / 90.8%** — flat | — |
| MozartK279 opening (notation test) | fifths −1 (F) FAIL | **−1 (F) FAIL** — unchanged | 0 (C) |
| composing_tests | 596/596 | **596/596** ✓ | pass |
| notation_tests | 52/57 | **52/57** (same 5) | pass |
| pipeline_snapshot_tests | 0/11 | **0/11** | pass |

**Two decisive Step-2 findings:**
1. **Step-2 does NOT clear the case-identity gate.** All three presets still carry new class-(a) cases. The residual is
   diminished/share-tone **rotation churn**, which is *orthogonal to key tuning* — Step-2 sharpens the **key** scorer, so
   it cannot resolve which rotation of a symmetric dim7 (or a share-tone tetrad) is "root". It even reshuffled the churn
   (fixed bwv387 on Default, introduced bwv282@12000 on Baroque).
2. **Step-2's measured key-accuracy gain does NOT move the chord/BIR metric here.** Chord-identity agreement is flat
   (90.9%→90.9% etc.). A decoder-level pre-check (no rebuild) shows the K279 opening slice reads **Fmaj at every
   sharpening strength** (sharp1, sharp2 −0.9/−0.5, even −1.5/−1.0): the short opening has **no local distinguishing
   degree** to penalize, so the scale-contrast lever is *inert* for it. The sweep's +57/+73 was a *region-KEY* accuracy
   gain on the held-out split; it does not translate into the *chord-root* BIR gate, and does not fix the reweight-inert
   no-local-evidence openings.

**Conclusion:** the combined Step-1+Step-2 increment is faithful and correctly scoped (P4 byte-identical, S2 grid
stable, no duplication), and on Baroque/Default it **fixes more BIR cases than it breaks** (6 vs 3 / 7 vs 2) — but it
**cannot clear the strict case-identity gate**, because the residual regressions are key-orthogonal class-(a)
diminished/share-tone **rotation ambiguities** (+ the Jazz +1). This is precisely the user-anticipated "dim7 churn →
its own scoped decision," and it is the gate-design gap the CLAUDE.md flags for Stage 5/6 (a two-tier / spelling-aware
gate). The working tree currently holds Step-1 + Step-2 sharp1 (the Step-2 edit is a 3-line decode-only block, trivially
revertible).

## §5c — USER DECISION (2026-06-23): hold + revert Step 2

The user directed **hold + revert Step 2**. The 3-line decode-only Step-2 block in `analyzeRegions` was reverted; the
working tree now holds the **faithful Step-1 wiring only** (decoder `decode()` is called with the un-modified caller
`keyPrefs`). Rebuilt clean to keep binaries coherent with the held source. **No commit** — held for Cowork
verification at source. The Step-2 `scaleMembership` reweight is deferred to a separate increment gated on the held-out
KEY metric (where its measured +57/+73 belongs), not the chord/BIR gate (on which it was flat here).

**Held state = Step-1-only wiring**, whose gate numbers (already measured this session) are: BIR Baroque **53** (2 new
class-(a)), Jazz **24** (2 new class-(a), +1), Default **53** (3 new class-(a)); composing **596/596**, notation
**52/57**, snapshots **0/11** with **P4 byte-identical**; S2 grid stable; held-out faithful (K279 wired == as-graded
decoder). The unresolved item carried forward is the class-(a) dim7/share-tone **rotation churn** (the scoped decision)
+ the Jazz +1 — to be taken up under the gate-policy / Stage-5 two-tier-gate question, not bundled into "accept."

## §5d — COMMIT-GATE re-run under the (B)-amended two-tier gate (2026-06-23) — surfaced, pre-commit

Per the COMMIT instruction: held state = **Step-1-only** (rule (b) duration-majority, S2 seed, **Step-2 reverted**,
shared scorer baseline −0.20/−0.05, no reweight residue — confirmed). Full gate re-run on the (b) build:

**BIR (canonical tools, all presets) — passes the (B)-amended gate:**
- **Baroque 53** (net −4), **Jazz 24** (net +1, accepted), **Default 53** (net −4).
- **Zero new class-(b)** on any preset (guardrail 1). Every new case verified **class-(a) at the score** (independent
  music21 over the GT region span this session):
  | case | preset(s) | GT-span pcs | structure |
  |---|---|---|---|
  | bwv272@4320 | B/J/D | {D,F,Ab,B} | symmetric dim7 [3,3,3,3] |
  | bwv289@20160 | B/D | {C#,E,G,Bb} | symmetric dim7 [3,3,3,3] |
  | bwv291@17760 | J | {D,E,G,Bb} | Eø7≡Gm6 share-tone |
  | bwv387@10560 | D | {D,F,Ab,B} | symmetric dim7 read as E7♭9 upper structure (dim7-subset-of-V7♭9) |
- **class-(b) (decidable-root) count non-increasing** (guardrail 3): only class-(a) cases were added and several cases
  fixed, so the class-(b) count can only fall. Magnitude small (≤3 new/preset) — within the watch.

**Both suites:** composing **596/596**; notation **52/57** (the 5 expected production moves: MozartK279 opening,
Corelli sparse-beat, Corelli cadence markers, RN + Nashville behavior snapshots); pipeline_snapshot **0/11** (goldens
pending ratified refresh).

**Pipeline snapshot diff (produced transiently via `--update-goldens`, then reverted git-clean — NOT refreshed):**
- **P4 (`tickLocal`) byte-identical in all 11** (P4-defer holds; no leak).
- Change classification (field histogram over the diff): **key 299 + romanNumeral/text 160 + mode 24** = the decoder's
  whole-sequence key choice replacing the per-region resolver, with dependent key-relative RN/mode re-spell — mostly
  relative/fifth-related shifts (G→C, E→A, D→F, C→A, …), the build-report-predicted move **(i)** (incl. the accepted
  −3 Baroque-stable cases, e.g. K279 opening C→F, faithfully wired); **confidence/score 26** = the **C1** mapping
  **(iii)**; **quality/root 10** = chord re-reading under the new key, incl. class-(a) rotation relabels **(ii)**;
  **tick/startTick/durationTicks 17** = Pass-2/2b sub-boundary movement (NOT coarse-grid). No unexplained/structural
  changes.

**S2 coarse grid stable** (seed @521 unchanged ⇒ greedy-expand boundaries identical; the tick shifts are Pass-2/2b).
**Held-out faithful** (K279 wired key == as-graded `--decode-keymode` == Fmaj; the Jazz BIR cases' wired keys match the
as-graded decoder) — no §2.5-fidelity discrepancy.

**STATUS (was STOP/SURFACE §3 — now RATIFIED + COMMITTED §4):** user ratified the BIR class-split + the classified
snapshot diff; proceeded to §4.

## §5e — §4 COMMIT (local, unpushed) — 2026-06-23, `a6b08af3fe`
- `--update-goldens` for the ratified P1/P2/P3 changes; **P4 (`tickLocal`) byte-identical** re-confirmed (0 P4 hunks);
  re-ran `pipeline_snapshot_tests` → **11/11 green**.
- Committed **locally on master** (`a6b08af3fe`, ahead of `origin/master` by 1, **NOT pushed**): **17 files** = the 5
  Step-1 wiring sources + the 11 refreshed snapshot goldens + the STATUS.md post-wiring BIR-baseline record.
  **Excluded** (verified absent from the commit): CLAUDE.md (the two-tier amendment is a separate Cowork doc-sync —
  canonical class-(b) sets untouched), `batch_analyze.cpp`/`localmodulationdetector.{cpp,h}` (B2 trio), the WIP docs,
  and the STATUS.md OQ-1 held WIP (isolated via `git stash`, restored unstaged after commit). `cc_*` reports gitignored.
- **HOLD (§6):** no push. `origin/master` unchanged at `2203ad9fda`. Awaiting Cowork source-verification of the
  committed object + user ratification before any push — **`origin` only, NEVER `upstream`**.

## §6 — Decision requested (held — do NOT commit until ratified) — POST Step-2

Step 2 was brought forward (§5b) and **does not clear the gate**: the residual is key-orthogonal class-(a)
diminished/share-tone **rotation churn** (+ Jazz +1), which neither the wiring nor the key reweight can resolve. No
class-(b) functional regression exists; on Baroque/Default the increment fixes more BIR cases than it breaks. The
strict **case-identity** gate (no new BIR=false case of *any* class) cannot be met by a key-layer change. Options:

1. **Accept class-(a) rotation churn as a scoped gate exception** ★ — re-read the gate as "no new class-(b) *functional*
   regression" (which HOLDS: 0 functional regressions, net BIR ≤ baseline on Baroque/Default). The CLAUDE.md already
   flags symmetric-dim7 as structurally unresolvable and names a future two-tier/spelling-aware gate (Stage 5/6); this
   is that gap surfacing. Then: decide Step-2 keep-vs-revert (it's chord/BIR-flat — its value is the held-out KEY
   metric, not measured here), update the 5 behavioral tests + refresh P1/P2/P3/keyAreas goldens (**P4 untouched**),
   commit locally. **Requires the user to ratify redefining the gate's intent** (a policy decision, not mine).
2. **Pursue a dim7/share-tone rotation stabilizer** (separate increment) — e.g. a key-context-aware diminished-rotation
   tie-break, or stabilizing the Pass-2/2b sub-region boundaries so chord-analysis changes don't reshuffle which tick a
   symmetric sonority lands on — aiming to actually clear the strict gate. More work; before any commit.
3. **Revert Step-2** (no chord/BIR benefit here; defer the reweight to a separate increment gated on the held-out KEY
   metric, where its +57/+73 belongs), keep the faithful Step-1 wiring, and take option 1 or 2 on that.
4. **Hold for Cowork review at source** (no further changes from me now).

Per the directive I am holding here. Working tree: 5 source files modified (unstaged; Step-1 wiring + the 3-line
Step-2 decode-only block), goldens git-clean, nothing staged, no commit. `upstream` not involved.

# cc_anchor_recompute_report.md — ANCHOR recompute-on-merged-tones: implementation + measurement

**Verdict: ★ HARD STOP (§6). Do NOT commit, do NOT `--update-goldens`.** The architecture change is
implemented as specified and the bounded settle is well-behaved, but the measured output movement is **away from
the DCML/music21 oracle** on exactly the held-harmony population the anchor targets. The naive "re-analyze the raw
tone union" recompute **over-reads non-chord (embellishment) tones**, promoting plain triads to suspended/added
chords. This is the §6 stop condition ("net oracle movement NOT toward DCML / new actionable errors → redesign,
don't ship") **and** the hard BIR gate (§6 "BIR=false increases in ANY preset (case-identity) → HARD STOP").

The working tree carries the (uncommitted) change for Cowork's mechanism review. HEAD is unchanged.

---

## 1. The change (as implemented — matches the ratified §0–§3 scope)

All edits are confined to `src/composing/analysis/region/regionanalyzer.cpp` (the orchestration body + the two
merge helpers). No detector, template, gate, scoring term, catalog, or out-of-module file was touched.

**New shared helpers (anon namespace):**
- `pcPresenceMask(tones)` — 12-bit pitch-class presence bitmask.
- `recomputeMergedChordIdentity(region, preMask, postMask, analyzer, prefs)` — **the §2 byte-identity guard +
  the recompute.** Adopts a fresh identity **only when `preMask != postMask`** (the union introduced a pitch
  class the surviving chord was never scored against). Otherwise keeps today's bass-only restamp → byte-identical.
  When it does recompute, it calls the production oracle `IChordAnalyzer::analyzeChord(region.tones,
  region.keyModeResult.fifths, region.keyModeResult.mode, /*context*/nullptr, prefs)` and adopts `front()`.
  Returns whether `(root,quality)` actually changed (drives the settle). Key is the region's **own** inherited
  key — not re-resolved (key axis stays decoupled, per §1). Temporal context is `nullptr` (a merged region's
  temporal neighborhood is ill-defined — see §6 below; this is a deliberate, flagged choice).
- `kAnchorSettleMaxIterations = 4`; `anchorNoteSettle(where, iters)` — env-gated (`CC_ANCHOR_SETTLE_LOG`)
  diagnostic, zero behavioral impact when unset.

**`tryCollapseSameChordRegion`** (Pass-1 `:725`, Pass-2 `:928`) — new params `(analyzer, prefs)`. On a firing
merge: capture `preMask`, extend endTick, `mergeChordAnalysisTones`, capture `postMask`, call the recompute
helper. **Bounded backward-settle (§3):** while the recompute moved the survivor's identity and it now equals its
own predecessor (contiguous, same root+quality), fold the survivor into the predecessor and re-derive, capped at
`kAnchorSettleMaxIterations`.

**`coalesceShortSameRootRuns`** (Pass-3 `:1144`) — split into `coalesceShortSameRootRunsOnce(... analyzer,
prefs)` (returns whether any recompute changed an identity) + a settle wrapper that re-runs while changed, capped
at `kAnchorSettleMaxIterations`. The run survivor's identity is now re-derived from the union (`preMask`/`postMask`
guarded) instead of inheriting the longest sub-region's identity + bass restamp.

`restampBassMinorSeventhAfterMerge` left in place (§0 deferred item 3). Split-first re-order (§0 item 1) and
joint-key re-emit (§0 item 2) **not** touched.

---

## 2. Build + unit tests

| Step | Result |
|---|---|
| Build (unity, `setup_and_build.bat`) | **clean, exit 0** (all 7 targets linked) |
| `composing_tests.exe` | **545/545 PASS** |
| `notation_tests.exe` | **52/57 — 5 FAILED** (all held-harmony over-reads; details below) |
| `pipeline_snapshot_tests.exe` (no `--update-goldens`) | **0/11 PASS — all 11 goldens moved** |

### 2.1 notation_tests failures — all are oracle-aligned assertions, all regress (Corelli op01n08d / Chopin BI16)
These are hand-written assertions encoding the **DCML ground-truth** chord track, not refreshable goldens.

| Test | Tick | HEAD (oracle) | After | Mechanism |
|---|---|---|---|---|
| `…OpeningNoteContextMatchesPopulateInCMinor` | 0 | `i` | `i(add11)` | union add-11 over-read |
| `…PreservesCorelliOp01n08dCarryInAndLateDominant` | 1440 | `Cm` | `Csus2` | union sus2 over-read |
| (same) | 2880 | `Cm` | `Cmadd9` | union add9 over-read |
| `…OpeningAndSparseLateBeatsDoNotSmearPreviousChord` | 8·0 | `G` | `Gsus` | union sus over-read |
| `…UserReportedChordTrackAudit` | 24·0 | `Fm` | `Fsus2` | union sus2 over-read |
| `ChopinBI16OpeningCollapsesRepeatedTonicRegions` | — | 1 region | 2 regions | recompute changed a region's quality → broke the downstream equal-chord collapse |

### 2.2 snapshot diffs — corpus-wide, same direction
All 11 goldens (Bach chorales, BWV806, Mozart K279/K280, Chopin Op30, Corelli, Schumann) moved. Representative:
`bach_chorale_003` → `i(add11)6`; `mozart_k280_1` → `Fsus`, `Isus4`; `mozart_k279_1` → region boundary shift
`12840 → 13440`. The pattern is uniform: **plain triad → sus/add over-specification**, plus a few
identity-driven boundary ripples.

**This is broader than the dossier's "small, merged-regions-only, inspectable" prediction — but the guard is
NOT leaking.** The changes localize to held harmonies (where merges-with-new-PC happen) and their downstream
boundary ripples. The dossier simply under-estimated how *common* "merge that adds a passing/suspension PC" is in
this corpus (dense 4-part homophony) — the targeted population is large, not small. (A dedicated unmerged-region
byte-identity audit is a redesign-verification step; the evidence here — composing unit tests green, all moves on
held harmonies — is consistent with a correctly-functioning guard.)

---

## 3. Bounded settle (§3) — mechanism is SOUND

Env-gated sweep over **510 scores** (bach_chorales + corelli). The settle re-iterated to exactly **iterations=2**
in 138 instances (79 `coalesceShortSameRootRuns`, 59 `tryCollapseSameChordRegion`) and **never exceeded 2**
(cap of 4 never approached; no oscillation). This is squarely the dossier's "expectation 1, occasionally 2".
The settle machinery is correct and convergent — the problem is **not** the settle.

---

## 4. BIR hard gate — Baroque (primary preset)

Corpus regenerated clean (353/353, manifest valid) with the anchor binary; `characterise_bir_false.py
--corpus-dir tools/corpus/baroque`.

- **Count:** HEAD 57 → after **54**.
- **But the gate is case-identity, and it is split — 11 NEW, 14 REMOVED:**

**NEW BIR=false cases (regressions — HARD STOP):**
```
bwv166.6@16080  bwv2.6@13440   bwv244.10@2400  bwv272@9600   bwv301@1440  bwv320@23040
bwv363@3840     bwv397@5280    bwv40.8@20160   bwv431@480    bwv64.8@16320
```
Several are literal embellishment over-reads in the BIR table itself: **`bwv40.8@20160 → Bbsus/G`**,
**`bwv431@480 → Fsus/D`** (both "incomplete minor-seventh"), `bwv272@9600 → Ddim7/F`.

**REMOVED BIR=false cases (genuine fixes):**
```
bwv10.7@36000  bwv102.7@17520  bwv14.5@8160   bwv227.7@18120  bwv245.17@4800  bwv261@33840
bwv320@31680   bwv352@1440     bwv358@6000    bwv381@4800     bwv416@10080    bwv429@24240
bwv432@5520    bwv60.5@30960
```

**Net:** the union-recompute **does** help where the inherited slice was a genuine misread (14 fixed), but
**hurts** where the inherited slice was the correct chord-tone reading (11 new). **11 new case identities = HARD
STOP** under §6, independent of the favorable net count.

### 4.1 Jazz / Default — NOT RUN (deliberate, logged — no silent cap)
Skipped on purpose. The Baroque case-identity increase + the corpus-wide snapshot/notation regression is already
a conclusive hard-stop; the change will not ship in this form, so two further 353-score regens would be wasted
compute. **Available on request** if Cowork/user wants the full three-preset table before the redesign decision.
(Oracle root-error `--section-level` per-beat view likewise deferred — it would only magnify the same regression.)

---

## 5. Root-cause analysis (for the redesign) — this is a *direction* problem, not a guard/threshold tweak

The defect the anchor identifies is **real**: a merged region's chord is inherited from one pre-merge slice
instead of re-derived from the final tones. But re-deriving from the **raw tone union** is the wrong fix, because
the union is a *superset* that includes **non-chord tones** — suspensions, passing tones, neighbor tones,
anticipations — which the original per-slice analysis correctly treated as embellishments. `analyzeChord` on the
full vertical union (especially with **no temporal continuity** to anchor the held harmony) promotes those
embellishments to chord members → `sus`/`add`/`add11`. The *old* behavior (inherit the dominant slice's
chord-tone-only triad + restamp bass) was **closer to the oracle precisely because** the dominant slice was the
embellishment-free reading.

Two corroborating ripples worth noting for the redesign:
- **Temporal `nullptr` is implicated.** The recompute drops the root-continuity signal that, in production,
  keeps a held harmony anchored against its own restatement. This is the dossier §5.2 coupling risk surfacing.
- **Identity→segmentation ripple** (dossier §5.1): `mozart_k279` boundary `12840→13440` — a recomputed identity
  changed a downstream collapse boundary. Identity changes are not inert w.r.t. partition.

**The fix needs a chord-tone vs non-chord-tone discriminator in the recompute**, e.g. one of:
1. **Duration/metric-weighted tone filtering** before re-analysis (drop low-weight, short-duration tones that are
   embellishments, then analyze the chord-tone core), or
2. **Adopt-only-if-stronger** restriction — reject a recomputed identity that merely *adds an extension* to the
   inherited (root,quality) (i.e. only adopt a genuinely different/better-supported root or quality, never a
   sus/add over-specification of the same root), or
3. **Preserve temporal continuity** so the held harmony stays anchored across the union.

Any of these is a **scoring/embellishment-logic** change — which under §6 / the CLAUDE.md scoring-doc rules is a
**separate scoring task**, not part of this region-orchestration step. **Surfacing, not proceeding.**

---

## 6. Stop conditions hit (§6)
- ✔ **BIR=false case-identity increase** (Baroque +11) → HARD STOP.
- ✔ **Net oracle movement NOT toward DCML / new actionable errors** (notation + snapshot over-reads) → STOP,
  redesign.
- ✔ **Change appears to need scoring/embellishment logic** (the chord-tone discriminator) → out of this step's
  scope → STOP and surface.
- ✘ Settle >2 / oscillation — **not** hit (max 2, convergent).
- ✘ Guard byte-identity leak on unmerged regions — no evidence of leak (moves localize to held harmonies).

## 7. What I did NOT do (per protocol)
- Did **not** `--update-goldens`. Did **not** commit. HEAD unchanged.
- Left the implementation in the working tree (uncommitted) for Cowork's mechanism verification.

## 8. Recommendation
The architecture diagnosis is correct and the isolated-core mechanism (guard + settle) works as designed — but
the recompute input (raw tone union) is wrong. **Redesign the recompute to operate on the chord-tone core, not
the raw union** (option 1 or 2 in §5), which is a scoring-layer task to be scoped under the CLAUDE.md scoring-doc
rules. Awaiting ratification of this finding and direction before any further code change. If desired, I can run
Jazz/Default to complete the three-preset table first.

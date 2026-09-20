# cc_anchor_redesign_dossier.md — ANCHOR redesign: which LAYER owns embellishment discrimination

**READ-ONLY investigation. HEAD = `dd418ecfed` (unchanged). No code/behavior change.**
The §0 revert of `src/composing/analysis/region/regionanalyzer.cpp` was applied; the 3 held B2 files
(`section/localmodulationdetector.cpp`/`.h`, `tools/batch_analyze.cpp`) and pre-existing held docs are
untouched. The revert affected `regionanalyzer.cpp` only.

---

## DECISIVE VERDICT (read this first)

**None of A, B, or C is the proper-layer fix, and D's genuine benefit is ~2 cases against ~11 oracle-root
degradations. Recommendation: ABANDON the "re-derive the merged region from the final tone union" direction
entirely. The proper layer for embellishment discrimination is the one production already uses — fine
SEGMENTATION + inherit-the-embellishment-free-slice on merge — and it is working.** The residual defect the
anchor targets (an inherited slice that is itself an *incomplete / under-segmented* misread) is **narrow
(genuinely 2 of 25 cases here)** and is the *mechanical opposite* of the embellishment over-read, so a single
union-recompute cannot serve both. Pursue those 2 cases (if at all) as **per-case segmentation/scoring**
investigations, not a region-orchestration recompute.

A second, independent finding fell out of the data and matters for any future attempt: **the BIR
(bass-is-root) case-identity gate is a misleading proxy for oracle-root movement.** It scored **5 of the
anchor's 14 "fixes" as improvements when they are in fact oracle-root *regressions*** (the recompute happened to
make a *wrong* root equal the bass). Any redesign must be judged against an **oracle-root** metric, not BIR
alone.

---

## §2A — Temporal context (architecture / region-layer). VERDICT: ruled OUT.

**The decisive sub-question — within-vertical vs segmentation — is answered at source: production discriminates
embellishments by SEGMENTATION, not by a within-vertical temporal signal.** Three source facts, all in
`regionanalyzer.cpp` / `chordanalyzer.cpp` at HEAD:

1. **The merge helpers inherit an embellishment-free slice; they never re-derive identity from the union.**
   - `coalesceShortSameRootRuns` (`regionanalyzer.cpp:62-72`): *"The combined region inherits the chord
     identity of the **longest sub-region** (the Cm variants dominate over the Csus2 / C7 **passing-tone
     misreads**)."* The Csus2/C7 readings are real — they are what `analyzeChord` returns **for those slices in
     isolation** — and the design deliberately discards them by inheriting the longest sibling.
   - `absorbShortRegions` (`:188-212`): short embellishment slices *"analyzed in isolation produce exotic
     readings (sus / add11 / non-root-bass dim)"*; they are absorbed by **endTick extension only — no tone
     merge, no re-analysis**. The host identity is untouched.
   - `tryCollapseSameChordRegion` (`:166-186`): merges **only when root AND quality already match**; identity is
     kept, bass restamped. It never re-scores the union.

   So embellishment discrimination is a **segmentation-level** operation: an embellishment lives in its own
   short slice and is removed by *inheriting a different slice's identity*. **A flattened merged region cannot
   be rescued by temporal context** — the discrimination was never a within-vertical decision to begin with.

2. **Extension/sus/add promotion is CONTEXT-BLIND.** `detectExtensions(...)`
   (`chordanalyzer.cpp:217`) takes `(pcWeight, rootPc, quality, tpcForPc, rootTpc, extThreshold)` — **no
   `ChordTemporalContext` parameter**. Whether a PC becomes a `sus`/`add9`/`13` is a pure weight-threshold +
   spelling test. Passing a non-null context to the union recompute **cannot change a single extension flag.**

3. **What temporal context *does* feed is root/inversion ranking, not embellishment filtering.** The five
   progression signals that read context (`rootContinuityBonus`, `resolutionBonus`, and the four inversion
   bonuses) were migrated to the competition pipeline (`chordanalyzer.h:380-439`) and select among **root/bass
   candidates**. They can dampen a *root flip* but are powerless over a same-root extension over-read.

**Can a valid context be constructed for a merged region?** Yes — `ChordTemporalContext` is buildable from
neighbor regions (prev/next root, bass, stepwise flags; `advanceTemporalContext` already does this per region).
But it would only re-rank roots. Tested against the actual 25 cases (§2C), root-anchoring via
`rootContinuityBonus` is **double-edged**: it might suppress some root-flip regressions (bwv40.8 G→Bb,
bwv431 D→F) but would *equally* suppress the **2 genuine fixes** (bwv14.5, bwv416), which *require* a root flip
away from the predecessor — and it touches **none** of the same-root extension over-reads. Not a discriminator.

> **§2A conclusion:** Temporal context is implicated only in the sense the report noted (the recompute drops
> root continuity), but it is **not** where embellishment discrimination lives and **cannot** express it.
> Candidate A is **ruled out** as the proper layer.

---

## §2B — Duration / metric weighting (data-representation). VERDICT: already in-layer; insufficient.

- **`ChordAnalysisTone` carries duration/metric weight** (`chordanalyzer.h:88-117`): `weight` ("duration ×
  metric weight, normalised to [0,1]"), plus `durationInRegion`, `distinctMetricPositions`,
  `simultaneousVoiceCount`.
- **`analyzeChord` already weights tones by it.** The pitch-class histogram is duration-weighted:
  `pcWeight[pc] += std::max(0.1, t.weight)` (`chordanalyzer.cpp:975-986`), and every extension/sus threshold
  (`extensionThreshold` 0.20, `kSeventhThreshold` 0.12, `kSus4StructuralFourthThreshold`) is an **absolute**
  comparison against that duration-weighted mass. A short passing tone (low duration ⇒ low weight) is already
  suppressed.
- **`mergeChordAnalysisTones` PRESERVES per-tone duration** (`chordanalyzer.h:138-173`): on a merge it **sums**
  `weight` and `durationInRegion`, sums `distinctMetricPositions`, maxes `simultaneousVoiceCount`. It does **not**
  collapse to presence.
- **The recompute did NOT lose duration information.** The experiment's `pcPresenceMask` was only the *adoption
  trigger* (`preMask != postMask` ⇒ "the union introduced a new PC"); the actual analysis call was
  `analyzeChord(region.tones, …)` on the **full duration-weighted union** (report §1). So the oracle saw all the
  duration it needed.

**Why the over-read happened anyway:** the offending PCs are **long** non-chord tones — a half-note suspension,
a sustained anticipation — whose duration-weight genuinely **exceeds** `extensionThreshold`. Duration weighting
*cannot* separate a long suspension (non-chord by *function*) from a genuine added tone (chord by function):
both have high duration. That is a **functional / voice-leading** distinction, not a weight magnitude.

> **§2B conclusion:** Duration weighting is already present, already preserved by the merge, and is **not the
> missing piece**. A *stricter* duration/metric filter (drop tones below X% of region duration before analysis)
> would be **new** discrimination logic that also drops genuine short chord tones — that is Candidate D, not an
> in-layer data fix. Candidate B as stated is **insufficient**.

---

## §2C — Adopt-only-if-stronger (region-layer policy). VERDICT: premise FALSIFIED; does not separate.

**Method.** The §2C task asks to classify the 14 REMOVED (report's "fixes") vs 11 NEW (regressions) by identity
delta. I reconstructed both readings read-only from the on-disk per-preset corpora (no build):
- **ANCHOR** reading = `tools/corpus/baroque/*.ours.json` — confirmed to be the *anchor* binary's output
  (`bwv40.8@20160 = Bbsus/G`, `bwv431@480 = Fsus/D`, matching report §4).
- **HEAD** reading = `tools/corpus/baroque_kma_abs/*.ours.json` — generated at `a03c2493bb`, which is **2 commits
  behind HEAD, both intervening commits (`8bc1441076`, `dd418ecfed`) labeled byte-identical refactors** ⇒
  byte-identical chord output to HEAD. (Cross-checked: `bwv40.8 = Gm7` there, the HEAD reading.)
- **ORACLE** = `tools/corpus/baroque/*.music21.json` `rootPitchClass` (corroborating oracle; DCML is GT but
  music21 root is the available read-only proxy and aligns with CLAUDE.md's gate semantics).

**Caveat (honest):** tick-level region matching does not perfectly reproduce `characterise_bir_false`'s
genuine-candidate + batch-region-granularity accounting (e.g. bwv60.5@30960 and bwv245.17@4800 read BIR-equal in
both dirs at the raw-region level), so the *exact* removed/new membership has minor slop. The **chord-label
deltas below — the actual §2C deliverable — are accurate**; only the mapping to the gate's integer bookkeeping
is approximate.

### 25-case table (HEAD → ANCHOR, with oracle-root direction)

**REMOVED (report: "fixes"):**

| case | HEAD | ANCHOR | Δ type | oracle root | direction vs oracle |
|---|---|---|---|---|---|
| bwv10.7@36000 | Bb/C (Maj) | Cmadd9 (Min) | ROOT+QUAL | G | neither |
| bwv102.7@17520 | EbMaj7/Ab | AbMaj9 | ROOT | Eb | **ANCH AWAY (regress)** |
| bwv14.5@8160 | Gm/Bb | Bbadd9 | ROOT+QUAL | Bb | **ANCH→oracle (FIX)** |
| bwv227.7@18120 | GMaj7/E | Em13 | ROOT+QUAL | G | **ANCH AWAY (regress)** |
| bwv245.17@4800 | F/D | FMaj7add13/D | same-root +ext | F | both match |
| bwv261@33840 | C#m/E | F#7/E | ROOT+QUAL | C# | **ANCH AWAY (regress)** |
| bwv320@31680 | D7/A | Am6 | ROOT+QUAL | F# | neither |
| bwv352@1440 | Am6/E | E+ | ROOT+QUAL | F# | neither |
| bwv358@6000 | E11/G# | G#dim7 | ROOT+QUAL | E | **ANCH AWAY (regress)** |
| bwv381@4800 | G6/F# | GMaj7add13 | same-root +ext | E | neither |
| bwv416@10080 | E7b9/G# | G#dim7 | ROOT+QUAL | Ab | **ANCH→oracle (FIX)** |
| bwv429@24240 | E/G# | E7 | same-root +ext (b7) | E | both match |
| bwv432@5520 | Am/E | EMaj7#5 | ROOT+QUAL | A | **ANCH AWAY (regress)** |
| bwv60.5@30960 | F#m | F#m13 | same-root +ext | F# | both match |

**NEW (report: "regressions"):**

| case | HEAD | ANCHOR | Δ type | oracle root | direction vs oracle |
|---|---|---|---|---|---|
| bwv166.6@16080 | Eb/C | EbMaj7add13/C | same-root +ext | G | neither |
| bwv2.6@13440 | Bb+/C | D7#5/C | ROOT (aug→aug) | Bb | **ANCH AWAY (regress)** |
| bwv244.10@2400 | Ab/F | Ab6/F | same-root +ext | C# | neither |
| bwv272@9600 | G7b9/F | Ddim7/F | ROOT+QUAL | G | **ANCH AWAY (regress)** |
| bwv301@1440 | G/A | Bm7/A | ROOT+QUAL | Ab | neither |
| bwv320@23040 | Em7b5/F | Gm13/F | ROOT+QUAL | E | **ANCH AWAY (regress)** |
| bwv363@3840 | C7/Bb | F#7b9/Bb | ROOT | Bb | neither |
| bwv397@5280 | Bb/D | Bb/D | **no change** | Bb | both match |
| bwv40.8@20160 | Gm7 | Bbsus/G | ROOT+QUAL (→sus) | G | **ANCH AWAY (regress)** |
| bwv431@480 | Dm7 | Fsus/D | ROOT+QUAL (→sus) | D | **ANCH AWAY (regress)** |
| bwv64.8@16320 | D+/E | F#7#5/E | ROOT (aug→aug) | D | **ANCH AWAY (regress)** |

### Two reasons Candidate C fails

**1. The Δ-type split is not clean.** Root/quality changes and same-root extensions appear in **both** buckets:

|  | ROOT or QUAL changed | same-root +ext only | no change |
|---|---|---|---|
| REMOVED (14) | 10 | 4 | 0 |
| NEW (11) | 8 | 2 | 1 |

C's rule "adopt root/quality changes, reject same-root sus/add" would therefore **adopt 8 of the 11
regressions** and **reject 4 of the 14 fixes** — the rule has no separating power. Refining it to "reject
`Suspended` quality + reject same-root added 6/9/11/13" catches the clearest over-reads (the two `sus`
flips bwv40.8/bwv431; the add cases bwv166.6/bwv244.10/bwv245.17/bwv381/bwv429/bwv60.5) but still adopts the
**six non-sus root-change regressions** (bwv2.6, bwv272, bwv301, bwv320@23040, bwv363, bwv64.8) and still
*rejects* the genuine same-root-extension-adjacent material.

**2. Δ-type is ORTHOGONAL to oracle-correctness — and the BIR "fix/regression" labels are themselves
unreliable.** Scoring the *oracle root* (the real north star) instead of BIR:
- The 14 "REMOVED/fixes" are **2 genuine oracle fixes** (bwv14.5, bwv416 — *both* ROOT+QUAL changes that C
  would adopt), **5 oracle regressions mislabeled as fixes** (bwv102.7, bwv227.7, bwv261, bwv358, bwv432), 3
  already-correct roots, 4 neither.
- The 11 "NEW/regressions" are **0 oracle fixes**, **6 confirmed oracle regressions**, rest neutral/neither.
- Net oracle-root movement of the recompute: **≈2 toward, ≈11 away.** Decisively negative.

The signal that distinguishes a genuine fix from a degradation is **oracle-root correctness**, which is *not*
encoded on the root-change-vs-extension axis C operates on. So no region-layer adopt-policy keyed on identity
delta can separate them.

> **§2C conclusion:** Candidate C's premise (clean fixes=root/quality, regressions=sus/add) is **false in the
> data**. C **does not separate** fixes from regressions and would, even refined, net-degrade the oracle root.
> Candidate C is **ruled out** as a sufficient region-layer fix.

---

## §2D — New scoring-layer discriminator. VERDICT: not the answer either; the premise is the problem.

D would be a duration-weighted non-chord-tone filter (drop the long suspension before analysis) or a
function/voice-leading-aware extension guard — genuine scoring logic under the CLAUDE.md scoring-doc rules
(`docs/scoring_model.md` sync; BIR gate on Baroque **and** Jazz before commit). It *could* address the **same-root
sus/add over-reads** (a small subset: bwv40.8, bwv431, bwv166.6, bwv244.10, bwv245.17, bwv381, …). But it
**cannot** address the **majority** of the damage, which is *root-flip* regressions (bwv2.6, bwv272, bwv301,
bwv320@23040, bwv363, bwv64.8, plus the 5 mislabeled "fixes") where the union's extra PCs flip the *root*
selection, not an extension flag. Those flips are caused by **feeding the raw union to the scorer at all** — the
very operation the redesign was meant to introduce. D would be patching damage that only exists *because* of the
recompute.

Crucially, the two genuine fixes (bwv416 `E7b9/G#`→`G#dim7`, bwv14.5 `Gm/Bb`→`Bbadd9`) are cases where
segmentation **split a real chord across slices** and the union **re-completed** it. Completing an
under-segmented chord and over-reading an embellishment are **the same operation** — both add the union's extra
PCs — with **opposite** correctness. No filter applied to the union can tell them apart, because the difference
lives upstream, in *why the segmentation split that span*.

> **§2D conclusion:** D is genuinely required *only if* one insists on keeping the union-recompute — and even
> then it fixes only the minority sus/add subset while leaving the root-flip majority. It is **not** a clean
> path. The correct response is to not introduce the union-recompute.

---

## Recommended redesign (for ratification)

1. **Abandon** the "re-derive merged region identity from the raw tone union" direction. The guard + bounded-settle
   machinery is sound and recoverable (`cc_anchor_recompute_report.md` §3), but its **input is architecturally
   wrong**: production's fine-segmentation + inherit-embellishment-free-slice **is** the embellishment-discrimination
   layer, and it out-performs the union-recompute on the oracle root (HEAD wins ~11 of the ~13 differing cases).
2. **Re-scope the residual defect to its true size.** The genuine target is "an inherited slice that is itself an
   *incomplete / under-segmented* misread" — **2 of 25 here** (bwv14.5, bwv416), both *chord-completion* cases, not
   embellishment cases. This is a **SEGMENTATION/SCORING** question (why did segmentation split a dim7 / a III
   chord; why did the surviving slice read the incomplete shell), to be investigated **per-case** at those layers —
   not a blanket region recompute. It is the *opposite* mechanism from the over-read and must not be conflated with
   it.
3. **Fix the metric before any retry.** The BIR case-identity gate mis-scored 5 oracle regressions as fixes.
   Any future attempt must be judged on an **oracle-root** metric (music21/DCML root agreement) **in addition to**
   the BIR gate, or it will be steered by a proxy that rewards making a *wrong* root equal the bass. (This aligns
   with the granularity/precision-metric work already flagged for Stage 5 in CLAUDE.md.)

**Layer of the recommended action:** *not* the region-orchestration layer (no A/B/C recompute). The only genuine
residual lives at the **segmentation + scoring** layers and is a **2-case, per-case** investigation — pursued, if
at all, under the scoring-doc rules with the dual (oracle-root + BIR) guardrail. The user ratifies direction
before any implementation.

---

## Stop-condition status (§4)
- No code/behavior change beyond the §0 revert. ✔ (HEAD `dd418ecfed`; working tree = revert + pre-existing held files only.)
- The §0 revert touched `regionanalyzer.cpp` only. ✔
- Candidates resolved from source + read-only corpus data. ✔ — with the one explicit caveat that the
  removed/new **integer** bookkeeping (not the chord-label deltas) is an approximate reconstruction of
  `characterise_bir_false`, because no build was run.
- No candidate implemented. ✔

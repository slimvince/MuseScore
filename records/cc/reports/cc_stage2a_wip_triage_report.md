# CC Stage-2a — Preserved-WIP hunk-by-hunk triage (READ-ONLY classification)

> **Scope discipline.** This is **classification only**. Nothing in the §1 set was applied, reverted,
> committed, or dropped. The stash `bc4fa79c4a… ("foundation WIP — preserved for Stage-2 hunk-by-hunk
> triage", `stash@{0}`)` is **intact**; the working tree is clean (only the §0.1 `CLAUDE.md` commit
> exists). Disposition is Stage 2b, gated on Cowork + user review of this report.

Date: 2026-06-25. HEAD before this stage: `b57dbfa7a8`. Every classification cites
`foundation_wip/<file>.patch` line ranges so Cowork can verify at source.

---

## §0 — The two protected steps (done)

### §0.1 — CLAUDE.md gate-table correction committed (local-only)

Commit **`1fb168f56e`** (parent `b57dbfa7a8`, on `master`, **unpushed**):
`docs: correct BIR gate tables to the ratified 53/24/53 (post-L3-wiring delta; the 57/23/57 tables were stale)`

`git show --stat 1fb168f56e` lists **only `CLAUDE.md`** (1 file, 30 insertions, 24 deletions) — confirmed.
The diff is exactly the 57/23/57 → 53/24/53 table correction + the `57/23`→`53/24` granularity-caveat line.
`upstream` untargeted; `origin` held (not pushed).

### §0.2 — Exact Default-53 BIR case set re-emitted (read-only) + verified

Re-ran `python tools/characterise_bir_false.py --corpus-dir tools/corpus/default` (manifest OK:
preset=Default, 353/353, git `b57dbfa7a8`, music21 9.9.1). Result: **53 genuine BIR=false cases.**

Full Default-53 set (stem@tick), sorted:

```
bwv10.7@36000, bwv14.5@8160, bwv144.6@15360, bwv144.6@16320, bwv151.5@13440, bwv153.1@18240,
bwv16.6@16800, bwv169.7@24960, bwv17.7@46080, bwv174.5@6240, bwv20.11@13440, bwv227.7@18000,
bwv244.32@5760, bwv244.46@960, bwv245.15@13920, bwv245.17@4800, bwv245.3@12480, bwv245.37@13920,
bwv245.40@51360, bwv258@10560, bwv261@33840, bwv269@20640, bwv272@4320, bwv272@4800, bwv272@8160,
bwv282@9120, bwv289@20160, bwv289@21600, bwv300@13440, bwv309@8640, bwv320@31680, bwv334@5280,
bwv334@6720, bwv342@25440, bwv358@6000, bwv364@2880, bwv387@10560, bwv392@14400, bwv40.3@2400,
bwv402@22080, bwv416@10080, bwv421@2880, bwv422@23040, bwv423@28320, bwv429@24240, bwv432@5520,
bwv45.7@20160, bwv48.3@2880, bwv57.8@15360, bwv64.8@5280, bwv77.6@22080, bwv94.8@24960, bwv96.6@13440
```

**Cross-check vs the CLAUDE.md-claimed Default set (programmatic `comm`):** Default-53 = Baroque-53
with **`{bwv352@1440, bwv60.5@30960}` removed** and **`{bwv227.7@18000, bwv387@10560}` added** — and
the other 51 identical to Baroque-53. This matches the committed CLAUDE.md Default description
**exactly**. → The CLAUDE.md ⚠-caveat ("re-confirm the exact Default set at the next corpus regen")
is now **resolved**: the set is re-measurement-verified. (Cowork may drop the ⚠ in a future doc pass.)

---

## §1 method note — what's in scope

Triaged the Stage-0 "leave-in-stash" set only (the 16 in-scope `foundation_wip/*.patch` files). The
six **Cowork already-recovered docs** (`COWORK_HANDOFF.md`, `cowork_design_doc_template.md`,
`cowork_layer{1,2,3}_*.md`, `cowork_target_architecture.md`) are **out of scope** and were not opened.

Anchored every "superseded?" call against (1) **committed HEAD** (grep of `src`+`tools`), (2) the
**layered specs** (`cowork_layer3_keymode_design`, `cowork_layer4_chordsymbol_design` SIGNED 2026-06-24
+ `cowork_layer4_spec_review`), and (3) the **stabilization plan** (`cowork_l1l3_stabilization_plan.md`),
plus the gitignored measurement reports that already recorded each WIP stream's verdict
(`cc_layer4_build_b_fairkey_report.md`, `cc_layer3_tpc_keymeasure_report.md`,
`cc_b2_subdominant_guard_report.md`).

**Three WIP work-streams account for all the code/tooling hunks:**

| Stream | Files | Anchor verdict |
|---|---|---|
| **TPC** (spelling-aware key-fit, `tpcKeyFitWeight` / `--tpc-measure`) | keymodesequence.{cpp,h}, keymodeanalyzer.h, regiontoneprimitives.cpp, cc_layer3_keymode_baseline.py | **Pre-decided DISCARD** (§2). tpc measured **marginal** (+0.5/+0.6 pts, `cc_layer3_tpc_keymeasure_report.md:16-27`); stabilization plan **Phase 4b builds the shared spelling view fresh** — "lands now so it is never retrofitted" (`cowork_l1l3_stabilization_plan.md:66-71`). |
| **Fair-key** (Layer-3 per-slice key → Layer-4 chord decoder, `--decode-chords-l3key`) | chordslicedecoder.{cpp,h}, batch_analyze.cpp (the decode hunks) | **DISCARD.** Held/uncommitted diagnostic; **verdict REJECTED** — the real L3 per-slice key recovers "+0.04 (Baroque) / −0.01 (Jazz) ≈ 0% of the gap … wiring the L3 key into the chord layer will not, by itself, improve chord-root" (`cc_layer4_build_b_fairkey_report.md:9-14,111-113`). Not in any forward plan; the SIGNED L4 spec is "not yet rebuilt" and decides its own key-feed mechanism. |
| **B2 subdominant guard** | localmodulationdetector.{cpp,h}, batch_analyze.cpp (the modulation-JSON hunks) | **DISCARD.** Measured **REJECTED** — "DOES NOT TRANSFER. 0 of 3 cleared" → "**no commit**" (`cc_b2_subdominant_guard_report.md:14-31,209`). Production byte-identical (suppression gated on dormant `jointKeyWiringEnabled()`). The real blocker is the upstream cadence anchor, not this guard. |

The doc patches and `compare_rn.py` are independent of these three streams (triaged individually below).

---

## §3 — Load-bearing check (the hidden-dependency hunt) — **CLEAR**

The Stage-0 build break was a *committed* consumer (`--seq-tpc-weight`) depending on an *uncommitted*
member, already backed out at `b57dbfa7a8`. **No remaining in-scope WIP hunk is depended on by committed
HEAD.** Verified by grep over `src`+`tools`:

- `subdominantOfAnchor`, `dominantSeventhPresent`, `targetFlat7Present`, `tpcKeyFitWeight`,
  `tpcKeyFitForSignature`, the per-slice `ChordSliceDecoder::decode` overload, `--decode-chords-l3key`,
  `--tpc-measure`, `--partial-key-breakdown` → **0 references on committed HEAD** (each symbol exists
  only inside its own WIP patch).
- Working tree is **clean** post-§0.1 (the WIP lives only in the stash), so HEAD builds independently of
  all of it. **Discarding any of these hunks cannot break the build or any committed test.**

**One dependency in the *safe* direction (noted, not a flag):** `localmodulationdetector.cpp` WIP
forward-declares and *calls* `jointKeyWiringEnabled()`, which **is** defined on HEAD
(`jointkeydecision.cpp:145`, decl `jointkeydecision.h:215`, already used by `sectionanalyzer.cpp:94` and
`regionanalyzer.cpp:1259`). That's WIP→HEAD (fine). Discarding the B2 WIP simply removes the new call;
the HEAD symbol and its existing live callers are untouched. So the B2 discard is fully self-contained.

> **Conclusion: no half-committed dependency remains. Nothing in the §1 set is load-bearing for HEAD.**

---

## §1/§2 — Per-file, per-hunk classification

### A. CODE — `src/composing/…`

#### A1. `chordslicedecoder.h` — **DISCARD** (fair-key) — 2 hunks

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.h:5–11` (`@@ -82`) | add `#include <utility>` | L4 | support `std::pair` in the new overload | yes — supports a discarded API | DISCARD | only needed by the fair-key overload below |
| `.h:13–34` (`@@ -280`) | new public `decode()` overload taking `perSliceKey` (`vector<{fifths,mode}>`); doc says decode-only, constant-vector reproduces scalar byte-for-byte, used only by `--decode-chords-l3key` | L4 | API seam for the fair-key per-slice key feed | yes — sole consumer is the rejected fair-key diagnostic; SIGNED L4 spec (not yet rebuilt) decides its own key-feed | DISCARD | clean byte-identical extension, but its only purpose (fair-key measurement) returned a **null verdict**; not in any forward plan |

#### A2. `chordslicedecoder.cpp` — **DISCARD** (fair-key) — 5 hunks

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.cpp:5–17` (`@@ -482`) | `using SliceKeyPrior = std::pair<int,KeySigMode>` + explanatory comment | L4 | per-slice prior type | yes | DISCARD | scaffolding for the fair-key feed |
| `.cpp:22–41` (`@@ -489`) | `decodeWindowed` signature `keyFifths,keyMode` → `keyBySlice` vector; add `keyBySlice.size()!=T` guard | L4 | thread per-slice key through the driver | yes | DISCARD | only reason to vectorize the key is the fair-key feed |
| `.cpp:43–68` | `keyAt` lambda; pass `keyAt(t)` into `buildSliceWork` in both the membership-off and windowed passes | L4 | apply per-slice key at scoring | yes | DISCARD | same |
| `.cpp:69–94` (`@@ -569`) | scalar `decode()` builds a constant `keyBySlice`; new per-slice `decode()` overload body | L4 | back-compat shim + the new overload | yes | DISCARD | constant path is byte-identical to today; the overload is the discarded feature |
| `.cpp:96–109` (`@@ -583`) | `redecodeRange` builds a constant `keyBySlice` | L4 | back-compat shim | yes | DISCARD | mechanical adaptation to the vectorized signature |

#### A3. `keymodesequence.h` — **DISCARD** (tpc, pre-decided) — 1 hunk

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.h:5–28` (`@@ -124`) | add `double tpcKeyFitWeight = 0.0` to `KeyModeSequencePreferences` + long doc-comment (decode-only spelling-aware key-fit; 0 = byte-identical) | L3 | optional spelling signal in the key emission | yes — Phase 4b rebuilds the shared spelling view fresh | DISCARD | pre-decided tpc half-feature; `cowork_l1l3_stabilization_plan.md:66-71` |

#### A4. `keymodesequence.cpp` — **DISCARD** (tpc, pre-decided) — 4 hunks

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.cpp:5–15` (`@@ -28`) | add `<unordered_map>`, `<utility>`, `engraving/dom/pitchspelling.h` (Tpc::TPC_C) | L3 | support tpc key-fit | yes | DISCARD | tpc support includes |
| `.cpp:17–53` (`@@ -102`) | new `tpcKeyFitForSignature()` — line-of-fifths diatonic-window penalty | L3 | spelling-aware key-fit score | yes | DISCARD | Phase-4b rebuild |
| `.cpp:58–66` (`@@ -138`) | `useTpc = (tpcKeyFitWeight != 0.0)` flag | L3 | gate the tpc path | yes | DISCARD | tpc gate |
| `.cpp:70–117` (`@@ -149`) | branch in `buildLattice`: when `useTpc`, add `tpcKeyFitWeight × fit` to emission, cache fit per signature, re-rank top-K | L3 | apply tpc reweight | yes | DISCARD | the tpc emission reweight itself (marginal verdict) |

#### A5. `keymodeanalyzer.h` — **DISCARD** (tpc, pre-decided) — 1 hunk

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.h:5–15` (`@@ -497`) | add `int tpc = -1` to `PitchContext` (read only by the decode-only tpc key-fit) | L1/L3 | carry spelling into the key emission | yes | DISCARD | inert at HEAD (default −1, no committed reader); part of tpc; Phase-4b builds the shared spelling view |

#### A6. `regiontoneprimitives.cpp` — **DISCARD** (tpc, pre-decided) — 1 hunk

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.cpp:5–12` (`@@ -268`) | populate `p.tpc = ne->tpc` in `pitchContextOverSpan` | L1 | feed spelling to the tpc key-fit | yes | DISCARD | the population side of the tpc field; Phase-4b rebuild |

#### A7. `localmodulationdetector.h` — **DISCARD** (B2, rejected) — 1 hunk

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.h:5–43` (`@@ -82`) | add 3 `LocalKeySpan` fields: `subdominantOfAnchor`, `dominantSeventhPresent`, `targetFlat7Present` (B2 guard decision/diagnostic fields) | L4/section | drive + measure the subdominant guard | yes — guard measured & **rejected** ("no commit") | DISCARD | `cc_b2_subdominant_guard_report.md:209`; the §3.5 dominant-7th refinement was itself measured & rejected (doesn't separate genuine V7→I from tonicized IV) |

#### A8. `localmodulationdetector.cpp` — **DISCARD** (B2, rejected) — 6 hunks

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.cpp:5–20` (`@@ -26`) | add `<map>`; forward-declare `bool jointKeyWiringEnabled()` | L4/section | reach the dormant wiring flag without a header back-edge | yes | DISCARD | scaffolding for the rejected guard (dependency direction is safe — see §3) |
| `.cpp:22–36` (`@@ -47`) | `constexpr double kSubdominantGuardAnchorConfidenceFloor = 0.5` | L4/section | confident-anchor gate | yes | DISCARD | guard threshold |
| `.cpp:41–52` (`@@ -108`) | build `regionMaskByStartTick` lookup | L4/section | read dominant-region pitch mask for the V7 refinement | yes | DISCARD | feeds the rejected refinement |
| `.cpp:57–69` (`@@ -177`) | per-run dominant-7th / target-flat-7 marker accumulators | L4/section | the V7 refinement markers | yes | DISCARD | rejected refinement |
| `.cpp:73–87` (`@@ -184`) | detect `dominantSeventhPc`/`targetFlat7Pc` in each confirming cadence's dominant region | L4/section | populate the markers | yes | DISCARD | rejected refinement |
| `.cpp:89–130` (`@@ -199`) | populate the 3 decision fields; `guardSuppresses = jointKeyWiringEnabled() && subdominantOfAnchor && confidence≥floor`; skip `push_back` when suppressing | L4/section | the guard itself (dormant) | yes | DISCARD | the rejected guard; production byte-identical because suppression is gated on the dormant flag |

#### A9. `tools/batch_analyze.cpp` — **DISCARD** (B2 + fair-key) — ~11 hunks

> **No tpc remnant** in this patch (the `--seq-tpc-weight` consumer was already backed out at `b57dbfa7a8`; verified absent here). Two clusters, both DISCARD:

| hunk (patch lines) | what | cluster | layer | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.cpp:5–14` (`@@ -1028`) | emit `anchorConfidence` in `writeModulationJson` | B2 | tooling | yes | DISCARD | diagnostic for the rejected guard |
| `.cpp:16–28` (`@@ -1040`) | emit `subdominantOfAnchor`/`dominantSeventhPresent`/`targetFlat7Present` span fields | B2 | tooling | yes | DISCARD | same |
| `.cpp:29–41` (`@@ -1773`) | `printHelp` text for `--decode-chords-l3key` | fair-key | tooling | yes | DISCARD | help for the rejected diagnostic |
| `.cpp:42–87` (`@@ -2250`) | `runChordDecode` gains `useL3Key,keyPrefs,declaredMode,seqPrefs`; builds `perSliceKey`; runs the L3 `KeyModeSequenceDecoder` to fill per-slice key | fair-key | tooling | yes | DISCARD | the fair-key feed driver (null verdict) |
| `.cpp:89–107` (`@@ -2270`) | `symbolFor` takes `sliceFifths` (per-slice spelling) | fair-key | tooling | yes | DISCARD | fair-key spelling |
| `.cpp:110–118` (`@@ -2287`) | emit `l3KeyFeed`/`l3KeyedSlices` | fair-key | tooling | yes | DISCARD | fair-key diagnostic output |
| `.cpp:119–135` (`@@ -2315`) | per-region `sliceFifths`/`sliceMode`/`regionKeyStr` | fair-key | tooling | yes | DISCARD | fair-key per-region key |
| `.cpp:138–146` (`@@ -2333`) | region `"key"` = `regionKeyStr` (was the single key) | fair-key | tooling | yes | DISCARD | fair-key |
| `.cpp:148–156` (`@@ -2363`) | alternates `symbolFor(alt, sliceFifths)` | fair-key | tooling | yes | DISCARD | fair-key |
| `.cpp:157–177` (`@@ -2418`,`@@ -2473`) | `decodeChordsL3Key` flag decl + `--decode-chords-l3key` arg parse (implies `--decode-chords`) | fair-key | tooling | yes | DISCARD | fair-key flag |
| `.cpp:178–207` (`@@ -2778`) | extract notated `declaredMode`; pass it + `keyPrefs`/`seqPrefs` to `runChordDecode` | fair-key | tooling | yes | DISCARD | fair-key plumbing |

### B. TOOLING — Python

#### B1. `tools/cc_layer3_keymode_baseline.py` — **DISCARD** (tpc, pre-decided) — 2 hunks

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.py:5–160` (`@@ -1563`) | `TpcStats` + `tpc_grade_corpus` + `_tpc_line` + `tpc_measure_main` (grade pc baseline vs `--seq-tpc-weight W` variants, stable-vs-modulation split) | tooling | the tpc measurement harness | yes — Phase-4b rebuild | DISCARD | tpc harness; verdict already recorded in `cc_layer3_tpc_keymeasure_report.md` |
| `.py:162–187` (`@@ -1590`) | argparse `--tpc-measure`/`--variant-dir` + dispatch | tooling | CLI for the harness | yes | DISCARD | same |

#### B2. `tools/compare_rn.py` — **INVESTIGATE** (read-only metric diagnostic) — ~10 hunks

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.py:5–50` (`@@ -273`) | `partial_key_subtag()` — sub-classify a `partial`-bucket pair by reference-key framing (`local_match` / `home_vs_local` / `other` / `keyfail`) | tooling | de-mask the modulation error that root-based crediting hides in `partial` | **unclear** | INVESTIGATE | read-only, redefines no bucket; analogous to the committed `key_disagree_subtag`; value for the key-axis is plausible but it's on no ratified backlog |
| `.py:55–67` (`@@ -391`) | `PieceStats` fields `pk_local_match/pk_home_vs_local/pk_other/pk_keyfail` | tooling | accumulate the sub-split | unclear | INVESTIGATE | additive, populated unconditionally |
| `.py:70–79` (`@@ -414`) | `merge()` accumulates the pk_* fields | tooling | aggregate | unclear | INVESTIGATE | mechanical |
| `.py:81–96` (`@@ -448`) | `score_regions` populates the pk_* split | tooling | wire it in | unclear | INVESTIGATE | mechanical |
| `.py:97–129` (`@@ -806`) | `format_partial_breakdown()` renderer | tooling | report the split | unclear | INVESTIGATE | output only |
| `.py:133–146` (`@@ -840`) | argparse `--partial-key-breakdown` | tooling | CLI flag | unclear | INVESTIGATE | additive flag |
| `.py:147–186` (`@@ -867/-901/-930/-946`) | wire the flag into the 4 output modes (single / cross-corpus / ours+dir / ours+tsv) | tooling | emit the breakdown | unclear | INVESTIGATE | mechanical |

> **Why INVESTIGATE, not DISCARD:** unlike tpc/fair-key/B2, this is **not** a rejected experiment — it is
> a self-contained, read-only measurement lens that touches no production code and redefines no metric
> bucket. Its *value* is the open question: it could be a useful committed companion to the existing
> `--key-breakdown` (S1/S2) for the masked-modulation question, or it could be exploratory and redundant.
> Cowork should decide. (Note: this is the pre-existing ` M tools/compare_rn.py` the STATUS narrative
> repeatedly flags as "held WIP, unstaged.")

### C. DOCS

#### C1. `cowork_github_9444_comment_draft.md` — **KEEP** (safety guard) — 1 hunk

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.md:5–13` (`@@ -1`) | prepend a **"⛔ SUPERSEDED — DO NOT POST"** banner: the draft's import-side fix *is* patch `cfc7eb5e39`, which is **fork-local-only and must NEVER be PR'd/contributed** to `musescore/MuseScore`; posting it would be a **HARD-STOP** violation | doc | prevent a distribution-constraint violation | no | **KEEP** | the banner is unambiguously correct and **actively protective** of the CLAUDE.md ★ DISTRIBUTION CONSTRAINT; it belongs as-is while the file exists |

> **Nuance for Stage 2b:** the banner itself says the file is "slated for deletion in the prune pass."
> So the *file-level* decision (keep the banner vs prune the whole draft) is Cowork's; either way the
> banner must not be lost while the draft lives. This is the **only KEEP** in the set.

#### C2. `STATUS.md` — **INVESTIGATE** (living-doc currency) — 1 hunk

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.md:5–…` (`@@ -3,7 +3,63`) | prepend a large session-8/9 narrative (Layer-1 note-model, Layer-2 slicer, Layer-3 Increments A/B/C, the refactor phase, the layer audit, the B2 build-and-reject, the architecture-first pivot), demoting the old `2026-06-14` head entry | doc | bring the living STATUS current to 2026-06-22 | **unclear / possibly** | INVESTIGATE | committed STATUS head is `2026-06-14`; this WIP is `2026-06-22` and narrates a **pre-stash track** (Layer-3 Increment C); committed HEAD is a **fresh layered track** (`0b42096d75` "Layer 1 / Phase 1a", `48909fb752`/`5f6b9828a5` "Layer 4 / Increment A/B"). Whether to fold this history in or discard as superseded needs Cowork's architectural context |

> **Flagged tension:** I cannot reconcile the session-9 "Layer-3 Increment C" numbering against the
> committed "Layer 1 Phase 1a / Layer 4 Increment A/B" numbering without Cowork's context — this is
> exactly the "Cowork knows the greater architectural plan; CC does not" boundary. Hence INVESTIGATE.

#### C3. `BUILD_AND_TEST.md` — **INVESTIGATE** (partially superseded by §0.1) — 2 hunks

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.md:5–14` (`@@ -180`) | update `analyze_inversion_errors.py` note from "stale/pending" → "**Baroque 24/13→47/57, Jazz 35/7→81/23**; false-halves (57/23) match the gate" | doc | record the corrected-parser re-measurement | **partly** | INVESTIGATE | the **47/57 & 81/23 figures are correct** and match committed CLAUDE.md; but the embedded "**57/23** gate" reference is now superseded by the §0.1 **53/24** correction — needs a small touch-up before it could land |
| `.md:18–39` (`@@ -291`) | same correction in the `--corpus-dir` section + update the inline command-comments to `47/57` / `81/23` | doc | same | partly | INVESTIGATE | same — valid figures, stale "57/23" gate framing |

#### C4. `docs/decoder_design.md` — **INVESTIGATE** (partially superseded by §0.1) — 1 hunk

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.md:5–11` (`@@ -258`) | update the gate-rebaseline note: `analyze_inversion` "24/13 stale/pending" → "**47/57** Baroque / **81/23** Jazz (false-halves = the 57/23 gate)" | doc | same correction | partly | INVESTIGATE | same as C3 — `47/57`/`81/23` valid; "57/23 gate" now stale vs 53/24 |

#### C5. `docs/back_half_design.md` — **INVESTIGATE** (asserts an un-ratified direction) — 1 hunk

| hunk (patch lines) | what | layer | intent | superseded? | class | rationale |
|---|---|---|---|---|---|---|
| `.md:5–17` (`@@ -1`) | prepend a "**★★ SUPERSEDED-IN-DIRECTION (2026-06-15)**" banner: the back half is re-grounding onto a **CONSTRAINED JOINT INFERENCE** architecture (`docs/architecture_joint_inference.md`); the local feed-forward shape is "the wrong shape" | doc | redirect the back-half design | **unclear** | INVESTIGATE | the joint-inference direction was **deliberately held out of committed docs as un-ratified** (per the STATUS narrative: the roadmap's joint-inference block was *stripped* before commit; the ARCHITECTURE.md forward-pointer stayed *unstaged*). This banner asserts that same un-ratified supersession — consistent with the held forward-pointer pattern, but its currency vs the *current* committed layered track is a Cowork/user call |

---

## §4 — Summary

### Counts (16 files; 47 hunks total)

| Classification | Hunks | Files |
|---|---|---|
| **KEEP** | **1** | `cowork_github_9444_comment_draft.md` (1) |
| **INVESTIGATE** | **18** | `compare_rn.py` (10), `STATUS.md` (1), `BUILD_AND_TEST.md` (2), `docs/decoder_design.md` (1), `docs/back_half_design.md` (1) … *(compare_rn = 10 mechanical hunks of one diagnostic)* |
| **DISCARD** | **28** | chordslicedecoder.{cpp,h} (7), keymodesequence.{cpp,h} (5), keymodeanalyzer.h (1), regiontoneprimitives.cpp (1), localmodulationdetector.{cpp,h} (7), batch_analyze.cpp (11), cc_layer3_keymode_baseline.py (2) — *(B2 + fair-key + tpc; some files double-count clusters)* |

*(KEEP is rare, as §2 predicted. The single KEEP is a doc safety-guard, not code.)*

### The only items needing a Cowork + user decision before Stage 2b

**KEEP (1):**
- `cowork_github_9444_comment_draft.md:5–13` — the DO-NOT-POST distribution-constraint banner. Decision is
  really file-level (keep banner vs prune the whole draft); the banner must survive while the file does.

**INVESTIGATE (5 streams):**
1. `compare_rn.py` `--partial-key-breakdown` (all 10 hunks, one diagnostic) — read-only de-masking lens on
   the `partial` bucket. *Question: commit it as a companion to `--key-breakdown`, or discard as
   exploratory/redundant?*
2. `STATUS.md` session-8/9 narrative prepend — *Question: fold this pre-stash-track history into the living
   STATUS, or discard as superseded by the fresh "Layer 1 Phase 1a / Layer 4 A/B" track?* (needs Cowork's
   architectural context — the layer-numbering doesn't line up from CC's side.)
3. `BUILD_AND_TEST.md` (2 hunks) — the `analyze_inversion` 47/57 & 81/23 correction is **valid**, but its
   "57/23 gate" framing is now stale vs the §0.1 **53/24**. *Question: re-touch to 53/24 and land, or discard?*
4. `docs/decoder_design.md` (1 hunk) — same as (3).
5. `docs/back_half_design.md` (1 hunk) — the SUPERSEDED-IN-DIRECTION (constrained-joint-inference) banner.
   *Question: is that un-ratified direction still the intended supersession, given the current committed
   layered track?*

**DISCARD design-note (not a decision item, recorded for completeness):** the `chordslicedecoder` per-slice
`decode()` overload (A1/A2) is a clean, **byte-identical-by-construction** API extension whose only consumer
was the null-verdict fair-key diagnostic. Discard it now; if the fresh L4 rebuild later adopts a per-slice
key feed, this is a reasonable shape to *re-derive* (it is not, however, the ratified mechanism — the SIGNED
L4 spec is "not yet rebuilt").

### Load-bearing hunks (§3)

**None.** No in-scope WIP hunk is depended on by committed HEAD; the working tree is clean and builds
independently of the entire stash. The B2 WIP's call to `jointKeyWiringEnabled()` is a safe WIP→HEAD
dependency (the HEAD symbol stays, used by live callers). Discarding any hunk is build-safe.

---

## Constraints honored

- READ-ONLY classification beyond the two §0 protected steps (the local-only `CLAUDE.md` commit + the
  read-only Default-53 re-measure). Applied / reverted / committed / dropped **nothing** from the §1 set.
- Stash `bc4fa79c4a…` **intact** (`git stash list` still shows `stash@{0}`); no disposition performed.
- `upstream` never targeted; `origin` held; the only commit is the local `CLAUDE.md` `1fb168f56e`.
- Stopped at classification — no Stage-2b disposition begun.

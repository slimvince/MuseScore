# Structural-Integrity Audit — total-unification + layer-adherence + workaround detection (all built layers)

> **Status: read-only grounded catalogue (CC, 2026-07-07; Engage arc #6).** HEAD `5fa16b77e0`, branch
> `master`, fork-only, ahead 0. Both regression stops green (untouched — read-only). No `src/` change, no
> corpus write, no build, no fix. Every catalogued site is grounded at file + symbol + line + mechanism;
> each classified VIOLATION / OK / UNCLEAR with a severity. Every fix named here is a **later, separate,
> user-ratified refactor** — this document queues them, it does not act.
>
> **This EXTENDS the prior architecture reviews; it does not re-derive them.** Priors read and built on:
> `cowork_l1l4_architecture_audit.md` (Q1 one-path, Q6 principles), `cowork_architecture_review_2026_07.md`
> (F-1…F-18, A-1…A-10), `cowork_implementation_review.md` (2026-06-10 — partly stale; verified at current
> code), and the owed-refactor records in `cowork_stage5_fitter_design.md` (OWED #1 file-split parked to R9;
> OWED #2 §6-block dissolution at Stage-5/E4) and the roadmap ENGAGE block (E0–E5, G1–G6).
>
> **Method.** The `results` carry substrate deep-diagnosed by CC directly (consumer map, cap→append
> dissolution tested at code, concern separation, clean-target, fan-out measured read-only). Every other
> built layer swept by four parallel read-only agents (fact layers L1/L1.5/L2; key L3 + decode; L4 gates +
> region + section; L5/L6/VL + tools), each hit re-grounded. Pattern-class hunted: **(a)** limit→compensating
> workaround · **(b)** concern-coupling · **(c)** duplication/multiple-paths-per-concern · **(d)**
> workaround-on-a-mechanism · **(e)** cross-layer reach-in · **(+)** any further structural form.

---

## 0. Headline

The composing module is **structurally sound and, in the rebuilt/dormant layers, unusually clean** — the
sweep confirms progress since the priors: the section-layer-in-notation violation is **closed**
(`analyzeSection` now in `composing/section/`), the `promoteToWinner` primitive **unified** Gate A + FM2 +
the three `buildResult` wrappers, `kMasks` now **derives** from `kTemplateIntervals`, the metric scripts are
**single-owned**, and `forwardoverride` is an exemplary one-mechanism-two-consumers reuse.

The genuine structural debt clusters in **exactly one place: the legacy Layer-4 production chord path**
(`harmonicfunctionlayer.cpp` + `chordpostpasses.cpp` + its consumers). The anchor (`results` cap→append +
pedal clobber + Iter 86/91 in-place mutation) is a real cap→workaround/concern-coupling tangle — **but its
clean-target is already built in the dormant decoder**, so the load-bearing sequencing verdict is: **the
tangle folds INTO the E4 decoder engagement, not a standalone pre-L5 refactor** — while **three portable
slices of it** (a shared "best different-root alternative" primitive; the serialization/display cap-views;
the fact-layer duplication cleanups) **are** genuine pre-L5 wins because they are path-independent or needed
by both paths.

Counts: **1 deep-diagnosed anchor** + **20 swept sites**. By class: **6 VIOLATION**, **8 UNCLEAR**,
**6 OK-noted / RESOLVED**. By severity: **2 HIGH**, **9 MED**, **9 LOW**. No new HIGH found outside the
anchor and one live-path reach-in (`findTemporalContext`).

---

## 1. THE ANCHOR — the `results` carry substrate (Layer 4, legacy production path)

`std::vector<ChordAnalysisResult> results` is built in `applyHarmonicFunction`
(`function/harmonicfunctionlayer.cpp`) and threaded through the post-scoring tail
(`chord/chordpostpasses.cpp`, `chord/postscoringgates.cpp`) into the region carry. It is **one structure
serving six-plus concerns**, with a cap→workaround pair at its core.

### 1.1 The complete consumer / concern map

| # | Concern | Site | Reads / mutates |
|---|---|---|---|
| 1 | **Winner selection** | `harmonicfunctionlayer.cpp:552` `chosenResult = results.front()` | `front()` = the chosen chord |
| 2 | **The ranked carry** | → `AnalyzedRegion.alternatives` (`analyzed_section.h:78`), `HarmonicRegion.alternatives` | `results[1..]` |
| 3 | **The cap-of-3** | `harmonicfunctionlayer.cpp:521` `if (results.size() >= 3) break;` | truncates the build |
| 4 | **The diff-root "guaranteed inversion alternative" append** | `harmonicfunctionlayer.cpp:530-549` | reaches around #3 to re-add a different-root entry |
| 5 | **Iter 86 bass-b7 promotion** | `chordpostpasses.cpp:135-149` | mutates `results.front().identity.extensions` in place |
| 6 | **Iter 91 bass-as-root promotion** | `chordpostpasses.cpp:163-188` | `promoteToWinner(..., kPromoteAppendOnly, stopBelowThreshold=false)` — the same append-past-cap idiom, citing the cap explicitly (line 178) |
| 7 | **Pedal detection** | `chordpostpasses.cpp:209-281` | reads `front()` (r1), runs a whole Pass-2 re-analysis, **`results = pass2` clobbers the vector** (274), **re-implements the diff-root scan** (262-269), and **defensively disables the append** for Pass 2 (240-241) |
| 8 | **Post-scoring gate flip** | `postscoringgates.cpp` `promoteToWinner`/FM2 | moves `front()`; reads `gateCtx->rawCandidates` (the **full, uncapped** `chosenPerBass`, `harmonicfunctionlayer.cpp:570-575`) |
| 9 | **Batch serialization cap** | `tools/batch_analyze.cpp:660-661` and `:712` | two sites, both `altIdx < 3` |
| 10 | **Bridge/display view** | `src/notation/internal/notationcomposingbridge.cpp:297-304` | carries **all** alternatives uncapped + re-homes each result's `function.keyTonicPc/keyMode` |

### 1.2 The cap→append chain — dissolution hypothesis TESTED at code (CONFIRMED)

`fix_results_cap_exhaustion.md` records the origin: after the threshold fix the correct different-root chord
cleared admission, but the **cap-of-3 was routinely exhausted by same-rootPc variants** (Bb, Bb7, BbMaj7…)
before the different-root chord could enter — so a "Guaranteed inversion alternative" append was added to
scan `chosenPerBass` and re-insert the highest-scoring different-root candidate past the cap.

**The dissolution is provable from the code, not assumed.** The append (`:541-547`) only ever pulls a
candidate with `rc.score >= threshold` (guard `:543`). An **uncapped** threshold-only build (remove the
`results.size() >= 3` break at `:521-523`) pushes **all** above-threshold candidates in score order — a
strict **superset** of what the append can add. Therefore, with the cap removed, `hasDiffRoot` is
necessarily true wherever the append would have fired, and **the append becomes dead code — cap and patch
cancel**. The winner (`front()`) is unchanged (it is the top-scorer either way); only the carried
`alternatives[]` grows. (Downstream is unaffected on the decision path: the gate flip reads the uncapped
`gateCtx->rawCandidates`, not `results[]`; the pedal reads `front()`. Only the serialized carry changes ⟹ a
behavior change on `.ours.json` bytes ⟹ the robust-stop explained-diff + re-baseline discipline — i.e. a
ratified adoption, not a free edit.)

**One honest discrimination (a true cap-artifact vs a legitimate targeted promotion):** Iter 91 (#6) uses
`kPromoteAppendOnly` with `stopBelowThreshold=false` — it can pull a **below-threshold** bass-rooted target.
That reach is **not** dissolved by uncapping-at-threshold; it is a genuinely different, deliberate targeted
promotion (it wants a specific structural target regardless of score). So: the **inversion-append (#4) is a
pure cap-artifact that dissolves**; Iter 91's below-threshold pull is a targeted promotion that stays. This
is exactly the VIOLATION-vs-legitimate line the audit must draw.

### 1.3 The concern separation (which concern belongs to which owner)

- **Winner** (#1) and **the ranked carry** (#2) are one legitimate structure — a decision plus its honest
  alternatives. That part is fine.
- **The cap (#3) + append (#4)** are a defect-and-patch pair on the *build*; they belong to neither the
  winner nor the carry — they are a workaround for the same-root-exhaustion the cap causes.
- **Pedal detection (#7)** is a **distinct chord-identity concern** that currently (i) **clobbers** the
  shared winner+carry vector (`results = pass2`), (ii) **re-derives** the best-different-root competitor for
  its confidence gap, and (iii) has to **defensively disable** the append because that display-carry concern
  contaminates its detection math. All three are symptoms of pedal *mutating the winning identity in place*
  rather than *reading the carry and producing a distinct pedal-annotated result*.
- **Serialization (#9)** and **display (#10)** are per-consumer projections; they currently **disagree**
  (batch truncates to 3, bridge carries all) — they should be explicit views over the one carry, not two
  independent truncations.
- **"Best different-root alternative"** is computed in **four** places (the append `:537-540`, the pedal gap
  `:262-269`, the FM2/`promoteToWinner` primitive, and the dormant decoder `chordslicedecoder.cpp:927-930`)
  — a genuine (c) duplication of one decision.

### 1.4 The clean-target design (design only — ALREADY BUILT in the dormant decoder)

The dormant L4 `ChordSliceDecoder` (`chord/chordslicedecoder.cpp:746-789`) already embodies the clean
target and does **not** reproduce the anchor's defect:
- a **governed** carry: `topK` over **distinct voicings** (dedups same-voicing, skips resolved siblings,
  `:751-763`) ∪ a **principled** incumbent-carry (the prevailing chord kept alive even below `topK` so the
  membership two-pass always has it, `:766-789`) — an intentional carry, **not** a same-root-exhaustion
  reach-around;
- the best **different**-root/inversion reading is **read FROM** the carry (`:927-930`), never forced back
  in by a compensating append;
- alternatives are **never pruned** on COMMIT/INHERIT (`decode_chord_tests.cpp:1371-1397`).

So the clean-target is: one governed carry (a single principled limit or uncapped), the different-root
alternative as a natural consequence, **pedal detection decoupled as a reader over the carry** (the decoder
has **no** pedal detection yet — a real gap the engage design must fill), and serialization + display as
separate per-consumer views. **This is why the anchor folds into E4 (§4): the decoder is the replacement,
and it already realizes most of the design.**

### 1.5 The fan-out (read-only, measured; a capped floor)

Measured across all three per-preset corpora (`tools/corpus/{baroque,jazz,default}`, 352 scores each,
~11k regions/preset). Because the internal cap is 3 **total** results (front + ≤2 alternatives), a serialized
`alternatives`-count of **3 occurs only when a diff-root/Iter-91 append pushed past the ceiling** — so the
`alts=3` rate is a direct read of **how often the cap→append workaround fires**:

| preset | alts=2 (cap ceiling) | **alts=3 (append fired)** | bass-root winners | of those carrying a diff-root alt |
|---|---|---|---|---|
| Baroque | 61.7 % | **36.2 %** | 63.3 % | 66.4 % |
| Jazz | 76.9 % | **21.5 %** | 67.3 % | 37.9 % |
| Default | 61.7 % | **36.1 %** | 63.7 % | 66.4 % |

The workaround fires on **over a third of all Baroque/Default regions** — it is load-bearing, not an edge
case. **Caveat (principle #1):** this is the *capped, serialized* distribution — a floor. The *true
untruncated* ranked-set size (above-threshold candidates before the cap) lives only in
`gateCtx->rawCandidates` and is not serialized; measuring it fully needs a `diagnoseChord`/dump instrument (a
later measured step). The 36 % at-ceiling rate is a strong lower bound on cap pressure.

### 1.6 Anchor classification

- **cap-of-3 (#3) + inversion-append (#4):** form **(a)** · **VIOLATION** · **HIGH** — a cap→workaround pair
  firing on ~36 % of regions, on the load-bearing production path.
- **the `results` vector serving winner+carry+cap+append+pedal+promotions (#1-7):** form **(b)** ·
  **VIOLATION** · **HIGH** — one structure, six concerns.
- **pedal `results = pass2` clobber + re-scan + defensive-disable (#7):** form **(b)/(e)** · **VIOLATION** ·
  **HIGH** — a detection concern mutating the winning identity in place and contaminated by a display concern.
- **"best different-root alternative" computed 4× (#4, #7, #8, decoder):** form **(c)** · **VIOLATION** ·
  **MED** — one decision, four sites; the portable pre-L5 win (§3, FQ-1).
- **serialization (#9) vs bridge (#10) cap divergence:** form **(c)** · **UNCLEAR→LOW** — two views disagree
  on the cap; make both explicit projections.

---

## 2. The catalogue — swept sites (one row per site)

Grouped by layer. Every row grounded at code. `†` = a NEW facet of an already-known item (not a
re-derivation). Sites the sweep confirmed CLEAN are listed in §2.6.

### 2.1 Fact layers — L1 notemodel · L1.5 engravingbridge · L2 slicing/harmony · scoreharvest

| # | Site — symbol | form | class | sev | mechanism (grounded) |
|---|---|---|---|---|---|
| S1 | `engravingbridge/regiontoneprimitives.cpp:451-592` — `findTemporalContext` | (e) | **VIOLATION** | **HIGH** | An L1.5 "view-only" primitive instantiates the L4 analyzer (`ChordAnalyzerFactory::create()`) and runs the full L4+L5 decision pipeline (`analyzeChord` + `applyIter8691Pedal` + `applyPostScoringGates`) **twice** to cold-analyze the previous/next chord *identity*, on the live path (`regionanalyzer.cpp:900`, `notationcomposingbridge.cpp:608`). A decision-layer computation executed inside the derived-view layer. |
| S2 | `engravingbridge/regiontoneprimitives.cpp:124-201` — `collectPitchContext` † | (c)/(e) | UNCLEAR | MED | NEW facet of the known two-pitch-context duplication: this builder does a **raw DOM walk** (`s->cr()`, `n->play()/n->visible()`) re-deriving note eligibility itself and bypassing L1, while its successor `pitchContextOverSpan` reads `model.overlapping()`. Live (`keyresolver.cpp:311`). |
| S3 | `regiontoneprimitives.cpp:280-368` & `:371-449` — `detectOnsetSubBoundaries`, `detectBassMovementSubBoundaries` † | (c)/(e) | UNCLEAR | MED | 3rd & 4th copies of the same raw-DOM eligibility+lowest-pitch-bass walk, live on Pass-2/2b (`regionanalyzer.cpp:1073,:1279`); slated to retire with the legacy segmenter — adjudicate whether to catalogue separately or fold into that retirement. |
| S4 | `harmony/harmonicsegmenter.cpp:161-325` — `collectNoteChangeTicks` † | (c) | UNCLEAR | MED | NEW facet of the two-segmenters gap: the legacy change-point collector carries **grace-skip** (`:197-199`) and **mid-tuplet snap** (`:274-317`) interpretation the pure `slicing::changePointSlices` excludes — a chord-track-emission concern riding inside change-point detection. |
| S5 | `engravingbridge/regiontonecollector.cpp:72-81` — `beatWeight` lambda | (c) | **VIOLATION** | LOW | Inlines the exact `{1.0,0.85,0.75,0.5}` BeatType→weight map that `scoreharvest::regionMetricWeightForBeatType` already owns — and this TU already includes that header. Trivial to unify. |
| S6 | `chord/chordanalyzer.cpp` tpc cluster (`tpcForPc[]:1231`, `countTpcMatches:592`, `tpcConsistencyBonus:743`) vs `engravingbridge` `lineOfFifths` † | (c) | UNCLEAR | MED | The L4 scorer keeps its own tpc reader although `engravingbridge::lineOfFifths` is declared "the SINGLE place" that interprets a tpc; the header records the fold as pending "when the decoder goes live and the legacy scorer retires" — an E4-scheduled fold, catalogued for completeness. |

### 2.2 Key layer L3 + decode

| # | Site — symbol | form | class | sev | mechanism (grounded) |
|---|---|---|---|---|---|
| S7 | `key/modepriorpresets.h:45-69` + `.cpp:34-55` — `ModePriorPreset` "Standard" | (c) | **VIOLATION** | LOW | The 21 "Standard" mode-prior magnitudes exist as three literal copies (struct initializers, explicit `standard.*=` assignments, and the `KeyModeAnalyzerPreferences` defaults), kept in sync by a **test** (`modepriorpresets_tests.cpp:106`) rather than a single source. |
| S8 | `key/keymodesequence.h:117-137` — `KeyModeSequencePreferences` cost/window constants | (c) | UNCLEAR | MED | The live decoder's `changeBaseCost/changePerFifthStep/relativePairExtraCost/decayRate/lookaheadWeight` are **copied by value** from the resolver's `hysteresisMargin`/`keySignatureDistancePenalty`/scoreharvest decay — no shared symbol, so a Stage-5 fit of either drifts them apart. |
| S9 | `region/regionanalyzer.cpp:585` & `:611` — full ranked key resolve as a segmentation seed | (d)/(b) | UNCLEAR | MED | The heavy `resolveKeyAndModeRanked` (lookahead loop + hysteresis) runs at `:585` but only `.front().{fifths,mode}` is consumed as a grid seed (the real per-region key comes from the decoder at `:615`); `resolveKeySignatureContext` is also computed twice for the same args — scored work retained "ONLY to keep the segmentation grid byte-stable (S2)". |
| S10 | `key/keymodesequence.cpp:224-226` vs `key/keymodeanalyzer.cpp:766-767` — emission-confidence sigmoid | (c) | UNCLEAR | LOW | The `1/(1+exp(-steepness*(gap-midpoint)))` sigmoid is written in two files (different `gap` inputs, "byte-for-byte" when the chosen state is the local argmax); a shared helper would remove the drift surface. |
| S11 | `region/regionanalyzer.cpp:1002-1012,:1222-1231,:1419-1428` — `ChordPathNode` construction | (c) | OK-noted | LOW | The node-build block is copy-pasted at all three commit sites feeding the (inert, ahead-of-wiring) `decoder.recordNode()`; deliberate dormant plumbing, but a genuine triplication a one-line `makeChordPathNode(...)` would remove. |

### 2.3 L4 gates + region + section (anchor excluded)

| # | Site — symbol | form | class | sev | mechanism (grounded) |
|---|---|---|---|---|---|
| S12 | `chord/chordanalyzer.cpp:990-1018` + `section/sectionanalyzer.cpp:128-157` + `:263-293` — degree + diatonic-to-key recomputation | (c) | **VIOLATION** | MED | The "derive tonicPc from fifths+mode, set `function.{degree,keyTonicPc,keyMode}`, loop every sounding pc against the scale for `diatonicToKey`" block is copy-pasted 3× (`buildChordResult`, `stabilizeHarmonicRegionsForDisplay`, `applyGapKeyContext`); only the innermost `diatonicDegreeForRootPc` is shared. |
| S13 | `chord/chordpostpasses.cpp:43-104` — `cptIsBassChordTone` | (c) | UNCLEAR | LOW | Reimplements per-quality triad-tone interval membership via a hardcoded `switch`, duplicating the `kTemplateIntervals` table's triad half (the extension half is a different, correctly-local concern). |
| S14 | `chord/postscoringgates.cpp` Gates L/G-E — quality-from-key mutation † | (b)/(e) | UNCLEAR | **HIGH** | NEW facet of the known "gates A–L are functional reasoning in the oracle": several gates additionally **mutate chord quality/root from key context** (Gate L: Augmented→Major when diatonic `:527`; Gate G-E: Minor-add6→HalfDim7 when the alt root is a diatonic function `:392`) — a quality-from-key second-guessing channel co-located with the inversion-bias gates. Dissolves at OWED #2 (§6-block, Stage-5/E4). |
| S15 | `region/regionanalyzer.cpp:984-987` vs `:1211` vs `:1408` — sparse-refinement call asymmetry | (c) | **VIOLATION** | MED | Pass-1 calls **both** `refineSparseChordQualityFromKeyContext` and `applyTonicPriorToSparseChord`; Pass-2/2b call **only the first** — a sub-divided sparse region silently gets a different quality-refinement than a top-level one. |
| S16 | `region/sparsechordrefinement.cpp:119,:168` — `refineSparseChordQualityFromKeyContext`/`applyTonicPriorToSparseChord` | (b)/(e) | UNCLEAR | MED | Both overwrite `result.identity.quality` (an L4 field) from the diatonic degree in the resolved key (an L5 concern) **after** the scorer committed — quality-from-key feedback living in the region orchestrator. |
| S17 | `section/sectionanalyzer.cpp:128-162` + `:263-294` — display-time degree recompute + 4th `refineSparse*` call | (c)/(b) | **VIOLATION** | MED | Two more copies of the S12 block, **plus** `stabilizeHarmonicRegionsForDisplay` re-runs `refineSparseChordQualityFromKeyContext` a **fourth** time at display-stabilize (`:158`), re-firing the region-commit overwrite. |
| **X** | (cross-cutting) **quality-from-key second-guessing** — ≥4 sites / 3 layers: `sparsechordrefinement` (region), `sectionanalyzer` stabilize (section), Gates L/G-E (chord), `forceChordTrackQualityFromKeyContext` (notation display) | (+) | **VIOLATION** | MED | One concern — "revise chord quality given the resolved key" — has **no single owner**; it is the structural root of S12/S15/S16/S17. Where it should live (L4 scorer as a low-confidence carry vs one post-resolution refinement) is an engage/L5 design decision. |

### 2.4 L5 (dormant) + L6 + VL + tools

| # | Site — symbol | form | class | sev | mechanism (grounded) |
|---|---|---|---|---|---|
| S18 | `function/` directory (`CMakeLists.txt:61-153`) — dir mixes L4 winner-selection + L5 units by name † | (b) | UNCLEAR | LOW | `harmonicfunctionlayer` (L4 winner selection) sits physically beside the eight L5 `function*` units and the L5/L6 `tonicizationlabeler`; **no code coupling** (clean at the include level) — the mixing is purely nominal, and the rename is already named as an engage-step item (`functionprogression.h:44-46`). |
| S19 | `function/functionresolver.cpp:460-468`, `functionoutput.h:90-98` — confidence-scale incommensurability † | (b) | UNCLEAR | MED | The known F-1 gap at concrete code: `tryOverride` compares a **bounded** `earlierConfidence=[0,1]` against an **unbounded** `contradictionStrength=bestPlaus−committedPlaus`; `FunctionConfidence.combined` is an unbounded additive. **Documented** as a Stage-5 calibration item (`:466-467`), deferred — **inherited at L5 engage** (surface before build-around, #13). |
| S20 | `tools/compare_rn.py:349,367,471` + `compare_analyses.py:229` — root-equality decision inlined | (c) | UNCLEAR | LOW | The root-agreement *decision* is a bare `root_pc == root_pc` inlined at 4 sites; the *derivation* is single-owned, so only the one-line comparison repeats — the R10-b root-agree figure rests on it; a `roots_agree(a,b)` helper would remove the drift surface. Likely not worth a change. |

### 2.5 RESOLVED / OK — confirmed progress (the audit extends the priors)

- **RESOLVED — section-layer-in-notation (was `cowork_implementation_review.md` Q1/Q2 top finding):**
  `analyzeSection` + section refinements now live in `composing/analysis/section/`; notation only *calls*
  them via documented thin pass-throughs. The old layering violation is **closed**.
- **RESOLVED — `promoteToWinner`** unified Gate A + FM2 + the three `buildResult` wrappers (arc #3b); the
  two promotion idioms are one primitive. Not re-flagged.
- **RESOLVED — `kMasks`** derives from `kTemplateIntervals` (compiler-enforced); the L1-audit Q1.3 item is
  closed.
- **OK — the dormant decoder carry** (`chordslicedecoder.cpp:746-789`): governed `topK`-on-distinct-voicings
  ∪ principled incumbent-carry, diff-root read from the carry — the anchor's clean-target, not a tangle.
- **OK — `forwardoverride`** (`function/forwardoverride.h`): one `OnePassClosure`+`overrideBar` mechanism
  reused by both the fine-grain override and the modulation recompute — exemplary #6.
- **OK — metric scripts single-owned:** `compare_analyses.py` owns alignment+classification, `dcml_parser.py`
  owns DCML rooting; `characterise_bir_false`/`analyze_inversion_errors`/`compare_rn`/`a8_rebaseline_measure`
  all **import** them and self-assert byte-identity — the de-facto metric is not duplicated.
- **OK (dormant-by-design, not rot):** `DecodeQualityLevel::Normal/Deep` inert seam; `redecodeRange`
  test-only seam; `jointkeydecision` default-OFF; `tonicizationlabeler` diagnostic-only; the `progression/`,
  `vocabulary/`, `grouping/`, `voiceleading/` dirs (swept, clean — reuse-not-duplicate discipline enforced
  in-header). `topK`/`maxAlternatives` in the key decoder are principled state-set bounds (union of per-slice
  top-K ∪ forced incumbents/pins), **not** cap→workaround pairs.

---

## 3. The prioritized fix-queue

Each entry is a later, separate, user-ratified refactor (#8's first category). Ordered by leverage.
**FQ-A / FQ-B** flags the sequencing verdict (§4): **A** = pre-L5, path-independent; **B** = folds into the
E4 engagement.

| FQ | What | Sites | class/sev | seq |
|---|---|---|---|---|
| **FQ-1** | **Unify the "best different-root alternative" scan into ONE primitive.** Extends `promoteToWinner`. Needed by BOTH the legacy path (until E4) AND the decoder — not throwaway. Byte-identical-provable per site. | anchor #4/#7/#8 + `chordslicedecoder.cpp:927-930` | (c)/MED | **A** |
| **FQ-2** | **Give quality-from-key ONE owner.** Resolve the ≥4-site/3-layer scatter (cross-cutting X + S12/S15/S16/S17); decide L4-scorer-carry vs single post-resolution refinement; the S12/S17 degree+diatonic recompute collapses to one `applyDiatonicKeyContext(...)` helper. | X, S12, S15, S16, S17 | (c)/(b)/MED | **B** (touches §6-block + L5) |
| **FQ-3** | **Relocate `findTemporalContext` out of L1.5.** The neighbour-chord-identity computation belongs to L4 / the temporal-context assembly; L1.5 exposes only the tone views. Live-path HIGH; fix is independent of the decoder internals. | S1 | (e)/HIGH | **A** (confirm not simpler at E4) |
| **FQ-4** | **The anchor cap→append + pedal clobber + Iter 86/91 in-place mutation.** The decoder's governed carry replaces the `results` substrate; the cap/append/clobber die by construction. Engage design must: (i) confirm the decoder `topK`+incumbent-union doesn't reproduce same-root exhaustion; (ii) give **pedal detection a reader-over-carry home** (decoder has none yet); (iii) route Iter 86/91 through FQ-1's primitive; (iv) re-express Iter 91's below-threshold pull as an explicit targeted promotion (it does not dissolve). | anchor #3-7 | (a)/(b)/HIGH | **B** (E4) |
| **FQ-5** | **Fact-layer duplication cleanups** (path-independent #6 wins): the beat-weight lambda (S5, trivial); the mode-prior triplication (S7); the emission-confidence sigmoid helper (S10); the `ChordPathNode` builder (S11). | S5, S7, S10, S11 | (c)/LOW | **A** |
| **FQ-6** | **Serialization/display cap-views.** Make batch (`altIdx<3`) and bridge (uncapped) explicit per-consumer projections over the one carry, not two independent truncations. | anchor #9/#10, S20 | (c)/LOW | **A** |
| **FQ-7** | **Seed the key decoder's cost/window constants from shared symbols** (S8) so a Stage-5 fit moves one source; drop the S9 full-resolve-as-seed if the grid needs only corrected fifths+declared mode. | S8, S9 | (c)/(d)/MED | **A**/Stage-5 |
| **FQ-8** | **The already-owed migrations** (cross-reference, unchanged): the two-segmenters retirement (absorbs S3/S4), the two-pitch-context collapse (absorbs S2), the tpc-reader fold (S6), the F-1 confidence contract (S19). | S2/S3/S4/S6/S19 | — | **B** (E4 / Stage-5) |

### 3.1 Stage-1 build status (Engage arc #7, 2026-07-07 — `cc_engage_pre_l5_refactor_report.md`)

The pre-L5 Stage-1 items were executed as byte-identical revertible commits (0-diff `.ours.json`
352×3 vs HEAD `0d7fcc6c48`; robust PASS; characterise 52/24/52; suites 1101/53/11 no-refresh):

- **FQ-5 — ✅ RESOLVED `65764881d0`.** S5 (beat-weight → `regionMetricWeightForBeatType`), S10 (shared
  `normalizedConfidenceSigmoid`), S11 (`makeChordPathNode` builder) fully unified. **S7 partial:** the
  redundant `standard.*=` copy-3 deleted; full A↔B single-sourcing deferred (couples the minimal
  `modepriorpresets.h` to `analysistypes.h` — a dependency-profile design decision, flagged).
- **FQ-7 — ✅ RESOLVED `56b06462db`.** S8 constants sourced from the shared symbols. **S9 adjudicated
  KEPT (load-bearing, NOT dead):** the `resolveKeyAndModeRanked@585` feeds `greedyExpandSegmentation@851`
  + `findTemporalContext@900` (the grid); dropping it would move the grid. Report-only, no change.
- **FQ-6 — ✅ RESOLVED `5420e6e543`.** `appendCappedAlternatives` shared projection in `analyzed_section.h`;
  batch cap=3, bridge uncapped, values verbatim (cap-#2 value lift stays deferred to Stage 3).
- **FQ-1 — ⛔ STOP-and-reported (not forced).** At code the four scans are NOT one decision: divergent
  "differs" predicate (rootPc-only #1/#2/#3 vs `sameChordSymbol` = root+quality #4), element type, and
  result-use; no byte-identical single primitive exists and `promoteToWinner` (promote-to-front of a
  *specific* target) is not the vehicle. The "one decision, four sites" premise over-counts at code
  granularity — declared for Cowork adjudication (report §5).
- **FQ-3 — ⛔ STOP-and-deferred to E4 (UNCLEAR-7 resolved → fold into E4).** Byte-identically relocatable
  and decoder-independent, BUT E4-entangled: the decoder (already seeded by `findTemporalContext` at
  `regionanalyzer.cpp:899-902`, `decoder.commit()≡advanceTemporalContext`) is the E4-decided owner of
  regional temporal context (ARCHITECTURE.md D-P4/D-BRIDGE/1068: the cold walk is superseded). Relocating
  to an interim L4 home now is the "redone at E4" case; most-invasive item (new region unit + notation
  wrapper + test relocation). Deferred, not forced (report §6).

---

## 4. ★ The sequencing call (the load-bearing output)

**The question:** which fixes are prerequisite refactors to do BEFORE the Layer-5 engagement design, vs which
fold INTO it — as **one coherent order** cross-referenced to the owed R9 file-split and the §6-block
dissolution.

**The key finding that decides it:** the anchor is a **legacy-Layer-4 tangle in code that E4 retires**, and
its **clean-target is already built in the dormant decoder**. So a full standalone refactor of the legacy
`results` substrate would be throwaway work on retiring code. **But three portable slices are genuine pre-L5
wins** because they are path-independent or serve both paths.

### The one coherent order

**Stage 1 — PRE-L5 (now; path-independent; mostly byte-identical-provable):**
- **FQ-1** the different-root primitive (needed by both paths; extends `promoteToWinner`).
- **FQ-3** relocate `findTemporalContext` out of L1.5 (live-path HIGH; decoder-independent).
- **FQ-5** the fact-layer duplication cleanups; **FQ-6** the cap-views; **FQ-7** the key-decoder constant
  sourcing.
- These retire real total-unification debt, shrink the surface the engage design must reason about, and none
  of them depends on the decoder.

**Stage 2 — STAGE-5 / the §6-block dissolution (OWED refactor #2; retirement map R1 "Gates A–L — E4, or
Stage-5 if first"):**
- **FQ-2** give quality-from-key one owner — decided **with** the §6-block dissolution (Gates L/G-E are part
  of that block; the sparse/section quality overwrites are the same concern).
- **FQ-8**'s **F-1 confidence contract** (S19) — the Stage-5 calibration item the resolver already defers.

**Stage 3 — E4 (the legacy chord path retirement; the decoder engages):**
- **FQ-4** the anchor — the decoder's governed carry **replaces** the `results` substrate; cap/append/pedal
  clobber die by construction. The audit's §1.4 clean-target is the **input** to this engage design (pedal
  home; exhaustion watch-item; Iter 91 targeted-promotion re-expression).
- **FQ-8**'s migrations land here: the two-segmenters retirement (S3/S4), the two-pitch-context collapse
  (S2), the tpc-reader fold (S6), the `function/` dir rename (S18).

**Stage 4 — R9 (after the E4 removals; OWED refactor #1):**
- The `chordanalyzer.cpp` file split — **"split once"** after the removals, exactly as parked.

**In one line:** *pre-L5 = FQ-1, FQ-3, FQ-5, FQ-6, FQ-7 (portable unification wins); part-of-L5/E4 = FQ-2,
FQ-4, FQ-8 (the legacy-path tangles the decoder + §6-block dissolution retire); then R9 splits the file
last.* This adds no new stage — it slots the audit's fixes into the plan the roadmap already has.

---

## 5. UNCLEAR rows for user adjudication

1. **S2/S3/S4** (fact-layer raw-DOM walks) — catalogue the 3rd/4th eligibility-walk copies and the legacy
   segmenter's tuplet-snap **separately**, or fold them wholesale into the already-scheduled two-segmenters
   retirement? (They are on that retirement path, but carry interpretation worth surfacing first.)
2. **S8/S9** (key-decoder constants copied-by-value; full-resolve-as-seed) — intended coupling / deliberate
   byte-stability, or un-unified constants + retained dead scoring work?
3. **S14/S16** (quality-from-key mutation in gates + region orchestrator) — is quality-from-key second-
   guessing acceptable across these owners until FQ-2, or does it need its single owner **before** the
   §6-block dissolution?
4. **S18** (the `function/` dir) — rename now (cheap, cosmetic) or hold for the E4 engage rename it is
   already scheduled with?
5. **S19** (F-1 at code) — accept the deferred θ/scale until Stage-5 calibration, or require the resolver to
   consume a normalized margin now (it is dormant, so low urgency)?
6. **S20** (root-equality inlined in the metric scripts) — worth a `roots_agree` helper given the R10-b
   figure rests on it, or leave as trivial equality?
7. **FQ-3 placement** — `findTemporalContext` relocation as a pre-L5 fix, or is it simpler to fold into the
   E4 temporal-context ownership move?

---

*CC, 2026-07-07. Engage arc #6 — structural-integrity audit, all built layers, read-only. Priors extended,
not re-derived. Every fix is its own later ratified refactor; the sequencing call slots them into the
existing R9 / §6-block / E4 plan. Cowork verifies the catalogue at objects → brings the fix-queue, the
sequencing call, and the UNCLEAR rows to the user.*

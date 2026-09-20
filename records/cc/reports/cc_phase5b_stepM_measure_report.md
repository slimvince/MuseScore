# CC — Phase 5b Step M (part 1): the engage MEASUREMENT (read-only)

**Status: READ-ONLY measurement + analysis. No production `src/composing/` edit, no decoder change.** The full-capability
new path (`--decode-chords`, all increments G1 → G2/G3 → two-reading inherit → G6 → G4 spelling-pin ON, decoder source at
HEAD `1e74f21ea4`) was run diagnostically over the corpus and graded; production is untouched. The only commit this step
created is the §0 doc commit. `upstream` untouched.

> **Measurement instrument (the one tool edit, reverted).** `batch_analyze.cpp` (a diagnostic *tool*, **not**
> `src/composing/`, **not** the decoder) carried a **temporary measurement-only emission** of the G6 fields the decoder
> already populates (`decision`, `openQuestion.{question,ambiguity}`, `confidenceModel`, the two competing readings) —
> additive JSON only. This is the same practice Step 4 used (its temporary `--chord-no-spelling-pin` flag). It was
> **reverted before finishing** (§Stops); the tree is clean, verifiable by sha that only the §0 doc changed.

---

## §0 — Sweep (doc-commit)

The working tree carried one unstaged `cowork_*` doc (`cowork_phase5b_l4_build_plan.md` — the Step-0 grounded-order edits
+ the Step-2 "DONE & ACCEPTED" / §15-O2-deferred annotations). Committed local-only:

**`6732e77c9a`** — `docs(cowork): Phase-5b plan/ledger updates` (`git show --stat`: the one plan doc; `scratch_artifacts/`
left untracked/gitignored). No ledger file was unstaged. Not pushed.

---

## TL;DR — the engage call: **engage-WITH-L5**, not refine-then-engage

1. **Where it commits, the new path BEATS legacy** — **+5.5 pts Baroque / +5.8 Default** dur-weighted chord-root on the
   *same committed slices*, common grain (decoder 77.8 % vs legacy 72.3 / 71.9 %); +6.0 on the full corpus. The
   per-slice architecture is **validated where it answers**. (§1)
2. **But it only commits 41.8 % of duration and abstains 58.2 %**, and a coverage-matched (full-coverage) engagement is
   **BELOW legacy**: the region-grain engage view (decoder where it commits, legacy fills the abstains) = **68.0 %
   Baroque / 67.6 % Default**, i.e. **−5.9 / −6.0 pts vs pure legacy (73.8 / 73.6 %)** at the same grain. (This 68.0 %
   **reconciles exactly** with the prior reports' "coverage-matched 68.0 %" — now benchmarked against legacy, which they
   did not do.) The abstention is **load-bearing**: forced to answer everywhere the decoder is only 57.8 % (≈ the
   pre-G1 always-commit line). (§1)
3. **~85 % of the abstention is genuinely function-dependent → Layer 5**, NOT recoverable by the deferred L4 refinements.
   By the G6 `ambiguity` label the abstain splits **Transition 47.1 % · Close 25.3 % · ShareTone 19.6 % · Insufficient
   4.6 % · RelativePair 3.4 % · SymmetricRotation 0.0 %**. The O2 + C2 + dim7-commit refinements together recover only
   **~15 % of the abstain ≈ 8.7 % of scorable duration**; the genuinely-function residual is **~85 % of abstain**.
   (§2 — stable on the full 326-stem corpus.)
4. **Projection: refine-then-engage cannot close the gap.** Pulling in O2 + C2 + dim7-commit drops abstain only
   **58.2 % → ~49.5 %** (residual still ~half the duration, all function-dependent → L5) and lifts committed coverage
   41.8 % → ~50.5 %. The residual is **too large and too function-dependent for any L4 refinement** — **L5 is the layer
   that resolves it.** (§3)
5. **Class-(b) hard-stop signal: 86 projected regressions** (per preset, TEST split) — slices where the new path commits
   a pitch-class-decidable root WRONG where legacy is right (74 genuine wrong-root, 12 softer; 1.42 % of scorable). At
   fine slice grain; these are exactly why naive engagement is −5.9 (transient fine commits corrupt correct legacy
   regions when grouped). **Flagged prominently** (§1 class-(b)); they are the engagement hard-stop class and need the
   L4→section grouping (F-3) + L5 override before any switch.

**→ Engage-viability verdict (the §3 decision data): the full-capability new path is (a) better-than-legacy where it
commits — YES; (b) with an *acceptable* residual abstain → L5 — the residual is LARGE (~49 %) but it is the CORRECT
function-dependent L5 hand-off, not an L4 defect. Refine-then-engage is NOT viable on its own (refinements buy ~9 %
coverage, not the ~half the abstain needs); the honest path is ENGAGE-WITH-L5 — engage the new spine together with the
L5 resolver that the 58 % abstain is, by construction, waiting for.** Cowork + user decide.

---

## Method

- **One decode, both presets.** `--decode-chords` over the canonical 353-stem corpus (`tools/corpus/*.xml`) via the
  Step-0/1 scratch driver (`decode_g1_driver.py`, the F-16 path fix), Baroque + Default → 353/353 each, 0 failures.
  **The decoder is preset-identical** (null-context vertical scoring + the same notated key): the two decode dirs are
  **content-identical on all 353 stems** (re-verified, 0 differences), corroborating the Step-0/1/2/3 fact. Only the
  **legacy baseline** differs by preset (`tools/corpus/{baroque,default}/*.ours.json`).
- **Graders.** The committed substrate (`cc_layer4_chord_baseline.py` + `compare_analyses.align_dcml_regions` + the
  music21 `RomanNumeral` GT index, held-out TEST split md5(stem)%100<20, dur-weighted) — **anchored**: the committed
  grader reproduces decoder among-committed **77.8 %** vs legacy native-region **73.8 / 73.6 %** (+4.0 / +4.2), matching
  the Step-4 build state exactly. The Step-M-specific lines (legacy-on-same-slices, coverage-matched, class-(b),
  ambiguity buckets, recoverability) are a read-only scratch analyzer (`scratch_artifacts/stepM_analyze.py`) over the
  same substrate. All numbers are **TEST split** unless noted; the §2 buckets are confirmed stable on the full 326-stem
  WiR-covered corpus.

A note on **granularity** (the load-bearing subtlety, per CLAUDE.md Stage 2.2-i): legacy is **per-region (coarse)**, the
new path **per-slice (fine)**. The committed grader's "legacy 73.8 %" is legacy at its **own region grain**; the same
legacy evaluated at the **fine slice grain** is only **60.6 %** (its coarse regions over-grab across GT-chord
boundaries). The honest comparisons below state their grain explicitly.

---

## §1 — Full coverage-matched comparison (the GO/NO-GO baseline)

Held-out TEST split, duration-weighted chord-root. Decoder is preset-identical, so (a)/(c)/abstain are equal across
presets; only the legacy-dependent lines (b)/(d)/(e)/(f)/(g) differ.

| line | Baroque | Default |
|---|---|---|
| **(a) raw committed accuracy** (decoder, among the slices it commits) | **77.8 %** | **77.8 %** |
| **(b) legacy accuracy on the SAME committed slices** (common grain) | 72.3 % | 71.9 % |
| **→ decoder advantage WHERE IT COMMITS** | **+5.5** | **+5.8** |
| (c) coverage-matched, forced best guess (decoder answers everywhere) | 57.8 % | 57.8 % |
| (d) legacy full, same fine slice grain | 60.6 % | 60.3 % |
| (e) legacy-fallback floor (commit where confident; legacy fills abstains, fine grain) | 62.9 % | 62.8 % |
| **(f) coverage-matched = REGION-GRAIN engage** (decoder-majority commit per legacy region; legacy fills empties) | **68.0 %** | **67.6 %** |
| (g) pure legacy at region grain (the native ~73.8 % line) | 73.8 % | 73.6 % |
| **→ region-grain engage Δ vs legacy** | **−5.9** | **−6.0** |
| **abstain %** | **58.2 %** | **58.2 %** |
| committed % (Commit 39.9 % + Inherit 2.6 %) | 41.8 % | 41.8 % |

(Full corpus, all-split corroboration: (a) 80.4 %, (b) 74.3 % → **+6.0** where committed; (f) 69.8 % vs (g) 74.9 % =
**−5.1**; abstain 57.4 %.)

**Reading.**
- **"Is it better where it answers?" — YES, decisively.** On the exact 41.8 % of duration it commits, the new path is
  **+5.5 / +5.8** over legacy at the *same* grain. This is the genuine asset and validates the per-slice scorer.
- **Raw committed accuracy 77.8 %, abstain 58.2 %.** The +5.5 is *among committed*; coverage-matched it is **below**
  legacy.
- **Coverage-matched (the engage line) = 68.0 % = the prior reports' number, now benchmarked: −5.9 vs legacy 73.8 %.**
  The prior steps cited 68.0 % as "the best variant / engage-relevant" but never set it against pure legacy at the same
  region grain; doing so shows naive engagement is a **−5.9 pt regression**. Two mechanisms: (i) the decoder abstains on
  58 % of duration (handed to legacy-fill, which on those hard regions is itself weaker), and (ii) the decoder's fine
  **transient commits**, reduced to region-majority, **override correct legacy regions** (the class-(b) mechanism below).
- **Abstention is load-bearing.** Forced to answer everywhere (c), the decoder is only **57.8 %** — essentially the
  pre-G1 always-commit line. The new path is good *because* it declines the hard 58 %, not because it sees more.

### §1 class-(b) check — the engagement hard-stop class

Slices where the new path **commits a pitch-class-decidable (non-symmetric) root WRONG** where **legacy is right** — the
class-(b) functional-regression hard-stop, projected for engagement (the decoder is dormant, so these are *projected*
engage regressions, not live).

| | Baroque | Default |
|---|---|---|
| class-(b) cases | **86** | **86** |
| duration | 27 480 (3.41 % of committed, **1.42 % of scorable**) | 27 480 (same) |
| decoder root NOT in GT chord-tones (**genuine** wrong root) | 74 | 74 |
| decoder root IN GT (inversion / share-tone member — softer) | 12 | 12 |
| by decision: Commit / Inherit | 61 / 25 | 61 / 25 |
| stem concentration (max per stem) | ≤4 (spread, not one pathological score) | ≤4 |

Examples (`stem@tick`: GTroot → decoder, legacy=GTroot): `bwv11.6@26400` (A→F#), `bwv16.6@3360` (D→B),
`bwv179.6@5040` (C#→A), `bwv244.44@2880` (A→D), `bwv245.28@13920` (E→A). **These are at fine slice grain** — typically a
transient sub-slice (a 6th/passing/arpeggiated fragment) of a region legacy reads correctly at the coarse grain. Whether
the deferred **L4→section grouping (F-3)** absorbs them, or **L5** overrides them, is the engage-step question — but
**as-is they are 86 projected wrong-where-legacy-right commits**, and they are exactly why (f) is −5.9. **This is the
hard-stop class; it must be driven to zero (grouping + L5) before any production switch.** No new class-(b) appears
*outside* engagement (production is byte-identical, corpus 53/24/53 untouched).

---

## §2 — Abstain breakdown by RECOVERABILITY (the strategic data)

Of the **abstained duration** (58.2 % of scorable), bucketed first by the G6 open-question `ambiguity` label, then mapped
to what would recover each. (TEST split; the percentages are confirmed stable on the full 326-stem corpus — shown in
parentheses.)

### (a) By G6 ambiguity label (% of abstained duration)

| ambiguity label | % of abstain (TEST) | (full corpus) | character |
|---|---|---|---|
| **Transition** | **47.1 %** | (47.0 %) | thin slice heading into a *different* next chord — needs the progression |
| **Close** | **25.3 %** | (25.9 %) | two close, otherwise-unrelated readings — general low margin |
| **ShareTone** | **19.6 %** | (18.5 %) | competing readings explain the SAME pcs (Am6↔F♯ø7) — pc-identical |
| **Insufficient** | **4.6 %** | (5.6 %) | too few chord tones to fix a chord (genuinely thin) |
| **RelativePair** | **3.4 %** | (3.0 %) | roots a minor third apart, major↔minor (C↔Am) |
| **SymmetricRotation** | **0.0 %** | (0.0 %) | — (see note) |

> **Note on SymmetricRotation = 0.** No abstain carries this label — confirming the Step-4 finding: after G1/G6 the
> decoder does **not** reach a symmetric *chosen* on dim7 slices (its window-winner is a *phantom non-dim* that G1
> abstains as Insufficient, or the dim7 collection lands in the C2 bucket). The dim7 churn is already *dissolved by
> abstention*, exactly as the design intends ("dissolve here, resolve at L5").

### (b) Mapped to recoverability (% of abstained duration)

| recoverability bucket | % of abstain (TEST) | (full corpus) | what recovers it | forced best-guess acc today |
|---|---|---|---|---|
| **dim7-commit** (SymmetricRotation dim7, spelling-pin pins) | **0.0 %** | (0.0 %) | the G4 pin — but nothing is so-labeled | — |
| **C2-newtype** (full 4-note dim7/mMaj7 collection, no TYPE) | **2.9 %** | (2.7 %) | the deferred dim7/mMaj7 catalogue types (G5/C2) | 8.7 % |
| **O2-joint** (Transition/Insufficient where a *bounded* joint window over the abstain-run recovers gt_root+triad) | **12.0 %** | (12.8 %) | the deferred §15-O2 bounded-window joint resolution | 32.9 % |
| **L5-function** (the genuinely function-dependent residual) | **85.0 %** | (84.5 %) | Architectural Layer 5 (progression / function) | 46.0 % |

- **O2-recoverable ≈ 12 % of abstain.** Bounded ±1-slice window, pooled ≤5 pcs (the spec's "one harmony's worth", not
  the whole run). **Sensitivity:** the *loose* whole-run pooling inflates this to ~37 % of abstain — but even then the
  residual function abstain stays ~35 % of scorable, so the strategic conclusion is **robust across the O2 proxy range**.
  The low *current* best-guess accuracy on this bucket (32.9 %) shows these slices are today phantoms — O2's job is real
  but unbuilt; 12 % is a *ceiling*. Examples: `bwv11.6@960` (Transition, sounding {D,E,A} of GT A), `bwv11.6@2160`
  (Transition, full {D,E,G#,B}).
- **C2-recoverable ≈ 2.9 % of abstain** — full dim7/mMaj7 collections the 17-template catalogue cannot name as a TYPE.
  Examples: `bwv174.5@24480` (mMaj7 {D,F,G#,B}), `bwv179.6@16080` (dim7 {C,D#,F#,A}), `bwv227.7@17520` (dim7
  {C#,E,G,A#}).
- **dim7-commit ≈ 0** — folds into C2/Insufficient (no SymmetricRotation label survives G1/G6, per the note above).
- **L5-function ≈ 85 % of abstain** — Transition (the genuine ones, where the joint window does NOT recover GT) + Close +
  ShareTone + RelativePair. These need the **progression / function** and are irreducible at L4 → correctly Layer 5.
  Examples: `bwv11.6@1200` (Close, {C#,E,A}), `bwv11.6@3360` (ShareTone, {E,A,B} vs GT {E,G#,B}), `bwv11.6@2640`
  (Transition, {F#,A} fragment).

---

## §3 — Engage-viability projection

**If O2 + C2 + dim7-commit are all pulled in** (the deferred refinements), projected over the held-out TEST split:

| | Baroque (TEST) | full corpus |
|---|---|---|
| current abstain % | 58.2 % | 57.4 % |
| recoverable abstain (O2+C2+dim7) | 15.0 % of abstain = **8.7 % of scorable** | 15.5 % = 8.9 % |
| **PROJECTED residual abstain → L5** (genuinely-function) | **49.5 %** | 48.5 % |
| projected committed coverage | 50.5 % (from 41.8 %) | 51.5 % (from 42.6 %) |
| projected among-committed accuracy — **ceiling** (recovered commit correctly) | 81.6 % | 83.8 % |
| projected among-committed accuracy — **floor** (recovered at today's readingA rate) | 69.2 % | 71.4 % |

**The projection answers §3's two halves:**
- **(a) Better-than-legacy where committed? YES** — and it stays so after refinement (+5.5/+5.8 today; the refinements
  add coverage, not error, in the ceiling case). The per-slice scorer is the genuine asset.
- **(b) Acceptable residual abstain → L5? The residual is LARGE (~49 % of scorable) — but it is the CORRECT, by-design
  function-dependent L5 hand-off, not an L4 shortfall.** Refine-then-engage moves abstain only 58.2 % → ~49.5 % (the
  refinements are worth ~9 % of duration); it **cannot** close the gap, because **~85 % of the abstain is genuinely
  function-dependent** (Transition/Close/ShareTone/RelativePair). At the user-facing region grain, naive engagement is
  **−5.9 vs legacy** with **86 class-(b) regressions** — engagement *as L4-only* is a net regression.

**→ The honest call is ENGAGE-WITH-L5, not refine-then-engage.** The 58 % abstain is, by construction, the open question
the L4→L5 contract (G6) hands forward; the dominant residual is function — so the engagement that realises the
+5.5-where-committed asset at the user-facing grain is the one that **switches the new L1→L4 spine on together with the L5
resolver** (function/cadence/progression) that resolves the Transition/ShareTone/RelativePair/Close residual *and*
overrides the class-(b) transients. The deferred L4 refinements (O2 ≈ 12 % of abstain, C2 ≈ 3 %) are a **minor pre-L5
coverage gain worth doing**, but they are **not a substitute for L5** and do not change the engage decision. Refining
first and engaging L4-alone would still strand ~half the duration in abstention and ship a −5.9 / 86-class-(b)
regression.

---

## §4 — Deliverables

- This report (`cc_phase5b_stepM_measure_report.md`, gitignored).
- Scratch artifacts (gitignored / untracked under `scratch_artifacts/`): the G6-emission decode
  `corpus_decode_chord_stepM/{baroque,default}` (353/353 each, content-identical), the analyzer `stepM_analyze.py`, the
  graded outputs `stepM_analysis_test.txt` + `stepM_analysis_all.txt`, build log `build_stepM.log`.
- **No production edits, no decoder change.** The §0 doc commit `6732e77c9a` is the only commit. The temporary
  `batch_analyze.cpp` measurement emission is reverted (tree clean).

## §5 — Stops honored

- **No production `src/composing/` edit, no decoder change.** The decoder (`chordslicedecoder.{h,cpp}`) and all
  `src/composing/` source are byte-identical to HEAD `1e74f21ea4`; corpus gate **53/24/53 untouched** (the decoder is
  production-dead, `--decode-chords` returns before `analyzeScore`). The one tool edit (`batch_analyze.cpp`
  measurement-only G6 emission) is **reverted** before finishing — verifiable by sha that only the §0 doc changed. ✓
- **A class-(b) regression appears (§1): FLAGGED PROMINENTLY** (86 projected cases, the engagement hard-stop class) and
  the measurement continued (it is data for the engage decision, not a build STOP — the decoder is dormant, nothing
  shipped). ✓
- No `upstream` push. ✓

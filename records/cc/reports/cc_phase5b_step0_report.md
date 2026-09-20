# CC — Phase 5b Step 0: ground the L4 build (read-only investigation + measurement)

**Status:** READ-ONLY for production source (no `src/composing/` edits) + measurement (diagnostic corpus run, no
production change). Per `cowork_phase5b_l4_build_plan.md` Step 0. Decoder source is at commit `5f6b9828a5` (Increment B)
and clean; the `--decode-chords` path is unchanged from what the prior Layer-4 reports measured. `upstream` untouched.

**§0 doc-commit sha:** **`9ef7ff312a`** — `docs(cowork): Phase-5b incremental L4-build plan + F16 done`.
`git show --stat` lists ONLY the two docs (`cowork_phase5b_l4_build_plan.md` new + `cowork_l1l4_completion_ledger.md`
F16 edit); `scratch_artifacts/` left untracked.

---

## TL;DR — the grounded read

1. **The new path is built but INCOMPLETE against the spec in exactly the place the measurement says matters most.** The
   per-slice path always **commits** its top-scoring candidate; the spec's **commit / inherit / abstain** trichotomy and
   its **sufficiency gate** (the "never name a new symbol from too few notes" rule — the phantom-root defect rule) are
   **unbuilt**. Only a margin-based binary `uncertain` flag exists.
2. **Measured TODAY (restored gate, Baroque + Default), the new per-slice path is −15 pts behind legacy on chord-root**
   (58.4 % vs 73.8 % dur-weighted) — **reproducing the prior baseline to the digit**. Of that gap, granularity accounts
   for only ~2 pts; the **−13 pt residual at equal grain** is the per-slice **window not gathering the harmony** (42 %
   thin slices, 41 % phantom roots). The Increment-C **spelling-pin reaches only 3.1 %** of misses.
3. **No spec/architecture rethink is indicated** — the per-slice unit fits the as-built slicer exactly and shares L3's
   already-wired slice spine. But the plan's **provisional increment ORDER is wrong**: build **inherit/abstain +
   sufficiency FIRST** (targets the 42 %/41 % dominant residual), spelling-pin **last** (small). This re-grounds and
   confirms the prior `cc_layer4_residual_decomposition_report.md` verdict with the restored gate.
4. **First engage read: NO-GO to engage now** (−15 pts); **conditional GO on the architecture** once the inherit/abstain
   build closes the thin-slice deficit and a re-measure shows equivalent-or-better. Two genuine *engage-step* questions
   (not blockers for the dormant builds): where **grouping / section-layer integration** lives (F-3), and how the new
   **four-note types** enter without moving the legacy output (F-4).

---

## §1 — `chordslicedecoder` as-built vs the L4 spec (the gap)

Read line-by-line: `src/composing/analysis/chord/chordslicedecoder.{h,cpp}` (commit `5f6b9828a5`, Increment A + B) and
`cowork_layer4_chordsymbol_design.md` (SIGNED 2026-06-24). Corroborated by the pre-build audit
`cc_layer4_audit_dossier.md`.

### What is built (and matches the spec)
- **Per-slice listing — reuses the one scorer's cube (spec §4/§5.1, §9 "no second scorer").** `candidatesForWindow`
  ([chordslicedecoder.cpp:252](src/composing/analysis/chord/chordslicedecoder.cpp#L252)) runs the existing
  `analyzeChord` over each slice's window and surfaces the complete `fn::ScoringSnapshot::cells` cube (every
  bass × root × template cell with its vertical fit score), exactly as the L3 decoder surfaced the 252-candidate key
  dump. ✓ — **but the cube is over the 17 QUALITY templates only**; extensions/6ths/dim7/9ths are post-hoc on the
  winner (see G5).
- **Rank + choose winner.** `decideSlice` ([chordslicedecoder.cpp:288](src/composing/analysis/chord/chordslicedecoder.cpp#L288))
  ranks deterministically (`candidateBetter`) and sets `chosen = ranked.front()`.
- **Competing readings carried.** Ranked distinct voicings (capped at `topK`) ∪ the prevailing chord
  ([chordslicedecoder.cpp:325-363](src/composing/analysis/chord/chordslicedecoder.cpp#L325-L363)). ✓ spec §7.
- **Adaptive lazy-extend window (Increment B, spec §2).** `adaptiveWindow`
  ([chordslicedecoder.cpp:131](src/composing/analysis/chord/chordslicedecoder.cpp#L131)) grows ±1 slice until
  `minHarmonyPcs` distinct PCs or `maxContextSlices`. ✓ — but bounded by count, no selection-edge "request extension"
  (see G7).
- **Membership two-pass (Increment B).** `classifyMembership` + `finalizeSlice` + `decodeWindowed` two-pass over
  provisional neighbours ([chordslicedecoder.cpp:368,461,492](src/composing/analysis/chord/chordslicedecoder.cpp#L368));
  `enableMembership=true`, `twoPass=true` by default. BUILT — but the rule diverges (G2/G3).
- **Key as a feed-forward prior.** One notated key for the whole run, baked into the cube via the diatonic scorer prior;
  per-slice L3 feed-forward deferred (header §KEY). The fair-key test already simulated L3 per-slice key (build-B report)
  → ~0 pt move, so this is a wiring detail, not the lever.

> **Doc-drift flag (not a defect):** the `.h` top comment still says "**INCREMENT A only** … membership sets STUBBED
> EMPTY" ([chordslicedecoder.h:26,40-49](src/composing/analysis/chord/chordslicedecoder.h#L26-L49)). That is **stale** —
> Increment-B membership IS built and ON by default. Worth a one-line header correction whenever the file is next touched.

### What abstain / "uncertain" / inherit handling exists TODAY
- **`uncertain` = a single margin test.** `sc.uncertain = sc.confidence < uncertaintyMargin`
  ([chordslicedecoder.cpp:319](src/composing/analysis/chord/chordslicedecoder.cpp#L319)), where
  `confidence = chosen.score − best DIFFERENT (root,quality) score`. Every slice is still **named** (the diagnostic
  reports `namedSlices == slicesTotal`; e.g. bwv120.6 = 93/93 named, 51 flagged uncertain) — the flag never abstains.
- **No inherit.** The prevailing chord is ∪'d into `alternatives` but **never replaces the chosen chord** on a thin
  slice.
- **No named open question.** `SliceChord` carries no open-question label (root / quality / note-membership).

### What is MISSING / DIVERGENT vs the spec (precise, mapped to spec sections)

| # | Gap | Spec section | As-built |
|---|---|---|---|
| **G1** | **commit / inherit / abstain + sufficiency gate — largely UNBUILT (the headline gap)** | §4 step 3, §5 step 4, §9 "don't guess on thin evidence" | Always commits `ranked.front()`. **No** sufficiency gate (≥3 distinct chord-tones after membership), **no** inherit-prevailing-on-insufficiency, **no** abstain-with-open-question. The phantom-root rule ("a new symbol is never committed from too few notes") is **not enforced**. |
| **G2** | **membership three-tier rule — divergent** | §5 step 3 | As-built rule (`classifyMembership`): non-template note → NCT iff `(metrically weak) OR (both-sides-stepwise) OR (suspension)`. A flat two-cue OR, **not** the spec's structure-first ladder. **Tier 1** (stepwise→NCT regardless of weight) ✓; **Tier 2** (weak *leap* → CT-extension regardless of weight) **VIOLATED** — a weak non-stepwise note is called NCT; **Tier 3** (one-sided stepwise, weight-decided) uses weight only, ignores the one-sided structural signal + prevailing chord. |
| **G3** | **plausibility check (template tones tested) — different mechanism** | §5 step 3 | Template tones are auto-CT (never behaviour-tested). `implausibilityPenalty` charges a candidate for **extra** structural notes it leaves out (inverse framing) — catches "strong extra ⇒ prefer richer chord" one way, but **cannot** catch "the candidate's own 9th is really a passing tone" (the accented-passing-tone C-vs-Cadd9 case the spec calls out). |
| **G4** | **symmetric-root spelling-pin (Increment-C) — UNBUILT (confirmed)** | §5/§9 | Symmetric dim7/aug root = the scorer's winner, whose rotation is chosen by `dim7CharacteristicBonus` (**key-non-diatonicity → key-dependent**, the class-(a) churn source — `cc_layer4_audit_dossier.md` headline 4), **not** the deterministic notated-spelling pin. The `spellingview` primitive (`lineOfFifths`/`sharpFlatSense`) **exists** (`engravingbridge/spellingview.{h,cpp}`, Phase-4 capability) but the decoder does **not** consume it. tpc is carried (`rootTpc`) for naming only. |
| **G5** | **new four-note TYPES (dim7, minor-major) — UNBUILT (confirmed)** | §1, §9 | The 17-template catalogue ([chordanalyzer.cpp:1224-1242](src/composing/analysis/chord/chordanalyzer.cpp#L1224-L1242)) has `Diminished` as a **triad `{0,-3,-6}` only** — no `{0,3,6,9}` dim7 type, no `{0,3,7,11}` mMaj7 type. A dim7 is scored as dim-triad + extra note (exactly the replaced-code behaviour §9 corrects). Adding them touches the **shared production** catalogue (see §3 F-4). |
| **G6** | **confidence composite + open-question label — PARTIAL** | §7 | Confidence = **margin only**; spec confidence is composite (margin + sufficiency + membership-cleanliness). No open-question label. (Coupled to G1.) |
| **G7** | **bounded-context at selection edge — UNBUILT** | §2 | `adaptiveWindow` clamps to slice `[0, n-1]` and proceeds truncated; no "request one harmony's worth of extension" vs "score boundary" distinction (no selection concept). Inert for the whole-score diagnostic; needed for the bounded-context engagement (plan Step E). |

### Production status (confirmed production-dead → byte-identical until engaged)
`grep` over `src/`: `ChordSliceDecoder`/`chordslice` is referenced **only** by its own `.h/.cpp`, by
`tests/decode_chord_tests.cpp`, and by `tools/batch_analyze.cpp` (the `--decode-chords` diagnostic, which **returns
before `analyzeScore`**, batch_analyze.cpp:2233-2245). **`regionanalyzer.cpp` does NOT reference it** — the live chord
path is still the legacy per-region `analyzeChord` seam. Building on the decoder stays byte-identical (corpus 53/24/53
unchanged) until the engage step.

---

## §2 — New path vs legacy, measured TODAY (the baseline — uses the restored gate)

Method: a fresh `--decode-chords` run over the canonical 353-stem corpus, Baroque + Default (a Step-0 scratch driver
with **Windows-form paths** — see F-6 below — wrote `tools/corpus_decode_chord_step0/{baroque,default}`, 353/353 each,
0 failures), graded by the committed `tools/cc_layer4_chord_baseline.py` + `tools/cc_layer4_residual_decompose.py`
(decoder per-slice vs the legacy per-region `.ours.json`, both vs the When-in-Rome GT via music21 `RomanNumeral`,
held-out TEST split, dur-weighted = the granularity-comparable line). 326/353 WiR-covered.

### Headline — chord-root, duration-weighted (TEST split)

| dur-wt chord-root | Baroque | Default |
|---|---|---|
| per-region **legacy** baseline (`.ours.json`) | **73.8 %** | **73.6 %** |
| per-slice **new** decoder | **58.4 %** | **58.4 %** |
| **Δ (new − legacy)** | **−15.5 pts** | **−15.2 pts** |
| per-slice **reduced-to-region** grain | 60.7 % | 60.5 % |
| **residual at EQUAL grain** | **−13.1 pts** | **−13.1 pts** |

- **The decoder output is preset-identical** between Baroque and Default (all **353/353** decode JSONs byte-identical):
  the per-slice path scores **null-context vertical only** (`context=nullptr`, no inversion-context bonuses, no
  progression signals), and Baroque/Default share the struct chord defaults + the same notated key. Only the **legacy
  baseline** is preset-sensitive (73.8 vs 73.6 — its gates + section logic differ). This is a clean, expected fact, and
  it means the chord-axis Step-0 read is the same for both presets.
- **Reproduces the prior baseline to the digit** (`cc_layer4_build_b_fairkey_report.md` Baroque/Jazz −15.41/−15.34;
  `cc_layer4_residual_decomposition_report.md` −15.5/−15.3). The restored gate measures the same decoder; the −15 gap is
  stable and real.

### The SHAPE of the differences (where the −15 lives)

**Granularity is NOT the explanation.** Coarsening the decoder to the baseline's own region grain recovers only
**+2.3 / +2.2 pts**; a **−13.1 pt deficit remains at equal grain** (both presets). The decoder is wrong across
substantial spans, not just in short isolated slices.

**Miss decomposition (2815 per-slice misses):**

| bucket | count | % misses | what fixes it |
|---|---|---|---|
| **(b) spelling-fixable** (dim7 49 + aug 6 + ø7↔m6 32) | **87** | **3.1 %** | the Increment-C spelling-pin (G4) — **small** |
| (c) genuinely-wrong — **wrong root (root ∉ GT chord-tones)** | **1698** | **60.3 %** | the window/inherit/abstain build (G1) |
| (c) share-tone / function (root ∈ GT) | 503 | 17.9 % | Layer 5 (function) |
| (c) inversion (same notes, wrong root) | 108 | 3.8 % | bass/inversion |
| (c) other | 419 | 14.9 % | — |

**Fragment diagnostics over ALL misses — the "window not gathering" signal (the dominant cause):**
- **thin slice (≤2 named chord-tones): 42.1 %** · decoder notes ⊊ GT (saw a fragment): 35.9 % · **phantom root
  (root ∉ its own notes): 40.9 %** · foreign notes: 47.1 %.
- named-chord-tone histogram among misses: `0:20, 1:207, 2:959, 3:1339, 4:290` → **1186 (42 %) have ≤2 named tones.**
- top root misses (our→gt): `2→9, 9→4, 9→2, 7→2, 5→2, 11→2` — fifth / relative-root confusions (a dyad/fragment read
  as the wrong member of the prevailing harmony).

**Membership (NCT, spec §10 metric, TEST split):** NCT precision **50.4 %**, NCT recall **34.5 %**, CT precision
**82.9 %**, CT recall 90.3 %, over-read rate 22.2 %. (Preset-identical.) The membership lever is partway built (Increment
B) but the three-tier refinement (G2/G3) is the headroom — and over-read 22 % is exactly the inherit/abstain target.

**Reading:** the new path's deficit is **the spec's own unbuilt thin-slice handling (G1)** — a fine slice grid commits a
phantom chord on a 1–2-note fragment instead of inheriting the prevailing harmony or abstaining. The spelling-pin (G4)
is a real but tiny lever. This maps the §2 measurement **directly onto the §1 gap**.

---

## §3 — Architecture friction (the amendment radar)

**F-1 — per-slice (new) vs the L2 slicer: the unit FITS, no mismatch.** The decoder consumes `slicing::Slice` from
`changePointSlices` **directly** (batch_analyze.cpp:2257); the spec's L4 unit ("for each slice produced by Architectural
Layer 2") **is** the L2 slice. The slicer is the finest constant-sonority grid (a boundary at every eligible
onset/release — over-grab structurally impossible, slicer.h §invariants), so it produces **many thin slices**. The spec
*anticipates* this (window §2, arpeggios §5, incomplete-chords §5, inherit/abstain §4); the as-built decoder does **not
yet implement** the thin-slice handling the fine grid requires (G1). → **a build gap, not an architecture mismatch.** The
spec's per-slice decomposition fits the as-built slicer.

**F-2 — L3 + per-slice chord: SAME spine, unification-consistent.** L3 key already runs on the identical grid
(`regionanalyzer.cpp:579-581`: `changePointSlices` → `KeyModeSequenceDecoder::decode`). A per-slice chord path shares
that spine; per-slice key feed-forward (L3 → L4 prior) is natural and was already simulated cleanly (build-B fair-key,
~0 pt quality move). → **no friction; engaging per-slice chord unifies L3 + L4 on one grid (the architectural goal).**

**F-3 — the SECTION layer is the real ENGAGEMENT friction.** The live user-facing output is `analyzeSection`
(`section/sectionanalyzer.h`: Passes 1–4 + key/mode **stabilization** + cadence/pivot detection + display grouping),
which consumes **per-region** chord output. A per-slice path emits fine slices, not regions. Engaging therefore needs
either the section layer to consume slices, **or an L6 grouping / reduce-to-region adapter at the L4→section seam** (the
spec assigns "group consecutive same-chord slices" to Layer 6, §3/§13). **That grouping is not yet built/wired**, and the
pinned **P1–P4 snapshot goldens WILL move** on engagement (expected — engagement is behaviour-changing). → **an
engage-step architecture decision (where grouping lives), not a dormant-build blocker.**

**F-4 — "reuse one scorer" vs the new four-note TYPES (the sharpest amendment-radar point).** The decoder's design
principle is *reuse `analyzeChord`'s cube, no second scorer* (spec §9). But the spec's two new four-note types (dim7,
mMaj7, G5) would extend that **shared production** catalogue → the **legacy** path's output moves too (not
byte-identical). So this sub-build **cannot** be "alongside, dormant." Resolution options: (a) extend the shared
catalogue → behaviour-changing for legacy, must gate/measure; (b) decoder-local listing → forks the scorer (violates
§9). **Note the spelling-PIN is separable from the new-types:** re-rooting the chosen candidate from tpc (consuming
`spellingview`) needs **no** new template — only *naming* dim7/mMaj7 as a distinct quality does. → Increment-C should
**split** into **C1 spelling-pin** (decoder-local, dormant) and **C2 new types** (touches the shared catalogue,
behaviour-changing, gated). Both are small (3.1 %).

**F-5 — bounded-context (G7) + dense-start config (F17).** `weightedPcView` is called with
`excludeLookAheadOnDenseStart=false` in the decoder; the F17 alignment with the live path and the selection-edge
bounded-context contract are **Step-E decisions** per the plan — not Step-0 blockers, recorded here.

**F-6 — tooling note (not a production matter).** `tools/decode_chord_corpus.py` has the **same unix-path bug F16 fixed
in `run_bach_preset.py`** (it passes `/c/s/MS/…` paths that fail under this session's `MSYS_NO_PATHCONV=1` —
`batch_analyze` reports "failed to load score"). The committed **gate** path (`run_bach_preset.py`) is unaffected; I
worked around it with a scratch driver using Windows-form paths. Flag for a tools-only follow-up (mirror the F16 fix into
the decode driver).

**Verdict:** the spec's L4 decomposition **still fits** the as-built L1–L3. No layer-architecture amendment is indicated
at Step 0. The two genuine open architecture decisions (F-3 grouping/section integration, F-4 new-types entry) are
**engage-step** questions the incremental method is designed to surface — neither blocks the dormant build steps.

---

## §4 — Deliverable: grounded increment sequence + first engage/no-go read

### Re-grounded increment sequence (amends the plan's provisional order)

The plan listed the **spelling-pin (Increment C) first**. The measurement says **re-order**: the dominant residual
(−13 pt at equal grain; 42 % thin / 41 % phantom / 60 % wrong-root) is the **unbuilt commit/inherit/abstain +
sufficiency gate (G1)**, *not* the spelling-pin (3.1 %, G4). This confirms the prior
`cc_layer4_residual_decomposition_report.md` verdict with the restored gate.

Each step below is **dormant / byte-identical** (decoder-only, no production consumer; corpus 53/24/53 unchanged) and
ends with a re-run of the §2 new-vs-legacy diagnostic:

1. **Step 1 — commit / inherit / abstain + sufficiency gate (G1, §5 step 4).** The phantom-root rule: a slice with
   < 3 independent chord-tones either **inherits** the prevailing chord (when consistent) or **abstains** ("uncertain",
   open question named) — never commits a new symbol. Targets the 42 % thin / 41 % phantom dominant residual. **This is
   the lever.** Re-measure dur-wt chord-root + the over-read rate.
2. **Step 2 — membership three-tier rule (G2) + spec plausibility check (G3, §5 step 3).** Replace the flat
   weak-OR-stepwise rule with the structure-first ladder; test template tones for embellishment behaviour (the true
   C-vs-Cadd9 discriminator). Re-measure NCT precision/recall (today 50.4 % / 34.5 %) + chord-root.
3. **Step 3 — confidence composite + open-question label (G6, §7).** Make "uncertain" honest (margin + sufficiency +
   membership-cleanliness; root/quality/note-membership label) — the Layer-5 hand-off contract.
4. **Step 4 — spelling-pin (Increment C1, G4, §5/§9).** Decoder-local, dormant; consume `spellingview.lineOfFifths`,
   re-root symmetric candidates from tpc deterministically (kills the class-(a) churn). Unit-test against the
   residual-verified cases (`bwv16.6 m9b4` C♯, `bwv179.6 m8b2` D♯, `bwv177.5 m4b2.5` D♯). Small but clean.

**Deferred to / decided at the engage step (behaviour-changing — gated, not dormant):** C2 new four-note types (G5,
F-4); bounded-context selection edge (G7, F-5); section-layer / L6 grouping integration (F-3); F17 dense-start alignment.

After Steps 1–4, run **Step M** (the full new-vs-legacy comparison, both presets) → the engage GO/NO-GO.

### First engage / no-go read

- **NO-GO to engage now.** The new per-slice path is **−15 pts behind legacy** on chord-root; engaging would regress the
  user-facing output (and class-(b) functional roots — the hard-stop). Do not switch `regionanalyzer.cpp` yet.
- **But this is NOT an architecture rethink.** The gap is dominated by a **spec-described, unbuilt mechanism** (G1
  inherit/abstain + sufficiency) that maps **directly** onto the measured 42 %/41 % thin/phantom residual. The per-slice
  architecture is sound: the unit fits the slicer (F-1), it shares L3's wired spine (F-2), and it is the spec's
  end-state.
- **Therefore: conditional GO on the architecture, with the increment ORDER amended** (build inherit/abstain FIRST,
  spelling-pin last), re-measuring at each step. Re-assess engagement at Step M: engage only if the new path is
  **equivalent-or-better** (zero new class-(b); class-(a) churn understood). The two engage-step architecture questions
  (F-3 grouping, F-4 new-types entry) are surfaced now so they are decided **before** the switch, not discovered during
  it — which is the point of going incremental.

---

## §5 — Stops / constraints honored
- **No production `src/composing/` source edit** (read-only + measurement). ✓
- No wiring; `regionanalyzer.cpp` chord seam untouched; decoder stays diagnostic-only (`--decode-chords` returns before
  `analyzeScore`). ✓
- No `upstream` push. ✓
- Artifacts: decode output `tools/corpus_decode_chord_step0/` + scratch driver + grading logs under `scratch_artifacts/`
  are **untracked/local**; this report is gitignored (`/cc_*.md`). The only commit this step created is the §0 doc
  commit `9ef7ff312a`. ✓

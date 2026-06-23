# Layer 3 — PER-SLICE ANALYSIS WITH CONTEXT — Design Document (⛔ SUPERSEDED 2026-06-21)

> **★ SUPERSEDED — do not use as the plan.** This draft treated "analysis" as ONE fat layer (key + chord + function
> + NCT) with sub-layers L3a/b/c. Per user (2026-06-21) the analysis half is **decomposed into single-responsibility
> layers**: **L3 key/mode → L4 chord symbol (+ non-chord tones) → L5 function → L6 grouping**, ordered by dependency
> (key/mode needs only the notes; it is the root). The key/mode-first ordering, the dependency argument, the
> research survey, and the Cowork correction (an earlier chord-symbol-first lean was wrong) are recorded in
> **`cowork_layer3_keymode_design.md`** (the live L3 design) and `cowork_target_architecture.md` §2. The still-valid
> content here — §0.1 scope/scale/incrementality/context-extension — has been carried into the key/mode doc (§0.2).
> Retained only for history.

# (superseded) Layer 3 — PER-SLICE ANALYSIS WITH CONTEXT

> Upstream-first sweep, layer 3, anchored to the ratified target (`cowork_target_architecture.md`): given the
> **constant-tonal-sonority slices** (layer 2, `changePointSlices`, built + validated) over the **note model**
> (layer 1), assign each slice its **harmonic interpretation with context** — key, chord, and chord-tone/NCT
> membership — so that grouping equal analyses (layer N) yields the harmonic reading. **This is the layer where
> analysis behavior CHANGES.**
>
> **No code until the user signs off (§9). Layer 1 + layer 2 frozen upstream; grouping (LN) downstream.**
>
> **★ Provenance (no-assume rule):** the as-is (§3) is from source reads this session of `regionanalyzer.cpp`
> (the `runPass1` analyze loop, L588–748) + prior reads of `chordanalyzer`/`harmonicfunctionlayer`/`scoring_model.md`
> /`layer_architecture_audit.md`, and the Contrapunctus/JNMR findings (`contrapunctus_findings.md`). Specifics not
> re-confirmed at source this session are marked `[verify]` for the layer-3 read-only audit.

## §0 — ★ The sequencing reality (read first — it defines what layer 3 *is*)
Layers 1 and 2 were **byte-identical / isolated**: we changed the note source and built an unused slicer, and
nothing in the analysis output moved. **Layer 3 is the opposite.** It is where the L2 slicer is finally **wired
in**, where the segment-first over-grab **dissolves**, and where the L1 tie-de-inflation **+3/+1/+1 oracle wobble
re-tunes**. So:

- **L3 BREAKS byte-identity by design.** The pipeline snapshot goldens *will* change; the validation shifts from
  "byte-identical" to **"oracle hold-or-improve"** (the per-event tiered oracle-root metric — which, unlike at L2,
  **applies here**) plus the BIR gate on **both presets** (Baroque + Jazz, no BIR-false regression — the CLAUDE.md
  hard stop). Golden refresh only after the output change is *verified correct*.
- **L3 is too big to build atomically.** It is three coupled sub-problems — key, chord, NCT membership — each a
  judgment. Building/auditing them in one step is the failure mode the sweep exists to avoid. §5 proposes a
  **sub-layer decomposition (L3a/L3b/L3c)**, each its own design → audit → build → measure increment, upstream-first
  *within* L3.
- **The un-ratified line.** The "constrained joint inference" re-grounding (held out of the canonical docs) is the
  *eventual* shape of L3's key/decision core, and the **gate-dissolution** (deferred refactor #2 → Stage 5) lives
  here too. **L3-core does NOT build either.** It establishes the per-slice-with-context substrate that is
  **compatible with** the joint decoder, and reuses the existing scoring oracle + gates per slice. Where a choice
  would commit to the un-ratified joint design, L3 stops and flags it (§7).

## §0.1 — ★ SCOPE, SCALE, INCREMENTALITY, CONTEXT-EXTENSION (user mandate 2026-06-21 — binding on L3 and the audit)
**Scope = ANY score opened in MuseScore — any size, any style.** This is the product intent, not an aspiration.
Tristan Act 1 is *in* scope, not out of it. The Baroque tuning is the current **calibration maturity**, NOT the
scope boundary. The architecture honors universality by construction: **the fact layers (L1 note model, L2 slices)
are style-agnostic and lossless** — correct on Tristan as on a Bach chorale — and **style-specificity lives ONLY in
L3's calibration** (presets / thresholds / gates / key model), **never in L3's structure.** L3 must analyze any
score *structurally* even where it cannot yet analyze it *accurately*; nothing in L3's shape may assume functional
diatonic tonality (cf. CLAUDE.md: structural entry conditions or preset overrides, never style-narrowing a shared
threshold).

> **★ THE WORKING UNIT IS A SELECTION, NOT THE WHOLE SCORE (user, corrected 2026-06-21).** In the **shipping**
> product the analyzer always works on a **defined part**: a single note/chord, or a user-selected run of measures
> (possibly partial). That selection is the initial working span; L1/L2/L3 operate on it and annotate it / drive the
> status bar. **Reading an entire score end-to-end is ONLY the non-shipping inferrer validation** (the 353-stem
> corpus run; Tristan-in-full). *Caveat on the current code:* `NoteModel::build(score)` today builds the **whole**
> score even when only a range is analyzed — so a selection in Tristan currently constructs the entire act's model.
> That is the waste R1/R3 target; the working unit must become the selection, not the score. **[verify]** the exact
> selection→range path at source in the audit.

Four hard requirements follow:

- **(R1) PERFORMANCE AT THE WORKING-SPAN (and full-score in validation).** Cost must scale with the **working span**
  (selection + extension), and the working span must **not default to the whole score**. The validation harness *does*
  run whole scores (an 80-minute act), so L1's `overlapping()`/range queries and L3's per-slice + context loops must
  be **indexed**, not O(N²) — invisible on a chorale, fatal on a full act. The audit pins the complexity, not assumes it.
- **(R2) INCREMENTAL RE-ANALYSIS — never re-analyze the whole score per edit.** An edit re-analyzes only the **dirty
  tick-span plus its bounded context margin**, reusing cached output elsewhere. Dirty-range invalidation, not a full
  pass. The bounded-context design is what makes this possible (local edit ⇒ local re-slice ⇒ local re-analysis) —
  a *second* reason beyond tractability to keep context bounded. **★ Tension:** the un-ratified **global-joint key
  decision works AGAINST R2** (a globally-integrated key lets a key-relevant edit ripple wide), a real cost to set
  against the joint decoder at the gated Stage 5.
- **(R3) THE WORKING SPAN IS EXTENSIBLE — context extension beyond the selection (HYBRID; user-agreed 2026-06-21).**
  A later layer routinely needs context *outside* the selection (key needs the prior cadence; an edge slice needs
  its neighbor for NCT). So the span must **grow on demand**, not be a fixed one-shot build. Mechanism = **hybrid**:
  a small cheap **fixed margin** for the common ±a-slice/beat cases, plus **lazy pull** (extend → re-decide → stop
  when the decision stabilizes or a hard cap is hit) for the rare long-range case (key). **As-is precedent (found at
  source, keyresolver.cpp:274–315):** the key resolver ALREADY does this hybrid — a **fixed backward** lookback
  (`LOOKBACK_BEATS=16` = 4 whole notes) + a **dynamic forward** lookahead that steps out until `confident`
  (`dynamicLookaheadConfidenceThreshold`) or `atMax` (`dynamicLookaheadMaxBeats`); the chord/region path adds a
  **carry-in walk** for notes sustained from before the start. **Gaps to fix in L3:** (a) it is **asymmetric** —
  only *forward* is lazy; *backward* is a fixed window and cannot reach a cadence > ~4 wholes back (key needs lazy
  backward too); (b) it is **scattered** per-consumer (key resolver / region carry-in / next-region lookahead), not
  one protocol — unify it on the slice grid. **The "how far / stop criterion" itself is deferred** to the
  chord-progression sub-layers (where temporal context actually breaks ties), per user; the existing
  `dynamicLookahead{ConfidenceThreshold,MaxBeats,StepBeats}` prefs are the concrete starting knob.
- **(R4) STYLE LIVES IN CALIBRATION, NOT STRUCTURE** (restated): L3's shape is style-blind; presets/thresholds carry
  style. **[verify]** the current edit-trigger / invalidation behavior at source (does today's pipeline re-run a
  region or the whole score on
  edit?) — the `regionanalyzer` `[startTick,endTick)` range is the substrate, but the UI invalidation path is
  unconfirmed.

## §1 — Intended role (the single responsibility)
**Decide, for each slice, the harmonic interpretation it carries — with look-around context — such that the
grouped result is the analysis.** Concretely, per slice: the prevailing **key / local tonicization**, the **chord**
(root + quality + inversion), and which of the slice's notes are **chord tones vs non-chord tones (NCT)**. It is
the layer that makes the **judgment layer 2 deliberately deferred**: *which slice boundaries are real chord
changes* (vs passing/neighbor/suspension embellishment within a held harmony). Its output feeds LN, which groups
adjacent equal analyses; the grouped output *is* the harmonic rhythm.

> **★ The defining hard problem (the dual of over-grab).** Today's segment-first analyzer **over-grabs**: a coarse
> region spans ≥2 chords and is forced to one. Per-slice analysis makes over-grab **structurally impossible** (a
> slice can't span a chord change — L2 guaranteed that). But the failure mode **flips**: analyzing each fine slice
> independently would **over-segment** (every passing tone → a spurious new chord). So L3's central task is the
> judgment that suppresses spurious chord changes — **NCT recognition + context** — turning a held harmony's many
> slices back into one chord. Over-grab and over-segmentation are the two errors; L3 is where the line between them
> is drawn correctly, with evidence, instead of by a coarse heuristic up front.

## §2 — Scope
**IN:** wiring the L2 slicer into the live pipeline; per-slice key/local-tonic, chord, and NCT-membership decisions
with a context window; the over-grab dissolution; producing per-slice analyses for LN to group.
**OUT (frozen or later):** the slice grid itself → L2 (frozen); the note model → L1 (frozen); **grouping/display of
equal analyses → LN** (separate, downstream — though L3 must be designed knowing LN groups its output); the
**full constrained-joint key decoder** and the **gate-layer dissolution into fitted weights** → un-ratified
Stage 5/6 (flagged in §7, **not built** in L3-core).

## §3 — What the code currently does (the as-is being replaced)
Analysis is **per coarse REGION** (the over-grabbing `greedyExpandSegmentation` boundaries + Pass-2/2b
sub-boundaries), not per slice. The per-region analyze loop (`regionanalyzer.cpp` `runPass1`, L588–748, verified
this session):
1. **Tone evidence:** `ebr::weightedPcView(noteModel, regionStart, regionEnd, …)` → a weighted **pitch-class**
   aggregate of the region (the L1-derived view; note the region can already span >1 chord).
2. **Key (per-region, local):** `kr::resolveKeyAndModeRanked(score, regionStart, …, prevKeyResult)` → ranked keys;
   the winner is `ranked.front()` — a **per-region argmax with hysteresis** (carries `prevKeyResult` forward). `[verify]`
   the resolver internals.
3. **Context inputs (greedy/local):** a `ChordTemporalContext` carrying stepwise-bass flags, a recent-roots window,
   the `regionMetricWeight`, and a **next-region lookahead** (`nextBassPc`, `nextRootPc` via `inferNextRootPc`).
4. **Chord (scoring oracle):** `chordAnalyzer->analyzeChord(tones, keyFifths, keyMode, &temporalCtx, prefs,
   &gateCtx)` → ranked candidates (the vertical-evidence scoring oracle; templates + bonuses; `scoring_model.md`).
5. **Winner selection (competition + gates):** `applyHarmonicFunction` (progression signals + winner) + the
   post-scoring **Gates A–L** (`PostScoringGateContext`). `[verify]` exact gate set on this path.
6. **Path commit:** a Stage-3.1 **beam-1** `decode::ChordPathDecoder` owns the path state and `commit()`s the
   winner — but it **computes no score** (analyzeChord + applyHarmonicFunction run upstream; the decoder is
   currently a byte-identical path-state holder, per `docs/decoder_design.md`).
7. **Then** Pass-2/2b sub-segmentation + Pass-3 merge (`coalesceShortSameRootRuns`/`absorbShortRegions`) — the
   chord-dependent merge that is the over-grab seam (mapped in the L2 audit).

So today: **decide spans (over-grab) → aggregate to weighted PCs → per-region key argmax → score one chord →
gate-correct → greedy-commit → merge.** The judgment is baked in *before* analysis and the unit is the coarse
region.

## §4 — What is missing or not appropriate
- **4.1 Per-region, not per-slice → over-grab is built in upstream.** The biggest single error lever (~45% on the
  canonical corpus). The fix is structural: analyze the L2 slices, not coarse regions.
- **4.2 Key is per-region local argmax + hysteresis — the wrong shape.** The measured key-axis arc (Stages 4a–4d)
  showed the relative-pair floor and the modulation gap are **structural ceilings of locality**, not tuning misses.
  Key is ~47–55% of charged error. Local feed-forward cannot reach it. `[verify]` the resolver, but the diagnosis
  is established.
- **4.3 No explicit NCT membership.** The region picks **one** chord and its non-chord tones are absorbed
  implicitly into the weighted-PC aggregate. Per-slice analysis **requires** an explicit chord-tone/NCT decision
  per note (a passing-tone slice must be recognized as NCT against the prevailing chord, not scored as a new
  chord). This is a **new first-class output** (cf. the JNMR-2024 chord-first + per-note membership approach).
- **4.4 "Decoding" is greedy beam-1 and scoreless.** The path decoder exists but holds state only; there is no real
  context decode (no beam, no look-around scoring) — context is the few greedy flags in `temporalCtx`.
- **4.5 The evidence is pre-aggregated to weighted pitch classes**, discarding the note set the slice carries
  (cf. L2's "slice identity is the note set, not the PC set"). NCT membership needs notes, not a PC histogram.
- **4.6 Gates A–L are post-hoc corrections** (load-bearing; deferred-refactor #2 dissolves them into fitted weights
  at Stage 5). Not L3-core's to dissolve — but L3 re-homes scoring per-slice and must not entrench them further.

## §5 — Target design (per-slice analysis with context) + the sub-layer decomposition
**Shape:** consume the L2 slices; for each slice decide `{key/local-tonic, chord(root,quality,inversion),
per-note NCT membership}` using a **bounded look-around context**; emit per-slice analyses; **LN groups adjacent
equal analyses** (over-grab dissolves; harmonic rhythm emerges). Reuse the existing **scoring oracle**
(`analyzeChord`) as the per-slice chord-evidence engine and the existing key resolver, but **re-homed to the slice
grid and given real context** rather than per-region argmax.

**★ Proposed sub-layer decomposition (built upstream-first WITHIN L3, each its own design→audit→build→measure):**

- **L3a — wire the slicer in (structural over-grab dissolution, minimal new judgment).** Replace the coarse-region
  loop with the slice grid: analyze each slice with the **existing** machinery (key + `analyzeChord` + gates), then
  group equal adjacent (a first, honest LN). *Expected oracle effect:* the **OVER-GRAB tier drops**; the
  **over-segmentation** failure mode (4.3 dual) **appears** and is *measured* — this increment's job is to expose
  its size, not yet fix it. This is the lowest-risk first cut and it isolates the structural change from the
  intelligence changes.
- **L3b — NCT / context to suppress over-segmentation.** Add explicit per-note chord-tone/NCT membership against a
  prevailing-harmony context window, so passing/neighbor/suspension slices stop spawning spurious chords. This is
  the chord-axis intelligence; the chord tier is near-ceiling already, so the target is to **recover** what L3a's
  fragmentation costs and net-improve via correct embellishment handling. (JNMR-2024 chord-first + membership;
  Contrapunctus per-beat with a small candidate vocabulary.)
- **L3c — key with context (the path), attacking the dominant tier.** Replace per-slice/region key argmax with a
  context-aware key decision (a key path / look-around). This is where the **KEY tier** (the ~50% lever) is
  attacked and where the **+3/+1/+1 L1 wobble re-tunes**. **This is also where the un-ratified joint-inference
  pressure is highest** — L3c builds the *local-context* form and **stops at the boundary of the full joint
  decoder** (§7), which remains gated.

**Invariants for L3 (all sub-steps):**
- **Consumes L2 slices unchanged** (frozen upstream); reads the **note set** per slice (`overlapping`) for NCT, not
  only the weighted-PC view.
- **Annotate, don't destroy:** per-slice analyses are added; the slices + note model remain the source of truth;
  grouping is LN's non-destructive view (the L2 principle, carried forward).
- **No new over-grab:** L3 never re-introduces a "decide a coarse span before analysis" step; spans emerge from
  grouping equal per-slice analyses.
- **Reuse, don't rebuild, the scoring oracle + key resolver** where they are correct; change the **unit** (slice)
  and the **context** (look-around), not the vertical-evidence templates (those are near-ceiling).

## §6 — Correctness oracle / metric (this layer MOVES the numbers)
Unlike L1/L2, L3 changes analysis output, so the **per-event tiered oracle-root metric is the gate** (the standing
metric tool): the target is to **reduce charged error**, tier-attributed — primarily **OVER-GRAB** (L3a) and
**KEY** (L3c), with **CHORD-ID** held near its ceiling (L3b must not regress it). Each sub-step:
- reports the oracle delta **by tier**, on **both presets** (Baroque + Jazz) — any **BIR-false increase in either
  preset is a hard stop** (CLAUDE.md gate policy); the 57/23/57 identity sets are the reference;
- refreshes the **pipeline snapshot goldens** *only* after the output change is verified correct (the
  `--update-goldens` discipline), and re-runs both test suites;
- carries **full branch coverage of the new code** (the standing coverage rule) + the L2-style corpus property
  checks where applicable;
- expects and **explains** the L1 +3/+1/+1 re-tune (it was ratified as "re-tunes at L3").

## §7 — Open questions (for the audit / sign-off — these are the real decisions)
1. **Sub-layer ordering** (§5): is L3a→L3b→L3c (structure → chord/NCT → key) the right order? *Lean: yes* — land
   the structural over-grab dissolution first (measurable, low-risk), then recover fragmentation (NCT), then attack
   key. Alternative: key-context first (key is the dominant error). Trade-off: key-first changes the hardest thing
   before the structure is stable.
2. **How much context, and in what form** — a fixed look-around window? the existing `ChordPathDecoder` elevated to
   actually score (beam search over slice analyses)? a key-path model? This is the seam with the **un-ratified
   joint inference**; L3-core must pick the *minimal* context that works and flag where more would cross into the
   gated joint design.
3. **NCT vocabulary + membership model** — passing/neighbor/suspension/anticipation/pedal as an explicit small
   vocabulary with per-note membership (JNMR-2024), or a lighter chord-tone/non-chord-tone binary first? *Lean:
   start binary (chord-tone vs not) in L3b, refine the NCT vocabulary later.*
4. **Is LN (grouping) part of L3 or its own layer?** *Lean: separate* (per the target), but L3a must ship a minimal
   grouping to be measurable. Decide whether the full LN (display/harmonic-rhythm) is a later layer.
5. **Key↔chord coupling / ordering** — feed-forward (key→chord, as today) vs the joint decision the re-grounding
   argues for. *L3-core stays feed-forward with context; the joint decision is the gated Stage-5 step.* Confirm
   this boundary is where the user wants it.
6. **Gates A–L** — reuse per-slice as-is in L3 (their dissolution is deferred Stage 5), confirmed? Do not entrench.
7. **Snapshot-golden + re-baseline policy** — L3 deliberately re-baselines; confirm the per-sub-step golden-refresh
   + dual-preset BIR gate is the acceptance bar.

## §8 — What gets verified in the read-only audit (before any L3 code)
The `[verify]` items: the exact `resolveKeyAndModeRanked` behavior + hysteresis; the precise Gate A–L set on the
live path and which are chord- vs key- vs progression-dependent; how `analyzeChord` consumes `temporalCtx` +
lookahead (so per-slice context wiring is grounded); the `ChordPathDecoder` commit semantics; where the merge
(`coalesce`/`absorb`) sits relative to grouping; and a **measurement** of the §1 dual — size the over-segmentation
that L3a will expose (e.g. a proxy: how many slices per current region; how many are single-note/NCT). The audit
also pins which existing pieces **move to LN** vs are deleted.
Plus the §0.1 requirements: **(R1)** pin the actual complexity of `overlapping()` / range queries and the
per-slice + context loops (indexed vs O(N²)) and whether they hold at full-act scale; **(R2)** map the current
edit-trigger / invalidation path — does the live pipeline re-analyze a `[startTick,endTick)` region or the whole
score on an edit? — so the incremental dirty-range + context-margin design is grounded in what exists.

## §9 — Sign-off
- [ ] **Role (§1):** L3 = per-slice analysis with context (key/chord/NCT), making the "which boundary is a real
      chord change" judgment L2 deferred; output grouped by LN.
- [ ] **Sequencing (§0):** L3 **breaks byte-identity by design**; validated by the oracle metric + dual-preset BIR,
      not byte-identity; built as **sub-layers L3a→L3b→L3c** (or an agreed reorder).
- [ ] **As-is (§3)** accepted as the baseline being replaced.
- [ ] **Gaps (§4) / Target (§5)** approved / amended: ____________________
- [ ] **The un-ratified boundary (§0/§7):** L3-core builds the per-slice-with-context substrate and **stops** at
      the full joint key decoder + gate dissolution (gated Stage 5/6). Confirm this is the right line.
- [ ] Proceed to the **read-only layer-3 audit** (§8) before any code.

*Nothing in layer 3 is built until signed. Layers 1 + 2 frozen upstream; LN downstream; the un-ratified
joint-inference + gate-dissolution remain held (Stage 5/6).*

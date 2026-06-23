# Cowork audit — CONSOLIDATED OBLIGATION MAP (phase-1 synthesis)

> **★ RE-ASSESSED 2026-06-20 (see `cowork_architecture_reassessment.md`) — supersedes parts of §B/§C/§E below.**
> After CC's anchor dossier (union-recompute ABANDONED — production's segmentation-based embellishment
> discrimination is correct, source-verified) + the Contrapunctus/papers study (external SOTA convergence), the
> plan changed:
> - **Anchor (the old "biggest structural lever" / S1-S2 segmentation recompute): ABANDONED** — it was a
>   misdiagnosis; the chord-inherited-from-clean-slice is correct, and the union-recompute is net oracle-negative.
>   Genuine residual is tiny (2/25, *under*-segmentation) → per-case scoring, not a re-layer.
> - **C2 gate-dissolution: DEFERRED** — selection layer is saturated (us ~24%/1.7%; external: Viterbi/refiguring/
>   window all rejected), so dissolving the gates is code-health, not accuracy.
> - **X2 chord↔key "circularity": RE-CLASSIFIED** — not a defect; key-first/chord-against-key is the correct
>   design, resolved by key *quality* (K1), not re-layering.
> - **X1: folded into K1** (it silences cadence evidence exactly where K1 needs it).
> - **★ NEW meta-finding: BIR is a misleading proxy** (scored 5 oracle-root regressions as fixes) → an
>   **oracle-root (+ tiered) metric is now the precondition** before any inference work.
> - **Revised order:** metric-first → **K1 cadence precision (the #1 lever, validated both sides)** → K3 soft+
>   calibration → [learned chord-label re-ranker = Stage-5+ roadmap]. The KEY axis is where the leverage is;
>   the chord axis is near its rule-based ceiling. The A-section (K1/K2/K3) below stands and is now the priority.


> **★ PROVENANCE (user, 2026-06-17 — "redo wherever you audited memory and not truth"):** This map separates
> two kinds of claim. **TRUTH = committed-object source reads done THIS session** (the mechanisms, structure,
> code logic, decomposition seams) — these stand. **PROVISIONAL = any NUMBER or any "measured (B/B2/4b/4c/4d/
> functional-residual/J-key-*)" finding carried from MEMORY of prior investigations** — these are NOT verified,
> are error-prone, and must be re-measured by CC's fresh per-layer empirical audit before they are trusted.
> Memory already produced THREE errors, all corrected by fresh source reads: **(1)** anchor "~44% pin-wrong" →
> CC's measured **27.6%** (I'd mis-cited a hard-constraint-on-contested-cases metric as piece accuracy);
> **(2)** detector fires on "I→V" → actually **V/V→V** (I→V is an ascending fifth, excluded — verified
> `cadencekeyanchor.cpp:95`); **(3)** disambiguation "inert on tonic-present-both" → only on the
> **both-complete-triad** sub-floor (verified `keymodeanalyzer.cpp:455-487`). **Treat every `[prov]`-tagged
> number below as pending CC measurement.** The map's STRUCTURE (mechanisms + the two-track verdict) is
> source-grounded and held by CC's reconciliation so far; the QUANTITIES are not.

> **★ SEQUENCING GATE (user, 2026-06-17): STRUCTURAL fixes BEFORE inference.** This audit is QA on the
> layers + the overall architecture. Its findings are two kinds, fixed in STRICT ORDER:
> **(1) STRUCTURAL — "wrong place / missing place"** (a responsibility smeared/duplicated, a layer to split or
> merge, a missing proper layer something is compensating for) = **the C-obligations (S1–S3) + the
> decomposition flags + X2/X3.** These are fixed FIRST — they ARE "getting the architecture right," the
> precondition. **(2) CORRECTNESS — "right place, wrong output"** = the **A/B obligations (K*, C1–C4)** —
> deferred to AFTER the structure is correct. **Never tune a K1/C1 correctness fix while a responsibility is
> still misplaced** (it would tune inference on a structure about to change). So: finish the audit → phase-2
> architecture review → **fix the structural obligations (architecture phase)** → THEN inference correctness
> (on the corrected architecture).

> Synthesis of the per-layer independent audits (`cowork_audit_*.md`). **Read-only — obligations, not fixes.**
> North star: best = CORRECT inference (vs the DCML/music21 oracle). To be reconciled with CC's primary
> audits, then fed into phase-2 (architecture review) and the eventual inference work.
> **Coverage: PHASE-1 COMPLETE — all ~19 layers audited** (key axis ×6, chord axis ×5, regionanalyzer, +
> the P3/P4 completeness pass: sectionanalyzer-KeyArea/stabilization, tonicizationlabeler, harmonicsegmenter,
> tone-collection, formatters, voicing, diagnose, mode-presets — `cowork_audit_remaining_layers.md`). The
> orchestration/output layers added no obligation that changes the two-track verdict; their findings are
> folded in below (Layer-B stabilization → K3; KeyArea ≥0.8 gate → X1; tonicization↔modulation → S1;
> the duplicated key-collection primitive → S3; mode-prior presets → K3 calibration).

## A. KEY-AXIS obligations — converge to 3 roots (remedy: calibration/learned + the joint combination)
- **K1 [correctness · key-axis · the ROOT] Cadence-detection precision wall.** The leading-tone test is
  structurally vacuous (the dominant's "leading tone" is just its major third, present in every major triad)
  → fires on **I→IV** (subdominant, 72% spurious) and **V/V→V** (chromatic applied dominant). *(CORRECTED
  vs CC's audit: NOT I→V — diatonic I→V is an ascending fifth, structurally excluded by the descending-fifth
  test; verified at source `cadencekeyanchor.cpp:95`.)* **Anchor accuracy vs DCML = 72.4% correct / 27.6%
  pin-wrong** piece-level (CC fresh measurement; my earlier "~44%" was a mis-cited hard-constraint-on-
  contested-cases metric, NOT piece accuracy — corrected). **Leading residual = the dominant V/V→V over-read
  (9.8%) > the relative-pair flip (6.4%)** the anchor was built to fix. Partial-sig degrades sharply (58.9%
  vs 75.2%) → confirms the `chromaticLeadingTone` mis-fire. **Feeds 3 layers:** anchor, modulation detector, joint-decision non-chorale regressions.
  **Single highest-leverage fix.** Behavior-changing; needs better key-agnostic discrimination / constrained-
  joint-soft / calibration — not a local patch.
  - **Modulation detector reconciliation (CC-MEASURED, audit #2 — `[prov]` RETIRED):** precision **47.0%** /
    recall **33.4%** CONFIRMED (region; 53.6%/27.6% span/segment). **Self-confirmation CONFIRMED + quantified:
    81.8%** of FP spans (157/192) have NO independent confirming cadence (gate non-discriminating on the FP
    side; TP 99.1% confirmed). FP composition: subdominant 24.5% + dominant 17.7% = **42.2% cadence-wall**
    (100% subdom = literal I→IV, 100% dom = V/V→V — corrected-K1 reproduced), but **foreign 32.3% is the
    LARGEST bucket** + relative 19.3% → **K1 clears only ~42% of modulation FPs; the majority is
    foreign/relative/over-extension.**
  - **NEW obligation K1b [correctness · key-axis · IN-LAYER fixable]: establishment over-extension** — 18.2%
    of FP spans have a genuine cadence but over-grab a brief tonicization into a sustained span via the loose
    `kPitchTolerance=2` (verified `localmodulationdetector.cpp:46,103-111`) + nearest-cadence assignment.
    Distinct from the upstream cadence wall → fixable IN-LAYER (tolerance/segmentation), NOT deferred to K1.
- **K2 [correctness · key-axis · structural] Note-scorer relative-pair limit** (`keymodeanalyzer`). Relatives
  share the collection → notes can't fully separate them. **CORRECTED at source (`keymodeanalyzer.cpp:455-487`):
  `applyPairwiseDisambiguation` is NOT inert on tonic-present-both wholesale** — clauses 3/4 DO resolve the
  sub-case where both have their tonic but one triad is INCOMPLETE (the Em/G opening: E-G-B completes Em, G
  lacks its 5th). It is inert specifically on the **both-tonic-present AND both-complete-triad** floor — the
  genuinely-ambiguous case. **CC-MEASURED, audit #4 — `[prov]` RETIRED + REFRAMED:** note-only relative-pair
  error **~32%** (declared hint recovers ~10pp → ~21%); prov "~1383 flips" → **2467 change / 1631
  declared-rescued** (Baroque, corrected parser). **★ The floor is NOT the both-complete-triad symmetric tie
  (only ~4%) — it is MISSING LOCAL EVIDENCE:** TONIC_ASYM (~37%) + NEITHER (~43%) = **~80% of the error are
  regions where the local notes carry NO decisive relative triad at all.** The disambiguation resolves the
  one-incomplete-triad band (~16%, ~73% toward DCML). So K2 is a **missing-evidence floor → resolvable ONLY by
  external evidence (K3 SOFT integration + K1 cadence), NOT reweightable here** — this is WHY K3's soft
  integration is the lever. **21-mode mis-win DOWNGRADED to ~0.1% (contained by modePrior + family selection)
  — a NON-problem; do NOT "fix" it** (my "richness risk" was overstated). Dorian/partial-sig wall confirmed
  (same ~17%/56 stems as K3). *(My "both-complete-triad floor" framing — corrected by CC's measurement.)*
- **K3 [correctness · key-axis · the SYNTHESIS] Joint decision** (`jointkeydecision`). **CC-MEASURED, audit #3
  — `[prov]` RETIRED, all reproduced** (producer verified byte-unchanged since `5fee657578`): soft re-rank WINS
  **+3.80/+3.50/+12.24 pp; S2 −140/−96/−1706** (exact); home-fifths HARD pin UNSAFE **17.0/17.0/17.2%, 56
  stems** (exact); candidate chord⊆key constraint 14% would-prune-correct (→ correctly soft). **★ The scoped
  JOINT SEARCH is INERT — strengthened:** joint−soft = **−0.04/−0.14/−0.06 pp**, moving only **0.16–0.29% of
  regions (17/26/33), net slightly NEGATIVE on S2.** → **The constrained-joint combination's entire value is
  its SOFT broad-evidence integration, NOT the lattice search (META-PRINCIPLE confirmed by measurement).** The
  single most decision-relevant result: **the eventual key-axis lever is soft-evidence QUALITY + CALIBRATION,
  not a fancier joint search.** *(Definition note: coupled-core measures ~21–24% now vs the original sizing
  ~13.5% — the known structural-proxy-vs-oracle over-count, not a new error; reconcile the definition, no
  behavior change. Phase-2: the working-tree B2 guard back-references this layer's `jointKeyWiringEnabled()` —
  a modulation→joint flag coupling.)* Home-pair soft-demotion is not separably safe
  (redux) → calibration / a confident-contradiction signal / learned. The active `keyresolver` hysteresis =
  old local-greedy entrenchment the joint decode replaces.

## B. CHORD-AXIS obligations — healthy oracle; remedy: competition rules + gate-dissolution
- **C1 [correctness · chord-axis · rule-reachable] Competition wrong-winner selection**
  (`harmonicfunctionlayer`). **CC-MEASURED, audit #5 — `[prov]` RETIRED + CORRECTED:** the functional/vertical
  split at HEAD is **91.0% functional / 9.0% vertical** (root_err 2365 = all_differ 2153 + music21-agree 212;
  reproduced + matches committed STATUS.md "95.2/4.8→91.0/9.0"). **My `[prov] 95.2/4.8` was the OLD buggy-parser
  number; corrected-at-HEAD = 91.0/9.0** (vertical doubled but still a clear minority; music21 independently
  agrees with our root on 94% of the residual). **★ The chord-axis-"healthy" verdict HOLDS** — ~91% of root
  errors are downstream (competition/defensible-ambiguity), not vertical. The functional errors are graded
  largely **rule-reachable** (hand-buildable). Risk: the heuristic-accretion complexity. **★ CC-MEASURED, audit
  #6 — RE-ATTRIBUTED (the main result):** of the 2153 functional residual, the COMPETITION layer owns only
  **~24% (~509)**; the rest routes elsewhere — **ROOT_ABSENT 38.7% → the floor** (reserved), **HELD 37.7% →
  SEGMENTATION over-segmentation (S1/S2 — the BIGGEST single driver, STRUCTURAL/fix-first)**, ROOT_PRESENT 16%
  + CAD64 7.6% = competition. **Pure-rerank is only ~1.7% (36 regions)** — most ROOT_PRESENT cases need a
  candidate never surfaced → **FUNCTIONAL RULES, not re-weights** (music21 agrees with US, not DCML). Top
  wrong-winner patterns (the actionable list): **cadential-6-4 (~184, largest)**, viio↔V7 share-tone (~50),
  applied-target labeling (~50, Stage-6), bass-anchoring bias (216/345 root on the bass while DCML roots an
  upper voice). **So the chord-axis hand-buildable obligation is SMALLER + more specific than I had it (~24%,
  functional rules led by cadential-6-4); the BIGGEST chord lever is the STRUCTURAL segmentation fix (S1) —
  fix-first.** *(Decomposition CORRECTED: this layer is 2-way not 3-way — progression-scoring + competition;
  function/degree is delegated to `buildChordResult` `chordanalyzer.cpp:952`, verified; + it marshals gateCtx
  for the gate layer.)*
- **C2 [architecture · chord-axis] Post-scoring compensation cluster → DISSOLUTION** (`postscoringgates` A–L +
  `chordpostpasses` + `sparsechordrefinement`). These are CONTEXT PATCHES (next-region/key/bass) for what the
  local competition got wrong → the refactor-#2 gate-dissolution target; **chord-joint is TRACTABLE** (the
  gates already work). Baroque-calibrated → Jazz-generalization concern.
- **C3 [correctness FLOOR · reserved] Symmetric dim7/aug root** (`chordanalyzer` oracle). pc-undefined by
  construction → the reserved learned-emission slice; not hand-buildable. **CC-CORRECTED: my "~53% Baroque"
  was a GATE-CASE stat (53% of Baroque BIR=false cases, 30/57), NOT corpus-wide** — corpus-wide symmetric
  sonorities are only **2.5% of regions** (concentrated in the vertical-fixable 28.8% bucket → the truly-
  vertical-fixable headroom is <9%). **fully-dim7 {0,3,6,9} is DERIVED** (dim triad + key-gated
  `dim7CharacteristicBonus` rotation-selector), not a template — and that rotation-selector **DEFINES the
  symmetric-dim7 root by reading the key** → a deeper chord↔key coupling (X2 broadened: the "vertical" oracle
  reads the key in TWO terms). C4 jazz-vocab gap real but UNMEASURABLE read-only (the GT "Jazz corpus" is
  Bach-under-Jazz-preset; real jazz `.mscz` won't load in standalone batch_analyze) — flagged.
- **C4 [completeness · chord-axis · jazz] Oracle vocabulary** = 17 tertian/sus/power; no extended/altered
  jazz harmony.

## C. STRUCTURAL obligations (different in kind — refactors, mostly behavior-sensitive → deferred)
- **S1 Region Pass triplication + SEGMENTATION = the biggest chord-axis residual driver** (`regionanalyzer`
  Pass 1/2/2b "keep in sync") → de-duplicate; behavior-sensitive. **★ Elevated (audit #6): over-segmentation
  is 37.7% of the functional residual — the single largest chord-axis lever, and STRUCTURAL → fix-FIRST per
  the sequencing gate (higher-value than the competition rules).**
- **S2 Chord-identity ≠ final-region** (Pass-3 merge changes tones after chord computed → broke re-emission).
  The chord layer's output isn't a clean function of its region. Deep re-layering target.
- **S3 Decomposition flags:** shared cadence-detection primitive (anchor + modulation consumers);
  `harmonicfunctionlayer` = **2 jobs (progression/temporal-scoring + competition) — CC-CORRECTED from my "3";
  function/degree is delegated to `buildChordResult`, a different layer** (+ it marshals gateCtx for the gates);
  two cadence detectors
  (inference vs display); two key-decision paths (active resolver + dormant joint → migration); **a duplicated
  key-collection/pc primitive re-implemented across ≥4 layers** (cadencekeyanchor / localmodulationdetector /
  jointkeydecision / tonicizationlabeler) → extract one shared primitive.

## D. CROSS-CUTTING findings (architecture-level, for phase-2)
- **X1 [correctness] The ≥0.8 confidence-gate blind spot.** `hasAssertiveKeyConfidence` silences cadence/pivot
  detection (`sectioncadencedetection`), KeyArea grouping, and the old detector — **on exactly the uncertain
  regions that most need analysis.** Systematic.
- **X2 The chord↔key circularity.** The oracle's diatonic-root tiebreak + `sparsechordrefinement` read the
  key; the key reads the chords. Recurring coupling (the re-emission/2-pass freeze manages it).
- **X3 The UNIFYING diagnosis: both axes are "local decision needs CONTEXT."** Gates (chord) and cadence/
  relative-pair walls (key) are the same root → the constrained-joint architecture is right for BOTH,
  re-derived bottom-up. Chord-joint tractable; key-joint walled on K1 (cadence precision).

## E. The two-track remedy (the actionable verdict for the eventual inference work)
- **Chord-axis track = hand-buildable:** competition-rule completion (C1) + gate-dissolution (C2); floor → B.
- **Key-axis track = SOFT-EVIDENCE QUALITY + CALIBRATION (NOT a joint search — measured inert, K3):** fix K1
  (cadence precision) FIRST (highest leverage, feeds 3 layers; clears ~42% of modulation FPs + the K1b
  in-layer over-extension covers more) → then the joint combination's SOFT integration (K3) resolves K2;
  calibration + possibly a learned emission for the partial-sig / dim7 floors. **NOT hand-buildable rules,
  and NOT a fancier lattice/search** (the scoped joint moves <0.3% of regions, net negative — CC-measured).
- Structural (S1–S3) + cross-cutting (X1–X3) feed the **phase-2 architecture review** (decomposition +
  interactions), which uses this map.

## Reconciliation status
Per-layer reconciliation vs CC's fresh measurement (agreement hardens, divergence corrects). **★ KEY AXIS
CLOSED — 4/19 layers reconciled:** **cadencekeyanchor** (CC corrected 2 remembered: 44%→27.6%, I→V→V/V→V),
**localmodulationdetector** (confirmed 47/33; self-conf 81.8%; +K1b over-extension), **jointkeydecision**
(confirmed ALL; joint-search-inert / soft-is-the-lever strengthened), **keymodeanalyzer** (confirmed my
source-correction + REFRAMED: floor is missing-evidence ~80% not symmetric-tie ~4%; 21-mode downgraded to
~0.1% non-problem). **The key-axis CONVERGENCE is now measurement-grounded across all 4:** the resolution is
the joint SOFT integration (K3, the measured lever) + upstream cadence precision (K1) — NOT per-layer
reweighting/search. **5/19 reconciled — chord-oracle (#5) added:** functional/vertical CORRECTED 95.2/4.8→
**91.0/9.0** (my stale pre-correction number; **verdict HOLDS** — 91% functional, oracle healthy); symmetric
~53% was a gate-case stat (corpus-wide 2.5%); X2 broadened. **6/19 reconciled — competition layer (#6) added:** RE-ATTRIBUTED the 2153 residual — competition owns only
~24%, **segmentation 37.7% (the biggest driver, S1, structural) + floor 38.7%** — so the chord-axis
hand-buildable obligation is smaller/more-specific (functional rules, cadential-6-4 led) and the biggest chord
lever is the STRUCTURAL segmentation fix; decomposition CORRECTED to 2-way. **Track record: CC corrected
5 of my remembered/structural claims (44%, 95.2%, symmetric-scope, 21-mode, 3-way→2-way) + confirmed/sharpened
the rest — the structure/verdicts held every time, the quantities/attributions did NOT.** **6 of the 6
high-value layers (key axis ×4, chord oracle, competition) now reconciled.** Remaining: the P3/P4
orchestration/output (lower obligation; the S-numbers). **Next: P3/P4 quick reconcile, then PHASE-2 — where
the structural "wrong place/missing place" obligations (now incl. segmentation as the biggest chord lever)
consolidate into the fix-first architecture work.**

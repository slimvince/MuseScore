# Combined Layer Audit — Plan (Cowork + CC)

> **Read-only acceptance review of the now-layered architecture.** The pure-byte-identical splits are done
> (commits `41f7c65f63` / `ed4b462021` / `2024f2951e` / `a03c2493bb` + the justified cohesive skips), so each
> layer is physically separable and can be audited in isolation. **This is the deferred back-half acceptance
> review** (handoff standing method). **No code changes — findings only.** The output is a prioritized
> **obligation map** that becomes the to-do list for when inference-improvement work reopens *on the correct
> architecture*. The "no fixing/improving inferring — refactoring only" rule still holds: the audit produces
> obligations, it does not implement them.
>
> **★ NORTH STAR (user, 2026-06-17): the goal is the BEST possible inference, where BEST = CORRECT.** Every
> per-layer obligation is judged against the **true analysis** — the DCML / music21 ground-truth oracle where
> the layer's output is checkable — NOT against whether it passes a proxy gate (BIR / rn_agree). A layer can
> pass the gate and still be WRONG on cases the gate never sees; those are precisely the obligations we want.
> Keep the established metric discipline: the oracle is the correctness standard (never game a proxy), and
> **separate genuine incorrectness from convention-boundary ambiguity** (cases where analysts themselves
> disagree = the honest floor, not a fixable error).

---

## §1 — Two phases (order matters BETWEEN phases, not within phase 1)

- **Phase 1 — per-layer isolation audits.** Each layer audited alone: state its single responsibility, audit
  correctness + completeness against THAT responsibility only (inputs assumed correct, consumers ignored),
  pin gaps as that layer's obligations. Order within phase 1 is pure prioritization (each audit is
  independent) — sequenced by value below, but any order is valid.
- **Phase 2 — architecture review.** AFTER phase 1, using its accumulated findings: are these the *right*
  layers, is any responsibility split / duplicated / misplaced across layers, and do the layers depend +
  compose correctly (feed-forward vs circular, the seams, the bolt-ons). Phase 1's depth feeds phase 2.

## §2 — Division of labor (USE CC MAXIMALLY)

**CC = primary auditor (the workhorse).** CC has fresh authoritative source access + can build/run, so CC does:
- the deep source read of the full layer + **data-flow / call-site / dependency tracing**;
- the **EMPIRICAL probe** — build the layer, feed it real + enumerated inputs, observe outputs, test the
  cases its responsibility implies (the half Cowork *cannot* do — the corpus/build is CC's);
- the primary per-layer audit dossier (responsibility, correctness, completeness, gaps), committed/reported.

**Cowork = independent second opinion + architecture judgment (the cross-check + context).** For each layer
Cowork independently assesses it against the **committed object** + the **bigger architecture context CC
lacks**, then reconciles with CC's dossier:
- Is the layer's stated responsibility the *right* contract for the target architecture?
- Does each gap actually *matter* for the inference priority (key-axis accuracy), and is its fix
  behavior-changing (→ deferred) or structural?
- Agreement → high-confidence obligation; disagreement → a real ambiguity to resolve (the harmonicsegmenter /
  vtest pattern — two independent paths).
Cowork **leads phase 2** (needs the bigger context); CC supports phase 2 empirically (dependency graphs,
cross-layer data-flow, probing suspected circularities).

**Per-layer workflow:** CC primary-audits a layer → reports (dossier; if it writes a probe, commit it
locally) → Cowork independent-second-opinions (committed-object + context) → reconcile → **pin the layer's
obligations** in the running obligation map → next layer.

## §3 — Per-layer audit method (what each audit produces)

For one layer:
1. **Responsibility (the contract):** one sentence — its inputs, its single job, its output. If it has *more
   than one* responsibility, that itself is a phase-2 finding (note + continue).
2. **Correctness (vs the TRUE analysis):** on valid inputs, does it produce the **correct** output — judged
   against the DCML / music21 ground-truth oracle where the output is checkable, not against a proxy gate? CC
   traces the logic + empirically tests against the oracle. Pin every case where the output is WRONG vs truth
   (distinguish a genuine error from convention-boundary ambiguity — the latter is the honest floor, noted
   but not a fixable obligation).
3. **Completeness (correctly, vs the case space):** does it handle *all* the cases its responsibility
   implies, **correctly**? CC **enumerates** the case space (all cadence types / chord qualities / key
   relationships) and tests coverage against the oracle. Pin every case it mis-handles or omits — this is
   where most obligations live (e.g. the cadence anchor's I→IV/I→V leading-tone blind spot = a correctness
   gap to formalize here). A case passing the existing gate but WRONG vs the true analysis is still an
   obligation.
4. **Gaps → obligations:** each gap tagged: `[correctness]` vs `[completeness]`; `[priority: key-axis /
   chord-axis / peripheral]`; `[fix: structural (poss. now) / behavior-changing (deferred to inference
   reopen)]`. Inputs-assumed-correct and consumers-ignored — interaction gaps are phase-2, not here.

## §4 — Layer inventory + priority sequence (phase 1)

Sequenced by value — the **key-axis accuracy bottleneck first** (its obligations feed the stated priority);
within a group, any order. ~19 TUs.

**P1 — key-axis evidence + decision (the bottleneck + the priority):**
`cadencekeyanchor.cpp` (cadence detection + key anchor — the recurring precision wall) · `sectioncadence
detection.cpp` (section cadence/pivot) · `localmodulationdetector.cpp` (modulation spans) ·
`keymodeanalyzer.cpp` residual (the mode-data + scorer library: MODES/CHARACTERISTIC/score*/pairwise-
disambiguation/resolveToFifths) · `keyresolver.cpp` (resolveKeyAndModeRanked + hysteresis) ·
`jointkeydecision.cpp` (the dormant constrained-joint decision).

**P2 — chord axis (foundational, central to all downstream):**
`chordanalyzer.cpp` residual (the vertical oracle: templates + scoring + basisIndep + buildChordResult) ·
`harmonicfunctionlayer.cpp` (competition / ranking / migrated bonuses) · `postscoringgates.cpp` (gates A–L)
· `chordpostpasses.cpp` (Iter-86/91 pedal) · `sparsechordrefinement.cpp`.

**P3 — segmentation / region / section orchestration:**
`harmonicsegmenter.cpp` (greedyExpandSegmentation) · `regionanalyzer.cpp` (the multi-pass Pass-1/2/2b/3
pipeline — note its known triplication is a phase-2 dependency/structure finding) · `regiontonecollector.cpp`
+ `regiontoneprimitives.cpp` (tone collection) · `sectionanalyzer.cpp` residual (analyzeSection /
stabilization / KeyArea).

**P4 — output / peripheral:**
`chordsymbolformatter.cpp` · `chordvoicing.cpp` · `chorddiagnose.cpp` · `tonicizationlabeler.cpp` ·
`keymodeformatting.cpp` · `modepriorpresets.cpp`.

## §5 — Phase 2: architecture review (Cowork-led, CC-supported)

Using the phase-1 obligation map, audit the COMPOSITION:
- **Decomposition:** are these the right layers? Single-responsibility each (phase-1 flagged any with >1)?
  Any responsibility **split across** layers (e.g. `buildChordResult` shared oracle/gate infra; the
  triplicated diatonic-scale tables; cadence logic in both `cadencekeyanchor` and `sectioncadencedetection`)
  or a layer that should be **merged/split** differently?
- **Interactions / dependencies:** does the data flow feed-forward correctly, or are there **circularities**
  (the chord↔key dependency; the joint-decision 2-pass; the `regionanalyzer` Pass triplication)? Is the
  **post-scoring gate layer** a real layer or compensation for non-jointness (the deferred dissolution)? Are
  the seams (the headers) the right contracts?
- **Against the target** (`architecture_joint_inference.md`): where does the current layering match the
  constrained-joint target, and where does it diverge (the deferred gate-dissolution, the bolt-on wiring)?
- **Output:** the architecture-level obligations + a verdict on the deferred structural refactors (gate
  dissolution; any re-layering), feeding the eventual inference-on-correct-architecture work.

## §6 — Deliverable + constraints
- **Output:** a consolidated, prioritized **obligation map** (per-layer P1–P4 + architecture) — each
  obligation tagged priority + **STRUCTURAL ("wrong place / missing place") vs CORRECTNESS ("right place,
  wrong output")**.
- **★ SEQUENCING GATE (user, 2026-06-17): STRUCTURAL fixes come BEFORE any inference improvement.** After the
  audit + phase-2, the architecture-fix phase resolves the structural obligations (decomposition, misplaced/
  duplicated responsibilities, missing layers, the deferred refactors) — getting the architecture right —
  and ONLY THEN does inference-correctness work begin, on the corrected architecture. Never tune a
  correctness fix on a structure about to change.
- **Read-only throughout.** No code change; no inference change. Empirical probes CC writes are diagnostics
  (committed locally if useful, byte-identical to production). Behavior-changing fixes are pinned, not done.
- **Cadence:** one layer at a time (CC audits → Cowork second-opinions → reconcile → pin) through P1→P4,
  then phase 2. Each CC audit verified by Cowork at the committed object / against the pasted dossier.

## §7 — Start
First layer: **`cadencekeyanchor.cpp`** (P1, the precision bottleneck) — CC primary-audits per §3, Cowork
second-opinions. (Order is prioritization only; any P1 layer is a valid start.)

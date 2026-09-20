# Stage 3.2 Beam-Widening Design — Drafting Report

*CC, 2026-06-13. Base commit `a652dc1ba7` (Stage 3.4-i complete; HEAD output-identical to
`548adb7b2e`). Deliverable: the design doc `docs/beam_widening_design.md` (DRAFT, uncommitted
pending ratification — roadmap rule 4) and this report. No production code, no committed change;
the only writes are these two untracked docs.*

---

## §1 — Probes run and what they settled (esp. the Δ=+7a lattice walk)

All probes were throwaway, read-only `batch_analyze.exe --dump-regions` runs (Git Bash launch
per `feedback_batch_analyze_windows`), `--preset Baroque` (the Δ=+7a identity set's gate), to
**confirm the 2026-06-09 per-cell oracle dump is still current at `a652dc1ba7`** (Stage 3.3 was
byte-identical, so the totals should hold) and to capture the **predecessor and successor
regions** the dump did not — needed for the forward-edge question. Nothing was rebuilt; no
production prototyping.

| # | Probe | Result | What it settled |
|---|---|---|---|
| P1 | `bwv102.7.xml --dump-regions batch`, regions near t17520 | predecessor `Bb`(r10) → failing region `EbMaj7/Ab`(r3, 3.050) → successor `Bb`(r10) | The lattice's predecessor/successor roots. Predecessor is **Bb, not Eb** (so node A earns no rcb and is locally correct); successor is **Bb**, a whole step from Ab → **no V→I forward signal** to rescue node B. |
| P2 | `bwv261.xml --dump-regions batch`, regions near t33840 | failing region `C#m/E`(r1, 3.300) → successor `C#m7♭5/E`(r1) | Confirms the C# continuation; the successor is itself a C#-continuation artifact. F#→C# *is* a descending fifth, so a promoted w_seq would favor F#7 — but only +0.20 against a 0.375 gap (§3 below). |
| P3 | both, scores vs the 2026-06-09 dump | `EbMaj7/Ab` 3.050, `C#m/E` 3.300 match the dump's committed totals | The dump is **current** at `a652dc1ba7`; the lattice walk uses live numbers. |

**The Δ=+7a lattice walk — the load-bearing derivation (design §3).** Using the dump's
per-cell decomposition (`cc_deltaseven_7a_diagnostic_report.md` Part C) for the node candidate
scores and the probes for the predecessor/successor:

- **bwv102.7.** Node A (transient `{D,Eb,G,Bb}`): Ab weight 0 → AbMaj7 not a candidate; oracle
  reads EbMaj7 = **3.05, the highest-scoring node in the neighborhood, locally correct**. Node B
  (present-root `{C,Eb,G,Ab}`): AbMaj7 wins vertically by 0.225 (2.550 vs Eb/Ab 2.325), but rcb
  +0.40 (from A=Eb) flips it. **Greedy path 5.775 > "correct" path 5.600 by 0.175** — and 0.175
  is exactly `rcb(0.40) − margin(0.225)`. A is locked to Eb (Ab unscorable), so the beam has
  nothing to revise; the greedy path **is the global optimum**.
- **bwv261.** Node S2 (`{C#,E}`): C#m beats F#7 by **1.25** (F# absent) — overwhelming, not a
  near-tie. Node S3 (`{C#,E,F#,A#}`): F#7 wins vertically by 0.025, but rcb +0.40 (from S2=C#m)
  flips it. **Greedy opt1 6.525 > F#7-target opt2 6.150 by 0.375.** Global optimum is again the
  greedy (wrong) path.

Arithmetic verified independently (report-local Python check; reproduced in design §3 tables).

**What this settled, and why it is a stop-condition finding.** The part-1 thesis — "a global
decode never irrevocably commits the transient wrong root, so the rcb edge from a *low-scoring*
transient does not survive" — rests on the transient being **low-scoring**. The dump shows it is
the **highest-scoring** node (EbMaj7 3.05, C#ø7 3.35), **locally correct** given the tones it
sees. The continued-root (wrong) path is therefore the genuine score maximum, which a global
decode finds exactly as a greedy decode does. **Re-ranking the search cannot change which path
scores highest; only re-weighting the edges or changing the candidate set (segmentation) can.**
Δ=+7a is structurally **Δ=+7b with `basisDep > 0`** (a sounding third on the wrong reading), which
is why Gate R fixed Δ=+7b but is inapplicable here. Per the instruction's stop condition ("the
Δ=+7a derivation showing the beam does NOT fix it — report; it reshapes the whole acceptance
roster"), this is reported, not papered over: **Δ=+7a is removed from the 3.2 win column** and
routed to Stage 5 (rcb reweighting + a new forward-completion edge) or joint segmentation
(design §3.4, OQ1).

No probe required a rebuild or any source change; the working tree is `a652dc1ba7`-clean (the
only new files are the two design docs). The temporary `/c/tmp/bwv102_regions.json` /
`bwv261_regions.json` dumps are throwaway and untracked.

---

## §2 — Section map + the three most load-bearing claims

**Section map** (`docs/beam_widening_design.md`):
1. Scope + the behavior-change contract (Level-0 byte-identical default; the three-condition
   gate that replaces byte-identity: ratified-in-advance, DCML-adjudicated, measured).
2. What "widen the beam" concretely means — beam-in to top-K; the Viterbi forward+backtrack
   decode; Q2 forward-edge promotion to a true two-sided lattice; the caveat that promoting the
   *existing* forward signals ≠ a new completion edge.
3. **The Δ=+7a mechanism, derived** — both lattice walks, the thesis falsification, the three
   unlock forks. The centerpiece.
4. The must-not-break set as hard constraints — Δ=+7b trio, Gate I's double obligation, the
   identity sets, the 11 snapshots (bias touches 8).
5. Gate-retirement sequencing (Q3: 3.4 leads 3.2; the concrete fold order).
6. Acceptance roster with measured expected deltas + DCML adjudication (Δ=+7a downgraded).
7. Beam width K=8 + decode cost (decode-once; Level-1 not interactive-bounded).
8. Config scope (Default eval / Baroque calibration / Jazz hard-stop; no threshold re-tune).
9. Migration sub-steps 3.2-a…e; risks; flag-vs-in-place; rollback.
10. Open Questions OQ1–OQ5.

**The three most load-bearing claims and their evidence:**

1. **The wider beam does NOT fix Δ=+7a at K=8 over the fixed segmentation** (design §3). Evidence:
   the per-cell dump (`cc_deltaseven_7a_diagnostic_report.md` Part C) + the live probes (§1) +
   the verified lattice arithmetic. The transient node is locally correct and highest-scoring;
   the continued-root path is the global optimum; rcb(0.40) exceeds the vertical margin
   (0.225 / 0.025); the differentiating forward signals don't fire on the actual successors. This
   reshapes the roster (§6) and is OQ1.

2. **Every remaining gate mutates identity, so 3.2 is fully gated behind 3.4** (design §5; Q3).
   Evidence: `cc_stage3_4i_dossier.md` §3 (the per-gate "mutates id? → caps beam" column is *yes*
   for all thirteen, including the structural keeper J). There is no non-mutating gate to widen
   past early, so the fold-then-widen order is total, not selective.

3. **Gate I is the single concentrated BIR risk, double-coupled** (design §4.2). Evidence:
   `cc_stage3_4i_dossier.md` §3/§5 — on Default, gate retirement is BIR-free; the only
   BIR-relevant gate is I on Jazz (−5 fixes), and disabling I *also* fails both Δ=+7b Gate-R
   pins. So 3.2's beam-widening BIR risk is concentrated in **one gate's two proof obligations**
   (5 Jazz fixes + the Δ=+7b first-inversion selection), not spread across the set. If I cannot
   fold without losing one, it stays a re-rank (OQ3).

---

## §3 — Open-Questions list (forks for ratification)

Reproduced from `docs/beam_widening_design.md` §10. Each carries a CC recommendation; the
decision is Cowork/user's.

- **OQ1 — Δ=+7a retargeting.** K=8 does not fix Δ=+7a (§3). Three unlocks: Stage-5 rcb
  reweighting, a new symmetric forward-completion edge, or joint segmentation. *Rec: accept the
  finding, retarget 3.2 onto the gate-subsumption roster, route Δ=+7a to Stage 5 (rcb reweight +
  completion edge, fitted jointly against the Δ=+7b/Alberti must-holds); avoid joint
  segmentation until the Stage-5 granularity-robust metric exists.*
- **OQ2 — Does 3.2 ship without a user-facing BIR win?** Default is BIR-identity-free at 3.2; the
  value is architectural + the Jazz bwv74.8 opportunity. *Rec: ship it — the consolidation
  (gates→decode, greedy→global) is the prerequisite for Stage-5 edge fitting; frame 3.2 as "the
  decode Stage 5 fits," not "the Δ=+7a fix."*
- **OQ3 — Gate I: fold or hold?** If I can't fold without losing one of its two obligations, it
  stays a post-decode re-rank and the beam does not widen past it. *Rec: attempt the fold with
  both pinned; hold I if either moves. Highest-stakes call in the stage.*
- **OQ4 — Promote existing forward signals (Q2) vs design a new completion edge.** The existing
  signals don't rescue Δ=+7a (§2.3/§3). *Rec: promote the existing signals in 3.2-b (subsumes
  H/Iter-91, completes the two-sided lattice); design the new completion edge in Stage 5 with the
  rcb reweighting. Keep them separate.*
- **OQ5 — Threshold/level-dependence.** *Rec: no gate threshold becomes beam-width- or
  level-dependent at 3.2; if the bias-fold forces it, prefer a structural entry condition
  (CLAUDE.md policy).*

---

## §4 — Unknowns / caveats

- **The §3 finding is derived, then needs the live-decode confirmation 3.2-c will produce.** The
  lattice walk uses the per-cell dump + region probes; it does **not** run an actual K=8 decode
  (no decoder exists yet — 3.1 shipped beam-1 only). The derivation is robust (the greedy path is
  the arithmetic global optimum over the enumerated candidates), but the implementation run must
  confirm Δ=+7a stays null and, if it moves, find the term the derivation missed (a fired forward
  edge, an un-enumerated candidate). Design §9 risk 1.
- **Forward-edge promotion's full effect needs the successor *cell* scores, not just roots.** The
  probes give successor *winners* (Bb; C#m7♭5), enough to show the differentiating signals don't
  fire (bwv102.7) or are too small (bwv261, +0.20 vs 0.375 gap). A complete proof would dump the
  successor snapshots' cells under a true two-sided decode — deferred to 3.2-b's measurement,
  since it cannot change the §3 conclusion (bwv261's gap alone exceeds any single forward bonus).
- **Gate I × Gate R coupling on Δ=+7b is established but not mechanically dissected** (carried
  from `cc_stage3_4i_dossier.md` §6.4): disabling I fails both Δ=+7b pins, but whether I selects
  the first inversion directly or via the bias sort is a 3.2-d design input, not derived here.
- **bias-fold snapshot count.** Bias touches 8/11 snapshots; the fold's exact golden deltas
  depend on the inversion-edge migration (3.3 landed the edges; the *fold* — removing the gate —
  is 3.2-a). The 8 are an upper bound on the snapshots needing DCML adjudication, not a count of
  changes.
- **Region counts / scores are `--preset Baroque` at `a652dc1ba7`.** The Δ=+7a numbers are the
  Baroque identity-set's; the conclusion (high-scoring transient, rcb > margin) is structural and
  config-robust (the mechanism is the same on Default-14, where bwv102.7/bwv261 also sit).
- **No stop-condition beyond Δ=+7a was hit.** No must-hold is broken without a guard (§4 design);
  Gate I's foldability is flagged as a fork (OQ3), not assumed; no scope creep into key-path
  (Stage 4) or functional-layer (Stage 6) beyond the stated interfaces.

---

*Design doc stays uncommitted until the ratification addendum (roadmap rule 4). This report is
the input to that ratification.*

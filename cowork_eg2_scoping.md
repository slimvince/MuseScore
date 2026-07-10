# EG-2 Scoping — Rebuilt-vs-Legacy Go/No-Go, Opened Under the Premise Gate

> **Cowork, 2026-07-10 (session 36). The FIRST work item opened under CLAUDE.md #17–#19.**
> EG-2 (`cowork_engage_arc_plan.md` Stage-3 entry gate): *does the REBUILT chord path (decoder
> carry + the intended selection) beat the LEGACY production path against the DCML root ground
> truth?* — the go/no-go on the whole E4 engagement. This document is the **desk-simulate-stage
> opening**: the premise ledger v1, the #19 instrument-establishment plan, and the desk-simulation
> plan. **The probe is NOT specified here** — per the #17 funnel it may only be specified after
> the desk simulation is done and its predictions are recorded, and may only RUN after the
> instrument is established. Instrument facts below were grounded by a read-only sweep
> (citations at file:line); no code changed.

## §1 The measured question, stated precisely

**Target quantity:** class-(b)-style (pitch-class-decidable-root) root-disagree DURATION vs DCML,
per preset, on the a8 union-of-boundaries unit (variant-b, segmentation-invariant,
duration-weighted) — the same unit as the robust stop. **Comparison:** the E0 full-spine chain
output vs the committed legacy `.ours.json`, both graded by the identical substrate.
**Verdict form:** rebuilt beats legacy iff its class-(b) root-disagree duration is lower per
preset by more than the desk-sim-predicted noise band, with the win/loss set-diff explained
per run (the block-(A) discipline). **Jazz is excluded from any correctness claim** (EG-6: no
licensed jazz GT; Jazz may be run consistency-only, labeled as such).

## §2 Premise ledger v1

**P1 (ASSUMPTION — the go/no-go claim itself).** "The rebuilt path is more root-correct than the
legacy path." This is the claim under test; its written quantitative prediction (direction +
magnitude band per preset + per failure class) is OWED at the end of the desk simulation (§4),
BEFORE the probe is specified. No prediction, no probe.

**P2 (FACT — the grading substrate is established).** The a8 unit self-validates byte-for-byte
against `compare_rn.grid_score_regions()` per piece (`tools/robust_stop/README.md:59-60`); the
E0 grader reuses it verbatim ("no new comparator", `cc_e0_fullspine_report.md:70-72`); the joint
probe already maps decoder output to DCML spans via the shared `_dcml_time_spans` +
`_active_index_at` (`measure_joint_probe.py:59-70`). Segmentation-invariance is load-bearing
here — the two paths segment differently (per-slice vs coarse regions) and the variant-b unit
absorbs that by construction. The legacy baseline is committed
(`tools/robust_stop/`, 63.36/62.37/63.25 root-agree, corpus `c50002fee1`).

**P3 (PROXY→TARGET — every gap between "E0 chain today" and "post-E4 production", declared per
#17(d)).** The probe's subject is a **proxy**; the target is post-E4 production. The gaps:

| # | gap | direction of bias | ledger treatment |
|---|---|---|---|
| G1 | **Key feed:** E0 gives the decoder ONE home key (`inferLocalKey[0]`, `cc_e0_fullspine_report.md:51`); E4 feeds per-slice L3 keys | **Handicaps the rebuilt path on modulating pieces** — a rebuilt WIN under G1 is strong evidence; a LOSS is ambiguous (could be the handicap) | asymmetric read of the verdict, declared up front |
| G2 | **Carry shape:** `topK=6` voicing cap (`chordslicedecoder.cpp:746-789`); the distinct-root carry is owed at E4 | the full-fan-out selection is NOT measurable; top-roots behavior is | probe measures the top-of-carry path only; stated in the verdict |
| G3 | **Selection:** the E0 chain runs the AS-BUILT resolver — progression-first + `attemptFineGrainOverride` UNCONDITIONAL (the Tier-1 traps, `functionresolver.cpp:221-246/529-531`) — NOT the intended selection (arc #9) | the override is measured net-harmful (−756): running it in the probe poisons the rebuilt arm with a known-bad component | **the probe arm must run with the override DISABLED** (the Phase-3 finding: "best measurable θ disables it") and must declare that the channel re-ordering is NOT exercised — the probe measures *decoder carry + argmax (+key/cadence arms as-built minus override)*, a LOWER BOUND on the intended selection |
| G4 | **Extensions carry gap:** `ScoringCell→ChordSliceCandidate` never assigns `extensions`/`naturalFifthPresent` (defaults 0, `chordslicedecoder.cpp:443-453`; `cc_e0_fullspine_report.md:227-254`) — seventh/aug6 labels structurally non-firable on the E0 chain | affects QUALITY labels; root grading mostly insulated — but per #17(e) the false-negative path must be enumerated: a missing seventh CAN flip a root where the seventh disambiguates rotation (dim7/V7♭9 family) | desk-sim case 3 (bwv272) probes exactly this; if the desk sim shows root flips from G4, the carry-fix precedes the probe |
| G5 | **Deferred C2/G5 chord types** (`chordslicedecoder.h:97-103`) | equal for both arms (shared template catalogue) — non-differential | declared, no action |

**P4 (Class B / #19 — the E0 instrument is NOT established).** What exists: flag-OFF
byte-identity to production (`cc_e0_fullspine_report.md:86-95`) and the established grader
substrate (P2). What does NOT exist: (a) the fs_* dumps carry a **stale manifest stamp**
(`d1d4d3d7f0` vs corpus `c50002fee1`) and the collector never calls `validate_corpus_dir`
(`cc_engage_c3_measurement_report.md:173-188`); (b) **no reproduce-check** of the chain output
(two runs byte-identical); (c) the **86-vs-2181 granularity reconciliation is unresolved**
(`cc_e0_fullspine_report.md:327-329`) — note: grading on the a8 unit (P2) makes this moot for
ROOT duration specifically, but that insulation claim itself must be checked (#17(e)): the unit
is segmentation-invariant only over covered spans; confirm equal coverage between arms.
Establishment plan in §3. **The probe may not run before §3 completes.**

**P5 (FACT — failure-population structure, the basis for per-class predictions).** From the O1
investigation (`CLAUDE.md` block (D)): ~60 % Baroque of the legacy residual is
spelling-resolvable, most of the rest bass/inversion or segmentation over-grab (which
`changePointSlices` removes by construction), and the genuinely function-only remainder is the
small share-tone set. The rebuilt path's wins should therefore concentrate in the over-grab and
spelling classes; the share-tone class should NOT move without the intended selection (G3).
These become quantitative per-class predictions at the end of the desk sim.

**P6 (THEORY — why the rebuilt path should win at all).** Per-slice decoding over the L2
change-point grid removes the over-grab class structurally (segmentation research grounding,
`cowork_functional_analysis_research_grounding.md`); the decoder's spelling-pin addresses the
symmetric-rotation class (Micchi/McLeod spelling line). Both are cited-specific (#2), but their
MAGNITUDE on this corpus is exactly what the desk sim + probe must put numbers on.

## §3 The #19 establishment plan for the E0 instrument (before any probe)

1. **Re-dump** `--dump-fullspine` ×presets on the pinned corpus at current HEAD; stamp a
   manifest (corpus `git_hash` + instrument commit + flag set) exactly per the a8 pattern;
   wire the collector through `characterise_bir_false.validate_corpus_dir` (the shared guard).
2. **Reproduce-check:** run twice; assert byte-identical output (the R10-b lesson: identity, not
   assumption).
3. **Derive what the unit measures on the E0 shape:** confirm the per-slice `regions[]` grade on
   the a8 unit covers the same DCML span set as the legacy arm (coverage equality check —
   the P4(c) insulation check). Any coverage asymmetry is a STOP.
4. **Override-off variant:** confirm the probe arm can run with `attemptFineGrainOverride`
   disabled via the existing dormant θ/params (no `src/` change; if a flag is needed, that is a
   separate revertible instrument `feat` per #14).

## §4 The desk-simulation plan (the #17(c) stage — hours, not a session)

Trace BY HAND, at the score, legacy-vs-decoder-under-home-key on five known failing runs —
"which term moves, by how much, on this actual case?" — and record the predicted winner per
case BEFORE any probe output is seen:

| case | class | what to trace | prior expectation to check |
|---|---|---|---|
| `bwv10.7@36000` | segmentation over-grab (5-note scale across `i43`/`iv532`) | does the slice grid split what legacy over-grabbed, and does each slice decode to the GT root? | rebuilt WINS by construction (P6) — if the trace does NOT show it, P6 is in trouble early |
| `bwv352@1440` | share-tone function-only (Am6↔F♯ø7) | pc-identical: does ANY decoder term separate the rotations under the home key? | NO CHANGE without the intended selection (G3) — a flip here would be a surprise (STOP) |
| `bwv272@4320` | symmetric dim7 rotation (G♯dim7) | the spelling-pin vs the key-gated `dim7CharacteristicBonus`; AND the G4 seventh-carry false-negative path | uncertain — this case DECIDES whether G4 must be fixed pre-probe |
| `bwv174.5@6240` | bass/inversion vs root (E/G♯ beats G♯ø7) | bass channel treatment in the decoder vs legacy's inversion bonuses | trace to predict; no prior committed |
| `bwv416@10080` | segmentation-union fix precedent | does per-slice decoding preserve the fix the union produced? | rebuilt should HOLD the fix; regression here = the slicing premise needs refinement |

**Output of the desk sim (the gate to the probe):** the filled prediction table — per-preset
direction + magnitude band on class-(b) root-disagree duration, per-class fire-rate expectations
(over-grab, spelling, bass/inversion, share-tone), and the G4 disposition (carry-fix before
probe: yes/no). Recorded in this doc as §5 BEFORE the probe instruction is written.

## §5 Written predictions — ★ RECORDED at the desk sim (2026-07-10, BEFORE any probe exists)

The §4 desk simulation was executed the same day (traces in §7). Predictions, falsifiable, per
#17(b) — the probe verdict is read against THESE, not retrofitted:

**Per-case (the five §4 runs, E0 chain under the G1 single-home-key handicap, override OFF):**

| case | prediction | confidence | the term that moves |
|---|---|---|---|
| `bwv10.7@36000` | rebuilt WINS (root G = GT) | HIGH | segmentation: the clean slice {G,D,F} loses the over-grabbed C/E♭; the B♭ reading has no B♭ sounding and dies with the window |
| `bwv352@1440` | rebuilt WINS (root F♯ = GT) — **prior OVERTURNED at desk** | MED-HIGH | the over-grab had also corrupted the BASS (legacy's E bass arrives at tick 1680); the clean slice's bass is F♯3, and `bassNoteRootBonus` 0.70 dwarfs the 0.0125 Am6-vs-F♯ø7 gap |
| `bwv272@4320` | rebuilt WINS (root G♯ = GT) | MEDIUM | the decoder's spelling-pin on the complete, correctly-spelled G♯–B–D–F dim7; the G4 extensions gap shows NO root-flip path on this case (dim7 is a 4-tone template, not root+extension) |
| `bwv174.5@6240` | NO CHANGE (legacy's E/G♯ persists; still wrong) | MED-HIGH | the same vertical scorer imputes the absent E root under the Dmaj home key; the fix needs the per-slice f♯ local key (post-E4, gap G1) or the selection's key-consistency channel (gap G3) — the designated G1-handicap case |
| `bwv416@10080` | rebuilt HALF-WINS (≥240 of 480 ticks): slice [10080,10320) → G♯ via spelling-pin (certain-ish); slice [10320,10560) uncertain — the passing E completes a full E7 template {E,G♯,B,D} and may win unless membership salience down-weights the 240-tick E | MEDIUM | spelling-pin on slice 1; `membershipSalienceThreshold`/duration weighting on slice 2 |

**Aggregate (the P1 prediction):** on Baroque and Default, the rebuilt arm's class-(b)
root-disagree DURATION decreases by **15–40 %** vs the legacy reference (wide band — the desk
sample is 5 documented, hence understood-biased, cases). Wins concentrate in: segmentation
over-grab, symmetric-spelling (dim7 rotation), and bass-corrected share-tone classes.
Unchanged: wrong-local-key cases (G1) and imputed-root cases. **New errors WILL appear**
(predicted mechanism: a short passing tone completing a stronger template, the bwv416-slice-2
type) — the prediction is net decrease; if class-(b) duration INCREASES on any preset, the
answer is no-go as scoped, and diagnosis precedes any conclusion (§6). Jazz: consistency-only,
no prediction (EG-6).

**G4 disposition (owed by §4):** NO pre-probe carry-fix required for ROOT grading — no
root-flip path via the zeroed `extensions` field was found on the dim7/V7♭9 family case
(quality labels remain affected; the probe checks the dim7 rotation distribution to confirm).

**Ledger update from the desk sim (recorded as evidence, not surprise-at-build):** the §4 prior
for `bwv352@1440` ("share-tone cannot move without the intended selection") was WRONG — the O1
"function-only residual" classification partially conflates legacy segmentation artifacts:
over-grab corrupts not only the pc window but the BASS, so part of the presumed-L5 residual is
L2-resolvable. This sharpens P5 and is exactly the class of discovery the desk-sim stage exists
to make cheaply (explorational scope).

## §6 Sequencing (corrected at pre-registration, 2026-07-10)

**Strictly sequential, per the #17 funnel: (1) commit this doc with §5 EMPTY (pre-registration —
the plan is provenance-stamped before any measurement, #16/#17(b)); (2) desk sim (§4) — the
cheapest stage runs first and may kill or reshape the probe before the establishment re-dumps
are paid for; (3) instrument establishment (§3) only if the desk sim's filled predictions
warrant a probe; (4) probe spec, then run.** The probe itself is read-only (explorational
scope — surprises permitted there; they feed the ledger). The verdict comes back to the user
with the P3 asymmetry applied: a rebuilt win under the G1 handicap is decision-grade; a loss is
diagnosed before any conclusion is drawn.

## §7 Desk-sim traces (the evidence behind §5; executed 2026-07-10)

Materials: notes with spelling extracted from `tools/corpus/<stem>.xml` (divisions 10080,
tick = div×480/10080, onsets verified against `.ours.json` region boundaries and `tones`);
legacy output from `tools/corpus/baroque/*.ours.json`; GT from the When-in-Rome rntxt
(`tools/dcml/when_in_rome/Corpus/.../analysis.txt` via `dcml_parser`); failing-run lines from
`tools/robust_stop/baroque_variant_b_root_fail_runs.txt`.

**T1 `bwv10.7@36000`** (fail line 8: `our=Bb/C(10) → dcml_root=7 cls=b`). Legacy region
[36000,36960) grabbed 960 ticks spanning two GT chords; its tone set {C,D,E♭,F,G} contains NO
B♭ — the committed B♭ root is imputed from neighbor-polluted content (C,E♭ from ticks
35520/36480). The change-point slice at [36000,36480) contains exactly D3,D4,F4,G4 (G4 tied
from 34560) = {G,D,F}, an incomplete G7 — music21's own reading. Root G is diatonic in the
g-minor home key; the B♭ candidate has no sounding root and no M3. Verdict: the failure is
pure window pollution; per-slice decode lands G = GT.

**T2 `bwv352@1440`** (fail line 4241: `our=Am6/E(9) → dcml_root=6 cls=b`). The slice
[1440,1680) is a complete, correctly-spelled F♯ø7: F♯3(bass), E4, A4, C5. Legacy's region
[1440,2640) over-grabbed G♯4 AND E3 — both arriving at tick 1680 — so legacy scored a 5-pc
window with an E BASS that does not exist at the failing span. Legacy's own margin: Am6/E
2.7875 vs F♯m7♭5 2.775 = 0.0125. On the clean slice the bass is F♯3; `bassNoteRootBonus`
(0.70, root-in-bass) accrues to the F♯ø7 reading and cannot accrue to Am6-with-6th-in-bass —
a swing ~50× the gap. The diatonic prior opposes F♯ in a-minor but is 0.30 at full strength,
still under the swing. Verdict: F♯ = GT. ★ The §4 prior ("pc-identical share-tone can't move
without L5") is refuted at the desk: over-grab had corrupted the BASS, not just the pc set.

**T3 `bwv272@4320`** (fail line 2425: `our=Bdim7/D(11) → dcml_root=8 cls=a`). The beat-slice
is the complete dim7 D3,G♯3,F4,B4 — all four tones sound; spelled G♯–B–D–F = stacked minor
thirds from G♯, the GT rotation (viio4/3 of a). No E sounds (an E7♭9 reading would be
rootless). The decoder's symmetric-sonority spelling-pin exists precisely for
dim-triad-as-dim7 (`chordslicedecoder.h:86`); the notated spelling uniquely selects root G♯.
G4 check: the dim7 label is a 4-tone template, not root+extension — the zeroed `extensions`
field has no path to the ROOT here. Verdict: G♯ = GT via the pin (MEDIUM — conditional on the
pin firing for complete dim7s, which is its declared purpose).

**T4 `bwv174.5@6240`** (fail line 900: `our=E/G#(4) → dcml_root=8 cls=b`). The slice is
G♯3,B3,F♯4,B4 = {G♯,B,F♯} — no E and no D♯ sound anywhere in the region. Legacy imputes the
absent E root (E/G♯ II6, 2.16) over the sounding-root G♯ reading (oracle rank-1 G♯ø7 1.89 —
`cc_absent_root_investigation.md:274`). The decoder reuses the same vertical scorer snapshot;
under the Dmaj home key (G1) nothing re-ranks: the imputed-root preference is a scorer
property, not a segmentation artifact, and the GT's f♯ local key (corroborated by the next
chord C♯–E♯–B = V7/f♯) is exactly what the single-home-key feed cannot supply. Verdict: no
change; the designated G1-handicap case.

**T5 `bwv416@10080`** (fail line 5700: `our=E7b9/G#(4) → dcml_root=8 cls=b`). Two slices:
[10080,10320) = D5,F4,B3,G♯3 — complete dim7, correctly spelled from G♯ (GT viio7/V) → the T3
mechanism applies, root G♯. [10320,10560): the alto passing eighth F4→E4 yields {E,G♯,B,D} — a
COMPLETE E7, first-inversion-with-3rd-in-bass; the legacy E7♭9 root rests entirely on this
240-tick passing tone. Whether the decoder's membership/duration weighting
(`membershipSalienceThreshold` 0.55) suppresses the short E against three 480-tick holdovers is
genuinely uncertain — recorded as the split prediction and as the predicted mechanism for NEW
rebuilt-arm errors.

---

*Cowork, 2026-07-10, session 36. Instrument grounding sweep citations:
`cc_e0_fullspine_report.md`, `cc_engage_c3_measurement_report.md`, `measure_joint_probe.py`,
`tools/robust_stop/README.md`, `chordslicedecoder.{h,cpp}`, `batch_analyze.cpp`,
`cc_anchor_redesign_dossier.md`, `cc_absent_root_investigation.md`,
`cowork_layer5_engagement_design.md`, `cowork_l1_l5_premise_debt_audit.md`. Desk-sim materials
extracted read-only from `tools/corpus/` + the When-in-Rome GT; no repo file modified by the
extraction.*

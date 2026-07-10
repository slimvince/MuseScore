# OPEN ITEMS REGISTER — the ONE home for every discovered-but-unresolved issue

> **Created 2026-07-10 (session 36), user-directed** after a full-repo sweep found 91 open items
> scattered across 12 tracking surfaces with 11 status contradictions. **Standing rule (CLAUDE.md
> "Open-items register" section):** read this file at session start; a stage may not open while a
> register item gating it is open; every new discovery gets a row in the same commit that records
> it; every resolution flips its row with provenance. Detail lives at the cited source — rows here
> are pointers, not restatements. IDs are stable; do not renumber.

## A. STAGE-3 ENTRY GATE — blocks E4/L5 engagement (from `cowork_engage_arc_plan.md`)

| ID | item | source | status |
|---|---|---|---|
| OI-1 | EG-1: T1-1 resolver progression-first re-ordering (arc-#9 design) must land pre-production | arc plan; premise-debt T1-1; `functionresolver.cpp:221-246` | OPEN — prerequisite |
| OI-2 | EG-1: T1-2 F-B override demotion (arc-#11 design; `attemptFineGrainOverride` unconditional, −756) | arc plan; premise-debt T1-2; `functionresolver.cpp:529-531` | OPEN — prerequisite |
| OI-3 | EG-2: rebuilt-vs-legacy go/no-go | `cc_eg2_probe_report.md` | PROBED — P1 not supported as measured (abstention artifact); honest re-measure blocked on OI-1/OI-2; decision with user |
| OI-4 | EG-3: pedal reader HARD-GATED on owed-P1 over an established pedal-dense corpus (premise currently unfavorable 0.20/0.50/0.20, n=2–5) | arc plan; L5-engage §9.2 #3; owed-P1 | OPEN — gated |
| OI-5 | EG-4: confidence-scale commensurability (T1-3/S19/F-1/D-FS) owes #17 ledger + desk sim before any θ/kBoundary fit; combinedBoundary calibration already FAILED (D-8) | arc plan; premise-debt T1-3 | OPEN |
| OI-6 | EG-5: extend `tools/param_manifest.json` to L1/L2 constants + live-L3 hysteresis margins before Stage 5 closes (T3-1) | arc plan; premise-debt T3-1 | OPEN |
| OI-7 | EG-6: Jazz validation status — establish jazz GT corpus or de-scope Jazz correctness claims (T3-2) | arc plan; premise-debt T3-2 | OPEN |

## B. Owned by Stage-3 / E4 (build + design decisions at the engage step)

| ID | item | source | status |
|---|---|---|---|
| OI-8 | FQ-4 anchor: decoder carry replaces `results` (cap→append + pedal clobber + Iter 86/91 die by construction) | audit §3; §9.2 #1 | OPEN |
| OI-9 | Distinct-root-preserving carry (topK caps voicings, ≥3rd root not guaranteed; exclusion tail #12) | L5-engage §2.3; §9.2 #2 | OPEN |
| OI-10 | FQ-2 quality-from-key single owner (S12/S14/S15/S16/S17) — decided WITH §6-block dissolution | audit; §9.2 #5 | OPEN (owner named-not-chosen — contradiction G) |
| OI-11 | FQ-1 different-root primitive — retires WITH the decoder (reassigned E4; audit §3 table stale) | audit §3.1 | OPEN |
| OI-12 | FQ-3 `findTemporalContext` ownership move (reassigned E4; audit §3 table stale) | audit §3.1 | OPEN |
| OI-13 | FQ-8 owed migrations: two-segmenters, two-pitch-context, tpc-reader fold, `function/` rename (S18) | audit; §9.2 #7 | OPEN |
| OI-14 | PC-1 E4 design question: symmetric-set detection from pc set vs land C2/G5 dim7 type vs (c) generalize spelling channel (OI-15) | `cowork_eg1_premise_checks.md` | OPEN — design decision at E4, each option owes #17 ledger |
| OI-15 | ★ Spelling as a FIRST-CLASS evidence primitive (user-raised 2026-07-10): tpc facts are L1-carried but consumed only by the pin; O1 measured ~60% of Baroque residual spelling-resolvable; arc-#9 channel #2. Design where the general spelling channel lives (#6/#7) | PC-1 amendment; O1; arc #9 | OPEN — E4/L5 design input |
| OI-16 | T1-4 decoder rotation assumes key prior correct (diatonic terms only key input; spelling-pin sole guard) + two chord-equality relations (`sameChordVoicing`/`sameChordSymbol`) latent inconsistency | premise-debt T1-4 | OPEN — surfaces at E4 |
| OI-17 | PC-3 Xsus fifth mis-rooting (43% of EG-2 new errors) — hypothesis UNCHECKED (bass-on-fifth + sus template); checkable at bwv87.7@9600 cube | PC-3; cc_eg2 §2.4 | OPEN — L4 scorer owner; check at E4 design, fix per #8 timing |
| OI-18 | L4 temporal-extension trigger specified NOT coded (silently truncates); whole §2.15 extension cluster exercised nowhere; unified orchestration contract owed | roadmap §2.15 | OPEN — at engage |
| OI-19 | S18 `function/` dir rename (rides R7) | audit UNCLEAR-4 | OPEN |
| OI-20 | Jazz +1 interim class-(a) case — retires when Layer 4 pins rotation/center | CLAUDE.md two-tier block | OPEN — interim |
| OI-21 | owed-P2 confirmation-gap reproduction (carry margin vs pass2 sigmoid) | L5-engage §8 | OPEN — post-E4 |
| OI-22 | owed-FB1: F-B annotate must move class-(b) duration favorably at its build event | L5-engage §8 | OPEN — at F-B build |

## C. Owned by Stage-5 (precision phase — do NOT fix earlier, #8)

| ID | item | source | status |
|---|---|---|---|
| OI-23 | Tier-2 Class-B mass: ~30 live constants hand-set pre-2026-06-13 against the broken batch gate; only kWStepIn ever robust-unit-fit — retires as the fitter RUNS | premise-debt T2; param_manifest | OPEN |
| OI-24 | O-17: recover the 53 lost F-B corrections via a correctness-correlated signal | fitter O-17; fb §4.4 | OPEN |
| OI-25 | T3-3 dormant placeholder constants (L5 firewall 1.0s, θ, inline 1.0/0.5/0.25, §15-13 null) — load-bearing at engage, fit at Stage 5 | premise-debt T3-3 | OPEN |
| OI-26 | O-13/§15-13 family-4 weight: size-viable but not runnable until L5 engages (objective gap) | fitter O-13 | OPEN — blocked |
| OI-27 | Uncalibratable confidences: L5 mid-range inversion (non-monotone), tonicVote (anti-monotone), L1.5 spread — maps deferred D-8, fixes belong to owning layers | fitter §11 | OPEN |
| OI-28 | `uncertaintyMargin` 0.5 never-fit seed governs decoder abstention (18% duration) — fit at Stage 5; behavior characterized at PC-2 | PC-2 | OPEN |
| OI-29 | §6-block dissolution (OWED #2) incl. S14/S16 quality-from-key gates | roadmap; audit | OPEN |
| OI-30 | Stage 3.3 oracle temporal-signal migration + Gate R basisDep proxy revisit | roadmap | OPEN |
| OI-31 | Stage 6.3 convention-gap buckets (Maj→Dom7 implied sevenths etc.) | roadmap | OPEN |
| OI-32 | O-2 class-(a) weighting revisit trigger (conditional) | fitter O-2 | OPEN — trigger |

## D. Instrument / measurement layer

| ID | item | source | status |
|---|---|---|---|
| OI-33 | ★ Abstain-aware robust-stop convention OWED before any abstaining path is adoption-gated (metric is abstention-reducible; probe grader = prototype; pinned a8 untouched) | PC-2; cc_eg2 §4.5 | OPEN |
| OI-34 | O-12 corpus git-tracking decision (user call) | fitter O-12 | OPEN — user |
| OI-35 | O-18 stale fs_* manifests process fix (validate or re-manifest E0 dirs; EG-2 used fresh stamped dumps — generalize) | fitter O-18 | OPEN |
| OI-36 | O-10 retained-rule liveness counts at every adoption sandwich | fitter O-10 | STANDING |
| OI-37 | CLASS_A_INVESTIGATE advisory: rebuilt-arm dim7 churn +46320 > 9600 tripped read-only (cc_eg2 §2.6) — investigate at E4 design | CLAUDE.md; cc_eg2 | OPEN advisory |
| OI-38 | O-5/Wave-3 corpus onboarding (jazz/pop GT tiers; pedal-dense corpus for OI-4; VL-D census gap) | fitter O-5; roadmap | OPEN |
| OI-39 | Overfitting risk: single-composer 326-score split; idiom coverage 1/5 (A-7 marks) | fitter §11 | OPEN debt |
| OI-40 | R-11 conformal / R-12 self-consistency levers (deferred dispositions) | fitter §15 | OPEN — deferred |

## E. User adjudication / ratification pending

| ID | item | source | status |
|---|---|---|---|
| OI-41 | #17(c) sharpening: "establish the mechanism FIRES (control flow) before tracing arithmetic" | PC doc §"hands" | ✅ RATIFIED 2026-07-10 — folded into CLAUDE.md #17(c) |
| OI-42 | Audit §5 UNCLEAR rows 1–7 (S2/S3/S4 cataloguing; S8/S9; S14/S16 acceptability; S18 timing; S19 θ deferral; S20 helper; FQ-3 stage) | audit §5 | OPEN — user |
| OI-43 | PONDER-POINT 1: reopen joint (key,chord) RANKING framing (arc-#12 measured key-first-then-chord, not joint ranking) — explorational under #17 if reopened | handoff | OPEN — user |
| OI-44 | Joint step B1–B4 status: design DELIVERED / build SHELVED / framing REOPENED (contradiction B) — needs one declared status | fitter O-4; §9.2 #6; handoff | OPEN — user |

## F. Doc-sync debt (#10) — annotate, don't rewrite history

| ID | item | source | status |
|---|---|---|---|
| OI-45 | scoring_model §4/§6 stale anchors + kHalfDimFirstInversionBonus missing from §6 | premise-debt T3-4 | OPEN — fix at next scoring_model touch |
| OI-46 | Audit §3/§4 tables contradict §3.1 build-status on FQ-1/FQ-3 stage (contradiction A) | audit | OPEN — annotate tables |
| OI-47 | STATUS.md submission-era sections (Current State BIR 25/16, Post-submission priorities, Known Gaps, Future Considerations, COWORK_HANDOFF.md dangling ref) contradict governing docs (contradiction C) | STATUS.md | OPEN — banner + triage (§G) |
| OI-48 | `backlog_chord_track_flag.md` referenced by two live docs, file DOES NOT EXIST (contradiction J) | STATUS refs | OPEN — recreate or re-point |
| OI-49 | D-L3a "closed" (fitter) vs "remains" (roadmap G1) (contradiction K) | fitter §4.5; roadmap | OPEN — reconcile |
| OI-50 | FQ-2 "decided at Stage 2" (arc plan) vs "enumerated-not-resolved" (L5-engage) (contradiction G) | arc plan; L5-engage | OPEN — annotate arc plan |
| OI-51 | Foreign uncommitted `cowork_joint_key_chord_design.md` SHELVED-banner edit sitting in the working tree since session 35 | cc_eg2 §0 | OPEN — fold or discard |
| OI-52 | S20 root-equality helper (trivial; "likely not worth it" — decide and close either way) | audit UNCLEAR-6 | OPEN — trivial |

## G. Submission-era backlog (pre-engage-arc; TRIAGE: supersede or adopt into A–F)

| ID | item | source | status |
|---|---|---|---|
| OI-53 | Tonicization classifier (V/V, V/ii) wired, not implemented | STATUS post-sub #9 | OPEN — likely superseded by L5 design; triage |
| OI-54 | Pedal-point calibration needs corpus evidence (= OI-4/OI-38 pedal-dense corpus) | STATUS post-sub #10 | MERGED → OI-4/OI-38 |
| OI-55 | Ninth-detection gap (melody/harmony conflation) | STATUS post-sub #11 | OPEN — triage at E4 |
| OI-56 | auto_review.py designed, not implemented | STATUS post-sub #12 | OPEN — triage |
| OI-57 | Corpus QA systematic pass (84-score registry era) | STATUS post-sub #13 | OPEN — largely superseded by corpus manifests; triage |
| OI-58 | Known Gaps block: tone weights 1.0; tie re-split; cadence labels English; MusicXML sus export bug; piano-pedal decay model; Rampageswing walking bass | STATUS Known Gaps | OPEN — triage |
| OI-59 | Corelli notation regressions (Gm vs G m1b3 etc.) + 4 deferred notation tests + chopin_bi105 segmentation cascade | STATUS known regressions | OPEN — verify still-current, then assign |
| OI-60 | Blocking/needs-fix trio: chord-symbols-as-input context-menu path; declaredMode soft-boost; implode chord-track gaps | STATUS next-session | OPEN — verify still-current |
| OI-61 | Future Architectural Considerations (bridge reorg; static analyzers; voice roles; include friction; chord-track flag OI-48; chord-staff rename) | STATUS FAC | OPEN — long-horizon |
| OI-62 | Tuning §11.3a–f documented-not-implemented | STATUS | OPEN — triage |
| OI-63 | S7 full mode-prior single-sourcing (Stage-1 leftover, dependency-profile call) | audit; arc plan | OPEN |

## H. Long-horizon roadmap (held deliberately; listed so they are never "forgotten")

| ID | item | source | status |
|---|---|---|---|
| OI-64 | Engage plan E1–E5 (wire → A/B → default-ON → retirements → seal); gates G1–G6 (G2 not met at E0) | roadmap | OPEN — the arc itself |
| OI-65 | Retirement map R1–R9 (R9 = chordanalyzer.cpp split, LAST) | roadmap | OPEN |
| OI-66 | Recognition consumer (encyclopedia → L5 prior) designed-not-built | roadmap | OPEN — deferred |
| OI-67 | Style-clustering / idiom auto-detection / mixtures | fitter A-8ask | OPEN — deferred |
| OI-68 | Capability tracks A-3/A-4/A-5 + NCT L4 lever + voice-leading axis | roadmap | OPEN — deferred |
| OI-69 | Joint segmentation (past Stage 5) | roadmap | OPEN — deferred |
| OI-70 | B3 dim7-template dead end + rootContinuity sparse-gate dead end + Gate-A enharmonic constraint (standing cautions §8) | scoring_model §8 | STANDING constraints |
| OI-71 | Roadmap 0.1 doc pass (stale explorationMode refs; untracked audit doc) | roadmap 0.1 | OPEN |

## I. Siloed analyzed facts (fact-publication sweep 2026-07-10 — `cowork_siloed_facts_audit.md`)

One root cause, one design owner: the shared cross-layer surfaces are voice-blind,
spelling-blind, membership-blind — resolved by the **E4 carry/surface design** (which facts the
shared surfaces publish), not per-site patches. OI-15 (spelling) is the headline instance.

| ID | item | source | status |
|---|---|---|---|
| OI-72 | `StepwiseSignals` (per-note suspension/step/leap, per voice) TRAPPED in decoder membership — the voice-leading evidence L5 selection + pedal need | siloed audit #1 | OPEN — E4 surface design |
| OI-73 | Membership verdict (`chordTonePcs`/`nonChordTonePcs`) dies at the L4→L5 boundary — `FunctionSlice` never copies it | siloed audit #2 | OPEN — E4 surface design |
| OI-74 | Voice/staff identity dropped at `ChordAnalysisTone` — the shared tone surface is VOICE-BLIND (structural root of OI-72/73; pedal "upper-voice" has no channel) | siloed audit #17 | OPEN — E4 surface design |
| OI-75 | `keyAlternatives`/`keyConfidence`: ZERO production consumers (diagnostics only) — the L5 carry contract's key inputs sit unread | siloed audit #4/#5 | OPEN — consumed at L5 engage |
| OI-76 | Cadence detections transient (recomputed per emit path, never stored on regions); L5 cadence channel blocked; production detector circular by design | siloed audit #7 | OPEN — E4 |
| OI-77 | Bass-chord-tone/inversion VERDICT recomputed at ~60 call sites (facts shared, derivation duplicated) — channel #1 has no published form | siloed audit #11 | OPEN — E4 primitive |
| OI-78 | `declaredMode` siloed to the key path; chord diatonic bonus reads only the inferred key | siloed audit #12 | OPEN — design input |
| OI-79 | Duplicated constants: pedal sigmoid inlined (2.0/1.5) vs prefs; emission sigmoid written in two files (S10) | siloed audit #16 | OPEN — fold at next touch |
| OI-80 | Score-annotation input facts (chord symbols/RN/Nashville) recognized as TODO flags, never read | siloed audit #14 | OPEN — long-horizon |

*Sweep provenance: session-36 full-repo sweep (12 surfaces, 91 raw items, 11 contradictions) —
the raw sweep detail with file:line citations is preserved in the session record; rows above
consolidate duplicates (e.g. pedal appears once as OI-4 with merged sources). Items marked
MERGED/superseded stay listed until their absorbing row closes.*

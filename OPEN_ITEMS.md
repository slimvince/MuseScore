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
| OI-84 | ★ FULL-COVERAGE AUDIT PLAN (corrected 2026-07-10 — the earlier "audit-at-touch" form was rejected by the user as risky: touching 1 % would audit 1 %, and new work would build on unknown problems, itself a #18 violation at architecture scale). The plan: (a) PARTITION the module by the retirement map R1–R9 — code that RETIRES at E4 gets NO audit, only the #12 interpretation-check at deletion (A1 verdict); (b) the SURVIVING stack is audited EXHAUSTIVELY per layer in DEPENDENCY ORDER — L1 → L2 → L3 → L4 (decoder + surviving scorer core) → L5 + the instruments — each a read-only session whose ledger output feeds the corresponding E4 step's #17 ledger; (c) enforcement = arc-plan EG-7: an E4 step may not open until every layer it DEPENDS ON (not merely touches) is audit-certified. Coverage of the end-state architecture: 100 % before it carries new load. FIRST ITEM: the L1/L2 certification audit (also the least-covered layers to date) | session-36 user challenge ×2 | OPEN — EG-7; **L1/L2 CERTIFIED by the user, 2026-07-11**, on pass 1 + pass 2 + the OI-89 fully-blind re-run (`cc_l1l2_audit_blind_rerun_report.md`; zero correctness defects found by either reader; residual findings tracked at OI-86/OI-87). **The next layer in dependency order: the L3 audit** (key/mode inference). **★ L3 PASS-1 DONE 2026-07-11** (blind enumerative, P1–P4; `cc_l3_audit_pass1_report.md`; freeze `61dabd86d1`): 22 deep files (15 L3 + 7 L3-MIXED) → **1943 dispositioned rows** (every one verdicted), decoder fire-rate **352/352** (`c50002fee1`; 11.43 % uncertain slices, 3.94 % region key-change, 275/352 modulating). 8 findings (OI-90…OI-95 + existing OI-75), **NONE a correctness bug; the L3 spine reproduces its documented design.** **Certification NOT granted by pass 1** — pass 2 (the DT signature sweep, fresh session) + the P6 error-rate are owed. |
| OI-86 | L1/L2 PASS-1 layering findings (#7/#6): upward cross-layer deps — `metricweights.h:42`→`key/keymodeanalyzer.h` (L1.5→L3), `regiontonecollector.cpp:37` + `regiontoneprimitives.cpp:37/38`→`chord/` (L1.5→L4; the audit-Q2 back-edge is killed in the HEADER only, live in the .cpp); mixed-layer grab-bags (engravingbridge + metricweights host L2-legacy/L3/L4 code); two metric-weight tables (`regionMetricWeightForBeatType` vs `beatTypeToWeight`, #6 dup). Much rides existing retirements R4/R5/R6 + FQ-8/OI-13. Promoted DT-19. **PASS-2 refinements (`cc_l1l2_audit_pass2_report.md` §3/§5): DT-19 4 upward includes reproduced mechanically; `SpanWindowWeights` `decayRate=0.7`/`lookaheadWeight=0.5` are DT-3 value-copies of `scoreharvest::DECAY_RATE`/`LOOKAHEAD_WEIGHT` (a refit silently diverges); DT-16 4 raw-DOM note re-readers (`collectPitchContext`, `detectOnset/BassSubBoundaries`, `findTemporalContext`) — the mechanical reason those files are mixed-layer; all ride R5/R6/E4.** **Blind-re-run refinement (2026-07-11, `cc_l1l2_audit_blind_rerun_report.md` §5): the `regiontonecollector.cpp:37`→`analysisutils.h` upward include is not merely upward but UNUSED — none of its 6 exported symbols is referenced in that TU (grep-verified) — so it is removable outright (zero behavior change), which alone would delete that specific L1.5→L4 back-edge. Needs a build-confirm; removal itself waits for the E4 #8 timing.** | `cc_l1l2_audit_pass1_report.md` §3a/§3b; `cc_l1l2_audit_pass2_report.md` §3/§5; `cc_l1l2_audit_blind_rerun_report.md` §5; DT-19 | OPEN — dissolves at E4 retirements; re-verify at each |
| OI-88 | L1/L2 PASS-2 doc-precision findings (DT-12/#10, minor, non-correctness): (a) **stale file:line anchor** `slicer.h:68` cites `regionanalyzer.cpp:579` for `KeyModeSequenceDecoder::decode` — actual call at `:634`/`:705` (line 579 drifted to a Layer-1 comment); (b) `note_model.h:157-163` docstring "**no layer calls [`extend`] yet**" is contradicted by 3 gated production call sites (`regionanalyzer.cpp:702` behind `ReachBackOptions::enabled`=false; `chordslicedecoder.cpp:1387/1393` behind `enableEdgeExtension`; `textureclassifier.cpp:183/187`) — the dormancy SUBSTANCE holds (all gated off), only the wording is inaccurate. One-line doc fixes; do not touch code (#8). | `cc_l1l2_audit_pass2_report.md` §5-A/§5-B; `cc_l1l2_audit_blind_rerun_report.md` §4; DT-12 | ✅ RESOLVED 2026-07-11 (`f76e8b65c8`, comment-only, no behavior change): (a) `slicer.h` anchor rewritten symbol-led + cites both real call sites `:634`/`:705`; (b) `note_model.h` reworded to "dormant in SUBSTANCE, callers gated off on the production path" citing the 3 gated sites. Both re-verified at the code; the blind re-run independently re-found (b). |
| OI-90 | L3 PASS-1 file-table mis-tags (DT-21): the L1/L2 file-table tagged `decode/chordpathdecoder.h` "L3 key-mode decoder scaffolding" — it is the beam-1 **CHORD**-path decoder (Layer 4; includes `chord/chordanalyzer.h`, threads `ChordAnalysisResult`/`ChordIdentity` via `advanceTemporalContext`); `region/sparsechordrefinement.{h,cpp}` similarly re-tagged L4 (chord-quality refinement consuming the L3 key as a prior). Corrected in `gen_inventory.py --layer l3`; the L1/L2 `tools/audit/l1l2/file_table.csv` reason strings are now stale. Promoted DT-21. | `cc_l3_audit_pass1_report.md` §8; `tools/audit/l3/file_table.csv`; DT-21 | OPEN — correct the L1/L2 file-table reason at its next touch (comment/data-only; #8 no code) |
| OI-92 | L3 PASS-1 duplicated table (DT-3, #6): `jointkeydecision.cpp:73-88` `kJkdTemplates` (14-entry tertian chord vocabulary) is comment-declared "IDENTICAL to `tools/cc_joint_residual_probe.py` TEMPLATES" but NOT sync-test-guarded (unlike the `ModePriorPreset`↔`KeyModeAnalyzerPreferences` mode-prior dup, which `modepriorpresets_tests` guards) — a C++↔Python value-copy that silently diverges if either drifts. Diagnostic-only, gated OFF. | `cc_l3_audit_pass1_report.md` §5 OI-92; DT-3; OI-63 (mode-prior single-sourcing sibling) | OPEN — add a sync test or single-source at the joint-key wiring touch (#8) |
| OI-93 | L3 PASS-1 cross-layer deps (DT-19, #7): (a) `section/cadencekeyanchor.h:50` + `section/jointkeydecision.h:85` `#include chord/chordanalyzer.h` (a HEAVY L4 header) solely for `ChordQuality`, which lives in the dependency-free types leaf `analysistypes.h:120` — an avoidable header back-edge the types-leaf refactor removed for `keymodeanalyzer.h`/`regiontonecollector.h` but LEFT here (one-line include swap to the leaf); (b) 5 core-L3 `.cpp` include `chord/analysisutils.h` for `normalizePc`/`diatonicMaskFromFifths` — dependency-free pc primitives siloed under `chord/` (layering smell, light). | `cc_l3_audit_pass1_report.md` §5; `tools/audit/l3/pass1_dispositions.csv` (2 BACK-EDGE + 5 BACK-EDGE-NOTE); DT-19; OI-86 (L1/L2 sibling) | OPEN — fix (a) at the next section-header touch (#8); (b) rides a shared-pitch-utils leaf decision |
| OI-94 | L3 PASS-1 contract deferrals (P3 negative space; documented, not defects): (a) a mid-piece NOTATED key-signature CHANGE is not re-anchored — the decoder reads one signature at startTick and tracks a notated key change only via the note-driven change cost (`regionanalyzer.cpp:626-628`, "a deferred refinement"); (b) the A-3 dominant-implication key-evidence channel (L3 §15) is named but NOT built (= OI-68). | `cc_l3_audit_pass1_report.md` §3/§5 OI-94; OI-68 (A-3 capability track) | OPEN — (a) a deferred L3 refinement; (b) tracked at OI-68 |

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
| OI-87 | L1/L2 PASS-1 constant manifest-gap list (feeds EG-5/OI-6, DT-2): 16 hand-set inference-affecting constants NOT in `param_manifest.json` — beat-weight table 1.0/0.85/0.75/0.5 (`metricweights.cpp:77-82`), sliding-window LOOKBACK_BEATS 16 / LOOKAHEAD_BEATS 8 / DECAY_RATE 0.7 / LOOKAHEAD_WEIGHT 0.5 (`metricweights.h:57-60`), weightedPcView repetition-boost 0.3 + cross-voice 1.5 (`regiontonecollector.cpp:297/312`), phrase k 1.0 / minSilenceTicks 240 / coincidenceWeight 0.0 (`phraseboundaryview.h`) — [wGap/wInterOnset/wPitch/spikeCeilingFactor ARE in the manifest]. | `cc_l1l2_audit_pass1_report.md` §3c; `tools/audit/l1l2/pass1_dispositions.csv`; OI-6/EG-5; DT-2 | OPEN — Stage-5/EG-5 manifest extension |
| OI-91 | L3 PASS-1 constant manifest-gap (DT-2; the **L3 twin of OI-87**, feeds OI-6/EG-5): the ENTIRE L3 key/mode emission-scoring surface is absent from `tools/param_manifest.json` — the ~60 `KeyModeAnalyzerPreferences` weights/bonuses/penalties (`analysistypes.h`), the 21×5 `ModePriorPreset` mode priors (`modepriorpresets.cpp`), the `KeyModeSequencePreferences` change-cost/window settings, the cadence-anchor `kWeight*` (1.0/2.0/1.0/1.0), local-modulation `kEstablishmentMinChords`=5 / `kPitchTolerance`=2, the partial-sig `kPervasiveFraction`=0.03 / `kDominanceRatio`=2.0, and `JointKeyWeights` — ALL code-labeled "[empirical — Stage-5 fits]". The manifest (Stage-5 fitter Phase-0 inventory; production scope = "live rebuilt L1–L3") lists only the section annotate gate `kAnnotateKeyConfidenceThreshold` (group G10); **0 params sited in key/mode files**. [Cross-check whether `cowork_stage5_fitter_design.md` deliberately defers L3 key-emission fitting; if not, a coverage gap.] | `cc_l3_audit_pass1_report.md` §5 OI-91; `tools/audit/l3/pass1_dispositions.csv` (387 UNFIT); OI-6/EG-5/OI-87/OI-23/OI-25; DT-2 | OPEN — Stage-5/EG-5 manifest extension |

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
| OI-85 | L1/L2-audit Task-0 git-state incident: plumbing commits `eb624d442d`/`7123c7cb55` left the object DB + ref AHEAD of the working tree + main index (staged reversal of the session-36 doc arc + unmaterialized disk on 4 docs); resolved READ-ONLY via `git reset` (unstage) + `git restore` (materialize) with user authorization — nothing discarded (all files == HEAD). Plus a CONCURRENT-EDIT HAZARD: the working tree is live-edited by Cowork (the OI-43 edit; ref moves) — CC staged only its own files and appended (never rewrote) shared docs. Promoted DT-18. | `cc_l1l2_audit_pass1_report.md` §0; DT-18 | OPEN — convention owed (a plumbing commit ends with a main-index refresh + a disk-vs-HEAD verify) |
| OI-89 | L1/L2 pass-2 second reading was only PARTIALLY blind: the pass-2 instruction (Cowork-authored) required `STATUS.md` at Task 0 while `STATUS.md` carried pass 1's headline verdict ("spine is sound") — declared by CC in `cc_l1l2_audit_pass2_report.md` §0. Consequence (user decision 2026-07-11, principle-derived: the audit protocol's second-reading step requires full blinding; #19 forbids trusting a known-defective instrument because its defect "probably didn't matter"): **L1/L2 certification WITHHELD**; remedy = a fresh-session re-run of the blinded second reading + the error-rate measurement under a corrected instruction (`cc_instruction_l1_l2_audit_blind_rerun.md`: STATUS.md/OPEN_ITEMS.md/DEFECT_TYPES.md/handoff/both pass reports all withheld until the blind verdicts are frozen; new seeds; the 40 error-rate rows judged blind FIRST, then compared). Instruction-design failure promoted DT-20. | `cc_l1l2_audit_pass2_report.md` §0; `cc_l1l2_audit_blind_rerun_report.md`; DT-20; Cowork session 2026-07-11 | ✅ RE-RUN DONE 2026-07-11, remedy delivered: fully-blind reading (111 rows, seed 20260712) + error-rate (40 rows, seed 20260713), ALL verdicts frozen at `fbcb59c8d7` before any withheld file opened (strictly stronger blinding than pass 2 — STATUS.md not read until after the freeze). Result: reading 94/111 issue-agree, error-rate 35/40; **every disagreement is verdict-axis (retirement-map / DT-2 constants / DT-19 includes), ZERO correctness misses**; the leak moved the agreement NUMBERS (reading flag rate 23.6 %→1.8 %, error rate 0/40→12.5 %) but NOT the substance — pass 1/2's "spine sound, findings tracked" reproduced independently. **L1/L2 spine certification PROPOSED (report §5)** → **✅ CERTIFICATION GRANTED by the user, 2026-07-11, on the fully-blind re-run — row closed.** |
| OI-95 | L3-audit tooling debt: (a) **#6** — `tools/audit/l3/gen_l3_dispositions.py` is a SECOND disposition generator alongside the L1/L2 `tools/audit/gen_dispositions.py` (blinding forbade extending the withheld original during pass 1); unify into ONE layer-selected generator the way `gen_inventory.py --layer` was, now that blinding is lifted; (b) the committed `tools/audit/l1l2/{l1l2_functions.csv,l1l2_decls.csv,inventory.json}` are LINE-STALE vs current `note_model.h` (rows shifted +4; substance byte-identical — proven at the L3 inventory build) — a re-gen restamp owed at a convenient L1/L2 touch. | `cc_l3_audit_pass1_report.md` §5 OI-95 + §1; #6 | OPEN — housekeeping; (a) unify generators, (b) restamp l1l2 artifacts |

## E. User adjudication / ratification pending

| ID | item | source | status |
|---|---|---|---|
| OI-41 | #17(c) sharpening: "establish the mechanism FIRES (control flow) before tracing arithmetic" | PC doc §"hands" | ✅ RATIFIED 2026-07-10 — folded into CLAUDE.md #17(c) |
| OI-42 | Audit §5 UNCLEAR rows 1–7 — plain-language explanations + PRINCIPLE-DERIVED verdicts in `cowork_adjudication_dossier.md` Part A | adjudication dossier | ✅ RATIFIED 2026-07-10 — six were pure rule applications; the one genuine acceptance: A3, tolerating the quality-overwrite #12 violation until E4 (kept visible via OI-10) |
| OI-43 | Reopen the joint (key,chord) ranking question (user, handoff — there called "ponder-point 1"). Sharpened 2026-07-11 (Cowork): the arc-#12 probe decided the KEY FIRST (decode under argmax key, re-decode under carried alternatives) and graded only ROOT flips — the framing the research grounding §3 says to escape (Raphael & Stoddard single (tonic,mode,chord) state; Wu & Yoshii: sequential coupling = the pipeline to escape; "carry a beam of (key,chord) hypotheses, not commit to key first"). What the probe legitimately bounds: chord-axis benefit over the carried-key menu (oracle ceiling +0.6 pp; carried alts are collection siblings — that fact survives any framing). What it does NOT test: (1) the KEY AXIS — chord evidence re-ranking the key (key-agree ~68/64/67 % has more headroom than root-agree ~63 %); (2) a key menu wider than the carried `keyAlternatives`. NEXT ACTION when hold lifts: draft a read-only re-measure scoping under #17 — written quantitative prediction recorded first, key axis primary. | handoff; `cowork_functional_analysis_research_grounding.md` §3; Cowork session 2026-07-11 | ON HOLD (user, 2026-07-11) until CC's in-progress audit first half (OI-84) completes — then decision with user |
| OI-44 | Joint step B1–B4 status: design DELIVERED / build SHELVED / framing REOPENED (contradiction B) — needs one declared status | fitter O-4; §9.2 #6; handoff | OPEN — user |

## F. Doc-sync debt (#10) — annotate, don't rewrite history

| ID | item | source | status |
|---|---|---|---|
| OI-45 | scoring_model §4/§6 stale anchors + kHalfDimFirstInversionBonus missing from §6 | premise-debt T3-4 | OPEN — fix at next scoring_model touch |
| OI-46 | Audit §3/§4 tables contradict §3.1 build-status on FQ-1/FQ-3 stage (contradiction A) | audit | OPEN — annotate tables |
| OI-47 | STATUS.md submission-era sections (Current State BIR 25/16, Post-submission priorities, Known Gaps, Future Considerations, cowork_handoff.md dangling ref) contradict governing docs (contradiction C) | STATUS.md | OPEN — banner + triage (§G) |
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
| OI-75 | `keyAlternatives`/`keyConfidence`: ZERO production consumers (diagnostics only) — the L5 carry contract's key inputs sit unread. **L3 PASS-1 re-confirmed independently (2026-07-11, OI-75):** both are PUBLISHED-but-unconsumed (declared dormancy, consumer named = L5 modulation recompute); further, the production 0.8 KeyArea/cadence gate reads the emission SIGMOID (`keyModeResult.normalizedConfidence`), NOT the better-calibrated boundary MARGIN (`keyConfidence`, code-noted 2.8–3.1× better calibrated) — the deliberate D-L3a stance (relates OI-49 D-L3a "closed"-vs-"remains" contradiction). | siloed audit #4/#5; `cc_l3_audit_pass1_report.md` §5 OI-75; OI-49 | OPEN — consumed at L5 engage |
| OI-76 | Cadence detections transient (recomputed per emit path, never stored on regions); L5 cadence channel blocked; production detector circular by design | siloed audit #7 | OPEN — E4 |
| OI-77 | Bass-chord-tone/inversion VERDICT recomputed at ~60 call sites (facts shared, derivation duplicated) — channel #1 has no published form | siloed audit #11 | OPEN — E4 primitive |
| OI-78 | `declaredMode` siloed to the key path; chord diatonic bonus reads only the inferred key | siloed audit #12 | OPEN — design input |
| OI-79 | Duplicated constants: pedal sigmoid inlined (2.0/1.5) vs prefs; emission sigmoid written in two files (S10) | siloed audit #16 | OPEN — fold at next touch |
| OI-80 | Score-annotation input facts (chord symbols/RN/Nashville) recognized as TODO flags, never read | siloed audit #14 | OPEN — long-horizon |
| OI-81 | Key runner-up (closeness of the 2nd-best key) folded into a confidence number and discarded in-analyzer; only the batch tool serializes it — the L5 key-consistency channel wants it | siloed audit #6; dossier B6 | OPEN — E4 fact-publication design |
| OI-82 | Per-note beat weight / fine metric salience decoder-private (region-level IS published) | siloed audit #10; dossier B10 | OPEN — E4 fact-publication design (with OI-72/73/74) |
| OI-83 | Dispositions declared OK-BY-DESIGN, kept visible: `bothLicensed` (Stage-5 fitter telemetry) and the fan-out SUMMARY (diagnostic); the LOST uncapped readings behind the summary are the OI-9 distinct-root carry | siloed audit #8/#9; dossier B8/B9 | DECLARED — no action; the loss itself is OI-9 |

**Coverage note (user-challenged 2026-07-10): all 17 siloed-facts findings are now mapped** —
1→OI-72, 2→OI-73, 3→OI-15, 4/5→OI-75, 6→OI-81, 7→OI-76, 8→OI-83, 9→OI-9(+OI-83), 10→OI-82,
11→OI-77, 12→OI-78, 13→OI-4, 14→OI-80, 15→OI-11, 16→OI-79, 17→OI-74. Items 1/2/3/10/17 are ONE
design decision (the E4 fact-publication/surface design — dossier Part B); the proposed
"publish-once, consumers-read" corollary awaits ratification (dossier, end of Part B).

*Sweep provenance: session-36 full-repo sweep (12 surfaces, 91 raw items, 11 contradictions) —
the raw sweep detail with file:line citations is preserved in the session record; rows above
consolidate duplicates (e.g. pedal appears once as OI-4 with merged sources). Items marked
MERGED/superseded stay listed until their absorbing row closes.*

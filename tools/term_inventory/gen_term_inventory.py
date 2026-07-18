#!/usr/bin/env python3
"""Generate the term-inventory artifact for the term-level theory-grounding audit.

Dispatch: cc_instruction_term_inventory.md (Cowork, 2026-07-18) — the code-enumeration
half of the joint-estimator design pass (cowork_joint_estimator_architecture.md §4 step 1).

What is generated vs hand-verified (#17f):
- The TERM ROWS below are HAND-VERIFIED readings of the source (each row was read at the
  cited file:line during the 2026-07-18 sweep; hand_verified=yes on every row). They are
  data in this script so the derivable columns and every count in the report are computed
  mechanically, never hand-typed.
- MECHANICALLY DERIVED by this script: param_manifest.json coverage per constant name; all
  summary counts (per layer / liveness / roster factor / provenance / manifest coverage);
  the OI-23 measured figures; the template-count staleness check (parsed from source + doc);
  the scoring_model.md name-mention check; the DT-26 tree-wide identifying-pattern sweep
  with its per-file disposition (the script FAILS if a hit file has no disposition); and
  the OI-179 multiply-annotated ground-truth census (computed live from tools/corpus +
  the When-in-Rome tree through dcml_parser._build_wir_index).

Outputs (written next to this script):
- term_inventory.csv          — one row per term (the Task-1 deliverable)
- term_inventory_summary.json — every figure the report cites
Run:  python tools/term_inventory/gen_term_inventory.py
"""

import csv
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# ─────────────────────────────────────────────────────────────────────────────
# Roster factors (cowork_joint_estimator_architecture.md §2, quoted keys)
# ─────────────────────────────────────────────────────────────────────────────
ROSTER = {
    "F1": "NCT-cleaned tone collections / pitch content -> emission P(pitches|tonic,mode,chord)",
    "F2": "notated signature + declared mode -> prior on (tonic, mode)",
    "F3": "notated spelling + accidentals -> spelling-conditioned emission + mode disambiguation",
    "F4": "cadence votes + leading-tone events -> emission/transition factor on (tonic,mode) at cadences",
    "F5": "progression grammaticality -> chord transition term",
    "F6": "harmonic rhythm + boundary strength -> segmentation (semi-Markov duration) model",
    "F7": "beat strength / metric position -> emission weighting + chord-change-on-strong-beat prior",
    "F8": "fermatas + phrase facts -> segment-boundary and cadence-location priors",
    "F9": "bass-motion skeletons -> bass/inversion emission",
    "NONE": "maps to no §2 roster factor (keep/fix/drop input for the design pass)",
}

# ─────────────────────────────────────────────────────────────────────────────
# THE TERM ROWS (hand-verified at the cited lines, 2026-07-18 sweep).
# Tuple: (name, layer, liveness, decl_site, apply_site, form, constants, consumers,
#         roster_factor, notes)
# constants: "name=value [provenance]; ..." — names are matched against
# tools/param_manifest.json mechanically. provenance: hand-set | fit-adopted |
# derived | preset-table | study-fitted | swept | structural (no numeric value).
# ─────────────────────────────────────────────────────────────────────────────
CA = "src/composing/analysis/chord/chordanalyzer.cpp"
AT = "src/composing/analysis/types/analysistypes.h"
HFL_H = "src/composing/analysis/function/harmonicfunctionlayer.h"
HFL_C = "src/composing/analysis/function/harmonicfunctionlayer.cpp"
PSG = "src/composing/analysis/chord/postscoringgates.cpp"
CPP2 = "src/composing/analysis/chord/chordpostpasses.cpp"
SCR = "src/composing/analysis/region/sparsechordrefinement.cpp"
RA = "src/composing/analysis/region/regionanalyzer.cpp"
KMA_C = "src/composing/analysis/key/keymodeanalyzer.cpp"
KMS_H = "src/composing/analysis/key/keymodesequence.h"
KMS_C = "src/composing/analysis/key/keymodesequence.cpp"
KR = "src/composing/analysis/key/keyresolver.cpp"
MPP = "src/composing/analysis/key/modepriorpresets.cpp"
HS_H = "src/composing/analysis/harmony/harmonicsegmenter.h"
HS_C = "src/composing/analysis/harmony/harmonicsegmenter.cpp"
MW_H = "src/composing/analysis/scoreharvest/metricweights.h"
MW_C = "src/composing/analysis/scoreharvest/metricweights.cpp"
RTC_C = "src/composing/analysis/engravingbridge/regiontonecollector.cpp"
RTC_H = "src/composing/analysis/engravingbridge/regiontonecollector.h"
RTP = "src/composing/analysis/engravingbridge/regiontoneprimitives.cpp"
PBV_H = "src/composing/analysis/engravingbridge/phraseboundaryview.h"
SA_H = "src/composing/analysis/section/sectionanalyzer.h"
SA_C = "src/composing/analysis/section/sectionanalyzer.cpp"
SCD = "src/composing/analysis/section/sectioncadencedetection.cpp"
CKA = "src/composing/analysis/section/cadencekeyanchor.cpp"
LMD = "src/composing/analysis/section/localmodulationdetector.cpp"
JKD_H = "src/composing/analysis/section/jointkeydecision.h"
CSD_H = "src/composing/analysis/chord/chordslicedecoder.h"
CSD_C = "src/composing/analysis/chord/chordslicedecoder.cpp"
FC_H = "src/composing/analysis/function/functioncadence.h"
FM_H = "src/composing/analysis/function/functionmodulation.h"
FR_H = "src/composing/analysis/function/functionresolver.h"
FO_H = "src/composing/analysis/function/forwardoverride.h"
FOUT_H = "src/composing/analysis/function/functionoutput.h"
PR_H = "src/composing/analysis/progression/progressionrecognizer.h"
TC_H = "src/composing/analysis/voiceleading/textureclassifier.h"
BA = "tools/batch_analyze.cpp"
NIB = "src/notation/internal/notationimplodebridge.cpp"

TERMS = [
    # ── L4 scoring oracle (LIVE) ─────────────────────────────────────────────
    ("scoreTemplateTones", "L4-oracle", "live", f"{CA}:450-463", f"{CA}:1467",
     "additive weighted presence sum per template tone; per-position factor x min(weight, cap)",
     "kRootToneFactor=1.8 [hand-set]; kSecondToneFactor=1.2 [hand-set]; kOtherToneFactor=1.0 [hand-set]; kTemplateToneWeightCap=3.0 [hand-set]",
     "basisIndepMatrix -> cell.basisIndep -> competition pipeline", "F1",
     "root>second>other ordering claimed theory-grounded in code comment; values empirical"),
    ("scoreExtraNotes", "L4-oracle", "live", f"{CA}:473-544", f"{CA}:1468",
     "signed additive per non-template pc: Extension +factor*min(w,cap); Contradiction -kContradictionPenalty*...; Foreign -kForeignPenalty*...",
     "kContradictionPenalty=0.75 [hand-set]; kExtensionFactor7th=0.45 [hand-set]; kExtensionFactorFlat13=0.20 [hand-set]; kExtensionFactorDefault=0.35 [hand-set]; kForeignPenalty=0.45 [hand-set]; kExtraNoteWeightCap=2.0 [hand-set]",
     "basisIndep -> competition pipeline", "F1",
     "inline bars: w<0.01 not-sounding cutoff (:487); M3/P4-absent contradiction overrides test <0.1 (:505/:511)"),
    ("Sus4 TPC third disambiguation", "L4-oracle", "live", f"{CA}:98-99", f"{CA}:~520 (inside scoreExtraNotes)",
     "spelling-conditioned extension factor override for interval 3 over Sus4: Eb spelling -> 0.10, D# spelling -> 0.45",
     "kSus4FlatThirdFactor=0.10 [hand-set]; kSus4SharpThirdFactor=0.45 [hand-set]",
     "scoreExtraNotes", "F3", "one of the few live spelling-conditioned emission terms"),
    ("dim7CharacteristicBonus", "L4-oracle", "live", f"{CA}:555-585", f"{CA}:1469-1470",
     "conditional additive bonus = rotation selector: Diminished + dim7 pc sounding + full triad + dim7 pc NON-diatonic to signature collection (pcInMask)",
     "kDim7CharacteristicBonus=0.75 [hand-set]",
     "basisIndep", "F1",
     "OI-168-fixed form (signature mask, no tonic); THE dim7 rotation-selection mechanism (do not remove without replacement)"),
    ("nonBassAdjustment", "L4-oracle", "live", f"{CA}:632-654", f"{CA}:1581",
     "subtractive penalty for Min7/4-note-Sus4/HalfDim with root!=bass; waived on full TPC spelling match",
     "kNonBassPenalty=0.35 [hand-set]",
     "basisDep", "F9", "TPC waiver is a spelling-conditioned exception (F3 aspect)"),
    ("structuralPenalties", "L4-oracle", "live", f"{CA}:660-743", f"{CA}:1471",
     "subtractive template-family consistency penalties (missing defining tones; enharmonic ambiguity; power-chord vs triad)",
     "kSus4MissingFourth=0.70 [hand-set]; kSus4StructuralFourthThreshold=0.50 [hand-set]; kSus4VariantMissing7th=0.70 [hand-set]; kSus4Maj7MissingP5=0.50 [hand-set]; kDom7FlatFiveTpcPenalty=0.55 [hand-set]; kDom7FlatFiveMissing7th=0.50 [hand-set]; kPowerChord3PcPenalty=0.30 [hand-set]",
     "basisIndep", "F1",
     "inline 0.05 presence bars at :697/:709/:731 (OI-106b); distinctPcs>=3 power gate :738"),
    ("tpcConsistencyBonus", "L4-oracle", "live", f"{CA}:748-754", f"{CA}:1472",
     "additive per non-root template tone whose authored TPC matches the expected circle-of-fifths delta",
     "tpcConsistencyBonusPerTone=0.20 [hand-set]",
     "basisIndep", "F3", "the main live spelling-conditioned chord emission term"),
    ("appliedBassRootBonus + bassRootBonusMultiplier", "L4-oracle", "live", f"{CA}:756-805,872-883", f"{CA}:1574-1581",
     "additive bass-root reward x support-shell multiplier (full 1.0 / shell 0.3 / bare 0.1)",
     "bassNoteRootBonus=0.70 [hand-set]; bassRootThirdOnlyMultiplier=0.3 [hand-set]; bassRootAloneMultiplier=0.1 [hand-set]; kBassSupportPresenceThreshold=0.05 [hand-set]",
     "basisDep + cell.appliedBassBonus (threshold de-inflation)", "F9", ""),
    ("diatonicRootContribution", "L4-oracle", "live", f"{CA}:910-917", f"{CA}:1473",
     "additive bonus when candidate root is in the key SIGNATURE's diatonic collection (pcInMask(diatonicMaskFromFifths(fifths), pc); no tonic, no mode scale)",
     "diatonicRootBonus=0.30 [hand-set]",
     "basisIndep", "NONE",
     "P(chord-root | key collection) coupling; nearest joint-model home: the key-conditioned chord emission (the OI-168-fixed signature-mask FORM, arch doc §3)"),
    ("complexityFactor", "L4-oracle", "live", f"{CA}:1476-1483", f"{HFL_C}:427",
     "multiplicative discount when evidenceRatio(distinctPcs/templateTones) < floor: factor = floor + ratio; else 1.0",
     "kComplexityEvidenceFloor=0.5 [hand-set]",
     "score multiply (cf)", "F1", "Iter-74 FixA; one constant serves as threshold AND additive floor"),
    ("augFactor", "L4-oracle", "live", f"{CA}:1487-1505", f"{HFL_C}:427",
     "multiplicative halving (x0.5, can apply twice) for Augmented templates on thin/bare-root evidence",
     "kAugThinEvidenceFactor=0.5 [hand-set]",
     "score multiply (af)", "F1", "Iter-78/79"),
    ("wComplete", "L4-oracle", "live", f"{CA}:1519-1550", f"{HFL_C}:428",
     "flat additive bonus: joint scoring + root-position + exactly 3 distinct pcs + all triad tones present > presence bar",
     "kWComplete=0.50 [hand-set]; kWCompletePresenceThreshold=0.05 [hand-set]",
     "post-multiply score add", "F9", "Iter-92; root-position complete triads outrank slash readings"),
    ("detectExtensions thresholds", "L4-oracle", "live", f"{CA}:270-383", f"{CA}:976,981,997,1095",
     "hard presence thresholds deciding identity extension bits (not score)",
     "kSeventhThreshold=0.12 [hand-set]; kExtensionThreshold=0.20 [hand-set]",
     "identity.extensions", "F1",
     "inline higher bars 0.3 (#11 :357, b13 :377) and 0.2 (:378) — OI-106b class"),
    ("pcWeight floor max(0.1, w)", "L4-oracle", "live", f"{CA}:1133", f"{CA}:1133",
     "per-tone weight floor before scoring (every sounding tone counts at least 0.1)",
     "pcWeightFloor=0.1 [hand-set, inline]",
     "pcWeight histogram", "F7", "interacts with kSeventhThreshold (must exceed the floor)"),
    ("bass-candidate enumeration", "L4-oracle", "live", f"{CA}:1161,1176-1276", f"{CA}:1248-1252",
     "hard gates: enumeration fires on (onset-true AND onset-false present) OR sparse-upper (distinctPc<=2, >=2 cands, lowestPitch>60); weight filter fraction; cap 4 candidates",
     "bassPassingToneMinWeightFraction=0.05 [hand-set]; bassCandCap=4 [hand-set, inline]; registerCutoffMidi=60 [hand-set, inline]",
     "joint (bass,root,template) grid", "F9", "Iter-92 joint scoring"),
    ("hasStructuralBass", "L4-oracle", "live", f"{CA}:1320", f"{CA}:1600-1605",
     "hard gate: lowestPitch<=60 OR distinctPcs>=3; ANDed into inversion-bonus eligibility flags",
     "structural (bars 60 / 3) [hand-set, inline]",
     "supportsInversionBonuses / qualifiesCompleteTriad", "F9", "sparse upper-register bass gets no inversion bonuses"),
    ("jointScoringEnabled", "L4-oracle", "live", f"{CA}:1166-1172", f"{HFL_C} (wSeq/wDim/wStep gates)",
     "hard gate: any tone has onsetAtRegionStart or distinctMetricPositions>0 (i.e. came from regional accumulation)",
     "structural",
     "wComplete/wSeq/wDim/wStep firing", "F7", ""),
    ("minDistinctPcsForCandidate", "L4-oracle", "live", f"{AT}:374", f"{CA}:1304",
     "hard admission gate: fewer distinct pcs than this -> no candidates (segmenter relaxes to 1; Pass-1 sparse-admission retries at 1)",
     "minDistinctPcsForCandidate=3 [hand-set]",
     "analyzeChord admission", "F1", ""),
    ("buildChordResult: degree + diatonicToKey", "L4-oracle", "live", f"{CA}:1002-1062", "published on ChordAnalysisResult",
     "lookup: degree = index of rootPc in (keyTonicPc + parent-scale) — TONIC-relative; diatonicToKey = degree>=0 AND every pc with weight>0.2 in parent scale",
     "diatonicWeightBar=0.2 [hand-set, inline]",
     "post-scoring gates read scale/keyTonicPc; published flag read by notationimplodebridge.cpp:1205", "NONE",
     "OI-170/OI-173 carried defect sites (class-(a) collection-through-tonic; parent-scale degree basis); default-OFF signature-mask twin :1038-1062"),
    ("quality normalizations in buildChordResult", "L4-oracle", "live", f"{CA}:921-998", "results[]",
     "hard rewrites: augmented root correction (bass pc present>0.05); Sus2->Sus4 upgrade when P4 sounding; Sus->Major+omitsThird when Maj7 present and no third (>0.2 bars)",
     "presenceBars=0.05/0.2 [hand-set, inline]",
     "results[] identity", "F1", ""),

    # ── L4 competition pipeline (LIVE) ───────────────────────────────────────
    ("rootContinuityBonus + Gate R", "L4-competition", "live", f"{AT}:219; {HFL_C}:54-58,237-242,274-284", f"{HFL_C}:423-425",
     "additive continuity bonus when candidateRoot==previousRoot, folded pre-multiply; Gate R (hard) zeroes it when rcb>0 AND fullBasisDep<=0 AND bass foreign to template (kMasks lookup), Final phase only",
     "rootContinuityBonus=0.40 [hand-set]",
     "competition score", "F5",
     "self-transition prior in disguise; Gate R masks derived from kTemplateIntervals [derived]"),
    ("resolutionEdgeBonus", "L4-competition", "live", f"{AT}:226; {HFL_C}:120-146", f"{HFL_C}:410-412",
     "additive: prevDim->Maj/min semitone up; prevHalfDim->Maj P4 up; prevAug->same root",
     "resolutionBonus=0.35 [hand-set]",
     "fullBasisIndep (pre-multiply)", "F5", "a 3-rule resolution-grammar fragment"),
    ("inversionContextBonus (4 bonuses + cap)", "L4-competition", "live", f"{AT}:245-287; {HFL_C}:148-179", f"{HFL_C}:413-417",
     "additive sum: completeTriad (stepwise evidence) + stepwiseFromPrev + stepwiseToNext + sameRoot, clamped at cap (cap non-binding: sums 1.85/0.75)",
     "stepwiseBassInversionBonus=0.5 [hand-set]; stepwiseBassLookaheadBonus=0.5 [hand-set]; completeTriadInversionBonus=0.45 [hand-set]; sameRootInversionBonus=0.4 [hand-set]; maxTotalInversionContextBonus=2.0 [hand-set]",
     "fullBasisDep", "F9", "Jazz preset overrides: 0.20/0.20/0.20/0.15 (batch_analyze.cpp:4230-4233)"),
    ("wSeqBonus", "L4-competition", "live", f"{HFL_H}:125; {HFL_C}:60-67", f"{HFL_C}:429-432",
     "additive: next root a P4 above candidate root (V->I), distinctPcs>=4, Final phase",
     "kWSeq=0.20 [hand-set]",
     "post-multiply score add", "F5", ""),
    ("wDimBonus + post-bonus quality guard", "L4-competition", "live", f"{HFL_H}:126; {HFL_C}:69-78,479-496", f"{HFL_C}:433-438",
     "additive: Dim/HalfDim one semitone below next root, distinctPcs>=4; guard: accept with-wDim winner only if Dim/HalfDim else fall back",
     "kWDim=0.15 [hand-set]",
     "winner variant selection", "F5", "rotation-correction signal, not quality-flip (guard enforces)"),
    ("wStepIn/wStepOut + surgical guard", "L4-competition", "live", f"{HFL_H}:127-129; {HFL_C}:89-111,309-353", f"{HFL_C}:451-454",
     "additive stepwise-bass bonuses (root-position, non-Power, Final phase); blocked when an m7-family competitor a m3 below bass is within kStepBudget",
     "kWStepIn=0.125 [fit-adopted (2.2e); 0.10 on Jazz/Standard carriers]; kWStepOut=0.10 [hand-set]; kStepBudget=0.235 [derived kWStepIn+kWStepOut+0.01]",
     "post-multiply score add", "F9",
     "the ONLY robust-unit-fitted value in the system (OI-23); 4 load-bearing gates"),
    ("ScoringPhase gating", "L4-competition", "live", f"{AT}:386; {HFL_C}:374", "all progression-signal call sites",
     "hard phase gate: Segmentation phase suppresses wStep/wSeq/wDim and Gate R (rcb stays active)",
     "structural",
     "segmentation vs final scoring", "F6", "keeps segmentation independent of progression signals"),
    ("kScoreThresholdRatio + result cap + diff-root append", "L4-competition", "live", f"{HFL_H}:135; {HFL_C}:508-549", f"{HFL_C}:510,521,524,533-549",
     "carry policy: threshold=(best - winnerBassBonus)*ratio; cap 3 results; guaranteed different-root append when winner bass-rooted",
     "kScoreThresholdRatio=0.75 [hand-set]; resultCap=3 [hand-set, inline]",
     "results[]/alternatives[] (L5-consumed carry)", "NONE",
     "output-surface carry policy, not an inference factor; information-loss relevant (#12, OI-9)"),
    ("cross-bass winner selection + tie policy", "L4-competition", "live", f"{HFL_C}:388-504", f"{HFL_C}:499-504",
     "argmax over all (bass,root,template) cells; exact-double compare, then lower tiePriority (template index), then lower rootPc",
     "structural",
     "committed winner", "NONE", "near-ties unprotected (documented FP fragility)"),

    # ── L4 post-scoring gates (LIVE) ─────────────────────────────────────────
    ("gate outer guard", "L4-gates", "live", f"{PSG}:154-157", f"{PSG}:154",
     "hard gate over ALL rules: inversionSuspicionMargin>0 AND inversionBonusReduction<1 AND >=2 results AND distinctPcs>=3",
     "inversionSuspicionMargin=0.70 [hand-set]; inversionBonusReduction=0.0 [hand-set]",
     "whole gate block", "NONE", "disabling the margin disables every gate (pinned F2/F3)"),
    ("bias correction", "L4-gates", "live", f"{PSG}:320-360", f"{PSG}:334-339",
     "subtractive deduction bassNoteRootBonus*(1-reduction) from bass-root Maj/Min winner when margin < suspicion margin; seventh-exempt; then stable re-sort",
     "inversionSuspicionMargin=0.70 [hand-set]",
     "re-ranked results[]", "F9", "counteracts bass-root bonus over-fire on inversions"),
    ("HalfDim first-inversion bonus", "L4-gates", "live", f"{PSG}:48,217-239", f"{PSG}:351-356",
     "additive bonus to a HalfDim inversion alt inside the flip block (preferMinorOverMajorAdd6 carriers)",
     "kHalfDimFirstInversionBonus=0.55 [hand-set]",
     "bias-correction re-sort", "F9", "Iter-61 Option B"),
    ("FM2 enharmonic flip (Major-add6 <-> Minor7)", "L4-gates", "live", f"{PSG}:273-282", f"{PSG}:278",
     "hard promotion (swap-or-append) of Minor at (root+9)%12 when winner Major+add6, preset-gated",
     "preferMinorOverMajorAdd6=true(Baroque/Standard)/false(Jazz/Default) [hand-set preset]",
     "winner", "NONE",
     "enharmonic-identity disambiguation; nearest factor: spelling-conditioned emission (F3) should decide this"),
    ("Gate E (first-inversion Minor->Major)", "L4-gates", "live", f"{PSG}:295-311", f"{PSG}:307",
     "hard swap: winner Minor, Major alt at (root+8)%12 sounding, stepwise bass evidence",
     "structural (uses extensionThreshold)",
     "winner", "F9", "DEFER disposition (Stage-5 audit)"),
    ("Gates G-E / G-D (Minor-add6 <-> HalfDim7)", "L4-gates", "live", f"{PSG}:380-407", f"{PSG}:403",
     "hard promotion of HalfDim7 at (root+9)%12: G-E on key-degree membership {LT, supertonic, mediant} (TONIC-relative); G-D on >=2 consecutive stepwise bass",
     "structural (degree offsets 11/2/4; count>=2)",
     "winner", "NONE",
     "G-E is a genuine-tonic (degree) site — OI-170 class-(b), 58 winner swaps Baroque; enharmonic disambiguation via key function"),
    ("Gate H (augmented rotation)", "L4-gates", "live", f"{PSG}:421-461", f"{PSG}:441-461",
     "hard swap among augmented enharmonic rotations {+4,+8} on temporal sub-gates (next-root match / recent roots / stepwise count>=2)",
     "structural",
     "winner", "NONE", "class-(a) rotation churn family; DEFER disposition"),
    ("Gate I (first-inversion Major over root-position Minor)", "L4-gates", "live", f"{PSG}:46,474-518", f"{PSG}:517-518",
     "hard swap: same bass, I4 interval, root diatonic (TONIC-anchored scale loop — OI-170 class-(a) site), margin <= kGateIMargin",
     "kGateIMargin=0.45 [hand-set]",
     "winner", "F9", "RETAIN-structural (disabling adds +5 class-(b) Jazz)"),
    ("Gate L (Major over Augmented same-root)", "L4-gates", "live", f"{PSG}:47,541-576", f"{PSG}:575-576",
     "hard swap: Major alt at same root+bass, diatonic (TONIC-anchored — OI-170 class-(a) site), margin <= kGateLMargin, seventh-excluded",
     "kGateLMargin=0.35 [hand-set]",
     "winner", "NONE", "quality correction (Aug->Maj); RETAIN (18 Jazz sites)"),
    ("Gate J (viio -> V7)", "L4-gates", "live", f"{PSG}:592-612", f"{PSG}:608",
     "hard swap: root-position Dim triad with M3-below pc sounding -> Major+m7 rooted there (V6/5 reading)",
     "structural (uses extensionThreshold)",
     "winner", "F5", "RETAIN (catastrophic on Jazz if disabled)"),

    # ── L4 post-passes (LIVE) ────────────────────────────────────────────────
    ("Iter-86 bass-b7 promotion", "L4-postpass", "live", f"{CPP2}:135-149", f"{CPP2}:147",
     "in-place extension stamp: bass at b7 of a plain Maj/Min winner above extensionThreshold -> MinorSeventh added",
     "structural (interval 10)",
     "winner extensions (suppresses pedal check)", "F9", ""),
    ("Iter-91 bass-as-root promotion", "L4-postpass", "live", f"{CPP2}:163-188", f"{CPP2}:183-186",
     "hard append-promotion when next region's root equals current bass and delta/quality pattern matches (A: 8+Minor, B: 9+Major)",
     "structural (deltas 8/9)",
     "winner", "F5", "forward-context gated"),
    ("pedal-point two-pass check", "L4-postpass", "live", f"{CPP2}:190-277", f"{CPP2}:271-277",
     "conditional replacement: bass not a chord tone + >=2 upper pcs -> re-analyze upper voices; commit when sigmoid(1/(1+exp(-1.5*(gap-2.0)))) >= threshold",
     "pedalConfidenceThreshold=0.65 [hand-set]; pedalSigmoidSteepness=1.5 [hand-set, inline]; pedalSigmoidMidpoint=2.0 [hand-set, inline]",
     "committed results + isPedalPoint", "F1", "sigmoid literals inlined (OI-79 duplication)"),

    # ── L4 commit-path refinements (LIVE) ────────────────────────────────────
    ("applyTonicPriorToSparseChord", "L4-commit", "live", f"{SCR}:182-223", f"{RA}:1017",
     "hard quality overwrite: thin quality (Power/Sus2/Sus4) + <=2 distinct pcs + root is a diatonic DEGREE -> degree's diatonic triad quality",
     "structural (distinctPc bar 2)",
     "committed quality (before decoder.commit)", "NONE",
     "OI-172: live genuine-tonic identity write (172/183/172 overwrites); P(chord-quality | degree) prior in disguise"),
    ("refineSparseChordQualityFromKeyContext + Aeolian guard", "L4-commit", "live", f"{SCR}:122-180", f"{RA}:1015,1233,1423",
     "Unknown-quality upgrade to the degree's diatonic triad; guard: lone tonic/dominant pc in Aeolian stays Unknown",
     "structural",
     "committed quality", "NONE", "sibling of OI-172 (this one only acts on Unknown)"),

    # ── L2 segmentation (LIVE) ───────────────────────────────────────────────
    ("Round-1 anchor gates", "L2", "live", f"{HS_H}:43-47; {HS_C}:639-674", f"{HS_C}:722-746",
     "per-region hard threshold filter (no global objective): on-beat + duration >= scaled min + staves >= 75% mean + analyzeChord winner score >= scaled min",
     "kAnchorMinScore=1.5 [hand-set]; kAnchorMinDurationTicks=480 [hand-set]; staveFraction=0.75 [hand-set, inline]; kRefActiveStaves=3.5 [hand-set]; kScoreFloorFraction=0.75 [hand-set]",
     "greedyExpandSegmentation anchors", "F6",
     "audit disposition: L2-LEGACY, retires R6 (slicer successor wired but legacy path still live)"),
    ("Round-2 gap-fill", "L2", "live", f"{HS_H}:52; {HS_C}:422-555", f"{HS_C}:455-555",
     "fill between anchors: sort candidates by score desc; promote if score >= scaled kRound2MinScore and harmonically distinct from neighbours; long gaps (>4x min duration) drop bilateral context",
     "kRound2MinScore=1.25 [hand-set]; longGapMultiplier=4 [hand-set, inline]",
     "segmentation regions", "F6", ""),
    ("head-gap tonic prior (Iter-74 Fix-B)", "L2", "live", f"{HS_C}:848-889", f"{HS_C}:860-889",
     "hard identity overwrite: synthesized head region whose winner is not tonic-rooted and margin < 0.4 gets a tonic-rooted alternative or the modal tonic triad outright",
     "kHeadGapTonicPreferenceMargin=0.4 [hand-set]",
     "committed head region root/bass/quality", "NONE",
     "OI-175: the third live chord-deciding genuine-tonic site (first outside L4); fire count unmeasured"),
    ("head/tail gap synthesis gates", "L2", "live", f"{HS_C}:823,915", f"{HS_C}:823,915",
     "synthesize covering region only when top candidate score > 0; tail synthesis has NO tonic prior",
     "structural",
     "segmentation coverage", "F6", ""),
    ("Pass-2 onset-Jaccard sub-boundaries", "L2", "live", f"{RTC_H}:194; {RTP}:279-368", f"{RTP}:360",
     "hard: Jaccard distance of consecutive onset sets >= threshold AND >= 2 quarter notes since last boundary",
     "onsetBoundaryThreshold=0.25 [hand-set]; minGapTicks=960 [hand-set, inline]",
     "region subdivision", "F6", "live callers pass opts.onsetBoundaryThreshold (kDefaultOnsetBoundaryThreshold)"),
    ("Pass-2b bass-movement sub-boundaries", "L2", "live", f"{RTC_H}:207; {RTP}:370-449", f"{RTP}:441",
     "hard: ANY bass pc change with >= 2 quarter notes gap fires a boundary; iterated up to 8 passes",
     "minGapTicks=960 [hand-set]; kMaxBassMovementPasses=8 [hand-set]",
     "region subdivision", "F6", ""),
    ("region size floors + coalesce", "L2", "live", f"{MW_H}:68-69; {RA}:67-68,123-169,246-251", f"{RA}:251,1088,1287",
     "hard floors: Pass-2/2b eligibility 4 quarters; Pass-3 absorbs regions < 1 quarter; short same-root runs (>=3 regions, >=720 ticks) coalesce",
     "kMinRegionTicks=480 [hand-set]; kPass2MinRegionTicks=1920 [hand-set]; kPass2bMinRegionTicks=1920 [hand-set]; kCoalesceMinRunTicks=720 [derived]; kCoalesceMinRunCount=3 [hand-set]",
     "final region stream", "F6", ""),
    ("Pass-1 sparse-admission fallback", "L2", "live", f"{RA}:896-911", f"{RA}:911",
     "retry Pass 1 with minDistinctPcsForCandidate=1 when the first attempt returns empty",
     "structural",
     "region stream (0-region regression guard)", "F6", "Iter 75"),
    ("change-point slicer", "L2", "live", "src/composing/analysis/slicing/slicer.cpp:40-105", f"{RA}:579,651",
     "structural: boundaries = every eligible note onset/release, clipped; NO numeric terms",
     "structural",
     "slice stream (L3 decode substrate)", "F6", "coexists with legacy greedy-expand (declared transition)"),

    # ── L1.5 derived views (LIVE) ────────────────────────────────────────────
    ("regionMetricWeightForBeatType table", "L1.5", "live", f"{MW_C}:73-84", f"{RTC_C}:158,168,229; {RA}:985",
     "lookup table: DOWNBEAT 1.0 / STRESSED 0.85 / UNSTRESSED 0.75 / default 0.5",
     "beatWeights=1.0/0.85/0.75/0.5 [hand-set table]",
     "region tone base weight", "F7", "one of TWO metric-weight tables (#6 dup with beatTypeToWeight, OI-86)"),
    ("beatTypeToWeight (key-path beat weights)", "L1.5", "live", f"{MW_C}:39-53; {AT}:816-822", f"{RTP}:153,213",
     "prefs-driven lookup: 7 beat-type weights (downbeat 1.0, stressed 0.7, unstressed 0.4, subbeat 0.2)",
     "beatWeightDownbeat=1.0 [hand-set]; beatWeightCompoundStressed=0.7 [hand-set]; beatWeightSimpleStressed=0.7 [hand-set]; beatWeightCompoundUnstressed=0.4 [hand-set]; beatWeightSimpleUnstressed=0.4 [hand-set]; beatWeightCompoundSubbeat=0.2 [hand-set]; beatWeightSubbeat=0.2 [hand-set]",
     "key-path pitch context weighting", "F7", ""),
    ("timeDecay + span window", "L1.5", "live", f"{MW_H}:57-60,104; {MW_C}:110-113", f"{RTP}:158,267; {KMS_C}:86-87",
     "exponential decay decayRate^(beatsAgo/beatsPerUnit); lookahead notes weighted 0.5; window sizes 16/8 beats",
     "DECAY_RATE=0.7 [hand-set]; LOOKAHEAD_WEIGHT=0.5 [hand-set]; LOOKBACK_BEATS=16 [hand-set]; LOOKAHEAD_BEATS=8 [hand-set]",
     "key-path pitch context; L3 decoder emission windows", "F7",
     "SpanWindowWeights defaults 0.7/0.5/4.0 are DT-3 value-copies (OI-86)"),
    ("weightedPcView base weight + boosts", "L1.5", "live", f"{RTC_C}:236-314", f"{RTC_C}:381-390",
     "tone.weight = (durationInRegion/regionDuration) x beat weight; then repetition boost x(1+0.3*(distinctOnsets-1)); cross-voice boost x1.5; normalized to sum 1",
     "repetitionBoost=0.3 [hand-set, inline]; crossVoiceBoost=1.5 [hand-set, inline]",
     "ChordAnalysisTone.weight -> analyzeChord pcWeight", "F7", "OI-86/OI-87 constants; loudness never enters (OI-58 residue)"),
    ("pedal-tail carry", "L1.5", "live", f"{RTC_C}:151,316-341; {AT}:325", f"{RTC_C}:334",
     "sustain-pedal tail contribution: (tailDuration/regionDuration) x attack beat weight x multiplier; gather window 4 whole notes back",
     "pedalTailWeightMultiplier=0.3 [hand-set]; backWindowWholeNotes=4 [hand-set, inline]",
     "tone.weight", "F7", "flat discount, no decay (OI-58 item 5)"),
    ("dense-start lookahead exclusion", "L1.5", "live", f"{RTC_C}:206,220,280", f"{RTC_C}:220",
     "hard: >=3 pcs sounding at region start (batch path only) -> notes onsetting after start dropped",
     "denseStartPcBar=3 [hand-set, inline]",
     "tone collection", "F7", "D1 divergence: batch true / bridge false (intentional)"),
    ("phrase-boundary view (silence/marker detector)", "L1.5", "dormant", f"{PBV_H}:82-115", "src/composing/analysis/engravingbridge/phraseboundaryview.cpp:368-456",
     "per-voice surface strength wGap*gap+wInterOnset*ioi+wPitch*pitch; peak when > mean + k*SD; markers (fermata/barline/rest>=240 ticks) spike at 1.5x ceiling",
     "wGap=0.50 [hand-set]; wInterOnset=0.30 [hand-set]; wPitch=0.20 [hand-set]; k=1.0 [hand-set]; tauTicks=0 [hand-set]; coincidenceWeight=0.0 [hand-set]; minSilenceTicks=240 [hand-set]; spikeCeilingFactor=1.5 [hand-set]",
     "gated OFF (jointKeyWiring)", "F8",
     "the ONLY term surface for F8; fermatas enter only as generic markers"),
    ("spelling view (line-of-fifths facts)", "L1.5", "dormant", "src/composing/analysis/engravingbridge/spellingview.cpp:36-76", f"{CSD_C}:553",
     "structural fact extraction: lineOfFifths(tpc), sharp/flat sense, span centroid; no tunable constants",
     "structural",
     "dormant decoder spelling pin only", "F3", "no live L3 consumer — L3 emission is spelling-blind"),

    # ── L3 key/mode emission (LIVE) ──────────────────────────────────────────
    ("L3 note weighting", "L3", "live", f"{AT}:606-610; {KMA_C}:228-233", f"{KMA_C}:228-233",
     "multiplicative per note: min(duration x beat, cap) x bassMultiplier if bass",
     "noteWeightCap=3.0 [hand-set]; bassMultiplier=2.0 [hand-set]",
     "all L3 emission components", "F7", ""),
    ("scale-membership scoring (4-way)", "L3", "live", f"{AT}:619-622; {KMA_C}:238-261", f"{KMA_C}:255-258",
     "additive per note by (in candidate scale) x (in signature scale): 1.00 / 0.25 / -0.20 / -0.05",
     "scaleScoreInBoth=1.00 [hand-set]; scaleScoreInCandidateOnly=0.25 [hand-set]; scaleScoreInKeySigOnly=-0.20 [hand-set]; scaleScoreInNeither=-0.05 [hand-set]",
     "emission score", "F1", "the collection-membership emission (key axis)"),
    ("triad/tonal-centre evidence", "L3", "live", f"{AT}:630-639; {KMA_C}:265-313", f"{KMA_C}:297-310",
     "additive: tonic/third/fifth/leading-tone weighted presence + complete-triad bonus or missing-tonic penalty + capped extra-scale term",
     "tonicWeight=1.60 [hand-set]; thirdWeight=0.70 [hand-set]; fifthWeight=0.50 [hand-set]; leadingToneWeight=0.40 [hand-set]; completeTriadBonus=2.50 [hand-set]; missingTonicPenalty=-2.50 [hand-set]; extraScaleFactor=0.10 [hand-set]; extraScaleCap=5.0 [hand-set]",
     "emission score", "F1", ""),
    ("characteristic-pitch term", "L3", "live", f"{AT}:648-649; {KMA_C}:321-355", f"{KMA_C}:344-349",
     "additive boost/penalty on presence/absence of the mode's distinguishing pitch (half boost when only one of two present)",
     "characteristicPitchBoost=1.80 [hand-set]; characteristicPitchPenalty=-0.60 [hand-set]",
     "emission score", "F1", "mode-disambiguation term (K279 diagnosis implicated the presence threshold)"),
    ("true leading-tone boost", "L3", "live", f"{AT}:659; {KMA_C}:363-375", f"{KMA_C}:363-375",
     "additive when pc (tonic+11) present above 0.1",
     "trueLeadingToneBoost=1.20 [hand-set]",
     "emission score", "F4", "a leading-tone EVENT reduced to presence (not resolution)"),
    ("mode priors (21) + preset tables", "L3", "live", f"{AT}:671-695; {MPP}:27-170", f"{KMA_C}:378-407",
     "additive per-candidate prior by mode; 5 named presets x 21 modes + app-default table override the fields",
     "modePriorIonian=1.20 [preset-table]; modePriorAeolian=1.00 [preset-table]; modePriorAltered=-3.50 [preset-table]; (21 fields x 6 tables) [preset-table]",
     "emission score -> decode", "F2",
     "OI-174/OI-147: the mode-vocabulary question lives here (21 modes x 12 tonics = 252 states)"),
    ("key-signature proximity penalty", "L3", "live", f"{AT}:723; {KMA_C}:411-420", f"{KMA_C}:411-420",
     "subtractive linear: -penalty x circle-of-fifths distance from notated signature",
     "keySignatureDistancePenalty=0.60 [hand-set]",
     "emission score; ALSO the decoder's changePerFifthStep (shared symbol)", "F2", ""),
    ("tonal-centre comparison (family-winner)", "L3", "live", f"{AT}:709-714; {KMA_C}:429-441,670-688", f"{KMA_C}:670-688",
     "secondary weighted score deciding relative-pair family winner when delta > threshold",
     "tonalCenterTonicWeight=2.20 [hand-set]; tonalCenterThirdWeight=1.00 [hand-set]; tonalCenterFifthWeight=0.70 [hand-set]; tonalCenterLeadingTone=0.50 [hand-set]; tonalCenterTriadBonus=2.00 [hand-set]; tonalCenterDeltaThreshold=0.25 [hand-set]",
     "winner selection", "F1", "relative major/minor disambiguation — the measured weak axis"),
    ("pairwise relative-pair disambiguation", "L3", "live", f"{AT}:733-735; {KMA_C}:455-488", f"{KMA_C}:632",
     "post-hoc additive mutation on top-2 same-signature candidates (complete-triad vs no-tonic; only-tonic)",
     "disambiguationTriadBonus=4.50 [hand-set]; disambiguationTriadCost=1.50 [hand-set]; disambiguationTonicBonus=1.00 [hand-set]",
     "ranked candidates", "F1", ""),
    ("declared-mode penalty", "L3", "live", f"{AT}:752; {KMA_C}:598-603", f"{KMA_C}:598-603",
     "subtractive penalty on candidates whose mode class contradicts the file's declared mode (graded, was a 7.0 wall)",
     "declaredModePenalty=1.0 [hand-set]",
     "emission score", "F2", "the declared-mode prior channel (OI-78 siloing)"),
    ("partial-signature correction", "L3", "live", f"{KR}:107-190", f"{KR}:248",
     "hard one-step signature correction when a pervasive dominant accidental is present (>=3% of weight and >=2x its natural)",
     "kPervasiveFraction=0.03 [hand-set]; kDominanceRatio=2.0 [hand-set]",
     "corrected fifths anchor for resolver + decode", "F2", "Baroque partial/Dorian signatures"),
    ("dynamic lookahead (resolver)", "L3", "live", f"{AT}:789-791; {KR}:308-326", f"{KR}:318-325",
     "iterative window expansion until confidence >= threshold or cap (2-beat steps, 24-beat max)",
     "dynamicLookaheadConfidenceThreshold=0.60 [hand-set]; dynamicLookaheadStepBeats=2 [hand-set]; dynamicLookaheadMaxBeats=24 [hand-set]",
     "resolveKeyAndModeRanked", "NONE", "windowing policy, not a model factor"),
    ("mode-switching hysteresis (resolver)", "L3", "live", f"{AT}:801,807; {KR}:340-356", f"{KR}:340-356",
     "hard margin: a key/mode switch must beat the incumbent by the margin (relative pair has its own)",
     "hysteresisMargin=2.0 [hand-set]; relativeKeyHysteresisMargin=2.0 [hand-set]",
     "resolver ranked output; ALSO decoder change-cost defaults (shared symbols)", "NONE",
     "OI-97: the two margins are value-coupled by comment only; nearest factor: the (tonic,mode) transition term of the joint decode (not on the §2 roster)"),
    ("L3 sequence decoder (Viterbi)", "L3", "live", f"{KMS_H}:112-155; {KMS_C}:242-398", f"{RA}:636,707",
     "forward max-sum DP over per-slice top-K union of 252 (tonic,mode) candidates; transition cost = base + perFifth x cofDistance + relativePairExtra; backward pass for sequence margin",
     "topK=8 [hand-set]; changeBaseCost=2.0 [derived=hysteresisMargin]; changePerFifthStep=0.60 [derived=keySignatureDistancePenalty]; relativePairExtraCost=2.0 [derived=relativeKeyHysteresisMargin]; windowBeats=4.0 [hand-set]; beatsPerDecayUnit=4.0 [hand-set]; uncertainThreshold=1.0 [hand-set]; maxAlternatives=4 [hand-set]",
     "per-slice key/mode -> region keys -> L4 key context", "NONE",
     "the existing (tonic,mode) transition structure the joint model subsumes; not itself a §2 roster factor"),
    ("L3 confidence sigmoid", "L3", "live", f"{AT}:777-778; {KMA_C}:762-777", f"{KMS_C}:224-225",
     "sigmoid(top1-top2 gap) -> normalizedConfidence (midpoint 2.0, steepness 1.5)",
     "confidenceSigmoidMidpoint=2.0 [hand-set]; confidenceSigmoidSteepness=1.5 [hand-set]",
     "downstream 0.8 annotate gate; exposure buckets", "NONE", "reporting/abstention surface (OI-79 notes the duplicated sigmoid form)"),

    # ── L3 section pipeline (LIVE) ───────────────────────────────────────────
    ("annotate key-confidence gate", "L3-section", "live", f"{SA_H}:91", f"{SA_C}:760; {SCD}:56",
     "hard abstention bar: key-dependent annotations (key areas, cadence labels) need normalizedConfidence >= 0.8",
     "kAnnotateKeyConfidenceThreshold=0.8 [hand-set]",
     "user-visible annotations", "NONE", "G10 manifest row; abstention policy"),
    ("island key stabilization", "L3-section", "live", f"{SA_C}:90-163", f"{SA_C}:108-125",
     "structural smoothing: a 1-region key island is overwritten by the stable key unless the change persists into the next region",
     "structural",
     "displayed region keys", "NONE", "post-hoc smoothing duplicating what a decode transition should do; runs only when joint wiring OFF"),
    ("live cadence patterns (PAC/PC/DC/HC)", "L3-section", "live", f"{SCD}:101-137", "notationcomposingbridge.cpp:1244",
     "hard degree-pattern rules on adjacent regions (e.g. PAC: degree 4->0 non-minor, or 6-dim->0), same key, confidence-gated",
     "structural (kMaxPivotLookaheadRegions=8 [hand-set])",
     "cadence labels written to score", "F4",
     "key-DEPENDENT (degree-based) — the circular form OI-166's key-agnostic detector is meant to replace; annotation-only (no key feedback)"),
    ("sparse-gap chord inference (section)", "L3-section", "live", f"{SA_C}:295-407,502-517,706-710", f"{SA_C}:392",
     "interval-table inference for thin gaps (m3/M3/dim5/P5 -> quality priority Major/Minor=3, Dim=2, fifth=1); gaps <3 pcs carry neighbours; measure-opening carry within 1 beat",
     "structural (priority seeds 3/2/1; pc bars 3; 1-beat window)",
     "displayed gap regions", "F1", "display-path refinement (P2 annotation pipeline)"),

    # ── L3 dormant key machinery ─────────────────────────────────────────────
    ("joint key weights (J-key)", "L3-dormant", "dormant", f"{JKD_H}:141-150", "src/composing/analysis/section/jointkeydecision.cpp:235-349",
     "additive re-rank weights over the scoped key lattice + Viterbi transition penalty; config-B chord-coupling bonus with rank decay",
     "scalePrior=1.0 [hand-set]; localPrior=0.5 [hand-set]; cadenceAnchor=0.8 [hand-set]; modulation=1.0 [hand-set]; bassIsRootTonic=0.15 [hand-set]; declaredHint=1.0 [hand-set]; transitionPenalty=1.2 [hand-set]; couplingBonus=0.6 [hand-set]",
     "gated OFF (MUSE_JOINT_KEY_WIRING)", "NONE",
     "the shelved J-key-iii scoped-joint step; superseded in spirit by the ratified joint estimator"),
    ("cadence key-anchor vote", "L3-dormant", "dormant", f"{CKA}:115-118,151-154", f"{CKA}:151-167",
     "weighted vote per detected authentic cadence into (tonic,mode) buckets: base + structural(phrase boundary) + chromatic LT + recency; winner by weight share",
     "kWeightBase=1.0 [swept]; kWeightStructural=2.0 [swept]; kWeightChromatic=1.0 [swept]; kWeightFinality=1.0 [swept]",
     "dormant joint-key path / diagnostics", "F4",
     "leading-tone PRESENCE test (not resolution) — the false-positive-prone form functioncadence replaces"),
    ("local-modulation establishment", "L3-dormant", "dormant", f"{LMD}:47-48", f"{LMD}:89,190",
     "hard: a tonicization becomes a local-key span after >=5 consistent chords (<=2 out-of-collection pcs each) + >=1 confirming cadence",
     "kEstablishmentMinChords=5 [hand-set]; kPitchTolerance=2 [hand-set]",
     "dormant joint-key path", "NONE", "tonicization-vs-modulation duration prior in disguise"),

    # ── L4 dormant slice decoder ─────────────────────────────────────────────
    ("chord-slice decoder preferences", "L4-decoder", "dormant", f"{CSD_H}:158-318", f"{CSD_C} (decode/decideSlice/finalizeSlice)",
     "13 tunable settings: window half-widths (1/3), topK 6, uncertainty margin 0.5, pc floors (1/3), membership salience threshold 0.55 + reference duration 1.0 + penalty weight 0.6, stepwise gap tolerance 0, commit sufficiency 3, master switches, edge extension (OFF, 4 steps x 1 slice)",
     "contextSlices=1 [hand-set]; maxContextSlices=3 [hand-set]; topK=6 [hand-set]; uncertaintyMargin=0.5 [hand-set]; minDistinctPcs=1 [hand-set]; minHarmonyPcs=3 [hand-set]; membershipSalienceThreshold=0.55 [hand-set]; membershipReferenceDurationQn=1.0 [hand-set]; membershipPenaltyWeight=0.6 [hand-set]; stepwiseGapToleranceTicks=0 [hand-set]; sufficiencyChordTones=3 [hand-set]; maxEdgeExtendSteps=4 [hand-set]; edgeExtendIncrementSlices=1 [hand-set]",
     "diagnostic decode paths only (batch_analyze --decode-chords)", "F1",
     "OI-103: only sufficiencyChordTones is in the manifest; ranking score is the oracle's verticalScore (no second scorer)"),
    ("decoder membership/salience scoring", "L4-decoder", "dormant", f"{CSD_C}:236-241,342-376,839-851,883-917", f"{CSD_C}:1139-1143",
     "salience = metricWeight x min(1, durationQn/ref); tone-tier ladder (suspension/step/leap); implausibility penalty summed and subtracted x penaltyWeight; composite confidence = min(margin, sufficiency, cleanliness)",
     "kNoCompetitorConfidence=1000.0 [hand-set]",
     "decoder re-rank + uncertainty", "F1", "the NCT-classification machinery (Tier-1/2/3) lives here, dormant"),

    # ── L5 dormant function machinery ────────────────────────────────────────
    ("function-cadence vote weights", "L5", "dormant", f"{FC_H}:194-206", "src/composing/analysis/function/functioncadence.cpp:159-197",
     "additive tonic-vote per detected cadence: base + bass-5->1 + leading-tone-resolves + genuine-dominant-7th + metric + phrase-boundary(2.0) + final-bar; half/plagal/evaded discounted x0.5",
     "wBase=1.0 [hand-set]; wBassFiveToOne=1.0 [hand-set]; wLeadingTone=1.0 [hand-set]; wSeventh=1.0 [hand-set]; wMetric=1.0 [hand-set]; wPhraseBoundary=2.0 [hand-set]; wFinalBar=1.0 [hand-set]; discountHalf=0.5 [hand-set]; discountPlagal=0.5 [hand-set]; discountEvaded=0.5 [hand-set]",
     "no production consumer (OI-166: chord-derived, not the specified L1.5 pre-scan)", "F4",
     "key-agnostic but CHORD-derived tonic hypothesis (arr.rootPc)"),
    ("modulation decision params", "L5", "dormant", f"{FM_H}:109-118,128", "src/composing/analysis/function/functionmodulation.cpp:75-86",
     "modulation iff cadence-confirmed AND persistence evidence (wDuration x wholes + wCadentialWeight x votes + wSpelling) > baseChangeCost",
     "baseChangeCost=1.0 [hand-set]; wDuration=1.0 [hand-set]; wCadentialWeight=1.0 [hand-set]; wSpelling=0.5 [hand-set]; kTicksPerWholeNote=1920.0 [structural]",
     "no production consumer", "NONE", "tonicization-vs-modulation decision form"),
    ("progression licensing grammar", "L5", "dormant", "src/composing/analysis/function/functionprogression.cpp:44-142", "isLicensedProgression",
     "boolean root-motion grammar (desc 5th/3rd, asc 2nd/5th, desc 2nd, diatonic dim 5th, applied resolutions); NO numeric constants",
     "structural",
     "no production consumer", "F5", "the fullest existing progression-grammaticality term — dormant"),
    ("function resolver plausibility", "L5", "dormant", f"{FR_H}:210-216", "src/composing/analysis/function/functionresolver.cpp:90-107,277",
     "plausibility = wLicensedOut + wLicensedIn + wCadentialFit; deciding margin 0.5; per-kind confidence seeds 0.25/0.5/1.0; fine-grain forward override channel",
     "wLicensedOut=1.0 [hand-set]; wLicensedIn=1.0 [hand-set]; wCadentialFit=1.0 [hand-set]; decidingMargin=0.5 [hand-set]",
     "no production consumer", "F5", ""),
    ("forward-override bar", "L5", "dormant", f"{FO_H}:80-83", "src/composing/analysis/function/forwardoverride.cpp:26-45",
     "override iff contradictionStrength > baseBar + confidenceScale x clamp01(earlierConfidence); once per pass",
     "baseBar=1.0 [hand-set]; confidenceScale=1.0 [hand-set]",
     "no production consumer", "NONE", "the ratified forward-override pattern's constants"),
    ("function output confidence", "L5", "dormant", f"{FOUT_H}:102-109", "functionoutput.cpp",
     "additive confidence combination + boundary squash x/(x+k)",
     "wCadenceVote=1.0 [hand-set]; wLicensedFit=1.0 [hand-set]; wNextBestMargin=1.0 [hand-set]; kBoundary=1.0 [hand-set]",
     "no production consumer", "NONE", "representational"),
    ("progression recognizer priors", "L5", "dormant", f"{PR_H}:109-133", "src/composing/analysis/progression/progressionrecognizer.cpp:95-116,250",
     "idiom prior = matchScore x max seed/histogram blend (alpha=evidence/(evidence+blendRate)); cue discounts x0.5",
     "blendRate=1.0 [hand-set]; admissionThreshold=0.0 [hand-set]; modeCueFactor=0.5 [hand-set]; chordsOnlyFactor=0.5 [hand-set]",
     "no production consumer", "F5", ""),
    ("VL-C texture classifier", "L5", "dormant", f"{TC_H}:132-137", "src/composing/analysis/voiceleading/textureclassifier.cpp:85-133",
     "z-scored nearest-centroid over 20 features; fit=exp(-distance/scale); abstain floors (fit/margin/samples)",
     "fitScale=2.6734128 [study-fitted]; fitFloor=0.129574792 [study-fitted]; marginFloor=0.00718666965 [study-fitted]; evidentialFloor=8 [hand-set]",
     "no production consumer", "NONE", "generated reference tables (textureclassifierreference.h)"),

    # ── notation-bridge consumption surface (LIVE product path) ──────────────
    ("key exposure buckets (implode bridge)", "bridge", "live", f"{NIB}:79-96", f"{NIB}:84-95",
     "hard confidence buckets deciding key exposure in imploded output: <0.5 none / <0.8 tentative / else assertive",
     "kTentativeKeyExposureThreshold=0.5 [hand-set]; kAssertiveKeyExposureThreshold=0.8 [hand-set]",
     "imploded chord-staff output", "NONE",
     "consumption-side decision constants on NO audited surface and in no manifest (new register row)"),
    ("preset carriers (batch_analyze)", "bridge", "live", f"{BA}:4206-4261", f"{BA}:4267-4281",
     "per-preset overrides: Jazz extensionThreshold 0.12 + reduced inversion bonuses + kWStepIn 0.10; Baroque/Standard preferMinorOverMajorAdd6 true; Default = product config",
     "presetKWStepIn=0.125/0.10 [fit-adopted/hand-set per carrier]",
     "measurement carriers (Baroque/Jazz/Default)", "NONE", "carrier definitions, not model terms"),
]

# ─────────────────────────────────────────────────────────────────────────────
# DT-26 tree-wide scope check: identifying patterns + per-file dispositions.
# The sweep FAILS if a hit file has no disposition row here.
# ─────────────────────────────────────────────────────────────────────────────
SWEEP_PATTERNS = {
    "named-term-constant": r"k[A-Z][a-zA-Z]*(Bonus|Penalty|Margin|Threshold|Weight|Prior|Cost|Factor|Ratio|Budget)\s*=\s*[-0-9]",
    "term-shaped-variable": r"(double|float|int)\s+[a-zA-Z_]*([Bb]onus|[Pp]enalty|[Ww]eight|[Tt]hreshold|[Mm]argin|[Pp]rior|[Cc]ost)[a-zA-Z_]*\s*=\s*[-0-9.]",
    "tonic-construction": r"ionianTonicPcFromFifths|keyModeTonicOffset",
}
# disposition: IN-SCOPE (enumerated above) | TEST | UPSTREAM-NON-ANALYSIS | CONSUMER |
#              DIAGNOSTIC-CARRIER — with a one-line reason.
SWEEP_DISPOSITIONS = {
    # in-scope files (enumerated in TERMS)
    "src/composing/analysis/chord/chordanalyzer.cpp": "IN-SCOPE",
    "src/composing/analysis/chord/chordanalyzer.h": "IN-SCOPE (kTemplateCount/kTemplateIntervals/derived masks)",
    "src/composing/analysis/chord/postscoringgates.cpp": "IN-SCOPE",
    "src/composing/analysis/chord/chordslicedecoder.cpp": "IN-SCOPE (dormant decoder)",
    "src/composing/analysis/chord/chordslicedecoder.h": "IN-SCOPE (dormant decoder)",
    "src/composing/analysis/chord/analysisutils.h": "IN-SCOPE (shared primitives: pcInMask/diatonicMaskFromFifths/ionianTonicPcFromFifths)",
    "src/composing/analysis/decode/chordpathdecoder.h": "IN-SCOPE (computes no score — verified)",
    "src/composing/analysis/engravingbridge/phraseboundaryview.h": "IN-SCOPE (dormant F8 surface)",
    "src/composing/analysis/engravingbridge/regiontonecollector.cpp": "IN-SCOPE",
    "src/composing/analysis/engravingbridge/regiontonecollector.h": "IN-SCOPE",
    "src/composing/analysis/function/functioncadence.h": "IN-SCOPE (dormant L5)",
    "src/composing/analysis/function/functionmodulation.cpp": "IN-SCOPE (dormant L5)",
    "src/composing/analysis/function/functionmodulation.h": "IN-SCOPE (dormant L5)",
    "src/composing/analysis/function/functionoutput.h": "IN-SCOPE (dormant L5)",
    "src/composing/analysis/function/functionprogression.h": "IN-SCOPE (dormant L5)",
    "src/composing/analysis/function/functionresolver.h": "IN-SCOPE (dormant L5)",
    "src/composing/analysis/function/harmonicfunctionlayer.cpp": "IN-SCOPE",
    "src/composing/analysis/function/harmonicfunctionlayer.h": "IN-SCOPE",
    "src/composing/analysis/grouping/groupinglayer.h": "IN-SCOPE (dormant; alignmentWindowTicks=480, codetta knobs inert 0/0.0)",
    "src/composing/analysis/harmony/harmonicsegmenter.cpp": "IN-SCOPE",
    "src/composing/analysis/harmony/harmonicsegmenter.h": "IN-SCOPE",
    "src/composing/analysis/key/keymodeanalyzer.cpp": "IN-SCOPE",
    "src/composing/analysis/key/keymodeanalyzer.h": "IN-SCOPE",
    "src/composing/analysis/key/keymodesequence.h": "IN-SCOPE",
    "src/composing/analysis/key/keyresolver.cpp": "IN-SCOPE",
    "src/composing/analysis/progression/progressionrecognizer.cpp": "IN-SCOPE (dormant)",
    "src/composing/analysis/progression/progressionrecognizer.h": "IN-SCOPE (dormant)",
    "src/composing/analysis/region/harmonicrhythm.h": "IN-SCOPE (regionMetricWeight carrier field default 1.0; no scoring term)",
    "src/composing/analysis/region/regionanalyzer.cpp": "IN-SCOPE",
    "src/composing/analysis/region/sparsechordrefinement.cpp": "IN-SCOPE",
    "src/composing/analysis/section/cadencekeyanchor.cpp": "IN-SCOPE (dormant)",
    "src/composing/analysis/section/jointkeydecision.h": "IN-SCOPE (dormant)",
    "src/composing/analysis/section/localmodulationdetector.cpp": "IN-SCOPE (dormant)",
    "src/composing/analysis/section/sectionanalyzer.cpp": "IN-SCOPE",
    "src/composing/analysis/section/sectionanalyzer.h": "IN-SCOPE",
    "src/composing/analysis/section/sectioncadencedetection.cpp": "IN-SCOPE",
    "src/composing/analysis/types/analysistypes.h": "IN-SCOPE",
    "src/composing/analysis/voiceleading/textureclassifier.h": "IN-SCOPE (dormant VL-C)",
    "src/composing/analysis/voiceleading/textureclassifierreference.h": "IN-SCOPE (generated study-fitted reference)",
    "src/composing/analyzed_section.h": "IN-SCOPE (POD carrier defaults, no scoring term — verified: confidence/weight struct fields)",
    # out-of-scope, dispositioned
    "src/engraving/compat/pageformat.cpp": "UPSTREAM-NON-ANALYSIS (page layout)",
    "src/engraving/dom/box.h": "UPSTREAM-NON-ANALYSIS (layout)",
    "src/engraving/dom/pitchspelling.cpp": "UPSTREAM-NON-ANALYSIS (note-input/MIDI spelling algorithm; our analysis reads authored TPC — spelling is INPUT; flagged as input-provenance context only)",
    "src/engraving/dom/system.h": "UPSTREAM-NON-ANALYSIS (layout)",
    "src/engraving/playback/playbackcontext.h": "UPSTREAM-NON-ANALYSIS (playback)",
    "src/engraving/rendering/iscorerenderer.h": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/accidentalslayout.cpp": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/accidentalslayout.h": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/chordlayout.cpp": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/chordlayout.h": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/guitarbendlayout.cpp": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/slurtielayout.cpp": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/tappinglayout.cpp": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/textlayout.cpp": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/score/tlayout.cpp": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rendering/single/singlelayout.cpp": "UPSTREAM-NON-ANALYSIS (rendering)",
    "src/engraving/rw/read114/read114.cpp": "UPSTREAM-NON-ANALYSIS (legacy file read)",
    "src/importexport/midi/internal/midiimport/importmidi_clef.cpp": "UPSTREAM-NON-ANALYSIS (MIDI import)",
    "src/importexport/midi/internal/midiimport/importmidi_lrhand.cpp": "UPSTREAM-NON-ANALYSIS (MIDI import)",
    "src/importexport/midi/internal/midiimport/importmidi_quant.cpp": "UPSTREAM-NON-ANALYSIS (MIDI import)",
    "src/importexport/musicxml/internal/import/importmusicxmlpass1.cpp": "UPSTREAM-NON-ANALYSIS (import; the declared-mode dedup patch lives in pass2 — INPUT-producing, tracked in CLAUDE.md)",
    "src/importexport/musicxml/internal/import/importmusicxmlpass1.h": "UPSTREAM-NON-ANALYSIS (import)",
    "src/importexport/videoexport/internal/videowriter.cpp": "UPSTREAM-NON-ANALYSIS (video export)",
    "src/notation/internal/notationcomposingbridgehelpers.h": "CONSUMER (bridge segmentation helper defaults; detectOnsetSubBoundaries threshold default 0.25 — same value routed as opts.onsetBoundaryThreshold on live callers; enumerated under Pass-2 row)",
    "src/notation/internal/notationimplodebridge.cpp": "CONSUMER (ENUMERATED: key exposure buckets 0.5/0.8 — new register row; also kSameChordReannotationGap, OI-60c)",
    "src/notation/internal/notationnoteinput.cpp": "UPSTREAM-NON-ANALYSIS (note input UI margins)",
    "src/notation/internal/notationcomposingbridge.cpp": "CONSUMER (tonic used for display degree/labels — OI-173 D2/D3 definition sites; no scoring term)",
    "src/notation/internal/notationtuningbridge.cpp": "CONSUMER (intonation feature reads key/tonic; no inference term)",
    "src/notationscene/qml/MuseScore/NotationScene/continuouspanel.cpp": "UPSTREAM-NON-ANALYSIS (UI)",
    "src/notationscene/utilities/engravingitempreviewpainter.cpp": "UPSTREAM-NON-ANALYSIS (UI)",
    "tools/batch_analyze.cpp": "DIAGNOSTIC-CARRIER (preset carriers + decode-only sweep overrides; enumerated under preset-carriers row)",
}

# ─────────────────────────────────────────────────────────────────────────────
def repo_files(patterns):
    """Run the sweep patterns over src/**/*.{cpp,h} + tools/*.cpp, return {file: [pattern,...]}."""
    hits = {}
    files = glob.glob(os.path.join(ROOT, "src", "**", "*.cpp"), recursive=True)
    files += glob.glob(os.path.join(ROOT, "src", "**", "*.h"), recursive=True)
    files += glob.glob(os.path.join(ROOT, "tools", "*.cpp"))
    compiled = {k: re.compile(v) for k, v in patterns.items()}
    for f in files:
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        if "/tests/" in rel or rel.startswith("src/framework"):
            continue
        try:
            text = open(f, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        matched = [name for name, rx in compiled.items() if rx.search(text)]
        if matched:
            hits[rel] = matched
    return hits


def main():
    manifest = json.load(open(os.path.join(ROOT, "tools", "param_manifest.json"), encoding="utf-8"))
    manifest_names = {p["name"] for p in manifest["parameters"]}
    manifest_by_group = {}
    for p in manifest["parameters"]:
        g = p["group"].split(" ")[0].rstrip("—").strip()
        manifest_by_group.setdefault(g, []).append(p)

    # 1) term rows -> CSV with manifest coverage
    const_rx = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)=")
    rows = []
    for t in TERMS:
        (name, layer, live, decl, apply_, form, consts, consumers, factor, notes) = t
        cnames = const_rx.findall(consts)
        in_manifest = sorted(set(c for c in cnames if c in manifest_names))
        not_in_manifest = sorted(set(c for c in cnames if c not in manifest_names
                                     and consts != "structural" and "[structural]" not in consts))
        rows.append({
            "name": name, "layer": layer, "liveness": live,
            "decl_site": decl, "apply_site": apply_, "form": form,
            "constants": consts, "consumers": consumers,
            "roster_factor": factor, "roster_factor_text": ROSTER[factor],
            "constants_in_param_manifest": ";".join(in_manifest),
            "constants_not_in_param_manifest": ";".join(not_in_manifest),
            "hand_verified": "yes", "notes": notes,
        })

    csv_path = os.path.join(HERE, "term_inventory.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # 2) sweep + disposition check
    hits = repo_files(SWEEP_PATTERNS)
    undispositioned = sorted(h for h in hits if h not in SWEEP_DISPOSITIONS)
    sweep = {
        "patterns": SWEEP_PATTERNS,
        "hit_files": {h: {"patterns": hits[h],
                          "disposition": SWEEP_DISPOSITIONS.get(h, "UNDISPOSITIONED")}
                      for h in sorted(hits)},
        "undispositioned": undispositioned,
    }

    # 3) template staleness check
    src = open(os.path.join(ROOT, "src/composing/analysis/chord/chordanalyzer.h"),
               encoding="utf-8", errors="replace").read()
    m = re.search(r"kTemplateCount\s*=\s*(\d+)", src)
    k_template_count = int(m.group(1)) if m else None
    doc = open(os.path.join(ROOT, "docs", "scoring_model.md"), encoding="utf-8", errors="replace").read()
    doc_rows = len(re.findall(r"^\| \d+\s*\|", doc, re.M))
    m2 = re.search(r"currently (\d+)\) chord templates", doc)
    doc_count_claim = int(m2.group(1)) if m2 else None

    # 4) scoring_model.md mention check for every registered L4 constant
    reg_rx = re.compile(r'registerDouble\("([A-Za-z0-9_]+)"')
    reg_names = []
    for rel in ["src/composing/analysis/chord/chordanalyzer.cpp",
                "src/composing/analysis/chord/postscoringgates.cpp",
                "src/composing/analysis/section/sectionanalyzer.cpp"]:
        reg_names += reg_rx.findall(open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace").read())
    doc_mentions = {n: (n in doc) for n in sorted(set(reg_names))}
    undocumented = sorted(n for n, ok in doc_mentions.items() if not ok)

    # 5) OI-23 measured figures (from the manifest, mechanically)
    chord_groups = {"G1", "G2", "G3", "G4", "G5", "G6", "G7"}
    live_chord = [p for g, ps in manifest_by_group.items() if g in chord_groups
                  for p in ps if p.get("consuming_path") in ("production", "both")]
    live_all = [p for p in manifest["parameters"] if p.get("consuming_path") in ("production", "both")]
    live_by_group = {g: len([p for p in ps if p.get("consuming_path") in ("production", "both")])
                     for g, ps in sorted(manifest_by_group.items())}
    oi23 = {
        "definition": "param_manifest rows in chord-surface groups G1-G7 with consuming_path production|both",
        "measured_live_chord_surface_constants": len(live_chord),
        "live_rows_by_group": live_by_group,
        "of_which_fit_adopted": ["kWStepIn"],
        "manifest_total_rows": manifest["counts"]["total_rows"],
        "manifest_live_rows_all_groups": len(live_all),
        "note": "OI-23 claims '~30 live hand-set constants'; the manifest's chord-surface live rows are the closest mechanical measurement of that population (G1 oracle + G7 gate margins alone = the ~30-sized core). Constants NOT in the manifest at all (see per-row column) are additional to this figure.",
    }

    # 6) OI-179 census (computed live)
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import dcml_parser as dp
    stems = sorted(os.path.splitext(os.path.basename(p))[0]
                   for p in glob.glob(os.path.join(ROOT, "tools", "corpus", "*.xml")))
    idx = dp._build_wir_index(os.path.join(ROOT, "tools", "dcml", "when_in_rome"))
    covered = [s for s in stems if s in idx]
    bcmh = [s for s in covered
            if os.path.exists(os.path.join(os.path.dirname(idx[s]), "analysis_BCMH.txt"))]
    ch_dir = os.path.join(ROOT, "tools", "dcml", "when_in_rome", "Corpus",
                          "Early_Choral", "Bach,_Johann_Sebastian", "Chorales")
    folders = [d for d in sorted(os.listdir(ch_dir)) if os.path.isdir(os.path.join(ch_dir, d))]
    folders_with_bcmh = [d for d in folders
                         if os.path.exists(os.path.join(ch_dir, d, "analysis_BCMH.txt"))]
    # DCML bach_chorales harmony-label check
    import csv as _csv
    with open(os.path.join(ROOT, "tools", "dcml", "bach_chorales", "metadata.tsv"),
              encoding="utf-8") as f:
        meta = list(_csv.DictReader(f, delimiter="\t"))
    dcml_label_pieces = [r["piece"] for r in meta if r.get("label_count") and int(r["label_count"]) > 0]
    oi179 = {
        "corpus_stems": len(stems),
        "wir_covered_stems": len(covered),
        "covered_stems_with_second_analysis_BCMH": len(bcmh),
        "second_analysis_file": "analysis_BCMH.txt (header: 'Analyst: The Bach Chorales Melody-Harmony Corpus. See https://github.com/PeARL-laboratory/BCMH; Proofreader: Automated translation by Nestor Napoles Lopez')",
        "location": "tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/<NNN>/",
        "wir_chorale_folders_total": len(folders),
        "wir_chorale_folders_with_BCMH": len(folders_with_bcmh),
        "dcml_bach_chorales_repo_pieces": len(meta),
        "dcml_bach_chorales_pieces_with_harmony_labels": len(dcml_label_pieces),
        "stems_with_second_analysis": bcmh,
        "note": "counts only; no agreement grading built. Independence of the BCMH annotations from the WiR analyst annotations is a literature question (Cowork's half of OI-179).",
    }

    # 7) summary
    from collections import Counter
    prov_counter = Counter()
    for r in rows:
        for p in re.findall(r"\[([a-z-]+)", r["constants"]):
            prov_counter[p] += 1
    summary = {
        "generated_by": "tools/term_inventory/gen_term_inventory.py",
        "dispatch": "cc_instruction_term_inventory.md (2026-07-18)",
        "term_rows": len(rows),
        "rows_by_layer": dict(Counter(r["layer"] for r in rows)),
        "rows_by_liveness": dict(Counter(r["liveness"] for r in rows)),
        "rows_by_roster_factor": dict(Counter(r["roster_factor"] for r in rows)),
        "rows_with_no_roster_factor": [r["name"] for r in rows if r["roster_factor"] == "NONE"],
        "roster_factors_with_no_live_term": sorted(
            set(ROSTER) - {"NONE"}
            - set(r["roster_factor"] for r in rows if r["liveness"] == "live")),
        "constant_provenance_mentions": dict(prov_counter),
        "template_staleness_check": {
            "kTemplateCount_source": k_template_count,
            "scoring_model_doc_claim": doc_count_claim,
            "scoring_model_table_rows": doc_rows,
            "pass": k_template_count == doc_count_claim == doc_rows,
        },
        "registered_constants_doc_mention_check": {
            "registered_total": len(doc_mentions),
            "not_mentioned_in_scoring_model_md": undocumented,
        },
        "oi23_measured": oi23,
        "oi179_census": oi179,
        "dt26_sweep": sweep,
    }
    with open(os.path.join(HERE, "term_inventory_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1)

    print(f"rows: {len(rows)}  csv: {csv_path}")
    print(f"template check pass: {summary['template_staleness_check']['pass']}")
    print(f"registered constants w/o doc mention: {undocumented}")
    print(f"OI-23 measured (chord-surface live manifest rows): {oi23['measured_live_chord_surface_constants']}")
    print(f"OI-179: {oi179['covered_stems_with_second_analysis_BCMH']}/{oi179['wir_covered_stems']} covered stems have analysis_BCMH.txt")
    print(f"DT-26 undispositioned hit files: {undispositioned}")
    if undispositioned:
        sys.exit(1)


if __name__ == "__main__":
    main()

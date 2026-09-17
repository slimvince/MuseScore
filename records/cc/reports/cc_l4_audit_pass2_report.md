# CC REPORT — Layer-4 (chord) Certification Audit, PASS 2 (blind second reading + error rate + full catalog sweep) — EG-7 / OI-84 / OI-102

> **CC, 2026-07-12.** The second and final pass of the layer-4 certification audit
> (`cowork_audit_protocol.md` steps P5 / P6 / P8-second-run). Read-only fact-finding: no
> production behavior changed, no constant tuned, no golden refresh; `tools/robust_stop/`
> and `tools/corpus/` untouched. Every judgment was frozen and committed BEFORE any
> withheld file was opened (the DT-20 / OI-89 lesson). The certification decision is the
> user's; this report only PROPOSES.

## 0. What this pass did, and the blinding boundary

I am the independent second reader for layer 4. The first pass dispositioned all ~1,869
deep rows across three sessions (decoder / oracle / satellites). My job was to find what
the first pass got wrong or missed — to succeed by disagreeing.

**The freeze commit `d716ac1ca8` is the blinding boundary.** Everything in Task 1 (the
sampler, the 121-row blind reading, the 40-row blind error-rate judgments) was authored,
reviewed, and committed at `d716ac1ca8` while every withheld file was still unopened.

**When each withheld file was first opened — all strictly AFTER `d716ac1ca8`:**

| file | first opened |
|---|---|
| `DEFECT_TYPES.md` | Task 2, after the freeze |
| `OPEN_ITEMS.md` (full — the deferred mandatory session-start read) | Task 2, after the freeze |
| `STATUS.md` (head only) | Task 2, after the freeze |
| `tools/audit/l4/pass1_dispositions_{decoder,oracle,satellites}.csv` | Task 2, after the freeze |
| `cowork_handoff.md` | Task 6, after the freeze |

The pass-1 report `.md` files (`cc_l4_audit_pass1_*_report.md`) were **not** opened
separately — their conclusions reached me through the `OPEN_ITEMS.md` rows (OI-101…OI-114)
and the `STATUS.md` entries, which quote them in full. Safe reads used before the freeze:
`CLAUDE.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`, the
roadmap, `docs/scoring_model.md`, the RAW `tools/audit/l4/*.csv` inventory tables +
`manifest.json` + `file_table.csv`, the sampling-script code, `cc_instruction_l4_audit_pass1.md`,
and the source itself. **Note on partial file-level non-blindness (declared):**
`file_table.csv` is a designated-safe read, and its `reason` column carries file-level
population tags and a few file-level pass-1 findings (e.g. the `chordanalyzer.cpp`
MIS-TAG→scorer correction, the sparse-refinement L4/L5 boundary note). So the file-level
population disposition was not fully blind; the **row-level** verdicts (in the withheld
`pass1_dispositions_*` files) were fully blind.

## 1. Sample designs and seeds (Task 1)

The committed sampler `tools/audit/gen_pass2_sample_l4.py` (a sibling of the L1/L2
`gen_pass2_sample.py`; the L1/L2 script's seeds/domain are frozen provenance and must not
be edited) draws two samples from the RAW l4_*.csv deep inventory only — the `pass1_*`
artifacts are never read, so no pass-1 verdict can leak. New recorded seeds, distinct from
every seed used so far (L1/L2 `20260711`/`424242`; the `20260712`–`20260715` band reserved
by L3 / L4-pass-1):

- **Reading sample — seed `20260801`, 121 rows.** Stratified over the five row kinds in
  proportion to their counts (8 function / 61 literal / 15 field / 35 branch / 1+1
  crosslayer), with a coverage top-up so all 10 deep-audited files appear. Scope spread:
  decoder 20 / oracle 44 / satellites 57.
- **Error-rate sample — seed `20260802`, 40 rows, uniform** over the six deep-inventory
  kinds (adds `decl`). Kinds drawn: 16 literal / 12 branch / 6 function / 5 field / 1
  crosslayer / 0 decl. Scope: decoder 8 / oracle 13 / satellites 19.

Every sampled row was judged from the code, from scratch, at **full P2 verdict resolution**
(premises FACT/THEORY/ASSUMPTION; derived facts PUBLISHED/SILOED/TRAPPED/DUPLICATED;
constants ESTABLISHED/UNFIT/DEAD with the manifest-presence check; code SURVIVES/RETIRES;
plus the scope re-affirmation OUT-OF-L4-SCOPE for a row owned by an L3/L5 type) — the
OI-100 lesson (no coarse vocabulary). The blind dispositions are recorded by
`tools/audit/pass2_judge_l4.py` into `pass2_blind_reading.{csv,json}` and
`pass2_blind_errorrate.{csv,json}` (freeze `d716ac1ca8`).

**A line-drift reconciliation the reading had to handle.** The inventory was generated at
`7f57aad4b5`; `chordanalyzer.cpp` then gained the +127-line OI-110 fire-count block, so its
inventory line numbers run ~+120 ahead of HEAD. Every `chordanalyzer.cpp` row was located
by its **context string**, not its raw line (the other nine files did not drift). The
instrument is default-OFF and does not change scoring, so judging at HEAD is equivalent.

## 2. Comparison with pass 1 (Task 2) — `tools/audit/pass2_compare_l4.py`

The comparison joins each blind row to pass 1's disposition on the SAME inventory row
(the oracle's `loc` ranges parsed to their start line so a start-line key joins).

| sample | rows | CONCORDANT | CONCORDANT-CLEAN | CONCORDANT-EXCLUDED | DISAGREE |
|---|---|---|---|---|---|
| reading | 121 | 91 | 12 | 16 | **2** |
| error-rate | 40 | 30 | 5 | 5 | **0** |

- **CONCORDANT** — same verdict family.
- **CONCORDANT-CLEAN** — both "clean/tracked" but on a different verdict axis (pass 1 recorded
  a function's premise nature FACT/THEORY where I recorded code SURVIVES; or PUBLISHED-field
  vs SURVIVES). Not a disagreement — a function has both a premise and a code disposition.
- **CONCORDANT-EXCLUDED** — an `analysistypes.h` row owned by `KeyModeAnalyzerPreferences`
  (L3): I verdicted OUT-OF-L4-SCOPE; pass 1 excluded it from the L4 dispositions (satellites
  session, "L3 types excluded, lines <546"). Both agree it is out of L4 scope.

### 2.1 The two reading-sample disagreements — diagnosed, both verdict-axis

Both are `chordanalyzer.cpp` L143/L144: `kComplexityEvidenceFloor` and
`kAugThinEvidenceFactor`. **MINE = UNFIT** (hand-set `[empirical]`, registered for the
Stage-5 override loader but absent from `param_manifest.json`). **PASS 1 = ESTABLISHED**,
with the manifest gap recorded separately as a FLAG → **OI-106(a)**.

**Diagnosis: verdict-axis difference, NOT a substantive miss.** Both readers identified the
identical fact — these constants are absent from the manifest (pass 1 as OI-106(a); me as
the UNFIT verdict). The difference is only which P2 label to attach to a hand-set-but-role-
documented registered constant: pass 1's oracle constant-classifier defaulted it to
ESTABLISHED and carried the manifest gap as a flag; I folded the gap into an UNFIT verdict.
This is the SAME ESTABLISHED-vs-UNFIT boundary the L3 pass-2 re-derivation already
characterized (OI-100) — there the coarse reading over-used ESTABLISHED and pass 1's
conservative UNFIT was the one to rely on; here the roles are reversed but the boundary is
identical. **No protocol step let a miss through** (both readers converged on the finding),
and **no class is re-opened** (the class — hand-set constants absent from the manifest — was
already found and tracked by BOTH readers, OI-106/OI-103/OI-91).

**A self-caught error in my blind supporting-prose (declared, does not change the verdict).**
My frozen reason-text for L144 states "4 registered constants unmanifested … incl.
kExtensionThreshold". On unblinding + re-verification the true count is **3**
(`kWCompletePresenceThreshold`, `kComplexityEvidenceFloor`, `kAugThinEvidenceFactor`);
`kExtensionThreshold` IS in the manifest, under an annotated name `"kExtensionThreshold
(file constexpr; distinct from prefs.extensionThreshold)"`. My sampler's
`in_param_manifest_hint` used an exact/substring name match that the manifest's parenthetical
annotations defeated (a false negative in MY tooling, not in the audited code). The
core verdicts (both sampled constants ARE absent → UNFIT) are correct and match OI-106(a);
only the "4 / incl. kExtensionThreshold" detail in the reason string is wrong. Recorded here
transparently; the frozen artifact is left as frozen.

### 2.2 The reverse direction — rows pass 1 flagged that my per-row flag did not carry

Two reading-sample rows where pass 1 attached a flag and my flag column was empty
(SURVIVES-clean). Both diagnosed as **row-attribution differences, not missed defects**:

- `chordanalyzer.cpp` L268 `detectExtensions` (function): pass 1 cross-flagged the function
  to OI-106(b) (the inline unregistered thresholds 0.3/0.2/0.1 live in **literal** rows I
  did not sample). My function verdict SURVIVES is correct; the flagged content is in
  unsampled literal rows, so my sample simply did not draw them — the Task-3 whole-layer
  sweep is where the inline-threshold check belongs (it did not surface a NEW one).
- `sparsechordrefinement.h` L35 (crosslayer `#include chordanalyzer.h`): pass 1 put the
  L4/L5 boundary note (OI-102(i)) on this include row. The include itself is a correct L4-type
  dependency (SURVIVES); the boundary concern is the `.cpp`'s post-commit quality-overwrite
  behavior, which I was aware of and referenced from the file-table. Row-attribution, not a
  miss.

### 2.3 The measured error rate

**On the 40 blind-judged error-rate rows: 0 substantive disagreements → measured audit error
rate = 0/40 = 0.0 %.** No failing rows. No failure implies a whole class was judged wrongly
(the two reading-sample verdict-axis diffs are on a class both readers found and tracked).
This reproduces the L3 pass-2 outcome (0/40 substantive) and, like it, is strongest on the
scope/tag-heavy rows and cross-checked hardest on the ~judgment rows.

## 3. Whole-layer catalog sweep (Task 3) — all 21 DEFECT_TYPES over the full L4 inventory

The one instrument `tools/audit/gen_signature_sweep.py` was extended with a `--layer l4`
entry (LAYERS dict + a `registered_config` DT-2 mode that reads the `registerDouble`-
registered constant NAMES from source and the `*Preferences/*Preset/*Weights` config-struct
members, checking each against `param_manifest.json` — mechanical, no hardcoded answer). The
edit is **byte-identically inert for L3** (re-ran `--layer l3`: `sweep_results.json`
unchanged) and reproduces the L1/L2 counts. Hit tables: `tools/audit/l4/sweep_results.{json,txt}`.

### 3.1 Mechanical rules (6 + the local-dead-field rule), over all 3 scopes / 10 files

| DT | hits | disposition |
|---|---|---|
| **DT-2** unestablished/not-in-manifest constant | 89 | 3 registered oracle constants (→ **OI-106(a)**) + 17 `ChordSliceDecoderPreferences` (→ **OI-103**) + 64 `KeyModeAnalyzerPreferences` (L3, in the MIXED file → **OI-91**) + 5 non-scoring `ChordAnalyzerPreferences` toggles/enums (`scoringPhase`, `decodeQualityLevel`, `useExisting/Roman/Nashville…` booleans — correctly excluded from the fitter; confirms OI-102's "no new gap"). **No new gap.** |
| **DT-3** value-copied constant | 6 | 1 real = `relativeKeyHysteresisMargin == hysteresisMargin` (L3, MIXED file → **OI-97**); 5 regex false positives (comment words "sites"/"better"/"gateCtx"/"SliceChord"/"downbeat"). **No new.** |
| **DT-5** siloed/trapped fact (0–1 consumers) | 5 | `decodeSelection`/`classifyMembership`/`computeConfidence`/`nameOpenQuestion` (dormant decoder, 0 production consumers) + `recordNode` (ChordPathNode, 1 consumer) — reproduce the dormant-decoder declared-dormancy (**OI-102(ii)/OI-104**). **No new.** |
| **DT-12** stale anchor/dangling ref | 1 | **FALSE POSITIVE** — `chordanalyzer.h`:580 → `harmonicfunctionlayer.cpp:524`; verified at code, line 524 IS the `if (rc.score < threshold) break;` results-admission test the comment cites. The content-heuristic mis-picked the hint word "ranked". **Not a finding.** |
| **DT-16** raw-DOM outside L1 | 0 | Clean — the decoder reads the L1 `NoteModel::overlapping`, never the raw engraving DOM. |
| **DT-19** layer-boundary (upward include) | 2 | `chordanalyzer.cpp:25` + `chordslicedecoder.cpp:30` `#include function/harmonicfunctionlayer.h` (L4→L5). The known chord→competition coupling that **retires at R1 / renames at R7** (OI-19); pass 1 dispositioned both includes SURVIVES. **Tracked, dissolves at retirement.** |
| **DT-5 (local dead field)** | 1 | **NEW → OI-115.** See §3.3. |

### 3.2 Review rules (row-by-row against the 2,121-row inventory) — no new correctness defect, no new TYPE

- **DT-1** (unverified causal premise / Class A): none new — the oracle premises are FACT/THEORY
  (music theory), pass 1's 9 THEORY + 5 FACT; the one inference-affecting question is
  DECLARED, not carried (OI-109, P5-over-diminished).
- **DT-4** (silent overwrite of committed field): the sparse-refinement post-commit
  `identity.quality` overwrite — tracked (OI-102(i)/OI-10/OI-29).
- **DT-6** (duplicated derivation): the formatter's scale-interval / parent-map tables — tracked
  (**OI-111**); my reading extends it (the `DIATONIC_PARENT_INDEX` in `chordanalyzer.cpp:1460`
  is a THIRD copy of the 21→parent map that OI-111 lists inside the formatter only — see §5).
- **DT-7** (never/always fires): SymmetricRotation 0-fire (OI-104), aug-root correction 0-fire
  (OI-108(a)) — tracked; the sweep is not fire-rate-based, no new.
- **DT-8** (scale-incommensurable comparison): none — the decoder's confidence is a score-margin
  compared to `uncertaintyMargin` in the same units; `computeConfidence` composites three
  [0,1] axes by MIN.
- **DT-9/DT-10** (proxy→target / one-sided insulation): none in L4 (those concerns are L5/resolver).
- **DT-11** (hand-transcribed number): the formatter spelling-survey counts — tracked (**OI-114**).
- **DT-13** (interim exception without retirement): none new (the decoder is dormant, not an interim gate).
- **DT-14** (gate/precondition mismatch): the spelling-pin chosen-quality gate (the DT-14 founder);
  fire rates characterized by pass 1 (OI-104 relates). No new.
- **DT-15** (abstention-movable metric): the decoder abstain rate — tracked (OI-28/OI-33).
- **DT-17** (silently-truncating capability): Nashville chromatic `"?"` (OI-113); the L4
  temporal-extension trigger not coded (OI-18). Tracked.
- **DT-18** (plumbing-commit sync): not an L4-code finding; my own commits verified `git status`-clean.
- **DT-20** (self-defeating instruction): the pass-2 instruction correctly deferred the
  `OPEN_ITEMS.md` read to Task 2 and withheld all conclusion-bearing files until the freeze —
  the DT-20 lesson APPLIED, no violation.
- **DT-21** (layer mis-attribution in the inventory): OI-101's file-table corrections were used;
  re-verified `analysistypes.h`=MIXED, `chordpathdecoder.h`=L4-SCORER — consistent, no new mis-tag.

### 3.3 The one new item — `ExtensionFlags::hasNinth` dead local field (DT-5) → OI-115

`chordanalyzer.cpp`'s anonymous-namespace struct `ExtensionFlags` declares `bool hasNinth`
(`:348` inventory / current source) and assigns it once (`f.hasNinth = f.hasNinthNatural ||
f.hasNinthFlat || f.hasNinthSharp;`), but the field is **read nowhere** — grep-confirmed:
only the declaration and the one assignment exist in the TU, and no occurrence anywhere else
in `src/composing`. `extensionBits()` maps the three individual ninth flags, never the
aggregate; the "has any ninth" concept is served elsewhere by the free function
`hasAnyNinth()`. So `hasNinth` is a **dead / vestigial local field** (DT-5 waste, #6/#12) —
**no runtime effect** (a dead boolean assignment).

This is the **exact class as L3's OI-96** (`extraToneScore`): a dead LOCAL struct field
escapes both the cross-layer fields inventory (`l4_fields.csv` has 0 rows for `ExtensionFlags`
/ `hasNinth`) and pass 1's literal constant-classifier (`pass1_dispositions_oracle.csv` has 0
`hasNinth` rows), so pass 1 did not disposition it. The dedicated local-dead-field sweep is
what surfaces it. It is a hygiene finding, not a correctness defect, and — like OI-96 for L3 —
does not block certification. **New register row OI-115; existing TYPE DT-5, no new catalog entry.**

## 4. The OI-110 instrumentation lifecycle facts + recommendation (Task 4)

**What it is.** The oracle fire-count instrument = **127 default-OFF lines in
`src/composing/analysis/chord/chordanalyzer.cpp`** (the `OracleFireCounters` struct of ~22
counters, ~35 `fbump()`/`g_fireCounters` increment sites scattered through the scoring
helpers, `dumpOracleFireCounters()`/`flushOracleFireCounters()`, and the `atexit`
registration) **+ 6 lines in `tools/batch_analyze.cpp`** (a forward declaration at :130 and
the gated `flushOracleFireCounters()` call at :4620, before `TerminateProcess`). Confirmed by
`git diff --numstat 7f57aad4b5 HEAD` (127 / 6, zero deletions). Byte-identity was proven at
its introduction (`55829ebe15`) for both gated and ungated builds, all suites green (per OI-110 /
the oracle pass-1 report).

**What it measures that nothing else can.** Per-branch/per-term FIRE COUNTS of the oracle's
documented mechanisms over the corpus (analyzeCalls, insufficientData, jointEnabled,
bassEnumerated, dim7BonusFired, the four sus4/dom7b5 structural penalties, augFactorHalved,
wCompleteFired, nonBassPenaltyApplied/Waived, augRootCorrection, sus2ToSus4,
susToMajorOmitsThird, …) — the protocol-P4 "what does it DO" answer for the LIVE vertical
scorer. The batch `.ours.json`/`chordSymbol` output shows only the WINNING chord, not which
internal scoring terms fired, so nothing else in the toolchain counts these internal branches.

**Cost to re-run.** Cheap: set `MU_ORACLE_FIRECOUNT=<file>` and run `batch_analyze` over the
pinned corpus (the pass-1 run covered 352 stems / 122,047 `analyzeChord` invocations in a
normal corpus pass), then read one appended JSON line. No rebuild needed if the counters are
present; a revert-then-re-add is a mechanical edit (revertible, byte-identity proven).

**Cost to keep.** 127 lines of default-OFF weight inside the oracle TU (against #6/#7 — audit
scaffolding co-located with the live scorer); and a real maintenance burden at the planned
**R9 `chordanalyzer.cpp` file-split** — the `fbump()` sites are threaded through the scoring
helpers and must move with each helper.

**Would a later stage reuse it?** Plausibly: **OI-36** (Stage-5 fitter retained-rule liveness
counts at every adoption sandwich) wants exactly per-rule fire counts of the oracle rules, and
the **L5 audit's P4 step** will need the same fire-count pattern for the function layer. This
pass (the L4 second reading) did NOT need to re-run it — the frozen pass-1 fire table + code
reading sufficed.

**Recommendation (mine; the decision is the user's).** **Revert the instrument at the layer-4
audit close**, on #6/#7 cleanliness grounds: it is audit scaffolding, this second pass did not
need to re-run it, and it is cheaply re-addable and byte-identity-proven. IF instead the user
wants the fire-rate diagnostic retained for the imminent L5 audit and the Stage-5 OI-36
liveness checks, then **defer the revert to the R9 split and give it a clean home** (a
diagnostic translation unit), rather than leaving 127 audit lines in the live oracle
indefinitely. Either way the raw counters/aggregators under `tools/audit/l4/` remain as the
reproducible record. **No action taken this pass — facts + one recommendation only.**

## 5. Register outcome

- **NEW: OI-115** — `ExtensionFlags::hasNinth` dead local field (DT-5); §3.3.
- **Reproduced (referenced, not duplicated):** OI-106 (manifest gap — the 2 sampled UNFIT
  constants + the DT-2 sweep's 3 registered hits), OI-103 (decoder-preference manifest gap,
  17 hits), OI-91 (L3 key/mode manifest surface, 64 hits in the MIXED file), OI-97 (L3
  value-copy, 1 DT-3 hit), OI-111 (formatter duplicated tables — my reading adds that the
  21→parent map has a THIRD copy at `chordanalyzer.cpp:1460`, an enrichment for OI-111),
  OI-113 (Nashville `"?"`), OI-114 (spelling-survey counts), OI-102(i)/(ii) + OI-104/OI-108
  (boundary + declared dormancy + never-fires), OI-19/R1/R7 (chord→function coupling), OI-101
  (file-table tags, re-verified consistent).
- **OI-102** updated: the three-session pass-1 plan is complete AND pass 2 is done.
- **OI-110** updated: the lifecycle facts + recommendation added; decision left to the user.

## 6. Certification proposal (Task 5) — PROPOSED, awaiting the user's decision

I propose **certifying layer 4**, on the following, which are all met:

1. **First pass complete** — all three sessions (L4-2a decoder, L4-2b oracle, L4-2c
   satellites) dispositioned every deep row (OI-102 / STATUS).
2. **Blind second reading + error rate measured at full P2 vocabulary** — 121-row reading +
   40-row error-rate, all verdicts frozen at `d716ac1ca8` before any withheld file; **error
   rate 0/40 = 0.0 % substantive**, reading 119/121 concordant.
3. **Every disagreement diagnosed** — the 2 reading-sample diffs are verdict-axis
   (ESTABLISHED-vs-UNFIT on the manifest-gap constants, both readers found the gap); the 2
   reverse-direction rows are row-attribution; **0 substantive misses in either direction, no
   class re-opened.**
4. **The full catalog sweep found no untracked correctness defect** — the one new item
   (OI-115, dead `hasNinth` field) is a DT-5 hygiene/waste issue with no runtime effect, the
   same benign class as L3's OI-96 which did not block certification; DT-16 = 0; the one
   DT-12 hit is a verified false positive.

**Weakened only by named, tracked, non-correctness gaps** (as L1/L2/L3 were when certified):
the manifest gaps OI-91/OI-103/OI-106 (Stage-5/EG-5-owned), the duplications OI-111/OI-97
(fold-at-touch), the display-only OI-113/OI-114, the doc drifts OI-107/OI-112, and the two E4
boundary/retirement questions OI-102(i) (sparse-refinement layer home) and OI-102(ii)
(`chordpathdecoder` retire-vs-survive). None of these is a correctness defect in the surviving
L4 spine.

**This is a PROPOSAL — proposed, awaiting the user's decision.** I do NOT mark OI-84, OI-102,
or the EG-7 entry-gate condition satisfied; those remain OPEN for the user.

## 7. Artifacts + provenance

- Sampler: `tools/audit/gen_pass2_sample_l4.py` (seeds 20260801 / 20260802).
- Blind judgments: `tools/audit/pass2_judge_l4.py` → `tools/audit/l4/pass2_blind_{reading,errorrate}.{csv,json}` (freeze `d716ac1ca8`).
- Comparison: `tools/audit/pass2_compare_l4.py` → `tools/audit/l4/pass2_compare_{reading,errorrate}.csv`.
- Sweep: `tools/audit/gen_signature_sweep.py --layer l4` → `tools/audit/l4/sweep_results.{json,txt}`.
- Corpus `c50002fee1`; inventory instrument commit `7f57aad4b5`; audit HEAD `f1b69cc78d` at Task 0.

# CC Report — L1/L2 Certification Audit, PASS 2 (blinded second reading + signature sweep + measured error rate) — EG-7 / OI-84

> **Author: Claude Code, executing the L1/L2 audit PASS-2 instruction (Cowork, 2026-07-11).**
> Read-only fact-finding: no `src/` change, no constant tuned, no golden refresh; `tools/robust_stop/`
> and `tools/corpus/` untouched. This is **PASS 2 of 2** — the independent second reading (protocol
> P5), the measured error rate (P6), and the full DEFECT_TYPES signature sweep (P8, second run).
> **Certification is PROPOSED here, not granted** — the user decides (Task 4, point 4).
>
> **Provenance.** Inventoried at HEAD `7123c7cb55` (the pass-1 freeze), corpus `c50002fee1`. Pass-2
> commits: the blind reading `52d0623226` (`feat(tools)`, the P5 blinding boundary for this pass), the
> signature sweep + comparison + error-rate `b8dc714f50` (`feat(tools)`), and this `docs(cc)` fold.
> All figures in this report enter via generated artifacts under `tools/audit/l1l2/` (#17(f)); none is
> hand-transcribed.

---

## 0. What this pass is, and the blinding I actually had

The mission of the second reading (P5) is to **find what pass 1 missed** — it is rewarded by
disagreement, not agreement. I formed every verdict from the code (all 13 L1/L2 files read in full)
**before** opening any pass-1 disposition, report, or `OPEN_ITEMS.md` row.

**When each withheld file was first opened.** All were first opened in Task 2, **after** the Task-1
blind commit `52d0623226`:

| file | first opened |
|---|---|
| `cc_l1l2_audit_pass1_report.md` | Task 2, after `52d0623226` |
| `tools/audit/l1l2/pass1_dispositions.csv` / `.json` | Task 2, after `52d0623226` |
| `OPEN_ITEMS.md` (the deferred mandatory read) | Task 2, after `52d0623226` |
| `DEFECT_TYPES.md` | Task 2, after `52d0623226` |
| `cowork_siloed_facts_audit.md` | **not opened** — not required for the L1/L2 row comparison |
| `cowork_adjudication_dossier.md` | **not opened** — not required for the L1/L2 row comparison |

**Honest limit on the blinding (declared).** `STATUS.md` is a required Task-0 read, and its most-recent
block **summarizes pass 1's headline conclusions** (OI-85/86/87, DT-18/19, "the surviving L1/L2 spine
is sound"). So my blinding was **partial**: I saw pass 1's high-level verdict before reading code, but
**not** its row-by-row dispositions, its report, or the `OPEN_ITEMS` detail. My per-row verdicts were
nonetheless produced from the code itself (grep-verified consumers, read edge cases), which is what P5
requires. Where a pass-2 finding coincides with the STATUS headline I say so and do not claim it as new.

---

## 1. How the two samples were drawn (seeds recorded)

Both samples come from `tools/audit/gen_pass2_sample.py`, which rebuilds the disposition domain from the
**non-verdict** inventory files only (`file_table.csv` + `l1l2_*.csv` = 688 rows: 472 inventory + 216
file rows), so drawing them never reads pass 1's verdicts.

- **Blind sample (P5 / Task 1) — 110 rows, seed `20260711`.** Stratified across the five row kinds in
  proportion to their counts (function 14 / literal 23 / field 10 / branch 47 / crosslayer 16, by
  largest-remainder over 55/92/39/192/66), every one of the 13 L1/L2 files represented (0 coverage
  top-ups needed), processed in the script's shuffled order. Verdicts in
  `tools/audit/l1l2/pass2_blind_sample.{csv,json}`.
- **Error-rate sample (P6 / Task 4) — 40 rows, seed `424242`.** Uniform over the full 688-row domain
  (kinds: file 16, branch 9, crosslayer 5, function 5, literal 3, field 1, decl 1). Checks in
  `tools/audit/l1l2/pass2_errorrate_sample.{csv,json}`.

**One tooling bug found and fixed before use (a #13 stop, not hand-patched).** The first sampler run
gave duplicated/gapped `process_order` values: `draw_blind` and `draw_error` mutated the **same** row
dict objects, so a row drawn into both samples had its blind order clobbered by the error draw. Fixed by
deep-copying rows per sample; re-ran; verified `process_order` unique 1..110 and 1..40, 6 harmless
overlaps now isolated. The artifacts were regenerated, never hand-edited.

---

## 2. Task 2 — the two readings compared (81 agree / 29 diff), each diagnosed

`tools/audit/pass2_compare.py` matches my 110 blind rows to pass 1's dispositions by `(kind, file,
line)` and compares at the **flagged-vs-clean** level (my `flag != CLEAN` vs pass-1 verdict in
{UNFIT, ASSUMPTION, SURVIVES-MIXED, RETIRES}). Result (`pass2_compare.txt`): **AGREE 81, DIFF 29,
NO-MATCH 0** of 110 → a naive flag-level disagreement of **26 %**.

**On the actual findings the two passes AGREE.** Every substantive flag matched: the upward L1→L4
include (`regiontoneprimitives.cpp:38`→chord, blind FLAG = pass-1 ASSUMPTION), the three
`findTemporalContext` branches that run the full Layer-4 analyzer (blind FLAG = pass-1 SURVIVES-MIXED),
the constants-not-in-manifest (`k`, `DECAY_RATE`, `LOOKBACK/LOOKAHEAD_BEATS`, `coincidenceWeight` — blind
UNFIT = pass-1 UNFIT), the retiring Jaccard detectors (blind FLAG-MINOR "retires R6" = pass-1 RETIRES),
and the two beat-weight tables (blind FLAG-MINOR = pass-1 SURVIVES-MIXED).

**The 29 DIFFs decompose — none is a substantive factual contradiction:**

| class | n | rows | what it is | protocol diagnosis |
|---|---|---|---|---|
| **Module-propagation** | 13 | 8,14,28,32,40,44,45,62,76,78,84,85,94,98,103 (branches/fns) | pass 1 blanket-applies **SURVIVES-MIXED** to every branch of a mixed-layer *file*; I judged each branch's control flow **CLEAN** and only flagged where the layering issue is locally visible | the verdict vocabulary (P2) does not fix whether a file-level layering concern **propagates to every row** or stays a file-row. Not a miss by either — a granularity choice. Pass-1's propagation slightly inflates its flagged count without adding a row-level finding. |
| **Legacy-retire** | 2 | 48,55 (collectPitchContext branches) | pass 1 = **RETIRES(R5)**; I = SURVIVES/CLEAN (I noted "legacy builder" in the reason but did not elevate it to the verdict) | **my under-classification.** I applied the correctness question and answered "yes", but treated retirement-status as a file property. Pass-1's RETIRES is the sharper verdict → pass 1 was MORE complete here. |
| **Dormancy: prose vs row** | 11 | 23,29,53,66,79,83,92,95,97,101,104 (spelling/phrase/config) | I flagged dormancy **per-row** (FLAG-MINOR); pass 1's **row verdict** is PUBLISHED/SURVIVES but its **narrative §3d + fire-rate §4** flag the same dormancy | substantive **agreement**; pass 1 encoded dormancy in prose + the fire-rate table, not the per-row verdict. Same finding, different location. |
| **Doc-precision (new, mine)** | 1 | 6 (`extend()`) | I flagged the `note_model.h` comment "no layer calls it yet" as stale; pass 1 = SURVIVES/dormant, calls the doc accurate | see §5-A — a minor observation the second pass adds; the **dormancy substance agrees**. |
| **Judgment tie** | 1 | 16 (`4.0` beatsPerUnit) | pass 1 = UNFIT (not-in-manifest length-scale); I = ESTABLISHED (structural "4 beats per 4/4 measure") | a genuine ESTABLISHED-vs-UNFIT tie on a structural-yet-tunable length-scale. Both defensible. |
| **Matching artifact** | 1 | 26 (`regiontonecollector.cpp:297`) | line collision: two literals at :297 (the `1.0` base and the `0.3` boost); my sampled row is the `1.0` (ESTABLISHED), the co-located `0.3` is UNFIT | substantive **agreement** (the `1.0` is ESTABLISHED in both); the matcher pulled in the co-located row's verdict. |

**Net.** After diagnosis, the only genuine verdict-level differences are: **2 rows where pass 1 was more
complete** than my blind reading (`collectPitchContext` RETIRES), **1 row where I add a minor observation
pass 1 did not make** (the `extend()` doc wording), and **1 genuine judgment tie** (`4.0`). The remaining
25 DIFFs are recording granularity (module-propagation, dormancy-in-prose) over the same underlying facts.

---

## 3. Task 3 — the full DEFECT_TYPES sweep over the entire L1/L2 inventory (all 19 entries)

`tools/audit/gen_signature_sweep.py` runs the mechanical rules across **all** L1/L2 rows and fails loudly
if any rule cannot run (`sweep_results.{json,txt}`). The review-only rules were applied by reading the
inventory row by row. Two false-positive tool bugs and one silent-no-op were found and fixed before use
(DT-5 basename exclusion; DT-16 comment/builder false hits; DT-3 over-broad; DT-12 content-blind + a
silent skip of bare-filename anchors) — re-stamped, never hand-edited.

### 3.1 Mechanical rules

| DT | rule | hits | finding | new or covered |
|---|---|---:|---|---|
| **DT-2** | named constant not in `param_manifest.json` | 16 | the beat table, sliding-window (`LOOKBACK/LOOKAHEAD_BEATS`, `DECAY_RATE`, `LOOKAHEAD_WEIGHT`), `SpanWindowWeights` seeds, `weightedPcView` 0.3/1.5, phrase `k`/`minSilenceTicks`/`coincidenceWeight`, `kPass2bMinRegionTicks` | **covered — OI-87** (independently reproduced) |
| **DT-3** | value-copied constant (agree by comment, not reference) | 2 genuine | `SpanWindowWeights::decayRate=0.7` "== scoreharvest DECAY_RATE" and `lookaheadWeight=0.5` "== scoreharvest LOOKAHEAD_WEIGHT" (`regiontonecollector.h:249-250`) — literals coupled by comment to `scoreharvest::` constants of the same value | **refinement of OI-87/OI-86** — pass 1 flagged these as not-in-manifest but not as a value-copy; the coupling risk (a refit of `scoreharvest::DECAY_RATE` silently diverges from this default) is the #6/DT-3 angle. (3rd raw hit `note_model.h:87 duration=0` is a false positive — a zero-init + semantic comment.) |
| **DT-5** | derived fact with 0–1 consumers | 4 dormant + 4 single-consumer | 0 consumers: `sharpFlatSense`, `spanSpelling`, `SpanSpelling`, `computePhraseBoundaryProfile`; 1 consumer (live, not defects): `beatTypeToWeight`, `beatTypeForOnsetTick`, `distinctPitchClasses`, `buildPedalWindowIndex` | **covered — §3d** (declared-dormant, consumer named). The 1-consumer set is a threshold artifact (live single-consumer helpers), noted not flagged. |
| **DT-12** | stale anchor / dangling reference | 1 | `slicer.h:68` cites "`regionanalyzer.cpp:579` → `KeyModeSequenceDecoder::decode`", but the decode call is at `:634`/`:705` (line 579 is a Layer-1 comment) | **NEW** — a genuine stale file:line anchor pass 1 did not record → OI-88. (18 `.md` refs + 2 file:line anchors checked; the second anchor `spellingview.h:41`→`chordslicedecoder.cpp:553` points into the spelling-pin's doc block, the actual `lineOfFifths` call is at `:610` — borderline, not flagged.) |
| **DT-16** | raw-DOM note re-read outside the L1 note model | 4 | `collectPitchContext`, `detectOnsetSubBoundaries`, `detectBassMovementSubBoundaries`, `findTemporalContext` walk engraving-DOM notes directly (`toChord(cr)->notes()`, `n->ppitch()`) instead of the note model | **refinement of OI-86** — the same functions pass 1 named as the grab-bag; the sweep gives the mechanical reason they are mixed-layer. All 4 ride existing retirements (R5/R6) or the E4 move (`findTemporalContext`). The note-model builder (`note_model.cpp`) is correctly excluded — it IS the layer that reads the DOM. |
| **DT-19** | upward cross-layer include | 4 | `metricweights.h:42`→`key/` (L3); `regiontonecollector.cpp:37`, `regiontoneprimitives.cpp:37/38`→`chord/` (L4) | **covered — OI-86** (independently reproduced, exact) |

### 3.2 Review-only rules (applied row-by-row; rows checked = the full L1/L2 inventory)

- **DT-1** (unverified causal premise, Class A): **0.** L1/L2 is the fact/segmentation layer — it makes no
  key/chord decision, so it carries no load-bearing causal premise about the analysis. The weighting
  magnitudes (0.3/1.5/decay) are heuristic weights (DT-2), not Class-A premises. Confirms pass-1 "no Class-A".
- **DT-4** (silent overwrite of a committed field): **0.** L1/L2 produces facts and does not mutate a
  committed chord/key result. `findTemporalContext` runs the analyzer but reads its result, it does not
  overwrite a committed struct.
- **DT-6** (duplicated derivation): the two BeatType→weight tables (`regionMetricWeightForBeatType`
  hardcoded vs `beatTypeToWeight` prefs) and the bass=lowest-pitch recompute at
  `buildTones`/`weightedPcView`/`pitchContextOverSpan` — **both already registered** (OI-86 #6; OI-77).
- **DT-7** (never-fires / always-fires): the only zero-fire mechanisms are declared-dormant future-consumer
  paths (spelling, phrase, `extend()` on production) — **covered §4/§3d**. No surviving mechanism never-fires.
- **DT-8, DT-9, DT-15** (scale-incommensurable comparison / unvalidated proxy / abstention-movable metric):
  **N/A** — L1/L2 emits no confidence quantity, no proxy, no quality metric.
- **DT-10** (one-sided insulation claim): the slicer's "clip inert on whole-score" and the note-model
  "byte-identical" claims **enumerate their false-negative path** (`loadedStart<=front` etc.) and are
  test-backed. **0 one-sided claims.**
- **DT-11** (hand-transcribed measurement number): the L1/L2 **source** carries no measurement figures
  (only design-doc citations); this **report** uses generated artifacts only. **0.**
- **DT-13** (interim exception without a wired retirement): every L1/L2 interim names its retirement —
  `extend()` Phase-1a re-walk → Phase-1b; `detectOnset/BassSubBoundaries` → R6; `collectPitchContext` →
  R5; `findTemporalContext` → E4. **0 un-wired.**
- **DT-14** (gate/precondition mismatch): the pedal Pass-4 machinery fires only when a sustain pedal is
  present (≈0 on the Bach corpus) and the dense-start exclusion is batch-only — both are **documented
  population-scoping, correctly gated**, not a mismatch bug. Noted, not a defect.
- **DT-17** (silently-truncating capability): pass-1 P3 (§5) found no L1/L2 contract gap; the missing
  owned bass-view is **OI-77** (registered); `extend()` Phase-1b is deferred-not-silent. **0 new.**
- **DT-18** (plumbing commit index/disk desync): the pass-2 commits were verified disk==HEAD after each;
  the stale-lock incident (§5-C) is the OI-85 concurrent-git-hazard family, not a desync. **0 new.**

**No NEW defect TYPE is warranted.** Every sweep hit is an instance of an existing catalog entry
(DT-2/3/5/12/16/19); the doc-precision items (§5-A/B) are DT-12/#10-class instances, not a new pattern.
`DEFECT_TYPES.md` is therefore not extended by this pass.

---

## 4. Task 4 — measured audit error rate (P6)

`tools/audit/pass2_apply_errorrate.py` records the deep verification of pass 1's verdict on all 40
uniform-random rows (I read the code, its callers, and the settling data for each):

> **0 WRONG of 40 → measured error rate 0.0 %.**

No failing rows. The one row that repaid scrutiny was **process-order 33** — `collectPitchContext` →
**RETIRES(R5)**: correct, and it is exactly the class my *blind* reading under-classified (§2, the two
collectPitchContext branches). One near-miss worth recording (not an error): **process-order 38**,
`wInterOnset` → UNFIT — the disposition verdict is correct (a manifest-tracked but precision-phase /
not-yet-fit param is legitimately UNFIT under #19), but pass 1's **report prose §3c** loosely calls the
same param "ESTABLISHED-as-tracked" — a minor internal prose-vs-disposition drift inside pass 1, not a
wrong verdict.

**Honest caveat on the 0.0 %.** The 688-row domain is dominated by low-difficulty rows — 216 file tags
(mechanical L1/L2/L3+/RETIRES) and 192 branches (verdict inherited from the enclosing function). A
40-row uniform draw is therefore ~⅓ file tags + ~¼ inherited branches, and the 0 % is strongest for
those classes. The real judgment risk lives in the ~46 flagged rows (the constants, upward deps,
mixed-layer functions, dormancy) — and those are exactly what the **blind reading (§2) cross-checked
and found aligned**. So the two P5/P6 instruments are complementary: P6 shows the mechanical mass is
right; P5 shows the judgment rows agree.

---

## 5. New / refined findings this pass surfaced (→ OI-88; refinements to OI-86/OI-87)

**A. `extend()` docstring wording (DT-12/#10-class, minor).** `note_model.h:157-163` says the live path
"uses the whole-score `build(sc)` only" and "**no layer calls it yet** — that is Phase 3 reach-back."
The **substance is correct** — `extend()` fires 0 times on production — but the wording "no layer calls
it yet" is literally contradicted by three production call sites: `regionanalyzer.cpp:702` (the
reach-back loop, gated by `ReachBackOptions::enabled`, **default false** — "the production path"),
`chordslicedecoder.cpp:1387/1393` (gated by `decoderPrefs.enableEdgeExtension` on the dormant L4
decoder), and `textureclassifier.cpp:183/187`. A reader grepping for callers finds three; the comment
says none. A one-line clarification ("no layer calls it on the live/production path yet; the reach-back
call sites are gated off by default") removes the trap. Pass 1's dormancy verdict is correct; this is a
wording nit the second pass adds.

**B. Stale file:line anchor (DT-12, minor).** `slicer.h:68` cites "`regionanalyzer.cpp:579` →
`KeyModeSequenceDecoder::decode`"; the decode calls are at `:634`/`:705` (line 579 is now a Layer-1
note-model comment). The line number drifted as the file grew.

**C. The pass-2 git incident (OI-85 family, DT-18-adjacent).** Staging the Task-1 commit hit a **stale
`.git/index.lock`** (zero-byte, 29 minutes old, no live `git.exe` process) — the concurrent-edit hazard
OI-85 records. Removed READ-ONLY (the lock is only the mutex; the index was intact, nothing discarded);
staging then succeeded and disk==HEAD was verified. Same class as OI-85/DT-18, a different mechanism (a
crashed-process lock, not a plumbing desync).

**D. Refinements to existing rows (referenced, not duplicated):** the `SpanWindowWeights` 0.7/0.5
value-copy (DT-3) sharpens **OI-87/OI-86**; the four raw-DOM note re-readers (DT-16) sharpen the
**OI-86** grab-bag with a mechanical reason.

---

## 6. Certification proposal (Task 4 point 4) — PROPOSED, awaiting the user's decision

I only **propose**; Cowork verifies this report against the code and the **user decides**. I do **not**
mark OI-84 or EG-7 satisfied.

**The proposal.** Both required conditions hold:

1. **Both passes complete.** Pass 1 (blind enumerative, P1–P4) delivered the total inventory + a
   closed-set verdict for all 688 rows. Pass 2 (this session) delivered the independent blind reading
   (P5), the full DEFECT_TYPES sweep (P8 second run), and the measured error rate (P6).
2. **Error rate measured:** 0.0 % (0/40), with the honest caveat in §4.
3. **Every disagreement diagnosed:** the 29 flag-level DIFFs are classified in §2 (13 module-propagation,
   2 my-under-classification, 11 dormancy-prose-vs-row, 1 doc nit, 1 tie, 1 matching artifact); no
   substantive factual contradiction survives.

**What certification would rest on, stated precisely.** The audited **surviving L1/L2 spine — the
lossless note model (L1) and the change-point slicer (L2) — is sound**: independently confirmed clean,
edge-complete, and established (tie resolution, true-span segment-tree overlap, deterministic pure
change-point enumeration, byte-identical whole-score path). Across both passes: **no Class-A unverified
causal premise, and no correctness bug.** Every flagged item is one of a small, bounded set, all tracked
and none a correctness defect:

- **Upward layering deps + mixed-layer grab-bags** (OI-86 / DT-19 / DT-16) — dissolve at the E4
  retirements R4/R5/R6 and the `findTemporalContext`→E4 move; re-verify at each.
- **Hand-set inference constants outside the fit manifest** (OI-87 / DT-2), incl. the `SpanWindowWeights`
  value-copies (DT-3) — Stage-5 / EG-5 manifest extension.
- **Declared-dormant published facts** (spelling, phrase — DT-5/§3d) — consumer named, corollary-cleared.
- **Two minor doc-precision items** (§5-A/B → OI-88).

**Therefore I propose:** certify the **surviving L1/L2 spine (note model + change-point slicer)** as
audit-clean and fit to carry load into E4, with OI-86 / OI-87 / OI-77 / OI-88 recorded as known,
non-correctness, tracked-to-dissolve items — **status: proposed, awaiting the user's decision.** If the
user prefers to withhold certification until the mixed-layer files (`metricweights`, the engravingbridge
grab-bag) are actually split and the upward deps removed, the concrete remaining work is exactly
OI-86 (the E4 retirements) — nothing else in L1/L2 blocks correctness.

---

## 7. Commits, registers, push

- `52d0623226` (`feat(tools)`) — the blind reading + samples (P5 blinding boundary for this pass).
- `b8dc714f50` (`feat(tools)`) — the signature sweep + comparison + error-rate check.
- this `docs(cc)` fold — this report + the error-rate sample fill + **OI-88** (new) + STATUS + handoff.

Register: **OI-88** (the pass-2 doc-precision findings §5-A/B); OI-86 / OI-87 / OI-77 referenced with the
pass-2 refinements, not duplicated. `DEFECT_TYPES.md` unchanged (no new type). Read-only throughout;
`tools/robust_stop/` + `tools/corpus/` untouched; fork-only, `upstream` never pushed.

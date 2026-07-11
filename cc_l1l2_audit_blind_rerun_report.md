# CC Report — L1/L2 Certification Audit: FULLY-BLIND RE-RUN of the second reading + error-rate — EG-7 / OI-84 / OI-89

> **Author: Claude Code, executing `cc_instruction_l1_l2_audit_blind_rerun.md` (Cowork, 2026-07-11).**
> Read-only fact-finding on the audited layer: no `src/` change except the two authorized comment-only
> doc fixes (Task 4); no constant tuned, no golden refresh; `tools/robust_stop/` and `tools/corpus/`
> untouched. This re-runs ONLY the two blinding-dependent measurements of pass 2 (the independent second
> reading P5 + the error rate P6), this time **fully** blind — the catalog sweep (P8) from pass 2 stands
> and is NOT repeated.
>
> **Why this session exists.** Pass 2 declared its second reading only PARTIALLY blind: its instruction
> required reading `STATUS.md` at Task 0, and `STATUS.md` carried pass 1's headline verdict ("the
> surviving L1/L2 spine is sound"). The user WITHHELD certification of layers 1 and 2 pending an
> independent reading that never saw any prior conclusion (register OI-89; catalog DT-20). This is that
> reading. **Certification is PROPOSED here, not granted — the user decides; Cowork verifies at the code.**
>
> **Provenance.** Inventory frozen at the pass-1 manifest (`tools/audit/l1l2/manifest.json`, instrument
> `gen_inventory.py`, corpus `c50002fee1`, 688-row domain). Session HEAD at start `b5a9be9ac1`. All
> figures enter via generated artifacts under `tools/audit/l1l2/` (#17(f)); none is hand-transcribed.

---

## 0. The blinding I actually had (the whole point of this session)

Every one of my 111 + 40 verdicts was formed from the code alone — all 13 L1/L2 files read in full,
consumers grep-verified, edge cases traced — **before** opening ANY withheld file. The Task-1 sample +
verdict commit **`fbcb59c8d7`** is the unblinding boundary: the withheld list was lifted only after it.

**When each withheld file was first opened** (all AFTER `fbcb59c8d7`):

| file | first opened |
|---|---|
| `OPEN_ITEMS.md` (the deferred mandatory session-start read) | Task 2, after `fbcb59c8d7` |
| `DEFECT_TYPES.md` | Task 2, after `fbcb59c8d7` |
| `STATUS.md` | Task 2, after `fbcb59c8d7` |
| `cc_l1l2_audit_pass1_report.md`, `cc_l1l2_audit_pass2_report.md` | Task 2, after `fbcb59c8d7` |
| `tools/audit/l1l2/pass1_dispositions.csv/.json` | Task 2, after `fbcb59c8d7` |
| `tools/audit/l1l2/pass2_blind_sample.*`, `pass2_errorrate_sample.*` | Task 3, after `fbcb59c8d7` |
| `cowork_handoff.md` | Task 5, after `fbcb59c8d7` |
| `pass2_compare.txt`, `tools/audit/l1l2/sweep_results.*` | **not opened** — would leak pass-2 conclusions; not needed |
| `cowork_siloed_facts_audit.md`, `cowork_adjudication_dossier.md` | **not opened** — not required for the row comparison (same as pass 2) |

**This is a strictly stronger blinding than pass 2 had.** Pass 2 saw the `STATUS.md` headline before
reading code (its own §0 declares it). I did not open `STATUS.md`, `OPEN_ITEMS.md`, or anything
verdict-bearing until after freezing every blind verdict. To keep the blinding tight I also did NOT read
pass 1's disposition-generator (`gen_dispositions.py`) or the pass-2 apply/compare/sweep scripts (they
encode prior verdicts); I read only the non-verdict inventory tables + `gen_inventory.py` +
`gen_pass2_sample.py`'s CODE (not its outputs) + the source.

---

## 1. The two samples (new seeds, recorded)

Drawn by a NEW, independent instrument `tools/audit/gen_blind_rerun_sample.py` (modeled on
`gen_pass2_sample.py`'s structure by reading its code, never its outputs). It rebuilds the 688-row
domain from the non-verdict inventory only (`file_table.csv` + `l1l2_*.csv`, load order identical to
pass 2's so the global row index lines up row-for-row). Deterministic: byte-identical on re-run
(verified).

- **Reading sample (P5) — 111 rows, seed `20260712`** (≠ pass 2's `20260711`). Stratified across the
  five row kinds proportional to counts (function 14 / literal 23 / field 10 / branch 47 / crosslayer
  16, largest-remainder over 55/92/39/192/66), + 1 coverage top-up (`slicer.h:86` field) so **all 13
  L1/L2 files are represented**. Verdicts: `blind_rerun_reading.{csv,json}`.
- **Error-rate sample (P6) — 40 rows, seed `20260713`** (≠ pass 2's `424242`). Uniform over the full
  688-row domain (kinds: file 11, branch 9, literal 7, crosslayer 4, function 4, field 3, decl 2).
  Judged blind FIRST (my verdict recorded before any pass-1 comparison). Verdicts:
  `blind_rerun_errorrate.{csv,json}`.

Verdict vocabulary is the P2 rubric (`cowork_audit_protocol.md`): code→SURVIVES/RETIRES,
constant→ESTABLISHED/UNFIT/DEAD, field→PUBLISHED/SILOED/TRAPPED/DUPLICATED, crosslayer→layer-adherent
or back-edge, file→its tag. Each row also carries an explicit `flag` (issue / clean).

**My blind result.** Reading: 109 clean / **2 issue** (verdicts 77 SURVIVES / 23 ESTABLISHED / 11
PUBLISHED). Error-rate: 40 clean (I flagged none). The 2 issues:
- `regiontonecollector.cpp:37` includes `chord/analysisutils.h` (an L1.5→L4 edge) but uses **none** of
  its 6 exported symbols (grep-verified) — a candidate **unnecessary** cross-layer include (removability
  needs a build-confirm). Include hygiene, not a correctness defect.
- `note_model.cpp:204` `extend()` — the impl is correct, but the "who consumes it?" question exposed
  that its docstring at `note_model.h:161-163` said "no layer calls it yet" while production call sites
  exist. (Independently re-found blind; = OI-88(b) — see Task 4.)

---

## 2. Task 2 — my blind verdicts vs pass 1's dispositions, on the same rows

Compared mechanically by `tools/audit/compare_blind_rerun.py` (matches each of my rows to pass 1's
disposition by kind/file/line + discriminator; normalizes both vocabularies to issue-ness).

| sample | rows | issue-ness AGREE | DISAGREE |
|---|---|---|---|
| reading | 111 | **94 (84.7 %)** | 17 |
| error-rate | 40 | **35 (87.5 %)** | 5 |

**The disagreements decompose into three systematic verdict-AXIS differences — ZERO code-correctness
misses in either direction.** Every disagreement is a case where pass 1 assigned a disposition that
requires knowledge NOT derivable from a blind code-reading (the R1–R9 retirement map, the DEFECT_TYPES
catalog, or the `param_manifest.json` license) — and each maps to an already-registered finding.

**The retirement-map axis (10 reading + 2 error-rate = 12 rows).** Pass 1 verdicts the legacy
key-context / sub-boundary builders (`collectPitchContext`, `detectOnsetSubBoundaries`,
`detectBassMovementSubBoundaries`, and their branches) **RETIRES** — they retire at E4 with the legacy
key resolver / legacy segmenters (R5/R6). I read the same code as **SURVIVES** (sound, correct,
edge-complete) — and even NOTED the planned retirement in `collectPitchContext`'s reason. Diagnosis:
the P2 code axis is literally "RETIRES(R1–R9)/SURVIVES" = a **retirement-map** axis; the R1–R9 map is
roadmap knowledge, not in my blind inputs (inventory tables + code). A blind reader lacking it reads
correctness (SURVIVES). **Neither reading is wrong — the code IS sound AND IS scheduled to retire.** No
defect hidden. (Tracked: OI-65 retirement map; the functions ride R5/R6 per OI-86.)

**The precision-phase / manifest-gap constants (6 reading + 2 error-rate = 8 rows).** Pass 1
verdicts hand-set inference constants **UNFIT** under the strict #19 standard (not positively
established until fit at Stage 5, and DT-2 manifest cross-check): DECAY_RATE 0.7, cross-voice 1.5,
repetition 0.3, coincidenceWeight 0.0, wPitch 0.20, wInterOnset 0.30, spikeCeilingFactor 1.5,
LOOKAHEAD_BEATS 8. I verdicted them **ESTABLISHED** ("documented design default, fit for the
mechanism-fixing purpose"). Diagnosis: a **threshold difference on the constant axis** + **DT-2
under-recognition** — the DEFECT_TYPES catalog and the `param_manifest.json` concept were withheld from
me; the P8 signature sweep (with the catalog, pass 2) is precisely the step that flags these, which is
why P8 mandates a catalog-aware second pass. I correctly marked the *structural/identity* literals (pc
`% 12`, tree-index `2`, accumulator `0.0`) ESTABLISHED and agreed with pass 1 on those. (Tracked: OI-87
/ OI-23 / DT-2.)

**The upward cross-layer include policy (1 error-rate row).** `metricweights.h:42`→`key/` — pass 1
flags it ASSUMPTION (every upward include is a #7 layering finding, DT-19). I recognized the coupling
but marked it clean-with-note ("used, intrinsic"), flagging only the *unused* sibling
(`regiontonecollector.cpp:37`, where pass 1 and I AGREE — both flagged it). Diagnosis: without DT-19 in
hand I flagged an upward include only where I saw concrete removability, not categorically. (Tracked:
OI-86 / DT-19.)

**The extend() docstring (1 reading row, #68).** I flagged it (docstring stale); pass 1's
row-disposition noted dormancy (`fire=0`) and filed the staleness at the pass-2 doc-precision level
(OI-88 / DT-12). Same finding, different placement — **substantively concordant**, and an independent
blind re-discovery of OI-88(b).

**Bottom line of the comparison: not one disagreement is a missed defect.** Every one is pass 1 being
*more conservative* (flagging retirement-scheduled code and unfit constants a blind reader reads as
sound/documented) — i.e. pass 1 did not under-report; if anything my blind pass under-flagged the
catalog-driven types, and pass 1 correctly caught them. My blind reading independently reproduces pass
1's substantive conclusion — **the L1/L2 code is correct; the only findings are the tracked OI-86 /
OI-87 / OI-88 items** — and adds one refinement (the `analysisutils.h` include is not merely upward but
unused).

---

## 3. Task 3 — did the leak matter? (full-blind vs pass 2's partially-blind aggregates)

| measure | pass 2 (partial blind, saw STATUS headline) | this re-run (fully blind) | moved? |
|---|---|---|---|
| reading FLAG rate | 26 / 110 flagged = **23.6 %** (84 CLEAN / 22 FLAG-MINOR / 4 FLAG) | 2 / 111 = **1.8 %** | **yes, ~13×** |
| error rate (vs pass 1) | **0 / 40 = 0.0 %** | **5 / 40 = 12.5 %** | **yes** |
| KINDS flagged | upward includes, unfit/manifest constants, raw-DOM readers, doc staleness | the same classes (OI-86/87/88; DT-2/12/19) | **no** |
| any correctness bug | none | none | **no** |

**The honest answer: the leak moved the agreement NUMBERS but not the SUBSTANCE.** Both numbers are
sensitive to two things the leak/partial-blinding supplied — catalog possession and a shared frame — and
neither is a measure of code pathology:

- The **flag rate** collapses 23.6 %→1.8 % under full blinding because pass 2's flags were
  catalog-driven (a FLAG-MINOR on every DT-2 constant, DT-16 raw-DOM reader, DT-19 include). A reader
  without the catalog flags only what is egregious unaided (the unused include, the stale doc). The flag
  rate is revealed to be a function of *catalog possession*, not of defects.
- The **error rate** rises 0/40→5/40 because pass 2's 0/40 rested on a **shared frame** (the catalog +
  the leaked "spine is sound" headline): pass 2 reproduced pass 1's dispositions, including its
  UNFIT/RETIRES/ASSUMPTION flags, so it agreed 100 %. Remove that frame and a truly-blind reading
  diverges on exactly those catalog/retirement-map/manifest-driven verdicts — 12.5 %, **all of it
  verdict-axis, none of it a missed defect.** So the 0/40 was partly an artifact of the shared frame;
  12.5 % is the honest, un-anchored figure.
- The **kinds** of things flagged and the **correctness conclusion** are unchanged. Under full,
  un-anchored blinding an independent reader finds the same finding-classes and **no correctness bug** —
  the exact conclusion pass 1/2 reached. The leak did **not** cause pass 2 to miss anything (my blind
  pass finds nothing pass 2 missed); it made pass 2's agreement numbers look better than a truly-blind
  reading produces.

Per the instruction's warning: two whole CLASSES were "judged differently," and I state it plainly —
but neither class is "judged *wrongly*." The retirement-map class (my SURVIVES vs pass 1's RETIRES) and
the precision-constant class (my ESTABLISHED vs pass 1's UNFIT) are **verdict-axis/threshold
differences**, each traceable to withheld external knowledge, each already registered. There is no class
of rows where a real defect was missed and averaged away.

---

## 4. Task 4 — the two authorized doc fixes (comment-only; committed `f76e8b65c8`)

Both verified at the code first (line numbers had NOT moved; the call sites and gates were confirmed by
`grep`/`sed`), then reworded. **Comment-only; no compiled behavior can change (comments are stripped by
the preprocessor).** The self-check re-read the diff: two `//`-comment blocks, no code line touched.

- **`slicer.h:68`** — was `regionanalyzer.cpp:579 -> KeyModeSequenceDecoder::decode`; the decode calls
  are at `regionanalyzer.cpp:634` and `:705` (line 579 drifted onto a Layer-1 comment). Rewritten to
  lead with the symbol and cite **both** call sites (`… -> KeyModeSequenceDecoder::decode, at :634 and
  :705`) so the symbol name — not a bare line number — is the anchor.
- **`note_model.h:161-163`** — was "no layer calls it yet — that is Phase 3 reach-back," contradicted by
  three gated production call sites. Reworded to state the capability is **dormant in SUBSTANCE, not
  unused: callers exist but are gated off on the production path** — `regionanalyzer.cpp:702` (behind
  `ReachBackOptions::enabled=false`), `chordslicedecoder.cpp:1387/1393` (behind the decoder's
  `enableEdgeExtension`), `textureclassifier.cpp:183/187` — **so extend() fires 0 times on production**
  (pass 1's measured fire-rate). The Phase 1a/1b explanation above it is left intact. New anchors are
  paired with their gate/symbol names to resist future drift (DT-12).

These resolve both OI-88 items.

---

## 5. Certification proposal (Task 5.1) — PROPOSED, awaiting the user's decision

I only **propose**; Cowork verifies this report at the code; the **user decides**. I do NOT mark OI-84
or EG-7 satisfied.

**I propose CERTIFYING the surviving L1/L2 spine (the lossless note model L1 + the change-point slicer
L2), because the fully-blind re-run SUPPORTS it:**

1. **An independent reader, blind to every prior conclusion (strictly more blind than pass 2), read the
   same 13 files and found NO code-correctness defect anywhere** in 111 + 40 sampled rows.
2. **Every disagreement with pass 1 has pass 1 the more conservative party** — flagging retirement-map
   membership and un-fit constants that I (blind, without the map/catalog/manifest) read as
   sound/documented. Pass 1 did not under-report; the blind pass, if anything, under-flagged catalog
   types, and pass 1 caught them. So the pass-1/pass-2 substantive conclusion is **reproduced, not
   overturned**, under full blinding.
3. **The blinding leak is shown (Task 3) to have moved only the agreement numbers, not the substance.**
   The specific worry OI-89 was created to guard against — that the leaked headline made pass 2 *miss*
   something — is answered by measurement: a truly-blind reading misses nothing pass 2 caught.
4. Every residual finding is bounded, tracked, and non-correctness: upward layering deps + mixed-layer
   grab-bags (OI-86 / DT-19 / DT-16, dissolve at the E4 retirements), hand-set constants off the fit
   manifest (OI-87 / DT-2 / DT-3, Stage-5/EG-5), declared-dormant published facts (fact-publication
   corollary — consumer named), and the two doc-precision items now fixed (OI-88).

**One refinement to hand to Cowork:** `regiontonecollector.cpp:37`'s `analysisutils.h` include appears
**unused** (removable, which would delete that L1.5→L4 back-edge with zero behavior change) — a
sharpening of OI-86; needs a build-confirm before removal, and removal itself waits for the #8 timing
(the E4 retirements), so this is a note, not a fix.

**Honest caveat on the number.** This re-run's measured error rate is **5/40 = 12.5 %**, not pass 2's
0/40. That is not a regression in audit quality — it is the *un-anchored* figure, and it decomposes to
**zero correctness misses** (§2/§3). Read it as "a fully-blind reader diverges from the informed
dispositions only on catalog/retirement-map/manifest verdicts it could not derive blind," not as "12.5 %
of the audit is wrong."

**Status: proposed, awaiting the user's decision.** If the user prefers to withhold until the
mixed-layer files are actually split and the upward deps removed, the concrete remaining work is exactly
OI-86 (the E4 retirements) — nothing in L1/L2 blocks correctness.

---

## 6. Commits, registers, push

- **`239408faad`** (`docs(cowork)`) — Task 0: Cowork's five waiting files (the two `cc_instruction`
  files are gitignored via `/cc_*.md`; force-added with `git add -f`, matching the repo's established
  convention for tracked `cc_*.md` docs — noted as a deviation from the literal Task-0 `git add` line).
- **`fbcb59c8d7`** (`feat(tools)`) — Task 1: the sampler + both samples with from-scratch verdicts. **The
  unblinding boundary.**
- **`f76e8b65c8`** (`docs(composing)`) — Task 4: the two comment-only doc fixes.
- this **`docs(cc)`** fold — this report + `compare_blind_rerun.py` + register/STATUS/handoff updates.

Register: **OI-88 → RESOLVED** (both fixes, `f76e8b65c8`); **OI-89** status updated (re-run done,
fully blind, confirms pass 1/2 substance; certification decision returns to the user); **OI-86** refined
(the unused `analysisutils.h` include); **OI-84** status note updated. `DEFECT_TYPES.md` unchanged (no
new type). Read-only on the audited layer apart from the two authorized comment fixes.

Push: fork-only (`origin`); `upstream` verified push-disabled and untouched.

# CC — Layer-3 (key/mode) Certification Audit, PASS 2 (blind second reading + catalog sweep + measured error rate) — EG-7 / OI-84

> **Read-only fact-finding.** No production behavior change; no constant tuned; no golden refreshed;
> `tools/robust_stop/` and `tools/corpus/` reference artifacts untouched. This is the SECOND of two
> passes; certification is **proposed here, awaiting the user's decision** — it is not self-granted.
> Protocol: `cowork_audit_protocol.md` (P5 blind second reading, P6 measured error rate, P8 catalog
> sweep). Instruments (all reproducible, byte-identical on re-run): `tools/audit/gen_l3_pass2_sample.py`
> (sampler + verdict merge), `tools/audit/pass2_compare_l3.py` (pass-1 vs pass-2 comparison),
> `tools/audit/gen_signature_sweep.py --layer l3` (the mechanical DT sweep). Corpus pin `c50002fee1`;
> inventory HEAD `9e294f398d`.

## 0. Blinding log (protocol P8, second run) — when each withheld file was first opened

The second reading was FULLY blind: every reading + error-rate verdict was formed from the code and
FROZEN before any withheld file, pass-1 artifact, or the defect catalog was opened. This is the L1/L2
lesson (OI-89/DT-20) applied: the mandatory session-start `OPEN_ITEMS.md` read was deliberately
deferred to Task 2, declared in the instruction preamble (Cowork did the session-start register check
for the dispatch).

**Freeze commit (the blinding boundary): `1021e81e44`.** Every withheld file below was first opened
AFTER it, in Task 2 / Task 3.

| Withheld file | First opened |
|---|---|
| `DEFECT_TYPES.md` | Task 2 (after the `1021e81e` freeze) |
| `OPEN_ITEMS.md` (the deferred mandatory read) | Task 2 |
| `cc_l3_audit_pass1_report.md` | Task 2 |
| `tools/audit/l3/pass1_dispositions.csv` | Task 2 |
| `STATUS.md` | Task 2 (head only, to prepare the Task-5 prepend) |
| `tools/audit/gen_signature_sweep.py` (to extend it) | Task 3 |
| `cowork_handoff.md` (entry block, to update) | Task 5 |
| `tools/audit/l3/firerate.json`, `gen_l3_dispositions.py`, `measure_l3_firerate.py` | not opened this pass (cited from the pass-1 report only) |

**Safe reads used before the freeze:** `CLAUDE.md`, `cowork_audit_protocol.md`, the L3 inventory
tables (`tools/audit/l3/*.csv`, `inventory.json`, `manifest.json`), the sampling script
`tools/audit/gen_pass2_sample.py` (code only, to adapt — explicitly on the safe list), and the source
under `src/composing/`. No `*dispositions*` / `*firerate*` / pass-1 report / catalog file was opened
before the freeze.

## 1. Sample designs + seeds (protocol P5/P6)

Two deterministic samples drawn from the 1943-row L3 inventory by `tools/audit/gen_l3_pass2_sample.py`
(NEW seeds, both recorded, ≠ the pass-1 `20260712`/`20260713`). Sample SELECTION is purely mechanical;
the verdicts are separate hand-authored input (`pass2_reading_verdicts.json` /
`pass2_errorrate_verdicts.json`, keyed by the seed-fixed `process_order`), merged into the final
artifacts — so the generated CSV/JSON is never hand-edited (#17(f)). Re-running is byte-identical
(verified).

- **The independent second reading — `pass2_blind_reading.csv/.json`, seed `20260714`, 116 rows.**
  110 drawn proportional across the five row kinds (literal 55 / branch 29 / field 17 / crosslayer 5 /
  function 4 — the same stratification the L1/L2 pass-2 sampler used; the sixth kind `decl`, 12 rows,
  is reachable via top-up + the error-rate domain) + **6 per-file coverage top-ups so all 22 L3 files
  are represented**. Judged from the code, from scratch, in the shuffled processing order.
- **The error-rate sample — `pass2_blind_errorrate.csv/.json`, seed `20260715`, 40 rows.** Uniform over
  the full 1943-row inventory (all six kinds). Judged blind FIRST; the disagreement vs pass 1 is the
  measured error estimate.

This reader used a deliberately COARSE four-label vocabulary (ESTABLISHED / SURVIVES / PUBLISHED / DEAD)
rather than the full protocol-P2 rubric pass 1 applied (ESTABLISHED/UNFIT/DEAD · NO-ISSUE/SURVIVES/
RETIRES · FORWARD-OK/MIXED-DEFERRED/BACK-EDGE(-NOTE) · PUBLISHED · DEFERRED). The prose per row carries
the finer distinctions (empirical vs structural; forward vs back-edge; control-flow vs survivor-code);
§2 diagnoses the effect of the coarser labels on the raw-agreement number.

## 2. Unblind — comparison + diagnosis (protocol P5)

`tools/audit/pass2_compare_l3.py` joins each of my verdicts to pass 1's disposition on the SAME row
(by file+kind+line+ident) and classifies concordance on the SUBSTANTIVE axis (did either pass flag a
correctness / dead / siloed issue the other missed?), independent of the vocabulary-label difference.
Artifacts: `pass2_compare_reading.csv`, `pass2_compare_errorrate.csv`, `pass2_compare_summary.json`.

| Sample | rows | raw-label agree | substantively concordant | SUBSTANTIVE disagreements |
|---|---|---|---|---|
| reading | 116 | 40 (34.5 %) | **115 (99.1 %)** | **1** |
| error-rate | 40 | 11 (27.5 %) | **40 (100 %)** | **0** |

**Crosstab of the raw-label differences (my_verdict → pass1_verdict), reading sample:**
`ESTABLISHED→ESTABLISHED 30`, `ESTABLISHED→UNFIT 26`, `ESTABLISHED→DEFERRED 3`, `ESTABLISHED→NO-ISSUE 2`;
`SURVIVES→NO-ISSUE 30`, `SURVIVES→SURVIVES 5`, `SURVIVES→BACK-EDGE-NOTE 2`, `SURVIVES→MIXED-DEFERRED 2`,
`SURVIVES→FORWARD-OK 1`; `PUBLISHED→NO-ISSUE 9`, `PUBLISHED→PUBLISHED 5`; `DEAD→ESTABLISHED 1`.

**Every raw-label difference is axis-compatible except one.** The diagnoses:

- **Diagnosis A — the ONE substantive disagreement (reading #16): `extraToneScore`.**
  `keymodeanalyzer.cpp:588` `eval.extraToneScore = 0.0` — I judged **DEAD** (the literal writes
  `CandidateEvaluation::extraToneScore`, a field declared at `:217` and assigned here but **read
  nowhere**, grep-confirmed — a vestigial/dead local field, waste per #6/#12). Pass 1 judged the same
  literal **ESTABLISHED** with the generic constant reason "music-theory table entry / pc arithmetic —
  structural, not a tunable", which does not even fit `= 0.0`. **This contradicts pass-1 report §2's
  claim "zero DEAD constants and zero SILOED/TRAPPED facts among the L3-in-scope rows."**
  *Which protocol step let it through:* P1 + P2. The inventory's FIELDS table enumerates only
  **cross-layer** struct fields, so a dead LOCAL struct field (on the anonymous-namespace
  `CandidateEvaluation`) has no field-row — its only inventory footprint is the `0.0` literal; and
  pass-1's mechanical constant-classifier (`gen_l3_dispositions.py`) bucketed that literal ESTABLISHED
  with a templated reason WITHOUT a consumer-check on the write target. The DT-5 signature ("consumer
  count by grep; 0-1 consumers → flag") was applied to the cross-layer fields inventory, never to local
  fields. **This implies a whole CLASS** — numeric literals that write local struct fields, where the
  field may be dead — **which the Task-3 sweep re-examined** (a new `DT-5_local_dead_field` sub-check;
  §4). The class turned out to hold exactly ONE member (this one). New register row **OI-96** (DT-5).

- **Diagnosis B — the 75 reading + 29 error raw-label differences that are verdict-axis (vocabulary
  granularity), substantively concordant.** These fall in three groups, none a code miss:
  - **`ESTABLISHED→UNFIT` (26 reading / 9 error).** Empirical L3 tunables (mode priors, scale scores,
    disambiguation costs, cadence-anchor weights) I labeled ESTABLISHED; pass 1 labeled UNFIT (an
    empirical hand-set value is not "positively established" per #19). My PROSE explicitly called each
    "empirical" — so the substance matches; only my four-label set lacked the UNFIT bucket.
    *Which step:* P2 on my side — the coarser vocabulary collapsed the structural-vs-empirical split.
  - **`SURVIVES→NO-ISSUE` (30/13), `SURVIVES→{FORWARD-OK, MIXED-DEFERRED, BACK-EDGE-NOTE}` (5/2),
    `PUBLISHED→NO-ISSUE` (9/1), `ESTABLISHED→NO-ISSUE` (2/1), `ESTABLISHED→DEFERRED` (3/3).** Ordinary
    control-flow branches, forward/mixed/back-edge includes, plumbing fields, numeric field defaults,
    and L4-scope constants on the mixed leaf. For every one, both passes conclude "no correctness
    defect"; the label difference is which finer bucket the rubric assigns. The back-edge ones I noted
    as the same dependency pass 1 formalizes as OI-93. *Which step:* P2 vocabulary granularity.
  - This coarse-vocabulary choice is a characteristic of THIS reading, not a repo defect and not a
    pass-1 error; it does not imply any class was judged wrongly (substance is concordant). It is
    recorded here as a process note; a future second pass should use the full P2 rubric labels for a
    directly-diffable comparison. No register row (nothing in the repo is unresolved by it).

Direction check: no row exists where pass 1 flagged a real issue this reader missed. The 2 pass-1
BACK-EDGE + 5 BACK-EDGE-NOTE rows that fell in my sample I noted as the (tracked, OI-93) chord/ pc-util
dependency; the pass-1 RETIRES row (`resolveKeyAndModeRanked`) was not in either sample.

## 3. The measured error rate (protocol P6)

The error-rate sample is 40 rows judged blind FIRST. On the **substantive axis** (deep-verify at the
code: does the row actually have the property claimed?) the two passes are **40/40 concordant = 0/40 =
0.0 % substantive error**. There are **no failing rows** on the substantive axis.

The raw-label disagreement on the 40 is 29/40 (72.5 %), but this is **entirely the vocabulary-
granularity artifact of §2 Diagnosis B** — the crosstab of those 29 is `ESTABLISHED→UNFIT 9`,
`SURVIVES→NO-ISSUE 13`, `ESTABLISHED→DEFERRED 3`, `SURVIVES→{BACK-EDGE-NOTE,FORWARD-OK} 2`,
`ESTABLISHED→NO-ISSUE 1`, `PUBLISHED→NO-ISSUE 1` — zero substantive. The meaningful measured error
estimate is therefore **0/40 substantive**. (The one substantive miss surfaced this pass — the
`extraToneScore` dead field — landed in the READING sample, not the uniform error-rate sample; it is a
waste/hygiene item, not a correctness defect, and defines a class the Task-3 sweep re-examined to
exhaustion.)

Honesty note: this reader's raw agreement (11/40) is much lower than the L1/L2 second reader's (35/40),
solely because this reading used a coarser vocabulary — not because the L3 code disagrees more. The
substantive concordance (100 % on the error sample, 99.1 % on the reading sample) is the like-for-like
figure and is as strong as L1/L2's.

## 4. The full-catalog sweep (protocol P8) — every DT across all 1943 rows

### 4a. Mechanical rules — `gen_signature_sweep.py --layer l3` (one layer-selected instrument)

Per OI-95(a) the sweep tool was **extended with a `--layer` argument** (the `gen_inventory.py --layer`
pattern), NOT forked into a parallel script; `--layer l1l2` reproduces the original L1/L2 sweep with
**identical counts** (DT-2 16 / DT-3 3 / DT-5 8 / DT-12 1 / DT-16 4 / DT-19 4 — verified; the committed
L1/L2 artifacts were left untouched, restored after the verification run). The L3 run fails loudly if
any rule cannot run (none did). Reproducible (byte-identical on re-run). Hit tables:
`tools/audit/l3/sweep_results.{json,txt}`.

| DT | plain rule | L3 hits | verdict |
|---|---|---|---|
| **DT-2** unestablished / not-in-manifest constant | config-struct members (`*Preferences`/`*Preset`/`*Weights`) + named `k*` consts, none in `param_manifest.json` | **122** | **reproduces OI-91** — the whole L3 emission surface is un-inventoried. (~7 of the 122 are non-numeric: `ChordAnalyzerPreferences` enums/`useX` TODO bools/`ignoreDeclaredMode` toggle/`ModePriorPreset::name` — L4/config, not L3 tunables; the ~115 rest are the OI-91 tunables.) No new row. |
| **DT-19** layer-boundary upward include | L3/L3-MIXED include of a chord(L4)/function(L5) header | **18** | **reproduces OI-93** — the 2 heavy back-edges (`cadencekeyanchor.h`/`jointkeydecision.h` → `chordanalyzer.h`) + 5 pc-util silos (`analysisutils.h`) in PURE-L3 files, plus 11 expected orchestrator/DTO includes in L3-MIXED files (annotated). Caveat: the rule is directory-based, so `sectioncadencedetection.cpp:41`→`sparsechordrefinement.h` (target_area `region`, but content re-tagged L4 per OI-90) is not flagged — a DT-21 tooling note. No new row. |
| **DT-5** siloed / dormant symbol (0-1 external consumers) | L3 public symbols | **7** | 2 genuinely 0-consumer = **dormant BY DESIGN** (`decodeLattice` test-only; `setJointKeyWiringEnabled` J-key-iii gated OFF) — the pass-1 P4 characterization; 5 are correctly single-consumed live helpers (not siloed). No new siloed FACT. |
| **DT-5 (local)** dead LOCAL struct field (assigned, never read in its TU) | structs defined in L3 `.cpp` | **1** | **`CandidateEvaluation::extraToneScore`** (2 occurrences, 2 writes, 0 reads) — the class re-examination from §2 Diagnosis A. Exactly ONE member. New row **OI-96** (DT-5). |
| **DT-3** value-copied constant (agree by comment, not by reference) | comment couples a literal to a named symbol | **4** | 3 are heuristic false-positives (annotation comments "1 = downbeat" / "== hypothesis tonic" — not couplings). **1 real:** `analysistypes.h:788` `relativeKeyHysteresisMargin = 2.0` value-copies `hysteresisMargin = 2.0` (comment "= hysteresisMargin by default") — a documented soft-coupling. New row **OI-97** (DT-3, low). |
| **DT-16** raw-DOM interpretation outside L1 | L3 function walking engraving-DOM notes | **1** | **`partialSignatureCorrection` (`keyresolver.cpp:107`)** walks `s->cr` / `toChord(cr)->notes()` / `n->ppitch()` directly to build the signature-scoped pitch histogram, bypassing the L1 NoteModel. Pass 1 did not flag it. New row **OI-98** (DT-16, low-med). |
| **DT-12** stale anchor / dangling reference | `.md` refs + `file:line` anchors in L3 comments | **3** | 1 false-positive (`keymodeanalyzer.cpp:762` anchor is accurate — 762-767 bracket the sigmoid; heuristic mis-matched a word). **2 real (same ref):** `regionanalyzer.cpp:534` + `:815` cite `cowork_phase5c_step4_report.md`, which **does not exist** (not tracked, not gitignored) — a dangling doc-reference (#10). New row **OI-99** (DT-12, low). |

### 4b. Review-signature rules — row-by-row against the inventory

Applied by inspection over the 1943 rows / the 22 files (not mechanical). Rows/files checked per entry;
every hit recorded.

| DT | checked | result |
|---|---|---|
| DT-1 unverified causal premise carrying load | the emission-scoring premises + the D-L3a calibration claim | none — the scoring is music-theory tables + `[empirical]`-labeled weights (not asserted as fact); the "margin 2.8-3.1× better calibrated" claim is MEASURED (`cc_c1_reliability_report`). |
| DT-4 silent overwrite of a committed field | every post-commit mutation site (`applyJointKeyWiring` region.keyModeResult; `populateEmissionConfidence` chosen.normalizedConfidence) | none — the J-key path re-derives the `keyAlternatives` carry ALONGSIDE the override (PIN #2, carries not clobbers) and is gated OFF; `populateEmissionConfidence` writes the documented emission-scale side-effect and keeps the sequence margin on `.confidence` separately. |
| DT-6 duplicated derivation | pc-normalization / collection-fraction / diatonic-degree shapes | none new — the pc primitives are single-sourced via `analysisutils.h`; the mode-prior duplication is the tracked DT-3 OI-63 (sync-guarded). |
| DT-7 never-fires / always-fires | pass-1 `firerate.json` (352/352 decode; dormant machinery 0) | no defect — the 0-fire mechanisms are gated OFF BY DESIGN (correct for the build phase); the live decoder fires on every piece. |
| DT-8 scale-incommensurable comparison | every confidence-like quantity | none new — the emission-sigmoid vs sequence-margin scale split IS the tracked D-L3a / OI-75. |
| DT-9 unvalidated proxy→target | the reach-back "settled key in view" proxy | none — the premature-stopping proxy was already caught and REPLACED by the direct leading-edge-settled criterion (`regionanalyzer.cpp:651-657`). |
| DT-10 one-sided insulation claim | the no-circularity claims (jointkeydecision / localmodulationdetector) | none — enforced STRUCTURALLY (the input type physically cannot carry a resolved key). |
| DT-11 hand-transcribed measurement | this report's figures | none — every figure comes from a generated artifact (`pass2_compare_summary.json`, `sweep_results.json`, pass-1 `firerate.json`). |
| DT-13 interim exception without a retirement condition | the dormant mechanisms + the class-(a) exception | none new — each dormant build names its wiring condition (J-key-iii / 4d-ii); class-(a) is OI-20. |
| DT-14 gate/precondition mismatch (PC-1 shape) | the 0.8 `kAnnotateKeyConfidenceThreshold` gate | no new defect — the gate reads the emission sigmoid (the tracked D-L3a/OI-75 stance); its per-region pass-rate was not aggregated by pass 1 (flagged there, not silently skipped). |
| DT-15 abstention/coverage-movable metric | the "uncertain" flag / abstention | none new — tracked at OI-28 (uncertaintyMargin) / OI-33 (abstain-aware stop). |
| DT-17 silently-truncating capability | reach-back / redecodeRange / mid-piece key-sig re-anchor | none — reach-back + redecodeRange are DECLARED dormancy (gated / test-only); the mid-piece re-anchor is the DOCUMENTED deferral OI-94(a), not a silent truncation. |
| DT-18 plumbing-commit / working-tree desync | this session's commits | none — the Task-1 freeze is an ordinary commit; `git status` verified clean (disk == HEAD) immediately after. |
| DT-20 self-defeating instruction composition | THIS instruction's required reads vs its blinding | none — the instruction deliberately DEFERRED the mandatory `OPEN_ITEMS.md` read to Task 2 to avoid the exact L1/L2 leak (DT-20). The blinding held (§0). |
| DT-21 layer mis-attribution in the tag table | re-verified every L3 file tag at the code | no NEW mis-tag — pass-1's OI-90 re-tags (`chordpathdecoder.h`, `sparsechordrefinement` → L4) are correct; the only residue is the DT-19-sweep directory-based caveat above (OI-90 territory). |

## 5. Register + type promotion (Task 5, at unblind)

Four new rows, each its own issue; pass-1 rows referenced, not duplicated. **No new problem TYPE** — every
finding maps to an existing catalog entry, so `DEFECT_TYPES.md` is unchanged (the `DT-5_local_dead_field`
sub-check is a mechanical EXTENSION of DT-5's existing "0-1 consumers → flag" signature to local struct
fields, documented in the sweep script + here, not a new type).

| Finding | Register | Type | Correctness? |
|---|---|---|---|
| `extraToneScore` dead local field (contradicts pass-1 §2 "zero DEAD") | **OI-96 (new)** | DT-5 | no — waste/hygiene |
| `relativeKeyHysteresisMargin`=`hysteresisMargin` documented soft value-copy | **OI-97 (new)** | DT-3 | no — latent fitter caveat |
| `partialSignatureCorrection` raw-DOM walk outside L1 | **OI-98 (new)** | DT-16 | no — layering/dup smell (functionally correct) |
| `cowork_phase5c_step4_report.md` dangling md-ref ×2 | **OI-99 (new)** | DT-12 | no — doc-sync (#10) |
| OI-91 (DT-2 122) / OI-93 (DT-19 18) / OI-75 / OI-94 / OI-20 / OI-28 / OI-33 | referenced (pass 1) | — | reproduced independently |
| OI-95(a) sweep-tool unification | **discharged** — `gen_signature_sweep.py --layer` | — | — |

## 6. Certification proposal (Task 4)

**Both passes are complete** (pass 1 blind enumerative P1-P4; pass 2 blind second reading P5, sweep P8,
error rate P6). **The error rate is measured on blind-first verdicts** (0/40 substantive; 100 %
substantive concordance on the error sample, 99.1 % on the 116-row reading). **Every disagreement is
diagnosed** (§2): one substantive miss — `extraToneScore`, a dead field caught by this second reading,
a hygiene item now registered (OI-96) and its class swept to exhaustion (exactly one member); all other
disagreements are vocabulary-granularity, substance-concordant. **The sweep found no untracked
correctness defect** — the four new findings (OI-96/97/98/99) are all hygiene / layering / doc-sync;
DT-2 and DT-19 reproduce the tracked OI-91/OI-93 independently; the review DTs surfaced nothing new.

The L3 key/mode inference spine reproduces its documented design: the live sequence decoder + emission
scorer are music-theory-grounded and clean, the confirmed-modulation / joint-key machinery is correctly
gated OFF, and the layering is forward-only except the tracked chord/ back-edges. **No #3 surprise** —
every finding is a known class or a documented deferral.

**Proposal: CERTIFY the surviving Layer-3 (key/mode) spine — proposed, awaiting the user's decision.**
It rests on: both passes complete; a blind-first-measured 0/40-substantive error rate; every
disagreement diagnosed; the full catalog swept with zero untracked correctness defect. Cowork verifies
this report against the code; the user decides. This report does **not** mark the audit plan (OI-84) or
the entry gate (EG-7) satisfied — those are the user's; the status is written everywhere as **"proposed,
awaiting the user's decision."**

## 7. Instrument-establishment (#19) + self-check

- **Sampler** (`gen_l3_pass2_sample.py`): deterministic (stable sort + fixed seeds), byte-identical on
  re-run; SELECTION separated from authored verdicts so the generated artifact is never hand-edited;
  fails loudly on inventory drift (expects 1943 rows).
- **Comparison** (`pass2_compare_l3.py`): the concordance table is explicit and inspectable; the
  crosstab prints every (my_verdict → pass1_verdict) pair so no disagreement is hidden inside an
  aggregate.
- **Sweep** (`gen_signature_sweep.py --layer l3`): reproduces the L1/L2 counts under `--layer l1l2`
  (establishes the refactor is substance-preserving), fails loudly per rule, byte-identical on re-run;
  the DT-3/DT-12 heuristic false-positives are called out per hit rather than averaged away.
- **Self-check of this session's diffs** (the CLAUDE.md rule): the touched files are the three read-only
  audit scripts, their generated artifacts, this report, and the register/STATUS/handoff docs. No
  `src/composing/` file, no constant, no golden, no reference artifact changed. The committed L1/L2
  sweep artifacts were restored after the verification run (not mine to alter). Verdicts/reasons read
  against the guiding principles, the conventions (no self-invented labels — `reading`/`error-rate`/
  `process_order`/DT names all mirror the existing L1/L2 pass-2 + catalog vocabulary), and the gate
  policies.

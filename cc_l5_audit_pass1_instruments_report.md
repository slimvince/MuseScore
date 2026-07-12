# CC — Layer-5 + instruments audit, PASS 1, partition-2a (the regression-stop-core instruments) — EG-7 / OI-84 / OI-116

> **Session 2 of 3 of the L5+instruments first pass (register row OI-116).** This session
> covers the PYTHON MEASUREMENT INSTRUMENTS population. Per the Task-0.3 feasibility rule the
> 1,687-row instrument population was **split** (user-ratified this session): this artifact
> covers the **regression-stop core (7 files / 954 rows)**; the grading+fitting half
> (6 files / 733 rows) is deferred to a follow-up session (register row below). Blind
> enumerative pass (protocol P1–P4). **Certification is NOT decided here.**
>
> HEAD at audit: `dc2d564f9e`. Corpus hash: `c50002fee1`. Inventory: `tools/audit/l5/`
> (`gen_inventory.py`, committed `0382c3275e`).

## 0. Scope, split, and method

The INSTRUMENT population is 13 Python files / 1,687 deep inventory rows (functions +
numeric literals + branches + fields + I/O + cross-layer, from `tools/audit/l5/l5_*.csv`).
The dormant-resolver session-1 processed 815 rows; 1,687 is ~2× that, and the partition
artifact (`pass1_partition.json`, committed by Cowork at `0382c3275e`) itself flags "1687
rows may itself need a two-way sub-split." Every-row rigor for 1,687 rows **plus** 13
establishment tables, the contract-direction check, running the regression-stop pair, and
the report cannot be done in one session without thinning verdicts (Task 0.3 / guiding
principles forbid thinning). Per Task 0.3 the counts were stated and a split proposed; the
user ratified **regression-stop core now**.

| sub-population | files | rows | this session |
|---|---|---|---|
| regression-stop core | compare_analyses, dcml_parser, compare_rn, characterise_bir_false, a8_rebaseline_measure, robust_stop_diff, run_bach_preset | **954** | ✅ AUDITED |
| grading + fitting | analyze_inversion_errors, music21_batch, oracle_root_metric, calibration_fit, c1_reliability, stage5_fit_driver | 733 | ⏸ DEFERRED (register row) |

Per-file deep-row counts (verified against the l5 tables): compare_analyses 244, compare_rn
221, dcml_parser 164, a8_rebaseline_measure 113, run_bach_preset 106, characterise_bir_false
71, robust_stop_diff 35 = **954**.

**Method.** Every one of the 954 rows read at the code and given a closed-set verdict
(P2: premises FACT/THEORY/ASSUMPTION; derived facts PUBLISHED/SILOED/TRAPPED/DUPLICATED;
constants ESTABLISHED/UNFIT/DEAD; code SURVIVES/RETIRES). For instruments the P2 questions
take the **establishment** form (principle 19): what does each instrument claim to measure;
what oracle/derivation validates it; what is stamped; what fails silently. Contract direction
(P3) run from `CLAUDE.md`'s gate blocks + `tools/REPRODUCIBILITY.md`. Behavioral
characterization (P4) = running the instruments read-only against their committed reference.

Row disposition artifact: `tools/audit/l5/pass1_dispositions_instruments_core.csv` /
`.json` (954 inventory rows + 7 synthetic auditor rows for negative-space findings the
mechanical ast inventory did not surface = 961 rows).

## 1. Task-2 headline — the regression stop PASSES CLEAN at HEAD (highest-rank result)

Task 2 requires the regression-stop pair to PASS clean on the current head; a failure would
be "the highest-rank finding this audit can produce." It **passes, byte-identically**:

```
python tools/a8_rebaseline_measure.py --out-dir <scratch>        # reads tools/corpus + WiR READ-ONLY
  [baroque] validated grid==oracle OK; grid_b_cells=7882   (reference manifest: 7882) ✓
  [jazz]    validated grid==oracle OK; grid_b_cells=8099   (reference manifest: 8099) ✓
  [default] validated grid==oracle OK; grid_b_cells=7904   (reference manifest: 7904) ✓
python tools/robust_stop_diff.py --candidate <scratch>           # vs committed tools/robust_stop/
  === baroque === class-(b) dur ref=2932400 cand=2932400 delta=+0 -> PASS ; runs +0/-0
  === jazz    === class-(b) dur ref=2997520 cand=2997520 delta=+0 -> PASS ; runs +0/-0
  === default === class-(b) dur ref=2936000 cand=2936000 delta=+0 -> PASS ; runs +0/-0
  OVERALL: PASS   (exit 0)
```

- a8's per-piece **self-validation assertion** (variant-(b) decomposition byte-identical to
  the pinned `compare_rn.grid_score_regions()`) held on all 326×3 covered pieces.
- The reference was generated at head `443e79dabd` / a8 commit `c2914884af`; the reproduce
  at HEAD `dc2d564f9e` is byte-identical (run set-diff +0/-0), so nothing in the instrument
  chain or its inputs drifted.
- `characterise_bir_false.py` (the batch-stop diagnostic): `validate_corpus_dir` PASSED on all
  three committed corpora (352/352, git `c50002fee1`); BIR=false = **52 / 24 / 52** (matches
  the CLAUDE.md ratified sets exactly).
- `compare_rn.py --wir-bach ... --granularity-robust` reproduced the committed grid
  (exact=2718400, root_err=3038960, key_disagree=1305480, coverage 326/352) exactly.

**No highest-rank stop-and-report finding.** The regression stop is live, reproducible, and
self-validating at HEAD.

## 2. Disposition summary per verdict class (954 inventory rows + 7 synthetic)

| verdict | count | meaning here |
|---|---:|---|
| SURVIVES | 866 | live control-flow / library / I/O / field / import rows on the measurement path |
| FACT | 72 | pitch-class / diatonic-degree / modular-interval constants (music theory), incl. TICKS-basis arithmetic |
| RETIRES | 11 | dead code: `parse_dcml_file` + `find_dcml_file` and their 9 contained branches |
| UNFIT | 5 | hand-set measurement tolerances lacking independent establishment (0.5 ×3, 4/4 ×2) |
| ESTABLISHED | 3 | documented+verified measurement constants (TICKS_PER_QUARTER 480/480.0; advisory 9600) |
| PUBLISHED | 4 | DcmlRegion additive oracle fields — declared-dormant (consumer named), not waste |
| (synthetic) | 7 | auditor rows for findings the mechanical ast inventory did not emit a row for |

No row was SILOED / TRAPPED / DUPLICATED-as-a-verdict at row level (the note→pc duplication is
recorded as finding F9); no premise rows arise (instruments carry no inference premises). No
UNFIT constant is inference-affecting in the production sense, so the `param_manifest.json`
presence check does not apply — these are measurement tolerances, not scorer constants
(confirmed: `param_manifest.json` covers only chordanalyzer/analysistypes/harmonicfunctionlayer/
postscoringgates constants, none of the instrument internals).

## 3. Every flagged row (18 findings, F1–F18) — file:line + one sentence

Each finding has an `OPEN_ITEMS.md` row opened in the report commit (Task 4). F1/F2 are the
only ones that are code to delete; F14/F15/F16 + the two contract gaps in §5 are the
first-rank establishment findings for this scope.

- **F1 — `dcml_parser.py:76` `parse_dcml_file` — RETIRES (dead + #6).** The old DCML-TSV
  parser has no live consumer (referenced only in its own docstring example); it is
  superseded by `parse_abc_harmonies_file` and still carries the pre-P0 bare
  `except (ValueError,KeyError): continue` silent-drop pattern (:108). Two parsers, one concern.
- **F2 — `dcml_parser.py:475` `find_dcml_file` — RETIRES (dead).** Zero references anywhere in
  the repo; TSV lookup is `compare_rn._find_tsv`, WiR lookup is `find_wir_file`. Waste.
- **F3 — `dcml_parser.py:189` broad `except Exception: return None` in `_compute_root_pc`.** A
  systematic numeral mis-parse returns `root_pc=None` (region reads as "no GT root"), silently
  reducing GT root coverage rather than surfacing.
- **F4 — `dcml_parser.py:451` broad `except Exception: return globalkey` in `_resolve_dcml_key`.**
  Any key-resolution error silently falls back to the global key (wrong local tonic → wrong
  `root_pc` downstream), unlogged.
- **F5 — `compare_analyses.py:216, :516, :549` the `0.5` alignment overlap tolerance — UNFIT.**
  The core region-alignment measurement decision (lenient-OR ≥50% of *either* duration);
  rationale documented, value hand-set (not derived/oracle-established). Governs the
  batch-stop, the secondary metric, and the oracle-root metric alignment (NOT the robust grid,
  which unions boundaries and needs no overlap threshold).
- **F6 — `compare_analyses.py:449, :453` the `4 * tpb` hardcoded 4-beats-per-measure
  assumption — UNFIT.** In `_dcml_tick_for`'s extrapolation-beyond-anchors fallback; a silent
  approximation for non-4/4 meters on the WiR/rntxt alignment path (the path lacking `abs_tick`).
- **F7 — `compare_analyses.py:128` `_QUALITY_NORMALISE` completeness.** A quality string not in
  the map passes through unnormalised, so an unmapped variant could produce a false quality
  (dis)agreement; completeness not proven against both producers' full quality vocabularies.
- **F8 — `compare_analyses.py:99` `root_pc` default `-1` sentinel.** Two regions both missing a
  root compare equal (`-1 == -1`) in `_roots_match` → a false chord agreement (the two-way
  region compare only; `three_way_classify` guards on `None`).
- **F9 — note-name→pitch-class mapping DUPLICATED 3×.** `dcml_parser._NOTE_TO_PC` (:124),
  `compare_rn._KB_NOTE_DCML` (:222), `_KB_NOTE_OURS` (:223). One concern (#6) in three copies;
  the `_KB_` pair is a declared verbatim port of `key_confound.py`, still un-unified.
- **F10 — `compare_rn.py:514, :655` bare `except Exception: return None` → silent whole-piece
  drop.** `score_piece` / `grid_score_piece_tsv` drop a corrupt piece from the aggregate with
  no skip counter (unlike `dcml_parser`'s skipped-collector); a systematically failing piece
  silently shrinks the denominator.
- **F11 — `compare_rn.py:120` `normalise_rn` strips ALL parenthetical figures on both sides.**
  A DCML `V(b9)` vs ours `V` scores `exact`; documented leniency but it can mask a real
  extension difference in the exact/partial split.
- **F12 — `a8_rebaseline_measure.py:290` corrupt `.ours.json` folded into the `no_wir` count.**
  `except Exception: continue` conflates a parse-failure with a no-WiR-annotation; the gate
  denominator loses the score with no distinct "corrupt" accounting.
- **F13 — `a8_rebaseline_measure.py:97` `cell_class` split has no independent second
  implementation.** The class-(a)/(b) split — the hard-stop-governing quantity — is a pure
  pc-set test; it inherits the RN-bucket self-validation transitively (validated cell
  membership) but is not itself cross-checked by a second implementation. (A missing
  `pitchClassSet` → class 'b', the conservative/safe direction.)
- **F14 — `characterise_bir_false.py:50` `validate_corpus_dir` fingerprints `.ours.json`
  ONLY, not the paired `.music21.json` ground truth.** A stale/foreign music21 export passes
  the contamination gate undetected — yet a8's variant-(a) genuine filter and this tool's BIR
  gate read `.music21.json`. **Establishment gap in the corpus-integrity guard.**
- **F15 — `run_bach_preset.py:77` `_write_manifest` records only `.ours.json` fingerprints;
  `music21_version` is copy-through informational ("NOT enforced").** Root cause of F14: the
  manifest carries no `.music21.json` fingerprint, so the GT half is unverifiable at measure
  time.
- **F16 — `robust_stop_diff.py:90` `ref_class_durs` reads the reference baseline from the
  re-keyed `manifest.json`, not the sibling `summary.json`.** The candidate reads
  `summary.json` (a8's direct output); the reference reads a separately-assembled
  `manifest.json` (R10-a step). No cross-check of the manifest figure vs the run-enumeration it
  ships beside; a partial re-baseline of one artifact but not the other compares against a
  stale baseline silently. (Verified byte-consistent TODAY: manifest `class_b_root_disagree_dur`
  = a8 `summary.json` `b_cls_b_dur` exactly, all three presets.)
- **F17 — `run_bach_preset.py:206` subprocess `timeout=120s` per score.** A score exceeding it
  → FAILED → `complete=False` → fail-loud exit (not silent). Hardcoded per-score wall; noted,
  not a defect.
- **F18 — `run_bach_preset.py:68` `_detect_music21_version` reads only the first 4000 chars.**
  If `<software>` is beyond that, returns `None` silently; informational only — minor.

Inventory note (audit tool, not an instrument defect): `gen_inventory.py`'s cross-layer
extraction mis-resolves `run_bach_preset.py:198 import platform` (stdlib) to `tools/platform.py`
and tags it `instrument` — a false internal-import resolution. Recorded for the second-pass /
audit-tooling review.

## 4. Per-instrument establishment table (principle 19)

| instrument | claims to measure | establishment record | stamped | silent-failure modes | reproduce-check (this session) |
|---|---|---|---|---|---|
| **dcml_parser.py** | DCML-TSV / WiR-rntxt annotations → `DcmlRegion(root_pc, abs_tick)` | `root_pc` verified vs music21 `roman.RomanNumeral` (0/CC oracle, code comment :174); P0 Fraction-fix recovered 58.9% dropped GT; P4 all-endings col (29 Beethoven repeat mvts); P1 applied-rooting (877/880). Regression tests `tools/tests/test_dcml_parser_*` (INSTRUMENT-TEST, not run here) | TICKS_PER_QUARTER=480 documented+verified; library (no per-run stamp) | F3, F4 broad excepts; F1 dead parser carries pre-P0 bare-except | WiR path exercised transitively (a8/cbf/compare_rn); **TSV path (`parse_abc_harmonies_file`) NOT exercised** in this WiR-only session |
| **compare_analyses.py** | region-level ours-vs-music21 classification + DCML three-way/direct/anchored | alignment=tick-overlap ≥50% (documented lenient-OR); quality via normalization table; RN via degree regex — rationale documented, no oracle on the classifier itself | none (library) | F5 (0.5), F6 (4/4), F7 (quality-map completeness), F8 (-1 sentinel) | exercised transitively by every run; region-count metrics reproduce (cbf 52/24/52) |
| **compare_rn.py** | RN-level ours-vs-DCML + segmentation-invariant duration grid | `grid_score_regions` is the pinned primitive a8 self-validates against byte-identically; `extract_quality`/`normalise` documented (past bugs F-1/F-2 fixed); key parsers ported from `key_confound.py` | grid values live in the reference manifest | F9 (dup), F10 (silent piece drop), F11 (paren leniency) | **CLI run reproduced the committed grid exactly** (exact=2718400 etc.) |
| **characterise_bir_false.py** | genuine BIR=false residual characterization + `validate_corpus_dir` | `validate_corpus_dir` enforces the documented contamination contract (STRONG); BIR gate reproduces 52/24/52 | reads+prints manifest git_hash + counts | F14 (only `.ours.json` fingerprinted) | **RAN ×3: validate PASS (352/352, c50002fee1), BIR 52/24/52** |
| **a8_rebaseline_measure.py** | granularity-robust unit; 3 presets/2 variants/3 respects; failing-run enumerations + class split | **STRONG**: self-validates variant-(b) byte-identical to `grid_score_regions()` per piece (:204); calls `validate_corpus_dir` first; reuses pinned functions | writes `summary.json` (coverage, class durs); reference manifest carries head/corpus/instrument commit | F12 (corrupt→no_wir), F13 (class split not independently cross-checked) | **RAN: "grid==oracle OK" on 326×3; cells match reference exactly** |
| **robust_stop_diff.py** | class-(b) duration non-increase gate + run set-diff | **STRONG**: `parse_runs` fails loudly on format drift (:76); the hard stop is exactly the CLAUDE.md rule | reads the reference manifest (head/corpus provenance) | F16 (reads re-keyed manifest, no cross-check) | **RAN: OVERALL PASS, +0/-0, class-(b) delta +0 all presets** |
| **run_bach_preset.py** | regenerate a per-preset corpus + stamp/validate manifest | clean-slate isolation + fail-loud completeness (expected from `.xml` glob) enforced; per-`.ours.json` sha256 | manifest: preset/git_hash/timestamp/expected/ours_count/complete/music21_version(info)/exe id | F15 (only `.ours.json` fingerprinted), F17 (120s wall, fail-loud), F18 (4000-char version window) | **GENERATOR — cannot run read-only** (regenerates corpus + re-runs analyzer, long, writes near committed corpus); its `validate_corpus_dir` contract verified via the cbf startups passing |

## 5. Contract-direction check (P3) — documented guarantee → enforcing code or absence

From `CLAUDE.md` (blocks A + C gate policy), `tools/REPRODUCIBILITY.md`:

**Enforced (guarantee located in code):**
- G1 class-(b) root-disagree duration NON-INCREASING per preset → `robust_stop_diff.py:118-120,154,158` (`sys.exit`).
- G2 mandatory explained per-run set-diff (added/removed, each with class) → `robust_stop_diff.py:124-153`.
- G3 class-(a) INVESTIGATE flag (`CLASS_A_INVESTIGATE_TICKS=9600`) → `robust_stop_diff.py:47,133-135`.
- G4 a8 self-validates variant-(b) byte-identical to `grid_score_regions()` on every covered piece → `a8:204-210` (AssertionError).
- G5 corpus validation refuses missing/incomplete/contaminated dirs → `validate_corpus_dir` (`characterise_bir_false.py:50-98`).
- G6 the a8 instrument imports `validate_corpus_dir` (guard cannot bit-rot) → `a8:48,250` (shared, no duplication).
- G7 run_bach clean-slates the dir + exits nonzero unless complete (expected derived from `.xml`, not hard-coded) → `run_bach_preset.py:356-360, 375, 516-530`.
- G8 stamps `corpus_manifest.json` per preset → `run_bach_preset._write_manifest`.
- G9 TICKS basis (batch_analyze ticks/480) → shared `TICKS_PER_QUARTER=480`.

**Prose guarantee enforced by NOTHING (first-rank findings for this scope):**
- **U1 (REPRODUCIBILITY C2): `.music21.json` "canonical as-committed; regenerating is a
  deliberate re-baseline of the BIR denominators."** No enforcing code: `validate_corpus_dir`
  does not fingerprint `.music21.json`; `music21_version` is informational. A regenerated /
  foreign / version-mismatched GT half would pass every gate silently. → **F14 + F15.**
- **U2 (CLAUDE.md re-baseline discipline): "the manifest re-stamped with the new corpus
  git_hash" + "snapshot the outgoing reference first (O-12)."** Not enforced by any of the 7
  audited instruments: the gate-read `manifest.json` is assembled by a separate, non-audited
  R10-a step, and `robust_stop_diff` reads its baseline from that manifest without
  cross-checking it against `summary.json` or the run-enumeration it ships beside. → **F16.**

## 6. Blind / post-freeze split

- **Judged BLIND (before the Task-3 freeze):** all 954 inventory rows of the 7 core files +
  the 18 findings + the establishment/contract tables above. No withheld file opened.
- **Post-freeze (Task 3b, appended below after the freeze commit):** the audit's own
  verdict-embodying tooling. **Determination:** the audit's disposition-generating /
  signature-sweep scripts (`gen_resolver_dispositions.py`, `gen_signature_sweep.py`) are NOT in
  the 13-file INSTRUMENT deep-row partition (they live under `tools/audit/`, not the
  inventoried `tools/` measurement chain), so no deep row of THIS session's scope is an
  audit-tooling row. Per the special rule they are still dispositioned post-freeze as a
  clearly-marked section (§8).

## 7. Withheld-file open log

At the time of the freeze draft: **no withheld file has been opened.** Task-4 opens are logged
in §9 after the freeze.

## 8. Post-freeze — audit's own verdict-embodying tooling
*(appended after the Task-3 freeze commit; see §6 determination)*

## 9. Task-4 unblind, reconciliation, and push
*(completed after the freeze)*

# CC Stage 1d report — pin the Python metric scripts (closes Gate 1→2)

**Scope:** `docs/implementation_roadmap.md` Stage 1, item 1.6. Pin the de-facto metric
definitions in `tools/compare_analyses.py`, `tools/characterise_bir_false.py`, and
`tools/compare_rn.py` with known-input/known-output tests.

**Result:** new `tools/tests/test_metric_scripts.py` — **54 tests, all pass**
(`python -m unittest discover -s tools/tests -p "test_*.py"` → `Ran 54 tests … OK`;
direct `python tools/tests/test_metric_scripts.py` also OK). No pytest in the venv
(`python -m pytest --version` → *No module named pytest*; Python 3.14.3) → **unittest**.

**Untouched:** the three scripts under test + `dcml_parser.py` have **zero git diff**.
The C++ production binary and `tools/corpus/` are untouched (no build run). Only
`tools/tests/**` is added.

Every claim below is tagged **[code]** (verified by reading the source) or **[probe]**
(verified by running the function/script and observing output).

---

## 1. Survey — metric definitions as implemented

### 1.1 Entry points & data contracts

- **`compare_analyses.load_analysis(path)`** **[code]** reads `{"regions":[…]}` and maps
  camelCase JSON → snake_case `Region` (`rootPitchClass→root_pc`,
  `bassPitchClass→bass_pc`, `bassIsRoot→bass_is_root`, `noteCount→note_count`,
  `pitchClassSet→pitch_class_set`, `chordScore`, `chordScoreMargin`,
  `keyModeRunnerUp→key_runner_up`, `alternatives`, etc.). Pinned by
  `TestLoadAnalysisContract` against `align/contract.ours.json` **[probe]**.
- **`DcmlRegion`** (`dcml_parser`) **[code]**: `parse_abc_harmonies_file` reads TSV
  columns `mn, mn_onset, globalkey, localkey, relativeroot, chord, numeral`
  (`beat = mn_onset + 1`); `parse_rntxt_file` reads When-in-Rome `m{N} [b{beat}] [Key:]
  Numeral …` lines. **`root_pc` is computed from the `numeral` column resolved in the
  effective key; `chord_symbol` carries the raw `chord` column** — the two can diverge,
  which `compare_rn` relies on. **[probe]** confirmed: `numeral=I @localkey=G → root_pc 7`
  while `chord="I"`.
- **Cross-script reuse** **[code]**: both `characterise_bir_false` and `compare_rn`
  `sys.path.insert` `tools/` and `import compare_analyses as cmp` /
  `import dcml_parser as dcml`. `compare_rn.score_piece` calls
  `cmp.align_dcml_regions(…, mode=cmp.DEFAULT_DCML_MATCH_MODE)`;
  `characterise_bir_false.main` calls `cmp.align_regions`, `cmp.align_dcml_regions`,
  `cmp.classify`, `cmp.three_way_classify`. The alignment comparator is **single-sourced**
  in `compare_analyses`.

### 1.2 The metric definitions

- **Lenient-OR overlap rule** **[code+probe]** (`align_regions` / `_best_dcml_match_by_overlap`):
  for each of OUR regions, pick the other-side region with the **largest tick overlap**;
  aligned iff `overlap/our_dur ≥ 0.5` **OR** `overlap/their_dur ≥ 0.5`. The threshold is
  `≥` (inclusive). Requires `our_dur > 0` and `overlap > 0`. **[probe]** bracket:
  our `[0,100)` vs their `[51,200)` (our 49%, their 33%) → **not** aligned; vs `[50,200)`
  (our exactly 50%) → aligned; vs `[0,49)` (their-side 100% though our-side 49%) →
  aligned (OR clause); multi-candidate → max-overlap wins; zero-length our → never.
- **`three_way_classify(ours,m21,dcml)`** **[code+probe]** by root **pitch class**:
  `all_agree` / `dcml_ours_agree` (m21 wrong) / `music21_dcml_agree` (we wrong) /
  `all_differ`; `no_dcml` if any of the three pc is None. Purely pc-based ⇒ enharmonic
  spellings collapse (DCML `bII`@C → pc 1 = Db≡C#) **[probe]**.
- **BIR=false classification** (`characterise_bir_false.main`) **[code+probe]**: a case is
  a *genuine BIR=false residual* iff `classify(ours,m21).category == 'chord_disagree'`
  **and** `not ours.bassIsRoot` **and** `three_way_classify == 'music21_dcml_agree'`.
  `delta = (our_root − dcml_root + 12) % 12` (positive = our root above DCML;
  `dcml_root = their.root_pc`, equal to wir_pc by the music21_dcml_agree condition).
- **`compare_rn` normalization** **[code+probe]** (`normalise_rn`): strip leading
  `[…]` key-prefix; strip leading `→`/`>` modulation marker; `%`→`ø`; strip parenthetical
  figured-bass `(…)`. Degree-base comparison is **case-sensitive** (case encodes
  major/minor colour).
- **`compare_rn` buckets** (`classify_pair`) **[code+probe]**, root_pc + degree-base +
  full-string + coarse-quality:
  - `exact` — root match, degree-base (case) match, normalised strings equal.
  - `partial` — root + degree-base (case) match, strings differ (inversion/extension);
    also the root-only fallback when either side is unparseable but roots match.
  - `key_disagree` — root match, degree-base differs, **but `extract_quality` coarse
    token matches** (key/mode-context difference, e.g. V→I).
  - `quality_disagree` — root match, degree-base differs, **and coarse token differs**
    (true chord-quality error).
  - `root_err` — root_pc differs (≡ BIR=false fraction).
  - **2026-06-04 split invariant:** `key_disagree + quality_disagree` = the old single
    `quality_err` bucket = #(root match ∧ degree-base differs). Pinned.
- **`extract_quality`** **[code+probe]** coarse token from sigils (`°`,`ø`,`+`), the
  M7/maj7 pattern, and seventh figures `{7,65,43,42,2}`, with case (upper=major) as the
  triad default. See §4 for the suspect parts.

### 1.3 Unknowns / not fully established

- **"24" in the "24/13" headline:** `characterise_bir_false.py` prints **only** the
  BIR=*false* residual count (`TOTAL genuine BIR=false: 13` on the real corpus **[probe]**,
  matching the baseline). It does **not** compute the BIR=*true* `24`. So the memory note
  "24/13 headline = characterise_bir_false.py" is imprecise — this script emits the `13`;
  the `24` is not produced here and its source was not established in this run. The test
  pins what the script *actually* computes (the residual count + delta).
- **WiR file discovery** (`dcml.find_wir_file`/`_build_wir_index`) requires a real
  When-in-Rome repo tree (`Corpus/Early_Choral/…/remote.json`). The characterise test
  **stubs** `find_wir_file` (see NOT-PINNED, §3); the WiR *parser* and the
  classification+delta code run for real.

---

## 2. Fixture derivations (by hand)

Full tables in `tools/tests/fixtures/README.md`. Summary:

- **`rn/probe_rn.*`** (9 regions, 1:1 tick alignment, tpb=480): derived totals
  **matched=9, exact=5, partial=1, key_disagree=1, quality_disagree=1, root_err=1**;
  `root_aligned=9, root_agree=8`, `rn_agree=6`. Sum invariant `key_disagree+quality_disagree=2`.
  Beat 3 (`V` vs `I`@G, both pc 7) is the **V→I regression pin** (root_agree=True yet
  key_disagree, not quality error). Beats 6–9 pin `%`→`ø`, paren-strip, key-prefix-strip,
  modulation-marker-strip respectively.
- **`bir_corpus/probe01.*`** (4 regions): R0 → counted BIR=false (delta=7); R1 →
  excluded by `bassIsRoot=True` (the "BIR=true" exclusion); R2 → excluded
  (`dcml_ours_agree`, we're right); R3 → excluded (`full_agree`, pc1=Db enharmonic point).
  Derived **TOTAL=1, histogram {7:1}**.
- **`align/contract.ours.json`** (1 region): JSON→dataclass field-mapping contract.

---

## 3. Test inventory & NOT-PINNED

**Pinned (54 tests):**
- `TestAlignRegions` (8) — lenient-OR 50% bracket both sides, containment, multi-candidate,
  zero-length, no-overlap, empty.
- `TestClassify` (5) — full_agree / rn_differs / chord_disagree / near_agree / unaligned.
- `TestThreeWayClassify` (7) — all four buckets + no_dcml cases + enharmonic pc-collapse.
- `TestAlignDcmlRegions` (3) — time-overlap 1:1, sub-beat containment, beat-snap legacy.
- `TestCompareRnNormalisation` (5) + `TestExtractQuality` (7) + `TestClassifyPair` (8).
- `TestScorePiece` (6) — bucket counts, partition, split sum invariant, root parity,
  determinism.
- `TestLoadAnalysisContract` (2).
- `TestCharacteriseBirFalse` (3) — `main()` on the fixture corpus → TOTAL=1, delta hist,
  processed/coverage line.

**NOT-PINNED (with reasons):**
1. **WiR discovery** `dcml.find_wir_file` / `_build_wir_index` — needs a real
   When-in-Rome repo dir tree (`remote.json` index). Replicating it is impractical and
   it is pure file-system plumbing, not a metric definition; the test stubs it so the
   metric code (parse + classify + delta) is still exercised on real WiR rntxt.
2. **`compare_rn` cross-corpus orchestration** (`discover_corpora`, `--cross-corpus`,
   `CROSS_CORPORA` globs) and **CLI `main()`** — orchestration over real corpus dirs, not
   a metric definition.
3. **Presentation** — `compare_analyses.print_report`, `render_html_fragment`, and the
   `compare_rn`/`characterise` human dump formatting — display only, no metric content.
   (The characterise test asserts on key summary lines, which incidentally covers the
   count-printing path.)

---

## 4. Findings — suspect behavior pinned as-is (metric **decision-items**, not fixed)

> Per the Stage-1d hard constraint, these are pinned with
> `# pins current (suspect) behavior` and reported here. **Changing them re-baselines a
> metric and must be an explicit decision**, not a drive-by fix.

- **F-1 (real, exercised) — letter `o` diminished is not recognized by
  `extract_quality`.** The diminished branch keys off `°` (U+00B0), but **both DCML and
  our analyzer emit the letter `o`** (`viio6`, `iio7`; confirmed in
  `corelli/.../op01n01a.harmonies.tsv` and in `tools/corpus/*.ours.json` **[probe]**).
  So `extract_quality('viio6') == 'Min'` and `'viio7' == 'Min7'` — diminished triads/7ths
  are coarse-classified Min/Min7, and the `°` branch is effectively dead for the corpus.
  Effect is **symmetric** (both sides use `o`), so dim-vs-dim still buckets consistently;
  the loss is the dim-vs-minor distinction inside the disagreement bucket (a true
  dim/min quality error can be mislabelled `key_disagree`). Pinned in
  `TestExtractQuality.test_letter_o_diminished_is_NOT_recognised`.
- **F-2 (minor) — augmented-sixth / Neapolitan tokens.** `extract_quality('Ger65')` and
  `'N6'` → `'?'` (no accepted degree token), while **`'It6'` matches degree `I` and is
  mis-read as a major tonic (`'Maj'`)** **[probe]**. In `classify_pair`, a `?`/unparseable
  side falls back to root-only (→ `partial`/`root_err`). Pinned in
  `TestExtractQuality.test_augmented_sixth_and_neapolitan_unparseable` /
  `TestClassifyPair.test_unparseable_falls_back_to_root_only`.
- **F-3 (note, not a bug) — `characterise_bir_false` prints only the `13`.** See §1.3.
  The "24" (BIR=true) is not computed by this script. Recommend correcting the
  memory/handoff wording ("24/13 headline = characterise_bir_false.py") to "the `13`
  (BIR=false residual count) comes from characterise_bir_false.py".

No case was found where a script **miscounts on a hand-derived fixture** (the Stage-1d
stop condition) — every derived count matched the script output. F-1/F-2 are
definitional quirks of `extract_quality`, faithfully reproduced, not arithmetic errors.

**Non-vacuousness check [probe]:** monkeypatching `extract_quality` so the two sides
diverge flips the V→I pin from `key_disagree` to `quality_disagree` and the test **fails**
(1 failure) — the suite binds to the real classifier, not to a tautology.

---

## 5. Proposed `build_and_test.md` line (text only — NOT applied this run)

> **Python metric-script tests** (Stage 1d — pins the BIR / root_agree / rn_agree metric
> definitions). No pytest in the venv; use unittest:
> ```
> cd C:\s\MS && python -m unittest discover -s tools/tests -p "test_*.py"
> ```
> Expected: `Ran 54 tests … OK`. These must pass after any change to
> `tools/compare_analyses.py`, `tools/characterise_bir_false.py`, `tools/compare_rn.py`,
> or `tools/dcml_parser.py`; a failure means a metric definition changed and every
> baseline that depends on it must be re-derived.

---

## 6. Counts + single-commit proposal (awaiting Cowork confirmation)

- New files (all under `tools/tests/`): `test_metric_scripts.py` (54 tests),
  `fixtures/README.md`, `fixtures/rn/probe_rn.ours.json`,
  `fixtures/rn/probe_rn.harmonies.tsv`, `fixtures/bir_corpus/probe01.ours.json`,
  `fixtures/bir_corpus/probe01.music21.json`, `fixtures/bir_corpus/probe01.wir.txt`,
  `fixtures/align/contract.ours.json`.
- Scripts under test: **0 changes** (verified by `git diff --stat`).
- Real-corpus sanity **[probe]**: `python tools/characterise_bir_false.py` →
  `13 genuine BIR=false cases` (matches the documented Baroque BIR=false=13 baseline).

Proposed commit (tools/tests/** only):

```
test: pin the Python metric-script definitions (Stage 1d)

Known-input/known-output fixtures for align_dcml_regions (lenient-OR
threshold bracket), characterise_bir_false (BIR=true/false/not-counted,
enharmonic root), and compare_rn (all buckets incl. the 2026-06-04
key_disagree/quality_disagree classifier fix, normalization rules,
determinism). The metric definitions every baseline depends on now fail
loudly when changed (implementation_roadmap.md 1.6 — closes Gate 1->2).
Scripts themselves untouched.
```

This closes Gate 1→2 (with the documented 1.3 NOT-PINNED exceptions for the C++
segmentation passes).

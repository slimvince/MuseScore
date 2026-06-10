# Stage 1d metric-script test fixtures — hand derivations

These fixtures pin the **metric definitions** implemented by `tools/compare_analyses.py`,
`tools/characterise_bir_false.py`, and `tools/compare_rn.py`. Every expected count below
is derived by hand and cross-checked against a probe run of the actual functions
(`python tools/...` / direct calls) — never inferred from docstrings alone.

All fixtures use **ticks-per-beat = 480** and **measure 1 anchored at tick 0**, so the
DCML `(measure, beat) → tick` conversion in `compare_analyses._dcml_time_spans`
(`tick = measure_start + (beat-1)*tpb`) is trivial to follow.

---

## `rn/probe_rn.ours.json` + `rn/probe_rn.harmonies.tsv` — `compare_rn.score_piece`

9 regions, all measure 1, beats 1..9 → ticks `(k-1)*480 .. k*480`. The DCML TSV
(`mn_onset = k-1`, so `beat = k`) lands one row per beat, so alignment is 1:1 by exact
tick overlap. Roots: DCML root_pc comes from the **`numeral`** column resolved in the
**`localkey`**; the RN string compared comes from the **`chord`** column.

| beat | ours rn (root) | DCML chord / numeral @ localkey (root) | bucket | why |
|------|----------------|----------------------------------------|--------|-----|
| 1 | `I` (0)   | `I` / `I` @C (0)    | **exact**    | norm equal, root+case match |
| 2 | `I` (0)   | `I6` / `I` @C (0)   | **partial**  | root+degree-case match, inversion differs |
| 3 | `V` (7)   | `I` / `I` @G (7)    | **key_disagree** | root match (7); degree token differs (V vs I) but coarse quality both `Maj` → key/mode-context error, NOT quality error. **2026-06-04 regression pin.** |
| 4 | `V` (7)   | `v` / `i` @G (7)    | **quality_disagree** | root match (7); coarse quality `Maj` vs `Min` differ → true quality error |
| 5 | `ii` (2)  | `V` / `V` @C (7)    | **root_err** | roots 2 ≠ 7 |
| 6 | `iiø65` (2) | `ii%65` / `ii` @C (2) | **exact**  | `%`→`ø` normalization makes strings equal |
| 7 | `V` (7)   | `V(4)` / `V` @C (7) | **exact**    | paren figured-bass `(4)` stripped |
| 8 | `[C:]I` (0) | `I` / `I` @C (0)  | **exact**    | key-prefix `[C:]` stripped |
| 9 | `→V` (7)  | `V` / `V` @C (7)    | **exact**    | modulation marker `→` stripped |

Derived totals: **matched=9, exact=5, partial=1, key_disagree=1, quality_disagree=1,
root_err=1.** Buckets partition `matched` (5+1+1+1+1=9). ✓

**Sum invariant (2026-06-04 fix):** the old single `quality_err` bucket = #(root matches
AND degree token differs) = beats 3 and 4 = **2**. After the fix `key_disagree +
quality_disagree = 1 + 1 = 2`. ✓ (The fix conserves the total while routing the V→I
shape to `key_disagree` instead of mislabelling it a quality error.)

**root_agree vs rn_agree:** `root_aligned=9`; `root_agree=8` (only beat 5 mismatches pc).
`rn_agree = exact + partial = 6`. Beat 3 is the deliberate divergence: `root_agree=True`
yet not rn-exact — root agreement does **not** imply RN agreement.

---

## `bir_corpus/` — `characterise_bir_false.main()`

One synthetic score `probe01` (4 regions, measure 1, beats 1..4). `ours.json` and
`music21.json` align 1:1 by tick. The WiR rntxt (`probe01.wir.txt`,
`m1 C: I b2 V b3 IV b4 bII`) gives DCML roots I=0, V=7, IV=5, bII=1, aligned by the same
`(measure,beat)→tick` conversion.

A case enters the BIR=false residual set **iff** (script lines 95–104):
`classify(ours,music21).category == 'chord_disagree'` **and** `not ours.bassIsRoot`
**and** `three_way_classify(ours,music21,dcml) == 'music21_dcml_agree'`.
`delta = (our_root − dcml_root + 12) % 12`.

| beat | ours root / bassIsRoot | m21 root | DCML root | classify | three-way | counted? |
|------|------------------------|----------|-----------|----------|-----------|----------|
| 1 | 7 / **False** | 0 | 0 | chord_disagree | music21_dcml_agree | **YES — delta=(7−0)=7** |
| 2 | 2 / **True**  | 7 | 7 | chord_disagree | music21_dcml_agree | no — `bassIsRoot` excludes it |
| 3 | 5 / False | 9 | 5 | chord_disagree | dcml_ours_agree | no — we match DCML |
| 4 | 1 / True  | 1 | 1 | full_agree | all_agree | no — not a disagreement |

Derived: **TOTAL genuine BIR=false = 1**, delta histogram **{7: 1}**.

Beat 4 doubles as the **enharmonic/pc point**: DCML `bII` resolves to pc 1 (Db ≡ C#);
the comparison is purely pitch-class based, so the analyzer root_pc 1 agrees regardless
of spelling.

The script's WiR *discovery* (`dcml.find_wir_file` / `_build_wir_index`, which needs a
real When-in-Rome repo tree with `remote.json`) is stubbed in the test; the WiR
*parser* (`parse_rntxt_file`) and the *classification + delta* code run for real.

---

## `align/contract.ours.json` — `compare_analyses.load_analysis`

One region exercising the camelCase-JSON → snake_case-dataclass field mapping
(`rootPitchClass→root_pc`, `bassPitchClass→bass_pc`, `bassIsRoot→bass_is_root`,
`noteCount→note_count`, `pitchClassSet→pitch_class_set`, `chordScore`,
`chordScoreMargin`, `keyModeRunnerUp→key_runner_up`, `alternatives`). This pins the
input contract that all comparators depend on.

---

## Alignment / classify / three_way / extract_quality / classify_pair

These are pinned with **inline-constructed** `Region` / `DcmlRegion` objects in
`test_metric_scripts.py` (no data files needed) — see the per-test docstrings for the
threshold-bracket derivations (`align_regions`: 50% boundary, lenient-OR containment,
multi-candidate max-overlap, zero-length, no-overlap).

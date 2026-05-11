# Iteration 19: Characterize the remaining BIR=true=98 mismatches

## Goal

Pure diagnostic — zero logic changes. Write a Python script that precisely
categorizes all 98 remaining BIR=true mismatches using data already present
in the `.ours.json` corpus files. Produce a structured report for Cowork to
use when designing Iteration 20 gate(s).

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=98, BIR=false=788

---

## Step 2 — Inspect the .ours.json schema before writing code

Read two or three `.ours.json` regions that have both `bassIsRoot=true` and a
non-empty `alternatives` list. Determine definitively:

a. Does `alternatives[0]` duplicate the winner (same `chordSymbol`), or does
   the list start with the first real alternative?
b. Do alternative entries contain `rootPitchClass` / `bassPitchClass` fields,
   or only `chordSymbol` and `score`?
c. Is `chordScoreMargin` the raw score difference (`winner.score − alt.score`),
   or something post-deduction?

Run:
```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```
to confirm the current BIR=true=98 baseline before proceeding.

Report your findings from (a)–(c) before writing any code.

---

## Step 3 — Write `tools/analyze_bir_true_iter19.py`

The script must be self-contained. It may `import` from `tools/compare_analyses.py`
and `tools/dcml_parser.py` (already on sys.path via the existing pattern in
`analyze_inversion_errors.py`). Do not modify those shared modules.

### 3a — Identify BIR=true mismatch regions

Follow the same pattern as `analyze_inversion_errors.py`:
- Load every `*.ours.json` + its matching `*.music21.json` from `tools/corpus/`.
- Align with `cmp.align_regions()`.
- Classify each pair with `cmp.classify()`.
- Collect regions where `result.category == "chord_disagree"` AND
  `our_r.bass_is_root == True`.

Use the three-way `music21_dcml_agree` subset when it contains ≥ 50 cases;
otherwise use the two-way `chord_disagree` set. (This matches the fallback
logic in `analyze_inversion_errors.py`.) Print which set is used and its size.

### 3b — Chord-symbol parser helper

Write `parse_chord_symbol(sym: str) -> tuple[int, int]`:

- Strip a trailing `/Bass` inversion suffix if present; parse that suffix as
  the bass note.
- Parse the root letter + accidental: C=0, D=2, E=4, F=5, G=7, A=9, B=11;
  `#` adds 1, `b` subtracts 1 (mod 12).
- If no `/` suffix, `bassPc = rootPc`.
- Return `(-1, -1)` on any parse failure.

Smoke-test in the script (print results, not assert):
```
parse_chord_symbol("Gm")        → (7, 7)
parse_chord_symbol("Am/C")      → (9, 0)
parse_chord_symbol("F#m7/A")    → (6, 9)
parse_chord_symbol("Bbadd9")    → (10, 10)
parse_chord_symbol("Dm7/Bb")    → (2, 10)
```

### 3c — Per-case extraction

For each BIR=true mismatch region:

1. **Winner** (from the region's own fields):
   - `winner_rootPc` = `rootPitchClass`
   - `winner_bassPc` = `bassPitchClass`
   - `winner_quality` = `quality`
   - `winner_score`  = `chordScore`
   - `stored_margin` = `chordScoreMargin`

2. **Top real alternative** — the first entry in `alternatives` that has a
   different `chordSymbol` from the winner's `chordSymbol`. (Skip duplicates.)
   - `alt_symbol`, `alt_score`
   - `alt_rootPc`, `alt_bassPc` = `parse_chord_symbol(alt_symbol)`
   - `alt_quality` = infer from symbol (reuse `_infer_quality` from
     `analyze_inversion_errors.py` or reimplement inline)
   - `raw_margin` = `winner_score − alt_score`
   - If no distinct alternative exists, mark the case as **Category 4**.

3. **Key info** — parse the `key` field (e.g. `"Gmin"`, `"CMaj"`, `"F#Dor"`):
   - Extract the tonic letter+accidental → `keyTonicPc`
   - Detect mode from suffix: `"min"` → minor (mode 5), `"Maj"` → major (mode 0),
     others → unknown

4. **Derived flags**:
   ```
   alt_root_is_winner_bass  = (alt_rootPc == winner_bassPc)        # Cat 1 signal
   alt_bass_is_winner_bass  = (alt_bassPc == winner_bassPc)        # same bass note
   alt_is_clean             = alt_quality in {"Major", "Minor"}
   ```

5. **Source info**: `file` (stem), `measureNumber`, `beat`

### 3d — Categorize

Assign each case to exactly one category (highest-priority first):

| Cat | Condition | Label |
|-----|-----------|-------|
| 4 | No distinct alternative | No real alt |
| 1 | `alt_root_is_winner_bass == True` | Canonical inversion |
| 2 | `alt_bass_is_winner_bass == True` (but root differs from winner bass) | Same-bass, root shift |
| 3 | Neither of the above | Unrelated alt |

### 3e — Printed report

```
BIR=true mismatch analysis — Iteration 19
Using [three-way / two-way] set, n=N
=========================================

CATEGORY 1 — Canonical inversion (alt rootPc == winner bassPc)
  Count:  N  (X%)
  Winner qualities:  Major=N  Minor=N  MajorAdd6=N  MinorAdd6=N  Other=N
  Alt qualities:     Major=N  Minor=N  Other=N
  Alt is clean (Major/Minor):  N  (X%)
  raw_margin stats:  min=X.XX  median=X.XX  max=X.XX
  raw_margin < 0.50: N  (X%)
  raw_margin < 1.00: N  (X%)
  Examples (up to 5):
    bwvXX.X  m5  beat1  Cmaj → Am/C  margin=+0.42  key=Amin
    ...

CATEGORY 2 — Same bass, alt root unrelated to winner bass
  Count:  N  (X%)
  Winner/alt quality pairs:  (Major→Minor)=N  (Minor→Major)=N  ...
  raw_margin stats:  min=X.XX  median=X.XX  max=X.XX
  Examples (up to 3):
    ...

CATEGORY 3 — Unrelated alternative (no same-bass relationship)
  Count:  N  (X%)
  Examples (up to 3):
    ...

CATEGORY 4 — No real alternative in candidates
  Count:  N  (X%)

=========================================
SUMMARY
  Actionable (Cat 1 + 2):         N  (X%)
  Cat 1 only (cleanest target):   N  (X%)
  Cat 1 with clean alt:           N  (X%)
  Cat 1, clean alt, margin<0.50:  N  (X%)
  Cat 1, clean alt, margin<1.00:  N  (X%)
```

---

## Step 4 — Run the script

```
cd C:\s\MS && python tools/analyze_bir_true_iter19.py
```

Capture the **complete output** verbatim, including the smoke-test lines.

---

## Step 5 — Verify no baseline change

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Confirm BIR=true still equals 98, BIR=false still equals 788.
(The diagnostic script reads files but does not change any analyzer output.)

---

## Step 6 — Report to Cowork

Paste:
1. The Step 2 schema findings (a, b, c) verbatim.
2. The complete Step 4 output verbatim.
3. A 5–10 line interpretation:
   - Which category dominates, and by how much?
   - Is Cat 1 large enough to justify a new gate?
   - Are the raw margins in Cat 1 tight enough that a gate swap would be safe
     (i.e., would a gate cause regressions on BIR=false or test suites)?
   - What additional context (key, beat, quality pair) distinguishes the Cat 1
     cases — could it be a simple "always swap" or does it need conditions?
   - What is your recommended scope for Iteration 20?

Do NOT implement any gate, logic change, or scoring change.
Do NOT commit `analyze_bir_true_iter19.py` — it is a disposable diagnostic.

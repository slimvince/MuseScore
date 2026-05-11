# Iteration 23: Verify what the reference says for Cat 1 Minor→Dim cases

## Goal

Diagnostic only — zero code changes. Before designing any gate for the Cat 1
Minor→Dim cases, verify what the reference (music21 and WiR DCML) actually
says for those chords. We need to know whether the mismatch is:

  (A) Quality-only: reference also has rootPc=E (same root), but quality=Dim
      → switching Em→Edim would fix the BIR=true mismatch
  (B) Root-based: reference has a different rootPc entirely (e.g., C/E first
      inversion) → switching Em→Edim leaves rootPc unchanged and fixes nothing

This matters because the Cat 1 categorization only describes OUR own
candidates (alt.rootPc == winner.rootPc). It says nothing about what the
reference expects. If the reference expects a different root, the entire Cat 1
Minor→Dim gate idea is invalid.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — confirm baselines: BIR=true=71, BIR=false=788

---

## Step 2 — Inspect the classify() function

Read `tools/compare_analyses.py`. Find and report verbatim:
- The `classify()` function (or equivalent): what field(s) does it compare
  to determine `chord_disagree`? rootPc only? rootPc + quality? chordSymbol?
- The `three_way_classify()` function: same question.

This establishes whether chord_disagree can fire on quality-only differences
(same rootPc, different quality) or requires a rootPc mismatch.

---

## Step 3 — Spot-check 6 Cat 1 Minor→Dim cases

For each of the following 6 cases, open the corresponding `tools/corpus/`
files and report what the reference says:

| File        | Measure | Our winner |
|-------------|---------|------------|
| bwv153.9    | 5       | Em         |
| bwv154.3    | 1       | F#m        |
| bwv282      | 12      | Bm         |
| bwv302      | 1       | Em         |
| bwv353      | 8       | Dm         |
| bwv85.6     | 5       | Fm         |

For each case:

**A. music21 reference** — open `tools/corpus/bwvXXX.music21.json` and find
the region at the matching measure/beat. Report:
- `rootPitchClass` (music21's root)
- `chordSymbol` (music21's chord symbol)
- `bassIsRoot` or `bassPitchClass` if present

**B. WiR DCML reference** (if the file exists in `tools/dcml/when_in_rome/`):
- Find the matching RN label using `tools/dcml_parser.py`
- Report the resolved rootPc and the raw RN label

**C. Our winner** (from `tools/corpus/bwvXXX.ours.json`):
- Confirm `rootPitchClass`, `quality`, `bassPitchClass`, `chordSymbol`
- Report the top 2 alternatives with their chordSymbols and scores

---

## Step 4 — Classify the mismatch type for each case

For each spot-check case, label it:

- **TYPE-A (quality mismatch)**: reference rootPc == our rootPc, but quality
  differs. Switching to Edim (same root) would match the reference.
- **TYPE-B (root mismatch)**: reference rootPc ≠ our rootPc. Switching to
  Edim (same root) does NOT help.
- **TYPE-C (ambiguous)**: reference is unclear or rootPc conversion uncertain.

---

## Step 5 — Report to Cowork

Provide:

1. The `classify()` / `three_way_classify()` function verbatim from Step 2.
2. Per-case table (all 6 cases):
   ```
   bwv153.9 m5:
     Ours:    Em  rootPc=4  bass=4
     music21: [chordSymbol]  rootPc=N
     WiR:     [RN label]  rootPc=N
     TYPE:    A / B / C
   ```
3. Summary: how many of the 6 are Type A vs Type B?
4. Extrapolation: if Type A predominates, the quality tiebreaker gate is
   valid and would fix approximately N of the 22 cases. If Type B
   predominates, the Cat 1 Minor→Dim pattern is a categorization artifact and
   does not represent fixable errors via quality switching.

Do NOT implement any gate. Do NOT commit.

# Iteration 34: Genuine-48 extraction, Cat 2 cross-reference, residual Aug investigation

## Background

Iter 33 found that the `analyze_bir_true_iter19.py` script fell back to two-way mode
(n=625) because genuine three-way cases dropped below 50 (now 48). The two-way output
is dominated by Power5→Sus4 (213 Power winners, Cat 1) — a pattern almost certainly
absent from the genuine 48. The category distribution reported in Iter 33 describes
the two-way population, not the genuine errors.

This iteration has four goals, all diagnostic:
1. Clarify exactly what "three-way" means in the script — which sources are required
   to disagree, and whether the human-annotated DCML corpus is mandatory.
2. Fix the script so genuine three-way cases are always extracted and listed explicitly.
3. Cross-reference the two largest Cat 2 two-way patterns (Major→Minor7=49,
   Power→Major=52) against the genuine 48 to see how many genuine cases each covers.
4. Investigate the 3 residual Augmented TYPE-A cases that Gate L missed.

Do NOT implement any gate. Do NOT commit.

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.

---

## Step 0 — Clarify the three-way definition

Read `tools/analyze_bir_true_iter19.py` (or whichever script defines the genuine
error set). Find the exact logic that classifies a region as a "genuine three-way
error" and report:

1. Which sources are compared? Name them exactly as the script uses them
   (e.g. music21, When in Rome, DCML).
2. Is DCML (the human-annotated corpus) **required** to disagree with our output,
   or can the three-way condition fire without DCML?
3. What is the exact boolean condition? e.g.:
   - "all three must disagree with ours" — AND logic
   - "any two of three must disagree" — majority logic
   - "music21 AND DCML must disagree, WiR optional" — weighted
4. Quote the relevant lines from the script verbatim.

This matters because music21 and When in Rome are both automatic analyzers —
they can be wrong. DCML is human-annotated and is the most authoritative source.
A "genuine error" that excludes DCML disagreement is a much weaker signal.

---

## Step 1 — Confirm corpus baseline

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=48, BIR=false=787.

---

## Step 2 — Patch the categorization script

Open `tools/analyze_bir_true_iter19.py`. Find the branch that selects two-way vs
three-way mode. Add a block that **always** extracts and prints the genuine three-way
case list, regardless of which mode the broader analysis uses.

Specifically: before (or after) the existing mode-branch, add a section that:
- Builds the genuine three-way error set (music21 AND WiR/DCML both disagree with ours)
- For each genuine case, runs the same Cat 1 / Cat 2 / Cat 3 / Cat 4 classification
- Prints the full case list in the same format as the existing Cat prints:
  ```
  [GENUINE-CAT1] file=bwvXX  m=N  beat=X  winner=SYMBOL  alt=SYMBOL  margin=+X.XX  key=KEY  winner_q=Q  alt_q=Q
  [GENUINE-CAT2] file=bwvXX  m=N  beat=X  winner=SYMBOL  alt=SYMBOL  margin=+X.XX  key=KEY  winner_q=Q  alt_q=Q
  [GENUINE-CAT3] ...
  [GENUINE-CAT4] ...
  ```
- Prints a summary:
  ```
  GENUINE THREE-WAY CASES (n=48):
    Cat 1: N  winner_qualities: Q=N ...  alt_qualities: Q=N ...
    Cat 2: N  quality_pairs: (WQ→AQ)=N ...
    Cat 3: N
    Cat 4: N
  ```

This section must run regardless of whether the main analysis is in two-way or
three-way mode.

---

## Step 3 — Re-run and report genuine-48 distribution

```
cd C:\s\MS && python tools/analyze_bir_true_iter19.py
```

Report the complete new output verbatim, including both the existing two-way analysis
AND the new genuine three-way section.

---

## Step 4 — Cross-reference Cat 2 patterns against genuine 48

From the genuine-48 case list produced in Step 3, count:

A. How many genuine cases match `(Major→Minor7)` — winner=Major root-position,
   alt=Minor7 in first inversion (same bass, alt.rootPc ≠ winner.rootPc)?
   List each case with its margin and key.

B. How many genuine cases match `(Power→Major)` — winner=Power5 root-position,
   alt=Major (any inversion, same bass)?
   List each case with its margin and key.

C. For the `Major→Minor7` cases: note the I-interval for each
   `(winner.bassPc - alt.rootPc + 12) % 12` — is it consistently I3 (=3)?
   This determines whether Gate J logic (which caused 32 BIR=false regressions)
   is the relevant mechanism, or whether there is a different interval pattern.

**Context**: Cat 2 `Major→Minor7` with I3 interval is exactly Gate J territory.
Gate J was abandoned (Iter 29) because it caused 32 BIR=false regressions for
2 fixes, even with the vi-chord restriction. If the genuine overlap is small (≤5)
the fix/regression ratio may still be unacceptable. Report the count and let
Cowork decide.

---

## Step 5 — Investigate the 3 residual Augmented TYPE-A cases

Gate L fixed 4 of the Augmented→Major TYPE-A cases in Iter 32. Three cases remain
in the genuine set:

| File     | m  | b   | Winner | Alt | Key  |
|----------|----|-----|--------|-----|------|
| bwv345   | 8  | 2.0 | G+     | G   | Gmin |
| bwv407   | 19 | 4.0 | E+     | E   | Dmaj |
| bwv424   | 1  | 4.0 | E+     | E   | Amin |

For each, read the corpus JSON and report:
- The winner chord symbol and score
- The alt chord symbol and score
- The actual margin (`winner.score - alt.score`)
- Whether the alt is present in `alternatives[]` at all
- Which Gate L condition failed (if the alt is present):
  - margin > 0.35f?
  - alt.rootPc ≠ winner.rootPc?
  - alt.bassPc ≠ winner.bassPc?
  - root not diatonic to key?
  - winner has a seventh extension (extension guard blocks it)?

Run this Python script:

```python
import json, re

NOTE_TO_PC = {'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,
              'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}

MAJOR_SCALES = {
    0:[0,2,4,5,7,9,11], 2:[0,2,4,5,7,9,11], 4:[0,2,4,5,7,9,11],
    5:[0,2,4,5,7,9,11], 7:[0,2,4,5,7,9,11], 9:[0,2,4,5,7,9,11],
    11:[0,2,4,5,7,9,11]
}  # simplified — use the key field from JSON instead

def parse_root(sym):
    m = re.match(r'^([A-G][b#]?)', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else -1

def parse_bass(sym):
    m = re.search(r'/([A-G][b#]?)$', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else parse_root(sym)

TARGETS = [
    ('tools/corpus/bwv345.ours.json',  8,  2.0, 'Gmin'),
    ('tools/corpus/bwv407.ours.json',  19, 4.0, 'Dmaj'),
    ('tools/corpus/bwv424.ours.json',  1,  4.0, 'Amin'),
]

for fpath, meas, beat, key_label in TARGETS:
    data = json.load(open(fpath))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            wq   = r.get('quality', '')
            wsym = r.get('chordSymbol', '')
            wb   = r.get('bassPitchClass', -1)
            wr   = parse_root(wsym)
            ws   = r.get('chordScore', 0)
            has7 = any(x in wsym for x in ['7','9','11','13'])
            print(f"\n{fpath.split('/')[-1].replace('.ours.json','')} m={meas} b={beat} key={key_label}")
            print(f"  Winner: {wsym:12s} quality={wq:12s} score={ws:.3f} rootPc={wr} bassPc={wb} has7={has7}")
            found_major = False
            for i, alt in enumerate(r.get('alternatives', [])):
                aq   = alt.get('quality', '')
                asym = alt.get('chordSymbol', '')
                ar   = parse_root(asym)
                ab   = parse_bass(asym)
                asc  = alt.get('score', 0)
                margin = ws - asc
                if aq == 'Major' and ar == wr:
                    found_major = True
                    print(f"  Major alt[{i}]: {asym:12s} score={asc:.3f} margin={margin:+.3f} "
                          f"rootPc={ar} bassPc={ab}")
                    print(f"    Gate L checks: same_root={ar==wr} same_bass={ab==wb} "
                          f"margin_ok={margin<=0.35} ext_guard_ok={not has7}")
            if not found_major:
                print(f"  NO Major alt found with same root. Alt list (first 6):")
                for i, alt in enumerate(r.get('alternatives', [])[:6]):
                    print(f"    alt[{i}]: {alt.get('chordSymbol','?'):15s} "
                          f"q={alt.get('quality','?'):12s} score={alt.get('score',0):.3f}")
            break
```

---

## Step 6 — Report to Cowork

```
Step 0 — Three-way definition:
  Sources compared: [list]
  DCML required: [yes / no / partial]
  Exact condition: [AND / majority / other — quote the code]
  Implication: [are all 48 genuine errors ones where DCML also disagrees?]

Step 1 baseline: BIR=true=N, BIR=false=N

Step 3 — Genuine-48 distribution:
  Cat 1: N cases
    winner_qualities: [list]
    alt_qualities:    [list]
    Top patterns: (WQ→AQ)=N ...
  Cat 2: N cases
    quality_pairs: [list sorted by count]
  Cat 3: N cases
  Cat 4: N cases
  [full GENUINE case list verbatim]

Step 4 — Cat 2 cross-reference against genuine 48:
  (Major→Minor7) genuine overlap: N cases
    [list each: file, m, beat, margin, key, I-interval]
    I-interval pattern: [consistently I3 / mixed]
    Gate J relevance: [yes — same mechanism / no]
  (Power→Major) genuine overlap: N cases
    [list each]

Step 5 — Residual Augmented TYPE-A investigation:
  bwv345 m=8  b=2: [which Gate L condition failed]
  bwv407 m=19 b=4: [which condition failed]
  bwv424 m=1  b=4: [which condition failed]
```

Do NOT implement any fix. Do NOT commit.

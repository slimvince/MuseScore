# Iteration 24: Enumerate all Cat 1 Minor-winner cases and check references

## Background

Iter 23 established that the Cat 1 Minor→Dim pattern is not a quality error —
it is a root error. In all 6 sampled cases the reference chord is a
first-inversion chord (e.g. C/E, D/F#, G/B) whose bass is the major third of
the true root, and the correct first-inversion chord was already present in our
candidate list (as alt[1]) but lost to a root-position minor chord at the same
bass.

This iteration enumerates all Cat 1 Minor-winner cases (all `winner_quality ==
"Minor"` rows from the Iter 22 CAT1-ALL list, ≈25 cases) to determine:
1. Is the Type-B pattern universal, or are some actually Type A?
2. Is the correct first-inversion chord always in our candidates?
3. What is the score margin between our winner and the correct alt?
4. What is the scale-degree relationship: is bass always the major third (+4)
   of the true root, or are there minor-third (+3) or other intervals?

Zero code changes.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — confirm baselines: BIR=true=71, BIR=false=788

---

## Step 2 — Build the case list

From the Iter 22 CAT1-ALL output, extract all rows where `winner` is a Minor
chord (quality == "Minor" — includes plain "Xm" and "Xm6" symbols). From the
list provided that is approximately these cases (verify against the script
output):

```
bwv153.9   m=5   Em      key=Cmaj
bwv154.3   m=1   F#m     key=Amaj
bwv245.14  m=2   F#m     key=Amaj
bwv245.22  m=1   C#m     key=Emaj
bwv282     m=12  Bm      key=Gmaj
bwv301     m=2   Dm6     key=Dmin
bwv302     m=1   Em      key=Dmaj
bwv322     m=11  Em      key=Cmaj
bwv327     m=6   F#m     key=Dmaj
bwv353     m=8   Dm      key=Gmin
bwv359     m=1   F#m     key=Amaj
bwv378     m=13  Em      key=Gmaj
bwv383     m=6   Em      key=Cmaj
bwv397     m=1   Dm      key=Fmaj
bwv40.6    m=14  Gm      key=Dmin
bwv408     m=4   Dm      key=GDor
bwv409     m=4   F#m     key=Amaj
bwv423     m=9   Gm      key=Dmin  (beat 2)
bwv423     m=9   Dm      key=Dmin  (beat 3)
bwv85.6    m=5   Fm      key=Gmin
```

Also include the two Cat 1 MinorAdd6 cases (Gm6, Em6, Dm6 from
`bwv187.7 m14`, `bwv227.11 m10`, `bwv278 m8`):
```
bwv187.7   m=14  Gm6     key=Gmin
bwv227.11  m=10  Em6     key=Emin
bwv278     m=8   Em6     key=Emin
```

---

## Step 3 — For each case, look up music21 reference

Open `tools/corpus/bwvXXX.music21.json` for each file. Find the region
matching the measure number. Report:
- `rootPitchClass` (music21 root)
- `chordSymbol` (music21 chord symbol, for human readability)
- `bassPitchClass`

Also report from our `tools/corpus/bwvXXX.ours.json`:
- Our winner: `rootPitchClass`, `chordSymbol`, `chordScore`
- Alt[1] (first distinct alternative): `chordSymbol`, `score`
- `raw_margin` = our chordScore − alt[1] score

---

## Step 4 — Classify and derive interval

For each case compute:
- `ref_rootPc` = music21's rootPitchClass
- `interval` = (winner.bassPc − ref_rootPc) mod 12
  (how many semitones above the true root is our winning bass note?)
- `type`:
  - **I4** (interval=4): bass is the major third of the true chord → classic
    first inversion (6th chord)
  - **I3** (interval=3): bass is the minor third → first inversion of minor
    or diminished chord
  - **I7** (interval=7): bass is the fifth → second inversion (6/4 chord)
  - **OTHER**: some other interval → may be a different error type

For each I4/I3/I7 case, check: is the true reference chord (ref_rootPc +
appropriate quality) present as one of our candidates (alt[1..3])?

---

## Step 5 — Produce summary table

Print one row per case:

```
FILE          M    BEAT  OUR-WINNER  OUR-SCORE  REF-CHORD  REF-ROOT  ALT1-CHORD  ALT1-SCORE  MARGIN  INTERVAL  TYPE   REF-IN-ALTS
bwv153.9      5    3.0   Em  4.00    C/E        0          C/E       3.80        +0.20       I4      yes
...
```

Then print aggregate counts:
```
Total Minor-winner Cat 1 cases: N
  I4 (major-third inversion): N  (X%)  — ref in alts: N/N
  I3 (minor-third inversion): N  (X%)  — ref in alts: N/N
  I7 (fifth / 6-4 chord):     N  (X%)  — ref in alts: N/N
  OTHER (not an inversion):    N  (X%)

Where ref is in our candidates: N total  (X%)
Where ref is alt[1] (immediate runner-up): N
Raw margin stats (all cases): min / median / max
Raw margin < 0.30: N  (X%)
```

---

## Step 6 — Report to Cowork

Provide the full table and aggregate counts from Step 5, then answer:

1. Is the Type-B (root error, first inversion) pattern universal? Or are some
   cases genuinely quality errors?
2. What is the dominant interval type (I4, I3, I7)?
3. In what fraction of cases is the correct reference chord already in our
   candidates? In what fraction is it alt[1]?
4. What are the margins — are they tight enough that a gate can flip the result
   without requiring large score changes?
5. What additional condition (if any) should the gate check to avoid false
   positives — e.g., must the reference root be a diatonic chord in the key?

Do NOT implement any gate. Do NOT commit.

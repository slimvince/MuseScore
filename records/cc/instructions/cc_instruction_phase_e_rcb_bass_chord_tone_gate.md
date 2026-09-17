# CC Instruction: Phase E — rcb bass-chord-tone gate (Gate R)

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`,
`C:\s\MS\docs\scoring_model.md` (§2, §4 rootContinuityBonus, §9, §11),
and `C:\s\MS\cc_deltaseven_phase_e_diagnostic_report.md`.

---

## What this fixes and why

Diagnostic report confirms: the Δ=+7b cluster (bwv245.28 t4320, bwv296 t23040,
bwv320 t37440) is NOT a near-tie. The DCML-correct candidate leads the oracle by
0.38 (raw ≈ 1.90 vs 1.52). `rootContinuityBonus` (+0.40) reverses this clear win.

The wrong candidate is structurally implausible: it forces the CURRENT BASS NOTE
to be a non-chord-tone of the candidate root. Specifically, all three cases have
`(bassPc - candidateRootPc + 12) % 12 == 9` — a major sixth from root, which
appears in NONE of the 17 templates. The oracle correctly scores it lower (0.38
gap), but rcb overrides the oracle.

The mozart_k280-1 control is safe: its continued candidate always has a chord-tone
bass (G = P5 of C, E♭ = m3 of C minor). The gate does not fire there.

**Falsified alternatives (do not retry):**
- `consecutiveBassStepwiseCount` gate: {0,2,0} vs mozart {1,1,0,0} — no separation
- `previousQuality` gate: Minor/Major/Minor in both failing and control — no separation
- `wSeqBonus`: structurally off (distinctPcs=3 < 4 threshold) — unrelated

---

## The gate: Gate R

Before applying `rootContinuityBonus` in `harmonicfunctionlayer.cpp`, check whether
the candidate's bass is a chord tone of the candidate template. If not, zero the bonus.

**Condition:** `rcb > 0 AND (bassPc - rootPc + 12) % 12 ∉ template_intervals[tiePriority]`

This is a structural consistency check, not a progression/context signal. A non-chord-
tone bass continuation is harmonically impossible for the candidate — the oracle already
penalises it (0.38 raw gap) but rcb overwhelms the oracle's verdict. Gate R prevents
that override.

---

## Step 1 — Confirm tiePriority is the template index

In `harmonicfunctionlayer.h`, confirm that `ScoringCell::tiePriority` is documented as
"Template index" (value 0–16). It should be. If it is NOT actually the template index —
if it is a different disambiguation value — stop and report before proceeding.

Also confirm that the template array in `chordanalyzer.cpp` has 17 entries (matches
`scoring_model.md §2`). Read the `array<TemplateDef, 17>` declaration and verify the
interval sets for templates 0–3 match the table in §2 exactly. Report any discrepancy.

---

## Step 2 — Add helper function to harmonicfunctionlayer.cpp

Add a `static bool` helper function in `harmonicfunctionlayer.cpp`, before
`applyHarmonicFunction`. It takes `(rootPc, tiePriority, bassPc)` and returns
whether `bassPc` is a chord tone of the template.

The helper must enumerate the EXACT interval sets from the 17 templates in
`chordanalyzer.cpp`. Read those templates directly and transcribe the intervals —
do NOT guess or extrapolate from the quality name. The interval sets from
`scoring_model.md §2` are reproduced below as a cross-check; CC must verify them
against the actual code:

```
Template 0  Major triad:    {0, 4, 7}
Template 1  Maj7:           {0, 4, 7, 11}
Template 2  Dom7:           {0, 4, 7, 10}
Template 3  Dom7♭5:         {0, 4, 6, 10}
Template 4  Minor triad:    {0, 3, 7}
Template 5  Minor 7th:      {0, 3, 7, 10}
Template 6  Diminished:     {0, 3, 6}
Template 7  Sus4♭5:         {0, 5, 6, 10}
Template 8  HalfDim:        {0, 3, 6, 10}
Template 9  Augmented:      {0, 4, 8}
Template 10 Aug dom7:       {0, 4, 8, 10}
Template 11 Sus2:           {0, 2, 7}
Template 12 Sus4+m7:        {0, 5, 7, 10}
Template 13 Sus4+Maj7:      {0, 5, 7, 11}
Template 14 Sus4♯5:         {0, 5, 8, 10}    ← verify against code
Template 15 Sus♯4:          {0, 6, 7}         ← verify against code
Template 16 Power:          {0, 7}
```

**Suggested implementation skeleton — adapt to match what you find in the code:**

```cpp
/// Gate R helper: returns true if bassPc is a tone of the candidate's template,
/// false if the bass is foreign to the candidate's chord.
/// Returns true on unknown/out-of-range inputs (conservative — don't gate if unsure).
static bool bassIsTemplateChordTone(int rootPc, int tiePriority, int bassPc) noexcept
{
    if (rootPc < 0 || bassPc < 0 || tiePriority < 0 || tiePriority >= 17)
        return true;
    const int interval = (bassPc - rootPc + 12) % 12;

    // Interval bitmasks indexed by template index (0–16).
    // Bit i is set if semitone interval i (from root) is a template tone.
    // MUST stay in sync with the TemplateDef array in analyzeChord().
    // When adding a new template, update this table and scoring_model.md §R.
    static constexpr std::array<uint16_t, 17> kMasks = {
        // Row comments show template intervals for cross-checking
        (1u<<0)|(1u<<4)|(1u<<7),               // 0  Major triad     {0,4,7}
        (1u<<0)|(1u<<4)|(1u<<7)|(1u<<11),      // 1  Maj7            {0,4,7,11}
        (1u<<0)|(1u<<4)|(1u<<7)|(1u<<10),      // 2  Dom7            {0,4,7,10}
        (1u<<0)|(1u<<4)|(1u<<6)|(1u<<10),      // 3  Dom7♭5          {0,4,6,10}
        (1u<<0)|(1u<<3)|(1u<<7),               // 4  Minor triad     {0,3,7}
        (1u<<0)|(1u<<3)|(1u<<7)|(1u<<10),      // 5  Minor 7th       {0,3,7,10}
        (1u<<0)|(1u<<3)|(1u<<6),               // 6  Diminished      {0,3,6}
        (1u<<0)|(1u<<5)|(1u<<6)|(1u<<10),      // 7  Sus4♭5          {0,5,6,10}
        (1u<<0)|(1u<<3)|(1u<<6)|(1u<<10),      // 8  HalfDim         {0,3,6,10}
        (1u<<0)|(1u<<4)|(1u<<8),               // 9  Augmented       {0,4,8}
        (1u<<0)|(1u<<4)|(1u<<8)|(1u<<10),      // 10 Aug dom7        {0,4,8,10}
        (1u<<0)|(1u<<2)|(1u<<7),               // 11 Sus2            {0,2,7}
        (1u<<0)|(1u<<5)|(1u<<7)|(1u<<10),      // 12 Sus4+m7         {0,5,7,10}
        (1u<<0)|(1u<<5)|(1u<<7)|(1u<<11),      // 13 Sus4+Maj7       {0,5,7,11}
        0u,                                     // 14 PLACEHOLDER — fill from code
        0u,                                     // 15 PLACEHOLDER — fill from code
        (1u<<0)|(1u<<7),                        // 16 Power           {0,7}
    };

    return (kMasks[static_cast<size_t>(tiePriority)] & (1u << interval)) != 0;
}
```

**Fill in entries 14 and 15 from the actual template definitions in `chordanalyzer.cpp`.**

If any entry in this table is 0 after filling, stop and report — every template must
have at least one interval (interval 0, the root, is always present).

---

## Step 3 — Apply Gate R in Pass A (harmonicfunctionlayer.cpp ~L206)

The current code:
```cpp
const double rcb = rootContinuityBonus(cell.rootPc, ctx.previousRootPc,
                                       prefs.rootContinuityBonus);
const double newBasisIndep = cell.basisIndep + rcb;
```

Replace with:
```cpp
double rcb = rootContinuityBonus(cell.rootPc, ctx.previousRootPc,
                                 prefs.rootContinuityBonus);
// Gate R: withhold rcb when the bass is foreign to the candidate's own chord tones.
// Prevents a non-chord-tone continuation from inheriting the predecessor's +0.40.
if (rcb > 0.0 && !bassIsTemplateChordTone(cell.rootPc, cell.tiePriority, cell.bassPc)) {
    rcb = 0.0;
}
const double newBasisIndep = cell.basisIndep + rcb;
```

`cell.tiePriority` is the template index — confirmed in `ScoringCell` header comment.

---

## Step 4 — Build and run both test suites

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/gateR_comp.txt 2>&1; echo "exit:$?"
head -30 /tmp/gateR_comp.txt

cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/gateR_nota.txt 2>&1; echo "exit:$?"
head -30 /tmp/gateR_nota.txt
```

Read `src/composing/tests/chord_mismatch_report.txt`.

Expected result:
- Baroque BIR=false: 16 → **13** (three Δ=+7b cases fixed: bwv245.28, bwv296, bwv320)
- Baroque BIR=true: 25 → **≥25** (no regressions)
- Jazz BIR: unchanged or improved
- Snapshot goldens: ZERO drifted

If Baroque BIR=false < 13: unexpected bonus fix — report but don't be surprised.
If any BIR=true count drops (regression): **STOP. Do not commit. Report immediately.**
If snapshot goldens drift, this is expected for the three target scores (bwv245.28,
bwv296, bwv320) if they are in the pipeline snapshot corpus. Their output SHOULD
change to reflect the newly-correct chord. Handle as follows:
- Run `./pipeline_snapshot_tests.exe > /tmp/snap_gateR.txt 2>&1; echo "exit:$?"` and read the output
- Confirm the failing snapshot tests are ONLY the three target scores (nothing else)
- For each, verify the new output shows the DCML-expected chord (E major for bwv245.28,
  G major for bwv296, C major for bwv320)
- If and only if that checks out, run: `./pipeline_snapshot_tests.exe --update-goldens; echo "exit:$?"`
- Re-run `./pipeline_snapshot_tests.exe > /tmp/snap2.txt 2>&1; echo "exit:$?"` to confirm all pass
- If ANY snapshot test outside the three target scores fails: STOP and report.

---

## Step 5 — Corpus analysis (BOTH presets — MANDATORY)

Per CLAUDE.md gate threshold policy, corpus analysis must run for BOTH presets before
committing any gate addition:

```
# Baroque
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py; echo "exit:$?"

# Jazz (immediately after — reuses output dir)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py; echo "exit:$?"
```

Hard stops (do not commit if triggered):
- Baroque BIR=false increases above baseline (currently 16 before this fix)
- Jazz BIR=false increases above baseline (currently 10)

---

## Step 6 — Update docs/scoring_model.md

Gate R is a new scoring constraint. Per CLAUDE.md sync rule, any gate addition must
be documented in `scoring_model.md` in the SAME commit as the code change.

Add a new subsection under §4 ("Bonus and penalty terms"), after the
`rootContinuityBonus` section:

**Suggested title:** `### Gate R — rcb bass-chord-tone guard`

It should document:
- What the gate does and where it fires (Pass A, `harmonicfunctionlayer.cpp`)
- The condition: `rcb > 0 AND bassIsTemplateChordTone returns false`
- Why it exists: oracle correctly scores non-chord-tone-bass candidates lower, but
  rcb (+0.40) can overwhelm a 0.38 oracle lead; gate restores oracle priority
- The Δ=+7b mechanism it fixes (B/G♯, D/B, G/E — all interval=9, foreign to template)
- Safety: Alberti-bass safe (Alberti bass always uses chord tones), forward-compatible
  with template additions (sync table in `harmonicfunctionlayer.cpp`)
- Mozart control: passes unaffected (continued candidate always has chord-tone bass)

Also add a **sync requirement** to §9 ("Atomic update requirements"):
> When adding a template, update `kMasks` in `bassIsTemplateChordTone`
> (`harmonicfunctionlayer.cpp`) as a 5th mandatory site. Entries 0 and 0u are not
> valid — every template must have at least interval 0 (the root).

---

## Step 7 — Commit atomically (code + docs together)

If all tests pass and BIR improves as expected:

```
git add src/composing/analysis/function/harmonicfunctionlayer.cpp
git add docs/scoring_model.md
git commit -m "feat: Gate R — rcb bass-chord-tone guard (Δ=+7b fix, Baroque -3 BIR=false)"
```

Then update STATUS.md:
```
git add STATUS.md
git commit -m "docs: STATUS.md — Gate R commit, new BIR baselines"
```

Do not push.

---

## Report format

Write findings to `C:\s\MS\cc_gate_r_report.md`.

Include:
1. tiePriority confirmation (is it the template index?)
2. Interval sets verified for templates 14 and 15 (what did the code actually say?)
3. Final `kMasks` array as implemented (rows 0–16)
4. BIR before and after: `Baroque BIR=true=X, BIR=false=Y; Jazz BIR=true=X, BIR=false=Y`
5. Which of the three target cases are now fixed (which still fail, if any)
6. Any unexpected regressions or bonuses
7. Corpus analysis results for both presets
8. Whether snapshot goldens needed refreshing (and why, if so)

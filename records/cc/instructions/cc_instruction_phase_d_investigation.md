# CC Instruction: Phase D investigation — arpeggio sub-region mechanism

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), and
`C:\s\MS\docs\redesign_plan.md` Step 4 (Phase D section).

**This is a read-only investigation.** No source code changes. No build. The
goal is to confirm or correct the working hypothesis about why the DCML root
is absent from the arpeggiated sub-regions in bwv102.7 and bwv261, and to
characterise the corpus-wide impact of the candidate fix before any code is
written.

---

## Background

The two Δ=+7a BIR=false cases (bwv102.7 AbMaj7, bwv261 F#7) are segmentation +
rcb-cascade failures. The oracle is correct in present-root slices — in those
slices AbMaj7 and F#7 win by a clear margin. The failure is that a preceding
arpeggiated sub-region has the DCML root absent from its tone set, commits the
wrong chord, and `rootContinuityBonus` cascades that wrong root forward into
the slice where the oracle would get it right.

The working hypothesis (from Cowork's code reading, session 3):

1. **Pass 2b** (`regionanalyzer.cpp`) calls `detectBassMovementSubBoundaries`,
   which returns tick boundaries wherever the bass note changes within a parent
   region. For an arpeggiated chord, bass changes at every arpeggio step.

2. **`collectRegionTones`** (in `regiontonecollector.cpp`) handles each
   sub-region's tone collection. It includes a BACKWARD walk from the sub-region
   start to pick up notes that started before but still sustain into the window.
   The inclusion condition is:
   ```cpp
   if (noteEnd <= startTickInt) { continue; }
   ```
   Notes that end EXACTLY at `startTickInt` are excluded.

3. For an arpeggio, each arpeggio note ends at exactly the same tick where the
   next bass movement triggers a sub-boundary. So the previous arpeggio note
   (which may include the DCML root) has `noteEnd = startTickInt` → excluded
   from the sub-region's tone set.

4. Without the DCML root in the tone set, the oracle correctly identifies the
   best chord FROM WHAT IT CAN SEE — but that chord has the wrong root. That
   wrong root is then committed as `previousRootPc`, and `rootContinuityBonus`
   cascades it forward.

**Your job is to confirm or falsify this hypothesis and characterise the fix.**

---

## Task 1 — Read the code (no tools needed beyond Read/Grep)

### 1a. Confirm the backward walk condition

Read `src/composing/analysis/engravingbridge/regiontonecollector.cpp` around
line 316. Confirm:
- The backward walk iterates segments before `startTick`
- For each note found, it computes `noteEnd = segTickInt + actualTicks`
- The inclusion condition is `if (noteEnd <= startTickInt) { continue; }`

Answer: Is this the exact condition? Is there any other path that would include
a note with `noteEnd == startTickInt`?

### 1b. Read `detectBassMovementSubBoundaries`

Read `src/composing/analysis/engravingbridge/regiontonecollector.cpp` around
line 668. Answer:

- What exactly triggers a sub-boundary? Is it the first tick where a new bass
  note attacks, or something else?
- For a standard arpeggio figure, would each arpeggio step generate its own
  sub-boundary? Or only structural bass movements?
- Is there a minimum-duration threshold before a sub-boundary is accepted
  (similar to how Pass 2b has `kPass2bMinRegionTicks` for the parent)?

### 1c. Read `coalesceShortSameRootRuns`

Re-read `src/composing/analysis/region/regionanalyzer.cpp` starting at line 57.
Confirm:
- The coalesce function breaks the run when `rootPc` changes (line ~101)
- Since arpeggio sub-regions have different roots (different chords from
  incomplete tone sets), coalesce does NOT rescue the Δ=+7a cases
- State the exact condition under which this rescue WOULD apply

---

## Task 2 — Empirical confirmation via batch_analyze

### 2a. Find the failing measure number in bwv102.7

Run:
```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv102.7.xml" \
  --preset Baroque --dump-regions batch > /tmp/bwv102_regions.json 2>&1; echo "exit:$?"
```

Parse `/tmp/bwv102_regions.json` with Python (or `cat | python -c "..."`) to find
all regions where `quality == "Major"` and `rootPc == 3` (Eb, pc=3) or similar
wrong-root chords in the neighborhood. The failing region should show the wrong
root (Eb or whatever oracle picks without Ab). 

Identify: the measure number(s) and beat(s) of the wrong-root sub-region.

Also look for adjacent regions in the same measure to see the full arpeggio picture.

### 2b. Run --diagnose-measures for the failing bar

Once you have the measure number, run:
```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv102.7.xml" \
  --preset Baroque --diagnose-measures N > /tmp/bwv102_diag.json 2>&1; echo "exit:$?"
cat /tmp/bwv102_diag.json
```

Note: `--diagnose-measures` only shows the FIRST region in the measure. If the
failing sub-region is not the first one, run the measure BEFORE the failing
measure to see the first region there (or use --diagnose-measures with a comma
list to show multiple measures).

From the diagnostic output, report:
- `collected_notes` for the failing region: which pitch classes are present?
  Is the DCML root (Ab = pc 8 for bwv102.7) absent from `collected_notes`?
- `pc_weights`: is pc 8 (Ab) zero or near-zero?
- `output_symbol`: what chord does this region get?

### 2c. Repeat for bwv261

Run the same two commands for bwv261. The DCML label is F#7 (root F# = pc 6).
Confirm whether pc 6 (F#) is absent from the failing sub-region's tone set.

---

## Task 3 — Measure the corpus-wide impact of the candidate fix

The candidate fix is to change the backward walk condition in
`collectRegionTones` from:
```cpp
if (noteEnd <= startTickInt) { continue; }
```
to:
```cpp
if (noteEnd < startTickInt) { continue; }
```

This would include notes that end exactly AT the sub-region start tick (i.e.,
the note "touches" the sub-region boundary without overlapping into it).

**Do NOT implement this yet.** First characterise the impact.

Read `collectRegionTones` in full. Answer:

1. **How many call sites** call `collectRegionTones` with sub-region context
   (i.e., `parentStartTickInt != -1`)? These are the Pass 2b calls. For those
   calls, the backward walk is precisely the arpeggiation context.

2. **What happens for parent-scope calls** (where `parentStartTickInt < 0` and
   it defaults to `startTickInt`)? For those, the sub-region start IS the
   region start — there's no "arpeggio step predecessor" in the backward walk.
   The backward walk captures notes from the PREVIOUS HARMONY that sustain into
   this region. For those, `noteEnd == startTickInt` means the note ended
   exactly when this region started — that IS the previous chord's final note,
   and excluding it is correct.

3. **Conclusion**: Is the fix `< startTickInt` safe for both sub-region calls
   AND parent-scope calls? Or does it need to be scoped only to sub-region
   calls (i.e., conditioned on `parentStartTickInt >= 0 && parentStartTickInt < startTickInt`)?

4. **Check any other callers** of `collectRegionTones` in the codebase. Are
   there callers other than `regionanalyzer.cpp` Pass 2 and Pass 2b?

---

## Task 4 — Check the `--dump-regions` sub-region picture

The `--dump-regions batch` output shows post-merge regions, not the raw Pass 2b
sub-regions. To see the intermediate state, run:
```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv102.7.xml" \
  --preset Baroque --dump-regions notation-premerge > /tmp/bwv102_premerge.json 2>&1; echo "exit:$?"
```

Find the arpeggiated bar's sub-regions. Report: how many sub-regions does the
arpeggio figure produce? What are their tick boundaries and chord identities
(root + quality)?

---

## Report format

Write findings to `C:\s\MS\cc_phase_d_investigation_report.md`.

Include:

### Section 1 — Backward walk mechanism
Confirm or falsify the hypothesis. Quote the exact `noteEnd <= startTickInt`
condition (or correct it if it's different). Confirm whether notes ending
exactly at `startTickInt` are excluded.

### Section 2 — Sub-boundary trigger
What does `detectBassMovementSubBoundaries` respond to? Is it any bass attack,
or only certain patterns? Minimum duration?

### Section 3 — Empirical: bwv102.7 and bwv261
For each score:
- The failing sub-region: tick range, tone set (`collected_notes`), DCML root
  present or absent in tone set, chord identity output
- The correct sub-region (where DCML root IS present): tick range, tone set,
  chord identity (confirm oracle picks DCML root correctly here)

### Section 4 — Fix scope analysis
The `<= to <` fix: safe for sub-region calls only, or safe universally?
Recommended scoping. Any edge cases that need guarding.

### Section 5 — `--dump-regions notation-premerge` sub-region picture
How many sub-regions does the arpeggio produce? Tick boundaries and chord
identities.

### Section 6 — Your assessment
Does the hypothesis hold? Is the `<= to <` boundary fix the right approach,
or is there a better location to fix this?

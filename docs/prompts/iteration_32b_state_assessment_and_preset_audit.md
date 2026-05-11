# Iteration 32b: State assessment, preset audit, and Gate L triage

## Purpose

This is a diagnostic-and-suggest-only iteration. CC must NOT implement any code
changes, NOT commit anything, and NOT run `--update-goldens`. The sole outputs are
a complete state report and a list of concrete suggested fixes for Cowork to approve.

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.

---

## Step 1 — Git state

Run:

```
cd C:\s\MS && git log --oneline -8
cd C:\s\MS && git status
cd C:\s\MS && git diff HEAD
```

Report verbatim:
- Last 8 commits (hash + message)
- Any uncommitted changes (files modified, staged, untracked)
- Full diff of any uncommitted changes (paste verbatim, every line)

---

## Step 2 — Current Gate L code

Read `src/composing/analysis/chord/chordanalyzer.cpp`.

Find Gate L (the block inserted in Iter 32). Report:
- The exact line range (first line to closing `}`)
- The complete Gate L code block verbatim (every line, no paraphrasing)
- Specifically: does it include any extension guard on the winner? Quote the
  exact condition if present.

If Gate L is absent from the file, report that explicitly.

---

## Step 3 — Understand presets (document before running)

Read `src/composing/batch/batch_analyze.cpp` (or wherever preset-specific
settings are applied — search for "Baroque" and "Jazz" strings).

Report for EACH preset (Baroque, Jazz, and any others found):
- Which flags are set differently from defaults
- Specifically: what value is `preferMinorOverMajorAdd6` for each preset?
- Any other boolean flags or thresholds that differ between presets

This documents which gates fire differently per preset. Gate L must be safe
for ALL presets, not just Baroque.

---

## Step 4 — Run corpus analysis: Baroque preset

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report BIR=true and BIR=false counts for Baroque.

**Reference baseline**: BIR=true=52, BIR=false=787 (post-Iter 30).
Note whether BIR=false has increased from 787. This is the critical check.

---

## Step 5 — Run corpus analysis: Jazz preset

Find the Jazz preset name by checking `tools/run_bach_preset.py` or
`tools/corpus_registry.json` — look for a preset covering Jazz scores.
Then run:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report BIR=true and BIR=false counts for Jazz.

**Reference baseline**: whatever the Jazz baseline was before Iter 32. If unknown,
note that explicitly and compare only directionally.

Also run the composing tests (they cover catalog Jazz pieces):

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Report pass/fail and any failing test names verbatim.

---

## Step 6 — Triage: what is wrong with Gate L (if anything)

Based on Steps 2–5, assess Gate L against the following checklist:

**A. Extension guard**
Does Gate L skip when the winner has a seventh or other significant extension?
Augmented+seventh chords (e.g. C+7, E+7) must NOT be promoted to plain Major —
that would strip the seventh.
- Required condition (missing = bug): winner has no MinorSeventh, MajorSeventh,
  or similar extension. In C++ terms:
  ```cpp
  && !hasExtension(winner.identity.extensions, Extension::MinorSeventh)
  && !hasExtension(winner.identity.extensions, Extension::MajorSeventh)
  ```
  (or `winner.identity.extensions.empty()` if that accessor exists and is appropriate).
  Confirm which form is correct by checking how Gate K checks extensions.

**B. Baroque BIR=false regression**
Is BIR=false > 787 in Baroque? If yes, Gate L is over-firing.

**C. Jazz BIR=false regression**
Is BIR=false higher than the pre-Iter-32 Jazz baseline? If yes, Gate L is
over-firing in Jazz.

**D. Composing test failures**
Did composing_tests.exe pass 407/407? If not, list all failing tests.

**E. Premature commit**
Is Gate L committed with a known bug (missing extension guard, BIR=false
regression, or catalog test failure)? If so, a revert commit will be needed.

---

## Step 6b — Gate L false positive scan: Jazz corpus only

**Background**: gate thresholds (Gate I: 0.45, Gate K: 0.20, Gate L: 0.35) are
intentionally tuned against the Baroque corpus. Those values are correct for Baroque
and should not be changed to accommodate other presets. However, when a gate is also
active in Jazz (or another preset), it must not cause regressions there. The fix for
a Jazz regression is a preset-specific threshold or a tighter entry condition — never
loosening the Baroque-tuned value.

Gate L is the gate currently known to misfire in Jazz. Run this focused scan on the
Jazz corpus (from Step 5) to identify exactly what is firing and why:

```python
import json, glob, os, re

NOTE_TO_PC = {'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,
              'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}

def parse_root(sym):
    m = re.match(r'^([A-G][b#]?)', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else -1

def parse_bass(sym):
    m = re.search(r'/([A-G][b#]?)$', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else parse_root(sym)

# Point at the Jazz corpus directory output from Step 5
CORPUS_DIR = 'tools/corpus'

# Build BIR=true error set for Jazz corpus
bir_true = set()
for f in glob.glob(os.path.join(CORPUS_DIR, '*.ours.json')):
    bwv = os.path.basename(f).replace('.ours.json', '')
    ref_f = f.replace('.ours.json', '.music21.json')
    if not os.path.exists(ref_f):
        continue
    ours = json.load(open(f))
    ref  = json.load(open(ref_f))
    ref_map = {(r['measureNumber'], round(r['beat'], 2)): r
               for r in ref.get('regions', [])}
    for r in ours.get('regions', []):
        if not r.get('bassIsRoot', False):
            continue
        key2 = (r['measureNumber'], round(r['beat'], 2))
        if key2 in ref_map and not ref_map[key2].get('bassIsRoot', True):
            bir_true.add((bwv, r['measureNumber'], round(r['beat'], 2)))

print(f"Jazz BIR=true error set: {len(bir_true)} cases\n")
print("Gate L false positive scan (Augmented root-pos → same-root Major, threshold=0.35):")
print("  [HAS_7TH] = winner has a seventh in its symbol — extension guard would block this\n")

true_fix, false_pos = [], []
for f in sorted(glob.glob(os.path.join(CORPUS_DIR, '*.ours.json'))):
    bwv = os.path.basename(f).replace('.ours.json', '')
    data = json.load(open(f))
    for r in data.get('regions', []):
        if not r.get('bassIsRoot', False): continue
        if r.get('quality','') != 'Augmented': continue
        wb = r.get('bassPitchClass', -1)
        wr = parse_root(r.get('chordSymbol',''))
        ws = r.get('chordScore', 0)
        winner_sym = r.get('chordSymbol','')
        has_seventh = any(x in winner_sym for x in ['7','9','11','13'])
        for i, alt in enumerate(r.get('alternatives', [])):
            if alt.get('quality','') != 'Major': continue
            asym = alt.get('chordSymbol','')
            if parse_root(asym) != wr: continue
            if parse_bass(asym) != wb: continue
            margin = ws - alt.get('score', 0)
            if margin > 0.35: break
            key3 = (bwv, r['measureNumber'], round(r['beat'],2))
            is_error = key3 in bir_true
            tag = '[HAS_7TH] ' if has_seventh else ''
            row = (f"  {tag}bwv={bwv:12s} m={r['measureNumber']:3} b={r['beat']:.1f}  "
                   f"winner={winner_sym:10s}  alt[{i}]={asym:8s}  margin={margin:+.3f}  "
                   f"key={r.get('key','?')}  {'WOULD-FIX' if is_error else 'FALSE-POS'}")
            (true_fix if is_error else false_pos).append(row)
            break

print(f"TRUE fixes (BIR=true errors Gate L would correct in Jazz): {len(true_fix)}")
for r in true_fix: print(r)
print(f"\nFALSE POSITIVES (BIR=false cases Gate L would incorrectly change): {len(false_pos)}")
for r in false_pos: print(r)
```

Report complete output verbatim. The `[HAS_7TH]` rows confirm whether an extension
guard resolves all false positives. If false positives remain even without seventh
extensions, a lower Jazz-specific threshold may also be needed.

---

## Step 7 — Suggest fixes (DO NOT IMPLEMENT)

Based on Step 6, provide a concrete suggested action for each issue found.
Format each suggestion as:

```
ISSUE: [description]
SUGGESTED FIX: [exact change — file, line number(s), old code, new code]
EXPECTED OUTCOME: [what BIR counts / test results should look like after fix]
```

Examples of the kind of suggestions expected:

```
ISSUE: Gate L missing extension guard — fires on C+7 (augmented+seventh) and
       promotes to C, stripping the seventh. Caused N Jazz catalog failures.
SUGGESTED FIX: In chordanalyzer.cpp line N, inside Gate L entry block, add:
  && !hasExtension(winner.identity.extensions, Extension::MinorSeventh)
  && !hasExtension(winner.identity.extensions, Extension::MajorSeventh)
EXPECTED OUTCOME: Jazz catalog tests 407/407; Jazz BIR=false restored to baseline.

ISSUE: Gate L committed at commit [hash] without extension guard.
SUGGESTED FIX: Follow-up commit adding extension guard, or git revert [hash]
  then re-implement correctly.
EXPECTED OUTCOME: Clean state for Iter 33.
```

Do NOT make any changes. Do NOT revert anything. Do NOT run `--update-goldens`.
Report only.

---

## Step 7b — Threshold-per-preset assessment

Based on the Step 6b output, for EACH gate answer:

1. Does the gate produce false positives in Jazz that it does NOT produce in Baroque
   (or vice versa)? If so, the threshold is preset-unsafe.
2. What is the largest false-positive margin seen in each preset?
3. What is the smallest TRUE_FIX margin seen in each preset?
4. Is there a single threshold that is safe for ALL presets, or would preset-specific
   thresholds be required?

Report this as a table:

```
Gate  | Baroque fix margins | Baroque FP margins | Jazz fix margins | Jazz FP margins | Safe single threshold?
------|---------------------|--------------------|-----------------|-----------------|-----------------------
I     | min–max             | min–max (N cases)  | min–max         | min–max (N)     | yes/no
K     | ...                 | ...                | ...             | ...             | yes/no
L     | ...                 | ...                | ...             | ...             | yes/no
```

If any gate is unsafe with a single threshold, flag it as requiring preset-specific
threshold work in a future iteration. Do NOT implement preset-specific thresholds
in this iteration — suggest only.

---

## Step 8 — Standing preset rule (document for future iterations)

For Cowork's records, confirm and document:

1. Which preset(s) exist and their corpus script flags (from Step 3).

2. **Threshold philosophy** — to be stated in every future iteration prompt:
   Gate thresholds (Gate I: 0.45, Gate K: 0.20, Gate L: 0.35, etc.) are calibrated
   against the Baroque corpus and are intentionally Baroque-specific. They must NOT
   be loosened or tightened to accommodate other presets. If a gate causes regressions
   in a non-Baroque preset, the correct fix is either:
   - A tighter entry condition that structurally excludes the problematic chord type
     (preferred — e.g. extension guard blocks C+7 regardless of preset), OR
   - A preset-specific threshold override applied at the entry point, leaving the
     Baroque threshold unchanged.
   Never widen a Baroque-tuned threshold to cover a Jazz edge case.

3. **Testing rule** — to be followed for every gate change going forward:
   Before committing any gate addition or modification, run corpus analysis for
   BOTH Baroque and Jazz presets and report BIR=true and BIR=false for each.
   Any BIR=false increase in ANY preset is a hard stop.
   The composing tests (catalog, including Jazz pieces) must pass 407/407.

---

## Step 9 — Report to Cowork

```
Git state:
  Last commits: [list]
  Uncommitted changes: [none / list of files]
  Gate L present in code: [yes / no]
  Gate L committed: [yes at hash X / no]

Gate L code (verbatim):
  [paste complete Gate L block]

Preset settings:
  Baroque: preferMinorOverMajorAdd6=[T/F], [other flags]
  Jazz:    preferMinorOverMajorAdd6=[T/F], [other flags]

Baroque corpus:  BIR=true=N (was 52), BIR=false=N (was 787)
Jazz corpus:     BIR=true=N, BIR=false=N (pre-Iter-32 baseline: N if known)
Composing tests: N/407  [list any failures]

Triage:
  A. Extension guard: [present / MISSING]
  B. Baroque BIR=false regression: [none / +N]
  C. Jazz BIR=false regression: [none / +N]
  D. Composing test failures: [none / N failures: list]
  E. Premature commit with bug: [yes / no]

Suggested fixes:
  [list each ISSUE / SUGGESTED FIX / EXPECTED OUTCOME block]
```

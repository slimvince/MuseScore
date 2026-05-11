# Iteration 62: Parallelise run_bach_preset.py corpus regeneration

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=6, BIR=false=125. Jazz BIR=false=12.
(New baselines from Iter 61, commit a34dba041e.)

**This is a tooling-only change.** No source code in `src/composing/` is
modified. No BIR change is expected.

---

## Background

`tools/run_bach_preset.py` (223 lines) processes 353 chorales sequentially —
one subprocess per chorale. Per-chorale outputs (`.ours.json`) are fully
independent. The only shared resource during the loop is `diag_fh` (diagnostic
file handle, used only when `--diag-out` is specified). The aggregate report
is written after the loop completes.

Target machine: AMD Ryzen 9 3900X, 24 logical processors, SSD only.
Expected speedup: ~16–20× on corpus regen wall-clock time.

---

## Step 1 — Read the script in full

Read `tools/run_bach_preset.py`. Identify:
1. The shape of `_run_batch_analyze(exe, xml_path, ours_path, preset, diag_fh)`
2. Exactly what `diag_fh` receives per chorale (lines written, format)
3. How per-chorale comparison stats are accumulated into the aggregate
   (look for counters, dicts, or lists updated inside the loop)
4. Any other mutable shared state in the loop body

---

## Step 2 — Extract a top-level worker function

Create a module-level function (not a lambda or inner function — required for
Windows `spawn` pickling) that handles one chorale end-to-end and returns
everything the main process needs:

```python
def _process_one(args_tuple):
    """Process a single chorale. Returns (stem, stats_or_None, diag_lines)."""
    (exe, xml_path, ours_path, preset, skip_cpp, corpus_dir) = args_tuple
    stem = xml_path.stem
    m21_path = corpus_dir / f"{stem}.music21.json"

    if not m21_path.exists():
        return stem, None, []   # SKIP

    diag_lines = []
    if not skip_cpp or not ours_path.exists():
        if exe is None:
            return stem, None, []
        # Capture diag output in memory instead of writing to shared file
        ok = _run_batch_analyze(exe, xml_path, ours_path, preset, diag_fh=None)
        if not ok:
            return stem, None, []

    # Run per-chorale comparison/stat logic — adapt to actual function/fields
    stats = _compare_chorale(ours_path, m21_path)
    return stem, stats, diag_lines
```

Adapt to the actual function names and stat fields from Step 1. The key
constraints:
- No shared mutable state (no global counters, no file handles in worker)
- All inputs passed via the tuple; all outputs via return value
- The function must be defined at module top level

---

## Step 3 — Replace the sequential loop

```python
import concurrent.futures
import multiprocessing

workers = min(multiprocessing.cpu_count(), len(xml_files))
print(f"  Parallelising over {workers} workers ({len(xml_files)} chorales)...")

work_items = [
    (exe, xml_path, out_dir / f"{xml_path.stem}.ours.json",
     args.preset, args.skip_cpp, corpus_dir)
    for xml_path in xml_files
]

aggregate_stats = _empty_stats()   # adapt to actual initialisation

with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
    futures = {pool.submit(_process_one, item): item[1].stem
               for item in work_items}
    for future in concurrent.futures.as_completed(futures):
        stem = futures[future]
        try:
            stem_out, stats, diag_lines = future.result()
        except Exception as exc:
            print(f"  ERROR {stem}: {exc}")
            continue
        if stats is None:
            print(f"  [{stem:<30}]  SKIP")
            continue
        _accumulate(aggregate_stats, stats)
        if diag_fh is not None:
            diag_fh.writelines(diag_lines)
        # Keep progress output — order will be non-deterministic
        print(f"  [{stem:<30}]  OK")

# Aggregate report write — unchanged from original
```

Replace `_empty_stats`, `_accumulate`, field names with the actual identifiers
from the script. Preserve every stat field that feeds into the final aggregate
report.

---

## Step 4 — Verify outputs are identical

Run one Baroque corpus regen and confirm BIR unchanged:

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=6, BIR=false=125.

If BIR changes, there is a bug in argument passing or stat accumulation —
investigate before proceeding.

Spot-check 5 random `.ours.json` files against known-good content:
```python
import json
from pathlib import Path
for p in sorted(Path('tools/corpus').glob('bwv1*.ours.json'))[:5]:
    d = json.loads(p.read_text())
    print(p.name, len(d.get('regions', [])), 'regions')
```

---

## Step 5 — Time the run

```bash
Measure-Command { python tools/run_bach_preset.py --preset Baroque `
    --output-dir tools/corpus } | Select-Object TotalSeconds
```

(Use PowerShell `Measure-Command` for reliable timing on Windows.)

Record wall-clock seconds. Compare to the last known sequential time if
available, otherwise note it as the new baseline.

---

## Step 6 — Commit

```bash
git add tools/run_bach_preset.py
git commit -m "Tools: parallelise run_bach_preset.py with ProcessPoolExecutor

Sequential per-chorale loop replaced with ProcessPoolExecutor.
Workers = min(cpu_count=24, 353) on AMD Ryzen 9 3900X.
Per-chorale .ours.json outputs are independent; diag lines
collected in worker return value and written by main process.

BIR=true=6 BIR=false=125 confirmed post-parallelisation.
Wall-clock time: Ns → Ns"
```

---

## Step 7 — Report to Cowork

```
Workers used: N  (cpu_count = N)
diag_fh handling: [lines collected in worker return / temp files]

BIR after parallelisation:
  BIR=true=N  BIR=false=N  (must be 6/125)

Wall-clock time: Ns  (was ~Ns sequential if known, else: new baseline)
Speedup: ~Nx

JSON spot-check: 5 files checked, region counts [list]

Committed: [yes — hash] / [not committed — reason]
```

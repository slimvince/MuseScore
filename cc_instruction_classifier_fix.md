# CC Instruction — Fix compare_rn.py classifier + Maj→Dom7 investigation

**Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`

**Current state:** Branch `master`, HEAD `f3e0f5f72c`, **working tree clean.**
BIR baselines (lenient-OR): Baroque BIR=true=28, BIR=false=16; Jazz BIR=true=35,
BIR=false=10. Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
Tests: 407/407 composing, **52/52 notation (fully green)**, pipeline_snapshot
11/11 (1 skipped).
Roman numeral baseline (HEAD `f3e0f5f72c`, 9 non-Bach corpora, 61,233 regions):
rn_agree=27.6% (16,905/61,233); root_agree=49.3% parity check (corpus snapshot
`live_20260603/`). Hard stop: rn_agree must not drop below 27.6%.

**Unification is complete.** Both parameter divergences resolved: D1
(`excludeLookAheadOnDenseStart`) intentionally divergent and load-bearing; D2
(`pass1MinDistinctPcsForCandidate`) unified at `1` on both paths. STEP 1
(`3d80d0a91d`): dim7-completeness guard + Gate J — Jazz BIR=true 56→33 (−23),
Baroque BIR=false 25→23 (−2).

Hard stops always: Baroque BIR=false > 25, Jazz BIR=false > 13, any test
regression beyond the known Corelli notation failure.

---

## Task: Fix compare_rn.py classifier + investigate Maj→Dom7 gap

This is a **tooling task only** — no changes to `src/composing/`, no build
needed.

---

### Background

`tools/compare_rn.py` classifies each matched (ours, DCML) region pair into one
of four buckets:

- `exact` — full RN string matches
- `partial` — root+quality agree, inversion/extension differs
- `quality_err` — root PC agrees but `_same_quality()` returns False
- `root_err` — root PC disagrees

The `quality_err` bucket is **misleadingly named**. `_same_quality(ours_deg,
dcml_deg)` is a pure string-equality test (`ours_deg == dcml_deg`), so a pair
like V→I fires `quality_err` even though both are uppercase = major quality. The
`--quality-breakdown` analysis (saved in
`tools/reports/rn_quality_breakdown_f3e0f5f72c.txt`) revealed:

- **~68% are key disagreements**: root PC same, chord quality same, but scale
  degree differs because we detect a different key. E.g., V→I means "we say the G
  chord is scale degree 5 in C major; DCML says the same G chord is scale degree
  1 in G major." Both are major quality; this is a key/mode detection error, not a
  chord-quality error.
- **~32% are genuine quality errors**: root PC same, quality actually differs.
  E.g., I→V7 means "we say G major triad in G major; DCML says G dominant seventh
  in C major."

The `extract_quality()` function already exists and correctly returns coarse
quality tokens (Maj, Min, Dom7, Maj7, Min7, Dim, Dim7, HalfDim, HalfDim7, Aug,
Aug7). It is already called in `score_piece()` for the `qe_quality_pairs`
counter. It is **not yet used in `classify_pair()`** to sub-classify.

---

### Step 1 — Fix `classify_pair()` to emit `key_disagree` / `quality_disagree`

In `classify_pair()`, find this block (around line 248–257):

```python
root_match    = (ours_region.root_pc == dcml_region.root_pc)
quality_match = _same_quality(ours_parts[1], dcml_parts[1])

if root_match and quality_match:
    if ours_norm == dcml_norm:
        cat = "exact"
    else:
        cat = "partial"
elif root_match and not quality_match:
    cat = "quality_err"
else:
    cat = "root_err"
```

Change the `quality_err` branch to sub-classify using `extract_quality()`:

```python
elif root_match and not quality_match:
    o_ext_q = extract_quality(ours_norm)
    d_ext_q = extract_quality(dcml_norm)
    cat = "key_disagree" if o_ext_q == d_ext_q else "quality_disagree"
else:
    cat = "root_err"
```

Also update `RN_CATEGORIES` (around line 192) — replace `"quality_err"` with
the two new names:

```python
RN_CATEGORIES = ("exact", "partial", "key_disagree", "quality_disagree", "root_err")
```

---

### Step 2 — Update `PieceStats`

Replace the single `quality_err: int = 0` field with:

```python
key_disagree:     int = 0
quality_disagree: int = 0
```

Update the `add()` method accordingly:

```python
self.key_disagree     += other.key_disagree
self.quality_disagree += other.quality_disagree
```

Rename `qe_quality_pairs` / `qe_rn_pairs` to reflect they are now
`quality_disagree`-only (or keep names as-is and only populate them for
`quality_disagree` pairs — your choice; renaming to `qd_quality_pairs` /
`qd_rn_pairs` is cleaner but requires touching more lines).

---

### Step 3 — Update `score_piece()` counting

Find the block (around line 348–358) that increments `quality_err` and populates
`qe_quality_pairs` / `qe_rn_pairs`. Replace it with:

```python
elif pair.category == "key_disagree":
    stats.key_disagree += 1
elif pair.category == "quality_disagree":
    stats.quality_disagree += 1
    o_q = extract_quality(pair.ours_rn)
    d_q = extract_quality(pair.dcml_rn)
    stats.qe_quality_pairs[(o_q, d_q)] += 1
    stats.qe_rn_pairs[
        (pair.ours_rn or "<empty>", pair.dcml_rn or "<empty>")
    ] += 1
```

---

### Step 4 — Update `format_report()` output lines

Find the two lines (around line 428–430):

```python
lines.append(f"  quality_err:     {_pct(stats.quality_err, m):5.1f}%  ({stats.quality_err}/{m})"
             f"   (root agrees, quality wrong)")
```

Replace with:

```python
lines.append(f"  key_disagree:    {_pct(stats.key_disagree, m):5.1f}%  ({stats.key_disagree}/{m})"
             f"   (root agrees, quality agrees, scale degree wrong — key detection error)")
lines.append(f"  quality_disagree:{_pct(stats.quality_disagree, m):5.1f}%  ({stats.quality_disagree}/{m})"
             f"   (root agrees, quality differs — true chord-quality error)")
```

---

### Step 5 — Update `_format_quality_breakdown()`

Find the block that references `agg.quality_err` (around line 449–470). Update
it to use `agg.quality_disagree` as the denominator for the breakdown table
(the breakdown is now about genuine quality errors only). The header line should
change from `total quality_err` to `total quality_disagree`.

Also update the per-corpus lines that show `st.quality_err` to use
`st.quality_disagree`.

---

### Step 6 — Re-run cross-corpus baseline

After all edits are clean, run:

```
cd C:\s\MS && python tools/compare_rn.py --cross-corpus tools/reports/live_20260603 > tools/reports/rn_corrected_classifier_f3e0f5f72c.txt; echo "exit:$?"
```

Also run with `--quality-breakdown` to get the corrected breakdown:

```
cd C:\s\MS && python tools/compare_rn.py --cross-corpus tools/reports/live_20260603 --quality-breakdown > tools/reports/rn_corrected_breakdown_f3e0f5f72c.txt; echo "exit:$?"
```

(If either file already exists, overwrite it — these are regenerated reports.)

Report:
- rn_agree (should be identical to 27.6% — we only relabelled, not changed matching)
- New key_disagree % and quality_disagree % (replacing the old quality_err 21.7%)
- Top quality_disagree pairs from the breakdown

---

### Step 7 — Investigate Maj→Dom7 cases

From the corrected breakdown output (`rn_corrected_breakdown_f3e0f5f72c.txt`),
find the quality_disagree Maj→Dom7 pair count and the top-5 scores/corpora
contributing them.

**Goal:** determine whether the 7th pitch class is present above
`extensionThreshold` (0.20) in these regions, or whether it is genuinely
absent/weak.

Pick **3 concrete (score, tick) examples** from different corpora (e.g., one
Beethoven, one Mozart, one Grieg). For each:

a) Identify the score XML file path (use `docs/score_inventory.md` or the
   corpus directory listing).

b) Run batch_analyze with `--dump-regions notation` on that score and redirect
   output to a temp file:
   ```
   cd C:\s\MS\ninja_build_rel && ./batch_analyze.exe ../tools/corpus/<score>.xml --preset Baroque --dump-regions notation > /tmp/majtod7_<score>.txt 2>&1; echo "exit:$?"
   ```
   (Substitute the correct `--preset` for that corpus — Jazz for Jazz scores,
   Baroque for Baroque. Check `build_and_test.md` for the correct invocation
   syntax.)

c) Search the dump for the specific tick value:
   ```
   grep -A 20 "tick.*<TICK>" /tmp/majtod7_<score>.txt | head -30; echo "exit:$?"
   ```

d) For that region, report:
   - Our chord (quality, rootPc)
   - DCML chord symbol  
   - The 7th PC = `(rootPc + 10) % 12`
   - The pcWeight of that 7th PC in the region's tone list
   - Whether it's above 0.20 (extensionThreshold) or not

Summarise: across the 3 sampled cases, how many have the 7th PC:
- **Present but below threshold** (pcWeight < 0.20): we correctly don't
  extend; DCML may be hearing implied harmony or operating in a different
  harmonic context
- **Present and above threshold** (pcWeight ≥ 0.20): there may be a bug
  blocking extension detection (investigate why `detectExtensions` doesn't
  fire)
- **Absent entirely**: DCML's dominant seventh interpretation is contextual
  (e.g., they know it's a V7 chord even without the 7th sounding)

Report your findings in a clear summary. If the majority of sampled cases have
the 7th absent or below threshold, conclude: "extension-threshold gap — DCML
labels implied dominant sevenths that our analyzer correctly does not extend to
without sounding evidence; not an actionable bug." If the majority have the 7th
above threshold with no extension, flag it for a separate investigation.

---

### Done

Report back:
1. That compare_rn.py edits are complete and the script runs cleanly
2. The corrected rn_agree (verify it equals the original 27.6%)
3. The split: key_disagree % + quality_disagree % (these two should sum to the
   old quality_err 21.7%)
4. The Maj→Dom7 sampling conclusion

# Jazz BIR=false nondeterminism — investigation report

**Verdict: the mechanism is neither M1 (C++ nondeterminism) nor M2 (Python hash
salting). It is M3 — corpus-state contamination in the shared `tools/corpus`
directory.** The Jazz BIR=false count is *deterministic* (7) for a cleanly and
fully regenerated Jazz corpus; the 7–9 "band" the Stage-2.1 report observed is an
artifact of measuring a corpus that still held some **Baroque** `.ours.json`
files. Proven by direct reconstruction: pure Jazz = 7 → inject one Baroque
floater file → 8 → inject a second → 9.

Build under test: `8598cbd245` (HEAD after the Stage-2.1 commits); `batch_analyze.exe`
rebuilt 21:15. Baroque corpus restored to canonical state on exit (13, 353/353 OK).

All claims tagged [probe] (measured) or [code] (read).

---

## 1. Mechanism, with the proving observations

### M2 (Python-side hash salting) — RULED OUT

[probe] `characterise_bir_false.py` run **5× over one fixed Jazz corpus** (no
regeneration between runs):

```
TOTAL genuine BIR=false: 7   ×5
md5 of full stdout: b4740ba5774fe556d10809b5b1849fc4   (all 5 identical)
```

Not just the count — the **entire output is byte-identical** across the five
processes, each with its own `PYTHONHASHSEED`. The measurement path is
deterministic given fixed inputs.

[code] Confirmed by inspection — no count-affecting set/dict iteration exists:
- `align_regions` (compare_analyses.py:191) breaks overlap ties with `ov > best_overlap`
  (strict `>`) over the **ordered list** `theirs` — first-in-list wins, deterministic.
- `align_dcml_regions` / `_best_dcml_match_by_overlap` (:488) — same `ov > best_ov`
  list-order tie-break.
- `_dcml_tick_for` (:430) uses `max(...)/min(...)` over dict **keys** — the value is
  order-independent.
- `classify` / `three_way_classify` are pure scalar comparisons.

### M1 (C++ nondeterminism in `batch_analyze`) — RULED OUT

[probe] **Two full Jazz regenerations** (706 independent `batch_analyze` process
invocations, fresh ASLR each):

```
regen A  → BIR=false 7
regen B  → BIR=false 7
manifest A vs B (md5 of all 353 *.ours.json):  0 files differ
```

Zero of 353 output files changed across two complete regenerations. If winner
selection depended on pointer order / uninitialized state, at least one of 353×2
analyses would have diverged. None did.

[code] The winner is selected by a **total deterministic order**, not container
order: score (exact double `>`), then `tiePriority` (template index, lower wins),
then `rootPc` (lower wins) — `chordanalyzer.h:308`
(`// template index; lower = preferred on equal score`), pinned by
`functionlayer_tests.cpp:457` (`TiePolicy_ExactTie_LowerTiePriorityWins`) and
`:473` (`TiePolicy_ExactTie_LowerRootPcBreaksFullTie`). So even the many
`margin=0.000` exact-tie Jazz cases resolve deterministically. **The report's
stated mechanism — "the parallel batch path resolves ties nondeterministically" —
is wrong on two counts: there is no threading in `batch_analyze` (process-level
parallelism only, in `run_bach_preset.py`), and ties are broken by
tiePriority+rootPc, not by traversal order.**

### M3 (corpus-state contamination) — PROVEN

The Stage-2.1 verification ran **Baroque first, then Jazz, into the *same*
`tools/corpus`** (the workflow CLAUDE.md / build_and_test.md prescribe:
`run_bach_preset.py --preset {Baroque,Jazz} --output-dir tools/corpus`).
Baroque BIR=false (13) > Jazz (7). A corpus that is *mostly* Jazz but still holds
a few Baroque `.ours.json` therefore scores **strictly between 7 and 13** — i.e.
8 or 9.

[probe] Reconstruction from a pure Jazz corpus:

```
pure Jazz corpus                              → 7
+ inject Baroque bwv102.7.ours.json           → 8
+ inject Baroque bwv14.5.ours.json            → 9
```

This reproduces the report's "8 then 9" exactly. The contaminating file is a
**different preset's reading of the same score**, not a re-resolved tie.

**How the Baroque residue arises in practice (two driver entry points):**
1. [code] `run_bach_preset.py::_process_one` (:113–122): if `_run_batch_analyze`
   returns `False` (a timed-out or crashed worker — the documented Windows Qt
   hazard), status is `'FAILED'` and **`ours_path` is never overwritten**, so the
   prior-preset file persists. The aggregate line counts only `OK` results, so a
   partial corpus is easy to miss unless you check `353/353`.
2. [probe-plausible] Measuring while a regen is still in flight — workers complete
   in arbitrary scheduling order, so an early `characterise` read sees a Baroque/Jazz
   mix. (Not separately reconstructed; mechanism identical to #1.)

The shared mutable `tools/corpus` dir + a metric script that reads "whatever is
there" with no preset guard is the root cause.

---

## 2. Flipping-case identities

The "flip" is **not** a within-score tie flip — it is which preset's file occupies
the slot. The cases that move the Jazz count when staled to Baroque:

**Baroque-only BIR=false floaters (8)** — present as BIR=false in Baroque, absent
in clean Jazz; each raises the Jazz count by 1 if left as a Baroque file:

| stem | m.beat | tick | Baroque "our" | DCML | Δ | margin |
|---|---|---|---|---|---|---|
| bwv102.7 | 9.b4.5 | 17520 | EbMaj7/Ab | major-seventh | +7 | 0.325 |
| bwv14.5  | 5.b1   | 8160  | Gm/Bb     | whole-tone trichord | +9 | 0.040 |
| bwv17.7  | 32.b3  | 46080 | A/Eb      | incomplete ø7 | +6 | 0.000 |
| bwv174.5 | 4.b1   | 6240  | E/G#      | incomplete m7 | +8 | 0.000 |
| bwv261   | 18.b4.5| 33840 | C#m/E     | dominant-seventh | +7 | 0.000 |
| bwv269   | 15.b1  | 20640 | D/F#      | diminished triad | +8 | 0.000 |
| bwv301   | 1.b3   | 960   | G/A       | incomplete m7 | +8 | 0.000 |
| bwv381   | 3.b3   | 4800  | G6/F#     | minor-seventh | +3 | 0.000 |

**Clean Jazz BIR=false set (7)** — the deterministic Jazz residual:

| stem | m.beat | tick | Jazz "our" | DCML | Δ | margin |
|---|---|---|---|---|---|---|
| bwv244.15 | 6.b1  | 10080 | Bm/D      | major triad | +4 | 0.000 |
| bwv245.17 | 3.b2  | 4800  | F/D       | incomplete dom7 | +3 | 0.000 |
| bwv245.40 | 27.b3 | 51360 | F7sus/Bb  | quartal trichord | +2 | 0.060 |
| bwv422    | 14.b1 | 23040 | A7sus/D   | quartal trichord | +2 | 0.060 |
| bwv432    | 3.b3.5| 5520  | Am/E      | minor triad | +5 | 0.000 |
| bwv45.7   | 11.b2 | 20160 | F#7/E     | diminished triad | +8 | 0.110 |
| bwv74.8   | 7.b4  | 13440 | Em7/D     | major-2nd tetrachord | +4 | 0.000 |

Of these, **bwv244.15** and **bwv74.8** are Jazz-only (Baroque reads them
correctly) — if *those* scores carried Baroque residue the count would drop below
7. The report saw values *above* 7, which means its residue fell on the
Baroque-only floaters above. (Five cases — bwv245.17, bwv245.40, bwv422, bwv432,
bwv45.7 — are BIR=false in *both* presets and so never move the count.)

The `margin=0.000` entries are exact ties, but they resolve **deterministically**
(tiePriority+rootPc, §1 M1) — they are stable winners, not coin-flips.

---

## 3. Band distribution

| corpus state | measurements | distribution |
|---|---|---|
| **Jazz, clean full regen** | 7 (5 same-corpus + 2 independent full regens) | **{7: 7}** — deterministic |
| **Baroque, clean full regen** | 4 (3 same-corpus + 1 restore regen) | **{13: 4}** — deterministic |
| Jazz + Baroque residue (reconstructed) | — | 7 → 8 → 9 as floaters injected |

Baroque is **genuinely stable**, not merely less tie-prone: it is the *same*
deterministic pipeline; its 13 cases are fixed. Neither preset floats on its own.
The band exists only across the **mixed** state.

---

## 4. Localized code sites (no fix applied)

| site | role in the artifact |
|---|---|
| CLAUDE.md / build_and_test.md corpus-check recipe | instructs **both** presets to write `--output-dir tools/corpus` — the shared mutable dir is the precondition |
| `run_bach_preset.py::_process_one` :113–122 | a `FAILED` worker leaves the previous preset's `.ours.json` in place (no overwrite, no delete) |
| `run_bach_preset.py::main` aggregate (:242) | reports `compared_n/total`; a partial corpus is only caught if the reader checks for `353/353` |
| `characterise_bir_false.py` :28, :61 | reads every `*.ours.json` in `tools/corpus` with **no preset stamp / no mix guard** — silently scores a contaminated set |

Not a `chordanalyzer.cpp` / scoring problem at all — the analyzer and the metric
script are each deterministic.

---

## 5. Recommended fix design (for the Stage-2.2 decision — not implemented)

Pick one or combine; all are deterministic, none touch scoring:

1. **Per-preset output dirs (lowest-risk).** Stop sharing `tools/corpus` across
   presets. Use the script's *own default* (`tools/corpus_<preset>`) or explicit
   `tools/corpus_jazz` / `tools/corpus_baroque`, and give `characterise_bir_false.py`
   a `--corpus-dir` argument (today `_CORPUS_DIR` is hard-wired to `tools/corpus`).
   Contamination becomes structurally impossible.
2. **Preset stamp + mix guard.** Have `batch_analyze` write the preset into each
   `.ours.json` meta; `characterise_bir_false.py` asserts all files share one preset
   and **fails loud** on a mix. Catches the artifact regardless of dir hygiene.
3. **Fail-loud / clean-slate regen.** `run_bach_preset.py` should (a) `exit 1` when
   `compared_n < total`, and (b) delete each target `.ours.json` *before* its regen,
   so a failed worker yields a *missing* file (skipped) rather than a stale
   wrong-preset file. Makes "the corpus is exactly this preset" verifiable.

Recommended: **#1 as the durable fix + #3(a) as a cheap guard.** #2 is the most
robust but needs a `batch_analyze` output-schema touch (Stage-2.2 already opens the
batch path).

---

## 6. Interim gate guidance (until a fix lands)

A bare integer "Jazz BIR=false ≤ 7" is unsafe to gate on, because the integer is
only meaningful for a *clean, fully-regenerated, single-preset* corpus. Until the
fix:

- **Gate on a clean regen, not the raw count.** Require the Jazz regen log to show
  `Chorales compared: 353/353` (no `FAILED`/`SKIP`) *before* the count is read; if
  not, re-regenerate. A "7" off a partial corpus is luck; a "7" off 353/353 is real.
- **Gate on case *identity*, not magnitude.** The pass condition is: the Jazz
  BIR=false set equals exactly `{bwv244.15, bwv245.17, bwv245.40, bwv422, bwv432,
  bwv45.7, bwv74.8}` (and Baroque = its 13-case set in §2). A regression that swaps
  one case for another at the same count is then visible; contamination that adds a
  Baroque-only floater is rejected by identity even though the integer "looks" ≤ band.
- **Keep the existing structural co-gates** — snapshots 11/11 zero-diff and
  Baroque=13 (deterministic) — as the primary safety net; they already caught
  nothing-changed for Stage 2.1.

In short: until #1/#3 land, read "Jazz ≤ 7" as "clean 353/353 Jazz regen yields the
known 7-case identity set," with Baroque=13 and zero snapshot diffs as the
load-bearing gates. The historical "7"s (Gate R `cc_gate_r_report.md`, and every
stage since) were **single, un-multi-sampled** measurements; this is the first
multi-sample, and it shows the clean number is deterministic — the gate's intent is
sound, only its *operationalization* (raw integer off a shared dir) was fragile.

---

## 7. Stop-condition / integrity check

- Mechanism is M3, established by **positive reconstruction** (not a guess): M1 and
  M2 are independently falsified, and injecting Baroque files reproduces 7→8→9.
- **No Baroque gate-integrity emergency.** Baroque is deterministically 13; the
  flipping cases are Baroque *files* contaminating a Jazz *measurement*, not a
  Baroque scoring instability. Baroque's own metric does not float.

# CC REPORT — Layer-5 (function) + instruments Certification Audit, PASS 1 (blind enumerative) — EG-7 / OI-84

> **Session 2026-07-12.** First pass of the LAST audit in the dependency-ordered EG-7 plan
> (layers 1–4 certified). Protocol: `cowork_audit_protocol.md` steps P1–P4, blind (P8 first
> run). Certification is NOT granted here. **The feasibility stop FIRED** (instruction Task
> 1.4, expected): the machine-generated inventory is complete and frozen; the every-row
> dispositions (Task 2), the contract-direction check (Task 3 P3), and the behavioral
> characterization (Task 3 P4) are partitioned into the sequential sessions proposed in §5.
> This report records the frozen inventory, the population partition, the pass-1 findings
> that surfaced during tagging (a mis-tag is a finding), and the partition proposal.

## 1. Task 0 — preconditions, the register commit, and the authorized revert

- **Register commit** `bcd9645ac0` — `docs(cowork):` staged `OPEN_ITEMS.md` (Cowork's edits, not
  opened) + force-added `cc_instruction_l5_audit_pass1.md`. Working tree afterward: the known
  carry `cowork_joint_key_chord_design.md` + untracked scratch only (as expected).
- **Authorized revert** `940632ecd1` — `git revert --no-edit 55829ebe15` (register row OI-110,
  user-decided). Build green; **composing_tests 1101/1101 pass**, **notation_tests exit 0**,
  **pipeline_snapshot_tests exit 0**.
  - **⚠ DEVIATION-FROM-DESCRIPTION (surfaced, not a stop):** the instruction's verification step
    says "confirm the revert touched exactly those two files" (chordanalyzer.cpp + batch_analyze.cpp).
    The commit `55829ebe15` actually bundled **four** files — the two production files **plus two
    Python driver scripts** (`tools/audit/l4/pass1_oracle_firecount_run.py` and
    `pass1_oracle_firecount_agg.py`). `git revert --no-edit 55829ebe15` (the exact authorized command)
    reverts the whole commit, so it touched **4 files** (removed 127 lines from chordanalyzer.cpp,
    6 from batch_analyze.cpp, and deleted the two driver scripts, 236 deletions total). This is
    consistent with the stated intent "removes the oracle fire-count instrumentation" — the two
    scripts are that instrumentation's own run/aggregate drivers and have nothing left to drive once
    the C++ counters are gone (verified: both read `MU_ORACLE_FIRECOUNT` / the JSONL the reverted C++
    emitted). The command was exactly the one authorized and applied cleanly (exit 0, no conflict);
    only the post-hoc "two files" count in the instruction undercounts the reverted commit's own
    contents. Flagged here rather than treated as a hard stop.
- **Git state:** HEAD after revert `940632ecd1`; `git merge-base --is-ancestor 824c419cb9 HEAD` →
  exit 0. (No `git log` used; the revert hash was given.)

## 2. Task 1 — the machine-generated inventory (protocol P1)

Extended `tools/audit/gen_inventory.py` (ONE instrument, no parallel script) with `--layer l5`.
Two extensions:

- **A second scope root beside `src/composing`: the instruments under `tools/`.** Enumeration
  domain (mechanical + total, P1): top-level tracked `tools/*.{py,cpp,json}` + `tools/tests/*.py`.
  The audit's own artifact / committed-reference / fitted-data subtrees (`tools/audit/`,
  `tools/robust_stop/`, `tools/calibration_maps/`, `tools/reports/`, `tools/fonttools/`,
  `tools/jsdoc/`, gitignored corpora) are excluded with a documented reason — instrument OUTPUTS,
  not instruments under audit. (git pathspec `*` spans `/`, so the depth filter is in Python.)
- **A Python `ast` extractor** for the Python instruments (the C++ scan is unchanged for
  `.cpp/.h`). Rows: functions / literals (trivial 0/1 excluded) / branches / class-body fields /
  internal-module imports (the dependency edges) / **file-IO** (`open`/`json.load`/`json.dump`/
  `glob`/`read_text`/`write_text` — the instrument's read/write surface, per the instruction).
  Python is PARSED, not regex-scanned → the extraction is exact (#19 establishment), no parse
  failures across the 13 instruments.

**Prior-layer byte-identity preserved:** re-generating `--layer l4` into a scratch dir reproduces
every committed l4 CSV + `inventory.json` byte-for-byte; the manifest differs only in the
self-referential `script_blob_sha` and the `head_commit` stamp (both expected). The
`extraction_method` string and the new `io` total are l5-conditional for exactly this reason.

### Inventory totals (manifest `tools/audit/l5/manifest.json`, HEAD `940632ecd1`, corpus `c50002fee1`)

| | count |
|---|---|
| tracked files in scope | **351** (216 `src/composing` + 135 `tools/` instruments domain) |
| file-table rows | 351 (totality holds: Σ tag_counts = file_table_rows = 351) |
| deep-audited files | **34** |
| deep rows | **3,372** (funcs 326 · literals 772 · branches 1,685 · fields 307 · decls 28 · crosslayer 131 · io 123) |

### The population partition (each tag verified at the code + call sites — a mis-tag is a finding)

| tag | files | deep rows | population |
|---|---|---|---|
| `L5-DORMANT` | 20 | 815 | (b) the dormant-but-surviving resolver pipeline — `function/` (9 pairs) + `progression/progressionrecognizer` |
| `INSTRUMENT` | 13 | 1,687 | the Python measurement chain |
| `INSTRUMENT-HARNESS` | 1 | 870 | `batch_analyze.cpp` — the shared harness |
| `L5-RETIRES` | 3 | 0 (file-level note) | (a) legacy competition + the live circular cadence detector |
| `L5-MIXED` | 2 | 0 (file-level note) | (a) `sectionanalyzer.{h,cpp}` — L3-audited; L5 cadence/pivot part retires |
| `DEFERRED` | 4 | 0 | already L3-audited substrate (`localmodulationdetector`), or L6 (`groupinglayer`) |
| `INSTRUMENT-MANIFEST` | 1 | 0 (file-level) | `param_manifest.json` — the fit manifest |
| `INSTRUMENT-TEST` | 5 | 0 (file-level) | `tools/tests/test_*.py` — the instrument regression tests |
| `NON-INSTRUMENT` | 115 | 0 | tools/ scripts/registries/configs NOT in the measurement-chain import closure |
| (`src/composing` out-of-scope: L1 11 · L2 2 · L3+ 170 · RETIRES 4) | | | prior/other-layer scope |

The `INSTRUMENT` set is the **import closure** of the named entry points (the regression stops,
the corpus generators, the GT parser, the fitting), verified by chasing `import`s:
`compare_analyses` + `dcml_parser` at the base; then `compare_rn`, `characterise_bir_false`,
`a8_rebaseline_measure`, `robust_stop_diff`, `run_bach_preset`, `analyze_inversion_errors`,
`music21_batch`, `oracle_root_metric`, `calibration_fit` / `c1_reliability` / `stage5_fit_driver`
(fitting). Plus `batch_analyze.cpp` (harness) and `param_manifest.json` (fit manifest).

## 3. Pass-1 findings that surfaced during tagging (verified at code — provisional, blind)

These are the "a mis-tag is a finding" outputs of Task 1. They are recorded as candidate register
rows in §7 (Task 5) and are **provisional** until the deep dispositions confirm them.

- **F-L5-1 — `harmonicfunctionlayer.{h,cpp}` is mis-located in the layer taxonomy (a population
  mis-tag).** The tag inherited from the L1/L2 file table is "function layer (L5) — deferred to the
  L5 audit". Verified at the file header (`harmonicfunctionlayer.h:23-53`): it is the **legacy
  Layer-4 chord-competition pipeline** — *"Competition pipeline — the SINGLE owner of winner
  selection"*; `applyHarmonicFunction` applies the progression signals, runs the per-bass/cross-bass
  competition, and selects the winner (LIVE via `chordanalyzer`/`regionanalyzer`). Its functional
  labeling is *"E4 (planned)"*, never built. It is on the retirement map as **R1** (legacy
  competition) + **R7** (rename), NOT surviving L5. Corrected here to `L5-RETIRES` (file-level
  interpretation-check note only). Consequence: it fell in a **taxonomy gap** — deferred out of the
  L4 audit as "L5", but it is L4-legacy, so no audit deep-covered it; this audit records the
  interpretation-check note for its R1/R7 deletion.
- **F-L5-2 — Layer 5 has no pure "(c) LIVE-and-surviving" population; the live function-layer
  production code is entirely on the retirement map.** The only LIVE Layer-5 production code is the
  key-dependent (circular) cadence + pivot detection (`detectCadences`/`detectPivotChords` in
  `sectioncadencedetection.cpp` + `sectionanalyzer`), reached from the notation bridge
  (`notationcomposingbridge.cpp`) — and it is the **R2** retirement target (the L6 grouping layer
  is its forward-only rebuild). So the surviving function machinery is 100% **dormant**
  (`L5-DORMANT`), and the live function machinery is 100% **retiring**. This is not a defect — it is
  the structural shape of the engagement (replace the live legacy with the dormant resolver) — but
  it is worth stating because the instruction's three-population frame presumed a live-and-surviving
  (c) slice that, for L5, is empty.
- **F-L5-3 — `param_manifest.json` coverage of L5 is an open establishment question (deferred to
  the deep pass).** The fit manifest is the ledger the constants ESTABLISHED/UNFIT/DEAD check reads
  (CLAUDE.md). The 815 dormant-resolver rows include ~183 numeric literals; whether the manifest
  covers the L5 constants (or whether they are hand-set / firewall-deferred per the design's
  "build it right, do not tune it") is a Task-2 establishment check, flagged not yet done.

## 4. Retiring / mixed code — the file-level interpretation-check notes (Task 1.2)

For each `L5-RETIRES` / `L5-MIXED` file, the embedded interpretation that must be consciously kept
or rejected when it is deleted (no deep rows):

- `function/harmonicfunctionlayer.{h,cpp}` (R1/R7): the **SOLE owner of winner selection + the
  application of every progression signal** (rootContinuity, w_seq, w_dim, step bonuses). Its
  deletion re-homes winner selection into the dormant decoder (L4) — the L5 audit records that this
  is where competition physically lives, so its retirement is joint with the L4 decoder engagement.
- `section/sectioncadencedetection.cpp` (R2): the **cadence-type + pivot-chord interpretations** the
  live circular detector emits to the notation bridge (the ★ borrowed-chord/pivot/cadence markers at
  key-confidence ≥ 0.8). L5's dormant `functioncadence` (key-agnostic) + L6 grouping must be
  confirmed to cover or consciously reject each before deletion.
- `section/sectionanalyzer.{h,cpp}` (L5-MIXED): its L5 content (the `detectCadences`/
  `detectPivotChords` surface) is the same R2 live detector; its L3 key-stabilization content was
  already audited by the L3 audit. Deep rows are NOT re-generated here (the L3 inventory holds this
  file's rows — #6 no-duplication); only the L5-part interpretation note is recorded.

## 5. The feasibility stop and the proposed session partition (Task 1.4)

**The stop fired.** 3,372 deep rows across 34 files exceeds a single session's rigorous-disposition
budget (P2's four standing questions + premise labels + the P3 contract direction + P4 fire
rates/establishment). Calibration: the L4 pass-1 required **three** partition-sessions for ~2,121
rows (its satellites session alone dispositioned 699). No silent sampling; the complete inventory is
frozen and the machine-readable partition is `tools/audit/l5/pass1_partition.json`.

Proposed partition (matching the instruction's own suggestion — dormant resolver / live function
path / instruments — refined by row balance):

1. **Partition 1 — the dormant resolver pipeline** (`L5-DORMANT`, 20 files, **815 rows**). The
   engagement's clean target. Per the instruction, attend to what each module **reads from the
   carry** (the L4 abstentions/alternatives/confidence + open-question label; the L3 key
   alternatives) and what it **emits** — the engagement stands on exactly those surfaces.
   Production fire rate is zero by construction; characterize via the test suites (P4).
2. **Partition 2 — the Python instrument chain** (`INSTRUMENT`, 13 files, **1,687 rows**). P2 in its
   establishment form (#19): what each instrument claims to measure, what oracle/derivation
   validates it, what is stamped (corpus hash / commit) and what is not, what would break silently;
   the `l5_io.csv` read/write surface is the seam. **May itself need a two-way sub-split**
   (regression-stop core vs grading + fitting — the split is recorded in the partition JSON).
   Characterize by running the instruments read-only against their own committed reference
   artifacts (the regression-stop pair, the corpus validators).
3. **Partition 3 — the shared harness** (`batch_analyze.cpp`, **870 rows**). Establishment + the
   diagnostic-flag surface (`--decode-chords`/`--section-level`/`--diagnose-measures`/
   `--dump-regions`) + the reads (score) / writes (`.ours.json`) surface.

The **live/retiring function path** (populations a/c) is the file-level interpretation notes of §4 —
light, no deep rows — folded into whichever session opens Partition 1.

## 6. Behavioral characterization (Task 3 / P4) — not run this session

The feasibility stop deferred Task 3 with the dispositions. Recorded expectation for the deep
passes: the dormant resolver's production fire rate is **zero by construction** (no non-test caller;
`batch_analyze --decode`/diagnostic only) — it will be characterized via the test suites. The
instruments are characterized by RUNNING them read-only against their committed reference artifacts.
The live retiring cadence detector (`detectCadences`) has a real production fire rate (notation
bridge), measurable if its retirement note needs it.

## 7. Register + unblind (Task 5)

**Withheld files first opened — all AFTER the Task-4 freeze commit `0382c3275e` (the blinding
boundary held):** `OPEN_ITEMS.md`, `DEFECT_TYPES.md`, `STATUS.md`, `cowork_handoff.md` (2026-07-12,
Task 5). The one declared-safe exception `cowork_layer5_function_design.md` (the signed layer
contract) was read at session start per the instruction. No other withheld file
(`cc_*_report.md`, the `cowork_*` audit-era docs, the `tools/audit/**` dispositions/blind/sweep
artifacts) was opened — the blind inventory + findings (§1–§6) were fixed before this section.

**Register outcomes (`OPEN_ITEMS.md`, same commit as this report):**
- **OI-110 → ✅ CLOSED** with the revert commit `940632ecd1` (the deviation-from-description on the
  4-vs-2 file count recorded in the row + §1 here).
- **OI-116 (new)** — the L5 pass-1 feasibility stop + the 3-way partition + the owed deep passes /
  pass-2 sweep + the `param_manifest.json` L5-coverage establishment check (F-L5-3, DT-2). The
  OI-102 analog.
- **OI-117 (new)** — F-L5-1 the `harmonicfunctionlayer` mis-tag (**DT-21**, same family as OI-101's
  chordpathdecoder/sparsechordrefinement) + F-L5-2 the no-live-surviving-L5 structural observation.
- **OI-84 (audit plan)** — updated to record L5 pass-1 Task-1 done + the feasibility stop.

**New defect TYPE promoted into `DEFECT_TYPES.md`:** none. Every pass-1 finding maps to an existing
type — F-L5-1 is **DT-21** (layer mis-attribution in the tag table), F-L5-3 is **DT-2** (constant
establishment, deferred). F-L5-2 is an informational structural observation, not a defect type. The
instrument-specific type surface (if any) will emerge in the deep instrument passes (partition 2/3),
not in this inventory-only freeze.

**Certification:** NOT proposed. Only pass-1 Task 1 (the inventory) is complete; the deep
dispositions (Tasks 2–3, partitioned) and the pass-2 signature sweep are owed. When they complete
and pass, the OI-84 certification plan — and with it the whole dependency-ordered EG-7 plan — is done.

## 8. Self-check (CLAUDE.md, run over the actual diff before reporting done)

Re-read every touched file's diff against the guiding principles / conventions / gate policy /
DEFECT_TYPES:
- **#8 (no inference-problem coding):** the only code change is the authorized Task-0 revert (removes
  instrumentation); the inventory work is refactoring/tooling. No inference logic touched. ✓
- **#6 (no duplication):** ONE instrument extended (`gen_inventory.py`), not a parallel script; the
  Python extractor is a second language front-end sharing the row schema; L3-audited files
  (`localmodulationdetector`) and L3-inventoried mixed files (`sectionanalyzer`) are DEFERRED/note-only,
  their rows not re-generated. ✓
- **#7 / auditor-not-amender:** no fix applied to any discovered issue; findings → register rows only. ✓
- **#16 reproducibility:** manifest stamped (HEAD `940632ecd1`, corpus `c50002fee1`, script blob sha);
  prior-layer byte-identity re-proven. ✓
- **#19 establishment:** Python parsed (ast), not regex-guessed; the instrument set is the mechanical
  import closure, not hand-picked; the tools/ enumeration domain is total with a documented exclusion. ✓
- **Conventions — no self-invented jargon:** tags follow the existing audit tag-scheme pattern
  (L4-SCORER/L4-DECODER/... → L5-DORMANT/L5-RETIRES/INSTRUMENT/...); reasons cite real repository
  names (`harmonicfunctionlayer.h:23`, R1/R2/R7, §5.2, `notationcomposingbridge.cpp`). ✓
- **Shell rules:** `; echo "exit:$?"` on fallible commands; large output redirected to files. ✓
- **Git rules:** files staged by name (never `git add -A`); `git status` after each commit; the carry
  `cowork_joint_key_chord_design.md` left untouched; `cc_*.md` force-added in the fold. ✓
- **Push rule:** `origin` only, `upstream` push disabled (verified `git remote -v`). ✓

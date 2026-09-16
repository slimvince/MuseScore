# CC Instruction — Foundation Stage 0: restore a buildable, baselined HEAD (preserve WIP; back out the build break)

> **Context.** Committed HEAD `0b42096d75` cannot build the BIR harness — `batch_analyze.cpp` references
> `seqPrefs.tpcKeyFitWeight`, whose definition is only in your uncommitted WIP (the half-and-half `--seq-tpc-weight`
> commit at `5f6b9828a5`). Cowork verified this at the committed objects. This stage makes HEAD build again and locks
> the **true** clean baseline, **without discarding any WIP** — the ~2457-line WIP is triaged hunk-by-hunk in Stage 2,
> so every line of it must be **preserved** here. Decisions already made by the user: back out the consumer (not commit
> the orphaned member); the tpc feature stays deferred to Phase 4b.
>
> (CLAUDE.md bash rules: append `; echo "exit:$?"`; redirect large output to a file, read a slice. Build via
> `setup_and_build.bat` through PowerShell.)

## §0 — Preserve the entire WIP (discard NOTHING)
1. Report your tree state: `git status` and `git diff --stat` (and `git diff --cached --stat`). List the modified
   tracked files and the line count.
2. **Back it up two ways** before touching anything (this is the Stage-2 material — losing it is unacceptable):
   - a **combined patch**: `git diff > foundation_wip_combined.patch` (and `git diff --cached >> ...` if anything is
     staged);
   - **per-file patches** under `foundation_wip/` (one `.patch` per modified file) — Stage 2 examines hunks per file;
   - then **`git stash push -u -m "foundation WIP — preserved for Stage-2 hunk-by-hunk triage"`** so the working tree
     is clean. Record the **stash ref** and the patch paths in the report. (Both the stash and the patches are kept;
     belt and suspenders.)
3. Confirm `git rev-parse HEAD == 0b42096d75` and the tree is now clean.

## §1 — Back out the orphaned consumer (the decided build-break fix)
- Edit `tools/batch_analyze.cpp` to remove **every** `--seq-tpc-weight` / `tpcKeyFitWeight` reference (help text
  ~1761–1765, the arg match ~2524, the `seqPrefs.tpcKeyFitWeight = …` assignment ~2549, and anything else `git grep`
  shows). Confirm `git grep -n 'tpcKeyFitWeight\|seq-tpc-weight'` is **empty across the whole committed tree** afterward.
- This is **behaviour-neutral**: the flag was decode-only and defaulted to `0.0`, so no production path used it —
  confirm there is no other use. **Do not** add the member, **do not** touch `keymodesequence.*` (that hunk stays in
  the preserved WIP, classified discard in Stage 2).
- Commit **locally, unpushed**: `fix(tools): back out orphaned --seq-tpc-weight consumer — restore buildable HEAD (tpc deferred to Phase 4b)`.

## §2 — Build and lock the true baseline
- **Build.** Confirm it now **compiles** — including `batch_analyze`. **If the build fails for any reason other than
  the consumer you just removed → STOP and surface**: that is a *second* half-committed dependency on the WIP, which
  changes the picture.
- `composing_tests` (expect 624), `pipeline_snapshot_tests` (expect 11/11), `notation_tests` (report pass/fail **and
  the exact failing test names** — expect the 5 known: MozartK279, Corelli, PopulateCadence, HarmonyPinning RN +
  Nashville).
- **Canonical BIR**, all three presets, with the gate's own tool:
  ```
  python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
  python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque
  # …Jazz, …Default likewise
  ```
  Report, per preset, the **count AND the case-identity set** (stem@tick). (Cowork verifies these and uses them to
  correct CLAUDE.md's stale `57/23/57` tables to the real `53/24/53`.)

## §3 — Deliverable
`cc_foundation_stage0_report.md` (gitignored): §0 tree state + WIP backup location + stash ref; §1 the backout commit
hash + the empty-grep confirmation; §2 build-compiles result (+ any other dangling dependency found), the three suites
(with notation failing names), and the canonical BIR counts + case sets for all three presets.

## §4 — Constraints & stop conditions
- **Preserve the WIP** (stash + patches) — it is **never** dropped or discarded here; Stage 2 triages it hunk-by-hunk.
- **Do not triage/dispose any WIP hunk** beyond removing the committed consumer — no committing kept hunks, no
  reverting others (that is Stage 2). **Do not** refresh any golden or touch the 5 notation failures (that is Stage 3).
- Local commit only; **`origin` push is held** until the foundation is ratified clean; **`upstream` never**.
- Build fails for a reason other than the removed consumer → STOP (a second half-committed dependency).
- You start disposing WIP hunks, or fixing notation/goldens → STOP (Stage 2 / Stage 3).

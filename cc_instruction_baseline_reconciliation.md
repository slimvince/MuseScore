# CC Instruction — baseline reconciliation at committed HEAD (read-only / measurement; gates Phase 2)

> **Why.** Phase 1a is verified clean (commit `0b42096d75` = `note_model.{h,cpp}` + tests only; byte-identical). But
> your report read **BIR 53/24/53** and **5 failing notation tests**, attributed to "held WIP / Cowork's uncommitted
> changes." Cowork checked the repo: `git diff` and `git diff --cached` are **both empty** — there is **no uncommitted
> WIP** to blame, and none of Cowork's work this session was code (docs only). So whatever you measured is the state of
> **committed HEAD itself**, and it disagrees with the documented baseline (CLAUDE.md: **57 / 23 / 57**, both suites
> green). That gap is **not** a Phase-1a effect and must be reconciled **before Phase 2 builds on it.**
>
> **This is read-only diagnosis: measure and localize, fix NOTHING.** No code change, no commit, no golden refresh, no
> push. (CLAUDE.md bash rules: append `; echo "exit:$?"`; redirect large output to a file and read a slice.)

## §0 — Confirm you are measuring a CLEAN committed HEAD (the critical first step)
- In **your own environment**, run `git status` and `git diff --stat` (+ `git diff --cached --stat`). Report exactly
  what is uncommitted, if anything.
- If your working tree is **dirty** (any uncommitted change to a tracked file — e.g. `keymodesequence.*`,
  `keymodeanalyzer.h`, `localmodulationdetector.*`, `regiontoneprimitives.cpp`, `batch_analyze`), then your earlier
  "baseline" was measured on that dirty tree. **Stash it** (`git stash`) so HEAD is clean, and record the stash. All
  measurements below must be on **clean `0b42096d75`**.
- Confirm `git rev-parse HEAD` == `0b42096d75` and the tree is clean before building.

## §1 — Build clean HEAD and run both test suites
- Build (`setup_and_build.bat` via PowerShell).
- `composing_tests.exe` — report the count (expected 624 after Phase 1a).
- `notation_tests.exe` — report pass/fail and, if any fail, the **exact failing test names**. The question: are there
  **really 5 failures at clean HEAD**, or 0? If they fail, name them (you cited Mozart/Corelli implode + 2
  harmony-pinning snapshots).
- `pipeline_snapshot_tests.exe` — report pass/fail (no `--update-goldens`).

## §2 — Measure the BIR at clean HEAD with the CANONICAL tool (per CLAUDE.md), all three presets
Use the **gate's own tool**, not a side metric, so the number is comparable to the documented 57/23/57:
```
python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque
python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz
python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz
# Default (the user-run config):
python tools/run_bach_preset.py --preset Default --output-dir tools/corpus/default
python tools/characterise_bir_false.py --corpus-dir tools/corpus/default
```
Report, per preset: the **BIR=false count** AND the **case-identity set** (stem@tick) — the gate is the case set, not
the integer. Compare against CLAUDE.md's documented sets (Baroque 57 / Jazz 23 / Default 57).
- **If the canonical tool gives 57/23/57** → the earlier "53/24/53" was a *different metric or a dirty-tree reading*;
  say which tool produced 53/24 and confirm clean HEAD matches the docs. **Likely the simplest resolution.**
- **If the canonical tool gives 53/24/53 at clean HEAD** → the documented baseline is wrong *or* a committed change
  moved production. Proceed to §3.

## §3 — Localize a real delta (ONLY if §1/§2 differ from the documented baseline)
Do **not** bisect pre-emptively. If and only if clean HEAD genuinely differs from 57/23/57-green, find where it
entered by measuring the same canonical BIR + notation suites at the prior commits, newest first, stopping at the
first that matches the docs:
- `5f6b9828a5` (L4 Increment B), `48909fb752` (L4 Increment A) — both claimed *isolated / production byte-identical*;
- `a6b08af3fe` (L3 wiring) — the last production-key change, where 57/23/57 was documented (`9b643a454a`).
Report which commit first shows the delta — i.e. whether a supposedly-byte-identical isolated commit actually moved
production output, or the docs were stale from the L3-wiring point. Restore HEAD to `0b42096d75` afterward.

## §4 — Verdict (the reconciliation)
State plainly, with the measured numbers:
- clean-tree confirmation (and whether a stash was needed);
- both-suites result at clean HEAD (composing count; notation pass/fail + any failing names; snapshots);
- canonical BIR per preset (count + case set) vs the documented 57/23/57;
- the resolution, exactly one of: **(a)** docs match reality, baseline clean, the 53/24 was a side-metric/dirty-tree
  artifact → **proceed to Phase 2**; **(b)** docs are stale → CLAUDE.md's gate numbers need correcting (a doc fix, in
  the proper place, ratified by the user) before Phase 2; **(c)** a committed regression localized to commit X → a
  real fix in that layer before Phase 2.
- A recommendation; **do not act on (b)/(c)** here — surface for Cowork + user.

## §5 — Constraints & stop conditions
- **Read-only / measurement only.** No code edit, no golden refresh, no commit of code, no push. The corpus regen
  under `tools/corpus/` is the tool's normal output (it clean-slates per preset) — that is fine; do not commit it.
- The Phase-1a commit `0b42096d75` stays as-is and **unpushed**.
- Any stashed WIP from §0 is **restored or left stashed and reported** — never discarded.
- You start *fixing* anything (code or goldens) → STOP (diagnosis only; the fix is the next, gated step).
- A push would target `upstream` → STOP.

## §6 — Deliverable
`cc_baseline_reconciliation_report.md` (gitignored): §0 tree state, §1 suites, §2 canonical BIR (counts + case sets,
all three presets), §3 localization (if run), §4 verdict + recommendation.

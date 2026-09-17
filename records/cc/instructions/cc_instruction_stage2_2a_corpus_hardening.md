# CC Instruction: Stage 2.2a — Corpus-measurement hardening (M3 fix) + bookkeeping commit

## Context

Implements the fix design from `cc_jazz_nondeterminism_report.md` (roadmap **2.2a**,
inserted before 2.2). M3 recap: shared `tools/corpus` + FAILED-worker stale files +
`skip_cpp` reuse + no preset guard in `characterise_bir_false.py` ⇒ silently mixed
corpora. The fix makes contamination structurally impossible AND loudly detected.
**Tooling-only: metric DEFINITIONS unchanged** (alignment/classification logic in
`compare_analyses.py` / `compare_rn.py` untouched). Base: `8598cbd245`.

Standing rules apply (handoff): never guess; pin behavior with tests; explicit staging.

**Authorized files:** `tools/run_bach_preset.py`, `tools/characterise_bir_false.py`
(plumbing only — argument/validation code, NOT classification logic), other
`tools/run_*_validation.py` ONLY if they share the same output-dir pattern (survey
first; if touching them balloons the scope, document and defer), `tools/tests/**`,
CLAUDE.md + `build_and_test.md` (command sync), and the bookkeeping docs in Task 4.

## Task 1 — Design + survey

Target design (adjust only with stated reasons):
1. **Per-preset corpus dirs**: `tools/corpus/baroque/` and `tools/corpus/jazz/`
   (replacing the shared flat `tools/corpus`). Both can exist side-by-side — this also
   halves regen cost for both-preset checks (relevant for 2.2/Stage 5).
2. **Stamp + completeness validation**: `run_bach_preset.py` writes a
   `corpus_manifest.json` into the output dir (preset name, score count, per-score
   status, timestamp, batch_analyze identity if cheaply available e.g. mtime/size).
   On ANY `FAILED`/skip the run must say so prominently and exit nonzero (fail-loud);
   stale-file reuse paths (`skip_cpp`, FAILED early-return) must never leave a file
   from another preset countable — survey how to guarantee that (clean-slate the dir
   at regen start unless an explicit `--resume` is passed is acceptable).
3. **`characterise_bir_false.py --corpus-dir <dir>`** (with a sensible default), which
   VALIDATES the manifest: preset present, count complete (353/353), refuses to run on
   a manifest-less or incomplete dir (clear error). No classification-logic changes.
4. Survey `run_*_validation.py` + any other consumer of `tools/corpus` (grep) so no
   workflow silently breaks; report what you find before deciding their treatment.

## Task 2 — Implement + test

- Implement per the design. Extend `tools/tests/` to pin the NEW validation behavior:
  manifest written + validated, fail-loud on incomplete corpus, refusal on
  preset-mismatch (a synthetic contaminated-dir fixture — the M3 scenario must now
  produce an ERROR, not a wrong number). Existing 54 tests must stay green (adjust
  only those that constructed corpus dirs, and only mechanically).
- Update the commands in CLAUDE.md (the corpus-check section) and `build_and_test.md`
  to the new dirs/flags. Quote both diffs in the report.

## Task 3 — Full verification

```
cd C:\s\MS && python -m unittest discover -s tools/tests -p "test_*.py" > /tmp/s22a_py.txt 2>&1; echo "exit:$?"
tail -3 /tmp/s22a_py.txt
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque > /tmp/s22a_b.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz > /tmp/s22a_j.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque > /tmp/s22a_bir_b.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s22a_bir_b.txt
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz > /tmp/s22a_bir_j.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s22a_bir_j.txt
```
Required: Baroque **13** and Jazz **7** with the known identity sets (Jazz:
{bwv244.15, 245.17, 245.40, 422, 432, 45.7, 74.8}) — print and compare the identity
lists, not just totals. Plus one deliberate contamination probe: copy a Baroque file
into the jazz dir → characterise must ERROR (manifest mismatch), then restore.
No C++ build needed (no C++ change — confirm with `git status`).

Decide and document the fate of the old flat `tools/corpus/` (delete? leave with a
README breadcrumb? — pick one, justify; remember it's gitignored either way).

## Task 4 — Commits (two, then done)

- **Commit 1 (tooling):** `tools: per-preset corpus dirs + manifest validation
  (Stage 2.2a — M3 fix)` — run_bach_preset/characterise plumbing + tests +
  CLAUDE.md/build_and_test.md sync. Await Cowork confirmation before committing.
- **Commit 2 (bookkeeping docs, immediate, no confirmation needed):**
  `docs: session bookkeeping — Stage 1 completion, Stage 2.1, M3 investigation` —
  staging exactly: STATUS.md, COWORK_HANDOFF.md, docs/implementation_roadmap.md
  (the accumulated uncommitted updates; sanity-check coherence, don't rewrite).

## Report — `cc_stage2_2a_report.md`

Design decisions + deviations; survey of other corpus consumers; new-test inventory;
the verification table incl. both identity sets and the contamination-probe error;
CLAUDE.md/build_and_test.md diffs; old-dir disposition; commit hashes/proposal.
Interim-gate retirement: state explicitly that with the manifest validation in place,
"Baroque ≤ 13 / Jazz ≤ 7" regain their plain meanings (the Stage-2.1 interim wording
can be retired — Cowork will update the handoff).

Stop conditions: anything requiring a change to classification logic; a
`run_*_validation.py` survey result that makes the scope balloon; identity sets that
do NOT match the documented ones on a clean regen (that would be a NEW finding —
stop and report).

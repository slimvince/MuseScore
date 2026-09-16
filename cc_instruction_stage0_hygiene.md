# CC Instruction: Stage 0 — Hygiene and Honest Ground Truth

## Context

First step of the consolidated master plan: **read `docs/implementation_roadmap.md` first**
(Stages 0–7; this instruction implements Stage 0, items 0.1–0.6). Also read STATUS.md header
and `docs/scoring_model.md` (you will edit it — sync rule applies).

**Hard constraint for the entire instruction: zero behavior change.** Every code-touching
item must be byte-identical: 416/416 · 52/52 · 11/11, zero snapshot diffs, BIR=false
Baroque ≤ 13 / Jazz ≤ 7 (regenerate both presets; restore `tools/corpus/` to Baroque state
afterwards).

Worktree: `C:\s\MS` (master). Base: `e7d4ba2b1a`. The working tree has uncommitted doc
edits from planning sessions — these are expected and are committed as part of Task 1.
**Never stage the `muse` submodule.** Use explicit per-file `git add` only; no `git add -A`.

---

## Task 1 — Doc pass + doc commit (roadmap 0.1)

1. Find stale references that describe `explorationMode` as a live mechanism (it was
   replaced by `fn::ScoringPhase` in `e7d4ba2b1a`):
   ```
   grep -n "explorationMode" ARCHITECTURE.md docs/layer_architecture_audit.md docs/*.md | head -40; echo "exit:$?"
   ```
   Do NOT trust remembered line numbers — the files have shifted. Update each hit that
   presents explorationMode as current (rewrite to ScoringPhase or mark as historical).
   Leave genuinely historical narrative (e.g. "the former explorationMode flag") intact.
2. Review the uncommitted doc edits with `git diff <file> | head -…` per file:
   `ARCHITECTURE.md`, `CLAUDE.md`, `COWORK_HANDOFF.md`, `STATUS.md`,
   `docs/redesign_plan.md`, `docs/scoring_model.md` (if dirty). These are planning-session
   updates (architecture review addendum, §2.14 reconciliation, roadmap wiring, status
   entries) — sanity-check they are coherent, do not rewrite them.
3. Stage and commit the documentation set in ONE commit:
   - the files above (current state, including your Task-1 stale-ref fixes)
   - `docs/layer_architecture_audit.md` (currently untracked — must be committed)
   - `docs/implementation_roadmap.md` (currently untracked — must be committed)
   - Do NOT include: `muse`, `tools/dump_bir_cases.py` (separate concern), anything in
     `ai-assistant/`, any `cc_*.md` / `cowork_*.md` working files (gitignored or
     intentionally uncommitted).
   Proposed message:
   ```
   docs: consolidated roadmap + architecture-review updates (Stage 0.1)

   Add docs/implementation_roadmap.md (master plan, Stages 0-7) and commit the
   previously untracked docs/layer_architecture_audit.md. Record the 2026-06-10
   architecture reviews in redesign_plan.md (decode-target addendum) and
   ARCHITECTURE.md §2.14 (lattice reconciliation). Update stale explorationMode
   references to ScoringPhase post-e7d4ba2b1a. STATUS/COWORK_HANDOFF session log.
   ```

## Task 2 — Delete repo junk (roadmap 0.4)

Untracked junk to delete from the repo root (careful shell quoting — the first filename
contains spaces, parens, and a leading `s `):
- `./'s -ExecutionPolicy RemoteSigned) ; (& c:sMS.venvScriptsActivate.ps1)'` (mangled
  PowerShell artifact)
- `C:tmpbuild_out.txt` (literal filename in repo root)

```
cd C:\s\MS && ls -la | grep -i -E "ExecutionPolicy|tmpbuild"; echo "exit:$?"
```
Delete them (`rm -- '<exact name>'`), then verify `git status --porcelain` no longer shows
them. Leave `ai-assistant/` untouched. No commit needed (they were untracked).

## Task 3 — Remove dead fnCtx fields (roadmap 0.2)

`HarmonicFunctionContext.keyFifths` / `keyMode` are write-only (documented dead at
`chordanalyzer.cpp:~2935–44`). Remove:
1. The two fields from `HarmonicFunctionContext` (`harmonicfunctionlayer.h`).
2. The two writes + the "DEAD (write-only)" NOTE comment in `chordanalyzer.cpp`.
3. Check tests/other files for references first:
   ```
   grep -rn "fnCtx.keyFifths\|fnCtx.keyMode\|\.keyFifths\b" src/composing | head -20; echo "exit:$?"
   ```
   (Distinguish from other structs' legitimate `keyFifths` fields — only the
   `HarmonicFunctionContext` members go.)
4. Key influence reaches the function layer via `snapshot.scale`/`keyTonicPc` (frozen into
   `basisIndep`) — confirm no other consumer expected these fields.

## Task 4 — `kTemplateCount` shared constant (roadmap 0.3)

Eliminate the silent stack-overrun class: all template-sized arrays must derive their size
from ONE constant.

1. Define once, visible to both files (suggest `chordanalyzer.h`, near the template-related
   declarations; `harmonicfunctionlayer.cpp` sees it via its include of `chordanalyzer.h`):
   ```cpp
   inline constexpr std::size_t kTemplateCount = 17;
   ```
   Choose the namespace deliberately (`analysis` vs `function`) and document why.
2. Replace the literal 17 at all five sync sites (scoring_model.md §9 list):
   - `analyzeChord` `std::array<TemplateDef, 17>`
   - `kDiagTemplates` in `diagnoseChord`
   - the three score matrices (`basisIndepMatrix`, `complexityFactorMatrix`,
     `augFactorMatrix`) — inner array extent
   - `kMasks` `std::array<uint16_t, 17>` in `harmonicfunctionlayer.cpp`
3. Add `static_assert`s where cheap (e.g. `kMasks.size() == kTemplateCount` is implicit via
   the type; assert the two TemplateDef arrays agree if they are separate declarations).
4. **Sync rule:** update `docs/scoring_model.md` §3 ("Atomic update requirement") and §9
   step 5 to say sizes derive from `kTemplateCount` — adding a template now means updating
   the constant + the entries, and the compiler enforces array sizes.

## Task 5 — FP tie policy documentation (roadmap 0.5)

Add a short section to `docs/scoring_model.md` (suggest after §3) documenting:
- Winner selection uses exact `double` comparisons; ties broken by `tiePriority`
  (template index) then `rootPc` — deterministic given identical FP evaluation.
- No epsilon is used anywhere in ranking — intentional (state it).
- Fragility caveat: documented near-tie cases (e.g. the Δ=+7b 0.02-margin class, bwv320
  1.92 vs 1.90) could flip under FP re-association (compiler flags, platform, reordered
  arithmetic). Any change to optimization flags or evaluation order requires a full corpus
  A/B.
Doc-only; no code change. (A tie-stability *test* is Stage 1.7 — not this instruction.)

## Task 6 — Document divergences (roadmap 0.6) — comment/doc only

1. `onsetBoundaryThreshold`: batch (`tools/batch_analyze.cpp`) hard-codes 0.25; bridge reads
   `IComposingAnalysisConfiguration`. Add a comment at the batch site stating the divergence
   and that batch corpus numbers assume 0.25. Do NOT unify behavior (Stage 2 territory).
2. Region-collapse duplication: `regionanalyzer.cpp` same-root merge logic exists at two
   sites (~:497–505 main loop, ~:694–698 Pass 2 — re-grep, don't trust line numbers). Add a
   cross-referencing comment at both sites ("duplicated logic — keep in sync; see
   implementation_roadmap.md 0.6"). Extract a shared helper ONLY if the result is provably
   byte-identical and trivial; otherwise comments suffice.

---

## Task 7 — Build, test, corpus verification

Standard loop (VS Code bash rules: append `; echo "exit:$?"`, redirect large output):
```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/s0_compose.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s0_compose.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/s0_notation.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s0_notation.txt
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/s0_snap.txt 2>&1; echo "exit:$?"
tail -10 /tmp/s0_snap.txt
```
Expected: 416/416 · 52/52 · 11/11, zero snapshot diffs, no goldens refreshed.

BIR, both presets (code was touched in Tasks 3–4):
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus > /tmp/s0_bbar.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py > /tmp/s0_bir_b.txt 2>&1; echo "exit:$?"
tail -10 /tmp/s0_bir_b.txt
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus > /tmp/s0_bjazz.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py > /tmp/s0_bir_j.txt 2>&1; echo "exit:$?"
tail -10 /tmp/s0_bir_j.txt
# restore documented invariant:
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus > /tmp/s0_rest.txt 2>&1; echo "exit:$?"
```
Required: Baroque 13, Jazz 7, both unchanged.

---

## Commits

Commit 1 (Task 1): docs — message above. Commit immediately after Task 1 verification
(doc-only, no build needed).

Commit 2 (Tasks 3–6, after Task 7 passes): propose, do NOT commit until Cowork confirms.
Suggested message:
```
chore: Stage 0 hygiene — kTemplateCount, dead fnCtx fields, tie-policy docs

Derive all five template-sized array extents from a single kTemplateCount
constant (closes the silent stack-overrun class from B1; scoring_model.md §3/§9
updated per sync rule). Remove the write-only HarmonicFunctionContext
keyFifths/keyMode fields (documented dead since the Step-3 investigation).
Document the FP tie policy and the batch onsetBoundaryThreshold divergence;
cross-reference the duplicated region-collapse sites.

Byte-identical: 416/416, 52/52, 11/11, zero snapshot diffs; BIR 24/13 / 35/7
unchanged (both presets regenerated).
```
Stage files explicitly per commit. Never `muse`.

---

## Report — `cc_stage0_report.md`

1. **Doc pass:** list of stale-reference sites fixed (file + brief quote before/after).
2. **Junk deletion:** confirmation + any surprises.
3. **Dead fields:** diff summary; confirmation no other consumers existed.
4. **kTemplateCount:** placement decision + rationale; the five sites; any static_asserts.
5. **Tie policy + divergence docs:** sections added.
6. **Test/BIR results:** the full table.
7. **Deviations:** anything that didn't match this instruction's description of the code —
   report before working around it.
8. **Commit status:** commit 1 hash; commit 2 proposed (awaiting confirmation).

Stop and ask if: any test fails, BIR moves, a snapshot diffs, the stale-reference rewrite
would change a doc's *meaning* rather than its tense, or kTemplateCount placement forces an
include-direction change.

# submission-phase1 build error triage — CC prompt

Copy everything between `=== BEGIN PROMPT ===` and `=== END PROMPT ===` to CC.

---

=== BEGIN PROMPT ===

## Context

`submission-phase1` in `C:\s\MS` has a build error in
`src/notationscene/notationcontextmenumodel.cpp` — a **duplicate function
body** — that blocks a full `setup_and_build.bat` run on that branch. Test
binaries still build via `build_tests.bat`, so the error has been quietly
present; it surfaced during iter 10's Session 2 Phase 7 verification on
2026-04-24.

This session is **triage only**. `src/notationscene/` is outside the
autonomous-edit zone in CLAUDE.md (only `src/composing/` and
`notationaccessibility.cpp` are authorized). Diagnose, propose a fix,
halt — do not apply any fix without explicit approval.

## Phase 0 — Session start

1. Read `C:\s\MS\CLAUDE.md` and
   `C:\Users\vince\.claude\projects\c--s-MS\memory\MEMORY.md`.
2. Mid-write corruption sweep:
   - `git status`
   - `git diff --stat`
   - `git diff --ignore-cr-at-eol --stat`

   Working tree must be clean. If dirty, stop and report.
3. Branch state check:
   - `git rev-parse master` — record current SHA.
   - `git rev-parse submission-phase1` — record current SHA.
   - Expected starting point: master at `7554cc6583` (iter 10 finalization),
     submission-phase1 at `69ee6543fc` (iter 10 cherry-pick of Commit A).
     If either differs, stop and report before continuing.

## Phase 1 — Reproduce the failure

1. `git checkout submission-phase1`
2. Run the mid-write corruption sweep again after the branch switch.
3. `cmd.exe //c "C:\s\MS\setup_and_build.bat"`
4. Capture the full compiler error output for
   `notationcontextmenumodel.cpp`:
   - Exact error text (including `error:` / `C2xxx` codes if MSVC).
   - File path and line number of the duplicate function body.
   - Name of the duplicated function(s).
   - Any "previous definition here" pointer the compiler provides.

Record this before doing anything else — it is the factual base for the
rest of the diagnosis.

## Phase 2 — Archaeology

Determine where the duplicate came from. Work through these in order:

1. **Is it in the file itself?** Open
   `src/notationscene/notationcontextmenumodel.cpp` on submission-phase1.
   Locate both function bodies. Record:
   - Exact line numbers of both definitions.
   - Whether the bodies are identical or divergent.
   - The surrounding context of each (any `#ifdef`, namespace, or class
     scope differences).

2. **When were they introduced?** For each of the two definitions:
   - `git log -L <start>,<end>:src/notationscene/notationcontextmenumodel.cpp submission-phase1`
     (use line ranges from step 1) to get the commit history of each
     block.
   - `git blame -L <start>,<end> submission-phase1 -- src/notationscene/notationcontextmenumodel.cpp`
     for per-line provenance.
   - Record: which commit added each definition, author, date, subject
     line.

3. **Is the duplicate on master too?**
   - `git show master:src/notationscene/notationcontextmenumodel.cpp | grep -n <function-signature>`
   - If master also has the duplicate, this is a repo-wide bug that
     predates submission-phase1 branching. If master does not have it,
     something on submission-phase1's history introduced or failed to
     remove it — identify the delta.

4. **Merge/cherry-pick scar check.** submission-phase1 has been the
   recipient of multiple cherry-picks from master during iters 1–10.
   Check whether any of our cherry-picks touched this file:
   - `git log --all --source -- src/notationscene/notationcontextmenumodel.cpp | head -40`
   - Look for commits by us (iter-1..iter-10 subject lines) versus
     upstream commits. A duplicate body is a classic signature of a
     botched merge where both sides' edits got kept.

## Phase 3 — Synthesize the root cause

With Phase 1 and Phase 2 data in hand, answer:

1. **Classification.** One of:
   - (a) Predates our work on both branches — upstream MuseScore bug we
     inherited.
   - (b) Present on master but not on an earlier submission-phase1
     ancestor — introduced by one of our master commits and propagated
     via cherry-pick.
   - (c) Present only on submission-phase1 — introduced by a merge or
     cherry-pick conflict that was resolved badly on that branch.
   - (d) Something else (describe).

2. **Proposed fix.** One of:
   - Delete the older/duplicated body (identify which and why).
   - Merge the two bodies if they diverged meaningfully (identify the
     semantic delta).
   - Revert the introducing commit (identify SHA and side effects).
   - Escalate — if the fix is not obvious or touches logic you cannot
     assess safely.

3. **Blast radius.** Does the fix need to land on master, on
   submission-phase1, or both? If both, is the fix identical or do the
   branches have divergent expectations?

## Phase 4 — Report and halt

Do **not** apply any fix. Post a single report containing:

- Phase 1 reproduction: exact error text, line numbers, function names.
- Phase 2 archaeology: commit SHAs that added each definition, dates,
  subject lines, blast-radius check against master.
- Phase 3 classification + proposed fix + blast radius.
- A one-line recommended next action (e.g. "approve one-line revert of
  SHA xxxx on submission-phase1; master already clean" or "escalate —
  the two bodies diverged and choosing one risks breaking <feature>").

Return to master at the end:

- `git checkout master`
- Verify clean tree with `git status`.

Do not push anything this session. No commits.

=== END PROMPT ===

---

## Notes for me (Vincent) — not for CC

- Chose triage-only over triage+fix because `src/notationscene/` is
  outside CLAUDE.md's autonomous-edit zone. Fix goes in a separate short
  follow-up session once the root cause is known.
- Expected outcomes ranked by likelihood:
  1. Cherry-pick artifact from one of our iter-1–10 commits that touched
     the file — clean revert/fix.
  2. Upstream bug inherited on both branches — lowest effort on our end,
     just pick one body.
  3. Divergent intentional edit that got dual-kept — highest-effort fix,
     may need a conversation.
- After this triages, next candidates on the post-iter-10 list:
  - `docs/unified_analysis_pipeline.md` design note
  - 58-test composing gap audit on submission-phase1
  - Registry duplicate candidates + `home.mscz` empty-composer cleanup

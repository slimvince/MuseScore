# CC Instruction — Refactor: split regiontonecollector.cpp (byte-identical)

> **Next pure split** after refactor #1, per the Cowork-verified module-layering assessment
> (`cc_module_layering_assessment_dossier.md` §5 — `regiontonecollector.cpp` is the #1 pure-splittable
> candidate, no caveat). **STRICTLY BYTE-IDENTICAL — pure code movement, NO logic/scoring/inference change**
> (the standing rule: refactoring into layers only). **HELD for Cowork verification before commit; local,
> UNPUSHED.**

---

## §1 — The purity rule (same as refactor #1)
Only permitted edits: (a) cut a free function/helper verbatim out of
`src/composing/analysis/engravingbridge/regiontonecollector.cpp` and paste it unchanged into a new sibling
TU; (b) prefix any moved anonymous-namespace helper (internal-linkage rename ⇒ byte-identical, the
`jkd*`/`csf*` precedent); (c) register the new `.cpp` in `analysis/CMakeLists.txt`. **No logic/constant/
behavior change. Do NOT "fix" anything. The header that declares the moved functions stays unchanged** (the
stable boundary). If a move can't be byte-identical → STOP, surface (do not adapt logic).

## §2 — The split (per assessment §5)
`regiontonecollector.cpp` (891 lines) conflates the tone-collection/context **primitives** with the
`collectRegionTones` orchestrator. Move the **independent free functions** the assessment named —
`collectSoundingAt`, `buildTones`, `collectPitchContext`, the two sub-boundary detectors, `findTemporalContext`
— into a new TU (e.g. `engravingbridge/regiontoneprimitives.cpp`), leaving `collectRegionTones` as the lone
residual. **Re-confirm each moved function's call sites at source first** (via the committed object / file
reads) so nothing the residual still needs is moved out — exactly the call-site check that caught the
`coreIntervals` mis-map in #1. If any named function turns out NOT to be cleanly liftable (a shared
anon-ns helper split across the seam, or a residual dependency), STOP and surface — do not force it.

## §3 — Acceptance gate (MANDATORY — byte-identical)
1. Build green (`setup_and_build.bat`).
2. `composing_tests` + `notation_tests` pass.
3. `pipeline_snapshot_tests` 11/11 — **no `--update-goldens`** (a golden move ⇒ NOT byte-identical ⇒ STOP).
4. 3-preset corpus regen `.ours.json` **0-diff** (Baroque/Jazz/Default) + **BIR 57/23/57**.

Any deviation = STOP (a behavior change slipped in). Report the gate result.

## §4 — Deliver: COMMIT LOCALLY (unpushed) → Cowork verifies the committed object
**Workflow changed (user, 2026-06-17): Cowork verifies ONLY committed objects — never stale-risk
working-tree reads.** So: do the split + run the §3 gate **in your worktree** (your git is fresh /
authoritative), then **commit it locally, UNPUSHED**, as: *refactor: split regiontonecollector.cpp — lift
tone/context primitives into their own TU (byte-identical).* Report the **commit hash** + the §3 gate result
+ the move list in `cc_refactor_regiontonecollector_report.md`. **Cowork then verifies the COMMITTED OBJECT**
(`git show <hash> --numstat` move-only + `git show <hash>:path` content) — the only fully-reliable path. **If
Cowork finds a problem, revert** (`git reset --soft HEAD~1`) — safe, local/unpushed. **Do NOT push.**

## §5 — Stop conditions
- Any non-byte-identical step (golden / `.ours.json` / BIR / test move) → STOP.
- Any logic/scoring/inference change, or "fixing" anything → STOP (purity violation).
- A named function not cleanly liftable (shared helper / residual dependency) → STOP, surface (do not force).
- Any edit outside the new TU + `regiontonecollector.cpp` + `CMakeLists.txt` (+ the declaring header if it
  genuinely must change — flag it) → STOP.
- Committing before Cowork verifies the move-only diff → STOP. Any push → STOP.

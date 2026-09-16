# CC Instruction — J-key-iii (Step 3C): commit the verified wiring DORMANT (flag-OFF, byte-identical)

> **Ratified (user, 2026-06-15): option C.** A global flip-ON regresses non-chorale key reading (Step-3 §2:
> 3/8 out-of-scope snapshot scores), so the win is NOT flipped on. Instead, **land the verified wiring
> DORMANT** — flag default OFF, production byte-identical — to bank the architecture's first key-axis landing
> and consolidate the HELD working tree, with the global flip deferred to after the #4 dominant/subdominant
> guard (instruction B). **Local commit, UNPUSHED. Cowork verifies the staged set before the commit.**

---

## §1 — What this commits (and what it must NOT)

**Commit:** the verified production wiring + the HELD dependencies it needs to BUILD, all dormant behind the
default-OFF flag:
- `jointkeydecision.{h,cpp}` (the J-key-i strong-backbone producer + the `jointKeyWiringEnabled()` flag) and
  its tests.
- `applyJointKeyWiring` + the 2-pass call site in `regionanalyzer.cpp`; the Layer-B-inert guard in
  `sectionanalyzer.cpp`.
- Any **currently-uncommitted dependency** the above need to compile — notably the key-agnostic instruments
  `decideJointKey` consumes (`localmodulationdetector.{h,cpp}`, and confirm whether `cadencekeyanchor` /
  `tonicizationlabeler` are already committed vs HELD). **Identify the full build-dependency closure** (what
  must be in the commit for `composing_tests` + the bridge to build) and include exactly that.
- `tools/batch_analyze.cpp` `--joint-key-wiring` + `tools/run_bach_preset.py --joint-key-wiring` (the
  measurement toggles).

**Do NOT commit (stay HELD / gitignored):** the diagnostic probes + reports + corpora — `cc_*.md`,
`tools/cc_*.py`, `tools/corpus/*` (all already gitignored). Confirm `git status` shows none of these staged.
**Do NOT** stage any unrelated accumulated working-tree cruft — stage only the build-dependency closure above.

## §2 — Pre-commit gates (the dormant commit must be byte-identical)
- **Flag default OFF, env-gated** (`jointkeydecision.cpp:160-163`) — confirm the committed default produces
  **byte-identical** production: regen all 3 presets flag-OFF → `.ours.json` 0-diff vs the current baseline;
  **BIR 57/23/57**; suites **composing 545 / notation 57 / snapshots 11/11**, goldens **unchanged**.
- Build clean with the full dependency closure (no missing-symbol link errors — the reason the deps must be
  in the same commit).

## §3 — Stage + present HELD → Cowork verifies → commit
Stage exactly the §1 set. **Present the staged file list + `git status` HELD for Cowork** to verify the set
is the build-closure-and-nothing-more and that no diagnostic/cruft is staged. On Cowork's confirmation,
**commit (local, UNPUSHED)**. Commit message: *the constrained-joint key decision wired into production,
**DORMANT** (flag default OFF ⇒ byte-identical baseline); the first key-axis landing of the constrained-joint
architecture, gated pending the #4 dominant/subdominant guard (non-chorale generalization). Key win
+3.80/+3.50/+12.24 pp realized when enabled; chord axis untouched (key-only).* No `docs/scoring_model.md`
sync (key-only). **Do NOT push** (origin = the fork; user pushes separately per the git-topology rule).

## §4 — Stop conditions
- Any diagnostic file (`cc_*`, `tools/cc_*`, `tools/corpus/*`) or unrelated cruft staged → STOP, restage.
- Flag-OFF is NOT byte-identical (any `.ours.json` / BIR / snapshot diff) → STOP (the dormant commit must
  change nothing).
- A missing-dependency build/link error → identify the missing HELD file, add it to the closure, re-gate.
- Committing before Cowork has verified the staged set → STOP (present HELD first).
- Any push, or any edit outside the build-dependency closure → STOP.

# CC Instruction — Phase 5 backfill round 2, cluster 2 of 4: L4 oracle + gates (~98 upper-bound, oracle-asserted)

> **Why.** Cluster 2 of the stable-half branch backfill (`cowork_phase5_branch_backfill_spec.md`). Same rules as
> cluster 1 (engravingbridge, `3f2e4bebe2`): **coverage is the gap-finder, NOT the goal**; each test asserts the
> **theory/contract-correct value (oracle), re-derived at source** — never an echo. A correct oracle that **fails**
> current code → `DISABLED_`/xfail + flag (a surfaced defect), not a weakened test. **Tests-only — no production change.**
>
> **★ The ~98 is an UPPER BOUND.** Cluster 1's "53" was really ~20 — my triage over-counts ADD-TEST, calling some
> *provably-unreachable* defensive branches testable. **Re-confirm every branch's class at source** (you've corrected my
> triage three times now); test only the genuinely reachable ones, skip the defensive (Phase-6 seal) and any DEFER.
> *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §1 — The worklist (L4 oracle + gate ADD-TEST branches)
Files + triage ADD-TEST counts (upper bounds): `chord/chordanalyzer.cpp` (8), `chord/chordanalyzer.h` (11),
`chord/analysisutils.h` (3), `chord/postscoringgates.cpp` (**50** — the bulk), `chord/chordpostpasses.cpp` (16),
`chord/chordvoicing.cpp` (6), `function/harmonicfunctionlayer.cpp` (3).
- **Exact unhit locations:** grep `cc_union_branch_coverage_report.md` (§5) for each file.
- **Re-confirm class at source:** ADD-TEST (reachable real logic → oracle test) vs EXCLUDE-DEFENSIVE (can't-happen
  guard / exhaustive-enum `default:` / upstream-invariant → **skip**, Phase-6 seal) vs DEFER. Watch for the same
  over-count classes (impossible-rotation tautologies, no-tones fallbacks, enum `default:`s).
- Oracle themes (the **starting point** — derive the exact expected value at source):
  - **`postscoringgates.cpp` (the bulk):** each gate's **fires** vs **below-threshold-no-fire** outcome — Gates
    A / A-FM2, E, F, G-B/C/D/E, H-B/C/D, I, J, K, L. Build a `gateCtx` per case (mirror the existing
    `postscoringgates_tests.cpp`); assert the winner flips (or doesn't) per the documented gate rule.
  - **`chordanalyzer.cpp`:** add-#9 vs m3 disambiguation; #13-on-diminished suppressed; 6/9 negated by min7/maj7;
    missing-TPC → default extension; lowest-pitch bass dedup; below-`bassMinWeight` → lowest-pitch fallback;
    root-absent candidate → no triad-complete bonus.
  - **`chordanalyzer.h`:** empty-tones no-op merges; same-PC tpc backfill; ≥2 isBass → lowest-pitch bass;
    `advanceTemporalContext` sentinels (rootPc<0 → 0.0; empty candidates → 0.0; <2 → −1 margin); gates-empty → root −1.
  - **`analysisutils.h`:** `ionianTonicPcFromFifths` table (Cb=−7→11, A=+3→9, F#=+6→6) — one parametric test over
    fifths −7..+7 covers all three.
  - **`chordpostpasses.cpp`:** `cptIsBassChordTone` per-quality bass-is-chord-tone vs pedal; Iter86/Iter91 `bassPc<0`
    no-ops + the bass-as-root promotion guards; sparse-region `bassPc<0`.
  - **`chordvoicing.cpp`:** flat/sharp-fifth on a non-perfect-fifth quality; half-dim+Maj7 dup avoidance; added-6 as a
    13th skip; bass octave-up near the midpoint.
  - **`harmonicfunctionlayer.cpp`:** resolution-edge known-quality but prevRoot<0 → 0.0; winner-root≠bass (already an
    inversion) → no forced diff-root append; no above-threshold candidates → chosenResult unchanged.

## §2 — Write the tests (oracle-asserted) + §3 gate + §4 scope — IDENTICAL to cluster 1
- New `chord_branch_tests.cpp` (and/or extend `postscoringgates_tests.cpp` / `synthetic_tests.cpp` where the harness
  fits), registered in `tests/CMakeLists.txt`. Oracle from theory/contract, never echoed.
- A failing correct-oracle → `DISABLED_`/xfail + documented expected-vs-actual (rule 2). Do not weaken.
- **Gate:** all new tests pass (bar xfails); `composing_tests` grows; `notation_tests` + snapshots **unchanged**; corpus
  53/24/53 by construction; build green. **Any corpus/snapshot movement → STOP.**
- **Re-measure:** re-run the clang branch-coverage runner scoped to the L4 oracle+gate files; report each file's
  branch% before→after (note any COMDAT-folded covered-but-uncredited arms, like cluster 1's `isChordTrackStaff:83`).
- **Tests-only.** A gap closable only by changing production → STOP, flag (L4-build item). Skip defensive + DEFER. Do
  **not** annotate exclusions (Phase-6 seal). `upstream` never; local commit.

## §5 — Deliver
Commit **locally (unpushed)**: the new test file(s) + CMake (+ any new fixtures). Write
`cc_backfill_l4_oracle_report.md` (gitignored): tests added (per file), the branches you **re-classified
defensive/DEFER** at source (with the over-count count), any surfaced defects (xfails), the per-file branch% before→after
(+ any covered-but-uncredited), and the commit sha — so Cowork verifies by sha that only test files + CMake (+ fixtures)
changed, no production source.

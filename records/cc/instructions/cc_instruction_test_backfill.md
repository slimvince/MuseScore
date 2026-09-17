# CC Instruction — test-backfill: coverage tooling + close the MEASURED gaps (tests + tooling ONLY)

> **Why.** The user set a four-criteria test-adequacy bar (1: input classes per spec; 2: odd/empty/null input must not
> crash any layer; 3: all spec outcomes; 4: every branch hit at least once). CC's measured coverage audit
> (`cc_tree_repair_and_coverage_report.md`) found the genuine gaps. This pass installs the missing coverage instrument
> and writes the missing tests. **This is build-it-right (test completeness is foundation) — NOT precision work and NOT
> inference-fixing.** The only changes are **test files + a coverage tool + capture**. **NO production logic, NO new
> behavior, NO gate/threshold/scoring change.**
>
> **Coverage ≠ correctness.** OpenCppCoverage proves a branch *ran*; it says nothing about whether the output is
> *right* or whether the test *asserted* anything. A test that echoes the implementation's current output only guards
> against *change*, not *wrongness* — it can pin a bug as if it were the spec. Do not chase the coverage number; chase
> correct assertions. Coverage is only used to find branches **no** test touches.
>
> **Three hard rules:**
> 1. **Assert CORRECT values from an INDEPENDENT ORACLE — music theory, the documented contract, or music21 — NOT the
>    value the implementation emits.** Where the right answer is decidable (a voicing for a known quality, a Nashville
>    number for a degree, a documented contract, no-crash on bad input), assert THAT, hand-derived. A characterization
>    test that merely *pins current output* is allowed ONLY for genuinely tuned/heuristic results (a gate/margin/
>    threshold outcome), and only when **explicitly labeled a regression-guard, not a correctness proof.**
> 2. **A correct (oracle-derived) assertion that FAILS against current code is a SURFACED DEFECT, not a test to weaken.**
>    Mark it `DISABLED_`/xfail with a documented *expected vs actual*, and flag it in the report. Do **NOT** change
>    production to make it pass (no inference-fixing now), and do **NOT** lower the assertion to the wrong value (that
>    launders the bug). Do **NOT** test the spec's not-yet-built behavior (abstain/uncertain/spelling-pin) — §4.
> 3. **If a robustness test exposes a real crash, STOP and report it** as a tracked defect — do **not** fix it in this
>    pass (a crash-guard is still a production change; it gets its own ratified decision).

## §0 — Preamble: protect the uncommitted Cowork docs
Commit, **local-only**, the uncommitted Cowork doc edits in the tree (the audit correction banner, the plan fold-in, the
Phase-4 span-scope corrections): `docs(cowork): L1-L4 audit coverage-correction + test-backfill plan`. Confirm
`git show --stat <sha>` lists only doc files (no source). (Report the sha so Cowork can verify by explicit sha.)

## §1 — Coverage tooling (make criterion 4 measurable)
- **Install `OpenCppCoverage`** (the standard free MSVC line+branch coverage tool). If install is blocked/unavailable,
  **STOP and report** — do not fake numbers, do not substitute the block-only `Microsoft.CodeCoverage.Console` again.
- Produce a **BASELINE branch+line coverage report** for L1–L4 over `composing_tests` (and notation/snapshot where
  relevant). Capture to a file. **Its only use is as a gap-finder** — the precise map of which branches **no** test
  executes (drives §2). It is **not** a measure of correctness or of done; a covered branch with a weak/wrong assertion
  is still a gap in criteria 1–3.

## §2 — Write the missing tests (close the CONFIRMED gaps), each framed by the four criteria
For every module below add tests covering, as applicable: (1) the input classes the spec lists, (2) odd/empty/null/
outlier input asserting **no crash + defined behavior**, (3) each spec outcome, (4) the **uncovered branches** the §1
baseline identifies. Tests assert the **correct, oracle-derived** result (rule 1) — not the implementation's current
output; a failing correct-assertion is a surfaced defect (rule 2), not a value to weaken.

- **`chordvoicing`** (`closePositionVoicing`, `chordTonePitchClasses`) — currently **0% direct**: per-quality /
  per-inversion / per-extension voicings; the documented **Unknown-quality → empty voicing, bassPitch == −1** contract;
  octave-placement bounds.
- **`modepriorpresets`** — **0%**: the preset table lookup for each named preset; an unknown/default preset path.
- **`ChordSymbolFormatter::formatNashvilleNumber`** — **1 test**: all scale degrees, inversions, sevenths, minor-key,
  and the degenerate `degree < 0 → ""` contract.
- **L4 `analyzeChord` ROBUSTNESS (criterion 2 — the real hole; today only the <3-PC gate exists):** empty tone set,
  single note, unison / all-same-pitch, atonal cluster (≥3 non-tertian PCs), out-of-range key fifths (±>7), a
  tpc-absent note. **Assert NO CRASH + the defined result.** *(If any of these currently crashes → §-rule-2: STOP and
  report; do not add a guard here.)*
- **L3 option threads (line-executed but branch/assertion-untested):** `excludeStaves` (non-empty → the excluded staff's
  notes don't reach emission), `ignoreDeclaredMode == true` (the declared-drop arm), the **dynamic-lookahead growth
  loop** (force a low-confidence opening that grows the window to the max), and **`populateEmissionConfidence`** (assert
  the C1 `normalizedConfidence` the downstream 0.8 key-confidence gates consume).
- **Smaller confirmed L3 gaps (include if cheap):** the `declaredMode` arm at the emission analyzer; the
  `redecodeRange` arg-guard (`first<0`/`last≥T`/`first>last` → empty); the reach-back **hard-bound (`maxReachSteps`)
  stop** as a distinct outcome from convergence/score-start.

## §3 — Re-measure + gate
- **Re-run coverage**; report the **per-module branch% delta** (gaps closed, with the new numbers).
- **All ENABLED tests green; any oracle-test that exposed a defect is `DISABLED_`/xfail'd with a documented
  expected-vs-actual** (rule 2) — those are *surfaced findings*, an expected and valuable output of this pass, NOT a
  failed gate. List them explicitly. **BIR 53/24/53 + snapshots BYTE-IDENTICAL** — tests don't touch production, so
  nothing moves. **Any corpus/snapshot movement → STOP** (a test leaked into production — investigate, do not refresh
  goldens).
- Capture raw test output + the coverage report to files; in the summary **paste the headline numbers** (suite counts,
  branch% before→after) — evidence, not "all green".

## §4 — Scope & stops
- **NO production logic / behavior / gate / scoring change.** Tests + the coverage tool + capture only.
- **Do NOT test or build the L4 abstain/uncertain/inherit/spelling-pin** — production does not implement it; that is an
  L4 **build** item, not backfill. If a gap can only be closed by changing production → STOP and flag it as a build
  item.
- A robustness test reveals a crash → STOP, report (tracked defect, not fixed here).
- Coverage tool won't install → STOP, report (tooling decision).
- A push targets `upstream` → STOP. Local commit only.

## §5 — Deliver
Commit **locally (unpushed)**: the new tests + the coverage-tool config (the §0 docs committed separately first). Write
`cc_test_backfill_report.md` (gitignored): the §1 baseline, the §2 tests added per module, the §3 branch% before→after
+ green-suite counts + byte-identity proof, and the **surfaced findings** — the xfail'd oracle-defects (rule 2, with
expected-vs-actual) and any crashes (rule 3). Report all commit shas explicitly so Cowork can verify each by sha.

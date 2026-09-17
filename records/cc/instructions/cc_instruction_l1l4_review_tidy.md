# CC Instruction — L1–L4 comprehensive review + tidy: CODE / TESTS / TEST-DATA (the step-3 QA gate)

> **Why.** Per `cowork_l1l4_review_charter.md`: before opening L5, a comprehensive **know-don't-assume** review of the
> built L1–L4 + a **tidy** of imperfections. **You own code, tests, and test data** (on Windows — authoritative source +
> build/run); Cowork takes docs + architecture-coherence in parallel. **Verify every load-bearing claim at source
> (file:line); mark VERIFIED vs INFERRED.** **Tidy guardrails are strict — read §4 before fixing anything.**
> *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §0 — Preamble (sweep)
Commit local-only the unstaged Cowork docs (the review charter, the Phase-5b plan/ledger edits):
`docs(cowork): L1-L4 review charter + engage-with-L5 ratification`. Report the sha.

## §1 — CODE review (verified, not assumed)
For each layer, confirm the code **does what its design says**, and report any divergence/defect (cite file:line):
- **L1 `note_model`**, **L1.5 `engravingbridge` (incl. `spellingview`)**, **L2 `slicer`**, **L3 `key/*` + the
  reach-back orchestration**, **L4 `chord/*` (legacy `analyzeChord`/gates **and** the new dormant `chordslicedecoder`
  G1–G6+spelling-pin)**.
- **Unification / duplication:** any *new* duplication from the L4 build? The **deferred `analysisutils.h` relocation**
  (still chord/-located, used by L3 .cpp) — confirm it's tracked. The **two live segmenters** + **two pitch-context
  builders** — confirm they are honestly documented as *deferred to the joint-L5 engagement* (NOT silently dead).
- **★ tpc-pin unification (flagged by the doc review — resolve at source):** the tpc-capability spec §3 required the L4
  **spelling-pin to FOLD the ~55 inline tpc reads** (`tpcForPc` / `tpcConsistencyBonus` / `tpcSpellsAsSharp` …) in
  `chordanalyzer.cpp` **into the `spellingview` primitive** — one interpreter, not two. Determine **which happened**:
  did the spelling-pin fold them, or does a **second tpc reader now coexist** (the pin reads `lineOfFifths` while
  `chordanalyzer.cpp`'s inline cluster still interprets tpc independently)? **Report — do NOT fold now** (that's an
  engagement-step refactor, gated); just establish the truth (a unification residual to schedule, or already clean).
- **Dead-vs-staged honesty:** `chordslicedecoder` (dormant), `redecodeRange`, `tonicizationlabeler`,
  `DecodeQualityLevel::Normal/Deep` (inert) — confirm each is **comment-accurate** about *why* it's not live
  (deferred-engagement, not rot). Flag any stale "not wired / Increment-A only / stubbed" comments now false.
- **Stale comments / dead-vocabulary names:** e.g. `applyIter8691Pedal` and other iteration-vocabulary APIs.

## §2 — TEST review
- **Suites green** — run `composing_tests`, `notation_tests`, `pipeline_snapshot_tests`; report counts.
- **Oracle-quality:** spot-check the backfill + `decode_chord_tests` assert *theory/contract* values, not echoes.
- **Consolidate the surfaced-defect ledger:** every `DISABLED_`/xfail + labelled-guard across the suite — the
  German-bass slash, the Nashville placeholders, `chordanalyzer.cpp:449`, the leading-tone Phase-B guard — into one list
  (each: what, where, the correct expected, which firewall/phase it belongs to).
- **Stale/orphaned tests:** any test referencing removed code / never run.

## §3 — TEST DATA review
- **Orphaned fixtures:** re-verify **whole-repo** (the `mono_smoke_test` correction taught us per-dir grep is wrong) —
  the `chord_analysis_test.{musicxml,_expected.json,py}` "content moved" stubs and any others. Report confirmed orphans.
- **Fixture hygiene** (space-named `solid theory.musicxml`, dual encodings) and **corpus integrity** (manifests).

## §4 — TIDY (strict guardrails — per the charter)
- **Freely tidy (commit, gated byte-identical):** stale code *comments*, dead-vocabulary renames (behaviour-preserving),
  **delete confirmed-orphan test data/tests**. Each is its own small commit; suites + snapshots + corpus 53/24/53
  **unchanged**.
- **As-built doc entries you own (the doc review found these OMISSIONS):** add to **`STATUS.md`** a current-state entry
  for the COMPLETE-dormant L4 build (decoder `1e74f21ea4`, engage-with-L5, production still legacy) — STATUS's newest
  entry predates the L4 build; and add an **as-built Layer-4 section to `ARCHITECTURE.md`** (mirroring the L1/L2/L3
  blocks: `chordslicedecoder` per-slice commit/inherit/abstain + spelling-pin, built **dormant**, engages with L5).
  Also fix the stale `slicer.h:67` + `harmonicsegmenter.cpp:155` "NOT wired"/"isolated" **comments** (now false).
- **Flag, do NOT silently fix:** any *behavioural* code change, or a genuine correctness bug (German-bass) — those are
  ratified gated steps, listed in the report, not done here.
- **MUST NOT (STOP if tempted):** touch inference accuracy (leading-tone gate / scoring — firewall); **delete or
  "clean up" the dormant new-L4 path or the staged scaffolding** (`chordslicedecoder`/`redecodeRange`/
  `tonicizationlabeler`/`DecodeQualityLevel`) — they are deferred-engagement, their removal is the joint-L5 step.

## §5 — Gate
- After all tidy commits: `composing_tests` / `notation_tests` / `pipeline_snapshot_tests` green, **corpus 53/24/53
  unchanged**, snapshots no-refresh. Any movement → STOP (a "tidy" changed behaviour).

## §6 — Deliver
Write `cc_l1l4_review_report.md` (gitignored): §1 code findings, §2 test findings + the **consolidated surfaced-defect
ledger**, §3 test-data findings, §4 the tidy commits made (with shas) + the flagged-not-fixed list, and a blunt
**"L1–L4 code/tests/data: clean / residual items"** verdict — so Cowork verifies the tidy commits by sha and folds the
findings into the QA sign-off.

## §7 — Stops
- Inference-fixing, dormant-path/scaffolding deletion, or an unratified behavioural change → STOP, report.
- Any corpus/suite/snapshot movement from a "tidy" → STOP. `upstream` → STOP.

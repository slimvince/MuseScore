# CC instruction — OI-199 pass 1: the blind inventory across the review scope, the partition proposal, and the joint module's deep dispositions (READ-ONLY; certification is NOT granted by this pass)

> **★ BLINDNESS NOTICE — READ THIS FIRST, IT OVERRIDES A STANDING INSTRUCTION.**
> This dispatch runs the ratified **two-pass blind audit pattern** (OI-84's L1/L2, L3, L4, L5
> precedent). Pass 1 is a **blind enumerative** pass: you disposition everything, without being
> steered toward anything. Two deviations from the standing session-start read are therefore
> REQUIRED and deliberate, exactly as the L3 audit did (`OPEN_ITEMS.md` read deferred to its
> Task 2):
>
> 1. **Do NOT read `OPEN_ITEMS.md` or any `open_items/OI-*.md` file** until Task 4. Read
>    `CLAUDE.md`, `STATUS.md` and `BUILD_AND_TEST.md` as usual.
> 2. **Do NOT open §S (the sealed section at the foot of this file)** until Task 4. It contains
>    findings that would steer your reading and destroy the error-rate machinery's meaning.
>
> Both deferrals end at the **freeze commit** (Task 3), which is the blinding boundary and whose
> hash is the proof of ordering. Opening either early is a STOP that voids the pass — say so in
> the report rather than continuing.
>
> **Read first:** `CLAUDE.md`, `STATUS.md`, `BUILD_AND_TEST.md`, `DEFECT_TYPES.md` (the defect
> catalogue the sweep uses), `ARCHITECTURE.md` (the contract-direction check reads it), and the
> prior audit reports for the METHOD and the VERDICT VOCABULARY you must reuse unchanged:
> `cc_l3_audit_pass1_report.md`, `cc_l4_audit_pass1_report.md`,
> `cc_l4_audit_pass1_decoder_report.md`, `cc_l5_audit_pass1_report.md`. **Do not invent a
> vocabulary** (#6, and the standing no-self-invented-labels convention) — use the same row
> classes and verdict labels those passes used, and declare them in your report.
>
> **What this is.** OI-199 is the user-directed comprehensive code review: the certified two-pass
> blind pattern applied to everything the existing certifications predate — the joint module, the
> record path and seams, the codegen machinery, and the new instruments. **The user ratified
> pulling it forward** (2026-07-28) because the joint module is production on both surfaces, has
> never been reviewed, and — unlike the legacy path — is **not** retiring, so OI-84's
> never-audit-code-that-is-about-to-be-deleted rule does not shield it.
>
> **The user also ratified HOW the scope is decided: by measurement, not by estimate.** Both
> large prior audits (L4, L5) hit a feasibility stop at Task 1 and partitioned on measured row
> counts. **A feasibility stop with a proposed partition is the EXPECTED outcome here, not a
> failure** — say so plainly if the counts warrant it.
>
> **Current state:** branch `master`; expected HEAD `5135764ed7` — verify; mismatch = STOP.
> Riding Cowork edits: `cowork_handoff.md` and `STATUS.md` ride your first commit. This dispatch
> file stays untracked.
>
> **Hard stops:** origin only; **no fix, no refactor, no behavior change of any kind — you are an
> auditor, not an amender**; no inference change; no golden, `tools/corpus/` or
> `tools/robust_stop/` movement. A surprise is a STOP (#13). VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-28, at the user's ruling (scope-and-order alternative 2).

**Touchable set:** `tools/` (the inventory/sweep instruments and their artifacts); the test dirs
(if Task 2's behavioral characterization needs a driver); `src/composing/analysis/joint/` **only**
for a default-OFF fire-count instrument under the OI-110 disposition (used, then REVERTED in its
own commit, hash recorded); the register INDEX and detail files (Task 4 only); `STATUS.md`; the
riding Cowork files.

---

## Task 1 — the mechanical inventory across the whole review scope

Reuse the existing `gen_inventory.py` (extended at L5 with a second scope root and a Python
`ast` extractor — extend its selector, do not write a second inventory tool, #6). Re-prove the
prior layers' inventories byte-identical after any change to it, as L5 did.

**Scope, four areas:**

- **(a) the joint module** — `src/composing/analysis/joint/` and its tests.
- **(b) the record path and seams** — the record-arm code in
  `src/notation/internal/notationcomposingbridge.cpp`, `notationimplodebridge.cpp`,
  `notationtuningbridge.cpp`, `notationaccessibility.cpp`, the section record adapter, the
  presentation formatters, and the inference/presentation boundary guard.
- **(c) the codegen machinery** — the embedded-table generator, the generated artifact file, and
  the drift guard.
- **(d) the new instruments** — the Python instruments built during the joint-estimator and
  notation arcs under `tools/joint_estimator/` and `tools/notation_seams/`.

**The legacy arm is EXCLUDED BY CONSTRUCTION.** Code reachable only when
`useJointNotationRecord == false` retires at the OI-180 map, and OI-84's A1 verdict is explicit
that retiring code gets **no audit**, only the information-loss check at deletion. So in area
(b), tag every row **record-arm / legacy-arm / shared** and exclude legacy-only rows from the
in-scope count. **Report the tagging rule you used and the count you excluded** — if the arms
cannot be separated mechanically at some site, that is itself a finding (a #6 entanglement),
not a reason to abandon the rule.

**Deliver:** per area, the file count, the deep-file count, and the row count by row class
(function / include / field / literal / branch, plus the Python classes for area (d)); the
populations verified at the code and at call sites, as the prior passes did; and the generated
file in (c) identified as a **generated data population**, established by its drift guard rather
than by row disposition — say so explicitly rather than dispositioning 180 KB of embedded bytes.

**Then judge feasibility, and say it plainly.** If dispositioning every in-scope row at full
vocabulary is not achievable in this session, **STOP and propose a partition** with the measured
counts as its basis and a recommended order. The user's standing instruction is that **the joint
module holds first claim** on the deep work, and Cowork's amendment to the original OI-84
ordering is that **the instruments should be the SECOND partition, not the last** — because
every figure currently steering this arc came from them, and #19 forbids trusting an
unestablished instrument. Your proposal should honour both unless the counts give a reason not
to, in which case state the reason.

## Task 2 — the joint module's deep dispositions (first claim)

Regardless of the partition proposal, disposition area (a) fully in this session if feasible.

1. **Every in-scope row verdicted** at the full prior vocabulary — no row left blank, no coarse
   substitute vocabulary (the OI-100 lesson: a coarser label set invalidated a whole reading).
2. **The contract-direction check (the P3 pattern):** for every expectation `ARCHITECTURE.md`
   and the ratified governing documents state about this module, locate it in the code. Absence
   of a defect is not the finding; the finding is any expectation with no code, or any code with
   no expectation.
3. **Behavioral characterization (the P4 pattern) — fire rates on real routes.** Characterize
   what the module's branches actually do over the corpus: which branches never fire, which
   filters reject and at what rate, which paths carry the mass. Where this needs counters inside
   the module, follow the **OI-110 disposition exactly**: default-OFF, zero work and zero
   behavior change when off, byte-identity proven with it off, and **REVERTED in its own commit
   at the end of this dispatch** with the hash recorded so it can be cherry-picked back.

Findings get recorded in your report **but their register rows are written in Task 4**, after
the freeze — so that what you found is provably found blind.

## Task 3 — the FREEZE

Commit the dispositions and artifacts. **This commit is the blinding boundary**; record its hash
prominently. Nothing after this point can retroactively steer what came before it.

## Task 4 — unsealing, rows, and the reconciliation

Now, and only now: read `OPEN_ITEMS.md` and the detail files, and open **§S** below.

1. **Write the register rows** for everything you found (rule (c): index row and detail file in
   the commit that records the discovery), plus the rows §S specifies.
2. **The reconciliation — this is the point of the sealing.** For each of the three findings in
   §S, state plainly whether your blind pass found it independently, partially, or not at all,
   and by which row or which characterization. **Do not rationalize a miss.** A miss is a
   finding about the audit's power, not about the code, and it is exactly what we want to learn
   cheaply — it tells the user whether the remaining OI-199 partitions are worth their cost.
   Report it as a plain three-line verdict table.

## Task 5 — close

Report; `STATUS.md` entry; the counters reverted with byte-identity proven and both suites plus
the pipeline snapshots green. Commits per change-class. Push origin.

**Certification is NOT granted by this pass.** Pass 2 — a fully blind second reading in a fresh
session, a seeded error rate at full vocabulary, and the whole-scope defect-type signature sweep
— is a separate dispatch, and certification is the user's to grant on the measured record.

## Report

Hashes per commit, including the freeze and the revert. The Task-1 inventory table by area and
row class, the legacy-arm tagging rule and excluded count, and your feasibility judgement with
the partition proposal and its ordering rationale. The Task-2 disposition totals by verdict, the
contract-direction check's two-sided result, and the fire-rate characterization. Every finding
with file:line. The Task-4 reconciliation verdict table. Anomalies each diagnosed — a surprise is
a STOP.

Standing self-check before reporting: re-read the actual diff of every touched file against the
guiding principles, the conventions, the gate policies, and `DEFECT_TYPES.md`.

---
---

## §S — SEALED. Do not read before the Task 3 freeze commit exists.

*(Opening this before the freeze voids the pass — report it and stop.)*

Three findings arose from the 2026-07-28 analysis-cost measurement, **before** this audit ran.
They are sealed so that pass 1's discovery of them, or failure to discover them, is evidence
about the method. Write their rows now, and answer the Task-4 reconciliation against them.

**S1 — the joint decoder returns an EMPTY analysis on most orchestral scores.** Already rowed as
**OI-215** — read that row rather than re-rowing it. Summary: a candidate class is skipped unless
`present < min(2, |members|)` fails (`jointdecoder.cpp:444-445`), so a segment whose onset-pitch-class
union has fewer than two distinct classes admits nothing; a single event uncoverable by any
≤segCap window then empties `V[N]` and yields `complete=false`, 0 segments (`:838-841`). Measured:
13 of 23 committed large scores. **Reconciliation question: did your blind fire-rate
characterization surface this filter's rejection behaviour on its own?**

**S2 — the C++ decoder appears slower than the pure-Python reference.** `bach_chorale_001`, 80
events, C++ decode 5,650 ms (`large_score_decode_profile.json`); the Python reference,
memoization off, means 3,415 ms at 77.7 events (`window_study.json` cost curve). The build is
`RelWithDebInfo` `/O2 /Ob1 /DNDEBUG` — a debug build is excluded. Cowork's unconfirmed hypothesis
is `std::string` state in the innermost dynamic-programming loops (the class key, `backEnc`, the
state encoding). **Row it. Reconciliation question: did your dispositions flag the string-keyed
inner-loop state, or any other cost-structural defect, blind?**

**S3 — `buildAdapterFacts` is super-linear in events**, fitting `events^1.80` (95% CI 1.65–2.09,
R²=0.965, n=27) — near-quadratic fact extraction, 16.8 s on the largest score before analysis
begins. **Row it. Reconciliation question: did your dispositions find the repeated-scan
mechanism blind?**

**Also row, from the same session (not reconciliation subjects — record only):**

**S4 — a correction of record.** The analysis-cost report concluded that "the coupled DP
dominates and is not reusable across windows, so incremental patching saves ≤40%". That **does
not follow**: the 40.5/59.5 split is the cost share of a *cold whole-piece decode* and does not
establish that an edit forces full recomputation. Whether this semi-Markov recursion admits a
bounded local re-solve is unmeasured. Record incremental patching as **UNMEASURED, not refuted**,
and note the second unstated caveat — the split is Python-derived and a cost *fraction* does not
transfer automatically to C++.

**S5 — a declared process finding.** The analysis-cost dispatch required pre-registered
prediction bands per task (#17b) in two places; none of CC's own were registered before
measuring. CC surfaced this honestly. The measurements stand; what was lost is the guard against
motivated interpretation, and S4 is an instance of exactly the error that guard exists to catch.
Standing reminder for every future dispatch: register the bands in the artifact **before** the
measuring run.

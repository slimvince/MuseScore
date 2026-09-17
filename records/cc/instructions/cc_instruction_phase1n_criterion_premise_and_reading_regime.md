# CC dispatch — phase 1n: the section-level home criterion, the OI-165 premise, and the reading regime

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's rulings of the same
> date (fifth set).** Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1n_criterion_premise_and_reading_regime.md`.
> Copy it; do not retype from memory. The phase-1k commits cited a filename existing nowhere.
>
> **★ THIS DISPATCH ASSERTS NO FIGURES, BY THE RULE IT INSTALLS (Task 5).** Where a quantity is
> needed it is named as an **artifact field**, not transcribed as a number. If you find a bare
> figure anywhere below, it is a defect in this dispatch — report it.
>
> **★ THIS IS A RULING-APPLICATION WAVE. IT READS NO OI-207 DOCUMENTS.** Reads resume as dedicated
> waves under the regime Task 4 prepares. Do not open a document to "make progress".

## 0. Standing constraints

1. **Every amendment lands in the PROPER LAYER** (#7).
2. **NO inference-problem fixing.** Phase 1 under D-231. No fix, no design, no behavior change, no
   `src/` edit, no golden refresh, no `tools/corpus/` or `tools/robust_stop/` movement. **Renaming a
   symbol is a `src/` change and is not licensed here.**
3. **Never use the shell to read working-tree files.** File tools for content, existence, counts and
   searches. Shell only for read-only git object queries by explicit hash, and for the generator and
   guard scripts named below.
4. **Never work from memory.** Every written claim cites its primary source file:line, re-read this
   session.
5. **A surprise is a STOP** (#13).
6. Bare words carry the musical meaning. Bash: append `; echo "exit:$?"`; no large single outputs.

## 1. The rulings this dispatch carries

| # | Subject | Ruling | Applied here? |
|---|---|---|---|
| U1 | The contract-home criterion's granularity | **SECTION-level homes** (option A3), applied **staged** | Yes — **only if** the Task 1 tooling measurement clears §2.2 |
| U2 | D-428's classification | **Resolve OI-165's premise first** (option B1), then confirm or correct | Yes |
| U3 | The reading regime | **Read all owed, no tail bounded**, ordered by the stronger proxy, bands pre-registered (option C3) | Regime prepared; reading itself is later waves |
| U4 | Figures in dispatches and reports | **By citation to a generated artifact, never transcribed** (D1 + D3) | Yes |

## 2. Task 1 — The section-level home criterion (U1)

### 2.1 The criterion as ruled

**A home is a SECTION of a document.** It is admitted when a user-ratified surface delegates a
**stated concern** to that section **by name**, and that section **states rules** rather than
recording findings. The surrounding document's kind and its banner are not the test; they were
proxies for this, and the census case shows why they fail — `ARCHITECTURE.md:317-319` delegates the
licence-pool constraint to `cowork_score_census.md` **§8c**, a rule-stating block inside a
findings-kind document.

This **subsumes** the kind test rather than replacing it: a rule-stating section qualifies whatever
its surrounding document is. Rule (g)'s guard is intact — the delegation confers, and only the user
writes a delegation into `ARCHITECTURE.md`.

### 2.2 Measure the tooling cost FIRST, and stop on a pre-declared criterion

**Before changing any entry**, establish what in the tooling assumes document granularity: the
backbone entry shape's home field, `gen_decisions_register.py`'s rendering and `--check`,
`gen_cluster_dispositions.py --verify`'s quote and anchor resolution, and the drift report.

**The pre-declared stop (#17b), decided now so it is not decided under the pressure of the diff:**

- **PROCEED** if the change is confined to the home field's shape plus the generator and checker
  reading it, and **existing entries' anchors do not need re-aiming** to accommodate it.
- **STOP AND REPORT** if it reaches the anchor or drift machinery such that existing entries would
  need re-anchoring, or if the quote-verification path must change. In that case the user's declared
  fallback is the **graded delegation-form test**, with the bar between *"full specification of a
  concern"* and *"listed as a related document"* — **do not implement the fallback here**; report
  and stop.

### 2.3 If §2.2 says PROCEED — the staged application

Apply section-level homes **only where they decide something**:

- the ambiguous population of the kind test (`tools/audit/decisions/phase1m_measurements.json` →
  `task5_kind_test.entries_ambiguous`, enumerated in `task5_kind_test.ambiguous_documents`);
- the `cowork_score_census.md` entries (same artifact, the `rows` entry for that document).

**Everything else migrates as its document is next touched.** Do not re-home the whole population.
Record that staging in the register's own scope note so a reader knows the field is mixed and why.

For each entry brought to section granularity: name the section, cite the delegating sentence
file:line, and preserve the former document-level home in provenance (#12).

### 2.4 What this does to the earlier criteria

The delegation-specificity criterion (phase 1l) and the kind test (phase 1m) are **superseded by
this one, not falsified** — both were steps toward it and both produced the evidence that located
its error. Record them as superseded-by with that reasoning, so a reader meets the derivation rather
than three rival tests.

## 3. Task 2 — OI-165's premise, then D-428 (U2)

**Order is mandatory: the premise before the conclusion.** D-428 classifies the iteration-API
renames as debt on *partly-live* code, and that classification rests entirely on OI-165's statement
that the Layer-1.5 fact cycle is *"not currently scheduled to die"*. A conclusion is not more
established than its premise (#18).

### 3.1 The check

`open_items/OI-288.md:54-61` frames it: both production call sites of `findTemporalContext`
(`regionanalyzer.cpp:921`, `notationcomposingbridge.cpp:651`) are on the legacy arm, which the
retirement map's R1/R5/R6 delete under **D-418**. Establish, at the code and at the retirement map:

1. Are those two the **only** production call sites? Enumerate every caller.
2. Do R1/R5/R6 in fact delete both? Read the retirement map's own text; quote it.
3. Does the primitive have any **named future consumer** — the joint module, the record adapter, a
   planned Layer-1.5 surface? Answer from the record, not from plausibility. "Not stated" is a
   permitted answer.
4. Enumerate the **false-negative paths** for the conclusion you reach (#17e) — the ways the
   primitive could survive that this check would not see. This is an insulation claim and the rule
   requires them stated.

### 3.2 The consequence

**Write the answer INTO OI-165 as an answer**, not as a corrected premise — that row has carried an
unchecked liveness claim since it was opened, and it is the source the next reader will use.

Then confirm or correct **D-428**:

- if the primitive dies with the legacy arm, every call site is on retiring code, D-428 is **not
  live debt** but legacy cleanup the retirement discharges (OI-84 rule A1), and its entry and its
  LEGACY status change accordingly;
- if it survives, D-428 stands as written and OI-165 gains the consumer that makes it true.

Either way the entry records **which premise it now rests on and where that premise was checked**.

## 4. Task 3 — Install the figures rule (U4)

**The rule.** A figure enters a dispatch or a report **by citation to a generated artifact**, never
by transcription. Name the artifact and the field; do not copy the value into prose. This is
`CLAUDE.md` #17(f) — no hand-transcribed measurement numbers — applied where it was being ignored:
to dispatches and to session reports, not only to documents.

**Home.** `cowork_audit_protocol.md`'s dispatch-protocol section, beside D-250, D-251 and D-252,
which are the established home for rules about how a dispatch is written. Register entry in the same
commit (the same-commit rule, D-230).

**Its defense, stated at the home:** five figure-or-premise errors across three waves, each from a
value taken off a secondary surface rather than a primary one, each caught by a dispatch's own check
rather than by the writer's reading. The instances are on the record at `open_items/OI-286.md`,
`open_items/OI-288.md`, and the phase-1m measurement artifact's read-count reconciliation. Both
sides are bound: Cowork's dispatches and CC's reports.

**Generalize OI-283.** That row currently covers the register's hand-typed coverage claim. Note on
it that the same shape is now ruled for dispatches and reports, so the row's remedy is one instance
of a general rule rather than a one-off.

## 5. Task 4 — Prepare the reading regime (U3), do not read

**The ruling:** read every owed document, bound no tail, order by the stronger proxy, and register
predicted bands **before** reading so the proxy is established out-of-sample rather than merely used
(#17b, #19, #20).

Produce **one generated artifact** — a new section of the phase-1 measurement generator or its own
file, your call, but generated and committed — containing:

1. The owed document list (`phase1m_measurements.json` → `task6_reading_yield.owed_rows`) **ordered
   by the stronger proxy**. Cowork's independent recomputation on the artifact's read rows found
   **length outranks unresolved-cluster count and outranks named-in-ratified-surfaces**; the OI-207
   list's current ordering is by unresolved clusters, which is the weaker of the two. **Recompute
   all three rank correlations yourself and report them from the artifact** — do not take Cowork's
   word, and note that Cowork's and CC's phase-1m values for the length correlation differ slightly,
   which is itself a tie-handling question worth settling.
2. A **predicted yield band per owed document**, registered before any of them is read, with the
   band's basis stated and the proxy explicitly labelled a **structural proxy standing in for a
   behavioral quantity, unvalidated** (#17d).
3. The reading schedule under the dedicated-wave regime: how many documents a wave can hold, derived
   from the owed corpus's size fields (`task6_reading_yield.owed_total_bytes`,
   `owed_est_tokens`) rather than asserted, and the implied wave count.
4. **No tail is bounded.** State that explicitly, with the reason: the best proxy is
   fitted-and-self-measured on the read set and has counter-examples inside it, so a bound resting on
   it is the unvalidated proxy #17(d) forbids.

**Every later read wave records actual yield against the predicted band**, so the proxy is tested as
a by-product. Say so in the artifact, so the next wave inherits the protocol rather than reinventing it.

**Correct the OI-207 reading list's ordering** to the stronger proxy, with a dated note recording
that the previous ordering was by the weaker one and was never checked against the alternative.

## 6. Task 5 — Guards, notes, close

```
cd C:\s\MS && python tools/audit/decisions/gen_decisions_register.py --check > /tmp/reg_1n.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/audit/decisions/gen_cluster_dispositions.py --verify > /tmp/ver_1n.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/open_items_split_check.py > /tmp/split_1n.txt 2>&1; echo "exit:$?"
```

Read each output separately; all three pass at the committed tree. Anchor drift re-aimed **per
citation from the drift report's own line numbers**, never by an assumed uniform shift.

`STATUS.md` gains one POINTER entry, stating that this wave read no OI-207 documents by design and
that reads resume under the Task 4 regime. Commits by git plumbing; guards run explicitly at the
committed tree. Report the SHAs.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's own remedy, OI-274's body-tense
half, OI-287 (the ratification-surface directory), OI-289 (the LEGACY-marker re-verification, phase
2), OI-288(a) (the legacy-arm fire rate, phase 2), and the owed reads themselves.

## 7. Accepted outcomes

Tasks 2–5 are bounded and expected complete. **Task 1 stopping at §2.2 is a success, not a
failure** — the stop criterion was declared before the diff existed precisely so it could not be
amended under pressure (#22). A report saying "section granularity reaches the anchor machinery, here
is what it would cost" is the outcome that task was written to be able to produce.

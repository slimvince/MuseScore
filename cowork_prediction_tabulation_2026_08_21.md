# Tabulation — the sealed prediction against both evaluation reports

> **STATUS: RECORD.** Cowork (the successor-plan session), 2026-08-21. Written BEFORE any line of
> the successor plan was drafted and BEFORE this session opened the four plan versions or the
> existing review, as Ruling 3 of `cowork_rulings_2026_08_21_evaluation_brief_sitting.md` binds.
> It takes no ruling, touches no document, allocates no finding number, and is authority for
> nothing. It lands in git at the next Claude Code dispatch's Task 0 with the other 2026-08-21
> records.
>
> **Inputs, all read whole by this session:** `cowork_review_findings_prediction_2026_08_21.md`
> (the prediction, opened for the first time at this tabulation); `cc_report_plan_evaluation.md`
> at commit `3cfb220b1d` (parent `7d7a0e76f7`), read from a staged copy whose sha256
> `1f781a4a88393915…` matches the committed blob; `cowork_report_plan_evaluation_2026_08_21.md`
> (untracked, 42,761 bytes at staging). Every `file:line` below is to those three files.

---

## 0. How to read the verdict column

| verdict | meaning |
|---|---|
| **BOTH** | re-found independently by both evaluators, on their own evidence |
| **ONE (CC)** / **ONE (Cowork)** | re-found by that evaluator only |
| **NEITHER** | found by neither |
| *adjacent* | an evaluator reached a neighbouring finding that is not the predicted one; noted, not counted |

"Re-found" means the evaluator states the substance of the item with its own grounds. A mention
of the plan's own text on the point (for instance quoting the plan's L5) is not a re-finding.

---

## 1. The prediction's items, one row each

| # | prediction item (short) | CC report | Cowork report | verdict |
|---|---|---|---|---|
| §1 | the five-sub-field replacement for the falsification field (ARM / SITE / OBSERVABLE / DECISION RULE / NOT-FALSIFIED-BY), reached by tracing statements into code | did not trace into code; proposes a six-field form whose sixth field splits "in code" vs "in the residual" (`cc_report:750-767`) — *adjacent* | did not trace into code; keeps the five-field form (K2, `cowork_report:71`), adds an epistemic label (R9, `:115`) and uncertainty (M3, `:137`) — *adjacent* | **NEITHER** — the item's own precondition (tracing into code) was exercised by neither |
| §2.1 | a frame taken from `ARCHITECTURE.md`'s headings is contaminated (Layer 1–6 specifications subordinate to §3.3; table of contents omits the standing-rules section; fenced-code false headings) | rejects headings as the unit on other grounds (`cc_report:672-702`); does not state the §3.3 subordination or the table-of-contents defect — *adjacent* | R1 (`cowork_report:99`): numbered sections largely not the analysis; layer specifications live under §3 Directory Structure, "the structure most likely to be code-shaped is the one holding the specification" | **ONE (Cowork)** |
| §2.2 | the concerns are coupled, measured not argued (scale-degree chord axis; one capacity budget; the semi-Markov length bias) | §3.1/§3.3 (`cc_report:647-652, 672-689`): a per-section split asserts an unstated factorization (#18); factors are terms in one combined content score; cites the length-bias case (`:720-722`) | M2 (`cowork_report:135`): key and chord jointly determined; segmentation a modelled semi-Markov variable in the same decode; no version designs for it | **BOTH** |
| §2.3 | rule (d) on the key axis (commit, never abstain) sits in declared, unsettled tension with §5.7a; no plan step would find it | not stated | not stated ("what is abstained" appears only as a frame field, `:167`) | **NEITHER** |
| §2.4 | failing runs cannot be attributed to a section from the committed artifact; removes the load under error-mass ordering and depth | not stated; error-mass axis discussed only as one of v4's axes (`cc_report:346-354`) | D4 (`cowork_report:129`): clustering failing runs by decision needs a per-run causal diagnosis over 4,547 runs per preset, infeasible by hand and forbidden by tool; error mass survives only as an input from a later measurement | **ONE (Cowork)** — reached from feasibility, not from the artifact's fields |
| §2.5 | the ground-truth annotation schema enumerates conclusions, not decisions | not stated | cites the plan's own L5 for the point (`:165`); schema not opened | **NEITHER** |
| §2.6 | walking the deletion history does not fit any proposed budget (229 commits, 15,483 deleted lines, classification the cost driver) | Phase A's session counts have no basis and A3 is what L8/L9 says is unmeasured (`cc_report:356-364`); affordability CANNOT ESTABLISH (`:585-589`) | C3 (`:151`): Phase A's termination in budget cannot be established, history unmeasured; R7 (`:111`): tiers and B1 contradict on the history walk | **NEITHER** as a measured finding — both flag the cost as unmeasured, neither measured it |
| §2.7 | a section whose defect is a hole has no advance signature (rule (c)); the argument against deciding depth before reading | not stated | not stated | **NEITHER** |
| §2.8 | two missing axes — LIVE/DORMANT and establishment status — and sections that fit no depth tier | a different missing axis: how implementation-derived the text is (`cc_report:346-354`) — *adjacent* | C1 (`:147`): `docs/scoring_model.md` declares its mechanism dormant, so statements derived from it are quarantined on arrival; R1(i) (`:99`): §6, §8–§13, §19 are not the analysis | **ONE (Cowork)**, partial — dormancy and the non-analysis sections; establishment status not stated |
| §2.9 | arithmetic on the frame test (≈3 % chance of firing at a 10 % true rate); the A5/§10 self-contradiction; the founding instance refutes the threshold | 60 and "more than ten" carry no defense; CANNOT ESTABLISH whether they are right; the threshold is a hard branch to a STOP (`cc_report:597-602`) | K4 (`:75`): the binomial computed — a 10 % true rate exceeds 10/60 in about 3 cases in 100, a 25 % rate falls at or below it in about 9 in 100; C5 (`:155`) | **BOTH** on the undefended threshold; the arithmetic by **Cowork** only; the A5/§10 self-contradiction by **NEITHER** |
| §2.10a | guardrail 2 (no numbers, no rows) collides with open-items rule (c) and D-641 | §2.2 (`cc_report:323-344`): MERIT and CONFORMANCE stated as two; rule (c)/(e); repair = the worth test | R4 (`:105`): rule (e) and D-641; repair = the quarantined audit questions as the third home | **BOTH** |
| §2.10b | guardrail 11 is self-sealing (the clause forbids the act that would verify it) | KEPT as MERIT, the self-referential clause called correct (`cc_report:188-195`) | K8 (`:83`): keep verbatim | **NEITHER — and both evaluators reach the OPPOSITE verdict.** The review's finding is refuted twice over, independently |
| §2.11 | the lineage lost load-bearing material (v1's ten Stops; v2's governing correction; guardrails 7/9/10's second clauses) | §2.1a (`cc_report:216-268`): all three, plus v1's guardrail-4 parking clause and v2's unit-shape correction with its ratified grounding | §1 (`:28-33`): all three (the governing correction rated minor), plus v1's principle that the unit is derived from the domain, not inherited | **BOTH** — and each found one loss the other did not |
| §3.1 | three source files self-declare DORMANT against a live default; a fourth contradicting site | out of the brief's scope; not stated | out of scope; not stated | **NEITHER** (expected — an analysis finding, not a plan finding; its disposition is owed separately) |
| §3.2 | `CLAUDE.md` #21 routes the ceiling through a superseded phase numbering with no pointer to the remap | cites `CLAUDE.md:162-169` and the surface's remap `:319-321` together (`cc_report:425-429`) without flagging that #21's own text is stale — *adjacent* | D3 (`:127`) cites both the same way — *adjacent* | **NEITHER** as a defect finding; both read through the remap without noticing the stale text |
| §3.3 | [[OI-179]] OPEN and GATES, confirmed in `gating_ids` | confirmed (`cc_report:808-810`) | confirmed (`:12`) | **BOTH** (a check, not a finding) |
| §4 | what is GOOD: the defense rule ("because the implementation does this" is no defense); A6 worked; A5's instinct; §11's refusal to invent a number; §6's bounded migration; §13 and §15 existing | every one of the six is a KEPT finding (`cc_report:141-214`), §6 rated as improving on the ruled pruning plan (`:197-208`) | every one is a KEEP finding — K9, K2, K4, K5, K7, K11, plus the attack list kept under D1 (`:69-95, 123`) | **BOTH, the whole section.** The brief's two-polarity clause worked |
| §6 | the "not situated against the ruled six-phase structure" return should NOT be re-found as a largest return; an unbiased evaluation may note the collision as conformance and should not lead with it | the phase-structure collisions appear only as labelled CONFORMANCE halves, never first (`cc_report:425-435, 548-568`) | R2, R5, R10, R11 are CONFORMANCE, each with "is the rule right?" answered; none leads (`:101-119`) | **CONFIRMED as predicted** |

---

## 2. What the prediction did NOT contain, and both evaluators found

The prediction's own falsification clause (`prediction:303-306`) says: *both evaluations returning
a substantially different set of merit findings would say the existing review's evidence was an
artifact of its method, and the successor plan should then be built from the new evidence.* That
clause is **engaged in part**. The two evaluators' largest merit findings are not in the
prediction file at all, and they agree with each other on them:

| finding, new to the record | CC | Cowork | agreement |
|---|---|---|---|
| **A1's document set is wrong at the object**: the delegation-bar home population is 146 entries across 34 non-specification documents and excludes `ARCHITECTURE.md` (and `CLAUDE.md`) by construction (`DECISIONS.md:250`); Phase A could not see the plan's own subject | DROPPED, the largest finding (`cc_report:368-405`) | §3 measured fact; D2 DROP (`:57-59, 125`) | **BOTH — the strongest agreement in the two reports, and the only finding both put first** |
| the trust measurement built on recorded dead ends is wrong: the dead ends are LEGACY-scoped and disclaim the use; the list is mixed and needs the fact-gate's test (*does the fact survive the implementation being thrown away?*) as an admission test | REPAIRED (`cc_report:272-309`) | R3, M1 (`:103, 133`) | **BOTH** |
| no completeness accounting over the OUTGOING text — the grading runs from the derivation outward only; the ruled five-fate disposition with arithmetic is what fills it | MISSING, "the most important finding here" (`cc_report:439-474`) | R5 (`:107`) | **BOTH** |
| the unit must come from the model / the decisions the analysis makes, not from documents | the factor (`cc_report:672-702`) | the decision, derived from schema + published models + theory (`:165`) | **BOTH on the direction; they differ on the grain** — factor vs decision |
| §7's "OI-179 is computable from data that already exists" drops `CLAUDE.md:184-193`'s three qualifiers | REPAIRED-if-kept + CONFORMANCE, with "is the rule right? no, not as it stands" (`cc_report:407-435`) | D3, with "is the rule right? its ground is sound" (`:127`) | **BOTH on the merit defect; they DISAGREE on the ruled placement** — CC says the fifth-of-six placement is wrong, Cowork says the ruling's ground is sound and the plan's point is a question about when the measurement-design stage starts |
| the statement form has no place for a premise / an epistemic label / uncertainty | premise + false-negative path (`cc_report:513-531`); no uncertainty anywhere (`:540-546`) | R9 FACT/THEORY/CONJECTURE (`:115`); M3 uncertainty (`:137`) | **BOTH** (different fields named; same gap) |
| no per-phase retrospective | CONFORMANCE (`cc_report:548-554`) | R10 (`:117`) | **BOTH** |
| the first-unit budget breaches guardrail 5 / Phase A's numbers have no basis | Phase A (`cc_report:356-364`) | R6, Phase B's first unit (`:109`) | **BOTH**, on different phases |
| the plan's fact row "677 entries" is a pinned, historical value | ESTABLISHED at the pinned artifact (`cc_report:604-617`) | C4 CANNOT ESTABLISH (`:16, 153`) | **ONE (CC)**; Cowork flagged and stopped |

## 3. Found by one evaluator only (new to the record)

| finding | by | where |
|---|---|---|
| code sites and failing runs inside the deriving pass collide with the ruled clean-room constraint; "the only uncontaminated evidence" is the annotated scores, not which runs fail | Cowork | R2 (`:101`) |
| the refute-only brief in §15/B5 should be DROPPED; the attack list itself kept | Cowork | D1 (`:123`) |
| A4's error-mass clustering is infeasible as a Phase-A act | Cowork | D4 (`:129`) |
| the depth tiers contradict B1 and the density axis is circular | Cowork | R7 (`:111`) |
| boot-list member (6) `DEFECT_TYPES.md` fails the list's own limb (1) | Cowork | R8 (`:113`) |
| the literature must be fetched and read; an unfetched source yields no statement | Cowork | M4 (`:139`) |
| a held-out establishment test for the method: derive a decision whose user-ratified ruling is withheld, then compare | Cowork | M5, §5 (`:141, 171`) |
| a joint-coherence check at assembly | Cowork | M6 (`:143`) |
| A6's five test kinds omit the factor form and the conditional-independence premise — the dominant statement kinds in the production specification | CC | `cc_report:311-321` |
| v4's depth axes omit the pollution axis; the July screen (`tools/audit/july_screen_report.md`) already measures pollution per document, refuting the plan's fact row that no such artifact exists | CC | `cc_report:346-354, 476-491` |
| the preserved pre-restructuring text at `b006dc15b5` — the record's ruled "most valuable single untrusted source" — appears in no version | CC | `cc_report:493-511` |
| v3's §6 end state fills a hole in the ruled pruning plan (the rule is per specification; `ARCHITECTURE.md` is one file holding many) | CC | `cc_report:197-208` |
| the plan's §1(c) premise about provenance does not reach text | CC | `cc_report:502-507` |

## 4. Disagreements between the two evaluators, localised

1. **The grain of the unit.** CC: a factor of the model (ten factors at
   `cowork_joint_estimator_factorization.md:73-132`). Cowork: a decision the analysis makes,
   derived from three sources. Both reject documents and authored questions. What it turns on:
   whether the unit must be where a precision change lands (CC's test) or where a checkable
   disagreement is decidable against theory and the schema (Cowork's test). Not settled by either.
2. **The ruled placement of the ceiling measurement.** CC: the rule is wrong as it stands. Cowork:
   the rule's ground is sound; the plan's point is about the design's start. Both agree the plan's
   "computable" claim is false at `CLAUDE.md:184-193`.
3. **The pilot's subject.** Cowork (C1, §5) would choose the production model's segmentation
   decision over `docs/scoring_model.md` and says so as its own derivation, noting the ruled
   subject stands. CC does not raise it and runs its Step 3 on the boundary factor of the
   production model — which is, in substance, the same preference, reached without naming it as
   a departure from the ruled subject.
4. **Reliance on the plan's facts tables.** CC checked five fact rows at their artifacts and found
   one historical. Cowork opened none and declared every dependent verdict unmade.

## 5. What this table says about the prediction as a whole

- **Re-found by both:** §2.2, §2.10a, §2.11, §3.3, §4 whole, and the §6 negative prediction.
  Five of the seven items the prediction expected both to re-find (`prediction:292`) were not
  re-found by both: §2.1 (one), §2.3 (neither), §2.6 (neither as measured), §2.7 (neither),
  §2.9 (partly), §2.10b (refuted).
- **The prediction's conditional items** (§1, §2.4, §2.5 — "if the evaluator traces statements
  into code") were not exercised: neither evaluator traced a statement into code. Their status
  is unchanged — SWEEP, not established — and the successor plan cannot rest on them.
- **The two findings both evaluators put first are absent from the prediction.** The falsification
  clause is engaged to that extent: the successor plan is built from the new evidence, with the
  prediction's BOTH items carried as corroborated and its NEITHER items carried as UNESTABLISHED.
- **One item of the existing review is refuted twice over:** guardrail 11's self-referential clause
  is rated correct by both independent evaluators.
- **The existing review's SWEEP items** (§1, §2.1 in part, §2.4, §2.5, §2.6) remain UNESTABLISHED
  under #19 and enter the successor, if at all, marked so — Ruling 4.

---

*Provenance: Cowork, 2026-08-21, the successor-plan session, at tip `3cfb220b1d` (read by
`git show --stat` at that explicit hash on the user's machine; `git log`, `git status` and
`git rev-parse` not run). Written before the four plan versions, `cc_report_plan_challenge.md`,
`cc_instruction_plan_challenge.md` and `cowork_curated_boot_list_draft_2026_08_19.md` were opened
by this session.*

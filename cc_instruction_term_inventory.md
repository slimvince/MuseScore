# CC instruction — the term inventory for the term-level theory-grounding audit (READ-ONLY)

**Dispatch author:** Cowork, 2026-07-18, at the user's direction. **Type:** fact-finding enumeration
(#1 investigative, #5) — **no code change, no fix, no tuning, no inference work**. This is the
**code-enumeration half** of the term-level theory-grounding audit (`cowork_joint_estimator_architecture.md`
§4 step 1 — the #17 funnel's first stage). The **theory-derivation half** (deriving each factor's correct
*form* from published research) is Cowork's and is **NOT this dispatch** — do not derive, judge, or
recommend theory forms, and do not pre-decide the mode-vocabulary question (OI-174/OI-132/OI-147); that
decision is the user's.

**Read first:** `CLAUDE.md` in full (including the 2026-07-18 principles #20–#24), `OPEN_ITEMS.md`,
`cowork_joint_estimator_architecture.md` (the governing architecture; the §2 factor roster is the mapping
target), `cowork_key_chord_joint_inference_grounding.md`, `docs/scoring_model.md`, `ARCHITECTURE.md`,
`cowork_evidence_inventory.md`, `BUILD_AND_TEST.md`, the lean `cowork_handoff.md`.

---

## 1. Purpose

The joint estimator's design pass must answer "do we have the right terms with the right forms." The theory
half answers "what forms SHOULD the factors have"; this dispatch delivers the other side at file:line
resolution: **what terms does the current inference actually compute, in what form, with what constants and
provenance, and how do they map onto the §2 factor roster.** The current answer on record is "no — several
are known-wrong and it was never audited"; this inventory is what makes that auditable.

## 2. Task 1 — the term inventory

**Scope:** every inference-affecting term on the **live analysis path**, plus the dormant decoder's term
surface (`chordslicedecoder`), across L1–L5:

- L4 scoring: every template, bonus, penalty, guard, gate, score-matrix term, and post-scoring pass in
  `chordanalyzer.cpp` (cross-check `docs/scoring_model.md` §2/§4/§6 — run the staleness check);
- L3: key/mode priors, change costs, decoder transition terms, mode-prior presets;
- L2: segmentation terms — boundary scores, duration/gap priors, **including the head-gap tonic prior
  (the OI-175 site, `harmonicsegmenter.cpp:849-852`)**;
- L1/L1.5: metric weighting, tone-collection construction terms, span-window weights (the OI-86 value-copy
  sites included);
- cadence/leading-tone, spelling/tpc, and bass/inversion terms wherever they live.

**One row per term:** (a) name as in code; (b) file:line; (c) layer; (d) the implemented form, in plain
words (additive bonus / multiplicative factor / hard threshold gate / lookup table / etc.); (e) constants:
value(s) and provenance — hand-set / fit / derived, and whether `tools/param_manifest.json` covers it;
(f) consumers (who reads the result); (g) the `cowork_joint_estimator_architecture.md` §2 roster factor it
maps to, or **NONE**.

**Method:** start from the certified audit surfaces (the pass-1 disposition CSVs under `tools/audit/`,
`docs/scoring_model.md`, `tools/param_manifest.json`) but **verify every row at the code** — cite what you
verified, never what a document asserts (the standing CC-trust rule). The inventory artifact is
**generated/assembled, not hand-typed where derivable** (#17f); rows that are hand-verified readings are
marked as such.

**Mandatory cross-checks:**
1. `docs/scoring_model.md` template count vs `kTemplateCount` (the standing staleness check) and its §4
   term list vs what the sweep finds;
2. OI-23's "~30 live hand-set constants" claim — report the count you actually measure and flag any
   difference (do not amend OI-23's row text beyond adding the measured figure with provenance);
3. **the DT-26 scope check**: after enumerating the named files/layers, run the identifying patterns
   TREE-WIDE and disposition the out-of-scope remainder file by file — a scoped sweep proves completeness
   of the scope, never of the question (the OI-175 lesson).

## 3. Task 2 — the two-way gap map

- (a) §2 roster factors with **no current term** — the missing clue channels;
- (b) current terms mapping to **no roster factor** — each one a keep/fix/drop *input* for the design pass,
  explicitly **NOT decided here**;
- (c) cross-reference `cowork_evidence_inventory.md` §8: published evidence facts consumed by no term.

## 4. Task 3 — OI-179 feasibility census (counts only)

For the ground-truth ceiling measurement (OI-179): report what **multiply-annotated** ground truth exists —
of the 352 stems, how many carry more than one independent human analysis in the repo's corpora (the
WiR/DCML sources), and where. **Counts and locations only** — do NOT build any agreement grading, do NOT
touch the robust stop or its reference. If none exists in-repo, say so plainly; the literature side of
OI-179 is Cowork's.

## 5. Constraints

- **No behavior change anywhere** — no `src/` edit, no `tools/` behavior edit, no golden, no corpus regen,
  no re-baseline. New files allowed only for the report and the generated inventory artifact.
- Every claim cited at file:line; every figure from the generated artifact, none hand-typed (#17f/#24 —
  where a count has sampling or extraction uncertainty, say so).
- This is fact-finding: surprises are allowed (#5), but a surprise implicating **live inference
  correctness** is a STOP + an `OPEN_ITEMS.md` row (same commit), never a fix (#8/#13).
- No self-invented labels — use the names things already have.
- Self-check the diff before reporting (the standing rule).

## 6. Deliverable

`cc_term_inventory_report.md` + the generated inventory artifact (a CSV/JSON under `tools/term_inventory/`)
+ any new register rows, in **one commit**; force-add this instruction file; push to `origin` only
(`upstream` stays disabled). Lean `STATUS.md` entry per the post-split discipline (one dated entry; history
goes to the archive). **On completion:** Cowork runs the theory-derivation half against this inventory, and
the keep/fix/drop triage + the design-pass decisions (mode vocabulary, factorization, fitting
parameterization) go to the user with both halves on the table.

---

*(File note, CC 2026-07-18: this dispatch was delivered inline in the session prompt; no
`cc_instruction_term_inventory.md` existed on disk at session start. Per §6 "force-add this instruction
file", the dispatch text above is committed verbatim as received.)*

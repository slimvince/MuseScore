# CC C1 fold + §2.1 explanation — report

> **Docs/narrative only. No `src/` changes, no build, no tool-code changes, no gate re-measurement, no golden
> refresh, no push.** Discharges the two C1 loose ends (`cc_instruction_c1_fold_and_explanation.md`): Task 1
> (the owed §2.1 baseline-delta explanation) + Task 2 (the accumulated Cowork narrative fold).

## Task 1 — the §2.1 baseline-delta mechanism (benign; NO STOP)

§2.1 of `cc_c1_reliability_report.md` said the harness "reproduces the ratified A-8 variant-(b) key-agree
baseline **exactly**." That was imprecise — the numbers are near-equal, not equal: **68.18 vs 68.11 (Baroque)
/ 64.52 vs 64.43 (Jazz) / 67.77 vs 67.50 (Default)**, same-direction deltas of **0.06 / 0.08 / 0.27 pp**.

**What was read/run to establish the mechanism** (no guess — both aggregation paths read at source + a cheap
read-only scratch recompute, no corpus regen, no `src/` touch):
- `tools/c1_reliability.py` `measure_l3` — reports L3 key respect as **`agree/(agree+disagree)`**: it
  `continue`s on `key_verdict ∈ {keyfail, dcml_keyfail}`, tracking that duration separately as `keyfail_w` and
  **excluding it from the denominator**, so the reliability is conditioned on cells where OUR key parses.
- `tools/a8_rebaseline_measure.py` `measure_preset` — every scored cell gets one `key_verdict`, and the
  ratified baseline is **`agree/scored_dur`** (= `agree/(agree+disagree+keyfail+dcml_keyfail)`), with the
  key-parse-fail slice reported *separately* (A-8 report §2.2: 0.09 / 0.13 / 0.40 %) but kept in `scored_dur`.
- **Scratch recompute over the identical `build_piece_grid` cells [probe]:** `agree/scored` = **68.11 / 64.43
  / 67.50** (reproduces the A-8 baselines) and `agree/(agree+disagree)` = **68.18 / 64.52 / 67.77** (reproduces
  the C1 numbers). The gap is exactly `keyfail% / (1 − keyfail%)` (Default 67.50 × 0.399 %/(1 − 0.399 %) = 0.27
  pp). `join_drop_ticks = 0` on all three presets (the `--dump-region-keymargin` dump reproduces the
  frozen-corpus regions exactly, so the L3 confidence attaches to every cell) and `dcml_keyfail = 0` (all WiR
  keys parse).

**Verdict: a benign DENOMINATOR-SCOPE definition nuance, not a defect** — same numerator, same cells, same
duration weighting, same parser; only the treatment of the ~0.1–0.4 % key-parse-fail slice differs. **No STOP
condition was tripped** (the STOP was reserved for a join/primitive DEFECT — mis-joined cells, wrong parser,
wrong weighting — none of which is present; the join drops zero cells). The §2 reliability curves are
unaffected (they bin the scored/parseable cells; each curve's overall-correct IS the `agree/(agree+disagree)`
conditioning).

**Written as `§2.1a` in `cc_c1_reliability_report.md`** (the addendum), and §2.1's word "exactly" corrected to
"to within 0.06–0.27 pp — the key-parse-fail reweighting." Trailing line-count updated (273 → **305**).

## Task 2 — the narrative fold (reconciliation result)

**Fold commit: `ea6f41eef4`** (`docs(cowork): C1 §2.1a baseline-delta addendum + the accumulated Cowork
narrative fold`). Staged set verified == the dispatch list exactly before commit; **exactly 11 files**
(the §2.1a report + the 10-item list, item 10 = two instruction records):

| # | file | state |
|---|---|---|
| 1 | `STATUS.md` | modified (22g close-out + 22h/22i/22j) |
| 2 | `COWORK_HANDOFF.md` | modified (header + standing record through 22j) |
| 3 | `cowork_score_census.md` | modified (§8b/§8c governance) |
| 4 | `cowork_candidate_lever_register.md` | NEW (R-1…R-13) |
| 5 | `cowork_product_tool_register.md` | NEW (T-1…T-32 + E-1…E-14) |
| 6 | `cowork_polyphony_phrase_harmony_research.md` | modified (§6b at-pin) |
| 7 | `docs/implementation_roadmap.md` | modified (A-8 block + wave-plan) |
| 8 | `cowork_voiceleading_axis_design.md` | modified (§15-4/§5.4 at-pin) |
| 9 | `cc_c1_reliability_report.md` | modified (the §2.1a addendum — tracked; git add) |
| 10a | `cc_instruction_c1_reliability_instrumentation.md` | instruction record (force-add, `/cc_*.md` ignored) |
| 10b | `cc_instruction_c1_fold_and_explanation.md` | instruction record (force-add) |

**Reconciliation — no discrepancies:**
- Every listed file had real changes (none listed-but-unchanged).
- **Left OUT (the only working-tree remainder), correctly:** `idiom_discovery/vl_discovery_out.txt`,
  `idiom_discovery/vl_orthogonality_out.txt` (deliberately-untracked discovery dumps) and `scratch_artifacts/`
  (scratch) — the declared exclusions. No unlisted `cowork_*`/doc modified/untracked file existed beyond these.
- The `muse` submodule was untouched (not staged).
- **Nothing under `src/` in the commit** (`git diff --cached --name-only | grep ^src/` → empty [probe]).

## Confirmation

- **Docs-only:** no `src/` edit, no tool-code edit (`c1_reliability.py` unchanged — Task 1 found no defect, so
  no fix was warranted), no build, no gate re-measurement, no golden refresh. **The batch gate is untouched by
  construction (53/24/53)** — no analysis path or corpus was modified this dispatch.
- **Chain local/unpushed, fork-only** (never `upstream`).

## Deviation surfaced (Task 3 commit placement)

Task 3 asked for this report "force-added in the same commit" while also mandating it cite **the commit SHA**.
Those two are mutually exclusive — a report inside a commit cannot cite its own commit's SHA. Honoring Task 2's
"**exactly this list**" (which does not include this fold report) and the mandatory-SHA requirement, the fold
commit `ea6f41eef4` holds exactly the 10-item list, and **this report is a small follow-up commit citing that
SHA**. Flagged for the record, not worked around silently.

*Report line count: 81 lines.*

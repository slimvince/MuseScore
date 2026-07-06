# CC report — Stage-5 R10-b: the arc-closing RATIFICATION (the batch→robust stop handover is MADE)

> **DOCS + ONE-JSON-SNAPSHOT ONLY.** This dispatch MAKES the R10-a handover surface normative: it rewrites
> the CLAUDE.md gate/stop section to the robust-unit stop, freezes the batch 52/24/52 sets as history,
> corrects the 2.2e key-column error, fires roadmap R10, and closes the Stage-5 arc. **NO `src/` change, NO
> scoring value, NO corpus write, NO build, NO push.** It changes no inference behavior — outside the
> inference-fixing moratorium (this is regression-STOP infrastructure, not an analyzer change).
>
> **Dispatch:** `cc_instruction_stage5_r10b_ratification.md` (Cowork, 2026-07-06). **HEAD at start:**
> `8aea6e33e7` (the R10-a fold). **Branch:** `master`. Fork-only (`origin` = `slimvince/MuseScore`),
> local/unpushed.

---

## Task 0 — state check + the batch stop's LAST run as THE stop (PASS)

- HEAD `8aea6e33e7a4d3eb8077a710a8d5700bd6ce3be0`, branch `master`. Dirty set at start = the two normative
  docs (`CLAUDE.md`, `cowork_stage5_fitter_design.md`) + the new `tools/robust_stop/batch_stop_frozen_history.json`
  + known scratch (`idiom_discovery/*_out.txt`, `scratch_artifacts/`) — as the dispatch expects.
- **Batch stop `characterise_bir_false.py` ×3 = 52 / 24 / 52** (`Corpus OK … git c50002fee1`, 352/352, 326 WiR
  each preset). Case-identity sets parsed from the full enumeration table and diffed element-wise vs the
  CLAUDE.md ratified sets: **set-diff empty both directions, all three presets** (added=∅, removed=∅,
  count-equal). This is the batch stop's final run **as** the stop; after this dispatch it is a diagnostic.

## Task 1 — the CLAUDE.md gate/stop section is now the robust-unit stop (blocks A–D)

The `## Gate threshold and preset policy` section was restructured into four blocks, in order; the opening
threshold-policy paragraph, the `analyze_inversion_errors.py` secondary-metric note, the
"if a gate causes BIR=false regressions" structural-fix policy, and the preset-scoring-caps note were all
**preserved** (surrounding prose, not part of the stop rewrite).

- **(A) THE ROBUST-UNIT REGRESSION STOP (ratified R10-b, 2026-07-06)** — the new hard stop: the
  granularity-robust union-of-boundaries unit, variant (b) DCML-only (music21 is NOT GT), duration-weighted,
  segmentation-invariant; **root governs, RN + key tracked beside**. Committed reference `tools/robust_stop/`
  (per-preset `stem@runStartTick` run enumerations ≈6868/7036/6883 + `summary.json` + `manifest.json`).
  Ratified baselines **root 63.36/62.37/63.25, RN 44.58/42.40/44.41, key 68.13/64.43/67.50** (Baroque/Jazz/Default).
  **Hard stop = class-(b) root-disagree DURATION non-increasing per preset**; **mandatory explained per-run
  set-diff** (zero-new-case cannot scale to ~7k runs); **class-(a) duration tracked** (INVESTIGATE flag,
  `CLASS_A_INVESTIGATE_TICKS = 9600`), never an automatic stop. Runnable check
  `a8_rebaseline_measure.py` → `robust_stop_diff.py` (≈6 s). **Re-baseline discipline for future adoptions**
  (the 2.2e pattern generalized: re-baseline the reference in the adoption commit, run-diff explained + ratified
  per case, class-(b) non-increase proven, manifest re-stamped, outgoing reference snapshotted first per O-12).
  The A-8 dual-track note is folded into block (A), key-column-corrected.
- **(B) The two-tier per-cell class policy — CARRIED OVER, LIVE.** Preserved in full: the class-(a)
  (pc-UNDECIDABLE-root: symmetric dim7/aug/whole-tone + ø7/m6 share-tone) vs class-(b) (everything pc-decidable)
  definitions; the **five guardrails**; the **founding-evidence provenance** (`bwv272@4320`, `bwv289@20160`,
  `bwv291@17760`, `bwv387@10560`; `cowork_gate_policy_amendment.md`, `cc_layer3_jazz_churn_investigation.md`);
  the first-accepted-interim-case record. Reframed to note it now governs the robust unit's per-cell
  classification (class-(b) is ~96.5 % of root-fail time on this unit vs ≈53 % on the old batch residual).
- **(C) RETROSPECTIVE — the batch 52/24/52 stop (superseded, historical).** The `52/24/52` `stem@tick`
  identity-set blocks + the full L3-wiring/2.2e/corrected-parser history RELOCATED here, marked
  historical/superseded, pointing at `tools/robust_stop/batch_stop_frozen_history.json` and this report + the
  assembly report. States: it under-counted the true per-onset root error ~15–56× (a small music21-filtered
  reachable corner) and was replaced at R10-b. The batch stop's diagnostic form (`characterise_bir_false.py`
  KEPT — no longer the stop) + the shared corpus-integrity mechanism (its `validate_corpus_dir` imported by the
  a8 instrument) + the regen/diagnostic commands are retained here (relocated load-bearing prose).
- **(D) Caveats.** Cross-layer-budget caveat (O1) kept **LIVE** (an interpretation caveat, not a granularity
  one). Granularity caveat marked **✅ RESOLVED at R10-b** — the block-(A) robust unit is the mandated
  granularity-robust metric; the historical statement of the problem is kept for provenance, not deleted.

**No load-bearing element dropped** — every relocation preserved the prose verbatim; the two-tier guardrails,
founding evidence, and cross-layer caveat are all live in the rewritten section.

### Task 1b — the A-8 key-column correction, MADE normative

1. In the block-(A) A-8 dual-track note the key column was corrected **68.19/64.52/67.77 → 68.13/64.43/67.50**
   (the reproducible column; authoritative source `tools/robust_stop/manifest.json` `reproduce_status.key`).
2. The contradictory sentence *"its key figure reflects the a8 re-measure, not a 2.2e change"* was **removed**
   and replaced with the byte-identity truth: **Jazz key = the prior 64.43 exactly** (measured 64.4321) —
   identical `.ours.json` + WiR + git-unchanged key-path code cannot move the figure; the recorded 64.52 was a
   non-reproducible measurement-entry error, and by the same corpus+code identity Baroque 68.19 / Default 67.77
   were likewise erroneous (reproducible 68.13/67.50; Baroque a tiny +0.015 pp shift vs the prior 68.11 from the
   kWStepIn re-segmentation, Jazz/Default reproduce the prior to the digit).
3. **Repo-wide grep of `68.19` / `64.52` / `67.77` — per-occurrence disposition:**

| # | location | kind | disposition |
|---|---|---|---|
| 1 | `CLAUDE.md:142` (A-8 dual-track note) | **LIVE NORMATIVE** | **CORRECTED** → 68.13/64.43/67.50 + contradictory sentence fixed (block A) |
| 2 | `cowork_stage5_fitter_design.md` (2.2e EXECUTED log) | historical session log | **ANNOTATED** with a one-line R10-b correction note (not rewritten) |
| 3 | `cowork_stage5_fitter_design.md` O-15 (R10-a record) | historical session log | **left as-is** — already correctly documents 68.19/64.52/67.77 as the erroneous 2.2e-recorded value + names 68.13/64.43/67.50 reproducible |
| 4 | `STATUS.md:20` (discrepancy narrative) | historical session log | **left as-is** — describes the finding (history) |
| 5 | `STATUS.md:48` (R10-a session entry) | historical session log | **left as-is** — correctly describes the discrepancy (history) |
| 6 | `tools/robust_stop/README.md:44,46,49` | committed reference record | **left as-is** — documents reproducible-vs-2.2e (the R10-a reference) |
| 7 | `tools/robust_stop/manifest.json:64,70,76` (`recorded_2_2e` + `match_2_2e:false`) | committed data record | **left as-is** — records the finding as data |
| 8 | `tools/fit_ledgers/*.jsonl` (`key_pct` 68.1912/68.1941/67.7736) | machine-generated audit data | **left untouched** — distinct measured fit-audit values, NOT the ratified baseline triple |
| 9 | `scratch_artifacts/s5_2b_task1_tables.txt` (67.7736) | untracked scratch | **left untouched** |
| 10 | `fonts/*.sfd` (168.194, −568.199, 264.529, 67.7793, 567.773, …) | font glyph coordinates | **left untouched** — coincidental substrings, not the key numbers |

## Task 2 — the batch 52/24/52 sets frozen as history (both forms)

1. **CLAUDE.md:** relocated to block (C) (Task 1), the `52/24/52` `stem@tick` identity sets + full history,
   marked superseded.
2. **Machine-readable snapshot:** `tools/robust_stop/batch_stop_frozen_history.json` written + committed — the
   52/24/52 per-preset `stem@tick` identity sets, provenance (HEAD `8aea6e33e7`, corpus `c50002fee1`, 352/326,
   "SUPERSEDED at R10-b" status, pointer to this report + the assembly report), Default derivation. **Verified
   set-equal to the `characterise_bir_false.py` Task-0 output AND to the CLAUDE.md ratified sets before writing**
   (assertion in the generator; all three presets PASS).

## Task 3 — characterise disposition + roadmap R10 FIRED

1. `characterise_bir_false.py` → **KEPT-AS-DIAGNOSTIC** (R3 pattern): still runnable per-region, no longer the
   stop. Its `validate_corpus_dir` is imported by `a8_rebaseline_measure.py`, so the robust stop's own
   measurement keeps it from bit-rotting (retirement-by-silence guard — documented in CLAUDE.md block (C)).
2. **Roadmap R10 FIRED / design §4.7 EXECUTED:** `cowork_stage5_fitter_design.md` §4.7 carries the
   **★ R10-b FIRED** note (handover MADE, both stops green, R10 fired, arc CLOSED); a new **O-16** observation
   records the full arc-close. The **engage-arc dossier is handed off explicitly:** F-B redesign
   [1043/53/809, net-harmful override] · §15-13 [5544, parked — dormant-resolver objective] · θ/map wiring ·
   L1.5 surface map · GateA unification · the L5 inversion · tonicVote. **The Stage-5 arc is CLOSED.**

## Task 4 — both stops green at close (PASS)

- **Batch stop:** `characterise_bir_false.py` ×3 = **52 / 24 / 52**, set-diff empty both directions vs CLAUDE.md
  (Task 0; nothing under `src/` or `tools/corpus/` was touched, so this holds at close).
- **Robust stop (the successor sandwich, now THE stop — proven green):**
  `a8_rebaseline_measure.py --out-dir <scratch>` (validated grid==oracle OK all three; batch_gate 52/24/52) →
  `robust_stop_diff.py --candidate <scratch>` = **OVERALL PASS (exit 0)**: per preset **+0/−0 runs**, class-(b)
  root-disagree duration **Δ=0** (HARD STOP PASS), class-(a) Δ=0, 0 added / 0 removed runs. Identity-PASS.
- **Corpus** fingerprint-validated untouched (`Corpus OK … git c50002fee1`, all three).
- **Suites (no build — no `src/` change):** unchanged from the R10-a/Phase-3 baseline **composing 1101 (2 disabled)
  · notation 53 (+4 pre-existing skips) · pipeline_snapshot 11** — not re-run, as nothing they cover was touched
  (docs + one JSON only).

## Commit SHAs (this dispatch)

| # | SHA | Type | Contents |
|---|---|---|---|
| 1 — normative | `__SHA1__` | `docs:` | CLAUDE.md gate rewrite (blocks A–D + key correction) · `tools/robust_stop/batch_stop_frozen_history.json` · this report (force-add) |
| 2 — the fold | `__SHA2__` | `docs(cowork):` | STATUS (session 23) · COWORK_HANDOFF (new START-HERE) · `cowork_stage5_fitter_design.md` (§4.7 R10-b FIRED + O-16 + the 2.2e-log annotation) · `cc_instruction_stage5_r10b_ratification.md` (force-add) + the SHA back-fill above |

Provenance SHAs: HEAD-at-start `8aea6e33e7`; corpus `c50002fee1`; a8 instrument `c2914884af`; key parsers
`5f7cb7376e`.

## STOP-condition disclosures

- **No STOP tripped.** No load-bearing element dropped (two-tier guardrails, founding evidence, cross-layer
  caveat all relocated live); every key-number occurrence dispositioned (correct / annotate-history / leave-data);
  `characterise` = 52/24/52 set-diff empty; the robust sandwich is identity-PASS at close; the frozen snapshot is
  set-equal to the CLAUDE.md sets. No `src/` change, no corpus write, no push, no build.

---

*Drafted by CC, 2026-07-06. HEAD-at-start `8aea6e33e7`, corpus `c50002fee1`. Docs + one JSON snapshot only. The
Stage-5 arc is CLOSED; the engage arc opens on the handed-off dossier. Cowork verifies this report at objects →
the batch→robust handover is normative.*

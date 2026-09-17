# CC Instruction — Stage-5 R10-b: the arc-closing RATIFICATION (the batch→robust stop handover is MADE)

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** The user's arc-closing ratification event on the R10-a surface.
> R10-a assembled and verified the handover (reference artifacts, mapping, successor sandwich, draft text);
> **R10-b MAKES it normative.** This dispatch DOES change standing documents — that is its whole purpose —
> but it is a **docs + one-JSON-snapshot** change only: **NO `src/` change, NO scoring value, NO corpus
> write, NO build, NO push.** It changes no inference behavior, so it is outside the "no inference-fixing
> until refactoring/architecture/algorithmics complete" moratorium — this is the regression-STOP
> infrastructure handover, not an analyzer change.
>
> **Cowork verification done (2026-07-06):** R10-a verified at objects (`acba0f0404` feat + `8aea6e33e7`
> fold) AND at runtime — Cowork independently re-ran `a8_rebaseline_measure.py` (grid==oracle OK, batch
> 52/24/52, cell counts match the manifest) and `robust_stop_diff.py` (identity **PASS**, +0/−0 runs,
> class-(b) duration Δ=0 all presets, exit 0). The key finding is confirmed sound (Option 1 was ratified
> 2026-07-06). Both freeze decisions ratified by the user: **freeze the batch sets in BOTH CLAUDE.md history
> AND a machine-readable snapshot.**
>
> **Read first:** CLAUDE.md (the gate/stop sections + the A-8 dual-track note — the text this dispatch
> rewrites) · `cc_stage5_r10_assembly_report.md` (esp. §3.3 draft text, §3.4 cost note, the headline
> finding, the manifest `reproduce_status`) · `tools/robust_stop/manifest.json` (the authoritative
> reproducible numbers) · design §4.7 / O-15.
>
> **Current state:** HEAD `8aea6e33e7` (the R10-a fold), branch `master`, fork-only, unpushed. Batch stop
> **52/24/52** (corpus `c50002fee1`, fingerprint-validated). Reproducible A-8 baselines: root
> 63.36/62.37/63.25, RN 44.58/42.40/44.41, **key 68.13/64.43/67.50 (the reproducible column — NOT the
> erroneous 2.2e 68.19/64.52/67.77)**. Suites 1101/53(+4 skip)/11.
>
> **VS Code bash rules:** append `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read
> files** — use the file tools.

---

## Task 0 — state check + the batch stop's LAST run as THE stop
HEAD, branch, dirty set. Run `characterise_bir_false.py` ×3 → confirm **52/24/52**, set-diff empty both
directions vs the CLAUDE.md ratified sets. This is the batch stop's final run **as** the stop; after this
dispatch it is a diagnostic. Report the confirmation.

## Task 1 — rewrite the CLAUDE.md gate/stop section (the robust-unit stop becomes THE hard stop)

Substitute the batch-stop gate sections with the robust-unit stop, using the **§3.3 DRAFT** in
`cc_stage5_r10_assembly_report.md` as the basis for the new stop definition. **Target structure — four
blocks, in this order. Do NOT delete load-bearing prose; RELOCATE it to the retrospective/caveat blocks.**

**(A) THE ROBUST-UNIT REGRESSION STOP (ratified R10-b, 2026-07-06).** The §3.3 draft text: the unit
(granularity-robust union-of-boundaries cell, variant (b) DCML-only, duration-weighted, segmentation
-invariant); **root governs, RN + key tracked beside**; the committed reference `tools/robust_stop/`; the
ratified baselines **root 63.36/62.37/63.25, RN 44.58/42.40/44.41, key 68.13/64.43/67.50**; the hard stop =
**class-(b) root-disagree DURATION non-increasing per preset**; the **mandatory explained per-run set-diff**;
the runnable check (`a8_rebaseline_measure.py` → `robust_stop_diff.py`, ~6 s); the **re-baseline discipline
for future adoptions** (the 2.2e pattern generalized — an adoption re-baselines `tools/robust_stop/` in the
adoption commit, run-diff explained + ratified per case, class-(b) non-increase proven, manifest re-stamped,
outgoing reference snapshotted first per O-12).

**(B) The two-tier per-cell class policy — CARRIED OVER, LIVE (unchanged).** This is NOT superseded. Preserve
in full: the class-(a) (pitch-class-UNDECIDABLE-root: symmetric dim7/aug/whole-tone + ø7/m6 share-tone) vs
class-(b) (everything pc-decidable) definitions; the **five guardrails** (per-case score verification;
default-to-(b)-on-doubt; class-(b) non-increase; case identities recorded; interim-bridge status); the
**founding-evidence provenance** (`bwv272@4320`, `bwv289@20160`, `bwv291@17760`, `bwv387@10560`;
`cowork_gate_policy_amendment.md`, `cc_layer3_jazz_churn_investigation.md`). It now governs the robust unit's
per-cell classification. On this unit class-(b) is ~96.5 % of root-fail time (vs ≈53 % class-(a) on the old
batch residual) — the robust stop is governed by the meaningful count.

**(C) RETROSPECTIVE — the batch 52/24/52 stop (superseded at R10-b, historical reference).** Relocate the
`52/24/52` `stem@tick` identity-set blocks + their full L3-wiring/2.2e history here, clearly marked
**historical / superseded**. Point at `tools/robust_stop/batch_stop_frozen_history.json` (Task 2) and
`cc_stage5_r10_assembly_report.md`. State: it under-counted the true per-onset error ~15–56× (a small
music21-filtered reachable corner) and was replaced by the robust unit at R10-b.

**(D) Caveats.** Keep the **cross-layer-budget caveat (O1) LIVE** (it is an interpretation caveat, not a
granularity one). Mark the **granularity caveat RESOLVED** — R10-b delivers the mandated granularity-robust
metric; annotate it resolved rather than deleting it.

### Task 1b — the A-8 key-column correction (the declared R10-a finding, MADE normative here)
In the A-8 dual-track note (now part of block A):
1. Correct the key column **68.19/64.52/67.77 → 68.13/64.43/67.50** (the reproducible column;
   authoritative source = `tools/robust_stop/manifest.json` `reproduce_status.key`).
2. **Fix the contradictory sentence** "its key figure reflects the a8 re-measure, not a 2.2e change" —
   replace with the byte-identity truth: Jazz key = the prior **64.43** exactly (identical `.ours.json` +
   WiR + git-unchanged key-path code cannot move the figure — measured 64.4321); the earlier-recorded
   **64.52** was a non-reproducible measurement-entry error, and by the same corpus+code identity Baroque
   **68.19** / Default **67.77** were likewise erroneous (reproducible 68.13/67.50; Baroque shows a tiny
   +0.015 pp shift vs the prior 68.11 from the kWStepIn re-segmentation, Jazz/Default reproduce the prior to
   the digit). Corrected at R10-b.
3. **Grep the three erroneous numbers repo-wide** (`68.19`, `64.52`, `67.77`). For each occurrence: if it is
   a **live normative statement**, correct it; if it is a **historical session log** (STATUS/HANDOFF/design/
   contract session entries), **annotate with a one-line R10-b correction note — do NOT rewrite history**.
   Report the full occurrence list with your per-occurrence disposition.

## Task 2 — freeze the batch 52/24/52 identity sets as history (BOTH forms, user-ratified)
1. **CLAUDE.md:** as relocated in Task 1 block (C).
2. **Machine-readable snapshot:** write + commit `tools/robust_stop/batch_stop_frozen_history.json` — the
   52/24/52 `stem@tick` identity sets per preset, verbatim from the CLAUDE.md ratified sets (verify
   set-equal to `characterise_bir_false.py` output at Task 0 before writing), plus provenance (corpus
   `c50002fee1`, HEAD, date, "superseded at R10-b" status, pointer to `cc_stage5_r10_assembly_report.md`).

## Task 3 — characterise disposition + fire roadmap R10
1. `characterise_bir_false.py` → **KEPT-AS-DIAGNOSTIC** (R3 pattern): still runnable, no longer the stop.
   Note the retirement-by-silence guard already documented in R10-a — its `validate_corpus_dir` is imported
   by `a8_rebaseline_measure.py`, so the robust stop's own measurement keeps it from bit-rotting.
2. **Fire roadmap R10 / execute design §4.7:** mark R10 **FIRED** in `cowork_stage5_fitter_design.md`
   (§4.7 + O-15) and record **the Stage-5 arc CLOSED**. Hand off the engage-arc dossier explicitly:
   **F-B redesign [1043/53/809, net-harmful override] · §15-13 [5544, parked — dormant-resolver objective] ·
   θ/map wiring · L1.5 surface map · GateA unification · the L5 inversion · tonicVote.**

## Task 4 — sandwich + report + fold
1. **Both stops green at close:** `characterise_bir_false.py` ×3 = 52/24/52 set-diff empty (final
   confirmation) AND the robust sandwich (`a8_rebaseline_measure.py` → `robust_stop_diff.py`) identity
   **PASS** (+0/−0, class-(b) Δ=0 all presets) — the robust stop is now THE stop, so prove it green.
2. Corpus fingerprint-validated untouched (`Corpus OK … c50002fee1`). No `src/` change ⟹ no build; note
   suites unchanged from the R10-a/Phase-3 baseline (1101/53+4skip/11) — re-run only if you touched anything
   they cover (you should not have).
3. **Report** `cc_stage5_r10b_ratification_report.md` (force-add): the CLAUDE.md diff summary (blocks A–D +
   the key correction + the grep occurrence list/disposition); the frozen-history snapshot; R10 fired; both
   stops green; all SHAs.
4. **Fold** (`docs(cowork):`): `STATUS.md` (session 23 — the arc-close entry) · `COWORK_HANDOFF.md` (new
   START-HERE header: Stage-5 CLOSED, engage arc inherits the dossier) · `cowork_stage5_fitter_design.md` ·
   `cowork_confidence_contract.md` if it carries the key column · `cc_instruction_stage5_r10b_ratification.md`
   (force-add).

## STOP conditions
- The CLAUDE.md rewrite would **DROP** any load-bearing element (a two-tier guardrail, the founding
  evidence/provenance, the cross-layer-budget caveat) → STOP; relocate, never delete.
- Any key-number occurrence whose correct-vs-annotate disposition is unclear → report it, default to
  **annotate-for-history**, do not rewrite a historical log.
- `characterise` ≠ 52/24/52, or the robust sandwich not identity-PASS at close, or the frozen snapshot not
  set-equal to the CLAUDE.md sets → STOP.
- Any `src/` change; any corpus write; any push; any build-requiring change. (Docs + one JSON snapshot only.)

## Acceptance
CLAUDE.md gate section = the robust-unit stop (A) + two-tier policy preserved live (B) + batch sets
relocated to history (C) + caveats kept, granularity marked resolved (D) ✓ · A-8 key column corrected
68.19/64.52/67.77 → 68.13/64.43/67.50 + the contradictory sentence fixed + repo-wide occurrence list
dispositioned ✓ · `tools/robust_stop/batch_stop_frozen_history.json` committed, set-equal verified ✓ ·
`characterise` kept-as-diagnostic; roadmap R10 FIRED / §4.7 executed / Stage-5 arc CLOSED / engage-arc
dossier handed off ✓ · both stops green at close ✓ · report + fold with SHAs ✓ · no src/corpus/build/push ✓.

*Cowork, 2026-07-06. R10-a verified at objects + runtime; the batch→robust handover is the user's R10-b
ratification, made here. On CC's R10-b report: Cowork verifies at objects → the Stage-5 arc is CLOSED and
the engage arc opens on the handed-off dossier.*

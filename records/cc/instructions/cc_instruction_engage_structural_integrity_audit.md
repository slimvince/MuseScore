# CC Instruction — Engage arc #6: the STRUCTURAL-INTEGRITY audit (total-unification + layer-adherence + workaround detection) — read-only catalogue, ALL built layers

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** The U1 STOP surfaced an architectural smell incidentally: the
> Layer-4 `results` carry is a **cap→workaround tangle** — an arbitrary cap-of-3 truncates a needed
> different-root/inversion alternative, and a "guaranteed inversion alternative" append
> (`harmonicfunctionlayer.cpp:530-549`) reaches *below the cap* to force it back (the cap causes the problem
> the patch fixes), while the same `results` list simultaneously serves winner, carry, that patch, pedal
> detection, and two serialization/display truncations. Found by accident ⟹ likely not isolated. This
> dispatch makes principles **#6 (total unification), #7 (one concern per layer), #1 (build on clean
> theory, not workarounds)** **proactive** — the structural analogue of the information-loss audit — swept
> **systematically across every built layer**, not only where we stumbled.
>
> **READ-ONLY. No `src/` change, no corpus write, no build, no fix.** A grounded, classified catalogue; each
> fix is a later separate ratified event. Investigation + architectural design — moratorium-clear (and the
> fixes it queues are *refactoring*, #8's first category).
>
> **Scope discipline — specific in KIND, comprehensive in COVERAGE (#2):** hunt ONE pattern-class (below)
> across all built layers; deep-diagnose only the confirmed anchor (`results`); sweep-and-classify the rest.
> Do NOT re-derive prior work — **read the existing architecture reviews first and EXTEND them:**
> `cowork_l1l4_architecture_audit.md` (Q1 one-path/total-unification, Q6 principles-adherence),
> `cowork_architecture_review_2026_07.md`, `cowork_implementation_review.md`, and the known **owed
> refactors** already on record (the `chordanalyzer.cpp` file-split parked to R9; the Stage-5 gate
> dissolution) — cross-reference, don't duplicate.
>
> **Grounding rule (binding, #1):** every catalogued site grounded at the code (symbol + line + mechanism);
> a genuine violation distinguished from a legitimate design; ambiguous ⟹ UNCLEAR (never guessed).
>
> **Current state:** HEAD `5fa16b77e0`, branch `master`, fork-only, ahead 0. Both stops green (read-only, so
> untouched). Pending uncommitted CLAUDE.md #12 edit in the tree (leave it; a later dispatch folds it).
>
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read files.**

---

## The pattern-class to hunt (the taxonomy; classify each hit)
- **(a) limit → compensating workaround** — an arbitrary cap/threshold that truncates something needed, plus
  a patch that reaches around it to restore it (the `results`-cap / inversion-append exemplar). The clean
  fix removes/governs the limit so the patch is unneeded.
- **(b) concern-coupling** — one structure serving several distinct concerns that belong in separate
  layers/owners (`results` = winner + carry + inversion-patch + pedal + serialization + display). #7.
- **(c) duplication / multiple-paths-per-concern** — the same logic/decision in more than one place (the
  three `<3` caps for one concern; historically the three `buildResult` wrappers + two promotion idioms —
  now unified; look for siblings). #6.
- **(d) workaround-on-a-mechanism** — a fix layered on a symptom rather than its cause (patch built on a
  cap, a re-rank without recompute, a stand-in value). #1/#3.
- **(e) cross-layer reach-in** — a concern in one layer reading/mutating another layer's structure it should
  not own (pedal detection mutating the chord-readings carry; any read/write that risks the cross-axis
  acyclicity rule). #7.
- **(+) any further structural form the code reveals** — record it (there are likely more than these five).

## Task 0 — state + read the priors
HEAD/branch/ahead; both stops green (read-only). Read the existing architecture reviews + the owed-refactor
records (above) so this EXTENDS them.

## Task 1 — the anchor: deep-diagnose the `results` carry substrate (Layer 4)
Full, code-grounded diagnosis:
- **The complete consumer/concern map** of `results` (winner `front()`; the carry → `HarmonicRegion.alternatives`; the inversion-append; pedal detection `applyIter8691Pedal`; the batch/serialization caps #2; the bridge/display cap #3).
- **The cap→append chain:** confirm at the code + history (`fix_results_cap_exhaustion.md`) that the
  inversion-append exists *only* to counteract cap #1's truncation — i.e. test the hypothesis that a
  properly uncapped/governed carry **dissolves the append entirely** (cap and patch cancel).
- **The concern separation:** which of the coupled concerns belong to which layer/owner; where pedal
  detection (a distinct concern) should read the carry rather than mutate the winning identity in place.
- **The clean-target design** (design only, not built): one governed carry (uncapped or a single principled
  limit), the different-root/inversion alternative as a natural consequence, pedal detection decoupled,
  serialization + display as separate per-consumer views over the one carry.
- **The fan-out** (the user's "see what we have in reality") — measure the untruncated ranked-set size
  distribution per slice ×3 presets, read-only.

## Task 2 — sweep every built layer for the pattern-class
For each built layer + the shared cross-cutting structures, sweep for (a)–(e)(+); ground and classify each
hit. Cover: **L1** notes · **L1.5** phrase boundaries · **L2** segmentation · **L3** key · **L4** chord
(the legacy `analyzeChord`+gates path AND `ChordSliceDecoder`) · **L5** function (dormant) · **L6**
grouping/display · the **voice-leading axis** (VL-A/B/C) · the shared region/slice/confidence carries. Sweep
`tools/` ONLY where an instrument encodes a duplicated concern (e.g. the caps in `batch_analyze`).
Classify each hit: **VIOLATION** (a genuine #6/#7/#1 tangle/workaround/duplication) · **OK** (a legitimate
clean structure with multiple consumers, or a bound with a clear single-concern purpose — not a violation) ·
**UNCLEAR** (grounded but the violation-vs-legitimate call needs user adjudication). No assumed violations.

## Task 3 — the catalogue + the sequencing call
`cowork_structural_integrity_audit.md`: one row per site — location · pattern-form (a–e/+) · layers/concerns
involved · classification (VIOLATION / OK / UNCLEAR) · severity (a cap→workaround or cross-layer mutation on
a load-bearing path = high; cosmetic = low) · the clean-target sketch. Then:
- The **prioritized fix-queue** (each VIOLATION a later separate ratified refactor), with the `results`
  substrate + its clean-target as the anchor entry.
- **★ The sequencing recommendation (the load-bearing output):** which fixes are **prerequisite refactors to
  do BEFORE the Layer 5 engagement design** (#8 — restructuring first; e.g. untangling the carry Layer 5
  will consume) vs which fold **into** it — cross-referenced to the owed R9 file-split + the gate
  dissolution so the refactor order is one coherent plan, not piecemeal.
- The UNCLEAR rows for user adjudication.

## Task 4 — report + fold + push
1. Report `cc_engage_structural_integrity_audit_report.md` (force-add): method, layers swept, counts by
   classification, the anchor diagnosis, the sequencing call, all SHAs.
2. Sandwich (trivial — read-only): no `src/`; both stops untouched; suites unchanged (no build).
3. Fold (`docs(cowork):`): the catalogue + report · `STATUS.md` · `COWORK_HANDOFF.md` ·
   `cowork_stage5_fitter_design.md` (engage observation) · this instruction (force-add). Leave the pending
   CLAUDE.md #12 edit untouched.
4. Push fork-only — never toward `upstream`/`musescore/MuseScore` (`cfc7eb5e39` HARD STOP).

## STOP conditions
- Any `src/` change, corpus write, build, or fix (read-only catalogue only).
- Any catalogue entry not grounded at code, or any violation-vs-legitimate call **assumed** rather than
  verified — mark UNCLEAR (#1).
- Over-flagging: a legitimate clean structure with multiple consumers, or a bound with a clear single-concern
  purpose, is **OK**, not a violation (the info-loss audit's over-flagging guard, carried over).
- Re-deriving the prior architecture reviews instead of extending them (#6 — don't duplicate the review).
- Any push toward `upstream`/`musescore/MuseScore`.

## Acceptance
Priors read + extended (not re-derived) ✓ · the `results` substrate deep-diagnosed: consumer map, the
cap→append dissolution hypothesis tested, the concern separation, the clean-target design, the fan-out ✓ ·
every built layer swept for the (a)–(e)(+) pattern-class, each hit grounded + classified (VIOLATION / OK /
UNCLEAR) + severity-ranked ✓ · the prioritized fix-queue + **the pre-L5-vs-part-of-L5 sequencing call**
cross-referenced to the owed refactors ✓ · catalogue + report + fold with SHAs ✓ · no src/corpus/build/fix;
both stops green; pushed fork-only ✓.

*Cowork, 2026-07-06. Engage arc #6 — total-unification + layer-adherence made systematic, all built layers.
Read-only; every fix is its own ratified refactor. On CC's report: Cowork verifies the catalogue at objects
→ brings you the fix-queue, the sequencing call, and the UNCLEAR rows to adjudicate.*

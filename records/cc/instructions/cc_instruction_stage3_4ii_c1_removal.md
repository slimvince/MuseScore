# CC Instruction: Stage 3.4-ii — C1 gate removal, gated on a non-chorale spot-check

## Context

Dossier `cc_stage3_4i_dossier.md` §5(A) found E/F/K/Iter-86 fire on 0 regions across
353 Bach chorales × 3 configs ("dead-in-practice"), with the honest caveat that the
corpus is chorales only and E/F/K target inversion/augmented shapes that
classical/romantic repertoire exercises more. **Cowork decision: spot-check non-chorale
scores BEFORE any removal.** "Dead on chorales" is not "dead"; this run earns the
stronger claim or keeps the gate. Base: `a652dc1ba7`. Method A–H; held means held.

## Task 1 — The non-chorale spot-check (the gating measurement — do this FIRST)

The DCML MS3 sets are already cloned (`tools/dcml/{mozart_piano_sonatas,chopin_mazurkas,
corelli,bach_en_fr_suites,beethoven/ABC}/MS3/*.mscx`). Using the SAME env-driven
`gateDisabled()` harness from 3.4-i (re-add it; prove inert when unset = it does not
alter the enabled path):

1. Pick a deliberately gate-favorable spread — NOT random. E/F target Minor→Major
   inversions (stepwise bass); K targets augmented first-inversions. Choose scores
   likely to contain them: several Mozart sonata movements + Chopin mazurkas +
   Beethoven quartet movements (chromatic/augmented-rich) + a Corelli or two. Aim
   ~15–25 movements; **state your selection rationale per gate** (don't just grab the
   first N — pick for the shapes).
2. Run each of E, F, K, Iter-86 disabled (one at a time) over this set via
   `batch_analyze` (Standard/Baroque preset — the only config where the preset-gated
   block runs; verify E/F/G/H need Baroque, K/Iter-86 are not preset-gated so run all
   configs for those two). For each gate: **does it fire anywhere** (any region's
   winner changes when disabled)?
3. Report per gate: fired / did-not-fire, with the firing scores+ticks if any, and the
   DCML verdict on a sample of fires (is the gate's correction right where it fires?).

**This measurement decides each gate's fate** — do not pre-judge from the chorale 0s.

## Task 2 — Removals, gated on Task 1

For each of E / F / K / Iter-86 INDEPENDENTLY:

- **If Task 1 shows it fires NOWHERE** (chorales AND the non-chorale spread): remove it
  — delete the gate block, convert its Stage-1b pin to a `// historical logic, retired
  Stage 3.4-ii (fired on 0 regions, chorale + non-chorale corpora)` note or delete the
  pin (justify which; a pin for deleted code is dead weight, but a pin documenting the
  retired shape may have value — your call, stated). Update scoring_model §6.
- **If Task 1 shows it FIRES anywhere**: KEEP it. It becomes a C2 3.2-acceptance case
  instead (the decoder must reproduce that fix at wider beam) — add it to the dossier's
  §5(B) table with the measured firing case. Report, do not remove.

## Task 3 — Per-removal proof gate (each removal its own commit)

Per gate removed: build + composing/notation suites + snapshots 11/11 zero-diff +
corpus A/B ×3 sha256 (expect 0/353×3 by construction — it fired nowhere). ANY diff =
the gate was NOT dead = STOP, revert that removal, reclassify (a diff here means the
spot-check missed a chorale-corpus fire, a real finding).

Commits (one per retired gate, ALL held for Cowork ratification — held means held):
`refactor: retire Gate <X> (Stage 3.4-ii — 0 fires on chorale + non-chorale corpora)`.
The harness is reverted before committing; tree byte-identical to `a652dc1ba7` plus the
removals.

## Task 4 — Dossier addendum + doc riders

Append to the dossier (or a new `cc_stage3_4ii_report.md`): the spot-check selection +
results table + per-gate fate (retired / kept-as-C2). Update the 3.4-i dossier §5(B) if
any gate moved from C1 to C2. Note for the handoff which gates remain for 3.2.

## Report — inline + `cc_stage3_4ii_report.md`

§1 spot-check selection rationale + fire/no-fire results + DCML sample; §2 per-gate
fate; §3 per-removal proof-gate table + commit hashes (proposed, held); §4 the updated
C2 set for 3.2.

Stop conditions: a removal showing any corpus/snapshot diff (missed fire — stop,
reclassify); the spot-check unable to load the non-chorale MS3 scores (report the
obstacle — the snapshot harness loads .mscx, so batch should too; if not, that's the
finding); any temptation to remove a gate that fired (it's C2 now, not dead).

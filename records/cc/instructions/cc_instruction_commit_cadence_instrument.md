# CC Instruction: commit the cadence detector as a byte-identical instrument (NOT wired)

## Decision + framing

User chose **option C** (2026-06-14): pivot to Stage 6; **commit the cadence detector + diagnostic as an
instrument** (like the key-candidate dump precedent) to preserve the verified work and feed Stage 6 —
**separately from any decision to wire it into the resolver** (4c-ii wiring is deferred to a later,
Stage-6-informed integration). This commit is **byte-identical** (the detector is diagnostic-only; the
production resolver never calls it — Cowork-verified at source: `keyresolver.cpp` has zero detector refs).

## Commit exactly these files — the cadence instrument, nothing else

Stage and commit ONLY:
- `src/composing/analysis/section/cadencekeyanchor.h`
- `src/composing/analysis/section/cadencekeyanchor.cpp`
- `src/composing/tests/cadencekeyanchor_tests.cpp`
- `tools/batch_analyze.cpp` (the `--dump-cadence-anchor` diagnostic + the phrase-boundary/notated-signature
  reading that feeds it)

**Do NOT stage:** the gitignored `cc_*.md` reports, the gitignored `tools/corpus/**` regen, the gitignored
measurement scripts (`tools/cc_floor_classify.py`, `tools/b2_measure.sh`, etc. — leave them on disk),
`docs/` edits, `STATUS.md`/`COWORK_HANDOFF.md` (Cowork's). Confirm `git diff --cached --name-only` lists
**exactly the four files above** before committing; if anything else is staged, STOP and report.

## Verify byte-identity BEFORE committing (the instrument gate)

The resolver/winner must be untouched. Confirm:
- BIR gate **57 / 23 / 57** all three presets (identity sets unchanged);
- `pipeline_snapshot_tests` **11/11 zero golden diffs**;
- composing (incl. the 17 cadence-anchor tests) + notation suites green.
If any move, the detector leaked into scoring — STOP and report (it must be diagnostic-only).

## Commit message

```
feat(key): key-agnostic authentic-cadence detector + diagnostic (Stage 4c instrument, not wired)

A note-derived global tonic+mode anchor for the relative-major/minor key decision, built
key-agnostically (absolute root motion + chord quality + leading-tone presence + notated
signature for raised-LT salience + fermata/final-region for structural weighting; NEVER the
resolved key/mode/degree). Diagnostic-only: the production resolver does not call it (byte-
identical -- BIR 57/23/57, snapshots 11/11 zero-diff).

Measured realized detection 75.2% / clean-stem contradiction 25.3% on the relative-pair floor
(cc_stage4c_i / 4c_iii reports); too high to wire ungated. The residual is dominated by
dominant/subdominant tonicizations -- a functional-understanding gap that belongs to Stage 6
(tonicization vs cadence vs modulation). Wiring (gated 4c-ii) is deferred to a Stage-6-informed
integration. This commit preserves the verified instrument; it changes no analysis output.
```

**Do NOT push** (user pushes). Report the new commit hash + `git log --oneline -4`. Note the chain: this
commits on top of HEAD `cfc7eb5e39` (4a); the local-only history grows by one composing commit — the user
manages push/order.

## Stop conditions
- Anything other than the four files staged (report before committing).
- Any byte-identity movement (gate/snapshot/suite) — the detector leaked into scoring; STOP.

# Verify m340 Classification — Recon + Possible Fix

**Scope:** The MuseScore-parser recon
(`docs/musescore_parser_special_notations_recon.md`, commit
`ee50b1760c`) classified m340 as "Roman-only diff — already a
ConventionDiff; symbol matches." But the chord_mismatch_report
still lists m340 as RealDiff. Reconcile: either the test's
classification logic is wrong (and m340 should be flowing into
ConventionDiff), or the recon's read was wrong, or there's a
subtlety neither has surfaced.

This is a small read-then-decide session: investigate, surface
findings, and either fix the test classification or document
why m340 stays in RealDiff.

**Reference docs (read first):**
- `docs/musescore_parser_special_notations_recon.md` — the recon
  that classified m340 as already-ConventionDiff
- `src/composing/tests/chord_mismatch_report.txt` — current
  report; m340 entry shows actual catalog vs analyzer text
- `docs/extension_stripping_policy.md` — describes the
  progressive comparison protocol
- `src/composing/comparison_utils.h` (or similar) — likely home
  of `classifyComparison` and the protocol implementation

**Memory references** (auto-loaded):
- `project_no_stripping_in_production` — analyzer outputs maximal
- `project_chord_symbol_ban`

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).
3. Force rebuild and verify fresh binary timestamps. Build dir:
   `ninja_build_rel/`.

---

## Investigation phase

### Q1 — m340 entry in current chord_mismatch_report

Read `src/composing/tests/chord_mismatch_report.txt` for m340.
Capture verbatim:
- Catalog's expected text (chord symbol + Roman if both are tracked)
- Analyzer's actual text (same)
- Any other relevant fields the report has (notes, key context, etc.)

### Q2 — Why is m340 in RealDiff?

Read `classifyComparison`'s implementation (in the comparison
utility file). Walk through what happens when m340's catalog and
analyzer texts are passed in:

- Direct comparison: do they match? (Probably not, since it's a
  RealDiff)
- Progressive stripping: does any (degree, alterations-mode)
  combination produce a match between the two strings?
- If yes at some degree: should classify as ConventionDiff. Why
  doesn't it?
- If no at any degree: should classify as RealDiff. The recon's
  "symbol matches" claim was wrong.

Determine which scenario is actually happening. The recon's
claim ("symbol matches under stripping") is a testable assertion
— either the strings DO match under some stripping config and
the test isn't catching it, or they DON'T match and the recon was
wrong.

### Q3 — Roman vs symbol distinction

The recon mentioned "Roman-only diff" — implying the chord-symbol
comparison passes but the Roman numeral comparison fails. If the
test's RealDiff classification is based on EITHER symbol OR Roman
mismatching (i.e., RealDiff if any field disagrees), then a
Roman-only diff legitimately produces RealDiff status.

Two interpretations:
- **(α) Test conflates symbol and Roman.** If test classifies
  RealDiff when ANY field mismatches, m340 is correctly RealDiff
  even though the symbol matches. Recon's framing was loose.
- **(β) Test should treat fields independently.** Symbol can be
  ConventionDiff while Roman is RealDiff; the entry should be
  classified per-field rather than as a single bucket.
- **(γ) The Roman match logic is also stripping-aware.** If
  Romans go through their own classifyComparison (perhaps with
  Roman-specific stripping), and m340's Romans match under
  stripping, then the "Roman-only diff" framing would mean
  ConventionDiff for both fields → entry should be ConventionDiff
  overall.

Determine which model the test code actually implements. The
finding determines whether m340 is correctly classified or
mis-classified.

### Q4 — What does the recon's "symbol matches" mean concretely?

Re-read the recon's m340 analysis. It said the chord symbol
matches catalog under stripping. Verify by manually stripping the
analyzer's output text at degree 7 with both alterations modes
and checking against catalog. Does it actually match?

If yes: classification logic should treat as ConventionDiff. If
the test reports RealDiff anyway, the test has a bug (or model α
applies).

If no: the recon was wrong; m340 is correctly RealDiff and the
recon's classification needs updating.

---

## Decision point

Based on Q1-Q4, decide whether to fix or document:

- **Fix path:** test classification has a bug — symbol matches
  under stripping, Romans match (or are out-of-scope for this
  test), so m340 should be ConventionDiff. Update the
  classification logic to handle this case. Verify m340 moves
  out of RealDiff. composing_tests baseline drops by 1.
- **Document path:** test classification is correct — m340 is
  legitimately RealDiff because some field genuinely disagrees.
  Update the parser recon's m340 row to reflect this. No code
  change.

**Halt and surface findings before making either change.** Don't
silently fix or document; explain what you found and propose the
direction. The user approves before changes land.

---

## If fix path is approved

Cache pipeline_snapshot_tests baseline:
`cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_m340_baseline/`

Implement the targeted fix in `classifyComparison` or wherever
the per-field classification logic lives. Verify:

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./composing_tests.exe                 # baseline drops by 1; m340 no longer in RealDiff
./pipeline_snapshot_tests.exe         # 10/10 byte-identical
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_m340_baseline/
                                       # zero output
./notation_tests.exe                  # 53/53
```

Update the test's pinned RealDiff baseline reference (currently
4 per the formatter audit fix) to the new value (3).

Update `docs/musescore_parser_special_notations_recon.md`'s m340
row if the recon's framing needs adjustment.

---

## If document path is approved

No code change. Update
`docs/musescore_parser_special_notations_recon.md` to clarify
m340's status. Note in the verdict that "symbol matches but
some other field genuinely diverges" — explain which field and
why.

The composing_tests baseline stays at 4.

---

## Commit + push

Single commit reflecting whichever path was approved. Suggested
message skeletons:

**Fix path:**
```
Fix m340 classification — should be ConventionDiff not RealDiff

The MuseScore-parser recon (commit ee50b1760c) classified m340
as "symbol matches under stripping; only Roman differs." But the
test's classification logic was treating m340 as RealDiff
[because reason from Q3 finding].

Fix: [brief description of the test-logic change]

composing_tests RealDiff baseline drops from 4 to 3.

pipeline_snapshot_tests: 10/10 byte-identical.
notation_tests: 53/53.
```

**Document path:**
```
Document m340 RealDiff status — symbol matches but [field] differs

The MuseScore-parser recon (commit ee50b1760c) had framed m340
as "symbol matches under stripping; only Roman differs," implying
ConventionDiff classification. Investigation reveals:
[finding from Q1-Q4].

Updates docs/musescore_parser_special_notations_recon.md to
clarify the m340 entry's actual status.

composing_tests RealDiff baseline stays at 4.
```

**Push to origin at end of session.**

---

## Report back

- Investigation summary: Q1-Q4 findings
- Verdict: fix path or document path; decision rationale
- User approval received before changes landed
- Commit hash + push confirmation
- Test results
- Any deviations and why

---

## Scope guardrails

- **Do not** modify the catalog (`chordanalyzer_catalog.musicxml`).
  Standing do-not-touch.
- **Do not** modify analyzer logic (`analyzeSection`, `analyzeChord`,
  passes, formatters). The investigation is about test
  classification, not analyzer behavior.
- **Do not** modify pipeline_snapshot_tests harness. m340 is in
  composing_tests, not the snapshot suite.
- **Do not** silently fix or document — halt for approval at the
  decision point.
- If the investigation reveals broader test-classification issues
  beyond m340 (e.g., the per-field logic is misclassifying
  multiple entries), surface and pause; don't broaden scope
  unilaterally.

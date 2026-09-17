# CC Instruction: Measure the Default (user-run) gate config under the corrected parser

## Why

The 57/23 verification (`cc_gate_rebaseline_verify_report.md`) covered Baroque and Jazz, but
the CLAUDE.md gate section has a THIRD identity: **Default (the user-run config) = 14 =
Baroque-13 ∪ {bwv187.7 @ m14.b2}** (CLAUDE.md line 108). The corrected GT parser changes the
gate the same way it did for Baroque/Jazz, so Default-14 is now stale/undercounted too.
Before Cowork rewrites the gate section, the Default number must be measured — not guessed.
This closes the gate-section rewrite as ONE coherent change.

## Task (READ-ONLY analysis + corpus regen — same regime as the verify run)

1. Reproduce the OLD Default = 14 through the **canonical** tool with the HEAD-committed
   (pre-fix) parser blobs (the same A/B method you used for Baroque/Jazz: temporarily revert
   `dcml_parser.py`+`compare_analyses.py`, run, restore, verify staged blobs byte-identical).
   Confirm the OLD Default identity set = Baroque-13 ∪ {bwv187.7@...} (capture the exact
   `bwv187.7` tick — CLAUDE.md says m14.b2 but record the actual `stem@tick`).
2. With the **staged corrected parser**, measure the NEW Default via the canonical tool over
   the HEAD-stamped Default-config corpus (regenerate it if a Default-preset corpus dir isn't
   already present/valid at HEAD — 353/353, manifest-stamped). Report the **new Default
   count + full `stem@tick` identity set**.
3. Confirm **strict superset / 0 lost** (OLD-14 ⊆ NEW) via `comm -23`, exactly as for
   Baroque/Jazz. Report any lost case as a finding.
4. Spot-check that any Default-specific ADDED cases (beyond the Baroque +44) have
   oracle-correct GT roots `[oracle]`, and note whether they fall in the same
   ambiguity-dominated classes (symmetric-dim7 / viio-share-tone) or introduce a new class.

## Constraints

READ-ONLY + corpus regen only. Metric-batch fixes stay STAGED/HELD — **no new commit**. Do
NOT edit CLAUDE.md / STATUS.md (Cowork does the rewrite once this lands). No
production/engraving change (P3 out). Never-guess — if the Default-preset corpus mechanics
are unclear or a case can't be classified, report the unknown rather than assume. Stop if
the OLD config does not reproduce 14, or the regen isn't 353/353, or any OLD case is lost
(would mean the move is not a strict superset for Default).

## Report

Append to / alongside the verify report: the OLD-14 identity set, the NEW Default count +
identity set, strict-superset confirmation, and the ambiguity/actionable character of any
Default-specific additions. Every number [probe], every root [oracle].

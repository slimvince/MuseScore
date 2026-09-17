# CC instruction — the merged note-seam re-plumb (status bar + interaction + context menu on `noteView`) + the split-check living mode (seams-2 unit "note-seam")

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (the lean INDEX; open
> `open_items/OI-<n>.md` details as needed), `C:\s\MS\cowork_notation_output_contract.md`
> (§1 the note seam; §3.3 the slice; the presentation-derivations amendment).
>
> **What this is:** one unit of the notation-layer migration (P0–P4 + P-strings + the register
> split are DONE — the handoff's dated blocks are the record; `cc_instruction_notation_seams_2.md`
> is REFERENCE ONLY). This unit is the RATIFIED MERGED note-seam re-plumb (the P3 re-partition:
> the status-bar/note-context path + the old P5 consumers, ONE unit, because they share the
> `NoteHarmonicContext`↔record string-carriage — which this unit resolves ONCE). Plus one small
> register-tooling fix first.
>
> **Current state:** branch `master`; expected HEAD `599eebd45e` (P4 Task 3+4, pushed) —
> verify via `git show --stat 599eebd45e`; mismatch = STOP. Riding Cowork edit:
> `cowork_handoff.md` (commit with Task 1; verify it is the only non-yours tracked diff).
> This dispatch file stays untracked.
>
> **Hard stops, always:** push origin only; ANY behavior change with `useJointNotationRecord`
> OFF — byte-identity per commit (three suites green, NO golden refresh); no legacy-analysis
> call on the record path; no inference edit; no [0,1] remap of the nats gap; files outside
> the touchable set; a surprise is a STOP (#13). VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-27, at the P4 verification.

**Touchable set:** `src/notation/internal/**` (the note-seam consumers + the composing-bridge
note-context path), `src/notation/view/**` (ONLY `notationcontextmenumodel` if it lives
there — locate, don't assume), `src/composing/analysis/joint/**` ADDITIVE-only if a `noteView`
accessor gap surfaces, `tools/open_items_split_check.py` + `open_items/` + `OPEN_ITEMS.md`
(Task 1 only), the relevant test dirs + CMake lists, `ARCHITECTURE.md`, `STATUS.md`, the
riding Cowork file. NOT touchable: the joint inference files (the boundary guard enforces
this), corpus, goldens, `tools/robust_stop/`.

---

## Task 1 — the split-check living mode (OI-202: row created, fixed, flipped — ONE commit)

The P4 report's finding: `tools/open_items_split_check.py` compares only against the frozen
split baseline (`cb246a7580`), so every legitimately-added post-split item (OI-201, and every
future one) false-fails the count check. Fix:

1. The instrument gains a **living mode** (the default): (a) index rows ↔ detail files are a
   bijection (every ID both places, no duplicates, no orphans); (b) NO detail file carries a
   status line of its own (the two-place drift killer, checked mechanically — the header
   sentinel line must be present, and no `| OPEN`/`✅ RESOLVED`-style status cell outside the
   verbatim historical row block); (c) for the ORIGINAL 200 items, the byte-verbatim
   reconciliation against the frozen baseline stays exactly as is (the historical guarantee
   does not weaken); post-baseline items are checked structurally (a+b), never against the
   baseline. The historical split mode stays invocable (`--split-baseline`), and the committed
   `split_reconciliation.json` stays UNTOUCHED (it documents the split event).
2. Run the living mode; it must PASS on the current tree (OI-201 + OI-202 structural, the 200
   verbatim). Output artifact: `open_items/register_check.json` (the living report, #17f).
3. **OI-202**: index row + detail file created in this commit (the finding, quoted from the P4
   report, provenance `599eebd45e`'s report) and flipped ✅ RESOLVED in the same commit with
   this commit's mechanism (the created-and-resolved pattern, OI-195 precedent).

## Task 2 — the record-arm `NoteHarmonicContext` carriage (resolved ONCE)

The single-note surface (`analyzeNoteHarmonicContext` / `analyzeNoteHarmonicContextDetails`)
gains its record-arm branch: flag ON → the record (the produced whole-score record; reuse the
same production call pattern the P3a/P4 emitters use) → `noteView(rec, tick)` → ONE builder
that fills `NoteHarmonicContext` from record facts:

1. `chordResults[0]` = the committed segment via `chordResultFromRecordSegment` (the
   P-strings converter — the ONE record-segment→`ChordAnalysisResult` path, #6);
   `chordResults[1..]` = the §3.3 chord-axis alternatives through the SAME converter, ordered
   committed-first then descending content score (the contract's view ordering; the ordering
   difference vs legacy is the known P6-classified class); each alternative's
   `.identity.score` = its §3.3 content score (the audited score-suffix disposition).
2. `keyFifths`/`keyMode` from the record's two-mode key; `keyConfidence` = the RAW key-axis
   gap in nats, documented at the field write (the raw-nats rule — no remap; the field is
   carried, no in-tree reader, per the audit).
3. The pedal fields stay false/-1 (suspended, OI-194); `temporalExtensions` default (audited
   no-reader).
4. If the bounded-window decode cache (`buildWindowSection` and kin) integrates awkwardly
   with the whole-score record, do NOT force it: the record arm may bypass the window cache
   (whole-score produce per invalidation, the P3a/P4 pattern) — but any USER-VISIBLE
   performance regression concern is noted for the report, not silently absorbed, and any
   structural incompatibility is a FINDING.

## Task 3 — the three consumers on the carriage

1. **Status bar** (`analyzeHarmonicContextAtTick` → … → `harmonicAnnotation`): the record arm
   flows through the Task-2 builder; the string renders via the SAME
   `formatChordResultForStatusBar` family (P-strings) — the accessibility chain follows
   automatically (audited string-only).
2. **`notationinteraction.cpp:8311`** (harmony write): record arm writes the display symbol /
   Roman from the carriage (the P-strings forms).
3. **`notationcontextmenumodel.cpp:194`**: the menu builds from the carriage's
   `chordResults` (+ the "(%.2f)" suffix showing the §3.3 score, labeled as such by the
   audited disposition); the "tune as" entries read root/quality as today.
4. Tests: golden-less structural pins per consumer (the established P3a/P4 pattern) — the
   menu/status/harmony outputs equal the record's own published facts on ≥2 corpus scores;
   the ordering rule pinned; the out-of-span tick and produce-failure edges (nothing written,
   no partial output, #13).

## Task 4 — doc sync + closing

`ARCHITECTURE.md` (the note seam as-built: every audited consumer now dual-arm; what remains
before the switch = P6 + P7); `STATUS.md` closing entry. Commits per change-class (suggested:
Task 1; Task 2; Task 3+4); push origin.

## Report

Hashes; the living-mode check result (counts, PASS); the carriage's field-by-field source list
(the audit CSV note-seam rows each named); the cache disposition (integrated / bypassed-with-
note / FINDING); per-consumer pin evidence; suite totals per commit; reuse-vs-new /
what-retires (expected: the converter + formatters reused; `NoteHarmonicContext` itself
retires at the map — the carriage is transitional, say so); anomalies (a surprise is a STOP).
Standing self-check before reporting.

**After this unit:** P6 — the dual-arm classified comparison over the FULL notation output
surface (the switch-ratification evidence; catalogue includes OI-201 and the applied-chord
Nashville "?" convention), then P7 (doc sync/close), then the user's switch ratification.

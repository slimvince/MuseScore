# CC instruction — implode + tuning record paths, the exposure-bucket unification, the OI-182 execution (seams-2 partition unit "P4")

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (the lean INDEX; open
> `open_items/OI-<n>.md` details as needed — you will UPDATE OI-182's row + detail file in
> this dispatch), and `C:\s\MS\cowork_notation_output_contract.md` (§4 consumer mapping, §4.1
> presentation gates, the top presentation-derivations amendment).
>
> **What this is:** one unit of the notation-layer migration (the seams-2 partition; P0–P3a,
> the register split, and P-strings are DONE — the handoff's 2026-07-26/27 blocks are the
> running record; `cc_instruction_notation_seams_2.md` is REFERENCE ONLY for the ratified
> amendments it holds). This unit re-plumbs the LAST two span-seam consumers — the implode
> bridge (chord track) and the tuning bridge — onto the record path behind the existing
> default-OFF `useJointNotationRecord` flag, and executes the OI-182 register disposition.
>
> **Current state:** branch `master`; expected HEAD `b2c71fb6e3` (P-strings Task 3+4, pushed)
> — verify via `git show --stat b2c71fb6e3` and that HEAD matches; mismatch = STOP. Riding
> Cowork edit: `cowork_handoff.md` (commit with your first commit; verify it is the only
> non-yours tracked diff). This dispatch file stays untracked.
>
> **Hard stops, always:** push origin only; ANY behavior change with the flag OFF —
> byte-identity proven per commit (three suites green, NO golden refresh); no legacy-analysis
> call on the record path; no inference edit anywhere; no [0,1] pseudo-confidence mapping of
> the gap (the raw-nats rule); files outside the touchable set; a surprise is a STOP (#13).
> VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-27. **The ruled context this unit executes:** the
exposure-bucket unification was ratified to land HERE (the P2a pattern: threshold once, per
arm, at the set site; consumers read the stored result); the record arm's gate constants come
from the committed P1 measurement (`tools/notation_seams/exposure_constants.json`) at FULL
precision — the assertive one (`kAssertiveKeyExposureGap = 1.055757`) is already declared at
`sectionrecordadapter.cpp` (P2b); the tentative one is declared in this unit from the
artifact's exact value; **the 0.35 mode-suffix gate is NOT re-declared** — under the ratified
two-mode display rule the exotic mode suffix does not exist on the record path, so
`modeNameConfidenceThreshold`/`fallbackModeSuffix` retire there (the measured g₀.₃₅ stays in
the artifact as record, unwired); `kSameChordReannotationGap` (960 ticks) re-homes unchanged
as a declared presentation-timing constant. Display strings on the record arm go through the
P-strings paths (`chordResultFromRecordSegment` → `formatChordResultForStatusBar` family) —
never a new formatter.

**Touchable set:** `src/notation/internal/notationimplodebridge.{cpp,h}`,
`src/notation/internal/notationtuningbridge.cpp`,
`src/composing/analysis/section/**` (ONLY the per-arm bucket set-site, the P2a pattern),
the relevant test dirs + CMake lists, `ARCHITECTURE.md`, `STATUS.md`, `OPEN_ITEMS.md` +
`open_items/OI-182.md` (the execution update), the riding Cowork file. NOT touchable: the
joint module's inference files (the boundary guard will enforce this anyway), corpus, goldens,
`tools/robust_stop/`.

---

## Task 1 — the exposure-bucket unification (the P2a pattern completed)

1. The tentative/assertive BUCKET (`keyExposureBucket`, today thresholding
   `normalizedConfidence` at 0.5/0.8 inside the implode bridge) re-expresses as a stored
   per-arm result set ONCE at the section layer's set site (beside `hasAssertiveExposure`):
   legacy arm from `conf >= 0.5 / 0.8`; record arm from `gap >= kTentativeKeyExposureGap /
   kAssertiveKeyExposureGap`. Declare `kTentativeKeyExposureGap` from the committed artifact's
   EXACT `chosen_gap_nats` for the 0.5 row (read the artifact; do not transcribe from any
   report's rounding), with the full citation (value, legacy rate, record rate, residual).
2. The implode bridge reads the stored bucket; its local 0.5/0.8 re-thresholding retires from
   the read sites (the constants' definitions stay until the legacy path retires — mark them
   as legacy-arm-only where they remain live).
3. **Legacy byte-identity proven:** same value, same thresholds, same stage — any legacy
   output change is a STOP. Tests: bucket equality on the legacy arm (fixture mirroring the
   set site), record-arm bucket behavior on corpus pieces via `produceNotationRecord`.

## Task 2 — the implode bridge record path

Behind the flag, the implode entry (`notationimplodebridge.cpp:1374` cluster) derives its
section from the record (`produceNotationRecord` → `analyzeSectionFromRecord` — the P3a
pattern), then the existing implode machinery runs with these record-arm specifics:

1. Key runs / KeySig writes: fifths from the record's two-mode key (already on the derived
   regions); the key-run LABEL uses the two-mode form only — the exotic-suffix branch
   (`fallbackModeSuffix` + `keyAnnotationBaseLabel`'s exotic case) is legacy-arm only
   (comment: retires with the legacy path; the modal reading is the published successor fact).
2. Exposure gates: the stored bucket (Task 1) — no confidence literal anywhere on the record
   arm.
3. Chord-track strings: display symbol / Roman / Nashville via the P-strings shared paths.
4. Voicing/tones: the derived regions' tones (the adapter's composing-side re-collection —
   already delivered at P2b); the voicing dedup runs unchanged over them.
5. Coalescing: the audited semantics unchanged; `kSameChordReannotationGap` re-homed to the
   emitter site as a declared presentation-timing constant (same value, documented role) if it
   does not already sit there — a re-home, not a re-tune.
6. Borrowed-key/relationship/pivot branches that enumerate exotic modes: record arm takes the
   two-mode form; exotic enumeration is legacy-arm only.

## Task 3 — the tuning bridge record path

Behind the flag, `notationtuningbridge.cpp:762`'s region loop reads record segments (span,
rootPc, quality, key) — the audited rows are direct record fields; the single-note path reads
`noteView`. The tuning system's inputs are facts (pcs, keys), not display strings — if any
tuning input turns out to need a fact the record does not carry, that is a FINDING (#12),
not a port.

## Task 4 — the OI-182 execution + doc sync

1. **OI-182:** update the INDEX row (status → executed-at-the-record-surface, dated) and
   append the dated execution note to `open_items/OI-182.md`: every constant's disposition
   with its site — `kAssertiveKeyExposureGap` (P2b, `sectionrecordadapter.cpp`, cited),
   `kTentativeKeyExposureGap` (this unit, cited), the mode-suffix 0.35 gate RETIRED on the
   record path (C1; g₀.₃₅ unwired by design), `kSameChordReannotationGap` re-homed unchanged,
   the legacy 0.5/0.8 literals now legacy-arm-only. Never a status line in the detail file.
2. `ARCHITECTURE.md` (the implode/tuning record paths as-built; the completed bucket
   pattern); `STATUS.md` closing entry.
3. Commits per change-class (suggested: Task 1; Task 2; Task 3+4); the riding handoff on the
   first; push origin.

## Report

Hashes; the Task-1 legacy-equality evidence + the declared tentative constant (exact value +
citation); the implode record-arm behavior evidence (which snapshot/test pins what — new tests
golden-less, structural, per the P3a precedent; NO golden refresh); the tuning record-arm
evidence; any FINDING (an unsatisfiable consumed fact, quoted); the OI-182 update text; suite
totals per commit; reuse-vs-new / what-retires (expected: implode/tuning machinery reused over
the derived section; the exotic-suffix and confidence-literal reads become legacy-arm-only —
retiring at the map, say so); anomalies. Standing self-check before reporting.

**After this unit:** the merged note-seam re-plumb (status bar + `notationinteraction` +
`notationcontextmenumodel` on `noteView`, the string-carriage resolved once) → P6 (the
dual-arm classified comparison — the switch-ratification evidence; its catalogue includes
OI-201 and the applied-chord Nashville "?" convention) → P7 (doc sync/close). Each its own
fresh Cowork-written instruction.

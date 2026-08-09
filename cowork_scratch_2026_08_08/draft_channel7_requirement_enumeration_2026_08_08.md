# DRAFT — channel 7, the requirement-side enumeration: user-visible tasks → serving mechanism → establishment on the implied population

> **COWORK READING SURFACE — landed at the return STOP 2026-08-09; NOT ratified.** Phase-2 preparation for the outside-in channel. Method
> per §4: from each thing a user does, inward — which mechanism serves it, and is that
> mechanism established on the population the task implies? Gaps are rows. Sources this
> session: `ARCHITECTURE.md` §12 read in full (7191–7316), the §12.1b nine-action table, the
> OI-242 correction, the family rows, the seams records. ⟲ re-derived 2026-08-09: the away batch stopped
> before its Task 7, so the OI-349 probe has NOT run and the D-472/stabilization cell is
> unchanged (D-472 homed at the Layer-6 section with both arm ends visible; OI-349 OPEN and
> GATING; probe timing the user's call); re-derive again when that probe lands.
>
> The §12 governing requirement frames the whole channel: ZERO INFORMATION LOSS TO THE END
> USER — every inferred object displayable. So each task below also asks: can the user SEE
> what the analysis knows here, including its uncertainty?

## The task table (the probe's row inventory, drafted)

| # | User-visible task | Serving mechanism (record arm) | Establishment on the implied population — known state |
|---|---|---|---|
| 1 | Read the status bar on a selected note | note-seam funnel → whole-score `produceNotationRecord`, synchronous, per single-note selection | NOT established for large scores: seconds to tens of seconds (OI-203/OI-206); §12.1a corrected 2026-08-02 — cost is NOT negligible and suppressing the display WOULD skip the analysis; whether the preference becomes a performance control is OPEN |
| 2 | Annotate a span (chord symbols / RN / Nashville, single + selection forms — six actions) | record path, action-scoped | chorale-established via goldens; 13 of 23 large scores yield an EMPTY analysis (OI-215/227) → the actions silently produce nothing there; the all-or-nothing shape is the #12 failure the family design owes |
| 3 | Implode to chord track | record path implode seam, action-scoped | same empty-analysis exposure on the orchestral class; established on chorales |
| 4 | Tune selection / "Tune as ⟨reading⟩" context submenu | tuning region path + per-reading retune | same exposure; the right-click CHORD anchor is `notes().front()` — derivation not recorded, an engraving order not a musical one; OPEN at OI-257 |
| 5 | Edit continuously while composing (the up/down-arrow loop) | every keystroke is an edit → invalidates memoization → full re-analysis on next selection | the measured field case: ~20 s per keystroke on a sixty-bar arrangement (the OI-206 finding); unresolved by design — waits on the extent question (OI-210), deliberately LAST per the make-it-work-first rule |
| 6 | Analyze a symphony at all | the decode itself | the OI-215/227 cliffs: majority of the committed orchestral set gets NO answer; the family design's subject |
| 7 | Ask "why this reading?" | the two full candidate lists (D-006) are published; an explanation SURFACE for them | partial: the record carries alternatives; §12.2–12.4 (navigator, alternatives panel, tension curve) are PLANNED, not built — the explainability row (OI-154) is this gap's tracker; probe should restate what a user can reach TODAY vs the §12 zero-loss requirement |
| 8 | Trust a displayed reading's KEY | the root-governed measurement understates wrong-key damage (D-576, gate block (A)) | the caveat is recorded at the figures; the user-facing question — is there any display of key uncertainty? — is unprobed |
| 9 | Use a transposing-instrument score | the mixed concert/written representation (OI-246) | unexercised by the fit corpus; a family input; no notation-feature census piece covers it yet (channel 1's probe (b) does) |
| 10 | Rely on accessibility (screen reader) on analysis surfaces | §12.1 Qt accessibility patterns; `notationaccessibility.cpp` | the localization/accessibility non-conformance rows from the 2026-08-02 census (OI-245…OI-257 area; ⟲ re-derived 2026-08-09: OI-257 RESOLVED 2026-08-02 with the right-click chord anchor recorded "derivation not recorded" and its rightness left OPEN; the rest of the census-row set unmoved by the away batch — per-row states re-read when the probe runs) |

## What the probe itself would do (when phase 2 opens)

For each row: cite the serving mechanism at the code (most citations already exist above),
state the population the task implies (a composer's real score, not a chorale), and give the
establishment verdict with its evidence — established / established-on-the-wrong-population /
not established / no mechanism exists. Rows 1, 5 and 6 are already known-red and rowed; the
probe's yield is the rows NOBODY has opened: 7 (what is reachable today vs the zero-loss
requirement), 8 (key-uncertainty display), 10 (the accessibility residue). Predictions before
running (#17b); every gap a row; no fix inside the probe.

## One structural observation for the phase-2 surface (not a finding)

Rows 1–6 all converge on the two decisions already sequenced elsewhere: the extent question
(OI-210, deliberately last) and the family design (phase 3). Channel 7's marginal value is
therefore rows 7–10 — the cheap unopened ones — which supports running it EARLY and SMALL
rather than as a grand pass: it is mostly reading, and mostly done above.

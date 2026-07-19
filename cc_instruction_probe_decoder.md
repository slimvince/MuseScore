# CC instruction — the probe decoder (the funnel's read-only-probe stage; identity weights; measured against written predictions)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, **`cowork_joint_estimator_factorization.md` in FULL (the
> ratified structure this decoder implements — §1 variables, §2 score form WITH the granularity
> amendment, §3 factors, §5 decode incl. the below-threshold scoring rule)**,
> `cowork_factorization_desk_simulation.md` §1–§2 (the hand-computed tables this decoder must
> reproduce in its establishment mode), `cowork_sensitive_cell_probe.md` (ratified findings), and
> the OI-176/OI-177/OI-178/OI-180 rows.
>
> **Current state:** branch `master`, HEAD `b28b4a8fdb` (verify). One Cowork-authored uncommitted
> doc edit rides YOUR commit: `cowork_handoff.md` (the probe-stage state line; verify it is the
> only non-yours diff). **PYTHON-ONLY — this is the funnel's READ-ONLY PROBE stage, a measurement
> instrument, NOT the production build: no `src/` file is touched at all; no build, no test-suite
> run, no golden, no corpus regen, no re-baseline. The OI-178 adoption protocol is NOT in play —
> nothing here proposes adoption; this measures whether the ratified structure delivers, before
> any C++ exists.** Pinned instruments and `tools/robust_stop/` import-only, as always.
>
> **This is an explorational measurement run** (the ratified scope-of-surprise rule): a result
> outside the prediction bands below is ALLOWED here and is exactly what the stage exists to
> find — it is REPORTED prominently, never tuned away. **No value may be adjusted anywhere in
> response to any measured number (the firewall, grep-proven as in every fit dispatch).**

**Dispatch author:** Cowork, 2026-07-19, at the user's direction. Layer home:
`tools/joint_estimator/` (measurement instrument). The eventual production module builds ONLY
after this probe's results are reviewed by the user; the probe's outputs then serve as the
module's parity oracle.

## Task 1 — implement the probe decoder (`tools/joint_estimator/probe_decoder.py`)

The ratified decode, at identity weights (every factor weight = 1 — the mandated generative
baseline), over the committed inputs (`note_events/note_events.json`, `tables_all.json`,
`note_tables_all.json`, `factor_presence_all.json`):

- **States:** (key = 12 tonics × {major, minor}) × the chord-class vocabulary observed in the
  fitted tables (degree, quality, inversion figure, applied target — the normalized classes).
- **Events and segments:** the committed event lattice; segmentation is decided by the decode
  (semi-Markov); a segment is a contiguous event run carrying one (key, chord-class) state; key
  changes only at segment boundaries (the ratified variable structure).
- **The score of a candidate segmentation+labeling** = the sum over the ratified factors at the
  ratified granularities: the signature/declared-mode prior (INITIAL state only, re-anchored at a
  notated signature change — the ratified §3.10 form; signature and declared mode read from the
  same corpus-xml headers the table fit used); the pitch-emission per tone (category ×
  covariates); the chord-factor presence penalty per event of segment length (the §2 amendment;
  the factor_presence table supplies P(absent)); the spelling term per tone; the bass factor per
  event (the event's lowest sounding pitch against the segment's chord, through the
  bass/inversion table); the same-key chord transition per boundary (incl. the applied-relation
  cells); the key transition and entry tables at key changes; the boundary factor per event
  (boundary/no-boundary by beat class, event-level values). **The below-threshold scoring rule is
  the ratified §5 paragraph** (leftover mass apportioned by the outcome class's mode frequency —
  implement it once, document where).
- **Declared omissions (report them on every artifact):** the cadence factor (its feature weights
  are deliberately unfit until the weight-fitting stage) and the fermata term (fermatas are not in
  the note-event extraction — an extraction addendum owed; flag it). No substitute for either.
- **Decode:** exact semi-Markov Viterbi with the block-factorized transition (same-key vs
  key-change), plus the per-piece posterior summary the ratified §5 requires (at minimum: the
  best path, its score, and the runner-up key reading per segment span with its score gap).
  A segment-length cap only if the ratified established default demands it — state what you use.
  Measure and report decode time per piece (the tractability fact the §5 reserve decision needs).

## Task 2 — establish the decoder before any corpus number is read (the Class-B obligation)

**Injected-table parity mode:** a mode that swaps in the desk simulation's declared provisional
tables (its section 1, verbatim — including its cadence values, since the hand arithmetic used
them) and decodes the desk simulation's five synthetic cases (its §2: the authentic cadence, the
relative-pair ambiguity, the modally-notated opening, the tonicization, the deceptive cadence)
over their declared candidate sets. **The decoder's totals must reproduce the hand-computed
totals of the desk-simulation document to ±0.05,** case by case, including the near-tie
(−14.39 vs −14.32) and the retroactive flip. Any mismatch is a STOP — the decoder, not the hand
arithmetic, is presumed wrong until shown otherwise. Also reproduce, with the FITTED tables, the
fitted-probe recomputation of the bwv352 reading pair (both bass variants) and the bwv10.7
merge-versus-split comparison (`cowork_sensitive_cell_probe.md` §2–§3) to the same tolerance,
under the same declared leftover-rule variants that document used. Report the full parity table.

## Task 3 — decode the corpus and grade, against these written predictions

Decode all 326 covered pieces; write the committed decode artifact (per piece: segments, states,
scores, the posterior summary; provenance-stamped). Grade side-by-side on the robust unit through
the imported measurement chain (read-only), against the DCML ground truth — the same unit as the
committed baselines. **The predictions (Cowork, #17b, written here BEFORE any measurement — the
ratified asymmetric expectation: the joint structure's payoff is on the KEY axis; the chord-root
axis competes against years of hand-tuning):**

| axis (duration-weighted agree, 326 pieces) | current committed baselines (Baroque / Jazz / Default) | predicted for the identity-weight probe |
|---|---|---|
| key vs the LOCAL key | 65.99 / 62.98 / 65.71 % | **70–80 %** (direction: UP, the load-bearing prediction) |
| key vs the HOME key | 71.42 / 67.83 / 70.65 % | 72–82 % (UP) |
| chord root | 66.04 / 64.98 / 65.93 % | **55–70 %** (may sit BELOW current — stated in advance) |
| Roman numeral | 46.33 / 44.10 / 46.23 % | 40–55 % |

A result outside a band is a prominently-reported finding (allowed in this explorational run),
with the first-order mechanism diagnosed at 3–5 named pieces (which factor mis-carried) — never
adjusted for. Also report: per-piece decode time (mean/max), the ten pieces with the largest
key-axis wins and losses versus the Default baseline, and abstention/coverage facts (there should
be none — the probe commits its best path everywhere; verify).

## Commit

**One commit:** `tools: the probe decoder — ratified decode at identity weights; established against the desk-simulation hand arithmetic; corpus decode + side-by-side grading (read-only probe stage)` —
the decoder, its artifacts, this file (force-add), the one riding Cowork doc edit. Push **origin
only** (the standing hard stop on the upstream remote).

## Self-check before reporting (standing rule)

Re-read the actual diff: nothing outside `tools/joint_estimator/` + this file + the named handoff
edit; no pinned instrument modified; no `src/`; the firewall grep clean (the decoder imports
tables and note events; the GRADING import is confined to the Task-3 measurement step and cannot
feed back into any value); all figures generated. Report: the parity table (Task 2), the
prediction-versus-measured table (Task 3), timings, the win/loss piece lists with the named-piece
diagnoses, reuse-versus-new, anomalies. Surprises are the purpose of this stage — report them
loudly, build around nothing.

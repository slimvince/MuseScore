# CC instruction — where the analysis time goes: the cost profile, the scaling law, the editing cycle, the extent-candidate discrimination, and the ground-truth inventory (READ-ONLY; no fix, no design)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md`,
> `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX), and the detail files this
> dispatch serves: `open_items/OI-206.md` (the interactive regression — its dated notes carry
> the call-path facts and the Stage-3.1b correction), `open_items/OI-203.md` (the measured
> note-seam latency), `open_items/OI-188.md` (the decode prune cannot reach the ground truth —
> it bounds every ceiling claim, and it is why buying speed by pruning is not free),
> `open_items/OI-191.md` (the weight vector is under-determined across restarts),
> `open_items/OI-162.md` (the phrase-boundary layer is built but dormant — the gap is wiring,
> not detection), `open_items/OI-18.md` (the temporal-extension cluster: specified, never
> coded), `open_items/OI-38.md` / `open_items/OI-57.md` / `open_items/OI-39.md` (corpus
> onboarding, the stale extra-scores registry, single-composer risk). Also
> `docs/p3_granularity_ab_3_1b.md` (the shelved whole-score interactive prior, with its
> measured evidence), `cowork_architecture_review_2026_07.md` §7 (the Tristan stress case,
> especially finding F-11: in a texture that suppresses cadences and punctuation, the phrase
> profile goes flat and everything gated on it starves), `docs/score_inventory.md` (score
> locations and their intended use — read before touching any score), and `ARCHITECTURE.md`
> §2.14 (the **effort preset**, quick / normal / ambitious: ratified, unimplemented, with its
> two standing design rules — every cost-driving choice is an explicit setting, never a
> hardcoded constant; every expensive refinement is a cleanly separable on/off stage).
>
> **What this is.** The user has stated a standing requirement: **very large scores must be
> handled** — a full act of Tristan, a symphony — and considers that use case more common than
> the chorale corpus we fitted on. Today a single-note click on a sixty-bar six-staff
> arrangement costs about twenty seconds, and every pitch-change keystroke re-pays it. This
> dispatch establishes **what the analysis costs, why, and which of the candidate designs below
> are even viable** — measurement only. It is the measure-before-build stage of #17's funnel.
> The design decision surface is Cowork's next step, built on these artifacts.
>
> **What this is NOT.** Not a fix. Not a cache. Not the effort setting. Not a scope change.
> Not an inference change of any kind. The user's ruling stands: it is too early to implement
> the effort setting, because we do not yet know factually which parts of the inference must be
> switchable — establishing that is what this measurement is for.
>
> **Current state:** branch `master`; expected HEAD `2e139d2a06` (the OI-206 investigation's
> notes+doc commit, pushed) — verify; mismatch = STOP. Riding Cowork edits: `cowork_handoff.md`
> and `STATUS.md` ride your first commit; they are the only expected non-yours tracked diffs.
> This dispatch file stays untracked.
>
> **Hard stops:** origin only; **NO `src/` production change** (test-layer and `tools/`
> instruments only); no golden, no `tools/corpus/`, no `tools/robust_stop/` movement; no
> behavior change anywhere. **A surprise is a STOP (#13)** — and note the specific exposure:
> these orchestral scores are a class the fact adapter and the decoder have never seen. VS Code
> bash rules (`; echo "exit:$?"`, redirect large output) on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-28, at the user's ratification of the measurement plan, of
committing the large-score set, and of the candidate list in §A below.

**Touchable set:** `tools/extra scores/large/` and `tools/extra_scores_registry.json`;
`.gitattributes`; the test dirs (instrumented measurement drivers); NEW instruments and
artifacts under `tools/notation_seams/` and/or `tools/joint_estimator/`; the register INDEX and
detail files; `STATUS.md`; `docs/score_inventory.md`; the riding Cowork files.

---

## §A — The candidate designs this measurement must discriminate between

The open question is: **what temporal extent of the score does the analyzer read when answering
a query, and how often must it re-read it?** Those are two independent axes, and the candidates
occupy different cells. **This dispatch does not choose between them. It is designed so that
its results can eliminate some of them.** Every task below states which candidate it
discriminates.

*Extent:* (1) the whole piece; (2) a fixed bounded window around the query; (3) a window grown
from the query until the reading stops changing; (4) the enclosing musical unit — phrase, key
area, up to the nearest structural boundary (cadence, double bar, fermata, rehearsal mark);
(5) the viewport plus a margin, rather than the selection.

*Frequency:* (i) per query; (ii) once per edit; (iii) once, then patched incrementally — the
whole piece read once, and after an edit only the affected span re-analyzed and spliced.

*Also on the table:* answer immediately from a small extent and revise when a wider reading
arrives.

**The record's own status of this question (established, 2026-07-28, `cowork_handoff.md`):** it
was originally ratified as whole-piece ("decode-once-query-many", question Q1); overturned on
measurement at Stage 3.1b (2026-06-12) when the A/B falsified the whole-piece premise and it was
**shelved with evidence**; and explicitly **parked**, not answered — 3.1b's disposition says it
may not be re-attempted "without resolving the granularity question as a deliberate product
decision… it needs the granularity-robust metric the 2.2-i dossier mandated." **That
precondition is now satisfied** — the granularity-robust unit was ratified 2026-07-06, three
weeks before the seams dispatches specified whole-score without a ledger premise. So re-opening
the question is the route the record prescribes, not a departure from it.

**Predictions recorded BEFORE measuring (#17b).** These are bands to be checked and, if wrong,
reported as findings — not conclusions to be confirmed. A measurement designed so that it cannot
falsify them is a defective measurement (#18/#19).

- **The user's, 2026-07-28, in his words:** "always read the entire score will VERY likely not
  survive (maybe only under some effort setting = EXTREME)" — i.e. whole-piece is expected to
  end up as the top rung of the effort control's temporal dial, not as the default.
- **Cowork's:** that the embedded-table parse per call is immaterial (single-digit
  milliseconds), so the cost sits in the decode; and that cost is roughly linear in note events
  with a large constant set by segment cap × candidate keys × chord classes.
- **Yours:** state your own before you measure, per task.

---

## Task 0 — the register rows, the score set, and its registration

**0a. The register rows** (rule (c): index row AND detail file, in the commit that records the
discovery). Assign the next free IDs in order, run the living register check, and report the ID
mapping. Six rows, all discovered 2026-07-27/28 in the Cowork session:

1. **The large-score requirement** — user-directed 2026-07-28, in the user's own words: very
   large scores (a full act of Tristan, a symphony) must be handled, and are expected to be a
   more common use case than the corpora we hold. Status OPEN as a **standing design
   requirement**, not a defect: every subsequent design is judged against it. Record the
   collision it creates: the joint estimator's ratified tractability envelope is chorale scale
   (60–150 events, exact decode, documented pruning reserve), the fitted corpus is 326 Bach
   chorales by one composer (OI-39), and OI-38 already mandates late-romantic through atonal
   expansion. Link OI-200, OI-188, OI-38, OI-39.
2. **The analysis-extent question is open and the implementation contradicts the last ruling** —
   the §A history above, recorded as its own row so the question has a home: ratified as
   whole-piece, overturned and shelved with evidence at 3.1b, parked pending a metric that now
   exists, and currently implemented as whole-piece by dispatch specification without a ruling.
   Cross-reference OI-207 and OI-208 (this is the case that motivated both) and OI-18 (the
   specified, never-coded extension design).
3. **The parked crash** — the user crashed MuseScore while making a hidden piano part visible in
   a sixty-bar arrangement on the switched build; a second attempt did not reproduce.
   User-directed: parked pending recurrence, no work now. Status OPEN — observed once, not
   reproduced. Record the decisive cheap test for when it recurs: reproduce with
   `useJointNotationRecord = false` (the dormant legacy arm), separating a MuseScore
   part-visibility fault from anything of ours. Record the sub-question it raised: whether
   hidden staves feed the analysis input at all.
4. **The record producer analyzes the whole score regardless of the requested span** —
   `produceNotationRecord(score, stem, excludeStaves)` takes no tick range; all four record-arm
   seams (annotation emit `notationcomposingbridge.cpp:1495`, implode
   `notationimplodebridge.cpp:1420`, tuning, note seam `notationcomposingbridge.cpp:732`)
   analyze the entire score and narrow the result by view afterwards, while every legacy arm
   passed the actual span into `analyzeHarmonicRhythm` (`:1509`, `:1434`) — for Roman numerals,
   the selection plus a deliberate ~8-bar lookahead (`kMaxPivotLookaheadRegions`). Both a cost
   multiplier on every seam and an **analysis-input scope change** made without a ruling; the
   contract's span seam specifies the opposite ("the caller names a score span; the record for
   that span is returned").
5. **The `addAnalyzedHarmonyToSelection` per-note multiplier** —
   `notationinteraction.cpp:8256`/`:8311` calls the note-seam funnel **once per selected note**,
   so an N-note selection costs N whole-score analyses on the record arm.
6. **The embedded tables are stored as JSON text and parsed per call** —
   `jointembeddedartifacts.h` states the artifacts are embedded "VERBATIM (JSON bytes, not a
   parsed-structure codegen) and parsed at load through the SAME parser as the filesystem
   path"; `jointnotationproducer.cpp:37-40` states they are "loaded fresh per call (a
   shared/cached loader is a later, measured concern)". Ratified Decision D1 said "compiled-in
   constant data" without settling the form; the verbatim-bytes-plus-shared-parser form was
   chosen in Cowork's codegen dispatch on carried-forward-establishment (#19) and one-parse-path
   (#6) grounds, and **its runtime cost was never declared or measured**. Row this as a
   **decision record with an undeclared cost**, not a performance defect; Task 1 measures whether
   it matters at all.

**0b. The score set.** The user has added 23 scores under `"tools/extra scores/large/"` (quote
the path — it contains a space). Per the user's ratification these are **committed**, in the
tracked no-ground-truth class documented in `docs/score_inventory.md` (`ground_truth: false`),
consistent with the committed performance-corpus precedent rather than the gitignored
research-corpus one.

Before committing: **add an explicit `*.mscz binary` rule to `.gitattributes`** and prove
byte-identity across the commit round trip (hash on disk, commit, re-check out into a scratch
worktree, re-hash, compare). `.gitattributes` currently normalizes `* text=auto` with no `.mscz`
rule, and this repository has been bitten twice by line-ending normalization (OI-195, OI-34); a
corrupted score would be a silent, hard-to-diagnose fault. Any mismatch is a STOP.

**0c. Registration** (`tools/extra_scores_registry.json`, `ground_truth: false`). Per file,
**measured, never estimated**: note-event count as the fact adapter counts it, staff count,
measure count, file size, work and transcription source, and the **licence** as far as the
file's own metadata determines it (several names indicate OpenScore, which is CC0; others may
differ). Do not guess a licence — record "undetermined" and list those files in the report. This
is also a partial discharge of OI-57 (140 registry entries against 163 files on disk); note it
in the OI-57 detail file, do not close the row.

Three name pairs are the same work at very different sizes — Beethoven 9 (6.15 MB / 5.91 MB),
Jupiter (4.62 MB / 0.31 MB), Brandenburg 3 (2.86 MB / 0.12 MB). **Do not prune them.** Determine
what each actually is (full score vs reduction, embedded media vs plain, different
transcriptions) and record it; two transcriptions of one work at different densities are useful
data for a scaling law.

**Load failures are findings, not obstacles.** Any score that fails to import, throws, or
exhausts memory is reported with its diagnosis, never quietly dropped.

## Task 1 — where the time goes (the phase profile)

*Discriminates: every candidate. Nothing can be chosen until this exists.*

For each score in the existing performance corpus (`kPerfCorpus`) **and** each of the 23 new
scores, measure ONE cold `produceNotationRecord` at the record arm, broken into phases with wall
time, share of total, and peak memory:

1. **Score reading / fact extraction** — `buildAdapterFacts`.
2. **Table and weight loading** — the embedded-artifact parse, per call (row 6 above).
3. **The decode** — and within it, **mandatorily separated** (this split is the point of the
   task, not an optional refinement):
   - **segment content scoring** — the per-segment, per-(key, class) scoring that depends only
     on the segment's own contents and position, and
   - **the dynamic program** — the transition and path machinery that couples segments across
     the piece.
4. **Record assembly** — derived chord facts, spelling derivation, modal-reading counter, and
   the §3.3 posterior slice.

**Why the split in (3) is mandatory.** It decides whether *incremental patching* (extent: whole
piece, frequency: once then patched) is viable at all. Content scores are position-local and
were already proven reusable: the window study memoized them across overlapping windows by
(stem, span, key, class, pitch-class set) and established memo-on equals memo-off byte-identical.
If content scoring dominates, incremental patching is promising and the whole-piece extent may
survive at acceptable cost. If the coupled dynamic program dominates, it is not, and the extent
axis is where the cost must be paid. **Report which, with the numbers.**

**Name this hypothesis and test it:** the ratified §3.3 amendment publishes the **full**
scoreable candidate lists — all 104 chord classes and every candidate key, per segment, with no
truncation. On a chorale that is small; on a symphony with thousands of segments it may dominate
time and memory. If it does, that is a finding about a **ratified decision** (the full-list
amendment, user-ratified 2026-07-26, whose ledger explicitly excluded top-N and gap-window
truncation) and is reported as such — nothing about it is changed here.

## Task 2 — the scaling law

*Discriminates: whether the whole-piece extent can survive at any effort setting, and how the
extrapolation to Tristan scale behaves.*

Report how total and per-phase cost scale against **note-event count** and, separately,
**staff count** — with uncertainty (#24). A scaling exponent quoted without a confidence
interval is not established. Report residuals and diagnose any score departing from the fit.

Staff count must be reported as its own axis, not folded into events: orchestral density is the
new regime, and whether cost grows with simultaneity beyond its effect on the event count is
exactly what the chorale corpus could never show.

State, from the fitted law, what a full act of Tristan would cost, with the extrapolation's
uncertainty and declared assumptions — flagged as an extrapolation, never as a measurement.

## Task 3 — the editing cycle (the reported pain)

*Discriminates: the frequency axis — per query versus once-per-edit versus incremental.*

Using Task 1's instrumentation and the committed call-path facts
(`tools/notation_seams/callpath_facts.json`), measure on at least the sixty-bar-arrangement size
class and one large score, reporting **cost per user action**:

1. **A pitch change** (up/down arrow on a selected note): what re-runs, how many
   `produceNotationRecord` calls it triggers, total cost per keystroke. The undo-stack counter
   advances, so anything memoized on it is invalidated — establish that at the code and in the
   measurement.
2. **A navigation step** (left/right arrow): a selection change with no edit. Establish that the
   undo counter does *not* advance, and measure per-step cost.
3. **A multi-note command** — `addAnalyzedHarmonyToSelection` over selections of increasing
   size, measuring the per-note multiplier directly.

## Task 4 — discriminating the extent candidates

*This task exists so the design surface is decided by facts rather than by argument.*

**4a — the true cost of growing.** The window study measured the reading at each width but not
the cumulative cost of *getting there*. Measure the total cost of the grow-until-stable loop —
decode at width 4, test, widen, decode again — against a single decode at the final width, on
the large scores. Growing is only cheap if the repeated decodes reuse work; Task 1's content
memo tells you whether they can.

**4b — do structural boundaries exist in this repertoire?** The enclosing-musical-unit candidate
depends on boundaries being detectable. The phrase-boundary layer already reads fermatas,
barlines and silences but is dormant (OI-162), and the Tristan review's F-11 predicts that in
punctuation-poor textures the profile goes flat. Read-only, over the 23 large scores plus the
existing corpus: what boundary evidence exists per score (fermatas, double bars, rests across
all parts, rehearsal marks), what the resulting unit sizes would be in bars and events, and how
many scores have long stretches with no boundary at all. **Report the distribution, not an
average** — the failure mode is the tail.

**4c — the viewport question.** Report the event count contained in a typical screen of each
large score, so the viewport-anchored candidate can be priced against the same scaling law.

**Record your predictions for 4a–4c before measuring.**

## Task 5 — the ground-truth inventory (read-only)

*Discriminates: whether the accuracy half of the extent question can be measured at all yet.*

Enumerate the Roman-numeral-annotated material actually on disk (`tools/dcml/`, plus whatever
`docs/score_inventory.md` and the registries record), with, per corpus: repertoire, size range,
chromatic character, annotation coverage, and whether the annotation has been established as an
instrument (#21) or merely exists.

Answer one question plainly: **is there, on disk today, annotated material both substantially
larger and substantially more chromatic than a Bach chorale?** If yes, name and size it. If no,
say so — that answer makes the accuracy half dependent on OI-38, which is the user's to schedule.

Do NOT download, convert, or onboard anything. This is an inventory.

## Task 6 — dated notes, docs, close

Dated notes on OI-203 and OI-206; the new rows from Task 0a; `STATUS.md` entry;
`docs/score_inventory.md` gains the `large/` subfolder in its `tools/extra scores/` section
(#10). Commits per change-class: (0) rows, scores, registration; (1+2) profile instrument and
artifacts; (3) editing cycle; (4) extent discrimination; (5) ground-truth inventory; (6) notes
and docs. Push origin.

**NO fix, NO design, NO effort setting, NO scope change anywhere in this dispatch.**

## Report

Hashes per commit. The Task-0 ID mapping and licence-undetermined list. The Task-1 phase table
per score (events, staves, phase times, shares, peak memory), **with the content-scoring versus
dynamic-program split answered explicitly** and the posterior-slice hypothesis answered. The
Task-2 fitted scaling law in events and in staves, with uncertainty, residual outliers, and the
Tristan extrapolation with its assumptions. The Task-3 cost-per-user-action table. The Task-4
answers: the true cost of growing, the boundary-availability distribution with its tail, the
viewport event counts. The Task-5 plain answer. Your prediction-versus-measured table for every
band declared, including whether the evidence bears on the user's recorded expectation that the
whole-piece extent will not survive as a default — **report that honestly in whichever direction
it falls; a measurement that could only confirm it would be worthless.**

Anomalies, load failures and memory exhaustion, each diagnosed. A surprise is a STOP (#13), and
an orchestral score is a class neither the adapter nor the decoder has seen, so treat any
anomaly on one as stop-and-report rather than a curiosity.

Standing self-check before reporting: re-read the actual diff of every touched file against the
guiding principles, the conventions, the gate policies, and `DEFECT_TYPES.md`.

**After this dispatch:** Cowork presents the analysis-extent and interactive-cost decision
surface — the §A candidates rated on these numbers against the guiding principles and the
ultimate objective, with the 3.1b evidence, the Tristan review, and the user's framing that the
effort control is one setting with several dials including a temporal one. Then OI-207 (the
decision-conformance audit), then the marginals C++ follow-up.

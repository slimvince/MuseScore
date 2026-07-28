# OI-199 joint P3/P4 dispatch — Task 0 PRE-REGISTERED prediction bands (#17b)

> **Written BEFORE the measuring run** (`cc_instruction_oi199_joint_p3_p4.md` Task 0: "No prediction,
> no run"). Session 2026-07-28, base HEAD `b14a523112`. The instrument + harness are compiled but the
> `JointFireFit` / `JointFireLarge` DISABLED sweeps have NOT been run at the time this file is written.
> OI-219 is the standing reminder that the last dispatch failed to register bands; this is the guard.
> Each band is checked against the measured outcome in the report.

## The governing question and my prior

**Is OI-215 alone?** OI-215's mechanism is the candidate-admission MEMBER-OVERLAP gate (gate 2,
`jointdecoder.cpp` `candidateStates`: `present < min(2, |members|)`) applied to windows with **< 2
distinct onset pcs**. The dispatch asks whether other admission-rule-class / coverage-class failures
have siblings. My `scanCoverage` decomposes every uncoverable event into four mutually-exclusive
classes: `memberOverlapPure` (every covering window < 2 onset pcs — the OI-215 theorem case),
`memberOverlapRich` (some covering window ≥ 2 onset pcs but gate 2 still rejected all classes — the
SAME gate, broader trigger), `fitBlocked` (a rich window passed gates 1&2 but failed gate 3 / the NCT
budget — a DIFFERENT gate → sibling), `rootOnly` (rich windows never got a class past gate 1 → sibling).

## Prediction 1 — admission-rule-class failures beyond OI-215

- **P1a.** On the fit corpus (A): **ZERO** uncoverable events of ANY class (0/326 pieces incomplete).
  Chorales onset ≥ 2 distinct pcs in essentially every window (OI-215 detail states 0 on all 326).
  Band: `totalUncoverableEvents == 0`, `piecesComplete == 326`. A single uncoverable event on (A) would
  be a surprise (a STOP).
- **P1b.** On the large-score set (B): **`memberOverlapPure` dominates** — I predict ≥ 90 % of all
  uncoverable events are `memberOverlapPure`.
- **P1c.** `memberOverlapRich` **nonzero but small** — band 0–10 % of uncoverable events. (A ≥2-pc
  window whose pcs form no partial chord — e.g. a bare tritone or two pcs that co-occur in no vocab
  class — still fails gate 2. Same gate as OI-215, broader trigger; I would report it as a REFINEMENT
  of OI-215's "< 2 onset pcs" framing, not a distinct sibling.)
- **P1d.** `fitBlocked` (gate-3 / NCT-budget sibling): **I predict 0, but with genuine uncertainty.**
  Band: 0 to a handful (< 1 % of uncoverable). The NCT budget `max(1, j−i)` is tight only for a
  1-event window (budget 1); an isolated dense boundary event coverable by NO longer window could in
  principle fit-fail everywhere. If `fitBlocked > 0`, OI-215 is NOT alone (a genuine second gate).
- **P1e.** `rootOnly` (gate-1 / root-present sibling): **I predict 0.** With 7 candidate keys × the
  full class vocabulary, a ≥2-pc window almost certainly has some class with its root among the onset
  pcs. Band: 0 to a handful. `rootOnly > 0` ⟹ a genuine second gate.
- **Net verdict I expect to reach:** OI-215's member-overlap GATE is effectively the sole admission-
  class failure mechanism (pure + rich are the same gate); `fitBlocked`/`rootOnly` ≈ 0 → **OI-215 is
  alone at the gate level**, with the "< 2 onset pcs" framing possibly needing the `rich` refinement.
  I flag P1c/P1d/P1e as the bands most likely to surprise.

## Prediction 2 — dead branches on the FIT corpus (A)

I predict these fire ZERO (dead) on (A): **`dpEmpty`** (theorem: all complete). I predict all of the
following are LIVE (nonzero): `rejRootPresent`, `rejMemberOverlap`, `rejFit`, `dpComplete`, `trInitial`,
`trSameKey`, `trKeyChange`, `stInsert`, `stImprove`. Genuinely UNSURE (predict either, flagged):
`rejMemInvalid` (predict LIVE-small, could be 0), `trContentNegInf` (predict small/possibly DEAD —
`candidateStates` already prunes most invalid classes), `trNoBack` (predict rare/possibly DEAD — a
candidate with no admissible predecessor is unusual past the first boundary).

## Prediction 3 — dead branches on the LARGE-score decoded subset (B)

The decodable subset at cap 2000 is expected to be ~4 scores (brandenburg4_mvt3 + dvorak_cello_mvt2
COMPLETE; butterworth + holst_mercury EMPTY — from the analysis-cost profile). Prediction:
- **`dpEmpty` LIVE on (B)** (butterworth + holst_mercury) — ★ **the headline dead-branch DIFFERENCE:
  `dpEmpty` is DEAD on (A), LIVE on (B).** This is the structural shape of OI-215 the dispatch hunts.
- `dpComplete` LIVE (brandenburg4, dvorak_cello_mvt2).
- All admission + transition branches LIVE, as on (A).
- I predict NO branch that is LIVE on (A) but DEAD on (B) among the decoded subset (the large scores
  exercise a superset of textures) — though the decoded subset is small, so a rare (A)-branch could
  read 0 on (B) by sample size; I will flag any such as sample-limited, not structural.

## Prediction 4 — onset-diversity distribution

- (A) fit corpus: onset-diversity histogram concentrated at **2–6** distinct onset pcs; the `0–1`
  buckets **near zero** (that is exactly why (A) never hits OI-215).
- (B) large scores: a **nonzero `0–1` tail** — the sparse/sustained/unison windows that cause the
  member-overlap gate to empty the analysis. I predict the empty-decode scores (uncoverable > 0) are
  precisely those with a non-trivial `0–1` onset-diversity population at the right positions.

## What would falsify "OI-215 is alone"

`uncovFitBlocked > 0` or `uncovRootOnly > 0` at material scale on (B) ⟹ a genuine second admission
gate participates ⟹ OI-215 is NOT alone, and the OI-215 fix design must cover that gate too. That is
the specific finding this measurement exists to surface (#3: a surprise is a STOP).

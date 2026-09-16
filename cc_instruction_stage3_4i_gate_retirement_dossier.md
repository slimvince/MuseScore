# CC Instruction: Stage 3.4-i — gate-retirement dry-run dossier (+ two byte-identical ships)

## Context

Roadmap 3.4/3.4b, design §7 — but with a correction to §7's optimism that the dry-run
must confront: **"decoder-subsumed after 3.3" is unproven for E/F/I/K/L.** At beam 1
the pipeline is numerically the OLD pipeline (3.3 moved the bonuses, changed nothing);
the gates were added historically because those same bonuses did NOT suffice. So
removing a gate at beam 1 will, in general, change outputs wherever it fired — the §7
verdicts are hypotheses to MEASURE, not facts to execute. This run measures them.

Two-phase shape (the 2.2 pattern): **this run = per-gate differential dossier + the
two provably-byte-identical ships.** Everything behavior-changing goes to a decision
menu for 3.4-ii / 3.2 planning. Base: `548adb7b2e`.

Working method A–H applies. **"Held for ratification" means HELD — no commit before
the ratification file arrives (the 3.3 slip is on the record; do not repeat).** The
two ships below are pre-authorized EXCEPTIONS with explicit proof gates.

Mandatory reads: design §7 (verdict table + the F2/F5/F4 obligations), §13 Q3/Q4;
scoring_model §6; `postscoringgates_tests.cpp` (the per-gate pins = the differential
instruments); the 1b report §1.4 gate inventory; handoff 3.4 cleanup item (2-arg
Gate R overload).

---

## Task 1 — Pre-authorized ship #1: remove dead Gates B/C/D (3.4b)

Provably unreachable (1b-F1, Cowork-verified: condition supersets of Gate A behind
`!didEnharmonicFlip`). Removal MUST be byte-identical:
1. Delete the three blocks; update the §6 table (rows removed, history note) and the
   §8 "Gate A subsumes B/C/D" constraint (now historical).
2. Proof gate: build + all suites + snapshots zero-diff + ONE corpus regen×3 with
   identity-set check (cheap insurance; expect exact). Any diff = the unreachability
   proof was wrong = STOP (that would be a major finding).
3. Commit directly on green: `refactor: remove dead Gates B/C/D (Stage 3.4b — provably
   unreachable since 1b-F1)`.

## Task 2 — Pre-authorized ship #2: absorb Gate R into the rcb edge (+ overload cleanup)

Per design §7 ("Gate R is absorbed, not retired") — a byte-identical refactor:
1. The rcb computation in Pass A becomes one function (the design's
   `rcbEdge(src, dest)` shape) with the reconstructed-credit guard INSIDE it; the
   separate call-site `if (gateR... && applyProgressionSignals)` folds in (phase
   condition preserved exactly).
2. Delete the 2-arg test-compat `gateRZeroesRootContinuity` overload; update
   `gater_tests.cpp` to the production entry (deliberate re-pin of CALL SHAPE only —
   outcomes identical, each marked; the Δ=+7b pins untouched).
3. Proof gate: suites + snapshots + corpus×3 identity sets, all exact.
4. Commit directly on green: `refactor: absorb Gate R into the rcb edge; drop the
   test-compat overload (Stage 3.4)`.

## Task 3 — The per-gate differential dry-run (NO commits; the dossier's core)

For each remaining gate/pass — bias correction, A (+FM2), E, F, G-E, G-B/C/D, H,
I, K, L, J, Iter 86, Iter 91 — produce one differential row by disabling JUST that
gate (temporary compile-time switch or local edit; never committed):

1. **Pins**: which of its Stage-1b pinned tests fail without it (the list of what it
   still uniquely does).
2. **Corpus ×3**: BIR counts + identity-set deltas + total changed-region count, with
   per-case root old/new for every identity-set change.
3. **Snapshots**: which drift.
4. **Classification** (the dossier verdict per gate):
   - **(C1) dead-in-practice** — zero effect anywhere → candidate for immediate
     removal (list for ratification; do NOT ship in this run);
   - **(C2) beam-replaceable hypothesis** — its fixes look like path-decision
     corrections a wider beam could make (state the mechanism: what evidence would the
     decode use?) → 3.2 acceptance case;
   - **(C3) emission-fold candidate** — its correction is really a mis-scoring fix
     (state which emission term/threshold) → Stage-5-adjacent design work;
   - **(C4) functional-layer** — needs key/cadence context (per §7: A, G-family
     likely) → Stage 6;
   - **(C5) structural keeper** — J-class; stays until its layer exists.
5. **The Q3 consequence per gate**: if it mutates root/quality/bass and is NOT
   retired/folded before 3.2 widens the beam, what constraint does that impose?
   (This list becomes 3.2's design input — which gates cap the beam.)

Protocol notes: one gate at a time (no combinatorial disabling); the disable switch
must provably not alter the enabled path (show the diff); Jazz + Default included
because preset-gated gates (`preferMinorOverMajorAdd6`) differ per config.

## Task 4 — The F4/F6/F8 re-decide inventory (paper only)

For the 1b findings owned by gates likely to move (mixed live/captured reads in
H/I/K/L; unsorted results[] after swaps; G-E duplicate push): per finding, what the
CORRECT behavior would be, what changes if fixed, and which retirement event should
carry the fix. No code.

## Deliverable — `cc_stage3_4i_dossier.md`

§1 ship #1 evidence + hash; §2 ship #2 evidence + hash; §3 the per-gate differential
table (the centerpiece — one row per gate, pins/corpus/snapshots/classification/Q3
consequence); §4 the F4/F6/F8 inventory; §5 the decision menu for 3.4-ii: what to
retire now (C1s), what becomes 3.2 acceptance cases (C2s) with their measured
expected deltas, what defers (C3/C4/C5); §6 unknowns.

Stop conditions: Task 1 or 2 showing ANY diff (their byte-identity claims are
load-bearing — a diff is a finding, not a tolerance); a disable-switch that can't be
made provably inert when enabled; anything in Task 3 that tempts a "quick fix" — the
dry-run changes NOTHING.

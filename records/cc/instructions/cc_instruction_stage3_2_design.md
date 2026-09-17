# CC Instruction: Stage 3.2 design — beam widening (design-only, ratification-gated)

## Context

Stage 3.2 is the FIRST intentional behavior change of the entire plan. Everything since
the reviews has been byte-identical; 3.2 deliberately changes outputs — so it gets the
decoder-design treatment: **a ratified design document first (`docs/beam_widening_design.md`),
no production code, probes allowed (uncommitted) to answer design questions.** Base:
`a652dc1ba7`. Method A–H; held means held; ratification arrives as an addendum file.

This is where the part-1 thesis gets tested: a wider beam should dissolve Δ=+7a
(bwv102.7, bwv261) — the cases that defeated Phase D's three dead ends and every gate —
because a global decode never irrevocably commits the transient wrong root that feeds
the rcb cascade.

Mandatory reads: `docs/decoder_design.md` (esp. §3 AWKWARD-3 cold-lookahead, §9
quality↔beam, §11 acceptance roster, §13 Q2/Q3/Q6 decisions); the 3.4-i dossier
(C2 roster + per-gate Q3 beam-cap consequences) + 3.4-ii report (K mis-fire caution,
Iter-86 DCML-correct, E/F C2′); `redesign_plan.md` Δ=+7a (Phase D 3 dead ends, the
"inter-region revision is architectural, not a gate" conclusion); the Δ=+7a/Δ=+7b
distinction in COWORK_HANDOFF (the must-not-break trio).

## The design document must cover (section per item)

1. **Scope + the behavior-change contract.** What beam>1 changes and what it must NOT.
   Level-0 (beam-1) stays byte-identical and default; beam>1 is opt-in behind the
   quality knob (§9). State the new gate: BIR/snapshot changes are now ALLOWED but only
   on cases ratified in advance; every change is DCML-adjudicated; no change ships
   unmeasured.

2. **What "widen the beam" concretely means here.** Per Q6 (K=8 start): the per-region
   candidate set (top-K cells instead of top-3+diff-root); the lattice edges that
   become live. Critically — per Q2 (DECIDED: promote forward signals to true
   decoded-successor edges at Level 1): w_seq/w_dim/w_stepOut/lookahead stop reading the
   cold lookahead and read the decoded successor. Spell out the decode algorithm
   (Viterbi/beam forward + backtrack), the score = Σ emissions + Σ transitions over the
   path, and how the committed-predecessor backward edges (rcb etc.) now compose with
   forward edges in a true two-sided lattice.

3. **The Δ=+7a mechanism — how the decode actually fixes it, derived not asserted.**
   Walk bwv102.7 / bwv261 through the lattice: the transient wrong-root micro-region,
   the rcb edge it would feed, and WHY a path through the correct root outscores the
   path that commits the transient (the future root's emission + the avoided
   wrong-rcb). Quantify from the dossier/redesign_plan numbers (AbMaj7 2.55 vs Eb/Ab
   2.33 etc.). If the derivation shows the beam does NOT fix it at K=8, say so — that's
   a finding, not a failure to paper over.

4. **The must-not-break set, as hard lattice constraints.** Δ=+7b trio
   (bwv245.28/296/320 — Gate R + Gate I coupled), the Baroque-13 / Jazz-7 / Default-14
   identity sets, the 11 snapshots. For each: what about the wider decode could break it
   and the guard. Gate I's double obligation (5 Jazz fixes + Δ=+7b first-inversion) is
   the headline risk per 3.4-i — design how the decode reproduces BOTH or I stays.

5. **Gate-retirement sequencing (Q3, the load-bearing ordering).** Every remaining gate
   mutates identity, so each must retire/fold BEFORE the beam widens past it (a wider
   beam feeding pre-gate identities into backward edges is incoherent). Give the
   concrete order: which gates fold into emission/edges first, which become decode
   tie-breaks (I/K/L margins), which stay as post-decode re-rank at beam>1 and why.
   K's caution (reproduce the Baroque target, NOT the chromatic-romantic mis-fire —
   3.4-ii) is a design constraint here.

6. **The acceptance roster with measured expected deltas + DCML adjudication plan.**
   From 3.4-i/ii: Δ=+7a (target: fix; expected Baroque 13→≤13 — measure), Δ=+7b
   (hold), I/bias/K/Iter-86/L (the C2 reproductions). Per case: expected direction,
   how it's DCML-verified, and the ratification evidence the implementation run will
   produce. Distinguish "expected win" from "must-hold" from "measure-and-decide."

7. **Beam width K as a parameter + cost.** Per Q6 K=8 start; the decode cost vs the
   3.1b cache (decode-once still applies — a wider decode cached once); the perf budget
   at Level 1 (NOT interactive-bounded per §9, but state it). Memory per the design §2
   envelope (non-constraint).

8. **Config scope.** Beam>1 applies to which configs? The user-facing Default is the
   one that matters; Baroque is the calibration gate; Jazz the non-Baroque hard-stop.
   Per 3.4-i, the BIR-relevant action is Jazz-Gate-I — design which config the
   beam-widening is validated against and which thresholds (if any) become beam-width
   or quality-level dependent (CLAUDE.md preset policy still binds).

9. **Migration sequencing → roadmap; risks; rollback.** Map design sections to the
   implementation sub-steps (likely: gate folding first per §5, then beam-in widening,
   then forward-edge promotion); riskiest assumptions; what's behind the quality knob
   vs in-place; per-step rollback. The quality knob means Level-0 byte-identity is
   always the fallback.

10. **§Open Questions for Cowork/user** — genuine forks (e.g. if the Δ=+7a derivation
    needs K>8; if Gate I can't cleanly fold; if forward-edge promotion destabilizes a
    snapshot). Recommendations welcome; decisions are ours.

## Report — `cc_stage3_2_design_report.md`

§1 probes run + what they settled (esp. the Δ=+7a lattice walk — run a real probe if
the derivation needs the actual cell scores); §2 section map + the three most
load-bearing claims with evidence; §3 the Open-Questions list inline; §4 unknowns.
Design doc uncommitted until the ratification addendum.

Stop conditions: the Δ=+7a derivation showing the beam does NOT fix it (report — it
reshapes the whole acceptance roster); any design choice that would break a must-hold
without a guard; Gate I proving un-foldable without losing either obligation (a design
fork for ratification); scope creep into key-path (Stage 4) or functional-layer
(Stage 6) beyond stated interfaces.

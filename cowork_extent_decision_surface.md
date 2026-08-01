# The analysis-extent and re-read-frequency decision surface (OI-210) — DRAFT for the user's ruling

> **STATUS: DRAFT (Cowork, 2026-08-02). Prepared, not decidable yet.** Two gates stand between
> this draft and a ratification: (1) every cost and stability figure below comes from measurement
> tools the OI-199 measurement-tools partition has not yet audited — each figure carries its
> establishment label, and principle #19 forbids resting a ruling on an unestablished figure;
> (2) the candidate-admission family (OI-215/226/227/228) must be fixed before ANY extent choice
> produces an answer on orchestral music — on 13 of the 23 committed large scores every extent,
> bounded or not, currently returns an empty analysis if its span contains an uncoverable event.
> This document assembles the decision so the ruling is one sitting when its inputs are trusted.
> Terms are used as defined in `DECISIONS.md`'s terms table; register entries are cited D-nnn.

## §1 The question, narrowed by the record

The question as historically framed: what temporal extent does the analyzer read per query, and
how often does it re-read? The OI-207 adjudication's dated note on OI-210 narrows it: the EXTENT
axis was last ruled by the user on 2026-07-02 — the bounded-context contract (D-030: "cost scales
with the working span, not the whole score"; the span is extensible on request; D-031:
"Whole-score analysis is the degenerate case (selection = score)") — and that ruling POSTDATES
the Stage-3.1b shelving of whole-score. The whole-score producer now in production (D-011/D-020)
entered by dispatch specification with no ratifier. So this surface does not re-open
"bounded or whole": **bounded is the standing ruling.** What it puts before the user:

1. WHICH bounded form serves the interactive path;
2. the RE-READ FREQUENCY (per query / once per edit / once-then-patched) and what, if anything,
   is cached;
3. whole-piece's remaining place (the effort dial's top rung; the batch/corpus degenerate case);
4. the sequencing prerequisite (the admission-family fix).

The user's registered prediction (2026-07-28, verbatim): "always read the entire score will VERY
likely not survive (maybe only under some effort setting = EXTREME)." The measurements below
support it more strongly than predicted — whole-piece is not merely slow out of envelope, it
returns nothing on most orchestral scores.

## §2 The evidence, with establishment labels

**Sources and their status.** The window study (`tools/joint_estimator/window_study.json`) is the
strongest-established input: its whole-piece decode reproduces the committed parity reference on
all 109 sampled pieces (a mismatch refuses to publish), and its memo layer is established
memo-on = memo-off. The cost profile, editing-cycle table and large-score counts
(`tools/notation_seams/*.json`) are generated artifacts with declared generators, NOT yet audited
(the OI-199 partition-2 subject). The 3.1b A/B and the Tristan review are committed evidence
documents. Every figure below is labeled [W] window study, [C] cost profile family, [3.1b], or
[T] Tristan review.

**Stability and accuracy of bounding (chorale envelope).** [W] A query's committed reading equals
the whole-piece reading for 98.2 % of queries at a 4-measure window, 99.9 % at 8, 100 % at 16;
every one of 1,485 queries stabilizes at a bounded span (needs-whole-piece fraction 0.0; 1,458 of
1,485 stabilize by 4 measures). Ground-truth accuracy at the query points is UNCHANGED by
bounding (chord-root agreement identical at every span; the tonality column moves by −0.0007 at
span 8 and 0 at 16 — within nothing). **Envelope caveat:** homogeneous Bach chorales; the 3.1b
sensitive class (long-modulation, Mozart-like) is not represented, and [3.1b] measured exactly
that class as the one where granularity choices matter (root readings differing on 32–40 % of
ticks on contrapuntal/large pieces; the window path favored 59/41 overall, 65/35 on Mozart).

**Cost.** [C] The whole-piece produce is ~99 % decode; fact extraction alone grows ~events^1.80
(95 % range 1.65–2.09) — ~23 s floor extrapolated at a Tristan-act's ~60k events (flagged
extrapolation); measured whole-piece produce 5.3–107 s across the profiled scores. [W] The
bounded decode's cost shape rises ~0.94 s (4 measures) → 2.05 s (8) → plateau ~3.4 s at the
whole-piece clip — Python reference shape, NOT the C++ interactive latency (which exists measured
only for whole-piece, `noteseam_latency.json`). [C] The content-vs-dynamic-program split is
40.5/59.5, meaning naive result reuse cannot save the majority share — but OI-218 stands: whether
an edit admits a bounded local re-solve is UNMEASURED, not refuted.

**The failure mode that trumps cost.** [C] 13 of 23 large scores contain events no candidate
admission covers (OI-215/227): whole-piece decode returns 0 segments there, and any bounded span
containing such an event returns empty for that span too. The admission-family fix is therefore a
prerequisite for EVERY candidate below, not a rival concern.

**Structural boundaries.** [C] 24 of 27 scores have a boundary-free stretch longer than 30
measures (Fauré: 467 measures, 2,947 events, zero structural boundary) — [T] F-11 predicted
exactly this (punctuation-poor textures starve boundary-gated machinery).

**The editing loop.** [C] The change token is the undo index; a pitch edit advances it (so any
cache keyed on it re-pays per keystroke), navigation does not (a cache serves it); the annotate
command is one produce per selected note.

## §3 The extent candidates, rated

**(a) Fixed bounded window (≈8–16 measures).** For: measured sufficient on the envelope — 99.9 %
reading-stability at 8 measures at zero accuracy cost [W]; trivially bounded cost; simplest to
build (#17's smallest step). Against: the constant is a hand-set span with no derivation — the
rationale rule and DT-2 both bite (why 8?); out of envelope (the 3.1b sensitive class, Tristan)
a fixed margin is exactly where [3.1b] measured wrong readings; it ignores the ratified
extensible-span design (D-030 R3) that already prescribes something better.

**(b) Grow-until-stable (the ratified shape: start small, extend until the reading stops
changing, hard-bounded).** For: this is the recorded design (D-030 R3's extensible span; the
never-coded §2.15 extension cluster, OI-18) — the span is DERIVED per query from the evidence
rather than hand-set, which is the #1/#4-clean form; the stopping criterion now has a measured
seed (≈4–8 measures on the envelope [W]); its win is bounding, which is what R1 demands. Against:
unbuilt (the largest build of the candidates); "the reading stops changing" needs a ratified
definition (which fields, how compared — a premise-ledger item); the worst case must carry the
contract's stop-condition-plus-hard-bound or it degenerates to whole-piece on precisely the
music that can least afford it; its per-query cost is a few bounded decodes rather than one.

**(c) Enclosing musical unit (to the nearest structural boundary).** For: musically principled on
music that HAS punctuation. Against: measured against — 24/27 scores contain >30-measure
boundary-free stretches [C], so the "unit" degenerates to hundreds of measures exactly where
bounding matters; [T] F-11. Effectively eliminated by measurement as the primary form.

**(d) Viewport plus margin.** For: hard-bounded and cheap (a screen is ~15–120 events [C]).
Against: the analysis of a note would depend on scroll and zoom state — the same query returning
different readings for reasons no musical fact explains, which offends determinism (#16, and the
verifiability contract D-029); rejected unless some future display-only consumer wants it as a
presentation prefetch.

**(e) Whole piece.** For: on the chorale envelope it is the measured-equal gold form [W], and on
the batch/corpus surface (whole pieces ARE the selection) it remains the degenerate case D-031
already blesses. Against: ruled out as the interactive default by D-030/D-031; empties on most
orchestral scores until the admission fix (OI-215); cost grows super-linearly before the decode
even starts [C]. Its remaining place: the effort dial's top rung (the user's EXTREME), and
batch grading.

## §4 The frequency axis, rated

**Per query, no cache (the current state).** Indefensible once numbers exist: every navigation
step re-pays a full produce for an identical answer [C]. Recorded as the incumbent only.

**Once per edit — the keyed (score, change-token) record cache.** For: collapses navigation and
warm re-queries to lookups; collapses the annotate command's N produces to 1 (OI-213); composable
with ANY extent choice. Against: the edit loop re-pays per keystroke by construction [C] — a
cache alone does not solve composing; adds the first cache-invalidation surface to the record arm
(a #11 test obligation the record arm currently lacks entirely — see the C-5 candidate finding).

**Once, then incrementally patched.** For: the only form that could make sustained editing cheap;
content scores are position-local and reusable (~40 % [C]). Against: the dynamic-program share
(~60 %) is coupled; whether a bounded local re-solve after an edit is sound and cheap is
UNMEASURED (OI-218) — this option needs its own measurement before it can be rated honestly.

**Orthogonal and compatible with all of the above:** moving the status-bar computation off the
interactive thread (the OI-206 fix surface's presentation-side half) — it removes the freeze, not
the cost, and no candidate above removes the need for it during a first cold decode.

## §5 The reading the current record supports (provisional, not a ruling)

Bounded grow-until-stable as the target extent (it is the already-ratified shape, with a measured
stopping seed), reached via the fixed ≈8-measure window only if an interim step is wanted; the
keyed record cache regardless of extent (navigation and command multipliers are pure waste);
off-thread presentation regardless of everything; whole-piece retained as the effort dial's top
rung and the batch degenerate case; the once-then-patched option deferred to its own measurement
(OI-218). All of it conditional on: the admission-family fix first (no extent answers on
orchestral music before it), the measurement-tools audit before the figures are treated as
established, and the "stable" criterion written as a premise ledger before the build (#17).
Implementation seam, whichever form wins: the span input at the producer/adapter that OI-212
already names (input-scoping, not an inference change).

## §6 What is asked of the user, when the gates clear

One sitting, four checkboxes: the bounded form (a interim? b target?), the cache (yes/no), the
effort-dial placement of whole-piece, and the once-then-patched follow-up measurement (order it
or drop it). Nothing here requires re-opening D-030/D-031; everything here retires D-011/D-020's
unratified whole-score-per-query shape at the interactive seams.

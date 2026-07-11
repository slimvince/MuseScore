# Adjudication Dossier — Plain-Language Explanations + Principle-Derived Verdicts

> **Cowork, 2026-07-10 (session 36), user-directed:** *"Explain the issues so they can be
> understood, describe and value the alternatives in the light of principles."* This dossier
> covers (A) the structural audit's seven "UNCLEAR — user adjudication" rows and (B) all 17
> siloed-fact findings. **Method: apply the standing principles first; only where they do NOT
> decide is there a genuine user choice.** Result: the principles decide essentially
> everything; what remains for the user is ratifying the derivations (#14), not choosing among
> arbitrary options. **RATIFIED by the user 2026-07-10:** six of seven were pure rule
> applications; the one genuine acceptance was A3 (tolerating the quality-overwrite #12
> violation until E4, visible via OI-10). The Part-B fact-publication corollary was ratified
> the same day and now stands in CLAUDE.md beside the principles.

## Part A — the seven audit adjudications, in plain language

**A1. S2/S3/S4 — four separate places read the raw score and each re-decides which notes
count.** The architecture says only Layer 1 (the fact layer) may interpret the raw score
(which notes are real, audible, on the beat — e.g. skip ornamental grace notes, handle notes
inside tuplets). The audit found three helper functions that bypass Layer 1 and walk the raw
score themselves, each with its own private version of "which notes count" — one of them
skips grace notes, another snaps mid-tuplet time positions. That is the same decision
implemented four times (#6 violation) in the wrong layer (#7 violation). All four are already
scheduled to be deleted when the old segmenter retires at E4. *(The word "catalogue" in the
original row meant only: write these private rules down as an explicit list.)*
**The only real question:** when we delete them, do their private rules (grace-skip,
tuplet-snap) exist in Layer 1's single reading, or do they silently disappear?
**⚖ Verdict (#12 — no information loss):** before the E4 deletion, list each embedded rule
and check it against Layer 1; keep-or-reject each one consciously in the retirement commit.
No choice to make — #12 mandates the check; the deletion itself is already planned.

**A2. S8 — tuning numbers retyped instead of shared ("value copied").** The new key decoder
needed the same tuning numbers the old key resolver used (how expensive a key change is,
etc.). Instead of both components reading ONE named constant, the numbers were **retyped as a
second set of constants with the same values**. Why that is bad: it is one decision stored
twice (#6). The two copies agree today only by coincidence of history; the moment Stage 5
re-fits one copy, the other silently keeps the stale value — and nothing will flag it
(exactly the Class-B pattern #19 forbids: agreement that is unfalsified, not established).
**⚖ Verdict (#6):** single-source the constants. Timing: at E4 — the old resolver shrinks
there anyway (retirement map R5), and Stage-5 fitting (the moment the drift becomes
dangerous) comes after E4. Also EG-5 already requires these constants join the fit manifest.
**A2b. S9 — computed-then-discarded key ranking.** A full ranked key analysis runs, but only
its single top item is used, as a seed to keep the segmentation grid byte-stable. Kept
deliberately (adjudicated "load-bearing" at Stage 1). **⚖ Verdict:** dies with the segmenter
retirement at E4; until then it is a documented, deliberate inefficiency, not a correctness
risk. Nothing to decide.

**A3. S14/S16 — later passes OVERWRITE the chord quality Layer 4 committed.** After the
chord scorer decides "this is a minor chord", two later passes may change that quality based
on the resolved key — and they **keep no record of what they overwrote**. You are right that
this is exactly what #12 forbids: an overwrite that drops the original is information loss,
and it is also quality-from-key logic living in three different homes (#6/#7 — that is FQ-2's
whole point). So the END state is not in question: **one owner for quality-from-key, and any
revision must carry the original reading as a ranked alternative, never a silent overwrite.**
**The only real question is timing.** Alternatives: (i) rip the overwrites out now — that is
a production behavior change with no replacement owner yet (FQ-2's owner is decided at the E4
design), so it would be a cross-layer patch of exactly the kind #7 forbids; (ii) tolerate
until E4, where the §6-block dissolution + FQ-2 give the concern its single home, as one
ratified, revertible change (#14) under the robust stop (#11).
**⚖ Verdict (#7/#8/#14):** (ii). The violation stays VISIBLE in the register (OI-10, gating
the dissolution) — tolerated is not forgotten.

**A4. S18 — a folder whose NAME mixes layers.** The `function/` directory contains both
Layer-4 winner-selection code and Layer-5 units. There is **no code entanglement** — purely a
misleading folder name. Alternatives: rename now (a large, behavior-free diff) or rename at
E4 where the same files are already being renamed for retirement reasons (R7).
**⚖ Verdict (#8 + the arc plan's placement rule — do not touch what a scheduled step already
touches):** rename at E4. Nothing gained by doing it twice.

**A5. S19 — two confidence numbers on different scales compared as if equal.** One number is
bounded 0–1, the other is an unbounded sum (observed up to ~25); the override bar compares
them directly — like comparing meters with feet. This is the already-registered T1-3, and it
is now HARD-GATED (EG-4): before anyone fits the conversion constants, the premise "a fitted
constant CAN make these scales commensurable" must itself pass a #17 ledger + desk sim —
because the one calibration attempted so far failed (non-monotone).
**⚖ Verdict:** the audit's question ("accept deferral?") is superseded by EG-4, which is
stricter than either alternative the audit offered. Close the audit row pointing at EG-4.

**A6. S20 — the metric's core comparison written out four times.** The check "does our root
equal the ground-truth root" is a bare `==` in four measurement scripts. The derivation
behind it is single-owned; only the one-line comparison repeats. Risk: if the comparison ever
needs nuance, someone updates three of four sites and the headline number silently forks.
Cost of the fix: minutes.
**⚖ Verdict (#6 + #19 instrument hygiene):** add the one shared helper at the next instrument
touch; close the row then. Not worth its own commit; not acceptable to leave forever.

**A7. FQ-3 placement.** Already decided by the Stage-1 code inspection: fold into E4. The
only residue is that the audit's own summary table still shows the old answer — a doc-sync
annotation (OI-46). **Nothing to adjudicate.**

## Part B — the 17 siloed facts: complete disposition (are ALL taken care of? — YES, as follows)

The deep answer first: **items 1, 2, 3, 10 and 17 are not five problems — they are ONE
problem**: the shared surfaces between layers drop voice, spelling, and chord-membership
facts, so every consumer above Layer 4 either cannot get them or re-derives them privately.
The principles already prescribe the cure — **each derived fact is published exactly once, on
the producing layer's output surface; consumers read, never re-derive** (this is just
#6 one-path + #7 layer-ownership + #12 no-loss applied to facts; proposed below as an
explicit corollary). That publication design is a mandatory input to the E4 design step — it
is ONE design decision, not seventeen patches.

| # | finding (plain) | principle violated | disposition | row |
|---|---|---|---|---|
| 1 | Per-note voice-leading analysis (is this note a suspension? approached by step? by leap?) computed, used once, thrown away | #12 (derived facts lost), #7 (L5/pedal cannot reach them) | E4 fact-publication design | OI-72 |
| 2 | The chord-tone-vs-ornament verdict per pitch dies at the L4→L5 boundary (the L5 input struct never copies it) | #12 | E4 fact-publication design | OI-73 |
| 3 | Spelling per pitch never lifted above L4; one narrow consumer | #12/#6 | E4 design (options a/b/c recorded at PC-1) | OI-15 |
| 4+5 | The key-alternatives menu and the key confidence are computed and carried but NOTHING in production reads them | #12 (computed, unconsumed) — deliberate pre-wiring, so a dormancy fact, not a bug | consumed at L5 engage; visible until then | OI-75 |
| 6 | The key ranking's runner-up (how close the second-best key was) is folded into a confidence number and discarded; the serialized form exists only in the batch tool | #12 | NEW row — E4 fact-publication design (the L5 key-consistency channel wants it) | **OI-81 (added)** |
| 7 | Cadences are re-detected from scratch by every consumer and never stored; the production detector is also circular (uses the answer to find the evidence) | #6 (recomputation), #12 (not published) | E4: publish once on the region; the circular detector retires (R2/R3) | OI-76 |
| 8 | `bothLicensed` telemetry read only by a measurement flag | none — telemetry for the Stage-5 fitter, correctly behavior-neutral | DECLARED OK-BY-DESIGN (kept visible so it is never mistaken for dead code) | **OI-83 (added)** |
| 9 | The fan-out SUMMARY is diagnostic-by-design (fine), but the actual above-threshold READINGS behind it are truncated by the cap-of-3 and lost | #12 — the load-bearing loss | already the distinct-root-carry item; link made explicit | OI-9 (annotated via OI-83) |
| 10 | Region-level metric position IS published (fine); the per-note beat weight is decoder-private | #12 | folded into the same E4 fact-publication design as #1 | **OI-82 (added)** |
| 11 | "Is the bass a chord tone / is this an inversion" re-derived at ~60 call sites from raw fields | #6 (one decision, many private derivations) | E4: one published verdict/primitive | OI-77 |
| 12 | The mode the composer DECLARED in the score is read only by the key path; the chord layer's diatonic reasoning never sees it | #12 (an input fact siloed) | E4 design input | OI-78 |
| 13 | Pedal-point detection overwrites the annotation root and discards the full-voice reading | #12 (the overwrite class — same as A3) | already designed away (reader-over-carry, annotate-not-overwrite); build gated EG-3 | OI-4 |
| 14 | Chord-symbol/Roman-numeral annotations ON the score are declared as input flags but never read | not a violation — unbuilt capability | long-horizon | OI-80 |
| 15 | The "best different-root" margin computed independently in 4 places | #6 | retires with the decoder (FQ-1 at E4) | OI-11 |
| 16 | The pedal confidence curve's constants retyped inline instead of read from preferences; the emission sigmoid written in two files | #6 (constants duplicated — the same disease as A2/S8) | fold at next touch of those files | OI-79 |
| 17 | Voice identity exists at L1 and is DROPPED at the shared tone surface — the structural reason #1/#2 cannot be lifted today | #12 at the surface-design level | THE core E4 surface decision | OI-74 |

**Proposed corollary for ratification (the standing form of Part B):** *"Every derived
analytical fact is published exactly once, on the producing layer's output surface; consumers
read, never re-derive. A fact consumed by no one is either dormancy (declared, with its
future consumer named) or waste (removed)."* — derivable from #6/#7/#12, stated explicitly so
the next silo cannot form unnoticed.

*Cowork, session 36. Sources: `cowork_structural_integrity_audit.md` §2/§5,
`cowork_siloed_facts_audit.md`, `cowork_l1_l5_premise_debt_audit.md`, CLAUDE.md #1–#19.
Register rows updated in the same commit (OI-81/82/83 added; OI-42 pointed here).*

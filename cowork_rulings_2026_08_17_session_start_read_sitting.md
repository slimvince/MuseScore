# Rulings — the session-start-read sitting (2026-08-17): the route to a smaller ordinary session-start read

> **Sitting record (Cowork, 2026-08-17).** The user's rulings on the four options of the
> session-start-read decision surface, held after the eighth batch's return sitting and recorded
> beside its record (`cowork_rulings_2026_08_17_eighth_return.md`). **This record is the interim
> carrier (D-230); it lands in git at the next dispatch's Task 0.** Nothing is executed by anything
> here — no file is edited, no read regime changes until an executing dispatch performs it under
> the preconditions §1 states.

## 0. The sitting's ground

**Why the sitting was held at all.** The user's direction of 2026-08-16 — verbatim, *"we need to
prune (at least) claude.md and open_items.md because the mandatory reads at session start for you
and CC are too large (we are already hitting quality problems - and there are also other issues
like real monetary cost and response times)"* — is UNDISCHARGED for ordinary sessions. The split
landed and halved the five; the finer recognizer pass returned negative and Ruling 3 of
`cowork_rulings_2026_08_17_seventh_return.md` CLOSED that route naming the curated boot list as the
standing replacement; **F51 (recorded at §6 of the eighth-return record) establishes that the boot
list serves implementation-blind sessions only, so the named replacement does not reach ordinary
sessions and no ruled route existed.** This sitting supplies one.

**The measurement the surface rested on**, taken read-only at the git objects of the eighth batch's
terminus `f27c3ded70`, characters with line endings normalised: `OPEN_ITEMS.md` 340,400 (52%);
`CLAUDE.md` 151,045 (23%); `DECISIONS.md` 126,774 (19%); `BUILD_AND_TEST.md` 27,179 (4%);
`STATUS.md` 10,894 (2%); **total 656,292 characters**, paid by every session on both sides.

**One derived figure was DECLARED AN AUTHORED TRIAL and not a proposed mechanism**, on the shape
the 2026-08-16 §1 desk trial established: the writing side's own split of the index's rows counted
375 rows, 133 opening with the resolved mark and carrying 58,045 characters, ~17% of that file.
**The splitter is naive and disagrees with the project's ONE index parser on about six rows** where
a pipe character sits inside a code span. **That parser is the authority and this figure is an
order of magnitude the executing derivation must confirm**, never a population to act on.

**The structural precedent the surface turned on, read at `CLAUDE.md` in full this session:** the
CONDITIONAL READ is already a ruled pattern in that file, used twice — `docs/scoring_model.md` for
sessions touching scoring logic, and the joint estimator's specification section for sessions
touching its behaviour (Ruling 64, 2026-08-11), whose recorded excluded alternative is *"an
unconditional read, which spends capacity — this arc's measured scarcest resource — on every
session the condition excludes."*

**The presentation form held.** The full self-contained surface was delivered first as the turn's
final response; the user confirmed the reading (*"i have read it"*); the four questions were put in
their own later turn. **The user's ruling, verbatim: *"I agree with your recommendations"*** —
given against recommendations stated as A on all four questions.

## 1. Ruling 1 — the `OPEN_ITEMS.md` session-start read is replaced by the DERIVED GATING ANSWER, behind a #19 precondition

**A session no longer reads the whole index at session start. It reads the derived gating answer,
and opens the INDEX when it needs a row.** The ground is that the index is 52% of the mandatory
read and the session-start read serves ONE question — rule (b)'s *a stage may not open while a
register item gating it is open* — which a derivation already answers, and that gating is DERIVED
and never hand-added is the record's own standing rule (**D-436**).

**★ THE #19 PRECONDITION IS PART OF THE RULING AND NOT A FOLLOW-UP.** The artifact a session reads
instead **must be POSITIVELY ESTABLISHED before anything relies on it** — not merely unfalsified.
Until it is established, the current read stands unchanged. A session may not begin trusting the
substitute because the ruling exists.

**★ AND A PREMISE OF THE SURFACE IS CORRECTED HERE, BEFORE ANY ACT RESTED ON IT.** The surface
named `tools/audit/phase1_finish_line.json` and `tools/audit/nongating_apparatus_rows.json` as the
live derived gating artifacts. **That is half wrong, established at the committed guard artifact
after the ruling was given and before this record was written:**
`tools/audit/gen_phase1_finish_line.py` sits in the guard set's **HISTORICAL (frozen) class** under
§4 of the 2026-08-16 record — frozen in place as record, **never regenerated again** — so its
artifact is a historical record and NOT a live answer. **What IS live and passing:**
`gen_nongating_apparatus_rows.py --check` and `gen_gating_row_sizing.py --check`.

**The consequence for the executing dispatch, which is a widening of its work and not a change to
this ruling:** it may NOT assume a live derivation exists. **It DERIVES what the live gating answer
is** — at the live artifacts, under the six phases that superseded the three-phase structure, not
at the frozen phase-1 cut — establishes it under #19, and **STOPS to the user if no live derivation
answers rule (b)'s question**, rather than substituting a frozen record or authoring a new judgment.
The ruling above is what the user ruled; this paragraph is what discharging it now requires.

**What this ruling does NOT do.** It does not change rule (a)'s authority: the INDEX remains the
**authoritative status surface**, and the substitute is a route to one question it answers, never a
second home for status (#6). It flips no row, creates none, and discards none. It does not touch
[[OI-179]], which stays OPEN and GATES.

## 2. Ruling 2 — the archiving pass the ruled test already authorises is ORDERED

**The archivability test (§5(E) of the 2026-08-16 record) is applied to what has accumulated since
the split** — the resolved-opening rows still in `OPEN_ITEMS.md`, `DECISIONS.md` exhaustively, and
any span in the five that the test places — **riding whatever dispatch executes Ruling 1**, both
being archiving-shaped acts under the same safeguard.

**No new mechanism is ruled and none is needed:** the test is standing, the machinery is built and
proven byte-faithful, the read-before-move safeguard binds every span, and the doubt default keeps
a span the test cannot place at site. **The eighth batch is the safeguard's own evidence** — it
refused two ruled spans and cost nothing by refusing.

**The expectation is recorded honestly with the ruling, because it was stated in the surface and
accepted with it:** the last two passes both UNDER-delivered against their predictions (the split
returned −3.2% on `CLAUDE.md` against a predicted 23%; the finer pass returned a negative answer).
**A modest yield is the expectation, not a transformative one**, and a pass that returns little is
this ruling working rather than failing.

## 3. Ruling 3 — `BUILD_AND_TEST.md` becomes a CONDITIONAL read; `DECISIONS.md` explicitly does NOT

**`BUILD_AND_TEST.md` is demoted from an unconditional session-start read to a CONDITIONAL one:
mandatory for a session that builds, tests, or runs a tool whose command lives there.** This is the
input the user raised in conversation 2026-08-17 and the seventh-return record carried; **F51
establishes it was parked in the wrong sitting** (the boot list's, whose scope does not reach
ordinary sessions), and this is its correct home. The pattern is the twice-ruled conditional read,
applied for the first time to DEMOTE rather than to add; the file is 27,179 characters, 4% of the
mandatory read, which bounds the cost of the error in either direction.

**★ AND THE SAME TREATMENT IS RULED OUT FOR `DECISIONS.md`, which is the half that binds harder.**
Its rule (a) rests on a stated ground — *rulings bind mechanically only if every session reads
them* — and **a condition would replace a mechanical bind with a judgment each session makes about
its own work BEFORE reading the thing that would tell it whether the judgment is right.** That is
the never-work-from-memory rule's own failure shape and #19's silent-failure direction. 126,774
characters is not worth it. **A later ruling may revisit this; nothing here forecloses it, and the
ground above is what such a ruling would have to answer.**

## 4. Ruling 4 — the curated boot list STAYS at its ruled definition

**The curated boot list remains the implementation-free read list an implementation-blind session
boots from — for those sessions only** — exactly as
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` defines it and as preparation
output (d) commissions it. **It is NOT widened to ordinary sessions.** It remains a live, unblocked
preparation output, DRAFTED and RULED before any derivation session boots from it, and it is not
the route to a smaller ordinary session-start read — Rulings 1–3 are.

**Two grounds, both stated in the surface and accepted with the ruling.** Widening merges two
different purposes — **blindness** and **size** — into one artifact answering to two criteria,
which produce different lists by different tests, and that is the shape #6 exists against. And it
carries a mechanical consequence none of the other options has: **the callers sitting ruled that a
mandatory-read or boot listing HOLDS a retirement candidate**, so changing the boot list moves what
holds candidates and the archiving wave's inputs move with it.

## 5. What follows, and what this sitting did NOT do

**The executing dispatch's work from this sitting**, in the order the rulings bind: derive and
establish the live gating answer under #19 (Ruling 1, with the frozen-artifact correction as its
first task and a STOP if no live derivation answers rule (b)); the archiving pass (Ruling 2); the
`BUILD_AND_TEST.md` demotion written where a session meets it, and `DECISIONS.md` left untouched
with the ground recorded (Ruling 3). **Ruling 4 orders no act.**

**Riding the same dispatch's Task 0, from the eighth-return sitting and F51:** this record; the
eighth-return record with its §6 correction; the TWENTY-FIFTH handover block (uncommitted since it
was written during the eighth batch's flight) and a TWENTY-SIXTH; the dispatch itself; Ruling 1 of
the eighth-return record's standing constraint written where a future pass meets it; F49's
one-sentence correction at its generator; and **the F51 correction at its three remaining sites** —
`cowork_rulings_2026_08_17_seventh_return.md` §3 and the twenty-fourth and twenty-fifth handover
blocks — as recorded acts, the corrected wording preserved (#12).

**What this sitting did NOT do.** No file is edited and no read regime changes until an executing
dispatch performs it. No `CLAUDE.md` span moved — the two ruled at the eighth-return sitting stay
at site and that question is CLOSED. No open-items row created, flipped or discarded; [[OI-179]]
OPEN and GATES; [[OI-372]] the one standing red; [[OI-374]] untouched. No caller flag acted on, no
candidacy acted on, no fate moved. No mining, no fact-gate admission, no findings ledger. Nothing
under `src/`, `tools/corpus/` or `tools/robust_stop/`; no golden, no test, no measurement of the
analysis. F1–F51 ride to the preparation phase's retrospective with the E3 ordering defect and the
A1 premise error.

*Provenance: Cowork, 2026-08-17, the session-start-read sitting, the user present and ruling in
conversation; the user's words quoted verbatim in §0. The measurement in §0 was taken at the git
objects of `f27c3ded70` by explicit hash; `CLAUDE.md` was read IN FULL at the same commit before
the surface was drafted, its content hash matching the finer-archive artifact's recorded
`base_blob_sha256`. The frozen/live split in §1 was established at that commit's committed guard
artifact. This record is written in the remote Cowork environment, where the repository is reached
through the device bridge: no working-tree file was read through a shell.*

# Can the analysis afford to weigh every reading? — the eleventh family surface for the chord-and-key layer — 2026-10-05

> STATUS: DECISION SURFACE, NOT RULED. No question on it has been put. Written by the Cowork sitting that
> booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_ninety.md`. Tags: *checked* = read
> at the source this sitting; *relayed* = taken from a record and not re-read at its source; *my reading* =
> my inference. §A is the surface as delivered, corrected at its sites by the check; §B is the check, with
> every former wording kept (#12).

## §A. The surface

### 1. Where we are

You are ruling, family by family, on how the new specification of the analysis's central layer should
read. That layer looks at a passage and decides, all at once: which key each stretch is in; where one
harmony gives way to the next; which chord sounds over each stretch; and which notes are chord notes and
which are passing notes, suspensions and the like. One complete answer of that kind for the whole passage
is called a **reading** — the kind of analysis an analyst writes down.

This family asks one thing: **can the analysis afford to weigh every reading to the end before it
chooses?** The derivation calls this "possibly the point on which the whole charter's feasibility turns".
Ten families are ruled; this is the eleventh, the last of entry 279 §2 item 1's list.

### 2. The facts

**The rule, and why it exists.** The ratified framework forbids this layer to "discard a rival before the
whole sequence of spans has been scored", because "a wrong reading can be a local optimum" (*checked*,
`FRAMEWORK.md`, the L2 charter's "May not"). Musically: a passage can look like C major for two bars, and
the F♯ and the cadence in bar 4 then show it was in G all along; a search that threw the G reading away at
bar 1 can never get it back.

**L2-S36** (*checked*): "The search is exact, or it prunes only by a bound that provably cannot discard a
reading whose final candidate score could exceed a kept reading's. No beam that discards readings on
partial candidate scores is admitted. Where exactness is not affordable, the charter's rule, not the
search, is what must give way, and that is a ruling (OQ-L2-8 ★)." In plain words: every reading considered
is weighed to the end, or dropped early only on proof it could not have won; keeping only the best few
half-finished analyses (a "beam") is not allowed; if weighing everything is too slow, the user rules what
gives way. Status: "Settled as a rule. **Open** on whether it can be met."

**OQ-L2-8** (*checked*): "First a measurement: does exact (or bound-safe) inference over the joint state
fit on the scores the project must handle? Those include very large scores [RULED — D-201]. Then, if not,
a question for the user: narrow the admission rule (with L2-S2's ceiling cost), or relax the charter's
no-discarding rule, and by how much?" The two ways out: (a) let the analysis consider fewer kinds of
reading at all, any reading so excluded never findable, its cost counted against what analysts write; (b)
let the search drop half-finished readings early after all. **L2-S23**'s premise rests on the same question:
"The joint search can afford the assignment dimension (L2-S36)."

**How big the search now is.** The derivation (*checked*): far larger than a published model that afforded
exact search with 168 labels — "42 tonalities × a vocabulary of degrees, qualities, figures and applied
chains × the pair-term dependence of L2-S33" — and "Whether exact inference fits is a measurement this
session cannot make." Four rulings bear on it (*checked* at their records): the tonality family chose
spelled keys, 42 rather than 24, naming "the tractability question" as the cost; the chord-vocabulary
family kept every chord kind as its own state, "the state is larger"; the elaboration family admitted
eight relations, enlarging the search only if they are part of what is searched (left to L2-S33's
family); the cadential six-four family declined a third reading partly because "the state grows". No
count of the search's size appears anywhere I read.

**What the existing design says** (*relayed*, the old documents' words, not checked at the code). The
current engine searches exactly over 24 keys × a chord list counted from the chorales, a chord lasting at
most four events (D-004, D-098; the register wording *checked*). **What it does narrow — which chord
classes a stretch may even consider — "has no specified form anywhere in this architecture and no recorded
basis" (Row 1.12; D-098's entry, *checked*, says the same).** A reserve shortcut — **restricting key-change
candidates to a neighbourhood on the circle of fifths whose extent was to be fitted** — "was never adopted:
measured at the fitted weights its cost is worse than exact decode" (Rows 1.10, 1.11). Exact search was
"expected tractable" at "chorale-scale event counts (roughly 60–150 events)" (Row 10.52) — an expectation,
not a measurement at other sizes.

**What is already ruled about size and speed** (*checked*):
- **D-201:** "Very large scores MUST be handled, and are expected to be a MORE COMMON use than our corpora.
  A Wagner act or a symphony has to produce an analysis." Its record names the collision: the current
  engine's "ratified tractability envelope is chorale size (60-150 events)". It also records that "the
  decode returns nothing on 13 of 23 committed large scores" (OI-215/OI-227). **`CLAUDE.md` calls OI-215
  the "empty-decode cliff" and places it, with OI-227, in the struck-versus-sounding family; OI-215 and
  OI-227 were not opened by this sitting, so whether that fault bears on running time is not established
  here.**
- **D-200:** make it work first; trade precision for speed only once slowness has proved a problem, and
  first exhaust what makes the same computation faster.
- **C-8 / D-030:** the work scales with the music the user selects, not the whole piece; whole-score
  analysis is the case where the selection is the whole piece.
- **D-202** (deferred): one effort setting, which must be able to bound time; beside it the user's
  recorded prediction: "always read the entire score will VERY likely not survive (maybe only under some
  effort setting = EXTREME)".
- **D-035:** every cost-driving choice is a setting, never a hardcoded constant.
- **D-297 and `FRAMEWORK.md` §8.4:** "Never computing a possibility is not information loss; only
  discarding a computed one is."

**What the current phase allows** (*checked*, phase-definition surface §3.4): "NOT DONE: … no code change";
"NOT ALLOWED: implementation-derived material in the deriving sessions". A timing measurement of L2's
search needs a search that does not exist — code, which *on my reading* is a code change. Timing the
current engine answers a smaller question and brings implementation material in. So no measurement
needing code runs in this phase unless the user changes the phase rule. What can run is a **sizing on
paper**: from the ruled vocabulary, how many readings an exact search must weigh per change of chord, how
that grows with stretch length and selection length, and what known ways of making the same exact search
cheaper do to it. **Calling it the first stage of the ratified funnel — "desk-simulate (hours) → read-only
probe (a session) → build (an arc)", in the scope-of-surprise paragraph ratified with #17–#19 — is my
reading: #17(c) defines a desk simulation as a hand trace on corpus cases, which a sizing is not.** It
needs no code and reads no implementation.

### 3. What remains to decide — nothing yet; the record answers each step

- **Whether L2-S36's rule stands.** The ratified charter makes it. **The outgoing rows that differ from it
  are about the old engines' shortcuts and settings, or are reconciled at §4.1 below.**
- **Whether to investigate before choosing a way out.** Investigate by default, never ask (D-254); the
  derivation puts the measurement first. Choosing (a) or (b) now would be choosing blind.
- **Where the measurement runs.** The paper sizing now; a code probe only if the sizing cannot settle it,
  and then whether to allow one in this phase comes to the user on its own surface. *(This answer rests on
  my reading that such a probe is a code change under §3.4.)*
- **In what order any remedy is tried.** D-200 sets it: first what makes the same exact search cheaper —
  the old design's split of key changes into a separate block (Row 10.51(iii), already proposed for adoption
  by the comparison, not one of this family's parts) and a provably safe bound (L2-S36's own allowance);
  only then a ruled way out, (a) or (b), its cost measured and stated. **The selection-sized working span
  (C-8) is not one of these speed-ups: it is a ratified bound on what is searched at all, already in
  force, and the sizing takes it as given.**

So confirmations are put, not a choice.

### 4. The confirmations

**4.1 The rule stands, read with "never computing is not loss".** L2-S36 stands as derived; OQ-L2-8 stays
open as derived. D-297 and L2-S36 govern different acts: the admission rule decides which readings are
never generated (L2-S2's closure test with exclusions ruled by name governs that, and §8.4 says it is no
loss); L2-S36 forbids dropping a reading the search has begun to weigh. **Proposed addition to L2-S36:** "A
reading the admission rule never generates is not discarded (D-297; FRAMEWORK §8.4); what this statement
bars is dropping a reading the search has begun to score." An effort setting may not quietly reduce how
many readings the search keeps; if one ever does, that is the ruling OQ-L2-8 names.

**4.2 The route for OQ-L2-8.** The next act is the paper sizing, written by a fresh Cowork session and
landed as a document, every value it uses marked provisional (principle #17's rule for desk-simulation
values, *applied by analogy*) and its result carrying its uncertainty. If exact search is clearly
affordable at D-201's sizes within a working span, OQ-L2-8 is recorded "expected affordable; to be
confirmed by measurement at the build". If clearly not, the choice between (a) and (b) comes to the user,
with the sizes, before the L2 specification is ratified. If it cannot tell, whether to allow a code probe
in this phase comes to the user. Any remedy is tried in D-200's order.

**4.3 L2-S23: nothing left to place.** The elaboration-relations family placed or routed all 54 of its
parts: 31 AGREES (25 carried, 6 relocated to L1); 23 DIFFERS (12 historical, 5 quarantined, 6 travelling to
L2-S33's and L2-S31's families). Its premise travels with OQ-L2-8.

**4.4 The placements for L2-S36's 24 parts** (*checked* at each row in §6 of the comparison file):
- **ADOPTED — carried (L2-S36), as proposed (8):** Rows 1.8(i), 1.9, 7.79, 7.82, 7.86, 7.151, 10.51(i),
  48.2(i).
- **QUARANTINED, as proposed, with their audit questions (5):** Rows 7.17, 17.4(ii) (are the old and the
  shipped decoders exact?); Rows 7.81, 7.84, 7.98 (which key candidates the dormant key decoder keeps, by
  what rule).
- **HISTORICAL, as proposed (6):** Rows 1.10, 10.52(ii), 48.2(ii) (the reserve shortcut never adopted);
  Row 1.14 (scoped to the legacy segmenter and scorer); Row 21.27 (a superseded proposal); Row 43.12 (the
  effort-setting plan).
- **Row 7.104(i) stays UNPLACED, and Row 43.12 is held at its proposal** — both travel with the question of
  which dials the ambition setting (D-202) gets, which returns to the user after the paper sizing.
  *(Corrected after the ruling record's §1c. Former wording, kept (#12): "Row 7.104(i), from UNPLACED →
  HISTORICAL: the old key decoder's rule that an effort preset may lower 'the candidate count kept per
  slice'; L2-S36 admits no such count, and whether any setting may loosen L2's search is OQ-L2-8's ruling";
  and Row 43.12 was listed among the HISTORICAL "as proposed". Placing either now would pre-judge the dials
  question.)*
- **Row 21.73, from UNPLACED → ADOPTED — proposed:** the sentence of 4.1.
- **Not placed here (3):** Rows 8.97, 8.113, 9.322(ii) travel with Row 8.96, **to the family that takes
  L2-S11 — my reading of where Row 8.96 goes**.

Counted: 8 + 5 + 6 + 1 + 1 + 3 = 24. **The cut:** L2-S36 is taken out of entry 279 §2 item 2's
confirmation set, which keeps L2-S35, L2-S42 and L2-S43. The user can change the cut.

### 5. What was read, what was not, and what is unsettled

- **Read:** the derivation at §0–§2, L2-S1, L2-S2, L2-S7, L2-S23, L2-S31 to L2-S43, §4 and §7;
  `FRAMEWORK.md` at C-1 to C-9, **the L1 charter's opening (question, publication list, "Decides
  nothing")**, the L2 charter, DP-A to DP-E, §8, §10 and §11; the comparison file at §5, §7's entries for
  L2-S23, L2-S35, L2-S36 and L2-S43, §8's entry for OQ-L2-8, and L2-S36's 24 rows at §6; the
  phase-definition surface §3; register entries D-004, D-030, D-031, D-035, D-098, D-200, D-201, D-202,
  D-297; the ten families' ruling records searched for this family's identifiers, the elaboration-relations
  record whole.
- **Not read:** the code; `cowork_joint_estimator_factorization.md`; OI-209, OI-215, OI-226, OI-227; Row
  21.39; any paper.
- **Unsettled** (*my reading*): whether the 13-of-23 empty results bear on running time; where, after
  this phase, the build's timing measurement sits; whether the elaboration relations are part of the
  searched state (L2-S33's family).

This surface writes no instruction for Claude Code, edits no tracked document, amends neither the framework
nor the register, and allocates no register number.

**The questions, to be put later, one per turn:** 4.1; then 4.2; then 4.3 with 4.4.

---

## §B. The check, run in the turn after the user's "continue"

Over completeness, coherence, correctness and absolutes, at the sources staged this sitting. **Nine
corrections, each made at its site; former wordings kept here (#12):**

1. §2, the reserve shortcut: *former* "consider key changes only to keys near the current one on the circle
   of fifths". Row 1.10 reads "restricting key-change candidates to a fitted-mass neighborhood on the circle
   of fifths"; "near" dropped the fitted extent.
2. §2, D-201: *former* "`CLAUDE.md` files that fault (OI-215, OI-227) in the family concerned with what the
   engine reads and which chords it admits. So the record does not treat it as a measurement of running
   time." `CLAUDE.md` names the family "struck-versus-sounding" and asks of phase-2 items whether they
   could hold facts about reads or admission; it does not say the fault is not about running time, and
   OI-215/OI-227 were not opened. A claim stretched past its object; now narrowed.
3. §2, the funnel: *former* "the first stage of the standing order 'desk-simulate → read-only probe →
   build' (the funnel under principle #17)". The quotation dropped its parentheses, and the funnel sits in
   the scope-of-surprise paragraph, not in #17; and #17(c) defines a desk simulation as a hand trace on
   corpus cases. Now quoted whole and the application marked as my reading.
4. §3, remedies: *former* list included "the selection-sized working span (C-8)" as making "the same exact
   search cheaper". C-8 bounds what is searched; it is not a speed-up of the same computation. Separated.
5. §3: *former* "The ratified charter makes the rule, and nothing I read argues against it." Fourteen
   outgoing rows DIFFER; narrowed to what they are.
6. §2, completeness: the existing design's undocumented narrowing of which chord classes a stretch may
   consider (Row 1.12, D-098) was missing; added.
7. §3, where the measurement runs: the answer rests on my reading that a probe is a code change; now said
   at the point.
8. §5: *former* "the charters for the note-cutting layer and for this layer". Only the L1 charter's
   opening was read; corrected, and §7's entries for L2-S35 and L2-S43 added to what was read.
9. §4.4: the routing of Rows 8.97, 8.113, 9.322(ii) "to the family that takes the one decision, L2-S11"
   is my reading of where Row 8.96 goes; now marked.

**Applied by analogy, now said:** §4.2's use of #17's provisional-value rule.

**Checked and standing:** every quotation of L2-S23, L2-S33's dependence, L2-S36, OQ-L2-8 and the
derivation's size sentence; the charter's "May not" and "local optimum"; C-8, §8.4, D-200, D-201, D-202,
D-035, D-297, D-004, D-098 at their entries; §3.4's two quoted clauses; the four family records' cost
wording; L2-S23's counts at the elaboration-relations record; all 24 of L2-S36's rows and their proposed
dispositions; the arithmetic 8 + 5 + 6 + 1 + 1 + 3 = 24. **None of the corrections moves a confirmation or
a placement.**

**Declared:** no shell command was run, in the container or on the device; no memory tool was used.

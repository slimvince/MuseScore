# Rulings — the regress-termination sitting, 2026-08-25

> **STATUS: RULING RECORD.** Cowork, 2026-08-25 (the forty-seventh Cowork session). An interim
> carrier under the standing clause that a sitting record is written in the turn its ruling is
> given and lands in git at the next dispatch's Task 0.
>
> **Taken at branch tip `0f18b358bc6a8da5ec6064760d675129e64d8f3b`, unmoved.**
> `refs/remotes/origin/master` reads `f225b61343ff3de022d32d6b7514d835b87093cf`. Both measured by
> this session by reading `.git/HEAD`, `.git/refs/heads/master` and
> `.git/refs/remotes/origin/master` with the file tools on the user's machine; no shell command was
> run on the repository.
>
> **This record is untracked and root-level. Writing it turns
> `tools/audit/evidence_pin_membership.json` stale, because
> `tools/audit/gen_evidence_pin_membership.py` derives over root-level `cowork_rulings_*.md`
> files.** That is the standing structural condition reported at the sixty-fourth handoff entry and
> is the subject of a design question still owed by the user. **Nothing was running when this record
> was written**; no batch was disturbed.

---

## 0. What was put, and in what form

The sitting arose from a question the user put at the session's opening and sharpened over six
turns: whether the project is getting closer to a first version of the specifications, and — when
the answer was no — what was blocking it. The chain was traced to a four-level climb of
establishment demands, which the user named in his own words:

> *"This is EXACTLY what I mean by venturing further and further away from the actual problem, for
> each meta-level we insist that meta-level must be provable - which creates the next meta-level -
> indefinitely."*

The user then directed: *"Do whatever you need to do in order to MAKE SURE that you suggest rule
amendments that will stop the behaviour we just discussed is not desirable, then put forward
decision surfaces as per usual."*

Three decision surfaces were written and delivered as user-visible prose before any choice
question (D-249), each option's pros and cons naming the principle it rests on and rated towards
the ultimate objective and towards the guiding principles (D-424). The choice questions are put one
per turn. This record carries the first.

## 1. Ruling 1 — an establishment demand with no inspectable object is terminated by scope and by declaration (Alternatives A and B together; the user's words: "A and B together")

**The finding the ruling rests on, verified at the sources this sitting.**

- **#19 (D-182) names a closed list of four objects.** Verbatim: *"An instrument, corpus, gate, or
  recorded figure is trusted only after being positively established (oracle cross-check,
  derivation of what the measurement unit actually measures, reproduce-check) — never because it is
  merely unfalsified."* Each of the three named establishment methods requires an object that can
  be re-run. A session cannot be reproduce-checked.
- **#18 (D-181) reaches only checkable claims, by its own recorded ground.** Verbatim: *"No design
  may carry load on a causal claim about our own system or data that is checkable but unchecked."*
  Its recorded ground: *"the prohibition is specifically about claims that are CHECKABLE — the cost
  of checking is what makes leaving them unchecked indefensible."*
- **A claim about a session's boot is not checkable from outside that session.** The sixty-fourth
  handoff entry's own degradation report says of the two probe results: *"received as reported and
  not auditable from outside the sessions that wrote them."*
- **The successor plan already rules by declaration in three places.** Ruling 8 of 2026-08-21 opens
  the pilot without the empirical findings ledger, *"the hole is declared in the pilot's source
  declaration, not hidden"*; Ruling 5 reports every unplaceable statement with its uncertainty
  range rather than blocking; Ruling 12 makes a unit needing more depth a stop and a request.
- **Ruling 4 of 2026-08-21, which extends #19 to the derivation method, makes the OUTPUT the object
  of establishment, not the session.** Verbatim: *"Reproducing the ruled intent, or a defended
  alternative the user would rank beside it, establishes the method (#19)."* The user is the judge
  of that output. Nothing in Ruling 4 makes a session's boot an object of establishment.

**Ruled — the amendment text, in two limbs.**

**Limb A — the scope fence.** The following is added to #19 (D-182):

> The objects of this principle are the four it names and no others — a measurement tool, a corpus,
> a gate, a recorded figure — and each is an inspectable, re-runnable artifact, because each of the
> three establishment methods named here requires one. A session, a person or a conversation is
> never the object of a Class B demand.

The following is added to #18 (D-181):

> Class A reaches a causal claim only where that claim is checkable, which is this principle's
> recorded ground. A claim about the conditions under which a session ran — its boot, its context,
> what reached it — is not checkable from outside that session, and is therefore declared, not
> established.

**Limb B — the terminator.** #24 (D-187) is extended from figures to results:

> Every reported result carries its uncertainty. Where a condition of a result's production cannot
> be established at an inspectable object, that condition is DECLARED as a bound and the result
> stands with the bound attached. A declared bound discharges an establishment demand that has no
> inspectable object. It does not discharge one that has.

**The recommendation this side gave, and its ground.** A and B together, and explicitly NOT
alternative C (a depth cap on recursion). Ground: A and B are a scope clause and one extension of
principles already standing — no new principle, no new artifact, no new check and nothing new to
maintain. C would have been a new rule and a new counting obligation: apparatus proposed as the
cure for apparatus, which is the shape the sitting exists to leave. Alternative D (change nothing)
was rated as making the user the sole error-detection mechanism, at a measured price of 25 ruling
sittings and zero specification statements over five days.

**Declined:** C, on the ground above. D, on the measured price.

## 2. Ruling 2 — the decision-surface guard is registered, and every surface states which ratified phase its act serves (Alternative A′; the user's word: "A′")

**The finding the ruling rests on, verified at the sources this sitting.**

- **Every one of the four meta-levels was put as a decision surface and ruled by the user.** The
  surface form was followed. What failed is that no surface carried what was needed to see the
  climb. Bar (a) of the sharpened decision-surface rule — do not act on the latest news regardless
  of the larger context and the larger plan — never fired, because no author of any of those
  surfaces believed they were chasing news; each was answering a real failure. **A guard that asks
  whether an act is justified cannot stop a climb, because every step of a climb is justified.**
- **The sharpened decision-surface rule is NOT in the decisions register.** `DECISIONS.md` was
  searched for "sharpen", "latest", "self-generat", "most recent finding" and "larger plan": no
  matches. The rule exists only as prose re-typed by hand into each successor handoff entry — the
  least durable place in the system, for the rule that catches everything else.
- **The two registered decision-surface rules are cited nowhere in the operating record.** `D-424`
  (a surface names the principle behind every pro and con and rates every option on two axes) and
  `D-249` (the whole surface is delivered as user-visible text before any choice question) return
  ZERO occurrences across the whole of `cowork_handoff.md`. The register and the operating record
  do not reference each other in either direction.
- **The measured price of the present arrangement:** 25 distinct ruling sittings between 2026-08-21
  and 2026-08-25, of which six — `blinding_failure`, `determination_route`, `forward_fact`,
  `method_voiding`, `next_act`, `second_vector` — have as their subject whether the test of the
  method was valid, and not the method, the analysis or any specification. Zero specification
  statements were produced in that window.

**Ruled, in two limbs.**

**Limb 1 — registration.** The sharpened decision-surface rule is entered in the decisions register
under its own identifier with its home named, so that it no longer depends on being re-typed into
each successor handoff entry. Its text is not changed by this ruling.

**Limb 2 — the field.** Every decision surface states, in one line, which of the ratified phases
the act it proposes serves — and where it serves none, says "none". No running tally is kept;
consecutive surfaces reading "none" are themselves the signal.

**Recorded as raised at the putting, not carried by the surface.** The surface put alternative A,
which included a running count of consecutive acts serving no ratified phase. A′ — the same
registration and field WITHOUT the count — was raised by this session at the putting and is
recorded as such, on the precedent of Ruling 11 of 2026-08-21. This side's recommendation changed
from A to A′ between the surface and the putting, on the volume finding of §3 below: a counting
obligation is a thing to get wrong, and [[OI-377]] is already open about a hand-count.

**Declined:** A, for the counting obligation A′ removes at no loss of signal. B (make #2
operational — name the specific open question an act closes, and require a ruling where that
question is about our own apparatus), because it catches the category and not the accumulation, and
all six climb sittings would have answered that the question was about the apparatus and
necessarily so. C (both A′ and B), for adding a second gate, one of them a judgement call, to every
proposed act. D (change nothing), on the measured price above — it leaves the user as the system's
sole error-detection mechanism with no document showing him what he needs to detect with.

## 3. The volume finding, recorded because two rulings rest on it

Put to this session by the user as a question — whether the number of rules and other standing
material is too much, and whether that is a common reason the rules are not effective. This side's
answer, recorded with its evidence:

- **Size is not the binding constraint.** This session made six counted errors (the counted-errors
  note at the foot of this record) while at roughly 15% of its context budget. Every one was a failure to RETRIEVE, not to hold: reasoning
  from glosses about texts never opened, with no way to know they should be opened.
- **The first-order cause is that the rules are not indexed to moments.** The register is organised
  by subject, which serves lookup when you already know a rule exists. Nothing is organised by when
  a rule fires. A rule attached to a moment is followable at any count; principles that all apply
  always, plus a register of 474 decisions with no situational index, are not followable at any
  count, and halving them would not help.
- **Three structural defects each manufacture apparent volume:** two rule systems that do not
  reference each other (above); rules with no trigger, of which #2 is the clearest — right words,
  never fires; and emphasis inflation in the handoff, whose entries escalate to five stars and
  whose current top entry bolds nearly every sentence, so that the marking carries no information
  and a reader falls back on recency and position — which is how a gloss comes to be treated as a
  source.
- **This supports the user's own observation of 2026-08-22** that pruning has not shrunk a session's
  boot context in practice. Pruning attacks size; size is not the problem.

**Carried as a condition on Rulings 1 and 2:** additions to the governing corpus are not free even
when each is small. What these amendments replace is a question owed and deliberately not bundled.

## 4. Ruling 3 — the existing derivation is judged first, then the held-out test is re-run, with the ledger running alongside (Alternative E then C, with B; the user's words: "E first, then C with B running alongside - if we are not operating on a too high meta level")

**Ruled with a condition, which this side answered before the ruling stood.** The user's condition
was that the acts not be at too high a meta level. Ruling 2's field was applied to each and
answered:

- **E** — the user reads the derivation that exists and judges it. This is the PILOT phase's own
  ruled postcondition, verbatim from the phase definition surface §3.2: *"the method is ruled
  usable, amended, or refuted by the user on evidence."* **Serves: the pilot phase.**
- **C** — a fresh session derives the harmony-boundary decision, producing a specification statement
  about how the analysis segments music. **Serves: the pilot phase.**
- **B** — the empirical findings ledger, a ruled preparation output. **Serves: the preparation
  phase.**

**None reads "none".** Set against the six climb sittings named in Ruling 2's findings, each of
which would have read "none", this is the field's first live use. **Recorded against this side: the
present sitting itself would read "none" on Rulings 1 and 2** — it is governance work, warranted by
the user's diagnosis, and it is the reason the sitting closes here rather than continuing to find
things to amend.

**Ruling 1's effect on this surface, recorded because it changed the ratings before the question was
put.** Under Ruling 1 a session's boot is a condition with no inspectable object and is therefore
DECLARED, not established. **The §0 check is consequently a declaration and not a measuring
apparatus.** Two consequences follow and are recorded as rulings of fact, not as new decisions:

- **The two §0 decisions the sixty-fourth handoff entry declared OWED BY THE USER — the §0 scope and
  the §0 timing — are MOOT and are discharged without being answered.** An apparatus that is not an
  apparatus has no scope defect and no timing hole to repair. The third decision that entry names
  (whether uncommitted root-level ruling records should be inputs to `evidence_pin_membership.json`)
  SURVIVES, blocks nothing, and is not ruled here.
- **Alternative C returned to being cheap**, which is the pilot's own ratified justification (*"prove
  the derivation method cheaply before trusting it"*). This side's recommendation of alternative A —
  opening the framework phase now on a declared UNTESTED verdict — was WITHDRAWN at the putting for
  that reason and is recorded as withdrawn, not declined on its merits.

**E, recorded as raised at the putting and not carried by the surface**, on the precedent of Ruling
11 of 2026-08-21. Its ground: Ruling 4 of 2026-08-21 establishes the method by *"reproducing the
ruled intent, **or a defended alternative the user would rank beside it**."* The second limb is a
judgement on the quality of the reasoning and does not require blindness. The user is the judge that
ruling names, being the holder of the ruled intent, and no bar on oracle-aware parties reaches him.

**E's bound, ruled with it.** E can establish the method on limb two ONLY. The match limb —
reproducing the ruled intent — is uninformative for a derivation whose session was contaminated.
**A verdict returned by E is a PARTIAL verdict and is recorded as one.** It does not discharge the
framework phase's prerequisite by itself; whether it does, with C's return, is a later question and
is not ruled here.

**The artifacts, named so the act is performable and NOT opened by this side.** The contaminated
first arm is `cowork_blind_derivation_harmony_boundary_2026_08_23.md`. The oracle Ruling 4 names is
the evidence-ranking ruling of 2026-08-11 at `ARCHITECTURE.md:394-402`. A comparison reading made
before the blinding failure was found stands as `cowork_comparison_harmony_boundary_reading.md`,
with `cc_report_comparison_harmony_boundary.md` beside it. **This session opened none of them.**

**Declined:** A, withdrawn at the putting as above rather than declined. D (refute the method and
design another), on the ground that the record is explicit the method is neither established nor
refuted — #19 forbids trusting something merely because it is unfalsified, and discarding something
merely because it is unestablished is the same error with the sign reversed. **B is not declined: it
runs alongside**, contending with nothing, being a Claude Code batch while E is the user's reading
and C a fresh Cowork session.

## 5. What these rulings do NOT do

No amendment is landed. The three amendment texts above are the ruled wording; the edits to their
home file are a landing act for a dispatch that does not yet exist. No dispatch is written. No
`src/` change, no build, no test, no guard run, no regeneration. No open-items row is created,
flipped or discarded. No finding number is allocated. No phase is un-held and no hold is lifted by
this record: **the framework phase stays HELD**, and Ruling 3 orders acts that may produce the verdict
rather than opening the phase without one. No entry is made in the decisions register by this record;
Ruling 2's registration limb is likewise a landing act for a dispatch that does not yet exist. No
handoff entry is written. **No session is opened by this record and no session is running** — E is the
user's reading, C is a fresh Cowork session the user opens, B is a Claude Code batch not yet
dispatched. None of the three blind or comparison artifacts was opened by this session.

**A question is owed and deliberately not bundled:** what these amendments replace, which follows
from §3.

---

*Provenance: Cowork, 2026-08-25, the forty-seventh session, at tip
`0f18b358bc6a8da5ec6064760d675129e64d8f3b`. Environment: the remote Cowork environment; every
governing document read from a bridge-staged snapshot with the file tools.*

*Declared departures and reading bounds. The session-start read was NOT taken and `CLAUDE.md` was
NOT opened — deliberately, so this session remains not oracle-aware by that route; the principle
texts quoted above were read as they are quoted inside `decisions/group_S.md`, which reproduces
`CLAUDE.md` lines 9–78, and no part of `CLAUDE.md` near lines 1489–1490 was read at any point.
`ARCHITECTURE.md` and `BUILD_AND_TEST.md` NOT read. Neither blind output read. The handoff was read
at its sixty-fourth entry whole, its sixty-third entry to line 400, the opening of its fifty-sixth
entry, and at targeted searches — NOT whole. `DECISIONS.md` was searched and read at its glossary
and at its group S table, NOT whole. `decisions/group_S.md` was read at eight entries only.
`cowork_rulings_2026_08_21_successor_plan_sitting.md` was read WHOLE.
`cowork_rulings_2026_08_15_phase_definition_sitting.md` and
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` were read at targeted
sections only. The start-state measurement of on-disk sizes and hashes ordered by the sixty-fourth
entry was NOT taken: a directory listing of the repository root exceeds the bridge tool's output
cap because of the standing untracked population, and no narrower route was authorised.*

*★ CONTAMINATION DECLARATION, made because the second contamination vector is a live subject of this
plan. This session READ the user's persistent memory filesystem at its boot, before it read the
handoff — `/preferences.md` and `/areas/musescore-arranger.md`, both in full. What reached it was
governance, vocabulary and protocol material together with corpus percentages and commit hashes.
No harmony-boundary withheld passage was observed in either file; that is an observation of what
was read and NOT a clearance, which this side is not qualified to give. This session therefore
stands contaminated by the memory vector and its own §0 report would have failed on that ground.*

*★ THIS SIDE'S OWN ERRORS THIS SITTING, counted and caught. (1) The user's standing instruction of
this date was filed to memory as a near-prohibition — "no automatic fixing unless" — and corrected
by the user, who stated that findings do lead to action and that the bar is judging each against
the perspective and the overall plan. (2) "The derivation method" was used without saying which
method, and the user had to ask. (3) #19 was characterised across three turns from the handoff's
glosses before its text was read. (4) The sharpened decision-surface rule was named as the
governing guard without checking whether it is registered; it is not. (5) The word "instrument" was
used in four consecutive turns against the 2026-08-17 vocabulary ruling that reserves it for a
violin and mandates "measurement tool". (6) An early account implied the meta-levels were
self-generated by sessions; they were each put as a surface and ruled by the user, and Ruling 4 of
2026-08-21 is his. All six were caught by the user, four of them by his asking a sharper question.
That the user is this system's working error-detection mechanism is itself a finding of the
sitting and is carried into its second surface.*

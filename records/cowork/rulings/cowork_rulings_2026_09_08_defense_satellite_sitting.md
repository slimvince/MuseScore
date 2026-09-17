# Rulings — the defense-satellite sitting, 2026-09-08

> **STATUS: RULING RECORD.** Cowork, 2026-09-08. Written in the turn the ruling was given, under the
> standing clause that a sitting record is written then and lands in git at the next dispatch's
> Task 0.
>
> **Taken at tip `d2ebe3cc98a33affdb5ffa2b8faf993bff6f0a71`**, read at `.git/refs/heads/master` with
> the file tools. Nothing was running. The surface ruled on is
> `ratification_surfaces/cowork_pruning_and_satellites_surface_2026_09_08.md`, delivered whole as
> user-visible text in its own turn with no choice question in that turn, and the questions were put
> one per turn as the standing form requires.

---

## 1. Ruling 1 — the defense of a rule MAY live in a satellite behind a pointer at the rule's home; the defense-at-home convention of 2026-08-01 is amended to that extent (Decision A of the surface; the user's words: *"Let us do A for now"*)

**What was put.** Whether the defense of a rule may live away from the rule — an amendment to the
standing convention of 2026-08-01 (`CLAUDE.md` Conventions; register entry **D-195**) that every
design decision carries its defense at its home. The surface put it as the user's own reason (c) of
2026-08-22 — *"the 'why' must not always be in the same place as the 'what' or 'how'"* — and as the
only route reaching the material a split cannot otherwise touch.

**Ruled.** The convention is amended: a rule's DEFENSE may be carried in a satellite, provided the
rule's own home carries a POINTER to it. **The rule itself does not move.**

**The user's own addition, given with the ruling and ruled with it, verbatim:** *"Maybe we could put
a note in the md that says thaT a must read - if we want to change anything - are its satellites?"*
**A session that intends to CHANGE a rule must read that rule's satellite first, and `CLAUDE.md`
states this.** The satellite is therefore a CONDITIONAL read whose condition is the session's own
intent to amend.

**Why the addition is not decoration — it is what makes the amendment safe.** The case AGAINST
moving a defense, stated on the surface, is that a rule whose ground is one hop away is a rule whose
ground stops being read, which is the never-work-from-memory failure (**D-112**) arriving by a
different door. The addition answers it exactly: the ground is not needed by a session that APPLIES
the rule; it is needed by a session that would CHANGE it, and that session is now told to read it.
**It also corrects a present weakness rather than only enabling a move:** as things stand nothing
tells an amending session to read a rule's history, while every session pays for that history at
every boot.

**It satisfies the mechanical-routing constraint the record already names.** The thirty-ninth
handover block (2026-08-22) records, as a reading, that routing to a satellite must be MECHANICAL —
a session must never read a file in order to learn whether it needed that file. *Am I about to
change a rule?* is answerable from the session's own dispatch before anything is opened. It is the
CONDITIONAL-READ pattern, ruled twice before (`docs/scoring_model.md`; Ruling 64's conditional read)
and applied a third time on 2026-09-07 to the eight conditional spans of `CLAUDE.md`.

### Two readings this side states, NOT ruled here, and each open to the user's correction

**(i) WHICH satellite is named at the site, never chosen by the session.** The note should bind a
session to read *the satellite the rule's own pointer names* — not "its satellites" as a class a
session identifies for itself. Otherwise the routing moves from the file into the session's
judgment, which is the thing the mechanical-routing constraint forbids.

**(ii) WHAT counts as a defense is already defined, and the definition is narrow.** The amended
convention's own words name three things and no others: **the published research or algorithm
adopted, the measurement that decided it, or the constraint that forced it.** Everything else stays
at the rule. In particular a CAVEAT THAT BOUNDS HOW A RULE OR A FIGURE IS READ is not a defense — it
is operative text a session acts on, and moving it out of the session-start read would carry live
material out of the boot, which is the failure the ruled doubt default exists against. This reading
is stated because the classification of 2026-09-08 found such caveats sitting in prose that reads
like a defense.

## 2. Ruling 2 — Decision B is DEFERRED, with a named re-opening condition rather than indefinitely (the user's words: *"wait with B until we hit your context/token-ceiling already on startup again (this is most likely fixed by now)"*)

**What was put.** Whether `DECISIONS.md` stays a whole-file session-start read, it being 127,608
characters of the 245,555-character boot — the majority of it — refused demotion once on 2026-08-17
on a ground the record preserved so that a later ruling could answer it.

**Ruled.** **DEFERRED. Nothing about `DECISIONS.md`'s session-start read changes.** The deferral
carries a TRIGGER stated by the user: **B is re-opened when a session again reaches its context or
token ceiling at startup.** It is therefore not an open item drifting; it is a decision waiting on an
observable event.

**The user's stated ground, recorded because a later session must be able to test it:** *"this is
most likely fixed by now"*. What the record holds on that: the 2026-09-07 membership ruling cut what
an ordinary session reads of `CLAUDE.md` from 160,955 characters to 97,805 — a reduction of 63,150 —
and the boot now measures 245,555 at `tools/audit/session_start_read_size.json`. **So something was
fixed, and by a measured amount. Whether it is enough is exactly what the trigger tests, and this
side asserts nothing about it.**

**What a later session owes on the trigger.** If a session reaches its ceiling at startup, that
observation is the condition firing and B returns to the user with the boot re-measured at that
tree. **A session must not re-open B on the ground that it thinks the boot is large.**

## 3. A CORRECTION THIS SIDE OWES ON ITS OWN SURFACE — Ruling 1's reach was UNDERSTATED

The surface presented Decision A as the route that reaches the MIXED class — the nineteen passages
of the classification where a live rule and the record of its own amendment are inseparable as
written. **That understates it, and the understatement was this side's.**

The classification's LIVE passages carry recorded defenses too. The convention of 2026-08-01 requires
one at every design decision, so a defense clause sits inside a large number of the seventy-six live
passages as well as inside the nineteen mixed ones. **A's reach is therefore the defense material
across the whole of the six session-start spans, not the mixed nineteen.**

**Two consequences follow and both are recorded rather than acted on.** The prize is larger than the
surface said — and it is UNMEASURED, so no figure is offered here. And measure-before-build
(**D-277**) is therefore not a formality on this one: the size of what would move must be derived
before anything moves, which is also what the user's own 2026-08-22 direction asked for when it said
the surface be built from sizes measured at the objects.

## 4. What these rulings do, together

Ruling 1 amends a standing convention and adds a conditional read; Ruling 2 changes nothing and sets
a trigger. **The next act is a MEASUREMENT and not a move:** derive, over the six session-start spans
of `CLAUDE.md`, how much is defense under the convention's own three-way definition, published as a
generated artifact so that no figure is authored. Only against that figure is it worth deciding
whether the satellite is one file or several, and what the note's exact wording is. **No text moves
until it is measured.**

## 5. What these rulings do NOT do

No text is moved, no satellite file is created, and `CLAUDE.md` is not edited — the note the user
asks for is not yet written, because its wording depends on reading (i) above and on the measurement.
No finding number is allocated. No open-items row is created, flipped or discarded; [[OI-380]]'s two
questions stand exactly as they stood, and neither is answered by Ruling 1 — a finer span unit is
still not commissioned, and the lint's scope still does not widen. No decisions-register entry is
written: Ruling 1 is a decision the register carries and its entry is owed under register rule (c),
which is presently discharged under the accumulated-run reading this line carries. Nothing is read,
regenerated or committed by these rulings. The reading pass and the pruning pass both stay paused,
and the gate is not lifted.

---

*Provenance: Cowork, 2026-09-08, at tip `d2ebe3cc98`. The surface was delivered whole in its own turn
and the decisions taken in the next. Every governing document read this session from a bridge-staged
snapshot with the file tools. The user's words, in order: "Let us do A for now and wait with B until
we hit your context/token-ceiling already on startup again (this is most likely fixed by now)."; "A:
Maybe we could put a note in the md that says thaT a must read - if we want to change anything - are
its satellites?"*

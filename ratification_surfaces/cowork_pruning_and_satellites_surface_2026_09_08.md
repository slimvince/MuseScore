# The pruning-and-satellites decision surface

**STATUS: a decision surface put to the user. Nothing is ruled here. No text is moved, no rule is
changed, no file is split, no row is created or flipped, and no register entry is written. No choice
question is asked in the turn that delivers this — the questions come one per turn, afterwards.**

This is the surface owed since 2026-08-22. It is written now because the classification pass of
2026-09-08 supplies the one thing it was always missing: a measured answer to what a restructure can
actually reach.

---

## 1. What you asked for, in your own words

On 2026-08-22, at a session's close, you said this. It was recorded as a direction and not a ruling,
and it is quoted here whole because a surface about it must not paraphrase it:

> *"It is likely that they could be further pruned, move things to satellite files, read only when
> needed. Maybe the language is verbose? Maybe we need satellite claude.md:s depending on the
> session's task (thinking or exploring or instructing or writing or coding or...). The same goes for
> all other files, split them in satellites, and satellites exist for different reasons: a)
> historical archeology b) all the gritty details c) the "why" must not always be in the same place
> as the "what" or "how" c) the LLM:s task at hand differs ... etc und so weiter ..."*

The ruling record of that same day says in terms that this direction is not ruled there and that its
decision surface is owed by a later session. Nothing since has written it. This is it.

## 2. The plain names of the things involved

Nothing here assumes you remember an identifier.

- **`CLAUDE.md`** — the standing-instructions file at the top of the repository. 162,259 bytes,
  1,918 lines.
- **`DECISIONS.md`** — the index of every recorded decision about how the system works: one row per
  decision, with the full entries in separate files underneath it. 130,229 bytes.
- **`STATUS.md`** — the short living record of what the last batch of work did. 17,491 bytes.
- **The gating-row list** — a small generated list naming which open issues currently block a stage
  from opening. A session reads the list, and opens the big issues register only when it needs a
  particular row.
- **The session-start read** — the set of things every session must read before it does anything.
  Since 2026-09-07 that is: six named spans of `CLAUDE.md`, the whole of `DECISIONS.md`, the whole of
  `STATUS.md`, and the gating-row list. **245,555 characters in total**, measured by the repository's
  own measurement tool and regenerated on 2026-09-07.
- **A "span"** — a named section of `CLAUDE.md`, named by its heading rather than by line numbers so
  that it cannot go stale when text moves.

## 3. What has happened to your direction since you gave it

Three of its four parts have been answered by acts already taken. That is worth stating plainly,
because it is what stops this surface being a menu.

**Part one — "satellite `CLAUDE.md`s depending on the session's task". This is delivered, and
delivered better than a file split would have delivered it.** On 2026-09-07 you ruled that a session
reads six spans of `CLAUDE.md` at session start, and eight further spans only when its own work
touches them — each of the eight naming the condition that calls for it in the file itself. That is
your task-kind routing, implemented as a membership rule rather than as separate files. It is
mechanical: a session never has to read a span to find out whether it needed that span, because the
condition is stated at the membership. And it cost nothing, because no text moved and so nothing
could be lost or duplicated in the moving. **The effect was measured: the ordinary session's read of
`CLAUDE.md` fell from the whole 160,955 characters to the 97,805 the six spans hold.**

**Part two — "further pruned". This route is now exhausted and the exhaustion is measured, not
guessed.** The pruning act of 2026-09-07 derived every span of `CLAUDE.md` that its archivability
test could reach, read each one whole, and moved none: two candidates, both left where they stood,
because each turned out to be a live statement carrying the opening of a preserved older wording, and
the rule is that doubt keeps a span where it is. And the growth of the file since the last big
archiving pass was attributed commit by commit at the git objects: in every amendment, the superseded
wording had already left the file in the same act that amended it. **So the file is not growing
because a pruning rule is being ignored. It is growing because each amendment leaves behind a pointer
and the ground for the amendment, which the rules require.**

**Part three — "the same goes for all other files". Measured, the answer is short.** The
session-start read has exactly four members. Two of them are small: `STATUS.md` at 17,316 characters
and the gating-row list at 2,826. The two large ones are `CLAUDE.md`'s six spans at **97,805** and
`DECISIONS.md` at **127,608**. The other big files in the repository — the handover record at 1.1
megabytes, the issues register at 363 kilobytes — are **not read at session start at all**. A session
opens the issues register when it needs a row and never reads the handover record except its entry
point. Splitting those two would not save a session one character of its boot.

**Part four — "maybe the language is verbose?" — is not answered by anything, and is not what this
surface is about.** Rewriting live rule text to be shorter is a different act from moving text
elsewhere: it changes the words a rule is made of, with the risk that the rule changes with them. It
is available and it is not proposed here.

## 4. What the classification pass found, and what it means

On 2026-09-08 `CLAUDE.md` was read line by line and every passage of the six session-start spans was
classified as one of three things:

- **a live rule** — text a working session acts on today: a rule, a bar, a stop condition, a
  prohibition, a caveat that bounds how a figure is read, or a pointer telling a session where to
  look;
- **a record of an amendment** — text whose subject is the history of the record itself: that a
  clause was narrowed or superseded, what its former wording was, which alternatives were declined,
  what it cost, and who ruled it when;
- **mixed** — a passage that is both, and inseparable as written.

112 passages. **Seventy-six are live rule with nothing to move. Seventeen are pure amendment record —
and five of those are one-line archive pointers that a previous ruling already fixed in place, so
they cannot move either. Nineteen are mixed.**

**The mixed nineteen are where the mass is, and they include several of the longest passages in the
file** — the rule about apparatus issues no longer drawing effort, the rule about what counts as a
delegation, the phase supersession, the rule about how the finish line is cut, the rule about which
shells may read a file. Each of them states a rule a session acts on today *and* the record of the
amendment that produced it, frequently inside one sentence.

**This is the same wall from the other side.** The pruning act hit it in September and wrote down what
would be needed to get past it: *a cut that separates a preserved wording from the live statement
announcing it*. It declined to invent one, because the record's two existing ways of cutting the file
into spans were each commissioned by a ruling with measured evidence behind it, and inventing a third
to reach one span is exactly the stretched judgment the doubt rule exists to prevent. That question —
whether such a finer cut should be commissioned — is already standing with you, on issue row OI-380.

## 5. The ceiling, which settles the size of the whole question

`CLAUDE.md`'s six session-start spans are **97,805** characters of a **245,555**-character boot.

**So if every character of `CLAUDE.md` left the session-start read entirely, the boot would fall to
147,750 — a cut of just under two fifths, and that is the absolute ceiling on everything discussed
above.** Inside that ceiling, what a clean split can actually take is the seventeen amendment-record
passages minus the five that cannot move — mostly short dated notes — plus whatever the mixed nineteen
would yield to a cut nobody has yet designed.

**And `DECISIONS.md` alone is 127,608 characters — more than half the boot on its own, and more than
the whole of `CLAUDE.md`'s session-start membership.**

That is the finding that reorders the question. **The work everyone has been discussing addresses the
smaller half.**

## 6. The two decisions this leaves, and nothing else

Everything above either is delivered, is exhausted, or has no measurable effect. Two questions
survive. Both are consequential, so each goes in its own later turn, one per turn, and neither is
asked here.

### Decision A — may the defense of a rule live away from the rule?

**What it is.** A standing convention of 2026-08-01 says every design decision carries its defense at
its home: wherever a rule is recorded, the record states *why* — the research adopted, the measurement
that decided it, or the constraint that forced it. That convention is why the mixed nineteen are
mixed. The rule and its ground sit in one passage because the convention puts them there.

**Why it is the live question.** Your own direction named this: *"the 'why' must not always be in the
same place as the 'what' or 'how'"*. That is not a file-shuffling idea — it is a proposed amendment to
that convention. **It is also the only route that reaches the mixed mass without inventing a new way
of cutting the file.** Instead of separating a live statement from a preserved wording inside a
passage, you would let the passage keep the rule and send the ground to a satellite behind a pointer.
The 2026-08-22 record already noticed this and recorded that whether a pointer satisfies the
defense-at-home convention **is yours to rule and no session's**.

**What is at stake either way.** Against: the convention exists because a defense written later from
memory is invention, and a rule whose ground is one hop away is a rule whose ground stops being read —
which is the failure the never-work-from-memory rule was written against, arriving by a different
door. For: the ground of a rule is, by construction, the thing a session does not act on; it is what a
session consults when it wants to challenge or re-take a decision. That is the same shape as the
gating-row list, where the answer is read at every boot and the evidence behind it is opened only when
a verdict is challenged — a pattern this project has already ruled twice and measured.

**What it would buy, honestly.** Some fraction of the mixed nineteen passages, which is some fraction
of 97,805 characters, which is some fraction of two fifths of the boot. It is the largest available
move on `CLAUDE.md` and it is still bounded by that ceiling.

### Decision B — does `DECISIONS.md` stay a whole-file read at every session start?

**What it is.** `DECISIONS.md` is read whole at session start, by rule (a) of its own section in
`CLAUDE.md`. It is 127,608 characters — the majority of the boot.

**It was already put and already answered once, and the record kept the ground so a later ruling could
answer it.** On 2026-08-17, when `BUILD_AND_TEST.md` was demoted to a conditional read, the same
treatment was considered for `DECISIONS.md` and ruled out. The ground is written into `CLAUDE.md` at
that spot, in these terms: rule (a) rests on the premise that **rulings bind mechanically only if
every session reads them**, and a condition would replace a mechanical bind with a judgment each
session makes about its own work *before* reading the thing that would tell it whether the judgment was
right. The passage says explicitly that it is recorded because a later ruling may revisit it and must
have the ground to answer.

**Why it comes back now, and it is not the same question.** It comes back because it is measured to be
the majority of the boot, which was not known then; the measurement that says so was repaired on
2026-09-07. And it comes back in a form the 2026-08-17 ground does not automatically defeat: the
question is not only *conditional or unconditional*. `DECISIONS.md` is an **index** — one row per
decision, with the full entries already living in separate files that a session opens as needed. So
the same index/detail split that already exists underneath it could be applied to the index itself,
without any session having to judge in advance whether it needed a decision.

**What is at stake.** This is the load-bearing member of the boot. Getting it wrong in the direction of
reading less is exactly the failure the 2026-08-17 ground names: a ruling that binds only the sessions
that happened to meet it. That failure has a second, already-rowed instance — the finding that
`CLAUDE.md` itself sometimes does not reach a session at all, which is open and for which no remedy is
proposed. **Any move on `DECISIONS.md` runs toward that hazard, and that is why it is a decision and
not an act.**

## 7. What this surface deliberately does not do

It proposes no split and rules none out. It does not ask you to choose between them here. It writes no
option list for the parts of your direction that the record has already answered — the task-kind
routing is delivered, the pruning route is exhausted, and the other big files are not in the boot, so
presenting those as choices would be manufacturing optionality over facts already settled.

It changes no rule, moves no text, and creates no row. It does not touch the reading pass or the
pruning pass, both of which stay paused, and it does not lift the gate.

---

*Every figure here is read at `tools/audit/session_start_read_size.json` (regenerated 2026-09-07) or
at a directory listing of the repository; the 147,750 figure is a subtraction over two of them and is
marked as such. The 2026-08-22 direction is quoted from the thirty-ninth handover block of
`cowork_handoff.md`, read whole at that block this session. The statement that it is unruled is read
at §6 of `cowork_rulings_2026_08_22_step_zero_return_sitting.md`. The two questions already standing
with the user are read at row OI-380 in `OPEN_ITEMS.md`. The classification is
`cowork_claude_md_live_rule_classification_2026_09_08.md`.*

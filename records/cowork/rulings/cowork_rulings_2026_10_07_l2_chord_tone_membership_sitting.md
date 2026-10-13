# Ruling record — the L2-S10 family (when a sounding note counts as a chord note) — 2026-10-07

> **STATUS: RULING RECORD.** Cowork, 2026-10-07 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_eight.md`. The surface these rulings are taken
> on is `ratification_surfaces/cowork_l2_chord_tone_membership_surface_2026_10_07.md` (29,738 bytes at this
> sitting's last staging; its §B is the check). The surface is not rewritten here and nothing in it is
> restated beyond what the ruling needs (#6). Each question is put alone, re-explained from scratch in plain
> words, with no widget, and each ruling is written here before the next question is put. Nothing is
> applied: the reading file's rows are re-marked, and amended texts written, by the application dispatch the
> L2 route ruling names as its step 2. No decisions-register identity is allocated.

---

## Ruling 1 — Decision 1 (the surface's §A.4.1): Row 6.45, the written spelling as a condition or as one weighed signal

**Put:** how to file Row 6.45 (`cowork_layer4_chordsymbol_design.md` §2: the notated spelling "is a
strong-but-fallible signal (engraving can be expedient; a MIDI import may carry arbitrary spelling), so it is
weighed, not trusted blindly, by the precedence ladder in §5"), against L2-S10 ("An event is a chord tone of a
span only if its spelled pitch class is a member of the span's chord, spelled"). Alternative A: HISTORICAL,
L2-S10 unchanged, the concern carried. Alternative B: held UNPLACED, travelling with OQ-L2-1. Alternative C:
L2-S10 amended now, the spelling a weighed signal. Recommended: A. Stated with the question: A and B file
only and leave L2's algorithm unchanged; C changes it.

**The user's words, verbatim:** *"A, if you by "allowance" mean "enharmonic allowance" (remember the rule
about language precision)."* Answered in the conversation: yes — every bare "allowance" in the question meant
the enharmonic allowance, a note counting as a chord member it sounds like though it is spelled differently.
The question had used the full term once and the bare word after it; that is a precision defect of the
question's wording, recorded here, and this record uses the full term throughout.

**What is ruled:**
- Row 6.45: **HISTORICAL** — a superseded design of the old per-slice chord engine.
- **L2-S10 stands as derived; its wording does not change.** Spelled membership stays the condition for a
  chord tone. **L2's algorithm as its statements define it is unchanged.**
- **Carried, not dropped (#12):**
  - Whether L2 admits an **enharmonic allowance** for chord-tone membership is decided by the closure
    measurement OQ-L2-1, as the derivation states ("an enharmonic allowance for chord-tone membership",
    derivation line 1205). L2-S10's share of OQ-L2-1 stays open; this ruling commissions nothing.
  - **A named gap, recorded with no route chosen:** OQ-L2-1 runs on the grading corpora it names and is not
    aimed at scores whose spelling was not written by a person (for example a score imported from MIDI, as
    Row 6.45 names). How often such a score's spelling leaves a chord unreachable is unmeasured. *(This side's
    reading of OQ-L2-1's design; whether any grading corpus was itself imported was not checked.)*
- Declined: Alternative B (the row would wait on a measurement not aimed at its imported-score half);
  Alternative C (a weighed-spelling cost no ground truth could fit, #20, #21; resting on the unchecked premise
  that misspelling is common enough to matter, #18; settling from a surface what the derivation routed to a
  measurement, D-254).

**Ground, as put (the surface's §A.4.1, as corrected at its §B):** towards the objective (#4), the spelled
distinctions the graded annotations write are kept — the German sixth against the dominant seventh (Row
50.26), the diminished seventh's root from its spelling (Row 6.101), the secondary leading tone read from the
spelling (Row 5.178); towards the principles, D-254 and #5, #18, #20 and #21, #12; the same shape as L2-S49
Ruling 1 of this date. Meta level: the analysis's own specification only.

---

## Ruling 2 — Decision 2 (the surface's §A.4.2): Row 24.39 claim (i), the old text on rootless jazz voicings

*Second sitting on this record: Cowork, 2026-10-07 (Stockholm), booted on
`records/cowork/handoff/cowork_handoff_entry_three_hundred_and_nine.md`.*

**The row's text** (`ARCHITECTURE.md` §5.8, *Known Analyzer Limitations*, *Rootless voicings*; re-read this
sitting at the comparison file, Row 24.39): "Correct handling requires knowing that a bass instrument is
providing the root, which is context the current analyzer does not have." Claim (i): reading such a chord
correctly requires knowing that a bass instrument supplies the root.

**How the question was corrected before it was put, on the user's challenges.** The surface's heading asked
"must the analysis know which instrument supplies a missing root?". The user: *"How can anybody play a
missing note?"* — the root is not missing from the music; in the situation the old text describes, it sounds
in another part. Then: *"For inference, do we have to know if there is anybody being a 'chord-playing
part'?"* — checked at the derivation: no L2 statement reads a part's role or instrument. L2 reads the sounding
set of all staves fed to the analysis (L2-S10), weighs the structural bass against the lowest sounding pitch
of each slice as "a reading decision, not a notated fact" (L2-S28), and reads per-voice melodic relations only
for elaborations (L2-S24). Then: *"how could the old analyzer NOT take in consideration that the chord's root
was played by another instrument!?"* — answered: this side cannot tell; the old text contradicts itself ("When
no root is present — … where the bass instrument provides the root"); two unchecked readings (the bass staff
not among the notes analysed; or the bass playing a passing note at that moment, so the root sounded nowhere
and the lowest note was promoted). That question is about old code and belongs to the audit with claim (ii).

**Settled by L2's own statements, not put as a choice (D-599):** claim (i) is **HISTORICAL** for L2 — L2 does
not need a part's role, and admits a chord whose root does not sound (L2-S10).

**Put:** what becomes of the idea behind it. A: written into the jazz named increment's premise list as a
thing to check, worded "Do a walking bass's passing notes mislead the chord reading? If so, is knowing which
part is the bass one useful remedy?", measured if there is reason to think it would improve the reading. B: L1
asked to publish each part's instrument now. C: dropped. Recommended: A. Stated with the question: every
alternative files only; L2's algorithm as its statements define it is unchanged.

**The user's words, verbatim:** *"A. BUT we will most likely not be able to "tell" who is subjectively (or
compositonally) the "bass". It must not be any specific instrument - could be a pianist's/accordeonists/
harpists/organist's/cembalist's left hand, an upright bass, a guitar, a basssoon or whatever."*

**What is ruled:**
- Row 24.39 claim (i): **HISTORICAL** for L2. **L2's algorithm as its statements define it is unchanged;
  L2-S10's wording does not change.**
- **Carried to the jazz named increment's premise list (chord-vocabulary Ruling 2 of 2026-10-05), with the
  user's condition as part of it:** whether a bass line's passing notes (a walking bass, for example) mislead
  the chord reading, and if so what remedies it. **The bass is a musical function, not an instrument:** it may
  be a keyboard player's left hand (piano, accordion, harp, organ, harpsichord), an upright bass, a guitar, a
  bassoon or any other part. **Which part carries the bass line is most likely not determinable**, whether
  meant as heard or as composed. No remedy may rest on naming a bass instrument; where a remedy needs a bass
  line, identifying it is itself a reading carried with its rivals, not a notated fact (the same footing as
  L2-S28's structural bass, and D-389's line between a notated voice and an inferred line).
- Declined: B (an L1 obligation decided from an L2 question with no premise examined, #17, #18 — and an
  instrument name would not identify the bass function in any case, on the user's ground); C (#12).

**Ground:** towards the objective (#4), the possible gain is examined where it could matter (jazz ensemble
writing) and nothing unchecked enters a specification; towards the principles, #12, #18, D-254, #6. Meta
level: the analysis's own specification.

**Corrections recorded with this ruling (staleness fixed at its sites, former wordings kept there):** the
surface's §A.4.2 heading and its sentence that the old analyzer "misread such chords" (stated as fact, never
checked); entry 309's §1 description of Decision 2. Both used "missing root".

---

## Ruling 3 — Confirmation 3 (the surface's §A.4.3): Rows 6.77 and 6.143, the old rule "never a new chord from too few notes"

**Put** (the surface delivered in one turn, the question in the next): file both rows QUARANTINED, with the
audit question of their sibling Row 6.96 ("does the dormant decoder's sufficiency test count three distinct
chord-tone pitch classes after membership, and how often does it fail on annotated chords?"). Row 6.77
(`cowork_layer4_chordsymbol_design.md` §4): "A new symbol is never committed from too few notes (this is the
rule the phantom-root defect violated)." Row 6.143 (same design, §9): "Chosen: a slice that cannot fix a chord
from its own gathered notes either inherits the prevailing chord (when consistent) or is marked "uncertain" —
a new symbol is committed only from enough notes." Stated with the question: files only; L2's algorithm
unchanged — L2 has no minimum number of notes for naming a chord and weighs a thin stretch like any other
(L2-S11, L2-S32). Put as a confirmation because the record answers it (D-599): the silence ruling of
2026-10-05 (no "uncertain" flag; that engine's commit / inherit / decline steps placed QUARANTINED in its
Ruling 2) and chord-vocabulary Ruling 1 (L2-S2: an annotated reading is excluded only by a named ruling
carrying its ceiling cost).

**The user's word:** *"confirmed"*.

**What is ruled:** Rows 6.77 and 6.143 **QUARANTINED**, with Row 6.96's audit question. **L2's algorithm as its
statements define it is unchanged; L2-S10's wording does not change.** Carried: the phantom-root failure stays
on record at Row 14.18 (proposed QUARANTINED); whether weighing alone keeps phantom roots away is a question
for the measurement stage (this side's reading).

---

## Ruling 4 — Confirmation 4 (the surface's §A.4.4): Row 43.23, the chord layer deferring a symmetric chord's root

**Put** (the explanation delivered, re-delivered at the user's request with documentation and algorithm kept
apart, the question in a later turn): file Row 43.23 HISTORICAL — a superseded plan. The row
(`cowork_target_architecture.md` §2, the minimality rule's worked example): "resolving a symmetric chord's
spelled root (diminished-seventh / augmented) needs spelling + function — a later layer — so the chord layer
names the *quality and bass* and **defers the root**, rather than pinning it by voice-leading or spelling
cleverness it shouldn't own." Stated with the question, separately: **documentation** — only the row's filing
label is set, its text not edited; **algorithm** — nothing changes, no L2 statement added, removed or
reworded. Put as a confirmation because the record answers it (D-599): the one-decision Ruling 1 of
2026-10-06 placed 22 rows of this shape HISTORICAL on Ruling 1 of 2026-08-29 ("Deferral-as-ownership ends for
the deciding layers: no question's answer is assembled across stages"). Declined: QUARANTINED — the row is a
design rule, not a description of the code.

**The user's word:** *"confirmed"*.

**What is ruled:** Row 43.23 **HISTORICAL**. **L2's algorithm as its statements define it is unchanged.** What
survives of the idea is already in L2's statements and in rows proposed carried (a diminished seventh's root
read from its spelling where the spelling shows it, Rows 6.101, 6.119(i), 6.145(i); otherwise the rotations
are rivals with their weights, L2-S43 — relayed from the no-early-discarding record, not re-read).

**The user's correction to carry:** *"explain and separate what is documentation-only and what is actual
algorithmical changes"* — every question states the two in separate parts, the documentation effect first,
the algorithm effect second, and anything describing what L2's statements already say is marked as
description, not change.

---

## Ruling 5 — §A.5: the remaining 22 parts as the comparison proposed them

**Put** (the parts listed in plain words, each row re-read whole at the comparison file this sitting, in one
turn; the question in a later turn): 8 ADOPTED — carried (L2-S10): Rows 1.47(ii), 6.101, 6.108(i), 6.119(i),
6.145(i), 6.199, 8.130, 50.26 (all AGREES at the comparison); 10 QUARANTINED with the comparison's audit
questions: Rows 3.25, 6.102, 5.178, 6.94, 6.96, 14.17(ii), 23.300(ii), 30.2, 24.37, 24.107(ii); 4 HISTORICAL:
Rows 23.219, 23.221, 23.242, 39.302. **Documentation:** each part gets the label above; no outgoing text is
edited. **Algorithm:** nothing changes.

**The user's clarification before the question, to carry as standing:** *"when you confirm that no
algorithmic change is being decided - tell me the currently decided method/algorithm."* The method stated in
answer, each quotation re-read at the derivation this sitting: L2-S1 (one reading of the working span:
boundaries, tonality, chord, per-event assignment); L2-S11 (boundaries decided with tonality, chord and
assignments in the one decision); L2-S10 whole; L2-S32 ("The coverage part is a cost, never a requirement");
L2-S28 (the figure's structural bass "a reading decision, not a notated fact"); L2-S43 (no reading discarded
before the whole working span is scored; equal scores published with equal mass, a declared principal, the tie
flagged); open for measurement: the enharmonic allowance (OQ-L2-1, Ruling 1); for jazz, the bass-line premise
with the user's condition (Ruling 2).

**The user's word:** *"confirmed"*.

**What is ruled:** the 22 parts placed as listed. **L2's algorithm as its statements define it is unchanged;
L2-S10's wording does not change.**

**The family is placed.** 2 already placed + Ruling 1: 1 + Ruling 2: 1 + Ruling 3: 2 + Ruling 4: 1 + Ruling 5:
22 = 29, against §7's 17 AGREES and 12 DIFFERS.

---

## Ruling 6 — §A.6: how far the ultimate objective's precedence reaches (governance, not the analysis)

**Put** (the surface in one turn, the question in the next): the open question `CLAUDE.md` states at
Conventions, *How a decision surface is written*, step 4 — "Where the objective and the principles conflict,
the objective takes precedence — **and how far that reaches is an OPEN QUESTION the user has not answered**:
read at its widest it could be taken as licence to override #18, #19 or #20 by asserting a benefit to the
objective … Until he answers, it is applied as written, and any case where the wide reading would change an
outcome is flagged to him." — against the user's two statements of 2026-10-07 (L2-S49 record, Rulings 3 and
5). A: settled as those words read — the objective outranks every design rule and principle in the long run,
acting through evidence; an asserted benefit overrides nothing, #18–#20 being how a benefit is established;
the flag ends. B: settled at the widest. C: not settled. Stated with it: the alternatives had largely
collapsed to A. **Documentation:** the step-4 sentence gets a standing answer, the edit made later by Claude
Code under a dispatch (Cowork does not edit `CLAUDE.md`). **Algorithm:** none.

**The user's words, verbatim:** *"A — the point is that we open up the backward edge WHEN we have reason to
suspect it might be beneficial - and this then needs to be investigated, tested, measured (#18, #19, #20)."*

**What is ruled:**
- **A.** The ultimate objective (maximum-precision inference, #4) is the prime objective and outranks every
  design rule in the long run. **It acts through evidence:** a design rule holds while there is no reason to
  suspect that breaking it would improve the inference; when there is such reason, the departure is opened up
  for investigation and is investigated, tested and measured under #18, #19 and #20 before it carries load.
  An asserted benefit by itself overrides nothing. The backward edge (D-466) is the user's worked instance.
- Step 4's per-case flag is no longer owed once the sentence is amended.
- **Carried for the next dispatch (not applied here):** amend `CLAUDE.md` Conventions, *How a decision surface
  is written*, step 4, replacing the OPEN QUESTION clause with this ruling, former wording preserved in place
  (#12). No decisions-register identity is allocated (the register's rule (c) is suspended; the route is
  `cowork_register_rule_c_suspension_2026_08_28.md`, as that block states).

---

## Not yet put (for the next sitting)

Nothing. Every item of the L2-S10 surface is ruled.
*(Former wording, preserved (#12): "§A.6 (how far the ultimate objective's precedence reaches, carried from
entry 308 §2).")*
*(Earlier former wording, preserved (#12): "The 22 parts of §A.5; and §A.6 (how far the ultimate objective's
precedence reaches, carried from entry 308 §2).")*
*(Former wordings, preserved (#12): "Decision 2 (§A.4.2, Row 24.39 claim (i)); Confirmation 3 …"; then
"Confirmation 3 (§A.4.3, Rows 6.77 and 6.143); Confirmation 4 …"; then "Confirmation 4 (§A.4.4, Row 43.23);
the 22 parts …")*

**The family's arithmetic.** All 29 row-parts under L2-S10 are placed (Ruling 5 above); none remains.
*(Former wordings, preserved (#12): "… 1 HISTORICAL by Ruling 4 (Row 43.23); 22 not yet ruled (§A.5). 2 + 1 +
1 + 2 + 1 + 22 = 29."; "… 26 not yet ruled (Decision 2: 1; Confirmation 3: 2; Confirmation 4: 1;
§A.5: 22). 2 + 1 + 26 = 29."; then "… 25 not yet ruled … 2 + 1 + 1 + 25 = 29."; then "… 23 not yet ruled
(Confirmation 4: 1; §A.5: 22). 2 + 1 + 1 + 2 + 23 = 29.")*

---

## Departures and bounds of this sitting

The device-info call was first; `C:\s\MS` was requested after it; the repository root was not listed.
Folders listed: the handoff folder, the rulings folder, `ratification_surfaces`. Repository files were staged
by path and read with the file tools. **One departure:** in the check turn, a shell command was run in the
container to append the surface's §B to this side's own working copy and to count its bytes; it read no
repository file. It is declared in the conversation, in this record and in entry 309. No memory tool, git,
widget, task list, subagent or web access. **The bridge fault fired once in its stale shape** on the surface's
check landing (the §A edits present, §B missing, 26,152 bytes); a second commit landed it whole (29,738 bytes,
§B's last line present at the staged-back copy).

*Provenance: Cowork, 2026-10-07 (Stockholm). The user's words: the opening instruction; "continue" (the
check); "continue" (Decision 1); the answer quoted under Ruling 1.*

**The second sitting (booted on entry 309).** The device-info call was first; `C:\s\MS` was requested after
it; the repository root was not listed. Folders listed: the handoff folder, the rulings folder,
`ratification_surfaces`. Repository files were staged by path and read with the file tools. **No shell
command was run**, in the container or on the device. No memory tool, git, widget, task list, subagent or web
access. *Provenance:* the opening instruction; the four challenges quoted under Ruling 2; "rephrase it all,
again"; "continue"; the answer quoted under Ruling 2; "continue"; "confirmed" (Ruling 3); "Again - explain and separate …" (quoted under Ruling 4); "continue";
"confirmed" (Ruling 4); the clarification quoted under Ruling 5; "continue"; "confirmed" (Ruling 5); the answer quoted under Ruling 6.

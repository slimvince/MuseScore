# Rulings — the step-zero return sitting, 2026-08-22

> **STATUS: RULING RECORD.** Cowork, 2026-08-22 (the fortieth Cowork session). An interim carrier
> under the standing clause that a sitting record is written in the turn its ruling is given and
> lands in git at the next dispatch's Task 0.
>
> **Taken at branch tip `64e7d2fd7f`** (parent `a1d7d95ecc`; `refs/heads/master` and
> `refs/remotes/origin/master` both at the tip), read by this session with `git show -s` and
> `git for-each-ref` at the explicit hash on the user's machine immediately before the sitting.
> The objects ruled on are the four findings of `cc_report_step_zero.md` §6, the report of the
> dispatch `cc_instruction_successor_plan_landing_and_step_zero.md`, executing Rulings 6 and 7 of
> `cowork_rulings_2026_08_21_successor_plan_sitting.md`. No document ruled here is generated.

---

## 0. What was put, and in what form

The four findings are put one per turn (the user's 2026-08-21 direction), each self-contained: the
things named re-explained from scratch, every alternative with its case for and against, the rating
towards the ultimate objective and towards the guiding principles, and the recommendation. The
user rules in a later turn. Each ruling is recorded below in the order put, in the user's own words
where the user gave them.

## 1. Ruling 1 — `STATUS.md` LEAVES the specification document set, by an authored exclusion; `STATUS.md` and `STATUS_ARCHIVE.md` become fact-gate mining inputs, read once, whole, after the pilot establishes the method (Alternative A as amended by the user; the user's word: "approved")

**The finding ruled on.** `cc_report_step_zero.md` §6 finding 2: `STATUS.md` is a member of the
derived document set by the ruled mechanism — the admitted delegation at `ARCHITECTURE.md:4265`
("the authoritative, current implemented/planned state lives in STATUS.md. Where a heading's status
and STATUS.md disagree, STATUS.md wins") — and contributes 200 of the 437 changed passages of the
widened July screen, all unread (`tools/audit/july_screen_report.md`, the per-document table), while
its subject is implementation status and not a specification of the analysis. The derivation's own
grade flags this (`tools/audit/specification_document_set.json` → `the_grades`, target `STATUS.md`).

**Ruled.**

(a) `STATUS.md` is EXCLUDED from the specification document set. The exclusion is an AUTHORED
INPUT to `tools/audit/gen_specification_document_set.py`, carrying the finding, the date
(2026-08-22) and the reason — the D-677 shape: an input to a derivation, never a hand edit to its
output — so that `--check` still re-derives the set. The derivation's name states the exclusion
(D-661: "derived from the admitted delegations, less one authored exclusion"). The ground is the
plan's own §5 exclusion ground: a process record is not a specification of the analysis.

(b) The delegation at `ARCHITECTURE.md:4265` is UNTOUCHED. Membership of the document set and
being a delegation target are different questions; nothing here edits a delegation.

(c) The 200 changed passages of `STATUS.md` STAY in the candidate enumeration
(`tools/audit/doc_change_candidates.json`) untouched (#12). They leave the widened screen
population and its read-share denominator; they are not read by the screen and carry no verdict.

(d) `STATUS.md` and `STATUS_ARCHIVE.md` are RECLASSIFIED as FACT-GATE MINING INPUTS under the
plan's §5 clause for process records ("enter only as mining inputs behind the fact-gate"). ONE
whole read of both is OWED, in its own run, AFTER the pilot has established the method (Ruling 4 of
2026-08-21), because the admission test applied in that read — *does the fact survive the
implementation being thrown away?* — is what the pilot exists to prove usable. Its output is the
list of surviving statements with their sources in the ledger's ruled entry shape (Ruling 8 of
2026-08-21), or the recorded finding that there were none. This is a PLAN LINE, not a dispatch (the
just-in-time rule).

**The user's stated ground, verbatim:** *"Best case 'status.md' is a history of what has been
done, not anything explaining why we do inference in a certain way - and in that case rewriting the
specs should theoretically not gain anything of knowing in which order and when any piece of work
(also including other things than specs and code) was done."* — with the later read proposed by the
user to make sure nothing was missed.

**Why the later read is owed rather than discarded (#10's cheap look).** The record shows the
best case has not always held: two grading conventions were "homed here 2026-08-02 from
`STATUS_ARCHIVE.md`" (`CLAUDE.md` gate block (A), OI-272), D-315 was "recorded ONLY in
`STATUS_ARCHIVE.md`" until 2026-08-08, and `DECISIONS.md` (line 264) states both archives were NOT
read in full by the register's enumeration.

**The alternatives declined.** B — `STATUS.md` stays a member and its 200 passages are read by the
screen: declined, effort with no ruled consumer (Ruling 12's depth inputs are per reconstruction
unit and no unit is derived from `STATUS.md`). C — stays a member, distribution partitioned out of
both consumers: declined, two mechanism changes for one authored input, and a measurement with no
consumer. D — defer until the other 144 are read: declined, the facts the ruling turns on are
already measured.

**What this ruling does NOT do.** No finding number is allocated. No open-items row is created,
flipped or discarded; [[OI-179]] stays OPEN and GATES. No standing clause is amended. The screen's
method, period and the existing verdicts are untouched. Nothing is read, regenerated or committed
by this ruling; the exclusion is executed by the next dispatch.

## 2. Ruling 2 — the nine members the screen cannot see KEEP their membership and are read whole by the derivation; ONLY their pollution input is recorded as "NOT EDITED IN THE RESTRUCTURING PERIOD; authored before it" (Alternative A; the user's words: "If we exclude them ONLY for the pollution measurement - then ok.")

**The finding ruled on.** `cc_report_step_zero.md` §6 finding 1: nine of the document-set members
have no changed passage in the candidate enumeration because no commit of the restructuring
period (opening EXCLUSIVE at `9306dc5072`, 2026-07-11; ending at `f2da61f8cd`, 2026-08-14; 435
commits) touched them — `cowork_layer1_note_model_design.md`, `cowork_layer2_slicing_design.md`,
`cowork_layer4_chordsymbol_design.md`, `cowork_layer5_engagement_design.md`,
`cowork_progression_schema_design.md`, `cowork_progression_schema_dictionary.md`,
`cowork_target_architecture.md`, `cowork_idiom_entry_mapping.md`, `docs/llm_integration.md`
(`tools/audit/july_screen_report.md`, "The coverage gap"). This session measured, by `git log`
over explicit hash ranges on the user's machine, that each was last edited BEFORE the period
opened (between 2026-06-07 and 2026-07-10) and that none was touched between the period's end and
the tip `64e7d2fd7f`.

**Ruled.**

(a) The nine REMAIN members of the specification document set. They are sources for the
derivation exactly as every other member is: read whole, every statement tested at the fact-gate,
every unplaceable statement a finding to the user (Ruling 5 of 2026-08-21). NOTHING is excluded
from the derivation, and no file is archived, moved or deleted.

(b) ONLY the pollution input of Ruling 12 is affected. For each of the nine, the July screen's
per-document value is recorded as a DECLARED THIRD VALUE — "NOT EDITED IN THE RESTRUCTURING
PERIOD; last authored before it, at <commit, date>" — derived by the generator from the candidate
enumeration and from git, never hand-typed (#17f, D-431). It is distinct from a measured
distribution and from "clean": the screen measures corrections made toward the code DURING the
period and has never measured authoring-time influence for any member; the fact-gate tests that,
per statement, for every source.

(c) The reading depth for a unit sourced from one of the nine is declared from the other two
properties (LIVE or DORMANT; declared establishment status) and the dependency structure, with
the value in (b) stated as the pollution input; Ruling 12's own STOP (a unit that proves to need
more depth stops and asks) is unchanged.

**The user's worry, recorded with the ruling.** *"my worry was that valueable knowledge will be
forever lost if we exclude the listed doucments."* Answered by (a) and by the standing record:
#12, Ruling 5 and Ruling 11 (one ratified replacement, ratified by the user having seen what it
replaces). The nine are the original design documents, written before the restructuring period
began correcting text toward the code.

**The alternatives declined.** B — widen the candidate enumeration to the nine members' whole
histories: declined, the per-passage grain collapses on an authoring commit, two of the four
classes are period-defined, and the falsification rule would fire by construction — a method
change Ruling 7 forbids. C — a new per-statement pollution read of the nine: declined, a new
measurement needing its own establishment (#19) that duplicates the detail-specification phase's
own fact-gated reading. D — record UNDECLARED: declined, discards a measured fact (#12).

**What this ruling does NOT do.** No finding number is allocated. No open-items row is created,
flipped or discarded; [[OI-179]] stays OPEN and GATES. The screen's method, period and existing
verdicts are untouched. Nothing is regenerated or committed by this ruling; the generator change
in (b) is executed by the next dispatch.

## 3. Ruling 3 — the document set stands as derived under rule (k); the documents the governance clause reaches only by glob or ellipsis are NOT members and become fact-gate mining inputs; the write-list route (rule (k)'s own remedy) stays open to the user per document (Alternative A, with B available afterwards; the user's words: "I agree with your recommendation")

**The finding ruled on.** `cc_report_step_zero.md` §6 finding 3: `ARCHITECTURE.md`'s document-
governance clause (`ARCHITECTURE.md:558-560` at the tip: *"The per-layer / per-component design
docs (`cowork_layer*_design.md`, `cowork_progression_schema_dictionary.md`,
`cowork_progression_schema_design.md`, the phrase-boundary design, …) are the authoritative detail
for their own scope"*) reaches the per-layer documents only through a glob and an ellipsis, which
`CLAUDE.md` decisions-register rule (k) (D-546, LIVE, user-ruled 2026-08-04) makes confer nothing.
Measured by this session at the tip object: the glob matches eleven files; seven are members by
separate explicit delegations; `cowork_layer2_reslice_design.md` is named only as a bare appended
citation (graded not admitted, `specification_document_set.json` → `the_grades`); four are not
named in `ARCHITECTURE.md` at all — `cowork_layer1_extend_design.md`,
`cowork_layer1_tone_collection_design.md`, `cowork_layer3_keymode_impl_design.md`,
`cowork_layer3_reachback_design.md`. None of the five was read by this session.

**Ruled.**

(a) Rule (k) is applied as ruled and is not reinterpreted. The specification document set stands
as derived: the five documents above are NOT members.

(b) The five are FACT-GATE MINING INPUTS — the class Ruling 1(d) of this sitting names — read once,
whole, behind the admission test, in the owed mining run after the pilot establishes the method.
Every statement survives or is withdrawn with its reason recorded (#12). A document the mining run
shows to carry a rule nothing else carries is a FINDING to the user.

(c) The write-list route stays open to the user: an explicit delegation written by the user into
`ARCHITECTURE.md` (rule (g)) makes a document a member on the next derivation, with the three
member properties declared. No session writes one. An edit to `ARCHITECTURE.md` made for this
purpose is a changed passage after the screen's period and is declared as such.

(d) The governance clause itself is not edited.

**The alternatives declined.** C — read the glob as naming every matching file at derivation
time: declined, the reading rule (k) forbids for its stated reason. D — rewrite the governance
clause to list its members: declined, it is B in a larger edit to the clause the derivation keys
on, achieving nothing B does not.

**What this ruling does NOT do.** No finding number is allocated. No open-items row is created,
flipped or discarded; [[OI-179]] stays OPEN and GATES. D-546 is untouched. Nothing is read,
written to `ARCHITECTURE.md`, regenerated or committed by this ruling.

## 4. Ruling 4 — the declared near-tie stands as graded: `cowork_idiom_entry_mapping.md` remains a member, its near-tie declared at the grade; the write-list route stays open (Alternative A; the user's words: "Agree with A.")

**The finding ruled on.** `cc_report_step_zero.md` §6 finding 4: the grade of
`cowork_idiom_entry_mapping.md` (`specification_document_set.json` → `the_grades`, the one
declared near-tie) — admitted on the form-first precedence from the single naming at
`ARCHITECTURE.md:5473` ("the per-entry re-tag is `cowork_idiom_entry_mapping.md`"), with the
competing appended-citation reading recorded beside it. The member is DORMANT
(`ARCHITECTURE.md:5472`), its own banner declares it "Provisional, easy to revise", and it carries
zero changed passages in the screen's period.

**Ruled.** The authored grade STANDS. The member remains in the set with its three properties
declared. No session overturns a declared near-tie by judgment (D-436). The user may settle the
form permanently by writing an explicit delegation or non-delegation into `ARCHITECTURE.md`
(rule (g)); none is written now.

**The alternatives declined.** B — take the competing reading and move the document to the
mining-input class: declined, a per-case override of the bar's own precedence rule for no yield.
C — the user writes the form now: available, not taken, nothing turns on it.

**What this ruling does NOT do.** No finding number, no row, no edit, no regeneration, no commit.

## 5. What these rulings do, together

All four findings of `cc_report_step_zero.md` §6 are ruled. The next Claude Code dispatch — NOT
written by this session (its degradation threshold was reached; see the fortieth handover block)
— executes: Ruling 1(a) (the authored exclusion of `STATUS.md` in
`gen_specification_document_set.py`, with the derivation's name updated under D-661) and the
consequent re-derivation of the widened screen population and the July screen (Ruling 1(c)); Ruling
2(b) (the declared third pollution value with the authoring commit and date, generated); then
either the continuation of the per-entry pass from the artifact's own `NOT YET READ` set (now 144
changed passages outside `STATUS.md`, per `july_screen_report.md` — re-derive it, do not carry
it), or the opening of the pilot under Rulings 3, 4 and 8 of 2026-08-21, or both in one dispatch
with the stoppable pass SECOND (D-670). Rulings 3 and 4 order no act in that dispatch. Two plan
lines are added, not dispatches: the owed whole read of `STATUS.md` + `STATUS_ARCHIVE.md` (Ruling
1(d)) and of the five glob-only documents (Ruling 3(b)) as fact-gate mining inputs, after the pilot
establishes the method.

## 6. What these rulings do NOT do

No finding number is allocated; the series stands at F88. No open-items row is created, flipped or
discarded; [[OI-179]] stays OPEN and GATES. No standing clause is amended; rule (k) / D-546 and
Rulings 6, 7 and 12 of 2026-08-21 are untouched. No `src/` change, no build, no test, no
measurement tool of the analysis, no guard run, nothing archived, moved or deleted. The two owed
dispositions the plan's §2 names remain owed and unrowed. The user's 2026-08-22 direction on
pruning and splitting the governing files into satellites is NOT ruled here; its decision surface
is owed by a later session (the fortieth handover block).

---

*Provenance: Cowork, 2026-08-22, the fortieth session, at tip `64e7d2fd7f`. Every governing
document read from a bridge-staged snapshot with the file tools; the declared tell of this session
is recorded in the fortieth handover block. The user's words, in order put: "approved"; "If we
exclude them ONLY for the pollution measurement - then ok."; "I agree with your recommendation"; "Agree with A.".*

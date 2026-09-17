# CC dispatch — SIZE the evidence-restoration effort. Nothing is analysed, nothing is restored, nothing is decided.

> **Status: ACTIVE DISPATCH, written 2026-08-13 (Cowork), at a verified STOP. Nothing is running.**
>
> **★ `cc_instruction_repair_direction_enumeration.md` IS WITHDRAWN AND MUST NOT BE RUN.** It was
> scoped to this arc, framed the fault as one-directional repair, and would have enumerated a
> narrower population than the one that matters. Its framing is superseded by the rulings at §0a.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_evidence_sizing.md`. Acts dated from the
> clock; **no positional count anywhere**; cite rulings by number, not by date. **`HEAD` is the
> current commit of EVERYTHING and is never used to mean the implementation — say *the code*.**
>
> **★ All standing rules as adopted.** D-253 in every dialect; git object queries by explicit hash
> are the admitted route, the working tree is read with the file tools. Hold-don't-guess. **NO EDIT
> OF ANY KIND — no document, no comment, no row, no register entry, no code. No restoration, no
> analysis, no verdict, no classification of any change as legitimate or not.** D-231 and #8 stand.
> One commit at the end carrying the sizing artifact; `origin` only.

## 0a. THE RULINGS THIS SIZES, taken by the user 2026-08-13

1. **A code-versus-documentation comparison is the AUDIT's work.** Performing it during
   restructuring ran the audit early, on an instrument not yet fit for it. **The fault is timing;
   direction is secondary.**
2. **A DISCREPANCY BETWEEN SPECIFICATION AND CODE IS EVIDENCE, NOT A DEFECT.** Where the two
   disagree we get a chance to evaluate whether either is correct. **Where they agree we learn
   nothing** — agreement is equally consistent with both being right and both being wrong. So a
   correction that brought them into line **destroyed a signal**, and did so selectively, at
   exactly the highest-information sites in the record.
3. **ALL EVIDENCE MUST BE RESTORED**, and the restoration criterion is: **restore if and only if
   the documentation was copied from the implementation.** How to fix is not a user decision.
4. **ANY change must be analysed** — additions, deletions and modifications alike. An addition can
   make a correct specification wrong without removing a word.
5. **The effort is sized first.** This dispatch is that and nothing else.

## 0b. WHAT IS SIZED

**The population: every change to every documentation surface across the restructuring period.**
No exclusion by document role, by change type or by apparent legitimacy — ruling 4 forbids it, and
the writing side has already had three attempted reductions refuted.

**★ THE CLASSIFICATION RULE, given by the user 2026-08-13, and it is what the sizing counts by.**

> **PURE restructuring of documentation is OK** — no knowledge loss, no change, no growth. **Any
> change to documentation that changes actual meaning, design, algorithm or content — regardless of
> how and where it is documented — is probably NOT OK.** *(The user's own words, and he notes there
> are probably exceptions to this soft rule.)*

**Two consequences, and the first is why this dispatch got smaller.** The test is **before-state
against after-state, inside the documentation** — it needs **neither the code nor the change's
recorded reason**. Content identical but rearranged, re-homed, re-titled, split or pointed at is
PURE restructuring. Content different in any direction — **lost, altered, or grown** — is flagged.
**Growth counts**: adding knowledge is not restructuring. And second: **the flag test and the
restoration criterion are different tests at different stages.** Flagging asks *did the content
change*; restoring asks *was it copied from the implementation*. The second applies only to what
the first flags.

**It is a SOFT rule with exceptions. An exception encountered is REPORTED, never decided** — the
sizing surfaces the classes the rule strains against and leaves them to the user.

**Report, per dimension, with the derivation stated:**

1. **The restructuring period's start, ESTABLISHED at the record** — not assumed, and not taken
   from any Cowork statement. If it cannot be established, report the bound that can be, and say
   what would settle it.
2. **Commits touching a documentation surface**, and **changed files** and **changed hunks** within
   them.
3. **A breakdown by document role** — specification-bearing, provenance, derived — **reported and
   NOT used to exclude anything.** State the rule used to assign a role and note that it is
   reported for the user's sight, not applied.
4. **★ THE PRIMARY COUNT: how many changes are PURE RESTRUCTURING and how many CHANGE CONTENT**,
   under the rule above, judged before-state against after-state and **without reading the code or
   the change's reason.** This is the number that sizes the effort.
5. **Of the content-changing set only: for how many does the record STATE the change's ground?** A
   dispatch, a commit body or a report saying why. **This does not affect the flag** — it feeds the
   later restoration test, since *copied from the implementation* is answerable by reading where a
   ground is recorded and needs a code comparison where it is not. Report it for the flagged set
   and not for the whole population.
5. **Edge classes encountered, reported and NOT classified:** stale code locators updated; measured
   baselines re-stamped from runs; banners and filing acts; generated artifacts regenerated
   wholesale. **Do not decide whether any of these count as copied from the implementation** — the
   user has said the criterion is mechanical, and whether these fall inside it is a question the
   sizing surfaces rather than answers.

## 0c. THE PREMISE LEDGER (#17a)

**FACT — verified by Cowork at the objects:** nothing about the population's extent. **Cowork has
looked only at this session's commits, has asserted a proportion it never counted, and has had
three proposed bounds refuted.** Nothing in this dispatch's framing should be treated as
established by the writing side.

**ASSUMPTION — checked before the act resting on it; a refutation is a STOP.**

- **A1.** The period's start is establishable at the record. *Check: if not, STOP and report the
  available bound rather than choosing one.*
- **A2.** A generated artifact's content is recoverable from its inputs, so regeneration loses
  nothing. **This is a claim about EACH generator and is not assumed.** *Check: state it per
  artifact family, or report it as unestablished for that family.*
- **A3.** The sizing publishes **whole or not at all** (D-671). *Check: if capacity runs short,
  name the dimensions covered and state the remainder as untouched.*

## 0d. THE TASKS

**Task 1 — the sizing**, published as a generated artifact under `tools/audit/` with its own
reproduce check, and the derivation of every number stated beside it.

**Task 2 — the close.** One `STATUS.md` pointer entry; the close appended to
`cowork_away_returns.md`. Report at the objects with commit hashes.

## 0e. WHAT IS DELIBERATELY NOT DONE

No change is analysed, classified, judged, restored or reverted. **No opinion is offered on how
large the effort should be, on what is legitimate, or on what should be done** — the sizing exists
so the user can see what the commitment is before making it. No row, no register entry, no discard.
The remaining ratified acts are not started. OI-179 stays OPEN and GATES.

## 0f. STOP RULES

Halt with a STOP if: the period's start cannot be established; a dimension cannot be derived without
judging a change; or the sizing cannot be published whole and its covered dimensions cannot be named.

---

*Provenance: Cowork, 2026-08-13, on the user's rulings above. The error being sized is the writing
side's: it wrote every dispatch that ran a code-versus-documentation comparison during restructuring
and never asked what the audit would then be measuring.*

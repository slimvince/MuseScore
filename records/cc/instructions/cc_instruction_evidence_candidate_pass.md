# CC dispatch — THE CANDIDATE PASS: enumerate every documentation change of the restructuring period and classify each as PURE RESTRUCTURING or CONTENT CHANGE

> **Status: ACTIVE DISPATCH, written 2026-08-13 (Cowork), at a verified STOP. Nothing is running.**
>
> **★ TWO EARLIER DISPATCHES ARE WITHDRAWN AND MUST NOT BE RUN** —
> `cc_instruction_repair_direction_enumeration.md` and `cc_instruction_evidence_sizing.md`. Both
> were built on framings the user has since superseded and both would enumerate too narrowly.
>
> **★ WHAT IS AT STAKE, STATED SO IT GOVERNS EVERY JUDGMENT BELOW.** This pass produces **THE
> CANDIDATE LIST**. A change that should have been flagged and is not will never be looked at
> again: the specification will keep the altered content, the audit will meet no discrepancy there,
> and a wrong algorithm will pass through the audit certified correct. **A missed candidate is not
> a smaller result — it is a silent, permanent loss of the evidence the audit exists to use.**
> **Over-flagging costs review time. Under-flagging costs the objective. They are not comparable,
> and every rule below is written on that asymmetry.**
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_evidence_candidate_pass.md`. Acts dated
> from the clock; **no positional count anywhere**; rulings cited by number, not by date. **`HEAD`
> is the current commit of EVERYTHING and never means the implementation — say *the code*.**
>
> **★ All standing rules as adopted.** D-253 in every dialect; git object queries by explicit hash
> are the admitted route, the working tree is read with the file tools. Hold-don't-guess. **NO EDIT
> OF ANY KIND — no document, comment, row, register entry, tool or code. Nothing is restored,
> reverted, corrected or resolved.** D-231 and #8 stand. One commit carrying the artifact and one
> for the close; `origin` only.

## 0a. THE RULINGS THIS PASS SERVES (user, 2026-08-13)

1. **A code-versus-documentation comparison is the AUDIT's work.** Running it during restructuring
   used an instrument not yet fit for it. **The fault is timing; direction is secondary.**
2. **A DISCREPANCY IS EVIDENCE, NOT A DEFECT.** Where specification and code disagree we get a
   chance to evaluate whether either is correct. **Where they agree we learn nothing** — agreement
   is equally consistent with both being right and both being wrong. A correction that brought them
   into line **destroyed a signal**, selectively, at the highest-information sites in the record.
3. **ALL EVIDENCE MUST BE RESTORED.** The restoration criterion — applied later, not here — is
   **restore if and only if the documentation was copied from the implementation.**
4. **ANY change must be analysed.** Additions, deletions and modifications alike.
5. **The effort is sized first**, and this pass is that sizing **and** the candidate list, because
   the size cannot be known without classifying.

## 0b. THE CLASSIFICATION RULE

**The user's own words, and they govern:**

> **PURE restructuring of documentation is OK** — no knowledge loss, no change, no growth. **Any
> change to documentation that changes actual meaning, design, algorithm or content — regardless of
> how and where it is documented — is probably NOT OK.** *(The user notes there are probably
> exceptions to this soft rule.)*

**The test is before-state against after-state, inside the documentation.** It needs **neither the
code nor the change's recorded reason**. Content identical but rearranged is PURE. Content
different in any direction — **lost, altered, or grown** — is a CONTENT CHANGE. **Growth counts:
adding knowledge is not restructuring.**

### The OK list — recognitions, not a space to reason within

- **Moving content to its owning home**, carried whole.
- **Removing redundancy — ONLY where the removed content survives at its one home** (#6), and only
  where what is collapsed is **recoverable from what is kept** (#12's recomputable clause). *Near
  duplicates usually differ in scope; collapsing them loses the difference.*
- **Removing an inconsistency AFTER RATIFICATION.** Without the ratification a session is deciding
  which of two documents is right, which is a content decision.
- **Language enhancement** under the mechanical language rules — reserved words, qualified
  predicates, defined terms, plain vocabulary. **OK by construction: if the meaning moved, it was
  not a language enhancement.**
- **Re-aiming a drifted pointer or anchor** at the same content.
- **Splitting or merging documents** with content carried whole.
- **Adding a POINTER to content that already exists** — navigation, not knowledge.
- **Recording the document's OWN provenance, ratification or supersession status.**
- **Preserving former wording under #12** as part of an allowed change.
- **An unambiguous transcription slip** — **but NEVER a value**, since a wrong number may be a real
  datum rather than a typo.

### ★ THE LOOK-ALIKES — these are where the damage will be, and each is a CONTENT CHANGE

- **"Clarifying" a rule.** Almost always narrows or widens what it covers.
- **"Removing redundancy"** where the two statements were not in fact identical.
- **Tidying a caveat, a hedge, or a "NOT claimed" clause.** Those carry **exclusion evidence**,
  which #12 says is information.
- **Updating an example to match current behaviour.** That is a code comparison.
- **Re-bannering a document whose body then reads differently in force.**
- **Replacing reasoning with description**, or a measured provenance with a statement of fact.
- **Changing a rule's force** — *must* to *should* — or its scope.

### Worked examples from this arc, which ARE the test rather than illustrations of it

- **CONTENT CHANGE.** The `kHalfDimFirstInversionBonus` paragraph: the stated correction was *which
  block the bonus fires in*, and the edit removed a paragraph carrying **musical reasoning** and a
  **measured provenance** (an iteration and a measured movement). *A narrow stated purpose does not
  make a narrow change.*
- **CONTENT CHANGE.** The draft banners: removing the stale banner was ratified; the same edit
  removed the documents' **provenance and ratification status**.
- **PURE.** Deleting `~L####` code locators, which D-307 forbids citing by in the first place.
- **PURE.** A footer date re-stamp.
- **FLAG, NOT PURE.** A measured baseline re-stamped from a run — the value changed, and whether a
  measurement counts as *copied from the implementation* is the user's question, not CC's.

## 0c. THE FIVE MECHANISMS THAT MAKE THIS STICK

1. **CLASSIFY PER HUNK, NEVER PER COMMIT OR PER FILE.** One commit routinely contains both pure
   restructuring and a content change. A commit-level verdict hides the second inside the first.
2. **THE DEFAULT ON DOUBT IS FLAG.** A change that cannot be placed confidently is **FLAGGED, never
   classified PURE.** Stated as a rule because of §0's asymmetry.
3. **EVERY *PURE* VERDICT CITES THE OK-LIST CLAUSE IT USED, BY NAME.** A verdict that cannot name
   its clause **is not a verdict and becomes a FLAG.** A wrong verdict then traces to a wrong clause
   rather than to judgment.
4. **THE STRETCH STOP.** If you find yourself **arguing** a change into the OK class, that is the
   signal — **flag it.** The OK list is a set of recognitions.
5. **SELF-CLASSIFICATION IS DECLARED.** Where a change being classified was made by an executing
   session under a Cowork dispatch — which is most of this arc — **the record says so per hunk**, so
   the user can weight an author grading their own work.

## 0d. THE POPULATION — and the seven ways it could be incomplete

**Derived mechanically from git, never from a list, and never from anything Cowork has said.**

- **The period's start is ESTABLISHED at the record.** If it cannot be established, **go back
  further, not less** — err early. Report the bound and what would settle it.
- **Include file RENAMES and whole-file DELETIONS.** A document deleted or renamed is invisible to a
  walk over files that currently exist, and is the classic miss.
- **Include files that no longer exist at the current commit.**
- **Detect CROSS-FILE MOVES within a commit** — content leaving one file and arriving in another
  looks like an unrelated deletion and addition. **Judge the pair together, or flag both.**
- **No exclusion by document role.** Ruling 4 forbids it. Report the role; do not filter on it.
- **Generated artifacts are a SEPARATE CLASS, reported and not dropped.** Their recoverability is a
  claim about **each generator** — state it per family or mark it **unestablished** for that family.
- **The ENUMERATION must be published WHOLE even if the CLASSIFICATION is partial** (D-671). A
  partial candidate list that looks complete is the worst outcome available; if capacity runs short,
  publish every member and name exactly which are classified and which are untouched.

## 0e. THE PREMISE LEDGER (#17a)

**FACT established by Cowork: nothing about this population.** Cowork looked only at this session,
asserted a proportion it never counted, and had **three** proposed bounds refuted by the user.
**Nothing in this dispatch's framing is evidence.**

**ASSUMPTION — checked before the act resting on it; a refutation is a STOP.**

- **A1.** The period's start is establishable. *If not, STOP and report the available bound.*
- **A2.** Rename and cross-file-move detection actually runs. *Check: demonstrate it found at least
  one, or establish that none exists in the population.*
- **A3.** A generated artifact's content is recoverable from its inputs. **Per generator, not
  blanket.** *Mark unestablished where it cannot be shown.*
- **A4.** Every hunk receives a verdict. *Check: hunks enumerated equals hunks classified plus hunks
  explicitly named untouched. **A hunk that fell out of the count is the failure this pass exists to
  prevent.***

## 0f. THE TASKS

**Task 1 — the enumeration**, published whole, as a generated artifact under `tools/audit/` with its
own reproduce check.

**Task 2 — the classification**, per hunk, under §0b and §0c, into the same artifact: verdict, the
clause cited for every PURE, the self-classification marker, and the role of the document.
**Report the FLAGGED set prominently and separately — that is the candidate list.**

**Task 3 — the close.** One `STATUS.md` pointer entry per task; the close appended to
`cowork_away_returns.md`. Report at the objects with commit hashes, and report **A2's and A4's
findings explicitly**.

## 0g. WHAT IS DELIBERATELY NOT DONE

Nothing is restored, reverted, corrected or resolved. **No change is judged legitimate or
illegitimate** — PURE and CONTENT CHANGE are descriptions of what the edit did, not verdicts on
whether it should have happened. **No comparison against the code**, in either direction, for any
purpose. No opinion on the effort's size beyond what the count states. No row, no register entry, no
discard. OI-179 stays OPEN and GATES.

## 0h. STOP RULES

Halt with a STOP if: the period's start cannot be established; rename or cross-file-move detection
cannot be made to run; a hunk cannot be given a verdict and FLAG would misdescribe it; the
enumeration cannot be published whole; or you find yourself arguing a change into the OK class and
the stretch stop does not resolve it.

---

*Provenance: Cowork, 2026-08-13, on the user's rulings. The error being sized is the writing side's:
it wrote every dispatch that ran a code-versus-documentation comparison during restructuring and
never asked what the audit would then be measuring.*

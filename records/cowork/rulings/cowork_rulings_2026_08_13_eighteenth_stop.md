# User rulings — 2026-08-13, the eighteenth stop: the restructuring phase was running the AUDIT early, and what follows from that

> **STATUS: RULING RECORD, an interim carrier (D-230).** Taken by the user in conversation on
> 2026-08-13, across a long exchange in which the user corrected the writing side repeatedly. **The
> classification of each ruling — decision or exercise — is OWED and not made here**, and the
> decisions register's own future is one of the things ruled on below, so the usual queue route may
> not survive.
>
> **★ THIS RECORD EXISTS BECAUSE ALMOST NOTHING BELOW WAS ON DISK.** A session inheriting the
> repository without it would resume the superseded plan, because the repository still describes
> that plan — including D-231's truth half, which is still live in a mandatory session-start read.

## 1. The diagnosis the rulings rest on

**A code-versus-documentation comparison is what the AUDIT does.** This arc performed those
comparisons during **restructuring** — so the audit ran early, out of sequence, against an
instrument not yet fit for it. **The fault is TIMING. Direction is secondary**, and it holds however
carefully each act was performed.

**A DISCREPANCY BETWEEN SPECIFICATION AND CODE IS EVIDENCE, NOT A DEFECT.** Where the two disagree
we get a chance to evaluate whether either is correct. **Where they agree we learn nothing** —
agreement is equally consistent with both being right and both being wrong. So each correction that
brought them into line **destroyed a signal**, selectively, at the highest-information sites in the
record.

**If specifications are amended to match the implementation, the audit is worth nothing** — worse,
it returns a **false clean result** carrying the authority of a completed audit, and a wrong
algorithm passes through certified correct. The record already forbids this shape one surface over:
gate block (A)'s conventions bar self-annotation from ever being a standard of correctness.

**And the specification may be perfectly restructured and still wholly wrong.** Restructuring is not
correcting.

## 2. The rulings

1. **RESTRUCTURING IS NOT CORRECTING.** Its output is documentation that is internally consistent,
   findable and one-home-per-concern — **an instrument fit to audit with.** It may be internally
   perfect and still wrong about the world and wholly at odds with the code. **The audit that
   follows is an audit OF THE CODE, with the documentation as the instrument**, and it is
   **two-directional**: code wrong, specification wrong, both wrong, both right differently, or
   something missing entirely.
2. **THE CLASSIFICATION RULE, in the user's words.** *PURE restructuring of documentation is OK — no
   knowledge loss, no change, no growth. Any change to documentation that changes actual meaning,
   design, algorithm or content — regardless of how and where it is documented — is probably NOT
   OK.* **A soft rule with exceptions; an exception is reported, never decided.**
3. **ALSO OK:** removing redundancy — **only where the removed content survives at its one home**
   and what is collapsed is recoverable; removing an inconsistency **after ratification**; and
   **language enhancements** under the mechanical language rules, which are OK by construction
   because if the meaning moved it was not one.
4. **ANY CHANGE MUST BE ANALYSED** — additions, deletions and modifications alike. **An addition can
   make a correct specification wrong without removing a word.**
5. **ALL EVIDENCE MUST BE RESTORED.** The restoration test is **not *copied from the
   implementation*** — that is useless, since nobody pasted code into a specification. It is
   **whether any fact in the code influenced the change**. Influence is **invisible in the text**: a
   narrowed rule reads exactly like a rule that was always narrow.
6. **D-231 MUST BE REPHRASED OR REMOVED.** Its truth half is the instruction that caused this and it
   is live in a mandatory read.
7. **NEW PHASES MUST BE DEFINED**, from the ultimate objective, from what restructuring means as
   ruled at (1), and from when and what the audit is. The existing phases conflate restructuring
   with truth-sync.
8. **THE DECISIONS REGISTER IS FILTERED, NOT WHOLESALE RETIRED.** Soft-discard — retired from the
   live record, not destroyed — only those entries where **no deciding act can be named**. *A
   decision ABOUT the code is legitimate; what is not a decision is an observation of what the code
   does, recorded as though it had been decided.* **Note the register's origin:
   `cc_instruction_decision_harvest.md` lists production code comments as a harvest source**, so
   this class exists by construction.
9. **THE `src/` COMMENT EDITS ARE MARKED, NOT REVERTED** — the correction stays, with a note that it
   was made during restructuring by a comparison that should not have happened, and is unsettled
   until the audit. *Reverting would restore comments describing a mechanism the code does not have,
   which creates no evidence because a code comment is not the independent side of the audit.*
10. **THE REPAIR IS RECONCILIATION, NOT ROLLBACK — pending a pilot.** Compare the pre-pollution
    baseline against the current text and write a coherent new version, fixing the pointers in other
    documents as part of the act. *It is robust to a wrong start date, where a rollback is not; and
    it lets the test change from provenance, which is invisible, to CHARACTER, which is visible —
    **does this text express a design intent, or describe an implementation?***
11. **THE PILOT ESTABLISHES THE METHOD BEFORE IT IS TRUSTED (#19).** One file, and the deliverable
    is a **proposal per difference**, never a silent rewrite by the side that wrote the text.
12. **SIZE THE PROBLEM AND ITS DOWNSTREAM EFFECTS EVEN WHERE THERE IS NO ALTERNATIVE** — the size
    decides sequencing and whose time is needed when.
13. **OPEN ITEMS:** rows affected by pollution are **marked as needing re-evaluation** and triaged
    **after** the reconciliation, because validity cannot be judged before it. Rows **closed on a
    contaminated act reopen** with provenance. **No new status token** — the state stays open and
    the property is a derived field, the shape the record settled for DISCARDED.
14. **`HEAD` IS NEVER USED TO MEAN THE IMPLEMENTATION**, and **licence** joins the reserved-word
    cleanup list — in this project it collides with real corpus and distribution rights. Say **a
    ruling from you permitting a named act**.
15. **THE WRITING SIDE READS CC's FULL CLOSE**, not the summary, and **proves it** by quoting
    something from the close that was not in the summary.

## 3. What is NOT ruled, and must not be assumed

**No repair is authorized.** Nothing is reverted, restored, reconciled or marked yet. **The phases
are not defined.** **D-231 is not yet rephrased.** **No file has been chosen for the pilot** beyond
`docs/scoring_model.md` being the writing side's recommendation, on the grounds that it took the
arc's largest single change, is a mandatory read, and contains a **known loss** usable as an
unstated seed. **The register filter is not run.** **No open-items row has been marked or reopened.**

*Provenance: Cowork, 2026-08-13. Every ruling above was taken in conversation after the writing side
put an alternative that the user refuted — the record of those refutations is the conversation, and
the grounds are restated here because the conversation does not survive the session.*

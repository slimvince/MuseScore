# The specification-versus-code audit: how a gap is CLASSIFIED and what may ADJUDICATE it

> **STATUS: COWORK READING SURFACE for phase 2, landed 2026-08-11 at a verified STOP on the
> user's direction ("make sure the above thinking makes it into phase 2"). NOT ratified, NOT a
> specification, NOT an authorization.** Phase 1 is open and D-231's order stands; nothing here
> commissions an audit, licenses a probe, or permits a fix. It fixes the METHOD before the audit
> runs, for the same reason a premise is written before the measurement rather than during it
> (#17b).
>
> **★ ITS POINTER LIVES AT `cowork_audit_protocol.md` P3 — "Audit the negative space (spec→code,
> not only code→intuition)"** — this audit's own section, as a one-line pointer naming this file
> and its unratified status (#6 — a pointer, never a copy). Without that pointer a phase-2
> session will not find it.
>
> **Why this passes the worth test #10 now carries.** Leaving the method unwritten risks an audit
> that adjudicates by judgment, and a judgment made inside a fact-gathering act produces wrong
> fixes to the inferrer — limb (a) of the test.

## 1. The problem, in the user's own framing

*"If and only if the specs are 100% complete and correct we know that the code needs fixing.
However, we do not know if specs are 100% complete and correct — so the gaps we find could be any
of: both correct in different ways, both incorrect, code correct or spec correct."*

That is the trap exactly. **The audit's output is actionable only to the degree the specification
is established**, and #19 says a thing is trusted only when positively established. A gap, on its
own, is evidence that two descriptions differ and nothing more, until something outside both of
them decides.

## 2. What a gap can be — seven classes, not four

The user's four stand. Three are added because the record has already produced each, and each has
a DIFFERENT resolution, which is why they are separated rather than lumped.

1. **The specification is correct, the code is wrong.** The fix is in the code, at its own layer.
2. **The code is correct, the specification is wrong.** The fix is D-231's doc-sync half.
3. **Both are wrong.** A design act; it belongs to phase 3.
4. **Both are correct, in different ways** — two defensible readings of one intent.
5. **★ THE SPECIFICATION IS SILENT.** Not incorrect — absent. The code does something nobody
   decided. **Not a doc-sync gap**, and its resolution differs in kind: either the rule is written
   from the code as a decision now taken, or it is admitted that the rule was never made and it
   becomes a phase-3 design question. *Evidence it is real and large:* the record already names
   candidate admission with no ratified basis, the notation-bridge constants, the hand-set
   constant mass, the fit manifest read by no code, and several duplicated tables. **In this
   repository this is expected to be the largest class**, and the *obvious from ratified
   decisions* test cannot touch it, because there is no ratified decision to consult.
6. **★ BOTH CORRECT, ABOUT DIFFERENT ARMS.** The legacy arm is compiled and dormant beside the
   joint arm, so a statement can be accurate about one and false about the other. *Measured
   instance, 2026-08-11:* a mechanism report was accurate about the dormant path while the arm it
   described had stopped shipping two weeks after it was written.
7. **★ THE GAP IS ILLUSORY.** Specification and code describing different granularities or
   different layers, so there is no disagreement — only a reading error. This class produces the
   most confident wrong conclusions per instance.

## 3. What may ADJUDICATE a gap — three standards, whose authority is the principles

**These three are the audit's whole authority. Nothing else adjudicates.**

- **A ratified decision that reached the specification — #14.** Where a ratified decision states
  the rule, the specification carries the authority and the code is what moves. *This is the class
  expected to be obvious, and the record supports that:* the struck-versus-sounding family was
  obvious the moment it was seen, because the specification says *per tone* and *each event's
  sounding bass* while the implementation walks onset-only tones, and the specification side is
  ratified.
- **A public algorithm or published research we decided to use — #1 and #2**, subject to the
  theory-grounding corollary: the source must have been fetched and read, and a claim from an
  unfetched source is an assumption wearing a citation.
- **★ THE MUSIC ITSELF.** Where a gap reduces to a musical fact, neither document decides and the
  score does. *Instance:* a reading was closed by observing that the sounding D♯–F♯–B is a B-major
  triad and the prior reading named a chord the notes do not contain. Where this standard applies
  it is not contestable, and it is reached for first because it is the cheapest.

## 4. ★ "NOT ADJUDICABLE" IS A FIRST-CLASS OUTCOME

Where none of the three decides — no ratified decision, no published algorithm, no musical fact,
just two plausible readings — **the gap is not adjudicable by the audit; the audit records it as
such and moves on.**

*Why this is load-bearing rather than a caveat:* without it every hard gap is resolved by the
auditor's judgment, and a judgment made inside a fact-gathering act is precisely what #8 and D-231
forbid — it converts an audit into a design exercise while phase 1 is still open. **The behaviour
already exists as a demonstrated model:** the 2026-08-11 re-pin met five analogies between a
pinned mechanism and a shipping one and **ruled none of them**, reporting each as an analogy.

## 5. ★ SORT BEFORE ADJUDICATING, AND ASK THE ARM QUESTION FIRST

**Two passes, in this order, because doing them together is what produces false gaps.**

**First, per gap: which arm is each statement about?** Until the legacy arm is deleted, a gap
unresolved for arm produces false gaps and false agreements in equal measure. Cheap, and asked
before anything else.

**Then sort, before looking at any gap's merits: does a ratified decision or a public algorithm
exist for this rule, or is the specification silent?** The first set is the audit proper and is
largely mechanical. **The second set is not an audit at all — it is the inventory of decisions
never taken**, and it feeds phase 3 rather than producing fixes. Sorting first keeps the audit's
size honest and stops the silent class being adjudicated as though a standard existed for it.

## 6. What this surface does NOT do

It commissions no audit, authorizes no probe, permits no fix and proposes no design. It moves no
row and proposes no ruling. It touches no measured value, no golden, no corpus of scores and
nothing under `tools/robust_stop/`. It is not a specification and is not ratified; **phase 1 is
open and D-231's order is untouched.** It does not claim the seven classes are exhaustive — it
claims each has occurred, and an eighth found during the audit is a finding, not a failure of this
file.

*Provenance: Cowork, 2026-08-11, from the user's own framing of the adjudication problem, with the
three added classes and the three standards each grounded in an instance the record already
carries.*

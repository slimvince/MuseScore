# The perspective inventory — put to the user for ratification

> **★ STATUS: RULED AND APPLIED (user, 2026-08-03) — SUPERSEDED BY ITS OWN EXECUTION.** The user
> read §5 below and ruled **option (c) with option (b)'s correction folded in**: amend the scope,
> correct channel 9, then ratify — because channel 9 is both the scope gap of §4(a) and the stale
> statement of §4(b), and ruling its scope while its own text said the work was finished would have
> ratified a contradiction. Applied at phase 1v (dispatch
> `cc_instruction_phase1v_channel_ratification.md`); register entry **D-439**; the row it closed is
> `OPEN_ITEMS.md` OI-298. **Nothing here is pending.** The §7 act list below was executed in full,
> in that order, plus the scope ruling §5(c) asked for.
>
> **What the ruling did NOT decide, because §6 below promises it:** the inventory's §6 program is
> NOT adopted, in whole or in part; OI-200 is not pulled forward and the inventory's own §9 request
> stays open and untaken; no probe, fix, design or inference change is authorized; phase 1 is not
> complete.
>
> **Retained unedited beneath, under #12** — a ruling is only readable against the surface it
> answered (**D-249**). In particular §1 and §4(a) below describe `CLAUDE.md`'s phase-2 clause as
> naming six subjects in a parenthesis: that was true when this surface was written and is what the
> user read; the ruling is what changed it.
>
> *Drafted as:* **STATUS: AWAITING THE USER.** Nothing here is applied. This is the reading surface
> for one
> decision: whether `cowork_oi200_perspective_inventory.md` becomes the ONE home for the discovery
> channels that `CLAUDE.md`'s phase-2 clause relies on. Prepared 2026-08-03 (CC, phase 1u, Task 2)
> on the user's ruling of the same date (option 2B: *the inventory becomes the one home and is
> ratified; the clause points at it*). **The clause has NOT been changed** — pointing a binding rule
> at content the user has not ratified is the defect this ruling exists to close, and changing the
> clause before the ratification would re-commit that defect in a new form.

---

## 1. What is being decided

`CLAUDE.md`'s phase-2 clause — the user-directed three-phase rule, register entry **D-231** — says
issue-finding is exhausted through *"the enumerated discovery channels"* and then names six subjects
in a parenthesis: populations, oracles, invariants, residual decomposition, concept gaps,
requirement side.

**The only place in the record where those channels are actually enumerated is
`cowork_oi200_perspective_inventory.md`.** That document's own status banner reads *"STATUS: DRAFT
for discussion (Cowork, 2026-08-01)"*, and its §9 records that its one requested decision — adopt,
amend or reject its proposed program — has not been taken.

So a binding rule leans on an unratified draft. The decision asked for here is whether that draft
becomes the home the rule may lean on.

## 2. Why it is asked now rather than at OI-200's turn

The document was written as an input to the architecture step-back (`OPEN_ITEMS.md` OI-200), whose
scheduled turn is later. Two things have happened since that make the ratification owed earlier:

- **The rule started pointing at it.** D-231 was ruled on 2026-08-02 and names *"the enumerated
  discovery channels"* as a phase gate. Before that, the inventory was a proposal nothing depended
  on; now the completeness of phase 2 is defined partly by it.
- **The phase-3 gate partition classifies against it.** Every item of
  `tools/audit/phase3_gate_partition.json` is a channel or an audit item, and the partition had to
  state, in its own `the_channel_enumeration_source.status_of_this_source`, that its structural
  source is a draft — carrying the caveat forward rather than resolving it. Each verdict there is
  therefore stated against the SUBJECT the rule names, with the draft's channel number used as a
  locator only. That is a workaround, and it is the one this ratification would retire.

**The ratification does not pull OI-200 forward.** What is asked is whether the ENUMERATION is the
one of record — not whether the §6 program runs now, nor in what order.

## 3. What the document is

`cowork_oi200_perspective_inventory.md`, ~337 lines. Its substance:

- **§2** states exactly what is and is not possible about unknown unknowns: they cannot be searched
  for by content, so what can be done is (a) vary the things that generate observations and (b)
  measure how much each search misses.
- **§3** is the honest inventory of how this project's genuinely unanticipated findings were
  actually found, each with a citation — a new input population, an independent reference
  disagreeing, a stated prediction missing its band, a field report, a challenge to a defended
  premise, history re-read. It also states what has NOT produced such findings.
- **§4** is the enumeration itself: ten channels, each with what is varied, why it can catch what
  nothing else catches, a precedent from this repository's own findings, and proposed probes.
- **§5** is how ignorance gets bounded without being enumerated — seeded detection power per
  method, sealed-finding reconciliation, coverage accounting per channel.
- **§6** sequences a proposed program; **§7** considers three alternatives; **§8** cites the
  external sources (metamorphic testing; the fault-seeding literature).

## 4. What a reader should check, including what this session found wrong in it

**(a) The rule names six subjects; the inventory has ten channels.** The four the rule does not name
are 4 (prediction-first operation), 8 (fresh-reader passes), 9 (history mining) and 10
(defect-signature sweeps). They are not padding, and they do not all behave alike — the per-channel
reading is recorded at `tools/audit/phase3_gate_partition.json` →
`assumption_A1_of_the_phase1u_dispatch.findings`, which was produced by reading the inventory in
full against the rule's own clause. **The short version: channel 4 is not a distinct search at all
(the inventory says so of it), channel 8 is the audit passes the rule already names under other
words, and channels 9 and 10 are distinct searches the rule names nowhere.** Ratifying the inventory
as the home settles what the clause reaches; leaving it unratified leaves that open.

**(b) One statement in it is not true at HEAD, and ratifying it as drafted would ratify that.**
Channel 9 says of history mining: *"Proposed probe: none new — the adjudication is this channel run
to completion."* The OI-207 adjudication is **not** run to completion. Its residual second pass ran
on 2026-08-02, and both of its faces are still live: the unresolved cluster residual is a current
figure at `tools/audit/decisions/disposition_manifest.json` → `disposition_counts.unresolved`, and
the owed full document reads are tracked on the OI-207 row itself. This is flagged rather than
silently corrected, because correcting a document while presenting it for ratification changes what
is being ratified.

**(c) It is a methodology surface, not a component design**, and says so in its own banner — the
fourteen-section component structure applies only where it maps. That is a stated omission, not a
gap found here.

**(d) It decides nothing about the system.** No inference behaviour, no gate, no threshold, no
corpus. What it would fix is which searches phase 2 consists of.

## 5. The options

- **(a) RATIFY AS DRAFTED, with the §4 enumeration as the one home; correct (b) above as a separate
  dated act.** *For:* it closes the gap the phase-2 clause has been carrying since 2026-08-02, and
  it is the narrowest act that does so — the ten channels become the enumeration of record, and the
  clause's six subjects stop being an under-naming of a list nobody has approved. Keeping the
  correction separate preserves what was ratified as a readable thing (**D-249**: a ruling is only
  readable against the surface it answered). *Against:* it ratifies a document with one known stale
  statement in it, even if the correction follows immediately.

- **(b) RATIFY WITH THE CHANNEL-9 CORRECTION APPLIED FIRST**, then point the clause at the corrected
  text. *For:* nothing false is ratified. *Against:* the surface put to the user and the surface
  ratified differ, which is the shape D-249 warns about; and the correction is to a description of
  scheduling, not to any channel's content.

- **(c) AMEND THE SCOPE BEFORE RATIFYING** — rule which of channels 4, 8, 9 and 10 the phase-2
  clause reaches, and ratify the enumeration with that answer written in. *For:* it answers (a)
  above rather than deferring it, and the phase-3 gate partition's channel verdicts would then rest
  on a ratified structure rather than on a subject-by-subject reading. *Against:* it is a larger
  decision than the one this surface was built for, and it touches what phase 2 must contain.

- **(d) REJECT — do not make it the home**, and instead write the enumeration into `CLAUDE.md` or
  into a specification directly. *For:* the rule and its enumeration would live in one place.
  *Against:* it duplicates a document that already exists and is good (**#6**), and it would put a
  methodology enumeration in a file that carries standing rules rather than method.

**Recommendation: (a).** It is the smallest act that stops a binding rule leaning on an unratified
draft; the one stale statement is about scheduling rather than about any channel's content, and
keeping its correction as a separate dated act keeps the ratified surface readable. Option (c) is
the one worth considering instead if the channel-scope question in §4(a) is felt to be the real
decision — it is a genuine question and this surface does not answer it.

## 6. What ratification would and would not do

**Would:** make `cowork_oi200_perspective_inventory.md` §4 the one home for the enumerated discovery
channels; let `CLAUDE.md`'s phase-2 clause POINT at it instead of listing six subjects (**#6** — the
list stops being a second, shorter enumeration); and retire the caveat the phase-3 gate partition
currently carries about its structural source.

**Would not:** adopt the §6 program or its sequence; schedule OI-200; authorize any probe, any fix,
any design or any inference change; or complete phase 1.

## 7. The act that follows a ratification

One commit: the inventory's banner flipped from DRAFT to its ratified state with the date and the
ruling; `CLAUDE.md`'s phase-2 clause changed from listing six subjects to pointing at the
inventory's §4 (**a change to a user-directed rule, so it is made only on this ratification**); the
register gains the entry; `tools/audit/gen_phase3_gate_partition.py`'s
`status_of_this_source` block updated and the artifact regenerated; and the row opened for this gap
flipped.

*Provenance: prepared 2026-08-03 at `cc_instruction_phase1u_partition_record_and_directory.md`,
Task 2, on the user's ruling AA2 of the same date. The gap this surface exists to close is tracked
at `OPEN_ITEMS.md` OI-298. Cross-ref `OPEN_ITEMS.md` OI-200 (the inventory's home row), OI-207
(the adjudication §4(b) is about), and `tools/audit/phase3_gate_partition.json` (the partition that
classifies against this enumeration).*

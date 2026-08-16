# The soft-discard's reach — what performing the ruled discard is allowed to touch beyond the decisions register, proposed for ruling

> **STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED AND NOTHING IS EXECUTED.**
> Drafted by the writing side on 2026-08-16 at the third preparation batch's STOP (finding F13 of
> `cc_report_preparation_third.md`). This file is on disk and uncommitted; the next batch's Task 0
> lands it, together with the twentieth handoff block, on the standing pattern. Per the standing
> presentation rule (`cowork_rulings_2026_08_15_batch_return.md` §5) every identifier used below
> is re-explained from scratch in §0 before any question rests on it. Per the standing
> alternatives rule, every alternative is presented in full prose, each cost and benefit naming
> its principle, each rated against the ultimate objective — as precise inference as possible.
>
> **What this surface decides and what it does not.** The soft-discard itself is RULED
> (`cowork_rulings_2026_08_16_preparation_return.md` §3) and is NOT re-decided here. What is put
> here is the question that STOP-reported batch returned: **what performing that ruled discard is
> allowed to REACH** — because the measurement showed the act's reach is wider than the
> decisions-register family the dispatch had assumed.

## 0. The referents, re-explained from scratch (read this section first)

- **The decisions register** — the project's record of WHAT WAS DECIDED about how this system
  works and whether each decision still stands. Its data file
  (`tools/audit/decisions/backbone_decisions.json`) is the only surface ever edited; the INDEX
  `DECISIONS.md` and the group files `decisions/group_*.md` are rendered from it.
- **The soft-discard** — the ruled act this surface is about: 165 register entries (the 194 for
  which no deciding act could be found, minus the 29 the sole-carrier guard withheld) are moved
  whole into a retired block of the data file — retired from the live record, **not destroyed**
  (#12), each individually revivable the moment a deciding act is later named. The live record
  would go 677 → 512 entries. Every retired record carries the user's own clause verbatim: *"a
  provenance verdict, not a judgment on soundness or usefulness; the statement stands at its home
  and is met by the derivation."*
- **The guard set** — the collection of derived checks (`gen_guard_state.py` runs them) that
  re-derive the project's committed artifacts and STOP on drift. It already distinguishes a
  **HISTORICAL class** beside the live checks — the current guard state reports ten historical
  records (`cc_report_preparation_third.md` §7). The precise reclassification mechanics are not
  restated here; the executing dispatch states them from the guard mechanism's own records, and
  a historical classification that the mechanism cannot express is a STOP, not an improvisation.
- **The superseded three-phase structure and "phase 1"** — until 2026-08-15 the governing
  structure was three phases (D-231), whose phase 1 made the specifications complete and true.
  On 2026-08-15 the user ruled the SIX-PHASE structure (preparation → pilot → framework → detail
  specifications → measurement design → audit), D-231 was rephrased in place, and the old
  structure is superseded (`cowork_rulings_2026_08_15_phase_definition_sitting.md` §2, §4). The
  six phases are what governs now; the preparation phase is open and mid-flight.
- **The old phase-1 gate derivations** — measurement tools that DERIVE the superseded phase 1's
  gate: `gen_phase1_completion_inventory.py` (what phase 1 still owed) and
  `gen_phase1_finish_line.py` (the scope of phase 1's completion), plus the delegation-grading
  derivation they and several sibling checks import. **D-436** reserves to the user what these
  derived cuts carry — a gating verdict comes from a cut and is never hand-added or hand-removed.
- **An authored judgment table** — a committed artifact whose verdicts were written by judgment
  (and ratified or accepted), not derived: the `CLAUDE.md` rule triage, the home classification's
  authored halves, the delegation bar's FORM judgments. A derived check re-verifies these tables
  against the record; it cannot re-author them.
- **A home** — the document (or section) where a decision's verbatim text lives. The register
  points at homes; several checks verify every home still resolves.
- **The §9 precedent** — the one prior ruling on this shape
  (`cowork_rulings_2026_08_15_phase_definition_sitting.md` §9): when landing the ruled D-231
  edit turned six checks red, the user permitted the four non-anchor artifacts to be regenerated
  alongside, **bounded to zero movement in any verdict, gate, cut or population field** — a
  ruling permitting a named act, under D-436, for that act alone.

## 1. What happened, and what is being decided

The third preparation batch derived the ruled soft-discard, applied it to the working tree,
measured the whole guard set at the edited tree, and **REVERTED** (every touched file proven
byte-identical to its committed blob by hashing both sides). The dispatch's assumption A3 — *"the
mutation's reach is the register family and its derived views ONLY"* — was **falsified by that
measurement**: fourteen checks turned red where one expected class was, and the reds are not
confined to the decisions-register family. The dispatch's own instruction for that outcome was a
STOP-and-report, and the batch obeyed it. Nothing was discarded; the derivation, the arithmetic
(194 = 29 withheld + 165 to retire, to the digit) and the committed plan
(`tools/audit/soft_discard_application.json`) all stand ready.

**So the question before the user is the REACH:** which artifacts beyond the decisions-register
family the discard-executing dispatch is authorized to touch, and under what bounds. Until that
is ruled, the ruled discard cannot be performed inside any honest dispatch.

## 2. The measured reach, cause by cause (FACT — quoted from `cc_report_preparation_third.md` §4.c)

**Cause 1 — the superseded phase-1 gate derivations HALT rather than drift.** Every entry homed
in `cowork_structural_integrity_audit.md` is in the discard population, so after the discard that
document stops being graded class C — and the delegation-grading derivation refuses to run
(*"STOP: authored draft for a document that is not class C"*). The checks reporting that same
STOP halt with it, among them **both old phase-1 gate derivations D-436 reserves** (the
completion inventory and the finish line) and the delegation-family siblings
(`gen_outstanding_delegations.py`, `gen_finish_line_item1_routes.py`,
`gen_item1_rehome_blocker.py`, `gen_r1_superseded_reach.py`). They do not go stale; they **stop
being derivable at all** — the superseded phase-1 gate is load-bearing on entries nobody decided.

**Cause 2 — authored judgment tables lose their subjects.** Three documents
(`cowork_layer2_slicing_design.md`, `cowork_phase2_architecture_review.md`,
`cowork_types_header_design.md`) stop being anybody's home, so the home classification and the
delegation bar carry authored judgments *"for a document that is nobody's home"*; the `CLAUDE.md`
rule triage carries an authored entry for D-192, a rule the retirement removes from the live
record; and the artifact-inventory ruling surface and the retirement caller-check stop
re-deriving. Clearing any of these means **re-authoring judgments** the third dispatch did not
authorize.

**Cause 3 (F15) — the decisions register's own generator is one of its own homes.** Inserting
the retired block's STOPs into `gen_decisions_register.py` moves an entry's anchored verbatim
from line 514 to 576, halting the legacy verification — teaching the mechanism about the retired
block is itself a change to a home document.

Only the anticipated class — the register-consuming checks that clear by regeneration
(`gen_decisions_filter.py`, `gen_deciding_act_recovery.py`) — behaved as the dispatch expected.

## 3. Why the §9 route does not discharge this

The §9 precedent permitted regeneration alongside a ruled edit **bounded to zero verdict
movement** — the measured cost there was one quote field, one inherited copy, one new mention,
one live-list entry, and nothing moved in any verdict, gate, cut or population. Here that bound
**cannot hold as a matter of arithmetic**: the discard's whole point is that verdicts move (165
entries leave the live record; a document whose only homed entries are all in that population
stops being a contract home; D-192's triage entry loses its subject). And for cause 1 there is
nothing to regenerate — the derivations STOP by their own design. So the reach needs its own
ruling, not a reuse of §9's; what §9 supplies is the FORM (a ruling permitting a named act,
under D-436, with a bound that travels with it), and this surface proposes that form at the
width this act actually needs.

## 4. The writing side's premise ledger for this surface

- **FACT** — fourteen reds, three causes, the quoted runner output: `cc_report_preparation_third.md`
  §4.c, verified by the writing side against the batch's full close before the twentieth handoff
  block was written.
- **FACT** — the discard arithmetic and the committed plan: report §4.b;
  `tools/audit/soft_discard_application.json`.
- **FACT** — the six phases govern and the three-phase structure is superseded:
  `cowork_rulings_2026_08_15_phase_definition_sitting.md` §2, §4; the ruled definitions' one home
  is `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3.
- **FACT** — the guard set carries a historical class today (ten historical records at the
  batch's end state): report §7.
- **FACT** — the mechanism work the act needs (the retired block's own STOPs in the renderer;
  the establishment pass consulting the retired block beside the live entries) is written and
  measured working — `--verify` passing at 512/512 with 33 surviving cross-references resolved
  against the retired block — and was reverted with the rest: report §4.d.
- **ASSUMPTION R1** — no LIVE consumer outside the superseded phase-1 program reads the old
  phase-1 gate artifacts (the completion inventory, the finish line, the delegation family's
  outputs). The preparation phase's ruled definition does not name them; the twentieth handoff
  block does not name them as live. **Check ordered (any alternative below that retires or
  freezes them):** the executing dispatch enumerates every reader of those artifacts at the
  current commit; a live consumer outside the superseded program is a STOP-and-report.
- **ASSUMPTION R2** — the affected checks are classifiable by derivation into "serves only the
  superseded phase-1 gate" versus "serves a standing rule of the current record". **Check
  ordered:** the classification is derived and published with per-member evidence (each check's
  imports and its own stated purpose); a member the derivation cannot place STOPS to the user
  rather than being guessed — the same shape the caller-kind ruling took for callers.

## 5. The alternatives, each rated against the principles and the ultimate objective

**Alternative A (recommended) — the superseded phase-1 apparatus follows its phase into
HISTORICAL status; the standing apparatus is regenerated under an enumerated-movement bound; the
mechanism edits land with the discard.** Three limbs, stated fully in §6. In one sentence each:
the checks that exist only to derive the superseded phase 1's gate are reclassified into the
guard set's existing historical class, their committed artifacts frozen as record; the standing
apparatus with authored halves is updated alongside the discard under the bound that movement is
permitted ONLY where the moved value's subject is a discard-population entry or a document whose
home standing those entries carried, every movement enumerated in the close; the
already-measured mechanism work lands with the discard commit, F15's anchored-quote movement
handled under the ordinary per-citation drift discipline.

- *For, on the principles.* The six-phase ruling already superseded the program those checks
  grade — keeping the superseded gate derivable forever would let a closed phase's apparatus
  permanently constrain the live record, which is the inversion the apparatus-lapse ruling
  (Ruling 66) closed at the open-items register: apparatus generating its own obligation stream.
  Historical status is the guard set's EXISTING mechanism, not an invention (#6). Nothing is
  destroyed: the artifacts freeze in place, the pre-discard derivation state stands at the git
  objects, and reviving a discarded entry revives its consumers' inputs with it (#12). The
  enumerated-movement bound keeps every authored-table change visible and challengeable (#15 —
  verify at the objects, winner and carry). D-436 is honored, not bypassed: this surface IS the
  user ruling that the reserved derivations' fate requires.
- *For, on the ultimate objective.* The preparation phase's outputs feed the derivation that
  rebuilds the specifications the audit will measure the code against. Every session the 165
  undecided entries stay live, they cost reading time and can mislead a deriving session — the
  user's own pruning direction names exactly this. A unblocks the ruled discard at the smallest
  authorized reach and returns capacity to the phase.
- *Against, stated honestly.* Historical status forecloses cheap regeneration of the old phase-1
  gate: if the user later wants the superseded phase 1's completion measured, the route is
  reviving the relevant entries and re-deriving — dearer than today. (What softens it: the
  completion statement was never commissioned, the finish line's last derivable state stays
  frozen on disk, and R1's ordered check catches any live consumer before anything freezes.) And
  the enumerated-movement bound is weaker than §9's zero-movement bound — necessarily, since the
  act's whole purpose is movement — so more rests on the enumeration being read at the close
  (#15 is the mitigation, not a discharge).

**Alternative B — re-author the affected apparatus so everything re-derives after the discard.**
Regenerate all fourteen checks' inputs: write new authored drafts for the delegation grading
that accept the post-discard document classes, re-author the home classification's and rule
triage's affected entries, and keep the old phase-1 gate derivable over the shrunken record.

- *For.* The guard set returns to all-green with no historical reclassification; the phase-1
  gate stays measurable without revival work; no reader ever meets a frozen artifact.
- *Against, on the principles and the objective.* The authored halves' subjects are GONE — what
  this alternative calls regeneration is new judgment work authored for a superseded program,
  which is precisely the capacity sink the lapse ruling closed (#4: capacity is this arc's
  measured scarcest resource; the recorded ground: the findings that bear on the objective came
  from reading specification against code and from probes, never from apparatus repair). It
  also cannot be bounded the way §9 was — the new drafts would be fresh authorship with no
  committed blob to diff against, the least verifiable class of change (#15, #19). Rated
  against the ultimate objective: it spends derivation-phase capacity to keep a superseded gate
  warm, and buys the inference nothing.

**Alternative C — carve the colliding entries out of the discard; execute the remainder.**
Withhold from the discard every entry whose retirement moves anything outside the
decisions-register family (the entries homed in `cowork_structural_integrity_audit.md`, D-192,
and whatever else the enumeration finds), and execute the discard over the rest.

- *For.* No apparatus is touched at all; the reach question is deferred rather than decided;
  the bulk of the noise still leaves the live record.
- *Against, on the principles and the objective.* It keeps a class of entries live for no reason
  their content supplies — kept as authority-shaped record solely because superseded tooling
  reads them, which is observation-as-decision (the Ruling-8 shape) reintroduced by the back
  door, and #6 inverted: the apparatus dictating the record instead of deriving from it. The
  withheld class needs its own tracking (new apparatus for old apparatus), and the reach
  question returns undiminished the day those entries retire — this alternative pays C's costs
  now and A-or-B's costs later. Rated against the ultimate objective: the deriving sessions
  keep paying reading cost for entries everyone agrees nobody decided.

*Also considered and set aside rather than rated in full:* leaving the discard permanently
unexecuted (Alternative C at full width — every cost above at maximum, the ruled act simply not
performed); and hand-editing the reserved derivations' outputs to skip the halted documents
(forbidden outright — a hand-moved gate verdict is the act D-436 exists against, and no
alternative rests on it).

## 6. What ruling Alternative A would order (stated so the executing dispatch can quote it)

1. **The derived split first (R2's check).** The executing dispatch derives, publishes and
   commits the classification of every check the discard's application turns red: SUPERSEDED
   (serves only the old phase-1 gate) or STANDING (serves a rule of the current record), each
   member with its evidence. A member the derivation cannot place, and any STANDING member whose
   red the enumerated-movement bound cannot explain, STOPS to the user. R1's reader enumeration
   runs before anything freezes.
2. **The SUPERSEDED members move to the guard set's historical class** by an authored
   classification change committed with the act, their committed artifacts frozen in place as
   record (#12), never regenerated again; the close names every member. Historical status
   records that these checks graded a superseded program — it asserts NOTHING about whether that
   program's obligations were discharged, and no completion claim of any kind rides this ruling.
3. **The STANDING members are regenerated alongside the discard in the same commit**, under the
   bound that travels with the act: movement ONLY in values whose subject is a
   discard-population entry, or a document whose class/home standing those entries alone
   carried; every moved value enumerated in the close and diffed at explicit hashes; any other
   movement is a STOP-and-report.
4. **The mechanism work lands with the discard commit** — the retired block's own STOPs in the
   renderer, the establishment pass consulting the retired block beside the live entries
   (already measured working at 512/512), and F15's anchored-quote remap under the ordinary
   per-citation drift discipline (`gen_cluster_dispositions.py --verify` the authority, F3's
   reading rule standing).
5. **Untouched by this ruling:** the 29 withheld sole-carriers and the 62 (their surface awaits
   its own sitting); the eight KIND-UNDERIVABLE callers and the prose-citation question; the
   archiving wave; [[OI-179]], which gates under #19 independently of any phase apparatus;
   [[OI-372]] and [[OI-374]]; everything under `src/`, `tools/corpus/`, `tools/robust_stop/`,
   every golden and every test.

## 7. What this surface does NOT do, and must not be read as doing

Nothing here is ruled and nothing is executed. No entry is discarded, no check reclassified, no
artifact frozen, no file moved. The soft-discard's own ruling stands exactly as taken and is not
re-opened; the sole-carrier guard's 29 and the 62's results stand on their own surface awaiting
their own sitting. This surface proposes; the user rules; the executing dispatch performs — in
that order and no other.

*Provenance: the writing side (Cowork), 2026-08-16, drafted at the third preparation batch's
verified STOP, from `cc_report_preparation_third.md` (read in full), the batch's full close in
`cowork_away_returns.md` (read in full, proved by quotation at the twentieth handoff block's
successor session), the ruling records of 2026-08-15/16 (read in full), and `CLAUDE.md` (read in
full before drafting, per the twentieth handoff block's binding order).*

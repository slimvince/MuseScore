# User directions — 2026-08-15 (night): the repair is re-shaped to DERIVATION-FIRST; the artifact inventory comes before the phases

> **STATUS: RULING RECORD, an interim carrier (D-230).** Taken by the user in conversation on
> 2026-08-15, in a long design exchange following the July screen's falsification firing. **The
> classification of each item — decision, direction, or accepted proposal — is OWED and not made
> here.** The formal structure these directions imply is NOT ruled yet: it is ratified at the
> phase-definition surface, which the user directed comes AFTER the artifact inventory. **This
> record exists so the directions survive the session** — the eighteenth stop's founding failure,
> not repeated. Where the user's own words carry the direction, they are quoted verbatim; where
> the writing side proposed and the user accepted in sequence, that provenance is stated.

## 1. The reframing, and its relation to the eighteenth stop

The eighteenth stop's Ruling 10 made the repair **reconciliation, not rollback — pending a
pilot**: compare the pre-pollution baseline against the current text, judge each difference by
CHARACTER. **The user's direction tonight re-shapes the repair to DERIVATION-FIRST**: the design
work is re-done from clean sources, and the current text is demoted to one untrusted witness
among several. This extends Ruling 10's own character test to its limit rather than contradicting
it, and Ruling 10 was explicitly pending a pilot. **The formal supersession is recorded at the
phase-definition surface, not here.**

## 2. The directions

1. **DERIVATION-FIRST, OVER EVERY SPECIFICATION.** The user's words: *"go through EVERY spec,
   THINK and REDO the design work and then decide what changes are needed to each and every spec.
   While doing this, peek at older versions of the spec to mine any nuggets."* And: *"We REDO the
   ENTIRE design/architecture/algorithm/research/public algorithms again - but we start with a
   spec whose quality can not be assumed at all."*
2. **THE CLEAN ROOM.** The user's words: *"and while doing this - NEVER look at implementation."*
   Operationalized (writing side's proposal, accepted in sequence): the derivation may read **the
   world, never the mirror** — published research, ratified design-intent rulings, ground-truth
   corpora and their annotator conventions are admissible; our code, our outputs, our goldens and
   our measured behaviour are not. **Derive BEFORE comparing**: the derived statement and its
   defense are written before the current text or history is opened. Implementation descriptions
   found in current specifications are **QUARANTINED as audit questions, never absorbed as design
   input.** Deriving sessions boot from a **curated, implementation-free read list** — the user:
   `CLAUDE.md` *"is not immune to changes that are needed... can be replaced (temporarily(?))"*
   for those sessions.
3. **EVIDENCE IS INPUT, NEVER THE DECISION.** The user's words: *"others research AS WELL AS our
   own is valuable input - but not necessarily how we later decide to do it (for example there
   might be different competing algorithms/methods and we can therefore choose max one of them -
   or none)."* Per design point: candidates enumerated from both sources with establishment
   status; a choice made against the ultimate objective and the principles — **at most one per
   concern (#6), or NONE, stated as "underived — open, needs a ruling or new research"**; rivals
   recorded in the defense (the constrained-optimum ledger shape, #12).
4. **OUR OWN EXPERIMENTAL FINDINGS ENTER VIA AN EMPIRICAL FINDINGS LEDGER, THROUGH AN AIRLOCK.**
   Admission test: *does the fact survive the implementation being thrown away?* Entries are
   approach-level, implementation-stripped, each with provenance, uncertainty (#24) and
   establishment status (#19), and its failure diagnosis or "cause undiagnosed". A measured-worse
   verdict rules out the TRIED IMPLEMENTATION of an approach, not always the approach. **Both
   polarities carried** — the user: *"'bad ideas' are useful as 'antipatterns'"* — in two kinds:
   **design antipatterns** into the ledger; **process antipatterns** into the phase definitions'
   constraints and stop rules. Existing seeds: `DEFECT_TYPES.md`, `docs/scoring_model.md` §8, the
   refuted-repair register entries.
5. **TOP-DOWN: THE FRAMEWORK BEFORE THE DETAIL SPECS.** The user's ground: each layer spec
   depends on border decisions between layers, so the all-encompassing architecture framework is
   decided FIRST — the layer decomposition, each layer's charter (question answered, evidence
   consumed, facts published) and the boundary contracts — seeded by the ratified design-intent
   rulings (the joint estimator, option A, 2026-07-17, above all). Detail specs derive inside
   their charters; content found in the wrong layer parks on a **cross-layer transfer list**.
6. **THE DISPOSITION DISCIPLINE AT EVERY REPLACEMENT.** The user's words: *"If we remove
   something from a spec we must know where to move it to (unless it should be discarded)."*
   Every statement of an outgoing text reaches ONE recorded disposition — **adopted / relocated
   (transfer list) / quarantined (audit question) / discarded (worth test, with finding, date,
   reason) / historical** — completeness checked by arithmetic (the harvest-discharge precedent).
   **The open-items remapping onto the new structure is folded into this discipline** (user:
   "yes - in the disposition discipline").
7. **THE RESTRUCTURING PHASE IS SUPERSEDED BY CONSTRUCTION.** The framework phase decides the
   target structure, so derived specs are BORN one-home-per-concern; the unfinished
   reorganization of the old text is not completed. **The formal closure ruling is owed at the
   phase surface.** What survives with changed jobs: the candidate artifacts and the screen as
   the MINING MAP; the baseline tree at `b006dc15b5` as the most valuable single witness version;
   Ruling 13's row marking at full force; ordinary upkeep of the operational surfaces.
8. **THE PILOT IS PERMITTED WITH A BOUNDED OBJECTIVE.** The user's words: *"We can do a pilot if
   the objective is to prove the method and get some sizing facts."* Subject `docs/scoring_model.md`
   (the hardest clean-room case, low boundary exposure); output **QUARANTINED as provisional**
   until the framework rules the charters; deliverable a proposal per difference, never a rewrite
   (eighteenth-stop Ruling 11).
9. **PHASE DEFINITIONS CARRY MANDATORY HEADERS.** The user's four: purpose/objective;
   prerequisites (precondition) and inputs (artifacts); postcondition (result) and outputs
   (artifacts); constraints (not done vs not allowed). The writing side proposed ten more
   (completion test with verifier; roles and reserved acts; reading rules; stop rules and
   escalation; invalidation and re-entry; forward gating; watchers for constraints; progress
   measurement; record and handover requirements; amendment rule) — **adoption of the full set is
   NOT ruled**; the proposed keep-test: does the header's absence have a recorded failure?
10. **THE ARTIFACT INVENTORY COMES FIRST — BEFORE THE PHASES ARE DRAFTED.** The user's direction:
    understand what artifacts we have and decide how they should be used before drafting the
    phases. A DERIVED walk of the tree (never hand-listed), every file classified by mechanical
    signature into classes with an unclassified STOP; per class: role per phase, mining verdict
    (including antipattern mining), retirement-candidate flag. **Retirement destroys nothing
    (#12)**: archive-with-record, out of every phase's inputs. Verdicts are PROPOSED by the tool's
    surface and RULED by the user; the phases are then drafted citing ruled classes — *enumerate
    at the object, not from the row's list*, applied at program scale.
11. **POINT DIRECTIONS FROM THE SAME EXCHANGE.** The user's time is parked until the sizing
    exists. Only CC and the writing side edit `src/` — *"Still some mechanism might be needed
    just to make sure"*: the proposed tripwire (a recorded `src/` tree-hash pin checked in the
    guard set) is NOT yet ruled. The classification of tests, goldens and the catalogs
    (`chordanalyzer_catalog.musicxml`, the pipeline-snapshot goldens, `tools/robust_stop/`, the
    registries and `docs/score_inventory.md`) is decided at the inventory surface. Whether the
    measurement layer's own specifications are in the derivation's scope is an OPEN ruling.
    `cowork_*` design documents are NOT direct witnesses — their value is measured by what the
    curation acts extract (fact-based, not presumed). **Handover-safety is required at the latest
    by the next handover.**

## 3. What is NOT ruled, and what is OPEN — none of it to be assumed

**The re-opened period question is OPEN and is the user's next ruling.** The July screen's
falsification FIRED (one hunk POSITIVELY CODE-INFLUENCED, quoted whole at the top of
`tools/audit/july_screen_report.md`); the ruling owed is the **WIDTH of "influence"** (the narrow
operational reading is what keeps any period decidable) and the **instance verdict**. The writing
side's recommendation, on record and not ruled: the narrow width; the period stands at
`b006dc15b5`; the fired hunk and the fifteen not-cleared carried BY NAME into the examination
set. **No ruling was taken.**

Also not ruled: the formal phase structure and D-231's rephrasing (eighteenth-stop Rulings 6 and
7, now scheduled after the inventory); the restructuring closure; the header-set adoption; the
curated-boot exception to the mandatory session-start reads; the `src/` pin; the
measurement-layer scope; ratification granularity (parked until sizing). Not run: the register
filter, the intent-versus-implementation-management sort of the surviving rulings, the findings
ledger, the inventory. Standing and rowless: the third guard red (`gen_guard_classification.py`
stalled since 2026-08-13). `STATUS.md` remains unreadable as a mandatory read (OI-370).

*Provenance: Cowork, 2026-08-15, recorded at the session's close from the conversation of the
same night. The user's verbatim words are marked as such; everything else is the writing side's
operationalization, accepted in sequence and awaiting formal ratification at the phase surface.*
